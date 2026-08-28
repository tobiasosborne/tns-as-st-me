<!-- ROLE: Lane-S2 proposer shard for AC-EX-2M.  Shared definitions, notation,
     and claim rows below are proposals only.  Status can be promoted only by
     the L6 proposer/critic loop. -->

# AC-EX-2M — fixed-packet two-magnon wave operators from exact ansatz bands

**Proposer status:** **SKETCH**.  Parts (A2M.1)--(A2M.2) are proved as the
conditional implication from proposed D31.  Part (A2M.3) has an unconditional
fixed-packet/value-level core and a clearly isolated soft-regularity
hypothesis; no soft-uniform Cook estimate is claimed.

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

**PROVE.**

1. **(A2M.1)** The fixed-packet limits

   `W_±F:=lim_{t→±∞}e^{itH}I e^{-itH_{0,12}}F`

   exist for `F∈𝒟_{12}`, where `I` is the two-creator identification in
   ⟨1⟩5.  No soft parameter occurs in this limit.
2. **(A2M.2)** `W_±` are isometries and intertwine joint time/space
   translations.  Their ranges avoid every D31-listed bound-band projection.
   On D6--D8, `W_+^*W_-` is exactly multiplication by D7's physical
   outgoing/incoming coefficient; a fixed packet range lies in the matching
   part of ML2's scattering summand, not its two-string summand.
3. **(A2M.3)** For each fixed soft packet scale `ε>0` satisfying D31, Lane
   S1's intended protocol has constructed-channel values.  Those values have
   weak `L²(I)` subsequential limit points with `ε→0` strictly last.  The
   stronger `C¹` limit-point/TGT statement is conditional only on
   `(ACE2M-SR)` in ⟨1⟩8;
   that condition is verified for the D6--D8 exact ML2 anchor.

*Justification.* D1, D3(a), D6--D8, D12(a′), proposed D31, and claim ML2.

### ⟨1⟩2. Fixed-packet and bound-band fence

**ASSUME.** D31.  **PROVE.** Neither the soft endpoint nor the two-string is
hidden in Cook.

**⟨2⟩1. [NEW]** Every estimate fixes `K_1,K_2` and may depend on
`ε_v,ε_0,d_B,η_inel`.  For a later one-sided profile
`f_ε(k)=ε^{-1/2}f(k/ε)` with `0∉supp f`, first form

`∀ε>0:  W_±^(ε)=lim_{t→±∞}e^{itH}I_εe^{-itH_{0,ε}}`,
with no `ε`-uniform bound.
*Justification.* D3(a), D12(a′), D17, and D31(4).

**⟨2⟩2. [NEW]** Let `P_B` be the sum of the joint spectral projections of the
D31-listed charge-two bound bands.  Since `W_±` intertwine energy and total
momentum, the fiberwise separation `d_B>0` implies `P_BW_±F=0`.
Like D28's `P_T`, `P_B` is an explicit channel projection; here it fences the
bound summand rather than naming a transmitted summand.
*Justification.* Proposed D31(5), and the standard intertwining computation
proved in ⟨1⟩7.⟨2⟩2.

**⟨2⟩3. [NEW — D6 exact fence]** On D6, ML2 gives one bound band.  With its
variables `K=k_1+k_2`, `q=(k_2-k_1)/2`, `c=cos(K/2)`,

`E_sc(K,q)-E_b(K)=J(1+c²-2c cos q)=J|e^{iq}-c|²>0`.
Its only zero has `q=0,c=1`, excluded by D31(4), so compact packets have
`d_B>0`.  ML2 has no third charge-two summand; `Θ_inel=+∞`.
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

**⟨2⟩2. [NEW]** The observable transfer maps at either end are bounded by
`C_A||C||` and `C_A||D||`, with `C_A` depending only on the condition numbers
of the fixed points, not on support length.  Therefore D1(c)'s Jordan-safe
bound `||E^{d_sep}-P||≤C_λ̃λ̃^{d_sep}` proves (D31-C2).

*Justification.* D1(c,d): in the `l=1` gauge each finite MPS block is a
Stinespring contraction; conjugating the right environment by `r^{1/2}`
costs only `||r^{1/2}||||r^{-1/2}||`.  This is the named computation
**MPS-2M-cluster**.  No bare `O(λ_E^{d_sep})` is used.

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

`D_{i,b}(n):=[H,a_{i,b}(n)]-Σ_{m,b'}h_{i,b'b}(m-n)a_{i,b'}(m)`.

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

