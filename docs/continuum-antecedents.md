<!-- ROLE: reference digest. AUTHORED by subagent per TJO task, 2026-08-25.
     Ground truth per L3: quotes/equations below are transcribed from local TeX
     under refs/arxiv-<id>/, file+line cited at each claim. Not itself a claim
     in claims/CLAIMS.md; theory shards should cite specific equations from
     here back to the refs/ source, not to this file. -->

# Continuum antecedents: what the lattice triangle must mirror

> **CORRECTION (2026-08-30, reduction lanes r1-smatrix.md + independent codex
> recomputation).** §5's translation obligation and "Surprise 2" are WRONG
> about the exponent: the ferromagnet has generalized-shift degree `n = 0`,
> so eq. (B) gives `σ ≥ min(2,1) = 1`, and 2201.01393 L.525–527 reaches
> `σ = 2` only for its `n = 1` examples. The proved lattice slope saturates
> the ORDINARY `σ = 1` type-B₂ Adler bound. Do not cite this file for a
> `σ = 2` claim; see `theory/lanes/reduction/r1-smatrix.md` and
> `docs/reduction-limits.md` §R1.

Seven sources, read from local TeX (`refs/arxiv-<id>/`, verified against
`refs/LEDGER.md`). Corner vocabulary follows `HANDOFF_MPS_SOFT_THEOREM.md`:
**Corner A** = asymptotic symmetry (𝒜 = (G_L×G_R)/G_diag, virtual insertions
V(g), Ward identity (WI)); **Corner C** = soft theorem (Conjecture S, soft
factor S(k), remainder R(k), Adler zero); **Corner B** = memory (Conjecture
M, collective-coordinate shift δx, zero-frequency weight).

---

## 1. Hamada–Sugishita, arXiv:1709.05018 — soft-pion triangle

File `refs/arxiv-1709.05018/draft1004.tex`. Model: complex scalar Φ + Dirac
Ψ, spontaneously broken global axial U(1)_A (L.166–207), NG boson "pion" π,
derivative couplings only — no gauge field, closest precedent to a
matter-only lattice Goldstone triangle.

**Soft pion theorem** (subleading; leading O(ω⁻¹) is *absent* since pion
vertices vanish as momenta→0, L.261–322):
```
lim_{ω→0} ⟨out| a_π(ωq) S |in⟩ = J⁽¹⁾(q) ⟨out|S|in⟩,          (softNGthrm, L.330)
J⁽¹⁾(q) = Σ_k [ -iy η_k / (2m p_k·q) ] ε_{μνρσ} q^μ p_k^ν J_k^{ρσ}
```
i.e. the soft factor is a **spin-rotation operator** (∝σ·q̂), not a pole —
the O(1) analogue of Weinberg's 1/ω pole. A trivial "leading" theorem also
holds, ω·(amplitude)→0 (L.416–421), giving a second charge Q⁰.

**Ward–Takahashi form** (L.356–414): soft charge `Q^soft(q̂) := -(i/4π)
lim_{ω→0}(a_π†-a_π)` (L.361) plus hard charge from the fermion bilinear,
`Q^hard(q̂)=(y/8πm²)∫d³p/(2E_p) ū γ⁵[q^μp^νγ_{μν}/(p·q)]u a†a+…` (L.385),
satisfy exactly `⟨out|[Q^soft+Q^hard, S]|in⟩=0` (L.377). This WT identity is
*independently re-derivable* from the ordinary (non-asymptotic) broken
U(1)_A current WT identity (L.438–464, `eq: WT U(1)A` L.451–453) via LSZ +
soft limit — the "exotic" asymptotic-symmetry derivation and the textbook
broken-symmetry derivation are shown to coincide (L.462–464). **This is the
cleanest continuum precedent for A⇒C via an ordinary, non-null-infinity
broken WT identity.**

