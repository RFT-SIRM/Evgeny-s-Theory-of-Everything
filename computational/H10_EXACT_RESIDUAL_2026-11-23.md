# H10 level-five residual: source-reconstructed exact coefficient certificate

Date: 23 November 2026

## Result

The pinned Lean source defines the H10 level-five recurrence residual and proves the unconditional recurrence
[
D_{m+1}^{(10)}(\theta)=3D_m^{(10)}(\theta)+C_{10}^{(5)}(\theta),\qquad m\ge4.
]
In particular, its exact finite correction is
[
C_{10}^{(5)}(\theta)=D_6^{(10)}(\theta)-3D_5^{(10)}(\theta).
]

The level-five and level-six trace matrices have now been reconstructed from the graph, orientation, flux, and SU(2) definitions at the pinned source revision. A three-prime modular computation and coefficient-wise signed CRT recover the following exact polynomial:
[
\begin{aligned}
C_{10}^{(5)}(\theta)={}&-748240s^2+11036800cs^2+4927360s^3\\
&-261920cs^3+330960s^4+1920cs^4\\
&-3200s^5+320cs^5+640s^6,
\qquad c=\cos(\theta/2),\quad s=\sin(\theta/2).
\end{aligned}
]

Equivalently, with (u=\theta/2),
[
\begin{aligned}
C_{10}^{(5)}(\theta)={}&-249810+2759440\cos u+3693520\sin u\\
&+208340\cos 2u-65430\sin 2u\\
&-2759560\cos 3u-1230840\sin 3u\\
&+41490\cos 4u+32700\sin 4u\\
&+120\cos 5u-200\sin 5u-20\cos 6u+10\sin 6u.
\end{aligned}
]

## Exact source reconstruction

The C++17 engine is stored in `computational/h10_level5_source_reconstruction.tar.gz` together with the Python CRT verifier. It mirrors the pinned declarations:

- `Graph/Sierpinski.lean`: recursive Sierpiński-gasket graph edges;
- `Orientation.lean`: first-occurrence vertex order in `A ++ B ++ C`;
- `Graph/Faces.lean`: `facesExact`, `fluxEdge`, and `fluxEdges`;
- `Operator.lean` and `OpSplit1.lean`: degree diagonal, edge connections, and orientation-dependent `-U` / `-Uᴴ` entries;
- `SU2.lean`: the three Pauli-axis rotations;
- `FinalClosed10.lean`: the Lean-checked recurrence identifying the residual with `D6 - 3*D5`.

For each prime, the program expands the sparse length-ten closed-walk sums coefficient by coefficient. The maximum matrix-row coefficient l1-norm is 10. The signed coefficient bound is
[
(2\cdot2190+6\cdot732)\,10^{10}=87,720,000,000,000.
]
The CRT modulus product is
[
6,000,596,319,075,658,215,133,
]
which is greater than twice the bound. Thus each recovered integer coefficient is unique.

The source graph counts checked by the program are:

| Level | Vertices | Edges | Faces |
|---|---:|---:|---:|
| 5 | 366 | 729 | 243 |
| 6 | 1095 | 2187 | 729 |

The same matrix builder reproduces the Lean H4 controls at levels 1–6:
[
-32,-64,-160,-448,-1312,-3904.
]
At \(\theta=\pi\), it obtains
[
D_5^{(10)}(\pi)=-2,505,633,280,\quad
D_6^{(10)}(\pi)=-7,512,392,320,
]
and hence
[
C_{10}^{(5)}(\pi)=D_6^{(10)}(\pi)-3D_5^{(10)}(\pi)=4,507,520.
]

## Reproduction

From the repository root, extract the two source files from the committed source bundle, then run:

```sh
tar -xzf computational/h10_level5_source_reconstruction.tar.gz -C .
python3 -m computational.h10_level5_residual_certificate --output computational/data/h10_level5_residual_certificate.json
python3 -m unittest computational.test_h10_level5_residual_certificate -v
```

The GitHub Actions workflow performs these steps, compares the regenerated JSON with the committed artifact, and uploads the exact certificate.

## Evidence boundary

The identity (C_{10}^{(5)}=D_6-3D_5), the all-angle recurrence, and its affine form are Lean-checked in the pinned source project. The finite coefficient expansion is an **exact external modular/CRT certificate** derived from a direct executable mirror of the pinned graph/operator definitions. It is not a Lean-kernel coefficient theorem, and the report does not claim that the C++ implementation itself is verified by Lean. This closes the finite computational derivation while preserving the formalization boundary.
