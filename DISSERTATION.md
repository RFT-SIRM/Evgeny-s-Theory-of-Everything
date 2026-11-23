> **Current status update — 23 November 2026.** The pinned source Lean development proves the H6/H8 recurrences from level 3, with exact external certificates for their finite 2-to-3 bridges, and proves the unconditional H10 recurrence from level 4 with affine form from level 5. H10 radius-four transport through degree 9 is Lean-checked. Its level-five correction is now source-reconstructed from the pinned graph/operator definitions by a direct C++ sparse-polynomial engine, a three-prime modular expansion, and signed coefficient-wise CRT under an explicit path-count bound. The coefficient expansion is an exact external certificate, not a Lean-kernel theorem. See CURRENT_EVIDENCE.md for exact scope.

# Recursive Graph Operators, Spectral Trace Defects, and Higher-Moment Recurrence

## Research dissertation

**Author:** Evgeny Zaprudnov  
**Research group:** RFT-SIRM  
**Version:** 1.0  
**Date:** 15 October 2026

## Abstract

This dissertation consolidates a research programme concerning trace defects of recursively constructed graph operators, focusing on Sierpinski-gasket approximations, SU(2)-connected operators, higher even trace moments, and a separate programme on signed Z2-flux Laplacians and spectral decimation. It distinguishes Lean-checked all-level recurrences within their stated ranges, exact external finite-level coefficient certificates, and numerical holdouts. It keeps these evidence categories separate and records the remaining formalization and structural questions.

For moments $p\in\{6,8,10\}$, let $\Delta_m^{(p)}(\theta)$ denote the trace defect between the specified SU(2)-connected operator and its commuting control at graph level $m$. The pinned source Lean project proves the H6/H8 all-angle recurrences from $m\geq3$, with exact external certificates for their finite $2\to3$ transitions; it proves the H10 all-angle recurrence for $m\geq4$ and its affine form for $m\geq5$. For H10, the level-five recurrence constant is $C_{10}^{(5)}=D_6-3D_5$. The finite traces at levels 5 and 6 are reconstructed from the pinned graph, orientation, flux, and SU(2) definitions by a sparse exact polynomial path expansion over three primes, followed by signed coefficient-wise CRT. The CRT product exceeds twice the proven coefficient bound, so the integer coefficients are uniquely recovered. This is an exact external certificate; the coefficient expansion itself is not a Lean-kernel theorem. Sparse-matrix-power calculations separately provide numerical holdouts through level 7 at five angles.

A separate, cross-project result now recorded in this synthesis archive proves the exact limit and finite-level remainder for a defined scalar invariant; its source proof is maintained in RFT-Cosmology-Genesis. This result is documented independently and is not presented as an all-level higher-moment recurrence or as a physical cosmological law.

A second research strand studies signed Z2-flux Laplacians and spectral decimation. Its exceptional-value criterion remains open, exploratory mass-index patterns are not established predictive laws, and no equivalence with the SU(2) operators is assumed. The remaining SU(2) tasks include Lean-kernel closure of the finite H6/H8 base transitions, optional Lean-kernel formalization of the exact external H10 coefficient reconstruction, and further path-class analysis. Any cross-model bridge still requires a precise mapping and proof.

**Keywords:** spectral graph theory; trace moments; Sierpinski graphs; SU(2) connections; Fourier coefficients; modular arithmetic; CRT; Lean; spectral decimation; reproducible computation.

## 1. Scope and central conclusion

The repository name “Theory of Everything” denotes a long-term research programme, not a claim that a universal theory has been completed. This document is a research dissertation/monograph, not a claim of award of an academic degree.

The strongest current milestone includes the pinned Lean proofs of the stated H6/H8 and H10 recurrence ranges, exact external finite base-transition certificates for H6/H8, and an exact source-reconstructed H10 level-five polynomial/Fourier coefficient obtained from the pinned graph/operator definitions by three-prime modular computation and signed CRT. The coefficient expansion is external to the Lean kernel. Reproducible numerical holdouts through level 7 at finite angles provide a separate evidence category. None establishes a universal cross-model theory.

