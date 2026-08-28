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

## Next steps (bd is the tracker — `bd ready`; queue re-ranked 2026-08-28
## after the TJO strategy exchange — full record in bd memory
## `session-3-strategic-record-2026-08-28-tjo`)

Corner scoreboard after the campaign: **A strong** (PROVED general; now
enriched by the density lemma and the tns-pwl scope theorem — charges live
on the center of the unbroken subgroup, the Weyl group makes the walls,
finite groups are a hard fence). **B strong-conditional** (M-INDEX:
channel-free quantization; hypotheses evidenced near-minimal by critic
counterexamples; missing only dynamical (LR) instances). **C now the
weakest corner** (S-general CONJECTURE; beyond two-body only Bethe
evidence). **Edges weakest overall.** The playbook to reapply: invert the
burden — symmetry/superselection gives quantization, dynamics only supplies
existence/values; protocol-level checkable hypotheses; pre-registered
falsifier; cross-family L6 loops.

1. **TJO decisions** — (a) is M-IDX-density a standalone letter? (b) TPM
   register vs pushing M-INDEX-LA-folium (tns-x3o)? (c) greenlight for the
   Corner-C campaign?
2. **tns-5oc (P1)** — Corner-C campaign: general soft theorem = ML4 Ward
   identity + AC-EX wave-operator existence, conditional only on D28 band
   data, no integrability; falsifier = the Bethe oracle O1--O10. Would
   upgrade edge A⇒C. Highest-value theory move on the board.
3. **tns-xf4 (P1)** — prove (LR) for D16: first unconditional dynamical
   instance of M-INDEX-spec; only window-relaxation needed, not
   completeness. The biggest remaining memory-corner prize.
4. **tns-r2c (P1)** — ACE-LD: the one lemma closing edge C⇒B (soft data
   enter the outcome law only through p_2 = <N_T^ex>).
5. **tns-q5z (P2)** — SPT TPM port: remove H-AD-edge from SPT-M' by
   transplanting the two-measurement register to an edge window.
6. **tns-x3o (P2)** folium charge operator; **tns-pwl (P2)** scope theorem
   mini-loop (semisimple zero-density lemma + joint-torus Z^r corollary);
   **tns-7ov (P3)** L2 splits/hygiene; **tns-gi9 (P4)** full counting
   statistics.
7. **B⇒A edge**: memory quantum as moment-map value — the Kähler route
   (tns-89h companion, TJO's program); tns-day notes updated.
8. Pre-campaign queue continues underneath: tns-f5r showcase (dressed-kink
   discipline mandatory), tns-cpq, tns-ebh (Bc |q|>1), tns-d51/tns-acr.
9. Paper v3 only after the register decision; the campaign's spine
   sentence: *symmetry quantizes; the ansatz supplies the kinematics;
   dynamics only picks the values.* A self-contained 13-page account for
   TJO exists at docs/report-memory-index/memory-index-report.pdf.

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
