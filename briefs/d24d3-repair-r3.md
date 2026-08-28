# Work order — D24(d)3 adjudication, repair round 3

**FAIL(F1,M1–M5)**: 1 FATAL, 5 MAJOR, 8 MINOR, 5 NOTE.  Trajectory
r1 → r2: `3/7/6/4 → 1/5/8/5`.  **All three r1 FATALs and five of seven r1
MAJORs are VERIFIED FIXED by fresh recomputation, and the single r2 FATAL is
newly surfaced, not a survivor.**  This is a converging artifact; finish it.

The critic states the split is **honest** — the value really is retired, no L4
file will assert a value of `𝔞_leg`, and the repaired class strictly contains
the frozen one, so the merge cannot install r1's contradiction.  Keep that.

## WRITING DISCIPLINE

Derive and Write ONE section per response; the file on disk must be a valid
partial deliverable at every moment.

## READ FIRST

`CLAUDE.md`; `briefs/critic-protocol.md` (**Standing checker obligations**);
`theory/verdicts/d24d3-adjudication-r2-critic.md` **IN FULL** (your work
order — read its fenced "reproduced and fenced" items first and do not churn
them); `theory/verdicts/d24d3-adjudication-r2.md` (your artifact);
`theory/verdicts/d24d3-adjudication-r1-critic.md` §1 (14 items still fenced);
`definitions.md` **D24(b) lines 923–929**; `theory/verdicts/corpus-r2.md:174–178`.

## F1 (FATAL) — the amputation convention is missing, so `𝔞_leg` is a rename

`definitions.md:923–929` (D24(b)) says "**amputated** one-hard amplitude" and
**fixes no amputation convention** anywhere in D24, `notation.md` or
`claims/CLAIMS.md`.  A convention rescaling sends `M_1^O ↦ cM_1^O`,
`E^O_desc ↦ c'E^O_desc`, `𝔞_leg ↦ (c'/c)𝔞_leg`.  Consequences, all fatal to
the round's headline: `𝔞_leg` is a **renaming** of the unknown `L(0,h)`, not a
decomposition; nothing forces the density out of `L`; and **AMP is not a
statable lemma**, even though §8 nominates it as the next prover target.

FIX DEMAND: fix the amputation convention explicitly, as displayed text in the
D24(b) merge proposal, so that `𝔞_leg` becomes convention-independent and AMP
becomes statable.  If you cannot, say so plainly and retract AMP as a named
lemma — an honest "the decomposition is convention-dependent and therefore
empty" is a real finding and is better than a nominated target nobody can
state.  Also fix `⟨1⟩2.⟨3⟩1`, whose justification cites three prose sentences,
none of which is a D-number, claim id, or named computation — an L6b leaf
violation at the load-bearing step.

## THE FIVE MAJORS

- **M1** — three merge strings claim the frozen clause is "recovered verbatim"
  at `ρ = 1/2`.  **False**: the repaired clause leaves `𝔞_leg` free at
  `ρ = 1/2` too.  Draw the consequence the artifact never draws: after the
  merge, **ML5-B (PROVED) predicts no number at any density**.  Decide and
  state what that means for ML5-B's row.  Also strike §5.1/ML5-A's claim about
  "the form in which D24(e) and `ml4_check.py` test it": the critic audited
  both — `ml4_check.py` has zero `chi`/`sgn` occurrences and both `𝔠_h`
  counterexamples have `M_1^O = 0`, so nothing there tests `𝔞_leg`.
- **M2, M4** — **two missed lockstep sites, one serious**:
  `theory/verdicts/corpus-r2.md:174–178` is the **promotion record** that made
  ML5-B PROVED and verifies the `𝔞_leg = 1` arithmetic, yet it stays in the
  row's where-proved column while the conclusion changes; and
  `paper/main.tex:524–527` is cited three times as authority but appears in
  neither §4.2 nor §4.3.  (`ml5-universality.md`, `TRIANGLE.md`,
  `notation.md`, `ml4_check.py`, D24(e) were verified **complete** — do not
  churn them.)
- **M3** — the checker, below.
- **M5** — D24-VAL's status is wrong **for a stated reason that is a category
  error**: unproved antecedents never downgrade an implication, and ML5-B and
  M-INDEX-spec carry PROVED for the same logical shape.  Its where-tested
  column also names gates that cannot test it.  Note the critic's positive
  finding: D24-VAL is vacuous-or-unknown at all four points **but honestly
  labelled so**, in three places — the S2 lane's R2-O2 pattern is NOT repeated.

## M3 — the checker, third pass

Fenced as genuinely fixed: green plus all four reds with exact exit paths; the
`−6%` mutant passes C4 (0.064) and dies at C6; `−7.99%` dies at C4 at 0.0839;
**both r1 no-ops are genuinely gone**.  Remaining:
- `C2(ii)` is still an identity in `two_s` probing only the `n=0` ladder
  element — a `cA_deepladder` mutant (wrong at every `n≥1`) **passes C2** and
  dies only at C3;
- the momentum loop is decorative; `require(1**p − 1 == 0)` cannot fail;
  `C7` is unfalsifiable at `N ∈ [60,480]`;
- **C6 is C4's comparison at a tighter band** — `predicted_jet(S,1.0) = 1/S`
  exactly, so both compare to the identical target and non-subsumption is free
  (any band `< 0.08`).  C6's real gain is the exponent interval
  `[0.989,1.017]` vs C4's `[0.947,1.061]` — say that, and stop claiming more.
- `ACCEPT_BAND = 0.02` is **post-hoc objectively** (`git log`: data
  `2026-08-26`, band `2026-08-29`) though your disclosure was accurate and it
  is not tuned to barely pass (6× margin).  It is however **1.2–2.4× tighter
  than the data's own quoted error** at every spin, and a `−3%` mutant inside
  the error bars is rejected.  Either widen it to the data's own error, or
  justify the tightening on the data's own terms.
- r1's M3(c)(iii) (build the jet from a constructed `E^O_desc`) was **declined
  without saying so** — either do it or record the declination.

## THE MERGE LIST (the critic's, apply it)

**MERGE**: clause 3a (unconditional — "the best thing in the round"), clauses
2/4/5, `notation.md` `Z_ρ` row, `𝒮_W(ρ)` row (l.258), `𝖲` row (l.244),
overload-rule-2 amendment, §5.5 ADVISORY.
**MERGE after one edit**: §5.1 D24(c) (strike the false D24(e)/`ml4_check.py`
clause); D24(d) preamble (add F1's convention sentence); clause 1 + `E^O_desc`
row (amend overload rule 8 — `E_O` is registered at `notation.md:124`); `L`
row (scope the provenance to D6).
**HOLD**: clause 3b, ML5-B row, D24-VAL row, ML5-A row, `𝔞_leg` row (its
rationale "bare `𝔞` is `𝔞_α`" is false — `𝔞_α` is subscripted).

Produce ONE coherent merge proposal: the orchestrator will not apply a partial
clause-3 split into an L4 file.

## LANE (writable, nothing else)

`theory/verdicts/d24d3-adjudication-r3.md` (create),
`theory/verdicts/d24d3-repair-r3-response.md` (create),
`theory/checks/d24d3_normalization_check.py`.  No shared-file edits; MERGE
PROPOSALS only.  No commits.

Work fully autonomously.  Do not ask questions.  ONE section per response.
