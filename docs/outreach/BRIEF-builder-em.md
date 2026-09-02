<!-- LANE BRIEF (Opus builder A, tns-fse): the EM lane of the IR-triangle WHY
     prologue. YOUR LANE (create/edit ONLY):
       docs/outreach/auditions/prologue/frag-em.html
       docs/outreach/auditions/NOTES-frag-em.md
     No other files. No bd operations. No git operations. Write the
     fragment to disk EARLY and after EVERY station (a previous builder of
     this lane was lost to a network outage before writing anything). -->

# Brief — Builder A: stations W2, W3, W4, W6, W7 → frag-em.html

Read, in order: docs/outreach/BRIEF-why-prologue.md (the design document —
all of it, especially the truth constraint, the EM engine, W2/W3/W4/W6/W7,
the fragment contract, and "The dimensional ladder" for the register);
docs/outreach/AUDITION-SPEC.md (binding contract); the header comment and
the W1 + W9 sections of docs/outreach/auditions/prologue/frag-gw.html (the
sister fragment — MATCH its contract conventions exactly: one
`<section class="stop" id="wN">`, then ONE `<style data-station="wN">` with
every selector scoped under `#wN`, then ONE `<script data-station="wN">`
IIFE; palette tokens read via getComputedStyle; no globals; THREE and
MathJax assumed loaded by the integrator; graceful fallback if THREE is
absent); the `:root` palette of docs/outreach/auditions/proof-atlas.html.
Load the artifact-design and dataviz skills before designing anything.

## The physics ground truth: the codex EM core

A codex lane is concurrently writing the exact EM engine:
  docs/outreach/auditions/prologue/em-core.js         (browser-safe IIFE → window.PROLOGUE.em)
  docs/outreach/auditions/prologue/em-core.test.mjs   (node tests; identities + residuals)
  docs/outreach/auditions/prologue/em-core-NOTES.md   (conventions, derivations, TeX line refs,
                                                       the exact sentences the page may print,
                                                       the list of things the page must NOT say)
Its spec is docs/outreach/BRIEF-em-core.md — read it now so you know the API
shape. It may not exist yet when you start. Plan of work:
1. Design + copy + markup + interaction scaffolding + rendering code for
   all five stations first (this is where YOUR judgment is final: layout,
   motion, colour, what the reader sees first, how the controls feel).
   Render from a thin adapter `P = window.PROLOGUE.em` so the physics is
   swappable.
2. Before finalising any numeric display, check whether em-core.js and
   em-core-NOTES.md exist (poll with ls every few minutes while you work;
   allow up to ~40 minutes). When they do: read the NOTES fully, inline
   em-core.js VERBATIM in a `<script data-station="em-core">` block placed
   before `#w2` (this is the one permitted use of window.PROLOGUE), wire
   every readout to its functions, run `node em-core.test.mjs` yourself
   and copy the residual table into your NOTES. Every sentence about the
   physics that the NOTES marks as "may print" is quotable; anything in
   its "must not say" list is forbidden.
3. If after ~40 minutes the core has not landed, implement the physics
   yourself from BRIEF-em-core.md with the same API names and a
   `<!-- PHYSICS: builder-implemented, pending codex core -->` marker at
   the top of the fragment, and say so in your NOTES; the integrator will
   swap the core in.

## Stations (from the brief; design freedom is yours, physics is not)

