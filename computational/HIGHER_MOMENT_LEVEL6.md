# Level-6 higher-moment holdout

This calculation extends the level-5 test to level 6 at $\theta=0,\pi/2,\pi$. The operator source is pinned to the same reviewed Evgeny-Theorem commit as the earlier holdouts.

For each power $p\in\{6,8,10\}$, the recurrence constant is fixed from levels 3 and 4: $C=d_4-3d_3$.
The script then predicts both level 5 and level 6 without refitting. It reports transition constants for 1→2 through 5→6 and cross-checks the published level-1..4 values at $\theta=\pi/2$.

Level 6 has 2,190-dimensional operators, so this workflow has a 45-minute limit. If the job fails due to time, memory, or numerical mismatch, record the failure and investigate; do not silently weaken the validation thresholds.

This is a numerical test of a candidate recurrence at three angles and six levels, not a proof for all levels or all angles.

The current script explicitly checks recurrence consistency at the level-2-to-level-3, level-4-to-level-5, and level-5-to-level-6 transitions, in addition to predicting levels 5 and 6 from the coefficient fixed at levels 3 and 4. The output is preserved in `data/higher_moment_level6_3angles.json`.
