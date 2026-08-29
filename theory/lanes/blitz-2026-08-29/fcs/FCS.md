# Full counting statistics of the D27 TPM memory law

## 0. Result and scope

This shard answers the lane question without introducing a channel inventory.
To respect `notation.md`'s binding bare-`χ` rule, the characteristic function
is always written explicitly as `Σ_ν p_ν exp(iλν)`; the brief's bare
`χ(λ)` is not imported into the repository notation.

The positive result has three parts.

1. D27 gives an exact finite-window counting-field identity, including exact
   formulas for every raw moment and a particularly useful pinched
   second-moment formula.
2. M-INDEX-spec fixes the complete model-independent limit information:
   integer support, positivity, `2π` periodicity, and the first cumulant
   `Σ_ννp_ν=-2sδx`.  D27 guarantees no second moment; higher cumulants need
   not exist, much less be universal.
3. For finite number-conserving quadratic fermions in a gauge-invariant
   quasifree state, the same TPM law has an exact determinant formula.  If
   the first measurement disturbs the state, the formula includes one compact
   phase average implementing the D27 pinching.  This is a genuine free
   comparator, not D16: D16 has `Δ>1`, whose Jordan--Wigner density-density
   interaction prevents the quadratic determinant reduction.

Self-status: **SKETCH**.  The algebra below is complete and the finite-Fock
checker is red-capable, but this blitz artifact has not passed the capped L6
hostile review required for a `PROVED` label.

---

## 1. Exact finite-window FCS

### ⟨1⟩1. THEOREM FCS-TPM (counting-field and moment identities)

**ASSUME.** D27 at one fixed finite window `W` and finite times
`t_-<t_+`.  Write `Q_-:=Q̂_{W,c_0}(t_-)`,
`Q_+:=Q̂_{W,c_0}(t_+)`, and use D27's `E_{W,t_-}` and
`𝒟_{W,t_-}`.  The escaped-charge sign is D27's
`ν=q_-−q_+`.

**PROVE.** For every real `λ`,

`Σ_ν p_{W;t_-,t_+}(ν)e^{iλν}
 = ⟨Ψ, 𝒟_{W,t_-}(e^{-iλQ_+})e^{iλQ_-}Ψ⟩`.       **(FCS.1)**

For every integer `n≥0`,

`Σ_ν ν^n p_{W;t_-,t_+}(ν)
 = Σ_q ⟨Ψ,E_{W,t_-}({q})(q-Q_+)^nE_{W,t_-}({q})Ψ⟩`. **(FCS.2)**

In particular,

`Σ_ννp(ν)=⟨Q_-⟩-⟨𝒟_{W,t_-}(Q_+)⟩`,             **(FCS.3)**

`Σ_νν²p(ν)=⟨Ψ,𝒟_{W,t_-}((Q_+-Q_-)²)Ψ⟩`.         **(FCS.4)**

No commutator of `Q_-` and `Q_+` is assumed to vanish.

**⟨2⟩1.** Expand the D27 TPM law over its initial and final spectral
resolutions and weight each term by `e^{iλ(q-q')}`.

*Justification.* D27(LR1)'s displayed finite-window law and M-INDEX-fin's
fixed-window offset cancellation; the numerical equality is independently
checked by `fcs_check.py` **FCS-C1**.

**⟨2⟩2.** Summing the final spectral resolution gives `e^{-iλQ_+}`;
on `E_{W,t_-}({q})`, the other phase is `e^{iλq}`.  Summing `q` is exactly
the D27 pinching followed by `e^{iλQ_-}`, proving (FCS.1).

*Justification.* D27's definitions of `E_{W,t}` and `𝒟_{W,t}`; checker
`fcs_check.py` **FCS-C1**.

**⟨2⟩3.** Differentiating the finite spectral sum `n` times at `λ=0`
gives (FCS.2), and `n=1` gives (FCS.3).

*Justification.* The spectrum is finite because `Q̂_{W,c_0}∈𝔄_W` is a
bounded local observable (D27 and the `Q̂_{W,c}` row of `notation.md`);
`fcs_check.py` **FCS-C3** checks (FCS.3).

