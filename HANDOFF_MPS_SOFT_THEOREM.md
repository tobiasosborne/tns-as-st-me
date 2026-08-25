# HANDOFF — A soft theorem, asymptotic symmetries, and memory effects for 1D lattice systems in MPS language

Prepared 2026-08-21 for a fresh agent with NO access to prior work. This document is self-contained:
every definition, claim, target theorem, and reference you need is stated here. Owner: Tobias Osborne
(theoretical physicist; expert in tensor networks and the MPS excitation ansatz; demands mathematical
rigour; do not flatter him). Subagents: Sonnet for search/coding, Opus for theory; no Fable subagents.

---

## 0. The goal in one paragraph

In quantum field theory there is an "infrared triangle" (Strominger et al.): three superficially
different facts — (i) soft theorems (universal factorization of scattering amplitudes when one
massless quantum's frequency → 0), (ii) asymptotic symmetries (symmetry transformations acting
nontrivially at infinity, modulo those that die off), and (iii) memory effects (permanent, zero-
frequency shifts left behind by radiation) — are three faces of one Ward identity. The goal here is
to FORMULATE AND PROVE the exact 1D lattice version of this triangle in matrix-product-state (MPS)
language, where every corner becomes a finite, checkable statement about tensors, and to verify it
numerically against exactly solvable models. The correct continuum antecedent is the GLOBAL-symmetry
(soft pion / Goldstone) triangle, NOT the photon/graviton one: there is no gauge mediator on a 1D
lattice, so the target soft theorem is an Adler-zero-type low-energy theorem, not a Weinberg 1/ω
pole. If proved, this is a self-contained paper: a new, elementary, and completely rigorous
incarnation of the infrared triangle, plus one genuinely novel prediction (an SPT/anomaly-modified
soft theorem, §5.4) with no continuum antecedent.

## 1. Background you must reconstruct or know (with the key equations)

