# Source repositories and provenance

## 1. Evgeny-Theorem

URL: https://github.com/RFT-SIRM/Evgeny-Theorem

Research area: SU(2)-connected operators on Sierpiński-gasket approximation graphs, fourth-moment trace-defect formula, Lean 4 formalization, and numerical exploration of higher moments.

Boundary: the source project documents the fourth-moment result as formalized. H⁶/H⁸/H¹⁰ claims must retain their numerical/open status unless a separate exact proof is available.

## 2. Phi-Genesis

URL: https://github.com/RFT-SIRM/Phi-Genesis

Research area: signed Z₂-flux Laplacians, spectral decimation with boundary/corner corrections, numerical inertia and spectral convergence, and exploratory mass-index hypotheses.

Boundary: incomplete Gate A closure and exploratory fitted patterns must not be represented as completed theorems.

## 3. RFT-Cosmology-Genesis

URL: https://github.com/RFT-SIRM/RFT-Cosmology-Genesis

Research area: a reduced phenomenological cosmology workflow together with an exact scalar-invariant remainder identity and a Lean formalization of its limit.

Formal result: PR #3, “formalize convergence of the invariant to its exact limit,” was merged on 16 October 2026. The merged source commit is [2a7782a8a56181313808019202089f167cf09cc2](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/commit/2a7782a56181313808019202089f167cf09cc2). The named Lean theorem is **rftInvariant_tendsto**; the exact remainder and decomposition are also machine-checked.

Boundary: this result proves a limit for the specified scalar formula only. It does not establish an observational fit, physical cosmological interaction, or a bridge to either of the two operator families above. The synthesis archive records the theorem and provenance; the proof remains in its source repository.

## Provenance requirements

For every imported result, record:
- source path and URL;
- source commit or release tag;
- exact statement and definitions;
- whether the result was copied, independently reproduced, or formally rechecked;
- any differences between the source and this synthesis.

Do not claim that a result was independently reproduced merely because it appears in a source repository.