**⟨2⟩4.** For `n=2`, inserting the initial spectral projections on both
sides turns each occurrence of `Q_-` at an endpoint into the scalar `q`.
Expanding the square therefore identifies (FCS.2) with (FCS.4).

*Justification.* D27's spectral resolution; `fcs_check.py` **FCS-C4**.

**⟨2⟩5. QED.**

**Noncommutative warning.**  Formula (FCS.4) is special to order two.
For `n≥3`, (FCS.2) is the safe formula: replacing it by
`⟨𝒟_{W,t_-}((Q_--Q_+)^n)⟩` silently inserts noncommuting `Q_-` factors
between `Q_+` factors.  D27 explicitly assumes only a first-moment
nondemolition condition, not asymptotic commutativity.

### ⟨1⟩2. COROLLARY FCS-FLUX (the noise datum exposed)

**ASSUME.** The hypotheses of ⟨1⟩1 and the finite-time continuity equation.

**PROVE.** The second raw moment is the D27-pinched quadratic fluctuation of
the time-integrated two-edge current.  Hence window-charge conservation
reduces the second cumulant to a current-current datum but does not fix it.

**⟨2⟩1.** The finite-window continuity equation writes `Q_+-Q_-` as the
time integral of the difference of the two cut currents at the endpoints of
`W` (with the sign fixed by the choice of inward versus outward current).

*Justification.* D10(b) and claim M-flux; the scalar `-2sc_0` in D27's
`Q̂_{W,c_0}` is time independent.

**⟨2⟩2.** Substitution in (FCS.4) expresses `Σ_νν²p(ν)` as the pinched
expectation of the square of that integrated current, equivalently a double
time current-current correlation in the post-first-measurement state.

*Justification.* ⟨1⟩1 (FCS.4), D27's pinching map, and `fcs_check.py`
**FCS-C4**.

**⟨2⟩3.** D27(LR2) constrains only the first-moment dephasing defect, while
D27(LR3) asks only first-moment tightness.  Neither hypothesis supplies the
current-current correlation in ⟨2⟩2.

*Justification.* D27(LR2--LR3), verbatim; claim M-INDEX-spec records exactly
that conditional scope.

**⟨2⟩4. QED.**

This identifies a concrete forward attack: prove a limit for the pinched
edge-current two-point function (or a stronger uniform second-moment bound).
The existing `lr-d16.md` route uses precisely such a bound to imply LR3, but
its D16 no-unbounded-content input remains conditional; the PROVED
LR-D16-EDW row controls the number of domain walls, not the length of a
wrong-phase block.

---

## 2. What survives in the ordered limit

### ⟨1⟩3. THEOREM FCS-UNIV (complete law-level consequences)

**ASSUME.** The hypotheses of claim M-INDEX-spec and one of its D27(LR3)
subsequential ordered laws `p`.

**PROVE.** Writing every formula explicitly rather than assigning a new
symbol to the characteristic function:

1. `Σ_νp_νe^{iλν}` is continuous, `2π`-periodic, equals `1` at `λ=0`,
   obeys complex-conjugation symmetry, has modulus at most one, and is
   positive definite.
2. It is continuously differentiable once and
   `-i(d/dλ)|_{λ=0}Σ_νp_νe^{iλν}=Σ_ννp_ν=-2sδx`.
3. If the variance is finite and `r` is the fractional part of
   `μ:=Σ_ννp_ν`, then
   `Var_p(ν)≥r(1-r)`, with equality exactly for a law supported on the two
   adjacent integers `⌊μ⌋,⌈μ⌉` (one integer if `r=0`).
4. M-INDEX-spec alone guarantees no second cumulant: an allowed
   integer-supported probability can have finite absolute first moment and
   infinite second moment.  Even when every moment exists, support plus the
   calibrated first moment does not determine any higher cumulant.

**⟨2⟩1.** Every ordered limit law is a probability on `ℤ` and has a finite
absolute first moment.

*Justification.* Claim M-INDEX-spec and D27(LR3)'s `(1+|ν|)` tightness.

**⟨2⟩2.** Normalisation, conjugation symmetry and the modulus bound follow
termwise.  Integer support gives `2π` periodicity.  For arbitrary real
`λ_1,…,λ_k` and complex `z_1,…,z_k`,

