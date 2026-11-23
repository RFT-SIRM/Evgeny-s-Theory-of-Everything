# Open problems

The current proven results and their exact boundaries are recorded in [CURRENT_EVIDENCE.md](CURRENT_EVIDENCE.md). The H10 finite coefficient derivation is no longer open computationally: it has an exact source-reconstructed external CRT certificate. The remaining items concern formalization, structural explanations, and separate research strands.

## OP-1 — Lean-kernel closure of the H6 and H8 base transitions

For the SU(2)-connected Sierpiński-gasket operators, Lean proves the all-angle H6 and H8 recurrences for every transition m ≥ 3, with affine forms from level 3. Their finite 2→3 transitions are supplied by exact polynomial certificates:

- H6: [p6_level3_orientation_certificate.py in the pinned Evgeny-Theorem source](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/computational/p6_level3_orientation_certificate.py);
- H8: [p8_base_certificate.py in the pinned Evgeny-Theorem source](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/computational/p8_base_certificate.py).

These are exact algebraic verifications, not numerical fits, but they are not Lean-kernel theorems. The remaining formalization task is to prove these finite polynomial identities in Lean without creating an unmaintainable proof term. The earlier [Evgeny-Theorem PR #11](https://github.com/RFT-SIRM/Evgeny-Theorem/pull/11) is closed without merge and was superseded by later source work.

## OP-2 — Lean-kernel formalization of the H10 finite coefficient expansion

The H10 level-five correction is now computed from the pinned source definitions, rather than inferred from supplied candidate coefficients. The executable C++ engine rebuilds the level-five and level-six graph/operator matrices from the recursive graph, face-flux, vertex-order, orientation, and SU(2) definitions. A sparse exact length-ten path expansion is computed modulo three primes; signed coefficient-wise CRT reconstructs the integer polynomial under a path-count bound, with the modulus product exceeding twice that bound. The result is reproduced by the workflow and checked against the committed JSON artifact.

The all-angle identity between the Lean recurrence constant and D6−3D5 is Lean-checked. The coefficient expansion itself is an **exact external certificate**, not a Lean-kernel theorem. The remaining task is to formalize that finite expansion in Lean if a maintainable kernel-level proof is feasible. See [the H10 source-reconstruction report](computational/H10_EXACT_RESIDUAL_2026-11-23.md).

## OP-3 — Extend path-class cancellation beyond the first gasket

The H6 first-level closed-walk classification is a finite exact calculation. Determine whether its cancellation pattern extends to higher graph levels or to H8/H10. Any generalization must classify the relevant walks and prove the cancellation algebraically.

## OP-4 — Phi-Genesis quantitative spectral asymptotics and exceptional set

Phi-Genesis has Lean-checked the selected A1 root as the least eigenvalue of its internally defined Q_{6+n}, convergence of the least-eigenvalue sequence, and transfer to the gauge-equivalent signed matrix. The next questions are separate:

1. prove a quantitative uniform tail estimate and identify the limiting constant explicitly;
2. prove or refute the proposed quadratic root-shift asymptotic;
3. complete the Gate A exceptional-set criterion;
4. extend any desired statements to levels outside the current theorem range;
5. establish the exact relation, if any, to the external theta=2π local-face operator.

The eigenvalue/convergence milestones are in [PR #30](https://github.com/RFT-SIRM/Phi-Genesis/pull/30) through [PR #33](https://github.com/RFT-SIRM/Phi-Genesis/pull/33); earlier Schur milestones are [PR #25](https://github.com/RFT-SIRM/Phi-Genesis/pull/25) through [PR #29](https://github.com/RFT-SIRM/Phi-Genesis/pull/29).

## OP-5 — Complete Gate A exceptional-set criterion

Characterize the full exceptional set for spectral decimation, including recursively generated preimages where relevant. Simple exclusion of a finite list is not a complete criterion. Preserve residual mismatches and negative results.

## OP-6 — Cross-model relationship

Determine whether there is a precise map between the SU(2)-connected operators and the signed-Z2-flux Laplacians. Specify the map, domains, boundary conditions, and the spectral or trace quantities it preserves, then prove the claim. Until then, the models remain distinct.

## OP-7 — Reproducible source verification

Keep the source-reconstruction C++ engine, Python CRT verifier, committed JSON, and CI workflow synchronized with the pinned Evgeny-Theorem SHA in CURRENT_EVIDENCE.md. The workflow must rebuild the finite traces, verify the CRT bound, and compare the generated artifact. Do not describe the external exact H6/H8/H10 certificates as Lean-kernel proofs.
