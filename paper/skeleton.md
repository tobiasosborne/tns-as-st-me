<!-- ROLE: the value-gate instrument (PRD.md). Every lane's output must land
     in a named slot here, or the lane does not run. Bullet-scale by design.
     This is NOT paper v2 (parked, not endorsed) — it is the v3 target.
     Every [id] is a claims/CLAIMS.md row; every GAP names its bd lane. -->

# Letter skeleton — the infrared triangle on the lattice

**Spine sentence** (each section is one clause of it):
*Symmetry quantizes the infrared data; the excitation ansatz supplies the
kinematics; dynamics only picks the values.*

**Register:** arXiv:1305.2176. 4 pages, exactly 3 figures, captions tell
the story alone (L9).

## Title (working)

- "The infrared triangle of a quantum spin chain" — or
- "Soft theorems, asymptotic symmetry, and memory in matrix-product states"

## Abstract (bullet scale)

- The continuum IR triangle (soft theorem / asymptotic symmetry / memory)
  has an exact 1D lattice avatar, formulated in MPS language.
- But its logic reshuffles: quantization of the memory needs NO scattering
  theory [M-INDEX-fin, M-INDEX-spec]; scattering only computes the value
  [S2-2body-S]; and the naive universality conjecture is FALSE
  [Conjecture-M refutation — prints as a central result, TJO directive].
- The soft slope is 1/S for every site spin, proved without integrability
  input on the two-body sector [S2-2body-S] and matched by wave operators
  built from ansatz band data alone [AC-EX-2M].
- An SPT rigidity dichotomy separates quantized edge residues from
  drifting bulk coefficients [SPT-E', SPT-M'] — illustrated on one
  non-integrable model (λ-D chain) crossing its phases. GAP→tns-f5r.

## §1 — Introduction

- Continuum triangle in two sentences (cite 1703.05448; Hamada–Sugishita
  1709.05018 as the direct scalar antecedent — refs/ has all TeX, L3).
- The question: is the triangle a theorem anywhere? On the lattice it can
  be, and the proof structure is NOT the continuum's: burden inverted.
- Announce the three results + the refutation as the fourth.

## §2 — Setup (half a column, definitions by pointer)

- Injective MPS vacua, kink sectors, windowed charge Q̂_{W,c₀} [D13, D16,
  D26]; TPM protocol datum [D27]. NO redefinitions — D-numbers own this.
- The λ-D chain as the running example Hamiltonian (also the numerics
  model): Néel / Haldane / large-D in one phase diagram.

## §3 — Corner A: asymptotic symmetry (shortest section; strong + done)

- Charge quantization: charges live on the center of the unbroken
  subgroup; Weyl group makes the walls; finite groups a hard fence
  [corner-A rows + tns-pwl scope theorem].
- Density by-product: 2ρ ∈ ℤ for U(1)-covariant injective-MPS
  antisymmetric vacuum pairs [M-IDX-density] — LSM-flavored, one sentence.

## §4 — Corner B: memory, quantized without scattering (the centerpiece)

- Finite window: coset integrality is UNCONDITIONAL [M-INDEX-fin].
- Limit law: D26(INT) + D27(LR, tightness only) ⟹ every subsequential
  TPM escaped-charge law is supported on ℤ, δx = −(2s)⁻¹ Σ ν·p_ν
  [M-INDEX-spec]. No channel inventory; bound states allowed.
- The window charge is not a new object: Q̂ lifts the conserved wall
  coordinate exactly, 𝒬_{c₀} = 2s(X₁ − c₀) [LD-ID] — and this identity
  KILLS the loophole class (no escaping-leg state has t-uniform kink
  tails) [LD-ID (i)].
- Half of (LR) is a theorem for free: Cesàro clause 1 from separability +
  strong continuity alone [LR1-GEN]; energy bounds the domain-wall NUMBER
  in D16 uniformly in time [LR-D16-EDW].
