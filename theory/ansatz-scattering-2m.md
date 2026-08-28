<!-- ROLE: Lane-S2 proposer shard for AC-EX-2M.  Shared definitions, notation,
     and claim rows below are proposals only.  Status can be promoted only by
     the L6 proposer/critic loop. -->

# AC-EX-2M — fixed-packet two-magnon wave operators from exact ansatz bands

**Proposer status:** **SKETCH**.  Parts (A2M.1)--(A2M.2) are proved as the
conditional implication from proposed D31.  Part (A2M.3) proves an
unconditional **diagonal-order** bounded-family/weak-limit-point statement.
For the asymptotic-leg reading of the D29 interface, `(ACE2M-LSZ)` is a theorem
by creator-choice independence; it is not a claim about a fixed-time charge
insertion.  An iterated-order first jet is conditional on `(ACE2M-SR)`.  No
soft-uniform Cook estimate is claimed.

## 0. Theorem and fixed-packet fence

### ⟨1⟩1. THEOREM AC-EX-2M

**ASSUME.** Proposed D31 `(H-ACE2M)` below.  Thus there is one D1 injective,
translation-invariant MPS vacuum `ω_A`, one exact selected magnon band
`ω(k)`, exact momentum-filtered creators, and two smooth compact packet
supports `K_1,K_2` whose nonzero velocity supports are separated by
`ε_v>0`.  Let

`ℋ_{0,12}:=L²(K_1;ℂ^m)⊗L²(K_2;ℂ^m)`,
`H_{0,12}:=ω⊗1+1⊗ω`,

on the smooth product core `𝒟_{12}`; the two slots are labels for the two
disjoint packet windows, not distinguishable particle species.

For (A2M.3) additionally assume the D29 interface clauses 1--5 in ⟨1⟩8.
In particular (D29-den) and the one-particle normalization (2M-1P) are
displayed interface hypotheses, not consequences of D31.  `(ACE2M-SR)` is
assumed only for the iterated first-jet conclusion.

**PROVE.**

1. **(A2M.1)** The fixed-packet limits

   `W_±F:=lim_{t→±∞}e^{itH}I e^{-itH_{0,12}}F`

   exist for `F∈𝒟_{12}`, where `I` is the two-creator identification in
   ⟨1⟩5.  A soft scale may label the fixed packet, but no `ε→0` operation
   occurs inside this limit.
2. **(A2M.2)** `W_±` are isometries and intertwine joint time/space
   translations.  Their ranges avoid every D31-listed bound-band projection.
   On D6--D8, `W_+^*W_-` is exactly multiplication by D7's physical
   outgoing/incoming coefficient; a fixed packet range lies in the matching
   part of ML2's scattering summand, not its two-string summand.
3. **(A2M.3)** The data are defined for every fixed soft packet scale `ε>0`
   satisfying D31.  For every sequence of full index tuples
   `(N_r,W_r,σ_r,t_r,ε_r)` in the D29 interface family, respecting the
   precedence in (D29-order) and with `ε_r↓0`, the corresponding data are
   bounded in `L²(I)` and have weakly convergent subsequences.  This is a
   **diagonal-order** statement; no unconditional existence of the iterated
   `N,t,W,σ` limit is asserted.  If D29's charge-created soft leg is an
   asymptotic leg carried through `t→±∞`, creator-choice independence proves
   `(ACE2M-LSZ)` in ⟨1⟩8 and identifies the fixed-`ε` subsequential value
   with the constructed `W_±^(ε)` channel.  The stronger `C¹` first-jet
   statement is conditional on `(ACE2M-SR)`; only its exhaustion-free,
   infinite-chain version is verified on D6--D8.

*Justification.* D1, D3(a), D6--D8, D12(a′), proposed D31, and claim ML2.

### ⟨1⟩2. Fixed-packet and bound-band fence

**ASSUME.** D31.  **PROVE.** Neither the soft endpoint nor the two-string is
hidden in Cook.

**⟨2⟩1. [NEW]** Every estimate fixes `K_1,K_2`.  Cook/Gram constants may
depend on `ε_v` and on the packet-amplitude Schwartz seminorms
`s_N(F):=sup_{0≤j≤N}||∂^jF||_∞`; the later joint-spectral fences
use `d_B,η_inel`.  The parameter `ε_0` is fixed by D31(4) but used by no
estimate in (A2M.1)--(A2M.2).  The seminorms carry the soft-family
divergence.  For a later one-sided profile
`f_ε(k)=ε^{-1/2}f(k/ε)` with `0∉supp f`, first form

`∀ε>0:  W_±^(ε)=lim_{t→±∞}e^{itH}I_εe^{-itH_{0,ε}}`,
with no `ε`-uniform bound.  Indeed

`||∂^jf_ε||_∞=ε^{-j-1/2}||f^{(j)}||_∞`,

so an upper bound for the `N` integrations by parts in **ACE-SP** carries
`ε^{-N}` beyond the fixed `L²` normalization (the raw `L∞` seminorm has
the displayed additional `ε^{-1/2}` factor).
*Justification.* D3(a), D12(a′), proposed D31(4), and the limit-order clause
of `briefs/soft-index-target.md`, Lane S2.

**⟨2⟩2. [NEW]** Let `P_B` be the sum of the joint spectral projections of the
D31-listed charge-two bound bands.  Since `W_±` intertwine energy and total
momentum, the fiberwise separation `d_B>0` implies `P_BW_±F=0`.
Like D28's `P_T`, `P_B` is an explicit channel projection; here it fences the
bound summand rather than naming a transmitted summand.
*Justification.* Proposed D31(5), and the standard intertwining computation
proved in ⟨1⟩7.⟨2⟩2.  This is a forward reference without circularity:
none of ⟨1⟩3--⟨1⟩7 uses ⟨1⟩2, so the dependency chain closes independently.

**⟨2⟩3. [NEW — D6 exact fence]** On D6, ML2 gives one bound band.  With its
variables `K=k_1+k_2`, `q=(k_2-k_1)/2`, `c=cos(K/2)`,

