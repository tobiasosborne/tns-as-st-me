<!-- ROLE: L6 critic verdict, round 1, on M-quant-G.
     Critic: Codex. Date: 2026-08-26. -->

# Critic verdict r1 — M-quant-G

Critic: Codex, adversarial review under L6/L6b/L10.  I treated
`theory/verdicts/corpus-r4.md` as the adjudicated ledger and did not reopen any
converged row.  I audited the new shard, its checker, the M-quant-G DAG row,
and both references in `TRIANGLE.md` §3/§7; re-derived the charge law and XXZ
numbers; ran the checker under `python3 -O`; and mutation-tested copies under
`/tmp/tns-mquant-g-r1.sIArBm` only.

**Decision:** **HOLD** the M-quant-G row.  The conditional two-channel theorem
itself survives: accepting H-MQG(1--4) and H-AD-G, the trusted B3 bookkeeping
and D18 channel projection give (G.1)--(G.2).  There is no hidden
`k=Theta(1/N)` uniformity claim, no proof of H-AD-G, and no upgrade of Mq-E or
full-chain D18.  The hold is caused by one independent scope error: the
advertised `U(1)^2` example/check is not an instance of H-MQG when the torus is
the full group or a central direct factor.  A small checker-quantifier guard is
also missing.

## Independent computations

### Charge orientation, centering, and the channel law

For a cut `c` and `W=[a,b]`, define the physical Hermitian charge with the two
vacuum densities subtracted on their respective sides.  Directly,

`Q_W^c = sum_{x=a}^c(S_x^z-s) + sum_{x=c+1}^b(S_x^z+s)`

has scalar term

`-s(c-a+1)+s(b-c)=s(a+b-1-2c)`.

Expanding D13(a) gives the same operator,

`Q_W^c=2s(X_W-c)`.

Thus conservation between separated in/out channels gives

`2s delta x + (q_out-q_in)=0`,

not its sign reverse.  Reflection has `q_out=q_in=-1`, hence `delta x_R=0`.
Transmission has `q_in=-1`, `q_out=+1`, hence
`delta x_T=-2/(2s)=-1/s`.  A common additive offset cancels between each leg
and its supporting vacuum; multiplying D10's anti-Hermitian generator by
`-i` gives exactly this Hermitian convention.  Rescaling the generator
rescales both `2s` and `q_out-q_in`, leaving
`-(q_out-q_in)/(2s)` invariant.  The sign and centering conventions in the
shard, DAG, and TRIANGLE therefore agree.

On the two outgoing channels, D18(AD2) makes
`N_T=W_+P_TW_+^*` an orthogonal projection.  Hence

`Delta X=-(1/s)N_T`,
`spec(Delta X) subset {0,-1/s}`, and
`Var(Delta X)=s^{-2}p(1-p)` with `p=<N_T>`.

This is the same projection calculation already adjudicated for concrete
M-quant, now with the branch charges made hypotheses.  It is a statement
about `Var(Delta X)`, not the one-time variance of `X_W`; all three active
surfaces preserve that distinction.

### Nonabelian and multi-circle arithmetic

For the `SU(2)` north/south pair, take
`S^z=sigma_z/2` and `g=-i sigma_x`.  Then
`g^dagger S^z g=-S^z`, `g|up>=-i|down>`, and the two vacuum densities are
`+1/2,-1/2`.  The common diagonal circle stabilises both rays.  With the
stated leg charges, the result is therefore `delta x_T=-2`.  This is a legal
nonabelian H-MQG charge register.

For several conserved circles the full conservation equation is vectorial:

`Delta rho * delta x + (q_out-q_in)=0`.

The checker's formal data `Delta rho=(2s,0)` and
`q_out-q_in=(2,0)` correctly give `delta x=-1/s` and zero spectator change.
What fails is its presentation as a bare-torus H-MQG instance; objection 1
below gives the covariance obstruction.

### XXZ instantiation

At `s=1/2`, the general result gives

`Delta X=-2N_T`, `delta x=-2p`,
`spec(Delta X) subset {0,-2}`, and `Var(Delta X)=4p(1-p)`.

