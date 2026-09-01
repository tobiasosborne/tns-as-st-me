# Brief — the WHY prologue: the infrared triangle in its home setting

TJO verdict on audition r1 (corrected wording, binding): NO audition wins.
Each has liked and disliked parts. The Proof Atlas is distinguished ONLY in
that it is the sole presentation that starts with a proper "why?" — and even
its why is far too short, has no interactive animations, and is "abrupt and
pitiless" for a reader unfamiliar with soft factors. The format decision for
the SYK/JT material remains OPEN. Directive: at least 5–10 visualisations
illustrating the soft triangle BEFORE SYK/JT appears; 2D and 3D interactive
apps/games; explicitly: "I want to see a bunch of detectors or charges, in
3d with three.js maybe, I want to shoot grav waves or soft photons at them.
Try 2d first if that is too hard."

Deliverable: `docs/outreach/auditions/ir-triangle-prologue.html` — a
STANDALONE prologue page, "the infrared triangle in its home setting". It is
its own artifact; it does not belong to any of the three r1 formats. Same
audience (QM, GR, QFT≤QED, many-body), same binding contract
(`docs/outreach/AUDITION-SPEC.md` — truth constraint, tech contract,
register). Visual identity: may reuse the proof-atlas token palette and type
stack as a convenient starting system, WITHOUT implying the prologue is part
of that page.

## Truth constraint, applied to interactives (non-negotiable, as amended)

TJO amendment (verbatim): "exactly solvable is surely not necessary, just
numerically tractable!" Operationally: every animated/interactive quantity
is computed from the TRUE equations, either (a) a closed form displayed
beside it, or (b) an honest, controlled numerical solution of the displayed
equations — method named (quadrature rule, ODE integrator, harmonic
truncation…), convergence checked in-page or in the builder's QA, and the
truncation/step stated where it matters. What remains forbidden is cartoon
dynamics: easing curves pretending to be fields, invented waveforms, or
plausible interpolation presented as physics. Retardation geometry exact.
Where a wave "propagates", the field at each detector at each frame comes
from the retarded solution (closed-form or numerically evaluated), not an
eased animation. Schematic-only drawings are allowed but carry the SCHEMATIC
tag and no numbers. Formulas quoted from
`refs/arxiv-1703.05448/soft_Arxiv_update.tex` wherever they exist there
(quote by line); self-contained derivations displayed on-page where the repo
has no source (the butterfly-trial Exhibit A-1 pattern). Numerical freedom
widens the design space: arbitrary user-drawn pulse profiles, general
trajectories, and flux patterns are all welcome so long as the solver is
honest and its error is controlled.

## Physics substrate (the two exactly solvable engines)

**EM engine — the kicked charge.** A charge q moving with constant velocity
β_i receives an instantaneous kick at t=0, x=0 to β_f (smooth-pulse limit
noted). Everything follows exactly:
- Time domain: outside radius R=ct the field is the boosted Coulomb field of
  the OLD motion; inside, of the NEW; the spherical shell at R=ct carries the
  transverse radiation connecting them (the Purcell/Liénard–Wiechert
  geometric construction — derive it on-page; the transverse/radial ratio in
  the shell is elementary geometry). This discontinuity is the campaign-
  relevant "bedrock" (Strominger, Lecture 1: "this fact is going to sort of
  be the Bedrock of everything we do from here on" [lvyyxkjwSCg @ see
  docs/strominger-wisdom/lectures/01-lvyyxkjwSCg-digest.md, entry 9] — quote
  it, labelled as a lecture remark, secondary source).
- Frequency domain: the exact radiation amplitude of the kick current has
  the 1/ω pole with coefficient q[β_f/(1−n̂·β_f) − β_i/(1−n̂·β_i)]·ε — the
  CLASSICAL soft factor; display Weinberg's quantum soft theorem verbatim
  from soft_Arxiv_update.tex:1075-1082 next to it and state the exact
  relation (classical limit / single-emitter case), no hand-waving.
- Memory: a test charge at distance r receives momentum kick
  Δp = q_test ∫E_⊥ dt; the time integral of the radiation field equals the
  ω→0 (DC) component. COMPUTE BOTH ROUTES IN-PAGE (quadrature of the exact
  time-domain field vs the closed-form DC limit) and print the agreement to
  float precision — the soft↔memory edge as a live numerical identity.

