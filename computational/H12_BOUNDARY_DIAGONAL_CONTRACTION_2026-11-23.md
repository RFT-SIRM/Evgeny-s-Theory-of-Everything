# H12 boundary contraction: exact word reduction and radius-five audit

Date: 23 November 2026

## Result

The degree-12 gluing expansion has been reduced from 2,048 ordered positive compositions to a boundary expression involving only diagonal spatial corner blocks of the powers \(K^j\), with full \(2\times2\) spin-matrix multiplication order preserved.

The reduction is exact under the gluing and short-distance hypotheses stated below. It does **not** discard nonzero off-diagonal corner blocks by pretending they vanish. On the exceptional level-3 graph those blocks really appear from power 8 onward; instead, the cyclic pairing argument shows that at most one such long spatial block can occur in one composition, while every other factor is spatially block diagonal. Consequently the trace sees only the spatial diagonal block of the one unrestricted factor.

The exact inventory is:

| Quantity | Exact result |
|---|---:|
| Ordered positive compositions of 12 | 2,048 |
| Compositions with at least one exponent \(\ge8\) at level 3 | 48 |
| Odd-\(r\) compositions, all trace-zero | 1,024 |
| Even-\(r\) compositions reduced to boundary products | 1,024 |
| Genuine off-diagonal corner terms needed in the trace | **0** |
| Cyclic representatives among even-\(r\) compositions | 179 |
| Sum of even-stratum cyclic weights | 2,047 |

The machine-readable inventory is `computational/data/h12_boundary_diagonal_contraction.json`.

## 1. Ordered-word expansion

The source representation is \(H_{m+1}=E K_m E^\top\), where \(K_m\) is block diagonal on three copies and \(N\) is the fixed-point-free pairing of the six glued corner states. Expanding the positive-moment trace gives

\[
\operatorname{Tr}((K+KN)^{12})=\operatorname{Tr}(K^{12})+
\sum_{r=1}^{12}\frac{12}{r}
\sum_{\substack{a_1+\cdots+a_r=12\\a_i\ge1}}
\operatorname{Tr}(K^{a_1}N\cdots K^{a_r}N).
\]

The 2,048 compositions are the nonempty cyclic gap descriptions. The factor \(12/r\) counts cyclic placements of the \(r\) gluing factors. The total weighted count is \(2^{12}-1=4,095\). Cyclic orbit grouping retains periodic words with their exact orbit sizes; it produces 179 representatives for even \(r\), with total weight 2,047.

## 2. Why odd strata vanish

At level 3 the distinct glued spatial corners in one copy are separated by graph distance 8. Thus every power \(K^j\) with \(1\le j<8\) has zero spatial off-diagonal block between distinct glued points in one copy.

Since \(a_1+\cdots+a_r=12\), at most one exponent can be at least 8. If \(r\ge3\) is odd, the cyclic list of \(r\) gaps has a matching of \((r-1)/2\) pairwise nonadjacent gaps, all shorter than 8. Replace each selected pair by \(N K^j N\). The short-distance hypothesis makes each such factor spatially block diagonal on the glued boundary. The nonadjacent choice ensures no two replacements consume the same \(N\). Exactly one \(N\) remains. All other factors are block diagonal with respect to the three-copy index, so the remaining trace is zero by the block-diagonal-times-one-pairing trace lemma.

The case \(r=1\) is \(\operatorname{Tr}(K^{12}N)=0\), since \(K^{12}\) is copy block diagonal while \(N\) pairs different copies.

Therefore all 1,024 odd-\(r\) compositions vanish.

## 3. Why even strata need no off-diagonal corner data

If \(r\) is even, choose one of the two alternating perfect matchings of the cycle of gaps. If there is a unique exponent at least 8, choose the matching that does not select it; otherwise either alternating matching works. The selected short gaps again collapse to spatially block-diagonal \(N K^j N\) factors.

