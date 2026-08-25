# Corner A — the lattice asymptotic symmetry: Ward identity and charge algebra

Proof shard for claims **WI** and **A1** of [`claims/CLAIMS.md`](../claims/CLAIMS.md),
plus the campaign-level pitfalls §5.  Companion shards (L2: 200--500 loc, one
lemma-cluster per file):
[`corner-a-goldstone.md`](corner-a-goldstone.md) — Lemma N, **G0**, and the
ferromagnet/oracle consistency check;
[`corner-a-kinks.md`](corner-a-kinks.md) — the broken case **A2**.
HANDOFF suggested a two-way split; three shards were needed to respect L2.
All symbols are those of
[`notation.md`](../notation.md); all definitions are D1--D5, D9--D11 of
[`definitions.md`](../definitions.md) and are not restated.  Literature enters
only through the quotations recorded in D2 and D5, taken from the local TeX
under `refs/` (L3).  Structure follows L6b.

Register note: every step below is either (i) an exact algebraic identity
between finite window vectors (D1(e)), (ii) a finite-dimensional linear-algebra
statement about `M_χ(ℂ)`, or (iii) a weak-* limit with an explicitly exhibited
rate `λ_E`.  No manipulation of an infinite-chain wave function occurs.

---

## ⟨1⟩1. Standing hypotheses

**⟨2⟩1. ASSUME.** (H1) D1: the infinite chain, `𝔄`, and an injective
canonical-form tensor family.  (H2) D2(a): a `G`-covariant vacuum family
`{A_α}` with `G` compact.  (H3) When derivatives in `G` are taken, hypothesis
(S) of D2(e).  (H4) When a Hamiltonian appears, D10: `H = Σ_x h_{x,x+1}`
translation invariant, finite range, `G`-invariant on-site.
Justification: D1, D2, D10.

**⟨2⟩2.** Throughout, `α` is fixed, `H_α` is its stabiliser, and *unbroken
case* means `H_α = G`.  Statements labelled "unbroken" are asserted only then.
Justification: D2(a).

**⟨2⟩3.** `V_α(g)` is unitary and `θ_α(g)` real; the pair is unique up to
`V ↦ e^{iφ}V`.
Justification: D2(b), which quotes refs/arxiv-2011.12127 Eq. (eq:XAX=B),
`X^{-1}A^iX = e^{iχ}Y^{-1}A^iY ⟹ χ = 0 ∧ ∃φ: X = e^{iφ}Y`, and
refs/arxiv-0802.0447 Lemma 1 for unitarity of `V`.

---

## ⟨1⟩2. LEMMA IT (composition; cocycles; normal ordering)

**ASSUME.** ⟨1⟩1.

**PROVE.** For all `g,h ∈ G`:
(i) `θ_α(hg) = θ_α(g) + θ_{g·α}(h)` and `V_{g·α}(h)V_α(g) = e^{iω_α(h,g)}V_α(hg)`;
(ii) restricted to `H_α`, `θ_α` is a homomorphism `H_α → U(1)` and `ω_α` is a
`U(1)`-valued 2-cocycle, whose class `[ω_α] ∈ H²(H_α,U(1))` is independent of
the phase choice in ⟨1⟩1.⟨2⟩3, of the MPS gauge, and of blocking;
(iii) (unbroken, normal ordering) `ǔ_α(g) := e^{−iθ_α(g)}u(g)` is a unitary
representation of `H_α` satisfying (IT) with phase `1`;
(iv) (unbroken) `V_α(g) r V_α(g)^† = r` and `E(V_α(g) Y V_α(g)^†) = V_α(g)E(Y)V_α(g)^†`.

**⟨2⟩1.** `𝒰(g)` acts on the physical index only, hence commutes with
`Y ↦ W^{-1}YW` acting on the virtual indices, and `𝒰(h)𝒰(g) = 𝒰(hg)`.
Justification: D2, and `Σ_{s'}u(h)_{ss'}u(g)_{s's''} = (u(h)u(g))_{ss''}`.

**⟨2⟩2.** Applying (IT) twice,
`𝒰(h)𝒰(g)A_α = e^{i(θ_α(g)+θ_{g·α}(h))}[V_{g·α}(h)V_α(g)]^{-1}A_{h g·α}[V_{g·α}(h)V_α(g)]`,
while `𝒰(hg)A_α = e^{iθ_α(hg)}V_α(hg)^{-1}A_{hg·α}V_α(hg)`.
Justification: ⟨2⟩1 and D2(b) applied at `α` and then at `g·α`.

