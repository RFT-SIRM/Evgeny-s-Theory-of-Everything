#!/usr/bin/env python3
"""Numerically reconstruct and off-grid validate integer Fourier candidates for R2 and R4.

This is coefficient discovery/regression evidence, not a symbolic proof.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from independent_sparse_level7 import delta

N = 21
HOLDOUT_ANGLES = (0.137, 0.51, 1.23, 1.87, 2.41, 2.7, 3.03)
POWERS = (6, 8, 10)

# Each moment stores (constant term, [(A_k, B_k), k=1..p]) for
# R_m(theta) = Delta_m - 3 Delta_(m-1) = a0 + sum(A_k cos(k theta/2) + B_k sin(k theta/2)).
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

def eval_candidate(candidate, power, theta):
    constant, modes = candidate[power]
    return float(constant + sum(
        A * np.cos(k * theta / 2) + B * np.sin(k * theta / 2)
        for k, (A, B) in enumerate(modes, start=1)
    ))

def transition(values, power, m):
    return values[m][f"H{power}"] - 3 * values[m - 1][f"H{power}"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/higher_moment_coefficient_candidates.json")
    args = parser.parse_args()

    samples = {kind: {p: [] for p in POWERS} for kind in ("R2", "R4")}
    for j in range(N):
        theta = 4 * np.pi * j / N
        values = {m: delta(m, theta) for m in range(1, 5)}
        for p in POWERS:
            samples["R2"][p].append(transition(values, p, 2))
            samples["R4"][p].append(transition(values, p, 4))
        print(f"Fourier sample {j + 1}/{N}", flush=True)

    spectral_errors = {}
    for kind in ("R2", "R4"):
        for p in POWERS:
            spectrum = np.fft.fft(np.asarray(samples[kind][p])) / N
            a0, modes = CANDIDATES[kind][p]
            errors = [abs(float(spectrum[0].real) - a0)]
            for k in range(1, N // 2):
                measured_A = 2 * float(spectrum[k].real)
                measured_B = -2 * float(spectrum[k].imag)
                expected_A, expected_B = modes[k - 1] if k <= p else (0, 0)
                errors.extend((abs(measured_A - expected_A), abs(measured_B - expected_B)))
            max_error = max(errors)
            spectral_errors[f"{kind}_H{p}"] = max_error
            if max_error > 1e-3:
                raise AssertionError(f"{kind} H{p}: integer Fourier candidate mismatch {max_error}")

    off_grid = {}
    for theta in HOLDOUT_ANGLES:
        values = {m: delta(m, theta) for m in range(1, 5)}
        off_grid[str(theta)] = {}
        for p in POWERS:
            for kind, m in (("R2", 2), ("R4", 4)):
                observed = transition(values, p, m)
                predicted = eval_candidate(CANDIDATES[kind], p, theta)
                residual = abs(observed - predicted)
                off_grid[str(theta)][f"{kind}_H{p}"] = {
                    "observed": observed, "candidate": predicted, "absolute_residual": residual
                }
                if residual > 1e-3:
                    raise AssertionError(f"off-grid mismatch at theta={theta}, {kind}, H{p}: {residual}")
        print(f"Off-grid angle {theta}: passed", flush=True)

    report = {
        "status": "integer Fourier candidates numerically reconstructed; not a symbolic proof",
        "fourier_variable": "phi = theta/2",
        "fourier_period_in_theta": "4*pi",
        "sampling": {"points": N, "angles": "theta_j = 4*pi*j/21, j=0,...,20",
                     "frequency_bound": "A trace of H^p is a trigonometric polynomial with modes |k| <= p in phi"},
        "candidate_convention": "R_m^(p)(theta) = Delta_m^(p)(theta) - 3 Delta_(m-1)^(p)(theta) = a0 + sum_k (A_k cos(k theta/2) + B_k sin(k theta/2))",
        "candidates": CANDIDATES,
        "max_fourier_coefficient_reconstruction_error": spectral_errors,
        "off_grid_holdout_angles": list(HOLDOUT_ANGLES),
        "off_grid_validation": off_grid,
        "interpretation": "The integer coefficients are reconstructed from floating-point traces and pass off-grid tests. Exact symbolic coefficient identities and an analytic derivation of the exceptional first transition remain open."
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {output}")

if __name__ == "__main__":
    main()
