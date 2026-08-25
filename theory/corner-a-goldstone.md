# Corner A — summation by parts, the Goldstone tensor, and the kinematic factor

**Revision r3** (2026-08-25), after verdicts r1 = FAIL(WI,A1,A2,G0) and
[`verdicts/corner-a-r2.md`](verdicts/corner-a-r2.md) = FAIL(A1,A2,G0,B3).
Dispositions: [`corner-a-r1-response.md`](corner-a-r1-response.md),
[`corner-a-r2-response.md`](corner-a-r2-response.md).
Numerics: [`checks/corner_a_check.py`](checks/corner_a_check.py), C0--C11 (ALL PASS).

Proof shard for claim **G0**.  Companion shards:
[`corner-a.md`](corner-a.md) (Lemma IT, **WI**, **A1**),
[`corner-a-kinks.md`](corner-a-kinks.md) (**A2**),
[`corner-a-pitfalls.md`](corner-a-pitfalls.md) (§5).
Definitions D1--D5, D9--D12 of [`definitions.md`](../definitions.md); symbols in
[`notation.md`](../notation.md).  Steps ⟨1⟩1--⟨1⟩4 live in `corner-a.md`;
numbering continues.  Structure per L6b.

**Two r1 claims are retracted here.**  (1) `|Φ_k(𝒩_k(X))⟩ = 0` is *false* as a
finite-window identity — it equals two boundary terms of norm `Θ(1)`; ⟨1⟩5 now
proves the exact identity *with* those terms and names the two limits (D12) in
which they disappear.  (2) G0(e) does **not** imply an Adler zero, a universal
soft coefficient, or oracle O7/O9; that overclaim is removed and replaced by an
explicit list of what Corner C must still supply (⟨1⟩6.⟨2⟩7).

---

## ⟨1⟩5. LEMMA SBP (summation by parts; the exact gauge remainder)

**ASSUME.** ⟨1⟩1; `A_α` injective; `Λ = [a,b]` finite with boundary vectors
`b_l,b_r`; `X ∈ M_χ(ℂ)`; `f : ℤ → ℂ` any profile.  Write `|ψ;X@m⟩` for the
window vector with `X` inserted on bond `(m|m+1)`, `m ∈ {a−1,…,b}` (the two
extreme values being edge bonds, admitted by D1(e)), and
`|ψ((·)@n)⟩` for the window vector with the bracketed tensor at site `n`.

**PROVE.**
(i) *(master identity, exact)*

  `Σ_{n∈Λ} f(n)|ψ((A_αX − XA_α)@n)⟩
     = − Σ_{m=a}^{b−1} (Δf)(m)\,|ψ;X@m⟩ + f(b)|ψ;X@b⟩ − f(a)|ψ;X@(a−1)⟩`,

with `(Δf)(m) := f(m+1) − f(m)`.  The last two terms are the **gauge
remainder** `𝔅_Λ[f,X]`.
(ii) *(null direction, exact)* For `f(n) = e^{ikn}`,

  `|Φ_k^Λ(𝒩_k(X))⟩ = e^{ik(b+1)}|ψ;X@b⟩ − e^{ika}|ψ;X@(a−1)⟩ = 𝔅_Λ[e^{ik·},X]`,

