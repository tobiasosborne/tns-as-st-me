<!-- ROLE: blitz-lane proof shard for the full-chain part of tns-d51.
     All notation is inherited from definitions.md D13--D18 and notation.md.
     P and Q below are temporary proof labels, not new project notation. -->

# D51 lift: a uniform wall-leakage bound and the unresolved Mourre step

## 0. Result and honest status

**STATUS: PARTIAL.**  This shard does not prove D18 for the full D16 chain and
does not claim asymptotic completeness.  It gives an unreviewed Lamport proof
candidate for a uniform-in-time estimate
on the probability of the `>=5`-domain-wall complement for a bounded-energy
spectral packet.  On the projected Fano continuum the estimate is
`O(Delta^{-2})` in probability as `Delta -> infinity`.  It also gives the
exact below-threshold Feshbach self-energy bounds.  The estimate neither
constructs the full scattering channels nor proves local decay.

The proof uses D16, the PROVED claim **LR-D16-EDW**, and, only for its Fano-band
specialisation, the CONJECTURE **Mq-E** and the conditional claim **Mq-AD3**.
The D18 clauses remain hypotheses outside the projected graph.

## 1. Statement

Work in D16's spin-`1/2` kink sector on the finite-deviation core used by
claim LR-D16-EDW.  The kink boundary condition makes the domain-wall number
odd.  In this proof only, let `P` be the spectral projection of `N_DW` onto
`{1,3}` and let `Q=1-P`, hence `Q` is the projection onto `N_DW>=5`.  Put

`A=PHP`, `C=QHQ`, and `B=QHP`, with `H=H_XXZ`; `C` means the self-adjoint
operator associated with the compressed closed quadratic form.

These letters are local proof labels; the repository notation `P_3` and
`H_3=P_3HP_3` remains the one fixed in `notation.md`.

**THEOREM D51-U (uniform energy-window wall leakage).**

**ASSUME.**  D16 with `J>0`, `Delta>1`; a bounded interval
`I=[c-w,c+w]` with `w>=0` and

`c < a_5 := (5J/2)(Delta-1)`;

and a unit vector `Psi` in `Ran 1_I(H)`.

**PROVE.**  For every real `t`,

`||Q exp(-itH)Psi|| <= min{1,(w+beta)/(a_5-c)}`,

`<exp(-itH)Psi,Q exp(-itH)Psi>
 <= min{1,[(w+beta)/(a_5-c)]^2}`,

where `beta=3J/2`.  The constants are independent of volume and
scattering time.

If, additionally, `Delta>5/2` and Mq-E identifies the incoming projected
continuum with the Fano band

`I_F=[3JDelta/2-J, 3JDelta/2+J]`,

then every *full-H energy-filtered* packet with spectral support in `I_F`
obeys

`sup_t ||Q exp(-itH)Psi||^2
 <= min{1,[(5/2)/(Delta-5/2)]^2}`.                          (D51.1)

The last display is asymptotically `O(Delta^{-2})`.  It is not asserted for a
bare vector in `Ran P`: Mq-E concerns `PHP`, and does not prove that a bare
projected packet has full-H spectral support in `I_F`.

**PROPOSITION D51-F (closed-channel Feshbach bound).**

**ASSUME.**  The D51-U block setup and `z` with `Re z<a_5`.

**PROVE.**  The following resolvent and self-energy bounds.

For every `z` with `Re z<a_5`, `C-z` is invertible on `Ran Q`.  With the
temporary self-energy label

`Sigma(z)=B^*(C-z)^{-1}B`,

one has

`||Sigma(z)|| <= 9J^2/[4(a_5-Re z)]`,

`||partial_z Sigma(z)|| <= 9J^2/[4(a_5-Re z)^2]`.           (D51.2)

Whenever the displayed inverses exist,

`P(H-z)^{-1}P=[A-z-Sigma(z)]^{-1}`.                         (D51.3)

Thus the `>=5`-wall sector is a closed virtual channel below `a_5`, with an
operator-norm `O(J/Delta)` self-energy and `O(Delta^{-2})` energy derivative
on Fano-band compacta.  This conclusion alone is not a Mourre estimate.

## 2. Lamport proof of D51-U

**⟨1⟩1. PROVE.**  The off-diagonal wall-sector coupling is bounded uniformly
in volume by `||B||<=beta=3J/2`.

