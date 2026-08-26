<!-- ROLE: L6 critic verdict, round 1, on M-quant + ML4 + ML5.
     Critic: Codex. Date: 2026-08-26. -->

# Critic verdict r1 — M-quant, M-flux, ML4, and ML5

Critic: Codex, adversarial review under L6/L6b/L10.  I read the governing
definitions and claims first, re-derived the six requested computations, audited
the limit orders and source/model quantifiers, ran all relevant checkers under
`python3 -O`, and mutation-tested copies under `/tmp` only.  The exact finite-time
flux identity, the conditional charge arithmetic, the projection-spectrum
calculation, the rank-two Kato--Rosenblum application *after accepting the Fano
reduction*, and the four-site `O_eta` coefficient all survive.  The package does
not.

The two decisive failures are independent.  ML4's claimed volume-uniform `C^1`
trace bound is false in the joint soft/thermodynamic scaling `k=2 pi/N`; its
checker samples only the fixed-volume Taylor regime.  ML5-A's advertised iff is
false because a vanishing first jet does not force the missing soft intercept to
vanish.  M-quant additionally uses a new spectral definition of H-AD that is not
D18, while the claimed unconditional projected theorem rests on an all-volume
sector-graph reduction for which the cited source contains only one finite
enumeration.

## Independent recomputations

### Kato--Rosenblum and the Fano resolvent

Accepting `memory-quantization.md` ⟨1⟩1.⟨2⟩1--⟨2⟩2, put

`V = H_3-H_0 = -(J/2)(|0><d|+|d><0|)`.

Both `H_0` and `H_3` are bounded self-adjoint operators on
`ell^2(Z) direct-sum C`.  On `span{|0>,|d>}`, `V` has eigenvalues `+/-J/2`,
so it has rank two and trace norm `||V||_1=J`.  No relative trace-class
hypothesis is needed: the perturbation itself is trace class.  Kato--Rosenblum
therefore gives the wave operators for `(H_3,H_0)` with initial space
`H_ac(H_0)=ell^2(Z)` and range `H_ac(H_3)`.  The decoupled `|d>` level belongs
to the pure-point part of `H_0`, not to the channel initial space.

For the full-line free chain,

`m_0(z)=<0|(z-E_c+(J/2)(T+T*))^{-1}|0>
       =((z-E_c)^2-J^2)^(-1/2)`

with the resolvent branch.  Feshbach reduction gives
`z-E_d-(J^2/4)m_0(z)`.  In the open band the boundary value of `m_0` has
nonzero imaginary part, so this denominator has no embedded real zero.
Outside the band its zeros are isolated and finite; threshold solutions are
constant/linear, possibly alternating, and not in `ell^2`.  Thus the stated
Fano operator has no singular-continuous part.  This validates
⟨1⟩2--⟨1⟩3 *conditional on the graph identification*.  It does not prove that
identification, does not turn D18 into the spectral AD1--AD4 of the shard, and
does not establish full-chain H-AD.

### Flux identity

From D13(a), constants drop out and D10(b) gives

`d X_W/dt = (1/(2s)) sum_{x=a}^b (j_{x-1|x}-j_{x|x+1})
           = (1/(2s))(j_{a-1|a}-j_{b|b+1})`.

Integrating over a finite interval proves (Mq.4), and evaluating the
finite-time Fourier transform at frequency zero gives the displayed DC form.
No asymptotic or integrability hypothesis occurs.  Mq-flux
⟨1⟩1--⟨1⟩4 survives.

### Charge arithmetic and `spec(Delta X)`

A kink at bond `m` has regularised charge `2s(m-c)`.  Reflection preserves the
leg charge `-1`, hence `m_R=m_i`.  Transmission changes the leg charge from
`-1` to `+1`; conservation gives
`2s(m_T-m_i)+2=0`, hence `m_T-m_i=-1/s`.  Thus the arithmetic in M-quant
⟨1⟩3--⟨1⟩5 is correct whenever the assumed two-channel decomposition is
available.

If `W_+` is an isometry onto `H_sc`, then
`N_T=W_+P_TW_+^*` is an orthogonal projection:
`N_T^2=W_+P_T^2W_+^*=N_T`.  Therefore
`spec(N_T) subset {0,1}` and
`spec(Delta X) subset {-1/s,0}`.  This is a statement on `H_sc`; it is not a
statement that every expectation is quantised.

### The `O_eta` coefficient

Write `z=e^{ih}`.  The contact equation

