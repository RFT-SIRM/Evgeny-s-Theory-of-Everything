# Evgeny's Theory of Everything

**A unified research program for recursive operators, spectral invariants, and higher-moment trace laws.**

This repository organizes a long-term mathematical research program around recursive graph operators, spectral invariants, trace-moment identities, and computationally testable conjectures. The title names the scope of the program; it does **not** assert that a complete theory of everything has been established.

## Research principles

1. **Separate theorem from evidence.** Every substantial claim must be labelled as formally proved, proved on paper, numerically observed, conjectural, or unresolved.
2. **Preserve negative results.** Failed tests, counterexamples, exceptional cases, and non-reproduced hypotheses are part of the research record.
3. **Make computation reproducible.** Record the exact operator, graph level, parameters, precision, algorithm, code revision, and test command.
4. **Do not promote a fit into a law.** Numerical agreement on finitely many levels is evidence for a conjecture, not a proof of a universal identity.
5. **Keep source projects distinct.** Results from different graph models or operator families may be compared, but a connection is not a theorem until its hypotheses and proof are supplied.

## Starting research strands

### 1. SU(2)-connected Sierpiński-gasket operators

The source project [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) studies graph operators with SU(2) edge connections and compares a noncommuting connection pattern with a commuting control.

Its documented central result is a closed fourth-moment trace defect:
\[
\Delta_m(H^4,\theta)
=\operatorname{Tr}(H_C^4)-\operatorname{Tr}(H_{C'}^4)
=-16(3^{m-1}+1)\sin^2(\theta/2),\qquad m\ge 1.
\]
The source repository reports a Lean 4 formalization of this fourth-moment identity. The exact theorem statement, definitions, assumptions, and reproducible build command must be taken from the source formalization; this overview is not a substitute for them.

Higher moments \(H^6,H^8,H^{10}\) remain a separate research strand. An arithmetic audit of the published reference table found a first-transition discrepancy in the proposed constant-coefficient recurrence; see [Audit 001](computational/HIGHER_MOMENT_RECURRENCE_AUDIT.md). This audit uses the published values and does not yet independently rerun the operator matrices.

### 2. Signed Z₂-flux and spectral-decimation research

The source project [RFT-SIRM/Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) studies signed graph Laplacians, spectral decimation with boundary/corner-defect corrections, inertia computations, and exploratory spectral or mass-index patterns.

Its claims have a different operator setup from the SU(2)-connected model above. A structural bridge between the projects is an open research question, not an assumed equivalence. The Gate A decimation audit and the proposed mass-index selection rule must remain explicitly unresolved unless new independent evidence closes them.

## Evidence labels

Use these labels consistently in documentation, issues, and commit messages:

- **FORMALIZED** — machine-checked in a specified proof assistant and build configuration.
- **PROVED** — a complete mathematical proof is documented, but not necessarily machine-checked.
- **NUMERICALLY REPRODUCED** — computation can be rerun from identified code and parameters; this is not a universal proof.
- **OBSERVED** — a reported pattern whose independent reproducibility or scope is not yet fully established.
- **CONJECTURE** — a precise statement proposed for proof or refutation.
- **OPEN** — not resolved.
- **REFUTED / NOT REPRODUCED** — contradicted by a counterexample or not recovered under a stated reproduction protocol. Include the protocol and scope.

## Repository map

- `FOUNDATIONS.md` — scope, terminology, and standards of evidence.
- `RESEARCH_PROGRAM.md` — workstreams and near-term research questions.
- `CLAIMS_AND_EVIDENCE.md` — claim ledger with source links and status.
- `OPEN_PROBLEMS.md` — precise unresolved questions and closure criteria.
- `HISTORICAL_DEVELOPMENT.md` — verified chronology and provenance.
- `MATHEMATICAL_FRAMEWORK.md` — definitions and the proposed cross-project framework.
- `references/SOURCE_REPOSITORIES.md` — source repositories and provenance boundaries.
- `computational/REPRODUCIBILITY.md` — computational reporting requirements.
- `computational/HIGHER_MOMENT_RECURRENCE_AUDIT.md` — arithmetic audit of the published H⁶/H⁸/H¹⁰ table.
- `formalization/README.md` — formal proof integration policy.

## Current status

This repository begins as a synthesis and verification layer over existing projects. It does not silently replace their results, change their claims, or assert that every source artifact has already been independently reproduced. The initial task is to make the research inventory auditable, then reproduce and extend results one claim at a time.

## How to contribute

Before adding a result, include:
1. the exact statement and definitions;
2. assumptions and domain of validity;
3. proof or algorithm;
4. tests and commands, including versions and parameters;
5. known exceptions, counterexamples, and limitations;
6. a status label from the list above.

A passing test establishes only what that test actually checks. A test that defines a constant from the same values used in an identity is not an independent verification of that identity.
