# Assembly report — `docs/outreach/auditions/ir-triangle-prologue.html`

Integrator lane, bd `tns-ur8`. Brief: `docs/outreach/BRIEF-integrator.md`. Design
document: `docs/outreach/BRIEF-why-prologue.md`. Binding contract:
`docs/outreach/AUDITION-SPEC.md`.

Three files were written: the page, this note, and 62 screenshots under
`docs/outreach/auditions/prologue/qa/`, all prefixed `pro-`. Nothing else in the
repository was touched — in particular neither fragment, `em-core.js`,
`qa-harness.html`, `qa-run.mjs` nor `proof-atlas.html`. The build script, the QA
driver and the authored chrome fragments live in the lane scratch directory and
are not committed; the page is the deliverable and it is complete on its own.

---

## 1. What was assembled

| | source | blocks |
|---|---|---:|
| masthead, W1, W5, W8, W9, W10, outro | `prologue/frag-gw.html` | 21 |
| EM reference core, W2, W3, W4, W6, W7 | `prologue/frag-em.html` | 16 |

Order on the page, as the brief fixes it:

    masthead → W1 → W2 → W3 → W4 → W5 → W6 → W7 → W8 → W9 → W10 → outro

with the EM reference core hoisted to the top of the file (see §3.1). Every
`<section class="stop" id="wN">`, every `<style data-station="wN">` and every
`<script data-station="wN">` is reproduced **byte for byte**, in its original
relative order, and nothing inside one was merged, rewritten or restructured.
The build asserts this: each of the 37 extracted blocks must occur in the page
exactly once, and the two fragments must supply exactly the expected station
sets — 429 675 bytes of fragment carried through unchanged.

## 2. Libraries, pinned, scripts only, cdnjs only

| | version | URL |
|---|---|---|
| MathJax | 3.2.2, SVG output | `cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.min.js` |
| three.js | 0.160.1, UMD | `cdnjs.cloudflare.com/ajax/libs/three.js/0.160.1/three.min.js` |

Both are the versions `prologue/qa-harness.html` loads, so the assembled page
runs the fragments against exactly the library builds they were repaired
against. They are the only two external scripts. The only external stylesheet is
the Google Fonts link for the proof-atlas type stack (Spectral, IBM Plex Sans,
IBM Plex Mono), each with a real fallback stack.

MathJax is configured as the harness configures it — `\(…\)` and `\[…\]` only,
no `$…$` (station 3 quotes TeX source containing `$`), `svg.fontCache: 'global'` —
plus `options.ignoreHtmlClass: 'tex2jax_ignore|mathjax_ignore'`, which the
harness got for free from MathJax's default and which this page has to state,
because station 3's verbatim source block relies on it.

**three.js is loaded and nothing uses it.** Neither fragment contains a single
reference to `THREE`: station 4 paints the celestial sphere by orthographic ray
casting on a 2-D canvas (EM lane §7.1, a deliberate choice about interpolation,
not effort) and station 5's range is a 2-D canvas too, which the design document
explicitly permits. The integrator brief nevertheless says to load it once, so it
is loaded once, and the page is tested with it blocked and with WebGL forced to
`null`: clean, and station 5 still fires. The claim in the lane brief that
hoisting the core "saves 28 KB" applies to the *fragment*, not to this page — the
assembled page needs exactly one copy of the core either way, so the hoist buys
ordering, not bytes.

## 3. Assembly decisions

### 3.1 The EM reference core is hoisted to the head

`<script data-station="em-core">` — `em-core.js` inlined verbatim by the EM lane,
the one place `window.PROLOGUE` is written — sits immediately after the two
library loads instead of between station 1 and station 2. The brief offers this
as the integrator's call. Taking it makes the invariant structural rather than
positional: the core is defined before *any* station script, so the reading
column is nothing but sections. Its bytes are unchanged, and the header comment
above it says where it came from and how to refresh it.

### 3.2 The shared class vocabulary is copied from the QA harness, not the atlas

Both fragments were written against a vocabulary they do not define. A static
pass over both fragments — every class used inside a `<section class="stop">`
against every selector in that station's own `<style data-station>` — found
twenty-one such names. Four are selector hooks that need no rules
(`.w1-ring`, `.w1-ring-ghost`, `.w1-trace`, `.w3-quoted`) and two are MathJax
configuration (`.tex2jax_ignore`, `.mathjax_ignore`). The remaining fifteen,
plus `.stop` itself and the `figure` / `figcaption` element defaults, are the
host's to supply:

    .stop .stop-head .plate .body .lede .eq .eq-label .eq-note
    .chart-title .chart-sub .quote .note-box .mono .eyebrow .btn .btn-primary
    figure figcaption

All of them exist in `proof-atlas.html`, and most of them also exist in
`prologue/qa-harness.html`, which is an atlas-derived subset. The host stylesheet
takes the **harness** version of every one, because that is the environment both
fragments were repaired in and QA'd against — the atlas's `.note-box` and its
`.chart-title` sizes differ, and no purpose is served by rendering the fragments
against CSS they have never been seen under. The palette and the type stack are
copied verbatim from `proof-atlas.html`, as the design document permits.

Specificity is not in doubt in either direction: every host rule is class- or
element-level, every fragment rule is scoped `#wN`, so a station always wins over
the host and never the other way round.

### 3.3 The chrome is this page's own

The design document says the prologue may reuse the atlas's token palette and
type stack "WITHOUT implying the prologue is part of that page". The palette and
faces are shared; nothing else is. The atlas's masthead, its route rail, its
segmented reading-mode control and its frame are not reused, and the page carries
no atlas wordmark, breadcrumb or back-link.

**The top bar** is a slim sticky strip: the page's name, a station readout that
doubles as the panel trigger at narrow widths, and a colour-theme control that
cycles *Auto → Light → Dark* (Auto removes `data-theme` entirely, so the default
is genuinely the viewer's system setting; the choice is remembered in
`localStorage` inside `try`/`catch`). Along its lower edge runs a two-pixel
scroll meter in `--accent`.

