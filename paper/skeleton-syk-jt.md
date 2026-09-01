<!-- SKELETON ONLY — SYK/JT companion paper (bd tns-wvp).
     PI directive 2026-08-31: BULLET POINTS ONLY, no prose paragraphs, every
     bullet <= 2 lines.  TJO writes all prose personally (L7 amended: no Fable
     prose writer for this deliverable).  This file is a VALUE GATE: every
     content bullet names its claim id / D-number / verdict file / arXiv id.
     A bullet tagged [UNBACKED] has no ledger backing and is a gap, not a plan. -->

# Skeleton — SYK/JT companion: the finite, relational infrared triangle

## Header

- **Thesis.** In nearly-AdS2/SYK the infrared triangle assembles but degenerates: the symmetry corner is finite, and memory survives only in the calibrated relational register D33, not the absolute register D32.
- **Candidate title 1.** *A Finite Infrared Triangle in Nearly-AdS2*
- **Candidate title 2.** *Relational Memory in the Schwarzian*
- **Candidate title 3.** *Two Registers of Memory in SYK*
- **Venue/length.** Short paper, PRL-companion register (apsrev4-2, ~4 pp main text + appendices); prose target arXiv:1305.2176 per `docs/prose-guide.md`.
- **Standing scope fence.** All positive results are Schwarzian-EFT statements in the *energy-balanced* sector, large-`C`-first window (`theory/verdicts/syk-jt-joint-critic-r2.md` §8 + r2a).

## Abstract skeleton (one bullet per sentence-slot)

- **S1 — setting.** Two-boundary nearly-AdS2/SYK as a 0+1d instance of the infrared-triangle question; observables fixed as an algebra first (`theory/lanes/syk-jt/observables-spec.md`, Layers 0–2).
- **S2 — the decisive computation.** A compact energy-balanced boundary pulse gives a calibrated relative-clock susceptibility equal, at `O(C^{-1})`, to the `ω→0` DC residue of the same soft attachment [JT-B-susc].
- **S3 — the negative half.** The absolute stationary-subtracted two-sided correlator has no nonzero late plateau in that window [JT-noplat-abs]; the pure Shenker–Stanford shift has zero plateau [JT-bfly-decay].
- **S4 — the definitional payload.** Two registers: absolute-response memory D32 vs calibrated relational memory susceptibility D33; the gravity instance passes D33 and fails D32.
- **S5 — the structural reason.** A thermal reference frame erodes its own record: numerator and denominator decay together, so readout cost grows exponentially in detector time (D33).
- **S6 — the symmetry corner.** The first non-Möbius mode is a broken kinematic tangent, not a charge [JT-A-tangent]; finite-grid ED refutes the two implemented candidate families only [JT-A-ward-grid].
- **S7 — honest limits.** Finite-`N` ED and the EFT window do not overlap at accessible sizes (labbook §19 "microscopic check", `numerics/results/syk_ed.json`); the matter-dressed route is open.

## §1 Introduction

- The triangle vocabulary and its three corners as the definitional baseline — cite **1703.05448** in the opening sentence that names soft theorem / asymptotic symmetry / memory.
- The transplant genre is crowded and active: cite **1709.05018** (pions), **2310.16683** (fractons), **2512.15796** (sound), **2411.13633** (3d), **2412.16142/2412.16149** in the same sentence that says the move is not new.
- **C5 phrasing fence.** Say "the first assembly for a 0+1d / nearly-AdS2 system"; never "the first triangle beyond X" — 2310.16683 owns that phrasing (deep sweep §1 C5).
- Cite **2201.05054** (Pasterski–Verlinde, "Mapping SYK to the sky") in the same paragraph as C5's first-ness claim, noting it runs the opposite direction (deep sweep Appendix).
- **C1 obligation.** Cite **2305.14411** and **1809.07266** in the FIRST paragraph that makes the memory claim — first-ness for "shockwave = memory" is not available (deep sweep §1 C1).
- Evidence for the negative claim C5: citer-set intersection 2411.13633 ∩ 2112.14609 = {2603.12902, 2412.05038}, both read, neither a counterexample (deep sweep §2).
- Quantitative C5 support, stated as absence of evidence not proof: only ~30 papers cite both 1703.05448 and the SYK founding papers; none poses the triangle (deep sweep Appendix).
- Contribution list, in order: the decisive computation [JT-B-susc, JT-bfly-decay, JT-noplat-abs]; the D32/D33 split; the finite symmetry corner [JT-A-* rows].

