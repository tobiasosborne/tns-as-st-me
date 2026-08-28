# Work order — ACE-LD prover (lemma closing the C⇒B edge)

You are the PROPOSER for the named lemma **ACE-LD**.  A hostile Opus critic
will attack every step by independent recomputation.  You are a relentless
prover: produce the proof, not a survey.

## WRITING DISCIPLINE (non-negotiable — two previous runs died here)

Derive and **Write ONE Lamport section per response**.  Do not draft the
whole proof in extended thinking before writing: that output is lost and the
run dies at the 64k cap.  Write ⟨1⟩1 to the file, then think, then write
⟨1⟩2, and so on.  The file on disk is the deliverable at every moment.

## READ FIRST, in order

1. CLAUDE.md (laws; **L6b Lamport format is mandatory**; L10 honest verdicts)
2. definitions.md — D10(c), D13(a), D14, D17, D18 (esp. clauses AD3, AD4 and
   their limit ORDER), D26(INT), D27(LR), D28
3. notation.md; claims/CLAIMS.md — read the **AD3-ex** row (CONJECTURE), the
   **AC-EX** row and its adjudicated scoping sentence, and **M-INDEX-fin**
   and **M-INDEX-spec** (both PROVED) in full
4. theory/ansatz-scattering.md IN FULL — especially ⟨1⟩3.⟨2⟩5 and ⟨1⟩4.⟨2⟩1
   (the O(|t|^{-N}) escape estimates you inherit), ⟨1⟩6.⟨2⟩3--⟨2⟩5 (the
   channel projections P_L, P_T), and ⟨1⟩7 IN FULL (the ASSUME block
   displaying (AD3-ex) verbatim, and the cross-term half that is already
   PROVED at ⟨1⟩7.⟨2⟩2)
5. theory/memory-index.md ⟨1⟩1 and ⟨1⟩5 (M-INDEX-fin: the finite-window
   coset integrality result — this is your main new tool)
6. theory/verdicts/ansatz-scattering-r1.md objection 4, and
   theory/verdicts/memory-index-r2.md (the HOLD rationale) + memory-index-r3.md
   objection 1 — these state the exact gap and the exact charge assignment

## THE TARGET

Prove **(AD3-ex)** as displayed verbatim in `theory/ansatz-scattering.md`
⟨1⟩7's ASSUME block:

> Let `Ψ=W_+(F_L,F_T)`, `Ψ_t:=e^{-itH}Ψ`.  For every fixed window `W`
> containing the kink core region, with `E_W(·)` the spectral measure of the
> regularised window charge `Q̂_W` and `P_ch`, `ch∈{L,T}`, the channel
> projections of ⟨1⟩6.⟨2⟩5:
> `lim_{t→+∞}||E_W({q_ch})Ψ_t − P_{ch}Ψ_t||=0`, the limit taken BEFORE `W↑ℤ`.

The gap, stated by the r1 critic and conceded in the shard: the free leg and
its dressing leave any fixed `W` at rate `O(|t|^{-N})` by ⟨1⟩3.⟨2⟩5 and
⟨1⟩4.⟨2⟩1, but converting that into convergence of the **window-charge
spectral projection** needs control of the boundary-straddling charge on `∂W`,
which no step of that shard supplies.  You supply it.

## SUGGESTED ROUTE (the finite-spectrum route — verify it, do not trust it)

