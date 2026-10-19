# Trace-composition identity: combinatorial proof

**Status:** a paper-level proof of the trace expansion below, subject to the usual cyclicity of matrix trace. The attached SymPy audit is a separate exact finite-instance check, not the proof itself.

## Statement

Let $K,N$ be square matrices over a commutative field of characteristic zero (or over a commutative ring in which the denominators $1,ldots,p$ are invertible). For every integer $p\ge1$,

$$
\operatorname{Tr}((K+KN)^p)
=
\operatorname{Tr}(K^p)
+
\sum_{r=1}^{p}\frac{p}{r}
\sum_{\substack{a_1+\cdots+a_r=p\\a_i\ge1}}
\operatorname{Tr}(K^{a_1}N\cdots K^{a_r}N).
$$

No commutativity assumption on $K$ and $N$ is made.

## Proof by cyclic word counting

Distribute the $p$ factors in $(K+KN)^p$. Each term is specified by a subset $S\subseteq\{1,\ldots,p\}$: positions in $S$ contribute $KN$, and all other positions contribute $K$. The empty subset contributes $\operatorname{Tr}(K^p)$.

Fix $r\ge1$ and consider all subsets with $|S|=r$. Read the selected positions cyclically around the trace word. If the successive selected positions have cyclic gaps $a_1,\ldots,a_r$, then each $a_i$ is a positive integer and $a_1+\cdots+a_r=p$. By cyclicity of trace, the corresponding term has trace

$$
\operatorname{Tr}(K^{a_1}N K^{a_2}N\cdots K^{a_r}N),
$$

up to cyclic rotation of the displayed factors.

Now count pairs consisting of a subset $S$ of size $r$ and a distinguished selected position in $S$. Every such subset is counted exactly $r$ times. Alternatively, choose the distinguished position as a starting location among the $p$ cyclic positions and then choose the ordered positive composition $(a_1,\ldots,a_r)$ of $p$. This counts the same pairs: there are $p$ choices of starting location for every ordered composition.

Cyclicity of trace means that rotating the chosen starting selected position does not change the trace contribution of the original subset. Therefore, if $T_r$ is the sum of trace contributions over all subsets of size $r$, and $C_r$ is the sum over all ordered positive compositions of $p$ into $r$ parts, the double count gives

$$
r T_r=p C_r,
\qquad
T_r=\frac{p}{r}C_r.
$$

Summing this equality over $r=1,\ldots,p$ and adding the empty-subset term proves the identity. $\square$

## Expansion-size check

There are $\binom{p-1}{r-1}$ ordered positive compositions of $p$ into $r$ parts. Hence

$$
\sum_{r=1}^{p}\binom{p-1}{r-1}=2^{p-1}
$$

composition terms appear across all $r$, before applying any graph-specific zero identities. The number of nonempty subsets in the original distributive expansion is $2^p-1$.

| $p$ | Composition terms | Nonempty distributive terms |
|---:|---:|---:|
| 6 | 32 | 63 |
| 8 | 128 | 255 |
| 10 | 512 | 1,023 |

## Exact computational cross-check

The script [audit_trace_composition_exact.py](audit_trace_composition_exact.py) checks this identity by exact rational/integer arithmetic on one concrete noncommuting pair of $3\times3$ matrices for every $p=1,\ldots,10$. The stored results are in [trace_composition_exact_audit.json](data/trace_composition_exact_audit.json); the difference is exactly zero in all ten cases.

This finite check is independent corroboration of the implementation, not a replacement for the proof above and not a proof of the higher-moment recurrence. The identity's use in the research project still requires careful matching of the abstract $K,N$ to the actual block decomposition and proof of the graph-specific support/vanishing hypotheses.
