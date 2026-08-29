<!-- ROLE: adversarial critic verdict, round r2, on theory/lr-d16.md,
     theory/lr-d16-r2-response.md and theory/checks/lr_d16_check.py
     (bd tns-xf4).  Protocol: briefs/critic-protocol.md incl. Standing checker
     obligations.  Brief: briefs/lr-d16-critic-r2.md.  Prior:
     theory/verdicts/lr-d16-r1.md FAIL(F1,F2,M1-M4).  Lane: this file only.
     Nothing else edited; no merge is authorised except by the explicit
     verbatim cells in §5; no commit. -->

# Critic verdict — (LR) for D16, r2 (adjudication + promotion)

**Verdict line is at the bottom.  Severity has fallen: no FATAL survives.**

Every number below was produced by me.  Where the checker's own module was
loaded it is said so explicitly; the two load-bearing numbers (the `(LRD.11)`
value and the `H_kink`/`H_XXZ` calibration) were also reproduced *from
scratch* in the full `2^N` space with no shared code.  Scratch scripts:
`indep1.py`, `indep2.py`, `indep3.py`, `indep4.py`, `eps.py`, `subsume.py`,
`mut/{mA,mB,mC,mD}.py` in the session scratchpad.

---

## 0. Headline

The lane took every retraction rather than defending anything, and that was
the right call.  **All six r1 objections are correctly disposed of at the
level of the mathematics.**  `(LR2′)` is gone, `(NR)` carries `sup_m` exactly
as specified, the class counterexample is gone, the K4-strength language is
gone *by content* and not merely by string, `⟨1⟩3` is byte-identical
(SHA-256 confirmed), and the checker went from 18 rows/10 unreachable/3 no-ops
to 17 rows all individually reachable with two of the three former no-ops now
genuine numerical certificates.

What fails is the **negative** layer — the sentences the round added while
retracting — and one merge proposal that was left untouched on my own r1
instruction and is now false because of the retraction.  Four MAJORs:

| # | one line |
|---|---|
| **M1** | **MP-4 was retained verbatim and now contradicts the round's own F1 retraction.**  Its second sentence still reads "*one clause proved in a weakened form that suffices downstream*" — the exact claim §0, ⟨1⟩2, ⟨1⟩4.⟨2⟩7 and §H item 8 withdraw.  It would write the retracted claim into `TRIANGLE.md`/`HANDOFF.md`.  **This is my error to own: r1 §4 said "MP-4: MERGE, unchanged", contradicting r1's own §0, and the lane obeyed literally.** |
| **M2** | "**(ESC) is false on the D16 state class (H3)**" is itself an unproved dynamical claim.  It needs the magnon to leave every fixed window as `|t|→∞` — a local-decay/completeness statement that ⟨1⟩2(ii) explicitly disclaims.  r1's F1(b) analytic paragraph had the same gap; I own it.  The retraction survives on the weaker ground. |
| **M3** | The checker's **two negative diagnostics C2(d) and C3(e)** — the only rows carrying the round's numerical case — are computed with the `H_kink` propagator, i.e. with the very finite-volume error the round fixed in C4(b) and which ⟨1⟩1.⟨2⟩1 forbids.  Applying the `m2` fix consistently makes **both rows FAIL**.  They also fail at `c_0=5` and at `Δ=1.2`. |
| **M4** | ⟨1⟩6.⟨2⟩4 calls `ACE-LD-obst′` "**proved**" and concludes a class theorem "**must**" carry a no-mean-transport clause.  `ACE-LD-obst′` has no `claims/CLAIMS.md` row; it is a pending merge proposal in a shard whose r2 verdict is FAIL(F1,M1–M6); and `ace-ld.md`'s own honest status records that **no model or state realising `θ>0` is exhibited anywhere in this corpus**.  The replacement for the retracted counterexample has the same defect — no witness — one notch softer. |

**None of the four touches `LR1-GEN` or `LR-D16-EDW`.**  Both rows are
promoted in §5, on my sentences.  `LR-D16` stays HOLD.

`M-INDEX-spec` is **unaffected and unimproved**, exactly as the shard says.
See §6.

---

## 1. Disposition of every r1 objection, verified by fresh recomputation

