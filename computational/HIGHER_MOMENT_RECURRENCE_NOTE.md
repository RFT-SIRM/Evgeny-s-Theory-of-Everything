# Higher-moment recurrence: numerical evidence note

**Status: numerically supported conjecture; not a theorem.**

## 1. Definitions

For graph level \(m\), angle \(\theta\), and even power \(p\in\{6,8,10\}\), define the trace defect
\[
\Delta_m^{(p)}(\theta)
=\operatorname{Tr}\bigl(H_C(m,\theta)^p\bigr)
-\operatorname{Tr}\bigl(H_{C'}(m,\theta)^p\bigr),
\]
where \(H_C\) is the non-commuting SU(2)-connection operator and \(H_{C'}\) is the commuting control operator built by the pinned implementation in [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem).

Define the transition residual
\[
R_m^{(p)}(\theta)
=\Delta_m^{(p)}(\theta)-3\Delta_{m-1}^{(p)}(\theta),
\qquad m\ge2.
\]

The candidate recurrence is
\[
\Delta_m^{(p)}(\theta)=3\Delta_{m-1}^{(p)}(\theta)+C_p(\theta),
\qquad m\ge3.
\]
Equivalently, \(R_m^{(p)}(\theta)=C_p(\theta)\) for \(m\ge3\). The transition \(m=2\), from level 1 to level 2, is numerically exceptional for every nonzero angle tested. This indexing is important: the claim is **not** that the same recurrence constant applies to the first transition.

## 2. What was computed

All workflows check out the source at commit [9ed32ae27b4493945624c2911d2815059613a9f5](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/9ed32ae27b4493945624c2911d2815059613a9f5). The synthesis repository's scripts and workflows are versioned; numerical outputs are preserved in JSON.

| Experiment | Levels | Angles | Holdout |
|---|---|---|---|
| Angle grid | 1–5 | \(\theta=k\pi/12\), \(k=0,\ldots,12\) | Fix \(C_p\) from \(R_4\); predict level 5; also compare \(R_3\) with \(R_4\) |
| Extended level | 1–6 | \(0,\pi/2,\pi\) | Fix \(C_p\) from \(R_4\); predict levels 5 and 6; compare \(R_3,R_5,R_6\) |
| Algorithm cross-check | 1–4 | all 13 angle-grid points | Compare eigenvalue-power sums with direct matrix-power traces |

The coefficient is fixed from \(R_4=\Delta_4-3\Delta_3\), not refitted to levels 5 or 6. The source matrices are Hermitian. The spectral method evaluates traces as sums of eigenvalue powers; the cross-check uses direct matrix powers on smaller levels. These are independent numerical evaluation routes, though both use the same operator-construction function.

## 3. Numerical results

On the 13-angle level-5 grid, maximum relative prediction residuals were:

| Moment | Maximum relative residual |
|---|---:|
| \(H^6\) | \(1.47\times10^{-12}\) |
| \(H^8\) | \(1.80\times10^{-12}\) |
| \(H^{10}\) | \(8.82\times10^{-13}\) |

On the level-6 holdout at \(0,\pi/2,\pi\), maximum relative residuals for the level-6 prediction were:

| Moment | Maximum relative residual |
|---|---:|
| \(H^6\) | \(9.28\times10^{-14}\) |
| \(H^8\) | \(6.74\times10^{-14}\) |
| \(H^{10}\) | \(3.56\times10^{-14}\) |

These values describe floating-point agreement on the stated finite test set. They do not imply a universal error bound, and small residuals are not a substitute for an exact proof.

Selected values of the coefficient inferred as \(R_4\):

| Angle | \(C_6(\theta)\) | \(C_8(\theta)\) | \(C_{10}(\theta)\) |
|---|---:|---:|---:|
| \(\pi/2\) | 2595.41125497 | 153107.523159 | 5287216.62181 |
| \(\pi\) | 5280.00000002 | 277504.000001 | 4507520.00009 |

At \(\theta=0\), all three trace defects and inferred constants vanish within the tested computation.

## 4. Interpretation and limits

The numerical evidence is consistent with a level-independent coefficient beginning at the level-2-to-level-3 transition. The first transition differs and must be treated as a base-case exception.

What is **not** established:
- an exact closed form for \(C_p(\theta)\);
- a proof that the recurrence holds for every graph level;
- a proof that it holds for every real angle;
- a general explanation of the exceptional first transition;
- a Lean formalization of the higher-moment recurrence.

## 5. Research closure criteria

This line of work should be called mathematically closed only when all of the following are supplied:

1. An exact expression or algebraic characterization of \(C_p(\theta)\).
2. A derivation from the graph/operator recursion, block structure, or closed-walk expansion.
3. A proof of the starting index and of the base-case exception.
4. Explicit hypotheses and treatment of exceptional parameter values.
5. A machine-checked proof where feasible, with the source revision and toolchain pinned.
6. Numerical tests retained as regression checks, not cited as the proof itself.

## Reproducibility links

- [13-angle holdout workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38761024619)
- [Level-6 holdout workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38761487012)
- [13-angle JSON results](data/higher_moment_angle_grid_13.json)
- [Level-6 results](HIGHER_MOMENT_LEVEL6_RESULTS.md)
- [Level-6 machine-readable data](data/higher_moment_level6_3angles.json)
