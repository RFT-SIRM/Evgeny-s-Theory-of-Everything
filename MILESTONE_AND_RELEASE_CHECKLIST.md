# Research milestone and closure checklist

## Current milestone: reproducible numerical evidence

**Status: achieved for the current finite test matrix; analytical closure remains open.**

This milestone includes:
- pinned source code from RFT-SIRM/Evgeny-Theorem;
- H⁶/H⁸/H¹⁰ level-5 holdouts at 13 predeclared angles;
- level-6 holdouts at 0, π/2, and π;
- recurrence consistency assertions for the tested transitions;
- direct matrix-power versus eigenvalue-power cross-checks at levels 1–4 on the 13-angle grid;
- machine-readable JSON outputs committed to the repository;
- a successful pinned-source Lean build for the source project's fourth-moment formalization;
- a claim ledger that separates formalized H⁴ from numerical higher-moment evidence.

## Current evidence boundary

The higher-moment recurrence is a **numerically supported conjecture**, not a proved theorem. The current calculations support a level-independent coefficient from the level-2-to-level-3 transition onward on the tested finite set. The level-1-to-level-2 transition is exceptional at every nonzero tested angle.

The exact coefficient functions C₆(θ), C₈(θ), C₁₀(θ), the universal level quantifier, and a proof of the exceptional base case remain unresolved.

## Completion checklist for the higher-moment recurrence

- [ ] Derive an exact expression or algebraic characterization for each coefficient Cₚ(θ).
- [ ] Derive the recurrence from the recursive graph/operator construction, not from numerical fitting.
- [ ] Prove the exact starting level and the exceptional base transition.
- [ ] State all hypotheses and exceptional parameter values explicitly.
- [ ] Independently verify symbolic identities against the pinned numerical data.
- [ ] Formalize the recurrence in Lean if the proof can be expressed and maintained cleanly.
- [ ] Add a regression test for each proved special case and retain the current holdouts.
- [ ] Update the claims ledger only after reviewing the proof and the formal build.

## Completion checklist for the broader unified program

- [ ] Preserve exact provenance and evidence boundaries for both source projects.
- [ ] Resolve or explicitly leave open the full exceptional set in Phi-Genesis spectral decimation.
- [ ] Do not present the mass-index fit as a predictive law without a derived selection rule and held-out validation.
- [ ] State and prove any proposed bridge between the SU(2)-connected operators and signed Z₂-flux Laplacians before claiming unification.
- [ ] Review the complete README, mathematical framework, claims ledger, open problems, reproducibility notes, and historical record.
- [ ] Run all computational and Lean workflows from the final commit.
- [ ] Tag a release only when its name describes the evidence actually delivered.

## Release policy

Do not tag the current state as a completed “Theory of Everything” or as a proven higher-moment law. The defensible milestone is a reproducible research package with a formalized H⁴ result inherited from its pinned source and a substantially expanded numerical record for H⁶/H⁸/H¹⁰. A future release can mark the analytical recurrence as proved only after the exact derivation and verification criteria above are satisfied.
