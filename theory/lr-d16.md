<!-- ROLE: proposer shard for bd tns-xf4 — prove D27(LR1--LR3) for the D16
     easy-axis XXZ kink sector.  Lane: this file + theory/checks/lr_d16_check.py.
     Nothing else in the repo is edited; shared-file text is in MERGE PROPOSALS. -->

# (LR) for D16 — charge-history local relaxation in the easy-axis XXZ kink sector

**Round r2 repaired proposer draft, 2026-08-29.  Self-status: SKETCH until the
L6 loop converges.  Read the HONEST STATUS section (§H) before citing anything
here.  LR1 and LR1-GEN are the critic-confirmed unconditional result; the r2
repair does not alter their proof.**

Target: D27 (`definitions.md`), clauses (LR1), (LR2), (LR3), for the D16 model
and a D17 kink packet.  Motivation: `M-INDEX-spec` (`claims/CLAIMS.md`) is
PROVED but conditional, with D27 assumed on every model and therefore with no
unconditional dynamical instance.  This shard supplies one instance as far as it
honestly goes and names, precisely, what is left open.

Summary of the verdict reached below (details in §H):

| clause | D16 verdict |
|---|---|
| LR1 | **PROVED unconditionally** (⟨1⟩3), and at class level (⟨1⟩6); critic-confirmed, unchanged in r2 |
| LR2 | verbatim **OPEN**; the r1 D16 claim **(LR2′) is WITHDRAWN** because its sufficient condition is false for every state obeying (H3): the escaped magnon contributes `O(1)` to `G(m)` |
| LR3 | **PROVED from the repaired, two-clause (NR)** (⟨1⟩5), whose second clause retains `sup_m`; the monotonicity lemma fixes the majorising observable, not the pinched state; (EDW) is unconditional |
| class statement | LR1-GEN is **PROVED**; the alleged class counterexample is **RETRACTED** and replaced by the surviving no-mean-transport scoping requirement |

---

## ⟨1⟩1. SETUP — registers, conventions, and the standing hypotheses

This step fixes objects and names.  It proves nothing; every later leaf cites
it by number.

**⟨2⟩1 (model).**  `H` is the D16 easy-axis XXZ chain: spin-`1/2` on `ℤ`,
`J>0`, `Δ>1`,
`h^{XXZ}_{x,x+1}=−J[S^x_xS^x_{x+1}+S^y_xS^y_{x+1}+Δ(S^z_xS^z_{x+1}−¼)]`,
`ω(k)=J(Δ−cos k)`, `v(k)=J sin k`, `ω_gap=J(Δ−1)>0`,
`q=Δ−√(Δ²−1)∈(0,1)`.  The site spin is `s=1/2`, so `d=2` and every `S^z_x` has
spectrum `{±1/2}`.  By D16's kink normalisation and claim **K3** (PROVED),
`H_kink` and `H_XXZ` generate the *same* derivation on `𝔄`; every dynamical
statement below is therefore a statement about `H_XXZ`, and `H_kink` is used
only where a *value* of the energy is needed.

*Justification.* D16; claim K3.

**⟨2⟩2 (orientation, fixed once).**  D13(a) is written for the orientation
`s_α=+s` at `−∞` and `s_β=−s` at `+∞`, i.e. `↑…↓`.  D16's displayed
zero-energy family `|K(z)⟩=⊗_n(|↑⟩_n+z q^n|↓⟩_n)` has `q∈(0,1)`, hence `↓` at
`−∞` and `↑` at `+∞`: it is the *opposite* orientation, and the telescoping
field `+\tfrac{J}{2}\sqrt{Δ²−1}(S^z_x−S^z_{x+1})` of D16 is the one that
normalises *that* family to zero.  D16's broken `ℤ₂` (the `π`-rotation about
`S^x`) is an automorphism of `H_XXZ` exchanging the two orientations and
reversing the sign of the telescoping field.  **Convention (LRD-O).**  This
shard works in D13(a)'s `↑…↓` orientation, with the `ℤ₂`-image kink family
`|K̄(z)⟩=⊗_n(|↓⟩_n+z q^n|↑⟩_n)` and the field `−\tfrac{J}{2}\sqrt{Δ²−1}
(S^z_x−S^z_{x+1})`.  K1--K3 hold verbatim for the `ℤ₂`-image because `ℤ₂` is
an automorphism carrying `h^{kink}` to the reflected `h^{kink}`.
With (LRD-O), telescoping gives, as a form on the kink sector,
`H_kink = H_XXZ − \tfrac{J}{2}\sqrt{Δ²−1}`, so a K2 zero-energy kink has
`H_XXZ`-energy exactly `C_K:=\tfrac{J}{2}\sqrt{Δ²−1}>0`.  (With the opposite
bookkeeping one would get `−C_K<0`, contradicting `H_XXZ⪰0` from ⟨1⟩5.⟨2⟩6;
the orientation is therefore not free, and fixing it is not cosmetic.)

*Justification.* D16 (both displays), D16's `G=U(1)⋊ℤ₂`, claims K1--K3,
and the sign of `S^z_{−∞}−S^z_{+∞}` in each orientation; named computation
**LRD-ORIENT**.

**⟨2⟩3 (reference configuration and the window charge).**  Fix the cut `c_0∈ℤ`
and let `ρ_{c_0}(x):=+1/2` for `x≤c_0` and `−1/2` for `x>c_0` be the sharp
reference kink at `c_0` (orientation (LRD-O)).  For a finite window
`W=[a,b]∋c_0` put

  `δ_x := S^z_x − ρ_{c_0}(x)`,  `Q̂_{W,c_0} = Σ_{x∈W} δ_x`.       **(LRD.1)**

This is *identically* D27's `Q̂_{W,c_0}=2s(𝔛_W−c_0)`: with `s=1/2`,
`2s(𝔛_W−c_0)=a−1−c_0+Σ_{x∈W}(S^z_x+½)` and
`Σ_{x∈W}(ρ_{c_0}(x)+½)=c_0−a+1`, so the two displays differ by nothing.
Consequences used repeatedly: `Q̂_{W,c_0}∈𝔄_W` is **diagonal in the `S^z`
product basis**, has **integer** spectrum contained in
`[a−1−c_0, b−c_0]`, hence at most `|W|+1` eigenvalues, and
`‖Q̂_{W,c_0}‖ ≤ R_W := max(c_0−a+1, b−c_0) ≤ |W|`.

*Justification.* D13(a), D27's display, D26 (which is automatic here: `s=1/2`
gives `e^{2πiS^z_x}=−I`, `c=−1`, `κ=1/2`), and named computation
**LRD-CAL**.  This also matches, symbol for symbol, the calibration frozen in
`theory/checks/memory_index_probe.py` (`Q_W = Σ_{x∈W}(S^z_x−ρ_vac(x))`).

**⟨2⟩4 (outside charge, escaped content, and the exhaustion).**  Put

  `Q̂_{W^c,c_0} := Σ_{x<a} δ_x + Σ_{x>b} δ_x`,
  `N_R^W := Σ_{x<a}(½−S^z_x) ≥ 0`,  `N_T^W := Σ_{x>b}(S^z_x+½) ≥ 0`,
  `𝒩_W := N_R^W + N_T^W ≥ 0`.                                     **(LRD.2)**

Because `c_0∈W`, `δ_x=−(½−S^z_x)` for `x<a` and `δ_x=+(S^z_x+½)` for `x>b`, so

  `Q̂_{W^c,c_0} = N_T^W − N_R^W`,  `|Q̂_{W^c,c_0}| ≤ 𝒩_W`.        **(LRD.3)**

`N_R^W`, `N_T^W` are D14's reflected and transmitted counts at `s=1/2`.  All of
`δ_x, Q̂_W, Q̂_{W^c}, N_R^W, N_T^W, 𝒩_W` are simultaneously diagonal in the
`S^z` product basis and hence mutually commuting; so are their Heisenberg
translates *at one common time*.  Every order comparison among these
unbounded diagonal observables is pointwise on configurations.  In
particular, the squaring steps below are valid because the compared operators
commute and are pointwise non-negative; no general operator-monotonicity of
`x↦x²` is invoked.  `W_m=[a_m,b_m]↑ℤ` is D27's padded
exhaustion, `W_1⊂W_2⊂⋯`, with both core-to-edge distances
`d_m := min(c_0−a_m, b_m−c_0) → ∞`.

*Justification.* (LRD.1), D14, D27, and the elementary sign computation
**LRD-OUT**.

**⟨2⟩5 (the finite-particle register (FN) — a hypothesis on the SELECTED
vector, not a sector-wide operator).**  Let `ℋ_ref` be the incomplete tensor
product over the reference configuration `ρ_{c_0}`: the `ℓ²`-closure of the
span of `S^z` product configurations differing from `ρ_{c_0}` in **finitely
many** sites.  On the dense span of those configurations the *regularised
charge*

  `𝒬 := Σ_{x∈ℤ} δ_x`                                              **(LRD.4)**

is diagonal with integer eigenvalues and is essentially self-adjoint.  Every
`h^{XXZ}_{x,x+1}` commutes with `S^z_x+S^z_{x+1}`, so each term of the
interaction preserves `𝒬`; with finite range this makes `𝒬` conserved and
`α_t` implementable on `ℋ_ref` (Lieb--Robinson, D17's finite-time preservation
clause).

