# H12 finite transition residual: exact source-mirrored CRT computation through level 8

Date: 23 November 2026

## Result

For the pinned SU(2)-connected Sierpiński-gasket operator definitions, let

\[
D_m^{(12)}(\theta)=\operatorname{Tr}(H_{\mathrm{face}}(m,\theta)^{12})
-\operatorname{Tr}(H_Z(m,\theta)^{12}),
\]

and define the finite transition residual

\[
C_{12}^{(m)}(\theta)=D_{m+1}^{(12)}(\theta)-3D_m^{(12)}(\theta).
\]

A source-mirrored C++ computation over three prime fields, followed by signed
coefficient-wise CRT, gives the exact finite identities

\[
\boxed{C_{12}^{(3)}(\theta)=C_{12}^{(4)}(\theta)
=C_{12}^{(5)}(\theta)=C_{12}^{(6)}(\theta)=C_{12}^{(7)}(\theta)}.
\]

The common canonical polynomial, reduced using \(c^2+s^2=1\), is

\[
\begin{aligned}
C_{12}(\theta)={}&-945325824s^2+1186927488cs^2
+208608384s^3-36718464cs^3\\
&+102067392s^4-2090112cs^4-18816s^5+158592cs^5\\
&+565760s^6-15360cs^6+29184s^7-384cs^7+384s^8,
\end{aligned}
\]

where \(c=\cos(\theta/2)\) and \(s=\sin(\theta/2)\).

Equivalently, with \(u=\theta/2\),

\[
\begin{aligned}
C_{12}(\theta)={}&-434210735
+296469408\cos u+156460488\sin u\\
&+421363848\cos 2u-9154878\sin 2u\\
&-296337816\cos 3u-52155792\sin 3u\\
&+12864588\cos 4u+4570026\sin 4u\\
&-131832\cos 5u+2016\sin 5u\\
&-17704\cos 6u+4938\sin 6u\\
&+240\cos 7u-456\sin 7u+3\cos 8u+3\sin 8u.
\end{aligned}
\]

At the endpoints,
\[
C_{12}(0)=0,\qquad C_{12}(\pi)=-634073536.
\]

The reconstructed level values at \(\theta=\pi\) are:

| Level \(m\) | Vertices | Edges | Faces | \(D_m^{(12)}(\pi)\) |
|---:|---:|---:|---:|---:|
| 3 | 42 | 81 | 27 | -18,026,705,824 |
| 4 | 123 | 243 | 81 | -54,714,191,008 |
| 5 | 366 | 729 | 243 | -164,776,646,560 |
| 6 | 1,095 | 2,187 | 729 | -494,964,013,216 |
| 7 | 3,282 | 6,561 | 2,187 | -1,485,526,113,184 |
| 8 | 9,843 | 19,683 | 6,561 | -4,457,212,413,088 |

All five adjacent differences \(D_{m+1}^{(12)}(\pi)-3D_m^{(12)}(\pi)\),
for \(m=3,4,5,6,7\), equal \(-634,073,536\).

## Exact reconstruction and CRT uniqueness

The level-7 certificate for transitions m=3,4,5,6 is carried forward unchanged.
The extension engine rebuilds the level-7 and level-8 recursive vertex orders,
gasket edges and faces, flux-edge indexing, orientation-dependent SU(2)
entries, and both axis assignments over the primes

\[
10000453,\quad 20000569,\quad 30000769.
\]

To make the level-8 extension tractable, the engine computes only the two
new graph levels (7 and 8), and reduces the polynomial after every
multiplication using
\[
c^2=1-s^2.
\]
It therefore propagates the canonical basis \(c^a s^b\), \(a\in\{0,1\}\),
instead of all 91 unreduced monomials of total degree at most 12. This is an
exact ring reduction, not a numerical approximation. The four prior finite transitions remain in the previously verified level-7
certificate and are copied unchanged. The new transition m=7 is reconstructed
coefficient-by-coefficient from the three prime-field outputs. The independent
integer path-sum cross-check at level 7 remains part of the test suite.

