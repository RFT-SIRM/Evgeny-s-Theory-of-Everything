#!/usr/bin/env python3
"""Arithmetic audit of published higher-moment reference values.

This reads the displayed reference values embedded below. It does not
recompute traces from the operator matrices.
"""
from decimal import Decimal, getcontext

getcontext().prec = 40

REFERENCE = {
    "H6": [
        "-3180.000000000000",
        "-6956.588745030516",
        "-18274.354980121832",
        "-52227.653685396537",
    ],
    "H8": [
        "-246909.026268397924",
        "-595053.284942481667",
        "-1632052.331668503582",
        "-4743049.471846580505",
    ],
    "H10": [
        "-14013358.982483163476",
        "-37686518.369789719582",
        "-107772338.487565994263",
        "-318029798.840893745422",
    ],
}


def transition_constants(values):
    """Return C_{m-1->m} = d_m - 3*d_{m-1} from decimal strings."""
    d = [Decimal(value) for value in values]
    return [d[i] - Decimal(3) * d[i - 1] for i in range(1, len(d))]


def audit():
    results = {power: transition_constants(values)
               for power, values in REFERENCE.items()}
    for power, constants in results.items():
        print(power)
        for transition, value in enumerate(constants, start=1):
            print(f"  C_{transition}->{transition + 1} = {value}")
        first_gap = abs(constants[0] - constants[1])
        later_gap = abs(constants[1] - constants[2])
        print(f"  first-vs-second gap = {first_gap}")
        print(f"  second-vs-third gap = {later_gap}")
    return results


if __name__ == "__main__":
    audit()