`Σ_{a,b}\bar z_a z_b Σ_νp_νe^{i(λ_a-λ_b)ν}
 = Σ_νp_ν |Σ_a z_ae^{-iλ_aν}|² ≥0`,

so the function is positive definite.

*Justification.* M-INDEX-spec's positivity and integer support; the finite
matrix check is `fcs_check.py` **FCS-C5--C6**.

**⟨2⟩3.** The finite absolute first moment permits termwise differentiation
once, and the derivative is `iΣ_ννp_ν`.  The M-INDEX ledger identifies this
mean with `-2sδx`.

*Justification.* D27(LR3) and claim M-INDEX-spec; the finite-window identity
is also checked by `fcs_check.py` **FCS-C3**.

**⟨2⟩4.** Put `m=⌊μ⌋`, `r=μ-m`.  For every integer `ν`,
`(ν-m)(ν-m-1)≥0`.  Taking expectations and subtracting `μ²` yields
`Var_p(ν)≥r(1-r)`.  Equality forces all mass onto the zero set
`{m,m+1}` and those weights are then fixed by the mean.

*Justification.* M-INDEX-spec's integer support and positivity;
`fcs_check.py` **FCS-C7** checks the inequality on a nontrivial TPM law.

**⟨2⟩5.** Define the symmetric law
`p_{+n}=p_{-n}=[2ζ(3)n³]^{-1}` for `n≥1` and `p_0=0`.  Its total mass is
one, its absolute first moment is `ζ(2)/ζ(3)<∞`, and its second moment is
`ζ(1)/ζ(3)=∞`.

*Justification.* D27(LR3) requires only the finite absolute first moment;
the partial-sum witness and its red-independent gates are
`fcs_check.py` **FCS-C9** and `check-green.txt`.

**⟨2⟩6.** The two strictly positive laws on the same support
`{0,1,2,3}` with weights `(0.20,0.65,0.10,0.05)` and
`(0.12,0.78,0.08,0.02)` both have mean one, but have respectively
second cumulants `0.50,0.28` and third cumulants `0.30,0.12`.

*Justification.* Exact finite arithmetic, checked by `fcs_check.py`
**FCS-C8** and recorded in `check-green.txt`.

**⟨2⟩7. QED.**

The fourth clause is an underdetermination certificate for the *conclusions*
of M-INDEX-fin/spec.  It does not assert that every abstract lattice law is
realised by a D16 scattering state.  The forward route is named in
FCS-FLUX: add current-noise control, a channel scattering matrix, or
quasifree dynamics.

### ⟨1⟩4. COROLLARY FCS-JUMP (what “quantized first-cumulant jump” can mean)

**ASSUME.** Two ordered laws satisfy M-INDEX-spec with wall memories
`δx_A,δx_B`.

**PROVE.** Their first-cumulant difference is always
`-2s(δx_B-δx_A)`, but it need not be an integer.  If, as an additional
spectral-flow hypothesis, the second law is the integer translate
`p^B_ν=p^A_{ν-d}` for some `d∈ℤ`, then its characteristic function is
multiplied by `e^{iλd}`; the first cumulant jumps by `d` and every existing
cumulant of order at least two is unchanged.

**⟨2⟩1.** Subtract the two M-INDEX-spec ledger identities.

*Justification.* Claim M-INDEX-spec.

**⟨2⟩2.** Under H-AD-G, the already-PROVED conditional reduction gives
`p=(1-⟨N_T⟩)δ_0+⟨N_T⟩δ_2`, hence the first cumulant is
`2⟨N_T⟩`, generally noninteger.

*Justification.* Claim M-INDEX-spec's H-AD-G reduction and D18(AD2); this is
the same Bernoulli arithmetic as memory-index.md **IDX-RED.1**.

**⟨2⟩3.** For the translate hypothesis, substitute `ν=μ+d` in the
characteristic sum.  Taking a local logarithm at `λ=0` adds only `iλd`.

*Justification.* M-INDEX-fin supplies `d∈ℤ` as the only translation compatible
with the common lattice; the algebra is checked by `fcs_check.py`'s
integer-periodicity gate **FCS-C5**.

