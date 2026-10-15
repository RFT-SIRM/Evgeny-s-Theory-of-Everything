# Open problems

## OP-1 — Derive the higher-moment recurrence and its constant

For the SU(2)-connected Sierpiński-gasket operator family, numerical calculations support
\[
\Delta_m(H^p,\theta)=3\Delta_{m-1}(H^p,\theta)+C_p(\theta),
\qquad p\in\{6,8,10\},
\]
from the transition \(2\to3\) onward for the tested levels and angles. The transition \(1\to2\) is exceptional in every nonzero angle tested.

Evidence already collected:
- levels 1–5 across seven angles \(0,\pi/6,\pi/4,\pi/3,\pi/2,2\pi/3,\pi\);
- levels 1–6 at \(0,\pi/2,\pi\);
- recurrence constants fixed using levels 3 and 4, with later levels held out;
- maximum relative level-6 prediction residuals below \(9.3\times10^{-14}\) for all three moments on the three-angle subset.

This remains finite numerical evidence, not a universal theorem.

Next tasks:
1. Derive an exact expression for each \(C_p(\theta)\), or determine its precise algebraic/trigonometric form.
2. Explain why the first transition is exceptional and prove the exact starting index.
3. Derive the recurrence from graph recursion, block structure, path expansions, or representation theory.
4. State assumptions and quantifiers precisely, including all exceptional parameters.
5. Formalize the result in Lean where feasible, after a paper proof is complete.

## OP-2 — Extend the path-class analysis

The source project reports that for H⁶ on the level-1 graph, single-triangle and two-triangle path classes contribute zero to the defect, while paths visiting all three axes contribute nonzero terms.

Determine whether this cancellation can be generalized to higher levels and to H⁸/H¹⁰. A valid proof should classify the relevant closed walks and explain the cancellation algebraically, not merely enumerate numerical traces.

## OP-3 — Complete exceptional set for spectral decimation

Characterize the full exceptional set, including recursively generated preimages where relevant. Simple exclusion of a finite list is insufficient if residual mismatches remain. State a criterion that can be checked independently at each level.

## OP-4 — Cross-model relationship

Determine whether there is a mathematically precise relation between the SU(2)-connected operators and signed Z₂-flux Laplacians. Candidate relationships must be stated as conjectures until a map and its consequences are proved.

## OP-5 — Reproducible formal CI

The synthesis repository now has a Lean CI workflow pointed at a pinned source revision. Verify that it completes a clean `lake build`, then keep formal proof status distinct from numerical CI status. A Python test pass does not establish that a Lean theorem compiles.
