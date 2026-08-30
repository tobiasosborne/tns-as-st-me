# O1: operational-status audit of the campaign definitions

## 0. Scope and decision rule

This audit applies TJO's criterion literally: an object is operational only if
a quantum experiment can measure its statistics or execute the operation it
names.  A tensor-network coordinate may still be useful, but it is **GAUGE**
unless the statement made with it is invariant under changes of tensor
representative and has a physical measurement or preparation on its other
side.  Each D-number and each separately requested claim-level object receives
exactly one of the three labels below.  The label is for the definition's
load-bearing object as used by the campaign; a paragraph may identify gauge
scaffolding inside an otherwise operational protocol, but it does not assign a
second status.

- **OBSERVABLE** means statistics of a specified POVM/PVM, local observable,
  spectroscopy, tomography, or interferometric scattering measurement.
- **IMPLEMENTABLE** means a finite quantum operation or a controlled limit of
  finite operations.  For a limit, the topology and error bound are part of
  the status.
- **GAUGE** means representation, coordinate, frame, ansatz, or analytic
  bookkeeping that no apparatus reads directly.  The paragraph then names
  the invariant physical content that the bookkeeping is allowed to support.

These labels are operational types, not truth statuses.  In particular,
**PROVED**, **SKETCH**, **CONJECTURE**, **REFUTED**, and **RETRACTED** entries in
`claims/CLAIMS.md` are unchanged.  D29 and D30 are not present in
`definitions.md`; they remain the **PROPOSED**, quarantined definitions in
`theory/soft-index-r2.md` section 7.  They are audited below as proposals, not
silently promoted to frozen definitions.  Arguments not already theorem-level
in the campaign are marked **[physical argument]** or **[textbook]**.

## 1. Positive result: the injective-MPS boundary algebra is operational

### 1.1 State-functional, not tensor-functional

For a uniform injective/normal MPS, the boundary algebra is
`M_χ(ℂ)` up to algebra isomorphism, not the displayed entries of one chosen
tensor.  The fundamental theorem says that equal normal MPS are related by a
similarity and phase; in canonical form the similarity is unitary.  The local
TeX states that two normal MPS are “equal ... if and only if” their tensors
are gauge related (`refs/arxiv-2011.12127/TN-Review-main.tex:1084-1086`), and
its formal equal-MPV
corollary says both that the matrix dimensions coincide and that
`A^i=XB^iX^{-1}` at `:1896-1900`, with a unitary `X` in the unital canonical
gauge at `:1905-1906`.  Therefore the state fixes `χ`, the abstract algebra
`M_χ(ℂ)`, its projective endpoint torsor, and the symmetry action up to inner
conjugacy.  Individual matrices `A^s`, `V(g)`, `M`, and a basis of `ℂ^χ` remain
GAUGE; the isomorphism class and all conjugation/projective invariants are
state-functional.  This is the first reason the injective boundary algebra is
not merely an artifact of an MPS representation.

### 1.2 Limit of executable strings, with the honest rate

Every truncated symmetry
`U_[x,y](g)=∏_{z=x}^y u_z(g)` is an executable depth-one product of on-site
unitaries.  WI identifies its two finite endpoints exactly.  In the unbroken,
normal-ordered A1 register, its action on any fixed local algebra `𝔄_W` is
eventually **exactly** the single-bond endpoint state: after the far endpoint
passes `W`, the error is zero.  In the broken A2 register the corresponding
statement is genuinely asymptotic.  For `O∈𝔄_W`, `w=max W`, and every
`λ̃∈(λ_E,1)`, the campaign proves

`|ω_α(U_[x,y](g)^† O U_[x,y](g))−ϱ_x^(g)(O)|
 ≤ C_λ̃ ||O|| λ̃^(y−w)`.

This is `theory/corner-a-kinks.md:120-128` and is derived from the Jordan-safe
transfer estimate at `:179-198`; a bare `λ_E^(y-w)` is not claimed.  Thus a
finite-resolution experiment on `W` with tolerance `ε` chooses, for known
`C_λ̃`, a far-end distance satisfying
`y−w ≥ log(C_λ̃||O||/ε)/(-log λ̃)` and applies a finite depth-one string.
The surviving operational notion is convergence of the prepared **state on
every fixed local measurement algebra** (weak-*), with zero error in A1(a) and
the displayed exponential error in A2(b).  No infinite product is being
declared an element of the quasi-local algebra.

### 1.3 Direct readout by strings and local tomography

The boundary data are observable in two complementary ways.  First, the
string-order experiment measures
`S_N=⟨x⊗u^⊗N⊗y⟩`; the local TeX calls `u` a “local unitary” and `x,y`
“local operators” (`refs/arxiv-0802.0447/StringOrder-v10.tex:112-122`) and
gives the transfer expression at `:175-183`.  Its Lemma 1 says there “exists a
unitary `V`” precisely at modulus-one twisted-transfer radius (`:185-197`).
Experimentally, an ancilla-controlled string followed by an ancilla
Hadamard/phase test reads the real and imaginary parts, while Hermitian product
instances can be obtained from joint local readout **[physical argument]**.
The endpoint probes can be chosen on sufficiently large blocks because their
transfer images “span the set of `D×D` matrices” (`:278-291`).  The same
source formulates symmetry as an invariance test on “every `N`-site reduced
density operator” (`:298-304`) and gives the concrete AKLT readout `V=σ_z`,
`S_L=-4/9` at `:392-399`.

Second, informationally complete tomography of a padded reduced density
matrix distinguishes the endpoint states.  A1(c) proves
`ω_A^{M@b}=ω_A^{M'@b}` iff `M'=cM`, so reduced-state tomography recovers the
endpoint point `[M]∈PGL(χ)` without selecting virtual coordinates.  Repeating
the string/tomography experiment for `g,h,hg` reconstructs the projective
multiplication phase up to rephasing and hence its cohomology class
`[ω]∈H²(G,U(1))` **[physical argument]**.  The 0802.0447 source proves the
string/symmetry/`V` link; the last cohomology reconstruction is the operational
inference from those measured endpoint maps plus A1(d3), not a claim that the
2008 paper itself states the later SPT classification.