| r1 id | lane's claim | my verification | ruling |
|---|---|---|---|
| **F1** | (LR2′) WITHDRAWN, not patched | grep + read of all seven r1 sites: `⟨1⟩2` bullet renamed `(LRD-2-BND)`; §0 row rewritten; `⟨1⟩4` title, ⟨2⟩5, ⟨2⟩7, ⟨2⟩8 rewritten; §H items 6, 8 rewritten; `⟨1⟩6.⟨2⟩3` renamed `LR2-BOUND-GEN` and marked "no D16 instance"; MP-2 HOLD; MP-3's `LR-D16` HOLD.  **No surviving step, status line or merge row asserts (LR2′).**  Residue re-attributed to the `O(1)` magnon at ⟨1⟩4.⟨2⟩6 and §H item 8 (r1 m3).  Checker row C2(d) relabelled and now computes `𝒩_W²` on `t∈[−40,40]` (r1 m4). | **ADOPTED** (but see **M2** on the *reason* given, and **M3** on C2(d)) |
| **F2** | (NR) repaired with `sup_m`, same constant | (LRD.13) now carries `φ_q^{(m)}:=E_{W_m,t_-}({q})Ψ` and the explicit sentence that the *observable* is fixed and the *state* is not.  (NR) is displayed as **two numbered clauses**, the second `sup_m sup_{t_-<t_+}Σ_q‖α_{t_+}(𝒩_{W_1})E_{W_m,t_-}({q})Ψ‖²<∞`.  I re-derived the constant: ⟨2⟩2 gives `Σ_{|ν|>M}(1+|ν|)p ≤ 2Σ_{|ν|>M}\|ν\|p ≤ (2/M)Σν²p`, ⟨2⟩4 gives `Σν²p_{W_m;t_-,t_+} ≤ S_{NR}`, ⟨2⟩5 transports it by Fatou, so `sup_m Σ_{\|ν\|>M}(1+\|ν\|)p_{W_m} ≤ 2S_{NR}/M`.  **Constant unchanged and correct.**  Clause 1 is *not* implied by clause 2 (`⟨Ψ,A²Ψ⟩` and `⟨Ψ,𝒟(A²)Ψ⟩` do not dominate one another), so "two clauses" is honest and not padding.  Lockstep exact: §0, ⟨1⟩2 (LRD-3), ⟨1⟩5.⟨2⟩4/⟨2⟩7, §H item 3 all say the same at the same strength. | **ADOPTED VERBATIM IN STRENGTH** |
| **M1** | MP-1 re-proposed in the subsequence/binder form | MP-1 now reads exactly my r1 fix demand, including the added clause fixing D27(LR2)'s limit *along the same common sequence*.  I checked that reading against the consumer: `theory/memory-index.md` line 402 (⟨1⟩7.⟨2⟩1) reads it "followed by the **common subsequence**".  ✔ | **ADOPTED** → **MERGE**, §5 |
| **M2** | counterexample RETRACTED, replaced by the scoping requirement | ⟨1⟩6.⟨2⟩5 is now an explicit retraction; ⟨1⟩2's Remark and §H item 11 match; nothing downstream leans on the refutation (I grepped `ballistic`, `group velocity`, `manifold`, `recoil`, `immobile`, `θ` — all six surviving hits are disclaimers).  **But the replacement, LR3-SCOPE, over-reaches: see M4.** | **ADOPTED**, replacement defective |
| **M3** | K4-strength language removed | **CONTENT test, done by reading, not grep.**  (i) §H "Bearing on the live cross-lane obstruction" now argues only from ⟨1⟩5.⟨2⟩4 and (FN)/(LRD.5); no model-wide claim.  (ii) ⟨1⟩2's Remark now says "K1--K2 supply only that every state in their closed product-family span is stationary; exhaustiveness is K4 and is not used."  (iii) ⟨1⟩6.⟨2⟩4 no longer contains the (C-imm) clause at all, and ⟨1⟩6.⟨2⟩6 forbids the upgrade in terms.  ⟨1⟩5.⟨2⟩8's headline was also weakened from "the D16 wall carries no group velocity" to "every state in the closed span … is exactly stationary".  I checked every one of the 8 `K4` occurrences and all 6 `ballistic`/`recoil` occurrences: **every one is a fence.**  I also checked the shard does **not** import `ace-ld.md` MP-6's `θ=0`-for-D16 sentence, which is the K4-strength claim flagged in that lane's own r2 M5 — the symbol `θ` does not occur in this shard.  **What remains is supported by K1+K2 alone.** | **ADOPTED BY CONTENT** ✔ |
| **M4** | checker rebuilt, 17 rows, all reachable | Reproduced: green **exit 0**, 17/17; `--red-all` **exit 1**, RED-OK 17/17; every individual `--red MODE` **exit 1** on exactly its singleton.  Stronger than the lane claims: I re-ran every mode over the **full 17-row suite** (not just its own group) and each still produced exactly its registered singleton — no collateral, no masking.  Zero bare asserts (`grep -c '^\s*assert '` = 0), so `-O` is strict.  **The three former no-ops: two are now genuine, one is not a no-op but is deductively subsumed — §3.**  New defects: **M3**, m1, m2. | **ADOPTED**, with M3/m1/m2 |
| m1 | hygiene fixed without a false core-invariance claim | ⟨1⟩1.⟨2⟩5 now states the common finite-deviation core for `𝒬, 𝒩_W, D`, defines Heisenberg expressions as extended quadratic forms, allows `+∞`, and ⟨1⟩1.⟨2⟩4 says the squaring steps are legitimate because the operators are simultaneously diagonal and pointwise non-negative.  ✔  **Not covered: `H_{XXZ}` itself** — see m3. | FIXED, one gap left |
| m2 | C4(b) evolves with `H_XXZ` | **Verified, and it is a real repair.**  Green: `max energy drift = 1.11e−14`.  Registered mutant `c4-kink-propagator` reverts to `H_kink` and is caught **by the energy-drift conjunct** (`1.007`), not by the inequality (slack still `−1.676`) — the correct exit path.  Independent reproduction of r1's drift numbers under `H_kink`: `+0.0598` at `t=3`, `−0.3441` at `t=12`, `−0.6215` at `t=48` (r1: `+0.060, −0.344, −0.621`) ✔.  **But the fix was applied to C4(b) only — M3.** | FIXED for C4(b) only |
| m3 | residue re-attributed to the `O(1)` magnon | ✔ everywhere (⟨1⟩4.⟨2⟩5, ⟨2⟩6, §H item 8, ⟨1⟩2). | FIXED |
| m4 | C2(d) computes `𝒩_W²`, `[−40,40]` | ✔ code reads `(n_w ** 2)` and `np.linspace(-40,40,201)`; caption now says (ESC) fails.  I reproduced `G = 0.9897, 0.9651, 0.9504`, `η = 11.94, 15.72, 19.50` from scratch. | FIXED, but see M3 |
| m5 | one genuine leaf by content; mis-citation recorded | ✔ I re-grepped `theory/memory-index.md`: `D27(LR2)` at line 354 (⟨1⟩5.⟨2⟩1, the mis-citation), line 406 (⟨1⟩7.⟨2⟩1, the genuine consumer), line 855 (a remark).  Count and content both as stated; MP-2 refers the cleanup to the owning lane. | FIXED |
| m6 | fenced (inside protected ⟨1⟩3) | Legitimate this round.  But the promoted `LR1-GEN` row's "no property of `Ψ` beyond normalisation" is licensed by ⟨1⟩3.⟨2⟩7, **not** by ⟨1⟩3's ASSUME line, which still over-lists (H1),(H3).  Recorded as m7 for r3; my §5 cell says so explicitly. | FENCE ACCEPTED |
| n1 | C4(c) is now the non-tautological finite-chain equality | ✔ and I separated the two effects the row conflates — see m2 below.  Reproduced from scratch in the full `2^12` space: `⟨K\|H_XXZ\|K⟩ = 1.1456439081`, `C_K = 1.1456439237`. | FIXED |
| n2 | fenced | **And on fresh inspection the proviso is automatic, so r1's n2 was over-cautious.**  ⟨2⟩5's extractions are *nested* subsequences of an increasing parent, so the `(n+1)`-th entry of the `(3+n)`-th sequence has parent index `≥ n+1`; `T_n` is therefore strictly increasing and a genuine subsequence with no extra clause.  This matters because the promoted row's word "subsequence" is now load-bearing. | FENCE ACCEPTED; r1 n2 **withdrawn as unnecessary** |
| n3 | cross-lane consistency expressed only via LR3-SCOPE | The consistency claim itself is still true, but LR3-SCOPE over-reaches — **M4**. | see M4 |

**⟨1⟩3 byte-identity — checked, not taken on trust.**  I extracted the text
from `## ⟨1⟩3.` to `## ⟨1⟩4.` from commit `365d143` (r1) and from `HEAD` (r2):
both 5619 bytes, `identical: True`, SHA-256
`0c28f353fee526373e26fc6bbcf41d18d411f2da557409281395ee5d14c0fde7` — **the
lane's quoted digest, matched exactly.**  LR1 is untouched, as ordered.

---

## 2. Objections

### M1 (MAJOR) — MP-4 still carries the sentence this round retracted

**(a) Location.**  `theory/lr-d16.md` §MP, **MP-4**, second sentence.  Also
`theory/lr-d16-r2-response.md` "Merge-proposal disposition", bullet MP-4
("retained unchanged, as ordered").

**(b) My computation.**  `git show 365d143:theory/lr-d16.md` vs `HEAD` — MP-4
is **byte-identical** between r1 and r2.  It reads:

> "…The honest headline is *one clause proved outright, one clause proved in a
> weakened form that suffices downstream, one clause reduced to a single named
> dynamical hypothesis*."

The middle clause is `(LR2′)`.  The same file now says, in four places, that
`(LR2′)` is **withdrawn** and delivers **nothing** downstream: §0's LR2 row;
⟨1⟩2's `(LRD-2-BND)` bullet ("Thus the r1 D16 result called **(LR2′)** is
WITHDRAWN, not patched"); ⟨1⟩4.⟨2⟩7 ("Thus it delivers **nothing** to
`M-INDEX-spec`"); §H item 8.  MP-4 targets `theory/TRIANGLE.md` and
`HANDOFF.md` — the two files the next session reads first.  Merging it as
written would put the round's retracted claim into the campaign's front matter
while the shard that generated it says the opposite four times.

This is a **lockstep failure between the shard and its own merge proposal**,
and it is my fault: r1 §4 ruled "**MP-4: MERGE**, unchanged.  It is the one
merge proposal that is exactly right", while r1 §0 had already written "it is
**not** 'one clause proved outright, one proved weakened but sufficient
downstream, one reduced to a single named dynamical hypothesis'".  r1
contradicted itself; the lane obeyed the ruling rather than the analysis.
That obedience was correct process.  The ruling is hereby **withdrawn**.

**(c) FIX DEMAND.**  Merge MP-4's **first** sentence only, and replace the
second sentence by the one in §5 of this verdict.  Do not merge the r1 text.

**(d) SURVIVING WEAKER STATEMENT.**  MP-4's first sentence is correct and is
the sentence the campaign needs: "`M-INDEX-spec` still has no fully
unconditional dynamical instance: for D16, LR1 is now unconditional and LR3 is
reduced to the single named input (NR), but LR2 verbatim remains open (residue
(DPH))."  Only the italicised "honest headline" clause is false.

---

### M2 (MAJOR) — "(ESC) is FALSE" is itself an unproved dynamical claim, asserted in the statement layer

**(a) Location.**  `theory/lr-d16.md` **⟨1⟩4.⟨2⟩5**, the sentence "**(ESC) is
false on the D16 state class (H3)**" and the three lines that follow it ("At
large `|t|` it lies outside every fixed `W_m`; … hence `G(m)≥1-o(1)` for every
fixed `m`").  Propagated to §0's LR2 row ("its sufficient condition **is
false** for every state obeying (H3)"), ⟨1⟩2's `(LRD-2-BND)` bullet ("**false
for every state obeying (H3)**"), ⟨1⟩6.⟨2⟩3 ("where ⟨1⟩4.⟨2⟩5 **proves** (ESC)
false"), §H items 6 and 8.

