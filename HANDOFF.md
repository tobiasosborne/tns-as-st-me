<!-- ROLE: live state. UPDATE POLICY: every session end + every phase boundary. -->

# HANDOFF — live state

Updated: 2026-08-25 (session 1, scaffold).

## Where we are
- P0 DONE: scaffold; 36 refs fetched + title-verified (refs/LEDGER.md); D1
  novelty sweep banked (docs/novelty-sweep.md) — verdict: novel, pitch as
  "exactification of the continuum triangle"; Hamada–Sugishita 1709.05018 is
  the direct antecedent; Lan–Xiao 2107.05401 the corner-B precedent.
- P2/oracle DONE (pending critic): theory/oracle-bethe.md — exact FM
  two-magnon S-matrix, soft phase δ = 2k_s + cot(k_h/2)k_s² (linear coeff
  HARD-INDEPENDENT; hard data enters at O(k_s²) as v_h/ω_h); green ED checker.
  Conjecture S must be reshaped accordingly when frozen.
- In flight: Opus Corner A drafter (definitions D1–D5 + D9+, theory/corner-a.md,
  claims WI/A1/A2/G0); Opus critic on the oracle (→ theory/verdicts/).
- Julia env ready (TensorKit 0.17.1).
- Ops note: network outages can hang codex/agents; codex thread lock may need
  killing stale processes before `codex exec resume --last` (flags BEFORE the
  resume subcommand).

## Phase plan
P0 scaffold+refs+novelty → P1 TRIANGLE.md (Corner A propositions, S/M precise)
→ P2 proofs (A⇒C core, Lamport-style, codex prover / Opus critic to fixed
point) → P3 Julia numerics (uMPS + excitation ansatz; S(k) vs Bethe; kink δx;
AKLT/SPT test) → P4 the PRL (apsrev4-2, 3 figures) → P5 final adversarial pass.

## Standing directives (TJO, 2026-08-25)
- North star: theorem + Bethe + MPS numerics on a serious model illustrating
  the memory effect. SPT headline only if it survives.
- Giulini framing in background (docs/framing.md): symplectic actions, Poisson
  charge algebras, explicit function spaces, potential (= bond/virtual data)
  fundamental.
- Lamport structured proofs for all rigorous arguments (L6b).
- TIB VPN available via TJO if paywalled sources are needed (ask first).
- Keep working autonomously until the PRL is top quality.
