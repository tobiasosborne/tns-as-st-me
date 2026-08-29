# Work order — SPECULATIVE HUNT: Duistermaat–Heckman in the lattice IR triangle (TJO directive 2026-08-29)

You are a speculative exploration lane. TJO's standing question: can the
**Duistermaat–Heckman theorem** (exact stationary phase; DH pushforward of
Liouville measure along a torus moment map is piecewise polynomial with
wall-crossing jumps; Atiyah–Bott/Berline–Vergne localization at fixed
points) be exploited in this project **non-artificially**? A previous
answer was "maybe". Your job: hunt down a useful application, consequence,
or creative result — or establish honestly that every candidate is
artificial.

**Non-artificial means:** DH does work that no simpler tool already does
in this repo. Rewriting a proved statement in DH vocabulary is worthless —
that exact failure mode just killed lane G3 (theory/soft-index-g3.md
⟨1⟩18, REPRODUCTION-ONLY: the "geometric proof" was the algebraic one in
Fubini–Study clothes). Read its ⟨1⟩17 fences and do not violate them.

## Process contract (PRD.md — read first)

Allowed outcomes, state yours in the header:
- **RESULT** — a new provable statement where DH is load-bearing, with at
  least the finite-dimensional instance proved and ED-checked;
- **PROGRAM** — a credible route with the FIRST computation actually done
  (not a wishlist);
- **NOTHING NON-ARTIFICIAL** — every candidate dies; say why, sharply.
Negative outcome ⟹ no rounds, line ends (PRD). Honest labels throughout;
speculative sections marked SPECULATIVE.

## READ

PRD.md, paper/skeleton.md (a result is valuable in proportion to the
skeleton slot it could fill), notation.md, definitions.md;
theory/soft-index-g3.md (the fresh anchor: exact postselected root
increment `μ_T([F_αψ])−μ_T([ψ]) = −α`, SU(3)-ED-verified, plus its
hybridization fences); docs/framing.md and briefs/bta-kahler-target.md
(TJO's Kähler/moment-map program — DH is its natural next theorem);
CLAIMS rows M-INDEX-fin, M-INDEX-spec, M-IDX-density, S-IDX-fin-r2,
SPT-E'; theory/memory-index.md §on the escaped-charge law.

## CANDIDATE DIRECTIONS (starting points, not limits — kill freely)

1. **The memory law as a DH measure.** M-INDEX-spec: every subsequential
   TPM escaped-charge law is a probability on ℤ. The DH pushforward of a
   torus moment map on a (projectivized sector / MPS manifold) is
   piecewise polynomial with integer wall structure. Is the escaped-charge
   law literally a DH measure for a natural torus action — making its ℤ
   support a DH integrality statement and the memory quantum a DH wall
   datum? A finite-N exact statement here would be a RESULT.
2. **Weight-multiplicity asymptotics.** The finite-dimensional DH measure
   of the sector torus action IS the weight distribution; its N→∞ limit
   shape controls the m_λ registers appearing in S-IDX-fin. Does DH
   piecewise-polynomiality give the uniform-in-N regularity that any
   (PROTO-LSZ)-type hypothesis needs — turning a SKETCH hypothesis into a
   theorem for a class of vacua?
3. **Localization for the soft limit.** k_s → 0 is the fixed locus of a
   circle action on the magnon band. Does ABBV localization compute the
   soft coefficient/Adler zero as a fixed-point contribution — giving the
   VALUE from geometry where D24 provably cannot (AMP obstruction,
   theory/amp.md)? Beware: any route producing 𝔞_leg must confront the
   D24N-C8 double-count fence (claims row AMP) or it is wrong.
4. **Wall-crossing = the rigidity dichotomy.** DH jumps at critical
   moment values vs the quantized-edge-residue plateau vs drifting bulk
   coefficient (skeleton §6, Fig 3). Is the SPT edge residue a DH
   invariant that CANNOT drift between walls — a no-go theorem for
   coefficient drift, checkable in the λ-D numerics?
5. **M-IDX-density via convexity.** 2ρ ∈ ℤ from integral vertices of the
   moment polytope — only interesting if it EXTENDS the proved row
   (new groups, new invariants), not if it re-derives it.

## LANE (writable; NOTHING else)

- theory/dh-hunt.md (CREATE — findings; L6b rigor for anything you call
  proved, prose allowed for the hunt narrative)
- theory/checks/dh_hunt_check.py (CREATE only if you have a RESULT or a
  PROGRAM's first computation: ED verification, green exit 0 under
  python3 -O, no bare asserts, ≥1 red mode)
- theory/dh-hunt-notes.md (CREATE, optional)

No edits to existing files; MERGE PROPOSALS section only if you have a
RESULT. No commits.

## Deliverable shape

(0) header: RESULT / PROGRAM / NOTHING NON-ARTIFICIAL, with the one-
sentence version and — if positive — the skeleton slot it fills; (1) the
hunt: each candidate direction with a verdict (dead: why; alive: the
computation); (2) the best item worked as far as one session allows;
(3) checker section if warranted; (4) MERGE PROPOSALS if warranted.
Write sections as you complete them.
