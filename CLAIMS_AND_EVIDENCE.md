# Claims and evidence ledger

This ledger is deliberately conservative. Status should be updated only with evidence and a source link or reproducible artifact.

| Claim | Current status | Evidence boundary | Next verification |
|---|---|---|---|
| Fourth-moment closed trace-defect formula in the SU(2) Sierpiński-gasket model | Reported as formally proved in source project | Applies only to the exact definitions and hypotheses in the source formalization; the synthesis CI builds the pinned source revision | Preserve source theorem statement, assumptions, toolchain, and successful Lean build |
| Exact limit and finite-level remainder for the defined scalar invariant | FORMALIZED in the separate RFT-Cosmology-Genesis project | Lean theorem rftInvariant_tendsto plus exact remainder/decomposition lemmas; post-merge Lean CI passed. No physical or observational claim follows | Keep the theorem dossier, source commit, toolchain, and CI links synchronized |
| Higher-moment H⁶ recurrence | Numerically supported conjecture from transition 2→3 onward; finite-level Fourier coefficients certified | Thirteen angles through level 5, \(0,\pi/2,\pi\) through level 6, and independent sparse traces through level 7 at five angles. Exact modular/CRT verification certifies \(R_2^{(6)}\) and \(R_4^{(6)}\) at the finite transitions 1→2 and 3→4. It does not prove \(R_m=R_4\) for all \(m\ge3\). | Prove level independence from the recursive operator structure and explain the base exception |
| Higher-moment H⁸ recurrence | Numerically supported conjecture from transition 2→3 onward; finite-level Fourier coefficients certified | Thirteen angles through level 5, \(0,\pi/2,\pi\) through level 6, and independent sparse traces through level 7 at five angles. Exact modular/CRT verification certifies \(R_2^{(8)}\) and \(R_4^{(8)}\) at the finite transitions 1→2 and 3→4. It does not prove \(R_m=R_4\) for all \(m\ge3\). | Prove level independence from the recursive operator structure and explain the base exception |
| Higher-moment H¹⁰ recurrence | Numerically supported conjecture from transition 2→3 onward; finite-level Fourier coefficients certified | Thirteen angles through level 5, \(0,\pi/2,\pi\) through level 6, and independent sparse traces through level 7 at five angles. Exact modular/CRT verification certifies \(R_2^{(10)}\) and \(R_4^{(10)}\) at the finite transitions 1→2 and 3→4. It does not prove \(R_m=R_4\) for all \(m\ge3\). | Prove level independence from the recursive operator structure and explain the base exception |
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