## §2 Setup and allowed observables

- The operational razor stated first: physically allowed observables must be specified or the memory question is ill-posed (`theory/lanes/syk-jt/observables-spec.md` header).
- **Layer 0.** Finite `N`: the fermion-parity-even part of the CAR algebra of 2N Majoranas; a single Majorana is not an observable (observables-spec Layer 0).
- **Layer 1.** Uniformly normalized even bilocals `(1/N)Σ_i ψ_i^X(t)ψ_i^Y(t')`, their finite products, and `H_L, H_R`; predictions are `N→∞` limit points with declared `1/C` errors.
- **Layer 2.** Mathematical home only, not load-bearing: emergent type III_1 one-sided factor (**2110.05497**), JT boundary algebra as crossed product with SL(2) constraint (**2301.07257**).
- **Exactly conserved allowed charges.** `E_L, E_R` and fermion parity — the ONLY ones after the pulse; this is what makes protocols "comparable" in the sense of D32.
- **Explicitly NOT observables.** The reparametrization field `f(u)`/`t(u)`, any relative Möbius frame label, and the non-energy Schwarzian charges `Q^a` (observables-spec "Explicitly NOT observables").
- **Limit-order convention, stated once and used everywhere.** `C→∞` first, then `1 ≪ κT ≪ κC` (invariantly `κT→∞` with `T/C→0`) (observables-spec "Consequences", critic r1 Objection 6).
- Cite **1606.01857** (verified TeX `GravityReparametrizationsRevised.tex`) for `Diff(S¹)→SL(2,R)` breaking and the Schwarzian boundary action; **2412.14799** for the large-`p` soft-mode action.
- Cite **1306.0622** as the object the paper re-reads (the Shenker–Stanford shock), at the point the shock protocol is introduced.

## §3 The decisive computation

