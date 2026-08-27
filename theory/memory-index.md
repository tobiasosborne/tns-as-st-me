<!-- ROLE: Lane-T1 proposer shard for M-INDEX.  Only the corrected
     finite-window/TPM theorem is claimed.  The requested strong L-A is
     refuted below by an explicit D17 counterexample.  Status: SKETCH until L6. -->

# M-INDEX — charge-history quantisation without channel completeness

## 0. Statement

The labels **D26** and **D27** below refer to the exact proposals in §6; they
are not additions to the shared definition file in this lane.

### THEOREM M-INDEX-spec (sharpened statement)

**ASSUME (H-IDX).**

1. H-MQG(1)--(4) of `memory-quantization-general.md`, verbatim.  In
   particular there is no H-AD-G/D18 assumption and no channel inventory.
2. **(INT)** is proposed D26: for the selected Hermitian charge,
   `exp(2πiS^z_x)=c I`, `|c|=1`.
3. Only for (G-IDX.2), **(LR)** is proposed D27: common-sequence Cesàro
   relaxation of the two one-time window states and the two-projective-
   measurement (TPM) history law, vanishing first-moment measurement
   back-action, and first-moment-tight/boundary-stable spatial exhaustion.

**PROVE.**  For `W=[a,b]` and a fixed `c_0∈W`, use the already-defined D13(a)
coordinate and the identity

`Q̂_{W,c_0}:=2s(𝔛_W-c_0)`                                      **(IDX.1)**

(the new name is proposed for `notation.md`; the equality is (G.3) of
M-quant-G, not a new definition of `𝔛_W`).  Then:

- **(G-IDX.0-fin)** unconditionally, every `Q̂_{W,c_0}` has spectrum in one
  coset of `ℤ`, and every fixed-window TPM escaped-charge increment is in
  `ℤ`.
- **(G-IDX.0-strong)** as requested in the campaign target is **false**:
  D9+D17+(INT) do not imply that `Q̂_{W,c_0}` has a self-adjoint
  infinite-window limit.  Consequently there is no unconditional sector-wide
  operator `Q̂` to which the requested pure-point conclusion can be applied.
  If such an operator is supplied and `exp(2πiQ̂)` is scalar, its spectrum is
  indeed pure point in one coset; this arithmetic implication is proved in
  ⟨1⟩2.
- **(G-IDX.1)** at finite time, `2s` times the wall-coordinate change is minus
  the charge escaped through the two boundaries; the ordered asymptotic
  ledger is its D27 limit.
- **(G-IDX.2)** under (LR), the TPM escaped-charge laws converge to a
  probability `p={p_ν}_{ν∈ℤ}` and

  `δx=-(1/(2s)) Σ_{ν∈ℤ}νp_ν`.                                 **(IDX.2)**

  Thus individual outcomes of this explicit history protocol, not their
  average, are multiples of `1/(2s)`.  Bound states, absorption, and extra
  channels are allowed because none is named.
- **(G-IDX.3)** under (LR) and additionally H-AD-G, `p_0=1-⟨N_T⟩`,
  `p_2=⟨N_T⟩`, all other `p_ν=0`; (IDX.2) and its variance reduce exactly to
  M-quant-G (G.1)--(G.2).

No statement below assumes `s∈(1/2)ℤ`.  The self-status of the corrected
theorem is **SKETCH** until the L6 loop converges.

---

## 1. L-A: what is unconditional, and the obstruction to the advertised form

### ⟨1⟩1. LEMMA L-A-fin (finite-window coset integrality)

**ASSUME.** D26(INT), H-MQG(2), `W=[a,b]`, and `c_0∈W`.

**PROVE.** There is `ρ_{W,c_0}∈ℝ/ℤ` such that
`spec Q̂_{W,c_0}⊂ρ_{W,c_0}+ℤ`; the same coset occurs at every time.

**⟨2⟩1.** Choose `κ∈[0,1)` with `c=e^{2πiκ}`.  Then
`spec S^z⊂κ+ℤ`.

