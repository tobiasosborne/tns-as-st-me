# BA-MM-fin — exact finite-window moment map on the D16 kink family

**SELF-STATUS: SKETCH.**  The core finite-window identity is proved exactly
below.  Promotion is reserved for the capped L6 review.  Two ancillary clauses
of the campaign rung require correction before promotion; they are isolated in
§4 rather than silently strengthened.

**BINDING FENCE.**  This is rung L1 only, on D16's `χ=1` product family.  It
does **not** close the `B => A` edge, supplies no evidence for `χ>1`, asserts no
sector-wide charge operator, and licenses **no paper claim**.  No Hamiltonian,
TDVP trajectory, scattering hypothesis, or infinite-window limit is used.

**PROVENANCE FENCE.**  The observation that TNS variational classes carry a
Kähler structure and that TDVP is the associated Hamiltonian flow originated
with Tobias Osborne, who communicated it to Jutho Haegeman, who made it work.
This provenance must not appear in a paper without Tobias Osborne's explicit
sign-off.  The present shard is repository-internal and makes no paper-scope
recommendation.

## 0. Statement and the necessary lift convention

Fix D16, a nonempty finite window `W=[a,b]`, and `c_0 in W`.  Thus `s=1/2`,
`q=Delta-sqrt(Delta^2-1) in (0,1)`, and

`z=q^{-x_0}e^{i phi}`,  `kappa:=-log q>0`.

The physical state is represented site by site by the normalised ray

`(|up>_n+zq^n|down>_n)/sqrt(1+|z|^2q^{2n})`.

For the Fubini--Study potential one must use the holomorphic lift of that same
ray,

`|Psi_W(z)> := tensor_{n=a}^b (|up>_n+zq^n|down>_n)`.

This is not a second state definition: multiplication of each site vector by
its positive norm leaves the product ray, hence its normalised state,
unchanged.  It is a necessary reading of the campaign target's proposed
D32(b).  If `log ||.||^2` were applied literally to the already normalised
vector, it would be identically zero and could not be a Fubini--Study
potential.  The state-normalised representative is used below for
expectations; the holomorphic representative is used for the curvature.

For the following calculation-only abbreviations,

`r_n(x_0):=|z|^2q^{2n}=exp(2kappa(x_0-n))`,
`u_n(x_0):=(1+r_n(x_0))^{-1}`,

the exact formulas are

`mathfrak{k}_W = sum_{n=a}^b log(1+r_n)`,                       (BA.1)

`varpi_W = Omega_W(x_0) dx_0 wedge dphi`,
`Omega_W = 2kappa sum_{n=a}^b r_n/(1+r_n)^2 > 0`,              (BA.2)

`mu_W = rho_{x_0,phi}(Qhat_{W,c_0})
      = a-1-c_0 + sum_{n=a}^b u_n`,                            (BA.3)

and therefore

`d mu_W = -Omega_W dx_0 = iota_{partial_phi} varpi_W`.         (BA.4)

All sums in (BA.1)--(BA.4) are finite.  In particular, (BA.4) has no transfer,
window-edge, thermodynamic, or dynamical remainder.

## 1. Structured proof of the exact identity

### ⟨1⟩1. Compute the one-site norm and frozen-charge expectation

**ASSUME.**  D16, `W=[a,b]`, `c_0 in W`, and the two representatives fixed in
§0.

**PROVE.**  Equations (BA.1) and (BA.3).

#### ⟨2⟩1. The squared norm of the holomorphic factor at site `n` is
`1+r_n`.

*Justification.*  D16 gives the factor
`|up>_n+zq^n|down>_n` and orthonormal spin basis vectors.  Its squared norm is
`1+|z|^2q^{2n}`; D16's `z=q^{-x_0}e^{i phi}` gives `r_n` as written in §0.
This is also the input independently accumulated by the geometry route in
`check_ba_mm_fin.py`.

#### ⟨2⟩2. The window lift has
`log <Psi_W|Psi_W> = sum_{n=a}^b log(1+r_n)`.

