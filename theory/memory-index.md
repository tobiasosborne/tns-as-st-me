<!-- ROLE: MERGED Lane-T1 shard for M-INDEX (round-2 synthesis).
     Baseline: the r1-PASSED codex shard (verdict theory/verdicts/memory-index-r1.md,
     PASS with MINOR 1-4 + NOTE 5-6 — all swept here).
     Imports from theory/memory-index-b.md (FAILed lane B, verdict
     theory/verdicts/memory-index-b-r1.md) ONLY at the strength of that critic's
     surviving-weaker-statement lines and fix demands: the decircularized density
     quantization lemma (⟨1⟩9), the zero-offset corollary (⟨1⟩10), the pure-tail
     vacuum charge laws with tail-specific normal ordering (⟨1⟩11), and the
     nonscalar-virtual-circle obstruction (⟨1⟩12, nonexistence direction only).
     Orchestrator obligations: briefs/synthesis-notes.md items 1-8, all applied.
     Every edit relative to the baseline is traceable to a named objection or
     synthesis-notes item; nothing was silently strengthened.
     Status: SKETCH until the r2 adjudication converges. -->

# M-INDEX — charge-history quantisation without channel completeness

## 0. Statement

The labels **D26** and **D27** are the LIVE numbered definitions in
`definitions.md` (merged 2026-08-28, commit `e0ce677`), which is authoritative
for their text; §8 now holds only pointers (L4, r2 objection 8).

**Sign convention (fixed once; resolves synthesis-notes item 1).**  All laws
are indexed primarily by the measured window-charge increment
`ΔQ_W := q_+ - q_-` (final minus initial TPM readout of the SAME fixed-window
observable `Q̂_{W,c_0}`); the escaped charge is `ν := -ΔQ_W = q_- - q_+`.  The
ledger identity is stated once:

`2s·δx = lim E[ΔQ_W] = -Σ_ν ν p_ν`,  i.e.  `δx = -(1/(2s)) Σ_ν ν p_ν`.

Under H-AD-G, transmission has `ΔQ_W = -2` and `ν = +2`; the support is
`{ΔQ_W = 0, -2} ≡ {ν = 0, +2}`, at `s = 1/2` equivalently `δx ∈ {0, -2}`
sites.  Checked against M-quant-G:
`δx = -(1/(2s))·2⟨N_T⟩ = -⟨N_T⟩/s` = (G.1), and the Bernoulli variance =
(G.2) (verified line by line in memory-index-r1.md V6).  The existing probe
`theory/checks/memory_index_probe.py` tabulates by the convention-free `Q_W`
value with predicted support `{0, -2}` — the same convention.  The campaign
target's `ν`-indexing is recovered by `ν = -ΔQ_W` and is consistent under
exactly this dictionary.

### THEOREM M-INDEX-spec (sharpened statement)

**ASSUME (H-IDX).**

1. H-MQG(1)--(4) of `memory-quantization-general.md`, verbatim.  In
   particular there is no H-AD-G/D18 assumption and no channel inventory.
2. **(INT)** is D26 (`definitions.md`): for the selected Hermitian charge,
   `exp(2πiS^z_x)=c I`, `|c|=1`.
3. Only for (G-IDX.2), **(LR)** is D27 (`definitions.md`): common-sequence Cesàro
   relaxation of the two one-time window states and the two-projective-
   measurement (TPM) history law, vanishing first-moment measurement
   back-action, and first-moment-tight spatial exhaustion.
4. Only for the unconditional strengthenings (G-IDX.0-ρ) and ⟨1⟩11--⟨1⟩12:
   hypothesis **(S)** of D2(e) at both tails, stated at every step that uses
   it.

**PROVE.**  For `W=[a,b]` and a fixed `c_0∈W`, use the already-defined D13(a)
coordinate and the identity

`Q̂_{W,c_0}:=2s(𝔛_W-c_0)`                                      **(IDX.1)**

(the name is live in `notation.md`; the equality is (G.3) of
M-quant-G, not a new definition of `𝔛_W`).  Then:

- **(G-IDX.0-fin)** unconditionally, every `Q̂_{W,c_0}` has spectrum in one
  coset of `ℤ`, and every fixed-window TPM escaped-charge increment is in
  `ℤ`.
- **(G-IDX.0-ρ)** under additionally (S) at both tails: the common tail
  density `ρ := ω_α(S^z) = -ω_β(S^z)` is quantized, `2ρ ∈ ℤ` (⟨1⟩9 —
  derived, not assumed), and the finite-window coset offset vanishes
  identically: `spec Q̂_{W,c_0} ⊆ ℤ` for every `W` and every `c_0`, with
  `e^{2πiQ̂_{W,c_0}} = 𝟙` exactly in `𝔄_W` (⟨1⟩10).
- **(G-IDX.0-strong)** as requested in the campaign target is **false**, by
  two independent mechanisms: D9+D17+(INT) do not imply that `Q̂_{W,c_0}`
  has a self-adjoint infinite-window limit — mechanism A is the
  log-divergent-fluctuation counterexample ⟨1⟩3 (outside every A2 folium);
  mechanism B is the nonscalar-virtual-circle obstruction ⟨1⟩12 (on the A2
  folium itself, with boundary-law fluctuations).  Consequently there is no
  unconditional sector-wide operator `Q̂` to which the requested pure-point
  conclusion can be applied.  If such an operator is supplied and
  `exp(2πiQ̂)` is scalar, its spectrum is indeed pure point in one coset;
  this arithmetic implication is proved in ⟨1⟩2.  The surviving
  folium-restricted candidate is recorded as an explicit CONJECTURE in
  ⟨1⟩3b.
- **(G-IDX.1)** at finite time, `2s` times the wall-coordinate change is minus
  the charge escaped through the two boundaries; the ordered asymptotic
  ledger is the D27-defined `δx` (a definition plus a one-line corollary,
  not a hypothesis — see D27).
- **(G-IDX.2)** under (LR), every (LR3)-subsequential limit `p` of the TPM
  escaped-charge laws is a probability supported on `ℤ` with

  `δx=-(1/(2s)) Σ_{ν∈ℤ}νp_ν`                                  **(IDX.2)**

  along that subsequence.  Support quantization is subsequence-free
  (tightness-only); D27's optional convenience clause buys uniqueness of the
  VALUE `δx`, nothing else.  Thus individual outcomes of this explicit
  history protocol, not their average, are multiples of `1/(2s)`.  Bound
  states, absorption, and extra channels are allowed because none is named.
- **(G-IDX.3)** under (LR) and additionally H-AD-G (with the AD3 reading
  named in ⟨1⟩8), `p_0=1-⟨N_T⟩`, `p_2=⟨N_T⟩`, all other `p_ν=0`; (IDX.2)
  and its variance reduce exactly to M-quant-G (G.1)--(G.2).

**Register discipline (binding; memory-index-b-r1 objections 2--4).**
`δx` is never claimed quantized — it is a `{p_ν}`-average.  Quantization
attaches to exactly two objects: (i) the TPM history law above, and (ii) the
direct channel law under H-AD-G: `spec(-2sΔX) ⊆ {0,2}` with weights
`1-⟨N_T⟩, ⟨N_T⟩`, hence `δx = -⟨N_T⟩/s` — exactly the active M-quant-G
result, a direct spectral statement about the single operator
`ΔX = -(1/s)N_T`, and **not** a two-time coupling theorem: M-quant-G
constructs no pair of asymptotic charge random variables and no joint law.
No implication H-AD-G ⟹ (LR) is claimed anywhere in this shard; D18(AD3)'s
frozen words fix no window-marginal topology (landmine L2, §6), and whether
the strengthened AD3 reading of ⟨1⟩8 implies D27 is left open.

