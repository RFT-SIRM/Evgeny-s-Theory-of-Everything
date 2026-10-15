#!/usr/bin/env python3
"""Level-5 numerical holdout for H6/H8/H10; not a proof."""
import argparse, json, sys
from pathlib import Path
import numpy as np

REF = {
  6: [-3180.0, -6956.588745030516, -18274.354980121832, -52227.653685396537],
  8: [-246909.026268397924, -595053.284942481667, -1632052.331668503582, -4743049.471846580505],
  10: [-14013358.982483163476, -37686518.369789719582, -107772338.487565994263, -318029798.840893745422],
}
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", required=True)
    ap.add_argument("--output", default="artifacts/higher_moment_level5.json")
    args = ap.parse_args()
    src = Path(args.source_root).resolve() / "src"
    sys.path.insert(0, str(src))
    from operators.operators import build_su2_bundle
    theta = np.pi / 2
    vals = {}
    for m in range(1, 6):
        print(f"Computing level {m}", flush=True)
        a, n = build_su2_bundle(m, theta, commuting=False)
        b, nb = build_su2_bundle(m, theta, commuting=True)
        if n != nb:
            raise RuntimeError("Operator vertex counts differ")
        ea, eb = np.linalg.eigvalsh(a), np.linalg.eigvalsh(b)
        vals[str(m)] = {f"H{p}": float(np.sum(ea**p)-np.sum(eb**p)) for p in (6,8,10)}
    checks = {}
    recurrence = {}
    for p in (6,8,10):
        diffs = [vals[str(m)][f"H{p}"] for m in range(1,6)]
        errs = [abs(diffs[i]-REF[p][i])/max(abs(REF[p][i]),1.0) for i in range(4)]
        if max(errs) > 2e-9:
            raise AssertionError(f"H{p} reference cross-check failed: {errs}")
        c = diffs[3] - 3*diffs[2]  # fixed on levels 3 and 4
        pred = 3*diffs[3] + c
        recurrence[f"H{p}"] = {
          "C_from_levels_3_4": c, "level5_actual": diffs[4],
          "level5_prediction": pred, "residual": diffs[4]-pred,
          "relative_residual": abs(diffs[4]-pred)/max(abs(diffs[4]),1.0),
          "C_from_levels_4_5": diffs[4]-3*diffs[3]
        }
        checks[f"H{p}"] = {"relative_errors_levels_1_to_4": errs}
    report = {
      "status": "numerical holdout only; not a proof",
      "source_repository": "RFT-SIRM/Evgeny-Theorem",
      "source_method": "Hermitian eigenvalues; Tr(H^p) = sum(lambda^p)",
      "theta": float(theta), "values": vals,
      "published_reference_checks": checks,
      "recurrence_holdout": recurrence
    }
    out = Path(args.output); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("Wrote", out)
if __name__ == "__main__":
    main()
