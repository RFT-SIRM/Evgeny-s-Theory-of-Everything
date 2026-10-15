# Research program

## Workstream A — Fourth-moment theorem

**Source:** [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem)

The source project documents a closed formula for a fourth-moment trace defect for a specified SU(2)-connected Sierpiński-gasket operator family and reports a Lean 4 formalization.

Tasks:
- preserve the exact definitions and theorem statement from the Lean source;
- record the exact Lean toolchain and Mathlib dependency state;
- reproduce the build from a clean checkout;
- complete the new pinned-source Lean CI build;
- ensure explanatory documents agree with the formal theorem's hypotheses and indexing.

## Workstream B — Higher moments and recurrence derivation

Investigate H⁶, H⁸, H¹⁰ and beyond without presupposing that observed patterns are universal.

Numerical holdout coverage now includes levels 1–5 at thirteen predeclared angles \\(k\\pi/12, k=0,\\ldots,12\\) and levels 1–6 at \(0,\pi/2,\pi\). The candidate recurrence appears stable from transition 2→3 onward, while transition 1→2 is exceptional. This is a research observation, not a general theorem.

Next tasks:
- derive the exact coefficient function \(C_p(\theta)\) for \(p=6,8,10\);
- prove the starting level and explain the exceptional base transition;
- use graph recursion, operator block structure, closed-walk enumeration, or representation theory to derive the recurrence;
- retain the fixed-coefficient holdout tests as regression checks, not as a substitute for proof;
- pursue Lean formalization only after the mathematical statement and proof route are clear.

A recurrence constant defined by \(C_m=\Delta_m-3\Delta_{m-1}\) makes the equation true by definition at that transition. Evidence for a level-independent constant requires comparing distinct transitions, with the constant fixed independently of the transitions being tested.

## Workstream C — Signed Z₂-flux spectral decimation

**Source:** [RFT-SIRM/Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis)

Tasks:
- preserve the distinction between exact algebraic identities and floating-point inertia computations;
- investigate boundary and corner-defect corrections to decimation;
- characterize exceptional values and their recursively generated preimages;
- keep the Gate A status open until a complete criterion is independently verified;
- preserve failed and non-reproduced mass-index selection hypotheses as negative results.

## Workstream D — Cross-model bridge

No equivalence between the SU(2)-connection operators and signed Z₂-flux Laplacians is assumed.

A valid bridge must specify:
- the two operator families and their domains;
- the map or transformation relating them;
- which spectral or trace quantities are preserved;
- boundary conditions and exceptional cases;
- a proof, or a clearly labelled conjecture with falsifiable consequences.

## Current sequence

1. Maintain the claims ledger and provenance map.
2. Complete and review the Lean CI build.
3. Derive the exact higher-moment coefficient functions and explain the base exception.
4. Extend path-class cancellation results beyond the level-1 H⁶ calculation.
5. Return to Gate A only with a precise exceptional-set criterion.
6. Formulate a unified theorem only after a rigorous bridge between the operator families is established.
