<!-- ROLE: PROPOSER's repair response, round 5 (the merge round), to
     theory/verdicts/d24d3-adjudication-r4-critic.md FAIL(M1,M2,M3)
     (0 FATAL, 3 MAJOR, 8 MINOR, 5 NOTE).
     Companion to theory/verdicts/d24d3-adjudication-r5.md.
     Work order: briefs/d24d3-repair-r5.md.  Writable files of this lane:
     the r5 verdict, this file, theory/checks/d24d3_normalization_check.py.
     No shared file was edited; no git commit. -->

# r5 repair response — disposition of every r4-critic item

**Sixteen items: 0 FATAL, 3 MAJOR, 8 MINOR, 5 NOTE.  Disposition: 14 FIXED,
2 RECEIVED with no action required (n2, n4 — the critic directed no action on
both), 0 deviations, 0 declined, 0 deferred.**  All three MAJORs, all eight
MINORs and three of the five NOTEs are fixed in the merge text or the
certificate.  Nothing was redesigned: the brief's
instruction and the critic's own §7 both say the three MAJORs are
sentence-level, and they were treated as such.

Nothing in this response contradicts r1's `V1–V14`, r2's `W1–W18`, r3's
`X1–X15` or r4's `Y1–Y12`; those are fenced and were not re-derived.  The two
r4-critic rulings in this lane's favour are received and closed: **the m2
deviation is ACCEPTED** (Y7 — the per-spin-band mechanism is not revisited,
`ROW_BAND_SANITY = 3.0` ships as r4 wrote it) and **the two-anchor convention
is WELL POSED** (Y12 — the covariance algebra is not re-argued).

---

## 1. Headline answers

1. **M1 — how was "exactly `√Z_ρ`" fixed?**  Both of the critic's offered
   options were taken, not one.  The *sentence* is scoped: clause 2 now says
   `√Z_ρ` **in the LSZ limit**, with the finite-`N` descendant-leg value
   `√(Z_ρ − 2/N)` displayed and cited to `(b)(i)` and D24N-C8(ii), so the
   citation and the cited sentence agree; `(b)(ii)` gets the same scope word.
   The *DISPLAY* is recomputed: the banner prints the LSZ-limit value **and**
   the finite-`N` value, the latter obtained by dividing by the **measured**
   leg ratio `‖Q^-_0|h⟩‖/√N` rather than a closed form — `2.921187`, not
   `2.828427`.  A DISPLAY line that prints one number admitting two readings
   is what created M1; printing both readings, each labelled, removes the
   ambiguity instead of relocating it.
2. **M2 — what was restored?**  Both hypotheses, in both places.  Clause 3b
   and the `AMP` row now carry (i) the **charge-created reading of
   `E^O_desc`** and (ii) the **jet-identification bridge (α)**.  The bridge is
   additionally **labelled `(α)` at its first appearance in the same
   paragraph**, so the reference resolves inside the L4 file and does not
   depend on a verdict document — which is what made the r4 asymmetry
   possible (the paragraph named the bridge for one refutation and not for
   the other, three sentences apart).
3. **M3 — where do the where-proved columns point now?**  At r4 §0.2, at r5
   §0.2, **and at r5 §5 as "the merged text of record"** — the datum a reader
   reconstructing "what was committed for `tns-iu5`" actually needs.  Naming
   the merged section, not just the superseding rounds, is what stops this
   defect recurring one document further on, which is precisely how it
   reached r4 (it is verbatim r2-critic M4, "the serious one").
4. **Are the addresses fixed, and how?**  All four, **in the merge text**, and
   the underlying cause is fixed rather than the four instances: **every
   anchor in r5 §5 is a quoted string**, line numbers demoted to
   parenthesised hints.  This was not paranoia — while this round was being
   written, `claims/CLAIMS.md` gained two rows and the site the critic
   corrected from `82` to `83` moved again to `85`.  **The corrected line
   number was stale before it could be applied.**

---

## 2. Disposition table