**Pion memory** (L.639–814): the *subleading* (1/r²) coefficient π⁽²⁾ of
the pion field shifts by the integrated hard flux, `π⁽²⁾(u=∞,θ) =
¼Δ_S²Q^hard(q̂)` (L.811), proved two ways — charge conservation (L.696–699)
and classically solving ∂²π+∂_μj^μ=0 via a Green's function on ℍ³
(L.707–813). Memory lives in the *sub*leading falloff coefficient, not the
leading 1/r term (which carries EM/gravitational memory), because the soft
theorem itself starts one order higher (L.700–702).

**Falloff assumptions**: stationary-phase mode expansion at large r for the
1/r, 1/r² Bondi-type expansion (L.515–526); no O(r⁰) term (vacuum π=0,
L.506); hyperbolic foliation near timelike infinity with fields falling as
τ^{-3/2} (fermion) / τ^{-3} (current) (L.559–576, L.649–654), used to make
the hard charge a finite integral over ℍ³.

> **Lattice translation obligation.** A⇒C must reduce to exactly this
> pattern — an ordinary (non-boundary) Ward identity of the truncated
> symmetry, LSZ'd onto excitation-ansatz legs — and Corner-B's memory
> observable must be identified with the analogue of this *subleading*
> falloff coefficient (one order beyond the naive displacement), since our
> soft-magnon factor also has no 1/k pole.

---

## 2. De Luca–Khoury–Wong, arXiv:2412.01910 — local memory↔soft derivation

File `refs/arxiv-2412.01910/draft_short.tex`. Explicitly avoids null
infinity: derives BMS-equivalent memory diffeomorphisms **locally**, in
transverse-traceless (TT) gauge around a GW detector — the setting closest
to a lattice bulk-observer construction.

**Derivation skeleton** (the template to mirror for a non-boundary proof):
1. Taylor-expand the local strain in retarded time u: `H_ij^TT =
   (1/R̄)[A_ij+B_ij u+…]` (L.192) — A_ij = displacement memory, B_ij =
   velocity-kick memory.
2. Exhibit the residual TT-preserving diffs removing each term: a
   volume-preserving anisotropic spatial rescaling `ξ_i =
   -(1/2R̄)(A_ij+B_ij u)x^j-…` (L.202) plus a compensating time-diff (L.210).
3. Prove this local residual diff is **exactly equivalent** to a BMS diff
   pulled into the detector frame plus compensating gauge transformations
   (L.216–279, identification L.267–270) — proved by explicit change of
   frame, not merely both derived from the same amplitude.
4. Build `Q^μ=ξ_αT^{αμ}`, derive the Ward identity `i∂_μ⟨Q^μΦ…⟩ -
   i⟨∂_μQ^μΦ…⟩ = Σ_mδ⁴(x-x_j)⟨…δΦ(x_m)…⟩` (L.302–306), Fourier-transform,
   LSZ-reduce to the amplitude soft theorem (L.307–322) whose leading pole
   `1/(k_m·q)` **exactly reproduces Weinberg's soft factor** (L.321).
5. The *same* local-diff logic is pushed through to equal-time (in-in)
   correlators, not just S-matrix elements (L.329–413) — a genuinely
   different observable class, often more natural for a lattice proof.

**Assumptions flagged as non-automatic**: the "physical mode condition"
(soft mode's time-dependence must match the long mode being removed,
L.358–360) and a transversality/"adiabatic" condition (L.360–361) — both
function-space restrictions imposed by hand.

> **Lattice translation obligation.** A⇒C should be built on exactly this
> skeleton — local truncated-symmetry current → Ward identity →
> excitation-ansatz limit → factorization — with no boundary invoked, and
> should additionally state the lattice equal-time-correlator form of
> Conjecture S, plus our own explicit "physical mode condition" on which
> symmetry-parameter profiles are admissible.

---

## 3. Strominger–Zhiboedov, arXiv:1411.5745 — displacement memory ⇔ soft graviton

File `refs/arxiv-1411.5745/memory_4.tex`. The canonical B⇔C proof, done
*without* asymptotic symmetry as an intermediate step (stated goal,
L.665–668).

