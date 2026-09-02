<!-- LANE BRIEF (codex, tns-170): physics-first critique of the ASSEMBLED
     prologue page. YOUR LANE (create/edit ONLY):
       docs/outreach/critic-prologue-r1.md
     Do NOT edit the page, the fragments, or the core. No bd, no git.
     Write the report incrementally. -->

# Brief — ir-triangle-prologue.html critique r1

Target: docs/outreach/auditions/ir-triangle-prologue.html (the standalone
WHY prologue: masthead, W1–W10, outro, provenance block). It is the
integration of two fragments that each went through a codex critique and
an Opus repair round; read those first so you do not re-raise settled
items or re-litigate evidence-backed rejections:
  docs/outreach/critic-frag-em-r1.md + docs/outreach/auditions/NOTES-frag-em.md (§10 repair ledger)
  docs/outreach/critic-frag-gw-r1.md + docs/outreach/auditions/NOTES-frag-gw.md
  docs/outreach/auditions/NOTES-prologue.md (integrator report)
Design document: docs/outreach/BRIEF-why-prologue.md. Contract:
docs/outreach/AUDITION-SPEC.md. Physics ground truth for the EM half:
docs/outreach/auditions/prologue/em-core.js + em-core-NOTES.md ("may
print" / "must not say" lists are binding). Ground-truth TeX:
refs/arxiv-1703.05448/soft_Arxiv_update.tex (quote by line). Lecture
remarks: docs/strominger-wisdom/lectures/*-digest.md.

## What to audit

1. **Regressions from integration.** Diff each fragment's sections
   against their copies in the assembled page (ignoring the integrator's
   documented changes in NOTES-prologue.md): any physics, prose, or
   provenance text altered? Any station script now sharing state or
   colliding on ids/listeners? Is the em-core block byte-identical to
   em-core.js (or the documented hoisted copy)? Does the page load
   exactly one MathJax and one three.js, both from the allowed CDNs,
   pinned?
2. **The whole-page truth audit.** Now that W1–W10 sit together: do any
   two stations contradict each other (conventions, signs, names for the
   same object — the EM lane calls the soft vector S⃗/N⃗/M⃗ in different
   stations and the repair ledger explains why; is that acceptable on one
   page, or does a reader lose the thread?); does the masthead/outro/
   provenance block make claims the stations do not earn; is W1 the only
   schematic and tagged; does W10's map link every corner and edge back
   to the station that actually exhibited it; are the three ladder rungs
   one honest sentence each with faithful scope.
3. **Physics spot-checks (fresh eyes).** Independently recompute three
   numbers the page prints in its default state (one EM, one GW, one W9)
   in node from the core / your own implementation and compare.
4. **Journey check for the target physicist** (QM, GR, QFT≤QED, many-
   body, unfamiliar with soft factors): walk the why→how→what arc; name
   the exact moment attention or trust would be lost; is the first
   screen of each station a plain paragraph plus a familiar anchor
   before any new object; register (no pop-sci, less gloss where numbers
   decide).
5. **Delight.** W4 and W5 must be genuinely delightful. Say concretely
   what is and is not, with fixes ranked by wow/effort.

## Report structure (docs/outreach/critic-prologue-r1.md)

1. Verdict: would the target physicist forward this? Publishable after
   one repair round, or not?
2. FATAL (must-fix): regressions, truth-constraint failures,
   contradictions, provenance errors — line refs + exact fixes.
3. BUGS and contract items.
4. Top improvements ranked by wow/effort (S/M/L), concrete enough to
   implement without questions.
5. Keep list.
6. What you could not verify (chromium will likely not launch in your
   sandbox: say NOT RUN, do not guess; the integrator's screenshots in
   docs/outreach/auditions/prologue/qa/ are evidence you may read if you
   can open PNGs).
Every criticism ships with its fix. Do not pad. If it is clean, say so.