The same finite-deviation configuration span is a common core for the
diagonal multiplication operators `𝒬`, `𝒩_W`, and `D`.  Their quadratic-form
inequalities are obtained first for finite spatial truncations and then by
monotone convergence.  A Heisenberg expression involving one of them means
the corresponding extended quadratic form in `U(t)Ψ` and may equal `+∞`;
the hypotheses `G(m)<∞` and (NR) state exactly where finiteness is required.
No invariance of the algebraic core under `U(t)` is asserted.

  **(FN).**  The selected D17 vector `Ψ` lies in `ℋ_ref` and is an eigenvector
  of `𝒬`: `𝒬Ψ=𝒬_0Ψ` with `𝒬_0∈ℤ`.

**Fence (binding).**  (FN) is a property of the *selected vector*, not the
construction of a sector-wide self-adjoint charge; the latter is the REFUTED
row `M-INDEX-LA-strong` and is **not** used, asserted, or re-derived anywhere
in this shard.  The `⟨1⟩3` counterexample of `theory/memory-index.md` (a D17
state with `log`-divergent window-charge variance) does **not** satisfy (FN),
which is exactly why (FN) is a hypothesis and not a theorem.  (FN) holds by
construction for the state used by `theory/checks/memory_index_probe.py` —
the exact ground state of a *fixed* `S^z` sector of the pure-kink problem,
acted on by one modulated `S^-` — and for any finite superposition of
configurations of fixed `𝒬`.

*Justification.* D16's on-site `U(1)` invariance, D10(a)'s finite-range
register, D17, and the REFUTED row `M-INDEX-LA-strong` (cited only to fence
against it).

**⟨2⟩6 (consequence: the window charge is the outside charge).**  On the
`𝒬=𝒬_0` eigenspace of `ℋ_ref`,

  `Q̂_{W,c_0} = 𝒬_0 − Q̂_{W^c,c_0}`  and, for every `t`,
  `α_t(Q̂_{W,c_0}) = 𝒬_0 − α_t(Q̂_{W^c,c_0})`.                    **(LRD.5)**

Hence the spectral resolutions coincide up to relabelling:
`E_{W,t}({q}) = ` the spectral projection of `α_t(Q̂_{W^c,c_0})` at `𝒬_0−q`.

*Justification.* (LRD.1), (LRD.4), ⟨2⟩5 (conservation of `𝒬` and its
scalarity on the selected eigenspace), and the fact that `α_t` is a
`*`-automorphism.

**⟨2⟩7 (the selected state).**  `Ψ` is a D17 `ℓ¹` kink packet obeying (FN):
concretely, the dressed kink of ⟨2⟩2 in a fixed `𝒬` sector, acted on by one
modulated magnon creator with a `C_c^∞` momentum profile `φ` supported away
from `k∈{0,π}`.  **Dressed-kink discipline (binding).**  A *sharp* kink is not
an admissible `Ψ`: at `Δ=2` it has overlap `0.923` with the dressed kink and
the `7.7%` defect radiates near-threshold magnon pairs, which fakes a `≈5%`
violation of the two-point concentration.  This discipline is inherited
verbatim from `theory/checks/memory_index_probe.py` (module docstring) and is
enforced in `theory/checks/lr_d16_check.py`.

*Justification.* D17, D16, ⟨2⟩5, and the recorded preparation study in
`theory/checks/memory_index_probe.py`.

**⟨2⟩8 (limit order — frozen, and used in this order everywhere below).**
(i) infinite-volume dynamics first; (ii) then, at each **fixed** `W`, the
`t_±→±∞` Cesàro limits; (iii) only then the spatial exhaustion `W_m↑ℤ`.  No
step below interchanges (ii) and (iii), and no `k→0` or plane-wave limit is
taken anywhere.

*Justification.* D27 (final paragraph), D17 (non-commuting packet/soft limits),
`theory/memory-index.md` ⟨1⟩7.⟨2⟩5.

**⟨2⟩9. QED** (setup complete).

---

## ⟨1⟩2. THE EXACT STATEMENT PROVED HERE, IN D27's OWN WORDS

**ASSUME.**
(H1) D16 with `J>0`, `Δ>1`, in the orientation (LRD-O) of ⟨1⟩1.⟨2⟩2.
(H2) D26 (INT) — automatic at `s=1/2`, with `c=e^{2πiS^z}=−I`, `κ=1/2`
     (⟨1⟩1.⟨2⟩3).
(H3) D17: `Ψ` is a fixed `ℓ¹` kink packet, dressed-kink prepared, with a
     `C_c^∞` magnon profile supported away from `k∈{0,π}` (⟨1⟩1.⟨2⟩7).
(H4) **(FN)** of ⟨1⟩1.⟨2⟩5: `Ψ∈ℋ_ref` and `𝒬Ψ=𝒬_0Ψ`.
(H5) A cut `c_0` and a padded exhaustion `W_m↑ℤ` with `d_m→∞` (D27).
(H6) The frozen limit order of ⟨1⟩1.⟨2⟩8.

**PROVE.**

- **(LRD-1) = D27(LR1), unconditional.**  There is one sequence `T_n→∞` such
  that for **every** finite window `W∋c_0` the two Cesàro states
  `ω^±_{W,n}` converge on `𝔄_W` (indeed on all of `𝔄`) and the double-Cesàro
  TPM laws `p_{W,n}(ν)` converge for every `ν∈ℤ`.  Proved in ⟨1⟩3 from (H1),
  (H3) alone — (H2), (H4) are not used.

- **(LRD-2-BND) = a scalar bound, not a D16 relaxation result.**
  Write `Δ_W(t_-,t_+):=⟨Ψ,[𝒟_{W,t_-}(Q̂_{W,c_0}(t_+))−Q̂_{W,c_0}(t_+)]Ψ⟩` for
  D27's first-moment nondemolition defect.  Then
  `limsup_n |double-Cesàro average of Δ_{W_m}| ≤ η_m` with an **explicit**
  `η_m = 4R_{W_m}\sqrt{G(m)}`.  This estimate is proved in ⟨1⟩4, but its
  sufficient condition `R_{W_m}²G(m)→0` is **false for every state obeying
  (H3)**: the outgoing magnon leaves every fixed window and contributes one
  unit to `𝒩_{W_m}`, so `G(m)≥1-o(1)` at every fixed `m`.  Thus the r1 D16
  result called **(LR2′) is WITHDRAWN**, not patched.  **D27(LR2) verbatim is
  OPEN**; ⟨1⟩4.⟨2⟩6 isolates the residue and names it (DPH).

- **(LRD-3) = D27(LR3), conditional on the repaired, two-clause (NR) of
  ⟨1⟩5.⟨2⟩7.**  `lim_{M→∞} sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν)=0`.  The
  monotonicity lemma ⟨1⟩5.⟨2⟩4 replaces the family of majorising observables
  `{𝒩_{W_m}}` by the single `𝒩_{W_1}`; it does **not** remove the
  `m`-dependence of the `W_m`-pinched state.  Accordingly (NR)'s second clause
  retains `sup_m`.  The domain-wall count is bounded unconditionally and
  uniformly in time by ⟨1⟩5.⟨2⟩6.

- **(LRD-4) optional convenience clause of D27(LR3)** (weak convergence of
  `{p_{W_m}}` to a probability `p`): **NOT proved**, and not needed.  Under
  (LRD-3) alone, `M-INDEX-spec` delivers subsequence-free support
  quantization and a per-subsequence value `δx`; see ⟨1⟩6.⟨2⟩5 and §H.

**What is deliberately NOT proved, and must not be read in.**
(i) Operator asymptotic commutativity of `Q̂_{W,c_0}(t_-)` and
`Q̂_{W,c_0}(t_+)`.  D27(LR2) is a **first-moment** condition and explicitly
does not assume the operator statement; nothing below uses or asserts it, and
⟨1⟩4 works with the *scalar* defect throughout.
(ii) Asymptotic completeness, a channel inventory, wave operators, or D18.
None is used; D27 is channel-free and so is this shard.
(iii) A sector-wide self-adjoint regularised charge — REFUTED
(`M-INDEX-LA-strong`); see the fence in ⟨1⟩1.⟨2⟩5.
(iv) Claim **K4** (thermodynamic uniqueness/flatness), which is CONJECTURE.
⟨1⟩5.⟨2⟩8 uses only the *flatness of the K1--K2 family itself*, which is a
consequence of two PROVED claims, and never uniqueness or completeness of the
kink band.
(v) The Fano graph and the transmission amplitude of `corner-b-draft.md` §5.2:
those rest on the finite-enumeration hypothesis S1, which that shard labels
"Evidence only".  No step below uses `t(k)`, `T(k)` or `δ_t(k)`.
(vi) Any Bethe input.  Bethe is an oracle, never a hypothesis.

**Remark (the surviving scope statement).**  This shard uses no spectral gap
and no Lieb--Robinson velocity estimate.  It therefore proves no implication
from "gap + Lieb--Robinson" to (LR), but neither does it refute one.  The r1
counterexample is retracted: it named no model, and its mobile-core mechanism
is excluded on (FN), where (LRD.5) identifies sharp-wall position with the
conserved charge.  What survives is the independent `ACE-LD-obst′` scoping
fact: a class theorem must exclude mean charge transport.  In the present
(FN) register a large increment requires unbounded wrong-phase **block
growth**, not rigid core transit.  K1--K2 supply only that every state in their
closed product-family span is stationary; exhaustiveness is K4 and is not
used.

