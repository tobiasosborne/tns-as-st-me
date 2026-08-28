# Critic brief — (LR) for D16, r1

Read `briefs/critic-protocol.md` first; everything there binds.

**TARGET:** `theory/lr-d16.md` and `theory/checks/lr_d16_check.py`.
**VERDICT FILE (your only writable file):** `theory/verdicts/lr-d16-r1.md`.

**Prior context you must read:** `briefs/lr-d16-prover.md` (what was asked);
`definitions.md` **D27 verbatim** (LR1, LR2, LR3 and the convenience clause),
D26(INT), D16, D17, D13(a); `claims/CLAIMS.md` rows M-INDEX-spec (its
adjudicated scoping sentence is the register), M-INDEX-fin, K1--K4 (**K4 is
CONJECTURE — flag any reliance on it**), and the REFUTED M-INDEX-LA-strong;
`theory/memory-index.md` ⟨1⟩5 and ⟨1⟩7.⟨2⟩2; `theory/corner-b-draft.md` §1.2;
`theory/checks/memory_index_probe.py` (dressed-kink discipline: sharp kinks
FAKE a 5% violation, `dwmax=3` is spuriously perfect).

**Attack these surfaces first:**

1. **LR2 is first-moment only.**  D27 clause 2 is a first-moment
   nondemolition condition and explicitly does NOT assume operator asymptotic
   commutativity.  Check the proof does not smuggle in the operator statement
   — that would be strictly stronger and would make the result circular with
   what M-INDEX-spec is trying to avoid.  This is the single most likely
   defect.
2. **The frozen limit order.**  Infinite-volume dynamics FIRST, fixed-window
   time limits SECOND, spatial exhaustion LAST.  Hunt for any interchange,
   including implicit ones inside a Cesàro estimate that is uniform in `W`.
3. **LR3 uniformity.**  Tightness is `sup_m`, uniform over the exhaustion.
   Check the bound really is uniform in `m` and not merely fixed-`m` decay
   with an `m`-dependent constant.  This is where a plausible-looking proof
   usually fails.
