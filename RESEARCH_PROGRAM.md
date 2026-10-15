# Research program

## Workstream A — Fourth-moment theorem

**Source:** [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem)

The source project documents a closed formula for a fourth-moment trace defect for a specified SU(2)-connected Sierpiński-gasket operator family and reports a Lean 4 formalization.

Tasks:
- preserve the exact definitions and theorem statement from the Lean source;
- record the exact Lean toolchain and Mathlib dependency state;
- keep the pinned-source CI build green after source or toolchain changes;
- ensure explanatory documents agree with the formal theorem's hypotheses and indexing.

## Workstream B — Higher moments and recurrence derivation

Investigate H⁶, H⁸, H¹⁰, and beyond without presupposing that observed patterns are universal.

Numerical holdouts cover levels 1–5 at thirteen predeclared angles \(\theta=k\pi/12\), \(k=0,\ldots,12\), and levels 1–6 at \(0,\pi/2,\pi\). The candidate recurrence appears stable from transition 2→3 onward on the tested set; transition 1→2 is exceptional. This is a research observation, not a general theorem.

Next tasks:
- derive the exact coefficient function \(C_p(\theta)\) for \(p=6,8,10\);
- prove the starting level and explain the exceptional base transition;
- derive the recurrence from graph recursion, operator block structure, closed-walk enumeration, or representation theory;
- retain fixed-coefficient holdouts as regression checks, not as a substitute for proof;
- pursue Lean formalization only after the mathematical statement and proof route are clear.

A recurrence constant defined as \(C_m=\Delta_m-3\Delta_{m-1}\) makes the equation true by definition at that transition. Evidence for a level-independent constant requires comparing distinct transitions, with the coefficient fixed independently of the transitions being tested.

## Workstream C — Signed Z₂-flux spectral decimation

**Source:** [RFT-SIRM/Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis)

Tasks:
- preserve the distinction between exact algebraic identities and floating-point inertia computations;
- investigate boundary and corner-defect corrections to decimation;
- characterize exceptional values and their recursively generated preimages;
- keep Gate A open until a complete criterion is independently verified;
- preserve failed and non-reproduced mass-index selection hypotheses as negative results.

## Workstream D — Cross-model bridge

No equivalence between the SU(2)-connection operators and signed Z₂-flux Laplacians is assumed.

A valid bridge must specify both operator families and domains, the map relating them, preserved spectral or trace quantities, boundary conditions and exceptional cases, and a proof—or a clearly labelled conjecture with falsifiable consequences.

## Current sequence

1. Maintain the claims ledger and provenance map.
2. Derive the exact higher-moment coefficient functions and explain the base exception.
3. Extend path-class cancellation results beyond the level-1 H⁶ calculation.
4. Return to Gate A only with a precise exceptional-set criterion.
5. Formulate a unified theorem only after a rigorous bridge between the operator families is established.