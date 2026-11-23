"""Exact finite-level H12 residual comparison by source-mirrored modular CRT.

This is an external exact computation, not a Lean-kernel theorem.  It builds
levels 3--6 from the pinned graph/operator definitions, computes the twelfth
trace moment over three primes, reconstructs all coefficients with signed CRT,
and compares C12_m = D12_(m+1) - 3 D12_m for m=3,4,5.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import tempfile
from collections import defaultdict

SOURCE_REPOSITORY = "https://github.com/RFT-SIRM/Evgeny-Theorem"
SOURCE_COMMIT = "4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f"
SOURCE_FILES = [
    "formalization/EvgenyTheorem/Graph/Sierpinski.lean",
    "formalization/EvgenyTheorem/Orientation.lean",
    "formalization/EvgenyTheorem/Graph/Faces.lean",
    "formalization/EvgenyTheorem/Operator.lean",
    "formalization/EvgenyTheorem/OpSplit1.lean",
    "formalization/EvgenyTheorem/SU2.lean",
]
MOMENT = 12
LEVELS = (3, 4, 5, 6)
PRIMES = (10_000_453, 20_000_569, 30_000_769)
GRAPH_COUNTS = {
    3: {"vertices": 42, "edges": 81, "faces": 27},
    4: {"vertices": 123, "edges": 243, "faces": 81},
    5: {"vertices": 366, "edges": 729, "faces": 243},
    6: {"vertices": 1095, "edges": 2187, "faces": 729},
}
EXPECTED_REDUCED = {
    (0, 2): -945325824,
    (0, 3): 208608384,
    (0, 4): 102067392,
    (0, 5): -18816,
    (0, 6): 565760,
    (0, 7): 29184,
    (0, 8): 384,
    (1, 2): 1186927488,
    (1, 3): -36718464,
    (1, 4): -2090112,
    (1, 5): 158592,
    (1, 6): -15360,
    (1, 7): -384,
}
EXPECTED_FOURIER = {
    "constant": -434210735,
    "cos(1u)": 296469408, "sin(1u)": 156460488,
    "cos(2u)": 421363848, "sin(2u)": -9154878,
    "cos(3u)": -296337816, "sin(3u)": -52155792,
    "cos(4u)": 12864588, "sin(4u)": 4570026,
    "cos(5u)": -131832, "sin(5u)": 2016,
    "cos(6u)": -17704, "sin(6u)": 4938,
    "cos(7u)": 240, "sin(7u)": -456,
    "cos(8u)": 3, "sin(8u)": 3,
}
EXPECTED_D_PI = {
    3: -18026705824,
    4: -54714191008,
    5: -164776646560,
    6: -494964013216,
}
EXPECTED_C_PI = -634073536


def _compiler() -> list[str]:
    requested = os.environ.get("CXX")
    if requested:
        command = shlex.split(requested)
        if not command or shutil.which(command[0]) is None:
            raise RuntimeError(f"C++ compiler not found: {requested!r}")
        return command
    for name in ("g++", "clang++", "c++"):
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
    """Canonical remainder under c^2 = 1 - s^2, with c-degree at most one."""
    out = {k: v for k, v in poly.items() if v}
    while any(a >= 2 for a, _ in out):
        (a, b), value = next((k, v) for k, v in out.items() if k[0] >= 2)
        del out[(a, b)]
        for key, delta in (((a - 2, b), value), ((a - 2, b + 2), -value)):
            out[key] = out.get(key, 0) + delta
            if out[key] == 0:
                del out[key]
    return dict(sorted(out.items()))


def _cmul(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def _power_terms(terms: dict[int, tuple[Fraction, Fraction]], n: int):
    out = {0: (Fraction(1), Fraction(0))}
    for _ in range(n):
        nxt = defaultdict(lambda: (Fraction(0), Fraction(0)))
        for k, value in out.items():
            for j, factor in terms.items():
                product = _cmul(value, factor)
                old = nxt[k + j]
                nxt[k + j] = (old[0] + product[0], old[1] + product[1])
        out = dict(nxt)
    return out


def polynomial_to_fourier(poly: dict[tuple[int, int], int]) -> dict[str, int]:
    """Convert c^a s^b to an exact Fourier series using z=exp(iu)."""
    c_terms = {1: (Fraction(1, 2), Fraction(0)), -1: (Fraction(1, 2), Fraction(0))}
    # sin(u) = (z - z^-1)/(2i) = -i z/2 + i z^-1/2.
    s_terms = {1: (Fraction(0), Fraction(-1, 2)), -1: (Fraction(0), Fraction(1, 2))}
    q = defaultdict(lambda: (Fraction(0), Fraction(0)))
    for (a, b), coefficient in poly.items():
        cp = _power_terms(c_terms, a)
        sp = _power_terms(s_terms, b)
        for k, cv in cp.items():
            for j, sv in sp.items():
                product = _cmul(cv, sv)
                old = q[k + j]
                q[k + j] = (old[0] + coefficient * product[0], old[1] + coefficient * product[1])
    result = {"constant": int(q[0][0])}
    if q[0][1] != 0:
        raise AssertionError("Fourier constant is not real")
    max_mode = max((abs(k) for k in q), default=0)
    for k in range(1, max_mode + 1):
        re, im = q[k]
        if q[-k] != (re, -im):
            raise AssertionError(f"Fourier reality condition failed at mode {k}")
        A, B = 2 * re, -2 * im
        if A.denominator != 1 or B.denominator != 1:
            raise AssertionError("Fourier coefficients are not integers")
        if A:
            result[f"cos({k}u)"] = int(A)
        if B:
            result[f"sin({k}u)"] = int(B)
    return result


def _evaluate_fourier_at_zero(fourier: dict[str, int]) -> int:
    return fourier["constant"] + sum(v for k, v in fourier.items() if k.startswith("cos(") and k != "cos(0u)")


def _evaluate_fourier_at_half_pi(fourier: dict[str, int]) -> int:
    value = fourier["constant"]
    cos_values = (1, 0, -1, 0)
    sin_values = (0, 1, 0, -1)
    for k, v in fourier.items():
        if k == "constant":
            continue
        mode = int(k[k.index("(") + 1:k.index("u)")])
        if k.startswith("cos("):
            value += v * cos_values[mode % 4]
        else:
            value += v * sin_values[mode % 4]
    return value


def _reconstruct(raw_rows: list[dict]) -> dict:
    primes = [int(row["prime"]) for row in raw_rows]
    if tuple(primes) != PRIMES:
        raise AssertionError("unexpected prime sequence")
    if any(row["max_degree"] != 4 for row in raw_rows):
        raise AssertionError("unexpected maximum graph degree")
    max_row_l1 = max(int(row["max_row_l1"]) for row in raw_rows)
    if max_row_l1 != 10:
        raise AssertionError(f"unexpected maximum row coefficient l1 norm: {max_row_l1}")
    for row in raw_rows:
        for m, counts in GRAPH_COUNTS.items():
            if f"m{m}" not in row["levels"]:
                raise AssertionError(f"missing graph level {m}")
            got = {k: row["levels"][f"m{m}"][k] for k in ("vertices", "edges", "faces")}
            if got != counts:
                raise AssertionError(f"source graph counts differ at level {m}: {got}")

    state_counts = {m: 2 * GRAPH_COUNTS[m]["vertices"] for m in LEVELS}
    bounds = {
        m: (2 * state_counts[m + 1] + 6 * state_counts[m]) * (max_row_l1 ** MOMENT)
        for m in (3, 4, 5)
    }
    max_bound = max(bounds.values())
    modulus_product = 1
    for prime in primes:
        modulus_product *= prime
    if modulus_product <= 2 * max_bound:
        raise AssertionError("CRT modulus product is too small for the coefficient bound")

    residuals = {}
    for m in (3, 4, 5):
        coeff_arrays = [row["residuals"][f"C{m}"]["coefficients"] for row in raw_rows]
        raw_poly: dict[tuple[int, int], int] = {}
        for a in range(MOMENT + 1):
            for b in range(MOMENT + 1 - a):
                residues_re, residues_im = [], []
                for array in coeff_arrays:
                    item = next(x for x in array if x[0] == a and x[1] == b)
                    residues_re.append(int(item[2]))
                    residues_im.append(int(item[3]))
                real = crt_symmetric(residues_re, primes, bounds[m])
                imag = crt_symmetric(residues_im, primes, bounds[m])
                if imag:
                    raise AssertionError(f"non-real H12 coefficient at c^{a}s^{b}: {imag}")
                if real:
                    raw_poly[(a, b)] = real
        reduced = reduce_cs(raw_poly)
        fourier = polynomial_to_fourier(reduced)
        c_pi_from_poly = sum(v for (a, b), v in reduced.items() if a == 0)
        c_zero_from_poly = sum(v for (a, b), v in reduced.items() if b == 0)
        for row, prime in zip(raw_rows, primes):
            if c_pi_from_poly % prime != row["residuals"][f"C{m}"]["C_pi"]:
                raise AssertionError(f"theta=pi modular endpoint mismatch for C{m} mod {prime}")
        if c_zero_from_poly != 0:
            raise AssertionError(f"C{m}(0) is not zero: {c_zero_from_poly}")
        if _evaluate_fourier_at_zero(fourier) != 0:
            raise AssertionError(f"Fourier C{m}(0) mismatch")
        if _evaluate_fourier_at_half_pi(fourier) != c_pi_from_poly:
            raise AssertionError(f"Fourier C{m}(pi) mismatch")
        residuals[m] = {
            "raw_coefficients": raw_poly,
            "reduced_coefficients": reduced,
            "fourier": fourier,
            "at_theta_zero": c_zero_from_poly,
            "at_theta_pi": c_pi_from_poly,
        }

    if not (residuals[3]["reduced_coefficients"] == residuals[4]["reduced_coefficients"] == residuals[5]["reduced_coefficients"]):
        raise AssertionError("H12 transition residuals differ across levels 3, 4, 5")
    common_poly = residuals[3]["reduced_coefficients"]
    common_fourier = residuals[3]["fourier"]
    if common_poly != EXPECTED_REDUCED or common_fourier != EXPECTED_FOURIER:
        raise AssertionError("H12 exact polynomial or Fourier expression changed")
    if residuals[3]["at_theta_pi"] != EXPECTED_C_PI:
        raise AssertionError("H12 theta=pi endpoint mismatch")

    d_pi = {}
    for m in LEVELS:
        bound = 2 * state_counts[m] * (max_row_l1 ** MOMENT)
        residues = [int(row["levels"][f"m{m}"]["D_pi"]) for row in raw_rows]
        d_pi[m] = crt_symmetric(residues, primes, bound)
    for m in (3, 4, 5):
        if d_pi[m + 1] - 3 * d_pi[m] != EXPECTED_C_PI:
            raise AssertionError(f"D_{m+1}-3D_{m} endpoint does not match C12")
    if d_pi != EXPECTED_D_PI:
        raise AssertionError("H12 level endpoint values differ")

    return {
        "status": "EXACT_EXTERNAL_CRT_FINITE_LEVEL_H12_RESIDUALS",
        "moment": MOMENT,
        "source": {
            "repository": SOURCE_REPOSITORY,
            "commit": SOURCE_COMMIT,
            "files": SOURCE_FILES,
            "definition": "D_m^(12) = Tr(H_face(m)^12) - Tr(H_Z(m)^12)",
            "finite_identity": "C12^(m) = D_(m+1)^(12) - 3*D_m^(12)",
        },
        "levels_computed": list(LEVELS),
        "transitions_compared": [3, 4, 5],
        "graph_counts": {str(m): GRAPH_COUNTS[m] for m in LEVELS},
        "max_graph_degree": 4,
        "max_row_coefficient_l1": max_row_l1,
        "primes": primes,
        "crt_modulus_product": modulus_product,
        "coefficient_bound_by_transition": {str(k): v for k, v in bounds.items()},
        "twice_max_coefficient_bound": 2 * max_bound,
        "crt_uniqueness_margin_ratio": modulus_product // (2 * max_bound),
        "D_m_at_theta_pi": {str(k): v for k, v in d_pi.items()},
        "common_reduced_polynomial": {f"c^{a}s^{b}": v for (a, b), v in common_poly.items()},
        "common_fourier": common_fourier,
        "residuals": {
            str(m): {
                "at_theta_zero": residuals[m]["at_theta_zero"],
                "at_theta_pi": residuals[m]["at_theta_pi"],
                "reduced_polynomial": {f"c^{a}s^{b}": v for (a, b), v in residuals[m]["reduced_coefficients"].items()},
                "fourier": residuals[m]["fourier"],
            }
            for m in (3, 4, 5)
        },
        "comparisons": {
            "C12_3_equals_C12_4": True,
            "C12_4_equals_C12_5": True,
            "C12_3_equals_C12_5": True,
        },
        "evidence_boundary": (
            "This certificate proves exact equality of the three finite transition residuals m=3,4,5, "
            "from the pinned source-mirrored graph/operator matrices. It does not prove the recurrence "
            "for every level, and it is not a Lean-kernel theorem. An all-level H12 boundary/locality "
            "argument and Lean formalization remain open."
        ),
    }


def recompute() -> dict:
    source = Path(__file__).with_name("h12_residual_engine.cpp")
    if not source.is_file():
        raise FileNotFoundError(f"missing C++ source engine: {source}")
    with tempfile.TemporaryDirectory(prefix="h12-source-residual-") as tmp:
        binary = Path(tmp) / "h12_source_residual"
        subprocess.run(
            _compiler() + ["-std=c++17", "-O3", "-DNDEBUG", str(source), "-o", str(binary)],
            check=True, capture_output=True, text=True, timeout=180,
        )
        rows = []
        for prime in PRIMES:
            run = subprocess.run(
                [str(binary), "--prime", str(prime)],
                check=True, capture_output=True, text=True, timeout=180,
            )
            rows.append(json.loads(run.stdout))
    return _reconstruct(rows)


def verify(payload: dict | None = None) -> dict:
    if payload is None:
        path = Path(__file__).parent / "data" / "h12_residual_certificate.json"
        payload = json.loads(path.read_text())
    if payload.get("status") != "EXACT_EXTERNAL_CRT_FINITE_LEVEL_H12_RESIDUALS":
        raise AssertionError("H12 artifact status marker mismatch")
    if payload.get("moment") != MOMENT or payload.get("source", {}).get("commit") != SOURCE_COMMIT:
        raise AssertionError("H12 moment/source pin mismatch")
    if payload.get("primes") != list(PRIMES):
        raise AssertionError("H12 prime set mismatch")
    if payload.get("crt_modulus_product", 0) <= payload.get("twice_max_coefficient_bound", 0):
        raise AssertionError("H12 CRT uniqueness bound fails")
    if payload.get("common_reduced_polynomial") != {f"c^{a}s^{b}": v for (a, b), v in EXPECTED_REDUCED.items()}:
        raise AssertionError("H12 reduced polynomial mismatch")
    if payload.get("common_fourier") != EXPECTED_FOURIER:
        raise AssertionError("H12 Fourier coefficients mismatch")
    if payload.get("D_m_at_theta_pi") != {str(k): v for k, v in EXPECTED_D_PI.items()}:
        raise AssertionError("H12 finite-level endpoint values mismatch")
    if payload.get("levels_computed") != list(LEVELS) or payload.get("transitions_compared") != [3, 4, 5]:
        raise AssertionError("H12 level/transition scope mismatch")
    expected_bounds = {"3": 996_000_000_000_000, "4": 2_940_000_000_000_000, "5": 8_772_000_000_000_000}
    if payload.get("coefficient_bound_by_transition") != expected_bounds:
        raise AssertionError("H12 coefficient bound metadata mismatch")
    expected_poly = {f"c^{a}s^{b}": value for (a, b), value in EXPECTED_REDUCED.items()}
    for m in (3, 4, 5):
        item = payload.get("residuals", {}).get(str(m), {})
        if item.get("reduced_polynomial") != expected_poly or item.get("fourier") != EXPECTED_FOURIER:
            raise AssertionError(f"H12 transition C12_{m} coefficient mismatch")
        if item.get("at_theta_zero") != 0 or item.get("at_theta_pi") != EXPECTED_C_PI:
            raise AssertionError(f"H12 transition C12_{m} endpoint mismatch")
    if payload.get("comparisons") != {
        "C12_3_equals_C12_4": True,
        "C12_4_equals_C12_5": True,
        "C12_3_equals_C12_5": True,
    }:
        raise AssertionError("H12 finite transition comparison mismatch")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Reconstruct finite H12 transition residuals by exact modular CRT.")
    parser.add_argument("--output", help="write reconstructed certificate JSON")
    parser.add_argument("--check-only", action="store_true", help="check committed JSON without compiling C++")
    args = parser.parse_args()
    result = verify() if args.check_only else recompute()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
