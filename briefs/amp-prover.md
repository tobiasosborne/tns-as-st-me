# Work order — AMP: prove or refute the soft-leg amputation lemma

You are the prover on claims row **AMP** (claims/CLAIMS.md), the named open
lemma left by the D24(d)3 merge and the last piece of value-content in the
ML5 factorisation: does charge-created soft-leg amputation contribute
`𝔞_leg(ρ) = 1/Z_ρ = 1/(2ρ)` — WITHOUT the jet-identification bridge (α)?

A sharp REFUTATION under the stated hypotheses is worth exactly as much as
a proof (CLAUDE.md L10). A proof that the question is undecidable from the
current definitions — i.e., that D24(b)+(d) leave 𝔞_leg genuinely
unconstrained beyond `≠ 0`, with the obstruction exhibited — is also a
result. What is NOT acceptable is a value produced by a mechanism the fence
below already refutes.

## Process contract (PRD.md — read it first)

ONE hostile critic round after this, then ONE repair, hard stop. Label
every step honestly: PROVED steps get full Lamport justification; gaps get
SKETCH/CONJECTURE in place with the obstruction displayed.

## READ FIRST, in order

1. `PRD.md`, `CLAUDE.md`, `notation.md`, `definitions.md` — especially D24
   in FULL as merged (text of record: theory/verdicts/d24d3-adjudication-r5.md §5;
   definitions.md carries the merged text).
2. `claims/CLAIMS.md` rows AMP, D24-VAL, ML5-B, S2-2body-S — the AMP row
   carries the binding quantitative fence; read every word.
3. `theory/verdicts/d24d3-adjudication-r3.md` ⟨1⟩4 and
   `-r4.md` §1.3 (the one-step leg-conversion computation).
4. `theory/checks/d24d3_normalization_check.py` — run it; understand
   D24N-C6, C8 and the `--red-halfpower` mode before writing anything.
5. `theory/spin-s-twomagnon.md` (the S2-2body-S shard — mind the ρ-vs-file-
   local-ρ trap flagged in the D24-VAL row).

## THE FENCE (binding; from the AMP row and D24N-C8)

- The leg-conversion factor is computed EXACTLY: `Q^-_k|Ω⟩ = √Z_ρ |k⟩`
  (D24N-C8), so a leg normalisation ALONE supplies only `Z_ρ^{-1/2}`, and
  that value is refuted against ansatz-free data at 5.2–12.5× margins
  (under the two named hypotheses in the AMP row, neither proved).
- AMP is therefore true only if a SECOND factor `Z_ρ^{-1/2}` arises from a
  mechanism that is NOT a leg normalisation. Any proposed proof must be
  checked against D24N-C8 or it double-counts the leg. Name your second
  mechanism explicitly and display why it is not a renaming of the leg.
- Candidate mechanisms to examine (not exhaustive; finding the right one is
  the task): the descendant-projection step in D24(d) clause 1 (the
  charge-created reading of `E^O_desc`); the windowed-charge smearing
  measure; the D24(b) two-anchor amputation convention itself (does fixing
  the convention force a Jacobian?); the finite-N `√(Z_ρ − 2/N)` mismatch
  and its LSZ limit.
- Statable only relative to D24(b)'s convention — if your argument ever
  needs a different normalisation, it is proving a different statement.

## LANE (writable; NOTHING else)

- `theory/amp.md` (CREATE — Lamport L6b shard)
- `theory/checks/amp_check.py` (CREATE — see below)
- `theory/amp-notes.md` (CREATE, optional)

Do NOT edit claims/CLAIMS.md, definitions.md, notation.md, any existing
file. CLAIMS-row updates go in a MERGE PROPOSALS section at the end of your
shard. No commits.

## Checker spec

- `python3 -O theory/checks/amp_check.py` exits 0 green; no bare asserts.
- Whatever your verdict, the checker must contain a computation that would
  CATCH the double-count: verify your claimed 𝔞_leg against D24N-C8's exact
  leg factor and fail (exit 1, registered red mode) if the proposed
  mechanism reduces to a pure leg rescaling.
- If you refute: encode the refutation as a red-capable computation with
  the pre-registered band displayed.

## Deliverable shape

`theory/amp.md`: (0) status header — PROVE or REFUTE or OBSTRUCTION, stated
in the first ten lines; (1) setup citing D-numbers only; (2) the Lamport
ladder; (3) the D24N-C8 double-count check, displayed; (4) checker section
(what each gate certifies and what it does not); (5) MERGE PROPOSALS.

Write each section to the file as you complete it — do not draft everything
before the first Write.
