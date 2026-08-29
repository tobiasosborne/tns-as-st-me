<!-- ROLE: process constitution. Read after CLAUDE.md, before doing anything.
     Where this conflicts with older habits recorded in HANDOFF.md, worklogs,
     or bd notes, THIS FILE WINS. Amended only by TJO. -->

# PRD — what this campaign is and how it runs

## Product

One result and one artifact:

- **The result (north star):** the 1D lattice infrared triangle — theorem +
  Bethe verification + MPS numerics on a serious model illustrating the
  memory effect.
- **The artifact (L9):** a 4-page PRL in the register of arXiv:1305.2176.

A session that moves neither is a failed session, however many critic rounds
it ran. Process output (verdicts, trajectories, audit hygiene) is cost, never
product.

## The two goals

1. **Rapid progress.** This is *rk-light*: an exploration campaign, not a
   formalisation campaign. If a task needs the full machinery — unbounded
   review loops, mutation-proving, meta-audits — it belongs in `../rk`, not
   here.
2. **Never admit a false result.** No statement ever carries a status
   stronger than its evidence. This is the only non-negotiable.

Every process rule in this repo must serve one of these two goals. A rule
serving neither is deleted, not obeyed.

## How goal 2 is met WITHOUT killing goal 1

The insight that makes both goals compatible: **soundness lives in the status
labels, not in polish.** A claim sitting at SKETCH or CONJECTURE forever
harms no one. The only fatal sin is a wrong label — PROVED on a false or
unproved statement, or a refutation silently ignored. Therefore:

- **Status discipline (L5).** Every claim in `claims/CLAIMS.md` with status ∈
  {PROVED, SKETCH, CONJECTURE, REFUTED}. Promotion to PROVED only through the
  capped loop below. When in doubt, the label goes DOWN. A sharp refutation
  with the surviving weaker statement is a *result* (L10).
- **The gate to PROVED** is a full Lamport structured proof (L6b) that
  survived the capped hostile loop below with no open FATAL/MAJOR on the
  promoted statement. Such a proof needs no falsifier. Anything less stays
  at SKETCH.
- **Falsifiers are early warning, binding in the negative.** A
  pre-registered red-capable probe (ED / checker / oracle) before a proof
  lands is cheap, shapes conventions, and catches what critics miss —
  prefer one whenever the claim admits a computation. Passing one proves
  nothing and promotes nothing. But a falsifier that DISAGREES blocks
  promotion unconditionally, even against a passed proof: it means the
  statement and the probe disagree about what is being claimed, and that
  must be resolved before any label moves up.
- **Ground truth (L3).** Quotes from local TeX only; red-green TDD (L1) for
  all numerics.
- **Capped hostile review (anti-Zeno, imported from rk):** see below.

What goal 2 does NOT require: review-to-fixed-point, adversarial audits of
checkers, audits of audits, reachability tables, or re-review of repairs.
A hostile critic always finds something; "iterate until zero findings" never
terminates and was the session-6 failure mode.

## The capped L6 loop (supersedes "iterate to fixed point")

Per artifact: **prove → attack → repair. Hard stop.**

- One prover pass, one hostile critic round, one repair wave.
- After the repair, the **orchestrator verifies fixes mechanically** against
  the critic's file:line claims (checkers, recomputation, falsifier) and
  adjudicates. Repairs are NOT re-reviewed by a fresh hostile pass.
- Residual objections become the claim's honest scope conditions or bd
  issues for a future lane — they do not extend the loop.
- **Sole exception:** an open FATAL touching a headline claim buys exactly
  one more round. "Headline" = a claim the Letter states or the north-star
  theorem depends on.
- If the loop ends with unresolved MAJORs: the claim stays at SKETCH with
  the objections recorded next to it. That is a legitimate terminal state —
  goal 2 is satisfied by the label, not by more rounds.
- **Rigor follows the claim's role, not the reviewer's appetite.**
  Headline claims get the full loop. Supporting lemmas, definitions,
  conventions, and checkers get one pass and a plain fix. Checkers are
  red-capable once, then frozen (postmortem R3).

## Negative results earn no rounds (TJO 2026-08-29)

Obstructions, blockers, no-go gates, underdetermination certificates:
**these are not progress.** They are useful ONLY if they suggest a new
strategy for moving forward. The rule:

- A negative result that names a viable new attack → the attack is
  value-gated like any lane; the negative note itself is recorded (bead or
  shard header) and gets NO critic round, NO repair, NO promotion machinery.
- A negative result with no forward strategy → STOP the line entirely and
  trigger a **total re-evaluation** of the approach with TJO. Do not spend
  another token certifying, reviewing, or polishing the dead end. A
  beautifully verified obstruction is still an obstruction.
- The verification machinery of this repo (L6 loops, checkers, verdicts)
  exists to protect POSITIVE claims the paper will state. It is never
  applied to negative side-results.

## Budget and lane discipline (postmortem R1, R5)

- **Value gate before any lane launches:** "if this converges, does the
  north-star sentence or the paper change?" No → file a bead, do not launch.
- **Session budget split, declared at session start:** ~50% the single
  highest-value open theorem, ~30% numerics/figures/paper, ≤20% repairs and
  hygiene. Inherited repair lanes never get priority over the north star by
  default.
- Critics may not expand scope into meta (auditing prior verdicts, process
  archaeology) unless a headline claim depends on it (R6).

## Model policy (TJO 2026-08-29, supersedes L6/L7 role split)

- **codex exec (GPT-5.6 Sol xhigh) is the workhorse: exploration, proving,
  AND adversarial review.** The same model proving and verifying is
  accepted for this campaign; cross-family verification waits for rk
  elevation of results that earn it. Quota is plentiful — use it
  extensively and in parallel lanes.
- **Opus subagents liberally** for everything else: numerics, checkers,
  mechanical work, search.
- **Fable** only for final paper prose (L7 exception unchanged).

## One record (postmortem R4)

Each event is narrated once, in its home:

- verdict → its file in `theory/verdicts/`
- tracker → bd note ≤ 5 lines
- commit message ≤ 10 lines
- user report: short, results first, process only if it changed a decision

## Definition of a good session

At session end, the honest answer to both must be yes:

1. Did the north star or the paper move — a status changed, a figure exists,
   a section is drafted — or was an explicit, recorded decision made that it
   should not?
2. Is every status label in CLAIMS.md still no stronger than its evidence?

Everything else — trajectories, rounds survived, objections closed — is not
progress and is not reported as such.
