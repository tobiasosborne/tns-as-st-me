<!-- ============================================================
     SUPERSEDED (2026-08-28, T1 round-2 synthesis).
     This lane-B shard FAILED its r1 critique:
     theory/verdicts/memory-index-b-r1.md — FAIL(1,2,3,4,5,6).
     Its surviving content was merged, at the critic's
     surviving-weaker-statement strength only, into the canonical shard
       theory/memory-index.md  (§5 there: ⟨1⟩9 M-IDX-density decircularized,
       ⟨1⟩10 zero offset, ⟨1⟩11 tail-normal-ordered vacuum laws,
       ⟨1⟩12 nonscalar-V_θ obstruction, nonexistence direction only),
     per briefs/t1-synthesis.md and briefs/synthesis-notes.md.
     Do NOT cite this file as a proof source; it is retained verbatim below
     as the historical lane-B record.  Its merge proposals are superseded by
     theory/memory-index.md §8.  Relevant verdicts:
       theory/verdicts/memory-index-b-r1.md (this shard, FAIL),
       theory/verdicts/memory-index-r1.md (baseline shard, PASS).
     ============================================================ -->

<!-- ROLE: independent proposer proof shard for Theorem M-INDEX, Lane T1,
     attempt B (Fable lane, briefs/t1-fable-prover.md).  Deliberately written
     without reading theory/memory-index.md (decorrelation).  The claim enters
     at SKETCH and awaits the cross-family L6 critic.  Structure follows
     CLAUDE.md L6b.  New hypotheses appear only as proposed D26/D27 in the
     MERGE PROPOSALS section (§5); no shared file is edited. -->

# M-INDEX (lane B) — memory quantization from superselection and charge-lattice rigidity

## 0. Status, rung, and what is claimed

**Proposer status: SKETCH** (L5; only the L6 loop promotes).

Rung on the fallback ladder of `briefs/memory-campaign-target.md`:
**M-INDEX-spec** (quantization under an explicit local-relaxation hypothesis
(LR)), *plus* an unconditional integrality core that is **stronger than the
template in one direction and weaker in another**:

* Stronger: under (INT) the charge-lattice offset is not merely constant —
  it is **zero for every window and every cut** (⟨1⟩3), because (INT) together
  with covariance on the two tails forces `e^{2πis}=c_{2π}` on the `α` tail
  and `e^{-2πis}=c_{2π}` on the `β` tail, hence **`2s ∈ ℕ`** (⟨1⟩2).  The
  memory quantum `1/(2s)` is itself quantized: `1/(2s) ∈ {1, 1/2, 1/3, …}`.
  This is derived, not assumed; no step below inputs `s ∈ ½ℤ`.
* Weaker: the template's G-IDX.0 — "the regularized total charge `Q̂` exists
  as a self-adjoint operator in the GNS representation" — is **false as
  stated** whenever the selected circle acts with nonscalar `V_θ` on the
  virtual space (⟨1⟩5; the same scalar/nonscalar dichotomy as claim A1(b)).
  The surviving — and for quantization fully sufficient — form is
  convergence **in law** with tightness (⟨1⟩4), plus the exact finite-window
  scalar identity `e^{2πiQ̌_W} = 𝟙` (⟨1⟩3).

Index philosophy (not a ported theorem): the "2π-flux acts trivially ⟹
integrality" mechanism of refs/arxiv-1810.07351/Index_Re.tex (abstract; §1.1;
the paragraph before §2 beginning "A computation … at flux φ=2π … the phase
factor χ(2π) has to be equal to 1.  This establishes integrality of the
index"), and its Example (Lieb–Schultz–Mattis: index = charge density for a
translation-invariant system).  Their setting is a gapped ground state and an
invariant unitary; nothing from that paper is used as a lemma here — every
step below is re-derived in the MPS register from D1–D2 and Lemma IT.

## 1. Hypotheses

**Standing (cited, never redefined — L4).**  H-MQG(1)–(4) of
`theory/memory-quantization-general.md` §0, verbatim: covariant injective MPS
vacuum family (D1, D2(a)); fixed pair `β = g·α ≠ α` with kink sector
`𝒦_{αβ}` from A2(a,c,d,f); common unbroken circle direction `ξ ∈ 𝔥_α ∩ 𝔥_β`
with Hermitian on-site charge `S^z := -i q(ξ)` and vacuum densities
`ω_α(S^z) = +s`, `ω_β(S^z) = -s`, `s > 0`; finite-range `G`-invariant `H`
with stationary vacua (D10, G0(e)); the selected packet `ϱ ∈ 𝒦^{(1)}_{αβ}`
(D17) with wall coordinate `𝔛_W` (D13(a)).  **H-MQG(5) = H-AD-G is NOT
assumed** except in ⟨1⟩8.  Smoothness (S) of D2(e) is assumed at `α` and `β`
for the selected circle direction and is stated at every step that uses it.
Limit order is always D18(AD4)'s: infinite-volume dynamics first, then
`t → ±∞` at fixed window, then `W ↑ ℤ`.

**New hypotheses (proposed numbered definitions; exact merge text in §5).**

**(INT) [proposed D26].**  The on-site representation of the selected circle
is integral up to a phase: there is `c_{2π} ∈ U(1)` with

  `e^{2πi S^z_x} = c_{2π}·𝟙_x`  on every site `x`.   (I.1)

Equivalently `spec(S^z) ⊂ γ_0 + ℤ` for some `γ_0 ∈ ℝ` with
`e^{2πiγ_0} = c_{2π}`.  True for every spin-`S` chain (`c_{2π} = e^{2πiS}`).
(INT) fixes the normalization of `ξ`; it is the only integrality input.

**(LR) [proposed D27].**  For the selected packet, its infinite-volume
evolution `ϱ_t`, windows `W = [a,b]` with a fixed cut `c ∈ W`, and the
regularized window charge

  `Q̌_W := Σ_{x=a}^{c}(S^z_x - s) + Σ_{x=c+1}^{b}(S^z_x + s) = 2s(𝔛_W - c)`  (I.2)

(the identity is (G.3), `memory-quantization-general.md` ⟨1⟩2, an
unconditional finite computation), write `μ_{W,t}` for the spectral law of
`Q̌_W` in `ϱ_t` — by ⟨1⟩3 below a probability measure on ℤ.  Clauses:

* **(LR1) settling.**  For each sufficiently large `W`, `μ_{W,t} → μ_{W,±}`
  weakly as `t → ±∞`.  *Cesàro variant admitted:* the time averages
  `T^{-1}∫_0^{T} μ_{W,±t}\,dt` converge along one common sequence
  `T_n ↑ ∞` for all `W`; every conclusion below then holds for the
  subsequential asymptotic values.
* **(LR2) uniform charge tightness.**
  `lim_{R→∞} sup_W Σ_{|ν|>R}(1+|ν|)\,μ_{W,±}(ν) = 0`.