**Displacement memory**, two routes: BMS route — vacuum transition
C_zz(u_i)→C_zz(u_f) (L.553) gives detector separation shift `ΔL =
(r₀/2L)ΔC_zz δz²+c.c.` (L.605–607) with ΔC_zz an integral of radiated flux
T_uu over a sphere Green's function (L.609–611); Braginsky–Thorne route —
explicit jump in asymptotic TT metric from an n→m event, `Δh^TT_μν(k) =
(1/r₀)√(G/2π)(Σ_out p'p'/(k·p') - Σ_in pp/(k·p))^TT` (L.681–683).

**Equivalence chain to the soft graviton formula** (L.680–701, key move):
1. Fourier-transform via stationary phase: `h^TT_μν(ω,k) = 4πi lim_{r→∞} r
   ∫du e^{iωu} h^TT_μν(u,rk)` (L.688–691).
2. Assume h^TT approaches *finite but different* values as u→±∞ (the
   falloff assumption doing all the work) ⇒ the DC jump is literally the
   ω-pole residue: `Δh^TT(k) = (1/4πir₀) lim_{ω→0}(-iωh^TT(ω,k))` (L.692–695).
3. Identify `ωh^TT_μνε^μν` with the amplitude ratio, i.e. Weinberg's soft
   factor: `lim ωh^TT ε = √(8πG)ε·S(k)` (L.699).
4. Substituting (3) into (2) reproduces the Braginsky–Thorne formula exactly
   (L.700).

Chain: **DC memory = Fourier ω→0 residue = soft-theorem coefficient**, by
Fourier calculus alone — no charges or Ward identities needed for *this*
edge. (Memory=BMS-vacuum-transition, the A-side link, is argued separately
via the explicit `f=-ΔC` supertranslation, L.626–628 — kept logically
distinct.)

> **Lattice translation obligation.** C⇒B should be provable by the same
> Fourier-residue argument, provided we can prove (not assume) the lattice
> analogue of "order parameter/collective coordinate approaches finite but
> different values at early/late times" for excitation-ansatz wavepackets;
> this edge is logically independent of Corner A and should be its own
> lemma, not folded into the A⇒C Ward-identity proof.

---

## 4. Agrawal–Nguyen, arXiv:2504.10577 — soft theorems ⇒ SSB (general statement)

File `refs/arxiv-2504.10577/Letter.tex`. Claim: soft theorems for a symmetry
**necessarily imply** SSB of that symmetry, proved field-theoretically (no
semiclassical hand-waving) using carrollian/celestial correlators.

**Mechanism** (L.136–221): compare the soft theorem to the abstract Ward
identity `⟨0|[Q_λ,O_1…O_n]|0⟩ = -iΣ_a e_aλ(x_a)⟨0|O_1…O_n|0⟩` (L.118–125).
If the RHS is generically nonzero — as the soft theorem's angular kernel
forces — then Q_λ|0⟩≠0, i.e. SSB. Not an assumption but a derivation: the
soft photon/graviton theorem, rewritten in carrollian variables, literally
*is* the RHS for `λ(x;y,ε)=(y-x)/|y-x|²` (photon, L.174–177) or
`T(x;y,ε)=2(y-x)²/|y-x|²` (graviton, L.207–210).

**Where the Adler zero sits** (L.346–361): explicitly the *unbroken*
foil — "spontaneous symmetry breaking usually comes with interesting
constraints… of which Adler's zero is a perfect example." Nonzero soft pole
⇒ SSB via the Ward-identity match above; vanishing leading term (Adler
zero) is the standard unbroken-NG-boson statement, treated only as
comparison. The shifted vacuum is identified with the soft state itself,
`Q_λ|0⟩ ≡ i lim_{ω→0}ωa†(ωq)|0⟩` (L.180, L.214), and the Goldstone modes
are shown (zero-momentum Poincaré rep argument, L.223–332) to be conformal
fields on the celestial sphere with **logarithmic** two-point functions
(L.325) — tied to discrete-series representation theory of the
massless-particle little group, with no obvious lattice analogue.

