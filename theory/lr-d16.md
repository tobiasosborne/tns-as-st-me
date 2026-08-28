<!-- ROLE: proposer shard for bd tns-xf4 — prove D27(LR1--LR3) for the D16
     easy-axis XXZ kink sector.  Lane: this file + theory/checks/lr_d16_check.py.
     Nothing else in the repo is edited; shared-file text is in MERGE PROPOSALS. -->

# (LR) for D16 — charge-history local relaxation in the easy-axis XXZ kink sector

**Round r1 proposer draft, 2026-08-29.  Self-status: SKETCH until the L6 loop
converges.  Read the HONEST STATUS section (§H) before citing anything here.**

Target: D27 (`definitions.md`), clauses (LR1), (LR2), (LR3), for the D16 model
and a D17 kink packet.  Motivation: `M-INDEX-spec` (`claims/CLAIMS.md`) is
PROVED but conditional, with D27 assumed on every model and therefore with no
unconditional dynamical instance.  This shard supplies one instance as far as it
honestly goes and names, precisely, what is left open.

Summary of the verdict reached below (details in §H):

| clause | D16 verdict |
|---|---|
| LR1 | **PROVED unconditionally** (⟨1⟩3), and at class level (⟨1⟩6) |
| LR2 | verbatim **OPEN**; the weakened **(LR2′)** is PROVED (⟨1⟩4) and is shown to suffice for every downstream use in `theory/memory-index.md` |
| LR3 | **PROVED from one named dynamical input (NR)** (⟨1⟩5); the `sup_m` is removed unconditionally by the monotonicity lemma ⟨1⟩5.⟨2⟩4, and the energy--domain-wall bound ⟨1⟩5.⟨2⟩6 is unconditional |
| class statement | **CONJECTURE** (⟨1⟩6); LR1 alone generalises with a proof |

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
translates *at one common time*.  `W_m=[a_m,b_m]↑ℤ` is D27's padded
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

- **(LRD-2′) = a weakening of D27(LR2), unconditional given (H1)--(H4).**
  Write `Δ_W(t_-,t_+):=⟨Ψ,[𝒟_{W,t_-}(Q̂_{W,c_0}(t_+))−Q̂_{W,c_0}(t_+)]Ψ⟩` for
  D27's first-moment nondemolition defect.  Then
  `limsup_n |double-Cesàro average of Δ_{W_m}| ≤ η_m` with an **explicit**
  `η_m = 4R_{W_m}·ε_{W_m}` and `η_m→0` along every padded exhaustion whose
  padding grows at least logarithmically faster than `log|W_m|` — in
  particular along the geometric or linear paddings used in practice.  Proved
  in ⟨1⟩4.  **D27(LR2) verbatim (`→0` at *fixed* `W`) is NOT proved here**;
  ⟨1⟩4.⟨2⟩6 isolates the exact residue and names it (DPH).

- **(LRD-3) = D27(LR3), conditional on the single named input (NR) of
  ⟨1⟩5.⟨2⟩7.**  `lim_{M→∞} sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν)=0`.  The `sup_m`
  is eliminated *unconditionally* by the monotonicity lemma ⟨1⟩5.⟨2⟩4; the
  domain-wall count is bounded *unconditionally* and uniformly in time by
  ⟨1⟩5.⟨2⟩6; (NR) is the residual dynamical statement that no wrong-phase
  block grows without bound, and ⟨1⟩5.⟨2⟩8 records the D16 mechanism
  (exact flatness of the K1--K2 kink family) that makes it plausible and
  numerically visible.

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

**Remark (why the D16 instance is not an instance of the ballistic case).**
D27(LR3) is known to be *false* for a model whose charge-carrying core
transits a window ballistically: the escaped increment then grows like the
window, `|ν|≍2s|W_m|`, and no exhaustion is first-moment tight.  ⟨1⟩5.⟨2⟩4
shows that this failure can never be manufactured by the window geometry
alone — the outcome bound is `m`-independent — so it must come from genuine
core transport.  The structural feature of D16 that removes it is
⟨1⟩5.⟨2⟩8: the whole zero-energy kink family of K1--K2 sits at one common
energy, so the wall carries no group velocity.  This is stated as the
scoping constraint on the class statement in ⟨1⟩6: **"gap + Lieb--Robinson"
alone cannot suffice, because a gapped finite-range model with a mobile
charged core satisfies both and fails LR3.**

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

## ⟨1⟩4. LR2 — the exact defect identities, (LR2′) PROVED, verbatim LR2 OPEN

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

**⟨2⟩5 (LEMMA LR2′ — PROVED).**  Define the **escape profile**

  `G(m) := sup_{t∈ℝ} ⟨Ψ, α_t(𝒩_{W_m})²Ψ⟩ ∈[0,∞]`.                **(LRD.10)**

