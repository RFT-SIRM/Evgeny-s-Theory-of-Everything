# Open problems

## OP-1 — Prove the higher-moment recurrence and explain its base correction

For the SU(2)-connected Sierpiński-gasket operator family, numerical calculations support

$
\Delta_m^{(p)}(\theta)=3\Delta_{m-1}^{(p)}(\theta)+C_p(\theta),
\qquad p\in\{6,8,10\},

$
from transition $2\to3$ onward for tested levels and angles. The transition $1\to2$ is exceptional at every nonzero tested angle.

The exact Fourier coefficients of the finite-level residuals

$
R_2^{(p)}=\Delta_2^{(p)}-3\Delta_1^{(p)},\qquad
R_4^{(p)}=\Delta_4^{(p)}-3\Delta_3^{(p)}

$
have now been certified by a modular/CRT computation for $p=6,8,10$. The certificate is documented in [HIGHER_MOMENT_MODULAR_CERTIFICATE.md](computational/HIGHER_MOMENT_MODULAR_CERTIFICATE.md). It certifies the finite-level formulas, not the all-level assertion $R_m^{(p)}=R_4^{(p)}$ for every $m\ge3$.

Evidence already collected:
- levels 1–5 across thirteen predeclared angles $\theta=k\pi/12$, $k=0,\ldots,12$;
- levels 1–6 at $0,\pi/2,\pi$;
- independent sparse-matrix-power traces through level 7 at five angles;
- coefficient $C_p=R_4^{(p)}$ fixed from levels 3 and 4 and tested on held-out levels;
- exact modular/CRT coefficient recovery for $R_2$ and $R_4$, plus seven off-grid floating-point validations.

This remains an open all-level theorem.

Next tasks:
1. Prove $R_m^{(p)}(\theta)=R_4^{(p)}(\theta)$ for every $m\ge3$, rather than inferring it from finite holdouts.
2. Derive this level-independence from graph recursion, block structure, closed-walk expansions, or representation theory.
3. Explain structurally why the first transition differs; the finite-level correction has a certified Fourier form, but its graph-recursive cause is not yet known.
4. State assumptions and quantifiers precisely, including exceptional parameter values.
5. Formalize the all-level recurrence and base correction in Lean where feasible, after a paper proof is complete.

## OP-2 — Extend the path-class analysis

The source project reports that for H⁶ on the level-1 graph, single-triangle and two-triangle path classes contribute zero to the defect, while paths visiting all three axes contribute nonzero terms.

Determine whether this cancellation can be generalized to higher levels and to H⁸/H¹⁰. A valid proof should classify the relevant closed walks and explain the cancellation algebraically, not merely enumerate numerical traces.

## OP-3 — Complete exceptional set for spectral decimation

Characterize the full exceptional set, including recursively generated preimages where relevant. Simple exclusion of a finite list is insufficient if residual mismatches remain. State a criterion that can be checked independently at each level.

## OP-4 — Cross-model relationship

Determine whether there is a mathematically precise relation between the SU(2)-connected operators and signed Z₂-flux Laplacians. Candidate relationships must be stated as conjectures until a map and its consequences are proved.

## OP-5 — Reproducible formal CI

The synthesis repository has a Lean CI workflow pointed at a pinned source revision. The pinned-source Lean CI has completed successful builds; rerun it after source or toolchain changes and keep formal proof status distinct from numerical CI status. A Python test pass does not establish that a Lean theorem compiles.