*Justification.* D26 and the finite-dimensional spectral computation
`e^{2πiλ}=c ⇒ λ-κ∈ℤ`.  This is named computation **IDX-FW.1**.  It is the
exact finite-window ingredient used in
`refs/arxiv-1810.07351/Index_Re.tex`, §“The index theorem”,
(`A:IntegerCharge`) and (`eq: choice t`); no BBDF dynamical conclusion is
imported.

**⟨2⟩2.** Expanding D13(a) gives

`Q̂_{W,c_0}=Σ_{x=a}^bS^z_x+s(a+b-1-2c_0)`.

*Justification.* M-quant-G (G.3), proved there by the named finite-sum
computation, and D13(a).

**⟨2⟩3.** Therefore one may take

`ρ_{W,c_0}=|W|κ+s(a+b-1-2c_0)  (mod ℤ)`.

*Justification.* ⟨2⟩1--⟨2⟩2 and addition of finite spectra of commuting
on-site operators; named computation **IDX-FW.2**.

**⟨2⟩4.** For the Heisenberg observable
`Q̂_{W,c_0}(t)=α_t(Q̂_{W,c_0})`, the spectrum and hence the offset are the
same.

*Justification.* Spectrum is invariant under the H-MQG(3) C*-automorphism
`α_t`; named computation **IDX-FW.3**.

**⟨2⟩5. QED.**

### ⟨1⟩2. LEMMA L-A-arith (the valid operator implication)

**ASSUME.** A self-adjoint `Q̂` exists and
`e^{2πiQ̂}=e^{2πiq_0}I` for some `q_0∈ℝ`.

**PROVE.** `Q̂` is pure point and `spec Q̂⊂q_0+ℤ`.

**⟨2⟩1.** The spectral measure of `Q̂` vanishes outside
`{λ:e^{2πiλ}=e^{2πiq_0}}=q_0+ℤ`.

*Justification.* Spectral functional calculus, named computation
**IDX-SA.1**.

**⟨2⟩2.** Hence `I=Σ_{n∈ℤ}E_{Q̂}({q_0+n})` strongly and `Q̂` is the direct
sum of its eigenspaces.

*Justification.* Countable additivity of the spectral resolution and
⟨2⟩1; named computation **IDX-SA.2**.

**⟨2⟩3. QED.**  This proves the spectral conclusion, but not either premise.

### ⟨1⟩3. PROPOSITION L-A-obstruction (D17 does not give `Q̂`)

**ASSUME.** H-MQG(1)--(3), D9, D17, and D26(INT).

**PROVE.** These hypotheses admit a state in `𝒦^{(1)}_{αβ}` for which the
regularised window charges have no self-adjoint strong-resolvent limit.

**⟨2⟩1.** Let one site have basis `|m⟩`,
`m∈{-3/2,-1/2,1/2,3/2}`, and `S^z|m⟩=m|m⟩`.  Let
`G=U(1)⋊ℤ_2`, with the circle generated by `S^z` and the reflection
`R|m⟩=|-m⟩`.  Take the `χ=1` vacua
`α=⊗|1/2⟩`, `β=⊗|-1/2⟩`, and `H=0`.

*Justification.* Direct representation check **IDX-CE.1**:
`RS^zR=-S^z`, `e^{2πiS^z}=-I`, the two product tensors satisfy D1 and D2(a),
reflection exchanges them, and `H=0` satisfies H-MQG(3).  Here `s=1/2` is an
example value, not an assumption in the theorem.

**⟨2⟩2.** For `n≥1`, put `ε_n=(n+1)^{-1/2}` and

`|ψ_{-n}⟩=sqrt(1-ε_n²)|1/2⟩+(ε_n/sqrt2)(|-1/2⟩+|3/2⟩)`.

Take the product state `ϱ` with these vectors at `-n` and `|-1/2⟩` at every
site `x≥0`.

*Justification.* Product-state construction **IDX-CE.2**; each displayed
vector is normalised.