*Justification of the display of hypotheses.* D27 verbatim, D16, D17, D26,
`claims/CLAIMS.md` rows K1--K4, `M-INDEX-spec`, `M-INDEX-LA-strong`.

**⟨2⟩1. QED** (statement fixed).

---

## ⟨1⟩3. LEMMA LRD-1 (= D27(LR1)) — PROVED UNCONDITIONALLY

**ASSUME.** (H1), (H3) of ⟨1⟩2.  (Not used: (H2), (H4), (H5), and any
scattering, gap, completeness or channel input.)

**PROVE.** There is a single sequence `T_n→∞` such that

(i) for every `A∈𝔄` the limits
`ω^±(A) := lim_n ω^±_{W,n}(A)` exist, where
`ω^+_{W,n}(A)=T_n^{-1}∫_{T_n}^{2T_n}⟨Ψ,α_t(A)Ψ⟩dt` and
`ω^-_{W,n}(A)=T_n^{-1}∫_{-2T_n}^{-T_n}⟨Ψ,α_t(A)Ψ⟩dt`
(so in particular for every `A∈𝔄_W` at every fixed finite `W∋c_0`), and the
limits are states on `𝔄`; and

(ii) for every finite window `W∋c_0` and every `ν∈ℤ` the double-Cesàro TPM
weights `p_{W,n}(ν)` of D27(LR1) converge, and their limits `p_W` form a
probability measure on `ℤ`.

**⟨2⟩1 (the algebra is separable and the dynamics is norm-continuous).**
`𝔄` is the quasi-local algebra of a spin-`1/2` chain: the C*-inductive limit
of the countable directed family `{𝔄_Λ}` of finite-dimensional matrix
algebras, so `𝔄_loc` contains a countable `‖·‖`-dense subset `𝔇` (take
rational-coefficient words in a fixed finite generating set of each `𝔄_Λ`,
`Λ` ranging over the countably many finite intervals).  Since `H` is
translation-invariant and of finite range (D16, D10(a)), the infinite-volume
dynamics `α_t` exists as a strongly continuous one-parameter group of
`*`-automorphisms of `𝔄`, i.e. `t↦α_t(A)` is `‖·‖`-continuous for each
`A∈𝔄`.

*Justification.* D16 (finite range, translation invariance), D10(a)'s
finite-range register, D17's finite-time Lieb--Robinson clause (the same
estimate that yields the group), and the elementary separability count
**LRD-SEP**.

**⟨2⟩2 (the Cesàro objects are states).**  For each `A∈𝔄` the map
`t↦⟨Ψ,α_t(A)Ψ⟩` is continuous and bounded by `‖A‖`, so the integrals defining
`ω^±_{W,n}` converge absolutely; `ω^±_{W,n}` is linear, positive
(`ω(A^*A)≥0` pointwise in `t`), and unital, hence a state on `𝔄`.  Note
`ω^±_{W,n}` does **not** in fact depend on `W`; the `W`-label is D27's and is
retained verbatim.

*Justification.* ⟨2⟩1, D27(LR1)'s display, and the positivity of
`t↦⟨Ψ,α_t(A^*A)Ψ⟩`.

**⟨2⟩3 (first extraction: the two one-time Cesàro states).**  The state space
`S(𝔄)` of a separable unital C*-algebra is weak-`*` compact and metrizable,
hence **sequentially** compact.  Apply this to `S∋ω^+_{·,T}` along `T=1,2,3,…`
to extract `T_n^{(1)}→∞` with `ω^+_{·,T_n^{(1)}}→ω^+` weak-`*`; apply it again
along `T_n^{(1)}` to `ω^-` to extract a further subsequence `T_n^{(2)}` with
`ω^-_{·,T_n^{(2)}}→ω^-`.  Both limits are states (weak-`*` limits of states on
a unital C*-algebra are states).  This gives (i) for every `A∈𝔄`, hence for
every `A∈𝔄_W` at every fixed `W` simultaneously — one sequence, all windows.

*Justification.* ⟨2⟩1, ⟨2⟩2, Banach--Alaoglu with metrizability from
separability; named computation **LRD-COMPACT**.

**⟨2⟩4 (the TPM integrand is continuous and the `ν`-range is finite).**  Fix a
finite `W∋c_0`.  By ⟨1⟩1.⟨2⟩3, `Q̂_{W,c_0}∈𝔄_W` has a **finite** spectrum
`σ_W⊂ℤ` with `|σ_W|≤|W|+1`, so its spectral projections `E_W({q})` are
elements of `𝔄_W` and `E_{W,t}({q})=α_t(E_W({q}))`.  Hence

  `F_{W,ν}(t_-,t_+) := Σ_{q∈σ_W}‖α_{t_+}(E_W({q−ν}))α_{t_-}(E_W({q}))Ψ‖²`

is a finite sum of jointly continuous functions of `(t_-,t_+)`, takes values in
`[0,1]`, vanishes identically unless `ν∈σ_W−σ_W` (a finite subset of `ℤ` of
cardinality `≤2|W|+1`), and satisfies `Σ_ν F_{W,ν}(t_-,t_+)=1` for every
`(t_-,t_+)`.  Therefore `p_{W,n}(ν)=T_n^{-2}∫∫F_{W,ν}` is well defined,
lies in `[0,1]`, and `Σ_ν p_{W,n}(ν)=1` for every `n`.

*Justification.* ⟨1⟩1.⟨2⟩3 (finite integer spectrum), ⟨2⟩1 (norm-continuity of
`α_t`), D27(LR1)'s display, and `theory/memory-index.md` ⟨1⟩5.⟨2⟩1--⟨2⟩3
(the same law, its positivity, normalisation, and integrality of `ν`); named
computation **LRD-TPM**.

**⟨2⟩5 (second extraction: one diagonal sequence for all `(W,ν)`).**  The
index set `𝕀 := {(W,ν) : W=[a,b] finite, c_0∈W, ν∈ℤ}` is countable.  Enumerate
it as `i_1,i_2,…`.  Starting from `T_n^{(2)}` of ⟨2⟩3, extract successively
nested subsequences along which `p_{i_1,n}, p_{i_2,n}, …` converge (each is a
sequence in the compact interval `[0,1]`), and take the diagonal sequence
`T_n := T_n^{(2+n)}`.  Along `T_n`, every `p_{W,n}(ν)` converges, to a limit
`p_W(ν)∈[0,1]`, **and** the conclusions of ⟨2⟩3 persist (a subsequence of a
convergent sequence converges to the same limit).

*Justification.* ⟨2⟩4, Bolzano--Weierstrass, and the standard Cantor diagonal
construction; named computation **LRD-DIAG**.

**⟨2⟩6 (the limit is a probability on `ℤ`).**  Each `p_{W,n}` is supported in
the fixed finite set `σ_W−σ_W⊂ℤ` (⟨2⟩4), independent of `n`.  A pointwise
limit of probability measures on a **fixed finite** set is a probability
measure on that set; no mass can escape.  Hence `p_W` is a probability on `ℤ`
with `Σ_ν p_W(ν)=1` and `supp p_W ⊆ σ_W−σ_W ⊆ ℤ`.

*Justification.* ⟨2⟩4, ⟨2⟩5; integrality of `ν` is `theory/memory-index.md`
⟨1⟩5.⟨2⟩3 (offset cancellation at fixed `W`), re-derived here from
⟨1⟩1.⟨2⟩3's integer spectrum.

**⟨2⟩7 (scope: what was actually used).**  The proof consumed exactly three
inputs: (a) `𝔄` separable and unital; (b) `α_t` a strongly continuous
one-parameter automorphism group; (c) `Q̂_{W,c_0}∈𝔄_W` self-adjoint with
finite spectrum at each fixed `W`.  It used **no** gap, **no** Lieb--Robinson
velocity, **no** ergodicity, **no** scattering, and **no** property of `Ψ`
beyond normalisation.  It also did **not** prove pointwise-in-`t` convergence,
which D27(LR1) does not ask for.  This is recorded as Lemma **LR1-GEN** and
reused in ⟨1⟩6.

*Justification.* Inspection of ⟨2⟩1--⟨2⟩6.

**⟨2⟩8. QED.** □

---

## ⟨1⟩4. LR2 — exact defect identities and bound; D16 LR2′ WITHDRAWN, LR2 OPEN

Throughout, `W=[a,b]∋c_0` is fixed, `P_q := E_{W,t_-}({q}) = α_{t_-}(E_W({q}))`,
`φ_q := P_qΨ`, `A := Q̂_{W,c_0}(t_+) = α_{t_+}(Q̂_{W,c_0})`, and

  `Δ_W(t_-,t_+) := ⟨Ψ,[𝒟_{W,t_-}(A)−A]Ψ⟩`                        **(LRD.6)**

is D27(LR2)'s defect.  **This is a scalar quantity throughout; no operator
statement about `[Q̂_W(t_-),Q̂_W(t_+)]` is made, used, or implied.**

