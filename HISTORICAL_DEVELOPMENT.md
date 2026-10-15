# Historical development and provenance

## Scope and verification policy

This chronology is reconstructed from the GitHub commit history of this repository and the pinned source references used by its workflows. The first 31 commits on main were created on 2026-10-15 UTC. Their commit messages are preserved in Git history; the milestones below group those commits by the work they introduced. A commit message is evidence of a recorded change, not by itself evidence that a mathematical claim is true.

Source projects:
- [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) — SU(2)-connected Sierpiński-gasket operators and the reported formalized fourth-moment result.
- [RFT-SIRM/Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) — signed Z₂-flux spectral decimation, inertia, boundary/corner corrections, and exploratory numerical hypotheses.

The higher-moment workflows pin the operator source to [RFT-SIRM/Evgeny-Theorem commit 9ed32ae27b4493945624c2911d2815059613a9f5](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/9ed32ae27b4493945624c2911d2815059613a9f5). The Lean workflow builds that pinned source project; it does not prove the higher-moment recurrence.

## Verified milestones in the synthesis repository

| Milestone | Commit(s) | Recorded work and evidence boundary |
|---|---|---|
| Repository initialization and standards | bd0dae6b3551, 21cd76d3c40f, aac41cba1550, d4d4305ba583, 1ae9e5d486fd, 4bf3b2d1a5a4, 5ebd9fc16ac6, 00be596b9b0c, faa09c68ab22, fff86a77dec0 | Initial README, foundations, research plan, claim ledger, open problems, historical record, mathematical framework, source references, reproducibility policy, and formalization notes. |
| Documentation integrity and provenance | 40f543bfadee, 5d699898807e, 5573e20556ae, 8719e804d6c9 | Added automated document checks, contribution/evidence standards, and baseline repository hygiene. These checks validate structure and provenance labels, not theorem truth. |
| First higher-moment arithmetic audit | 0ae3307a31f1 | Audited the recurrence's base transition and added arithmetic CI. The first transition was retained as an exception rather than hidden by a fitted constant. |
| Reproducible level-5 holdout | 159a95c54b09, 5cb3f55aff94 | Added a pinned-source level-5 calculation and recorded its outputs and evidence status. |
| Fixed angle-grid holdouts | b0f73045deff, 5ff4dfc1c5f3, c8f16650a4c5 | Added multi-angle higher-moment checks, results, and assertions that fail on recurrence mismatch. |
| Level-6 extension and formal build | b5c43066f6bb, 1ef2712d9b3e, 1a022f8f50a7 | Added level-6 held-out predictions, pinned Lean CI, and corresponding claim-ledger updates. |
| Focus on analytic closure | b1c5e39c4b79 | Reoriented the research program toward deriving exact recurrence coefficients and explaining the exceptional base transition, rather than merely adding numerical points. |
| Thirteen-angle grid and independent numerical route | 4351fb480313, 819fcda8c475, e62576607468 | Expanded the level-5 grid to 13 predeclared angles, preserved results, and compared eigenvalue-power sums with direct matrix-power traces at smaller levels. |
| Stronger held-out assertions and consolidated evidence | 6b0c5ee48abd, fb57d96f79a8 | Added recurrence-consistency assertions across specified transitions and consolidated machine-readable data and interpretation. |
| Explicit closure criteria and preserved level-6 data | 06e5edbbd88a | Preserved level-6 outputs and documented the criteria required before the recurrence can be called a theorem. |
| Lean build on every main update | 3476ac9e63b3 | Added a pinned-source Lean build to push and pull-request CI. The successful build concerns the source project's fourth-moment formalization only. |

The commit history contains 31 commits through 3476ac9e63b364c00e84f6a28883e3e77c317a18 at the time this chronology was checked. The chronology is intentionally commit-backed and does not invent earlier dates for the source projects or claim that all prior research archives have been reviewed.

## Current scientific interpretation

1. The source project's fourth-moment formula is reported as Lean-formalized for its exact definitions and assumptions; the synthesis CI successfully builds a pinned source revision.
2. The H⁶/H⁸/H¹⁰ recurrence is supported by finite numerical holdouts through level 6 on a specified set of angles. It remains a conjecture.
3. The transition \(1\to2\) is numerically exceptional for every nonzero angle tested.
4. Exact coefficient functions and a universal proof for all levels and angles have not been obtained.
5. Phi-Genesis Gate A remains open, the mass-index fit is not established as predictive, and a cross-model equivalence has not been proved.

## Provenance rule for future changes

Every new milestone should record the commit or tag, exact claim or code change, test command/workflow, result, and remaining limitations. Preserve failed tests and negative results. Do not infer mathematical validity from a green status icon alone.