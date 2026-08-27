# Critic B, round 1 — `memory-index-b.md`

Target: `theory/memory-index-b.md` only.  The decorrelation exclusions in the
work order were observed.

## 1. MAJOR — the advertised density derivation is formally circular in the frozen notation

**(a) Location.** `theory/memory-index-b.md` §0, H-MQG(4),
⟨1⟩2.⟨2⟩5, §7, and merge proposal M-IDX-density; lockstep source
`definitions.md` D13, introductory paragraph and D13(a).

**(b) Independent computation / counterexample.**  The algebra in ⟨1⟩1--
⟨1⟩2 is sound after replacing `s` by a genuinely free density parameter
`rho`.  If `f_alpha(theta)` is the IT phase along the common unbroken
one-parameter subgroup, differentiating the twisted transfer contraction gives
`f_alpha'(0)=omega_alpha(S^z)=rho`; additivity and continuity give
`exp(i f_alpha(theta))=exp(i rho theta)`.  At `theta=2 pi`, (INT) and MPS
uniqueness give

`exp(2 pi i rho)=c_(2pi)`.

The beta tail gives `exp(-2 pi i rho)=c_(2pi)`, hence
`exp(4 pi i rho)=1` and `2 rho in Z`.  This calculation uses the stated
one-site translation-invariant injective tensor (D1), common unbroken circle
(D2), (S), and (INT); it uses neither a cut nor a correlation assumption.

But the theorem does not introduce a new `rho`.  It imports D13(a)'s `s`, and
the frozen preamble to D13--D18 says explicitly that `s` is the *site spin*
with `d=2s+1`.  Since D1 already has `d in N`, that source definition implies
`2s=d-1 in N` before (INT) or covariance is invoked.  H-MQG(4) then insists
that the wall coordinate is “exactly D13(a), with the charge and `s` fixed in
item 2.”  Thus the proof does not algebraically use half-integrality, but the
formal theorem statement already assumes it through its single source.  The
headline “derived, not assumed” is not licensed in the present DAG.

**(c) FIX DEMAND.**  Introduce a density/jump parameter independent of D13's
site-spin symbol (or generalize D13 explicitly in the shared-source loop), and
state the theorem with that parameter before claiming a new LSM-type result.

**(d) SURVIVING WEAKER STATEMENT.**  Conditional on treating `s` as an
arbitrary real vacuum density rather than D13's site spin, ⟨1⟩1--⟨1⟩2 do prove
the noncircular theorem `e^(2 pi i s)=c_(2pi)=e^(-2 pi i s)`, hence
`2s in N` for `s>0`.

## 2. FATAL — Lemma R reads substantially more into D18(AD3) than D18 says

**(a) Location.** `theory/memory-index-b.md` ⟨1⟩8.⟨2⟩1 and (IDX.3)(a);
lockstep source `definitions.md` D18(AD3--AD4) and D17.

**(b) Independent computation / counterexample.**  AD3 states that leg charge
and non-bound dressing leave a fixed window, that the “remaining local state
is a kink charge eigenstate,” and that the increasing-window limit of D13(a)
exists on it.  It does not specify:

1. a topology in which the reduced state on each fixed window converges;
2. that “kink charge eigenstate” means an eigenstate of every finite-window
   `Qcheck_W` rather than a sector/total-charge label;
3. convergence of the spectral law of `Qcheck_W`;
4. uniform integrability of `|Qcheck_W|` as `W` grows.

D17 does not fill the gap.  Its first-moment clause is the *spatial* condition
`sum_x |x| |rho(S^z_x)-s_tail|<infinity`; it controls one-point expectations,
not `rho(|Qcheck_W|)`, charge variance, or spectral tails.  The elementary
failure mode

`mu_W=(1-1/W) delta_0 +(1/(2W)) delta_W +(1/(2W)) delta_(-W)`

