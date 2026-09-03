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
