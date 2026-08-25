<!-- ROLE: L6 critic verdict, round 1, on the three Corner-A proof shards.
     Critic: Codex. Date: 2026-08-25. -->

# Critic verdict r1 — Corner A (WI, A1, A2, G0)

Critic: Codex, adversarial pass under L6/L6b.  Artifacts:
`theory/corner-a.md`, `theory/corner-a-kinks.md`, and
`theory/corner-a-goldstone.md`, checked against `notation.md`, D1--D11,
`docs/framing.md`, `claims/CLAIMS.md`, and the frozen D6--D8 conventions in
`theory/oracle-bethe.md`.

Method: I re-expanded WI coefficient by coefficient, recomputed the half-string
and cocycle composition laws from their definitions, checked the sector
arguments independently, and derived the current identity and the Heisenberg
FM current directly.  I also ran a four-site, `chi=2` Pauli-basis MPS check and
a seven-site one-magnon ring check.  The decisive numerical data are recorded
below; no repo numerical implementation was used.

## Independent spot checks

Take `A = (I,X,Y,Z)/2`, `r=I/2`, with physical dimension four and virtual
dimension two.  This is injective in one site and its transfer channel is
depolarising (`lambda_E=0`).  The `Z_2` action

`u(g)=diag(1,-1,-1,1)`, `V(g)=Z`

satisfies D2's convention `U(g)A=V(g)^{-1} A V(g)`.  On four sites, with
`R={1,2}` and generic complex boundary vectors, direct enumeration of all
`4^4` coefficients gave

```
max | U_R psi - psi[A_0 V^{-1} A_1 A_2 V A_3] | = 0.0.
```

Thus the **interior** WI telescoping and its endpoint orientation in
`corner-a.md` are correct: D2 puts `V^{-1}` on the left boundary and `V` on the
right.  (The older HANDOFF brief, line 42, has these reversed.)

For the continuous adjoint action with anti-Hermitian virtual generator
`K=-iZ/2`, the same tensor gives exactly

```
max_s ||B_G^s-(A^s K-K A^s)|| = 0,
max_s ||B_G^s-N_k(K)^s-(1-e^{ik})A^sK|| = 0       (k=0.37),
rank N_0 = 3,    rank N_0.37 = 4.
```

For the `chi=1` all-up FM tensor `A^up=1, A^down=0` and
`q=iS^x`, one instead obtains

`B_G=(0,i/2)`, `ran N_0={0}`, and
`min_c ||B_G-cA||=1/2`.

This supports the corrected tensor-level broken/unbroken dichotomy.  It does
not support the stronger claims made around it, for the reasons below.

## Numbered objections

### 1. MAJOR — WI is not an identity on *every* `Lambda superset R` under D1(e)

**Steps:** `corner-a.md` ⟨1⟩3 ASSUME/PROVE and ⟨2⟩4--⟨2⟩5; propagated to the WI
row of `claims/CLAIMS.md` ("all windows").

D1(e)'s window vector has insertions only between tensors in `[a,b]`:

`<b_l|T_a M_{a|a+1} ... T_b|b_r>`.

If `Lambda=R=[a,b]`, the alleged insertions on `(a-1|a)` and `(b|b+1)` are
outside the defined window expression.  The actual coefficient after applying
the symmetry is

`<b_l| V^{-1} A_beta^{s_a} ... A_beta^{s_b} V |b_r>`,

not the D1(e) vector with the unchanged arbitrary `b_l,b_r`.  One may repair
the theorem by requiring one exterior tensor on each side, or by extending
D1(e) to boundary-bond operators (equivalently changing the boundary vectors).
As written, the universal quantifier used to mark WI PROVED is false.  The
four-site check above confirms the repaired, strictly-interior identity and
also confirms that there is no silent `V`/`V^{-1}` flip in that repaired form.

### 2. MINOR — the WI claims row multiplies a state by a phase

**Step:** `claims/CLAIMS.md` WI row versus `corner-a.md` ⟨1⟩3.⟨2⟩5.

The vector identity carries `e^{i|R|theta}`, but the induced state does not:
the phase cancels between bra and ket, as the shard itself says.  A nontrivial
phase times a state is not a state.  The DAG row must distinguish the window
vector identity from the state identity.