which is **not zero**: for the `χ=2` Pauli tensor at `k=0.37` with generic
boundary vectors, `‖·‖ = 1.771` (check C3b; the r1 critic measured `0.591` with
different boundary data).  r1's "`= 0` identically" is retracted.
(iii) *(uniform bound)* `‖𝔅_Λ[f,X]‖ ≤ 2C_∂‖X‖\max(|f(a)|,|f(b)|)`, with `C_∂`
of D1(e), uniformly in `Λ`.
(iv) *(D12(a): vanishing remainder)* If `f ∈ c_0(ℤ)` then `‖𝔅_Λ‖ → 0` in norm
as `Λ ↗ ℤ`.  This is a statement about the **remainder only**; it does not by
itself make either side a convergent vector.  If moreover `f ∈ ℓ¹ ∩ BV`
(D12(a′)) both sides are absolutely convergent sums of uniformly bounded window
vectors and the identity is remainderless in the limit.  *(r2 asserted the
stronger conclusion for all of `c_0`; since `c_0 ⊄ ℓ¹`, that was
over-quantified — r2 objection 4.)*
(v) *(D12(b): plane waves)* For `f(n) = e^{ikn}`, `‖𝔅_Λ‖ = O(1)` uniformly in
`Λ` by (iii); hence `‖\,|Λ|^{-1/2}|Φ_k^Λ(𝒩_k(X))⟩\,‖ = O(|Λ|^{-1/2}) → 0` and
the gauge identity holds in the δ-normalised topology.  **No claim is made
about the growth of the bulk term**: r2's `Θ(|Λ|^{1/2})` is false — for `χ = 1`,
`A_αX ∝ A_α` and the plane-wave sum is a bounded geometric sum (check **C10**).
The `|Λ|^{-1/2}` conclusion needs only the upper bound (iii).
(vi) *(ranks)* For `α=β`, `rank\,𝒩_k = χ²` for `k ≠ 0` and `rank\,𝒩_0 = χ²−1`:
the rank **drops** by one as `k → 0`.

**⟨2⟩1. PROVE (i).**
**⟨3⟩1.** `Σ_{n∈Λ} f(n)|ψ((A_αX)@n)⟩ = Σ_{n=a}^{b} f(n)|ψ;X@n⟩`, since placing
`A_α^sX` at site `n` is placing `X` on the bond immediately to its right.
Justification: D1(e), D5(a).
**⟨3⟩2.** `Σ_{n∈Λ} f(n)|ψ((XA_α)@n)⟩ = Σ_{n=a}^{b} f(n)|ψ;X@(n−1)⟩
 = Σ_{m=a−1}^{b−1} f(m+1)|ψ;X@m⟩` by the substitution `m = n−1`.  This is a
**finite** relabelling, not a bilateral rearrangement.
Justification: D1(e), reindexing a finite sum.
**⟨3⟩3.** Subtracting, the bonds `m = a,…,b−1` occur in both sums with
coefficients `f(m)` and `f(m+1)`, giving `−(Δf)(m)`; the bond `m = b` occurs
only in ⟨3⟩1 with `f(b)`, and the bond `m = a−1` only in ⟨3⟩2 with `f(a)`.
Justification: ⟨3⟩1--⟨3⟩2.
**⟨3⟩4.** Numerical confirmation to machine precision (`3.1·10^{-17}`) for both
a plane wave and a generic decaying profile.
Justification: check C3.
**⟨3⟩5. QED.**

**⟨2⟩2. PROVE (ii).** Apply ⟨2⟩1 with the substitution `X ↦ X` in the
combination `𝒩_k(X)^s = e^{ik}A_α^sX − XA_α^s`: by ⟨3⟩1--⟨3⟩2 with
`f(n)=e^{ikn}` and `f(m+1) = e^{ik}f(m)`,
`Σ_n f(n)|ψ(𝒩_k(X)@n)⟩ = e^{ik}[Σ_{n=a}^{b} f(n)|ψ;X@n⟩ − Σ_{m=a−1}^{b−1} f(m)|ψ;X@m⟩]
 = e^{ik}[f(b)|ψ;X@b⟩ − f(a−1)|ψ;X@(a−1)⟩]`, which is the displayed expression.
Justification: ⟨2⟩1.⟨3⟩1--⟨3⟩2 and `e^{ik}f(b) = e^{ik(b+1)}`,
`e^{ik}f(a−1) = e^{ika}`.
**⟨3⟩1.** Verified: the momentum sum equals the two boundary terms to
`3.5·10^{-17}` and has norm `1.771 ≠ 0`.
Justification: check C3b.
**⟨3⟩2. QED.**

