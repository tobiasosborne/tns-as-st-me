<!-- ROLE: L6 critic verdict, round 4 narrow adjudication of the r3 sweep.
     Critic: Codex. Date: 2026-08-26. -->

# Critic verdict r4 — terminal narrow adjudication

I audited the committed tree at `b8040e5`, restricted to the five requested
repairs, the four r3 promotions, SPT-E', and the checker matrix.  Commit-scope
note: `git diff b8040e5~1 b8040e5` contains no source repair; it adds the r3
response ledger and result/beads data.  The source edits themselves entered in
its parent `b981e50`.  This provenance mismatch does not change the tree being
adjudicated.

## Repair adjudication

| item | verdict | independent audit |
|---|---|---|
| N3 residual | RESOLVED | `notation.md:241` now calls `Γ_N(k)` an off-shell analytic interpolation at fixed periodic `N`, matching every active ML4 consumer.  This is forced because the ring momenta are discrete; continuous fixed-`N` variation of `k` cannot be an on-shell soft sequence. |
| R3-N1 | RESOLVED | SPT-E'(iii) and D21 retain only the fixed-tensor congruence and lift-gauge invariance.  The false path-constancy conclusion is absent, and SPT-M' takes a difference of the same fixed-system affine lattice, so the offset cancels without a deformation claim. |
| R3-N2 | RESOLVED | The B3 summary now contains only finite-time label rigidity and `2s·δx+(q_out−q_in)=0`; torsor/flatness is explicitly left to K4.  Section 10 and all DAG surfaces mark the displayed Fano formula and quadratic zero PROVED conditional on Mq-E, while full-chain accuracy is SKETCH and universality is CONJECTURE. |
| R3-N3 | RESOLVED | SPT-E-AKLT is exactly (4.1) and its AKLT-family `-Z/2` limit.  Direct summation gives `−(1−b²)Σ_{n=0}^{L−1}(2b²−1)^nZ=−[1−(2b²−1)^L]Z/2`.  The product residue is now supporting comparison only. |
| R3-N4 | RESOLVED | S-C6 separately inserts the anti-Hermitian one-site generator `-iS^z` through `inserted_transfer`, applies the dual-left compression, and checks `Q=i M` and `-iQ=M` against the independently computed Hermitian compression `M`.  It no longer defines the tested partial charge as `i*measured`. |

## Promotion fidelity

| row | verdict | comparison with the exact corpus-r3 sentence |
|---|---|---|
| SPT-B' | FAITHFUL | Common-gap continuity, continuous/`C^p` external data, H-soft-p for derivative limits, and the need for a separate local-constancy proof are preserved; no topological constancy is inferred. |
| SPT-T' | FAITHFUL | Only the registered identities (5.1)--(5.2) are unconditional; physical use still requires H-split and H-dress, and the second endpoint compensates. |
| SPT-D' | FAITHFUL | The ordered registered product realizes the cocycle; for compact semisimple Lie algebra it is removed only as a coboundary in a chosen phase section.  Physical use retains H-split/H-dress. |
| SPT-M' | FAITHFUL | It is PROVED only as the implication conditional on H-split, H-AD-edge, charge conservation, and definite channel charges.  It uses fixed-tensor congruence and protects module/capacity, not a nonzero amplitude. |

The four promotions agree in `claims/CLAIMS.md`, `theory/TRIANGLE.md`, and the
proof shard.  One stale definitions preamble is recorded below; it does not
strengthen or invalidate a promoted theorem.

## New objection

### R4-N1. MINOR — stale pre-r3 status sentence in the definitions preamble

**Location:** `definitions.md:743-750`.

**Independent audit.**  The preamble still says that “the parent SPT claims
remain SKETCH awaiting critic r3.”  In the adjudicated tree SPT-B', SPT-T',
SPT-D', and the scoped conditional SPT-M' are PROVED in the claim DAG,
TRIANGLE, and their proof shard.  This is a stale summary sentence, not a
mathematical dependency or a second L5 cell.

**Fix demand:** update that preamble to the r3/r4 status ledger: B'/T'/D'/M'
PROVED, E' PROVED per this verdict, and M'-dyn CONJECTURE.

**Surviving statement:** all four r3 promotions and the SPT-E' promotion below
survive with their present hypotheses and scopes.

## SPT-E' decision

**PROMOTE TO PROVED.**  Clause (i) follows from compensated WI telescoping and
the derivative-before-window limit, giving the centered Hermitian residue
`Q_edge=-iX_C^circ`; clause (ii) is the projective-irrep dimension bound;
clause (iii) is now only the valid fixed-tensor shifted-lattice statement plus
lift-gauge invariance; and clause (iv) is the exact geometric contraction
(4.1).  H-split remains explicit for every physical-edge reading.  With the
false deformation-constancy sentence deleted, no missing step remains in the
displayed clauses (i)--(iv).

## Checker audit

All eight checkers passed under `python3 -O`: `corner_a_check.py`,
`crosscheck_corner_b_tk.py`, `ml2_completeness_check.py`, `ml4_check.py`,
`mquant_check.py`, `oracle_bethe_check.py`, `soft_current_recon_check.py`, and
`spt_rebuild_check.py`.  Copies under `/tmp/tns-corpus-r4-checks.YjuhfZ` killed
all four documented red modes with exit `1`: M-quant continuity residue
`2.340e+00`, ML4 false-uniform scaling, SPT sign error `1.333e+00`, and SPT
uncentered-gauge error `3.700e-01`.  No source checker was mutated, no checker
contains a bare Python `assert`, and `git diff --check` passes.

**Fixed-point declaration (freeze-restoration ledger).**  Final active claim-row
statuses touched since r1 are: **PROVED** — WI, A1, A2, G0, S2-2body, ML2,
ML4-A, ML4-Ward, ML5-A, ML5-B, M-flux, B3, SPT-B-mult, SPT-B', SPT-E-AKLT,
SPT-E' (this verdict), SPT-T', SPT-D', SPT-M', OR1, OR2, K1, K2, K3, Mq-AD3
(conditional on Mq-E), M-quant (conditional on D18), and M-tk (conditional on
Mq-E for the displayed graph); **SKETCH** — ML4 and N2; **CONJECTURE** —
S-general, ML1, ML3, ML6, SPT-M'-dyn, N1, K4, Mq-E, and Bc; **REFUTED** —
A2-orbit-r1, G0-soft-r1, S2, unrestricted ML5, the literal M, SPT-B-r1, and
SPT-nogo.  Historical S, SPT-B, SPT-E, SPT-T, SPT-D, and SPT-M rows are
superseded and have no active claim row.  No FATAL or MAJOR objection remains;
R4-N1 is editorial residue only.

PASS