Accordingly, the **injective-MPS boundary algebra — OBSERVABLE**: its matrix
coordinates are gauge, but its algebra up to isomorphism, endpoint-state
torsor, effective action, and multiplier class are reconstructible from
finite-string interferometry and padded-window tomography.  Its state action
is also approximable by the finite implementers of section 1.2.

### 1.4 A1(b): what is implementable, and what is not

A1(b) is not a contradiction to section 1.2; it is the necessary operational
distinction.  Put `Ψ_y=U_[x,y](g)Ω_A`.  If `V(g)` is non-scalar, A1(b) proves
that `(Ψ_y)_y` is not Cauchy, so no operator sequence `U_[x,y](g)` converges
strongly on the vacuum representation.  There is therefore no coherent
half-chain unitary gate, no norm-convergent endpoint vector prepared by that
sequence, and no experiment that can treat the formal infinite product as a
single operator while retaining interference between all cutoffs.  If `V(g)`
is scalar, WI instead makes the sequence constant on `Ω_A`, so the obstruction
vanishes exactly.

What survives for non-scalar `V(g)` is weaker and operationally sufficient for
local state preparation: for each finite measurement window and accuracy,
perform one sufficiently long finite string and compare the resulting local
statistics.  Those statistics converge weak-* as in section 1.2, even though
the global vectors do not converge strongly.  In the broken case the limit
can even leave the vacuum folium; in the unbroken case A1 determines the local
endpoint state, while its GNS-vector realization remains the explicitly
SKETCH split-property box in `theory/corner-a.md` section
`⟨1⟩4.⟨2⟩9`.  The operational theorem is therefore about a compatible family
of local experiments, not an infinite-system unitary operator.

### 1.5 Honest fence: non-injective MPS and PEPS

All three routes use injectivity.  For a non-injective MPS, canonical form has
several normal blocks/peripheral fixed points: equal-state representations
need not select one minimal `M_χ` boundary algebra, the transfer map need not
converge to the rank-one projector `P`, and a half-string can retain
cutoff/sector data.  Consequently neither the single-algebra fundamental-
theorem conclusion, the `C_λ̃λ̃^m` mixing bound, nor the padded tomography
bijection of A1(c) transfers without extra block/sector choices.  Those
choices are GAUGE until an operational superselection measurement fixes them.

For PEPS the normal/injective fundamental theorem has a restricted analogue
(`refs/arxiv-2011.12127/TN-Review-main.tex:1951-1964`), but a two-dimensional
cut carries a boundary system whose size grows with perimeter, not one fixed
`M_χ`.  More importantly, topological and other non-injective PEPS require
MPO intertwiners (`:1966-1968`); the same review says the general MPS theorem
has no easy 2D generalization at `:1429-1433`.  The older local TeX is equally
explicit that the symmetry-to-virtual-tensor implication is “less straight”
in 2D (`refs/arxiv-0802.0447/StringOrder-v10.tex:430-451`).  Hence the
campaign's PT1--PT4 data can support an operational finite-annulus theorem
when instantiated, but the categorical PEPS typing itself is not yet a
state-functional boundary algebra for an arbitrary microscopic PEPS.

The amendment r1a to `theory/verdicts/reduction-defs-adjudication-r1.md` is
binding here: the fact that a QED boundary algebra is not a fixed finite
`M_χ` is a difference of physical theories, not a defect in the asymptotic-
symmetry scheme or in Corner A.  This audit asks whether the spin-chain
boundary algebra has its own experiments; sections 1.1--1.4 answer yes and do
not revive the withdrawn “finite `χ`” objection.

## 2. Definition audit: D1--D12

### D1 — **GAUGE**

The quasi-local algebra and state are physical, but D1's load-bearing MPS
tensor, canonical form, transfer matrix, boundary vectors, and virtual bond
decorations are a representation of that state.  No apparatus measures an
entry of `A^s` or inserts an arbitrary `M∈GL(χ)` on a virtual bond.  The
operational content is the family of reduced density matrices and their local
expectations, the measurable correlation length, and—by the injective
fundamental theorem—`M_χ` only up to isomorphism.  A decorated state becomes
operational only when a physical preparation is supplied (for example the
truncated symmetry in WI) and is then read by local tomography.  Action
needed: retain D1 as scaffolding but never call the chosen tensor or decoration
itself a state observable.

### D2 — **GAUGE**

The on-site unitary `u(g)` is executable and covariance of finite reduced
states is observable, but D2 packages these physical facts through tensors,
the intertwiner `V_α(g)`, its phase section, and the derivative `X_α(ξ)`.
Those entries change under MPS similarity and phase gauge.  The invariant
content is: which finite-volume symmetry leaves or permutes the vacuum
states, the stabilizer `H_α`, and the cohomology class inferred from endpoint
string experiments.  The measurement is finite-window state tomography
before and after `u(g)^⊗W`; the virtual IT equation is the gauge proof of that
physical covariance, not another experiment.

### D3 — **IMPLEMENTABLE**

For `f∈𝔉_c`, `U[f]` is a finite parallel product of prescribed on-site
unitaries, hence a depth-one control operation.  For an eventually constant
half-line profile, the only legitimate implementation is the sequence of
finite strings followed by local measurements: it is eventually exact on
fixed local algebras in A1 and has error
`C_λ̃||O||λ̃^(y-w)` in A2 for every `λ̃∈(λ_E,1)`.  A plane wave is not a
gate; a smooth momentum packet is prepared by its finite/truncated real-space
profile.  Thus D3 correctly separates executable controls from a formal
infinite product.

### D4 — **GAUGE**

