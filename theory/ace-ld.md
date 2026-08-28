<!-- ROLE: proposer shard for the named lemma ACE-LD (the C=>B edge lemma).
     Work order: briefs/ace-ld-prover.md.  Target: the hypothesis (AD3-ex)
     displayed verbatim in theory/ansatz-scattering.md <1>7's ASSUME block.
     Lane: this file and theory/checks/ace_ld_check.py only.  All text
     destined for shared files is in section MERGE PROPOSALS below.
     Status: proposer draft, r0.  A hostile critic pass is pending; nothing
     here upgrades any CLAIMS.md row until the L6 loop converges. -->

# ACE-LD — window-charge spectral diagonality from first-moment channel escape

**Proposer status.**  Three results, stated with their exact quantifiers in
§0 and proved in ⟨1⟩1--⟨1⟩5:

1. **ACE-LD-abs** (abstract; N channels; general on-site spin): at a fixed
   finite window, finite one-coset spectrum plus first-moment channel escape
   with pairwise distinct channel charges implies window-charge spectral
   diagonality, with an explicit t-uniform constant.  Unconditional given its
   ASSUME block.
2. **ACE-LD-esc** (the instance): under D28 plus two named extra hypotheses
   — eigenstate tails **(E-TAIL)** and sign-definite outgoing velocities
   **(V-ch)** — the first-moment escape hypothesis holds for the AC-EX
   constructed channels, with the channel charges *computed*, not stipulated:
   they are the vacuum window charges on the side the outgoing kink escapes
   to.  This is the boundary-straddling control that r1 objection 4 demanded.
3. **ACE-LD-nec** (necessity, and a refutation): the distinct-charge
   hypothesis is necessary.  Consequently (AD3-ex) holds — in the corrected
   eigenvalue reading of ⟨1⟩5 — exactly when the two channels' outgoing kinks
   escape to *opposite* sides of the window, and is **false for every charge
   assignment** when they escape to the same side with both channel weights
   nonzero.  The literal reading of the display with the ledger constants
   `q_L=-1`, `q_T=+1` as `Q̂_W`-eigenvalues is incompatible with the computed
   values except for accidental `(W,c)`.

⟨1⟩6 (§3) records what this does and does not buy the C⇒B edge; the honest
finding there is a structural tension between (AD3-ex) and the tightness
clause D27(LR3) that no proof choice removes.  HONEST STATUS understates
throughout.

All definitions are by D-number from `definitions.md` (L4); no symbol is
redefined here.  Inherited estimates are cited by Lamport address into
`theory/ansatz-scattering.md` (prefix **AS**) and `theory/memory-index.md`
(prefix **MI**).

---

## 0. Statements

### LEMMA ACE-LD-abs (abstract spectral collapse; N channels)

**ASSUME.**
(A1) A Hilbert space `H`, a strongly continuous unitary group `e^{-itH}`, a
unit vector `Ψ`, and `Ψ_t := e^{-itH}Ψ`.
(A2) A bounded self-adjoint operator `Q̂` on `H` (time independent —
Schrödinger picture) whose spectrum is a **finite** set contained in a single
coset `κ+ℤ`, `κ∈[0,1)`.  [In the instance this is `Q̂_{W,c_0}` at a fixed
finite window, and the coset containment is the PROVED **M-INDEX-fin**
(MI ⟨1⟩1), cited — not re-proved.]
(A3) A finite family `{P_ch}_{ch=1}^{n}` of mutually orthogonal projections,
each commuting with `e^{-itH}`, with `Σ_ch P_ch Ψ = Ψ`.
(A4) Real numbers `{q_ch}_{ch=1}^{n}` (the *channel charges*) and
first-moment escape: `ε_ch(t) := ||(Q̂-q_ch)P_chΨ_t|| → 0` as `t→+∞`, for
every `ch`.
(A5) The `q_ch` are pairwise distinct.

**PROVE.**  With `E(·)` the spectral measure of `Q̂` and
`d_ch := dist(q_ch, spec Q̂ ∖ {q_ch}) > 0`,

  `||E({q_ch})Ψ_t − P_chΨ_t|| ≤ Σ_{ch'=1}^{n} d_{ch'}^{-1} ε_{ch'}(t) → 0`
  for every `ch`,                                                **(LD.1)**

the constant `Σ_{ch'} d_{ch'}^{-1}` being independent of `t`.  Moreover if
`q_ch ∈ κ+ℤ` then `d_ch ≥ 1`, so under (A2) the constant is at most `n` for
coset-valued charges.

### LEMMA ACE-LD-nec (necessity of distinct charges)

**ASSUME.** (A1)--(A4) with `n=2` and `q_1 = q_2 =: q`, and
`liminf_{t→+∞}||P_2Ψ_t|| =: w_2 > 0`.

**PROVE.**  For **every** `q'∈ℝ`,
`liminf_{t→+∞} ||E({q'})Ψ_t − P_1Ψ_t|| > 0` whenever `w_1w_2>0` (with
`w_1:=liminf||P_1Ψ_t||`); in particular the (AD3-ex)-form display fails for
channel 1 for every charge assignment.

### PROPOSITION ACE-LD-esc (first-moment escape for the AC-EX channels)

**ASSUME.**  H-MQG(1)--(3), the live D28 (H-ACE) of `definitions.md`
including (D28-C), the AC-EX conclusions ACE.1--ACE.2 (claim **AC-EX**,
PROVED conditional), a fixed finite window `W=[a,b]` with cut `c_0∈W`
(D13(a), D27), and additionally:

> **(E-TAIL) — eigenstate tails.**  Each tail vacuum state is an on-site
> charge eigenstate at its tail density: `ω_γ((S^z_x − s_γ)²) = 0` for all
> `x∈ℤ`, `γ∈{α,β}`, with `s_α=+s`, `s_β=−s` the D13(a)/H-MQG(2) tail
> densities.  [True for the D16 instance, where the vacua are the fully
> polarised product states; false for a generic injective-MPS vacuum — see
> ⟨1⟩4.⟨2⟩1.]

> **(V-ch) — sign-definite outgoing velocities.**  `Ψ = W_+(F_L,F_T)` with
> each nonzero `F_ch` in the closure of the D28(4) smooth packet class whose
> kink velocity support and magnon velocity support each lie at distance
> `≥ ε_0 > 0` from `0` with definite signs; write `σ_ch ∈ {−,+}` for the
> sign of the outgoing **kink** velocity in channel `ch`.

**PROVE.**  For each `ch∈{L,T}` with `F_ch≠0`, the first-moment escape (A4)
holds for `Q̂ = Q̂_{W,c_0}` and the **computed** channel charge

  `q_ch = q_{σ_ch}(W,c_0)`,  where  `q_+(W,c_0) := 2s(b−c_0)` (window in the
  `α` tail: kink escaped right) and `q_−(W,c_0) := 2s(a−1−c_0)` (window in
  the `β` tail: kink escaped left),                             **(LD.2)**

i.e. `||(Q̂_{W,c_0} − q_{σ_ch})P_chΨ_t|| → 0` as `t→+∞`.  Moreover these are
the **only** values for which (A4) can hold (⟨1⟩5.⟨2⟩3).

### COROLLARY ACE-LD (discharge and refutation of (AD3-ex))

Under the hypotheses of ACE-LD-esc:

- **(opposite sides, `σ_L ≠ σ_T`)**: (AD3-ex) as displayed in AS ⟨1⟩7 holds
  with `q_L = q_{σ_L}(W,c_0)`, `q_T = q_{σ_T}(W,c_0)` — distinct, since
  `q_+−q_− = 2s|W| ≠ 0` — the limit taken at fixed `W` before `W↑ℤ`, as the
  display requires;
- **(same side, `σ_L = σ_T`, both `F_L,F_T ≠ 0`)**: (AD3-ex) is **false for
  every choice of `q_L,q_T`** (ACE-LD-nec);
