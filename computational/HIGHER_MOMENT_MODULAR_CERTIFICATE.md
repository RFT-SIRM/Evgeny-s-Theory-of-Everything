# Exact finite-level Fourier coefficient certificate

**Status: exact finite-level coefficient identities certified by modular arithmetic and CRT; the all-level recurrence remains open.**

This certificate upgrades the floating-point Fourier reconstruction in [the coefficient-candidate note](HIGHER_MOMENT_COEFFICIENT_CANDIDATES.md). It verifies the displayed Fourier coefficients for $R_2^{(p)}(\theta)=\Delta_2^{(p)}(\theta)-3\Delta_1^{(p)}(\theta)$ and $R_4^{(p)}(\theta)=\Delta_4^{(p)}(\theta)-3\Delta_3^{(p)}(\theta)$, for $p=6,8,10$. It does **not** prove that $R_m^{(p)}=R_4^{(p)}$ for all $m\ge3$.

## Exact reconstruction

Write $\phi=\theta/2$. The $p$-th trace is a trigonometric polynomial with modes $e^{ik\phi}$ for $|k|\le p$, because every matrix entry is linear in $\cos\phi$ and $\sin\phi$. For $p\le10$, the 21 points $\theta_j=\frac{4\pi j}{21}$, $j=0,\ldots,20$, therefore determine all possible Fourier modes without aliasing.

The calculation is repeated in three finite fields with primes $q\in\{10000453,\ 20000569,\ 30000769\}$. Each prime is $1\bmod 84$, so the field contains a primitive 21st root of unity and a square root of $-1$. The script builds the source graph/operator construction over each field, computes traces of matrix powers exactly modulo $q$, and performs the 21-point discrete Fourier transform in the field.

Each operator entry has Fourier coefficients with denominator dividing 2. A product of $p$ entries therefore has denominator dividing $2^p$; consequently, $2^p$ times every Fourier coefficient of the trace defect is an integer. The script compares these scaled coefficients with the proposed integer coefficients modulo all three primes.

## CRT uniqueness bound

For these Sierpiński graphs the maximum vertex degree is 4. The block operator has diagonal block norm at most 4 and connection-adjacency norm at most 4, hence $\|H\|\le8$. For a graph with $n_m$ vertices, the operator dimension is $2n_m$, so $|\operatorname{Tr}(H^p)|\le 2n_m\,8^p$.
This yields bounds on $R_2^{(p)}$ and $R_4^{(p)}$, and hence on each scaled Fourier coefficient. The product of the three primes is greater than twice every such bound. Since the candidate and the true scaled coefficients agree modulo each prime, their difference is divisible by the CRT modulus; the bound forces that difference to be zero.

This certifies the finite-level Fourier coefficients exactly, subject to the stated graph/operator construction, Fourier-mode bound, denominator argument, and norm bound. The committed script records and checks each bound and modular residue.

## What this does and does not prove

**Certified here:**
- exact Fourier coefficients of $R_2^{(p)}$ at the level-1-to-2 transition;
- exact Fourier coefficients of $R_4^{(p)}$ at the level-3-to-4 transition;
- the explicit finite-level correction $R_2^{(p)}-R_4^{(p)}$.

**Still open:**
- a derivation from the recursive graph/operator structure explaining why $R_2$ differs;
- a proof that $R_m^{(p)}=R_4^{(p)}$ for every $m\ge3$ and every angle;
- a Lean formalization of that all-level statement.

Reproduce with:

```sh
python -m pip install "numpy>=1.24,<3" "scipy>=1.10,<2"
python computational/verify_higher_moment_coefficients_modular.py --output artifacts/higher_moment_modular_certificate.json
```

Workflow: [Exact modular coefficient certificate](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/workflows/higher-moment-modular-certificate.yml).
