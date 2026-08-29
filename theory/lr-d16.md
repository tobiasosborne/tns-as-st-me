<!-- ROLE: proposer shard for bd tns-xf4 — prove D27(LR1--LR3) for the D16
     easy-axis XXZ kink sector.  R3 lane: this file,
     theory/lr-d16-r3-response.md, theory/checks/lr_d16_check.py.  Nothing else
     in the repo is edited; shared-file text is in MERGE PROPOSALS. -->

# (LR) for D16 — charge-history local relaxation in the easy-axis XXZ kink sector

**Round r3 repaired proposer draft, 2026-08-29.  Self-status: SKETCH until the
L6 loop converges.  Read the HONEST STATUS section (§H) before citing anything
here.  `LR1-GEN` and `LR-D16-EDW` are already PROVED in `claims/CLAIMS.md` on
the r2 critic's wording; this shard is kept in lockstep with those rows.**

Target: D27 (`definitions.md`), clauses (LR1), (LR2), (LR3), for the D16 model
and a D17 kink packet.  Motivation: `M-INDEX-spec` (`claims/CLAIMS.md`) is
PROVED but conditional, with D27 assumed on every model and therefore with no
unconditional dynamical instance.  This shard supplies one instance as far as it
honestly goes and names, precisely, what is left open.

Summary of the verdict reached below (details in §H):

| clause | D16 verdict |
|---|---|
| LR1 | **PROVED unconditionally** (⟨1⟩3), and at class level (⟨1⟩6); `LR1-GEN` is PROVED in the DAG |
| LR2 | verbatim **OPEN**; the r1 D16 claim **(LR2′) is WITHDRAWN** because its antecedent (ESC) is unavailable, while the resulting estimate is weaker than the free bound at five of six sampled times under both finite-volume propagators |
| LR3 | **PROVED from the repaired, two-clause (NR)** (⟨1⟩5), whose second clause retains `sup_m`; the monotonicity lemma fixes the majorising observable, not the pinched state; the EDW operator inequality is unconditional |
| class statement | `LR1-GEN` is **PROVED**; beyond it this shard supplies only an input inventory, while the unpromoted `ACE-LD-obst′` identifies an unwitnessed transport hypothesis a future theorem would have to contend with |

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
diagonal multiplication operators `𝒬`, `𝒩_W`, and `N_{DW}`.  Their quadratic-form
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
  TPM laws `p_{W,n}(ν)` converge for every `ν∈ℤ`.  Proved in ⟨1⟩3 from (H1)
  only for the existence of `α_t`, together with `‖Ψ‖=1`; (H2)--(H6) are not
  used.

- **(LRD-2-BND) = a scalar bound, not a D16 relaxation result.**
  Write `Δ_W(t_-,t_+):=⟨Ψ,[𝒟_{W,t_-}(Q̂_{W,c_0}(t_+))−Q̂_{W,c_0}(t_+)]Ψ⟩` for
  D27's first-moment nondemolition defect.  Then
  `limsup_n |double-Cesàro average of Δ_{W_m}| ≤ η_m` with an **explicit**
  `η_m = 4R_{W_m}\sqrt{G(m)}`.  This estimate is proved in ⟨1⟩4, but its
  sufficient condition `R_{W_m}²G(m)→0` is **not established for any D16
  state obeying (H3)**: proving or refuting the needed uniform escape profile
  requires local decay in the one-kink/one-magnon sector, i.e.
  D18(AD1)--(AD3), which item (ii) below declines to assume.  Moreover, the
  resulting finite-volume estimate is weaker than the free bound at five of
  six sampled times under either propagator.  Thus the r1 D16 result called
  **(LR2′) is WITHDRAWN**, not patched.  **D27(LR2) verbatim is OPEN**;
  ⟨1⟩4.⟨2⟩6 isolates the residue and names it (DPH).