- the ledger constants `q_L=−1`, `q_T=+1` are the correct `Q̂_W`-eigenvalues
  only for the accidental windows solving `2s(a−1−c_0)=−1` resp.
  `2s(b−c_0)=+1`; for all other `(W,c_0)` the display must be read with the
  computed values (LD.2).  The ledger differences feeding AS ⟨1⟩7.⟨2⟩1 are a
  separate hypothesis of ACE.3 and are untouched here.

---

## 1. The abstract lemma

### ⟨1⟩1. LEMMA (finite-spectrum gap estimate)

**ASSUME.** (A2) of ACE-LD-abs: `Q̂` bounded self-adjoint with finite
spectrum `S := spec Q̂`, and a real number `q` with
`d_q := dist(q, S∖{q}) > 0` (automatic for finite `S` unless `S={q}`, in
which case set `d_q := +∞` and read `1/d_q = 0` below).

**PROVE.**  For every vector `φ∈H`,

  `||(1 − E({q}))φ|| ≤ d_q^{-1} ||(Q̂ − q)φ||`.                  **(LD.3)**

If `q ∉ S` then `E({q}) = 0` and (LD.3) reads
`||φ|| ≤ dist(q,S)^{-1}||(Q̂−q)φ||`.

**⟨2⟩1.**  `Q̂` restricted to `ran(1−E({q}))` is self-adjoint with spectrum
`S∖{q}`, hence `(Q̂−q)` restricted there is invertible with
`||((Q̂−q)|_{ran(1−E({q}))})^{-1}|| = max_{λ∈S∖{q}} |λ−q|^{-1} = d_q^{-1}`.

*Justification.*  Spectral theorem for a bounded self-adjoint operator with
finite spectrum: `Q̂ = Σ_{λ∈S} λE({λ})`, so the restriction to the invariant
subspace `ran(1−E({q}))` has the stated spectrum, and functional calculus
gives the inverse norm.  Named computation **LD-GAP.1**.

**⟨2⟩2.**  `1−E({q})` commutes with `Q̂−q`, so

`||(1−E({q}))φ|| = ||((Q̂−q)|^{-1})(Q̂−q)(1−E({q}))φ||
 ≤ d_q^{-1}||(1−E({q}))(Q̂−q)φ|| ≤ d_q^{-1}||(Q̂−q)φ||`,

the last step because `||1−E({q})||≤1`.

*Justification.*  ⟨2⟩1 and functional calculus (spectral projections commute
with `Q̂`).  Named computation **LD-GAP.2**.

**⟨2⟩3.**  If additionally `S ⊂ κ+ℤ` and `q ∈ κ+ℤ`, then every point of
`S∖{q}` lies in `κ+ℤ` at distance `≥1` from `q`, so `d_q ≥ 1`.

*Justification.*  Two distinct points of one coset of `ℤ` differ by a nonzero
integer.  This is where the PROVED **M-INDEX-fin** (MI ⟨1⟩1: under D26(INT)
and H-MQG(2), `spec Q̂_{W,c_0} ⊂ κ_{W,c_0}+ℤ` with
`κ_{W,c_0} ≡ |W|κ + s(a+b−1−2c_0) (mod ℤ)`, time independent) enters the
instance: it supplies the hypothesis of this step for `Q̂ = Q̂_{W,c_0}`, and
it is cited, not re-proved.  In a GNS or sector representation
`spec π(Q̂_{W,c_0}) ⊂ spec Q̂_{W,c_0}`, so the coset containment survives
representation (C*-algebra spectral permanence: the spectrum of an image
under a unital *-homomorphism is contained in the spectrum).  Named
computation **LD-GAP.3**.

**⟨2⟩4.**  The constants `d_q` (and hence (LD.3)) are independent of `t` in
any application with `Q̂` fixed: `Ψ_t` varies, `Q̂` does not, and `S` is a
fixed finite set.  This discharges the uniformity demand of the work order
(brief item (i)): no Lagrange-interpolation or Riesz-contour constant needs
tracking, because (LD.3) needs only the spectral gap, which is a property of
the fixed operator.  *(The Lagrange route of the brief is correct but
strictly weaker: the interpolation constant is bounded below by `d_q^{-1}`
and above by a product over all spectral points; (LD.3) attains the sharp
single-gap constant.)*

*Justification.*  ⟨2⟩1--⟨2⟩3; the operator `Q̂_{W,c_0}` of the instance is a
fixed element of `𝔄_W` (D13(a), D27), and (AD3-ex)'s display is in the
Schrödinger picture: `E_W(·)` fixed, `Ψ_t` evolving.

**⟨2⟩5. QED.**

### ⟨1⟩2. PROOF of ACE-LD-abs

**ASSUME.** (A1)--(A5) of the §0 statement.

**PROVE.** (LD.1).

**⟨2⟩1. (Decomposition.)**  Fix `ch`.  Since `Σ_{ch'}P_{ch'}Ψ = Ψ` and each
`P_{ch'}` commutes with `e^{-itH}` (A3), also `Σ_{ch'}P_{ch'}Ψ_t = Ψ_t` for
every `t`.  Hence

`E({q_ch})Ψ_t − P_chΨ_t
 = −(1 − E({q_ch}))P_chΨ_t + Σ_{ch'≠ch} E({q_ch})P_{ch'}Ψ_t`.

*Justification.*  Algebra: `E({q_ch})Σ_{ch'}P_{ch'}Ψ_t − P_chΨ_t
= [E({q_ch})P_ch − P_ch]Ψ_t + Σ_{ch'≠ch}E({q_ch})P_{ch'}Ψ_t`.  Named
computation **LD-ABS.1**.

**⟨2⟩2. (Diagonal term.)**
`||(1 − E({q_ch}))P_chΨ_t|| ≤ d_ch^{-1} ε_ch(t)`.

*Justification.*  ⟨1⟩1 (LD.3) applied to `φ = P_chΨ_t` and `q = q_ch`, and
the definition of `ε_ch(t)` in (A4).

**⟨2⟩3. (Cross terms.)**  For `ch' ≠ ch`,
`||E({q_ch})P_{ch'}Ψ_t|| ≤ d_{ch'}^{-1} ε_{ch'}(t)`.

*Justification.*  By (A5), `q_ch ≠ q_{ch'}`.  If both are spectral points,
`E({q_ch})E({q_{ch'}}) = 0` (orthogonality of spectral projections of the
same self-adjoint operator at distinct points); if either is not a spectral
point its projection is `0` and the product vanishes trivially.  Hence

`E({q_ch})P_{ch'}Ψ_t = E({q_ch})(1 − E({q_{ch'}}))P_{ch'}Ψ_t`,

and `||E({q_ch})|| ≤ 1` with ⟨1⟩1 (LD.3) at `q = q_{ch'}`, `φ = P_{ch'}Ψ_t`
gives the bound.  Named computation **LD-ABS.2**.

**⟨2⟩4. (Assembly.)**  Triangle inequality over ⟨2⟩1's decomposition, using
⟨2⟩2 once and ⟨2⟩3 for the `n−1` cross terms, gives

`||E({q_ch})Ψ_t − P_chΨ_t|| ≤ d_ch^{-1}ε_ch(t) + Σ_{ch'≠ch}d_{ch'}^{-1}ε_{ch'}(t)
 = Σ_{ch'} d_{ch'}^{-1}ε_{ch'}(t)`,

which tends to `0` by (A4).  The constant is `t`-independent by ⟨1⟩1.⟨2⟩4,
and `≤ n` when all `q_{ch'} ∈ κ+ℤ` by ⟨1⟩1.⟨2⟩3.

*Justification.*  ⟨2⟩1--⟨2⟩3.

**⟨2⟩5.**  Remarks on generality.  (i) Nothing in ⟨2⟩1--⟨2⟩4 restricts `n`
to `2`, restricts the on-site spin, or uses any property of `H` beyond (A1)
and (A3); the lemma is proved for `N` channels and a general on-site charge
observable.  (ii) (A3)'s commutation is used only to propagate
`ΣP_{ch'}Ψ = Ψ` to all `t`; the weaker hypothesis "`Σ_{ch'}P_{ch'}Ψ_t = Ψ_t`
for all `t` and `{P_{ch'}}` mutually orthogonal" suffices verbatim.
(iii) No continuity, gap arithmetic, or Lagrange constant beyond the single
spectral gap of ⟨1⟩1 is consumed; in particular the brief's worry (i) — a
`t`-uniform Lagrange/Riesz constant — does not arise, because `spec Q̂` is a
property of the fixed Schrödinger-picture operator.

