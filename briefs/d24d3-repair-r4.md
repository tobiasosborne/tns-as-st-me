# Work order — D24(d)3, repair round 4 (the closing round)

**FAIL(F1,M1–M5)**: 1 FATAL, 5 MAJOR, 8 MINOR, 4 NOTE.
Trajectory `3/7/6/4 → 1/5/8/5 → 1/5/8/4`.

**Read the critic's own assessment before you plan anything:** five of r2's six
items are VERIFIED FIXED by fresh recomputation; the r3 FATAL is **newly
surfaced, not a survivor** — it is reachable *only because* §5.0 now exists;
and the remaining blockers are, in the critic's words, **"three sentences
(F1), two citations (M1), one clause (M4), one row (M5)."**  This round closes
the artifact.  Do not redesign it.

## WRITING DISCIPLINE

ONE section per response, written to disk before you think about the next.

## READ FIRST

`CLAUDE.md`; `briefs/critic-protocol.md` (Standing checker obligations);
`theory/verdicts/d24d3-adjudication-r3-critic.md` **IN FULL** — and its
**X1–X15 fenced VERIFIED list FIRST**: fifteen items are certified, including
the leg-conversion identity and eigenvector, all §3/§7.1 arithmetic, the
derived band `0.047854`, span appliability, every `notation.md` anchor,
ML5-B's constant-agnostic proof, the annotation-not-erratum call, the complete
withdrawal, and the 1.69× correction.  **Do not churn any of them.**
Then `theory/verdicts/d24d3-adjudication-r3.md` (your artifact), and the r1/r2
critic verdicts for priors.

## F1 — the FATAL, and it is three sentences

§5.0 normalises `M_2^O`'s soft leg **but not the soft leg inside clause (d)2's
residue** — the object that actually fixes `𝔞_leg`.  The critic measured the
residue in both normalisations at `2S = 1,2,3,4`, `N=8`: against the
charge-created leg it is `2i·Z_ρ·J sin h` (what clause 2 displays and D24N-C3
certifies); against the δ-normalised leg §5.0 mandates it is
`2i·√Z_ρ·J sin h`.  It also computed `‖Q^-_q|h⟩‖² = Z_ρN − 2` analytically and
by ED, reproducing `ml4-ward-reduction.md` (11)'s `(N−2)` at `Z_ρ = 1`.
Therefore `⟨1⟩0.⟨3⟩1`'s "clauses 1,2,4,5 are invariant" is **false for
clause 2**.