`V(g)`, `N_α`, the left-multiplication map on `M_χ`, the padded-window
operator `𝒱_b`, the twisted group algebra, and `X_α(ξ)` are virtual
coordinates.  In particular, a linear map defined on `ran ι` is not thereby a
unitary or channel available on the full physical window Hilbert space.  The
operational content is the endpoint-state action `[V(g)]∈PGL(χ)`, its kernel
and orbit, and the multiplier class reconstructed through finite symmetry
strings and tomography.  D4 may state that invariant boundary algebra, but
any assertion that `𝒱_b(M)` itself is a laboratory bond gate needs a physical
CPTP extension and is not supplied here.

### D5 — **GAUGE**

The excitation tensor `B`, its location in an MPS word, and the null
coordinate `X` are ansatz data; many `B`'s represent the same generalized
vector, and D5 alone supplies no eigenvalue, pole, band isolation, creator, or
wave operator.  The operational content appears only after a spectral theorem
or the exact hypotheses of D28/D31 identify the quotient class with a
preparable particle packet.  Then spectroscopy and scattering measure the
band and S-matrix, never the raw `B` or `X`.  Action needed: keep the name
“excitation ansatz,” not “particle definition.”

### D6 — **IMPLEMENTABLE**

The finite-ring Heisenberg Hamiltonian is a realizable analog/digital
Hamiltonian and its time evolution is a quench operation; the all-up state and
local spin flips are standard preparations.  Momentum wave packets are made
by phase-patterned superpositions of flips, and energy/magnon number are read
by spectroscopy and spin-resolved detection.  Infinite-chain plane waves are
only kernels for these packet experiments.  The coordinate bases are a
description of the preparation, while the implemented Hamiltonian fixes their
physical meaning.

### D7 — **OBSERVABLE**

Once incoming and outgoing packet ordering is fixed, `|S_12|²` is obtained
from channel populations and the phase of `S_12` from interference with a
reference/no-scattering arm or full outgoing wavefunction tomography
**[physical argument]**.  Reversing the channel convention inverts the
amplitude but does not change the measured scattering operator.  The bound
dispersion and decay length follow from energy spectroscopy and spatial
correlations.  Thus the coefficient convention is bookkeeping, while the
channel S-matrix data defined by it are observable.

### D8 — **IMPLEMENTABLE**

D8 specifies a preparation-and-scan protocol: hold a hard packet inside a
chosen compact half-zone, prepare one-sided soft packets with successively
smaller signed carrier momentum, and keep the velocity ordering fixed.  Each
finite packet experiment is executable; the limit is an extrapolation of
those experiments, not a prepared `k=0` plane wave.  The measured outputs are
the D7 phase/probabilities and dispersion, and the excluded simultaneous or
wrong-channel limits prevent an operational channel relabelling midway
through the scan.

### D9 — **OBSERVABLE**

The vacuum-pair sector `(α,β)` is read by translating an informationally
complete local observable far to the left and right; for decorated injective
MPS the error decays exponentially.  Distinct pairs are therefore classical
asymptotic records unaffected by local operations.  Endpoint states in
`E_b^α` are distinguished by padded-window tomography via A1(c), and the
`G`-orbit is prepared by finite strings in the local weak-* sense.  The
representative rule `g⋆M=V(g)M` is gauge scaffolding inside this observable
definition; the measured objects are the tail labels and reduced states, not
`M` itself.

### D10 — **OBSERVABLE**

With the Hermitian convention `-iq_x`, the on-site charge, every finite
modulated charge `-iQ[f;ξ]`, and the cut current `-ij_b` are physical local
observables.  Measure the charge terms site-resolved and the current either by
direct bond measurement or from the change of charge on one side during a
short quench; the continuity equation cross-checks the two.  The virtual
potential `𝒥_b=X_α(ξ)` is gauge scaffolding and has no direct meter—the
operational statement it proves is the response of physical `q_x` on the
vacuum.

### D11 — **GAUGE**

`B_G(ξ)` is a derivative of an MPS tensor and its dimension modulo
`𝒩_0(X)` is a tangent-space count, not a detector outcome.  Its invariant
content is the physical charge-created packet
`Q_k(ξ)▹ω_α` and, when a Hamiltonian supplies an isolated mode, the number and
dispersion of Goldstone branches measured by dynamical structure factors.
The type-B deficiency must therefore be stated as a rank/response theorem for
physical charge correlators; the raw span of tensor entries remains gauge.

### D12 — **GAUGE**

D12 controls the boundary remainder generated by changing the ansatz
representative `B→B+𝒩_k(X)`.  The profiles, norms, and `O(|Λ|^-1/2)` statement
are mathematical controls on when two gauge representatives give the same
packet or delta-normalized matrix elements; no experiment measures
`𝔅_Λ[f,X]` as an independent object.  Its operational content is the
invariance of all physical packet observables under that replacement, with
the stated `ℓ¹∩BV`, `c_0`, or per-site limit and no stronger convergence
claim.

## 3. Definition audit: D13--D23

### D13 — **OBSERVABLE**

`𝔛_W` is a bounded local sum of commuting `S_x^z` measurements, so its
distribution and expectation are obtained by site-resolved spin readout on
the same finite window at the initial and final times; `δx` is their ensemble
mean difference.  The spectral dress measures the same finite-time endpoint
difference after integrating the local response.  Operationally it is a wall
coordinate only after fixing the kink core/dressing and keeping packet charge
outside `W`; otherwise internal charge rearrangement can mimic translation,
as the prior reduction audit found.  The first-moment dress is not a separate
memory measurement without a defined leg subtraction and is identically
conserved before that subtraction.

### D14 — **OBSERVABLE**

`N_R`, `N_T`, and `N_W` are asymptotic sums of site-resolved magnetization
relative to calibrated tail vacua.  On a D17 packet they are measured by
increasing the left, right, and central detection windows until the omitted
tail weight is below tolerance.  Repeated scattering shots give the
transmitted/reflected probabilities and their packet average.  This is a
counting measurement, and the definition correctly forbids replacing the
measured average by `T` evaluated at the mean momentum.

### D15 — **OBSERVABLE**

Reflection and transmission probabilities are the frequencies of separated
outgoing magnon detections on the two tails.  The complex phase `δ_t(k)` is
measured only with coherent phase-sensitive scattering—e.g. interference of
the transmitted packet with a calibrated reference packet—and its derivative
can be checked against the transmitted packet's spatial delay
**[physical argument]**.  It is not obtained from `T(k)` alone and, as D15
states, is not the D13 wall displacement.

