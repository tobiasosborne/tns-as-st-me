<!-- ROLE: live state. UPDATE POLICY: every session end + every phase boundary. -->

# HANDOFF — live state

Updated: 2026-09-01, session 11 (Strominger wisdom + batch-13 + Liouville).
Read order gate: CLAUDE.md → **PRD.md (the process constitution — where it
conflicts with older habits recorded here or anywhere, PRD WINS)** →
HANDOFF_MPS_SOFT_THEOREM.md → this file → paper/skeleton.md.

## Session 11 — wisdom-of-Strominger database, refs batch-13, Liouville rung

**Wisdom of Strominger (tns-t66, CLOSED).** TJO directive: mine the SIDE
REMARKS of Strominger's video lectures, not the arXiv-notes content, into a
queryable secondary source. Built: 16 cleaned timestamped transcripts in
`refs/strominger-videos/` (the 10-lecture Harvard IR-structure course, the
CSTQ colloquium, 5 extra talks; pipeline `scripts/vtt2md.py` + current
yt-dlp — the system yt-dlp 2024.04 is too old for subtitles), a 41-item
source manifest (`docs/strominger-video-manifest.md`; PIRSA/Cornell have no
captions), and `docs/strominger-wisdom/`: INDEX + 16 digests + 22 topic
files (676 entries) + **campaign-hooks.md (30 hooks — read this first)**.
Highest-value finds: (i) lecture-9 "the word calibrated is extremely
important" vs Strominger's extra-05 "flat connections are physical, you
don't care about the device" — an explicit inter-source TENSION mapping
onto the D32/D33 two-register ruling (external support that the split is
substantive); (ii) extra-01: finite systems generically have LESS symmetry
than their infinite limits (AdS3 cutoff cautionary tale) — predicts the
shape of the R2 refuted-orbit finding; (iii) antipodal matching has no
first-principles proof ("sitting there for 130 years") and its firmness
varies across talks; (iv) a hooks-NOT-found section (no lattice/MPS, no
SYK/JT, no measurement-cost material in the corpus — don't re-search).
Cautions: lecture 9 is GUEST-lectured (likely Zhiboedov — never attribute
to Strominger); three famous-sounding asides are verbatim in the written
notes (cite TeX, list in INDEX §4.3); the whole database is secondary —
NOT L3 ground truth. Raw VTTs are gitignored (regenerable).

**Refs batch-13 (tns-8gu, CLOSED).** All 21 skeleton-cited ids without
local TeX fetched + title-verified (LEDGER Batch 13); the companion paper's
L3 gate section is DISCHARGED in `paper/skeleton-syk-jt.md`. One real bug
found: the C3 universality-bound citation **2201.03650 was the wrong id**
(a BKT paper); correct Kruthoff id **2204.09685** fetched+verified and
substituted at every occurrence (skeleton + deep-sweep doc). The stale
"companion-cite-notes.md does not exist" UNBACKED flag was corrected (it
exists and records the 1408.6560 mismatch). **TJO companion prose writing
is now fully unblocked on references.**

**Liouville rung (tns-7wd, CLOSED — ladder complete).** codex, 904-line
Lamport report `theory/lanes/syk-jt/liouville-rung-report.md`: Q1
HOLD/underdetermined — the large-p sources do not fix the microscopic
two-time forcing, so plateau existence is not determined; conditionally,
IF the completed sourced problem satisfies the displayed relaxation
condition (L.23) THEN the plateau survives and equals the DC residue.
Q2: first truncation-lifting correction δv = 2/(βJ) + O((βJ)⁻²). Q3:
Schwarzian butterfly decay recovered; no controlled finite-v reversal.
Absolute-decay scale T ~ p/κ sits outside the controlled 1/p window
(echoes the ED rung's non-overlap one rung up). NO CLAIMS merge proposals;
per PRD value gate no critic rounds spent.

**Resume order for session 12:** (1) TJO writes companion prose from
`paper/skeleton-syk-jt.md` (references all local now; consult
`docs/strominger-wisdom/campaign-hooks.md` for framing support, citing TeX
only); (2) TJO decision: C5 headline strength; (3) optional corner-A lane:
LMZ relational construction to n=2 (still the named open route); (4)
main-campaign queue unchanged: tns-bfc, tns-25h, tns-94j (the D32/D33
naming decision — note hook H1 and the H10 higher-moments disagreement
bear on it directly), tns-kng, tns-bsk, tns-7ou.

## Session 10 — SYK/JT: the decisive computation, two memory registers, corner A, companion paper

**TJO directives this session (all persisted):** (i) execute the SYK/JT
decisive computation with codex; (ii) OPERATIONAL RAZOR sharpened — "this
question cannot be correctly answered unless you specify the physically
allowed observables clearly," now a lane-scoped 3-layer C*-algebra spec
(theory/lanes/syk-jt/observables-spec.md: Layer 0 even-CAR bedrock /
Layer 1 uniform bilocals + E_L,E_R / Layer 2 emergent vN factors, with
the iterated-limit convention C→∞ first, 1≪κT≪κC); (iii) **TJO RULING —
two memory registers, now D32/D33 in definitions.md**: D32 = memory
(unqualified, absolute-response, reserved word), D33 = calibrated
relational memory susceptibility (declared-cost ratio functional, DC
identity). Lattice kinks pass D32; SYK/JT passes D33 only; GW strain both
(persistent ruler — the registers coincide iff the ruler persists);
(iv) **L7 AMENDED (revokes 2026-08-25 exception): NO Fable prose writer
ever — "Fable is not good at prose"; paper skeletons bullet-level only**
(CLAUDE.md updated in-repo, bd memory + auto-memory updated).

**Nine claims registered, all L6-converged, scopes copied verbatim from
critic rulings:** the decisive computation (T.1)–(T.3), two blind lanes
(analytic + Julia TDD) → critic r1 FAIL(8) → repair → r2 FAIL(1) → r2a
PASS gave **JT-B-susc** (balanced-pulse calibrated susceptibility = DC
soft residue at O(1/C), numerics to 0.011%), **JT-bfly-decay** (the
Shenker–Stanford butterfly shift has ZERO plateau — transient relational
time delay, NOT memory), **JT-noplat-abs** (no absolute late plateau even
when the ratio plateaus; unbalanced sector retracted — no implementable
equal-(E_L,E_R) reference exists). Corner-A precision memo
(corner-a-precision.md: PW internals — only the Casimir descends; gap
list G1–G6) then the G3 wave (construct/obstruct/ward-numeric, mutually
blind → critic FAIL(3) → repair → r1a PASS) gave **JT-A-tangent,
JT-A-ward-grid, JT-A-uv-noexact, JT-A-purejt, JT-A-notconserved,
JT-A-baredescent**. The STRONG n=2 refutation is explicitly HELD (not
claimed): open route = matter-dressed one-boundary or explicitly
relational two-boundary implementer on a separated regulated core (LMZ
1904.12820 builds exactly the SL(2) relational version — natural next
theory lane). Physics frame on the bead: TFD = Hartle–Hawking vacuum of
the two-boundary problem; thermality is modular (Rindler), kinematically
forced in 0+1d (S^0 realized as horizon-split boundaries); spin chain ~
GR vacuum-sector memory, SYK/JT ~ Rindler-wedge memory.

**Microscopic ladder (tns-7wd, in progress):** ED rung DONE — honest
negative: at N_m=8–14, βJ=5–10 the EFT and ED windows do not overlap
(absolute difference non-decaying at N_m≥10 = finite-size
quasiperiodicity; calibrated ratio NOT self-averaging, sign flips across
seeds). Layer-0 evidence only; no claim rows touched. Liouville rung
queued.

**Companion paper (tns-wvp, P1 epic) — all campaign-side gates
discharged:** novelty swept three ways (pass-1 agent; 16-agent Workflow,
159 hits, 88 deduped, docs/syk-jt-novelty-sweep-deep.md; exact INSPIRE
citer intersections: Strominger-lectures ∩ MS-SYK = 13, ∩ MSY-NAdS2 = 21,
union ~30, NONE poses the triangle question — quantitative C5 support).
Verdicts: **C2 NOVEL unconditional** (the flagged kill-shot grep of
GJW/MSY-diving/Maldacena–Qi/LMTV/Kourkoulou–Maldacena full TeX found NO
DC/ω→0 identification and zero "memory" mentions — batch 11); **C4
(D32/D33) NOVEL**; **C5 NOVEL** (wording per cite-notes); C1/C3
PARTIAL-OVERLAP with exact citation obligations mapped (C1: He–Raclariu–
Zurek + Donnay et al. in first memory paragraph; C3: reposition as
operational sharpening of Grumiller-menagerie/Godet–Marteau/Harlow–Wu/
Maxfield; so(2,2) extension 2410.10768 forces plain-JT scoping; PW
type-II size vs charge-algebra conflation fence; 2409.15415 defused).
Refs batches 9–12 fetched + title-verified (~30 sources; LEDGER records
the sweep's 1408.6560 wrong-id → correct Stanford–Susskind 1406.2678).
**paper/skeleton-syk-jt.md** landed (Opus, 127 bullets, claim-id-backed,
bullet-only per amended L7) + **docs/companion-cite-notes.md** (4 Sonnet
lanes, all quotes file:line).

**Resume order for session 11:** (1) TJO writes the companion prose from
the skeleton (campaign side does NOT draft prose); (2) fetch pass for
the 18 cited ids without local TeX (skeleton L3-gate list; 3 load-bearing:
2604.19866, 2512.02825, 2201.05054); (3) TJO decision: C5 headline as
literature observation vs stronger; (4) Liouville rung (tns-7wd); (5)
optional corner-A lane: extend LMZ relational construction to n=2 (the
named open route); (6) β-sweep (future work, unbacked). Main-campaign
queue (tns-bfc, tns-25h, tns-94j, tns-kng, tns-bsk, tns-7ou…) untouched
this session — tns-25h and tns-94j now carry D32/D33 context notes.

**Ops notes (additions):** gpt-5.6-sol "model at capacity" errors are
transient — `codex exec -s workspace-write resume <session-id>` recovers
with context intact (used 4×, including across a network outage; kill
hung trees first, logs frozen >30 min = hung). The launch-cwd trap bit
again (a critic resumed from refs/ could not write theory/) — ALWAYS
launch codex from repo root. Agent-tool transcripts are JSONL; extract
final reports via last long assistant text block.

## Session 9 — the labbook (TJO directive 2026-08-30)

TJO rejected acronym-soup reporting. **`labbook/` now exists and is LAW
(L11):** a sharded LaTeX labbook (18 shards, 202 pp, compiles clean) that
restates ALL definitions D1–D31 in full, presents every CLAIMS row under a
descriptive human name with status/scope/provenance, glosses every campaign
identifier in a 170-entry dictionary shard, includes a negative-results
chapter, and a numerics chapter with 13 matplotlib figures regenerated from
`numerics/results/*.json` by `labbook/figures/make_figures.py` plus prose
(never verbatim) descriptions of the Julia codes. Style contract:
`labbook/WRITING-GUIDE.md`. **Lockstep gate: `scripts/check-labbook.sh`**
(claim-id/D-number coverage + verbatim ban) runs at session close; any
commit touching CLAIMS.md / definitions.md / numerics results must update
the owning shard in the same commit. Built by an 11-agent Opus wave;
tracked as tns-27m. Incidental source fixes: stale CONJECTURE gloss on
M-INDEX-LA-folium inside the ACE-LD-eps row corrected (owning row is the
status of record); sharper tns-kng diagnosis recorded on the bead (the
NaN is the readout-window guard refusing an empty sample set after edge
leak 5.0e-3 > 1e-3 tolerance; real defects = exit-0 write + missing
finiteness gate).

## Session 7 — PRD, the general-G swarm, the 2+1 wave, numerics

Sessions 6's process failure ("process porn") was answered structurally:
**PRD.md** now governs (anti-Zeno capped loops: prove → attack → repair,
hard stop; value gate; negative results earn NO rounds; hygiene is
plumbing; 50/30/20 budget; codex proves AND verifies per TJO model-policy
amendment). **paper/skeleton.md** is the value-gate instrument: every
lane output lands in a named slot or gets no budget. The winning pattern
is in bd memory `winning-pattern-2026-08-29-general-g-campaign`:
N parallel strategy lanes incl. one adversarial battery → ONE joint
critic (cross-consistency is its unique job) → ONE mechanical
hybrid/repair wave → orchestrator verifies and merges.

**13 promotions to PROVED in one session** (all L6-capped, all
orchestrator-verified — checkers green + reds fired, never on report):

- **S-IDX-fin-r2** — finite soft index identity, SU(2) ring, both Ward
  registers (critic recomputed the whole proof; its 1 MAJOR was a
  checker truth table, repaired + verified both ways).
- **S-IDX-fin-G** — the same operator theorem at EVERY compact G,
  root-wise, both registers — carrier upgraded same-day to ANY finite
  graph/lattice (W1 dimension audit: only D10(a) notation was 1D).
  5-lane swarm → joint critic (0 FATAL) → 9-step hybrid
  (theory/soft-index-general.md).
- **S-IDX-G-label** — sector-label integrality, disconnected G included.
- **S-IDX-MATCH-HS-SEP + S-IDX-D29-value-HS-SEP** — (MATCH-S) proved on
  the separated-preparation subclass, every spin S, zero remainder;
  slope sgn(v_h−v_s)/S with the value entering ONLY via S2-2body-S.
  **The 1D soft limit law now rests on ONE gap: (PROTO-LSZ), bd tns-7ou.**
- **2+1 wave (5 lanes + Opus recon, joint critic 0 FATAL):**
  **A-INDEX-TC-fin** (exact toric-code endpoint label + same-circle TPM
  shift + braiding character), **M-INDEX-2D-fin** (2D window
  integrality), **A-INDEX-PEPS** (categorical selection theorem,
  conditional on displayed PT1–PT3), **SHAPE-FLAT** (isotopy flatness,
  holonomy fence). M-INDEX-2D-spec at SKETCH under the W5 nonvacuity cap.
- Plus AC-EX-2M r5 hoist landed (lane closed lockstep with its row).

**Negatives, recorded once, zero rounds spent (PRD rule):** AMP is an
OBSTRUCTION (theory/amp.md — D24 fixes only Z_ρ^{-1/2}; parked on
tns-iu5); DH fully mapped (theory/dh-hunt.md: no exact-integrality
application; theory/dh-semiclassical.md RESULT: coadjoint-orbit phase
envelope F/S+G/S², frozen-ED gated at 2.62%, but NO DH law for the p_ν);
NO-CAT-SOFT (category fixes no Taylor coefficient — gapless input
needed); cat-hunt RESULT (fusion-channel datum; the Ward operator half
is genuinely Lie) — companion-paper material, deliberately unpromoted.

**2+1 instruments standing:** theory/boundary-2d.md + W4 gates
(perimeter, loop-area, 1-form, angular, register-trap-in-2D);
docs/2p1-antecedents.md (13 refs fetched+verified, batch 4; three
binding warnings: no displacement memory in 2+1, the gapped 0=0 trap,
d=3 fall-off inversion). G5 battery + G3 §17 fences also stand.

**Numerics (tns-f5r):** Wave 1 DONE and committed — λ-D ground states
across all phases + AKLT calibration, 120 TDD assertions, full suite
3787 green; D-sweep/Δ-sweep = **Fig 3 raw data** (doublet exact to
1e-13, O(1) jump bracketing D_c≈0.97, Δ_c≈1.186; NOTE: O^x separates
Néel/Haldane, O^z does NOT). **Wave 2 (kink memory) INTERRUPTED at
session end: WIP committed UNVERIFIED** — first coefficient row 1.9184
vs 2s=1.9207 (0.12%) but tests not confirmed; relaunch and red-green
first, trust nothing in that commit.

**Paper:** v2 stays PARKED (unchanged). paper/skeleton.md is the v3
target; §5's theorem slots flipped to DONE today; Fig 1
(paper/figures/fig1-triangle.tex/pdf) drafted, status-honest, compiles
clean at 8.40cm. Fig 2/3 await wave-2 data + a drawing pass.

**Refs:** fully restored on this machine (39 + 13 batch-4 dirs, all
titles TeX-verified); LEDGER updated; remote origin EXISTS
(github.com:tobiasosborne/tns-as-st-me) — the old "no remote" note is
dead.

## Session 9 (continued) — the reduction program (TJO directive)

TJO: reconciliation with the continuum must be REDUCTION, not analogy —
"the only acceptable general result reduces, in the right limits, to what
people actually accept as memory / soft theorem / asymptotic symmetries",
physics rigor (EFT matching, LSZ) sufficing. Directive persisted in bd
memory. Executed as 1 Opus + 3 codex lanes; verdicts concur
(docs/reduction-limits.md is the record; labbook shard 18 presents it;
lane files theory/lanes/reduction/). **R1** soft theorem: reduces with
caveats — strict continuum limit is free (Dyson), limits commute, the 1/S
slope is the matched cutoff-scale scattering length 1/(spin density),
ordinary σ=1 Adler class (σ=2 note in docs/continuum-antecedents.md was
WRONG, corrected in place). **R2**: the naive 1+1d specialization of the
continuum construction is exactly the REFUTED orbit row — the lattice
corrects the continuum expectation; soft/hard charge split reduces
cleanly. **R3**: displacement δx=−N_T/s reduces CLEANLY onto magnonics
(Yan–Wang–Xia, refs/arxiv-1106.4382 fetched+verified, Batch 6), constants
included; **transmission T(k) DOES NOT REDUCE** (sharp-wall zero vs
reflectionless continuum wall; regimes disjoint) → **tns-bsk P1,
referee-critical**. **R4**: edges reduce conditionally; every silent
continuum assumption mapped to a named lattice hypothesis; new gap:
Cesàro-vs-pointwise Tauberian bridge (tns-94g). Also tns-1tq (factor-2
audit in the R1 amplitude match). Honest summary for the Letter: in
corner B the lattice proves where the continuum computes and computes
where the continuum proves; the unconditionally computed quantity is the
two-magnon soft slope.

## Session 9 (continued 2) — the definitional audit (TJO: "suspicious of
## the definitions"; 3+1 lattice QED as control)

Four codex lanes (q1 Gauss / q2 memory / q3 soft / q4 HOSTILE, run blind),
verdicts concur; adjudicated in
**theory/verdicts/reduction-defs-adjudication-r1.md** (the record). Net:
**no L5 status was wrong — the exposure is in NAMING.** New findings:
(N1, FATAL to a generic-memory reading) D26+D27 = integer charge-transfer
counting statistics, NOT radiative memory (Maxwell counterexample: soft
endpoint shift with δ₀ matter TPM); missing reconstruction theorem
(charge ledger ↔ bond/potential-side field memory — exactly where
framing.md said memory lives) → new P1 bead. (N2 — **WITHDRAWN at r1a, TJO ruling**: the
finite-χ complaint was a category error; corner A is the accepted
definitional SCHEME of asymptotic symmetry, correctly instantiated on both
theories — "the only part which is obviously correct" (TJO). The Gauss
nucleus stands EXACT at finite spacing: (WI) = the constant-profile Gauss
telescope on H_phys, with a [physical argument] arrow to Strominger's
Q_hard+Q_soft. Surviving scope note only: the two theories' asymptotic
ALGEBRAS are non-isomorphic and must not be identified — a claim never
made. Fatal count drops to two: N1 memory naming, N3 S_W bootstrap.) (N3) D24(d)'s class is a bootstrap
(conditions restate the factorization) — tns-axg now framing-critical.
(N4) D24(b) IS the accepted LSZ leg definition; the D29 fixed-time datum
is pre-asymptotic, equal to it only on the separated class (proved), else
O(k) off — proto-LSZ is a DEFINITIONAL gap. (N5) D13(a) centering
amendment owed (charged-dressing masquerade) → P2 bead. Weinberg control
PASSES: the definitions correctly distinguish gauge (1/k pole, outside
the regular class) from global (Adler zero). Magnonics reduction keeps
the word "memory" defensible WITHIN magnetism only. **Letter naming
discipline is a TJO decision (P1 bead): safe names are charge ledger /
Fourier response / TPM statistics / exact-band scattering; the skeleton's
"exact 1D lattice avatar" framing must be revisited.**

## Session 9 (continued 3) — the operational wave (O1–O4) + framing

TJO directives: (i) OPERATIONAL RAZOR — representations are never
operational; only observable/implementable quantities are (injective-MPS
boundary algebra passes); (ii) one-species framing — sector separation
replaces species separation, memory needs a probe ⟹ soliton, no assembled
one-species continuum triangle exists; (iii) pure gravity INCLUDED —
JT/SYK appreciated. Four codex lanes DONE, adjudicated in
**theory/verdicts/operational-wave-adjudication-r1.md**: O1 = 48-row
operational registry (endpoint states/class/TPM/phases OBSERVABLE or
IMPLEMENTABLE — TJO's claim substantiated; V(g) GAUGE with conjugacy+[ω]
surviving; PT1–PT3 GAUGE pending circuits); O2 = six explicit experiments
+ PROVED-style impossibility: ansatz gauge X has zero quantum Fisher
information — exactly non-identifiable (scaffolding fence, no DAG row);
O3 = boundary-observables school audit (JNPW 2307.12552, Bhardwaj
2410.21454, Ogata–PG–RdA 2509.23734 tensor-network Haag duality, Corbelli
2510.23790 — refs batch 7, all title-verified): IMPORT Haag duality as
the cut-exhaustiveness theorem (tns-r7q), CITE per the §5.3 debt table
(tns-bfc P1, blocks Letter prose), novelty narrowed but scoped theorems +
soft/memory links stand; O4 = SYK/JT one-soft-species pure-gravity
triangle CANDIDATE (refs batch 8) with the named decisive computation
(T.1)–(T.3) on tns-62n (two-sided Schwarzian plateau vs DC soft residue;
decisive both ways — "butterfly shift = 2d memory" or its sharp refusal).
Also tns-0g9 (operational-registry lockstep restatements). Labbook shard
19 integration lane in flight. Ops: codex roots workspace at LAUNCH CWD
(launch from repo root only); codex network unreliable — orchestrator
pre-fetches + title-verifies, lanes get local paths.

## Resume order for session 8

1. **Numerics wave 2 relaunch** (tns-f5r): kink memory + edge contrast;
   verify the WIP commit red-green before building on it. Feeds Fig 2
   and the north-star sentence's last clause.
2. **tns-7ou (PROTO-LSZ)** — the sole remaining 1D limit-law gap.
3. **Figures 2–3** from landed data; then the paper-v3 drafting decision
   (most of §§3–5 is now PROVED-backed; L7: prose = Fable subagent
   reading docs/prose-guide.md first).
4. TJO decisions parked: companion paper(s) — categorical (cat-hunt +
   anyon-selection-hybrid + 2+1 rows), semiclassical envelope; the
   proposed 2-sentence §7 clause in theory/dh-semiclassical.md §6.
5. Queue beneath: tns-9z4 probe unfreeze, tns-uxr audit, tns-iu5
   residue sub-tasks, tns-xf4 (LR for D16), tns-pwl, corner-A hygiene
   (stale "Edges of the triangle" block in CLAIMS — one-line fix at
   next CLAIMS-touching merge).

## Ops notes (session-7 additions; prior notes stand where PRD allows)

- codex exec roots its writable workspace at the LAUNCH CWD: always launch
  from the repo root, never from a subdirectory (a lane launched from
  `refs/` could not write `theory/`; session 9 lost one lane run to this).
  Codex network access is also unreliable (DNS-blocked in some sessions):
  pre-fetch arXiv sources yourself, title-verify, then hand lanes local
  paths.
- codex exec: config defaults gpt-5.6-sol xhigh; `-s workspace-write`
  BEFORE the `resume` subcommand; on a transport timeout mid-write,
  `codex exec -s workspace-write resume --last "<finish instruction>"`
  recovers the session with context intact — instruct incremental
  section-by-section writes.
- codex lanes sometimes close/claim beads inside their sandbox — check
  bd status after every lane and reopen if premature.
- CLAIMS merges: escape pipes inside backticks (restriction bars
  `\|_{...}`) with a backtick-aware walker; awk column counts don't
  honor `\|` — use escape-aware splitting to validate rows.
- The sonnet safety classifier can time out and block Bash briefly;
  wait and retry, do read-only work meanwhile.
- A peer session (local-llm-b4) ran GPU benchmarks today; coordination
  protocol worked (hold-at-lane-boundary on request). Nothing owed.