> **Lattice translation obligation.** Corner A's unbroken-vs-broken 𝒜
> bookkeeping should be shown equivalent to "Conjecture S has S(k)→0
> (Adler zero) vs. S(k)→const≠0 at reference k" — state explicitly which
> regime our type-B lattice Goldstone falls into (§5 below), and do NOT
> expect a logarithmic Goldstone-CFT structure — that is a continuum,
> Poincaré-representation-theoretic artifact with no analogue for a compact
> lattice Brillouin zone.

---

## 5. Mojahed–Brauner, arXiv:2108.03189 + arXiv:2201.01393 — type-B Goldstone soft scaling

Files `refs/arxiv-2108.03189/main.tex`, `refs/arxiv-2201.01393/manuscript.tex`.
Model M1 (Heisenberg ferromagnet, ω∝k² magnon) is a **type-B₂** Goldstone
theory — this is the precise continuum classification and soft-scaling
machinery for that class.

**Soft-scaling definition** (2108.03189 L.81–86): rescale one leg's momentum
p_i→εp_i, define σ_i via A_n∝ε^{σ_i}. Ordinary Adler zero: σ_i≥1;
"exceptional" EFTs exceed naive derivative counting.

**Type A vs. type B** (2201.01393 L.125–129): type A_m = real scalar,
ω∝|p|^m; type B_{2m} = complex scalar/conjugate pair, ω∝|p|^{2m}. **B_{2m}
is unconstrained by the CHMW theorem for any d,m**; A_m needs d>m. The
ferromagnet magnon is manifestly type B₂.

**Soft-scaling bound** (2201.01393 §4, core result):
```
σ ≥ min(m,  n+1)     for type A_m  (with d ≥ m+1)                  (eq. A, L.487)
σ ≥ min(2m, n+1)     for type B_{2m}                                (eq. B, L.490)
```
n = degree of the theory's generalized spatial shift symmetry (L.446–472).
**Type-B enhancement needs NO additional shift symmetry** — the dispersion
alone (ω∝p^{2m}) buys the extra k-powers, unlike type-A where enhanced σ
needs redundant symmetry. Worked example: Schrödinger-DBI achieves σ=2
(L.523–529) from the m=1 dispersion alone, no hidden symmetry required.

**Adler-zero derivation skeleton** (2201.01393 §4.1, L.405–439): on-shell
factorization `⟨β|J^μ(0)|α⟩ = i/(p⁰-ω(|p|))⟨Ω|J^μ|θ(p)⟩⟨β+θ(p)|α⟩+R^μ(p)`
(L.421); current conservation cancels the NG pole exactly (L.415, using
`⟨Ω|J^μ|θ(p)⟩=e^{-ip·x}[ip^μF₁+iδ^{μ0}F₂]`, L.410), leaving `⟨β+θ(p)|α⟩ =
(p⁰R₀+p^rR_r)/(ωF₁+F₂)|_{p⁰=ω}` (L.431) — the Adler zero then requires the
*additional, non-automatic* assumption that R^μ(p) is regular as p→0
on-shell (L.433–439, explicitly flagged "does not automatically follow from
standard polology rules"). This is the exact nonrelativistic analogue of
the 1709.05018 fermion-pole mechanism and the template for the lattice A⇒C
proof at k→0.

**No lattice analogue**: the bound (eq. A/B) is for asymptotic free
particle states in infinite continuum space — no counterpart to the
lattice's finite Brillouin zone / discrete SPT class H²(G,U(1)); the CHMW
dimensional bound is a T=0 long-range-order existence statement, irrelevant
where we start from an exact known ground state.

> **Lattice translation obligation.** Conjecture S's "S(k)→0 linearly"
> claim must be shown to be the σ=2 bound of eq. (B) with m=1, reusing the
> pole-cancellation mechanism verbatim ((WI)-telescoping is the lattice
> R^μ(p)-regularity claim made *provable* rather than merely non-automatic)
> — and we need no CHMW-type existence argument, a genuine simplification
> over the continuum EFT setting.

---

## 6. Fracton infrared triangle, arXiv:2310.16683

File `refs/arxiv-2310.16683/frac-short.tex`. First non-Lorentzian
realization of the full triangle — closest precedent for a triangle built
on a theory without boost invariance.

**Three corners, named exactly** (Fig. 1, L.176–186): "Soft theorem",
"Asymptotic symmetries", "Memory effect" around "Fracton IR triangle",
bidirectional arrows between all three — same shape as Strominger's, built
from a dipole-conserving U(1) gauge theory with tensor field A_ij
(L.248–256), asymptotic gauge symmetries `Λ=rλ(θ,φ)+uc·η(θ,φ)+ε(θ,φ)+O(1/r)`
(L.535) at TWO radiative sectors.

**"Double kick" memory — precise definition** (L.189–199, L.404–462): two
propagation speeds c (transverse T) and c̃=c/√2 (transverse-longitudinal
TL) ⇒ **two distinct null infinities**, u=t-r/c and ũ=t-r/c̃ (L.467–472). A
distant test dipole receives **two separate memory kicks** at two retarded
times, dipole orientation staying inert (L.456–461). Memory per sector =
DC jump of the sector's radiative field:
```
δĀ^T_ij(n)  = (1/4πc²)  Σ_α η^α d^{α⊥}_(i v^{α⊥}_j)               / (1-n·v^α/c)   (L.415)
δĀ^TL_i(n)  = (1/4πc̃²) Σ_α η^α (d^{α⊥}_i v^α_r + v^{α⊥}_i d^α_r) / (1-n·v^α/c̃)  (L.417)
```
producing a net velocity kick via the generalized Lorentz force over both
retarded-time windows (L.441–443), including a term ∝δu that is the *same
order* in 1/r as the wave term, unlike ordinary EM (L.449–452).

**Dipole soft theorem** (L.748–797): derived FROM the memory, not
independently, following Strominger–Zhiboedov: soft factors S^#_ij =
-4πc_#²δĀ^#_ij are *by construction* equal to the memory (L.760–761,
L.787) — here B⇒C holds by definition, not an independent Fourier-residue
argument (contrast §3).