### D16 — **IMPLEMENTABLE**

The finite-chain XXZ bond Hamiltonian is an executable analog/digital quench,
and its local terms can be calibrated spectroscopically.  The kink-normalizing
telescoping field is a boundary preparation/energy convention; in infinite
volume it does not change the local derivation.  Kink profiles can be prepared
with opposite boundary polarizations and their center and residual phase read
from local spin tomography.  The infinite product formula is a state
description, while finite-volume ground-state preparation followed by the
XXZ evolution is the physical operation.

### D17 — **OBSERVABLE**

Membership in the `ℓ¹` kink class is a statement about the measured tail
magnetization profile and, when used, its first moment.  It is approached by a
nested sequence of site-resolved windows and is falsified by persistent tail
mass; exact membership is an asymptotic property rather than one finite-shot
event.  Its operational content is precisely that the half-line charge and
wall moment can be estimated with a controllable truncation tail.  A plane
wave fails this experimental localization test, which is why packets must be
fixed before a soft limit.

### D18 — **GAUGE**

The Møller maps, chosen channel Hilbert spaces, identification `J`, and the
decomposition `ℋ_b⊕ℋ_sc` are an asymptotic representation of scattering, not
direct meter readings.  Their operational content is the existence of stable
in/out packet preparations, the exhaustive list of separated detector
channels, their measured probabilities and charges, and local relaxation near
the kink.  D18 is acceptable scaffolding only as an explicit hypothesis; a
claim whose content assumes `W_±` or channel completeness must restate those
as operational scattering conditions or flag them as uninstantiated.

### D19 — **GAUGE**

The compressed transfer operator `𝒞_C`, the fixed register `E_C=ℂ^χ`, its
basis, and the order in which a tensor contraction is taken are
representation-level data.  The finite profiles themselves are executable
local charge/string controls, but their identification with an edge register
requires H-split.  The invariant operational content is the limiting matrix
of physical boundary-response statistics after a physical edge realization
has been supplied; absent H-split, D19 is a numerical/tensor register only.

### D20 — **GAUGE**

`𝔉_{N,L}^{bulk}`, `ℜ_{C,L}`, and `𝕊_{C,L}^{comp}` are compressions through
chosen channel embeddings, tangent gauges, Gram normalizations, and a virtual
compensating insertion.  They are not themselves laboratory observables.
Their gauge-invariant content is in scalar matrix elements between physically
prepared channel states, or in a physically compressed edge operator under
H-split, measured by tomography/interferometry.  Continuity and H-soft-p are
analytic controls on that extraction and must not be presented as physical
operations.

### D21 — **GAUGE**

The Schmidt register, projective matrices, centered virtual generator, lift,
and charge-lattice offset are representation data until H-split supplies an
intertwining isometry into a physical half-chain edge space.  Under that
hypothesis the invariant consequences—edge degeneracy at least `d_ω`, the
centered charge spectrum, and its offset—are measured by edge spectroscopy
and symmetry action tomography.  The phase-gauge invariance of
`Q_edge=-iX_C^∘` is necessary but not by itself a preparation or measurement;
the physical-edge theorem remains conditional exactly as the definition says.

### D22 — **IMPLEMENTABLE**

At finite `L` the channel-free core is an explicit two-projective-measurement
operation: projectively measure the bounded local Hermitian charge `Q_L^∂` at
`t_-`, evolve under the physical Hamiltonian, measure the same charge at
`t_+`, and record `ν=q_-−q_+` (or `m=-ν`).  Repetition gives the probability
law.  The ordered Cesàro/window limit is a limit of these executable
protocols, with E-LR supplying convergence/tightness rather than another
observable.  The virtual ordered products and the optional channel operator
are gauge scaffolding; neither H-AD-edge nor a wave operator is required for
the finite TPM experiment.

### D23 — **GAUGE**

The exact tensors, their virtual Pauli matrices, range maps, and tensor paths
are construction coordinates.  What they operationally determine are local
parent and boundary Hamiltonians: those Hamiltonians can be implemented and
their ground/edge spectra measured, independently of which tensor gauge was
used to derive them.  Accordingly, comparisons must be phrased as statements
about the physical `H_{C,+}` spectrum, symmetry, gap, or edge response; a
difference between raw tensors is not itself a phase measurement.  The
specific open-AKLT Hamiltonian does remove an ambiguity in a future scattering
experiment, but it does not make the tensor coordinates observable.

## 4. Definition audit: D24--D31

### D24 — **IMPLEMENTABLE**

A local source is enacted by a finite source pulse coupling to its Hermitian
components, or by a displayed ancilla/postselected Kraus operation; an
exponentially quasi-local source is approximated by finite partial sums in
norm, with error bounded by the omitted `Σ_X||O_X||`; D24's diameter weight
alone does not give a distance-from-origin rate **[textbook]**.  The resulting one- and
two-particle amplitudes are obtained by asymptotic packet preparation and
phase-sensitive scattering tomography in the fixed D24(b) normalization.
What is not automatically operational is membership in the engineered
five-clause class `𝒮_W(ρ)`: it must be verified from those scattering data and
is not known to have a microscopic member.  Thus D24 defines executable
sources, but its conditional factorization class must be advertised as a
bootstrap criterion, not as an already populated physical universality class.

### D25 — **OBSERVABLE**

If the proposed multiplier exists, it is a ratio of packet-smeared physical
S-matrix elements with and without the additional soft leg.  Its magnitude is
measured from channel statistics and its phase by interferometry; scanning the
soft packet tests the linear zero and remainder.  Dependence only on measured
charges and velocities is an empirical universality claim.  This operational
classification does not promote `S-general`: existence, factorization,
`𝒮_W` membership, and process independence remain CONJECTURE as recorded.

### D26 — **OBSERVABLE**