The work has five goals:
1. State the trace-defect notation consistently.
2. Explain what the finite-level certificate proves and does not prove.
3. Document why modular arithmetic and CRT strengthen floating-point reconstruction.
4. Record numerical checks as finite evidence, not universal proof.
5. Define clear mathematical closure criteria.

## 2. Mathematical setting

Let $G_m$ be the finite graph at level $m$ in the specified Sierpiński-gasket approximation. Let $H_C(m,\theta)$ be the SU(2)-connected operator and $H_{C'}(m,\theta)$ the commuting control operator from the pinned source construction. Their exact definitions, boundary conventions, dimensions, and connection data are those of the upstream source and must not be silently changed.

For even $p$, define

$$
\Delta_m^{(p)}(\theta)=\mathrm{Tr}(H_C(m,\theta)^p)-\mathrm{Tr}(H_{C'}(m,\theta)^p).
$$

For $m \geq 2$, define the transition residual

$$
R_m^{(p)}(\theta)=\Delta_m^{(p)}(\theta)-3\Delta_{m-1}^{(p)}(\theta).
$$

The candidate recurrence is

$$
R_m^{(p)}(\theta)=C_p(\theta),\quad m\geq3,
$$

equivalently,

$$
\Delta_m^{(p)}(\theta)=3\Delta_{m-1}^{(p)}(\theta)+C_p(\theta),\quad m\geq3.
$$

The first transition, $R_2^{(p)}$, is treated separately from the later-transition candidate $R_4^{(p)}$. The coefficient is fixed from the level-3-to-4 transition and then used for prediction, not refitted at every level. Otherwise, defining $C_m=\Delta_m-3\Delta_{m-1}$ would make the recurrence true by definition and provide no evidence of level independence.

Set $\phi=\theta/2$. Since the source operator entries are linear in $\cos\phi$ and $\sin\phi$, products of $p$ entries have Fourier modes of order at most $p$. The 21 sample points are $\theta_j=\frac{4\pi j}{21}$ for $j=0,1,\ldots,20$, and are used for moments through $p=10$. The exact certificate uses finite-field transforms and a uniqueness argument rather than relying on floating-point interpolation alone.

## 3. Fourth-moment result

The upstream project [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) reports the identity

$$
\Delta_m(H^4,\theta)=-16(3^{m-1}+1)\sin^2(\theta/2),\quad m\geq1,
$$

for its specified operator definitions and hypotheses, with a Lean 4 formalization. The synthesis repository builds a pinned source revision with a pinned toolchain. The upstream definitions and hypotheses remain authoritative; this dissertation does not independently re-prove that result.

The fourth-moment theorem does not automatically imply a recurrence for $H^6$, $H^8$, or $H^{10}$. Higher moments contain additional operator products and possible cancellations, so they require their own derivations. The evidence boundary is therefore explicit:
- H^4: reported as formally proved upstream and checked by the pinned Lean build.
- H^6 and H^8: Lean recurrences for $m\ge3$, with exact external $2\to3$ base-transition certificates not yet formalized in Lean.
- H^10: unconditional Lean recurrence for $m\ge4$ and affine form for $m\ge5$. Its level-five correction is now reconstructed from the pinned finite graph/operator definitions by exact three-prime modular expansion and signed CRT. The coefficient expansion is an exact external certificate, not a Lean-kernel theorem.

## 4. Exact finite-level modular/CRT certificate

The verifier documented in [HIGHER_MOMENT_MODULAR_CERTIFICATE.md](computational/HIGHER_MOMENT_MODULAR_CERTIFICATE.md) certifies Fourier coefficients of R_2^(p) and R_4^(p), for $p\in\{6,8,10\}$. It repeats the computation over primes

$$
q\in\{10000453,20000569,30000769\}.
$$

Each prime is 1 modulo 84, providing roots needed for the 21-point transform and a square root of -1. The verifier builds the graph/operator data over each finite field, computes matrix-power traces modulo q, performs the transform, and compares scaled coefficients with the candidate integers.

Every operator entry has Fourier coefficients with denominator dividing 2. A product of p entries therefore has denominator dividing 2^p, so 2^p times each coefficient is integral under the stated construction. The certificate uses this denominator control to compare integer coefficients modulo the three primes.

The graph family has maximum vertex degree at most 4. The documented block estimates bound the diagonal block norm by 4 and the connection-adjacency norm by 4, giving $\|H\|\leq 8$. For dimension $2n_m$,

$$
|\mathrm{Tr}(H^p)|\leq 2n_m 8^p.
$$

These bounds induce bounds on the scaled Fourier coefficients. The product of the three primes exceeds twice the applicable coefficient bound. If the candidate and true coefficient agree modulo each prime, their difference is divisible by the CRT modulus; the size bound then forces the difference to be zero.

This certifies the specified finite-level coefficients under the graph/operator, mode, denominator, and norm assumptions checked by the verifier. It does not extend the level index to all m. It certifies:
- R_2 at the level-1-to-2 transition;
- R_4 at the level-3-to-4 transition;
- the finite-level correction R_2 - R_4;
for p = 6, 8, 10.

The exact coefficient tables and bounds are kept in the companion certificate report to avoid duplicating a second, potentially inconsistent transcription here.

### H10 source-reconstruction certificate

In addition to the earlier H6/H8 finite-transition certificates, the level-five H10 correction is now rebuilt directly from the pinned SU(2) graph/operator source. The C++17 engine mirrors the recursive graph edges, first-occurrence vertex order, face-flux edges, orientation-dependent matrix entries, and Pauli-axis rotations. It expands the length-ten trace sums modulo three primes, recovers all integer coefficients with signed CRT, verifies the row l1-norm and path-count coefficient bound, checks H4 source controls at levels 1–6, and reproduces the exact theta=pi endpoints. The modulus product exceeds twice the coefficient bound. The full result, commands, source pin, and evidence boundary are in [H10_EXACT_RESIDUAL_2026-11-23.md](computational/H10_EXACT_RESIDUAL_2026-11-23.md). This is an exact external certificate, not a Lean-kernel coefficient theorem.

## 5. Numerical validation

The repository includes:
- level-5 holdouts at 13 predeclared angles theta = k pi / 12;
- level-6 holdouts at 0, pi/2, pi;
- independent sparse-matrix-power predictions through level 7 at five angles;
- direct matrix-power versus eigenvalue-power comparisons on levels 1-4;
- 21-point floating-point Fourier reconstruction and seven off-grid checks;
- exact modular/CRT coefficient checks.

The sparse implementation reconstructs the graph and operator and computes traces through sparse matrix powers without using eigenspectra. It is an independent numerical route, not an independent mathematical definition: it still aims to implement the same operator family.

The recurrence note reports maximum relative residuals on the level-5 13-angle grid of approximately $1.47\times10^{-12}$ for $H^6$, $1.80\times10^{-12}$ for $H^8$, and $8.82\times10^{-13}$ for $H^{10}$. On the level-6 three-angle holdout, the reported maxima are approximately $9.28\times10^{-14}$, $6.74\times10^{-14}$, and $3.56\times10^{-14}$, respectively. The sparse level-7 report provides the exact angle set, tables, commands, and limitations.

These small residuals support the candidate but are not universal error bounds. A finite set of angles cannot establish an identity for all angles, and a finite set of graph levels cannot establish a statement for every level. Independent implementations reduce some shared-code risks but may still share mathematical assumptions and graph conventions.

## 6. The exceptional first transition

The certified finite-level formulas show that $R_2^{(p)}$ differs from $R_4^{(p)}$. The companion report factors the correction as

$$
R_2^{(p)}(\theta)-R_4^{(p)}(\theta)=\sin^2(\phi)Q_p(\phi),\quad \phi=\theta/2.
$$

For $p=6$, the reported quotient is $Q_6(\phi)=-24$; for $p=8$ and $p=10$ it contains additional trigonometric modes. The exact coefficients are recorded in [HIGHER_MOMENT_COEFFICIENT_CANDIDATES.md](computational/HIGHER_MOMENT_COEFFICIENT_CANDIDATES.md).

The factor implies that the correction vanishes at $\theta=0$ and $\theta=2\pi$. This is an algebraic property of the finite-level formulas, not yet a derivation from the recursive graph structure. Possible explanations involving new vertices, boundary/corner effects, newly available closed walks, or incomplete cancellation are hypotheses, not established results.

A satisfactory explanation must identify the operator terms or walk classes contributing to the correction, derive its trigonometric structure, explain why the contribution does not persist at later transitions, and prove the result for the specified graph/operator family. The exceptional case is a central mathematical clue and should not be hidden.

## 7. Separate signed-flux spectral-decimation programme

The second strand, [RFT-SIRM/Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis), studies signed Z2-flux Laplacians, spectral decimation, boundary/corner corrections, inertia calculations, and exploratory mass-index patterns.

Gate A remains open: simple exclusions of a small exceptional set have not produced complete matching, and the full exceptional set is not characterized. A hypothesis about recursively generated preimages must be derived and independently verified before it is treated as a theorem.

A fitted or selected mass-index pattern is not a predictive physical law without a stated selection mechanism, a prospective prediction protocol, and held-out validation. No equivalence between the SU(2)-connected operators and signed Z2-flux Laplacians is assumed. A bridge must specify both operator families, a map between them, boundary conditions and exceptional cases, preserved quantities, and a proof—or a falsifiable conjecture clearly labelled as such.

## 8. Reproducibility and formal verification

The repository distinguishes:
- **FORMALIZED:** machine-checked in a specified proof assistant and build configuration;
- **PROVED:** complete written proof with assumptions and quantifiers;
- **NUMERICALLY REPRODUCED:** rerunnable computation with code, parameters, and outputs;
- **OBSERVED:** reported pattern not fully scoped or independently reproduced;
- **CONJECTURE / OPEN:** unresolved;
- **NOT ESTABLISHED:** evidence does not warrant the stronger claim.

A reproducible computational record should identify commit SHA, command, runtime and dependencies, graph level and parameters, precision/tolerance, raw output, and known limitations. A passing workflow proves only the assertions it executes. The pinned Lean workflow builds the source library containing the stated H4, H6/H8, and H10 declarations; the H10 source-reconstruction workflow recompiles the C++ engine, reconstructs the finite level-five/six traces modulo three primes, applies signed CRT under an explicit coefficient bound, and compares the generated JSON with the committed artifact. That expansion is exact external evidence, not a Lean-kernel theorem.

Failed runs should remain in history as evidence tied to their original commit. A later successful run on a fixed commit does not rewrite the old result; both records have distinct meanings.

### Related exact scalar-invariant limit theorem

A separate formalized result concerns the scalar invariant

$$
I_m(\theta)
=-16\frac{3^{m-1}+1}{3^{m+1}+3}
\sin^2\!\left(\frac{\theta}{2}\right),
\qquad m\geq1.
$$

Its exact limit is

$$
I_\infty(\theta)
=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right).
$$

The exact finite-level remainder is

$$
I_m(\theta)-I_\infty(\theta)
=-\frac{32}{9(3^m+1)}
\sin^2\!\left(\frac{\theta}{2}\right).
$$

The full statement, algebraic derivation, Lean theorem names, source commit, and CI evidence are kept in [the exact invariant limit theorem dossier](theorems/exact_invariant_limit.md). The source proof is maintained separately in [RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis); it was merged in PR #3, and the post-merge Lean build passed.

This is recorded as a related formalized scalar result, not as evidence for the higher-moment theorem ranges beyond their stated assumptions, an observational CMB fit, a physical interaction, or an equivalence among the distinct operator models.
## 9. Limitations

1. **Finite levels:** the modular certificate covers specified transitions, not infinitely many levels.
2. **Finite angles:** numerical checks cover a finite set and do not prove a universal identity over the angle domain.
3. **Implementation dependence:** the certificate depends on the implemented graph/operator construction and its mode, denominator, and norm arguments.
4. **Shared assumptions:** independent numerical implementations can share the same mathematical or modelling mistake.
5. **Lean scope:** the pinned build compiles the source library containing the stated H4, H6/H8, and H10 declarations. The finite H6/H8 bridge certificates and the finite H10 coefficient expansion are exact external certificates, not Lean-kernel theorems.
6. **Cross-model gap:** the SU(2) and signed-flux models remain distinct until a precise bridge is proved.
7. **Licensing:** this repository's original material is under Apache-2.0 subject to its LICENSE and NOTICE; upstream projects remain separate works under their own terms. This document is not legal advice.

## 10. Research agenda and closure criteria

### Priority 1: close the remaining finite Lean bridges

The H6/H8 recurrences are Lean-proved for $m\ge3$, and their finite $2\to3$ transitions have exact external certificates. The next formalization target is to prove these two finite transition identities in Lean where maintainable. The H10 recurrence is Lean-proved for $m\ge4$, with affine form from $m\ge5$. Its finite level-five coefficient is now reconstructed exactly from the pinned graph/operator definitions by the external three-prime CRT engine; a kernel-level formalization of that finite computation remains optional future work.

### Priority 2: extend the path-class explanation

Extend the finite first-gasket H6 closed-walk cancellation classification to higher levels, or establish precisely where its cancellation pattern fails.

### Priority 3: formalize the proof

After the written derivation is complete, formalize its core lemmas and theorem in Lean where feasible, pin the toolchain, and retain regression tests. The formal statement must match the written assumptions, boundary conditions, and indexing.

### Priority 4: close or delimit Gate A

Derive a complete exceptional-value criterion for the signed-flux decimation mechanism. If it cannot be proved, retain the open status and report which cases match or fail.

### Priority 5: test mass-index selection prospectively

Fix the mechanism, exclusions, and predictions before examining held-out cases. Until a derived rule and held-out validation exist, the pattern remains exploratory.

### Priority 6: establish any cross-model bridge

Start with a precise map preserving one clearly defined quantity. Only broaden the unification claim after the narrower statement has been proved and checked against counterexamples.

### Mathematical closure checklist

The status of each higher moment must be stated with its own theorem range and evidence boundary:
1. H6/H8: Lean recurrence for every $m\ge3$, with the finite $2\to3$ transition currently supported by exact external certificates.
2. H10: Lean recurrence for every $m\ge4$ and affine form for every $m\ge5$; its level-five correction has an exact external source-reconstructed CRT certificate. The coefficient expansion is not a Lean-kernel theorem.
3. Do not present the exact external H10 coefficient expansion as a Lean-kernel theorem; preserve the distinction between source-reconstructed CRT evidence and formal proof.
4. Preserve the assumptions, parameter domain, orientation, graph indexing, and exceptional cases of the pinned source.
5. Keep regression tests and the claims ledger aligned with the source theorem and the external certificate.

The broader programme should be called unified only after a precise, proved bridge between the SU(2) and signed-flux models exists.

## 11. Conclusion

The current milestone is neither merely a numerical fit nor a completed universal theory. It comprises the pinned Lean recurrence results for H4, H6/H8, and H10 within their stated ranges; exact external finite base-transition certificates for H6/H8; an exact source-reconstructed H10 level-five polynomial/Fourier coefficient obtained by modular computation and signed CRT; and numerical holdouts through level 7 at finite angles. These components provide different forms of evidence and must remain distinct.

The modular/CRT calculations certify their stated finite-level coefficients under explicit arithmetic and norm bounds. The new H10 engine independently rebuilds the level-five and level-six operator traces from the pinned source definitions and recovers the exact integer coefficient expansion using a CRT modulus larger than twice the coefficient bound. This closes the finite H10 coefficient derivation as an exact external certificate, but not as a Lean-kernel theorem. The H6/H8 finite base-transition identities likewise remain external certificates. The structural explanation of path-class cancellation and the separate cross-model questions remain open.

The next steps are to formalize the H6/H8 finite base-transition certificates in Lean where feasible, extend the H6 path-class analysis, and continue the independent signed-flux questions. The signed-flux questions should remain separate until their exceptional cases are resolved and a precise bridge is proved. A defensible scientific record states both what has been established and what remains unknown.

## Appendix A. Reproduction commands

Run from a clean checkout at the commit being evaluated.

~~~sh
python -m pip install "numpy>=1.24,<3" "scipy>=1.10,<2"
python computational/verify_higher_moment_coefficients_modular.py --output artifacts/higher_moment_modular_certificate.json
python -m computational.h10_level5_residual_certificate --output artifacts/h10_level5_residual_certificate.json
python -m unittest computational.test_h10_level5_residual_certificate -v
~~~

This verifies the finite-level Fourier coefficients within the verifier's stated assumptions and bounds. It does not prove the all-level recurrence.

~~~sh
python -m pip install "numpy>=1.24,<3" "scipy>=1.10,<2"
python computational/independent_sparse_level7.py --output artifacts/independent_sparse_level7.json
~~~

This checks finite predictions through level 7 at the stated angles; it is a numerical holdout, not a proof.

~~~sh
python scripts/check_docs.py
~~~

This checks repository structure and provenance references, not mathematical validity. Use the pinned Lean workflow for the source Lean library. The H10 verifier recompiles the source-mirroring C++ engine, reconstructs the level-five/six traces modulo three primes, applies signed coefficient-wise CRT under an explicit bound, and verifies the generated JSON against the committed artifact. The resulting coefficient expansion is an exact external certificate, not a Lean-kernel theorem.

## Appendix B. Claim-status table

| Statement | Status | Evidence boundary |
|---|---|---|
| Fourth-moment trace-defect formula | Reported FORMALIZED upstream | Applies to source definitions and assumptions; pinned Lean build |
| Exact limit and finite-level remainder of the defined scalar invariant | FORMALIZED in separate Lean source project | rftInvariant_tendsto, rftInvariant_remainder, and rftInvariant_exact_decomposition in RFT-Cosmology-Genesis; post-merge Lean CI passed. No physical-law claim follows |
| R_2^(p) coefficients for p = 6, 8, 10 | Exact finite-level certificate | First transition only |
| R_4^(p) coefficients for p = 6, 8, 10 | Exact finite-level certificate | Level-3-to-4 transition only |
| Predictions through level 7 at five angles | Numerically reproduced | Finite sparse-matrix-power holdout |
| H6/H8 recurrence for m >= 3 | LEAN-CHECKED | Their finite 2-to-3 transitions are exact external certificates, not yet Lean-kernel theorems |
| H10 recurrence for m >= 4 and affine form for m >= 5 | LEAN-CHECKED | Radius-four transport and recurrence are proved in the pinned Lean source |
| H10 level-five recurrence constant | EXACT EXTERNAL SOURCE-RECONSTRUCTED CRT CERTIFICATE | Direct finite graph/operator reconstruction at levels 5 and 6; three-prime modular expansion and signed CRT under an explicit coefficient bound; not a Lean-kernel coefficient theorem |
| Structural explanation of 1→2 exception | Open | Correction is certified; recursive cause is not derived |
| Complete Gate A exceptional-value criterion | Open / not established | Existing diagnostic does not close all cases |
| Predictive mass-index law | Not established | Needs a derived mechanism and prospective held-out tests |
| Equivalence of SU(2) and signed Z2-flux operators | Open | Needs precise map and proof of preserved quantities |

## References and research artifacts

1. RFT-SIRM/Evgeny-Theorem, upstream source for the specified SU(2)-connected Sierpiński-gasket operators and reported fourth-moment Lean formalization: https://github.com/RFT-SIRM/Evgeny-Theorem
2. RFT-SIRM/Phi-Genesis, separate research programme on signed Z2-flux Laplacians, spectral decimation, inertia, and exploratory mass-index patterns: https://github.com/RFT-SIRM/Phi-Genesis
3. Exact finite-level modular/CRT certificate: https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_MODULAR_CERTIFICATE.md
4. Higher-moment recurrence evidence: https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_RECURRENCE_NOTE.md
5. Independent sparse level-7 holdout: https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_SPARSE_LEVEL7.md
6. Fourier coefficient candidates and exceptional transition: https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_COEFFICIENT_CANDIDATES.md
7. Claims and evidence ledger: https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/CLAIMS_AND_EVIDENCE.md
8. Reproducibility protocol: https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/REPRODUCIBILITY.md

The Git history and machine-readable artifacts form part of the provenance record. Readers should record the exact commit SHA associated with any reproduced result.
