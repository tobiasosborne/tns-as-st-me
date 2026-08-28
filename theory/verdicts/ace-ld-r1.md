<!-- ROLE: adversarial critic verdict, round 1, on theory/ace-ld.md and
     theory/checks/ace_ld_check.py.  Protocol: briefs/critic-protocol.md.
     Brief: briefs/ace-ld-critic-r1.md (incl. ADDENDUM).
     Lane: this file only.  Nothing here edits the shard, definitions.md,
     notation.md or claims/CLAIMS.md; no merge is authorised by this file. -->

# ACE-LD r1 — critic verdict

**Verdict: FAIL(F1, M1, M2, M3, M4, M5, M6).**

Every objection below carries (a) an exact step address, (b) my own
independent computation or counterexample, (c) a one-line FIX DEMAND, and
(d) the surviving weaker statement.  Scripts I wrote for this pass live in
the session scratchpad and are named inline; every number quoted was produced
by running them, not read off the shard.

**Headline.**  The mathematics of this shard is, step for step, better than
its packaging.  I re-derived ACE-LD-abs and ACE-LD-nec and they are correct;
I re-derived the charge values and they are correct; I built the scattering
configuration the shard's own checker never builds and ACE-LD-obst's TPM law
reproduced to four digits, including the `⟨3⟩1` step the lane declined to
write out.  What fails is the *reach*: the hypothesis conjunction
`(E-TAIL) ∧ (V-ch)` is **empty on every model this corpus has instantiated**,
because `(E-TAIL)` is equivalent to `χ=1` `S^z`-product vacua — which pins us
to D16 — and D16's kink band is *exactly flat*, so `v_K ≡ 0` and `(V-ch)`
fails there.  The merge proposals would import that emptiness into the DAG as
a status upgrade and would put a false universal statement about D28 into
`claims/CLAIMS.md`.

---

## 0. What the orchestrator asked me to recompute first

**Is `ν = ±2s|W|` an artifact of the regularised window charge's `c₀`
offset — the offset M-INDEX-fin ⟨1⟩5.⟨2⟩3 proves cancels in the TPM
increment?  No.  The obstruction is not a `c₀` artifact.**

I re-derived both charge values from the frozen D13(a) definition rather than
from the shard.  With `𝔛_W = a-1 + (1/2s)Σ_{x=a}^{b}(S^z_x+s)` and
`Q̂_{W,c₀} = 2s(𝔛_W-c₀)`:

- `Q̂_{W,c₀} = Σ_{x=a}^{b}S^z_x + s(a+b-1-2c₀)` — reproduces MI ⟨1⟩1.⟨2⟩2.
- `α` tail (`S^z ↦ +s`): `s|W| + s(a+b-1-2c₀) = 2s(b-c₀) = q_+`.
- `β` tail (`S^z ↦ -s`): `-s|W| + s(a+b-1-2c₀) = 2s(a-1-c₀) = q_-`.
- `q_+ - q_- = 2s(b-(a-1)) = 2s|W|`, **with `c₀` cancelling identically.**

So the `c₀` offset *does* cancel — that cancellation is exactly what
M-INDEX-fin ⟨1⟩5.⟨2⟩3 asserts, and what it buys is **integrality of `ν`**
(`ν ∈ ℤ`), not boundedness of `ν`.  What survives the cancellation is
`2s·(range of 𝔛_W)`, and `𝔛_W` ranges over exactly `[a-1, b]` by
construction, an interval of length `|W|`.  A wall that sweeps the window
therefore *must* register `|ν| = 2s|W|`; this is the saturation of the
clamped observable and it is the physically correct answer for a wall whose
displacement is unbounded.  The shard's arithmetic is right and the
orchestrator's suspected escape hatch is closed.

**Independent numerical confirmation of the whole obstruction.**  The shard's
own LD-C5 does *not* build ACE-LD-obst's configuration (see M3).  I built it:
one incoming right-moving packet prepared far to the LEFT of a barrier (this
is `(V-in)`, `σ̄ = −`), reflection reversing the velocity (kink returns,
`σ = −`) and transmission continuing (kink transits, `σ = +`) — i.e. exactly
`σ_L ≠ σ_T`.  Then I computed D27's TPM
`Σ_q ||E_W({q-ν})e^{-i(t_+-t_-)H}E_W({q})Ψ_{t_-}||²` verbatim
(`probe4.py`, `N=8192`, `t_± = ∓600`):

```
 |W|   LD-IN defect   nu atoms                 Sum nu p    Sum|nu|p   LR3 tail(M=10)
   17   2.407e-09     +0:0.5567  -17:0.4433      -7.536      7.536       7.980
   33   2.407e-09     +0:0.5567  -33:0.4433     -14.630     14.630      15.073
   65   2.407e-09     +0:0.5567  -65:0.4433     -28.816     28.816      29.259
  129   2.407e-09     +0:0.5567  -129:0.4433    -57.188     57.188      57.632
  257   2.407e-09     +0:0.5567  -257:0.4433   -113.933    113.933     114.377
  513   2.407e-09     +0:0.5567  -513:0.4433   -227.424    227.424     227.867
```

with independently measured `|r|² = 0.5567`, `|t|² = 0.4433`.  Every clause of
⟨1⟩6.⟨2⟩2 is reproduced: (i) `⟨3⟩1` (LD-IN) holds to `2.4e-09`; (ii) the law
is exactly `‖F_ret‖²δ_0 + ‖F_tr‖²δ_{-2s|W|}` with `2s=1`; (iii) exactly one
channel transits; (iv) `Σ_{|ν|>M}(1+|ν|)p_{W_m} = (1+|W_m|)·0.4433` — check
`(1+513)(0.4433) = 227.86` against the measured `227.867` — so D27(LR3) fails
along the exhaustion; (v) the weak limit is defective at mass `0.5567`;
(vi) `δx = -(2s)^{-1}Σννp = +|W|·0.4433` diverges linearly.

**ACE-LD-obst survives my attack.**  It is not a `c₀` artifact, not a sign
error, and not a numerical accident.  Objections M2 and M3 are about its
*hypotheses* and its *certificate*, not its conclusion.

---

## 1. FATAL

### F1 (FATAL) — `(E-TAIL) ∧ (V-ch)` is empty on every model this corpus has instantiated, and ⟨1⟩6.⟨2⟩3 asserts a false universal about D28

**(a) Location.**  `theory/ace-ld.md` §0 ACE-LD-esc ASSUME (the `(E-TAIL)`
and `(V-ch)` blocks); ⟨1⟩4.⟨2⟩1's scope parenthesis; ⟨1⟩6.⟨2⟩2 ASSUME;
**⟨1⟩6.⟨2⟩3 first sentence**; MERGE PROPOSALS MP-1 rows 2 and 3, MP-2, MP-3.

**(b) My computation.**  Three independent steps.

