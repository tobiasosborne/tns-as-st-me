# Work order — (PROTO-LSZ) and (MATCH-S): the last gaps of the soft limit law

The soft-index ladder now has PROVED finite theorems at general compact G
(claims rows S-IDX-fin-r2, S-IDX-fin-G, S-IDX-G-label). The limit law
S-IDX-spec-r2 sits at SKETCH with exactly two named missing hypotheses,
both model-level (claims rows S-IDX-spec-struct-r2, S-IDX-spec-r2;
skeleton slot "§5 limit law"):

- **(PROTO-LSZ):** the finite protocol-to-LSZ decomposition for the
  fixed-time D29 charge-created datum;
- **(MATCH-S):** identification of the fixed-time D29 readout with the
  on-shell multiplier through `o(ε)`.

Your job: prove one or both for a concrete class — the fully polarised
spin-S band of D6/H_S is the natural first target, because there
S2-2body-S (PROVED) supplies the on-shell side exactly. Partial results
that shrink the gap honestly (e.g. (MATCH-S) proved under a displayed
decay hypothesis that D6 satisfies) are valuable; relabeling is not.

## Process contract (PRD.md — read first)

ONE hostile critic + ONE repair follow a positive delivery. An
OBSTRUCTION gets a sharp header and no rounds. Honest labels per step.
The falsifier rule binds: your statements must be consistent with the
passed probe data (theory/checks/soft_index_probe.py, quote as
P1+P2(a)-only — its P2(b) gate is a known no-op, bd tns-9z4).

## READ

PRD.md; paper/skeleton.md; theory/soft-index-r2.md IN FULL (the ladder
you are completing — especially §3's displayed (PROTO-LSZ)/(MATCH-S)
statements and the D29 MERGE PROPOSALS, which remain quarantined);
theory/verdicts/soft-index-r2-critic.md (what the critic certified and
what it fenced); claims rows S2-2body-S, AC-EX-2M, S-IDX-HR-value-r2
(the on-shell instance deliberately kept separate — understand why
before you try to connect anything); theory/ansatz-scattering-2m.md
⟨1⟩2–⟨1⟩7′ (the wave-operator machinery available to you);
theory/soft-current-recon.md (R15)–(R18); definitions.md D6–D8, D24–D31.

## HARD FENCES

1. The value 1/S enters ONLY through S2-2body-S matching. No
   stipulation, no regularity-only pinning (proved impossible), no
   𝔞_leg derivation (AMP obstruction, theory/amp.md — a leg
   normalisation supplies only Z_ρ^{-1/2}, D24N-C8).
2. Register discipline per the ML4-Ward ERRATUM everywhere.
3. No D29/D30 merge — your refinements go in MERGE PROPOSALS.
4. S-IDX-HR-value-r2's separation stands: a Haag-Ruelle on-shell
   instance is not a D29 protocol instance. If your (MATCH-S) proof
   BUILDS the bridge between them, that is exactly the theorem wanted —
   but it must be a proof, not an identification by fiat.

## LANE (writable; NOTHING else)

- theory/proto-lsz-match.md (CREATE — L6b shard)
- theory/checks/proto_lsz_match_check.py (CREATE — green exit 0 under
  python3 -O, no bare asserts, ≥1 red mode per load-bearing identity;
  reuse the probe's frozen data where relevant rather than re-deriving)
- theory/proto-lsz-match-notes.md (CREATE, optional)

No edits to existing files. MERGE PROPOSALS for proposed CLAIMS rows.
No commits.

## Deliverable shape

(0) header: which hypothesis is proved, for which class, in the first
ten lines; (1) setup by D-number; (2) the ladder; (3) interfaces to
S2-2body-S / AC-EX-2M as used; (4) checker section; (5) MERGE PROPOSALS.
Write each section as you complete it.