- **(LRD-3) = D27(LR3), conditional on the repaired, two-clause (NR) of
  ⟨1⟩5.⟨2⟩7.**  `lim_{M→∞} sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν)=0`.  The
  monotonicity lemma ⟨1⟩5.⟨2⟩4 replaces the family of majorising observables
  `{𝒩_{W_m}}` by the single `𝒩_{W_1}`; it does **not** remove the
  `m`-dependence of the `W_m`-pinched state.  Accordingly (NR)'s second clause
  retains `sup_m`.  The domain-wall operator inequality is unconditional;
  its uniform-in-time expectation bound applies when `E_0` is finite and
  conserved, exactly as in the PROVED `LR-D16-EDW` row.

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
conserved charge.  Separately, `theory/ace-ld.md`'s `ACE-LD-obst′` is an
unpromoted merge proposal in a shard at `FAIL(F1,M1--M6)`; it would obstruct
LR3 on states satisfying (M-ESC), but no such state or model is exhibited in
the corpus.  It therefore identifies a transport hypothesis a class theorem
would have to contend with, not a clause the theorem is known to need.  In
the present (FN) register a large increment requires unbounded wrong-phase
**block growth**, not rigid core transit.  K1--K2 supply only that every state
in their closed product-family span is stationary; exhaustiveness is K4 and
is not used.

*Justification of the display of hypotheses.* D27 verbatim, D16, D17, D26,
`claims/CLAIMS.md` rows K1--K4, `M-INDEX-spec`, `M-INDEX-LA-strong`.

**⟨2⟩1. QED** (statement fixed).

---

## ⟨1⟩3. LEMMA LRD-1 (= D27(LR1)) — PROVED UNCONDITIONALLY

**ASSUME.** (H1) only for the existence of the strongly continuous dynamics
`α_t`, and `‖Ψ‖=1`.  (Not used: (H2)--(H6), or any scattering, gap,
completeness or channel input.)

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

is valid, but **(ESC) is unavailable for the D16 state class (H3)**.  The
free dispersion has `|v(k)|=J|sin k|` bounded away from zero on the chosen
compact momentum support, but turning that kinematic observation into escape
of the interacting one-kink/one-magnon state from every fixed window requires
a local-decay/completeness statement, i.e. D18(AD1)--(AD3), which this shard
does not assume.  Thus neither `G(m)≥1-o(1)` nor (ESC) is established here.
The r1 D16 result named **(LR2′) is nevertheless retracted** because it was
conditional on this undischarged antecedent.  Its finite-volume bound is also
uninformative where sampled: under the required `H_{XXZ}` propagator at
`N=12`, `W=[4,9]`, the six values of `4R_Wε_W(t_-)` at
`t_-=0,-2,-5,-9,-20,-40` are `10.0,11.9,9.7,5.0,6.8,6.5`, so five exceed
the free bound `2‖Q̂_W‖=6` (the old `H_kink` diagnostic gives the same
five-of-six count).  No claim about the truth of (ESC), and no retuning of the
propagator or constant, is needed for the withdrawal.

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
at **fixed** `W`.  ⟨2⟩5 gives only `≤4R_W\sqrt{G(W)}` and does not establish
that this upper bound vanishes.  The finite-volume `H_{XXZ}` diagnostic shows
that the escaped-content contribution is `O(1)` on the two inner sampled
windows, rather than merely the exponentially small K1--K2 kink tail
`O(q^{2d_W})`; it does **not** establish the infinite-time escape mechanism.
The missing statement is
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
for D16 it is not removed because no vanishing `η_m` has been established.

**⟨2⟩8. QED** (the scalar bound is proved; the D16 LR2′ claim is withdrawn
because its antecedent is unavailable; LR2 verbatim is reduced to (DPH) and
left OPEN). □

---

## ⟨1⟩5. LR3 — first-moment tightness

**ASSUME.** (H1)--(H6) of ⟨1⟩2, and D27(LR1) as established in ⟨1⟩3.

**PROVE.** `lim_{M→∞} sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν)=0`, given the repaired,
two-clause input (NR) of ⟨2⟩7.  Steps ⟨2⟩1--⟨2⟩5 are unconditional in the
standing register; ⟨2⟩6's operator inequality is unconditional, while its
expectation bound assumes finite conserved `E_0`.

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

