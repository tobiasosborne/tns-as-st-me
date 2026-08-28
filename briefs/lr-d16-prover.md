# Work order — prove (LR) for D16 (bd tns-xf4)

You are the PROPOSER.  A hostile critic from a different model family will
attack every step by independent recomputation.  Be a relentless prover:
produce the proof, not a survey.

## WHY THIS IS THE BIGGEST REMAINING MEMORY-CORNER PRIZE

`M-INDEX-spec` is PROVED but **conditional**, and it currently has **zero
unconditional dynamical instances**, because D27(LR) is assumed on every
model.  One honest instance converts the memory corner from
"conditional theorem" to "theorem with a model".  That is the whole task.

It is far cheaper than the old target it replaces (full-chain D18/H-AD,
bd `tns-d51`, now demoted): (LR) needs only **window relaxation plus
first-moment tightness** — NOT completeness, NOT channel exhaustion, NOT a
channel inventory.  The channel-free formulation of M-INDEX-spec is exactly
what makes this reachable.  Do not accidentally prove more than you need.

## READ FIRST, in order

1. CLAUDE.md (laws; **L6b Lamport format is mandatory**; L10 honest verdicts)
2. `definitions.md` — **D27 (LR1--LR3) IN FULL and verbatim** (this is your
   PROVE target, clause by clause), D26(INT), D13(a), D16 (the model), D17
   (the kink packet), D10(c), D14
3. `claims/CLAIMS.md` — **M-INDEX-fin** and **M-INDEX-spec** rows in full
   (including their verbatim adjudicated scoping sentences: match that
   register exactly), plus K1--K4 (the D16 kink facts already PROVED, and K4
   which is CONJECTURE — you may not lean on K4), M-IDX-density, and the
   REFUTED row M-INDEX-LA-strong (you may not rely on it, and you must not
   re-derive a sector-wide charge operator: its unconditional existence is
   REFUTED)
4. `theory/memory-index.md` IN FULL — especially ⟨1⟩5 (finite-window coset
   integrality), ⟨1⟩7.⟨2⟩2 (the ledger identity that makes LR3 give `δx`),
   and the r1/r2/r3 scoping discipline
5. `theory/corner-b-draft.md` §1.2 (the D16 kink construction, K1--K3) and §5
6. `theory/checks/memory_index_probe.py` — the ED probe that already supports
   (LR) empirically (relaxation visible, no boundary-stranded charge).  RUN IT.
   Its dressed-kink discipline is mandatory reading: **sharp kinks FAKE a 5%
   violation** and `dwmax=3` is spuriously perfect.  Do not build a numerical
   argument that repeats either mistake.

## THE TARGET

Prove LR1, LR2, LR3 of D27 for the D16 model (easy-axis XXZ kink sector), for
a D17 kink packet, via the one-body kink--magnon reduction.

Clause by clause, what you actually owe:
- **LR1** — existence of the Cesàro limits `ω^±_{W,n}` on `𝔄_W` and of the
  double-Cesàro TPM laws `p_{W,n}(ν)`, along ONE sequence `T_n→∞`, at every
  fixed `W`.  Note the generous structure: you get to CHOOSE the sequence,
  and Cesàro averaging plus a compactness/diagonal argument is usually enough
  — do not prove pointwise-in-`t` convergence you do not need.
- **LR2** — the first-moment nondemolition condition: the double-Cesàro
  average of `⟨Ψ,[𝒟_{W,t_-}(Q̂_{W,c_0}(t_+)) − Q̂_{W,c_0}(t_+)]Ψ⟩ → 0`.
  Read the definition carefully: this is a FIRST-MOMENT statement.  Operator
  asymptotic commutativity is explicitly NOT assumed and you must not smuggle
  it in — that would be a strictly stronger claim and the critic will say so.
- **LR3** — first-moment tightness of `{p_{W_m}}` along the exhaustion:
  `lim_{M→∞} sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν)=0`.  This is where a uniform
  bound on the escaped charge is needed; the optional convenience clause
  (weak convergence to a probability `p`) buys ONLY uniqueness of the value
  `δx` — prove it separately or leave it, and say which.

Limit order is frozen and load-bearing: **infinite-volume dynamics first,
fixed-window time limits second, spatial exhaustion last**.  Any step that
interchanges these is a FATAL.

## AMBITION AND GENERALITY (TJO directive 2026-08-28)

Structure the shard so the result is as general as your proof honestly
supports, with the D16 instance as the certified special case:

- ⟨1⟩1--⟨1⟩2: setup and the exact statement you will prove, in D27's own
  words, with every hypothesis displayed.
- ⟨1⟩3--⟨1⟩5: the three clauses for D16.  This is the unconditional
  deliverable and it is the one that must land.
- ⟨1⟩6 (**the stretch goal — attempt it, fence it honestly**): the CLASS
  statement.  Isolate which structural inputs your D16 proof actually used —
  candidates: a spectral gap above the kink band, a Lieb--Robinson bound,
  finite range, D26(INT), the one-body reduction — and state the general
  lemma "gap + Lieb--Robinson (+ …) ⟹ (LR)" for whatever hypothesis set you
  genuinely used.  If you can prove it, that is a substantially bigger result
  than the instance and it should be the headline.  If you cannot, state the
  general conjecture precisely, mark it CONJECTURE, name the missing step,
  and DO NOT let its shadow strengthen ⟨1⟩3--⟨1⟩5.

## YOUR LANE (writable — nothing else)

- `theory/lr-d16.md` (create)
- `theory/checks/lr_d16_check.py` (create)

Do NOT edit `definitions.md`, `notation.md`, `claims/CLAIMS.md`, `HANDOFF.md`,
or any existing shard or checker.  Text destined for a shared file goes in a
**MERGE PROPOSALS** section of your own file as exact replacement text; the
orchestrator merges after the critic converges.

## OBLIGATIONS

- Lamport structure throughout: ⟨1⟩1, ⟨1⟩2, …, sub-proofs ⟨2⟩1…, explicit
  ASSUME/PROVE at every nontrivial step, terminal QED steps.  **Every leaf
  cites a D-number, a claim id, or a named computation.**
- A **HONEST STATUS** section: what is proved unconditionally, what is
  conditional and on what, what is only numerical evidence.  Understate.
  If a clause resists, DOWNGRADE and say so — a proof of LR1+LR3 with LR2
  honestly open is a real result and a good outcome; a hand-waved LR2 is a
  FATAL next round.
- A red-capable checker `theory/checks/lr_d16_check.py`: ED certificates for
  the clauses you prove (Cesàro convergence rates at fixed `W`, the LR2
  first-moment defect shrinking, the LR3 tail sum uniform in `m`), green exit
  0 under `python3 -O`, and at least two `--red` mutations that MUST exit 1.
  No bare `assert`.  Mutation-test on COPIES in a temp dir.  Use the
  dressed-kink discipline of `memory_index_probe.py`; a sharp kink is not an
  acceptable initial state.
- Bethe is an ORACLE ONLY, never a hypothesis (bd memory
  `law-integrability-free-hypotheses`).  D16 is easy-axis XXZ; you may use
  its explicit one-body kink--magnon structure, but no closed Bethe
  factorisation and nothing beyond two-body contact structure.
- You may NOT rely on any REFUTED row.  You may NOT use the second display of
  ML4-Ward (9) at `n≥2` (ERRATUM; correct form `P J^-_0 = 2D(D^†D)^{-1}J^z_0`).
- Quote references only from local TeX under `refs/` (L3), by section/equation.

Work fully autonomously.  Do not ask questions.  Do not stop at a plan.
