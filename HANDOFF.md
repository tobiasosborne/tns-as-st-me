<!-- ROLE: live state. UPDATE POLICY: every session end + every phase boundary. -->

# HANDOFF — live state

Updated: 2026-08-26, after the corpus-r2 proposer repair. Read order gate:
CLAUDE.md → HANDOFF_MPS_SOFT_THEOREM.md (the
brief) → this file → theory/TRIANGLE.md (the frozen framework, D2).

## Where we are — one paragraph

Critic `theory/verdicts/corpus-r2.md` adjudicated the summit corpus and the r2
proposer repair is now applied.  Fifteen narrow items are PROVED: S2-2body,
ML4-A, the exact Ward projection, ML5-A/B, M-flux, K1--K3, B3, Mq-AD3
conditional on Mq-E, M-quant conditional on D18, the Fano formula/zero
conditional on Mq-E for the displayed graph, closed SPT multiplier
cancellation, and the exact AKLT-family contraction.  The fixed-ring ML4
formulas are explicitly off-shell; the on-shell infinite-volume result remains
open.  SPT N1--N6 are repaired using a Hermitian centered endpoint charge,
continuous external path data, distinct Schmidt and padded-window modules,
correct Whitehead phrasing, H-dress lockstep, and a specific open AKLT parent
Hamiltonian.  Parent SPT rows remain SKETCH awaiting focused critic r3.
Corner-C `𝖲` has definition D25.  The brief's original Conjecture M remains
REFUTED; universality of the Fano zero/coefficient remains CONJECTURE.

## State of the artifacts

- theory/TRIANGLE.md and claims/CLAIMS.md — synchronized to corpus-r2; parent
  SPT rows await critic r3.
- All 8 checkers in theory/checks/ PASS under `python3 -O` (rerun before
  trusting anything: `for f in theory/checks/*.py; do python3 -O $f; done`).
- Red guards fail as intended: M-quant sign, ML4 uniformity, SPT edge sign,
  and the new uncentered U(1) phase gauge.
- Converged loops: oracle (r2 PASS), Corner A (r3 PASS), ML2 (r2 PASS).
  Corpus-r2 promotions are applied; the repaired parent SPT package still
  needs focused critic r3 (tracked by tns-gk4).
- paper/ — v1 draft + figures (all generated from equations + committed JSONs
  via paper/figures/make_figures.py). Known: needs v2 (tns-2ze) absorbing the
  freeze, the generality directive, and the ML5 no-contact form; TJO must
  sign off on printing the Conjecture-M refutation; known window-arg bug in
  make_profile_data.jl call (worked around in make_figures.py).
- numerics/ — TriangleMPS (TensorKit env ready but current shards use plain
  sparse/KrylovKit); 1510+828 tests green; scans in numerics/results/.

## Next steps (bd is the tracker — `bd ready`)

P0: tns-0xi (L6 critic on M-quant + ML4/ML5 shards), tns-zw2 (M-quant general
form), tns-7ut (ML3 form-factor regularity), tns-bhm (parent: A⇒C core).
P1: tns-acr (ML1+ML6), tns-8e9 (Bc spin-1 falsifier numerics), tns-2ze (paper
v2), tns-gk4 (critic on drafts+TRIANGLE), tns-axg (three-body channel),
tns-d51 (full-chain H-AD lift).
P2: tns-cpq (AKLT/SPT deciding computation), tns-peh (ML2 minor residue).
Suggested resume order: tns-0xi first (the two new proof shards must survive
review before the paper leans on them), then tns-2ze (v2 rewrite), then Bc
falsifier + AKLT (they decide the headline), then the remaining ML ladder.

## Standing directives (TJO)

- North star: theorem + Bethe + MPS numerics on a serious model illustrating
  the memory effect. SPT headline only if it survives.
- Giulini framing in background (docs/framing.md).
- Lamport structured proofs (L6b); rk-light method; proposer/critic to fixed
  point; no Fable subagents EXCEPT the paper writeup (L7, docs/prose-guide.md
  mandatory pre-read — the guide is extracted from 5 verified exemplars in
  refs/prose-exemplars/).
- Generality directive: theorems stated in (G, injective MPS, finite-range)
  form; FM/XXZ as instantiation; Bethe strictly oracle (integrability-free
  hypotheses).
- TIB VPN available via TJO for paywalled refs (Dyson 1956, Nielsen–Chadha
  1976 still non-local).

## Ops notes (hard-won)

- codex exec: flags BEFORE the `resume` subcommand; prompt via file redirect
  (`- < file`), NOT heredoc-to-stdin (breaks in background harness); zero CPU
  + empty output + no new ~/.codex/sessions rollout = hung at startup (kill
  and relaunch — happened 2× during network flaps); NEVER `pkill -f 'codex
  exec'` from a compound command that itself contains that string.
- Background agents killed by outages resume via SendMessage; codex holds a
  thread lock — kill stale processes before `resume --last`.
- Checker discipline: no bare asserts (python -O strips them); every checker
  must be red-capable (mutation-tested); don't pipe checker output through
  `tail` in a `&&` chain (masks exit code).
- Julia env: numerics/ has TensorKit 0.17.1 + KrylovKit; full test suite ~8
  min.
