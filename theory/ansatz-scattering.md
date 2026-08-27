<!-- ROLE: T2 proposer shard for AC-EX.  Only a critic-fixed L6 loop may
     promote the claim.  New definitions are merge proposals, not live D-numbers.
     r2 revision (2026-08-28): repairs to the four MAJOR and two MINOR
     objections of theory/verdicts/ansatz-scattering-r1.md; see §6 REPAIR
     RESPONSE for the objection-by-objection map.  Every edit below is
     traceable to an objection id; no other change was made. -->

# AC-EX — fixed-packet kink--magnon wave operators from exact ansatz bands

**Proposer status:** **SKETCH**.  This is an existence and isometry theorem on
specified packet domains.  It proves neither asymptotic completeness nor that
an arbitrary incoming vector has an expansion in the constructed outgoing
channels.  Proposed definition D28 is reproduced verbatim in **MERGE
PROPOSALS** and is cited below as `D28-P`.  After the r1 loop, part **ACE.3 is
conditional** on a named local-decay hypothesis `(AD3-ex)` that this shard does
*not* prove (Objection 4).

## 0. Theorem

### THEOREM AC-EX

**ASSUME.** H-MQG(1)--(3) from `memory-quantization-general.md`, proposed
`D28-P (H-ACE)`, and — for ACE.3 only — the charge assignment
`q_in=q_L=-1`, `q_T=+1` together with the local-decay hypothesis `(AD3-ex)`
stated in ⟨1⟩7.

**PROVE.**  On the fixed packet domains of D28-P:

1. **(ACE.1)** the Cook limits `W_-^L`, `W_+^L`, and `W_+^T` exist;
2. **(ACE.2)** `W_-^L` and `W_+:=W_+^L\oplus W_+^T` are isometries, and
   `N_T^{ex}:=W_+P_TW_+^*` is an orthogonal projection on the constructed
   out-space `H_out^{ex}:=ran W_+` (D18's `N_T`, restricted to this range);
3. **(ACE.3)** *(conditional on `(AD3-ex)`)* for a normalized event vector in
   `ran W_-^L\cap H_out^{ex}` for which Lane T1's outcome measure exists,
   the constructed-channel part of that measure is

   `p_ν^{ex}=||P_LW_+^*Ψ||² δ_{ν,0}+||P_TW_+^*Ψ||² δ_{ν,2}`,

   so `p_2^{ex}=⟨Ψ,N_T^{ex}Ψ⟩` and the T1 ledger gives
   `δx_ex=-p_2^{ex}/s`.

Infinite-volume dynamics is formed first, then the wave-operator time limit;
any T1 fixed-window limit follows that, and `W↑ℤ` is last (D17--D18 order).
No statement is made at `k=0` or after a packet-soft limit.

### 0.1 Standing conventions of this shard

**(C1) Vacuum vectors versus vacuum states** *(Objection 6)*.  `ω_γ`,
`γ∈{α,β}`, is the vacuum **state** on `𝔄` (D1(d)); `(H_γ,π_γ,Ω_γ)` is its GNS
triple, and `Ω_γ` is a vector **in `H_γ` only**.  There is no vacuum vector in
the kink Hilbert space `H_{αβ}` of D28-P(1).  Every display of the form
`XΩ_γ=0` below is a statement in `H_γ` about `π_γ(X)`, equivalent to
`ω_γ(X^†X)=0`; the corresponding statement inside `H_{αβ}` is always made
through the two-cluster inequality (D28-C), never by transporting `Ω_γ`.

**(C2) Filtered frames** *(Objection 1)*.  Fix once and for all momentum
filters `χ_K,χ_γ∈C_c^∞(𝕋)` and companions `χ̃_K,χ̃_γ∈C_c^∞(𝕋)` as in
D28-P(3)--(4): `χ_•≡1` on the corresponding packet momentum support,
`χ̃_•≡1` on `supp χ_•`, and `supp χ̃_•` contained in the neighbourhood on which
the corresponding dispersion is `C^∞`.  Write `e_x(p):=e^{-ipx}`,
`ê_x^K:=χ_K e_x`, `ê_n^γ:=χ_γ e_n`.  The **filtered Wannier frames** are

`κ_a(x):=Γ_K(ê_x^K⊗e_a)`,  `a_{γ,b}(n)Ω_γ=Γ_{M,γ}(ê_n^γ⊗e_b)`  (D28-P(3)),

and the **filtered hopping kernels** are the Fourier coefficients of the
matrix-valued `C^∞` symbols `h_K:=E_Kχ̃_K` and `h_γ:=ω_γχ̃_γ`:
`h_{K,a'a}(m):=∫(dp/2π)e^{ipm}(h_K(p))_{a'a}`, likewise `h_{γ,b'b}(m)`.
Unfiltered objects carry a superscript `(0)`: `κ_a^{(0)}(x):=Γ_K(e_x⊗e_a)`.
The r1 shard used `χ_K=χ_γ≡1` (position deltas); that choice is what
Objection 1 refuted, and it is also inconsistent with D28-P(3)'s own
spacetime-Schwartz energy--momentum filter, which cannot produce a
momentum-flat profile.

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
label of a bare mixed-uMPS formula.  In particular `κ_a(x)=Γ_K(ê_x^K⊗e_a)` is
supported, in the spectral sense, on the compact energy set `E_K(supp χ_K)`,
so all vectors used below lie in a bounded spectral subspace of `H_{αβ}` and
every commutator manipulation with `H` is on an entire vector for the
dynamics.

*Justification.* D28-P(2), the SNAG fibering of ⟨2⟩2, and `supp χ_K` compact
(C2).  The phase ambiguity being removed is recorded in
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
products.  Step ⟨1⟩6 replaces this by the **displayed** two-cluster inequality
(D28-C) of D28-P(5); no vacuum Fock formula is imported.  What (D28-C) does
*not* supply is the source's four-point decay estimate `(full-decay)`; ⟨1⟩6.⟨2⟩1
therefore derives the multi-cluster form it needs from the single displayed
cut, rather than assuming it.

*Justification.* Source Theorem `clustering`, Lemma `clustering-lemma` (its
proof's `P({0})^⊥=1-|Ω⟩⟨Ω|` decomposition and display `(full-decay)`),
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

### ⟨1⟩3. Filtered creators are almost local and their defects vanish exactly

**ASSUME.** D28-P(1),(3),(4),(5).

**PROVE.** (a) The filtered magnon creators are almost local, uniformly under
lattice translation; (b) the filtered hopping kernels `h_K,h_γ` are rapidly
decreasing; (c) the one-body defect `D_{γ,b}(n)` is almost local and satisfies
`ω_γ(D_{γ,b}(n)^†D_{γ,b}(n))=0`; (d) the kink frame has **no** defect.

**⟨2⟩1.** For local `A` and `r>v_LR|t|`, finite-range Lieb--Robinson gives a
conditional-expectation approximant `A_{t,r}` supported in the `r`-fattening
of `supp A`, with `||τ_t(A)-A_{t,r}||≤Ce^{-μ(r-v_LR|t|)}`.

*Justification.* Named computation **ACE-LR**, obtained by applying the
finite-range `(LRB)` to observables outside the fattened support and then the
conditional-expectation argument of source Proposition `cor:localization`.

**⟨2⟩2.** If `F(t,n)` is Schwartz and its Fourier support isolates the selected
magnon shell, split the smearing into `|t|+|n|≤R` and its complement.  Apply
⟨2⟩1 with fattening `R` to the first part and Schwartz decay to the second;
the error is `O(R^{-N})` for every `N`.  Hence `a_{γ,b}(n)=τ_n(τ_F(A_{γ,b}))`
is almost local, uniformly in `n`, and bounded: `||a_{γ,b}(n)||≤||A_{γ,b}||·||F||_1`.

*Justification.* **ACE-LR**, source Lemma `almost-locality` (whose proof is the
same split, with `A_{(r)}` the truncated smearing), and D28-P(3).

**⟨2⟩3. (Kernel decay — the repair of Objection 1.)**  `h_K=E_Kχ̃_K` and
`h_γ=ω_γχ̃_γ` are `C^∞` on all of `𝕋`, hence their Fourier coefficients obey
`|h_K(m)|+|h_γ(m)|≤C_N⟨m⟩^{-N}` for every `N`.

*Justification.* `χ̃_•∈C_c^∞` with `supp χ̃_•` a compact subset of the open
neighbourhood `U_•` on which the dispersion is `C^∞` (D28-P(4)).  On `U_•` the
product of two `C^∞` functions is `C^∞`; on the open set `𝕋∖supp χ̃_•` the
product vanishes identically; the two open sets cover `𝕋`.  Rapid decay of
Fourier coefficients of a `C^∞` function on `𝕋` is repeated integration by
parts.  *Note what is and is not claimed:* the **global** `C²` dispersion has
only `o(m^{-2})` Fourier coefficients — this is exactly the r1 defect — and no
statement about the unfiltered kernels is made or used anywhere below.

**⟨2⟩4. (Exact defect equations.)**  With
`D_{γ,b}(n):=[H,a_{γ,b}(n)]-Σ_{m,b'}h_{γ,b'b}(m-n)a_{γ,b'}(m)`,

`π_γ(D_{γ,b}(n))Ω_γ=Γ_{M,γ}((ω_γ-h_γ)χ_γe_n⊗e_b)=0`,

i.e. `ω_γ(D^†D)=0`; and on the kink side, exactly,
`Hκ_a(x)=Σ_{x',a'}h_{K,a'a}(x'-x)κ_{a'}(x')` with **no** defect term.

*Justification.* ASSUME `HΩ_γ=0` (stationary vacuum, H-MQG(1) with the
generator normalised to annihilate the vacuum) and the exact band equations
`HΓ_{M,γ}=Γ_{M,γ}ω_γ`, `H_{αβ}Γ_K=Γ_KE_K` (D28-P(2)--(3)).  Then
`π_γ([H,a(n)])Ω_γ=HΓ_{M,γ}(ê_n^γe_b)=Γ_{M,γ}(ω_γê_n^γe_b)`, while
`Σ_{m,b'}h_{γ,b'b}(m-n)Γ_{M,γ}(ê_m^γe_{b'})=Γ_{M,γ}(χ_γe_n·h_γe_b)`, because
`Σ_mh_γ(m-n)e^{-ikm}=e^{-ikn}h_γ(k)`.  Their difference carries the factor
`χ_γ(ω_γ-ω_γχ̃_γ)=χ_γω_γ(1-χ̃_γ)≡0` since `χ̃_γ≡1` on `supp χ_γ`.  The kink
identity is the same computation with `(E_K-h_K)χ_K≡0` and `Γ_K` exact.  This
is named computation **ACE-filter**; it is the step the r1 position-delta
normalisation could not supply.

**⟨2⟩5.** `D_{γ,b}(n)` is almost local about `n`, uniformly in `n`.

*Justification.* `[H,a(n)]=Σ_x[h_x,a(n)]` converges in norm because `H` has
finite range and `a(n)` is almost local (⟨2⟩2), so `||[h_x,a(n)]||` is rapidly
decreasing in `dist(x,n)`; the resulting sum is almost local about `n`.  The
subtracted term is a convolution of the almost-local family `a_{γ,b'}(m)` with
the rapidly decreasing kernel `h_γ` (⟨2⟩3), hence almost local about `n`.
D10(a) supplies the finite-range structure.

**⟨2⟩6. (Filtered two-cluster estimate.)**  For every `N` there is `C_N` with:
for all frame indices, all `x,x'`, all `r≥1`, and every `A,B` as in (D28-C)
(supported on the `α` resp. `β` side at distance `≥r` from `{x,x'}`; either may
be `1`),

`|⟨κ_a(x),ABκ_{a'}(x')⟩-ω_α(A)ω_β(B)⟨κ_a(x),κ_{a'}(x')⟩| ≤ C_N||A||\,||B||⟨r⟩^{-N}`.

*Justification.* `κ_a(x)=Σ_{x̄}χ̂_K(x̄-x)κ_a^{(0)}(x̄)` with `χ̂_K` rapidly
decreasing and `||κ_a^{(0)}(x̄)||=1` (Gram-normalised `Γ_K`, D28-P(2)).  Split
the double sum at `|x̄-x|≤r/2` and `|x̄'-x'|≤r/2`: on that part `Λ_α,Λ_β` are
still on their respective sides of both `x̄,x̄'` and at distance `≥r/2` from
them, so the hypothesis (D28-C) of D28-P(5) applies and gives
`C_cl||A||\,||B||λ̃^{r/2}`; off it, the bracket is bounded by `2||A||\,||B||`
and the weights sum to `||χ̂_K||_1·C_N'⟨r⟩^{-N}`.
Uniformity in `x,x'` (hence in `t` when the positions are packet-driven) is the
uniformity clause of D28-P(5).  This is named computation **ACE-tail**.

**⟨2⟩7. QED.**

### ⟨1⟩4. Fixed packets separate in velocity

**ASSUME.** D28-P(4).

**PROVE.** The real-space packet outside its velocity cone has summable decay
strong enough for Cook's method.

**⟨2⟩1.** For
`f_t(x)=∫(dp/2π)e^{i(px-tE(p))}f(p)`, choose a cone containing
`E'(supp f)`.  Outside it, `|x/t-E'(p)|≥ε_v`; repeated integration by parts
with `(it(x/t-E'(p)))^{-1}∂_p` gives pointwise `C_N⟨|x|+|t|⟩^{-N}`.

*Justification.* Named computation **ACE-SP**; D28-P(4) supplies smoothness on
a neighbourhood of `supp f`, compact support and the positive separation
denominator.  This rederives the one-dimensional case of source Proposition
`norm-corollary`.

**⟨2⟩2.** Summing first over `|x|≤C|t|` and then over its complement yields
`||1_{outside}f_t||_1=O(|t|^{1-N})`, whereas
`||f_t||_1=O(1+|t|)`.

*Justification.* **ACE-SP** and the convergent sum
`Σ_{|x|>C|t|}⟨x⟩^{-N}=O(|t|^{1-N})`.  *(Objection 7.)*  `O(1+|t|)` is a
deliberate overestimate of the true dispersive rate `O(|t|^{1/2})`; it is used
only as an upper bound, and it is what produces the `|t|²` prefactor in
⟨1⟩5.⟨2⟩5.  With the sharp rate the prefactor is `|t|` and `N≥4` suffices;
nothing below depends on the difference, since `N` is free.

**⟨2⟩3.** If `dist(V_K,V_M)=ε_v>0`, the main cones obey
`|x-y|≥ε_v|t|/2` for large `|t|`; the sign conditions in D28-P(4) put the
magnon on the left for `t→-∞`, and on the declared left/right side for
`t→+∞`.  In particular, for `|t|` large enough that `ε_v|t|/2>2w` (`w` the
`θ_c` transition width of ⟨1⟩5.⟨2⟩1), the near-diagonal region `|x-y|≤2w` lies
entirely outside the product of the two main cones, so ⟨2⟩1 applies there to at
least one factor.

*Justification.* D28-P(4) and elementary cone geometry.

**⟨2⟩4. QED.**

### ⟨1⟩5. The cluster defect is Cook integrable

**ASSUME.** D28-P and ⟨1⟩3--⟨1⟩4.

**PROVE.** `∫_{|t|≥1}||(H I_c-I_cH_{0,c})e^{-itH_{0,c}}F||dt<∞` for each
allowed packet and channel end.

**⟨2⟩1. (The identification, with `θ_c` specified — Objection 5.)**  Fix
`w≥1` and `θ∈C^∞(ℝ)` monotone with `θ'` supported in `[-w,w]`,
`||θ'||_∞≤C/w`, `θ=1` on `[w,∞)`, `θ=0` on `(-∞,-w]`; put `θ_T(u):=θ(u)`,
`θ_L(u):=1-θ(u)`, restricted to `u∈ℤ`.  Both are fixed profiles, independent
of `t` and of the packet.  With the filtered kink frame `κ_a(x)` of (C2),

`I_cF:=Σ_{x,y,a,b}θ_c(y-x)F^{ab}(x,y)a_{c,b}(y)κ_a(x)`.

This is the kink--magnon precursor identification.

*Justification.* D28-P(2)--(5); `||a_{c,b}(y)κ_a(x)||≤C_a` uniformly by
⟨1⟩3.⟨2⟩2 and `||κ_a(x)||=||χ_K||_{L²}`, so absolute convergence holds on the
Schwartz packet core; the limiting isometry (not `I_c` itself) extends by ⟨1⟩6.

**⟨2⟩2. (ACE-Cook.)**  `H_{0,c}` is multiplication by `E_K(p)+ω_γ(k)`, which on
the packet domain coincides with convolution by the filtered kernels
`h_K,h_γ` (D28-P(4): the packet momentum supports lie in `{χ_•≡1}`, and
`h_•=`dispersion there).  Writing `Haκ=aHκ+[H,a]κ` and inserting ⟨1⟩3.⟨2⟩4,

`(HI_c-I_cH_{0,c})F = Σ_{x,y}θ_c(y-x)F(x,y)D_{c,b}(y)κ_a(x) + T_M + T_K`,

`T_M := Σ_{x,y}a(y)κ(x)Σ_{y''}h_γ(y-y'')[θ_c(y''-x)-θ_c(y-x)]F(x,y'')`,
`T_K := Σ_{x,y}a(y)κ(x)Σ_{x''}h_K(x-x'')[θ_c(y-x'')-θ_c(y-x)]F(x'',y)`

(frame indices suppressed).  The exact kink identity of ⟨1⟩3.⟨2⟩4 removes the
kink part of `H_{0,c}` with **no** residue, and the exact magnon equation
leaves precisely `D_{c,b}(y)κ_a(x)`; the only other residue is the failure of
the two hopping kernels to commute with `θ_c`.

*Justification.* Direct commutator calculation, D28-P(2)--(4), ⟨1⟩3.⟨2⟩4, and
⟨1⟩1.⟨2⟩3 for the domain (all vectors lie in a bounded spectral subspace, and
`a_{c,b}(y)` has compact energy--momentum transfer by D28-P(3), so
`a(y)κ(x)` does too).  This is named computation **ACE-Cook**.

**⟨2⟩3. (Defect term.)**  `||D_{γ,b}(y)κ_a(x)||≤C_N⟨x-y⟩^{-N}` for every `N`.

*Justification.* Truncate `D_{γ,b}(y)` almost-locally at radius `|x-y|/3`
(⟨1⟩3.⟨2⟩5), producing `O_{|x-y|/3}∈𝔄_Λ` with `Λ` at distance `≥|x-y|/3` from
`x` on the `γ` side, and error `C_N⟨x-y⟩^{-N}`.  Then
`||D_{γ,b}(y)κ_a(x)||²=⟨κ_a(x),D^†Dκ_a(x)⟩`, and **ACE-tail** (⟨1⟩3.⟨2⟩6, the
one-tail case with the opposite factor `1`) applied to `O=(D^†D)_{trunc}` gives
`⟨κ_a(x),Oκ_a(x)⟩=ω_γ(O)||κ_a(x)||²+O(⟨x-y⟩^{-N})`.  Finally
`ω_γ(O)=ω_γ(D^†D)+O(⟨x-y⟩^{-N})=O(⟨x-y⟩^{-N})` by ⟨1⟩3.⟨2⟩4.  *(Objection 6:
the vanishing quantity is the vacuum **state** evaluation `ω_γ(D^†D)`, equal to
`||π_γ(D)Ω_γ||²_{H_γ}`; no vacuum vector is transported into `H_{αβ}`.)*

**⟨2⟩4. (Commutator terms — the repair of Objection 1.)**
`||T_M||+||T_K||=O(|t|^{2-N})` for every `N`, uniformly for `|t|≥t_0`.

*Justification.* By the triangle inequality and ⟨2⟩1,
`||T_M||≤C_aΣ_{x,y''}|F_t(x,y'')|·S(y''-x)` with
`S(u):=Σ_m|h_γ(m)|·|θ_c(u)-θ_c(u+m)|` (substituting `m:=y-y''`, `u:=y''-x`, so
that `y-x=u+m`).  Two properties of `S`:
**(S1)** `S(u)≤2||h_γ||_1<∞` for every `u`, and `||h_γ||_1<∞` by ⟨1⟩3.⟨2⟩3;
**(S2)** for `|u|>2w`, `θ_c(u)-θ_c(u+m)=0` unless the interval `[u,u+m]` meets
the transition region `[-w,w]`, which forces `|m|≥|u|-w≥|u|/2`; hence by
⟨1⟩3.⟨2⟩3, `S(u)≤2Σ_{|m|≥|u|/2}|h_γ(m)|≤C_{N+2}Σ_{|m|≥|u|/2}⟨m⟩^{-N-2}≤C_N'⟨u⟩^{-N-1}`.
Now split the `(x,y'')` sum by cones (⟨1⟩4.⟨2⟩3).  *On* the product of the two
main cones, `|u|≥ε_v|t|/2>2w`, so (S2) gives `S≤C_N'⟨ε_v|t|/2⟩^{-N-1}`, and
multiplying by `||F_t||_1=O(|t|²)` (⟨1⟩4.⟨2⟩2) leaves `O(|t|^{1-N})`.  *Off* it,
at least one factor of `F_t=f_t⊗g_t` is outside its own cone, so
`Σ_{off}|F_t|≤||1_{out}f_t||_1||g_t||_1+||f_t||_1||1_{out}g_t||_1=O(|t|^{2-N})`
by ⟨1⟩4.⟨2⟩1--⟨2⟩2, and (S1) bounds `S` there.  The off-cone piece is the
binding one, giving `O(|t|^{2-N})`.  `T_K` is the same computation with
`u:=y-x''`, `m:=x-x''` and `h_K` in place of `h_γ`.  **This is the step that
fails for the r1
unfiltered kernels**: with only `o(m^{-2})` decay, regime (i) gives
`S(u)=o(1/|u|)` and hence a non-integrable `o(1/|t|)` majorant — exactly
Objection 1(b)(ii).

**⟨2⟩5.** The defect term of ⟨2⟩2 obeys the same cone split as ⟨2⟩4: on the
main cones `Σ|F_t|·C_N⟨x-y⟩^{-N}≤C_N⟨ε_v|t|/2⟩^{-N}||F_t||_1=O(|t|^{2-N})` by
⟨2⟩3 and ⟨1⟩4.⟨2⟩2--⟨2⟩3, and off them `O(|t|^{2-N})` as in ⟨2⟩4.  Combining
with ⟨2⟩4 and taking `N≥5` gives the majorant `C|t|^{-3}`, which is integrable
(`N≥4` would already do).  Since
`d[e^{itH}I_ce^{-itH_{0,c}}F]/dt=i e^{itH}(HI_c-I_cH_{0,c})e^{-itH_{0,c}}F`,
Cook's criterion yields `W_-^L`, `W_+^L`, and `W_+^T`.

*Justification.* ⟨2⟩3--⟨2⟩4 and the fundamental theorem of calculus for
Hilbert-space-valued `C^1` functions.  **⟨2⟩6. QED.**

---

## 3. Isometry, channel number, and the T1 bridge

### ⟨1⟩6. ACE.1 and ACE.2

**ASSUME.** ⟨1⟩3--⟨1⟩5 and D28-P(5).

**PROVE.** The constructed wave operators are isometries and `N_T^{ex}` is
well defined, without completeness.

**⟨2⟩1. (Four-cluster factorization, derived — Objection 3(ii).)**  For `y,y'`
on the `γ` side at distance `≥r` from `{x,x'}`, and every `N`,

`|⟨a_{γ,b}(y)κ_a(x),a_{γ,b'}(y')κ_{a'}(x')⟩ - ⟨κ_a(x),κ_{a'}(x')⟩·G_γ^{bb'}(y,y')| ≤ C_N⟨r⟩^{-N}`,

where `G_γ^{bb'}(y,y'):=⟨Γ_{M,γ}(ê_y^γe_b),Γ_{M,γ}(ê_{y'}^γe_{b'})⟩_{H_γ}` is
the **exact** magnon Gram form.

*Justification.* Write the left scalar product as `⟨κ_a(x),Oκ_{a'}(x')⟩` with
`O:=a_{γ,b}(y)^†a_{γ,b'}(y')`.  By ⟨1⟩3.⟨2⟩2, `O` is almost local about
`{y,y'}` with `||O||≤C_a²`; truncate it to `𝔄_Λ`, `Λ` on the `γ` side at
distance `≥r/3` from `{x,x'}`, with error `C_N⟨r⟩^{-N}`.  **ACE-tail**
(⟨1⟩3.⟨2⟩6, one-tail case) then factors it, and the vacuum evaluation is
exactly the magnon
Gram: `ω_γ(a(y)^†a(y'))=⟨π_γ(a(y))Ω_γ,π_γ(a(y'))Ω_γ⟩=G_γ^{bb'}(y,y')` by
D28-P(3).  So the four-cluster form follows from the **single** displayed cut
(D28-C) plus almost-locality — no iterated-factorization hypothesis is needed,
and the source's `(full-decay)` four-point estimate is not imported.  This is
named computation **ACE-Gram**.

**⟨2⟩2.** On the packet domain the filters are invisible: if `supp F̂` lies in
`{χ_K≡1}×{χ_γ≡1}` then `Σ_xF(x)κ_a(x)=Γ_K(F̂χ_Ke_a)=Γ_K(F̂e_a)` and likewise
for the magnon factor.  Hence, summing ⟨2⟩1 against `F_t` and using ⟨1⟩4.⟨2⟩3
(`r≥ε_v|t|/2` on the main cones, the rest `O(|t|^{1-N})`),
`lim_{t→±∞}||I_ce^{-itH_{0,c}}F||=||F||`.  Unitarity of `e^{itH}` and strong
convergence imply `||W_cF||=||F||`.

*Justification.* **ACE-Gram**, Gram-normalisation of `Γ_K,Γ_{M,γ}`
(D28-P(2)--(3)), the filter-support clause of D28-P(4), and ⟨1⟩5.

**⟨2⟩3.** For the two outgoing sides the two magnons sit on *opposite* tails, so
the operator between the kink frames is a genuine two-sided product
`O=A·B`, `A:=a_{α,b}(y)^†` on the `α` side and `B:=a_{β,b'}(y')` on the `β`
side.  This is the two-sided case of ⟨1⟩3.⟨2⟩6, which factors it as
`ω_α(A)ω_β(B)⟨κ_a(x),κ_{a'}(x')⟩+O(⟨r⟩^{-N})`; the one-point factor
`ω_β(a_{β,b'}(y'))` vanishes because the creator has strictly positive energy
transfer.  Hence `ran W_+^L⊥ran W_+^T` and `W_+=W_+^L\oplus W_+^T` is an
isometry.

*Justification.* D28-P(3),(5) in its two-sided form (this is the **only** step
that uses both tails at once), ⟨1⟩3.⟨2⟩6, source energy-momentum transfer relation
`(EM-transfer-relation)` (a creator with strictly positive energy transfer has
vanishing vacuum one-point function), and **ACE-Gram**.

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

### ⟨1⟩7. ACE.3, bridge to the T1 outcome measure — CONDITIONAL

**ASSUME.** A normalized `Ψ∈ran W_-^L∩H_out^{ex}`, the charge clause of the
theorem, existence of Lane T1's ordered-limit outcome measure, **and the
following hypothesis, which this shard does not prove** *(Objection 4)*:

> **(AD3-ex) — local decay on the constructed channels.**  Let
> `Ψ=W_+(F_L,F_T)` and `Ψ_t:=e^{-itH}Ψ`.  For every fixed window `W`
> containing the kink core region, with `E_W(·)` the spectral measure of the
> regularised window charge `Q̂_W` (D10(c), D13(a)) and `P_ch`, `ch∈{L,T}`,
> the channel projections of ⟨1⟩6.⟨2⟩5:
> `lim_{t→+∞}||E_W({q_ch})Ψ_t-P_{ch}Ψ_t||=0`, the limit being taken before
> `W↑ℤ` (D18 AD4 order).

`(AD3-ex)` is the AD3 clause of D18 restricted to the constructed channels;
D28-P deliberately does not contain it.  The missing derivation is recorded as
named lemma **ACE-LD** (see HONEST STATUS): the free leg and its dressing leave
any fixed `W` at rate `O(|t|^{-N})` by ⟨1⟩3.⟨2⟩5 and ⟨1⟩4.⟨2⟩1, but converting
that into convergence of the *window-charge spectral projection* requires
control of the boundary-straddling charge on `∂W` that no step of this shard
supplies.

**PROVE.** Given `(AD3-ex)`, the constructed channels give `p_0^{ex}=1-p_2^{ex}`
and `p_2^{ex}=⟨N_T^{ex}⟩`.

**⟨2⟩1.** Write `W_+^*Ψ=(F_L,F_T)`.  Reflection has
`ν=q_L-q_in=0`; transmission has `ν=q_T-q_in=2`.

*Justification.* The theorem's charge assignment and named computation
**ACE-ledger**.

**⟨2⟩2.** Under `(AD3-ex)` the two channels are asymptotically charge-diagonal,
and the inter-channel cross terms vanish:
`|⟨Ψ_t,P_LE_W({q_T})Ψ_t⟩|≤||E_W({q_T})P_LΨ_t||·||Ψ_t||→0` by Cauchy--Schwarz
and `(AD3-ex)` applied to the `L` component.  Hence the asymptotic charge
spectral projections on the constructed channel space are `P_L` at `ν=0` and
`P_T` at `ν=2`; coherence between the two legs is retained until this spectral
measure is taken.

*Justification.* `(AD3-ex)`, Cauchy--Schwarz, D14, D17, the theorem's definite
channel charges, and ⟨1⟩6.⟨2⟩3--⟨2⟩5.  *(The cross-term step is proved here;
the channel-diagonality input is hypothesised, not proved — Objection 4.)*

**⟨2⟩3.** Hence
`p_2^{ex}=||F_T||²=⟨Ψ,N_T^{ex}Ψ⟩` and
`p_0^{ex}=||F_L||²=1-p_2^{ex}`.  B3 gives
`2sδx_ex+2p_2^{ex}=0`, exactly Lane T1's target formula
`-(2s)^{-1}Σ_ννp_ν` on support `{0,2}`.

*Justification.* ⟨2⟩1--⟨2⟩2, claim B3, Lane T1's ledger formula (G-IDX.2 of
`briefs/memory-campaign-target.md`, row to be cited once merged), and
**ACE-ledger**.

**⟨2⟩4.** If an incoming vector is not in `H_out^{ex}`, AC-EX supplies no
probabilities for its orthogonal component.  This is the precise point where
asymptotic completeness would be needed and is not claimed.

*Justification.* ⟨1⟩6.⟨2⟩5.  **⟨2⟩5. QED.**  □

---

## 4. CHECKER SPEC

### ACE-C1 (propagation and defect decay; unchanged arithmetic)

Implement on `ℓ²(ℤ_N²)` with
`E_K(p)=0.16(1-cos p)`, `ω(k)=1+0.6(1-cos k)`, smooth bump packets supported
in `p∈[0.05,0.15]`, `k∈[0.65,0.75]`, and contact defect
`V(x,y)=1_{|x-y|≤3}`.  Use FFT free propagation with `N≥8192` before wraparound.

The checker must certify: kink bandwidth `W_K=0.32`; magnon gap `Δ_M=1`;
packet energy supremum `<1.163` versus the two-magnon threshold `2`; and
velocity separation `>0.33`.  It then computes
`C(t)=||V e^{-itH_0}(f⊗g)||_2` at `t=128,256,…,4096`; the normalized-bump
reference values are approximately
`0.1888,0.0844,0.0166,0.00241,0.000228,0.0000105`.  Require the last three
effective doubling exponents to be `<-2`, together with convergence of the
trapezoidal Cook tail: its last interval contribution is `<0.26` and each of
its last two contribution ratios is `<0.30`.

Mutation `--red-equal-velocity` sets the two dispersions and momentum packets
equal; `C(t)` then does not pass the decay/tail gate.  This certificate tests
**ACE-SP** and the cone-separation input to **ACE-Cook**.  It does **not**
certify the MPS transfer hypothesis (D28-C) or completeness.

*(Objection 2.)*  The gates `Δ_M-W_K=0.68>0` and `sup I_in<Θ_inel` are
**fence arithmetic on Remark D28-R**, not proof gates: no step of ⟨1⟩3--⟨1⟩7
consumes them.  The mutation `--red-absorption` (`Δ_M=0.2`) is retained only as
a regression guard that the fence is computed correctly; it can catch no error
in the proof and must not be reported as a red test of AC-EX.

### ACE-C2 (kernel decay is load-bearing; the Objection-1 red test)

Same lattice, dispersions and packets.  Fix the smooth step `θ` of ⟨1⟩5.⟨2⟩1
with `w=4`, and a magnon filter `χ̃∈C_c^∞` with `χ̃≡1` on `[0.6,0.8]`,
`supp χ̃⊂[0.5,0.9]`.  Compute the `θ`-commutator defect of ⟨1⟩5.⟨2⟩2,

`C_θ(t):=|| Σ_{y''}h(y-y'')[θ(y''-x)-θ(y-x)]F_t(x,y'') ||_{ℓ²(x,y)}`,
`F_t=f_t⊗g_t` normalized, at `t=128,256,…,4096`.

*Green run:* `h(m)` = Fourier coefficients of `h_γ=ωχ̃` (rapidly decreasing).
Gate: the last three effective doubling exponents of `C_θ(t)` are `<-2`, and
the trapezoidal Cook tail's last two contribution ratios are `<0.30`.
*Predicted mechanism (⟨1⟩5.⟨2⟩4 regime (i)):* the dominant factor is
`Σ_{|m|≥ε_v t/2}|h(m)|`, which is `O(t^{-∞})` here, so `C_θ` should fall faster
than any power until it hits the FFT/wraparound floor; the gate is stated at
`<-2` to stay well above that floor.

*Red mutation `--red-slow-kernel`:* replace `h` by `h_slow(m):=c⟨m⟩^{-2}` with
`c` fixed by `||h_slow||_1=||h_γ||_1`.  Then
`Σ_{|m|≥R}|h_slow(m)|≍2c/R` with `R≍ε_v t/2`, so `C_θ(t)≍t^{-1}`: the effective
doubling exponent tends to `-1` and the trapezoidal contribution per octave
tends to the constant `c'ln2`, ratio `→1`.  Both gates must FAIL.  A `|m|^{-2}`
kernel is precisely the borderline the r1 hypotheses left open
(`C²(𝕋)⇒o(m^{-2})`, and `∫dtΣ_{|m|>ε_vt}|h(m)|<∞ ⟺ Σ_m|m||h(m)|<∞`), so this
mutation tests exactly the leaf Objection 1 broke.

Neither certificate touches D28-C; that hypothesis is checkable only in a model
with an explicit exact kink frame (D16's `|K(z)⟩` family is the natural
candidate) and is left to a separate certificate.

## 5. MERGE PROPOSALS

### `definitions.md` — append exactly

> **D28 (H-ACE: exact fixed-packet kink--magnon band data).**  Assume
> H-MQG(1)--(3).  In addition:
>
> 1. The kink folium has a covariant positive-energy Hilbert realization
> `(H_{αβ},π_{αβ},U_{αβ})` implementing the commuting infinite-volume time and
> lattice translations.  This is extra structure beyond the state-set
> definition D9/A2.  The vacuum GNS triples are `(H_γ,π_γ,Ω_γ)`, `γ∈{α,β}`
> (D1(d)), with `HΩ_γ=0`; there is no vacuum vector in `H_{αβ}`.
> 2. Its Hamiltonian has an isolated finite-multiplicity kink band with
> dispersion `E_K∈C²(𝕋)` (matrix valued on the finite frame index).  A fixed
> Gram-normalized, translation-covariant finite-core ansatz frame gives an
> **exact** band map `Γ_K`, satisfying `H_{αβ}Γ_K=Γ_KE_K`; it is not merely a
> Rayleigh--Ritz approximation.
> 3. Each relevant vacuum tail `γ∈{α,β}` has an isolated selected magnon band
> `ω_γ` (identified as `ω` when symmetry relates the tails), gap
> `Δ_M:=min_kω(k)>0`, and Gram-normalized **exact** band map `Γ_{M,γ}`.  A
> spacetime-Schwartz energy-momentum filter of a local observable gives
> almost-local creators `a_{γ,b}(n)` with strictly positive energy transfer and
> with the **momentum-filtered normalisation**
> `a_{γ,b}(n)Ω_γ=Γ_{M,γ}(χ_γe_n⊗e_b)`, `e_n(k):=e^{-ikn}`,
> for a fixed filter `χ_γ∈C_c^∞(𝕋)`; translation covariance makes `χ_γ`
> independent of `n`.  This equality, not merely nonzero overlap with the
> band, is part of the exactness hypothesis.  *(A position-delta normalisation
> — the case `χ_γ≡1` — is not assumed and is in fact incompatible with a
> compactly supported energy--momentum filter.)*
> 4. Packet amplitudes are finite sums of `C_c^∞` products and the resulting
> physical packet states lie in the `ℓ¹` class D17.  The dispersions
> are `C^∞` on open neighbourhoods `U_K,U_γ` of their packet momentum supports
> (global `C²` is retained), their kink and magnon velocity supports have
> distance `ε_v>0`, and their signs are: incoming-left `v_M-v_K≥ε_v` at
> `t→-∞`; outgoing-left `v_M-v_K≤-ε_v`; outgoing-right `v_M-v_K≥ε_v` at
> `t→+∞`.  Thus this is a fixed-packet condition and excludes equal velocities
> and the soft endpoint.  **Filter compatibility:** the filters of (3) and the
> kink filter `χ_K∈C_c^∞(𝕋)` satisfy `χ_•≡1` on the corresponding packet
> momentum support and `supp χ_•⊂U_•`; companions `χ̃_•∈C_c^∞(𝕋)` satisfy
> `χ̃_•≡1` on `supp χ_•` and `supp χ̃_•⊂U_•`.  The channel Hamiltonian symbols
> `h_K:=E_Kχ̃_K`, `h_γ:=ω_γχ̃_γ` are then `C^∞(𝕋)` and agree with the
> dispersions on the packet supports.
> 5. **(Two-cluster factorization through the vacuum tails.)**  Write
> `κ_a^{(0)}(x):=Γ_K(e_x⊗e_a)` for the unfiltered exact kink Wannier vectors.
> There are `C_cl<∞` and `λ̃∈(max(λ_{E_α},λ_{E_β}),1)` (D1(c)) such that for
> every `γ∈{α,β}`, all frame indices `a,a'`, all `x,x'∈ℤ`, every `r≥1`, and
> every pair `A∈𝔄_{Λ_α}`, `B∈𝔄_{Λ_β}` with `Λ_α⊂(-∞,min(x,x')-r]` on the `α`
> side and `Λ_β⊂[max(x,x')+r,∞)` on the `β` side (either factor may be `1`) —
>
>   `|⟨κ_a^{(0)}(x),ABκ_{a'}^{(0)}(x')⟩ - ω_α(A)ω_β(B)⟨κ_a^{(0)}(x),κ_{a'}^{(0)}(x')⟩| ≤ C_cl||A||\,||B||\,λ̃^r`.  **(D28-C)**
>
> The one-tail case is `B=1` (or `A=1`), where `ω(1)=1`; the genuinely two-sided
> case is used only in ⟨1⟩6.⟨2⟩3.  `C_cl` and `λ̃` depend on the model and the
> frame only: **not** on
> `A,B,Λ_α,Λ_β,r,x,x',a,a'`, and in particular not on any time parameter (the positions
> are packet-driven and time dependent downstream).  This is the localization
> input that turns exact band equations into a two-cluster estimate; isolated
> eigenvalues alone do not imply it.  It is the sole replacement for the vacuum
> clustering apparatus of `refs/arxiv-1412.2970` (Lemma `clustering-lemma`,
> Theorem `clustering`); no four-point analogue of `(full-decay)` is assumed.
>
> The asymptotic channel Hamiltonian is multiplication by `E_K(p)+ω_γ(k)`.
> Smooth packet domains with the three velocity signs are denoted
> `D_-^L,D_+^L,D_+^T`; `P_L,P_T` are the two outgoing direct-sum projections.
>
> **Remark D28-R (regime fence; NOT a hypothesis of AC-EX).**  Put
> `K_-:=min E_K`, `K_+:=max E_K`, `W_K:=K_+-K_-`, and let `I_in` be the range
> of `E_K(p)+ω(k)` on the incoming packet support.  Same-band kink absorption
> is excluded by `d_abs:=dist(I_in,[K_-,K_+])>0`; the packet-independent
> sufficient condition is `Δ_M>W_K`.  With `Δ_r:=min_kω_r(k)` for every other
> known one-particle vacuum band and `K_*:=inf_{j≥2,p}E_{K,j}(p)` for every
> other known kink band, `sup I_in+η_inel<Θ_inel` where
> `Θ_inel:=min{K_-+2Δ_M,K_*,inf_r(K_-+Δ_r)}` and `η_inel>0`; absent entries are
> `+∞`.  The three entries respectively exclude an additional magnon, a
> higher-kink absorption channel, and a different one-particle channel.  An
> uncomputed wall--magnon bound band is not excluded.
> **These inequalities are used nowhere in the proof of AC-EX.**  Their role is
> to make the *exactness* hypotheses (2)--(3) physically plausible — an isolated
> exact band is not to be expected when a competing channel is open — so they
> belong to the justification of D28, not to its inferential content.  Adding
> or deleting them changes no step of `theory/ansatz-scattering.md`.

### `claims/CLAIMS.md` — append exactly

| AC-EX | Under D28/H-ACE's **exact** ansatz-band, sector-covariance, momentum-filtered-frame, velocity-separation, and displayed two-cluster hypotheses (D28-C), the fixed-packet kink--magnon Cook limits exist and are isometries; `N_T` is a projection on the constructed out-space.  **Conditionally on the named local-decay hypothesis (AD3-ex)**, on vectors lying in both the constructed in- and out-ranges the T1 measure has constructed support `{0,2}` with `p_2=⟨N_T⟩`.  No completeness, raw-band-data implication, bound-state exclusion, threshold-inequality use, or soft limit is claimed. | SKETCH | D1, D5, D9, D10, D13, D14, D17, B3, D28 | theory/ansatz-scattering.md | ACE-C1, ACE-C2 (specified in shard; not yet implemented) |

*(Objection 8.)*  `M-quant-G` is **not** a dependency: ⟨1⟩7 uses B3 and Lane
T1's ledger formula, not M-quant-G's conclusion.  When Lane T1's row (M-INDEX)
merges, add it to depends-on in place of the bracketed reference in ⟨1⟩7.⟨2⟩3.
`(AD3-ex)` should be recorded as its own row at status CONJECTURE, with
`where-proved` empty and the missing lemma named **ACE-LD**.

### `notation.md` — append exactly

| `Γ_K`, `Γ_{M,γ}` | exact Gram-normalized kink and tail-magnon band maps assumed by H-ACE | definitions.md D28 |
| `E_K`, `K_-`, `K_+`, `W_K`, `Δ_M` | kink dispersion, its extrema and bandwidth, and the selected magnon gap | definitions.md D28 |
| `χ_K,χ_γ,χ̃_K,χ̃_γ` | momentum filters and their companions fixing the filtered frames and kernels | definitions.md D28(3),(4) |
| `h_K,h_γ` | filtered hopping kernels (Fourier coefficients of `E_Kχ̃_K`, `ω_γχ̃_γ`); rapidly decreasing | definitions.md D28(4) |
| `κ_a(x)`, `κ_a^{(0)}(x)` | filtered and unfiltered exact kink Wannier vectors | theory/ansatz-scattering.md (C2) |
| `θ_c` | fixed smooth monotone channel cutoff, transition width `w` | theory/ansatz-scattering.md ⟨1⟩5.⟨2⟩1 |
| `ε_v`, `d_abs`, `Θ_inel`, `η_inel` | velocity gap, same-kink absorption gap, known inelastic threshold, and its margin (last three: fence only, Remark D28-R) | definitions.md D28 |
| `D_-^L`, `D_+^L`, `D_+^T` | incoming-left, outgoing-left, and outgoing-transmitted fixed-packet domains | definitions.md D28 |
| `H_out^{ex}`, `N_T^{ex}` | constructed outgoing range and its transmitted-channel projection; no completeness implied | theory/ansatz-scattering.md ACE.2 |

## 6. REPAIR RESPONSE — `theory/verdicts/ansatz-scattering-r1.md`

**Hypothesis numbering map (r1 → r2), for the diff.**  `P(1)–P(4)` keep their
numbers (P(3) and P(4) have amended text, marked below).  r1 `P(5)` (thresholds)
is **withdrawn as a hypothesis** and reappears as **Remark D28-R**.  r1 `P(6)`
(clustering substitute) becomes `P(5)`, displayed as **(D28-C)**; the display tag
carries no number, so a later renumbering cannot silently break citations.  Every
`D28-P(6)` of r1 therefore reads `D28-P(5)` here, and no r2 citation of `P(5)`
means the thresholds.

| Obj | Severity | Disposition | Exact edit location |
|---|---|---|---|
| 1 | MAJOR | **FIXED** by repair (R2), the momentum-filtered frame — *not* by strengthening smoothness. D28-P(3) normalisation `a(n)Ω_γ=Γ_{M,γ}δ_{n,b}` → `Γ_{M,γ}(χ_γe_n⊗e_b)`; kink frame filtered likewise; kernels are now `h_•=`dispersion`·χ̃_•∈C^∞(𝕋)`. Global `C²` is retained (no strengthening); the local-`C^∞` clause was already in D28-P(4). | §0.1(C2); ⟨1⟩3 PROVE(b,d), ⟨2⟩3, ⟨2⟩4 (**ACE-filter**), ⟨2⟩5; ⟨1⟩5.⟨2⟩1--⟨2⟩4 (the `T_M,T_K` estimate is now written out in full, with the failure mode of the r1 argument stated); D28(3),(4) merge text; new checker **ACE-C2**. |
| 2 | MAJOR | **RETRACTED as a hypothesis / DOWNGRADED to a remark.** The threshold inequalities are moved out of the numbered hypotheses into **Remark D28-R**, labelled "used nowhere in the proof". Claims row and checker prose realigned; `--red-absorption` demoted to a fence regression guard. | D28 merge text (former item 5 → Remark D28-R); §4 ACE-C1 closing paragraph; claims row wording ("threshold-inequality use ... not claimed"). Former item 6 renumbered to item 5. |
| 3 | MAJOR | **FIXED** — displayed as inequality **(D28-C)** with explicit quantifiers, constants `C_cl,λ̃`, the exact objects bounded, the side/separation condition, and position/frame/time uniformity. The multi-cluster form the critic asked for is now **derived** (⟨1⟩6.⟨2⟩1) from the single cut plus almost-locality, so no iterated-factorization hypothesis is assumed; the filtered-frame version is derived in ⟨1⟩3.⟨2⟩6. | D28 merge item 5 (D28-C); ⟨1⟩3.⟨2⟩6 (**ACE-tail**); ⟨1⟩6.⟨2⟩1 (**ACE-Gram**); ⟨1⟩2.⟨2⟩3 (records that `(full-decay)` is not imported). |
| 4 | MAJOR | **DOWNGRADED.** ACE.3 is now explicitly conditional on the named hypothesis **(AD3-ex)**, displayed in ⟨1⟩7's ASSUME, flagged in the theorem statement, the claims row, and HONEST STATUS. The missing lemma is named **ACE-LD** with the exact gap stated (boundary-straddling charge on `∂W`). The cross-term half of the critic's reconstruction *is* proved (⟨1⟩7.⟨2⟩2), so only channel-diagonality is hypothesised. | Theorem preamble and ACE.3 statement; ⟨1⟩7 heading, ASSUME block, ⟨2⟩2; claims row; HONEST STATUS ¶2. |
| 5 | MINOR | **FIXED** — `θ_c` defined: `C^∞`, monotone, `θ'` supported in `[-w,w]`, `||θ'||_∞≤C/w`, fixed profile independent of `t`. The width `w` enters ⟨1⟩4.⟨2⟩3 and the two regimes of ⟨1⟩5.⟨2⟩4. | ⟨1⟩5.⟨2⟩1; ⟨1⟩4.⟨2⟩3; notation merge row. |
| 6 | MINOR | **FIXED** — the display is now `ω_γ(D^†D)=||π_γ(D)Ω_γ||²_{H_γ}=0` with the truncation error split out, and a standing convention (C1) forbids transporting `Ω_γ` into `H_{αβ}`. | §0.1(C1); ⟨1⟩3.⟨2⟩4; ⟨1⟩5.⟨2⟩3; D28 merge item 1. |
| 7 | NOTE | **ACKNOWLEDGED, not changed.** The crude `||f_t||_1=O(1+|t|)` is kept (it is used only upward); a parenthetical records the sharp `O(|t|^{1/2})` and that it would give `N≥4` instead of `N≥5`. | ⟨1⟩4.⟨2⟩2. |
| 8 | NOTE | **FIXED** — `M-quant-G` removed from depends-on; ⟨1⟩7.⟨2⟩3 now cites B3 plus Lane T1's ledger formula, with a note to add the M-INDEX row on merge. | Claims row; ⟨1⟩7.⟨2⟩3; note under the claims merge block. |

**No silent strengthening.**  The only hypothesis changes are: (i) D28-P(3)'s
creator normalisation, replaced by the filtered one (weaker on the momentum
range reached, and required for internal consistency of D28-P(3) itself);
(ii) D28-P(4) gains the filter-compatibility clause, which is a *choice* of
`χ_•,χ̃_•` made possible by the local-`C^∞` clause already present in r1 — it
adds no regularity demand; (iii) former P(5) deleted from the hypothesis
package (strictly weaker); (iv) former P(6) sharpened into (D28-C) — this is
the one place where the hypothesis became *more specific*, as demanded, and its
strength is now visible.  (D28-C) is displayed in the **two-sided** form
`O=AB` because ⟨1⟩6.⟨2⟩3 genuinely needs both tails at once; this matches r1
P(6)'s own wording ("observables separated onto **either** tail") but is
formally stronger than a one-sided display would be, and the r2 critic should
price it as such.  (v) ACE.3 gained the hypothesis `(AD3-ex)`, i.e. the
conclusion was weakened.  Nothing else in the argument was altered; ⟨1⟩1,
⟨1⟩2, ⟨1⟩4 and ⟨1⟩6.⟨2⟩3--⟨2⟩5 are unchanged in content.

**Self-reported L2 violation.**  The repaired shard is ~740 lines against L2's
200--500.  The overrun is entirely §5 (MERGE PROPOSALS) plus §6 (this repair
response); the proof proper (§0--§3) is ~400 lines.  Proposed remedy at merge
time, not taken here because `theory/ansatz-scattering.md` is this lane's only
writable file: move §5 to `theory/merge/ace-d28.md` and §6 to
`theory/verdicts/ansatz-scattering-r2-response.md`.

## 7. HONEST STATUS

**Proved (from D28-P).**  ACE.1 and ACE.2: the Cook/isometry implication,
including the MPS two-cluster replacement for vacuum clustering.  The Cook
majorant now closes: `O(|t|^{2-N})` for every `N`, from rapidly decreasing
*filtered* kernels (⟨1⟩3.⟨2⟩3), the exactly vanishing defect (⟨1⟩3.⟨2⟩4), and
cone separation (⟨1⟩4).  The four-cluster Gram factorization is derived, not
assumed.

**Conditional.**  ACE.3 holds only under `(AD3-ex)` (⟨1⟩7).  The missing lemma
**ACE-LD** is: *from ⟨1⟩3--⟨1⟩4, deduce that the window-charge spectral
projection of the constructed channel states becomes channel-diagonal in the
`t→+∞`-then-`W↑ℤ` order.*  Cone decay and almost-locality push the dressing out
of any fixed `W` at rate `O(|t|^{-N})`, but the charge straddling `∂W` is not
controlled by anything in this shard.  Until **ACE-LD** is proved, the bridge
from T2's constructed channels to T1's outcome measure is a hypothesis, and
should be recorded in the DAG as such.

**Assumed, and not supplied by the excitation ansatz.**  The raw generalized
eigenvalues of refs 1103.2286/1810.07006 do **not** prove D28-P: exact band
invariance, covariant kink-sector implementation, exact filtered frames, and
the displayed two-cluster inequality (D28-C) are assumptions.  (D28-C) is the
load-bearing one — it is the campaign's flagged "the adaptation IS the theorem"
ingredient — and it is now at least a checkable statement rather than a
gesture; it is plausibly satisfiable on D16's XXZ kink, where the `|K(z)⟩`
family gives an exact flat kink band with finite-core one-magnon states over
either product vacuum, but this shard does not verify it there.

**Explicitly not used.**  The inelastic/absorption threshold inequalities
(Remark D28-R) enter no step.  They fence the physical regime in which the
exactness hypotheses are plausible; they are not premises of AC-EX, and the
`--red-absorption` mutation tests only their arithmetic.

**Not claimed anywhere.**  No soft (`k→0`), plane-wave, equal-velocity,
packet-uniform, model-uniform, density, or asymptotic-completeness statement.
The general obstruction remains precise: without a covariant localized exact
kink frame the cancellation **ACE-Cook** cannot even be formulated; without
(D28-C) its vacuum-zero defect need not be small on a kink; and without a
momentum filter the hopping kernels are not summable enough for Cook's
criterion, which is what the r1 loop found.