Then for every `n` and every `m`,
`|T_n^{-2}∫∫ Δ_{W_m}(t_-,t_+)\,dt_-dt_+| ≤ η_m := 4R_{W_m}\sqrt{G(m)}`, and
therefore the double-Cesàro average of `Δ_{W_m}` has `limsup_n` at most
`η_m`.  Consequently **(LR2′)** holds — the defect vanishes along the
exhaustion — whenever `R_{W_m}^2\,G(m)→0`.  Two unconditional facts about
`G`: (i) `G` is non-increasing in `m`, because `𝒩_{W_m}` is a sum of
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
`W`: for the D16 dressed kink the window charge is **not** exactly sharp,
because the K1--K2 kink profile has exponentially small but nonzero weight
across each window edge.  The missing statement is therefore

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

**⟨2⟩7 (LR2′ suffices for every downstream use of LR2 in `memory-index.md`).**
`theory/memory-index.md` consumes D27(LR2) at exactly one leaf,
⟨1⟩7.⟨2⟩1, to convert (IDX.4) into
`Σ_ν ν p_W(ν)=ω_W^-(Q̂_{W,c_0})−ω_W^+(Q̂_{W,c_0})` at fixed `W`.  Replacing
LR2 by (LR2′) replaces that equality at `W_m` by
`|Σ_ν ν p_{W_m}(ν) − [ω_{W_m}^-(Q̂)−ω_{W_m}^+(Q̂)]| ≤ η_m`.
Every later step of ⟨1⟩7 is unaffected: ⟨2⟩2 is the exact identity (IDX.1)
with the scalar `−2sc_0` cancelling and carries the same `η_m`; ⟨2⟩3 (support
quantization, Prokhorov on `ℤ`) uses LR1 and LR3 only and never LR2; and
⟨2⟩4 takes `m→∞`, where `η_m→0` kills the error.  Hence **(IDX.2), the
theorem's conclusion, holds verbatim with (LR2) weakened to (LR2′)** — the
subsequential-value and support statements of `M-INDEX-spec` are unchanged.
The proposed replacement text is in MERGE PROPOSALS (MP-2); this shard does
not edit `theory/memory-index.md`.

*Justification.* `theory/memory-index.md` ⟨1⟩6 (IDX.4), ⟨1⟩7.⟨2⟩1--⟨2⟩4,
D27, and ⟨2⟩5.  Note the error is introduced *before* the spatial limit and
removed *by* it, so ⟨1⟩1.⟨2⟩8's limit order is respected, not circumvented.

**⟨2⟩8. QED** (LR2′ proved; LR2 verbatim reduced to (DPH) and left OPEN). □

---

## ⟨1⟩5. LR3 — first-moment tightness

**ASSUME.** (H1)--(H6) of ⟨1⟩2, and D27(LR1) as established in ⟨1⟩3.

**PROVE.** `lim_{M→∞} sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν)=0`, given the single
named input (NR) of ⟨2⟩7.  Steps ⟨2⟩1--⟨2⟩6 are unconditional.

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

**⟨2⟩4 (MONOTONICITY LEMMA — the `sup_m` is removed unconditionally).**  For
`W⊆W'` (both containing `c_0`), `𝒩_{W'} ≤ 𝒩_W` as operators, and
`|Q̂_{W^c,c_0}| ≤ 𝒩_W`.  Hence along the exhaustion, for every `m`, every
`t_±`, and every `n`,

  `Σ_νν²p_{W_m;t_-,t_+} ≤ 2⟨Ψ,α_{t_-}(𝒩_{W_1})²Ψ⟩
                          + 2Σ_q‖α_{t_+}(𝒩_{W_1})φ_q‖²`,          **(LRD.13)**

a bound that **does not depend on `m`**.

*Justification.* `𝒩_W=Σ_{x<a}(½−S^z_x)+Σ_{x>b}(S^z_x+½)` is a sum of
non-negative diagonal terms over `ℤ∖W` (⟨1⟩1.⟨2⟩4); enlarging `W` deletes
terms, so `𝒩_{W'}≤𝒩_W` pointwise on configurations, hence as operators, and
`α_t` preserves operator order.  `|Q̂_{W^c}|≤𝒩_W` is (LRD.3).  Named
computation **LRD-MONO** (the same computation as ⟨1⟩4.⟨2⟩5(i)).

**Remark (this is the answer to the `sup_m` trap, and to the ballistic
objection).**  D27(LR3) is a `sup_m` statement, uniform over the exhaustion,
not fixed-`m` decay with an `m`-dependent constant; ⟨2⟩4 shows the required
uniformity is *free*, because the escaped-content majorant is monotone in the
window and the **smallest** window dominates.  In particular an escaped
increment growing like the window, `|ν|≍2s|W_m|`, can never be produced by
window geometry alone: by (LRD.13) it would force the *fixed*, smallest-window
quantity `⟨α_t(𝒩_{W_1})²⟩` to diverge, i.e. genuine unbounded transport of the
charged core.  Whether such transport occurs is a dynamical question about the
model, settled model-by-model; ⟨2⟩8 identifies the D16 feature that answers it
here.  Nothing in this remark asserts or denies the claim of any other lane.

