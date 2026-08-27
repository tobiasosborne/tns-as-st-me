<!-- ROLE: campaign target specification for the 2026-08-27 max-ambition
     memory-theorem campaign (TJO greenlight: 4-6h, 3 codex xhigh + 3 Fable).
     Both T1 provers and the T2 prover read THIS FIRST, then the read-order
     gate: CLAUDE.md -> definitions.md -> notation.md -> claims/CLAIMS.md ->
     theory/memory-quantization-general.md -> theory/TRIANGLE.md §3. -->

# Campaign target — the general memory theorem, two lanes

## Why this campaign exists

The corpus's memory corner is M-quant-G: a conditional implication whose
entire physical content sits in H-AD-G = D18(AD1-AD4) — wave operators,
asymptotic completeness, an exhaustive two-channel inventory, no bound
states. That hypothesis is (a) proved for no model, (b) FALSE in general
(wall-magnon bound states, kink absorption when the kink bandwidth exceeds
the magnon gap, extra bands), and (c) degenerate exactly at the soft
endpoint (group velocity -> 0 kills every propagation estimate). The
campaign goal is to RESTRUCTURE the theorem so that:

  **Quantization of memory needs no scattering theory at all.
  Scattering theory is only needed to compute the VALUE.**

Lane T1 proves quantization from superselection/charge-ledger structure
alone. Lane T2 proves rigorous existence (not completeness) of the
kink-magnon wave operators from excitation-ansatz band data, which computes
the value in the two-channel regime and bridges to M-quant-G.

## Standing setting (cite, never redefine — L4)

All from `definitions.md` / `theory/TRIANGLE.md` §0:
(H1) injective uniform MPS vacuum family, D1; (H2) compact G, covariant
family, D2(a); selected unbroken circle direction ξ with on-site charge
S^z := -i q(ξ), vacuum densities ω_α(S^z)=+s, ω_β(S^z)=-s, s>0, exactly
H-MQG(2) of `theory/memory-quantization-general.md`; (H4) finite-range
G-invariant H, D10, both vacua stationary, cut-current continuity G0(e);
kink sector 𝒦_αβ from A2(a,c,d,f); ℓ¹ packet class D17; wall coordinate
𝔛_W D13(a) (one lattice translation of the kink = regularized charge 2s);
order of limits ALWAYS: infinite-volume dynamics first, then t→±∞ at fixed
window, then window → ℤ (the D17/AD4 discipline; the k→0 soft limit NEVER
commutes with these).

New hypotheses may be introduced ONLY as numbered proposals (D26, D27, ...)
in a MERGE PROPOSALS section of your shard; definitions.md is not your
lane.

## Lane T1 — THEOREM M-INDEX (memory quantization as superselection)

### Target statement (template — sharpen, weaken, or split as the proof demands)

**ASSUME (H-IDX).**
1. H-MQG(1)-(4) verbatim (so: NO H-AD-G, NO D18, NO channel inventory).
2. **(INT — integrality/circle hypothesis.)** The on-site representation of
   the selected circle {exp(θξ)} is a genuine U(1) representation up to
   phase: e^{2πi S^z_x} = c·𝟙 on-site, |c|=1. (True for every spin-S chain;
   state it as D26.)
3. **(LR — local relaxation, minimal dynamical input; formulate as D27.)**
   For the selected D17 packet vector Ψ and each fixed window W ⊇ wall
   core: the window-restricted Heisenberg state converges as t→±∞ in the
   Cesàro (time-averaged) sense along a common subsequence, AND the family
   of spectral distributions of the regularized window charge Q̂_W(t) in Ψ
   is tight, uniformly in t, with vanishing boundary-straddling mass
   (charge does not accumulate on ∂W as the double limit is taken).
   Formulating the WEAKEST sufficient (LR) is half the theorem's value.

**PROVE.**
(G-IDX.0) *Sector charge integrality.* In the GNS representation of 𝒦_αβ
   the regularized total charge Q̂ exists as a self-adjoint operator,
   e^{2πiQ̂} is a scalar, hence Q̂ has PURE POINT spectrum contained in a
   single coset q₀ + ℤ. (Route: A2 covariance + (INT) + D17 summability;
   this is the superselection-integrality lemma L-A. It should be
   UNCONDITIONAL — no (LR).)
(G-IDX.1) *Ledger.* 2s·(𝔛_W-jump between the two asymptotic limits)
   = −(asymptotic escaped-charge difference); the finite-time version is
   exactly M-flux (already PROVED — cite, do not reprove).
(G-IDX.2) *Quantization.* Under (LR), the limiting distribution of the
   two-time wall-charge difference is a probability measure {p_ν} supported
   on ℤ (offsets cancel in the difference), so
        δx = −(1/2s)·Σ_ν ν·p_ν,   ν ∈ ℤ,
   and every asymptotic memory outcome is an integer multiple of 1/(2s).
   Bound states, extra channels, absorption: all ALLOWED — they land on
   other integers ν, they do not break the theorem.
(G-IDX.3) *Consistency corollary.* Under additionally H-AD-G, {p_ν} is
   supported on {0, 2} with p₂ = ⟨N_T⟩ and (G-IDX.2) reduces exactly to
   M-quant-G (G.1)-(G.2). (This anchors the new theorem to the converged
   row; any mismatch is a FATAL bug in your proof.)

