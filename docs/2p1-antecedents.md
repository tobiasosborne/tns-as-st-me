<!-- ROLE: reference digest for the 2+1 lift (lane W5 of bd tns-7pp).
     AUTHORED by subagent per TJO task, 2026-08-29. Ground truth per L3:
     every quoted phrase below is transcribed from local TeX under
     refs/arxiv-<id>/, with file+line. Not itself a claim in claims/CLAIMS.md;
     theory shards cite the refs/ source, not this file. Companion to
     docs/continuum-antecedents.md (the 1+1/4d digest). -->

# 2+1 antecedents: what the literature says the lattice triangle can and cannot be

Thirteen sources, Batch 4 of `refs/LEDGER.md`. Written against TJO's read that
in 2+1 **asymptotic symmetry is understood, memory is tractable, and the soft
theorem is the unknown**. Corner vocabulary as in
`HANDOFF_MPS_SOFT_THEOREM.md`: **A** = asymptotic symmetry / charge algebra,
**B** = memory, **C** = soft theorem.

---

## (a) Soft theorems in 2+1 / 3D

### 1. Cotler–Jensen–Prohazka–Riegler–Salzer, arXiv:2411.13633 — *Soft gravitons in three dimensions*

The single most important antecedent. Working in 3d flat-space quantum gravity
coupled to massless matter, they find "**three equivalent results: a soft
graviton theorem, an infinite-dimensional BMS asymptotic symmetry, and a
gravitational memory effect**" — explicitly "despite the absence of a
propagating graviton" (`arXiv_v1.tex` L.93). The mechanism is that pure 3d
gravity is rewritten as a *magnetic Carrollian theory living on null infinity*
with Schwarzian-like boundary degrees of freedom (same line); the soft mode is
therefore a **boundary/edge degree of freedom**, not a bulk particle, and the
"soft theorem" is a Ward identity for supermomentum / super-angular momentum
that is "nothing more than the far-field limit of the constraint equations"
(L.111). Their memory is a **radial** displacement — "a 'rotational
displacement' memory effect and a 'time displacement' memory effect visible at
leading order in 1/r … Unlike in four spacetime dimensions these memory effects
describe a permanent radial displacement rather than angular displacements"
(L.1307).

*What the lattice 2+1 statement should therefore claim:* that the soft insertion
is a **boundary/virtual-level mode of the 2+1 state**, and that the soft theorem
is a constraint (Gauss-law / Ward) identity relating that insertion to the
in/out hard data — not an amplitude with a bulk 1/ω pole. *What it should
avoid:* asserting a bulk propagating soft quantum in a gapped 2+1 phase; the 3d
lesson is precisely that the triangle can close with **no bulk radiative mode at
all**, provided the boundary sector is retained.

### 2. Batlle–Campello–Gomis, arXiv:1703.01833 — *Canonical Realization of (2+1)-dimensional Bondi-Metzner-Sachs symmetry*

Constructs "canonical realizations of the bms3 algebra as symmetry algebras of a
free Klein–Gordon field in 2+1 dimensions, for both the massive and massless
case" (`main.tex` L.110ff), in two forms: on-shell in terms of Fourier modes,
and off-shell with **non-local** transformations of the field and its momenta;
Noether charges are given for both supertranslations and superrotations. This is
the cleanest demonstration that corner A in 2+1 needs **no gravity and no gauge
field** — a free matter field already carries an infinite-dimensional charge
algebra.

*Claim:* a lattice 2+1 corner A can be built directly from the mode expansion of
a gapless (or quasiparticle) sector, by transplanting this construction. *Avoid:*
reading this as evidence for a soft theorem. The charges here are *constructed*
and shown to close; nothing in the paper derives a soft limit from them. It is a
precise instance of "A is understood, C is not".

### 3. Shimizu–Sugishita, arXiv:2503.20173 — *Asymptotic symmetry and confinement in three-dimensional QED*

