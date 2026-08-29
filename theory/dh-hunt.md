# NOTHING NON-ARTIFICIAL — DH does not supply a missing lattice-IR theorem

**One sentence.**  Every natural Duistermaat--Heckman (DH) candidate either
has the wrong object type (a continuous Liouville pushforward rather than the
discrete, state- and dynamics-dependent TPM law), consumes the representation
multiplicities or scattering data it was meant to produce, or collapses in the
two-dimensional kink family to the already-known moment-map identity
`dμ = ι_Xϖ`; consequently it fills no slot of `paper/skeleton.md`.

This is the terminal outcome allowed by `PRD.md`: there is no checker, no
critic/repair round, and no MERGE PROPOSALS section.  In particular, nothing
below is offered as a new positive claim for `claims/CLAIMS.md`.

## 1. Hunt ledger

| candidate | verdict | decisive reason |
|---|---|---|
| 1. The memory law as a DH measure | **DEAD** | An ordinary DH measure on a natural positive-dimensional Hamiltonian torus manifold is a continuous, piecewise-polynomial Liouville pushforward.  The D27/M-INDEX-spec object is the atomic Born law `Σ_ν p_νδ_ν` on `ℤ`, depending on a state, two-time dynamics, dephasing, and an ordered exhaustion.  Degenerate zero-dimensional components can manufacture atoms only by putting the desired atoms and their volumes in by hand; DH then proves neither integrality nor their weights. |
| 2. Weight-multiplicity asymptotics | **DEAD** | The claim that the projective DH measure “is the weight distribution” is false already for two spins; §2 computes the two distinct measures exactly.  More generally the projective DH spline takes the weight multiplicities as its Dirichlet parameters (or, in localization language, as dimensions of fixed components), so it does not produce them.  Moreover `m_{λ,N}` in S-IDX-fin-r2 is the scalar charge/weight value, not a weight multiplicity, and (PROTO-LSZ) is an operator/scattering regularity hypothesis, not a sector-counting hypothesis. |
| 3. ABBV localization for the soft coefficient | **DEAD** | For the internal circle, every vector in the selected one-magnon band has the same charge, so its projective band is fixed wholesale; `k_s=0` is not an isolated fixed locus.  Lattice translation is `C_N` on a finite ring, while infinite-volume quasi-momentum is a band parameter, not the required Hamiltonian circle action on the state phase space.  ABBV also has no input containing the D24 source, current, on-shell channel, or amputation.  Importing those data recreates the Ward/LSZ proof and violates the G3 §17 fences; attempting to obtain `𝔞_leg` from leg normalization alone hits the D24N-C8 square-root/double-count fence. |
| 4. DH wall crossing as the SPT rigidity dichotomy | **DEAD** | DH walls are critical *moment values inside one fixed Hamiltonian torus space*.  The `λ-D` sweep changes the tensor/Hamiltonian and its symplectic data.  SPT-E' deliberately proves only a fixed-tensor congruence and explicitly disclaims deformation constancy of the centered offset.  Any plateau follows from constancy of the projective edge class plus gap/H-split hypotheses; that is the existing representation-theoretic argument, not DH. |
| 5. M-IDX-density from convexity/integral vertices | **DEAD** | Integral vertices do not make interior moment-map values integral: even the spin-`1/2` sphere has all expectation values in `[-1/2,1/2]`.  M-IDX-density uses the stronger and different fact that the injective-MPS IT phase is a circle character whose slope equals the tail density, followed by the two-tail antisymmetry.  The higher-rank torus extension is the same character-lattice argument component by component; DH adds no group or invariant. |
| 6. The D16 Kähler kink cylinder (`BA-DH`) | **DEAD AS DH** | On a two-dimensional Hamiltonian circle manifold, `dμ=ι_{∂φ}ϖ` already gives locally `ϖ=±dμ∧dφ`, so the DH pushforward is constant and `∫ϖ=2πΔμ`.  The area-per-translation and `1/(2s)` quantum therefore come from the D13 calibration plus the moment-map identity in two lines.  This is exactly the reproduction-only failure pre-registered in `briefs/bta-kahler-target.md` L4 and §8.  No natural `χ>1` symplectic endpoint factor currently exists to make a higher-dimensional DH statement do more work. |

The verdicts preserve the five binding fences of
`theory/soft-index-g3.md` §17.  In particular no DH statement is used for a
descendant Gram inverse, current covariance, omission of a highest-weight
projector, a finite-group/central-torus soft leg, or identification of a
postselected root step with a memory protocol.

