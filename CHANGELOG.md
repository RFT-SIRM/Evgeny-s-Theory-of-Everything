# Changelog

## 2026-11-23

- Recorded a proposed polynomial and Fourier representation for the finite H10 level-five recurrence correction.
- Added an exact-integer checker for equivalence of the two supplied candidate forms and endpoint arithmetic against supplied trace values; it does not derive the candidate from the pinned Lean residual definition.
- Kept the H10 all-level recurrence and affine-form theorems separate from this external candidate-form check.
- Left OP-2 open pending proof that the proposed polynomial equals the pinned Lean residual definition.


This file records material repository changes; the complete chronological record
is the Git commit history.

## 2026-10-16

- Added a sourced theorem dossier for the exact limit and finite-level remainder of the scalar invariant formalized in RFT-Cosmology-Genesis.
- Updated the dissertation, mathematical framework, claims ledger, formalization policy, source map, and provenance notice to record the result and its passing post-merge Lean build without claiming physical validation or cross-model equivalence.

## 2026-10-15

- Added an Apache License 2.0 file for this repository's original contributions.
- Added citation metadata and an attribution boundary for separate upstream projects.
- Clarified that the exact modular/CRT certificate covers finite-level Fourier coefficients and does not prove the all-level higher-moment recurrence.
- Updated the final status and historical addendum to distinguish scientific evidence from repository/CI changes.
- Extended documentation-integrity checks to require license, notice, and citation metadata.
- Preserved prior failed GitHub Actions runs as historical records tied to their original commits.