`E_sc(K,q)-E_b(K)=J(1+c²-2c cos q)=J|e^{iq}-c|²>0`.
Its only zero has `q=0,c=1`, excluded by D31(4), so compact packets have
`d_B>0`.  Along `k_s→0` at fixed `0<|k_h|<π`,
`ε_v→|v_h|`, `d_B→J sin²(k_h/2)>0`, and `η_inel=+∞`; only
`ε_0` (D31's distance of either velocity set from zero) degenerates, and
`ε_0` is used by no estimate in §§2--3.  ML2 has no
third charge-two summand; `Θ_inel=+∞`.
*Justification.* D6--D8 and ML2 equations (18)--(21),
`theory/ml2-completeness.md` ⟨1⟩5.

**⟨2⟩4. QED.**

## 1. The vacuum clustering upgrade

### ⟨1⟩3. D31-C follows from the D1 transfer gap

**ASSUME.** D1(c,d), with `C,D` local and the right end of `supp C` separated
from the left end of `supp D` by `d_sep≥1` uniform sites.

**PROVE.** For every `λ̃∈(λ_E,1)` there is `C_{A,λ̃}<∞`, independent of the
two support lengths, such that

`|ω_A(CD)-ω_A(C)ω_A(D)|≤C_{A,λ̃}||C|| ||D|| λ̃^{d_sep}`. **(D31-C2)**
**⟨2⟩1. [NEW — named computation MPS-2M-cluster]** In canonical form the
connected contraction is exactly

`⟨l,E_C(E^{d_sep}-P)E_D(r)⟩`,  `P(Y)=tr(Y)r`.
*Justification.* D1(c,d); inserting `P` between the two observable transfer
maps gives separately the two D1(d) contractions, hence their product.

**⟨2⟩2. [NEW]** For a block of length `w`, put
`V_wx:=Σ_s|s⟩⊗A^{s_1}⋯ A^{s_w}x`.  D1(c)'s `l=1` gauge gives
`V_w^†V_w=1`, so `V_w` is an isometry for every `w`.  For every block
operator `O` of length `w_O`, define the contraction
`Ψ_O(Y):=tr_{d^{w_O}}[(O⊗1)V_{w_O}YV_{w_O}^†]=E_O(Y)`.
Then `||Ψ_D(r)||_1≤||D||||r||_1=||D||` and
`|tr Ψ_C(Z)|≤||C||||Z||_1`.  The exact chain identity is

`ω_A(CD)-ω_A(C)ω_A(D)=tr Ψ_C((E^{d_sep}-P)Ψ_D(r))`.

Therefore

`|ω_A(CD)-ω_A(C)ω_A(D)|
 ≤||C||||D|| ||E^{d_sep}-P||_{1→1}`,

uniformly in both support lengths.  D1(c)'s Jordan-safe bound proves
(D31-C2); `C_{A,λ̃}` absorbs the finite-dimensional norm-equivalence
constant between D1(c)'s unnamed norm and `||·||_{1→1}`.

*Justification.* D1(c,d), the displayed Stinespring-isometry computation
**MPS-2M-cluster**, and finite-dimensional norm equivalence.  No bare
`O(λ_E^{d_sep})` is used.

**⟨2⟩3. [ADAPTED — ACE-tail, `ansatz-scattering.md` ⟨1⟩3.⟨2⟩6]** If
`A_i(n)` are uniformly almost-local translates, truncate each at radius
`d_sep/6`.  The errors are `O(d_sep^{-N})`, while the clusters remain
separated by at least `d_sep/3`; (D31-C2) then gives
rapid clustering.  In particular, when `{x,x'}` and `{y,y'}` are ordered
clusters at distance `d_sep`,

`|ω_A(a_2(y)^*a_1(x)^*a_1(x')a_2(y'))
 -G_1(x,x')G_2(y,y')|≤C_N⟨d_sep⟩^{-N}`,  **(D31-C4)**

where `G_i(n,n'):=⟨a_i(n)Ω_A,a_i(n')Ω_A⟩`.  Commuting the two middle
clusters before applying (D31-C2) costs another `O(d_sep^{-N})`.

*Justification.* (D31-C2), proposed D31(3), and
`refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`, §“Arveson spectrum and
almost local observables”, Lemma `commutator-decay` and Theorem
`smearing-theorem`.

**⟨2⟩4. QED.**  Thus, unlike D28-C, D31-C2/C4 are consequences of the
one-vacuum D1 transfer gap and are not independent hypotheses.

## 2. (A2M.1): Cook existence

### ⟨1⟩4. Exact filtered one-particle equations

**ASSUME.** Proposed D31(2)--(4).

**PROVE.** The creator defects annihilate the vacuum and are almost local.

**⟨2⟩1. [VERBATIM PORT — `ansatz-scattering.md` ⟨1⟩3.⟨2⟩2--⟨2⟩3]** A
spacetime-Schwartz filter of a local observable is almost local uniformly
under translation, and the Fourier coefficients of
`h_i:=ωχ̃_i∈C^∞(𝕋)` decrease faster than every power.

*Justification.* Proposed D31(3)--(4) and
`refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`, Theorem
`smearing-theorem`, Lemma `almost-locality`, and equation `(wave-packet)`.

**⟨2⟩2. [VERBATIM PORT — ACE-filter, `ansatz-scattering.md`
⟨1⟩3.⟨2⟩4--⟨2⟩5]** Put

`D_{i,b}(n):=[H,a_{i,b}(n)]-Σ_mh_i(m-n)a_{i,b}(m)`.

Then `D_{i,b}(n)Ω_A=0`, and `D_{i,b}(n)` is almost local about `n`, uniformly
in `n`.

*Justification.* Proposed D31(2)--(4).  Exactness gives
`HΓ_M=Γ_Mω`; filter compatibility gives
`χ_i(ω-ωχ̃_i)=0`; finite range plus rapid kernel decay preserves almost
locality.  This is named computation **ACE-filter**.

**⟨2⟩3. QED.**

### ⟨1⟩5. The two-magnon Cook derivative is integrable

**ASSUME.** ⟨1⟩4 and `F∈𝒟_{12}`.  Define

`IF:=Σ_{x,y,b,c}F^{bc}(x,y)a_{1,b}(x)a_{2,c}(y)Ω_A`.

**PROVE.** `||(HI-IH_{0,12})e^{-itH_{0,12}}F||` is integrable at both time
ends.

**⟨2⟩1. [ADAPTED — ACE-Cook, `ansatz-scattering.md` ⟨1⟩5.⟨2⟩2]** Directly
expand `H a_1a_2Ω_A` and cancel both filtered free convolutions.  Since
`D_2(y)Ω_A=0` and `D_1(x)Ω_A=0`,

`(HI-IH_0)F=Σ_{x,y}F(x,y)[D_1(x),a_2(y)]Ω_A`.  **(2M-Cook)**

This is simpler than kink ACE-Cook: there is no channel cutoff `θ_c`, hence
no `T_M` or `T_K` commutator with a hopping kernel.

*Justification.* Proposed D31(3)'s compact energy--momentum transfer puts
`a_1(x)a_2(y)Ω_A` in a bounded spectral subspace and hence in `Dom H`;
⟨1⟩4.⟨2⟩2 and the product commutator identity then apply.  This is the named
computation **2M-Cook**.

**⟨2⟩2. [ADAPTED — ACE-tail]** For every `N`,
`||[D_1(x),a_2(y)]||≤C_N⟨x-y⟩^{-N}`.

*Justification.* Uniform almost locality from ⟨1⟩4 and
`refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`, Lemma
`commutator-decay`.  No vacuum clustering is needed for this Cook leaf.

**⟨2⟩3. [VERBATIM PORT — ACE-SP, `ansatz-scattering.md` ⟨1⟩4]** Outside
each packet's velocity cone the real-space free packet is
`O(⟨|x|+|t|⟩^{-N})`; its outside-cone `ℓ¹` norm is `O(|t|^{1-N})`, while its
full `ℓ¹` norm is `O(1+|t|)`.  On the product of the two main cones,
`|x-y|≥ε_v|t|/2` for large `|t|`.

*Justification.* Proposed D31(4), named computation **ACE-SP**, and
`refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`, Proposition
`norm-corollary`, equation `(non-stationary)`.

**⟨2⟩4. [ADAPTED — `ansatz-scattering.md` ⟨1⟩5.⟨2⟩5]** Apply (2M-Cook) and
split into the product cones and their complement.  The first part is at most
`C_N|t|²⟨ε_v|t|/2⟩^{-N}`; the complement is `O(|t|^{2-N})`.  Taking `N≥5`
gives an integrable `C|t|^{-3}` majorant.  Here
`C_N=C_N(ε_v,s_N(F))` has the packet-seminorm dependence and soft-family
divergence displayed in ⟨1⟩2.⟨2⟩1.  In particular `ε_0` occurs in no Cook
constant; `d_B,η_inel` enter only the later joint-spectral fences.

*Justification.* ⟨2⟩2--⟨2⟩3 and the same cone sum as named computation
**ACE-Cook** in `theory/ansatz-scattering.md` ⟨1⟩5.⟨2⟩5.

**⟨2⟩5. [ADAPTED — source Haag--Ruelle Cook step]** Since

`d(e^{itH}Ie^{-itH_0}F)/dt=i e^{itH}(HI-IH_0)e^{-itH_0}F`,

the fundamental theorem of calculus and ⟨2⟩4 give both strong limits.

*Justification.* `refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`, §“Scattering
states and their Fock space structure”, Theorem `Haag-Ruelle`, equation
`(scattering-state)` and its first proof paragraph.  The source uses
`HR-auxiliary(a)` to kill the one-particle derivative; exact ansatz equations
and **2M-Cook** replace precisely that source hypothesis here.

**⟨2⟩6. QED.**  This proves (A2M.1).

## 3. (A2M.2): isometry and the ML2 exact-match anchor

### ⟨1⟩6. The limiting maps are isometries

**ASSUME.** ⟨1⟩3--⟨1⟩5.

**PROVE.** `⟨W_±F,W_±G⟩=⟨F,G⟩` on `𝒟_{12}`.

**⟨2⟩1. [ADAPTED — ACE-Gram, `ansatz-scattering.md` ⟨1⟩6.⟨2⟩1]** On the
product velocity cones, apply (D31-C4) to the four-creator scalar product.
Because each exact band map is Gram-normalized and `χ_i=1` on its packet
support, the factorized limit is the tensor-product free Gram form.

*Justification.* ⟨1⟩3.⟨2⟩3 and proposed D31(2)--(4).  This is named
computation **2M-Gram**, the one-vacuum adaptation of **ACE-Gram**.

**⟨2⟩2. [ADAPTED — ACE-SP]** The complement of the product cones contributes
`O(|t|^{4-N})`; summing (D31-C4) on the main cones contributes
`O(|t|⁴⟨ε_v|t|/2⟩^{-N})`.  Hence

`lim_{t→±∞}⟨Ie^{-itH_0}F,Ie^{-itH_0}G⟩=⟨F,G⟩`.

*Justification.* **2M-Gram** and ⟨1⟩5.⟨2⟩3's **ACE-SP** bounds.

**⟨2⟩3. [VERBATIM PORT — `ansatz-scattering.md` ⟨1⟩6.⟨2⟩2]** Unitarity of
`e^{itH}` and strong convergence now imply `||W_±F||=||F||`; polarization
gives the displayed scalar-product identity, and the maps extend uniquely to
the packet-domain closures.

*Justification.* ⟨2⟩2 and the Hilbert-space polarization identity.

**⟨2⟩4. QED.**

### ⟨1⟩7. Intertwining, bound isolation, and D6--D8 exact match

**ASSUME.** ⟨1⟩5--⟨1⟩6.

**PROVE.** The conclusions of (A2M.2), including the ML2 anchor.

**⟨2⟩1. [VERBATIM PORT — `ansatz-scattering.md` ⟨1⟩6.⟨2⟩4]** Replacing `t`
by `t+s` in the defining limit gives
`e^{isH}W_±=W_±e^{isH_0}`.

*Justification.* The group laws and existence of the limits in ⟨1⟩5.

**⟨2⟩2. [ADAPTED]** Translation covariance of `a_i(n)` gives the analogous
total-momentum intertwining.  Joint functional calculus then proves
`P_BW_±=0` from D31's fiberwise `d_B>0`, and proves orthogonality to every
listed inelastic channel below `Θ_inel`.

*Justification.* Proposed D31(1),(3),(5), ⟨2⟩1, and the SNAG joint spectral
calculus used in `refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`, equation
`(SNAG)` and Definition `wave-definition`.

**⟨2⟩3. [NEW — exact ML2 match]** Specialize to D6--D8.  ML2's generalized
eigenfunction is

`Ψ^sc_{Kq}(x,x+r)=(e^{iK(x+r/2)}/2π)[S(K,q)e^{iqr}+e^{-iqr}]`,

with `k_1=K/2-q`, `k_2=K/2+q`, `S(K,q)=S_{12}` and the exact resolution
(21).  Here every torus pair is first put in ML2's chart by the unique data

`K^♯=Arg(e^{i(k_1+k_2)})∈(-π,π]`, `q^♯∈(0,π)`,

for which
`{e^{i(K^♯/2-q^♯)},e^{i(K^♯/2+q^♯)}}={e^{ik_1},e^{ik_2}}`.
The branch labels and the following in/out assignment are stated in this
fundamental domain; the odd-`r` anti-periodicity under a different `K` lift
changes the fiber gauge, not `S_phys`.  If `v(k_2)>v(k_1)`, stationary phase
puts the `e^{-iqr}` term in the
incoming region (`k_2` on the left at `t→-∞`) and the `e^{iqr}` term in the
outgoing region.  Therefore

`W_-f=𝒰_sc^{-1}f`, `W_+g=𝒰_sc^{-1}(S_{12}^{-1}g)`, and
`W_+^*W_-f=S_{12}f`.

If the velocity order is reversed, the same computation gives `S_{21}`.
Thus the constructed labels are exactly D7's physical out/in labels, not a
new convention.  Moreover `|S(K,q)|=1` by ML2 (18), since `c` is real, so
the adjoint computation in the last displayed identity is valid.

*Justification.* D7; ML2 equations (15), (17)--(21), proved without Bethe
completeness in `theory/ml2-completeness.md` ⟨1⟩5; and **ACE-SP** stationary
cone selection.  ML2 (15) supplies the fundamental-domain/anti-periodicity
rule, and D7 supplies the explicit incoming convention.

**⟨2⟩4. [NEW — fixed-pair scope]** For each fixed D31 packet pair on
D6--D8, `ran W_±` is a closed subspace of the matching part of ML2's
`L²(dK,dq)` scattering summand and is orthogonal to its `L²(dK)` bound-band
summand.  Whether varying the creators/windows exhausts the scattering
summand is open; no compatibility across window pairs or asymptotic
completeness is claimed.

*Justification.* ⟨2⟩2--⟨2⟩3, ML2 resolution (21), and proposed D31(5).
The creator-choice-independence clause of source Theorem `Haag-Ruelle` is not
needed to compare or exhaust different packet-window ranges here.  It is
ported only in ⟨1⟩8 for the distinct fixed-pair task of replacing the
asymptotic charge creator by the exact filtered creator.

**⟨2⟩5. QED.**  This proves (A2M.2).

## 4. (A2M.3): nonvacuity bridge to Lane S1

### ⟨1⟩8. The sole D29 interface block and the soft-regularity condition

**INTERFACE ASSUMPTIONS ON LANE S1'S PROPOSED D29 — ALL ARE HERE.**

1. `𝒜_{N,W,σ,t}(ε)` is the normalized **connected** on-shell
   pairing, with and without one normalized charge-created soft leg.  The
   charge leg is an **asymptotic** Haag--Ruelle leg carried through the same
   `t→±∞` operation as the hard leg; it is not the fixed-time action of a
   charge operator on an already prepared hard vector.  In D10(c)'s
   position-profile convention the time-zero insertion is
   `Q[f̂_ε;ξ^-]=Σ_x f̂_ε(x)q_x^-`.  Its on-shell positive-energy
   filter and free packet evolution define an almost-local HR family
   `a_{Q,2,b,t}[f_{ε,t}]`.  The datum is valued in D24(b)'s `L²(I)` hard
   norm and presupposes no wave operator.
2. At fixed `W,σ,ε`, finite-volume local matrix elements converge to D1
   GNS matrix elements before the scattering-time limit; hard
   preparation/resolution converge, when wave operators exist, into
   `ran W_-`/`ran W_+`.
3. Write the amputated datum at an allowed full index tuple `α` as
   `𝒜_α(h)=𝒝_α(h)/𝒟_α(h)`, `h∈I`.  On the **selected hard
   packet** and along the chosen tuple family, assume the displayed uniform
   denominator and numerator bounds

   `ess inf_{α} ess inf_{h∈I}|𝒟_α(h)|≥d_I>0`,
   `sup_α||𝒝_α||_{L²(I)}≤C_I<∞`. **(D29-den)**

   Consequently
   `sup_α||𝒜_α||_{L²(I)}≤C_I/d_I`.  Cauchy--Schwarz for
   the normalized preparation/resolution supplies the second bound; the
   first is the explicit nonzero-amputation hypothesis.
4. The precedence is
   `N→∞ ≺ t→±∞ ≺ (W↑ℤ,σ↓0)_j ≺ ε↓0`.
   **(D29-order)**  No later operation is taken inside an earlier one;
   `W` and `σ` may be exhausted jointly along `j`.  Thus the unconditional
   statement below concerns full-index diagonals respecting this precedence,
   not an asserted iterated `lim_{σ}lim_W`.  Under `(ACE2M-SR)`, the
   `j`-diagonal is a specified specialization and `ε` is then iterated last.
5. **(5a), pairing convention.** Compare D29's connected pairing with hard
   vectors in `ran W_-^(ε)`, `ran W_+^(ε)` and the same soft profile
   `f_ε`; this fixes the pairing, not its value.

   **(5b), one-particle on-shell normalization.**  At fixed `ε>0`, with
   `χ_2=1` on `supp f_ε`, the two admissible HR creator families obey,
   for every scattering time,

   `a_{Q,2,b,t}[f_{ε,t}]Ω_A
     =a_{2,b,t}[f_{ε,t}]Ω_A
     =Γ_M(f_ε⊗e_b)`, **(2M-1P)**

   and their velocity support is disjoint from the selected hard packet by
   D31(4).  Equality (2M-1P) is the normalized one-particle content of the
   D29 on-shell charge leg; it is not an operator equality on hard states.
   No `ε↓0`-uniform estimate is included.

These are the complete interface clauses; reconciliation with Lane S1's final
D29 is an orchestrator task.

**⟨2⟩1. [NEW — D6 one-particle normalization]**

**ASSUME.** D6--D8 and fixed `ε>0`.  **PROVE.** (2M-1P) holds for the D6
charge creator and the D31 filtered creator.

On D6, `q_x^-=S_x^-`, so, with D10(c)'s argument convention,

`Q[f̂_ε;ξ^-]Ω=Σ_x f̂_ε(x)S_x^-Ω
 =Σ_x f̂_ε(x)|x⟩=Γ_M(f_ε)=a_{2,b}[f_ε]Ω`.

The measure is `dk/(2π)`, so `Γ_M` is isometric.  Applying the two
on-shell HR evolutions preserves this vacuum vector for every `t` by the exact
band equation.

*Justification.* D6, D10(c), `soft-current-recon.md` ⟨1⟩1 for
`q_x^-=S_x^-`, proposed D31(2)--(3), and source equation
`(creation-on-vacuum)` in §“Haag--Ruelle creation operators”.

**⟨2⟩2. [PORTED THEOREM — creator-choice independence / `(ACE2M-LSZ)`]**

**ASSUME.** Interface clauses 1, 5(a)--(b), D31(3)--(4), and fixed `ε>0`.
**PROVE.** Replacing the asymptotic charge creator by `a_{2,b}` changes no
fixed-`ε` connected on-shell pairing.

Put `Δ_{2,t}:=a_{Q,2,b,t}[f_{ε,t}]-a_{2,b,t}[f_{ε,t}]`.
By (2M-1P), `Δ_{2,t}Ω_A=0`.  If the soft creator is rightmost in a
two-particle precursor, the precursor difference is therefore zero.  In the
opposite order it is

`Δ_{2,t}a_{1,t}[g_t]Ω_A=[Δ_{2,t},a_{1,t}[g_t]]Ω_A`.

D31(4)'s disjoint velocity supports, almost locality, and the packet cone
estimate make this commutator `O(|t|^{-∞})`.  Hence both `t→+∞` and
`t→-∞` precursor differences vanish in norm.  Pairing either limit with
the same hard out/in vector, and applying the same argument to the disconnected
subtractions, proves equality of the connected on-shell pairings.  This is
`(ACE2M-LSZ)` as an **operator-level asymptotic statement**.

*Justification.* `refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`,
§“Scattering states and their Fock space structure”, Theorem
`Haag-Ruelle`, final clause after equation `(Asymptotic symmetry)`, and its
last proof paragraph; source Lemma `commutators-decay(a)` and
`HR-auxiliary(d)`; D31(3)--(4); ⟨1⟩5--⟨1⟩6.  The displayed
commutator is the source proof specialized to two creators.

This port does **not** identify the raw fixed-time vector
`Q_{k_s}|k_h⟩` with a scattering eigenvector.  On D6 the PROVED identity
`Q_{k_s}|k_h⟩-|B^{in}⟩=(1-S_{12})|P_{12}⟩
=-2ik_s|P_{12}⟩+O(k_s²)` (R8 and R19) remains true.  It is precisely why
clause 1 requires an asymptotic on-shell leg.

*Justification.* Claim S2-2body, `theory/soft-current-recon.md`
⟨1⟩2.⟨2⟩3 (R8) and ⟨1⟩5 (R19).

**(ACE2M-SR).** Apply only the first two D29 operations. Let `j` index `(W_j,σ_j)` with `W_j↑ℤ`, `σ_j↓0`, and at fixed `ε>0` put

`A_j(ε):=lim_{t→±∞}lim_{N→∞}𝒜_{N,W_j,σ_j,t}(ε)∈L²(I)`.

Existence of these two inner limits is part of `(ACE2M-SR)`, not a
consequence of the diagonal boundedness statement.  Require the continuous
extension `A_j(0):=lim_{ε↓0}A_j(ε)`, membership in
`C¹([0,ε_★];L²(I))`, and relative compactness of
`{A_j(ε),∂_εA_j(ε):j,0≤ε≤ε_★}` in `L²(I)`, together with

`lim_{δ↓0}sup_j sup_{|ε-ε'|≤δ}||∂_εA_j(ε)-∂_εA_j(ε')||_{L²(I)}=0`. **(SR)**

This amplitude-data condition is not a Cook-integrand hypothesis, but it is uniform in `j` down to `ε=0` and therefore is genuine non-Cook soft uniformity.

*Justification.* D24(b), D3(a), D12(a′), and the order mandated by
`briefs/soft-index-target.md`, Lane S2.

### ⟨1⟩9. Constructed-channel limit points

**ASSUME.** D31 and the D29 interface block; assume `(ACE2M-SR)` only for
the iterated first-jet conclusion.

**PROVE.** (A2M.3).

**⟨2⟩1. [NEW — diagonal bounded-family core]** For any full-index sequence
`α_r=(N_r,W_r,σ_r,t_r,ε_r)` respecting (D29-order), with `ε_r↓0`,
interface clause 3 gives

`sup_r||𝒜_{α_r}||_{L²(I)}≤C_I/d_I`.

Reflexivity of `L²(I)` therefore gives a weakly convergent subsequence.
This proves exactly the diagonal statement in (A2M.3); it neither forms nor
asserts the inner iterated-limit object and does not use `W_±`.

*Justification.* D29 interface clauses 1 and 3, (D29-den), and weak sequential
compactness of bounded sets in the reflexive space `L²(I)`.

**⟨2⟩2. [ADAPTED — fixed-packet AC-EX bridge]** At fixed `ε>0`, ⟨1⟩5
supplies `W_±^(ε)`.  The proved creator-independence theorem
`(ACE2M-LSZ)` in ⟨1⟩8.⟨2⟩2 replaces (5a)'s asymptotic charge creator
by the D31(3) creator without changing the connected pairing.  Thus every
fixed-`ε` subsequential value for which the hard preparation/resolution
converges is the constructed-channel value.  Wave operators enter (A2M.3)
only here.

*Justification.* (A2M.1)--(A2M.2), interface clauses 2 and 5,
and ⟨1⟩8.⟨2⟩2.

**⟨2⟩3. [NEW]** Under `(SR)`, Banach-valued Arzelà--Ascoli gives
`j_ℓ` converging in `C¹([0,ε_★];L²(I))`; Lane S1's TGT first jet
exists with last operation

`lim_{ε↓0}[lim_{ℓ→∞}lim_{t→±∞}lim_{N→∞}
 𝒜_{N,W_{j_ℓ},σ_{j_ℓ},t}(ε)]`.

No `ε→0` limit is taken inside ⟨1⟩5's Cook integral; `ε` is a fixed packet parameter there, with constants diverging as `ε↓0`.

*Justification.* `(ACE2M-SR)`, D29-order, and Arzelà--Ascoli in the
relatively compact metric target specified by `(SR)`.

**⟨2⟩4. [NEW — D6 satisfies D31]**

**ASSUME.** D6 and fixed compact packets obeying D31(4).  **PROVE.** D6 is a
nonempty instance of D31(1)--(5).

The all-up state is the `χ=1` injective product MPS; its transfer map has no
nontrivial peripheral block.  The shifted D6 Hamiltonian is positive,
`HΩ=0`, and in its finite-excitation GNS space has no normalizable zero-energy
vector beyond `Ω`: equality in every positive swap bond forces a fixed-`n`
coordinate wave to be constant under adjacent exchanges/translations, and
that constant is not in `ℓ²` for `n≥1`.  `S^z` supplies the conserved circle
grading.  The map
`Γ_Mg=∫(dk/2π)g(k)Σ_xe^{ikx}|x⟩` is isometric and obeys
`HΓ_M=Γ_Mω`; in charge one it is the entire scalar band.  A
spacetime-Schwartz filter of `S_n^-` gives D31(3)'s covariant creators and can
be chosen equal to one on either fixed packet.  Compact separated packet
supports give D31(4).  Finally ML2 gives exactly the scattering and one bound
summand; ⟨1⟩2.⟨2⟩3 proves `d_B>0`, while the alternative propagating
inventory is empty and `η_inel=+∞`.

*Justification.* D1, D6's positive swap form, proposed D31, ML2 equations
(17)--(21), and the Plancherel resolution ML2 (21).  This is a direct
verification, not an appeal to Bethe completeness or to integrability.

**⟨2⟩5. [NEW — D6 exhaustion-free first jet]**

**ASSUME.** D6--D8, `I=[a,b]⋐(0,π)`, and D24(b)'s normalized packet
multiplier convention.  **PROVE.** The `j`-independent infinite-chain datum is
`C¹` at `ε=0` and has a nonempty limit-point set.

Normalize `f` in `L²` and put
`dμ_f(u)=|f(u)|²du`, `m_1=∫u dμ_f(u)`.  For the exact D7
multiplier, the packet-amputated datum is

`A(ε)(h)=∫dμ_f(u) S_phys(εu,h)`.

S2-2body's compact-hard Taylor remainder and D24(b)'s product-packet norm give

`A(ε)=A(0)+εm_1∂_{k_s}S_phys(0,·)+O_{L²(I)}(ε²)`.

Thus `A∈C¹([0,ε_★];L²(I))`; a singleton family is relatively
compact and has an equicontinuous first jet.  This uses the normalized
multiplier amputation of D24(b), with no extra `ε^{-1}` factor.

*Justification.* Claims S2-2body and ML2, D24(b), and the exact-match
computations ⟨1⟩7.⟨2⟩3 and ⟨1⟩8.⟨2⟩1--⟨2⟩2.  S2-2body is proved
from the two-body contact equations; no integrability hypothesis enters.

**⟨2⟩6. [NEW — scope]** D31 alone does not imply `(SR)`: fixed-packet
Cook constants diverge through the packet seminorms and control neither an
on-shell first derivative nor the `(W,σ)` exhaustion.  The `(W,σ)`-uniform
version is open on every model, D6 included.  Creator independence proves
`(ACE2M-LSZ)` only for the asymptotic-leg interface; a fixed-time insertion
retains the R8 branch term displayed in ⟨1⟩8.⟨2⟩2.

*Justification.* ⟨1⟩2.⟨2⟩1, ⟨1⟩5's **ACE-SP**, and the ML3/ML6
CONJECTURE rows in `claims/CLAIMS.md`.

**⟨2⟩7. QED.**  This proves (A2M.3) at the stated diagonal/conditional
strength.

## 5. Reference-hypothesis audit

### ⟨1⟩10. What the exact ansatz replaces

**ASSUME.** D31.  **PROVE.** No source hypothesis is imported silently.

**⟨2⟩1. [ADAPTED]** D31(1)--(3)'s positive-energy GNS representation, exact band map isolated within the
charge-one sector, and filtered creators replace the source's isolated mass shell and `B_t^*(g_t)Ω=B^*(g)Ω`.  *Justification.*
`refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`, Definitions `mass-shell-definition`, `HR-creation-operators`, Lemma
`HR-auxiliary(a)`, and equation `(creation-on-vacuum)`.

**⟨2⟩2. [NEW/ADAPTED]** D1 plus **MPS-2M-cluster** replaces Hamiltonian-gap clustering, permitting gapless D6; D31's local
smoothness/separated velocities replace global regularity.  Density, full-Fock, and completeness arguments are not ported.
*Justification.* D1(c,d), D6, ⟨1⟩3; source Theorem `clustering`, Proposition `norm-corollary`, and Theorems `Haag-Ruelle`,
`Haag-Ruelle-Fock`, `s-matrix`.

**⟨2⟩3. [PORTED, SCOPED]** Source Theorem `Haag-Ruelle`'s final
creator-choice-independence clause is ported in ⟨1⟩8.⟨2⟩2.  Its matching
vacuum-vector and cross-velocity hypotheses are exactly (2M-1P) and D31(4).
It is used only for the asymptotic D29 soft leg.  It is not used to compare
different packet-window ranges in ⟨1⟩7.⟨2⟩4 and supplies no density or
completeness conclusion.

*Justification.* Source §“Scattering states and their Fock space structure”,
Theorem `Haag-Ruelle`, final clause and final proof paragraph; ⟨1⟩8.

**⟨2⟩4. QED.**

## 6. CHECKER SPEC

### A2M-C1 — connected transfer identities on one model

**A2M-C1a (fixed-point subtraction).** Use D23's AKLT tensor
`A^a=σ_a/√3`, `r=I/2`, and Cartesian `S^z`.  At `d=1,…,12`, contract
`C=D=I+S^z` directly, subtract `ω_A(C)ω_A(D)`, and independently evaluate

`⟨l,E_C(E^{d-1}-P)E_D(r)⟩`.

Both **connected** answers must equal `4/3·(-1/3)^d` within `10^-12`, and
each successive ratio must obey `|ratio+1/3|≤10^-8`.  This certifies only
the fixed-point-subtracted connected two-point identity on one model.
**Red `--red-c1a`:** replace `E^{d-1}-P` by `E^{d-1}`; its retained `+1`
must fail both gates.

**A2M-C1b (support-length independence).** For all `w_C,w_D∈{1,2,3}`, take `C_{w_C}=⊗_{j=1}^{w_C}(I+S^z_j)` and likewise `D_{w_D}`, separated by `d_sep∈{2,4,6}` sites. Compare direct and fixed-point-subtracted contractions and, with `λ̃=1/2`, require

`max_{w_C,w_D,d_sep}
 |conn|/(||C_{w_C}||||D_{w_D}||λ̃^{d_sep}) ≤0.1`.

Compute operator norms independently by singular values.  Also require, at
every fixed `d_sep`,

`ratio(w_C,w_D,d_sep)≤ratio(1,1,d_sep)+10^-12`

for all `w_C,w_D∈{1,2,3}`.  **Red `--red-c1b`:** replace the rate by
`λ̃^{d_sep+2(w_C+w_D)}`; the cap must fail.  **Red
`--red-supportfold`:** multiply the fixed-point-subtracted connected numerator
by `w_Cw_D` only in the support-variation calculation; it must disagree by
more than `10^-12` with the independently direct-contraction ratio profile.
The ordinary monotonicity gate is retained, but this profile-agreement gate is
the direct certificate that a support-length factor has not been hidden in
`C_{A,λ̃}`.

**Uncertified scope.** AKLT's transfer map is diagonalizable, so A2M-C1 certifies neither D1(c)'s Jordan-safe `λ̃>λ_E` form nor D31-C4, exact bands, `(ACE2M-LSZ)`, or `(ACE2M-SR)`. Every gate/red mode must use `raise` or `sys.exit`, never bare `assert`; green and red run under `python3 -O`, and every red mode exits nonzero.

## 7. MERGE PROPOSALS

### Exact addition to `definitions.md`

## D31 (H-ACE2M: exact fixed-packet two-magnon data over one vacuum)

Fix one translation-invariant injective canonical MPS tensor `A` and its D1 state/GNS triple `(ω_A,H_A,Ω_A)`. All constructions use this one vacuum representation; no D2(a) covariant vacuum family is required. Assume:

1. A finite-range translation-invariant Hamiltonian generates the dynamics, is implemented in `H_A` by commuting
   positive-energy time/lattice translations, and is normalized by `HΩ_A=0`, `ker H=ℂΩ_A`.  A conserved circle charge
   grades the selected magnon by one unit and the construction lies in its charge-two sector.
2. There is a finite-multiplicity scalar magnon band `ω∈C²(𝕋)`, isolated within the charge-one sector on clause 4's packet neighbourhoods, and a Gram-normalized translation-covariant **exact** map `Γ_M:L²(𝕋;ℂ^m)→H_A` with `HΓ_M=Γ_M(ω⊗1_m)`. The multiplicity is fixed; matrix-valued crossings are outside D31. Exactness is not a Rayleigh--Ritz conclusion.
3. For each packet window, a compact-energy-momentum-supported spacetime-Schwartz filter of a charge-one local observable gives uniformly almost-local positive-energy-transfer creators with `a_{i,b}(n)=τ_n(a_{i,b}(0))`, `a_{i,b}(n)Ω_A=Γ_M(χ_i e_n⊗e_b)`, `e_n(k)=e^{-ikn}`.
4. Packet amplitudes are finite sums of `C_c^∞` products.  The dispersion is `C^∞` on neighbourhoods `U_i` of compact
   supports `K_i`; `V_i=ω'(K_i)` obey `dist(V_1,V_2)≥ε_v>0`, `dist(V_i,{0})≥ε_0>0`.  The latter nonzero-velocity clause is part of the campaign packet register but is used by no estimate in (A2M.1)--(A2M.2); only `ε_v` enters Cook/Gram.  Filters satisfy `χ_i=1` on `K_i`,
   `supp χ_i⊂U_i`; companions satisfy `χ̃_i=1` on `supp χ_i`, `supp χ̃_i⊂U_i`; put `h_i=ωχ̃_i∈C^∞(𝕋)`.
5. Supply an inventory `𝓡_inel` of every alternative propagating charge-two band tuple `r=(r_1,…,r_n)` expressible from
   the stated exact band data, and set `θ_r(K):=inf_{Σp_j=K,Σq_{r_j}=2}Σ_jω_{r_j}(p_j)`.  Put `K_Σ=K_1+K_2` and
   `I_2={(ω(k_1)+ω(k_2),k_1+k_2):k_i∈K_i}`.  For every `r∈𝓡_inel`, require
   `ω(k_1)+ω(k_2)+η_inel<θ_r(k_1+k_2)` for one `η_inel>0` and all `k_i∈K_i`; equivalently, when applicable,
   `sup_{(E,K)∈I_2}E+η_inel<Θ_inel`, `Θ_inel:=inf_{K∈K_Σ,r}θ_r(K)`; absent channels count as `+∞`.  Every charge-two
   bound band in the supplied exact data is isolated by
   `d_B:=inf_{k_i∈K_i,j}|ω(k_1)+ω(k_2)-E_{B,j}(k_1+k_2)|>0`; `P_B` is the sum of its joint spectral projections.
   Bound bands are present but are not incoming/outgoing two-magnon channels.

No clustering inequality is assumed.  D1(c,d) implies, for every `λ̃∈(λ_E,1)` and local `C,D` separated by `d_sep`,

`|ω_A(CD)-ω_A(C)ω_A(D)|≤C_{A,λ̃}||C|| ||D||λ̃^{d_sep}`. **(D31-C2)**

After uniformly almost-local truncation this implies (D31-C4) of `theory/ansatz-scattering-2m.md` ⟨1⟩3.  Both estimates
are consequences, not hypotheses.  The theorem is fixed-packet only; a soft scale and its limit are not part of D31.

### Exact additions to `claims/CLAIMS.md`

| AC-EX-2M | Under D31/H-ACE2M over one D1 injective translation-invariant MPS vacuum, exact momentum-filtered magnon bands and two compact nonzero separated-velocity packets give fixed-packet Cook wave operators `W_±`; D1's transfer gap derives D31-C2, and with D31(3)'s uniform almost-locality also D31-C4, so no independent clustering hypothesis is assumed.  The maps are isometries, intertwine joint translations, and avoid the D31-listed fiberwise-isolated charge-two bound bands.  On D6--D8 a fixed packet range lies in the corresponding part of ML2's Jacobi scattering summand: `W_+^*W_-` carries D7's `S_phys`, while the two-string is orthogonal.  For Lane S1's D29 interface, every full-index sequence respecting (D29-order) is `L²(I)`-bounded under (D29-den) and has weak diagonal subsequences; no unconditional iterated-order object is asserted.  If the charge-created soft leg is carried as an asymptotic HR leg, the ported creator-choice-independence theorem `(ACE2M-LSZ)` identifies its fixed-`ε` value with the constructed channel from the one-particle normalization (2M-1P) and D31(4).  First-jet compactness is conditional on `(ACE2M-SR)`, whose full `(W,σ)`-uniform version is open on every model; D6 verifies D31 and only the exhaustion-free infinite-chain first jet.  No fixed-time charge/scattering-vector equality, soft-uniform Cook bound, equal-velocity/endpoint construction, bound-state wave operator, range exhaustion, or asymptotic completeness is claimed. | SKETCH | D1, D3(a), D6--D8, D10, D12(a′), D24, D31, ML2, S2-2body | theory/ansatz-scattering-2m.md | theory/checks/ansatz_scattering_2m_check.py, A2M-C1a/C1b |

### Exact additions to `notation.md`

| Symbol | Meaning | First fixed in |
|---|---|---|
| `ℋ_{0,12}`, `H_{0,12}`, `𝒟_{12}` | labeled two-packet free magnon channel, sum Hamiltonian, and smooth product core | definitions.md D31; theory/ansatz-scattering-2m.md |
| `K_i`, `V_i`, `a_{i,b}(n)`, `χ_i`, `χ̃_i`, `h_i` | fixed packet supports, velocity supports, exact filtered creators, filters/companions, and rapidly decaying filtered symbols | definitions.md D31 |
| `I_2`, `𝓡_inel`, `Θ_inel`, `η_inel`, `E_{B,j}`, `d_B`, `P_B` | selected two-magnon joint energy--momentum set, inventoried alternative channels and threshold/margin, bound bands, their fiberwise separation, and bound projection | definitions.md D31 |
| `d_sep` | number of uniform transfer sites separating two local/almost-local clusters in D31-C2/C4 | definitions.md D31 |
| `ε_v`, `ε_0`, `s_N(F)` | D31 packet-velocity separation, distance of each packet velocity from zero (unused by A2M.1--A2M.2), and fixed-packet Schwartz seminorm | definitions.md D31(4); theory/ansatz-scattering-2m.md ⟨1⟩2 |
| `V_w`, `Ψ_O` | block Stinespring isometry and block-to-virtual contraction used in MPS-2M-cluster | theory/ansatz-scattering-2m.md ⟨1⟩3.⟨2⟩2 |
| `f_ε`, `Q[f̂_ε;ξ^-]`, `a_{2,b}[f_ε]`, `a_{Q,2,b,t}[f_{ε,t}]` | rescaled momentum packet, D10(c) charge with its position-space Fourier profile, exact filtered packet creator, and asymptotic charge HR creator | theory/ansatz-scattering-2m.md ⟨1⟩2, ⟨1⟩8 |
| `𝒜_α`, `𝒝_α`, `𝒟_α`, `d_I`, `C_I` | D29 full-index amputated datum, numerator, hard denominator, and its selected-packet lower/numerator bounds | theory/ansatz-scattering-2m.md ⟨1⟩8(3) |
| `A_j(ε)`, `ε_★` | post-`N,t` D29 datum along the joint `(W_j,σ_j)` exhaustion and its soft-scale interval endpoint | theory/ansatz-scattering-2m.md ⟨1⟩8 `(ACE2M-SR)` |
| `(ACE2M-LSZ)` | theorem that fixed-`ε` connected on-shell pairings are independent of the asymptotic soft creator when (2M-1P) and cross-velocity separation hold | theory/ansatz-scattering-2m.md ⟨1⟩8.⟨2⟩2 |
| `(ACE2M-SR)` | `j=(W_j,σ_j)`-uniform compact-containment and equicontinuous first jet after existence of the `N,t` limits; a genuine non-Cook soft-uniformity hypothesis | theory/ansatz-scattering-2m.md ⟨1⟩8 |

## 8. HONEST STATUS

**Proved from D31.**  (A2M.1)--(A2M.2): fixed-packet Cook existence, isometry, translation intertwining, separation from
listed bound/inelastic channels, and exact ML2/D7 agreement on D6--D8.  D31-C2/C4 are derived from D1, not assumed.

**Proved diagonal bridge.**  Under the displayed selected-hard-packet
denominator bound (D29-den), the full-index D29 family is `L²(I)`-bounded,
so every sequence respecting (D29-order) has a weakly convergent subsequence.
This is diagonal compactness only; existence of the iterated inner limits is
not claimed.  For an asymptotic D29 charge leg, creator-choice independence
proves `(ACE2M-LSZ)` from (2M-1P) and D31(4).  The raw fixed-time D6 mismatch
(R8) is retained and is outside that theorem.

**Conditional.** Generic iterated first-jet control assumes `(ACE2M-SR)`,
including existence of the `N,t` limits.  ML2/S2-2body verify only its
`j`-independent infinite-chain version, while `(W,σ)`-uniform control is open
even on D6.

**ML1 items still open.**  This shard does **not** close ML1: (i) endpoint packets; (ii) equal velocities; (iii) a
two-string/bound-band wave operator and transitions; (iv) soft-uniform channel norms; (v) general-model range exhaustion.
ML2 supplies only the D6 exact spectral anchor.

**Assumed.** Exact band invariance/creator normalization, positive-energy
covariance, and the threshold inventory are D31 hypotheses, not variational
consequences.  At the D29 interface, asymptotic-HR admissibility of the charge
leg, (2M-1P), and (D29-den) are displayed hypotheses; creator-choice
independence derives `(ACE2M-LSZ)` from them.  Separation from D31-listed bound
bands is derived from `d_B>0`, not assumed.  ML1/ML3/ML6, Bethe completeness,
and soft-uniform Cook estimates are unused.
