# H12 degree-12 boundary word expansion — exact combinatorial reduction

Date: 23 November 2026

## 1. Algebraic expansion

The gluing architecture recorded in `LEAN_GLUE_EXTENSION_PLAN.md` writes the
parent operator in the form \(K+KN=K(I+N)\), with \(N\) supported on the
finite gluing-boundary subspace. For any positive integer \(p\), cyclicity of
trace gives the noncommutative identity

\[
\operatorname{Tr}((K+KN)^p)-\operatorname{Tr}(K^p)
=
\sum_{r=1}^{p}\frac{p}{r}
\sum_{\substack{a_1+\cdots+a_r=p\\a_i\ge1}}
\operatorname{Tr}(K^{a_1}N\cdots K^{a_r}N).
\]

No commutation of \(K\) and \(N\) is used. The coefficient \(p/r\) is the
cyclic-word multiplicity: a word with \(r\) selected \(N\)-positions is
counted once for each choice of a distinguished selected position, while
there are \(p\) possible cyclic starting positions.

For \(p=12\), this gives exactly \(2^{11}=2048\) ordered-composition terms.
The coefficient for a term with \(r\) occurrences of \(N\) is \(12/r\).
The sum of all these rational weights is exactly \(4095\).

Because \(N\) is supported on the boundary subspace \(\mathcal B\), put
\(P_{\mathcal B}\) for its projection, \(N_{\mathcal B}=P_{\mathcal B}NP_{\mathcal B}\),
and
\[
A_m^{(j)}=P_{\mathcal B}K_m^jP_{\mathcal B}.
\]
Then every term is a trace on the fixed boundary space:
\[
\operatorname{Tr}(K_m^{a_1}N\cdots K_m^{a_r}N)
=
\operatorname{Tr}_{\mathcal B}
\left(A_m^{(a_1)}N_{\mathcal B}\cdots
      A_m^{(a_r)}N_{\mathcal B}\right).
\]
This is the full degree-12 boundary-word expansion before applying the
graph-specific zero-block and pairing relations. It keeps the spin blocks
\(2\times2\) and does not commute their products.

## 2. Exact distance cutoff

A factor \(K_m^j\) can connect two distinct outer corners only if
\(j\ge 2^m\), because their graph distance is \(2^m\). Every exponent in a
nontrivial composition of 12 is at most 11.

- At level 3 the corner distance is 8. A composition can therefore contain a
  potentially off-diagonal corner factor exactly when at least one part
  \(a_i\ge8\).
- At level 4 and above the corner distance is at least 16, so no exponent
  \(a_i\le11\) can produce an off-diagonal corner block.

The executable inventory in `h12_boundary_word_expansion.py` gives:

| Number \(r\) of \(N\)'s | All compositions | Potentially off-diagonal at level 3 |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 11 | 8 |
| 3 | 55 | 18 |
| 4 | 165 | 16 |
| 5 | 330 | 5 |
| 6 | 462 | 0 |
| 7 | 462 | 0 |
| 8 | 330 | 0 |
| 9 | 165 | 0 |
| 10 | 55 | 0 |
| 11 | 11 | 0 |
| 12 | 1 | 0 |
| **Total** | **2048** | **48** |

Thus 2,000 of the 2,048 words are diagonal-corner-only already at the
exceptional \(3\to4\) transition. Exactly 48 words (24 with odd \(r\), 24
with even \(r\)) require retaining possible cross-corner blocks at level 3.
Their aggregate cyclic weight is exactly 192.

For every transition \(m\to m+1\) with \(m\ge4\), all 2,048 words use only
diagonal corner blocks \(A_m^{(j)}\), \(1\le j\le11\). Equivalently,
\(A_m^{(j)}\) is block diagonal by boundary corner, with one \(2\times2\)
spin block per corner.

## 3. Reduction to a fixed finite boundary problem

For \(m\ge4\), the boundary formula is therefore
\[
C_{12}^{(m)}
=
\sum_{r=1}^{12}\frac{12}{r}
\sum_{\substack{a_1+\cdots+a_r=12\\a_i\ge1}}
\operatorname{Tr}_{\mathcal B}
\left(A_m^{(a_1)}N_{\mathcal B}\cdots
      A_m^{(a_r)}N_{\mathcal B}\right),
\]
where each \(A_m^{(j)}\) is assembled solely from diagonal \(2\times2\)
corner moments. This is a fixed-size expression independent of the number of
interior graph vertices.

The radius-to-moment locality lemma gives the exact cutoff
\(j\le2R+1\). Setting \(R=5\) covers all powers \(j\le11\). Consequently,
once the rooted radius-five operator-labelled corner neighborhoods are shown
to be level-independent (including the directed connection blocks and any
required consistent corner gauge), every \(A_m^{(j)}\) in this expression is
level-independent. Since \(N_{\mathcal B}\) is the fixed gluing matrix, the
right-hand side is then independent of \(m\ge4\). That is the structural
mechanism needed for the all-level H12 recurrence from level 4 onward.

## 4. Exact remaining tasks

This calculation closes the **word enumeration and distance classification**;
it does not yet claim the complete graph-specific boundary contraction or a
Lean theorem. The next obligations are now finite and explicit:

1. Bind the boundary projection and the exact \(N_{\mathcal B}\) blocks to the
   existing `GlueData`/`G.N` definitions, verifying the support and pairing
   identities rather than assuming them.
2. Reduce the 2,048 displayed words with those exact \(N_{\mathcal B}\)
   identities. In particular, do not discard odd-\(r\) terms until the
   involutive pairing property has been established.
3. Prove the radius-five operator-labelled corner transport for every
   \(m\ge4\), preserving the \(2\times2\) blocks (or a consistent gauge).
4. Use the existing exact external CRT bridge \(C_{12}^{(3)}=C_{12}^{(4)}\)
   for the exceptional first transition, then combine it with the generic
   \(m\ge4\) boundary identity.
5. Formalize the reusable composition identity, the boundary contraction,
   and the radius-five transport in the formal proof project only when
   explicitly scheduled; this update does not modify that repository.

The level-8 CRT certificate remains finite external evidence. This report does
not promote it to an all-level theorem or a Lean-kernel result.

## Reproduction

From the synthesis repository root:

```sh
python3 -m computational.h12_boundary_word_expansion \
  --output computational/data/h12_boundary_word_expansion.json
python3 -m unittest computational.test_h12_boundary_word_expansion -v
```