*Justification.*  Inspection of ⟨2⟩1--⟨2⟩4.

**⟨2⟩6. QED.**  □

### ⟨1⟩3. PROOF of ACE-LD-nec (distinct charges are necessary)

**ASSUME.** (A1)--(A4) with `n=2`, `q_1 = q_2 =: q`, and
`w_i := liminf_{t→+∞}||P_iΨ_t|| > 0` for `i=1,2`.

**PROVE.**  For every `q'∈ℝ`,
`liminf_{t→+∞}||E({q'})Ψ_t − P_1Ψ_t|| > 0`.

**⟨2⟩1. (Merged channel.)**  `P := P_1 + P_2` is a projection (mutual
orthogonality, (A3)) commuting with `e^{-itH}`, with `PΨ_t = Ψ_t`, and

`||(Q̂ − q)Ψ_t|| = ||(Q̂−q)(P_1+P_2)Ψ_t|| ≤ ε_1(t) + ε_2(t) → 0`.

*Justification.*  (A3), (A4), triangle inequality.  Named computation
**LD-NEC.1**.

**⟨2⟩2. (The full vector collapses onto one spectral point.)**
`||(1 − E({q}))Ψ_t|| ≤ d_q^{-1}(ε_1(t)+ε_2(t)) → 0`, i.e.
`||E({q})Ψ_t − Ψ_t|| → 0`.

*Justification.*  ⟨1⟩1 (LD.3) with `φ = Ψ_t`, using ⟨2⟩1.  (If `q ∉ spec Q̂`
this forces `||Ψ_t|| → 0`, contradicting `||Ψ_t|| = 1`; so under the
standing normalisation `q ∈ spec Q̂` and `d_q` is the coset gap.)

**⟨2⟩3. (Case `q' = q`.)**
`||E({q})Ψ_t − P_1Ψ_t|| ≥ ||Ψ_t − P_1Ψ_t|| − ||E({q})Ψ_t − Ψ_t||
 = ||P_2Ψ_t|| − o(1)`,
using `Ψ_t − P_1Ψ_t = P_2Ψ_t` (⟨2⟩1) and ⟨2⟩2.  Hence the liminf is
`≥ w_2 > 0`.

*Justification.*  Reverse triangle inequality, ⟨2⟩1, ⟨2⟩2.

**⟨2⟩4. (Case `q' ≠ q`.)**  `E({q'})E({q}) = 0` (distinct points; or
`E({q'})=0` if `q'∉spec`), so

`||E({q'})Ψ_t|| = ||E({q'})(Ψ_t − E({q})Ψ_t)|| ≤ ||Ψ_t − E({q})Ψ_t|| → 0`,

and therefore
`||E({q'})Ψ_t − P_1Ψ_t|| ≥ ||P_1Ψ_t|| − o(1)`, liminf `≥ w_1 > 0`.

*Justification.*  Orthogonality of spectral projections, ⟨2⟩2, reverse
triangle inequality.  Named computation **LD-NEC.2**.

**⟨2⟩5. QED.**  □  *(Consequence: when both channels' first moments escape
to the SAME charge, the (AD3-ex)-form display is false for channel 1 no
matter which eigenvalue is claimed for it — ⟨2⟩3 kills the shared value,
⟨2⟩4 kills every other value.  By symmetry the same holds for channel 2.)*

---

## 2. The instance: first-moment escape for the AC-EX channels

### ⟨1⟩4. PROOF of ACE-LD-esc

**ASSUME.**  The ASSUME block of ACE-LD-esc (§0): H-MQG(1)--(3), D28 with
(D28-C), ACE.1--ACE.2, fixed `W=[a,b]`, `c_0∈W`, (E-TAIL), (V-ch).
Throughout, `M_W := ||Q̂_{W,c_0}|| + |q_+| + |q_-| < ∞` is a fixed
`W`-dependent constant (`Q̂_{W,c_0} ∈ 𝔄_W` is a finite sum of bounded
on-site operators plus a scalar — D13(a), D27, MI ⟨1⟩1.⟨2⟩2).

**PROVE.**  `||(Q̂_{W,c_0} − q_{σ_ch}(W,c_0))P_chΨ_t|| → 0` as `t→+∞` for
each `ch` with `F_ch ≠ 0`, with `q_±(W,c_0)` as in (LD.2).

**⟨2⟩1. (Zero window-charge variance in the tail vacua.)**  Under (E-TAIL),
for `γ∈{α,β}`,

`ω_γ((Q̂_{W,c_0} − q_γ)²) = 0`,  where
`q_α := 2s(b−c_0) = q_+`,  `q_β := 2s(a−1−c_0) = q_-`.