**⟨2⟩6 (energy--domain-wall bound (EDW), in the exact `LR-D16-EDW`
register).**  In the basis
`(|↑↓⟩,|↓↑⟩)` the D16 bond term `h^{XXZ}_{x,x+1}` is
`(JΔ/2)I − (J/2)σ^x`, with eigenvalues `(J/2)(Δ∓1)`, and it annihilates
`|↑↑⟩,|↓↓⟩`.  Hence, with `P^{DW}_x` the projection onto
`span{|↑↓⟩,|↓↑⟩}_{x,x+1}` and
`N_{DW}:=Σ_xP^{DW}_x` the domain-wall number,

  `h^{XXZ}_{x,x+1} ⪰ \tfrac{J}{2}(Δ−1)\,P^{DW}_x`,
  `H_{XXZ} ⪰ \tfrac{J}{2}(Δ−1)\,N_{DW} ⪰ 0`.                     **(LRD.14)**

The sum is a quadratic-form inequality on the finite-deviation core of
`ℋ_ref`; the same bondwise inequality and sum are exact on every finite open
chain.

Consequently, **for any state `Ψ` whose energy
`E_0:=⟨Ψ,H_{XXZ}Ψ⟩` is finite and conserved by the D16 dynamics**,

  `⟨Ψ, α_t(N_{DW})Ψ⟩ ≤ \frac{2E_0}{J(Δ−1)}` **for every `t`**.     **(LRD.15)**

For the bare K1--K2 kink, ⟨1⟩1.⟨2⟩2 gives `E_0=C_K=\tfrac{J}{2}\sqrt{Δ²−1}`
and hence `⟨N_{DW}⟩ ≤ \sqrt{(Δ+1)/(Δ−1)}`, which `→1` as `Δ→∞` (one wall) and
diverges as `Δ→1⁺` (the kink delocalises) — both as they must.  For the kink
plus magnon state used by the checker, finiteness and conservation are
verified directly under the finite-chain `H_{XXZ}` propagator; this shard does
not derive those two state properties from D17.

*Justification.* D16's displayed `h^{XXZ}`, the explicit `2×2` block (the same
block as claim **K1**'s ⟨1⟩1, before the telescoping field is added),
`Δ>1`, the stated finiteness-and-conservation hypotheses on `E_0`, and
⟨1⟩1.⟨2⟩2 for the value of `C_K`.  Named computation **LRD-EDW**; certified
numerically as row `LRD-C4` of `theory/checks/lr_d16_check.py`.  This is the
PROVED `LR-D16-EDW` row of `claims/CLAIMS.md`; it bounds the **number** of
phase boundaries and nothing about their length.

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

**⟨2⟩9 (THEOREM LRD-MESC-NR — cross-lane incompatibility).**

**ASSUME.**  The following hypotheses hold for the **same** vector `Ψ`, cut
`c_0`, padded exhaustion `W_m = [a_m,b_m] ↑ ℤ`, D27 clause-1 sequence
`T_n → ∞`, fixed-window laws `p_{W_m}`, and D27 limit order.

1. The D16 standing register (H1)--(H6) of ⟨1⟩2, including D26(INT), the D17
   packet, (FN), and D27(LR1).
2. H-MQG(1)--(3) and D27(LR2), i.e. the remaining hypotheses of the exact
   `ACE-LD-obst-prime` row not already explicit in (H1)--(H6).
3. **(M-ESC)** on this exhaustion:
   `θ_{tr} := liminf_m
   |ω^+_{W_m}(𝔛_{W_m})-ω^-_{W_m}(𝔛_{W_m})|/|W_m| > 0`.

For this same exhaustion, `(NR)` means exactly the conjunction introduced at
⟨2⟩7:

1. `sup_{t∈ℝ}⟨Ψ,α_t(𝒩_{W_1})²Ψ⟩ < ∞`;
2. `sup_m sup_{t_-<t_+}Σ_q
   ‖α_{t_+}(𝒩_{W_1})E_{W_m,t_-}({q})Ψ‖² < ∞`.

**PROVE.**  `(NR)` fails.  Equivalently, on every padded exhaustion in the
joint register above on which (M-ESC) holds, at least one of these two bounds
is infinite.

**⟨3⟩1. (The transport obstruction gives `¬D27(LR3)` on this exhaustion.)**
The exact claim row `ACE-LD-obst-prime` applies to the objects fixed in the
ASSUME block and yields

`sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν) = ∞` for every `M`;

hence D27(LR3) fails for this exhaustion.

