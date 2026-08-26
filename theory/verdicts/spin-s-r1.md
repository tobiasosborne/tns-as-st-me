<!-- ROLE: L6 critic verdict, round 1, on Theorem S2-2body-S,
     theory/checks/spin_s_slope_check.py, and the associated DAG surfaces.
     Critic: Codex. Date: 2026-08-26. -->

# Critic verdict r1 — Theorem S2-2body-S

I independently re-derived the occupation-basis Hamiltonian, all three
configuration equations, the contact elimination, unitarity, the physical
soft branch, and the compact-hard remainder.  I also audited the derivation
history's recorded wrong turn, ran the checker under `python3 -O`, and killed
four mutations on copies under `/tmp`.  No FATAL or MAJOR objection survives.

## 1. NOTE — the local equations and channel count are correct

**Exact steps:** ⟨1⟩1.⟨2⟩2--⟨1⟩2.⟨2⟩4, especially equations (3)--(5), (8),
and (10).

**Independent computation.**  On one bond,

`-J(S_x.S_{x+1}-S^2)=JS(n_x+n_{x+1})-Jn_xn_{x+1}`
` -(J/2)(S_x^+S_{x+1}^-+S_x^-S_{x+1}^+)`.

After summing bonds this gives (1).  A magnon hopping into an empty site has
matrix element `-JS`.  The `(1,1)<->(0,2)` matrix element is

`-(J/2)sqrt(2S)sqrt(2(2S-1))=-J sqrt(S(2S-1))=-Jg`.

Thus separated occupancies have diagonal `4JS` and four `-JS` hops;
adjacent occupancies have diagonal `J(4S-1)`, two outer `-JS` hops, and two
`-Jg` double-occupancy hops; a double occupancy has diagonal `4JS` and the
two reverse `-Jg` hops.  These are exactly (3)--(5).

For `S>=1`, fixed `(k_1,k_2)` leaves three amplitudes `(A,B,rho)`, hence two
ratios after quotienting overall normalization.  Equations (5) and (4) give
two independent contact conditions on (T.1):

`S b rho=gW`,
`W=Sa Sigma-g a rho`.

They therefore determine the two ratios exactly.  For `S=1/2`, the normalized
double state does not exist, `g=0`, and there are only `(A,B)` modulo scale;
the single adjacent condition gives `W=(a/2)Sigma`.  Equivalently `mu=b` at
`2S=1`, so (9) reduces honestly to the same one condition.  The system is
neither under- nor over-determined in either case.

The boxed warning in ⟨1⟩2.⟨2⟩1 accurately identifies the historical error.
The actual proof does not repeat it: it never equates `Psi(x+1,x)` with
`Psi(x,x+1)`.  In (10) it uses only the two distinct artificial diagonal
values `Psi(x,x)` and `Psi(x+1,x+1)` in a subtraction from the physical
adjacent equation, while retaining the independent physical amplitude
`d(x)=rho P^x`.

**Fix demand:** none.

**Surviving statement:** equations (3)--(5) exhaust the two-magnon sector,
and the two contacts determine the regular scattering solution exactly; at
`S=1/2` the double channel disappears rather than being silently retained.

## 2. NOTE — elimination gives (T.2), and (T.2) is unitary on shell

**Exact steps:** ⟨1⟩2.⟨2⟩3--⟨1⟩3.⟨2⟩2.

**Independent computation.**  With `P=z_1z_2`, the free energy gives

`E-4JS=-JS ab/P`.

Equation (5) then gives `Sb rho=gW`.  Substitution into the adjacent equation
gives

`W[b+(2S-1)a]=S Sigma ab`,

so, with `mu=(2S-1)a+b`,

`A(z_2mu-Sab)+B(z_1mu-Sab)=0`.

The nonzero-denominator clause of (T.1) forces `B!=0` for a nonzero wave and
hence

`A/B=(Sab-z_1mu)/(z_2mu-Sab)`.

For real momenta put `z_1=ur`, `z_2=u/r`, where
`u=exp(i(k_1+k_2)/2)` and `r=exp(i(k_1-k_2)/2)`.  Direct Laurent reduction
gives exactly

`S_12=n/(-conj(n))`,

`n=2S cos(K/2)cos(q_rel)`
`  -exp(iq_rel)[(2S-1)cos(K/2)+cos(q_rel)]`.

