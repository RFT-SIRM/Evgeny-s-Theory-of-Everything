# Research milestone and closure checklist

## Current milestone: exact finite-level coefficients plus reproducible holdouts

**Status: finite-level coefficient certificate and numerical validation achieved; analytical all-level closure remains open.**

This milestone includes:
- pinned source code from RFT-SIRM/Evgeny-Theorem;
- H⁶/H⁸/H¹⁰ level-5 holdouts at 13 predeclared angles;
- level-6 holdouts at 0, $\pi/2$, and $\pi$;
- independent sparse-matrix-power holdouts through level 7 at five angles;
- exact modular/CRT certificates for the Fourier coefficients of $R_2^{(p)}$ and $R_4^{(p)}$, $p=6,8,10$;
- seven off-grid floating-point validations of the reconstructed coefficient expressions;
- direct matrix-power versus eigenvalue-power cross-checks at levels 1–4;
- machine-readable JSON outputs and a successful pinned-source Lean build for the source project's fourth-moment formalization;
- a claims ledger that separates formalized H⁴ from the still-open all-level higher-moment recurrence.

## Current evidence boundary

The all-level higher-moment recurrence remains a **conjecture**, not a proved theorem. The exact finite-level Fourier coefficients for $R_2$ and $R_4$ are certified by modular arithmetic and CRT, and the recurrence passes numerical holdouts through level 7 at five angles. This does not prove $R_m=R_4$ for every $m\ge3$ or every angle.

## Completion checklist for the higher-moment recurrence

- [x] Recover and certify exact Fourier coefficients for the finite-level residuals $R_2^{(p)}$ and $R_4^{(p)}$, $p=6,8,10$, using the modular/CRT certificate.
- [x] Independently validate the coefficient candidates at seven off-grid angles and recurrence predictions through level 7 at five angles.
- [ ] Derive the recurrence from the recursive graph/operator construction, not from finite-level coefficient identities alone.
- [ ] Prove $R_m^{(p)}(\theta)=R_4^{(p)}(\theta)$ for every $m\ge3$ and all stated angles.
- [ ] Prove the exact starting level and explain the exceptional base transition structurally.
- [ ] State all hypotheses and exceptional parameter values explicitly.
- [ ] Formalize the all-level recurrence in Lean if the proof can be expressed and maintained cleanly.
- [ ] Add regression tests for each proved special case and retain the current holdouts.
- [ ] Update the claims ledger again only after reviewing the all-level proof and formal build.

## Completion checklist for the broader unified program

- [ ] Preserve exact provenance and evidence boundaries for both source projects.
- [ ] Resolve or explicitly leave open the full exceptional set in Phi-Genesis spectral decimation.
- [ ] Do not present the mass-index fit as a predictive law without a derived selection rule and held-out validation.
- [ ] State and prove any proposed bridge between the SU(2)-connected operators and signed Z₂-flux Laplacians before claiming unification.
- [ ] Review the complete README, mathematical framework, claims ledger, open problems, reproducibility notes, and historical record.
- [ ] Run all computational and Lean workflows from the final commit.
- [ ] Tag a release only when its name describes the evidence actually delivered.

## Release policy

Do not tag the current state as a completed “Theory of Everything” or as a proven higher-moment law. The defensible milestone is an exact finite-level coefficient certificate plus reproducible higher-moment holdouts, with the universal recurrence and its structural explanation still open. A future release can mark the recurrence as proved only after the all-level derivation and verification criteria above are satisfied.