**⟨2⟩4. QED.**

Thus existing spectral-flow/index machinery pins the lattice and the
calibrated mean relation.  A quantized *jump* requires the extra statement
that the entire law undergoes an integer translation; no current claim in
`claims/CLAIMS.md` supplies that statement.

---

## 3. Determinant formula in the genuinely free case

### ⟨1⟩5. THEOREM FCS-FREE (finite quasifree TPM determinant)

**ASSUME.** A finite `M`-dimensional one-particle space and its fermionic
Fock space.  The two measured charges have the form
`Q_-=dΓ(P_-)+cI`, `Q_+=dΓ(P_+)+cI`, where `P_±` are one-particle
orthogonal projections (the second may be the Heisenberg evolution of the
first under a quadratic number-conserving Hamiltonian).  The initial state is
a gauge-invariant quasifree state with one-particle correlation matrix
`0≤C≤I`.  The TPM protocol is D27's initial spectral measurement followed
by the final one.

**PROVE.** The exact characteristic function is

`Σ_νp_νe^{iλν}
 = (1/2π)∫_0^{2π}dθ det[I-C+C U_{λ,θ}]`,            **(FCS.5)**

where

`U_{λ,θ}=e^{iθP_-}e^{-iλP_+}e^{i(λ-θ)P_-}`.       **(FCS.6)**

If `[C,P_-]=0`, the first measurement is nondisturbing and (FCS.5) reduces
to the Levitov--Lesovik/Klich form

`Σ_νp_νe^{iλν}
 = det[I-C+C e^{-iλP_+}e^{iλP_-}]`.                **(FCS.7)**

The common scalar `c` cancels, as required by M-INDEX-fin.

**⟨2⟩1.** For any one-particle matrix `A`, its exterior-algebra lift obeys
`Tr_Fock Γ(A)=det(I+A)` and `Γ(A)Γ(B)=Γ(AB)`.

*Justification.* On each exterior-power sector the trace is the corresponding
elementary symmetric polynomial of the eigenvalues of `A`; their sum is
`det(I+A)`.  Polynomial continuation covers nondiagonalisable `A`.
The identity is exercised in `fcs_check.py` **FCS-C2--C2b**.

**⟨2⟩2.** A gauge-invariant quasifree density matrix with correlation `C`
satisfies, for every one-particle unitary `U`,

`Tr_Fock(ρ_C Γ(U))=det(I-C+CU)`.

**ASSUME.** First `0<C<I`.

**PROVE.** Write
`ρ_C=det(I-C)Γ(C(I-C)^{-1})`; then apply ⟨2⟩1 and multiply the determinant
by `det(I-C)`.  Eigenvalues zero or one follow by continuity.

*Justification.* The occupation-basis construction of a gauge-invariant
quasifree state and the exact finite-Fock comparison in `fcs_check.py`
**FCS-C2--C2b**.  **QED.**

**⟨2⟩3.** Because `Q_-` has integer-spaced number spectrum, its nonselective
first-measurement map is the exact phase projection

`𝒟_-(ρ_C)=(1/2π)∫_0^{2π}e^{-iθQ_-}ρ_Ce^{iθQ_-}dθ`.

*Justification.* D27's spectral dephasing map and M-INDEX-fin's common-coset
integer spacing; Fourier orthogonality removes precisely the off-diagonal
charge blocks.  The phase projection is checked in `fcs_check.py`
**FCS-C2**.

**⟨2⟩4.** Insert ⟨2⟩3 into the mixed-state version of (FCS.1), move `ρ_C`
cyclically to the front of the trace, use
`e^{itdΓ(P)}=Γ(e^{itP})`, and apply ⟨2⟩2.  The resulting one-particle product
is exactly (FCS.6), proving (FCS.5).

*Justification.* D27, ⟨1⟩1 (FCS.1), and `fcs_check.py` **FCS-C2**.

**⟨2⟩5.** If `[C,P_-]=0`, then `[ρ_C,Q_-]=0`, so D27's first pinching leaves
the state unchanged.  Apply ⟨2⟩2 directly to (FCS.1), giving (FCS.7).

