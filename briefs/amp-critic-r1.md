# Work order — AMP r1 HOSTILE CRITIC (the only critic round)

Target: `theory/amp.md` + `theory/checks/amp_check.py`, the prover's
OBSTRUCTION verdict on claims row AMP: that D24(b)+(d) fix only the leg
conversion `Z_ρ^{-1/2}` and leave the residual scalar unconstrained, so
`𝔞_leg(ρ) = 1/Z_ρ` is not derivable from current hypotheses.

## Process contract (PRD.md — read first)

This is the ONE hostile round; one repair wave follows, then the
orchestrator adjudicates mechanically. Budget your hostility accordingly:
find what is WRONG, not what could be polished. Verdict classes: FATAL
(conclusion false or unsupported), MAJOR (a step's stated justification
does not prove it), MINOR, NOTE. Rigor follows the claim's role: this is a
supporting lemma about definitional underdetermination, not a headline
theorem — do not expand scope into meta-audits (PRD forbids it).

## READ

`PRD.md`; `claims/CLAIMS.md` rows AMP, D24-VAL, ML5-B; `definitions.md`
D24 in full; `theory/verdicts/d24d3-adjudication-r5.md` §5 (text of
record) and `-r3.md` ⟨1⟩4, `-r4.md` §1.3; `theory/checks/
d24d3_normalization_check.py` (run it); `briefs/amp-prover.md` (the
prover's binding fence); then the target files.

## ATTACK SURFACES (mandatory; add your own)

1. **The freedom certificate.** An underdetermination claim is only proved
   by exhibiting TWO admissible packages satisfying EVERY D24 clause
   (1,2,3a,3b,4,5, both conventions of (b), the invariance list) with
   different `𝔞_leg`. Does AMP-C1 actually construct full D24 packages, or
   only the clauses the prover found convenient? Recompute; if a clause is
   silently unverified in the construction, that is MAJOR at least.
2. **Hidden constraints.** Does any D24 clause, notation.md rule, or the
   d24d3-r5 merged text constrain the residual scalar in a way the shard
   missed (e.g. the two-anchor convention of D24(b), the invariance list,
   the clause-2 LSZ scope, C¹-uniformity of the 3a extension in ρ or h)?
   If yes, the OBSTRUCTION is FALSE and that is FATAL.
3. **The double-count accounting.** The shard claims exactly one inverse
   square root survives (AMP-C2). Recompute the vacuum and descendant
   factors independently from D24N-C8's construction. Check the finite-N
   route (AMP-C3): is `N·|a_N − Z_ρ^{-1/2}|` bounded, and is the limit
   claim actually what the finite-N algebra gives?
4. **Checker honesty.** Run green + both red modes yourself. Does each red
   mode mutate something a REAL defect would produce, or is it theater?
   Does any gate certify less than the shard's checker section claims?
5. **Consistency with the corpus.** The shard must not contradict D24-VAL
   (the conditional value IS 1/(2S) under bridge (α)) or ML5-B's `𝔞_leg ≠ 0`
   usage. Check the MERGE PROPOSALS section's proposed CLAIMS wording for
   silent strengthening in either direction.

## LANE (writable; NOTHING else)

- `theory/verdicts/amp-r1.md` (CREATE)

Structure: verdict line first (PASS / FAIL(ids)); numbered objections
R1-O1… each with severity, the exact quoted text attacked, and your
recomputation; a final section proposing the exact CLAIMS.md disposition
for the AMP row (verbatim cell text) IF your verdict licenses one. No
edits to any other file. No commits.