*Justification.*  D16 makes the kink a product family, so finite-window norms
multiply.  Taking the logarithm and using ⟨2⟩1 gives (BA.1).  This is the
proposed D32(b) potential evaluated on D16's holomorphic window lift.

#### ⟨2⟩3. In the normalised one-site state,

`rho(S^z_n)= (1-r_n)/(2(1+r_n))`, and
`rho(S^z_n+1/2)=u_n`.

*Justification.*  D16 fixes `s=1/2` and the amplitudes of the `S^z=+1/2`
and `S^z=-1/2` basis vectors.  Dividing their squared weights `1` and `r_n`
by `1+r_n` gives both displayed identities.  The independent observable route
in `check_ba_mm_fin.py` constructs the same expectation directly from these
normalised probabilities.

#### ⟨2⟩4. D13(a) and `(IDX.1)` give (BA.3).

*Justification.*  D13(a) freezes

`mathfrak{X}_W=a-1+(1/(2s))sum_{n=a}^b(S^z_n+s)`.

The PROVED claim **M-INDEX-fin** records `(IDX.1)`,
`Qhat_{W,c_0}=2s(mathfrak{X}_W-c_0)`.  At D16's `2s=1`, taking the product
state expectation and applying ⟨2⟩3 yields
`mu_W=a-1-c_0+sum_n u_n`.  Neither the cut nor `phi` occurs in a derivative.

#### ⟨2⟩5. QED for ⟨1⟩1.

*Justification.*  Equations (BA.1) and (BA.3) are ⟨2⟩2 and ⟨2⟩4,
respectively; both use only D13(a), D16, and **M-INDEX-fin**.

### ⟨1⟩2. Compute the windowed Kähler form

**ASSUME.**  The hypotheses of ⟨1⟩1 and the proposed D32(c) convention
`varpi_W=i partial partialbar mathfrak{k}_W`.

**PROVE.**  Equation (BA.2), including positivity and `U(1)` invariance.

#### ⟨2⟩1. In the holomorphic coordinate `z`,

`partial_z partial_zbar log(1+q^{2n}z zbar)
 = q^{2n}/(1+q^{2n}|z|^2)^2`.

*Justification.*  Differentiate the finite elementary function from
⟨1⟩1.⟨2⟩1 once in `zbar` and once in `z`.  This leaf is mirrored by the
mixed-derivative accumulation in the named computation
`check_ba_mm_fin.py::omega_geometry`.

#### ⟨2⟩2. The coordinate change in D16 obeys

`i dz wedge dzbar = 2kappa |z|^2 dx_0 wedge dphi`.

*Justification.*  From D16 and §0,
`z=e^{kappa x_0+i phi}`.  Hence
`dz=z(kappa dx_0+i dphi)` and
`dzbar=zbar(kappa dx_0-i dphi)`; direct exterior multiplication gives the
display.  The sign agrees with the orientation registered in
`check_ba_mm_fin.py::omega_geometry`.

#### ⟨2⟩3. Combining ⟨2⟩1 and ⟨2⟩2 gives

`varpi_W = [2kappa sum_{n=a}^b r_n/(1+r_n)^2]
            dx_0 wedge dphi`.

*Justification.*  Sum the mixed derivatives from ⟨2⟩1, multiply by the
two-form in ⟨2⟩2, and use `r_n=|z|^2q^{2n}` from D16 and §0.  The sum is
finite, so termwise differentiation is unconditional.

#### ⟨2⟩4. `Omega_W>0` everywhere, and `varpi_W` is Kähler, symplectic,
and `U(1)`-invariant.

*Justification.*  D16 gives `kappa>0`, and every `r_n` is strictly positive.
Since `W` is nonempty, every summand in (BA.2) is positive.  Thus the
coefficient of `dx_0 wedge dphi` never vanishes on the two-dimensional
cylinder.  It is closed either from its `i partial partialbar` construction or
directly because `d(Omega_W dx_0 wedge dphi)=0`.  The mixed coefficient in
⟨2⟩1 is positive, so this real `(1,1)` form is positive for the complex
coordinate `z` and hence Kähler.  Equation (BA.2) depends on `x_0` but not on
`phi`, proving invariance under the target's selected circle
`phi -> phi+theta`.  Positivity is also gated on 3,536 cases by the named
computation `check_ba_mm_fin.py`.

