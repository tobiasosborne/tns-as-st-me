<!-- LANE BRIEF (codex, tns-az6): QA + constructive critique of the
     committed-but-unverified GW-lane fragment. YOUR LANE (create/edit ONLY):
       docs/outreach/critic-frag-gw-r1.md            (your report)
       docs/outreach/auditions/prologue/qa-harness.html
       docs/outreach/auditions/prologue/qa-run.mjs
     Do NOT edit frag-gw.html (an Opus repair agent does that from your
     report). No bd operations. No git operations. Write the report
     incrementally (network outages kill lanes; disk survives). -->

# Brief — frag-gw.html QA and physics critique

Target: docs/outreach/auditions/prologue/frag-gw.html (165 KB; stations
W1, W5 game, W8, W9, W10 + masthead/outro). Its builder was killed during
its own QA phase; its last words were that its QA harness had bugs. Treat
the fragment as structurally complete and UNVERIFIED.

Read first: docs/outreach/AUDITION-SPEC.md (binding contract),
docs/outreach/BRIEF-why-prologue.md (design document: truth constraint as
amended, GW engine spec, stations W1/W5/W8/W9/W10, the dimensional ladder,
the fragment contract), then the fragment fully — markup, styles, scripts.
Ground truth for quotes: refs/arxiv-1703.05448/soft_Arxiv_update.tex, by
line (the fragment header lists the lines it claims to quote — check each
quote verbatim against the TeX). Lecture-remark quotes: check against
docs/strominger-wisdom/lectures/*-digest.md by video id.

## Part 1 — physics audit (FATAL items first)

Trace the JS of every station and check the mathematics it implements:
- W5 GW mode / W8: the spherical-harmonic solve of the memory constraint
  (TeX :2633, :2635, :2638). Verify the operator eigenvalues used for
  D_z² / the ℓ-dependent inversion factors, the exclusion of ℓ=0,1 and
  the stated reason, the normalisation of Y_ℓm and of the flux, the
  Green's function sign, and the geodesic-deviation map (:2590-2594) from
  ΔC_zz to the ring deformation. Reimplement the solve independently in a
  scratch node script (under your lane files or inline in qa-run.mjs) and
  compare numbers against the fragment's functions for a few flux
  patterns (extract the fragment's functions by evaluating its IIFEs in
  jsdom/playwright and calling them, or by copying them out).
- W5 soft-photon mode: the exact retardation per detector, the velocity
  kick formula and the "Δv predicted vs Δv integrated" ledger — is the
  integration a real quadrature of the displayed field or an eased
  animation? (Cartoon dynamics is forbidden by the truth constraint.)
- W9: the closed-form inverse Fourier transforms of the assembled
  rational response function (pole iA/(ω+i0), second real-axis pole,
  damped resonance) — verify each closed form analytically; verify the
  "late limit equals −iω f̃|_{ω→0} exactly when hypotheses hold" claim
  and that breaking a hypothesis produces the failure the page shows.
- W1: is it SCHEMATIC-tagged as required? Any numbers shown?
- W10: the ladder's three rungs — one sentence of honest content each,
  no overclaiming; the Ward-identity statement is REPORTED with :1064.
For each defect: line number, what is wrong, the exact correct statement
or code change.

## Part 2 — contract and code audit

Fragment contract (BRIEF section "Build process"): one <style
data-station> and one <script data-station> per section, selectors scoped
by id, no globals except window.PROLOGUE, no library loading, palette by
proof-atlas token names only. Check for: leaked globals, duplicate ids,
listeners on document/window that could collide with other fragments,
requestAnimationFrame loops that never stop (CPU when offscreen), missing
THREE-absent / WebGL-absent fallback paths, reduced-motion handling,
unhandled promise rejections.

## Part 3 — headless run (playwright)

Playwright chromium is installed (`@playwright/cli` globally; browsers
under ~/.cache/ms-playwright). Build a reusable harness:
- `qa-harness.html`: a wrapper page that (a) copies the `:root` palette
  block(s) from docs/outreach/auditions/proof-atlas.html for BOTH themes
  (light default; dark under `[data-theme="dark"]` and the prefers-color-
  scheme media query, exactly as proof-atlas does), (b) loads MathJax 3
  (SVG output) and pinned three.js r160+ from cdnjs as the integrator
  will, (c) injects one or more fragment files given by query string
  (`?frag=frag-gw.html,frag-em.html`) via fetch + innerHTML with scripts
  re-executed in order (script tags inserted via innerHTML do not run —
  clone them), (d) exposes `window.__qa = {errors:[], warnings:[]}`
  collecting window.onerror, unhandledrejection and console.error.
- `qa-run.mjs`: a node script driving playwright over the harness (serve
  the prologue directory with a tiny static server on localhost),
  running: both themes × viewports 390/768/1300 px; a scroll-through
  with screenshots per station into docs/outreach/auditions/prologue/qa/
  (you may create this directory — it is inside your lane); a
  no-horizontal-scroll check (document.scrollWidth <= innerWidth); an
  interaction smoke test that clicks every button/range in each station
  and fires the W5 game once in each mode; a THREE-absent run (block the
  three.js request via route interception) asserting the fallback
  renders and no errors; a console-error sweep. Print a summary table.
  NOTE: codex network access is sometimes DNS-blocked; if the CDN cannot
  be reached from your run, say so, run the THREE-absent/MathJax-absent
  path anyway, and mark the CDN-dependent checks as NOT RUN.
Run it; put the summary and the screenshot list in the report. Read the
screenshots yourself if you can (they are your evidence for layout).

## Report structure (docs/outreach/critic-frag-gw-r1.md)

1. Verdict paragraph (is the fragment ready to integrate after repair?).
2. FATAL: physics/truth-constraint items (must-fix, with fixes).
3. BUGS: JS errors, contract violations, layout failures found by the
   headless run (with fixes).
4. Top improvements ranked by wow/effort for the target physicist
   (QM, GR, QFT≤QED, many-body), each with a concrete fix and S/M/L tag.
   The bar: W5 must be genuinely delightful, not merely correct.
5. Keep list: what must not be touched in repair.
6. Harness usage: exact commands to rerun qa-run.mjs, so the integrator
   reuses it on the assembled page.
Every criticism ships with its fix. Say plainly if you could not verify
something. Do not pad.