**⟨2⟩5 (passing the bound to the fixed-window limit laws).**  If the right
side of (LRD.13) is finite, call it `S`.  Then `Σ_νν²p_{W_m,n} ≤ S` for every
`n` by convexity of the double-Cesàro average, and by ⟨1⟩3.⟨2⟩5
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

  **(NR) — no unbounded escaped content.**  With `W_1` the smallest window of
  the exhaustion,
  `S_{NR} := sup_{t_-<t_+}\big[2⟨Ψ,α_{t_-}(𝒩_{W_1})²Ψ⟩
   + 2Σ_q‖α_{t_+}(𝒩_{W_1})E_{W_1,t_-}({q})Ψ‖²\big] < ∞.`

**THEOREM (LRD-3).**  Under (H1)--(H6) and (NR), D27(LR3) holds, with the
explicit tail bound `sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν) ≤ 2S_{NR}/M`.

*Proof.* ⟨2⟩4 gives (LRD.13) with right side `≤S_{NR}` for every `m`; ⟨2⟩5
transports it to the limit laws; ⟨2⟩2 converts it into the tail statement.
□

**Scope of (NR), stated plainly.**  (NR) has two clauses of unequal weight.
The first, `sup_t⟨α_t(𝒩_{W_1})²⟩<∞`, says the total wrong-phase content
outside one fixed window has a bounded second moment for all time — the honest
form of "the wall does not run away and no bubble grows without bound".  The
second says the same after the first TPM measurement; it is the statement
that a projective measurement of the window charge does not itself create
unbounded escaped content, and it is implied by the first whenever `𝒩_{W_1}`
is bounded on the smallest `α`-invariant subspace containing `Ψ`.  (EDW)
(⟨2⟩6) proves *unconditionally* that the **number** of phase boundaries is
bounded uniformly in time; what (EDW) does not control is their **length**,
because in one dimension a wrong-phase block of any length carries the same
`O(1)` Ising cost.  That gap is precisely (NR), and naming it is the honest
statement of where this shard stops.

**⟨2⟩8 (the D16 feature that makes (NR) the right hypothesis: exact flatness
of the K1--K2 family).**  Let `𝒦_flat` be the closed span in `ℋ_ref` of the
K2 zero-energy family `{|K̄(z)⟩}` of ⟨1⟩1.⟨2⟩2.  Then `H_kink` vanishes on
`𝒦_flat`, so `α_t` acts on it trivially (up to the constant phase `e^{-iC_Kt}`
in the `H_XXZ` normalisation): **every kink wave packet built from the D16
family is exactly stationary, and the D16 wall carries no group velocity.**

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
⟨2⟩8 therefore does **not** prove (NR); it identifies the structural reason
(NR) is the right hypothesis for D16 rather than a disguised falsehood, and it
is the sentence that separates D16 from the ballistic-transit class in which
D27(LR3) is known to fail: there the charged core has a nonzero group
velocity, here the exact zero-energy family has none.

**⟨2⟩9. QED** (LR3 proved from (NR); ⟨2⟩1--⟨2⟩6 and ⟨2⟩8 unconditional). □

---

## ⟨1⟩6. THE CLASS STATEMENT (stretch goal) — one theorem, one conjecture

**⟨2⟩1 (inventory: what the D16 proof actually consumed).**  Reading
⟨1⟩3--⟨1⟩5 backwards, the inputs are exactly:

| ingredient | used by | model-specific? |
|---|---|---|
| separable unital quasi-local `𝔄`, strongly continuous `α_t` | ⟨1⟩3 | no |
| `Q̂_{W,c_0}∈𝔄_W` self-adjoint, finite spectrum | ⟨1⟩3, ⟨1⟩4 | no (finite local dim) |
| `spec Q̂_{W,c_0}⊂ℤ` (D26(INT)) | ⟨1⟩4.⟨2⟩4 | no (INT) |
| (FN): selected vector an eigenvector of a conserved regularised charge | ⟨1⟩4.⟨2⟩4, ⟨1⟩5.⟨2⟩3 | no, but a hypothesis on the vector |
| escape profile `G(m)` with `R_{W_m}²G(m)→0` | ⟨1⟩4.⟨2⟩5 | **yes** |
| (NR): uniform escaped-content second moment | ⟨1⟩5.⟨2⟩7 | **yes** |
| flat K1--K2 family / zero core velocity | ⟨1⟩5.⟨2⟩8 (motivation for (NR)) | **yes** |
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
observable with finite spectrum for each finite `W`.  Then **D27(LR1) holds**:
there is a single sequence `T_n→∞` along which all the Cesàro states and all
the double-Cesàro TPM laws converge, and each `p_W` is a probability on the
finite set `spec Q̂_W − spec Q̂_W`.