has a perfectly convergent signed first moment (`0`) and pointwise limit
`delta_0`, while
`sum_(|nu|>R) |nu| mu_W(nu)` has supremum at least `1` for every `R`.
This is exactly information that one-point/D13 expectation convergence cannot
exclude.  AD3 may have intended a stronger trace-norm window-marginal
statement, but the frozen words do not state it.  Consequently neither LR1
nor LR2 follows as written, and (IDX.3)(a) is unproved.  This is the shard's
self-declared weakest step, and it fails on the stated hypotheses.

**(c) FIX DEMAND.**  Delete (IDX.3)(a), or strengthen D18 by an explicit
fixed-window reduced-state/law convergence clause plus uniform integrability
of the window-charge laws; do not cite D17 as a substitute.

**(d) SURVIVING WEAKER STATEMENT.**  H-AD-G still implies the already active
M-quant-G channel displacement law.  Separately assumed LR1--LR3 still imply
the marginal-law conclusions of (IDX.2).  No implication H-AD-G => LR has
been established.

## 3. FATAL — the claimed M-quant-G reduction invents a joint coupling absent from its source

**(a) Location.** `theory/memory-index-b.md` (IDX.3)(b),
⟨1⟩8.⟨2⟩2--⟨2⟩3, and merge proposal M-INDEX; lockstep source
`theory/memory-quantization-general.md` (G.1)--(G.2),
⟨1⟩4--⟨1⟩5.

**(b) Independent computation / counterexample.**  The arithmetic itself
matches:

`Delta X=-(1/s)N_T  =>  -2s Delta X=2N_T`,

so the directly defined channel displacement has law `{0,2}` in the
escape-signed convention and mean `2<N_T>`.  However M-quant-G defines only
the outgoing-channel projection `N_T=W_+ P_T W_+^*` and the displacement
operator `Delta X=-(1/s)N_T`.  It never constructs two asymptotic charge
random variables with laws `mu_-` and `mu_+`, never proves that they commute,
and never constructs a coupling whose difference is `-2s Delta X`.
Wave operators and a channel projection do not by themselves provide such a
joint law.  In particular, the source's proof needs only charge conservation
per channel and does not prove either marginal-law statement introduced in
this shard.

Thus ⟨1⟩8.⟨2⟩2's sentence “The channel decomposition provides the physical
coupling” is not in M-quant-G and is not derived here.  The constants and sign
in (G.1) are correct, but the quantifiers/registers do not match.  Under the
work order, any (G-IDX.3) source mismatch is fatal.

**(c) FIX DEMAND.**  State (IDX.3) only as the direct channel law of
`-2s Delta X=2N_T`, or prove asymptotic charge operators/instruments and show
that their joint law has marginals `mu_-`,`mu_+` and the stated difference.

**(d) SURVIVING WEAKER STATEMENT.**  Under H-AD-G,
`spec(-2s Delta X) subset {0,2}` with weights
`1-<N_T>,<N_T>`, and therefore `delta x=-<N_T>/s`; this is exactly the active
M-quant-G result.  It is not yet a coupling theorem for the new charge laws.

## 4. FATAL — (LR) yields integer-valued formal bookkeeping, not the claimed physical outcome law

**(a) Location.** `theory/memory-index-b.md` (IDX.2), especially
⟨1⟩7.⟨2⟩4, the bold sentence “Every asymptotic memory outcome,” §4, and the
merge proposal M-INDEX.

**(b) Independent computation / counterexample.**  From two marginal laws on
`Z`, every abstract coupling `gamma` indeed has an integer-valued coordinate
difference and

`E_gamma[nu_+-nu_-]=m_+-m_-`.

That is a correct measure-theoretic identity, but LR1--LR3 supply no physical
coupling.  Choosing the independent coupling is arbitrary dynamics-free
bookkeeping.  A sequential two-time measurement does define integer readouts,
but its second marginal is generally disturbed by the first measurement, so
its mean difference need not equal the unmeasured-state quantity `delta x`.
Conversely, the noncommuting operator difference is not lattice-valued: for
`Q_-=|0><0|` and `Q_+=|+><+|`, both spectra are `{0,1}`, whereas
`spec(Q_+-Q_-)={-1/sqrt(2),+1/sqrt(2)}`.

