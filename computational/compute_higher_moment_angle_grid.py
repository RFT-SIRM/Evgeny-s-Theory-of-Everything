#!/usr/bin/env python3
"""Angle-grid holdout audit for H6/H8/H10 through level 5; not a proof."""
import argparse, json, sys
from pathlib import Path
import numpy as np

REF_PI2 = {
  6: [-3180.0, -6956.588745030516, -18274.354980121832, -52227.653685396537],
  8: [-246909.026268397924, -595053.284942481667, -1632052.331668503582, -4743049.471846580505],
  10: [-14013358.982483163476, -37686518.369789719582, -107772338.487565994263, -318029798.840893745422],
}
ANGLES = [float(k*np.pi/12) for k in range(13)]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", required=True)
    ap.add_argument("--output", default="artifacts/higher_moment_angle_grid.json")
    args = ap.parse_args()
    sys.path.insert(0, str(Path(args.source_root).resolve() / "src"))
    from operators.operators import build_su2_bundle

    report = {
      "status": "numerical angle-grid holdout; not a proof",
      "source_repository": "RFT-SIRM/Evgeny-Theorem",
      "method": "NumPy eigvalsh; Tr(H^p) = sum(lambda^p)",
      "levels": [1,2,3,4,5],
      "powers": [6,8,10],
      "angles_radians": [float(x) for x in ANGLES],
      "results": {}
    }
    crosscheck_max = {f"H{p}": 0.0 for p in (6,8,10)}
    for theta in ANGLES:
        key = f"{theta:.12g}"
        values = {}
        for m in range(1,6):
            print(f"theta={theta:.8g}, level={m}", flush=True)
            a, n = build_su2_bundle(m, float(theta), commuting=False)
            b, nb = build_su2_bundle(m, float(theta), commuting=True)
            if n != nb:
                raise RuntimeError("Operator vertex counts differ")
            ea, eb = np.linalg.eigvalsh(a), np.linalg.eigvalsh(b)
            values[str(m)] = {f"H{p}": float(np.sum(ea**p)-np.sum(eb**p)) for p in (6,8,10)}
            # Independent numerical route: direct matrix powers on smaller levels.
            if m <= 4:
                for p in (6,8,10):
                    direct = float(np.trace(np.linalg.matrix_power(a, p)).real
                                   - np.trace(np.linalg.matrix_power(b, p)).real)
                    spectral = values[str(m)][f"H{p}"]
                    rel = abs(direct - spectral) / max(abs(direct), 1.0)
                    crosscheck_max[f"H{p}"] = max(crosscheck_max[f"H{p}"], rel)
                    if rel > 5e-9:
                        raise AssertionError(
                            f"H{p} spectral/direct-trace cross-check failed "
                            f"at level={m}, theta={theta}: relative error={rel}"
                        )
        transitions = {}
        for p in (6,8,10):
            d = [values[str(m)][f"H{p}"] for m in range(1,6)]
            c12, c23, c34, c45 = [d[i]-3*d[i-1] for i in range(1,5)]
            pred5 = 3*d[3]+c34
            relative_residual = abs(d[4]-pred5)/max(abs(d[4]),1.0)
            transition_residual = abs(c23-c34)/max(abs(c34), 1.0)
            if relative_residual > 1e-8 or transition_residual > 1e-8:
                raise AssertionError(
                    f"H{p} recurrence check failed at theta={theta}: "
                    f"level5={relative_residual}, transition2to3={transition_residual}"
                )
            if abs(theta) > 1e-12 and abs(c12-c34) < 1e-3:
                raise AssertionError(f"H{p} expected base-transition exception not detected at theta={theta}")
            transitions[f"H{p}"] = {
              "C_1_to_2": c12, "C_2_to_3": c23, "C_3_to_4": c34,
              "C_4_to_5": c45, "level5_prediction_from_C34": pred5,
              "level5_actual": d[4], "level5_residual": d[4]-pred5,
              "relative_residual": relative_residual
            }
        report["results"][key] = {"theta": float(theta), "values": values, "transitions": transitions}
        if abs(theta - np.pi/2) < 1e-12:
            for p in (6,8,10):
                errors = [abs(values[str(m)][f"H{p}"]-REF_PI2[p][m-1])/max(abs(REF_PI2[p][m-1]),1.0) for m in range(1,5)]
                report["pi_over_2_reference_relative_errors"] = report.get("pi_over_2_reference_relative_errors", {})
                report["pi_over_2_reference_relative_errors"][f"H{p}"] = errors
                if max(errors) > 2e-9:
                    raise AssertionError(f"H{p} pi/2 published reference check failed: {errors}")
    report["independent_direct_trace_crosscheck_max_relative_error_levels_1_to_4"] = crosscheck_max
    out = Path(args.output); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("Wrote", out)
if __name__ == "__main__":
    main()