Since (T.1) excludes the corresponding zero denominator, `n!=0`; therefore
`|S_12|=1`.  Exchanging `z_1,z_2` exchanges numerator and denominator with
the same minus sign, proving `S_12(k_2,k_1)=S_12(k_1,k_2)^{-1}`.  At
`S=1/2`, `mu=b` and the permitted cancellation gives precisely the frozen
oracle fraction (16).

**Fix demand:** none.

**Surviving statement:** (T.2), its on-shell unitarity, exchange inversion,
and its exact `S=1/2` degeneration all survive.

## 3. NOTE — the soft branch, endpoint exclusions, and pole scope are sound

**Exact steps:** Statement (T.3)--(T.4) and
⟨1⟩4.⟨2⟩1--⟨1⟩4.⟨2⟩3.

**Independent computation.**  Let `x=z_1` and `y=exp(ik_h)`.  At `x=1`,

`N(1,y)=D(1,y)=S(y^2-1)`.

For fixed `0<|k_h|<pi` this is nonzero.  Applying
`partial_{k_s}=ix partial_x` gives

`[partial_{k_s}N-partial_{k_s}D]_{x=1}=i(y^2-1)`,

and hence

`partial_{k_s} log S_12|_0=i/S`,
`partial_{k_s} delta_12|_0=1/S`.

The continuous phase through `S_12(0,k_h)=1` is therefore unique locally.
For fixed allowed `k_h`, `v_S(k_h)!=0`, so
`sgn(v_h-v_s)` is constant in a sufficiently small two-sided soft
neighborhood.  D7 selects `S_12` for positive sign and its inverse for
negative sign; inversion negates the branch.  This gives exactly
`partial_{k_s}delta_phys|_0=sgn(v_h-v_s)/S` and the two expansions (T.3).

For the pole audit, the denominator is the quadratic

`D(x,y)=-Sy x^2+(Sy^2-S-y^2+y)x+Sy+y^2-y`.

Its complex zeros are the bound-channel poles.  None intrudes at the soft
base because `D(1,y)=S(y^2-1)`, and on every compact hard subset away from
`0,+/-pi` continuity supplies a common pole-free soft neighborhood.  The
real regular domain also excludes `D=0` explicitly; together with the
unitarity identity this leaves no real on-shell pole.  At `S=1/2` numerator
and denominator share the familiar `b` factor, and (T.1)'s `b!=0` clause
makes its cancellation honest.

The edge attacks confirm that the theorem's exclusions are load-bearing, not
cosmetic.  At `k_h=0`, velocity separation is lost and the removable ratio is
identically one near the soft point, so the claimed slope would not extend.
At `k_h=pi`, `D(x,-1)=(x-1)(Sx+S-2)`; the soft base is again singular before
special cancellations (and for `S=1` the nearby ratio tends to `-1`, not the
chosen phase base `1`).  Bound poles and the equal-velocity point can approach
`k_s=0` as `k_h` approaches an endpoint.  For an allowed fixed hard momentum,
however, `v_h=v_s` is outside a sufficiently small soft neighborhood.  A
compact subset of the stated open hard domain has positive distance from all
these problems.  This is exactly, and no stronger than, the local-uniformity
claim in (T.3).

**Fix demand:** none.  Do not widen the theorem to simultaneous soft-hard
limits, the endpoints, or an equal-velocity channel without a new analysis.

**Surviving statement:** the signed physical slope and `O(k_s^2)` remainders
hold for each fixed `0<|k_h|<pi`, locally uniformly on compact hard subsets
with fixed channel; no bound-state pole enters that domain.

## 4. NOTE — the proof is integrability-free and the DAG is in lockstep

**Exact steps:** ⟨1⟩2.⟨2⟩1, ⟨1⟩3.⟨2⟩3, and
⟨1⟩5.⟨2⟩2; `claims/CLAIMS.md` rows `S2-2body`, `S2-2body-S`, and `Bc`;
`theory/TRIANGLE.md` §§2.3, 4, and 7.

**Independent computation.**  Once total momentum and the free energy are
fixed, the separated relative-coordinate equation has the two exchanged
plane-wave solutions.  The shard then substitutes them, together with the
one local double amplitude, into every separated, adjacent, and double
configuration.  This is direct generalized-eigenvector verification; it
does not invoke a spin-`S` Bethe-completeness theorem.  The only use of the
frozen spin-`1/2` leaves is the `S=1/2` comparison and D7/D8 channel
convention.  ML2 is not generalized or silently assumed.