**⟨2⟩1.**  In the `S^z` configuration basis the Ising part of D16 preserves
`N_DW`, while an XY matrix element has magnitude `J/2` and is possible only
at an antiparallel bond.

*Justification.* D16 and the two-site block in claim **LR-D16-EDW**.

**⟨2⟩2.**  Swapping the two spins at such a bond leaves that bond a domain
wall and toggles the two adjacent wall indicators.  It therefore changes
`N_DW` by `-2`, `0`, or `+2`.

*Justification.* D16's nearest-neighbour XY term; the configuration identity
is independently enumerated by named computation **D51-CHECK** in
`d51_check.py`.

**⟨2⟩3.**  A three-wall configuration has at most three antiparallel bonds,
so its row in the bipartite `P`--`Q` coupling graph has degree at most three.
A configuration which couples directly back to `P` must have exactly five
walls.  A reducing move must be centred in a run of at least three adjacent
wall indicators.  Splitting five wall indicators into runs shows that at
most three of them can be such centres, so the column degree is at most three.

*Justification.* ⟨2⟩2 and named computation **D51-CHECK**; a run of length
`ell` has `max(ell-2,0)` reducing centres, whose sum at fixed total length
five is at most three.  Configurations with seven or more walls cannot reach
`{1,3}` in one D16 bond move.

**⟨2⟩4.**  The Schur row/column estimate for this weighted bipartite adjacency
matrix gives `||B|| <= (J/2)sqrt(3*3)=3J/2`.

*Justification.* D16, claim **LR-D16-EDW**, and ⟨2⟩1--⟨2⟩3; the Schur estimate follows by applying
Cauchy--Schwarz first to every row and then summing with the column-degree
bound.

**⟨2⟩5.**  The same finite-degree argument and the diagonal D16 energy show
that `A` is bounded.  The full off-diagonal part `B+B^*` is bounded by
⟨2⟩4.  Hence `H-(B+B^*)` is self-adjoint on `Dom H` by bounded perturbation
and is block diagonal; its restrictions are `A` and the self-adjoint
compressed operator `C`.  Thus `Dom H=Ran P direct-sum Dom C`, and the block
identity used below is valid on `Dom H`.

*Justification.* D16, ⟨2⟩1--⟨2⟩4, and the compressed-form meaning of `C` fixed
in Section 1.

**⟨2⟩6. QED.**

**⟨1⟩2. PROVE.**  `C>=a_5 Q` as a quadratic form.

**⟨2⟩1.**  Claim LR-D16-EDW gives
`H >= [J(Delta-1)/2]N_DW` on the finite-deviation core.

*Justification.* PROVED claim **LR-D16-EDW**, whose model input is D16.

**⟨2⟩2.**  On `Ran Q`, `N_DW>=5`; compression of ⟨2⟩1 by `Q` therefore gives
`QHQ >= (5J/2)(Delta-1)Q=a_5Q`.

*Justification.* Claim **LR-D16-EDW**, ⟨2⟩1, and the spectral definition of the temporary proof
projection `Q` in Section 1.

**⟨2⟩3. QED.**

**⟨1⟩3. PROVE.**  The first estimate of D51-U holds at `t=0`.

**⟨2⟩1.**  Since `Psi in Ran 1_I(H)` and `I=[c-w,c+w]`, spectral calculus
gives `||(H-c)Psi||<=w||Psi||` and places `Psi` in `Dom H`.

*Justification.* The spectral-window ASSUME clause of D51-U; D16 supplies the
self-adjoint dynamics.

**⟨2⟩2.**  Taking the `Q` component of `(H-c)Psi` gives the exact block
identity

`(C-c)QPsi=Q(H-c)Psi-B PPsi`.

*Justification.* The temporary block labels in Section 1 and D16.

**⟨2⟩3.**  By ⟨1⟩2 and `c<a_5`, `(C-c)^{-1}` exists with norm at most
`(a_5-c)^{-1}`.  Hence ⟨2⟩2, ⟨1⟩1, and ⟨2⟩1 give

`||QPsi|| <= (w+beta)/(a_5-c)||Psi||`.

*Justification.* D16, ⟨1⟩1, ⟨1⟩2, ⟨2⟩1--⟨2⟩2.

**⟨2⟩4.**  Orthogonality of `Q` also gives `||QPsi||<=||Psi||`; taking the
smaller of the two bounds proves the first display at `t=0`.

