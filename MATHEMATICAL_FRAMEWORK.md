# Mathematical framework: current definitions and boundaries

## 1. Trace-moment defects

For a finite-dimensional operator H, the k-th trace moment is Tr(H^k). Given two explicitly defined operators H_C and H_C', define
\[
\Delta_m(H^k,\theta)=\mathrm{Tr}(H_C^k)-\mathrm{Tr}(H_{C'}^k).
\]
The model, graph level, parameter, boundary conditions, and sign convention must be specified. This generic notation does not assert that distinct source projects use the same operator.

## 2. SU(2)-connected Sierpiński-gasket model

For the precise operators in [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem), the source proves
\[
\Delta_m(H^4,\theta)=-16(3^{m-1}+1)\sin^2\left(\frac{\theta}{2}\right),\qquad m\ge1.
\]
The Lean source declaration and formal hypotheses are authoritative.

The higher-moment status must be recorded by its actual theorem range:

- H6: Lean recurrence and affine form for m ≥ 3; exact 2→3 bridge certified externally, not in Lean's kernel.
- H8: Lean recurrence and affine form for m ≥ 3; exact 2→3 bridge certified externally, not in Lean's kernel.
- H10: unconditional Lean recurrence for m ≥ 4, affine form for m ≥ 5, using proved radius-four transport through degree nine. The level-five residual is exact but not yet expanded into a trigonometric polynomial.

The exact declarations and finite-certificate files are listed in [CURRENT_EVIDENCE.md](CURRENT_EVIDENCE.md). The fourth-moment theorem does not imply higher-moment recurrences; each moment requires its own proof.

## 3. Signed-Z2-flux model

The signed-flux model in [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) uses its own signed Laplacian, gauge conventions, and spectral-decimation boundary data. Its Schur/Rayleigh results are separate from the SU(2) trace-moment results. The current formalized bootstrap statements concern a shifted quadratic form and Rayleigh minima; do not relabel them as an operator eigenvalue theorem without a proof.

Gate A's full exceptional-value criterion, the proposed quadratic spectral law, and the predictive interpretation of the mass-index fit remain unestablished.

## 4. Exact limit of a separately defined scalar invariant

A separate source project defines
\[
I_m(\theta)=-16\frac{3^{m-1}+1}{3^{m+1}+3}\sin^2\left(\frac{\theta}{2}\right).
\]
Its exact decomposition is
\[
I_m(\theta)=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right)
-\frac{32}{9(3^m+1)}\sin^2\left(\frac{\theta}{2}\right).
\]
Consequently,
\[
I_\infty(\theta)=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right),\qquad
I_m-I_\infty=-\frac{32}{9(3^m+1)}\sin^2\left(\frac{\theta}{2}\right).
\]
The limit and exact remainder are machine-checked in [RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis). This scalar theorem does not establish a physical cosmological law or an equivalence with either operator model above.

## 5. What a unified theorem must contain

Any future cross-model theorem must state:
1. the exact mathematical objects and admissible parameters;
2. all hypotheses, quantifiers, and exceptional cases;
3. the map between operator families;
4. the invariant or identity being transferred;
5. a proof that handles boundary and orientation effects;
6. the formal or independent computational evidence and its limitations.

Similarity of graph geometry or numerical behaviour is not a proof of operator equivalence.