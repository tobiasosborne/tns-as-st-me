<!-- LANE BRIEF Q3: definitional audit, corner C (soft insertions) vs 3+1
     lattice QED. TJO directive 2026-08-30: audit the DEFINITIONS — show what
     the discrete and continuous soft-theorem definitions say about each
     other. Heuristics ok. Output: theory/lanes/reduction/q3-soft-defs.md,
     INCREMENTALLY. -->

# Q3: Do the campaign's soft-insertion DEFINITIONS discretize the accepted soft-photon definitions?

## Inputs

- `definitions.md` D10 (modulated charge Q[f;ξ]), D12 (the limits in which
  the gauge remainder vanishes), D24(b) (leg normalisation), D25 (soft
  multiplier); the PROPOSED D29 fixed-time charge-created protocol datum
  (quarantined in theory/soft-index-r2.md §7 MERGE PROPOSALS — read it).
- `claims/CLAIMS.md` rows G0, S-IDX-fin-r2, S-IDX-MATCH-HS-SEP,
  AC-EX-2M-D29 (the last one documents an O(k_s) mismatch between the
  fixed-time datum and Haag–Ruelle creators — central to this audit).
- `refs/arxiv-1703.05448/soft_Arxiv_update.tex` (LOCAL TeX): the QED soft
  theorem — the Weinberg pole S⁽⁰⁾ = Σ_k e_k (p_k·ε)/(p_k·q), its LSZ
  definition (amputated amplitude, photon momentum q → 0), and the
  statement that Q_ε-insertion between in/out states IS the soft theorem.
  Quote with file+line.
- `refs/arxiv-1709.05018/draft1004.tex`: the global-symmetry (gauge-free)
  version — Q^soft as a limit of Goldstone creation operators (L.361).
- Lattice QED background [textbook]-flagged; no memory-quoted arXiv ids;
  verify any fetched title.

## Task

1. **The two definitions of "insert a soft quantum."** Continuum-accepted:
   an LSZ-amputated asymptotic photon/Goldstone leg with momentum q → 0
   AFTER the t → ±∞ limit. Campaign: a FIXED-TIME modulated-charge
   insertion Q[f_ε] on a prepared state (D29). These differ by an order of
   limits. Make the difference quantitative in the simplest QED setting you
   can (heuristic perturbative lattice QED, or the campaign's own D6 model
   as the control case): compute or estimate what a fixed-time charge
   insertion creates versus what an asymptotic soft leg is, and relate to
   the campaign's own documented O(k_s) mismatch (AC-EX-2M-D29 row) and to
   the proved zero-remainder matching on the separated class
   (S-IDX-MATCH-HS-SEP). The deliverable: a clean statement of WHEN
   (which limit sequence, which state class) the fixed-time definition and
   the accepted LSZ definition coincide, and at what order they differ
   otherwise.
2. **The Weinberg-pole control experiment.** The campaign asserts (brief
   §5.1) that no 1/ω pole exists without a gauge mediator. Run the
   definitional control: in lattice QED, does the campaign's definitional
   apparatus (modulated charge insertion, soft multiplier as first jet)
   PRODUCE the Weinberg pole when transplanted? Heuristically derive: the
   coupling of the soft lattice photon to a hard charged leg gives the
   1/(p·q) factor from the propagator adjacent to the emission vertex;
   show where in the campaign's definitional language this pole would sit
   (a 1/k first jet of the multiplier instead of an Adler zero), and hence
   that the definitions correctly DISTINGUISH the gauge and global cases
   rather than being blind to the difference. If they do not distinguish
   them, that is a definitional failure — report it.
3. **G0's pure-gauge clause vs the continuum statement "a soft photon is a
   large gauge transformation".** The campaign proves the k = 0 Goldstone
   insertion is pure gauge on unbroken directions (G0). The continuum canon
   says the ω → 0 photon is pure large-gauge. Compare the two DEFINITIONS
   of "pure gauge" (MPS null direction B = AX − XA vs A_μ → A_μ + ∂_με)
   and state the exact correspondence and its limits.
4. **Verdict per definition** (D10+D12, D24(b)/D25, D29-proposed): same
   object as the accepted one under stated limits / same up to listed gaps
   / different (and what the difference does).

## Rules

Physics register; [physical argument]/[textbook] flags; continuum quotes
from local TeX with file+line; statuses unchanged (D29 stays PROPOSED); no
edits outside theory/lanes/reduction/; no bd operations; no LEDGER edits.