* **(LR3) no boundary accumulation.**  `μ_{W,±}(ν)` converges for every
  `ν ∈ ℤ` as `W ↑ ℤ` (cut `c` fixed); with (LR2) the limits `μ_±` are then
  probability measures with convergent first moments
  `m_± = Σ_ν ν μ_±(ν) = lim_W m_{W,±}`.
* **(LR4) flux integrability (ledger only).**  For each edge bond of each
  sufficiently large `W`, `t ↦ ϱ_t(j_{edge})` is Lebesgue-integrable on ℝ.

*Weakest-form remark.*  At fixed `W` the law `μ_{W,t}` lives on a fixed
finite subset of ℤ (⟨1⟩3 plus `‖Q̌_W‖ < ∞`), so Cesàro subsequential limits
satisfying (LR1) exist **unconditionally** by compactness and a diagonal
extraction over the countable window family.  The honest minimal hypothesis
is therefore (LR2)+(LR3) along that extraction; (LR1) as plain limits is the
physically expected upgrade.  Formulating (LR) this way is deliberate: the
theorem quantizes *every* subsequential asymptotic memory value.

## 2. THEOREM M-INDEX

**ASSUME.**  H-MQG(1)–(4), (S) at `α` and `β` for the selected circle, (INT).
For (IDX.2): additionally (LR1)–(LR3).  For the asymptotic ledger in (IDX.1):
additionally (LR4).  For (IDX.3): additionally H-AD-G = H-MQG(5).

**PROVE.**

**(IDX.0a) Density quantization.**  `e^{2πis} = c_{2π} = e^{-2πis}`, hence
`c_{2π}^2 = 1`, `c_{2π} = ±1`, and `2s ∈ ℕ`.  In particular `s ∈ ℤ` iff
`c_{2π} = +1` and `s ∈ ℤ + ½` iff `c_{2π} = -1`.

**(IDX.0b) Exact finite-window integrality; zero offset.**  For every finite
window `W` and every cut `c ∈ W`,

  `e^{2πi Q̌_W} = 𝟙`  exactly, in `𝔄_W`;   (I.3)

hence in every state and every representation `spec(Q̌_W) ⊆ ℤ` (pure point:
`𝔄_W` is finite-dimensional) and `spec(𝔛_W) ⊆ (1/2s)ℤ`.  No dynamical,
spectral, or asymptotic hypothesis enters.

**(IDX.0c) Sector charge laws (the surviving GNS statement).**  For the
vacua `ω_α, ω_β` and for every two-sided decorated kink reference state
`ϱ_0 = ω_{α|β}^{(m)}[T]` (D1(e′)) with finitely many modifications, the
window-charge characteristic functions converge **uniformly in `θ`**, with
rate `λ̃^{min(n_L,n_R)}` in the two tail margins, to a continuous limit;
consequently the laws `μ_W` converge weakly to a probability measure on ℤ
and the family `{μ_W}` is tight.  For the pure vacuum the limit law is exact:

  `μ_∞^{α}(ν) = (2π)^{-1}∫_{-π}^{π} e^{-iθν}\,|tr(V_θ\,r)|^2\,dθ`,   (I.4)

with `V_θ := V_α(exp(θξ))`.

**(IDX.0-op) Dichotomy (refutation of the templated operator form).**  In
the GNS representation of `ϱ_0`: if `V_θ` is scalar for every `θ` (on both
tails), the unitaries `e^{iθQ̌_W}` stabilize exactly on the dense decorated
domain and a self-adjoint `Q̂` exists with `Q̂Ψ = Q̌_WΨ` for all large `W`.
If `V_{θ_0}` is nonscalar for some `θ_0` on either tail, then
`{e^{iθ_0 Q̌_W}}_W` is **not** Cauchy on the GNS vector, and no self-adjoint
`Q̂` with `e^{iθQ̂} = s\text{-}lim\,e^{iθQ̌_W}` exists.  The obstruction is
the nondegenerate limiting vacuum charge law (I.4).  This is the charge-law
shadow of claim A1(b) (strings implemented by no strongly convergent
sequence iff `V` nonscalar).

**(IDX.1) Ledger.**  Finite-time: exactly claim M-flux (PROVED; cited, not
reproved).  Asymptotic, under (LR4): with the escaped charge defined
flux-wise,

  `ΔQ_esc(W) := ∫_ℝ dt\,[ϱ_t(j_{b|b+1}) - ϱ_t(j_{a-1|a})]`,
  `2s·δx_W^∞ = -ΔQ_esc(W)`,  and  `2s·δx = -ΔQ_esc := lim_W ΔQ_esc(W)`.  (I.5)

**(IDX.2) Quantization.**  Under (LR1)–(LR3): `μ_±` are probability measures
on ℤ; the asymptotic memory exists and equals

  `δx = (1/2s)(m_+ - m_-)`;   (I.6)

for **every** coupling `γ` of `(μ_-, μ_+)` one has
`δx = (1/2s)\,E_γ[ν_+ - ν_-]` with integrand in ℤ pointwise; with the
canonical independent coupling, `p_ν := (μ_+ ⋆ μ̌_-)(ν)` (the law of the
difference of independent draws) and the escape-signed `p̃_ν := p_{-ν}`,

  `δx = (1/2s)Σ_ν ν\,p_ν = -(1/2s)Σ_ν ν\,p̃_ν`,  `ν ∈ ℤ`.   (I.7)

**Every asymptotic memory outcome is an integer multiple of `1/(2s)`**, and
by (IDX.0a) `1/(2s) ∈ {1, 1/2, 1/3, …}`.  `δx` itself is only the
`{p_ν}`-average and is **not** claimed quantized.  Bound states, absorption,
extra channels are all allowed: they redistribute `{p_ν}` within ℤ.

**(IDX.3) Reduction.**  Under additionally H-AD-G: (a) the selected vector
satisfies (LR1)–(LR3) (Lemma R, ⟨1⟩8 — the weakest step of this shard);
(b) the scattering coupling furnished by `W_±` has difference law supported
on `{0, 2}` (escape-signed) with `p̃_2 = ⟨N_T⟩`, `p̃_0 = 1 - ⟨N_T⟩`; and
(c) (I.7) becomes `δx = -⟨N_T⟩/s`, i.e. exactly M-quant-G (G.1), with
(G.2) verbatim.  No mismatch.

## 3. Proof

Throughout, `E_α` is the transfer map of `A_α` in canonical form (`l = 𝟙`,
`r > 0`, D1(c)); `L_M(Y) := MY`; `V_θ := V_α(exp(θξ))`, and on the `β` tail
`V'_θ := V_β(exp(θξ))`; `u(θ) := u(exp(θξ)) = e^{iθS^z}` on one site.
`q̌_x := S^z_x - s` for `x ≤ c` and `S^z_x + s` for `x > c` (the regularized
density of (I.2)).

### ⟨1⟩1. NC-1: the IT phase slope is the charge density