No statement below assumes `s∈(1/2)ℤ`; under (S) the tail density is instead
*derived* to satisfy `2ρ∈ℤ` (⟨1⟩9).  The self-status of the corrected
theorem is **SKETCH** until the L6 loop converges.

---

## 1. L-A: what is unconditional, and the obstruction to the advertised form

### ⟨1⟩1. LEMMA L-A-fin (finite-window coset integrality)

**ASSUME.** D26(INT), H-MQG(2), `W=[a,b]`, and `c_0∈W`.

**PROVE.** There is `κ_{W,c_0}∈ℝ/ℤ` such that
`spec Q̂_{W,c_0}⊂κ_{W,c_0}+ℤ`; the same coset occurs at every time.

*(The offset symbol is `κ_{W,c_0}` — renamed from the baseline's
`ρ_{W,c_0}` to free `ρ` for the imported density parameter of ⟨1⟩9; an L4
collision fix, no content change.)*

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

`κ_{W,c_0}=|W|κ+s(a+b-1-2c_0)  (mod ℤ)`.

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

### ⟨1⟩3. PROPOSITION L-A-obstruction (mechanism A: D17 does not give `Q̂`)

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

### ⟨1⟩3b. THEOREM M-INDEX-LA-folium (fixed-kink implementer)

Let `ϱ_0=ϱ_x^{(g)}` be the fixed bare A2/D1(e′) kink, and let the selected
circle be common-unbroken, `h_θ∈H_α∩H_β`, with (S) at both tails and
D26(INT).  In the GNS representation of `ϱ_0`, the circle automorphisms are
implemented by a strongly continuous unitary group `U(θ)=e^{iθQ̂}` with
`e^{2πiQ̂}∈ℂ𝟙`; hence `Q̂` is pure point with spectrum in one coset of `ℤ`.

Proof: `theory/folium-implementer.md`
⟨1⟩1--⟨1⟩6.  Injectivity turns every nearby circle-rotated junction matrix
into a continuously varying local vector in the fixed kink GNS folium;
irreducibility then gives a locally `C¹` projective implementer, whose scalar
cocycle is removed explicitly on the one-dimensional parameter group.

This is the implementer route, not a strong-resolvent limit of
`Q̂_{W,c_0}`.  For nonscalar `V_θ`, ⟨1⟩12 still proves that those bare window
unitaries are not Cauchy; the compatibility is proved in the folium shard
⟨1⟩7.  The theorem covers the fixed bare A2 kink (and finite-core variants
whose padded blocked tensors span `M_χ(ℂ)`), not arbitrary D1(e′) finite-core
modifications.  **Status: PROVED** (capped L6 passed: critic theory/verdicts/blitz-la-folium-r1.md, 0 FATAL / 0 MAJOR).
(live since 2026-08-28).

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
and only then the padded exhaustion `W↑ℤ`; the resulting asymptotic ledger
identity is exactly the display of ⟨1⟩7.⟨2⟩2,
`Σ_ννp_W(ν)=-2s[ω_W^+(𝔛_W)-ω_W^-(𝔛_W)]`, whose spatial limit defines `δx`.

