# Higher-moment Fourier coefficient candidates

**Status: strong numerical reconstruction; exact symbolic derivation and universal proof remain open.**

Let
\[
R_m^{(p)}(\theta)=\Delta_m^{(p)}(\theta)-3\Delta_{m-1}^{(p)}(\theta),
\qquad \phi=\theta/2.
\]
The candidate recurrence coefficient is (C_p(\theta)=R_4^{(p)}(\theta)). The exceptional first transition is (R_2^{(p)}(\theta)).

The following integer Fourier coefficients were reconstructed from 21 equally spaced samples over a (4\pi) period, then checked against off-grid sparse-trace evaluations. They are **candidate identities inferred numerically**, not yet symbolic proofs. The reproducibility script checks coefficient recovery and off-grid residuals in CI.

## Candidate later-transition coefficients (C_p(\theta)=R_4^{(p)}(\theta))

\[
\begin{aligned}
C_6(\theta)={}&2256+48\cos\phi+576\sin\phi-2256\cos(2\phi)\\
&-48\cos(3\phi)-192\sin(3\phi).
\end{aligned}
\]

\[
\begin{aligned}
C_8(\theta)={}&96872+18944\cos\phi+62784\sin\phi\\
&-96896\cos(2\phi)-128\sin(2\phi)\\
&-18944\cos(3\phi)-20928\sin(3\phi)\\
&+24\cos(4\phi)+64\sin(4\phi).
\end{aligned}
\]

\[
\begin{aligned}
C_{10}(\theta)={}&-249810+2759440\cos\phi+3693520\sin\phi\\
&+208340\cos(2\phi)-65430\sin(2\phi)\\
&-2759560\cos(3\phi)-1230840\sin(3\phi)\\
&+41490\cos(4\phi)+32700\sin(4\phi)\\
&+120\cos(5\phi)-200\sin(5\phi)\\
&-20\cos(6\phi)+10\sin(6\phi).
\end{aligned}
\]

At \(\theta=\pi/2\), these give the previously observed coefficients approximately (2595.41125497), (153107.523159), and (5287216.62180). At \(\theta=\pi\), they give (5280), (277504), and (4507520).

## Candidate first-transition coefficients (R_2^{(p)}(\theta))

\[
\begin{aligned}
R_2^{(6)}(\theta)={}&2244+48\cos\phi+576\sin\phi-2244\cos(2\phi)\\
&-48\cos(3\phi)-192\sin(3\phi).
\end{aligned}
\]

\[
\begin{aligned}
R_2^{(8)}(\theta)={}&87024+17984\cos\phi+71040\sin\phi\\
&-87120\cos(2\phi)-176\sin(2\phi)\\
&-17984\cos(3\phi)-23680\sin(3\phi)\\
&+96\cos(4\phi)+88\sin(4\phi).
\end{aligned}
\]

\[
\begin{aligned}
R_2^{(10)}(\theta)={}&-1751950+2621560\cos\phi+5497240\sin\phi\\
&+1660950\cos(2\phi)-103570\sin(2\phi)\\
&-2618620\cos(3\phi)-1831380\sin(3\phi)\\
&+90970\cos(4\phi)+51800\sin(4\phi)\\
&-2940\cos(5\phi)-620\sin(5\phi)\\
&+30\cos(6\phi)-10\sin(6\phi).
\end{aligned}
\]

The distinct (R_2) and (R_4) candidates make the first-transition exception explicit as a different function of angle. They do **not** yet explain its structural cause in the graph/operator recursion.

## Reconstruction protocol

- Use (N=21=2p_{\max}+1) angle samples, (\theta_j=4\pi j/21), (j=0,\ldots,20).
- Compute (R_2) and (R_4) directly from sparse matrix-power traces for levels 1–4.
- Recover the Fourier coefficients by a discrete Fourier transform and compare them with the displayed integer candidates.
- Validate at seven off-grid angles, not used in the Fourier reconstruction.
- Separately test the proposed recurrence on held-out levels 5–7 with the sparse-trace workflow.

The bound on Fourier frequency follows from each operator entry being linear in (\cos(\theta/2)) and (\sin(\theta/2)): a trace of the (p)-th matrix power is a trigonometric polynomial with modes at most (p) in (\phi=\theta/2\). The numerical calculation is consistent with that finite-dimensional representation. It does not by itself certify exact integer coefficients.

Reproduce with:

```sh
python -m pip install "numpy>=1.24,<3" "scipy>=1.10,<2"
python computational/derive_higher_moment_coefficients.py --output artifacts/higher_moment_coefficient_candidates.json
```

Workflow: [Higher-moment Fourier coefficient candidates](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/workflows/higher-moment-coefficient-candidates.yml).
