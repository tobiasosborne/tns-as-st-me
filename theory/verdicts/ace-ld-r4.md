<!-- ROLE: adversarial critic verdict, round 4 (promotion clearance), on
     theory/ace-ld.md, theory/ace-ld-r4-response.md and
     theory/checks/ace_ld_check.py.
     Protocol: briefs/critic-protocol.md (incl. Standing checker obligations).
     Priors: theory/verdicts/ace-ld-r1.md FAIL(F1,M1-M6);
             theory/verdicts/ace-ld-r2.md FAIL(F1,M1-M6);
             theory/verdicts/ace-ld-r3.md FAIL(F1,M1-M3) + cells 8(A)-(D).
     Lane: this file only.  Nothing here edits the shard, definitions.md,
     notation.md, claims/CLAIMS.md or the checker; the corrected cells in
     section 8 are the only text authorised for merge; no commit. -->

# ACE-LD r4 — critic verdict (promotion clearance)

**Verdict: FAIL(M1, M2).**
**Trajectory: r1 FAIL(F1,M1--M6) → r2 FAIL(F1,M1--M6) → r3 FAIL(F1,M1--M3)
→ r4 FAIL(M1,M2).**
1 FATAL + 6 MAJOR → 1 FATAL + 6 MAJOR + 8 MINOR + 6 NOTE → 1 FATAL + 3 MAJOR
+ 8 MINOR + 6 NOTE → **0 FATAL + 2 MAJOR + 7 MINOR + 7 NOTE.**
**No FATAL survives.  Both §8(E) preconditions are discharged.  All four
promotions are GO, with three corrected cells supplied verbatim in §8.**

Every number below was produced by me, by an independent route, this round.
Scripts named inline live in the session scratchpad: `lr2r4.py` (own ring
Hamiltonian, own packet, own clamp charge, own pinching — nothing imported
from the checker), `c6indep.py` (own `L=12` basis, own XXZ kink Hamiltonian,
own window charge, own TPM law), `chi.py` (the r3 F1 counterexample,
re-run), plus mutation copies under `r4mut/`.

**Headline.**  The r4 round is the strongest in this lane's history and it
earns the promotions.  The FATAL I owned in r3 is fully retired: the shard
now states sharp on-site charge, records the `χ=1` form as REFUTED with my
own counterexample, keeps the simple-eigenvalue conditional as a corollary,
and applies the correction at **every** site F1(a) enumerated — I checked all
ten and found no residue.  The four promotion cells are **byte-identical** to
my r3 §8(A)--(D) (machine-diffed; only `\|` escaping and an appended
"(pending L6 loop)" differ).  MP-4 binds exactly the five §8(E) symbols with
anchors that all resolve.  And the LR2 republication is right: I reproduced
`−3.3592` at `T = 20/40/80`, `−6.0832`/`−8.3868` at `t_-=0`, and
`0.8563/0.0170/0.1267`, from scratch — and the `V_0=0` separator **genuinely
separates**, passing the wedge at a *larger* value (`8.3868`) than green and
dying at the Cesàro gate at `−1.997e-04`.

Two things fail, and **both are downstream of my own r3 text**.  **M1** is
r3 M3 recurring at exactly the gates the r3 M3 repair introduced: §5's list
is advertised as a COMPLETE enumeration of unreached gates and omits two —
LD-C5b's `T`-stability gate and LD-C6's `t_+`-sweep gate — reached by no
registered mutation.  I fired both on copies; both have teeth.  **M2** is the
symbol audit: my r3 §8(E) claimed every symbol in the cells is bound, and it
is not — `p_tr` in cell (B) is bound nowhere in `notation.md`,
`definitions.md` or `claims/CLAIMS.md`, and neither are `(E-TAIL)`, `(V-ch)`,
`(V-in)`, `σ_L`, `σ_T`.  MP-4 faithfully reproduces my incomplete audit.  The
lane executed the work order correctly in both cases; the defective text is
mine, and §8 corrects it.

---

## 0. What I recomputed first

**(i) The LR2 republication, from scratch** (`lr2r4.py`: own ring
`H = Σ|x⟩⟨x+1| + h.c. + V_0|x_c⟩⟨x_c|` on `N = 2048`, own bump packet at
`k = −π/2`, own D13(a) clamp charge on `|W| = 17`, own branch decomposition
and forward transport).  Nothing imported.

| quantity | green `V_0 = 1.2` | separator `V_0 = 0` |
|---|---|---|
| wedge `\|Σνp − (⟨Q̂⟩_- − ⟨Q̂⟩_+)\|` | **6.0832** | **8.3868** |
| `t_-=0` defect at `t_+=300` | **−6.0832** | **−8.3868** |
| double-Cesàro `T=20` | **−3.359232** | **−1.997142e-04** |
| double-Cesàro `T=40` | **−3.359184** | `−1.687e-06` |
| double-Cesàro `T=80` | **−3.359207** | `−3.167e-09` |
| double-Cesàro `T=120` | `−3.359207` | `−3.847e-11` |
| double-Cesàro `T=200` | `−3.359382` | `−6.390e-14` |
| branch weights at `t_-=−80` | **0.8563/0.0170/0.1267** | `1.0000/0.0000/0.0000` |
| branch weights at `t_-=−400` | **0.8563/0.0170/0.1267** | `1.0000/0.0000/0.0000` |

Every published figure reproduces to the printed digit, including the
proposer's claimed `T = 80` scratch value.  **The separator separates**: it
clears `C5B_WEDGE_MIN = 1.0` by a factor `8.4` and dies at the Cesàro floor.
The mechanism is confirmed and is simpler than the shard says: at `V_0 = 0`
the backward-evolved packet is in **one** clamp branch (weight `1.0000`), so
the pinching is the identity and the defect is exactly zero up to numerics;
with the barrier it is permanently three-branch.

**(ii) The D16 kink+magnon battery, rebuilt from scratch** (`c6indep.py`: own
`C(12,7)` basis, own `h^{kink}` with the telescoping field, own `S^-` at site
10, own window charges).  Half-filled ground energy `4.98e-17`.

