#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

EXPECTED_HEAD="0c9d184abc0e83abe8d27f3ca47efd041fe7faa8"
EXPECTED_BRANCH="research/h10-op2-exact-residual"
ACTUAL_HEAD="$(git rev-parse HEAD)"
ACTUAL_BRANCH="$(git branch --show-current)"

if [[ "$ACTUAL_HEAD" != "$EXPECTED_HEAD" || "$ACTUAL_BRANCH" != "$EXPECTED_BRANCH" ]]; then
  echo "STOP: expected $EXPECTED_BRANCH at $EXPECTED_HEAD"
  echo "Found: $ACTUAL_BRANCH at $ACTUAL_HEAD"
  exit 1
fi

if ! git diff --quiet -- OPEN_PROBLEMS.md CURRENT_EVIDENCE.md .github/workflows/higher-moment-modular-certificate.yml; then
  echo "STOP: one of the documentation/workflow targets already has local edits."
  exit 1
fi

for file in \
  computational/h12_residual_engine.cpp \
  computational/h12_residual_certificate.py \
  computational/test_h12_residual_certificate.py \
  computational/H12_FINITE_RESIDUAL_2026-11-23.md \
  computational/data/h12_residual_certificate.json; do
  if [[ -e "$file" ]]; then
    echo "STOP: destination already exists: $file"
    exit 1
  fi
done

mkdir -p computational/data .github/workflows
cp "$SCRIPT_DIR/computational/h12_residual_engine.cpp" computational/
cp "$SCRIPT_DIR/computational/h12_residual_certificate.py" computational/
cp "$SCRIPT_DIR/computational/test_h12_residual_certificate.py" computational/
cp "$SCRIPT_DIR/computational/H12_FINITE_RESIDUAL_2026-11-23.md" computational/
cp "$SCRIPT_DIR/computational/data/h12_residual_certificate.json" computational/data/
cp "$SCRIPT_DIR/.github/workflows/higher-moment-modular-certificate.yml" .github/workflows/

cat >> OPEN_PROBLEMS.md <<'OPEN_PROBLEMS_APPEND'

## OP-8 — All-level H12 transition recurrence

An exact source-mirrored three-prime signed CRT computation now reconstructs the degree-12 transition residuals for levels m=3,4,5 and establishes the finite identities C12^(3)=C12^(4)=C12^(5). The common polynomial, Fourier form, graph counts, coefficient bounds, and reproduction commands are recorded in [H12_FINITE_RESIDUAL_2026-11-23.md](computational/H12_FINITE_RESIDUAL_2026-11-23.md), with the machine-readable result in [h12_residual_certificate.json](computational/data/h12_residual_certificate.json).

This is finite-level external exact evidence, not an all-level recurrence and not a Lean-kernel theorem. The remaining task is to prove the radius-five corner transport and degree-12 boundary expansion uniformly in m, derive the all-level recurrence with explicit starting index, and formalize the result in Lean.
OPEN_PROBLEMS_APPEND

cat >> CURRENT_EVIDENCE.md <<'CURRENT_EVIDENCE_APPEND'

## 8. H12 finite transition-residual certificate (23 November 2026)

A new exact external CRT computation reconstructs the degree-12 trace-defect residuals C12^(m)=D_(m+1)^(12)-3D_m^(12) for m=3,4,5 from the pinned Evgeny-Theorem graph, orientation, flux, and SU(2) operator definitions at source commit 4ccfae17. The three canonical integer polynomials agree exactly: C12^(3)=C12^(4)=C12^(5). The computation uses primes 10000453, 20000569, and 30000769; the CRT modulus product exceeds twice the explicit coefficient bound. See [the H12 report](computational/H12_FINITE_RESIDUAL_2026-11-23.md) and [the machine-readable certificate](computational/data/h12_residual_certificate.json).

Scope boundary: this establishes equality only for the three computed finite transitions. It does not prove the H12 recurrence for all graph levels and is not a Lean-kernel theorem. A uniform radius-five corner-transport argument, degree-12 boundary expansion, and Lean formalization remain open.
CURRENT_EVIDENCE_APPEND

python3 -m py_compile computational/h12_residual_certificate.py computational/test_h12_residual_certificate.py
python3 -m computational.h12_residual_certificate --output /tmp/h12_residual_certificate.generated.json
cmp /tmp/h12_residual_certificate.generated.json computational/data/h12_residual_certificate.json
python3 -m unittest computational.test_h12_residual_certificate -v
git diff --check

echo "H12 files applied and exact CRT verification passed. No commit was created."
git status --short
git diff --stat
