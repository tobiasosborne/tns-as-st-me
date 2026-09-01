# Builder notes — memory-lab.html (for the critic)

Structure: masthead (5-tag provenance key) → WHY (test-mass ring SVG,
SCHEMATIC-labelled) → toy bench (one exactly solvable relaxational dof,
ẋ=−γ[x−x_eq]+f(t), closed form displayed AND evaluated; absolute register
A(t)=Ke^{−γt}, calibrated R=K/x₀, shot cost N≥(σ/ηK)²e^{2γt}; hard fence
that it establishes nothing about the next sections) → HOW (5 ingredients
one at a time, then D32/D33 quoted IN FULL from definitions.md) → WHAT
(Schwarzian station: 9×6 parameter map, 8 computed cells, 46 hatched NOT
COMPUTED, no interpolation; unbalanced rows carry the verbatim t2-numeric
restriction; Fig 1 calibrated (linear) over absolute (log) with the
T>√(C/κ̄) region hatched "beyond the declared window"; Fig 2 DC
extrapolation with ω=0.2 ringed "excluded from the fit"; decisive plate =
16-row number ledger, deliberately unglossed; Fig 3 butterfly instrument,
exact g=[[a,α],[0,1/a]]) → VERIFY (left: recorded Julia run 96/96 + real
testset names + pre-repair RED 81/1/82 + poison exit contracts, "this
page does not execute Julia"; right: six checks the browser ACTUALLY runs
on the embedded JSON, incl. closed-form-vs-80-stored-samples 5.15e-9,
RK4 order 4.039) → epilogue (triangle as map only; three claim rows
verbatim; what-is-open; provenance index).

Provenance: whole results JSON embedded byte-for-byte (commit 73b2753),
comment invites a diff. FOUND A REAL TRAP: the JSON stores the Julia 2×2
Möbius matrix COLUMN-MAJOR (json.mobius[i][j]=g[j][i]); with the
transpose the closed form reproduces every stored array to 5.15e-9,
without it ~1e-1. Documented in a code comment; should be recorded
repo-side. Fig 1 uses the dressed bilocal kernel actually used by
_bilocal in numerics/src/schwarzian_memory.jl (κ_L=1, κ_R=k_final kept
separate; per-row κ spread stated — that spread IS the changed conserved
charge on unbalanced rows). δG/Δu computed cancellation-free
(expm1/log1p). The 0.011% figure stated with both underlying ratios and
its r2a adjudication scope (two balanced rows). Fig 3 closed forms
checked against 60-digit mpmath (worst 9.2e-16); the naive
T−arcosh(D/2) was 0.6% wrong at T=30 and is NOT used; (3.15) verified
live, residual 9.4e-14. Palette dataviz-validated both themes; verified
standalone file:// render, both themes, 390/768/1280px, zero JS errors.

Cut from Pick 1 (deliberate): ω dial → static Fig 2 (only 4 computed
frequencies; a dial would interpolate across a scope boundary); ED
"change microscope" panel (second dataset, outside provenance set); QED
soft-photon on-ramp compressed to a clause; Lamport proofs + claims DAG
(Pick 3 territory); full r1→r2→r2a history (Pick 2 territory) — kept only
the decisive RED and the O9 restriction.

## Builder's own known weaknesses (verify, then triage)

1. Default row is C=10 where the whole plateau lies inside the hatched
   beyond-window band; caption invites C=100. Defaulting to C=100 is a
   defensible alternative.
2. Fig 1's line = exact formula evaluated on a FITTED Möbius matrix;
   tagged with both tags; arguably deserves a third tag.
3. Butterfly sliders roam (a,α) freely; caption says implementable
   reachability is a separate question, but the instrument draws frames
   no computed run realises.
4. Toy's shot-cost law assumes i.i.d. additive fixed-variance noise —
   stated, not derived.
5. Parameter-map frame (C∈{1..300}, ε∈{0.01,0.05,0.1}) is an editorial
   choice; hatching honest, extent arbitrary.