**⟨2⟩3.** `ϱ∈𝒦^{(1)}_{αβ}`, including D17's optional spatial first moment.

*Justification.* `|ψ_{-n}⟩→|1/2⟩`, so product factorisation gives both D9(a)
limits.  Moreover
`⟨ψ_{-n}|S^z|ψ_{-n}⟩=1/2` exactly and the right expectation is `-1/2`, so
both D17 sums, including their `|x|`-weighted version, are identically zero.
This is named computation **IDX-CE.3**.

**⟨2⟩4.** With `c_0=-1`, the charge on `W_N=[-N,N]` has, in the cyclic
product vector, the same spectral distribution as
`L_N=Σ_{n=1}^N(S^z_{-n}-1/2)`.  Its characteristic function is

`φ_N(t)=Π_{n=1}^N[1-ε_n²(1-cos t)]`.

*Justification.* D13(a)/(IDX.1); the right-tail summands annihilate the
right product vector.  The three values of each left summand are
`0,-1,+1` with probabilities `1-ε_n²,ε_n²/2,ε_n²/2`.  Named computation
**IDX-CE.4**.

**⟨2⟩5.** If `V_N=Σ_{n=1}^Nε_n²`, then `V_N→∞` and
`sup_k P(L_N=k)≤C V_N^{-1/2}`.

*Justification.* On `[-π,π]`, `1-cos t≥2t²/π²`; hence
`|φ_N(t)|≤exp(-2V_Nt²/π²)`.  Fourier inversion and the Gaussian integral give
the bound.  Named computation **IDX-CE.5**.

**⟨2⟩6.** `⟨Ω_ϱ,(Q̂_{W_N,-1}-i)^{-1}Ω_ϱ⟩→0`.

*Justification.* For fixed `K`, the contribution from `|k|≤K` is at most
`(2K+1)CV_N^{-1/2}` by ⟨2⟩5, while the complement is at most `1/K` in
absolute value; take `N→∞`, then `K→∞`.  Named computation **IDX-CE.6**.

**⟨2⟩7.** No self-adjoint strong-resolvent limit can exist.

*Justification.* Such a limit `Q̂` would make the resolvents converge strongly,
but for every self-adjoint `Q̂`,
`Im⟨Ω_ϱ,(Q̂-i)^{-1}Ω_ϱ⟩=∫(λ²+1)^{-1}dμ_ϱ(λ)>0`, contradicting ⟨2⟩6.
Named computation **IDX-CE.7**.

**⟨2⟩8. QED.**  D17 controls means, not charge fluctuations or implementability.
Moreover D9 defines `𝒦_{αβ}` as a set of states, while a GNS representation
belongs to one state; “the GNS representation of `𝒦_{αβ}`” has no canonical
meaning without an additional folium choice.  This is a definitional
consequence of D9(a) and the GNS convention in D1(a).

**⟨1⟩3a. Remark (why BBDF does not repair existence).**  BBDF assumes an
approximately invariant clustering state with local charge fluctuations and
uses those hypotheses to prove that its boundary phase at `2π` is trivial.
Those are Assumptions (iii)--(v) in
`refs/arxiv-1810.07351/Index_Re.tex`, §“The index theorem”, and the phase
argument is in §“Proof of Theorem 2.1” around (`Defchi`) and
(`lem:the phase understood`).  H-IDX supplies none of those hypotheses, and
the reference does not construct a regularised total charge in a D9 sector.

---

## 2. (G-IDX.1): the ledger

### ⟨1⟩4. LEMMA L-B (finite-time and ordered-limit ledger)

**ASSUME.** H-MQG(1)--(4), `t_-<t_+`, and `W=[a,b]`.

**PROVE.** If escaped charge is positive outward, then

`2s[ϱ_{t_+}(𝔛_W)-ϱ_{t_-}(𝔛_W)]=-Δq_esc(W;t_-,t_+)`. **(IDX.3)**