*Proof.* Verbatim ⟨1⟩3, whose ⟨2⟩7 records that only these three inputs were
used. □

**Consequence worth recording.**  D27 carries LR1 as a *hypothesis*.  By
LR1-GEN it is a **theorem** for every model in the campaign's setting, so
D27(LR1) can be demoted from hypothesis to corollary without weakening
`M-INDEX-spec`.  Proposed text is MP-1 in MERGE PROPOSALS; this shard does not
edit `definitions.md`.

**⟨2⟩3 (PROPOSITION LR2′-GEN — PROVED, conditional on the escape profile).**
Add to LR1-GEN: D26(INT) so that `spec Q̂_{W,c_0}⊂κ+ℤ`; a conserved
regularised charge `𝒬` with `𝒬Ψ=𝒬_0Ψ` and `Q̂_{W_m,c_0}Ψ_t→𝒬_0Ψ_t` (the (FN)
register of ⟨1⟩1.⟨2⟩5); and the escape profile `G(m)` of (LRD.10).  If
`R_{W_m}²G(m)→0` then (LR2′) holds, with the explicit rate
`η_m=4R_{W_m}\sqrt{G(m)}`, and by ⟨1⟩4.⟨2⟩7 that suffices for every downstream
use of D27(LR2) in `theory/memory-index.md`.

*Proof.* Verbatim ⟨1⟩4.⟨2⟩1--⟨2⟩5, ⟨2⟩7; no D16-specific fact enters. □

**⟨2⟩4 (CONJECTURE LR3-CLASS — NOT proved).**  Let `H` be translation
invariant, finite range, `U(1)`-invariant in D10(a)'s sense on a spin-`S`
chain, with two stationary product-like vacua of densities `±s` and a kink
sector `𝒦_{αβ}`.  Assume in addition:

1. **(C-gap)** a spectral gap `Δ_M>0` above each vacuum;
2. **(C-FN)** the selected D17 packet satisfies (FN);
3. **(C-imm)** *immobile charged core*: the zero-energy (or lowest) kink
   manifold is exactly degenerate under lattice translation, so the core
   carries identically zero group velocity — the property proved for D16 in
   ⟨1⟩5.⟨2⟩8 from K1--K2;
4. **(C-disp)** the non-core content disperses: for one fixed window `W_1`,
   `sup_t⟨Ψ,α_t(𝒩_{W_1})²Ψ⟩<∞`, and the same after a `Q̂_{W_1}` pinching.

Then D27(LR1)--(LR3) hold, and with ⟨2⟩3 also (LR2′).

**Status: CONJECTURE.**  Clauses 1--3 do not imply clause 4, and clause 4 *is*
(NR): the conjecture as displayed is therefore honest but weak — it asserts
that (C-gap)+(C-imm) should let one *derive* (C-disp) rather than assume it.
**The missing step, named:** a bound showing that a gapped `U(1)` chain with an
immobile core cannot accumulate unbounded wrong-phase block *length* outside a
fixed window as `t→∞`.  (EDW) (⟨1⟩5.⟨2⟩6) proves the analogous statement for
block *number* in D16 and is the natural template; what is absent is any
mechanism converting "finitely many phase boundaries, uniformly in time" into
"boundaries that do not separate ballistically".  In a gapped model the
expected mechanism is that an anti-core excitation costs `Ω(Δ_M)` and its
separation from the core is not energetically free, but the Ising cost of a
one-dimensional block is length-independent, so energy alone cannot deliver
it.  A proof would need a genuinely dynamical input — a propagation estimate
for the core-anti-core pair — and this shard does not have one.

*Justification.* The hypothesis list is exactly the inventory of ⟨2⟩1;
the "not proved" verdict is the honest reading of ⟨1⟩5.⟨2⟩7's scope
paragraph.

**⟨2⟩5 (SCOPING FENCE — "gap + Lieb--Robinson ⟹ (LR)" is FALSE as a class
statement, and which clause fails).**  D27(LR3) fails for a model whose
charge-carrying core transits a window ballistically: the fixed-window time
limit then puts the core outside `W` for all large `t_+`, the outcome
saturates at the window edge, and the escaped increment grows like the window,
`|ν|≍2s|W_m|`, so no exhaustion is first-moment tight.  Such a model can be
finite range and gapped.  Therefore **(C-imm), or some equivalent
no-ballistic-charge-transport clause, is not decorative — it is load-bearing,
and any class statement without it is refutable.**  Note what does *not* fail
there: LR1 still holds by ⟨2⟩2 (which uses nothing dynamical), and the LR2
analysis of ⟨1⟩4 is untouched; the failure is confined to LR3, and by
⟨1⟩5.⟨2⟩4 it is confined further, to the single fixed quantity
`sup_t⟨α_t(𝒩_{W_1})²⟩` at the smallest window.  The `c_0` offset plays no
role in this: it cancels identically in `ν=q_-−q_+` at fixed `W`
(`theory/memory-index.md` ⟨1⟩5.⟨2⟩3, re-derived here at ⟨1⟩1.⟨2⟩3).