At a FIXED finite window `W`, `Q̂_{W,c}=2s(𝔛_W−c)` is a bounded self-adjoint
operator with **finite** spectrum, and by the PROVED **M-INDEX-fin** that
spectrum lies in a single coset `κ_{W,c}+ℤ`.  A finite-spectrum self-adjoint
operator has spectral projections that are POLYNOMIALS in the operator
(Lagrange interpolation on the eigenvalue list; equivalently a Riesz contour
integral with a fixed separation `≥1` between coset points supplied by
M-INDEX-fin).  If so, `E_W({q})` is norm-continuous in `Q̂_W` with a constant
depending only on `W` and the coset separation — and the hard problem
collapses to the FIRST-MOMENT statement
`||(Q̂_W − q_{ch})P_{ch}Ψ_t|| → 0`,
which is exactly what the `O(|t|^{-N})` escape estimates plus the ledger of
⟨1⟩7.⟨2⟩1 can deliver.
Two things you must NOT wave at: (i) the Lagrange/Riesz constant must be
uniform in `t` at fixed `W` (it is, if it depends only on the spectrum of
`Q̂_W`, which is `t`-independent — prove that, do not assume it); (ii) the
window charge of the *dressing* of the outgoing leg is not the bare channel
charge at finite `t` — that difference is precisely the boundary-straddling
term, and it is what your `O(|t|^{-N})` estimates must kill.
If this route fails, say exactly where and prove whatever weaker statement
survives.  A sharp refutation with the surviving weaker statement is a
PRODUCT here, not a failure.

## AMBITION AND GENERALITY (TJO directive 2026-08-28)

Do not settle for the two-channel kink--magnon instance.  Structure the shard
so the lemma is proved at the **general** level it deserves:

- ⟨1⟩1--⟨1⟩3: the abstract lemma.  ASSUME a finite window `W`, a bounded
  window-charge observable with finite spectrum in one coset of `ℤ`
  (M-INDEX-fin's conclusion, cited — not re-proved), a finite family of
  mutually orthogonal channel projections `{P_ch}` summing to the identity on
  the constructed out-space, definite channel charges `{q_ch}`, and
  first-moment channel escape.  PROVE window-charge spectral diagonality.
  State it for **N channels**, not two, and for a general on-site spin.
- ⟨1⟩4--⟨1⟩5: the instance.  Verify each hypothesis for the AC-EX
  construction with `ch∈{L,T}`, `q_in=q_L=−1`, `q_T=+1`, discharging
  (AD3-ex) exactly as ⟨1⟩7 displays it.
- ⟨1⟩6: what this buys the DAG.  (AD3-ex) is the sole hypothesis fencing
  ACE.3; discharging it makes the two-channel outcome law unconditional
  GIVEN D28, which is the C⇒B edge.  State precisely what remains
  conditional (D28-C is unverified on any model — do not hide that).

## YOUR LANE (writable — nothing else)

- `theory/ace-ld.md` (create)
- `theory/checks/ace_ld_check.py` (create)

Do NOT edit definitions.md, notation.md, claims/CLAIMS.md, HANDOFF.md, or any
existing shard.  Text destined for a shared file goes in a **MERGE PROPOSALS**
section of your own file as exact replacement text; the orchestrator merges
after the critic converges.

## OBLIGATIONS

- Lamport structure throughout: ⟨1⟩1, ⟨1⟩2, …, sub-proofs ⟨2⟩1…, explicit
  ASSUME/PROVE at every nontrivial step, terminal QED steps.  **Every leaf
  cites a D-number, a claim id, or a named computation.**  Critics attack
  "⟨1⟩4.⟨2⟩2"; give them addresses.
- A **HONEST STATUS** section: what is proved, what is hypothesised, what is
  merely evidence.  Understate.
- A red-capable checker: a numerical certificate of the abstract lemma on a
  small explicit model (finite window, explicit finite-spectrum charge, two
  or three channels with escaping packets), plus at least two `--red`
  mutations that MUST make it exit 1 (e.g. break the coset separation; give a
  channel an indefinite charge).  No bare `assert` — they vanish under
  `python3 -O`.  Mutation-test on COPIES in a temp dir.
- You may NOT rely on any REFUTED row.  You may NOT use the second display of
  ML4-Ward (9) at n≥2 (ERRATUM; correct form `P J^-_0 = 2D(D^†D)^{-1}J^z_0`).
- Bethe is an ORACLE ONLY, never a hypothesis.
- Quote references only from local TeX under `refs/` (L3), by section/equation.

Work fully autonomously.  Do not ask questions.  ONE Lamport section per
response, written to the file as you go.
