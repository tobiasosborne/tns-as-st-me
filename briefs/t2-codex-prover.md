# Work order — T2 prover (codex lane B)

You are the PROPOSER for Theorem AC-EX in an adversarial rk-light loop; a
hostile critic from a different model family will attack every step by
independent recomputation. You are a relentless prover: given the target,
work it to the end. Do not stop at a survey or a plan — produce the proof.

READ FIRST, in order:
1. briefs/memory-campaign-target.md  (the target — Lane T2 is yours)
2. CLAUDE.md (laws; L6b Lamport format is mandatory)
3. definitions.md, notation.md (single sources — cite, never redefine;
   D18 defines the AD clauses your theorem partially discharges)
4. claims/CLAIMS.md
5. refs/arxiv-1412.2970/Scattering_spin-AHP1.tex — your PRIMARY technique
   source (Bachmann-Dybalski-Naaijkens Haag-Ruelle for gapped spin systems).
   Identify precisely which lemmas use translation invariance of the VACUUM
   and what replaces it in the kink sector.
6. theory/memory-quantization-general.md (H-AD-G — you are proving the
   existence half of AD1 + the AD2 setup, conditionally on band data)
7. refs/arxiv-1103.2286, refs/arxiv-1810.07006 (excitation ansatz — the
   source of your ASSUMED spectral hypotheses; assumed, not derived)

YOUR LANE (writable): theory/ansatz-scattering.md — nothing else. Create
it. Everything for shared files goes in MERGE PROPOSALS as exact text.

DELIVERABLE: theory/ansatz-scattering.md, Lamport style per the output
contract in the target doc:
- Sharpened H-ACE with the inelastic-threshold inequalities stated
  explicitly in band data (kink bandwidth vs magnon gap etc.).
- (ACE.1) existence via Cook's method: kink-magnon precursors, the fibered
  translation action on 𝒦_αβ, Lieb-Robinson + stationary-phase estimates
  ported from 1412.2970 with every port re-derived (analogy is not proof).
- (ACE.2) isometry + N_T on the constructed out-subspace; completeness
  explicitly NOT claimed.
- (ACE.3) bridge lemma to the T1 outcome measure (read Lane T1's target
  statement in the target doc; do NOT read or wait for the T1 shard).
- CHECKER SPEC + MERGE PROPOSALS + HONEST STATUS sections.

RULES OF ENGAGEMENT:
- Downgrade over ambition; a fixed-packet existence theorem with explicit
  hypotheses beats a sketched completeness claim. NO soft-limit claims.
- Every leaf: D-number, claim id, named computation, or refs/ location.
- Budget: ~2 hours. If the full kink-background port resists, land the
  clean special case (kink initially at rest / narrow kink band) with the
  general obstruction stated precisely.
- Work fully autonomously. Never ask questions. Never wait.
