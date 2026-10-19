# Higher-moment recurrence: structural proof obligations

**Purpose:** turn the numerical conjecture into a finite, auditable list of mathematical obligations. This is a research plan, not a proof of the all-level recurrence.

Related records:
- [Recurrence evidence and status](HIGHER_MOMENT_RECURRENCE_NOTE.md)
- [Finite-level modular/CRT certificate](HIGHER_MOMENT_MODULAR_CERTIFICATE.md)
- [Claims and evidence ledger](../CLAIMS_AND_EVIDENCE.md)
- [Lean source repository](https://github.com/RFT-SIRM/Evgeny-Theorem)

## 1. Keep the indices separate

For $p\in\{6,8,10\}$, let
\[
\Delta_m^{(p)}(\theta)=\operatorname{Tr}(H_C(m,\theta)^p)
-\operatorname{Tr}(H_{C'}(m,\theta)^p),\qquad
R_m^{(p)}=\Delta_m^{(p)}-3\Delta_{m-1}^{(p)}.
\]
Here $p$ is the moment power, while the subscript in $R_m^{(p)}$ is the graph-level transition. Thus $R_4^{(10)}$ means the degree-10 residual for the transition $3\to4$; it is not the fourth-moment theorem.

The conjecture under investigation is
\[
R_m^{(p)}(\theta)=R_4^{(p)}(\theta)\quad
\text{for every }m\ge3.
\]
The exact finite-level certificate establishes the Fourier coefficients of $R_2^{(p)}$ and $R_4^{(p)}$, but does not establish this quantified statement.

## 2. Exact base-transition correction at \(\theta=\pi\)

Evaluating the certified candidate Fourier coefficients at \(\theta=\pi\) gives:

| Power $p$ | $R_2^{(p)}(\pi)$ | $R_4^{(p)}(\pi)$ | $R_4^{(p)}(\pi)-R_2^{(p)}(\pi)$ |
|---:|---:|---:|---:|
| 6 | 5,256 | 5,280 | 24 |
| 8 | 268,960 | 277,504 | 8,544 |
| 10 | 4,006,040 | 4,507,520 | 501,480 |

These are exact evaluations of the integer Fourier candidates in the modular certificate, not new floating-point matrix computations. They confirm that the first transition cannot be folded into the same constant as the $3\to4$ transition. They do not identify the structural cause of the exception.

## 3. Algebraic lemma needed for a higher-power gluing proof

The fourth-moment Lean development represents the glued operator using a block-diagonal operator $K_m$ on three copies and a gluing matrix $N$, with
\[
\operatorname{Tr}(H_{m+1}^{p})=
\operatorname{Tr}((K_m+K_mN)^p).
\]
For (p>4), the proof must expand all words, not extrapolate the fourth-power formula by changing the exponent.

A useful trace identity, for finite square matrices (K,N), is
\[
\operatorname{Tr}((K+KN)^p)=\operatorname{Tr}(K^p)+
\sum_{r=1}^{p}\frac{p}{r}
\sum_{\substack{a_1+\cdots+a_r=p\\a_i\ge1}}
\operatorname{Tr}(K^{a_1}N K^{a_2}N\cdots K^{a_r}N).
\]
The inner sum runs over ordered compositions of (p). The factor (p/r) accounts for cyclic rotations of the (r) gluing transitions. A formal proof should establish this identity independently of the graph-specific hypotheses.

The graph-specific lemma must then show which terms vanish and which terms depend only on corner data. Matrix blocks are (2\times2) spin matrices; they must not be treated as scalars until commutation or scalarity is proved.

## 4. Distance cutoff and the special $H^{10}$ bridge

A matrix power $K_m^a$ has zero $(u,v)$-block whenever the graph distance between $u$ and $v$ exceeds $a$. Distinct outer corners of the level-$m$ Sierpiński graph are at distance $2^m$.

In a nontrivial term of the expansion above, there are $r\ge1$ factors $N$, so each exponent $a_i\le p-r\le p-1\le9$. Consequently, for $p\le10$ and $m\ge4$,
\[
2^m\ge16>9\ge a_i,
\]
and all off-diagonal corner-to-corner blocks $K_m^{a_i}$ vanish. This gives a precise locality cutoff for the gluing expansion from level 4 onward, subject to the exact support properties of the implemented $K_m,N$.

The transition $3\to4$ is exceptional for the generic argument at $p=10$: level 3 has corner distance $2^3=8$, so an off-diagonal block of $K_3^8$ is not ruled out by distance alone. Therefore, a proof for $H^{10}$ cannot simply apply the $m\ge4$ cutoff to the $3\to4$ transition. A separate exact bridge is needed.

The cutoff does not itself prove recurrence. It only removes cross-corner terms in the higher-power gluing expansion.

## 5. Corner moments reduce to a finite local problem

For a closed walk of length $j$ beginning and ending at a corner, the maximum graph distance reached is at most \(\lfloor j/2\rfloor\). Thus diagonal corner blocks of powers $K_m^j$, for $j\le9$, depend only on the rooted, labelled radius-4 neighbourhood of that corner, including degrees, edge labels, and connection blocks.

This yields a clean target lemma:

> **All-level corner-locality lemma (open).** For every $m\ge4$, the rooted, labelled radius-4 neighbourhood at each designated corner of the level-$m$ graph is isomorphic to the corresponding neighbourhood in the reference level, with the operator labels and corner roles preserved.

From that lemma, a second open lemma must prove that the diagonal corner blocks of (K_m^j) are invariant under the rooted labelled isomorphism for all $j\le9$. The proof must include the onsite degree terms and the $2\times2$ connection blocks.

For $p=6,8$, the distance cutoff also applies at the $3\to4$ step because $2^3=8>p-1$. For $p=10$, the separate finite bridge described above is needed before the cutoff-based induction can start.

## 6. Proof dependency graph

1. **Generic matrix identity:** prove the composition-sum trace expansion for all $p\le10$.
2. **Support lemma:** formalize the distance bound for powers of the block operator and identify exactly which corner terms survive.
3. **Local geometry lemma:** prove the all-level rooted, labelled radius-4 corner-neighbourhood isomorphism.
4. **Corner-moment lemma:** deduce equality of diagonal corner blocks through order 9, preserving spin-matrix structure.
5. **Higher-power gluing lemma:** express each transition residual in terms of those corner blocks and derive its level-independent value for $m\ge4$.
6. **Base bridge:** establish $R_3^{(p)}=R_4^{(p)}$ for $p=6,8$, and establish $R_4^{(10)}=R_5^{(10)}$ for $p=10$, exactly. The existing certificate covers $R_4$ itself, not this missing equality.
7. **Induction and formalization:** combine the bridge and the $m\ge4$ recurrence, then formalize the resulting theorem in Lean.

Each item is a separate proof obligation. Numerical agreement at finitely many levels does not discharge any all-level obligation.

## 7. Diagnostic experiment completed: corner powers through order 9

The diagnostic script [diagnose_corner_moments.py](diagnose_corner_moments.py) computes the $2\times2$ corner blocks of $H_m^j$, $j=1,\ldots,9$, using the operator builder in [independent_sparse_level7.py](independent_sparse_level7.py). The compact machine-readable results are in [corner_moment_diagnostic_summary.json](data/corner_moment_diagnostic_summary.json).

Tested levels were $m=3,4,5,6$, with vertex counts $42,123,366,1095$. Diagonal corner-block invariance was checked at ten angles: $\pi/2$, $\pi$, $0.73$, $0.137$, $0.51$, $1.23$, $1.87$, $2.41$, $2.7$, and $3.03$ radians. Off-diagonal block magnitudes are fully summarized for the first three angles in the JSON artifact. Both the noncommuting SU(2) operator and commuting control were checked.

### Observations

- For each tested angle and each model, all diagonal corner blocks $(H_m^j)_{cc}$ agreed across levels 3, 4, 5, and 6 for every $j=1,\ldots,9$. The maximum absolute difference in the computed arrays was $0$.
- On level 3, off-diagonal corner blocks vanished for powers $j=1,\ldots,7$ and became nonzero at $j=8$.
- At $j=8$, the maximum absolute matrix entry was approximately $1$ for both models at the three fully reported angles. At $j=9$, these blocks were also nonzero and had maximum entry magnitudes between about $20.8$ and $34.2$ in those three cases, depending on angle and model.

### What this establishes—and what it does not

This is reproducible numerical evidence that the diagonal corner moments through order 9 are level-independent across the tested levels and angles, and it confirms the distance-8 obstruction for the degree-10 gluing argument. It is consistent with a finite-radius corner-locality lemma.

It is **not** an all-level proof. The data concern the full operator $H_m$ generated by the current sparse implementation; they do not themselves prove that every labelled radius-4 neighbourhood is isomorphic for all levels, nor that the gluing identity in the Lean development has exactly the required block support. The next proof task is to establish the rooted labelled neighbourhood isomorphism and then derive equality of corner moments symbolically. For $p=10$, the nonzero level-3 off-diagonal blocks at orders 8 and 9 mean the $3\to4$ transition needs a separate exact treatment; the locality cutoff only applies once the corner distance exceeds 9.

The script should be run with the repository's documented NumPy/SciPy environment. Its output is a diagnostic, not a certificate of the all-level recurrence.

## 8. Expansion-size audit

The composition expansion has $\binom{p-1}{r-1}$ ordered compositions for each number $r$ of gluing transitions. Summing over $r$ gives $2^{p-1}$ composition terms before using graph-specific zero terms. The number of terms in the original distributive expansion with at least one gluing factor is $2^p-1$.

| Power $p$ | Composition terms $2^{p-1}$ | Binary words with at least one gluing factor $2^p-1$ |
|---:|---:|---:|
| 6 | 32 | 63 |
| 8 | 128 | 255 |
| 10 | 512 | 1,023 |

A numerical sanity check with generic noncommuting $3\times3$ matrices confirmed the stated composition identity for $p=1,\ldots,7$ to floating-point roundoff (absolute discrepancies from about $10^{-15}$ to $10^{-11}$ in that test). This is a consistency check only; it is not the symbolic proof required for Lean. The count shows why a direct term-by-term expansion for $p=10$ should be automated or factored into reusable lemmas rather than maintained manually.


## 9. Repeated verification and correction log

The first version of `diagnose_corner_moments.py` incorrectly expected `operator()` to return the graph coordinates as well as the matrix. This was caught during source-level reinspection before treating the output as validated. The script was corrected to obtain coordinates from the graph constructor separately (commit `5c49f0f`), and the finite-level calculation was rerun in the analysis environment. The updated [JSON report](data/corner_moment_diagnostic_summary.json) now explicitly records the correction and its caveat.

Separately, [audit_trace_composition_exact.py](audit_trace_composition_exact.py) and [its exact output](data/trace_composition_exact_audit.json) check the trace-composition identity using exact rational arithmetic for a concrete noncommuting pair of $3\times3$ matrices, for powers $p=1,\ldots,7$. Every exact difference is zero. This is stronger than a floating-point check of that example, but remains a single-instance verification, not a proof for arbitrary matrices or $p\le10$.

Before promoting any diagnostic to a theorem, the remaining independent checks are:
1. run both committed scripts in the repository's documented Python environment;
2. compare their output to the committed JSON artifacts;
3. add CI coverage for the scripts and artifact consistency;
4. prove the generic composition identity symbolically and the corner-locality statement for arbitrary levels.


## 10. Trace-composition identity closed at the paper-proof level

The general cyclic trace-counting argument is now written out in [TRACE_COMPOSITION_IDENTITY_PROOF.md](TRACE_COMPOSITION_IDENTITY_PROOF.md). It proves the factor $p/r$ by double-counting pairs consisting of a cyclic word with $r$ selected $KN$ factors and a distinguished selected position. This proof requires only distributivity and cyclicity of trace; it does not assume that $K$ and $N$ commute.

The exact rational-matrix audit was extended from powers $1\ldots7$ to $1\ldots10$. For the fixed noncommuting $3\times3$ test matrices, the exact trace values agree at every power through 10; the exact differences are zero. See [the updated audit script](audit_trace_composition_exact.py) and [stored results](data/trace_composition_exact_audit.json).

A GitHub Actions workflow, [higher-moment-diagnostics.yml](../.github/workflows/higher-moment-diagnostics.yml), now runs the corner diagnostic and exact algebra audit, checks key invariants and compares generated exact results against the committed JSON. Its existence is confirmed; a successful Actions run still must be observed before describing the workflow as green.

### Remaining proof boundary

This closes the general trace-counting derivation on paper, but it does **not** close the research theorem. The remaining difficult obligations are the graph-specific block decomposition, the all-level corner-neighbourhood argument, and the exceptional degree-10 transition where level-3 cross-corner terms occur at powers 8 and 9.