The Hermitian on-site circle charge has a finite spectral PVM; single-site
spectroscopy determines its coset `κ+ℤ`, and a `2π` rotation checks the common
phase `c`.  Finite-window sums are measured by simultaneous site-resolved
charge readout.  D26 therefore has direct operational content, but it measures
a compact on-site matter charge: the prior reduction audit correctly forbids
renaming it a generic angle-dependent QED large-gauge charge or a radiative
memory field.

### D27 — **IMPLEMENTABLE**

For every finite `W`, D27 instructs the experimenter to measure the bounded
wall charge `Q̂_{W,c_0}`, evolve, measure it again, and form the escaped
increment.  Repeating at the two time slabs produces the double-Cesàro TPM
weights, and repeating for a padded exhaustion realizes the stated ordered
sequence of finite experiments.  LR2--LR3 are convergence/nondemolition
hypotheses, not extra gates.  Operationally this is compact-charge full
counting statistics and a wall-charge ledger; without a reconstruction theorem
it is not generic electromagnetic/gravitational field memory.

### D28 — **GAUGE**

The exact ansatz frames `Γ_K,Γ_M`, Gram normalization, filters, Wannier
vectors, and two-cluster inequality are representation-level hypotheses.  An
apparatus instead sees isolated energy-momentum bands, localized packet
creators, separated detector channels, and scattering probabilities.  The
content of AC-EX can be operationally re-anchored to those spectral and
clustering properties, but the claim that a chosen finite-core ansatz frame is
an exact band map is not itself measured and is unverified on every model in
this kink register.  D28 also excludes the soft endpoint, so it cannot by
itself operationalize a soft-limit statement.

### D29 (PROPOSED) — **IMPLEMENTABLE**

At every admissible finite index, prepare the hard packet, apply the smeared
physical charge `Q[f_ε]`, evolve for the declared settling time, and compare
the interacting two-magnon state with the freely evolved reference on the
chosen momentum window.  The complex overlap/projection ratio can be obtained
by controlled-interference/Hadamard tests or full two-magnon tomography
**[physical argument]**; its Fourier kernel is a readout convention, not a
virtual tensor.  The operation is finite and exact, with `N,T,W,σ` taken to
their outer limit at fixed `ε` and `ε↓0` last.  It is not an LSZ soft-leg
amplitude in general; equality of readouts is PROVED only on D29-HS-SEP, and
the proposed status remains quarantined.

### D30 (PROPOSED) — **OBSERVABLE**

TGT asserts nondegeneracy, tightness, clusterability, and `C¹` regularity of
the measured D29 ratios and row measures along a stated scaling sequence.
These are properties inferred by repeating the finite D29 experiment over
increasing indices and soft scales; they are not a physical operation of their
own, but their entire scalar content is in observable statistics.  Any
component compactness imported from a separate decomposition inherits that
decomposition's hypothesis.  Crucially, the data admit the Möbius/phase shift
that moves the jet while preserving regularity, so D30 cannot operationally
fix a soft coefficient or smuggle in on-shell matching.

### D31 — **GAUGE**

The exact map `Γ_M`, filtered almost-local creators, packet frames, and channel
inventory are a representation chosen to prove Cook limits.  Their
operational content is an isolated charge-one spectral band, preparable
localized packets with separated velocities, exclusion of listed competing
bands by spectroscopy, and the resulting two-particle S-matrix.  D31-C2/C4
are state-correlation estimates and hence testable through separated local
correlators, but the assertion that a particular ansatz map is exact should be
replaced by spectral-projector language in any theorem statement meant to be
representation independent.  No fixed-packet estimate here supplies a
uniform soft limit.

## 5. Requested claim-level objects

### Bond implementer `V(g)` — **GAUGE**

The virtual unitary and its phase are fixed only up to conjugation and
`V(g)→e^{iφ(g)}V(g)`; neither is a physical bond gate.  The padded-window map
`𝒱_b(V(g))` is likewise only a linear operator on an ansatz subspace unless a
physical channel extension is provided.  Its operational content is the
state-level projective transformation `[V(g)]`, prepared by a finite symmetry
string and reconstructed from endpoint reduced states, plus the invariant
multiplier class.  Any statement about matrix entries of `V(g)` must therefore
be replaced by conjugacy/projective data.

### Endpoint states `ω_A^{M@b}` — **OBSERVABLE**

An endpoint state is a positive functional, hence its physical content is the
statistics of local POVMs.  Informationally complete tomography on a window
padded by at least `n_0` sites on each side distinguishes every endpoint point
`[M]∈PGL(χ)` by A1(c); increasing windows checks consistency.  Symmetry-orbit
members are prepared locally by long finite strings, exactly on fixed windows
in A1(a).  The representative matrix `M` is gauge and need not be an
available microscopic gate, but the reduced-state family is observable.

### Projective class `[ω]∈H²(G,U(1))` — **OBSERVABLE**

`[ω]` is invariant under MPS gauge and phase-section changes.  It is inferred,
not read by a single Hermitian meter: measure the PGL endpoint action for a
generating set through string preparation and padded tomography, reconstruct
the multiplication/obstruction to an honest unitary lift, and identify its
cohomology class **[physical argument]**.  Equivalently, symmetry-resolved
string-order selection rules and physical-edge projective tomography under
H-split diagnose it.  A single state-level composition hides scalar phases,
so the full family of endpoint actions—not one density matrix—is required.

### Truncated symmetry `U_R(g)` — **IMPLEMENTABLE**

It is a finite depth-one product of calibrated on-site unitaries.  The
experiment applies the gates in parallel on `R`, then measures local
observables near either endpoint.  WI predicts the exact finite-window
statistics and fixes the endpoint orientation.  The formal half-infinite
symbol has only the controlled weak-* implementation of sections 1.2 and 1.4
and is not a separate infinite operator.

### Modulated charge `Q[f]` — **OBSERVABLE**

