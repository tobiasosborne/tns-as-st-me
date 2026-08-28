# Work order — D24(d)3 ρ-normalization adjudication (orchestrator lane)

Corpus referral bd `tns-iu5`, P1, BLOCKS the D29/D30 merge and bd `tns-axg`.
You are an adjudicator, not a lane advocate: neither S1 lane may own this edit,
and you must not import either lane's workaround uncritically.

## THE DEFECT (S1-A r1 critic, cross-lane item 4)

`definitions.md` D24(d) clause 3 freezes the external flux normalisation as
`L(0,h) = −iχ/v_h`.  Combined with the PROVED row **ML5-B**, that constant
predicts soft slope **2 at EVERY tail density ρ**.  This contradicts the
PROVED row **S2-2body-S**, which gives slope **1/S** at site spin `S`, exact
for all `S`.  The two agree only at `ρ = 1/2`.  Consequence: the source class
`𝒮_W` of D24(d) is **EMPTY for ρ ≠ 1/2** — vacuous, not false.

The two S1 lanes patched it incompatibly and both were faulted for it:
S1-A silently redefined the flux constant inside its own D29(5) (part of its
FATAL F1); S1-B kept D24(d)3 verbatim and multiplied by an **undefended**
factor `1/(2ρ)`.

## THE TASK

Adjudicate the ρ-dependence of the D24(d)3 normalisation **once**, in
`definitions.md`, so that it is DERIVED rather than stipulated.

Acceptance arithmetic, fixed in advance:
- the repaired normalisation must reproduce slope **1/S** for spin-`S`
  (matching PROVED S2-2body-S at `S ∈ {1/2, 1, 3/2, 2}`), and
- must reproduce **2** at `ρ = 1/2`, and
- must leave every other clause of D24(d) and the PROVED implication ML5-B
  intact, or else say exactly which clause has to move and why.

Note for calibration (this is a hint, not a result — verify or refute it):
a factor `1/(2ρ)` on `L(0,h)` reproduces both numbers, since
`2·(1/(2ρ)) = 1/ρ` and `ρ = S` for the fully polarised tail.  That is exactly
S1-B's undefended factor.  Your job is to decide whether it is CORRECT and, if
so, to **derive it from the LSZ flux normalisation of the external leg** —
where does the tail density enter the external-leg flux factor? — rather than
to bless it.  If it is wrong, produce the right ρ-dependence and show the
arithmetic.  If no ρ-dependence can be derived and D24(d)3 must instead be
retired or split, say so plainly: an honest refutation with the surviving
weaker statement is the preferred outcome over a fitted constant (rk-light
law 5).

## READ FIRST

1. CLAUDE.md (laws; L4 single-source definitions; L10)
2. `definitions.md` D24 IN FULL (esp. (b) the packet norms, (c) the contact
   first jet, (d) clauses 1--5, (e) the refuting sources), D13(a), D25
3. `claims/CLAIMS.md` rows: ML5-A, ML5-B, ML5, S-general, S2-2body,
   **S2-2body-S**, M-IDX-density (which fixes what `ρ` means and proves
   `2ρ ∈ ℤ`), and note that `ρ` is a DENSITY symbol distinct from D13's
   site-spin `s` — the r2 objection-1 fence
4. `theory/ml5-universality.md` IN FULL (⟨1⟩2 ML5-A, ⟨1⟩3--⟨1⟩4 the
   implication and the `O_η` refutation)
5. `theory/spin-s-twomagnon.md` (the PROVED 1/S slope law and its register)
6. `theory/verdicts/soft-index-r1.md` cross-lane item 4 (the finding),
   `theory/verdicts/soft-index-b-r1.md` (lane B's 1/(2ρ) and why the critic
   called it undefended), `theory/verdicts/soft-index-adjudication-r1.md` §3
7. `theory/checks/spin_s_slope_check.py` and
   `numerics/results/spin1-bc-falsifier.json` — existing spin-S slope data
   you can and should reuse as ground truth

## YOUR LANE (writable — nothing else)

- `theory/verdicts/d24d3-adjudication-r1.md` (create — the adjudication)
- `theory/checks/d24d3_normalization_check.py` (create — the certificate)

**Do NOT edit `definitions.md` yourself.**  Put the repaired D24(d) clause 3
(and any other clause that must move with it, and the re-scoped ML5-B row text
for `claims/CLAIMS.md`) in a **MERGE PROPOSALS** section of your verdict file,
as EXACT replacement text with the surrounding context needed to apply it
verbatim.  The orchestrator applies it.

## DELIVERABLE

`theory/verdicts/d24d3-adjudication-r1.md` containing:
1. **Statement of the defect**, reproduced by your own independent
   computation — do not take the critic's word for slope 2; derive it from
   D24(d)3 + ML5-B yourself and show the steps.
2. **The adjudication**, in Lamport form: the derivation of the correct
   ρ-dependence from the external-leg LSZ flux normalisation, with every leaf
   citing a D-number, a claim id, or a named computation.
3. **Acceptance check**: the repaired constant evaluated at
   `S ∈ {1/2,1,3/2,2}` against PROVED S2-2body-S, and at `ρ=1/2`.
4. **Blast radius**: every claim row and every shard step whose text changes,
   listed by id and step address (grep, don't guess).  Explicitly answer:
   is `𝒮_W` nonempty after the repair, or is nonemptiness still open?
5. **MERGE PROPOSALS**: exact replacement text for `definitions.md` D24(d)
   and for the ML5-B row of `claims/CLAIMS.md`.
6. **HONEST STATUS**: what is proved, what is stipulated, what is evidence.

## CHECKER OBLIGATION

`theory/checks/d24d3_normalization_check.py` must be red-capable: green exit 0
under `python3 -O`; at least two `--red` mutations that MUST exit 1 (e.g. the
frozen ρ-independent constant, which must now FAIL at `S=1`; a wrong power of
ρ).  No bare `assert`.  Mutation-test on COPIES in a temp dir.  Reuse the
existing spin-S data rather than inventing numbers.

Work fully autonomously.  Do not ask questions.