**(b) My computation.**  The step `G(m) ≥ 1-o(1)` is derived from three
ingredients: `𝒩_{W}² ⪰ 𝒩_W` on the integer spectrum (correct, I verified it);
`v(k)=J\sin k` bounded away from `0` on `supp φ` (correct, D16); and **"at
large `|t|` the magnon lies outside every fixed `W_m`"**.  The third is not a
consequence of the first two.  Non-zero group velocity of the *free* band is
not propagation of the *interacting* state: what is needed is that the
kink--magnon system has no bound state overlapping `φ`, i.e. local decay /
RAGE / asymptotic completeness in the one-kink-one-magnon sector.  That is
precisely D18(AD1)--(AD3), and ⟨1⟩2's not-proved list item (ii) says in terms:
"Asymptotic completeness, a channel inventory, wave operators, or D18.  **None
is used**".  The shard therefore uses, in its statement layer, an input it
declares unused two pages earlier.  A Lieb--Robinson bound cannot supply it:
LR bounds spreading from above, never escape from below.

**I own the same defect in r1.**  r1's F1(b) *Analytic* paragraph reads "the
magnon leaves every fixed window as `|t|→∞`" with no more justification than
`v(k)≠0`.  The lane adopted my sentence, including my gap.

The numerical support does not close it, and at the largest window it points
the other way.  Under the propagator the shard's own ⟨1⟩1.⟨2⟩1 mandates
(`H_{XXZ}`; see M3), over `t∈[−200,200]`, 2001 points, from the checker's own
`Context`:

| window | `R_W` | `G(m)` under `H_kink` | `G(m)` under `H_XXZ` |
|---|---|---|---|
| `[4,9]` | 3 | 0.990 | 0.989 |
| `[3,10]` | 4 | 0.965 | 0.949 |
| `[2,11]` | 5 | 0.952 | **0.278** |

`G(3)=0.278` is stable to the grid (identical on `[−40,40]`/201 points and
`[−200,200]`/2001 points).  At `N=12` the complement of `W_3` is two sites, so
the largest window carries no information about escape at all — which is the
honest reading, and it is not "`G(m) ≥ 1-o(1)` at every fixed `m`".

**(c) FIX DEMAND.**  In ⟨1⟩4.⟨2⟩5, §0, ⟨1⟩2, ⟨1⟩6.⟨2⟩3 and §H items 6/8,
replace "**(ESC) is false**" / "**proves (ESC) false**" by: "**(ESC) is not
established for any D16 state obeying (H3), and both the mechanism and the
finite-volume evidence point against it**"; and add one clause naming the
missing input — "*establishing `G(m) ≥ 1-o(1)` would require a local-decay
statement for the one-kink/one-magnon sector, i.e. D18(AD1)--(AD3), which
⟨1⟩2(ii) declines to assume*".

**(d) SURVIVING WEAKER STATEMENT.**  The withdrawal of `(LR2′)` **stands, and
stands on stronger ground than the shard uses**: `(LR2′)` was only ever
delivered *conditionally on (ESC)*, (ESC) is unproved for every D16 state, and
`η_m = 4R_{W_m}\sqrt{G(m)}` is below the free bound `2‖Q̂_W‖ = 6` at five of
six sampled `t_-` (I reproduced r1's `ε_W` row exactly under **both**
propagators: `ε = 0.837, 0.995, 0.969, 0.363, 0.692, 0.872` under `H_kink`,
`0.837, 0.994, 0.812, 0.417, 0.565, 0.544` under `H_{XXZ}`; five of six exceed
`6` in each case).  An estimate that is unavailable and, where measurable,
weaker than the one-line trivial bound must be withdrawn — no claim about the
truth of (ESC) is needed to withdraw it.  Everything else in ⟨1⟩4 is intact:
(LRD.6)--(LRD.10), the `4R_Wε_W` bound, `Δ_W(t,t)≡0`, the boundary-current
form, the (FN)-consuming step ⟨2⟩4, `(DPH)` correctly marked CONJECTURE, and
the refusal to patch with operator asymptotic commutativity.

---

### M3 (MAJOR) — the two rows that carry the round's entire numerical case run on the propagator the round itself corrected, and both fail once the m2 fix is applied consistently

**(a) Location.**  `theory/checks/lr_d16_check.py` `row_c2` line 333
(`env, prop = ctx.env, ctx.pk`) and `row_c3` line 452 (same), governing
**LRD-C2(d)** and **LRD-C3(e)**; §C's rows C2(d) and C3(e); §H "Numerical
evidence only", the sentence "C2(d) shows `G=0.990,0.965,0.950` and
`η=11.9,15.7,19.5`, evidence **against** the r1 D16 LR2′ claim.  C3(e) shows
the pinched term `1.383/1.797/1.872`, **evidence for retaining `sup_m`**."

**(b) My computation.**  `ctx.pk` is the `H_kink` propagator.  The shard's own
⟨1⟩1.⟨2⟩1 says: "*every dynamical statement below is therefore a statement
about `H_XXZ`, and `H_kink` is used only where a **value** of the energy is
needed*".  K3's telescoping equivalence is an **infinite-volume** statement; on
the `N=12` **open** chain `H_kink = H_XXZ − (J/2)\sqrt{Δ²−1}(S^z_1 − S^z_{12})`
and the two do not commute.  This is exactly r1's m2, which the round accepted
and fixed — **in C4(b) only**.  C1, C2, C3 were left on `H_kink`.

I applied the same fix to `row_c2`/`row_c3` on a copy
(`sed` on the two `ctx.pk` occurrences, one line changed, nothing else):

    [FAIL] LRD-C2(d) O(1) magnon; ESC fails: G = 0.989, 0.949, 0.278;
                                             eta = 11.9, 15.6, 10.5
    [FAIL] LRD-C3(e) pinched state varies with m:
           2 sum ||N_W1 eta_q^(m)||^2 = 1.607 / 1.670 / 1.747; spread = 0.140
    FAIL: 2 row(s)                                              exit=1

Every other row stays green — as it must, since C1(a), C2(a)--(c), C3(a)--(d),
C4, C5, C6 are propagator-independent identities and operator inequalities.
**The only two rows whose verdict depends on the choice of finite-volume
generator are precisely the two the round rests on.**  C2(d)'s acceptance test
(`min G > 0.90` **and** `η` strictly increasing by `>1`) fails on both
conjuncts; C3(e)'s (`spread > 0.40` **and** strictly increasing by `>0.03`)
fails on the first.

They are not robust in the other directions either.  Two further data
mutations on copies, each a change the shard itself calls immaterial:

| mutation | C2(d) | C3(e) | C4(c) |
|---|---|---|---|
| `C0 = 5` (⟨1⟩6.⟨2⟩5 r1: "the `c_0` offset plays no role; it cancels identically") | **FAIL** `G=0.995,0.896,0.885` | **FAIL** `1.839/2.008/1.987`, spread `0.169`, **not monotone** | PASS |
| `DELTA = 1.2` (an admissible D16 parameter, `Δ>1`) | **FAIL** `G=1.318,0.967,0.882` | **FAIL** `3.431/3.019/2.675`, **decreasing** | **FAIL** `3.78e−4` |
| `DELTA = 3.7` | PASS | PASS `spread 0.507` | PASS |

