# Radius-to-moment locality lemma

**Status:** the radius-to-moment implication is proved on paper, and the uniform radius-four operator transport needed for H10 is now formalized upstream in CornerLocality.lean, FinalTilde.lean, and FinalClosed10.lean. See [CURRENT_EVIDENCE.md](../CURRENT_EVIDENCE.md) for exact declarations and source pin.

## Lemma

Let $H$ and $H'$ be block matrices indexed by vertices of graphs, with the same finite-dimensional internal block space at each vertex. Let $o$ and $o'$ be distinguished roots. Suppose the rooted radius-$R$ induced neighbourhoods are isomorphic by a map $\phi$ that preserves every directed operator block:
$$
H_{uv}=H'_{\phi(u),\phi(v)}
$$
for every ordered pair $u,v$ in the radius-$R$ ball (including zero blocks for non-edges). Then
$$
(H^j)_{oo}=(H'^j)_{o'o'} \qquad (0\le j\le 2R+1).
$$

The same statement holds if the blocks are related by a single consistent internal basis change $S$, namely $H'_{\phi(u),\phi(v)}=S^{-1}H_{uv}S$; then the conclusion is conjugacy of the root blocks by $S$.

## Proof

For $j\ge1$, expand the root block of the matrix power as a sum over closed vertex walks:
$$
(H^j)_{oo}
=\sum_{v_1,\ldots,v_{j-1}}
H_{o v_1}H_{v_1v_2}\cdots H_{v_{j-1}o}.
$$
A term can be nonzero only when every consecutive pair is an edge (or a permitted on-site block). Consider a contributing closed walk of length $j$. If the walk is at vertex $v_t$ after $t$ steps, then
$$
d(o,v_t)\le t,\qquad d(o,v_t)\le j-t,
$$
because the initial segment reaches $v_t$ in $t$ steps and the remaining segment returns to $o$ in $j-t$ steps. Hence
$$
d(o,v_t)\le \min(t,j-t)\le \lfloor j/2\rfloor.
$$
If $j\le2R+1$, then $\lfloor j/2\rfloor\le R$. Every contributing closed walk therefore lies entirely inside the radius-$R$ ball. The rooted isomorphism gives a bijection between these walks and preserves every factor in their ordered block products, so the sums agree term by term. The case $j=0$ is the identity block. A consistent basis change conjugates each product and therefore conjugates the sum. $\square$

## Consequence for the current project

For $R=4$, exact preservation of the directed operator blocks on a rooted radius-4 neighbourhood implies equality of diagonal corner blocks $(H^j)_{oo}$ for every $j\le9$. This gives a clean explanation for why radius 4 is the relevant locality scale for the sixth-, eighth-, and tenth-moment calculations.

The directed labelled-graph audit remains an independent finite regression check. The all-level operator-level transport is no longer supported solely by that finite audit: it is represented by upstream Lean transport theorems and is used in H10TransportAll_proved. The H10 recurrence still retains its separate exact level-five residual-expression boundary.

## Degree-10 boundary warning

The lemma concerns diagonal root blocks through power 9. It does not claim that off-diagonal blocks between distinct corners vanish at powers 8 or 9. Those blocks are observed to be nonzero on level 3 and must remain explicit in the $3\to4$ transition analysis for degree 10.