*Justification.* D27(LR1,LR3), the D27 definition of `δx`, and D17's
prescribed order of limits; the asymptotic content is displayed and proved
in ⟨1⟩7 and is not re-derived here.  *(Leaf repaired per memory-index-r1
NOTE 6: the former prose clause now points at ⟨1⟩7's display.)*

**⟨2⟩3. QED.**

---

## 3. (G-IDX.2): the two-time theorem under (LR)

### ⟨1⟩5. LEMMA L-C (finite-window history law)

**ASSUME.** D26, fixed `W,c_0`, and finite `t_-<t_+`.

**PROVE.** D27's TPM law is a probability supported on `ℤ`, without assuming
that `Q̂_{W,c_0}(t_-)` and `Q̂_{W,c_0}(t_+)` commute.

**⟨2⟩1.** If `E_{W,t}` is the spectral resolution of `Q̂_{W,c_0}(t)`, set

`p_{W;t_-,t_+}(ν)=Σ_{q∈κ_{W,c_0}+ℤ}
 ||E_{W,t_+}({q-ν})E_{W,t_-}({q})Ψ||²`, `ν∈ℤ`.

*Justification.* D27(LR2); the first projection is the initial
measurement and the leftmost projection is the final measurement.  This is
named computation **IDX-TPM.1**.

**⟨2⟩2.** Positivity is manifest and summing over `ν,q` gives `1`.

*Justification.* The two spectral resolutions each sum to `I`; sequential
use of Parseval gives normalisation.  Named computation **IDX-TPM.2**.

**⟨2⟩3.** `ν=q_- -q_+∈ℤ` (the §0 convention, `ν=-ΔQ_W`) because both
measurements use the *same* fixed `W,c_0` and hence the same offset
`κ_{W,c_0}`.

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

**PROVE.** Every (LR3)-subsequential ordered limit `p` is supported on `ℤ`
and obeys (IDX.2); under D27's convenience clause, `p` and `δx` are unique.

**⟨2⟩1.** At fixed `W`, double Cesàro averaging of (IDX.4), followed by the
common subsequence, gives

`Σ_ννp_W(ν)=ω_W^-(Q̂_{W,c_0})-ω_W^+(Q̂_{W,c_0})`.

*Justification.* D27(LR1--LR2); LR2 is exactly the vanishing averaged
dephasing defect.  This explicitly closes the two-time landmine.

**⟨2⟩2.** Therefore
`Σ_ννp_W(ν)=-2s[ω_W^+(𝔛_W)-ω_W^-(𝔛_W)]`.

*Justification.* (IDX.1); the common scalar `-2sc_0` cancels exactly.

**⟨2⟩3.** Along the padded exhaustion, with (LR3) in its tightness-only
form: every subsequence of `{p_{W_m}}` has a further subsequence
`p_{W_{m_j}}⇒p'` with `p'` a probability on `ℤ` and
`Σνp_{W_{m_j}}(ν)→Σνp'(ν)`.  EVERY such limit is supported on `ℤ` —
support quantization is subsequence-free.  Under the optional convenience
clause the limit `p` is unique.

*Justification.* Prokhorov on the closed set `ℤ` plus (LR3)'s `(1+|ν|)`
weight, which prevents both loss of mass and loss of the first moment.
Since `ℤ` is closed and every `p_W` is supported there, every weak limit is
supported there.  The W-dependent `κ_{W,c_0}` cannot smear because it was
removed in ⟨1⟩5.⟨2⟩3 before the spatial limit.  This closes the
weak-limit-smearing landmine.  *(Restated per memory-index-r1 objection 2:
weak convergence of the full sequence is a convenience normalisation for the
VALUE, not an input to support quantization.)*

**⟨2⟩4.** Taking the spatial limit in ⟨2⟩2 along the same subsequence yields
(IDX.2), with `δx` the D27-defined value — unique under the convenience
clause, otherwise per subsequence.

*Justification.* The D27 definition of `δx` and its one-line existence
corollary, ⟨2⟩3, and `s>0` from H-MQG(2).  *(Former hypothesis LR4 is now a
definition; memory-index-r1 objection 1.)*

**⟨2⟩5.** No plane-wave or soft limit was taken.

*Justification.* H-MQG(4) and D17: the normalisable packet is fixed before
all limits.  **⟨2⟩6. QED.**

---

## 4. (G-IDX.3): exact reduction to M-quant-G

### ⟨1⟩8. COROLLARY (consistency under H-AD-G)

**ASSUME.** H-IDX, D27, and additionally H-AD-G exactly as in M-quant-G,
with D18(AD3) read as **weak-\* convergence of the window restriction, per
channel, to the corresponding kink charge eigenstate**.  This reading is
named here because D18's frozen words fix no topology (landmine L2, §6); it
is the reading M-quant-G's own uses need (memory-index-r1 objection 4).

**PROVE.** `p=(1-⟨N_T⟩)δ_0+⟨N_T⟩δ_2`, and (IDX.2) is (G.1)--(G.2).

**⟨2⟩1.** Reflection has core-charge change `0`; transmission has core-charge
change `-2`.

*Justification.* M-quant-G ⟨1⟩4: `q_L-q_in=0` and `q_T-q_in=2`, with
`2sδx+(q_out-q_in)=0`.

**⟨2⟩2.** (AD3-topology lemma; the two-line lemma demanded by
memory-index-r1 objection 4.)  (i) *Incoming concentration:* for the
incoming kink-charge eigenvalue `q_*`, `E_W({q_*})∈𝔄_W` and, as `t→-∞`,

`‖E_W({q_*})Ψ_t-Ψ_t‖²=1-⟨Ψ_t,E_W({q_*})Ψ_t⟩=1-⟨Ψ,E_{W,t}({q_*})Ψ⟩→0`,

by the named AD3 reading applied to the window observable `E_W({q_*})`: the
incoming window-charge law tends to the point mass at `q_*`.  *(Indexing
convention, fixed per r2 NOTE 14: `E_W` and `E_{W,t}` are D27's objects and
are not redefined here (L4) — under D27's convention `E_{W,t}(·)=α_t(E_W(·))`
— so the time label rides on exactly one of the two factors, never as a fixed
`t_∓` subscript on a running vector `Ψ_t`.  The `α_{-t}` written here at r2
NOTE 14 was a wrong-sign gloss and is withdrawn per r3 objection 5; the
displayed identity is unchanged and is correct under D27.)*
(ii) *Cross-term vanishing:* for the outgoing `r|R⟩+t|T⟩` at running `t→+∞`,
with the same convention,

`|⟨R|E_W({q_R})|T⟩| ≤ ‖E_W({q_R})|T⟩‖
 = ⟨T|E_W({q_R})|T⟩^{1/2} → 0`,

by Cauchy--Schwarz, since the `T`-leg's window law concentrates on
`q_T ≠ q_R`.

*Justification.* The named AD3 reading and the spectral projections
`E_{W,t}({q})∈𝔄_W`; named computation **IDX-AD3.1**.

**⟨2⟩3.** Since `ν` was defined as escaped change, i.e. minus core change,
its channel values are `0` and `2`; their weights are
`1-⟨N_T⟩` and `⟨N_T⟩`.

*Justification.* D18(AD2--AD4) and ⟨2⟩2: the incoming local remainder is a
definite kink-charge eigenstate (⟨2⟩2(i)), the two outgoing local remainders
are the charge eigenstates whose changes are fixed in ⟨2⟩1, and the TPM Born
weights receive no inter-channel cross terms (⟨2⟩2(ii)); the limiting
spectral projections are the orthogonal reflected/transmitted channel
projections of AD2.  Thus the TPM Born weights are `1-⟨N_T⟩,⟨N_T⟩`.
Coherence is retained; no norm-mixture replacement is used.  This is the
channel identification in M-quant-G ⟨1⟩5.

**⟨2⟩4.** (IDX.2) becomes `δx=-⟨N_T⟩/s`, and the displacement variance is

`(2s)^{-2}Var_p(ν)=s^{-2}⟨N_T⟩(1-⟨N_T⟩)`.

*Justification.* Bernoulli computation **IDX-RED.1** and ⟨2⟩3; these are
exactly M-quant-G (G.1)--(G.2).

**⟨2⟩5. QED.**

*Remark (empirical fence; synthesis-notes item 4).*  The probe
`theory/checks/memory_index_probe.py` finds extra integer mass at
`Q_W∈{-1,-3}` carried by near-threshold two-magnon channels with zero group
velocity — outside H-AD-G's two-channel inventory, yet exactly on the
integers.  This is direct empirical support for the channel-free register of
(G-IDX.2) and a concrete reason the two-point corollary (G-IDX.3) needs
H-AD-G's inelastic-threshold fence (AD1: no further propagating channel; no
bound-state component).

---

## 5. Imported lane-B core (decircularized and repaired per memory-index-b-r1)

*Everything in this section enters at the strength of the lane-B critic's
surviving-weaker-statement lines and fix demands; nothing rests on the
FAILed shard's own authority.  Nothing in §§2--4 depends on this section.*

### ⟨1⟩9. LEMMA M-IDX-density (density quantization; unconditional)

**ASSUME.** D1 injective tensors `A_α, A_β`; D2(a) covariance with a common
unbroken circle direction `ξ∈𝔥_α∩𝔥_β` and on-site charge `S^z=-iq(ξ)`;
(S) of D2(e) at `α` and `β`; D26(INT) with scalar `c`.  Write

`ρ := ω_α(S^z)`,  and assume  `ω_β(S^z) = -ρ`

— `ρ` is a **fresh real density parameter**, deliberately NOT D13's
site-spin symbol `s` (whose frozen preamble reads `d=2s+1` and would make
`2s∈ℕ` an assumption; memory-index-b-r1 objection 1).  No cut, no window,
no correlation hypothesis, and no dynamical input enter.

**PROVE.** `e^{2πiρ}=c=e^{-2πiρ}`; hence `e^{4πiρ}=1` and `2ρ∈ℤ`.

**⟨2⟩1.** (IT phase slope = density.)  Put `f_α(θ):=θ_α(exp(θξ))`,
`V_θ:=V_α(exp(θξ))`, `u(θ):=e^{iθS^z}` on one site.  Then
`ω_α(u_x(θ))=e^{if_α(θ)}tr[V_θ^{-1}E_α(V_θ r)]`, and differentiating at
`θ=0` (legitimate by (S); `V_0=𝟙`, `dV_θ/dθ|_0=X_α(ξ)=:X`):

`d/dθ ω_α(u_x(θ))|_0 = if_α'(0)-tr[XE_α(r)]+tr[E_α(Xr)] = if_α'(0)`,

using `E_α(r)=r` and `tr[E_α(Y)]=tr[Y]` (left-canonical).  Also
`d/dθ ω_α(u_x(θ))|_0=iω_α(S^z)=iρ`.  Hence `f_α'(0)=ρ`.

*Justification.* D1(c),(d), D2(b),(e); this is the critic's own derivation
route, `memory-index-b-r1.md` §1(b) (= lane-B NC-1); named computation
**IDX-ρ.1**.

**⟨2⟩2.** (Additivity + continuity.)  `f_α` is additive mod `2π` on the
unbroken circle (Lemma IT, corner-a.md ⟨1⟩2(i), with `exp(θξ)·α=α`); by (S)
it is `C¹` near `0` with `f_α(0)=0`; the continuous lift's additivity defect
is a continuous `2πℤ`-valued function vanishing at the origin, hence `≡0`
near `(0,0)`; Cauchy's functional equation gives `f̃_α(θ)=ρθ` near `0`, and
`f_α(nθ)=nf_α(θ) mod 2π` extends it: `f_α(θ)=ρθ mod 2π` for all `θ∈ℝ`.

