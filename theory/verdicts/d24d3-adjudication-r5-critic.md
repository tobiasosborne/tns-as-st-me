<!-- ROLE: ADVERSARIAL CRITIC verdict, round 5 (FINAL MERGE CLEARANCE) on
     corpus referral bd `tns-iu5`.
     TARGETS: theory/verdicts/d24d3-adjudication-r5.md,
              theory/verdicts/d24d3-repair-r5-response.md,
              theory/checks/d24d3_normalization_check.py.
     Brief: briefs/d24d3-critic-r5.md; protocol: briefs/critic-protocol.md.
     Priors: r1 (3 FATAL/7 MAJOR), r2 (1/5), r3 (1/5), r4 (0/3).
     WRITABLE FILE OF THIS LANE: this file only.  No shared file was edited,
     the target and its checker were not touched, no git commit was made. -->

# r5 critic verdict — D24(d)3, the merge round: the merge is CLEAR, five MINORs are owed

**Verdict line: `PASS`.  0 FATAL, 0 MAJOR, 5 MINOR, 6 NOTE.**

**Trajectory `3/7/6/4 → 1/5/8/5 → 1/5/8/4 → 0/3/8/5 → 0/0/5/6`.**  Second
consecutive round with no FATAL, **first round with no MAJOR**, and the first
in which the repair was itself put through red-green before it shipped.  All
three r4 MAJORs are fixed in substance and in the merged bytes; I verified
each by fresh recomputation rather than by reading.  The five MINORs below
are one L5 rendering defect, one dropped quantifier, one gate-subsumption
residual, one overstated anchoring claim and one mis-cited path — none of
them blocks the commit, and each carries a one-line fix.

**GO on the commit.  See §7 for the exact ordered recipe, §8 for the
checker-in-`HEAD` determination (the lane is RIGHT), §9 for `tns-iu5`.**

---

## 0. What I did

* Read `CLAUDE.md`, `definitions.md`, `notation.md`, `claims/CLAIMS.md`, the
  three targets in full, and the r4-critic verdict (my priors) in full.
* **Rebuilt M1's numbers from scratch twice** — once by a paper derivation of
  `‖Q^-_q|h⟩‖²`, once by an occupation-basis ED with its own ladder
  coefficients — at twelve `(2S,N)` points including `N = 10`, which the
  checker never tests, and at odd `N`, and at the excluded point `q = h`.
* **Ran the lane's own probe against both checkers** (r4's, extracted from
  `a979177`, and `HEAD`'s) to test the claimed red-green transition.
* Ran green + all seven red modes + eight of the lane's data mutants under
  `python3 -O`; built **eleven fresh data mutants of my own**, including two
  that falsify the ground truth itself; built **thirteen code mutants on
  copies**, one per gate, and recorded the exit *path* of each.
* **Applied all thirteen merge edits myself**, by string anchor with an
  assertion at every step, to copies of the **current** (post-`8a92310`)
  shared files, and diffed the result byte-for-byte against the lane's.
* Re-grepped every anchor in §4.3, §5 and §5.5″ for existence and uniqueness
  at the live file state; re-checked the nineteen-site enumeration whole-repo.
* Ran the reliance audit (REFUTED rows, ML4-Ward (9) at `n≥2`, Bethe, `𝒮_W`
  nonemptiness) against the **merged** text, not the verdict prose.

---

## 1. VERIFIED CORRECT this round — FENCE THIS, do not churn it

The `V*` (r1), `W*` (r2), `X*` (r3) and `Y*` (r4) fences stand and were not
re-derived except where a claim of this round depends on them.  New fences
`Z1–Z20`.

**Z1.  The red-green transition on the repair is REAL, and I reproduced it.**
`scratchpad/m1_display_probe.py` imports nothing from the repo: it builds the
two-quantum sector in the occupation basis with its own `ladder(n,t) =
√((n+1)(t−n))`, forms `Q^-_0|h⟩` by summing site lowerings over a normalised
one-magnon state, and compares the result against every float the C3 DISPLAY
line prints.  Run against `HEAD`'s checker: **exit 0**.  Run against r4's
checker (`git show a979177:theory/checks/…`, placed in a scratch root with a
copy of the data): **exit 1**, message "*the banner prints the LSZ-limit
number labelled as THE '(b)-asymptotic residue'*".  The acceptance test is
not self-fulfilling: it requires a printed float within `1e-5` of a number the
probe computed itself, **and** the two scope words.  A repair that is itself
red-green tested is the standard this campaign wants; this one meets it.

**Z2.  M1's numbers, recomputed by two independent routes.**  Paper: writing
`t := 2S`, `Q^-_q|h⟩` has pair part `t²Σ_{a<b}|e^{iqa+ihb}+e^{iqb+iha}|² =
t²(N²−2N)` (using `Σ_x e^{i(q−h)x} = 0`) and double-occupancy part
`2t(t−1)N`; dividing by the `tN` from `|h⟩`'s normalisation gives
`t(N−2)+2(t−1) = tN−2` **exactly**.  ED confirms at `2S = 1,2,3,4` and
`N = 6,8,10`: `4,6,8,10,14,18,16,22,28,22,30,38`, max error `7.1e-15`.  At
the operating point `2S = 4, N = 8, h = π/4`: `‖Q^-_0|h⟩‖² = 30.0000000000`,
leg ratio `1.9364916731` against `√Z_ρ = 2`, charge-created residue
`5.656854`, LSZ-limit `2.828427`, **finite-`N` `2.921187`**, discrepancy
**`3.2797 %`**.  The lane's table and my r4 table agree to every printed
digit, from three separate constructions.

