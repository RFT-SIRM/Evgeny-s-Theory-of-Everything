#!/usr/bin/env python3
"""Exact algebraic audit of the trace-composition expansion.

Uses SymPy over rational matrices to compare the distributive expansion of
Tr((K + K*N)^p) with the ordered-composition formula. The matrices are
deliberately noncommuting. This verifies the algebraic identity on a concrete
exact instance; the general identity still requires a proof.
"""
from itertools import product
import json
from pathlib import Path
import sympy as sp

P_MAX = 7


def compositions(n):
    if n == 0:
        yield ()
        return
    for first in range(1, n + 1):
        for tail in compositions(n - first):
            yield (first,) + tail


def main():
    K = sp.Matrix([[1, 2, 0], [0, 1, 1], [1, 0, 2]])
    N = sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    assert K * N != N * K, "test matrices must be noncommuting"

    results = {}
    for p in range(1, P_MAX + 1):
        lhs = sp.trace((K + K * N) ** p)
        rhs = sp.trace(K ** p)
        by_r = {}
        for r in range(1, p + 1):
            inner = 0
            for comp in compositions(p):
                if len(comp) != r:
                    continue
                word = sp.eye(K.rows)
                for a in comp:
                    word = word * (K ** a) * N
                inner += sp.trace(word)
            by_r[str(r)] = str(sp.factor(sp.Rational(p, r) * inner))
            rhs += sp.Rational(p, r) * inner
        assert sp.simplify(lhs - rhs) == 0, f"identity mismatch at p={p}"
        results[str(p)] = {
            "lhs_exact": str(lhs),
            "rhs_exact": str(sp.simplify(rhs)),
            "difference_exact": "0",
            "composition_terms_by_r": by_r,
            "composition_count": 2 ** (p - 1),
            "binary_word_count_with_gluing": 2 ** p - 1,
        }

    report = {
        "status": "exact rational-matrix verification on one noncommuting instance; not a general proof",
        "matrix_dimension": 3,
        "K": [[int(K[i, j]) for j in range(3)] for i in range(3)],
        "N": [[int(N[i, j]) for j in range(3)] for i in range(3)],
        "commutator_nonzero": K * N != N * K,
        "powers": results,
    }
    out = Path("artifacts/trace_composition_exact_audit.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("Exact trace-composition identity passed for p=1..", P_MAX)
    print("Wrote", out)


if __name__ == "__main__":
    main()