#### ⟨2⟩5. QED for ⟨1⟩2.

*Justification.*  ⟨2⟩3 is (BA.2), and ⟨2⟩4 proves its asserted geometric
properties from D16 and the named checker.

### ⟨1⟩3. Differentiate the frozen memory observable

**ASSUME.**  Equation (BA.3) from ⟨1⟩1.

**PROVE.**  `partial_{x_0}mu_W=-Omega_W` and `partial_phi mu_W=0`.

#### ⟨2⟩1. Each D16 weight satisfies

`partial_{x_0}r_n=2kappa r_n`, and
`partial_{x_0}u_n=-2kappa r_n/(1+r_n)^2`.

*Justification.*  D16 and §0 give
`r_n=exp(2kappa(x_0-n))` and `u_n=(1+r_n)^{-1}`.  Direct differentiation
gives both formulas.  The named computation
`check_ba_mm_fin.py::dmu_observable` differentiates the independently
assembled D13(a) expectation by complex step rather than calling the
geometry formula.

#### ⟨2⟩2. `partial_{x_0}mu_W=-Omega_W`.

*Justification.*  Differentiate the finite sum in (BA.3), use ⟨2⟩1, and
compare with (BA.2).  The scalar `a-1-c_0` differentiates to zero.  This uses
D13(a), D16, and no asymptotic estimate.

#### ⟨2⟩3. `partial_phi mu_W=0`.

*Justification.*  By D16, the normalised probabilities depend on `z` only
through `|z|^2=q^{-2x_0}`.  Equation (BA.3) therefore contains no `phi`.

#### ⟨2⟩4. QED for ⟨1⟩3.

*Justification.*  The two requested derivatives are ⟨2⟩2 and ⟨2⟩3, derived
from D13(a) and D16 and independently exercised by `check_ba_mm_fin.py`.

### ⟨1⟩4. Prove the exact moment-map identity

**ASSUME.**  The target fixes the fundamental vector field to be
`xi^sharp=partial_phi`.

**PROVE.**  `dmu_W=iota_{xi^sharp}varpi_W` identically at finite `W`.

#### ⟨2⟩1. `dmu_W=-Omega_W dx_0`.

*Justification.*  Expand the differential and apply
⟨1⟩3.⟨2⟩2--⟨2⟩3.  The source inputs of those leaves are D13(a) and D16.

#### ⟨2⟩2. `iota_{partial_phi}varpi_W=-Omega_W dx_0`.

*Justification.*  Insert `partial_phi` into (BA.2):
`iota_{partial_phi}(dx_0 wedge dphi)=-dx_0`.  Equation (BA.2) was proved from
D16 in ⟨1⟩2 and is independently evaluated by
`check_ba_mm_fin.py::omega_geometry`.

#### ⟨2⟩3. The equality has no remainder of any kind.

*Justification.*  The two sides in ⟨2⟩1--⟨2⟩2 are the identical finite sum
`-2kappa sum_{n=a}^b r_n/(1+r_n)^2 dx_0`.  No invocation of D1(c), a transfer
limit, or a window enlargement occurs; the only source definitions are D13(a)
and D16.

#### ⟨2⟩4. QED for ⟨1⟩4.

*Justification.*  Equality follows term by term from ⟨2⟩1 and ⟨2⟩2; exactness
is ⟨2⟩3.  This proves the core claim **BA-MM-fin** at prover status.

### ⟨1⟩5. QED for the theorem in §0

**ASSUME.**  D13(a), D16, the target's proposed D32(b,c)/D34(a,b)
conventions, and `xi^sharp=partial_phi`.

**PROVE.**  (BA.1)--(BA.4), positivity, invariance, and finite-window
exactness.

