# Builder notes — butterfly-trial.html (for the critic)

Decision tree: preliminary vote (Exhibit A, labelled "settles nothing, on
purpose") → three cross-examinations with one consequential vote each:
(1) comparability/charge sector, wrong vote opens the (E_L,E_R) ledger +
Objection 1 verbatim + retraction from t1-analytic ⟨1⟩3.⟨2⟩7; (2)
constant-vs-decay, RSS ratio 6.83e11 and ΔAIC 107.0 recomputed IN PAGE
from embedded arrays, fit toggle + residual strip; (3) circularity,
Objection 4 verbatim + FIX VERIFIED disposition. Verdict card then case
history (real order restored there; r1 terminal line reported as it
reads: eight objections, FAIL(1,2,4,6)).

Provenance: embedded JSON byte-verbatim vs numerics/results/
schwarzian_memory.json (commit b766eab); page recomputes RSS/AIC (source
convention AIC = n·log(RSS/Σy²)+2k, from schwarzian_memory.jl:229-249) and
the ω→0 intercept — matches to one ulp; pre-repair circular-transform
outputs are NOT in the JSON so they appear only as quotations, page says
so; κT_max=√(κC) drawn with verbatim status string; Exhibit A-1 (Wigner
delay) flagged as standard scattering theory restated, the only non-repo
exhibit; verify panel = three recorded runs (81/81, 96/96, 93 pass/3
fail), page states it executes nothing. Transliteration disclosed under
every verbatim block. Voice discipline: CRITIC/ADJUDICATOR/PROVER blocks
verbatim-only.

QA done: jsdom full-control exercise; headless Firefox 1400px/390px both
themes; palette validated (dataviz checks pass both modes); no page-level
horizontal scroll.

## Builder's own known weaknesses (verify, then triage)

1. Exhibit A-1's decay statement asserted without local TeX citation.
2. Exhibit C's chart cannot visually show the 2.5e-5 agreement; digits
   carry it; ω=0.2 off-axis reported in words.
3. Four-point model selection is weak evidence in isolation; charts are
   louder than the theorem on screen.
4. Exhibit B′: two nearly coincident model lines, visually weak (fitted
   rate at the grid's lower endpoint; caption explains).
5. Cross-examinations not in historical order (timeline restores it).
6. MathJax CDN dependency; offline degrades to raw TeX, no fallback.
7. localStorage restores votes; returning reader sees panels settled.
8. Five non-adjudicated r1 objections paraphrased (labelled), not quoted.
9. Length at top of the 20-minute budget if all 11 drawers opened.
10. Ledger interaction is inspection, not construction (reader cannot
    attempt to build an admissible comparator and fail).

---

# Repair log — round 1 (against docs/outreach/critic-butterfly-trial-r1.md)

All line references below are to the PRE-repair file. Every item in the
critique's §2 is fixed; §3 items 1, 2, 3, 4, 5, 6, 8, 9 are done, 7 is
partial, 10 is done at the level the critic called "the minimum acceptable
fallback". Nothing on the §6 keep list was removed: the preliminary vote and
its "settles nothing" contract, the two-register architecture, the charge
sector retraction, the in-page recomputation (verified below to still
reproduce every stored value), the fit controls and residual strip, the B'
caption sentence, the circularity demonstration, the exact butterfly law with
its full scope, the three-card verdict, the honest negative dockets, and the
visual system all survive unchanged or strengthened.

## §2 — truth constraint (all ten were MUST-FIX)

1. **Wigner branch and the unsourced decay claim.** Adopted the critic's
   continuous branch verbatim, and restricted the exhibit explicitly to one
   isolated zero-background Breit-Wigner resonance; the eq-tag now says in so
   many words that the principal branch of arctan[(G/2)/(E_r-E)] would jump at
   E=E_r and would not differentiate to that Lorentzian. Added the one-line
   stationary-phase derivation (outgoing phase kr+2d(E), peak at
   t=r/v+2 hbar d'(E)) so the delay is derived on the page rather than asserted.
   **Deviation, deliberate.** The critic offered two ways to repair the
   local-decay statement: cite a theorem with hypotheses, or replace it by an
   explicitly solved calculation. L3 forbids quoting a reference from memory
   and refs/ contains no local-decay/RAGE source, so citing a textbook was not
   available. Took the second branch: the exhibit now displays the exact free
   Gaussian packet, the bound |<psi,O psi>| <= int_B |psi|^2 <= L/(sqrt(2pi)
   sigma_t) ~ 1/t for any pre-fixed bounded-region observable with ||O||<=1,
   and then STATES the remaining hypothesis for the scattered run (no
   bound-state component, asymptotically a free outgoing packet) as a
   restriction, adding that it is not proved here and that nothing later on
   the page rests on it. The colophon says the repository holds no source for
   Exhibit A-1 and that the exhibit is therefore self-contained instead. The
   preliminary-vote settlement text carrying the same over-strong claim was
   qualified the same way.
2. **One-mode / "coupled" JT on-ramp.** Replaced with the critic's paragraph
   verbatim ("Take two copies prepared in the thermofield-double state...
   no finite-N conclusion is used here"), plus one sentence pointing to the
   open docket. No inter-copy coupling is asserted anywhere now.
3. **D33 normalization clause and the false drawer label.** Added "with
   normalization fixed by measured injected charge" before "nothing fitted" in
   the displayed D33, in bold. Took the stronger of the critic's two options
   for the drawer: it now contains D32 and D33 COMPLETE and verbatim
   (definitions.md lines 1373-1412), checked character-for-character against
   the file by script; the source line records that nothing was transliterated
   or omitted, so the label "Both definitions, verbatim" is now true.
4. **Balance gate classifying from the profile string.** Implemented the
   critic's source-owned scope field. Each embedded ledger row now carries
   `_balance_scope` ("leading-order balanced" / "unbalanced"), and the wrapper
   carries `_balance_scope_source` naming critic r2 Objection 9 as its origin.
   buildLedger() and describeLedger() read that field; the profile string is no
   longer consulted and no numerical tolerance was invented. The SECTOR column
   header now reads "as classified in r2 O9", the panel intro says the column
   is the adjudicated classification and not a page-side tolerance, and the
   balanced detail reads "Balanced at leading order ... the full run leaves a
   residual dE_R = 2.826e-08 ... a same-energy reference exists to the retained
   leading Schwarzian order". The old "Rows one and two are exact statements"
   note is gone with the static table it belonged to (see §3.5), and its
   replacement says the balance is a leading-order statement with a measured
   residual.
5. **Four points proving an asymptote.** Restructured cross-examination II to
   theorem -> scope -> computed diagnostic (also §3.2): the butterfly law
   (3.15) and the general balanced law (3.2)-(3.9) now stand, each with its
   full scope sentence, BEFORE Exhibit B and before the vote. Act-head no
   longer says "no room to argue". Decision 2 option B now reads "the computed
   window selects decay, and the theorem above then fixes the asymptote", and
   the settlement is split into "What the four points establish" (a strong
   preference on this window, and nothing beyond it) and "What fixes the
   asymptote" (JT-noplat-abs in its stated scope). The finite-C proxy is now
   drawn as hatching, and the caption states per run how many fitted points lie
   beyond it: at C=10 every fitted point does, so the fit "is a diagnostic, not
   a finite-C validity certificate". For C=100 the classification uses a
   display-only 1e-9 band, disclosed as such, because T=10 exceeds the recorded
   max_T = 9.99999999992932 only at the eleventh figure; the caption says one
   point "sits on it, to the precision the marker is recorded at" rather than
   asserting a meaningless inequality.
6. **Silent interpolation in Exhibit B'.** The connector polyline is deleted
   (jsdom asserts zero <path> elements in that chart). Only the two labelled
   fitted models are lines; the caption says so. The same hatched finite-C
   proxy region and dashed kT_max rule as Exhibit B were added, and the legend
   gained the hatch swatch and the outside-fit-window marker.
7. **"memory identity" at the decisive moment.** Now "a leading-order identity
   between the calibrated D33 susceptibility and the zero-frequency soft
   residue".
8. **Over-broad second verdict card.** Now "So this fixed allowed observable,
   G_LR, carries no nonzero D32 plateau in that scope. Nothing is claimed about
   other allowed observables." Badge changed to "No D32 plateau in dG_LR".
9. **Provenance taxonomy.** Adopted the four-badge split: PROVED FORMULA /
   PAGE-EVALUATED / COMPUTED SAMPLE / RECORDED QUOTE-RUN, plus the pre-existing
   OUTSIDE WINDOW. Re-badged every instrument: A-1 and the new comparator are
   PAGE-EVALUATED; the shock matrix, the butterfly law and the general balanced
   law are PROVED FORMULA; the two readouts, the historical circular tail, D32/
   D33, A-2 and the Not-claimed list are RECORDED QUOTE; the decoy panel is
   RECORDED RUN. Every displayed-but-not-evaluated formula's tag now says so.
   Footer replaced with the critic's required wording verbatim; the JSON block
   comment now explains that selected fields were copied value-for-value into a
   smaller wrapper, names the two page-added underscore keys, and the source
   list repeats it.
10. **Stale-run state in open settlements.** settle() now records the open vote
    in `openVotes` and fills all run-dependent values through one
    `fillRunDependent()` path; changing either run selector calls
    `rowChanged()`, which redraws the three exhibits AND re-renders every open
    settlement. The Decision 2 ruling also prints its run label ("run 7,
    C = 100") so provenance stays visible. jsdom regression: settle at C=10,
    switch to C=100, assert both the RSS ratio and the label changed.

## §3 — improvements

1. **Result before the argument. DONE.** A flat "The finding, before the
   argument for it" block sits immediately under the deck with the critic's
   three sentences, plus one line saying the votes are the route by which the
   reader checks them, not a device for withholding the answer.
2. **Butterfly law ahead of the model-selection chart. DONE.** See §2.5. The
   Shenker-Stanford geodesic cross-check moved up with it as a plain sourced
   quotation; the PROVER voice rail that used to sit inside that block is now a
   drawer, so the decisive screen carries no courtroom ornament.
3. **Fit honest about strength and validity window. DONE.** "no room to argue"
   gone; hatching plus a dashed marker for the finite-C proxy in both B and B';
   marker style encodes fit-window membership and hatching encodes the proxy,
   so the two distinctions are separate channels; B' connector removed; RSS
   ratio, dAIC and the residual strip kept.
   **Partial deviation:** the critic asked for the JT-noplat-abs asymptotic
   "directly under the chart" while item 2 asks for theorem-then-diagnostic.
   The two cannot both be literal; item 2's ordering won, so the law is
   immediately above the chart instead, and the caption points back to the
   iterated limit rather than to a finite endpoint.
4. **Exhibit C independence made visible. DONE.** A three-column route ledger
   (late detector / DC route / soft route) with each route's computed value, a
   paragraph saying explicitly that the DC route and the late detector share
   the integrated trajectory while the soft route does not, equation (4.13)
   displayed with its leading-order domain, and the two ratios in large type
   (intercept / late detector, intercept / soft-vertex prediction) each labelled
   "Internal" or "Independent".
5. **Reader constructs the comparator. DONE.** The static three-row charge
   table is replaced by two segmented controls for the reference clock
   exponents. The page evaluates E = C k^2 / 2 on both sides from real computed
   inputs (C = 10, k_i = 2 pi / beta = 1 from the results file, k_f from ledger
   row 1) and shows the pulsed pair, the constructed pair and the difference.
   Only the matched pair unlocks the "match" state, and its verdict is the
   critic's: "algebraically matchable, but no implementable two-dot preparation
   is supplied" -- the actual obstruction, tied to the held docket. The
   (k_f,k_f) case is identified as the reference as submitted and the (k_i,k_i)
   case as the plain equilibrium that becomes admissible for a balanced pulse.
6. **Two-boundary diagram. DONE.** The schematic now labels t_L(u) and t_R(u),
   marks the simultaneous SL(2,R) map as gauge with the relative configuration
   as the observable, labels the compact right-boundary source at u_*, labels
   G_LR as the allowed cross-boundary observable, and states that no inter-copy
   interaction is assumed. Moved next to the readout definitions so setup and
   observables are one panel; the aria-label was rewritten to match.
7. **Compress the main path. PARTIAL.** The commit chronology, the five-
   objection digest, the mutation transcript, Objections 1/4/6 in full and the
   source inventory were already after the verdict; that section is now titled
   "Appendix - the full adversarial record" and says in its standfirst that it
   is optional evidence, not a continuation. The long quotation stacks were cut
   out of the Decision 1 and Decision 3 settlements (prover retraction, r2 O1
   and r2 O4 dispositions) and moved into a new appendix drawer, "The
   retraction, and the two dispositions that closed the loop"; the two
   settlements now carry one terse critic quotation each. The duplicated
   butterfly-law block was deleted when the law moved up, and the second r1 §4
   critic quotation in cross-examination II was dropped, leaving one critic turn
   there plus one inside the settlement the reader opted into -- not literally
   "one per cross-examination", which is where this item stops short.
8. **Provenance labels that answer one question each. DONE.** See §2.9. Also
   added a small "derived here from sample X using formula Y" line under every
   derived table: the fit readout, the DC readout, the 1/(1+w^2) table, the
   ledger detail, the comparator, and a caption on the cost table saying
   nothing in it is derived here.
9. **Unprejudiced trial and coherent linked state. DONE.** Votes are no longer
   written to or read from localStorage at all, so every visit meets the
   decisions unsettled; the theme preference is still stored, separately. Run
   changes propagate to all three exhibits and to any open ruling (§2.10).
10. **Mathematics fallback. DONE at the minimum level the critic specified.** A
    watcher shows a visible notice -- "Mathematics rendering is unavailable ...
    Every formula on this page remains present as TeX source, and every number
    is in the tables" -- if MathJax has not initialised after eight seconds.
    Verified by aborting all cdnjs requests in headless Chrome: notice appears,
    all five charts and all tables still render, no page errors. Hand-set
    HTML/SVG fallbacks for the seven load-bearing equations were NOT done.

## QA after repair

- jsdom full-control exercise, 58 assertions, all pass, zero JS errors: five
  charts render; five tables populate; route ledger and both headline ratios
  fill; Exhibit B' contains no <path>; both hatch patterns present; nothing
  settled on load and no vote pre-pressed; all nine vote buttons settle; the
  Decision 2 stale-run regression; both run selectors stay synced; three fit
  toggles; three horizon toggles; all four comparator combinations give four
  distinct verdicts and only the matched pair unlocks "match"; all eight ledger
  rows select by mouse and by keyboard and the sector labels come from
  `_balance_scope` (2 balanced, 6 unbalanced); theme cycles auto/light/dark.
- Numerical fidelity re-checked after the edits: the in-page recomputation
  still reproduces every stored value for both runs -- RSS constant and
  exponential, both AICs, the RSS ratio (6.830784e+11 at C=10, 6.894527e+11 at
  C=100), the dAIC (106.999502, 107.036656), the selected model, and the
  omega^2 intercept at all three horizons (e.g. 2.582964514865e-05 against the
  stored 2.582964514865e-05). The comparator's dE agrees with the stored
  `energy_change` to 8e-15 relative.
- Headless Chrome, prefers-color-scheme light and dark, at 390 / 768 / 1300 px:
  no horizontal page scroll at any combination (scrollWidth == innerWidth in
  all six), no element escaping the wrap, no console or page errors, 191
  equations typeset, explicit token background in both themes.
- A separate clipping probe (scrollWidth > clientWidth on non-scroll
  containers) found and fixed two real bugs introduced by this repair: the
  comparator grid needed minmax(0,1fr) and min-width:0 on its children, and the
  kappa readout line needed to be a wrapping flex row instead of nbsp-joined
  text. One benign case remains: the butterfly-law scope paragraph overhangs
  its 70ch measure by 25px because an inline MathJax box cannot break. It is
  overflow:visible inside a 1010px panel, so nothing is clipped or pushed.
- Chart palette re-validated with the dataviz validator after the repair: all
  six checks PASS on both surfaces. New badge colour checked for text contrast:
  6.4:1 light, 5.1:1 dark.
- Size 176 KB, single file, no new external resources.

## Where the critic was wrong or imprecise

- **§2.1's "add that external source" could not be honoured as written.** L3
  makes local TeX the only admissible ground truth and refs/ has no scattering
  or local-decay source, so the honest repair was to make the exhibit
  self-verifying and say the repository has no source for it. Recorded above
  and in the colophon.
- **§2.5's "for C=10, every fitted point is beyond kT_max ~ 3.16" is right;
  the implied clean cut at C=100 is not.** There max_T = 9.99999999992932 and
  the fitted grid contains T=10, which exceeds it at the eleventh significant
  figure. Reporting "3 of 4 beyond" would be true but would hand the reader a
  numerically meaningless distinction, so the page classifies that point as
  sitting on the marker, with the display-only band disclosed.
- **§2.9's claim that "the page recomputes derived statistics" contradicts
  "nothing was regenerated" is correct, but the same paragraph's list of
  non-evaluated formulas omitted one**: the M_shots scaling in "What the
  plateau would cost to see" is also displayed and not evaluated. Its tag now
  says so too.
- **§3.3 and §3.2 conflict** on where the JT-noplat-abs asymptotic goes
  (directly under the chart, versus theorem before diagnostic). Resolved in
  favour of §3.2; noted above.
