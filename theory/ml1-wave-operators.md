# ML1 — canonical infinite-chain magnon wave operators

**Lane status:** **PROVED-candidate for D6--D8.**  The statement below is the
missing D6 wave-operator theorem, not a general variational-ansatz theorem.
It uses the PROVED global Plancherel resolution `ML2` and the PROVED
fixed-packet Cook theorem `AC-EX-2M`.  Endpoint and equal-velocity packets
remain outside the time-dependent assertion.

## ⟨1⟩1. Theorem ML1-D6

**ASSUME.** D6--D8 and `J>0`.  In the canonical ML2 chart put

`𝒞:=(-π,π]×(0,π)`, `c(K):=cos(K/2)`,

`k_1:=K/2-q`, `k_2:=K/2+q` (understood on the momentum torus), and

`E(K,q):=J(2-2c(K)cos q)`, `E_b(K):=J(1-c(K)^2)`.

Let `Σ_bad⊂\overline{𝒞}` be the union of `q∈{0,π}`, `K=π`, and the curves on
which either `k_i∈{0,π}`.  A *regular packet* is a finite sum of smooth
compactly supported product packets whose support has positive distance from
`Σ_bad`.  Write

`𝓗_ch:=L²(𝒞,dK dq)`, `𝓗_b,ch:=L²((-π,π],dK)`.

**PROVE.**  There are canonical maps

`W_-:𝓗_ch→𝓗_2`, `W_+:𝓗_ch→𝓗_2`

with the following properties.

1. `W_±` are isometries with the same range `𝓗_sc`; the D6 two-magnon space
   is the orthogonal sum `𝓗_2=𝓗_sc⊕𝓗_b` with
   `𝓗_b≃𝓗_b,ch`.
2. They intertwine time and lattice translations, and
   `W_+^*W_-=M_{S_phys}`, where `S_phys=S_{12}` in the canonical chart away
   from `K=π` and `|S_phys|=1`.
3. On every regular packet they are the strong time-dependent Møller limits

   `W_±F=s-lim_{t→±∞}e^{itH}I e^{-itE}F`,

   for the canonical two-lowering identification `I`.  Thus the limits exist
   and are isometric on precisely the packet class requested by ML1.
4. In each relative-coordinate fiber `K≠0` there is exactly one normalized
   bound eigenvector

   `b_K(r)=sqrt(1-c(K)^2)c(K)^{r-1}`, `r≥1`,

   of energy `E_b(K)`; at `K=0` it is a threshold resonance, not an `ℓ²`
   vector.  No bound vector lies in either wave-operator range.
5. The one-magnon scattering space is `𝓗_1=ℓ²(ℤ)≃L²(𝕋,dk/(2π))`; its
   incoming and outgoing maps coincide with the Fourier spectral map and are
   unitary.

*Justification.* D6--D8, claim `ML2`, and claim `AC-EX-2M`.

## ⟨1⟩2. The spectral spaces are canonical

**ASSUME.** D6 and claim `ML2`.  **PROVE.** The spaces and transforms in
⟨1⟩1 are well defined without assuming Bethe completeness.

**⟨2⟩1.**  Center Fourier transform carries the chamber
`{(x,y)∈ℤ²:x<y}` to the direct integral of half-line fibers

`(h_Kf)_1=Jf_1-Jc(K)f_2`,

`(h_Kf)_r=2Jf_r-Jc(K)(f_{r-1}+f_{r+1})`, `r≥2`.

*Justification.* D6 and claim `ML2`, equations (15)--(16).

**⟨2⟩2.**  Let `𝒰_sc` and `𝒰_b` be the coefficient maps against ML2's
delta-normalized kernels `Ψ^sc_{Kq}` and `Ψ^b_K`.  Then

`𝒰_2:=(𝒰_sc,𝒰_b):𝓗_2→𝓗_ch⊕𝓗_b,ch`

is unitary, and it conjugates `H` to `M_E⊕M_{E_b}`.

*Justification.* Claim `ML2`, its fiber identity (20) and resolution (21).

**⟨2⟩3.**  Consequently

`𝓗_sc:=𝒰_sc^*𝓗_ch`, `𝓗_b:=𝒰_b^*𝓗_b,ch`

are closed orthogonal reducing subspaces and exhaust `𝓗_2`.

*Justification.* Claim `ML2` and the unitarity in ⟨2⟩2.

**⟨2⟩4.**  In a fixed fiber the free constant-coefficient half-line Jacobi
operator differs from `h_K` only in the first diagonal entry.  The fiber
resolution has exactly the continuum `q∈(0,π)` plus the single vector `b_K`
for `K≠0`; at `K=0`, `b_K(r)=1` is not square summable.