- **GAP (the one honest hole in this section): D27 clauses 2–3 for D16**
  — the first fully unconditional dynamical instance. bd tns-xf4. If it
  stays open, the section prints the conditional form honestly; the
  theorem does not fall.

## §5 — Corner C: the soft theorem (structure vs value)

- Two-body, every spin S: exact slope ∂δ_phys|₀ = sgn(v_h−v_s)/S, no
  integrability assumed [S2-2body-S]; Bethe oracle agreement [OR1, O7–O9].
- Wave operators exist from ansatz band data alone; W₊*W₋ IS the physical
  S-matrix [AC-EX-2M] — "the ansatz supplies the kinematics."
- **GAP (the headline theorem): the soft law as a symmetry constraint on
  every limit point of the charge-created protocol datum** — S-IDX-fin →
  S-IDX-spec, value pinned by on-shell matching to [S2-2body-S], never by
  stipulation. bd tns-v44, IN FLIGHT. This is the sentence the Letter
  exists for; if the lane fails r2, the section becomes the two-body
  theorem + the falsifier evidence, labelled as such.
- One sentence of honesty: universality beyond the protocol class is
  REFUTED [ML5 scoping / Conjecture-M], and the coefficient carries no
  number from factorization alone — the value is on-shell data.

## §6 — Memory effect seen: the λ-D chain (numerics; Fig. 2+3 feeder)

- Non-integrable by construction — the integrability-free hypotheses of
  §4–5 are load-bearing, not decorative.
- Kink transport in the Néel phase: measured δx/N_T = −1/s on integers
  [existing: spin-s falsifier data; NEW: λ-D points GAP→tns-f5r wave 2].
- Rigidity dichotomy across Haldane/large-D: quantized edge residue
  plateau vs drifting bulk coefficient [SPT-E', SPT-M'; data GAP→tns-f5r
  wave 1 sweep].

## §7 — Discussion (5 sentences max)

- What survived the continuum analogy, what did not (the refutation is
  content, not apology) — L10 register.
- The inverted burden as the exportable lesson: symmetry ⟹ quantization;
  dynamics ⟹ values. Kähler/moment-map outlook, one clause [tns-89h].

## The three figures

- **Fig. 1 — the lattice triangle, annotated.** The three corners with
  their claim-status: PROVED / PROVED / theorem-with-named-gap, edges
  labelled by the actual implications (A⇒B charge quantization; C⇒B value
  transfer through p₂; A⇒C Ward constraint). Caption states the spine
  sentence. [Drawn from CLAIMS.md; no new math. Can be made TODAY.]
- **Fig. 2 — memory quantization.** λ-D Néel kink: escaped-charge
  distribution on ℤ, δx staircase vs −(2s)⁻¹Σν·p_ν; inset: the D16
  falsifier integers. [GAP→tns-f5r wave 2 + existing results JSON.]
- **Fig. 3 — the dichotomy.** String order + entanglement degeneracy +
  edge residue across the Haldane/large-D sweep: the quantized plateau
  survives where the bulk coefficient drifts. [GAP→tns-f5r wave 1.]

## Gap ledger (the whole to-do list of the Letter)

| Slot | needs | lane | status |
|---|---|---|---|
| §5 headline (finite thm) | — | tns-v44 | **DONE: S-IDX-fin-r2 PROVED** |
| §5 generality | — | tns-fea | **DONE: S-IDX-fin-G + S-IDX-G-label PROVED (compact G)** |
| §5 limit law | (PROTO-LSZ) + (MATCH-S) for the D29 datum | none yet | SKETCH rows entered; next theory target |
| §4 instance | D27(2–3) for D16 | tns-xf4 | open; conditional print OK |
| §6 + Fig 3 | λ-D wave 1 (sweep) | tns-f5r | Opus IN FLIGHT |
| §6 + Fig 2 | λ-D wave 2 (kinks) | tns-f5r | after wave 1 |
| Fig 1 | drawing only | — | unblocked NOW |
| everything else | already PROVED | — | cite and write |

Anything a lane produces that has no slot in this file does not go in the
Letter and gets no further budget (PRD value gate).
