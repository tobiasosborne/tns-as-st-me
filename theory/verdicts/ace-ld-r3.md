<!-- ROLE: adversarial critic verdict, round 3, on theory/ace-ld.md,
     theory/ace-ld-r3-response.md and theory/checks/ace_ld_check.py.
     Protocol: briefs/critic-protocol.md (incl. Standing checker obligations).
     Brief: briefs/ace-ld-critic-r3.md.  Priors: theory/verdicts/ace-ld-r1.md
     FAIL(F1,M1-M6); theory/verdicts/ace-ld-r2.md FAIL(F1,M1-M6).
     Lane: this file only.  Nothing here edits the shard, definitions.md,
     notation.md or claims/CLAIMS.md; the promotion cells in section 8 are the
     only text authorised for merge, and they are authorised subject to the
     conditions stated there; no commit. -->

# ACE-LD r3 — critic verdict

**Verdict: FAIL(F1, M1, M2, M3).**
**Trajectory: r1 FAIL(F1,M1--M6) → r2 FAIL(F1,M1--M6) → r3 FAIL(F1,M1--M3).**
1 FATAL + 6 MAJOR → 1 FATAL + 6 MAJOR + 8 MINOR + 6 NOTE → 1 FATAL + 3 MAJOR
+ 8 MINOR + 6 NOTE.  Severity is falling and the round earns three promotions.

Every number below was produced by me, by an independent route.  Scripts live
in the session scratchpad and are named inline (`lr2.py`, `lr2b.py`,
`lr2c.py`, `lr2d.py`, `d16indep.py`, `chi.py`, `mut.py`).  The D16 battery was
rebuilt from scratch in the full `2^12` Hilbert space (not the checker's
sector-combinatorics construction) so that no number below is read off the
target.

**Headline.**  The retraction is complete, honest and correctly executed: all
seven r2 F1(a) sites are rewritten, MP-3(ii) is withdrawn, and MP-1's
`ACE-LD-eps` row carries the r2 §8(A) sentence **verbatim** (I diffed it: the
only differences are markdown pipe-escaping `‖`→`||` and a trailing period).
`ACE-LD-obst′` is right and is now stated at the right strength.  `LD-ID` is
right, exact, and worth its own row.  The checker is the best in this lane's
history: 21/21 red modes, every exit path in §5's table reproduced to the last
digit, the r2 tautology model now a *detected* mutant, and — the item the
brief asked me to press hardest — a seventh no-op gate correctly **refused**.

Three things fail.  **The FATAL is mine.**  `THEOREM ACE-LD-χ` says what my
own r2 M1(c) told the lane to write, and my r2 M1(c) was wrong: (K-TAIL) does
**not** force `χ=1` product tail vacua; it forces *sharp on-site charge*, and
the two coincide only when the tail density is a **simple** eigenvalue of
`S^z` — which H-MQG, D2(a) and D26 do not supply, and which
`notation.md` line 270 and `definitions.md` line 582 explicitly refuse to
impose.  I have built a counterexample.  The lane executed the work order
faithfully; the defect is upstream, in `ace-ld-r2.md` M1 and its §5 item 10.
**M1** is r2's F1 failure mode recurring one notch smaller: MP-3's replacement
text — merge text destined for `theory/ansatz-scattering.md` — states LD-MONO
without the qualifier that saves it, and is then refuted by the shard's own
LD-ID ⟨3⟩3 by up to twenty-one orders of magnitude.  **M2** is the LR2 item:
the lane's *finding* is real and I fence it, but the shipped gate measures a
different quantity, and a state on which D27(LR2) holds **exactly** passes the
same gate with a larger value.  **M3** is reachability, again.

---

## 0. What I recomputed first

**(i) LD-ID ⟨3⟩1, from the frozen definitions and then on every basis state.**
By hand: D13(a) `𝔛_W = a−1+(1/2s)Σ_{x=a}^b(S^z_x+s)`, `Q̂_{W,c_0}=2s(𝔛_W−c_0)`
(MI ⟨1⟩1.⟨2⟩2, notation.md line 267), and
`Σ_{x∈W}s_{γ_{c_0}}(x) = s[(c_0−a+1)−(b−c_0)] = −s(a+b−1−2c_0)`, so
`Q̂_{W,c_0} = Σ_{x∈W}(S^z_x − s_{γ_{c_0}}(x))` exactly.  Numerically
(`d16indep.py`), over six windows `[4,7],[3,8],[2,9],[1,10],[1,12],[2,6]` and
all `4096` basis states of the `L=12` chain: **`max|LHS−RHS| = 0.000e+00`.**

**(ii) `𝒬_{c_0} = 2s(X_1−c_0)`, from D13(c) directly.**  D13(c) reads
`X_1 = Σ_{x>0}(ϱ(S^z_x)+s)/(2s) − Σ_{x≤0}(s−ϱ(S^z_x))/(2s)`, so
`2sX_1 = Σ_{x>0}(S^z_x+s) + Σ_{x≤0}(S^z_x−s) = Σ_x(S^z_x − s_{γ_0}(x))`, and
moving the cut from `0` to `c_0` subtracts `2s c_0`.  The identification is
correct, and it is an identification with a **frozen** object, not a new one.

**(iii) The D16 instantiation, rebuilt in the full `2^{12}` space.**
All 13 sector ground energies vanish (`max|E_0| = 8.232e-17`); the half-filled
kernel is one-dimensional with gap `1.5341`; site profile
`−0.5,−0.5,−0.5,−0.4999,−0.4981,−0.4565,+0.4565,+0.4981,+0.4999,+0.5,+0.5,+0.5`
(↓ at `−∞`, ↑ at `+∞` — the ℤ₂-image of D13(a), m2 confirmed again).  Window
data:

| `W` | `⟨Q̂_W⟩` | `min_q‖(Q̂_W−q)Ψ‖` | ratio |
|---|---|---|---|
| `[4,7]` | `−0.99801996` | `4.453450e-02` | — |
| `[3,8]` | `−0.99991374` | `9.304727e-03` | `0.208933` |
| `[2,9]` | `−0.99999624` | `1.941946e-03` | `0.208705` |
| `[1,10]`| `−0.99999984` | `4.045736e-04` | `0.208334` |

against `q = Δ−√(Δ²−1) = 0.20871215`.  (K-TAIL) profile, core `K=[4,7]`,
ℤ₂-flipped assignment: right `4.356e-02, 9.092e-03, 1.898e-03, 3.960e-04,
8.266e-05`; left `1.898e-03, 3.960e-04, 8.266e-05`; per-site ratios `0.20871`
and `0.20872` — **both sides, every step**; `C_K = 0.208712`.  **⟨2⟩9(c)'s
r3 digits, §5's LD-C7 figures and LD-C7(e)'s profile are all correct.**  m1
and n5 are properly fixed.

**(iv) (K-TAIL) is not a clustering hypothesis.**  Each `D_x` is self-adjoint,
so `|ω_φ(D_xD_{x'})| = |⟨D_xφ,D_{x'}φ⟩| ≤ ‖D_xφ‖‖D_{x'}φ‖`: the off-diagonal
clause of (K-TAIL) is **implied by, hence equivalent to, its on-site clause**.
Measured on D16: `max_{same-side pairs} |ω_φ(D_xD_{x'})|/(C_K²q^{d+d'}) =
1.0000`, attained on the diagonal.  Consequence, in the lane's favour:
LD-C7(e) certifies (K-TAIL) **in full**, not merely its diagonal (see n1).

---

## 1. FATAL

### F1 (FATAL) — THEOREM ACE-LD-χ's `χ=1` clause is FALSE.  (K-TAIL) forces *sharp on-site charge*, not a product vacuum; the two coincide only when `s_γ` is a SIMPLE eigenvalue of `S^z`, which no hypothesis in force supplies.  I built the counterexample.  **This is my own r2 M1(c) coming back — the lane wrote exactly what I demanded**