**ASSUME.** H-MQG(1)–(2), (S) at `α`.

**PROVE.** `θ'_α(ξ) = ω_α(S^z) = s`, and the one-site twisted transfer map
obeys `E_{u(θ)} = e^{iθ_α(θ)}\,L_{V_θ^{-1}} ∘ E_α ∘ L_{V_θ}` where
`θ_α(θ) := θ_α(exp(θξ))`.

**⟨2⟩1.**  For every `θ`, `Σ_{s'}u(θ)_{ss'}A_α^{s'} =
e^{iθ_α(θ)}V_θ^{-1}A_α^{s}V_θ`.
*Justification.*  D2(b) (IT) at the group element `exp(θξ) ∈ H_α`
(the circle is unbroken, H-MQG(2)).

**⟨2⟩2.**  Hence for the generalized transfer map
`E_{u(θ)}(Y) := Σ_{s,s'} u(θ)_{ss'} A^{s'} Y (A^{s})^†`:
`E_{u(θ)}(Y) = e^{iθ_α(θ)} Σ_s V_θ^{-1}A^sV_θ\,Y\,(A^s)^† =
e^{iθ_α(θ)}\,V_θ^{-1}E_α(V_θ Y)`.
*Justification.*  ⟨2⟩1 and D1(b),(d).

**⟨2⟩3.**  `ω_α(u_x(θ)) = e^{iθ_α(θ)}\,tr[V_θ^{-1}E_α(V_θ r)]`.
*Justification.*  ⟨2⟩2 with left environment `l = 𝟙` and right environment
`r` (D1(c),(d)).

**⟨2⟩4.**  Differentiating ⟨2⟩3 at `θ = 0` (legitimate by (S): `V_θ` is `C¹`
near `0` with `V_0 = 𝟙`, `dV_θ/dθ|_0 = X_α(ξ) =: X`):
`d/dθ\,ω_α(u_x(θ))|_0 = iθ'_α(ξ) - tr[X E_α(r)] + tr[E_α(X r)]
= iθ'_α(ξ) - tr[Xr] + tr[Xr] = iθ'_α(ξ)`,
using `E_α(r) = r` and `tr[E_α(Y)] = tr[Y·E_α^*(𝟙)] = tr[Y]`
(left-canonical, `E_α^*(𝟙) = 𝟙`).
*Justification.*  D1(c), D2(e).

**⟨2⟩5.**  Also `d/dθ\,ω_α(u_x(θ))|_0 = ω_α(iS^z) = is`.  Comparing with
⟨2⟩4: `θ'_α(ξ) = s`.
*Justification.*  H-MQG(2) (`ω_α(S^z) = +s`) and norm-differentiability of
the on-site exponential.  **⟨2⟩6. QED.**

*(The same computation at `β` with `ω_β(S^z) = -s` gives `θ'_β(ξ) = -s`.)*

### ⟨1⟩2. L-A′: density quantization (IDX.0a)

**ASSUME.** H-MQG(1)–(2), (S) at `α` and `β`, (INT).

**PROVE.** `θ_α(θ) = sθ mod 2π` for all `θ ∈ ℝ`; `e^{2πis} = c_{2π}`;
`e^{-2πis} = c_{2π}`; hence `c_{2π}^2 = 1` and `2s ∈ ℕ`.

**⟨2⟩1.**  `f(θ) := θ_α(exp(θξ))` is additive mod `2π`:
`f(θ + θ') = f(θ) + f(θ') mod 2π`.
*Justification.*  Lemma IT (corner-a.md ⟨1⟩2(i)) with `g, h` in the circle,
`g·α = α` (unbroken, H-MQG(2)); `exp(θξ)exp(θ'ξ) = exp((θ+θ')ξ)` in the
one-parameter subgroup; `θ_α(g)` is unique for each `g` (D2(b)), so `f` is a
well-defined function of `θ`.

**⟨2⟩2.**  `f(θ) = sθ mod 2π` for all `θ`.
*Justification.*  By (S), `f` is `C¹` near `0` with `f(0) = 0`; choose the
continuous lift `f̃` there.  The additivity defect
`f̃(θ+θ') - f̃(θ) - f̃(θ')` is a continuous `2πℤ`-valued function of
`(θ,θ')` near `(0,0)` vanishing at the origin, hence `≡ 0`; Cauchy's
functional equation with continuity gives `f̃(θ) = f̃'(0)θ = sθ` near `0`
(⟨1⟩1.⟨2⟩5), and `f(nθ) = n f(θ) mod 2π` (⟨2⟩1, induction) extends the
identity to all `θ ∈ ℝ`.  Named computation **NC-2**.

**⟨2⟩3.**  At `θ = 2π`, (INT) gives `u(2π) = c_{2π}𝟙`, so (IT) reads
`c_{2π}A_α^s = e^{if(2π)}V_{2π}^{-1}A_α^sV_{2π}`.  By the uniqueness clause
of D2(b) (refs/arxiv-2011.12127, Eq. (eq:XAX=B):
`X^{-1}A^iX = e^{iχ}Y^{-1}A^iY ⟹ χ = 0 ∧ X ∈ e^{iφ}Y`, applied with
`Y = 𝟙`), `V_{2π}` is scalar and `e^{if(2π)} = c_{2π}`.  With ⟨2⟩2:
`e^{2πis} = c_{2π}`.
*Justification.*  (INT), D2(b), ⟨2⟩2.

**⟨2⟩4.**  The same argument at `β` (density `-s`, ⟨1⟩1 remark) gives
`e^{-2πis} = c_{2π}`.
*Justification.*  H-MQG(2) (the circle lies in `H_β` and the SAME on-site
`u`, hence the same `c_{2π}`, acts on every site), (S) at `β`, (INT).

**⟨2⟩5.**  Dividing: `e^{4πis} = 1`, so `2s ∈ ℤ`; `s > 0` gives `2s ∈ ℕ`;
`c_{2π} = e^{2πis} ∈ {±1}` with the stated parity.
*Justification.*  ⟨2⟩3–⟨2⟩4.  **⟨2⟩6. QED.**

*Remark (sanity, and why injectivity is load-bearing).*  A `χ = 2` spin-1
tensor with virtual `U(1)` charges `(0,1)` and would-be density `s = 1`
forces the entry pattern `A^{+1}` diagonal, `A^{0}` strictly lower
triangular, whose transfer fixed point cannot be positive definite: the
would-be counterexample to "slope = density" is never an injective D1
tensor.  This is checker computation C-IDX-1's red family (§6).

### ⟨1⟩3. L-A: exact finite-window integrality and zero offset (IDX.0b)

**ASSUME.** (INT); for the final cancellation also ⟨1⟩2.

**PROVE.** (I.3), and the offset bookkeeping in public.