## 2. Best candidate worked exactly: projective DH is not the weight law

The finite calculation below kills the premise of candidate 2 while also
showing precisely what projective DH *does* remember.

### ⟨1⟩1. Finite representation and the two proposed measures

**ASSUME.**  Let `V=(ℂ²)^{⊗2}` and let the circle generator be total
`Q=S^z_1+S^z_2`, with one-site weights `±1/2`.  Then

`V=V_{-1}⊕V_0⊕V_{+1}`, with dimensions `(1,2,1)`.

Let `M=P(V)=ℂP³` carry normalized Fubini--Study Liouville measure and moment
map

`μ([v])=⟨v,Qv⟩/⟨v,v⟩`.

There are two a priori different probability measures:

1. the normalized multiplicity (weight-counting) law
   `η_wt=(1/4)δ_{-1}+(1/2)δ_0+(1/4)δ_{+1}`;
2. the DH law `η_DH=μ_*(vol_FS)`.

*Justification.*  The three dimensions are the elementary two-spin weight
count.  The moment map is the finite-projective normalization already fixed
in `theory/soft-index-g3.md` (G3.1)--(G3.2).

### ⟨1⟩2. Exact DH density

**PROVE.**

`dη_DH(x) = (3/2)(1-|x|)^2 1_{[-1,1]}(x) dx`.              **(DH.1)**

**⟨2⟩1.**  Decompose `v=v_-⊕v_0⊕v_+` and put
`p_j=||v_j||²/||v||²`.  A Fubini--Study random ray can be obtained by
normalizing a standard complex Gaussian in `V`.  The three block norms are
independent Gamma variables with shapes `(1,2,1)`.  Therefore
`(p_-,p_0,p_+)` has Dirichlet density

`6p_0` on `p_j≥0`, `p_-+p_0+p_+=1`.

*Justification.*  A block of `d` independent standard complex Gaussian
coordinates has squared norm equal to a sum of `d` independent exponential
variables, hence Gamma shape `d`.  Changing variables from the three Gamma
variables to their sum and normalized fractions gives the displayed
Dirichlet density; the normalization is
`Γ(4)/(Γ(1)Γ(2)Γ(1))=6`.

**⟨2⟩2.**  By the weight decomposition,

`μ=p_+-p_-`.

Set `x=p_+-p_-` and `s=p_++p_-`.  Then
`p_±=(s±x)/2`, `p_0=1-s`, the Jacobian is `1/2`, and the simplex becomes
`|x|≤s≤1`.

*Justification.*  Direct substitution and the projective moment formula
(G3.2).

**⟨2⟩3.**  Integrating out `s` gives

`f_DH(x)=∫_{|x|}^1 6(1-s)(1/2)ds=(3/2)(1-|x|)^2`

for `|x|≤1`, and zero otherwise.  Its integral is
`2·(3/2)∫_0^1(1-x)^2dx=1`.

*Justification.*  Elementary one-variable integration.

**⟨2⟩4. QED.**

### ⟨1⟩3. The mismatch is structural, not a normalization choice

**PROVE.**  `η_DH≠η_wt`.

**⟨2⟩1.**  `η_wt` is supported on three points, while (DH.1) is absolutely
continuous and gives each point zero mass.

*Justification.*  ⟨1⟩1 and ⟨1⟩2.

**⟨2⟩2.**  Even their second moments differ:

`∫x²dη_wt=1/2`, whereas
`∫x²dη_DH=3∫_0^1x²(1-x)²dx=1/10`.

*Justification.*  Direct evaluation (`∫_0^1x²(1-x)²dx=1/30`).

**⟨2⟩3. QED.**

This two-spin example already has genuine wall crossing: (DH.1) is polynomial
on `(-1,0)` and `(0,1)`, with the internal weight `0` as its wall.  It is a
genuine DH spline, but it is not a discrete weight distribution.

### ⟨1⟩4. Why the general projective formula cannot rescue S-IDX

For a torus representation `V=⊕_λV_λ`, the same Gaussian proof gives block
fractions `(p_λ)` with Dirichlet parameters `dim V_λ` and

`μ_T=Σ_λp_λλ`.                                            **(DH.2)**

Thus the projective DH density is a multivariate Dirichlet spline whose input
already includes every weight-space dimension.  ABBV says the same thing in
fixed-set language: the fixed components are `P(V_λ)`, whose dimensions are
`dim V_λ-1`.  Localization can reorganize an integral once those components
and normal weights are known; it does not infer the missing multiplicities
from symmetry alone.

