<!-- ROLE: adversarial critic verdict, AC-EX-2M round 6 (CONVERGENCE CHECK).
     Writable lane: this file only.  No repair, no CLAIMS/definitions/notation
     edit, no commit. -->

# AC-EX-2M — r6 critic verdict (convergence check)

**Targets.** `theory/ansatz-scattering-2m.md`,
`theory/ansatz-scattering-2m-r5-response.md`,
`theory/checks/ansatz_scattering_2m_check.py`.
**Priors.** `-r1` … `-r5`; trajectory `6 → 2 → 1 → 1 → 1` MAJOR, 0 FATAL.
**Scope.** `git diff 433f0b3..HEAD` on the two lane files, plus the promoted
rows in `claims/CLAIMS.md`.  Nothing settled in r1–r5 is re-litigated and r5
§7's fence is not churned.

## 0. Headline, stated precisely so it cannot be misread

**Against the shard, the checker and the r5 response: 0 MAJOR, 0 FATAL.  The
repair lane has converged.**  Every claim it made about its own work is true,
and I checked the checkable ones byte by byte rather than reading them.

**Against the promotion package** — `claims/CLAIMS.md` + `definitions.md` +
`notation.md`, which no lane may edit and which no round has audited on this
axis — **1 MAJOR**: `AC-EX-2M` is the only PROVED row in the DAG whose
`depends-on` names a definition that does not exist in the single source.
That is R6-O1.  It is repaired by one orchestrator commit containing zero
mathematics; the block to be merged is already written verbatim in the shard.

So the trajectory line is **`6 → 2 → 1 → 1 → 1 → 1`**, and the honest gloss is
that the 1 has moved off the artifact under repair and onto the file the
artifact was promoted into.  Compare r5's own summary of the same drift:
r4's MAJOR indicted a soundness defect, r5's indicted no mathematics, and
r6's indicts no *shard* at all.

Also, up front, because the brief asked and because it is the most interesting
thing that happened this round: **the lane's rejection of my predecessor's
option (α) is CORRECT**, and I proved it in exact rational arithmetic rather
than reproducing the lane's floats.  §5 fences it.

---

## 1. What I independently recomputed (obligation 1)

| id | claim under test | how I tested it, independently | result |
|---|---|---|---|
| **X1** | `⟨1⟩7′.⟨2⟩1`'s body is the old `⟨1⟩9.⟨2⟩4` byte-for-byte | `git show 433f0b3:…` to a temp file; extracted both blocks by `awk` on their headers; `cmp` | **TRUE**, 1167 bytes, `cmp` silent |
| **X2** | `⟨1⟩3`--`⟨1⟩7` byte-identical to the promotion commit | extracted lines `126–383` (old) and `150–407` (new) — `⟨1⟩3` heading through the blank line before the next `##` — and `cmp` | **TRUE**, 11155 bytes each, `cmp` silent |
| **X3** | the only edit inside `⟨1⟩2`--`⟨1⟩7` is the one sentence r5 mandated | `diff -u` of the whole `⟨1⟩2` block, old vs new | **TRUE**: exactly one hunk, `⟨1⟩2.⟨2⟩2`'s Justification, and it is R5-O7's demanded text |
| **X4** | `⟨1⟩7′` sits between `⟨1⟩7` and `⟨1⟩8`, outside `⟨1⟩9`'s ASSUME | line addresses: `⟨1⟩7` @340, `## 3′` @408, `⟨1⟩7′` @410, `## 4` @448, `⟨1⟩8` @450 | **TRUE** |
| **X5** | no step of `⟨1⟩2`--`⟨1⟩7′` consumes a D29 clause | `grep` over lines 96–447 for `D29`, `ACE2M-LSZ`, `ACE2M-SR`, `(SR)`, `⟨1⟩8`, `⟨1⟩9`, `Haag` | **TRUE**: every hit is either a `refs/` citation, `⟨1⟩7.⟨2⟩4`'s explicit *disclaimer* of use, or `⟨1⟩7′`'s own D29-freeness declarations |
| **X6** | `⟨1⟩2.⟨2⟩2`'s new acyclicity sentence | enumerated **every** `⟨1⟩n` cross-reference in lines 150–447 | **TRUE**: no step of `⟨1⟩3`--`⟨1⟩7′` cites `⟨1⟩7.⟨2⟩2`; the only `⟨1⟩2` references are `⟨1⟩5.⟨2⟩4→⟨1⟩2.⟨2⟩1` (scope) and `⟨1⟩7′.⟨2⟩1→⟨1⟩2.⟨2⟩3` |
| **X7** | option (α) is an exact identity | analytic one-liner **plus** a from-scratch reimplementation over `Fraction` with arbitrary rational tensors, observable, "fixed point" and `δ`, five seeds | **exact residual `0`, five for five** (§5) |
| **X8** | the lane's four (α) floats | reimplemented (α) on a copy of the checker | `8.313e−17` / `8.791e−17` / `1.038e−16` / `2.949e−16` — **all four match to two digits** |
| **X9** | checker green + seven reds | `python3 -O`, repository root | green **exit 0**; all seven **exit 1**; exit paths identical to r5 §4.1 and to the applied `where-tested` cell |
| **X10** | eight mutants on copies | rebuilt `c1,c2,c3,d1–d4` and the `λ̃` battery from scratch in a scratch dir | **every row of the lane's §4.2 reproduces exactly**, including `c3`'s `G4 1.000e−06 / G6 1.600e−05`, `d4`'s `cap 0.197531`, `λ̃=0.34 → cap 0.106797`, `λ̃=0.9999 → exit 0` |
| **X11** | the `16×` bound and the `(6.25·10^-14,10^-12]` fire-alone window | derived in closed form: `‖C^{⊗w}‖=2^w`, so `1/(‖C‖‖D‖λ̃^{d_sep})` is maximal at `w_C=w_D=1,d_sep=6`, `=1/(4·2^{-6})=16`; hence G6-alone needs `agreement∈(10^{-12}/16,10^{-12}]` | **both figures confirmed analytically** |
| **X12** | the C1a ground truth `4/3·(−1/3)^d` | a **third** independent construction: AKLT MPS in the standard `\|+1,0,−1⟩` basis, `A^{+1}=√(2/3)σ^+`, `A^0=−√(1/3)σ^z`, `A^{-1}=−√(2/3)σ^-`, physical `S^z=diag(1,0,−1)` | transfer spectrum `{1,−1/3,−1/3,−1/3}` (so `λ_E=1/3` exactly), connected correlator matches to `4.7e−17`, `d=1..12` |
| **X13** | §7 mirror vs live `claims/CLAIMS.md` | escape-aware cell split, byte compare | `AC-EX-2M-D29` **byte-identical, 3465 bytes**; `AC-EX-2M` **DIFFERS** — see R6-M1 |
| **X14** | six columns each | split on unescaped `\|` | both rows: 8 fields = leading blank + **6 columns** + trailing blank. **TRUE** |
| **X15** | zero bare asserts | `grep -cE '^\s*assert\b'` | **0** |
| **X16** | reliance audit (obligation 5) | parsed every `depends-on` cell against `definitions.md` and `claims/CLAIMS.md` statuses | `S2-2body` PROVED, `ML2` PROVED, `ML1/ML3/ML6` named only as CONJECTURE/open; **no `ML4`, no `ML4-Ward`, no `ML5` (REFUTED), no `𝒮_W`**; every bare `S2` is the lane name; two explicit Bethe/integrability disclaimers. **CLEAN, sixth consecutive round** — *except* that the same parse produced R6-O1 |
| **X17** | R5-N6's blast-radius claim | `grep -rl` under `theory/`, plus every `depends-on` cell | **TRUE**: only the shard's own checker mentions it; the only DAG consumer is `AC-EX-2M-D29` (SKETCH) |

