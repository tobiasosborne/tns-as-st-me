# Work order — T1 prover (codex lane A)

You are the PROPOSER for Theorem M-INDEX in an adversarial rk-light loop; a
hostile critic from a different model family will attack every step by
independent recomputation. You are a relentless prover: given the target,
work it to the end. Do not stop at a survey or a plan — produce the proof.

READ FIRST, in order:
1. briefs/memory-campaign-target.md  (the target — Lane T1 is yours)
2. CLAUDE.md (laws; L6b Lamport format is mandatory)
3. definitions.md, notation.md (single sources — cite, never redefine)
4. claims/CLAIMS.md (the DAG; note REFUTED row M — do not rely on it)
5. theory/memory-quantization-general.md (M-quant-G — your theorem must
   reduce to it under H-AD-G, per (G-IDX.3))
6. theory/memory-quantization.md, theory/TRIANGLE.md §3 (context)
7. refs/arxiv-1810.07351/Index_Re.tex (BBDF index — technique source)

YOUR LANE (writable): theory/memory-index.md — nothing else. Create it.
Everything for shared files goes in your MERGE PROPOSALS section as exact
replacement text.

DELIVERABLE: theory/memory-index.md containing, in Lamport hierarchical
style per the output contract in the target doc:
- The sharpened statement of M-INDEX (H-IDX, (INT)=D26 proposal, (LR)=D27
  proposal — formulate the WEAKEST (LR) you can actually use).
- Lemma L-A = (G-IDX.0) sector charge integrality, proved UNCONDITIONALLY
  (no (LR)). This lemma alone is publishable; get it airtight.
- (G-IDX.1) ledger, citing M-flux rather than reproving.
- (G-IDX.2) quantization under (LR) — the heart. The two-time landmine and
  the weak-limit-smearing landmine in the target doc are where you will be
  attacked; address both IN the proof, with explicit offset bookkeeping.
- (G-IDX.3) consistency reduction to M-quant-G (G.1)-(G.2).
- CHECKER SPEC + MERGE PROPOSALS + HONEST STATUS sections.

RULES OF ENGAGEMENT:
- Downgrade over ambition at every fork: a weaker proved statement beats a
  stronger sketch. Record every retreat in HONEST STATUS.
- Every leaf justification: D-number, claim id, named computation, or
  refs/<id>/<file> + location. A citation from memory is a FATAL defect.
- No integrability, no model-specific input, no s ∈ ½ℤ.
- Budget: ~2 hours of focused work. If (G-IDX.2) resists, land L-A +
  (G-IDX.1) + the sharpest partial (G-IDX.2) you can prove, and state
  exactly which step is missing and why.
- Work fully autonomously. Never ask questions. Never wait.
