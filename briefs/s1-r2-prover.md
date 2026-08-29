# Work order — soft-index r2: the ONE unified S1 shard (bd tns-v44)

You are the prover for the campaign's north-star theorem: the lattice soft
theorem as a symmetry constraint on limit points of the charge-created,
windowed, packet-smeared protocol datum. Both r1 lanes (S1-A, S1-B) FAILED
with FATALs, but the LAW survived every falsification attempt. Your job is
the r2 shard that supersedes both lanes, built to the adjudicated design.
This is a PROVE task, not a survey: deliver a complete Lamport L6b proof
ladder, honest about every gap.

## Process contract (PRD.md — read it first, it supersedes older habits)

- You get ONE hostile critic round after this, then ONE repair. There is no
  fixed-point iteration. Anything you cannot prove, label SKETCH or
  CONJECTURE in place with the obstruction stated — a wrong label is the
  only fatal sin; an honest SKETCH is a legitimate deliverable.
- Every leaf justified by a D-number, a claim id (claims/CLAIMS.md), or a
  named computation. No leaf cites folklore or memory.

## READ FIRST, in order

1. `PRD.md`, `CLAUDE.md` (laws), `notation.md`, `definitions.md`.
2. `theory/verdicts/soft-index-adjudication-r1.md` IN FULL — §3 (binding
   design) and §4 (r2 work order), INCLUDING the ORCHESTRATOR ERRATUM
   prepended to it (it corrects §3.7; the erratum wins).
3. `theory/verdicts/ml4-ward-n2-audit.md` — §2.3–2.4 list the 15 damaged
   statement sites your shard absorbs.
4. `claims/CLAIMS.md` rows: S2-2body-S (PROVED — your value supplier),
   ML5-B, D24-VAL, AMP, ML4-Ward (scoped, ERRATUM), AC-EX-2M.
5. `definitions.md` D24 (as merged by d24d3-adjudication-r5.md §5), D25,
   D26–D28, D31.
6. Lane records `theory/soft-index.md` (S1-A) and `theory/soft-index-b.md`
   (S1-B) — you supersede them; do NOT edit them.
7. `theory/checks/soft_index_probe.py` (the passed falsifier; its P2(b)
   η-gate is a known no-op, bd tns-9z4 — quote it as P1+P2(a)-only) and
   `theory/checks/ml4_ward_n2_check.py` (the register-trap certificate).

## LANE (writable; NOTHING else)

- `theory/soft-index-r2.md` (CREATE — the unified shard)
- `theory/checks/soft_index_r2_check.py` (CREATE — checker per spec below)
- `theory/soft-index-r2-notes.md` (CREATE, optional — working notes)

Do NOT edit: claims/CLAIMS.md, definitions.md, notation.md, any existing
theory/ file, the frozen probe. Any D29/D30 text you need goes in a MERGE
PROPOSALS section at the end of your shard — the orchestrator merges. No
commits (your sandbox cannot commit; the orchestrator owns git).

## BINDING DESIGN (adjudicated; deviations need a displayed justification)

1. **Ladder:** S-IDX-fin (unconditional finite-volume index identity) →
   S-IDX-spec (every subsequential limit of the windowed, packet-smeared,
   charge-created protocol datum obeys the soft law, under D29 PROTO + D30
   TGT) → instances from PROVED ansatz bands.
2. **D29 = lane B's** (concrete, probe-computable clauses), carrying **lane
   A's ℓ_h / m_λ registers**.
3. **The corrected Ward identity MUST NAME ITS REGISTER.** Either
   full-sector: `P_{n,N} J^-_0 = 2 D_{n,N} A_n^{-1} J^z_0` with
   `A_n = D†D` on ALL of `H_{n,N}`; or highest-weight-restricted:
   `(1/m_λ) Q_0 Π_hw J^z_0`, `m_λ = (N−2n)/2`. NEVER "over m_λ with the
   2DA^{-1} form" — that hybrid IS the refuted second display of ML4-Ward
   (9), certified identical at 0.00e+00 by ml4_ward_n2_check.py row C5.
   The adjudication §3.7 literally instructs the hybrid; the ERRATUM
   corrects it. Follow the erratum.
4. **Adler anchor:** the Q_0-created-state computation (exactly 1), stated
   for the object it is actually true of. The r1 (B6) anchor is dead: it
   fails S≥1 and is a readout tautology at S=1/2.
5. **The slope VALUE comes from on-shell matching to PROVED S2-2body-S**
   (`∂_{k_s}δ_phys|_0 = sgn(v_h−v_s)/S`, claims row S2-2body-S). Value
   from stipulation inside D29(5) is DEAD: it was proved constructively
   that no regularity-only (TGT) can pin the jet. Structure from symmetry,
   value from on-shell data — that is the campaign's spine.
6. **𝔞_leg discipline (riders from tns-iu5, all load-bearing):**
   (i) display `𝔞_leg(ρ)` as the OPEN constant of D24(d)3b; cite D24-VAL
   for the conditional matched value and AMP for the conjecture;
   (ii) NEVER describe 𝔞_leg as derivable;
   (iii) NEVER produce its value by a leg-normalisation mechanism — that
   supplies only `Z_ρ^{-1/2}` (D24N-C8) and is refuted at 5.2–12.5×;
   (iv) NEVER assume clause (d)2's residue and `E^O_desc` share a
   normalisation — D24(d)2 displays that they differ by `√Z_ρ` in the LSZ
   limit (`√(Z_ρ − 2/N)` at finite N, q ≠ h).
7. **Absorb the 15 damaged sites** enumerated in ml4-ward-n2-audit.md
   §2.3–2.4: every statement your shard inherits from the lane records must
   appear in corrected form; add a table mapping each damaged site to where
   your shard states the corrected version.

## Checker spec (theory/checks/soft_index_r2_check.py)

- Green: exit 0 under `python3 -O`; no bare asserts.
- MUST fold in ml4_ward_n2_check.py's register trap as a standing red
  test — the r1 checker specs (SIDX-C1 / SIB-C0–C3) would not have caught
  F1; yours must.
- At least one red mode per load-bearing numerical identity in the shard,
  each exiting 1 via a registered mutation that a real defect would
  produce. Red-green: state in the shard's checker section what each gate
  certifies and — explicitly — what it does not.

## Deliverable shape

`theory/soft-index-r2.md`: Lamport L6b throughout (⟨1⟩n steps, explicit
ASSUME/PROVE, terminal QED per level). Sections: (0) status header + what
supersedes what; (1) definitions used (cite D-numbers only — redefine
NOTHING); (2) S-IDX-fin with full proof; (3) S-IDX-spec with full proof or
honest SKETCH per step; (4) the Ward/Adler/S2-matching interfaces; (5) the
damaged-site correction table; (6) checker section; (7) MERGE PROPOSALS
(D29/D30 final text + proposed CLAIMS rows with statuses you can defend).

Work section by section; write each section to the file as you complete it
(do not draft the whole proof before writing — sessions have died that way).
