# Level-5 higher-moment holdout results

**Status:** numerical result reproduced in GitHub Actions; not a proof.

- Workflow run: [Higher-moment holdout computation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38758708458)
- Synthesis commit: `159a95c54b0923218640a1563a220a7c4ef3c95e`
- Pinned source commit: [RFT-SIRM/Evgeny-Theorem @ 9ed32ae](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/9ed32ae27b4493945624c2911d2815059613a9f5)
- Parameter: \(\theta=\pi/2\)
- Method: Hermitian eigenvalues via NumPy `eigvalsh`; calculate \(\operatorname{Tr}(H^p)=\sum_j\lambda_j^p\). The published source tests use direct matrix powers for H⁸ and H¹⁰, giving a distinct numerical route.
- Levels 1–4 matched the published references with relative discrepancies below \(1.3\times10^{-13}\).

## Level-5 results and holdout residuals

The recurrence constant was fixed from levels 3 and 4:
\[
C=d_4-3d_3,
\]
then the level-5 prediction was \(d_5^{\mathrm{pred}}=3d_4+C\). Level 5 was not used to fit the constant.

| Moment | \(d_5=\Delta_5(H^p,\pi/2)\) | \(C_{3\to4}\) | \(C_{4\to5}\) | Relative prediction residual |
|---|---:|---:|---:|---:|
| H⁶ | −154087.54980121367 | 2595.411254964536 | 2595.4112549955025 | \(2.01\times10^{-13}\) |
| H⁸ | −14076040.892380476 | 153107.52315880358 | 153107.52315998077 | \(8.36\times10^{-14}\) |
| H¹⁰ | −948802179.9008713 | 5287216.621796608 | 5287216.621850014 | \(5.63\times10^{-14}\) |

## Interpretation

1. The first transition \(1\to2\) remains an exception in the published table for all three powers.
2. At \(\theta=\pi/2\), the recurrence inferred from levels 3 and 4 predicts level 5 with very small relative residuals for H⁶, H⁸, and H¹⁰.
3. This supports the numerical recurrence regime beginning with the transition \(2\to3\) for these powers at this parameter. It does **not** prove a universal identity for every level or every angle.
4. The computation and published-reference cross-check both passed in CI. This validates the numerical pipeline at the stated scope; it is not an analytic proof.

## Next checks

- Repeat the level-5 holdout across a declared grid of angles, especially \(\theta=0\) and \(\theta=\pi\).
- Run level 6 if resource estimates remain acceptable.
- Correct source-project wording only after the broader checks are reviewed.