The shard, new DAG row, S2-2body cross-reference, TRIANGLE theorem paragraph,
and status index all state the same regular two-body ratio and
`sgn(v_h-v_s)/S` slope.  Every surface keeps `S2-2body-S` at SKETCH pending
this critic.  The Bc row and TRIANGLE §4 restrict the result to a unit-charge
hard magnon, leave the memory half conditional, leave `|q_hard|>1` open, and
retain Bc as CONJECTURE.  S-general is likewise untouched.

**Fix demand:** after promotion, change only the `S2-2body-S` status and its
pending-critic labels, using the scoping sentence below.  Do not upgrade Bc,
S-general, the memory claim, or the charge-`>1` factor.

**Surviving statement:** the direct two-body theorem needs no integrability
or completeness assumption, and the present cross-references contain no
silent strengthening.

## 5. NOTE — checker and mutation audit pass

**Exact step:** ⟨1⟩5.⟨2⟩1.

**Independent computation.**  The optimized run exited `0` with

`closed-form=1.337e-15`, `unitarity=8.882e-16`,
`exchange=3.334e-16`, `physical-slope=1.200e-11`,
`S=1/2 ratio=5.237e-16`, and `ring residual=1.696e-14`.

The documented `--red` mode exited `1` at the independent Laurent identity.
Three additional copies under `/tmp/spin-s-r1-mutants.INoStR` also died under
`python3 -O`:

| mutation | exit | killing check |
|---|---:|---|
| `mu=(2S-1)a-b` | 1 | SS-C3 independent closed forms |
| interchange `a,b` in `mu` | 1 | SS-C3 independent closed forms |
| omit the double-occupancy amplitude for `S>=1` | 1 | SS-C6 ring residual `1.118e+00` |

The grid and signed-slope checks cover every `2S=1,...,8` on both hard
half-zones; the independently assembled periodic Hamiltonian covers
`2S=1,2,3,4`.  Thus the checker is genuinely general-`S`, not a disguised
spin-`1/2` reduction.  Every failure uses `SystemExit(1)`, so optimization
does not erase the tests.

**Fix demand:** none.

**Surviving statement:** the checker is green, red-capable, sensitive to the
double channel, and proportionate evidence for all symbolic claims it says
it checks.

## 6. MINOR — the shard violates two explicit notation-table rules

**Exact steps:** Statement (T.3), ⟨1⟩2.⟨2⟩1, and
⟨1⟩4.⟨2⟩2; compare `notation.md` overload rule 2 and its spin-`S` table.

**Independent computation.**  `notation.md` reserves bare `chi` as a channel
sign exclusively to `oracle-bethe.md` ⟨1⟩3 and requires every other shard to
spell out `sgn(v_h-v_s)`.  The target instead defines and repeatedly uses bare
`chi` in lines 35--49 and 310--319.  It also introduces bare
`P:=z_1z_2` in ⟨1⟩2 even though the symbol table reserves `P` for the spin
swap/product comparator and adds no spin-`S` overload row for this momentum
product.  The new table rows cover `a,b,mu,g,rho,Sigma,W,q_rel,c_K,n` but not
this `P` (nor the local double amplitude `d(x)`).

**Fix demand:** spell out `sgn(v_h-v_s)` throughout the shard; rename the
momentum product, preferably to a non-colliding local symbol, and add any
remaining spin-`S` local symbols required by L4 to the table.  This is an
editorial notation repair and is not a prerequisite for the mathematical
promotion.

**Surviving statement:** all formulas and conclusions survive unchanged.

## Promotion decision

**PROMOTE.**  Exact scoping sentence:

> `S2-2body-S` is **PROVED** for the bilinear isotropic ferromagnet `H_S=-J sum_x(S_x.S_{x+1}-S^2)` and the real regular two-magnon domain (T.1): the separated, adjacent, and, for `S>=1`, double-occupancy equations directly give `S_12=(Sab-z_1mu)/(z_2mu-Sab)`, while for every fixed `0<|k_h|<pi` the D7 physical phase has `partial_{k_s}delta_phys|_0=sgn(v_h-v_s)/S`, locally uniformly only on compact hard subsets with fixed channel.  This proves the unit-charge exact two-body slope only; it does not prove endpoint or equal-velocity limits, spin-`S` Bethe completeness, S-general, the memory half, the `|q_hard|>1` factor, or Conjecture Bc.

No mathematical step is missing.  Objection 6 is notation-only.

PASS