### 3. FATAL — A1's endpoint sectors are identical by definition, and its
claimed diagonal stabiliser is generally wrong

**Steps:** D9(c), `corner-a.md` ⟨1⟩4(e)--(f), especially ⟨2⟩5.⟨3⟩2 and ⟨2⟩6;
`claims/CLAIMS.md` A1 row.

D9(c) defines the `g`-twisted endpoint family using

`{omega_A^{M@b}: M in V(g) GL(chi)}`.

But `V(g)` is invertible, so `V(g) GL(chi)=GL(chi)` for every `g`.  All of the
purported endpoint sectors are literally the same set.  A1(f)'s transitive
relabeling is therefore vacuous and circular: the object it purports to derive
was introduced in D9, and D9's actual formula has erased `g`.

Independently, A1(c) itself says that a residue acts trivially whenever its
virtual matrix is scalar.  Therefore the stabiliser of the vacuum under
`G_L x G_R` contains all pairs whose combined residue
`V(g_L)V(g_R)^{-1}` is scalar; it is diagonal only when the projective action
is faithful (`N_alpha={e}`).  No such hypothesis is assumed.  A one-site
product vacuum invariant under a `Z_2` action has `chi=1`, `V(g)=1`, and
`H_alpha=G`; then **all** of `G_L x G_R` fixes the state, while A1(e) says the
stabiliser is exactly `G_diag` and the orbit is `G`.  The actual orbit is one
point.  At minimum the effective group must be reduced by `N_alpha`, and D9(c)
must be replaced by a non-vacuous equivalence relation.

### 4. FATAL — the twisted-algebra multiplication uses the wrong inverse and
order, and phases do not act on states as claimed

**Steps:** D4(a), D4(d), `corner-a.md` ⟨1⟩4(d), ⟨2⟩4.⟨3⟩1--⟨3⟩3.

D4 defines `Vcal_b(g)=Vcal_b(V(g)^{-1})` and defines `Vcal_b(M)` by **left**
multiplication of the existing bond insertion.  Hence, with the usual operator
composition convention,

```
(Vcal_b(h)Vcal_b(g))(M_b)
 = V(h)^{-1} V(g)^{-1} M_b
 = (V(g)V(h))^{-1} M_b
 = exp[-i omega(g,h)] V(gh)^{-1} M_b.
```

This is not the displayed
`Vcal_b(h)Vcal_b(g)=exp[i omega(h,g)]Vcal_b(hg)`.  The proof silently replaces
the D4 implementer `V(g)^{-1}` by `V(g)` in ⟨2⟩4.⟨3⟩1.  Correcting this requires
choosing an action convention and then using the inverse/opposite multiplier.

There is a second, more physical obstruction.  `Vcal_b` is defined on
**states**.  Multiplying a ket bond insertion by `exp(i omega)` has no effect on
the normalised state, so an equation with a scalar phase multiplying a state
map does not realise a twisted group algebra.  The multiplier lives on virtual
vectors/edge Hilbert spaces, not on the state orbit as presently defined.
Constructing such an action is exactly where the split/normality issue in
⟨1⟩4.⟨2⟩9 enters; it cannot be declared unused.

### 5. MAJOR — the lemma `omega^{M@b}=omega iff M is scalar` is plausible, but
the given proof does not prove it

**Steps:** `corner-a.md` ⟨1⟩4.⟨2⟩2.⟨3⟩1--⟨3⟩3; D1(e).

D1 calls `omega_A[T]` a state but gives no normalization denominator for a
general `M in GL(chi)`.  Taken literally, the matrix elements in ⟨3⟩1 scale by
`|c|^2` for `M=cI`, contradicting the asserted "converse is trivial".  If
normalization is implicit, equality of states gives equality only after a
common normalization factor; the proof must first obtain
`M Z M^dagger = gamma Z`, not `M Z M^dagger=Z`.