**⟨2⟩1.**  All the `S^z_x` commute, so from (I.2),
`e^{2πiQ̌_W} = [∏_{x∈W}e^{2πiS^z_x}]·e^{2πi[-s(c-a+1)+s(b-c)]}
= c_{2π}^{\,|W|}\,e^{2πis(a+b-1-2c)}·𝟙 =: z_W·𝟙`.
*Justification.*  (INT) sitewise; finite scalar algebra.  **Under (INT)
alone** the spectrum of `Q̌_W` lies in `q_W + ℤ` with
`e^{2πiq_W} = z_W` — a lattice whose offset drifts with `a, b, c`.  This is
the smearing landmine, displayed rather than hidden.

**⟨2⟩2.**  Substituting `c_{2π} = e^{2πis}` (⟨1⟩2.⟨2⟩3):
`z_W = e^{2πis[(b-a+1)+(a+b-1-2c)]} = e^{4πis(b-c)}`.
The drift now depends only on the cut-to-edge distance.
*Justification.*  ⟨2⟩1, ⟨1⟩2.⟨2⟩3.

**⟨2⟩3.**  Substituting `e^{4πis} = 1` (⟨1⟩2.⟨2⟩5) and `b - c ∈ ℤ`:
`z_W = 1`.  Hence (I.3); `spec(Q̌_W) ⊆ ℤ` pure point in the
finite-dimensional `𝔄_W`; and by (I.2), `spec(𝔛_W) ⊆ c + (1/2s)ℤ =
(1/2s)ℤ` (as `2sc ∈ ℤ`).
*Justification.*  ⟨2⟩2, ⟨1⟩2.⟨2⟩5, (I.2).  **⟨2⟩4. QED.**

*The two-sided calibration of D13(a) is exactly what kills the offset: the
`-s` and `+s` counterterms on the two sides of the cut conspire with
`c_{2π}^{|W|}` so that `z_W = 1` for every `W` and every `c`.  A one-sided
regularization (`-s` throughout) leaves `z_W = (c_{2π}e^{-2πis})^{|W|}·(…) `
which under ⟨1⟩2 equals `e^{-4πis·\#\{x>c\}}` — for `2s` odd this
alternates with the window parity.  Checker mutation C-IDX-2-red.*

### ⟨1⟩4. L-B: sector charge laws converge with tightness (IDX.0c)

**ASSUME.** H-MQG(1)–(2), (S), (INT); the reference state
`ϱ_0 = ω_{α|β}^{(m)}[T]` of D1(e′) with junction `m`, modifications in a
fixed finite set, cut `c` fixed.

**PROVE.** Uniform convergence of characteristic functions; weak convergence
to a probability law on ℤ; tightness; and (I.4) for the pure vacuum.

**⟨2⟩1.**  (Exact conjugation of the normal-ordered twisted string.)  On an
`α`-tail site, the one-site map of `e^{iθ(S^z-s)}` is
`e^{-iθs}E_{u(θ)} = e^{i(θ_α(θ)-sθ)}L_{V_θ^{-1}}∘E_α∘L_{V_θ}
= L_{V_θ^{-1}}∘E_α∘L_{V_θ}` — the phase cancels **exactly**, for all `θ`,
by `θ_α(θ) = sθ` (⟨1⟩2.⟨2⟩2).  On a `β`-tail site the same holds with
`V'_θ` and `θ_β(θ) = -sθ`.  Composing a pure stretch of `n` sites:
`L_{V_θ^{-1}}∘E_α^{\,n}∘L_{V_θ}` — a single conjugated transfer power.
Named computation **NC-3**.
*Justification.*  ⟨1⟩1.⟨2⟩2, ⟨1⟩2.⟨2⟩2, D2(d).

**⟨2⟩2.**  For `W = [a,b]` containing the junction, all modifications, and
the cut, with tail margins `n_L, n_R` between `∂W` and the finite middle
block: the characteristic function
`φ_W(θ) := ϱ_0(∏_{x∈W}e^{iθq̌_x})` equals, by D1(e′)'s consistent window
contraction,
`φ_W(θ) = N^{-1}\,tr[\,l_α\,(V_θ^{-1}E_α^{\,n_L}(V_θ\,·\,))\,
M_θ\,(V'^{-1}_θ E_β^{\,n_R}(V'_θ\,r_β))\,]`
(schematically; `N` is the same contraction at `θ = 0`), where the middle
block `M_θ` collects the finitely many modified sites, the junction, and the
`|c - m|` mismatch sites where the counterterm label differs from the tensor
label — each of the latter contributing an exact scalar `e^{∓2iθs}` times
the pure conjugated map (⟨2⟩1).  `θ ↦ M_θ` is norm-continuous and
`2π`-periodic-bounded on `[-π, π]`.
*Justification.*  D1(e′) (well-definedness lemma), ⟨2⟩1; (I.3) gives exact
`2π`-periodicity of `φ_W`.

**⟨2⟩3.**  As `n_L, n_R → ∞`: `E_α^{n} = P_α + O(λ̃^{n})`,
`E_β^{n} = P_β + O(λ̃^{n})` (D1(c), any `λ̃ ∈ (max λ_E, 1)`), and all the
maps `L_{V_θ}` have norm `1` (unitarity), so
`sup_{θ∈[-π,π]}|φ_W(θ) - G(θ)| ≤ C\,λ̃^{min(n_L,n_R)}`,
with `G` continuous, `G(0) = 1` (the denominator converges to a positive
constant by D1(e′) nondegeneracy).
*Justification.*  D1(c), ⟨2⟩2; uniformity in `θ` because every θ-dependent
factor is uniformly bounded on the compact `[-π,π]`.

**⟨2⟩4.**  (Elementary Lévy step, self-contained.)  For a probability law
`μ` on ℤ with characteristic function `φ`, and `0 < u ≤ π`:
`u^{-1}∫_{-u}^{u}(1 - \mathrm{Re}\,φ(θ))\,dθ =
Σ_ν μ(ν)\,2(1 - \mathrm{sinc}(uν)) ≥ Σ_{|ν| ≥ 2/u}\,μ(ν)`,
since `sinc(x) := sin(x)/x ≤ 1/|x| ≤ 1/2` for `|x| ≥ 2`.  Named computation
**NC-4** (truncation inequality; two lines, no external citation).
Applying it with ⟨2⟩3: given `ε`, pick `u` with
`u^{-1}∫_{-u}^{u}(1-\mathrm{Re}\,G) < ε/2` (continuity of `G` at `0`,
`G(0)=1`), then `μ_W(|ν| ≥ 2/u) < ε` for all large `W`: **tightness**.
Fourier inversion on ℤ (`μ_W(ν) = (2π)^{-1}∫_{-π}^{π}e^{-iθν}φ_W(θ)dθ`)
plus uniform convergence gives `μ_W(ν) → g_ν ≥ 0` for every `ν`, and
tightness gives `Σ_ν g_ν = 1`: weak convergence to a probability law on ℤ.
*Justification.*  ⟨2⟩3, NC-4, (I.3) (support in ℤ).