For finite real `f`, the Hermitian charge `Q^H[f]=-iQ[f]` is a bounded sum of
on-site charge observables and is measured by weighted site-resolved readout;
its exponential can also be implemented as parallel phase rotations.
Wave-packet versions are limits of rapidly decaying/truncated profiles.  A
bare nonzero-momentum plane-wave sum is neither a quasi-local observable nor a
gate and has meaning only inside the specified packet Fourier transform.

### TPM protocol and escaped-charge law — **IMPLEMENTABLE**

Measure the same finite-window charge PVM at `t_-` and `t_+`, with physical
evolution in between, and classically record `ν=q_-−q_+`; this is a standard
sequential quantum instrument even when the two Heisenberg observables do not
commute.  Repeated runs yield the escaped-charge probability law.  D22/D27's
ordered infinite limits are limits of these implementable finite protocols;
tightness and nondemolition are hypotheses on their measured statistics, not
an assumed difference operator.

### Windowed wall coordinate `𝔛_W` — **OBSERVABLE**

All summands commute and are local, so a single site-resolved magnetization
shot produces an eigenvalue of `𝔛_W`; ensembles give its expectation and
before/after change.  Its interpretation as translation requires a fixed,
centered wall core and controlled exterior packet charge.  Without that
calibration it remains an observable, but it observes total window
magnetization rather than uniquely observing wall position.

### Two-magnon physical phase `δ_phys` — **OBSERVABLE**

After fixing the incoming/outgoing velocity convention, coherently scatter a
hard packet with a narrow soft packet and interfere the outgoing channel with
a calibrated reference to recover the phase of `S_phys`; packet tomography is
an alternative **[physical argument]**.  Repeating for signed soft carriers
determines its slope.  Population measurements alone determine `|S|²`, not
`δ_phys`, and the continuous branch convention must remain fixed across the
scan.

### Fixed-time protocol datum (proposed D29) — **IMPLEMENTABLE**

The finite datum is obtained by charge-created packet preparation, a physical
quench for time `T`, and an interferometric projection against the explicitly
prepared free reference over a chosen momentum window.  Every finite ratio is
therefore operational; the admissibility and order of limits prevent an empty
fixed-`N` soft sample.  Its equality to the asymptotic S-matrix readout is a
separate theorem on D29-HS-SEP and otherwise fails already at the sought
`O(k_s)` order, so “fixed-time datum” and “LSZ amplitude” must remain distinct.

### Excitation-ansatz tensors `B` and gauge data `X` — **GAUGE**

`B` is a coordinate in a tensor tangent space and `X` generates a null change
`B→B+e^{ik}AX-XA`; neither has a detector.  The invariant content is the
packet/generalized physical vector modulo the D12 boundary remainder and,
only with exact spectral input, its energy band and S-matrix.  Gauge fixing,
Gram normalization, and continuity of `B` along a path are proof choices, not
physical hypotheses unless rewritten as smoothness of spectral projectors and
measured form factors.

### PEPS hypothesis PT1 (tube PVM) — **GAUGE**

An abstract representation of `Tub(𝒞)` and its central idempotents is
categorical/PEPS typing.  Its operational content would be a physically
specified annular PVM whose outcomes are the sectors `a`; outside the toric
code the campaign has not supplied that microscopic measurement.  A theorem
may assume the PVM algebraically, but an experimental claim must provide the
annular operators and their measurement circuit.

### PEPS hypothesis PT2 (pure endpoint) — **GAUGE**

The tensor equation `P_y^end T_x=δ_yxT_x` labels a PEPS/ribbon
representative.  Its operational content is a deterministic small-circle
sector outcome `x` under a specified endpoint PVM.  Until a microscopic
endpoint preparation and that PVM are given, “pure endpoint” is a typing
hypothesis and not an observed quasiparticle label.

### PEPS hypothesis PT3 (pulling-through module action) — **GAUGE**

Zipper, associator, and pulling-through equations are representation-level
identities.  Their invariant, checkable consequence is the zero probability
for forbidden annular transitions and the allowed fusion support
`N_xa^b>0`.  Thus the equations may prove a selection theorem, but the theorem
should be stated as support of physical PVM/Kraus statistics rather than as
direct observability of a tensor deformation.

### PEPS hypothesis PT4 (protocol instrument) — **IMPLEMENTABLE**

PT4 is precisely the missing physical operation: either a normalized family
of channel-resolved Kraus maps is enacted, or one displayed Kraus outcome is
postselected and its success probability recorded.  Process tomography can
verify normalization.  Category data do not generate this instrument, so its
existence remains a model-specific hypothesis even though, once supplied, it
is an executable protocol.

### Toric-code row's endpoint label `x` — **OBSERVABLE**

For the finite toric-code instance, apply the open Pauli ribbon and measure the
same electric/magnetic boundary PVM before and after; the outcome shift is the
definite label `x`.  A closed complementary ribbon measures the associated
braiding character and distinguishes all four labels.  This is an anyon/ribbon
endpoint label, not a D9 one-dimensional kink label; its operational status is
secured by the explicit finite PVM and Pauli-string experiment in
`A-INDEX-TC-fin`.

## 6. Re-anchor list: statements whose content still names representation data

The following list is exhaustive at the level of campaign statement families:
it includes a row when changing a tensor, ansatz frame, edge register, rigging,
or categorical realization changes an object quantified over in the
**statement**, not merely a convenient proof.  “Restate” means the public
statement should quantify over the operational column; “flag” means the gauge
statement may remain but must be identified as conditional scaffolding.

