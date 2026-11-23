# H10 level-five residual: proposed coefficient expression and internal identity check

Date: 23 November 2026

The H10 recurrence proved in the pinned Lean source has an unconditional
level-five affine form. Its finite correction is represented by the trace
difference (C_{10}^{(5)}=D_6-3D_5).

A proposed coefficient expression for this correction is recorded as

\[
\begin{aligned}
C_{10}^{(5)}(\theta)={}&-748240s^2+11036800cs^2+4927360s^3\\
&-261920cs^3+330960s^4+1920cs^4\\
&-3200s^5+320cs^5+640s^6,
\quad c=\cos(\theta/2),\ s=\sin(\theta/2).
\end{aligned}
\]

Equivalently, with (u=\theta/2),

\[
\begin{aligned}
C_{10}^{(5)}(\theta)={}&-249810+2759440\cos u+3693520\sin u\\
&+208340\cos 2u-65430\sin 2u\\
&-2759560\cos 3u-1230840\sin 3u\\
&+41490\cos 4u+32700\sin 4u\\
&+120\cos 5u-200\sin 5u-20\cos 6u+10\sin 6u.
\end{aligned}
\]

The script verifies the equivalence of the supplied polynomial and Fourier forms exactly in the quotient ring
\(\mathbb Z[c,s]/(c^2+s^2-1)\), using integer binomial coefficients. It also
evaluates the polynomial at \((c,s)=(1,0)\) and \((0,1)\), and checks
agreement at \(\theta=\pi\) with the supplied trace endpoint values.
The endpoint arithmetic recorded for the trace calculation is
\(D_5(\pi)=-2,505,633,280\),
\(D_6(\pi)=-7,512,392,320\), hence
\(C_{10}^{(5)}(\pi)=4,507,520\).

**Evidence boundary.** This repository-side script checks only the internal
identity between the supplied polynomial and Fourier forms and the stated
endpoint arithmetic. It does not derive the candidate polynomial from the
pinned Lean definition `defectO10_num_residual_constant`, nor does it
reconstruct the level-five and level-six graph trace matrices from scratch.
The trace values and candidate coefficients are inputs to this checker,
not outputs independently derived by it. Therefore equality of the proposed
polynomial to the source residual for all real angles remains open. The
all-level recurrence and affine form remain Lean results in the pinned
upstream source; the candidate-form check is not a Lean-kernel theorem.

Run:

```sh
python -m computational.h10_level5_residual_certificate
python -m unittest computational.test_h10_level5_residual_certificate -v
```
