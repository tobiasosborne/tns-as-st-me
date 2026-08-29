<!-- ROLE: proposer response to theory/verdicts/lr-d16-r2.md, repair round 3.
     Lane: theory/lr-d16.md, this file, theory/checks/lr_d16_check.py only.
     claims/CLAIMS.md and notation.md were read but not edited.  No commit. -->

# (LR) for D16 — response to critic r2, repair round 3

All four MAJOR objections are adopted.  The positive conclusions fenced by
the critic survive: `LR1-GEN` and `LR-D16-EDW` remain PROVED on the exact DAG
wording, D27(LR2) remains OPEN, and D27(LR3) remains conditional on the
two-clause (NR).  The negative layer is weakened: no retraction is asserted
more strongly than the available proof.

## 1. Disposition

| critic id | disposition | repair |
|---|---|---|
| M1 | **ADOPTED** | MP-4 retains its first sentence and uses the r2 critic's replacement second sentence verbatim: one clause proved, one still open with residue (DPH), one reduced to a named two-clause hypothesis. |
| M2 | **ADOPTED** | Every claim that (ESC) is false, or was proved false, is removed.  The shard now says (ESC) is unavailable without D18(AD1)--(AD3).  The withdrawal of (LR2′) rests on its undischarged antecedent and on the sampled bound being weaker than the free bound at five of six times under both finite-volume propagators. |
| M3 | **ADOPTED** | C2(d) and C3(e) now use `H_XXZ`, gate `H_XXZ` energy conservation, and have registered `H_kink` reversion mutants.  Their captions and conclusions are weakened to exactly what the corrected data show.  No propagator or constant was tuned to preserve the r2 verdict. |
| M4 | **ADOPTED** | `ACE-LD-obst′` is identified as an unpromoted merge proposal in a shard at `FAIL(F1,M1--M6)`, with no exhibited (M-ESC) model/state.  It identifies a hypothesis a class theorem would have to contend with; no necessity claim remains. |

## 2. Corrected `H_XXZ` numerical record

The two r2 load-bearing diagnostics change exactly as the critic reported.

### C2(d)

With `H_XXZ`, `N=12`, `Δ=2.5`, `c_0=6`, `t∈[-40,40]` on 201 samples:

| window | outside sites | `G` | `η=4R_W√G` | r3 reading |
|---|---:|---:|---:|---|
| `[4,9]` | 6 | `0.989` | `11.9` | finite-volume inner-window `O(1)` sample |
| `[3,10]` | 4 | `0.949` | `15.6` | finite-volume inner-window `O(1)` sample |
| `[2,11]` | 2 | `0.278` | `10.5` | display only; no escape information |

Thus the r2 monotone/increasing certificate is gone.  The row gates only the
two inner-window observations and explicitly labels `W_3` display-only.  It
does not claim an exhaustion limit or evidence for/against (ESC).

At `W=[4,9]` and `t_-=0,-2,-5,-9,-20,-40`, the `H_XXZ` sharpness values are
`ε=0.837,0.994,0.812,0.417,0.565,0.544`, hence
`4R_Wε=10.0,11.9,9.7,5.0,6.8,6.5`: five of six exceed the free bound
`2‖Q̂_W‖=6`.  The old `H_kink` cross-check gives
`ε=0.837,0.995,0.969,0.363,0.692,0.872` and likewise five of six exceed `6`.
This comparison is the withdrawal ground; it is not an asymptotic claim.

### C3(e)

With `H_XXZ`, the pinched terms are

`1.607 / 1.670 / 1.747`, with spread `0.140` and spread/mean `0.084`.

The old `spread>0.40` certificate fails.  The repaired row tests only relative
variation above numerical tolerance and imposes no ordering condition.  This
is a finite-sample display of `m`-dependence, not a numerical proof that
`sup_m` is necessary.  The analytic reason `sup_m` stays is proof-theoretic:
the monotonicity lemma fixes the observable but does not derive a uniform
bound over the `m`-dependent pinched states.

Both rows conserve `H_XXZ` energy (`2.18e-14` and `9.77e-15` maximum drift on
their respective grids).  Their new `c2-kink-propagator` and
`c3-kink-propagator` mutants are caught by energy drifts `1.03` and `0.705`,
respectively, on exactly their registered rows.

## 3. Checker residues

- C1(b) now gates only raw spectral integrality.  Its `ν`-integrality and
  support computations, both derived from the same spectral blocks, are
  labelled DISPLAY and removed from the acceptance conjunction.  The support
  theorem itself remains proved analytically at ⟨1⟩3.⟨2⟩4--⟨2⟩6.
- C3(d) is no longer an evidence row.  It is labelled DISPLAY as deductively
  subsumed by C3(b)+C3(c); under `H_XXZ` its majorant exceeds C3(b)'s by at
  least `5.490e-4` over the registered samples.
- Green mode has 16 evidence rows plus the two displays.  `--red-all` runs
  every mutant over the full 16-row suite and reports `RED-OK 18/18`: each
  mutant reaches exactly its registered singleton with no collateral failure
  or masking.  There are no bare `assert` statements, so `python3 -O` is
  strict.

## 4. DAG lockstep

The shard now matches the two already-PROVED rows in `claims/CLAIMS.md`:

- ⟨1⟩3 assumes only existence of the strongly continuous dynamics and
  `‖Ψ‖=1`; ⟨1⟩6 states `LR1-GEN` for every prescribed sequence and expressly
  excludes pointwise and full-sequence convergence.
- ⟨1⟩5.⟨2⟩6 uses the promoted notation `P^{DW}_x`, `N_{DW}`.  Its operator
  inequality is unconditional, while the time-uniform expectation conclusion
  carries finiteness and conservation of `E_0` as hypotheses on the selected
  state, exactly as the critic's DAG cell does.
- The historical caveats embedded in the immutable DAG cells are discharged
  here: ⟨1⟩3 no longer over-lists (H3), the shard no longer writes `N_{DW}` as
  `D`, and ⟨1⟩5.⟨2⟩6 no longer asserts finiteness/conservation without proof.
  Per the work order, the DAG itself was not edited.
- MP-3 is marked APPLIED rather than re-proposed; the DAG cells are named as
  authoritative.  `LR-D16` remains HOLD.

## 5. Resulting honest headline

`M-INDEX-spec` still has no fully unconditional dynamical instance.  For D16,
LR1 is unconditional and in fact the class theorem `LR1-GEN`; LR2 is OPEN at
(DPH), with the r1 (LR2′) route withdrawn because (ESC) is unavailable; LR3 is
conditional on the named two-clause (NR).  The class-level contribution beyond
`LR1-GEN` is an inventory, not a counterexample and not a necessity theorem.
