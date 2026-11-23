"""Incrementally extend the exact H12 CRT certificate from level 7 to level 8.

The four previously checked transitions (m=3,4,5,6) are retained verbatim from
the level-7 certificate. This engine computes only D_7 and D_8 from the pinned
source-mirrored graph/operator matrices, then reconstructs the new transition
C_12^(7)=D_8-3D_7 over three primes by signed CRT.
"""
from __future__ import annotations

import argparse
import hashlib
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import tempfile

SOURCE_REPOSITORY = "https://github.com/RFT-SIRM/Evgeny-Theorem"
SOURCE_COMMIT = "4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f"
MOMENT = 12
LEVELS = (3, 4, 5, 6, 7, 8)
TRANSITIONS = (3, 4, 5, 6, 7)
NEW_TRANSITION = 7
PRIMES = (10_000_453, 20_000_569, 30_000_769)
GRAPH_COUNTS = {
    7: {"vertices": 3282, "edges": 6561, "faces": 2187},
    8: {"vertices": 9843, "edges": 19683, "faces": 6561},
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
    7: -1485526113184,
    8: -4457212413088,
}
EXPECTED_C_PI = -634073536
ROW_L1_BOUND = 10
CANONICAL_REDUCTION_FACTOR = 64
EXPECTED_BASE_SHA256 = "57a91fba36ae14dad80b52b97ec7844cbcf38ba2dbc3d5d25e52c9b5c6af57a7"
ENGINE_SHA256 = "e6c85ae166070b0499cd3232fae8a94fc7b2e219de2c578a5b74886f374a506f"
RAW_PRIME_SHA256 = {
    10_000_453: "ef09a30154e5158632c90478143879f259dd7979b8958936faac8a5ee4bf3e5d",
    20_000_569: "56aa9c6534626015b029d42e9e44b91b854bd3ae30112d74f6e9a68934815858",
    30_000_769: "19946c7fd608b22bfe2611a98961c347b35bc0e6d13b442d583f9d8799073411",
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


def math_product(values: list[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


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
    c_terms = {1: (Fraction(1, 2), Fraction(0)), -1: (Fraction(1, 2), Fraction(0))}
    s_terms = {1: (Fraction(0), Fraction(-1, 2)), -1: (Fraction(0), Fraction(1, 2))}
    q = defaultdict(lambda: (Fraction(0), Fraction(0)))
    for (a, b), coefficient in poly.items():
        cp, sp = _power_terms(c_terms, a), _power_terms(s_terms, b)
        for k, cv in cp.items():
            for j, sv in sp.items():
                product = _cmul(cv, sv)
                old = q[k + j]
                q[k + j] = (old[0] + coefficient * product[0], old[1] + coefficient * product[1])
    if q[0][1] != 0:
        raise AssertionError("Fourier constant is not real")
    result = {"constant": int(q[0][0])}
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
    return fourier["constant"] + sum(v for k, v in fourier.items() if k.startswith("cos("))


def _evaluate_fourier_at_half_pi(fourier: dict[str, int]) -> int:
    value = fourier["constant"]
    for key, coefficient in fourier.items():
        if key == "constant":
            continue
        mode = int(key[key.index("(") + 1:key.index("u)")])
        if key.startswith("cos("):
            value += coefficient * (1 if mode % 4 == 0 else -1 if mode % 4 == 2 else 0)
        else:
            value += coefficient * (1 if mode % 4 == 1 else -1 if mode % 4 == 3 else 0)
    return value


def _level_coefficients(item: dict, prime: int) -> dict[tuple[int, int], tuple[int, int]]:
    out = {}
    for a, b, re, im in item["coefficients"]:
        key = (int(a), int(b))
        if key in out:
            raise AssertionError(f"duplicate polynomial coefficient {key}")
        out[key] = (int(re) % prime, int(im) % prime)
    expected = {(a, b) for a in range(2) for b in range(MOMENT + 1 - a)}
    if set(out) != expected:
        raise AssertionError("reduced polynomial coefficient basis is incomplete")
    return out


def _check_level7_base(base: dict) -> None:
    if base.get("levels_computed") != [3, 4, 5, 6, 7]:
        raise AssertionError("baseline H12 certificate is not the verified level-7 artifact")
    if base.get("transitions_compared") != [3, 4, 5, 6]:
        raise AssertionError("baseline H12 certificate has unexpected transition scope")
    if base.get("source", {}).get("commit") != SOURCE_COMMIT:
        raise AssertionError("baseline H12 source pin mismatch")
    if base.get("D_m_at_theta_pi", {}).get("7") != EXPECTED_D_PI[7]:
        raise AssertionError("baseline H12 level-seven endpoint mismatch")
    if base.get("common_reduced_polynomial") != {f"c^{a}s^{b}": v for (a, b), v in EXPECTED_REDUCED.items()}:
        raise AssertionError("baseline H12 polynomial mismatch")
    if base.get("common_fourier") != EXPECTED_FOURIER:
        raise AssertionError("baseline H12 Fourier expression mismatch")
    if base.get("crt_modulus_product") != math_product(list(PRIMES)):
        raise AssertionError("baseline H12 CRT modulus mismatch")


def _extend_certificate(base: dict, raw_rows: list[dict]) -> dict:
    _check_level7_base(base)
    primes = [int(row["prime"]) for row in raw_rows]
    if tuple(primes) != PRIMES:
        raise AssertionError(f"unexpected source prime sequence: {primes}")
    if any(int(row["max_graph_degree"]) != 4 for row in raw_rows):
        raise AssertionError("unexpected graph degree")
    max_row_l1 = max(int(row["max_row_coefficient_l1"]) for row in raw_rows)
    if max_row_l1 != ROW_L1_BOUND:
        raise AssertionError(f"unexpected row coefficient l1 norm: {max_row_l1}")

    for row in raw_rows:
        if set(row["levels"]) != {"m7", "m8"}:
            raise AssertionError("the extension engine must return exactly levels 7 and 8")
        for m in (7, 8):
            got = row["levels"][f"m{m}"]
            counts = {key: int(got[key]) for key in ("vertices", "edges", "faces")}
            if counts != GRAPH_COUNTS[m]:
                raise AssertionError(f"source graph counts differ at level {m}: {counts}")

    states7 = 2 * GRAPH_COUNTS[7]["vertices"]
    states8 = 2 * GRAPH_COUNTS[8]["vertices"]
    raw_bound = (2 * states8 + 6 * states7) * (max_row_l1 ** MOMENT)
    canonical_bound = raw_bound * CANONICAL_REDUCTION_FACTOR
    modulus_product = math_product(primes)
    twice_max_bound = max(
        int(base["twice_max_canonical_coefficient_bound"]),
        2 * canonical_bound,
    )
    if modulus_product <= twice_max_bound:
        raise AssertionError("CRT modulus product is too small for the level-seven canonical coefficient bound")

    level_polys = []
    residues_pi_hi = []
    residues_pi_lo = []
    for row, prime in zip(raw_rows, primes):
        levels = row["levels"]
        level_polys.append({
            7: _level_coefficients(levels["m7"], prime),
            8: _level_coefficients(levels["m8"], prime),
        })
        residues_pi_hi.append(int(levels["m8"]["D_pi"]))
        residues_pi_lo.append(int(levels["m7"]["D_pi"]))

    poly: dict[tuple[int, int], int] = {}
    for a in range(2):
        for b in range(MOMENT + 1 - a):
            rr, ii = [], []
            for item, prime in zip(level_polys, primes):
                hi_re, hi_im = item[8][(a, b)]
                lo_re, lo_im = item[7][(a, b)]
                rr.append((hi_re - 3 * lo_re) % prime)
                ii.append((hi_im - 3 * lo_im) % prime)
            real = crt_symmetric(rr, primes, canonical_bound)
            imag = crt_symmetric(ii, primes, canonical_bound)
            if imag:
                raise AssertionError(f"non-real H12 coefficient at C7, c^{a}s^{b}: {imag}")
            if real:
                poly[(a, b)] = real

    fourier = polynomial_to_fourier(poly)
    c_zero = poly.get((0, 0), 0) + poly.get((1, 0), 0)
    c_pi = sum(value for (a, _), value in poly.items() if a == 0)
    if poly != EXPECTED_REDUCED or fourier != EXPECTED_FOURIER:
        raise AssertionError("level-seven transition differs from the established H12 polynomial")
    if c_zero != 0 or c_pi != EXPECTED_C_PI or _evaluate_fourier_at_zero(fourier) != 0:
        raise AssertionError("level-seven transition endpoint mismatch")
    if _evaluate_fourier_at_half_pi(fourier) != EXPECTED_C_PI:
        raise AssertionError("level-seven Fourier endpoint mismatch")

    d7_bound = 2 * states7 * (max_row_l1 ** MOMENT)
    d8_bound = 2 * states8 * (max_row_l1 ** MOMENT)
    d7 = crt_symmetric(residues_pi_lo, primes, d7_bound)
    d8 = crt_symmetric(residues_pi_hi, primes, d8_bound)
    if d7 != EXPECTED_D_PI[7] or d8 != EXPECTED_D_PI[8]:
        raise AssertionError("level-seven/eight theta=pi endpoint reconstruction mismatch")
    if d8 - 3 * d7 != EXPECTED_C_PI:
        raise AssertionError("D8(pi)-3D7(pi) does not match C12(pi)")

    result = deepcopy(base)
    result["levels_computed"] = list(LEVELS)
    result["transitions_compared"] = list(TRANSITIONS)
    result["graph_counts"]["8"] = GRAPH_COUNTS[8]
    result["D_m_at_theta_pi"]["8"] = d8
    result["raw_path_l1_bound_by_transition"]["7"] = raw_bound
    result["canonical_coefficient_bound_by_transition"]["7"] = canonical_bound
    result["twice_max_canonical_coefficient_bound"] = twice_max_bound
    result["crt_uniqueness_margin_ratio"] = modulus_product // twice_max_bound
    result["residuals"]["7"] = {
        "at_theta_zero": c_zero,
        "at_theta_pi": c_pi,
        "reduced_polynomial": {f"c^{a}s^{b}": v for (a, b), v in sorted(poly.items())},
        "fourier": fourier,
    }
    result["comparisons"].pop("all_four_finite_transitions_equal", None)
    result["comparisons"]["C12_6_equals_C12_7"] = True
    result["comparisons"]["all_five_finite_transitions_equal"] = True
    result["evidence_boundary"] = (
        "This certificate proves exact equality of five finite transition residuals, m=3,4,5,6,7, "
        "from the pinned source-mirrored graph/operator matrices. The level-7-to-8 extension was "
        "reconstructed over three prime fields and joined to the verified level-3--7 certificate. "
        "It does not prove the recurrence for every graph level, and it is not a Lean-kernel theorem. "
        "A uniform radius-five corner-transport argument and degree-12 boundary expansion remain open."
    )
    result["incremental_extension"] = {
        "base_certificate": "computational/data/h12_level7_residual_certificate.json",
        "base_certificate_sha256": EXPECTED_BASE_SHA256,
        "new_transition": "C12^(7)=D8^(12)-3*D7^(12)",
        "new_levels_computed_from_source": [7, 8],
        "engine_sha256": ENGINE_SHA256,
        "raw_modular_data": {
            str(p): f"computational/data/h12_level8_raw_modular/prime_{p}.json" for p in PRIMES
        },
    }
    return result


def _read_cached_rows(here: Path) -> list[dict]:
    rows = []
    for prime in PRIMES:
        path = here / "data" / "h12_level8_raw_modular" / f"prime_{prime}.json"
        if not path.is_file():
            raise FileNotFoundError(f"missing level-8 raw modular output: {path}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != RAW_PRIME_SHA256[prime]:
            raise AssertionError(f"raw level-8 modular output hash mismatch for prime {prime}")
        rows.append(json.loads(path.read_text()))
    return rows


def recompute(use_cached_prime_data: bool = False) -> dict:
    here = Path(__file__).parent
    base_path = here / "data" / "h12_level7_residual_certificate.json"
    if not base_path.is_file():
        raise FileNotFoundError(f"missing prior exact level-7 certificate: {base_path}")
    if hashlib.sha256(base_path.read_bytes()).hexdigest() != EXPECTED_BASE_SHA256:
        raise AssertionError("prior level-7 certificate does not match the expected verified artifact")
    base = json.loads(base_path.read_text())
    source = here / "h12_residual_engine.cpp"
    if hashlib.sha256(source.read_bytes()).hexdigest() != ENGINE_SHA256:
        raise AssertionError("level-8 C++ engine does not match the source used for the stored prime runs")
    cached_rows = _read_cached_rows(here)
    if use_cached_prime_data:
        rows = cached_rows
    else:
        with tempfile.TemporaryDirectory(prefix="h12-level8-extension-") as tmp:
            binary = Path(tmp) / "h12_level8_source_residual"
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
                row = json.loads(run.stdout)
                rows.append(row)
        if rows != cached_rows:
            raise AssertionError("fresh C++ level-7/8 runs differ from the recorded three-prime raw outputs")
    return _extend_certificate(base, rows)


def verify(payload: dict | None = None) -> dict:
    if payload is None:
        path = Path(__file__).parent / "data" / "h12_residual_certificate.json"
        payload = json.loads(path.read_text())
    if payload.get("status") != "EXACT_EXTERNAL_CRT_FINITE_LEVEL_H12_RESIDUALS":
        raise AssertionError("H12 certificate status mismatch")
    if payload.get("moment") != MOMENT or payload.get("source", {}).get("commit") != SOURCE_COMMIT:
        raise AssertionError("H12 source pin or moment mismatch")
    if payload.get("levels_computed") != list(LEVELS) or payload.get("transitions_compared") != list(TRANSITIONS):
        raise AssertionError("H12 finite-level scope mismatch")
    if payload.get("primes") != list(PRIMES):
        raise AssertionError("H12 prime sequence mismatch")
    if payload.get("max_graph_degree") != 4 or payload.get("max_row_coefficient_l1") != ROW_L1_BOUND:
        raise AssertionError("H12 graph/row-norm metadata mismatch")
    if payload.get("common_reduced_polynomial") != {f"c^{a}s^{b}": v for (a, b), v in EXPECTED_REDUCED.items()}:
        raise AssertionError("H12 reduced polynomial mismatch")
    if payload.get("common_fourier") != EXPECTED_FOURIER:
        raise AssertionError("H12 Fourier expression mismatch")
    if payload.get("D_m_at_theta_pi") != {str(k): v for k, v in EXPECTED_D_PI.items()}:
        raise AssertionError("H12 endpoint values mismatch")
    if payload.get("comparisons") != {
        "C12_3_equals_C12_4": True,
        "C12_4_equals_C12_5": True,
        "C12_5_equals_C12_6": True,
        "C12_6_equals_C12_7": True,
        "all_five_finite_transitions_equal": True,
    }:
        raise AssertionError("H12 transition comparison mismatch")
    if payload.get("crt_modulus_product") != math_product(list(PRIMES)):
        raise AssertionError("H12 CRT modulus product mismatch")
    raw_bounds = {
        3: 996_000_000_000_000,
        4: 2_940_000_000_000_000,
        5: 8_772_000_000_000_000,
        6: 26_268_000_000_000_000,
        7: 78_756_000_000_000_000,
    }
    canonical_bounds = {str(k): v * 64 for k, v in raw_bounds.items()}
    if payload.get("raw_path_l1_bound_by_transition") != {str(k): v for k, v in raw_bounds.items()}:
        raise AssertionError("H12 raw path bound metadata mismatch")
    if payload.get("canonical_reduction_factor") != 64 or payload.get("canonical_coefficient_bound_by_transition") != canonical_bounds:
        raise AssertionError("H12 canonical coefficient bound metadata mismatch")
    if payload.get("twice_max_canonical_coefficient_bound") != 10_080_768_000_000_000_000:
        raise AssertionError("H12 doubled CRT bound mismatch")
    if payload.get("crt_uniqueness_margin_ratio") != 595:
        raise AssertionError("H12 CRT uniqueness margin mismatch")
    for m in TRANSITIONS:
        item = payload.get("residuals", {}).get(str(m), {})
        if item.get("reduced_polynomial") != {f"c^{a}s^{b}": v for (a, b), v in EXPECTED_REDUCED.items()}:
            raise AssertionError(f"H12 polynomial mismatch at transition {m}")
        if item.get("fourier") != EXPECTED_FOURIER:
            raise AssertionError(f"H12 Fourier mismatch at transition {m}")
        if item.get("at_theta_zero") != 0 or item.get("at_theta_pi") != EXPECTED_C_PI:
            raise AssertionError(f"H12 endpoint mismatch at transition {m}")
    if payload.get("incremental_extension") != {
        "base_certificate": "computational/data/h12_level7_residual_certificate.json",
        "base_certificate_sha256": EXPECTED_BASE_SHA256,
        "new_transition": "C12^(7)=D8^(12)-3*D7^(12)",
        "new_levels_computed_from_source": [7, 8],
        "engine_sha256": ENGINE_SHA256,
        "raw_modular_data": {
            str(p): f"computational/data/h12_level8_raw_modular/prime_{p}.json" for p in PRIMES
        },
    }:
        raise AssertionError("H12 incremental-extension metadata mismatch")
    here = Path(__file__).parent
    base_path = here / "data" / "h12_level7_residual_certificate.json"
    engine_path = here / "h12_residual_engine.cpp"
    if hashlib.sha256(base_path.read_bytes()).hexdigest() != EXPECTED_BASE_SHA256:
        raise AssertionError("verified level-7 base certificate hash mismatch")
    if hashlib.sha256(engine_path.read_bytes()).hexdigest() != ENGINE_SHA256:
        raise AssertionError("level-8 source engine hash mismatch")
    reconstructed = _extend_certificate(json.loads(base_path.read_text()), _read_cached_rows(here))
    if reconstructed != payload:
        raise AssertionError("final H12 certificate does not match the raw three-prime level-8 outputs")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Extend the exact H12 CRT certificate through level eight.")
    parser.add_argument("--output", help="write reconstructed certificate JSON")
    parser.add_argument("--check-only", action="store_true", help="check the JSON without compiling the C++ engine")
    parser.add_argument("--use-cached-prime-data", action="store_true", help="reconstruct CRT from the recorded C++ outputs instead of rerunning the engine")
    args = parser.parse_args()
    result = verify() if args.check_only else recompute(use_cached_prime_data=args.use_cached_prime_data)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