**The rail** is the one piece of real information design the integrator added. It
is a ladder: a hairline spine with ten numbered nodes, the current one filled and
ringed, the ones behind it filled grey, and the spine itself filled in `--accent`
exactly as far down as the reader has come. Beside each station sit **three small
marks — soft, symmetry, memory — filled where that station exhibits that corner
of the triangle.** They start empty at station 1, fill one at a time, and are all
three filled only at station 10. That is a true statement about the page's
structure rather than decoration, it is the map the design document asks
station 10 to be, available on every screen, and it is the reason the rail is
worth its column. The assignment is the one the design document gives: W2, W3, W4
soft; W5, W8 memory; W6 and W9 soft *and* memory (the two-route identity and the
hinge are the edge between them); W7 symmetry; W10 all three; W1 none, because
station 1 is the question. Each mark row carries an `aria-label` naming its
corners, and the legend under the rail says what the three columns are.

Below 1040 px the rail becomes a panel dropped from the bar — hidden until asked
for, closed by `Escape`, by a link, or by a click outside. That keeps a
55 000-pixel page from opening with a wall of navigation on a phone.

`--die` is nowhere in the chrome. The EM lane asks that it stay reserved for
radiation rather than being spent on rail highlights or link states (its §8.1),
and it is: every accent in the bar and the rail is `--accent`.

### 3.4 Reading measure left alone

`.stop` keeps the atlas's `max-width: 46rem`. At 17 px Spectral that is a wide
line — nearer 90 characters than the 65 a fresh design would choose — but it is
the measure both fragments were built, laid out and QA'd at, and the canvases,
the `aspect-ratio` boxes, the MathJax overflow thresholds and station 5's
`min-width: 1360px` full-bleed bench are all sized against it. Narrowing it here
would be a cross-cutting change to five stations' figures made blind. The frame
is instead sized so that the reading column is 780 px — 44 px of slack, which is
what station 5's bench bleeds into at wide viewports without ever reaching the
frame edge.

### 3.5 Cross-links and the Part II placeholder

Every in-page anchor resolves, in the live DOM, in all six theme × width
configurations: eleven distinct static hrefs plus the four station 10 builds on
click (`#w5`, `#w9`, `#w8`, `#w1`). The one deliberate exception is the Part II
button, which carries `href="#"` and `data-atlas-link` as the brief instructs;
the chrome script suppresses its default so that a click on a placeholder does
not throw the reader back to the top of a very long page. A one-sentence block
above it says what the Proof Atlas is, in terms of the three Schwarzian results
station 10 already names, and says the address is filled in at publication.

### 3.6 The provenance block

A collapsed `<details>` after the outro, carrying: the rule every figure obeys,
quoted verbatim from station 10's own disclosure ("Every moving quantity on this
page is a closed form, a controlled numerical solve of an equation displayed
beside it, or a labelled quotation — with one deliberate exception, the
number-free schematic that opens station 1…"); the sixteen quoted line ranges of
`refs/arxiv-1703.05448/soft_Arxiv_update.tex` with what each supplies and which
station uses it; the five lecture-remark digests with video ids and timestamps,
labelled auto-captions and secondary; the EM reference core's sixteen-row test
table; the EM stations' ten live checks with the two convergence notes; the nine
independent gravitational and frame checks; both fragment lanes' recorded harness
counts with the GW lane's two argued disagreements named; and this page's own QA
table.

## 4. Everything changed beyond pure assembly

Four things, all of them in host CSS or host script, none of them inside a
fragment block.

1. **The EM core was moved** (§3.1). Bytes unchanged; the brief offers the choice.
2. **`.stop { scroll-margin-top: 5.25rem }`**, where the harness has `1rem`. The
   assembled page has a sticky bar; without this every rail link would land with
   the station heading under the bar. Measured: all ten land at exactly 84 px.
3. **No `scroll-behavior: smooth`.** It was in the first draft and came out after
   QA. The page is about 55 000 px tall, and Chrome's smooth scroll across that
   distance takes seconds — the first QA run failed rail navigation for exactly
   this reason, with stations still in flight half a second after the click. A
   station index should land at once.
4. **The rail spine is re-measured when the narrow-width panel opens.** The panel
   is `display: none` while shut, so its dots have no geometry and the spine came
   out zero-height in the first 390 px screenshot. Found by looking at the
   screenshot, fixed in the chrome script.
5. **The current station has a scroll-position fallback.** The
   `IntersectionObserver` names the station crossing the middle tenth of the
   viewport; when no station does — above station 1, below station 10, or after
   a jump straight to the end of the page — the rail now falls back to the last
   station whose top has gone past that band, instead of keeping whatever it
   last saw. Found by screenshotting the provenance block, where the rail was
   showing no station at all.

(The provenance block, the Part II block and the chrome are the integrator's own
content; small styling decisions inside them are not listed here.)