*Justification.* D6 and claim `ML2`, equations (16), (19)--(21).

**⟨2⟩5. QED.**

## ⟨1⟩3. Incoming and outgoing transforms

**ASSUME.** ⟨1⟩2 and D7.  **PROVE.** The stationary maps in ⟨1⟩1 are
isometries with physical scattering multiplier `S_phys`.

**⟨2⟩1.**  For almost every `(K,q)∈𝒞`,

`v(k_2)-v(k_1)=2J cos(K/2)sin q>0`.

The only equality locus in the canonical chart is `K=π`, a two-dimensional
Lebesgue-null line.  Hence D7 assigns the `e^{-iqr}` branch as incoming and
the `e^{iqr}` branch as outgoing almost everywhere, with multiplier

`S_phys(K,q)=S(K,q)=(c(K)-e^{-iq})/(e^{iq}-c(K))`.

*Justification.* D6--D7 and claim `ML2`, equations (17)--(18).

**⟨2⟩2.**  `|S_phys|=1` almost everywhere: the numerator is minus the
complex conjugate of the denominator.  Assigning any unit value on the null
exceptional set makes `M_{S_phys}` unitary on `𝓗_ch`.

*Justification.* D7 and claim `ML2`, equation (18).

**⟨2⟩3.**  Define globally

`W_-:=𝒰_sc^*`, `W_+:=𝒰_sc^*M_{S_phys^{-1}}`.

Then `W_±^*W_±=1`, `ran W_-=ran W_+=𝓗_sc`, and

`W_+^*W_-=M_{S_phys}`.

*Justification.* Claim `ML2`, ⟨1⟩2.⟨2⟩2, and ⟨2⟩2.

**⟨2⟩4.**  Both maps intertwine `M_E` with `H|_{𝓗_sc}` and the total-momentum
multiplier `M_K` with lattice translation.

*Justification.* Claim `ML2`, equations (17)--(21), and the definitions in
⟨2⟩3.

**⟨2⟩5. QED.**

## ⟨1⟩4. The stationary maps are the Møller limits on regular packets

**ASSUME.** A regular packet `F` as in ⟨1⟩1.  **PROVE.** The two strong
limits in ⟨1⟩1(3) exist and equal the restrictions of ⟨1⟩3's maps.

**⟨2⟩1.**  The support of `F` is covered by finitely many product rectangles
on each of which the two velocity supports have a positive separation
`ε_v>0`, the individual momenta avoid `0,π`, and all dispersion/filter
symbols are smooth.

*Justification.* D6--D8 and compactness of the regular support in ⟨1⟩1.

**⟨2⟩2.**  On each such rectangle D6 satisfies D31(1)--(5), and the
fixed-packet Cook limits exist and are isometries.

*Justification.* Claim `AC-EX-2M`, including its D6 nonvacuity step and its
fixed-packet Cook conclusion.

**⟨2⟩3.**  Those local limits equal `𝒰_sc^*` on the incoming side and
`𝒰_sc^*M_{S_phys^{-1}}` on the outgoing side.  Therefore limits obtained
from two overlapping packet rectangles agree on their overlap.

*Justification.* Claim `AC-EX-2M`, its exact ML2/D7 match, and ⟨1⟩3.⟨2⟩3.

**⟨2⟩4.**  Summing the finite rectangle decomposition proves the strong
limits for `F`; their values are `W_-F` and `W_+F`.

*Justification.* Claim `AC-EX-2M`, linearity of strong limits, and ⟨2⟩1--⟨2⟩3.

**⟨2⟩5.**  The union of regular packet spaces is dense in `𝓗_ch`, because
`Σ_bad` is a finite union of one-dimensional subsets of the two-dimensional
chart together with boundary sets.  The compatible isometries therefore
extend uniquely to the global maps of ⟨1⟩3.  This extension is abstract on
`Σ_bad`; no equal-velocity or endpoint time-dependent estimate is claimed.

*Justification.* D3(a), claim `ML2`, and the isometry of ⟨1⟩3.⟨2⟩3.

**⟨2⟩6. QED.**

## ⟨1⟩5. Bound isolation and the one-magnon channel

**ASSUME.** ⟨1⟩2--⟨1⟩4.  **PROVE.** The remaining assertions of ⟨1⟩1.

**⟨2⟩1.**  For every `K≠0`, substitution of
`b_K(r)=sqrt(1-c²)c^{r-1}` in the half-line recurrence gives eigenvalue
`E_b(K)=J(1-c²)` and unit relative norm.  The rank-one boundary defect has no
second eigenvalue.

*Justification.* Claim `ML2`, equations (19)--(21).