**GW engine — null-burst memory on the sphere.** Linearized gravity at null
infinity: the memory ΔC_zz is sourced by the energy flux through null
infinity via the constraint equation (quote the memory-effect equations from
soft_Arxiv_update.tex's memory section — locate the supermomentum/constraint
formula in the TeX and cite lines). For a burst of null energy with angular
distribution T(n̂) = Σ_{ℓm} T_{ℓm} Y_{ℓm}, the sphere equation inverts
EXACTLY in spherical harmonics (the ℓ-dependent factors are algebraic;
ℓ=0,1 excluded — say why). Implement the exact ℓm solve (truncate at ℓ≤8,
stated), render the resulting PERMANENT deformation of rings of test masses
at each angle, with the transient burst passing at the retarded time.
Quote soft_Arxiv_update.tex:329 ("subtle DC effect… permanent shift") and
:336 ("Weinberg was scattering elementary particles, while Braginsky and
Thorne were scattering black holes, but this distinction is irrelevant in
the deep infrared!").

## The stations (10; order fixed)

**W1 — The question.** Short. One ring of test masses, one passing wave,
toggle "permanent strain" — the r1 atlas opener upgraded visually but still
SCHEMATIC-tagged; ends with: whether anything REMAINS different is the whole
subject. ≤1 screen.

**W2 — The bedrock (2D interactive).** The kicked charge's field lines,
exact Purcell construction: drag kick magnitude/direction and time slider;
old Coulomb outside R=ct, new inside, the connecting shell rendered from the
exact geometry; readout of E_⊥/E_r in the shell. The lecture-remark quote.
This is where the reader FIRST SEES that "information about the kick" lives
in an expanding shell whose DC content never dies.

**W3 — The same event, in frequency (2D).** Exact |A(ω,n̂)|² of the kick:
log-log spectrum flattening to the soft plateau as ω→0; slider on ω; the
1/ω pole displayed; extract the soft factor coefficient live and show it
next to Weinberg's theorem (TeX:1075-1082, verbatim). Side readout: soft
photon NUMBER ∫dω/ω diverges logarithmically — compute N(ω_min) live with a
cutoff slider (the IR divergence, exact, one sentence of interpretation).

**W4 — The soft factor on the celestial sphere (3D).** User builds a
scattering event: place 2–5 charged in/out momenta (draggable directions,
charge and speed controls); the sphere is painted with the exact
|Σ_k η_k Q_k β_k·ε/(1−n̂·β_k)|² angular distribution; rotate/zoom. Every
hard particle drags its own pole across the sphere. 3D via three.js
(pinned cdnjs r160+, script only) or hand-rolled projection — builder's
choice; MUST degrade to a legible static fallback if WebGL is absent.

**W5 — Shoot the detectors (THE GAME, 3D; flagship of the prologue).**
TJO's explicit ask. A range of detectors in 3D (three.js; if quality is at
risk, ship the 2D-canvas version and note 3D for r3 — 2D permitted by TJO).
Two modes:
- SOFT PHOTONS: an array of free test charges at various angles/distances;
  the user kicks the source charge (aim + strength); the exact radiation
  shell expands at c (retardation exact per detector), each test charge
  jitters transiently and RETAINS the exact velocity kick; per-detector
  ledger: Δv predicted by the DC formula vs Δv integrated — equal.
- GRAV WAVES: an array of test-mass rings; the user fires a null-energy
  burst with a chosen angular pattern (pick lobes / paint T(n̂) coarsely);
  the exact ℓm memory solve gives each ring its permanent deformation; the
  transient passes, the deformation stays. Scoreboard-style readout: which
  detectors remember, and by how much — angle dependence visible.
No points/badges — the "game" is aiming and seeing the physics respond;
every number on the ledger exact.

**W6 — Memory ⇒ the soft theorem was inevitable (2D).** The two-route
identity as its own station: pick any kick; the page computes ∫E_⊥dt by
quadrature AND the ω→0 closed form; print both to 12 digits with their
difference. One paragraph: a DC field component IS a pole at ω=0 — which is
why a scattering theory whose late-time fields carry memory MUST have a
universal soft pole. The triangle's first edge, earned.

