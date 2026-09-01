# Builder notes — proof-atlas.html (for the critic)

Route (5 stops, verdict at 05): 01 why the three corners know about one
another (final-value theorem as load-bearing identity) → 02 what counts
as a detector (two-sided correlator (0.4), mechanism diagram) → 03 fair
comparison (ΔE=∫P du, retained sector ΔE=0) → 04 soft clock mode +
zero-frequency weight ((4.9)=(4.13); hosts the Lamport showcase + DC
chart) → 05 persistence ((3.7); recorded-run charts, witness table,
three verdicts, D32/D33 split → the pullback DAG). ENTHUSIAST/REFEREE is
a task toggle (referee REPLACES the account with assumptions/limit
order/falsifier/criticism/not-claimed; no red boxes). Two-line
translation rails per stop.

Lamport showcase: JT-B-susc via t1-analytic ⟨1⟩2–⟨1⟩5; 4 flyover
headlines → 31 leaves with ASSUME/PROVE/RETRACT/VERDICT tags, equations,
"Because:" lines citing displayed equations / named computations /
TeX file:line; includes the RETRACT leaf ⟨1⟩3.⟨2⟩7 and [physical
argument] markers.

Sub-DAG (11 nodes): observables-spec (spec, no status), D32, D33; the
three PROVED verdict rows; JT-A-tangent (dashed, per its own "context
only" wording), JT-A-ward-grid, JT-A-purejt + JT-A-notconserved (no
incoming edge, labelled "no dependencies"); a HOLD node for the
unbalanced generalization (dotted connector, card says it is NOT a
CLAIMS row but the closing sentence of JT-noplat-abs); an explicit
dotted divider: "no dependency edge between the two groups in
claims/CLAIMS.md" — the ask box's refusal target.

Provenance: only balanced parameter points 6 and 8 plotted (1–5,7
unbalanced, demoted by r2 O9 — stated twice, never plotted). Embedded
numbers diffed bit-for-bit vs schwarzian_memory.json @ b766eab; 13
verbatim blocks diffed vs CLAIMS/definitions @ a65007a, exact. DC
dashed line = in-page least-squares refit reproducing stored
extrapolated_residue to 0.000e+00. The 0.011% agreement is text only
(cannot be honestly drawn at that scale). No dual axes. Verify = 
transcribed run, labelled not-executing, incl. pre-repair 81/1 RED and
the critic's 93/3 mutation. Ask box = labelled MOCK, four extractive
answers + refusal fallback naming the held node, missing edge, finite-N
gap. QA caught: D33 reads "the ruler IS persistent" (not "persists").

Cut from Pick 3: 7 stops → 5; subscribable status diffs; labbook +
Strominger DB as browsable sources; voice split inside nodes; glossary;
full r1 transcript (only the three physics-changing objections, in
referee mode).

## Builder's own known weaknesses (verify, then triage)

1. Stop 01 thinnest — quotation + one identity; the QED soft factor is
   referred to, not written down.
2. Lamport leaves are compressions, not transcriptions; equations and
   justifications faithful, surrounding prose is the builder's. Worth a
   line-by-line check against ⟨1⟩2–⟨1⟩5.
3. Symmetry cluster under-motivated; reader meets the four JT-A rows
   cold at the pullback.
4. Δu panel: two nearly coincident curves (dashed overlay + caption).
5. Referee mode on stop 05 HIDES the witness panels; a referee arguably
   wants both at once.
6. overflow-x:clip on body (sticky survives); Safari<16 ignores it.
7. No render test below ~360px (DAG min-width 820px inside scroller).
8. Only two of five statuses occur on the map; legend explains, but an
   unsympathetic reader may read it as uniformly green.

---

# Repair log — round 1 (same builder, after critic-proof-atlas-r1.md)

All edits are in `docs/outreach/auditions/proof-atlas.html` only. File is
206 KB, single file, no new external resources (MathJax 3 SVG from cdnjs and
Google Fonts as before).

## §2 truth-constraint audit — all twelve items

