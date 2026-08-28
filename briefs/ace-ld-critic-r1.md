# Critic brief — ACE-LD r1

Read `briefs/critic-protocol.md` first; everything there binds.

**TARGET:** `theory/ace-ld.md` and `theory/checks/ace_ld_check.py`.
**VERDICT FILE (your only writable file):** `theory/verdicts/ace-ld-r1.md`.

**Prior context you must read:** `briefs/ace-ld-prover.md` (what was asked);
`theory/ansatz-scattering.md` ⟨1⟩7 in full (the (AD3-ex) display the shard
must discharge, verbatim — check the shard proves THAT statement and not a
neighbouring one); `theory/verdicts/ansatz-scattering-r1.md` objection 4 (the
original gap); `claims/CLAIMS.md` rows AD3-ex, AC-EX, M-INDEX-fin,
M-INDEX-spec; `definitions.md` D10(c), D13(a), D14, D17, D18 (esp. the AD3/AD4
limit ORDER).

**Attack these surfaces first — this is where a proof of this shape breaks:**

1. **The finite-spectrum route.**  The brief suggested proving `E_W({q})` is a
   polynomial in `Q̂_W` (Lagrange/Riesz) using M-INDEX-fin's coset
   integrality.  Interrogate it hard: is the interpolation constant genuinely
   uniform in `t` at fixed `W`?  Is the spectrum of `Q̂_W` really
   `t`-independent, and is that PROVED in the shard or assumed?  Does the
   argument silently need `W↑ℤ` uniformity, which the frozen limit order
   forbids?
2. **The boundary-straddling term.**  This is the entire content of the
   lemma.  Does the shard actually bound the window charge of the *dressing*
   of the outgoing leg, or does it quietly identify the dressed leg's window
   charge with the bare channel charge at finite `t`?  Construct an explicit
   configuration where they differ and see whether the shard's estimate
   survives it.
3. **Limit order.**  `t→+∞` BEFORE `W↑ℤ` (D18 AD4).  Any interchange is FATAL.
4. **Generality overreach.**  The brief asked for an abstract `N`-channel
   lemma.  Check the abstract statement is not secretly two-channel, that
   "definite channel charges" is a real hypothesis rather than a definition
   in disguise, and that the instance section verifies every abstract
   hypothesis for the AC-EX construction rather than asserting it.
5. **Circularity.**  Does the shard use ACE.3, or anything downstream of
   (AD3-ex), to prove (AD3-ex)?  Does it use M-INDEX-spec, whose own reduction
   clause reads D18(AD3) in a particular way?
6. **The checker.**  Does it certify the abstract lemma or merely exhibit a
   model where the conclusion happens to hold?  Do its red modes fire for the
   right reason?  Mutation-test it yourself on a copy.

**Deliverable beyond the standard format:** state explicitly whether
(AD3-ex) may now be discharged from the AC-EX row — and if so, exactly what
ACE.3's remaining conditionality is (the charge assignment and Lane T1's
outcome measure do NOT go away), and what the C⇒B edge may now be called.

---

## ADDENDUM (orchestrator, after the prover landed) — what actually came back

The lane did NOT simply prove (AD3-ex).  It returned a mostly NEGATIVE
result, and the negative half is now the load-bearing claim.  **A wrong
refutation is as damaging as a wrong proof** — attack the negative claims at
least as hard as the positive ones.  Specifically:

**Positive claims to verify:**
- **ACE-LD-abs** (⟨1⟩1--⟨1⟩2): the abstract `N`-channel lemma, claimed
  unconditional, with bound `‖E({q_ch})Ψ_t − P_chΨ_t‖ ≤ Σ_{ch'} d_{ch'}^{-1}
  ε_{ch'}(t)`.  The lane claims the suggested Lagrange/Riesz machinery was
  unnecessary — a single spectral-gap bound suffices — and that the
  `t`-uniformity worry is vacuous because `Q̂_W` is Schrödinger-picture fixed.
  **Check that reasoning specifically**: is the constant really `≤ n`, is the
  gap really `≥1` from M-INDEX-fin, and does the bound degrade as the number
  of channels grows?
- **ACE-LD-nec** (⟨1⟩3): distinct charges are *necessary*.  Verify the
  counterexample is genuine and not an artifact of a degenerate weight choice.

**Negative/obstruction claims to attack hardest:**
- The lane asserts (AD3-ex) as intended is **not derivable from D28 alone**,
  because on D28's ballistic packet class the kink escapes every fixed window,
  so the correct charges are `W`-dependent kinematic values
  `q_{σ_ch}(W,c₀) ∈ {2s(b−c₀), 2s(a−1−c₀)}` rather than the ledger constants
  `−1,+1`.  **Is that right?**  If so it is a real result about the ledger's
  reading; if it is an artifact of the lane's own window convention or of a
  sign error in `c₀`, it is a serious false alarm.  Recompute the charges.
- It asserts (AD3-ex) holds **iff `σ_L ≠ σ_T`** (channels' kinks exit on
  opposite sides) and is FALSE for every charge assignment when both exit the
  same side with both weights nonvanishing.  Construct both configurations
  explicitly and check.
- **ACE-LD-obst** (⟨1⟩6.⟨2⟩2) is the most consequential claim of the round:
  in the regime where (AD3-ex) is provable, the transit channel's TPM outcome
  is `ν = ±2s|W|`, so **D27(LR3) first-moment tightness fails along every
  exhaustion**, making (AD3-ex) and Lane T1's ordered outcome measure jointly
  unsatisfiable unless the transit weight vanishes — i.e. ACE.3 would be
  *vacuously* guarded on this class, and the `{0,2}` ledger support would be a
  no-transit idealization rather than a fixed-window theorem.  If this
  survives, it reaches **M-INDEX-spec's hypotheses and the whole C⇒B edge**,
  and it must not be accepted on one lane's say-so.  Recompute `ν` yourself.
  Check whether the growth is an artifact of the regularised window charge's
  `c₀` offset (which M-INDEX-fin shows cancels in the TPM increment) rather
  than a genuine physical divergence — **that cancellation is exactly the kind
  of thing this obstruction could have missed.**
- Two NEW named hypotheses were introduced, **(E-TAIL)** (zero tail variance,
  `ω_γ((S^z_x−s_γ)²)=0`; claimed true in D16, false for AKLT-like vacua) and
  **(V-ch)** (sign-definite outgoing velocities).  Audit whether they are
  genuine hypotheses or smuggled conclusions, and whether (E-TAIL) silently
  restricts the theorem to product (χ=1) vacua — the corpus has been burned by
  exactly that restriction before (TJO 2026-08-27).
- The lane self-declares one soft spot: ⟨1⟩6.⟨3⟩1 (LD-IN) is argued as the
  time-reflection of ⟨1⟩4 but not written out.  Verify or fault it.

**Cross-lane obligation:** a separate lane is proving D27(LR) for D16
(`theory/lr-d16.md`, bd `tns-xf4`).  If ACE-LD-obst is correct, it bears
directly on whether LR3 can hold for a ballistic transit channel.  Say
explicitly in your verdict whether the two results are consistent, and if not,
which one you believe and why.