---

## 2. FATAL

**None.**  Sixth consecutive round.

---

## 3. MAJOR

### R6-O1 (MAJOR) — `AC-EX-2M` is the only PROVED row in the DAG whose load-bearing hypothesis does not exist in `definitions.md`

**(a) Location.**  `claims/CLAIMS.md`, row `AC-EX-2M`, `depends-on` cell:
"`D1, D3(a), D6--D8, D12(a′), D31, ML2`", against `definitions.md` (which ends
at D28) and `notation.md`.  The only text of D31 in the repository is
`theory/ansatz-scattering-2m.md:836`, under the heading
`### Exact addition to definitions.md`, inside `## 7. MERGE PROPOSALS`, in a
file whose ROLE banner reads: *"Shared definitions, notation, and claim rows
below are **proposals only**."*

**(b) My computation.**  Four parts, all mechanical.

*(i) D31 is absent from the single source, in every heading style.*
`grep -c "D31" definitions.md` → **0**.  Not "under a different heading level":
zero occurrences of the string.  I checked the heading styles explicitly,
because `definitions.md` mixes `## D28 (…)` with `**D6 (…)**` and a naive
`^## D\d+` scan falsely reports D6–D8 missing.  With both styles accepted,
`definitions.md` defines exactly `D1 … D28`.

*(ii) `AC-EX-2M` is the unique offender at PROVED.*  I parsed every row's
`depends-on` cell (escape-aware split, since these rows contain `\|`) and
differenced the D-numbers against the defined set.  The complete output is two
rows:

```
AC-EX-2M       **PROVED** (conditional, A2M.1--A2M.2; …)   missing=['D31']
AC-EX-2M-D29   SKETCH                                       missing=['D31']
```

Every other row in the DAG resolves.  So this is not a corpus-wide convention
being applied consistently — it is one row, and it is at PROVED.

*(iii) The row's own statement text is written in unanchored symbols.*  The
applied `AC-EX-2M` statement cell asserts its theorem using `P_B`, `d_B`,
`𝓡_inel`, `𝒟_{12}`, `Γ_M`, `I_2`, `ε_v`, `η_inel`.  Counting occurrences in
the two single sources:

| symbol | `notation.md` | `definitions.md` |
|---|---|---|
| `d_B`, `𝓡_inel`, `𝒟_{12}`, `Γ_M`, `P_B` | **0** | **0** |
| `(ACE2M-LSZ)`, `(ACE2M-SR)`, `𝒜_α`, `A_j(ε)` | **0** | **0** |
| `ε_v`, `Θ_inel`, `η_inel` | 1 row — bound to **`definitions.md D28`**, annotated *"(last three: fence only, Remark D28-R)"* | D28 only |
| `S_phys`, `λ_E` | present | present |