> **Lattice translation obligation.** If a future lattice model ever has
> more than one Goldstone velocity scale (not the case for M1/M2 as
> currently scoped), Corner-B/C machinery must go sector-by-sector exactly
> as here rather than assume a single universal S(k); for the present scope
> flag this as a known generalization path, not a gap.

---

## 7. Strominger, arXiv:1703.05448 §1.1 "The Infrared Triangle" — canonical logic

File `refs/arxiv-1703.05448/soft_Arxiv_update.tex`, L.308–341 (this material
is in §1 "Introduction"/§1.1; the lecture notes have no separate numbered
"§2 triangle" section — §2 in the compiled paper is "QED", L.433 — recorded
here for the ledger since the task named "§2"). The *canonical statement*
of the triangle's logic, reused by every paper above.

**Three corners** (L.311–334): soft theorems = "universal properties of…
scattering amplitudes when a massless external particle becomes soft";
asymptotic symmetries = "the nontrivial exact symmetries or conserved
charges of any system with an asymptotic region or boundary" (exact, not
merely approximate); memory effect = "a subtle DC effect, in which the
passage of [radiation] produces a permanent shift in the relative positions
of a pair of inertial detectors."

**Soft⇔Memory, the master move** (L.333, quoted since it is the template
for every C⇔B proof above): *"The former is a statement about momentum
space poles in scattering amplitudes, while the latter concerns a DC shift
in asymptotic data between late and early times. These are the same thing,
because the Fourier transform of a pole in frequency space is a step
function in time."*

**Symmetry⇔Soft**: "every symmetry has a Ward identity that equates
scattering amplitudes of symmetry-related states… These Ward identities
turn out to be nothing but the soft theorems… in disguise" (L.334) — A⇒C
asserted as a general principle here, proved in detail later in the same
notes and in the papers above; §1.1 is a pointer, not a derivation.

> **Lattice translation obligation.** TRIANGLE.md's top-level narrative
> should state the triangle in exactly this register — three independently
> meaningful statements joined by two provable edges — with C⇔B presented
> expositorily as "Fourier transform of a pole is a step function" applied
> to S(k) and δx, even though the rigorous lattice proof (via
> excitation-ansatz wavepackets, per Conjecture M) needs far more care than
> this one-line slogan.