**⟨2⟩3. PROVE (iii).** Each of the two terms is a single window vector with one
extra insertion of norm `‖X‖`; D1(e) bounds each by `C_∂‖X‖`, uniformly in
`|Λ|`, because the contraction is `(b_l⊗\bar b_l|E^{|Λ|}|b_r⊗\bar b_r)`-type
and `E^m` is power-bounded (D1(c)).
Justification: D1(e), D1(c).  **⟨3⟩1. QED.**

**⟨2⟩4. PROVE (iv).** For `f ∈ c_0`, `max(|f(a)|,|f(b)|) → 0` as `a → −∞`,
`b → +∞`; apply (iii).  Measured with the centred profile `(1+|n−c|)^{-3}`:
`‖𝔅_Λ‖/‖bulk‖ = 3.4·10^{-1}, 5.7·10^{-2}, 8.5·10^{-3}, 1.2·10^{-3}` for
`L = 4,8,16,32` (check **C4**).  For the second clause: each window vector has
norm `≤ C_∂‖X‖` (D1(e)), so `f ∈ ℓ¹` makes the left side and `Δf ∈ ℓ¹` makes
the bulk sum absolutely convergent, uniformly in `Λ`.
Justification: (iii), D1(e), D12(a),(a′), check C4.  **⟨3⟩1. QED.**

**⟨2⟩5. PROVE (v).** For `f(n) = e^{ikn}`, `|f| ≡ 1`, so (iii) gives
`‖𝔅_Λ‖ ≤ 2C_∂‖X‖` uniformly in `Λ`; dividing by `|Λ|^{1/2}` gives the claim.
Measured: `‖𝔅_Λ‖ ∈ [1.31, 2.03]` for `L = 4,…,32` (check **C5**).
Justification: (iii), D12(b).
**⟨3⟩1.** The r2 proof instead argued from a claimed bulk growth
`Θ(|Λ|^{1/2})`.  That claim is **false**: for `χ = 1`, `A_αX ∝ A_α`, so the
plane-wave bulk sum is `(Σ_{n=a}^{b}e^{ikn})·|ψ⟩`, of norm bounded by
`2C_∂/|1−e^{ik}|` for every `Λ` (check **C10**).  The upper bound (iii) alone
suffices and is what is used.
Justification: check C10; r2 objection 4(b), conceded.
**⟨3⟩2. QED.**