**(a) Location.**  `theory/ace-ld.md` **⟨1⟩4.⟨2⟩9(b)⟨3⟩3** (the sentence "By
(a)'s Cauchy--Schwarz argument, `ω_γ = ⊗_x|s_γ⟩⟨s_γ|` — a `χ=1`
`S^z`-product state"); the same step inherited from **⟨2⟩9(a)** ("This is
EQUIVALENT to `ω_γ` being the fully polarised `χ=1` `S^z`-product state");
§0 **THEOREM ACE-LD-χ** PROVE block ("Both tail vacua are the `χ=1` fully
polarised `S^z`-product states"); §0 **THEOREM ACE-LD-ε SCOPE** ("(K-TAIL)
entails `χ=1` `S^z`-product tail vacua"); §4 HONEST STATUS, "Proved …"
ACE-LD-χ bullet and "Proved conditionally" Forced-scope clause;
**MP-1 row `ACE-LD-eps`**, "it therefore **forces both tail vacua to be `χ=1`
`S^z`-product states with `s ∈ spec S^z`**" — which is merge text destined for
`claims/CLAIMS.md`.  Upstream: `theory/verdicts/ace-ld-r2.md` **M1(b),(c),(d)**
and **§5 item 10** and **§8(A)** — my own, and wrong.

**(b) My computation** (`chi.py`, verified numerically; the algebra is exact).

*Where the proof breaks.*  ⟨3⟩2 correctly gives `ω_γ((S^z_0−s_γ)²)=0`.
Cauchy--Schwarz then correctly gives `ω_γ((S^z_x−s_γ)A)=0` for all `A`, hence
with `A = Π_x^{(m)}` the on-site spectral projection of `S^z_x`,
`(m−s_γ)ω_γ(Π_x^{(m)})=0`, hence `ω_γ(Π_x^{(m)})=δ_{m,s_γ}` and
`s_γ ∈ spec S^z`.  All correct.  The next words are not: writing
`ω_γ = ⊗_x|s_γ⟩⟨s_γ|` presumes that the eigenvalue `s_γ` names a unique
on-site **vector**.  It does so only if `dim ker(S^z−s_γ)=1`.  H-MQG(2) fixes
`S^z := −i q(ξ)` for a primitive circle direction of an arbitrary unitary
`u: G → U(ℂ^d)` and says nothing about multiplicities; D26(INT) says only
`spec S^z ⊂ κ+ℤ` ("True for every spin-`S` chain") and imposes none;
`notation.md` line 208/270 and `definitions.md` line 582 carry an explicit
**fence** that the gloss `d = 2s+1` "is the fully polarised special case and
is NOT a constraint".  So the simple-spectrum hypothesis is not merely absent
— the corpus has deliberately refused it.

*The counterexample.*  On-site space `ℂ² ⊗ ℂ³` (`d = 6`), circle charge
`S^z := σ^z/2 ⊗ 𝟙_3`.  Then `spec S^z = {+1/2, −1/2}`, **each of multiplicity
3**, and `e^{2πiS^z} = −𝟙`, so D26(INT) holds with `κ = 1/2`.  Take
`G = U(1) ⋊ ℤ₂` with `U(1)` generated by `S^z` and `ℤ₂` the flip
`σ^x ⊗ 𝟙_3`, and

  `ω_α = ⊗_x(|↑⟩⟨↑| ⊗ ϱ_{AKLT})`,  `ω_β = ⊗_x(|↓⟩⟨↓| ⊗ ϱ_{AKLT})`,

with `ϱ_{AKLT}` the spin-1 AKLT state in the `ℂ³` factor.  Measured
(`chi.py`): the composite tensor is **injective** (span rank of length-2
products `= 4 = χ²`); the transfer spectrum is `1` with second modulus
`1/3`, so the vacua cluster exponentially and D9(a)'s boundary conditions
hold; the bond Schmidt spectrum is `(0.5, 0.5)`, so **`χ = 2`, not `1`**.
`ω_α(S^z) = +1/2 = s = −ω_β(S^z)` (H-MQG(2) ✓, `s>0` ✓), `β = g·α` for the
`ℤ₂` element (H-MQG(1) ✓), common unbroken circle `U(1) ⊂ H_α ∩ H_β` ✓.
Now let `φ` be the sharp domain wall in the `ℂ²` factor with the AKLT chain
running unbroken through: `ω_φ ∈ 𝒦_{αβ}`, and `D_xφ = (S^z_x − s_{γ(x)})φ = 0`
at **every** site, so (K-TAIL) holds with `C_K = 0` and any `λ̃ ∈ (0,1)`,
core `K = [0,1]`.

Every hypothesis of THEOREM ACE-LD-χ holds; its conclusion fails.  The
`χ=1` clause is refuted, and so is ⟨2⟩9(a)'s "EQUIVALENT to … `χ=1`
`S^z`-product state" (the equivalence is with *sharp on-site charge*).

**(c) FIX DEMAND.**  In all six places, replace "`χ=1` `S^z`-product tail
vacua" by "tail vacua of **sharp on-site charge** `s_γ` — `ω_γ((S^z_x−s_γ)²)=0`,
equivalently `ω_γ(Π_x^{(s_γ)})=1`, at every site — hence `±s ∈ spec S^z`";
add as a separate clause "if moreover `s_γ` is a **simple** eigenvalue of
`S^z` (e.g. the standard spin-`S` register `d = 2s+1`), then
`ω_γ = ⊗_x|s_γ⟩⟨s_γ|` and `χ=1`"; and record in §0 and HONEST STATUS that the
unqualified `χ=1` form is REFUTED under H-MQG(1)--(2) alone, citing this
objection's counterexample.  MP-1's `ACE-LD-eps` row must take the corrected
clause of §8(A) below, **not** the r2 §8(A) sentence, which I hereby withdraw.

**(d) SURVIVING WEAKER STATEMENT — and it is still a theorem worth the round.**
*(K-TAIL) plus D9(a) membership forces both tail vacua to have zero on-site
charge variance at every site, hence `±s ∈ spec S^z`.*  I re-derived every
step and endorse it.  Everything the shard actually needs survives: sharp
on-site charge already excludes every vacuum with nonzero on-site charge
variance, in particular generic injective-MPS vacua — the scope point the
theorem exists to make.  **The concrete corollary the brief singles out
survives intact and I certify it: a spin-1 chain with calibration `s = 1/2`
admits no (K-TAIL) kink state, because `±1/2 ∉ spec S^z = {−1,0,1}`.**  What
is lost is only the bond-dimension clause.  The upgrade from r2's hedged
remark to a theorem was the right move; the theorem was simply stated one
clause too strong, at my instruction.

---

## 2. MAJOR

### M1 (MAJOR) — MP-3's LD-MONO sentence, the text destined for `theory/ansatz-scattering.md`, drops the qualifier that makes the lemma true and is then refuted by the shard's own LD-ID ⟨3⟩3 by up to `10^{21}`

**(a) Location.**  `theory/ace-ld.md` **MP-3**, clause (ii) replacement text:
"an assumed ε-form (AD3-ex) at one core-containing window **propagates to
every larger window** up to a uniform `2C_Kλ̃^{d_W}/(1−λ̃)`, using annulus
clustering only — **compatible with a leg that has already escaped**."
Secondarily **⟨1⟩4.⟨2⟩7**, LEMMA LD-MONO's closing PROVE gloss ("propagates to
every larger window up to a uniform additive …"), whose universal `W'` does not
match its own ASSUME, which fixes one `W'`.

**(b) My computation** (`d16indep.py`, last block; exact by hand as well).
Sharp kink at `c_0 = 0` with `s = 1/2`, one magnon (flipped spin relative to
the local vacuum) at `y = 40` on the `β` side — i.e. a leg of charge `2s = 1`
that has escaped `W` but lies **inside** `W' = [−100,100]`.  Then
`Σ_{x∈W'∖W}D_x` picks up exactly the leg:

| `W` | `d_W` | `‖(Q̂_{W'}−Q̂_W)φ‖` measured | LD-MONO's asserted uniform bound (`C_K=1, λ̃=q`) |
|---|---|---|---|
| `[−4,4]` | 4 | `1.0000` | `4.80e-03` |
| `[−8,8]` | 8 | `1.0000` | `9.10e-06` |
| `[−16,16]` | 16 | `1.0000` | `3.28e-11` |
| `[−32,32]` | 32 | `1.0000` | `4.25e-22` |

The measured value is `2s = |q_leg|`, at every padding, and the asserted
bound is violated by up to twenty-one orders of magnitude.  This is not a
new fact — it is **the shard's own LD-ID ⟨3⟩3**, read at `W' ↑ ℤ`.  The
lemma itself is safe: its ASSUME demands the (K-TAIL) bound *on the annulus
`W'∖W`*, which fails the instant the annulus reaches the leg, and ⟨2⟩7's own
parenthetical says "compatible with an escaping leg that has already passed
**beyond `W'`**".  MP-3 deletes exactly those four words and keeps "every
larger window".  Read literally, MP-3's sentence is false, and it is the
sentence that would enter `theory/ansatz-scattering.md` — the same failure
mode as r2's F1, one notch smaller.

**(c) FIX DEMAND.**  In MP-3(ii) and in ⟨2⟩7's PROVE gloss, restore the
quantifier: "propagates to every larger window `W'` **whose annulus `W'∖W`
carries no escaped charge — equivalently, every `W'` the leg has already
passed beyond**; at the first `W'` that reaches the leg the difference is
exactly the leg charge (LD-ID ⟨3⟩3), so the transport is not available past
that window."

**(d) SURVIVING WEAKER STATEMENT.**  LD-MONO **as ASSUMEd is correct** and I
endorse it: I re-derived LD-SPLIT and ⟨2⟩2(i), and the annulus hypothesis is
genuinely weaker than (K-TAIL) (it says nothing about the far tail) and
genuinely compatible with a leg beyond `W'`.  It is the right thing to offer
the AS lane, and HONEST STATUS states it correctly ("compatible with an
escaped leg **beyond the outer window**").  Only MP-3's compression is false.

---

### M2 (MAJOR) — LD-C5b does not measure D27(LR2).  It measures the dephasing defect at `t_- = 0`; D27(LR2) pinches at `t_- → −∞`.  The *finding* is nevertheless TRUE, at a different number — and a state on which D27(LR2) holds **exactly** passes the same gate with a **larger** value

**(a) Location.**  `theory/ace-ld.md` §5, `LD-C5b` bullet ("This certifies
that the D27(LR2) pinching `𝒟` genuinely acts on a two-branch state — and
that LR2 measurably FAILS there (the defect saturates at `6.083` by
`t = 320`; it does not Cesàro-decay)") and its clause (ii); the same claim in
§4 HONEST STATUS "Merely evidence"; `theory/checks/ace_ld_check.py`
`check_c5b` docstring and its green log line ("**LR2 fails pointwise AND on
average here (measured)**"); `theory/ace-ld-r3-response.md` row M4(v).

**(b) My computation** (`lr2.py`, `lr2b.py`, `lr2c.py`, `lr2d.py`; own
Hamiltonian, own packet, own clamp charge, own pinching — nothing imported).

*First, what the gate is.*  `Σ_ν ν p_W(ν) = ⟨Q̂_W⟩_{t_-} −
⟨𝒟_{W,t_-}(Q̂_W(t_+))⟩` identically, so the shipped wedge is exactly
`|⟨𝒟_{W,t_-}(Q̂_W(t_+))⟩ − ⟨Q̂_W(t_+)⟩|` — the D27(LR2) integrand — **at the
single time pair `(t_-,t_+) = (0,300)`**.  I reproduce it: `6.0832`, the
checker's value to four decimals.

*Second, the shard's "saturation" is a `t_+` sweep at `t_- = 0`, which is not
D27's quantity.*  Measured at `t_- = 0`: `−6.0798, −6.0828, −6.0832,
−6.0832, −6.0832, −6.0832, −6.0832, −6.0828` at
`t_+ = 40,80,160,240,300,320,400,500`.  Saturation confirmed — and irrelevant,
because D27(LR2) averages over `t_+ ∈ [T,2T]` **and `t_- ∈ [−2T,−T]`**.

*Third, the actual D27(LR2) double-Cesàro average* (9×9 grids on
`[T,2T]×[−2T,−T]`):

| `T` | 20 | 40 | 80 | 120 | 200 |
|---|---|---|---|---|---|
| mean defect | `−3.3592` | `−3.3592` | `−3.3592` | `−3.3592` | `−3.3594` |

**`−3.3592`, not `6.083`.**  So D27(LR2) *does* fail on the shipped
straddling state — the lane's conclusion is right — but the number the shard
publishes for that claim is the wrong quantity, larger by a factor `1.81`.

*Fourth, the inference is invalid, and I have the counterexample.*  Take the
**same straddling packet in the same window with `V_0 = 0`** (no barrier).
Then the `t_-=0` defect is `−8.3868` — **larger** than the green
configuration — while the D27(LR2) quantity is
`−1.35e-06, −2.17e-09, −2.66e-13, −2.13e-14` at `T = 50,100,200,300`, i.e.
**LR2 holds exactly**.  I ran `check_c5b` on that model on a copy
(`mut.py` block C): **it PASSES the gate.**  A gate that a state satisfying
D27(LR2) passes cannot certify that D27(LR2) fails.

*Fifth, the mechanism the shard never names.*  Why does LR2 fail on the
shipped state?  Under **backward** evolution the straddling packet splits
across three clamp-charge branches and stays split forever: left `q=0`
`0.8563`, inside `W` `0.0170`, right `q=17` `0.1267`, constant from
`t_- = −20` to `t_- = −400`.  The pinching therefore never becomes trivial.
The barrier bound state (`E = 2.332381`, weight `0.0170` in `ψ_0`, `0.99995`
of its mass inside `W`) is **not** the cause: projecting it out leaves the
defect at `−3.4116`.

**(c) FIX DEMAND.**  Re-anchor LD-C5b at `t_- ≪ 0` (or on a double-Cesàro
pair) and gate the corrected quantity with a floor keyed to `3.359`, not
`6.083`; quote `3.359` wherever the (LR2) claim is made; delete "AND on
average (measured)" from the green log line and §5 unless the average is
actually computed in the checker (it is computed nowhere); and register the
`V_0 = 0` straddling model as a red mode of the **corrected** gate, since it
is the state that separates "`𝒟` acts" from "LR2 fails".

**(d) SURVIVING WEAKER STATEMENT — two of them, and I fence both.**
(1) The gate's *other* advertised content is exactly right: in the straddling
configuration `𝒟` genuinely acts (`6.0832`), so LD-C5(d)'s agreement to
`4e-11` in the concentrated configuration is due to gate (a) and to nothing
else.  That was r2 M4's demand and it is met.
(2) **The finding itself is TRUE and I certify it independently: D27(LR2)
fails on the shipped straddling state, with double-Cesàro defect `−3.3592`,
stable across `T = 20…200`, and it fails because the backward-evolved state
stays split across three window-charge branches, not because of the bound
state.**  This is a real fact about a frozen definition clause and it should
be recorded as one — at the right number.

---

### M3 (MAJOR) — §5's "Honest unreached rows" is presented as the reachability disclosure but omits every gate that an earlier gate shadows, including the one gate that carries LD-C6's advertised content; and that gate's threshold is time-tuned — the *green* model fires it at `t_+ = 20`

**(a) Location.**  `theory/ace-ld.md` §5, "**Honest unreached rows (disclosed,
not papered over):**" (three numbered items) and the reachability table above
it; `theory/ace-ld-r3-response.md` row M4(i) and its checker record ("plus an
explicit **unreached** list with reasons");
`theory/checks/ace_ld_check.py` `check_c6` gate (c) and `C6_MOM_BOUND = 1.0`.

**(b) My computation** (`mut.py`, on a copy, plus the full `--red` exit-path
log).

*The unreached list is incomplete.*  Reading every exit path of all 21 modes,
these gates are reached by **no** registered mutation and are **not** listed:
LD-C6's BOUNDED-FIRST-MOMENT gate; LD-C7(e)'s per-side PROFILE-RATIO sub-gate;
LD-C5's transit-atom sub-gate (`ptr > 0.05`); LD-C5's off-atom-mass sub-gate
(`|other| < 1e-4`); LD-C5(c)'s transmit-weight half (`|ptr−t²| < 1e-3`);
LD-C5's ring-cut guard; LD-C2's monotone-decrease sub-gate; LD-C6's
magnon-creation guard; LD-C1's wrap guard.  Two of these carry advertised
evidence, and in both the cause is the standing obligation's named pattern —
*an earlier gate fires first on every mutant that would reach them*.  I
verified both by disabling the shadowing gate on a copy:

- LD-C6 first moment, with the SUPPORT gate disabled: `c6-moving` fires it at
  `Σ|ν|p = 12.4024 > 1.0`.  It has teeth; nothing reaches it.
- LD-C7(e) profile ratio, with the `C_K` gate disabled: `c7-orientation`
  fires it at `ratio 1.0000` on side L.  Same.

*And LD-C6's threshold is tuned to the shipped time, not to the claim.*  The
gate's advertised content is "`Σ|ν|p ≤ 1.0` at every window — **non-extensive
in `|W|`**".  I ran the **green** model at other protocol times:
`t_+ = 4` passes (`0.453`); **`t_+ = 20` FIRES at `Σ|ν|p = 1.0712 > 1.0` at
`W=[3,8]`**; `t_+ = 40` and `t_+ = 200` pass again.  So `C6_MOM_BOUND = 1.0`
is a constant calibrated to `t_+ = 4`; what the gate certifies is
"`Σ|ν|p ≤ 1` at `t_+ = 4`", not bounded transport.  (Related but not a defect:
the liveness margin is thin — moving the magnon from site 10 to site 7 drops
`1−p_0` to `1.158e-02`, below the `0.02` floor, and the gate fires.)

**(c) FIX DEMAND.**  Either enumerate every unreached gate in §5's list with
its shadowing gate named, or state plainly that the list covers only
evidence-carrying gates and then include LD-C6's first moment and LD-C7(e)'s
ratio in it; reorder `check_c6` so the first-moment gate is evaluated before
the support gate (one line, and it makes `c6-moving` reach it); and either
raise `C6_MOM_BOUND` above the `t_+`-sweep maximum with the sweep recorded, or
restate the gate as "`Σ|ν|p ≤ 1` at the fixed protocol time `t_+ = 4`" in §5
and in MP-1's obst row "tested in" cell.

**(d) SURVIVING WEAKER STATEMENT.**  The r2 M4 blanket claim is genuinely
gone and the published table is genuinely measured — I reproduced all 21 exit
paths and every quoted digit.  LD-C6's SUPPORT gate is real, reached, and
carries the contrast the rebuild was for (`c6-moving` dies at
`mass 7.296e-01 at |ν|>3`, against LD-C5's `ν = −|W|` atom).  LD-C5(e)'s floor
and LD-C3's liveness floor are correctly disclosed as unreachable in-class,
and I confirm both.  The defect is that the disclosure stops three items early
and that one threshold is time-tuned.

---

## 3. MINOR

**m1 (MINOR) — LD-ID's ASSUME line covers ⟨3⟩1 only, yet HONEST STATUS files
the whole theorem as unconditional.**  *(a)* ⟨1⟩4.⟨2⟩7, "**THEOREM LD-ID.**
ASSUME H-MQG(1)--(2)"; §4 HONEST STATUS, bucket "**Proved, given only its own
ASSUME block (unconditional as an implication)**", LD-ID bullet.  *(b)* Only
⟨3⟩1 follows from H-MQG(1)--(2).  ⟨3⟩2 consumes (K-TAIL) (the limit vector
does not otherwise exist) and D13(c); ⟨3⟩3 consumes (K-TAIL) with
`t`-independent constants **and** D18(AD3); ⟨3⟩4 consumes (K-TAIL), (K-Q) at
`ε_Q = 0`, `t`-uniform data and D27's definition of `δx`.  The sub-steps do
name these in their own text, so nothing is hidden — but the theorem-level
ASSUME and the HONEST STATUS bucket both say otherwise.  *(c)* Extend LD-ID's
ASSUME to list the per-clause hypotheses, and split the HONEST STATUS bullet
into "⟨3⟩1--⟨3⟩2 unconditional / ⟨3⟩3--⟨3⟩4 conditional as named".  *(d)* The
mathematics is correct at every step; this is lockstep only.  My §8(C) cell
carries the split.

**m2 (MINOR, L6b) — ⟨3⟩3's norm lower bound is asserted, not derived.**
*(a)* ⟨1⟩4.⟨2⟩7 ⟨3⟩3, "`‖𝒬_{c_0}Ψ_t − Q̂_{W,c_0}Ψ_t‖ ≥ |q_leg| − o(1)`",
justified only by "⟨3⟩2 and D18(AD3)'s frozen clause".  *(b)* The step is
true, but the one-line reason is missing: for unit `Ψ_t`,
`‖Σ_{x∉W}D_xΨ_t‖ ≥ |⟨Ψ_t, Σ_{x∉W}D_xΨ_t⟩| = |Σ_{x∉W}ω_{Ψ_t}(D_x)|`, and
D18(AD3) says that mean tends to `q_leg`.  L6b requires the leaf.  *(c)*
Display that inequality as the justification.  *(d)* ⟨3⟩3's conclusion stands.

**m3 (MINOR) — MP-1's obst row and MP-6 assert `θ_{tr} = 0` for D16 on
M-quant-G without naming M-quant-G's condition, which this very shard shows is
incompatible with (K-TAIL).**  *(a)* MP-1 `ACE-LD-obst-prime` not-claimed
clause; MP-6; ⟨1⟩5.⟨2⟩6(iii); §0 obst′ Scope.  *(b)* M-quant-G is PROVED
**conditional on H-AD-G**, i.e. on D18(AD1)--(AD4) for the selected vector —
open for D16 (`AD3-ex` is CONJECTURE; full-chain D18 is bd `tns-d51`).  The
shard writes "M-quant-G's conclusion (PROVED conditional)" without naming the
condition.  This matters *here* more than elsewhere, because LD-ID ⟨3⟩3 proves
D18(AD3) jointly unsatisfiable with (K-TAIL) — so the `θ_{tr}=0` fence and the
ε-theorem apply to disjoint state classes, and a reader of the merged row
cannot see that.  *(c)* Name the condition and add one sentence that the two
statements concern different states (a kink--magnon D17 packet under H-AD-G
versus a magnon-free (K-TAIL) sector state).  *(d)* The fence's conclusion is
still right and `tns-xf4` is still not pre-empted.  My §8(B) cell names the
condition.

**m4 (MINOR, L5) — the obst row's dependency on the first-moment identity is
mis-registered.**  *(a)* MP-1 register note, "M-INDEX-spec is on no row";
obst row depends-on `D13, D17, D26, D27, M-INDEX-fin`.  *(b)* ⟨1⟩5.⟨2⟩2
consumes MI ⟨1⟩7.⟨2⟩1--⟨2⟩2, which lies inside **M-INDEX-spec's** where-proved
range (`memory-index.md ⟨1⟩4--⟨1⟩8`), not M-INDEX-fin's (`⟨1⟩1, ⟨1⟩5`).
Listing M-INDEX-spec would however be *worse*, since its statement is
(LR3)-conditional and the proof is a contradiction against (LR3).  *(c)* Keep
the depends-on as is and add the r2 n6 sentence to the row prose: the identity
is consumed at sub-step level, whose leaves carry only D27(LR1)--(LR2) and
(IDX.1).  *(d)* No circularity — r2 n6 checked both leaves and so did I.

**m5 (MINOR) — MP-6's cross-lane composition is cited against a superseded
verdict, and its stated route is now the wrong one.**  *(a)* MP-6; also the
lr-d16-r1 citations at ⟨3⟩1, ⟨3⟩4, HONEST STATUS and MP-1's obst row.
*(b)* `theory/verdicts/lr-d16-r2.md` now exists ("Severity has fallen: no
FATAL survives"), `(LR2′)` is withdrawn, and `(NR)` has been **repaired to two
clauses carrying `sup_m`**.  The composition survives — and is now cleaner
than MP-6 says: `theory/lr-d16.md` ⟨1⟩5.⟨2⟩7 THEOREM (LRD-3) states
`(NR) ⟹ D27(LR3)` with tail `2S_{NR}/M`, so composing with ACE-LD-obst′(b)
gives `(M-ESC) ⟹ ¬(NR)` **directly**, with no appeal to ⟨1⟩5.⟨2⟩4's
monotonicity remark.  *(c)* Re-cite MP-6 to the repaired THEOREM (LRD-3) and
to lr-d16-r2, and add MP-1's no-witness disclosure to MP-6 as well — lr-d16-r2
M4(b)3 makes precisely the point that a conditional with an empty antecedent
constrains nothing until a witness exists.  *(d)* The composition is correct
and worth transmitting.

**m6 (MINOR) — the eps row's incompatibility clause drops the `t`-independence
qualifier that makes it true.**  *(a)* MP-1 `ACE-LD-eps`, "so no state
carrying an escaping leg of nonzero charge satisfies it".  *(b)* At a **single**
time, (K-TAIL) *is* satisfiable with a leg present at any finite distance `R`,
by taking `C_K ∼ λ̃^{-R}`; the incompatibility is with `t`-**independent**
`(K, C_K, λ̃)`, exactly as ⟨3⟩3 and the ε-t Class warning say.  *(c)* Insert
"with `t`-independent `(K, C_K, λ̃)`".  *(d)* The clause is right as ⟨3⟩3
states it.  My §8(A) cell carries the qualifier.

**m7 (MINOR) — HONEST STATUS's own L2 self-report is stale.**  *(a)* §4,
"(i) This shard is ~1200 lines".  *(b)* `wc -l` = **1447**; the r3-response
row m8 says "~1450".  *(c)* Say 1447.  *(d)* MP-5's split is still the right
answer and I endorse it again.

**m8 (MINOR) — the checker advertises a flag it does not have.**  *(a)*
`theory/checks/ace_ld_check.py` module docstring, "The reachability TABLE is
printed by `--table`".  *(b)* `python3 -O theory/checks/ace_ld_check.py
--table` → argparse usage error; `main` registers only `--red` and
`--red-<mode>`.  *(c)* Implement `--table` or delete the sentence.  *(d)* The
table itself is in §5 and is correct.

---

## 4. NOTE

**n1 (NOTE — in the lane's favour, and a simplification it is missing).**
(K-TAIL)'s off-diagonal clause is *equivalent* to its on-site clause: each
`D_x` is self-adjoint, so `|ω_φ(D_xD_{x'})| ≤ ‖D_xφ‖‖D_{x'}φ‖ ≤
C_K²λ̃^{d(x)}λ̃^{d(x')}`.  Measured on D16, the ratio
`|ω_φ(D_xD_{x'})|/(C_K²q^{d+d'})` maxes at exactly `1.0000` on the diagonal.
Two consequences: **LD-C7(e) certifies (K-TAIL) in full**, which is stronger
than the n5 disposition claims; and ⟨1⟩4.⟨2⟩2(i) can be proved by the
triangle inequality alone (`‖Σ_F D_xφ‖ ≤ Σ_F ‖D_xφ‖`), with no square
expansion.  (K-TAIL) should be described as an on-site tail-decay hypothesis,
not as "clustering".

**n2 (NOTE — the M2 addition is genuine, and the shard understates it).**
The brief asks whether the `M_0` route is a real addition over D27's own
existence corollary.  It is, and by more than the shard says.  D27's corollary
("LR3 makes the left side converge, hence the right side") delivers
convergence **along the full sequence only under D27's optional convenience
clause**, and otherwise only along an (LR3) subsequence — so boundedness
follows only along that subsequence.  ⟨1⟩5.⟨2⟩3 delivers `sup_m` over **all**
`m`, with no subsequence and no convenience clause.  Rule: the addition is
genuine, and the disclosure should say *that*, not merely "without passing
through weak convergence".

**n3 (NOTE — checker runs, measured here).**  `python3 -O` green → **exit 0**
in 27.8 s (§5 says 118 s — machine-local, drop the wall clock or mark it as
such); `--red` → **exit 1, RED-OK, 21/21** in 81.6 s.  Every one of the 21
registered exit paths in §5's table reproduced **verbatim**, including
`separation 1.000e-01`, `spread 4.142e-01`, `[P_+,H] 5.316e-01`,
`orthogonality 6.455e-02`, `resolution 8.068e-02`, `26.4/0.80/1.00`,
`p0 = 0`, `−12.4024 vs −11.4024`, `defect 9.971e-01`,
`0.2704 != 0.3204`, `13.132 -> 13.132`, `1.776e-15`, `4.260e-11`,
`1−p_0 = −2.220e-16`, `mass 7.296e-01`, `0.1717`, `−0.499010`, `defect 0`,
`max|E0| 1.146`, `C_K = 2525.009`.  Spec/code lockstep is **exact**.  No bare
`assert` anywhere.

**n4 (NOTE — credit).**  `--red-c6-static` is a genuine, sharp disposition of
r2 M3: the r2 tautology model is now itself a registered mutant and dies at
the new liveness gate (`1−p_0 = −2.220e-16`).  That is the strongest available
proof that the rebuilt gate tests what the old one could not, and I confirm it.

**n5 (NOTE — credit).**  The corrected `c1-leak` registration is right: the
measured pattern is LD-C1 resolution `8.068e-02`, LD-C2 `1.099e-01`, LD-C4
`4.841e-02`, LD-C3 survives — exactly as registered.  Recording that the first
red run exited 2 and caught the mis-registration is the right kind of
disclosure and the corpus should keep doing it.

**n6 (NOTE — the seventh no-op was correctly refused, and I certify the
reason).**  The lane's algebra is right: `Σ_ν ν p_W = ⟨Q̂_W⟩_{t_-} −
⟨𝒟_{W,t_-}(Q̂_W(t_+))⟩` **identically**, so a gate comparing those two sides
would be `x ≡ x` — the campaign's no-op pattern, and it would have been number
seven.  I confirm this both algebraically and numerically: my independently
computed pinch defect `⟨𝒟_0(Q̂(300))⟩ − ⟨Q̂(300)⟩ = −6.0832` equals the
checker's `Σνp − (⟨Q̂⟩_- − ⟨Q̂⟩_+) = 6.0832` to every printed digit, which is
the identity holding.  **Refusing to ship it was correct and deserves the
credit the brief anticipated.**  What the substitute gate then measures is the
subject of M2.

---

## 5. VERIFIED CORRECT — fenced; the r4 repair lane must not churn this

Each item re-derived or re-run by me, independently.  **This fence is
additional to r2 §5's 14 items, which I re-read step by step and confirm are
untouched — no fenced step was reworked, exactly as the r3-response claims.**

1. **LD-ID ⟨3⟩1**, `Q̂_{W,c_0} = Σ_{x∈W}(S^z_x − s_{γ_{c_0}}(x))` exactly.
   Re-derived from D13(a)+MI ⟨1⟩1.⟨2⟩2 and checked on all `4096` basis states
   over six windows: `max|LHS−RHS| = 0.000e+00`.
2. **LD-ID ⟨3⟩2**, `𝒬_{c_0} = 2s(X_1−c_0)`.  Re-derived from D13(c)'s own
   display.  The identification is with a frozen object; m3 of r2 is properly
   discharged.
3. **LD-ID ⟨3⟩3's logic** (given m2's missing leaf): the contradiction is
   correct, and its quantitative witness is right — I get `‖(Q̂_{W'}−Q̂_W)φ‖ =
   2s` at every padding for an escaped leg.
4. **LD-ID ⟨3⟩4's arithmetic**: `|δx| ≤ (2s)^{-1}·2·2C_Kλ̃^{d_W}/(1−λ̃) =
   s^{-1}·2C_Kλ̃^{d_W}/(1−λ̃) → 0`, using `𝔛_W = Q̂_W/(2s)+c_0` and Cesàro
   convexity.  Correct.
5. **LEMMA LD-MONO as ASSUMEd** (⟨2⟩7): correct, genuinely anchor-free,
   genuinely uniform in `W'`, and genuinely compatible with a leg beyond `W'`.
   Only MP-3's compression of it is wrong (M1).
6. **ACE-LD-χ's `s_γ ∈ spec S^z` clause** and the **spin-1 at `s = 1/2`
   exclusion**.  Correct, and they survive F1 untouched.  So does the
   zero-on-site-variance conclusion, which is what the scope argument needs.
7. **The M2 restatement**, verbatim and identical in all three demanded places
   (§0 obst′(c); ⟨1⟩5.⟨2⟩4's closing; MP-1's obst row), with the word
   "contrapositive" surviving only in the sentences that say it is *not* one.
   The `O(1)` rate is right and the `M_0` argument re-derives.
8. **⟨1⟩5.⟨2⟩3** (`Σ|ν|p ≤ M_0·1 + 1`) and the conversion to
   `sup_m|ω^+−ω^-|(𝔛_{W_m}) ≤ (M_0+1)/(2s)`.  Re-derived.
9. **LD-C7(a)--(e), every number**, by an independent full-`2^{12}` ED:
   sector energies `8.232e-17`; kernel dimension 1 in the half-filled sector
   with gap `1.5341`; defects `4.453450e-02, 9.304727e-03, 1.941946e-03,
   4.045736e-04`; ratios `0.208933, 0.208705, 0.208334`; `⟨Q̂_W⟩` from
   `−0.99801996` to `−0.99999984`; (K-TAIL) profile and both-side ratios
   `0.20871`; `C_K = 0.208712`.  **m1 and n5 are fully and correctly fixed.**
10. **The F1 retraction is complete.**  All seven r2 F1(a) sites rewritten;
    MP-3(ii) withdrawn and replaced; and MP-1's `ACE-LD-eps` row is the r2
    §8(A) sentence **verbatim** (diffed: only `‖`→`||` escaping and a trailing
    period differ).  No "supplies AS ⟨1⟩7.⟨2⟩2" claim survives anywhere.
11. **The checker's green and red runs** as documented in n3: exit 0 / exit 1
    RED-OK 21/21, 21 exit paths reproduced digit for digit.
12. **`--red-c6-static` and the corrected `c1-leak` registration** (n4, n5).
13. **LD-C7(e) certifies (K-TAIL) in full**, by n1's Cauchy--Schwarz
    equivalence — stronger than the shard claims for it.
14. **The refusal to ship the identity-with-`𝒟` gate** (n6): the identity is
    exact, the gate would have been `x ≡ x`, and the refusal was right.
15. **M6 is properly fixed.**  MP-2 now carries M6(c) verbatim, `AD3-ex` stays
    CONJECTURE, "not refuted, unavailable" is the correct verdict, and the
    §8(E) regime split by escaped charge is in.
16. **M5 is properly fixed** in all four places plus ⟨1⟩4.⟨2⟩4: K1+K2 PROVED,
    K4 named CONJECTURE, band flatness no longer load-bearing, LD-C7(a)
    correctly demoted to "sector ground energies only".
17. **m5, m6, m7, n3, n4, n6 are fixed as claimed** — I checked each site.
    The 21 claimed dispositions are honest with the three exceptions this
    verdict raises (M1 inside F1's disposition, M2's `on average` inside
    M4(v), M4(i)'s unreached list).

---

## 6. Register comparison against the nearest PROVED rows

The nearest adjudicated rows — **M-INDEX-fin**, **M-INDEX-spec**, **AC-EX**,
**AC-EX-2M** — each carry an "Adjudicated scoping (verbatim)" paragraph that
(i) names every hypothesis in full, (ii) states the conclusion as an explicit
conditional implication, and (iii) closes with an enumeration of what is not
claimed, **including the negative facts that hurt**.

MP-1's three rows now do all three, and the eps row does (iii) properly for
the first time: the retraction, the joint unsatisfiability, the `δx = 0`
consequence, the m7 no-witness disclosure and the n1 subsumption are all in
the not-claimed enumerations.  **On register this is the strongest round the
lane has produced, and it is now at the same standard as M-INDEX-spec.**  Two
gaps remain and both are addressed in my cells: the eps row states one
positive clause that is *false* (the `χ=1` clause — F1, inherited from my own
r2 §8(A), so the register defect is mine and not the lane's), and the obst row
asserts `θ_{tr}=0` for D16 on a conditional whose condition it does not name
(m3) — the same species of defect as AC-EX's "(D28-C) is the load-bearing
hypothesis and is unverified on any model", which that row *does* disclose.

---

## 7. The item the brief asked me to press hardest — ruling

**Did the lane withhold the identity gate for a good reason?  Half yes, half
no, and the half that matters is yes.**

- **The refusal itself is correct and I certify it.**  `Σ_ν ν p_W ≡
  ⟨Q̂_W⟩_{t_-} − ⟨𝒟_{W,t_-}(Q̂_W(t_+))⟩` is an identity; an identity gate
  would have been the campaign's seventh no-op.  Confirmed algebraically and
  numerically (n6).  **Credit is due and I record it.**
- **The stated ground is wrong as stated.**  "The defect saturates at `6.083`
  with no Cesàro decay, i.e. D27(LR2) genuinely fails" conflates the defect at
  `t_- = 0` with D27's double-Cesàro average over `t_- ∈ [−2T,−T]`.  The
  inference is invalid: the same straddling packet with `V_0 = 0` has a larger
  `t_-=0` defect (`−8.3868`), passes the shipped gate, and satisfies D27(LR2)
  **exactly** (`−2.1e-14` at `T = 300`).
- **But the conclusion is TRUE on the shipped state, and I fence it.**  The
  genuine D27(LR2) double-Cesàro defect there is **`−3.3592`**, stable across
  `T = 20, 40, 80, 120, 200`.  D27(LR2) really does fail on a straddling
  state.  The mechanism is that the backward-evolved packet stays split across
  three window-charge branches (`0.8563 / 0.0170 / 0.1267`) forever; the
  barrier bound state is not the cause.
- **Net:** a real finding about (LR2), reached for a reason that does not
  support it, published at the wrong number, and asserted "on average" in a
  log line where no average is computed.  The finding is fenced at `−3.3592`;
  the gate needs re-anchoring at `t_- ≪ 0` (M2).

---

## 8. Promotion rulings — the cells

Promotion happens on these sentences.  Every symbol used below is bound in
`definitions.md` / `notation.md` or is **defined inline in the cell itself**;
I state the bindings explicitly in §8(E) because the last two promotions in
this campaign carried unbound symbols.  **All four cells are conditional on
the two merge preconditions in §8(E).**

### (A) `ACE-LD-ε` — **YES, at PROVED (conditional)**, with this cell

This replaces the r2 §8(A) sentence, which I withdraw (F1).

> **Adjudicated scoping (verbatim, ace-ld-r3 §8(A)).**  Proved only as the conditional implication: H-MQG(1)--(2), a finite core `K = [ℓ,r]`, a finite window `W = [a,b] ⊇ K` with cut `c_0 ∈ W` and padding `d_W := min(ℓ−a, b−r)+1`, the on-site tail deviations `D_x := S^z_x − s_{γ(x)}` where `s_{γ(x)}` is the D13(a)/H-MQG(2) tail density on the side of `x` (`s_α = +s`, `s_β = −s`), and a unit vector `φ` satisfying **(K-TAIL)** — `|ω_φ(D_xD_{x'})| ≤ C_K²λ̃^{dist(x,K)}λ̃^{dist(x',K)}` for all same-side `x, x' ∉ K`, with constants `C_K < ∞` and `λ̃ ∈ (0,1)` — and **(K-Q)** — `||𝒬_{c_0}φ − q_φφ|| ≤ ε_Q`, where the relative-charge limit **vector** `𝒬_{c_0}φ := lim_n Q̂_{W_n,c_0}φ` exists on every (K-TAIL) state, is exhaustion-independent, and satisfies `𝒬_{c_0} = 2s(X_1 − c_0)` with `X_1` the exactly conserved first-moment wall coordinate frozen in D13(c) — `⟹` `||(Q̂_{W,c_0} − q_φ)φ|| ≤ ε_Q + 2C_Kλ̃^{d_W}/(1−λ̃)`, and hence `dist(q_φ, κ_{W,c_0}+ℤ)` is bounded by the same quantity.  Two forced consequences of (K-TAIL), each proved: **(i)** in the D9(a) kink class it is equivalent to "no charge lies outside the core" (`||𝒬_{c_0}φ − Q̂_{W,c_0}φ|| ≤ 2C_Kλ̃^{d_W}/(1−λ̃)` for every finite `W ⊇ K` with `c_0 ∈ W`), and it forces both tail vacua to have **sharp on-site charge**: `ω_γ((S^z_x − s_γ)²) = 0`, equivalently `ω_γ(Π_x^{(s_γ)}) = 1` for the on-site spectral projection `Π_x^{(m)}` of `S^z_x`, at every site — hence `±s ∈ spec S^z`, so a spin-1 chain with calibration `s = 1/2` admits no (K-TAIL) kink state.  When in addition `s_γ` is a **simple** eigenvalue of `S^z` (as in the standard spin-`S` register `d = 2s+1`) this makes `ω_γ` the `χ=1` fully polarised `S^z`-product state; under H-MQG(1)--(2) alone it does **not**, and the unqualified `χ=1` form is REFUTED (ace-ld-r3 F1).  **(ii)** With `t`-independent `(K, C_K, λ̃)` it is **jointly unsatisfiable with D18(AD3)'s clause that the free leg charge leaves the window** — so no state carrying an escaping leg of nonzero charge satisfies it with `t`-independent constants, `q_L ≠ q_T` is unavailable within one D18 conserved-charge sector, and on states that do satisfy it with `ε_Q = 0` and `t`-uniform data the ordered wall displacement is `δx = 0`.  NOT claimed: that (AD3-ex-ε) supplies `theory/ansatz-scattering.md` ⟨1⟩7.⟨2⟩2's cross-term step (it does not — the hypothesis fails on that entire class; the r2 claim to the contrary is RETRACTED); the exact fixed-`W` (AD3-ex); D18(AD3)'s weak-\* clause or M-INDEX-spec's reduction clause; the `χ=1` product form of the tail vacua under H-MQG alone; any statement about generic injective-MPS vacua; any infinite-volume proof of (K-TAIL) or (K-Q) on any model; the existence of a sector-wide conserved charge operator (only the limit vector on a (K-TAIL) state is constructed; M-INDEX-LA-strong is REFUTED and is not contradicted, its refuting state having polynomially decaying deviations and lying outside the (K-TAIL) class; M-INDEX-LA-folium, the infinite-volume route to (K-Q)'s `t`-uniformity, is CONJECTURE).  The hypothesis class is inhabited: D16's exact zero-energy sector states satisfy (K-Q) exactly and (K-TAIL) at rate `λ̃ = q = Δ−√(Δ²−1)` — independently verified by full-`2^L` exact diagonalisation at `L = 12`, `||D_xφ|| = 4.356e-02, 9.092e-03, 1.898e-03, 3.960e-04, 8.266e-05` with per-site ratios `0.20871` on both sides and `C_K = 0.2087`, in the ℤ₂-image of D13(a)'s orientation.

- **status:** `**PROVED** (conditional)`
- **depends on:** `D13, D26, M-INDEX-fin`
- **proved in:** `theory/ace-ld.md ⟨1⟩4`
- **tested in:** `theory/checks/ace_ld_check.py LD-C7 (green exit 0; --red exit 1, RED-OK 21/21, exit paths tabulated in the shard §5 and re-run independently in ace-ld-r3.md n3).  Gates (b)--(c) certify the conclusion's λ̃^{d_W} rate (defects 4.45e-02 … 4.05e-04, ratios 0.2089/0.2087/0.2083 against q = 0.208712); gate (e) certifies the HYPOTHESIS (K-TAIL) itself site-by-site, and by Cauchy--Schwarz on the self-adjoint D_x the on-site clause is equivalent to the full same-side clause, so (e) certifies (K-TAIL) in full (ace-ld-r3.md n1).  No gate bears on (K-Q), on the infinite-volume statement, or on the sharp-charge corollary, which is exact algebra.`

### (B) `ACE-LD-obst′` — **YES, as a negative row, at PROVED (conditional)**, with this cell

> Under H-MQG(1)--(3), D26(INT), and the D27 setting (a D17 vector `Ψ`, a cut `c_0`, a padded exhaustion `W_m = [a_m,b_m] ↑ ℤ` containing `c_0`) with D27(LR1)--(LR2) but **not** D27(LR3), assume **(M-ESC)**: `θ_{tr} := liminf_m |ω^+_{W_m}(𝔛_{W_m}) − ω^-_{W_m}(𝔛_{W_m})|/|W_m| > 0`.  Then **(a)** `|Σ_ν ν p_{W_m}(ν)| ≥ 2sθ_{tr}|W_m|(1−o(1)) → ∞`; **(b)** D27(LR3) FAILS: `sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν) = ∞` for every `M`; **(c)** D27's ordered wall expectation `δx` is undefined along that exhaustion, its defining differences diverging linearly at rate `≥ θ_{tr}` per window site.  **Positive form (NOT a contrapositive):** the same step gives directly that on any (LR) state the mean wall transport is uniformly bounded, `sup_m |ω^+_{W_m}(𝔛_{W_m}) − ω^-_{W_m}(𝔛_{W_m})| ≤ (M_0+1)/(2s)`, where `M_0` is any threshold with `sup_m Σ_{|ν|>M_0}(1+|ν|)p_{W_m}(ν) ≤ 1`; in particular `θ_{tr} = 0`.  Disclosure: this is the quantitative form of D27's own existence corollary, and the genuine addition is the `M_0` tightness route — strictly stronger than that corollary, which delivers convergence along the full sequence only under D27's optional convenience clause and otherwise only along an (LR3) subsequence, whereas this bound is a `sup` over **all** `m` with no subsequence and no convenience clause.  Mechanism (mean escape gives `θ_{tr} = p_tr`) uses only the mean tail densities of H-MQG(2)/D13(a): no variance hypothesis, no `(E-TAIL)`, `(V-ch)` or `(V-in)`, no `σ_L ≠ σ_T`, no channel projections, no wave operators, no D28.  The first-moment identity is consumed at the level of `theory/memory-index.md` ⟨1⟩7.⟨2⟩1--⟨2⟩2, whose leaf justifications carry only D27(LR1)--(LR2) and (IDX.1) — not the (LR3)-conditional statement of M-INDEX-spec — so the proof by contradiction against (LR3) is non-circular.  NOT claimed: any statement about D16 or any confined-kink class.  There `θ_{tr} = 0`, but only on named conditionals: every state in the closed span of D16's K1--K2 family is exactly stationary (K1+K2 PROVED; exhaustion of `ker H_kink` by that family is K4, CONJECTURE), and the D17 kink--magnon bound `|δx| ≤ ⟨N_T⟩/s` is M-quant-G's conclusion, which is PROVED **conditional on H-AD-G, i.e. on D18(AD1)--(AD4) for that vector** — open for D16 (bd `tns-d51`; `AD3-ex` is CONJECTURE).  Note that D18(AD3) is jointly unsatisfiable with (K-TAIL) (row ACE-LD-eps), so this `θ_{tr} = 0` fence and the ε-theorem concern **disjoint** state classes: a kink--magnon D17 packet under H-AD-G, versus a magnon-free (K-TAIL) sector state.  LD-C7(a) certifies only the 13 sector ground energies at `L = 12`.  The bd `tns-xf4` lane is NOT pre-empted.  Also NOT claimed: any statement about D28's packet class as such (D28(4) constrains only `v_M − v_K`, and D28's class contains `θ_{tr} = 0` members); mass-defectiveness of weak limits (first-moment divergence only); the two-atom law as a theorem (numerically exhibited only).  **No model or state realising `(M-ESC)` is exhibited anywhere in this corpus** — independently confirmed by the parallel lane (`theory/verdicts/lr-d16-r1.md` M2(b)1, `theory/verdicts/lr-d16-r2.md` M4(b)3) — so this row constrains a hypothesis class, and until a witness exists it makes no clause of any class theorem necessary.

- **status:** `**PROVED** (conditional)`
- **depends on:** `D13, D17, D26, D27, M-INDEX-fin`
- **proved in:** `theory/ace-ld.md ⟨1⟩5`
- **tested in:** `theory/checks/ace_ld_check.py LD-C5 — incoming concentration ≤ 3.2e-6 at every window and the exact two-atom TPM support {ν = 0, ν = −|W|} including the ν = 0 atom, with weights matching the independently measured |r|² = 0.2704, |t|² = 0.7296, on a one-particle barrier model; its identity and tail-floor gates are disclosed consequences of those facts, not independent evidence.  LD-C6 — kink+magnon bounded-transport contrast on the D16 battery at the fixed protocol time t_+ = 4 (support: mass at |ν| > 3 below 9.1e-13; first moment ≤ 0.453).  Caveats recorded per ace-ld-r3.md M3: LD-C6's first-moment gate is reached by no registered mutation (the support gate shadows it) and its threshold 1.0 is tuned to t_+ = 4 — the same green model at t_+ = 20 gives 1.0712 and the gate fires.  **Neither certificate exhibits an (M-ESC) state, and no gate bears on claims (a)--(c), which are proved, not tested.**`

### (C) `LD-ID` — **YES, as its own row, at PROVED**, with this cell

> Under H-MQG(1)--(2), for every finite window `W = [a,b]` with `c_0 ∈ W`, and with the step density `s_{γ_{c_0}}(x) := +s` for `x ≤ c_0` and `−s` for `x > c_0`: `Q̂_{W,c_0} = Σ_{x∈W}(S^z_x − s_{γ_{c_0}}(x))` **exactly** — no offset and no factor.  Consequently, on any state on which the increasing-window limit exists — in particular on every (K-TAIL) state of row ACE-LD-eps, where `𝒬_{c_0}φ := lim_n Q̂_{W_n,c_0}φ` exists and is exhaustion-independent — `𝒬_{c_0} = Σ_{x∈ℤ}(S^z_x − s_{γ_{c_0}}(x)) = 2s(X_1 − c_0)`: the relative window charge is **not a new object** but the vector-valued lift of D13(c)'s first-moment wall coordinate `X_1`, which D13(c)'s trap paragraph records as exactly conserved.  Two corollaries, each on its own named hypotheses.  **(i)** If `Ψ_t` carries an outgoing free leg of charge `q_leg ≠ 0` that has left `W` in the sense of D18(AD3), then `||𝒬_{c_0}Ψ_t − Q̂_{W,c_0}Ψ_t|| ≥ |Σ_{x∉W} ω_{Ψ_t}(D_x)| → |q_leg|`, while (K-TAIL) with `t`-independent `(K, C_K, λ̃)` bounds the same quantity by `2C_Kλ̃^{d_W}/(1−λ̃)` uniformly in `t`; choosing `d_W` with `2C_Kλ̃^{d_W}/(1−λ̃) < |q_leg|` is a contradiction.  Hence **no state in D18(AD3)'s escaping-leg class satisfies (K-TAIL) with `t`-independent constants**, and `q_L ≠ q_T` is unavailable within one D18 conserved-charge sector.  **(ii)** Under (K-Q) with `ε_Q = 0` and `t`-uniform (K-TAIL) data, `q_φ` is a `t`-independent eigenvalue of the conserved `𝒬_{c_0}`, and D27's ordered wall expectation obeys `|δx| ≤ s^{-1} lim_m 2C_Kλ̃^{d_{W_m}}/(1−λ̃) = 0`: on that class the ordered memory is exactly zero — D13(c)'s trap in windowed dress.  The window-charge identity is unconditional under H-MQG(1)--(2); the `𝒬_{c_0}` identification additionally requires the increasing-window limit to exist; (i) additionally requires D18(AD3) and `t`-independent (K-TAIL) constants; (ii) additionally requires (K-Q) at `ε_Q = 0`, `t`-uniform data, and D27's definition of `δx`.  NOT claimed: that (i) or (ii) holds outside those hypotheses; which regime any given model occupies; the existence of `𝒬_{c_0}` as a sector-wide operator — only the limit VECTOR on a (K-TAIL) state is constructed, so M-INDEX-LA-strong (REFUTED) is respected and not contradicted, its refuting state having polynomially decaying deviations and lying outside the (K-TAIL) class.

- **status:** `**PROVED**` (the identity unconditionally; corollaries (i),(ii) conditional exactly as stated in the cell)
- **depends on:** `D13, D18, D27, M-INDEX-fin`
- **proved in:** `theory/ace-ld.md ⟨1⟩4.⟨2⟩7`
- **tested in:** `No gate is required: the identity is exact algebra.  Independently re-verified in ace-ld-r3.md §0(i) on all 2^12 basis states of the D16 battery over six windows (max|LHS−RHS| = 0.000e+00), in ace-ld-r2.md §0(i) symbolically and on a 201-site lattice, and reached independently by the parallel lane (theory/verdicts/lr-d16-r1.md §2 item 1).  Corollary (i)'s quantitative witness re-measured in ace-ld-r3.md M1(b): ||(Q̂_{W'}−Q̂_W)φ|| = 2s at every padding for an escaped leg inside the annulus.`

### (D) `ACE-LD-χ` — **NO, not at the claimed strength.**  A corrected row may enter, under a different id

The `χ=1` statement may **not** enter `claims/CLAIMS.md` in any form (F1).
What may enter, at **PROVED**, is the following row under the id
**`ACE-LD-sharp`** — the id `ACE-LD-χ` should not be reused, because the
corrected statement no longer says anything about `χ`:

> Under H-MQG(1)--(2), let `φ` be a unit vector whose state `ω_φ` lies in the D9(a) kink sector `𝒦_{αβ}` and satisfies **(K-TAIL)** with core `K` and constants `C_K, λ̃` (row ACE-LD-eps).  Then both tail vacua have **sharp on-site charge**: for `γ ∈ {α, β}` and every site `x`, `ω_γ((S^z_x − s_γ)²) = 0`, equivalently `ω_γ(Π_x^{(s_γ)}) = 1` where `Π_x^{(m)}` is the on-site spectral projection of `S^z_x` at eigenvalue `m`.  Hence the tail density is an on-site **eigenvalue**: `s_α = +s ∈ spec S^z` and `s_β = −s ∈ spec S^z`.  Proof inputs, all named: D9(a) supplies the weak-\* tail relaxation `ω_φ(τ_x(O)) → ω_γ(O)` for `O ∈ 𝔄_loc` (no extra relaxation hypothesis is needed); (K-TAIL) at `x = x'` drives `ω_φ(D_x²) ≤ C_K²λ̃^{2dist(x,K)} → 0`; Cauchy--Schwarz on `(S^z_x − s_γ)` pins the on-site spectral weights; D2(a) gives translation invariance of `ω_γ`.  **Concrete corollary, by arithmetic alone: a spin-1 chain with calibration `s = 1/2` admits NO (K-TAIL) kink state, since `±1/2 ∉ spec S^z = {−1, 0, 1}`.**  Sharp on-site charge means zero on-site charge variance and therefore excludes every vacuum with nonzero on-site charge variance, in particular generic injective-MPS vacua — which is the scope boundary of row ACE-LD-eps.  NOT claimed: that the tail vacua are `χ=1` fully polarised `S^z`-product states.  That stronger form needs `s_γ` to be a **simple** eigenvalue of `S^z` — true in the standard spin-`S` register `d = 2s+1`, and true in D16, but not implied by H-MQG(1)--(2), D2(a) or D26(INT), all of which admit degenerate on-site charge eigenspaces (`notation.md`'s `d = 2s+1` gloss is explicitly fenced as the fully polarised special case and not a constraint).  Under H-MQG(1)--(2) alone the `χ=1` form is **REFUTED**: with on-site space `ℂ² ⊗ ℂ³` and `S^z := σ^z/2 ⊗ 𝟙_3` (so `spec S^z = {±1/2}`, each of multiplicity 3, and `e^{2πiS^z} = −𝟙`, so D26(INT) holds with `κ = 1/2`), the vacua `ω_α = ⊗_x(|↑⟩⟨↑| ⊗ ϱ_{AKLT})` and `ω_β = ⊗_x(|↓⟩⟨↓| ⊗ ϱ_{AKLT})` are injective MPS of bond dimension `χ = 2` (bond Schmidt spectrum `(1/2, 1/2)`, transfer gap `1/3`), covariant for `G = U(1) ⋊ ℤ₂` with `ω_α(S^z) = +1/2 = s = −ω_β(S^z)`; the sharp domain wall in the `ℂ²` factor lies in `𝒦_{αβ}` and has `D_xφ = 0` at every site, so it satisfies (K-TAIL) with `C_K = 0` while its tail vacua are not product states (ace-ld-r3 F1).

- **status:** `**PROVED**`
- **depends on:** `D2(a), D9(a), D13, D26`
- **proved in:** `theory/ace-ld.md ⟨1⟩4.⟨2⟩9(b), once ⟨3⟩3's χ=1 clause is replaced by the sharp-charge clause per ace-ld-r3 F1`
- **tested in:** `theory/checks/ace_ld_check.py LD-C7(e) certifies the HYPOTHESIS (K-TAIL) on the D16 instance (||D_xφ|| per-site ratios 0.20871 on both sides, C_K = 0.209, red-armed by --red-c7-orientation at C_K = 2525); the conclusion is exact algebra and needs no gate.  The refuting counterexample to the χ=1 form is verified numerically in ace-ld-r3.md F1(b).`

### (E) Merge preconditions and symbol bindings (read before applying any cell)

**Precondition 1 — F1 must be applied to the shard in the same commit.**  Cell
(A) states the sharp-charge form; `theory/ace-ld.md` §0 (twice), ⟨2⟩9(a),
⟨2⟩9(b)⟨3⟩3 and HONEST STATUS still say `χ=1`.  Merging (A) without the F1
repair puts the row and the shard out of lockstep, which is the defect this
method exists to catch.

**Precondition 2 — MP-4 must merge with, or before, cells (A)--(D).**  The
symbols `𝒬_{c_0}`, `(K-TAIL)`, `(K-Q)`, `(M-ESC)` and `θ_{tr}` are **not**
currently in `notation.md`; MP-4 is the row that binds them.  The cells define
each inline as well, so they are self-contained if read alone, but L4 requires
the single-source entries.  MP-4 is otherwise correct as drafted (m3 applied,
`θ_{tr}` renamed with the `notation.md` line-271 twist-variable overload
flagged) — **MERGE it**.

**Symbol bindings, checked one by one.**  Bound already: `S^z` (D26,
`notation.md` line 208); `s`, `s_α = +s`, `s_β = −s` (H-MQG(2),
`notation.md` line 208, `definitions.md` D13 preamble); `𝔛_W`
(`notation.md` line 209, D13(a)); `δx` (`notation.md` line 210, D13(a));
`X_1` (`notation.md` line 211, D13(c)); `Q̂_{W,c_0}` (`notation.md` line 267,
D27); `κ_{W,c_0}` (`notation.md` line 270, M-INDEX-fin's adjudicated cell);
`λ̃` (`notation.md` line 65, D1(c)); `𝒦_{αβ}`, `ω_α`, `ω_β`, `τ_x`, `𝔄_loc`
(D9(a), D2(a)); `p_{W_m}(ν)`, `ω^±_{W_m}`, `𝒟_{W,t_-}` (D27); `N_T`, `⟨N_T⟩`
(D14, D18(AD2)); `Δ`, `q`, `H_kink` (D16); `χ` (D1, D2(a)); `spec S^z`,
`κ` (D26); `H-MQG(1)--(3)` (`theory/memory-quantization-general.md` ASSUME,
referenced from `definitions.md` D28's preamble — the same binding the PROVED
`M-INDEX-spec` and `AC-EX` cells already use).  Defined inline in the cells
because they have no single-source entry: `K = [ℓ,r]`, `d_W`, `D_x`, `C_K`,
`ε_Q`, `q_φ`, `M_0`, `Π_x^{(m)}`, `ϱ_{AKLT}`, `S_{NR}`.  Bound by MP-4 once it
merges: `𝒬_{c_0}`, `(K-TAIL)`, `(K-Q)`, `(M-ESC)`, `θ_{tr}`.  **Every D-number
cited in the four cells resolves: D2(a), D9(a), D13(a),(c), D14, D16, D17,
D18(AD1)--(AD4), D26, D27, D28(4).  I checked each against
`definitions.md`.**

---

## 9. Ruling on MP-1 through MP-6

- **MP-1 row `ACE-LD-abs`** — **MERGE as written.**  Unchanged since r2's
  approval; ⟨1⟩1--⟨1⟩3 fenced twice; no depends-on is correct (r1 m5).
- **MP-1 row `ACE-LD-eps`** — **MERGE with cell §8(A) substituted.**  The
  drafted row is the r2 §8(A) sentence verbatim, which is exactly right of it
  — but that sentence contains the `χ=1` clause I now withdraw.  Subject to
  Precondition 1.
- **MP-1 row `ACE-LD-obst-prime`** — **MERGE with cell §8(B) substituted**
  (m3's condition named, m4's sub-step qualification added, the LD-C6 caveats
  of M3 in the tested-in cell).
- **MP-2** — **MERGE as written.**  M6(c) is applied verbatim, `AD3-ex`
  correctly stays CONJECTURE, "not refuted, it is unavailable" is the right
  verdict, and the §8(E) regime split by escaped charge is carried faithfully.
  This is the cleanest of the six.
- **MP-3** — **HOLD.**  (i), (iii), (iv) and the `ν`-orientation flag are
  sound and may merge.  Clause (ii)'s LD-MONO sentence must first take M1(c)'s
  quantifier; as drafted it would put into `theory/ansatz-scattering.md` a
  statement the same shard refutes at ⟨1⟩4.⟨2⟩7 ⟨3⟩3.  The withdrawal of the
  r2 clause (ii) is correct and complete and must not be reintroduced.
- **MP-4** — **MERGE**, and it is a **precondition** of MP-1 (§8(E)).  m3 and
  n2 are correctly applied.
- **MP-5** — **ENDORSE**, third time.  1447 lines against a 200--500 band; the
  hypothesis sets of ⟨1⟩4 and ⟨1⟩5 are disjoint; the split is overdue and is
  the single highest-value structural action left in this lane.
- **MP-6** — **MERGE with m5's re-citation.**  The composition
  `(M-ESC) ⟹ (NR) fails` is correct and correctly attributed to the
  composition of the two critic passes rather than to this shard.  But
  `theory/verdicts/lr-d16-r2.md` has superseded r1, `(NR)` is now the repaired
  two-clause form, and `theory/lr-d16.md` ⟨1⟩5.⟨2⟩7 THEOREM (LRD-3) now states
  `(NR) ⟹ D27(LR3)` outright — so the composition follows **directly** from
  (LRD-3) and needs no appeal to ⟨1⟩5.⟨2⟩4's monotonicity remark.  Re-cite,
  and carry MP-1's no-witness disclosure into MP-6 as well, since lr-d16-r2
  M4(b)3 rules that a conditional with an empty antecedent makes no clause
  necessary.

---

## 10. Objection ledger

| id | severity | one line |
|---|---|---|
| F1 | **FATAL** | ACE-LD-χ's `χ=1` clause is FALSE — (K-TAIL) forces sharp on-site charge, and `χ=1` needs `s_γ` SIMPLE in `spec S^z`, which no hypothesis supplies; counterexample `ℂ²⊗ℂ³`, `S^z = σ^z/2⊗𝟙_3`, `|↑⟩⊗AKLT` vacua at `χ=2` with `D_xφ ≡ 0`.  **Inherited from my own r2 M1(c)/§5 item 10/§8(A)** |
| M1 | MAJOR | MP-3's LD-MONO sentence drops "beyond the outer window" and is refuted by the shard's own LD-ID ⟨3⟩3: with the leg in the annulus, `‖(Q̂_{W'}−Q̂_W)φ‖ = 2s = 1.0000` against an asserted bound down to `4.25e-22` |
| M2 | MAJOR | LD-C5b measures the LR2 defect at `t_- = 0` (`6.083`), not D27(LR2)'s double-Cesàro average (`−3.3592`); the same straddling packet at `V_0 = 0` gives `−8.3868` at `t_-=0`, PASSES the gate, and satisfies LR2 exactly (`−2.1e-14`).  The finding is nonetheless TRUE and is fenced at `−3.3592` |
| M3 | MAJOR | §5's unreached list stops three evidence-carrying gates early (LD-C6 first moment, LD-C7(e) ratio — both shadowed, both shown live on a copy); and `C6_MOM_BOUND = 1.0` is time-tuned — the GREEN model fires it at `t_+ = 20` with `1.0712` |
| m1 | MINOR | LD-ID's ASSUME covers ⟨3⟩1 only; HONEST STATUS files the whole theorem as unconditional |
| m2 | MINOR | L6b: ⟨3⟩3's `≥ |q_leg| − o(1)` has no displayed derivation |
| m3 | MINOR | the `θ_{tr}=0` fence cites M-quant-G without naming H-AD-G, the very hypothesis LD-ID ⟨3⟩3 shows incompatible with (K-TAIL) |
| m4 | MINOR | L5: MI ⟨1⟩7.⟨2⟩1--⟨2⟩2 sits in M-INDEX-spec's range, not M-INDEX-fin's; the register note needs the sub-step qualification |
| m5 | MINOR | MP-6 cites lr-d16-r1 (superseded); the composition now follows directly from the repaired THEOREM (LRD-3) |
| m6 | MINOR | the eps row's "no state carrying an escaping leg satisfies it" omits "with `t`-independent constants" |
| m7 | MINOR | HONEST STATUS says "~1200 lines"; the file is 1447 |
| m8 | MINOR | the checker docstring advertises `--table`; the flag does not exist |
| n1 | NOTE | (K-TAIL)'s off-diagonal clause is EQUIVALENT to its on-site clause (Cauchy--Schwarz; measured ratio maxes at `1.0000` on the diagonal) — so LD-C7(e) certifies it in full and ⟨2⟩2(i) needs only the triangle inequality |
| n2 | NOTE | the `M_0` addition is genuine and understated: D27's corollary needs the convenience clause for a full-sequence statement; ⟨2⟩3 needs neither it nor a subsequence |
| n3 | NOTE | green exit 0 (27.8 s), `--red` exit 1 RED-OK 21/21 (81.6 s); all 21 exit paths and every quoted digit reproduced; spec/code lockstep exact; no bare `assert` |
| n4 | NOTE | credit: `--red-c6-static` turns the r2 tautology model into a detected mutant (`1−p_0 = −2.220e-16`) |
| n5 | NOTE | credit: the corrected `c1-leak` registration matches measurement, and recording that the first red run exited 2 is the right discipline |
| n6 | NOTE | credit: the seventh no-op was correctly refused — `Σνp ≡ ⟨Q̂⟩_{t_-} − ⟨𝒟_{t_-}(Q̂(t_+))⟩` is an identity, confirmed algebraically and numerically (`6.0832` both ways) |

---

FAIL(F1, M1, M2, M3)
