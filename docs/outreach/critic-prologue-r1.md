# Assembled prologue critique — round 1

Audit target: `docs/outreach/auditions/ir-triangle-prologue.html`.

## 1. Verdict

**Publishable after one focused repair round; not yet something I would forward.** The scientific
centre is unusually strong. W4 is genuinely delightful, W5 contains real rather than decorative
numerics, W6 earns the soft–memory edge, W8 makes the gravitational solve visible, and W9 is an
excellent statement of the hypotheses. The integration itself preserved every fragment block and
the reference core exactly.

The present stop is the last screen, where the page asks to be trusted as a synthesis. W10 clips two
corner boxes and its clickable map omits every electromagnetic station even while its prose names
them. Worse, the assembly-owned provenance drawer resurrects two pre-repair EM statements, including
the false linear-in-frequency correction. Those are small repairs in code, but they land exactly at
the reader's trust test. W5 is scientifically impressive but does not yet clear the brief's
"genuinely delightful" flagship bar: the decisive response is still easier to read in its table
than to see happen on the range.

## 2. FATAL — must fix

1. **The assembly-owned provenance block contradicts the repaired stations**
   (`ir-triangle-prologue.html:8074,8082-8085`). The finite-radius W6 row still prints the old
   one-component values `0.004854 / 0.004853 / 0.004853 / 0.004850`; the repaired station computes the
   full-vector residual; rerunning the current finite-radius route gives the default values
   `0.005001 / 0.005000 / 0.005000 / 0.004999`. More seriously, the following paragraph says the W3
   gap falls "in exact proportion to ω" and is the first correction in `ωτ`. W3 now correctly shows
   that the energy spectrum is even in frequency and the correction is quadratic
   (`:2408-2416`). **Fix:** replace the W6 values with the four full-vector values above. Replace the
   W3 sentence with: "The gap is physical rather than quadrature error: at the opening settings it
   is `2.52e-8`, `2.52e-10`, `2.52e-12` at `ω=10^-2,10^-3,10^-4`; it therefore falls as `ω²`, and the
   leading correction is `O((ωτ)²)` with coefficient `3.106e-2`." Do not quote the superseded §3.2
   prose from `NOTES-frag-em.md`; §10.1 item 3 and §10.2 item 8 are the repair ledger of record.

2. **W10 is neither the link map promised by the design nor an exact account of what the page
   earned** (`:7628-7632,7830-7855`). The six panels generate links to only four distinct targets:
   `#w1`, `#w5`, `#w8`, and `#w9`. The asymptotic-symmetry corner and Ward-identity edge have empty
   `where` arrays even though both name W7; the soft corner omits W2–W4; memory omits W6; and the
   soft–memory edge omits the page's dedicated identity at W6. The rail is useful but is not a
   substitute for the map the reader is told to click. The lede also says every element except one
   was watched happen, while W7 itself says it stops one step short of constructing symmetry
   generators (`:5960-5962`). **Fix:** make the `where` arrays at least:

   - `S → W2, W3, W4`
   - `A → W7`
   - `M → W5, W6, W8` (W1 may remain as a clearly labelled schematic setup, not as an exhibit)
   - `SM → W5, W6, W9`
   - `AM → W7, W8`
   - `AS → W7`

   Update the soft panel's second paragraph to name W3's coefficient and W4's angular pattern before
   W5's detector ledger. Replace the lede's universal claim with: "Every panel points back to what
   this page actually earned. W7 exhibits the conservation-law content of the symmetry corner; the
   symmetry–soft Ward identity is reported from the source rather than derived here."

3. **The opener and W10 turn the existence of memory and a soft theorem into universal statements**
   (`:1315-1321,7831-7842`). W1 asks about an unspecified passing gravitational wave and then says
   the answer is "yes" and the offset is fixed by the energy. A generic waveform or angular source
   need not have a nonzero memory component. W10 broadens the soft theorem still further to "any
   scattering amplitude" with "one massless particle"; the displayed theorem is the leading soft
   **photon** theorem in QED, not a theorem for an arbitrary massless species. Its memory panel again
   says free detectors categorically do not return. **Fix:** in W1 say, "For a burst with a nonzero
   memory component, yes: something stays different; for the null-energy burst solved below, the
   constraint fixes that component from the angular flux." In W10 say, "In QED, add an outgoing
   photon and take its energy to zero…" and "After a burst with nonzero memory, free detectors can
   fail to return…" The restriction makes the claims true without weakening the story.

4. **The page-wide meaning of the `Exact formula` badge is false for W4**
   (`:1172-1174` versus `:3031-3037`). The masthead promises "No fitting, no interpolation" for an
   exact-formula figure. W4 carries that badge but explicitly and correctly says the browser
   bilinearly rescales its finite texture between exact samples. **Fix:** change the legend copy to:
   "The displayed closed form is the expression sampled by the page. There is no fitting; any
   finite sampling or display resampling is stated in the figure caption." Preserve W4's honest
   texel-count and interpolation disclosure.

