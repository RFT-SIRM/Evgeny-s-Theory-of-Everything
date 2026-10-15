# Evgeny's Theory of Everything

**A unified research program for recursive operators, spectral invariants, and higher-moment trace laws.**

This repository organizes a long-term mathematical research program. Its title names the scope of the program; it does **not** assert that a complete theory of everything has been established.

## Latest result: level-5 holdout

A pinned GitHub Actions calculation independently recomputed H⁶, H⁸, and H¹⁰ at \(\theta=\pi/2\) through level 5 using Hermitian eigenvalues. Levels 1–4 matched the published reference values with relative discrepancies below \(1.3\times10^{-13}\). A recurrence constant fixed from levels 3 and 4 predicted level 5 with relative residuals:

| Moment | Relative residual at level 5 |
|---|---:|
| H⁶ | \(2.01\times10^{-13}\) |
| H⁸ | \(8.36\times10^{-14}\) |
| H¹⁰ | \(5.63\times10^{-14}\) |

The first transition \(1\to2\) remains an exception in the published table. The new calculation supports a later-level numerical recurrence at this angle; it is not a universal proof.

- [Full result and limitations](computational/HIGHER_MOMENT_LEVEL5_RESULTS.md)
- [Reproduction protocol](computational/HIGHER_MOMENT_HOLDOUT.md)
- [Workflow and artifact](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38758708458)
- [Earlier arithmetic audit](computational/HIGHER_MOMENT_RECURRENCE_AUDIT.md)

## Research principles

1. **Separate theorem from evidence.** Label each claim as formalized, proved on paper, numerically reproduced, observed, conjectural, or open.
2. **Preserve negative results.** Failed tests, counterexamples, exceptional cases, and non-reproduced hypotheses are part of the record.
3. **Make computation reproducible.** Record the operator, graph level, parameters, precision, algorithm, source revision, and command.
4. **Do not promote a fit into a law.** Finite numerical agreement is not a proof of a universal identity.
5. **Keep source projects distinct.** Similarities between different operator families do not establish equivalence.

## Research strands

### SU(2)-connected Sierpiński-gasket operators

Source: [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem).

The documented fourth-moment trace defect is
\[
\Delta_m(H^4,\theta)
=\operatorname{Tr}(H_C^4)-\operatorname{Tr}(H_{C'}^4)
=-16(3^{m-1}+1)\sin^2(\theta/2),\qquad m\ge 1.
\]
The source project reports this identity as formalized in Lean 4. Exact definitions and assumptions are in the source formalization. Higher moments \(H^6,H^8,H^{10}\) remain a separate numerical and analytical research program.

### Signed Z₂-flux and spectral decimation

Source: [RFT-SIRM/Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis).

This project studies signed graph Laplacians, spectral decimation with boundary/corner corrections, inertia computations, and exploratory spectral or mass-index patterns. Gate A remains open while residual mismatches and the full exceptional set remain unexplained. The proposed mass-index rule is not established as a predictive law.

## Evidence labels

- **FORMALIZED** — machine-checked in a specified proof assistant and build configuration.
- **PROVED** — complete written proof with assumptions and quantifiers.
- **NUMERICALLY REPRODUCED** — rerunnable computation with identified code, parameters, and outputs.
- **OBSERVED** — pattern not yet independently reproduced or fully scoped.
- **CONJECTURE** — precise statement awaiting proof or refutation.
- **OPEN** — unresolved.
- **NOT ESTABLISHED / NOT REPRODUCED / REFUTED** — use with an explicit evidence boundary or counterexample.

## Repository map

- `FOUNDATIONS.md` — scope, terminology, and evidence standards.
- `RESEARCH_PROGRAM.md` — workstreams and research questions.
- `CLAIMS_AND_EVIDENCE.md` — claim ledger.
- `OPEN_PROBLEMS.md` — unresolved questions and closure criteria.
- `HISTORICAL_DEVELOPMENT.md` — chronology and provenance.
- `MATHEMATICAL_FRAMEWORK.md` — definitions and cross-project boundaries.
- `references/SOURCE_REPOSITORIES.md` — source repositories and provenance.
- `computational/REPRODUCIBILITY.md` — computational reporting requirements.
- `computational/HIGHER_MOMENT_RECURRENCE_AUDIT.md` — arithmetic audit of published values.
- `computational/HIGHER_MOMENT_HOLDOUT.md` — reproducible level-5 calculation protocol.
- `computational/HIGHER_MOMENT_LEVEL5_RESULTS.md` — observed numerical results.
- `formalization/README.md` — formal proof integration policy.

## Contribution requirements

Every result should include exact definitions, assumptions, proof or algorithm, commands and versions, known exceptions, and an evidence label. A passing test establishes only what that test actually checks.
