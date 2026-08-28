<!-- ROLE: adversarial critic verdict, round r1, on theory/lr-d16.md +
     theory/checks/lr_d16_check.py (bd tns-xf4).  Lane: this file only.
     Nothing else edited; no commit. -->

# Critic verdict — (LR) for D16, r1

**Target:** `theory/lr-d16.md` (983 lines), `theory/checks/lr_d16_check.py` (547 lines).
**Verdict line is at the bottom.**  Read §1 (objections) before §2 (fence) —
§2 is large, and it is deliberately large: most of this shard is right.

Everything below was recomputed.  Scripts used are throwaway; every number
quoted is reproducible from the shard's own checker module by the recipes
stated inline.

---

## 0. Headline

The shard's own three-line summary is

| clause | shard's verdict | this critic's verdict |
|---|---|---|
| LR1 | PROVED unconditionally | **PROVED unconditionally — confirmed.**  One sequence, all windows.  LR1-GEN is a correct theorem. |
| LR2 | verbatim OPEN, (LR2′) PROVED and *sufficient downstream* | **(LR2′) is EMPTY on the shard's own state class.**  Its sufficient condition `R_{W_m}²G(m)→0` is FALSE for every `Ψ` satisfying (H3).  Nothing is delivered to `memory-index.md`. **F1** |
| LR3 | PROVED from one named input (NR); `sup_m` removed unconditionally | **NOT proved from (NR) as stated.**  (LRD.13) is not `m`-independent — the second term is a `W_m`-pinching, and pinchings are not monotone.  `sup_m` survives, inside the hypothesis. **F2** |
| class statement | CONJECTURE + a volunteered REFUTATION of "gap + LR ⟹ (LR)" | **The refutation exhibits no model** and its stated mechanism is inconsistent with (FN), which the shard itself proves.  Must not enter the corpus. **M2** |

Two clauses of the shard's own honest headline therefore fail: it is **not**
"one clause proved outright, one proved weakened but sufficient downstream,
one reduced to a single named dynamical hypothesis".  It is **one clause
proved outright (LR1, a real and clean result), one clause reduced to a named
hypothesis that is FALSE for the intended states (LR2), and one clause reduced
to a named hypothesis that is stated too weakly to close it (LR3)**.

`M-INDEX-spec` is **unaffected and unimproved**: it still assumes D27(LR2) and
still has no unconditional dynamical instance.  Nothing here damages it.

---

## 1. Objections

### F1 (FATAL) — the escape profile does not vanish, so (LR2′) never fires