The sharpest warning in the batch. They show that the asymptotic symmetries of
3d QED have "**trivial** actions on asymptotic states … under the assumption of
confinement" (`arxiv_v1.tex` L.79), because "in three dimensions … asymptotic
charged particles are prohibited to exist by the finite energy condition. This
is the logarithmic confinement of QED₃" (L.179–180) — the classical potential
"diverges as a logarithm of the distance" (L.143). They conclude with "the
absence of the memory effect in three-dimensional electromagnetism with finite
energy conditions" (L.454), and note the soft-photon integral has an IR
divergence at k→0 reflecting the same obstruction (L.557). Note the author
overlap with 1709.05018 (Hamada–Sugishita), our 4d soft-pion template.

*Claim:* nothing, until the 2+1 model's *charged/soft sector is shown to have
finite-energy asymptotic states*. *Avoid:* any 2+1 soft theorem stated for a
sector whose charges are confined or logarithmically dressed — the whole triangle
degenerates to 0=0 there, and it will look like a proof.

*(Scalar-soft context for 2+1 is already in Batch 1: 1703.07885
Campiglia–Coito–Mizera and 2504.10577; the 4d soft-pion triangle is 1709.05018.)*

## (b) Memory in 2+1 and the odd-dimension subtleties

### 4. Satishchandran–Wald, arXiv:1712.00873 — *Memory effect for particle scattering in odd spacetime dimensions*

Direct computation of memory for point-particle scattering in odd d. Verdict:
"there is **no gravitational memory effect in all odd dimensions**. For scalar
and electromagnetic fields, there is no memory effect for d≥7; **for d=3 there
is an infinite momentum memory effect**, whereas for d=5 … the displacement of a
test particle will grow unboundedly with time" (`PRD_final_odd_Memory.tex`
L.31). The d=3 mechanism is a **tail**: "the force decays in time only as
1/√U, so for any U₀, the integrated effect of the force on the momentum for all
U > U₀ is never negligible. In this sense, there is an infinite momentum memory
effect for d=3" (L.221; EM case L.311; summary L.526).

*Claim:* in 2+1 the memory observable should be a **momentum/velocity kick**, and
its natural statement is a *rate* or a regulated/finite-window quantity. *Avoid:*
defining 2+1 memory as a permanent displacement and expecting a finite number —
in the continuum d=3 that number diverges. This is the single most concrete
"what 'memory' means changes in 2+1" warning.

### 5. Garfinkle et al., arXiv:1702.00095 — *The Memory Effect for Particle Scattering in Even Spacetime Dimensions*

The companion even-d computation: "there is no memory effect in d>4 dimensions"
(`main.tex` L.39, L.431). Together with 1712.00873 it establishes that **d=4 is
the exceptional case**, not the generic one: the familiar permanent-displacement
memory is a 4d accident, and every other dimension either has none or has a
divergent/tail-dominated substitute.

*Claim:* the 1+1 lattice memory result the campaign already has should not be
presented as "the generic dimension-independent statement". *Avoid:* a 2+1 paper
sentence of the form "as in four dimensions, memory is a permanent shift".

### 6. Satishchandran–Wald, arXiv:1901.05942 — *The Asymptotic Behavior of Massless Fields and the Memory Effect*

Provides the vocabulary this campaign needs. Two orders in the 1/r expansion are
named: "we refer to the leading (slowest fall-off) term n = d/2 − 1 as
*radiative order*, and we refer to the term with 1/r^{d−3} fall-off as
*Coulombic order*" (`main.tex` L.179). Memory "first arises at Coulombic order"
and splits into "**null memory**" (associated with energy flux to null infinity)
and "**ordinary memory**" (the metric failing to be stationary one order faster
than Coulombic, generic when matter comes in or goes out at less than the speed
of light) (L.49, L.76). Crucially: "**in odd dimensions … the total memory
effect at Coulombic order and slower fall-off always vanishes**" (L.49), and
scalar-type memory is a diffeomorphism that is an asymptotic symmetry only in
d=4 (a mere gauge transformation for d>4), while vector and tensor memory are
not diffeomorphisms at all (L.49).

*Claim:* a 2+1 lattice memory claim must say **which order** it lives at, and
must separate the flux-driven ("null") piece from the ordinary piece — the two
have different lattice observables and only the flux piece is tied to the soft
sector. *Avoid:* the analysis is stated for **d ≥ 4** and does not cover d=3;
d=3 must be taken from 1712.00873 instead. Note also the order inversion: at
d=3 the formulas give radiative 1/r^{1/2} but Coulombic 1/r⁰, i.e. Coulombic
does not decay and is *slower* than radiative, the reverse of d>4. Flag that as
an extrapolation outside 1901.05942's stated scope, not as their result.

