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

## 7. Immediate next computational experiment

Before writing a Lean generalization, generate a machine-readable table of the diagonal corner blocks
\[
(K_m^j)_{cc},\quad j=1,\ldots,9,
\]
for the three corner roles, at levels (m=3,4,5,6) and several angles. Separately record the off-diagonal corner blocks ((K_3^8)_{cd}) for (c\ne d). This experiment can:
- identify which corner powers actually vary with level or angle;
- test the radius-4 locality claim against the implementation;
- quantify the exceptional $H^{10}$ bridge;
- supply small, focused examples for Lean lemmas.

The output must include the source revision, graph construction, angles, matrix convention, and exact/numerical precision. It should be labeled a diagnostic, not a proof. The all-level theorem remains open until the geometry and matrix identities are proved for arbitrary levels.