The shard notices both caveats, but then continues to call the arbitrary
coupling values “memory outcomes.”  Under LR alone it has proved an
integer-valued representation of a difference of marginal means, not an
outcome distribution of the dynamical event.  This falls short of the target
G-IDX.2 unless a coupling/decoherence/instrument clause is added to LR.

**(c) FIX DEMAND.**  Replace “outcome” by “formal coupling bookkeeping”
everywhere, or add and prove a physical asymptotic joint-law clause with the
correct marginals and first moment.

**(d) SURVIVING WEAKER STATEMENT.**  Under LR1--LR3,
`delta x=(m_+-m_-)/(2s)` and this number can be written as the expectation of
an integer difference under any chosen coupling.  `delta x` itself is not
quantized, and no measurement law follows.

## 5. MAJOR — (IDX.0c) is false for the vacua with the shard's defined `Qcheck_W`

**(a) Location.** `theory/memory-index-b.md` (IDX.0c), (I.2),
⟨1⟩4.⟨2⟩1--⟨2⟩5 (“pure vacuum specialization”), and (I.4).

**(b) Independent computation / counterexample.**  `Qcheck_W` in (I.2)
subtracts `s` on the left of the cut and adds `s` on the right.  In the pure
alpha vacuum the natural normal-ordered charge is instead
`Q_W^alpha=sum_(x in W)(S^z_x-s)`.  With `n_R=b-c`,

`Qcheck_W=Q_W^alpha+2s n_R`.

Hence its characteristic function has the omitted factor
`exp(2 i s theta n_R)`.  The simplest counterexample is the product alpha
vacuum with `S^z=s` exactly: then
`law(Qcheck_W)=delta_(2s n_R)`, which escapes to infinity and is not tight as
the right edge grows.  Formula (I.4) instead computes the law of
`Q_W^alpha`; it silently changes the operator/normal ordering.  The analogous
problem occurs for beta.  The two-sided alpha|beta kink calculation is not
affected because (I.2) matches its tails.

**(c) FIX DEMAND.**  Remove the vacua from (IDX.0c), or separately define
tail-specific vacuum charges `Q_W^alpha` and `Q_W^beta` and state (I.4) only
for those operators.

**(d) SURVIVING WEAKER STATEMENT.**  The characteristic-function/tightness
argument can hold for two-sided decorated alpha|beta references with the
step-normal-ordered `Qcheck_W`, and (I.4) holds for a pure vacuum after using
its own uniform normal ordering.

## 6. MAJOR — the advertised one-sided checker mutation stays green

**(a) Location.** `theory/memory-index-b.md` ⟨1⟩3 final remark, §4
weak-limit paragraph, and checker C-IDX-2/C-IDX-2-red in §6.

**(b) Independent computation / counterexample.**  Let
`n_R=b-c`.  Replacing the `+s` counterterm on the right by `-s` throughout
gives

`Q_one=Qcheck_W-2s n_R`.

After ⟨1⟩2 has derived `2s in Z`, this deterministic difference is an
integer.  Therefore

`exp(2 pi i Q_one)=exp(2 pi i Qcheck_W) exp(-2 pi i (2s)n_R)=1`

for every window, including half-odd-integer `s`.  For `s=1/2,1,3/2` and
`n_R=3,4,5`, direct evaluation gives phase `1` in all nine cases.  There is no
parity alternation.  Equivalently, using `c_(2pi)=exp(2 pi i s)`, each
one-sided factor has phase `c_(2pi) exp(-2 pi i s)=1`.

Thus the `s -> s+0.1` mutation would fail as desired, but the alternative
one-sided mutation explicitly promised by C-IDX-2-red would *not* fail.  The
claim that D13's two-sided calibration is “exactly what kills the offset” is
also false once the density theorem is assumed: it is needed to identify
wall position, not to make this one-sided charge integral.  The checker spec
is implementable, but this mutation does not test the asserted dependency.