Moreover, the particular choice
`P_1=|a><c|`, `Q_1^dagger=|a><c|` in ⟨3⟩3 does not extract arbitrary matrix
entries and does not imply the displayed matrix identity.  Injectivity gives
that word products **span** `M_chi`, not that each `P_i` independently ranges
over every matrix; a multilinear extension argument is needed.  A repaired
normalised proof should indeed force `M` to be scalar, but A1(b), A1(c), and the
claimed stabiliser currently depend on a missing load-bearing argument.

### 6. MINOR — A1's Cauchy criterion is false as stated

**Step:** `corner-a.md` ⟨1⟩4.⟨2⟩3.⟨3⟩2.

Because `<Psi_y,Psi_y'>=rho_{y'-y}`, Cauchy convergence requires uniform
control for **all** differences after the two endpoints are large.  It is not
equivalent merely to `rho_n -> 1` as `n -> infinity`; successive vectors have
fixed squared distance `2-2 Re rho_1`.  The one-way implication actually used
later (Cauchy implies the required limiting behavior) is enough to repair the
nonconvergence result, so this is not by itself fatal, but the stated iff leaf
violates L6b.

### 7. MAJOR — `[omega]` enters only at group level; the asserted Lie-algebra
central term is not "exactly" the SPT index

**Steps:** D4(d), `corner-a.md` ⟨1⟩4(d), ⟨2⟩4.⟨3⟩3--⟨3⟩4;
`docs/framing.md` lines 14--18.