- **W2 The bedrock** — 2D canvas. Kicked charge, exact Purcell/Liénard–
  Wiechert field lines: drag kick magnitude/direction, time slider, old
  Coulomb outside R=t, new inside, the connecting shell from exact
  geometry; live readout E⊥/E_r in the shell. Lecture-remark quote
  (digest docs/strominger-wisdom/lectures/01-lvyyxkjwSCg-digest.md,
  entry 9 / lines ~95-100: "…the Bedrock of everything we do from here
  on"), attributed as a lecture remark with video id + timestamp.
- **W3 Same event, in frequency** — exact spectrum d²I/dωdΩ on log-log,
  flattening to the soft plateau; ω slider; the 1/ω amplitude pole; the
  soft coefficient extracted live and displayed beside Weinberg's theorem
  quoted VERBATIM from refs/arxiv-1703.05448/soft_Arxiv_update.tex:1075-
  1082 (MathJax); the exact classical↔quantum relation sentence from the
  core NOTES. Photon number N(ω_min) with a cutoff slider (the log IR
  divergence), one sentence of interpretation.
- **W4 The soft factor on the celestial sphere** — 3D (three.js as global
  THREE, pinned by the integrator; if absent, a hand-rolled orthographic
  projection to canvas MUST still render a legible sphere). Reader
  places 2–5 charged in/out momenta (draggable directions, charge and
  speed controls, charge conservation handled per the core NOTES); the
  sphere is painted with the exact polarization-summed |soft factor|²;
  rotate/zoom; each hard particle drags its own pole. This must be
  DELIGHTFUL: immediate response, beautiful field pattern, sensible
  colour map (dataviz skill: sequential palette, validated on both
  surfaces).
- **W6 Memory ⇒ the soft theorem was inevitable** — the two-route
  identity as its own station: pick any kick, the page computes the
  quadrature route and the closed-form route and prints both to 12
  digits with their difference (the core NOTES tell you exactly which
  quantity makes this identity TRUE as stated — obey it; show the
  Coulomb-drift term separately if the NOTES say so). One paragraph: a
  DC field component IS a pole at ω=0.
- **W7 One conservation law per angle** — before/after angular profiles
  of the Coulombic 1/r² field (exact boosted-Coulomb), the per-angle
  ledger from the constraint at null infinity (quote the TeX equation
  and lines that the core NOTES identify); select an angle, see the
  balance. Then the antipodal interlude: a free particle through a
  Penrose diagram entering at θ and exiting antipodally (exact map from
  the core; interactive angle); the Lecture-2 student remark ("it's not
  surprising when you think about it the right way", digest 02 line ~75);
  the honest caveat (Lecture 1 digest entry 12: no first-principles
  derivation known to him); close with "I kind of dislike this word
  asymptotic symmetries…" (Lecture 1 digest line ~33). Quote these
  exactly as the digests have them, with video id + timestamp, labelled
  as lecture remarks (auto-captions), never load-bearing.

Each station opens with one plain-language paragraph and one familiar
anchor (Coulomb field, wave packet, interferometer) before any new
object. Register: good simple communication, cautious optimism; the
interface gets LESS glossy where numbers decide. SCHEMATIC tag on any
drawing that is not computed. No pop-sci; no invented waveforms; no
easing that pretends to be a field.

## Engineering constraints

- Single fragment file, target 120–180 KB; no external assets beyond the
  integrator's MathJax + three.js; images inline SVG or canvas.
- requestAnimationFrame loops must pause when the section is offscreen
  (IntersectionObserver) and respect prefers-reduced-motion.
- No horizontal scroll at 390/768/1300 px; both themes via the tokens.
- Test as you go: a quick local harness is fine (a scratch wrapper page
  with the proof-atlas `:root` block, MathJax + three.js from cdnjs) —
  keep it in your scratch directory, NOT in the repo. Playwright chromium
  is available (`npx playwright` / ~/.cache/ms-playwright) for a
  JS-error sweep and screenshots at the three widths; do it before you
  finish. If the codex lane's docs/outreach/auditions/prologue/
  qa-harness.html + qa-run.mjs exist by then, use those instead.

## Finish

docs/outreach/auditions/NOTES-frag-em.md: what was built per station,
the physics source used (core inlined at what commit-time / or builder-
implemented), residual table, QA results (errors, widths, themes,
THREE-absent), known gaps, and the three design decisions you want the
integrator to preserve. Then stop.
