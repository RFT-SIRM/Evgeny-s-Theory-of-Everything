# Open problems

The current proven results and their exact boundaries are recorded in [CURRENT_EVIDENCE.md](CURRENT_EVIDENCE.md). The following items are the remaining work, not a claim that every higher-moment recurrence is still open.

## OP-1 — Lean-kernel closure of the H6 and H8 base transitions

For the SU(2)-connected Sierpiński-gasket operators, Lean already proves the all-angle H6 and H8 recurrences for every transition m ≥ 3, with affine forms from level 3. The finite 2→3 transitions are supplied by exact polynomial certificates:

- H6: [p6_level3_orientation_certificate.py in the pinned Evgeny-Theorem source](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/computational/p6_level3_orientation_certificate.py);
- H8: [p8_base_certificate.py in the pinned Evgeny-Theorem source](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/computational/p8_base_certificate.py).

These are exact algebraic verifications, not numerical fits, but they are not yet Lean-kernel theorems. The next task is to formalize these finite polynomial identities in Lean without creating an unmaintainable proof term. The earlier [Evgeny-Theorem PR #11](https://github.com/RFT-SIRM/Evgeny-Theorem/pull/11) is closed without merge and was superseded by later source work; it is provenance, not an outstanding integration PR.

## OP-2 — Explicit trigonometric form of the H10 correction [OPEN — CANDIDATE FORMS ONLY, 23 NOVEMBER 2026]

The unconditional H10 recurrence and affine form remain Lean-proved from levels 4 and 5 respectively. The report records a proposed polynomial and Fourier expression. The external script proves only that these two supplied forms are equivalent in \(\\mathbb Z[c,s]/(c^2+s^2-1)\) and checks their endpoint arithmetic against supplied trace values. It does not prove that the proposed polynomial equals `defectO10_num_residual_constant`, the pinned Lean source definition of the recurrence constant. Deriving or independently verifying that equality for all real angles is still the open task; see computational/H10_EXACT_RESIDUAL_2026-11-23.md.

## OP-3 — Extend path-class cancellation beyond the first gasket

The H6 first-level closed-walk classification is a finite exact calculation. Determine whether its cancellation pattern extends to higher graph levels or to H8/H10. Any generalization must classify the relevant walks and prove the cancellation algebraically.

## OP-4 — Phi-Genesis operator eigenvalue and spectral-law closure

Phi-Genesis has formalized the Schur corner-response recursion, strict pivot positivity, shifted quadratic-form bounds, A1-root uniqueness, identification of the selected A1 root with the least eigenvalue of its internally defined `Q_{6+n}`, and convergence of the least-eigenvalue sequence (also transferred to the signed matrix by gauge conjugacy). The next questions are separate:

1. prove a quantitative uniform tail estimate and identify the limiting constant explicitly;
2. prove or refute the proposed quadratic root-shift asymptotic;
3. complete the Gate A exceptional-set criterion;
4. extend any desired statements to small levels outside the current theorem range;
5. establish the exact relation, if any, to the external theta=2π local-face operator.

The eigenvalue/convergence milestones are in [PR #30](https://github.com/RFT-SIRM/Phi-Genesis/pull/30) through [PR #33](https://github.com/RFT-SIRM/Phi-Genesis/pull/33); earlier Schur milestones are [PR #25](https://github.com/RFT-SIRM/Phi-Genesis/pull/25) through [PR #29](https://github.com/RFT-SIRM/Phi-Genesis/pull/29).

## OP-5 — Complete Gate A exceptional-set criterion

Characterize the full exceptional set for spectral decimation, including recursively generated preimages where relevant. Simple exclusion of a finite list is not a complete criterion. Preserve residual mismatches and negative results.

## OP-6 — Cross-model relationship

Determine whether there is a precise map between the SU(2)-connected operators and the signed-Z2-flux Laplacians. Specify the map, domains, boundary conditions, and the spectral or trace quantities it preserves, then prove the claim. Until then, the models remain distinct.

## OP-7 — Reproducible source verification

The synthesis Lean workflow must build the pinned Evgeny-Theorem source SHA listed in [CURRENT_EVIDENCE.md](CURRENT_EVIDENCE.md). Re-run the documentation audit, exact modular certificate, arithmetic audit, and pinned Lean build on the final PR head. Do not describe the external exact H6/H8 certificates as Lean proofs.