## 3. Bugs and contract items

1. **Confirmed: W10's triangle overflows its own viewBox by two units on each side**
   (`:7636,7828,7860-7863`). The lower nodes are centred at `x=86` and `x=614` with width `176`,
   so their boxes occupy `[-2,174]` and `[526,702]` inside `viewBox="0 0 700 400"`. The outer
   strokes are visibly clipped in the supplied dark 1300 px screenshot. **Exact fix:** change only
   the SVG attribute to `viewBox="-4 0 708 400"`. That contains both boxes with two units of margin
   and preserves every node, edge, label, and hit target coordinate.

2. **Two W9 formulas look truncated before the reader discovers that they scroll**
   (`:7218-7247,7303,7312`). At 1300 px the second-pole and damped-resonance cards share the row;
   their right-hand sides are cut at rest in the supplied screenshot. Internal scrolling satisfies
   the overflow contract but is poor equation presentation. **Exact fix:** set
   `#w9 .w9-parts { grid-template-columns: minmax(0, 1fr); }`; each card then gets the full reading
   measure. Keep `.w9-part-eq { overflow-x:auto }` for genuinely narrow screens.

3. **W9 still calls the zero-frequency term an always-on pole when `A=0`**
   (`:7209-7215`; compare the correctly conditional verdict at `:7533-7567`). The previous repair
   fixed the marker and verdict but not the card heading. **Fix:** make the static card title "The
   zero-frequency term" and replace "always on" by "coefficient A". The formula and dynamic verdict
   then correctly decide whether that term actually contains a pole.

4. **The three names for the EM transverse coefficient are consistent, but the reader is never
   given the crosswalk** (`:2346-2355,5273-5284,5890-5903`). The formulas show
   `S⃗ = N⃗ = M⃗`; the W3 current coefficient still has the correctly displayed opposite projection,
   `S⃗·ε = -S_cl`. There is no sign contradiction. Source-faithful station notation is defensible,
   but on one page the silent renaming looks like three objects. **Fix:** add one sentence to W6's
   first equation note: "This is the same transverse endpoint vector called `S⃗` in W3–W4; W7 calls
   it `M⃗` to follow the notation of its constraint, so `N⃗≡S⃗≡M⃗` on this page." Do not alter the
   `S⃗·ε=-S_cl` sign statement.

5. **Google Fonts is allowed, not a contract violation.** Although the default is no external
   resources, `AUDITION-SPEC.md:61-65` expressly permits a Google Fonts stylesheet when real fallback
   stacks are present. The one stylesheet at `ir-triangle-prologue.html:42-44` is from
   `fonts.googleapis.com`; the three stacks at `:77-79` provide Georgia/Times, system sans, and
   system mono fallbacks. The stated artifact host also allows that origin. **Ruling: PASS; no fix.**

6. **Library loading and integration isolation pass the source audit.** There is exactly one MathJax
   3.2.2 SVG load and one three.js 0.160.1 load (`:330-338`), both pinned and from cdnjs. All 37
   section/style/script blocks extracted from the two fragments occur byte-for-byte exactly once in
   the page. The station order is masthead, W1–W10, outro; IDs are unique; all inline scripts compile;
   the station IIFEs retain local state; and the only shared application namespace is the authorised
   `window.PROLOGUE`. The hoisted bytes between the core markers have SHA-256
   `bc71fb940a41bea7e2aad7c500a10a775402ebadda307df240cb1d9911b12413`, exactly matching
   `em-core.js`. No integration listener or state collision was found. Three.js is unused dead weight,
   but the integrator brief explicitly required one load; remove it only if that brief is relaxed.

### Fresh number spot-checks

All three checks agree with the default page readouts.

- **EM, W6:** direct calls to the reference core at `β_i=0`, `β_f=0.7`, `τ=0.1`, `θ=62°`,
  `r=10^3`, 16 GL8 panels give the closed vector
  `(-0.8128417900432666, 0.43219564621460455, 0)` and quadrature
  `(-0.8128417900432665, 0.43219564621460455, 0)`. The relative residual is
  `1.2059772998e-16`, matching the printed `1.21e-16`.
- **GW, W8:** an independent 200,000-panel composite-Simpson projection of the normalised
  `κ=12` beam, through `ℓ=44`, gives `∫F dΩ=1.0000000000000067`, 99% of flux by `ℓ≤7`, 99% of
  memory strain by `ℓ≤4`, `82.3920148%` of memory strain power in `ℓ=2`, and
  `99.9988759%` retained through `ℓ≤8`. These match the page's `1`, `7`, `4`, `82.39%`, and
  `99.9989%`.
- **W9:** evaluating its displayed default closed form independently at `t=34`,
  `1+2(0.6)e^{-0.45(34)}cos(2.2·34)`, gives `1.0000002247154987`; the page prints
  `1.000000225` and a difference of `2.25e-7`.