4. **LR1's chosen sequence.**  The prover may choose `T_n`.  Check the SAME
   sequence works for every fixed `W` simultaneously, as D27 requires ("one
   sequence `T_n→∞` such that, for every fixed `W`…"), rather than a
   `W`-dependent subsequence — a diagonal argument needs the exhaustion to be
   countable and the extraction order to respect item 2.
5. **Integrability leakage.**  D16 is easy-axis XXZ.  Bethe is an ORACLE
   ONLY.  Flag any use of closed Bethe factorisation or of structure beyond
   two-body contact.
6. **The stretch section.**  If a general "gap + Lieb--Robinson ⟹ (LR)"
   statement is claimed, attack it as a separate artifact and be ruthless
   about whether the D16 proof's constants really only used those inputs.  If
   it is marked CONJECTURE, check that no earlier step borrows its strength.
7. **The checker.**  ED certificates must use dressed kinks; a sharp-kink
   initial state is a known artifact generator.  Verify the red modes fire
   for the stated reason, on copies.

**Deliverable beyond the standard format:** state explicitly, clause by
clause, whether LR1 / LR2 / LR3 are proved unconditionally for D16 — because
if all three are, M-INDEX-spec gains its **first unconditional dynamical
instance**, which is a headline. Do not certify that lightly, and say plainly
if only a subset survives.

---

## ADDENDUM (orchestrator, after the prover landed)

The lane returned a **clause-split result**, not a clean proof, and it is the
strongest positive artifact of the round.  Attack it accordingly — the danger
here is not overclaiming in the statement, it is a load-bearing step that does
not survive recomputation.

**Claimed:**
- **LR1 — PROVED UNCONDITIONALLY** (⟨1⟩3) by compactness + diagonal
  extraction, using no gap, no Lieb--Robinson velocity, and no property of `Ψ`
  beyond normalisation; generalised as **LR1-GEN** (⟨1⟩6.⟨2⟩2).  **MP-1
  therefore proposes an EDIT TO D27** — that D27 carries as a hypothesis
  something that is a theorem.  That is a change to an L4 single source and
  needs your explicit MERGE/HOLD.
  *Attack:* D27 demands ONE sequence `T_n` serving **every fixed `W`**
  simultaneously.  Does the diagonal argument actually deliver that, or a
  `W`-dependent subsequence?  Is `spec Q̂_{W,c₀}` finite for the reason
  claimed?  Is `α_t` strong continuity enough, or is uniformity in `t` needed
  somewhere?
- **LR2 — verbatim OPEN**; a weakened **(LR2′)** is proved, with residue named
  **(DPH)** and marked CONJECTURE.  The prover explicitly did NOT patch it with
  operator asymptotic commutativity.
  *Attack the mitigation, which is the risky claim:* ⟨1⟩4.⟨2⟩7 asserts LR2 is
  consumed at **exactly one leaf** of `theory/memory-index.md` (⟨1⟩7.⟨2⟩1),
  that the error enters before the spatial limit and is removed by it, and
  therefore that **(IDX.2) and M-INDEX-spec's conclusions hold verbatim with
  LR2 weakened to (LR2′)**.  That is a claim about ANOTHER shard and about a
  PROVED row.  Verify it by reading `memory-index.md` yourself and grepping
  every use of LR2 — if there is a second consumer, the mitigation fails and
  M-INDEX-spec is affected.
- **LR3 — PROVED from one named input (NR)** (⟨1⟩5), via an exact
  second-moment identity, an edge split, a **monotonicity lemma**
  `𝒩_{W'} ≤ 𝒩_W` claimed to kill `sup_m` "for free" (the smallest window
  dominates), and an **energy--domain-wall bound**
  `H_XXZ ⪰ (J/2)(Δ−1)D ⟹ ⟨D(t)⟩ ≤ 2E₀/(J(Δ−1))`, uniform in time.
  *Attack:* is **(NR)** a genuine single hypothesis or a repackaging of LR3
  itself?  Does the monotonicity lemma really hold in the claimed direction —
  a `sup_m` collapsing to the smallest window is surprising and is exactly
  where a sign or inclusion error would hide.  Recompute (EDW)'s operator
  inequality independently.
- **Class statement — CONJECTURE, and a NEGATIVE result the lane volunteered:**
  ⟨1⟩6.⟨2⟩5 claims **"gap + Lieb--Robinson ⟹ (LR)" is FALSE as a class
  statement**, exhibiting a gapped finite-range model with a mobile charged
  core that satisfies both and fails LR3.  Verify that counterexample; if it
  stands it saves the campaign real effort, and if it is wrong it must not
  enter the corpus.
- **Cross-lane:** flatness of D16's kink band was derived from **K1+K2 only**
  (both PROVED), never citing the CONJECTURE row K4 — check that claim
  strictly, since the instruction to avoid K4 was explicit.  ⟨1⟩5.⟨2⟩4 further
  claims the outcome bound is majorised by a fixed smallest-window quantity
  independent of `m`, so `|ν| ≍ 2s|W_m|` cannot be manufactured by window
  geometry or the `c₀` offset.  A separate lane (`tns-r2c`) claims exactly such
  growth for a ballistic transit channel and its critic CONFIRMED that claim.
  Say explicitly whether the two are consistent — the prover asserts they are
  and that D16 is outside the obstruction's class because its band is flat.

**Checker:** exit 0 on 18 rows; four red modes each exit 1; **two source-level
mutations on copies**, one exiting 1 and one (a legitimate cut move) exiting 0
to show the rows are not over-fitted.  That is the first lane this round to do
the non-over-fitting check unprompted.  Verify it anyway, and apply every
standing obligation — especially reachability: which gate kills each mutant,
and is any of the 18 rows reached by nothing?

**Two caveats the lane states itself in §H** — `N=12` certifies identities and
inequalities, not asymptotics; and the honest headline is *one clause proved
outright, one proved weakened but sufficient downstream, one reduced to a
single named dynamical hypothesis*, so **M-INDEX-spec still has no fully
unconditional dynamical instance**.  Check that this honesty is maintained
everywhere in the shard and not just in §H.