The third line is the sharp one: `notation.md` currently binds `ε_v`,
`Θ_inel`, `η_inel` to **D28**, while the shard's proposed additions bind the
same three symbols to **D31**, and the applied `AC-EX-2M` row uses them in the
D31 sense.  That is an L4 collision (*"Every symbol/definition lives exactly
once"*) waiting at the merge, and it is live in the DAG today: a reader
resolving `η_inel` from `notation.md` lands on D28's fence remark, not on
D31(5)'s inelastic inventory.

*(iv) Why this is MAJOR and not bookkeeping.*  `AC-EX-2M` at PROVED asserts
exactly one thing: *D31 ⟹ (A2M.1)–(A2M.2)*.  If D31 has no canonical text, the
row's entire content is unresolvable from the single source, and L9 —
*"every statement in the Letter traces to a PROVED claim"* — cannot be
discharged for anything this row supports.  The register comparison makes it
concrete: the nearest PROVED sibling `AC-EX` depends on `D28`, which **is** in
`definitions.md` at line 1081 with its symbols in `notation.md`.  r5 compared
the two rows on seven axes and found `AC-EX-2M` in register or stronger on all
of them; it did not check the eighth axis, hypothesis anchoring, and on that
axis `AC-EX-2M` is the weaker of the two.  The precedent for the severity is
r5's own MAJOR, which likewise indicted no mathematics: *a correct step filed
in the wrong place, and a cell pointing at the wrong range.*  This is a correct
definition filed in a proposals section while the row that depends on it stands
at PROVED.

**(c) FIX DEMAND.**  One orchestrator commit, no mathematics:
merge `theory/ansatz-scattering-2m.md` §7's `### Exact addition to
definitions.md` block into `definitions.md` verbatim as `## D31 (H-ACE2M:
exact fixed-packet two-magnon data over one vacuum)`; merge §7's
`### Exact additions to notation.md` table into `notation.md`, and resolve the
`ε_v`/`Θ_inel`/`η_inel` collision explicitly (either one row per definition,
`ε_v` (D28) and `ε_v` (D31), or one row naming both sources); then replace
both §7 proposal blocks with a pointer to the merged text, so the shard stops
carrying a second copy.  Until that lands, `AC-EX-2M` is PROVED against a
hypothesis with no canonical text.

**(d) SURVIVING WEAKER STATEMENT.**  *Nothing mathematical weakens.*  Every
proposition (A2M.1)–(A2M.2) asserts remains proved, relative to the D31 text as
printed at `theory/ansatz-scattering-2m.md:836`, and `⟨1⟩7′` still exhibits D6
as a model of that text.  The surviving statement is: **`AC-EX-2M` is PROVED
(conditional) relative to a hypothesis whose only text lives in a proposals
section of the shard, so the row is not yet auditable from the single source.**
The status does **not** need to fall — see §8.

---

## 4. MINOR

### R6-M1 (MINOR) — the §7 mirror is now stale: three sites claim "byte-for-byte" and are false as of commit `b691621`

**(a)** `theory/ansatz-scattering-2m.md`: the header status block
(*"§7 mirrors both applied rows byte-for-byte"*), §7's
`### Applied claims/CLAIMS.md lockstep mirror` preamble
(*"reproduced byte-for-byte from `claims/CLAIMS.md`"*), §8 **Merged status**
(same sentence), and §7's **One residue** paragraph (*"Until it is made, this
mirror stays byte-identical to the applied row"*).

**(b) My computation.**  Escape-aware extraction of both rows from both files:

```
AC-EX-2M      claims/CLAIMS.md 4310 bytes   shard §7 mirror 4467 bytes   DIFFER
AC-EX-2M-D29  claims/CLAIMS.md 3465 bytes   shard §7 mirror 3465 bytes   IDENTICAL
```

First difference at character 2918 — the `where-proved` cell, and only that
cell.  I confirmed the lane was **not** wrong when it wrote §5:
`git show b691621 -- claims/CLAIMS.md` shows exactly one changed line,
`−4467 / +4310`.  So the lane's "4467 and 3465 bytes, checked
programmatically" was true at the moment it was written, and the divergence was
created afterwards by the orchestrator applying r5 §9 condition 2.  The lane
even pre-wrote the fix, in the right words, in the **One residue** paragraph.
This is a stale mirror, not a false claim.

**(c) FIX DEMAND.**  Replace the §7 mirror's `AC-EX-2M` row with the live
4310-byte row (the only change is `where-proved` → "*theory/ansatz-scattering-2m.md
⟨1⟩2--⟨1⟩7′*"), and rewrite the **One residue** paragraph in the past tense:
*"r5 §9 condition 2 has been applied (`b691621`): the cell now reads
`theory/ansatz-scattering-2m.md ⟨1⟩2--⟨1⟩7′`, and this mirror reproduces it."*
The three "byte-for-byte" sentences then become true again without edit.

**(d) SURVIVING WEAKER STATEMENT.**  The authoritative file is correct: live
`claims/CLAIMS.md` points `where-proved` at `⟨1⟩2--⟨1⟩7′`, and `⟨1⟩7′` is
where the certificate is.  `AC-EX-2M-D29`'s mirror is exact.  Only the shard's
copy of one cell is behind, in the direction of the *older* text.

---

### R6-M2 (MINOR, fix this first) — the applied PROVED row's nonvacuity citation still points at the address the hoist vacated

**(a)** `claims/CLAIMS.md`, row `AC-EX-2M`, **statement** cell:

> "…it is instantiated: D6 satisfies D31(1)--(5) (**⟨1⟩9.⟨2⟩4** with ⟨1⟩2.⟨2⟩3,
> whose justifications cite no D29 clause), so the implication is not vacuous."