**⟨2⟩1 (exact off-diagonal form).**  `Δ_W(t_-,t_+) = −Σ_{q≠q'}⟨φ_q,Aφ_{q'}⟩`.

*Justification.* `Σ_qP_q=I` (spectral resolution of a finite integer spectrum,
⟨1⟩1.⟨2⟩3), so `⟨Ψ,AΨ⟩=Σ_{q,q'}⟨φ_q,Aφ_{q'}⟩` while
`⟨Ψ,𝒟_{W,t_-}(A)Ψ⟩=Σ_q⟨φ_q,Aφ_q⟩` by the displayed definition of `𝒟` in D27;
subtract.  Named computation **LRD-DEF.1**.  (Same algebra as
`theory/memory-index.md` ⟨1⟩6.⟨2⟩1--⟨2⟩2, in the opposite direction.)

**⟨2⟩2 (the defect is a pure boundary-current object, and vanishes at equal
times).**  For any scalar `c` and any operator `B` commuting with every `P_q`,
`Σ_{q≠q'}⟨φ_q,(c+B)φ_{q'}⟩=0`.  Since `Q̂_{W,c_0}(t_-)` commutes with every
`P_q` by construction,

  `Δ_W(t_-,t_+) = −Σ_{q≠q'}⟨φ_q, [∫_{t_-}^{t_+}α_t(𝒥_W)\,dt]\,φ_{q'}⟩`,
  `𝒥_W := i[H,Q̂_{W,c_0}] = j_{a−1|a}−j_{b|b+1}`,                 **(LRD.7)**

where `j` is D10(a)'s cut current.  In particular `Δ_W(t,t)=0` identically,
and `‖𝒥_W‖ ≤ 2\max_m‖j_{m|m+1}‖ =: C_j`, a constant **independent of `W`**:
the whole defect lives on the two window edges.

*Justification.* D10(a) (finite-support cut current, nearest-neighbour case
`j_{x|x+1}=−[h_{x,x+1},q_x]`), D10(b) (continuity equation, so that all bulk
terms cancel and only the two straddling bonds survive), ⟨2⟩1, and
translation invariance of `H` (D16) for the `W`-independence of `C_j`.  Named
computation **LRD-DEF.2**.

**⟨2⟩3 (uniform scalar bound by the initial-time charge sharpness).**  Put

  `ε_W(t_-)² := 1 − ‖E_{W,t_-}({𝒬_0})Ψ‖² ∈[0,1]`.                **(LRD.8)**

Then `|Δ_W(t_-,t_+)| ≤ 4‖Q̂_{W,c_0}‖·ε_W(t_-) ≤ 4R_W·ε_W(t_-)` for all
`t_+`, with `R_W ≤ |W|` from ⟨1⟩1.⟨2⟩3.

*Justification.* Write `Ψ=φ_{𝒬_0}+χ`, `‖χ‖=ε_W(t_-)`.  Then
`⟨Ψ,AΨ⟩−Σ_q⟨φ_q,Aφ_q⟩ = 2\Re⟨φ_{𝒬_0},Aχ⟩+⟨χ,Aχ⟩−Σ_{q≠𝒬_0}⟨φ_q,Aφ_q⟩`,
whose modulus is at most `2‖A‖ε+‖A‖ε²+‖A‖ε² ≤ 4‖A‖ε` for `ε≤1`; and
`‖A‖=‖α_{t_+}(Q̂_W)‖=‖Q̂_W‖` because `α_{t_+}` is a `*`-automorphism.  Named
computation **LRD-DEF.3**.

**⟨2⟩4 (the sharpness defect IS the escaped-charge second moment —
unconditional given (FN)).**  For every `t`,

  `ε_W(t)² ≤ ⟨Ψ, α_t(Q̂_{W^c,c_0})²Ψ⟩ ≤ ⟨Ψ, α_t(𝒩_W)²Ψ⟩`.        **(LRD.9)**

*Justification.* `spec Q̂_{W,c_0}⊂ℤ` and `𝒬_0∈ℤ` (⟨1⟩1.⟨2⟩3, ⟨2⟩5), so
`|q−𝒬_0|≥1` for every spectral value `q≠𝒬_0`; hence
`ε_W(t)²=Σ_{q≠𝒬_0}‖E_{W,t}(q)Ψ‖² ≤ Σ_q(q−𝒬_0)²‖E_{W,t}(q)Ψ‖²
=⟨Ψ,(α_t(Q̂_{W,c_0})−𝒬_0)²Ψ⟩`.  By (LRD.5) and conservation of `𝒬`
(⟨1⟩1.⟨2⟩5--⟨2⟩6), `α_t(Q̂_{W,c_0})−𝒬_0 = −α_t(Q̂_{W^c,c_0})`; then (LRD.3).
Named computation **LRD-DEF.4**.  *This step is where (FN) is consumed, and
it is the only place in ⟨1⟩4 where it is.*

**⟨2⟩5 (LEMMA LRD-2-BND — PROVED bound; r1's D16 conclusion
WITHDRAWN).**  Define the **escape profile**

  `G(m) := sup_{t∈ℝ} ⟨Ψ, α_t(𝒩_{W_m})²Ψ⟩ ∈[0,∞]`.                **(LRD.10)**

Then for every `n` and every `m`,
`|T_n^{-2}∫∫ Δ_{W_m}(t_-,t_+)\,dt_-dt_+| ≤ η_m := 4R_{W_m}\sqrt{G(m)}`, and
therefore the double-Cesàro average of `Δ_{W_m}` has `limsup_n` at most
`η_m`.  The abstract implication

  **(ESC)** `R_{W_m}²G(m)→0` `⟹` the defect vanishes along the exhaustion

is valid, but **(ESC) is false on the D16 state class (H3)**.  The `C_c^∞`
magnon has `|v(k)|=J|sin k|` bounded away from zero on its compact momentum
support.  At large `|t|` it lies outside every fixed `W_m`; whether it exits
left or right, it contributes exactly one to `N_R^{W_m}` or `N_T^{W_m}`.
Since `𝒩_{W_m}` has non-negative integer spectrum,
`𝒩_{W_m}²⪰𝒩_{W_m}`, and hence `G(m)≥1-o(1)` for every fixed `m`.  Thus
`R_{W_m}²G(m)` cannot vanish and `η_m` grows at least linearly in `R_{W_m}`.
The r1 D16 result named **(LR2′) is retracted**.  The bound is not rescued by
its constant: `|Δ_W|≤2‖Q̂_W‖` is always available, whereas at `W=[4,9]` the
measured `4R_Wε_W(t_-)≈10--12` exceeds the free bound `2‖Q̂_W‖=6` at five of
six sampled times.  No constant is patched to make the estimate useful.

Two unconditional facts about `G` remain: (i) `G` is non-increasing in `m`,
because `𝒩_{W_m}` is a sum of
non-negative diagonal terms over `ℤ∖W_m` and `W_m` increases, so
`𝒩_{W_{m+1}} ≤ 𝒩_{W_m}` pointwise, hence `α_t(𝒩_{W_{m+1}})^2 ≤
α_t(𝒩_{W_m})^2`; (ii) at each **fixed** `t`, `⟨Ψ,α_t(Q̂_{W_m^c})²Ψ⟩→0` as
`m→∞`, because `Q̂_{W_m}Ψ_t→𝒬Ψ_t=𝒬_0Ψ_t` in `ℋ_ref` for `Ψ_t` in the domain
of `𝒬` (⟨1⟩1.⟨2⟩5).  What (i)--(ii) do **not** give by themselves is
uniformity in `t`, which is exactly the content of `G(m)→0`.

*Justification.* ⟨2⟩3, ⟨2⟩4, (LRD.10); monotonicity of the diagonal sums
(named computation **LRD-MONO**, reused in ⟨1⟩5.⟨2⟩4); dominated convergence
for (ii); and the triangle inequality for the double Cesàro average of a
uniformly bounded function.

**⟨2⟩6 (what is NOT proved: the residue (DPH), and why the shard stops here).**
D27(LR2) verbatim asks for the double-Cesàro average of `Δ_W` to tend to `0`
at **fixed** `W`.  ⟨2⟩5 gives only `≤4R_W\sqrt{G(W)}`, and `G(W)>0` at fixed
`W`.  The relevant residue is **not** the exponentially small K1--K2 kink
tail `O(q^{2d_W})`; it is the outgoing **O(1) magnon**, which leaves every
fixed window and contributes one to `𝒩_W`.  The missing statement is
therefore

  **(DPH) — dephasing residue.**  At each fixed `W`,
  `lim_n T_n^{-2}∫_{T_n}^{2T_n}dt_+∫_{-2T_n}^{-T_n}dt_- Σ_{q≠q'}
   ⟨φ_q(t_-),α_{t_+}(Q̂_{W,c_0})φ_{q'}(t_-)⟩ = 0`,

i.e. the surviving off-diagonal coherences average to zero rather than merely
staying small.  **(DPH) is a CONJECTURE.**  Its plausible mechanism in D16 is
that the two edge coherences carry incommensurate phases from the two
outgoing legs, which separate spatially, so their double-Cesàro average
cancels; but "the legs separate" is a completeness statement (D18/AC-EX
territory) and is not available here.  Attempting to close (DPH) by asserting
`[Q̂_W(t_-),Q̂_W(t_+)]→0` would be a **strictly stronger** claim than D27(LR2)
and is explicitly refused by D27's own text; this shard does not make it.

