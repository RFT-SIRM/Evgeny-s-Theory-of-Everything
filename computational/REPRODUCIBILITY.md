# Computational reproducibility protocol

## Required record

Every computational result should record:
- repository and commit SHA;
- command executed;
- operating system and language/runtime versions;
- dependencies and versions;
- graph level, model parameters, and precision/tolerance;
- raw output or a machine-readable artifact;
- known failure modes and limitations.

## Numerical checks

- State whether arithmetic is exact, arbitrary precision, or floating point.
- Define the tolerance before interpreting the output.
- Test base cases and exceptional cases.
- Compare against an independent implementation or exact result where practical.
- Do not use a fitted value both to define a recurrence constant and as the sole evidence that the recurrence holds.

## Formal checks

Machine-checked claims must identify the proof assistant version, dependency revision, build command, and successful build log. A Python test suite does not establish that a Lean theorem compiles.

## Reproduction status

This repository is newly initialized. No claim is made here that the source projects' full test suites or formal builds have already been rerun from clean environments.