**⟨2⟩1.** The finite-time identity is exactly M-flux, with
`Δq_esc=-∫_{t_-}^{t_+}[ϱ_t(j_{a-1|a})-ϱ_t(j_{b|b+1})]dt`.

*Justification.* Active claim **M-flux**, proved in
`memory-quantization.md` §1 from D10(b) and D13(a).  No part is reproved here.

**⟨2⟩2.** Under D27, first take the common `t→±∞` Cesàro limit at fixed `W`
and only then the padded exhaustion `W↑ℤ`; (IDX.3) becomes the asymptotic
ledger.

*Justification.* D27(LR1,LR3,LR4) and D17's prescribed order of limits.

**⟨2⟩3. QED.**

---

## 3. (G-IDX.2): the two-time theorem under (LR)

### ⟨1⟩5. LEMMA L-C (finite-window history law)

**ASSUME.** D26, fixed `W,c_0`, and finite `t_-<t_+`.

**PROVE.** D27's TPM law is a probability supported on `ℤ`, without assuming
that `Q̂_{W,c_0}(t_-)` and `Q̂_{W,c_0}(t_+)` commute.

**⟨2⟩1.** If `E_{W,t}` is the spectral resolution of `Q̂_{W,c_0}(t)`, set

`p_{W;t_-,t_+}(ν)=Σ_{q∈ρ_{W,c_0}+ℤ}
 ||E_{W,t_+}({q-ν})E_{W,t_-}({q})Ψ||²`, `ν∈ℤ`.

*Justification.* Proposed D27(LR2); the first projection is the initial
measurement and the leftmost projection is the final measurement.  This is
named computation **IDX-TPM.1**.

**⟨2⟩2.** Positivity is manifest and summing over `ν,q` gives `1`.

*Justification.* The two spectral resolutions each sum to `I`; sequential
use of Parseval gives normalisation.  Named computation **IDX-TPM.2**.

**⟨2⟩3.** `ν=q_- -q_+∈ℤ` because both measurements use the *same* fixed
`W,c_0` and hence the same offset `ρ_{W,c_0}`.

*Justification.* L-A-fin ⟨1⟩1.  This is offset cancellation before either
limit; it is not spectral arithmetic for a difference of noncommuting
operators.

**⟨2⟩4. QED.**

### ⟨1⟩6. LEMMA L-D (TPM mean and the dephasing defect)

**ASSUME.** The hypotheses of ⟨1⟩5.

**PROVE.** With
`𝒟_{W,t_-}(A)=Σ_qE_{W,t_-}({q})AE_{W,t_-}({q})`,

`Σ_ννp_{W;t_-,t_+}(ν)=
 ⟨Q̂(t_-)⟩-⟨𝒟_{W,t_-}(Q̂(t_+))⟩`.                 **(IDX.4)**

**⟨2⟩1.** The first measured value contributes `Σ_qq⟨E_{t_-}({q})⟩` and the
second contributes `Σ_q⟨E_{t_-}({q})Q̂(t_+)E_{t_-}({q})⟩`.

*Justification.* Expand the first moment of the probability in ⟨1⟩5 and use
the final spectral resolution; named computation **IDX-TPM.3**.

**⟨2⟩2.** These are respectively the two terms on the right of (IDX.4).

*Justification.* Spectral functional calculus and the displayed definition
of `𝒟`; named computation **IDX-TPM.4**.  **⟨2⟩3. QED.**

### ⟨1⟩7. THEOREM (G-IDX.2)

**ASSUME.** H-IDX, including D27(LR).

**PROVE.** The ordered limit `p` is supported on `ℤ` and obeys (IDX.2).

**⟨2⟩1.** At fixed `W`, double Cesàro averaging of (IDX.4), followed by the
common subsequence, gives

`Σ_ννp_W(ν)=ω_W^-(Q̂_{W,c_0})-ω_W^+(Q̂_{W,c_0})`.

*Justification.* D27(LR1--LR2); LR2 is exactly the vanishing averaged
dephasing defect.  This explicitly closes the two-time landmine.

