<!-- ROLE: T2 proposer shard for AC-EX.  Only a critic-fixed L6 loop may
     promote the claim.  New definitions are merge proposals, not live D-numbers. -->

# AC-EX — fixed-packet kink--magnon wave operators from exact ansatz bands

**Proposer status:** **SKETCH**.  This is an existence and isometry theorem on
specified packet domains.  It proves neither asymptotic completeness nor that
an arbitrary incoming vector has an expansion in the constructed outgoing
channels.  Proposed definition D28 is reproduced verbatim in **MERGE
PROPOSALS** and is cited below as `D28-P`.

## 0. Theorem

### THEOREM AC-EX

**ASSUME.** H-MQG(1)--(3) from `memory-quantization-general.md`, proposed
`D28-P (H-ACE)`, and the charge assignment `q_in=q_L=-1`, `q_T=+1` when
ACE.3 is invoked.

**PROVE.**  On the fixed packet domains of D28-P:

1. **(ACE.1)** the Cook limits `W_-^L`, `W_+^L`, and `W_+^T` exist;
2. **(ACE.2)** `W_-^L` and `W_+:=W_+^L\oplus W_+^T` are isometries, and
   `N_T^{ex}:=W_+P_TW_+^*` is an orthogonal projection on the constructed
   out-space `H_out^{ex}:=ran W_+` (D18's `N_T`, restricted to this range);
3. **(ACE.3)** for a normalized event vector in
   `ran W_-^L\cap H_out^{ex}` for which Lane T1's outcome measure exists,
   the constructed-channel part of that measure is

   `p_ν^{ex}=||P_LW_+^*Ψ||² δ_{ν,0}+||P_TW_+^*Ψ||² δ_{ν,2}`,

   so `p_2^{ex}=⟨Ψ,N_T^{ex}Ψ⟩` and the T1 ledger gives
   `δx_ex=-p_2^{ex}/s`.

Infinite-volume dynamics is formed first, then the wave-operator time limit;
any T1 fixed-window limit follows that, and `W↑ℤ` is last (D17--D18 order).
No statement is made at `k=0` or after a packet-soft limit.

---

## 1. Translation and reference-use audit

### ⟨1⟩1. The kink sector has the fibering needed by the proof

**ASSUME.** D28-P(1)--(3).

**PROVE.** Momentum, group velocity, and energy transfer used below are
defined without a translation-invariant kink state.

**⟨2⟩1.** Translation invariance of the finite-range interaction gives
`τ_tτ_n=τ_nτ_t` on `𝔄`; the Lieb--Robinson estimate and almost locality are
therefore representation independent.

*Justification.* D10(a), finite-range dynamics, and
`refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`, equations
`(exchange-property)`, `(LRB)` and Theorem `smearing-theorem`.

**⟨2⟩2.** D9/A2 only fix state-sector labels; they do not furnish a cyclic
translation-fixed vector.  D28-P(1) separately assumes a covariant positive
energy representation `(H_{αβ},π_{αβ},U_{αβ})`.  SNAG applied to the commuting
unitaries `U_{αβ}(t,n)` gives the direct-integral momentum fibers.

*Justification.* D9(a), claim A2, D28-P(1), and the SNAG computation in
`refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`, equation `(SNAG)`.

**⟨2⟩3.** In those fibers the exact kink map obeys
`H_{αβ}Γ_Kf=Γ_K(E_Kf)` and `U_{αβ}(0,n)Γ_Kf=Γ_K(e^{-ipn}f)`; hence the kink
momentum is the momentum of the sector translation, not the phase-ambiguous
label of a bare mixed-uMPS formula.

*Justification.* D28-P(2).  The phase ambiguity being removed is recorded in
`refs/arxiv-1810.07006/p5_excitations.tex`, subsection “Topological
excitations”, after equation `(eq:kink)`.

**⟨2⟩4.** The excitation papers supply a finite-dimensional generalized
eigenproblem and kink/magnon candidates, but not exact spectral subspaces.
The word **EXACT** in D28-P(2)--(3) is therefore a hypothesis, including zero
ansatz variance and the distributional eigen-equations.

*Justification.* D5; `refs/arxiv-1103.2286/dispersionrelation_final.tex`, the
Rayleigh--Ritz paragraph after the two quadratic forms; and
`refs/arxiv-1810.07006/p5_excitations.tex`, equations `(eq:kink)`, `(eig)` and
the warning after `(eq:quasi_inveff)` that continuum eigenvectors need not be
well approximated.

**⟨2⟩5. QED.**

### ⟨1⟩2. Exact inventory of vacuum translation invariance in the source

**ASSUME.** The construction in `refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`.

**PROVE.** Every vacuum-dependent ingredient used or deliberately omitted
here has an explicit replacement.

**⟨2⟩1.** Source Lemma `lem:FT` uses invariance of the ground state to obtain
`U(t,n)Ω=Ω`; source Lemma `HR-auxiliary(a)` then uses that equality and the
mass-shell spectral integral to prove `B_t^*(g_t)Ω` is time independent.
D28-P(1)--(3) replace these two steps by the covariant sector representation
and the exact fiber equations of ⟨1⟩1.⟨2⟩3.

*Justification.* Source Lemmas `lem:FT`, `HR-auxiliary(a)`, equation
`(creation-on-vacuum)`, D28-P(1)--(3), and ⟨1⟩1.

**⟨2⟩2.** Source Theorem `Haag-Ruelle` uses `HR-auxiliary(a)` once more: the
time derivative of a one-particle creator annihilates `Ω`, after which it is
commuted to the right.  In the kink sector there is no such `Ω`.  Step
⟨1⟩5 instead computes `H I_c-I_cH_{0,c}` and cancels it with the two exact
one-body equations.

*Justification.* Source Theorem `Haag-Ruelle`, its first proof paragraph;
D28-P(2)--(3); and named computation **ACE-Cook** in ⟨1⟩5.

**⟨2⟩3.** Source Lemma `clustering-lemma` and Theorem `Haag-Ruelle-Fock` use
the unique invariant vacuum, vacuum clustering, and `BΩ=0` to factor scalar
products.  Step ⟨1⟩6 replaces this by the two-sided MPS transfer factorization
of D28-P(6); no vacuum Fock formula is imported.

*Justification.* Source Theorem `clustering`, Lemma `clustering-lemma`,
Theorem `Haag-Ruelle-Fock`, D1(c,e′), and named computation **ACE-Gram** in
⟨1⟩6.

**⟨2⟩4.** Source Lemmas `single-particle-density`,
`Lebesgue-absolute-continuity`, `single-particle-density-two`, and Theorem
`s-matrix` use cyclicity/invariance to extend the construction to a full Fock
space.  They are not ported; consequently AC-EX makes no density or
completeness claim.

*Justification.* The four cited source results and the theorem statement.
Source Theorem `harmonic-theorem` explicitly survives in any positive-energy
covariant representation, but its Fock-space application is not needed here.

**⟨2⟩5. QED.**

---

## 2. The three estimates

### ⟨1⟩3. Lieb--Robinson gives the required almost-local creators

**ASSUME.** D28-P(1),(3),(6).

**PROVE.** The filtered magnon creators and their one-body defects are almost
local, uniformly under lattice translation.

**⟨2⟩1.** For local `A` and `r>v_LR|t|`, finite-range Lieb--Robinson gives a
conditional-expectation approximant `A_{t,r}` supported in the `r`-fattening
of `supp A`, with `||τ_t(A)-A_{t,r}||≤Ce^{-μ(r-v_LR|t|)}`.

*Justification.* Named computation **ACE-LR**, obtained by applying the
finite-range `(LRB)` to observables outside the fattened support and then the
conditional-expectation argument of source Proposition `cor:localization`.

**⟨2⟩2.** If `F(t,n)` is Schwartz and its Fourier support isolates the selected
magnon shell, split the smearing into `|t|+|n|≤R` and its complement.  Apply
⟨2⟩1 with fattening `R` to the first part and Schwartz decay to the second;
the error is `O(R^{-N})` for every `N`.

*Justification.* **ACE-LR**, source Lemma `almost-locality`, and D28-P(3).

**⟨2⟩3.** Thus `a_{γ,b}(n)=τ_n(τ_F(A_{γ,b}))` is almost local.  Since the band
dispersion is smooth on the selected support, its Fourier hopping kernel is
rapidly decreasing; therefore

`D_{γ,b}(n):=[H,a_{γ,b}(n)]-Σ_{m,b'}h_{γ,bb'}(m-n)a_{γ,b'}(m)`

is almost local and satisfies `D_{γ,b}(n)Ω_γ=0`.

*Justification.* D10(a), D28-P(3),(4), Fourier integration by parts, and the
exact magnon equation `HΓ_{M,γ}=Γ_{M,γ}ω` from D28-P(3).

**⟨2⟩4. QED.**

### ⟨1⟩4. Fixed packets separate in velocity

**ASSUME.** D28-P(4).

**PROVE.** The real-space packet outside its velocity cone has summable decay
strong enough for Cook's method.

**⟨2⟩1.** For
`f_t(x)=∫(dp/2π)e^{i(px-tE(p))}f(p)`, choose a cone containing
`E'(supp f)`.  Outside it, `|x/t-E'(p)|≥ε_v`; repeated integration by parts
with `(it(x/t-E'(p)))^{-1}∂_p` gives pointwise `C_N⟨|x|+|t|⟩^{-N}`.

*Justification.* Named computation **ACE-SP**; D28-P(4) supplies smoothness,
compact support and the positive separation denominator.  This rederives the
one-dimensional case of source Proposition `norm-corollary`.

**⟨2⟩2.** Summing first over `|x|≤C|t|` and then over its complement yields
`||1_{outside}f_t||_1=O(|t|^{1-N})`, whereas
`||f_t||_1=O(1+|t|)`.

*Justification.* **ACE-SP** and the convergent sum
`Σ_{|x|>C|t|}⟨x⟩^{-N}=O(|t|^{1-N})`.

**⟨2⟩3.** If `dist(V_K,V_M)=ε_v>0`, the main cones obey
`|x-y|≥ε_v|t|/2` for large `|t|`; the sign conditions in D28-P(4) put the
magnon on the left for `t→-∞`, and on the declared left/right side for
`t→+∞`.

*Justification.* D28-P(4) and elementary cone geometry.

**⟨2⟩4. QED.**

### ⟨1⟩5. The cluster defect is Cook integrable

**ASSUME.** D28-P and ⟨1⟩3--⟨1⟩4.

**PROVE.** `∫_{|t|≥1}||(H I_c-I_cH_{0,c})e^{-itH_{0,c}}F||dt<∞` for each
allowed packet and channel end.

**⟨2⟩1.** With kink Wannier vectors `κ_a(x):=Γ_Kδ_{x,a}`, define

`I_cF:=Σ_{x,y,a,b}θ_c(y-x)F^{ab}(x,y)a_{c,b}(y)κ_a(x)`,

where `θ_L=1` far to the left and `θ_T=1` far to the right.  This is the
kink--magnon precursor identification.

*Justification.* D28-P(2)--(4),(6); absolute convergence holds on the
Schwartz packet core, and the limiting isometry (not `I_c` itself) extends by
⟨1⟩6.

**⟨2⟩2.** Without `θ_c`, the exact kink equation cancels the kink part of
`H_{0,c}`, and the exact magnon equation leaves precisely
`D_{c,b}(y)κ_a(x)`.

*Justification.* Direct commutator calculation
`H aκ=aHκ+[H,a]κ`, D28-P(2)--(3), and ⟨1⟩3.⟨2⟩3.  This is named computation
**ACE-Cook**.

**⟨2⟩3.** For `y` on the `γ` tail of `κ_a(x)`, truncate `D_{γ,b}(y)` and the
kink core at radius `|x-y|/3`.  Its squared norm is a two-sided MPS
contraction.  The leading transfer projection is
`||D_{γ,b}(y)Ω_γ||²=0`; D1(c)'s remainder and the truncation errors give, for
every `N`, `||D_{γ,b}(y)κ_a(x)||≤C_N⟨x-y⟩^{-N}`.

*Justification.* ⟨1⟩3, D1(c,e′), D28-P(6), and the transfer decomposition
`E_γ^r=P_γ+O(λ̃^r)` for every `λ̃∈(λ_{E_γ},1)`.  This is named computation
**ACE-tail**.

**⟨2⟩4.** Commuting the hopping kernels through `θ_c` adds only terms near
`|x-y|=O(1)` plus rapidly decreasing long-hop tails.  By ⟨1⟩4 their packet
norm is `O(|t|^{2-N})`; on the main cones **ACE-tail** gives
`O(|t|²e^{-μ ε_v|t|/2})` (or `O(|t|^{2-N})` after almost-local truncation).

*Justification.* D28-P(4),(6), ⟨1⟩4.⟨2⟩2--⟨2⟩3, and rapid decay of the
hopping kernels from ⟨1⟩3.⟨2⟩3.

**⟨2⟩5.** Taking `N≥5` gives an integrable majorant.  Since
`d[e^{itH}I_ce^{-itH_{0,c}}F]/dt=i e^{itH}(HI_c-I_cH_{0,c})e^{-itH_{0,c}}F`,
Cook's criterion yields `W_-^L`, `W_+^L`, and `W_+^T`.

*Justification.* ⟨2⟩4 and the fundamental theorem of calculus for
Hilbert-space-valued `C^1` functions.  **⟨2⟩6. QED.**

---

## 3. Isometry, channel number, and the T1 bridge

### ⟨1⟩6. ACE.1 and ACE.2

**ASSUME.** ⟨1⟩5 and D28-P(6).

**PROVE.** The constructed wave operators are isometries and `N_T^{ex}` is
well defined, without completeness.

**⟨2⟩1.** In a same-channel scalar product, all kink cores lie in one velocity
cone and all magnon cores in the disjoint cone.  Contracting the intervening
uniform MPS tail gives the product of the exact kink and magnon Gram forms;
the remainder is bounded exactly as in ⟨1⟩5.⟨2⟩3--⟨2⟩4.

*Justification.* D1(c,e′), D28-P(2),(3),(6), and named computation
**ACE-Gram**.

**⟨2⟩2.** Exact Gram normalization of `Γ_K,Γ_{M,γ}` therefore gives
`lim_{t→±∞}||I_ce^{-itH_{0,c}}F||=||F||`.  Unitarity of `e^{itH}` and strong
convergence imply `||W_cF||=||F||`.

*Justification.* **ACE-Gram**, D28-P(2)--(3), and ⟨1⟩5.

**⟨2⟩3.** For the two outgoing sides, transfer factorization leaves a vacuum
one-point factor on at least one tail; it vanishes because the creator has
strictly positive energy transfer.  Hence `ran W_+^L⊥ran W_+^T` and
`W_+=W_+^L\oplus W_+^T` is an isometry.

*Justification.* D28-P(3),(6), source energy-momentum transfer relation
`(EM-transfer-relation)`, and **ACE-Gram**.

**⟨2⟩4.** Each limit intertwines its free channel dynamics:
`e^{isH}W_c=W_ce^{isH_{0,c}}`.

*Justification.* In the defining limit replace `t` by `t+s`; the finite shift
does not change `t→±∞`, and the group laws move the remaining `s` to the two
sides.  This is the standard wave-operator intertwining computation.

**⟨2⟩5.** On `H_out^{ex}=ran W_+`,
`N_T^{ex}=W_+P_TW_+^*` satisfies `(N_T^{ex})^2=N_T^{ex}` and is self-adjoint.
No assertion is made on `(H_out^{ex})^⊥` or that `H_out^{ex}` exhausts a
spectral subspace.

*Justification.* ⟨2⟩3 and orthogonality of `P_T` in the direct-sum channel
space.  **⟨2⟩6. QED.**

### ⟨1⟩7. ACE.3, bridge to the T1 outcome measure

**ASSUME.** A normalized `Ψ∈ran W_-^L∩H_out^{ex}`, the charge clause of the
theorem, and existence of Lane T1's ordered-limit outcome measure.

**PROVE.** The constructed channels give `p_0^{ex}=1-p_2^{ex}` and
`p_2^{ex}=⟨N_T^{ex}⟩`.

**⟨2⟩1.** Write `W_+^*Ψ=(F_L,F_T)`.  Reflection has
`ν=q_L-q_in=0`; transmission has `ν=q_T-q_in=2`.

*Justification.* The theorem's charge assignment and named computation
**ACE-ledger**.

**⟨2⟩2.** The asymptotic charge spectral projections on the constructed
channel space are `P_L` at `ν=0` and `P_T` at `ν=2`; coherence between the
two legs is retained until this spectral measure is taken.

*Justification.* The assumed T1 ordered-limit measure, D14, D17, the theorem's
definite channel charges, and ⟨1⟩6.⟨2⟩3--⟨2⟩5.

**⟨2⟩3.** Hence
`p_2^{ex}=||F_T||²=⟨Ψ,N_T^{ex}Ψ⟩` and
`p_0^{ex}=||F_L||²=1-p_2^{ex}`.  B3 gives
`2sδx_ex+2p_2^{ex}=0`, exactly Lane T1's target formula
`-(2s)^{-1}Σ_ννp_ν` on support `{0,2}`.

*Justification.* ⟨2⟩1--⟨2⟩2, claim B3, and **ACE-ledger**.

**⟨2⟩4.** If an incoming vector is not in `H_out^{ex}`, AC-EX supplies no
probabilities for its orthogonal component.  This is the precise point where
asymptotic completeness would be needed and is not claimed.

*Justification.* ⟨1⟩6.⟨2⟩5.  **⟨2⟩5. QED.**  □

---

## 4. CHECKER SPEC

Implement named certificate **ACE-C1** on `ℓ²(ℤ_N²)` with
`E_K(p)=0.16(1-cos p)`, `ω(k)=1+0.6(1-cos k)`, smooth bump packets supported
in `p∈[0.05,0.15]`, `k∈[0.65,0.75]`, and contact defect
`V(x,y)=1_{|x-y|≤3}`.  Use FFT free propagation with `N≥8192` before wraparound.

The checker must certify: kink bandwidth `W_K=0.32`; magnon gap `Δ_M=1`;
absorption margin `Δ_M-W_K=0.68`; packet energy supremum `<1.163` versus the
two-magnon threshold `2`; and velocity separation `>0.33`.  It then computes
`C(t)=||V e^{-itH_0}(f⊗g)||_2` at `t=128,256,…,4096`; the normalized-bump
reference values are approximately
`0.1888,0.0844,0.0166,0.00241,0.000228,0.0000105`.  Require the last three
effective doubling exponents to be `<-2`, together with convergence of the
trapezoidal Cook tail: its last interval contribution is `<0.26` and each of
its last two contribution ratios is `<0.30`.

Mutation `--red-equal-velocity` sets the two dispersions and momentum packets
equal; `C(t)` then does not pass the decay/tail gate.  Independent mutation
`--red-absorption` sets `Δ_M=0.2`; the explicit `Δ_M>W_K` gate must fail.
This certificate tests **ACE-SP**, **ACE-Cook**, and both load-bearing threshold
inequalities; it does not certify the MPS transfer hypothesis or completeness.

## 5. MERGE PROPOSALS

### `definitions.md` — append exactly

> **D28 (H-ACE: exact fixed-packet kink--magnon band data).**  Assume
> H-MQG(1)--(3).  In addition:
>
> 1. The kink folium has a covariant positive-energy Hilbert realization
> `(H_{αβ},π_{αβ},U_{αβ})` implementing the commuting infinite-volume time and
> lattice translations.  This is extra structure beyond the state-set
> definition D9/A2.
> 2. Its Hamiltonian has an isolated finite-multiplicity kink band with
> dispersion `E_K∈C²(𝕋)`.  A fixed Gram-normalized, translation-covariant
> finite-core ansatz frame gives an **exact** band map `Γ_K`, satisfying
> `H_{αβ}Γ_K=Γ_KE_K`; it is not merely a Rayleigh--Ritz approximation.
> 3. Each relevant vacuum tail `γ∈{α,β}` has an isolated selected magnon band
> `ω_γ` (identified as `ω` when symmetry relates the tails), gap
> `Δ_M:=min_kω(k)>0`, and Gram-normalized **exact** band map `Γ_{M,γ}`.  A
> spacetime-Schwartz energy-momentum filter of a local observable gives
> almost-local creators `a_{γ,b}(n)` with
> `a_{γ,b}(n)Ω_γ=Γ_{M,γ}δ_{n,b}` in the chosen finite frame and with strictly
> positive energy transfer.  This equality, not merely nonzero overlap with
> the band, is part of the exactness hypothesis.
> 4. Packet amplitudes are finite sums of `C_c^∞` products and the resulting
> physical packet states lie in the `ℓ¹` class D17.  The dispersions
> are `C^∞` on neighbourhoods of their supports (global `C²` is retained),
> their kink and magnon velocity supports have distance `ε_v>0`, and their
> signs are: incoming-left `v_M-v_K≥ε_v` at `t→-∞`; outgoing-left
> `v_M-v_K≤-ε_v`; outgoing-right `v_M-v_K≥ε_v` at `t→+∞`.  Thus this is a
> fixed-packet condition and excludes equal velocities and the soft endpoint.
> 5. Put `K_-:=min E_K`, `K_+:=max E_K`, `W_K:=K_+-K_-`, and let `I_in` be
> the range of `E_K(p)+ω(k)` on the incoming packet support.  Same-band kink
> absorption is excluded by
> `d_abs:=dist(I_in,[K_-,K_+])>0`; the packet-independent sufficient condition
> is the explicit inequality `Δ_M>W_K`.  With
> `Δ_r:=min_kω_r(k)` for every other known one-particle vacuum band and
> `K_*:=inf_{j≥2,p}E_{K,j}(p)` for every other known kink band, require
> `sup I_in+η_inel < Θ_inel`, where
> `Θ_inel:=min{K_-+2Δ_M, K_* , inf_r(K_-+Δ_r)}` and `η_inel>0`; absent entries
> are `+∞`.  The three entries respectively exclude an additional magnon, a
> higher-kink absorption channel, and a different one-particle channel.  An
> uncomputed wall--magnon bound band is not excluded by this inequality.
> 6. The exact ansatz Wannier cores are almost local about their labelled
> positions, uniformly over the finite frame, and mixed matrix elements with
> observables separated onto either tail factor through the corresponding
> vacuum transfer projection with the D1(c) `λ̃` bound.  This is the
> localization input that turns exact band equations into a two-cluster
> estimate; isolated eigenvalues alone do not imply it.
>
> The asymptotic channel Hamiltonian is multiplication by `E_K(p)+ω_γ(k)`.
> Smooth packet domains with the three velocity signs are denoted
> `D_-^L,D_+^L,D_+^T`; `P_L,P_T` are the two outgoing direct-sum projections.

### `claims/CLAIMS.md` — append exactly

| AC-EX | Under D28/H-ACE's **exact** ansatz-band, sector-covariance, transfer-factorization, velocity-separation, and explicit inelastic-threshold hypotheses, the fixed-packet kink--magnon Cook limits exist and are isometries; `N_T` is a projection on the constructed out-space.  On vectors lying in both the constructed in- and out-ranges, the T1 measure has constructed support `{0,2}` with `p_2=⟨N_T⟩`.  No completeness, raw-band-data implication, bound-state exclusion, or soft limit is claimed. | SKETCH | D1, D5, D9, D10, D13, D14, D17, B3, M-quant-G, D28 | theory/ansatz-scattering.md | ACE-C1 (specified in shard; not yet implemented) |

### `notation.md` — append exactly

| `Γ_K`, `Γ_{M,γ}` | exact Gram-normalized kink and tail-magnon band maps assumed by H-ACE | definitions.md D28 |
| `E_K`, `K_-`, `K_+`, `W_K`, `Δ_M` | kink dispersion, its extrema and bandwidth, and the selected magnon gap | definitions.md D28 |
| `ε_v`, `d_abs`, `Θ_inel`, `η_inel` | velocity gap, same-kink absorption gap, known inelastic threshold, and its margin | definitions.md D28 |
| `D_-^L`, `D_+^L`, `D_+^T` | incoming-left, outgoing-left, and outgoing-transmitted fixed-packet domains | definitions.md D28 |
| `H_out^{ex}`, `N_T^{ex}` | constructed outgoing range and its transmitted-channel projection; no completeness implied | theory/ansatz-scattering.md ACE.2 |

## 6. HONEST STATUS

What is proved here is the Cook/isometry implication from D28-P, including the
MPS transfer replacement for the vacuum and the exact `{0,2}` bridge on the
intersection of constructed ranges.  The raw generalized eigenvalues of
refs 1103.2286/1810.07006 do **not** prove D28-P: exact band invariance,
covariant kink-sector implementation, smooth exact frames, and tail
factorization are assumed.  The inequalities `Δ_M>W_K` and
`sup I_in<Θ_inel` exclude the named band-data channels only; they neither
exclude an uncomputed wall--magnon bound band nor prove completeness.  The
general obstruction is therefore precise: without a covariant localized
exact kink frame, the cancellation **ACE-Cook** cannot even be formulated;
without D28-P(6), its vacuum-zero defect need not be small on a kink.  No soft,
equal-velocity, packet-uniform, model-uniform, or asymptotic-completeness claim
survives.