*Justification.*  Claim **ACE-LD-obst-prime** (`claims/CLAIMS.md`, status
**PROVED** conditional): its hypotheses are H-MQG(1)--(3), D26(INT), the D27
setting, D27(LR1)--(LR2), and (M-ESC), all listed above; its conclusion (b)
is exactly `¬D27(LR3)`.  The row depends on D13, D17, D26, D27, and the exact
claim row **M-INDEX-fin**.  No conclusion of `M-INDEX-spec` is consumed.

**⟨3⟩2. (Assume `(NR)` for contradiction.)**

**ASSUME.**  Both clauses of `(NR)` displayed above hold.

**PROVE.**  A contradiction.

*Justification.*  This is proof by contradiction applied to the conjunction
defined at ⟨2⟩7; the exact DAG transcription of that conditional is claim
**LR-D16-NR** (added with this theorem; proved at ⟨1⟩5.⟨2⟩1--⟨2⟩7).

**⟨3⟩3. (`(NR)` gives D27(LR3) on the same exhaustion.)**  By
THEOREM (LRD-3), the two bounds in ⟨3⟩2 give

`sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν) ≤ 2S_{NR}/M → 0`.

Thus D27(LR3) holds for the same family `{p_{W_m}}`.

*Justification.*  Exact claim **LR-D16-NR**: under (H1)--(H6), D27(LR1),
and the repaired two-clause `(NR)`, D27(LR3) holds with tail bound
`2S_{NR}/M`; its proof is ⟨1⟩5.⟨2⟩1--⟨2⟩7 and was independently re-derived
in `theory/verdicts/lr-d16-r2.md` §4 item 3.  D27(LR3) is the definition at
`definitions.md` D27(3).  The optional weak-convergence convenience clause is
not used.

**⟨3⟩4. (Contradiction.)**  Steps ⟨3⟩1 and ⟨3⟩3 respectively assert the
negation and the truth of D27(LR3) for one and the same family
`{p_{W_m}}`; they cannot both hold.

*Justification.*  D27(3) fixes one predicate on the common exhaustion and
common fixed-window laws; ⟨3⟩1 cites exact claim **ACE-LD-obst-prime**, and
⟨3⟩3 cites exact claim **LR-D16-NR**.  Classical non-contradiction.

**⟨3⟩5. (Discharge and universal scope.)**  Therefore the assumption in
⟨3⟩2 is false, so `¬(NR)`.  Because the padded exhaustion in the theorem's
ASSUME block was arbitrary, the implication holds for every padded exhaustion
on which the joint register and (M-ESC) hold:

`(M-ESC)  ⟹  ¬(NR)`.  **QED.** □

*Justification.*  ⟨3⟩2--⟨3⟩4, implication introduction, and universal
generalisation over the arbitrary padded exhaustion of D27.

**Ownership and nonvacuity fence.**  This theorem belongs in `lr-d16.md`:
`(NR)` is defined once at ⟨2⟩7 and is a D16-specific sufficient input for
LR3.  `ACE-LD-obst-prime` remains the general obstruction; `ace-ld.md` must
cite **LRD-MESC-NR**, not restate this proof.  No model or state satisfying
(M-ESC) is exhibited in the corpus (the disclosure already carried by the
exact `ACE-LD-obst-prime` row), so this is a conditional incompatibility, not
a D16 counterexample and not evidence that either particular clause of `(NR)`
fails on the selected D16 packet.

**⟨2⟩10. QED** (LR3 proved from (NR); the cross-lane incompatibility proved
by composition; ⟨2⟩1--⟨2⟩5 and ⟨2⟩8 unconditional in the standing register;
⟨2⟩6 in the exact `LR-D16-EDW` register). □

---

## ⟨1⟩6. CLASS-LEVEL CONTENT — one theorem and one bounded inventory

**⟨2⟩1 (inventory: what the D16 proof actually consumed).**  Reading
⟨1⟩3--⟨1⟩5 backwards, the inputs are exactly:

| ingredient | used by | model-specific? |
|---|---|---|
| separable unital quasi-local `𝔄`, strongly continuous `α_t` | ⟨1⟩3 | no |
| `Q̂_{W,c_0}∈𝔄_W` self-adjoint, finite spectrum | ⟨1⟩3, ⟨1⟩4 | no (finite local dim) |
| `spec Q̂_{W,c_0}⊂ℤ` (D26(INT)) | ⟨1⟩4.⟨2⟩4 | no (INT) |
| (FN): selected vector an eigenvector of a conserved regularised charge | ⟨1⟩4.⟨2⟩4, ⟨1⟩5.⟨2⟩3 | no, but a hypothesis on the vector |
| scalar escape bound `4R_{W_m}\sqrt{G(m)}`; (ESC) is unavailable on (H3) | ⟨1⟩4.⟨2⟩5 | **yes** |
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
`*`-automorphisms of `𝔄`, `Ψ` a unit vector in any representation of `𝔄`,
`c_0` a cut, and `Q̂_{W,c_0}∈𝔄_W` self-adjoint with finite spectrum at each
finite window `W∋c_0`.  Then **every** prescribed sequence `S_n→∞` admits a
subsequence `T_n=S_{n_j}` along which, **simultaneously for every such `W`**,
the two Cesàro states converge weak-`*` on all of `𝔄` to states and every
double-Cesàro TPM weight converges.  Each limit `p_W` is a probability
supported in the finite set `spec Q̂_W−spec Q̂_W`, which under D26(INT) lies
in `ℤ`.  Clause 1 is therefore a theorem but is not removable: it binds the
single sequence used by D27's clauses 2--3.  Not claimed are pointwise-in-time
convergence, full-sequence convergence, or anything about D27(LR2) or (LR3).

*Proof.* The proof of ⟨1⟩3 with its index sequence `T=1,2,3,…` replaced by the
prescribed `S_n`; nested extraction makes the diagonal a genuine subsequence.
⟨1⟩3.⟨2⟩7 records that only separability, strong continuity, finite window
spectrum, and `‖Ψ‖=1` are used. □

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
has no established D16 instance under (H3), where ⟨1⟩4.⟨2⟩5 records that
(ESC) is unavailable without a local-decay input.

*Proof.* Verbatim ⟨1⟩4.⟨2⟩1--⟨2⟩5, ⟨2⟩7; no D16-specific fact enters. □

**⟨2⟩4 (SCOPING REQUIREMENT LR3-SCOPE — what actually survives).**  Neither a
spectral gap nor a Lieb--Robinson velocity estimate is used anywhere in
⟨1⟩3--⟨1⟩5, so this shard supplies no proof that those two inputs imply (LR),
and no refutation either.  Separately, `theory/ace-ld.md`'s `ACE-LD-obst′` —
a merge proposal, not yet a `claims/CLAIMS.md` row, in a shard at
`FAIL(F1,M1--M6)` — would show that D27(LR3) fails on states satisfying
(M-ESC).  No such state or model is exhibited anywhere in this corpus, so
this identifies a hypothesis a class theorem would have to *contend with*,
not a clause it is known to need.

*Justification.* Inventory ⟨2⟩1, the status of `ACE-LD-obst′` in
`theory/ace-ld.md` and `theory/verdicts/ace-ld-r2.md`, and the explicit absence
of an (M-ESC) witness recorded by that shard.

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

**⟨2⟩6 (unresolved inputs a full class theorem would have to address).**
Three items:
(a) (DPH) of ⟨1⟩4.⟨2⟩6 for verbatim LR2; (b) the (FN) register, which cannot
be upgraded to the REFUTED sector-wide `M-INDEX-LA-strong`; and (c) control of
wrong-phase block **length**, such as the repaired two-clause (NR).  The
unwitnessed (M-ESC) hypothesis is a possible obstruction to that third item,
not proof that a no-mean-transport clause is necessary.  (EDW) controls block
number only.  K1--K2 show stationarity only on their closed family span;
using that span to assert model-wide no recoil or to exhaust the low-energy
kink states would require K4 (CONJECTURE) and is forbidden.

**⟨2⟩7. QED** (`LR1-GEN` proved; `LR2-BOUND-GEN` conditional with no
established D16 (H3) instance; the unsupported counterexample retracted;
LR3-SCOPE reduced to the inventory and the unpromoted, unwitnessed
`ACE-LD-obst′` conditional). □

---

## §C. CHECKER REGISTRY — `theory/checks/lr_d16_check.py`

