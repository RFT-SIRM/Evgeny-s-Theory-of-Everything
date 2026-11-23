H12 finite-residual package for Evgeny-s-Theory-of-Everything

Contains the exact C++ source-mirrored H12 engine, three-prime signed CRT
reconstruction, certificate JSON, tests, and report. It also integrates H12 into
the existing higher-moment certificate workflow and records the remaining
all-level proof obligation in OPEN_PROBLEMS.md and CURRENT_EVIDENCE.md.

From the repository root, run:
  bash h12-release/APPLY_AND_VERIFY_H12.sh

The script checks the expected branch/base commit, preserves the existing H10
worktree changes and stash, applies the H12 files, runs the exact three-prime
reconstruction, compares the generated JSON to the certificate, runs tests,
and performs git diff --check. It does not commit, push, reset, stash, or switch
branches.
