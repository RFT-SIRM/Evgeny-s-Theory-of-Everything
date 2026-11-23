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

## OP-8 — All-level H12 transition recurrence

An exact source-mirrored three-prime signed CRT computation reconstructs the degree-12 transition residuals for levels m=3,4,5,6,7 and establishes the finite identities C12^(3)=C12^(4)=C12^(5)=C12^(6)=C12^(7). The common polynomial, Fourier form, level-8 graph counts, canonical coefficient bounds, and reproduction commands are recorded in [H12_FINITE_RESIDUAL_2026-11-23.md](computational/H12_FINITE_RESIDUAL_2026-11-23.md), with the machine-readable result in [h12_residual_certificate.json](computational/data/h12_residual_certificate.json).

This is finite-level external exact evidence, not an all-level recurrence and not a Lean-kernel theorem. The remaining task is to prove the radius-five corner transport and degree-12 boundary expansion uniformly in m, derive the all-level recurrence with explicit starting index, and formalize the result in Lean.


### H12 degree-12 boundary-word reduction

The 12th-power noncommutative trace expansion has 2,048 ordered composition terms. At the exceptional level-3 corner distance 8, exactly 48 terms can contain an off-diagonal corner-power block (24 with odd and 24 with even numbers of gluing factors). From level 4 onward the corner distance is 16, exceeding every exponent 1 through 11, so all terms reduce to diagonal 2x2 corner moments. The exact inventory and boundary-projection formula are in [H12_BOUNDARY_WORD_EXPANSION_2026-11-23.md](computational/H12_BOUNDARY_WORD_EXPANSION_2026-11-23.md). Still required: instantiate and verify the exact boundary matrix blocks, prove radius-five operator-labelled transport uniformly, and formalize the contraction.

## OP-8 progress — degree-12 boundary contraction (23 November 2026)

The trace-word reduction for H12 is now closed conditionally on the source gluing/locality hypotheses: odd numbers of N factors vanish, and even strata reduce to 2×2 diagonal corner-block products. The apparent 48 long-gap cases at the level-3 transition do not create off-diagonal trace terms. Radius-five locality has a paper-level recursive argument and independent finite audits, but has not yet been formalized in Lean. Remaining work: complete the H12 copy-A/B/C transfer bookkeeping, deduce the all-level constant boundary correction for every m ≥ 3, and formalize the radius-five and degree-12 trace-word arguments in Lean. The finite CRT certificate through level 8 remains external evidence, not a kernel theorem. See [H12 boundary-contraction report](computational/H12_BOUNDARY_DIAGONAL_CONTRACTION_2026-11-23.md).