**⟨2⟩5.**  Pure vacuum specialization: no middle block; `l_α = 𝟙`;
`E_α^{n}(V_θ r) → tr(V_θ r)\,r`; hence
`φ_I(θ) → tr(V_θ r)\,tr(V_θ^{-1} r) = |tr(V_θ r)|^2`
(`V_θ^{-1} = V_θ^†`, `r = r^† > 0`), which is (I.4).  Note
`[V_θ, r] = 0` by Lemma IT (corner-a.md ⟨1⟩2(iv)).
*Justification.*  ⟨2⟩3 with `M_θ` empty, D1(c).  **⟨2⟩6. QED.**

*(First moments: for `ϱ_0` the means `m_W = ϱ_0(Q̌_W)` converge as `W ↑ ℤ`
by the exponential D9(a) factorization rate of decorated states,
corner-a-kinks.md ⟨1⟩8(iii); for general `𝒦^{(1)}` states by the D17 `ℓ¹`
clause.  Tightness of the general D17 window laws is NOT claimed — that is
exactly what (LR2) hypothesizes for the evolved packet.)*

### ⟨1⟩5. The operator form of G-IDX.0: dichotomy and refutation (IDX.0-op)

**ASSUME.** As ⟨1⟩4; GNS representation `(H, π, Ω)` of `ϱ_0`.

**PROVE.** (IDX.0-op).

**⟨2⟩1.**  `Q̌_{W'} - Q̌_W = Q̌_{shell}` with commuting summands, so for any
unit vector `Ψ`:
`‖(e^{iθQ̌_{W'}} - e^{iθQ̌_W})Ψ‖^2 = 2 - 2\,\mathrm{Re}\,⟨Ψ,
e^{-iθQ̌_{shell}}Ψ⟩`.
*Justification.*  On-site charges commute; unitarity.  Named computation
**NC-5a**.

**⟨2⟩2.**  (Nonscalar case.)  Take `Ψ = Ω` and grow `W'` by an interval `I`
of length `ℓ` deep in the (say) `α` tail.  By ⟨1⟩4.⟨2⟩3 (window = `I`, no
middle block, both margins large),
`⟨Ω, e^{-iθQ̌_I}Ω⟩ → |tr(V_θ r_α)|^2` as `ℓ` and the distances diverge.
For `r > 0`, `tr\,r = 1`, unitary `V`: `|tr(V r)| =
|tr(r^{1/2}Vr^{1/2})| ≤ 1` with equality **iff** `V ∈ U(1)𝟙`
(Cauchy–Schwarz with strict positivity; named computation **NC-5b**).  So if
`V_{θ_0}` is nonscalar, the right side of ⟨2⟩1 has liminf
`≥ 2(1 - |tr(V_{θ_0}r)|^2) > 0`: the family is not Cauchy at `θ_0`, and no
strong limit of `e^{iθ_0Q̌_W}` exists.  Since strong-resolvent convergence
of `Q̌_W` would force strong convergence of every `e^{iθQ̌_W}`, no
self-adjoint `Q̂` arises as the naive limit.  (At `θ ∈ 2πℤ` there is no
obstruction: `e^{2πiQ̌_W} = 𝟙` identically, (I.3) — consistent with
`spec ⊆ ℤ` in law.)
*Justification.*  ⟨2⟩1, ⟨1⟩4.⟨2⟩3,⟨2⟩5, NC-5b.

**⟨2⟩3.**  (Scalar case.)  If `V_θ` and `V'_θ` are scalar for all `θ`, then
by ⟨1⟩4.⟨2⟩1 the twisted one-site map on every pure tail stretch equals the
untwisted `E` exactly, so for `Ψ = π(B)Ω` (`B` local) and any two windows
containing `supp B`, the modifications, junction, and cut:
`⟨Ψ, e^{-iθQ̌_{shell}}Ψ⟩ = ⟨Ψ, Ψ⟩` exactly, i.e. the left side of ⟨2⟩1 is
`0`: the unitaries **stabilize exactly** on the dense decorated domain.
Define `Q̂Ψ := Q̌_{W_0(Ψ)}Ψ`; consistency and self-adjointness on this
domain are immediate, and `e^{2πiQ̂} = 𝟙`.
*Justification.*  ⟨1⟩4.⟨2⟩1, ⟨2⟩1.  This is the charge analogue of A1(b)'s
"for scalar `V_α(g)` the strings stabilise exactly".  **⟨2⟩4. QED.**

*Consequence for the campaign: quantization must not be routed through a
total-charge operator.  Everything below uses only finite-window laws and
their weak limits — which ⟨1⟩3–⟨1⟩4 control completely.*

### ⟨1⟩6. G-IDX.1: the ledger (IDX.1)

**ASSUME.** H-MQG(1)–(4); (LR4) for the asymptotic form.

**PROVE.** (I.5).

**⟨2⟩1.**  Finite-time: for all finite `t_i < t_f`,
`ϱ_{t_f}(𝔛_W) - ϱ_{t_i}(𝔛_W) = (1/2s)∫_{t_i}^{t_f}dt\,
[ϱ_t(j_{a-1|a}) - ϱ_t(j_{b|b+1})]`.
*Justification.*  Active claim **M-flux** (PROVED), verbatim; the Hermitian
current convention is H-MQG(2)'s fixed `-i` as in
memory-quantization-general.md ⟨1⟩3.⟨2⟩2.  Not reproved.

**⟨2⟩2.**  Under (LR4) both time limits of the integral exist absolutely;
subtracting and rearranging gives the first identity of (I.5) with
`ΔQ_esc(W)` as displayed — the net signed charge that left `W` through its
two edges over the whole event (D10(a)'s sign: `j_{m|m+1} > 0` is rightward
flow).
*Justification.*  ⟨2⟩1, dominated convergence, D10(a).

**⟨2⟩3.**  If also (LR1)–(LR3) hold, then `δx_W^∞ = (1/2s)(m_{W,+} -
m_{W,-})` (the spectral computation of the same two expectations), so the
flux and spectral readings of the ledger agree at every `W`, and `W ↑ ℤ`
gives the second identity of (I.5) with `ΔQ_esc = -(m_+ - m_-)`.
*Justification.*  (I.2) (cut `c` cancels in the difference of expectations),
(LR1)–(LR4).  **⟨2⟩4. QED.**

### ⟨1⟩7. G-IDX.2: quantization under (LR) (IDX.2)

**ASSUME.** H-MQG(1)–(4), (S), (INT), (LR1)–(LR3).

**PROVE.** (I.6), (I.7), and the outcome-spectrum statement.

**⟨2⟩1.**  For each large `W`, `μ_{W,±}` exist and are probability measures
supported on the finite set `spec(Q̌_W) ⊆ ℤ`; all moments converge under
(LR1) since the support is finite at fixed `W`.
*Justification.*  (LR1), ⟨1⟩3, finite-dimensionality of `𝔄_W`.

