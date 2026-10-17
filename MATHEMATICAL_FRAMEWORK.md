# Mathematical framework: current definitions and boundaries

## 1. Trace-moment defects

For a finite-dimensional operator $H$ and a positive integer $k$, the $k$-th trace moment is $\mathrm{Tr}(H^k)$. Given two explicitly defined operators $H_C$ and $H_{C'}$, one may define the trace defect

$$
\Delta_m(H^k,\theta)=\mathrm{Tr}(H_C^k)-\mathrm{Tr}(H_{C'}^k).
$$

The model must specify how the level $m$ and parameter $\theta$ enter the operators. This generic notation does not assert that every operator family has the same formula.

## 2. Documented fourth-moment result

The source project reports the following formula for its specific SU(2)-connected Sierpiński-gasket model:

$$
\Delta_m(H^4,\theta)=-16(3^{m-1}+1)\sin^2\left(\frac{\theta}{2}\right),\qquad m\geq1.
$$

The exact definitions of $H_C$, $H_{C'}$, the graph level, and the connection patterns are those in the [source project](https://github.com/RFT-SIRM/Evgeny-Theorem) and its Lean definitions. This summary does not replace those formal definitions or independently re-prove the theorem.

## 3. Higher moments are not yet unified laws

Numerical patterns for $k=6,8,10$ may suggest recurrences, but each proposed recurrence needs its own:

- exact statement and range of validity;
- proof, or explicitly bounded numerical evidence;
- base-case analysis;
- independent verification;
- list of exceptional cases.

Agreement at finitely many levels or angles cannot establish a universal statement.

## 4. Distinct spectral models

The signed $Z_2$-flux model studied in [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) must not be silently identified with the SU(2)-connection model. Before transferring a result between them, one must compare the graph, edge weights or connections, boundary conditions, and operator definitions explicitly.

## 5. Exact limit of a separately defined scalar invariant

A separate source project defines, for $m\geq1$, the scalar invariant

$$
I_m(\theta)=-16\frac{3^{m-1}+1}{3^{m+1}+3}\sin^2\left(\frac{\theta}{2}\right).
$$

Its exact decomposition is

$$
I_m(\theta)=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right)-\frac{32}{9(3^m+1)}\sin^2\left(\frac{\theta}{2}\right).
$$

Consequently, the limit is

$$
I_\infty(\theta)=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right).
$$

The exact finite-level remainder is

$$
I_m(\theta)-I_\infty(\theta)=-\frac{32}{9(3^m+1)}\sin^2\left(\frac{\theta}{2}\right).
$$

The machine-checked Lean proof is maintained in [RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis). The statement, algebraic derivation, theorem names, source commit, and CI evidence are collected in the [exact invariant limit theorem dossier](theorems/exact_invariant_limit.md).

This scalar theorem has its own definitions and proof boundary. It does not establish a cosmological interaction, agreement with observations, or an equivalence with either the SU(2)-connection or signed-flux operator model.

## 6. What a unified theorem must contain

A proposed general theorem must specify:

1. the mathematical objects and admissible parameters;
2. all hypotheses and quantifiers;
3. the exact invariant or identity;
4. a proof that handles exceptional cases;
5. a formalization or independent computational check, where practical;
6. an explicit account of what the theorem does not imply.