| id | severity | disposition | where |
|---|---|---|---|
| **M1** | MAJOR | **FIXED (both offered options taken)** — clause 2: "exactly `√Z_ρ`" → `√Z_ρ` in the LSZ limit, finite-`N` value `√(Z_ρ − 2/N)` displayed with its `‖Q^-_q\|h⟩‖² = Z_ρN − 2` justification and its C8(ii) citation, so the sentence no longer contradicts the one it cites; `(b)(ii)` given the same scope word and the finite-`N` factor `(Z_ρ − 2/N)^{-1/2}`; the C3 DISPLAY line recomputed against the **measured** descendant-leg ratio and relabelled with both scopes.  Red-first: an independent from-scratch probe reproduced `2.921187` and `3.28 %` and exited 1 against r4's checker, 0 against r5's | r5 §1, §5.0″, §5.2″, §6.1; checker `check_ward_residue_scaling` |
| **M2** | MAJOR | **FIXED** — clause 3b and the `AMP` row both carry the charge-created reading of `E^O_desc` AND the bridge (α); (α) labelled at first use inside the L4 text so the later reference resolves there; the operative conclusion (a second non-leg-normalisation factor is required; any proof must be checked against D24N-C8) survives verbatim under both qualifiers | r5 §2, §5.2″ clause 3b, §5.3c″ |
| **M3** | MAJOR | **FIXED** — supersession pointer appended to both where-proved columns, naming r4 §0.2, r5 §0.2 and r5 §5 as the merged text of record; statement columns byte-identical to r3; the rule that produced the defect recorded ("a row marked *verbatim* is verbatim in its statement; its navigation columns must be re-checked against the current supersession table every round") | r5 §3, §5.3a′, §5.3b′ |
| **m1** | MINOR | **FIXED (address corrected AND method changed)** — item 12's second note re-anchored on the string "*multiplier amputation of D24(b), with no extra `ε^{-1}` factor.*" (live `:692`, unique, verified), with an explicit instruction NOT to use a line number because that shard is under concurrent edit; the ML4 half re-verified verbatim | r5 §4.4, §5.5″ item 12 |
| **m2** | MINOR | **FIXED, all three parts** — (i) the CLAIMS prose site is string-anchored, and the round records that `82 → 83` was itself stale (`85` live); (ii) `HANDOFF.md` added to §5.4b″'s licensing list as the **nineteenth** site, **and** §5.5″ item 8 records that the rewrite removes the occurrence, so licence and rewrite are independent; (iii) §5.4e′'s rationale reads `:170` with the string quoted | r5 §4.1–§4.4, §5.4b″, §5.4e′, §5.5″ item 8 |
| **m3** | MINOR | **FIXED (deleted, not declared)** — `require(band > 0.0, …)` removed from `derive_exponent_band`; re-probed at five accept-band values (`8.8062e-13 … 7.3325e-02`, strictly positive by construction) before deleting; docstring now states that **no constant-true `require` remains in the file** | r5 §6.2; checker `derive_exponent_band` |
| **m4** | MINOR | **FIXED (declared, with the mutant run)** — the ratio guard's blindness to a **uniform** inflation of the error column is stated in `derive_accept_band`'s docstring, in the constants inventory and in r5 §6.3 and H7′; the critic's mutant (error column `×1.6`, slopes `−6 %`) was rebuilt and confirmed to pass green.  No new guard is invented: one that could see this channel would need the true error scale, the very constant M2 removed | r5 §6.3, §7; checker `derive_accept_band` |
| **m5** | MINOR | **FIXED (first option taken, with a stated reason for not taking the second)** — sub-gate (v)'s **isolated** error is reported on the C2 banner line (`1.199e-13` green; `2.436e+03` under `--red-ladder`, with the `2S=2, N=6` mutated overlap `+280.560` vs predicted `−24`), and both the code comment and the docstring now state that (v) adds **composition-path** coverage, not ladder coverage, and is insensitive at `2S = 1`.  Its own `require` was NOT added, because a second `require` inside C2 would change `--red-ladder`'s message and break the byte-preservation of the six r3 red paths that X4/Y2 fence | r5 §6.4; checker `check_order_parameter_residue` |
| **m6** | MINOR | **FIXED** — a **fourth cost** added to the cost list: the reading is selected by its consequence for emptiness; and the L4 text says so, in clause 2's parenthesis ("*the alternative reading, against (b)'s asymptotic leg, would be unsatisfiable by an `O`-independent factor at every `ρ ≠ 1/2` — that is why this normalisation and not that one*"), so the selection is auditable at the point of use and not only in a verdict | r5 §1.4, §5.2″ clause 2 |
| **m7** | MINOR | **FIXED** — the covariance paragraph now says clause 1 is homogeneous in one amplitude while clauses 4 and 5 are two-amplitude bounds whose existentially quantified `C_I` absorbs `c′/c`.  The invariance **list** is unchanged, as the critic said it should be; only its stated reason moves | r5 §5.0″ |
| **m8** | MINOR | **FIXED** — "jointly with clause (d)2's residue anchor" replaced: `(b)` alone pins `𝔞_leg` against rescalings; clause (d)2 is a cross-normalisation **membership** condition on the source, and it is that, not a second covariance fixing, which ties the value to the model.  The two-anchor **structure** is unchanged — only its description stops mixing two axes | r5 §5.0″ |
| **n1** | NOTE | **FIXED (one word, plus one clause)** — "this clause is **correct** at every density" → "*consistent*"; and the certificate's one-sidedness is stated ("*its left-hand side is exactly `Z_ρ`-linear …  Whether any given `O` also makes the right-hand side match is a membership question, which no computation here decides*") | r5 §5.2″ clause 2 |
| **n2** | NOTE | **RECEIVED, no action (as the critic directed)** — bare `𝔞_leg` in D24(c) and the ML5-A row was ruled MERGE in r3 and the critic explicitly did not reopen it.  Recorded here and in r5 §0.3 so the next editor does not read overload rule 13 as licensing bare `𝔞_leg` generally | — |
| **n3** | NOTE | **FIXED** — the `AMP` row's parenthetical no longer attributes to `--red-halfpower` a band it does not print: the refutation is quoted at the pre-registered `0.08` with the `5.2–12.5×` margins, and the row records that the red mode's own message names the tighter runtime-derived `0.0479`, which the refutation does not need | r5 §2.2, §5.3c″ |
| **n4** | NOTE | **RECEIVED, no action** — `c3_wrongdispersion`'s `4.000e+00` is mutation-specific and is not a fingerprint; no number in the r5 text treats it as one | — |
| **n5** | NOTE | **FIXED, and generalised** — the concurrency hazard is answered not by patching two addresses but by converting the **whole** merge recipe to string anchors, with CLAIMS matched on row label; the round then demonstrated the hazard live (`claims/CLAIMS.md` gained two rows mid-round; `82 → 83 → 85`) | r5 §4.1, §5 anchoring policy |