**Z3.  The finite-`N` DISPLAY value is genuinely MEASURED, and the two scopes
are labelled.**  `check_ward_residue_scaling` divides by
`np.sqrt(inner(charged,charged).real/sites)`, where `charged` is built by
summing `apply_lowering` over sites — not by C8's closed form.  I substituted
the closed form `np.sqrt(two_s − 2/sites)` on a copy: the banner prints the
**identical** `2.921187`, which is simultaneously (i) proof that the code
measures rather than restates, and (ii) an independent confirmation that the
measurement agrees with C8(ii).  Both values remain DISPLAY and gate nothing,
which is the correct disposition (they would be subsumed by C3 ∧ C8 — Y4).

**Z4.  Green banner byte-identical.**  I extracted the fenced banner from r5
§6.5 and diffed it against live stdout under `python3 -O`: **identical**,
character for character, all twelve lines, exit `0`.

**Z5.  All seven red modes: same gate, same first stderr token, same
numbers.**  `--red-frozen`/`--red-power`/`--red-halfpower` all reach and die
at the **acceptance test itself** (C6) with `1.0016/2.0027/3.0033`,
`0.4984/0.6640/0.7467`, `0.4158/0.7347/1.0033`; `--red-ward` C3 `1.697e+01`;
`--red-ladder` C2 `1.477e+06`; `--red-legfactor` C8 `5.657e+00`;
`--red-descnorm` C8 `2.000e+00`.  Byte-preserved against Y2 and r5's table.

**Z6.  Eight data mutants reproduce exactly.**  `m6_shift30`, `m_shift34`,
`m_shift40` **pass** (X13/Y6 preserved); `m_shift45` dies at C6 acceptance
`S=2.0 dev=0.0482`; `m2b_shift60` at C6 `S=0.5 dev=0.0604`; `m2_shift799` at
C4 `0.0839`; `m_errwide` at the ratio guard `0.0790 … 3.78x … 0.0209`;
`m8_errinflate` at the subsumption guard `derived band 0.1914`.  And
**`errscale16_shift60` (error column `×1.6`, slopes `−6 %`) passes**, exactly
as §6.3 declares.  The blind spot is real, is disclosed, and is bounded.

**Z7.  Every gate can fail, and each dies at its OWN name.**  Thirteen
targeted code mutations on copies, one hypothesis each:
`c1_frozenjet` → C1; `c1_matchedjet` → C1; `c2_denseladder` → C2
`3.464e-02`; `c2_overlapsign` → C2 `1.280e+02`; `c3_dispersion` → C3
`5.657e+00`; `c4_truth` → C4 `1.0043`; `c6_ratioguard` → C6 corrupted-entry;
`c6_symbolicpin` → C6 `roots [1/2], not [1]`; `c7_gap` → C7 `1.855e-01`;
`c8_eigen` → C8 eigenvector `1.000e-02`; `c8_nosqrt` → C8 overlap
`4.060e-01`; `c8_descoff` → C8 descendant `1.000e+00`.  Control copy: exit 0.
**No gate in this file is decoration** — with the single exception recorded
at m3 below (C5).

**Z8.  The checker is not self-fulfilling: I falsified the DATA, not the
code.**  Eleven fresh mutants, every one dies at a named gate: band moved to
`0.20` → C4; `decision_band` key deleted → C4; `A_ring_summary` deleted → C4;
`error` column deleted → C6; errors zeroed → C6 "band is zero"; all `S=2`
rows dropped → C4; **ground truth replaced by `1/S²`** → C4 `1.0000`;
**ground truth replaced by the frozen law `2`** → C4 `3.0000`; error column
`×100` → subsumption guard `4.7854`; missing file → C4.  The one that
**passes** is `×1.59` error with `−5.9 %` slopes — the declared channel,
capped by the `band < 0.08` guard, i.e. bounded by the pre-registered band
against which the two refutations carry `5.2–12.5×` and `12.5–37.5×` margins.

**Z9.  Sub-gate C2(v), isolated, at every claimed number.**  Green isolated
error `1.199e-13` (it is the binding sub-gate — C2's reported max *is* (v)'s);
under `--red-ladder` isolated `2.436e+03`, with the `2S=2, N=6` mutated
overlap `+280.560` against predicted `−24`; insensitive at `2S = 1`
(`1.99e-14`, `2.57e-14`).  Its closed form `−2N·Z_ρ` I re-derived and
re-confirmed from scratch at eight `(2S,N)` points, max error `1.2e-13`.
Every one of §6.4's measured claims is exact.

**Z10.  m3's re-probe was actually run, not copied.**  `ratio = 0.880539`
reproduced; the five probe values are `8.8062e-13, 8.8054e-07, 8.8098e-04,
4.3221e-02, 7.3325e-02` — including the non-monotone first entry, which is a
double-precision artefact of `log(1/(1−1e-12))` and could not have been
produced by scaling the second.  The deleted guard was indeed constant-true.

**Z11.  THE MERGE APPLIES, IN ONE PASS, AGAINST THE FILES AS THEY STAND
NOW.**  I extracted all thirteen blocks programmatically (five of them from
r3, as the Mechanics table directs), asserted every string anchor unique at
the moment it is used, and applied them to copies of the current
`definitions.md` / `notation.md` / `claims/CLAIMS.md`: **13/13 in one pass**,
`definitions.md` descending, `notation.md` in `b″ → a′ → c → f → e → d`,
CLAIMS by row label.  My output is **byte-identical to the lane's scratch
application** (`cmp` clean on all three files).  Result: `1348 / 312 / 145`
by `wc -l` (= `1349 / 313 / 146` by `split("\n")` count — see n1).

**Z12.  The merged files are structurally sound.**  Overload rules run
`1…13` contiguously; rules 2, 8 and 13 read coherently; the blank line before
`All other symbols are unique.` is preserved; `D24(a)–(e)` read coherently
through `D25`; the five new `notation.md` rows introduce **no duplicate
registry key**; `N` is already a registered symbol (`notation.md:21`, D6), so
clause 2's finite-`N` sentence uses only registered notation; and after the
merge exactly **two** bare `𝒮_W` remain in `definitions.md` — the D24 header
and the D25 site — both of which §5.4b″'s licensing clause names explicitly.