The trilemma you must resolve explicitly, because each horn has a different
cost:
- **literal reading** (per your own merged preamble, "All amplitudes below are
  in the normalisation convention of (b)") makes clause 2 **unsatisfiable** by
  `√Z_ρ` at every `ρ ≠ 1/2` — `𝒮_W(ρ)` is provably empty again and the
  original defect is reinstated one clause over;
- **shape reading** → r2's F1 survives verbatim;
- **normalisation-fixing reading** → `𝔞_leg = 1` by construction.
Your ⟨1⟩4's `Z_ρ^{-1/2}` follows only from the **mixed** reading your preamble
forbids.  All of this is invisible at `ρ = 1/2`, which is why three rounds
missed it.

FIX: say, in displayed text, which normalisation clause (d)2's residue is
quoted in, and make clauses 1–3 consistent with that choice.  Then re-derive
⟨1⟩4 under the reading you actually adopt.  If the honest outcome is that the
narrowing survives only under a reading you must now adopt explicitly, say so.

## THE Q IDENTITY SURVIVES — protect it

`Q^-_k|Ω⟩ = √(Z_ρ)|k⟩` is **exact**: independent from-scratch ED at
`2S = 1,2,3`, `N = 5,6`, residual `0.000e+00`, with `|k⟩` an exact `H_S`
one-magnon eigenvector to `≤3.2e-15`.  Every refutation number was recomputed
by hand — `0.0004 / 0.4158 / 0.7347 / 1.0033`, margins **5.2–12.5×** against
the pre-registered `0.08`, needing no band at all.  The critic calls the
narrowing "the best thing in the round", conditional on F1's reading.  Keep it,
and fix its one soft spot (m1): the **descendant** leg carries `Z_ρ − 2/N` per
site and is exact only in the LSZ limit, while D24N-C8 tests only the vacuum
case.

## M1 — the convention's authority is thinner than claimed

It is well defined **only in the fully polarised spin-`S` register**.  D12(b),
cited as its authority, **fixes no norm and explicitly withdraws** the one norm
claim it made; at general `ρ` the asymptotic one-magnon kernel is claim **ML1,
which is CONJECTURE**.  It is consistent with existing corpus uses of
"amputated" only because **every existing use sits at `ρ = 1/2`** —
`ml4-ward-reduction.md:63–68` grants strictly wider amputation freedom, and
`ansatz-scattering-2m.md:621–631` uses the very `S_phys`-valued convention your
⟨1⟩0.⟨3⟩6 says it refuses.  Two citations to fix; scope the convention to the
register where it is defined, and name ML1 as the gap off that family.

## M4 — the rename is live at 18 sites, you listed 5

`𝒮_W → 𝒮_W(ρ)`: two omissions are **inside `definitions.md` itself**
(l.916 header, l.1004), plus `CLAIMS.md:29,82`, `ml5-universality.md` ×5,
`main.tex` ×4.  Enumerate all 18.

## M5 — one row: `AMP`.  M2/M3 — the checker

- **"There is no acceptance constant in the file" is FALSE, and you assert it
  in four layers.**  `EXPONENT_FIT_BAND = 0.03` gates C6, is post-registered,
  and is **strictly tighter than the derived band** — a `−3.4%` shift inside
  the data's own quoted error dies on it.  r2's M3(b)(iii) is **relocated, not
  fixed**.  Either derive that band too, or retract the four claims.
- Guards: zero ✓, missing ✓, **over-wide ✗** — one inflated error entry gives
  band `0.0790` and silently loosens C6 by 1.65×.
- **Fifth shipped no-op in this certificate**: the "real cross-momentum
  orthogonality gate" is `0 ≡ 0` for every input (probed at 1, 3.7, −5, 1e6),
  and `cB_onek` is killed only by `require(len([a,b,c]) >= 3)`, a
  constant-true assertion — remove that guard and one momentum passes with
  `max_error` **identical to green**.
- Self-declared gaps: accurate on all five declared, **incomplete on three**.

## MERGE — nearly there, and it must still land as ONE commit

The three `definitions.md` spans **do** apply cleanly in descending order
without overlap (the critic applied them to a scratch copy; anchors exact; the
(b) replacement preserves the original paragraph verbatim).  **But
`notation.md`'s six edits carry no ordering instruction and the written order
breaks two of their own stated anchors** (m3) — supply the order.

Critic's rulings to honour: **MERGE** §5.2 clauses 1, **3a unconditionally**,
4, 5 and closing; §5.3d ML5-A; §5.4a `Z_ρ` and `E^O_desc` rows; §5.4c/d/e/f;
§5.5 (**not optional, and extend it**).  **MERGE-after-F1**: §5.1 D24(c);
§5.3a ML5-B; §5.3b `D24-VAL`; §5.4a `L(k,h)` row.  **HOLD**: §5.0, §5.2
preamble, §5.2 clause 2, §5.2 clause 3b, §5.3c `AMP`, §5.4a `𝔞_leg(ρ)` row,
§5.4b `𝒮_W(ρ)` row.

Note two rulings in your favour: the `D24-VAL` plain-`PROVED` status deviation
was **required** by the CLAIMS header (the r2 critic's label was wrong and it
says so), and r1's M3(c)(iii) declination is **accepted as correctly
reasoned**.

## LANE (writable, nothing else)

`theory/verdicts/d24d3-adjudication-r4.md`,
`theory/verdicts/d24d3-repair-r4-response.md`,
`theory/checks/d24d3_normalization_check.py`.  MERGE PROPOSALS only; no
shared-file edits; no commits.

Work fully autonomously.  Do not ask questions.  ONE section per response.