### 7. Pate–Raclariu–Strominger, arXiv:1707.08016 — *Color Memory*

Memory as **holonomy**, not displacement: "a pair of test 'quarks' initially in
a color singlet generically acquire net color as a result of the flux. A
nonlinear formula is derived for the relative color rotation of the quarks. For
weak color flux the formula linearizes to the Fourier transform of the soft
gluon theorem" (`main.tex` L.352 and abstract). The memory reads off the change
between initial and final flat connections on the celestial sphere (L.409).

*Claim:* for a 2+1 topologically ordered lattice state the memory observable
should be the **change in a parallel-transport/holonomy datum of a string
operator encircling the region** — an object that survives when there is no
propagating radiation to displace anything. This is the observable shape that
composes with 1511.08090's sector labels. *Avoid:* the linearization to a soft
factor is only valid for *weak* flux; the exact statement is nonlinear, so a
lattice "memory = soft factor" identity should carry a weak-flux hypothesis.

## (c) Soft theorems and asymptotic symmetries for non-invertible / categorical symmetries

### 8. García Etxebarria–Iqbal, arXiv:2211.09570 — *A Goldstone theorem for continuous non-invertible symmetries*

They "study systems with an Adler–Bell–Jackiw anomaly in terms of non-invertible
symmetry", present "a new kind of non-invertible charge defect where a key role
is played by a **local current operator localized on the defect**", with defects
"labeled by elements of a continuous U(1)", and use this to "**prove an analogue
of Goldstone's theorem for such non-invertible symmetries**" (`draft07.tex`
L.208–215). This is, as far as this recon found, the only existing Goldstone
theorem for a non-invertible symmetry.

*Claim:* a categorical 2+1 soft theorem may legitimately assume a gapless mode
when the continuous categorical symmetry is spontaneously broken — that input is
now a theorem, not a hope. *Avoid:* writing the Ward identity with a bulk
Noether current. The current here lives **on the defect**; the lattice statement
must be a defect-supported (MPO-string-supported) Ward identity, which is a
different object from the 1+1 corner-A identity the campaign already proved.

### 9. Choi–Lam–Shao, arXiv:2205.05086 — *Non-invertible Global Symmetries in the Standard Model*

For every rational angle 2πp/N they construct a conserved, gauge-invariant
topological operator implementing the ABJ-anomalous axial rotation; these
operators "do not obey a group multiplication law, but a **non-invertible fusion
algebra over TQFT coefficients**", "act invertibly on all local operators as
axial rotations, but non-invertibly on the 't Hooft lines", and "**lead to
selection rules, which are consistent with the scattering amplitudes in QED**"
(`QED_draft.tex` L.86–91). They then show the π⁰F∧F coupling is *required* to
match the non-invertible symmetry in the UV, so that "the conventional argument
for the neutral pion decay using the ABJ anomaly is now rephrased as a matching
condition of a generalized global symmetry" (L.92–93).

*Claim:* the amplitude-level output of a non-invertible symmetry, as currently
understood, is a **selection rule** — which processes vanish — not a soft factor.
The 2+1 lattice soft theorem should therefore first be attempted in Adler-zero
form ("this soft limit vanishes / this sector-changing amplitude is forbidden"),
which is also the weakest claim and the easiest to falsify numerically. *Avoid:*
promising a soft *factor* (a nonzero universal coefficient) from categorical
data alone; nothing in this literature yet supplies one. Pairs with the already
fetched 2403.04835 (non-invertible symmetry constraining the 1+1 S-matrix).

### 10. Inamura–Ohmori, arXiv:2305.05774 — *Fusion Surface Models: 2+1d Lattice Models from Fusion 2-Categories*

Constructs explicit (2+1)-dimensional lattice systems — "fusion surface models"
— with "finite non-invertible symmetries described by general fusion
2-categories", generalizing the 1+1d anyon chains of Aasen–Fendley–Mong
(`main.tex` L.72–76, L.135). The construction covers "anomalous or non-anomalous
one-form symmetries, 2-group symmetries, or non-invertible one-form symmetries
that capture non-abelian anyon statistics" (L.74), with symmetry TFTs playing
the structural role.