`(2z-z_ke^{ih}-1)s+(2z_k-z_ke^{ih}-1)=0`

at `k=0` gives `s(0,h)=1`; differentiating gives
`s'(0,h)=2i`.  In the bra, the derivative is `-2i`.  For
`d_01,d_12,d_23,d_03=(1,-1,1,-1)`, differentiation of the four pair amplitudes
gives

`-i sum d_xy[(2+x)e^{-ihy}+y e^{-ihx}]
 = -i[-2+2e^{-3ih}]
 = 2i(1-e^{-3ih})`.

All one-site marginals of `D|Omega>` vanish, so the intercept is zero, while
`D|Omega>` is orthogonal to the one-magnon sector.  Consequently
`M_1^{O_eta}` is eta-independent and the shift is exactly
`2i eta(1-e^{-3ih})k+O_I(k^2)`.  ML5 ⟨1⟩4 is a valid refutation of
universality over unrestricted local sources.

### ML5-A in both directions

Necessity is valid: if (4) holds and `M_2` is differentiable, differentiation
at zero gives `mathfrak c_h(O)=0`.  Sufficiency is not valid.  Taylor's theorem
with `mathfrak c_h(O)=0` gives only

`M_2^O(k)=M_2^O(0)+2i chi k M_1^O+O(k^2)`.

The unmentioned constant `M_2^O(0)` remains.  For example, in the theorem's
stated Banach-space hypotheses take `M_1=0` and `M_2(k)=u` for any nonzero
`u in L^2(I)`.  Then `mathfrak c=0` and the second derivative is uniformly
zero, but (4) fails.  There is also an actual four-site FM source with this
defect:

`V=(9/4)S^-_0S^-_2-(3/2)S^-_0S^-_3-(3/2)S^-_1S^-_2+S^-_1S^-_3`.

It has `M_1^V=0`.  Using the same differentiated pair formula as for `D`, the
first-jet coefficient at each Fourier power is respectively
`9/2-9/2`, `-3+3`, `9/2-9/2`, and `-3+3`, so
`partial_k M_2^V(0,h)=0`.  Nevertheless

`M_2^V(0,h)=3/4-(1/2)e^{-ih}+(3/4)e^{-2ih}-(1/2)e^{-3ih}`

is not identically zero.  Thus `mathfrak c_h(V)=0` but (4) fails within the
shard's own local-source model.  The affine direction has the same defect for
every source difference.  Moreover a generic locally uniform
second-derivative bound gives an `O_O(k^2)` remainder, not the relative bound
(2) proportional to `||M_1^O||`, unless that proportional bound is separately
assumed.

### ML4 and the missing uniform constant

ML4-A itself is correct: `U^*R=0` and norm-`C^1` regularity imply
`Gamma(k)^*R=(Gamma(k)-Gamma(0))^*R=O(k)`, and multiplication by
`e^{ik}-1=O(k)` gives `O(k^2)`.  At each fixed `N`, the same Taylor argument
applies to the scalar trace in (15).  The application fails when it asserts a
constant independent of `N`.

I evaluated the shard's own formulas (12)--(14), with the independently
assembled `Q_0` and `J^-_0`, at the fixed hard ring momentum `h=2pi/5` and
the soft ring momentum `k=2pi/N`.  Put
`F_N(k)=<B_N(k,h),(1-P_{1,N})J^-_0|h>>`.  The claimed (15)--(17) require both
`|F_N(k)|/|k|` and
`|(e^{ik}-1)F_N(k)|/(sqrt(N-2)k^2)` to be uniformly bounded (the square root
is the normalization in `Gamma_N`).  Instead:

| `N` | `|F_N|` | `|F_N|/k` | unnormalised amplitude `/k^2` | `Gamma_N` amplitude `/k^2` |
|---:|---:|---:|---:|---:|
| 40 | 1.025465 | 6.5283 | 6.5216 | 1.0579 |
| 80 | 1.302956 | 16.5897 | 16.5855 | 1.8779 |
| 120 | 1.388718 | 26.5226 | 26.5195 | 2.4413 |
| 160 | 1.430295 | 36.4222 | 36.4198 | 2.8974 |
| 200 | 1.454820 | 46.3084 | 46.3065 | 3.2909 |
| 240 | 1.470995 | 56.1879 | 56.1863 | 3.6420 |

The mechanism is elementary: although `B_N(0,h)` is exactly the descendant,
for `k=c/N` the relative phase changes by order one across separations of
order `N`.  Hence `B_N(c/N,h)-B_N(0,h)` is not uniformly `O(k)` in the packet
trace used here.  The proof's fixed-`N` derivative constant grows with volume.
More explicitly, the low-frequency part of the relative-coordinate sum gives

