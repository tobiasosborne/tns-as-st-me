STATUS: PROVED-candidate

- Measured all six registered C5b/C6 mutant paths: none reaches `C5b-STABILITY` or `C6-SWEEP`; their wedge/floor and moment/support/liveness shadows are tabulated.
- Added both gates to the copied spec's unreached list and removed the unqualified completeness claim from the spec and checker docstring.
- Added an executable `0 < T < N_BAR/8 = 256` configuration guard; shipped `(20,40)` passes and mutation `(20,256)` is rejected.
- Replaced the stale `notation.md line 271` citation with the content anchor ``the `μ_∞^α` row``.
- Green checker exits 0; all 23 registered mutations and the reachability self-mutation exit 1 with `RED-OK`; both shadowed gates were separately fired.
- `PATCH.md` targets `theory/ace-ld.md` and `theory/checks/ace_ld_check.py`; all copies, scripts, tables, and logs remain in this lane.
