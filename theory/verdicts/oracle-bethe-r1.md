<!-- ROLE: L6 critic verdict, round 1, on theory/oracle-bethe.md.
     Critic: Opus. Date: 2026-08-25. Artifact hash: theory/oracle-bethe.md @ 451 lines. -->

# Critic verdict r1 — `theory/oracle-bethe.md` (Bethe oracle O1–O10)

Critic: Opus (adversarial pass, L6). Date 2026-08-25.
Method: every boxed equation re-derived independently (sympy, exact rational
algebra in `z_j = e^{ik_j}` and in `λ_j`), every numerical claim re-run,
the checker mutation-tested, O5 independently tested against my own ED
(N = 18 and N = 24, momentum-resolved), and the "scattering length" claim
compared against local TeX ground truth (`refs/arxiv-1602.08692`,
`refs/arxiv-1312.6793`).

## 0. What survived the attack (stated first, so the objections are readable)

Every **boxed** equation in the shard is correct as written, on the domain
written. Specifically I independently confirmed:

* (1), (2), (3), (4): free/one-magnon algebra — exact residual `0` in sympy.
* (5) → (7) → (6): the contact condition reduces to
  `A₁₂(z₁z₂−2z₂+1) + A₂₁(z₁z₂−2z₁+1) = 0` (the negative of the shard's (7),
  same equation), hence `S₁₂ = A₁₂/A₂₁ = −(z₁z₂−2z₁+1)/(z₁z₂−2z₂+1)`. Exact.
* (8): with `z = (λ+i/2)/(λ−i/2)`, sympy `cancel` gives
  `z₁z₂−2z₁+1 = 4i(λ₁−λ₂+i)/[(2λ₁−i)(2λ₂−i)]` and
  `z₁z₂−2z₂+1 = −4i(λ₁−λ₂−i)/[(2λ₁−i)(2λ₂−i)]` — **the two intermediate
  expressions in ⟨1⟩2.⟨2⟩7.⟨3⟩2 are exactly right**, and
  `S₁₂ = (λ₁−λ₂+i)/(λ₁−λ₂−i)`, difference `0`. The load-bearing
  S₁₂-vs-S₂₁ orientation is *also* pinned numerically: mutating the repo
  checker to `S → 1/S` makes `check_ed` go red at `residual` (see §3), so the
  orientation is not a matter of taste here. It further agrees with the
  textbook XXX Bethe equation `((u+i/2)/(u−i/2))^N = Π_l (u−u_l+i)/(u−u_l−i)`
  under `u = λ = ½cot(k/2)`, since the periodicity condition on the D7 wave is
  `e^{iNk₁} = S₁₂` (I re-derived this from `ψ(0,y) = ψ(y,N)`).
* (14): `∂_{k_s} log S₁₂|₀ = 2i` and `∂²_{k_s} log S₁₂|₀ = −2(1+a)/(a−1)
  = 2i cot(k_h/2)`. Exact.
* (12), (13): δ-coefficients `k_s¹ → 2`, `k_s² → cot(k_h/2)` exactly; I also
  computed the next two, `k_s³ → cos k_h/(1−cos k_h)` (verified against a
  5-point numerical third derivative to 8 digits) and the quartic.
* (15): all four forms verified (`v_h/ω_h`, `(2J−ω_h)/v_h`, `√((2J−ω_h)/ω_h)`,
  `v_h² = ω_h(2J−ω_h)`), on `0 < k_h < π`.
* (16), (17): verified numerically for `σ = ±1`, `k_h = 1.10`; residual
  `≈ 1.6 ω_s^{3/2}`, i.e. the stated `O(ω_s^{3/2})` is sharp, not conservative.