*Justification.* ⟨1⟩1.⟨2⟩3 (`‖Q̂_W‖≤R_W`, saturation at the edge),
⟨1⟩5.⟨2⟩4, ⟨1⟩3.⟨2⟩7.  This paragraph asserts nothing about the truth of any
other lane's shard; it records only what the D16 proof needs in order not to
generalise falsely.

**⟨2⟩6 (what a full class theorem would have to add).**  Beyond ⟨2⟩4's missing
step, two items.  (a) (DPH) of ⟨1⟩4.⟨2⟩6, which is a genuine dephasing
statement and is likely the harder of the two; note that ⟨1⟩4.⟨2⟩7 makes it
*unnecessary* for `M-INDEX-spec`, so a class theorem may reasonably be stated
with (LR2′) in place of (LR2).  (b) The (FN) register: it is a hypothesis on
the selected vector, and `M-INDEX-LA-strong` is REFUTED, so it cannot be
upgraded to a sector-wide operator statement; a class theorem must carry it as
a hypothesis, exactly as ⟨2⟩4 does.

**⟨2⟩7. QED** (one class theorem, LR1-GEN; one class proposition, LR2′-GEN;
one explicitly fenced CONJECTURE, LR3-CLASS). □

---

## §C. CHECKER REGISTRY — `theory/checks/lr_d16_check.py`

D16 at `J=1`, `Δ=2.5`, `N=12`, cut `c_0=6`, windows `W_1=[4,9] ⊂ W_2=[3,10] ⊂
W_3=[2,11]`, exact diagonalization in the conserved `S^z` sectors, exact
spectral time evolution, dressed-kink initial state (⟨1⟩1.⟨2⟩7).

*Notation bridge (checked, not assumed).*  ⟨1⟩1.⟨2⟩2 writes the (LRD-O) family
as the `ℤ₂`-image `⊗_n(|↓⟩_n+zq^n|↑⟩_n)`; the checker builds it in the
equivalent normalisation `⊗_n(|↑⟩_n+zq^{-n}|↓⟩_n)`, which is the same family
(divide each factor by `zq^n` and rename `z↦z^{-1}`) and is the form in which
the K1 kernel condition reads `a_n=q\,a_{n+1}` directly.  Row LRD-C5(a)
verifies bondwise annihilation in **all 13** `S^z` sectors, which is the
content actually used by ⟨1⟩5.⟨2⟩8; row LRD-C1(c)'s failure under the wrong
root `q=Δ+\sqrt{Δ²−1}` (recorded below) shows the bridge is load-bearing and
not a free reparametrisation.  **These are
algebraic certificates — identities and operator inequalities — not asymptotic
physics: `N=12` cannot hold a ballistic window, and no row claims it does.**
The asymptotic evidence for (LR) is `theory/checks/memory_index_probe.py`,
re-run for this round and PASS (exit 0), which is not duplicated here.

