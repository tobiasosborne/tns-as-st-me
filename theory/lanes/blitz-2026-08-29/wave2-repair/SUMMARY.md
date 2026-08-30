# Wave-2 numerics repair — SUMMARY (Opus lane, persisted by orchestrator)

STATUS: DONE — shard 55/55, full suite 3842/3842 green (logs in this dir).

## 1. What the 0.408 was

**(b) finite-size edge–bulk overlap.** Not adiabaticity (the failing sample is
taken at t=0, before any dynamics), not truncation (χ=24 vs 48 differ by
1e-6), not non-quantized physics (|m_L| → 0.4965 at L=64).  The windowed edge
charge obeys ½ − |m_L| ≈ 0.70·e^{−L/2ξ} with fitted ξ = 6.03 sites — the
spin-1 Heisenberg correlation length; fit reproduces every L ≥ 32 to <1%.
The running sum at L=24 peaks exactly at ℓ = L/2, so no window choice
recovers the deficit — only a longer chain.  Diagnostic table:

| L | |m_L| | ½−|m_L| |
|---|---|---|
| 16 | 0.333234 | 0.166766 |
| 24 | 0.407643 | 0.092357 |
| 32 | 0.451133 | 0.048867 |
| 40 | 0.474613 | 0.025387 |
| 48 | 0.486891 | 0.013109 |
| 64 | 0.496518 | 0.003482 |

## 2. What changed

- `MEDGE_HALDANE` NOT lowered; gate still `> 0.45`.
- Edge testset geometry L 24→40 (production geometry; 0.4746 clears the
  gate; L=32 rejected as a 0.0011 margin), χ 24→32 (rank-24 DMRG2 floors at
  residual 1.09e-8 above tolerance: 1607s vs 4.0s), χ_max 32→48.
- NEW cheap testset "the edge half unit is quantised" (ground-state only,
  runs first): m24 < m40 < m64 < ½; m64 > 0.49; 5.0 < ξ_fit < 7.0
  (fitted 6.10).  Would have identified the original failure immediately.

## 3. Counts

Before: 51 pass / 1 fail (test :213).  After: shard 55/55 (11m31.6s), full
suite 3842/3842 (20m47.6s) = 3787 prior + 55 (+3 are the new assertions).

## 4. Memory coefficient (Fig 2/3 data)

Convergence JSON regenerated, ranks [32,48,64]; every coefficient
recomputed independently from raw fields (match to 1e-12):
χ=32: 1.918387433246717; χ=48: 1.918400884863052; χ=64: 1.918404027484692
vs 2s = 1.920679955492809 (0.1185%).  χ 48→64 moves 3.1e-6: CONVERGED.
The WIP's committed χ=32 value agrees with the fresh run to 11 sig figs —
the killed agent's data was genuinely computed.  At χ_max=64:
dx_X2=8.534665379994, nu=−16.372936438215, v_meas=2.134 vs v_th=2.182,
Edrift=2.64e-4.

## 5. Results files

- lambdaD-kink-memory-convergence.json — TRUSTWORTHY (regenerated, 3 ranks).
- lambdaD-edge-memory.json — TRUSTWORTHY, NEW (L=40, χ=48, χ_max=64, t=0..20).
- lambdaD-kink-dispersion.json — unchanged; s-calibration independently
  confirmed (fresh VUMPS 2s identical to committed).
- NOT regenerated: transport + dispersion production stages (~2-3h each);
  lambdaD-kink-memory.json still absent.

## 6. Honest caveat (filed as bead)

Production edge run: m_L exactly frozen for t ≤ 5 (deviation 7.2e-6), then
a magnon front (v ≈ 2.5) crosses the window edge at t ≈ 6, overshooting to
|m_L| = 0.505 > ½ — bulk charge crossing the window, NOT edge-memory decay.
The honest readout window is t ≲ L/(2v) ≈ 5; the module docstring caveats
only the (far longer) edge–edge splitting time.  The record's t=20
retention (0.971) is front-contaminated.  The repaired test's t_end = 3.0
sits in the clean regime.  Production contrast: Haldane |m_L(0)| = 0.4746
vs large-D max 0.00375 (ratio 127).
