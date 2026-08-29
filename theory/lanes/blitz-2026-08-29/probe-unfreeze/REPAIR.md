# Probe-unfreeze repair certificate

## ⟨1⟩1. P2(b): the dressed protocol is distinct before projection

**ASSUME.**  The one-hard state is in `H_1`; D10(c) supplies the smeared
broken charge `Q[f]`; D24(e) supplies
`D=S^-_0S^-_1-S^-_1S^-_2+S^-_2S^-_3-S^-_0S^-_3` and its translates.

**PROVE.**  The repaired P2(b) evaluates a genuinely distinct dressed vector,
but its D29 charge-created two-magnon projection is eta-independent.

**⟨2⟩1.**  `Q[f]` lowers once, hence `Q[f]|hard>` is in `H_2`; every term of
`D[f]` lowers twice, hence `D[f]|hard>` is in `H_3`.

*Justification.* D10(c), D24(e), and named computation
`soft_index_probe.py::d24_deformation_on_hard`.

**⟨2⟩2.**  Therefore the computed dressed state is
`Q[f]|hard> direct-sum eta D[f]|hard>` in `H_2 direct-sum H_3`, and its
explicit `H_2` projection equals the bare charge-created state exactly.

*Justification.* D10(c), D24(e), and named computation
`soft_index_probe.py::run_p2`.

**⟨2⟩3.**  The equality is not produced by repeating an expression: at the
two tested momenta the computed `H_3` norms are `5.5020069112` and
`4.9371180144`, while the projected differences and relative eta
sensitivities are both exactly zero.

*Justification.* Named computation `after_green_results.json`, `p2.eta_rows`.

**⟨2⟩4. QED.**

## ⟨1⟩2. P2(b): two independent red paths fire

**ASSUME.**  The green construction of ⟨1⟩1 and the frozen threshold
`P2B_EXACT=1e-10`.

**PROVE.**  The new gate is red-capable through two distinct corruptions of
the sector argument, and each corruption produces measured nonzero
eta-sensitivity before exit.

**⟨2⟩1.**  `--red-eta-sector` applies `Q_0^dagger` to the computed `H_3`
block before projection.  The leaked `H_2` difference is `1.2583935002`,
with relative eta-sensitivity `0.8389290001`, so the gate exits one.

*Justification.* Named computation `soft_index_probe.py --red-eta-sector`
and `red_eta_sector_results.json`.

**⟨2⟩2.**  `--red-eta-rank` changes the D24(e) term from two lowerings to
one.  The erroneous same-sector difference is `1.5000000000`, with relative
eta-sensitivity `1.0000000000`, so the gate exits one.

*Justification.* D24(e), named computation
`soft_index_probe.py --red-eta-rank`, and `red_eta_rank_results.json`.

**⟨2⟩3.**  Both failures serialize their measured rows before `SystemExit`;
the red certificate is therefore numerical rather than inferred from an exit
code alone.

*Justification.* Named computation `soft_index_probe.py::fail` and the two
red JSON files cited above.

**⟨2⟩4. QED.**

## ⟨1⟩3. P3: both recorded defects are repaired

**ASSUME.**  P3 must retain the frozen raw-growth threshold `2.5` and bounded
datum threshold `2.0` while comparing a fixed hard momentum across sizes.

**PROVE.**  The repaired P3 uses the D29 interacting/free datum and keeps
`h=2pi/5` exactly fixed.

**⟨2⟩1.**  The size sequence `(15,20,25,30,35,40)` consists only of
multiples of five, so `hard_idx=N/5` represents `h=2pi/5` at every size.
All six serialized hard momenta equal `1.2566370614359172`.

*Justification.* Named computation `soft_index_probe.py::run_p3` and
`after_green_results.json`, `p3.hard_momenta`.

**⟨2⟩2.**  The smeared value now evolves `Phi(0)=Q[f]|hard>`, Fourier
transforms the interacting and free kernels, divides their pairing by total
free-row mass, and records `|r-1|`.  It never calls the ML4 orthogonal-current
projection used by the frozen implementation.

*Justification.* D10(c) and named computation
`soft_index_probe.py::d29_protocol_datum`.

**⟨2⟩3.**  On the fixed-`h` sequence the raw first/last ratio is
`2.7086235876>2.5`; the D29 values have max/median
`1.4044533952<2.0`.  Thus disease visibility and protocol boundedness both
pass without conflating the two data.

*Justification.* Named computation `after_green_results.json`, `p3`.

**⟨2⟩4. QED.**

## ⟨1⟩4. Full battery and honest scope

**ASSUME.**  Python optimization is enabled so bare assertions, if any, would
not protect a gate.

**PROVE.**  The final copied probe is green on the real model and red on all
four registered corruptions exercised in this lane.

**⟨2⟩1.**  `python3 -O soft_index_probe.py` exits zero.  P1 gives slopes
`1.9929248158` at `S=1/2` and `1.0217264891` at `S=1`; P2(a) remains within
its error band; repaired P2(b) gives zero sensitivity; repaired P3 gives the
values in ⟨1⟩3; P4 remains honestly `geometry-limited` and non-gating.

*Justification.* Named computation `after_green_results.json`.

**⟨2⟩2.**  `--red` exits one with P1 relative error `1.9893872238`, and
`--red-p3` exits one because the disease remains visible under its inverted
gate.

*Justification.* Named computations `red_p1_results.json` and
`red_p3_results.json`.

**⟨2⟩3.**  The two additional P2 mutations exit one with the nonzero values
proved in ⟨1⟩2.  Hence the repaired eta gate has two independent red paths.

*Justification.* Named computations `red_eta_sector_results.json` and
`red_eta_rank_results.json`.

**⟨2⟩4.**  These finite computations repair the falsifier and establish no
infinite-volume D29 limit, no D24 class membership, and no theorem promotion.

*Justification.* Claims `S-IDX-spec-struct-r2` (SKETCH) and
`AC-EX-2M-D29` (SKETCH); PRD status discipline.

**⟨2⟩5. QED.**