**⟨2⟩3.** The two right-hand sides of ⟨2⟩2 are equal; by the uniqueness in
⟨1⟩1.⟨2⟩3 the phases agree mod `2π` and the unitaries agree up to a phase.
This is (i), with `ω_α(h,g)` defined as that phase.
Justification: ⟨2⟩2 and ⟨1⟩1.⟨2⟩3.

**⟨2⟩4.** For `g,h ∈ H_α`, `g·α = α`, so (i) reads `θ_α(hg)=θ_α(g)+θ_α(h)` and
`V_α(h)V_α(g)=e^{iω_α(h,g)}V_α(hg)`; associativity of the triple product
`V(g_1)V(g_2)V(g_3)` gives
`ω_α(g_1,g_2)+ω_α(g_1g_2,g_3) = ω_α(g_2,g_3)+ω_α(g_1,g_2g_3)`.
Justification: (i) and associativity of matrix multiplication.

**⟨2⟩5.** Replacing `V_α(g) ↦ e^{iφ(g)}V_α(g)` sends
`ω_α(h,g) ↦ ω_α(h,g)+φ(h)+φ(g)−φ(hg)`, a 2-coboundary; the MPS gauge
`A^s ↦ Y^{-1}A^sY` sends `V_α(g) ↦ Y^{-1}V_α(g)Y`, leaving `ω_α` unchanged;
blocking `n` sites, `A^{(n)} := A^{s_1}\!⋯A^{s_n}`, reproduces (IT) with the
*same* `V_α(g)` and phase `nθ_α(g)`, leaving `ω_α` unchanged.  Hence `[ω_α]` is
well defined.  This is (ii).
Justification: ⟨2⟩4, D2(b), and D1(c).

**⟨2⟩6.** By (ii), `ǔ_α(h)ǔ_α(g) = e^{−i(θ_α(h)+θ_α(g))}u(hg) = ǔ_α(hg)`, so
`ǔ_α` is a representation; substituting into (IT) removes the phase.  This is
(iii).
Justification: ⟨2⟩4 and D2(d).

