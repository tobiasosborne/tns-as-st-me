<!-- ROLE: L6 proposer repair disposition for M-quant-G, round 1.
     Date: 2026-08-26. -->

# M-quant-G repair r1

Response to `mquant-g-r1.md`: both requested repairs are applied, with the
theorem formula, D18/Mq-E conditional structure, frozen XXZ values, and
CLAIMS/TRIANGLE status wording unchanged.

| Verdict item | Disposition | Repair and evidence |
|---|---|---|
| 1. MAJOR — incompatible bare `U(1)^2` example | **REPAIRED** | Shard §3 now constructs `G=(U(1)^2)\rtimes\mathbb Z_2`, `Q_1=diag(1,-1)`, `Q_2=2I`, the Weyl matrix `r`, `u(\theta,\phi)`, and the rays `\alpha,\beta=r\alpha`.  It verifies the common stabilising torus, density vectors `(1,2),(-1,2)`, and vector conservation.  The adjacent remark records the `Ad` fixed-point obstruction for abelian/central ambient factors.  Checker C2 constructs the same matrices numerically and derives its conservation vectors from their expectations. |
| 2. MINOR — C1 general-`s` quantifier unguarded | **REPAIRED** | C1 evaluates the transmitted quantum, mean, and variance at `s=1` and `s=3/2`, then requires `s` to remain in all three free-symbol sets.  On an isolated copy, replacing C1's symbol by `Rational(1,2)` exits `1` at the `s=1` transmitted-quantum check. |
| 3. NOTE — structural versus arithmetic hypotheses | **NO CHANGE REQUIRED** | The shard already states that distinction and the verdict requested no repair. |

## Verification

All nine files in `theory/checks/*.py` pass under `python3 -O` (9/9, each
exit `0`).  The documented
`python3 -O theory/checks/mquant_general_check.py --red` exits `1` with
transmitted-quantum residue `1/s`.  The isolated `s=1/2` copy mutation also
exits `1`, as recorded above.
