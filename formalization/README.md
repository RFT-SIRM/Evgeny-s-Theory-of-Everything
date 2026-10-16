# Formalization integration

The primary formalization currently lives in the source repository [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem).

Before copying or restructuring Lean files here:
1. inspect the exact source theorem and all imported definitions;
2. preserve the source license and attribution;
3. pin the Lean toolchain and Mathlib dependency revision;
4. build from a clean checkout;
5. add a CI workflow that runs the actual Lean build;
6. keep the formal theorem statement synchronized with the claim ledger.

Do not add placeholder Lean files or mark a theorem as formalized merely because the source repository describes it as such. The present document records the integration policy; it does not itself contain a proof.


## Separate scalar-invariant limit theorem

The theorem **rftInvariant_tendsto** and the exact finite-level remainder for a defined scalar invariant are maintained in [RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis), file [formalization/lean/CosmologyGenesis.lean](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/blob/2a7782a8a56181313808019202089f167cf09cc2/formalization/lean/CosmologyGenesis.lean). Its post-merge Lean build passed on the merged main commit. See [the theorem dossier](../theorems/exact_invariant_limit.md) for the statement, exact remainder, commit, and CI evidence.

This is a separate proof project from the synthesis workflow described above. Do not state that the synthesis repository's pinned fourth-moment workflow builds this theorem, and do not treat this scalar result as a proof of a physical cosmological claim or a bridge between operator models.