`lim_{N->infinity} N^{-1}<B_N(c/N,h),B_N(0,h)>
 = 8(1-cos(c/2))/c^2`.

At `c=2pi` this is `4/pi^2`, rather than its `c=0` value `1`.  The contact
piece changes by `o(1)`, while the descendant subtraction has coefficient
`2iv(h)/(N-2)`, so

`lim |F_N(2pi/N)| = 2|v(h)|(1-4/pi^2) = 1.549765...`

for the checker's `J=1.37` and `h=2pi/5`.  Thus (15)'s ratio grows linearly
and the normalized (17) ratio grows as `sqrt(N)`.  This is exactly an
order-of-limits obstruction, not a Bethe issue.

## Checker and mutation audit

All green commands passed under optimized mode:

* `mquant_check.py`: operator residue `0`, finite-time residue `3.366e-16`,
  scan residuals `0.004330` and `0.001233` within budget `0.005563`;
* `ml4_check.py`: Ward/projection residuals below `3.473e-15`, fitted amplitude
  exponents `1.99700--1.99988`, and `O_eta` coefficient error `9.963e-06`;
* the relevant Fano, current-reconstruction, ML2, and oracle dependency
  checkers also passed.

I copied all six scripts to `/tmp/tns-mquant-ml45-r1-mutations-20260826` and
mutated only those copies.  Reversing the M-flux current, omitting the ML4
projection, replacing the Fano denominator factor `16` by `8`, replacing the
soft coefficient `2` by `1` in each of the current/oracle checks, and deleting
the even-`N` ML2 singular inventory all exited `1`.  The observed failures were,
respectively, operator residue `2.340`, projection residue `2.740`, all 12 Fano
runs outside tolerance, coefficient error `1.000`, exceptional-inventory
mismatch at `N=6`, and oracle derivative error `1.000`.  The checkers are
red-capable for those local defects.  They do not cover the theorem-level
quantifiers identified below.

## Numbered objections

### 1. FATAL — ML4's volume-uniform `O(k^2)` bound is false

**Attacked steps:** ML4 ⟨1⟩4.⟨2⟩2.⟨3⟩3--⟨3⟩4 and
⟨1⟩4.⟨2⟩3.⟨3⟩1--⟨3⟩4; equations (15)--(17).

The computation above supplies a legal sequence of ring momenta with fixed
`h in I`, `k=2pi/N -> 0`, for which the alleged uniform constant diverges.
The `C^1` hypothesis is used correctly in ML4-A, but the FM channel does not
satisfy it with a volume-independent trace constant on the stated product
packet class.  ML2 (20)--(21) gives completeness; it does not say that the
finite-volume transported traces converge uniformly in this joint limit.
The surviving statement is fixed-`N` `O(k^2)`, or an iterated limit with a
new quantitative restriction such as `kN -> 0`; neither is the CLAIMS row.

**Fix demand:** downgrade ML4 to the proved fixed-volume/ordered-limit
statement, or supply a genuinely packet-smeared infinite-volume trace estimate
that controls `k=Theta(1/N)` and add that scaling to the checker.

### 2. FATAL — ML5-A's sufficiency and affine sufficiency omit the soft intercept

**Attacked steps:** ML5 ⟨1⟩2.⟨2⟩2--⟨2⟩3.

`mathfrak c_h(O)=0` fixes only the derivative.  It does not imply
`M_2^O(0)=0`, so Banach-space Taylor gives a constant plus the claimed linear
term.  The explicit constant-map counterexample above satisfies every stated
regularity hypothesis; the displayed four-site `V` gives the same
counterexample inside the actual FM source class.  The cited Taylor theorem
therefore says less than the leaf claims.  The relative remainder (2) also
needs a source-uniform bound not present in the assumptions.

**Fix demand:** make the criterion
`M_2^O(0)=0` **and** `mathfrak c_h(O)=0`, impose the corresponding two
conditions on affine source differences, and state the exact norm controlling
the second derivative.

### 3. MAJOR — ML5-B never assumes or proves an exhaustive LSZ decomposition

**Attacked steps:** ML5 ⟨1⟩3.⟨2⟩1--⟨2⟩3, especially the leaf “all other
terms” in ⟨2⟩2.