*Justification.* ⟨2⟩1--⟨2⟩5, D27(LR2) final sentence, D18/AC-EX scoping in
`claims/CLAIMS.md`.

**⟨2⟩7 (downstream consequence of the withdrawal).**
By content, `theory/memory-index.md` consumes D27(LR2) at one genuine leaf,
⟨1⟩7.⟨2⟩1, to convert (IDX.4) into
`Σ_ν ν p_W(ν)=ω_W^-(Q̂_{W,c_0})−ω_W^+(Q̂_{W,c_0})` at fixed `W`.  Replacing
LR2 by (LR2′) replaces that equality at `W_m` by
`|Σ_ν ν p_{W_m}(ν) − [ω_{W_m}^-(Q̂)−ω_{W_m}^+(Q̂)]| ≤ η_m`.
Every later step of ⟨1⟩7 is unaffected: ⟨2⟩2 is the exact identity (IDX.1)
with the scalar `−2sc_0` cancelling and carries the same `η_m`; ⟨2⟩3 (support
quantization, Prokhorov on `ℤ`) uses LR1 and LR3 only and never LR2; and
⟨2⟩4 would take `m→∞`, where an actually vanishing `η_m` would kill the
error.  That conditional mitigation is algebraically correct, but its
antecedent is unavailable for D16 by ⟨2⟩5.  Thus it delivers **nothing** to
`M-INDEX-spec`, which is unaffected because it already assumes D27(LR2), and
`M-INDEX-fin` is safe because its finite-window TPM arithmetic uses no
dephasing limit.  `memory-index.md` ⟨1⟩5.⟨2⟩1 also cites D27(LR2), but by
content uses only D27's clause-1 TPM display; that lane-local mis-citation is
recorded in MP-2 and not edited here.

*Justification.* `theory/memory-index.md` ⟨1⟩6 (IDX.4), ⟨1⟩7.⟨2⟩1--⟨2⟩4,
D27, and ⟨2⟩5.  The conditional error would be introduced *before* the
spatial limit and removed *by* it, so the limit order would be respected;
for D16 it is not removed because `η_m` does not vanish.

**⟨2⟩8. QED** (the scalar bound is proved; the D16 LR2′ claim is withdrawn;
LR2 verbatim is reduced to (DPH) and left OPEN). □

---

## ⟨1⟩5. LR3 — first-moment tightness

**ASSUME.** (H1)--(H6) of ⟨1⟩2, and D27(LR1) as established in ⟨1⟩3.

**PROVE.** `lim_{M→∞} sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν)=0`, given the repaired,
two-clause input (NR) of ⟨2⟩7.  Steps ⟨2⟩1--⟨2⟩6 are unconditional.

**⟨2⟩1 (exact second-moment identity — unconditional).**  With
`ΔQ̂_W := Q̂_{W,c_0}(t_+)−Q̂_{W,c_0}(t_-)`,

  `Σ_ν ν² p_{W;t_-,t_+}(ν) = ⟨Ψ, 𝒟_{W,t_-}((ΔQ̂_W)²) Ψ⟩`.          **(LRD.11)**

*Justification.* By D27(LR1)'s display and the spectral theorem for
`A:=Q̂_{W,c_0}(t_+)`,
`Σ_νν²p = Σ_{q,q'}(q−q')²‖E_{W,t_+}({q'})φ_q‖² = Σ_q⟨φ_q,(A−q)²φ_q⟩`.
Since `Q̂_{W,c_0}(t_-)φ_q=qφ_q` and both operators are self-adjoint,
`⟨φ_q,(A−q)²φ_q⟩=⟨φ_q,(A−Q̂_{W,c_0}(t_-))²φ_q⟩`, and summing over `q` is the
definition of `𝒟_{W,t_-}` paired with `Ψ`.  Named computation **LRD-M2**.
This is the exact second-moment companion of the first-moment identity
(IDX.4) of `theory/memory-index.md` ⟨1⟩6.

**⟨2⟩2 (Chebyshev: first-moment tightness follows from a uniform second
moment).**  For any probability `p` on `ℤ` and any `M≥1`,
`Σ_{|ν|>M}(1+|ν|)p(ν) ≤ 2Σ_{|ν|>M}|ν|p(ν) ≤ (2/M)Σ_νν²p(ν)`.
Hence if `S := sup_m sup_{t_-<t_+} Σ_νν²p_{W_m;t_-,t_+}(ν) < ∞` then
`sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν) ≤ 2S/M → 0`, which is exactly D27(LR3).

*Justification.* `1+|ν| ≤ 2|ν|` for `|ν|≥1`, and `|ν|≤ν²/M` for `|ν|>M≥1`;
elementary.  Named computation **LRD-CHEB**.

**⟨2⟩3 (splitting the second moment onto the two window edges —
unconditional given (FN)).**  By (LRD.5),
`ΔQ̂_W = α_{t_-}(Q̂_{W^c,c_0}) − α_{t_+}(Q̂_{W^c,c_0})` (the scalar `𝒬_0`
cancels).  For self-adjoint `X,Y`, `2X²+2Y²−(X−Y)²=(X+Y)²⪰0`, and
`𝒟_{W,t_-}` is a positive unital map, so from (LRD.11)

  `Σ_νν²p_{W;t_-,t_+} ≤ 2⟨Ψ,α_{t_-}(Q̂_{W^c})²Ψ⟩
                       + 2Σ_q‖α_{t_+}(Q̂_{W^c})φ_q‖²`,             **(LRD.12)**

where the first term used that `α_{t_-}(Q̂_{W^c,c_0})` commutes with every
`P_q` (it is a function of `α_{t_-}(Q̂_{W,c_0})`'s complement in the same
commuting family, ⟨1⟩1.⟨2⟩4 and ⟨2⟩6), so `𝒟_{W,t_-}` acts on it as the
identity.  Both terms are `⟨escaped charge²⟩`: the first in `Ψ`, the second in
the post-first-measurement (pinched) state.

*Justification.* ⟨1⟩1.⟨2⟩4, ⟨1⟩1.⟨2⟩6, ⟨2⟩1, positivity of the pinching, and
named computation **LRD-SPLIT**.

**⟨2⟩4 (MONOTONICITY LEMMA — the observable is fixed, not the pinched
state).**  For
`W⊆W'` (both containing `c_0`), `𝒩_{W'} ≤ 𝒩_W` as operators, and
`|Q̂_{W^c,c_0}| ≤ 𝒩_W`.  Hence along the exhaustion, for every `m`, every
`t_±`, with `φ_q^{(m)}:=E_{W_m,t_-}({q})Ψ`,

  `Σ_νν²p_{W_m;t_-,t_+} ≤ 2⟨Ψ,α_{t_-}(𝒩_{W_1})²Ψ⟩
                          + 2Σ_q‖α_{t_+}(𝒩_{W_1})φ_q^{(m)}‖²`.    **(LRD.13)**

The majorising **observable** is the fixed `𝒩_{W_1}`.  The second term still
depends on `m`, because the dephased state
`Σ_q|φ_q^{(m)}⟩⟨φ_q^{(m)}|` depends on the `W_m` pinching.  Positivity of a
pinching does not make its expectation of a non-commuting positive observable
monotone.

*Justification.* `𝒩_W=Σ_{x<a}(½−S^z_x)+Σ_{x>b}(S^z_x+½)` is a sum of
non-negative diagonal terms over `ℤ∖W` (⟨1⟩1.⟨2⟩4); enlarging `W` deletes
terms, so `𝒩_{W'}≤𝒩_W` pointwise on configurations, hence as operators, and
`α_t` preserves operator order.  `|Q̂_{W^c}|≤𝒩_W` is (LRD.3).  Named
computation **LRD-MONO** (the same computation as ⟨1⟩4.⟨2⟩5(i)).

**Remark (what the monotonicity lemma actually buys).**  D27(LR3) is uniform
over the exhaustion.  ⟨2⟩4 prevents the window geometry from enlarging the
majorising observable: every term is measured with the fixed `𝒩_{W_1}`.
Uniformity is nevertheless **not free**, because the measured/dephased state
varies with `m`.  On (FN), (LRD.5) pins a sharp wall's position to `𝒬_0`, so a
large increment cannot be blamed on rigid core transit; it requires
unbounded wrong-phase block growth visible either in `Ψ` or in the
`W_m`-dephased state.  This is exactly why (NR)'s second clause retains
`sup_m`.

**⟨2⟩5 (passing a uniform bound to the fixed-window limit laws).**  If the
right side of (LRD.13) is bounded by one finite `S` uniformly in `m,t_-,t_+`,
then `Σ_νν²p_{W_m,n} ≤ S` for every `m,n` by convexity of the double-Cesàro
average, and by ⟨1⟩3.⟨2⟩5
`p_{W_m,n}(ν)→p_{W_m}(ν)` pointwise, so Fatou on the counting measure gives
`Σ_νν²p_{W_m}(ν) ≤ liminf_n Σ_νν²p_{W_m,n}(ν) ≤ S`, uniformly in `m`.  With
⟨2⟩2 this is D27(LR3).

