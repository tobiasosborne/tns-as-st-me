<!-- LANE BRIEF O1: operational-status audit of the campaign's definitions.
     TJO directive 2026-08-30 (VITAL, binding, verbatim intent): "the
     representation of the state, e.g., as MPS, or PEPS, or whatever, is NOT
     operationally well defined. What IS operationally well defined
     corresponds to quantities that are observable or implementable. The
     boundary algebra of an MPS does fit this, at least for injective MPS.
     If you cannot describe an experiment with QM that can observe or
     implement it, it is not operationally meaningful."
     Output: theory/lanes/reduction/o1-operational-audit.md, INCREMENTALLY. -->

# O1: operational status of every campaign definition and load-bearing object

## Inputs

- `definitions.md` IN FULL (D1–D31, chunked reads); `notation.md`.
- `theory/corner-a.md` (the A1 endpoint/boundary-algebra results, esp. the
  clause that half-infinite truncated strings act on states exactly as bond
  insertions, and the (b) non-implementability-iff-nonscalar clause — these
  are the operationally decisive statements).
- `refs/arxiv-0802.0447` (LOCAL TeX: string order and symmetries in MPS —
  the operational detection route for the projective class; quote file+line).
- `claims/CLAIMS.md` rows WI, A1, A2, G0, S-IDX-fin-r2, S-IDX-MATCH-HS-SEP,
  M-INDEX-fin/spec, A-INDEX-PEPS, SHAPE-FLAT (statuses unchanged).
- Context (do not repeat, extend): theory/lanes/reduction/q1-gauss.md,
  q2-memory-defs.md, q4-adversarial-defs.md;
  theory/verdicts/reduction-defs-adjudication-r1.md incl. amendment r1a.

## The classification to produce

For EVERY definition D1–D31 and for these claim-level objects — the bond
implementer V(g), the endpoint states ω^{M@b}, the projective class
[ω]∈H²(G,U(1)), the truncated symmetry U_R(g), the modulated charge Q[f],
the TPM protocol and escaped-charge law, the windowed wall coordinate, the
two-magnon physical phase δ_phys, the fixed-time protocol datum (proposed
D29), the excitation-ansatz tensors B and gauge data X, the PEPS typing
hypotheses (PT1)–(PT4), the kink endpoint label of the toric-code row —
assign exactly one status with a one-paragraph justification:

- **OBSERVABLE**: expectation/statistics of a physical observable; name the
  measurement.
- **IMPLEMENTABLE**: a physical operation (unitary/channel/protocol) a QM
  experiment can perform; name the operation, including whether it is
  finite-depth, a quench, or a limit of implementables with a quantitative
  convergence rate (the transfer gap matters here).
- **GAUGE**: representation-level bookkeeping with no direct experiment; then
  state what gauge-invariant/operational content it carries (e.g. its
  equivalence class, or the physical statement it is used to prove) — a
  GAUGE label is not a defect when the object is scaffolding for an
  operational theorem, but the theorem's STATEMENT must then be checkable
  operationally.

## Special mandates

1. **Substantiate TJO's positive claim quantitatively**: the boundary
   algebra of an INJECTIVE MPS is operationally well defined. Assemble the
   three routes with the actual statements: (i) the fundamental theorem —
   the tensor, hence the boundary algebra up to isomorphism, is a functional
   of the STATE (not the representation); (ii) implementability — truncated
   symmetries are finite products of on-site unitaries, and the endpoint
   action is their weak-* limit with exponential rate set by the transfer
   gap (quote the campaign's own proved rate), so it is approximable by
   implementables with quantitative error; (iii) observability — string
   order parameters and endpoint-state tomography on reduced density
   matrices detect the class [ω] and the endpoint data (quote 0802.0447).
   Also state the honest fence: which of these routes fail for
   non-injective MPS and for PEPS (this bears on the conditional
   2+1 rows, whose (PT) hypotheses are representation-level).
2. **The A1(b) dichotomy is the operational crux of corner A**: for
   non-scalar V(g) NO strongly convergent implementing sequence exists —
   reconcile this proved non-implementability with the operational status
   you assign (weak-* implementability at the level of states vs norm
   implementability of an operator; say precisely which operational notion
   survives and which experiment corresponds to it).
3. **Re-anchor list**: every campaign statement whose CONTENT (not merely
   whose proof) depends on representation-level data, with the operational
   restatement it needs or the GAUGE label it should carry. The PEPS
   selection row and the ansatz-conditioned scattering hypotheses are prime
   suspects; the S-matrix conclusions are prime survivors (phases are
   interferometrically observable).
4. Close with a table: object → status → experiment (or gauge content) →
   action needed (none / restate / flag).

## Rules

Physics register; [physical argument]/[textbook] flags; local-TeX quotes
with file+line; statuses in claims/CLAIMS.md unchanged; no edits outside
theory/lanes/reduction/; no bd operations; no LEDGER edits.