**⟨2⟩7.** Write `Ã^s := 𝒰(g)A^s`.  Then
`Σ_s Ã^s Y (Ã^s)^† = Σ_{s,s',s''}u_{ss'}\overline{u_{ss''}}A^{s'}Y(A^{s''})^† = E(Y)`
by unitarity of `u(g)`; and by (IT) with `g ∈ H_α` the same sum equals
`V^{-1}E(VYV^†)V`.  Hence `E(VYV^†)=VE(Y)V^†`.  Putting `Y=r` gives
`E(VrV^†)=VrV^†`; uniqueness of the fixed point (D1(c)) and `tr(VrV^†)=tr r=1`
give `VrV^† = r`.  This is (iv).
Justification: D2(b), D1(c), and unitarity of `u(g)`, `V_α(g)`.
[Equivalent to condition C2 of refs/arxiv-0802.0447: "`E` is covariant, i.e.
for all `X`, `E(VXV^†)=VE(X)V^†`".]

**⟨2⟩8. QED.** (i)--(iv) are ⟨2⟩3, ⟨2⟩5, ⟨2⟩6, ⟨2⟩7.

---

## ⟨1⟩3. THEOREM WI (truncated-symmetry identity)

**ASSUME.** ⟨1⟩1; `R = [a,b]` a finite interval; `g ∈ G`; `Λ ⊇ R` a finite
window; boundary vectors `b_l, b_r ∈ ℂ^χ` arbitrary.

**PROVE.** Exactly, as window vectors (D1(e)),

  `U_R(g) |ψ_Λ(A_α; b_l,b_r)⟩ = e^{i|R|θ_α(g)} |ψ_Λ(T_R^{(g)}; b_l,b_r)⟩`,   **(WI)**

where the decoration `T_R^{(g)}` carries `A_α` on `Λ∖R`, `A_{g·α}` on `R`, the
bond insertion `V_α(g)^{-1}` on `∂_-R` and `V_α(g)` on `∂_+R`.  In particular,
in the unbroken case the interior is unchanged and the *entire* effect of a
symmetry applied to a region is two virtual operators on the region's two
boundary bonds.

**⟨2⟩1.** Expanding `U_R(g)|ψ_Λ⟩` in the physical basis, the coefficient of
`|s'⟩` is obtained from that of `|s⟩` by replacing, at each `x ∈ R`, the matrix
`A_α^{s_x}` by `Σ_{s_x} u(g)_{s'_x s_x} A_α^{s_x}`.
Justification: D3(b), `U_R(g)=Π_{x∈R}u_x(g)`, and linearity; the matrices at
sites outside `R` are untouched.

**⟨2⟩2.** By (IT), each such replacement equals
`e^{iθ_α(g)} V_α(g)^{-1} A_{g·α}^{s'_x} V_α(g)`.
Justification: D2(b).

**⟨2⟩3.** The ordered product over `x=a,…,b` is therefore
`e^{i|R|θ_α(g)} V_α(g)^{-1} A_{g·α}^{s'_a}\,[V_α(g)V_α(g)^{-1}]\,A_{g·α}^{s'_{a+1}}⋯A_{g·α}^{s'_b} V_α(g)`,
and every interior bracket is `𝟙`.
Justification: ⟨2⟩2 and associativity; `|R| = b-a+1` factors of the phase.

**⟨2⟩4.** The surviving factors are `V_α(g)^{-1}` immediately left of site `a`
— i.e. on bond `∂_-R = (a−1|a)` — and `V_α(g)` immediately right of site `b`
— i.e. on bond `∂_+R = (b|b+1)`.  This is exactly the decoration `T_R^{(g)}`.
Justification: ⟨2⟩3 and D1(e), D3(b).

**⟨2⟩5.** The identity holds for every `Λ ⊇ R` and every `b_l,b_r`, hence also
for the induced states: for `O ∈ 𝔄_W` with any finite `W`,
`ω_α(U_R(g)^† O U_R(g)) = ω_α[T_R^{(g)}](O)`, the phase cancelling.
Justification: ⟨2⟩1--⟨2⟩4, D1(d), D1(e).

**⟨2⟩6. QED.** WI is proved. □

**⟨2⟩7. Remark (hypotheses, honestly).** (a) The telescoping ⟨2⟩1--⟨2⟩4 uses
*only* (IT); injectivity is needed to *obtain* (IT) from the invariance of the
state and to make `(θ_α,V_α)` unique (⟨1⟩1.⟨2⟩3), not for the algebra.
(b) The phase `e^{i|R|θ_α(g)}` is extensive in `|R|`; it is *not* removable by
any rescaling of the state, only by the normal ordering of ⟨1⟩2(iii), which
replaces `u` by `ǔ_α` — physically, by measuring the charge relative to its
vacuum density.  Every "half-infinite string" statement below is made for `ǔ_α`
or for the *state*, on which the phase acts trivially; asserting a limit of the
*operator* `U_{[x,y]}(g)` with `θ_α(g) ≠ 0` is meaningless.
(c) The left/right assignment `V^{-1}` on `∂_-R`, `V` on `∂_+R` is fixed by the
(IT) convention of D2(b); the opposite convention flips both.

---

## ⟨1⟩4. THEOREM A1 (charge algebra, `𝒜`, and `[ω_α]`)

**ASSUME.** ⟨1⟩1, ⟨1⟩2, ⟨1⟩3, and the unbroken case `H_α = G`; normal ordering
(so `θ_α ≡ 0` and `U_ℤ` fixes `ω_α`).

**PROVE.**
(a) *(charges live on one bond)* For any finite `R` the right insertion is
invisible to observables to its left and the left insertion invisible to
observables to its right; consequently the half-infinite operations of D3(c)
exist **as maps on states**, with
`1_{[x,∞)}g ⊳ ω_α = ω_α^{V_α(g)^{-1}@(x−1|x)}`, and the convergence is
*exact* (not merely asymptotic) once the window is separated from the moving
end.
(b) *(non-implementability)* If `V_α(g) ∉ U(1)·𝟙` then `(U_{[x,y]}(g)Ω_A)_y`
is **not** Cauchy in `H_A`; the half-infinite symmetry is implemented on states
but not by a strongly convergent sequence of operators.
(c) *(faithfulness)* `ω_α^{M@b} = ω_α` iff `M ∈ ℂ·𝟙`.  Hence the asymptotic
operation labelled by `g` acts nontrivially exactly for `g ∉ N_α :=
{g : V_α(g) ∈ U(1)𝟙}`, a normal subgroup of `G`.
(d) *(charge algebra and its central extension)* The bond implementers satisfy
`𝒱_b(h)𝒱_b(g) = e^{iω_α(h,g)}𝒱_b(hg)` on decorated states: `g ↦ V_α(g)` is a
projective unitary representation of `G` on the virtual space `ℂ^χ`, i.e. a
representation of the twisted group algebra `𝔞_α = ℂ_{ω_α}[G]` (D4(d)).  Its
class `[ω_α] ∈ H²(G,U(1))` **is** the central extension of the asymptotic
charge algebra, and infinitesimally
`[𝔮_b(ξ),𝔮_b(ζ)] = 𝔮_b([ξ,ζ]) + c_α(ξ,ζ)𝟙`.
(e) *(`𝒜` and the diagonal)* At a common bond `b`, the left half-infinite
operation leaves `V_α(g_L)` and the right one leaves `V_α(g_R)^{-1}`, so their
composite is `𝒱_b(V_α(g_L)V_α(g_R)^{-1})`; for `g_L = g_R = g` this is the
identity on states, and it equals the global symmetry `U_ℤ(g)`.  Hence the
action of `G_L × G_R` on the vacuum sector factors through the coset space
`𝒜 = (G_L×G_R)/G_diag ≅ G`, `(g_L,g_R) ↦ g_L g_R^{-1}`.
`𝒜` is a **group** iff `G` is abelian (D4(c)).
(f) *(what `𝒜` relabels)* `𝒜` acts transitively on the set of `g`-twisted
endpoint sectors of D9(c), and *faithfully* on `G/N_α` (by (c)); it does
**not** move the sector label `(α,α)` of D9(a), which is trivial in the
unbroken case.  Reading A1 as a statement about the `𝒦_{αβ}` labels would make
it vacuous; the content is the `𝔞_α`-module structure of the endpoint.
(g) *(invariance of the SPT index)* `[ω_α]` is constant along any continuous
path `t ↦ A_α(t)` of injective canonical-form tensors that are `G`-symmetric at
every `t`, provided `H²(G,U(1))` is discrete (`G` finite, or `G` compact with
finite `H²`).

**⟨2⟩1. PROVE (a).** Environments absorb the far insertion exactly.

**⟨3⟩1.** In canonical form `l = 𝟙`, `E(r)=r`.  Inserting a unitary `M` on a
bond replaces the environment accumulated up to that bond by `M^† 𝟙 M = 𝟙` on
the left, or `M r M^† ` on the right.
Justification: D1(c), D1(e).

**⟨3⟩2.** For `M = V_α(g)^{±1}`, `M r M^† = r` by ⟨1⟩2(iv); and `M^†𝟙M = 𝟙`.
Justification: ⟨1⟩2(iv), unitarity.

**⟨3⟩3.** Hence for `O ∈ 𝔄_W` and `R = [x,y]` with `y > max W`, the value
`ω_α(U_R(g)^†OU_R(g))` computed by WI does not involve the insertion at
`∂_+R`: the environment to the right of `W` is `E^{y−maxW}(V r V^†) = E^{…}(r) = r`.
Justification: ⟨3⟩1--⟨3⟩2, WI ⟨1⟩3.⟨2⟩5, and `E(r) = r`.

**⟨3⟩4.** Therefore `y ↦ ω_α∘Ad(U_{[x,y]}(g)^†)` is *eventually constant* on
each `𝔄_W`, equal to `ω_α^{V_α(g)^{-1}@(x−1|x)}`; the weak-* limit of D3(c)
exists.  Symmetrically for the left-moving end.
Justification: ⟨3⟩3 and D3(c).

**⟨3⟩5. QED.**

**⟨2⟩2. PROVE (c).** `ω_α^{M@b} = ω_α` iff `M ∈ ℂ𝟙`.

**⟨3⟩1.** Choose a window `W = [−w,w]` containing the bond `b = (0|1)` with
`w ≥ n_0` of D1(c).  With `l=𝟙`, the reduced matrix elements of `ω_α^{M@b}` on
`W` are `tr[P_1 M P_2 r Q_2^† M^† Q_1^†]` with
`P_1 = A^{s_{-w}}\!⋯A^{s_0}`, `P_2 = A^{s_1}\!⋯A^{s_w}` and `Q_i` the same
built from `s'`; those of `ω_α` are the same with `M = 𝟙`.
Justification: D1(d), D1(e).

**⟨3⟩2.** By injectivity, `P_1,P_2,Q_1,Q_2` range over all of `M_χ(ℂ)`.
Justification: D1(c) with `w ≥ n_0`.

**⟨3⟩3.** Equality for all choices, with `P_1 = |a⟩⟨c|`, `Q_1^† = |a⟩⟨c|`,
gives `M Z M^† = Z` for `Z = P_2 r Q_2^†`; as `r` is invertible these `Z` span
`M_χ(ℂ)`.  Hence `M` commutes with `M_χ(ℂ)`, so `M ∈ ℂ𝟙`.  The converse is
trivial.
Justification: ⟨3⟩1--⟨3⟩2 and the triviality of the centre of `M_χ(ℂ)`.

**⟨3⟩4.** `N_α = {g : V_α(g) ∈ U(1)𝟙}` is the preimage of the centre under a
projective representation, hence a normal subgroup.
Justification: ⟨1⟩2(i) and ⟨3⟩3.

**⟨3⟩5. QED.**

**⟨2⟩3. PROVE (b).** Non-implementability.

**⟨3⟩1.** Put `Ψ_y := U_{[x,y]}(ǔ_α(g))Ω_A`, a unit vector.  For `y<y'`,
`⟨Ψ_y,Ψ_{y'}⟩ = ω_α(U_{[y+1,y']}(ǔ_α(g)))`, which by translation invariance
equals `ρ_n := ω_α(U_{[1,n]}(ǔ_α(g)))`, `n = y'-y`.
Justification: unitarity, `U_{[x,y]}^†U_{[x,y']} = U_{[y+1,y']}`, and
translation invariance of `ω_α`.

**⟨3⟩2.** `(Ψ_y)` is Cauchy iff `ρ_n → 1`, iff `‖U_{[1,n]}(ǔ_α(g))Ω_A − Ω_A‖→0`.
Justification: `‖Ψ_y−Ψ_{y'}‖² = 2−2\,\mathrm{Re}\,ρ_n` and ⟨3⟩1.

**⟨3⟩3.** Assume `ρ_n → 1`.  Fix `O ∈ 𝔄_{[−w,w]}` and take `n > w`.  Then
`|ω_α(U_{[1,n]}^†OU_{[1,n]}) − ω_α(O)| ≤ 2‖O‖\,‖U_{[1,n]}Ω_A − Ω_A‖ → 0`.
Justification: Cauchy--Schwarz in `H_A`.

**⟨3⟩4.** By WI and ⟨2⟩1.⟨3⟩3, for `n > w` the left-hand side of ⟨3⟩3 equals
`|ω_α^{V_α(g)^{-1}@(0|1)}(O) − ω_α(O)|`, which is independent of `n`.  Hence it
vanishes for every such `O`, so `ω_α^{V_α(g)^{-1}@(0|1)} = ω_α` on every
window, so by (c) `V_α(g) ∈ ℂ𝟙`.
Justification: ⟨1⟩3, ⟨2⟩1.⟨3⟩3, ⟨2⟩2.

**⟨3⟩5.** Contrapositive: `V_α(g) ∉ U(1)𝟙 ⟹ (Ψ_y)` not Cauchy.
Justification: ⟨3⟩2--⟨3⟩4.

**⟨3⟩6. QED.**

**⟨2⟩4. PROVE (d).** Charge algebra.

**⟨3⟩1.** `𝒱_b(M)𝒱_b(M') = 𝒱_b(MM')` by definition of bond insertion, and
`V_α(h)V_α(g)=e^{iω_α(h,g)}V_α(hg)` by ⟨1⟩2(ii).
Justification: D4(a), ⟨1⟩2(ii).

**⟨3⟩2.** Hence `g ↦ V_α(g)` is an `ω_α`-projective unitary representation of
`G` on `ℂ^χ`, i.e. a `*`-representation of `𝔞_α = ℂ_{ω_α}[G]`; a genuine
representation exists in the class iff `[ω_α] = 0`.
Justification: ⟨3⟩1 and D4(d).

**⟨3⟩3.** Under (S), differentiating `V_α(exp(εξ))V_α(exp(ε'ζ))` twice at the
origin and antisymmetrising gives
`[X_α(ξ),X_α(ζ)] − X_α([ξ,ζ]) = c_α(ξ,ζ)𝟙` with `c_α` the antisymmetrised
second derivative of `ω_α`, a Lie-algebra 2-cocycle.
Justification: ⟨3⟩1, D2(e), and the standard differentiation of a projective
representation.

**⟨3⟩4.** `[ω_α]` is the projective class of the SPT literature.
Justification: refs/arxiv-2011.12127, "it is perfectly fine if they transform
according to projective representations, that is, representations up to a phase
`X_gX_h=e^{iω(g,h)}X_{gh}`", classified by `H²_α(G,U(1))`; and
refs/arxiv-1412.5604, "In one dimension, Matrix Product States were used to
completely classify SPT phases via the second cohomology group of their
symmetry group".

**⟨3⟩5. QED.**

**⟨2⟩5. PROVE (e).** `𝒜` and the diagonal.

**⟨3⟩1.** WI applied to `R = [x',b]` with `x' → −∞` leaves the `∂_+R`
insertion `V_α(g_L)` on bond `b` — this is the *left* half-infinite string
`U_{(−∞,b]}(g_L)`.  WI applied to `R = [b+1,y]` with `y → +∞` leaves the
`∂_-R` insertion `V_α(g_R)^{-1}` on the *same* bond `b` — this is the *right*
string `U_{[b+1,∞)}(g_R)`.  Both limits exist by ⟨2⟩1.
Justification: ⟨1⟩3.⟨2⟩4, ⟨2⟩1, D4(b).

**⟨3⟩2.** For `g_L = g_R = g` the two insertions at the same bond multiply to
`V_α(g)V_α(g)^{-1}=𝟙`; and the composite operation is the global `U_ℤ(g)`,
which fixes `ω_α` (unbroken).  Hence `G_diag` is exactly the stabiliser of the
vacuum state inside `G_L×G_R`.
Justification: ⟨3⟩1, D2(a) with `H_α=G`, and (c) (`𝟙 ∈ ℂ𝟙`).

**⟨3⟩3.** The orbit map `(g_L,g_R) ↦ (g_L,g_R)⊳ω_α` therefore factors through
the coset space `(G_L×G_R)/G_diag`, and `[(g_L,g_R)] ↦ g_Lg_R^{-1}` is a
bijection onto `G` intertwining the residual actions — the combination
`g_Lg_R^{-1}` being exactly the one that survives in
`V_α(g_L)V_α(g_R)^{-1}` up to the cocycle phase (⟨1⟩2(ii)).
Justification: ⟨3⟩2 and the orbit--stabiliser bijection.

**⟨3⟩4.** `G_diag` is normal in `G×G` iff `G` is abelian; hence the quotient
carries a group structure iff `G` is abelian.
Justification: `(h_1,h_2)(g,g)(h_1,h_2)^{-1}=(h_1gh_1^{-1},h_2gh_2^{-1})`,
which lies in `G_diag` for all `g,h_i` iff `G` is abelian.

**⟨3⟩5. QED.**

**⟨2⟩6. PROVE (f).** By (a) the only residue of a half-infinite string is a
bond insertion; by (c) two group elements give the same state exactly when they
agree modulo `N_α`; by ⟨1⟩8(iii) (corner-a-kinks.md) the boundary labels at
`±∞` are unchanged because `g·α = α`.  Hence `𝒜` permutes the endpoint sectors
D9(c) transitively, with kernel `N_α`, and fixes the sector label `(α,α)`.
Justification: ⟨2⟩1, ⟨2⟩2, D9(a), D9(c).  **⟨3⟩1. QED.**

**⟨2⟩7. PROVE (g).** Along a symmetric path, `V_α(g;t)` may be chosen
continuously in `t` for each `g` (it is determined up to a phase by the tensor,
and by refs/arxiv-0802.0447 Lemma 1 it is the eigenvector of `E_u(t)` for the
unique eigenvalue of modulus one, which depends continuously on `t` while
injectivity and that spectral isolation persist).  Then `ω_α(h,g;t)` is
continuous, so `[ω_α(t)]` is a continuous map into the discrete set
`H²(G,U(1))`, hence constant on connected components.
Justification: refs/arxiv-0802.0447 Lemma 1 (uniqueness of the modulus-one
eigenvalue of `E_u`), continuity of isolated spectral projections, D1(c).
**⟨3⟩1. QED.**

**⟨2⟩8. QED.** (a)--(g) are ⟨2⟩1--⟨2⟩7.  □

**⟨2⟩9. SKETCH (normality of the endpoint state).**

> **BOXED — what is missing.** We do *not* prove here that `ω_α^{M@b}` is a
> *normal* state of `π_α(𝔄)''`, i.e. a vector state in `H_A`.  The expected
> proof uses the split property of an exponentially clustering pure MPS state:
> `H_A ≅ H_L ⊗ H_R` across any bond with `Ω_A = Σ_{i=1}^{χ}\sqrt{λ_i}|L_i⟩|R_i⟩`
> of Schmidt rank exactly `χ`, whereupon a bond insertion `M` is the vector
> `Σ_{ij}\sqrt{λ_j}M_{ij}|L_i⟩|R_j⟩ ∈ H_A`.  The missing ingredient is the
> infinite-volume Schmidt decomposition (split property) with the identification
> of the Schmidt index with the MPS virtual index; at finite windows it is
> elementary (D1(e)), and the limit is standard but is not derived from a source
> in `refs/`.  **Nothing in (a)--(g) or in WI, A2, G0 depends on this**; the
> half-infinite operations are used only as maps on states (D3(c)), where (a)
> gives an exact, not merely asymptotic, answer.

---

## §5. Pitfalls, scope, and terminology

### 5.1 Normalizability, the vacuum manifold, boosts, and *which* symmetry is broken

**(P1) Three different objects at `k = 0`.**  These must never be conflated:
1. *The momentum-`k` ansatz vector* `|Φ_k(B_G(ξ))⟩ = Q_k(ξ)Ω_α`.  For the
   ferromagnet and `ξ = ξ_x` this is `\tfrac{i}{2}Σ_x e^{ikx}S^-_x|Ω⟩`, with
   `⟨Φ_k(B_G)|Φ_{k'}(B_G)⟩ = \tfrac14·2πδ(k−k')` for **every** `k`, including
   `k = 0` (from `⟨Ω|S^+_yS^-_x|Ω⟩ = δ_{xy}`).  So it is a δ-normalised
   generalised vector, never an element of `H_A`, and `k = 0` is **not** special
   in that respect.  Assertions that "the `k=0` magnon fails to be normalisable
   while `k ≠ 0` is fine" are simply wrong.
2. *The smeared charge* `Q_Λ(ξ)Ω_α` (profile `1_Λ ∈ 𝔉_ec(ξ)`, D3(a)).  Here
   `k = 0` **is** special, and it is the sharp discriminator between broken and
   unbroken directions:
   - `ξ ∈ 𝔥_α` (normal ordered): by G0(d) the sum telescopes,
     `Q_Λ(ξ)Ω_α = (𝒥_{maxΛ}(ξ) − 𝒥_{minΛ−1}(ξ))Ω_α`, whose window norm is
     bounded **uniformly in `Λ`** (it is two bond insertions, norm² `≤ 4‖X_α(ξ)‖²`).
     The charge is implementable.
   - `ξ ∈ 𝔪_α` (broken): no such telescoping exists (that is exactly G0(b)),
     and for the ferromagnet `‖Q_Λ(ξ_x)Ω_α‖² = |Λ|/4 → ∞` (generator convention:
     corner-a-goldstone.md ⟨1⟩7).  The broken charge is **not** implementable;
     only the derivation `O ↦ ω_α([Q_Λ(ξ),O])`, `Λ ⊇ supp(O)`, survives.
     This is the lattice form of the Goldstone non-implementability theorem and
     the sharp analogue of the soft-photon zero-mode subtlety.
3. *The finite vacuum rotation* `ω_{g·α}`, `g ∉ H_α`: a state **disjoint** from
   `ω_α` (corner-a-kinks.md ⟨1⟩8), macroscopically different, in no sense a
   vector in `H_A`.  Exponentiating (2) does not give (1), and neither is (3).

**(P2) No boosts.** Nothing above uses Galilean or Lorentz covariance; the
universal factor of G0(e) is `(e^{ik}−1)`, a lattice difference operator, not a
covariant object.  Any soft factor derived from Corner A will depend on lattice
momenta and group velocities `v(k)` and cannot be recast covariantly.

**(P3) The ferromagnet is type B.** corner-a-goldstone.md ⟨1⟩7(iii) derives `2 → 1` Goldstone
counting from the tensor data, and ibid. ⟨1⟩7(iv) derives `ω ∼ k²`.  Consequently
the soft expansion must be organised in **`k`**, not in `ω`: by oracle O10 the
energy variable produces a direction-labelled Puiseux series
`δ = 2σ\sqrt{2ω_s/J} + O(ω_s)`.  Every soft statement in this campaign is an
expansion in `k`.

**(P4) Which symmetry is broken — FM versus Ising/XXZ.**  These are *not* the
same situation and must never be conflated:
- *M1, isotropic FM.* `G = SU(2)` is **fully broken** in the ground state; the
  stabiliser `H_α = U(1)` survives.  `Ω_vac ≅ S²` is a **continuum**.  The
  Goldstone (magnon) belongs to the broken directions `𝔪_α`, so G0's
  pure-gauge statement does **not** apply to it (corner-a-goldstone.md ⟨1⟩6(b)).  There are no gapped
  kinks: the "kinks" produced by A2 interpolate between infinitesimally
  different vacua and cost arbitrarily little energy.  The `U(1)` that survives
  is *not* the Goldstone direction, and `[ω_α]=0` for it.
- *M2, easy-axis XXZ (`Δ>1`) / Ising.* The broken group is the **discrete**
  `ℤ₂` spin flip; `Ω_vac = {↑,↓}`; kinks are genuine gapped domain walls; the
  continuous `U(1)` about `z` remains unbroken and *is* where (IT), WI and A1
  apply with `H_α = U(1)`.  There is no Goldstone; "soft" means a low-frequency
  expansion **about the magnon gap**, and this must be said explicitly wherever
  M2 is used.
- Consequently the phrase "the broken symmetry" is ambiguous in this project
  and is banned: every statement names its group (`G`, `H_α`, or the broken
  complement `𝔪_α`) explicitly.

### 5.2 Exact on the ansatz manifold versus true statements about the model

- **Exact for the MPS state, unconditionally:** WI (⟨1⟩3), Lemma IT, Lemma N,
  A1(a)--(f), G0(a)--(d), A2's algebraic content.  These are identities about
  `ω_{A_α}` and about the linear space of ansatz vectors; they hold for *any*
  injective covariant family, whether or not it is a ground state of anything.
- **Exact for the true model only when the MPS is exact:** corner-a-goldstone.md ⟨1⟩7 (the isotropic
  ferromagnet, where `|Ω⟩` is an exact product ground state, `χ=1`, and the
  one-magnon states are exact eigenvectors).  This is why M1 is the model of
  record for the soft theorem.
- **Uses only `H`, not the ansatz:** G0(e).  It is an operator identity in
  `𝔄_loc` and is therefore true of the *true* model, whatever its ground state.
  This is the reason G0(e), not G0(b), is the seed of Corner C.
- **Approximate for a variational MPS:** if `ω_A` approximates a true ground
  state with local error `ε` (in the sense `|ω_A(O)−ω_{gs}(O)| ≤ ε‖O‖` for `O`
  supported in a window of size `w`), then WI and A1 hold for `ω_{gs}` up to
  `O(ε)` on each such window.  No claim of this campaign currently relies on
  that; if one does, the `ε`-tracking must be written out.
- **Not established here:** that the excitation-ansatz S-matrix equals the true
  S-matrix.  For M1 magnons it does (exact eigenstates); for M2 kinks at
  generic `Δ` it does not, and any statement there is variational.

### 5.3 Terminology discipline (coinages flagged)

| term used here | status | established name |
|---|---|---|
| "MPO Ward identity", **(WI)** | **coinage** of HANDOFF §1.2 | pulling-through; symmetry action on the virtual level; string-order structure of refs/arxiv-0802.0447 |
| "lattice asymptotic symmetry group `𝒜`" | **coinage**; and see below | no established name; the underlying object is the pair of edge/virtual symmetry actions |
| "asymptotic charge algebra `𝔞_α`" | **coinage** | twisted group algebra `ℂ_ω[G]` of the projective edge representation |
| "bond current potential `𝒥`" | **coinage** (from docs/framing.md §4) | none; the virtual/tangent data `X` of the MPS |
| "kink = contact term of a broken truncated symmetry" | **coinage** (slogan) | domain wall; topological sector of the excitation ansatz (refs/arxiv-1810.07006) |
| "SPT index `[ω_α]`" | **established** | second cohomology class classifying 1D SPT phases (refs/arxiv-1412.5604, refs/arxiv-2011.12127) |
| "intertwining relation (IT)" | **established** | fundamental theorem of MPS / intertwiner (refs/arxiv-0802.0447 Lemma 1, C1) |

**Additional flag (`𝒜` is not a group).**  HANDOFF §2 and
`claims/CLAIMS.md` call `𝒜 = (G_L×G_R)/G_diag` a *group*.  By A1(e)/D4(c) this
is correct **iff `G` is abelian**; `G_diag` is normal in `G×G` only in that
case.  For `G = SU(2)` (model M1) it is a homogeneous `G_L×G_R`-space
isomorphic to `G` as a set.  The paper must not write "asymptotic symmetry
group" for nonabelian `G`.

---

## Claim status produced by the Corner A shards

| claim | status | where |
|---|---|---|
| **WI** | **PROVED** (exact, finite-window algebra; hypotheses in ⟨1⟩3.⟨2⟩7) | this shard, ⟨1⟩3 |
| **A1** | **PROVED** for (a)--(g); the *completeness* of `[ω_α]` as a phase invariant is cited, not proved (⟨1⟩4.⟨2⟩7 proves invariance only); normality of the endpoint state is **SKETCH** (⟨1⟩4.⟨2⟩9) and is used nowhere | this shard, ⟨1⟩4 |
| **G0** | **PROVED**, in a corrected form: pure gauge ⟺ unbroken (⟨1⟩6(b)); the universal soft prefactor is `(e^{ik}−1)` (⟨1⟩6(e)) | [`corner-a-goldstone.md`](corner-a-goldstone.md), ⟨1⟩6--⟨1⟩7 |
| **A2** | **PROVED** for (a)--(f); the FM continuum-`Ω_vac` uniformity is **SKETCH** | [`corner-a-kinks.md`](corner-a-kinks.md), ⟨1⟩8--⟨1⟩9 |
