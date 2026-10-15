# Claims and evidence ledger

This ledger is deliberately conservative. Status should be updated only with evidence and a source link or reproducible artifact.

| Claim | Current status | Evidence boundary | Next verification |
|---|---|---|---|
| Fourth-moment closed trace-defect formula in the SU(2) Sierpiński-gasket model | Reported as formally proved in source project | Applies only to the exact definitions and hypotheses in the source formalization | Rebuild Lean project from clean checkout; add a Lean CI job |
| Higher-moment H⁶ recurrence | Numerically supported from transition 2→3 onward through level 5 on seven tested angles | Pinned CI calculation; maximum level-5 relative prediction residual across the grid ≈ 1.65×10⁻¹². Transition 1→2 remains exceptional | Test level 6; derive C(θ) analytically or document a counterexample |
| Higher-moment H⁸ recurrence | Numerically supported from transition 2→3 onward through level 5 on seven tested angles | Pinned CI calculation; maximum level-5 relative prediction residual across the grid ≈ 8.28×10⁻¹³. Transition 1→2 remains exceptional | Test level 6; derive C(θ) analytically or document a counterexample |
| Higher-moment H¹⁰ recurrence | Numerically supported from transition 2→3 onward through level 5 on seven tested angles | Pinned CI calculation; maximum level-5 relative prediction residual across the grid ≈ 5.70×10⁻¹³. Transition 1→2 remains exceptional | Test level 6; derive C(θ) analytically or document a counterexample |
| Gate A spectral-decimation matching is completely closed | OPEN / not established | Reported matching rates are below 100% under simple exclusions; exceptional set not fully characterized | Derive and test complete exceptional-value criterion |
| Mass-index rule is a predictive physical law | NOT ESTABLISHED | Index selection and fit do not by themselves derive a predictive rule | Preregister selection protocol and test on held-out cases |
| A structural bridge between the SU(2) and signed Z₂-flux models exists | OPEN | Different operator constructions; resemblance is not proof | State a precise mapping and prove preserved properties |

## Status definitions

- **FORMALIZED:** machine-checked in a specified proof assistant and build configuration.
- **PROVED:** complete written proof with assumptions and quantifiers.
- **NUMERICALLY REPRODUCED:** rerunnable computation with code, parameters, and outputs.
- **OBSERVED:** pattern reported but not yet independently reproduced or fully scoped.
- **CONJECTURE:** precise statement awaiting proof or refutation.
- **OPEN:** unresolved.
- **NOT ESTABLISHED:** available evidence does not justify the stronger claim.
- **NOT REPRODUCED / REFUTED:** use only with a documented protocol or explicit counterexample.

## Update protocol

For every change, include the prior wording, revised wording, reason for the change, and evidence. Do not erase negative results. Do not cite a passing test as evidence for a broader statement than the test exercises.