*Justification.* ⟨1⟩3.⟨2⟩5--⟨2⟩6, ⟨2⟩2--⟨2⟩4, Fatou's lemma for non-negative
summands.

**⟨2⟩6 (UNCONDITIONAL energy--domain-wall bound (EDW)).**  In the basis
`(|↑↓⟩,|↓↑⟩)` the D16 bond term `h^{XXZ}_{x,x+1}` is
`(JΔ/2)I − (J/2)σ^x`, with eigenvalues `(J/2)(Δ∓1)`, and it annihilates
`|↑↑⟩,|↓↓⟩`.  Hence, with `P^{DW}_x` the projection onto
`span{|↑↓⟩,|↓↑⟩}_{x,x+1}` and `D:=Σ_xP^{DW}_x` the domain-wall number,

  `h^{XXZ}_{x,x+1} ⪰ \tfrac{J}{2}(Δ−1)\,P^{DW}_x`,
  `H_{XXZ} ⪰ \tfrac{J}{2}(Δ−1)\,D ⪰ 0`.                          **(LRD.14)**

Since `E_0 := ⟨Ψ,H_{XXZ}Ψ⟩` is finite on a D17 packet and conserved,

  `⟨Ψ, α_t(D)Ψ⟩ ≤ \frac{2E_0}{J(Δ−1)}` **for every `t`**.          **(LRD.15)**

For the bare K1--K2 kink, ⟨1⟩1.⟨2⟩2 gives `E_0=C_K=\tfrac{J}{2}\sqrt{Δ²−1}`
and hence `⟨D⟩ ≤ \sqrt{(Δ+1)/(Δ−1)}`, which `→1` as `Δ→∞` (one wall) and
diverges as `Δ→1⁺` (the kink delocalises) — both as they must.  For the kink
plus one magnon of profile `φ`, `E_0=C_K+∫\frac{dk}{2π}|φ(k)|²ω(k)`.

*Justification.* D16's displayed `h^{XXZ}`, the explicit `2×2` block (the same
block as claim **K1**'s ⟨1⟩1, before the telescoping field is added),
`Δ>1`, conservation of `H_{XXZ}` under `α_t`, and ⟨1⟩1.⟨2⟩2 for the value of
`C_K`.  Named computation **LRD-EDW**; certified numerically as row
`LRD-C4` of `theory/checks/lr_d16_check.py`.

**⟨2⟩7 (the residual input (NR), stated once and used once).**

  **(NR) — no unbounded escaped content (TWO clauses).**  With `W_1` the
  smallest window of the exhaustion:

  1. `sup_{t∈ℝ}⟨Ψ,α_t(𝒩_{W_1})²Ψ⟩<∞`;
  2. `sup_m sup_{t_-<t_+}Σ_q
     ‖α_{t_+}(𝒩_{W_1})E_{W_m,t_-}({q})Ψ‖²<∞`.

  Equivalently, let
  `S_{NR}:=sup_m sup_{t_-<t_+}[2⟨Ψ,α_{t_-}(𝒩_{W_1})²Ψ⟩
   +2Σ_q‖α_{t_+}(𝒩_{W_1})E_{W_m,t_-}({q})Ψ‖²]<∞`.

**THEOREM (LRD-3).**  Under (H1)--(H6) and (NR), D27(LR3) holds, with the
explicit tail bound `sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν) ≤ 2S_{NR}/M`.

*Proof.* ⟨2⟩4 gives (LRD.13) with right side `≤S_{NR}` for every `m`; ⟨2⟩5
transports it to the limit laws; ⟨2⟩2 converts it into the tail statement.
□

**Scope of (NR), stated plainly.**  (NR) is **two clauses, not one**, and they
have unequal weight.
The first, `sup_t⟨α_t(𝒩_{W_1})²⟩<∞`, says the total wrong-phase content
outside one fixed window has a bounded second moment for all time — the honest
form of "the wall does not run away and no bubble grows without bound".  The
second retains `sup_m`: it says the same after each `W_m` first TPM
measurement.  The monotonicity lemma makes the observable `𝒩_{W_1}` fixed but
does not make these pinched states independent of `m`.  (EDW)
(⟨2⟩6) proves *unconditionally* that the **number** of phase boundaries is
bounded uniformly in time; what (EDW) does not control is their **length**,
because in one dimension a wrong-phase block of any length carries the same
`O(1)` Ising cost.  That gap is precisely (NR), and naming it is the honest
statement of where this shard stops.  (NR) is genuine and non-circular:
it controls `sup_t` state/dephased-state second moments, while LR3 controls
only tails of double-Cesàro limit laws; LR3 does not recover either clause.

**⟨2⟩8 (the D16 feature that makes (NR) the right hypothesis: exact flatness
of the K1--K2 family).**  Let `𝒦_flat` be the closed span in `ℋ_ref` of the
K2 zero-energy family `{|K̄(z)⟩}` of ⟨1⟩1.⟨2⟩2.  Then `H_kink` vanishes on
`𝒦_flat`, so `α_t` acts on it trivially (up to the constant phase `e^{-iC_Kt}`
in the `H_XXZ` normalisation): **every state in the closed span of the K1--K2
family is exactly stationary.**

