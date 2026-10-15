# Evgeny's Theory of Everything

**A unified research program for recursive operators, spectral invariants, and higher-moment trace laws.**

This repository organizes a long-term mathematical research program. Its title names the scope of the program; it does **not** assert that a complete theory of everything has been established.

## Latest result: higher-moment angle-grid holdout

A pinned GitHub Actions calculation recomputed H⁶, H⁸, and H¹⁰ through level 5 at seven angles \(0,\pi/6,\pi/4,\pi/3,\pi/2,2\pi/3,\pi\). The recurrence constant was fixed using levels 3 and 4; level 5 was held out.

Across the grid, maximum relative prediction residuals were approximately \(1.65\times10^{-12}\) for H⁶, \(8.28\times10^{-13}\) for H⁸, and \(5.70\times10^{-13}\) for H¹⁰. The first transition \(1\to2\) remains exceptional at every nonzero angle tested. This supports a candidate numerical recurrence from transition \(2\to3\) onward; it is not a universal proof.

- [Angle-grid results and interpretation](computational/HIGHER_MOMENT_ANGLE_GRID_RESULTS.md)
- [Angle-grid workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38759029736)
- [Level-6 results](computational/HIGHER_MOMENT_LEVEL6_RESULTS.md)
- [Level-6 workflow](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38759404528)
- [Level-5 protocol](computational/HIGHER_MOMENT_HOLDOUT.md)
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
- `computational/HIGHER_MOMENT_HOLDOUT.md` — single-angle level-5 protocol.
- `computational/HIGHER_MOMENT_LEVEL5_RESULTS.md` — level-5 result at \(\theta=\pi/2\).
- `computational/HIGHER_MOMENT_ANGLE_GRID.md` — angle-grid protocol.
- `computational/HIGHER_MOMENT_ANGLE_GRID_RESULTS.md` — angle-grid results.
- `computational/HIGHER_MOMENT_LEVEL6.md` — level-6 protocol.
- `computational/HIGHER_MOMENT_LEVEL6_RESULTS.md` — level-6 results.

## Contribution requirements

Every result should include exact definitions, assumptions, proof or algorithm, commands and versions, known exceptions, and an evidence label. A passing test establishes only what that test actually checks.
