# Contributing

The repository is a mathematical research record. Contributions should make claims more precise and more reproducible.

## Before submitting

- State the mathematical objects, assumptions, and quantifiers.
- Identify whether the result is proved, formalized, numerically reproduced, observed, conjectural, or open.
- Link the source file and commit for inherited results.
- Include the exact commands and environment for computations.
- Preserve negative results and counterexamples.
- Avoid claims of universal validity from a finite numerical sample.

## Testing

Run the documentation-integrity check:

```sh
python3 scripts/check_docs.py
```

This script checks document presence and provenance markers only. It does not run source-project tests, compile Lean, or prove mathematical statements.
