# Corner A — null directions, the Goldstone tensor, and the universal soft factor

Proof shard for claim **G0** of [`claims/CLAIMS.md`](../claims/CLAIMS.md).
Companion shards: [`corner-a.md`](corner-a.md) (setting, Lemma IT, **WI**,
**A1**, and the campaign pitfalls §5) and
[`corner-a-kinks.md`](corner-a-kinks.md) (**A2**).  Split into three shards
per CLAUDE.md L2 (200--500 loc, one lemma-cluster per file); HANDOFF's
suggested two-way split would leave the first shard at ~700 lines.

Definitions D1--D5, D9--D11 of [`definitions.md`](../definitions.md); symbols
in [`notation.md`](../notation.md).  Steps ⟨1⟩1--⟨1⟩4 referenced below live in
[`corner-a.md`](corner-a.md); numbering continues from there.  Structure per
L6b.

---

## ⟨1⟩5. LEMMA N (null directions of the excitation ansatz)

**ASSUME.** ⟨1⟩1; `A_α, A_β` injective; `k ∈ (−π,π]`; `X ∈ M_χ(ℂ)`.

**PROVE.** (i) `|Φ_k(𝒩_k^{αβ}(X); A_α,A_β)⟩ = 0`, where
`𝒩_k^{αβ}(X)^s = e^{ik}A_α^s X − X A_β^s`.
(ii) For `k ≠ 0` and `α=β`, `𝒩_k` is injective, so `dim\,ran\,𝒩_k = χ²`.
(iii) For `k = 0` and `α=β`, `ker\,𝒩_0 = ℂ𝟙`, so `dim\,ran\,𝒩_0 = χ²−1`.
The missing direction is `A_α` itself: `|Φ_0(A_α)⟩` is the (non-normalisable)
vacuum direction `Σ_n Ω_A`, and `|Φ_k(A_α)⟩ = 0` for `k ≠ 0`.

