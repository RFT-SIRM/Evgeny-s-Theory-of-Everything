# Formalization integration

The primary SU(2)-operator formalization is maintained in [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem). The synthesis workflow checks out a pinned source revision and runs the actual upstream Lean library build; it does not copy or re-formalize the source modules here.

## Pinned source and build

- Source commit: [4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f).
- Toolchain: leanprover/lean4:v4.33.1.
- Mathlib revision: v4.33.1.
- Build target: lake build EvgenyTheorem.
- Workflow: [synthesis pinned Lean build](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/workflows/lean-formalization.yml).

The source state was built successfully by [Lean CI run 42481191661](https://github.com/RFT-SIRM/Evgeny-Theorem/actions/runs/42481191661) at commit a7b732a04d1b4e619cd050b2b643daf491e86fa2. The current pin 4ccfae is 14 commits ahead; its compare contains only documentation/HTML changes and no Lean source changes. The synthesis PR must still pass its own pinned build on the exact PR head before merge.

## Formal results represented

- H4: traceDefect_closed, all m ≥ 1, all real angles.
- H6: defectO6_num_growth_recurrence and defectO6_num_affine_growth, m ≥ 3; finite 2→3 polynomial certificate is external to Lean.
- H8: defectO8_succ_num_level4_constant_boundary and defectO8_num_affine_closed_form_from_level3, m ≥ 3; finite 2→3 sparse-polynomial certificate is external to Lean.
- H10: H10TransportAll_proved; defectO10_succ_num_level5_constant_boundary_unconditional, m ≥ 4; defectO10_num_affine_closed_form_from_level5_unconditional, m ≥ 5. The exact level-five residual is still presented as a trace expression.

The exact source files, hypotheses, and finite-certificate boundaries are listed in [CURRENT_EVIDENCE.md](../CURRENT_EVIDENCE.md).

## Separate source projects

The Schur/Rayleigh formalization is maintained in [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis); it is not built by this workflow and concerns a distinct signed-Z2-flux operator. The exact scalar-invariant limit theorem is maintained in [RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis), with its separate dossier at [theorems/exact_invariant_limit.md](../theorems/exact_invariant_limit.md).

Do not add placeholder Lean files, copy upstream code without provenance, or mark an external exact certificate as a Lean-kernel proof.