* (9), (10): recursion re-derived; `sp.solve` returns the **single** root
  `t = cos(K/2)` and `E = J sin²(K/2)`. Gap identity
  `2J[1−cos(K/2)] − J sin²(K/2) − J[1−cos(K/2)]² = 0`. Exact.
  String pole: at `k₁ = K/2 − iη`, `k₂ = K/2 + iη`, `e^{−η} = cos(K/2)` the
  denominator of (6) vanishes to `1e−41` and `λ₁−λ₂ = +i` exactly, so the
  "normalizable sign" statement is correct.
* **O5 is true but untested in the repo**; I tested it myself. Independent ED
  on `N = 18, 24` with a translation-operator momentum projection reproduces
  `E_b(K) = J sin²(K/2)` to `2e−16` at `K = π`, `1.5e−13` at `K = 2.62`,
  degrading to `2e−2` at the smallest `K` on the ring — exactly the
  delocalization at `K → 0` that ⟨1⟩2.⟨2⟩8.⟨3⟩5 predicts.
* The recorded transcript in ⟨1⟩4.⟨2⟩3 reproduces **digit for digit** on a
  fresh run, and ⟨3⟩1's arithmetic about it (max residual `2.585e−15`, max
  `c2` error `2.17e−10`, tolerances `2e−11` / `3e−9`) is correct.

There is therefore **no FATAL objection**. The objections below are about
statements that are *not* boxed equations: the invariance/interpretation
claims, the quantifiers, one unjustified ansatz, and the coverage and
failure-mode of the checker.

---

## 1. MAJOR — "leading scattering length 2" is a misnomer, and the shard's own ⟨2⟩6.⟨3⟩2 refutes it