*Justification.* D27's dephasing map and `fcs_check.py` **FCS-C2b**.

**⟨2⟩6.** The scalar `cI` drops from `e^{-iλQ_+}e^{iλQ_-}` and from the
conjugation in ⟨2⟩3.

*Justification.* M-INDEX-fin's fixed-window offset cancellation.

**⟨2⟩7. QED.**

**Thermodynamic fence.**  FCS-FREE is finite dimensional.  Passing its
determinant to an infinite system needs a Fredholm determinant or an
equivalent regularisation, including a trace-class condition on the counting
perturbation.  D1, D26 and D27 provide no such hypothesis, so no
infinite-volume determinant is claimed here.

### ⟨1⟩6. PROPOSITION FCS-D16-SCOPE (why FCS-FREE is not a D16 theorem)

**ASSUME.** D16, in particular `Δ>1`.

**PROVE.** The standard Jordan--Wigner representation of the D16 Hamiltonian
is interacting and does not meet FCS-FREE's quadratic-evolution hypothesis.
Consequently the existing D16 machinery supplies (FCS.1)--(FCS.4), but no
Levitov--Lesovik determinant.

**⟨2⟩1.** Under Jordan--Wigner, the `S^xS^x+S^yS^y` part becomes fermion
hopping, while `S^z_xS^z_{x+1}` becomes
`(n_x-1/2)(n_{x+1}-1/2)`, which contains the quartic term `n_xn_{x+1}`.

*Justification.* D16's displayed XXZ bond Hamiltonian; this is direct local
Pauli/Jordan--Wigner algebra.

**⟨2⟩2.** Its coefficient is nonzero because D16 fixes `Δ>1`.  Therefore
Heisenberg evolution is not the one-particle conjugation `P_+=U^*P_-U`, and
a quasifree initial state is not generally kept quasifree.

*Justification.* D16; FCS-FREE's ASSUME line.

**⟨2⟩3.** The PROVED D16 rows currently available are LR1-GEN and
LR-D16-EDW.  They give Cesàro subsequence existence and a domain-wall-number
energy bound, respectively; neither is a quasifree trace identity or a
current-noise evaluation.

*Justification.* Claims LR1-GEN and LR-D16-EDW.

**⟨2⟩4. QED.**

The XX point `Δ=0` is quadratic, but lies outside D16 (`Δ>1`) and lacks its
easy-axis kink setting.  Applying (FCS.5) there is a free comparator, not an
instantiation of the D16 memory theorem.

---

## 4. Checker record and honest status

`fcs_check.py` constructs a four-mode finite fermion Fock space, a seeded
quasifree state not commuting with the first window number, and a seeded
quadratic evolution.  It computes the TPM law directly from both spectral
resolutions and compares it with (FCS.1), (FCS.3), (FCS.4), and (FCS.5).  A
second commuting state checks (FCS.7).  It also checks periodicity, a
Bochner matrix, the lattice variance floor, the equal-mean counterexample,
and the heavy-tail witness.

The green run is recorded in `check-green.txt`: all ten registered gates pass;
the TPM trace, projected determinant, first moment and second moment residues
are respectively `4.578e-16`, `5.579e-16`, `8.327e-17`, and `2.220e-16`.
The red run is `check-red.txt`: reversing only the final-charge counting-field
sign raises the determinant residue to `7.428e-01`, so **FCS-C2 fails** and
the process exits nonzero.  Every number in this paragraph is generated by
the named script.

### Outcome

- **Positive:** exact channel-free finite TPM FCS and moment identities;
  universal ordered-law constraints; a sharp variance floor; an exact
  phase-projected determinant formula for finite quasifree dynamics.
- **Boundary:** D27 controls only the first cumulant in the spatial limit.
  Higher cumulants can be undefined and are not fixed by lattice support plus
  calibrated displacement.
- **D16:** interacting, so the determinant route does not apply.  The named
  forward attack is the pinched edge-current two-point function in FCS-FLUX;
  alternatively add genuine quasifree dynamics or a scattering/channel
  determinant hypothesis.
- **Status:** SKETCH pending the repository's capped hostile review; no shared
  claim or definition is proposed for promotion by this lane.