**(c) FIX DEMAND.**  Delete the one-sided C-IDX-2-red mutation and the parity
claim; retain only a mutation that breaks a necessary premise, such as the
counterterm shift or one tail's covariance phase.

**(d) SURVIVING WEAKER STATEMENT.**  The exact two-sided identity (I.3) is
correct, and the `s -> s+0.1` mutation produces the intended drifting phase.

## 7. MINOR — the A1(b) analogy is not itself the claimed two-tail self-adjointness proof

**(a) Location.** `theory/memory-index-b.md` (IDX.0-op) and
⟨1⟩5.⟨2⟩2--⟨2⟩3; source `theory/corner-a.md` A1(b),
⟨1⟩4.⟨2⟩3.

**(b) Independent computation / counterexample.**  A1(b) is an iff for a
single unbroken, normal-ordered pure-vacuum GNS string.  It has no padding
hypothesis; padding belongs to A1(d), not A1(b).  The shard applies the idea
to a two-sided decorated kink GNS, so it is outside A1(b)'s literal
hypotheses.  Its own tail-shell contraction plausibly supplies the needed
extension: a nonscalar virtual unitary gives
`2(1-|tr(V_theta r)|^2)>0`, while scalar virtual unitaries make remote shells
act trivially.  My independent seeded `chi=2` contraction gave, at
`theta=pi` and length 30,
`phi=0.0416984784` versus limit `0.0416984671`, hence obstruction
`1.9166030432>0`.

What is not “immediate” is self-adjointness of the algebraically defined
`Qhat`.  Exact stabilization of every `exp(i theta Qcheck_W)` on a dense local
domain should first be assembled into a strongly continuous unitary group;
Stone's theorem then gives a self-adjoint generator, and one must show its
action agrees with stabilized `Qcheck_W`.  The present leaf asserts those
domain conclusions without that argument.

**(c) FIX DEMAND.**  Present the two-tail result as a new lemma, prove exact
shell invariance on the local GNS domain, construct the strongly continuous
group, and invoke Stone; cite A1(b) only as the one-tail analogue.

**(d) SURVIVING WEAKER STATEMENT.**  The scalar/nonscalar iff is consistent
with A1(b), uses the required tailwise normal ordering, and needs no padding.
The nonscalar branch already proves absence of the proposed strong unitary
limit.

## 8. MINOR — the general two-sided contraction is left schematic at a load-bearing leaf

**(a) Location.** `theory/memory-index-b.md` ⟨1⟩4.⟨2⟩2--⟨2⟩3 and §7,
weakest-step item (2); checker C-IDX-2/3.

