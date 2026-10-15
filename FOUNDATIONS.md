# Foundations and scope

## Purpose

The project aims to develop a coherent mathematical framework for recursive graph operators, spectral invariants, trace moments, and related computational conjectures. “Theory of Everything” is a programmatic title, not a claim of a completed universal theory.

## Core objects

The source projects currently investigate at least two distinct settings:

1. Graph operators on Sierpiński-gasket approximations with SU(2) edge connections.
2. Signed Z₂-flux graph Laplacians and spectral-decimation / inertia questions.

These settings must be defined separately. Similar geometry or terminology does not imply identical operators, spectra, boundary conditions, or theorems.

## Standards of mathematical claims

A statement is not considered established merely because:
- a finite set of numerical examples agrees with it;
- a test suite passes;
- a fitted parameter yields a small residual;
- a source README describes it informally;
- two different models show superficially similar behaviour.

Every theorem must identify its objects, assumptions, quantifiers, and domain of validity. Every computational result must identify the implementation and reproducible conditions.

## Invariants and trace moments

For an operator H, a trace moment is typically written Tr(H^k), provided the operator and trace are defined in the stated finite-dimensional setting. A moment defect compares the same moment for two explicitly defined operators or configurations. The exact convention for the sign of a defect must be stated at every interface and must remain consistent across code, tests, and documentation.

## Research discipline

- Preserve source links and commit provenance.
- Keep counterexamples and negative results.
- Never silently convert numerical evidence into a theorem.
- Distinguish an implementation bug from a mathematical counterexample.
- When correcting a claim, record the old statement, new statement, reason, and evidence.
