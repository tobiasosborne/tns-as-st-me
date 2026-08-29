# Work order — general-G soft index, strategy G5: boundary mapping / falsifier (bd tns-fea)

Parallel strategy 5 of 5. The other four lanes try to PROVE the general-G
finite soft index identity by different routes. Your job is the opposite
and equally valuable (PRD: falsifiers are early warning, binding in the
negative): map WHERE the theorem can possibly hold, by hunting
counterexamples and degenerate cases BEFORE the critic rounds. Your
output directly shapes the hybridization: any general claim a prover lane
makes that your battery kills is dead on arrival.

**Mandatory battery (compute, do not speculate):**

1. **Abelian G = U(1)^k.** No roots, no ladder operators. Does a soft
   index identity even have content here (no broken-charge-created
   magnon in the SU(2) sense)? Determine what the correct degenerate
   statement is — trivially-true, empty, or genuinely different.
2. **Finite groups.** Corner A records finite groups as a hard fence for
   charge quantization. Verify by explicit small-model ED whether the
   finite identity has a finite-group analogue or provably cannot
   (discrete charge, no current zero modes — what replaces J^z?).
3. **Non-simply-connected and disconnected G** (SO(3) vs SU(2); O(2)):
   does the identity see the fundamental group / the disconnected
   components? ED a small SO(3)-symmetric chain where the SU(2) lift
   changes the sector lattice.
4. **Broken vs unbroken interplay.** The SU(2) theorem lives where the
   symmetry acts with a highest-weight sector structure. Construct an
   instance where the unbroken subgroup H is nonabelian (e.g. G=SU(3)
   broken to H=SU(2)×U(1)) and test the natural generalization
   numerically on small N: does the multiplicity-space action break the
   naive per-root identity? THIS IS THE CENTRAL EXPERIMENT — it directly
   tests G1's route.
5. **The register trap at rank >1.** ml4_ward_n2_check.py certified the
   SU(2) full-sector/highest-weight trap at 0.00e+00. Build the SU(3)
   analogue of that certificate: exhibit numerically whether the naive
   scalar-weight substitution fails at rank 2 the way it fails at SU(2).

Process contract: PRD.md. You produce DATA and sharp finite statements,
not a proof shard: every claim in your report must be an ED-verified
computation with the script that reproduces it. Honest negatives are the
product here — this lane cannot fail by finding obstructions, only by
being vague.

READ: PRD.md, notation.md, definitions.md; theory/soft-index-r2.md §2;
theory/corner-a.md (the finite-group fence rows); theory/checks/
ml4_ward_n2_check.py (the certificate style to imitate);
theory/checks/soft_index_r2_check.py.

LANE (writable, NOTHING else): theory/soft-index-g-boundary.md (CREATE —
findings, one section per battery item, each with the computed numbers
and the reproducing command), theory/checks/soft_index_g_boundary_check.py
(CREATE: runs the whole battery, green exit 0 under python3 -O, no bare
asserts; each battery item is a gate with its finding encoded — including
NEGATIVE findings as assertions that the failure persists). No edits to
existing files. No commits.

Deliverable: (0) a summary table in the first thirty lines — battery item
→ finding (HOLDS / FAILS / DEGENERATE / DIFFERENT-STATEMENT) → number →
gate name; then the sections. Write sections as you complete them.
