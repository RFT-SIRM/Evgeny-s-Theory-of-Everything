# Higher-moment angle-grid audit

This workflow tests H⁶, H⁸ and H¹⁰ on levels 1–5 at seven fixed angles: 0, π/6, π/4, π/3, π/2, 2π/3 and π. The angle set is explicit in the script before results are inspected.

For each angle and power, the script computes the transition constants C_{m-1→m} = Δ_m − 3Δ_{m−1}, fixes C from levels 3 and 4, and compares the level-5 prediction against the computed value. It also records the first transition so base-case exceptions remain visible. The π/2 results are cross-checked against the published level-1..4 table.

The operator construction is taken from the pinned Evgeny-Theorem commit in the workflow. The method uses Hermitian eigenvalues, a different numerical route from direct matrix powers used by some source tests. It is not a proof and does not establish a universal recurrence.

Workflow output is uploaded as the artifact `higher-moment-angle-grid`. Review residuals, angle by angle, before changing any claim or theorem wording.
