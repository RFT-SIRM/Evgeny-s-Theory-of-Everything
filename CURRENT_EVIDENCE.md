# Current evidence snapshot

**Snapshot date: 9 November 2026.** This file is the authoritative current status of the research strands represented in this synthesis archive. The repository title names a research programme; it is not a claim that a universal theory or a cross-model theorem has been completed.

## 1. Pinned source projects

| Workstream | Exact source revision | Verification boundary |
|---|---|---|
| SU(2)-connected Sierpiński-gasket operators | [Evgeny-Theorem @ 4ccfae17](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f) | Lean 4.33.1 / Mathlib 4.33.1. Latest successful source Lean build: [run 42481191661](https://github.com/RFT-SIRM/Evgeny-Theorem/actions/runs/42481191661), on a7b732a04d1b4e619cd050b2b643daf491e86fa2. A GitHub compare confirms the 14 commits from that build to 4ccfae changed documentation/HTML only, not Lean source. |
| Signed-Z2-flux spectral decimation | [Phi-Genesis @ a80cc8a0](https://github.com/RFT-SIRM/Phi-Genesis/commit/a80cc8a08ce68bb945d0867fbdfcbea74a20c20f) | Schur/Rayleigh PRs #25–#29 are merged; their PR-head Lean runs passed. Scope: quadratic-form and Rayleigh-minimum statements under their stated hypotheses. |
| Exact scalar-invariant limit | [RFT-Cosmology-Genesis @ 2a7782a8](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/commit/2a7782a8a56181313808019202089f167cf09cc2) | Merged PR #3; post-merge Lean build [run 38904548580](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/actions/runs/38904548580). This is a distinct theorem about a separately defined scalar formula. |

The synthesis Lean workflow checks out the pinned Evgeny-Theorem source and runs its library build. It does not compile Phi-Genesis or RFT-Cosmology-Genesis as part of the same Lean package.

## 2. SU(2) trace-moment results

The authoritative definitions of the graph, operators, edge connections, orientations, and trace defects are in the pinned Evgeny-Theorem source. The declarations below are source Lean declarations; this archive records their scope rather than duplicating their proofs.

| Moment | Lean-checked result | Remaining boundary |
|---|---|---|
| H4 | traceDefect_closed: all-angle identity \(\Delta_m(H^4,\theta)=-16(3^{m-1}+1)\sin^2(\theta/2)\), for every \(m\ge1\). | No remaining gap for this stated theorem. |
| H6 | defectO6_num_growth_recurrence and defectO6_num_affine_growth: all-angle recurrence and affine form for every \(m\ge3\). The exact residual is defectO6_num_residual_constant. | The finite \(2\to3\) transition is supplied by exact Gaussian-integer polynomial arithmetic in computational/p6_level3_orientation_certificate.py. It is an exact external certificate, not a Lean-kernel theorem. Combining it with the Lean recurrence gives the all-angle formula from \(m\ge2\). |
| H8 | defectO8_succ_num_level4_constant_boundary and defectO8_num_affine_closed_form_from_level3: all-angle recurrence and affine form from \(m\ge3\). The exact residual is defectO8_num_residual_constant. | The finite \(2\to3\) transition is supplied by the exact sparse-polynomial certificate computational/p8_base_certificate.py. This certificate is not yet a Lean-kernel theorem. |
| H10 | H10TransportAll_proved establishes radius-four glued-state diagonal transport through degree 9 for both axis configurations, for all \(m\ge4\). defectO10_succ_num_level5_constant_boundary_unconditional proves the recurrence for \(m\ge4\); defectO10_num_affine_closed_form_from_level5_unconditional proves the affine form for \(m\ge5\). | defectO10_num_residual_constant is an exact finite level-five trace expression. It has not yet been expanded into an elementary trigonometric/Fourier polynomial. This is a presentation/simplification gap, not a missing transport hypothesis in the cited Lean results. |

### Source map

- H6/H8 recurrence and affine-form proofs: [FinalTilde.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/formalization/EvgenyTheorem/FinalTilde.lean).
- Tenth-moment gluing: [GlueTrace10.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/formalization/EvgenyTheorem/GlueTrace10.lean).
- Glued-row transport: [GlueRows10.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/formalization/EvgenyTheorem/GlueRows10.lean).
- Orientation/level recurrence: [FinalOrient10.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/formalization/EvgenyTheorem/FinalOrient10.lean).
- Unconditional H10 transport and affine form: [FinalClosed10.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/formalization/EvgenyTheorem/FinalClosed10.lean).
- Corner order/orientation support: [CornerLocality.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f/formalization/EvgenyTheorem/CornerLocality.lean).

The H6 finite-transition discussion is tracked in [Evgeny-Theorem PR #11](https://github.com/RFT-SIRM/Evgeny-Theorem/pull/11). An exact external certificate must not be described as a Lean-kernel theorem.

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
2. Expand the exact level-five H10 residual into an explicit trigonometric/Fourier expression, if that stronger presentation is required.
3. Extend the H6 path-class cancellation result beyond the finite first-level calculation.
4. Complete Phi-Genesis Gate A and the full exceptional-set criterion.
5. Establish the operator-eigenvalue interpretation and proposed quadratic law in Phi-Genesis.
6. Prove a precise bridge between the SU(2)-connected operators and signed-Z2-flux Laplacians, if such a bridge exists.

## 6. Evidence policy

- **LEAN-CHECKED:** the proposition compiles in the pinned Lean/Mathlib environment under its stated hypotheses.
- **EXACT EXTERNAL CERTIFICATE:** a finite algebraic identity is verified by exact reproducible code but is not checked by Lean's kernel.
- **NUMERICAL HOLDOUT:** a finite computation tests a prediction; it is not an all-level proof.
- **OPEN:** no sufficient proof/certificate is recorded.

A green CI run validates only the assertions exercised by that workflow. It does not turn an external certificate into a Lean theorem, upgrade a quadratic-form result to an operator eigenvalue theorem, or prove equivalence of distinct operator models.

## 7. Merge criterion

The synthesis PR is ready only when the documentation/reference audit, exact modular certificate, recurrence arithmetic audit, and pinned Lean build pass on the same PR head. The source projects are consumed at the exact pins above; this integration does not modify either upstream source project.