| Campaign statement/content | Representation dependence | Required operational anchor | Action |
|---|---|---|---|
| D1--D2 tensor/canonical/IT data | `A,E,r,V,X` and phase/basis sections change with the MPS representative. | Reduced density matrices, measured symmetry action, correlation decay, and `[ω]` reconstructed from strings; retain only algebra/isomorphism and conjugacy classes. | restate |
| WI window-vector identity | The vector decoration and the two virtual insertions are tensor coordinates. | Lead with WI-state: apply finite `U_R(g)` and compare local reduced states near the two endpoints; keep the vector identity as its GAUGE proof. | restate |
| A1(d1), D4 charge algebra, and the unproved GNS edge action | `𝒱_b` acts on a padded MPS image and need not extend to a physical unitary/channel; the GNS realization is SKETCH. | State the `PGL(χ)` action on tomographed endpoint states and the obstruction class; any physical edge-Hilbert action must carry H-split or an explicit CPTP realization. | flag |
| A1(g) phase-path statement | Its current antecedent is a path of canonical tensors. | Use a continuous symmetric path of physical states/gapped Hamiltonians whose injective canonical representatives exist; the measured invariant is local constancy of the endpoint projective class. | restate |
| D5, D11, D12 and G0(a)--(c) | `B`, `B_G`, `X`, tangent gauge, and the SBP remainder are ansatz coordinates. | State physical charge-created packet identities and dynamical-structure-factor/spectral-band consequences; keep the tensor null-direction theorem as GAUGE. | restate |
| G0(d)'s bond “potential” | `𝒥_b=X_α(ξ)` is virtual. | The operational claim is the equality of local charge-response matrix elements with differences of endpoint responses prepared by finite strings; G0(e)'s continuity equation is already physical. | restate |
| D19--D20, SPT-B-mult, and SPT-B' registered coefficients | Transfer compressions, channel embeddings, Gram gauges, and `V⊗V̄` are chosen registers. | Express conclusions as finite closed-string/charge correlation matrices between prepared states; require physical channel embeddings for any operator claim. | restate |
| D21 and SPT-E-AKLT/SPT-E'/SPT-T'/SPT-D' | The Schmidt register, `Q_edge`, ordered `V` products, and registered residues are virtual until H-split/H-dress. | Under H-split/H-dress, use edge spectroscopy, symmetry-operation tomography, and endpoint interference; without them the rows are GAUGE algebra and must say so. | flag |
| D23 comparison tensors | Raw tensor paths and virtual Pauli actions are not phase observables. | Compare the implementable parent/boundary Hamiltonians by gap, ground-state, symmetry, and edge-response measurements. | restate |
| D24(d)'s `𝔞_leg` and claims ML5-B, D24-VAL, AMP, S-IDX-spec-struct-r2/S-IDX-spec-r2 | The constant depends on the D24(b) external-leg/amputation normalization; `𝒮_W` membership is uninstantiated. | Fix the physical packet calibration explicitly and report the observable S-matrix phase jet; otherwise carry `𝔞_leg` as convention-dependent GAUGE data and flag nonemptiness. | flag |
| D28 and AC-EX | Exact finite-core ansatz frames, `Γ_K,Γ_M`, and D28-C are hypotheses about a chosen representation, unverified on every model. | Replace exact-ansatz language by isolated physical spectral projectors, localized creator preparations, uniform physical cluster estimates, and detector-defined channel separation.  The resulting Cook/S-matrix conclusion then survives. | restate |
| D31, AC-EX-2M, ML1-D31-kernel, and S-IDX-HR-value-r2 | `Γ_M`, its rigging, filtered creator equality, and the supplied inventory are exact frame data. | Quantify over the physical charge-one spectral band/projector, almost-local creators calibrated on the vacuum, and spectroscopic exclusion of other channels; the D6 S-matrix conclusion is representation independent. | restate |
| Proposed D29/D30 component decompositions and AC-EX-2M-D29/S-IDX spectral uses | Fourier coordinates are harmless, but identifying the fixed-time charge state with an asymptotic creator changes the first jet at `O(k_s)`. | Keep D29 as its finite interferometric protocol; require the separately named matching theorem.  Use S-IDX-MATCH-HS-SEP only on D29-HS-SEP and do not infer general LSZ equality. | flag |
| PT1--PT3 and A-INDEX-PEPS/FUSION-SOFT | Tube idempotents, pure endpoint tensors, and pulling-through modules are categorical PEPS typing, not supplied microscopic instruments beyond toric code. | Provide physical annular/small-circle PVMs and endpoint Kraus maps; state the conclusion as zero support for forbidden measured fusion outcomes. | flag |
| SHAPE-FLAT | Equality is asserted inside an exact fixed-point MPO/string representation and after associator identifications. | State path invariance of code-space matrix elements measured with resolved endpoints, or retain the row as a fixed-point GAUGE theorem; no off-fixed-point extension without a quasi-adiabatic physical construction. | flag |

## 7. Operational survivors and unchanged status boundary

Several major conclusions do **not** depend in content on a tensor
representative.  A2's sector jump is detected from physical tail states;
G0(e) is an operator continuity equation; D13/D14 and the M-INDEX-fin/spec
rows are local magnetization/TPM statements; `A-INDEX-TC-fin` is an explicit
finite Pauli/PVM experiment; and the finite core of SPT-M' is the same-window
charge TPM arithmetic, with the SPT interpretation only conditional on the
flagged edge register.  `M-IDX-density` also states a physical density
quantization even though IT is used in its proof.

The S-matrix conclusions are prime survivors.  `S2-2body`,
`S2-2body-S`, OR1/OR2, ML1's D6 scattering operator,
`S-IDX-MATCH-HS-SEP`, `S-IDX-D29-value-HS-SEP`, and
`S-IDX-PROTO-SCALAR-HS-SEP` concern packet scattering probabilities or
interferometric phases once their explicit physical packet hypotheses hold.
Changing `B`, `X`, `Γ`, an MPS gauge, or a channel basis conjugates the
description but cannot change the measured on-shell phase.  Conversely,
conditionality and nonvacuity fences remain: operational meaning does not
turn an unproved band hypothesis, PEPS instantiation, source-class member, or
soft-uniform limit into an established one.  No status in
`claims/CLAIMS.md` is changed by this audit.

## 8. Closing status/action table