*Justification.* ⟨1⟩4.⟨2⟩2 and the product commutator identity.  This is the
named computation **2M-Cook**.

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
gives an integrable `C|t|^{-3}` majorant.

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
`O(|t|^{2-N})`; summing (D31-C4) on the main cones contributes
`O(|t|²⟨ε_vt/2⟩^{-N})`.  Hence

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
(21).  If `v(k_2)>v(k_1)`, stationary phase puts the `e^{-iqr}` term in the
incoming region (`k_2` on the left at `t→-∞`) and the `e^{iqr}` term in the
outgoing region.  Therefore

`W_-f=𝒰_sc^{-1}f`, `W_+g=𝒰_sc^{-1}(S_{12}^{-1}g)`, and
`W_+^*W_-f=S_{12}f`.

If the velocity order is reversed, the same computation gives `S_{21}`.
Thus the constructed labels are exactly D7's physical out/in labels, not a
new convention.

*Justification.* D7; ML2 equations (17)--(21), proved without Bethe
completeness in `theory/ml2-completeness.md` ⟨1⟩5; and **ACE-SP** stationary
cone selection.  The coefficient assignment is D7's explicit incoming
convention.

**⟨2⟩4. [NEW]** Taking the compatible union over all compact packet windows
avoiding zero/equal velocities gives a dense core in ML2's `L²(dK,dq)`
scattering representation; the excluded sets are null.  On that union the
isometric extensions match ML2's entire scattering summand.  A fixed D31
pair gives only its corresponding subspace.  The orthogonal `L²(dK)` summand
is the bound band and is not constructed.

*Justification.* ML2 resolution (21), its absolute-continuity proof
⟨1⟩5.⟨2⟩4, and D31(5).  This is an exact consistency anchor, not a claim of a
bound-state wave operator or pointwise endpoint control.

**⟨2⟩5. QED.**  This proves (A2M.2).

## 4. (A2M.3): nonvacuity bridge to Lane S1

### ⟨1⟩8. The sole D29 interface block and the soft-regularity condition

**INTERFACE ASSUMPTIONS ON LANE S1'S PROPOSED D29 — ALL ARE HERE.**

1. `𝒜_{N,W,σ}(ε)` is the connected on-shell pairing between normalized hard
   packet preparation/resolution, with and without one normalized
   charge-created soft leg `Q[f_ε]`; it is valued in D24(b)'s `L²(I)` hard
   norm and does not presuppose wave operators.
2. At fixed `W,σ,ε` its finite-volume local matrix elements converge to the
   D1 GNS matrix elements before any scattering-time limit; hard preparation
   and resolution converge, when wave operators exist, to vectors in
   `ran W_-` and `ran W_+`.
3. The amputating hard denominator is nonzero on the selected hard packet and
   is bounded away from zero along the chosen subsequence.
4. The order is exactly

   `N→∞  ≺  t→±∞  ≺  W↑ℤ  ≺  σ↓0  ≺  ε↓0`.  **(D29-order)**

5. At every fixed `ε>0`, D29's on-shell pairing agrees with the constructed
   channel pairing of `W_±^(ε)`; no uniformity as `ε↓0` is included.

These five clauses are the complete interface used below; reconciliation with
Lane S1's final D29 is an orchestrator task.

**(ACE2M-SR) — the one additional regularity hypothesis.**  After the first
four D29-order operations, let `A_j(ε)∈L²(I)` be any exhaustion/packet-width
sequence of constructed-channel data.  On some `[0,ε_0]`, assume the sets
`{A_j(ε),∂_εA_j(ε):j,ε}` are relatively compact in `L²(I)` and

`lim_{δ↓0}sup_j sup_{|ε-ε'|≤δ}||∂_εA_j(ε)-∂_εA_j(ε')||_{L²(I)}=0`. **(SR)**

This is a compact-containment plus equicontinuous-first-jet condition; it is
strictly a statement about amplitude data after fixed-packet scattering, not
about Cook integrands.

*Justification.* D24(b), D3(a), D12(a′), and the order mandated by
`briefs/soft-index-target.md`, Lane S2.

### ⟨1⟩9. Constructed-channel limit points

**ASSUME.** D31 and the D29 interface block; for the first-jet conclusion also
assume `(ACE2M-SR)`.

**PROVE.** (A2M.3).

**⟨2⟩1. [ADAPTED — fixed-packet AC-EX bridge]** At every fixed `ε>0`,
⟨1⟩5 supplies `W_±^(ε)`, so D29 interface clause 5 supplies a channel value.
Normalized channel matrix elements are bounded by Cauchy--Schwarz; clause 3
keeps amputation bounded.  Thus scalar projections of the datum have
subsequential weak `L²(I)` limit points along every `ε_j↓0` taken after the
earlier D29-order operations.

*Justification.* (A2M.1), (A2M.2), D29 interface clauses 1,3,5, and
Cauchy--Schwarz plus weak sequential compactness of bounded sets in the
reflexive space `L²(I)`.