**⟨2⟩1. PROVE (i).** In `|Φ_k(𝒩_k(X))⟩ = Σ_n e^{ikn}[…A_α (e^{ik}A_αX) A_β…]
− Σ_n e^{ikn}[…A_α (XA_β) A_β…]`, the first sum has, at index `n`, a uniform
tensor everywhere with `X` on bond `(n|n+1)` and total coefficient `e^{ik(n+1)}`;
re-indexing `m = n+1` turns it into the second sum term by term.
Justification: D5(a), D5(b), and re-indexing a bilateral sum.
[Ground truth, refs/arxiv-1103.2286: "the choice `B^s = e^{iκ}A^sX − X\tilde A^s`
results in `|Φ_κ(B)⟩ = 0`".]
**⟨3⟩1. QED.**

**⟨2⟩2. PROVE (ii).** Suppose `e^{ik}A^sX = XA^s` for all `s`, `X ≠ 0`.
Iterating, `A^{s_1}\!⋯A^{s_n}X = e^{-ikn}XA^{s_1}\!⋯A^{s_n}`.  For `n ≥ n_0`
the products span `M_χ` (D1(c)); taking the span element `𝟙` gives
`X = e^{-ikn}X`, hence `e^{ikn}=1`; applying this at `n` and `n+1` gives
`e^{ik}=1`, i.e. `k = 0`.
Justification: D1(c) and induction on the (IT)-free algebra.
**⟨3⟩1. QED.**

**⟨2⟩3. PROVE (iii).** For `k=0`, `𝒩_0(X)=0` iff `X` commutes with every
`A^s`, iff (by D1(c), `n ≥ n_0`) `X` commutes with `M_χ(ℂ)`, iff `X ∈ ℂ𝟙`.
`|Φ_0(A_α)⟩ = Σ_n Ω_A` diverges, and for `k ≠ 0`,
`|Φ_k(A_α)⟩ = (Σ_n e^{ikn})Ω_A = 0` as a tempered distribution in `k` away from
`k=0`.
Justification: D1(c), D5(a), and `Σ_n e^{ikn} = 2πδ(k)`.
**⟨3⟩1. QED.**

**⟨2⟩4. QED.** □  [Consistent with refs/arxiv-1103.2286: "For any `κ≠0` … `B`
has `D²` linearly independent zero modes … For `|Ψ(A)⟩=|Ψ(\tilde A)⟩` … there
are only `D²−1` linearly independent zero modes".]

---

## ⟨1⟩6. THEOREM G0 (Goldstone tensor; pure gauge ⟺ unbroken; the universal
## factor `1−e^{ik}`)

**ASSUME.** ⟨1⟩1--⟨1⟩3, ⟨1⟩5, hypotheses (S) and (H4); `ξ ∈ 𝔤`; `B_G(ξ)` of
D11(a).

**PROVE.**
(a) *(exact form on unbroken directions)* For `ξ ∈ 𝔥_α`,
  `B_G(ξ) = A_α X_α(ξ) − X_α(ξ)A_α + θ'_α(ξ)\,i\,A_α`,
and after normal ordering (⟨1⟩2(iii)) the last term is absent:
  `B_G(ξ) = A_α X_α(ξ) − X_α(ξ)A_α = 𝒩_0(X_α(ξ))`.
(b) *(the dichotomy)* `B_G(ξ) ∈ ran\,𝒩_0 + ℂA_α` **iff** `ξ ∈ 𝔥_α`.  Thus
"the `k=0` Goldstone tensor is pure gauge" is true precisely for **unbroken**
directions and **false** for every genuinely broken (Goldstone) direction.
(c) *(`k`-dependence)* For `ξ ∈ 𝔥_α`, normal ordered, and any `k`,
  `B_G(ξ) = 𝒩_k(X_α(ξ)) + (1−e^{ik})A_αX_α(ξ)`,
hence exactly
  `|Φ_k(B_G(ξ))⟩ = (1−e^{ik})\,|Φ_k(A_αX_α(ξ))⟩ = −ik\,|Φ_k(A_αX_α(ξ))⟩ + O(k²)`.
At `k=0` the right-hand side vanishes; the gauge-orbit dimension jumps from
`χ²−1` to `χ²` (Lemma N), and this jump is exactly the factor `(1−e^{ik})`.
(d) *(lattice Noether / the bond potential)* Exactly, on the vacuum,
  `q_x(ξ)▹ω_α = (𝒥_{x|x+1}(ξ) − 𝒥_{x−1|x}(ξ))▹ω_α`  (`ξ ∈ 𝔥_α`, normal ordered),
i.e. the *physical* charge density acting on the vacuum is the lattice
divergence of the *virtual* bond quantity `𝒥` (D10(d)).
(e) *(the soft seed; both cases)* Under (H4), for any `f ∈ 𝔉_c(ξ)`,
  `[H, Q[f;ξ]] = Σ_x (f(x+1)−f(x))\,j_{x,x+1}(ξ)`,
and in the wave-packet sense of D3(a),
  `[H, Q_k(ξ)] = (e^{ik}−1)\,J_k(ξ)`.
The prefactor `(e^{ik}-1) = ik + O(k²)` is **universal**: independent of `H`,
of `ξ`, of the vacuum, and of every other leg's data.  This is the Adler-zero
mechanism that survives symmetry breaking, and the only one that does.

**⟨2⟩1. PROVE (a).** Differentiate (IT) at `g=exp(εξ)`, `ε=0`, with `ξ ∈ 𝔥_α`
so `g·α = α`, using `V_α(e)=𝟙`:
`d/dε[e^{iθ_α}V_α^{-1}A_αV_α] = iθ'_α(ξ)A_α − X_α(ξ)A_α + A_αX_α(ξ)`.
The left side is `B_G(ξ)` by D11(a).  Normal ordering sets `θ_α ≡ 0`.
Justification: D2(b), D2(e), D11(a), ⟨1⟩2(iii), product rule.
**⟨3⟩1. QED.**

**⟨2⟩2. PROVE (b).**

**⟨3⟩1.** (⟸) is ⟨2⟩1.
Justification: ⟨2⟩1 and `ran\,𝒩_0 = {A_αX−XA_α}`.

**⟨3⟩2.** (⟹) Suppose `B_G(ξ) = A_αX − XA_α + cA_α` for some `X ∈ M_χ`,
`c ∈ ℂ`.  Reading this back through D11(a), the one-parameter family
`ε ↦ 𝒰(exp(εξ))A_α` has derivative in the tangent space of the *gauge orbit*
of `A_α` (the `𝒩_0`-directions) plus the scaling direction `A_α`.
Justification: D11(a), D5(b).

**⟨3⟩3.** By D1(d) the map `A ↦ ω_A` is constant on gauge orbits and on rays;
hence `d/dε\,ω_{exp(εξ)·α}(O)|_0 = 0` for every `O ∈ 𝔄_loc`.
Justification: D1(d), the gauge invariance `A^s ↦ Y^{-1}A^sY` and phase
invariance of `ω_A`, and ⟨3⟩2.

**⟨3⟩4.** Write `c(ε) := ω_{exp(εξ)·α}`.  By the group law
`c(ε_0+ε) = c(ε_0) ∘ Ad(U(exp(εξ))^†)` evaluated in the `exp(ε_0ξ)·α` frame, so
the derivative of `c` at any `ε_0` is the image of its derivative at `0` under
an automorphism; by ⟨3⟩3 the latter vanishes, hence `c' ≡ 0` and, `c` being
`C¹` by (S), `c` is constant.  Thus `exp(εξ)·α = α` for all `ε` (the `ω_α` are
pairwise distinct, D2(a)), i.e. `exp(εξ) ⊂ H_α` and `ξ ∈ 𝔥_α` — `H_α` being a
closed subgroup of the compact group `G`, hence a Lie subgroup with Lie algebra
`𝔥_α`.
Justification: ⟨3⟩3, D2(a), D2(e), and Cartan's closed-subgroup theorem.

**⟨3⟩5. QED.**

**⟨2⟩3. PROVE (c).** `𝒩_k(X) = e^{ik}A_αX − XA_α = (A_αX − XA_α) + (e^{ik}−1)A_αX`,
so `B_G(ξ) = 𝒩_0(X_α(ξ)) = 𝒩_k(X_α(ξ)) − (e^{ik}−1)A_αX_α(ξ)`.  Applying
`|Φ_k(·)⟩` and Lemma N(i) kills the `𝒩_k` term.  Expanding `1−e^{ik}` gives the
`O(k)` statement.
Justification: ⟨2⟩1, ⟨1⟩5(i), linearity of `B ↦ |Φ_k(B)⟩` (D5(a)).
**⟨3⟩1.** (Cross-check) The alternative split with `X ↦ e^{-ik}X` gives
`|Φ_k(B_G)⟩ = (e^{-ik}−1)|Φ_k(X_α A_α)⟩`; consistency with the displayed form
requires `|Φ_k(X A_α)⟩ = e^{ik}|Φ_k(A_αX)⟩`, which is the statement that moving
a bond insertion one site to the right multiplies the momentum sum by `e^{ik}`.
Justification: D5(a), re-indexing.
**⟨3⟩2. QED.**

**⟨2⟩4. PROVE (d).** Acting with `q_x(ξ)` on the vacuum replaces `A_α` at site
`x` by `B_G(ξ)` (D11(b)); by (a), normal ordered, this is
`A_αX_α(ξ) − X_α(ξ)A_α`, i.e. `X_α(ξ)` inserted on bond `(x|x+1)` minus
`X_α(ξ)` inserted on bond `(x−1|x)`.
Justification: D11(a), D11(b), ⟨2⟩1, D1(e), D10(d).
**⟨3⟩1. Remark.** This is the infinitesimal form of WI: it is what makes `𝒥` —
a purely virtual, bond-supported object — the lattice analogue of the gauge
potential of docs/framing.md §4, with `q` the field strength.  Summing
`x ∈ R` telescopes back to WI's two boundary insertions.
**⟨3⟩2. QED.**

**⟨2⟩5. PROVE (e).**

**⟨3⟩1.** By (H4), `[h_{x,x+1}, q_x(ξ)+q_{x+1}(ξ)] = 0`, so with
`j_{x,x+1}(ξ) := −[h_{x,x+1},q_x(ξ)]` (D10(a)) also
`j_{x,x+1}(ξ) = [h_{x,x+1},q_{x+1}(ξ)]`.
Justification: D10(a) and (H4).

**⟨3⟩2.** Only `h_{x−1,x}` and `h_{x,x+1}` fail to commute with `q_x(ξ)`, so
`[H,q_x(ξ)] = [h_{x−1,x},q_x(ξ)] + [h_{x,x+1},q_x(ξ)] = j_{x−1,x}(ξ) − j_{x,x+1}(ξ)`.
Justification: ⟨3⟩1, D10(b), locality of `h`.

**⟨3⟩3.** Hence for `f ∈ 𝔉_c(ξ)` (a finite sum, so `Q[f;ξ] ∈ 𝔄_loc` and every
rearrangement is legitimate),
`[H,Q[f;ξ]] = Σ_x f(x)(j_{x−1,x} − j_{x,x+1}) = Σ_x (f(x+1)−f(x)) j_{x,x+1}`.
Justification: ⟨3⟩2 and a single Abel summation, finite by `f ∈ 𝔉_c(ξ)`
(D3(a)).

**⟨3⟩4.** For `f(x)=e^{ikx}`, `f(x+1)−f(x) = (e^{ik}−1)e^{ikx}`, giving
`[H,Q_k(ξ)] = (e^{ik}−1)J_k(ξ)`; this holds as an identity of quadratic forms
against wave packets `φ ∈ C_c^∞`, since the plane wave is not in `𝔉_c(ξ)`
(D3(a)).
Justification: ⟨3⟩3, D3(a), D10(c).

**⟨3⟩5.** The factor `(e^{ik}−1)` came only from the *profile*, not from `H`,
`ξ`, or the state.  Its `O(k)` coefficient is therefore hard-data independent.
Justification: ⟨3⟩4.

**⟨3⟩6. QED.**

**⟨2⟩6. QED.** (a)--(e) are ⟨2⟩1--⟨2⟩5.  □

**⟨2⟩7. Remark (correction to the brief).** HANDOFF §2 Corner C asserts that
the `k=0` Goldstone tensor is pure gauge "with `X = V'(0)`".  By (b) that is
correct only along **unbroken** directions, where by (c) it produces no
Goldstone at all whenever `V_α` acts trivially (e.g. `χ = 1`).  For a genuinely
broken direction (IT) does not hold, `B_G(ξ) ∉ ran\,𝒩_0`, and
`|Φ_0(B_G(ξ))⟩ ≠ 0`.  The universal, symmetry-breaking-proof statement is (e).
This correction is load-bearing for Corner C and is recorded in
[`claims/CLAIMS.md`](../claims/CLAIMS.md).

---

## ⟨1⟩7. PROPOSITION FM (oracle consistency: the isotropic ferromagnet)

**ASSUME.** D6 (`H = Σ_x (J/2)(1−P_{x,x+1})`, `|Ω⟩=|↑↑⋯⟩`, `J>0`);
`G = SU(2)`, `u = ` the spin-`1/2` representation; `A_α^{↑}=1`, `A_α^{↓}=0`,
`χ=1`, so `ω_{A_α}` is the state of `|Ω⟩` and is injective (`E = 1`, `λ_E = 0`).
*Generator convention.* One-parameter subgroups are written in the physicists'
form `exp(iεS^a)`; the corresponding element of `𝔤 = 𝔰𝔲(2)` is `ξ_a := iS^a`,
so `q(ξ_a) = iS^a` is anti-Hermitian as D10 requires.  Write
`|k⟩ := Σ_x e^{ikx}S^-_x|Ω⟩` (D6).

**PROVE.** (i) `H_α = U(1)` (rotations about `z`); `SU(2)` is fully broken to
this `U(1)` in the ferromagnetic ground state.  (ii) `[ω_α] = 0` and the
unbroken `U(1)` produces **no** Goldstone tensor.  (iii) The two broken real
generators produce **one** complex Goldstone tensor (type B):
`B_G(S^y) = i\,B_G(S^x)`.  (iv) `|Φ_k(B_G(S^x))⟩ ∝ |k⟩` is the exact magnon,
and ⟨1⟩6(e) reproduces the oracle dispersion `ω(k)=J(1−\cos k)` of O1.

**⟨2⟩1. PROVE (i)--(ii).** `u(e^{iεS^z})|↑⟩ = e^{iε/2}|↑⟩`, so
`𝒰(e^{iεS^z})A_α = e^{iε/2}A_α`: (IT) holds with `V_α = 1`, `θ_α(ε)=ε/2 ≠ 0`.
Rotations off the `z`-axis map `|↑⟩` to a different unit vector, hence
`A_α` to a different (inequivalent, `χ=1`) tensor: `H_α = U(1)`.
`H²(U(1),U(1)) = 0` and `V_α ≡ 1`, so `[ω_α]=0`; `X_α = 0`, so by ⟨1⟩6(a)
normal-ordered `B_G = 0`.
Justification: D6, D2(a), D2(b), ⟨1⟩6(a).
**⟨3⟩1. Remark.** `θ'_α = 1/2 ≠ 0` is exactly the extensive WI phase
`e^{i|R|θ}` of corner-a.md ⟨1⟩3.⟨2⟩7(b): the naive `S^z` charge does not annihilate the
ferromagnetic vacuum; `ǔ_α` subtracts the vacuum magnetisation density.
**⟨3⟩2. QED.**

**⟨2⟩2. PROVE (iii).** `𝔪_α = span_ℝ{ξ_x, ξ_y}`.  Since `A_α^{↓}=0`, D11(a)
gives `B_G(ξ)^s = Σ_{s'}q(ξ)_{ss'}A_α^{s'} = q(ξ)_{s↑}`; with
`⟨↓|S^x|↑⟩ = 1/2` and `⟨↓|S^y|↑⟩ = i/2`, and `⟨↑|S^{x,y}|↑⟩ = 0`,
  `B_G(ξ_x) = \tfrac{i}{2}(0,1)`,  `B_G(ξ_y) = −\tfrac12(0,1) = i\,B_G(ξ_x)`.
The real 2-dimensional `𝔪_α` therefore maps onto a **1-dimensional complex**
space of Goldstone tensors: two broken generators, one Goldstone mode.  This is
the type-B count of D11(c), derived rather than assumed.
Justification: D6, D11(a), D11(c), and the spin-`1/2` matrix elements.
**⟨3⟩1. Remark.** The complexified statement is cleaner: `S^+` annihilates
`|Ω⟩` site-wise, so the raising direction gives `B_G = 0` identically (it
satisfies (IT) trivially with `V=𝟙, θ=0`), while `S^-` gives the magnon.  The
type-B degeneracy is exactly this splitting of `𝔪_α ⊗ ℂ` into an annihilating
and a creating half.
Justification: `S^+|↑⟩ = 0` and D11(a).
**⟨3⟩2. QED.**

**⟨2⟩3. PROVE (iv).** Take `ξ = ξ_x`, so `q_x(ξ_x)|Ω⟩ = \tfrac{i}{2}S^-_x|Ω⟩`
and hence, by D5(a) and D11(b),
`|Φ_k(B_G(ξ_x))⟩ = Q_k(ξ_x)|Ω⟩ = \tfrac{i}{2}|k⟩` — the exact one-magnon state
of D6.  For the dispersion, `h_{x,x+1}|Ω⟩ = 0` and
`P_{x,x+1}S^-_x|Ω⟩ = S^-_{x+1}|Ω⟩`, so
`h_{x,x+1}S^-_x|Ω⟩ = \tfrac{J}{2}(S^-_x − S^-_{x+1})|Ω⟩`, whence by D10(a)
`j_{x,x+1}(ξ_x)|Ω⟩ = −[h_{x,x+1},q_x(ξ_x)]|Ω⟩ = −\tfrac{iJ}{4}(S^-_x − S^-_{x+1})|Ω⟩`
and, summing with `e^{ikx}` and shifting the second term,
`J_k(ξ_x)|Ω⟩ = −\tfrac{iJ}{4}(1−e^{-ik})\,|k⟩`.
By ⟨1⟩6(e) and `H|Ω⟩ = 0`,
`H\,Q_k(ξ_x)|Ω⟩ = [H,Q_k(ξ_x)]|Ω⟩ = (e^{ik}−1)J_k(ξ_x)|Ω⟩
 = −\tfrac{iJ}{4}(e^{ik}−1)(1−e^{-ik})|k⟩ = \tfrac{i}{2}J(1−\cos k)\,|k⟩`,
i.e. `H|k⟩ = J(1−\cos k)|k⟩`: the common factor `i/2` cancels.
Justification: D6, D5(a), D10(a), D11(b), ⟨1⟩6(e), and
`(e^{ik}−1)(1−e^{-ik}) = 2\cos k − 2`.
**⟨3⟩1.** This equals oracle fact **O1** of [`oracle-bethe.md`](oracle-bethe.md).
Note that the type-B quadratic dispersion `ω ∼ Jk²/2` arises as **two** factors
of `(1−e^{ik})`: one from the modulated profile (⟨1⟩6(e)), one because the
ferromagnetic current is itself a difference of broken charge densities.
Justification: ⟨2⟩3 and O1.
**⟨3⟩2. QED.**

**⟨2⟩4. QED.** □

**⟨2⟩5. Remark (compatibility with the Bethe soft phase).** Oracle **O7**
gives `δ = 2k_s + \cot(k_h/2)k_s² + O(k_s³)`: the linear coefficient is the
hard-data-independent constant `2`, and the first hard invariant appears only
at `O(k_s²)`.  This is exactly the structure forced by ⟨1⟩6(e): the soft
insertion carries the universal prefactor `(e^{ik_s}−1) = ik_s + O(k_s²)` whose
`O(k_s)` coefficient cannot depend on the hard leg, while the leg-dependent
data can only enter at the next order.  The determination of the *value* `2`
requires evaluating `J_{k_s}` between the hard legs and is Corner C's
obligation, not Corner A's.  Corner A asserts only the **structure**
(universal linear prefactor, leg data first at `O(k²)`), and that structure
matches the oracle.

---

## Claim status produced by this shard

| claim | status | where |
|---|---|---|
| **G0** | **PROVED**, in a corrected form: `B_G(ξ)` is pure gauge at `k=0` **iff** `ξ` is unbroken (⟨1⟩6(b)); for unbroken `ξ` the exact `k`-dependence is `\|Φ_k(B_G)⟩ = (1−e^{ik})\|Φ_k(A_αX_α(ξ))⟩` (⟨1⟩6(c)); the universal, breaking-proof soft prefactor is `(e^{ik}−1)` in `[H,Q_k] = (e^{ik}−1)J_k` (⟨1⟩6(e)) | ⟨1⟩6 |
| supporting **Lemma N** (null directions, rank `χ²` vs `χ²−1`) | **PROVED** | ⟨1⟩5 |
| supporting **Proposition FM** (type-B count `2→1`; `ω(k)=J(1−cos k)` re-derived from G0(e), matching oracle **O1**) | **PROVED** | ⟨1⟩7 |
| brief's mechanism paragraph ("the `k=0` magnon is pure gauge with `X=V'(0)`") | **CORRECTED** — true only for unbroken directions; false for the Goldstone direction | ⟨1⟩6.⟨2⟩7 |
