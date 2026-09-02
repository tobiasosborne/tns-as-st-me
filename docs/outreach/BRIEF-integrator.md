<!-- LANE BRIEF (Opus integrator, tns-ur8): assemble the standalone WHY
     prologue page from the two repaired fragments. YOUR LANE (create/edit
     ONLY):
       docs/outreach/auditions/ir-triangle-prologue.html   (the deliverable)
       docs/outreach/auditions/NOTES-prologue.md           (your report)
       docs/outreach/auditions/prologue/qa/                (screenshots)
     Do NOT edit the fragments, em-core.js, proof-atlas.html, or any other
     file. No git, no bd. Write the page to disk early and after every
     assembly step. -->

# Brief — integrator: ir-triangle-prologue.html

Inputs (read all, in this order):
1. docs/outreach/BRIEF-why-prologue.md — the design document: stations
   W1–W10 in fixed order, the dimensional ladder, interaction & register,
   the fragment contract and the integrator's duties.
2. docs/outreach/AUDITION-SPEC.md — binding contract (truth constraint,
   tech contract: single self-contained file, scripts only from cdnjs /
   jsdelivr, MathJax 3 SVG output, no external CSS; artifact-compatible;
   both themes; no horizontal scroll at 390/768/1300).
3. docs/outreach/auditions/proof-atlas.html — copy its `:root` palette
   for both themes (light default, dark under `[data-theme="dark"]` and
   the prefers-color-scheme media query with the `:root:not([data-
   theme="light"])` guard) and its type stack as the starting system.
   The prologue is NOT part of the atlas; no shared chrome that implies
   it is.
4. The two fragments and their notes:
   docs/outreach/auditions/prologue/frag-em.html (+ NOTES-frag-em.md)
   docs/outreach/auditions/prologue/frag-gw.html (+ NOTES-frag-gw.md)
   and the critic reports docs/outreach/critic-frag-em-r1.md,
   critic-frag-gw-r1.md (know what was fixed and what was rejected with
   evidence; do not re-litigate).
5. docs/outreach/auditions/prologue/qa-harness.html + qa-run.mjs — the
   codex QA harness; reuse its checks on the assembled page.

## Assembly

- Page order: masthead/intro (from frag-gw's `w0-masthead`), W1 (gw),
  em-core script block, W2, W3, W4 (em), W5 (gw), W6, W7 (em), W8, W9,
  W10 (gw), outro (gw). Move the `<script data-station="em-core">` block
  to just before W2 (or hoist it to the head after the libraries — your
  call; it must run before any EM station script).
- Shared styles: one `<style>` in the head with the palette, type
  stack, `.stop` layout, the station rail (10 stations, sticky or
  drawer at narrow widths, current-station highlight via
  IntersectionObserver), MathJax display sizing, reduced-motion
  defaults. Keep each fragment's `<style data-station>` and `<script
  data-station>` blocks intact and in order; do not merge or rewrite
  them; do not restructure fragment physics.
- Libraries: ONE MathJax 3 (cdnjs, SVG output, tex-svg) and ONE pinned
  three.js from cdnjs (r160 or later, the UMD build `three.min.js`)
  loaded BEFORE any station script. Per the NOTES, frag-em has zero
  THREE references and frag-gw degrades gracefully without it; still
  load it once as the brief specifies, and keep the THREE-absent path
  working.
- Title: `<title>` a short name (this is the artifact's tab name);
  first 8 KB of the file. Favicon is set at publish time, not in-page.
- Cross-links: W10 lights up elements linking back to the stations by
  id (`#w2` …) — verify every anchor in both fragments resolves in the
  assembled page; add a "Part II: Proof Atlas" outro link as a plain
  external link placeholder the orchestrator will fill (leave `href="#"`
  with `data-atlas-link`), do not invent a URL.
- Provenance block at the end (collapsed `<details>`): the TeX lines
  quoted, the digests quoted, the harness residual tables from both
  NOTES, and the sentence "W1 is a number-free schematic; every other
  moving quantity is a closed form or a stated numerical solve" —
  exactly as repaired in frag-gw.

## QA (mandatory, with evidence)

Run qa-run.mjs against the assembled page (adapt the harness invocation
or write a 20-line wrapper in your scratch dir; playwright chromium works
outside the codex sandbox: `npx playwright`, browsers under
~/.cache/ms-playwright). Required: both themes × 390/768/1300; zero JS /
console errors; document.scrollWidth <= innerWidth everywhere; every
range/button/select in every station exercised; W5 fired in both modes;
THREE-absent run (route-block three.js) clean; MathJax-absent run does
not throw; rail navigation works; anchors resolve; file size printed;
screenshots per station per theme at 1300 px and a full-page at 390 px
saved under prologue/qa/. LOOK at the screenshots (you can read PNGs)
and fix layout collisions, overflow, unreadable overlays, and any station
whose first screen does not show its plain-language paragraph plus its
familiar anchor before the new object.

## Finish

NOTES-prologue.md: assembly decisions, library versions pinned, harness
summary table, screenshot list, anything you changed outside pure
assembly (should be near-empty; justify each), remaining known gaps for
the codex critic round. Reply with a short report.