**⟨2⟩2. [NEW]** Under `(SR)`, Banach-valued Arzelà--Ascoli gives a subsequence
converging in `C¹([0,ε_0];L²(I))`.  Hence Lane S1's TGT first jet exists on
constructed-channel vectors.  Its last operation is visibly

`lim_{ε_j↓0}[lim_{σ↓0}lim_{W↑ℤ}lim_{t→±∞}lim_{N→∞}
 𝒜_{N,W,σ,t}(ε_j)]`;

no limit is interchanged and `ε_j` never enters ⟨1⟩5's Cook integral.

*Justification.* `(ACE2M-SR)`, D29-order, and the Arzelà--Ascoli theorem in
the relatively compact metric target specified by `(SR)`.

**⟨2⟩3. [NEW — nonempty D6 anchor]** On D6--D8, ⟨1⟩7 identifies the channel
datum with ML2's D7 multiplier.  On a compact hard interval
`I=[a,b]⋐(0,π)`, S2-2body gives uniform `C²` control at `k_s=0`; smooth packet
smearing is bounded in D24(b)'s `L²(I)` norm.  The family is therefore
relatively compact with an equicontinuous first jet, so `(SR)` holds and the
limit-point set is nonempty.

*Justification.* Claims ML2 and S2-2body; D24(b); `TRIANGLE.md` §2.3's uniform
compact-hard remainder; and the exact-match computation ⟨1⟩7.⟨2⟩3.  This
uses ML2's Jacobi resolution, not a Bethe-completeness assumption.

**⟨2⟩4. [NEW — scope]** D31 alone does not imply `(SR)` for a general model:
fixed-packet Cook constants may diverge when a velocity gap closes, and they
control neither an on-shell first derivative nor the `W,σ` exhaustion.

*Justification.* The explicit `ε_v` denominators in **ACE-SP** and the ML3/ML6
CONJECTURE rows in `claims/CLAIMS.md`.

**⟨2⟩5. QED.**  This proves (A2M.3) at the stated conditional strength.

## 5. Reference-hypothesis audit

### ⟨1⟩10. What the exact ansatz replaces

**ASSUME.** D31.  **PROVE.** No source hypothesis is imported silently.

**⟨2⟩1. [ADAPTED]** D31(1)--(3)'s positive-energy GNS representation, exact band map, and filtered creators replace the
source's isolated mass shell and `B_t^*(g_t)Ω=B^*(g)Ω`.  *Justification.*
`refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`, Definitions `mass-shell-definition`, `HR-creation-operators`, Lemma
`HR-auxiliary(a)`, and equation `(creation-on-vacuum)`.

**⟨2⟩2. [NEW/ADAPTED]** D1 plus **MPS-2M-cluster** replaces Hamiltonian-gap clustering, permitting gapless D6; D31's local
smoothness/separated velocities replace global regularity.  Density, full-Fock, and completeness arguments are not ported.
*Justification.* D1(c,d), D6, ⟨1⟩3; source Theorem `clustering`, Proposition `norm-corollary`, and Theorems `Haag-Ruelle`,
`Haag-Ruelle-Fock`, `s-matrix`.

**⟨2⟩3. QED.**

## 6. CHECKER SPEC

### A2M-C1 — transfer-gap clustering (load-bearing for isometry)

Use D23's AKLT tensor `A^a=σ_a/√3`, `r=I/2`, and Cartesian `S^z`.  At distances `d=1,…,12`, contract
`C=D=I+S^z` directly and independently contract

`⟨l,E_C(E^{d-1}-P)E_D(r)⟩`.

Both connected answers must equal `4/3·(-1/3)^d` within `10^-12`; successive ratios must equal `-1/3`.
This certifies **MPS-2M-cluster**, including fixed-point subtraction.

**Red mutation.** Replace `E^{d-1}-P` by `E^{d-1}`.  Since `ω_A(I+S^z)=1`, the mutant retains `+1` and must fail both
gates.  Run under `python3 -O`; the mutation must exit nonzero.  This does not certify exact bands or `(ACE2M-SR)`.

## 7. MERGE PROPOSALS

### Exact addition to `definitions.md`

## D31 (H-ACE2M: exact fixed-packet two-magnon data over one vacuum)

Fix one translation-invariant injective canonical MPS tensor `A=A_α` from a D2(a) covariant vacuum family and its D1
state/GNS triple `(ω_A,H_A,Ω_A)`.  All constructions use this one vacuum representation.  Assume:

1. A finite-range translation-invariant Hamiltonian generates the dynamics, is implemented in `H_A` by commuting
   positive-energy time/lattice translations, and is normalized by `HΩ_A=0`, `ker H=ℂΩ_A`.  A conserved circle charge
   grades the selected magnon by one unit and the construction lies in its charge-two sector.