| `t_+` | `[4,7]` | `[3,8]` | `[2,9]` | `[1,10]` |
|---|---|---|---|---|
| 4 | `0.0175` | `0.4022` | `0.4226` | `0.4531` |
| 20 | `0.4703` | **`1.0712`** | `0.7935` | `0.0553` |
| 40 | `0.1809` | `0.9038` | `0.8960` | `0.1279` |
| 200 | `0.0566` | `0.5397` | `0.5660` | `0.3797` |

(`Σ|ν|p`.)  Support mass at `|ν|>3`: worst `9.13e-13` at `t_+=4`.
**Every entry of §5's sweep table is correct**, and the sweep maximum
`1.0712` at `t_+ = 20`, `W = [3,8]` is exactly my r3 M3(b) firing value,
independently reproduced.  m1/n5/LD-C7's fenced digits are untouched.

**(iii) The F1 counterexample, re-run** (`chi.py`): `ℂ²⊗ℂ³`,
`S^z = σ^z/2 ⊗ 𝟙_3`; span rank of length-2 products `= 4 = χ²` (injective),
transfer spectrum `1, 1/3`, bond Schmidt spectrum `(0.5, 0.5)` so `χ = 2`,
`ω_α(S^z) = +1/2`, `ω_α((S^z−s)²) = 0` exactly so (K-TAIL) at `C_K = 0`,
`e^{2πiS^z} = −𝟙` so D26(INT) at `κ = 1/2`.  Cell (D)'s REFUTED clause is
correct as transplanted.

**(iv) Checker runs, measured here.**  `python3 -O` green → **exit 0**,
52.3 s; `--red` → **exit 1, RED-OK, 23/23**, 95.0 s (23 registered modes, 30
"broken as registered" lines).  Every exit path in §5's 23-row table
reproduced verbatim, including the two new ones (`−1.997e-04 within 3.0 at
T=20`; `mass 3.742e-02 at |ν|>3`) and the changed one (`c6-moving` now
`12.4024 > 1.2 at |W|=17`).  No bare `assert`.  Spec/code lockstep exact.

**(v) The cells, machine-diffed against my r3 §8.**  After unescaping
`\|`→`|` and collapsing whitespace, all four **statement** cells are
character-for-character identical to r3 §8(A)--(D) (lengths 3415, 3240,
2313, 2335 — verdict and shard agree exactly).  depends-on, proved-in and
tested-in are identical too; the only delta anywhere is the appended
"(pending L6 loop)" on each status, which the lane discloses and the
orchestrator drops.  **The transplant claim is true.**

---

## 1. FATAL

**None.**  The r3 FATAL is retired.  See §5 items 1--4.

---

## 2. MAJOR

### M1 (MAJOR) — §5's unreached list is advertised as a COMPLETE enumeration and omits the two gates the r4 repair itself added.  Neither LD-C5b's `T`-stability gate nor LD-C6's `t_+`-sweep gate is reached by any registered mutation; I fired both on copies

