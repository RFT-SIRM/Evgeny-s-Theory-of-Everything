#!/usr/bin/env python3
"""Diagnostic of corner blocks of powers of the pinned higher-moment operators.

This is a floating-point structural diagnostic, not a proof. It independently
reuses the graph/operator construction from independent_sparse_level7.py and
records diagonal corner blocks (H^j)_{cc}, j=1,...,9, plus off-diagonal corner
blocks at level 3. The latter tests the distance-8 obstruction relevant to H^10.
"""
import argparse
import json
from pathlib import Path

import numpy as np

from independent_sparse_level7 import operator

ANGLES = (("pi_over_2", float(np.pi / 2)),
          ("pi", float(np.pi)),
          ("theta_0_73", 0.73),
          ("theta_0_137", 0.137),
          ("theta_0_51", 0.51),
          ("theta_1_23", 1.23),
          ("theta_1_87", 1.87),
          ("theta_2_41", 2.41),
          ("theta_2_7", 2.7),
          ("theta_3_03", 3.03))
LEVELS = (3, 4, 5, 6)
MAX_POWER = 9


def corner_indices(vertices):
    lookup = {xy: i for i, xy in enumerate(vertices)}
    return [lookup[(0.0, 0.0)], lookup[(1.0, 0.0)], lookup[(0.0, 1.0)]]


def corner_blocks(level, theta, commuting):
    H, vertices, _edges, _faces = operator(level, theta, commuting)
    corners = corner_indices(vertices)
    power_matrix = H.copy()
    blocks = {}
    for power in range(1, MAX_POWER + 1):
        blocks[power] = {
            f"{a}{b}": power_matrix[
                2 * corners[a]:2 * corners[a] + 2,
                2 * corners[b]:2 * corners[b] + 2
            ].toarray()
            for a in range(3) for b in range(3)
        }
        power_matrix = power_matrix @ H
        power_matrix.eliminate_zeros()
    return blocks, len(vertices)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/corner_moment_diagnostic.json")
    args = parser.parse_args()

    report = {
        "status": "floating-point diagnostic; not a proof",
        "operator_source": "computational/independent_sparse_level7.py::operator",
        "corner_coordinates": [[0, 0], [1, 0], [0, 1]],
        "levels": list(LEVELS),
        "powers": list(range(1, MAX_POWER + 1)),
        "angles": {},
        "checks": {
            "diagonal_corner_blocks_invariant_across_levels_3_to_6": True,
            "off_diagonal_corner_blocks_first_nonzero_at_power_8_on_level_3": True
        }
    }
    for angle_name, theta in ANGLES:
        angle_result = {"theta_radians": theta, "models": {}}
        for commuting in (False, True):
            model_name = "commuting_control" if commuting else "noncommuting_SU2"
            data = {}
            vertex_counts = {}
            for level in LEVELS:
                data[level], vertex_counts[level] = corner_blocks(level, theta, commuting)
            diagonal_diffs = {}
            for power in range(1, MAX_POWER + 1):
                err = max(
                    float(np.max(np.abs(data[level][power][f"{c}{c}"]
                                        - data[3][power][f"{c}{c}"])))
                    for level in LEVELS for c in range(3)
                )
                diagonal_diffs[str(power)] = err
                if err > 1e-9:
                    report["checks"]["diagonal_corner_blocks_invariant_across_levels_3_to_6"] = False

            offdiag_max = {}
            for power in range(1, MAX_POWER + 1):
                offdiag_max[str(power)] = max(
                    float(np.max(np.abs(data[3][power][f"{a}{b}"])))
                    for a in range(3) for b in range(3) if a != b
                )
            first_nonzero = next(
                (power for power in range(1, MAX_POWER + 1)
                 if offdiag_max[str(power)] > 1e-9), None
            )
            if first_nonzero != 8:
                report["checks"]["off_diagonal_corner_blocks_first_nonzero_at_power_8_on_level_3"] = False

            angle_result["models"][model_name] = {
                "vertex_counts": {str(k): v for k, v in vertex_counts.items()},
                "max_abs_diagonal_corner_block_difference_vs_level_3_by_power": diagonal_diffs,
                "max_abs_off_diagonal_corner_block_entry_on_level_3_by_power": offdiag_max,
                "first_nonzero_off_diagonal_corner_power_on_level_3": first_nonzero
            }
        report["angles"][angle_name] = angle_result

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report["checks"], indent=2))
    print("Wrote", output)
    if not all(report["checks"].values()):
        raise SystemExit("corner diagnostic check failed")


if __name__ == "__main__":
    main()
