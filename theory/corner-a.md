# Corner A — the lattice asymptotic symmetry: Ward identity and charge algebra

**Revision r3** (2026-08-25), after critic verdicts
[`verdicts/corner-a-r1.md`](verdicts/corner-a-r1.md) = FAIL(WI,A1,A2,G0) and
[`verdicts/corner-a-r2.md`](verdicts/corner-a-r2.md) = FAIL(A1,A2,G0,B3).
Dispositions: [`corner-a-r1-response.md`](corner-a-r1-response.md),
[`corner-a-r2-response.md`](corner-a-r2-response.md).
Numerical backing for every repair: [`checks/corner_a_check.py`](checks/corner_a_check.py),
checks **C0--C11** (ALL PASS, run 2026-08-25).

Proof shard for claims **WI** and **A1** of [`claims/CLAIMS.md`](../claims/CLAIMS.md),
Companion shards (L2: 200--500 loc, one lemma-cluster per file):
[`corner-a-goldstone.md`](corner-a-goldstone.md) — Lemma SBP, **G0**, and the
ferromagnet/oracle consistency check;
[`corner-a-kinks.md`](corner-a-kinks.md) — the broken case **A2**;
[`corner-a-pitfalls.md`](corner-a-pitfalls.md) — §5, the campaign-level pitfall
and terminology list.
All symbols are those of [`notation.md`](../notation.md); all definitions are
D1--D5, D9--D12 of [`definitions.md`](../definitions.md) and are not restated.
Literature enters only through the quotations recorded in D2 and D5, taken from
the local TeX under `refs/` (L3).  Structure follows L6b.

Register note: every step below is either (i) an exact algebraic identity
between finite window vectors (D1(e)), (ii) a finite-dimensional linear-algebra
statement about `M_χ(ℂ)`, or (iii) a weak-* limit with an explicitly exhibited
rate `λ̃ ∈ (λ_E,1)` (D1(c)).  Where an identity holds only in a limit, the norm
and the limit are named (D12); r1 was rejected partly for failing to do this.

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

**ASSUME.** ⟨1⟩1; `R = [a,b]` a finite interval; `g ∈ G`; and **either**
(W1) a finite window `Λ ⊇ R` together with the D1(e) edge-bond insertions,
**or** (W2) a window `Λ ⊇ [a−1,b+1]`, in which case both insertions land on
interior bonds.  Boundary vectors `b_l, b_r ∈ ℂ^χ` arbitrary.

**PROVE.** Exactly, as window vectors,

  `U_R(g) |ψ_Λ(A_α; b_l,b_r)⟩ = e^{i|R|θ_α(g)} |ψ_Λ(T_R^{(g)}; b_l,b_r)⟩`,   **(WI)**

where `T_R^{(g)}` carries `A_α` on `Λ∖R`, `A_{g·α}` on `R`, the bond insertion
`V_α(g)^{-1}` on `∂_-R = (a−1|a)` and `V_α(g)` on `∂_+R = (b|b+1)`.  And, as
states, **with no phase**, for every `O ∈ 𝔄`,

  `ω_α(U_R(g)^† O\, U_R(g)) = ω_α[T_R^{(g)}](O)`.   **(WI-state)**

In particular, in the unbroken case the interior is unchanged and the *entire*
effect of a symmetry applied to a region is two virtual operators on the
region's two boundary bonds.

**⟨2⟩1.** Expanding `U_R(g)|ψ_Λ⟩` in the physical basis, the coefficient of
`|s'⟩` is obtained from that of `|s⟩` by replacing, at each `x ∈ R`, the matrix
`A_α^{s_x}` by `Σ_{s_x} u(g)_{s'_x s_x} A_α^{s_x}`.
Justification: D3(b), `U_R(g)=Π_{x∈R}u_x(g)`, and linearity; sites outside `R`
are untouched.

**⟨2⟩2.** By (IT), each such replacement equals
`e^{iθ_α(g)} V_α(g)^{-1} A_{g·α}^{s'_x} V_α(g)`.
Justification: D2(b).