The unselected gaps are the remaining \(K^{a_i}\) factors. All but at most one have exponent below 8, so all but at most one are spatially block diagonal on the glued boundary. In the trace of a product with all other factors spatially block diagonal, the one unrestricted factor contributes only its spatial diagonal block. This remains true when every diagonal spatial block is a fully general, noncommuting \(2\times2\) spin matrix.

For an even composition \((a_1,\ldots,a_r)\), define

\[
M_j(x)=(K^j)_{x,x}\in M_2(\mathbb C),
\]

where \(x\) is a glued spatial corner and the entry is its ordered spin block. The resulting boundary contraction is

\[
B(a_1,\ldots,a_r)=\sum_{x\in\mathcal G}
\operatorname{tr}_2\!\left(
M_{a_1}(\sigma x)M_{a_2}(x)\cdots
M_{a_{r-1}}(\sigma x)M_{a_r}(x)
\right).
\]

No factors have been commuted or scalarized. Cyclic rotation leaves \(B\) unchanged: rotate the product under \(\operatorname{tr}_2\), then reindex \(x\mapsto\sigma x\). Thus the even part of the degree-12 trace correction is exactly

\[
\boxed{\displaystyle
\sum_{\substack{2\le r\le12\\r\ \mathrm{even}}}
\frac{12}{r}\sum_{(a_1,\ldots,a_r)\in\operatorname{Comp}(12,r)}
B(a_1,\ldots,a_r).}
\]

The independent exact test constructs all six glued spatial states and three copies, assigns arbitrary noncommuting integer \(2\times2\) spin blocks, permits arbitrary long spatial off-diagonal blocks at powers 8--12, and checks every composition by direct closed boundary paths. All 1,023 odd words with \(r\ge3\) vanish, and all 1,024 even words equal the displayed diagonal-block formula. The single-\(N\) case is checked separately. Seven regression tests pass.

## 4. Connection to the pinned source lemmas

The following declarations were inspected read-only at `RFT-SIRM/Evgeny-Theorem@4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f`:

- `GlueK.pOpO_succ_trace_ordered_words`: the actual three-copy Sierpiński operator has the ordered-word trace expansion for every positive power.
- `GlueK.sg_EKEt`: identifies the level-\((m+1)\) operator with the three-copy pushforward.
- `GlueSG.sgGlue` / `GlueSG.sgσ`: the six glued states are paired by a fixed-point-free involution; `glW` requires the spin coordinate to be preserved.
- `GlueAlg.Q_eq_diag`: collapses \(N K^j N\) under the same-copy glued-state vanishing premise.
- `GlueAlg.trace_BD_N`: annihilates a copy-block-diagonal product followed by a single \(N\).
- `GlueCorner.sgK_pow_GlueDiag_of_OAnti` and `GlueCorner.sgK_pow_hkg_of_OAnti`: provide the spin and geometric parts of the corner-vanishing hypotheses for the concrete operator.

The source's state-level hypotheses are stronger than the spatial-block hypotheses used by the independent \(2\times2\) test. Hence the block test does not assume away noncommutativity; it stress-tests a more general spin-block setting.

No file in `Evgeny-Theorem` was modified by this package.

## 5. Radius-five locality for powers through 11

A closed walk of length \(j\) starting and ending at a corner stays within distance \(\lfloor j/2\rfloor\). Therefore a rooted radius-five isomorphism preserving the full directed operator blocks identifies the diagonal corner blocks through \(j=11\).

The existing recursive corner-neighbourhood argument extends from radius 4 to radius 5 without changing its mechanism:

1. For every \(m\ge3\), the nearest junction with another recursive copy is at distance \(2^m\ge8>5\). A radius-five outer-corner ball lies wholly inside its corner copy; no ball vertex is a copy junction, so the full-graph onsite degree is preserved.
2. Face lists are concatenated in blocks of length \(3^m\), divisible by 3. Hence the face-index Pauli-axis label modulo 3 is preserved by the recursive copy map.
3. No vertex of the radius-five ball is removed as a shared junction by the `eraseDups`/`removeAll` filtering in the recursive vertex order. Filtering other list entries cannot reverse the relative order of two surviving vertices. Thus the directed smaller-index/larger-index sign selecting \(U\) versus \(U^\ast\) is preserved on the ball.
4. The exceptional `oNum`/`oTil` edge lies in copy B at coordinates \((2^m-1,0)\) or \((2^m,0)\). Its nearest glued B corner is at coordinate distance at least \(2^m-1\ge7>5\). Thus it does not intersect any glued-root radius-five ball for \(m\ge3\).

