# Claims and evidence ledger

The canonical, commit-pinned detail is in [CURRENT_EVIDENCE.md](CURRENT_EVIDENCE.md). This ledger is the at-a-glance status; it must not be read more broadly than the stated objects and hypotheses.

| Claim | Current status | Evidence boundary | Remaining work |
|---|---|---|---|
| SU(2) fourth-moment trace-defect formula | **LEAN-CHECKED** for every m ≥ 1 and theta in R | Source declaration traceDefect_closed in Evgeny-Theorem; exact source revision and CI provenance are pinned in CURRENT_EVIDENCE.md. | No remaining gap for this stated theorem. |
| SU(2) H6 recurrence | **LEAN-CHECKED** for every m ≥ 3, with affine form from level 3 | defectO6_num_growth_recurrence and defectO6_num_affine_growth; exact 2→3 bridge is a Gaussian-integer polynomial certificate, not a Lean-kernel theorem. | Formalize the finite bridge in Lean if feasible. |
| SU(2) H8 recurrence | **LEAN-CHECKED** for every m ≥ 3, with affine form from level 3 | defectO8_succ_num_level4_constant_boundary and defectO8_num_affine_closed_form_from_level3; exact 2→3 bridge is a sparse-polynomial certificate, not a Lean-kernel theorem. | Formalize the finite bridge in Lean if feasible. |
| SU(2) H10 recurrence | **LEAN-CHECKED** unconditionally for every m ≥ 4; affine form for every m ≥ 5 | H10TransportAll_proved establishes radius-four diagonal transport through degree 9; defectO10_num_residual_constant is an exact level-five trace expression. | Expand the level-five constant into an explicit trigonometric/Fourier polynomial if desired. |
| Phi-Genesis Schur bootstrap | **FORMALIZED** within the quadratic-form/Rayleigh-minimum scope | Merged Schur and inertia PRs; A1-root uniqueness and selected-root convergence. This is not yet an operator eigenvalue theorem. | Prove eigenvalue identification, explicit closed form, quadratic law, and handle levels N < 6. |
| Phi-Genesis Gate A is completely closed | **OPEN** | Full exceptional-value characterization is not established. | Derive and independently verify a complete criterion. |
| Mass-index fit is a predictive physical law | **NOT ESTABLISHED** | A numerical fit does not derive a predictive selection rule. | Preregister and test a derived selection rule on held-out cases. |
| Exact limit of the separately defined scalar invariant | **LEAN-CHECKED** in RFT-Cosmology-Genesis | rftInvariant_tendsto, exact decomposition and remainder; separate source project and CI. | No physical-cosmology claim follows. |
| A theorem identifies the SU(2) and signed-Z2 operator families | **OPEN / NOT ESTABLISHED** | The models have distinct definitions; no proved map preserving the required quantities is recorded. | State and prove a precise inter-model map, if one exists. |

## Status vocabulary

- **LEAN-CHECKED:** the exact proposition compiles in the pinned Lean/Mathlib environment under its stated hypotheses.
- **EXACT EXTERNAL CERTIFICATE:** finite algebraic identity verified by exact code, but not checked by Lean's kernel.
- **NUMERICALLY REPRODUCED:** rerunnable finite computation with parameters and outputs.
- **OPEN:** no sufficient proof/certificate is recorded.
- **NOT ESTABLISHED:** current evidence does not justify the stronger claim.

A successful test or CI run validates only the assertion exercised by that workflow. A finite exact certificate is stronger than floating-point agreement but is not automatically a Lean theorem.