Let \(N_m=2|V_m|\) be the spin-expanded matrix dimension, and let the maximum
row coefficient \(\ell^1\)-norm be \(W=10\). Before canonical reduction, the
path-count bound for the coefficient \(\ell^1\)-sum of the transition residual
is
\[
B_m^{\rm raw}=(2N_{m+1}+6N_m)W^{12}.
\]
For a monomial \(c^a s^b\) of degree at most 12, canonical reduction expands
\[
c^a=(1-s^2)^{\lfloor a/2\rfloor}c^{a\bmod2},
\]
whose coefficient \(\ell^1\)-sum is at most
\(2^{\lfloor a/2\rfloor}\le64\). Thus a valid bound for every canonical
coefficient is
\[
B_m^{\rm canonical}=64B_m^{\rm raw}.
\]

The raw and canonical bounds are:

| Transition \(m\) | Raw path \(\ell^1\) bound | Canonical coefficient bound |
|---:|---:|---:|
| 3 | 996,000,000,000,000 | 63,744,000,000,000,000 |
| 4 | 2,940,000,000,000,000 | 188,160,000,000,000,000 |
| 5 | 8,772,000,000,000,000 | 561,408,000,000,000,000 |
| 6 | 26,268,000,000,000,000 | 1,681,152,000,000,000,000 |
| 7 | 78,756,000,000,000,000 | 5,040,384,000,000,000,000 |

The CRT modulus product is
\[
6,000,596,319,075,658,215,133,
\]
which exceeds twice the largest canonical coefficient bound,
\[
10,080,768,000,000,000,000.
\]
The uniqueness margin ratio is 595. All reconstructed imaginary
coefficients vanish. The same 13 canonical integer coefficients are obtained
for each of the five transitions.

## Reproduction

From the repository root:

```sh
python3 -m computational.h12_residual_certificate --output computational/data/h12_residual_certificate.json
python3 -m unittest computational.test_h12_residual_certificate -v
```

The level-7 source certificate is preserved at
`computational/data/h12_level7_residual_certificate.json`. The extension engine
compiles `computational/h12_residual_engine.cpp` and independently rebuilds
levels 7 and 8 over all three primes, then extends the prior certificate with
the new transition C12^(7). It checks the graph counts, row norm, CRT uniqueness,
all coefficients, Fourier form and endpoints.

From the repository root, the normal command above recompiles the C++ engine
and reruns the three new prime calculations. For a fast reconstruction using
the three recorded raw C++ outputs (whose hashes are checked), run:

```sh
python3 -m computational.h12_residual_certificate --use-cached-prime-data --output computational/data/h12_residual_certificate.json
```

The GitHub Actions workflow uses the normal fresh-engine command and compares
the generated JSON with the certificate.

## Evidence boundary — important

This is an **exact external finite-level CRT certificate** establishing
\(C_{12}^{(3)}=C_{12}^{(4)}=C_{12}^{(5)}=C_{12}^{(6)}=C_{12}^{(7)}\) for the
five computed finite transitions. It does **not** prove that \(C_{12}^{(m)}\)
is independent of \(m\) for every level, and it is not a Lean-kernel theorem.
It does not yet establish an all-level H12 recurrence or an affine closed form.

The next mathematical obligation is to prove the radius-five corner transport
for powers through degree 11, derive the full degree-12 boundary expansion
uniformly in the graph level, and formalize the resulting recurrence in Lean.


## Follow-up: degree-12 boundary word expansion

The complete ordered-composition inventory and its level-3/level-4 corner-distance classification are recorded in [H12_BOUNDARY_WORD_EXPANSION_2026-11-23.md](H12_BOUNDARY_WORD_EXPANSION_2026-11-23.md). This is an exact algebraic/combinatorial reduction, not yet the graph-specific boundary contraction or an all-level Lean theorem.