---

## Report

### Key equations extracted (schematic)

| Source | Corner | Equation (schematic) |
|---|---|---|
| 1709.05018 | C | `lim_{ω→0}⟨a_π S⟩=J⁽¹⁾(q)⟨S⟩`, J⁽¹⁾~spin-rotation, O(1) not O(1/ω) |
| 1709.05018 | A | `[Q^soft+Q^hard,S]=0`, Q^hard from fermion bilinear ⊗ q^μp^νγ_{μν}/(p·q) |
| 1709.05018 | B | `π⁽²⁾(u=∞)=¼Δ_S²Q^hard(q̂)` — memory in the *sub*leading falloff coefficient |
| 2412.01910 | A→C | local TT residual diff → Ward id `∂_μ⟨Q^μΦ…⟩=Σδ⁴⟨δΦ…⟩` → LSZ → Weinberg pole |
| 1411.5745 | B⇔C | `Δh^TT=(1/4πir₀)lim ω→0(-iωh^TT(ω))`, ωh^TT = soft factor by S-matrix def |
| 2504.10577 | A⇐C | soft pole ⇔ nonzero RHS of Ward id ⇔ Q_λ|0⟩≠0 (SSB); Adler zero = unbroken foil |
| 2108.03189/2201.01393 | C | σ≥min(2m,n+1) type-B (no extra symmetry); Adler zero via `⟨β+θ⟩=(pR)/(ωF₁+F₂)` |
| 2310.16683 | full △ | two speeds ⇒ two null infinities ⇒ "double kick" memory; sector-wise B⇒C |
| 1703.05448 §1.1 | logic | pole in ω ↔ step function in u (Fourier); Ward id = soft theorem "in disguise" |

### Surprises (continuum assumptions with no obvious lattice analogue)

1. **Subleading, not leading, memory** (1709.05018): the pion soft theorem
   starts at O(1) not O(1/ω), so memory lives in the *subleading* falloff
   coefficient, not the leading term that carries EM/gravitational memory —
   directly analogous to our situation (magnon S(k) also has no 1/k pole),
   so should be read as confirmation, not surprise. But it means intuition
   from EM/gravity memory about "the" memory observable being the leading
   term is wrong for a derivative-coupled Goldstone, ours included.
2. **Type-B enhancement needs no extra symmetry** (2201.01393): the σ≥2
   bound for the ferromagnet's class comes purely from ω∝k² via the same
   pole-cancellation mechanism as ordinary type-A, no redundant shift
   symmetry required (unlike Galileon/DBI). Good news: A⇒C need not hunt a
   hidden higher symmetry of the Heisenberg ferromagnet, only correctly use
   the k² dispersion in the pole cancellation.
3. **Discrete-series Goldstone CFT is a purely continuum artifact**
   (2504.10577): logarithmic two-point functions of celestial Goldstone
   modes follow from massless-particle little-group representation theory
   and a continuous celestial sphere. A 1D lattice has neither — this piece
   of machinery has **no lattice counterpart and should not be sought**;
   flag in TRIANGLE.md as a deliberate non-mirroring, not a gap.
4. **Multi-sector triangles are the generic case, not the exception**
   (2310.16683): the fracton triangle needed one soft/memory pair *per*
   propagation speed. M1/M2 has a single dispersion so this does not bite
   now, but it warns that "the" S(k) and "the" δx in Conjecture S/M are
   implicitly single-sector assumptions — worth an explicit remark in
   TRIANGLE.md rather than leaving it silent.
5. **Remainder regularity is asserted, never proved, in the continuum**
   (2201.01393, 1709.05018): every continuum Adler-zero proof read here
   needs a technical assumption ("R^μ(p) regular as p→0", "no surface
   term", "no additional singularities besides the NG pole") flagged as
   non-automatic and simply assumed. Our (WI)-telescoping mechanism is
   explicitly meant to *prove* the lattice analogue of this regularity
   rather than assume it — arguably the paper's chief technical
   contribution relative to every continuum antecedent read here, worth
   stating prominently in the Letter's introduction.