*Justification.* Lemma IT (corner-a.md ⟨1⟩2(i)), D2(b),(e), ⟨2⟩1; named
computation **IDX-ρ.2**.

**⟨2⟩3.** (θ=2π.)  (INT) gives `u(2π)=c𝟙`, so (IT) reads
`cA_α^s=e^{if_α(2π)}V_{2π}^{-1}A_α^sV_{2π}`.  By the uniqueness clause of
D2(b) (refs/arxiv-2011.12127, Eq. (eq:XAX=B):
`X^{-1}A^iX=e^{iχ}Y^{-1}A^iY ⟹ χ=0 ∧ X∈e^{iφ}Y`, applied with `Y=𝟙`),
`V_{2π}` is scalar and `e^{if_α(2π)}=c`.  With ⟨2⟩2: `e^{2πiρ}=c`.

*Justification.* (INT), D2(b) uniqueness, ⟨2⟩2.

**⟨2⟩4.** The same computation at `β` (density `-ρ`; same on-site `u`, hence
the same scalar `c` on every site) gives `e^{-2πiρ}=c`.

*Justification.* D2(a) (the circle lies in `H_β`), (S) at `β`, (INT).

**⟨2⟩5.** Dividing: `e^{4πiρ}=1`, so `2ρ∈ℤ`; and `c=e^{2πiρ}∈{±1}`.
**QED.**

*Remark (LSM flavour).*  `U(1)`-covariant injective MPS tails admit only
half-integer-quantized densities given (INT): an LSM-type rigidity,
paralleling the “index = charge density” Example of
refs/arxiv-1810.07351/Index_Re.tex but re-derived in the MPS register with
no gap, clustering, or dynamical input beyond injectivity.  This is a NEW
unconditional result relative to the baseline theorem; claim row
**M-IDX-density** in `claims/CLAIMS.md` (live since 2026-08-28; the status
of record is the one shown there).

*Remark (failed counterexample, recorded per memory-index-b-r1 objection
9(c)).*  A `χ=2` attack at `ρ=0.37` fails by the virtual charge-cycle
obstruction: covariance forces every closed virtual path to satisfy the
filling congruence, so no strongly connected virtual charge graph exists at
non-half-integer density; a period-two escape becomes noninjective, outside
D1.  No `χ≥2` counterexample was found.

### ⟨1⟩10. COROLLARY (zero offset)

**ASSUME.** H-IDX items 1--2, (S) at both tails, and H-MQG(2)'s convention
that the D13(a) calibration parameter equals the tail density (`s=ρ`).

**PROVE.** `κ_{W,c_0}≡0`: for every `W` and every `c_0∈W`,
`e^{2πiQ̂_{W,c_0}}=𝟙` exactly in `𝔄_W`, `spec Q̂_{W,c_0}⊆ℤ` (pure point;
`𝔄_W` is finite-dimensional), and `spec 𝔛_W⊆c_0+(1/2s)ℤ`.

**⟨2⟩1.** From ⟨1⟩9.⟨2⟩3, `c=e^{2πiρ}`, so ⟨1⟩1.⟨2⟩1's `κ` satisfies
`κ≡ρ (mod ℤ)`.  Substituting into ⟨1⟩1.⟨2⟩3 with `s=ρ`:

`κ_{W,c_0} ≡ ρ(b-a+1)+ρ(a+b-1-2c_0) = 2ρ(b-c_0) ≡ 0 (mod ℤ)`,

since `2ρ∈ℤ` (⟨1⟩9.⟨2⟩5) and `b-c_0∈ℤ`.

*Justification.* ⟨1⟩1.⟨2⟩3, ⟨1⟩9; named computation **IDX-ρ.3**.  Both
bookkeeping stages are in public: under (INT) alone the offset drifts with
`W` (the smearing landmine, displayed); the two-tail covariance kills it
identically.  **⟨2⟩2. QED.**

*Remark.*  Nothing in §§2--4 needs this corollary: the TPM increment
cancels the offset at fixed `W` regardless (⟨1⟩5.⟨2⟩3).  It strengthens
L-A-fin from “one coset” to “the zero coset” under (S), and it is what the
existing probe's P1/P2 integrality findings instantiate at `s=1/2`.

### ⟨1⟩11. LEMMA (vacuum charge laws, tail-specific normal ordering)

*(Imported in the repaired form demanded by memory-index-b-r1 objection 5;
scoped to pure tails per objection 8's surviving line.)*

**ASSUME.** As ⟨1⟩9 — in particular NO site-spin symbol `s` and no `s=ρ`
identification (r2 objection 4: this lemma needs neither); the pure vacuum
`ω_α` (or `ω_β`); the **tail-specific vacuum charges**

`Q_W^α := Σ_{x∈W}(S^z_x-ρ)`,  `Q_W^β := Σ_{x∈W}(S^z_x+ρ)`

(uniform normal ordering against the vacuum's own density — NOT the
two-sided `Q̂_{W,c_0}`, whose law in a pure vacuum is the escaping shifted
point mass `δ_{2ρn_R}` and is not tight; that was objection 5's
counterexample).

**PROVE.** For intervals `I` of length `n`, the characteristic functions
`φ_I(θ)=ω_α(e^{iθQ_I^α})` converge uniformly on `[-π,π]` with rate `λ̃^n`
to the continuous limit `|tr(V_θ r)|²`; the laws `μ_I` converge weakly to
the probability measure on `ℤ`

`μ_∞^α(ν)=(2π)^{-1}∫_{-π}^{π}e^{-iθν}|tr(V_θ r)|²dθ`,        **(IDX.5)**

and the family `{μ_I}` is tight.

**⟨2⟩1.** (Exact phase cancellation.)  On an `α` site, the one-site map of
`e^{iθ(S^z-ρ)}` is
`e^{-iθρ}E_{u(θ)}=e^{i(f_α(θ)-ρθ)}L_{V_θ^{-1}}∘E_α∘L_{V_θ}
=L_{V_θ^{-1}}∘E_α∘L_{V_θ}` — the phase cancels exactly for all `θ`, by
`f_α(θ)=ρθ` (⟨1⟩9.⟨2⟩2).  Composing `n` sites gives the single conjugated
transfer power `L_{V_θ^{-1}}∘E_α^n∘L_{V_θ}`.

*Justification.* ⟨1⟩9.⟨2⟩1--⟨2⟩2, D2(d); named computation **IDX-ρ.4**
(= lane-B NC-3, verified independently by the lane-B critic to residue
`1.6·10^{-16}`, memory-index-b-r1.md §8(b)).

**⟨2⟩2.** `φ_I(θ)=tr[V_θ^{-1}E_α^n(V_θ r)]`; with `E_α^n=P_α+O(λ̃^n)`
(D1(c)) and `‖L_{V_θ}‖=1`,
`sup_θ|φ_I(θ)-tr(V_θr)tr(V_θ^{-1}r)|≤Cλ̃^n`, and
`tr(V_θr)tr(V_θ^{-1}r)=|tr(V_θ r)|²` since `V_θ^{-1}=V_θ^†`, `r=r^†>0`;
`[V_θ,r]=0` by Lemma IT (corner-a.md ⟨1⟩2(iv)).

*Justification.* ⟨2⟩1, D1(c); named computation **IDX-ρ.5**.

**⟨2⟩3.** (Support and tightness.)  `spec Q_I^α⊆n(κ-ρ)+ℤ=ℤ`, where
`κ≡ρ (mod ℤ)` follows from `c=e^{2πiρ}` (⟨1⟩9.⟨2⟩3) together with
`c=e^{2πiκ}` (**D26**(INT) directly, and ⟨1⟩1.⟨2⟩1, whose own justification
is D26 plus the finite-dimensional spectral computation; the direct D26
citation is added per r3 NOTE 12) — no site-spin symbol `s` and no `s=ρ`
identification enters, so this step does not import ⟨1⟩10's hypothesis
(r2 objection 4).  Hence `φ_I` is `2π`-periodic and Fourier inversion on `ℤ`
applies.  Truncation inequality (**IDX-ρ.6**, = lane-B NC-4, verified by
the lane-B critic in objection 10): for a law `μ` on `ℤ` and `0<u≤π`,
`u^{-1}∫_{-u}^u(1-Re φ(θ))dθ = Σ_ν μ(ν)·2(1-sinc(uν)) ≥ Σ_{|ν|≥2/u}μ(ν)`.
Applying it with ⟨2⟩2 and continuity of the limit at `0` gives tightness;
inversion plus uniform convergence gives weak convergence to (IDX.5) with
total mass `1`.  **⟨2⟩4. QED.**

*Scope fence (memory-index-b-r1 objections 5 and 8).*  For a two-sided
D1(e′) decorated `α|β` kink reference, the two-sided `Q̂_{W,c}` does match
both tails and the analogous convergence is expected to extend to a fixed
finite middle block — but the exact ordered middle-block CP contraction was
left schematic in lane B and is NOT claimed here.  The certified statements
are: the pure-tail lemma above, and the deep-shell reduction in ⟨1⟩12,
which needs only ⟨1⟩11 plus A2's weak-\* convergence.

### ⟨1⟩12. PROPOSITION (mechanism B: nonscalar virtual circle obstructs `Q̂`)

*(Imported at the strength of memory-index-b-r1 objection 7(d): the
NONEXISTENCE direction only.)*

**ASSUME.** A D1(e′) two-sided decorated kink reference `ϱ_0` with GNS
representation `(H,π,Ω)`; (S), D26(INT); **H-MQG(2)'s `s=ρ`** (the D13(a)
calibration parameter equals the tail density — consumed in ⟨2⟩1 and listed
here per r2 objection 4); and `V_{θ_0}=V_α(exp(θ_0ξ))` nonscalar for some
`θ_0` (either tail; stated for `α`).

