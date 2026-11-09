# Research programme

## Workstream A — SU(2) fourth-moment theorem

**Source:** [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem)

The source Lean development proves the all-angle fourth-moment trace-defect formula for every m ≥ 1. The synthesis workflow pins the source revision and builds the actual EvgenyTheorem library. Exact theorem definitions and source provenance are authoritative upstream.

## Workstream B — SU(2) higher moments

The current formal status is no longer merely numerical:

- **H6:** Lean proves the recurrence and affine form from level 3 onward. The exceptional finite 2→3 identity has an exact Gaussian-integer polynomial certificate outside the Lean kernel.
- **H8:** Lean proves the recurrence and affine form from level 3 onward. The exceptional finite 2→3 identity has an exact sparse-polynomial certificate outside the Lean kernel.
- **H10:** Lean proves radius-four corner transport through degree 9, an unconditional recurrence from level 4, and an unconditional affine form from level 5. The exact level-five correction remains a finite trace expression rather than an expanded trigonometric polynomial.

The next mathematical tasks are narrowly scoped: formalize the H6/H8 finite base identities in Lean where maintainable, and simplify the exact H10 level-five residual if an explicit coefficient formula is required. Numerical holdouts and modular/CRT certificates remain independent regression evidence, not substitutes for Lean proofs.

## Workstream C — Signed-Z2-flux spectral decimation

**Source:** [RFT-SIRM/Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis)

The merged Schur programme proves the graph-matrix corner-response recursion, strict pivot positivity in the bootstrap window, shifted quadratic-form bounds for levels at least 6, uniqueness of the A1 root in the window, and convergence of selected roots as Rayleigh minima of the quadratic form.

Remaining tasks include the operator eigenvalue identification, the proposed quadratic law, the small-level cases N < 6, and the full Gate A exceptional-set criterion. The mass-index fit remains exploratory and is not a predictive law.

## Workstream D — Cross-model bridge

No equivalence between the SU(2)-connection operators and signed-Z2-flux Laplacians is assumed. A valid bridge must define a map between the exact operator families and prove which spectra, traces, boundary data, or other quantities it preserves. Until such a result exists, the two models remain separate mathematical workstreams.

## Workstream E — Exact scalar-invariant limit

**Source:** [RFT-SIRM/RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis)

The separately defined scalar invariant has an exact finite-level remainder and Lean-checked limit theorem rftInvariant_tendsto, merged at source commit 2a7782a8a56181313808019202089f167cf09cc2. It is maintained separately from both operator families and does not establish a physical cosmological law.

## Current execution order

1. Keep the current evidence matrix and source SHA pins synchronized.
2. Finish the synthesis PR by passing documentation, exact arithmetic, modular/CRT, and pinned Lean CI on the same head.
3. Consider Lean-kernel formalization of the H6/H8 finite base bridges.
4. Derive an explicit H10 correction polynomial if that form is mathematically useful.
5. Continue the remaining Phi-Genesis spectral questions without upgrading quadratic-form statements to eigenvalue theorems.
6. Attempt a cross-model theorem only after a precise candidate map has been stated and tested.