*Claim:* this is the concrete arena — a 2+1 lattice Hamiltonian whose symmetry is
a fusion 2-category, the direct analogue of the anyon chains that carried the 1+1
results. Any 2+1 triangle statement should be pinned to a model in this class so
that the symmetry data is exact rather than emergent. *Avoid:* assuming the 1+1
anyon-chain arguments carry over verbatim: the symmetry operators here are
codimension-1 **surfaces** in spacetime with line and point defects on them
(objects / 1-morphisms / 2-morphisms), so the "virtual insertion V(g)" of the 1+1
story becomes an extended object with its own internal structure.

### 11. Bultinck–Mariën–Williamson–Şahinoğlu–Haegeman–Verstraete, arXiv:1511.08090 — *Anyons and matrix product operator algebras*

The PEPS-side dictionary. Topological order in these states "is a consequence of
the symmetry of the underlying tensors in terms of matrix product operators";
from those MPOs one builds a C*-algebra whose **central idempotents are the
topological sectors**, from which topological spin, S-matrix, fusion and
braiding follow (`AnyonsPEPS.tex` L.47, L.86). Because "the matrix product
operator symmetries are acting purely on the virtual level … the ensuing Wilson
loops are not fattened when perturbing the system" — the sector labels survive
away from the RG fixed point (L.47, L.61).

*Claim:* the 2+1 lattice asymptotic charge should be an **MPO string acting on
the virtual level**, and the conserved labels are the central idempotents. This
is where a lattice "large gauge transformation" naturally lives, and the
non-fattening statement is what makes the labels usable on a serious (non-fixed-
point) model — exactly the property a memory index needs. *Avoid:* treating the
MPO symmetry as acting on physical operators; it does not, which is why the
charge is invisible to local physical observables and must be detected by a
string/holonomy observable of the 1707.08016 type.

## (d) Asymptotic symmetries and edge modes of Chern–Simons and topological phases

### 12. Geiller, arXiv:1703.04748 — *Edge modes and corner ambiguities in 3d Chern–Simons theory and gravity*

Boundaries "can break gauge invariance, and thereby turn gauge degrees of
freedom into physical ones"; extending the covariant Hamiltonian formalism with
new boundary fields makes it invariant under arbitrary large gauge
transformations, and "by studying the examples of Abelian Chern–Simons theory
and first order three-dimensional gravity … the new boundary observables satisfy
the known corresponding **Kac–Moody affine algebras**" (`Boundary.tex` L.122).
The introduction records the classic statement that these are "the famous
conformal edge currents of Chern–Simons theory" (L.132), and that 3d gravity's
infinitely many boundary dof coexist with finitely many bulk ones.

*Claim:* corner A in 2+1 is the **edge symmetry**, and its algebra is expected to
be current-algebra-like (Kac–Moody) rather than abelian — a richer structure than
the 1+1 (G_L×G_R)/G_diag the campaign has. *Avoid:* over-claiming novelty on
corner A; this identification is thirty years old in the CS literature and the
paper should cite it and move on, per TJO's read.

### 13. Donnelly–Freidel, arXiv:1601.04744 — *Local subsystems in gauge theory and gravity*

The formalism behind 1703.04748: a gauge-invariant classical phase space for a
spatial slice with boundary is obtained "by introducing new degrees of freedom on
the boundary"; in Yang–Mills these are "a choice of gauge on the boundary,
transformations of which are generated by the normal component of the nonabelian
electric field", and they transform under a group of *surface symmetries*
(`symplectic.tex` L.88–96).

*Claim:* this is the continuum justification for the lattice fact that cutting a
PEPS leaves virtual-level degrees of freedom carrying the charge — the extended
Hilbert space of the entanglement-entropy literature. It licenses treating the
virtual bond space as physical charge data rather than as gauge redundancy.
*Avoid:* nothing load-bearing; this is background that keeps the lattice
construction from looking ad hoc.

---

## Synthesis — what the literature suggests the 2+1 soft theorem should be

