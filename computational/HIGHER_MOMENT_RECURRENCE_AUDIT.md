# Audit 001 — higher-moment recurrence constants

**Status:** arithmetic audit of published regression values; not an independent rerun of the operator matrices.

## Question

For each moment power p in {6, 8, 10}, the source project publishes values
\(d_m = \Delta_m(H^p,\pi/2)\) for levels m = 1, 2, 3, 4 and discusses a recurrence

\[
d_m = 3d_{m-1} + C.
\]

The constant implied by a particular transition is

\[
C_{m-1\to m} := d_m - 3d_{m-1}.
\]

If one fixed constant applies starting at m = 2, then the first transition 1→2 must agree with later transitions, within a declared numerical tolerance.

## Arithmetic results

The following values were recomputed using decimal arithmetic from the printed regression table in [Evgeny-Theorem/THEOREM.md](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md). Values below are derived from those displayed decimals; the raw matrix calculations were not rerun for this audit.

| Moment | C₁→₂ | C₂→₃ | C₃→₄ |
|---|---:|---:|---:|
| H⁶ | 2583.411254969484 | 2595.411254969716 | 2595.411254968959 |
| H⁸ | 145673.793862712105 | 153107.523158941419 | 153107.523158930241 |
| H¹⁰ | 4353558.577659770846 | 5287216.621803164483 | 5287216.621804237367 |

## Findings

1. **The first transition is an exception in all three displayed tables.** C₁→₂ differs materially from both later constants for H⁶, H⁸, and H¹⁰.
2. **The second and third transition constants agree closely at the precision of the published values.** This is evidence for a later-level pattern across these two transitions, not proof that it continues for every level or parameter.
3. **The documented H⁶ recurrence range needs correction or clarification.** The source document says the recurrence holds for m ≥ 2. Under the table's indexing, that includes the 1→2 transition, which does not share the later constant.
4. **One test is tautological.** In `tests/test_path_class_h6.py`, `_recurrence_constant(theta)` is defined as `_delta(4, 6, theta) - 3 * _delta(3, 6, theta)`; therefore the test of the 3→4 transition cannot independently verify that transition. The 4→5 test is more informative because it tests a new transition using the constant fixed from levels 3 and 4.

## What this does and does not establish

- It establishes an arithmetic inconsistency between the published level-1-to-4 table and a recurrence claimed to start at m ≥ 2.
- It suggests a candidate recurrence regime beginning with the 2→3 transition for the displayed θ = π/2 values.
- It does **not** prove a recurrence for all levels, all θ, or any exact symbolic formula for C(θ).
- It does **not** independently validate the underlying numerical trace values; those must be regenerated from the operator implementation.

## Required next checks

1. Regenerate H⁶/H⁸/H¹⁰ from the source operator code in a clean environment.
2. Fix C using levels 3 and 4, then predict level 5 without refitting; record residuals for all three powers.
3. Where feasible, test level 6 as a further holdout.
4. Repeat over a preregistered θ grid and include θ = 0 and θ = π.
5. Update the source project's recurrence wording and tests only after the new calculations are run and reviewed.

## Reproduction

From this repository root:

```sh
python3 computational/audit_recurrence.py
python3 -m unittest discover -s tests -p 'test_reference_recurrence_audit.py' -v
```

These commands audit arithmetic over the printed reference table. They do not build the source matrices or prove a theorem.