| Object | Status | Experiment or gauge-invariant content | Action needed |
|---|---|---|---|
| Injective-MPS boundary algebra | OBSERVABLE | Finite string interferometry plus padded reduced-state tomography reconstructs `M_χ` up to isomorphism, the endpoint torsor, and `[ω]`; finite strings approximate the state action with the section 1.2 rate. | none |
| D1 | GAUGE | Tensor/canonical/transfer/decorations; invariant content is the physical state, reduced densities, correlations, and abstract boundary algebra. | flag |
| D2 | GAUGE | `V,X,θ` are coordinates; finite reduced-state symmetry tests and `[ω]` are invariant. | restate |
| D3 | IMPLEMENTABLE | Depth-one finite on-site strings; weak-* half-string state preparation, exact in A1 and exponentially controlled in A2. | none |
| D4 | GAUGE | Virtual left multiplication; operational content is the string-induced `PGL(χ)` endpoint action and multiplier class. | restate |
| D5 | GAUGE | `B` modulo `𝒩_k(X)`; physical particle content requires a spectral band/creator theorem. | flag |
| D6 | IMPLEMENTABLE | Prepare spins/magnon packets and quench with the finite Heisenberg Hamiltonian. | none |
| D7 | OBSERVABLE | Channel populations, bound-state spectroscopy, and interferometric S-matrix phase. | none |
| D8 | IMPLEMENTABLE | Fixed-hard/one-sided-soft packet preparation and momentum scan in a fixed velocity channel. | none |
| D9 | OBSERVABLE | Tail tomography reads `(α,β)`; padded tomography reads endpoint states. | none |
| D10 | OBSERVABLE | Site charge, weighted charge, and cut-current measurements; virtual `𝒥` only proves the response identity. | restate |
| D11 | GAUGE | Tensor tangent and quotient count; invariant content is physical charge response and spectral Goldstone modes. | restate |
| D12 | GAUGE | Null-representative boundary remainder; content is invariance of packet observables in the named topology. | flag |
| D13 | OBSERVABLE | Site-resolved `S^z` gives `𝔛_W` and its before/after expectation. | restate |
| D14 | OBSERVABLE | Left/right/central magnetization counting after scattering. | none |
| D15 | OBSERVABLE | Outgoing channel counts and coherent phase/delay measurement. | none |
| D16 | IMPLEMENTABLE | Finite XXZ quench with boundary-polarized kink preparation. | none |
| D17 | OBSERVABLE | Growing-window tail magnetization and first-moment convergence. | none |
| D18 | GAUGE | Møller/channel representation; content is exhaustive detector channels, probabilities, charges, and local decay. | flag |
| D19 | GAUGE | Transfer/Schmidt register; physical edge response only after H-split. | flag |
| D20 | GAUGE | Compressed operator with chosen embeddings/gauges; physical matrix elements require prepared states/edge realization. | flag |
| D21 | GAUGE | Virtual edge module/lift/offset; conditional content is edge degeneracy and charge spectroscopy under H-split. | flag |
| D22 | IMPLEMENTABLE | Same finite boundary charge measured twice around a physical evolution; repeat for the TPM law. | none |
| D23 | GAUGE | Comparison tensors; invariant content is the implementable parent/boundary Hamiltonian and its spectrum. | restate |
| D24 | IMPLEMENTABLE | Local/quasi-local source pulse and asymptotic scattering tomography in a fixed calibration. | flag |
| D25 | OBSERVABLE | Conditional soft S-matrix ratio, magnitude, phase, and momentum scaling. | flag |
| D26 | OBSERVABLE | On-site charge spectroscopy and `2π` rotation phase. | restate |
| D27 | IMPLEMENTABLE | Finite-window wall-charge TPM repeated over time slabs and window exhaustion. | restate |
| D28 | GAUGE | Exact ansatz frames and D28-C; physical anchor is spectral bands, localized creators, clustering, and detector channels. | restate |
| D29 (proposed) | IMPLEMENTABLE | Charge-created packet, finite quench, and interferometric overlap with the free reference. | flag |
| D30 (proposed) | OBSERVABLE | Scaling regularity/tightness of repeated D29 readouts; no coefficient fixed. | flag |
| D31 | GAUGE | Exact band map/rigging/inventory; physical anchor is spectral projectors, calibrated creators, and channel spectroscopy. | restate |
| Bond implementer `V(g)` | GAUGE | Only `[V(g)]`, its conjugacy data, and `[ω]` survive tensor/phase gauge. | restate |
| Endpoint states `ω^{M@b}` | OBSERVABLE | Informationally complete padded-window tomography; symmetry orbit prepared by finite strings. | none |
| Projective class `[ω]` | OBSERVABLE | Reconstruct the endpoint PGL action/string-order selection rules and infer the lift obstruction. | none |
| Truncated symmetry `U_R(g)` | IMPLEMENTABLE | Parallel finite on-site gates followed by endpoint measurements. | none |
| Modulated charge `Q[f]` | OBSERVABLE | Weighted site-charge measurement of `Q^H=-iQ`; packet limit for noncompact profiles. | none |
| TPM protocol and escaped-charge law | IMPLEMENTABLE | Sequential PVM, evolution, second PVM, and repeated-shot frequency law. | none |
| Windowed wall coordinate `𝔛_W` | OBSERVABLE | Commuting site magnetization PVM and ensemble mean. | restate |
| Two-magnon phase `δ_phys` | OBSERVABLE | Coherent outgoing/reference interference with a fixed channel convention. | none |
| Fixed-time D29 datum | IMPLEMENTABLE | Finite charge insertion, quench, momentum-window overlap/tomography. | flag |
| Ansatz `B` and gauge `X` | GAUGE | Only the quotient physical packet and any independently established spectral data are invariant. | flag |
| PT1 tube PVM | GAUGE | Abstract tube-algebra idempotents; needs a microscopic annular PVM circuit. | flag |
| PT2 pure endpoint | GAUGE | Tensor typing; needs deterministic small-circle sector measurement. | flag |
| PT3 pulling-through action | GAUGE | Tensor identities; physical content is zero probability of forbidden fusion outcomes. | flag |
| PT4 protocol instrument | IMPLEMENTABLE | Normalized Kraus family or recorded postselected Kraus operation, once supplied microscopically. | flag |
| Toric-code endpoint label `x` | OBSERVABLE | Same-circle electric/magnetic PVM shift and complementary closed-ribbon braiding character. | none |
