# Critic brief — AC-EX-2M round 3 (adjudication round)

Read `briefs/critic-protocol.md` first; everything there binds.

**TARGET:** `theory/ansatz-scattering-2m.md`,
`theory/ansatz-scattering-2m-r2-response.md`,
`theory/checks/ansatz_scattering_2m_check.py`.
**VERDICT FILE (your only writable file):**
`theory/verdicts/ansatz-scattering-2m-r3.md`.

**This is an ADJUDICATION round, not a fresh attack.**  Your own r1 and r2
verdicts are your priors.  Scope your reading with `git diff` — attack what
CHANGED, verify claimed dispositions, and do NOT re-litigate what already
passed.  That narrowing is the cost control; a round that reopens settled
text has failed.

**Read:** `theory/verdicts/ansatz-scattering-2m-r1.md` and `-r2.md` in full;
`briefs/s2-repair-r2.md` (the work order the prover was given);
`theory/ansatz-scattering-2m-r2-response.md` (its claimed dispositions).

**Obligations specific to this round:**

1. **Verify every claimed disposition by fresh recomputation**, one row per
   objection: VERIFIED-FIXED / PARTIALLY-FIXED / NOT-FIXED / REGRESSED.  A
   prover claim of "FIXED" is a hypothesis, not evidence.
2. **R2-O1 is the round's centre of gravity.**  The demanded repair was to
   port the creator-choice-independence clause of the Haag--Ruelle theorem in
   `refs/arxiv-1412.2970` and thereby prove (ACE2M-LSZ) as an OPERATOR
   statement.  Check against the local TeX by section and equation number
   (L3 — never from memory): does the ported clause say what the shard needs?
   Are its hypotheses actually owned by this shard, as the r2 critic asserted?
   And does the result now survive the corpus's PROVED (R8), which gives
   `Q_{k_s}|k_h⟩ − |B^in⟩ = −2ik_s|P_12⟩ + O(k_s²)` — nonzero at exactly the
   soft law's linear order?  If the prover instead downgraded, check the
   downgrade is honest and complete rather than a restatement of the same
   claim in softer words.
3. **R2-O2**: is (A2M.3) now scoped to the diagonal order actually proved, or
   is the iterated order proved?  Vacuous-truth gaps are FATAL if they
   reappear.  Clause 3's packet qualifier and the `L²(I)` denominator bound
   must both be present and used.
4. **Checker regressions**: the two specced defects were the missing
   "connected" in A2M-C1a (literal reading failed by 1.0) and the ratio
   gate's tolerance (spec's own 1e-12 fails green from d=7).  Verify both are
   fixed IN CODE, that green and every red mode still behave, and that no new
   gate is a no-op.
5. **Trajectory check**: r1 6 MAJOR → r2 2 MAJOR.  Report the r3 count and say
   plainly whether severity is falling monotonically.  If it is not, the
   artifact is being re-overclaimed each round and you should say so.

**Deliverable beyond the standard format:** an explicit **PROMOTE / HOLD**
decision for the (A2M.3) interface clause and for AC-EX-2M as a whole, with
the missing step NAMED for every HOLD.  If you PROMOTE, supply the exact
scoping sentence to be copied verbatim into `claims/CLAIMS.md` — the
orchestrator will apply it without paraphrase.