**⟨2⟩2.**  As `W ↑ ℤ` (cut fixed): `μ_{W,±} → μ_±` weakly with
`μ_±(ℤ) = 1` and `m_{W,±} → m_± = Σ_ν ν μ_±(ν)`.  ℤ is closed, so no
smearing off the lattice is possible; (LR2)'s `(1+|ν|)` weight prevents both
mass and first-moment escape.
*Justification.*  (LR2), (LR3).  *(This is where the weak-limit landmine is
disposed of: the offset is identically `0` for every `W` by ⟨1⟩3 — there is
no `W`-dependent lattice to drift — and tightness pins the mass.)*

**⟨2⟩3.**  The asymptotic memory exists and equals (I.6):
`δx = lim_W (1/2s)[m_{W,+} - m_{W,-}] = (1/2s)(m_+ - m_-)`, in the AD4
order (dynamics, then `t`, then `W`).
*Justification.*  D13(a), (I.2), ⟨2⟩1–⟨2⟩2.

**⟨2⟩4.**  (Couplings; the two-time bookkeeping in public.)
`Q̌_W(t_f)` and `Q̌_W(t_i)` are noncommuting Heisenberg observables; no
spectral difference of them is formed anywhere in this proof.  Instead: for
ANY probability coupling `γ` on `ℤ × ℤ` with marginals `(μ_-, μ_+)`,
`E_γ[ν_+ - ν_-] = m_+ - m_-` (linearity of expectations of marginals), and
the integrand `ν_+ - ν_-` takes values in ℤ pointwise.  The canonical
independent coupling defines `p_ν` and `p̃_ν = p_{-ν}` and yields (I.7).
The theorem asserts: the outcome spectrum of every such asymptotic
bookkeeping is `(1/2s)ℤ`; the selection of a *physical* coupling is
additional dynamical information (supplied under H-AD-G in ⟨1⟩8, by channel
projections — commuting, hence an honest joint law).  No claim is made that
repeated two-time measurements sample `{p_ν}` absent such a decomposition;
that overclaim is the REFUTED Conjecture M's graveyard and is not entered.
*Justification.*  ⟨2⟩2–⟨2⟩3; elementary measure theory on ℤ².

**⟨2⟩5.**  `1/(2s) ∈ {1, 1/2, 1/3, …}` by ⟨1⟩2.⟨2⟩5.  Extra channels, bound
states, or absorption change `μ_±` — never the support lattice, which is
fixed by ⟨1⟩3 alone.
*Justification.*  ⟨1⟩2, ⟨1⟩3.  **⟨2⟩6. QED.**

### ⟨1⟩8. G-IDX.3: reduction to M-quant-G under H-AD-G (IDX.3)

**ASSUME.** H-MQG(1)–(5) (i.e. also H-AD-G = D18(AD1–AD4) with
`q_in = q_L = -1`, `q_T = +1`).

**PROVE.** (IDX.3)(a)–(c).

**⟨2⟩1.**  (Lemma R: H-AD-G ⟹ (LR1)–(LR3) for the selected vector.
**Weakest step; proof at sketch granularity within this SKETCH shard.**)
(LR1): AD3 states that for every fixed window containing the kink, the free
leg charge and non-bound dressing leave the window as `t → ±∞` and the
remaining local state is a kink charge eigenstate — so the window law of
`Q̌_W` settles to the (channel-mixed) kink-position charge law; AD4 fixes
the order.  (LR3): AD3's final clause — the increasing-window limit of
D13(a) exists on the limit state — is window consistency.  (LR2): the out
state is `W_+(φ_R, φ_T)` with two normalizable channel legs (AD1–AD2); the
kink-position marginal of each channel is a fixed normalizable packet
distribution, so its window charge laws are tight with uniformly integrable
first moments (D17 first-moment clause for the packet class).  *If the
critic reads AD3 more weakly than "the window marginal converges with its
first moment", the missing content must be added to H-AD-G explicitly;
(IDX.3)(b)–(c) below are unaffected, since they cite M-quant-G wholesale.*
*Justification.*  D18(AD1–AD4), D17, H-MQG(4).

**⟨2⟩2.**  On `ℋ_sc`, `ΔX = -(1/s)N_T` with `N_T = W_+P_TW_+^*` an
orthogonal projection.  The channel decomposition provides the physical
coupling of ⟨1⟩7.⟨2⟩4: the joint outcome law of (incoming, outgoing) wall
charge conditioned on channel.  The law of `-2s·ΔX = 2N_T` is
`{0 \text{ w.p. } 1-⟨N_T⟩;\ 2 \text{ w.p. } ⟨N_T⟩}`; i.e. the escape-signed
difference law is `p̃_0 = 1 - ⟨N_T⟩`, `p̃_2 = ⟨N_T⟩`, supported on `{0,2}`.
*Justification.*  Active claim **M-quant-G** ⟨1⟩4–⟨1⟩5 (PROVED conditional
on H-AD-G, per mquant-g-r2.md), D18(AD2).

**⟨2⟩3.**  Then (I.7) gives `δx = -(1/2s)(0·p̃_0 + 2·p̃_2) = -⟨N_T⟩/s`,
which is (G.1); the spectrum `{0, -1/s}` and Bernoulli variance are (G.2)
verbatim.  Consistency check passed: no constant, sign, or convention
mismatch between the index formulation and the converged M-quant-G row.
For the XXZ instantiation (`s = 1/2`): `p̃` on `{0,2}`, `δx = -2⟨N_T⟩` —
the frozen M-quant numbers (memory-quantization.md (Mq.2), (Mq.8)).
*Justification.*  ⟨1⟩7.⟨2⟩4, ⟨2⟩2, M-quant-G (G.1)–(G.2).
**⟨2⟩4. QED.** □

## 4. The two named landmines, addressed

**Two-time non-commutation.**  No difference of the noncommuting
`Q̌_W(t_f), Q̌_W(t_i)` is ever formed.  The proof subtracts *expectations*
of one fixed observable at two times (⟨1⟩6, M-flux), and represents the
asymptotic difference of *means* through couplings of the two marginal laws
(⟨1⟩7.⟨2⟩4).  "Difference of lattice-valued observables is lattice-valued"
is neither used nor true; what is proved is: both marginals live on the SAME
offset-free lattice ℤ (⟨1⟩3), so every coupling's difference variable is
ℤ-valued pointwise.  A physical joint law exists only where dynamics
supplies commuting channel projections (⟨1⟩8.⟨2⟩2).

**Weak-limit smearing / offset drift.**  The offset is computed in public in
⟨1⟩3: under (INT) alone it drifts as `c_{2π}^{|W|}e^{2πis(a+b-1-2c)}`; the
two-sided D13(a) calibration reduces it to `e^{4πis(b-c)}`; the two-tail
covariance (⟨1⟩2, `e^{4πis} = 1`) kills it identically.  Weak limits then
stay on ℤ because ℤ is closed and (LR2) forbids mass escape; the D17
first-moment clause enters only for convergence of means.  The checker
mutation (§6, C-IDX-2-red) reproduces the drift when the calibration is
broken, so the cancellation is machine-falsifiable.

