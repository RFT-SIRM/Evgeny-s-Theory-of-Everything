# Evgeny's Theory of Everything

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

**A unified research program for recursive operators, spectral invariants, and higher-moment trace laws.**

This repository organizes a long-term mathematical research program. Its title names the scope of the program; it does **not** assert that a complete theory of everything has been established.

## License and attribution

This repository's original synthesis documentation, scripts, and configuration are licensed under the [Apache License 2.0](LICENSE). The upstream projects linked below are separate works; their files and licenses are not relicensed by this repository. See [NOTICE](NOTICE) for provenance and attribution boundaries. To cite this research snapshot, see [CITATION.cff](CITATION.cff).

## Research dissertation

The standalone research dissertation by **Evgeny Zaprudnov** consolidates the programme. The current theorem-by-theorem status, source revisions, Lean declarations, and remaining proof boundaries are maintained in [CURRENT_EVIDENCE.md](CURRENT_EVIDENCE.md).

## Current milestone

The current milestone is a reproducible synthesis of Lean-checked H4; H6/H8 recurrences with exact external finite base-transition certificates; the unconditional H10 recurrence and affine form; the signed-Z2 least-eigenvalue identification and convergence theorem for the explicitly defined internal graph matrices; and the exact limit of a separate scalar invariant. The source pins, theorem ranges, and proof boundaries are recorded in [CURRENT_EVIDENCE.md](CURRENT_EVIDENCE.md).

### Higher-moment holdouts

For $H^6,H^8,H^{10}$, the recurrence coefficient is fixed from levels 3 and 4 and then tested on held-out levels. The level-5 test covers 13 predeclared angles $\theta=k\pi/12$, $k=0,\ldots,12$. The level-6 test covers $0,\pi/2,\pi$. A separate sparse-matrix-power holdout tests levels 1–7 at five angles without using eigenspectra; Fourier coefficient candidates are reconstructed from 21 samples and checked at seven off-grid angles. Direct matrix-power traces are also compared with eigenvalue-power sums on levels 1–4.

- [13-angle holdout workflow — passed](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38761487044)
- [Level-6 holdout workflow — passed](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38761487012)
- [Documentation/reference audit workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/workflows/documentation-integrity.yml)
- [Pinned Lean formalization build workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/workflows/lean-formalization.yml)
- [Independent sparse holdout through level 7 — passed](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38767388243)
- [Fourier coefficient reconstruction and off-grid validation — passed](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38767383292)
- [13-angle machine-readable results](computational/data/higher_moment_angle_grid_13.json)
- [Level-6 machine-readable results](computational/data/higher_moment_level6_3angles.json)
- [Consolidated recurrence evidence note](computational/HIGHER_MOMENT_RECURRENCE_NOTE.md)
- [Independent sparse level-7 holdout report](computational/HIGHER_MOMENT_SPARSE_LEVEL7.md)
- [Higher-moment Fourier coefficient candidates](computational/HIGHER_MOMENT_COEFFICIENT_CANDIDATES.md)
- [Exact finite-level modular/CRT coefficient certificate](computational/HIGHER_MOMENT_MODULAR_CERTIFICATE.md)
- [H10 level-five source-reconstructed exact CRT certificate](computational/H10_EXACT_RESIDUAL_2026-11-23.md)
- [H12 finite transition-residual CRT certificate through level 8](computational/H12_FINITE_RESIDUAL_2026-11-23.md)
- [H12 degree-12 boundary-word expansion and distance classification](computational/H12_BOUNDARY_WORD_EXPANSION_2026-11-23.md)
- [H10 source-reconstruction bundle: C++ finite-trace engine and Python CRT verifier](computational/h10_level5_source_reconstruction.tar.gz)
- [Exact modular certificate workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/workflows/higher-moment-modular-certificate.yml)
- [Independent sparse level-7 workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/workflows/independent-sparse-level7.yml)
- [Fourier coefficient candidate workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/workflows/higher-moment-coefficient-candidates.yml)

**Updated proof status.** Lean proves the all-angle H6/H8 recurrences from level 3, with exact external certificates for their finite 2-to-3 transitions. For H10, Lean proves radius-four diagonal transport through degree nine, the unconditional recurrence from level 4, and affine form from level 5. The finite level-five correction is now reconstructed directly from the pinned graph/operator definitions: a C++ source mirror computes the level-five and level-six trace polynomials modulo three primes, and signed CRT recovers the unique integer coefficients under an explicit path-count bound. The all-angle relation of the recurrence constant to D6−3D5 is Lean-checked; the coefficient expansion remains an exact external certificate, not a Lean-kernel theorem. See CURRENT_EVIDENCE.md and the H10 report.

## Research strands

### SU(2)-connected Sierpiński-gasket operators

Source: [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem).

