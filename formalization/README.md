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