*Justification.* K1 gives `h^{kink}_{x,x+1}⪰0` bondwise, so for every finite
`Λ` the form `Σ_{x∈Λ}h^{kink}_x` is `⪰0`; K2 gives
`h^{kink}_x|K̄(z)⟩=0` for every bond, so that form has value `0` on each
`|K̄(z)⟩` and hence on the whole family; positivity then puts the closed span
in the kernel (the kernel of a positive self-adjoint operator is a closed
subspace), and `e^{-itH_kink}` restricts to the identity there.  `H_kink` is
well defined and symmetric on the dense span of finite-deviation
configurations of `ℋ_ref` because `h^{kink}` annihilates `|↑↑⟩` and `|↓↓⟩`
(K1's kernel), so only finitely many bonds act nontrivially on such a vector.
Both K1 and K2 are **PROVED** rows of `claims/CLAIMS.md`.

**Two fences on ⟨2⟩8, both binding.**
(i) This proves flatness *of the K1--K2 family*, not uniqueness, isolation, or
completeness of a kink band.  Those are claim **K4**, which is CONJECTURE with
finite-volume evidence only, and are **not** used here or anywhere in this
shard.
(ii) `𝒦_flat` does not contain the physical `Ψ`, which carries a magnon.
⟨2⟩8 therefore does **not** prove (NR), does not show that `𝒦_flat` exhausts
the low-energy kink states, and does not place D16 outside a ballistic class.
The exhaustiveness/no-recoil upgrade is precisely K4 (CONJECTURE).

**⟨2⟩9. QED** (LR3 proved from (NR); ⟨2⟩1--⟨2⟩6 and ⟨2⟩8 unconditional). □

---

## ⟨1⟩6. CLASS-LEVEL CONTENT — one theorem and one scoping requirement

**⟨2⟩1 (inventory: what the D16 proof actually consumed).**  Reading
⟨1⟩3--⟨1⟩5 backwards, the inputs are exactly:

| ingredient | used by | model-specific? |
|---|---|---|
| separable unital quasi-local `𝔄`, strongly continuous `α_t` | ⟨1⟩3 | no |
| `Q̂_{W,c_0}∈𝔄_W` self-adjoint, finite spectrum | ⟨1⟩3, ⟨1⟩4 | no (finite local dim) |
| `spec Q̂_{W,c_0}⊂ℤ` (D26(INT)) | ⟨1⟩4.⟨2⟩4 | no (INT) |
| (FN): selected vector an eigenvector of a conserved regularised charge | ⟨1⟩4.⟨2⟩4, ⟨1⟩5.⟨2⟩3 | no, but a hypothesis on the vector |
| scalar escape bound `4R_{W_m}\sqrt{G(m)}`; (ESC) is false on (H3) | ⟨1⟩4.⟨2⟩5 | **yes** |
| repaired two-clause (NR), including `sup_m` after pinching | ⟨1⟩5.⟨2⟩7 | **yes** |
| stationarity of the closed K1--K2 family span (no exhaustiveness) | ⟨1⟩5.⟨2⟩8 (motivation only) | **yes** |
| spectral gap | **nowhere** | — |
| Lieb--Robinson velocity | only through existence of `α_t` | — |

Two entries deserve emphasis.  A spectral gap is used at **no** step.  A
Lieb--Robinson bound is used only to build the infinite-volume dynamics, never
as a light-cone estimate.  Whatever the general theorem is, "gap +
Lieb--Robinson" is **not** its hypothesis set; see ⟨2⟩5.

*Justification.* Inspection of ⟨1⟩3.⟨2⟩7, ⟨1⟩4.⟨2⟩4--⟨2⟩5, ⟨1⟩5.⟨2⟩3--⟨2⟩8.

**⟨2⟩2 (THEOREM LR1-GEN — PROVED).**  Let `𝔄` be the quasi-local algebra of a
quantum spin system on a countable lattice with uniformly finite local
dimension, `α_t` a strongly continuous one-parameter group of
`*`-automorphisms of `𝔄` (e.g. any finite-range or exponentially decaying
translation-invariant interaction), `Ψ` any unit vector in any GNS
representation, `c_0` any cut and `Q̂_{W,c_0}∈𝔄_W` any self-adjoint window
observable with finite spectrum for each finite `W`.  For **any prescribed**
sequence `S_n→∞`, there is a subsequence `T_n=S_{n_j}` along which all the
Cesàro states and all double-Cesàro TPM laws converge, and each `p_W` is a
probability on the finite set `spec Q̂_W − spec Q̂_W`.  In particular
**D27(LR1) holds** with one sequence for all windows.

*Proof.* Verbatim ⟨1⟩3, whose ⟨2⟩7 records that only these three inputs were
used. □

**Consequence worth recording.**  Clause 1 existentially binds the `T_n` used
by clauses 2--3 and therefore must remain in D27.  LR1-GEN says that for any
starting `T_n→∞` a subsequence satisfies clause 1, so the substantive content
of (LR) lies entirely in clauses 2--3.  Proposed text is MP-1; this shard does
not edit `definitions.md`.

**⟨2⟩3 (PROPOSITION LR2-BOUND-GEN — PROVED bound, not a D16 instance).**
Add to LR1-GEN: D26(INT) so that `spec Q̂_{W,c_0}⊂κ+ℤ`; a conserved
regularised charge `𝒬` with `𝒬Ψ=𝒬_0Ψ` and `Q̂_{W_m,c_0}Ψ_t→𝒬_0Ψ_t` (the (FN)
register of ⟨1⟩1.⟨2⟩5); and the escape profile `G(m)` of (LRD.10).  If
`R_{W_m}²G(m)→0` then the exhaustion defect vanishes, with the explicit rate
`η_m=4R_{W_m}\sqrt{G(m)}`.  This is a reusable conditional implication.  It
has no D16 instance under (H3), where ⟨1⟩4.⟨2⟩5 proves (ESC) false.

*Proof.* Verbatim ⟨1⟩4.⟨2⟩1--⟨2⟩5, ⟨2⟩7; no D16-specific fact enters. □

**⟨2⟩4 (SCOPING REQUIREMENT LR3-SCOPE — what actually survives).**  Neither a
spectral gap nor a Lieb--Robinson velocity estimate is used anywhere in
⟨1⟩3--⟨1⟩5.  Therefore this shard supplies no proof that those two inputs
imply (LR).  Independently, `theory/ace-ld.md`'s proved `ACE-LD-obst′` says
that D27(LR3) fails under its explicit mean-tail-transport hypothesis
(M-ESC).  Any future class theorem must therefore include a no-mean-transport
clause strong enough to exclude (M-ESC), or derive one from named model
structure.

*Justification.* Inventory ⟨2⟩1 and `ACE-LD-obst′` in `theory/ace-ld.md`
⟨1⟩5.  This is a necessary scoping requirement, not a model counterexample.

**⟨2⟩5 (RETRACTION of the r1 class counterexample).**  The r1 sentence
"gap + Lieb--Robinson ⟹ (LR) is false" is withdrawn.  It named, constructed,
and cited no finite-range gapped model.  Its proposed mechanism, a rigid
charge-carrying core crossing the window, is also excluded by this shard's
own (LRD.5): on (FN), a sharp wall displaced by `d` changes `𝒬` by `d`, so
fixed `𝒬_0` pins its position.  An increment `|ν|≍2s|W_m|` would instead
require unbounded wrong-phase **block** growth.  No witness for that mechanism
is supplied here or by `ace-ld.md`, which explicitly withdrew the statement
that the D16 kink is ballistic.

*Justification.* (LRD.5), (FN), `theory/ace-ld.md`'s withdrawal, and the
absence of a named model in r1.  The surviving statement is ⟨2⟩4 only.

**⟨2⟩6 (what a full class theorem would have to add).**  Three items:
(a) (DPH) of ⟨1⟩4.⟨2⟩6 for verbatim LR2; (b) the (FN) register, which cannot
be upgraded to the REFUTED sector-wide `M-INDEX-LA-strong`; and (c) a genuine
no-mean-transport estimate controlling wrong-phase block **length**, such as
the repaired two-clause (NR).  (EDW) controls block number only.  K1--K2 show
stationarity only on their closed family span; using that span to assert
model-wide no recoil or to exhaust the low-energy kink states would require
K4 (CONJECTURE) and is forbidden.

**⟨2⟩7. QED** (LR1-GEN proved; LR2-BOUND-GEN conditional but empty for the
D16 (H3) class; the unsupported counterexample retracted; LR3-SCOPE retained). □

---

## §C. CHECKER REGISTRY — `theory/checks/lr_d16_check.py`

D16 at `J=1`, `Δ=2.5`, `N=12`, cut `c_0=6`, windows `W_1=[4,9] ⊂ W_2=[3,10] ⊂
W_3=[2,11]`, exact diagonalization in the conserved `S^z` sectors, exact
spectral time evolution, dressed-kink initial state (⟨1⟩1.⟨2⟩7).

The r2 checker was simplified gate-by-gate before registration.  C1(b) tests
the **raw** `q_w` array rather than already-rounded keys.  C3(a) constructs
`α_{t_±}(Q̂_W)` as independent matrices on an `N=8` sector and compares the
pinched square with the separately generated TPM law.  C3(d) tests only the
honest `W_m`-pinched majorant; C3(e) separately exposes the pinching's
`m`-dependence.  C4(b) evolves with `H_XXZ` and gates its energy conservation.
The tautological r1 C4(c) ratio and the subsumed r1 C6(b) row were deleted;
C4(c) now checks the actual finite-chain equality `⟨K|H_XXZ|K⟩≈C_K`.

| row | evidence / green value | registered mutant (exact exit path) |
|---|---|---|
| C1(a) | TPM normalisation, error `6.66e−16` | `c1-nonunitary` → C1(a) |
| C1(b) | raw `spec Q_W⊂ℤ`, support in `spec−spec`; both integer defects `0` | `c1-noninteger` (`q_w↦q_w+0.3`) → C1(b) |
| C2(a) | `Δ_W(t,t)=0`, error `1.11e−15` | `c2-unequal-time` → C2(a) |
| C2(b) | `|Δ_W|≤4R_Wε_W`, slack `−4.110` | `c2-small-constant` → C2(b) |
| C2(c) | `ε_W²≤⟨Q̂_{W^c}²⟩`, slack `−1.462e−4` | `c2-mismatched-complement` → C2(c) |
| C2(d) | **negative diagnostic:** `G=0.990,0.965,0.950`, `η=11.9,15.7,19.5`; (ESC) fails | `c2-delete-outside-data` → C2(d) |
| C3(a) | independent matrix (LRD.11): `1.2910437765` both routes, error `2.00e−15` | `c3-perturb-final-evolution` → C3(a) |
| C3(b) | edge split (LRD.12), slack `−3.280e−2` | `c3-mismatched-complement` → C3(b) |
| C3(c) | `𝒩_{W'}⪯𝒩_W`, `|Q̂_{W^c}|⪯𝒩_W`, exact | `c3-signed-majorant` → C3(c) |
| C3(d) | honest `W_m`-pinched fixed-observable bound, slack `−1.211e−1` | `c3-delete-majorant` → C3(d) |
| C3(e) | **negative diagnostic:** pinched term `1.383/1.797/1.872`, spread `0.490` | `c3-freeze-pinching` → C3(e) |
| C4(a) | bond EDW, minimum eigenvalue `−0.0` | `c4-wrong-gap` → C4(a) |
| C4(b) | `H_XXZ` energy drift `1.11e−14`; `max⟨D⟩=3.053≤4.753` | `c4-kink-propagator` → C4(b) |
| C4(c) | `⟨K|H_XXZ|K⟩=1.1456439081`, `C_K=1.1456439237` | `c4-sharp-calibration` → C4(c) |
| C5(a) | K1--K2 local kernel, residual `8.01e−19` | `c5-wrong-root` → C5(a) |
| C5(b) | distinct kink-bond positivity gate, minimum eigenvalue `−0.0` | `c5-overstrong-field` → C5(b) |
| C6(a) | sharp/dressed overlap `0.9545`, sharp energy `0.1044` | `c6-identify-sharp-dressed` → C6(a) |

**Exit paths and reachability.**
`python3 -O theory/checks/lr_d16_check.py` → **exit 0**, 17/17 green.
`python3 -O theory/checks/lr_d16_check.py --red-all` → **exit 1, RED-OK
17/17**.  It prints the row-by-row table above verbatim as exit paths.  Each
individual `--red MODE` evaluates the target row group directly, evaluates
every gate in that group without short-circuiting, and exits 1 only when the
failed-row list is **exactly** the registered singleton; a missed or collateral
path exits 2.  Thus no row is unreachable and no two modes are bit-identical
in effect.  Data mutations include a non-unitary propagator, noninteger raw
spectrum, mismatched complement, deleted outside-count data, perturbed final
Heisenberg evolution, frozen `W_1` pinching, wrong finite-volume propagator,
and sharp/dressed substitution.  No bare `assert` appears, so `-O` is strict.

---

## §H. HONEST STATUS

**Proved unconditionally for D16 (nothing further assumed beyond D16, D17 and
the standing setup).**
1. **D27(LR1)** — ⟨1⟩3.  Complete, and it needed less than expected: only
   separability of `𝔄`, strong continuity of `α_t`, and finiteness of
   `spec Q̂_{W,c_0}`.  It generalises verbatim (⟨1⟩6.⟨2⟩2, **LR1-GEN**): from
   any prescribed `T_n→∞`, a subsequence supplies clause 1.  Clause 1 remains
   the binder for the sequence quantified over by clauses 2--3.
2. The exact second-moment identity (LRD.11) and the equal-time and
   boundary-current forms of the LR2 defect, (LRD.7).
3. The **monotonicity lemma** ⟨1⟩5.⟨2⟩4: the escaped-content majorant is
   monotone in the window, so the family of majorising observables collapses
   to `𝒩_{W_1}`.  The `W_m`-pinched state remains `m`-dependent, so `sup_m`
   remains in (NR)'s second clause.
4. The **energy--domain-wall bound (EDW)** ⟨1⟩5.⟨2⟩6:
   `H_{XXZ} ⪰ \tfrac{J}{2}(Δ−1)D`, hence `⟨D(t)⟩ ≤ 2E_0/(J(Δ−1))` for all
   time.  Elementary, and apparently not recorded elsewhere in the campaign.
5. **Flatness of the K1--K2 kink family** ⟨1⟩5.⟨2⟩8, derived here from the two
   PROVED rows K1 and K2 and nothing else: the closed span of the exact
   zero-energy family lies in `ker H_kink`, so every state in that span is
   stationary.  **This is not K4**: it says nothing about states outside the
   span and no model-wide no-recoil claim is made.

**Proved conditionally, with the condition named.**
6. **LRD-2-BND** — ⟨1⟩4.⟨2⟩5 — the scalar estimate with
   `η_m=4R_{W_m}\sqrt{G(m)}`.  Its abstract (ESC) consequence is valid but
   empty for the D16 (H3) class; it is not listed as a D16 LR2′ result.
7. **D27(LR3)** — ⟨1⟩5.⟨2⟩7 — conditional on the repaired **two-clause
   (NR)**, including `sup_m` in the pinched clause, with tail `2S_{NR}/M`.

**Left OPEN, and stated as such.**
8. **D27(LR2) verbatim** is **not** proved.  ⟨1⟩4.⟨2⟩6 isolates the residue
   (DPH) and marks it CONJECTURE.  The bound of ⟨1⟩4.⟨2⟩3 is uniform in the
   times but does not vanish at fixed `W`, because the outgoing magnon
   contributes `O(1)` to `𝒩_W`; the exponentially small kink tail is not the
   obstruction.  The r1 D16 **(LR2′) is WITHDRAWN** because (ESC) is false.
   We did **not** patch this by asserting operator
   asymptotic commutativity, which D27 forbids and which would be a strictly
   stronger claim.  The abstract downstream mitigation has no D16 antecedent;
   `M-INDEX-spec` is unaffected and unimproved, and `M-INDEX-fin` is safe.
9. **The two clauses of (NR)** themselves.  (EDW) bounds the **number** of phase boundaries uniformly
   in time; it does not bound their **length**, because a one-dimensional
   wrong-phase block of any length carries the same `O(1)` Ising cost.  That
   is the whole gap.
10. **D27(LR3)'s optional convenience clause** (weak convergence of
    `{p_{W_m}}`): not proved, not needed, not claimed.
