# Recursive Graph Operators, Spectral Trace Defects, and Higher-Moment Recurrence

## Research dissertation

**Author:** Evgeny Zaprudnov  
**Research group:** RFT-SIRM  
**Version:** 1.0  
**Date:** 15 October 2026

## Abstract

This dissertation consolidates a research programme concerning trace defects of recursively constructed graph operators, focusing on Sierpinski-gasket approximations, SU(2)-connected operators, higher even trace moments, and a separate programme on signed Z2-flux Laplacians and spectral decimation. It distinguishes four kinds of claims: an upstream fourth-moment result reported as Lean-formalized; exact finite-level Fourier-coefficient certificates for selected higher-moment residuals; numerical recurrence checks at finitely many levels and angles; and universal recurrence statements that remain conjectural.

For moments $p\in\{6,8,10\}$, let $\Delta_m^{(p)}(\theta)$ denote the trace defect between the specified SU(2)-connected operator and its commuting control at graph level $m$. Define the residual by $R_m^{(p)}(\theta)=\Delta_m^{(p)}(\theta)-3\Delta_{m-1}^{(p)}(\theta)$. The candidate recurrence asserts that $R_m^{(p)}(\theta)$ is independent of $m$ for $m\geq3$, while the first transition $m=2$ is exceptional. A modular calculation over three finite fields, together with Fourier-mode and denominator bounds, an operator-norm estimate, and a Chinese-remainder-theorem uniqueness argument, certifies the stated Fourier coefficients of $R_2^{(p)}$ and $R_4^{(p)}$ for these moments. Independent sparse-matrix-power calculations check predictions through level 7 at five angles. These results are finite-level evidence; they do not establish the all-level recurrence.

A second research strand studies signed Z2-flux Laplacians and spectral decimation. Its exceptional-value criterion remains open, exploratory mass-index patterns are not established predictive laws, and no equivalence with the SU(2) operators is assumed. The dissertation concludes with a proof-oriented agenda: derive the recurrence from graph/operator recursion, explain the exceptional base transition, formalize the all-level result where feasible, and establish any cross-model bridge only after defining and proving a precise mapping.

**Keywords:** spectral graph theory; trace moments; Sierpinski graphs; SU(2) connections; Fourier coefficients; modular arithmetic; CRT; Lean; spectral decimation; reproducible computation.

## 1. Scope and central conclusion

The repository name “Theory of Everything” denotes a long-term research programme, not a claim that a universal theory has been completed. This document is a research dissertation/monograph, not a claim of award of an academic degree.

The strongest current milestone is: exact finite-level Fourier coefficients, reproducible numerical predictions through level 7 at a finite set of angles, and a pinned Lean build for an upstream fourth-moment result. The all-level higher-moment recurrence remains open. A passing workflow validates only the assertions it actually executes.

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
- H^6, H^8, H^10: exact finite-level coefficient certificates and numerical recurrence evidence.
- The all-level higher-moment recurrence: open.

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

A reproducible computational record should identify commit SHA, command, runtime and dependencies, graph level and parameters, precision/tolerance, raw output, and known limitations. A passing workflow proves only the assertions it executes. The pinned Lean build concerns the upstream fourth-moment formalization, not the higher-moment recurrence.

Failed runs should remain in history as evidence tied to their original commit. A later successful run on a fixed commit does not rewrite the old result; both records have distinct meanings.

## 9. Limitations

1. **Finite levels:** the modular certificate covers specified transitions, not infinitely many levels.
2. **Finite angles:** numerical checks cover a finite set and do not prove a universal identity over the angle domain.
3. **Implementation dependence:** the certificate depends on the implemented graph/operator construction and its mode, denominator, and norm arguments.
4. **Shared assumptions:** independent numerical implementations can share the same mathematical or modelling mistake.
5. **Lean scope:** the build covers the pinned upstream fourth-moment result only.
6. **Cross-model gap:** the SU(2) and signed-flux models remain distinct until a precise bridge is proved.
7. **Licensing:** this repository's original material is under Apache-2.0 subject to its LICENSE and NOTICE; upstream projects remain separate works under their own terms. This document is not legal advice.

