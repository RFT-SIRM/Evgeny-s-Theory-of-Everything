# Claims and evidence ledger

This ledger is deliberately conservative. Status should be updated only with evidence and a source link or reproducible artifact.

| Claim | Current status | Evidence boundary | Next verification |
|---|---|---|---|
| Fourth-moment closed trace-defect formula in the SU(2) Sierpiński-gasket model | Reported as formally proved in source project | Applies only to the exact definitions and hypotheses in the source formalization | Rebuild Lean project from clean checkout; add a Lean CI job |
| Higher-moment H⁶ recurrence | Numerically supported from transition 2→3 onward at θ = π/2 through level 5 | Levels 1–4 match published references; a level-5 holdout predicted from levels 3–4 has relative residual ≈ 2.01×10⁻¹³. The first transition 1→2 has a different implied constant | Test a declared angle grid and level 6; then derive or refute analytically |
| Higher-moment H⁸ recurrence | Numerically supported from transition 2→3 onward at θ = π/2 through level 5 | Levels 1–4 match published references; level-5 holdout relative residual ≈ 8.36×10⁻¹⁴. The first transition 1→2 has a different implied constant | Test a declared angle grid and level 6; then derive or refute analytically |
| Higher-moment H¹⁰ recurrence | Numerically supported from transition 2→3 onward at θ = π/2 through level 5 | Levels 1–4 match published references; level-5 holdout relative residual ≈ 5.63×10⁻¹⁴. The first transition 1→2 has a different implied constant | Test a declared angle grid and level 6; then derive or refute analytically |
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
