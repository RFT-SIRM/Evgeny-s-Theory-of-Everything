# Claims and evidence ledger

This ledger is deliberately conservative. Status should be updated only with evidence and a source link or reproducible artifact.

| Claim | Current status | Evidence boundary | Next verification |
|---|---|---|---|
| Fourth-moment closed trace-defect formula in the SU(2) Sierpiński-gasket model | Reported as formally proved in source project | Applies only to the exact definitions and hypotheses in the source formalization | Lean CI successfully built the pinned source revision; repeat after source or toolchain changes |
| Higher-moment H⁶ recurrence | Numerically supported from transition 2→3 onward through level 6 | Pinned CI calculations: thirteen angles through level 5, and 0, π/2, π through level 6; max level-6 relative prediction residual ≈ 9.28×10⁻¹⁴; direct trace/eigenvalue cross-check at levels 1–4 agrees within 4.37×10⁻¹² for H⁶, 1.60×10⁻¹² for H⁸, and 1.42×10⁻¹² for H¹⁰; 13-angle level-5 max residual ≈ 1.47×10⁻¹². Transition 1→2 remains exceptional | Derive C(θ) analytically; test additional levels only if needed for proof discovery |
| Higher-moment H⁸ recurrence | Numerically supported from transition 2→3 onward through level 6 | Pinned CI calculations: thirteen angles through level 5, and 0, π/2, π through level 6; max level-6 relative prediction residual ≈ 6.74×10⁻¹⁴; 13-angle level-5 max residual ≈ 1.80×10⁻¹². Transition 1→2 remains exceptional | Derive C(θ) analytically; test additional levels only if needed for proof discovery |
| Higher-moment H¹⁰ recurrence | Numerically supported from transition 2→3 onward through level 6 | Pinned CI calculations: seven angles through level 5, and 0, π/2, π through level 6; max level-6 relative prediction residual ≈ 3.56×10⁻¹⁴; 13-angle level-5 max residual ≈ 8.82×10⁻¹³. Transition 1→2 remains exceptional | Derive C(θ) analytically; test additional levels only if needed for proof discovery |
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