*(i) `(E-TAIL)` is equivalent to `χ=1` `S^z`-product vacua.*  Assume
`ω_γ((S^z_x-s_γ)²)=0` for all `x`.  Cauchy–Schwarz on the state gives
`|ω_γ((S^z_x-s_γ)A)|² ≤ ω_γ((S^z_x-s_γ)²)ω_γ(A^*A) = 0`, so
`ω_γ(S^z_xA) = s_γω_γ(A)` for **every** `A ∈ 𝔄`.  Take `A = Π_x^{(m)}`, the
on-site spectral projection of `S^z_x` at `m`: then `(m-s_γ)ω_γ(Π_x^{(m)})=0`,
so `ω_γ(Π_x^{(m)})=0` for `m≠s_γ` and `ω_γ(Π_x^{(s_γ)})=1` for every `x`.  A
state assigning `1` to each of finitely many projections assigns `1` to their
product, and `⊗_{x∈Λ}Π_x^{(s_γ)}` is **rank one** on `𝔄_Λ`.  Hence
`ω_γ = ⊗_x|s_γ⟩⟨s_γ|` exactly.  The converse is immediate.  So `(E-TAIL)`
holds **iff** the vacuum is the fully `S^z`-polarised product state — `χ=1`.
The shard's own "extremality" escape (`s=S` forces the eigenvector property)
does not widen this: extremality *implies* the product state by the same
argument.  Its stated scope, "false for a generic injective-MPS vacuum", is
therefore a serious understatement: it is false for **every** vacuum that is
not the `S^z`-product state.  This is the restriction TJO fenced on
2026-08-27.

*(ii) `(E-TAIL)` is necessary, not merely sufficient.*  `(AD3-ex)` quantifies
over every fixed window containing the kink core.  `(AD3-ex)` at `W` forces
`‖(Q̂_W-q_ch)P_chΨ_t‖ → 0` (`Q̂_W` bounded, `E_W({q})` projects onto its
`q`-eigenspace), hence zero asymptotic variance of `Q̂_W`.  For an escaped
channel ACE-tail (AS ⟨1⟩3.⟨2⟩6) transfers that to `ω_γ`, so
`Var_{ω_γ}(Σ_{x∈W}S^z_x)=0` is required at every such `W`.  Comparing `W` and
`W∪{b+1}` and using `|Cov| ≤ √(Var·Var)` gives `Var_{ω_γ}(S^z_x)=0` at each
added site, and translation invariance of the vacuum propagates it.  So
`(E-TAIL)` is *forced* — it is not an extra convenience.

*(iii) D16 — the only corpus model satisfying `(E-TAIL)` — provably violates
`(V-ch)`.*  D16 fixes `Ω_vac={↑,↓}`, "both exact injective product vacua with
`χ=1`", so `(E-TAIL)` holds there and (by (i)) essentially nowhere else in the
corpus.  D16 also asserts an "exact zero-energy product family"
`|K(z)⟩=⊗_n(|↑⟩_n+zq^n|↓⟩_n)`.  I verified this by exact diagonalisation
(`d16_flat.py`, `Δ=2.5`, `q=0.208712`, `L=9`, full `H_kink` including the
telescoping boundary field):

```
   z          <K(z)|H|K(z)>     ||H|K(z)>||
   0.2        +1.77e-18          4.23e-17
   1.0        +1.82e-17          1.22e-16
   q^-2       +5.65e-17          2.20e-16
   q^-4       +6.79e-17          2.51e-16
   5.0        +5.11e-17          2.11e-16
   2i         +3.67e-17          1.91e-16
   -3.0       +4.23e-17          2.52e-16
 lowest eigenvalue of H = 0.000000 in EVERY S^z sector (dims 1..126)
```

Every member of the family — real, complex, and at every kink centre — is an
exact zero mode, and the ground energy is `0` in every sector.  The kink band
is therefore **exactly flat**: `E_K ≡ 0`, hence `v_K ≡ 0`.  `(V-ch)` demands
the kink velocity support at distance `≥ ε_0 > 0` from `0`.  D16 fails it
identically.

*Consequence.*  `(E-TAIL) ∧ (V-ch) = ∅` on every model this corpus has
instantiated.  ACE-LD-esc, COROLLARY ACE-LD and ACE-LD-obst are all
conditional on a hypothesis set with no known instance — the same defect that
keeps `𝒮_W`'s nonemptiness at `ρ≠1/2` open under bd `tns-iu5`, and which the
critic protocol's reliance audit fences by name.

*(iv) The load-bearing sentence of ⟨1⟩6.⟨2⟩3 is false as written.*  It reads
"**On the fixed-packet class of D28 the kink is ballistic**: every channel's
kink escapes any fixed window", and MP-1's obst row ends "…not a fixed-window
theorem **on D28 packets**".  D28(4) constrains *only the relative* velocity:
"their kink and magnon velocity supports have distance `ε_v>0`, and their
signs are: incoming-left `v_M-v_K ≥ ε_v`; outgoing-left `v_M-v_K ≤ -ε_v`;
outgoing-right `v_M-v_K ≥ ε_v`".  All three are satisfied by `v_K ≡ 0` with
`|v_M| ≥ ε_v`.  D28's class therefore *contains* the static-kink class, and
D16 realises it.  The ballistic property is `(V-ch)`'s, which the lane itself
introduced — it is not D28's.  This is a false universal statement about a
frozen definition, sitting in the merge text.

**(c) FIX DEMAND.**  Replace every "on D28 packets" / "on the fixed-packet
class of D28" with "on the `(V-ch)` sub-class of D28 packets"; state in §0,
HONEST STATUS and MP-1 that `(E-TAIL) ⟺ χ=1` `S^z`-product vacua, that
`(E-TAIL) ∧ (V-ch)` has **no instance in this corpus**, and that D16 satisfies
`(E-TAIL)` but has an exactly flat kink band and so violates `(V-ch)`.

**(d) SURVIVING WEAKER STATEMENT.**  ACE-LD-esc, COROLLARY ACE-LD and
ACE-LD-obst stand **as conditional implications on their own ASSUME blocks**
— I found no error in their proofs.  What does not survive is any claim about
D28's packet class as such, and any DAG upgrade premised on the class being
inhabited.  A D28-admissible model with `χ=1` `S^z`-product vacua *and* a
dispersive kink band would instantiate them; none is exhibited here, and D16
is not one.

---

## 2. MAJOR

### M1 (MAJOR) — `(E-TAIL)`'s scope is understated and the `χ>1` refutation is declined on a false reason

**(a) Location.**  ⟨1⟩4.⟨2⟩1's parenthetical "*(Scope of (E-TAIL): …)*";
HONEST STATUS "Hypothesised / not proved", bullet `(E-TAIL)`; MP-1 row 2's
parenthesis "true in D16, false for generic MPS vacua".

