# Claims and evidence ledger

This ledger is deliberately conservative. Status should be updated only with evidence and a source link or reproducible artifact.

| Claim | Current status | Evidence boundary | Next verification |
|---|---|---|---|
| Fourth-moment closed trace-defect formula in the SU(2) Sierpiński-gasket model | Reported as formally proved in source project | Applies only to the exact definitions and hypotheses in the source formalization | Rebuild Lean project from clean checkout; link theorem and CI run |
| Higher-moment H⁶ recurrence | Numerical research claim; stated starting range requires audit | Decimal arithmetic on the published m=1..4 table gives C₁→₂ ≈ 2583.4113 but C₂→₃ and C₃→₄ ≈ 2595.4113; source wording “m ≥ 2” therefore conflicts with the table | Regenerate matrix traces; hold out levels 5 and 6; clarify the exact starting level |
| Higher-moment H⁸ recurrence | Numerical research claim; no general analytic theorem established here | Published m=1..4 table has C₁→₂ ≈ 145673.7939, while C₂→₃ and C₃→₄ ≈ 153107.5232 | Independently regenerate traces and test held-out levels |
| Higher-moment H¹⁰ recurrence | Numerical research claim; no general analytic theorem established here | Published m=1..4 table has C₁→₂ ≈ 4353558.5777, while C₂→₃ and C₃→₄ ≈ 5287216.6218 | Independently regenerate traces and test held-out levels |
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