*Justification.* D16, ⟨2⟩3, and the projection property of `Q`.

**⟨2⟩5. QED.**

**⟨1⟩4. PROVE.**  Both estimates hold for every real `t`.

**⟨2⟩1.**  `exp(-itH)` commutes with `1_I(H)`, preserves the norm and preserves
`Ran 1_I(H)`.

*Justification.* D16's self-adjoint dynamics and the spectral-window ASSUME
clause of D51-U.

**⟨2⟩2.**  Apply ⟨1⟩3 to `Psi_t=exp(-itH)Psi`; every constant is independent
of `t`.

*Justification.* D16, ⟨1⟩3, and ⟨2⟩1.

**⟨2⟩3.**  Squaring the norm estimate gives the probability estimate because
`Q` is an orthogonal projection.

*Justification.* D16, ⟨2⟩2, and the projection property of `Q`.

**⟨2⟩4. QED.**

**⟨1⟩5. PROVE.**  The Fano-band specialisation is (D51.1).

**⟨2⟩1.**  Conditional on Mq-E, the incoming projected continuum has centre
`c=3JDelta/2` and half-width `w=J`.

*Justification.* CONJECTURE **Mq-E** and conditional claim **Mq-AD3**, as
displayed in `theory/memory-quantization.md` (Mq.7).

**⟨2⟩2.**  For `Delta>5/2`,
`a_5-c=J(Delta-5/2)>0`; substitution in ⟨1⟩4 gives (D51.1).

*Justification.* CONJECTURE **Mq-E**, ⟨1⟩2, ⟨1⟩4, and ⟨2⟩1.

**⟨2⟩3.**  The square in (D51.1) is `O(Delta^{-2})`; the estimate is uniform
in time but does not identify a full-H incoming spectral packet.

*Justification.* (D51.1), D18(AD1--AD2), and the explicit scope fence in the
statement of D51-U.

**⟨2⟩4. QED.**

**⟨1⟩6. QED.**

## 3. Lamport proof of D51-F

**⟨1⟩1. PROVE.**  The bounds (D51.2) hold.

**⟨2⟩1.**  For `Re z<a_5`, Section 2 ⟨1⟩2 gives
`||(C-z)^{-1}|| <= (a_5-Re z)^{-1}`.

*Justification.* D16, claim **LR-D16-EDW**, D51-U Section 2 ⟨1⟩2, and the spectral theorem applied to the
self-adjoint compression of D16's `H`.

**⟨2⟩2.**  Inserting `||B||^2<=9J^2/4` on both sides of the resolvent proves
the first bound in (D51.2).

*Justification.* D16, D51-U Section 2 ⟨1⟩1, and ⟨2⟩1.

**⟨2⟩3.**  Resolvent differentiation gives
`partial_z Sigma(z)=B^*(C-z)^{-2}B`; the same estimates prove the second
bound in (D51.2).

*Justification.* D16, ⟨2⟩1--⟨2⟩2, and direct differentiation of the resolvent
identity.

**⟨2⟩4. QED.**

**⟨1⟩2. PROVE.**  The Feshbach identity (D51.3) holds.

**⟨2⟩1.**  Relative to `Ran P direct-sum Ran Q`,
`H-z` has blocks `[[A-z,B^*],[B,C-z]]`.

*Justification.* The temporary block labels in Section 1 and D16.

**⟨2⟩2.**  Solving the lower block equation gives
`Q u=-(C-z)^{-1}B P u+(C-z)^{-1}Q f` for `(H-z)u=f`.

*Justification.* D16, ⟨1⟩1, and ⟨2⟩1.

**⟨2⟩3.**  Substitution into the upper equation gives the Schur complement
`A-z-B^*(C-z)^{-1}B=A-z-Sigma(z)` and hence (D51.3).

*Justification.* D16 and ⟨2⟩1--⟨2⟩2.

**⟨2⟩4. QED.**

**⟨1⟩3. QED.**

## 4. Exact residue to full D18

### 4.1 Why a small self-energy is not a uniform dynamics comparison