**(b) My computation.**  Two parts.

*The scope sentence is wrong in kind.*  By F1(b)(i) the correct statement is
an **equivalence**, `(E-TAIL) ⟺ ω_γ = ⊗_x|s_γ⟩⟨s_γ|`, i.e. `χ=1`.  "False for
generic MPS vacua" reads as a measure-zero caveat; the truth is that it holds
on a single point of vacuum space.  Since the campaign's north star is MPS,
this is the difference between a theorem about the programme and a theorem
about one product-state model.

*The declined refutation is available from machinery the shard already
cites.*  HONEST STATUS says a `χ>1` refutation "would need a quantitative
variance lower bound on the dressed state, which ⟨1⟩4's upper-bound machinery
does not give".  But ACE-tail (AS ⟨1⟩3.⟨2⟩6) is an **asymptotic equality**,
not an upper bound:
`⟨κ(x),Aκ(x)⟩ = ω_α(A)‖κ(x)‖² + O(C_N‖A‖⟨r⟩^{-N})` — it delivers the lower
bound for free.  With `A=(Q̂_W-q)²` and
`ω_α(A) = Var_{ω_α}(Q̂_W) + (ω_α(Q̂_W)-q)² ≥ Var_{ω_α}(Q̂_W)`,
`‖(Q̂_W-q)κ(x)‖² ≥ Var_{ω_α}(Q̂_W)‖κ(x)‖² - C_NM_W²⟨r⟩^{-N}` for **every**
`q`.  `‖κ_a(x)‖ = ‖χ_K‖_{L²} > 0` is fixed (AS ⟨1⟩5.⟨2⟩1), and the dressed
norm `‖a(y)κ(x)‖² = ‖κ(x)‖²G_γ(y,y) + O(⟨r⟩^{-N})` is bounded below by
ACE-Gram (AS ⟨1⟩6.⟨2⟩1).  For an injective-MPS vacuum
`Var_{ω_γ}(Σ_{x∈W}S^z_x)` is extensive, hence `>0` at every `W`.  The
refutation is two steps from what ⟨1⟩4 already runs.

*The counterexample offered is out of class.*  ⟨1⟩4.⟨2⟩1 cites AKLT,
`ω((S^z_x)²)=2/3`.  I confirmed that number from the AKLT MPS
(`A^{+1}=√(2/3)σ^+`, `A^0=-(1/√3)σ^z`, `A^{-1}=-√(2/3)σ^-`, fixed point
`I/2`: `p(m)=1/3` each, `⟨(S^z)²⟩=2/3`).  But AKLT has tail density `s=0`,
and H-MQG(2) requires `s>0` — so it is outside the kink setting and
establishes nothing there.  An in-class witness is any vacuum with
non-saturated tail density `s ∈ (0,S)` not attained as an on-site `S^z`
eigenvalue (e.g. spin-1 with `s=1/2`), for which `(E-TAIL)` fails by
arithmetic alone.

**(c) FIX DEMAND.**  State `(E-TAIL) ⟺ χ=1` `S^z`-product vacua as an
equivalence with the two-line proof, prove the `χ>1` refutation of (A4) from
the ACE-tail *equality* plus ACE-Gram, and replace the AKLT illustration with
an in-class (`s>0`) witness.

**(d) SURVIVING WEAKER STATEMENT.**  ACE-LD-esc is unaffected as an
implication.  What changes is its advertised reach: "first-moment escape holds
under D28 + two extra hypotheses" becomes "first-moment escape holds only for
`χ=1` `S^z`-product vacua, and provably fails otherwise".

---

### M2 (MAJOR) — ACE-LD-obst is over-hypothesised; the tightness failure follows from the first moment alone and needs none of `(E-TAIL)`, `(V-ch)`, `(V-in)`, `σ_L≠σ_T`, distinct charges, or `⟨3⟩1`

**(a) Location.**  ⟨1⟩6.⟨2⟩2 ASSUME and its proof ⟨3⟩1–⟨3⟩3; MP-1 row 3.

**(b) My computation.**  D27 states its own identity: "at every fixed `m`,
`Σ_ν ν p_{W_m}(ν) = -2s[ω^+_{W_m}(𝔛_{W_m}) - ω^-_{W_m}(𝔛_{W_m})]`
(`theory/memory-index.md ⟨1⟩7.⟨2⟩2`)".  And D27(LR3) implies a **uniform
first absolute moment**: choose `M₀` with `sup_m Σ_{|ν|>M₀}(1+|ν|)p_{W_m} ≤ 1`;
then `Σ_ν|ν|p_{W_m} ≤ M₀·1 + 1` for every `m`, since `p_{W_m}` is a
probability.  Hence

> **LR3 ⟹ `sup_m |ω^+_{W_m}(𝔛_{W_m}) - ω^-_{W_m}(𝔛_{W_m})| < ∞`.**

Now the only input needed on the dynamics is the **mean**: for a channel
whose kink escapes to the `α`/`β` side, `ω^±_W(𝔛_W) → b` resp. `a-1` by
D13(a) and the tail densities of H-MQG(2) — *no variance statement, hence no
`(E-TAIL)`*.  If the total transit probability `p_tr := P(out-side ≠ in-side)`
is positive, then `|Σ_ν ν p_{W_m}| = 2s·p_tr·|W_m| + o(|W_m|) → ∞`, so LR3
fails.  Distinct charges, sign-definite channels, and the norm-concentration
of `⟨3⟩1` are all unnecessary.

Numerically, the mechanism is robust exactly as predicted.  My `probe3.py`
run *violates* `(V-in)` (LD-IN defect `5.50e-01`, incoming state spread over
two window charges) and still gives
`Σ|ν|p = 7.167, 13.913, 27.405, 54.388, 108.361` at
`|W| = 17,33,65,129,257` — clean linear growth.  The shard's **own** green
LD-C5 also violates `(V-in)` and also shows unbounded tails
(`18 → 34 → 66 → 130`).  So the shard is proving under `(V-in)` a conclusion
its own certificate shows does not need it.

Note also that on any ballistic branch (`v ≠ 0`) the position runs from
`-sign(v)∞` to `+sign(v)∞`, so **every** branch transits: `p_tr = 1` unless
the scattering genuinely reverses the kink velocity.  The `ν=0` atom exists
only for the velocity-reversing channel.  That makes the obstruction *more*
general than the shard's `σ_L ≠ σ_T` framing, not less — and it is the reason
this objection is a strengthening demand, not a refutation.

**(c) FIX DEMAND.**  Re-derive ⟨1⟩6.⟨2⟩2(b) from D27's own first-moment
identity plus D13(a)/H-MQG(2) tail densities, dropping `(E-TAIL)`, `(V-ch)`,
`(V-in)`, `σ_L≠σ_T` and `⟨3⟩1` from its ASSUME, and keep the two-atom law
`(a)` as the separate, more heavily hypothesised refinement it is.