**⟨2⟩3.** The ordered product over `x=a,…,b` is
`e^{i|R|θ_α(g)} V_α(g)^{-1} A_{g·α}^{s'_a}[V_α(g)V_α(g)^{-1}]A_{g·α}^{s'_{a+1}}⋯A_{g·α}^{s'_b} V_α(g)`,
and every interior bracket is `𝟙`.
Justification: ⟨2⟩2 and associativity; `|R| = b−a+1` factors of the phase.

**⟨2⟩4.** The surviving factors are `V_α(g)^{-1}` on bond `∂_-R` and `V_α(g)`
on `∂_+R`.  Under (W2) these are interior bonds of `Λ`; under (W1) they are
edge bonds, admitted by D1(e) and equivalent to
`b_l ↦ V_α(g)^{-†}b_l = V_α(g)b_l`, `b_r ↦ V_α(g)b_r`.
Justification: ⟨2⟩3, D1(e), D3(b).

**⟨2⟩5.** (WI-state): the phase `e^{i|R|θ_α(g)}` appears in bra and ket and
cancels, and the decoration differs from `A_α` on finitely many sites and
bonds, so `ω_α[T_R^{(g)}]` is a decorated state in the sense of D1(e).
Justification: ⟨2⟩1--⟨2⟩4, D1(d), D1(e).

**⟨2⟩6. QED.** WI is proved. □

**⟨2⟩7. Remark (the r1 defect, and what fixed it).** r1 asserted (WI) "for
every `Λ ⊇ R`" with a window vector that admitted *interior* bond insertions
only.  For `Λ = R` the two insertions then lie outside the expression and the
claim is **false**: measured discrepancy `1.658` for the `χ=2` Pauli tensor
(check C2).  Two repairs are available and both are adopted above: enlarge the
window (W2), or admit edge-bond insertions (W1, the D1(e) revision) — the
latter restores exactness to `0.0` (check C2b).
Justification: r1 objection 1; checks C2, C2b.

**⟨2⟩8. Remark (orientation, now genuinely pinned).** The assignment
`V^{-1}` on `∂_-R`, `V` on `∂_+R` is fixed by the (IT) convention of D2(b).
**HANDOFF §1.2 line 42 states the opposite orientation**; the brief is a
historical document and is not edited, so the correction is recorded here and
in §5.3.  Note that the `ℤ₂` example used by the r1 critic to "confirm" the
orientation has `V = Z = V^{-1}` and is *blind* to the flip; check C1 therefore
uses a `U(1)` symmetry with `V(t) = e^{itZ/2} ≠ V(t)^{-1}`, where the correct
orientation gives error `5.6·10^{-17}` and the flipped one `0.267` (checks
C0, C1, C1b, C1c).

**⟨2⟩9. Remark (hypotheses, honestly).** (a) The telescoping ⟨2⟩1--⟨2⟩4 uses
*only* (IT); injectivity is needed to *obtain* (IT) and to make `(θ_α,V_α)`
unique (⟨1⟩1.⟨2⟩3), not for the algebra.
(b) The phase `e^{i|R|θ_α(g)}` is extensive in `|R|`, removable only by the
normal ordering of ⟨1⟩2(iii).  It belongs to the *vector* identity; a phase
times a state is not a state, so (WI-state) carries none (r1 objection 2).
Asserting a limit of the *operator* `U_{[x,y]}(g)` when `θ_α(g) ≠ 0` is
meaningless.

---

## ⟨1⟩4. THEOREM A1 (endpoint torsor, charge algebra, and `[ω_α]`)

**Rewritten in r2.** r1's A1 was rejected on four counts: its endpoint sectors
were defined by `V_α(g)GL(χ) = GL(χ)` and were therefore all the same set
(obj 3); its twisted-algebra law used the wrong inverse and order and was
asserted on states, where phases are invisible (obj 4); its scalar lemma
ignored normalisation and needed a multilinear extension (obj 5); and its
stabiliser was `G_diag` only when the projective action is faithful (obj 3).
The corrected statement below separates three levels — window vectors, states,
GNS — and proves the first two.