**PROVE.** `{e^{iθ_0Q̂_{W,c_0}}}_W` is not Cauchy in the strong topology on
`Ω`; hence the window charges `Q̂_{W,c_0}` have no self-adjoint
strong-resolvent limit in this GNS representation.

**⟨2⟩1.** For nested windows `W⊂W'` differing by a shell `I` of length `ℓ`
deep in the `α` tail (left of the cut), the on-site summands commute, so

`‖(e^{iθQ̂_{W',c_0}}-e^{iθQ̂_{W,c_0}})Ω‖² = 2-2 Re⟨Ω,e^{-iθQ_I^α}Ω⟩`,

where `Q̂_{W',c_0}-Q̂_{W,c_0}=Σ_{x∈I}S^z_x-sℓ` equals the ⟨1⟩11
tail-normal-ordered shell charge `Q_I^α=Σ_{x∈I}(S^z_x-ρ)` **precisely because
`s=ρ`** (H-MQG(2); this is where the ASSUME's identification is consumed —
r2 objection 4).

*Justification.* On-site commutation and unitarity, H-MQG(2)'s `s=ρ`; named
computation **IDX-ρ.7** (= lane-B NC-5a).

**⟨2⟩2.** Iterated limit: at fixed `ℓ`, letting the distance from `I` to the
junction, decorations, and cut tend to infinity,
`⟨Ω,e^{-iθQ_I^α}Ω⟩→ω_α(e^{-iθQ_I^α})` by A2's weak-\* convergence at rate
`λ̃^{dist}` (corner-a-kinks.md ⟨1⟩8; D1(e′)); then `ℓ→∞` gives
`→|tr(V_θr_α)|²` by ⟨1⟩11.⟨2⟩2.  This routes the computation entirely
through the certified pure-tail lemma and avoids the schematic middle-block
contraction (memory-index-b-r1 objection 8).

*Justification.* A2 (PROVED), ⟨1⟩11.

**⟨2⟩3.** For `r>0`, `tr r=1`, unitary `V`: `|tr(Vr)|≤1` with equality iff
`V∈U(1)𝟙` (Cauchy--Schwarz with strict positivity; named computation
**IDX-ρ.8**, = lane-B NC-5b).  Nonscalar `V_{θ_0}` therefore gives, along
the iterated family of ⟨2⟩2,

`liminf ‖(e^{iθ_0Q̂_{W'}}-e^{iθ_0Q̂_{W}})Ω‖² ≥ 2(1-|tr(V_{θ_0}r)|²) > 0`:

the family is not Cauchy at `θ_0`.  Strong-resolvent convergence of
`Q̂_{W,c_0}` would force strong convergence of every `e^{iθQ̂_{W,c_0}}`;
contradiction.  (At `θ∈2πℤ` there is no obstruction — consistent with
⟨1⟩10.)  **⟨2⟩4. QED.**