**(d) SURVIVING WEAKER STATEMENT — actually a stronger one.**
*ACE-LD-obst′:* under H-MQG(1)–(3), D28 and D27(LR1), if the kink component
escapes every fixed window with net transit probability `p_tr > 0`, then
`|Σ_ν ν p_{W_m}(ν)| = 2s·p_tr·|W_m| + o(|W_m|)`, so D27(LR3) fails along every
padded exhaustion and the ordered outcome measure is defective.  This has a
non-empty hypothesis set (unlike ACE-LD-obst as stated — see F1) and is the
version that should carry the round's negative result.

---

### M3 (MAJOR) — the checker never instantiates ACE-LD-obst; LD-C5's model violates `(V-in)`, produces no `ν=0` atom, and is never red-tested

**(a) Location.**  `theory/checks/ace_ld_check.py` `check_c5` and the
`REGISTRY` (`LD-C5` absent from every red mode); `theory/ace-ld.md` §5's
`LD-C5` paragraph; MP-1 row 3's "tested in … LD-C5".

**(b) My computation.**  LD-C5 builds `Ψ = c_-φ_- + c_+φ_+` in a **free**
model — a superposition of a left- and a right-mover.  Its early-time state is
therefore *not* concentrated on a single window charge, so `(V-in)` and
⟨3⟩1 are violated by construction, and its law is
`{-|W|: 0.36, +|W|: 0.64}` with **no `ν=0` atom at all**.  The shape
⟨1⟩6.⟨2⟩2(a) actually asserts — `‖F_L‖²δ_0 + ‖F_T‖²δ_{±2s|W|}`, "exactly one
channel transits" — is therefore never exercised by the certificate that
MP-1 cites for it.  The green run certifies only that *some* model has an
unbounded LR3 tail.

I built the missing configuration (`probe4.py`; §0 above): incoming packet
prepared far left of a barrier, reflection reversing velocity.  It reproduces
⟨2⟩2(a) exactly (`0.5567δ_0 + 0.4433δ_{-|W|}`), confirms ⟨3⟩1 to `2.4e-09`,
and reproduces (b) to four digits.  So the shard's conclusion is right and its
certificate is the wrong model.

