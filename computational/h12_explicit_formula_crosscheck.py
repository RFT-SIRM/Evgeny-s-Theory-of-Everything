"""Cross-check of the explicit H12 closed form against the external CRT certificate.

Upstream (RFT-SIRM/Evgeny-Theorem) proves in Lean, for every real theta and m >= 3,
D_{m+1} = 3 D_m + C_12, and records the explicit exact forms

    D_3  = 32 s^2 Q_3(c, s),      C_12 = -64 s^2 Q_12(c, s),
    D_m  = 32 s^2 (3^(m-3) (Q_3 - Q_12) + Q_12)    for m >= 3,

with c = cos(theta/2), s = sin(theta/2), c^2 + s^2 = 1.  The two finite identities
are exact computer-algebra certificates there, not Lean-kernel theorems.

This module compares those explicit forms with computational/data/
h12_residual_certificate.json, which was produced by a separate implementation
(a C++/Python source mirror of the pinned graph and operator definitions with
three-prime signed CRT).  Only exact integer and rational arithmetic is used.

Checked here:
  1. the circle reduction (c^2 -> 1 - s^2) of -64 s^2 Q_12 equals the certificate's
     common reduced polynomial exactly, as a polynomial;
  2. -64 Q_12(0, 1) equals the certificate's residual at theta = pi for m = 3..7;
  3. the closed form for D_m at theta = pi equals the certificate's D_m(pi) for
     m = 3..8.

Not checked here: the full polynomial D_3 = 32 s^2 Q_3 (only its value at theta = pi,
through item 3).  That identity is certified upstream.
"""
from __future__ import annotations

import json
import re
import sys
from fractions import Fraction
from math import comb
from pathlib import Path

CERTIFICATE = Path(__file__).resolve().parent / "data" / "h12_residual_certificate.json"

# Exponent keys are (power of c, power of s).
Q3 = {
    (6, 0): -12, (5, 1): 24, (5, 0): 1032, (4, 1): -2040, (4, 0): -80120,
    (3, 1): 42894, (3, 0): 2400282, (2, 1): -67494, (2, 0): -30361019,
    (1, 1): -2479593, (1, 0): 275590614, (0, 1): 3481440, (0, 0): -566815997,
}
Q12 = {
    (6, 0): 6, (5, 1): 6, (5, 0): 240, (4, 1): -456, (4, 0): -8858,
    (3, 1): 2466, (3, 0): -33138, (2, 1): 618, (2, 0): 1612501,
    (1, 1): 571254, (1, 0): -18512844, (0, 1): -3259668, (0, 0): 13167067,
}
D_LEVELS = (3, 4, 5, 6, 7, 8)
C_LEVELS = (3, 4, 5, 6, 7)


def times_s2(poly: dict[tuple[int, int], int], factor: int) -> dict[tuple[int, int], int]:
    """factor * s^2 * poly."""
    return {(i, j + 2): factor * v for (i, j), v in poly.items()}


def reduce_c_squared(poly: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    """Reduce c^2 to 1 - s^2, leaving c-exponents 0 or 1 (the certificate's canonical form)."""
    out: dict[tuple[int, int], int] = {}
    for (i, j), value in poly.items():
        quotient, remainder = divmod(i, 2)
        for k in range(quotient + 1):
            key = (remainder, j + 2 * k)
            out[key] = out.get(key, 0) + value * comb(quotient, k) * (-1 if k % 2 else 1)
    return {key: value for key, value in out.items() if value}


def evaluate(poly: dict[tuple[int, int], int], c: Fraction, s: Fraction) -> Fraction:
    return sum(Fraction(v) * c**i * s**j for (i, j), v in poly.items())


def closed_form_at_pi(m: int) -> int:
    """32 s^2 (3^(m-3) (Q3 - Q12) + Q12) at c = 0, s = 1."""
    c, s = Fraction(0), Fraction(1)
    q3, q12 = evaluate(Q3, c, s), evaluate(Q12, c, s)
    value = 32 * s**2 * (3 ** (m - 3) * (q3 - q12) + q12)
    assert value.denominator == 1
    return int(value)


def parse_reduced(payload: dict[str, int]) -> dict[tuple[int, int], int]:
    out = {}
    for key, value in payload.items():
        match = re.fullmatch(r"c\^(\d+)s\^(\d+)", key)
        assert match, f"unexpected monomial key {key!r}"
        out[(int(match.group(1)), int(match.group(2)))] = int(value)
    return out


def verify(path: Path = CERTIFICATE) -> dict:
    cert = json.loads(path.read_text(encoding="utf-8"))
    certificate_reduced = parse_reduced(cert["common_reduced_polynomial"])
    explicit_reduced = reduce_c_squared(times_s2(Q12, -64))
    residual_pi = int(-64 * evaluate(Q12, Fraction(0), Fraction(1)))
    return {
        "residual_polynomial_matches": explicit_reduced == certificate_reduced,
        "residual_terms": len(certificate_reduced),
        "residual_at_pi_expected": residual_pi,
        "residual_at_pi_matches": {
            m: int(cert["residuals"][str(m)]["at_theta_pi"]) == residual_pi for m in C_LEVELS
        },
        "d_at_pi_matches": {
            m: int(cert["D_m_at_theta_pi"][str(m)]) == closed_form_at_pi(m) for m in D_LEVELS
        },
    }


def main() -> int:
    result = verify()
    print(json.dumps(result, indent=2, sort_keys=True))
    ok = (
        result["residual_polynomial_matches"]
        and all(result["residual_at_pi_matches"].values())
        and all(result["d_at_pi_matches"].values())
    )
    print("H12 explicit-formula cross-check:", "PASSED" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
