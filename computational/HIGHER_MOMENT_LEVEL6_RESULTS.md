# Level-6 higher-moment holdout results

**Status:** numerical holdout passed on the pinned source implementation; not a proof.

- Workflow: [Higher-moment level-6 holdout](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38761487012)
- Synthesis commit tested: `6b0c5ee48abdc80e52a8dbca2a67d325364190f0`
- Source commit: [RFT-SIRM/Evgeny-Theorem @ 9ed32ae](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/9ed32ae27b4493945624c2911d2815059613a9f5)
- Levels: 1–6
- Powers: 6, 8, 10
- Angles: $0,\pi/2,\pi$
- Method: NumPy Hermitian eigenspectra; traces evaluated as sums of eigenvalue powers.
- The published level-1..4 references at $\theta=\pi/2$ passed the script's relative-error checks.

The constant $C=d_4-3d_3$ was fixed using levels 3 and 4. Neither level 5 nor level 6 was used to fit it; both were predictions.

## Level-6 prediction residuals

| Angle | H⁶ relative residual | H⁸ relative residual | H¹⁰ relative residual |
|---|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| $\pi/2$ | $9.28\times10^{-14}$ | $6.74\times10^{-14}$ | $3.56\times10^{-14}$ |
| $\pi$ | $7.63\times10^{-15}$ | $1.11\times10^{-14}$ | $2.06\times10^{-14}$ |

Full output for all three angles, moments, levels, transition constants, and residuals is preserved in [machine-readable JSON](data/higher_moment_level6_3angles.json).

## Interpretation

1. The candidate recurrence with a constant fixed from levels 3 and 4 predicts both levels 5 and 6 to numerical precision at all three tested angles.
2. The first transition $1\to2$ remains exceptional at nonzero angles; later transition constants agree to numerical precision.
3. The result extends the finite numerical evidence to level 6, including $\theta=0$ and $\theta=\pi$. It does not prove the recurrence for all levels or all angles and does not derive a symbolic formula for $C(\theta)$.
4. The computation ran successfully on GitHub Actions with 2,190-dimensional operators at level 6.

## Next target

Derive the recurrence from the graph/operator recursion and obtain an exact expression for $C(\theta)$. Until a proof exists, retain the status **numerically supported conjecture**, not theorem.