*Justification.*  ⟨1⟩1 proves (BA.1),(BA.3); ⟨1⟩2 proves (BA.2), positivity,
and invariance; ⟨1⟩3--⟨1⟩4 prove (BA.4) with no remainder.  Every source leaf
is D13(a), D16, **M-INDEX-fin**, or the named computation
`check_ba_mm_fin.py`.  QED.

## 2. What “conjugate pair” is proved to mean

The exact identity makes the D16 terminology rigorous in the following
precise sense: `(x_0,phi)` are global symplectic coordinates on the cylinder,
and `x_0` is a strictly monotone reparameterisation of the canonical momentum
`mu_W` conjugate to `phi`.  The raw coordinate `x_0` is not unit-normalised
Darboux momentum at finite `W`.

### ⟨1⟩1. Establish the Darboux coordinate and the brackets

**ASSUME.**  The campaign target's proposed D33(b) convention
`iota_{X_f}varpi_W=df` and `{f,g}_{varpi_W}=varpi_W(X_f,X_g)`.

**PROVE.**  `(phi,mu_W)` is a Darboux pair, while the literal bracket sentence
in advertised L1.c must be reversed.

#### ⟨2⟩1. `x_0 -> mu_W(x_0)` is strictly decreasing, and

`varpi_W=dphi wedge dmu_W`.

*Justification.*  By ⟨1⟩3, `dmu_W=-Omega_W dx_0`; by ⟨1⟩2,
`Omega_W>0`.  Therefore the derivative never vanishes, and
`Omega_W dx_0 wedge dphi=dphi wedge dmu_W`.  Both inputs ultimately cite
D13(a) and D16.

#### ⟨2⟩2. The Hamiltonian vector fields are

`X_{mu_W}=partial_phi`,
`X_phi=Omega_W^{-1}partial_{x_0}`, and
`X_{x_0}=-Omega_W^{-1}partial_phi`.

*Justification.*  Insert each displayed vector into (BA.2), using
`iota_{partial_phi}(dx_0 wedge dphi)=-dx_0` and
`iota_{partial_{x_0}}(dx_0 wedge dphi)=dphi`.  Match the results to
`dmu_W=-Omega_Wdx_0`, `dphi`, and `dx_0`, respectively.  The required
nonvanishing of `Omega_W` is ⟨1⟩2, proved from D16.

#### ⟨2⟩3. Consequently,

`{phi,mu_W}_{varpi_W}=1`,
`{x_0,mu_W}_{varpi_W}=0`, and
`{x_0,phi}_{varpi_W}=Omega_W^{-1}`.                            (BA.5)

*Justification.*  Substitute the three vector fields from ⟨2⟩2 into the
target's bracket convention.  Evaluation in (BA.2) gives the three values.
This is an algebraic consequence of D16 and the exact identity ⟨1⟩4.

#### ⟨2⟩4. QED for the conjugacy statement.

*Justification.*  ⟨2⟩1 proves that `mu_W` is the momentum coordinate
canonically paired with `phi`; ⟨2⟩3 gives the unit Darboux bracket.  Since
`x_0` is a global strictly monotone coordinate along `mu_W`, D16's phrase
“conjugate pair `(x_0,phi)`” is valid as a non-canonically normalised
symplectic-coordinate statement.  It is **not** the literal L1.c display
`{x_0,mu_W}=1`, `{phi,mu_W}=0`, which (BA.5) disproves.  QED.

## 3. Exact finite-window period and the edge correction

This section is included because the campaign rung calls its one-period area
exact at finite `W`.  The exact calculation shows that assertion is false for
a fixed finite window; the advertised value is recovered only after the window
edges leave the kink.

### ⟨1⟩1. Compute the one-period area

**ASSUME.**  D16 and a fixed finite `W=[a,b]`.

**PROVE.**  For every finite `x_0`,

`int_{x_0}^{x_0+1} int_0^{2pi} varpi_W
 =2pi [u_b(x_0)-u_{a-1}(x_0)]`,                               (BA.6)