Hypotheses 1--4 bound a descendant term, an orthogonal-current term, and a
named direct-contact term.  No hypothesis or prior claim states the identity
that their sum equals `M_2^O`, and no leaf excludes an additional reduced
term with a nonzero first jet.  ML4 equation (11) computes `PJ`; it is not an
LSZ reduction formula for a source amplitude.  Calling the named two terms
“all other terms” is precisely the missing ML1/ML6 reduction, not a deduction
from hypotheses 3--4.

**Fix demand:** add an exact, normed LSZ decomposition as an explicit
hypothesis of ML5-B, or prove it and cite the resulting claim before summing
the terms.

### 4. FATAL — the shard silently replaces frozen D18 by a stronger spectral H-AD

**Attacked steps:** M-quant ⟨1⟩4.⟨2⟩4, Theorem M-quant
⟨1⟩1.⟨2⟩2 and ⟨1⟩5, and Corollary Mq-quant ⟨1⟩1.

D18 defines H-AD for state families at two finite scattering times as an
approximate convex decomposition, with data `(t_i,t_f,W,epsilon)`.  It contains
no Hilbert space, wave operator, scattering subspace, or projection.  Section
2 of the shard redefines the same name as exact AD1--AD4 with complete Moller
operators.  D18 can support approximate charge-expectation arithmetic; it
cannot define `N_T=W_+P_TW_+^*` or justify its spectrum.  This violates L4 and
makes the CLAIMS dependency “D16--D18” materially weaker than the theorem
actually used.

**Fix demand:** give the spectral hypothesis a distinct D-number and scope
the operator/spec theorem to it; retain a separate expectation-only theorem
with D18's explicit `epsilon` error.

### 5. FATAL — the projected Jacobi reduction is not proved for the quantified sector

**Attacked steps:** Mq-AD3 ⟨1⟩1.⟨2⟩1--⟨2⟩2 and
⟨1⟩4.⟨2⟩3--⟨2⟩4.

The leaf cites “domain-wall enumeration S1” and says it is independently
established in `kink-sector-notes.md` §2.  The cited S1 exists, but its support
is explicitly one `N=14` enumeration (component size 12 and a degree
histogram), not an all-`N` or infinite-chain proof.  The notes say that the
whole `<=3`-wall manifold has `O(N^2)` states and that the truncation is not an
exact sector; they do not prove the asserted connected-component isomorphism
to `ell^2(Z) direct-sum C` or the left/right charge labelling.  Kato--Rosenblum
is sound only after this missing reduction.

**Fix demand:** provide a Lamport-structured all-volume enumeration and an
explicit unitary from the incoming cyclic component to the Fano graph before
calling Mq-AD3 unconditional.

### 6. MAJOR — the DAG adds a variance theorem absent from the shard

**Attacked steps:** Corollary Mq-quant ⟨1⟩1--⟨1⟩2 and Theorem M-quant
⟨1⟩5--⟨1⟩6 as consumed by the M-quant CLAIMS row and TRIANGLE §3.2.

Those steps prove `Delta X=-(1/s)N_T`, its expectation, and its spectrum.  They
do not prove the DAG's
`Var(X_W)=s^{-2}<N_T>(1-<N_T>)`.  Projection algebra does prove this formula
for `Var(Delta X)` in a normalized scattering vector.  Replacing that by the
one-time variance of `X_W` additionally requires a sharp initial wall (or a
two-time measurement convention), control of initial wall fluctuations, and
the operator relation between asymptotic `X_W` and `Delta X`.  None is stated.

**Fix demand:** change the DAG/TRIANGLE statement to `Var(Delta X)`, or add
the missing initial-state and two-time-observable hypotheses and prove the
identification.

### 7. MAJOR — M-flux does not imply that current is a difference of virtual bond potentials

**Attacked steps:** Mq-flux ⟨1⟩2--⟨1⟩3 as silently strengthened in the M row
and TRIANGLE §3.1.

The flux steps prove a difference of *physical boundary currents*.  G0(d)
says that the charge density acting on the vacuum is a difference of virtual
bond insertions,
`q_x triangleright omega=(Jcal_{x|x+1}-Jcal_{x-1|x}) triangleright omega`.
It does not say that the current `j_{x|x+1}` is a lattice divergence of
`Jcal`, as TRIANGLE §3.1 asserts.  The exact M-flux formula survives, but
“memory is a difference of bond data” is not an unconditional consequence of
the cited claim.

**Fix demand:** delete the bond-potential sentence and the G0(d) dependency
from M-flux, or prove a separate dynamical identity relating the time-integrated
boundary current to endpoint bond insertions in the stated state class.