- **Result 1 [JT-B-susc].** `Δu_rel = [2Cκ²]^{-1}∫(u−u_*)P(u)du + O(C^{-2})` at leading one-soft/tree order, for a compact energy-balanced right-boundary power pulse with a single synchronization event `u_*`.
- **Result 1, second clause [JT-B-susc].** It "equals at that order the `ω→0` DC residue of the same invariant bilocal soft attachment" — the DC identity, at that order only.
- **Result 1, scope, verbatim [JT-B-susc].** "the `O(C^{-2})` remainder is controlled here only at fixed detector time, and neither a uniform finite-`C` late-time bound nor practical permanence is claimed."
- **Result 1, exclusion [JT-B-susc].** "Exact finite-amplitude equality to a single-soft vertex is excluded" (critic r2 §8(i), (4.13)–(4.14)).
- **Result 2 [JT-noplat-abs].** The `u_*`-synchronized same-energy absolute correlator difference `δG_LR(T) = 𝒩_Δ κ^{2Δ} e^{−2Δκ(T−u_*)}[a^{−2Δ}−1+O(e^{−κ(T−u_*)})]`, every `Δ>0`.
- **Result 2, scope, verbatim [JT-noplat-abs].** "no nonzero late plateau in the large-`C`-first window even when its calibrated ratio approaches a nonzero susceptibility"; balanced sector only.
- **Result 3 [JT-bfly-decay].** For `g_shock=(1 α; 0 1)`, `Δu_rel^NL(T) = −ακ^{-1}e^{−κ(T−u_*)}+O(e^{−2κ(T−u_*)})` and `δG_LR(T)=O(e^{−(2Δ+1)κ(T−u_*)})`; zero plateau.
- **Result 3, framing sentence [JT-bfly-decay].** "The celebrated butterfly frame shift is a transient relational time delay, not stationary-subtracted memory."
- **C2 obligation.** Cite **2604.19866** and **2512.02825** as the flat-space statement of the memory↔soft Fourier pairing, in the sentence that states the DC identity — the structure is textbook; the nAdS2 realization is ours.
- **C2 obligation.** Cite **1608.05687**, **1704.05333**, **1804.00491** (and **1804.09834**, **1707.02325**) as prior computations of the same shift by a different route, at the point the shift is introduced.
- **C2 evidence, now discharged.** `refs/LEDGER.md` Batch 11: full-text grep of all five for zero-frequency/DC/Kubo/susceptibility/static-response/`ω→0` found no such identification; zero "memory" mentions.
- **C1 obligation.** Cite **2603.18509** at the point of the numerical adjudication — a published transient-not-permanent result for a driven two-sided SYK time delay (deep sweep §1 C1).
- **Switchback lineage.** Cite **1406.2678** (true switchback origin, per LEDGER §7) and **2304.15008 / 2406.04397 / 2506.19013**, noting none states the late-time decay-vs-plateau of the shift.
- **Do NOT cite 1408.6560 as a switchback paper** — confirmed title mismatch (deep sweep §7, `refs/LEDGER.md`).
- Provenance for the numbers: `theory/lanes/syk-jt/t1-analytic.md` ⟨1⟩2–⟨1⟩5 (analytic), `numerics/results/schwarzian_memory.json` (numeric), `numerics/test/test_schwarzian_memory.jl` (96 green).

## §4 The two registers of memory

- **D32 (absolute-response register).** A comparable pair exhibits memory iff a single allowed observable, fixed in advance with `T`-independent norm bound, has a nonzero late-time expectation difference.
- **D32 fence.** "The word 'memory' without qualifier is reserved for this register throughout the campaign" (definitions.md D32).
- **D32 comparability.** Two protocols are comparable when they agree on every exactly conserved allowed charge of the specification — here `E_L, E_R`, parity (D32 + observables-spec §3).
- **D33 (calibrated relational memory susceptibility).** Ratio/finite combination of allowed expectations, with measurement cost declared as part of the claim; three conditions (i)–(iii) of D33.
- **D33 condition (iii).** The limit equals the declared zero-frequency (DC) datum of the corresponding soft-theorem statement, normalization fixed by measured injected charge, nothing fitted.
- **D33 fence.** "Satisfying D33 does NOT license the unqualified word 'memory' (D32)"; the adjudicated D33-without-D32 instance is exactly [JT-B-susc] + [JT-noplat-abs].
- **The structural reading (D33 closing sentences).** A thermal reference frame erodes its own record; readout cost grows exponentially in detector time.
- **The cost, quantified** (`schwarzian_memory.json` `detector_window`; critic r2 §5 O6): `M_shots = O(e^{4Δκ(T−u_*)}/η²)`, with a stored maximum usable detector time per row.
- **The coincidence criterion (D33).** GW strain is the paradigm D33 functional that also passes D32 because its calibrating denominator does not decay — "the two registers coincide exactly when the ruler is persistent."
- **Contrast with the lattice campaign.** The chain's kink memory passes the strong register at fixed cost because its two asymptotic endpoints share no horizon (labbook §19 "two registers" paragraph).
- **C4 obligation — comparison, not citation.** Survive a direct comparison with the FGHN persistent-observable programme **1901.00021**, **1912.13449**, **2109.03832**; a referee will ask why the registers are not a special case.
- **C4 obligation.** Cite **2601.23019** in the same paragraph as D33 — closest published statement of the calibration register ("detectors are intrinsically insensitive to the final offset").
- **C4 obligation.** Differentiate from the displacement-vs-velocity two-register split **2406.07106 / 2402.02594**, and from detector-dependence **2608.09295**, where D33's registers are named.
- **C4 obligation.** Distinguish from **2308.02445** (finite-`T` soft theorems = thermal *corrections* to soft factors, explicitly not erosion of the record) at the thermal-erosion claim.
- **C4 obligation.** Cite **2312.10454** (memory as a quantum-noise floor) where the measurement-cost argument is made; cite **1912.12806** as precedent for a published memory-vs-charge structural tension.