*Remark (what is NOT claimed; memory-index-b-r1 objection 7).*  The
converse — for scalar `V_θ` on both tails the stabilised charges assemble
via a strongly continuous group and Stone's theorem into a self-adjoint
`Q̂` — is plausible (it is the charge shadow of A1(b)'s scalar branch) but
requires the group construction and is not proved here; it is subsumed in
the ⟨1⟩3b conjecture.  Numerical evidence for ⟨2⟩3: the lane-B critic's own
independent seeded `χ=2` contraction gives obstruction
`2(1-|tr(V_πr)|²)=1.9166>0` (memory-index-b-r1.md §7(b)).

*How the two mechanisms bound the retreat from opposite sides.*  Mechanism
A (⟨1⟩3): `log`-divergent window-charge variance, `χ=1`, `H=0`, disjoint
from every A2 folium — D17's mean control does not control fluctuations.
Mechanism B (here): boundary-law `O(1)` variance, exactly on the A2 folium
— even perfectly tame fluctuations obstruct strong operator convergence
whenever the virtual circle action is nonscalar.  Together they show the
operator form fails both off and on the folium; only the law-level
statements (⟨1⟩11) and the implementer-route conjecture (⟨1⟩3b) survive.

---

## 6. Landmine exhibits (permanent; binding register)

**L1 (two-time non-commutation).**  For `Q_-=|0⟩⟨0|`, `Q_+=|+⟩⟨+|` on
`ℂ²`, both spectra are `{0,1}⊂ℤ`, yet
`spec(Q_+-Q_-)={-1/√2,+1/√2}` — “difference of lattice-valued observables
is lattice-valued” is FALSE.  (Equivalently, for `Q=diag(0,1)` and a
rotated `Q(t)`, `spec(Q(0)-Q(t))={±|sin φ|}`; memory-index-r1.md V3.)  No
step of this shard forms such a difference: integrality enters only through
the two same-window spectral resolutions (⟨1⟩5.⟨2⟩3), and the naive
unmeasured mean difference deviates from the TPM mean by the generically
nonzero dephasing defect (checker mutation IDX-C2).

**L2 (marginal laws do not self-upgrade).**  (i) *Uniform-integrability
failure:* `μ_W=(1-1/W)δ_0+(1/(2W))δ_W+(1/(2W))δ_{-W}` has pointwise limit
`δ_0` and exact signed first moment `0`, yet
`Σ_{|ν|>R}|ν|μ_W(ν)≥1` for every `R` — one-point/D13 expectation
convergence can NEVER exclude this (memory-index-b-r1 objection 2).
(ii) *Mean escape:* `p_m=(1-1/m)δ_0+(1/m)δ_m` is tight with weak limit
`δ_0` but first moment `≡1↛0` (checker mutation IDX-C4).  These are why
D27(LR3) demands the `(1+|ν|)` weight, and why **no implication
H-AD-G ⟹ (LR) is claimed**: D18(AD3)'s frozen words fix no window-marginal
topology and supply no uniform integrability.  Any future bridge must add
the ⟨1⟩8 reading (or stronger) to D18 explicitly and prove (LR) from it;
until then the connection is open.

**L3 (register).**  `δx` is a mean and is never claimed quantized.
Quantization claims attach to (i) the TPM history law (⟨1⟩7) and (ii) the
direct channel law of `-2sΔX` under H-AD-G (§0 register paragraph) — never
to a two-time coupling: under (LR) alone, writing `δx=(1/2s)·E_γ[ν_+-ν_-]`
for a coupling `γ` of the two marginal laws is dynamics-free bookkeeping,
not an outcome law (memory-index-b-r1 objections 3--4).  This shard's
outcome statements are exclusively about the explicitly stated TPM protocol.

---

## 7. CHECKER SPEC (consolidated)

**Existing and PASSING — cite, do not duplicate.**
`theory/checks/memory_index_probe.py` (D16 XXZ at `Δ=2`; exact sector at
`N=22` validating the `≤5`-domain-wall space, then `N=37,50`; pre-registered
P1--P5, all PASS; `--red` capable).  Findings of record:
(i) *Integrality, as an arithmetic certificate* (P2; reworded per r2
objection 9): at every window and time, mass farther than `10^{-9}` from `ℤ`
is `≤10^{-11}` — but P2 certifies that `spec Q̂_W ⊂ ℤ` holds **by
construction of the observable** in the D16 instantiation (`site_sz` and
`rho_vac` are both exactly `±1/2`, so every eigenvalue is an exact IEEE
integer for any state, evolved or not).  It is an arithmetic certificate of
(G-IDX.0), **not** a dynamical one, and it says nothing about the law
(G-IDX.2).  The outcome-support finding — extra integer mass at
`Q_W∈{-1,-3}`, carried by near-threshold zero-velocity two-magnon channels
(the ⟨1⟩8 fence remark) — is **P3's** content, not P2's.  Its red
sensitivity is likewise arithmetic (`RED_RHO_SHIFT=0.3` on a 10-site window
is exactly `3.0`, so the three 10-site windows are silent under red); a red
shift coprime to the window widths is referred to the checker lane.  (ii) *Estimator independence* (P4; synthesis-notes item 2): `δx`
read from `{p_ν}` agrees with the independent gradient-centroid estimator
`X̂₁` to `<0.1` sites; `X̂₂=⟨Q_W⟩+const` is tautological and is not used as
validation.  (iii) *Numerics culture* (P1/P3; synthesis-notes item 3):
sharp-kink preparation fakes a `~5%` quantization violation (excitation
defect radiating near-threshold pairs); the dressed kink collapses it
`×22`.  Future memory numerics MUST use dressed kinks; `dwmax=3` is
spuriously perfect (cannot host kink dressing) and is banned as a control.
(iv) Tables are indexed by the convention-free `Q_W` value, support
`{0,-2}` — the §0 convention.

**IMPLEMENTED AND COMMITTED (`a529a10`, checker lane repair `6f746d5`):
`theory/checks/memory_index_check.py`.**
Deterministic certificates; every red mutation breaks a necessary premise
except IDX-C4 and IDX-C7(i)(b), whose mutations are an inserted false
assertion and a counterterm-arithmetic perturbation respectively (SPEC NOTES
6 and 1).
Run status of record (memory-index-r3.md §0 V3, `python3 -O`): green **exit
0**, IDX-C1--C8 all green as **ten registered rows**; `--red` **exit 1**,
`RED-OK`, **10 of 10** checks report "caught", each with its own diagnostic.
Companion probe: `memory_index_probe.py` green **exit 0**, `--red`
**exit 1** (190 pre-registered violations), `--selftest` **exit 0**.
*The three r2-objection-3 coverage defects are CLOSED at `6f746d5` and
re-verified by independent recomputation in memory-index-r3.md §0 V3: the
⟨1⟩9.⟨2⟩4 tail mutation is now the separately registered row IDX-C7(ii) with
a live red path; the IDX-ρ.6 assertion is non-vacuous as IDX-C8rho, guarded
by `require(out > 0)` and a printed VACUITY LEDGER; the SPEC NOTE count is
reconciled at seven with a COUNT ledger.  Carried forward, not a gate:
`memory_index_probe.py`'s `RED_RHO_SHIFT = 0.3` remains resonant with the
10-site windows (r3 NOTE 10; the checker's own shift was replaced by the
irrational `RED_SHIFT`, SPEC NOTE 7).  The specification below is the frozen
target; deviations are recorded in the file's own SPEC NOTES.*

1. **IDX-C1 (finite-window offset and TPM).**  `S^z=diag(-3/2,…,3/2)`,
   three-site window, two seeded Haar unitaries as Heisenberg times, seeded
   normalised vector.  Compute both spectral resolutions and the TPM law.
   Expected: normalisation residue `<10^{-12}`, all nonzero increments
   within `10^{-12}` of `ℤ`, (IDX.4) residue `<10^{-12}`.
2. **IDX-C2 (two-time red mutation).**  Replace the TPM mean by the naive
   unmeasured difference `⟨Q̂(t_-)⟩-⟨Q̂(t_+)⟩` with the same noncommuting
   unitaries.  Must fail at `>10^{-6}` (the dephasing defect; certifies
   that D27(LR2), not L1's false arithmetic, closes the two-time step).
3. **IDX-C3 (mechanism-A counterexample).**  For `N=2^j`, `j=4..16`:
   `V_N`, the IDX-CE.4 Fourier distribution, `r_N=Σ_kP(L_N=k)/(k-i)`.
   Expected: `V_N~log N`, `max_kP(L_N=k)√V_N` bounded, `|r_N|` decreasing.
   Mutation `ε_n→(n+1)^{-1}` must fail the registered `V_N→∞` test.
4. **IDX-C4 (weak-limit red mutation).**  Feed
   `p_m=(1-1/m)δ_0+(1/m)δ_m`: report tight weak convergence but REJECT
   first-moment convergence (D27(LR3) fails) — kills “tightness alone”.
5. **IDX-C5 (M-quant-G reduction).**  Symbolic `p_0=1-P, p_2=P`: mean
   `-P/s`, variance `P(1-P)/s²`.  Mutating the transmitted escaped charge
   `2→1` must fail both.
6. **IDX-C6 (slope = density; from lane B C-IDX-1).**  `χ=2`
   charge-diagonal injective families (spin-3/2, virtual charges `(0,1)`,
   target `ρ=1/2`; spin-2 companion, `ρ=1`), 50 seeded draws each,
   left-canonicalised, injectivity verified.  Expected:
   `|ω(S^z)-ρ|<10^{-12}` for EVERY draw (the parameter-independence that is
   M-IDX-density's content).  Mutation (must FAIL): move one tensor entry
   to a forbidden charge slot — covariance (a necessary premise) breaks and
   the measured density varies with the draw.
7. **IDX-C7 (exact conjugation and zero offset; from lane B C-IDX-0/2,
   repaired per objection 6).**  (a) Build the one-site twisted map of
   `e^{iθ(S^z-ρ)}` and compare with `L_{V_θ^{-1}}∘E∘L_{V_θ}` at 20 values
   of `θ`; residue `<10^{-13}`.  (b) Two-sided `α|β` D1(e′) contraction,
   windows `[-n,n]`, `n=2..12`, cuts `c∈{-2..2}`: `|φ_W(2π)-1|<10^{-12}`.
   Mutations (each must FAIL): counterterm shift `ρ→ρ+0.1`
   (`|φ_W(2π)-1|=Θ(1)`, drifting with `n`); tail-covariance-phase mutation
   — replace the `β` tensor by one whose tail density is `-ρ+0.2` (shifted
   virtual charge pattern), breaking the two-tail relation ⟨1⟩9.⟨2⟩4.
   *The lane-B one-sided-regularisation mutation and its parity claim are
   DELETED: after ⟨1⟩9 the one-sided charge differs from `Q̂_{W,c}` by the
   deterministic integer `2ρn_R`, so that mutation stays green
   (memory-index-b-r1 objection 6).*
8. **IDX-C8 (vacuum law and obstruction; from lane B C-IDX-3/4, repaired
   per objections 5 and 8).**  Vacuum intervals `|I|=2..40` with the
   TAIL-NORMAL-ORDERED `Q_I^α`: FFT of `φ_I` against the (IDX.5) limit
   `|tr(V_θr)|²`; expected `sup_θ|φ_I-G|≤Cλ̃^{|I|}` (fitted exponential),
   `|Σ_νμ_∞(ν)-1|<10^{-10}`, and the QUANTIFIED tightness bound of
   IDX-ρ.6 (not monotone tail decay, which was over-strong).  AKLT
   cross-check (D23): limit law `(1/4,1/2,1/4)` on `ν∈{-1,0,+1}`.
   Obstruction: `2(1-Re φ_I(π))` on growing deep-tail shells in the kink
   GNS contraction converges to `2(1-|tr(V_πr)|²)>0` for the charged
   `χ=2` families (certifies ⟨1⟩12.⟨2⟩3), and is `<10^{-12}` for a `χ=1`
   product comparator.  Mutation (must FAIL): replace `G` by
   `|tr V_θ|²/χ²` (wrong environment): sup-distance stalls at `Θ(1)`.

---

## 8. MERGE PROPOSALS

### 8.1 → `definitions.md` D26, D27 — APPLIED 2026-08-28 (commit `e0ce677`)

The proposed texts are **live and authoritative** at `definitions.md`
"Memory-index campaign — D26--D27" (D26: circle-integral on-site charge;
D27: charge-history local relaxation (LR), including the `δx` definition
clause).  Cite the live D-numbers; the former verbatim copy in this shard is
deleted per L4 (r2 objection 8) — a definition lives exactly once.  The r2
repair to D26's third sentence (`ρ=0` admitted; r2 objection 7) exists only
in `definitions.md`.

### 8.2 → `claims/CLAIMS.md` rows — APPLIED 2026-08-28 (commit `e0ce677`)

Live and authoritative rows: **M-INDEX-fin**, **M-INDEX-spec**,
**M-IDX-density**, **M-INDEX-LA-folium**, **M-INDEX-LA-strong** in
`claims/CLAIMS.md`.  The r2 repairs (edges, scoping, where-tested wording;
objections 4, 5, 9 and NOTES 10--12) exist only there.  Statuses shown in
`claims/CLAIMS.md` are the ones of record; this shard asserts none.

### 8.3 → `notation.md` rows — APPLIED 2026-08-28 (commit `e0ce677`)

Live and authoritative rows in `notation.md`: `Q̂_{W,c}`; `E_{W,t}`, `𝒟_{W,t}`;
`p_{W;t_-,t_+}`, `p_ν`, `ΔQ_W`; `ρ` (density); `Q_W^α`, `Q_W^β`, `μ_∞^α`;
`δx` (asymptotic).  The r2 fence on the `ρ` row and on the standing `s` row
(objection 1) exists only in `notation.md`.

---

## 9. HONEST STATUS

1. **Proved in this shard (pending r2):** unconditional finite-window coset
   integrality (⟨1⟩1); the exact TPM support and moment identity
   (⟨1⟩5--⟨1⟩6); the M-flux ledger by citation (⟨1⟩4); subsequence-free
   support quantization of the ordered TPM outcome law under D27's
   tightness-only (LR), with the value unique under the optional
   convenience clause (⟨1⟩7); exact reduction to M-quant-G under H-AD-G
   with the AD3 topology named and its two-step lemma displayed (⟨1⟩8);
   and, newly imported at certified strength: density quantization `2ρ∈ℤ`
   under (S)+(INT) (⟨1⟩9, unconditional, decircularized), the identically
   zero offset (⟨1⟩10), and the pure-tail vacuum charge laws (⟨1⟩11).
2. **Refuted:** the operator form of the requested L-A, by TWO mechanisms
   bounding the retreat from both sides: D17 fluctuation divergence off the
   folium (⟨1⟩3) and the nonscalar-`V_θ` obstruction on the folium (⟨1⟩12).  The fixed-A2-folium implementer theorem is proved in ⟨1⟩3b by the separate implementer route, so the REFUTED row remains restricted to the sector-wide/window-limit statement (L10).
3. **Assumed, not derived:** D27.  No implication H-AD-G ⟹ (LR) is claimed;
   the AD3-topology gap is named (⟨1⟩8 recital, landmine L2), and the μ_W
   exhibits show one-point convergence can never supply LR3.  (S) is
   assumed only where stated (⟨1⟩9--⟨1⟩12, (G-IDX.0-ρ)).
4. **Protocol scope:** the probability law is the explicitly stated TPM law.
   Without asymptotic commutativity there is no protocol-independent
   spectral law of `Q̂(+∞)-Q̂(-∞)`; no such operator is claimed, and no
   coupling of marginal laws is called an outcome (landmines L1, L3).
5. **Limit scope:** offsets cancel at fixed `W` before `W↑ℤ`; first-moment
   tightness, stronger than bare tightness, passes the expectation; support
   quantization needs only tightness (subsequential form).  D17's spatial
   first-moment clause does not supply this spectral uniform integrability.
6. **Not imported from lane B (deliberately, per its FAIL):** the coupling
   “outcome” language (objections 3--4); Lemma R / H-AD-G ⟹ (LR)
   (objection 2); the vacuum statement for the two-sided operator
   (objection 5, repaired to tail normal ordering); the one-sided checker
   mutation and parity claim (objection 6); the scalar-branch
   self-adjointness construction (objection 7); the general decorated
   middle-block contraction (objection 8, scoped to pure tails + deep
   shells).
7. **Forbidden inputs not used:** no integrability, model-specific
   scattering, channel completeness (except in the consistency corollary),
   soft interchange, or assumption `s∈(1/2)ℤ` (under (S) the density
   quantization is a conclusion).
8. **Status:** `claims/CLAIMS.md` is the status of record (L5); as this shard
   stands, M-INDEX-fin, M-INDEX-spec and M-IDX-density are **SKETCH**;
   M-INDEX-LA-folium is **PROVED** (implementer route, blitz-la-folium-r1); M-INDEX-LA-strong is **REFUTED**
   with both mechanisms recorded.  M-INDEX-full (deriving (LR)) was not
   obtained in either lane; the campaign's top rung remains open.  The r2
   verdict's four promotion decisions are the orchestrator's step after gate
   verification and are **not** applied in the lane-A repair pass (§10).

---

## 10. r2 repair response (lane A)

Work order: `theory/verdicts/memory-index-r2.md` (adjudicator verdict
**FAIL(1,2,3)**, 2026-08-28).  Lane A owns `definitions.md`, `notation.md`,
`claims/CLAIMS.md`, `theory/memory-index.md`, `theory/ansatz-scattering.md`.
`theory/checks/` belongs to the parallel checker lane and was not touched.
**No status promotion was applied** — that is the orchestrator's step after
gate verification (verdict §4).

| id | sev | disposition | exact edit location |
|---|---|---|---|
| 1 | MAJOR | **FIXED** (FIX DEMAND applied verbatim, three surfaces) | `notation.md` `ρ` (density) row — parenthesis replaced by the demanded sentence; `notation.md` `s` row (Corner B block) — same sentence as **Fence (r2 objection 1)**; `definitions.md` Corner B D13--D18 preamble (after "…`s = 1/2` in every concrete statement.") — same sentence as a *Fence* paragraph |
| 2 | MAJOR | **FIXED** | `claims/CLAIMS.md` **AC-EX** row, statement cell rewritten from the verdict §4 scoping sentence: `N_T^{ex}`, `H_out^{ex}` restored throughout; "for which Lane T1's outcome measure exists" restored; ACE.3 stated as conditional on **both** (AD3-ex) **and** the existence of Lane T1's ordered-limit measure; (D28-C) two-sidedness and its unverified status recorded.  Status left at **SKETCH** (AC-EX is HOLD); where-tested cell records the ACE-C1/ACE-C2 gate |
| 3 | MAJOR | **SKIPPED — checker lane** | `theory/checks/memory_index_check.py` (split `check_c7`, mutation-(ii) red branch, SPEC NOTE count, IDX-ρ.6 assertion, docstring `:21-22`).  Lane A recorded the open defect where a reader meets it: `claims/CLAIMS.md` M-IDX-density where-tested cell, and §7's checker preamble |
| 4 | MINOR | **FIXED** | ⟨1⟩11 ASSUME (states that no `s`/`s=ρ` enters); ⟨1⟩11.⟨2⟩3 (now cites ⟨1⟩9.⟨2⟩3 + ⟨1⟩1.⟨2⟩1 for `κ≡ρ (mod ℤ)`; the ⟨1⟩10 citation, which carried `s=ρ`, is dropped); ⟨1⟩12 ASSUME (gains **H-MQG(2)'s `s=ρ`**); ⟨1⟩12.⟨2⟩1 (displays `Q̂_{W'}-Q̂_W=Σ_{x∈I}S^z_x-sℓ` and names `s=ρ` as the reason it equals `Q_I^α`); `claims/CLAIMS.md` M-INDEX-LA-strong where-proved cell (mechanism B's extra hypotheses disclosed; mechanism A flagged as needing neither (S) nor `s=ρ`) |
| 5 | MINOR | **FIXED** | `claims/CLAIMS.md`: M-INDEX-spec depends-on `+ M-INDEX-fin`; AC-EX depends-on `+ M-INDEX-spec`; M-IDX-density depends-on `D1, D2(b,e), D26` → `D1, D2(a,b,e), D26`.  `theory/ansatz-scattering.md` ⟨1⟩7.⟨2⟩3 justification now cites row **M-INDEX-spec** instead of `briefs/memory-campaign-target.md`; §6 row 8 annotated |
| 6 | MINOR | **FIXED** | `claims/CLAIMS.md` **AD3-ex** row: the displayed limit `lim_{t→+∞}\|\|E_W({q_ch})Ψ_t-P_{ch}Ψ_t\|\|=0` quoted verbatim from ⟨1⟩7's ASSUME with the "before `W↑ℤ`" order; the ordered-limit gloss demoted to a parenthetical describing ACE-LD; last clause replaced by "no part of (AD3-ex) is proved; ⟨1⟩7.⟨2⟩2 derives the inter-channel cross-term vanishing FROM it…" |
| 7 | MINOR | **FIXED** | `definitions.md` D26, third sentence → "No **arithmetic** condition on the real tail-density parameter `ρ` is included (`ρ=0` is admitted — the AKLT cross-check at §7 IDX-C8; H-MQG(2)'s `s>0` is a separate hypothesis of the kink setting)".  The duplicate in this shard's §8.1 is gone (objection 8), so the live text is the only copy |
| 8 | MINOR (L4) | **FIXED** | This shard §8.1--§8.3 → pointers to live `definitions.md` D26/D27, the five live DAG rows, the six live notation rows (~78 lines removed).  `theory/ansatz-scattering.md` §5 → pointers to live D28/D28-C/D28-R, the AC-EX and AD3-ex rows, the nine notation rows (~100 lines removed).  Prefixes dropped: `D28-P` → `D28` (48 occurrences) in the T2 proof text and header; "proposed D26/D27" → live D-numbers in §0 and ⟨1⟩9's remark |
| 9 | MINOR | **FIXED** (document half; one suggestion referred) | §7 "Findings of record (i)" reworded to the demanded text — P2 is an **arithmetic** certificate of (G-IDX.0) true by construction of the observable, not a dynamical one, and the `Q_W∈{-1,-3}` finding is **P3's**; `claims/CLAIMS.md` M-INDEX-fin where-tested cell amended to match.  *Referred to the checker lane:* "consider a red shift coprime to the window widths" (`memory_index_probe.py`) |
| N10 | NOTE | **FIXED** | `claims/CLAIMS.md` M-IDX-density: LSM sentence gains "— for an antisymmetric tail pair; one tail alone gives only `ρ∈κ+ℤ`, and a general pair only `ρ_α-ρ_β∈ℤ`." |
| N11 | NOTE | **FIXED** | ⟨1⟩3b gains "Where the content sits" (existence is the whole content; the scalar clause is a Schur one-liner once the implementer exists); same in `claims/CLAIMS.md` M-INDEX-LA-folium |
| N12 | NOTE | **FIXED** | §7 heading "To implement after merge" → "IMPLEMENTED AND COMMITTED (`a529a10`)" with the run status of record (green exit 0; `--red` exit 1, RED-OK 8/8; probe `--red` exit 1, `--selftest` exit 0); "proposed" dropped from the where-tested cells of M-INDEX-fin, M-INDEX-spec, M-IDX-density, M-INDEX-LA-strong |
| N13 | NOTE | **FIXED** | `theory/ansatz-scattering.md` §6 "No silent strengthening" ledger gains clause **(vi)**: D28(1)'s `HΩ_γ=0`, labelled a normalisation consequence of H-MQG(3), not a new assumption |
| N14 | NOTE | **FIXED** | ⟨1⟩8.⟨2⟩2(i) re-indexed: `E_W({q_*})` on the running `Ψ_t`, with the identity written `1-⟨Ψ_t,E_W({q_*})Ψ_t⟩=1-⟨Ψ,E_{W,t}({q_*})Ψ⟩`, plus a stated indexing convention; (ii) made consistent |

**L2.** Per verdict §3 the splits are post-promotion hygiene.  The two
pre-promotion carve-outs are done here: objection 8's pointerization (above),
and no status change in this commit.  The L2-correct cut for this shard when it
is taken remains §5 (⟨1⟩9--⟨1⟩12) → `theory/memory-index-density.md`.
