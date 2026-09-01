<!-- LANE BRIEF: audit of candidate communication formats for the SYK/JT
     results (outreach pivot). YOUR LANE (create/edit ONLY):
     docs/outreach/format-audit.md. No bd operations, no other files.
     Work fully autonomously; no network needed. -->

# Format audit: creative communication of the SYK/JT results

## Context

Traditional journal publishing is treated as dead for this purpose. The
campaign (this repo) has proved a set of results about a finite, relational
infrared triangle in SYK/JT gravity — soft theorem ↔ asymptotic symmetry ↔
memory effect — including: a decisive computation showing the balanced-pulse
calibrated susceptibility equals the DC soft residue at O(1/C) (numerics to
0.011%); a sharp refutation (the Shenker–Stanford butterfly shift has ZERO
plateau — a transient relational time delay, NOT memory); a two-register
definition of memory (D32 absolute response vs D33 calibrated relational
susceptibility, coinciding iff the ruler persists); honest HOLD verdicts and
scope fences throughout. Campaign assets that formats can exploit at low
marginal cost: a claims DAG with statuses (PROVED/SKETCH/CONJECTURE/REFUTED)
and dependencies; hierarchical Lamport-style proofs; numerics JSONs and a
green test suite; full adversarial proposer/critic transcripts (objection
trajectories like r1 FAIL(8) → repair → r2a PASS); a 202-page readable
labbook; a 676-entry database of Strominger's off-script lecture remarks.

## Target audience (binding)

A traditional physicist: knows QM, GR, basic QFT (up to QED, no more),
comfortable with many-body QM and Fock space. NOT assumed: holography, SYK,
JT, Schwarzian, celestial anything, modern frontend culture. Two
consequences: (a) the physics on-ramp must start from what they know
(two-level systems, harmonic chains, scattering, GW memory as reported in
LIGO-era coverage); (b) interactive/web polish that is routine in the
frontend world will read as ASTONISHING to this audience — the wow budget
is cheap, but wow must come from manipulating PHYSICS they understand, not
from chrome.

## Truth constraint (TJO directive, binding on every format)

No oversimplifications. Only true statements — no vague pop-science.
Speaking in generalities is allowed, and conjectures are allowed, but
everything asserted must be mathematically correct. Operationally:
simplification by RESTRICTION (an exactly stated special case) is
permitted; simplification by DISTORTION (cartoon dynamics, false analogies
presented as mechanism) is not. Interactive components must implement the
actual equations or exact solvable reductions of them. Wow must be won
without lying.

## Goal function

Maximize "wow" / magic for that audience. The experience should carry them
on a journey with the narrative arc WHY? → HOW? → WHAT?: first the burning
question (why should a quantum simulator remember anything? why is the
gravitational-wave memory effect a statement about symmetry?), then the
mechanism, only then the results. Creativity counts; ho-hum-in-frontend is
fine; ho-hum-for-a-physicist is fatal.

## The candidate formats

1. Bespoke HTML webapp: interactive components, nonlinear storytelling.
2. Gamification (generic).
3. Videos.
4. Podcast-type discussion.
5. AI "lecturer" controlling an HTML canvas, dynamically building a lecture
   via Socratic questioning of the individual viewer.
6. The claims DAG as the publication: interactive argument graph, statuses
   colored, edges clickable down to proofs/numerics/critic verdicts; the
   linear paper is just one guided path through the graph.
7. Executable paper: sliders on the decisive computation (βJ, C, pulse
   balance), reader watches the absolute signal die while the calibrated
   ratio plateaus; a "verify" button reruns the actual test suite.
8. Adversarial review as content: publish the proposer/critic transcripts
   as a readable/listenable drama (three voices: prover, critic,
   adjudicator).
9. Referee-mode toggle: one artifact, enthusiast reading vs skeptic reading
   (every claim rendered with scope fences and NOT-claimed statements).
10. The two-registers lab: hands-on toy — reader operates a detector and a
    ruler that may or may not persist, discovers D32 vs D33 themselves;
    GW strain vs SYK/JT side by side; win condition = rediscovering the
    definitional split.
11. Triangle-as-navigation: the IR triangle is the homepage; corners and
    edges are the map; click an edge → statement/proof/numerics/caveats.
12. "Ask the paper": RAG-grounded AI interlocutor constrained to PROVED
    rows and scope fences; refuses beyond scope.
13. Publish the side-channel: blackboard-voice recordings/transcripts of
    the authors (asides, confusions, retracted-conjecture anecdotes),
    indexed like the Strominger wisdom DB; dual-register toggle
    (rigorous voice ↔ blackboard voice).
14. Claim-granular citation + epistemic badges: permalinks per claim,
    machine-readable status manifests, subscribable status-upgrade diffs.
15. Interactive Lamport proofs: collapsible proof hierarchy, flyover at
    ⟨1⟩-level, expandable to definitions and named computations.
16. Negative results serialized: the lab log as episodes; refutations are
    plot twists, HOLD verdicts are cliffhangers.
17. Conjecture bounty board: precisely specified open problems (e.g. the
    held n=2 refutation) as public challenges feeding an adversarial
    review loop.
18. The detective game: player is the critic; given a plausible claim and
    data, find the failing hypothesis; levels built from the campaign's
    real objection history.

Bundling is allowed and encouraged: formats that are natural skins over a
shared substrate (claims DAG + executable numerics + AI mediator) may be
recommended as one pick if and only if the bundle has ONE coherent
audience-facing identity.

## Your task

Write `docs/outreach/format-audit.md`:

1. **Scoring table**, all 18: wow-for-physicists (1–10), creativity (1–10),
   fit to the why→how→what journey (1–10), feasibility from existing
   campaign assets (1–10), plus a one-line sharpest-criticism column. Score
   from the TARGET AUDIENCE's chair, not a web developer's and not a
   colleague-in-the-field's.
2. **Failure analysis**: for the top ~8, the single most likely way each
   fails to be magical for this audience (e.g. "wow decays after 90
   seconds", "requires SYK background the audience lacks", "reads as a
   gimmick to exactly this audience").
3. **Recommendation: exactly 3 picks** (bundles allowed per the rule
   above), each with: the audience-facing identity in one sentence; why it
   wins on wow for THIS audience; how the why→how→what arc runs through
   it; the on-ramp from QM/GR/QED-level knowledge to the SYK/JT results;
   the kill-risk and its mitigation; what existing campaign assets it
   consumes.
4. **Explicit cuts**: the strongest idea you nevertheless cut, and why.

Be opinionated. A sharp ranking with reasons beats diplomatic mush. You are
not choosing what is easiest to build; you are choosing what a
50-year-old GR professor forwards to three colleagues with the message
"you have to see this."