11. The **class theorem beyond LR1-GEN**.  The r1 alleged counterexample to
    "gap + Lieb--Robinson ⟹ (LR)" is retracted: no model was supplied and its
    core-transit mechanism contradicts (FN)/(LRD.5).  What survives is the
    scoping requirement LR3-SCOPE: this shard uses neither a gap nor an LR
    velocity, and `ACE-LD-obst′` independently requires a no-mean-transport
    clause in any future class theorem.

**Numerical evidence only (not proof).**  The §C table.  At `N=12`, C2(d)
shows `G=0.990,0.965,0.950` and `η=11.9,15.7,19.5`, evidence **against** the
r1 D16 LR2′ claim.  C3(e) shows the pinched term
`1.383/1.797/1.872`, evidence for retaining `sup_m`.  Algebraic rows certify
the displayed identities and operator inequalities; none certifies
asymptotic physics.  C4(c) checks the non-tautological finite-chain equality
`⟨K|H_XXZ|K⟩=1.1456439081` against `C_K=1.1456439237`.

**Bearing on the live cross-lane obstruction.**  ⟨1⟩5.⟨2⟩4 proves only that
the majorising **observable** can be fixed to `𝒩_{W_1}`.  The `W_m`-pinched
state remains `m`-dependent, so the corresponding term stays under `sup_m`.
An increment `|ν|≍2s|W_m|` cannot arise from the `c_0` offset (which cancels
at fixed `W`) and, under (FN), cannot arise from rigid sharp-core transit; it
requires wrong-phase block growth in the state or pinched state.  Separately,
`ACE-LD-obst′` proves that mean tail transport must be excluded by a class
theorem.  No model counterexample is claimed here.

**Register discipline inherited and respected.**  `δx` is never claimed
quantized; it is a `{p_ν}`-average (`M-INDEX-spec`'s adjudicated scoping).  No
sector-wide charge operator is constructed (`M-INDEX-LA-strong` is REFUTED).
K4 is neither cited nor used as proved: every K1--K2 consequence is scoped to
the closed span of that family, with no model-wide no-recoil or exhaustiveness
claim.  The `n≥2` display of ML4-Ward (9) is not used anywhere.  Bethe appears
nowhere.  No reference is quoted, from `refs/` or otherwise; every leaf cites
a D-number, a claim id, or a named computation defined in this file.

---

## §MP. MERGE PROPOSALS (for the orchestrator; nothing outside this lane is edited)

**MP-1 — `definitions.md`, D27.**  After the sentence ending
"`converge.  The sum is over q∈spec Q̂_{W,c_0} and absent spectral values
contribute zero.`", append:

> *(For any `T_n→∞` there is a subsequence along which clause 1 holds, whenever
> `𝔄` is separable, `α_t` is strongly continuous, and `spec Q̂_{W,c_0}` is
> finite at fixed `W`.  Clause 1 is retained because it existentially binds
> the common sequence used by clauses 2--3; with that binder understood, the
> substantive content of (LR) lies entirely in clauses 2--3.  In clause 2,
> "tends to zero" means along this same common sequence.  Proof:
> `theory/lr-d16.md` ⟨1⟩3 and ⟨1⟩6.⟨2⟩2, LR1-GEN.)*

**MP-2 — HOLD.**  Do not merge the r1 LR2′ mitigation: its antecedent is
false for D16.  `M-INDEX-spec` is unaffected and unimproved; `M-INDEX-fin` is
safe.  Lane-local cleanup proposed separately: `memory-index.md`
⟨1⟩5.⟨2⟩1 should cite D27's clause-1 TPM display rather than D27(LR2), because
it uses no dephasing limit.

**MP-3 — `claims/CLAIMS.md`: two PROVED rows; LR-D16 remains HOLD.**

| id | statement | proposed status | depends-on | where-proved | where-tested |
|---|---|---|---|---|---|
| LR1-GEN | For any quantum spin system with separable quasi-local `𝔄`, strongly continuous `α_t`, and finite-spectrum window observables, every prescribed `T_n→∞` has a subsequence on which both Cesàro states and all double-Cesàro TPM laws converge simultaneously for every fixed `W`; each limit is a probability on `spec Q̂_W−spec Q̂_W` (and under D26, on `ℤ`).  No gap, LR velocity, scattering, or property of `Ψ` beyond normalisation is used. | PROVED | D26, D27 | theory/lr-d16.md ⟨1⟩3, ⟨1⟩6.⟨2⟩2 | theory/checks/lr_d16_check.py C1(a,b): green 0; `--red c1-nonunitary`, `--red c1-noninteger` each exit 1 |
| LR-D16-EDW | In D16, `h^{XXZ}_{x,x+1} ⪰ \tfrac{J}{2}(Δ−1)P^{DW}_x`, hence in infinite volume `H_{XXZ} ⪰ \tfrac{J}{2}(Δ−1)D` and `⟨Ψ,α_t(D)Ψ⟩ ≤ 2E_0/(J(Δ−1))` for all `t`, with `E_0=⟨Ψ,H_{XXZ}Ψ⟩` conserved and finite on a D17 packet.  Bounds the NUMBER of phase boundaries, not their length. | PROVED | D16 | theory/lr-d16.md ⟨1⟩5.⟨2⟩6 | theory/checks/lr_d16_check.py C4(a--c): green 0; `--red c4-wrong-gap`, `--red c4-kink-propagator`, `--red c4-sharp-calibration` each exit 1; finite open-chain dynamics uses `H_XXZ`, not `H_kink` |

`LR-D16` remains **HOLD**: LR1 is unconditional; D16 LR2′ is withdrawn and
LR2 remains open; LR3 holds only under repaired two-clause (NR).

**MP-4 — `theory/TRIANGLE.md` / `HANDOFF.md` one-liner.**  "`M-INDEX-spec`
still has no fully unconditional dynamical instance: for D16, LR1 is now
unconditional and LR3 is reduced to the single named input (NR), but LR2
verbatim remains open (residue (DPH)).  The honest headline is *one clause
proved outright, one clause proved in a weakened form that suffices
downstream, one clause reduced to a single named dynamical hypothesis*."
