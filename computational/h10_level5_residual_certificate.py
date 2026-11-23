"""Rebuild the H10 level-five correction from the pinned source definitions.

The C++17 engine mirrors the pinned graph, orientation, face-flux and SU(2)
operator definitions. It expands Tr(H_face^10)-Tr(H_Z^10) at levels 5 and 6
modulo three primes. This module reconstructs the integer coefficients using
signed CRT and an explicit path-count bound. The all-angle identity C10=D6-3D5
is Lean-checked; the coefficient expansion is an exact external certificate,
not a Lean-kernel theorem.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import tempfile

SOURCE_REPOSITORY = "https://github.com/RFT-SIRM/Evgeny-Theorem"
SOURCE_COMMIT = "4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f"
SOURCE_FILES = [
    "formalization/EvgenyTheorem/Graph/Sierpinski.lean",
    "formalization/EvgenyTheorem/Orientation.lean",
    "formalization/EvgenyTheorem/Graph/Faces.lean",
    "formalization/EvgenyTheorem/Operator.lean",
    "formalization/EvgenyTheorem/OpSplit1.lean",
    "formalization/EvgenyTheorem/SU2.lean",
    "formalization/EvgenyTheorem/FinalClosed10.lean",
]
RECURRENCE_THEOREM = "defectO10_succ_num_level5_constant_boundary_unconditional"
PRIMES = (10_000_453, 20_000_569, 30_000_769)
POLYNOMIAL = {
    "s^2": -748240, "c*s^2": 11036800, "s^3": 4927360,
    "c*s^3": -261920, "s^4": 330960, "c*s^4": 1920,
    "s^5": -3200, "c*s^5": 320, "s^6": 640,
}
FOURIER = {
    "1": [-249810, 0], "cos(u),sin(u)": [2759440, 3693520],
    "cos(2u),sin(2u)": [208340, -65430],
    "cos(3u),sin(3u)": [-2759560, -1230840],
    "cos(4u),sin(4u)": [41490, 32700],
    "cos(5u),sin(5u)": [120, -200],
    "cos(6u),sin(6u)": [-20, 10],
}
H4_EXPECTED = {1: -32, 2: -64, 3: -160, 4: -448, 5: -1312, 6: -3904}
D5_PI_EXPECTED, D6_PI_EXPECTED, C10_PI_EXPECTED = -2_505_633_280, -7_512_392_320, 4_507_520
GRAPH_COUNTS = {
    "vertices_m5": 366, "edges_m5": 729, "faces_m5": 243,
    "vertices_m6": 1095, "edges_m6": 2187, "faces_m6": 729,
}


def _compiler() -> list[str]:
    requested = os.environ.get("CXX")
    if requested:
        command = shlex.split(requested)
        if not command or shutil.which(command[0]) is None:
            raise RuntimeError(f"C++ compiler not found: {requested!r}")
        return command
    for name in ("clang++", "g++", "c++"):
        path = shutil.which(name)
        if path:
            return [path]
    raise RuntimeError("A C++17 compiler is required (Xcode Command Line Tools or g++).")


def crt_symmetric(residues: list[int], moduli: list[int], bound: int) -> int:
    if len(residues) != len(moduli) or not moduli:
        raise ValueError("CRT residue/modulus length mismatch")
    value, product = 0, 1
    for residue, prime in zip(residues, moduli):
        if not 0 <= residue < prime:
            raise ValueError(f"residue {residue} is not reduced modulo {prime}")
        value += product * (((residue - value) * pow(product, -1, prime)) % prime)
        product *= prime
    if product <= 2 * bound:
        raise AssertionError("CRT product does not exceed twice the coefficient bound")
    if value > product // 2:
        value -= product
    if abs(value) > bound:
        raise AssertionError(f"recovered coefficient {value} exceeds bound {bound}")
    return value


def reduce_cs(poly: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    out = {k: v for k, v in poly.items() if v}
    while any(a >= 2 for a, _ in out):
        (a, b), value = next((k, v) for k, v in out.items() if k[0] >= 2)
        del out[(a, b)]
        for key, delta in (((a - 2, b), value), ((a - 2, b + 2), -value)):
            out[key] = out.get(key, 0) + delta
            if out[key] == 0:
                del out[key]
    return out


def _fourier_to_cs() -> dict[tuple[int, int], int]:
    from math import comb
    modes = [(-249810, 0), (2759440, 3693520), (208340, -65430),
             (-2759560, -1230840), (41490, 32700), (120, -200), (-20, 10)]
    out: dict[tuple[int, int], int] = {}
    for k, (cos_coeff, sin_coeff) in enumerate(modes):
        for r in range(k + 1):
            value = (cos_coeff * (-1) ** (r // 2) if r % 2 == 0
                     else sin_coeff * (-1) ** ((r - 1) // 2)) * comb(k, r)
            out[(k - r, r)] = out.get((k - r, r), 0) + value
    return {k: v for k, v in out.items() if v}


def _labels(poly: dict[tuple[int, int], int]) -> dict[str, int]:
    labels = {
        (0, 2): "s^2", (1, 2): "c*s^2", (0, 3): "s^3",
        (1, 3): "c*s^3", (0, 4): "s^4", (1, 4): "c*s^4",
        (0, 5): "s^5", (1, 5): "c*s^5", (0, 6): "s^6",
    }
    return {labels[k]: v for k, v in sorted(poly.items()) if v}


def recompute() -> dict:
    source = Path(__file__).with_name("h10_level5_source_residual_certificate.cpp")
    if not source.is_file():
        raise FileNotFoundError(f"missing C++ source engine: {source}")
    with tempfile.TemporaryDirectory(prefix="h10-source-residual-") as tmp:
        binary = Path(tmp) / "h10_source_residual"
        subprocess.run(_compiler() + ["-std=c++17", "-O3", "-DNDEBUG", str(source), "-o", str(binary)],
                       check=True, capture_output=True, text=True, timeout=180)
        rows = []
        for prime in PRIMES:
            run = subprocess.run([str(binary), "--prime", str(prime)], check=True,
                                 capture_output=True, text=True, timeout=180)
            item = json.loads(run.stdout)
            if item.get("prime") != prime:
                raise AssertionError("C++ engine prime mismatch")
            rows.append(item)

    moduli = [int(x["prime"]) for x in rows]
    if tuple(moduli) != PRIMES or any(x["graph"] != GRAPH_COUNTS for x in rows):
        raise AssertionError("source prime sequence or graph counts mismatch")
    max_row_l1 = max(int(x["max_row_l1"]) for x in rows)
    max_degree = max(int(x["max_degree"]) for x in rows)
    if max_degree != 4:
        raise AssertionError(f"unexpected maximum vertex degree: {max_degree}")
    for item in rows:
        controls = {int(k): int(v) for k, v in item["h4_sanity"]}
        if controls != {k: v % int(item["prime"]) for k, v in H4_EXPECTED.items()}:
            raise AssertionError("H4 source controls failed")

    # For length ten, each trace coefficient is bounded by N*W^10.
    # C=D6-3D5 therefore has bound (2*N6+6*N5)*W^10.
    bound = (2 * 2190 + 6 * 732) * (max_row_l1 ** 10)
    product = 1
    for p in moduli:
        product *= p
    if product <= 2 * bound:
        raise AssertionError("three-prime CRT product is too small")

    raw: dict[tuple[int, int], int] = {}
    for a in range(11):
        for b in range(11 - a):
            real, imag = [], []
            for item in rows:
                entry = next(z for z in item["coefficients"] if int(z[0]) == a and int(z[1]) == b)
                real.append(int(entry[2])); imag.append(int(entry[3]))
            re = crt_symmetric(real, moduli, bound)
            im = crt_symmetric(imag, moduli, bound)
            if im:
                raise AssertionError(f"non-real coefficient at c^{a}s^{b}: {im}")
            if re:
                raw[(a, b)] = re
    canonical = reduce_cs(raw)
    polynomial = _labels(canonical)
    if polynomial != POLYNOMIAL or reduce_cs(_fourier_to_cs()) != canonical:
        raise AssertionError("source polynomial differs from canonical polynomial/Fourier certificate")

    def endpoint(field: str) -> int:
        return crt_symmetric([int(x[field]) for x in rows], moduli, bound)
    d5, d6, c10 = endpoint("D5_pi"), endpoint("D6_pi"), endpoint("C10_pi")
    if (d5, d6, c10) != (D5_PI_EXPECTED, D6_PI_EXPECTED, C10_PI_EXPECTED) or d6 - 3*d5 != c10:
        raise AssertionError("theta=pi endpoint or D6-3D5 identity mismatch")
    if canonical.get((0, 0), 0) != 0:
        raise AssertionError("C10(0) must vanish")
    at_pi = sum(v for (a, _), v in canonical.items() if a == 0)
    if at_pi != c10:
        raise AssertionError("polynomial endpoint disagrees with trace CRT")

    return {
        "source": {"repository": SOURCE_REPOSITORY, "commit": SOURCE_COMMIT,
                   "files": SOURCE_FILES, "recurrence_theorem": RECURRENCE_THEOREM,
                   "finite_identity": "C10^(5)(theta) = D6(theta) - 3*D5(theta)"},
        "method": "sparse exact polynomial path expansion modulo three primes, followed by coefficient-wise signed CRT",
        "primes": moduli, "crt_modulus_product": product,
        "coefficient_absolute_bound": bound, "max_row_l1": max_row_l1,
        "max_vertex_degree": max_degree, "graph_counts": GRAPH_COUNTS,
        "H4_source_controls": {str(k): v for k, v in H4_EXPECTED.items()},
        "D5_pi": d5, "D6_pi": d6, "C10_pi": c10,
        "raw_C10_polynomial": {f"c^{a}*s^{b}": v for (a, b), v in sorted(raw.items())},
        "polynomial": polynomial, "fourier": FOURIER,
        "evidence_scope": ("The finite level-five/six trace expansion is reconstructed from the pinned graph, orientation, flux, and SU(2) definitions by an exact external modular/CRT computation. The all-angle recurrence identifying the level-five residual with D6-3D5 is Lean-checked. The coefficient expansion itself is not a Lean-kernel theorem."),
        "status": "SOURCE_RECONSTRUCTED_EXACT_EXTERNAL_CRT_CERTIFICATE",
    }


def verify(payload: dict | None = None) -> dict:
    if payload is None:
        path = Path(__file__).parent / "data" / "h10_level5_residual_certificate.json"
        payload = json.loads(path.read_text())
    if payload.get("status") != "SOURCE_RECONSTRUCTED_EXACT_EXTERNAL_CRT_CERTIFICATE":
        raise AssertionError("H10 artifact is not marked as source-reconstructed")
    if payload.get("source", {}).get("commit") != SOURCE_COMMIT:
        raise AssertionError("H10 source pin mismatch")
    if payload.get("polynomial") != POLYNOMIAL or payload.get("fourier") != FOURIER:
        raise AssertionError("H10 polynomial or Fourier coefficients differ")
    if (payload.get("D5_pi"), payload.get("D6_pi"), payload.get("C10_pi")) != (D5_PI_EXPECTED, D6_PI_EXPECTED, C10_PI_EXPECTED):
        raise AssertionError("H10 endpoint values differ")
    if payload["D6_pi"] - 3 * payload["D5_pi"] != payload["C10_pi"]:
        raise AssertionError("H10 endpoint recurrence fails")
    if payload.get("crt_modulus_product", 0) <= 2 * payload.get("coefficient_absolute_bound", 0):
        raise AssertionError("H10 CRT modulus is not larger than twice the bound")
    if payload.get("graph_counts") != GRAPH_COUNTS:
        raise AssertionError("H10 source graph counts differ")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild H10 finite traces from pinned Lean source definitions and CRT them.")
    parser.add_argument("--output", help="write exact certificate JSON to this path")
    parser.add_argument("--check-only", action="store_true", help="check committed JSON without compiling C++")
    args = parser.parse_args()
    result = verify() if args.check_only else recompute()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        path = Path(args.output); path.parent.mkdir(parents=True, exist_ok=True); path.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
