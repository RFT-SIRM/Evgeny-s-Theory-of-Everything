#!/usr/bin/env python3
"""Level-6 higher-moment holdout at theta = 0, pi/2, pi; not a proof."""
import argparse, json, sys
from pathlib import Path
import numpy as np

REF_PI2 = {
  6: [-3180.0, -6956.588745030516, -18274.354980121832, -52227.653685396537],
  8: [-246909.026268397924, -595053.284942481667, -1632052.331668503582, -4743049.471846580505],
  10: [-14013358.982483163476, -37686518.369789719582, -107772338.487565994263, -318029798.840893745422],
}
ANGLES = [0.0, float(np.pi/2), float(np.pi)]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", required=True)
    ap.add_argument("--output", default="artifacts/higher_moment_level6.json")
    args = ap.parse_args()
    sys.path.insert(0, str(Path(args.source_root).resolve() / "src"))
    from operators.operators import build_su2_bundle

    report = {
      "status": "numerical level-6 holdout; not a proof",
      "source_repository": "RFT-SIRM/Evgeny-Theorem",
      "method": "NumPy eigvalsh; Tr(H^p) = sum(lambda^p)",
      "levels": [1,2,3,4,5,6],
      "powers": [6,8,10],
      "angles_radians": ANGLES,
      "results": {}
    }
    for theta in ANGLES:
        values = {}
        for m in range(1,7):
            print(f"theta={theta:.8g}, level={m}", flush=True)
            a, n = build_su2_bundle(m, theta, commuting=False)
            b, nb = build_su2_bundle(m, theta, commuting=True)
            if n != nb:
                raise RuntimeError("Operator vertex counts differ")
            ea, eb = np.linalg.eigvalsh(a), np.linalg.eigvalsh(b)
            values[str(m)] = {f"H{p}": float(np.sum(ea**p)-np.sum(eb**p)) for p in (6,8,10)}
        transitions = {}
        for p in (6,8,10):
            d = [values[str(m)][f"H{p}"] for m in range(1,7)]
            c34 = d[3] - 3*d[2]  # fixed from levels 3 and 4
            transitions[f"H{p}"] = {
              "C_1_to_2": d[1]-3*d[0], "C_2_to_3": d[2]-3*d[1],
              "C_3_to_4": c34, "C_4_to_5": d[4]-3*d[3],
              "C_5_to_6": d[5]-3*d[4],
              "level5_prediction_from_C34": 3*d[3]+c34,
              "level5_actual": d[4],
              "level5_relative_residual": abs(d[4]-(3*d[3]+c34))/max(abs(d[4]),1.0),
              "level6_prediction_from_C34": 3*d[4]+c34,
              "level6_actual": d[5],
              "level6_relative_residual": abs(d[5]-(3*d[4]+c34))/max(abs(d[5]),1.0)
            }
            if abs(theta-np.pi/2) < 1e-12:
                errors=[abs(d[m-1]-REF_PI2[p][m-1])/max(abs(REF_PI2[p][m-1]),1.0) for m in range(1,5)]
                report["pi_over_2_reference_relative_errors"] = report.get("pi_over_2_reference_relative_errors", {})
                report["pi_over_2_reference_relative_errors"][f"H{p}"] = errors
                if max(errors)>2e-9:
                    raise AssertionError(f"H{p} published reference check failed: {errors}")
        report["results"][f"{theta:.12g}"]={"theta":theta,"values":values,"transitions":transitions}
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2,sort_keys=True))
    print("Wrote",out)
if __name__=="__main__":
    main()