**("What does the wall charge at `t = +∞` mean before channels exist?")**
Nothing: only the iterated limits of finite-window laws are used, in the
AD4 order, everywhere.  `μ_±` are constructed objects; no `t = ∞` observable
exists in this shard (and ⟨1⟩5 shows even the `W ↑ ℤ` charge operator does
not exist in general).

## 5. MERGE PROPOSALS (exact text; no shared file edited here)

**(i) definitions.md — append after D25:**

> ## D26 (integrality of the selected circle)
>
> In the setting of H-MQG(2) (`theory/memory-quantization-general.md` §0),
> the on-site representation of the selected circle `{exp(θξ)}` is integral
> up to a phase: there is `c_{2π} ∈ U(1)` with `e^{2πiS^z_x} = c_{2π}𝟙_x`
> on every site; equivalently `spec(S^z) ⊂ γ_0 + ℤ`,
> `e^{2πiγ_0} = c_{2π}`.  (True for every spin-`S` chain, with
> `c_{2π} = e^{2πiS}`.)  D26 fixes the normalization of `ξ` and is the only
> integrality input of Theorem M-INDEX; under D26, (S), and H-MQG(2), the
> vacuum density satisfies `e^{2πis} = c_{2π} = e^{-2πis}`, hence
> `2s ∈ ℕ` (claim M-IDX-density) — a conclusion, not a hypothesis.
>
> ## D27 (local relaxation (LR) for the selected kink packet)
>
> [Insert clauses (LR1)–(LR4) verbatim from theory/memory-index-b.md §1,
> including the Cesàro variant and the weakest-form remark.]

**(ii) claims/CLAIMS.md — new rows (all SKETCH until the L6 loop):**

> | M-IDX-density | Under H-MQG(1–2), (S) at both tails, and D26: `θ_α(exp(θξ)) = sθ`, `e^{2πis} = c_{2π} = e^{-2πis}`, hence `2s ∈ ℕ` and `c_{2π} = ±1`.  Density quantization is derived, not assumed. | SKETCH | D1, D2(b,c,e), D26, A2(a) | theory/memory-index-b.md ⟨1⟩1–⟨1⟩2 | checker spec C-IDX-1 |
> | M-IDX-int | Unconditional finite-window integrality: `e^{2πiQ̌_W} = 𝟙` exactly for every window and cut, so `spec(Q̌_W) ⊆ ℤ` and `spec(𝔛_W) ⊆ (1/2s)ℤ` in every state; the lattice offset is identically zero (no `W`-drift). | SKETCH | D13(a), D26, M-IDX-density | theory/memory-index-b.md ⟨1⟩3 | checker spec C-IDX-2 |
> | M-IDX-law | Sector charge laws: for vacua and D1(e′) kink cores the window-charge characteristic functions converge uniformly (rate `λ̃^{margin}`) to a continuous limit; the laws converge weakly to probability measures on ℤ and are tight; vacuum limit law `= |tr(V_θ r)|²`-transform.  The naive total-charge operator exists iff `V_θ` is scalar for all `θ` (dichotomy, sibling of A1(b)); the templated operator form of G-IDX.0 is REFUTED for nonscalar `V_θ`. | SKETCH | D1(c,e′), D2(b,e), D26, M-IDX-density, M-IDX-int, A1(b) | theory/memory-index-b.md ⟨1⟩4–⟨1⟩5 | checker spec C-IDX-3, C-IDX-4 |
> | M-INDEX | Memory quantization as superselection bookkeeping: under H-MQG(1–4), (S), D26, D27(LR1–LR3): the asymptotic wall-charge laws `μ_±` are probability measures on ℤ, `δx = (1/2s)(m_+ − m_-)`, every coupling outcome is in `(1/2s)ℤ` with `2s ∈ ℕ`, and `δx = −(1/2s)Σν p̃_ν`.  Ledger: finite-time = M-flux; asymptotic under D27(LR4).  Under additionally H-AD-G, `p̃` is `{1−⟨N_T⟩, ⟨N_T⟩}` on `{0,2}` and the theorem reduces exactly to M-quant-G (G.1)–(G.2).  `δx` itself is NOT quantized; scattering theory is needed only for the VALUE. | SKETCH | M-IDX-density, M-IDX-int, M-IDX-law, M-flux, M-quant-G, D13(a), D17, D26, D27 | theory/memory-index-b.md ⟨1⟩6–⟨1⟩8 | checker spec §6 |

**(iii) notation.md — new rows:**

> | `c_{2π}` | on-site circle scalar `e^{2πiS^z} = c_{2π}𝟙` (D26); equals `e^{2πis} = ±1` under M-IDX-density | definitions.md D26 (proposed) |
> | `Q̌_W`, `q̌_x` | regularized window charge `2s(𝔛_W − c)` and its density (`S^z_x ∓ s` across the cut) | theory/memory-index-b.md (I.2) |
> | `μ_{W,t}`, `μ_±`, `m_±` | spectral law of `Q̌_W` in `ϱ_t`; its iterated asymptotic limits; their means | theory/memory-index-b.md §1–§3 |
> | `p_ν`, `p̃_ν` | canonical (independent-coupling) two-time difference law and its escape-signed reflection | theory/memory-index-b.md (I.7) |
> | `ΔQ_esc(W)` | flux-defined escaped charge `∫dt[ϱ_t(j_{b\|b+1}) − ϱ_t(j_{a−1\|a})]` | theory/memory-index-b.md (I.5) |

## 6. CHECKER SPEC (machine-checkable certificates; file to be created as `theory/checks/memory_index_b_check.py`)

Model family: `χ = 2` charge-diagonal injective tensors.  Spin-3/2
(`S^z = diag(3/2,1/2,-1/2,-3/2)`), virtual charges `v = (0,1)`, density
target `s = 1/2`: free complex entries at `(m; i,j) ∈
{(1/2;1,1), (1/2;2,2), (3/2;1,2), (-1/2;2,1)}` (pattern `m = s + v_j − v_i`).
Spin-2 companion with `s = 1`: entries at `{(1;1,1), (1;2,2), (2;1,2),
(0;2,1)}`.  Draw entries from a fixed-seed complex Gaussian; left-canonicalize;
verify injectivity (simple top transfer eigenvalue, `r > 0`, length-2 word
rank 4).  The `β` tensor is the spin-flipped partner (density `−s`).

* **C-IDX-0 (exact conjugation, NC-3).**  Build the one-site twisted map
  `𝔼_θ` of `e^{iθ(S^z−s)}` directly and compare with
  `L_{V_θ^{-1}}∘E∘L_{V_θ}`, `V_θ = e^{iθ\,diag(v)}·(\text{phase fixing})`,
  at 20 values of `θ`.  Expected: residue `< 10^{-13}`.
