# Independent sparse higher-moment holdout through level 7

**Status: local numerical cross-check passed; dedicated CI must pass on the commit. Not a proof.**

## Method

The existing angle-grid and level-6 workflows evaluate traces through Hermitian eigenspectra. This script separately reimplements the Sierpiński graph and SU(2) block-operator construction, then computes traces from sparse matrix powers. It neither imports the source operator builder nor uses eigenvalues. This is an independent numerical evaluation route, not an independent mathematical definition of the model.

## Protocol

- Moments p = 6, 8, 10; levels m = 1,...,7.
- Angles theta = pi/2 and pi.
- Fix C_p(theta) = Delta_4^(p)(theta) - 3 Delta_3^(p)(theta).
- Predict levels 5, 6, and 7 without refitting; inspect the first transition separately.

Reproduce with:

```sh
python -m pip install "numpy>=1.24,<3" "scipy>=1.10,<2"
python computational/independent_sparse_level7.py --output artifacts/independent_sparse_level7.json
```

## Results at theta = pi/2

The sparse trace computation reproduces the published level-1-to-4 values within relative error 4.4e-12 or better.

| Moment | C(1->2) | C(3->4) | Level-7 defect |
|---|---:|---:|---:|
| H6 | 2583.411254969 | 2595.411254969 | -1,376,406.303191 |
| H8 | 145673.793862716 | 153107.523158938 | -126,071,937.938791 |
| H10 | 4353558.577659726 | 5287216.621804237 | -8,518,070,752.620697 |

Relative prediction residuals using C_p fixed from levels 3 and 4:

| Moment | Level 5 | Level 6 | Level 7 |
|---|---:|---:|---:|
| H6 | 3.32e-14 | 2.53e-14 | 2.40e-14 |
| H8 | 0 at displayed precision | 3.54e-15 | 1.18e-15 |
| H10 | 2.01e-15 | 3.36e-16 | 1.12e-16 |

## Results at theta = pi

| Moment | C(1->2) | C(2->3) and later transitions |
|---|---:|---:|
| H6 | 5256 | 5280 |
| H8 | 268960 | 277504 |
| H10 | 4006040 | 4507520 |

The level-7 defects at pi are -3,000,288, -300,230,144, and -22,532,669,440, respectively.

## Interpretation and limits

This strengthens finite numerical evidence for a level-independent recurrence constant from transition 2->3 onward at the two tested angles, through level 7. It reproduces the exceptional 1->2 transition using a numerical route different from the eigenspectrum workflows.

It does **not** derive exact symbolic expressions for C6(theta), C8(theta), C10(theta), explain the exception analytically, or prove the recurrence for all levels and angles. Tiny floating-point residuals are not proof certificates.

Workflow: [Independent sparse level-7 holdout](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions/workflows/independent-sparse-level7.yml).