1. **Final-value hinge.** Stop 01 rebuilt as a three-line blackboard. The lede
   is now "In the standard asymptotic formulations of QED and gravity, a
   leading soft theorem, its Ward identity, and a memory observable are related
   under explicit boundary and regularity assumptions." The general FVT display
   is gone; the hinge is now the licensed special case, in the critic's words:
   `ε̃_sub(ω)=iA_*/(ω+i0)+O(1) ⟹ lim_{u→∞}ε_sub(u)=A_*=lim_{ω→0}[−iω ε̃_sub(ω)]`,
   with transform convention, retarded `ω+i0` prescription, "no additional
   nondecaying physical homogeneous components", and the explicit sentence that
   a zero-frequency pole does not by itself make a response settle. Referee
   panel for stop 01 rewritten to match.
2. **Microscopic on-ramp.** "two coupled SYK dots" → "two SYK copies, or dots,
   prepared in a thermofield double state, with a compact source acting on the
   right copy", plus "No coupling term between the dots is introduced anywhere
   on this route." (observables-spec.md:11-13).
3. **D32 comparability / balanced family.** Lede clause is now "otherwise the
   pair is not comparable in the sense of D32, so its difference cannot support
   the memory verdict at issue", with an added sentence that a non-comparable
   difference may still be measurable. The "not a trick" paragraph is replaced
   by the scoped version: the balanced sector is the sector with a constructed
   same-charge reference; a general balanced pulse only returns the net energy;
   the explicit raise–hold–lower family is the one in the proof.
4. **Lamport label + restored definitions.** Header eyebrow now reads "Faithful
   compressed proof map — 31 leaves"; the disclosure summary reads "faithful
   compressed proof map (31 leaves); open the source for the full derivation";
   the source line reads "Open the source for the full derivation:
   t1-analytic.md ⟨1⟩2–⟨1⟩5, lines 195–861". Each level-one heading carries the
   lines it compresses (195–369 / 371–578 / 580–776 / 778–861). Restored inline:
   (2.4) with `g_can` before (2.5); (2.7) defining `B` and `H_κ` before (2.8);
   (2.10) in ⟨1⟩2.⟨2⟩8; (3.11)–(3.13) inside the RETRACT leaf with a sentence
   naming the correct-algebra / invalid-detector split. ⟨1⟩5.⟨2⟩6 gained an
   "Updated since the shard was written" justification citing
   `claims/CLAIMS.md:109`. Provenance footer entry rewritten. The proof itself
   was not rewritten: 31 leaves, 21 PROVE / 3 ASSUME / 5 VERDICT / 2 RETRACT,
   both [physical argument] markers, all four flyover headlines intact.
5. **DC "browser refit".** `chartDC` now calls `fitDC(row)`, which computes both
   `slope` and `intercept = (sy − slope*sx)/n` from the three plotted recorded
   residues; the dashed line and the intercept marker use the computed value.
   A three-row micro-ledger prints "Browser refit of the intercept, from the
   three plotted points" / "Recorded intercept in the results file" /
   "Difference" — the last is the real computed difference, which renders as
   `0.000e+0` for the shown C = 100 row (checked independently in Python:
   exactly 0.0; the C = 10 row would print 6.776e-21). Recorded value kept and
   separately labelled.
6. **Detector gloss.** The "dividing that envelope out" paragraph is gone. Stop
   05 now opens with a two-definition display block: the linear susceptibility
   `(R_g−1)/[2Δκ tanh(κ(T−u_*))] = −δG_LR/∂_T G_eq` under `|R_g−1|≪1`, and the
   exact nonlinear readout defined implicitly by `G_pulse(T,T)=G_eq(T−Δu_NL,…)`
   and solved by (3.6) for `D_g ≥ 2`, sourced to (3.3)–(3.6), with "Neither is
   obtained by removing a fitted envelope from the data." The following prose
   says only that the late asymptotics cancel the same exponential factor.
7. **Finite-C proxy boundary.** Both stop-05 panels (and both stop-04
   thumbnails) now draw per-row dotted markers at the recorded
   `maximum_usable_T` (3.1622776579341707 and 9.99999999992932) and hatch the
   region beyond each, with boxed labels "C = 10 proxy edge", "C = 100 proxy
   edge" and "hatched: outside the conservative proxy". Foot notes, the figure
   note, the witness-table row notes and the stop-05 referee "Limit order" cell
   all say that the T = 20 and T = 40 samples, the model selections (fitted on
   T = 5…40) and the optional T = 40 normalization are fixed-C asymptotic
   diagnostics outside the conservative proxy, and that the analytic
   large-C-first verdict does not rest on them.
