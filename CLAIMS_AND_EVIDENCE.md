# Claims and evidence ledger

This ledger is deliberately conservative. Status should be updated only with evidence and a source link or reproducible artifact.

| Claim | Current status | Evidence boundary | Next verification |
|---|---|---|---|
| Fourth-moment closed trace-defect formula in the SU(2) Sierpiński-gasket model | Reported as formally proved in source project | Applies only to the exact definitions and hypotheses in the source formalization | Rebuild Lean project from clean checkout; link theorem and CI run |
| Higher-moment H⁶ recurrence | Numerical research claim; general analytic theorem not established here | Published tables show level-dependent behaviour at the base transition and apparent stabilization at later transitions | Regenerate values; test a fixed constant on independent higher levels |
| Higher-moment H⁸ recurrence | Numerical research claim; general analytic theorem not established here | Finite numerical table only | Independent reproduction and proof or counterexample |
| Higher-moment H¹⁰ recurrence | Numerical research claim; general analytic theorem not established here | Finite numerical table only | Independent reproduction and proof or counterexample |
| Gate A spectral-decimation matching is completely closed | OPEN / not established | Reported matching rates are below 100% under simple exclusions; exceptional set not fully characterized | Derive and test complete exceptional-value criterion |
| Mass-index rule is a predictive physical law | NOT ESTABLISHED | Index selection and fit do not by themselves derive a predictive rule | Preregister selection protocol and test on held-out cases |
| A structural bridge between the SU(2) and signed Z₂-flux models exists | OPEN | Different operator constructions; resemblance is not proof | State a precise mapping and prove preserved properties |

## Status definitions

- **FORMALIZED:** machine-checked in a pinned, reproducible environment.
- **PROVED:** complete written proof with assumptions and quantifiers.
- **NUMERICALLY REPRODUCED:** rerunnable computation with code, parameters, and outputs.
- **OBSERVED:** pattern reported but not yet independently reproduced or fully scoped.
- **CONJECTURE:** precise falsifiable statement awaiting proof or refutation.
- **OPEN:** unresolved.
- **NOT ESTABLISHED:** available evidence does not justify the stronger claim.
- **NOT REPRODUCED / REFUTED:** use only with a documented protocol or explicit counterexample.

## Update protocol

For every change, include the prior wording, revised wording, reason for the change, and evidence. Do not erase negative results. Do not cite a passing test as evidence for a broader statement than the test exercises.