### 8. MAJOR — the spin and model quantifiers outrun D16 and the projected proof

**Attacked steps:** Theorem M-quant ⟨1⟩2--⟨1⟩4 and Mq-AD3
⟨1⟩1--⟨1⟩5 as promoted by the M-quant CLAIMS row.

The shard's full-chain header quantifies over arbitrary on-site spin `s`, while
D16 fixes the concrete spin-`1/2` XXZ chain and Mq-AD3 explicitly proves only
spin `1/2`.  The algebraic equation `delta m=-1/s` is general *if* one assumes
vacuum jump `2s`, leg charges `-1,+1`, and a two-channel spectral decomposition,
but no higher-spin XXZ channel theorem or higher-spin version of D16 supplies
those hypotheses.  The DAG phrase “under (A1)--(A4) of D16--D18” therefore
cannot carry the arbitrary-`s` theorem.

**Fix demand:** scope the concrete theorem and DAG row to `s=1/2`, or state a
separate abstract charge-arithmetic corollary with all higher-spin channel
hypotheses explicit.

### 9. MINOR — several memory leaves cite superseded draft labels rather than the D-number source

**Attacked steps:** Mq-flux ⟨1⟩1, Mq-AD3 ⟨1⟩4.⟨2⟩3, and Theorem M-quant
⟨1⟩2.⟨2⟩1--⟨2⟩2.

These leaves cite `Bd3`/`Bd4`, while the mandated sources are D13/D14.  The
historical labels can be found in `corner-b-draft.md`, but L4 and L6b require
the promoted D-numbers.  The header also mentions claim `A2(e')`, which is not
a CLAIMS row/subclaim name; the corrected classification is A2(e).

**Fix demand:** replace every active `Bd3`/`Bd4` and `A2(e')` citation by the
actual D13/D14/A2(e) source and keep historical labels only in history prose.

### 10. MAJOR — the numerical certificates are red-capable but do not test their advertised quantifiers

**Attacked steps:** ML4 ⟨1⟩6.⟨2⟩1--⟨2⟩2 and the M-quant numerical-certificate
claims consumed by the CLAIMS “tested in” column.

`ml4_check.py` uses only `N=12,...,20` and soft steps at most `3.2e-4`, so
`kN` is tiny and it necessarily sees the fixed-`N` Taylor exponent.  The
countersequence `k=2pi/N` passes outside that sampling window and directly
falsifies uniformity.  `mquant_check.py` checks M-flux plus agreement with a
committed `s=1/2`, `dwmax=3` scan; it does not construct wave operators, test
absence of singular-continuous spectrum, test `spec(Delta X)`, or prove the
charge theorem.  Mutation success establishes local sensitivity, not semantic
coverage of those claims.

**Fix demand:** add a scaled-soft/volume test to ML4 and describe the M-quant
checker in the DAG as a flux/empirical certificate only.

## Quantifier, integrability, and negative-claim audit

No hidden Bethe or many-body integrability hypothesis was found in these
shards.  ML4/ML5 use the direct two-body contact equation and ML2's Jacobi
resolution; M-quant uses a direct domain-wall/Fano reduction.  Those uses obey
the integrability-free directive.  The failure of ML4 is instead the order of
`N -> infinity` versus `k -> 0`, and the full-chain memory lift remains an
asymptotic-completeness problem.

No attacked proof step relies on `A2-orbit-r1`, `G0-soft-r1`, or the brief's
refuted Conjecture M.  The memory shard explicitly rejects the first two, and
TRIANGLE §3.5 correctly keeps Conjecture M refuted.  The stale bond-potential
overread in objection 7 is a new misuse of valid G0(d), not a resurrection of
`G0-soft-r1`.

## Surviving weaker statement

Mq-flux is exact.  Given an explicitly stated two-channel spectral
decomposition, charge conservation gives branch displacements `0` and `-1/s`,
and the transported channel projection has spectrum in `{0,1}`.  For the
displayed Fano operator, trace-class scattering and the resolvent computation
give complete absolutely-continuous scattering plus finitely many bound
states.  ML4-A is a valid abstract fixed-point cancellation lemma, and the FM
trace has a second soft zero at every fixed finite volume, but the claimed
volume-uniform estimate is not proved and is false for the shard's finite-ring
trace.  `O_eta` validly refutes unrestricted source universality.  ML5-A
survives only as the necessity of a zero contact first jet; sufficiency also
requires a zero soft intercept and the stated remainder control.

FAIL(1,2,3,4,5,6,7,8,10)