So the two diagnostics' thresholds are fitted to one point
(`Δ=2.5, c_0=6, N=12, H_kink`) and flip under the correct propagator, under a
neutral cut shift, and at another admissible anisotropy.  Under `Δ=1.2` the
pinched term is *decreasing* in `m` — so r1's F2(b) parenthetical about the
*direction* ("increasing in `m` — the opposite direction from the one the
lemma needs") is also parameter-specific; **I withdraw the direction claim and
keep only the `m`-dependence**, which is what F2 actually needs.

**(c) FIX DEMAND.**  (1) Switch `row_c2` and `row_c3` to `ctx.px`, so that
every dynamical row obeys ⟨1⟩1.⟨2⟩1, and gate `H_{XXZ}` energy conservation
there as C4(b) already does.  (2) Re-gate C3(e) on the claim it certifies and
nothing more: `spread/mean > tol` with **no ordering requirement** — the shard
claims `m`-dependence, not monotonicity.  (3) Re-caption C2(d) as a
*finite-volume illustration at the two inner windows only*, state that
`W_3=[2,11]` leaves two sites outside and carries no escape information at
`N=12`, and delete "evidence against" from §H — an `N=12` open chain cannot be
evidence about an `m→∞` escape profile in either direction.  (4) Re-derive the
§C and §H numbers under the corrected propagator.

**(d) SURVIVING WEAKER STATEMENT.**  Both **conclusions** survive; only the
certificates fail.  (i) F2's conclusion is untouched: under `H_{XXZ}` the
pinched term still varies with `m` (`1.607 / 1.670 / 1.747`), and in any case
F2 was never a refutation — the `sup_m` is required because the bound is *not
derived* without it, which is a proof-theoretic fact no propagator can change.
(ii) F1's conclusion is untouched for the reason given in M2(d).  (iii) The
inner-window numbers are robust: `G([4,9]) = 0.989`, `G([3,10]) = 0.949` under
either propagator and either time grid.  (iv) All fifteen other rows are
propagator-independent and stand.

---

### M4 (MAJOR) — LR3-SCOPE calls a non-DAG, currently-failing merge proposal "proved", and derives a necessity claim from a hypothesis class with no witness

**(a) Location.**  `theory/lr-d16.md` **⟨1⟩6.⟨2⟩4** (LR3-SCOPE), the sentence
"Independently, `theory/ace-ld.md`'s **proved** `ACE-LD-obst′` says that
D27(LR3) fails under its explicit mean-tail-transport hypothesis (M-ESC).  Any
future class theorem **must** therefore include a no-mean-transport clause
strong enough to exclude (M-ESC)", and its *Justification* line ("This is a
**necessary** scoping requirement, not a model counterexample").  Propagated to
§0's class row ("replaced by the surviving no-mean-transport scoping
requirement"), ⟨1⟩2's Remark ("a class theorem **must** exclude mean charge
transport"), ⟨1⟩6.⟨2⟩6(c), and §H item 11.

**(b) My computation.**  Three independent checks, all against the corpus.

1. **`ACE-LD-obst′` is not a `claims/CLAIMS.md` row.**  I grepped: the only
   ACE-LD row in the DAG is `AD3-ex` (CONJECTURE).  `ACE-LD-obst-prime` exists
   only as a *merge-proposal table row inside* `theory/ace-ld.md` (line 1291),
   self-labelled "PROVED (conditional; **pending L6 loop**)".  Under L5,
   status lives in `CLAIMS.md`; calling it "proved" in a proof shard is a
   status upgrade this lane cannot perform.
2. **Its owning shard is at FAIL.**  `theory/verdicts/ace-ld-r2.md` ends
   `FAIL(F1, M1, M2, M3, M4, M5, M6)`.  That verdict *does* say
   "`ACE-LD-obst′` is **correct**; I re-derived it in full" — so the
   mathematics is likely fine — but it also carries **M2: "obst′'s
   'contrapositive ⟹ `o(|W_m|)`' is a quantifier slip"**, i.e. the statement
   is currently registered with the wrong quantifier.  Citing it as settled
   while its own lane holds an open quantifier objection is premature.
3. **(M-ESC) has no witness, and `ace-ld.md` says so.**  Its own open-items
   list: "*(M-ESC) on any concrete model/state: **no model or state realising
   `θ > 0` is exhibited anywhere in this corpus*** (r2 m7; independently
   confirmed by the parallel lane, lr-d16-r1 M2(b)1)."  A conditional
   `(M-ESC) ⟹ ¬(LR3)` whose antecedent has no instance cannot make a clause
   **necessary** in a class theorem: if `(M-ESC)` is empty, "gap + LR ⟹ (LR)"
   could be true with no such clause at all.  **This is r1's M2 defect —
   a class-level claim with no exhibited model — reappearing in the sentence
   that was supposed to replace it, one notch softer.**  The word doing the
   illegitimate work is "must".

**(c) FIX DEMAND.**  Rewrite ⟨1⟩6.⟨2⟩4 to: "Neither a spectral gap nor a
Lieb--Robinson velocity estimate is used anywhere in ⟨1⟩3--⟨1⟩5, so this shard
supplies no proof that those two inputs imply (LR), and no refutation either.
Separately, `theory/ace-ld.md`'s `ACE-LD-obst′` — a merge proposal, not yet a
`CLAIMS.md` row, in a shard at FAIL(F1,M1--M6) — would show that D27(LR3)
fails on states satisfying (M-ESC); **no such state or model is exhibited
anywhere in this corpus**, so this identifies a hypothesis a class theorem
would have to *contend with*, not a clause it is *known to need*."  Delete
"proved", "must" and "necessary" from ⟨2⟩4, ⟨1⟩2's Remark, ⟨1⟩6.⟨2⟩6(c) and
§H item 11.

**(d) SURVIVING WEAKER STATEMENT.**  The genuinely established half of
LR3-SCOPE is the **inventory result**, and it is a good one, fully carried by
⟨1⟩6.⟨2⟩1 which I re-verified line by line against ⟨1⟩3--⟨1⟩5: **a spectral
gap is used at no step, and a Lieb--Robinson bound only to construct `α_t`,
never as a light-cone estimate.**  Hence this shard supports no "gap +
Lieb--Robinson ⟹ (LR)" class theorem in either direction — which is exactly
the honest, model-free statement, and it needs no reference to `ace-ld.md` at
all.  Also surviving: the retraction argument of ⟨1⟩6.⟨2⟩5 itself, which is
correct — on (FN), (LRD.5) gives `𝒬 = d` for a sharp wall at `c_0+d`, so fixed
`𝒬_0` pins the wall and a large `|ν|` requires wrong-phase block growth, not
rigid core transit.  I re-derived that from (LRD.1) independently.

---

### m1 (MINOR) — LRD-C3(d) is not a no-op but is deductively subsumed by C3(b)+C3(c)

**(a)** `row_c3`, the `majorant_worst` block; §C row C3(d).
**(b)** C3(d) gates `Σν²p ≤ 2⟨w,𝒩_{W_1}²⟩ + 2Σ_q‖𝒩_{W_1}η_q‖²`; C3(b) gates
the same left side against the smaller `2⟨w,Q̂_{W^c}²⟩ + 2Σ_q‖Q̂_{W^c}η_q‖²`.
Since `|Q̂_{W_m^c}| ⪯ 𝒩_{W_m} ⪯ 𝒩_{W_1}` pointwise — which C3(c) already gates
(`max(|Q_Wc| − N_W1) = +0.000`, `max(N_W' − N_W) = +0.000` at all three
windows) — C3(d)'s majorant dominates C3(b)'s.  I measured the gap at every
sampled `(t_-,t_+,W)`: **minimum `+1.044e−3 ≥ 0`**, so `C3(b) PASS ⟹ C3(d)
PASS`.  Its only registered mutant zeroes the majorant outright
(`slack +3.701`), which tests that the majorant is read, not that the bound
holds.  (The F2-relevant content correctly moved to C3(e), which is genuine —
`c3-freeze-pinching` collapses the terms to `1.383/1.383/1.383`, spread `0.000`
— but overfitted, M3.)
**(c)** Either delete C3(d) as decoration and say in §C that (LRD.13) is
certified as the composition C3(b)∘C3(c), or give it an independent mutant
(e.g. shrink `𝒩_{W_1}` to `0.5·n_w1`, which r1 showed has teeth: slack
`+2.745`).
**(d)** (LRD.13) itself is correct and is certified — just not *independently*
by C3(d).

### m2 (MINOR) — the C5/C6 rebuild lost the only gate certifying that the vector used everywhere else is a zero mode, and C4(c) conflates two effects

**(a)** `row_c5` (`local` is a 4-component two-site vector), the deletion of
r1's `LRD-C6(b)`, `row_c4`'s calibration block, and the deletion of §C's
"*Notation bridge (checked, not assumed)*" paragraph.
**(b)** r1's C5(a) computed `‖H_kink|K̄(z)⟩‖` for the **`N=12` vector in all 13
`S^z` sectors**; r1's C6(b) checked `⟨v|H_kink|v⟩ = 0` for `v = env["dressed"]`
and I judged it *subsumed by C5(a)*.  r2 deleted C6(b) — correct under r1's
finding — but simultaneously **replaced C5(a) by a single two-site
`4×4` block at one bond**, which is no longer about `env["dressed"]` at all.
The subsumption therefore no longer holds, and **no r2 gate certifies that the
vector every other row propagates is a zero mode of `H_kink`.**  It is true —
I computed it from scratch in the full `2^12` space: `‖H_kink·dressed‖ =
3.37e−16`, `⟨K|H_kink|K⟩ = 5.7e−17` — but it is now uncertified.
C4(c) is a partial surrogate only, and it conflates two effects: I separated
them, `⟨S^z_1 − S^z_{12}⟩ = 1 − 1.3665e−8` and `C_K·1.3665e−8 = 1.566e−8`,
which is the **whole** of the reported `|diff| = 1.57e−8`.  So C4(c) measures
boundary polarisation, not the zero-mode property, and cannot separate the two.
Finally, §C's notation bridge — which r1 fenced as "sound and load-bearing" —
was deleted, so §C no longer connects C5(a)'s `[1, zq^{-5}, zq^{-4}, z²q^{-9}]`
to ⟨1⟩1.⟨2⟩2's `|K̄(z)⟩`, and the `c5-wrong-root` mutant's relevance is
unexplained.
**(c)** Restore a one-line gate `‖H_kink · env["dressed"]‖ < tol` (it costs
nothing — the matrix is already built for C6(a)); restore the notation-bridge
paragraph; re-caption C4(c) as a **boundary-polarisation** certificate, which
is what it is.
**(d)** ⟨1⟩5.⟨2⟩8 is unaffected: K1+K2 give `𝒦_flat ⊆ ker H_kink` by pure
algebra, and the two-site kernel check is a mathematically sufficient
certificate for a product family with a bond-independent ratio `q`.  Coverage,
not correctness, was lost.

### m3 (MINOR) — `E_0` finiteness and conservation are asserted, and lie outside the m1 hygiene paragraph

**(a)** ⟨1⟩5.⟨2⟩6, "Since `E_0 := ⟨Ψ,H_{XXZ}Ψ⟩` is finite on a D17 packet and
conserved"; its *Justification* line lists no source for either.
**(b)** ⟨1⟩1.⟨2⟩5's repaired hygiene paragraph names a common core for the
**diagonal multiplication operators** `𝒬, 𝒩_W, D` only.  `H_{XXZ}` is not
diagonal and is not covered; nothing establishes its essential self-adjointness
on that core, hence nothing establishes `⟨U(t)Ψ, H_{XXZ}U(t)Ψ⟩ = E_0`.
Finiteness is derivable in one line and I gave the derivation in r1 §2 item 6
(`P^{DW}_x ⪯ n_x + n_{x+1}` and `0 ⪯ h_x ⪯ (J/2)(Δ+1)P^{DW}_x`, so
`E_0 ≤ (J/2)(Δ+1)Σ_x⟨P^{DW}_x⟩ < ∞` by D17's `ℓ¹` clause), but the shard still
does not contain it.  This matters because `LR-D16-EDW` is proposed **PROVED**
and `E_0` finite-and-conserved is in its statement.
**(c)** Either add the two-line derivation and the `H_{XXZ}` self-adjointness
sentence to ⟨1⟩5.⟨2⟩6, or carry finiteness/conservation as explicit
hypotheses.  **My §5 cell takes the second route**, so the row is safe to merge
today.
**(d)** The bond inequality, the sum, and the bound are all correct; only the
status of the two `E_0` properties is at issue.

### m4 (MINOR) — L4: the EDW row would promote the symbol `D`, which is already taken

**(a)** MP-3's `LR-D16-EDW` row, `D:=Σ_xP^{DW}_x`; ⟨1⟩5.⟨2⟩6.
**(b)** `definitions.md` **D13(b)** already uses `D(x)` for the DC weight
`\lim_{ω→0}\int dt e^{iωt}\dot m_x(t)`, and `D1`--`D28` is the definition
namespace.  `notation.md` contains neither `P^{DW}` nor a domain-wall number
(the nearest entry is line 264, `P_3` = "the `≤3`-domain-wall projection", a
different object from `memory-quantization.md`).  MP-3 proposes no
`notation.md` edit, so promoting the row as written injects a colliding symbol
into the DAG with no single-source entry.
**(c)** Rename to `N_{DW}` and add a `notation.md` row in the same merge.
**My §5 cell does the rename and defines the symbol inline**, so the row is
mergeable today; the `notation.md` entry is still owed.
**(d)** The mathematics is unaffected.

### m5 (MINOR) — "Proof: Verbatim ⟨1⟩3" is inexact for the strengthened LR1-GEN

**(a)** ⟨1⟩6.⟨2⟩2, the one-line proof.
**(b)** ⟨1⟩3.⟨2⟩3 extracts along `T = 1,2,3,…`; the strengthened statement
quantifies over an **arbitrary prescribed** `S_n→∞`.  The argument is the same
with the index set replaced, but "verbatim" is not literally true, and the word
"subsequence" in the promoted row is load-bearing.  I checked the substance:
(i) sequential compactness applies along any prescribed sequence; (ii) the
nested-extraction diagonal `T_n := T_n^{(2+n)}` **is** a genuine subsequence
with strictly increasing parent indices, because the `(n+1)`-th entry of a
subsequence of the `(2+n)`-th sequence sits at parent index `≥ n+1`; (iii)
`T_n → ∞` since every subsequence of a divergent sequence diverges.  So the
statement is delivered — and r1's n2 proviso is unnecessary, which I withdraw.
**(c)** Replace by "The proof of ⟨1⟩3 with the index sequence `T=1,2,3,…`
replaced by the prescribed `S_n`; nested extraction makes the diagonal a
genuine subsequence."
**(d)** `LR1-GEN` as strengthened is correct — this is a citation-precision
item only, and I have promoted the row.

### m6 (MINOR) — the r2 checker has no row bearing on Cesàro convergence, and r1's C1(c) was deleted without replacement

**(a)** MP-3's `LR1-GEN` `where-tested` cell (`C1(a,b)`); the deletion of r1's
`LRD-C1(c)` ("Cesàro contraction, `TV(8,24)=0.130 → TV(24,72)=0.026`").
**(b)** C1(a) certifies TPM normalisation, C1(b) raw integer spectrum and
support.  Neither says anything about the convergence LR1 asserts.  Convergence
along a subsequence is not a finite-`N` testable statement, so this is not a
defect in the claim — but the cell should not imply that it is tested.
**(c)** Say so in the cell.  **My §5 cell does.**
**(d)** LR1-GEN is a theorem with a complete proof; it needs no numerical
certificate.

### m7 (MINOR, deferred by the work order) — ⟨1⟩3's ASSUME still over-lists

⟨1⟩3's ASSUME says "(H1), (H3) of ⟨1⟩2"; ⟨2⟩7 says only three inputs are used
and "no property of `Ψ` beyond normalisation".  The lane's fence is legitimate
— the work order protected ⟨1⟩3 and it is byte-identical — but the promoted
row's strength is licensed by ⟨2⟩7, not by the ASSUME line.  **FIX for r3:**
change ⟨1⟩3's ASSUME to "(H1) for the existence of `α_t`; `‖Ψ‖=1`".  This is a
strengthening; nothing can break.  My §5 cell records the discrepancy inline so
the DAG is not misleading in the interim.

### n1 (NOTE) — correcting r1's own `‖[H_kink,H_XXZ]‖`

r1's m2(b) quoted `‖[H_kink,H_XXZ]‖ = 16.60`.  That is the **Frobenius** norm
in the 792-dimensional `S^z` sector.  The **operator** norm is
`1.1456439237 = C_K` exactly — I get `1.1456` both in the sector and in the
full `2^{12}` space, consistent with
`[H_kink,H_XXZ] = -\tfrac{J}{2}\sqrt{Δ²−1}\,[S^z_1 − S^z_{12}, H_{XXZ}]`, whose
two disjoint-support pieces each have norm `J/2`.  The **finding** stands
untouched — the drift numbers `+0.0598 / −0.3441 / −0.6215` reproduce exactly —
only the quoted norm was mislabelled.

### n2 (NOTE) — mutant quality census

Of the 17 registered mutants: 14 are mechanism mutations (wrong root,
overstrong field, mismatched complement `×2`, non-unitary propagator,
non-integer raw spectrum, unequal time, perturbed final evolution, frozen
pinching, wrong gap constant, wrong propagator, sharp-for-dressed `×2`,
signed majorant); **2 are degenerate "zero the data" mutations**
(`c2-delete-outside-data` → `G = 0.000, 0.000, 0.000`; `c3-delete-majorant`);
1 is a bare constant flip (`c2-small-constant`, `4.0 → 0.05`).  The three weak
ones test that an input is read, not that a bound holds.  I also confirmed
C3(a) is a **genuine two-route identity check** and not a rescaled duplicate:
perturbing only the `t_+` Hamiltonian on the matrix side fires it
(`|diff| = 6.08e−4`), while running both routes with an absurd `Δ = 37` leaves
it green (`1.4016294534` both routes) — which is correct behaviour, since
(LRD.11) is an identity for *any* unitary dynamics.  The row certifies the
identity, not the physics, and §C says exactly that.

### n3 (NOTE) — C4(c)'s red event duplicates C6(a)'s green gate

`c4-sharp-calibration` substitutes the sharp kink and reports
`⟨K|H_XXZ|K⟩ = 1.2500000000`, i.e. an excess of `0.1044` over `C_K` — the same
number C6(a) already gates as `E_kink(sharp) = 0.1044`.  The two rows'
red/green events coincide in content.  Not a defect; worth one sentence in §C.

### n4 (NOTE) — reliance audit clean

No REFUTED row is relied on: `M-INDEX-LA-strong` occurs five times, every one a
fence.  The `n≥2` display of ML4-Ward (9) occurs only in §H's disclaimer.
Bethe occurs twice, both in the "deliberately NOT proved" list.  `t(k)`,
`T(k)`, `δ_t(k)` occur once, in the same list.  `𝒮_W` occurs nowhere and is
irrelevant at `s=1/2`.  K1, K2, K3 are PROVED rows and K4 is CONJECTURE
(`claims/CLAIMS.md` lines 60--63), and all 8 `K4` occurrences are fences.  The
frozen limit order ⟨1⟩1.⟨2⟩8 is respected at every step; no `k→0` or plane-wave
interchange.  `git status` is clean — no shared file was edited by this lane.
The one reliance defect is **M4**, and it concerns a *non-DAG* statement, not a
REFUTED one.

---

## 3. The three former no-ops — are they genuine, or renamed?

Answered by simplifying each gate symbolically first, then by data mutation on
copies, exactly as the Standing obligations require.

**LRD-C1(b) — GENUINE (in one of its three conjuncts).**  r1's version rounded
first and then compared a Python `int` with its own `round`, and survived
`rho_ref = 0.3/−0.7` unchanged.  r2 gates
`raw_err = max|q_w − rint(q_w)|` on the **raw** array.  I re-ran **r1's exact
data mutation** on a copy — `rho_ref → 0.3 / −0.7`, so that `spec Q̂_W ⊄ ℤ` and
the row's stated content is genuinely false:

    [FAIL] LRD-C1(b) raw integer spectrum/support:
           max dist(spec Q_W,Z) = 2.00e-01 ; max dist(nu,Z) = 8.88e-16

**It now fires on the mutation that exposed it as a no-op.**  The repair is
real.  *But two of its three conjuncts are still tautologies*: `nu_err`
compares `q − q'` (both drawn from the same `spec`) with its own rounding —
`8.88e−16` even under the mutation — and `supp_ok` checks membership in
`allowed`, which is built from the same `blocks`.  They are harmless, and they
are also worthless; say so in §C or delete them.

**LRD-C3(a) — GENUINE.**  r1's version regrouped one sum two ways
(`0 ≡ 0`) and survived a non-unitary "dynamics".  r2 builds
`α_{t_±}(Q̂_W) = U_±^†\,\mathrm{diag}(q_w)\,U_±` as explicit matrices on an
independent `N=8` sector and compares the pinched square with a separately
generated TPM law.  I verified the routes are genuinely disjoint (the TPM route
never forms a matrix; the matrix route never calls `tpm_law`) **and reproduced
the value by a third, from-scratch route in the full `2^8` space with no shared
code**: `1.2910437765` versus `1.2910437765`, `|diff| = 2.22e−16`,
`Σp = 1.000000000000`.  It fires under a real one-sided dynamics perturbation
(`mut/mC.py`, `|diff| = 6.08e−4`) and correctly stays green when the *same*
wrong Hamiltonian is used on both sides — the right behaviour for an identity.
**This is now the check r1 said it should have been.**

**LRD-C3(d) — NO LONGER BLIND, BUT SUBSUMED.**  r1's complaint was that C3(d)
could not distinguish the derived `W_m`-pinched bound from the claimed
`W_1`-pinched one.  r2 removes the claim, so the row now honestly gates only
the derived bound, and the `m`-dependence moved to the new C3(e) — which is
genuine (`c3-freeze-pinching` collapses it to spread `0.000`).  So the r1
defect is gone.  **But C3(d) is now deductively implied by C3(b) plus the
dominance C3(c) already gates** (m1: minimum gap `+1.044e−3` over all samples),
so it contributes no independent evidence.  Verdict: not a no-op, not a
certificate either — **decoration with a live exit**.

**Reachability, re-measured independently.**  I ran every red mode over the
**full 17-row suite** rather than only its own group, which is a stronger test
than the lane's own `--red-all`:

    all 17 modes -> exactly their registered singleton, no collateral, no masking

That is a real improvement over r1 (10 of 18 rows killed by no mode).  The
"no earlier gate masks a later one" property is achieved partly by
construction — `red_result` restricts to `ROW_GROUP[target]` — but the
full-suite run shows it holds anyway.  Green exit 0; `--red-all` exit 1
RED-OK 17/17; every `--red MODE` exit 1; zero bare asserts; `-O` strict.

---

## 4. VERIFIED CORRECT — fenced, do not churn

Re-verified this round, by the route stated.  Everything r1 fenced and did not
change is still fenced; only the items I actually re-ran are listed.

1. **⟨1⟩3 (LR1) — byte-identical to r1 and still PROVED unconditionally.**
   SHA-256 `0c28f353…0fde7`, 5619 bytes, `identical: True` against commit
   `365d143`.  The r1 fence stands in full: separability, metrizable weak-`*`
   compactness, finite `spec Q̂_W`, countable `𝕀`, Cantor diagonal, extraction
   done **once before any window is fixed**, `p_W` a probability on a fixed
   finite subset of `ℤ`.  **Do not touch this section.**
2. **⟨1⟩6.⟨2⟩2 (LR1-GEN), in its strengthened any-sequence/subsequence form.**
   The strengthening is delivered (m5(b)), including that the diagonal is a
   genuine subsequence.  **Promoted, §5.**
3. **The (NR) repair and THEOREM (LRD-3).**  (LRD.11), Chebyshev, the edge
   split `2X²+2Y²−(X−Y)²=(X+Y)²⪰0`, `𝒟_{W,t_-}` acting as the identity on
   `α_{t_-}(Q̂_{W^c})²` (correct on (FN), by (LRD.5)), `𝒩_{W'} ⪯ 𝒩_W`,
   `|Q̂_{W^c}| ⪯ 𝒩_W`, Fatou, and the tail constant `2S_{NR}/M` — all
   re-derived, all correct, and the two clauses of (NR) are logically
   independent.
4. **⟨1⟩5.⟨2⟩6 (EDW).**  Re-derived independently: in `(|↑↑⟩,|↑↓⟩,|↓↑⟩,|↓↓⟩)`
   the bond term is `0` on `|↑↑⟩,|↓↓⟩` and `[[JΔ/2,−J/2],[−J/2,JΔ/2]]` on the
   domain-wall block, eigenvalues `(J/2)(Δ∓1)`, so
   `h^{XXZ} ⪰ (J/2)(Δ−1)P^{DW}` bondwise with equality on the symmetric
   eigenvector.  `E_0 = 3.5646`, bound `2E_0/(J(Δ−1)) = 4.7528`,
   `max⟨D⟩ = 3.053`.  **Promoted, §5.**
5. **⟨1⟩5.⟨2⟩8 uses K1+K2 and never K4** — re-verified, and the fences (i)/(ii)
   are now matched by every summary sentence in the file (M3 of r1 fully
   discharged).  I confirmed independently that the family really is in the
   kernel at `N=12`: `‖H_kink · dressed‖ = 3.37e−16`.
6. **⟨1⟩1.⟨2⟩2 orientation and ⟨1⟩1.⟨2⟩3 calibration.**  Reproduced from
   scratch in the full `2^{12}` space: `⟨K|H_XXZ|K⟩ = 1.1456439081` against
   `C_K = 1.1456439237`, with the `1.57e−8` gap accounted for **exactly** by
   `⟨S^z_1 − S^z_{12}⟩ = 1 − 1.3665e−8`.  `Q̂_{W,c_0} = Σ_{x∈W}δ_x` with no
   offset; `𝒬 = q_w + q_{w^c} = −1` identically on the sector, so (FN) is
   automatic there.
7. **⟨1⟩4.⟨2⟩3's `4R_Wε_W(t_-)` bound and the free-bound comparison.**
   Reproduced under both propagators; "five of six sampled times exceed
   `2‖Q̂_W‖ = 6`" is exact (M2(d)).
8. **The `m2` repair itself.**  C4(b) now conserves `H_{XXZ}` to `1.11e−14` and
   its mutant is caught by the drift gate at `1.007` — a genuine, specific,
   load-bearing red certificate, and the cleanest single improvement in the
   round.
9. **The leaf audit (r1 m5) and MP-1's clause-2 reading** — both confirmed
   against `theory/memory-index.md` lines 354, 402, 406.
10. **Reliance and fences** — n4.

---

## 5. Merge rulings, with the exact cells

Promotion happens on these sentences.  Apply verbatim; do not paraphrase.

### MP-1 — **MERGE**, with one verification condition

MP-1 is exactly my r1 fix demand, including the clause fixing D27(LR2)'s limit
along the common sequence.  Merge as proposed.

**Condition (one check, then merge).**  MP-1's third clause *weakens* D27(LR2)
(a limit along `T_n` is implied by a limit as `T→∞`), and D27 is a hypothesis of
the PROVED row `M-INDEX-spec`.  Weakening a hypothesis strengthens the theorem,
so the orchestrator must confirm no `memory-index.md` step needs the stronger
reading.  **I have checked this and it is safe**: `D27(LR2)` is cited at three
places — line 406 (⟨1⟩7.⟨2⟩1), the only genuine consumer, which already reads
it "followed by the **common subsequence**"; line 354 (⟨1⟩5.⟨2⟩1), which by
content uses only clause 1's TPM display; and line 855, a remark.  Record that
sentence in the merge note.

### MP-2 — **HOLD** (confirmed)

Correct as the lane has it.  Transmit the lane-local cleanup to the
`memory-index` owner: ⟨1⟩5.⟨2⟩1 should cite D27's clause-1 TPM display, not
D27(LR2).

### MP-3 row 1 — `LR1-GEN` — **MERGE as PROVED**

| id | statement | status | depends on | proved in | tested in |
|---|---|---|---|---|---|
| LR1-GEN | Let `𝔄` be the quasi-local algebra of a quantum spin system on a countable lattice with uniformly finite local dimension, `α_t` a strongly continuous one-parameter group of `*`-automorphisms of `𝔄`, `Ψ` a unit vector in any representation of `𝔄`, `c_0` a cut, and `Q̂_{W,c_0}∈𝔄_W` self-adjoint with finite spectrum at each finite window `W∋c_0`.  Then **every** prescribed sequence `S_n→∞` admits a subsequence `T_n=S_{n_j}` along which, **simultaneously for every such `W`**, the two Cesàro states `ω^±_{W,n}` converge weak-`*` on all of `𝔄` to states, and every double-Cesàro TPM weight `p_{W,n}(ν)` converges; each limit `p_W` is a probability supported in the finite set `spec Q̂_W − spec Q̂_W`, which under D26(INT) lies in `ℤ`.  This is D27's clause 1, so **clause 1 is a theorem, not a restriction — but it is not removable**: it existentially binds the single sequence that D27's clauses 2--3 quantify over, and the substantive content of `(LR)` therefore lies entirely in clauses 2--3.  The proof consumes exactly three inputs — separability of `𝔄`, strong continuity of `α_t`, finiteness of `spec Q̂_W` — and **no** spectral gap, Lieb--Robinson velocity, ergodicity, scattering or completeness input, and no property of `Ψ` beyond `‖Ψ‖=1` (per ⟨1⟩3.⟨2⟩7; ⟨1⟩3's ASSUME line still over-lists (H1),(H3) and is due a strengthening in a later round).  NOT claimed: pointwise-in-`t` convergence, which D27 does not ask for; convergence along the full sequence; anything about D27(LR2) or (LR3). | **PROVED** | D26, D27 | theory/lr-d16.md ⟨1⟩3.⟨2⟩1--⟨2⟩8, restated at ⟨1⟩6.⟨2⟩2 | theory/checks/lr_d16_check.py C1(a) TPM normalisation `6.66e−16`, C1(b) raw integer spectrum/support; green exit 0, `--red c1-nonunitary` and `--red c1-noninteger` each exit 1 on exactly that row.  These certify the finite-`W` TPM arithmetic only; **no gate bears on the Cesàro convergence itself**, which is not a finite-`N` testable statement and needs none — the proof is complete. |

### MP-3 row 2 — `LR-D16-EDW` — **MERGE as PROVED**

The r1 `m2` conservation error is fixed and I verified the fix directly: C4(b)
now propagates with `H_{XXZ}` (drift `1.11e−14`) and its registered mutant
reverts to `H_kink` and is caught **by the energy-drift gate** at `1.007`.  The
cell below carries `E_0`'s two properties as explicit hypotheses (m3) and
renames the domain-wall number away from D13(b)'s `D(x)` (m4), so it is safe to
apply today.

| id | statement | status | depends on | proved in | tested in |
|---|---|---|---|---|---|
| LR-D16-EDW | In D16, in the two-site basis `(\|↑↑⟩,\|↑↓⟩,\|↓↑⟩,\|↓↓⟩)` the bond term `h^{XXZ}_{x,x+1}` annihilates `\|↑↑⟩` and `\|↓↓⟩` and equals `(JΔ/2)I−(J/2)σ^x` on the domain-wall block, with eigenvalues `(J/2)(Δ∓1)`; hence bondwise `h^{XXZ}_{x,x+1} ⪰ \tfrac{J}{2}(Δ−1)P^{DW}_x`, where `P^{DW}_x` projects onto `span\{\|↑↓⟩,\|↓↑⟩\}_{x,x+1}`.  Summing, as a quadratic form on the finite-deviation core of `ℋ_ref`, `H_{XXZ} ⪰ \tfrac{J}{2}(Δ−1)N_{DW} ⪰ 0` with `N_{DW}:=Σ_xP^{DW}_x` the domain-wall **number** (written `D` in the shard; renamed here because `D(x)` is already D13(b)'s DC weight — L4, and a `notation.md` entry for `N_{DW}`, `P^{DW}_x` is still owed).  Consequently, **for any state `Ψ` whose energy `E_0:=⟨Ψ,H_{XXZ}Ψ⟩` is finite and is conserved by the D16 dynamics**, `⟨Ψ,α_t(N_{DW})Ψ⟩ ≤ 2E_0/(J(Δ−1))` for every `t`.  This bounds the **NUMBER** of phase boundaries uniformly in time and **nothing about their LENGTH** — a one-dimensional wrong-phase block of any length carries the same `O(1)` Ising cost — so it does **not** give D27(LR3) and does not give either clause of (NR).  Finiteness and conservation of `E_0` are stated here as hypotheses on the selected state: ⟨1⟩5.⟨2⟩6 asserts both without proof, and ⟨1⟩1.⟨2⟩5's operator-hygiene paragraph covers only the diagonal operators `𝒬, 𝒩_W, N_{DW}`, not `H_{XXZ}` (both are expected to hold on a D17 packet — `P^{DW}_x ⪯ n_x+n_{x+1}` and `0 ⪯ h_x ⪯ (J/2)(Δ+1)P^{DW}_x` give `E_0 < ∞` from D17's `ℓ¹` clause — but that derivation is not in the shard).  The bond inequality and the sum are exact in infinite volume **and on any finite open chain**; a finite-chain certificate must use the `H_{XXZ}` propagator, because `H_kink` and `H_{XXZ}` generate the same derivation only in infinite volume (K3) and differ at finite `N` by the boundary term `\tfrac{J}{2}\sqrt{Δ²−1}(S^z_1−S^z_N)`. | **PROVED** | D16, K3 | theory/lr-d16.md ⟨1⟩5.⟨2⟩6 | theory/checks/lr_d16_check.py C4(a) bond inequality, min eig `−0.0`; C4(b) `H_XXZ` energy drift `1.11e−14` and `max⟨N_DW⟩ = 3.053 ≤ 4.753`; C4(c) finite-chain calibration `⟨K\|H_XXZ\|K⟩ = 1.1456439081` vs `C_K = 1.1456439237`.  Green exit 0; `--red c4-wrong-gap`, `--red c4-kink-propagator` (caught by the energy-drift gate at `1.007` — this is the certificate of the r1 `m2` repair) and `--red c4-sharp-calibration` each exit 1 on exactly that row. |

### MP-3 row 3 — `LR-D16` — **HOLD** (confirmed; the lane is right)

Restated: for D16, **LR1 is unconditional** (and is now a class theorem);
**LR2 verbatim is OPEN**, its residue named `(DPH)` and marked CONJECTURE, and
the r1 `(LR2′)` route is dead because its antecedent (ESC) is unavailable
(M2 — unavailable, not proved false); **LR3 holds only under the repaired
two-clause (NR)**, whose second clause carries `sup_m` and which (EDW) does not
supply because it bounds block number and not block length.  A row asserting
`(LR)` for D16 cannot be written until either `(DPH)` or `(NR)` is discharged.

### MP-4 — **HOLD as written; MERGE the first sentence with this replacement second sentence**

Do not merge the r1 text (M1).  Merge exactly:

> "`M-INDEX-spec` still has no fully unconditional dynamical instance: for D16,
> LR1 is now unconditional — indeed a class theorem, `LR1-GEN` — and LR3 is
> reduced to the single named input (NR), but LR2 verbatim remains open
> (residue (DPH)).  The honest headline is *one clause proved outright, one
> clause still open with its residue named, and one clause reduced to a named
> two-clause dynamical hypothesis*.  The clause that became unconditional is
> the one that carried no content: D27's clause 1 only binds the sequence its
> clauses 2--3 quantify over."

---

## 6. What `M-INDEX-spec` still lacks — stated explicitly

Unchanged by this round, in either direction, and the shard says so correctly
at ⟨1⟩4.⟨2⟩7 and §H item 8.

- **It still has no fully unconditional dynamical instance.**  D27 is assumed
  on every model.  After r2, for the one model where the assumption has been
  attacked seriously:
  - **D27(LR1)** is discharged unconditionally (`LR1-GEN`) — **but this buys
    nothing**, because clause 1 was never a constraint: it existentially binds
    the sequence clauses 2--3 quantify over, and `LR1-GEN` says every candidate
    sequence has a subsequence satisfying it.  The content of `(LR)` was always
    in clauses 2--3, and both remain assumed.
  - **D27(LR2)** is **open**, reduced to `(DPH)`, a CONJECTURE.  The r1 route
    around it — replace LR2 by `(LR2′)` and let the exhaustion kill the error —
    is dead: its antecedent (ESC) is unavailable for every D16 state obeying
    (H3).
  - **D27(LR3)** is **conditional on (NR)**, two clauses, the second carrying
    `sup_m`.  (EDW) is the only unconditional input and it controls block
    number, not block length.
- **The (FN) register cannot be upgraded.**  A sector-wide self-adjoint
  regularised charge is `M-INDEX-LA-strong`, **REFUTED**; (FN) stays a
  hypothesis on the selected vector.
- **The reduction clause is untouched**: it still additionally assumes H-AD-G
  with D18(AD3) read as weak-`*` window convergence per channel, a reading
  D18's frozen words do not fix.

So the campaign's standing claim is intact and this lane's headline must not
drift from it: **`M-INDEX-spec` has no fully unconditional dynamical
instance**.  What this round genuinely adds to the DAG is two side results —
`LR1-GEN` and `LR-D16-EDW` — neither of which touches that sentence.

---

## 7. Register comparison against `M-INDEX-spec`

`M-INDEX-spec`'s adjudicated scoping sentence is the register: every
hypothesis named, nothing derived that was assumed, no conditional upgraded
into a fact.

**On the positive claims the shard is now exactly in that register, and the r1
divergences are gone.**  §0, ⟨1⟩2, ⟨1⟩4, ⟨1⟩5, §H and MP-3 all say the same
thing at the same strength about LR1 (unconditional), LR2 (open, residue
`(DPH)`, `(LR2′)` withdrawn), LR3 (conditional on two-clause (NR) with
`sup_m`), and the K4 fence.  I checked each layer against each other layer;
the r1 lockstep failures — §0 stronger than §H on LR2, "`sup_m` removed for
free", K4-strength summary sentences — are **all** repaired.  That is a real
achievement and the round should be credited for it.

**The residual divergences are all in the negative layer**, where the round
over-claims its own retractions:

1. **MP-4** still asserts what the shard withdraws (M1) — the only place a
   retracted claim would reach a shared file.
2. §0 / ⟨1⟩2 / ⟨1⟩4.⟨2⟩5 / ⟨1⟩6.⟨2⟩3 / §H say "**(ESC) is false**" where the
   honest register is "(ESC) is not established, and both mechanism and
   finite-volume evidence point against it" (M2).  Asserting an unproved
   dynamical statement as proved is the same failure mode whether the
   conclusion is positive or negative.
3. ⟨1⟩6.⟨2⟩4 says a class theorem "**must**" carry a no-mean-transport clause,
   on the authority of a "**proved**" statement that has no DAG row, sits in a
   FAIL'd shard, and quantifies over a hypothesis class the corpus records as
   having **no exhibited instance** (M4).
4. §H calls C2(d) and C3(e) "evidence" while they are the only two rows that
   flip under the propagator correction the same round applied elsewhere (M3).

The pattern is worth naming for r3: **a retraction is a claim too.**  This
round retracted honestly but then asserted the retractions with more force
than it had earned.  Saying "we cannot establish this, and here is why we
doubt it" is the register; saying "this is false" is not, unless it is proved.

---

FAIL(M1, M2, M3, M4)

*(No FATAL survives; severity fell from FAIL(F1,F2,M1--M4).  `LR1-GEN` and
`LR-D16-EDW` are **MERGED** on the cells in §5 notwithstanding this verdict —
none of M1--M4 is load-bearing for either row.  `LR-D16` stays HOLD.  MP-1
merges with the §5 condition; MP-2 holds; MP-4 merges only with the §5
replacement sentence.)*
