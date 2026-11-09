# Source repositories and provenance

## 1. SU(2)-connected graph operators

URL: [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem)  
Pinned revision: [4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f)

Current evidence boundary:
- H4 all-angle closed formula is Lean-checked for every m ≥ 1.
- H6 and H8 recurrences/affine forms are Lean-checked from m ≥ 3; finite 2→3 bridges are exact polynomial certificates outside Lean's kernel.
- H10 radius-four transport through degree nine and unconditional affine recurrence/form are Lean-checked for m ≥ 4/m ≥ 5; the level-five residual remains a trace expression.
- Successful source Lean build [run 42481191661](https://github.com/RFT-SIRM/Evgeny-Theorem/actions/runs/42481191661) is on a7b732a; the 14 later commits to the pinned revision changed documentation/HTML only.
- H6 finite-bridge formalization is discussed in [PR #11](https://github.com/RFT-SIRM/Evgeny-Theorem/pull/11); do not conflate an exact external certificate with a Lean proof.

## 2. Signed-Z2-flux spectral decimation

URL: [RFT-SIRM/Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis)  
Pinned revision: [a80cc8a08ce68bb945d0867fbdfcbea74a20c20f](https://github.com/RFT-SIRM/Phi-Genesis/commit/a80cc8a08ce68bb945d0867fbdfcbea74a20c20f)

Current evidence boundary:
- Schur corner-response and matrix-to-Schur bridge are recorded in merged PRs #21–#26.
- Strict pivot positivity in the bootstrap window was merged in PR #27.
- Shifted quadratic-form interval/nonnegativity results for levels at least 6 were merged in PR #28.
- A1-root uniqueness and convergence of selected roots as Rayleigh minima of the shifted quadratic form were merged in PR #29.
- These statements do not yet prove the operator eigenvalue formulation, the proposed quadratic law, or the cases below level 6.
- Gate A's full exceptional-set criterion remains open; the mass-index fit is not an established predictive law.

## 3. Exact scalar-invariant limit

URL: [RFT-SIRM/RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis)  
Source commit: [2a7782a8a56181313808019202089f167cf09cc2](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/commit/2a7782a8a56181313808019202089f167cf09cc2)

Formal result: PR #3 merged on 16 October 2026. Lean theorem rftInvariant_tendsto, exact remainder rftInvariant_remainder, and exact decomposition rftInvariant_exact_decomposition; post-merge Lean CI [run 38904548580](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/actions/runs/38904548580).

Boundary: this result proves the limit and exact finite-level remainder for the defined scalar formula only. It does not establish an observational fit, physical cosmological interaction, or bridge to either operator family above.

## Provenance requirements

For every imported result, record the source path and URL, exact source commit, theorem names and assumptions, whether it was copied or rechecked, successful CI evidence, and any difference between source and synthesis statements. Do not claim independent reproduction merely because a theorem or file appears in a source repository.