D16 at `J=1`, `Δ=2.5`, `N=12`, cut `c_0=6`, windows `W_1=[4,9] ⊂ W_2=[3,10] ⊂
W_3=[2,11]`, exact diagonalization in the conserved `S^z` sectors, exact
spectral time evolution, dressed-kink initial state (⟨1⟩1.⟨2⟩7).

The r3 checker was simplified gate-by-gate before registration.  C1(b) gates
only the **raw** `q_w` array; the integer-increment and support observations
derived from the same spectral blocks are labelled DISPLAY rather than used
as tautological conjuncts.  C3(a) constructs `α_{t_±}(Q̂_W)` as independent
matrices on an `N=8` sector and compares the pinched square with the separately
generated TPM law.  C3(d) is labelled DISPLAY because it is deductively
subsumed by C3(b)+C3(c).  C2(d) and C3(e) now evolve with `H_XXZ` and each
gates its energy conservation; registered mutants revert each row to
`H_kink`.  C3(e) gates relative variation only, with no ordering requirement.
C4(b) also evolves with `H_XXZ` and gates its energy conservation.  The
tautological r1 C4(c) ratio and the subsumed r1 C6(b) row remain deleted;
C4(c) checks the actual finite-chain equality `⟨K|H_XXZ|K⟩≈C_K`.

| row | evidence / green value | registered mutant (exact exit path) |
|---|---|---|
| C1(a) | propagator-independent TPM normalisation, error `6.66e−16` | `c1-nonunitary` → C1(a) |
| C1(b) | raw `spec Q_W⊂ℤ`, defect `0`; increment/support arithmetic DISPLAY only | `c1-noninteger` (`q_w↦q_w+0.3`) → C1(b) |
| C2(a) | `Δ_W(t,t)=0`, error `1.89e−15` | `c2-unequal-time` → C2(a) |
| C2(b) | `|Δ_W|≤4R_Wε_W`, slack `−4.736` | `c2-small-constant` → C2(b) |
| C2(c) | `ε_W²≤⟨Q̂_{W^c}²⟩`, slack `−1.350e−4` | `c2-mismatched-complement` → C2(c) |
| C2(d) | `H_XXZ` finite-volume display: `G=0.989,0.949,0.278`, `η=11.9,15.6,10.5`; only the two inner windows are gated; `4R_Wε_W>6` at five of six samples; energy drift `2.18e−14` | `c2-delete-outside-data`, `c2-kink-propagator` → C2(d) |
| C3(a) | independent matrix (LRD.11): `0.5159528928` both routes, error `0` | `c3-perturb-final-evolution` → C3(a) |
| C3(b) | edge split (LRD.12), slack `−1.824e−1` | `c3-mismatched-complement` → C3(b) |
| C3(c) | `𝒩_{W'}⪯𝒩_W`, `|Q̂_{W^c}|⪯𝒩_W`, exact | `c3-signed-majorant` → C3(c) |
| C3(d) | **DISPLAY, not an evidence row:** fixed-observable slack `−2.882e−1`; its majorant exceeds C3(b)'s by at least `5.490e−4`, so C3(b)+C3(c) imply it | none (deductively subsumed) |
| C3(e) | `H_XXZ` finite sample `1.607/1.670/1.747`, spread/mean `0.084`, with no direction claim; energy drift `9.77e−15` | `c3-freeze-pinching`, `c3-kink-propagator` → C3(e) |
| C4(a) | bond EDW, minimum eigenvalue `−0.0` | `c4-wrong-gap` → C4(a) |
| C4(b) | `H_XXZ` energy drift `1.11e−14`; `max⟨N_{DW}⟩=3.053≤4.753` | `c4-kink-propagator` → C4(b) |
| C4(c) | `⟨K|H_XXZ|K⟩=1.1456439081`, `C_K=1.1456439237` | `c4-sharp-calibration` → C4(c) |
| C5(a) | K1--K2 local kernel, residual `8.01e−19` | `c5-wrong-root` → C5(a) |
| C5(b) | distinct kink-bond positivity gate, minimum eigenvalue `−0.0` | `c5-overstrong-field` → C5(b) |
| C6(a) | sharp/dressed overlap `0.9545`, sharp energy `0.1044` | `c6-identify-sharp-dressed` → C6(a) |