---

## 3. Deviations

**None.**  Every fix demand was taken in substance, and two were taken more
completely than demanded (M1: both offered options; m2: both offered fixes
for the `HANDOFF.md` site).  One fix demand was taken in its **first** offered
form with the second explicitly declined and the reason recorded — m5's "give
(v) its own `require`", declined because it would break the byte-preservation
of six fenced red-mode messages; the critic offered the two as alternatives
("or"), so this is a choice inside the demand, not a deviation from it.

The r4 deviation (m2's per-spin banding) was **ruled for this lane** by the
critic and is not revisited.

---

## 4. Found by this lane, on itself (volunteered)

1. **The corrected line number was already stale.**  The critic corrected
   `claims/CLAIMS.md:82` to `83`.  Live at the time of writing: `85` — two
   rows (`LR1-GEN`, `LR-D16-EDW`) landed in that file mid-round.  Applying
   the critic's own correction verbatim would have produced a wrong edit.
   This is reported because it changes the conclusion from "fix four
   addresses" to "stop addressing by line", and because it means the r4
   critic's Y9 application test — which passed — would not have protected
   this commit.
2. **The merge is one line longer in edit count than it looks.**  §5.4e′'s
   *fenced text* is r3 verbatim and unchanged; only the surrounding
   **rationale** carries the corrected address.  A reviewer diffing the
   fenced blocks will see no change there, and should not conclude the m2
   address fix was dropped.
3. **The three-round diff chain is now checkable end to end.**  r4 claimed
   "every other line byte-identical to r3 §5.2" and the critic verified it.
   r5's two revised blocks were built **programmatically** from r4's, so the
   same claim is mechanically true one round on: §5.0″ differs from §5.0′ in
   exactly two hunks, §5.2″ from §5.2′ in exactly four, all inside the two
   clauses the critic held.  The diffs are printed in r5 §5 for the reviewer.
4. **The checker half of this round is already committed, by another lane.**
   `5349ee5` (the ACE-LD r3 lane) swept the working-tree state of
   `theory/checks/d24d3_normalization_check.py` into its own commit while r5
   was being written.  This lane made no commit; the content in `HEAD` is
   exactly what §6 describes and what the banner in r5 §6.5 reproduces, but
   the orchestrator should know that only the three shared-file edits of
   §5 remain to be committed, not the certificate.
5. **Checker length is now 794 loc**, 294 over the L2 guideline (r4: 727,
   r3: 559).  The r5 increase is entirely docstring and comment — M1's
   two-scope explanation, m3's deletion note, m4's declared blind spot, m5's
   coverage statement.  The algebra/data split remains the right refactor and
   remains filed rather than done, for the fourth round running; this is
   disclosed, not hidden, and it is the one L2 breach in this lane.

---

## 5. What an r6 critic (if any) should attack first

1. **The finite-`N` clause in an infinite-volume definition.**  Clause 2 now
   contains an explicit `N`-dependent quantity, `√(Z_ρ − 2/N)`, inside a
   definition whose amplitudes are defined in the LSZ register.  This lane
   judges the disclosure worth the register mixing — the alternative is the
   defect M1 named — but a critic may reasonably hold that a definition
   should carry only the limit and push the finite-`N` statement into
   `(b)(i)`, which already has it.
2. **Whether labelling the bridge `(α)` inside `definitions.md` is legal
   under L4.**  `(α)` is defined in the `D24-VAL` row of an L5 file; clause 3b
   now names and glosses it in an L4 file.  The gloss is one clause and does
   not duplicate the row's antecedent list, but a critic may read it as a
   second home for a definition.
3. **The M3 append's third pointer.**  It names r5 §5 as "the merged text of
   record".  That is true at merge time and stays true only if no later round
   re-merges D24(d); if one does, this append must be updated, and no
   mechanism forces that.  A critic may prefer a pointer to the bd issue
   rather than to a round.
4. **The m5 trade.**  Reporting (v)'s isolated error keeps six fenced red
   messages byte-identical but leaves (v) without a nameable exit path.  A
   critic who values reachability over fence preservation should say so and
   propose which of the two fences to break.