**⟨2⟩2.**  Since `ran W_±=𝓗_sc` and `𝓗_sc⊥𝓗_b`, both wave operators
annihilate the bound-channel projection on their ranges.  The direct integral
bound band is a separate stable composite channel, not a two-free-magnon
incoming/outgoing channel.

*Justification.* Claim `ML2` and ⟨1⟩2.⟨2⟩3.

**⟨2⟩3.**  In the D6 one-flip sector, Fourier transform

`(𝓕_1ψ)(k)=Σ_x e^{-ikx}ψ(x)`

is unitary from `ℓ²(ℤ)` to `L²(𝕋,dk/(2π))` and conjugates `H` to
`ω(k)=J(1-cos k)`.  With no lower particle channel, the incoming and outgoing
one-magnon maps are both `𝓕_1^*`.

*Justification.* D6 and oracle claim `O1`.

**⟨2⟩4. QED.**

## ⟨1⟩6. Delta-normalized one-magnon kernel beyond the product vacuum

This section addresses the `tns-iu5` sub-task named in the lane brief.  It is
conditional on the exact-band hypothesis D31; it does not assert that a
generic variational excitation tensor satisfies D31.

**ASSUME.** D31(1)--(2), with multiplicity `m`, and use the rigging

`C^∞(𝕋;ℂ^m) ⊂ L²(𝕋,dk/(2π);ℂ^m) ⊂ 𝒟'(𝕋;ℂ^m)`.

**PROVE.** There are generalized one-magnon kernels `|k,b⟩`, `1≤b≤m`,
unique up to a measurable unitary change of multiplicity frame, such that

`Γ_M f=Σ_b∫(dk/(2π)) f_b(k)|k,b⟩`,

`⟨k,b|k',b'⟩=2πδ(k-k')δ_{bb'}`,

`H|k,b⟩=ω(k)|k,b⟩`,

and packets made from these kernels are exactly the one-particle legs used by
the D31 two-magnon wave operators.

**⟨2⟩1.**  Transport the `C^∞` Fréchet topology through `Γ_M` to
`Φ_M:=Γ_M C^∞(𝕋;ℂ^m)`.  For each `(k,b)` define the continuous evaluation
functional `|k,b⟩∈Φ_M'` by

`⟨Γ_M g|k,b⟩:=overline{g_b(k)}`.

For test functions `f,g∈C^∞(𝕋;ℂ^m)`, D31's Gram normalization
gives

`⟨Γ_M f,Γ_M g⟩=Σ_b∫(dk/(2π)) overline{f_b(k)}g_b(k)`.

Thus `Γ_M f=Σ_b∫f_b(k)|k,b⟩dk/(2π)` as a weak identity in `Φ_M'`.

*Justification.* D31(2) and continuity of point evaluation on `C^∞(𝕋)`.

**⟨2⟩2.**  Testing the kernel twice against arbitrary `f,g` turns its Gram
form into the right side of ⟨2⟩1.  Therefore, as a distribution,

`⟨k,b|k',b'⟩=2πδ(k-k')δ_{bb'}`.

*Justification.* D31(2) and ⟨2⟩1.

**⟨2⟩3.**  The exact intertwining `HΓ_M=Γ_M(ω⊗1_m)` implies the
distributional eigen-equation `H|k,b⟩=ω(k)|k,b⟩`; translation covariance
gives the corresponding momentum eigen-equation.

*Justification.* D31(1)--(2).

**⟨2⟩4.**  D31(3)'s filtered creator satisfies
`a_{i,b}(n)Ω=Γ_M(χ_i e_n⊗e_b)`.  Because `χ_i=1` on the packet support,
integrating these vectors against a packet reproduces exactly
`Γ_M f=∫f_b(k)|k,b⟩dk/(2π)`.  Thus no charge-created normalization is hidden
in the kernel; it has the unit external-leg weight stipulated by D24(b).

*Justification.* D24(b), D31(3)--(4), and ⟨2⟩1--⟨2⟩3.

**⟨2⟩5.**  A measurable unitary change of the `m`-component fiber changes
the columns but preserves the delta Gram form and every packet norm.  No
stronger pointwise uniqueness is meaningful for a generalized kernel.

*Justification.* D31(2) and ⟨2⟩2.

**⟨2⟩6. QED.**

## ⟨1⟩7. QED

The global spectral decomposition is ⟨1⟩2; the incoming/outgoing isometries
and multiplier are ⟨1⟩3; their strong-limit realization on all regular
packets and compatible dense extension are ⟨1⟩4; bound isolation and the
one-magnon channel are ⟨1⟩5.  Hence Theorem ML1-D6 is proved.  Section
⟨1⟩6 separately proves the D31-conditional delta-normalized one-magnon
kernel needed off the fully polarised product family.  QED.
