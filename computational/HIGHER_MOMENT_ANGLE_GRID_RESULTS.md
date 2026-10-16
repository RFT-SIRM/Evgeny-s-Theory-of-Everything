# Higher-moment angle-grid results

**Status:** numerical holdout passed on the pinned source implementation; not a proof.

- Workflow: [Higher-moment angle-grid holdout](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38761487044)
- Synthesis commit tested: `6b0c5ee48abdc80e52a8dbca2a67d325364190f0`
- Source commit: [RFT-SIRM/Evgeny-Theorem @ 9ed32ae](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/9ed32ae27b4493945624c2911d2815059613a9f5)
- Levels: 1–5
- Powers: 6, 8, 10
- Angles: $0,\pi/6,\pi/4,\pi/3,\pi/2,2\pi/3,\pi$
- Method: NumPy Hermitian eigenspectra; traces evaluated as sums of eigenvalue powers.

## Results

For each angle and moment, the recurrence constant was fixed from levels 3 and 4, then used to predict level 5. The maximum relative residual across H⁶, H⁸, and H¹⁰ was:

| Angle | Maximum relative residual |
|---|---:|
| 0 | 0 (all defects vanish) |
| $\pi/6$ | $1.65\times10^{-12}$ |
| $\pi/4$ | $3.45\times10^{-13}$ |
| $\pi/3$ | $2.78\times10^{-13}$ |
| $\pi/2$ | $2.01\times10^{-13}$ |
| $2\pi/3$ | $2.09\times10^{-13}$ |
| $\pi$ | $2.06\times10^{-14}$ |

The π/2 calculation also reproduced the published levels 1–4 reference values within the configured tolerance. A second numerical route evaluated direct matrix powers at levels 1–4 for every grid angle; maximum relative disagreement with eigenvalue-power sums was about $4.37\times10^{-12}$ (H⁶), $1.60\times10^{-12}$ (H⁸), and $1.42\times10^{-12}$ (H¹⁰). Across the full angle grid, constants inferred from transitions 2→3, 3→4, and 4→5 agree to numerical precision for all three moments. The first transition 1→2 remains different for each nonzero angle tested.

Examples at $\theta=\pi$:
- H⁶: $C_{1\to2}\approx5256$, while later transitions give $C\approx5280$.
- H⁸: $C_{1\to2}\approx268960$, while later transitions give $C\approx277504$.
- H¹⁰: $C_{1\to2}\approx4006040$, while later transitions give $C\approx4507520$.

## Interpretation

The numerical evidence now supports a more precise candidate statement: for the tested operator family, the recurrence with a level-independent constant appears to apply from the transition $2\to3$ onward (equivalently, $m\ge3$ in $\Delta_m=3\Delta_{m-1}+C(\theta)$), while the base transition $1\to2$ is exceptional.

The 13-angle data are stored in [`data/higher_moment_angle_grid_13.json`](data/higher_moment_angle_grid_13.json). Maximum relative level-5 residuals across the grid are approximately $1.47\times10^{-12}$ (H⁶), $1.80\times10^{-12}$ (H⁸), and $8.82\times10^{-13}$ (H¹⁰). The complete numerical output, including every sampled coefficient and residual, is preserved in [`data/higher_moment_angle_grid_13.json`](data/higher_moment_angle_grid_13.json). This remains a finite numerical result on levels 1–5 and 13 angles. It does not prove the recurrence for all levels or all angles, nor does it derive a symbolic expression for $C(\theta)$. A separate [level-6 holdout](HIGHER_MOMENT_LEVEL6_RESULTS.md) has also passed at $0,\pi/2,\pi$. An analytic derivation remains the principal open target.
