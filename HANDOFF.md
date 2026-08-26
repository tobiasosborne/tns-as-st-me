<!-- ROLE: live state. UPDATE POLICY: every session end + every phase boundary. -->

# HANDOFF — live state

Updated: 2026-08-26, end of session 1 (paused on TJO instruction after the
freeze landed). Read order gate: CLAUDE.md → HANDOFF_MPS_SOFT_THEOREM.md (the
brief) → this file → theory/TRIANGLE.md (the frozen framework, D2).

## Where we are — one paragraph

The campaign went scaffold → refs → novelty sweep → three adversarial L6 loops
(oracle, Corner A, ML2), ALL CONVERGED (PASS verdicts in theory/verdicts/),
→ the FREEZE (theory/TRIANGLE.md, 2026-08-26). Proved and frozen: the general
MPS theorems (WI, A1 charge algebra/torsor with [ω] central extension, A2
sector-jump with double-coset classification, G0 dichotomy); Theorem S2-2body
(soft phase δ_phys = 2·sgn(v_h−v_s)k_s + (|v_h|/ω_h)k_s², the 2 derived from
the current/contact equation, integrability-free hypotheses, Bethe as oracle
only); ML2 completeness; ML4 at n=1 (orthogonal-current O(k_s²) suppression);
ML5 refuted for unrestricted sources (explicit counterexample O_η) and PROVED
on the no-contact Ward-covariant class 𝒮_W — necessary and sufficient;
Theorem M-quant for the projected kink dynamics (H-AD proved via
Kato–Rosenblum on the Fano/Jacobi reduction; δx = −⟨N_T⟩/s, spec(ΔX) ⊂
{−1/s, 0}); the analytic t(k) verified against independent numerics at 1–6%
over Δ ∈ [1.5,12]; the memory soft zero T = 16(Δ−1)²k². The brief's original
Conjecture M (δx = DC limit of soft factor) is REFUTED — the memory quantum is
a charge, not a phase. Headline candidate: Conjecture Bc ("the two 2's" =
|q|/s) with a spin-1 falsifier. SPT dichotomy (bulk [ω]-cancellation, edge
detection via representation type only) is drafted, critic pending. Paper v1
(Fable-authored, prose-guide-primed) exists with three real figures and
compiles at PRL shape.

## State of the artifacts

- theory/TRIANGLE.md — FROZEN framework; changes require reopening the
  relevant L6 loop (rule in its §7 and the CLAIMS.md footer).
- claims/CLAIMS.md — the DAG, quantifier-exact, all rows current.
- All 7 checkers in theory/checks/ PASS under `python3 -O` (rerun before
  trusting anything: `for f in theory/checks/*.py; do python3 -O $f; done`).
- Converged loops: oracle (r2 PASS), Corner A (r3 PASS), ML2 (r2 PASS).
  NOT yet critic-reviewed: ml4-ward-reduction.md, ml5-universality.md,
  memory-quantization.md, TRIANGLE.md itself, corner-b-draft.md,
  spt-rebuild.md (rebuilt 2026-08-26, SKETCH pending critic r2; it supersedes
  spt-scoping-draft.md — tracked: tns-0xi, tns-gk4).
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
