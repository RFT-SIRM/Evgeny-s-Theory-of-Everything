# Higher-moment recurrence: evidence and exact finite-level coefficients

**Status: exact Fourier coefficients certified for the finite-level residuals; the all-level recurrence remains an open conjecture.**

## 1. Definitions

For graph level \(m\), angle \(\theta\), and even power \(p\in\{6,8,10\}\), define
\[
\Delta_m^{(p)}(\theta)
=\operatorname{Tr}\bigl(H_C(m,\theta)^p\bigr)
-\operatorname{Tr}\bigl(H_{C'}(m,\theta)^p\bigr),
\]
where \(H_C\) is the non-commuting SU(2)-connection operator and \(H_{C'}\) is the commuting control operator built by the pinned implementation in [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem).

Define the transition residual
\[
R_m^{(p)}(\theta)=\Delta_m^{(p)}(\theta)-3\Delta_{m-1}^{(p)}(\theta),
\qquad m\ge2.
\]

The candidate recurrence is
\[
\Delta_m^{(p)}(\theta)=3\Delta_{m-1}^{(p)}(\theta)+C_p(\theta),
\qquad m\ge3.
\]
Equivalently, \(R_m^{(p)}(\theta)=C_p(\theta)\) for \(m\ge3\). The first transition \(R_2^{(p)}\) is exceptional.

## 2. Evidence and exact finite-level result

Numerical holdouts cover:
- levels 1–5 at thirteen predeclared angles \(\theta=k\pi/12\), \(k=0,\ldots,12\);
- levels 1–6 at \(0,\pi/2,\pi\);
- independent sparse-matrix-power predictions through level 7 at five angles;
- direct matrix-power versus eigenvalue-power trace checks on levels 1–4.

In addition, the exact modular/CRT certificate proves the finite-level Fourier coefficient identities for \(R_2^{(p)}\) and \(R_4^{(p)}\), for \(p=6,8,10\). The coefficient denominator and Fourier-mode bounds, three prime moduli, and CRT uniqueness bounds are documented in [HIGHER_MOMENT_MODULAR_CERTIFICATE.md](HIGHER_MOMENT_MODULAR_CERTIFICATE.md). This is stronger than floating-point interpolation, but it does not establish \(R_m=R_4\) for all \(m\ge3\).

## 3. Numerical regression results

On the 13-angle level-5 grid, maximum relative prediction residuals were:

| Moment | Maximum relative residual |
|---|---:|
| \(H^6\) | \(1.47\times10^{-12}\) |
| \(H^8\) | \(1.80\times10^{-12}\) |
| \(H^{10}\) | \(8.82\times10^{-13}\) |

On the level-6 holdout at \(0,\pi/2,\pi\), maximum relative residuals were:

| Moment | Maximum relative residual |
|---|---:|
| \(H^6\) | \(9.28\times10^{-14}\) |
| \(H^8\) | \(6.74\times10^{-14}\) |
| \(H^{10}\) | \(3.56\times10^{-14}\) |

The independent sparse-matrix-power workflow tests levels 5–7 at five angles and passes. These are finite regression tests, not a universal error bound.

## 4. Interpretation and limits

What is now established computationally and by the modular/CRT certificate:
- exact Fourier coefficients of the finite-level residual \(R_2^{(p)}\) at the transition 1→2;
- exact Fourier coefficients of the finite-level residual \(R_4^{(p)}\) at the transition 3→4;
- an explicit finite-level correction \(R_2^{(p)}-R_4^{(p)}\);
- numerical recurrence predictions through level 7 at five angles.

What remains **not** established:
- that \(R_m^{(p)}(\theta)=R_4^{(p)}(\theta)\) for every \(m\ge3\);
- a derivation of that level-independence from the recursive graph/operator structure;
- a structural explanation of the exceptional first transition;
- a Lean formalization of the all-level recurrence.

## 5. Research closure criteria

This line of work should be called mathematically closed only when all of the following are supplied:

1. A proof that the certified \(R_4^{(p)}(\theta)\) is the residual \(R_m^{(p)}(\theta)\) for every \(m\ge3\).
2. A derivation from the graph/operator recursion, block structure, or closed-walk expansion.
3. A proof of the starting index and a structural account of the base-case correction.
4. Explicit hypotheses and treatment of exceptional parameter values.
5. A machine-checked proof where feasible, with the source revision and toolchain pinned.
6. Numerical and modular checks retained as regression certificates, not cited as substitutes for the all-level proof.

## Reproducibility links

- [13-angle holdout workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38761024619)
- [Level-6 holdout workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38761487012)
- [Five-angle sparse level-7 holdout](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38767388243)
- [Floating-point Fourier reconstruction and off-grid checks](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38767383292)
- [Exact modular/CRT coefficient certificate](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38769047951)
- [13-angle JSON results](data/higher_moment_angle_grid_13.json)
- [Level-6 results](HIGHER_MOMENT_LEVEL6_RESULTS.md)
- [Level-6 machine-readable data](data/higher_moment_level6_3angles.json)