### 1.1 MPS structure and the intertwining relation
Uniform MPS |ψ(A)⟩ with tensor A^s_{ij} (physical index s, virtual indices i,j of dimension χ),
injective (transfer matrix E = Σ_s A^s ⊗ Ā^s has a unique eigenvalue of largest modulus). For an
on-site symmetry group G with unitaries u(g) satisfying U(g)|ψ⟩ = |ψ⟩, the fundamental theorem of
MPS gives the LOCAL INTERTWINING RELATION:
    Σ_{s'} u(g)_{ss'} A^{s'} = e^{iθ(g)} V(g)^{-1} A^s V(g),                     (IT)
with V(g) a projective representation on the virtual space, class [ω] ∈ H²(G, U(1)) — the 1D SPT
index. (References: Pérez-García–Wolf–Sanz–Verstraete–Cirac on string order and symmetries in MPS,
arXiv:0802.0447; Cirac–Pérez-García–Schuch–Verstraete review, arXiv:2011.12127.)

### 1.2 The truncated-symmetry ("MPO Ward") identity
Apply the symmetry only on an interval R = [a,b]: U_R(g) = Π_{x∈R} u(g). Using (IT) at every site of
R, the virtual V's telescope and cancel in the bulk, leaving exactly two virtual insertions at the
edges of R:
    U_R(g) |ψ(A)⟩ = e^{i|R|θ} |ψ(A; V(g) inserted on bond a−1|a, V(g)^{-1} on bond b|b+1)⟩.  (WI)
This exact identity is the lattice Ward identity: a symmetry applied to a region acts only at the
region's boundary, as virtual-space operators. All selection rules and current-conservation
statements follow from (WI) plus transfer-matrix calculus. For g = e^{iεQ} infinitesimal, (WI) is
lattice Noether: ⟨[Q_R, O]⟩ = boundary terms.

### 1.3 Excitation ansatz, topological (kink) sectors, and S-matrices
One-particle states: |Φ_k(B)⟩ = Σ_x e^{ikx} |ψ(A...A B A...A)⟩ with B at site x (Haegeman et al.,
arXiv:1103.2286; tangent-space review arXiv:1810.07006). Gauge freedom: B ≃ B + e^{ik}A X − X A
(null directions). Kink sectors: when G is spontaneously broken with degenerate injective vacua
{A_α}, the ansatz with A_α tensors to the left and A_β to the right of B describes topological
(domain-wall) excitations, with mixed transfer matrices. Two-particle S-matrices are computable
within this framework: Vanderstraeten–Haegeman–Osborne–Verstraete, "S-matrix from matrix product
states" (arXiv:1312.6793, PRL 112, 257202) and "Scattering particles in quantum spin chains"
(arXiv:1506.01008, PRB 92, 125136); real-time wavepacket scattering: arXiv:1907.02474; kink/false-
vacuum collisions with MPS: Milsted–Liu–Preskill–Osborne–Vidal, arXiv:2012.07243 (PRX Quantum 3,
020316). DOWNLOAD AND READ THE TEX SOURCES of at least 1312.6793, 1506.01008, 1103.2286, 2012.07243
(arXiv e-print endpoint: https://arxiv.org/e-print/<id>, wait 3 s between requests; verify every id
by reading the actual title — do not trust this list blindly, and record any id that fails to match).

### 1.4 The continuum triangle (for orientation only)
Strominger's lectures (arXiv:1703.05448) for the photon/graviton triangle; the global-symmetry
version closest to this project: Campiglia–Coito–Mizera / Hamada et al. on soft pion theorems as
asymptotic-symmetry Ward identities and the associated "pion memory" (search: "soft pion theorem
asymptotic symmetry memory", e.g. arXiv:1703.07885). Soft theorems for spontaneously broken
symmetries and Adler zeros: arXiv:2504.10577 and references therein. Also relevant physics folklore:
Dyson's 1956 result that ferromagnetic magnon interactions vanish as k → 0 (a lattice Adler zero
avant la lettre), and the Bethe-ansatz fact that the Heisenberg-ferromagnet two-magnon S-matrix
S(λ₁−λ₂) = (λ−i)/(λ+i) → 1 as one rapidity → ∞ (soft magnon decouples).

## 2. The 1D lattice triangle to be established

Setting: local Hamiltonian H on a spin chain, symmetry group G on-site; MPS vacua; excitation-ansatz
particles; when G (or a subgroup) is broken, kinks. Two model classes instantiate the triangle
(neither alone exhibits everything; this tension is structural, see §6.1):
  (M1) isotropic spin-1/2 Heisenberg FERROMAGNET (type-B Goldstone: SSB allowed in a 1D ground
       state; exact product-state vacuum; gapless magnons ω ~ k²; exact Bethe S-matrices as
       independent oracle; no kinks);
  (M2) easy-axis XXZ ferromagnet, Δ = J_z/J_⊥ > 1 (two product vacua |↑…↑⟩, |↓…↓⟩; kinks; magnons
       gapped — soft statements become low-frequency expansions about the gap).

### Corner A — asymptotic symmetry (rigorous now; formalize it)
Define the lattice asymptotic symmetry group
    𝒜 := (G_L × G_R) / G_diag,
transformations acting independently at the two spatial infinities modulo the global (diagonal)
symmetry. Implementation in MPS: NOT by physical operators but by virtual insertions V(g) on the
boundary bonds at ±∞ — precisely the endpoint operators of half-infinite truncated symmetry strings
via (WI). Facts to state and prove cleanly: (a) unbroken case — 𝒜 relabels charge superselection
sectors; its projective class [ω] ∈ H²(G,U(1)) is the SPT index (the lattice "anomaly of the
asymptotic symmetry"); (b) broken case — the 𝒜-orbit is the set of vacuum pairs (α_L, α_R), and
nontrivial pairs are exactly the kink superselection sectors: acting with the half-infinite
truncated symmetry U_{[x,∞)}(g) on a vacuum creates a kink at x. A kink is the contact term of a
broken truncated symmetry. This corner is bookkeeping on known structure; write it as Definitions
and Propositions with complete proofs.

### Corner C — the soft theorem (the conjecture; the core of the project)
**Conjecture S (lattice soft theorem).** Let |Φ⟩ be an n-particle excitation-ansatz scattering state
with legs carrying 𝒜-data {q_i (charges), v_i (group velocities); for kink legs, topological charge
(α,β) and collective-coordinate data}. Let the (n+1)-th leg be a Goldstone mode of momentum k (model
M1: a magnon on the ferromagnetic vacuum). Then as k → 0:
    M_{n+1}(k; p_1…p_n) = S(k; {q_i, v_i}) · M_n(p_1…p_n) + R(k),
where the soft factor S is UNIVERSAL — a function only of the legs' 𝒜-data, independent of the
microscopic tensors B_i — with S → 0 as k → 0 (Adler zero; leading term linear in k with universal
coefficient), and R(k) = o(S(k)).
**Mechanism to be turned into a proof:** at k = 0 the Goldstone tensor is the symmetry rotation of
the vacuum tensor, B_G = (d/dε)[u(e^{iεQ})·A]|_0, and (IT) shows this B_G is PURE GAUGE (a null
direction of the ansatz, B = AX − XA form with X = V′(0)) — the k = 0 magnon is the global rotation.
At small k, gauge invariance fails at O(k), and (WI)-telescoping localizes the failure onto the
other legs (the only places where the vacuum data changes), with coefficient = their 𝒜-charges.
Kink legs: the soft magnon couples only to the kink's zero mode (collective coordinate) — the
1D avatar of "soft radiation couples to solitons only through their moduli."

### Corner B — memory effect (define the observable; prove given C)
Memory observables: (i) dynamical — the permanent displacement δx of a kink's collective coordinate
after a magnon wavepacket transmits through it (in magnonics this is "magnon-driven domain-wall
motion"; it has never been framed as a memory effect — that framing is part of the contribution);
(ii) spectral — the ω → 0 Fourier weight of the local order-parameter time series during a
scattering event; (iii) spatial — a kink is itself a vacuum transition, memory written in space.
**Conjecture M (lattice memory formula):** δx (equivalently the DC weight) equals the zero-frequency
limit of the soft factor S summed over the event — the lattice Braginsky–Thorne relation. Given
Conjecture S this should follow by Fourier analysis; the work is defining δx sharply on the lattice
(the kink position operator within the mixed-sector ansatz) and controlling wavepacket corrections.

### The three edges (what implies what)
  A ⇒ C : Ward identity (WI) + excitation-ansatz gauge structure ⇒ soft factorization. THE core
          proof obligation. All technology exists; the new work is controlling the remainder R(k).
  C ⇒ B : DC limit / stationary phase. Provable once C and the corner-B definitions are fixed.
  B ⇒ A : memory is valued in the 𝒜-orbit of vacua; measuring it identifies the asymptotic
          transformation. Superselection bookkeeping; rigorous now.

## 3. Verification oracles (use them; they are the referees that cannot be argued with)

1. **Bethe ansatz (M1):** the exact two-magnon S-matrix of the Heisenberg ferromagnet. Zeroth check:
   soft decoupling S → 1. Real check: the universal subleading (Adler-zero coefficient) predicted by
   Conjecture S must match the expansion of the exact S-matrix. If it does not, the conjecture as
   stated is wrong — diagnose whether the failure is in universality (tensor-dependence sneaks in)
   or in the claimed form of S.
2. **Dyson's k → 0 magnon decoupling** (ferromagnet, 1956) as an independent statement of the
   Adler zero.
3. **Numerics:** build a small, self-contained MPS code (Julia recommended; plain arrays and
   LinearAlgebra suffice — do NOT depend on any external private code; ITensors.jl or a from-scratch
   implementation of uniform MPS + excitation ansatz are both acceptable, from-scratch preferred for
   auditability). Red/green TDD; every lemma numerically checked gets a test. Compute: (a) excitation-
   ansatz magnon–magnon amplitudes in M1 at decreasing k, extract S(k) and compare with Bethe; (b) in
   M2, real-time wavepacket simulation of magnon-through-kink transmission (the arXiv:2012.07243
   methodology), measure δx vs magnon momentum content, test Conjecture M; (c) the SPT test of §5.4.

## 4. Deliverables, in order

  D1 **Novelty sweep** (before proving anything): search for prior art on "soft theorem" +
     lattice/MPS/spin chain, "asymptotic symmetry" + lattice, "memory effect" + spin chain/domain
     wall/magnon, "Adler zero" + magnon/lattice, in 2015–2026. As of 2026-08-21 a careful search
     found NO formulation of a TN/MPS soft theorem or an MPS infrared triangle; verify this is still
     true and record the closest prior art (expected: the S-matrix-from-MPS line; soft-pion-triangle
     continuum papers; magnon-driven domain-wall-motion literature).
  D2 **TRIANGLE.md** — the framework document: Corner A as definitions+propositions with proofs;
     Conjectures S and M stated precisely (all quantifiers explicit: which states, which momenta,
     which norms for R(k)); the three edges with proof status. Every claim labelled
     PROVED / SKETCH / CONJECTURE. LaTeX-math Markdown.
  D3 **Proof of edge A ⇒ C** at whatever strength survives adversarial review — full theorem for
     M1 magnons at n = 2 (2 → 2 + soft) is the minimal publishable core; kink legs and general n
     are extensions.
  D4 **Numerical report**: the three checks of §3.3 with pass/fail criteria fixed in advance.
  D5 **Verdict**: theorem proved (state it), or precise diagnosis of where it fails and what weaker
     true statement survives.

## 5. Pitfalls, honest caveats, and one genuinely new prediction

### 5.1 Structural tensions (respect them; do not paper over)
- Mermin–Wagner/Coleman: no type-A continuous SSB in 1D ground states. The triangle lives on type-B
  (ferromagnet, ω ~ k² — note the soft expansion is in k with quadratic dispersion; state whether S
  is expanded in k or in ω and be consistent) or on discretely broken symmetry (kinks, gapped
  magnons — soft statements are expansions about the gap, and say so explicitly).
- No boosts on the lattice: the universal factor cannot take a Lorentz-covariant form; finding its
  correct lattice form (dependence on group velocities v_i) is part of the problem, not an obstacle.
- Weinberg's 1/ω pole requires a gauge mediator; it has NO clean 1D lattice home (the Schwinger
  model confines and masses the photon). Anyone who claims a 1/ω pole in this setting is wrong.
- Gapless points are where MPS is weakest. The ferromagnet dodges this (exact product vacuum,
  magnons exact one-particle states); do not drift into critical chains.
- The k = 0 magnon in the ferromagnet is a global rotation of a degenerate vacuum manifold (S²) —
  normalizability and the distinction between |k = 0⟩ and the vacuum rotation must be handled with
  the same care as soft-photon zero modes in QED; this is where sloppy arguments will die under
  review.

### 5.2 The excitation ansatz is variational
Its S-matrix is exact only asymptotically / for exact quasiparticles (M1 magnons are exact; M2 kinks
at generic Δ are not exactly product-sector states). Distinguish sharply between statements exact at
the level of the ansatz manifold and statements about the true model.

### 5.3 Terminology discipline
"MPO Ward identity", "lattice asymptotic symmetry group 𝒜", "lattice Braginsky–Thorne relation" are
COINAGES of this handoff — established literature names are: fundamental theorem of MPS /
intertwiners; pulling-through; symmetry twists/defects. The paper must say which is which.

### 5.4 The novel prediction worth the whole exercise (test it, it is falsifiable)
In an SPT phase the asymptotic symmetry 𝒜 is realized projectively (class [ω] ∈ H²). Conjecture:
soft amplitudes carry this class — e.g. for the spin-1 Haldane chain (AKLT point as the tractable
representative; magnons = the triplet mode, gapped, so "soft" = low-frequency about the gap), the
soft expansion of magnon scattering off an edge or a symmetry twist is modified by the projective
(edge-spin-1/2) structure relative to a trivial phase with identical symmetry. Formulate this
precisely and test numerically. No continuum antecedent is known; if it survives, it is the
headline. If it is vacuous (the class drops out of all amplitudes), prove THAT — a clean negative
is also a result.

## 6. Method

Adversarial pipeline: Opus prover drafts TRIANGLE.md → 3 independent Opus critics (lenses: (1)
rigour of the A ⇒ C telescoping proof and the R(k) remainder; (2) oracle consistency — recompute the
Bethe expansion and Dyson limit independently and attack the claimed universal coefficient; (3)
definitions/quantifiers — normalizability of soft modes, ansatz-vs-model gap, corner-B observable
well-definedness) → Opus adjudicator who independently recomputes disputed points → prover revises;
iterate until no fatal/major objections survive; final independent verifier re-derives every PROVED
item and writes VERIFICATION.md with a verdict table. All agents write their outputs to files on
disk BEFORE returning (structured returns have been observed to crash). Poll background work at
≤ 5-minute intervals. Numerics in Julia with red/green TDD and git commits at each step.

Success = a proved theorem with its exact scope, verified against oracles — or a sharp refutation
with the surviving weaker statement identified. A pile of unproven analogies is failure.
