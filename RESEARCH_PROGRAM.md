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

Numerical holdouts cover levels 1–5 at thirteen predeclared angles $\theta=k\pi/12$, $k=0,\ldots,12$, levels 1–6 at $0,\pi/2,\pi$, and independent sparse-matrix-power checks through level 7 at five angles. Exact modular/CRT checks now certify the Fourier coefficients of the finite-level residuals $R_2^{(p)}=\Delta_2^{(p)}-3\Delta_1^{(p)}$ and $R_4^{(p)}=\Delta_4^{(p)}-3\Delta_3^{(p)}$, for $p=6,8,10$.

The remaining central question is whether $R_m^{(p)}(\theta)=R_4^{(p)}(\theta)$ for every $m\ge3$ and every angle. This is still a conjecture.

Next tasks:
- derive the level-independent recurrence from graph recursion, operator block structure, closed-walk enumeration, or representation theory;
- explain the exceptional transition $1\to2$, whose finite-level correction is now explicitly certified but not structurally explained;
- retain fixed-coefficient holdouts as regression checks, not as a substitute for proof;
- pursue Lean formalization after the all-level statement and proof route are clear.

A recurrence constant defined as $C_m=\Delta_m-3\Delta_{m-1}$ makes the equation true by definition at that transition. Evidence for a level-independent constant requires comparing distinct transitions, with the coefficient fixed independently of the transitions being tested.

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

## Workstream E — Exact scalar-invariant limit

**Source:** [RFT-SIRM/RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis)

The scalar invariant defined in that project has the exact remainder

$
I_m(\theta)-I_\infty(\theta)
=-\frac{32}{9(3^m+1)}\sin^2\!\left(\frac{\theta}{2}\right),
\qquad
I_\infty(\theta)=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right).

$
Its convergence theorem is machine-checked in Lean as **rftInvariant_tendsto**; the post-merge Lean build passed. The shared theorem dossier records the statement and provenance in [the exact invariant limit page](theorems/exact_invariant_limit.md).

This workstream is deliberately tracked separately from the higher-moment recurrence and signed-flux decimation programme. It does not establish a physical cosmological law or a bridge between the distinct operator models.

## Current sequence

1. Maintain the claims ledger and provenance map.
2. Prove that the certified finite-level coefficient $R_4^{(p)}$ is the same residual at every level $m\ge3$.
3. Derive the base-case correction from the recursive graph/operator structure.
4. Extend path-class cancellation results beyond the level-1 H⁶ calculation.
5. Return to Gate A only with a precise exceptional-set criterion.
6. Formulate a unified theorem only after a rigorous bridge between the operator families is established.