## §5 The symmetry corner

- **Structural fact + four prior formulations in ONE sentence.** Infinite naive reparametrization symmetry, finite surviving algebra: cite **1708.08471 / 2005.08999 / 2108.04841 / 2603.18154** together (deep sweep §1 C3).
- **C3 fence.** Do NOT present "only SL(2) survives" as a discovery; restate as a sharpened, quantified version of a known structural fact (deep sweep §1 C3).
- **C3 fence.** Cite **1904.12820** (Lin–Maldacena–Zhao exact SL(2) generators vs approximate constructions) — pass-1 sweep PRIORITY; a referee who knows it will ask why this is not a restatement.
- **C3 universality bound.** Phrase as "a finite subalgebra set by the isometry content", with plain JT/SYK giving SL(2,R); cite **2503.13680**, **2506.02629**, **2410.10768**, **2204.09685** in that sentence.
- **Result [JT-A-tangent].** The Bucca–Mezei Ansatz mode-2 tangent `V_{2,c}γ_* = 2 sin(2τ̄)(1−cos d)`, inducing `dG/ds = sgn(d)V_{2,c}γ_*/(2p) + O(p^{-2})`.
- **Result [JT-A-tangent], scope, verbatim.** "an explicitly broken kinematic response of allowed bilocal expectations, not an affiliated charge, finite-`N` operation, or controlled Ward identity."
- **Wording fence [JT-A-tangent].** No "charge", "memory", "symmetry generator", "conserved" or "permanent" wording may attach to this row (`theory/verdicts/g3-wave-critic-r1.md` §8.2).
- **Result [JT-A-ward-grid].** `q=4` two-dot ED, `N_m=8,10,12`, `βJ=5,10`, three seeds, `δJ=0.15`: projected relative Ward defects `0.5501 ≤ d_N ≤ 1.0124`, constant-model fits, no decay with size.
- **Result [JT-A-ward-grid], scope, verbatim.** "finite-grid evidence against only those two candidate definitions, not a universal non-Möbius-charge no-go"; the `n=1` control defects are also not small.
- **Result [JT-A-uv-noexact].** No exact mode-2 charge implements the literal primary reparametrization rule on a diagonal-stable same-side finite-`N` UV core; defect uniform and contact-localizing.
- **Result [JT-A-purejt].** In pure JT (no matter) all affiliated adjoint actions are trivial beyond functions of the Hamiltonian — "pure JT ONLY; supplies no matter-coupled no-go".
- **Result [JT-A-notconserved].** `[δ_1, δ_{ε^L_{2,c}}] = −2δ_{sin 2t} ≠ 0`; does not exclude a nonconserved or controlled approximately conserved implementer.
- **Result [JT-A-baredescent].** The bare nonzero-weight mode-2 constraint expression does not descend through the diagonal SL(2) constraint; dressed constraint scalars remain open.
- **The 2409.15415 defusal, stated explicitly.** Its ideal-observer construction is state/trajectory estimation of `f(u)`, and the paper itself notes `f(u) ≠ H_f` unless `Sch(f,u)=0` (deep sweep §1 C3).
- **Nearest methodological neighbours for the finite-`N` numerics.** Cite **2002.05725** (ED to N=60, Lyapunov/OTOC not Ward defects) and **2102.06647** (analytic finite-`N` reparametrization action).
- **Watch item, recheck at submission.** **2602.14079** (discrete BF JT, lattice-level asymptotic symmetry algebras, revised Aug 2026) — nearest neighbour to the lattice angle; not a triangle today.