The projective multiplier of `V` is the group-level SPT datum.  Differentiating
a local section need not retain it.  The standard counterexample is the AKLT
edge: the nontrivial projective `SO(3)` representation has the `Z_2` group
extension, while `H^2(so(3),R)=0` (Whitehead's lemma) and the spin-half edge
generators satisfy the ordinary `su(2)` commutator with no central scalar.
Thus a torsion SPT class can have zero infinitesimal cocycle.  The leaf
"standard differentiation" cannot justify the campaign's identification of
the group class with a Lie-algebra central charge.  The valid weaker statement
is that `[omega]` defines the multiplier/central extension of the **group** (or
its twisted group algebra, after fixing the inverse convention); `c_alpha` is
at most its local infinitesimal image and can lose all topological information.

### 8. FATAL — A1's physical charge-algebra conclusion is circular, and the
normality SKETCH is load-bearing

**Steps:** D4(d), D9(c), `corner-a.md` ⟨1⟩4(d),(f), and boxed ⟨1⟩4.⟨2⟩9.

A1 lists D4 and D9 among its assumptions, but D4(d) already **defines** the
asymptotic charge algebra to be `C_omega[H_alpha]`, while D9(c) already defines
the endpoint modules that A1 claims to identify.  The theorem therefore does
not establish the symplectic/physical action demanded by `docs/framing.md`; it
repeats a definition.  To upgrade the formal virtual matrices into physical
charges one must construct their action in a representation or on an edge
algebra.  The only offered route is the split-property/vector-state argument
in ⟨2⟩9, which is explicitly SKETCH.  Without it, `[omega]` is formal virtual
bookkeeping and A1's advertised charge algebra on the relevant state space is
not proved.

### 9. NOTE — the factorised sector-disjointness lemma survives the attack

**Steps:** `corner-a-kinks.md` ⟨1⟩8(i)--(ii).

Approximating a vector by `pi(C)Omega` and using the factorised boundary
condition does preserve both asymptotic labels under normal perturbations.  If
two representations have a common nonzero subrepresentation, a transported
vector state is normal in both, contradicting the uniqueness of the boundary
limits.  I found no counterexample to ⟨1⟩8(i)--(ii).  This part is a useful
surviving lemma independent of the later orbit claim.

### 10. MAJOR — A2's limit object is outside D1(e), and the advertised exact
rate is not justified by `lambda_E`

**Steps:** `corner-a-kinks.md` ⟨1⟩9(b), ⟨2⟩2.⟨3⟩2--⟨3⟩4, ⟨1⟩8(iii); D1(c),(e).

`rho_x^(g)` differs from the uniform `A_alpha` tensor on an entire half-chain.
It is therefore **not** a decorated state under D1(e), which permits only
finitely many modified sites/bonds.  The proof compares finite states to this
undeclared object before constructing it.  It can be constructed consistently
as the weak-* limit, but then positivity, normalization, and the transfer
formula must be part of that construction rather than imported from D1(e).

`lambda_E` is defined in D1(c), but as the largest subleading spectral modulus.
For a transfer map with a nontrivial Jordan block at that modulus,

`E^m-P = O(m^p lambda_E^m)`, not `O(lambda_E^m)`.

The honest pure-exponential statement is for every chosen
`tilde_lambda in (lambda_E,1)`, with a constant depending on it (or else with
the polynomial prefactor retained).  The proof's appeal to "the spectral
decomposition" does not exclude Jordan blocks.  Also the relevant symbol is
initially `lambda_{E_beta}`; equality along a group orbit follows from IT by
similarity, but is not stated at this leaf.  Thus weak-* convergence is
credible, while the claimed rate `lambda_E^(y-w)` is not proved under D1.

### 11. FATAL — A2(e)'s `Acal`-orbit/relative-twist statement is false for
nonabelian broken symmetry

**Steps:** D9(d), `corner-a-kinks.md` ⟨1⟩9(e), ⟨2⟩5;
`claims/CLAIMS.md` A2 row.

The componentwise `G_L x G_R` orbit of `(alpha,alpha)` has stabiliser
`H_alpha x H_alpha`, not `G_diag`; it is

`(G/H_alpha) x (G/H_alpha)`,

which is not `(G x G)/G_diag` in general.  For the shard's own M1 example,
`G=SU(2)`, `H=U(1)`: the vacuum-pair space is `S^2 x S^2` (dimension four),
whereas `Acal` is set-isomorphic to `SU(2)` (dimension three).

Nor is `g_L g_R^{-1}` invariant under the diagonal physical action: simultaneous
left multiplication sends it to
`h g_L g_R^{-1} h^{-1}`.  Vacuum pairs modulo global rotations are classified
in the `S^2` example by their relative angle, and generally by an appropriate
double-coset datum, not by an element of `Acal`.  The claimed relative twist is
also choice-dependent when representatives are changed by stabiliser elements.
A2(a)--(d) may survive, but A2(e) and the DAG's global orbit statement do not.

### 12. MAJOR — "kink = contact term" is a name, not a proved contact-term
identity

**Steps:** `corner-a-kinks.md` lines 11--16, ⟨1⟩9(d), and
`corner-a.md` terminology table line 459.

What ⟨1⟩9(d) proves (modulo objections 9--10) is a sector jump: finite strings
give kink--antikink decorations and the weak-* half-string limit has one
different asymptotic label.  No contact term is defined in `notation.md` or
definitions.md, no distributional Ward identity is written, and no matrix
element is shown to be supported at coincident insertions.  The main shard
itself calls the phrase a coinage/slogan.  It cannot simultaneously appear in
the A2 PROVED row as mathematical content.  Replace it by the precise
surviving-end/sector-jump statement, or define and prove an actual contact-term
formula.

### 13. FATAL — Lemma N is not an exact finite-window null identity, so G0(c)'s
displayed vector equality is not proved in the declared register

**Steps:** D1(f), D5(a)--(b), `corner-a-goldstone.md` ⟨1⟩5(i), ⟨2⟩1, and
⟨1⟩6(c).⟨2⟩3.

On a finite window `[a,b]`, reindexing the two sums in `Phi_k(N_k(X))` cancels
only the interior bond insertions.  It leaves

```
e^{ik(b+1)} [right-boundary X term]
 - e^{ika} [left-boundary X term].
```

These do not vanish for arbitrary D1(e) boundary vectors.  In the four-site
`chi=2` test specified above, at `k=0.37` with generic boundaries,

`||Phi_k^Lambda(N_k(K))|| = 0.5912426665717146`,

not zero.  The bilateral reindexing in ⟨1⟩5.⟨2⟩1 is a formal infinite-sum
argument and contradicts D1(f)'s promise that identities are first exact
finite-window identities.  The standard excitation-ansatz gauge equivalence
is valid only after specifying the thermodynamic/generalised-vector quotient
and proving the boundary terms disappear there.  Until that is done,

`Phi_k(B_G)=(1-e^{ik})Phi_k(AX)`

has the omitted boundary term `Phi_k(N_k(X))` and is not an exact window-vector
identity.  This is load-bearing for G0(c).

### 14. FATAL — "(IT) fails for broken directions" contradicts D2 and fails in
the explicit FM tensor

**Steps:** `claims/CLAIMS.md` G0 row; `corner-a-goldstone.md`
⟨1⟩6.⟨2⟩7 and lines 180--185.

D2(b) assumes (IT) for **every** `alpha,g`, with the target tensor
`A_{g dot alpha}`.  In the all-up FM, for a broken `x` rotation,

`U(epsilon)A_up=(cos(epsilon/2), i sin(epsilon/2))=A_{g(epsilon) dot alpha}`

with `chi=1`, `V=1`, `theta=0`.  Thus D2's (IT) holds exactly.  Its derivative
is `B_G=(0,i/2)`, which is not in `ran N_0={0}`; the numerical residual modulo
the ray is `1/2`, as recorded above.  What fails is only an intertwining
relation that returns to the **same** vacuum tensor.  Calling that failure of
(IT) is a direct internal contradiction and obscures the actual reason the
broken tensor is physical.

### 15. NOTE — the corrected tensor-level dichotomy itself survives the two
decisive examples

**Steps:** `corner-a-goldstone.md` ⟨1⟩6(a)--(b).

For the continuous adjoint symmetry of the `chi=2` Pauli MPS,
`B_G=AK-KA=N_0(K)` exactly; for the broken all-up FM direction,
`B_G=(0,i/2)` has distance `1/2` from `ran N_0+C A`.  The integration argument
in ⟨1⟩6.⟨2⟩2 is plausible once the smooth group action on local state
functionals is written carefully.  The defensible statement is:

> after normal ordering, the same-vacuum tangent is gauge exactly for
> `xi in Lie(H_alpha)`; a broken real Lie-algebra direction is not.

This survival does not cure objections 13--14 or supply a soft theorem.

### 16. MINOR — the rank jumps in the opposite limiting direction, and it does
not cause the `(1-e^{ik})` factor

**Steps:** `corner-a-goldstone.md` ⟨1⟩5(ii)--(iii), ⟨1⟩6(c), lines 77--78.

Lemma N's finite-dimensional rank calculation is correct: for the `chi=2`
example the ranks are `rank N_0=3` and `rank N_0.37=4`, matching
`chi^2-1` and `chi^2`.  Thus the rank **drops** by one on taking `k -> 0`; the
wording "at `k=0` ... jumps from `chi^2-1` to `chi^2`" is backwards unless the
direction of motion is explicitly away from zero.  More importantly, the
factor follows algebraically from comparing `N_0(X)` with `N_k(X)`; no argument
shows that a rank discontinuity is "exactly" that factor.

### 17. NOTE — the nearest-neighbour current identity and the FM O1
re-derivation are correct under the frozen conventions

**Steps:** D6, D10, `corner-a-goldstone.md` ⟨1⟩6(e), ⟨1⟩7.⟨2⟩3.

From D10 directly,

```
[H,q_x]=j_{x-1,x}-j_{x,x+1},
[H,Q[f]]=sum_x (f(x+1)-f(x)) j_{x,x+1}.
```

With the frozen Fourier kernel `f(x)=e^{ikx}`, this is exactly
`[H,Q_k]=(e^{ik}-1)J_k`.  For the Heisenberg FM and `q=iS^x`, direct bond
commutation gives

```
j_{x,x+1}|Omega> = -iJ/4 (|x>-|x+1>),
J_k|Omega> = -iJ/4 (1-e^{-ik}) |k>.
```

Consequently `H|k>=J(1-cos k)|k>`, agreeing with frozen oracle O1.  An
independent `N=7`, `J=1.3`, `k=2pi/7` ring calculation gave commutator residual
`1.14e-16` and energy `0.4894632575836464`, versus exact
`0.48946325758364634`.

### 18. FATAL — the current identity does not imply an Adler zero, a universal
linear soft coefficient, or oracle O7/O9

**Steps:** `corner-a-goldstone.md` ⟨1⟩6(e), especially lines 87--89 and
⟨2⟩5.⟨3⟩5; ⟨1⟩7.⟨2⟩5; `claims/CLAIMS.md` G0 row and the A=>C edge.

In a matrix element, the identity says only

`<out|[H,Q_k]|in>=(e^{ik}-1)<out|J_k|in>`.

All dependence on `H`, `xi`, the vacuum, and the hard legs is in `J_k`.
Already if `<out|J_k|in>=C_hard+O(k)`, the coefficient of the linear term is
`i C_hard`, so hard data enters at `O(k)`, not necessarily `O(k^2)`.  If the
current matrix element has a `1/k` infrared singularity there is no zero at
all.  Regularity, LSZ/scattering reduction, factorisation, and a Ward identity
relating `J_0` to external charges are precisely the missing Corner-C work.

The factor is also convention-dependent: the kernel `e^{-ikx}` gives
`e^{-ik}-1`, and reversing the orientation/sign of the current flips it.  Its
Hamiltonian independence is the tautological statement that a discrete
difference was factored out after **defining** a Hamiltonian-dependent current;
it is not universality of the complete soft coefficient.

The shard itself concedes that obtaining oracle O7/O9's number `2` requires
evaluating `J_k` between hard legs.  Therefore G0 does not rederive O7/O9, does
not prove their hard-independence, and does not yet furnish the campaign's
load-bearing A=>C edge.  It rederives only O1 in the one-magnon sector, where
the FM current happens to supply a second lattice difference.

### 19. MAJOR — G0(e)'s Hamiltonian quantifier exceeds its proof

**Steps:** `corner-a.md` ⟨1⟩1(H4), `corner-a-goldstone.md` ⟨1⟩6 ASSUME and
⟨2⟩5.⟨3⟩2; D10.

H4 says finite range, while ⟨2⟩5.⟨3⟩2 uses the nearest-neighbour assertion that
only `h_{x-1,x}` and `h_{x,x+1}` meet `q_x`.  A longer-range invariant
Hamiltonian has several crossing terms and D10(a)'s single-bond formula is not
the required current.  One can recover a factor `e^{ik}-1` by defining the
current across each cut as the sum of all interactions crossing it, but that
is a new definition and proof.  As written, G0(e) is proved only for the
nearest-neighbour D10 Hamiltonian, not the finite-range H4 class.

### 20. MAJOR — the two SKETCH boxes are not both non-load-bearing

**Steps:** `corner-a.md` ⟨1⟩4.⟨2⟩9 and `corner-a-kinks.md`
⟨1⟩10.⟨2⟩3; campaign uses in `claims/CLAIMS.md` and `docs/framing.md`.

The A1 split/normality sketch is load-bearing if `mathfrak a_alpha` is to be a
physical charge algebra acting on the relevant state space rather than a
formal matrix algebra; objections 4 and 8 show exactly where it is needed.
The A2 continuum-uniformity sketch is not needed for the pointwise fixed-`g`
sector statement, but it is load-bearing for any limit `g -> e`, Goldstone
cloud, or continuum-vacuum memory construction in M1.  The shard itself bans
using those sectors for Conjecture S, so no downstream claim may silently use
the boxed M1 interpretation while calling A2 fully closed.

## Surviving weaker result

After repair, the material supports the following narrower package:

1. WI telescopes with `V^{-1}` on the left and `V` on the right for windows
   containing those boundary bonds (or after boundary operators are defined).
2. For unbroken directions, half-string **state functionals** converge locally
   to a bond-decorated functional; non-scalar virtual residue obstructs strong
   convergence on the vacuum vector.  No physical twisted charge algebra or
   nontrivial endpoint-sector classification has yet been constructed.
3. For fixed broken `g`, finite strings stay in `K_{alpha,alpha}` and the
   half-string has a weak-* kink limit in `K_{alpha,g dot alpha}`; use a
   `tilde_lambda>lambda_E` rate and omit the false global `Acal` classification
   and undefined contact-term slogan.
4. The tensor tangent is gauge after normal ordering exactly for unbroken real
   Lie-algebra directions, while the FM broken spin flip is not.  The
   nearest-neighbour continuity equation is exact and reproduces O1, but no
   soft-scattering factor or O7/O9 universality follows without new Corner-C
   input.

FAIL(WI,A1,A2,G0)
