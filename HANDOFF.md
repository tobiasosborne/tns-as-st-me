<!-- ROLE: live state. UPDATE POLICY: every session end + every phase boundary. -->

# HANDOFF — live state

Updated: 2026-08-26, end of session 2 (paused on TJO instruction after the
L6 fixed point + M-quant-G promotion landed). Read order gate: CLAUDE.md →
HANDOFF_MPS_SOFT_THEOREM.md (the brief) → this file → theory/TRIANGLE.md.

## Where we are — one paragraph

Session 2 stress-tested the 2026-08-26 freeze and rebuilt it stronger. Two
adversarial critic rounds (triangle-r1, mquant-ml45-r1) VOIDED the freeze —
35 objections incl. 12 FATAL: statuses promoted without verdicts (L5
violation), B3(ii) false by sign+factor 2, D18 mismatched to the proof, and
the SPT draft dead at definition level. Three repair/adjudication rounds
later (trajectory 35 → 7 → 4 → PASS, theory/verdicts/corpus-r2/r3/r4.md) the
corpus reached an L6 FIXED POINT: **27 PROVED rows** — the full triangle
(WI/A1/A2/G0, S2-2body, M-flux, B3, conditional M-quant/Mq-AD3/M-tk, ML4-A/
Ward, ML5-A/B, K1-K3, ML2, OR1-2) **plus the rebuilt SPT package**
(SPT-B'/E'/T'/D'/M' + two splits; spt-scoping-draft superseded by
theory/spt-rebuild.md). The SPT story is now the RIGIDITY DICHOTOMY: bulk
soft coefficients deform continuously (measured 0.125→0.2402 on a symmetric
path), edge residue exactly ±1/2, quantized in the [ω]-shifted lattice.
**Conjecture Bc SURVIVED its falsifiers** — two independent implementations
measured slope = 1/s and δx/N_T = −1/s across s ∈ {1/2, 1, 3/2, 2}
(pre-registered 8% criteria; the slope law is now EXACT analytics, 3.3e-15),
so "the two 2's = |q|/s" is live, with the |q_hard| factor untested.
**Theorem M-quant-G** (memory law in the (G, injective MPS, finite-range)
register, conditional on H-AD-G) is PROVED per its converged loop
(mquant-g-r2 PASS) — with the discovered Weyl-element criterion: a bare
abelian symmetry cannot realize a kink vacuum pair. Conjecture M's
refutation will be printed as a central result (TJO sign-off recorded).

## State of the artifacts

- claims/CLAIMS.md — the DAG, current through corpus-r4 + mquant-g-r2; the
  fixed-point ledger is in corpus-r4.md's final section.
- theory/ — all shards carry converged verdicts (corner-a r3, oracle r2,
  ml2 r2, corpus r2/r3/r4, mquant-g r2). spt-rebuild.md is the SPT ground
  truth; memory-quantization-general.md is M-quant-G.
- theory/checks/ — 9 checkers, all PASS under `python3 -O`; red modes
  documented and verified (incl. U(1) uncentered-gauge and k=Θ(1/N) probes).
  Rerun: `for f in theory/checks/*.py; do python3 -O $f; done`
- numerics/ — suite **3667 green** (~8 min). Two independent Bc packages:
  spin1_* → results/spin1-bc-falsifier.json; spins_* (general S) →
  results/spin1-bc-crosscheck.json. S-matrix derivations agree to 1.1e-15.
  Analytic spin-S slope law in numerics/docs/spin1-twomagnon-notes.md (first
  derivation there recorded WRONG; the corrected one is the non-symmetric
  free-extension contact algebra).
- paper/ — v2 COMPLETE and L6-CERTIFIED (paper-v2-r5.md PASS, five
  adversarial rounds 20→6→2→1→0; certification paragraph in the verdict).
  4-page main text + appendices A-E, 3 figures from committed JSONs,
  paper/v2-claim-audit.md maps every sentence to its DAG row. Also since
  session-2 close: S2-2body-S PROVED (exact spin-S slope law, spin-s-r1.md)
  — Bc's slope half is now a theorem at unit charge; corpus at 28 PROVED
  rows. AWAITING: TJO's own read of paper/main.pdf.
- Decisions recorded: SPT results ARE in the paper (rigidity dichotomy);
  Conjecture-M refutation printed as central result; numerics standardized
  on TensorKit+MPSKit (laptop-scale, low χ); ED stays as checker layer.

## Next steps (bd is the tracker — `bd ready`)

1. TJO reads paper/main.pdf; any edits re-enter via a critic round.
2. tns-f5r — MPSKit showcase: spin-1 λ–D chain (all corners + SPT in one
   phase diagram); tns-cpq dynamical SPT-M'-dyn computation feeds it.
3. tns-ebh — Bc falsifier round 2: charge-2 hard leg (|q| factor).
4. tns-7ut (ML3), tns-acr (ML1+ML6), tns-axg (𝒮_W), tns-d51 (full-chain
   D18), tns-00l (Mq-E all-volume) — the conjecture frontier, not
   paper-blocking.
5. Parked/companion: tns-89h (Kähler/moment-map + Duistermaat–Heckman),
   tns-0w0 ((2+1)d lattice celestial program), tns-qyb (experimental
   proposal), tns-1u8 (ML2 post-sweep minor residue).

## Standing directives (TJO) — unchanged plus session-2 additions

- North star: theorem + Bethe + MPS numerics on a serious model. SPT
  rigidity dichotomy IS in the paper (TJO 2026-08-26, emphatic).
- Print the Conjecture-M refutation as a central result (TJO sign-off
  2026-08-26).
- Generality directive SATISFIED for Corner A + memory law (M-quant-G).
- Numerics: MPSKit/TensorKit for showcase, ED for checkers; laptop budget
  (χ ≲ 64; gapped phases, AKLT anchor χ=2).
- L7 unchanged: no Fable subagents EXCEPT paper prose (prose-guide gate).
- The rk-light method is now a reusable skill: ~/.claude/skills/rk-light.

## Ops notes (session-2 additions; session-1 notes still valid)

- codex exec: defaults (gpt-5.6-sol, xhigh) are correct; launch with
  `-s workspace-write -C <repo> - < brief.md`, run_in_background, then
  VERIFY startup (ps + output file growth) — silent hangs happen.
- Parallel agents: strict file-lane briefs + merge-proposal pattern worked
  flawlessly (6 concurrent, 0 conflicts). Checker mutation-testing on
  COPIES only.
- L6 verdict format that made loops converge: every objection = location +
  independent computation + fix demand + surviving weaker statement; later
  rounds adjudicate deltas only (git diff scoping). Promotions applied by
  copying the critic's exact scoping sentence — and CHECK the verdict's
  promotions actually landed in the DAG (one was missed and caught late).
- Julia numerics survive network outages (local compute); codex dies but
  resumes (`codex exec resume --last` after killing stale processes).
- No git/dolt remote exists — local commits ARE the durable record; the
  CLAUDE.md push mandate is unsatisfiable in this clone.