## §6 Discussion

- The triangle in 0+1d assembles but degenerates: finite symmetry corner, D33-only memory corner, DC identity at `O(C^{-1})` — one sentence, each half carrying its claim id.
- The honest negative, stated in the main text not buried: EFT and ED windows do not overlap at accessible sizes, so the ED neither supports nor refutes [JT-B-susc, JT-bfly-decay, JT-noplat-abs].
- Single-realization stability is not yet present: the calibrated ratio is not self-averaging at `N_m=10,12` (`numerics/results/syk_ed.json` `self_averaging`, spread comparable to mean, sign flips).
- The general lesson worth exporting: memory needs a persistent ruler; where the reference frame thermalizes, the triangle survives only in the susceptibility register (D33).
- Positioning close: the transplant move is old, the target is new (deep sweep §1 C5); the honest residual is the matter-dressed/relational route, named as open by both analytic lanes.

## Figure slots

### Figure 1 — the decisive computation (`numerics/results/schwarzian_memory.json`)

- Panel (a): `delta_G_LR(T)` on `late_time_grid = [2,5,10,20,40]` for the two balanced rows (`profile = derivative_gaussian_balanced`, `C = 10, 100`); log axis showing exponential decay [JT-noplat-abs].
- Panel (b): `delta_u_rel(T)` on the same grid, same two rows, approaching its plateau (`fitted_mobius_tail`); the D33 register beside the failed D32 register [JT-B-susc].
- Panel (c): `dc.residue_ratio` vs `dc.omega = [0.2,0.1,0.05,0.025]` with the `ω²` linear intercept; `extrapolated_vertex_ratio` = 1.000110 (`C=10`), 0.999988 (`C=100`) — "0.011% or better" (critic r2a).
- Caption fence, mandatory: the other six rows (`top_hat`, `gaussian`) are formal Schwarzian trajectory/DC diagnostics and license no operational detector conclusion (critic r2a, Objection 9).

### Figure 2 — the two registers and their cost (`schwarzian_memory.json` + `numerics/results/syk_ed.json`)

- Panel (a): D32 vs D33 on one axis from the two balanced rows — `delta_G_LR` decaying against `delta_u_rel` flat; annotate with D33's coincidence criterion ("the ruler is persistent").
- Panel (b): the D33 cost clause, from `schwarzian_memory.json` `detector_window` — model `M_shots ~ exp(4ΔκT)/η²`, `maximum_usable_T = 3.16`, `sample_cost_for_10pct_late_delta = 8.36e13` (balanced `C=10`).
- Panel (c): the honest negative — `syk_ed.json` `fits.delta_g_absolute.winner` per row, and `self_averaging` plateau mean vs std at `N_m=8,10,12`, `βJ=5,10`, 5 seeds (labbook §19).

### Figure 3 — the symmetry corner at finite `N` (`numerics/results/syk_ward.json`)

- Panel (a): `main_rows` (216) projected relative Ward defect vs `N_m ∈ {8,10,12}` for both candidates, `βJ=5,10`, 3 seeds, 3 probes; band `0.5501–1.0124`, constant-model fits [JT-A-ward-grid].
- Panel (b): the two controls that make the negative honest — `n0_control.maximum_relative_defect = 2.06e-16` (machine precision) and the 108 `n1_control_rows` whose defects are also not small.
- Caption fence, mandatory: finite-grid evidence against those two candidate definitions only; not a universal non-Möbius-charge no-go [JT-A-ward-grid; g3-wave-critic-r1 §8.3].

## NOT claimed (held, retracted, or explicitly excluded)

