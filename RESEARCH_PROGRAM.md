# Research program

## Workstream A — Fourth-moment theorem

**Source:** [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem)

The source project documents a closed formula for a fourth-moment trace defect for a specified SU(2)-connected Sierpiński-gasket operator family and reports a Lean 4 formalization.

Tasks:
- preserve the exact definitions and theorem statement from the Lean source;
- record the exact Lean toolchain and Mathlib dependency state;
- reproduce the build from a clean checkout;
- add or verify CI that actually runs the Lean build;
- ensure explanatory documents agree with the formal theorem's hypotheses and indexing.

## Workstream B — Higher moments

Investigate H⁶, H⁸, H¹⁰ and beyond without presupposing that observed patterns are universal.

Tasks:
- regenerate the moment tables from source code;
- verify graph-level indexing and the sign convention for the defect;
- independently test proposed recurrences on levels not used to define their constants;
- test base cases and exceptional levels explicitly;
- seek structural proofs, or record precise obstructions and counterexamples.

A recurrence constant defined by C_m = Δ_m − 3Δ_(m−1) makes the equation Δ_m = 3Δ_(m−1) + C_m true by definition. Evidence for a level-independent constant requires comparison across distinct transitions, with the constant fixed independently of the transition being tested.

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

## Initial sequence

1. Establish a claim ledger and provenance map.
2. Reproduce the source projects' documented results.
3. Fix tests that are tautological or insufficiently independent.
4. Add continuous integration for all formal and computational checks.
5. Only then formulate a unified theorem with explicit hypotheses.