**⟨2⟩6. PROVE (vi).**
**⟨3⟩1.** Suppose `e^{ik}A^sX = XA^s` for all `s`, `X ≠ 0`.  Iterating,
`A^{s_1}⋯A^{s_n}X = e^{-ikn}XA^{s_1}⋯A^{s_n}`; for `n ≥ n_0` the products span
`M_χ` (D1(c)), so by linearity `MX = e^{-ikn}XM` for all `M ∈ M_χ`.  Taking
`M = 𝟙` gives `e^{ikn} = 1`; applying this at `n` and `n+1` gives `e^{ik} = 1`,
i.e. `k = 0`.  So `𝒩_k` is injective for `k ≠ 0`.
Justification: D1(c) and linearity.
**⟨3⟩2.** For `k = 0`, `𝒩_0(X) = 0` iff `X` commutes with every `A^s`, iff (by
D1(c)) with all of `M_χ(ℂ)`, iff `X ∈ ℂ𝟙`.  So `rank\,𝒩_0 = χ²−1`.
Justification: D1(c).
**⟨3⟩3.** Hence the rank *drops* from `χ²` to `χ²−1` in the limit `k → 0`
(r1's wording had the direction ambiguous).  Confirmed for `χ=2`:
`rank\,𝒩_{0.37} = 4`, `rank\,𝒩_0 = 3`.
Justification: ⟨3⟩1--⟨3⟩2; r1 critic's spot check, objection 16.
**⟨3⟩4. Remark.** The factor `(1−e^{ik})` of G0(c) follows *algebraically* from
comparing `𝒩_0(X)` with `𝒩_k(X)` (⟨1⟩6.⟨2⟩3); it is **not** caused by, nor
derived from, this rank discontinuity.  r1 suggested otherwise.
**⟨3⟩5. QED.**

**⟨2⟩7. QED.** □

---

## ⟨1⟩6. THEOREM G0 (Goldstone tensor: pure gauge ⟺ unbroken; the kinematic
## factor `1−e^{ik}`; the lattice continuity equation)

**ASSUME.** ⟨1⟩1--⟨1⟩3, ⟨1⟩5, hypotheses (S) and (H4); `ξ ∈ 𝔤`; `B_G(ξ)` of
D11(a).

**PROVE.**
(a) *(exact form on unbroken directions)* For `ξ ∈ 𝔥_α`,
`B_G(ξ) = A_αX_α(ξ) − X_α(ξ)A_α + i\,θ'_α(ξ)A_α`, and after normal ordering
(⟨1⟩2(iii)) the last term is absent: `B_G(ξ) = 𝒩_0(X_α(ξ))`.
(b) *(the dichotomy)* `B_G(ξ) ∈ ran\,𝒩_0 + ℂA_α` **iff** `ξ ∈ 𝔥_α`.
**Wording (r1 correction):** for a broken direction it is **not** the case that
"(IT) fails" — D2(b) gives (IT) for every `g`, with target `A_{g·α}`.  What
fails is the **same-vacuum return** `g·α = α`, so `B_G(ξ)` is a tangent to the
vacuum manifold rather than to the gauge orbit.
(c) *(`k`-dependence, with the limit named)* For `ξ ∈ 𝔥_α`, normal ordered, and
any `k`, `B_G(ξ) = 𝒩_k(X_α(ξ)) + (1−e^{ik})A_αX_α(ξ)`, hence on a finite window
`Λ = [a,b]` the **exact** identity is
  `|Φ_k^Λ(B_G(ξ))⟩ = (1−e^{ik})Σ_{m=a}^{b} e^{ikm}|ψ;X@m⟩
      + e^{ik(b+1)}|ψ;X@b⟩ − e^{ika}|ψ;X@(a−1)⟩`,
equivalently, combining the two right-edge coefficients,
  `|Φ_k^Λ(B_G(ξ))⟩ = (1−e^{ik})Σ_{m=a}^{b−1} e^{ikm}|ψ;X@m⟩
      + e^{ikb}|ψ;X@b⟩ − e^{ika}|ψ;X@(a−1)⟩`,
with `X := X_α(ξ)`.
**r2 correction (objection 3, conceded).** r2 displayed the bulk sum truncated
at `b−1` *while keeping the uncombined coefficient* `e^{ik(b+1)}`, thereby
omitting `(1−e^{ik})e^{ikb}|ψ;X@b⟩`.  Independently measured discrepancy
`0.4505862126399518`, exactly the norm of the omitted term; both corrected forms
above agree with the left-hand side to `5.9·10^{-17}` (check **C9**).
The clean form `|Φ_k(B_G(ξ))⟩ = (1−e^{ik})|Φ_k(A_αX_α(ξ))⟩` is recovered only
in the D12(b) δ-normalised sense (the two edge terms are `O(1)`, hence
`O(|Λ|^{-1/2})` after normalisation).  For a decaying profile the correct
statement is the real-space SBP identity of ⟨1⟩5(i) with `f ∈ ℓ¹ ∩ BV`
(D12(a′)), **not** this fixed-`k` equation — a plane wave is not in `c_0`
(r2 objection 4).
(d) *(lattice Noether / the bond potential)* Exactly, on the vacuum, with no
limit and no boundary term,
`q_x(ξ)▹ω_α = (𝒥_{x|x+1}(ξ) − 𝒥_{x−1|x}(ξ))▹ω_α` for `ξ ∈ 𝔥_α`, normal
ordered: the *physical* charge density acting on the vacuum is the lattice
divergence of the *virtual* bond quantity `𝒥` (D10(d)).
(e) *(continuity equation, finite range)* Under (H4) with range `R_h`, using the
**cut current** `j_{m|m+1}(ξ) := −[H, Σ_{y≤m}q_y(ξ)] ∈ 𝔄_loc` (D10(a)):
`[H, q_x(ξ)] = j_{x−1|x}(ξ) − j_{x|x+1}(ξ)`, and for every `f ∈ 𝔉_c(ξ)`
  `[H, Q[f;ξ]] = Σ_x (f(x+1) − f(x))\,j_{x|x+1}(ξ)`,
whence, in the wave-packet sense of D3(a), `[H,Q_k(ξ)] = (e^{ik}−1)J_k(ξ)`.
**Scope (r1 correction):** r1 proved this only for nearest neighbours while
quantifying over finite range; the cut current repairs the gap.
**Status of the factor (r1 correction):** `(e^{ik}−1)` is a *kinematic* factor
coming from the profile alone.  It is **not** a soft factor, implies **no**
Adler zero and **no** universality, and does **not** rederive O7/O9 — see
⟨2⟩7 and corner-a-pitfalls.md §5.2(iv).

**⟨2⟩1. PROVE (a).** Differentiate (IT) at `g = exp(εξ)`, `ε=0`, with
`ξ ∈ 𝔥_α` so `g·α = α`, using `V_α(e) = 𝟙`:
`d/dε[e^{iθ_α}V_α^{-1}A_αV_α] = iθ'_α(ξ)A_α − X_α(ξ)A_α + A_αX_α(ξ)`.
The left side is `B_G(ξ)` by D11(a).  Normal ordering sets `θ_α ≡ 0`.
Confirmed numerically for the `χ=2` Pauli tensor with `K = −iZ/2`:
`max_s ‖B_G^s − (A^sK − KA^s)‖ = 0`.
Justification: D2(b), D2(e), D11(a), ⟨1⟩2(iii), product rule; r1 critic's spot
check (objection 15).
**⟨3⟩1. QED.**

**⟨2⟩2. PROVE (b).**
**⟨3⟩1.** (⟸) is ⟨2⟩1.
Justification: ⟨2⟩1, `ran\,𝒩_0 = {A_αX − XA_α}`.
**⟨3⟩2.** (⟹) Suppose `B_G(ξ) = A_αX − XA_α + cA_α`.  The map `A ↦ ω_A` is
constant on gauge orbits `A ↦ Y^{-1}AY` and on rays `A ↦ cA` (D1(d)), so its
differential annihilates `ran\,𝒩_0 + ℂA_α`; hence
`d/dε\,ω_{exp(εξ)·α}(O)|_0 = 0` for every `O ∈ 𝔄_loc`.
Justification: D1(d), D11(a).
**⟨3⟩3.** Write `c(ε) := ω_{exp(εξ)·α}`.  By the group law the derivative of
`c` at any `ε_0` is the image of its derivative at `0` under an automorphism;
by ⟨3⟩2 the latter vanishes, so `c' ≡ 0`, and `c` is `C¹` by (S), hence
constant.  The `ω_α` being pairwise distinct (D2(a)), `exp(εξ)·α = α` for all
`ε`, so `ξ ∈ 𝔥_α` — `H_α` closed in compact `G`, hence a Lie subgroup with Lie
algebra `𝔥_α`.
Justification: ⟨3⟩2, D2(a), D2(e), Cartan's closed-subgroup theorem.
**⟨3⟩4.** Both directions confirmed on the two decisive examples: the `χ=2`
Pauli tensor with unbroken adjoint `U(1)` gives `B_G = 𝒩_0(K)` exactly; the
all-up FM tensor with a broken `x`-rotation gives `B_G = (0,i/2)`,
`ran\,𝒩_0 = {0}`, and `min_c‖B_G − cA‖ = 1/2 ≠ 0`.
Justification: r1 critic's spot checks, objection 15.
**⟨3⟩5. QED.**

**⟨2⟩3. PROVE (c).**
**⟨3⟩1.** `𝒩_k(X) = (A_αX − XA_α) + (e^{ik}−1)A_αX`, so
`B_G(ξ) = 𝒩_0(X) = 𝒩_k(X) − (e^{ik}−1)A_αX` with `X = X_α(ξ)`.  Confirmed
exactly: `max_s‖B_G^s − 𝒩_k(X)^s − (1−e^{ik})A^sX‖ = 0` at `k = 0.37`.
Justification: ⟨2⟩1; r1 critic's spot check.
**⟨3⟩2.** Apply `Σ_{n∈Λ}e^{ikn}|ψ(·@n)⟩`.  By ⟨1⟩5.⟨2⟩1.⟨3⟩1, placing `A_α^sX`
at site `n` is placing `X` on bond `n`, so
`Φ_k^Λ(A_αX) = Σ_{m=a}^{b} e^{ikm}|ψ;X@m⟩` — the sum runs to **`b`**, not `b−1`.
By ⟨1⟩5(ii), `Φ_k^Λ(𝒩_k(X)) = e^{ik(b+1)}|ψ;X@b⟩ − e^{ika}|ψ;X@(a−1)⟩`.
Adding gives the first displayed identity.
Justification: ⟨1⟩5(i),(ii).  *(r2 mismatched the two summation ranges; this
step is where the omitted term was lost.)*
**⟨3⟩3.** The second display follows from
`(1−e^{ik})e^{ikb} + e^{ik(b+1)} = e^{ikb}`.
Justification: algebra.
**⟨3⟩4.** Verified: both displays agree with the left-hand side to
`5.9·10^{-17}` and `3.9·10^{-17}`, while the r2 display is off by
`0.4505862126399518`.
Justification: check **C9**.
**⟨3⟩5.** Limits: the two edge terms are bounded uniformly in `Λ` by
⟨1⟩5(iii), so `|Λ|^{-1/2}` kills them (D12(b)); no bulk growth rate is claimed
or needed.  For `f ∈ ℓ¹ ∩ BV` the real-space identity ⟨1⟩5(i) is remainderless
in the limit (D12(a′)).
Justification: ⟨1⟩5(iii),(iv),(v), D12.
**⟨3⟩6. QED.**

**⟨2⟩4. PROVE (d).** Acting with `q_x(ξ)` on the vacuum replaces `A_α` at site
`x` by `B_G(ξ)` (D11(b)); by (a), normal ordered, this is
`A_αX_α(ξ) − X_α(ξ)A_α`, i.e. `X_α(ξ)` on bond `(x|x+1)` minus `X_α(ξ)` on
bond `(x−1|x)`.  This is a single-site statement: no infinite sum, no
reindexing, hence no boundary term — it is unaffected by the Lemma SBP defect.
Justification: D11(a),(b), ⟨2⟩1, D1(e), D10(d).
**⟨3⟩1. Remark.** This is the infinitesimal form of WI, and it is what makes
`𝒥` — a purely virtual, bond-supported object — the lattice analogue of the
gauge potential of docs/framing.md §4, with `q` the field strength.  Summing
`x ∈ R` telescopes back to WI's two boundary insertions (and the boundary terms
that survive there are precisely WI's two insertions, not an error).
**⟨3⟩2. QED.**

**⟨2⟩5. PROVE (e).**
**⟨3⟩1.** `j_{m|m+1}(ξ) := −[H, Σ_{y≤m}q_y(ξ)] = −Σ_x[h_x, Σ_{y≤m}q_y(ξ)]` is a
finite sum: `[h_x, Σ_{y≤m}q_y] = 0` when `supp\,h_x ⊆ {y≤m}` (it equals
`[h_x, Σ_{y∈supp h_x}q_y] = 0` by `G`-invariance) and when
`supp\,h_x ∩ {y≤m} = ∅`; only the `≤ R_h` straddling terms survive.  Hence
`j_{m|m+1}(ξ) ∈ 𝔄_loc`.
Justification: D10(a), (H4).
**⟨3⟩2.** `Σ_{y≤m}q_y − Σ_{y≤m−1}q_y = q_m`, so
`[H,q_m] = [H,Σ_{y≤m}q_y] − [H,Σ_{y≤m−1}q_y] = j_{m−1|m} − j_{m|m+1}`.
Justification: ⟨3⟩1, linearity.  *(For `R_h = 2` this reduces to r1's
nearest-neighbour computation; the general case is objection 19's repair.)*
**⟨3⟩3.** For `f ∈ 𝔉_c(ξ)` (finite sum, so every rearrangement is legitimate),
`[H,Q[f;ξ]] = Σ_x f(x)(j_{x−1|x} − j_{x|x+1}) = Σ_x (f(x+1)−f(x))j_{x|x+1}`.
Justification: ⟨3⟩2 and one Abel summation, finite by D3(a).
**⟨3⟩4.** For `f(x) = e^{ikx}`, `f(x+1)−f(x) = (e^{ik}−1)e^{ikx}`, giving
`[H,Q_k(ξ)] = (e^{ik}−1)J_k(ξ)` as an identity of quadratic forms against wave
packets `φ ∈ C_c^∞`, since the plane wave is not in `𝔉_c(ξ)` (D3(a)).
Justification: ⟨3⟩3, D3(a), D10(c).
**⟨3⟩5. QED.**

**⟨2⟩6. QED.** (a)--(e) are ⟨2⟩1--⟨2⟩5.  □

**⟨2⟩7. Remark (what G0(e) does NOT give — r1 objection 18, conceded in full).**
r1 called `(e^{ik}−1)` "universal" and claimed it forces oracle O7/O9's
hard-independent linear coefficient.  Both claims are withdrawn.
- In a matrix element the identity says only
  `⟨out|[H,Q_k]|in⟩ = (e^{ik}−1)⟨out|J_k|in⟩`.  *All* dependence on `H`, `ξ`,
  the vacuum, and the hard legs sits in `⟨out|J_k|in⟩`.  If
  `⟨out|J_k|in⟩ = C_hard + O(k)` then hard data enters at `O(k)`, not `O(k²)`;
  if `⟨out|J_k|in⟩` has a `1/k` infrared singularity there is no zero at all.
- The factor is convention-dependent: kernel `e^{−ikx}` gives `e^{−ik}−1`, and
  reversing the orientation or sign of the current flips it.  Its
  `H`-independence is the tautology that a discrete difference was factored out
  *after* defining an `H`-dependent current.
- Corner C must supply, and Corner A does not: (i) regularity of
  `⟨out|J_k|in⟩` at `k = 0` on the relevant scattering states; (ii) an
  LSZ/scattering reduction turning the operator identity into a statement about
  amplitudes; (iii) a Ward identity relating `J_0` to the external legs'
  charges; (iv) control of the remainder in a stated norm.
- What *is* rederived is **O1 only**, in the one-magnon sector (⟨1⟩7), where
  the FM current happens to supply a second lattice difference.

**⟨2⟩8. Remark (correction to the brief).** HANDOFF §2 Corner C asserts the
`k=0` Goldstone tensor is pure gauge "with `X = V'(0)`".  By (b) that holds
only along **unbroken** directions, where by (c) it produces no Goldstone
whenever `V_α` acts trivially (e.g. `χ = 1`).  Along a broken direction (IT)
still holds — with target `A_{g·α}` — but the same-vacuum return fails,
`B_G(ξ) ∉ ran\,𝒩_0`, and `|Φ_0(B_G(ξ))⟩ ≠ 0`.  The brief is historical and is
not edited; see corner-a-pitfalls.md Flag 5.

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

**⟨2⟩5. Remark (relation to oracle O7/O9 — r1 overclaim withdrawn).**
r1 stated that O7's hard-independent linear coefficient `2` in
`δ = 2k_s + \cot(k_h/2)k_s² + O(k_s³)` is "exactly the structure forced by"
G0(e).  **It is not forced by anything proved here** (⟨1⟩6.⟨2⟩7).  The honest
statement is a *consistency observation with a stated gap*:

- G0(e) supplies a kinematic prefactor `(e^{ik_s}−1) = ik_s + O(k_s²)`.
- **If** the current matrix element `⟨out|J_{k_s}|in⟩` between the hard legs is
  regular at `k_s = 0` and has a `k_s`-independent leading value, **then** the
  linear coefficient of the connected phase is hard-independent, matching O9.
- Neither hypothesis is established.  Establishing them — plus the LSZ
  reduction — is precisely Corner C's obligation.  Until then the agreement is
  a target, not a derivation, and O7/O9 remain oracle facts that Corner A does
  not reproduce.

Only **O1** is rederived here (⟨2⟩3), and only in the one-magnon sector.

---

## Claim status produced by this shard (r2)

| item | status | where |
|---|---|---|
| **G0(a)**, **G0(b)** — pure gauge at `k=0` **iff** `ξ` unbroken; broken case is failure of *same-vacuum return*, not of (IT) | **PROVED** | ⟨1⟩6.⟨2⟩1--⟨2⟩2 |
| **G0(c)** — exact finite-window identity with **both** edge terms: `(1−e^{ik})Σ_{m=a}^{b−1}e^{ikm}\|ψ;X@m⟩ + e^{ikb}\|ψ;X@b⟩ − e^{ika}\|ψ;X@(a−1)⟩` | **PROVED**.  The clean form `(1−e^{ik})\|Φ_k(A_αX_α(ξ))⟩` holds **only** in the D12(b) δ-normalised sense; for decaying profiles use the real-space SBP identity with `f ∈ ℓ¹∩BV` (D12(a′)).  r2's display, which dropped `(1−e^{ik})e^{ikb}\|ψ;X@b⟩`, is retracted | ⟨1⟩5, ⟨1⟩6.⟨2⟩3, check C9 |
| **G0(d)** — lattice Noether: `q_x ▹ ω_α = (𝒥_{x\|x+1} − 𝒥_{x−1\|x}) ▹ ω_α` | **PROVED** (single site; no limit, no boundary term) | ⟨1⟩6.⟨2⟩4 |
| **G0(e)** — `[H,Q[f;ξ]] = Σ_x(Δf)(x)\,j_{x\|x+1}(ξ)`, finite range, cut current | **PROVED** for the full finite-range class (r1 proved only nearest neighbour) | ⟨1⟩6.⟨2⟩5 |
| G0(e) ⟹ Adler zero / universal soft coefficient / O7 / O9 | **RETRACTED** — see ⟨1⟩6.⟨2⟩7; open for Corner C | — |
| supporting **Lemma SBP** — exact master identity *with* its two boundary terms; (iv) remainder-vanishing for `c_0` and norm convergence for `ℓ¹∩BV`; (v) `‖𝔅_Λ‖ = O(1)` **upper bound only** | **PROVED** (replaces r1's false `\|Φ_k(𝒩_k(X))⟩ = 0`; r2's `Θ(\|Λ\|^{1/2})` bulk claim withdrawn, check C10) | ⟨1⟩5 |
| supporting **Proposition FM** — type-B count `2→1`; `ω(k) = J(1−\cos k)` rederived from G0(e), matching oracle **O1** | **PROVED** | ⟨1⟩7 |
| brief's mechanism ("the `k=0` magnon is pure gauge with `X=V'(0)`") | **CORRECTED** — true only for unbroken directions | ⟨1⟩6.⟨2⟩8 |