- **The strong `n=2` refutation is NOT claimed.** "the strong operational Diff-charge corner A fails at its first non-Möbius mode" is unlicensed — HOLD, `theory/verdicts/g3-wave-critic-r1.md` §8.1.
- Reason the strong form fails (all three, state them): source-closure audit is not a nonexistence theorem; analytic no-gos have a matter-coupled scope gap; the `n=1` control is not small (g3-wave-critic-r1 §8.1, §5.4).
- **Unbalanced-protocol detectors are NOT claimed.** The six unbalanced rows are formal diagnostics only; the T2 "all eight" generalization is HELD (`theory/verdicts/syk-jt-joint-critic-r2.md` §7 Objection 9 + r2a).
- **The all-profiles generalization of [JT-noplat-abs] is HELD** — no implementable unequal-energy reference protocol exists yet (CLAIMS.md JT-noplat-abs; critic r2 Objection 9).
- **Practical permanence is NOT claimed.** [JT-B-susc] excludes "a uniform finite-`C` late-time bound" and "practical permanence"; the `O(C^{-2})` remainder is controlled only at fixed detector time.
- **Exact finite-amplitude equality to a single-soft vertex is excluded** (critic r2 §8(i), (4.13)–(4.14)) — the DC identity holds at leading one-soft/tree order.
- **A universal no-go for non-Möbius charges is NOT claimed.** [JT-A-purejt] is pure-JT only and "supplies no matter-coupled no-go"; [JT-A-notconserved] does not exclude a nonconserved implementer.
- **No dressed-constraint statement is claimed.** [JT-A-baredescent] is bare mode only (g3-wave-critic-r1 §8.4).
- **`G3-O` claims nothing.** Relabelled "source-closed insufficiency audit"; algebraic non-descent is not independently proved (g3-wave-critic-r1 r1a, §8.4 table).
- **`G3-LL-NOCLOSURE` is NOT a result.** HOLD as G3, retained only as conditional on the LL type-III_1 conjecture plus G4-strength hypotheses (g3-wave-critic-r1 §8.4).
- **No finite-`N` permanence claim.** `syk_ed.json` `conventions.limit_scope`: "no finite-N permanence claim; compare only structurally to large-C-first EFT."
- **No first-ness for "shockwave = memory"** (2305.14411, 1809.07266) and **none for "the two-sided SYK time delay is transient"** (2603.18509) — deep sweep §1 C1.

## Open problems stated in the paper

- **The matter-dressed / relational route.** A matter-dressed or relational nonconserved implementer on a fixed separated/heat-regulated core — built by no lane, excluded by no lane (g3-wave-critic-r1 §8.4 "OPEN").
- **The equal-energy reference protocol.** No implementable unequal-`(E_L,E_R)` reference exists, which is exactly what holds the all-profiles generalization of [JT-noplat-abs] (critic r2 Objection 9).
- **The Liouville rung.** Redo the decisive computation in the large-`p` collective/Liouville theory, then at fixed disorder, then on the chain (labbook §19; `o4-syk-jt-recon.md`:634).
- **The `β`-sweep / vacuum limit.** Named a strengthener, not a gate, in bd `tns-wvp`. [UNBACKED — no claim row, no verdict, no data file; state as future work only]
- **C5 itself has no claim row.** "First assembly for a 0+1d system" is a novelty verdict of `docs/syk-jt-novelty-sweep-deep.md`, not a PROVED claim — label it as a literature statement, never a theorem.
- **The window-overlap problem.** A quantitatively matched EFT/ED window, or larger `N_m`, is the only route from the honest negative to a microscopic test (labbook §19 "honest negative").
- **Self-averaging.** A single-realization or self-averaging statement is required for a genuinely operational claim and is absent at these sizes (`syk_ed.json` `self_averaging`; labbook §19).

## Positioning fences (one per novelty landmine)