**(a) Location.**  `theory/ace-ld.md` §5, "**Honest unreached rows — COMPLETE
enumeration (r4, per ace-ld-r3 M3: every gate or guard reached by no
registered mutation is listed …)**" (the ten-item list); the same claim in
`theory/checks/ace_ld_check.py` module docstring, bullet 5 ("the complete
unreached-gate list (r3 M3) live in the spec, section 5 …; each unreached
gate is listed with its shadowing gate named");
`theory/ace-ld-r4-response.md` row M3(i) ("§5's unreached list is now a
COMPLETE enumeration (10 items)").  The gates: `check_c5b`'s
`require(spread < C5B_LR2_STAB, …)` and `check_c6`'s sweep loop
`for tplus in C6_SWEEP: … require(mom <= C6_MOM_BOUND, … sweep gate …)`.

**(b) My computation** (instrumented copy `r4mut/trace.py`, a `REACHED` set
tagged at every gate; then teeth tests on two further copies).

*Exit paths, per mode, measured:*

| mode | gates actually evaluated | dies at |
|---|---|---|
| `c5b-flat` | `C5b-WEDGE` | wedge |
| `c5b-concentrated` | `C5b-WEDGE` | wedge |
| `c5b-nobarrier` | `C5b-WEDGE`, `C5b-CESARO-FLOOR` | Cesàro floor |
| `c6-static` | `C6-MOMENT`, `C6-SUPPORT`, `C6-LIVENESS` | liveness |
| `c6-moving` | `C6-MOMENT` | first moment |
| `c6-weaktransit` | `C6-MOMENT`, `C6-SUPPORT` | support |

`C5b-STABILITY` and `C6-SWEEP` appear in **no** row.  They are the only two
gates in the file with that property, and neither is in §5's list.

*Both have teeth — I fired them.*  (1) `C6_MOM_BOUND = 1.0` on a copy: gate
(a) passes at `t_+ = 4` (`0.453`) and the **sweep** fires —
`LD-C6: first moment 1.0712 > 1.0 at W=[3,8], t_+=20 (sweep gate …)`.  So
the sweep is *not* subsumed by gate (a) and is exactly the repair r3 M3(iii)
asked for.  (2) `C5B_LR2_TS = (20.0, 256.0)` on a copy: the floor passes at
both spans (`−3.3592`, `−3.2618`) and the **stability gate** fires —
`double-Cesaro defect not T-stable: values -3.3592, -3.2618 spread 9.741e-02
>= 0.02`.

*And the sweep is worse than unreached on the mutant battery.*
`C6BarrierAdapter.c6_laws` ignores `tplus` and returns one cached law set, so
on every registered `c6` mutant the sweep would re-check the identical
numbers four times — the campaign's no-op shape.  This is disclosed in the
code docstring and nowhere in §5.  It does not make the gate a no-op on
green (see (b)(1)), but it means the sweep's evidence is **green-side only**.

**(c) FIX DEMAND.**  Add two items to §5's list — "11. `LD-C5b`'s
`T`-STABILITY gate: reached by no registered mutation (`--red-c5b-nobarrier`
dies at the Cesàro floor at the first span); teeth confirmed on a copy at
spans `(20, 256)`, firing at spread `9.741e-02`." and "12. `LD-C6`'s
`t_+`-SWEEP gate: reached by no registered mutation (every `c6` mutant dies
at the first-moment, support or liveness gate), and on the `c6` mutant
battery the adapter's protocol time is fixed so the sweep re-checks one
cached law set; teeth confirmed on a copy with the bound at `1.0`, firing at
`1.0712` while gate (a) passes at `0.453`." — and drop the word COMPLETE
from §5 and from the checker docstring unless the list is exhaustive.

**(d) SURVIVING WEAKER STATEMENT — and it is a real advance.**  The r3 M3
disclosure gap is *mostly* closed and I fence what is there: the ten listed
items are correct, I re-derived each shadowing relation, and items 4 and 5
(the two I fired on a copy in r3) are handled exactly right — item 5 is
*removed* from the list because the reorder genuinely makes `--red-c6-moving`
reach the first-moment gate (measured `12.4024 > 1.2 at |W|=17`), and the
support gate is genuinely re-armed by the new `--red-c6-weaktransit`
(measured `3.742e-02`).  The time-tuned threshold is genuinely fixed: `1.2`
sits above a *recorded* sweep maximum `1.0712` that I reproduced from my own
ED.  All three M3 demands are met on substance.  What fails is only the
completeness *sentence*, at the two gates the repair added.

---

### M2 (MAJOR) — the promotion cells still carry symbols bound nowhere in `definitions.md`, `notation.md` or `claims/CLAIMS.md`.  `p_tr` is used in a POSITIVE clause of cell (B).  My r3 §8(E) audit asserted otherwise and MP-4's preamble reproduces that assertion

**(a) Location.**  `theory/verdicts/ace-ld-r3.md` §8(E), "Every symbol used
below is bound in `definitions.md` / `notation.md` or is **defined inline in
the cell itself**" and its two enumerations — **mine, and wrong**; reproduced
verbatim as the MP-4 preamble in `theory/ace-ld.md` **MP-4** ("All other
symbols the MP-1 cells use are either already bound — per the §8(E) audit:
… — or defined inline in the cells themselves (…)"); consumed by **MP-1**
row `ACE-LD-obst-prime`, in the clause "Mechanism (mean escape gives
`θ_{tr} = p_tr`) uses only the mean tail densities of H-MQG(2)/D13(a): no
variance hypothesis, no `(E-TAIL)`, `(V-ch)` or `(V-in)`, no `σ_L ≠ σ_T`,
…".

**(b) My computation** (exhaustive, not sampled).  I extracted every
backticked code span from the four cells — 123 distinct spans — reduced them
to atomic identifiers, and grepped each against all three single sources.

*Bound, verified one by one:* `S^z`, `S^z_x`, `spec S^z`, `κ` (D26);
`s`, `s_α`, `s_β`, `𝔛_W`, `δx`, `X_1` (D13(a),(c) + notation);
`Q̂_{W,c_0}` (notation `Q̂_{W,c}` row + D27 + MI (IDX.1));
`κ_{W,c_0}` (notation, M-INDEX-fin's cell); `λ̃` (notation, D1(c));
`𝒦_{αβ}`, `ω_α`, `ω_β`, `τ_x`, `𝔄_loc` (D9(a), D2(a), notation);
`p_{W_m}(ν)`, `ω^±_{W_m}`, `𝒟_{W,t_-}`, `(LR1)`--`(LR3)` (D27 §1--3, verified
in the text at `definitions.md:1189--1210`); `N_T`, `⟨N_T⟩` (D14);
`Δ`, `q = Δ−√(Δ²−1)`, `H_kink` (D16 + notation `H_{\rm kink}` row);
`χ` (D1, D2(a)); `v_M`, `v_K`, `D28(4)` (D28 clause 4, verified);
`q_L`, `q_T` (CLAIMS.md M-quant-G/AC-EX rows); `H-AD-G`, `M-quant-G`,
`AD3-ex`, `M-INDEX-fin`, `M-INDEX-spec`, `M-INDEX-LA-strong`,
`M-INDEX-LA-folium`, `K1`, `K2`, `K4` (CLAIMS.md rows — I opened each);
`H-MQG(1)--(3)`.  *Defined inline in the cells:* `K = [ℓ,r]`, `d_W`, `D_x`,
`C_K`, `ε_Q`, `q_φ`, `M_0`, `Π_x^{(m)}`, `q_leg`.
**Every D-number cited by the cells resolves**: D2(a), D9(a), D13(a),(c),
D14, D16, D17, D18(AD1)--(AD4), D26(INT), D27(LR1)--(LR3), D28(4).  I opened
each in `definitions.md`.

*Unbound, all in cell (B):*

- **`p_tr`** — `grep -F` over `notation.md`, `definitions.md`,
  `claims/CLAIMS.md`: **0 hits in all three.**  Not defined inline either.
  It is defined only in the shard, at `⟨1⟩5.⟨2⟩5` ("the kink has transited to
  the right of `W_m` with weight `p_tr`").  A `claims/CLAIMS.md` reader
  cannot resolve it.  This is a **positive** clause of the row, not a
  disclaimer.
- **`(E-TAIL)`, `(V-ch)`, `(V-in)`, `σ_L`, `σ_T`** — 0 hits in all three.
  These are r1-local hypothesis names, withdrawn from the shard's live
  content in r2, surviving only in a historical notice.  They occur in the
  cell only inside a *negative* list ("no variance hypothesis, no (E-TAIL) …")
  so no claim depends on resolving them — but the row still ships five
  unresolvable tokens.
- `ϱ_{AKLT}` (cell D) is named, not defined; it is self-describing and
  standard, so I let it stand — recorded as n7, not demanded.

Note `S_{NR}`, which my r3 §8(E) listed among the inline symbols, does **not**
occur in any cell (it is MP-6 text); that entry was harmless over-listing.

**(c) FIX DEMAND.**  In cell (B), bind `p_tr` inline and mark the retired
hypotheses as retired — the two edits are in §8(B) below, verbatim; and MP-4's
preamble must not repeat "every symbol … is bound" until the corrected cell is
the one being described.

**(d) SURVIVING WEAKER STATEMENT — and precondition 2 is still discharged.**
The precondition as I worded it was that `𝒬_{c_0}`, `(K-TAIL)`, `(K-Q)`,
`(M-ESC)` and `θ_{tr}` be bound.  **MP-4 binds exactly those five and nothing
else**, in three rows, at an insertion point whose anchors I resolved by
substring: the table header "ML4 / ML5 / M-quant (added at the freeze with the
summit shards)" (`notation.md:260`), the `` `δx` (asymptotic) `` row (line 290)
and the `` `Γ_K`, `Γ_{M,γ}` `` row (line 291) are adjacent, in that order, so
the insertion point is unique and well posed; the `μ_∞^α` overload anchor
resolves too (line 289, carrying `(2π)^{-1}∫e^{-iθν}\|tr(V_θr)\|²dθ` — the
exact string MP-4 quotes) and is in the same table.  I confirmed by grep that
none of the five is currently bound anywhere, that `𝒬` collides with nothing
in `notation.md`/`definitions.md`, and that MP-4 touches no frozen row.
**MP-4 is correct and is a MERGE.**  The residue is five extra tokens my own
audit failed to enumerate, and §8 fixes them.

---

## 3. MINOR

**m1 (MINOR) — cell (A)'s tested-in describes a checker run that no longer
exists.**  *(a)* `theory/verdicts/ace-ld-r3.md` §8(A) tested-in, "`--red` exit
1, RED-OK **21/21**, exit paths tabulated in the shard §5 and re-run
independently in ace-ld-r3.md n3"; carried into `theory/ace-ld.md` MP-1 row
`ACE-LD-eps`.  *(b)* Measured this round: **23/23**, and §5's table has 23
rows.  A row merged with "21/21" points at a 23-row table.  *(c)* Take §8(A)
below (two tokens change).  *(d)* Everything else in the cell is correct and
re-measured: `4.45e-02 … 4.05e-04`, `0.2089/0.2087/0.2083`, `q = 0.208712`,
`C_K = 0.209`, per-site ratio `0.20871` both sides.  **This is the lane's own
disclosure and it was right to flag it.**

**m2 (MINOR) — cell (B)'s tested-in ships two caveats that the same revision
repairs, understating the evidence.**  *(a)* r3 §8(B) tested-in, "Caveats
recorded per ace-ld-r3.md M3: LD-C6's first-moment gate is reached by no
registered mutation (the support gate shadows it) and its threshold 1.0 is
tuned to `t_+ = 4` …"; carried into MP-1 row `ACE-LD-obst-prime`.  *(b)* Both
are now false: `--red-c6-moving` reaches the first-moment gate (measured exit
path `first moment 12.4024 > 1.2 at W=|W|=17`) and the threshold is `1.2`,
above the recorded sweep maximum `1.0712` which I reproduced independently.
The true residual caveat is M1's (the sweep gate is unreached).  *(c)* Take
§8(B) below.  *(d)* The rest of the cell — LD-C5's `≤ 3.2e-6`, the two-atom
support, `|r|² = 0.2704`, `|t|² = 0.7296`, "neither certificate exhibits an
(M-ESC) state" — is correct and re-measured.  **Also the lane's own
disclosure.**

**m3 (MINOR, L5) — cell (D)'s proved-in carries a condition this revision
discharges.**  *(a)* r3 §8(D) proved-in, "`theory/ace-ld.md ⟨1⟩4.⟨2⟩9(b),
once ⟨3⟩3's χ=1 clause is replaced by the sharp-charge clause per ace-ld-r3
F1`"; MP-1 row `ACE-LD-sharp`.  *(b)* ⟨3⟩3 now proves the sharp-charge form
outright (I read it: `ω_γ(Π_x^{(m)}) = δ_{m,s_γ}`, `s_γ ∈ spec S^z`, the
spin-1 exclusion, and the retired clause quoted and struck).  Merging the
conditional pointer would put a discharged instruction into the DAG.
*(c)* Take §8(D)'s one-line proved-in below.  *(d)* The cell's statement and
status are correct and stay verbatim.

**m4 (MINOR, lockstep) — HONEST STATUS attributes a `T = 80` measurement to
the checker, which does not make it.**  *(a)* §4, "Merely evidence", "the
**double-Cesàro defect `−3.3592`**, stable across `T = 20, 40, 80` (checker)
and `T = 20…200` (ace-ld-r3 M2(b))".  *(b)* `C5B_LR2_TS = (20.0, 40.0)` —
two spans.  The `T = 80` value is a proposer scratch run (r4-response
"Independent pre-repair reproduction"), not a gate.  The *fact* is true — I
measure `−3.359207` at `T = 80` — but the attribution is not.  *(c)* Write
"`T = 20, 40` (checker), `T = 80` (proposer scratch; independently confirmed
ace-ld-r4 §0(i)) and `T = 20…200` (ace-ld-r3 M2(b))".  *(d)* The number and
the stability claim survive: I confirm `−3.3592` at every `T` from 20 to 200.

**m5 (MINOR, L4) — HONEST STATUS still cites a stale `notation.md` line
number for the `θ` overload, and it now points at the wrong row.**  *(a)* §4,
"Honest defects", "(iv) The shard-local symbol `θ` of (M-ESC) collides with
the frozen twist variable `θ` of `notation.md` line 271 (r2 n2)".  *(b)*
`notation.md:271` is the `` `𝔠_h(O)` `` row (the contact first jet).  The
twist-`θ` row is line **289** (`` `Q_W^α`, `Q_W^β`, `μ_∞^α` ``).  MP-4 was
string-anchored for exactly this reason and got it right; HONEST STATUS was
not updated with it.  *(c)* Replace "line 271" by "the `μ_∞^α` row" — the
same content anchor MP-4 uses.  *(d)* The overload is real and `θ_{tr}` is the
right merged name; only the pointer is stale.

**m6 (MINOR) — the double-Cesàro protocol has an undocumented validity
ceiling, and the published stability range sits just inside it.**  *(a)*
`theory/checks/ace_ld_check.py` `C5B_LR2_TS` / `_c5b_cesaro_defect` (no wrap
guard); `theory/ace-ld.md` §5 LD-C5b gate (b), "the critic finds the same
value out to `T = 200`".  *(b)* The protocol evolves to `|t| = 2T` at group
velocity `\|v\|_max = 2` on a ring of `N = 2048`, so the excitation re-enters
the window once `4T ≥ N/2 = 1024`, i.e. `T ≥ 256`.  Measured, on the checker's
own model and on mine independently: `T=200 → −3.3594`, `T=250 → −3.3593`,
`T=256 → −3.2618`, `T=260 → −2.8319`, `T=275 → −2.2841`, `T=300 → −1.2620`.
The separator drifts the same way (`+2.07e-02` at `T=300`, against `1e-14`
at `T=200`).  At the shipped spans `(20, 40)` there is no contamination and
every gate is sound; but `C5B_LR2_TS` is a bare constant with no guard, and a
future edit to `T = 300` would make the *green* model fail the floor.
*(c)* Add a one-line comment/guard at `C5B_LR2_TS`: "valid only for
`4T < N_BAR/2`, i.e. `T < 256`; beyond that the ring wraps and the defect
drifts (measured `−3.2618` at `T=256`, `−1.2620` at `T=300`)", and in §5
qualify "out to `T = 200`" as "out to `T = 200`, the ring-wrap horizon being
`T = 256`".  *(d)* The shipped measurement and the `T = 20…200` stability
claim are correct and I fence them.

**m7 (MINOR) — the `t_+`-sweep gate's `t_+ = 4` element is a literal
re-check of gate (a).**  *(a)* `check_c6`, `rows_t = rows if tplus ==
C6_TPLUS else m.c6_laws(tplus)`.  *(b)* At `tplus = 4.0` the sweep loop
re-evaluates `require(mom <= C6_MOM_BOUND)` on the identical cached `rows`
gate (a) already passed — one of four sweep iterations carries no
information.  Not harmful (the other three are live and I fired the gate at
`t_+ = 20`), but it is the "deductive subsumption between gates" item.
*(c)* Skip `C6_TPLUS` in the sweep loop, or say in §5 that the sweep's
`t_+ = 4` element is the same evaluation as gate (a).  *(d)* The sweep's
evidential content — `Σ|ν|p ≤ 1.2` at `t_+ ∈ {20,40,200}` — is real and
independently reproduced.

---

## 4. NOTE

**n1 (NOTE — credit; the F1 retirement is complete and I checked every
site).**  All ten F1(a) echo sites carry the sharp-charge form: the file
header ROLE comment; proposer-status item 4 (`§0`, lines 66--79); the r1
deletion notice's `(E-TAIL)` equivalence (lines 88--95, with the correct
observation that every instantiated model has simple `s_γ`, so the emptiness
argument is unaffected); THEOREM ACE-LD-ε **SCOPE** (238--247); THEOREM
ACE-LD-sharp `§0` statement + its "NOT PROVED — REFUTED" block (248--287);
⟨1⟩4.⟨2⟩9(a)'s corrected equivalence note (914--931); ⟨2⟩9(b)'s proof head
(932--937); ⟨3⟩3 (959--971, retired clause quoted and struck); the ⟨2⟩9
closing corner paragraph (971--980); HONEST STATUS "Proved" (1169--1178),
"Proved conditionally" forced-scope (1206--1213) and the new "Refuted /
withdrawn" entry (1250--1262); MP-1's eps row and the new `ACE-LD-sharp` row.
`grep` for `χ=1` / "product state" / "fully polaris" returns **no** unhedged
occurrence anywhere.  The id `ACE-LD-χ` is not reused.  **The `±s ∈ spec S^z`
clause and the spin-1-at-`s=1/2` exclusion survive verbatim in every one of
them**, and the surviving conditional (simple `s_γ` ⟹ `χ=1`) is kept as a
corollary, exactly as F1(c) demanded.

**n2 (NOTE — credit; the fence held).**  I diffed `HEAD~1..HEAD` on
`theory/ace-ld.md` (519 insertions, 181 deletions).  Every deletion is a
site F1(a), M1, M2, M3 or an `m`-item names.  The r3 §5 fence's mathematical
items are untouched: ⟨2⟩1--⟨2⟩2's derivation is retained *unchanged* with the
n1 triangle-inequality remark added beside it ("the square expansion is
retained as the verified derivation, unchanged"); LD-ID ⟨3⟩1, ⟨3⟩2, ⟨3⟩4 are
byte-identical; ⟨3⟩3 gains only m2's displayed leaf; LD-MONO's ASSUME and
proof are untouched and only the gloss takes M1's quantifier.  **No fenced
step was reworked.**

**n3 (NOTE — credit; the corrected LD-C5b gate is not a no-op, and I proved
it by moving the data).**  `_c5b_cesaro_defect` compares `Σ_b⟨b_{t_+},Q̂
b_{t_+}⟩` against `⟨ψ(t_+),Q̂ψ(t_+)⟩` — the cross terms, not two textually
identical expressions.  It returns `−3.3592` on the shipped state and
`−1.997e-04 → −6.4e-14` on a state satisfying LR2, i.e. it **moves with the
physics**, which is what the standing obligation asks for.  My independent
implementation and the checker's agree to six decimals at `T = 20, 200, 250,
300` — so the pinching is implemented correctly as well as gated correctly.

**n4 (NOTE — credit; the separator is the strongest item of the round).**
The `V_0 = 0` straddling packet passes gate (a) at `8.3868` — 8.4× the floor,
and *larger than green's* `6.0832` — and dies at gate (b) at `−1.997e-04`.
That is a genuine separation of "`𝒟` acts" from "LR2 fails", registered as a
red mode, built from a physical model change rather than a constant flip.
It is exactly what r3 M2(c) demanded and it is the right kind of red mode:
a **data/model** mutation, not a code mutation.  Distinctness checked:
`c5b-nobarrier` (straddling, `V_0=0`) is not bit-equivalent to
`c5-nobarrier` (packet 300 sites left, `V_0=0`) — different battery,
different exit path; `c6-weaktransit` (`V_0=10`) is not bit-equivalent to
`c6-moving` (`V_0=1.2`) — different exit gate.

**n5 (NOTE — credit; the correct number is now everywhere it should be).**
`−3.3592` appears in §5 gate (b), HONEST STATUS "Merely evidence", the
checker docstring and the green log line; `6.083` survives only where it is
explicitly labelled "certifies ONLY that `𝒟` acts".  The green log line
"LR2 fails pointwise AND on average here (measured)" is **gone** — I ran the
checker and read the line.  The r3 sentences it replaced are quoted in §5 as
deleted, which is the right kind of record.

**n6 (NOTE — the wedge/Cesàro pair is genuinely two-sided).**  Neither gate
implies the other, and both directions are witnessed: `c5b-flat` and
`c5b-concentrated` pass the Cesàro side vacuously and die at the wedge
(`1.776e-15`, `4.260e-11`); `c5b-nobarrier` passes the wedge and dies at the
Cesàro floor.  No subsumption.

**n7 (NOTE — two small things I am recording, not demanding).**  (i) Cell
(D)'s depends-on omits `ACE-LD-eps`, though it takes (K-TAIL) from that row's
statement; this is hypothesis-sharing rather than dependency and the cell
names the source in-line ("row ACE-LD-eps"), so I leave it.  (ii) `ϱ_{AKLT}`
in cell (D) is named but not formally defined; the subscript is
self-describing and the object is standard.

---

## 5. VERIFIED CORRECT — fenced; no repair lane may churn this

Re-derived or re-run by me this round, independently of the target.
**This fence is additional to r2 §5's 14 items and r3 §5's 17, which I
re-read and confirm are untouched (n2).**

1. **The F1 retirement, at all ten sites** (n1), including the preserved
   `±s ∈ spec S^z` clause and the spin-1-at-`s=1/2` exclusion.
2. **THEOREM ACE-LD-sharp's proof** ⟨1⟩4.⟨2⟩9(a)--(b): ⟨3⟩1 (D9(a) plain
   boundary condition `ϱ(τ_n(O)) → ω_{α/β}(O)`, verified at `definitions.md:386--392`), ⟨3⟩2
   ((K-TAIL) diagonal + D2(a) translation invariance of the injective-MPS
   vacuum — the quantifier "every site" is genuinely delivered), ⟨3⟩3
   (Cauchy--Schwarz ⟹ `ω_γ(Π_x^{(m)}) = δ_{m,s_γ}` ⟹ `s_γ ∈ spec S^z`).
   Correct at every step.
3. **The `χ=1` counterexample**, re-run (`chi.py`, §0(iii)): injective,
   `χ = 2`, transfer gap `1/3`, `D_xφ ≡ 0`, D26(INT) at `κ = 1/2`.
4. **M1's quantifier restoration**, in both places — MP-3(ii) and ⟨2⟩7's
   LD-MONO gloss now carry "whose annulus `W'∖W` carries no escaped charge —
   equivalently, every `W'` the leg has already passed beyond", with the
   `2s = 1.0000` vs `4.25e-22` measurement recorded.  The lemma as ASSUMEd is
   untouched, as M1(d) required.
5. **m1's per-clause ASSUME split** in LD-ID and the matching HONEST STATUS
   split; **m2's displayed leaf** at ⟨3⟩3
   (`‖Σ_{x∉W}D_xΨ_t‖ ≥ |⟨Ψ_t,Σ_{x∉W}D_xΨ_t⟩|`); **m3's** named condition
   (H-AD-G) in all three places plus the disjoint-classes sentence;
   **m4, m6, m7, m8** as claimed (I checked each site; `--table` is gone from
   the docstring and `argparse` registers no such flag).
6. **m5's re-citation is correct and the address resolves**:
   `theory/lr-d16.md` THEOREM (LRD-3) is at line 692, inside `⟨1⟩5.⟨2⟩7`
   (which spans 679--714), and states `(NR) ⟹ D27(LR3)` with tail
   `2S_{NR}/M`.  `theory/verdicts/lr-d16-r2.md` is the current verdict (no
   r3 exists).  The composition `(M-ESC) ⟹ ¬(NR)` is direct.
7. **The LR2 republication, every figure** (§0(i)): `6.0832`, `−3.3592` at
   `T = 20/40/80/120/200`, `−8.3868`, `−1.997e-04`, `0.8563/0.0170/0.1267`
   at `t_- = −80` and `−400`.
8. **The LD-C6 sweep table, every entry** (§0(ii)), the support mass
   `9.13e-13`, the liveness `0.453`, and the sweep maximum `1.0712` at
   `t_+ = 20`, `W = [3,8]`.
9. **The LD-C7 battery, unchanged** from r3's independent full-`2^{12}`
   rebuild: sector energies `≈ 5e-17`, defects `4.45e-02 … 4.05e-04`, ratios
   `0.2089/0.2087/0.2083`, `C_K = 0.209`, per-site ratio `0.20871` both sides.
10. **The checker's green and red runs**: exit 0 (52.3 s), exit 1 RED-OK
    23/23 (95.0 s); all 23 exit paths reproduced verbatim.
11. **The four cells are byte-identical to r3 §8(A)--(D)** (§0(v)), the only
    delta being "(pending L6 loop)".  The machine-transplant claim is true.
12. **MP-4 binds exactly the five §8(E) symbols**, its three anchors all
    resolve, none of the five is bound anywhere today, `𝒬` collides with
    nothing, and no frozen row is touched (M2(d)).
13. **Reliance audit, clean.**  No cell or step relies on a REFUTED row:
    `M-INDEX-LA-strong` is cited only as *not contradicted* (correctly — the
    cells construct a limit **vector** on a (K-TAIL) state, not a sector
    operator); no use of ML4-Ward (9) at `n≥2`; no Bethe hypothesis; no
    appeal to `𝒮_W` being nonempty at `ρ≠1/2`.  Dependency statuses
    verified in `claims/CLAIMS.md`: M-INDEX-fin PROVED, M-INDEX-spec PROVED
    (conditional), M-quant-G PROVED (conditional), AD3-ex CONJECTURE, K1/K2
    PROVED, K4 CONJECTURE, M-INDEX-LA-folium CONJECTURE — every status the
    cells assert about them is right.
14. **Nothing is merged yet**: `claims/CLAIMS.md` contains no ACE-LD row, so
    the promotion is genuinely pending and the cells are the whole delta.

---

## 6. Register comparison against the nearest PROVED rows

The nearest adjudicated rows — **M-INDEX-fin**, **M-INDEX-spec**,
**M-quant-G**, **AC-EX** — each carry an "Adjudicated scoping (verbatim)"
paragraph that (i) names every hypothesis, (ii) states the conclusion as an
explicit conditional, and (iii) closes with what is *not* claimed, including
the negative facts that hurt.

All four cells do all three, and the two register gaps I recorded in r3 are
closed: the eps row's one false positive clause (`χ=1`) is gone and replaced
by the sharp-charge form with the REFUTED disclosure attached, and the obst
row now names H-AD-G as M-quant-G's condition and says the two fences concern
**disjoint** state classes.  Cell (B)'s closing "**No model or state realising
`(M-ESC)` is exhibited anywhere in this corpus** … until a witness exists it
makes no clause of any class theorem necessary" is a harder self-limitation
than M-INDEX-spec's, and cell (D) volunteers its own refutation.
**On register these four rows are at or above the standard of every PROVED
row in the DAG.**  The one residue is M2's five unresolvable tokens in cell
(B), which is a resolvability defect and not a register defect — no
adjudicated row in the corpus ships a symbol bound nowhere, and after §8(B)
these will not either.

---

## 7. The two §8(E) preconditions — ruling

**Precondition 1 (F1 applied shard-wide, in the same revision): DISCHARGED.**
All ten sites, verified individually (n1); no unhedged `χ=1` survives; the
retired clause is quoted and struck rather than silently deleted; the shard
and the cells now say the same thing at the same strength.  The revision that
carries the cells is the revision that carries the correction.

**Precondition 2 (MP-4 binds `𝒬_{c_0}`, (K-TAIL), (K-Q), (M-ESC), `θ_{tr}`,
and merges with or before MP-1): DISCHARGED as worded.**  Exactly those five,
in three rows, string-anchored to an insertion point I resolved by substring
(all three anchors present and mutually adjacent in the right order),
collision-free, no frozen row touched, and marked as MP-1's precondition in
both MP-1's preamble and MP-4's.  **But it is discharged only as *I* worded
it**: the audit sentence MP-4's preamble reproduces — mine — overstates, and
five further tokens in cell (B) are bound nowhere (M2).  That is a defect in
my r3 text, not in the lane's execution, and §8(B) repairs it.  With §8(B)
applied, the DAG takes no unbound symbol and no unresolvable D-number.

---

## 8. Promotion rulings — GO, with three corrected cells

**GO on all four.**  Apply the r3 §8(A)--(D) cells as the shard has them,
with exactly the substitutions below.  Everything not quoted here is
unchanged and stays verbatim.

### (A) `ACE-LD-ε` — **MERGE.**  Replace the *tested-in* cell only (m1)

> theory/checks/ace_ld_check.py LD-C7 (green exit 0; --red exit 1, RED-OK 23/23, exit paths tabulated in the shard §5 and re-run independently in ace-ld-r4.md §0(iv)).  Gates (b)--(c) certify the conclusion's λ̃^{d_W} rate (defects 4.45e-02 … 4.05e-04, ratios 0.2089/0.2087/0.2083 against q = 0.208712); gate (e) certifies the HYPOTHESIS (K-TAIL) itself site-by-site, and by Cauchy--Schwarz on the self-adjoint D_x the on-site clause is equivalent to the full same-side clause, so (e) certifies (K-TAIL) in full (ace-ld-r3.md n1).  No gate bears on (K-Q), on the infinite-volume statement, or on the sharp-charge corollary, which is exact algebra.

Statement, status, depends-on and proved-in: **unchanged, verbatim.**

### (B) `ACE-LD-obst′` — **MERGE**, with two edits in the statement (M2) and a replaced tested-in (m2, M1)

**Edit 1** (statement).  Replace the string

> `Mechanism (mean escape gives `θ_{tr} = p_tr`) uses only the mean tail densities of H-MQG(2)/D13(a): no variance hypothesis, no `(E-TAIL)`, `(V-ch)` or `(V-in)`, no `σ_L ≠ σ_T`, no channel projections, no wave operators, no D28.`

by

> `Mechanism (mean escape gives `θ_{tr} = p_tr`, where `p_tr` is the outgoing-Cesàro weight with which the kink has transited beyond `W_m` and `1−p_tr` the weight with which it stayed) uses only the mean tail densities of H-MQG(2)/D13(a): no variance hypothesis, none of the retired r1 hypotheses `(E-TAIL)`, `(V-ch)`, `(V-in)` (withdrawn in r2 and defined nowhere outside the deletion notice of `theory/ace-ld.md` §0), no channel-variance separation `σ_L ≠ σ_T`, no channel projections, no wave operators, no D28.`

**Edit 2** (tested-in).  Replace the whole cell by

> theory/checks/ace_ld_check.py LD-C5 — incoming concentration ≤ 3.2e-6 at every window and the exact two-atom TPM support {ν = 0, ν = −|W|} including the ν = 0 atom, with weights matching the independently measured |r|² = 0.2704, |t|² = 0.7296, on a one-particle barrier model; its identity and tail-floor gates are disclosed consequences of those facts, not independent evidence.  LD-C6 — kink+magnon bounded-transport contrast on the D16 battery at the fixed protocol time t_+ = 4 (support: mass at |ν| > 3 below 9.1e-13; first moment ≤ 0.453), with the first-moment bound 1.2 held across a recorded t_+ sweep {4, 20, 40, 200} whose maximum is 1.0712 (t_+ = 20, W = [3,8]).  The ace-ld-r3 M3 caveats are REPAIRED in r4 and re-measured independently (ace-ld-r4.md §0(ii),(iv)): the first-moment gate is evaluated first and IS reached (--red-c6-moving, 12.4024 > 1.2 at |W| = 17), the support gate is armed (--red-c6-weaktransit, mass 3.742e-02 at |ν| > 3), and the threshold is keyed to the recorded sweep rather than to t_+ = 4.  Residual caveat (ace-ld-r4.md M1): the t_+-SWEEP gate itself is reached by no registered mutation — every c6 mutant dies at the first-moment, support or liveness gate, and on the c6 mutant battery the adapter's protocol time is fixed so the sweep re-checks one cached law set — so the sweep is green-side evidence only; its teeth were confirmed on a copy, firing at 1.0712 with the bound at 1.0 while gate (a) passes at 0.453.  **Neither certificate exhibits an (M-ESC) state, and no gate bears on claims (a)--(c), which are proved, not tested.**

Status, depends-on and proved-in: **unchanged, verbatim.**

### (C) `LD-ID` — **MERGE exactly as the shard has it.**  No change

Statement, status, depends-on, proved-in and tested-in all stay verbatim.  I
re-verified the identity's algebra and both corollaries' hypotheses this
round; the r3 numbers it cites (`max|LHS−RHS| = 0.000e+00` over six windows
and all `2^{12}` basis states; `‖(Q̂_{W'}−Q̂_W)φ‖ = 2s` at every padding)
stand.

### (D) `ACE-LD-sharp` — **MERGE.**  Replace the *proved-in* cell only (m3)

> theory/ace-ld.md ⟨1⟩4.⟨2⟩9(b)

The condition "once ⟨3⟩3's χ=1 clause is replaced by the sharp-charge clause
per ace-ld-r3 F1" is **discharged by this revision** and must not enter the
DAG.  Statement, status, depends-on and tested-in: **unchanged, verbatim.**

### (E) Merge preconditions — both discharged; two conditions on the ORDER only

1. **MP-4 merges with or before MP-1.**  Unchanged from r3 §8(E), and MP-4
   is correct as drafted (string anchors verified; exactly five symbols).
2. **The three cell substitutions above are applied at merge.**  Without
   §8(B) Edit 1 the DAG takes an unbound `p_tr`; without §8(A)/§8(B) Edit 2
   and §8(D) it takes three stale evidence descriptions.  None of these
   blocks the *statements*, which are all correct as they stand.

**M1 does not block the merge** — with §8(B)'s residual caveat in place the
merged row states the reachability position honestly.  M1 is a work order on
`theory/ace-ld.md` §5 and the checker docstring, to be discharged in the same
commit or the next.

---

## 9. Ruling on MP-1 through MP-6

- **MP-1** — **MERGE**, with the three §8 substitutions.  `ACE-LD-abs`
  unchanged and still correct (no depends-on, per r1 m5).
- **MP-2** — **MERGE as written**, third approval; unchanged since r3.
- **MP-3** — **MERGE**, hold released.  Clause (ii) now carries M1(c)'s
  quantifier verbatim in substance, with the refutation recorded.  Clauses
  (i), (iii), (iv) and the `ν`-orientation flag are unchanged and sound.
- **MP-4** — **MERGE**, and it remains a **precondition** of MP-1.  Anchors
  verified.  One request, not a condition: do not carry my r3 §8(E) sentence
  "every symbol … is bound" into `notation.md` — it is a critic's audit note,
  it is incomplete (M2), and it has no place in the frozen table.
- **MP-5** — **ENDORSE, fourth time.**  1785 lines against a 200--500 band.
  The split of ⟨1⟩5 into `theory/ace-ld-obst.md` is now the single highest
  value action left in this lane, and the r4 growth (+338 lines) makes it
  more urgent, not less.
- **MP-6** — **MERGE as written.**  m5 correctly applied; the (LRD-3) address
  resolves; the no-witness disclosure travels with the constraint.

---

## 10. Objection ledger

| id | severity | one line |
|---|---|---|
| M1 | MAJOR | §5's "COMPLETE enumeration" of unreached gates omits the two gates the r4 repair added — LD-C5b's `T`-stability and LD-C6's `t_+`-sweep are reached by NO registered mutation; I fired both on copies (`spread 9.741e-02`; `1.0712 > 1.0` while gate (a) passes at `0.453`), and on the c6 mutant battery the sweep re-checks one cached law set |
| M2 | MAJOR | The promotion cells carry symbols bound nowhere: `p_tr` in a POSITIVE clause of cell (B), plus `(E-TAIL)`, `(V-ch)`, `(V-in)`, `σ_L`, `σ_T` in its negative list — 0 hits each across `notation.md`, `definitions.md`, `claims/CLAIMS.md`.  **My own r3 §8(E) audit asserted otherwise**; MP-4 reproduces it |
| m1 | MINOR | cell (A)'s tested-in says "RED-OK 21/21"; the shipped checker is 23/23 and §5's table has 23 rows |
| m2 | MINOR | cell (B)'s tested-in ships the two r3 M3 caveats this revision repairs, understating the evidence |
| m3 | MINOR | cell (D)'s proved-in carries the now-discharged condition "once ⟨3⟩3's χ=1 clause is replaced" |
| m4 | MINOR | HONEST STATUS attributes `T = 80` to the checker; `C5B_LR2_TS = (20, 40)` — the fact is true, the attribution is not |
| m5 | MINOR | HONEST STATUS (iv) cites `notation.md` line 271 for the twist-`θ` overload; line 271 is the `𝔠_h(O)` row, the twist row is 289 (MP-4 already anchors it by content) |
| m6 | MINOR | the double-Cesàro protocol wraps the `N = 2048` ring at `T ≥ 256` (measured `−3.2618` at `T=256`, `−1.2620` at `T=300`); `C5B_LR2_TS` has no guard and §5 quotes "out to `T = 200`" without the ceiling |
| m7 | MINOR | the sweep gate's `t_+ = 4` element re-checks gate (a)'s cached laws — one of four iterations is deductively subsumed |
| n1 | NOTE | credit: F1 applied at all ten sites, `±s ∈ spec S^z` and the spin-1 exclusion verbatim in every one, id not reused, no unhedged `χ=1` anywhere |
| n2 | NOTE | credit: the r3 §5 fence held — diff-verified; ⟨2⟩2's derivation retained unchanged beside the n1 remark |
| n3 | NOTE | credit: the double-Cesàro gate moves with the data (`−3.3592` vs `−6.4e-14`); my implementation and the checker's agree to 6 decimals at four spans |
| n4 | NOTE | credit: the `V_0=0` separator genuinely separates — wedge `8.3868` (passes, larger than green's `6.0832`), Cesàro `−1.997e-04` (dies); a model mutation, not a constant flip |
| n5 | NOTE | credit: "AND on average (measured)" is gone from the log line; `−3.3592` is in §5, HONEST STATUS, the docstring and the log; `6.083` survives only where labelled "`𝒟` acts" |
| n6 | NOTE | wedge and Cesàro gates are mutually independent, both directions witnessed; no subsumption |
| n7 | NOTE | recorded, not demanded: cell (D)'s depends-on omits `ACE-LD-eps` (hypothesis-sharing, named in-line); `ϱ_{AKLT}` is named but not defined |

---

FAIL(M1, M2)
