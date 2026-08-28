# Critic protocol (shared) — read this, then your target-specific brief

You are the ADVERSARIAL CRITIC.  **Attack; do not summarize.**  Your job is
to find what is wrong, and where it is right, to say exactly how far the
truth extends.  A critic pass that reads as a book report has failed.

## Read order (always)

1. `CLAUDE.md` — the laws (L4 single-source definitions, L6b Lamport,
   L10 honest verdicts)
2. `definitions.md`, `notation.md` — the single sources
3. `claims/CLAIMS.md` — the DAG.  Note which rows are PROVED, which are
   CONJECTURE, and which are **REFUTED** (nothing may rely on a REFUTED row)
4. the target artifact, in full
5. any prior verdicts on that target (`theory/verdicts/`) — these are your
   priors

## Obligations (all five; a verdict missing any of them is void)

1. **RECOMPUTE, never referee.**  Independently re-derive the key steps.
   Construct counterexamples.  Where a number is claimed, produce that number
   yourself by an independent route.  "The argument reads plausibly" is not a
   finding in either direction.
2. **Quantifier audit.**  For every claim: are the quantifiers in the
   statement the ones the proof delivers?  The most common defect in this
   corpus is a statement asserted for all `n` (or all `ρ`, or iterated
   limits) whose proof covers one value (or the diagonal order only).
3. **Lockstep audit.**  Statement, proof shard, HONEST STATUS paragraph,
   MERGE PROPOSALS, and any DAG row must all say the same thing at the same
   strength.  Divergence between layers is the failure mode this method most
   often catches — check it explicitly and report it even when minor.
4. **Checkers, and mutations on COPIES.**  Run every checker the target
   claims, green and red, under `python3 -O`.  Then mutation-test it
   yourself: copy it to a temp dir, break one hypothesis, confirm nonzero
   exit.  A checker that cannot fail is not evidence.  Look specifically for
   gates that are no-ops (this corpus has shipped one: two "different"
   expressions that were textually identical, certifying 0.0 by
   construction).
5. **Reliance audit.**  No step may rely on a REFUTED row; on the second
   display of ML4-Ward (9) at `n≥2` (ERRATUM — correct form
   `P J^-_0 = 2D A^{-1} J^z_0` with `A=D^†D` on the FULL sector (register-dependent — see `theory/verdicts/ml4-ward-n2-audit.md` §1.2; in the hw-restricted register that string collapses back to the refuted display and the correct form is `(1/m_λ)Q_0Π_{hw}J^z_0`)); on Bethe integrability as a hypothesis
   (oracle only, beyond two-body contact structure); or on the class `𝒮_W`
   being nonempty at `ρ≠1/2` while bd `tns-iu5` is open.

## Output format (mandatory)

A verdict file.  Numbered objections, each classified
**FATAL / MAJOR / MINOR / NOTE**, each carrying all four of:

- **(a)** exact location — file plus step address (`⟨1⟩4.⟨2⟩2`), not "section 4"
- **(b)** your independent computation or counterexample
- **(c)** a one-line **FIX DEMAND**
- **(d)** the **SURVIVING WEAKER STATEMENT** — what remains true after your
  objection lands

(c) and (d) are what turn a FAIL into a work order instead of a demolition.
An objection without them will be rejected and the round redone.

Also required in every verdict:
- a section listing what you independently **VERIFIED CORRECT** (fence it, so
  the repair lane does not churn it);
- a **register comparison** against the adjudicated scoping sentence of the
  nearest PROVED row — is this artifact claiming in the same honest register?

**Final line:** `PASS` (no FATAL and no MAJOR) or `FAIL(list of ids)`.

## Lane

Your verdict file ONLY.  Do not repair the target, do not edit
`definitions.md`, `claims/CLAIMS.md`, `notation.md`, or the shard you are
attacking.  Do not git commit.

Work fully autonomously.  Do not ask questions.  Do not soften findings to be
agreeable — a severity-falling FAIL is the method working.

---

## Standing checker obligations (added 2026-08-29 — a CAMPAIGN-LEVEL PATTERN)

This corpus has now shipped **four** gates that did not test what they
advertised, found in three separate rounds:

1. `soft_index_probe.py` P2(b): compared `proto` with `proto_dressed`, which
   were the identical expression — recorded exactly `0.0` by construction.
2. `ansatz_scattering_2m_check.py` profile-agreement gate (r3 R3-O2): a
   rescaled duplicate of the agreement gate; a genuine two-sided support-fold
   passes it.
3. `d24d3_normalization_check.py` D24N-C2 "soft-leg norm": algebraically
   `sites·two_s/sites − two_s ≡ 0` — returns 0 for every input.
4. `d24d3_normalization_check.py` `check_exponent_is_one`: `lstsq(x, x)`,
   design matrix identical to target, so `p=1` "to 1e-9" is a tautology.

Therefore, for EVERY checker you attack or write:

- **Simplify each gate symbolically before believing it.**  If the expression
  reduces to `0 ≡ 0`, or to `x` fitted against `x`, or to a comparison of two
  textually identical subexpressions, the gate is a no-op regardless of what
  it prints.  Feed it absurd inputs (`two_s = 3.7`, `−5.0`, `1e6`) and see
  whether anything moves.
- **Check gate REACHABILITY, not just gate correctness.**  If an earlier gate
  fires first on every mutant, the later gates — typically the acceptance test
  the artifact actually rests on — are never exercised.  Report the exit
  *path*, not only the exit *code*: for each `--red` mode, name which gate
  killed it.  "All three mutants died at C4 and never reached the acceptance
  test" is a finding.
- **Mutate the DATA, not only the code.**  An acceptance checker must be shown
  non-self-fulfilling by falsifying the ground truth it compares against
  (shift every row, move the decision band, delete the band key, remove the
  data file).  A checker that only responds to flipping one of its own
  constants proves nothing about the claim.
- **Check for deductive subsumption between gates.**  If gate `Cj`'s bound is
  implied by gate `Ci`'s, `Cj` adds no evidence; say so and say what would.
5. `ace_ld_check.py` LD-C5: violates its own `(V-in)` hypothesis, never
   produces the `ν=0` atom it certifies, and **has no red mode at all**;
   `--red-coset` is bit-identical to a constant shrink and blind to cosets.

- **Check that every gate can FAIL AT ALL.**  A gate with no red mode is
  decoration.  Enumerate the gates, enumerate the red modes, and report any
  gate that no mutation reaches.  Then check each red mode is *specific*: if
  `--red-X` is bit-identical in effect to `--red-Y`, one of them is testing
  nothing it claims to.