The estimate proved above controls the `Q` weight of a *full-H
energy-filtered* packet.  It does not prove
`sup_t ||exp(-itH)Psi-exp(-itA)Psi||=O(Delta^{-1})`.  Such a target is false
even for a scalar self-energy: replacing `A` by `A+epsilon` changes the
evolution by the phase `exp(-it epsilon)`, whose norm difference reaches two
at times of order `1/|epsilon|`.  D51-F gives precisely an `O(J/Delta)`
energy correction, so its phase can accumulate on scattering times.

The forward attack must therefore construct a **dressed effective channel**
and compare scattering states, not compare the bare propagators uniformly in
operator norm.  D18(AD1) is formulated in exactly that wave-operator register.

### 4.2 The missing projected-resolvent/Mourre estimate

Let `P_F` denote the incoming Fano cyclic component supplied only under Mq-E,
and let `P_o=P-P_F` contain the other `{1,3}`-wall components.  This split is
essential: eliminating `Q` produces `Sigma(z)` on *all* of `Ran P`; virtual
five-wall paths can couple `P_F` to `P_o`.  The norm bound (D51.2) neither
makes that coupling zero nor proves that `P_o` has no on-shell continuum.

For a compact interval `I` in the interior of the projected Fano band and
also below `a_5` (the whole projected band is below `a_5` only when
`Delta>7/2`), the exact next estimate is the weighted limiting-absorption
bound

`sup_{E in I, 0<eta<=1}
 ||<X>^{-s}P_F[A-E-i eta-Sigma(E+i eta)]^{-1}P_F<X>^{-s}||
 < infinity`,                                                   (D51-M)

for some `s>1/2`, with `X` the relative coordinate on `Ran P_F` carried by
Mq-E.
It must be accompanied by one of the following mutually exclusive channel
conclusions:

1. **exclusion:** `P_o[A-z-Sigma(z)]^{-1}P_F` has no boundary-value
   singularity on `I`; or
2. **inventory:** every singular `P_o` boundary component is added to
   `H_as` as an extra propagating channel.

The first route is required to prove D18(AD1)'s present two-tail statement
with “no further propagating channel.”  The second route changes the D18
instance and the downstream two-channel displacement observable, so it
cannot be silently substituted.

A concrete Mourre route to (D51-M) is to decompose the self-energy into a
tail-translation-invariant part and a short-range remainder,

`Sigma(E+i0)=Sigma_as(E)+K(E)`,                                  (D51-SR)

then prove, uniformly for `E in I`: (i) the renormalised tail dispersion has
group velocity bounded away from zero; (ii) `K(E)` and its first two
commutators with the Jacobi conjugate operator are compact/short-range; and
(iii) there is no embedded eigenvalue or threshold resonance.  Those are
the missing estimates, not consequences of the operator-norm bound (D51.2).

Once (D51-M), (D51-SR), the channel exclusion/inventory, and the Mq-E local
observable map are supplied, the remaining standard stationary-scattering
steps target D18 as follows: boundary values give local decay for smooth
packets away from thresholds (AD3); the renormalised comparison dynamics
gives wave operators and their range (AD1--AD2); and D18 fixes the limit
order (AD4).  None of these implications is claimed proved in this lane.

### 4.3 What has and has not moved

**Established:** the coupling across the `3/5`-wall boundary has a
volume-independent norm; the five-wall compression has a rigorous energy
floor; energy-filtered full evolution consequently has uniform-in-time
`O(Delta^{-2})` five-wall probability at large anisotropy; and the closed
sector contributes an analytic, quantitatively bounded Feshbach self-energy.

**Still open:** Mq-E itself; preparation of the full-H spectral packet from a
projected incoming packet; the weighted estimate (D51-M); exclusion or
inventory of other on-shell `{1,3}`-wall components; full wave-operator
completeness; D18(AD3) local charge decay; and all `Delta` near the isotropic
point where the wall-energy threshold does not close the higher channel.

## 5. Red-capable check

Named computation **D51-CHECK** is `d51_check.py`.  On all opposite-tail open
chains with 6 through 12 dynamical spins it enumerates every configuration
and every D16 XY move.  The green record `d51_check.out` reports wall changes
only in `{-2,0,2}`, cross-boundary maximum degrees `(3,3)`, and the Schur
constant `beta/J=1.5`.  The mutation `--red` replaces the row-degree bound
three by two; `d51_check_red.out` records the expected exit code one when a
degree-three configuration is encountered.  This checks the finite graph
identity and mutation sensitivity only; it does not test the spectral or
infinite-time theorem.
