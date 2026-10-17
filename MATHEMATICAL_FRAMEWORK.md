# Mathematical framework: current definitions and boundaries

## 1. Trace-moment defects

For a finite-dimensional operator H and a positive integer k, the k-th trace moment is Tr(H^k). Given two explicitly defined operators H_C and H_C', one may define a defect
$$
\Delta_m(H^k,\theta)
=\mathrm{Tr}(H_C^k)-\mathrm{Tr}(H_{C'}^k).
$$
The subscript m and parameter θ must be defined by the model. This generic notation is not a claim that every operator family shares the same formula.

## 2. Documented fourth-moment result

The source project reports the following formula for its specific SU(2)-connected Sierpiński-gasket model:
$$
\Delta_m(H^4,\theta)
=-16(3^{m-1}+1)\sin^2(\theta/2),\qquad m\ge 1.
$$
The exact definitions of H_C, H_C', the graph level, and the connection patterns must be taken from the source theorem and its Lean definitions. This repository's summary must not replace those formal definitions.

## 3. Higher moments are not yet unified laws

Numerical patterns for k = 6, 8, 10 may suggest recurrences, but each recurrence needs its own:
- exact statement and range;
- proof or explicitly bounded numerical evidence;
- base-case analysis;
- independent verification;
- exception list.

A finite set of matching values cannot establish a universal statement.

## 4. Distinct spectral models

The signed Z₂-flux model in Phi-Genesis must not be silently identified with the SU(2)-connection model. The graph, edge weights/connections, boundary conditions, and operator definitions need to be compared explicitly before any transfer of results is valid.

## 5. Exact limit of a separately defined scalar invariant

A separate source project defines
$$
I_m(\theta)=-16\frac{3^{m-1}+1}{3^{m+1}+3}\sin^2\!\left(\frac{\theta}{2}\right),\quad m\geq1,
$$
and proves the exact decomposition
$$
I_m(\theta)=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right)
-\frac{32}{9(3^m+1)}\sin^2\!\left(\frac{\theta}{2}\right).
$$
Thus the limit is

$$
I_\infty(\theta)=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right).
$$

The exact finite-level remainder is

$$
I_m(\theta)-I_\infty(\theta)
=-\frac{32}{9(3^m+1)}\sin^2\left(\frac{\theta}{2}\right).
$$

The Lean proof is maintained in [RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis), with provenance and exact verification links in [the theorem dossier](theorems/exact_invariant_limit.md).

This scalar theorem has its own definitions and proof boundary. It does not establish a cosmological interaction, observational agreement, or an operator equivalence with the SU(2) or signed-flux strands above.

## 6. What a unified theorem must contain

A proposed general theorem must state:
1. the mathematical objects and admissible parameters;
2. all hypotheses and quantifiers;
3. the exact invariant or identity;
4. the proof, including exceptional cases;
5. a formalization or independent computational check where practical;
6. a clear account of what the theorem does not imply.