These four points give a paper-level all-level radius-five directed-operator transport argument for the specified source recursion. The corresponding radius-five transport has not yet been added as a Lean theorem.

## 6. Independent finite checks

Two reproducible audits accompany the argument:

- `h12_operator_corner_label_radius5_audit.json`: exact graph-isomorphism audit of radius-five directed labels for all three corners, levels 3--10, and both the noncommuting SU(2) operator and commuting control. Every ball matches its same-corner level-3 reference; each has 19 vertices and 66 directed edges.
- `h12_corner_moments_order11_diagnostic.json`: sparse numerical diagnostic for levels 3--6, powers 1--11, ten angles, and both operator models. The largest observed diagonal-block difference across levels is exactly 0 in the computed arrays. On level 3, spatial off-diagonal corner blocks first appear at power 8; their maximum absolute entries at powers 8, 9, 10, and 11 are approximately 1.0000, 34.1760, 694.6654, and 10,903.6759 respectively.

The first audit is finite combinatorial evidence; the second is floating-point diagnostic evidence. Neither is described as a Lean proof. They are independent regression checks for the paper-level locality and the pairing reduction.

## 7. What is closed and what remains

**Closed in this synthesis step:** the degree-12 ordered-word inventory; the odd/even pairing classification; the exact diagonal-corner contraction formula; cyclic orbit counts and integer weights; the level-three exceptional-block treatment; the radius-five paper induction; and finite reproducibility checks.

**Still required for a full all-level H12 theorem:**

1. Write the H12 copy-A/B/C trace-transfer bookkeeping in the synthesis proof, extending the already existing H10 pattern to moment 12 and making every orientation/gauge map explicit.
2. Combine that transfer with the invariant radius-five diagonal corner blocks to identify the level-independent boundary correction for every \(m\ge3\).
3. Port the radius-five transport, degree-12 trace-word pairing reduction, and the final recurrence to Lean; compile the Lean project and add the resulting theorem names/source pin to `CURRENT_EVIDENCE.md`.
4. Use the exact external H12 CRT certificate through level 8 as the finite coefficient identification, while keeping its evidence label external until the coefficient identity is proved in Lean.

The target recurrence is

\[
D_{m+1}^{(12)}(\theta)=3D_m^{(12)}(\theta)+C_{12}(\theta),
\qquad m\ge3,
\]

with the already reconstructed finite candidate
\(C_{12}(\pi)=-634{,}073{,}536\) and the exact polynomial/Fourier coefficients recorded in `H12_FINITE_RESIDUAL_2026-11-23.md`. This report does not label the target recurrence as Lean-formalized or as fully closed before items 1--3 are discharged.

## Reproduction

From the repository root:

```sh
python3 -m computational.h12_boundary_diagonal_contraction --output computational/data/h12_boundary_diagonal_contraction.json
python3 -m unittest computational.test_h12_boundary_diagonal_contraction -v
python3 -m computational.audit_operator_corner_labels_radius5 --output computational/data/h12_operator_corner_label_radius5_audit.json
python3 computational/diagnose_corner_moments_h12.py --output computational/data/h12_corner_moments_order11_diagnostic.json
```

The first two checks are exact integer/combinatorial calculations. The directed-label audit uses a self-contained exact small-graph isomorphism checker and only the Python standard library. The auxiliary corner-moment diagnostic requires NumPy and SciPy; local installation skips this auxiliary floating-point diagnostic with an explicit notice when either dependency is absent, while GitHub Actions installs both. The GitHub Actions workflow compares all three regenerated JSON artifacts with the committed results.