- **C3 repositioning.** Cite **1708.08471 / 2005.08999 / 2108.04841 / 2603.18154** in the sentence stating the structural fact; ours is the all-`N` obstruction framing, the protocol framing, and the measured defect.
- **PW conflation fence.** **2301.07257**'s type-II∞-with-matter result sizes the observable algebra; it does not say which asymptotic charges exist. Our finiteness does not contradict it — say so.
- **PW usage fence.** [JT-A-purejt] rests on `refs/arxiv-2301.07257` `Paper.tex:751-769` and is pure-JT only; the matter case is exactly where the type-II∞ algebra lives.
- **The 2409.15415 defusal.** Say explicitly that its weak-measurement observer estimates the mode `f(u)`, not a conserved non-Möbius charge, and that the paper itself notes `f(u) ≠ H_f` unless `Sch(f,u)=0`.
- **The Pasterski–Verlinde reverse-direction note.** **2201.05054** maps SYK to the celestial sphere (SYK as a toy model of the 4d soft sector); ours runs the other way — must-cite, non-overlapping (deep sweep Appendix).
- **C5 phrasing fence.** "First assembly for a 0+1d / nearly-AdS2 system", never "first triangle beyond X"; **2512.15796** is inside the window and must be re-checked at submission.
- **C1 first-ness fence.** The framing move and the transience verdict both have precedent; our claim is the AdS2/JT/SYK instantiation, the memory-theoretic adjudication, and the calibrated-ratio residue.
- **C4 comparison fence.** FGHN persistent observables must be *beaten*, not merely cited: say why the two registers are not a special case of persistent observables.
- **Genre fence.** **2412.16142 / 2412.16149** show "assemble the remaining corner" is a recognized genre — cite them so the contribution is not mistaken for a claim of methodological novelty.

## L3 gate — citation obligations with NO local TeX yet

**DISCHARGED 2026-09-01 (refs Batch 13, bd tns-8gu):** every id listed below
is now fetched and title-verified in `refs/` — see `refs/LEDGER.md` Batch 13.
One correction found in the process: the C3 universality-bound citation
**2201.03650 was the WRONG id** (it is a BKT-transitions paper); the intended
Kruthoff higher-spin JT paper is **2204.09685** (fetched, verified; this file
and the deep-sweep doc corrected in place). Original obligation list kept for
provenance:

- Not in `refs/`: **2604.19866**, **2512.02825** (both load-bearing for the C2 framing sentence).
- Not in `refs/`: **2201.05054** (must-cite, Pasterski–Verlinde reverse-direction note).
- Not in `refs/`: **2503.13680**, **2506.02629**, **2204.09685** (three of the four C3 universality-bound ids; 2410.10768 is local; NOTE: 2204.09685 replaces the wrong id 2201.03650 recorded pre-batch-13 — see refs/LEDGER.md Batch 13).
- Not in `refs/`: **1406.2678** (switchback origin), **2304.15008**, **2406.04397** (2506.19013 is local).
- Not in `refs/`: **1912.13449** (FGHN), **2608.09295**, **2402.02594**, **2312.10454**, **1912.12806** (C4 comparison set; 1901.00021, 2109.03832, 2601.23019, 2406.07106 are local).
- Not in `refs/`: **2002.05725**, **2102.06647** (C3 finite-`N` methodological neighbours), **2412.16142 / 2412.16149**, **2602.14079** (watch item), **2307.15725**.
- Unresolved LEDGER conflicts touching cited ids: **1709.09871** (author/content), **2112.14609** (author), **1711.08467** (author), **2310.19885** (content) — deep sweep §7.
- ~~`docs/companion-cite-notes.md` is referenced by `refs/LEDGER.md` Batch 12 but does not exist~~ — STALE FLAG, corrected 2026-09-01: the file exists and records the 1408.6560 mismatch (LEDGER concurs) and the 2406.07106 verification.