Also, the already-frozen Fano expression has
`T(k)=16(Delta-1)^2 k^2+O(k^4)`, so the optional projected soft-memory shadow
is `delta x(k)=-32(Delta-1)^2 k^2+O(k^4)`.  These reproduce M-quant
(Mq.2), (Mq.8), and (Mq.10) exactly.  The instantiation explicitly leaves
Mq-E CONJECTURE and full-chain D18 assumed.

## Hypothesis, limit, and dependency audit

H-AD-G is textually exactly D18(AD1--AD4) plus the charge triple and the
absence of an extra/bound channel for the selected vector.  The other inputs
used by the proof are separately exposed as H-MQG(1--4): the fixed sector,
vacuum density jump, finite-range conserved current, D17 packet, and D13(a)
coordinate.  The load-bearing event identity is also active claim B3, which
the r4 instruction requires treating as a trusted leaf in precisely this
D18-separated scope.

The limit order is explicit and sufficient for that conditional scope:
infinite volume and wave operators, then large time at fixed `W`, then
`W` increasing to the chain.  D17 supplies only state-specific `l1` tails;
the shard claims no rate or uniformity.  Its optional exponential estimate is
restricted to one fixed D1(e') decoration and fixed tensors.  In particular,
the theorem excludes plane waves and makes no statement along
`k=Theta(1/N)`.  I found no volume-uniform strengthening to attack.

The shard, CLAIMS row, and TRIANGLE §3.2/§7 are in lockstep: M-quant-G is
SKETCH pending this critic; `(T)` is optional and used only for the D9(d)
double coset; H-AD-G is not derived; and no soft zero, Mq-E, or full-chain
claim is promoted.  Every proof leaf cites an active r4 claim, a D-number, a
prior hierarchical step, or a displayed finite computation.  There is no
Bethe or integrability leaf.

## Checker and mutation audit

The optimized green run exited `0` and printed the exact general, SU(2),
torus-vector, and XXZ arithmetic.  The documented `--red` mutation changed
`q_T` to `-1`, exited `1`, and reported residue `1/s`.  The checker contains
no bare Python `assert`, and direct optimized compilation succeeded.

On copies only, three local mutants were killed:

| copy mutation | exit | observed failure |
|---|---:|---|
| reverse the sign in `displacement` | 1 | transmitted residue `2/s` |
| move the D13 origin from `a-1` to `a` | 1 | window residue `-2s` |
| change the XXZ soft coefficient `16` to `8` | 1 | residue `16(Delta-1)^2` |

A fourth mutation, replacing C1's symbolic positive `s` by the hard-coded
`s=1/2`, still exited `0` and printed `PASS`.  That surviving mutation is
objection 2.  None of these computations constructs MPS tensors, wave
operators, or H-AD-G; the shard and DAG honestly say so.

## Numbered objections

### 1. MAJOR — the advertised `U(1)^2` instantiation is incompatible with the covariant vacuum-pair hypotheses

**Attacked steps:** `memory-quantization-general.md` §3, especially the claim
that “a torus such as `U(1)^2`” satisfies the group-theoretic example;
§5's description of MqG-check C2; and
`mquant_general_check.py` `check_rank_two_abelian_factor`.

**Exact failed step.**  H-MQG(1) requires `beta=g·alpha`, while H-MQG(2)
requires a common selected generator with vacuum densities `(+s,-s)`,
`s>0`.  D2(a) covariance gives, for the Hermitian generator `Q=-iq(xi)`,

`omega_beta(Q)=omega_alpha(u(g)^dagger Q u(g))
              =omega_alpha(Q(Ad_{g^{-1}} xi))`.

If `G` is abelian, or if the selected torus is a central direct factor, then
`Ad_{g^{-1}}xi=xi`.  Therefore
`omega_beta(Q)=omega_alpha(Q)=+s`, contradicting the required `-s`.
Equivalently, an abelian symmetry element cannot move a state along its orbit
while reversing the expectation of a generator with which it commutes.

**Independent computation.**  For a diagonal two-circle representation,
direct matrix multiplication gives `u^dagger Q_1 u-Q_1=0` and zero orbit
charge difference.  The checker's lines setting
`vacuum_jump=(2s,0)`, `q_in=(-1,2)`, and `q_out=(1,2)` merely assume a formal
conservation vector; they construct no `g`, vacua, or representation satisfying
H-MQG(1--2).  By contrast, adjoining a noncommuting element
`r=-i sigma_x` gives `r^dagger Q_1 r=-Q_1` while preserving a spectator
`Q_2=2I`.  That is a semidirect/normalizer example, not bare `U(1)^2` or a
central abelian factor.

**Fix demand.**  Either delete the torus language and call C2 only a formal
rank-two conservation check, or replace it by an actual compact ambient group
such as `(U(1)^2) semidirect Z_2` (or a nonabelian group with a Weyl element),
construct `u`, `g`, `alpha`, and `beta`, verify the common torus and the
`(+s,-s)` density jump, and then check both charge components.  State
explicitly that a purely abelian `G`/central abelian factor cannot realise the
nonzero jump for two vacua in one `G`-orbit.

**Surviving statement.**  The componentwise vector conservation arithmetic is
correct, and the scalar M-quant-G implication survives for every *compatible*
covariant pair.  The `SU(2)` and XXZ examples are compatible.  This objection
does not produce a counterexample satisfying H-MQG; it shows that one claimed
example never satisfies its hypotheses.

### 2. MINOR — the checker does not guard its advertised general-`s` quantifier

**Attacked steps:** `memory-quantization-general.md` §5's statement that C1 is
the symbolic general-`s` subtraction and
`mquant_general_check.py` `check_general_arithmetic`.

**Exact failed step.**  On a copy, changing only
`s=Symbol(..., positive=True, nonzero=True)` to `s=Rational(1,2)` left every
internal equality green, exited `0`, and still printed
“PASS: M-quant-G symbolic charge arithmetic”.  The checker therefore guards
the formula at its current source value but does not guard that C1 still
quantifies over symbolic `s`; an XXZ-only shadow can masquerade as the general
certificate.

**Independent computation.**  The unmutated source genuinely returns
`-1/s` and `-T/s`, so this is a mutation-coverage defect, not evidence against
the theorem.

**Fix demand.**  Add an explicit domain guard, for example require that the
positive symbol `s` remains in the free-symbol set of the transmitted and mean
expressions, and make the success message conditional on that guard.  A
symbolic `nu` check of `delta x=-nu/(2s)` would also cover the theorem's stated
general-charge corollary.

**Surviving statement.**  The present source performs correct SymPy algebra
for symbolic `s`, and the documented charge-sign red mode is effective.

### 3. NOTE — the MPS hypotheses are structural context, not a minimal arithmetic basis

**Attacked steps:** H-MQG(1) and §1's “what replaces product vacuum” list.

**Exact audit.**  Compactness, covariance, injectivity, common finite `chi`,
and the A2 half-string construction establish the requested MPS setting and a
nonempty fixed kink sector.  Once that sector, D13/D17, conserved charge, and
D18 channels are assumed, steps ⟨1⟩3--⟨1⟩5 do not use injectivity or `chi`.
Translation invariance is also stronger than the local conservation arithmetic
strictly needs.  The shard says this explicitly at §1, so there is no hidden
minimality claim and no logical defect.

**Fix demand.**  None is required for correctness.  If “general memory law” is
intended to mean a hypothesis-minimal result, split out a charge-bookkeeping
lemma for stationary tails plus D13/D17/D18 and state the injective-MPS theorem
as its structural corollary.

**Surviving statement.**  Arbitrary finite bond dimension introduces no extra
term into the charge law; the proof never uses `chi=1` or an MPS-uniform tail
rate.

## Promotion decision

**HOLD M-quant-G.**  Repair objection 1 before promotion.  No change is needed
to the formula, D18/Mq-E conditional structure, XXZ numbers, or the
CLAIMS/TRIANGLE status wording.  After replacing or honestly relabelling the
torus example and adding the minor C1 domain guard, the surviving conditional
theorem is promotion-ready on the audited argument.

FAIL(1)