which is strictly between `0` and `2pi`.

#### ⟨2⟩1. `u_n(x_0+1)=u_{n-1}(x_0)`.

*Justification.*  D16 and §0 give
`u_n(x)=[1+exp(2kappa(x-n))]^{-1}`.  Replacing `x` by `x+1` gives the
displayed index shift exactly.

#### ⟨2⟩2. `mu_W(x_0)-mu_W(x_0+1)=u_b(x_0)-u_{a-1}(x_0)`.

*Justification.*  Apply ⟨2⟩1 to the finite sum (BA.3):
`sum_{n=a}^b u_n(x+1)=sum_{m=a-1}^{b-1}u_m(x)`.  Subtraction telescopes.
The cut-dependent scalar cancels exactly, as also required by the PROVED
claim **M-INDEX-fin**.

#### ⟨2⟩3. Equation (BA.6) holds.

*Justification.*  Integrate (BA.4):
`int_{x}^{x+1}Omega_W(y)dy=mu_W(x)-mu_W(x+1)`.  The `phi` integral contributes
`2pi`, and ⟨2⟩2 supplies the endpoint expression.  The inputs are D13(a),
D16, and **M-INDEX-fin**.

#### ⟨2⟩4. The factor in brackets is strictly between zero and one.

*Justification.*  From D16's `kappa>0`, `0<u_n<1` at finite arguments, and
`u_n` is strictly increasing with the site index `n`.  Since
`b>a-1`, `0<u_b-u_{a-1}<1`.  Thus a fixed finite window never has exactly
the advertised area `2pi*2s=2pi` at D16's `s=1/2`.

#### ⟨2⟩5. The target normalisation is recovered with explicit edge defect.

*Justification.*  The deficit from one is
`[1-u_b(x_0)]+u_{a-1}(x_0)`, the sum of the two D16 logistic tail weights.
It tends to zero when `b-x_0 -> +infinity` and `x_0-a -> +infinity`.
Equivalently,
`mu_W(x_0+1)-mu_W(x_0)=-1` up to exactly those two edge terms.  This is the
finite-window correction anticipated qualitatively by D13(a), now computed
without invoking D1(c).

#### ⟨2⟩6. QED for ⟨1⟩1.

*Justification.*  ⟨2⟩3 proves the exact formula, ⟨2⟩4 refutes exact unit area
at finite `W`, and ⟨2⟩5 supplies the surviving edge-corrected statement from
D13(a) and D16.  QED.

## 4. Adjudication-critical corrections to the advertised rung

The exact core (L1.a--L1.b) survives.  The following corrections are necessary
before any shared claim row can be proposed.

1. **Holomorphic-lift correction.**  “Site-normalised family” specifies the
   state map and the expectation in (BA.3).  The potential in proposed D32(b)
   must be the norm of a local nonzero **holomorphic lift** of those rays.  The
   norm of the normalised representative is one and has zero curvature.

2. **Bracket correction.**  With the target's own convention
   `iota_{X_f}varpi=df`, L1.c's brackets are reversed.  The exact result is
   (BA.5): `{phi,mu_W}=1` and `{x_0,mu_W}=0`.  The raw D16 pair
   `(x_0,phi)` is a non-canonically normalised symplectic pair;
   `(phi,mu_W)` is the Darboux pair.

3. **Finite-period correction.**  L1.d's first sentence is not exact at fixed
   finite `W`.  Its exact replacement at `s=1/2` is (BA.6).  The value `2pi`
   is approached only when both edges recede, with explicit defect
   `2pi([1-u_b]+u_{a-1})`.  The sign in the chosen D16 orientation is
   `mu_W(x_0+1)-mu_W(x_0) -> -1`.

These are repairs to the target statement, not loopholes in (BA.4).  In
particular, neither correction introduces a remainder into the finite-window
moment-map identity.

## 5. Checker specification and recorded runs

The red-capable certificate is `check_ba_mm_fin.py` in this lane directory.
It uses only Python, NumPy, D13(a), and D16.