Nothing was changed inside either fragment, and no fragment behaviour was
re-described. In particular the GW lane's seven preserved decisions all hold:
the beam normalisation still lives in the beam weight; station 5 is still
described as a leading-1/R null-infinity calculation in all three places;
`window.PROLOGUE` is created only by the EM core and by nothing else on the page
(checked at run time in all six configurations, where the only globals added are
`PROLOGUE`, `MathJax`, `THREE` and three.js's own `__THREE__`); the masthead's
"Start with the question" is still an `<a href="#w1">` and the host defines `.btn`
and `.btn-primary` as bare class selectors; no colour literal was reintroduced
outside the three palette blocks; and `#w10 .w10-rung.is-here` is untouched. The
EM lane's four decisions hold too, `spherePattern` and the `S⃗ = −S_cl` sign
relation included.

## 5. QA

Playwright chromium 1.62.1, driven by a lane-local driver
(`qa-prologue.mjs`, 578 lines; the assembler is `build.mjs`, 125 lines). **PASS 84, FAIL 0, WARN 0.**

`qa-run.mjs` could not be reused directly: its static audit, its Node physics
audit and its interaction and physics browser lanes all read `frag-gw.html`
unconditionally, and its `--frag` switch reaches only the browser matrix (the EM
lane diagnosed this in its §10.6 and wrote its own driver for the same reason).
The new driver serves **this file** inside the same minimal
`<!doctype>/<head>/<body>` skeleton an artifact is published in, rather than
re-hosting it through `qa-harness.html` — the page is a whole document now, and
its own `<style>`, its own two `<script src>` tags and its own chrome script are
exactly what has to be tested; re-hosting it as a fragment would double-load both
libraries and both palettes. What it does reuse is the harness's instrumentation,
behaviour for behaviour: the `console.error` hook, `window.onerror`, the
`unhandledrejection` listener and the capture-phase resource-error listener, all
installed before any page script runs.

The recorded run is against the shipped file. The one later edit was
length-neutral by construction: the provenance block prints the page's own byte
count, so the six digits were corrected in place and the file rebuilt to exactly
the same 477 771 bytes, changing nothing outside a collapsed `<details>`.

| lane | rows | what it checks |
|---|---:|---|
| matrix | 60 | light and dark × 390 / 768 / 1300 px: runtime errors, `console.error`, `document.scrollWidth ≤ clientWidth` for html and body, elements escaping the viewport without a scroller of their own, duplicate ids, in-page anchors, globals created, missing palette tokens (`[data-token-error]`), theme stamping, both libraries present |
| rail | 7 | all ten rail links land on their station; the highlight follows; the spine fill is monotone; station 10's map builds only links that resolve; the scroll meter runs 0 → 1; the theme control cycles all three states; no page errors |
| drawer | 4 | at 390 px the panel opens from the bar and closes on `Escape`, both themes |
| interaction | 5 | every control in every station driven, the two draggable canvases dragged and zoomed, station 5 fired in both modes, then no new blank readout, no `NaN`, no page error, no sideways scroll |
| fallback | 7 | three.js and WebGL blocked; the whole CDN blocked (MathJax absent too); unstamped root under each system colour scheme; `prefers-reduced-motion: reduce` |
| file | 1 | size |

Numbers worth quoting:

| | |
|---|---|
| horizontal scroll, all six configurations | `html = body = viewport` at 390, 768 and 1300, both themes |
| escaping elements | none, in all six |
| runtime and console errors | none, in all six, and none after the interaction sweep |
| globals added | `PROLOGUE`, `MathJax`, `THREE`, `__THREE__` — no stray |
| palette token errors | none (the EM fragment stamps `data-token-error` on any station whose host is missing a token; no station is stamped) |
| MathJax | 325 typeset containers, both themes, all three widths |
| controls exercised | 44 ranges, 4 number fields, 5 selects, 4 checkboxes, 32 buttons, across ten stations; the masthead and the outro have no controls, by design |
| station 5 | fired in both modes to a full `15 / 15` detector ledger |
| rail navigation | 10/10 land at exactly 84 px; highlight 10/10; spine fill 0, 31, 70, 118, 157, 204, 261, 309, 356, 404 px |
| scroll meter | `scaleX(0)` at the top, `scaleX(1)` at the bottom |
| three.js and WebGL blocked | no errors, station 5 still fires, no sideways scroll |
| whole CDN blocked | no errors; the page renders with TeX source in place of typeset math |
| unstamped root | `data-theme` absent under both system schemes; body paints `rgb(237,240,242)` / `rgb(13,20,24)` from tokens |
| file size | 477 771 bytes (467 KB), against the spec's 5 MB ceiling |

Four readouts are blank at rest and stay blank: the "gain over the row above"
cell of the first row of station 3's decade table, which has no row above it, and
station 4's three "this line alone" numbers, which apply only in the solo view.
Both are the fragments' own not-applicable states, and the EM lane records the
second family as deliberate ("zero states are states, not failures", its
§10.7.4). The check is therefore before-versus-after: the sweep created no new
blank cell and produced no `NaN`, `Infinity` or `undefined` anywhere.

## 6. Screenshots

62 files under `docs/outreach/auditions/prologue/qa/`, all prefixed `pro-`, so
that nothing the two fragment lanes left there is disturbed.

* `pro-{light,dark}-1300-{w0-masthead,w1,…,w10,w-outro}.png` (24) — the whole
  station. The sticky bar is hidden (visibility only, layout preserved) during
  these captures: a tall element screenshot is stitched, and a sticky bar is
  otherwise composited into every seam.
* `pro-{light,dark}-1300-{station}-first.png` (24) — the first screen of each
  station, scrolled as a reader arriving by rail link sees it. These are the ones
  that answer the brief's question about whether a station opens with its plain
  paragraph and its familiar anchor before the new object.
* `pro-{light,dark}-1300-chrome.png` (2) — the page at rest.
* `pro-{light,dark}-768-w6-first.png`, `pro-{light,dark}-768-rail.png` (4) — the
  mid width, and the station panel open over it.
* `pro-{light,dark}-390-full.png` (2) — the whole page at 390 px, 55 605 px tall.
* `pro-{light,dark}-390-rail.png` (2) — the panel open on a phone width.
* `pro-w5-{em,gw}-fired.png` (2) — the range after firing, in each mode.
* `pro-nothree-1300-w5.png`, `pro-nolibs-1300-w3.png` (2) — the two degraded runs.

They were looked at, not merely produced. Three things came out of looking:

1. The narrow-width panel had no spine (§4.4) — fixed.
2. The first `-chrome.png` pair caught the page mid-scroll, which is what
   surfaced the smooth-scroll problem (§4.3).
3. A band in the first tall station captures turned out to be the sticky bar
   composited into a stitch seam, not a layout defect — the driver now hides the
   bar for those captures. Independently checked: no `.eq` on the page overflows
   its box at 1300 px.

## 7. Known gaps, for the codex critic round

1. **Station 10 does not link to the electromagnetic stations.** Its corner and
   edge panels build links to `#w1`, `#w5`, `#w8` and `#w9` only; its prose names
   station 7 and the two-route identity but the clickable list has no `#w2`,
   `#w3`, `#w4`, `#w6` or `#w7`. The design document asks for links to those. The
   `where:` lists are inside `<script data-station="w10">`, which the integrator
   may not edit, so this is a GW-lane repair. The rail's three-mark matrix is a
   partial substitute — it gives the corner-to-station map on every screen — but
   it is not the same thing as the map lighting up.
2. **Two display equations in station 9 read as truncated at rest.** In the
   `.w9-parts` grid the "second pole" and "damped resonance" cards are about
   356 px wide at 1300 px and their formulas want about 371 px, so they scroll
   inside `#w9 .w9-part-eq` — the GW lane's own scroller, whose font is already
   at `0.82em`. Nothing overflows the page and no check fails, but the reader's
   first sight of both formulas is a cut-off right edge. Fixing it means
   shrinking or stacking inside station 9, which is that lane's call.
3. **Station 10's triangle is two pixels too wide for its own viewBox.** The
   drawing is `viewBox="0 0 700 400"`; the corner nodes are placed at
   `A = [86, 316]` and `M = [614, 316]` with box width `w = 176`, so the two
   lower boxes span `x ∈ [−2, 174]` and `[526, 702]` and lose their outer border
   to the SVG's own clip — visible at every width, in both themes. Both numbers
   are in `<script data-station="w10">`, out of the integrator's reach. Any one
   of three one-line fixes closes it: `viewBox="-4 0 708 400"`, `w = 172`, or
   moving the two corners to `x = 90` and `x = 610`.
4. **The reading measure is wide** (§3.4), inherited deliberately. If the critic
   thinks 46 rem is too long a line for 17 px Spectral, that is a decision for
   the whole family of pages — the atlas, the prologue and whatever follows — not
   for this file alone.
5. **three.js is dead weight** (§2): about 600 KB of script that no station
   references, loaded because the brief says to. If the r3 round does not add a
   WebGL station, dropping it is a one-line saving and a faster first paint.
6. **The page is very long** — 55 605 px at 390 px width, twelve sections, 467 KB.
   The rail and the meter are what make that navigable; whether it is too long
   for the audience is a judgement the critic should make.
7. Everything the two fragment lanes list as a remaining gap is still a remaining
   gap: `NOTES-frag-gw.md` §8 (the two runner-side harness disagreements, the
   permanent listener WARN, the W8 Richardson pairing, W1 schematic by design,
   the Ward identity reported rather than derived) and `NOTES-frag-em.md` §10.6
   (`qa-run.mjs` still being a GW runner, `retardedTime`'s absolute tolerance,
   W4's sampled maximum being a search rather than a bound).
---

## Repair round r1

Input: `docs/outreach/critic-prologue-r1.md` (codex; 4 FATAL, 6 bugs and contract items,
4 ranked improvements, a keep list, and a section on what it could not verify because
Chromium would not start in its sandbox). Lane: bd `tns-170`.

Four files were touched: the page, the two fragments, and this note. `em-core.js`,
`qa-harness.html`, `qa-run.mjs`, the other three auditions and every earlier screenshot
were not. The new screenshots all carry the `pro-r1-` prefix so that nothing the
integrator or either fragment lane left in `prologue/qa/` is disturbed.

**Everything was checked against the code before it was changed.** The provenance numbers
were recomputed from `em-core.js` in Node rather than copied out of the critique, the
station-10 link map was read out of the live DOM, and the two remaining wording items were
checked against the stations they describe. On this round the critic was right on every
FATAL and on every bug that claimed a defect; the two items it ruled PASS were re-verified
and are PASS. Nothing was rejected. Three things it did not report were found by looking at
the screenshots and fixed; they are listed under §R4.

### R1. The fragment contract and block identity

The fragments are the source of record. Every in-station edit below was made in
`prologue/frag-em.html` or `prologue/frag-gw.html` and then copied into the page by a small
sync script, so that the two can only agree. Assembly-owned chrome — the top bar,
the rail, the Part II block and the provenance drawer — lives only in the page.

A check script (lane scratch, `block-identity.mjs`) asserts the invariant the integrator's
build asserted: every `<section class="stop">`, `<style data-station>` and
`<script data-station>` block in the page is byte-identical to its fragment source and
occurs exactly once, the two fragments supply exactly the 36 expected blocks between them,
and the hoisted core between the `BEGIN/END VERBATIM` markers still hashes to `em-core.js`.

    page blocks (excluding em-core): 36
    fragment blocks: em 15 + gw 21 = 36
    em-core sha256 hoisted fb0a178998a1eaf4dc62ec851fa153de4fd0b84111ca036d7c611cccfda49d97
    em-core sha256 file    fb0a178998a1eaf4dc62ec851fa153de4fd0b84111ca036d7c611cccfda49d97  MATCH
    BLOCK IDENTITY: PASS

(The critic quotes `bc71fb94…` for the core; that is the hash of `em-core.js` **including**
its trailing newline, which the inlined copy does not carry. Both statements are true and
they are about the same bytes; the check above strips the trailing newline from the file
before hashing, and is otherwise the same comparison.)

It ran after every edit and passes on the shipped file.

### R2. The four FATAL items

**1 — the assembly-owned provenance drawer contradicted the repaired stations. APPLIED.**
Both halves were recomputed here, in Node, against `prologue/em-core.js`, rather than taken
from the report.

*The station-6 finite-radius row.* The station's repaired route measures the full-vector
residual `|r∫E_rad dt − N⃗| / |N⃗|`, and the drawer was still printing the pre-repair
one-component numbers. Re-running the current route — the same 8-node Gauss–Legendre rule,
the same doubling to a relative `10⁻¹⁰`, the same window `t_obs(∓τ/2)` — at the settings the
station opens with (`β_i = 0`, `β_f = 0.70`, `cτ = 0.10`, `θ = 62°`) gives

    closed form  N⃗ r = (-0.8128417900432666, 0.4321956462146045, 0)
    10^2  64 panels  rel 5.001e-5   (rel)*r = 0.005001
    10^3  64 panels  rel 5.000e-6   (rel)*r = 0.005000
    10^4  64 panels  rel 5.000e-7   (rel)*r = 0.005000
    10^5  64 panels  rel 4.999e-8   (rel)*r = 0.004999

which is the critic's set and `NOTES-frag-em.md` §10.2 item 8's set. For the record, the
one-component form the drawer was printing gives `0.01034` four times over at these
settings, not the `0.004854 / …` it carried either — those are older still. The row now
reads the four full-vector values and its heading says "full-vector relative difference".

*The station-3 paragraph.* It said the gap "falls in exact proportion to ω" and is "the
first physical correction in ωτ". The station has said the opposite since its own repair,
and the station is right. Recomputed here from `radiationSpectrum` and `dcRadiationField`
at the figure's opening settings (`β_f = 0.60`, `cτ = 0.09`, `θ = 55°`):

    tau=0.09  gaps = 2.515836e-8 / 2.515839e-10 / 2.515427e-12   at w = 1e-2, 1e-3, 1e-4
              gap/(w tau)^2 = 3.105970e-2 / 3.105974e-2 / 3.105466e-2   ratio per decade 100.00
    tau=0.18  gaps = 1.006334e-7 / 1.006333e-9 / 1.006419e-11
              gap/(w tau)^2 = 3.105970e-2 / 3.105967e-2 / 3.106231e-2
    tau=0.36  gaps = 4.025336e-7 / 4.025336e-9 / 4.025323e-11
              gap/(w tau)^2 = 3.105969e-2 / 3.105969e-2 / 3.105959e-2

A factor of a hundred per decade, and a coefficient that does not move when `τ` is doubled
twice: the correction is `O((ωτ)²)`, not `O(ωτ)`. The paragraph now gives the three gaps,
says it falls as `ω²`, quotes the coefficient `3.106e-2`, and says why the linear term
cannot be there (the time-domain pulse is real, so `|J(ω)|²` is even). The superseded §3.2
prose in `NOTES-frag-em.md` was not used; §10.1 item 3 and §10.2 item 8 are the ledger of
record, as the critic says.

**2 — station 10 was not the link map its own prose promises. APPLIED, and slightly
enlarged.** Read out of the live DOM before touching anything: the six panels built links to
four distinct targets, `#w1`, `#w5`, `#w8`, `#w9`; the asymptotic-symmetry corner and the
Ward-identity edge built none at all while naming station 7 in their prose. Confirmed.

The `where` arrays were then checked one at a time against what the station in question
actually exhibits, not against the list in the report, and the result is a superset of the
critic's minimum:

| element | links now | why each one |
|---|---|---|
| soft corner | W2, W3, W4, W5 | W2 is where the transverse content of the shell first becomes visible; W3 extracts the coefficient as the plateau and prints it beside Weinberg's bracket; W4 paints the many-particle angular pattern with its exact forward zero; W5's closed-form column evaluates the same coefficient per detector |
| symmetry corner | W7 | the only station that exhibits it |
| memory corner | W5, W6, W8, W1 | W5 fires the range, W6 computes the electromagnetic offset twice, W8 takes the gravitational one apart by multipole; W1 is kept, labelled "(schematic setup)" as the critic allows |
| soft ⟷ memory | W6, W5, W9 | W6 is the dedicated two-route identity — the page's own strongest exhibit of this edge, and it was missing; W5 repeats it fifteen times; W9 holds the hypotheses |
| symmetry ⟷ memory | W7, W8 | W7's ledger is the electromagnetic form of exactly this statement; W8 maps Φ |
| symmetry ⟷ soft | W7 | the identity is reported, not derived; what the page exhibits is the conservation law it would be the quantum statement of |

The soft panel's second paragraph now names W3's coefficient and W4's angular pattern before
W5's ledger, as asked. The lede is replaced with the sentence the critic supplies, in the
page's own voice: every panel points back to what the page earned, station 7 exhibits the
conservation-law content of the symmetry corner, and the Ward identity is reported from the
source rather than derived here. That is consistent with station 7's own footer, which says
in as many words that the page stops one step short of the corner.

**3 — existence claims stated universally. APPLIED.** Both places were checked against the
stations.

* Station 1 said, of an unspecified passing gravitational wave, "the answer is **yes,
  something stays different**, the permanent offset is fixed by the energy that flew past".
  A generic waveform need not have a memory component at all. It now says: for a burst with
  a nonzero memory component the answer is yes; for the null-energy burst solved from
  station 5 onwards the constraint fixes that component from the angular flux; and a wave
  whose news integrates to zero leaves the ring where it found it. The station's question —
  which of the two endings you get — survives intact, and now has a criterion attached.
* Station 10's soft panel said "any scattering amplitude" and "one massless particle". What
  the page displays, and what station 3 quotes by line, is the leading soft **photon**
  theorem in QED. It now opens "In QED, take a scattering amplitude, add one outgoing photon
  and send its energy to zero", and says explicitly that the analogous statements for other
  massless species are not what is displayed here.
* Its memory panel said free detectors "do not return". It now says they "can fail to
  return", after a burst with a nonzero memory component — which is also the honest reading
  of the station's own two nulls, where the permanent strain is exactly zero along the beam
  axis and at its antipode.

**4 — the page-wide meaning of the "Exact formula" badge was false for station 4. APPLIED.**
Station 4 carries the badge and correctly discloses that the browser bilinearly resamples
its finite texture between exact samples; the masthead legend promised "No fitting, no
interpolation". The legend now reads: the displayed closed form is the expression the page
actually evaluates; there is no fitting; any finite sampling or display resampling is stated
in the figure caption. Station 4's texel count and interpolation disclosure are untouched.

### R3. Bugs and contract items

**1 — station 10's triangle overflowed its own viewBox. APPLIED, with more margin than
prescribed.** Confirmed from the source: the lower nodes are centred at `x = 86` and
`x = 614` with box width `176`, so the boxes span `[−2, 174]` and `[526, 702]` inside
`viewBox="0 0 700 400"`, and their outer strokes were clipped. The critic's exact fix,
`viewBox="-4 0 708 400"`, was applied first and screenshotted; at 1300 px it leaves about
two device pixels between the box border and the frame, which still reads as flush. The
shipped value is `viewBox="-16 0 732 400"` — the same fix with fourteen units of margin
instead of two. Every node, edge, label and hit-target coordinate is unchanged; the drawing
is 3 % smaller. The QA row checks containment (`x ≤ −2` and `x + width ≥ 702`) rather than
a literal string, so a future adjustment cannot silently reintroduce the clip.

**2 — two station-9 formulas read as truncated at rest. APPLIED exactly.**
`#w9 .w9-parts` was `repeat(auto-fit, minmax(15rem, 1fr))`; it is now
`minmax(0, 1fr)`, one card per row, so each formula gets the full reading measure.
`#w9 .w9-part-eq { overflow-x: auto }` is kept for genuinely narrow screens. Checked in the
new captures: all three cards typeset without a cut edge at 1300 px.

**3 — station 9 called the zero-frequency term an always-on pole. APPLIED exactly.** The
card is now titled "The zero-frequency term" and its corner tag reads "coefficient A". The
formula and the dynamic verdict, which already decide correctly whether that term contains a
pole, are untouched.

**4 — the three names for the transverse coefficient had no crosswalk. APPLIED.** Confirmed
that there is no sign contradiction: station 3's closed form defines `S⃗`, station 6's
`N⃗` is the same integral, station 7's `M⃗` is the same closed form, and the one genuine
sign, `S⃗·ε = −S_cl`, is a projection and is stated where it belongs. Station 6's first
equation note now carries a short "one vector, three names" sentence saying
`N⃗ ≡ S⃗ ≡ M⃗`, why each station keeps its own source's letter, and that the projection
relation is the one thing that is *not* an identity of names. The `S⃗·ε = −S_cl` statement
in station 3 was not touched, as `NOTES-frag-em.md` §10.7.3 requires.

**5 — Google Fonts. CONFIRMED PASS, no change.** `AUDITION-SPEC.md:61-65` permits a Google
Fonts stylesheet with real fallback stacks, and there is exactly one. Re-verified here that
the fallbacks are real and that nothing bypasses them: every `font-family` declaration in
the whole file is one of `var(--serif)`, `var(--sans)` or `var(--mono)` — no other
`font-family` string exists — and the three stacks are
`"Spectral", Georgia, "Times New Roman", serif`,
`"IBM Plex Sans", -apple-system, "Segoe UI", Helvetica, Arial, sans-serif` and
`"IBM Plex Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace`. The QA fallback lane
now blocks `fonts.googleapis.com` and `fonts.gstatic.com` as well as the CDN, and the page
renders clean.

**6 — library loading and integration isolation. CONFIRMED PASS, no change.** One pinned
MathJax and one pinned three.js, both from cdnjs, both `<script>`. Block identity re-checked
after every edit (§R1). The only globals created in every run are `PROLOGUE`, `MathJax`,
`THREE` and three.js's own `__THREE__`.

### R4. Three things the critic did not report, found in the screenshots

1. **A subscript in a knob label drifted into the middle of its row.**
   `#w5 .w5-knob > span` and `#w9 .w9-knob > span` were flex rows with
   `justify-content: space-between`, so a `<sub>` inside the label became a flex item of its
   own: "frequency ω&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;1.60", and "kick strength β … f …
   0.60". Both labels are now ordinary inline text in a block, with the value floated right.
   Widening station 9's cards (bug 2) is what made this impossible to miss.
2. **The oscilloscope's closed-form rule was hidden under the curve that meets it.** The
   dashed rule is now drawn after both traces, so the reader watches the cumulative curve
   arrive at a line that stays visible; its label was also pulled clear of the frame.
3. **On a phone the range's hint sat on top of the detectors.** Below 560 px the hint drops
   out of the canvas overlay and takes its own strip underneath.

### R5. Improvements

All four ranked improvements were shipped. The two S items first, then the two M items on
the flagship.

**#3 (S) — station 10 as a real illuminated index. APPLIED; one part deliberately not
done.** The six `where` arrays and the expanded `viewBox` are in (§R2 item 2, §R3 item 1).
The chips now carry the same accent border and tint that the selected node box or edge has
just taken in the drawing, sit under their own rule with a label that says whether a corner
or an edge is being reported, and deepen to solid accent on hover and keyboard focus. So
the element you clicked and the stations that showed it read as one object.

*Not done, with a reason.* The critic asks for "the same corner/edge colour as the selected
SVG element". The drawing has no per-element colour: all three corners and all three edges
light in `--accent`, so the chips matching `--accent` **is** matching the selected element.
Inventing a second and third highlight colour would mean either a colour literal, which the
palette gate forbids, or spending `--keep` and `--die`, which carry a fixed page-wide
meaning in all ten stations (`--keep` the Coulombic/hard/"before" class, `--die` the
radiative/soft/"after" class) and which the EM lane asks not be spent on highlights. A
per-element palette is a decision for the whole family of pages, not for this file.

**#4 (S) — station 3's raw TeX behind a disclosure. APPLIED.** The typeset theorem, the line
range, the macro-expansion note and the verbatim source all stay in the DOM. The nine lines
of source now sit inside `<details>` with the summary "Inspect the source — lines
1075–1083, character for character", which keeps the `Quoted` tag beside it. The paragraph
that introduces the block was rewritten to match: the equation is set out with the five
abbreviations written out, and the TeX is one click away so the two can be compared without
taking the setting on trust. `<pre>` is still in MathJax's default `skipHtmlTags` and still
carries the belt-and-braces ignore classes, so nothing about the verbatim guarantee changes.

**#1 (M) — one detector is the protagonist of the shot. APPLIED.** Selection is persistent
and reversible, by three routes: click a detector in the range; click a row in the ledger;
or focus the range and use `←`/`→` to step and `Escape` to let go. `Enter`/`Space` picks one
up and puts it down. The canvas is now focusable and shows a focus ring, and the rows are
focusable too.

What the followed detector gets: a heavier accent ring; a dashed **ghost of where it was
before anything arrived**, labelled "before" in the electromagnetic mode and "dashed: where
it started" for the gravitational rings; its index drawn in accent rather than grey; and the
final displacement and velocity arrow it already had. When the front is going past it, an
extra ring in `--die` appears around it and its ledger row lights.

Every one of those cues is driven from tables the station had already computed. A new helper
walks the cumulative impulse table that already drives the animated arrow and reports the
detector times at which that detector has taken up 0.1 %, 5 %, 95 % and 99.9 % of the kick
it ends with; the 5 %–95 % interval is what "the front is going past" means, and the page
says so. In the gravitational mode the same read-off is made from the displayed profile.
**No new physical quantity is computed anywhere in this improvement**, and the ledger rows
of every detector light as their own fronts pass — up to 4 at once in the electromagnetic
mode and 8 in the gravitational one, which is the retardation spread made visible.

**#2 (M) — a two-trace oscilloscope for the followed detector. APPLIED.** A second figure
between the controls and the ledger, in two lanes.

* *Electromagnetic mode.* Upper lane: `E⊥` at that detector, sample by sample. Lower lane:
  the running integral `∫E⊥ dt` of exactly that lane. Dashed rule: the closed form, which
  knows only the two velocities. Both lanes are columns of the **same** cumulative Simpson
  table that drives the animated arrow. The only change to the engine is one extra stored
  column, `E[i] = fv[i] / jc[i]`: the stored integrand divided by the Jacobian
  `dt/dt' = 1 − n̂·β` the table already carries, which recovers the field itself. No solve,
  no quadrature rule and no window changed. Beside the
  traces: the closed-form Δv, the integrated Δv, their difference, the panel count that
  table settled on and its own endpoint residual. In the captures, following test charge 6
  (`75°, −32°`, `R = 8.45`) at the settings the station opens with prints
  `−8.672405462e-2` in both columns, a difference of `3.19e-16`, 1024 panels and an
  endpoint residual of `1.39e-17`.
* *Gravitational mode.* Upper lane: the news `r ∂ᵤh₊` passing that ring. Lower lane: the
  strain `r h₊` it has built up. Dashed rule: the permanent shift the constraint fixes from
  the angular flux. Beside them, `∫N du` over the whole record, by composite Simpson on the
  displayed profile over `u ∈ [−16, 16]` with 4096 panels: it prints `1.000000000000`, and
  it goes on printing that when the ringing slider is moved, which is the point — the ringing
  term starts and ends at zero and contributes nothing to the endpoint.

The station's own two data colours keep their page-wide meaning: `--die` for the radiative
signal going past, `--keep` for what is retained. The figure carries the `Controlled
numerical solve` tag in the electromagnetic mode and `Exact formula` in the gravitational
one, matching what each lane actually is. The provenance note under it says, in plain words,
why the permanent number survives: the upper lane goes up, comes back and ends at zero, and
the lower lane does not come back — it walks to the rule and stays.

The two M improvements are what the critic asked for as the flagship's missing "aim →
arrival → response → retained record", and they are views of existing tables. **The physics
of station 5 is untouched**: the same two engines, the same 15 detectors, the same solve, the
same ledger columns and the same residuals.

### R6. The keep list

Nothing on it was touched. Station 4's orthographic canvas, isolated-line view, peak ring,
forward zero, transverse arrow and live gauge-failure calculation are as they were. Station
5's two modes and both numerical engines are unchanged — the improvements above sit beside
them and read from them. Station 6's separation of radiation memory from Coulomb drift and
its three-route table are unchanged; the only edit inside it is the added crosswalk
sentence. Station 8's `ℓ ≤ 8` solve, single-`ℓ` mode, Green-kernel check, gauge disclosure
and low-pass explanation are unchanged. Station 9's causal/advanced split and its
independent late-limit predicate are unchanged; the two edits are the card title and the
grid. Station 1 remains the sole number-free schematic and keeps its tag — the FATAL 3 edit
is to a sentence of prose after the figure, and it makes the schematic's status clearer, not
weaker. The three ladder rungs and their scope disclosures are unchanged. The page-local
rail, immediate anchor jumps, theme control, scoped station ownership and the hoisted
reference core are unchanged.

Both fragment lanes' preserved decisions also hold: `spherePattern` is still the sole texel
evaluator; a missing palette token is still an integration error and no colour literal was
added (the only `#rrggbb` strings in either fragment remain the two in the header comment);
the four zero states still print zero with an explanation; the beam normalisation still
lives in the beam weight; station 5 is still described as a leading-`1/R` null-infinity
calculation in all three places; `window.PROLOGUE` is still created only by the EM core; the
masthead's "Start with the question" is still an `<a href="#w1">`; and
`#w10 .w10-rung.is-here` still has no negative inline margin.

### R7. Harness

A lane-local driver (`qa.mjs`, scratch, ~380 lines) serves
`docs/outreach/auditions/` over http and wraps **this file** in the same minimal
`<!doctype>/<head>/<body>` skeleton an artifact is published in, with the console,
`window.onerror`, `unhandledrejection` and capture-phase resource-error hooks installed
before any page script. `qa-run.mjs` still cannot drive the assembled page — its static,
Node-physics and interaction lanes all read `frag-gw.html` unconditionally, which is the same
reason both fragment lanes and the integrator wrote their own drivers. Playwright chromium
1.62.1, headless, outside the codex sandbox.

**PASS 89, FAIL 0, WARN 0. 20 screenshots.**

| lane | rows | result | what it checks |
|---|---:|---|---|
| matrix | 54 | PASS | light and dark x 390 / 768 / 1300 px: runtime errors, `console.error`, `scrollWidth <= clientWidth` on html and body, elements escaping the viewport without a scroller of their own, duplicate ids, every in-page anchor resolving, globals created, `[data-token-error]`, both libraries present |
| station 10 | 8 | PASS | every corner and edge builds links; all resolve; between them they reach `#w1`...`#w9`; the `viewBox` contains both lower corner boxes |
| rail | 2 | PASS | all ten rail links land on their station, at exactly 84 px, in both themes |
| station 5 | 12 | PASS | fired in both modes to a full 15-row ledger; a detector followed from the ledger, stepped with the keyboard and released with `Escape`; the oscilloscope draws both traces in both modes; no blank, `NaN`, `Infinity` or `undefined` readout; the arrival highlight reaches the ledger while the shot is scrubbed |
| interaction | 8 | PASS | 44 ranges, 4 number fields, 5 selects, 4 checkboxes, 26 buttons and 5 disclosures driven in both themes, then no errors, no non-finite readout, no sideways scroll |
| fallback | 5 | PASS | three.js blocked and WebGL forced to `null`; the whole CDN *and* both font origins blocked; `prefers-reduced-motion: reduce`; an unstamped root under each system colour scheme |

Numbers worth quoting:

| | |
|---|---|
| horizontal scroll | `html = body = viewport` at 390, 768 and 1300, both themes |
| escaping elements | none, in all six configurations |
| runtime and console errors | none, in all six, and none after the interaction sweep |
| globals added | `PROLOGUE`, `MathJax`, `THREE`, `__THREE__` - no stray |
| palette token errors | none |
| MathJax | 330 typeset containers, both themes, all three widths |
| station 10 | 6 elements, 15 links, all resolving; targets `#w1`...`#w9`, up from `#w1 #w5 #w8 #w9` |
| station 5 | fires to `15 / 15` in both modes; the oscilloscope draws 2 traces in both; up to 4 (EM) and 8 (GW) ledger rows lit at once while a shot is scrubbed |
| rail navigation | 10/10 land at exactly 84 px, both themes |
| three.js and WebGL blocked | no errors, the range still fires to 15 rows, the oscilloscope still draws |
| CDN and fonts blocked | no errors, no sideways scroll, TeX source in place of typeset math |
| unstamped root | `data-theme` absent under both system schemes; body paints `rgb(237,240,242)` / `rgb(13,20,24)` |
| file size | 507 081 bytes, against the spec's 5 MB ceiling |
| block identity | PASS after every edit (§R1) |

**Screenshots**, 20, all prefixed `pro-r1-` so that nothing the earlier lanes left in
`prologue/qa/` is disturbed:

* `pro-r1-{light,dark}-1300-{w5,w9,w10}.png` - the three stations the critic asked to be
  looked at, whole, in both themes.
* `pro-r1-{light,dark}-1300-w5-{em,gw}-followed.png` - the flagship with a detector
  followed and the oscilloscope open, in each mode and each theme.
* `pro-r1-{light,dark}-1300-provenance.png` - the provenance drawer, opened.
* `pro-r1-{light,dark}-1300-legend.png` - the masthead with its legend opened, where the
  FATAL 4 wording lives.
* `pro-r1-{light,dark}-{768,390}-w5.png` - the flagship at the two narrower widths.
* `pro-r1-nothree-1300-w5.png`, `pro-r1-nolibs-1300-w5.png` - the two degraded runs.

They were looked at, not merely produced; the three defects in §R4 came out of looking,
and so did the decision to widen station 10's `viewBox` past the prescribed two units.

### R8. Remaining gaps

1. **The rail's three marks and station 10's link map are not the same statement, and a very
   careful reader could notice.** The rail marks W5 and W8 as memory only, following the
   design document's corner assignment; station 10's soft corner now also links to W5,
   because W5's closed-form column really does evaluate the classical soft coefficient. Both
   are true — the rail says which corner a station is *about*, the map says which stations
   *showed* an element — but nothing on the page says so. Making the rail agree would mean
   changing an assignment the design document fixes, which is not this round's call.
2. **Station 10's per-element colour** is one accent for all six elements (§R5, #3). If a
   later round wants six, the palette needs two more highlight tokens chosen for the whole
   family of pages.
3. **three.js is still dead weight** (about 600 KB, referenced by nothing), still loaded
   because the integrator brief says to.
4. **The page is longer than it was**: 507 081 bytes, up from 477 771. The two station-5
   improvements are about 22 KB of that and the rest is prose.
5. Everything the two fragment lanes list as a remaining gap is still a remaining gap:
   `NOTES-frag-gw.md` §8 and `NOTES-frag-em.md` §10.6 — in particular `qa-run.mjs` is still
   a GW runner (this round wrote its own driver for the same reason the two lanes did),
   `retardedTime`'s absolute tolerance still costs station 6 its two largest radii at one
   hostile setting, station 4's maximum is still a search rather than a bound, and the Ward
   identity is still reported rather than derived — now said in four places instead of
   three.
6. **The reading measure is still 46 rem**, inherited deliberately; a decision for the whole
   family of pages.
