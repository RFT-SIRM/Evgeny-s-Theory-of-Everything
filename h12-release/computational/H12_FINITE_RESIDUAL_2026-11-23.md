# H12 finite transition residual: exact source-mirrored CRT computation

Date: 23 November 2026

## Result

For the pinned SU(2)-connected Sierpiński-gasket operator definitions, define

\[
D_m^{(12)}(\theta)=\operatorname{Tr}(H_{\mathrm{face}}(m,\theta)^{12})
-\operatorname{Tr}(H_{Z}(m,\theta)^{12}),
\]

and the finite transition residual

\[
C_{12}^{(m)}(\theta)=D_{m+1}^{(12)}(\theta)-3D_m^{(12)}(\theta).
\]

An exact C++ source mirror and three-prime signed CRT reconstruction give

\[
\boxed{C_{12}^{(3)}(\theta)=C_{12}^{(4)}(\theta)=C_{12}^{(5)}(\theta)}
\]

as exact polynomial identities on the unit circle, for these three finite
transitions. The common canonical polynomial, reduced using
\(c^2+s^2=1\), is

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

The independently reconstructed level values at \(\theta=\pi\) are

| Level \(m\) | Vertices | Edges | Faces | \(D_m^{(12)}(\pi)\) |
|---:|---:|---:|---:|---:|
| 3 | 42 | 81 | 27 | -18,026,705,824 |
| 4 | 123 | 243 | 81 | -54,714,191,008 |
| 5 | 366 | 729 | 243 | -164,776,646,560 |
| 6 | 1,095 | 2,187 | 729 | -494,964,013,216 |

Each of the three adjacent differences \(D_{m+1}^{(12)}(\pi)-3D_m^{(12)}(\pi)\),
for \(m=3,4,5\), equals \(-634,073,536\).

## Exact reconstruction and uniqueness bound

The C++ engine reconstructs levels 3--6 from the recursive vertex ordering,
edge and face construction, flux-edge indexing, orientation-dependent SU(2)
entries, and the two axis assignments (face-cyclic and constant-Z). It computes
all degree-12 trace coefficients modulo

\[
10000453,\quad 20000569,\quad 30000769.
\]

The graph counts at each level are checked by the program. Across all computed
matrices the maximum graph degree is 4 and the maximum row coefficient
\(\ell^1\)-norm is 10. For a transition residual
\(C_{12}^{(m)}=D_{m+1}^{(12)}-3D_m^{(12)}\), the coefficient bound used is

\[
B_m=(2N_{m+1}+6N_m)10^{12},
\]

where \(N_m=2|V_m|\) is the spin-expanded matrix dimension. The largest bound,
at \(m=5\), is

\[
B_5=8,772,000,000,000,000.
\]

The CRT modulus product is

\[
6,000,596,319,075,658,215,133>2B_5
=17,544,000,000,000,000.
\]

Thus each reconstructed integer coefficient is unique under the stated
source-mirror and row-norm bound. All reconstructed imaginary coefficients
vanish. Canonical reduction by \(c^2=1-s^2\) gives exactly the same 13 integer
coefficients for all three transitions.

## Reproduction

From the repository root:

```sh
python3 -m computational.h12_residual_certificate --output computational/data/h12_residual_certificate.json
python3 -m unittest computational.test_h12_residual_certificate -v
```

The first command compiles `computational/h12_residual_engine.cpp`, recomputes
the degree-12 traces over all three primes, reconstructs the exact coefficients,
and writes the JSON artifact. The unit tests check the pinned source, CRT
uniqueness margin, polynomial/Fourier forms, and the three finite-level
transition equalities.

## Evidence boundary — important

This is an **exact external finite-level CRT certificate**. It establishes
\(C_{12}^{(3)}=C_{12}^{(4)}=C_{12}^{(5)}\) for the source-mirrored finite
matrices. It does **not** prove that \(C_{12}^{(m)}\) is independent of \(m\)
for every level, and it is not a Lean-kernel theorem. In particular, this
certificate does not yet establish an all-level H12 recurrence or an affine
closed form. The next mathematical obligation is to prove the radius-five
corner transport and the degree-12 boundary expansion uniformly in the graph
level, then formalize the resulting recurrence in Lean.
