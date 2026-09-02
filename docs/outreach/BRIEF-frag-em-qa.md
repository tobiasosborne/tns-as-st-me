<!-- LANE BRIEF (codex, tns-az6 sibling for the EM lane): physics-first
     critique of the Opus-built EM fragment. YOUR LANE (create/edit ONLY):
       docs/outreach/critic-frag-em-r1.md      (your report)
       docs/outreach/auditions/prologue/qa-run.mjs   (extend ONLY if a new
                                              numerical check is needed)
     Do NOT edit frag-em.html or em-core.js. No bd, no git. Write the
     report incrementally. -->

# Brief — frag-em.html physics critique and QA

Target: docs/outreach/auditions/prologue/frag-em.html (196 KB; stations
W2, W3, W4, W6, W7; the codex EM core is inlined verbatim in
`<script data-station="em-core">`). Builder report:
docs/outreach/auditions/NOTES-frag-em.md. Physics ground truth:
docs/outreach/auditions/prologue/em-core.js, em-core.test.mjs,
em-core-NOTES.md (its "may print" sentences and its "must not say" list
are binding on the page). Design document: docs/outreach/BRIEF-why-
prologue.md; contract: docs/outreach/AUDITION-SPEC.md. Sister report for
structure and standard: docs/outreach/critic-frag-gw-r1.md (same format;
same severity discipline).

## Part 1 — physics audit (FATAL first)

- Does every printed number come from the inlined core, unmodified? Diff
  the inlined block against em-core.js byte-for-byte. Look for any
  station-local re-implementation of physics, any eased animation
  standing in for a field, any interpolation presented as computation.
- W2: the Purcell/streamline construction — is the field-line picture
  the exact construction (both routes) and is the E⊥/E_r readout the
  core's? Check the collinear-kick restriction is stated where the
  reader sees it. Check the "bedrock" lecture quote against
  docs/strominger-wisdom/lectures/01-lvyyxkjwSCg-digest.md.
- W3: spectrum, soft coefficient, photon number — units and constants as
  the core NOTES specify; Weinberg's theorem quoted VERBATIM from
  refs/arxiv-1703.05448/soft_Arxiv_update.tex:1075-1082 (diff it); the
  classical↔quantum sentence exactly as the NOTES permit.
- W4: the polarization-summed sphere pattern; charge-conservation
  handling; the caveat banner; is the colour map honest (no log/gamma
  applied silently — if applied, is it labelled)?
- W6: the two-route identity — which quantity is printed, does the page
  say precisely what the NOTES say makes the identity TRUE (radiation-
  order term vs Coulomb drift)? Verify the 12-digit claim by running the
  core functions yourself in node with the page's default parameters.
- W7: the per-angle ledger equation and its TeX line quote; sphere-
  divergence vs field confusion; the antipodal geometry and the three
  lecture quotes against the digests (01 lines ~33, ~95-100, entry 12;
  02 line ~75), attribution format (video id + timestamp, "lecture
  remark").
- Every "must not say" item in em-core-NOTES.md: grep the fragment for
  each and report violations.

## Part 2 — contract, code, layout

Fragment contract compliance (one style + one script per section, id-
scoped selectors, no leaked globals except window.PROLOGUE.em, no
library loading, tokens only), rAF loops gated by IntersectionObserver
and reduced-motion, listener collisions, unhandled rejections, and the
THREE-absent path (the builder says the fragment has zero THREE
references — confirm). Run the numerical parts of qa-run.mjs that apply;
try the browser run (`node qa-run.mjs` with `?frag=frag-em.html`) — if
chromium cannot launch in your sandbox, say NOT RUN and do not guess.

## Report structure (docs/outreach/critic-frag-em-r1.md)

1. Verdict. 2. FATAL physics/truth items with line refs and exact fixes.
3. BUGS. 4. Top improvements ranked by wow/effort (W4 must be genuinely
delightful; W2 is the reader's first sight of the shell — does it land?).
5. Keep list. 6. What you could not verify. Every criticism ships with
its fix; do not pad; if the fragment is clean say so.