| row | certifies | green value |
|---|---|---|
| LRD-C1(a) | ⟨1⟩3.⟨2⟩4,⟨2⟩6 normalisation of `p_{W,n}` | `max|Σp−1| = 7.8e−16` |
| LRD-C1(b) | ⟨1⟩3.⟨2⟩6 support `⊆ spec−spec ⊂ ℤ`, `|allowed|=11` | exact |
| LRD-C1(c) | ⟨1⟩3 Cesàro contraction (diagnostic gate) | `TV(8,24)=0.130 → TV(24,72)=0.026` |
| LRD-C2(a) | ⟨1⟩4.⟨2⟩2 `Δ_W(t,t)=0` identically | `3.8e−15` |
| LRD-C2(b) | ⟨1⟩4.⟨2⟩3 `|Δ_W| ≤ 4R_Wε_W(t_-)` | slack `−1.0` (bound loose, as expected at `R_W=3`) |
| LRD-C2(c) | ⟨1⟩4.⟨2⟩4 `ε_W² ≤ ⟨Q̂_{W^c}²⟩` — the (FN)/(LRD.5) step | slack `−1.5e−4` |
| LRD-C2(d) | ⟨1⟩4.⟨2⟩5(i) escape profile falls with padding | `G = 0.9897, 0.9637, 0.9315` |
| LRD-C3(a) | ⟨1⟩5.⟨2⟩1 second-moment identity (LRD.11) | `max|LHS−RHS| = 4.4e−16` |
| LRD-C3(b) | ⟨1⟩5.⟨2⟩3 edge split (LRD.12) | slack `−3.3e−2` |
| LRD-C3(c) | ⟨1⟩5.⟨2⟩4 monotonicity `𝒩_{W'} ≤ 𝒩_W`, `|Q̂_{W^c}| ≤ 𝒩_W` | exact |
| LRD-C3(d) | ⟨1⟩5.⟨2⟩4 the `m`-uniform bound (LRD.13) | slack `−1.2e−1` over 3 windows |
| LRD-C4(a) | ⟨1⟩5.⟨2⟩6 `h^{XXZ} ⪰ (J/2)(Δ−1)P^{DW}` (`4×4`) | `min eig = −0.0e0` |
| LRD-C4(b) | ⟨1⟩5.⟨2⟩6 `⟨D(t)⟩ ≤ 2E_0/(J(Δ−1))` over `t∈[−12,12]` | `3.084 ≤ 4.753` |
| LRD-C4(c) | ⟨1⟩5.⟨2⟩6 bare-kink value | `E_0/c = 1.5275 = \sqrt{(Δ+1)/(Δ−1)}` **to 4 decimals, on a finite chain** |
| LRD-C5(a) | ⟨1⟩5.⟨2⟩8 flatness: `‖H_kink|K̄(z)⟩‖=0` in **all 13** `S^z` sectors | `2.9e−16` |
| LRD-C5(b) | ⟨1⟩5.⟨2⟩8 `H_kink ⪰ 0` with `0` attained in every sector | `[−4.1e−14, +4.1e−14]` |
| LRD-C6(a) | ⟨1⟩1.⟨2⟩7 sharp kink is inadmissible | `|⟨sharp|dressed⟩|²=0.9545`, `E_kink(sharp)=0.1044` |
| LRD-C6(b) | ⟨1⟩1.⟨2⟩7 the state actually used is a zero mode | `4.5e−17` |

**Exit paths.**  Green: `python3 -O theory/checks/lr_d16_check.py` → **exit 0**,
18/18 rows PASS.  Four red mutations, each **exit 1**:

| mutation | what it breaks | rows that catch it |
|---|---|---|
| `--red-split` | complement charge taken on a mismatched window, so `Q̂_W+Q̂_{W^c}` is no longer the conserved scalar — kills (LRD.5) | LRD-C2(c) slack `+1.0e−1`, LRD-C3(b) slack `+2.48` |
| `--red-edw` | `(Δ+1)` in place of `(Δ−1)` in (EDW) | LRD-C4(a) `min eig = −1.0`, C4(b) slack `+1.05`, C4(c) |
| `--red-monotone` | majorises the escaped charge by the **signed** `Q̂_{W^c}` instead of the non-negative `𝒩_W` | LRD-C3(c) `max(𝒩_{next}−𝒩_{prev}) = +1.000` |
| `--red-sharp` | feeds the sharp kink where the dressed kink is required | LRD-C5(a) residual `0.511`, LRD-C6(b) `E=0.104` |

Two of these are load-bearing red certificates rather than regression guards:
`--red-split` red-certifies the (FN)/(LRD.5) step that ⟨1⟩4.⟨2⟩4 and
⟨1⟩5.⟨2⟩3 both consume, and `--red-monotone` red-certifies that the
**non-negativity of the D14 counts** — not the window size — is what removes
`sup_m` in ⟨1⟩5.⟨2⟩4.  Two source-level mutations were additionally run on
copies in a scratch directory (the repo file untouched): replacing `q` by the
wrong root `Δ+\sqrt{Δ²−1}` → **exit 1** (LRD-C1(c), C5(a), C6(b)); moving the
cut to `c_0=5`, a legitimate different geometry → **exit 0**, confirming the
rows are not over-fitted to one cut.  No bare `assert` appears; every gate is
an explicit comparison, so `python3 -O` is equally strict.

---

## §H. HONEST STATUS

**Proved unconditionally for D16 (nothing further assumed beyond D16, D17 and
the standing setup).**
1. **D27(LR1)** — ⟨1⟩3.  Complete, and it needed less than expected: only
   separability of `𝔄`, strong continuity of `α_t`, and finiteness of
   `spec Q̂_{W,c_0}`.  It generalises verbatim (⟨1⟩6.⟨2⟩2, **LR1-GEN**), which
   means D27 carries as a hypothesis something that is a theorem.
2. The exact second-moment identity (LRD.11) and the equal-time and
   boundary-current forms of the LR2 defect, (LRD.7).
3. The **monotonicity lemma** ⟨1⟩5.⟨2⟩4: the escaped-content majorant is
   monotone in the window, so D27(LR3)'s `sup_m` collapses to the smallest
   window.  This is the structural answer to the "uniform over the
   exhaustion" trap and it costs nothing.
4. The **energy--domain-wall bound (EDW)** ⟨1⟩5.⟨2⟩6:
   `H_{XXZ} ⪰ \tfrac{J}{2}(Δ−1)D`, hence `⟨D(t)⟩ ≤ 2E_0/(J(Δ−1))` for all
   time.  Elementary, and apparently not recorded elsewhere in the campaign.
