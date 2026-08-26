<!-- ROLE: L6 critic verdict, round 2, on the repaired M-quant-G row.
     Critic: Codex. Date: 2026-08-26. -->

# Critic verdict r2 — M-quant-G

Critic: Codex, adversarial round-2 adjudication under the supplied promotion
brief.  I treated `theory/verdicts/mquant-g-r1.md` as my prior verdict and
audited only its objection 1, objection 2 and checker minors, the repair diff,
and the resulting promotion scope.  Both requested repairs survive direct
recomputation.

**Decision:** **PROMOTE** the M-quant-G row as a conditional theorem.  The new
semidirect-product example is a genuine H-MQG(1--2) instantiation, the checker
guards the general-`s` certificate, and the repair introduces no strengthening
of the already-audited theorem or its dependencies.

## 1. Objection 1 — repaired semidirect-product instantiation

Set

`Q_1=diag(1,-1)`, `Q_2=2I`, `r=[[0,1],[1,0]]`,
`alpha=(1,0)^T`, and `beta=r alpha=(0,1)^T`.  Direct exact multiplication gives

`r^dagger Q_1 r=diag(-1,1)=-Q_1`,
`r^dagger Q_2 r=Q_2`, and `r^2=I`.

Moreover,

`u(theta,phi)=diag(exp(i(theta+2phi)),exp(i(-theta+2phi)))`

satisfies

`r u(theta,phi) r=u(-theta,phi)`.

Thus the matrices represent the stated compact
`(U(1)^2) semidirect Z_2`, with the Weyl element reversing the first circle
and preserving the spectator circle.  The torus acts on the two rays by

`u(theta,phi) alpha=exp(i(theta+2phi)) alpha`,
`u(theta,phi) beta=exp(i(-theta+2phi)) beta`.

Consequently the same full torus lies in both ray stabilisers.  Its exact
vacuum-density vectors are

`(<alpha|Q_1|alpha>,<alpha|Q_2|alpha>)=(1,2)` and
`(<beta|Q_1|beta>,<beta|Q_2|beta>)=(-1,2)`.

The selected `Q_1` direction therefore has `(+s,-s)` with `s=1`, while `Q_2`
is unchanged.  Since the torus fixes each ray projectively and `r` swaps the
two distinct rays, their orbit is a covariant family of `chi=1` injective
product-MPS vacua.  This supplies the group/vacuum content of H-MQG(1--2);
the shard correctly does not infer H-AD-G for the example.

The abelian-exclusion remark is also correct.  Covariance for
`beta=g·alpha` gives

`omega_beta(Q_xi)=omega_alpha(Q_{Ad_{g^{-1}} xi})`.

For an abelian ambient group, or an Ad-fixed selected central direction,
`Ad_{g^{-1}}xi=xi`; hence the two expectations are equal and cannot be
`(+s,-s)` for `s>0`.  This is exactly the fixed-point obstruction stated in
round 1.

## 2. Objection 2 and checker minors

The required runs gave:

| check | exit | result |
|---|---:|---|
| `python3 -O theory/checks/mquant_general_check.py` | 0 | printed the general `-1/s`, semidirect-product `-1`, zero spectator change, frozen XXZ values, and `PASS` |
| `python3 -O theory/checks/mquant_general_check.py --red` | 1 | `FAIL: transmitted quantum is not -1/s: residue=1/s` |
| isolated copy with C1's `s` replaced by `Rational(1,2)` | 1 | `FAIL: C1 transmitted quantum at s=1: residue=-1` |

C1 evaluates the quantum, mean, and variance at `s=1,3/2` and separately
requires the positive symbol `s` to remain in all three free-symbol sets.  The
round-1 hard-code survivor is therefore killed.

C2 no longer assumes formal vectors.  It constructs numerical matrices for
`Q_1,Q_2,r,u(theta,phi)`, constructs `alpha` and `beta=r alpha`, checks
unitarity, the Weyl conjugations, the semidirect relation and common ray
stabilisation, and derives both density/charge vectors from matrix
expectations before testing vector conservation.  The exact computation in
§1 independently verifies the parameter-general identities behind C2's
sampled numerical check.

## 3. No-silent-strengthening audit

Against the round-1-audited statement at `0fdcc7e`, the shard diff is confined
to §3's replacement of the invalid bare-torus example and §5's accurate C1/C2
checker description.  The theorem hypotheses, (G.1)--(G.2), the general
`-nu/(2s)` clause, D18/H-AD-G conditionality, limit order, and all limitation
boxes are unchanged.  The XXZ instantiation, its frozen values, the Mq-E-only
projected implication, and the explicit statement that full-chain D18 remains
a hypothesis are unchanged.  `claims/CLAIMS.md` and `theory/TRIANGLE.md` have
an empty diff against that baseline, so their SKETCH/pending-critic wording
has not been silently promoted ahead of this verdict.

## 4. Promotion decision

**PROMOTE M-quant-G.**  Exact scoping sentence to copy into the DAG:

> `M-quant-G` is **PROVED only as the conditional implication** H-MQG(1--4) + H-AD-G (exactly D18(AD1--AD4) for the fixed packet, with `q_in=q_L=-1`, `q_T=+1`, no other propagating channel, and no bound-state component) implies (G.1)--(G.2); H-AD-G itself, Mq-E, full-chain D18, any soft zero, and all packet/model/soft-limit uniformity remain unproved.

No missing step remains on the audited conditional argument.

PASS