and, in the same cell:

> "…is consumed by no step of **⟨1⟩2--⟨1⟩7**."

**(b) My computation.**  `⟨1⟩9.⟨2⟩4` no longer proves D6 ⊨ D31; it is a
labelled cross-reference marker that says so in its first line
(*"[HOISTED — now ⟨1⟩7′; address retained, not renumbered]"*).  So the PROVED
row's own nonvacuity citation now resolves to a signpost rather than a proof.
Condition 2 corrected the `where-proved` cell and left the statement cell
untouched — I verified there is exactly one changed line in `b691621`'s
`claims/CLAIMS.md` diff.  The second pointer is a scope mismatch of the same
kind: the row's declared proof range is now `⟨1⟩2--⟨1⟩7′`, but its
D29-freeness sentence certifies only `⟨1⟩2--⟨1⟩7`, i.e. it stops one step short
of the range the row itself declares — and the step it stops short of is
precisely the one whose D29-freeness was r5's entire MAJOR.  (The stronger
statement is true: X5 above walks `⟨1⟩2--⟨1⟩7′` and finds no D29 clause.)

**(c) FIX DEMAND.**  Two substring replacements in `claims/CLAIMS.md`, row
`AC-EX-2M`, statement cell — exact text:

```
it is instantiated: D6 satisfies D31(1)--(5) (⟨1⟩9.⟨2⟩4 with ⟨1⟩2.⟨2⟩3, whose justifications cite no D29 clause), so the implication is not vacuous.
```
→
```
it is instantiated: D6 satisfies D31(1)--(5) (⟨1⟩7′ with ⟨1⟩2.⟨2⟩3, whose justifications cite no D29 clause), so the implication is not vacuous.
```

and

```
is consumed by no step of ⟨1⟩2--⟨1⟩7.
```
→
```
is consumed by no step of ⟨1⟩2--⟨1⟩7′.
```

Then re-mirror in §7 (R6-M1).

**(d) SURVIVING WEAKER STATEMENT.**  Both propositions are TRUE as facts; only
the addresses are stale.  The certificate exists, is at `⟨1⟩7′`, is outside
`⟨1⟩9`'s D29 ASSUME, and the `where-proved` cell — the authoritative locator —
already names it.  An auditor following the stale pointer lands on a marker
that redirects in its own heading, so nothing is unfindable.

---

### R6-M3 (MINOR) — the `⟨1⟩9.⟨2⟩4` marker's pointer inventory is now wrong in both directions

**(a)** `theory/ansatz-scattering-2m.md` `⟨1⟩9.⟨2⟩4`, the sentence
*"…so that the pointers in the applied `claims/CLAIMS.md` rows stay exact —
`AC-EX-2M`'s "plus ⟨1⟩9.⟨2⟩4", `AC-EX-2M-D29`'s "excluding ⟨1⟩9.⟨2⟩4 (which
belongs to AC-EX-2M)", and its "(⟨1⟩9.⟨2⟩5)" for the constructed-channel
jet."*

**(b) My computation.**  I enumerated **every** `⟨1⟩n[.⟨2⟩m]` pointer in both
live rows with a regex sweep.  Result: the marker names three pointers, of
which

- *"plus ⟨1⟩9.⟨2⟩4"* — **no longer exists** (deleted by condition 2);
- *"excluding ⟨1⟩9.⟨2⟩4"* — exists, in `AC-EX-2M-D29`'s `where-proved`;
- *"(⟨1⟩9.⟨2⟩5)"* — exists, in `AC-EX-2M-D29`'s statement cell;

and it **omits** the one live `AC-EX-2M` pointer to this address, the statement
cell's *"(⟨1⟩9.⟨2⟩4 with ⟨1⟩2.⟨2⟩3…)"* of R6-M2.  So the marker
under-inventories exactly the pointer that makes its own case, and
over-inventories one that is gone.  This is why the lane's stated precondition
for renumbering — *"renumbering becomes safe in the same pass in which the
orchestrator applies r5 §9 condition 2"* — is **false**: condition 2 touched
one cell, and two live `⟨1⟩9` pointers plus the stale `⟨2⟩4` citation remain.

**(c) FIX DEMAND.**  Replace the marker's pointer list with the audited one:
*"…so that the live pointers stay resolvable — `AC-EX-2M`'s statement-cell
citation of the D6 instance, and `AC-EX-2M-D29`'s "excluding ⟨1⟩9.⟨2⟩4" and
"(⟨1⟩9.⟨2⟩5)"."*  Better still, apply R6-M2 first and then reduce the list to
the two `AC-EX-2M-D29` pointers.

**(d) SURVIVING WEAKER STATEMENT.**  The marker's *decision* — retain the
address rather than renumber — is right, for the reasons in §6; only its
justification list is out of date.  The mathematics of `⟨1⟩9` is untouched: no
step of `⟨1⟩9` uses the marker and it contributes nothing to (A2M.3), exactly
as it says.

---

## 5. The G8 decision — the lane was RIGHT, and this is now fenced

The lane implemented r5's suggested fix (α), measured it, and refused it.
The brief asked me to verify the linearity claim independently.  I did, three
ways, and it holds.