**(a) Location.**  `theory/lr-d16.md` ⟨1⟩4.⟨2⟩5 (the sentence "Consequently
**(LR2′)** holds … whenever `R_{W_m}²G(m)→0`"), propagated to ⟨1⟩2 bullet
(LRD-2′) ("`η_m→0` along every padded exhaustion whose padding grows at least
logarithmically faster than `log|W_m|` — in particular along the geometric or
linear paddings used in practice"), to §0's summary table row LR2 ("the
weakened (LR2′) is PROVED (⟨1⟩4) **and is shown to suffice for every
downstream use**"), to ⟨1⟩4.⟨2⟩7, to §H items 6 and 8, to ⟨1⟩6.⟨2⟩3
(LR2′-GEN), and to MP-2 and MP-3's `LR-D16` row.

**(b) My computation.**  `G(m) := sup_t⟨Ψ,α_t(𝒩_{W_m})²Ψ⟩` does **not** tend
to `0`; it tends to `≈1`, at every window, for exactly the states (H3)
selects.

*Analytic.*  `𝒩_W = Σ_{x<a}(½−S^z_x) + Σ_{x>b}(S^z_x+½)` is diagonal with
spectrum in `ℤ_{≥0}`, hence `𝒩_W² ⪰ 𝒩_W` and
`G(m) ≥ sup_t⟨Ψ,α_t(𝒩_{W_m})Ψ⟩`.  (H3) fixes a `C_c^∞` magnon profile `φ`
supported away from `k∈{0,π}`, so `v(k)=J\sin k` is bounded away from `0` on
`supp φ` (D16), and the magnon leaves every fixed window as `|t|→∞`.  A magnon
that has left `W` to the right is an `↑` in the `↓` region and contributes
exactly `1` to `N_T^W`; to the left it is a `↓` in the `↑` region and
contributes exactly `1` to `N_R^W`.  Either way
`limsup_{|t|→∞}⟨α_t(𝒩_{W_m})⟩ ≈ 1` for **every** `m`, whence
`G(m) ≥ 1−o(1)` and `η_m = 4R_{W_m}\sqrt{G(m)} ≍ 4R_{W_m} → ∞`.
The shard's ⟨1⟩4.⟨2⟩5(i) proves `G` non-increasing, which is true and useless:
a non-increasing sequence bounded below by `≈1` does not go to `0`, and
`R_{W_m}²G(m) → ∞`.

*Numerical, from the shard's own checker module (`build_states`, `Propagator`,
`window_charges`), `t∈[−40,40]`, 201 points:*

| window | `R_W` | `sup_t⟨𝒩_W⟩` | `G(m)=sup_t⟨𝒩_W²⟩` | `η_m=4R_W√G` |
|---|---|---|---|---|
| `[4,9]` | 3 | 0.9896 | 0.9897 | **11.94** |
| `[3,10]` | 4 | 0.9651 | 0.9651 | **15.72** |
| `[2,11]` | 5 | 0.9504 | 0.9504 | **19.50** |

`η_m` **increases**.  The shard's own row LRD-C2(d) reports the same numbers
(`0.9897, 0.9637, 0.9315`) and labels them "escape profile falls with
padding": a `6%` fall on a 12-site chain, entirely explained by the outside
region shrinking from 6 sites to 2, and nowhere near the `q^{2d}` decay
(`q=0.2087` at `Δ=2.5`) that a "logarithmically faster padding" rate would
need.  The shard's numerics are evidence **against** its own rate claim.

*Worse: the bound is below the trivial bound.*  `|Δ_W| ≤ 2‖Q̂_{W,c_0}‖ ≤ 2R_W`
holds with no work at all.  ⟨1⟩4.⟨2⟩3 delivers `4R_Wε_W(t_-)`, which beats
`2R_W` only when `ε_W(t_-) < ½`.  Measured `ε_W(t_-)` at `W=[4,9]`:

    t_- =   0    -2    -5    -9   -20   -40
    eps  = 0.837 0.995 0.969 0.363 0.692 0.872   (4R_W*eps = 10.0,11.9,11.6,4.4,8.3,10.5)

so at five of six sampled times the shard's bound is **weaker than the
one-line trivial bound**, and it is weakest exactly in the asymptotic regime
the Cesàro average is supported on.  This is the mechanical statement of the
same defect: `ε_W(t_-)→1` because the magnon is outside `W` at large `|t_-|`,
so the window charge is not sharp there.

**(c) FIX DEMAND.**  Delete the rate sentence from ⟨1⟩2; restate ⟨1⟩4.⟨2⟩5 as
the *conditional* "IF **(ESC)**: `R_{W_m}²G(m)→0` THEN (LR2′)", register
**(ESC)** as a named hypothesis and record in the same paragraph that (ESC) is
**FALSE for every `Ψ` obeying (H3)** because one escaping magnon puts `G≈1` at
every window; then mark the LR2 row of §0, §H item 6/8, MP-2 and MP-3 as
delivering **nothing** for D16.

**(d) SURVIVING WEAKER STATEMENT.**  (i) The exact defect identities
⟨1⟩4.⟨2⟩1 and ⟨1⟩4.⟨2⟩2 (`Δ_W = −Σ_{q≠q'}⟨φ_q,Aφ_{q'}⟩`; the boundary-current
form (LRD.7) with `𝒥_W=j_{a−1|a}−j_{b|b+1}` and `Δ_W(t,t)≡0`) are correct and
survive intact.  (ii) The bound `|Δ_W| ≤ 4R_W ε_W(t_-)` and the sharpness
inequality `ε_W(t)² ≤ ⟨α_t(Q̂_{W^c})²⟩ ≤ ⟨α_t(𝒩_W)²⟩` are correct.  (iii) The
*conditional* mitigation of ⟨1⟩4.⟨2⟩7 — "if the defect is bounded by `η_m`
with `η_m→0` along the exhaustion, then `memory-index.md` ⟨1⟩7.⟨2⟩1--⟨2⟩4 and
(IDX.2) survive verbatim" — is a correct and reusable conditional; only its
antecedent is unavailable.  (iv) The shard's refusal to patch LR2 with
operator asymptotic commutativity is correct and should be preserved: I
checked ⟨1⟩4 line by line and **no operator statement about
`[Q̂_W(t_-),Q̂_W(t_+)]` is used, asserted, or implied anywhere** — the brief's
"single most likely defect" is genuinely absent.

---

### F2 (FATAL) — (LRD.13) is not `m`-independent; (NR) as stated does not prove LR3

**(a) Location.**  ⟨1⟩5.⟨2⟩4, the display (LRD.13) and the sentence "a bound
that **does not depend on `m`**"; ⟨1⟩5.⟨2⟩7 (NR) and THEOREM (LRD-3);
propagated to §0's summary table ("the `sup_m` is removed unconditionally by
the monotonicity lemma"), ⟨1⟩2 bullet (LRD-3), §H item 3, §H's cross-lane
paragraph, ⟨1⟩6.⟨2⟩1's inventory row, and MP-3's `LR-D16` row.

**(b) My computation.**  ⟨1⟩4's standing convention fixes
`φ_q := E_{W,t_-}({q})Ψ` **for the window `W` under discussion**, so in
(LRD.13) the right-hand `φ_q` is `φ_q^{(m)} = α_{t_-}(E_{W_m}({q}))Ψ`.  The
derivation of ⟨2⟩3 gives, honestly,

    Σ_ν ν² p_{W_m;t_-,t_+} ≤ 2⟨Ψ, α_{t_-}(𝒩_{W_1})² Ψ⟩
                            + 2⟨Ψ, 𝒟_{W_m,t_-}( α_{t_+}(𝒩_{W_1})² ) Ψ⟩ .

The **first** term is `m`-independent — that part of the monotonicity lemma is
correct and I verified it.  The **second** term is the expectation of a fixed
positive operator in the `W_m`-**dephased** state
`ρ_m = 𝒟_{W_m,t_-}(|Ψ⟩⟨Ψ|)`, and `ρ_m` depends on `m`.  There is no general
inequality here: for `B = |χ⟩⟨χ|` with `χ ⊥ Ψ`, `⟨Ψ,BΨ⟩ = 0` while
`⟨Ψ,𝒟(B)Ψ⟩ = Σ_q|⟨χ,φ_q⟩|²` can be strictly positive — pinching *raises*
expectations of operators that do not commute with the pinching family, and
`α_{t_+}(𝒩_{W_1})` does not, at `t_+≠t_-`.  `‖𝒟(B)‖ ≤ ‖B‖` would rescue it,
but `𝒩_{W_1}` is unbounded on `ℋ_ref` and the shard's own escape clause in
⟨2⟩7 ("implied by the first whenever `𝒩_{W_1}` is bounded on the smallest
`α`-invariant subspace containing `Ψ`") is vacuous for the same reason.

*The `m`-dependence is real, in the shard's own model.*  `D16`, `Δ=2.5`,
`N=12`, `c_0=6`, windows `[4,9]⊂[3,10]⊂[2,11]`, at `(t_-,t_+)=(−8,+9)`:

| `W_m` | `2Σ_q‖𝒩_{W_1}η_q^{(m)}‖²` | RHS of (LRD.13) as derived |
|---|---|---|
| `[4,9]` | 1.3829 | 2.0784 |
| `[3,10]` | 1.7971 | 2.4926 |
| `[2,11]` | 1.8725 | 2.5680 |

a `24%` spread, and **increasing** in `m` — the opposite direction from the
one the lemma needs.  (NR) of ⟨2⟩7 bounds only the `m=1` entry (it is written
with `E_{W_1,t_-}({q})Ψ` explicitly), so THEOREM (LRD-3) does not follow from
it.  What the monotonicity lemma actually removes is the `m`-dependence of the
majorising **observable**, not of the majorising **state**.

I searched for a numerical counterexample to the `W_1`-pinched bound over a
`25×25` grid `t_-∈[−24,0]`, `t_+∈[0,24]` and all three windows: the largest
value of `Σν²p_{W_m} − RHS^{(W_1)}` is `−0.095`.  So the claimed inequality is
not *refuted* at `N=12` — it is simply **not derived**, and (see M4) the
checker cannot see the difference.

**(c) FIX DEMAND.**  Replace (NR)'s second clause by its `sup_m` form —
`sup_m sup_{t_-<t_+} Σ_q‖α_{t_+}(𝒩_{W_1})E_{W_m,t_-}({q})Ψ‖² < ∞` — and
delete every claim that the monotonicity lemma removes `sup_m` "for free",
replacing it with: the lemma reduces the `m`-dependent family of majorising
observables `{𝒩_{W_m}}` to the single fixed `𝒩_{W_1}`, and nothing more.

**(d) SURVIVING WEAKER STATEMENT.**  (i) `𝒩_{W'} ⪯ 𝒩_W` for `W ⊆ W'`, and
`|Q̂_{W^c,c_0}| ⪯ 𝒩_W` — both correct, both verified; the squaring step is
legitimate here (though the shard never says why) only because the two
operators are simultaneously diagonal.  (ii) (LRD.11), (LRD.12) and the
Chebyshev step ⟨2⟩2 are correct and I re-derived all three independently.
(iii) **THEOREM (LRD-3) holds verbatim under the repaired (NR)** — so the
result is recoverable at the cost of admitting a `sup_m` inside the
hypothesis, with the same explicit tail bound `2S_{NR}/M`.  (iv) The
cross-lane conclusion survives in weakened form: since the majorising
*observable* is the fixed `𝒩_{W_1}`, an escaped increment `|ν| ≍ 2s|W_m|`
still cannot be manufactured by window geometry or by the `c_0` offset — it
still requires the fixed quantity `𝒩_{W_1}` to be large, either in `Ψ` or in
the dephased state.  That is enough for §H's cross-lane paragraph, once
reworded.

---

### M1 (MAJOR) — MP-1's D27 edit: **HOLD**

**(a) Location.**  `theory/lr-d16.md` §MP, MP-1; asserted at ⟨1⟩6.⟨2⟩2
("D27(LR1) can be demoted from hypothesis to corollary without weakening
`M-INDEX-spec`") and §H item 1 ("D27 carries as a hypothesis something that is
a theorem").

**(b) My computation.**  I checked the quantifier structure of D27 verbatim.
`(LR)` is a single existential over one sequence: *"There is one sequence
`T_n→∞` such that, for every fixed `W`, … converge"* (clause 1), and clauses 2
and 3 then speak about **that** sequence — clause 3 begins "Writing `p_W` for
the fixed-window time limit", which exists only because clause 1 supplied
`T_n`.  `memory-index.md` ⟨1⟩7.⟨2⟩1 consumes exactly this: "double Cesàro
averaging of (IDX.4), **followed by the common subsequence**".

LR1-GEN proves `∃T_n:` clause 1.  It does **not** prove that the `T_n`
produced by that compactness argument satisfies clauses 2--3, and clause 1 is
therefore not removable: delete it and `p_W` is undefined and clauses 2--3
lose their binder.  MP-1's own last sentence ("retained … only so that D27
reads as a self-contained package") mis-describes why it must be retained, and
a reader who takes "LR1 is a theorem, not a hypothesis" at face value may
conclude that any `T_n→∞` will do.  It will not.

The genuinely correct and useful statement — which the shard has earned and
should claim — is: *for **any** sequence `T_n→∞` there is a subsequence along
which clause 1 holds; hence the entire content of `(LR)` lies in clauses 2 and
3, and clause 1 costs nothing and constrains nothing.*  (This also exposes a
real ambiguity in D27 that the edit would freeze in place: clause 2's "tends
to zero" does not say whether the limit is over `T→∞` or along `T_n`.
`memory-index.md` reads it along `T_n`.)

**(c) FIX DEMAND.**  HOLD MP-1 as written; re-propose it as the subsequence
form above, keeping clause 1 explicitly as the binder of `T_n`, and add one
clause fixing D27(LR2)'s limit as *along `T_n`* to match `memory-index.md`
⟨1⟩7.⟨2⟩1.

**(d) SURVIVING WEAKER STATEMENT.**  LR1-GEN itself is fully correct and is
the strongest result in this shard (see §2).  It merits a PROVED `CLAIMS.md`
row on its own; it does not merit an edit to D27 in the form proposed.

---

### M2 (MAJOR) — the volunteered negative class result exhibits no model, and its mechanism contradicts (FN)

**(a) Location.**  ⟨1⟩6.⟨2⟩5 ("**'gap + Lieb--Robinson ⟹ (LR)' is FALSE as a
class statement**"; "Such a model can be finite range and gapped"), with the
same assertion at ⟨1⟩2's Remark and §H item 11 ("**refuted as a class
statement** … a gapped, finite-range model with a mobile charged core
satisfies both and fails LR3").

**(b) My computation.**  ⟨1⟩6.⟨2⟩5 **names no model, constructs none, and
cites none**.  It asserts that one exists.  I looked for one, in the corpus
and by construction, and the situation is worse than "unproved":

1. *The corpus does not supply it.*  `theory/ace-ld.md` ⟨1⟩5
   (ACE-LD-obst′, the confirmed cross-lane obstruction) is a statement about a
   **hypothesis class** `(M-ESC)` — mean tail transport `θ>0` — not about a
   model; its scope paragraph says in terms "A kink component transiting every
   fixed window with asymptotic mean weight `p_tr>0` gives `θ=p_tr`", and
   `theory/ace-ld.md` §0 records that r1's sentence "on the fixed-packet class
   of D28 the kink is ballistic" was **FALSE** (verdict F1(b)(iv)) and is
   withdrawn.  No gapped finite-range instance is exhibited anywhere.
2. *The stated mechanism is inconsistent with (FN), which this shard proves.*
   ⟨1⟩6.⟨2⟩5 blames "a charge-carrying core that transits a window
   ballistically".  But under `U(1)` conservation the sharp-kink position and
   the regularised charge are the same variable: by the shard's own (LRD.1)
   and (LRD.5), a sharp wall at `c_0+d` has `𝒬 = +d`, so on the `𝒬=𝒬_0`
   eigenspace the wall position is **pinned** and cannot drift at all.  A
   `|ν| ≍ 2s|W_m|` swing therefore cannot come from rigid core transit in this
   register; it requires `𝒩_{W_m} ≍ |W_m|`, i.e. an unbounded wrong-phase
   **block**, which is a different mechanism (and is exactly the one ⟨1⟩5.⟨2⟩7
   correctly names as the gap between (EDW) and (NR)).  So the sketch does not
   even describe a counterexample to LR3-CLASS as displayed, whose clause 2 is
   (C-FN).

**(c) FIX DEMAND.**  Downgrade ⟨1⟩6.⟨2⟩5 from "FALSE / refuted" to "not
supported by this shard, and not obtainable from it", or exhibit an explicit
finite-range, `U(1)`-invariant, gapped model with two `±s` vacua and a D17
state realising `θ>0`; and delete the "mobile charged core" phrasing, which is
excluded by (LRD.5) on the `(FN)` register.

**(d) SURVIVING WEAKER STATEMENT.**  Two things are true and are worth
recording exactly as they stand: (i) **a spectral gap is used at no step of
this shard, and a Lieb--Robinson bound only to build `α_t`** — I verified this
by reading ⟨1⟩3--⟨1⟩5 for every appeal to a velocity or a gap and found none;
so the D16 proof gives no evidence for a "gap + LR" class theorem, and
⟨1⟩6.⟨2⟩1's inventory table is accurate.  (ii) Any class theorem must carry a
no-mean-transport clause, because `ace-ld.md`'s ACE-LD-obst′ shows D27(LR3)
fails whenever `(M-ESC)` holds.  That is a scoping argument, and it is a good
one — it is simply not a refutation.

---

### M3 (MAJOR) — §H upgrades the fenced ⟨1⟩5.⟨2⟩8 into a K4-strength model statement

**(a) Location.**  §H, "Bearing on the live cross-lane obstruction": "⟨1⟩5.⟨2⟩8
proves that D16's exact zero-energy kink family is degenerate, **so the D16
core has no group velocity and D16 sits outside the ballistic class**"; same
upgrade at ⟨1⟩2's Remark ("the whole zero-energy kink family of K1--K2 sits at
one common energy, so **the wall carries no group velocity**") and at
⟨1⟩6.⟨2⟩4 clause 3, which describes (C-imm) as "the zero-energy … kink
**manifold** is exactly degenerate … — the property proved for D16 in
⟨1⟩5.⟨2⟩8".

**(b) My computation.**  ⟨1⟩5.⟨2⟩8 proves, correctly and from K1+K2 only, that
`\overline{span}\{|K̄(z)⟩\} ⊆ ker H_kink`, hence that vectors **in that span**
are stationary.  It proves nothing about `ker H_kink ∖ 𝒦_flat` and nothing
about a band.  "The D16 core has no group velocity", "the D16 wall carries no
group velocity" and "the kink **manifold** is exactly degenerate" are
statements about the model, i.e. they need the kernel to be exhausted by the
family — which is precisely **K4**, a CONJECTURE row.  `corner-b-draft.md`
§1.2 states the prohibition in terms: *"No no-recoil, unique-torsor, or
all-`Δ` dynamical statement may cite K4 as proved."*  The shard's own fence
⟨1⟩5.⟨2⟩8(i)--(ii) says exactly the right thing; §H, ⟨1⟩2 and ⟨1⟩6.⟨2⟩4 then
say more than the fence allows.  This is a lockstep failure between the proof
layer (fenced, correct) and the summary layer (unfenced), of exactly the kind
the brief asked me to check strictly.

Nothing in the *proof* layer relies on K4: I verified ⟨1⟩5.⟨2⟩8's leaves
against K1 and K2 as stated in `corner-b-draft.md` §1.2 and recomputed the
`2×2` kernel condition independently (see §2, item 3).  The reliance is
confined to the summary sentences.

**(c) FIX DEMAND.**  In §H, ⟨1⟩2's Remark and ⟨1⟩6.⟨2⟩4 clause 3, replace
"the D16 core/wall has no group velocity" and "kink manifold" by "every state
in the closed span of the K1--K2 family is exactly stationary", and add "the
statement that this span exhausts the low-energy kink states is K4
(CONJECTURE) and is not used".

**(d) SURVIVING WEAKER STATEMENT.**  ⟨1⟩5.⟨2⟩8 as fenced: `𝒦_flat ⊆ ker H_kink`
from K1+K2 alone, with `Ψ ∉ 𝒦_flat`.  That is a genuine, correctly-derived,
K4-free result and it does motivate (NR).  It does not place D16 outside any
class by itself.

---

### M4 (MAJOR) — checker: two no-op gates, one gate blind to the claim it advertises, 10 of 18 rows unreachable

Green run reproduced: `python3 -O theory/checks/lr_d16_check.py` → **exit 0**,
18/18, all §C values matching to the printed digits.  All four red modes
reproduced: **exit 1**, rows exactly as tabulated.  Both source-level
mutations reproduced on copies: wrong root `q=Δ+\sqrt{Δ²−1}` → **exit 1**
(C1(c), C5(a), C6(b)); `c_0=5` → **exit 0**, 18/18.  No bare `assert`; `-O` is
equally strict.  Credit where due — the non-over-fitting check is real.  The
following are the defects.

**(a) Locations.**  `theory/checks/lr_d16_check.py` `row_c1` (LRD-C1(b)),
`row_c3` (LRD-C3(a), LRD-C3(d)), module docstring `--red-monotone` line.

**(b) My computations.**

*(i) LRD-C1(b) "integer support" is a no-op.*  `spec` is
`np.unique(np.round(q_w,9))`; `allowed = {int(round(x−y))}` over `spec×spec`;
and inside `tpm_law` the key is `nu = int(round(q − qp))` with `q,qp` drawn
from the **same** `spec`.  So `set(p) ⊆ allowed` is true by construction for
any input, and `ok_int`'s test `abs(nu − round(nu)) < 1e-12` compares a Python
`int` with its own `round` — identically `0`.  **Data mutation on a copy:**
replace `rho_ref` by `0.3 / −0.7`, so that `spec Q̂_W ⊄ ℤ` and the row's stated
content is false.  Result: `LRD-C1(b) integer support: PASS, |allowed| = 11`
— unchanged.  (The run does exit 1, but via C2(c) and C3(c), not via the
integrality row.)

*(ii) LRD-C3(a) "second-moment identity (LRD.11)" is a no-op.*  Both sides are
built from the same `etas`: `lhs = Σ_ν ν² law[ν]` where `law` was accumulated
as `law[q−q'] += Σ_{j∈block(q')}|η_q|²_j`, and `rhs = Σ_q Σ_j |η_q|²_j
(q_w[j]−q)²`.  Since `q_w[j] = q'` on `block(q')`, the two are the same sum
regrouped: `0 ≡ 0`.  The row never forms `α_{t_+}(Q̂_W)`, never forms
`(ΔQ̂_W)²`, and never applies `𝒟_{W,t_-}` — i.e. it never touches the content
of (LRD.11).  **Mutation on a copy:** make `Propagator.evolve` non-unitary
(`return 1.37*…`).  Result: `Σ_ν p = 2.52` (C1(a) fails, correctly), and
`LRD-C3(a): PASS, max|LHS−RHS| = 1.78e−15`.  A gate that survives a
non-unitary "dynamics" is testing arithmetic, not physics.
*(For the record I did verify (LRD.11) myself by the independent route — see
§2, item 5 — so the identity is true; the row is what is empty.)*

*(iii) LRD-C3(d) is blind to the `m`-independence it advertises.*  It computes
`t2u` from `etas`, i.e. from the `W_m` blocks, so it evaluates the *derived*
(`m`-dependent) right-hand side, not the *claimed* (`W_1`-pinched) one.
**Mutation on a copy** implementing the shard's actual claim — recompute
`etas1` from `W_1`'s blocks and use those in `t2u`: result **identical**,
`max slack over 3 windows = −1.211e−01`, exit 0.  The row cannot distinguish
the two readings, because the maximum is attained at `m=1` where they
coincide.  So the shard's flagship claim F2 attacks has no certificate at all.
(The row is not vacuous: halving the majorant, `maj1 → 0.5*n_w1`, kills it,
slack `+2.745`.  It has teeth against the constant, none against the
quantifier.)

*(iv) Reachability.*  Exit paths, by mutation:

| mutation | rows that fire |
|---|---|
| `--red-split` | C2(c), C3(b) |
| `--red-edw` | C4(a), C4(b), C4(c) |
| `--red-monotone` | C3(c) **only** |
| `--red-sharp` | C5(a), C6(b) |

**10 of the 18 rows are killed by no shipped red mode**: C1(a), C1(b), C1(c),
C2(a), C2(b), C2(d), C3(a), C3(d), C5(b), C6(a).  Among them are both no-ops
(C1(b), C3(a)) and the row carrying the F2 claim (C3(d)).  The module
docstring states that `--red-monotone` must fail "LRD-C3(c,d)"; it fails only
C3(c) (the §C table in the shard is correct here; the docstring is not).

*(v) Deductive subsumption.*  `LRD-C6(b)` (`⟨v|H_kink|v⟩ = 0` for
`v = env["dressed"]`) is implied by `LRD-C5(a)` (`‖H_kink v‖ = 0` for the same
vector in the same sector); likewise the "0 attained" half of C5(b).  C6(b)
additionally prints "`E_kink(used) = 4.52e−17 (dressed reference 4.52e−17)`"
— in green mode `used` and `zero` are literally the same vector, so the
parenthetical is a comparison of a number with itself.

**(c) FIX DEMAND.**  (1) Rebuild LRD-C1(b) to test `spec Q̂_W ⊂ ℤ` on the raw
`q_w` array (`max|q_w − round(q_w)|`), not on already-rounded keys.  (2)
Rebuild LRD-C3(a) to form `α_{t_±}(Q̂_W)` as matrices and compare
`Σ_ν ν²p` with `⟨Ψ,𝒟_{W,t_-}((ΔQ̂_W)²)Ψ⟩` computed from them (my §2 item 5
recipe), and add a red mode that perturbs one of the two evolutions.  (3)
Split LRD-C3(d) into `C3(d-i)` (derived, `W_m`-pinched) and `C3(d-ii)`
(claimed, `W_1`-pinched), with a red mode for each.  (4) Add red modes
reaching C1(a)/C1(c)/C2(a)/C2(b)/C2(d)/C5(b)/C6(a), or delete the
"18/18 rows" framing and state which rows are decoration.  (5) Fix the
`--red-monotone` docstring.

**(d) SURVIVING WEAKER STATEMENT.**  The checker's genuine certificates are
LRD-C2(c), C3(b), C3(c) (red-certified by `--red-split`/`--red-monotone`),
C4(a)(b)(c) (red-certified by `--red-edw`), C5(a) and C6(b)
(red-certified by `--red-sharp`) — eight rows with live red paths, all of
which I reproduced.  That is a respectable certificate set; the claim of "18
registered rows, four red modes" overstates it by a factor of two.

---

### m1 (MINOR) — unbounded-operator hygiene is asserted, never established

**(a)** ⟨1⟩1.⟨2⟩5--⟨2⟩6, (LRD.4), (LRD.5); ⟨1⟩4.⟨2⟩4--⟨2⟩5; ⟨1⟩5.⟨2⟩3--⟨2⟩6.
**(b)** `𝒬`, `𝒩_W`, `Q̂_{W^c,c_0}` and `D` are **not** elements of `𝔄`, yet
`α_t(·)` is applied to all four and `α_t` is defined on `𝔄`.  ⟨1⟩1.⟨2⟩5
asserts essential self-adjointness of `𝒬` on the finite-deviation span and
implementability of `α_t` on `ℋ_ref` with a one-line justification; nothing is
said for `𝒩_W` or `D`.  Also, ⟨1⟩4.⟨2⟩5(i) and ⟨1⟩5.⟨2⟩4 pass from `A ⪯ B` to
`A² ⪯ B²`, which is **false** for general positive operators (squaring is not
operator monotone) and is legitimate here only because `𝒩_{W'}` and `𝒩_W` are
simultaneously diagonal.  The shard never says so.
**(c)** State once, in ⟨1⟩1.⟨2⟩5, the common core (finite-deviation
configurations), essential self-adjointness for `𝒬, 𝒩_W, D` on it, invariance
of the core, and the sentence "all inequalities among these operators are
pointwise on configurations, so squaring preserves them".
**(d)** Every displayed inequality is *true* on the natural core; only the
hygiene is missing.

### m2 (MINOR) — LRD-C4(b) treats a non-conserved quantity as conserved

**(a)** `row_c4`, the `bound = e0 / gapc` line; certifies ⟨1⟩5.⟨2⟩6 (LRD.15).
**(b)** The checker propagates with `hk_e` (`H_kink`) but computes
`E_0 = ⟨Ψ,H_XXZ Ψ⟩` at `t=0` and treats it as conserved.  On a 12-site *open*
chain `H_kink = H_XXZ − (J/2)\sqrt{Δ²−1}(S^z_1 − S^z_{12})` and the two do not
commute: `‖[H_kink,H_XXZ]‖ = 16.60`.  Measured drift of `⟨H_XXZ⟩(t)` under the
checker's own propagator: `+0.060` at `t=3`, `−0.344` at `t=12`, `−0.621` at
`t=48` (against `E_0 = 3.5647`).  K3's telescoping equivalence is an
*infinite-chain* statement; at `N=12` it is a boundary term with teeth.  The
row still passes on `t∈[−12,12]` (slack `−1.67`), so nothing is refuted.
**(c)** Either evolve with `hx_e` for this row, or compare `⟨D(t)⟩` against
`2⟨H_XXZ⟩(t)/(J(Δ−1))` at the same `t`, and say in §C that K3 is exact only in
infinite volume.
**(d)** (EDW) itself — `h^{XXZ}_{x,x+1} ⪰ (J/2)(Δ−1)P^{DW}_x`, hence
`H_{XXZ} ⪰ (J/2)(Δ−1)D` and `⟨α_t(D)⟩ ≤ 2E_0/(J(Δ−1))` — is correct in
infinite volume; I re-derived the `4×4` block independently (§2, item 6).

### m3 (MINOR) — ⟨1⟩4.⟨2⟩6 misdiagnoses its own residue

**(a)** ⟨1⟩4.⟨2⟩6, "`G(W)>0` at fixed `W`: for the D16 dressed kink the window
charge is **not** exactly sharp, because the K1--K2 kink profile has
exponentially small but nonzero weight across each window edge"; repeated at
§H item 8.
**(b)** The kink-tail contribution is `O(q^{2d_W})` with `q = 0.2087` at
`Δ=2.5` — utterly negligible.  The actual residue is the **escaped magnon**,
`O(1)` at every window (F1: `G(m) = 0.99, 0.97, 0.95`).  Naming the wrong
mechanism is what makes the "logarithmically faster padding" rate of ⟨1⟩2 look
plausible; naming the right one makes F1 immediate.
**(c)** Replace the clause by "because the D17 packet's magnon leaves every
fixed window, contributing `≈1` to `𝒩_W` at large `|t|`".
**(d)** (DPH) remains correctly identified as the missing dephasing statement,
and correctly marked CONJECTURE.

### m4 (MINOR) — LRD-C2(d) measures a different quantity from (LRD.10), under a misleading caption

**(a)** `row_c2`'s escape-profile block; §C row LRD-C2(d).
**(b)** (LRD.10) defines `G(m) = sup_t⟨α_t(𝒩_{W_m})²⟩`; the code computes
`sup_t⟨α_t(Q̂_{W_m^c})²⟩`, a strictly smaller quantity (`|Q̂_{W^c}| ⪯ 𝒩_W`),
over `t∈[−12,12]` only.  The caption "escape profile falls with padding"
describes a monotonicity test whose 6% fall is a finite-`N` artefact of the
outside region shrinking from 6 sites to 2 (F1).
**(c)** Compute `n_w` rather than `q_wc`, widen the time grid, and re-caption
as "escape profile is `O(1)`, not decaying — (LR2′)'s sufficient condition
fails here".
**(d)** The numbers themselves are correct and are, read properly, the
strongest evidence in the file — for F1.

### m5 (MINOR) — the "consumed at exactly one leaf" audit is textually wrong

**(a)** ⟨1⟩4.⟨2⟩7, first sentence.
**(b)** I grepped every occurrence of `LR2` in `theory/memory-index.md`.
D27(LR2) is cited at **two** leaves, not one: ⟨1⟩7.⟨2⟩1 (the genuine consumer)
**and ⟨1⟩5.⟨2⟩1**, whose *Justification* line reads "D27(LR2); the first
projection is the initial measurement…".  The second citation sits inside
`M-INDEX-fin`'s `where-proved` (`⟨1⟩1, ⟨1⟩5`), a *different* PROVED row.
Checking the content: ⟨1⟩5.⟨2⟩1 merely displays the TPM law and needs D27's
**clause-1 display**, the two spectral resolutions and offset cancellation
(⟨1⟩5.⟨2⟩3) — it does not use the dephasing defect.  So the citation is a
mis-citation in `memory-index.md`, the content claim survives, and
`M-INDEX-fin` is not at risk.  (Also checked: `theory/soft-index-b.md` lines
594 and 1018 mention D27(LR1--LR2) only as an *analogy* for (TGT2), not as a
consumer; `theory/memory-index-b.md`'s "(LR2)" is that shard's own private
label for uniform charge tightness, a different statement.)
**(c)** Restate as "consumed at exactly one leaf **by content**
(⟨1⟩7.⟨2⟩1); ⟨1⟩5.⟨2⟩1 cites D27(LR2) but uses only D27's clause-1 display —
that mis-citation is referred to the `memory-index` lane", and add the note to
MP-2.
**(d)** The mitigation's leaf audit is right on content; only its "exactly
one" count is wrong.

### m6 (MINOR) — ⟨1⟩3's ASSUME over-lists its hypotheses

**(a)** ⟨1⟩3 ASSUME ("(H1), (H3) of ⟨1⟩2") vs ⟨1⟩3.⟨2⟩7 ("no property of `Ψ`
beyond normalisation") and ⟨1⟩2's (LRD-1) bullet ("from (H1), (H3) alone").
**(b)** (H3) is D17 + the dressed-kink preparation + the magnon profile.  None
of it is used: ⟨2⟩1--⟨2⟩6 use separability, strong continuity, finiteness of
`spec Q̂_W`, and `‖Ψ‖=1`.  (H1) is used only to know `α_t` exists.
**(c)** Change ⟨1⟩3's ASSUME to "(H1) for the existence of `α_t`; `‖Ψ‖=1`".
**(d)** LR1 is *stronger* than advertised, not weaker.

### n1 (NOTE) — LRD-C4(c)'s "coincidence" is an identity

`E_0/c = \sqrt{(Δ+1)/(Δ−1)}` is not a numerical cross-check: given
⟨1⟩1.⟨2⟩2's `E_0 = C_K = (J/2)\sqrt{Δ²−1}` and `c = (J/2)(Δ−1)`, the ratio is
`\sqrt{Δ²−1}/(Δ−1) ≡ \sqrt{(Δ+1)/(Δ−1)}` identically.  §H calls it "a pleasant
but unclaimed cross-check"; §C calls it agreement "to 4 decimals, on a finite
chain".  It is a tautology *once* `E_0 = C_K` — and *that* is the real
finite-`N` check, which I ran: `⟨K|H_XXZ|K⟩ = 1.1456439081` against
`C_K = 1.1456439237`, agreement to 8 decimals.  Re-caption accordingly.

### n2 (NOTE) — the diagonal sequence needs one word

⟨1⟩3.⟨2⟩5's `T_n := T_n^{(2+n)}` requires the standard proviso that the `n`-th
diagonal entry be chosen with index `≥ n` (else `T_n` need not be increasing).
One clause fixes it.

### n3 (NOTE) — the cross-lane consistency claim is correct

§H's "consistent with, and logically independent of" the ballistic-transit
lane is right, and I verified it from the other side: `ace-ld.md`'s
ACE-LD-obst-prime row states in its own scope "NOT claimed: any statement
about D16 or any confined-kink class (`θ=0` there — the bd `tns-xf4` lane is
NOT pre-empted)".  Both lanes agree; there is no cross-lane contradiction.
(This is independent of M2, which is about the *class* statement, not about
the other lane.)

---

## 2. VERIFIED CORRECT — fenced, do not churn

Each item was recomputed independently, by the route stated.

1. **⟨1⟩1.⟨2⟩3, the calibration.**  `2s(𝔛_W − c_0)` with D13(a)'s
   `𝔛_W = a−1+\frac{1}{2s}Σ_{x∈W}(S^z_x+s)` at `s=1/2` gives
   `a−1−c_0+Σ_{x∈W}(S^z_x+½)`, and `Σ_{x∈W}(ρ_{c_0}(x)+½) = c_0−a+1`, so
   `Q̂_{W,c_0} = Σ_{x∈W}δ_x` **exactly** — no offset, no factor.  Spectrum
   `⊆ [a−1−c_0, b−c_0] ⊂ ℤ`, at most `|W|+1` values, `‖Q̂‖ ≤ R_W ≤ |W|`.  All
   confirmed.
2. **⟨1⟩1.⟨2⟩2, the orientation bookkeeping — this is careful, correct, and
   not cosmetic.**  D16's displayed family `⊗(|↑⟩+zq^n|↓⟩)` with `q∈(0,1)` is
   `↓` at `−∞` and `↑` at `+∞`, i.e. opposite to D13(a); the `ℤ₂` image
   `⊗(|↓⟩+zq^n|↑⟩)` with the reversed field is the right one; telescoping over
   `[−L,L]` gives `S^z_{−L}−S^z_{L} → 1`, hence
   `H_kink = H_XXZ − C_K`, `C_K = (J/2)\sqrt{Δ²−1} > 0`.  **Numerically
   confirmed at `N=12`, `Δ=2.5`:** `⟨K|H_XXZ|K⟩ = 1.1456439081` vs
   `C_K = 1.1456439237`.  The sign-consistency argument (the opposite
   bookkeeping would give `−C_K < 0`, contradicting `H_XXZ ⪰ 0`) is right.
3. **⟨1⟩5.⟨2⟩8 uses K1+K2 and never K4 — verified strictly.**  In the (LRD-O)
   sign the `(|↑↓⟩,|↓↑⟩)` block of `h^kink` is
   `[[JΔ/2−C, −J/2],[−J/2, JΔ/2+C]]`, `C=(J/2)\sqrt{Δ²−1}`; its kernel
   condition is `a = qb` with `q = Δ−\sqrt{Δ²−1}`, and I checked **both**
   equations close: the second reduces to `−1 + (Δ+\sqrt{Δ²−1})(Δ−\sqrt{Δ²−1})
   = −1 + 1 = 0`.  This is the `ℤ₂` mirror of `corner-b-draft.md` §1.2's
   `|↑↓⟩+q^{-1}|↓↑⟩`, and it is exactly the family the checker builds
   (`⊗(|↑⟩+zq^{-n}|↓⟩)`), so §C's "notation bridge" is sound and load-bearing
   (the wrong root fails, reproduced).  Kernel of a positive operator is
   closed, so `𝒦_flat ⊆ ker H_kink`.  **No step of ⟨1⟩5.⟨2⟩8 touches K4.**
   (K4-strength language appears only in the summary layer — M3.)
4. **⟨1⟩3 (LR1) — PROVED, quantifiers correct, and it is the best thing here.**
   `𝔄` is separable (countable directed family of finite matrix algebras,
   rational words); `α_t` is norm-continuous in `t` for finite range;
   `S(𝔄)` is weak-\* compact **and metrizable**, hence sequentially compact;
   `spec Q̂_{W,c_0}` is finite because `𝔄_W` is finite-dimensional (the
   shard's sharper reason — diagonal with `≤|W|+1` integer values — is also
   right); `𝕀 = \{(W,ν)\}` is countable; Cantor diagonal.  The extraction is
   done **once**, before any window is fixed, so the sequence serves **every**
   `W` simultaneously — D27's "one sequence `T_n→∞` such that, for every fixed
   `W`" is delivered, not a `W`-dependent subsequence.  Strong continuity is
   enough; no uniformity in `t` is needed anywhere.  `p_W` is a probability on
   the fixed finite set `σ_W−σ_W ⊂ ℤ`, so no mass escapes.  **LR1-GEN
   (⟨1⟩6.⟨2⟩2) is correct as stated** and deserves its own PROVED row.
5. **⟨1⟩5.⟨2⟩1, the second-moment identity (LRD.11) — verified by an
   independent route.**  I built `α_{t_±}(Q̂_W)` as explicit matrices
   `U_t^† \mathrm{diag}(q_w) U_t`, formed `ΔQ̂_W`, built the pinching
   `Σ_q P_q^{(t_-)}(ΔQ̂_W)²P_q^{(t_-)}`, and compared with `Σ_ν ν²p` computed
   from the TPM law: `0.5483368101` versus `0.5483368101`, difference
   `1.1e−15`, at `(t_-,t_+)=(−8,+3)`, `W=[4,9]`.  (This is the check LRD-C3(a)
   should have been — M4(ii).)  The algebra of ⟨2⟩1 is also right on paper:
   `⟨φ_q,(A−q)²φ_q⟩ = ⟨φ_q,(A−Q̂(t_-))²φ_q⟩` because `Q̂(t_-)φ_q = qφ_q`.
6. **⟨1⟩5.⟨2⟩6 (EDW).**  In `(|↑↓⟩,|↓↑⟩)`,
   `h^{XXZ} = (JΔ/2)I − (J/2)σ^x`, eigenvalues `(J/2)(Δ∓1)`, and `h^{XXZ}`
   annihilates `|↑↑⟩,|↓↓⟩`, so `h^{XXZ} ⪰ (J/2)(Δ−1)P^{DW}` bondwise and
   `H_{XXZ} ⪰ (J/2)(Δ−1)D ⪰ 0`.  Correct.  A bonus the shard asserts but does
   not prove, and which is in fact derivable: `E_0 < ∞` on a D17 packet,
   because `P^{DW}_x ⪯ n_x + n_{x+1}` with `n` the deviation from the local
   vacuum and `0 ⪯ h_x ⪯ (J/2)(Δ+1)P^{DW}_x`, so `E_0 ≤ (J/2)(Δ+1)Σ_x⟨P^{DW}_x⟩
   < ∞` by D17's `ℓ¹` clause.
7. **⟨1⟩4.⟨2⟩1--⟨2⟩4.**  `Δ_W = −Σ_{q≠q'}⟨φ_q,Aφ_{q'}⟩`; the boundary-current
   form with `𝒥_W = i[H,Q̂_W] = j_{a−1|a} − j_{b|b+1}` (I checked D10(a)'s sign
   convention against D26's `S^z = −iq(ξ)`: it closes exactly), `Δ_W(t,t)≡0`,
   `‖𝒥_W‖ ≤ C_j` independent of `W`; the `4‖A‖ε` estimate
   (`2‖A‖ε + ‖A‖ε² + ‖A‖ε² ≤ 4‖A‖ε` for `ε≤1`); and
   `ε_W(t)² ≤ ⟨α_t(Q̂_{W^c})²⟩ ≤ ⟨α_t(𝒩_W)²⟩` using `|q−𝒬_0|≥1` on the integer
   spectrum.  All correct.
8. **⟨1⟩5.⟨2⟩2--⟨2⟩5.**  Chebyshev (`1+|ν| ≤ 2|ν|` for `|ν|≥1`,
   `|ν| ≤ ν²/M` for `|ν|>M≥1`, giving `2S/M`); the edge split
   (`2X²+2Y²−(X−Y)² = (X+Y)² ⪰ 0`, and `𝒟_{W,t_-}` acting as the identity on
   `α_{t_-}(Q̂_{W^c})²` because that operator commutes with every `P_q`); the
   monotonicity `𝒩_{W'} ⪯ 𝒩_W` and `|Q̂_{W^c}| ⪯ 𝒩_W`; Fatou on the counting
   measure.  All correct.  Only the *`m`-independence conclusion* drawn from
   them fails (F2).
9. **Fences and reliance audit — clean.**  No REFUTED row is relied on
   (`M-INDEX-LA-strong` is cited only to fence against it, and the ⟨1⟩1.⟨2⟩5
   fence is exactly right: the `memory-index.md` ⟨1⟩3 counterexample does not
   satisfy (FN)).  The `n≥2` display of ML4-Ward (9) appears nowhere.  Bethe
   appears nowhere, as hypothesis or otherwise; no closed factorisation, no
   `t(k)`/`T(k)`/`δ_t(k)` from `corner-b-draft.md` §5.2.  `𝒮_W` at `ρ≠1/2` is
   irrelevant here (`s=1/2` throughout).  No `k→0` or plane-wave limit is
   taken.  The frozen limit order of ⟨1⟩1.⟨2⟩8 is respected at every step I
   checked, including inside ⟨1⟩4.⟨2⟩7's Cesàro estimate — the `η_m` error is
   introduced at fixed `W_m` and only then is `m→∞` taken; there is **no**
   interchange.  D27(LR3)'s optional convenience clause is correctly declared
   not proved and not needed.
10. **Checker, reproduced.**  Green exit 0, 18/18, values matching §C.
    `--red-split` → exit 1 (C2(c) `+9.99e−2`, C3(b) `+2.476`);
    `--red-edw` → exit 1 (C4(a) `−1.000`, C4(b) `+1.047`, C4(c));
    `--red-monotone` → exit 1 (C3(c) `+1.000`);
    `--red-sharp` → exit 1 (C5(a) `0.511`, C6(b) `0.104`).
    Source-level mutations on copies: wrong root → exit 1 (C1(c), C5(a),
    C6(b)); `c_0=5` → exit 0, 18/18.  Both `--red-split` and `--red-monotone`
    are genuine, distinct, load-bearing red certificates and neither is
    bit-identical to another.  No bare `assert`.

---

## 3. Register comparison against `M-INDEX-spec`

`M-INDEX-spec`'s adjudicated scoping sentence is the register: *"Proved only
as the conditional implication … D27 is assumed, not derived; no implication
H-AD-G ⟹ (LR) is claimed; no sector-wide total-charge operator is
constructed…"* — i.e. every hypothesis named, nothing derived that was
assumed, no upgrade of a conditional into a fact.

**§H is in that register and is the best-written section of the shard.**  It
names (NR), names (DPH), refuses the operator-commutativity patch in terms,
declares "`M-INDEX-spec` still has no fully unconditional dynamical instance",
and MP-4 repeats it.  **The other layers are not.**  §0's summary table says
(LR2′) "is PROVED … and is shown to suffice for every downstream use" where §H
says "conditional only on the escape profile"; ⟨1⟩2 asserts a decay rate for
`η_m` that ⟨1⟩4 never proves and that the shard's own numerics contradict;
⟨1⟩5.⟨2⟩4 and §H item 3 both assert the `sup_m` is removed "for free"; and §H's
cross-lane paragraph and ⟨1⟩2's Remark carry K4-strength language that
⟨1⟩5.⟨2⟩8's own fence forbids.  MP-3's `LR-D16` row would carry both errors
into the DAG.  So the answer to the lockstep audit is: **statement, proof
shard and HONEST STATUS agree on LR1; they diverge on LR2 and LR3, in the
direction of the summary layer being stronger than the proof layer.**

---

## 4. Answers to the four questions the brief asks in terms

- **LR1:** PROVED unconditionally for D16, and at class level (LR1-GEN).  One
  sequence, every window, no gap, no LR velocity, no property of `Ψ` beyond
  normalisation.  Confirmed by recomputation.  This is a real result.
- **(LR2′):** proved only as `|avg Δ_{W_m}| ≤ 4R_{W_m}\sqrt{G(m)}`, whose
  right-hand side **diverges** for the shard's own state class.  Strength:
  **empty for D16**.  D27(LR2) verbatim remains OPEN, correctly, with (DPH)
  named.
- **LR3:** the route is sound and the ingredients are correct, but the theorem
  does not follow from **(NR) as stated**; it follows from (NR) with `sup_m`
  restored in the pinched clause.  Strength: **conditional on a repaired,
  slightly stronger (NR)**.
- **The LR2 mitigation** does **not** hold: the leaf audit is right on content
  (one genuine consumer, `memory-index.md` ⟨1⟩7.⟨2⟩1; a second, harmless
  mis-citation at ⟨1⟩5.⟨2⟩1), and the error-before-limit/removed-by-limit
  structure is right, but the error is not removed because `η_m → ∞`.
  Consequence for `M-INDEX-spec`: **none, in either direction.**  It is
  neither damaged nor improved; it keeps D27(LR2) as a hypothesis and still
  has no unconditional dynamical instance.
- **(NR) is genuine, not circular.**  It is a statement about the escaped
  content of the *state* under the dynamics (`sup_t` of a second moment at one
  fixed window); D27(LR3) is a statement about the *tail of the two-time
  outcome law*, uniform over the exhaustion.  (NR) ⟹ LR3 (with the F2
  repair); LR3 does not give back (NR), since LR3 constrains only the
  double-Cesàro-averaged laws and says nothing about `sup_t`.  It is however
  **two clauses, not one**, and the second is the one that carries the F2 gap.
- **The class-statement counterexample does not stand** — no model is
  exhibited and the stated mechanism is excluded by the shard's own (LRD.5) on
  the (FN) register.  It must not enter the corpus as a refutation.  What
  should enter is the scoping fact: this proof uses no gap and no
  Lieb--Robinson velocity, so it supports no "gap + LR" class theorem either
  way, and `ace-ld.md`'s ACE-LD-obst′ already shows a no-mean-transport clause
  is necessary.
- **MP-1: HOLD.**  See M1.  Re-propose as the subsequence form.
- **MP-2: HOLD** (its antecedent is unavailable — F1; and the leaf count needs
  the m5 correction).
- **MP-3: HOLD** all three rows.  `LR1-GEN` can be **MERGED as PROVED** once
  its statement is detached from MP-1's D27 wording; `LR-D16-EDW` can be
  **MERGED as PROVED** with the infinite-volume caveat of m2 added to
  `where-tested`; `LR-D16` must not be merged in its present wording (it
  carries both F1's and F2's errors).
- **MP-4: MERGE**, unchanged.  It is the one merge proposal that is exactly
  right, and after this verdict it is *more* right than the shard knew.

---

FAIL(F1,F2,M1,M2,M3,M4)
