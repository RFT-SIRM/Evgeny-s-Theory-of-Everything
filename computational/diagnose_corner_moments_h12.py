#!/usr/bin/env python3
"""Sparse numerical diagnostic of diagonal corner blocks through power 11.

It compares the three outer-corner 2x2 diagonal blocks at levels 3--6 for ten
angles and both the SU(2) and commuting-control models. It also records when
spatially off-diagonal corner blocks first become nonzero on level 3. This is a
numerical diagnostic, not a proof; the exact locality argument is separate.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from independent_sparse_level7 import graph, operator

ANGLES = (
    ("pi_over_2", float(np.pi / 2)),
    ("pi", float(np.pi)),
    ("theta_0_73", 0.73),
    ("theta_0_137", 0.137),
    ("theta_0_51", 0.51),
    ("theta_1_23", 1.23),
    ("theta_1_87", 1.87),
    ("theta_2_41", 2.41),
    ("theta_2_7", 2.7),
    ("theta_3_03", 3.03),
)
LEVELS = (3, 4, 5, 6)
MAX_POWER = 11


def corner_indices(vertices: list[tuple[float, float]]) -> list[int]:
    lookup = {xy: i for i, xy in enumerate(vertices)}
    return [lookup[(0.0, 0.0)], lookup[(1.0, 0.0)], lookup[(0.0, 1.0)]]


def corner_blocks(level: int, theta: float, commuting: bool) -> tuple[dict, int]:
    matrix = operator(level, theta, commuting)
    vertices, _edges, _faces = graph(level)
    corners = corner_indices(vertices)
    power_matrix = matrix.copy()
    blocks: dict[int, dict[str, np.ndarray]] = {}
    for power in range(1, MAX_POWER + 1):
        blocks[power] = {
            f"{a}{b}": power_matrix[
                2 * corners[a] : 2 * corners[a] + 2,
                2 * corners[b] : 2 * corners[b] + 2,
            ].toarray()
            for a in range(3)
            for b in range(3)
        }
        power_matrix = power_matrix @ matrix
        power_matrix.eliminate_zeros()
    return blocks, len(vertices)


def build_diagnostic() -> dict:
    report = {
        "status": "finite floating-point sparse-matrix diagnostic; not a proof",
        "operator_source": "computational/independent_sparse_level7.py::operator",
        "corner_coordinates": [[0, 0], [1, 0], [0, 1]],
        "levels": list(LEVELS),
        "powers": list(range(1, MAX_POWER + 1)),
        "angles": {},
        "checks": {
            "diagonal_corner_blocks_invariant_across_levels_3_to_6_through_power_11": True,
            "off_diagonal_level3_corner_blocks_vanish_below_power_8": True,
            "off_diagonal_level3_corner_blocks_nonzero_at_power_8": True,
        },
        "tolerance": 1e-9,
    }
    global_max_diagonal_error = 0.0
    global_offdiag_max = {power: 0.0 for power in range(1, MAX_POWER + 1)}

    for angle_name, theta in ANGLES:
        angle_result = {"theta_radians": theta, "models": {}}
        for commuting, model_name in (
            (False, "noncommuting_SU2"),
            (True, "commuting_control"),
        ):
            data = {}
            vertex_counts = {}
            for level in LEVELS:
                data[level], vertex_counts[level] = corner_blocks(level, theta, commuting)

            diagonal_diffs = {}
            offdiag_max = {}
            for power in range(1, MAX_POWER + 1):
                diff = max(
                    float(
                        np.max(
                            np.abs(
                                data[level][power][f"{corner}{corner}"]
                                - data[3][power][f"{corner}{corner}"]
                            )
                        )
                    )
                    for level in LEVELS
                    for corner in range(3)
                )
                diagonal_diffs[str(power)] = diff
                global_max_diagonal_error = max(global_max_diagonal_error, diff)
                if diff > report["tolerance"]:
                    report["checks"][
                        "diagonal_corner_blocks_invariant_across_levels_3_to_6_through_power_11"
                    ] = False

                off = max(
                    float(np.max(np.abs(data[3][power][f"{a}{b}"])))
                    for a in range(3)
                    for b in range(3)
                    if a != b
                )
                offdiag_max[str(power)] = off
                global_offdiag_max[power] = max(global_offdiag_max[power], off)
                if power < 8 and off > report["tolerance"]:
                    report["checks"][
                        "off_diagonal_level3_corner_blocks_vanish_below_power_8"
                    ] = False

            first_nonzero = next(
                (
                    power
                    for power in range(1, MAX_POWER + 1)
                    if offdiag_max[str(power)] > report["tolerance"]
                ),
                None,
            )
            if first_nonzero != 8:
                report["checks"][
                    "off_diagonal_level3_corner_blocks_nonzero_at_power_8"
                ] = False

            angle_result["models"][model_name] = {
                "vertex_counts": {str(k): v for k, v in vertex_counts.items()},
                "max_abs_diagonal_corner_block_difference_vs_level_3_by_power": diagonal_diffs,
                "max_abs_spatial_off_diagonal_corner_block_entry_on_level_3_by_power": offdiag_max,
                "first_nonzero_spatial_off_diagonal_corner_power_on_level_3": first_nonzero,
            }
        report["angles"][angle_name] = angle_result

    report["summary"] = {
        "maximum_diagonal_block_error_all_models_angles_levels_powers": global_max_diagonal_error,
        "maximum_spatial_off_diagonal_level3_corner_block_entry_by_power": {
            str(k): global_offdiag_max[k] for k in range(1, MAX_POWER + 1)
        },
        "first_nonzero_spatial_off_diagonal_level3_corner_power": next(
            (k for k in range(1, MAX_POWER + 1) if global_offdiag_max[k] > report["tolerance"]),
            None,
        ),
    }
    if not all(report["checks"].values()):
        raise AssertionError("H12 corner-moment diagnostic failed")
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", default="computational/data/h12_corner_moments_order11_diagnostic.json"
    )
    args = parser.parse_args()
    payload = build_diagnostic()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"checks": payload["checks"], "summary": payload["summary"]}, indent=2))
    print("Wrote", output)


if __name__ == "__main__":
    main()
