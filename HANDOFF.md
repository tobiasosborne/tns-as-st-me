<!-- ROLE: live state. UPDATE POLICY: every session end + every phase boundary. -->

# HANDOFF — live state

Updated: 2026-08-28, end of session 3 (the overnight memory-index campaign,
TJO greenlight: "prove the most general, most ambitious result conceivable",
3 Fable + 3 codex xhigh + Opus lanes, ~6h autonomous). Read order gate:
CLAUDE.md → HANDOFF_MPS_SOFT_THEOREM.md → this file → theory/TRIANGLE.md.

## Where we are — one paragraph

**The paper is PARKED by TJO verdict** (2026-08-27: "really really bad, I
would never author something like this" — its L6 r5 PASS certified
claim-licensing, not quality; do not treat it as endorsed). The session
instead attacked the campaign's weakest corner: memory was a conditional
theorem (M-quant-G) whose entire content sat in the unproved-anywhere,
false-in-general scattering package H-AD-G, validated only on one
ferromagnetic family with χ=1 product vacua. The memory-index campaign
RESTRUCTURED it: **quantization needs no scattering theory; scattering only
computes the value.** New PROVED rows (all L6: three r1 verdicts → r2 → r3,
MAJORs 6→3→1→repaired, 0 FATAL): **M-INDEX-fin** (finite-window coset
integrality, unconditional), **M-INDEX-spec** (conditional: D26(INT)+D27(LR,
tightness-only) ⟹ every subsequential TPM escaped-charge law is supported
on ℤ, δx = −(2s)⁻¹Σν·p_ν; NO channel inventory, bound states allowed;
reduces exactly to M-quant-G under H-AD-G), **M-IDX-density** (LSM-type
by-product: 2ρ∈ℤ for U(1)-covariant injective-MPS antisymmetric vacuum
pairs — publishable alone), **AC-EX** (ACE.1–2: existence half of
D18(AD1)+(AD2) from exact excitation-ansatz band hypotheses D28, via
momentum-filtered Cook estimates; the ansatz supplies the kinematics,
existence is then a theorem — completeness never claimed). **REFUTED:
M-INDEX-LA-strong** (no unconditional sector-wide charge operator; two
independent mechanisms — D17-fluctuation counterexample AND the A1(b)
nonscalar-V_θ obstruction; folium-restricted form survives as CONJECTURE
M-INDEX-LA-folium). New CONJECTURE **AD3-ex** (missing lemma ACE-LD) fences
ACE.3. Pre-registered ED falsifier `memory_index_probe.py` PASSED before
the proofs landed (off-lattice mass exactly 0 at N=50; near-threshold
zero-velocity magnon pairs land ON integers — the soft-endpoint degeneracy
is absorbed by the channel-free formulation, empirically).

## State of the artifacts

- claims/CLAIMS.md — 7 new rows (4 PROVED w/ verbatim adjudicated scoping,
  1 REFUTED, 2 CONJECTURE); definitions.md D26/D27/D28; notation.md +15
  rows. All lockstep-audited (r2 obligation, r3 spot-check: no silent
  strengthening).
- theory/memory-index.md (canonical T1, 976 lines — L2 split is
  post-promotion hygiene, tns pending), theory/memory-index-b.md
  (superseded lane-B record), theory/ansatz-scattering.md (T2). Verdicts:
  memory-index-r1/-b-r1/-r2/-r3, ansatz-scattering-r1.
- theory/checks/ — 14 checkers all green under `python3 -O`;
  memory_index_check.py (10 rows, red 10/10), ansatz_scattering_check.py
  (4 red modes), memory_index_probe.py (ED; dressed-kink discipline:
  sharp kinks FAKE a 5% violation; dwmax=3 spuriously perfect).
- Notable process results: the loop caught TWO adjudicator errors via
  red-first checker work (r2 R9(iii) overruled — kernel-tail scaling lives
  on the Cook majorant, not C_θ); both T1 provers independently refuted the
  operator charge lemma by different mechanisms; the r2 critic re-derived
  the density theorem while objecting only to its notation (circularity
  fence now on 3 surfaces).
- Paper: UNCHANGED and PARKED. Nothing from this campaign is in the paper.
- No git remote exists — local commits are the durable record.

## Next steps (bd is the tracker — `bd ready`)

1. **TJO review of the memory-index package** — TRIANGLE.md §3.6 is the
   5-minute read; theory/memory-index.md §0 the 30-minute one. Decisions
   needed: (a) is M-IDX-density a standalone letter? (b) does the TPM
   register satisfy the "true generality" ask, or push M-INDEX-LA-folium
   next (the implementer-route charge operator)?
2. ACE-LD / AD3-ex (new bd row): the one lemma separating AC-EX from an
   unconditional-given-D28 two-channel law.
3. M-INDEX-LA-folium: O(1) twisted-transfer variance + local
   implementability markers recorded; a focused prover round is plausible.
4. L2 splits (memory-index §5 → own shard; checker toolbox) + NOTE-10
   probe RED_RHO_SHIFT coprime fix — hygiene, one Sonnet pass.
5. Then the pre-campaign queue: tns-f5r showcase (now with the dressed-kink
   discipline), tns-cpq, tns-ebh (Bc |q|>1), tns-d51/tns-acr (these two are
   now "verify D28/H-AD-G instances", cheaper than before).
6. Paper v3: only after TJO defines the register; the memory-index package
   changes the Letter's spine (quantization-without-channels is the story).

## Standing directives (TJO)

- Paper v2 is NOT endorsed; park it. L6 passes license claims, not prose.
- 2026-08-27 greenlight (up to 3 Fable / 3 codex xhigh, workflows) was for
  the 4-6h campaign window, now SPENT — revert to L7 defaults (no Fable
  subagents except paper prose; Opus/Sonnet free for mundane work).
- Sol/codex works best on exhaustively specified goals ("rottweiler") —
  keep the brief style of briefs/memory-campaign-target.md.
- SPT rigidity dichotomy stays in the paper (2026-08-26, emphatic);
  Conjecture-M refutation prints as a central result.

## Ops notes (session-3 additions; session-1/2 notes still valid)

- Parallel repair lanes MUST get a reconciliation pass before adjudication
  (r3 objection 2: lane A's doc edits went stale when lane B landed 3h
  later). Sequence doc-lane after checker-lane, or budget an extra pass.
- Pre-registered falsifier probes BEFORE the proof lands are cheap and
  decisive (memory_index_probe.py shaped the ν-convention and killed a
  fake 5% violation before any critic saw it).
- codex sandbox cannot commit (.git read-only) — orchestrator owns all
  commits; verify codex startup via log growth (both provers ~35 min,
  ~170KB logs).
- Opus session limits can kill a lane mid-flight (one 429 at 03:50 CEST);
  relaunch is clean if the lane made no edits — check `git status -s`
  before relaunching.
