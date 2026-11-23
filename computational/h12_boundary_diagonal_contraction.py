"""Exact combinatorial reduction of the degree-12 gluing trace to diagonal blocks.

The module enumerates all ordered positive compositions of 12.  It uses the
partial-involution pairing structure of GlueData.N and the short-distance
cutoff for distinct glued points in the same copy.  It records:

* odd-N words, which reduce to zero by pairing all but one N;
* even-N words, which reduce to a trace of ordered 2x2 diagonal corner blocks;
* cyclic composition representatives and their exact integer weights.

This is a symbolic/combinatorial audit.  It records the exact hypotheses
needed by the word-reduction proof and points to the existing source lemmas
that discharge the pairing/cutoff part.  Radius-five transport and the final
copy-level synthesis are still separate proof obligations; this is not a
Lean-kernel theorem.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path

POWER = 12
LEVEL3_CORNER_DISTANCE = 8
LEVEL4_CORNER_DISTANCE = 16


def compositions(total: int, parts: int) -> list[tuple[int, ...]]:
    """All ordered positive compositions of total into exactly parts terms."""
    if total < 1 or parts < 1 or parts > total:
        return []
    if parts == 1:
        return [(total,)]
    out: list[tuple[int, ...]] = []
    for cuts in combinations(range(1, total), parts - 1):
        boundaries = (0, *cuts, total)
        out.append(tuple(boundaries[i + 1] - boundaries[i] for i in range(parts)))
    return out


def rotations(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(word[i:] + word[:i] for i in range(len(word)))


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(rotations(word))


def independent_safe_gap_set(
    word: tuple[int, ...], distance: int
) -> tuple[int, ...]:
    """Choose (r-1)/2 cyclically nonadjacent safe gaps for odd r >= 3."""
    r = len(word)
    if r < 3 or r % 2 == 0:
        raise ValueError("an odd word of length at least three is required")
    need = (r - 1) // 2
    safe = [i for i, exponent in enumerate(word) if exponent < distance]
    for chosen in combinations(safe, need):
        chosen_set = set(chosen)
        if all((i + 1) % r not in chosen_set for i in chosen):
            return tuple(chosen)
    raise AssertionError(f"no safe matching for {word} at distance {distance}")


def even_pairing_safe_gaps(
    word: tuple[int, ...], distance: int
) -> tuple[int, ...]:
    """Choose one alternating perfect matching, avoiding the (unique) long gap."""
    r = len(word)
    if r < 2 or r % 2:
        raise ValueError("an even word is required")
    long = [i for i, exponent in enumerate(word) if exponent >= distance]
    if len(long) > 1:
        raise AssertionError(f"more than one long gap in degree-{sum(word)} word: {word}")
    # The two alternating matchings are the even and odd indices.  Select the
    # one not containing the unique long exponent; if no long exponent exists,
    # use the even-index matching as the canonical choice.
    parity = 1 if long and long[0] % 2 == 0 else 0
    chosen = tuple(i for i in range(r) if i % 2 == parity)
    if any(word[i] >= distance for i in chosen):
        raise AssertionError(f"selected pairing contains a long gap: {word}, {chosen}")
    return chosen


def _orbit_inventory(total: int, parts: int) -> dict:
    words = compositions(total, parts)
    unseen = set(words)
    representatives: list[dict] = []
    orbit_sizes: Counter[int] = Counter()
    weight_sum = Fraction(0)
    while unseen:
        representative = min(unseen)
        orbit = set(rotations(representative))
        unseen.difference_update(orbit)
        orbit_size = len(orbit)
        coefficient = Fraction(total, parts) * orbit_size
        if coefficient.denominator != 1:
            raise AssertionError(
                f"nonintegral cyclic coefficient for p={total}, r={parts}, {representative}"
            )
        representatives.append({
            "composition": list(representative),
            "orbit_size": orbit_size,
            "coefficient": coefficient.numerator,
        })
        orbit_sizes[orbit_size] += 1
        weight_sum += coefficient
    representatives.sort(key=lambda item: tuple(item["composition"]))
    if sum(orbit_sizes.values()) != len(representatives):
        raise AssertionError("cyclic orbit count mismatch")
    if sum(size * count for size, count in orbit_sizes.items()) != len(words):
        raise AssertionError("cyclic orbits do not partition the compositions")
    return {
        "r": parts,
        "composition_count": len(words),
        "cyclic_orbit_count": len(representatives),
        "orbit_size_histogram": {str(k): orbit_sizes[k] for k in sorted(orbit_sizes)},
        "cyclic_weight_sum": str(weight_sum),
        "representatives": representatives,
    }


def build_inventory(power: int = POWER, distance: int = LEVEL3_CORNER_DISTANCE) -> dict:
    if power != 12:
        raise ValueError("this audited contraction is specialized to power 12")
    if distance != 8:
        raise ValueError("the audited exceptional-level cutoff is specialized to 8")

    rows = []
    odd_count = even_count = odd_long = even_long = 0
    odd_matching_count = 0
    raw_long_total = 0
    for r in range(1, power + 1):
        words = compositions(power, r)
        expected = 1 if r == 1 else __import__("math").comb(power - 1, r - 1)
        if len(words) != expected:
            raise AssertionError(f"composition count mismatch at r={r}")
        long_words = [word for word in words if max(word) >= distance]
        raw_long_total += len(long_words)
        row = {
            "r": r,
            "composition_count": len(words),
            "raw_long_gap_count": len(long_words),
        }
        if r == 1:
            row.update({
                "trace_class": "single_N_zero",
                "matching_size": 0,
            })
            odd_count += len(words)
            odd_long += len(long_words)
        elif r % 2:
            matchings = [independent_safe_gap_set(word, distance) for word in words]
            if any(len(x) != (r - 1) // 2 for x in matchings):
                raise AssertionError("odd matching size mismatch")
            row.update({
                "trace_class": "odd_N_zero_after_pairing_all_but_one",
                "matching_size": (r - 1) // 2,
            })
            odd_count += len(words)
            odd_long += len(long_words)
            odd_matching_count += len(words)
        else:
            matchings = [even_pairing_safe_gaps(word, distance) for word in words]
            if any(len(x) != r // 2 for x in matchings):
                raise AssertionError("even perfect matching size mismatch")
            row.update({
                "trace_class": "even_N_diagonal_boundary_contraction",
                "matching_size": r // 2,
            })
            even_count += len(words)
            even_long += len(long_words)
        rows.append(row)

    even_orbits = [_orbit_inventory(power, r) for r in range(2, power + 1, 2)]
    total_orbits = sum(x["cyclic_orbit_count"] for x in even_orbits)
    weighted_even = sum(Fraction(x["cyclic_weight_sum"]) for x in even_orbits)

    # Exact total-weight identity: sum_r (p/r) * C(p-1,r-1) = 2^p - 1.
    weighted_all = sum(
        Fraction(power, r) * len(compositions(power, r))
        for r in range(1, power + 1)
    )
    if odd_count != 1024 or even_count != 1024:
        raise AssertionError("degree-12 parity split mismatch")
    if raw_long_total != 48 or odd_long != 24 or even_long != 24:
        raise AssertionError("raw long-gap inventory mismatch")
    if total_orbits != 179 or weighted_even != 2047 or weighted_all != 4095:
        raise AssertionError("cyclic contraction inventory mismatch")

    return {
        "status": "EXACT_ALGEBRAIC_BOUNDARY_CONTRACTION_CONDITIONAL_ON_GLUE_LOCALITY",
        "moment": power,
        "level3_corner_distance": distance,
        "level4_and_later_corner_distance": LEVEL4_CORNER_DISTANCE,
        "maximum_number_of_long_gaps_per_composition": 1,
        "ordered_compositions_total": 1 << (power - 1),
        "raw_compositions_with_a_part_at_least_8": raw_long_total,
        "raw_long_gap_split": {"odd_r": odd_long, "even_r": even_long},
        "after_pairing_reduction": {
            "odd_r_compositions_vanish": odd_count,
            "even_r_compositions_reduce_to_boundary_products": even_count,
            "genuine_off_diagonal_corner_terms_required": 0,
        },
        "cyclic_even_r_reduction": {
            "representative_count": total_orbits,
            "even_r_composition_weight_sum": str(weighted_even),
            "all_word_weight_sum": str(weighted_all),
            "by_r": even_orbits,
        },
        "by_r": rows,
        "trace_expansion": {
            "identity": "Tr((K+K*N)^12) = Tr(K^12) + sum_{r=1}^{12} (12/r) * sum_{a in Comp(12,r)} Tr(K^a1*N*...*K^ar*N)",
            "ordered_composition_count": 2048,
            "total_weighted_nonempty_word_count": "4095",
            "weight_explanation": "12/r counts cyclic placements of the r gluing factors; cyclic orbit grouping uses the exact orbit size, including periodic words",
        },
        "boundary_formula": {
            "corner_block": "M_j(x) = the ordered 2x2 spin block (K^j)_{x,x}",
            "even_composition": (
                "B(a_1,...,a_r) = sum_{x in G.g} tr_2("
                "M_{a_1}(sigma x) M_{a_2}(x) ... "
                "M_{a_{r-1}}(sigma x) M_{a_r}(x)) for even r"
            ),
            "trace_defect_correction": (
                "sum_{r even} (12/r) * sum_{a in Comp(12,r)} B(a); "
                "all odd-r strata vanish"
            ),
            "spin_block_order": "the full 2x2 matrix order is preserved; no commutation or scalar reduction is assumed",
            "offdiagonal_corner_use": "at most one long spatial corner block can occur in a composition; after all other factors are spatially block diagonal, only its spatial diagonal block contributes to the trace",
        },
        "pairing_reduction": {
            "odd_r": "choose a cyclically nonadjacent matching of (r-1)/2 short gaps; the remaining single N makes the trace zero by the BD*N trace lemma",
            "even_r": "choose one alternating perfect matching avoiding the unique long gap; all selected N*K^j*N factors and all remaining short K^j factors are spatially block diagonal, leaving at most one unrestricted long factor",
            "long_gap_threshold_at_level3": 8,
            "maximum_long_gaps_per_composition": 1,
            "genuine_offdiagonal_corner_terms_required": 0,
        },
        "source_pin": {
            "repository": "https://github.com/RFT-SIRM/Evgeny-Theorem",
            "commit": "4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f",
            "files": [
                "formalization/EvgenyTheorem/GlueK.lean",
                "formalization/EvgenyTheorem/GlueSG.lean",
                "formalization/EvgenyTheorem/GlueAlg.lean",
                "formalization/EvgenyTheorem/GlueCorner.lean",
            ],
            "declarations": [
                "GlueK.sg_EKEt",
                "GlueK.pOpO_succ_trace_ordered_words",
                "GlueSG.sgGlue",
                "GlueSG.sgσ",
                "GlueAlg.Q_eq_diag",
                "GlueAlg.trace_BD_N",
                "GlueCorner.sgK_pow_GlueDiag_of_OAnti",
                "GlueCorner.sgK_pow_hkg_of_OAnti",
            ],
        },
        "source_scaffolding": [
            "Evgeny-Theorem@4ccfae17: GlueK.pOpO_succ_trace_ordered_words gives the ordered-word trace expansion for every positive power",
            "Evgeny-Theorem@4ccfae17: GlueAlg.Q_eq_diag reduces N*K^j*N under the glued-corner vanishing hypothesis",
            "Evgeny-Theorem@4ccfae17: GlueAlg.trace_BD_N annihilates a copy-block-diagonal product followed by one N",
            "Evgeny-Theorem@4ccfae17: GlueCorner.sgK_pow_GlueDiag_of_OAnti and sgK_pow_hkg_of_OAnti supply the spin and geometric cutoff hypotheses",
        ],
        "radius_five_locality_argument": {
            "radius": 5,
            "minimum_level": 3,
            "junction_distance": "2^m >= 8 > 5",
            "diagonal_corner_powers_covered": "0 through 11",
            "face_axis_label_inheritance": "copy face-list offsets are 3^m, divisible by 3",
            "directed_orientation_inheritance": "the radius-five ball contains no copy junction, so all its vertices survive duplicate filtering and their relative vertex-order is preserved",
            "special_oNum_oTil_flip_clearance": "nearest glued B-corner coordinate distance is at least 2^m - 1 >= 7 > 5",
            "evidence_status": "PAPER_LEVEL_RECURSIVE_ARGUMENT; NOT A LEAN_KERNEL_THEOREM",
        },
        "required_hypotheses": [
            "N is supported on the glued boundary, is a fixed-point-free involution there, and preserves the two-dimensional spin coordinate",
            "K is block diagonal with respect to the three-copy map",
            "for distinct glued spatial points in one copy, every spatial off-diagonal 2x2 block of K^j vanishes for 1 <= j < 8 at level 3 (or, at levels with corner distance 16, for all 1 <= j <= 11)",
            "the gluing pairing uses one consistent spin basis on both ends (the concrete source uses the same spin label in glW)",
        ],
        "evidence_boundary": (
            "The exact degree-12 word contraction is proved under the listed pairing and cutoff hypotheses. "
            "The pinned source has stronger state-level corner-vanishing lemmas for the concrete operator. "
            "The all-level radius-five transfer and the final copy-level recurrence synthesis remain paper/formalization obligations; "
            "this artifact is not a Lean-kernel theorem."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rebuild the exact H12 odd/even boundary-word contraction inventory."
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = build_inventory()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
