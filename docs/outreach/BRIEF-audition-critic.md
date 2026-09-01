<!-- LANE BRIEF: constructive critic for ONE outreach audition. The
     orchestrator names your target file and your output file at launch.
     YOUR LANE (create/edit ONLY): your named output file
     docs/outreach/critic-<name>-r1.md. No other files, no bd operations. -->

# Audition critic brief — constructive, ranked, actionable

You are reviewing an audition prototype: a single self-contained HTML
vertical slice communicating this campaign's SYK/JT results to a
traditional physicist (QM, GR, QFT≤QED, many-body/Fock space). This is an
IMPLEMENTATION review: the decision to build this format is already made.
Your job is to make it better, not to relitigate the format. Sharp
observations, concrete fixes.

Read first: docs/outreach/AUDITION-SPEC.md (the binding contract — truth
constraint, provenance rules, tech contract, register),
docs/outreach/format-audit.md (your target's Pick section — the design
document and its kill-risk analysis), the builder's final-report notes if
present, and THEN the target HTML file itself, fully — read the actual
markup, styles, scripts, and embedded data; trace the reader's path
screen by screen; evaluate the JS logic (does the code actually evaluate
the equations it displays? does it interpolate where it claims not to?).
Cross-check embedded data and quoted statements against the repo ground
truth (claims/CLAIMS.md, definitions.md, theory/lanes/syk-jt/,
numerics/results/schwarzian_memory.json, the critic verdict files).

## Output structure (your named output file)

1. **Verdict** (one paragraph): would the target physicist forward this?
   Where does the wow actually land, and where does it leak?
2. **Truth-constraint audit** (FATAL items): every mathematically wrong,
   overclaiming, provenance-untagged, silently-interpolated, or
   misquoted item, with file line references and the exact correct
   statement or required label. These are must-fix.
3. **Top 10 improvements**, ranked by (impact on wow for the target
   audience) / (effort). Each: the problem in one sentence; the concrete
   fix in enough detail that a builder can implement it without asking
   questions (name the section/element, describe the interaction or
   copy change, give replacement wording where wording is the issue);
   an effort tag (S/M/L).
4. **Journey check**: walk the why→how→what arc as the target reader;
   name the exact moment attention would be lost or trust would be
   damaged, and the fix.
5. **Register check**: any pop-sci drift, arrogance, or gloss at the
   decisive moment (the spec demands the interface get LESS glossy
   there); quote the offending copy and rewrite it.
6. **Keep list**: what is genuinely excellent and must NOT be touched in
   repair — be specific, so the repair round does not regress it.

Tone: a senior colleague invested in this succeeding. Every criticism
ships with its fix. Do not pad; if only 7 improvements are real, list 7.