The source project formally proves the fourth-moment trace-defect identity $\Delta_m(H^4,\theta)=\mathrm{Tr}(H_C^4)-\mathrm{Tr}(H_{C'}^4)=-16(3^{m-1}+1)\sin^2(\theta/2)$ for $m\ge1$
for its specified operator definitions and assumptions, with a Lean 4 formalization. The synthesis CI builds a pinned source revision. Higher moments $H^6,H^8,H^{10}$ are a separate research program and are not covered by that theorem.

### Signed Z₂-flux and spectral decimation

Source: [RFT-SIRM/Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis).

This project studies signed graph Laplacians, spectral decimation with boundary/corner corrections, inertia computations, and exploratory spectral or mass-index patterns. Its merged Lean work proves the Schur corner-response bridge, strict pivot positivity in the bootstrap window, uniqueness of the selected A1 root, identification of that root with the least eigenvalue of the internally defined graph matrix Q_(6+n), convergence of the least-eigenvalue sequence, and transfer to the gauge-equivalent signed matrix. The limit lies in an exact rational interval of width 2·10^-36. These statements apply to the specified internal graph matrices; they do not identify them with the external theta=2π local-face operator. Still open are an effective uniform tail estimate, an explicit limiting-constant characterization, proof or refutation of the quadratic root-shift law, the complete Gate A exceptional-set criterion, and any extension beyond the stated level range. The mass-index rule is not established as predictive.

No equivalence between the SU(2)-connected operators and signed Z₂-flux Laplacians is assumed. A bridge between them remains an open research question.

### Exact scalar-invariant limit theorem

A related, separately sourced result is the exact limit and finite-level remainder of a defined scalar invariant. Its theorem statement, algebraic derivation, Lean source, provenance, and evidence boundary are recorded in [the exact invariant limit theorem dossier](theorems/exact_invariant_limit.md). The machine-checked proof is maintained in [RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis), where [PR #3](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/pull/3) was merged and the post-merge Lean build passed. This theorem concerns the stated scalar formula; it does not establish a physical cosmological law or a bridge between the other operator models in this archive.

## Evidence labels

- **FORMALIZED** — machine-checked in a specified proof assistant and build configuration.
- **PROVED** — complete written proof with assumptions and quantifiers.
- **NUMERICALLY REPRODUCED** — rerunnable computation with identified code, parameters, and outputs.
- **OBSERVED** — pattern not yet independently reproduced or fully scoped.
- **CONJECTURE** — precise statement awaiting proof or refutation.
- **OPEN** — unresolved.
- **NOT ESTABLISHED / NOT REPRODUCED / REFUTED** — use with an explicit evidence boundary or counterexample.

## Repository map

- CURRENT_EVIDENCE.md — authoritative current proof/evidence matrix and pinned source revisions.
- FOUNDATIONS.md — scope, terminology, and evidence standards.
- RESEARCH_PROGRAM.md — workstreams and research questions.
- CLAIMS_AND_EVIDENCE.md — claim ledger.
- OPEN_PROBLEMS.md — unresolved questions and closure criteria.
- HISTORICAL_DEVELOPMENT.md — commit-backed chronology and provenance.
- MATHEMATICAL_FRAMEWORK.md — definitions and cross-project boundaries.
- references/SOURCE_REPOSITORIES.md — source repositories and provenance.
- computational/REPRODUCIBILITY.md — computational reporting requirements.
- computational/HIGHER_MOMENT_RECURRENCE_AUDIT.md — arithmetic audit of published values.
- computational/HIGHER_MOMENT_RECURRENCE_NOTE.md — numerical evidence and proof-closure criteria.
- computational/HIGHER_MOMENT_SPARSE_LEVEL7.md — sparse-trace holdout through level 7, without eigenspectrum evaluation.
- computational/HIGHER_MOMENT_COEFFICIENT_CANDIDATES.md — numerically reconstructed Fourier candidates for the higher-moment coefficients and exceptional first transition.
- MILESTONE_AND_RELEASE_CHECKLIST.md — milestone and mathematical closure criteria.
- FINAL_STATUS.md — current-stage closure report.
- LICENSE — Apache License 2.0 for this repository's original contributions.
- NOTICE — upstream provenance and third-party licensing boundary.
- CITATION.cff — citation metadata for the research repository.
- CHANGELOG.md — curated milestone and documentation changes.
- SECURITY.md — responsible reporting guidance.
- computational/data/ — committed machine-readable calculation outputs.

## Research principles

1. Separate theorem from evidence.
2. Preserve negative results and exceptional cases.
3. Record source revisions, parameters, algorithms, and outputs.
4. Do not promote a fit or finite numerical agreement into a universal law.
5. Keep distinct operator constructions separate until a precise bridge is proved.
6. Treat passing CI as evidence only for the assertions the workflow actually runs.

Every result should state its definitions, assumptions, proof or algorithm, commands and versions, known exceptions, and evidence label.

## H12 boundary contraction update — 23 November 2026

The degree-12 gluing expansion now has an exact combinatorial boundary-word contraction: all 1,024 odd-pairing strata vanish and all 1,024 even-pairing strata reduce to ordered products of diagonal 2×2 spin blocks. A cyclic matching argument removes the apparent 48 level-three long-gap cases from the trace; no off-diagonal corner block is needed in the final contraction. The radius-five locality argument and finite audits through levels 3–10 are documented in [the H12 boundary-contraction report](computational/H12_BOUNDARY_DIAGONAL_CONTRACTION_2026-11-23.md). This is not yet a Lean-kernel H12 recurrence: copy-transfer synthesis and the Lean formalization remain open.