### Journey and register

The why → how → what arc works. In the supplied first-screen captures, W1 starts from an
interferometer, W2 from Coulomb's law, W3 from a short wave packet, W4 from dipole radiation, W5
from an aim-and-fire detector range, W6 from impulse, W7 from Gauss's law, W8 from multipoles, and
W9 from a damped oscillator before introducing its new object. The prose becomes appropriately
plain and numerical at W5–W9.

The first attention loss is the raw nine-line TeX source immediately followed by a second rendering
of the same theorem in W3 (`:2428-2460`); it is excellent audit evidence in the middle of the reading
path. The first trust loss is W10: the clipped corner borders are visible before a click, and clicking
the symmetry corner or Ward edge produces no route back to W7. The fatal fixes above restore trust;
moving the raw TeX behind a disclosure is the highest-value pacing edit.

## 4. Top improvements ranked by wow/effort

1. **[M — highest wow] Make one W5 detector the protagonist of the shot.** W4 already passes the
   delight test: rotating the sphere, dragging a hard line, isolating it, and seeing a finite peak
   ring with an exact forward zero turns a correction into a discovery. W5 does not yet pass. Its
   range is a sparse set of points and its payoff is principally a 15-row ledger. Reuse the existing
   detector index/highlight path, but make selection persistent by click and keyboard; when the
   computed front reaches that detector, flash the detector and matching row, leave a faint
   before-position ghost, and keep the final displacement/velocity arrow. Drive every cue from the
   existing retarded-time and cumulative-solve tables. This supplies aim → arrival → response →
   retained record without inventing dynamics.

2. **[M — high wow] Give the selected W5 detector a two-trace oscilloscope.** Plot the already
   computed instantaneous field/news and its cumulative integral, mark the current retarded time,
   and draw the closed endpoint as a horizontal rule. Keep the panel count and endpoint residual
   beside the trace. In GW mode use news and cumulative strain; in EM mode use `E_rad` and cumulative
   velocity kick. The reader would then see why the permanent number survives instead of learning it
   from the last table column.

3. **[S — high trust/wow] Repair W10 as a real illuminated index.** Apply the six `where` arrays and
   expanded viewBox in §2–§3, then make the selected element's station chips appear in the same
   corner/edge colour as the selected SVG element. No new physics or layout is needed; it turns the
   final screen from a broken summary into a satisfying recap.

4. **[S — medium pacing win] Put W3's character-for-character TeX behind a disclosure.** Keep the
   typeset theorem, line range, macro expansion note, and verbatim source in the DOM, but show the raw
   TeX only after "inspect the source" is opened. This preserves the truth/provenance contract while
   removing the one place the forward journey reads like a source audit.

## 5. Keep list

- Keep W4's orthographic canvas, isolated-line view, peak ring, forward zero, transverse arrow, and
  live gauge-failure calculation. It is the page's most distinctive interaction and does not need a
  WebGL rewrite.
- Keep W5's two modes and numerical engines: the EM history integral is genuinely independent of
  the endpoint column, the GW burst keeps unit energy while width changes, and both ledgers visibly
  state their asymptotic/truncation scope. Add experiential cues around them; do not simplify them.
- Keep W6's separation of radiation memory from Coulomb drift and its three-route convergence table.
  This is where the page most convincingly earns an edge of the triangle.
- Keep W8's `ℓ≤8` solve, single-`ℓ` mode, Green-kernel check, source-dependent gauge disclosure, and
  low-pass explanation.
- Keep W9's causal/advanced split and its independent late-limit predicate. Apart from the `A=0`
  card label and cramped formulas, it is exceptionally clear.
- Keep W1 as the sole number-free schematic and keep its visible tag. No other station smuggles in
  schematic dynamics.
- Keep the three one-sentence ladder rungs and their scope disclosures. They faithfully separate the
  proved, in-progress, and negative lower-dimensional results without turning the prologue into an
  advertisement.
- Keep the page-local rail, immediate anchor jumps, theme control, scoped station ownership, and the
  hoisted reference core.

## 6. What I could not verify

**Chromium: NOT RUN.** I attempted Playwright Chromium locally; the browser died before creating a
page with `FATAL: content/browser/sandbox_host_linux.cc:41 ... Operation not permitted`. Therefore I
do not independently claim the runtime error sweep, control sweep, theme switching, network-loaded
MathJax/fonts/three.js behavior, or horizontal-scroll matrix.

I did inspect the supplied integrator evidence rather than infer its appearance: the dark 1300 px
whole-station captures for W4, W5, W9, and W10, plus the dark 1300 px first-screen captures for W2,
W3, W6, W7, and W8. Those images directly show the W10 clipping and W9 at-rest truncation and support
the journey judgment above. They cannot establish animation timing or input behavior. The
integrator's recorded `PASS 84, FAIL 0, WARN 0` remains evidence from its environment, not a run I
reproduced here.
