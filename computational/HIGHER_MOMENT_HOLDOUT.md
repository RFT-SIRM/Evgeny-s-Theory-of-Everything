# Higher-moment level-5 holdout

This workflow computes H6, H8 and H10 at theta = pi/2 for levels 1 through 5 from the source operator construction in the pinned Evgeny-Theorem revision.

It cross-checks levels 1–4 against the published reference values before interpreting level 5. The recurrence constant is fixed using levels 3 and 4 only; level 5 is held out and predicted without refitting. The JSON artifact reports actual values and residuals.

The calculation uses Hermitian eigenvalues and computes Tr(H^p) as sum(lambda^p), whereas the source reference tests use direct matrix powers for H8 and H10. This is a distinct numerical route but shares the same operator construction. It is numerical evidence, not a proof.

A successful run validates only the computation and cross-checks described here. A small level-5 residual supports the recurrence at this parameter and level; a large residual challenges it. Neither outcome establishes a universal identity over all levels or angles.