## 10. Research agenda and closure criteria

### Priority 1: prove the all-level recurrence

Prove $R_m^{(p)}(\theta)=R_4^{(p)}(\theta)$ for every $m\geq3$, $p\in\{6,8,10\}$, and every stated admissible angle. Candidate approaches include closed-walk expansions, block-operator recursion, cancellation of connection-dependent path classes, and representation-theoretic identities. These are research directions, not established results.

### Priority 2: derive the base correction

Explain R_2 - R_4 from the recursive construction, including the factorization and the reason the correction is absent at later transitions.

### Priority 3: formalize the proof

After the written derivation is complete, formalize its core lemmas and theorem in Lean where feasible, pin the toolchain, and retain regression tests. The formal statement must match the written assumptions, boundary conditions, and indexing.

### Priority 4: close or delimit Gate A

Derive a complete exceptional-value criterion for the signed-flux decimation mechanism. If it cannot be proved, retain the open status and report which cases match or fail.

### Priority 5: test mass-index selection prospectively

Fix the mechanism, exclusions, and predictions before examining held-out cases. Until a derived rule and held-out validation exist, the pattern remains exploratory.

### Priority 6: establish any cross-model bridge

Start with a precise map preserving one clearly defined quantity. Only broaden the unification claim after the narrower statement has been proved and checked against counterexamples.

### Mathematical closure checklist

The higher-moment recurrence should be called proved only when:
1. a complete derivation from recursive graph/operator structure is available;
2. the same coefficient is proved for every m >= 3 and the base transition is handled separately;
3. hypotheses, parameter domain, and exceptions are explicit;
4. intermediate identities agree with the finite-level certificate;
5. a machine-checked proof is supplied where feasible, without unverified placeholders;
6. the claims ledger and documentation are updated to match the theorem.

The broader programme should be called unified only after a precise, proved bridge between the SU(2) and signed-flux models exists.

## 11. Conclusion

The current milestone is neither merely a numerical fit nor a completed universal theorem. It comprises exact finite-level Fourier-coefficient certificates, numerical predictions checked through level 7 at a finite set of angles, and a pinned Lean build for an upstream fourth-moment result. These components provide different forms of evidence and must remain distinct.

The modular/CRT calculation replaces approximate coefficient recovery with an exact finite-level statement under explicit arithmetic and norm bounds. The sparse-matrix-power holdout adds a separate numerical route. The first-transition correction gives a precise target for structural explanation. Yet the central question—whether the later residual is independent of every level and every admissible angle—remains open.

The next step is mathematical, not cosmetic: derive the all-level recurrence, explain the exceptional base transition, and formalize the result where feasible. The signed-flux questions should remain separate until their exceptional cases are resolved and a precise bridge is proved. A defensible scientific record states both what has been established and what remains unknown.

## Appendix A. Reproduction commands

Run from a clean checkout at the commit being evaluated.

~~~sh
python -m pip install "numpy>=1.24,<3" "scipy>=1.10,<2"
python computational/verify_higher_moment_coefficients_modular.py --output artifacts/higher_moment_modular_certificate.json
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

This checks repository structure and provenance references, not mathematical validity. Use the pinned Lean workflow for the upstream fourth-moment formalization only.

## Appendix B. Claim-status table

| Statement | Status | Evidence boundary |
|---|---|---|
| Fourth-moment trace-defect formula | Reported FORMALIZED upstream | Applies to source definitions and assumptions; pinned Lean build |
| R_2^(p) coefficients for p = 6, 8, 10 | Exact finite-level certificate | First transition only |
| R_4^(p) coefficients for p = 6, 8, 10 | Exact finite-level certificate | Level-3-to-4 transition only |
| Predictions through level 7 at five angles | Numerically reproduced | Finite sparse-matrix-power holdout |
| R_m^(p) = R_4^(p) for all m >= 3 and all stated angles | Open conjecture | Requires structural all-level proof |
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