For the lattice soft index the mismatch is sharper:

- `m_{λ,N}` in `S-IDX-fin-r2` is the scalar `S^z` value on a positive-weight
  register (for the primitive band, `NS-1`), not `dim V_λ`;
- the full-sector object that matters is the operator
  `A_{λ,N}=D_{λ,N}†D_{λ,N}` and the descendant-range projector, which DH.2
  does not determine (`theory/soft-index-g3.md` §§6--7);
- (PROTO-LSZ) controls an exhaustive source/current/channel decomposition,
  uniform `C¹` data, contact terms, and boundary gradients.  No bound on
  `dim V_λ`, even a perfect one uniform in `N`, implies any of those clauses.

The only route from DH to actual multiplicity asymptotics would be to replace
this spin-chain representation by a separate geometric-quantization problem
and invoke a “quantization commutes with reduction” theorem.  That changes the
input problem, and the resulting sector counts are already obtained here by
elementary tensor-product characters.  It supplies neither the current
operator nor the soft-limit estimates, so it fails the skeleton value gate.

## 3. The remaining candidates worked to their stopping points

### 3.1 The TPM law cannot literally be an ordinary DH measure

At every fixed `W`, D27 produces

`p_W=Σ_{ν∈ℤ}p_W(ν)δ_ν`.

The weights are matrix elements of products of two spectral projections at
different times, followed by a Cesàro limit.  They depend on `Ψ`, `α_t`, the
initial measurement back-action, and eventually LR2--LR3.  By contrast a DH
law depends only on a symplectic manifold, its Liouville form, a torus action,
and its moment map.  The finite calculation above makes the type mismatch
visible even before dynamics is added.

One can force an atomic “DH measure” by taking a disconnected union of
zero-dimensional symplectic components, putting the constant moment value
`ν` on the component labelled by `ν`, and assigning it volume `p_ν`.  This is
artificial in the exact sense of the work order: the construction imports the
support, integrality, and Born weights it purports to explain.  Moment maps
also admit additive constants, so DH alone cannot make those chosen constants
integral.  M-INDEX-fin already obtains the actual integrality from D26 and
fixed-window coset-offset cancellation, with fewer and weaker inputs.

A “quantum DH measure” based on characters does not repair the mismatch.
Characters count representation weights (or traces with insertions); the TPM
law is a state-specific two-time matrix element and is not a character.  An
equivariant insertion encoding both `Ψ` and `α_t` would merely transplant the
entire TPM calculation into the localization integrand.

Nor does the usual semiclassical bridge have the correct limit.  A quantum
weight measure approaches a continuous DH law after a high-tensor-power limit
and rescaling weights by the power.  D27(LR3) instead keeps the *unscaled*
escaped integer `ν` first-moment tight.  Dividing `ν` by volume would collapse
the memory law to `δ_0`; declining to divide leaves an atomic law, not a DH
density.

### 3.2 There is no soft fixed point to localize on

The natural internal circle acts on a one-magnon state by its charge
character.  Projectively that scalar action is trivial, so the whole
one-magnon projective band is fixed, not only `k=0`.  On a finite ring the
translation symmetry is discrete (`C_N`) and has no ABBV infinitesimal
generator.  In infinite volume the Brillouin circle labels irreducible
translation characters; it is not thereby a Hamiltonian circle action on a
compact scattering phase space, and `k=0` is not its fixed point.

The two meanings of stationary phase also do not meet.  DH exact stationary
phase applies to an equivariant integral whose phase is a Hamiltonian moment
map.  The scattering estimates use phases built from the dispersion,
`tω(k)-kx`, plus an on-shell scattering phase.  No identity in D1--D31 turns
that dispersion into the internal-charge moment map.

More decisively, the soft coefficient is not a symmetry-only integral.
S-IDX-fin-r2 needs the Hamiltonian-dependent current vector, the full-sector
polar inverse, and a channel velocity.  Multiplying the Hamiltonian by a
constant leaves the projective symmetry geometry unchanged while multiplying
the current/velocity residue `2iv_S(h)`.  D24 then adds source membership,
contact cancellation, and amputation.  ABBV has no access to these quantities
until they are inserted as hypotheses, at which point the calculation is the
existing Ward/LSZ route in localization notation.  For the numerical value of
`𝔞_leg`, D24N-C8 already proves that charge-created versus asymptotic-leg
normalization supplies only `Z_ρ^{-1/2}`; a DH volume factor cannot be silently
used as the second `Z_ρ^{-1/2}` without identifying a distinct mechanism and
proving the D24 bridge.