**⟨2⟩2.** Therefore
`Σ_ννp_W(ν)=-2s[ω_W^+(𝔛_W)-ω_W^-(𝔛_W)]`.

*Justification.* (IDX.1); the common scalar `-2sc_0` cancels exactly.

**⟨2⟩3.** Along the padded exhaustion, `p_W⇒p`, `p(ℤ)=1`, and
`Σνp_W(ν)→Σνp(ν)`.

*Justification.* D27(LR3): first-moment tightness prevents both loss of mass
and loss of the first moment.  Since `ℤ` is closed and every `p_W` is
supported there, the limit is supported there.  The W-dependent
`ρ_{W,c_0}` cannot smear because it was removed in ⟨1⟩5.⟨2⟩3 before the
spatial limit.  This closes the weak-limit-smearing landmine.

**⟨2⟩4.** Taking the spatial limit in ⟨2⟩2 yields (IDX.2).

*Justification.* D27(LR4), ⟨2⟩3, and `s>0` from H-MQG(2).

**⟨2⟩5.** No plane-wave or soft limit was taken.

*Justification.* H-MQG(4) and D17: the normalisable packet is fixed before
all limits.  **⟨2⟩6. QED.**

---

## 4. (G-IDX.3): exact reduction to M-quant-G

### ⟨1⟩8. COROLLARY (consistency under H-AD-G)

**ASSUME.** H-IDX, D27, and additionally H-AD-G exactly as in M-quant-G.

**PROVE.** `p=(1-⟨N_T⟩)δ_0+⟨N_T⟩δ_2`, and (IDX.2) is (G.1)--(G.2).

**⟨2⟩1.** Reflection has core-charge change `0`; transmission has core-charge
change `-2`.

*Justification.* M-quant-G ⟨1⟩4: `q_L-q_in=0` and `q_T-q_in=2`, with
`2sδx+(q_out-q_in)=0`.

**⟨2⟩2.** Since `ν` was defined as escaped change, i.e. minus core change,
its channel values are `0` and `2`; their weights are
`1-⟨N_T⟩` and `⟨N_T⟩`.

*Justification.* D18(AD2--AD4): the incoming local remainder is a definite
kink-charge eigenstate, while the two outgoing local remainders are the
charge eigenstates whose changes are fixed in ⟨2⟩1.  Their limiting spectral
projections are the orthogonal reflected/transmitted channel projections of
AD2.  Thus the TPM Born weights are `1-⟨N_T⟩,⟨N_T⟩`.  Coherence is retained;
no norm-mixture replacement is used.  This is the channel identification in
M-quant-G ⟨1⟩5.

**⟨2⟩3.** (IDX.2) becomes `δx=-⟨N_T⟩/s`, and the displacement variance is

`(2s)^{-2}Var_p(ν)=s^{-2}⟨N_T⟩(1-⟨N_T⟩)`.

*Justification.* Bernoulli computation **IDX-RED.1** and ⟨2⟩2; these are
exactly M-quant-G (G.1)--(G.2).

**⟨2⟩4. QED.**

---

## 5. CHECKER SPEC

Create `theory/checks/memory_index_check.py` only after this shard is merged.
It must implement these deterministic certificates.

1. **IDX-C1 (finite-window offset and TPM).**  Use
   `S^z=diag(-3/2,-1/2,1/2,3/2)`, a three-site window, two fixed seeded Haar
   unitaries for the two Heisenberg times, and a fixed seeded normalised
   complex vector.  Compute the two spectral resolutions and the TPM law.
   Expected: normalisation residue `<10^-12`, all nonzero increments within
   `10^-12` of `ℤ`, and (IDX.4) residue `<10^-12`.
2. **IDX-C2 (two-time red mutation).**  Replace the TPM mean by the naive
   unmeasured difference `⟨Q̂(t_-)⟩-⟨Q̂(t_+)⟩` while keeping the same
   noncommuting seeded unitaries.  This mutation must fail at `>10^-6`.
   It certifies that D27(LR2), not “difference of lattice observables”, closes
   the two-time step.
