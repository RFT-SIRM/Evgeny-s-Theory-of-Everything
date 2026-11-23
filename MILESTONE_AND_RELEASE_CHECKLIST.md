# Research milestone and release checklist

## Current milestone: formally proved recurrences with explicit evidence boundaries

**Status:** H4 is fully Lean-checked; H6/H8 recurrences are Lean-proved from level 3 with exact external finite base-transition certificates; H10 has an unconditional Lean recurrence from level 4 and affine form from level 5. Proposed polynomial/Fourier forms for its finite level-five coefficient are recorded and mutually checked, but equality to the Lean residual definition remains open; Phi-Genesis additionally has Lean-checked least-eigenvalue identification and convergence for its internal graph matrices; this remains distinct from the SU(2) operator family.

## Established and verified

- [x] H4 all-angle closed form for every level m ≥ 1 in Lean.
- [x] H6 all-angle Lean recurrence and affine form for m ≥ 3.
- [x] Exact H6 2→3 Gaussian-integer polynomial certificate.
- [x] H8 all-angle Lean recurrence and affine form for m ≥ 3.
- [x] Exact H8 2→3 sparse-polynomial certificate.
- [x] H10 radius-four glued-state diagonal transport through degree nine, both axis configurations, all m ≥ 4.
- [x] H10 unconditional Lean recurrence for m ≥ 4 and affine formula for m ≥ 5.
- [ ] Establish that the proposed H10 polynomial/Fourier forms equal `defectO10_num_residual_constant`; the current checker tests only mutual equivalence and supplied endpoint arithmetic.
- [x] Phi-Genesis Schur bridge, strict pivot positivity, shifted quadratic-form bootstrap, A1 root uniqueness, least-eigenvalue identification, and convergence of least eigenvalues for its internal graph matrices.
- [x] Separate scalar-invariant limit and exact remainder theorem in RFT-Cosmology-Genesis.
- [x] Existing numerical holdouts, sparse trace checks, and exact modular/CRT finite-level certificates retained as independent regression evidence.

## Remaining mathematical work

- [ ] Formalize the finite H6 2→3 bridge in Lean.
- [ ] Formalize the finite H8 2→3 bridge in Lean.
- [ ] Extend H6 path-class cancellation beyond the finite first-level calculation.
- [ ] Prove a quantitative uniform tail bound and establish/refute the proposed quadratic root-shift law in Phi-Genesis.
- [ ] Complete the Phi-Genesis Gate A exceptional-set characterization.
- [ ] Prove any proposed SU(2)/signed-Z2 cross-model bridge.

## Integration PR acceptance checklist

- [x] Pin the source Evgeny-Theorem revision to 4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f.
- [ ] Ensure all summary documents agree with [CURRENT_EVIDENCE.md](CURRENT_EVIDENCE.md).
- [ ] Pass documentation/reference audit on the final documentation PR head.
- [ ] Pass exact modular/CRT certificate workflow on the final documentation PR head.
- [ ] Pass arithmetic audit and its regression tests on the final documentation PR head.
- [ ] Pass the pinned Lean build on the final documentation PR head.
- [ ] Review the full diff for obsolete claims and broken links.

## Release policy

The archive may be released as a rigorously sourced research synthesis after its PR checks pass. It must not be tagged as a completed universal Theory of Everything, and it must not claim equivalence between the SU(2) and signed-Z2 operator models.