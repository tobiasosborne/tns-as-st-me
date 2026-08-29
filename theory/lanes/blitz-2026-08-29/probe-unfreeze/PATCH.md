# Anchored merge instructions

Target only: `theory/checks/soft_index_probe.py`.

Baseline target SHA-256: `dae9213a4b6206be331158610f639afd482b8f4b4a1925bafa2c623bb9c919f6`.
Patched lane-copy SHA-256: `b60cb7345fd3c9907c2950859aabff7277915f5f7e74f38d2776dfb8a33e3146`.

Apply these string-anchored edits from the lane copy
`theory/lanes/blitz-2026-08-29/probe-unfreeze/soft_index_probe.py`:

1. At the exact docstring anchor `Mutation discipline: --red mutates the
   frozen P1 prediction`, add the two eta red modes and their nonzero-value
   requirement.
2. Replace the exact constant anchor `SIZES_P3 = (12, 16, 20, 24, 28, 32)`
   with the fixed-`h` multiple-of-five sequence and add `P2_ETA = 0.375`.
3. At `def fail(message: str) -> None:`, insert JSON serialization of the
   current `RESULTS` before the existing print/exit, so firing red gates retain
   their measurements.
4. Between the exact anchors `return mat` at the end of `lowering_matrix` and
   `def gaussian_packet`, insert `lower_at_site` and
   `d24_deformation_on_hard` exactly as in the lane copy.  Their comments cite
   D10(c) and D24(e).
5. In `run_p1`, after the exact row terminator
   `"quick_smoke_only": quick}`, insert the lane-copy assignment that records
   the row before either P1 `require` can fire.
6. Replace the whole block from `def run_p2(red: bool) -> dict:` through the
   return immediately before `# ---------------- P3` with the lane-copy P2
   block.  This computes `(Q[f]|hard>) direct-sum (eta D[f]|hard>)`, projects
   to `H_2`, records norms/sensitivity, and implements both red mutations.
7. Between `current_on_hard`'s final `return vec / (np.exp(1j * k) - 1.0)`
   and `def run_p3`, insert `d29_protocol_datum` exactly as in the lane copy.
   Then replace the whole `run_p3` block through its `return row` with the
   lane-copy version: fixed `h=2*pi/5`, true interacting/free D29 aggregate,
   and serialized row diagnostics.
8. At `def main() -> None:`, transplant the lane-copy allowed-flag set,
   one-eta-mutation check, eta-mode dispatch, and P2 sensitivity print.  Keep
   the remainder of the main loop unchanged.

No other shared file is targeted.  Before/after full outputs are
`before_soft_index_probe_results.json` and `after_green_results.json`; the
four firing red outputs are `red_p1_results.json`, `red_p3_results.json`,
`red_eta_sector_results.json`, and `red_eta_rank_results.json`.
