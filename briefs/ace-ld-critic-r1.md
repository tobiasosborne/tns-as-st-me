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
