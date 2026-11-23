#!/usr/bin/env python3
"""Compare finite H12 floating-point diagnostics independent of JSON formatting/ULPs."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

REL_TOL = 1e-12
ABS_TOL = 1e-12


def compare(expected: Any, actual: Any, path: str = "$") -> None:
    if isinstance(expected, bool) or isinstance(actual, bool):
        if type(expected) is not type(actual) or expected != actual:
            raise ValueError(f"{path}: expected {expected!r}, got {actual!r}")
        return
    if isinstance(expected, dict) and isinstance(actual, dict):
        if expected.keys() != actual.keys():
            missing = sorted(expected.keys() - actual.keys())
            extra = sorted(actual.keys() - expected.keys())
            raise ValueError(f"{path}: key mismatch; missing={missing}, extra={extra}")
        for key in expected:
            compare(expected[key], actual[key], f"{path}.{key}")
        return
    if isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            raise ValueError(f"{path}: expected list length {len(expected)}, got {len(actual)}")
        for index, (left, right) in enumerate(zip(expected, actual)):
            compare(left, right, f"{path}[{index}]")
        return
    if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
        if isinstance(expected, int) and isinstance(actual, int):
            if expected != actual:
                raise ValueError(f"{path}: expected {expected!r}, got {actual!r}")
        elif not math.isclose(float(expected), float(actual), rel_tol=REL_TOL, abs_tol=ABS_TOL):
            raise ValueError(
                f"{path}: expected {expected!r}, got {actual!r}; "
                f"difference exceeds rel_tol={REL_TOL}, abs_tol={ABS_TOL}"
            )
        return
    if type(expected) is not type(actual) or expected != actual:
        raise ValueError(f"{path}: expected {expected!r}, got {actual!r}")


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(
            "usage: compare_h12_corner_moments_diagnostic.py ACTUAL.json EXPECTED.json"
        )
    actual_path, expected_path = map(Path, sys.argv[1:])
    actual = json.loads(actual_path.read_text(encoding="utf-8"))
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    compare(expected, actual)
    print(
        "H12 order-11 floating-point diagnostic matches: "
        f"exact structure/metadata and numeric values within rel_tol={REL_TOL}, "
        f"abs_tol={ABS_TOL}."
    )


if __name__ == "__main__":
    main()
