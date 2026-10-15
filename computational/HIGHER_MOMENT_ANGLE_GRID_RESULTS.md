# Higher-moment angle-grid results

**Status:** numerical holdout passed on the pinned source implementation; not a proof.

- Workflow: [Higher-moment angle-grid holdout](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38759029736)
- Synthesis commit tested: `b0f73045deff77aa84aaa8446af1020c8915539e`
- Source commit: [RFT-SIRM/Evgeny-Theorem @ 9ed32ae](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/9ed32ae27b4493945624c2911d2815059613a9f5)
- Levels: 1–5
- Powers: 6, 8, 10
- Angles: \(0,\pi/6,\pi/4,\pi/3,\pi/2,2\pi/3,\pi\)
- Method: NumPy Hermitian eigenspectra; traces evaluated as sums of eigenvalue powers.

## Results

For each angle and moment, the recurrence constant was fixed from levels 3 and 4, then used to predict level 5. The maximum relative residual across H⁶, H⁸, and H¹⁰ was:

| Angle | Maximum relative residual |
|---|---:|
| 0 | 0 (all defects vanish) |
| \(\pi/6\) | \(1.65\times10^{-12}\) |
| \(\pi/4\) | \(3.45\times10^{-13}\) |
| \(\pi/3\) | \(2.78\times10^{-13}\) |
| \(\pi/2\) | \(2.01\times10^{-13}\) |
| \(2\pi/3\) | \(2.09\times10^{-13}\) |
| \(\pi\) | \(2.06\times10^{-14}\) |

The π/2 calculation also reproduced the published levels 1–4 reference values within the configured tolerance. Across the full angle grid, constants inferred from transitions 2→3, 3→4, and 4→5 agree to numerical precision for all three moments. The first transition 1→2 remains different for each nonzero angle tested.

Examples at \(\theta=\pi\):
- H⁶: \(C_{1\to2}\approx5256\), while later transitions give \(C\approx5280\).
- H⁸: \(C_{1\to2}\approx268960\), while later transitions give \(C\approx277504\).
- H¹⁰: \(C_{1\to2}\approx4006040\), while later transitions give \(C\approx4507520\).

## Interpretation

The numerical evidence now supports a more precise candidate statement: for the tested operator family, the recurrence with a level-independent constant appears to apply from the transition \(2\to3\) onward (equivalently, \(m\ge3\) in \(\Delta_m=3\Delta_{m-1}+C(\theta)\)), while the base transition \(1\to2\) is exceptional.

This remains a finite numerical result on levels 1–5 and seven angles. It does not prove the recurrence for all levels or all angles, nor does it derive a symbolic expression for \(C(\theta)\). A level-6 holdout and an analytic derivation are the next verification targets.