### ⟨1⟩1. Green certificate

**ASSUME.**  D16 on the registered grid

- `Delta in {1.05,1.5,2,4}`;
- 221 values of `x_0` in `[-2.25,3.25]`;
- four fixed windows, including asymmetric windows and nonzero cuts.

**PROVE.**  The two independently programmed routes agree within the fixed
tolerance and `Omega_W` stays positive.

#### ⟨2⟩1. The geometry route does not call the observable route.

*Justification.*  `omega_geometry` differentiates
`log product_n(1+q^{2n}|z|^2)` in `z,zbar` and then converts
`i dz wedge dzbar` to `dx_0 wedge dphi`.  This is the named computation
`check_ba_mm_fin.py::omega_geometry`, based on D16.

#### ⟨2⟩2. The observable route does not call the geometry route.

*Justification.*  `mu_observable` assembles the D13(a)/(IDX.1) expectation
from normalised one-site up probabilities; `dmu_observable` differentiates it
by complex step at `h=10^{-30}`.  This is the named computation
`check_ba_mm_fin.py::dmu_observable`, based on D13(a), D16, and
**M-INDEX-fin**.

#### ⟨2⟩3. The green run passes.

*Justification.*  The saved named computation `checker-green.txt` records
exit code `0`, 3,536 cases, maximum absolute residual
`8.881784e-16`, maximum tolerance-scaled residual `4.037175e-04`, and
minimum `Omega_W=3.890260e-04>0`.

#### ⟨2⟩4. QED for ⟨1⟩1.

*Justification.*  Independence is ⟨2⟩1--⟨2⟩2 and the registered decision is
⟨2⟩3.  This is numerical corroboration only; the proof for all admissible
parameters and finite windows is ⟨1⟩1--⟨1⟩5 above.  QED.

### ⟨1⟩2. Red certificate

**ASSUME.**  Mutate only the D13(a) outer calibration from `2s` to `2s+1`,
which is `1 -> 2` at D16's `s=1/2`; leave the geometry route unchanged.

**PROVE.**  The checker fires.

#### ⟨2⟩1. The mutation doubles `partial_{x_0}mu_W` but not `Omega_W`.

*Justification.*  `mu_observable` applies the mutable outer multiplier only
after assembling the D13(a) expectation.  `omega_geometry` has no calibration
argument.  These are the separate named routes in `check_ba_mm_fin.py`.

#### ⟨2⟩2. The red run exits `1` with `RED-OK`.

*Justification.*  The saved named computation `checker-red.txt` records
maximum absolute residual `1.162866`, positive unchanged geometry, the message
`RED-OK: mutated calibration was caught`, and exit code `1`.

#### ⟨2⟩3. QED for ⟨1⟩2.

*Justification.*  ⟨2⟩1 isolates the intended mutation and ⟨2⟩2 demonstrates
that it reaches the identity gate.  The checker is red-capable.  QED.

## 6. Honest status

- **Established exactly:** on every D16 parameter `Delta>1`, every nonempty
  finite `W`, every `c_0 in W`, and every `(x_0,phi)`, the holomorphic-lift
  Fubini--Study form is positive and satisfies
  `dmu_W=iota_{partial_phi}varpi_W`, with no remainder.
- **Established exactly:** `(phi,mu_W)` is Darboux; `(x_0,phi)` is a global,
  non-canonically normalised symplectic coordinate pair because
  `partial_{x_0}mu_W<0` everywhere.
- **Refuted as written:** the two brackets in advertised L1.c, and exact unit
  symplectic area for a fixed finite window in L1.d.  Equations (BA.5)--(BA.6)
  are the surviving sharp replacements and name the forward repair.
- **Not established:** any `chi>1` claim, any infinite-window construction,
  a sector operator, dynamics, scattering, reduction, the `B=>A` edge, or a
  statement suitable for `paper/`.
- **Self-status remains SKETCH** pending the campaign's one critic round and
  orchestrator adjudication.  No shared-file patch was made or requested.
