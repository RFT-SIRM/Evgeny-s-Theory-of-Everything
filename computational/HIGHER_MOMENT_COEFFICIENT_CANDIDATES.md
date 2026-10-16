# Higher-moment Fourier coefficient candidates

**Status: exact finite-level Fourier identities certified by modular/CRT; the all-level recurrence remains open.**

Let
\[
R_m^{(p)}(\theta)=\Delta_m^{(p)}(\theta)-3\Delta_{m-1}^{(p)}(\theta),
\qquad \phi=\theta/2.
\]
The candidate later-transition coefficient is \(C_p(\theta)=R_4^{(p)}(\theta)\). The exceptional first transition is \(R_2^{(p)}(\theta)\).

The following integer Fourier coefficients give the exact finite-level identities for \(R_2^{(p)}\) and \(R_4^{(p)}\). They were first reconstructed numerically, then certified by modular arithmetic over three finite fields and a CRT uniqueness bound; see [the exact certificate](HIGHER_MOMENT_MODULAR_CERTIFICATE.md). They do **not** establish that \(R_m^{(p)}=R_4^{(p)}\) for every \(m\ge3\).

## Certified finite-level later-transition residual \(R_4^{(p)}(\theta)\)

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

At \(\theta=\pi/2\), these give approximately \(2595.41125497\), \(153107.523159\), and \(5287216.62180\). At \(\theta=\pi\), they give \(5280\), \(277504\), and \(4507520\).

## Certified finite-level first-transition residual \(R_2^{(p)}(\theta)\)

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

## A factorization pattern for the exceptional transition

Subtracting the candidate later-transition coefficient gives
\[
R_2^{(p)}(\theta)-C_p(\theta)=\sin^2\phi\,Q_p(\phi).
\]
The certified quotient functions are
\[
Q_6(\phi)=-24,
\]
\[
\begin{aligned}
Q_8(\phi)={}&-19840-3840\cos\phi+11008\sin\phi\\
&-288\cos(2\phi)-96\sin(2\phi),
\end{aligned}
\]
and
\[
\begin{aligned}
Q_{10}(\phi)={}&-3103440-539280\cos\phi+2405520\sin\phi\\
&-198320\cos(2\phi)-76240\sin(2\phi)\\
&+12240\cos(3\phi)+1680\sin(3\phi)\\
&-200\cos(4\phi)+80\sin(4\phi).
\end{aligned}
\]

The certified correction has a quadratic zero at \(\theta=0\) and also vanishes at \(\theta=2\pi\). This factorization follows algebraically from the certified finite-level formulas, but it is not yet a derivation from the graph/operator recursion. The structural cause of the exception remains open.

## Reconstruction protocol

- Use \(N=21=2p_{\max}+1\) samples, \(\theta_j=4\pi j/21\), \(j=0,\ldots,20\).
- Compute \(R_2\) and \(R_4\) directly from sparse matrix-power traces for levels 1–4.
- Recover Fourier coefficients by a discrete Fourier transform and compare them with the displayed integer coefficients.
- Validate at seven off-grid angles not used in the Fourier reconstruction.
- Separately test recurrence predictions on held-out levels 5–7 with the sparse-trace workflow.

Each operator entry is linear in \(\cos(\theta/2)\) and \(\sin(\theta/2)\), so a trace of the \(p\)-th matrix power has Fourier modes of order at most \(p\) in \(\phi=\theta/2\). The 21-point reconstruction is therefore the right finite Fourier sampling size for moments through \(p=10\). Floating-point reconstruction and off-grid agreement were the discovery and consistency checks; exact integer coefficients are certified separately by the modular/CRT argument above.

Reproduce with:

```sh
python -m pip install "numpy>=1.24,<3" "scipy>=1.10,<2"
python computational/derive_higher_moment_coefficients.py --output artifacts/higher_moment_coefficient_candidates.json
```

The dedicated [Fourier coefficient candidate workflow passed](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38767383292). The expanded [independent sparse level-7 holdout also passed](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/runs/38767388243).
