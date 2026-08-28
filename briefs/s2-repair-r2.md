# Work order — S2 repair round 2 (codex, prover family continuity)

You are the PROPOSER repairing Theorem AC-EX-2M after its round-2 critic
verdict.  A hostile critic from a different model family will attack every
edit by independent recomputation.  Be a relentless prover: produce the
repaired proof, not a plan.

BUDGET NOTE: this is codex use #1 of a cap of 7 for the whole campaign.
Work the target to the end in this one run.

READ FIRST, in order:
1. CLAUDE.md (laws; **L6b Lamport format is mandatory**; L10 honest verdicts)
2. briefs/soft-index-target.md (the campaign target — Lane S2 is yours)
3. theory/verdicts/ansatz-scattering-2m-r2.md  IN FULL — this is your work
   order.  Also theory/verdicts/ansatz-scattering-2m-r1.md (priors) and
   theory/ansatz-scattering-2m-r1-response.md (your lane's r1 response
   format — reuse it exactly).
4. theory/verdicts/soft-index-adjudication-r1.md §3--§4 (BINDING).
5. definitions.md (D6, D24, D28, D31 proposal), notation.md,
   claims/CLAIMS.md (AC-EX's adjudicated scoping sentence is the register
   you must match).
6. theory/ansatz-scattering.md (the ACE machinery you inherit),
   theory/ml2-completeness.md (the (A2M.2) anchor, PROVED).
7. refs/arxiv-1412.2970/Scattering_spin-AHP1.tex — cite by section/equation
   number, NEVER from memory (L3).

## YOUR LANE (writable — nothing else)

- `theory/ansatz-scattering-2m.md`
- `theory/ansatz-scattering-2m-r2-response.md`  (create)
- `theory/checks/ansatz_scattering_2m_check.py` (create or edit)

Do NOT touch definitions.md, notation.md, claims/CLAIMS.md, HANDOFF.md, or
any other shard.  Everything destined for a shared file goes in your
MERGE PROPOSALS section as exact replacement text.  The orchestrator merges.

## THE TWO MAJORS (both must be resolved, not deflected)

**R2-O1 — (ACE2M-LSZ) is a vacuum-vector hypothesis used as an operator
statement.**  The critic verified your ⟨1⟩8.⟨2⟩1 D6 anchor is CORRECT *as a
vacuum identity* (R_ε=0, Γ_M isometric with dk/2π) but ⟨1⟩9.⟨2⟩2 needs the
operator statement, and on D6 the corpus's PROVED (R8) contradicts it:
`Q_{k_s}|k_h⟩ − |B^in⟩ = −2ik_s|P_12⟩ + O(k_s²)` — nonzero at exactly the
soft law's linear order.
FIX DEMAND (the critic named the upgrade and verified you already own both
its hypotheses): port the final clause of the Haag--Ruelle theorem of
refs/arxiv-1412.2970 — **creator-choice independence** — and use it to prove
(ACE2M-LSZ) as an operator statement.  That converts a hypothesis into a
theorem and closes r1-O2 completely.  Your r1 response explicitly REFUSED to
port creator independence; that refusal is correct for ⟨1⟩7.⟨2⟩4 and wrong
for ⟨1⟩9.⟨2⟩2 — scope the refusal, do not repeat it.
If the port genuinely fails, you must DOWNGRADE (L10 / rk-light law 5): state
the surviving weaker statement the critic gave you, and say plainly that the
operator form remains hypothesis.  A silent restatement is a FATAL next round.

**R2-O2 — the sole unconditional step of (A2M.3) proves a diagonal-order
statement while (A2M.3) asserts an iterated-order one** (vacuous-truth gap),
plus a clause-3 regression.
FIX DEMANDS: (i) scope (A2M.3) to the diagonal-order statement ⟨1⟩9.⟨2⟩1
actually proves, or prove the iterated order; (ii) restore interface clause
3's packet qualifier "on the selected hard packet"; (iii) bound the `L²(I)`
denominator away from zero, with the hypothesis displayed.

## THE NINE MINORS

Address EVERY one of R2-O3 … R2-O11 with a row in the response table.
Two are checker-spec defects you must fix in code, not prose:
- restore the word **"connected"** to the A2M-C1a spec (the literal reading
  currently fails by 1.0);
- put a **tolerance** on the ratio gate (the spec's own 1e-12 fails green
  from d=7).

## OBLIGATIONS

- Every objection gets a row in `ansatz-scattering-2m-r2-response.md`:
  objection id → FIXED / RETRACTED / DOWNGRADED / RESIDUE, with the exact
  edit location (file + step id).  No objection may be silently ignored.
- LOCKSTEP: if a claim weakens, its statement, its HONEST STATUS paragraph,
  and its MERGE PROPOSALS row all move together in the same edit.
- CHECKER: your checker must be red-capable.  Mutation-test on a COPY in a
  temp dir, never in place.  No bare `assert` (they vanish under `python3 -O`).
  Run green (exit 0) and every red mode (exit 1) and paste the output.
- You may NOT rely on any REFUTED row, and you may NOT use the second
  display of ML4-Ward (9) at n≥2 — it carries an ERRATUM; the correct form
  is `P J^-_0 = 2D A^{-1} J^z_0` with `A=D^†D` on the FULL sector (register-dependent — see `theory/verdicts/ml4-ward-n2-audit.md` §1.2; in the hw-restricted register that string collapses back to the refuted display and the correct form is `(1/m_λ)Q_0Π_{hw}J^z_0`) (exact at every n).
- Bethe is an ORACLE ONLY; no hypothesis may use integrability beyond
  two-body contact structure.

## STRATEGY DIRECTIVE

Downgrade over ambition.  Where the critic offers "downgrade or prove more",
take the downgrade unless the proof is actually in hand — and where it hands
you a named port that closes a MAJOR (R2-O1), do the port.  A sharp,
honestly-scoped theorem beats an overclaimed one; the trajectory is
6 → 2 MAJOR and must reach 0.

Work fully autonomously.  Do not ask questions.  Do not stop at a survey.