3. **IDX-C3 (D17 counterexample).**  For `N=2^j`, `j=4,…,16`, compute
   `V_N`, the Fourier distribution from **IDX-CE.4**, and
   `r_N=Σ_kP(L_N=k)/(k-i)`.  Expected: `V_N` grows as `log N`,
   `max_kP(L_N=k)√V_N` stays bounded, and `|r_N|` decreases.  Mutating
   `ε_n` to `(n+1)^{-1}` must fail the registered `V_N→∞` growth test.
4. **IDX-C4 (weak-limit red mutation).**  Feed
   `p_m=(1-1/m)δ_0+(1/m)δ_m`.  The checker must report tight weak convergence
   but reject first-moment convergence because D27(LR3) fails.  This kills
   the “tightness alone is enough” mutation.
5. **IDX-C5 (M-quant-G reduction).**  Symbolically substitute
   `p_0=1-P`, `p_2=P`; expected mean `-P/s` and variance
   `P(1-P)/s²`.  Mutating the transmitted escaped charge `2→1` must fail both
   exact target expressions.

---

## 6. MERGE PROPOSALS

### 6.1 Exact text to append to `definitions.md`

```markdown
## D26 (circle-integral on-site charge)

For the selected Hermitian circle charge `S^z=-iq(ξ)`, hypothesis **(INT)**
means that there is `c∈U(1)` with `e^{2πiS^z_x}=cI` on one site.  Equivalently,
after choosing the unique `κ∈[0,1)` with `c=e^{2πiκ}`,
`spec S^z⊂κ+ℤ`.  No condition on the real vacuum-density parameter `s>0` is
included or inferred.

## D27 (charge-history local relaxation, LR)

Fix the D17 vector `Ψ`, a cut `c_0`, and a padded exhaustion
`W_m=[a_m,b_m]↑ℤ` containing `c_0`.  Put
`Q̂_{W,c_0}=2s(𝔛_W-c_0)` and let `E_{W,t}` be the spectral resolution of its
Heisenberg translate.  **(LR)** means:

1. There is one sequence `T_n→∞` such that, for every fixed `W`, the Cesàro
   states
   `ω^+_{W,n}(A)=T_n^{-1}∫_{T_n}^{2T_n}⟨Ψ,α_t(A)Ψ⟩dt` and
   `ω^-_{W,n}(A)=T_n^{-1}∫_{-2T_n}^{-T_n}⟨Ψ,α_t(A)Ψ⟩dt`, `A∈𝔄_W`,
   and the double-Cesàro TPM laws
   `p_{W,n}(ν)=T_n^{-2}∫_{T_n}^{2T_n}dt_+∫_{-2T_n}^{-T_n}dt_-
   Σ_q||E_{W,t_+}({q-ν})E_{W,t_-}({q})Ψ||²`
   converge.  The sum is over `q∈spec Q̂_{W,c_0}` and absent spectral values
   contribute zero.
2. With `𝒟_{W,t_-}(A)=Σ_qE_{W,t_-}({q})AE_{W,t_-}({q})`, the double-Cesàro
   average of
   `⟨Ψ,[𝒟_{W,t_-}(Q̂_{W,c_0}(t_+))-Q̂_{W,c_0}(t_+)]Ψ⟩`
   tends to zero for every fixed `W`.  This is only a first-moment
   nondemolition condition; operator asymptotic commutativity is not assumed.
3. Writing `p_W` for the fixed-window time limit, `p_{W_m}` converges weakly
   to a probability `p` and the family is first-moment tight:
   `lim_{M→∞}sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν)=0`.
   If `W_m^∘` is obtained by deleting one interaction-range collar from both
   edges, `||p_{W_m}-p_{W_m^∘}||_TV→0` (vanishing boundary-straddling mass).
4. The ordered wall expectation
   `δx=lim_{m→∞}[ω^+_{W_m}(𝔛_{W_m})-ω^-_{W_m}(𝔛_{W_m})]`
   exists.  Infinite-volume dynamics is formed first, the fixed-window time
   limits second, and the spatial exhaustion last.  No plane-wave or `k→0`
   interchange is included.
```