**Analytic.**  `block_transfer(·,w)` is `w`-fold `observable_transfer(C,·)`,
which is linear in its matrix argument; `vacuum_expectation` is `tr`, linear;
`fixed_projection(right) = tr(right)·RIGHT_FIXED = ω_D·RIGHT_FIXED`.  Hence

```
fixed − fixed_δ = tr(B_{w_C}(δ·ω_D·RIGHT_FIXED))
                = δ·ω_D·tr(B_{w_C}(RIGHT_FIXED))
                = δ·ω_C·ω_D        (since one_c := tr(B_{w_C}(RIGHT_FIXED)))
```

identically — for every tensor, observable, fixed point, separation, support
length and `δ`.  (α)'s residual is `0` by construction, not by AKLT.

**Exact arithmetic (the decisive test).**  I reimplemented the whole C1b
algebra from scratch over `fractions.Fraction`, with **arbitrary rational**
`A^s` (χ=2, d=3), observable `C`, "fixed point" `RF` and `δ`, on the full
`(w_C,w_D,d_sep)` grid, five random seeds:

```
seed     1  delta=9/11  EXACT max residual = 0
seed     2  delta=7/9   EXACT max residual = 0
seed     3  delta=2     EXACT max residual = 0
seed    17  delta=3/5   EXACT max residual = 0
seed  2026  delta=1     EXACT max residual = 0
```

Exactly zero, five for five, on data with no relation to AKLT.  A gate with
genuine content cannot do that.

**Float reproduction.**  Independently reimplementing (α) on a copy of the
checker reproduces all four of the lane's numbers to two digits:
baseline `8.313e−17`; `A^a=σ_a/2` → `8.791e−17`; `RIGHT_FIXED=diag(.6,.4)` →
`1.038e−16`; `C=I+2S^z` → `2.949e−16`.  With fully random complex tensors the
absolute residual rises to `1.334e−04` — and the **relative** residual is
`5.27e−16`, i.e. pure double roundoff at the inflated scale.  That is the last
loophole closed: (α) does not "come alive" on harder data.

**Verdict on the decision.**  Option (α) would have been the corpus's *sixth*
identically-zero gate, and the worst of the six, because unlike the other five
it would have carried a δ-sensitivity name and a `10^{-12}` tolerance — it
would have read as a numerical certificate to every future round.  Option (β)
was correct.  I also confirm (β) was executed completely: the relabel appears
in the module docstring's new **WHAT EACH GATE IS EVIDENCE FOR** paragraph, in
the twelve-line probe comment, in G8's violation message, in
`--red-route-collapse`'s help string, and in §6's new paragraph ending *"No
round may cite G8 as numerical evidence"* — with the `route_guard` print key
deliberately unchanged so the applied `where-tested` cell stays true.  G8 keeps
the only content it ever had: `c1` (`direct := fixed`) and `c2`
(`fixed := direct`) both die on **G8 alone**, and `c3` (a genuine subtraction
error) leaves G8 at `0` while G4 reports `1.000e−06`.

> **FENCED — do not re-propose.**  The δ-sensitivity "upgrade" of G8 is an
> exact algebraic identity, proved analytically and in exact rational
> arithmetic in `ansatz-scattering-2m-r6.md` §5.  Any future round that
> proposes it is proposing a sixth identically-zero gate.  A proposer that
> tested a critic's suggested fix and refused it on measurement did the right
> thing, and the r5 critic (me, one round earlier) was wrong to offer (α) as
> an option.

---

## 6. RULING on the renumbering (brief item 2)

**Ruling: renumbering is PERMITTED but NOT RECOMMENDED, and r5 §9 condition 2
alone does NOT make it safe.**

*The lane's reasoning was right in kind and incomplete in inventory.*  Right in
kind: sliding `⟨2⟩5→⟨2⟩4` would make `AC-EX-2M-D29`'s *"excluding ⟨1⟩9.⟨2⟩4"*
name the constructed-channel jet — which **does** belong to `AC-EX-2M-D29` —
and would strand the *"(⟨1⟩9.⟨2⟩5)"* pointer.  That is exactly the hazard, and
declining to renumber rather than silently breaking two applied cells was the
correct call.  Incomplete in inventory: it found two of the three live pointers
and missed `AC-EX-2M`'s statement-cell citation (R6-M2, R6-M3), so its stated
precondition — *"renumbering becomes safe in the same pass in which the
orchestrator applies condition 2"* — is false.  Condition 2 changed one cell.

**Disposition A — RECOMMENDED: do not renumber.**  Keep `⟨2⟩5`--`⟨2⟩7` where
they are and keep the marker at `⟨1⟩9.⟨2⟩4`.  Three reasons.  (i) Lamport
imposes no contiguity requirement on `⟨2⟩` numbering; a labelled vacated
address is *more* auditable than a silent renumber, because it explains the
gap in place.  (ii) **Five prior verdicts (`-r1`…`-r5`) cite `⟨1⟩9.⟨2⟩4` and
`⟨1⟩9.⟨2⟩5` by those addresses**, and the verdicts are this campaign's audit
trail.  Renumbering silently invalidates every one of them and would require a
translation table that costs more than the marker.  (iii) The marker is a
declared non-proof-step that no step of `⟨1⟩9` uses; it carries no
mathematical weight.  Under Disposition A the required edits are R6-M2's two
`claims/CLAIMS.md` substrings, R6-M3's corrected pointer list, R6-M1's mirror
resync, and one `AC-EX-2M-D29` `where-proved` clarification:

```
theory/ansatz-scattering-2m.md ⟨1⟩8--⟨1⟩9, excluding ⟨1⟩9.⟨2⟩4 (which belongs to AC-EX-2M)
```
→
```
theory/ansatz-scattering-2m.md ⟨1⟩8--⟨1⟩9, excluding the vacated address ⟨1⟩9.⟨2⟩4, whose content is hoisted to ⟨1⟩7′ and belongs to AC-EX-2M
```

**Disposition B — permitted, if contiguity is wanted.**  Then **all** of the
following must land in ONE commit, or the PROVED row will cite a step
belonging to the SKETCH row as its nonvacuity certificate:

1. shard: delete the `⟨1⟩9.⟨2⟩4` marker; renumber `⟨2⟩5→⟨2⟩4`, `⟨2⟩6→⟨2⟩5`,
   `⟨2⟩7→⟨2⟩6` (QED).
2. `claims/CLAIMS.md`, `AC-EX-2M` statement cell — **required today anyway**
   (R6-M2): `(⟨1⟩9.⟨2⟩4 with ⟨1⟩2.⟨2⟩3` → `(⟨1⟩7′ with ⟨1⟩2.⟨2⟩3`.
3. `claims/CLAIMS.md`, `AC-EX-2M` statement cell — **required today anyway**
   (R6-M2): `no step of ⟨1⟩2--⟨1⟩7.` → `no step of ⟨1⟩2--⟨1⟩7′.`
4. `claims/CLAIMS.md`, `AC-EX-2M-D29` statement cell:
   `on D6 (⟨1⟩9.⟨2⟩5)` → `on D6 (⟨1⟩9.⟨2⟩4)`.
5. `claims/CLAIMS.md`, `AC-EX-2M-D29` `where-proved`:
   `theory/ansatz-scattering-2m.md ⟨1⟩8--⟨1⟩9, excluding ⟨1⟩9.⟨2⟩4 (which belongs to AC-EX-2M)`
   → `theory/ansatz-scattering-2m.md ⟨1⟩8--⟨1⟩9`.
6. shard §7: re-mirror both rows after 2–5.
7. a translation note (`r1–r5 cite the pre-hoist addresses ⟨1⟩9.⟨2⟩4 = now
   ⟨1⟩7′, ⟨1⟩9.⟨2⟩5 = now ⟨1⟩9.⟨2⟩4`) in the shard header, so the verdict
   corpus stays readable.

**Warning, and it is the reason this ruling exists.**  If step 1 is done
without steps 2–3, `AC-EX-2M`'s statement cell would read
*"D6 satisfies D31(1)--(5) (⟨1⟩9.⟨2⟩4 …)"* while `⟨1⟩9.⟨2⟩4` had become the
constructed-channel jet — a step that belongs to `AC-EX-2M-D29` and sits under
`⟨1⟩9`'s D29 ASSUME.  The PROVED row would then cite a D29-conditioned step as
its D29-independent nonvacuity certificate.  **That would be a MAJOR**, and it
would be r5's MAJOR reintroduced with the sign flipped.  Steps 2–3 are not
optional under either disposition.

---

## 7. Dispositions (brief item 5): are nine residues really deferrals?

Counted from the r5 response's table: **9 FIXED** (R5-O1…O7, N4, N8), **1
SUPERSEDED** (N3), **9 RESIDUE** (N1, N2, N5, N6, N7, N9, N10, N11, N12) — 19,
matching the brief.

Nine residues *is* a lot, so I checked each against the actual file rather than
the label.  The decisive fact: **all nine residues are r5 NOTEs**, and a NOTE
in this corpus is an observation, not a work order.  Eight of them are of the
form "this was already right; keep it", and "RESIDUE" is the correct
disposition for a NOTE that required no change:

| id | claimed | verified against the file |
|---|---|---|
| N1 | `⟨1⟩9.⟨2⟩5`'s Justification untouched | **TRUE** — string-identical to `433f0b3` |
| N2 | byte-freeze ends in exactly one place, disclosed | **TRUE** — X3: one hunk, and it is the one r5 mandated |
| N5 | `16×` and the fire-alone window stay quantified | **TRUE** — present in §6 and in the applied row; both figures re-derived analytically (X11) |
| N6 | blast radius recorded in the shard | **TRUE**, and the *claim* is true (X17) |
| N7 | `\|S_phys\|=1` at `⟨1⟩7.⟨2⟩3` unchanged, now also in `⟨1⟩1` | **TRUE** — `⟨1⟩7.⟨2⟩3` is inside the byte-identical range (X2) |
| N9 | no `refs/` citation changed | **TRUE** — no citation appears in any diff hunk |
| N10 | `⟨1⟩2.⟨2⟩3` untouched | **TRUE** — X3 |
| N11 | `⟨1⟩8` clause 3 untouched; only the schema paragraph appended | **TRUE** — the sole `⟨1⟩8` hunk is appended after **(SR)** |
| N12 | §6 still scopes the cap to `λ̃=1/2` | **TRUE**, and re-measured: `0.34 → G5 cap 0.106797`, `0.9999 → exit 0` |

**None is an unaddressed objection wearing a label.**  N2 is the only one that
records a deviation, and it discloses it accurately.  The three standing
RESIDUE-1/2/3 in the response's §6 are likewise honest: RESIDUE-1 is the
renumbering (ruled on in §6 above, with the lane's precondition corrected),
RESIDUE-2 is `--red-supportfold`'s self-fulfilling character (now disclosed in
§6 of the shard, not only in verdicts — a genuine improvement), RESIDUE-3 is
the open every-`λ̃` quantifier, which remains analytic content and is stated as
such.