2. There is a finite-multiplicity selected magnon band `ω∈C²(𝕋)`, isolated on the packet neighbourhoods in clause 4, and
   a Gram-normalized translation-covariant **exact** band map `Γ_M:L²(𝕋;ℂ^m)→H_A`, with `HΓ_M=Γ_Mω`.  Exactness is a
   hypothesis, not a Rayleigh--Ritz conclusion.
3. For each packet window, a compact-energy-momentum-supported spacetime-Schwartz filter of a charge-one local
   observable gives uniformly almost-local creators `a_{i,b}(n)` of strictly positive energy transfer, with
   `a_{i,b}(n)Ω_A=Γ_M(χ_i e_n⊗e_b)`, `e_n(k)=e^{-ikn}`.
4. Packet amplitudes are finite sums of `C_c^∞` products.  The dispersion is `C^∞` on neighbourhoods `U_i` of compact
   supports `K_i`; `V_i=ω'(K_i)` obey `dist(V_1,V_2)≥ε_v>0`, `dist(V_i,{0})≥ε_0>0`.  Filters satisfy `χ_i=1` on `K_i`,
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

| AC-EX-2M | Under D31/H-ACE2M over one D1/D2(a) injective translation-invariant MPS vacuum, exact momentum-filtered magnon bands and two compact nonzero separated-velocity packets give fixed-packet Cook wave operators `W_±`; D1's transfer gap derives D31-C2/C4, so no independent clustering hypothesis is assumed.  The maps are isometries, intertwine joint translations, and avoid the fiberwise-isolated charge-two bound bands.  On D6--D8 they match exactly the corresponding part of ML2's Jacobi scattering summand: `W_+^*W_-` carries D7's `S_phys`, while the two-string is orthogonal.  For Lane S1's D29 interface, channel values exist with the soft scale last; first-jet/TGT compactness is conditional on `(ACE2M-SR)`, verified only on the D6--D8 anchor.  No soft-uniform Cook bound, equal-velocity/endpoint construction, bound-state wave operator, or asymptotic completeness is claimed. | SKETCH | D1, D2(a), D3(a), D6--D8, D12(a′), D31, ML2, S2-2body | theory/ansatz-scattering-2m.md | proposed checker A2M-C1 |

### Exact additions to `notation.md`

| Symbol | Meaning | First fixed in |
|---|---|---|
| `ℋ_{0,12}`, `H_{0,12}`, `𝒟_{12}` | labeled two-packet free magnon channel, sum Hamiltonian, and smooth product core | definitions.md D31; theory/ansatz-scattering-2m.md |
| `K_i`, `V_i`, `a_{i,b}(n)`, `χ_i`, `χ̃_i`, `h_i` | fixed packet supports, velocity supports, exact filtered creators, filters/companions, and rapidly decaying filtered symbols | definitions.md D31 |
| `I_2`, `𝓡_inel`, `Θ_inel`, `η_inel`, `E_{B,j}`, `d_B`, `P_B` | selected two-magnon joint energy--momentum set, inventoried alternative channels and threshold/margin, bound bands, their fiberwise separation, and bound projection | definitions.md D31 |
| `d_sep` | number of uniform transfer sites separating two local/almost-local clusters in D31-C2/C4 | definitions.md D31 |
| `(ACE2M-SR)` | compact-containment and equicontinuous-first-jet hypothesis on D29 data after fixed-packet scattering; never a Cook hypothesis | theory/ansatz-scattering-2m.md ⟨1⟩8 |

## 8. HONEST STATUS

**Proved from D31.**  (A2M.1)--(A2M.2): fixed-packet Cook existence, isometry, translation intertwining, separation from
listed bound/inelastic channels, and exact ML2/D7 agreement on D6--D8.  D31-C2/C4 are derived from D1, not assumed.

**Conditional.**  Generic (A2M.3) first-jet control assumes `(ACE2M-SR)`: D31 supplies every fixed-scale channel value,
but not the soft derivative or window/width exhaustion.  ML2/S2-2body verify `(SR)` on D6--D8, a nonempty instance.

**ML1 items still open.**  This shard does **not** close ML1: (i) endpoint packets; (ii) equal velocities; (iii) a
two-string/bound-band wave operator and transitions; (iv) soft-uniform channel norms; (v) general-model range exhaustion.
ML2 supplies only the D6 exact spectral anchor.

**Assumed.**  Exact band invariance/creator normalization, positive-energy covariance, and the threshold inventory are
D31 hypotheses, not variational consequences.  ML1/ML3/ML6, Bethe completeness, soft-in-Cook, and bound-band exclusion
are not used.
