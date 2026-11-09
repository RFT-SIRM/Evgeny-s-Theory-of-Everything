# Current research status

**Status as of 9 November 2026:** the synthesis archive is being updated to reflect formal results added after its October snapshot. H4 is fully Lean-checked; H6/H8 have Lean recurrences from level 3 plus exact external base-transition certificates; H10 has an unconditional Lean recurrence from level 4 and affine form from level 5. The signed-Z2 Schur/Rayleigh results are a separate workstream.

## Source and verification snapshot

- Synthesis repository base: [aa7d3e2efe0a7d7e2a929320a2683d37b11ee8fe](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/commit/aa7d3e2efe0a7d7e2a929320a2683d37b11ee8fe).
- SU(2) source: [RFT-SIRM/Evgeny-Theorem at 4ccfae17](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f).
- Latest successful Lean formalization build for the same Lean source state: [run 42481191661](https://github.com/RFT-SIRM/Evgeny-Theorem/actions/runs/42481191661), on a7b732a…; the 14 commits from that build to 4ccfae… change documentation/HTML only.
- Lean toolchain: leanprover/lean4:v4.33.1; Mathlib: v4.33.1.
- Signed-flux source: [RFT-SIRM/Phi-Genesis at a80cc8a0](https://github.com/RFT-SIRM/Phi-Genesis/commit/a80cc8a08ce68bb945d0867fbdfcbea74a20c20f).
- Separate scalar-invariant source: [RFT-SIRM/RFT-Cosmology-Genesis at 2a7782a8](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/commit/2a7782a8a56181313808019202089f167cf09cc2).

## Established results

1. **H4:** all-angle closed formula for every level m ≥ 1, Lean-checked in Evgeny-Theorem.
2. **H6:** all-angle Lean recurrence and affine form for every m ≥ 3. The finite 2→3 transition is supplied by an exact Gaussian-integer polynomial certificate, not yet a Lean-kernel theorem.
3. **H8:** all-angle Lean recurrence and affine form for every m ≥ 3. The finite 2→3 transition is supplied by an exact sparse-polynomial certificate, not yet a Lean-kernel theorem.
4. **H10:** radius-four glued-state diagonal transport through degree nine is Lean-proved for all m ≥ 4; the all-angle recurrence is unconditional for m ≥ 4, and the affine formula is unconditional for m ≥ 5. The level-five constant remains an exact trace expression.
5. **Phi-Genesis:** the Schur and bootstrap programme includes strict pivot positivity, shifted quadratic-form bounds for levels at least 6, uniqueness of the A1 root in the bootstrap window, and convergence of selected roots as Rayleigh minima. It is not yet an operator eigenvalue theorem.
6. **Scalar invariant:** the separately defined scalar invariant has a Lean-checked exact limit and finite-level remainder in RFT-Cosmology-Genesis.

## Still open

- Lean-kernel proofs of the finite H6 and H8 2→3 certificates.
- An explicit trigonometric/Fourier expansion of the exact H10 level-five trace correction.
- An all-level path-class explanation for higher-moment cancellation.
- Phi-Genesis operator eigenvalue identification, proposed quadratic law, and the small-level extension.
- Complete Gate A exceptional-set characterization.
- Any proved bridge between the SU(2) and signed-Z2 operator families.

## Merge decision

This repository can be released as a carefully sourced research synthesis once its PR checks pass on one head commit. It must not be described as a completed universal theory or as proving equivalence between its distinct operator models. The integration PR updates the pinned source reference and evidence ledger; it does not modify either upstream source project.