**W7 — One conservation law per angle (2D + sphere).** The asymptotic-
symmetry corner made concrete: before/after angular profiles of the
Coulombic (1/r²) field of the kicked charge (exact boosted-Coulomb closed
forms); their difference angle-by-angle equals the DC radiation content at
that angle (the constraint at null infinity — quote the EM
constraint/conservation equation from the TeX with lines). Interactive:
select an angle, see the local ledger balance. Then the antipodal
interlude: a free particle drawn through a Penrose diagram enters at angle
θ and exits at the antipodal angle (exact geometry; interactive angle) —
with the Lecture-2 student remark ("it's not surprising when you think
about it the right way", digest 02 entry) and the honest caveat from the
wisdom DB: Strominger states the antipodal matching has no first-principles
derivation he knows of. Close with his "I kind of dislike this word
asymptotic symmetries… they are symmetries just like any other" (Lecture 1).

**W8 — The gravitational memory range (2D/3D).** The GW engine full-screen:
paint/pick the flux distribution, solve exactly, watch a lattice of rings
acquire permanent strain; the Braginsky–Thorne "deep infrared" quote; the
LIGO/pulsar-timing detection sentence from TeX:329 (quoted). If W5's GW
mode already carries this fully, W8 may instead deepen it (harmonic-by-
harmonic decomposition view: slider over ℓ showing which angular structures
of the burst survive into memory) — builder's judgment, no duplication.

**W9 — The hinge, with its hypotheses (2D).** Interactive Fourier bench:
build a response function from parts — a pole iA/(ω+i0) (residue slider), an
optional second real-axis pole, an optional damped resonance; the page
evaluates the EXACT inverse transform of the assembled rational function
(closed forms, displayed) and shows the time-domain response; the late
limit exists and equals −iωf̃|_{ω→0} exactly when the hypotheses hold —
break them and watch it fail. This is the atlas's repaired stop-01 hinge,
now discoverable instead of asserted.

**W10 — The triangle, assembled.** The three corners and three edges as an
interactive map where each element lights up and links back to the stations
that exhibited it (W2/W3 soft; W5/W6/W8 memory; W7 symmetry; W6/W9 the
soft↔memory edge; W7 the symmetry↔soft edge stated as Ward identity with
the TeX:1064 quote — reported, not derived). Then the pivot, verbatim in
spirit from the atlas: every corner assumed detectors whose rulers do not
change while measuring — what survives when the ruler is part of a thermal
state? → link to the Proof Atlas (Part II).

## The dimensional ladder (TJO steer, 2026-09-01, mid-build)

TJO: "Ideally I would love a 1d, 2d, 3d vis, each illustrating the IR
triangle on different systems (maybe the 1d version IS the SYK/JT story)".
And: "I unreasonably want this to be awesome".

Consequences: (a) THIS page is the 3+1-dimensional rung — the triangle in
its home setting (kicked charges, gravitational memory). (b) W10's pivot is
reframed as the LADDER, not a bare SYK/JT pointer: the same triangle can be
asked of lower-dimensional quantum systems — a 1D lattice of spins (where
this campaign has proved its own soft index theorem and computed kink
memory), and a 0+1D pair of black-hole boundary clocks (SYK/JT), where the
ruler itself is thermal. Present the ladder as three rungs with this page
as the top rung and the other two as coming attractions, one sentence of
honest content each — no overclaiming, no empty teasers. (c) The bar is
maximal: the flagship game (W5) and the sphere (W4) must be genuinely
delightful, not merely correct — motion, immediate response to input,
beauty in the field patterns; the truth constraint is not a license for
drabness.

## Interaction & register

The reader must never be punished for unfamiliarity: each station opens
with one plain-language paragraph and one familiar anchor (Coulomb field,
wave packet, interferometer) before any new object. Wisdom-DB quotes are
seasoning, one per station at most, always attributed as lecture remarks
(video id + timestamp from the digests), never load-bearing. Register per
the spec: good simple communication, cautious optimism; the interface gets
less glossy where numbers decide.

## Build process (multi-agent; fragment contract)

Because ten stations exceed one sitting, the build is split:
- **Builder A (EM lane):** stations W2, W3, W4, W6, W7 → fragment file
  `docs/outreach/auditions/prologue/frag-em.html`.
- **Builder B (GW + frame lane):** stations W1, W5, W8, W9, W10 + masthead/
  intro/outro copy → fragment `docs/outreach/auditions/prologue/frag-gw.html`.
- **Fragment contract:** each fragment = a sequence of
  `<section class="stop" id="wN">…</section>` blocks, each followed by ONE
  `<script data-station="wN">` containing an IIFE that touches only its own
  section's DOM (query scoped by id); NO shared globals except
  `window.PROLOGUE` (a namespace the integrator owns); all colors via the
  proof-atlas token names (copy its `:root` palette into a comment header
  for reference; do NOT emit `<style>` in fragments — put any
  station-specific CSS in a `<style data-station="wN">` block scoped by id
  selectors); math via MathJax `\[ \]` (integrator loads it once); three.js
  assumed available as global `THREE` (integrator loads pinned cdnjs
  script once) — degrade gracefully if absent.
- **Integrator (Opus):** assembles `ir-triangle-prologue.html` — masthead +
  rail (10 stations) + shared styles + the two fragments in order + single
  MathJax + single pinned three.js + QA (both themes, 390/768/1300px, no
  horizontal scroll, JS error sweep, WebGL-absent fallback). The prologue is
  standalone; do NOT edit proof-atlas.html. Do NOT restructure fragment
  physics.
- Then: codex critic (physics-correctness first — every closed form checked,
  every quadrature-vs-closed-form identity verified), one repair round,
  republish.
