<!-- ROLE: live state. UPDATE POLICY: every session end + every phase boundary. -->

# HANDOFF — live state

Updated: 2026-08-30, session 9 (the labbook session). Read order gate:
CLAUDE.md → **PRD.md (the process constitution — where it conflicts with
older habits recorded here or anywhere, PRD WINS)** →
HANDOFF_MPS_SOFT_THEOREM.md → this file → paper/skeleton.md.

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