### 3.3 DH walls do not run along the `λ-D` coupling axis

For a fixed Hamiltonian torus space, a DH wall is a critical value of `μ`.
The phase-diagram coordinate `λ` or `D` instead changes the Hamiltonian, MPS
tensor, fixed point `r`, virtual generator, and potentially the symplectic
form itself.  A family of DH measures may drift smoothly with those data
without crossing any moment-map wall.

This is exactly compatible with the proved SPT rows.  SPT-E' places the
fixed-tensor spectrum in `q^∘_{ω,C}+ℤ` and explicitly makes no deformation-
constancy claim for the centered offset.  The protected datum is the
projective module/class, while a bulk coefficient or centered charge can
vary.  To forbid variation one must separately prove constancy of the
equivariant cohomology/prequantum class and control H-split across the path;
those hypotheses would do the rigidity work before DH is invoked.  Therefore
DH supplies neither the Fig. 3 plateau nor a no-go for the drifting bulk
coefficient.

### 3.4 Convexity does not quantize a vacuum density

For a projective torus action, the moment image is the convex hull of the
weights.  Its generic points are convex combinations and are not lattice
points.  Already on `P(ℂ²)`, `μ=⟨S^z⟩` fills the interval
`[-1/2,1/2]`.  Integral (or half-integral) vertices therefore do not imply an
integral expectation value.

M-IDX-density succeeds because injectivity and (IT) make the vacuum phase a
continuous circle character, its derivative equals `ρ`, and D26 plus the
antisymmetric second tail gives `e^{2πiρ}=e^{-2πiρ}`.  For a torus `T^r`, the
same proof pairs with every cocharacter and says that the density difference
lies in the character lattice (and twice an antisymmetric density does).
That is a direct higher-rank extension, but it is character theory plus the
MPS fundamental theorem; DH convexity is neither needed nor strong enough.

### 3.5 The only natural kink DH computation is tautological

Suppose the D16 kink cylinder really has coordinates `(x_0,φ)`, invariant
form `ϖ=Ω(x_0)dx_0∧dφ`, circle field `∂_φ`, and memory moment map `μ(x_0)`.
The moment-map identity gives, up to the fixed sign convention,

`μ'(x_0)=-Ω(x_0)`.

Consequently Liouville measure is `|dμ|dφ`, its pushforward is the constant
`2π` density, and for one lattice translation

`∫_{x_0}^{x_0+1}∫_0^{2π}ϖ=2π[μ(x_0)-μ(x_0+1)]`.

If D13 calibration supplies `|Δμ|=2s`, the area is `2π·2s` and the position
quantum is `1/(2s)`.  DH has performed no inference beyond integrating the
defining moment-map identity.  This is useful geometric interpretation, but
`briefs/bta-kahler-target.md` explicitly classifies it as reproduction-only
in two dimensions.  Making DH nontrivial requires a natural higher-dimensional
`χ>1` reduced space; the repo currently has only a `PGL(χ)` endpoint torsor,
not a symplectic form on it, and the nonscalar-virtual-circle obstruction may
prevent a global moment map.  Adding an auxiliary orbit solely to create DH
walls would be artificial.

## 4. Checker decision

No `theory/checks/dh_hunt_check.py` is created.  The work order permits it
only for a RESULT or a PROGRAM first computation, while the terminal status
is **NOTHING NON-ARTIFICIAL**.  The exact `ℂP³` calculation in §2 is short
symbolic integration and serves to decide a route negatively; wrapping it in
an ED gate would violate `PRD.md`'s rule against verification machinery for
negative side-results.

## 5. Terminal assessment

The closest thing to a legitimate use of DH is the projective Dirichlet-spline
formula (DH.2).  It is mathematically real and its `ℂP³` instance has an
honest wall at the zero weight.  It nevertheless fails the project test: it
is a distribution of *expectation values of random rays*, not the TPM charge
history or the normalized weight-counting law; it consumes multiplicities
rather than deriving them; and it controls none of the current, descendant,
source, channel, or soft-uniform data missing from §5 of the skeleton.

The D16 moment-map cylinder remains worthwhile as Kähler interpretation, but
DH there is exactly the “two-line computation wearing a large hat” already
warned against in the target brief.  No candidate found in this hunt makes DH
load-bearing without changing the problem or inserting the desired answer as
geometric input.  The line therefore ends.