8. **Provenance blanket.** HTML comment and visible slice note both replaced by
   "Every displayed value is a sourced closed form, a recorded sample, or an
   explicitly labelled deterministic transform or extrapolation of recorded
   samples; no curve crosses an uncomputed scope boundary", with the transforms
   enumerated (DC intercept, optional normalization, printed ratios). DC chart
   tag is now "Computed samples + stated least-squares extrapolation". Added to
   the figure note: line segments join adjacent recorded samples and are not a
   fitted model.
9. **Pullback claim + hand-drawn arrows.** Pullback text is now "Each
   registered result on this sub-map opens to its status, dependencies, proof
   source, computation, and criticism; definitions and specifications are
   explicitly statusless." The stronger option was taken for the arrows: the map
   is now generated at render time from an inline snapshot
   (`<script type="application/json" id="dag-data">`) carrying each row's
   `depends-on` string copied from claims/CLAIMS.md. `dagEdges()` derives a
   solid edge from any row naming observables-spec.md, dashed context edges from
   any row naming "D32/D33 context only", and no edge where the field is "—"
   (those nodes are labelled "no dependencies", also generated). The gap
   sentence under the map and the header badge are computed from the generated
   edge list (`crossing.length`, currently 0), not asserted.
10. **Atlas count.** Intro, `<desc>` and badge now say eleven objects: one
    specification, two definitions, seven claim rows, one scope fence that is
    not a claims row — and the counts are computed from the node data, not typed.
11. **Mock answer a3.** Now opens "Not established. The all-profiles
    generalization beyond the balanced sector is HOLD because no implementable
    unequal-energy reference protocol has been constructed. The one-kick
    transfer-matrix algebra exists but carries no detector verdict."
12. **Mock answer a2.** "The honest answer" is now "Not in the reserved D32
    sense. In the declared large-C-first window there is a gauge-invariant
    calibrated susceptibility with exponentially growing readout cost, but no
    persistent absolute record."

## §3 improvements, in the critic's rank order

1. **First empirical payoff earlier — DONE.** Immediately after the (4.9)=(4.13)
   equality: a "What the recorded run does" strip with two thumbnails (δG_LR
   dying over sixteen decades; Δu_rel flat on a log axis, the two rows a decade
   apart), both carrying the proxy markers, and the sentence "The absolute
   reading vanishes; the calibrated susceptibility approaches the same DC
   residue." The full Lamport tree now sits behind a closed disclosure,
   "Inspect the compressed proof", followed by the full-size DC chart.
