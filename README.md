# Evgeny's Theory of Everything

**A unified research program for recursive operators, spectral invariants, and higher-moment trace laws.**

This repository organizes a long-term mathematical research program. Its title names the scope of the program; it does **not** assert that a complete theory of everything has been established.

## Current milestone

The current milestone is a reproducible research package: a pinned Lean build for the source project's fourth-moment result, expanded numerical holdouts for the sixth, eighth, and tenth trace moments, versioned machine-readable outputs, and explicit evidence boundaries.

### Higher-moment holdouts

For \(H^6,H^8,H^{10}\), the recurrence coefficient is fixed from levels 3 and 4 and then tested on held-out levels. The level-5 test covers 13 predeclared angles \(\theta=k\pi/12\), \(k=0,\ldots,12\). The level-6 test covers \(0,\pi/2,\pi\). A separate sparse-matrix-power holdout tests levels 1–7 at five angles without using eigenspectra; Fourier coefficient candidates are reconstructed from 21 samples and checked at seven off-grid angles. Direct matrix-power traces are also compared with eigenvalue-power sums on levels 1–4.

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
- [Exact modular certificate workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/workflows/higher-moment-modular-certificate.yml)
- [Independent sparse level-7 workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/workflows/independent-sparse-level7.yml)
- [Fourier coefficient candidate workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/workflows/higher-moment-coefficient-candidates.yml)

The recurrence candidate appears stable from transition \(2\to3\) onward on the tested finite set. Exact modular/CRT checks certify the Fourier coefficients of the finite-level residuals \(R_2\) and \(R_4\), while sparse-trace holdouts test levels 5–7 at five angles. This is not yet a proof that the recurrence holds at every level and angle. The exact coefficient functions \(C_6(\theta),C_8(\theta),C_{10}(\theta)\) and a proof for all levels and angles remain open.

## Research strands

### SU(2)-connected Sierpiński-gasket operators

Source: [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem).

The source project reports the fourth-moment trace-defect identity
\[
\Delta_m(H^4,\theta)
=\operatorname{Tr}(H_C^4)-\operatorname{Tr}(H_{C'}^4)
=-16(3^{m-1}+1)\sin^2(\theta/2),\qquad m\ge1,
\]
for its specified operator definitions and assumptions, with a Lean 4 formalization. The synthesis CI builds a pinned source revision. Higher moments \(H^6,H^8,H^{10}\) are a separate research program and are not covered by that theorem.

### Signed Z₂-flux and spectral decimation

Source: [RFT-SIRM/Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis).

This project studies signed graph Laplacians, spectral decimation with boundary/corner corrections, inertia computations, and exploratory spectral or mass-index patterns. Gate A remains open while residual mismatches and the full exceptional set remain unexplained. The proposed mass-index rule is not established as a predictive law.

No equivalence between the SU(2)-connected operators and signed Z₂-flux Laplacians is assumed. A bridge between them remains an open research question.

## Evidence labels

- **FORMALIZED** — machine-checked in a specified proof assistant and build configuration.
- **PROVED** — complete written proof with assumptions and quantifiers.
- **NUMERICALLY REPRODUCED** — rerunnable computation with identified code, parameters, and outputs.
- **OBSERVED** — pattern not yet independently reproduced or fully scoped.
- **CONJECTURE** — precise statement awaiting proof or refutation.
- **OPEN** — unresolved.
- **NOT ESTABLISHED / NOT REPRODUCED / REFUTED** — use with an explicit evidence boundary or counterexample.

## Repository map

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
- computational/data/ — committed machine-readable calculation outputs.

## Research principles

1. Separate theorem from evidence.
2. Preserve negative results and exceptional cases.
3. Record source revisions, parameters, algorithms, and outputs.
4. Do not promote a fit or finite numerical agreement into a universal law.
5. Keep distinct operator constructions separate until a precise bridge is proved.
6. Treat passing CI as evidence only for the assertions the workflow actually runs.

Every result should state its definitions, assumptions, proof or algorithm, commands and versions, known exceptions, and evidence label.