**Exit paths and reachability.**
`python3 -O theory/checks/lr_d16_check.py` → **exit 0**, 16/16 evidence rows
green (plus two labelled displays).
`python3 -O theory/checks/lr_d16_check.py --red-all` → **exit 1, RED-OK
18/18 mutants**.  Each `--red MODE` evaluates the **full 16-row suite** without
short-circuiting and exits 1 only when the failed-row list is exactly the
registered singleton; a missed or collateral path exits 2.  Thus no evidence
row is unreachable and no collateral failure is masked.  Data mutations
include a non-unitary propagator, noninteger raw spectrum, mismatched
complement, deleted outside-count data, perturbed final Heisenberg evolution,
frozen `W_1` pinching, three independently registered wrong finite-volume
propagators, and sharp/dressed substitution.  No bare `assert` appears, so
`-O` is strict.

---

## §H. HONEST STATUS

**Proved unconditionally or algebraically in the stated register.**
1. **D27(LR1)** — ⟨1⟩3.  Complete, and it needed less than expected: only
   separability of `𝔄`, strong continuity of `α_t`, and finiteness of
   `spec Q̂_{W,c_0}` and `‖Ψ‖=1`.  The same proof with the index sequence
   replaced gives the PROVED **LR1-GEN** row: from any prescribed `T_n→∞`, a
   subsequence supplies clause 1.  Clause 1 remains the binder for the
   sequence quantified over by clauses 2--3.
2. The exact second-moment identity (LRD.11) and the equal-time and
   boundary-current forms of the LR2 defect, (LRD.7).
3. The **monotonicity lemma** ⟨1⟩5.⟨2⟩4: the escaped-content majorant is
   monotone in the window, so the family of majorising observables collapses
   to `𝒩_{W_1}`.  The `W_m`-pinched state remains `m`-dependent, so `sup_m`
   remains in (NR)'s second clause.
4. The **energy--domain-wall bound (EDW)** ⟨1⟩5.⟨2⟩6:
   `H_{XXZ} ⪰ \tfrac{J}{2}(Δ−1)N_{DW}` as a quadratic-form inequality.  The
   PROVED `LR-D16-EDW` row states the consequence
   `⟨N_{DW}(t)⟩≤2E_0/(J(Δ−1))` for states whose `E_0` is finite and conserved;
   those two state properties are hypotheses, not derived here from D17.
5. **Flatness of the K1--K2 kink family** ⟨1⟩5.⟨2⟩8, derived here from the two
   PROVED rows K1 and K2 and nothing else: the closed span of the exact
   zero-energy family lies in `ker H_kink`, so every state in that span is
   stationary.  **This is not K4**: it says nothing about states outside the
   span and no model-wide no-recoil claim is made.

**Proved conditionally, with the condition named.**
6. **LRD-2-BND** — ⟨1⟩4.⟨2⟩5 — the scalar estimate with
   `η_m=4R_{W_m}\sqrt{G(m)}`.  Its abstract (ESC) consequence is valid but
   unavailable for the D16 (H3) class without local decay; it is not listed
   as a D16 LR2′ result.
7. **D27(LR3)** — ⟨1⟩5.⟨2⟩7 — conditional on the repaired **two-clause
   (NR)**, including `sup_m` in the pinched clause, with tail `2S_{NR}/M`.

**Left OPEN, and stated as such.**
8. **D27(LR2) verbatim** is **not** proved.  ⟨1⟩4.⟨2⟩6 isolates the residue
   (DPH) and marks it CONJECTURE.  The bound of ⟨1⟩4.⟨2⟩3 is uniform in the
   times but supplies no vanishing estimate at fixed `W`.  The r1 D16
   **(LR2′) is WITHDRAWN** because (ESC) is unavailable; establishing the
   escape statement used in r2 would require D18(AD1)--(AD3).  At the sampled
   finite-volume points the bound is also weaker than the free bound at five
   of six times under both propagators.  We did **not** patch this by asserting
   operator asymptotic commutativity, which D27 forbids and which would be a
   strictly stronger claim.  `M-INDEX-spec` is unaffected and unimproved, and
   `M-INDEX-fin` is safe.
9. **The two clauses of (NR)** themselves.  Given finite conserved energy,
   (EDW) bounds the **number** of phase boundaries uniformly in time; it does
   not bound their **length**, because a one-dimensional wrong-phase block of
   any length carries the same `O(1)` Ising cost.  That is the whole gap.