5. **Flatness of the K1--K2 kink family** ⟨1⟩5.⟨2⟩8, derived here from the two
   PROVED rows K1 and K2 and nothing else: the closed span of the exact
   zero-energy family lies in `ker H_kink`, so it is pointwise stationary and
   the D16 wall has no group velocity.  **This is not K4**: no uniqueness,
   isolation or completeness of a kink band is claimed or used.

**Proved conditionally, with the condition named.**
6. **(LR2′)** — ⟨1⟩4.⟨2⟩5 — with the explicit rate `η_m=4R_{W_m}\sqrt{G(m)}`,
   conditional only on the escape profile obeying `R_{W_m}²G(m)→0`.
7. **D27(LR3)** — ⟨1⟩5.⟨2⟩7 — conditional on the single input **(NR)**,
   `S_{NR}<∞`, with the explicit tail bound `2S_{NR}/M`.

**Left OPEN, and stated as such.**
8. **D27(LR2) verbatim** is **not** proved.  ⟨1⟩4.⟨2⟩6 isolates the residue
   (DPH) and marks it CONJECTURE.  The bound of ⟨1⟩4.⟨2⟩3 is uniform in the
   times but does not vanish at fixed `W`, because the D16 dressed kink has
   exponentially small but nonzero charge weight across each window edge.  We
   record explicitly that we did **not** patch this by asserting operator
   asymptotic commutativity, which D27 forbids and which would be a strictly
   stronger claim.  The mitigation is ⟨1⟩4.⟨2⟩7: (LR2′) suffices for every
   downstream use of LR2 in `theory/memory-index.md`, because the error is
   introduced before the spatial limit and removed by it.
9. **(NR)** itself.  (EDW) bounds the **number** of phase boundaries uniformly
   in time; it does not bound their **length**, because a one-dimensional
   wrong-phase block of any length carries the same `O(1)` Ising cost.  That
   is the whole gap.
10. **D27(LR3)'s optional convenience clause** (weak convergence of
    `{p_{W_m}}`): not proved, not needed, not claimed.
11. The **class statement**.  ⟨1⟩6 delivers one class theorem (LR1-GEN) and
    one class proposition (LR2′-GEN); the LR3 class statement stayed a
    **CONJECTURE** (⟨1⟩6.⟨2⟩4) whose clause 4 is (NR) itself, i.e. it is
    honest but currently weak.  "Gap + Lieb--Robinson ⟹ (LR)" as originally
    floated is **refuted as a class statement** by ⟨1⟩6.⟨2⟩5: a gapped,
    finite-range model with a mobile charged core satisfies both and fails
    LR3.  A spectral gap is used at no step of this shard.

**Numerical evidence only (not proof).**  The §C table.  `N=12` certifies
identities and operator inequalities exactly, and certifies flatness across all
13 `S^z` sectors to `3e−16`; it certifies nothing asymptotic.  The
independently re-run `memory_index_probe.py` (exit 0) supplies the asymptotic
side.  The bare-kink coincidence `E_0/c = 1.5275 = \sqrt{(Δ+1)/(Δ−1)}` at
`N=12` is a pleasant but unclaimed cross-check of (EDW)'s constant.

