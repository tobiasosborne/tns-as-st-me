#!/usr/bin/env python3
# Cross-lane verification: Corner B analytic kink-magnon reflection
#   R(k;Delta) = x/(1+x),  x = J^4/(16 omega^2 v^2),
#   omega = J(Delta - cos k), v = J sin k   (J = Jperp = 1)
# (theory/corner-b-draft.md, <=3-wall projection) against the INDEPENDENT
# sparse-sector scan numerics/results/memory-scan-1.json (WP N2a).
# Pass criterion fixed in advance: every 'main-*' and 'Dscan-*' run agrees
# within 8% (finite-packet-width corrections shrink with k0 and Delta).
import json, math, sys
d = json.load(open('numerics/results/memory-scan-1.json'))
bad = 0
for run in d['runs']:
    lbl = run['label']
    if not (lbl.startswith('main-') or lbl.startswith('Dscan-')):
        continue
    res = run['result']; p = res.get('params', res)
    D, k = float(p.get('Delta', p.get('delta'))), float(p.get('k0'))
    Rv = res.get('R', res.get('reflection'))
    Rm = float(Rv if Rv is not None else res['observables']['R'])
    w, v = D - math.cos(k), math.sin(k)
    x = 1.0 / (16 * w * w * v * v)
    Rp = x / (1 + x)
    ok = abs(Rm / Rp - 1) < 0.08
    bad += (not ok)
    print(f"{lbl:18s} D={D:4.1f} k0={k:4.2f} R_meas={Rm:8.5f} R_pred={Rp:8.5f} ratio={Rm/Rp:5.3f} {'ok' if ok else 'FAIL'}")
if bad:
    print(f"FAIL: {bad} runs outside 8%"); sys.exit(1)
print("PASS: analytic t(k) (corner-b-draft) matches independent XXZ scan on all main/Dscan runs")
