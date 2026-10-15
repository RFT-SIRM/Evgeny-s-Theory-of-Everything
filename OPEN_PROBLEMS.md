# Open problems

## OP-1 — Independent recurrence verification for higher trace moments

For each proposed recurrence of the form
\[
\Delta_m = 3\Delta_{m-1}+C(\theta),
\]
determine the exact starting level, parameter domain, and operator family for which it holds.

An arithmetic audit of the published θ = π/2 reference table found that the first transition 1→2 has a different implied constant from transitions 2→3 and 3→4 for H⁶, H⁸, and H¹⁰. This is a warning about the claimed starting range, not a refutation of a recurrence that may hold from a later level.

Requirements:
- define Δ_m and the sign convention precisely;
- estimate or derive C(θ) independently of the transition used to test the recurrence;
- test at least one additional level not used to fit or define the constant;
- include base cases and exceptional levels;
- distinguish floating-point tolerance from exact equality;
- regenerate the source matrix traces rather than relying only on the published table.

## OP-2 — Structural derivation of higher-moment laws

Determine whether the observed higher-moment behaviour follows from graph recursion, operator block structure, path expansions, representation-theoretic identities, or another exact mechanism. If no such derivation is found, document the obstruction rather than promoting the numerical pattern.

## OP-3 — Complete exceptional set for spectral decimation

Characterize the full exceptional set, including recursively generated preimages where relevant. Simple exclusion of a finite list is insufficient if residual mismatches remain. State a criterion that can be checked independently at each level.

## OP-4 — Cross-model relationship

Determine whether there is a mathematically precise relation between the SU(2)-connected operators and signed Z₂-flux Laplacians. Candidate relationships must be stated as conjectures until a map and its consequences are proved.

## OP-5 — Reproducibility and formal CI

Make the source project's exact theorem build part of automated verification. Pin toolchain and dependencies. Keep computational tests and formal proof checks separately visible so that a Python test pass cannot be mistaken for formal verification.