6. extrapolated_vertex_ratio shown for unbalanced rows too ("diagnostic
   only"); stricter reading would suppress it.
7. MathJax CDN dependency; offline display math degrades to raw TeX
   (load-bearing symbols in prose are hand-set and survive).
8. Sign-changing δG rows (Gaussian) plot |δG| on the log panel with a
   subtitle note; fast readers could miss the sign.

---

# Repair log — round 1 (response to `docs/outreach/critic-memory-lab-r1.md`)

Same builder, one repair round. Data spine untouched: the embedded JSON is
still byte-identical to the working results file (verified by sha256 after
the repair), the column-major Möbius transpose is unchanged, the DC refits
and every recorded-run number are unchanged. Nothing outside
`docs/outreach/auditions/` was touched.

## §2 — FATAL items (all fixed)

1. **Artifact opening convention.** File now begins `<title>` then
   `<meta charset="utf-8">` then `<style>`. The three font tags
   (2 preconnects + the Google Fonts stylesheet) are **deleted**; the three
   face stacks were extended with real, commonly installed fallbacks
   (Palatino/Georgia, Liberation Sans Narrow/Arial, DejaVu Sans Mono) and a
   comment records that no webfont is fetched. The only remaining external
   resource is the pinned cdnjs MathJax script the spec allows.
   *Deviation:* the critic said "make `<title>` the first element"; the
   charset meta is kept, moved to second. Reason: the file must also render
   standalone from `file://`, where a missing charset makes a browser guess
   and mojibake every κ, Δ, ×, and superscript on the page. The prescan for
   `<meta charset>` reads the first 1024 bytes regardless of order, and the
   Artifact wrapper's own charset already matches, so this is safe in both
   contexts and still satisfies "the file begins with `<title>`".

2. **"exactly solvable gravitational clock system".** Masthead lede now reads
   "…come apart in a controlled Schwarzian gravitational-clock calculation: a
   numerically integrated pulse fixes a fitted post-pulse frame, and proved
   closed forms determine its late detector response." "Exactly solvable" now
   appears only on the toy.

3. **Toy fences.** (a) `x_eq = 0` and `x_0 = 1` are declared in the prose
   above the bench and again beside the two registers, with the general
   statement `A = K`, `R = K/x_0` and the note that they coincide only
   because `x_0 = 1`. (b) The conclusion is now "The fixed difference decays
   with the ruler, while the calibrated ratio remains nonzero. No memory
   label follows from this toy: it has no soft-theorem or DC datum of any
   kind, so it establishes neither D33 nor any Schwarzian conclusion."
   (c) The live verdicts lost "the apparatus remembers" and "the pulse was
   not forgotten"; the γ=0 verdict is now the critic's sentence.
   (d) The shot-cost readout states the i.i.d. additive fixed-variance noise
   model as an assumption, and says explicitly that the count is for `A(t)`
   alone and that `R` is a different estimator whose variance is not
   modelled here. *Deviation:* the critic offered "state and derive its
   i.i.d. additive-noise estimator" as the alternative; we chose the other
   branch — claim no ratio cost at all — because deriving a ratio estimator
   on a toy would add an unbacked model to a section whose whole job is to
   establish nothing.

4. **D32 truncation.** The final parenthesis ("Relation to D26/D27 … tracked,
   not assumed.") is appended verbatim; "quoted in full" is now true.

5. **`𝒩_Δ` provenance.** The general detector equation now displays
   `G_LR = 𝒩_Δ[…]^Δ`, and the sentence under it states that the results file
   and every number on this page use `𝒩_Δ = 1`, which is what the JS
   evaluates.

6. **Approximate vs exact energy balance.** The balanced banner and the
   plate row now carry the required label: energy-balanced *at leading
   order*, the displayed nonzero energy change is the finite
   numerical/nonlinear residual, the conclusion is restricted to the
   registered leading-order balanced scope and is not an inference of exact
   finite-`C` D32 comparability. The words "comparable in the sense of D32"
   and "the two protocols are comparable" are gone.

7. **"not exhibited" ≠ "does not exist".** Both places now read "no
   implementable two-dot reference protocol with the same measured unequal
   one-sided energies has been exhibited", and the banner adds that this is a
   statement about what has been shown: the all-profiles generalization is
   HELD, not refuted.

8. **Figure 2's scope in a reachable state.** Implemented the critic's
   *best* fix, plus a way back to the data. `renderFig2Mode()` switches the
   station between two modes atomically. Unbalanced selection: the whole
   `<figure>` is moved (`appendChild`) into a collapsed disclosure headed by
   a fence carrying the verbatim O9 restriction; the panel title becomes
   "Formal Schwarzian kernel diagnostic — DC residue ÷ soft vertex", a
   "Licenses no detector conclusion" tag is added, the intro paragraph is
   swapped, the 0.011% paragraph is replaced by a note that the adjudicated
   figure belongs to the balanced rows and is not restated, the DC readout
   tile shows "—" with a withheld note, and the plate is retitled "The row as
   computed — formal diagnostic" with matching intro and scope eyebrow.
   Balanced selection restores every one of those. Verified by driving all 8
   cells and both compare directions in a headless browser.

9. **Shot count → scaling proxy.** Both rows renamed "shot-cost scaling
   proxy at `T_max`", the computed value retained, and the constants caveat
   appended verbatim in substance ("up to unknown protocol-dependent
   variance and finite-difference calibration constants … it is not a
   calibrated experimental shot count"). The toy's own shot readout is left
   named for `A(t)` because there it *is* an exact consequence of a stated
   noise model (see item 3d).

10. **Butterfly instruction.** Replaced with the critic's dynamic-safe
    sentence: at `a = 1`, varying `α` changes only the transient and the late
    value remains zero; for `a ≠ 1`, `α` still drops out but the late value
    is `−log a/κ`. True in every reachable slider state.

11. **Formal-frame instrument.** Panel head carries three persistent tags
    (Exact formula · Formal frame family · Reachability not computed), and a
    fence sits **above** the sliders stating that no computed run realises a
    general `a ≠ 1` frame and that only `a = 1` is claim-bearing. Button
    renamed "Explore a formal a ≠ 1 frame". A live state line under the
    controls says which of the two the reader is in. "That is claim
    JT-noplat-abs" became "This is the algebraic decay mechanism used by
    JT-noplat-abs; that claim additionally assumes a compact implementable
    energy-balanced pulse and the registered large-`C`-first scope, neither
    of which the sliders supply." The `a = 1` readout is tied to
    JT-bfly-decay and now uses the critic's `lim Δu_rel^NL = 0` phrasing.

12. **Epilogue.** Prose: "This page tested the late-response corner of that
    triangle … and found a calibrated D33 susceptibility, not D32 memory."
    Triangle node renamed "late response" with sublabel "D33 passes · D32
    fails"; edge label "soft datum ↔ calibrated susceptibility at leading
    order"; the SVG `aria-label` rewritten to match. The closing paragraph
    gained "at leading order and in the balanced sector".

## §5 register table

All seven rows applied, with the critic's replacement wording where given
(masthead, HOW step 2, toy conclusion, toy live verdict, Figure 3
button/readout, decisive butterfly readout, epilogue). "A thermal reference
frame erodes its own ruler" is kept where it follows the numbers.

## §3 — ranked improvements

1. **DONE.** Default is now the balanced `C = 100` row (index 7). A
   "Compare the finite-C proxy (C = 10)" button toggles to its partner and
   back. The note beside it is generated from the data by `windowSentence()`
   and states exactly which stored samples lie inside the declared window.
   *Correction to the critic here:* `T_max` for the balanced `C = 100` row is
   `9.99999999992932`, so the `T = 10` sample is **outside** the window by
   `7.1×10⁻¹¹`, not inside it. The note says so rather than claiming
   "T = 2, 5 and 10 all lie inside".
2. **DONE.** Three-line result strip immediately after the Schwarzian
   on-ramp, each line link-scrolling to its figure or the plate.
   *Wording deviation:* the critic's line 1 read "calibrated susceptibility =
   independently extracted DC datum to 0.011% or better". The adjudicated
   0.011% is the *DC-residue ÷ soft-vertex* deviation, not the plateau-vs-DC
   one, so the strip uses the t2-numeric sentence instead: "the calibrated
   relative-delay detector approaches a nonzero susceptibility, and its
   extrapolated DC residue agrees with the independently normalised soft
   vertex to 0.011% or better". (The plateau-vs-DC agreement happens to be
   0.0025% on both balanced rows, but that number is not the registered one
   and is not quoted.)
3. **DONE.** Station modes — see §2 item 8.
4. **DONE.** Formal-frame provenance and reachability sentence moved above
   the sliders; `a = 1` is the only claim-bearing state; every `a ≠ 1` state
   is labelled an algebraic comparison. The exact family is kept.
5. **DONE.** Live-check table gained a "check type" column
   (recomputation / threshold, assigned exactly as the critic specified),
   the panel carries both `Exact formula` and `Computed sample` tags, the
   intro explains the two kinds, and the check-4 note now says it validates
   serialization, matrix orientation and rendering formulas and does not
   rerun the sourced ODE.
6. **DONE.** A "Proved closed form · fitted computed frame" tag sits beside
   the Figure 1 legend with the per-row fit residual, and says the fitted
   matrix is the input so the line is not an independent second trajectory
   computation — while keeping "not an interpolation of the markers".
7. **DONE.** All five ingredients are visible from the start; the control is
   now a single "Walk me through" that moves emphasis (with an "n of 5"
   readout) and cycles. A two-row operational comparison of D32 vs D33 sits
   in the main path, the limit-order quotation stays in the main path, and
   the two verbatim definitions moved behind "Read the exact campaign
   definitions".
8. **DONE.** Figure 1 carries a two-line annotation at `T_max` — the cost
   proxy for the selected row and "unknown multiplicative calibration
   constants" — and the calibrated readout tile repeats "practical
   permanence is not established".
9. **DONE.** Sign-changing rows now draw negative stored samples as open
   markers and positive as filled (`Panel.dotsBySign`), the zero crossing of
   the closed form is located by scan and marked with a dashed vertical rule
   and a label, the legend gains an "open marker: δG_LR < 0 there" entry, and
   the readout is renamed `signed δG_LR at T = 40`. The log-magnitude panel
   is retained. *Deviation:* the crossing label is placed in the **lower**
   margin, not the upper — in the upper margin it collided with the
   "beyond the declared window" band label on exactly the rows that have a
   crossing.
10. **DONE (both halves).** The Google-font dependency is removed entirely
    (§2 item 1). All seven display equations carry a hand-set
    `data-fallback`; if MathJax never loads, a fallback routine swaps them in
    and appends a one-line note. It triggers on the script's `error` event
    and on a `window.MathJax.startup` check at load, guarded by an
    `mjx-container` test so a successful typeset is never overwritten.
    Verified by pointing the script at a nonexistent file.

## Not regressed (§6 keep list)

Opening question and SCHEMATIC ring; toy equation, closed form and transfer
fence; five-way provenance key and byte-identical embedded JSON; 9×6 map with
8 filled / 46 hatched (plus the sentence the critic asked for, that the frame
is an editorial inspection grid, not a theorem-defined domain); Figure 1's
paired panels, markers, independent DC line and hatching; Figure 2's
non-circular construction (ringed ω=0.2, browser refit, three horizons,
measured-charge normalization, decoy regression); the unglossy 16-row plate;
the recorded-run / browser-arithmetic split with its adversarial history; the
careful numerics (column-major transpose, `expm1`/`log1p`, stable butterfly
formula); the three claim rows and the open-problems paragraph.

Two in-chart labels were shortened or moved for legibility, not content: the
Figure 1 DC line label is now "DC residue" (the legend still carries
"independently extracted DC residue"), because at `C = 10` the long form
overlapped the window-band label.

## QA performed

Headless Firefox, `file://`, on the real file and on driven copies:

- All 8 parameter cells clicked in sequence, both compare directions, every
  slider driven to both ends (`toy-gamma` 0→0.6, `toy-F`, `toy-w`, `toy-t`
  3→40, `bf-a` 0.90→1.10 including 0.999/1/1.001, `bf-alpha` 0→6), all
  buttons and both disclosures toggled: **no JS errors** (window `error` and
  `unhandledrejection` handlers report into the page; badge reads clean).
- Both themes: `[data-theme="dark"]` and the un-stamped
  `prefers-color-scheme: dark` path both render dark with correct token
  colours; the light path renders light. Theme toggle round-trips (its
  localStorage memory is why a second load in the same profile starts dark).
- 390 / 768 / 1280 px: `documentElement.scrollWidth === clientWidth` at all
  three — no horizontal page scroll. Wide tables scroll inside their own
  containers; ledger gutters tighten under 560px so the values stay visible,
  and the D32/D33 comparison table now scrolls rather than crushing.
- MathJax present: equations typeset. MathJax absent: all seven equations
  fall back to hand-set plain text with an explanatory note.
- `node --check` on the extracted script: clean. Tag balance on the markup:
  clean. Embedded JSON sha256 equals the working results file.
- File size 185 KB; only external resource is the pinned cdnjs MathJax
  script.

**Late amendment to §3 item 5.** The first wording of the check-type gloss
defined "recomputation" as "evaluates a closed form here" — true of checks 1
and 4 but not of check 5 (a convergence order from the stored terminal
errors) or check 6 (a cross-row comparison of two stored arrays). The gloss
now reads "derives its value here, in your browser, from the embedded arrays
— a closed form, a determinant, a convergence order, a cross-row comparison",
which is true of all four. The critic's 1/4/5/6-vs-2/3 split is kept.
