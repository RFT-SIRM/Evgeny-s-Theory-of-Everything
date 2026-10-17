# Exact Limit Theorem for the Scalar Invariant

**Status:** machine-checked in Lean 4 in the source repository linked below. This page records the theorem in the shared research archive and preserves its provenance; it does not claim an independent second formalization here.

## 1. Definition

For an integer level $m\geq 1$ and a real parameter $\theta$, define the scalar invariant

$

I_m(\theta)
=-16\frac{3^{m-1}+1}{3^{m+1}+3}
 \sin^2\!\left(\frac{\theta}{2}\right).

$

Set

$

I_\infty(\theta)
:=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right).

$

## 2. Theorem

For every $\theta\in\mathbb R$,

$

\boxed{\lim_{m\to\infty} I_m(\theta)=I_\infty(\theta)
=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right).}

$

Moreover, for every integer $m\geq1$ and every $\theta\in\mathbb R$, the exact finite-level remainder is

$

\boxed{
I_m(\theta)-I_\infty(\theta)
=-\frac{32}{9(3^m+1)}
 \sin^2\!\left(\frac{\theta}{2}\right).
}

$

The remainder identity gives an explicit error term for each finite level; because $3^m+1\to\infty$, the remainder tends to zero.

## 3. Algebraic derivation

The elementary identities

$

3^{m-1}+1=\frac{3^m+3}{3},
\qquad
3^{m+1}+3=3(3^m+1)

$

give

$

\begin{aligned}
I_m(\theta)
&=-\frac{16(3^m+3)}{9(3^m+1)}
  \sin^2\!\left(\frac{\theta}{2}\right)\\
&=-\frac{16}{9}
  \left(1+\frac{2}{3^m+1}\right)
  \sin^2\!\left(\frac{\theta}{2}\right)\\
&=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right)
  -\frac{32}{9(3^m+1)}
  \sin^2\!\left(\frac{\theta}{2}\right).
\end{aligned}

$

Subtracting $I_\infty(\theta)$ yields the exact remainder. Its second term tends to zero as $m\to\infty$, proving the stated limit.

## 4. Formal verification and reproducibility

The Lean source is maintained in the separate repository [RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis):

- Source file: [formalization/lean/CosmologyGenesis.lean](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/blob/2a7782a8a56181313808019202089f167cf09cc2/formalization/lean/CosmologyGenesis.lean)
- Limit theorem: **rftInvariant_tendsto**
- Exact remainder theorem: **rftInvariant_remainder**
- Equivalent decomposition: **rftInvariant_exact_decomposition**
- Merge commit containing the theorem: [2a7782a8a56181313808019202089f167cf09cc2](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/commit/2a7782a8a56181313808019202089f167cf09cc2)
- Lean build on the post-merge main commit: [GitHub Actions run 38904548580](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/actions/runs/38904548580)
- Python regression suite on that post-merge commit: [GitHub Actions run 38904548632](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/actions/runs/38904548632)

The source project pins Lean 4.33.1 and Mathlib 4.33.1. The Lean build is the machine-checked evidence for the named Lean statements; the Python tests provide regression checks and should not be described as proving the theorem.

## 5. Scope and evidence boundary

This is a theorem about the scalar formula defined in Section 1. Its formalization proves the limit and remainder for those definitions and quantifiers.

It does **not** by itself establish that the scalar invariant describes a physical cosmological interaction, fits observed CMB data, or constitutes a new physical law. It also does not prove an equivalence between the SU(2)-connected operators and the signed $Z_2$-flux Laplacians discussed elsewhere in this archive. Those are separate claims requiring their own precise definitions and proofs.

## 6. Provenance

This result was merged into **main** of RFT-Cosmology-Genesis on 16 October 2026. The shared archive records the statement and points to the source proof and CI evidence; it does not duplicate the source Lean project or imply that the theorem has been independently re-formalized in this repository.
