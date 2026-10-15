# Claims and evidence ledger

This ledger is deliberately conservative. Status should be updated only with evidence and a source link or reproducible artifact.

| Claim | Current status | Evidence boundary | Next verification |
|---|---|---|---|
| Fourth-moment closed trace-defect formula in the SU(2) Sierpiński-gasket model | Reported as formally proved in source project | Applies only to the exact definitions and hypotheses in the source formalization; the synthesis CI builds the pinned source revision | Preserve source theorem statement, assumptions, toolchain, and successful Lean build |
| Higher-moment H⁶ recurrence | Numerically supported conjecture from transition 2→3 onward through level 6 | Thirteen angles through level 5 and \(0,\pi/2,\pi\) through level 6; maximum level-5 residual \(\approx1.47\times10^{-12}\), maximum level-6 residual \(\approx9.28\times10^{-14}\); direct-trace/eigenvalue cross-check \(\approx4.37\times10^{-12}\). Transition 1→2 remains exceptional | Derive \(C_6(\theta)\), prove the starting index, and explain the base exception |
| Higher-moment H⁸ recurrence | Numerically supported conjecture from transition 2→3 onward through level 6 | Thirteen angles through level 5 and \(0,\pi/2,\pi\) through level 6; maximum level-5 residual \(\approx1.80\times10^{-12}\), maximum level-6 residual \(\approx6.74\times10^{-14}\); direct-trace/eigenvalue cross-check \(\approx1.60\times10^{-12}\). Transition 1→2 remains exceptional | Derive \(C_8(\theta)\), prove the starting index, and explain the base exception |
| Higher-moment H¹⁰ recurrence | Numerically supported conjecture from transition 2→3 onward through level 6 | Thirteen angles through level 5 and \(0,\pi/2,\pi\) through level 6; maximum level-5 residual \(\approx8.82\times10^{-13}\), maximum level-6 residual \(\approx3.56\times10^{-14}\); direct-trace/eigenvalue cross-check \(\approx1.42\times10^{-12}\). Transition 1→2 remains exceptional | Derive \(C_{10}(\theta)\), prove the starting index, and explain the base exception |
| Gate A spectral-decimation matching is completely closed | OPEN / not established | Reported matching rates remain below 100% under simple exclusions; the full exceptional set is not characterized | Derive and independently test a complete exceptional-value criterion |
| Mass-index rule is a predictive physical law | NOT ESTABLISHED | Index selection and a numerical fit do not derive a predictive selection rule | Preregister a selection protocol and test held-out cases |
| A structural bridge between the SU(2) and signed Z₂-flux models exists | OPEN | Different operator constructions; resemblance is not proof | State a precise mapping and prove which properties it preserves |

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