### 6.2 Exact rows to append to `claims/CLAIMS.md`

```markdown
| M-INDEX-fin | Under D26(INT), every finite-window regularised wall charge `Q̂_{W,c}=2s(𝔛_W-c)` has spectrum in one coset of `ℤ`, and the escaped increment in the explicit two-projective-measurement protocol is integer-valued because the two fixed-window offsets cancel. | SKETCH | D13(a), D26 | theory/memory-index.md ⟨1⟩1, ⟨1⟩5 | proposed memory_index_check.py IDX-C1,C2 |
| M-INDEX-spec | Under H-MQG(1)--(4), D26(INT), and D27(LR), the ordered TPM escaped-charge law is supported on `ℤ` and `δx=-(2s)^{-1}Σ_ννp_ν`; under H-AD-G it reduces exactly to M-quant-G (G.1)--(G.2).  This is a protocol-explicit conditional theorem, not a proof of LR or of a sector-wide total-charge operator. | SKETCH | M-flux, M-quant-G, D13, D17, D26, D27 | theory/memory-index.md ⟨1⟩4--⟨1⟩8 | proposed memory_index_check.py IDX-C1--C5 |
| M-INDEX-LA-strong | D9+D17+(INT) imply existence of a self-adjoint regularised total charge in every `𝒦_{αβ}` GNS representation. | REFUTED | — | counterexample: theory/memory-index.md ⟨1⟩3 | proposed memory_index_check.py IDX-C3 |
```

### 6.3 Exact rows to append to `notation.md`

```markdown
| `Q̂_{W,c}` | regularised fixed-window wall charge `2s(𝔛_W-c)`; a bounded local observable | proposed definitions.md D27; theory/memory-index.md (IDX.1) |
| `E_{W,t}`, `𝒟_{W,t}` | spectral resolution of `Q̂_{W,c}(t)` and its nonselective spectral-dephasing map | proposed definitions.md D27 |
| `p_{W;t_-,t_+}`, `p_ν` | finite-window TPM escaped-charge law (`ν=q_-−q_+`) and its ordered D27 limit | proposed definitions.md D27; theory/memory-index.md ⟨1⟩5--⟨1⟩7 |
```

---

## 7. HONEST STATUS

1. **Proved in this shard:** unconditional finite-window coset integrality;
   the exact TPM support and moment identity; the M-flux ledger by citation;
   quantisation of the ordered TPM outcome law under the explicit D27
   relaxation/nondemolition/first-moment-tightness assumptions; and exact
   reduction to M-quant-G.
2. **Refuted:** the requested sector-wide L-A existence statement under only
   D9, D17, and (INT).  The counterexample is already `χ=1` and `H=0`; the
   failure is that D17 controls means but not fluctuations.  This is the main
   retreat from the campaign target.
3. **Assumed, not derived:** D27.  Neither injective-MPS clustering nor
   finite-range dynamics is shown here to imply the two-time first-moment
   nondemolition clause or the spatial first-moment tightness clause.
4. **Protocol scope:** the probability law is the explicitly stated TPM law.
   Without asymptotic commutativity there is no protocol-independent spectral
   law of `Q̂(+∞)-Q̂(-∞)`; no such operator is claimed.
5. **Limit scope:** offsets cancel at fixed `W` before `W↑ℤ`; first-moment
   tightness, stronger than bare tightness, is used to pass the expectation.
   D17's spatial first-moment clause does not by itself supply this spectral
   uniform integrability.
6. **Forbidden inputs not used:** no integrability, model-specific scattering,
   channel completeness (except only in the consistency corollary), soft
   interchange, or assumption `s∈(1/2)ℤ`.
7. **Status:** M-INDEX-spec is **SKETCH** pending hostile L6 criticism.
   M-INDEX-full was not obtained; the advertised L-A is false as stated.
