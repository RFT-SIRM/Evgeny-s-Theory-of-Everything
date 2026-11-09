# Open problems

The current proven results and their exact boundaries are recorded in [CURRENT_EVIDENCE.md](CURRENT_EVIDENCE.md). The following items are the remaining work, not a claim that every higher-moment recurrence is still open.

## OP-1 — Lean-kernel closure of the H6 and H8 base transitions

For the SU(2)-connected Sierpiński-gasket operators, Lean already proves the all-angle H6 and H8 recurrences for every transition m ≥ 3, with affine forms from level 3. The finite 2→3 transitions are supplied by exact polynomial certificates:

- H6: computational/p6_level3_orientation_certificate.py;
- H8: computational/p8_base_certificate.py.

These are exact algebraic verifications, not numerical fits, but they are not yet Lean-kernel theorems. The next task is to formalize these finite polynomial identities in Lean without creating an unmaintainable proof term. See [Evgeny-Theorem PR #11](https://github.com/RFT-SIRM/Evgeny-Theorem/pull/11) for the source discussion.

## OP-2 — Explicit trigonometric form of the H10 correction

The unconditional H10 recurrence and affine form are proved in Lean from levels 4 and 5 respectively. The correction defectO10_num_residual_constant is currently an exact finite level-five trace expression. Expand and certify it as an explicit trigonometric/Fourier polynomial, or document why the trace-expression form is the preferred canonical statement.

## OP-3 — Extend path-class cancellation beyond the first gasket

The H6 first-level closed-walk classification is a finite exact calculation. Determine whether its cancellation pattern extends to higher graph levels or to H8/H10. Any generalization must classify the relevant walks and prove the cancellation algebraically.

## OP-4 — Phi-Genesis operator eigenvalue and spectral-law closure

Phi-Genesis has formalized the Schur corner-response recursion, strict pivot positivity in the bootstrap window, shifted quadratic-form bounds for levels at least 6, uniqueness of the A1 root in that window, and convergence of selected roots as Rayleigh minima. The next questions are separate:

1. identify the A1 Rayleigh minimum with the bottom eigenvalue of the specified graph matrix;
2. prove or refute the proposed quadratic law;
3. extend the argument to the remaining small levels N < 6;
4. keep closed-form claims separate from the convergence theorem.

The relevant merged milestones are [PR #25](https://github.com/RFT-SIRM/Phi-Genesis/pull/25) through [PR #29](https://github.com/RFT-SIRM/Phi-Genesis/pull/29).

## OP-5 — Complete Gate A exceptional-set criterion

Characterize the full exceptional set for spectral decimation, including recursively generated preimages where relevant. Simple exclusion of a finite list is not a complete criterion. Preserve residual mismatches and negative results.

## OP-6 — Cross-model relationship

Determine whether there is a precise map between the SU(2)-connected operators and the signed-Z2-flux Laplacians. Specify the map, domains, boundary conditions, and the spectral or trace quantities it preserves, then prove the claim. Until then, the models remain distinct.

## OP-7 — Reproducible source verification

The synthesis Lean workflow must build the pinned Evgeny-Theorem source SHA listed in [CURRENT_EVIDENCE.md](CURRENT_EVIDENCE.md). Re-run the documentation audit, exact modular certificate, arithmetic audit, and pinned Lean build on the final PR head. Do not describe the external exact H6/H8 certificates as Lean proofs.