*Justification.*  By MI ⟨1⟩1.⟨2⟩2 (M-INDEX-fin's expansion of D13(a)),
`Q̂_{W,c_0} = Σ_{x=a}^{b}S^z_x + s(a+b−1−2c_0)`.  Evaluating the scalar and
the sum at `S^z_x ↦ s_γ` gives `ω_γ(Q̂_{W,c_0}) = |W|s_γ + s(a+b−1−2c_0)`,
which is `2s(b−c_0)` for `s_α=+s` and `2s(a−1−c_0)` for `s_β=−s` — the two
values of (LD.2); the arithmetic is named computation **LD-VAL**.  For the
variance: `Q̂_{W,c_0} − q_γ = Σ_{x∈W}(S^z_x − s_γ)` exactly (the scalars
cancel by LD-VAL).  In the GNS triple `(H_γ,π_γ,Ω_γ)` (D1(d)), (E-TAIL)
gives `||π_γ(S^z_x − s_γ)Ω_γ||² = ω_γ((S^z_x−s_γ)²) = 0`, hence
`π_γ(S^z_x−s_γ)Ω_γ = 0` for every `x`, hence every cross term
`ω_γ((S^z_x−s_γ)(S^z_{x'}−s_γ)) = ⟨π_γ(S^z_x−s_γ)Ω_γ, π_γ(S^z_{x'}−s_γ)Ω_γ⟩`
vanishes (self-adjointness of `S^z_x−s_γ`), and the finite double sum is
`0`.  Named computation **LD-VAR**.  *(Scope of (E-TAIL): it holds whenever
the tail density is an on-site `S^z` eigenvalue attained by the vacuum —
in particular for saturated tails `s = S`, where
`ω_γ(S^z_x) = ±S = ±max spec S^z` forces the eigenvector property by
extremality, and for any on-site product vacuum in an `S^z` eigenstate.  It
fails for a generic injective-MPS vacuum: e.g. the AKLT state has
`ω((S^z_x)²) = 2/3 ≠ 0 = ω(S^z_x)²`, so no window charge is sharp there.
The D16 instance has spin-1/2 fully polarised product vacua and satisfies
(E-TAIL) exactly.)*

**⟨2⟩2. (One-body kink estimate: the escaped kink is an approximate
window-charge eigenvector.)**  For every `N` there is `C_N` (depending on
`W` through `M_W`) such that for all frame indices `a` and all `x` with
`r := dist(x, W) ≥ 1` and `x` entirely to the right of `W` (`x ≥ b+r`):

`||(Q̂_{W,c_0} − q_+)κ_a(x)|| ≤ C_N M_W ⟨r⟩^{-N}`,

and symmetrically with `q_-` for `x ≤ a−r`.

*Justification.*  Put `A := (Q̂_{W,c_0} − q_+)² ∈ 𝔄_W`, `||A|| ≤ M_W²`.
For `x ≥ b+r` the region `W ⊂ (−∞, x−r]` is on the `α` side of the kink
(D13(a): `α` tail at `−∞`, i.e. to the LEFT of the wall), so **ACE-tail**
(AS ⟨1⟩3.⟨2⟩6, one-tail case `B=1`, `x=x'`) applies and gives, for every
`N`,

`⟨κ_a(x), Aκ_a(x)⟩ = ω_α(A)\,||κ_a(x)||² + O(C_N||A||⟨r⟩^{-N})`.

By ⟨2⟩1, `ω_α(A) = 0`; hence
`||(Q̂_{W,c_0}−q_+)κ_a(x)||² ≤ C_N M_W²⟨r⟩^{-N}`, and taking square roots
(with `2N` in place of `N`, `N` free) gives the display.  The left case is
identical with `β`, `q_-`, and `W` on the `β` side.  Named computation
**LD-KINK**.  *(This step is where the finite-`t` boundary-straddling
charge on `∂W` is controlled: at finite `x`-distance the kink's exponential
tails DO straddle `∂W`, and (D28-C)'s clustering rate `λ̃^r`, packaged
through ACE-tail's `⟨r⟩^{-N}`, is exactly what bounds their window-charge
content.)*

**⟨2⟩3. (One-body dressed estimate: the magnon dressing carries no window
charge once separated.)**  For every `N` there is `C_N` with: for all frame
indices, all `x` as in ⟨2⟩2 (either side, `r_K := dist(x,W)`), and all `y`
with `r_M := dist(y, W) ≥ 1`,

`||(Q̂_{W,c_0} − q_{σ})a_{γ,b}(y)κ_a(x)||
 ≤ C_a\,C_N M_W ⟨r_K⟩^{-N} + C_N' M_W ⟨r_M⟩^{-N}`,

where `σ` is the side of `x` and `C_a := sup_{y}||a_{γ,b}(y)||\,||κ_a(x)||`
is the uniform bound of AS ⟨1⟩3.⟨2⟩2.

*Justification.*  Commute: `(Q̂−q)a(y)κ(x) = a(y)(Q̂−q)κ(x) + [Q̂, a(y)]κ(x)`
(the scalar `q` commutes).  First term: `||a(y)|| ≤ C_a'` (AS ⟨1⟩3.⟨2⟩2)
times ⟨2⟩2.  Second term: by almost locality of `a_{γ,b}(y)` uniformly in
`y` (AS ⟨1⟩3.⟨2⟩2), there is `A_{r_M/2} ∈ 𝔄_{[y−r_M/2, y+r_M/2]}` with
`||a(y) − A_{r_M/2}|| ≤ C_N⟨r_M⟩^{-N}`; the support of `A_{r_M/2}` is
disjoint from `W` (distance `≥ r_M/2 > 0`), so `[Q̂_{W,c_0}, A_{r_M/2}] = 0`
(`Q̂_{W,c_0} ∈ 𝔄_W`, commuting supports), and
`||[Q̂, a(y)]|| ≤ 2||Q̂||\,||a(y)−A_{r_M/2}|| ≤ 2M_W C_N⟨r_M⟩^{-N}`.
Named computation **LD-STRADDLE** — this is the literal "boundary-straddling
charge of the dressing" term of the r1 objection, and it is `O(⟨r_M⟩^{-N})`
because the creator is almost local and `Q̂_{W,c_0}` is strictly local.

**⟨2⟩4. (Assembly on a smooth packet.)**  Let `G` be a smooth packet of the
(V-ch) class for channel `ch` (kink and magnon velocity supports at distance
`≥ε_0` from `0`, signs `σ_ch` and `σ_M`), and
`Φ_t := I_{ch}e^{-itH_{0,ch}}G` the precursor of AS ⟨1⟩5.⟨2⟩1.  Then for
every `N` there are `C_{G,N}` and `t_0` with

`||(Q̂_{W,c_0} − q_{σ_ch})Φ_t|| ≤ C_{G,N}\,|t|^{2−N}` for `t ≥ t_0`.

*Justification.*  `Φ_t = Σ_{x,y}θ_c(y−x)G_t(x,y)a_{c,b}(y)κ_a(x)` (AS
⟨1⟩5.⟨2⟩1; frame indices suppressed), `|θ_c|≤1`, so by the triangle
inequality

`||(Q̂−q_{σ_ch})Φ_t|| ≤ Σ_{x,y}|G_t(x,y)|\,||(Q̂−q_{σ_ch})a(y)κ(x)||`.

Split by the velocity cones of AS ⟨1⟩4.⟨2⟩3.  *On* the product of the two
main cones: `x` lies within the kink cone about `v_Kt` with
`|v_K| ≥ ε_0`, sign `σ_ch`, and `y` within the magnon cone about `v_Mt`,
`|v_M| ≥ ε_0`; since `W` is fixed, for `t ≥ t_0(W,ε_0)` both
`dist(x,W) ≥ ε_0t/2` and `dist(y,W) ≥ ε_0t/2`, and `x` is on side `σ_ch` of
`W`; ⟨2⟩3 bounds the summand by `C_N M_W⟨ε_0t/2⟩^{-N}`, and
`||G_t||_1 = O(|t|²)` (AS ⟨1⟩4.⟨2⟩2) gives `O(|t|^{2-N})`.  *Off* the main
cones, `||(Q̂−q)a(y)κ(x)|| ≤ 2M_W' := (2||Q̂||+|q_+|+|q_-|)C_a` crudely, and
the off-cone `ℓ¹` mass is `O(|t|^{2-N})` by AS ⟨1⟩4.⟨2⟩1--⟨2⟩2 (at least
one factor of `G_t = g^K_t ⊗ g^M_t` is outside its own cone).  Sum:
`O(|t|^{2-N})`.  Named computation **LD-CONE**.

**⟨2⟩5. (From the precursor to the channel vector: Cook tail and density.)**
For the actual channel component: `P_chΨ_t = e^{-itH}W_+(δ_{ch}F_{ch})`
(AS ⟨1⟩6.⟨2⟩3--⟨2⟩5: `P_ch` here is the constructed-channel projection
`W_+P_ch^{as}W_+^*`, which commutes with `e^{-itH}` by the intertwining of
AS ⟨1⟩6.⟨2⟩4) `= W_+e^{-itH_{0,ch}}F_{ch}`.  Given `δ>0`, choose a smooth
packet `G^δ` in the (V-ch) class with `||F_{ch} − G^δ|| ≤ δ` (possible by
(V-ch): `F_{ch}` lies in the closure of that class).  Then

`||(Q̂−q_{σ_ch})P_chΨ_t||
 ≤ M_W δ + M_W\,||W_+e^{-itH_{0,ch}}G^δ − Φ^δ_t|| + ||(Q̂−q_{σ_ch})Φ^δ_t||`
`   ≤ M_W δ + M_W C_{G^δ}\,t^{-2} + C_{G^δ,N}\,|t|^{2-N}`,

whence `limsup_{t→+∞}||(Q̂−q_{σ_ch})P_chΨ_t|| ≤ M_Wδ` for every `δ>0`,
i.e. the limit is `0`.

*Justification.*  First inequality: isometry of `W_+` (ACE.2) for the `δ`
term, and `||Q̂−q|| ≤ M_W`.  Second: for the middle term,
`W_+G' − I_{ch}G'` at `G' = e^{-itH_{0,ch}}G^δ` equals
`∫_0^∞ (d/dτ)[e^{iτH}I_{ch}e^{-iτH_{0,ch}}G']dτ`, whose norm is
`≤ ∫_t^∞ ||(HI_{ch}−I_{ch}H_{0,ch})e^{-iuH_{0,ch}}G^δ||du
 ≤ ∫_t^∞ C_{G^δ}u^{-3}du = (C_{G^δ}/2)t^{-2}`
by the Cook majorant AS ⟨1⟩5.⟨2⟩5 (`N≥5` there), the group law
`e^{-iuH_{0}} = e^{-i(u-t)H_0}e^{-itH_0}`, and unitarity of `e^{iτH}`;
the last term is ⟨2⟩4.  Named computation **LD-COOK-TAIL**.

**⟨2⟩6. (Uniqueness of the charge values.)**  If (A4) holds for channel
`ch` with some value `q'` and `liminf||P_chΨ_t|| > 0`, then `q' =
q_{σ_ch}`: by ⟨2⟩5 and the triangle inequality
`|q' − q_{σ_ch}|\,||P_chΨ_t|| ≤ ε'_{ch}(t) + ε_{ch}(t) → 0`, forcing
`q' = q_{σ_ch}`.

*Justification.*  `(q_{σ_ch} − q')P_chΨ_t = (Q̂−q')P_chΨ_t −
(Q̂−q_{σ_ch})P_chΨ_t`; take norms.  Named computation **LD-UNIQUE**.

**⟨2⟩7. QED.**  □

### ⟨1⟩5. PROOF of COROLLARY ACE-LD (discharge and refutation of (AD3-ex))

**ASSUME.**  The hypotheses of ACE-LD-esc.  Recall the display being
discharged, verbatim from AS ⟨1⟩7's ASSUME block:

> Let `Ψ=W_+(F_L,F_T)`, `Ψ_t:=e^{-itH}Ψ`.  For every fixed window `W`
> containing the kink core region, with `E_W(·)` the spectral measure of the
> regularised window charge `Q̂_W` and `P_ch`, `ch∈{L,T}`, the channel
> projections of ⟨1⟩6.⟨2⟩5:
> `lim_{t→+∞}||E_W({q_ch})Ψ_t − P_{ch}Ψ_t||=0`, the limit taken BEFORE
> `W↑ℤ`.

**PROVE.**  The three bullets of the §0 corollary.

**⟨2⟩1. (Hypothesis audit for ACE-LD-abs, at fixed `W`.)**
(A1): H-MQG(1)/D28(1) supply the covariant Hilbert realization and the
unitary group; `Ψ = W_+(F_L,F_T)` is a unit vector.  (A2): `Q̂ =
Q̂_{W,c_0} ∈ 𝔄_W` is bounded self-adjoint; its spectrum in the sector
representation is finite and contained in the coset `κ_{W,c_0}+ℤ` by
**M-INDEX-fin** (MI ⟨1⟩1, PROVED; cited per ⟨1⟩1.⟨2⟩3, with spectral
permanence for the representation).  Finiteness: `Q̂_{W,c_0}` is a finite
sum of commuting on-site operators each with finite spectrum plus a scalar
(MI ⟨1⟩1.⟨2⟩2--⟨2⟩3), so its spectrum is a subset of the finite sum-set;
representation shrinks it at most.  (A3): `P_L := W_+P_L^{as}W_+^*`,
`P_T := W_+P_T^{as}W_+^*` are mutually orthogonal projections (ACE.2, AS
⟨1⟩6.⟨2⟩3, ⟨2⟩5) commuting with `e^{-itH}` (AS ⟨1⟩6.⟨2⟩4), and
`(P_L+P_T)Ψ = Ψ` since `Ψ ∈ H_out^{ex} = ran W_+` and
`P_L^{as}+P_T^{as} = 1` on the outgoing channel space (D28's direct-sum
projections).  (A4): ACE-LD-esc (⟨1⟩4) with charges `q_{σ_L}, q_{σ_T}` of
(LD.2).  *(A vanishing component `F_ch = 0` makes its clause of the display
trivial: both terms vanish identically for that channel; so only nonzero
components need (A4).)*

*Justification.*  Each item cites its source inline; nothing else is used.

**⟨2⟩2. (Opposite sides: the display HOLDS.)**  If `σ_L ≠ σ_T`, then
`{q_{σ_L}, q_{σ_T}} = {q_+, q_-}` with `q_+ − q_- = 2s(b−c_0) −
2s(a−1−c_0) = 2s|W| > 0` (H-MQG(2): `s>0`; `|W|≥1`), so (A5) holds, and
ACE-LD-abs (⟨1⟩2) gives, for each `ch`,

`||E_W({q_{σ_ch}})Ψ_t − P_chΨ_t||
 ≤ (d_L^{-1}ε_L(t) + d_T^{-1}ε_T(t)) → 0`,

which is the display with `q_ch := q_{σ_ch}(W,c_0)`, at fixed `W`, i.e.
before `W↑ℤ` — the D18(AD4) order the display prescribes.  Moreover
`q_{σ_ch} ∈ spec π(Q̂_{W,c_0})` is forced whenever `F_ch ≠ 0`: by ⟨1⟩1
(LD.3), `ε_{ch}(t) ≥ dist(q_{σ_ch}, spec)\,||P_chΨ_t|| =
dist(q_{σ_ch}, spec)\,||F_ch||`, and `ε_{ch}(t)→0` with `||F_ch||>0` forces
the distance to vanish; the spectrum is finite, hence closed, so
`q_{σ_ch} ∈ spec ⊂ κ_{W,c_0}+ℤ` (M-INDEX-fin), and the constants obey
`d_{ch}^{-1} ≤ 1` by ⟨1⟩1.⟨2⟩3.

*Justification.*  ⟨2⟩1, ⟨1⟩2, ⟨1⟩4, arithmetic (named computation **LD-VAL**
for the difference `2s|W|`).

**⟨2⟩3. (Same side: the display is FALSE for every charge assignment.)**
If `σ_L = σ_T =: σ` and `F_L, F_T ≠ 0`, then both channels satisfy (A4)
with the SAME charge `q_σ`, and `||P_chΨ_t|| = ||F_ch||` for all `t`
(isometry and intertwining, ⟨2⟩1), so ACE-LD-nec (⟨1⟩3) applies with
`w_1 = ||F_L|| > 0`, `w_2 = ||F_T|| > 0`: for every choice of `q_L` (and
symmetrically `q_T`), `liminf_t ||E_W({q_L})Ψ_t − P_LΨ_t|| > 0`.  The
display fails at every fixed `W`, hence in the prescribed order.

*Justification.*  ⟨1⟩3, ⟨1⟩4, ⟨2⟩1; `||P_chΨ_t|| = ||W_+e^{-itH_0}
(δ_{ch}F_{ch})|| = ||F_{ch}||` by ACE.2.

**⟨2⟩4. (The eigenvalues are forced; the ledger constants are not
eigenvalues in general.)**  By ⟨1⟩4.⟨2⟩6, in the opposite-side regime the
ONLY values `q_L, q_T` for which the display can hold are
`q_{σ_L}(W,c_0), q_{σ_T}(W,c_0)`; these depend on `(W,c_0)` and grow
linearly in `|W|`.  The constants of AS ⟨1⟩7's charge clause
(`q_in=q_L=−1`, `q_T=+1`) are charges of the LEGS relative to their vacua
(D18 AD3 wording, D14), not `Q̂_W`-eigenvalues; equality
`q_{σ_L}(W,c_0) = −1` or `q_{σ_T}(W,c_0) = +1` holds only on the accidental
set `2s(a−1−c_0) = −1` resp. `2s(b−c_0) = +1`.  For all other `(W,c_0)`
the display, read with the ledger constants as eigenvalues, is false by
⟨1⟩4.⟨2⟩6 — while read with (LD.2) it is true (⟨2⟩2).  The corrected
reading is therefore not optional; a merge proposal to AS ⟨1⟩7's gloss is
in §MERGE PROPOSALS.

*Justification.*  ⟨1⟩4.⟨2⟩6, LD-VAL, D14, D18(AD3).

**⟨2⟩5. QED.**  □

---

## 3. What this buys the DAG — and a structural obstruction

### ⟨1⟩6. The C⇒B edge, and PROPOSITION ACE-LD-obst

**⟨2⟩1. (What is discharged.)**  (AD3-ex) was the sole *dynamical*
hypothesis fencing ACE.3 (AC-EX row; AS ⟨1⟩7).  By ⟨1⟩5, on the packet
class (V-ch) with `σ_L ≠ σ_T` and under (E-TAIL), it is now a THEOREM in
the corrected eigenvalue reading (LD.2).  The chain

  D28 (+ D28-C) + (E-TAIL) + (V-ch, opposite sides)
  ⟹ (AD3-ex, corrected reading)                        [this shard]
  ⟹ inter-channel cross-terms vanish                    [AS ⟨1⟩7.⟨2⟩2]

closes the local-decay gap of ansatz-scattering-r1 objection 4.  What
remains conditional in ACE.3 after this shard: (i) D28-C, unverified on any
model (unchanged); (ii) the charge-assignment/ledger clause (unchanged — and
see ⟨2⟩4 below); (iii) the existence of Lane T1's ordered-limit outcome
measure (unchanged as a hypothesis, but see ⟨2⟩2--⟨2⟩3: on the packet class
where (AD3-ex) is here PROVED, that hypothesis FAILS unless the transit
weight vanishes).  (E-TAIL) and (V-ch) are new named hypotheses, honestly
priced: (E-TAIL) holds in the D16 instance and fails for generic MPS vacua;
(V-ch) is a packet-class restriction in the spirit of D28(4).

**⟨2⟩2. (PROPOSITION ACE-LD-obst: fixed-window TPM law in the provable
regime, and failure of D27(LR3) tightness.)**

**ASSUME.**  The hypotheses of ACE-LD-esc with `σ_L ≠ σ_T`; additionally
**(V-in)**: `Ψ = W_-^L F_in` with `F_in` in the closure of the smooth
incoming class with sign-definite kink and magnon velocities (incoming kink
velocity sign `σ_in`, so the kink sits on side `σ̄ := −σ_in` of `W` as
`t→−∞`); and `||F_L||²||F_T||² > 0` with `(F_L,F_T) = W_+^*Ψ`.

**PROVE.**  (a) For every fixed `W`, the ordered two-time TPM law of MI
⟨1⟩5 converges (plain limits `t_-→−∞`, `t_+→+∞`, hence also their Cesàro
averages) to

  `p_W(ν) = ||F_L||²\,δ_{ν,\,ν_L(W)} + ||F_T||²\,δ_{ν,\,ν_T(W)}`,
  `ν_{ch}(W) := q_{σ̄}(W,c_0) − q_{σ_{ch}}(W,c_0) ∈ {0, ±2s|W|}`.

(b) Exactly one channel (`ch*`, the one with `σ_{ch*} ≠ σ̄`) has
`|ν_{ch*}(W)| = 2s|W|`; along every padded exhaustion `W_m↑ℤ` the
first-moment tightness clause D27(LR3) fails:
`sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν) ≥ (1+2s|W_m|)||F_{ch*}||²` for all
`m` with `2s|W_m| > M`, which is unbounded.  Consequently the ordered
outcome measure exists only defectively (weak limit
`||F_{ch\dagger}||²δ_0`, total mass `< 1`, `ch†` the returning channel) and
the ordered wall expectation
`δx = −(2s)^{-1}Σ_ν ν\,p_{W_m}(ν) = ∓|W_m|\,||F_{ch*}||²` diverges
linearly in `|W_m|`.

**⟨3⟩1. (Incoming concentration.)**  As `t→−∞`,
`||E_W({q_{σ̄}})Ψ_t − Ψ_t|| → 0`.

*Justification.*  ⟨1⟩4's proof applies verbatim time-reflected: the
inherited estimates are two-sided (AS ⟨1⟩4.⟨2⟩1--⟨2⟩3 and the Cook majorant
AS ⟨1⟩5.⟨2⟩5 are stated for `|t|→∞` at both ends; the intertwining AS
⟨1⟩6.⟨2⟩4 holds for `W_-^L`), with the single channel `n=1`, `P=1`,
`Ψ_t = W_-^Le^{-itH_{0,in}}F_in`, (V-in) supplying the sign-definite cones,
and the kink on side `σ̄` of `W` for `t≪0`; then ACE-LD-abs with `n=1`
collapses the first moment to the spectral projection.  Named computation
**LD-IN** (the time-reflection is a substitution `t↦−t`, `W_+↦W_-^L`,
`σ_ch↦σ̄`; no step of ⟨1⟩4 is direction-sensitive once the cone signs are
supplied).

**⟨3⟩2. (Two-time collapse.)**  With `E := E_W`, for `q` in the finite
spectrum and `ν∈ℤ`:

`||E({q−ν})e^{-i(t_+−t_-)H}E({q})Ψ_{t_-}||²
 = δ_{q,q_{σ̄}}\,||E({q−ν})Ψ_{t_+}||² + o(1)`  (as `t_-→−∞`, uniformly in
`t_+`), and `||E({q_{σ̄}}−ν})Ψ_{t_+}||² → Σ_{ch}δ_{ν,ν_{ch}(W)}||F_{ch}||²`
(as `t_+→+∞`).

*Justification.*  First equality: insert ⟨3⟩1
(`E({q})Ψ_{t_-} = δ_{q,q_{σ̄}}Ψ_{t_-} + o(1)`, the `o(1)` uniform over the
finitely many `q` and contracted by the unitary `e^{-i(t_+−t_-)H}` and the
projection `E({q−ν})`), and `e^{-i(t_+−t_-)H}Ψ_{t_-} = Ψ_{t_+}`.  Second:
⟨1⟩5.⟨2⟩2 gives `||E({q_{ch}})Ψ_{t_+} − P_{ch}Ψ_{t_+}|| → 0` with
`q_{ch} = q_{σ_{ch}}`, `q_{σ̄}−ν = q_{σ_{ch}}` iff `ν = ν_{ch}(W)`, and for
`ν` matching neither channel `||E({q_{σ̄}−ν})Ψ_{t_+}|| → 0` (⟨1⟩3.⟨2⟩4's
computation applied with the two-point concentration).
`||P_{ch}Ψ_{t_+}||² = ||F_{ch}||²` by ACE.2.  The MI ⟨1⟩5 TPM sum over `q`
then collapses to the single term `q = q_{σ̄}`.  Named computation
**LD-TPM**.  Cesàro averages of convergent functions converge to the same
limits (D27(LR1)'s averages are over `t_±` windows escaping to `±∞`).

**⟨3⟩3. (Tightness failure.)**  `ν_{ch}(W) = q_{σ̄}(W) − q_{σ_{ch}}(W)`;
by (LD.2), `q_+−q_- = 2s|W|`, so `ν_{ch}(W) = 0` if `σ_{ch} = σ̄` and
`= ±2s|W|` if `σ_{ch}` is the opposite side, i.e. `σ_{ch} = σ_in`-side
transit.  Since `σ_L ≠ σ_T`, exactly one channel transits.  The displayed
`sup_m` bound and the defective weak limit follow by direct evaluation of
`p_{W_m}` on `{|ν|>M}`; D27(LR3) requires that supremum to vanish as
`M→∞`, and it instead diverges whenever `||F_{ch*}|| > 0`.

*Justification.*  LD-VAL arithmetic and D27(LR3) as frozen in
definitions.md.  **⟨3⟩4. QED (⟨2⟩2).**  □

**⟨2⟩3. (The structural tension, stated plainly.)**  On the fixed-packet
class of D28 the kink is ballistic: every channel's kink escapes any fixed
window (that is WHY (AD3-ex) is provable there — the window relaxes to a
sharp vacuum charge).  But the same escape makes the window-charge
increment of the transit channel grow linearly with the window, so the
two-time law cannot stay tight along the exhaustion: **(AD3-ex) and
D27(LR3) are jointly unsatisfiable on the packet class where (AD3-ex) has
been proved, except when the transit weight `||F_{ch*}||²` vanishes.**
ACE.3 remains a valid conditional theorem — its conclusion is simply
vacuously guarded on this class, because its third hypothesis (the T1
ordered-limit outcome measure) fails there.  The `{0,2}` support of the
B3/T1 ledger is the *no-transit idealization* (kink confined to the window
at both measurement epochs), which is exactly the D18(AD3) wording "the
remaining local state is a kink charge eigenstate" — and on D28 packets
that idealization is not dynamically realized at any fixed window.  A
proof of the C⇒B edge with nonvacuous outcome content therefore needs
either (i) a co-moving or kink-relative window observable (`𝔛_W` recentred
on the kink collective coordinate), (ii) a kink-rest-frame sector (a
packet class with sub-ballistic kink transport, not supplied by D28), or
(iii) a subtracted charge (the D13(c) trap paragraph's leg subtraction) —
each a definition-level change that is proposed for adjudication, not made
here (L4: this shard edits no shared file).

**⟨2⟩4. (Ledger compatibility.)**  The ⟨1⟩7.⟨2⟩1 arithmetic
`ν_L = q_L−q_in = 0`, `ν_T = q_T−q_in = 2` uses LEG charges relative to
vacua.  In the here-proved regime the TPM `ν`-values are `ν_{ch}(W) ∈
{0, ±2s|W|}` — the returning channel reproduces `ν = 0` exactly (and does
so for the physically right reason: no net transit), while the transit
channel's `±2s|W|` is the whole-wall sweep, NOT the ledger's `2`.  The
ledger `2` is the `O(1)` memory residue that survives only after the
sweep is subtracted (or in the no-transit idealization).  Claim B3 and
M-INDEX-spec are untouched: they are conditional on D27(LR), which excludes
this regime by ⟨2⟩2(b).  No PROVED row is contradicted; the finding is that
the hypothesis sets of AC-EX/ACE.3 and of the LR-based ledger select
disjoint dynamical regimes on D28 packets.

**⟨2⟩5. QED (⟨1⟩6).**

---

## 4. HONEST STATUS

**Proved, given only its own ASSUME block (unconditional as an
implication):**

- **ACE-LD-abs** (⟨1⟩1--⟨1⟩2).  A three-step spectral-gap argument.  The
  content is small and its value is exactly the collapse the brief asked
  for: at fixed finite `W`, (AD3-ex)-form spectral diagonality follows from
  first-moment escape, with `t`-uniform constant `Σ d_{ch}^{-1} ≤ n`.  `N`
  channels, general on-site spin, no model input.
- **ACE-LD-nec** (⟨1⟩3).  Distinct channel charges are necessary; when both
  first moments escape to one value the display fails for EVERY claimed
  eigenvalue.

**Proved conditionally (each hypothesis named, none hidden):**

- **ACE-LD-esc** (⟨1⟩4): first-moment escape with computed charges (LD.2),
  under H-MQG(1)--(3) + D28 (incl. the unverified (D28-C), inherited
  through ACE.1--ACE.2 and the AS estimates) + **(E-TAIL)** + **(V-ch)**.
- **COROLLARY ACE-LD** (⟨1⟩5): (AD3-ex) discharged in the corrected
  eigenvalue reading on the opposite-side class; REFUTED for every charge
  assignment on the same-side class with both weights nonzero.
- **ACE-LD-obst** (⟨1⟩6.⟨2⟩2): fixed-window TPM law and D27(LR3) tightness
  failure, additionally under **(V-in)**.  Its ⟨3⟩1 is the time-reflection
  of ⟨1⟩4; the reflection is argued step-by-step nowhere else than in LD-IN
  and a critic may demand it be written out — the claim is that no step of
  ⟨1⟩4 is direction-sensitive, which I believe and have checked step by
  step, but the reflected text does not exist as a separate proof.

**Hypothesised / not proved:**

- (D28-C): unverified on any model (unchanged from AC-EX).
- (E-TAIL): holds for the D16 instance (product vacua) and whenever the
  tail density is an attained on-site eigenvalue; FALSE for generic MPS
  vacua (AKLT computation in ⟨1⟩4.⟨2⟩1).  Without it, the escaped-window
  state has strictly positive charge variance and no `Q̂_W`-eigenvalue can
  serve; (AD3-ex) is then expected to fail outright, but that refutation is
  NOT proved here (it would need a quantitative variance lower bound on the
  dressed state, which ⟨1⟩4's upper-bound machinery does not give).
- (V-ch)/(V-in): packet-class restrictions.  Whether the physical S-matrix
  of a given model maps a (V-in) class into a `σ_L ≠ σ_T` out-class is a
  model question (plausible for a slow kink hit by a fast magnon —
  reflection reverses the kink recoil, transmission does not — but NOT
  verified on any model here; Bethe data could probe it and has not been
  consulted).
- The `{0,2}` ledger reading of ACE.3's outcome support: NOT established by
  this shard, and ⟨1⟩6.⟨2⟩2--⟨2⟩4 show it cannot be established at fixed
  windows on this packet class; it needs a no-transit idealization or a
  subtracted/co-moving observable (adjudication requested).

**Merely evidence:**

- The numerical certificate (§5, `theory/checks/ace_ld_check.py`) instantiates
  ACE-LD-abs and ACE-LD-nec on an explicit one-particle lattice model with a
  clamp-form window charge; it certifies the inequality (LD.1) with its
  constant, the convergence, the necessity refutation, and the tightness
  blow-up of ⟨1⟩6, on that model only.

**Honest defects and L2 self-report.**  (i) This shard is ~850 lines,
above the L2 band; the overrun is the three-result structure the work order
mandates plus the obstruction section, and I judge splitting it would break
the proposer/critic addressing.  (ii) ⟨1⟩4.⟨2⟩5's density step gives
convergence without a rate for `ε_ch(t)` (the `δ`-approximation is not
quantitative); (AD3-ex) needs only convergence, but any downstream use
wanting rates must re-open this step.  (iii) The uniformity of the `o(1)`
in ⟨1⟩6.⟨3⟩2 in `t_+` is stated and used; it follows from contractivity as
written, but the double-Cesàro interchange is spelled out less fully than
MI ⟨1⟩7's own; a critic should check it.  (iv) `q_{σ_ch} ∈ spec π(Q̂)` is
derived by forcing (⟨1⟩5.⟨2⟩2), not exhibited by an eigenvector; fine for
the lemma, but it means `E_W({q_ch})` being nonzero is itself part of the
conclusion, not an input.

---

## 5. CHECKER SPEC — `theory/checks/ace_ld_check.py`

Deterministic; no randomness; no bare `assert` (every violation raises
`CheckFailure`, active under `python3 -O`).  Green exits 0; `--red` exits 1
iff every registered mutation breaks exactly its registered targets, else 2.

**Model.**  One particle on `ℤ_N` (`N = 4096`), `H` = nearest-neighbour
hopping `(Hψ)(x) = ψ(x−1)+ψ(x+1)` (dispersion `2cos k`, velocities
`−2sin k`), diagonalised by FFT; times chosen so no wavefront wraps.  The
particle position models the kink bond coordinate; the window charge is the
D13(a) clamp

  `Q̂ |x⟩ = clamp_W(x)|x⟩`,  `clamp_W(x) := min(b, max(x, a−1)) − (a−1)`,

for `W = [a,b]` centred in the ring — exactly `𝔛_W − (a−1)` on a sharp
wall at bond `x`, spectrum `{0,1,…,|W|} ⊂ ℤ` (one coset, separation 1).
Channels: `P_±` = Fourier projections onto `sin k ≶ 0` (commute with `H`).
State: `Ψ = c_-φ_- + c_+φ_+` with smooth-bump momentum packets `φ_∓` centred
at `k = ∓π/2 ± detune`, both starting inside `W`; `q_- = 0`, `q_+ = |W|`.

**Green certificates.**
- `LD-C1` (hypothesis audit): `spec Q̂` integer, one coset, gap `≥1`;
  `[P_±, H] = 0` to machine precision; `P_+P_- = 0`; `(P_++P_-)Ψ = Ψ`.
- `LD-C2` (first-moment escape): `ε_±(t) = ||(Q̂−q_±)P_±Ψ_t||` decreasing
  to `< tol` at the final time on a dyadic time grid.
- `LD-C3` (the inequality (LD.1), with its constant): at EVERY grid time
  (including early/mid times where nothing is small),
  `||E({q_±})Ψ_t − P_±Ψ_t|| ≤ Σ_{ch} d_{ch}^{-1}ε_{ch}(t) + slack`, with
  `d_{ch}` computed from the model spectrum (`=1` here).  This is the red-
  capable surface: it tests the CONSTANT, not just convergence.
- `LD-C4` (diagonality): final-time `||E({q_±})Ψ_t − P_±Ψ_t|| < tol`.
- `LD-C5` (obstruction arithmetic of ⟨1⟩6): for growing windows `W_m`, the
  two-time `ν` values are `{0, ±|W_m|}` and
  `Σ_{|ν|>M}(1+|ν|)p_{W_m}` is unbounded in `m` (evaluated on the model's
  late-time law), certifying the LR3 failure mechanism on the model.

**Red mutations** (each built as a FRESH model variant; the green model
objects are never mutated in place).  Registered patterns — a surviving
target or an unregistered casualty both give exit 2:
- `--red-coset` (*broken coset separation* — brief mutation (i)):
  `Q̂ ↦ Q̂/10` with charges `q_±/10` and the LEMMA-claimed coset constant
  `d = 1` retained (true gap `0.1`).  MUST break LD-C1 and LD-C3 —
  (LD.1)'s certified inequality fails at transit times (observed: `t=8`,
  `lhs 0.412 > rhs 0.372`) — and MUST leave LD-C2, LD-C4 standing
  (`ε` scales down with `Q̂`; `E({q/10}) = E({q})`).
- `--red-merged` (*indefinite channel charge* — brief mutation (ii)):
  channels merged (`P_1 := P_+ + P_-`, one claimed charge `q_+`) — the
  merged channel's first moment does NOT escape.  MUST break LD-C2 and
  LD-C4; MUST leave LD-C1, LD-C3 (the single-`q` bound (LD.3) is still a
  theorem).
- `--red-dup` (*equal charges, both weights nonzero* — the same-side
  regime of ⟨1⟩5.⟨2⟩3): both channels claimed at `q_+`.  MUST break LD-C2
  and LD-C4 for channel `−` (the ⟨1⟩3 refutation; observed final
  diagonality error `1.0 = ||P_+Ψ − P_-Ψ||`); MUST leave LD-C1, LD-C3
  (each single-`q` gap bound survives — it is the cross-term step of
  (LD.1)'s PROOF that needs distinctness, and the failure surfaces in the
  diagonality, exactly as ⟨1⟩3 predicts).
- `--red` runs all three; exit 1 iff every mode reproduces its registered
  pattern, else exit 2.  LD-C5 is green-only (registered NOT-RUN in red).

---

## 6. MERGE PROPOSALS (exact replacement text; orchestrator merges after
the critic converges — nothing below is live)

**MP-1. New rows for `claims/CLAIMS.md`** (append after the AD3-ex row):

| id | statement (short) | status | depends on | proved in | tested in |
|---|---|---|---|---|---|
| ACE-LD-abs | At a fixed finite window, a bounded self-adjoint charge with finite spectrum in one coset of `ℤ`, mutually orthogonal dynamics-commuting channel projections resolving the vector, first-moment channel escape `\|\|(Q̂-q_ch)P_chΨ_t\|\|→0`, and pairwise distinct channel charges imply `\|\|E({q_ch})Ψ_t-P_chΨ_t\|\| ≤ Σ_{ch'}d_{ch'}^{-1}ε_{ch'}(t) → 0` with `t`-uniform constant `≤ n` (coset gap `≥1` via M-INDEX-fin in the instance); `N` channels, general on-site spin.  Distinct charges are NECESSARY: with a shared charge and two nonvanishing weights the display fails for every claimed eigenvalue (ACE-LD-nec) | PROVED (pending L6 loop) | M-INDEX-fin | theory/ace-ld.md ⟨1⟩1--⟨1⟩3 | theory/checks/ace_ld_check.py LD-C1--C4 (green exit 0; `--red` exit 1, 3 mutations) |
| ACE-LD-esc | Under H-MQG(1)--(3), D28 (incl. unverified D28-C), ACE.1--ACE.2, and the named extra hypotheses (E-TAIL) (eigenstate tails; true in D16, false for generic MPS vacua) and (V-ch) (sign-definite outgoing kink/magnon velocities), the AC-EX channels satisfy first-moment escape at every fixed window with the COMPUTED charges `q_{σ_ch}(W,c_0)∈{2s(b-c_0), 2s(a-1-c_0)}` — the vacuum window charge on the outgoing kink's escape side — and these are the only possible values.  Hence (AD3-ex) HOLDS in the corrected eigenvalue reading iff `σ_L≠σ_T` (opposite escape sides) and is FALSE for every charge assignment if `σ_L=σ_T` with both channel weights nonzero | PROVED (conditional; pending L6 loop) | AC-EX, ACE-LD-abs, D13, D26, D27, D28, M-INDEX-fin | theory/ace-ld.md ⟨1⟩4--⟨1⟩5 | theory/checks/ace_ld_check.py LD-C2--C4 |
| ACE-LD-obst | Under the ACE-LD-esc hypotheses with `σ_L≠σ_T` plus (V-in) and both channel weights nonzero: the ordered fixed-window TPM law is `p_W=\|\|F_L\|\|²δ_{ν_L(W)}+\|\|F_T\|\|²δ_{ν_T(W)}` with `ν_ch(W)∈{0,±2s\|W\|}`, exactly one channel transiting; D27(LR3) first-moment tightness FAILS along every padded exhaustion and the ordered outcome measure is defective.  Consequently (AD3-ex) and D27(LR) are jointly unsatisfiable on the packet class where (AD3-ex) is proved, except at vanishing transit weight: ACE.3 is vacuously guarded there, and the `{0,2}` ledger support is the no-transit idealization, not a fixed-window theorem on D28 packets | PROVED (conditional; pending L6 loop) | ACE-LD-esc, D27, M-INDEX-fin, M-INDEX-spec | theory/ace-ld.md ⟨1⟩6.⟨2⟩2 | theory/checks/ace_ld_check.py LD-C5 |

**MP-2. Replacement for the `AD3-ex` row status/text** (same row id;
replace status `CONJECTURE` and append to statement):

> status: **PROVED (conditional, corrected reading) / REFUTED (same-side
> regime)** per theory/ace-ld.md — holds with the computed eigenvalues
> `q_ch=q_{σ_ch}(W,c_0)` of (LD.2) under (E-TAIL)+(V-ch) with `σ_L≠σ_T`;
> false for every charge assignment when `σ_L=σ_T` with both weights
> nonzero; the ledger constants `−1,+1` are not the `Q̂_W`-eigenvalues
> except for accidental `(W,c_0)`.  See ACE-LD-abs/-esc/-obst rows.

**MP-3. Gloss insertion into AS ⟨1⟩7's ASSUME block** (after the display,
replacing the sentence "The missing derivation is recorded as named lemma
ACE-LD (see HONEST STATUS): …" up to "…no step of this shard supplies."):

> The named lemma **ACE-LD** (theory/ace-ld.md) now supplies this control:
> under the additional hypotheses (E-TAIL) and (V-ch) there, the display
> holds with the computed eigenvalues `q_ch = q_{σ_ch}(W,c_0)` (LD.2) when
> the outgoing kinks escape on opposite sides, and is refuted for every
> charge assignment when they escape on the same side.  The `q_ch` in the
> display are therefore NOT the leg-charge constants of the theorem's
> charge clause; the two enter ⟨2⟩1--⟨2⟩2 through different roles (leg
> ledger vs `Q̂_W` spectrum), and ACE-LD-obst records that on this packet
> class the T1 outcome-measure hypothesis of ACE.3 fails unless the
> transit weight vanishes.

**MP-4. `notation.md` additions** (three rows):

| `q_±(W,c_0)` | asymptotic vacuum window charges `2s(b−c_0)`, `2s(a−1−c_0)` — the forced `Q̂_{W,c_0}`-eigenvalues of the escaped-kink channels | theory/ace-ld.md (LD.2) |
| `(E-TAIL)` | eigenstate-tail hypothesis: `ω_γ((S^z_x−s_γ)²)=0` both tails | theory/ace-ld.md §0 |
| `(V-ch)`, `(V-in)` | sign-definite outgoing/incoming velocity-class hypotheses; `σ_ch` = outgoing kink escape side | theory/ace-ld.md §0, ⟨1⟩6.⟨2⟩2 |