**Bearing on the live cross-lane obstruction (asked for explicitly; no position
taken on that lane's shard).**  ⟨1⟩5.⟨2⟩4 proves, unconditionally, that the
outcome bound `Σ_νν²p_{W_m}` is majorised by a quantity attached to the
**smallest** window and independent of `m`.  Consequently an escaped increment
growing like `|ν|≍2s|W_m|` cannot be an artefact of window geometry or of the
`c_0` offset (which cancels identically at fixed `W`,
`theory/memory-index.md` ⟨1⟩5.⟨2⟩3); if it occurs, it must occur already in
the fixed smallest-window quantity `sup_t⟨α_t(𝒩_{W_1})²⟩`, i.e. as genuine
unbounded transport of the charged core.  That is consistent with, and
logically independent of, the claim that a ballistic transit channel breaks
LR3 tightness; this shard neither assumes nor refutes it.  What this shard
does add is the D16-side half of the dichotomy: ⟨1⟩5.⟨2⟩8 proves that D16's
exact zero-energy kink family is degenerate, so the D16 core has no group
velocity and D16 sits outside the ballistic class — and ⟨1⟩6.⟨2⟩5 records
that any class statement omitting that clause is refutable.

**Register discipline inherited and respected.**  `δx` is never claimed
quantized; it is a `{p_ν}`-average (`M-INDEX-spec`'s adjudicated scoping).  No
sector-wide charge operator is constructed (`M-INDEX-LA-strong` is REFUTED).
K4 is never cited as proved.  The `n≥2` display of ML4-Ward (9) is not used
anywhere.  Bethe appears nowhere.  No reference is quoted, from `refs/` or
otherwise; every leaf cites a D-number, a claim id, or a named computation
defined in this file.

---

## §MP. MERGE PROPOSALS (for the orchestrator; nothing outside this lane is edited)

**MP-1 — `definitions.md`, D27.**  After the sentence ending
"`converge.  The sum is over q∈spec Q̂_{W,c_0} and absent spectral values
contribute zero.`", append:

> *(LR1 is a theorem, not a hypothesis, whenever `𝔄` is separable, `α_t` is
> strongly continuous, and `spec Q̂_{W,c_0}` is finite at each fixed `W` — in
> particular for every finite-local-dimension spin chain in this campaign's
> setting.  Proof: `theory/lr-d16.md` ⟨1⟩3, Lemma LR1-GEN.  It is retained in
> the (LR) list only so that D27 reads as a self-contained package.)*

**MP-2 — `theory/memory-index.md`, ⟨1⟩7.⟨2⟩1.**  After the existing
justification paragraph, append:

> *(LR2 may be weakened.  If instead of D27(LR2) one has only
> **(LR2′)**: `|double-Cesàro average of Δ_{W_m}| ≤ η_m` with `η_m→0` along the
> exhaustion, then this step holds at `W_m` up to `η_m`, ⟨2⟩2 carries the same
> `η_m`, ⟨2⟩3 is untouched (it uses LR1 and LR3 only), and ⟨2⟩4's spatial
> limit removes the error.  (IDX.2) and the support statement are therefore
> unchanged.  See `theory/lr-d16.md` ⟨1⟩4.⟨2⟩5, ⟨2⟩7.)*

**MP-3 — `claims/CLAIMS.md`, three proposed new rows** (statuses as
adjudicated by the critic, not by this shard):

| id | statement | proposed status | depends-on | where-proved | where-tested |
|---|---|---|---|---|---|
| LR1-GEN | For any quantum spin system with separable quasi-local `𝔄`, strongly continuous `α_t`, and a window observable with finite spectrum at each fixed `W`, D27(LR1) holds: one sequence `T_n→∞` gives convergence of both Cesàro states and all double-Cesàro TPM laws, each a probability on `spec Q̂_W−spec Q̂_W ⊂ ℤ`.  Compactness plus a diagonal argument; no gap, no Lieb--Robinson velocity, no scattering, no property of `Ψ` beyond normalisation. | PROVED | D26, D27 | theory/lr-d16.md ⟨1⟩3, ⟨1⟩6.⟨2⟩2 | theory/checks/lr_d16_check.py LRD-C1 (green exit 0; `--red` exit 1) |
| LR-D16-EDW | In D16, `h^{XXZ}_{x,x+1} ⪰ \tfrac{J}{2}(Δ−1)P^{DW}_x`, hence `H_{XXZ} ⪰ \tfrac{J}{2}(Δ−1)D` and `⟨Ψ,α_t(D)Ψ⟩ ≤ 2E_0/(J(Δ−1))` for all `t`, with `E_0=⟨Ψ,H_{XXZ}Ψ⟩` conserved and finite on a D17 packet.  Bounds the NUMBER of phase boundaries uniformly in time; bounds no length. | PROVED | D16 | theory/lr-d16.md ⟨1⟩5.⟨2⟩6 | theory/checks/lr_d16_check.py LRD-C4 (green 0; `--red-edw` 1) |
| LR-D16 | For D16 and a D17 dressed-kink packet obeying (FN): D27(LR1) holds unconditionally; (LR2′) holds with rate `η_m=4R_{W_m}\sqrt{G(m)}` and suffices for every downstream use of D27(LR2) in memory-index; D27(LR3) holds **conditionally on (NR)**, `sup_t` of the escaped-content second moment at the SMALLEST window being finite, the `sup_m` having been removed unconditionally by the monotonicity lemma.  D27(LR2) verbatim is OPEN, reduced to the named residue (DPH).  The D16 feature that removes the ballistic failure mode is the exact degeneracy of the K1--K2 zero-energy kink family (K4 is NOT used). | SKETCH (r1 proposer; conditional on (NR); LR2 open) | D13(a), D14, D16, D17, D26, D27, K1, K2, K3, M-INDEX-spec | theory/lr-d16.md ⟨1⟩3--⟨1⟩5 | theory/checks/lr_d16_check.py LRD-C1--C6 (18/18 green, exit 0; four `--red` modes exit 1) |

**MP-4 — `theory/TRIANGLE.md` / `HANDOFF.md` one-liner.**  "`M-INDEX-spec`
still has no fully unconditional dynamical instance: for D16, LR1 is now
unconditional and LR3 is reduced to the single named input (NR), but LR2
verbatim remains open (residue (DPH)).  The honest headline is *one clause
proved outright, one clause proved in a weakened form that suffices
downstream, one clause reduced to a single named dynamical hypothesis*."