**(b) Independent computation / counterexample.**  The displayed contraction
introduces an undefined schematic middle map `M_theta`, suppresses the exact
left/right composition order, and then cites D1(e') as if it supplied the
formula.  D1(e') supplies the CP contraction, not this twisted reduction.  A
generic `chi=2` recomputation does support the intended pure-tail algebra:
length-two word rank `4`, density residual `5.94e-15`, left-canonical residual
`1.70e-14`, and NC-3 map residual `1.59e-16`; the length-30 characteristic
also converged to the predicted boundary trace as recorded in objection 7.
That evidence does not replace the missing exact middle-block derivation for
arbitrary finite decorations.  The proposed checker file is absent, and the
specification's “monotone-decaying tails” condition is stronger than
tightness and need not hold monotonically with window size.

**(c) FIX DEMAND.**  Write the exact ordered CP-map contraction and its norm
bound, including normalization and every mismatch scalar; replace monotonicity
by the quantified tightness bound actually proved.

**(d) SURVIVING WEAKER STATEMENT.**  NC-3 and transfer primitivity do support
uniform characteristic-function convergence for pure tails and should extend
to a fixed finite middle block once that contraction is written explicitly.

## 9. NOTE — the `chi=2`, non-half-integer density attack fails for the right reason

**(a) Location.** `theory/memory-index-b.md` ⟨1⟩1--⟨1⟩3 and checker C-IDX-1;
mandatory density/cut attack surface.

**(b) Independent computation / counterexample.**  Take the requested
non-half-integer value `s=0.37` and on-site charge coset
`0.37+Z`.  An alpha tensor can be engineered with virtual charges `(0,1)`:
diagonal entries have physical charge `0.37`, and the two off-diagonal entries
have charges `1.37` and `-0.63`; generic coefficients can be injective.

For the beta tensor with slope `-0.37`, let its two virtual charges differ by
`d`.  Covariance would require the two off-diagonal physical charges
`-0.37+d` and `-0.37-d` both to lie in `0.37+Z`.  Adding those two conditions
requires `-1.48 in Z`, impossible.  A diagonal entry would require
`-0.37 in 0.37+Z`, also impossible.  Thus no strongly connected virtual
charge graph exists; the transfer map cannot be irreducible/injective.  More
generally, a closed virtual path enforces the filling congruence, and
primitivity removes a larger-unit-cell escape.  A period-two construction can
evade a one-site congruence only by becoming noninjective, which is outside
D1.  This pinpoints where the attempted counterexample fails.

The finite offsets independently recompute as
`q_W mod Z = 2s(b-c)` after using the alpha-tail relation.  For cuts `c=0`,
windows `[-1,2]`, `[-2,2]`, `[-2,3]`, the offsets are all `0 mod Z` at
`s=1/2`; at `s=0.37` they are respectively `0.48,0.48,0.22 mod Z`, with
phases `-0.992115+0.125333i`, the same, and
`0.187381+0.982287i`.  The nonintegral phases persist for an arbitrary cut
until the impossible beta-tail covariance condition is imposed.  Once both
tail relations hold, (I.3) is an operator identity; a correlated `chi>=2`
region cannot spoil it.

**(c) FIX DEMAND.**  Keep the density proof, but repair objection 1's formal
parameter circularity and describe the failed counterexample by the virtual
charge-cycle obstruction rather than the narrower triangular example.

**(d) SURVIVING WEAKER STATEMENT.**  No `chi=2` counterexample was found;
after freeing the density parameter from D13, the density theorem and exact
arbitrary-cut identity survive this attack.

## 10. NOTE — the Levy/tightness step and explicit two-time avoidance are correct

**(a) Location.** `theory/memory-index-b.md` ⟨1⟩4.⟨2⟩4,
⟨1⟩7.⟨2⟩1--⟨2⟩4, and §4.

**(b) Independent computation / counterexample.**  For an atom at `nu`,

`u^(-1) int_(-u)^u (1-cos(theta nu)) dtheta
 =2(1-sinc(u nu))`,

which is at least `1` for `|nu|>=2/u`; NC-4 is correct.  Uniform convergence
of characteristic functions to a function continuous at zero therefore gives
tightness.  Fourier inversion plus tightness prevents loss of total mass.
LR2's `|nu|` weight is also genuinely needed for means: the laws
`(1-1/W)delta_0+(1/W)delta_(W^2)` converge weakly to `delta_0` while their
means diverge.  With the fixed lattice `Z`, LR2--LR3 prevent mass escape and
first-moment escape; a coupling formed *after* these limits cannot smear
support off `Z`.

The shard also does not form the noncommuting operator difference.  The
projection example in objection 4 confirms why that avoidance is necessary.
The remaining defect is the physical-coupling overclaim, not the Levy
compactness step.

**(c) FIX DEMAND.**  No change to NC-4 or LR2--LR3; limit the coupling language
as demanded in objections 3--4.

**(d) SURVIVING WEAKER STATEMENT.**  Given LR1--LR3 as independent
hypotheses, the limiting marginal laws are probability measures on `Z` with
convergent first moments and no weak-limit smearing.

FAIL(1,2,3,4,5,6)
