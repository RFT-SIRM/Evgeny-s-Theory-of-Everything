# Current evidence snapshot

**Snapshot date: 23 November 2026.** This file is the authoritative current status of the research strands represented in this synthesis archive. The repository title names a research programme; it is not a claim that a universal theory or a cross-model theorem has been completed.

## 1. Pinned source projects

| Workstream | Exact source revision | Verification boundary |
|---|---|---|
| SU(2)-connected Sierpiński-gasket operators | [Evgeny-Theorem @ 4ccfae17](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f) | Lean 4.33.1 / Mathlib 4.33.1. Latest successful source Lean build: [run 42481191661](https://github.com/RFT-SIRM/Evgeny-Theorem/actions/runs/42481191661), on a7b732a04d1b4e619cd050b2b643daf491e86fa2. A GitHub compare confirms the 14 commits from that build to 4ccfae changed documentation/HTML only, not Lean source. |
| Signed-Z2-flux spectral decimation | [Phi-Genesis @ a80cc8a0](https://github.com/RFT-SIRM/Phi-Genesis/commit/a80cc8a08ce68bb945d0867fbdfcbea74a20c20f) | Pinned Lean source includes the later merged eigenvalue-identification, least-eigenvalue convergence, and signed/signless transfer results (#30–#33). Scope remains the internally defined graph matrices; this is not yet an equivalence to the external SU(2) operator model. |
| Exact scalar-invariant limit | [RFT-Cosmology-Genesis @ 2a7782a8](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/commit/2a7782a8a56181313808019202089f167cf09cc2) | Merged PR #3; post-merge Lean build [run 38904548580](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/actions/runs/38904548580). This is a distinct theorem about a separately defined scalar formula. |

The synthesis Lean workflow checks out the pinned Evgeny-Theorem source and runs its library build. It does not compile Phi-Genesis or RFT-Cosmology-Genesis as part of the same Lean package.

**Pin check, 18 November 2026.** The three source projects have moved since the pins above, but their Lean sources have not. Comparing each pin with the current `main` shows: Evgeny-Theorem at `35dcd3e` differs from `4ccfae17` only in two documentation files (no `.lean`, `lakefile`, `lean-toolchain` or `lake-manifest.json` change); Phi-Genesis at `b8fa4a1` has no `.lean`, `lakefile.lean`, `lean-toolchain` or `lake-manifest.json` change since `a80cc8a0` (documentation, workflows and numerical records only); RFT-Cosmology-Genesis at `86be521` has no change under `formalization/` since `2a7782a8` (documentation, Python diagnostics and Planck/CAMB records only). The pins therefore still identify the Lean source state of each theorem. They were not moved, because a newer pin would assert a Lean build of a revision that this archive's workflow has not built.

## 2. SU(2) trace-moment results

The authoritative definitions of the graph, operators, edge connections, orientations, and trace defects are in the pinned Evgeny-Theorem source. The declarations below are source Lean declarations; this archive records their scope rather than duplicating their proofs.

| Moment | Lean-checked result | Remaining boundary |
|---|---|---|
| H4 | traceDefect_closed: all-angle identity \(\Delta_m(H^4,\theta)=-16(3^{m-1}+1)\sin^2(\theta/2)\), for every \(m\ge1\). | No remaining gap for this stated theorem. |
| H6 | defectO6_num_growth_recurrence and defectO6_num_affine_growth: all-angle recurrence and affine form for every \(m\ge3\). The exact residual is defectO6_num_residual_constant. | The finite \(2\to3\) transition is supplied by exact Gaussian-integer polynomial arithmetic in computational/p6_level3_orientation_certificate.py. It is an exact external certificate, not a Lean-kernel theorem. Combining it with the Lean recurrence gives the all-angle formula from \(m\ge2\). |
| H8 | defectO8_succ_num_level4_constant_boundary and defectO8_num_affine_closed_form_from_level3: all-angle recurrence and affine form from \(m\ge3\). The exact residual is defectO8_num_residual_constant. | The finite \(2\to3\) transition is supplied by the exact sparse-polynomial certificate computational/p8_base_certificate.py. This certificate is not yet a Lean-kernel theorem. |
| H10 | H10TransportAll_proved establishes radius-four glued-state diagonal transport through degree 9 for both axis configurations, for all \(m\ge4\). defectO10_succ_num_level5_constant_boundary_unconditional proves the recurrence for \(m\ge4\); defectO10_num_affine_closed_form_from_level5_unconditional proves the affine form for \(m\ge5\). | The level-five recurrence constant is \(C_{10}^{(5)}=D_6-3D_5\). A direct C++ mirror of the pinned graph/operator definitions reconstructs the level-five/six trace polynomials over three primes; signed coefficient-wise CRT recovers the exact polynomial. This is an exact external certificate, not a Lean-kernel coefficient theorem. | Lean-kernel formalization of the finite coefficient expansion, if a maintainable proof is feasible. |

### H10 level-five correction — exact source-reconstructed coefficient

The pinned Lean recurrence gives the level-five constant as \(C_{10}^{(5)}=D_6-3D_5\). The executable source mirror follows the pinned graph recursion, vertex ordering, face/flux indexing, orientation-dependent matrix entries, and the three Pauli-axis SU(2) rotations. It computes the sparse length-ten trace expansion for levels 5 and 6 modulo the primes 10000453, 20000569, and 30000769. With maximum row coefficient \(\ell^1\)-norm 10, the signed coefficient bound is 87,720,000,000,000; the CRT modulus product is 6,000,596,319,075,658,215,133, exceeding twice that bound. Therefore every recovered integer coefficient is unique. The resulting polynomial and Fourier expression are recorded in the H10 report and machine-readable certificate. The all-angle identity between the Lean recurrence constant and \(D_6-3D_5\) is Lean-checked; the finite coefficient expansion itself is an exact external CRT certificate, not a Lean-kernel theorem.

### Source map

- H6/H8 recurrence and affine-form proofs: [FinalTilde.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/formalization/EvgenyTheorem/FinalTilde.lean).
- Tenth-moment gluing: [GlueTrace10.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/formalization/EvgenyTheorem/GlueTrace10.lean).
- Glued-row transport: [GlueRows10.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/formalization/EvgenyTheorem/GlueRows10.lean).
- Orientation/level recurrence: [FinalOrient10.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/formalization/EvgenyTheorem/FinalOrient10.lean).
- Unconditional H10 transport and affine form: [FinalClosed10.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/formalization/EvgenyTheorem/FinalClosed10.lean).
- Corner order/orientation support: [CornerLocality.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/formalization/EvgenyTheorem/CornerLocality.lean).

The finite H6/H8 certificates are maintained in the pinned Evgeny-Theorem source, not in this synthesis repository. [Evgeny-Theorem PR #11](https://github.com/RFT-SIRM/Evgeny-Theorem/pull/11) is closed without merge; its work was superseded by the later source state. An exact external certificate must not be described as a Lean-kernel theorem.

## 3. Signed-Z2-flux spectral-decimation results

This is a distinct operator family; these claims do not prove an SU(2) trace-moment identity.

- The graph-matrix/Schur-boundary and corner-response construction is represented by merged Schur bridge and response PRs #21–#26.
- PR #27 proves strict positivity of the relevant Schur pivots in the bootstrap window.
- PR #28 proves shifted quadratic-form bounds for levels at least 6.
- PR #29 proves uniqueness of the A1 root in the bootstrap window and convergence of selected roots as Rayleigh minima of the shifted quadratic form.

This is not yet an operator eigenvalue theorem. The eigenvalue formulation, explicit closed form, proposed quadratic law, and small levels \(N<6\) remain open. Gate A's complete exceptional-set criterion remains open; the mass-index fit is not an established predictive law.

## 4. Separate scalar-invariant theorem

The page [exact_invariant_limit.md](theorems/exact_invariant_limit.md) records the exact limit and finite-level remainder for the scalar invariant defined in RFT-Cosmology-Genesis. It does not establish a physical cosmological law or a bridge to either operator family.

## 5. Remaining mathematical tasks

1. Formalize the exact finite \(2\to3\) H6 and H8 transition certificates in Lean, if a maintainable kernel-level proof is feasible.
2. Formalize the exact finite H10 coefficient reconstruction in Lean, if a maintainable kernel-level proof is feasible; the source-reconstructed modular/CRT certificate is already complete.
3. Extend the H6 path-class cancellation result beyond the finite first-level calculation.
4. Complete Phi-Genesis Gate A and the full exceptional-set criterion.
5. Establish a quantitative uniform tail estimate and prove or refute the proposed quadratic root-shift asymptotic in Phi-Genesis; least-eigenvalue identification and convergence are already Lean-checked for its internal graph matrices.
6. Prove a precise bridge between the SU(2)-connected operators and signed-Z2-flux Laplacians, if such a bridge exists.

## 6. Evidence policy

- **LEAN-CHECKED:** the proposition compiles in the pinned Lean/Mathlib environment under its stated hypotheses.
- **EXACT EXTERNAL CERTIFICATE:** a finite algebraic identity is verified by exact reproducible code but is not checked by Lean's kernel.
- **NUMERICAL HOLDOUT:** a finite computation tests a prediction; it is not an all-level proof.
- **OPEN:** no sufficient proof/certificate is recorded.

A green CI run validates only the assertions exercised by that workflow. It does not turn an external certificate into a Lean theorem, upgrade a quadratic-form result to an operator eigenvalue theorem, or prove equivalence of distinct operator models.

## 7. Merge criterion

The evidence snapshot is tied to the exact source pins above. The synthesis integration PR #5 has already been merged; its documentation/reference audit, exact modular certificate, and pinned Lean build passed on the merged commit. This documentation update does not modify any upstream source project.