#!/usr/bin/env python3
"""Exact modular/CRT certificate for finite-level higher-moment Fourier coefficients.

This certifies the Fourier coefficients of R2=Delta_2-3 Delta_1 and
R4=Delta_4-3 Delta_3 for p=6,8,10. It does not prove R_m=R4 for all m.
"""
import argparse
import json
import math
from pathlib import Path
import numpy as np
from independent_sparse_level7 import graph

POWERS = (6, 8, 10)
N = 21
PRIMES = (
    (10000453, 5, (2, 3, 7, 11, 79, 137)),
    (20000569, 11, (2, 3, 7, 17, 47, 149)),
    (30000769, 11, (2, 3, 7, 11161)),
)
CANDIDATES = {
    "R2": {
        6: (2244, [(48, 576), (-2244, 0), (-48, -192), (0, 0), (0, 0), (0, 0)]),
        8: (87024, [(17984, 71040), (-87120, -176), (-17984, -23680), (96, 88), (0, 0), (0, 0), (0, 0), (0, 0)]),
        10: (-1751950, [(2621560, 5497240), (1660950, -103570), (-2618620, -1831380), (90970, 51800), (-2940, -620), (30, -10), (0, 0), (0, 0), (0, 0), (0, 0)]),
    },
    "R4": {
        6: (2256, [(48, 576), (-2256, 0), (-48, -192), (0, 0), (0, 0), (0, 0)]),
        8: (96872, [(18944, 62784), (-96896, -128), (-18944, -20928), (24, 64), (0, 0), (0, 0), (0, 0), (0, 0)]),
        10: (-249810, [(2759440, 3693520), (208340, -65430), (-2759560, -1230840), (41490, 32700), (120, -200), (-20, 10), (0, 0), (0, 0), (0, 0), (0, 0)]),
    },
}
VERTICES = {1: 6, 2: 15, 3: 42, 4: 123}


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def build_operator(level, sample, q, zeta, imag_unit, commuting):
    vertices, edges, faces = graph(level)
    n = len(vertices)
    if n != VERTICES[level]:
        raise AssertionError(f\"unexpected vertex count at level {level}: {n}\")
    degree = [0] * n
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
    if max(degree) > 4:
        raise AssertionError(f\"maximum degree exceeds the certified bound at level {level}\")

    z = pow(zeta, sample, q)
    z_inv = pow(zeta, (-sample) % N, q)
    inv2 = pow(2, -1, q)
    inv2i = pow((2 * imag_unit) % q, -1, q)
    cosine = ((z + z_inv) * inv2) % q
    sine = ((z - z_inv) * inv2i) % q

    pauli = (
        ((0, 1), (1, 0)),
        ((0, (-imag_unit) % q), (imag_unit, 0)),
        ((1, 0), (0, (-1) % q)),
    )
    flux_axis = {tuple(sorted(edge)): None for edge in edges}
    for face_index, (a, b, _c) in enumerate(faces):
        flux_axis[tuple(sorted((a, b)))] = 2 if commuting else face_index % 3

    dimension = 2 * n
    rows = [dict() for _ in range(dimension)]
    for v in range(n):
        for spin in range(2):
            rows[2 * v + spin][2 * v + spin] = degree[v] % q

    for (a, b), axis in flux_axis.items():
        if axis is None:
            u = ((1, 0), (0, 1))
            ud = u
        else:
            sigma = pauli[axis]
            u = tuple(tuple(
                ((cosine if i == j else 0) - imag_unit * sine * sigma[i][j]) % q
                for j in range(2)) for i in range(2))
            ud = tuple(tuple(
                ((cosine if i == j else 0) + imag_unit * sine * sigma[i][j]) % q
                for j in range(2)) for i in range(2))
        for i in range(2):
            for j in range(2):
                forward = (-u[i][j]) % q
                reverse = (-ud[j][i]) % q
                if forward:
                    rows[2 * a + i][2 * b + j] = forward
                if reverse:
                    rows[2 * b + j][2 * a + i] = reverse
    return rows


def trace_powers(rows, q):
    dimension = len(rows)
    sparse_entries = [(i, j, value) for i, row in enumerate(rows) for j, value in row.items()]
    power_matrix = np.eye(dimension, dtype=np.int64)
    result = {}
    for power in range(1, max(POWERS) + 1):
        next_matrix = np.zeros_like(power_matrix)
        for i, j, value in sparse_entries:
            next_matrix[:, j] = (next_matrix[:, j] + power_matrix[:, i] * value) % q
        power_matrix = next_matrix
        if power in POWERS:
            result[power] = int(np.trace(power_matrix) % q)
    return result


def validate_prime_and_roots(q, root, factors):
    if not is_prime(q):
        raise AssertionError(f"{q} is not prime")
    for factor in factors:
        if pow(root, (q - 1) // factor, q) == 1:
            raise AssertionError(f"{root} is not a primitive root modulo {q}")
    if (q - 1) % 84:
        raise AssertionError(f"{q}-1 must be divisible by 84")
    zeta = pow(root, (q - 1) // N, q)
    imag_unit = pow(root, (q - 1) // 4, q)
    if pow(zeta, N, q) != 1 or pow(zeta, 3, q) == 1 or pow(zeta, 7, q) == 1:
        raise AssertionError(f"invalid 21st root of unity modulo {q}")
    if pow(imag_unit, 2, q) != q - 1:
        raise AssertionError(f"invalid square root of -1 modulo {q}")
    return zeta, imag_unit


def compute_residuals(q, root, factors):
    zeta, imag_unit = validate_prime_and_roots(q, root, factors)
    values = {}
    for sample in range(N):
        levels = {}
        for level in range(1, 5):
            noncommuting = trace_powers(build_operator(level, sample, q, zeta, imag_unit, False), q)
            commuting = trace_powers(build_operator(level, sample, q, zeta, imag_unit, True), q)
            levels[level] = {p: (noncommuting[p] - commuting[p]) % q for p in POWERS}
        values[sample] = levels

    residual_samples = {"R2": {p: [] for p in POWERS}, "R4": {p: [] for p in POWERS}}
    for sample in range(N):
        for p in POWERS:
            residual_samples["R2"][p].append((values[sample][2][p] - 3 * values[sample][1][p]) % q)
            residual_samples["R4"][p].append((values[sample][4][p] - 3 * values[sample][3][p]) % q)

    checks = {}
    inv_n = pow(N, -1, q)
    scale_cache = {p: pow(2, p, q) for p in POWERS}
    for kind in ("R2", "R4"):
        for p in POWERS:
            y = residual_samples[kind][p]
            spectrum = [
                (sum(y[j] * pow(zeta, (-j * k) % N, q) for j in range(N)) * inv_n) % q
                for k in range(N)
            ]
            expected_constant, modes = CANDIDATES[kind][p]
            errors = [(scale_cache[p] * (spectrum[0] - expected_constant)) % q]
            for k in range(1, N // 2):
                measured_a = (spectrum[k] + spectrum[(-k) % N]) % q
                measured_b = (imag_unit * (spectrum[k] - spectrum[(-k) % N])) % q
                expected_a, expected_b = modes[k - 1] if k <= p else (0, 0)
                errors.extend((
                    (scale_cache[p] * (measured_a - expected_a)) % q,
                    (scale_cache[p] * (measured_b - expected_b)) % q,
                ))
            if any(errors):
                raise AssertionError(f"{kind} H{p} coefficient mismatch modulo {q}")
            checks[f"{kind}_H{p}"] = "all scaled Fourier coefficients match modulo this prime"
    return checks


def coefficient_bound(kind, power):
    # For a graph Laplacian with maximum degree 4, ||H|| <= 8.
    # |Tr(H^p)| <= 2*n*8^p and |Delta_m| <= 4*n_m*8^p.
    if kind == "R2":
        multiplier = 4 * VERTICES[2] + 12 * VERTICES[1]
    else:
        multiplier = 4 * VERTICES[4] + 12 * VERTICES[3]
    max_function = multiplier * (8 ** power)
    # |A_k|, |B_k| <= 2 sup |R|. Each coefficient has denominator dividing 2^p.
    return (2 ** (power + 1)) * max_function


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/higher_moment_modular_certificate.json")
    args = parser.parse_args()

    product = math.prod(q for q, _root, _factors in PRIMES)
    bounds = {
        f"{kind}_H{p}": coefficient_bound(kind, p)
        for kind in ("R2", "R4") for p in POWERS
    }
    if any(product <= 2 * bound for bound in bounds.values()):
        raise AssertionError("CRT modulus product is not large enough for the coefficient bounds")

    prime_checks = {}
    for q, root, factors in PRIMES:
        prime_checks[str(q)] = compute_residuals(q, root, factors)
        print(f"Exact modular DFT passed modulo {q}", flush=True)

    report = {
        "status": "exact finite-level Fourier coefficient certificate via modular arithmetic and CRT",
        "scope": "R2 = Delta_2 - 3 Delta_1 and R4 = Delta_4 - 3 Delta_3, moments p=6,8,10",
        "not_claimed": "This does not prove R_m = R4 for all m >= 3, nor a Lean theorem for the recurrence.",
        "fourier_sampling": {"N": N, "angles": "theta_j = 4*pi*j/21", "frequency_modes": "k=-10,...,10"},
        "primes_and_primitive_roots": [{"prime": q, "primitive_root": root, "prime_factors_of_q_minus_1": list(factors)} for q, root, factors in PRIMES],
        "crt_modulus_product": product,
        "scaled_coefficient_absolute_bounds": bounds,
        "candidate_scaled_coefficient_maxima": candidate_scaled_maxima,
        "crt_uniqueness_check": "modulus product exceeds twice every coefficient bound",
        "candidate_coefficients": CANDIDATES,
        "modular_checks": prime_checks,
        "integrality_basis": "Each operator entry has Fourier coefficients with denominator dividing 2; a product of p entries has denominator dividing 2^p. Therefore 2^p times every Fourier coefficient of a trace defect is an integer.",
        "operator_norm_bound": "Maximum graph degree is 4; block row-sum/Gershgorin gives ||H|| <= 8 for real theta. Use |Tr(H^p)| <= 2*n*8^p to bound the trace defects and their Fourier coefficients.",
        "interpretation": "Given the stated mode, denominator, and norm bounds, agreement modulo three primes with CRT modulus larger than twice the coefficient bounds certifies the displayed finite-level Fourier coefficients exactly. The all-level recurrence remains open."
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