**Step:** ⟨1⟩3.⟨2⟩4.⟨3⟩3 ("The natural invariant statement is: leading
scattering length `2`, followed by curvature `v_h/ω_h`"), propagated into O9.

The number `2` is the slope of the phase in the soft momentum **at fixed
nonzero hard momentum**. A scattering length is by definition the *zero*-momentum
object, and in this model that object is **zero**, not `2` — which the shard
itself computes two subsections later and does not connect.

Independent computation. From (8), `S₁₂` depends only on `Δλ = λ₁ − λ₂`, and
for real `Δλ` the continuous branch is the exact closed form

    δ(k₁,k₂) = 2 arctan( 1 / (λ(k₁) − λ(k₂)) ),   λ(k) = ½cot(k/2).

(I verified this against `arg S₁₂` at four kinematic points to 30 digits,
including `k₁ = −1.1, k₂ = 1.47` where `|δ| > 1`.) Put `k₁ = εx`, `k₂ = εy`.
Then `δ/ε → 2xy/(y−x)`, confirmed numerically:

    (x,y)=(1,2): δ/ε = 3.99999994 → 4      = 2xy/(y−x)
    (x,y)=(1,5): δ/ε = 2.49999998 → 2.5
    (x,y)=(-1,2): δ/ε = −1.33333333 → −4/3

So `δ` is homogeneous of degree **one** in `(k₁,k₂)` — it vanishes in the joint
soft limit — but it is **not** proportional to `(k₁−k₂)`; the limit depends on
the ratio `x/y`. Consequences:

1. In the convention used for lattice spin chains in this repo's own ground
   truth — `refs/arxiv-1312.6793/scatteringpaper.tex` line 102: *"for small
   momenta the phase shift behaves as `φ(κ₁,κ₂) ≈ −a(κ₁−κ₂)`, hence the
   definition of `a`"* — the isotropic FM **has no scattering length at all**,
   because no constant `a` reproduces `2xy/(y−x)`.
2. In the EFT convention, `refs/arxiv-1602.08692/spinwave.arXiv.final.tex`
   line 656: *"In the case of the ferromagnet system without external fields,
   the scattering length vanishes, though it may not be well-defined in the
   process, because of the appearance of scattering processes with massless
   particles."* That is the same physics: `δ → 0` in the joint soft limit,
   Goldstone/derivative coupling. It is the opposite of "scattering length 2".

I did **not** try to force a numerical comparison: 1602.08692 is a 3D continuum
EFT with a different (sign-flipped, see its line 1234) definition, and
1312.6793's `a₂ ≈ −2.30` is the **spin-1 antiferromagnet**, a different model —
its numerical proximity to `2` is a coincidence and must not be cited as
agreement.

**Repair (cheap).** Say what `2` actually is: `∂δ/∂k_s|₀ = 2` is the
**Wigner spatial displacement of the soft magnon, two lattice sites**,
hard-independent. Then state separately that the genuine zero-momentum
scattering length vanishes, and cite the two local TeX lines above as the
consistency check with Dyson/Goldstone. This *strengthens* the shard — a soft
theorem wants an Adler-type zero (CLAIMS.md row `S`: "Adler zero S → 0"), and
the joint-soft-limit vanishing is exactly that, whereas "scattering length 2"
reads as its negation.

## 2. MAJOR — the "hard-data-independent constant 2" is not invariant: it carries `sgn(v_h − v_s)`, and `cot(k_h/2) = v_h/ω_h` is not the invariant form off `k_h ∈ (0,π)`

**Steps:** ⟨1⟩3.⟨2⟩4 (whole step), boxed (15), O9.

The boxed equations are *true on `0 < k_h < π`*. The objection is to the
word **invariant** in ⟨3⟩3, which is what O9 advertises to Conjecture S.

D7 fixes `S₁₂ = A₁₂/A₂₁` as out/in only when `v(k₂) > v(k₁)`. With `k₁ = k_s`,
`k₂ = k_h ∈ (0,π)` that holds for small `|k_s|` of **either** sign (I checked
the attack the task asked for: for `k_s < 0`, `v_s < 0 < v_h`, so `A₁₂` = soft
on the left moving left, hard on the right moving right = separating =
outgoing; `A₂₁` = approaching = incoming. The in/out identification in
⟨1⟩2.⟨2⟩5.⟨3⟩3 is therefore **correct for both signs of `k_s`**, and the
direction-independence in (11)/(12) is physical, not a convention artifact.
That part of the attack fails; the shard survives it.)

But take `k_h < 0` instead. Then `v_h < 0 < v_s`, D7's proviso fails, the roles
swap, and the physical out/in ratio is `S₂₁ = S₁₂^{-1}`. Numerically at
`k_s = 10⁻³`, `|k_h| = 1.10`:

    δ(k_s, +k_h) = +0.002001631871      (physical, since v_h > v_s)
    δ(k_s, −k_h) = +0.001998369789      (NOT physical: out/in is S₂₁ here)
    physical phase at −k_h = −0.001998369789

So the physical soft phase is

    δ_phys = 2·sgn(v_h − v_s)·k_s + (|v_h|/ω_h)·k_s² + O(k_s³).

Two things follow that the shard does not say:

* the **linear coefficient is `2 sgn(k_h)`**, and `sgn(k_h)` is hard data. The
  headline "hard-data-independent constant 2" holds only after D8 has already
  restricted the hard magnon to half the Brillouin zone;
* the invariant quadratic coefficient is `|v_h|/ω_h`, **not** `v_h/ω_h`; (15)'s
  chain `cot(k_h/2) = v_h/ω_h = (2J−ω_h)/v_h = √((2J−ω_h)/ω_h)` is a chain of
  four expressions of which only the last is even in `k_h`, and the shard picks
  `v_h/ω_h` — the odd one — as "the natural invariant".

This is not pedantry for this campaign: CLAIMS.md row `S` asserts the soft
factor is *universal*, and a soft factor whose leading coefficient flips sign
with the relative-velocity sign of the spectator is a fact Conjecture S must
reproduce, not one it may inherit silently from D8's half-zone.

**Repair.** State O9 as
`δ_phys = 2 sgn(v_h − v_s) k_s + (|v_h|/ω_h) k_s² + O(k_s³)`, note that on D8's
domain this reduces to (12) with `cot(k_h/2) = v_h/ω_h`, and add the parity
check `δ_phys(−k_s,−k_h) = δ_phys(k_s,k_h)` (I verified it holds).

## 3. MAJOR — the `O(k_s³)` in (12)/(13) has no quantifier; O7/O8 are not usable as an oracle without one

**Steps:** ⟨1⟩3.⟨2⟩3.⟨3⟩2 ("Taylor's theorem … gives (12)"), O7, O8, and the
domain column "fixed hard momentum".

L6b demands explicit quantifiers. "Fixed hard momentum" makes (12) a *pointwise*
statement in `k_h`, with an implicit constant that is never named — yet
⟨2⟩6.⟨3⟩1 simultaneously asserts the constant blows up as `k_h → 0` and
concludes "truncation requires `|k_s| ≪ k_h`", which is a *uniformity*
statement. The shard therefore uses a uniformity fact it never states or proves.
Downstream, Conjecture S will be compared against O7 on some `k_h` range and
there is no remainder bound to compare against.

Independent computation supplying the missing statement. The nearest
singularity of `S₁₂` in `k_s` at fixed real `k_h` is at `λ(k_s) = λ(k_h) ± i`;
solving `k_s = 2 arccot(2(λ_h ± i))`:

    k_h = 0.05 → k_s = 0.049875 ∓ 0.002493i,  |k_s| = 0.049938
    k_h = 0.37 → 0.326568 ∓ 0.119780i,        |k_s| = 0.347842
    k_h = 1.10 → 0.522818 ∓ 0.579323i,        |k_s| = 0.780355
    k_h = 2.40 → 0.241921 ∓ 1.036559i,        |k_s| = 1.064420
    k_h = π    → ∓ i log 3                     (= 1.098612; ⟨2⟩6.⟨3⟩4 correct)

So the radius of convergence is `ρ(k_h) ≍ k_h` as `k_h → 0` and `ρ → log 3` as
`k_h → π`. Combined with the cubic coefficient `cos k_h/(1−cos k_h) ~ 2/k_h²`
(computed above), the honest statement is:

> For every `0 < a < π` there is `C(a) = O(a^{-2})` such that for all
> `k_h ∈ [a, π]` and all `|k_s| ≤ a/2`,
> `|δ(k_s,k_h) − 2k_s − cot(k_h/2)k_s²| ≤ C(a)|k_s|³`.

The closed form `δ = 2 arctan(1/(λ_s − λ_h))` (objection 1) makes this a
two-line proof: `λ_s = 1/k_s − k_s/12 + O(k_s³)`, so
`1/(λ_s − λ_h) = k_s + λ_h k_s² + (λ_h² + 1/12)k_s³ + …` and
`δ = 2u − (2/3)u³ + …` gives `2k_s + 2λ_h k_s² + (2λ_h² − ½)k_s³`, whose cubic
coefficient I checked equals `cos k_h/(1−cos k_h)` symbolically.

The same objection applies verbatim to the `O(ω_s^{3/2})` in (16)/(17) and to
O10.

## 4. MAJOR — ⟨1⟩2.⟨2⟩8.⟨3⟩2 proves the bound state from an unjustified ansatz; existence/uniqueness is not established

**Step:** ⟨1⟩2.⟨2⟩8.⟨3⟩2, justification "algebra in (10)".

⟨2⟩8's PROVE reads "The bound-state information … **is** (9)", i.e. a claim
about *the* bound state. The proof substitutes `f_r = t^{r−1}` and solves. But
`f_r = t^{r−1}` is a leaf with no justification — it is neither a definition,
nor a prior claim, nor a named computation. L6b: "every leaf justified".

What is missing (and is cheap): the bulk recursion in (10) is a two-term linear
recursion with characteristic polynomial `J cos(K/2) t² − (2J−E) t + J cos(K/2)`,
whose roots are `t` and `1/t`; `ℓ²` normalizability on `r ≥ 1` kills the `1/t`
branch whenever `|t| ≠ 1`; the `r = 1` boundary equation then fixes `t = cos(K/2)`
uniquely. Only after that is "the" bound state well defined. I confirmed
`sp.solve` returns the single root `t = cos(K/2)`, so the conclusion is right —
but the shard does not contain the argument.

Two smaller defects in the same step-cluster, which I fold in here:

* ⟨2⟩8.⟨3⟩3 says "For `0 < |K| < π`, `|t| < 1`", while **O5's domain column says
  `0 < |K| ≤ π`**. Both are true (`|cos(K/2)| < 1` on `0 < |K| ≤ π`), but the
  shard's own proof step is strictly narrower than the fact it certifies. Also,
  nothing states that `K` is taken mod `2π`; without that, `K ∈ (π, 2π)` gives
  `t = cos(K/2) < 0` — still normalizable, staggered — and O5's domain silently
  excludes a family it never mentions.
* ⟨2⟩8.⟨3⟩4's "the real scattering continuum begins at `2J[1−cos(K/2)]`" uses
  `min_p cos p = 1`, which is the minimizer only when `cos(K/2) > 0`. True on
  the stated domain, unstated as a hypothesis.

## 5. MAJOR — ⟨1⟩4.⟨2⟩4 "The numerical cross-check is complete" is an overclaim; O5, O6, O10 and (16)–(17) are tested by nothing

**Steps:** ⟨1⟩4.⟨2⟩2, ⟨1⟩4.⟨2⟩4 QED.

Coverage of `theory/checks/oracle_bethe_check.py` against the ten oracle facts:

| fact | tested? | by what |
|---|---|---|
| O1 `ω, v` | partially | only via `energy` inside `check_ed`; `v(k)` never used |
| O2 `E = ω+ω` | yes | `check_ed` residual/spectral |
| O3 `S₁₂` (6) | yes | `check_ed` (independent ED matrix) |
| O4 rapidity (8) | yes | `check_rapidities` |
| **O5 bound state** | **no** | — |
| **O6 `S₁₂ → 1`** | **no** | the fit never asserts `coefficients[0] ≈ 0` |
| O7/O8 (12)–(13) | yes, w.r.t. (6) | `check_soft_derivatives` |
| O9 `cot = v_h/ω_h` | no | `exact_second` is written as `1/tan(k_h/2)`; the identity `= v_h/ω_h` is never evaluated |
| **O10 Puiseux (16)–(17)** | **no** | — |

An `N = 18` ring already resolves the bound state; there is no reason for O5 to
be untested. I tested it (see §0) and it holds — so this is a coverage gap, not
an error. But "complete" is false as written, and under L1/L9 a table of ten
oracle facts presented after a `PASS` line implies more validation than exists.

**Repair.** Three added asserts (bound-state level from the momentum-resolved
ED vs `J sin²(K/2)`; `|coefficients[0]| < tol`; the `σ = ±1` Puiseux residual
scaling as `ω_s^{3/2}`), plus rewording ⟨2⟩4 to "the checks recorded here pass"
and adding a coverage line naming what is *not* checked.

## 6. MINOR — three intra-proof cross-references resolve to the wrong step

**Steps:** ⟨1⟩2.⟨2⟩2.⟨3⟩1, ⟨1⟩2.⟨2⟩3.⟨3⟩2, ⟨1⟩2.⟨2⟩4.⟨3⟩1.

* ⟨1⟩2.⟨2⟩2.⟨3⟩1 justifies by "the named bond-swap computation **⟨2⟩3.⟨3⟩2**".
  Inside ⟨1⟩2 that resolves to ⟨1⟩2.⟨2⟩3.⟨3⟩2 = "Collecting the shifts gives
  (4)". The intended target is ⟨1⟩**1**.⟨2⟩3.⟨3⟩2.
* ⟨1⟩2.⟨2⟩4.⟨3⟩1 makes the identical mistake.
* ⟨1⟩2.⟨2⟩3.⟨3⟩2 justifies by "⟨3⟩1 and **⟨2⟩4**"; inside ⟨1⟩2, ⟨2⟩4 is the
  *contact* equation (5), which is proved *later* and is not what is used. The
  intended target is ⟨1⟩1.⟨2⟩4 (the dispersion).

Under L6b these are exactly the defects the hierarchical style exists to
prevent. Fix: always write fully-qualified `⟨1⟩i.⟨2⟩j.⟨3⟩k` when crossing a
⟨1⟩-boundary.

## 7. MINOR — symbols used but absent from `notation.md`, which calls this "a defect"

`notation.md` ends: *"a symbol used anywhere without an entry here is a
defect."* The shard uses, prominently and inside boxed equations,
`ω_h`, `v_h` (in (15), (16), (17), O9, O10), `Δλ` (O4 row), and `a = e^{ik_h}`
(in (14)). D8 defines `ω_s` and `σ` but neither `ω_h` nor `v_h`. Add the two
hard-magnon symbols to D8 and to the table, or write `ω(k_h)`, `v(k_h)`.

## 8. MINOR — the checker is red-capable in the default mode but prints `PASS` unconditionally under `python -O`

I mutation-tested a copy in `/tmp/.../scratchpad/` (the repo copy was not
touched). All four mutations go red, which is the good news:

| mutation | result |
|---|---|
| outer sign of (6) flipped | red at `check_rapidities` |
| `S₁₂ → S₂₁` (num/den swapped) | red at `check_rapidities`; with that check bypassed, red at `check_ed` `residual` |
| `hamiltonian[row,column] -= J/2` → `+=` | red at `check_ed` `residual` |
| `2.0 → 2.0000001` in the numerator | red at `check_rapidities` |
| `exact_second` → `2/k_h` | red at `check_soft_derivatives` |
| asserted `first` → `2.0000001` | red at `check_soft_derivatives` |

The bad news: every check is an `assert`, so

    python3 -O theory/checks/oracle_bethe_check.py

prints `PASS: periodic Bethe vectors, ED spectrum, and soft coefficients` — and
so does `python3 -O` on the *sign-flipped* copy, whose printed
`c2 = 0.388779571458` disagrees with `exact_c2 = 0.388779569368` in plain sight.
A supported invocation in which the artifact's evidence line is emitted
unconditionally is a law-L1 hazard. Fix: replace `assert` with explicit
`if …: raise AssertionError(...)`, or gate the `PASS` print on a collected
failure count.

## 9. MINOR — ⟨1⟩2.⟨2⟩7.⟨3⟩4's "convention mismatch" warning has a dangling referent and a vacuous qualifier

Two problems in one leaf:

* "the **quoted** rapidity fraction" — nothing is quoted. The shard's own
  preamble says "No literature result is quoted". Under L3 a warning about a
  convention in the literature must name the local TeX source it warns about.
  As it stands the reader cannot check the warning.
* "are not the same coefficient ratio **for positive D7 rapidity**" — the
  qualifier is vacuous. `S₂₁ = S₁₂^{-1}` is an algebraic identity valid for all
  `λ`, positive or not; positivity of `λ` plays no role.

I also note, as ammunition for the repair rather than as an objection: the
*textbook* XXX form `((u+i/2)/(u−i/2))^N = Π (u−u_l+i)/(u−u_l−i)` with
`u = ½cot(k/2)` **agrees** with (8)'s first fraction. So the warning is aimed at
sources using `λ = −½cot(k/2)` or the reversed channel, and would be much
stronger if it said so.

## 10. MINOR — ⟨1⟩3.⟨2⟩6.⟨3⟩3's "precisely when" is not what happens

"Complex singularities obey `λ(k_s) − λ(k_h) = ±i`" — correct (I verified the
string has `λ₁ − λ₂ = +i` exactly and that this is the denominator zero).
"They approach zero **precisely when** the bound state delocalizes at total
momentum `K → 0`" — at fixed *real* `k_h` the singularity in `k_s` sits at a
*complex* `k_s`, so `K = k_s + k_h` is complex there and it is not the physical
bound state: e.g. `k_h = 0.05` gives `k_s = 0.049875 − 0.002493i`,
`K = 0.099875 − 0.002493i`. The correct and more useful statement is the
quantitative one in objection 3: `|k_s^sing| ≍ k_h`, which is what actually
licenses "`|k_s| ≪ k_h`".

## 11. MINOR — the `k_s = k_h` point is stated without saying the Bethe state is null there

**Step:** ⟨1⟩3.⟨2⟩6.⟨3⟩2. `S₁₂(k,k) = −1` is correct (I confirmed, exactly
`−1 + 0i`). But `S₁₂ = −1` means `A₁₂ = −A₂₁`, and at `k₁ = k₂` the D7 wave
collapses to `(A₁₂ + A₂₁)z^{x+y} ≡ 0`: there is no state. Presenting `S₁₂ = −1`
in a list of "endpoint qualifications" invites the reader to treat it as a
scattering fact at a physical kinematic point. O3's domain condition
("denominator nonzero") does not exclude it — the denominator is `(z−1)² ≠ 0`
there. Add "the Bethe state vanishes identically at coinciding momenta" to
⟨3⟩2 and to O3's domain column.

## 12. MINOR — the `k_h → π` kinematic caveat proved in ⟨2⟩6.⟨3⟩5 is not carried into the O-table

O7/O8/O9 record only "non-uniform as `k_h → 0`". But ⟨2⟩6.⟨3⟩5 establishes a
second restriction: for `k_s > 0` the D7 in/out identification needs
`sin k_s < sin k_h`, i.e. `k_s < π − k_h`, which is a *stronger* constraint than
`|k_s| ≪ 1` as `k_h → π`. Since the O-table is the campaign-facing deliverable,
that caveat belongs in the domain column of O7 (or O7's column must say
"subject to the D7 kinematic proviso, see ⟨1⟩3.⟨2⟩6.⟨3⟩5"), not only in the
proof body.

## 13. MINOR — "Dyson/Adler zero" is undefined terminology inside a justified leaf

⟨1⟩3.⟨2⟩2.⟨3⟩3 concludes "the connected interaction `S₁₂−1` … has the
Dyson/Adler zero", justified by "(11) and subtraction of the free S-matrix
identity". Neither "Dyson zero" nor "Adler zero" is in `notation.md`,
`definitions.md`, or defined here; the justification does not support the named
concept (it supports only `S₁₂ − 1 → 0`). Either define the term once (it is
what CLAIMS.md row `S` calls "Adler zero S → 0") or state the mathematical
content and drop the names.

## 14. NOTE — the exact closed form is missing and would shorten the shard

`δ = 2 arctan(1/(λ(k₁) − λ(k₂)))`, equivalently `S₁₂ = (Δλ+i)/(Δλ−i)` with
`Δλ` the only argument, is (a) exact, (b) manifestly a difference form in
rapidity — this is the Galilean-invariance property that
`refs/arxiv-1312.6793/scatteringpaper.tex` (footnote at line 746) flags as
generally *approximate* and which is *exact* here, a genuinely quotable
structural fact for the campaign — and (c) makes (11), (12), (13), the
uniformity of objection 3, the `k_s = k_h` value `δ = π`, and the `k_h → 0`
non-uniformity one-liners. Recommend promoting it to an oracle fact (O3′) and
rewriting ⟨1⟩3 around it.

## 15. NOTE — `check_soft_derivatives` is not independent of (6), and `check_ed` does not test the in/out reading

`check_soft_derivatives` re-evaluates `scattering()` and fits it, so it validates
the Taylor *algebra* of ⟨1⟩3 against (6) — which is a real check (it goes red
when the claimed coefficients are perturbed; see §8) — but it is not an
independent determination of the phase shift. Since `check_ed` independently
pins (6) against an ED matrix built only from D6, the chain is sound and this is
not circular. Still, a genuinely independent soft check exists and is cheap:
extract `δ` from the finite-size level shift on the ring
(`e^{iNk₁} = S₁₂` ⇒ `δ = Nk₁ − 2πn₁` at an ED-matched level) and compare with
`2k_s + cot(k_h/2)k_s²`. Separately, no numerical check can test D7's
out/in reading (objection 2) — that is a kinematic convention and must be
argued, not measured. Say so in ⟨1⟩4.

## 16. NOTE — `check_soft_derivatives` fits degree 6 on `|k_s| ≤ 1.6e−3`

`np.polynomial.polynomial.polyfit(momenta, phases, 6)` with `|x| ~ 10⁻³` has a
Vandermonde whose last column is `~10⁻¹⁸`; the fit is severely ill-conditioned
and only survives because the data are exact to machine precision. It works
today (errors `~1e−10` vs a `3e−9` tolerance) but it is brittle to any change of
window or degree, and the `2.17e−10` error at `k_h = 0.37` recorded in ⟨1⟩4 is
conditioning noise, not physics. Prefer central finite differences of `log S₁₂`
at two step sizes with Richardson extrapolation, or rescale `momenta` before
fitting.

## 17. NOTE — ⟨1⟩4 is a ⟨1⟩-level step of a proof whose content is a script transcript

The theorem's PROVE is "O1–O10 in ⟨1⟩5", and ⟨1⟩5.⟨2⟩1 correctly justifies only
by ⟨1⟩1–⟨1⟩3. ⟨1⟩4 therefore carries no deductive weight, yet sits inside the
Lamport hierarchy with ASSUME/PROVE/QED and a "⟨3⟩1 … Justification: the
recorded numbers" leaf. Move it to a `## Numerical record` section outside the
theorem (or make it an appendix of the shard), so that nothing in the proof tree
is justified by a printed line.

## 18. MINOR — ⟨1⟩2.⟨2⟩6.⟨3⟩2 needs "numerator nonzero"

`|S₁₂| = 1` follows from ⟨3⟩1 only where the numerator does not vanish. For real
momenta `z₁z₂ − 2z₁ + 1 = 0` forces `z₁z₂ = 1` and then `z₁ = 1`, i.e.
`k₁ = k₂ = 0` — the one excluded point, where (6) is `0/0`. It costs one clause
to say so, and it is the same exceptional point that makes O6's
`k_h ∈ (0,π)` restriction necessary.

---

## Summary verdict

**FAIL** — MAJOR: 1 (scattering-length misnomer, contradicted by the shard's own
joint-soft limit and by `refs/arxiv-1602.08692` l.656 / `refs/arxiv-1312.6793`
l.102), 2 (the linear coefficient carries `sgn(v_h − v_s)`; `v_h/ω_h` is not the
invariant quadratic form — `|v_h|/ω_h` is), 3 (no quantifier or remainder bound
for `O(k_s³)` / `O(ω_s^{3/2})`, while ⟨2⟩6.⟨3⟩1 already uses uniformity),
4 (the bound-state ansatz `f_r = t^{r−1}` is an unjustified leaf; no
existence/uniqueness, and ⟨2⟩8.⟨3⟩3's `0<|K|<π` contradicts O5's `0<|K|≤π`),
5 (⟨1⟩4.⟨2⟩4 "complete" overclaims: O5, O6, O9's identity and O10 are tested by
nothing). MINOR: 6, 7, 8, 9, 10, 11, 12, 13, 18. NOTE: 14, 15, 16, 17.
No FATAL: every boxed equation — (1)–(17) — was re-derived independently and is
correct on its stated domain, the S₁₂-vs-S₂₁ orientation in ⟨1⟩2.⟨2⟩7 is right
and is pinned both by textbook XXX Bethe equations and by mutation-testing
`check_ed`, the in/out reading survives the `k_s < 0` attack, O5 holds against my
own momentum-resolved ED at `N = 18, 24`, and the recorded transcript reproduces
digit for digit.