**ASSUME.** ⟨1⟩1--⟨1⟩3, the unbroken case `H_α = G`, and normal ordering
(⟨1⟩2(iii)), so `θ_α ≡ 0`.  Every statement mentioning `𝒲_{Λ,b}` or `𝒱_b`
additionally assumes the window is **padded about `b`** (D4(a1)).  Notation
`N_α`, `ρ_α`, `𝒜_eff`, `𝒲_{Λ,b}` from D4; `E_b^α`, `⋆` from D9(c), which is
definition-only — A1 does **not** assume D9(c′), it proves it (r2 objection 7).

**PROVE.**
(a) *(charges live on one bond)* For finite `R` the right insertion is
invisible to observables to its left and the left insertion invisible to those
to its right; hence the half-infinite operations of D3(c) exist **as maps on
states**, with `1_{[x,∞)}g ⊳ ω_α = ω_α^{V_α(g)^{-1}@(x−1|x)}`, and the
convergence is *exact* (eventually constant on each `𝔄_W`), not asymptotic.
(b) *(non-implementability)* **If and only if** `V_α(g) ∉ ℂ^×𝟙`, then `(U_{[x,y]}(g)Ω_A)_y` is
not Cauchy in `H_A`: the half-infinite symmetry is implemented on states but by
no strongly convergent sequence of operators.
(c) *(the endpoint bijection)* `ω_α^{M@b} = ω_α^{M'@b}` **iff** `M' ∈ ℂ^× M`.
Hence `E_b^α ≅ PGL(χ)` canonically (D9(c)).
(d) *(charge algebra — on padded window vectors, honestly)*
  (d1) On a window **padded about `b`** (D4(a1): at least `n_0` sites each side,
       `b_l,b_r ≠ 0`), the map `ι_{Λ,b} : M_χ(ℂ) → 𝒲_{Λ,b}` is injective, so
       `𝒱_b(M) := ι ∘ L_M ∘ ι^{-1}` is a well-defined linear operator and
       `𝒱_b(h)𝒱_b(g) = e^{iω_α(h,g)}𝒱_b(hg)`: a **linear representation of
       `𝔞_α = ℂ_{ω_α}[G]`** in which the multiplier acts nontrivially.
       *Padding is necessary, not cosmetic* — without it the kernel of `ι` need
       not be left-invariant and `𝒱_b` is not an operator at all (⟨2⟩4.⟨3⟩0).
  (d2) The induced action on **states** kills the multiplier and is the genuine
       homomorphism `ρ_α : G → PGL(χ)`, `ker ρ_α = N_α`.
  (d3) The window action (d1) **is** a lift of `ρ_α`, but a *projective* one,
       with multiplier `ω_α`; such a lift exists for every `[ω_α]`, trivial or
       not.  What `[ω_α]` obstructs is **removing the multiplier**: it is the
       obstruction to lifting `ρ_α : G → PGL(χ)` to an *honest homomorphism*
       `G → U(χ)`.  *(r2 objection 2: r2 said `[ω_α]` obstructs "lifting (d2) to
       (d1)", which is false, since (d1) exists unconditionally.  Retracted.)*
       This is not a restatement of D4 or D9: `ρ_α` and its multiplier are
       produced by Lemma IT from the fundamental theorem of MPS, and D9(c) is
       now definition-only (D9(c′) records these as *consequences*).
(e) *(stabiliser and orbit, corrected)* The stabiliser of `ω_α` in `G_L × G_R`
is `S_α = {(g_L,g_R) : g_Lg_R^{-1} ∈ N_α} ⊇ G_diag`, with equality **iff**
`N_α = {e}`.  The orbit is in bijection with `G/N_α = 𝒜_eff`, a genuine group.
`𝒜 = (G_L×G_R)/G_diag` is *not* the orbit unless `N_α = {e}`, and is a group
only for abelian `G`.
(f) *(what acts on what)* `𝒜_eff` acts simply transitively on the orbit
`ρ_α(G) ⊆ E_b^α`; it does **not** move the sector label `(α,α)` of D9(a),
which is trivial in the unbroken case.
(g) *(invariance of the SPT index)* `[ω_α]` is constant along any continuous
path of `G`-symmetric injective canonical-form tensors, provided
`H²(G,U(1))` is discrete.

**⟨2⟩1. PROVE (a).**
**⟨3⟩1.** In canonical form `l = 𝟙`, `E(r) = r`; a unitary insertion `M` on a
bond replaces the accumulated environment by `M^†𝟙M = 𝟙` (left) or `MrM^†`
(right).
Justification: D1(c), D1(e).
**⟨3⟩2.** For `M = V_α(g)^{±1}`, `MrM^† = r` by ⟨1⟩2(iv) and `M^†𝟙M = 𝟙`.
Justification: ⟨1⟩2(iv), unitarity.
**⟨3⟩3.** Hence for `O ∈ 𝔄_W` and `R = [x,y]`, `y > max W`, the value
`ω_α(U_R(g)^†OU_R(g))` does not involve the `∂_+R` insertion: the environment
right of `W` is `E^{y−maxW}(VrV^†) = r`.
Justification: ⟨3⟩1--⟨3⟩2, (WI-state), `E(r)=r`.
**⟨3⟩4.** So `y ↦ ω_α∘Ad(U_{[x,y]}(g)^†)` is eventually constant on each `𝔄_W`,
equal to `ω_α^{V_α(g)^{-1}@(x−1|x)}`; the D3(c) limit exists.
Justification: ⟨3⟩3, D3(c).
**⟨3⟩5. QED.**

**⟨2⟩2. PROVE (c).** *(repairs r1 objection 5.)*
**⟨3⟩1.** `ω^{M@b}` is defined with a normalisation; the correct target is
therefore `M Z M^† = γ Z` for some `γ > 0`, not `MZM^† = Z`.  (r1 asserted "the
converse is trivial", which is false for `M = c𝟙` before normalising.)
Justification: D1(d), D1(e).
**⟨3⟩2.** Take `W = [−w,w] ∋ b = (0|1)` with `w ≥ n_0`.  With `l = 𝟙`, the
`(s,s')` matrix element of the reduced state is
`tr[P_1 M P_2 r Q_2^† M^† Q_1^†]`, where `P_1 = A^{s_{-w}}⋯A^{s_0}`,
`P_2 = A^{s_1}⋯A^{s_w}` and `Q_i` are built from `s'`.
Justification: D1(d), D1(e).
**⟨3⟩3.** The four words `P_1,P_2,Q_1,Q_2` vary **independently** — `P_1,P_2`
over disjoint index blocks of `s`, and `s,s'` are independent — and by D1(c)
each ranges over a spanning set of `M_χ(ℂ)`.  Both sides of the equality
`tr[P_1MP_2rQ_2^†M^†Q_1^†] = γ\,tr[P_1P_2rQ_2^†Q_1^†]` are **multilinear** in
`(P_1,P_2,Q_1,Q_2)`, hence the equality extends from the spanning set to all of
`M_χ(ℂ)^{×4}`.
Justification: D1(c) with `w ≥ n_0`, and multilinear extension.  *(This is the
step r1 omitted.)*
**⟨3⟩4.** Put `P_1 = |a⟩⟨b'|`, `Q_1^† = |c⟩⟨a|`; the identity becomes
`⟨b'|M(P_2rQ_2^†)M^†|c⟩ = γ⟨b'|P_2rQ_2^†|c⟩` for all `b',c`, i.e.
`MZM^† = γZ` for `Z = P_2rQ_2^†`, and these `Z` span `M_χ(ℂ)` since `r` is
invertible.
Justification: ⟨3⟩3 and invertibility of `r`.
**⟨3⟩5.** `MZM^† = γZ` for all `Z`: taking `Z = 𝟙` gives `MM^† = γ𝟙`, so
`M = √γ\,U` with `U` unitary and `UZU^† = Z` for all `Z`, whence `U ∈ ℂ𝟙` and
`M ∈ ℂ^×𝟙`.  Applying this to `M'^{-1}M` gives the general statement
`ω^{M@b} = ω^{M'@b} ⟺ M' ∈ ℂ^×M`.
Justification: ⟨3⟩4 and triviality of the centre of `M_χ(ℂ)`.
**⟨3⟩6.** Numerical confirmation: window fidelities `fid(𝟙,c𝟙) = 1.000000`,
`fid(Z,0.4Z) = 1.000000`, `fid(𝟙,Z) = fid(𝟙,X) = fid(Z,X) = 0`,
`fid(Z,X+2Z) = 0.800`.
Justification: check C6.
**⟨3⟩7. QED.**

**⟨2⟩3. PROVE (b).** *(repairs r1 objection 6.)*
**⟨3⟩1.** `Ψ_y := U_{[x,y]}(ǔ_α(g))Ω_A` is a unit vector and, for `y<y'`,
`⟨Ψ_y,Ψ_{y'}⟩ = ω_α(U_{[y+1,y']}(ǔ_α(g))) = ρ_n`, `n = y'−y`, by translation
invariance.
Justification: unitarity, `U_{[x,y]}^†U_{[x,y']} = U_{[y+1,y']}`, D1(d).
**⟨3⟩2.** r1 claimed "Cauchy `⟺ ρ_n → 1`".  That is wrong: for `y,y' > Y` the
difference `n = y'−y` ranges over **all** positive integers, so Cauchy forces
`Re ρ_n > 1 − ε²/2` for every `n ≥ 1` and every `ε > 0`, i.e.
**Cauchy `⟹ ρ_n = 1` for all `n ≥ 1`** — a stronger and correct conclusion,
which is all that is used.
Justification: `‖Ψ_y−Ψ_{y'}‖² = 2−2Re ρ_{y'−y}` and ⟨3⟩1.
**⟨3⟩3.** So `U_{[1,n]}(ǔ_α(g))Ω_A = Ω_A` for every `n`, hence
`ω_α∘Ad(U_{[1,n]}^†) = ω_α`.  For `O ∈ 𝔄_{[−w,w]}` and `n > w` the far
insertion drops out by ⟨2⟩1.⟨3⟩3, so `ω_α^{V_α(g)^{-1}@(0|1)}(O) = ω_α(O)` for
all such `O`.
Justification: ⟨3⟩2, ⟨2⟩1.⟨3⟩3, (WI-state).
**⟨3⟩4.** By (c), `V_α(g) ∈ ℂ^×𝟙`.  Contrapositive gives the forward direction.
Justification: ⟨2⟩2.
**⟨3⟩5.** (Converse, so that (b) is an *iff* — r2 objection 5.)  If
`V_α(g) = c𝟙`, `|c| = 1`, then by WI the two boundary insertions are `c^{-1}𝟙`
and `c𝟙`, whose product is `𝟙`; hence `U_{[x,y]}(ǔ_α(g))Ω_A = Ω_A` for every
`y`, the sequence is constant, and the strings *do* stabilise.  So
non-implementability holds **exactly when** `V_α(g)` is non-scalar.
Justification: ⟨1⟩3 (WI), ⟨2⟩2.
**⟨3⟩6. QED.**

**⟨2⟩4. PROVE (d).** *(repairs r1 objections 4, 7, 8 and r2 objections 1, 2.)*

**⟨3⟩0.** *(well-definedness — the r2 gap).*  `𝒲_{Λ,b}` is a space of
**physical vectors**, so a rule phrased on decorated representatives is an
operator only if it preserves every linear relation among them.  For an
**unpadded** window it does not.  Counterexample (critic's, independently
verified): `A^0 = diag(1,2)`, `A^1 = X` — a legitimate D1 tensor (transfer
spectrum `{4.303, 3, 1, 0.697}`, unique top eigenvalue, length-2 words of rank
`4`) — with `u(g) = diag(1,−1)`, `V = Z`, `b_l = (\sqrt2,1)`, `b_r = (1,0)`,
one site on each side of the bond, and
`N = \begin{pmatrix}-\sqrt2&0\\1&0\end{pmatrix}`: then `ι(N) = 0` but
`‖ι(ZN)‖_∞ = 4`, so `ker\,ι` is not invariant under `L_Z` and `𝒱_b(Z)` is not
an operator on `𝒲_{Λ,b}`.  **On a padded window (D4(a1)) `ι` is injective**
(D4(a2)): the coefficient `b_l^†P M Q b_r` is linear in `P` and in `Q`, each
ranges over a spanning set of `M_χ(ℂ)` by D1(c), and `b_l,b_r ≠ 0`, so
`v^†(M−M')w = 0` for all `v,w`, i.e. `M = M'`.  Padding restores
`rank\,ι = χ² = 4` on the counterexample.
Justification: D4(a1)--(a4); checks **C8**, **C8b**.  *(r2 objection 1,
conceded; the r2 A1(d1) and its PROVED row were false as written.)*

**⟨3⟩1.** (d1) With `ι` injective, `𝒱_b(M) := ι ∘ L_M ∘ ι^{-1}` is well defined
and `𝒱_b(M)𝒱_b(M') = 𝒱_b(MM')`.  With the D4(a4) choice
`𝒱_b(g) := 𝒱_b(V_α(g))` (**not** `V_α(g)^{-1}`, which reverses the law) and
⟨1⟩2(ii),
`𝒱_b(h)𝒱_b(g) = 𝒱_b(V_α(h)V_α(g)) = e^{iω_α(h,g)}𝒱_b(V_α(hg)) = e^{iω_α(h,g)}𝒱_b(hg)`.
`𝒲_{Λ,b}` is a genuine linear space, so the phase acts nontrivially on it.
Justification: ⟨3⟩0, D4(a4), ⟨1⟩2(ii).

**⟨3⟩2.** (d2) By (c), states see `M` only modulo `ℂ^×`; the induced map is
`ρ_α(g) = [V_α(g)] ∈ PGL(χ)`, and ⟨3⟩1 gives `ρ_α(h)ρ_α(g) = ρ_α(hg)` — an
honest homomorphism — with `ker ρ_α = N_α` by definition.  Note this is
bond-independent and padding-independent: it is a statement about states.
Justification: ⟨2⟩2, ⟨3⟩1, D4(b).

**⟨3⟩3.** (d3) A lift of `ρ_α` to `U(χ)` is a choice `g ↦ V_α(g)` with
`V_α(h)V_α(g) = V_α(hg)` exactly, i.e. with `ω_α ≡ 0`.  By ⟨1⟩2(ii) the
ambiguity in `V_α` is a phase, changing `ω_α` by a coboundary; so such a choice
exists iff `[ω_α] = 0`, and `[ω_α] ∈ H²(G,U(1))` is precisely the obstruction —
the pullback under `ρ_α` of the extension class of
`1 → U(1) → U(χ) → PU(χ) → 1`.
**It is *not* an obstruction to the existence of the window action ⟨3⟩1**,
which exists for every `[ω_α]`: that action is a projective lift, and the
multiplier is exactly what `[ω_α]` measures.
Justification: ⟨1⟩2(ii), ⟨3⟩1--⟨3⟩2.  *(r2 objection 2, conceded.)*

**⟨3⟩4.** Ground truth for the identification of `[ω_α]` with the SPT index:
refs/arxiv-2011.12127, "it is perfectly fine if they transform according to
projective representations, that is, representations up to a phase
`X_gX_h = e^{iω(g,h)}X_{gh}`", classified by `H²_α(G,U(1))`; and
refs/arxiv-1412.5604, "In one dimension, Matrix Product States were used to
completely classify SPT phases via the second cohomology group of their
symmetry group".
**⟨3⟩5. QED.**

**⟨2⟩5. PROVE (e).** *(repairs r1 objection 3.)*
**⟨3⟩1.** By WI the left string leaves `V_α(g_L)` on bond `b` (the `∂_+R`
insertion of `R = [x',b]`, `x' → −∞`) and the right string leaves
`V_α(g_R)^{-1}` (the `∂_-R` insertion of `R = [b+1,y]`, `y → +∞`); both limits
exist by (a).  The composite residue is `V_α(g_L)V_α(g_R)^{-1}`.
Justification: ⟨1⟩3.⟨2⟩4, ⟨2⟩1, D4(c).
**⟨3⟩2.** By (c) this fixes `ω_α` iff `V_α(g_L)V_α(g_R)^{-1} ∈ ℂ^×𝟙`, i.e. iff
`ρ_α(g_L) = ρ_α(g_R)`, i.e. iff `g_Lg_R^{-1} ∈ N_α`.  So the stabiliser is
`S_α`, and `S_α = G_diag` iff `N_α = {e}`.
Justification: ⟨2⟩2, D4(b), ⟨1⟩2(ii).
**⟨3⟩3.** r1's counterexample-in-waiting, supplied by the critic: a `χ=1`
product vacuum with a `ℤ₂` symmetry has `V_α ≡ 1`, so `N_α = G`, `S_α = G×G`,
and the orbit is a **single point** — whereas r1's A1(e) predicted an orbit of
size `|G|`.  The corrected statement reproduces the single point.
Justification: ⟨3⟩2 with `N_α = G`; r1 objection 3.
**⟨3⟩4.** `S_α` is a subgroup (normality of `N_α`), and
`(g_L,g_R) ↦ g_Lg_R^{-1}N_α` is a well-defined bijection `(G×G)/S_α → G/N_α`:
replacing `(g_L,g_R)` by `(g_Ls_L,g_Rs_R)` with `s_Ls_R^{-1} = n ∈ N_α` changes
`g_Lg_R^{-1}` to `g_L n g_R^{-1} = (g_Lng_L^{-1})(g_Lg_R^{-1})`, same coset.
Justification: ⟨3⟩2, normality of `N_α`.
**⟨3⟩5.** `S_α` need not be normal in `G×G` (it is iff `G/N_α` is abelian), and
`G_diag` is normal iff `G` is abelian; hence `𝒜` carries a group structure only
for abelian `G`, while `𝒜_eff = G/N_α` is always a group.
Justification: `(h_1,h_2)(g,g)(h_1,h_2)^{-1} = (h_1gh_1^{-1},h_2gh_2^{-1})`.
**⟨3⟩6. QED.**

**⟨2⟩6. PROVE (f).** By (a) the only residue of a half-infinite string is a
bond insertion; by (c) the endpoint states are in bijection with `PGL(χ)`; by
(d2) the `G`-action on them is left translation by `ρ_α(g)`, hence simply
transitive on `ρ_α(G) ≅ 𝒜_eff`.  The sector label is `(α,α)` throughout since
`g·α = α`.  Non-vacuity: `χ=1` gives a one-point orbit, AKLT with
`G = ℤ₂×ℤ₂` and `V_α ∈ {𝟙,X,Z,XZ}` gives `N_α = {e}` and a **four**-point
orbit of pairwise distinct states (by (c)).
Justification: ⟨2⟩1, ⟨2⟩2, ⟨2⟩4, D9(a), D9(c).  **⟨3⟩1. QED.**

**⟨2⟩7. PROVE (g).** Along a symmetric path `V_α(g;t)` may be chosen
continuously (by refs/arxiv-0802.0447 Lemma 1 it is the eigenvector of `E_u(t)`
for the unique modulus-one eigenvalue, an isolated spectral projection, which
depends continuously on `t` while injectivity and that isolation persist); so
`ω_α(h,g;t)` is continuous and `[ω_α(t)]` is a continuous map into a discrete
set, hence locally constant.
Justification: refs/arxiv-0802.0447 Lemma 1, continuity of isolated spectral
projections, D1(c).  **⟨3⟩1. QED.**

**⟨2⟩8. QED.** (a)--(g) are ⟨2⟩1--⟨2⟩7.  □

**⟨2⟩9. SKETCH — the GNS/physical realisation, and what it is load-bearing for.**

> **BOXED.** *(r1 called this box "not load-bearing"; objection 20 showed that
> is false, and it is retracted.)*
>
> **Not proved:** that `ω_α^{M@b}` is a *normal* state of `π_α(𝔄)''`, i.e. a
> vector state in `H_A`; equivalently that `𝔞_α` acts on the GNS Hilbert space
> rather than on the finite-window spaces `𝒲_{Λ,b}`.  The expected proof uses
> the split property of an exponentially clustering pure MPS state:
> `H_A ≅ H_L ⊗ H_R` across any bond with
> `Ω_A = Σ_{i=1}^{χ}\sqrt{λ_i}|L_i⟩|R_i⟩` of Schmidt rank exactly `χ`,
> whereupon a bond insertion `M` is the vector
> `Σ_{ij}\sqrt{λ_j}M_{ij}|L_i⟩|R_j⟩ ∈ H_A`.  The missing ingredient is the
> infinite-volume Schmidt decomposition with the identification of the Schmidt
> index with the MPS virtual index; at finite windows it is elementary (D1(e)).
>
> **What it is load-bearing for:** the docs/framing.md §1--§2 desideratum —
> a charge algebra with a well-defined (symplectic) action *on the physical
> state space*.  **That desideratum is NOT met by this shard.**  What is proved
> is (d1) on finite-window vectors and (d2) on states.  Any downstream use of
> "the asymptotic charge algebra acting on `H_A`" must cite this box.
>
> **What it is NOT needed for:** (a), (b), (c), (e), (f), (g), WI, A2, G0.  The
> half-infinite operations are used only as maps on states (D3(c)), where (a)
> gives an exact answer.

**⟨2⟩10. Remark (the SPT class is not a Lie-algebra central charge).**
r1 asserted that `[ω_α]` "is" the central extension of the charge algebra and
that `c_α` is its infinitesimal form.  The second half is wrong in the way that
matters: for `𝔥_α` compact semisimple, `H²(𝔥_α,ℝ) = 0` (Whitehead's second
lemma), so `c_α ≡ 0` while `[ω_α]` can be a nontrivial torsion class — the AKLT
edge carries the nontrivial class in `H²(SO(3),U(1)) = ℤ₂` while its spin-½
generators satisfy the ordinary `su(2)` bracket with no central term.
**The lattice SPT anomaly is a group-cohomological multiplier, not a
Lie-algebra central charge.**  This is a genuine disanalogy with the continuum
"centrally extended Poisson charge algebra" of docs/framing.md §2 and must be
stated wherever that framing is invoked.
Justification: r1 objection 7; Whitehead's second lemma; D4(d) caveat.

---

## §5. Pitfalls, scope, and terminology

Sharded to [`corner-a-pitfalls.md`](corner-a-pitfalls.md) (L2).  It is the
campaign-level list and is referenced by all four Corner A shards.

---

## Claim status produced by the Corner A shards (r3)

| claim | status | where |
|---|---|---|
| **WI** | **PROVED**, with window hypothesis (W1) or (W2); the state form carries no phase | this shard, ⟨1⟩3 |
| **A1** | **PROVED**: (a); (b) as an **iff** in `V_α(g)` non-scalar; (c); (d1) **on padded windows only**; (d2); (d3) in the corrected sense (`[ω_α]` obstructs *removing the multiplier*); (e),(f),(g).  **Not** proved: the GNS/edge realisation — SKETCH and **load-bearing** for docs/framing.md (⟨1⟩4.⟨2⟩9).  Completeness of `[ω_α]` cited, not proved | this shard, ⟨1⟩4 |
| **G0** | **PROVED**: (a),(b),(d) for `ξ ∈ 𝔥_α` normal ordered; (c) as the corrected exact finite-window identity, with the clean form only in D12(b); (e) for any `ξ ∈ 𝔤` and finite-range `H`.  The r1 soft-theorem/O7–O9 corollary is **RETRACTED** | [`corner-a-goldstone.md`](corner-a-goldstone.md), ⟨1⟩5--⟨1⟩7 |
| **A2** | **PROVED** for (a)--(d),(f) per fixed `g ∉ H_α`, and (e′) **under hypothesis (T)** (else per `G`-orbit).  r1's (e) is **REFUTED**.  Continuum-`Ω_vac` uniformity is SKETCH and **load-bearing** for Corner B on M1 | [`corner-a-kinks.md`](corner-a-kinks.md), ⟨1⟩8--⟨1⟩10 |

Two claims are carried as negative results: **`A2-orbit-r1` REFUTED** and
**`G0-soft-r1` RETRACTED** (`claims/CLAIMS.md`).
Per-objection dispositions: [`corner-a-r1-response.md`](corner-a-r1-response.md),
[`corner-a-r2-response.md`](corner-a-r2-response.md).
Numerical backing: [`checks/corner_a_check.py`](checks/corner_a_check.py), C0--C11.