2. **REFEREE mode — DONE.** One global toggle in the sticky masthead
   (`#mode-seg`, persisted in localStorage in try/catch); per-stop mode bars
   removed. Each stop is split: `.account` (explanatory prose, translation
   rails) is hidden in referee mode; everything else — equations, the apparatus
   diagram, the thumbnail strip, both stop-05 panels, the witness table, the
   note boxes, the claim rows, D32/D33, the proof disclosure — stays visible in
   both modes. Each referee panel is now a titled block ("What licenses this —
   stop NN…") that appears alongside the evidence rather than replacing it.
3. **DC micro-ledger — DONE** (see §2.5). The fourth open point outside the fit
   is kept, as is the "too small to draw at this scale" decision.
4. **Window boundary + absolute/normalized control — DONE.** Per-row markers and
   hatch as in §2.7; a two-state control (Absolute / ÷ its own Δu_rel(40))
   defaults to absolute. **Deviation:** the absolute view uses a logarithmic y
   axis rather than linear. On a linear axis the C = 100 row is a flat line
   pinned to zero and its approach to its own late value is invisible; the log
   axis shows both the expected factor of ten and each row settling. Still one
   axis per panel, no dual axes.
5. **Proof map self-decoding — DONE** (see §2.4).
6. **Stop 01 blackboard on-ramp — DONE.** Three sourced lines: Weinberg's
   leading soft photon factor transcribed from
   `soft_Arxiv_update.tex:1075-1082` (charges, out-minus-in signs, q→0 scope,
   O(q⁰) corrections, "Not a result of this campaign"); the Ward-identity
   reading quoted from `:1064` as literature context; the conditioned hinge from
   §2.1. Kept the `:334` soft-theorem/memory quotation. Ends with the narrower
   question, in the critic's words.
7. **Detail panel instead of a card stack — DONE.** The eleven cards are now a
   hidden store; clicking or keyboard-activating a node renders one card into a
   `#node-detail` panel directly under the map, with "N of 11 · <row id>",
   Previous / Next / Back to map. Focus stays on the node (the panel is not
   focus-stolen); the selected node gets an accent outline; claim permalinks open
   the map with that panel selected.
8. **Symmetry priming — DONE.** Above the pullback button: "Does a conserved
   charge or Ward identity enforce the plateau?" / "No registered dependency
   establishes that edge." Above the map: a four-sentence primer on the four
   JT-A rows (broken kinematic response; two candidate definitions on a finite
   grid; pure JT only; nonconserved implementer still open). Header badge, all
   counts computed: "7 PROVED rows · 1 HOLD scope fence · 1 specification and 2
   definitions, statusless · 0 generated edges connect the detector group to the
   symmetry group."
9. **Two-row definition block — DONE** (see §2.6).
10. **Review-process narration subordinated — DONE.** The main path keeps one
    compact non-circularity statement ("Doubling the late detector value …
    leaves the independently extracted DC intercept unchanged; a mutation …
    runs 93 pass / 3 fail"); the pre-repair numbers (1.24368e-4 → 7.90455e-5,
    1.24780e-4 → 5.83348e-5), the 96/96 and 81/1 history and the coverage list
    now live in the stop-04 referee panel and in the verify drawer, which is no
    longer `open`. The recorded-run wording and "This page executes nothing" are
    unchanged.

## Not regressed (§6 keep list, re-checked in the built file)

Five-stop route + delayed pullback; stop-02 apparatus diagram, single
synchronization event, even-CAR/POVM grounding, non-observables list; stop-03
retraction as a first-class result; (4.9)=(4.13) with the "nothing fitted"
normalization, the O(C^-2) fence and the finite-amplitude exclusion; 31 leaves
(21 PROVE / 3 ASSUME / 5 VERDICT / 2 RETRACT), four flyover headlines, both
[physical argument] markers, ⟨1⟩3.⟨2⟩7; the fourth open DC point; only
parameter points 6 and 8, bit-level values, no persuasive curves for the
demoted six; recorded-run wording; 13 verbatim blocks (three claims, D32, D33,
scope fence, …); solid / dashed / dotted edge distinction, the no-edge divider,
the "no dependencies" labels; the MOCK ask box and its refusal; restrained
palette, theme parity, local scrollers, keyboard-operable nodes, permalinks, no
dual axes.

## QA performed (headless Firefox, file:// on the real file)

- Stops 01–05 in both reading modes; light and dark themes (dark checked on the
  charts, the map and the referee panels — hatch, proxy lines and label
  backdrops all follow the tokens).
- Widths 390 / 768 / 1300 px. **Bug found and fixed:** at 390 px the whole page
  overflowed horizontally (paragraph text clipped). Cause was the single-column
  `.layout` track: `grid-template-columns: 1fr` with default `min-width:auto`
  items, so a wide descendant blew the track out. Fixed with `minmax(0, 1fr)`
  plus `min-width: 0` on the layout children and `.stop`, and the same for
  `.chart-pair`, `.dsplit` and `.strip-grid`. Verified afterwards:
  `scrollWidth == clientWidth == 390`. Also added `html { overflow-x: clip }`
  with a comment recording why the clip fallback is safe (every wide block has
  its own `overflow-x:auto` scroller).
- Second layout bug fixed: multi-`<dd>` referee cells landed in the label
  column (`.ref-grid dd { grid-column: 2 }`, reset to 1 in the narrow media
  query).
- Permalink arrivals `#stop-1…#stop-5`, `#claim-JT-B-susc`, `#claim-JT-A-purejt`,
  `#claim-JT-A-tangent`, `#claim-JT-A-ward-grid` — all open the map with the
  right panel selected ("4 of 11 · JT-B-susc" etc.).
- No JS errors: an injected `window.onerror` / `unhandledrejection` trap
  reported "JS OK at load" at 1300 px and 390 px and on a permalink arrival.
- Node syntax check on the extracted script; both JSON blocks parse; HTML tag
  balance clean; 204 KB total.