Mutation-testing on copies (`mut.sh`) shows LD-C5 does have *some* teeth —
swapping its expected weights fires it (`M4`: "TPM weight at nu=-17.0 is
0.360000, expected 0.640000") — but no such mutation is registered, and
`REGISTRY` lists `LD-C5` as NOT-RUN in every red mode.  The round's most
consequential claim has no red capability at all.  I also ran the physically
decisive contrast (`M3`: flat dispersion, `v ≡ 0`, i.e. the static kink of
D16): the green run aborts at `LD-C2` ("eps_+(t_final) = 9.755e+00"), so the
checker correctly detects that escape is load-bearing — but it never gets to
LD-C5, so the *other half of the dichotomy* (static kink ⟹ `p_W = δ_0`, LR3
tight) is uncertified.

**(c) FIX DEMAND.**  Rebuild LD-C5 on a scattering model with a definite-side
incoming packet so the `ν=0` atom is produced and ⟨3⟩1 is measured; register
at least one LD-C5 red mutation; add a green `LD-C6` static-kink contrast
certifying `p_W = δ_0` with a bounded LR3 tail.

**(d) SURVIVING WEAKER STATEMENT.**  LD-C5 as it stands certifies: *in a free
one-particle model with a clamp-form window charge and two counter-propagating
packets, the D27 TPM law is supported on `{±|W|}` and the LR3 first-moment
tail grows linearly in `|W|`.*  That supports ACE-LD-obst′ (M2), not
ACE-LD-obst as stated.

---

### M4 (MAJOR) — MP-2 proposes an inadmissible L5 status and a DAG upgrade on a class with no known instance

**(a) Location.**  MERGE PROPOSALS MP-2; MP-1 rows 2 and 3 ("PROVED
(conditional; pending L6 loop)").

**(b) My computation.**  `claims/CLAIMS.md`'s own header freezes the rule:
"Authoritative L5 statuses: PROVED | SKETCH | CONJECTURE | REFUTED.
Empirical, conditional, under-review, and future-work qualifiers belong in
prose, **never as additional status values**."  MP-2's proposed value —
"**PROVED (conditional, corrected reading) / REFUTED (same-side regime)**" —
is a compound non-status, and a single claim id cannot carry both.
Substantively, by F1 the class on which the PROVED half would rest is empty
on every instantiated model, and by M5 the reading proved is not the reading
D18(AD3) and M-INDEX-spec use.  Note also that the REFUTED half is *itself*
conditional on `(V-ch)` (ACE-LD-nec needs both channels to escape to one
definite side), so neither half is unconditional.

**(c) FIX DEMAND.**  Withdraw MP-2; leave the `AD3-ex` row at **CONJECTURE**
and record the regime split in the row's prose, exactly as the adjudicated
M-INDEX-fin / M-INDEX-spec / AC-EX rows record theirs.

**(d) SURVIVING WEAKER STATEMENT.**  `AD3-ex` remains CONJECTURE, now with
sharp prose: it is refuted in the same-side regime, provable only in a
ballistic-kink `χ=1` regime that no instantiated model realises, and — by the
computation in §3 below — strictly false even in D16 at any fixed `W`, where
the correct statement is an `ε`-version.

---

### M5 (MAJOR) — the reading of AD3 that is discharged contradicts D18(AD3)'s and M-INDEX-spec's reading of the same clause

**(a) Location.**  ⟨1⟩6.⟨2⟩1 ("closes the local-decay gap of
ansatz-scattering-r1 objection 4"); ⟨1⟩5 preamble; MP-3's replacement gloss
for AS ⟨1⟩7.

**(b) My computation.**  D18(AD3), frozen: "For every fixed window containing
the kink, the free leg charge and non-bound dressing leave the window as
`t→±∞`; **the remaining local state is a kink charge eigenstate**."
M-INDEX-spec's adjudicated scoping paragraph repeats this: the reduction
clause "additionally assumes H-AD-G with D18(AD3) read as weak-\*
convergence of the window restriction, per channel, to the corresponding
**kink charge eigenstate**."  The shard's ⟨1⟩4 achieves the opposite: the
kink *also* leaves `W` (that is the entire mechanism — ⟨1⟩4.⟨2⟩2 needs
`dist(x,W) ≥ ε_0t/2`), and the remaining local state is a **vacuum** charge
eigenstate at `q_±(W,c₀)`.  So even where the discharge is valid it supplies
the vacuum reading, not the kink reading, and therefore does **not** feed
M-INDEX-spec's reduction clause.  ⟨1⟩6.⟨2⟩1's "closes the local-decay gap"
and MP-3's gloss both omit this, and MP-3 is the text that would land in
`theory/ansatz-scattering.md`.

**(c) FIX DEMAND.**  State in ⟨1⟩6.⟨2⟩1 and MP-3 that what is discharged is
the *vacuum-eigenstate* reading of the ⟨1⟩7 display, that D18(AD3)'s
"remaining local state is a kink charge eigenstate" clause is **not** thereby
supplied, and that M-INDEX-spec's reduction clause is untouched.

**(d) SURVIVING WEAKER STATEMENT.**  On the `(V-ch)`+`σ_L≠σ_T` class the
literal norm display of AS ⟨1⟩7 holds with `q_ch = q_{σ_ch}(W,c₀)`, which is
enough for AS ⟨1⟩7.⟨2⟩2's Cauchy–Schwarz cross-term step and for nothing
downstream of D18(AD3)'s kink-eigenstate wording.

---

### M6 (MAJOR) — LD-C3 does not test the constant it is billed as testing, `--red-coset` is blind to the coset, and §5's own prescription would make `--red` exit 2

**(a) Location.**  `theory/ace-ld.md` §5, `LD-C3` bullet ("**This is the red-
capable surface: it tests the CONSTANT, not just convergence**") and the
`--red-coset` bullet; `ace_ld_check.py` `Model.claimed_inv_gap` and
`check_c3`.

**(b) My computation.**  I ran the shipped checker: green exit `0`, `--red`
exit `1`, all three registered patterns reproduce, and §5's quoted red-coset
numbers are exact (`t=8, lhs 4.121597e-01 > rhs 3.724759e-01`).  Then I
bisected the asserted constant on copies:

```
 claimed_inv_gap = 0.40  -> LD-C3 PASSES (green exit 0)
 claimed_inv_gap = 0.30  -> LD-C3 PASSES
 claimed_inv_gap = 0.20  -> LD-C3 PASSES
 claimed_inv_gap = 0.10  -> LD-C3 fails: t=8, lhs 4.121597e-01 > rhs 3.724759e-01
 claimed_inv_gap = 0.05  -> LD-C3 fails: t=4
```

Two things follow.  First, the green model tolerates a claimed constant **five
times smaller** than the lemma's `Σd_{ch}^{-1}=1`, so LD-C3 certifies only
"the constant is within a factor 5", not "the constant is `Σd^{-1}`".
Second, the failure line at `0.10` is **character-for-character identical** to
`--red-coset`'s — as it must be, since `Q̂ ↦ Q̂/10` with `q ↦ q/10` leaves
`E({q/10}) = E({q})` and `P_ch` untouched (lhs bit-identical) and scales
`ε → ε/10` (rhs by `1/10`).  `--red-coset` is therefore *not* a coset
mutation; it is exactly a `10×` shrink of the asserted constant, and a genuine
coset break that preserves the gap (e.g. `spec → spec + √2`) would leave LD-C3
standing — correctly, since (LD.3) needs only the gap.

Third, and worst: §5 specifies "`d_ch` **computed from the model spectrum**
(`=1` here)".  I implemented that literally on a copy
(`claimed_inv_gap = 1/min(diff(sort(spec)))`) and re-ran `--red`:

```
--- red mode 'coset' ---
  LD-C1: broken as registered
  LD-C3: SURVIVED but registered to break -- mutation not detected
RED-MISMATCH: pattern not reproduced; exit 2.
```

So the checker's red capability rests on the code doing the *opposite* of what
its own specification prescribes.

**(c) FIX DEMAND.**  Delete the "it tests the CONSTANT" claim or tighten
LD-C3 until it does (report and gate `max_t lhs/rhs`, which is the informative
statistic — the logged "worst lhs-rhs margin `-1.02e-11`" is attained where
both sides are `~1e-11` and conveys nothing); rename `--red-coset` to
`--red-gap` and add a true coset mutation; and correct §5 to say the constant
is **asserted at 1 per ⟨1⟩1.⟨2⟩3**, not computed from the spectrum.

**(d) SURVIVING WEAKER STATEMENT.**  LD-C1–LD-C4 certify, on that model, that
(LD.1) holds at every grid time with the asserted constant `1`, that a
`10×`-optimistic constant is detected, and that merging channels or
duplicating a charge destroys escape and diagonality.  That is real and
useful; it is not a test of the sharp constant.

---

## 3. MINOR

**m1 (MINOR) — LD-C1's dynamical gates are structural no-ops in the model
class.**  *(a)* `check_c1`, the `[P_ch,H]`, orthogonality and resolution
blocks.  *(b)* All channels are Fourier masks and `H` is a Fourier
multiplier, so `[P_ch,H]=0` to machine precision **by construction**; the
masks are complementary, so `P_+P_-=0` and `(P_++P_-)Ψ=Ψ` likewise.  No
registered mutation can move them.  I built one that does (real-space
half-line projections, `m2.py`): `LD-C1: [P_+, H] != 0 (5.316e-01)`.  So the
gate has latent teeth and is simply never armed.  *(c)* Register the
real-space-projection mutation as a fourth red mode.  *(d)* LD-C1's surviving
content is its spectrum/coset arithmetic, which `--red-coset` does exercise.

**m2 (MINOR) — misaddressed Lamport pointer.**  *(a)* §0, PROPOSITION
ACE-LD-esc, PROVE: "Moreover these are the **only** values for which (A4) can
hold (⟨1⟩5.⟨2⟩3)."  *(b)* ⟨1⟩5.⟨2⟩3 is the same-side refutation.  The
uniqueness argument (LD-UNIQUE) is at **⟨1⟩4.⟨2⟩6**, which I checked and
which is correct.  *(c)* Repoint to ⟨1⟩4.⟨2⟩6.  *(d)* Uniqueness holds as
proved.

**m3 (MINOR) — statement/proof lockstep in ACE-LD-nec.**  *(a)* §0 LEMMA
ACE-LD-nec ASSUME lists only `w_2 > 0`; the PROVE then smuggles `w_1` in via
"whenever `w_1w_2>0`".  ⟨1⟩3's ASSUME correctly lists both.  *(b)* ⟨1⟩3.⟨2⟩4
genuinely needs `w_1>0`.  *(c)* Move `w_1>0` into the §0 ASSUME.  *(d)* The
lemma is correct as proved in ⟨1⟩3.

**m4 (MINOR) — three spec/code divergences in §5.**  *(a)* §5 vs
`ace_ld_check.py`.  *(b)* §5 says `N = 4096`; the code has `N_RING = 8192`.
§5 says packets "centred at `k = ∓π/2 ± detune`"; there is no detune anywhere
in the code (`K0 = π/2`, `K_WIDTH = 0.6`).  §5 says `d_ch` is "computed from
the model spectrum"; the code hardcodes `claimed_inv_gap = 1.0` (see M6).
*(c)* Bring §5 into lockstep with the code, or vice versa.  *(d)* The
certificates themselves are unaffected by the first two.

**m5 (MINOR) — inflated `depends on` lists.**  *(a)* MP-1 rows 1 and 3.
*(b)* ACE-LD-abs is claimed unconditional given its ASSUME; M-INDEX-fin
enters only the "`≤n`" refinement in the instance, so it is not a dependency
of the abstract row.  ACE-LD-obst lists M-INDEX-spec, but no step of
⟨1⟩6.⟨2⟩2 uses it — ⟨2⟩4 only *discusses* it.  *(c)* Drop M-INDEX-fin from
row 1 and M-INDEX-spec from row 3.  *(d)* The DAG edges that are actually
consumed (M-INDEX-fin for the instance, D27 and MI ⟨1⟩5 for the TPM) are
correct, and I found no cycle: no step uses ACE.3 or anything downstream of
`(AD3-ex)`.

**m6 (MINOR) — L4 symbol collisions in MP-4.**  *(a)* MP-4's three proposed
`notation.md` rows.  *(b)* `notation.md` line 216 already freezes `q` as the
D16 deformation parameter `Δ-√(Δ²-1)` (flagged "overload 6") — and D16 is the
very model in play, where `q_±(W,c₀)` would sit beside `q^n` in `|K(z)⟩`.
Line 220 already freezes `σ_k`, `σ_x` as packet widths, against MP-4's
`σ_ch`.  *(c)* Rename to e.g. `Q^{vac}_±(W,c₀)` and `ς_ch` before merging.
*(d)* The quantities themselves are well defined.

**m7 (MINOR) — L2.**  *(a)* Whole file, 861 lines against the 200–500 band.
*(b)* Self-reported in HONEST STATUS.  *(c)* Split §3 (⟨1⟩6, the obstruction)
into its own shard — it is a different result with a different hypothesis set
(M2), and the split fixes the addressing rather than breaking it.  *(d)* No
mathematical content is affected.

---

## 4. NOTE

**n1 (NOTE) — `ν` orientation is inconsistent between AS ⟨1⟩7 and the frozen
convention, and ⟨1⟩6.⟨2⟩4 compares the two without saying so.**
`notation.md` line 269 freezes "convention fixed once: `ν = -ΔQ_W = q_- - q_+`",
matching MI ⟨1⟩5.⟨2⟩3 and D27's `E_{W,t_+}({q-ν})E_{W,t_-}({q})`.  AS
⟨1⟩7.⟨2⟩1 writes `ν = q_L - q_in = 0`, `ν = q_T - q_in = 2` — the **opposite**
orientation.  The shard's ⟨1⟩6.⟨2⟩4 sets the two ledgers side by side and
does not flag the flip.  `|ν|` is unaffected, so no conclusion of this round
changes; the defect is inherited from AS and should be raised there.

**n2 (NOTE) — ⟨1⟩6.⟨2⟩2(b)'s display mixes `sup_m` with a per-`m` bound.**
"`sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν) ≥ (1+2s|W_m|)‖F_{ch*}‖²` for all `m` with
`2s|W_m| > M`" is true read as "for each such `m` the `m`-th term is `≥ …`,
hence the sup is unbounded", but as literally displayed the free `m` on both
sides is ill-formed.  Cosmetic.

**n3 (NOTE) — the AKLT illustration is out of class** (see M1): `s=0` against
H-MQG(2)'s `s>0`.  Its number `ω((S^z_x)²)=2/3` is correct; I re-derived it
from the AKLT MPS.

**n4 (NOTE) — two sloppy constant definitions in ⟨1⟩4.**  ⟨2⟩3 sets
`C_a := sup_y‖a_{γ,b}(y)‖·‖κ_a(x)‖`, which mixes an operator norm with a
vector norm and retains a free `x` while being called uniform.  ⟨2⟩4 writes
`2M_W' := (2‖Q̂‖+|q_+|+|q_-|)C_a`, defining `2M_W'` rather than `M_W'`.  Both
are valid upper bounds; only the naming is wrong.

---

## 5. VERIFIED CORRECT — fenced; the repair lane must not churn this

Each item below I re-derived or re-ran independently.  **Do not rework.**

1. **ACE-LD-abs is correct and its rebuttal of the brief is correct.**
   ⟨1⟩1.⟨2⟩1: on `ran(1-E({q}))` the inverse norm is
   `max_{λ∈S∖{q}}|λ-q|^{-1} = 1/min_{λ}|λ-q| = d_q^{-1}` — sharp.  ⟨2⟩2's
   commutation chain is right.  ⟨2⟩3's coset gap `≥1` is right.  ⟨1⟩2.⟨2⟩1's
   decomposition is an identity; ⟨2⟩3's cross-term bound via
   `E({q_ch})E({q_{ch'}})=0` is right; ⟨2⟩4 assembles to
   `Σ_{ch'}d_{ch'}^{-1}ε_{ch'}`, `≤ n` under coset containment.  The `q∉S`
   and `S={q}` degenerate cases are handled.  **The lane's claim that the
   brief's Lagrange/Riesz machinery is unnecessary and its `t`-uniformity
   worry vacuous is CORRECT**: `Q̂_{W,c₀}` is Schrödinger-picture fixed, its
   spectrum is `t`-independent, and only the single gap is consumed.  The
   `N`-channel and general-on-site-spin generality of ⟨1⟩2.⟨2⟩5(i) is genuine
   — nothing in ⟨2⟩1–⟨2⟩4 uses `n=2` or the spin value.
2. **ACE-LD-nec is correct and is not a degenerate-weight artifact.**
   ⟨1⟩3.⟨2⟩1–⟨2⟩4 check out in both cases (`q'=q` and `q'≠q`), including the
   `q∉spec Q̂` contradiction with `‖Ψ_t‖=1`.  The shipped `--red-dup` mode
   reproduces it with the honest final error `1.0 = ‖P_+Ψ - P_-Ψ‖`, and my own
   mutation battery confirms it fires for the stated reason.
3. **LD-VAL is correct, including the `c₀` cancellation** (§0 above):
   `q_+ = 2s(b-c₀)`, `q_- = 2s(a-1-c₀)`, `q_+-q_- = 2s|W|`, re-derived from
   D13(a) and MI ⟨1⟩1.⟨2⟩2 rather than from the shard.
4. **⟨1⟩4.⟨2⟩2's use of ACE-tail is legitimate.**  The hypothesis of (D28-C)
   — `Λ_α ⊂ (-∞, x-r]` — is met for `x ≥ b+r`, and `α` is the left tail in
   both D13(a) and D28(5), so the side assignment is right.  `A=(Q̂_W-q_+)²`
   with `B=1` is an admissible one-tail instance; the square-root step with
   `2N` for `N` is correct.
5. **⟨1⟩4.⟨2⟩3 (LD-STRADDLE) is correct and *is* the term r1 objection 4
   demanded.**  `[Q̂,a(y)] = [Q̂, a(y)-A_{r_M/2}]` since the truncation's
   support is at distance `≥ r_M/2` from `W`, giving
   `‖[Q̂,a(y)]‖ ≤ 2‖Q̂‖C_N⟨r_M⟩^{-N}`.  This is the literal
   boundary-straddling charge of the dressing.
6. **⟨1⟩4.⟨2⟩4–⟨2⟩5 are correct.**  `‖G_t‖_1 = O(|t|²)` is AS ⟨1⟩4.⟨2⟩2's
   `O(1+|t|)` per tensor factor (AS itself flags it as a deliberate
   overestimate; `N` is free).  The Cook tail
   `∫_t^∞ Cu^{-3}du = (C/2)t^{-2}` uses AS ⟨1⟩5.⟨2⟩5's `N≥5` majorant
   correctly, and `P_chΨ_t = W_+e^{-itH_{0,ch}}F_ch` is AS ⟨1⟩6.⟨2⟩4's
   intertwining.  ⟨2⟩6 (LD-UNIQUE) is correct.
7. **Limit order is clean.**  ⟨1⟩4 and ⟨1⟩5 work at fixed `W` with
   `W`-dependent constants `M_W`, `t_0(W,ε_0)`; ⟨1⟩6.⟨2⟩2 takes `t_±→∓∞`
   first and `W_m↑ℤ` last.  **No D18(AD4) interchange anywhere.**
8. **No circularity and no reliance on a REFUTED row.**  Nothing uses ACE.3,
   AS ⟨1⟩7, or anything downstream of `(AD3-ex)`.  ML4-Ward (9) at `n≥2` is
   not touched.  Bethe appears only as "has not been consulted".  `𝒮_W` at
   `ρ≠1/2` is not invoked.  B3's REFUTED half-line formula is not used.
9. **⟨1⟩6.⟨3⟩1 (LD-IN), the lane's self-declared soft spot, is sound.**  The
   inherited AS estimates (⟨1⟩4.⟨2⟩1–⟨2⟩3, ⟨1⟩5.⟨2⟩5) are two-sided in `t`
   and the intertwining holds for `W_-^L`, so the time reflection is a
   substitution.  I also **confirmed it numerically**: in the `(V-in)`
   configuration the defect `‖E_W({q_σ̄})Ψ_{t_-}-Ψ_{t_-}‖` is `2.407e-09`,
   flat across `|W| = 17…513`.  It should still be written out, but it is not
   a defect.
10. **⟨1⟩6.⟨3⟩2's uniformity in `t_+` holds.**  With
    `R := E({q})Ψ_{t_-} - δ_{q,q_σ̄}Ψ_{t_-}`, `‖E({q-ν})UR‖ ≤ ‖R‖ = o(1)`
    uniformly, and squaring costs a factor `2`.  The Cesàro reduction is
    legitimate since the plain limits exist and the spectrum is finite.  I
    also verified that D27's Heisenberg-picture TPM reduces to the
    Schrödinger form ⟨3⟩2 uses:
    `E_{W,t_+}({q-ν})E_{W,t_-}({q})Ψ = e^{it_+H}E_W({q-ν})e^{-i(t_+-t_-)H}E_W({q})Ψ_{t_-}`.
11. **ACE-LD-obst's conclusion is correct on its own hypotheses** — see §0.
12. **The checker runs exactly as documented.**  `python3 -O` green exit `0`,
    `--red` exit `1`, `RED-OK`; all three registered break/survive patterns
    reproduce; §5's quoted red-coset figures are exact.  No bare `assert`; no
    fabricated numbers anywhere in §5.

---

## 6. Register comparison against the nearest PROVED rows

The nearest PROVED rows — **M-INDEX-fin**, **M-INDEX-spec**, **AC-EX** —
each carry an *"Adjudicated scoping (verbatim)"* paragraph that (i) names
every hypothesis in full, (ii) states the conclusion as an explicit
conditional implication, and (iii) closes with an enumeration of what is
**not** claimed ("no implication H-AD-G ⟹ (LR) is claimed", "no completeness,
raw-band-data implication, bound-state exclusion, threshold-inequality use, or
soft limit is claimed").

MP-1's three proposed rows do (i) and partly (ii), but carry **no
not-claimed clause at all**, and their conclusions are stated with
unrestricted quantifiers — "on D28 packets", "false for generic MPS vacua",
"jointly unsatisfiable".  By F1 the first is false, by M1 the second is far
weaker than the truth, and by M2 the third is scoped to a class with no known
instance.  **This artifact is not claiming in the same honest register as the
adjudicated rows**, and that gap is the whole of this verdict's severity.
The shard's own HONEST STATUS section, by contrast, *is* in register — it
flags the `⟨3⟩1` gap, the missing rate in ⟨1⟩4.⟨2⟩5, and the unverified
model question about `σ_L ≠ σ_T`.  The defect is that MERGE PROPOSALS does not
inherit HONEST STATUS's caution.

---

## 7. Cross-lane obligation — ACE-LD-obst vs bd `tns-xf4` (LR for D16)

`theory/lr-d16.md` does not yet exist; `tns-xf4` is IN_PROGRESS.  **The two
results are consistent, and I believe both.**  The reason is F1(b)(iii): D16's
kink band is exactly flat (`‖H_kink|K(z)⟩‖ ≤ 2.5e-16` for every `z` I tested,
ground energy `0` in every `S^z` sector), so `v_K ≡ 0`, the wall never
transits, `p_tr = 0`, and by ACE-LD-obst′ (M2) the LR3 first moment stays
bounded.  D16 therefore sits squarely in the *complement* of ACE-LD-obst's
`(V-ch)`/`(V-in)` class, and the obstruction does not bear on `tns-xf4` at
all.  **The `tns-xf4` lane must not be told that this round pre-empts it** —
which is precisely what MP-1's unscoped "on D28 packets" wording would do.

What the obstruction *does* tell `tns-xf4`: LR3 for D16 will hinge on the
flatness of the kink band (or on some other mechanism confining the wall), not
on the magnon dynamics.  That is a usable hint, and it should be transmitted
as one.

---

## 8. Deliverables the brief asks for by name

**Can `(AD3-ex)` be discharged from the AC-EX row?  NO.**  Three independent
blocks:

1. *Emptiness (F1).*  It is discharged only under `(E-TAIL) ∧ (V-ch) ∧
   σ_L≠σ_T`, a conjunction with no instance in this corpus and provably
   violated by D16.
2. *Wrong reading (M5).*  What is discharged is the vacuum-eigenstate reading;
   D18(AD3)'s and M-INDEX-spec's "kink charge eigenstate" reading is
   untouched.
3. *It is false at fixed `W` even in D16.*  `(AD3-ex)` at `W` forces
   `‖(Q̂_W-q_ch)P_chΨ_t‖ → 0`, i.e. zero asymptotic variance of `Q̂_W`.  I
   computed that variance on D16's exact zero-energy kink states by exact
   diagonalisation (`d16_var.py`, `Δ=2.5`, `L=12`, `s=1/2`, `c₀=5`,
   `Q̂_W = Σ_{x∈W}S^z_x + s(a+b-1-2c₀)`), minimised over `q` (the minimum is
   `√Var`, attained at `q=⟨Q̂_W⟩`):

```
   W        <Qhat_W>    min_q ||(Qhat_W - q)Psi||        ratio
  [4,7]      +1.000000        0.044534
  [3,8]      +0.999914        0.009304                   0.2089
  [2,9]      +0.999996        0.001940                   0.2085
  [1,10]     +1.000000        0.000396                   0.2041      (q = 0.208712)
```

   The defect is strictly positive at every finite `W` — so `(AD3-ex)`'s exact
   limit fails — and it decays **exactly** like `q^{d_W}` per unit of
   core-to-edge padding, reproducing `q = Δ-√(Δ²-1) = 0.208712` to three
   digits.  `⟨Q̂_W⟩` sits on the integer coset, as M-INDEX-fin requires.

That last computation is also the **repair direction**, and it is already
written into the corpus.  D13(a) says in its own words that meaningfulness
needs "the kink core padded from both edges of `W`" and that "if `d_W` is the
minimum core-to-edge distance, D1(c) gives, for every `λ̃ ∈ (λ_E,1)`, a tail
bound `C_{λ̃}λ̃^{d_W}`".  The statement that is *true*, that is compatible
with D27(LR3), and that AS ⟨1⟩7.⟨2⟩2's Cauchy–Schwarz step actually consumes
in the ordered limit is the `ε`-version:

> **(AD3-ex-ε).**  `limsup_{t→+∞}‖(Q̂_W-q_ch)P_chΨ_t‖ ≤ C_{λ̃}λ̃^{d_W}` at each
> fixed `W`, hence `→ 0` as `W↑ℤ` in the D18(AD4) order.

The exact-zero form at fixed `W` is the over-idealisation; the shard proves it
only by pushing the kink out of the window, and that is exactly what kills
LR3.  A round-2 target of `(AD3-ex-ε)` on the static-kink class avoids both
horns.

**What the C⇒B edge may honestly be called now.**  Not closed, not
obstructed — **regime-split and rerouted.**  Precisely:

> The C⇒B edge remains **conditional on `(AD3-ex)`, which is now known to be a
> false dichotomy as literally displayed**: it is refuted whenever both
> channels' kinks escape to the same side; it is provable only on a
> ballistic-kink, `χ=1`-vacuum class that no instantiated model realises and
> on which D27(LR3) then fails (ACE-LD-obst′); and it is strictly false at any
> fixed window even in D16, where the correct form is the `λ̃^{d_W}`
> `ε`-version.  The `{0,2}` ledger support is not a fixed-window theorem about
> the *unsubtracted* window charge on any ballistic class; obtaining it needs
> either the `ε`-version on a confined-kink class, or one of the three
> definition-level moves the shard lists in ⟨1⟩6.⟨2⟩3 — of which (iii),
> subtracting the free wall motion, is already the frozen D13(c) trap
> paragraph.

**ACE.3's remaining conditionality is unchanged in count and worse in
quality**: (i) (D28-C), unverified on any model; (ii) the charge-assignment /
ledger clause, untouched — and now known to be a *different* ledger from the
TPM `ν`-ledger (⟨1⟩6.⟨2⟩4, plus n1's orientation flip); (iii) Lane T1's
ordered outcome measure, which by ACE-LD-obst′ fails on any class with a
transiting wall; plus the new (iv) `(AD3-ex)` itself, which this round did not
discharge.

---

## 9. Objection ledger

| id | severity | one line |
|---|---|---|
| F1 | **FATAL** | `(E-TAIL) ∧ (V-ch)` empty on the corpus (D16 has an exactly flat kink band); ⟨1⟩6.⟨2⟩3's "on D28 packets the kink is ballistic" is false — D28(4) constrains only `v_M-v_K` |
| M1 | MAJOR | `(E-TAIL) ⟺ χ=1` `S^z`-product vacua and is *necessary*; the `χ>1` refutation is declined on a false reason (ACE-tail is an equality) |
| M2 | MAJOR | ACE-LD-obst is over-hypothesised; LR3 failure follows from D27's own first-moment identity with none of `(E-TAIL)`, `(V-ch)`, `(V-in)`, `σ_L≠σ_T`, `⟨3⟩1` |
| M3 | MAJOR | LD-C5's model violates `(V-in)` and never produces the `ν=0` atom; no red mode; MP-1's "tested in … LD-C5" overclaims |
| M4 | MAJOR | MP-2 proposes a compound non-status and a DAG upgrade on an uninhabited class |
| M5 | MAJOR | the discharged reading is the *vacuum*-eigenstate reading; D18(AD3)/M-INDEX-spec's *kink*-eigenstate reading is untouched |
| M6 | MAJOR | LD-C3 tolerates a `5×`-optimistic constant; `--red-coset` is a `10×` constant shrink, blind to cosets; §5's own prescription makes `--red` exit 2 |
| m1 | MINOR | LD-C1's `[P,H]=0` / orthogonality / resolution gates are structural no-ops; a real-space-projection mutation does fire them |
| m2 | MINOR | §0 cites ⟨1⟩5.⟨2⟩3 for uniqueness; it is at ⟨1⟩4.⟨2⟩6 |
| m3 | MINOR | §0's ACE-LD-nec ASSUME omits `w_1>0` |
| m4 | MINOR | §5 vs code: `N=4096`/`8192`, phantom "detune", "`d_ch` computed"/hardcoded |
| m5 | MINOR | inflated `depends on` (M-INDEX-fin on the abstract row; M-INDEX-spec on obst) |
| m6 | MINOR | MP-4 overloads `q` (D16 deformation parameter) and `σ` (packet widths) |
| m7 | MINOR | L2: 861 lines; split ⟨1⟩6 into its own shard |
| n1 | NOTE | `ν` orientation: `notation.md` freezes `q_- - q_+`; AS ⟨1⟩7.⟨2⟩1 uses the opposite; ⟨1⟩6.⟨2⟩4 compares without flagging |
| n2 | NOTE | ⟨1⟩6.⟨2⟩2(b) mixes `sup_m` with a per-`m` bound |
| n3 | NOTE | the AKLT illustration has `s=0`, outside H-MQG(2); its value `2/3` is correct |
| n4 | NOTE | `C_a` mixes operator and vector norms; `2M_W'` names the wrong side |

---

FAIL(F1, M1, M2, M3, M4, M5, M6)
