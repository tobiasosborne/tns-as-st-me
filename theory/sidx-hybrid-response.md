# General-`G` hybrid repair response

This is the response record for the single repair wave ordered by
`theory/verdicts/sidx-general-g-joint-critic.md` under bd `tns-fea`.

## Narrow choices at ambiguous sites

1. The critic's step 1 names `theory/soft-index-g-hybrid.md`, while the work
   order's deliverable 1 explicitly names `theory/soft-index-general.md`.
   Exactly one hybrid was created, at the work-order path.  No
   `soft-index-g-hybrid.md` alias was created.
2. The two CLAIMS rows were required verbatim.  Their original
   `theory/soft-index-g-hybrid.md` strings were therefore retained even though
   the delivered shard has the work-order filename.  No authoritative CLAIMS
   row was edited.
3. Step 8's request for the shared calculation in the hybrid check table was
   read as requiring an executable green gate because the specified numbers
   were not jointly checked by one existing gate.  SIDXG-C6 was added to the
   existing G1 checker by reusing the existing G4 helpers; no mutation mode
   was added.
4. Lane-record edits were limited to explicit replacement/restatement orders:
   G1 received steps 2--3, G2 received step 5, and G4 received no edit because
   step 7 orders import/restatement in the hybrid rather than replacement in
   the lane record.

## Repair-order accounting

| step | disposition | location |
|---:|---|---|
| 1 | Created the single hybrid and stated that it supersedes all four lane/boundary shards for citation while leaving them as records. | `theory/soft-index-general.md` header; filename choice recorded above |
| 2 | Retained root normalization, positivity, polar projection, Ward contraction, and both operator registers.  Made displayed current covariance the hypothesis and D10 periodization only an example. | hybrid §§0--1; minimal current-register restatement in `theory/soft-index-g.md` ⟨1⟩1 and its proposal row |
| 3 | Replaced canonical irreducible-copy language by `bigoplus_tau I_{V_tau} tensor B_tau`, with explicit equivalent-copy and cross-`n` mixing. | hybrid §1.3; minimal restatement in `theory/soft-index-g.md` ⟨1⟩4 and its proposal row |
| 4 | Inserted G2.BLOCK as typed supporting algebra with `d:M_dom->M_out`, `A=d^dagger d`, `r=d^dagger j`, `B=A^+r` on `M_dom`; displayed global `K` covariance before Schur orthogonality, including disconnected `K`. | hybrid §2 |
| 5 | Replaced the scalar/rank-one boundary with (C-SCAL), stated the injective and selected-vector forms, and kept the normalized index-one proof unchanged.  One-dimensional nonzero source is sufficient, not necessary. | hybrid §§1.2, 2; `theory/soft-index-g2.md` introduction, ⟨1⟩2, ⟨1⟩10, and affected proposal prose |
| 6 | Chose the compact root circle in the G1/G2 dictionary.  Restricted a full-`H_alpha` line formula to line-preserving cases; otherwise used the whole broken module `W` or conjugate-root transport. | hybrid §3 |
| 7 | Imported the effective-centre affine torsor, common charge/current shift, cocharacter integrality, finite torsion, trivial-character case, pure-zero-mode anchor, and strict projector fence with displayed global current covariance.  Credited ED only for strict inclusion/replacement defect and G4.19 for underdetermination. | hybrid §4 |
| 8 | Added the shared SU(3) table with `lambda=3`, `spec A={3^4}`, mismatch `6.94e-16`, coefficient `2i/3`, denominator `2i`, and index error `1.22e-17`, all verbatim.  Reused the checker suite and added green-only SIDXG-C6; no mutation mode was added. | hybrid §5.2--§5.3; `theory/checks/soft_index_g_check.py` SIDXG-C6 |
| 9 | Ended the hybrid with G5 exclusion pointers and exactly the two verbatim CLAIMS rows.  Added no third G2 headline, scalar per-root row, finite-group soft row, or G3 strengthening. | hybrid §§6--7 |

## Objection dispositions

| objection | severity | disposition |
|---|---|---|
| G1-O1 | MINOR | Repaired.  Both hybrid and G1 now say canonical centralizer-isotypic summands, display `bigoplus_tau I_{V_tau} tensor B_tau`, and permit equivalent-copy/cross-`n` mixing. |
| G1-O2 | MINOR | Repaired.  Displayed current covariance is the theorem hypothesis; a chosen periodized D10 realization is only an example. |
| G1-O3 | NOTE | Retained.  Weyl transport preserves phases, projectors, singular values, and residuals without simultaneous diagonalization. |
| G2-O1 | MAJOR | Repaired.  The coefficient is `B=A^+r` on the source multiplicity register and the exact criterion is `dA^+r=cd`; rank one is neither necessary nor sufficient in general. |
| G2-O2 | MINOR | Repaired in the hybrid overlap.  G2.FULL uses the root circle; full `H_alpha` uses a line only when it preserves it, otherwise `W` or root transport is used. |
| G2-O3 | MAJOR | Repaired in the supporting lemma.  Global `K` covariance is displayed before Schur orthogonality, so disconnected elements are not inferred from infinitesimal covariance. |
| G2-O4 | NOTE | Retained unchanged mathematically.  The direct Ward contraction proves normalized index one without scalarity or rank hypotheses. |
| G4-O1 | NOTE | Retained.  The common sector shift, affine-offset cancellation, connected cocharacter integrality, and possible finite torsion are stated as representation-covariance consequences. |
| G4-O2 | MINOR | Repaired by attribution.  The `8<24` ED count and outside norm prove strict projector fineness/live replacement defect; abstract witness G4.19 proves underdetermination from labels alone. |
| G4-O3 | MINOR | Repaired in the hybrid theorem register.  Global finite-ring current covariance is assumed explicitly and D10 periodization is only an example. |

## Mechanical verification

| command family | result |
|---|---|
| `python3 -O theory/checks/soft_index_g_check.py` | exit `0`; SIDXG-C0--C6 pass; C6 reports mismatch `6.94e-16`, coefficient `2i/3`, denominator `2i`, index `1-1.2234898622556949e-17i`, Ward residual `3.85e-17` |
| four existing `soft_index_g_check.py --red-*` modes | each exits `1` at its intended SIDXG-C3 or C5 gate |
| `soft_index_g2_check.py` green / `--red-scalar-gram` | exits `0` / `1` |
| `soft_index_g4_check.py` green / two existing red modes | exits `0` / `1`, `1` |
| `soft_index_g_boundary_check.py` | exit `0`; G5-C1--C5 pass |
| `soft_index_r2_check.py` | exit `0`; SIDXR2-C0--C8 pass |
| proposal-row byte comparison | both critic CLAIMS rows occur verbatim in the hybrid |
| `python3 -m py_compile` and diff whitespace checks | pass |

## Scope audit

No edit was made to `claims/CLAIMS.md`, `definitions.md`, `notation.md`,
`theory/soft-index-r2.md`, `theory/soft-index-g-boundary.md`, any verdict, or
`theory/soft-index-g4.md`.  No new claim class or mutation mode was introduced.