**Z13.  The three diff claims are exactly true.**  §5.0″ vs §5.0′: **exactly
two hunks** (the covariance paragraph, m7+m8; `(b)(ii)`'s LSZ scope, M1).
§5.2″ vs §5.2′: **exactly four hunks, all inside clauses 2 and 3b**.  §5.4a′
is **byte-identical** to r4's four rows.  §5.4b″ differs from r4's by exactly
the insertion of `` `HANDOFF.md`, `` into the licensing enumeration.  The
three-round diff chain (r3 → r4 → r5) is therefore checkable end to end, and
I checked this link of it.

**Z14.  The stale-line-number vindication is confirmed, and the addresses are
fixed as strings.**  `claims/CLAIMS.md`'s corner-implication prose site is
live at **line 85** — not `82` (r4's), not `83` (my r4 correction): the file
gained the `LR1-GEN` and `LR-D16-EDW` rows at `137f922`.  **My own correction
went stale before it could be applied.**  The site is now anchored on the
string ``at `n≥2`, the exhaustive LSZ decomposition, and microscopic``, which
I verified unique.  All four addresses are fixed as strings, and
`HANDOFF.md:40` is present as the **nineteenth** site: live, string-unique,
**both** added to §5.4b″'s enumerated licence **and** rewritten by §5.5″
item 8, so neither depends on the other.  The nineteen-site enumeration is
complete for live corpus files (whole-repo re-grep; see m5 for the two
frozen-record sites).

**Z15.  Every same-commit anchor resolves at the live file state.**
`ansatz-scattering-2m.md` — item 12's string is unique at **`:692`**, and the
`E_O` string for §5.4e′'s rationale is unique at **`:170`**;
`ml4-ward-reduction.md` ML4-admissible sentence at `:64` (inside the stated
`63–68`); `corpus-r2.md:174–178`; `main.tex:244` still reads "five-condition"
(so the merged preamble's promise that the *count* is unchanged is kept),
`:524`, `:515–520`; `soft-index-b.md:808`; `soft-index-r1.md:170`;
`TRIANGLE.md` 24, 215, 254, 257, 528 — all five unique.  None of these files
moved in the two commits that landed during this review.

**Z16.  Reliance audit: CLEAN.**  Inside the merged D24 block the only ML4
contacts are the ML4-admissible amputation *class* (a definition), a
`ml4_check.py` pointer, the limitation sentence "*fixed-volume ML4 does not by
itself supply a volume-uniform bound*", and `ml4-ward-reduction.md` **(11)** —
which that shard's line 173 lists among the **PROVED** displays, and whose
`(N−2)` denominator my own `Z_ρ = 1` computation confirms is `‖Q_0|h⟩‖²`
(`N=6→4`, `N=8→6`).  The refuted second display of (9) at `n≥2` is never
touched.  `oracle-bethe.md` O7–O9 appears only as the contact route the
merged clause explicitly says its own conclusions do **not** rest on.
`S2-2body-S` is PROVED without an integrability hypothesis.  `𝒮_W(ρ)`
nonemptiness is never assumed: AMP is scoped to the `ρ` where the class is
nonempty, `D24-VAL` displays `(β_S)`, and the closing paragraph keeps it open
at every `ρ`.  No REFUTED row is used.  `ML1` is named at every point of use.

**Z17.  The checker in the worktree is byte-identical to `HEAD`, and `HEAD`'s
copy is the r5 version.**  `git diff HEAD` on the file is empty; the last
commit touching it is `5349ee5`; the diff `a979177 → HEAD` is `+92/−25` and
contains exactly the four r5 changes (the two-scope DISPLAY, the deleted
`require`, the declared blind spot, the isolated-(v) reporting).  §8 below.

**Z18.  No M3 append is owed on the `ML5-A` row.**  `corpus-r2.md`'s ML5-A
bullet certifies the two-condition iff — "*the two zero conditions remove the
first two unwanted terms and `K_O` bounds `R_2`*" — which is exactly what the
merged row still says, constant-agnostically.  It does not certify a
different conclusion, so the lane's reason for leaving §5.3d verbatim holds.

**Z19.  m7's and m8's replacement sentences are algebraically right.**  Under
`M_1 ↦ cM_1`, `M_2(k,·) ↦ c′(k)M_2(k,·)`: clause 1 is homogeneous in `M_2`
alone; clauses 4 and 5 have LHS scaling as `c′` and RHS as `c`, so they are
invariant only because `C_I` is existentially quantified and absorbs `c′/c`;
`𝔞_leg ↦ (c′(0)/c)𝔞_leg`, so `c′(0)/c = 1` from `(b)` **alone** pins it, and
clause (d)2 is a cross-normalisation membership constraint, not a second
covariance anchor.  The invariance *list* is unchanged, as I demanded.

**Z20.  All sixteen dispositions verified by fresh recomputation.**
14 FIXED (M1, M2, M3, m1–m8, n1, n3, n5), 2 RECEIVED with no action (n2 — not
reopened, and recorded so rule 13 is not read as licensing bare `𝔞_leg`; n4 —
`4.000e+00` appears **nowhere** in the r5 document, so no number treats it as
a fingerprint).  0 deviations, 0 declined, 0 deferred.  The one "declined"
half of m5 is a choice inside an "or", with the reason recorded; I accept it.

---

## 2. FATAL

**None.**

## 3. MAJOR

**None.**  All three r4 MAJORs land, in the merged bytes and not only in
prose:

* **M1** — merged clause 2 now reads "*differ by `√Z_ρ` **in the LSZ limit**;
  at finite `N` the descendant leg carries `√(Z_ρ − 2/N)` instead, since
  `‖Q^-_q|h⟩‖² = Z_ρN − 2` exactly ((b)(i); named computation D24N-C8(ii))*",
  and `(b)(ii)` carries the same scope with `(Z_ρ − 2/N)^{-1/2}`.  The
  citation and the cited sentence now agree, which is the whole of the
  objection.  The DISPLAY prints both scopes, each labelled, the finite-`N`
  one against the measured leg (Z3).  **Both offered options taken.**
* **M2** — clause 3b and the `AMP` row both carry (i) the charge-created
  reading of `E^O_desc` and (ii) the bridge, and the bridge is **labelled
  `(α)` at its first appearance in the same paragraph** (the frozen-stipulation
  sentence), so the later "*the same unproved bridge (α) named above*"
  resolves inside the L4 file.  The asymmetry I objected to is gone; the
  operative conclusion — a second, non-leg-normalisation factor is required,
  and any proof must be checked against D24N-C8 — survives verbatim.
  n3's stale band attribution is corrected in the same row.
* **M3** — both where-proved columns gain the supersession append naming r4
  §0.2, r5 §0.2 **and r5 §5 as the merged text of record**.  I checked r4
  §0.2's table: it does supersede the four r3 items the parenthetical names.
  **Does naming the merged section stop the recurrence?**  Partly, and the
  part that does is not the pointer.  The pointer is a fact with a shelf
  life — it is true at merge time and stays true only while no later round
  re-merges D24(d), as the lane itself flags.  What actually stops the
  recurrence is the **rule** r5 §3 records: *a row marked "verbatim" is
  verbatim in its statement; its navigation columns must be re-checked against
  the current supersession table every round.*  That rule generalises; the
  pointer does not.  I rule the fix sufficient **for this commit**, and I ask
  that the rule — not the pointer — be what `tns-iu5`'s closing note carries
  forward.

---

## 4. MINOR

**m1.  Two of the four `claims/CLAIMS.md` rows carry unescaped `|` inside code
spans, so they render as EIGHT-column rows in a six-column table — and the
"all four rows 6-column" verification claim is false for half of them.**

**(a) Location.**  r5 §5.3b′, the `D24-VAL` row (r5 `:763`), at
``𝒮_W(ρ)|_{ρ=S}`` — **twice**; r5 §5.3c″, the `AMP` row (r5 `:772`), at
``Q^-_k|Ω⟩ = √(Z_ρ)|k⟩`` — twice.

**(b) My computation.**  Splitting each row on `(?<!\\)\|` gives **8**
content fields where the table header (`| id | statement (short) | status |
depends on | proved in | tested in |`) has 6.  In a GFM table a pipe inside a
code span still terminates the cell unless escaped, so after the merge a
renderer shows `D24-VAL`'s *status* cell as "``_{ρ=S}` with `M_1^O ≠ 0` …``"
and `AMP`'s as "``Ω⟩ = √(Z_ρ)``" — not `PROVED` and `CONJECTURE`.  This is
**not** a defect r5 introduced in kind: the live file already has five such
rows (`S2-2body-S`, `ML4-Ward`, `M-tk`, `M-INDEX-fin`, `M-IDX-density`), and
`S2-2body-S` is the PROVED row this verdict's register comparison is taken
against.  But the corpus *does* have the convention — `WI`, `S2-2body`, `ML2`
and seven others escape as `\|` — and this commit adds two more violations to
an L5 single source in the round that claimed the rows were checked.

**(c) FIX DEMAND.**  In r5 §5.3b′ write ``𝒮_W(ρ)\|_{ρ=S}`` (both
occurrences) and in §5.3c″ write ``Q^-_k\|Ω⟩ = √(Z_ρ)\|k⟩`` — four
backslashes, applied to the merge text before the commit; and withdraw the
"all four rows 6-column" claim or restate it as "six *semantic* columns; two
rows need pipe escaping".

**(d) SURVIVING WEAKER STATEMENT.**  *The row contents, statuses, depends-on
sets and quantifiers are all correct and are unaffected — I read them field by
field.  What does not survive is the claim that the four rows were checked
for column structure, and the assumption that a reader's renderer will show
`PROVED` and `CONJECTURE` where the source says so.*

---

**m2.  Merged clause 2 states `‖Q^-_q|h⟩‖² = Z_ρN − 2` with no restriction on
`q`, and the round's OWN proof step states the hypothesis `q ≠ h`.  The
identity is false at `q = h` by a factor of two.**

**(a) Location.**  r5 §5.2″ clause **2**, sentence 3 ("*since `‖Q^-_q|h⟩‖² =
Z_ρN − 2` exactly ((b)(i); named computation D24N-C8(ii))*"), against r5
`§1.1⟨2⟩1` ("*at even `N`, for **`q ≠ h`** commensurate*") and against the
checker's own docstring ("*for q != h commensurate*").  The same omission is
in `(b)(i)`, which is r4 text I ruled MERGE — I flag it there but do not
reopen it.

**(b) My computation.**  Redoing the pair sum with `q = h`, the coefficient of
the unordered pair `{a,b}` is `t(e^{iha}+e^{ihb})` doubled in phase, giving
`Σ_{a<b}|·|² = 2N(N−1)` instead of `N²−2N`, hence `‖Q^-_h|h⟩‖² = 2Z_ρN − 2`.
ED confirms: `2S=4, N=8` gives **`62.000000`**, not `30`; `2S=2, N=6` gives
`22`, not `10`; `2S=3, N=8` gives `46`, not `22`.  The gate D24N-C8(ii) tests
only `(hard,soft) = (1,3)` and `(1,2)`, i.e. only `q ≠ h`, so the citation
again does not deliver the sentence's quantifier — the M1 pattern, one level
down.  (I also checked that "*at even `N`*" is an unnecessary restriction: the
identity holds at `N = 7, 9` too, so the merge text's silence on parity is
correct and only the `q` hypothesis is missing.)

**(c) FIX DEMAND.**  Two words in clause 2: "*since `‖Q^-_q|h⟩‖² = Z_ρN − 2`
exactly **for `q ≠ h`***", and the same two words in `(b)(i)` while the block
is open.

**(d) SURVIVING WEAKER STATEMENT.**  *Every use the definition makes is
inside the proved range: clause 2's leg is `Q_0|h⟩`, and the class fixes
`h ∈ I ⋐ (0,π)`, so `q = 0 ≠ h` always.  The conclusion "the descendant leg
carries `√(Z_ρ − 2/N)`", the LSZ scope, the DISPLAY, the AMP fence and the
refutation margins are all untouched.  What does not survive is an L4 single
source asserting an identity at a strength its own proof step and its own
named computation both decline to give it.*

---

**m3.  `check_defect`'s two `require`s are deductively subsumed by C4 and
cannot fire on any input — the exact species the round just deleted at m3 —
while the docstring now asserts "No constant-true `require` remains".**

**(a) Location.**  `theory/checks/d24d3_normalization_check.py`,
`check_defect`, the two `require` calls (`D24N-C5 frozen clause must match at
S=1/2` and `D24N-C5 frozen clause unexpectedly matched at S=…`), against the
module docstring's "*No constant-true ``require`` remains*" and against
`derive_exponent_band`'s "*it is the C5 situation … and like C5 it is demoted
to DISPLAY*".

**(b) My computation.**  `predicted_jet(0.5, None) = 2.0` and `1/0.5 = 2.0`
are the **same number**, so C5's first quantity, `|2 − mean_{S=1/2}|·0.5`, is
the `S = 1/2` term of C4's `worst = max_{spin,rows}|measured − 1/spin|·spin`,
bounded above by it by convexity.  C4 runs first in `main()` and requires
`worst < 0.08`; therefore the first C5 guard always holds.  For the second:
C4 gives `mean_S ∈ (1/S − 0.08/S, 1/S + 0.08/S)`, so
`|2 − mean_S|·S ≥ 2S − 1 − 0.08`, which is `0.92, 1.92, 2.92` at
`S = 1, 1.5, 2` — always `> 0.08`.  Both guards are unfirable.  Empirically:
I built two data mutants designed to trip them (`S=1/2` slope set to `1.5`;
slopes set to the frozen `2` off `S=1/2`) — both die at **C4**; only after I
neutered C4's `require` on a copy did C5 fire, with
`D24N-C5 frozen clause must match at S=1/2, deviation 0.2500` and
`D24N-C5 frozen clause unexpectedly matched at S=1.0`.  C5's exit path is
reachable **only if another gate is removed**.

**(c) FIX DEMAND.**  Delete both `require`s in `check_defect` (its numbers are
already printed and are DISPLAY), or scope the docstring: "*no constant-true
`require` remains outside C5, whose two guards are deductively subsumed by C4
and are retained only as regression checks against code mutation*".

**(d) SURVIVING WEAKER STATEMENT.**  *Nothing is exposed and no number moves:
C5 is declared DISPLAY and subsumed by C4 in the docstring, and its printed
deviations `0.000, 1.002, 2.003, 3.003` are exactly `|2 − 1/S|·S` on the true
data, which I reproduced.  The deletion of r4's `band > 0.0` guard was
correct and is not reopened.  What does not survive is the file's absolute
claim about itself — the sixth-round version of the campaign's standing
defect, now caught inside the sentence that announces its cure.*

---

**m4.  The blanket "every anchor in §5 is a quoted string, verified unique" is
false in four places — and two of them are edits this commit applies.**

**(a) Location.**  r5 §5, anchoring policy ("*Every string below was verified
**unique** in its target file this round*") and §4.1 ("*Anchor uniqueness was
re-verified live for every string in §5*"), against: §5.5″ **item 13**
(anchor ``𝖲(k_s) = 2ik_s``); §5.5″ **item 8** (anchor ``**Frozen 𝒮_W empty
for``); §5.5″ **item 12**, ML4 half ("*after the ML4-admissible-amputation
sentence*"); and §4.3 rows **11** and **12**.

**(b) My computation.**  Literal string search at the live file state:
* ``𝖲(k_s) = 2ik_s`` occurs **twice** in `theory/TRIANGLE.md`, at `:217` (the
  SCOPE block item 13 targets) and at `:249` ("*At `n = 1` in M1 … by §2.3*").
  Item 13's prose disambiguates by naming the **SKETCH** label, so the
  intended site is recoverable, but the quoted anchor alone is not unique.
* Item 8 says the `HANDOFF.md` line "*becomes*" a replacement text but supplies
  **only a start anchor and no end anchor** — the only replacement in the whole
  recipe without one.  The corpus-damage item actually spans `:40–42`
  ("*(3) **Frozen 𝒮_W empty for / ρ≠1/2** (D24(d)3+ML5-B force slope 2 at
  every ρ vs PROVED 1/S) — / tns-iu5, blocks any D29/D30 merge.*").  Applied
  to the matched line alone it leaves "*(D24(d)3+ML5-B force slope 2 at every
  ρ vs PROVED 1/S)*" standing — the retired claim, unretired.
* Item 12's ML4 half is anchored by a **description**, not a quoted string.
* §4.3 row 11's anchor ``for every O∈`` and row 12's ``PROVED.** Every O∈``
  **do not occur at all**: the live text is ``for every `O∈𝒮_W`.`` (`:141`)
  and ``**PROVED.** Every `O∈𝒮_W` obeys`` (`:152`) — the backtick is inside.
  A literal match fails.  (These two rows are "LICENSED bare", i.e. no edit is
  applied there, so nothing breaks; the *verification claim* is what fails.)

**(c) FIX DEMAND.**  Four substitutions, all verified unique by me at the live
state: item 13 → ``conditional on wave operators (ML1) and the amputation
convention`` (`:218`) or ``` `𝖲(k_s) = 2ik_s` and `‖R_{S2}(k_s,·)‖_{L²(I)}```
(`:217`); item 8 → add the end anchor ``tns-iu5, blocks any D29/D30 merge.``
and say the whole of item (3) is replaced; item 12's ML4 half → quote
``An **ML4-admissible analytic amputation at fixed `N`** may multiply (3)``;
§4.3 rows 11–12 → ``for every `O∈𝒮_W`.`` and ``**PROVED.** Every `O∈𝒮_W`
obeys``.  Then restate the policy sentence as "*every anchor that an
application step uses is a quoted string, verified unique*".

**(d) SURVIVING WEAKER STATEMENT.**  *The thirteen anchors that the L4/L5
merge actually uses ARE quoted strings and ARE unique — I asserted every one
of them at the moment of use and the application ran 13/13 in one pass (Z11).
The anchoring policy is the right durable fix and it demonstrably works where
it was applied.  What does not survive is the word "every": three same-commit
obligations and two rows of the disposition table were not put through the
uniqueness check the section says was run on all of them.*

---

**m5.  §4.3's closing parenthetical mis-names one of the two extra bare-`𝒮_W`
sites and then licenses both by a clause that does not enumerate them — the
same defect m2 of r4 found for `HANDOFF.md`, two sites on.**

**(a) Location.**  r5 §4.3, the note after the nineteen-site table: "*Two
further bare uses sit in `theory/ansatz-scattering-2m-r4-response.md` and
`theory/verdicts/ansatz-scattering-2m-r5.md`: verdict records are frozen
historical documents … and the licensing clause covers the form they use.*"

**(b) My computation.**  Whole-repo grep: the two sites m2 of r4 named are
`theory/ansatz-scattering-2m-r4-response.md:99` and
`theory/ansatz-scattering-2m-r5-**response**.md:227` — the second is a lane
*response* document in `theory/`, not the verdict
`theory/verdicts/ansatz-scattering-2m-r5.md`.  The error is invisible to a
spot-check because the misnamed file **also** contains a bare `𝒮_W`
(`:529`), as do `ansatz-scattering-2m-r4.md:519` and `-r6.md:528`.  And the
licensing clause as merged reads "*Written bare `𝒮_W` where the density is
fixed or immaterial — the D24 section header, D25, the CLAIMS rows …,
`ml5-universality.md`, `HANDOFF.md`, and the Letter*": a closed enumeration
that names neither file.  On the clause's own reading — which is exactly the
reading I applied to `HANDOFF.md` at r4, and which the lane accepted — those
two sites are **not** covered.

**(c) FIX DEMAND.**  Correct the path to
`theory/ansatz-scattering-2m-r5-response.md`, and replace "*the licensing
clause covers the form they use*" with the true reason: "*frozen lane records
— verdicts and `*-response` documents — are outside the registry's scope and
are never renamed*"; optionally add that half-clause to §5.4b″ so the rule is
stated where it is enforced.

**(d) SURVIVING WEAKER STATEMENT.**  *The disposition is right — those two
files are frozen records, no edit is owed on either, and the nineteen-site
enumeration of live corpus files is complete and correct (I re-grepped it).
What does not survive is the stated justification, which repeats the
enumerated-clause error one round after it was fixed, and one address in the
section whose subject is addresses.*

---

## 5. NOTE

**n1.  Line counts are `split("\n")` counts, one more than `wc -l`.**  The
lane reports `1349 / 313 / 146`; `wc -l` on its own scratch output (and on
mine, which is byte-identical) gives `1348 / 312 / 145`.  Likewise the
checker: r5 §6 says "**795 loc**", the repair response says "794 loc",
`wc -l` says `794`.  Nothing is wrong with the artefacts; recorded so the
orchestrator does not read a correct application as a failed one, and so the
two documents of one round stop disagreeing by one.

**n2.  "…and the refutation needs neither" (merged `AMP` row) has no clear
antecedent.**  The same sentence says the refutation *is* quoted at the
pre-registered `0.08`, so "neither band" reads as a contradiction; the
intended sense — that the margins are large enough that the choice of band is
immaterial — is the one §6.3 states.  One word ("*needs neither of them to be
tight*") would settle it.

**n3.  The isolated C2(v) error is printed only on the GREEN path.**  Under
`--red-ladder` the process dies inside `check_order_parameter_residue` before
any `print`, so the new reporting makes (v)'s *margin* visible, not its exit
path.  §6.4 and the docstring both say this honestly.  Recorded so a later
round does not read m5 as having been closed by a red-mode disclosure.

**n4.  C6 part 2's symbolic pin is input-independent.**  `sp.solve` on a
hard-coded `(2s)^p = 2s` cannot fail on any data; it fails only under code
mutation, which I confirmed (`roots [1/2], not [1]`).  Calling it "*the gated
content of C6 part 2*" is true against code mutation and not against data —
worth one clause, given that C6 part 1 is the only data-sensitive gate there.

**n5.  `(α)`'s definition now has two homes.**  It is defined in the
`D24-VAL` row (an L5 file) and glossed in `definitions.md` clause 3b (an L4
file).  The gloss carries a pointer to the row, so authority is unambiguous
and I rule it MERGE; but the L4-clean direction is the reverse one — put the
bridge's statement in `definitions.md` and have the row cite it.  A ticket,
not a blocker.

**n6.  `TRIANGLE.md:249` carries a second `𝖲(k_s) = 2ik_s` display** that
item 13's scoping edit does not reach.  It attributes the value to §2.3, i.e.
the contact route, which is precisely what the merged clause says the corpus's
`2` rests on — so **no edit is owed there**.  Recorded so a future round does
not "discover" it as an omission.

---

## 6. Register comparison

Nearest PROVED row: **`S2-2body-S`**, whose adjudicated scoping sentence is
the corpus standard — *"PROVED per spin-s-r1.md adjudication: proves the
unit-charge exact two-body slope only; it does not prove endpoint or
equal-velocity limits, spin-`S` Bethe completeness, S-general, the memory
half, the `|q_hard|>1` factor, or Conjecture Bc."*  Say exactly what is
proved, then enumerate by name what is not.

r5's own register paragraph does that, and I checked each conjunct against
the merged bytes rather than the prose: *"NOTHING promoted, no member
exhibited, no value installed, no status changed, no new gate, no new symbol;
`ML1`, AMP, `(α)` and nonemptiness all still open and all still named at
every point of use."*  All true — and after M2, true at **two more points of
use** than before.  H10's disclosure ("*the merge no longer ships the sentence
`Z_ρ^{-1/2}` is refuted without hypotheses anywhere*") is a weakening the
round volunteers against its own headline, which is the right register.

| Layer | What it says | Strength |
|---|---|---|
| §1.1–§1.3 | leg ratio `√(Z_ρ − 2/N)`, exact `√Z_ρ` only in the LSZ limit | **verified three ways (Z2)** |
| §5.2″ clause 2 | same, with `((b)(i); D24N-C8(ii))` | **citation and cited sentence now agree**; quantifier `q ≠ h` dropped (m2) |
| §5.2″ clause 3b / `AMP` row | `Z_ρ^{-1/2}` refuted **under (α) and the cc reading** | **exactly the demanded strength** |
| §5.3a′/§5.3b′ | where-proved → r4 §0.2, r5 §0.2, r5 §5 | **correct; the durable part is the recorded rule, not the pointer** |
| §6.1–§6.4 | DISPLAY recomputed; guard deleted; blind spot declared; (v) isolated | **all four reproduced exactly (Z3, Z6, Z9, Z10)** |
| §6 docstring | "no constant-true `require` remains" | **overstates — C5's two guards (m3)** |
| §5 anchoring policy | "every string verified unique" | **overstates in four places (m4)** |

**Reliance audit: clean** (Z16).

---

## 7. MERGE / HOLD, clause by clause — and the GO

| § | Clause | Decision | Note |
|---|---|---|---|
| **5.0″** | D24(b), the two-anchor convention | **MERGE** | M1's LSZ scope in `(b)(ii)` landed; m7/m8's two prose repairs are algebraically right (Z19); exactly two hunks against r4 (Z13). |
| 5.1 | D24(c) (r3 verbatim) | **MERGE** | Applies at the exact anchors; see n2 of r4 (bare `𝔞_leg`), not reopened. |
| **5.2″** | D24(d) preamble | **MERGE** | Five-condition count preserved and `main.tex:244` still reads it (Z15). |
| 5.2″ | clause 1 | **MERGE** | Unchanged; genuinely homogeneous. |
| **5.2″** | clause **2** | **MERGE with m2** | M1 fixed, n1 ("consistent") fixed, m6's selection-by-consequence clause added and correct. Owed: the two words `for q ≠ h`. |
| 5.2″ | clause **3a** | **MERGE** | Unchanged. |
| **5.2″** | clause **3b** | **MERGE** | M2 fixed; `(α)` labelled at first appearance, verified in the merged bytes. |
| 5.2″ | clauses 4, 5, closing ¶ | **MERGE** | Unchanged. |
| **5.3a′** | `ML5-B` row | **MERGE** | M3 append present and accurate against r4 §0.2. |
| **5.3b′** | `D24-VAL` row | **MERGE with m1** | M3 append present; owed: escape two `\|`. |
| **5.3c″** | `AMP` row | **MERGE with m1, n2** | M2's two hypotheses and n3's corrected attribution both present; owed: escape two `\|`. |
| 5.3d | `ML5-A` row (r3 verbatim) | **MERGE** | No append owed (Z18). |
| 5.4a′ | four new rows | **MERGE** | Byte-identical to r4's (Z13); no duplicate registry key (Z12). |
| **5.4b″** | `𝒮_W(ρ)` row + licence | **MERGE** | `HANDOFF.md` added as the nineteenth site (Z14); see m5 for the frozen-record carve-out. |
| 5.4c / 5.4d / 5.4f | `𝖲` row, rule 2, rule 13 | **MERGE** | Applied cleanly; rules 1–13 contiguous, blank line preserved (Z12). |
| 5.4e′ | rule 8 amendment | **MERGE** | Fenced text r3 verbatim; the rationale's `:170` is live and string-quoted. |
| **5.5″** | ADVISORY items 1–14 | **MERGE, NOT optional, with m4** | Items 1–7, 9–11, 14 verified live; **items 8, 12(ML4 half) and 13 need m4's anchors before application.** |
| — | checker | **DO NOT APPLY — already in `HEAD`** | §8. |

### GO / NO-GO

**GO.**  The five MINORs are quotable one-line edits to the merge text and to
two anchors; none of them changes a conclusion, a status, a quantifier of any
claim, or the structure of the application, and I have applied the thirteen
edits against the current files myself with every anchor asserted.  I do not
ask for another round.

### The exact ordered recipe (verified by application against `8a92310`)

0. **Patch the merge text first** (five one-line edits, no round required):
   m1's four `\|` escapes in §5.3b′/§5.3c″; m2's `for q ≠ h` in §5.2″
   clause 2 (and, while the block is open, in §5.0″ `(b)(i)`); m4's four
   anchor substitutions in §5.5″ items 8, 12, 13 and §4.3 rows 11–12; m5's
   path correction and reason in §4.3; n2's one word in §5.3c″.
1. **`definitions.md`, three REPLACEs, descending, by string anchor:**
   (a) ``**(d) The Ward-covariant no-contact class`` → ``is part of the ML5-B
   future work.`` ← r5 §5.2″;
   (b) ``**(c) The contact first jet.**`` → ``factorisation with the same
   stated norm control.`` ← **r3 §5.1** verbatim;
   (c) ``**(b) Amputated amplitudes.**`` → ``waves are generalised kernels
   inside `C_c^∞` packets (D3(a), D12(a′)).`` ← r5 §5.0″.
2. **`notation.md`, six edits, in the order `b″ → a′ → c → f → e → d`:**
   REPLACE the ``| `𝒮_W` | the five-condition`` row ← §5.4b″ → ADD the four
   rows after it ← §5.4a′ → replace the substring ``on the D24(d) class
   `𝒮_W`;`` ← §5.4c → INSERT rule 13 after ``    tensor (`TRIV₂`); no other
   reading of `T` takes that position.`` ← **r3 §5.4f** → APPEND to rule 8
   after ``   `→E_C`, or `E_C⊗E_C^*` (D19, D21).`` ← §5.4e′ → APPEND to
   rule 2 after ``   `χ` as a sign into any other shard.`` ← **r3 §5.4d**.
3. **`claims/CLAIMS.md`, four edits, matched on ROW LABEL:** REPLACE
   `| ML5-B |` ← §5.3a′ → ADD `| D24-VAL |` after it ← §5.3b′ → ADD
   `| AMP |` after that ← §5.3c″ → REPLACE `| ML5-A |` ← **r3 §5.3d**.
   Expected result: `1348 / 312 / 145` by `wc -l`.
4. **The fourteen §5.5″ obligations, same commit**, with m4's anchors for
   items 8, 12 and 13.
5. **Do NOT touch `theory/checks/d24d3_normalization_check.py`** — §8.
6. **Expect the commit to sweep.**  The beads pre-commit hook has swept
   unrelated lanes into three of the last four commits (`5349ee5` took this
   very checker; `286f8d3` took the whole LR-D16 lane).  The tree was clean
   at the moment I finished, but if another lane is mid-edit when you commit,
   say so in the commit message as `5349ee5` did, or wait for that lane.

---

## 8. Is the "checker is already in `HEAD`" claim correct?  **YES.**

Verified three ways, and the lane is right that it must **not** be
re-applied:

1. `git diff HEAD -- theory/checks/d24d3_normalization_check.py` is **empty**
   — the worktree copy and `HEAD`'s copy are byte-identical.
2. `git log -1 -- <checker>` names **`5349ee5`** ("ACE-LD r3 …"), whose own
   commit message carries the note "*commits here sweep beyond staged paths
   via the beads pre-commit hook*", and whose diffstat lists this checker
   (`117 ++++++----`) alongside two ACE-LD files.
3. `git diff a979177 HEAD -- <checker>` is `+92/−25` and contains **exactly**
   the four r5 changes and nothing else: the two-scope C3 DISPLAY with the
   measured leg ratio (M1), the deleted `require(band > 0.0)` with its reason
   (m3), the declared uniform-inflation blind spot (m4), and the isolated
   C2(v) reporting (m5).  Running `HEAD`'s copy reproduces r5 §6.5's fenced
   banner byte-for-byte (Z4) and all seven red exit paths (Z5).

So **only the three shared-file edits plus the §5.5″ obligations are owed.**
Re-applying the checker half would double-apply; skipping the shared-file half
would drop the merge.  One further point in the lane's favour that it did not
claim: `5349ee5` committed a checker whose docstring cites
`theory/verdicts/d24d3-adjudication-r5.md`, which was untracked at the time —
`286f8d3` has since committed that file, so the dangling reference is already
resolved and needs no action in this commit.

---

## 9. `𝒮_W(ρ)` nonemptiness, `tns-axg`, `tns-v44`, `tns-iu5`

**`𝒮_W(ρ)` nonemptiness remains OPEN at every `ρ`, `ρ = 1/2` included**, and
open rather than provably empty.  I re-checked for a residual emptiness
argument in the merged text and there is none: clause 2 constrains the source,
not the convention, and the m6 parenthesis states the alternative reading's
emptiness as a *reason for the choice*, correctly qualified by "*by an
`O`-independent factor*" — which is what makes it a statement about the
convention and not about any `O`.

* **bd `tns-axg`: stays OPEN and MAY NOT move.**  Nothing here exhibits a
  member.
* **bd `tns-v44`: unblocked on this axis.**  §5.5″ item 7's riders stand and
  are now enforced by displayed text in the definition itself.
* **bd `tns-iu5`: MAY NOT CLOSE.  Two of four sub-tasks remain.**
  1. *(DONE, r3+r4)* D24(b)'s amputation and soft-leg convention, scoped to
     the register where its kernel is constructed.
  2. **(CLOSES WITH THIS COMMIT)** clause (d)2's residue normalisation fixed
     in displayed text, clauses 1–3 made consistent with it, and the
     LSZ/finite-`N` scope of the conversion displayed and gated (D24N-C8(ii)).
     The r4 wording holds (M1, M2) are discharged; only m2's two words remain
     and they are part of this commit.
  3. **(OPEN — this is `ML1`)** supply, or scope away, the `δ`-normalised
     asymptotic one-magnon kernel off the fully polarised spin-`S` family.
  4. **(OPEN — the prover target)** prove or refute **AMP**, with the fence as
     now worded: leg conversion supplies exactly `Z_ρ^{-1/2}` in the LSZ
     limit, on the charge-created reading of `E^O_desc`, so a second,
     non-leg-normalisation factor of the same size is required.  `D24-VAL`
     stays vacuous-or-unknown until (4) closes or `tns-axg` exhibits a member.

  Carry forward in the issue **the rule, not the pointer** (M3): *a row marked
  "verbatim" is verbatim in its statement; its navigation columns must be
  re-checked against the current supersession table every round.*

---

**PASS**

*Trajectory `3/7/6/4 → 1/5/8/5 → 1/5/8/4 → 0/3/8/5 → 0/0/5/6`.  The physics is
unchanged for the fifth consecutive round and is now fenced at every layer
that ships: the leg-conversion identity is exact on the vacuum leg, correctly
scoped on the descendant leg, gated on both, and displayed in both scopes; the
two refutations are exact at the pre-registered band and now carry their two
hypotheses into the L4 file and the DAG row; and the corpus's `2` rests on the
contact route.  What most deserves recording is the method, not the result:
the lane wrote a from-scratch probe that failed against its own previous
checker and passed against the new one, and it caught, live, that the
correction I had handed it was already stale — which converted "fix four
addresses" into "stop addressing by line".  That is the loop working upstream
instead of downstream, and it is why this round is the one that clears.*