### Known landmines (the critic WILL attack exactly here)

- **Two-time fallacy.** Q̂_W(t) and Q̂_W(−t) do not commute; "difference of
  lattice-valued observables is lattice-valued" is FALSE in general. The
  quantization must come from the asymptotic structure (e.g. the limit
  distribution is a difference of values on a fixed coset — offsets must
  cancel EXACTLY, do the bookkeeping in public), not from naive spectral
  arithmetic. If you need asymptotic commutativity, PROVE it or put it in
  (LR) explicitly.
- **Weak-limit smearing.** Weak-* limits of lattice-supported measures stay
  lattice-supported only with tightness; a lattice with W-dependent offset
  drifting as W→ℤ can smear the support. The D13(a) calibration and the ℓ¹
  first-moment clause are what pin the offset; use them explicitly.
- **What does "the wall charge at t=+∞" mean** before channels exist? Only
  the double limit (t first, then W) is available. Every statement must
  survive the AD4 limit order.
- **δx itself is NOT claimed quantized** — it is a {p_ν}-average. Only the
  outcome spectrum is quantized. Do not overclaim; this exact overclaim
  killed Conjecture M (see REFUTED row M).
- s>0 is a real number; nothing may assume s ∈ ½ℤ.
- Fallback ladder (L5-honest): M-INDEX-full (decoherence/convergence proved
  from clustering) > M-INDEX-spec (quantization under explicit (LR)) >
  M-INDEX-exp (ledger identity only — this is nearly free and already
  close to M-flux; landing ONLY this is a FAILURE of the campaign, say so
  honestly if it happens).

### Ground truth you may cite (L3 — only these, only from refs/)

refs/arxiv-1810.07351 (BBDF many-body transport index — for the index
PHILOSOPHY and any technique you can genuinely port; their setting is
adiabatic pumping on a gapped ground state, NOT scattering — any claimed
port must be re-derived, not analogized), refs/arxiv-0802.0447 and
refs/arxiv-2011.12127 (MPS symmetry structure), plus everything already in
theory/ at its DAG status. Citing a result from memory without a refs/
file = FATAL objection.

## Lane T2 — THEOREM AC-EX (ansatz-conditioned wave-operator existence)

### Target statement (template)

**ASSUME (H-ACE).** H-MQG(1)-(3); the kink sector 𝒦_αβ carries a
translation action (A2) and its Hamiltonian has, in the fibered
(momentum) decomposition: an isolated kink band p ↦ E_K(p) with C²
dispersion, and the vacuum sectors carry an isolated magnon band
k ↦ ω(k); the selected incoming data are D17 packets with DISJOINT,
NONZERO group-velocity supports for magnon and kink, and total energy
below every inelastic threshold expressible in the band data (state the
inequalities explicitly — e.g. kink bandwidth vs magnon gap for the
absorption channel). These spectral hypotheses are exactly what the MPS
excitation ansatz computes (refs 1103.2286, 1305.2176, 1810.07006); they
are ASSUMED here, not derived.

**PROVE.**
(ACE.1) Haag-Ruelle-type existence: the kink-magnon precursor states
   converge as t→±∞ (Cook's method + Lieb-Robinson + stationary phase,
   following refs/arxiv-1412.2970 adapted from two particles over one
   vacuum to one magnon over a one-kink background — the adaptation IS the
   theorem; identify precisely where translation invariance of the vacuum
   was used in 1412.2970 and how the kink sector's translation action
   substitutes).
(ACE.2) The wave operators are isometries on the packet domain; N_T is
   well-defined on the CONSTRUCTED out-subspace (completeness NOT claimed,
   range NOT claimed to exhaust anything).
(ACE.3) Bridge lemma: on ran W₊ the T1 outcome measure {p_ν} restricted to
   the constructed channels reproduces ⟨N_T⟩-weighted charge bookkeeping —
   i.e. T2 computes the p_ν that T1 quantizes.

### T2 landmines

- 1412.2970 builds scattering states from ONE translation-invariant vacuum;
  the kink breaks translation invariance of the STATE but the SECTOR is
  translation-covariant — make the fibering precise before using Arveson
  spectra.
- The soft limit k→0 violates the velocity-separation hypothesis; AC-EX is
  a FIXED-packet theorem. Say so; do not claim any soft statement.
- Almost-eigenvector errors: if you assume the ansatz states are exact band
  eigenstates, say EXACT; if approximate, the error must enter Cook's
  integral quantitatively — choose one register and keep it.

## Output contract (both lanes; L6b)

Your ONLY writable files: your shard (stated in your brief) — Lamport
hierarchical proofs (⟨1⟩1, ⟨2⟩3, ASSUME/PROVE per nontrivial step, QED
steps, every leaf citing a D-number, a claim id, a named computation, or a
refs/ file+location), plus a final section: (i) MERGE PROPOSALS (exact
replacement text for definitions.md D26/D27..., claims/CLAIMS.md new rows
at status SKETCH, notation.md if needed); (ii) CHECKER SPEC — a concrete
machine-checkable certificate for at least one load-bearing step (what to
compute, on what model, expected value, and a mutation that must fail);
(iii) HONEST STATUS — what you proved, what you assumed, what broke.
Self-status is SKETCH; only the L6 loop promotes. Do not edit any shared
file. Do not touch numerics/. Work fully autonomously; never ask questions.
