"""Exact combinatorial inventory of the degree-12 gluing trace expansion.

This module enumerates the ordered-composition terms in
    Tr((K + K*N)^12) - Tr(K^12)
and classifies which terms can contain an off-diagonal corner block at
corner distances 8 (level 3) and 16 (level 4).

It does not encode graph-specific N blocks or claim a Lean theorem.  The
projection formula in the accompanying report is conditional only on the
documented support property that N is supported on the finite gluing-boundary
subspace.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from math import comb
from pathlib import Path
import json


def compositions(total: int, parts: int) -> list[tuple[int, ...]]:
    """All ordered compositions of total into exactly `parts` positive parts."""
    if total < 1 or parts < 1 or parts > total:
        return []
    if parts == 1:
        return [(total,)]
    out: list[tuple[int, ...]] = []
    # First part ranges from 1 to the largest value leaving `parts-1` ones.
    for first in range(1, total - parts + 2):
        for tail in compositions(total - first, parts - 1):
            out.append((first, *tail))
    return out


def inventory(power: int = 12, corner_distance: int = 8) -> dict:
    """Return exact word counts and exceptional words for a corner cutoff."""
    if power < 1:
        raise ValueError("power must be positive")
    if corner_distance < 1:
        raise ValueError("corner_distance must be positive")

    by_r = []
    all_words = 0
    exceptional_total = 0
    exceptional_odd = 0
    exceptional_even = 0
    total_weight = Fraction(0)
    exceptional_weight = Fraction(0)

    for r in range(1, power + 1):
        words = compositions(power, r)
        exceptional = [word for word in words if max(word) >= corner_distance]
        count = len(words)
        bad = len(exceptional)
        coefficient = Fraction(power, r)
        all_words += count
        exceptional_total += bad
        total_weight += coefficient * count
        exceptional_weight += coefficient * bad
        if r % 2:
            exceptional_odd += bad
        else:
            exceptional_even += bad
        by_r.append({
            "r": r,
            "composition_count": count,
            "expected_composition_count": comb(power - 1, r - 1),
            "coefficient": f"{coefficient.numerator}/{coefficient.denominator}",
            "possible_off_diagonal_count": bad,
            "diagonal_only_count": count - bad,
            "possible_off_diagonal_words": [list(x) for x in exceptional],
        })

    expected_total = 1 << (power - 1)
    if all_words != expected_total:
        raise AssertionError(f"composition count mismatch: {all_words} != {expected_total}")

    return {
        "power": power,
        "corner_distance": corner_distance,
        "ordered_compositions_total": all_words,
        "ordered_compositions_with_possible_off_diagonal_corner_factor": exceptional_total,
        "ordered_compositions_diagonal_only_by_distance_cutoff": all_words - exceptional_total,
        "exceptional_odd_r_count": exceptional_odd,
        "exceptional_even_r_count": exceptional_even,
        "weighted_composition_count": str(total_weight),
        "weighted_exceptional_count": str(exceptional_weight),
        "by_number_of_gluing_factors": by_r,
    }


def degree12_report_data() -> dict:
    """The two cutoffs governing transitions 3->4 and m->m+1 for m>=4."""
    level3 = inventory(12, 8)
    level4 = inventory(12, 16)
    even_r_count = sum(row["composition_count"] for row in level4["by_number_of_gluing_factors"]
                       if row["r"] % 2 == 0)
    odd_r_count = sum(row["composition_count"] for row in level4["by_number_of_gluing_factors"]
                      if row["r"] % 2 == 1)
    return {
        "moment": 12,
        "maximum_exponent_in_a_nontrivial_composition": 11,
        "level3_corner_distance": 8,
        "level4_and_later_corner_distance": 16,
        "level3": level3,
        "level4_and_later": level4,
        "even_r_composition_count": even_r_count,
        "odd_r_composition_count": odd_r_count,
        "generic_even_r_terms_only_if_N_is_a_disjoint_pairing": even_r_count,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Enumerate all degree-12 noncommutative gluing words and distance exceptions."
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = degree12_report_data()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
