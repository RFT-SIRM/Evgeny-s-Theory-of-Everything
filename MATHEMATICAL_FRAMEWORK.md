# Mathematical framework: current definitions and boundaries

## 1. Trace-moment defects

For a finite-dimensional operator H and a positive integer k, the k-th trace moment is Tr(H^k). Given two explicitly defined operators H_C and H_C', one may define a defect
$
\Delta_m(H^k,\theta)
=\mathrm{Tr}(H_C^k)-\mathrm{Tr}(H_{C'}^k).
$
The subscript m and parameter θ must be defined by the model. This generic notation is not a claim that every operator family shares the same formula.

## 2. Documented fourth-moment result

The source project reports the following formula for its specific SU(2)-connected Sierpiński-gasket model:
$
\Delta_m(H^4,\theta)
=-16(3^{m-1}+1)\sin^2(\theta/2),\qquad m\ge 1.
$
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

## 5. What a unified theorem must contain

A proposed general theorem must state:
1. the mathematical objects and admissible parameters;
2. all hypotheses and quantifiers;
3. the exact invariant or identity;
4. the proof, including exceptional cases;
5. a formalization or independent computational check where practical;
6. a clear account of what the theorem does not imply.