---

## 8. Register comparison against the nearest PROVED row

Nearest sibling: **`AC-EX`** (`PROVED` (conditional, ACE.1--ACE.2; per
memory-index-r3.md §4 amended sentence)).

| axis | `AC-EX` | `AC-EX-2M` (applied row, today) | verdict |
|---|---|---|---|
| status-cell form | `**PROVED** (conditional, ACE.1--ACE.2; per <verdict>)` | `**PROVED** (conditional, A2M.1--A2M.2; per ansatz-scattering-2m-r5.md §9)` | **in register** (r5's R5-O5 landed) |
| conditionality stated at the point of statement | yes | *"proved only as the conditional implication"* | **in register** |
| hypotheses flagged as assumed, not derived | yes | *"D31(1)--(5)'s … data are hypotheses, not consequences of a variational ansatz"* | **in register** |
| load-bearing hypothesis instantiated? | *"(D28-C) … **is unverified on any model**"* | D6 ⊨ D31, proved at `⟨1⟩7′`, D29-free (X5) | **stronger** |
| certificate lives inside the declared `where-proved` | yes | yes, since `b691621` | **in register** |
| checker caveats carried into the row | dead-mutation disclosure | `ratio_route` retraction with `16×` and the `(6.25·10^{-14},10^{-12}]` window; G8 disclosed as a code-shape guard | **in register**, and more explicit than the sibling |
| negative inventory | long, explicit, complete | long, explicit, complete | **in register** |
| **hypothesis anchored in `definitions.md`** | **D28 at `definitions.md:1081`; symbols in `notation.md`** | **D31 nowhere in `definitions.md`; five of its symbols nowhere in either single source** | **BREACH → R6-O1** |

Seven axes in register or stronger; one breach, on the axis nobody has checked
before.  The honest summary is that the *sentence* is in register and the
*filing* is not.

---

## 9. VERIFIED CORRECT — fenced, do not churn

r3 §7, r4 §7 and r5 §7 remain in force and were not re-litigated.  New or
re-confirmed this round:

- **All three byte-identity claims** (X1, X2, X3): the hoisted body and its
  Justification are the old `⟨1⟩9.⟨2⟩4` to the byte (1167 bytes); `⟨1⟩3`--`⟨1⟩7`
  are byte-identical to the promotion commit (11155 bytes); the only edit
  inside `⟨1⟩2`--`⟨1⟩7` is R5-O7's sentence.  *Checked with `cmp` and `diff`,
  not read.*
- **The hoist itself** (X4, X5): `⟨1⟩7′` sits between `⟨1⟩7` and `⟨1⟩8`,
  carries the ASSUME/PROVE r5 demanded, consumes no D29 clause, and the
  promoted row's `where-proved` cell now contains it.  **R5-O1 is CLOSED.**
- **The revised acyclicity sentence** at `⟨1⟩2.⟨2⟩2` (X6) — verified by
  enumerating every cross-reference in the range, not by reading the sentence.
  **R5-O7 is CLOSED.**
- **Option (α) is an exact algebraic identity** — analytic proof, exact
  rational arithmetic (five seeds, residual exactly `0`), and the lane's four
  floats reproduced (X7, X8).  §5's fence applies.
- **G8's relabel is complete and honest** across all four advertising sites,
  with the `route_guard` print key deliberately unchanged.  G8 still kills all
  three route-collapse implementations, each on G8 alone; `c3` confirms it is
  blind to a genuine error that G4 catches at `10^{-6}`.
- **Checker hygiene and coverage** (X9, X10, X15): green exit 0; seven reds
  exit 1; nine gates; seven pairwise-distinct violation sets; exit paths
  identical to the applied `where-tested` cell; `violations()` evaluates all
  nine before exit and masks nothing; zero bare `assert`; eight mutants on
  copies all exit 2; the `λ̃` battery reproduces exactly.
- **The `16×` amplification and the `(6.25·10^{-14},10^{-12}]` fire-alone
  window** derived in closed form from `‖C^{⊗w}‖=2^w` (X11), independently of
  the lane's measurement.
- **The C1a ground truth**, reproduced in a **third** tensor basis (X12):
  transfer spectrum `{1,−1/3,−1/3,−1/3}` so `λ_E=1/3` exactly, and
  `4/3·(−1/3)^d` to `4.7e−17` for `d=1..12`.
- **`AC-EX-2M-D29`'s mirror** is byte-identical at 3465 bytes; both rows have
  exactly six columns (X13, X14).
- **The `(SR)[X]` schema fix (R5-O4)** reads correctly: `(ACE2M-SR)=(SR)[A_j]`
  for the D29 datum *plus* the `N,t`-limit clause; `⟨1⟩9.⟨2⟩5` now says it
  verifies `(SR)[A]` with the limit clause **bypassed rather than satisfied**,
  and the same correction appears at `⟨1⟩1`(A2M.3), §8 **Conditional** and the
  `notation.md` proposal row.  Four sites, consistent.
- **Reliance audit CLEAN, sixth consecutive round** (X16): no REFUTED row, no
  ML4-Ward `n≥2`, no ML5, no `𝒮_W`, no Bethe/integrability hypothesis.
- **Blast radius zero** (X17).

**Recorded so no future round mistakes it for a divergence.**  `⟨1⟩9.⟨2⟩6`'s
Justification cites *"the ML3/ML6 CONJECTURE rows"* while §8 says
*"ML1/ML3/ML6 … are unused"*.  These are consistent: `⟨2⟩6` is a negative
scope step and cites those rows for the fact that they are **open**, never as
premises.  r2, r3, r4 and r5 each audited this and each found it clean; I
concur and am not reopening it.

---

## 10. NOTES

**R6-N1.**  The brief's figure "*⟨1⟩3--⟨1⟩7 are byte-identical at 10577
bytes*" is not reproducible and does not appear anywhere in the lane's
response — `grep` finds `10577` only in `briefs/s2-critic-r6.md`.  The r5
response §5 makes only the qualitative claim (*"`git diff` against the
promotion commit shows no hunk in that range"*), which is **TRUE**.  For the
record, the range `⟨1⟩3` heading → blank line before the next `##` is **11155
bytes / 10615 characters**, identical in both revisions.  Not a lane defect;
recorded so the number is not propagated.

**R6-N2.**  `⟨1⟩7′`'s **ASSUME** — *"D6 and fixed compact packets obeying
D31(4)"* — grants D31(4) and then proves D31(1)--(5), i.e. it proves clause (4)
by assuming it.  Harmless (the certificate is an existence statement: *choose*
D6 and *choose* such packets), and **it is r5's own FIX DEMAND text, copied
verbatim as ordered** — not a lane defect.  A future tightening, if anyone
touches it: *"ASSUME. D6, and two compact packet supports whose velocity
supports are disjoint, separated by `ε_v>0`, and bounded away from zero.
PROVE. D31(1)--(5) hold for these data."*

**R6-N3.**  `violations()` appends G8 **before** G7, so a hypothetical joint
firing would print the exit path as `[…,G8,G7]`, out of gate order.  No
registered mutant triggers both, so nothing observed is affected.  Cosmetic;
swap the two blocks if anyone edits that function.

**R6-N4.**  §7's **One residue** paragraph was written for an orchestrator who
had not yet acted, and the orchestrator acted (`b691621`) using its exact
proposed text.  That is the loop working: the lane identified an out-of-lane
edit, wrote the replacement string, and the string was applied verbatim.  Worth
recording as a pattern, not an objection.

**R6-N5.**  `D29` appears in no `depends-on` cell anywhere in
`claims/CLAIMS.md`, so R6-O1 does not extend to it; only `D31` is a formal
dependency of a row.  If `D29` is ever added to a `depends-on` cell, it will
need the same merge treatment.

---

## 11. Deliverable

- **MAJOR count: 1.**  Trajectory `6 → 2 → 1 → 1 → 1 → **1**`.  Against the
  shard, the checker and the r5 response the count is **0** — the repair lane
  converged.  The surviving MAJOR (R6-O1) is against the promotion package and
  is discharged by one orchestrator commit containing no mathematics.
- **FATAL: 0**, sixth consecutive round.
- **MINOR: 3** (R6-M1 stale §7 mirror; R6-M2 stale nonvacuity pointer inside
  the applied PROVED row; R6-M3 the marker's pointer inventory).  All three are
  in the same one-commit fix as R6-O1.
- **NOTE: 5.**
- **Byte-identity claims: all three HOLD**, checked with `cmp`/`diff`.  The
  lane's own `4467`/`3465` mirror figures were true when written; `4467` went
  stale two minutes later when the orchestrator applied condition 2.
- **Renumbering ruling: PERMITTED, NOT RECOMMENDED; condition 2 alone does not
  make it safe.**  §6 gives both dispositions and the exact replacement text.
  Two `claims/CLAIMS.md` substring edits (R6-M2) are required **today** under
  either disposition.
- **G8: the lane is RIGHT.**  Option (α) is an exact algebraic identity —
  proved analytically and in exact rational arithmetic — and would have been a
  sixth identically-zero gate wearing a numerical name.  §5 fences it against
  re-proposal, including against me.
- **`AC-EX-2M` stays at PROVED (conditional, A2M.1--A2M.2) with its current
  sentence.**  No word of the adjudicated scoping sentence needs to change:
  every proposition in it is true and re-verified.  What must change is around
  it — the two stale pointers (R6-M2) and the D31 merge (R6-O1).  Do **not**
  demote; the mathematics is not in question and never was this round.
- **`AC-EX-2M-D29` stays at SKETCH**, on the same two named missing steps,
  restated verbatim: **(i)** prove at `O(k_s)`, with a displayed uniform
  remainder, that the `T→∞` D29 readout's connected packet-amputated on-shell
  pairing equals the constructed-channel one despite the PROVED branch mismatch
  `Q_{k_s}\|k_h⟩−\|B^{in}⟩=(1−S_{12})\|P_{12}⟩=−2ik_s\|P_{12}⟩+O(k_s²)`;
  **(ii)** exhibit an `(ACE2M-SR)` instance for the fixed-time D29 family that
  `(SR)` constrains, including existence of its `N,t` limits.  The only datum
  for which the `(SR)` conditions are verified remains the one-element,
  exhaustion-free, infinite-chain constructed-channel family
  `A(ε)(h)=∫dμ_f(u)S_phys(εu,h)` on D6, which backs no D29 claim.

**FAIL(R6-O1)**