10. **D27(LR3)'s optional convenience clause** (weak convergence of
    `{p_{W_m}}`): not proved, not needed, not claimed.
11. The **class theorem beyond LR1-GEN**.  The r1 alleged counterexample to
    "gap + Lieb--Robinson ⟹ (LR)" is retracted: no model was supplied and its
    core-transit mechanism contradicts (FN)/(LRD.5).  What survives is the
    inventory: this shard uses neither a gap nor an LR velocity.
    `ACE-LD-obst′` is an unpromoted claim in a failing shard and has no
    exhibited (M-ESC) witness; it identifies a hypothesis a future theorem
    must contend with, not a clause it is known to need.

**Numerical displays only (not asymptotic evidence).**  Under `H_{XXZ}` at
`N=12`, C2(d) gives `G=0.989,0.949,0.278` and
`η=11.9,15.6,10.5`.  Only the two inner-window values illustrate `O(1)`
escaped content on the sampled time interval; `W_3=[2,11]` leaves only two
sites outside and carries no escape information.  C3(e) gives the pinched
sample `1.607/1.670/1.747`, spread/mean `0.084`: finite-sample dependence,
with no general monotonicity direction and no numerical proof that `sup_m` is
needed.  Retaining `sup_m` is instead forced by the proof, which does not
derive a uniform bound without it.  C4(c) checks the finite-chain equality
`⟨K|H_XXZ|K⟩=1.1456439081` against `C_K=1.1456439237`.

**Bearing on the live cross-lane obstruction.**  ⟨1⟩5.⟨2⟩4 proves only that
the majorising **observable** can be fixed to `𝒩_{W_1}`.  The `W_m`-pinched
state remains `m`-dependent, so the corresponding term stays under `sup_m`.
An increment `|ν|≍2s|W_m|` cannot arise from the `c_0` offset (which cancels
at fixed `W`) and, under (FN), cannot arise from rigid sharp-core transit; it
requires wrong-phase block growth in the state or pinched state.  Separately,
the unpromoted `ACE-LD-obst′` conditional would obstruct LR3 if an (M-ESC)
state existed; none is exhibited in the corpus.  No model counterexample or
necessity claim is made here.

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
unavailable for D16.  `M-INDEX-spec` is unaffected and unimproved;
`M-INDEX-fin` is safe.  Lane-local cleanup proposed separately: `memory-index.md`
⟨1⟩5.⟨2⟩1 should cite D27's clause-1 TPM display rather than D27(LR2), because
it uses no dephasing limit.

**MP-3 — APPLIED by the orchestrator; no longer a proposal.**  `LR1-GEN` and
`LR-D16-EDW` are PROVED in `claims/CLAIMS.md` on the r2 critic's exact cells.
The authoritative wording is those DAG rows, not the shorter r2 table that
formerly appeared here.  Lockstep points now reflected in this shard are:
`LR1-GEN` quantifies over every prescribed sequence and claims no pointwise or
full-sequence convergence; `LR-D16-EDW` uses `P^{DW}_x` and `N_{DW}`, and
carries finiteness and conservation of `E_0` as hypotheses on the selected
state.  C1(b)'s spectral support is proved analytically in ⟨1⟩3.⟨2⟩4--⟨2⟩6;
its checker gates raw integrality only and labels the by-construction support
arithmetic as DISPLAY.

`LR-D16` remains **HOLD**: LR1 is unconditional; D16 LR2′ is withdrawn and
LR2 remains open; LR3 holds only under repaired two-clause (NR).

**MP-4 — `theory/TRIANGLE.md` / `HANDOFF.md` one-liner.**  "`M-INDEX-spec`
still has no fully unconditional dynamical instance: for D16, LR1 is now
unconditional — indeed a class theorem, `LR1-GEN` — and LR3 is reduced to the
single named input (NR), but LR2 verbatim remains open (residue (DPH)).  The
honest headline is *one clause proved outright, one clause still open with its
residue named, and one clause reduced to a named two-clause dynamical
hypothesis*.  The clause that became unconditional is the one that carried no
content: D27's clause 1 only binds the sequence its clauses 2--3 quantify
over."