* **C-IDX-1 (slope = density).**  Compute `ω(S^z) = tr[E_{S^z}(r)]` for 50
  random draws of each family.  Expected: `|ω(S^z) − s| < 10^{-12}` for
  EVERY draw — the density is parameter-independent, the striking content of
  M-IDX-density.  **Mutation (must FAIL):** move one tensor entry to a
  forbidden charge slot (e.g. give `(1/2;1,2)` a nonzero value in the
  spin-3/2 family): covariance breaks and the measured density varies with
  the draw.
* **C-IDX-2 (zero offset).**  Two-sided `α|β` contraction (D1(e′)), junction
  `m = 0`, windows `[−n, n]`, `n = 2..12`, cuts `c ∈ {−2,…,2}`: compute
  `φ_W(2π)` by the transfer contraction.  Expected: `|φ_W(2π) − 1| <
  10^{-12}` for all `n, c`.  **Mutation C-IDX-2-red (must FAIL):** replace
  the counterterm `s` by `s + 0.1`, or use the one-sided regularization
  (`−s` on both tails): `|φ_W(2π) − 1|` is `Θ(1)` and drifts with `n`
  (the smearing landmine, made executable).
* **C-IDX-3 (law convergence and tightness).**  Vacuum windows
  `|I| = 2..40`: compute `μ_I(ν)` by FFT of `φ_I` on a `θ`-grid; compare
  with the (I.4) limit `G(θ) = |tr(V_θ r)|²`.  Expected:
  `sup_θ|φ_I − G| ≤ Cλ̃^{|I|}` (fit the measured exponential),
  `|Σ_ν μ_∞(ν) − 1| < 10^{-10}`, and monotone-decaying tails at fixed `R`.
  Cross-check on AKLT (D23 tensor, `V_θ = e^{iθσ^z/2}` up to phase,
  `r = 𝟙/2`): limit law `(1/4, 1/2, 1/4)` on `ν ∈ {−1, 0, +1}`.
  **Mutation (must FAIL):** replace `G` by `|tr V_θ|²/χ²` (wrong
  environment): the sup-distance stalls at `Θ(1)`.
* **C-IDX-4 (operator-form obstruction).**  Compute
  `2(1 − \mathrm{Re}\,φ_I(π))` for growing tail shells `I` in the kink GNS
  contraction.  Expected: convergence to `2(1 − |tr(V_π r)|²) > 0` for the
  charged `χ = 2` families (numerical lower bound recorded), certifying
  ⟨1⟩5.⟨2⟩2; and `< 10^{-12}` identically for a `χ = 1` product comparator
  (XXZ vacua), certifying the scalar branch ⟨1⟩5.⟨2⟩3.

*Pre-verification record (proposer-side, scratch implementation, seed 7;
the committed checker must reproduce these independently).*  Spin-3/2 family:
left-canonical residue `4.4·10^{-16}`, length-2 word rank `4`, measured
density `0.500000000000`; spin-2 family: density `1.000000000000` — the
parameter-independent density of C-IDX-1, for random draws.  NC-3 conjugation
residue `3.7·10^{-15}` over `θ ∈ [0.1, 6.2]`.  Zero offset:
`|φ_W(2π) − 1| ≤ 8·10^{-16}` over `n ∈ {3,6,9}`, `c ∈ {−2,0,2}` — and this
held **even before canonicalization**, as (I.3) predicts (unconditional, no
canonical form used).  Mutation `s → s+0.1`: `|φ_W(2π) − 1| = 0.618` (FAIL
as required).  Vacuum law: `φ_I(π) = 0.13878563 = |tr(V_π r)|²` to 8 digits
at `|I| = 30`; limit-law Fourier coefficients match (I.4) to 6 digits
(`μ(0) = 0.5694`, `μ(±1) = 0.2153`, `μ(±2) < 10^{-6}` for the spin-3/2
draw).  Obstruction: `2(1 − \mathrm{Re}\,φ_I(π)) → 1.722 > 0` stably.

## 7. HONEST STATUS

**Proved (pending L6 critique), rung M-INDEX-spec plus core:**
(IDX.0a) density quantization `2s ∈ ℕ` — new, unconditional under
(INT)+(S), derived not assumed; (IDX.0b) exact zero-offset integrality at
every finite window — unconditional; (IDX.0c) sector charge laws converge
with tightness on the reference folium — unconditional; (IDX.1) ledger,
finite-time by citation of M-flux, asymptotic under (LR4); (IDX.2)
quantization of the outcome spectrum under explicit (LR1)–(LR3), with `δx`
only a `{p_ν}`-average; (IDX.3) exact reduction to M-quant-G under H-AD-G.

**Refuted (within this shard, with a checker certificate):** the templated
operator form of G-IDX.0 — the regularized total charge exists as a
self-adjoint GNS operator only in the scalar-`V_θ` (e.g. `χ = 1`) case;
in general only the laws converge.  Sharp dichotomy, sibling of A1(b).

**Assumed:** (INT) = proposed D26 (mild: every spin-`S` chain); (LR) =
proposed D27 (the genuine dynamical input: settling, uniform tightness,
window consistency, flux integrability — each clause used exactly once and
named at its point of use); (S) of D2(e) at both tails; H-AD-G only inside
(IDX.3).

**Weakest steps, in order:** (1) ⟨1⟩8.⟨2⟩1 (Lemma R: H-AD-G ⟹ (LR)) —
depends on reading D18(AD3) as window-marginal convergence with first
moments; the fallback is stated inline (add the clause to H-AD-G; the
reduction arithmetic is unaffected).  (2) ⟨1⟩4.⟨2⟩2 — the D1(e′)
middle-block bookkeeping is schematic in one display; the checker C-IDX-2/3
computations are the certificate that the contraction order and mismatch
scalars are right.  (3) (LR3) is close in strength to asserting window
consistency of the limit laws; I could not derive it from (LR1)–(LR2) and
believe it is genuinely independent (charge parked exactly on `∂W` for all
late times is not excluded by tightness).

**What did NOT land (campaign honesty):** M-INDEX-full — deriving (LR) from
clustering/decoherence — was not attempted beyond Lemma R; the campaign's
top rung remains open.  Landing (IDX.0)–(IDX.2) is strictly more than the
nearly-free M-INDEX-exp rung (the ledger), because the integrality core,
the zero-offset cancellation, the tightness lemma, and the operator-form
refutation are all new relative to M-flux/M-quant-G.

**Not claimed:** no soft theorem, no Adler zero, no value of `⟨N_T⟩`, no
`s ∈ ½ℤ` assumption (it is a conclusion), no torsor/deformation invariant,
no measurement-theoretic sampling statement for `{p_ν}` absent H-AD-G, no
statement at `k = 0` (the packet is fixed; D17 discipline), no claim that
`𝒦^{(1)}` states beyond the reference folium have tight window laws
(that is exactly (LR2)).
