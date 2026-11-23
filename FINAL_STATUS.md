# Current research status

**Status as of 23 November 2026:** H4 is Lean-checked; H6/H8 have Lean recurrences from level 3 plus exact external base-transition certificates; H10 has an unconditional Lean recurrence from level 4, affine form from level 5, and an exact source-reconstructed external CRT certificate for its level-five coefficient. The finite coefficient expansion is not a Lean-kernel theorem. The signed-Z2 results are a separate operator family.

## Source and verification snapshot

- Synthesis repository snapshot before this documentation branch: [7f95dd9ce95ee040b2796671be2b6255b509818c](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/commit/7f95dd9ce95ee040b2796671be2b6255b509818c).
- SU(2) source: [RFT-SIRM/Evgeny-Theorem at 4ccfae17](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f).
- Latest successful Lean formalization build for the same Lean source state: [run 42481191661](https://github.com/RFT-SIRM/Evgeny-Theorem/actions/runs/42481191661), on a7b732a…; the 14 commits from that build to 4ccfae… change documentation/HTML only.
- Lean toolchain: leanprover/lean4:v4.33.1; Mathlib: v4.33.1.
- Signed-flux source: [RFT-SIRM/Phi-Genesis at a80cc8a0](https://github.com/RFT-SIRM/Phi-Genesis/commit/a80cc8a08ce68bb945d0867fbdfcbea74a20c20f).
- Separate scalar-invariant source: [RFT-SIRM/RFT-Cosmology-Genesis at 2a7782a8](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/commit/2a7782a8a56181313808019202089f167cf09cc2).

## Established results

1. **H4:** all-angle closed formula for every level m ≥ 1, Lean-checked in Evgeny-Theorem.
2. **H6:** all-angle Lean recurrence and affine form for every m ≥ 3. The finite 2→3 transition is supplied by an exact Gaussian-integer polynomial certificate, not yet a Lean-kernel theorem.
3. **H8:** all-angle Lean recurrence and affine form for every m ≥ 3. The finite 2→3 transition is supplied by an exact sparse-polynomial certificate, not yet a Lean-kernel theorem.
4. **H10:** radius-four glued-state diagonal transport through degree nine is Lean-proved for all m ≥ 4; the all-angle recurrence is unconditional for m ≥ 4, and the affine formula is unconditional for m ≥ 5. The level-five correction is reconstructed from the pinned finite graph/operator definitions by a three-prime modular computation and signed CRT, with a uniqueness bound. The finite coefficient expansion is an exact external certificate, not a Lean-kernel theorem.
5. **Phi-Genesis:** Lean identifies the selected A1 root with the least eigenvalue of the internally defined `Q_{6+n}`, proves convergence of the least-eigenvalue sequence, and transfers it to the signed matrix by gauge conjugacy. This does not prove equivalence with the external theta=2π local-face operator.
6. **Scalar invariant:** the separately defined scalar invariant has a Lean-checked exact limit and finite-level remainder in RFT-Cosmology-Genesis.

## Still open

- Lean-kernel proofs of the finite H6 and H8 2→3 certificates.
- A Lean-kernel formalization of the finite H10 coefficient expansion, if a maintainable proof is feasible.
- An all-level path-class explanation for higher-moment cancellation.
- Phi-Genesis quantitative uniform tail bound, explicit limiting-constant identification, proposed quadratic root-shift law, Gate A exceptional-set characterization, and small-level extension.
- Complete Gate A exceptional-set characterization.
- Any proved bridge between the SU(2) and signed-Z2 operator families.

## Merge decision

This repository is maintained as a carefully sourced research synthesis, not as a completed universal theory and not as a claim of equivalence between the distinct operator models. The H10 source-reconstruction files, report, exact artifact, and CI workflow are published together on main.