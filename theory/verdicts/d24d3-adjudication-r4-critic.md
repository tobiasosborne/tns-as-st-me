<!-- ROLE: ADVERSARIAL CRITIC verdict, round 4 (MERGE CLEARANCE), on
     theory/verdicts/d24d3-adjudication-r4.md (1127 loc),
     theory/verdicts/d24d3-repair-r4-response.md and
     theory/checks/d24d3_normalization_check.py (727 loc, rewritten),
     per briefs/critic-protocol.md + briefs/d24d3-critic-r4.md.
     Priors: -r1-critic (3F/7M/6m/4n), -r2-critic (1/5/8/5),
     -r3-critic (1/5/8/4).  WRITABLE FILE OF THIS LANE: this file only.
     definitions.md, notation.md, claims/CLAIMS.md, the artifact and its
     checker were NOT edited; no git commit.  Everything below was
     recomputed from scratch; the X1-X15 / W* / V* fences are not churned. -->

# r4 critic verdict — D24(d)3 adjudication, the merge-clearance round

**Headline.  The FATAL is gone and it is gone for the right reason.  The lane
took my own FIX DEMAND, promoted the mixed reading to an explicit two-anchor
convention, and paid the three costs in the merge text and not only in prose:
I diffed §5.2′ against r3 §5.2 line by line (the "every other line is
byte-identical" claim is exactly true), and the struck preamble, the shrunken
invariance list and the one-step re-derivation of `Z_ρ^{-1/2}` are all in the
text that would ship.  The two-anchor convention is **well posed** — I worked
the covariance algebra through with the hard-leg factor carried explicitly and
it closes: clause 2 is a membership condition on the source, not a second
covariance anchor, and it does not over- or under-determine `𝔞_leg`.  Both
standing checker complaints are genuinely discharged: the derived exponent
band's **subsumption proof is correct** (I re-derived the inequality chain),
so the demotion to DISPLAY is the right disposition and not a dodge; and the
`0 ≡ 0` orthogonality gate's replacement is **not** a new no-op — I derived
`⟨(Q_{k})²Ω,(Q_{k+π})²Ω⟩ = −2N·Z_ρ` on paper and then confirmed it by an
independent full-Hilbert-space Kronecker ED at `2S = 1,2,3,4`, `N = 4,6,8`.
The whole merge applies to scratch copies in the supplied order with every
stated anchor holding.**

**What still blocks the commit is three sentence-level defects, all of which
would be installed into an L4 or L5 file by this commit.**  (i) The round
repaired the vacuum-leg/descendant-leg confusion (m1) in `§1.3⟨3⟩1` and in
`(b)(i)` — and then reinstalled it in the two places it newly wrote: merged
clause 2 says the two legs "differ by **exactly** `√Z_ρ`" and cites `(b)(i)`,
the sentence that says they do not at finite `N`; and the new C3 DISPLAY line
prints `2.828427` as "the (b)-asymptotic residue" at `N = 8`, where the true
value against a `δ`-normalised descendant leg is `2.9212` (3.28 % out).
(ii) The AMP fence in merged clause 3b and in the new `AMP` DAG row states the
refutation of `Z_ρ^{-1/2}` **unconditionally**, three sentences after the same
paragraph names the jet-identification bridge for the frozen refutation, and
while `§1.3⟨3⟩3` and the `D24-VAL` row both say the refutation dies without
(α).  (iii) `ML5-B` and `D24-VAL` keep where-proved columns pointing only at
r3 — a document whose §5 merge text, invariance list and headline checker
claims r4 supersedes — which is verbatim the defect r2-critic M4 forced fixing
for `corpus-r2.md`.

**Trajectory.  r1 `3/7/6/4` → r2 `1/5/8/5` → r3 `1/5/8/4` → r4 `0/3/8/5`.**
First round with no FATAL.  Every one of the r3 items is genuinely fixed by
fresh recomputation; the three MAJORs are new, they are all repairs that
stopped one span short, and each is one or two sentences.

**Final line at the bottom.**

---

## 0.  What I did

Read `CLAUDE.md`, `definitions.md` D24 in full, `notation.md`,
`claims/CLAIMS.md`, the r1/r2/r3 critic verdicts, the r4 artifact and response
in full, the checker line by line.  Then, independently:

* re-derived the two-magnon closed form on paper and verified it by a
  from-scratch full-Hilbert-space Kronecker ED (no repo import) at
  `2S = 1,2,3,4`, `N = 4,6,8`;
* re-derived `‖Q^-_q|h⟩‖² = Z_ρN − 2` analytically
  (`2S(N−2) + 2(2S−1)`) and by sparse ED at `N = 6,8`;
* recomputed the Ward residue in **both** normalisations by independent sparse
  ED at `N = 6`, `2S = 1,2,3,4`;
* re-derived the exponent-band subsumption inequality chain symbolically and
  numerically;
* ran the checker green plus **all seven** red modes under `python3 -O`,
  recording exit paths; built 16 data mutants and 6 code mutants on copies,
  including two the lane did not build (`errscale`, `errscale+shift`);
* worked the `(c, c′)` covariance algebra through the (3a) quotient with the
  hard-leg amputation factor carried explicitly;
* **applied all thirteen merge edits to scratch copies** of `definitions.md`,
  `notation.md` and `claims/CLAIMS.md`, asserting every stated anchor at
  every step, in the r4 order;
* re-grepped the whole repo for `𝒮_W`, `E_O`, `D24(b)` and `D24(d)`, and
  re-verified every same-commit anchor named in §5.5′ and r3 §4.2 against the
  live files.

---

## 1.  VERIFIED CORRECT this round — fence this, do not churn it

The r1 `V*`, r2 `W*` and r3 `X*` fences stand and were not re-derived except
where noted.  New fences `Y1–Y12`.

**Y1.  Green is green and the banner is byte-identical.**  `python3 -O`,
exit `0`.  I extracted the fenced banner from r4 §6.5 and diffed it against
live stdout: **IDENTICAL**, character for character, all thirteen lines.

**Y2.  All seven red modes fire at the stated gate, with the stated first
stderr token and the stated numbers.**  Exit paths recomputed:

| mode | exit | gate | message |
|---|---|---|---|
| `--red-frozen` | 1 | **C6** | `dev=1.0016; 2.0027; 3.0033` |
| `--red-power` | 1 | **C6** | `dev=0.4984; 0.6640; 0.7467` |
| `--red-halfpower` | 1 | **C6** | `dev=0.4158; 0.7347; 1.0033` |
| `--red-ward` | 1 | **C3** | `1.697e+01` |
| `--red-ladder` | 1 | **C2** | `1.477e+06` |
| `--red-legfactor` | 1 | **C8** | `5.657e+00` |
| `--red-descnorm` | 1 | **C8** | `2.000e+00` |

The three candidate-value modes reach and die at the **acceptance test
itself**, not at an earlier guard — the pathology the standing obligations
warn about is absent.

**Y3.  The two-magnon replacement gate is REAL, and its closed form is
right.**  Derived independently on paper: with `t := 2S`,
`⟨(Q_{k_1})²Ω,(Q_{k_2})²Ω⟩ = 4t²Σ_{x<y}(−1)^{x+y} + 2t(t−1)Σ_x 1
= 4t²(−N/2) + 2Nt(t−1) = −2Nt = −2N·Z_ρ`, using `‖S^-_xS^-_yΩ‖² = t²`
(`x ≠ y`), `‖(S^-_x)²Ω‖² = 2t(t−1)` and `Σ_{x<y}(−1)^{x+y} = −N/2` for even
`N`.  Then verified by **independent full-Hilbert-space Kronecker ED** (no
repo import), `2S = 1,2,3,4`, `N = 4,6,8`: max error `8.85e-14`, exact
integers `−8, −12, −16, −16, −24, −32, −24, −36, −32, −48`.  **It is not a
no-op**: I isolated the sub-gate and ran it with the mutated ladder — its own
error is `2.44e+03` (at `2S = 2`, `N = 6` the mutated overlap is exactly
`+280.560` against predicted `−24`, reproducing §6.2's number), and the
predicted side is a ladder-free integer with no shared subexpression.
`c4_overlapsign` dies at C2 with `1.280e+02`, reproduced.  The momentum-pairing
argument is also right: `k` and `k+π` share total momentum `2k (mod 2π)`, and
any distinct-total-momentum pairing is zero by translation invariance — the
r3 no-op — exactly as the code comment says.

**Y4.  The subsumption proof is CORRECT, and the demotion to DISPLAY is the
right disposition.**  I re-derived it.  With `x_s := log(2S_s) > 0` on the fit
spins and `y_s := log(2/mean_s)`, lstsq gives
`p − 1 = Σx_s(y_s − x_s)/Σx_s² = −Σx_s log(mean_s·s)/Σx_s²`.  Acceptance
part 1 at the candidate exponent `1` is exactly `|1 − mean_s·s| ≤ b`, so
`mean_s·s ∈ [1−b, 1+b]`, so `|log(mean_s·s)| ≤ log(1/(1−b))` (since
`log(1+b) ≤ −log(1−b)`), so
`|p − 1| ≤ [Σx_s/Σx_s²]·log(1/(1−b))` — the derived band, exactly.  **A
`require` on the fitted exponent can therefore never fire on data that reaches
it.**  Numbers reproduced: `Σlog = 3.178054`, `Σlog² = 3.609214`, ratio
`0.880539`, `log(1/(1−0.047854)) = 0.049040`, band `0.043221 → 0.0432`.  The
lane's remark that my own `≈0.042` used `log(1+b)` is correct (`0.0412`).
This is a finding the lane made **on its own artifact**, against its own
interest, and it is right.  It also correctly notes r3's `0.03` did
independent work only because it was miscalibrated.

**Y5.  The descendant-leg gate is correct.**  `‖Q^-_q|h⟩‖² = Z_ρN − 2` derived
analytically — pair part `2S(N−2)` (using `Σ_{x≠y}e^{i(q−h)(x−y)} = −N`) plus
double-occupancy part `2(2S−1)` — and confirmed by independent sparse ED at
`2S = 1,2,3,4`, `N = 6,8`: `4, 6, 10, 14, 16, 22, 22, 30`, exact.
`--red-descnorm` is off by exactly `2.000`, as advertised.  X15 is now
correctly promoted into the certificate.

**Y6.  The M2 repair does what it says on the data.**  All fourteen data
mutants reproduced on copies: `m_shift30` **passes** (X13 preserved),
`m_shift34` **passes** (r3 rejected it), `m_shift40` **passes** (r3 rejected
it), `m_shift45` dies at acceptance with `S=2.0 dev=0.0482` — my own boundary
number — `m2b_shift60` dies at acceptance, `m_shift799` dies at C4 `0.0839`,
`m8_errinflate` dies at the subsumption guard `0.1914`, `m7_noerror` /
`m9_errzero` / `m3_bandmoved` / `m4_noband` / `m1_slope` die at their stated
guards.  **`m_errwide` and `m_errwide_shift60` — the two mutants that exposed
the load-bearing constant in r3 — now die at the new guard with
`worst row band 0.0790 is 3.78x the median row band 0.0209`.**  r2-critic
M3(b)(iii) is now genuinely closed, not relocated.

**Y7.  The one stated deviation (m2) is JUSTIFIED; I rule for the lane.**  I
checked both halves of its reason by computation.  (i) Per-spin banding *does*
reverse X13: the `S = 1` band is `max(0.0241,0.0044,0.0234)·1 = 0.02413`,
while the `−3 %` mutant's `S = 1` deviation is `|1 − 0.97·0.99840| = 0.03155
> 0.02413`, so `m6_shift30` would die — un-fixing a fix r2-critic M3(b)(iii)
demanded, r3 shipped and X13 certified.  (ii) A `2×` cap *does* reject the
shipped data: the twelve row bands are
`0.032025, 0.007440, 0.005210, 0.024125, 0.004397, 0.023443, 0.021531,
0.006322, 0.038772, 0.020249, 0.007371, 0.047854`, median `0.020890`, worst
ratio **`2.2907×`**.  `ROW_BAND_SANITY = 3.0` is a pure rejector (it appears
only in a `require`) and is declared.  **My r3 m2 fix suggestion was the wrong
trade and the lane is right to have refused it with the reason recorded.**

**Y8.  The residue in both normalisations, recomputed independently.**  Sparse
ED at `N = 6`, `2S = 1,2,3,4`, two hard momenta, current built from the raw
bond matrix: `⟨h|Q_0^†J^-_0|h⟩ = 2i·Z_ρ·J\sin h` exactly (`1.732051i`,
`3.464102i`, `5.196152i`, `6.928203i`), and against `Q_0|h⟩/√Z_ρ` it is
`2i√Z_ρ J\sin h`.  `‖Q_0|h⟩‖² = Z_ρN − 2` at every point.  My r3 F1(b)(i)
table reproduces at a different ring size, so the lane's adoption of it rests
on a fact and not on my arithmetic.

**Y9.  The whole merge applies, in one pass, in the supplied order.**  I
extracted all thirteen blocks programmatically and applied them to scratch
copies with an `assert` on every stated anchor: three `definitions.md`
REPLACEs in descending order (952–973, 931–950, 923–929), the six
`notation.md` edits in the **r4 order b′ → a′ → c → f → e → d**, and the four
`claims/CLAIMS.md` edits in the r4 order (5.3a, 5.3b, 5.3c′, 5.3d).  Every
assertion passed; no overlap, no drift, no hand-patching.  **The r4 ordering
is correct and it is the fix m3 asked for**: b′/a′ at 258 leave 244 and below
untouched; c at 244 leaves 145 and below untouched; f after 145 leaves 130 and
below untouched; e at 123–130 leaves 98 and below untouched; d last.  Result
lengths `1329 / 312 / 144`; the merged D24(b)–(d) block reads coherently
through D24(e), overload rules 2/8/13 read coherently, and the blank line
before `All other symbols are unique.` is preserved.

**Y10.  Anchors re-verified at the LIVE file state** (md5 `ea1ca49e…` /
`9cdac61d…` / `2f579f64…`): `definitions.md` 916, 923, 929, 931, 950, 952,
973, 1004; `notation.md` `𝖲` = 244, `𝒮_W` = 258, rule 2 = 91–98, rule 8 =
123–130, rule 9 = 131–134, rule 12 = 143–145, `All other symbols are unique.`
= 147, closing defect rule = 149–150; `claims/CLAIMS.md` ML5-A = 40,
ML5-B = 41.  X5 and X6 hold unchanged.

**Y11.  Every same-commit anchor outside the three L4/L5 files still resolves,
with one exception (m1 below).**  Verified live: `ml5-universality.md`
142–144, 155, 158, 170–172, 183–184, 324–327; `TRIANGLE.md` 24, 215, 254, 257,
528 and the SCOPE block 212–219 (`𝖲(k_s) = 2ik_s` at 217, the **SKETCH**
label at 218); `main.tex` 244–252, 515–520, 524–527; `corpus-r2.md` 174–178;
`soft-index.md` 161–162; `soft-index-b.md` 757–758, 808;
`soft-index-r1.md:170`; `ml4-ward-reduction.md` 63–68 (the ML4-admissible
sentence is verbatim where r4 says it is).

**Y12.  The §5.2′ diff claim is exactly true.**  I diffed the r4 D24(d) block
against r3's: the only changes are the preamble sentence, clause 2's
normalisation statement and both-normalisations parenthesis, clause 3b's
kernel-existence scope, and the AMP-fence gloss with the §1.3 pointer.
Clauses 1, 3a, 4, 5 and the closing paragraph are byte-identical.  Likewise
the covariance algebra: I carried a common hard-leg amputation `η` through the
(3a) quotient and confirmed it cancels **and** that clause 2, read
charge-created, is `η`-invariant provided its residue is the hard-leg-amputated
one — so `𝔞_leg = Z_ρ^{-1/2}` comes out `η`-free.  **The two-anchor convention
does not over- or under-determine anything: clause 2 constrains the source, (b)
fixes `c′(0)/c = 1`, and `𝔞_leg` is pinned once.**

---

## 2.  FATAL

**None.**  The r3 FATAL is discharged.  I record explicitly why, because the
discharge is the round's central claim and it is legitimate, not circular:
X2's fence made the narrowing conditional on the reading *"clause 2's residue
charge-created, `E^O_desc` in (b)'s"*; §1.1 adopts precisely that antecedent as
displayed text in the definition itself; a conditional whose antecedent is
subsequently asserted by an independent act (here, a convention choice recorded
in an L4 file) discharges without circularity, because nothing in the antecedent
was derived from the consequent.  The refused horns are each refused with my own
stated cost quoted, and the refusal of the "normalisation-fixing" horn is
correct: fixing the leg by demanding the residue be `2iv_hM_1` would make
`𝔞_leg = 1` by construction and restore the frozen clause.

---

## 3.  MAJOR

### M1.  The round's own m1 repair stops one span short: merged clause 2 says the two legs differ by **exactly** `√Z_ρ` and cites `(b)(i)` — the sentence that says they do not, on the descendant leg, at finite `N` — and the new C3 DISPLAY line prints the LSZ-limit number as a finite-`N` measurement, wrong by 3.28 %

**(a) Location.**  Merged `§5.2′` clause **2**, sentence 2: "*The two legs
differ by exactly `√Z_ρ` ((b)(i)), and that mismatch is part of what clause
3b's constant records: against (b)'s asymptotic leg the same residue reads
`2i v_h M_1^O(h)/√Z_ρ`*"; against merged `§5.0′` **(b)(i)**: "*on a descendant
(one-hard-magnon) state the same conversion holds per site **only up to
`O(1/(Z_ρN))`** — `‖Q^-_q|h⟩‖² = Z_ρN − 2` exactly (D24N-C8) — becoming
exactly `√Z_ρ` in the LSZ limit*".  Code: `d24d3_normalization_check.py`
`check_ward_residue_scaling`, ll.346–348 (`display_asym = abs(measured) /
np.sqrt(float(two_s))`) and the banner's second line.  Also `§5.0′` **(b)(ii)**
("*contributes **exactly** that conversion mismatch, `Z_ρ^{-1/2}`*").

**(b) My computation.**  Clause 2's leg is `Q_0|h⟩` — the charge acting on a
**one-hard-magnon** state, i.e. precisely the descendant leg, not the vacuum
leg.  I computed both norms by independent ED: `‖Q^-_q|h⟩‖² = Z_ρN − 2` (Y5),
while the `δ`-normalised asymptotic soft leg carries `‖|q⟩‖² = N`.  So the two
legs differ by `√((Z_ρN − 2)/N) = √(Z_ρ − 2/N)`, **not** by `√Z_ρ`, at any
finite `N`.  At the checker's own operating point (`2S = 4`, `N = 8`,
`h = π/4`):

| quantity | value |
|---|---|
| charge-created residue (measured) | `5.656854` |
| **printed** "(b)-asymptotic residue" `= cc/√Z_ρ` | `2.828427` |
| true residue against a `δ`-normalised descendant leg `= cc/√(Z_ρ−2/N)` | **`2.921187`** |
| discrepancy | **`3.28 %`** |

So the DISPLAY line is either (i) a tautology — it divides `cc` by `√Z_ρ` and
prints both, which is what "*deductively C3 / C8*" concedes — or (ii) a claim
about the `(b)` leg, in which case it is 3.28 % wrong at the `N` it is computed
at.  It is labelled as (ii).  Either way, the certificate's own new sub-gate
C8(ii) is the thing that proves the printed number cannot be what its label
says.  And in the L4 file the commit would install two sentences three
paragraphs apart that a reader must reconcile: "*only up to `O(1/(Z_ρN))`*"
and "*exactly `√Z_ρ` ((b)(i))*", the second citing the first.  This is
`m1` — the vacuum-leg/descendant-leg conflation — reinstalled in the two
places r4 newly wrote, after being correctly repaired in `§1.3⟨3⟩1`.

**(c) FIX DEMAND.**  In clause 2 write "*differ by `√Z_ρ` in the LSZ limit
(at finite `N` by `√(Z_ρ − 2/N)`, (b)(i))*", and either compute the DISPLAY's
asymptotic value as `|measured|/√((Z_ρN−2)/N)` or relabel it
"*LSZ-limit (b)-asymptotic value; the finite-`N` leg ratio is
`√(Z_ρ − 2/N)`, C8(ii)*".  One clause and one label.

**(d) SURVIVING WEAKER STATEMENT.**  *In the LSZ / infinite-volume register
where D24(b) amplitudes are defined, the conversion **is** exactly `√Z_ρ`, and
everything the adjudication concludes from it survives untouched: the
one-step derivation of `𝔞_leg^{leg-conv} = Z_ρ^{-1/2}`, the refutation
margins, and the AMP fence.  The finite-`N` correction is `≤ 1/(Z_ρN) ≈ 10^{-2}`
at `N = 60` against `5–12×` margins, exactly as `§1.3⟨3⟩1` says.  What does
not survive is the word "exactly" in a definition that cites, as its
authority, the sentence qualifying it — and the DISPLAY line's label.*

---

### M2.  The AMP fence ships the refutation of `Z_ρ^{-1/2}` **unconditionally** into `definitions.md` and into the `AMP` DAG row, dropping both of its hypotheses — three sentences after the same paragraph names one of them for the frozen stipulation

**(a) Location.**  Merged `§5.2′` clause **3b**: "*Fence on AMP: by (b)(ii) a
leg normalisation alone contributes `Z_ρ^{-1/2}` … **and that value is refuted
against the ansatz-free two-magnon data at the pre-registered band**, so AMP
requires a second factor `Z_ρ^{-1/2}` from a different mechanism*"; and
`§5.3c′`, the `AMP` row: "*a value the ansatz-free data refutes at the
PRE-REGISTERED band (`--red-halfpower`, deviations 0.42/0.73/1.00 vs band
0.08)*".  Against, in the **same clause 3b paragraph**, two sentences earlier:
"*As frozen, this clause stipulated `𝔞_leg = 1`, which **under the corpus's
jet-identification bridge** contradicts PROVED `S2-2body-S`*".  And against
`§1.3⟨3⟩3` ("*conditional on the bridge (α), without which nothing is matched
and nothing is refuted*"), r3 `⟨1⟩4.⟨3⟩4` ("*Without (α), nothing here is
refuted and nothing is matched*"), and the `D24-VAL` row, which carries (α) as
an explicit displayed antecedent and calls it "*not a PROVED row*".

**(b) My computation.**  Quantifier/hypothesis audit, twice.

*(i) The missing (α).*  The data are two-magnon **phase slopes**; `𝔞_leg` is a
**D24 amputation constant**.  The only thing that connects them is the
jet-identification bridge.  Strip (α) and the sentence has no content: the
`0.4158/0.7347/1.0033` deviations are deviations of an ML5-B jet from a
measured phase slope, and without (α) that comparison is not licensed.  The
merged paragraph therefore names the bridge for the refutation it likes
(frozen `𝔞_leg = 1`) and omits it for the refutation it also likes
(`Z_ρ^{-1/2}`), inside one paragraph.  That asymmetry is not defensible in an
L4 single source, and the DAG row repeats it while its sibling row two lines
above is scrupulous about the same hypothesis.

*(ii) The missing charge-created reading of `E^O_desc`.*  I worked the
derivation through.  `L = E^{(b)}_desc/[(e^{ik}−1)·2iv_h·M_1^O]`; both the
numerator and the literal denominator are (b)-normalised, so the convention
mismatch enters **only** through the step `E^{(cc)}_desc = R_{cc}·(e^{ik}−1)·
(−iχ/v_h)` — the assumption that "*the descendant term is exactly the
propagated charge-created leg, with no further dressing*".  `§1.3⟨3⟩2` states
that assumption, in parentheses.  `(b)(ii)` and clause 3b do not.  And
`§1.4` cost 3 says the data (under (α)) "*refutes that reading of `E^O_desc`
for any actual class member*" — so the merge text asserts, as a bare
consequence of the convention, a quantity computed under a hypothesis the same
document reports as refuted for every member of the class the definition is
about.

**(c) FIX DEMAND.**  In clause 3b: "*…contributes `Z_ρ^{-1/2}` **on the
charge-created reading of `E^O_desc`**, and **under the jet-identification
bridge (α) — the same unproved bridge named above** — that value is refuted
against the ansatz-free data at the pre-registered band…*".  Same two
qualifiers in the `AMP` row's Quantitative fence, whose "*PRE-REGISTERED
band*" sentence otherwise reads as evidence rather than as a conditional.

**(d) SURVIVING WEAKER STATEMENT.**  *The arithmetic is exact and fenced
(X2, reproduced at Y2): under (α) and the charge-created reading,
`Z_ρ^{-1/2}` misses by `0.4158/0.7347/1.0033` against a pre-registered `0.08`,
`5.2–12.5×`.  The fence's operative conclusion — that AMP needs a second,
non-leg-normalisation factor of exactly the computed size, and that any
proposed proof must be checked against D24N-C8 or it double-counts the leg —
survives verbatim under both qualifiers.  What does not survive is the word
"refuted" standing alone in an L4 file and an L5 row.*

---

### M3.  After the commit, `ML5-B` and `D24-VAL` point the DAG at r3 — whose §5 merge text, invariance list, `⟨1⟩4` conversion step and four headline checker claims r4 supersedes — with no supersession pointer.  This is r2-critic M4, one document over

**(a) Location.**  `§5.3a`, the `ML5-B` row, where-proved column: "*…clause-3
repair adjudicated in `theory/verdicts/d24d3-adjudication-r3.md` (bd tns-iu5
r3)*"; `§5.3b`, the `D24-VAL` row, where-proved column:
"*`theory/verdicts/d24d3-adjudication-r3.md` §2 ⟨1⟩3*".  Both are marked
"r3 verbatim" and neither mentions r4.  Against r4 `§0.2`, which supersedes
**eleven** r3 statements, including the §5/§5.2 preamble ("*All amplitudes
below are in the normalisation convention of (b)*" — struck as **false**),
`⟨1⟩0.⟨3⟩1`'s invariance list (**wrong**), `⟨1⟩4.⟨3⟩1` and `⟨1⟩4.⟨3⟩3`, and
"*there is no acceptance constant in the file*" in four layers.

**(b) My computation.**  Direct comparison of the two documents' §5.  r3
`§5.2`'s D24(d) block — the text a reader lands on from either row — contains
the preamble sentence r4 struck as false and clause 2 **without** its
normalisation statement.  Anyone reconstructing "what was merged for tns-iu5"
from the DAG's own pointers therefore reconstructs the r3 text, i.e. the
version whose defect this round exists to remove.  The corpus has already
adjudicated this exact species of defect: r2-critic M4 required the
`corpus-r2.md:174–178` **annotation** precisely "*so that ML5-B's where-proved
column does not point at a document certifying a different conclusion*", and
r3 §5.5 item 5 accepted it and calls it "the serious one".  The identical
argument applies to r3 itself now, and r4's fourteen same-commit obligations
contain no annotation of, or pointer to, r3's superseded status.  (r3 is not
this lane's writable file, which is exactly why the pointer must live in the
DAG rows, which are.)

**(c) FIX DEMAND.**  Append to both where-proved columns, in the merge text:
"*; superseded in part by `theory/verdicts/d24d3-adjudication-r4.md`, whose
§0.2 supersessions table is authoritative for the D24(d) preamble, the clause-2
normalisation, the invariance list and the ⟨1⟩4 conversion step*".  Two string
appends inside `§5.3a` and `§5.3b`; no other file changes.

**(d) SURVIVING WEAKER STATEMENT.**  *The rows' substance is right and I do
not reopen it: the `PROVED` status calls are correct (X7, X8), the
reparametrisation argument survives (X8), `S2-2body-S`'s exclusion from
ML5-B's depends-on is right, the `D24-VAL` antecedents are correctly displayed,
and the r3 steps the rows actually cite (`§2 ⟨1⟩3`, `ml5-universality ⟨1⟩3`)
are **not** among the superseded ones.  Only the navigation is defective —
and navigation is what an L5 file is.*

---

## 4.  MINOR

**m1.  `§5.5′` item 12's second anchor is stale, and that file is under
concurrent edit.**  `theory/ansatz-scattering-2m.md` was modified at 02:18
today by another lane (its r6 verdict landed during this review).  The ⟨2⟩5
step r4 names is no longer at `:621–631`: live it is at **`:673`** (the
`[RELABELED — D6 constructed-channel exhaustion-free first jet]` heading),
with "*D24(b)'s normalized packet multiplier convention*" at **`:675–676`** and
"*This uses the normalized multiplier amputation of D24(b), with no extra
`ε^{-1}` factor*" at **`:692`**; `§2`'s `:614` pointer now lands on an
unrelated Justification line.  *Fix:* apply item 12's second note after
`:692`, and — because that shard is actively being edited — instruct the
orchestrator to match on the quoted string rather than on the line number.
*Surviving:* the ML4 half of item 12 (`ml4-ward-reduction.md:63–68`) is exact
(Y11), and the note's text is correct for the step it targets.

**m2.  The "18 live sites" enumeration is neither fresh nor complete, and the
licensing clause's list does not cover one of them.**  My own whole-repo grep:
`claims/CLAIMS.md`'s corner-implication `𝒮_W` is at **line 83**, not 82 —
r4 §3 says it "*reproduc[es] the critic's table exactly*", which is what
propagated my r3 error rather than catching it.  **`HANDOFF.md:40` is a
nineteenth live site** and appears in no r4 list; it is not among the sites
`§5.4b′`'s licensing clause enumerates (D24 header, D25, the two CLAIMS rows,
`ml5-universality.md`, the Letter), so on the clause's own reading it would be
left unlicensed — it is saved only incidentally, because r3 §5.5 item 8
rewrites that very line.  Two further live bare uses sit in
`theory/ansatz-scattering-2m-r4-response.md:99` and `-r5-response.md:227`.
And `§5.4e`'s rationale still cites `ansatz-scattering-2m.md:146` as the live
`E_O` site "*re-verified this round*"; the live line is **`:170`** (`:146` is
now a `**⟨2⟩4. QED.**`).  *Fix:* correct `82 → 83`, add `HANDOFF.md` to the
licensing clause's list (or note that item 8 removes the occurrence), correct
`:146 → :170` in the rationale.  *Surviving:* the **disposition** is right and
nothing breaks — all 13 non-TRIANGLE sites are correctly licensed rather than
renamed, the five TRIANGLE renames are correctly kept, and after my scratch
application `definitions.md` and `notation.md` are mutually consistent (Y9).

**m3.  A new constant-true `require` ships in the round that deleted one for
being constant-true.**  `derive_exponent_band`, last line but one:
`require(band > 0.0, "D24N-C6 derived exponent band is zero")`.  By the
preceding guards `accept_band ∈ (0, 0.08)`, and `ratio = Σlog(2S)/Σlog²(2S)`
is the fixed positive constant `0.880539` over the module-level `SPINS`, so
`band = ratio·log(1/(1−accept_band)) > 0` **always**.  I probed it at
`accept_band = 1e-12, 1e-6, 1e-3, 0.0479, 0.0799`: `8.8e-13, 8.8e-7, 8.8e-4,
0.0432, 0.0733` — strictly positive by construction.  It cannot fail on any
input.  *Fix:* delete it, or declare it in the docstring's inventory as a
structurally-unreachable guard.  *Surviving:* it is harmless — the quantity it
guards is DISPLAY and gates nothing (§6.1) — and the file's real constants
inventory is otherwise accurate and complete.

**m4.  The corrupted-entry guard is scale-invariant, so a *uniform* inflation
of the quoted-error column still loosens the acceptance band up to the `0.08`
ceiling.**  `ROW_BAND_SANITY` tests `max/median`, a ratio, which is invariant
under multiplying every `error` entry by a constant.  My mutant, built on a
copy: multiply the whole `error` column by `1.6` **and** shift every slope by
`−6 %`.  Result: `exit 0`, green, with `D24N-C4 max_rel_dev=0.0641` and
`D24N-C6 candidate max_rel_dev=0.0631 vs acceptance band 0.0766 DERIVED from
the data's own quoted error`.  A `−6 %` corruption of the ground truth passes
every gate.  §6.4's stated residual covers "*a corrupted entry inflated by
less than 3× the median*"; it does not state that the guard is structurally
blind to the uniform channel.  *Fix:* one sentence in §6.4 and in the
docstring — "*the guard is a ratio and cannot see a uniform inflation of the
error column; the only backstop there is the `band < 0.08` subsumption
guard*".  *Surviving:* no conclusion is exposed, because both refutations hold
at the pre-registered `0.08` with `5–37×` margins and need no derived band at
all (X2), and `m8_errinflate` (`×4`) is caught by the subsumption guard.

**m5.  C2(v)'s reachability is real but indirect, and its marginal detection
power over C2(ii) is not established.**  Three measured facts.  (i) It is
**insensitive at `2S = 1`**: the coincidence term carries `2S − 1 = 0`, so my
isolated run gives `2.6e-14` under `--red-ladder`.  (ii) Under `--red-ladder`
its isolated error is `2.44e+03`, but C2 reports `1.477e+06`, which I traced to
sub-gate (iii) (multi-quantum norms at `2S = 4`: `576·3.7⁶ − 576`) — so **no
red mode's exit path ever names (v)**, and §6.2's "*`--red-ladder` moves it*"
is true of the quantity but not visible in any recorded verdict.  (iii) Every
mutation of `ladder_element` is already caught **exactly** by sub-gate (ii)'s
dense-matrix cross-check at every `n ≤ 2S−1`, so (v)'s independent content is
confined to the composition path (`apply_charge∘apply_charge`, `inner`, the
coincidence bookkeeping), which no red mode exercises; the only mutant that
reaches it, `c4_overlapsign`, mutates the *prediction* rather than the
measurement.  *Fix:* report the isolated (v) error alongside C2's max, or give
(v) its own `require` so its exit path is nameable; and state that (v) adds
composition-path coverage, not ladder coverage.  *Surviving:* **it is not a
no-op and it is not subsumed as an identity** — I derived and independently
verified the closed form (Y3), and in green it is the *tightest* sub-gate
(C2's reported `1.199e-13` **is** (v)'s error).  The r3 hole is genuinely
closed; only the evidence for it is reported one level too strongly.

**m6.  §1.4's cost list omits the round's own selection principle.**  §1.1
refuses the literal horn with the cost "*`𝒮_W(ρ)` is provably empty again — the
defect this adjudication exists to remove*".  That is a selection *by
consequence*: the normalisation was chosen, among two otherwise available
readings, because the other one empties the class the adjudication is trying to
keep.  That is defensible — the chosen reading is the corpus's own Ward
normalisation, `ml4-ward` (11) with its `(N−2)` denominator, which I
independently confirmed equals `‖Q_0|h⟩‖²` at `Z_ρ = 1` — but it is a fourth
cost, and it appears nowhere in §1.4 and nowhere in the L4 text.  A reader of
merged clause 2 cannot tell that the alternative reading would make the clause
unsatisfiable.  *Fix:* a fourth bullet in §1.4 and one clause in clause 2's
parenthesis — "*(the alternative reading, against (b)'s asymptotic leg, is
unsatisfiable by an `O`-independent factor at every `ρ ≠ 1/2`, which is why
this normalisation and not that one)*".  *Surviving:* the choice itself is
right and its consequences are correctly drawn.

**m7.  "Each is a homogeneous statement in one amplitude" is not true of
clauses 4 and 5.**  Merged `§5.0′`, covariance paragraph.  Clause 4 bounds the
orthogonal channel "*with the relative norm bound of (b)*", i.e.
`≤ C_I|k|²‖M_1^O‖`, and clause 5 likewise: LHS `⊂ M_2` scales with `c′`, RHS
with `c`.  These are **two**-amplitude statements; they are invariant only
because `C_I` is existentially quantified and absorbs `c′/c`.  Clause 1 alone
is genuinely homogeneous.  *Fix:* "*clause 1 is homogeneous in one amplitude;
clauses 4 and 5 are two-amplitude bounds whose constant `C_I` absorbs `c′/c`*".
*Surviving:* the invariance **list** (1, 4, 5 invariant; 2 not) is correct —
only its stated reason is.

**m8.  "Jointly with clause (d)2's residue anchor" conflates two different
jobs.**  Merged `§5.0′`: "*Fixing `c′(0)/c = 1` as above, jointly with clause
(d)2's residue anchor, is what makes `𝔞_leg` a number rather than a name*".
On the covariance group `𝔞_leg ↦ (c′(0)/c)𝔞_leg`, which the same paragraph
displays — so `c′(0)/c = 1`, supplied by (b) **alone**, already pins `𝔞_leg`
against the freedom the paragraph is about.  What clause 2 adds is different in
kind: a cross-normalisation *membership* constraint that ties `E^O_desc` to
`2iv_hM_1^O`, and it is that, not a covariance fixing, that produces a value.
Calling both "anchors" of one convention makes the paragraph read as if the
covariance freedom were fixed twice.  *Fix:* "*…is what pins `𝔞_leg` against
rescalings; clause (d)2, read charge-created, is a membership condition and it
is what ties the value to the model*".  *Surviving:* the algebra is right — I
verified `𝔞_leg` is determined exactly once (Y12) — and the two-anchor
**structure** is well posed; only its description mixes two axes.

---

## 5.  NOTE

**n1.**  D24N-C3 certifies only clause 2's **left-hand side**.  "*This clause
is correct at every density*" is a satisfiability claim that additionally needs
`M_1^O(h)` in (b)'s normalisation to equal `1` for the seed, an object no gate
computes and no corpus site fixes.  It is not wrong — clause 2 is a membership
condition, so nothing is asserted about any particular `O` — but "correct" is
the wrong word for a condition, and "*satisfiable*" in §1.1 is asserted rather
than shown.  One word ("*this clause is consistent at every density: its
left-hand side is exactly `Z_ρ`-linear …*") would settle it.

**n2.**  Bare `𝔞_leg` in merged D24(c) and in the ML5-A row is not a
"*fixed-`ρ` display*" in overload rule 13's sense — D24(c) is stated at every
density.  The span was ruled MERGE in r3 and I am **not** reopening it; flagged
only so the next editor does not read rule 13 as licensing bare `𝔞_leg`
generally.

**n3.**  The `AMP` row's parenthetical "(`--red-halfpower`, deviations
0.42/0.73/1.00 vs band 0.08)" attributes to that red mode a band it no longer
prints — its live message names the derived `0.0479`.  The deviations do exceed
`0.08`, so the claim is true; only the attribution is stale.

**n4.**  `c3_wrongdispersion`'s stated `4.000e+00` depends on the exact
mutation; my own variant (`2JS → 4JS`) dies at the same gate with `6.828e+00`.
Not a discrepancy — recorded so a future round does not read the number as a
fingerprint.

**n5.**  **Concurrency.**  `theory/ansatz-scattering-2m.md` and
`theory/checks/ace_ld_check.py` are dirty in the working tree and another
lane's r6 verdict appeared during this review.  Line-addressed same-commit
edits in that lane's files are a race; `claims/CLAIMS.md` row numbers could
drift too.  r4 already offers label-matching for CLAIMS; extend that
instruction to item 12.

---

## 6.  Register comparison

Nearest PROVED row: **`S2-2body-S`**, whose adjudicated scoping sentence is the
corpus standard — say exactly what is proved, then enumerate by name what is
not.

r4's own register paragraph does that, and does it well: "*F1 resolved by an
explicit two-anchor convention (a choice, priced in §1.4, not a theorem);
NOTHING promoted, no member exhibited, no value installed, `ML1` and AMP and
(α) and nonemptiness all still open and all still named at every point of
use*".  I checked each conjunct and each is true of the merge text.  §1.4 is
the best paragraph in the round — a cost list that names the loss of the
previous round's selling point.

Departures, all localised, all in text destined for an L4/L5 file:

| Layer | What it says | Strength |
|---|---|---|
| §1.4 costs 1–3 | one-convention preamble dead; clause 2 convention-constitutive; `Z_ρ^{-1/2}` demoted to a mismatch | **all three verified paid in the merge text** |
| §6.1 | fitted-exponent gate provably subsumed → DISPLAY | **correct, and volunteered against interest (Y4)** |
| §6.2 | the `0 ≡ 0` gate deleted; replacement derived | **correct (Y3)**; reachability over-reported (m5) |
| §5.2′ clause 2 | "differ by **exactly** `√Z_ρ` ((b)(i))" | **overstates (M1)** |
| §5.2′ 3b / `AMP` row | `Z_ρ^{-1/2}` "**is refuted**" | **overstates — (α) and the cc reading dropped (M2)** |
| §5.3a / §5.3b | where-proved → r3 only | **navigationally false after §0.2 (M3)** |

**Reliance audit: clean.**  No REFUTED row is used.  The only ML4 contact is
`ml4-ward-reduction.md` **(11)** — PROVED, and I independently confirmed its
`(N−2)` denominator is `‖Q_0|h⟩‖²` at `Z_ρ = 1` — never the `n ≥ 2` second
display of (9).  Bethe enters only through `S2-2body-S`, which is PROVED
*without* an integrability hypothesis, and the bridge (α) built on it is
declared unproved at every use except the two flagged in M2.  `𝒮_W(ρ)`
nonemptiness is never assumed: it is the displayed antecedent `(β_S)` of
`D24-VAL` and the explicit scope of the requantified `AMP` row, and §8 keeps it
open at every `ρ` under bd `tns-axg`.

---

## 7.  MERGE / HOLD, clause by clause

M1 is one clause in `§5.2′` plus one label in the checker; M2 is two clauses in
`§5.2′` and two in `§5.3c′`; M3 is two string appends in `§5.3a`/`§5.3b`.
Hours, not a round.  Nothing else in the merge is disturbed by any of them.

| § | Clause | Decision | Missing step |
|---|---|---|---|
| **5.0′** | D24(b) — the two-anchor convention | **MERGE after M1** | Paragraph 1 byte-preserving (X5); the D12(b) citation is correctly struck and replaced by D24N-C8 + `ML1` (M1 of r3 discharged); the covariance display and the freedom audit are algebraically right (Y12).  Fix `(b)(ii)`'s "exactly" with the LSZ scope word; **m7**, **m8** are prose repairs in the same paragraph. |
| 5.1 | D24(c), 931–950 (r3 verbatim) | **MERGE** | Applies verbatim at the exact anchors (Y9/Y10); carries `𝔞_leg` into all three displays; constant-agnostic sentence correct.  See **n2**. |
| **5.2′** | D24(d) preamble | **MERGE** | The struck blanket sentence and its replacement are exactly the F1 fix demand; the five-condition count is preserved; `Z_ρ`, `ρ > 0`, ANTISYMMETRY W8/W9/W16-fenced. |
| 5.2′ | clause 1 (`E^O_desc`) | **MERGE** | Unchanged; genuinely homogeneous (unlike 4/5 — m7). |
| **5.2′** | clause **2** | **HOLD** | **M1** ("exactly `√Z_ρ`" citing `(b)(i)`), **m6** (why this reading and not the other), **n1** ("correct" → "consistent"; one-sided certificate).  The displayed normalisation statement itself is exactly right and is the round's central repair — keep it verbatim. |
| 5.2′ | clause **3a** | **MERGE — unconditionally** | Unchanged; W10-fenced; the literal denominator is what makes the covariance work (Y12). |
| **5.2′** | clause **3b** | **HOLD** | **M2** (both dropped hypotheses).  The kernel-existence scope added this round is exactly r3-M1's fix demand and is correct; "*this definition fixes no value … `ρ = 1/2` included*" remains the honest centre of the file. |
| 5.2′ | clauses 4, 5, closing ¶ | **MERGE** | Unchanged; see **m7** for the covariance-paragraph wording only. |
| **5.3a** | ML5-B row (r3 verbatim) | **HOLD** | **M3** — one append.  Status, reparametrisation and depends-on all verified (X7, X8). |
| **5.3b** | `D24-VAL` row (r3 verbatim) | **HOLD** | **M3** — one append.  Antecedents (α)/(β_S) correctly displayed; the `ρ`-vs-`s` fence at the point of use is good practice. |
| **5.3c′** | `AMP` row | **HOLD** | **M2** (same two qualifiers), **n3** (stale band attribution).  The requantification is exactly r3-M5's fix demand and is correct; "*dropping (α) is what distinguishes this row from D24-VAL*" is the right answer to the double-count question. |
| 5.3d | ML5-A row | **MERGE** | Verified at the shard; the false D24(e)/`ml4_check.py` dependency stays struck. |
| 5.4a′ | `L(k,h)`, `Z_ρ`, `E^O_desc` rows | **MERGE** | Correct; anchors verified (Y10). |
| 5.4a′ | `𝔞_leg(ρ)` row | **MERGE** | The kernel-existence clause is added exactly as r3-M1 demanded, and the "asserted `= 1/Z_ρ` by the CONJECTURE row AMP (scoped, without the bridge)" wording tracks §5.3c′. |
| 5.4b′ | `𝒮_W(ρ)` row + licensing clause | **MERGE with m2's correction** | The licensing mechanism is the right (cheap) fix and mirrors overload rule 13; add `HANDOFF.md` to its enumerated list or note item 8 removes the site. |
| 5.4c | `𝖲` row cross-ref | **MERGE** | Anchor 244 re-verified; applied cleanly. |
| 5.4d | overload rule 2 amendment | **MERGE** | Applied cleanly at 91–98. |
| 5.4e | overload rule 8 amendment | **MERGE** | Fenced text is correct and applies at 123–130; only the **rationale**'s `:146` is stale (m2). |
| 5.4f | new overload rule 13 | **MERGE** | 13 confirmed next free (X6); inserted after 145 with the blank line preserved (Y9). |
| 5.5′ | ADVISORY items 1–14 | **MERGE, NOT optional, with m1's corrected address** | Items 1–9 verified live (Y11); items 10, 11, 13, 14 correct; **item 12's second anchor must become `ansatz-scattering-2m.md:692`, matched on the quoted string** (m1, n5). |

**May the merge proceed as ONE commit?**  **Yes — as one commit, and only as
one commit — but not as printed.**  I applied every span and the commit is
mechanically ready (Y9); what blocks it is three sentence-level repairs (M1,
M2, M3) plus the two corrected addresses in m1/m2.  I do **not** ask for
another full round: these are quotable one-line edits, and if the repair lane
lands exactly them, the merge is clear.

### The exact ordered recipe (verified by application, once M1–M3 are patched)

1. **`definitions.md`, descending, three REPLACEs.**
   (a) 952–973 (`**(d) The Ward-covariant no-contact class` → `is part of the
   ML5-B future work.`) ← r4 §5.2′, with M2's two qualifiers in 3b, M1's LSZ
   scope word and m6's clause in clause 2, n1's "consistent";
   (b) 931–950 (`**(c) The contact first jet.**` → `factorisation with the
   same stated norm control.`) ← r3 §5.1 verbatim;
   (c) 923–929 (`**(b) Amputated amplitudes.**` → `waves are generalised
   kernels inside \`C_c^∞\` packets (D3(a), D12(a′)).`) ← r4 §5.0′, with M1's
   scope word in (b)(ii) and m7/m8's two prose repairs.
2. **`notation.md`, six edits, in this order** (each anchor verified valid at
   the moment it is applied): §5.4b′ REPLACE line 258 → §5.4a′ ADD four rows
   after 258 → §5.4c one-string replace in line 244 → §5.4f INSERT rule 13
   after line 145 (blank line 146 and `All other symbols are unique.` at 147
   preserved) → §5.4e APPEND to rule 8 (block 123–130) → §5.4d APPEND to
   rule 2 (block 91–98).  Add `HANDOFF.md` to §5.4b′'s licensing list.
3. **`claims/CLAIMS.md`, four edits, matched on row label** (safer than line
   numbers — n5): REPLACE `| ML5-B |` (line 41) ← §5.3a **+ M3's append** →
   ADD `D24-VAL` after it ← §5.3b **+ M3's append** → ADD `AMP` after that ←
   §5.3c′ **+ M2's two qualifiers, n3's corrected attribution** → REPLACE
   `| ML5-A |` (line 40) ← §5.3d.
4. **The fourteen §5.5′ obligations, same commit**, with two corrections:
   item 12's second note goes after `theory/ansatz-scattering-2m.md:692`
   (match the string "*the normalized multiplier amputation of D24(b)*", not
   the line number); §5.4e's rationale reads `:170`, not `:146`; §3's CLAIMS
   address reads `83`, not `82`.
5. **Checker**, same commit: M1's DISPLAY label or divisor; m3's dead
   `require`; m4's one-sentence residual; m5's isolated-(v) reporting.

---

## 8.  `𝒮_W(ρ)` nonemptiness, `tns-axg`, `tns-iu5`

**`𝒮_W(ρ)` nonemptiness remains OPEN at every `ρ`, `ρ = 1/2` included** — and
it is now open rather than *provably empty*, which is a real gain: under the
adopted reading clause 2 is the corpus's own certified Ward identity, so the
`√Z_ρ` obstruction to membership that the literal reading created is gone.
I verified there is no residual emptiness argument: clause 2 constrains the
source, not the convention (Y12), and no other clause acquires an
`O`-independent factor.

* **bd `tns-axg`: stays OPEN and MAY NOT move.**  Nothing here exhibits a
  member.  The r1 M3(c)(iii) declination remains correctly reasoned.
* **bd `tns-v44`: unblocked on this axis.**  r3 §5.5 item 7's riders stand, and
  the F1 rider is now discharged *into the definition itself* — the merged text
  says in displayed words that clause (d)2's residue and `E^O_desc` are not in
  the same normalisation, so the shard cannot assume otherwise while citing it.
* **bd `tns-iu5`: MUST STAY OPEN.  Two of four sub-tasks remain, and a third
  is done-modulo-M1/M2's wording.**
  1. *(done, r3+r4)* D24(b)'s amputation and soft-leg convention, correctly
     scoped to the register where its kernel is constructed.
  2. *(substantively done, r4; wording HELD by M1 + M2)* the normalisation of
     clause (d)2's residue fixed in displayed text, and clauses 1–3 made
     consistent with it.  **This is what closes when the three MAJORs land.**
  3. *(OPEN — this is `ML1`)* supply, or scope away, the `δ`-normalised
     asymptotic one-magnon kernel off the fully polarised family;
     `𝔞_leg(ρ)`'s definedness at general `ρ` rests on it.
  4. *(OPEN — the prover target)* prove or refute **AMP**, with the sharpened
     fence: leg conversion supplies exactly `Z_ρ^{-1/2}` (in the LSZ limit —
     M1), so a second, non-leg-normalisation factor of the same size is
     required; `D24-VAL` stays vacuous-or-unknown until (4) closes or
     `tns-axg` exhibits a member.

---

## 9.  The four questions the brief asked

1. **Is the two-anchor convention well posed, or does it merely name the
   inconsistency?**  **Well posed.**  I carried the `(c, c′)` algebra through
   the (3a) quotient with the hard-leg factor `η` explicit: `η` cancels; clause
   2, read charge-created on the hard-leg-amputated residue, is `η`-invariant;
   `(b)` fixes `c′(0)/c = 1` and pins `𝔞_leg` exactly once; clause 2 then acts
   as a cross-normalisation *membership* condition that ties the value to the
   model.  Nothing is over- or under-determined.  Two caveats: the description
   of clause 2 as a second *covariance* anchor mixes two axes (m8), and the
   choice between the two readings was made by its consequence for emptiness,
   which is defensible but undisclosed (m6).  **The three claimed costs are all
   actually paid in the merge text**, not merely in prose — I diffed it (Y12).
   Nothing downstream assumes a single convention: the only shards that
   transplant D24(d)3 (`soft-index.md`, `soft-index-b.md:757–758, 808`) already
   receive ERRATUM pointers in the same commit, and the two `D24(b)` citation
   sites are correctly identified as D6-only coincidences.
2. **Does the Q-identity narrowing survive, and is the discharge legitimate?**
   **Yes, and yes** — see §2.  The X2 fence was conditional on exactly the
   reading now displayed in the definition; adopting an antecedent by an
   independent act discharges the conditional without circularity.  Its m1 soft
   spot is genuinely closed by a real gate (Y5), and the r3 overclaim now ships
   as `--red-descnorm` dying with error exactly `2.000e+00`.
3. **The checker.**  Both standing complaints are discharged.
   `EXPONENT_FIT_BAND` is deleted, the band is derived from the same error
   column, **the subsumption proof is correct** (Y4) and the demotion to
   DISPLAY is the right disposition — fence it.  The `0 ≡ 0` gate and its
   constant-true guard are gone and the replacement is a genuine test whose
   closed form I derived and verified independently (Y3).  Residual: one new
   constant-true `require` (m3), one structurally scale-blind guard (m4), one
   over-reported reachability (m5), and one DISPLAY line that prints an
   LSZ-limit number as a finite-`N` measurement (M1).  The m2 deviation is
   **accepted** — I ruled for the lane after checking both halves of its reason
   (Y7).
4. **Merge appliability.**  Verified by doing it (Y9): three `definitions.md`
   spans, six `notation.md` edits in the newly supplied order, four CLAIMS
   edits — all apply with every stated anchor asserted, and the supplied
   `notation.md` order is the correct fix for m3.  The 18-site rename list is
   correctly **split** (5 renamed, 13 licensed) but is not complete and one
   address is off by one (m2); one of the fourteen same-commit obligations has
   a stale anchor in a concurrently edited file (m1).  Neither blocks the
   commit once the corrected addresses in §7 are used.

---

**FAIL(M1, M2, M3)**

*Trajectory `3/7/6/4 → 1/5/8/5 → 1/5/8/4 → 0/3/8/5`.  First round with no
FATAL, and the first in which every prior item is fixed rather than relocated.
The physics is unchanged for the fourth consecutive round and is now better
fenced than at any earlier point: the leg-conversion identity is exact on the
vacuum leg and correctly qualified on the descendant leg, the descendant norm
is gated, the two refutations are exact at the pre-registered band, and the
corpus's `2` rests on the contact route.  What remains is one scope word, two
dropped hypotheses, and two DAG pointers.*