The 3d continuum already contains one complete infrared triangle, and its shape
is not the 4d one. In arXiv:2411.13633 the triangle closes in a theory with **no
propagating graviton**: the soft mode is a boundary degree of freedom living on
null infinity, the asymptotic symmetry is BMS₃, and the "soft theorem" is the
far-field limit of the constraint equations — a Gauss-law Ward identity relating
a boundary insertion to the hard in/out data. Read together with the edge-mode
literature (1703.04748, 1601.04744) and the PEPS dictionary (1511.08090), this
points to a single recommendation: **the 2+1 lattice soft theorem should be
stated for a boundary/virtual-level insertion — an MPO string or edge-mode
operator — and not for a bulk soft quasiparticle.** Its soft limit is a limit of
the *boundary* momentum along the edge; its charge algebra is expected to be
current-algebra-like; and the arena in which the symmetry data is exact rather
than emergent is the fusion-surface class of arXiv:2305.05774.

On the categorical side the literature is thinner and sets a lower ceiling.
arXiv:2211.09570 supplies the missing input — a genuine Goldstone theorem for a
spontaneously broken continuous non-invertible symmetry — but its conserved
current is **localized on the defect**, so the Ward identity that would drive a
soft theorem is defect-supported, not a bulk current identity; the 1+1 corner-A
argument does not transplant verbatim. arXiv:2205.05086 (with 2403.04835 from
Batch 2) shows that what a non-invertible symmetry currently delivers at the
amplitude level is a **selection rule** — which processes are forbidden — rather
than a soft factor. The honest target is therefore an **Adler-zero / selection-
rule form first**: "the soft limit of this sector-changing amplitude vanishes",
which is both the weakest defensible claim and the one a PEPS computation can
falsify. A soft *factor* with a universal coefficient should stay a CONJECTURE
until derived; no antecedent supplies one from categorical data.

Three warnings, in descending order of danger.

1. **Memory means something different in 2+1.** By the direct computations of
   1712.00873 and 1702.00095, permanent-displacement memory is a d=4 accident.
   In d=3 the retarded field has a tail — the force falls only as 1/√U — and the
   verdict is an "infinite momentum memory effect", with no gravitational memory
   at all. The 2+1 lattice observable should be a **momentum/velocity kick**,
   stated as a rate or on a finite window, never as a finite permanent
   displacement. If a lattice calculation returns a finite permanent shift, that
   is evidence the lattice regulator, not the physics, produced it.

2. **A confined or dressed charge sector silently trivialises the triangle.**
   arXiv:2503.20173 shows 3d QED's logarithmic confinement forbids finite-energy
   asymptotic charged states, making the asymptotic symmetry act trivially on
   the S-matrix and abolishing the 3d EM memory effect. The lattice analogue is
   immediate and dangerous: in a gapped 2+1 topological phase there is no
   radiative sector at all, so a "soft theorem" derived there risks being 0=0. A
   pre-registered falsifier must check that the sector carrying the charge has
   finite-energy asymptotic states — i.e. that the model is gapless at the
   boundary or tuned to criticality — before any status label moves.

3. **Name the order.** 1901.05942 forces the radiative (1/r^{d/2−1}) vs Coulombic
   (1/r^{d−3}) distinction and the null-vs-ordinary memory split; only the null
   piece is tied to flux and hence to the soft sector. Its analysis is stated for
   d ≥ 4 and does **not** cover d=3, where those exponents invert (Coulombic
   1/r⁰ does not decay and dominates the 1/r^{1/2} radiative term) — a structural
   oddity that should be flagged, not quietly extrapolated.

The constructive path these warnings leave open is the holonomy route. Colour
memory (1707.08016) measures the change in a flat connection by parallel
transport of test charges, an observable that needs no propagating radiation and
no permanent displacement; on the lattice its counterpart is the change in an
MPO/Wilson-string holonomy encircling the region, whose labels are exactly
1511.08090's central idempotents and survive perturbation away from the fixed
point. That gives a memory observable (corner B) and a charge (corner A) that are
already known to be well-defined in 2+1; the open edge of the triangle remains
corner C, and the literature's best guidance for it is: **defect-supported Ward
identity, boundary soft limit, Adler-zero form, weak-flux hypothesis.**
