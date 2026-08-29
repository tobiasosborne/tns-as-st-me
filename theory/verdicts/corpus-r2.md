<!-- ROLE: L6 critic verdict, round 2 adjudication, on the full repaired and
     rebuilt summit corpus.  Critic: Codex. Date: 2026-08-26. -->

# Critic verdict r2 — full repaired and rebuilt corpus

Critic: Codex, adversarial adjudication under L6/L6b/L10.  I treated
`mquant-ml45-r1.md` and `triangle-r1.md` as my own prior verdicts, checked every
requested disposition against the amended artifacts, re-derived the repaired
algebra, and reviewed `spt-rebuild.md` as a first-time target.  I also ran all
eight checkers under `python3 -O`, exercised `ml4_check.py --red-uniform`, and
mutation-tested two copies of the SPT checker under `/tmp`.

The non-SPT repair is mostly successful.  M-flux, the conditional M-quant
arithmetic, the Fano spectral consequence conditional on Mq-E, ML4-A, and both
repaired ML5 implications survive.  B3's transmitted branch now gives
`2s delta x+2=0`, hence `delta x=-1/s`, and its reflected branch gives zero.
The old false half-line formula is gone.

The rebuilt SPT package does not pass.  Its explicit tensors and AKLT numbers
are right, and the finite-group slant algebra is right, but the central Lie
endpoint identity is ill-typed and phase-gauge dependent: D20 constructs the
compression of D10's **anti-Hermitian** charge, while SPT-E' identifies it with
the **Hermitian** operator `-iX_C`.  Moreover a partial-charge compression is
invariant under `V(e^{epsilon xi}) -> e^{ia epsilon}V(e^{epsilon xi})`, whereas
`-iX_C` shifts by `a I`; the telescoping limit is a centered generator, not an
uncentered `X_C`.  The checker uses Hermitian `S^z` and a traceless AKLT
generator, so it cannot expose either defect.  There are additional MAJOR
failures in SPT-B' continuity, the SPT-D' Whitehead statement, the register
identification, ML4's purported fixed-ring on-shell limit, and status/
hypothesis lockstep.

---

## Independent recomputations

### 1. SPT-B': multiplier cancellation, transfer continuity, and the caveat

For one closed on-site string, WI gives `V(g)^{-1}` and `V(g)` at the two
ends.  In a doubled contraction their action is
`V(g) tensor conjugate(V(g))`.  Therefore

`[V(h) tensor conjugate(V(h))][V(g) tensor conjugate(V(g))]
 = omega(h,g) conjugate(omega(h,g)) V(hg) tensor conjugate(V(hg))`,

so the multiplier cancels exactly.  This proves absence of a *projective
multiplication failure* in the total closed register.  It does not make
`Ad(V)` class-blind: Pauli conjugation has D2 multiplicities `(1,1,1,1)`, while
scalar conjugation has `(4,0,0,0)`, and `Tr Ad(V(R_x))` is `0` versus `4`.

The compact-subpath transfer argument is sound **for continuous external
data**.  A common modulus gap permits a fixed Riesz contour around `1`;
continuity on a compact parameter interval bounds the complementary resolvent
uniformly, hence gives a uniform `C lambda_tilde^m` estimate and uniform
thermodynamic convergence.  This yields continuity, not local constancy.
Consequently a character multiplicity or another separately proved locally
constant bulk invariant is explicitly allowed.  The displayed
`C_bulk(b)=b^2/[4(1-b^2)]` is a valid counterexample to topological rigidity of
raw scalar coefficients, not a proof that no bulk invariant exists.

The theorem as written omits continuity of the external tensors/embeddings,
however.  B2 asks only for a fixed normalized register and a positive Gram
lower bound.  Keeping `A(t)` constant and choosing a discontinuous family of
normalized external embeddings satisfies those words and makes the scalar
coefficient jump.  This is NEW objection 2.

### 2. SPT-E': endpoint telescoping, centering, and module dimension

The finite group-string telescoping is correct up to the declared left/dual
orientation: the far WI endpoint can be cancelled, leaving one projective
endpoint factor.  The infinitesimal statement does not follow in the displayed
form.

D10 fixes `q_x(xi)^dagger=-q_x(xi)` and
`Q[f;xi]=sum_x f(x)q_x(xi)`.  Thus D20's
`R_{C,L}=C_C(Q[f_L;xi])` is anti-Hermitian.  Since
`X_C(xi)^dagger=-X_C(xi)`, D21's `Q_edge=-iX_C` is Hermitian.  They cannot be
equal except in the zero case.  Independently, rephase the same virtual lift by
`V_epsilon -> e^{ia epsilon}V_epsilon`.  Then
`X_C -> X_C+ia I`, while the physical partial charge and its compression are
unchanged.  Hence no uncentered equality to `-iX_C` is phase-gauge invariant.

Differentiating IT and summing the resulting transfer coboundary gives, up to
the chosen left/right sign,

`R_C(xi) = +/- [X_C(xi)-tr(r X_C(xi)) I]`

in the anti-Hermitian convention.  The corresponding Hermitian observable is
`-iR_C`, not D20's `R_C` itself.  The AKLT generator is traceless against
`r=I/2`, so the checker sees the correct special number while missing the
general defect.

The exact AKLT-family contraction itself is correct.  Direct Pauli
multiplication gives
`E_{S^z}(r)=-(1-b^2)Z/2` and `E_b(Z)=(2b^2-1)Z`; hence

`2 sum_{n=0}^{L-1} E_b^n(E_{S^z}(r))
 = -(1/2)[1-(2b^2-1)^L]Z`.

The module lower bound is also correct once a genuine endpoint module is
fixed: every invariant irreducible block has multiplier `omega`, so its
dimension is at least `d_omega`, and a nontrivial multiplier cannot occur in
dimension one.  But `E_C=C^chi` is not “equivalently” A1(d1)'s padded-window
module: the latter is isomorphic to `M_chi(C)` and has dimension `chi^2`, with
left action `L_V`, i.e. `chi` copies of the `E_C` action.  This is NEW
objection 4.

The shifted-weight calculation is valid only after the full-group lift and
central character in Sd8' are fixed: `e^{2pi i q}=nu_omega(z_xi)` implies
`q in q_omega+Z`.  Integer shifts or added linear modules can deform the raw
edge spectrum without changing the offset.  The rebuilt theorem mostly
respects that boundary; the invalid uncentered identification does not.

### 3. SPT-T' and SPT-D'

With `V(a)V(b)=e^{i omega(a,b)}V(ab)`, eliminate `V(hg)` between

`V(h)V(g)=e^{i omega(h,g)}V(hg)` and
`V(hgh^{-1})V(h)=e^{i omega(hgh^{-1},h)}V(hg)`.

This gives (5.1), and for commuting `g,h` gives the claimed slant phase
`e^{i[omega(h,g)-omega(g,h)]}`.  The second endpoint must carry the inverse
phase because the full on-site string is honest.  The repaired SPT-T' algebra
therefore survives.

The ordered finite-group product
`S(h)S(g)=e^{i omega(h,g)}S(hg)` also follows once a one-endpoint convention is
fixed.  The semisimple infinitesimal conclusion is overstated.  Whitehead says
the Lie-algebra 2-cocycle is a coboundary and can be removed by a phase choice;
it does not make the central term zero in every local section.  Starting from
honest generators `X(xi)` and replacing them by
`X'(xi)=X(xi)+i ell(xi)I` gives
`[X'(xi),X'(zeta)]=X'([xi,zeta])-i ell([xi,zeta])I`, a generally nonzero but
coboundary central term.  This is NEW objection 5.

### 4. SPT-M' charge bookkeeping

Given H-split, H-AD-edge, a conserved Hermitian total charge, and definite
asymptotic charges, the equation is immediate and correct:

`0=Delta Q_tot=Delta Q_edge+(Q_bulk,out-Q_bulk,in)`.

If both edge endpoints lie in the same shifted lattice `q_omega+Z`, their
difference is integral; for the AKLT doublet the possible differences are
`{-1,0,+1}`.  Expectations need not be integral.  H-AD-edge is used exactly
for the channel decomposition, and H-split for the physical edge register.
No H-soft-p assumption is needed for this charge identity.  Its promotion is
nevertheless blocked by the invalid definition of `Q_edge` and by the
lockstep defects below.  “Permanent” still additionally needs the isolated
charge-preserving edge dynamics stated in D22.

### 5. Non-SPT repaired algebra

* **M-flux.** Summing the local continuity equation over `W=[a,b]` gives
  `dot X_W=(2s)^{-1}(j_{a-1|a}-j_{b|b+1})`; finite-time integration proves the
  DC identity.  No virtual-potential conclusion follows or is now claimed.
* **M-quant.** Reflection has total charges
  `2s(m_i-c)-1` and `2s(m_R-c)-1`, hence `m_R=m_i`.  Transmission has
  `2s(m_i-c)-1` and `2s(m_T-c)+1`, hence `m_T-m_i=-1/s`.  Therefore
  `Delta X=-(1/s)N_T`, and projection algebra gives the stated spectrum and
  `Var(Delta X)=s^{-2}<N_T>(1-<N_T>)`.  This is conditional on D18, exactly as
  now stated.
* **Mq-AD3.** Conditional on Mq-E, the perturbation of the free Jacobi channel
  is rank two and trace class.  Kato--Rosenblum supplies complete wave
  operators on the absolutely continuous subspace.  The Feshbach denominator
  has nonzero imaginary part in the open band; outside it has only isolated
  roots, and threshold solutions are not in `ell^2`.  Together with Mq-E's
  observable/channel clauses, this supplies D18 for smooth packets away from
  thresholds.  It does not prove Mq-E or the full-chain lift.
* **ML5-A.** The two-condition iff is now exact.  Banach-valued Taylor gives
  `M_2(k)=M_2(0)+k partial_kM_2(0)+R_2`; the two zero conditions remove the
  first two unwanted terms and `K_O` bounds `R_2`.  The old constant-map and
  `V_int` counterexamples fail the new intercept condition.  The relative
  bound is correctly a separate hypothesis.
* **ML5-B.** Multiplying
  `(e^{ik}-1)[-i chi/v_h][2iv_hM_1]` gives `2i chi kM_1+O(k^2)`.  Hypothesis 1
  now says explicitly that the two bounded remainders are exhaustive.  This is
  a valid conditional implication; nonemptiness/microscopic membership is not
  proved.  *(bd `tns-iu5` r3: the same multiplication with the D24(d)3b
  constant carried gives `2i𝔞_leg χ k M_1 + O(k²)`; `𝔞_leg` enters as a
  nonzero constant factor and no step of this adjudication uses its value,
  so the implication certified here survives verbatim under
  reparametrisation.  Its displayed conclusion in `claims/CLAIMS.md` is
  updated accordingly; the promotion is not reopened.)*
* **B3.** The repaired transmitted and reflected calculations agree with
  M-quant and are cut independent after the stated leg subtraction.  The
  finite-time label argument has one minor missing density step: it must also
  approximate the evolved factor `alpha_t(D)`, not only the distant
  `alpha_t(tau_n(O))`.  See NEW objection 9.

### 6. Explicit TRIV tensor and numerical/checker record

I recomputed TRIV independently of the checker.  At `t=1`,

`T^x=[[0,sqrt(3)/2],[1/2,0]]`, `T^y=0`,
`T^z=diag(sqrt(3)/2,1/2)`.

Then `sum_s (T^s)^dagger T^s=I`,
`E(diag(3/4,1/4))=diag(3/4,1/4)`, and the transfer eigenvalues are
`{1,sqrt(3)/2,0,0}`.  The four selected length-two words
`(T^x)^2,(T^z)^2,T^zT^x,T^xT^z` have vectorized determinant `-3/64`, hence
rank four.  Substitution for all four D2 elements gives exactly
`u(g)T=theta(g)V_T(g)^{-1}T V_T(g)`, with
`theta=(1,-1,-1,1)` and `V_T=(I,Z,I,Z)`.  Thus the tensor is injective and
D2-covariant as claimed.

The optimized full suite passed, all eight scripts.  The SPT record reproduced
the shard's numbers:

* TRIV rank `4`, transfer `{1,0.866025403784,0,0}`, canonical residual
  `1.11e-16`, covariance residual `0`;
* D2 multiplicities `(1,1,1,1)`, `(4,0,0,0)`, and explicit TRIV2
  `(2,0,2,0)`; closed characters `0` versus `4`;
* bulk exact values `0.125000000000` and `0.240196078431`, Fourier values
  `0.125000023426`, `0.240196083171`, packet values `0.125000135674`,
  `0.240196105387`;
* edge formula error `1.665e-16`, limit error `2.220e-16`, and
  `|q_edge|=0.5`.

`python3 -O theory/checks/ml4_check.py --red-uniform` exited `1`, after the
normalized joint-scaling ratio grew from `1.057944` to `2.897405`.  In
`/tmp/tns-corpus-r2-spt.LFa3hc`, an edge-sign mutant exited `1` with error
`1.333`, and an independent `4 -> 8` bulk-denominator mutant exited `1` with
measured `0.125000023426` versus mutated `0.0625`.  The checkers are red-capable
for those finite computations.  They do not test SPT-E's Hermiticity/phase
gauge, H-split, general charge lattice, or H-AD-edge.

### 7. ML2 residue sweep

I compared the current shard with the version at the r2 PASS point and read
the amended proof.  The sweep changes no theorem formula, spectrum, inventory,
or checker algorithm.  It adds the missing derivations/cross-references,
states the `K=0` descendant representative, proves the degenerate `K=pi`
orthogonality and absence of singular-continuous spectrum, and changes the
imprecise “almost every `K != 0`” to the already implied “every `K != 0`”.
The optimized checker still reproduces the passed inventory.  Thus the sweep
changed proof completeness and wording, but no mathematical conclusion used by
this corpus.

---

## Objection-by-objection adjudication

### `mquant-ml45-r1.md`, mq-1--mq-10

| id | adjudication | independent check |
|---|---|---|
| mq-1 | **PARTIALLY RESOLVED** | The false uniform bound is retracted and the `k=2pi/N` countersequence is derived and checked.  The surviving fixed-ring “on-shell” `k->0` limit is not physical because ring momenta are discrete; see NEW 3. |
| mq-2 | **RESOLVED** | Taylor expansion leaves both an intercept and a first jet.  D24(c)/ML5-A now set both to zero, define the correct Banach second-derivative norm, and separately assume the relative bound. |
| mq-3 | **RESOLVED** | ML5-B hypothesis 1 is now the exact normed equality saying the three named contributions exhaust `M_2`; the proof invokes it before summing. |
| mq-4 | **RESOLVED** | D18 is now one coherent AD1--AD4 definition; the shard cites it and no longer derives projection spectrum from the old norm-mixture condition. |
| mq-5 | **RESOLVED** | Mq-E is an explicit all-volume/unitary hypothesis.  The Kato--Rosenblum/Feshbach conclusion is conditional on it and the finite `N=14` enumeration is labelled evidence. |
| mq-6 | **RESOLVED** | The variance is consistently `Var(Delta X)`; the extra sharp-initial-wall/two-time assumptions needed for `Var(X_W)` are stated. |
| mq-7 | **RESOLVED** | M-flux now contains only physical boundary currents.  No active theorem infers a current divergence from G0(d)'s virtual charge-density divergence. |
| mq-8 | **RESOLVED** | The concrete theorem is D16 spin `1/2`; arbitrary `s` appears only in the explicitly conditional charge arithmetic.  The short Corner-B summary is loose, but the theorem/DAG/TRIANGLE quantifiers are correct. |
| mq-9 | **RESOLVED** | Active M-quant leaves cite D13/D14/A2; `Bd` labels occur only in marked history/crosswalk prose. |
| mq-10 | **PARTIALLY RESOLVED** | ML4-Q1 tests the formerly missing joint scaling, `--red-uniform` fails, and the M-quant checker is honestly described as flux/empirical only.  The fixed-volume green exponent still tests a continuous non-ring interpolation rather than an on-shell fixed-ring limit (NEW 3). |

### `triangle-r1.md`, T1--T9

| id | adjudication | independent check |
|---|---|---|
| T1 | **RESOLVED** | Every r1-attacked positive row is at most SKETCH before this verdict; only Corner A, oracle, and ML2 retain PROVED. |
| T2 | **PARTIALLY RESOLVED** | The four-word enum and freeze rule are repaired, but the SPT-E DAG cell again contains two statuses (`SKETCH` and `CONJECTURE`) and SPT hypotheses are not in lockstep (NEW 6). |
| T3 | **RESOLVED** | The false half-line formula is absent.  Direct transmitted bookkeeping gives `delta x=-1/s`, reflection zero. |
| T4 | **RESOLVED** | D18 and every active consumer use the coherent wave-operator/local-decay definition; Mq-E is separate. |
| T5 | **RESOLVED** | TRIANGLE section 3.1 explicitly rejects the virtual-potential strengthening. |
| T6 | **RESOLVED** | TRIANGLE separates the general conditional arithmetic, the spin-`1/2` D16 theorem, the Mq-E projection, and the still-open general MPS lift. |
| T7 | **RESOLVED** | Section 6.1 lists ML1, ML3/joint scaling, ML4-3, exhaustive LSZ, microscopic `S_W` membership, and ML6; “closed at n=1” is gone. |
| T8 | **RESOLVED** | The all-register no-go is REFUTED.  The new bulk statement excludes only a projective multiplication anomaly and explicitly permits a quantized endpoint coefficient. |
| T9 | **RESOLVED** | The static computation now fixes tensors, Hamiltonian boundary terms, packet family, scalars, and tolerances, and maps each outcome to a scoped claim.  It honestly leaves dynamics to SPT-M'-dyn. |

### `triangle-r1.md`, B1--B9

| id | adjudication | independent check |
|---|---|---|
| B1 | **RESOLVED** | The transmitted branch now uses the total charge difference `(+1)-(-1)=2`, giving `2s delta x+2=0`; the raw half-line equation is explicitly refuted. |
| B2 | **PARTIALLY RESOLVED** | Stationary vacua, translation covariance, and LR quasi-locality are now the right argument.  One density leaf for the evolved local factor `alpha_t(D)` is omitted (NEW 9). |
| B3 | **RESOLVED** | B3 is a numbered ASSUME/PROVE/QED tree with actual D-number and theorem citations; the nonexistent Proposition N is gone. |
| B4 | **RESOLVED** | Neither B3 nor M-flux uses the unproved kink-sector virtual charge; R1/R3 are future optional interpretations. |
| B5 | **RESOLVED** | The norm-mixture condition is marked superseded and all active results use D18 AD1--AD4. |
| B6 | **RESOLVED** | K4 is consistently a conjecture; no-recoil and uniqueness predictions are explicitly conditional on K4/R5. |
| B7 | **RESOLVED** | The text distinguishes channel spectrum `{0,-1/s}` from continuous expectations and restricts the concrete dynamics to spin `1/2`; higher spin is a falsifier. |
| B8 | **RESOLVED** | All active theorem errors use `C_{lambda_tilde}lambda_tilde^{d_W}` with core-to-edge distance, never bare `lambda_E^L`. |
| B9 | **RESOLVED** | Section 10 and the DAG list B3/K1--K3/M-quant as SKETCH pending r2, not as already proved. |

### `triangle-r1.md`, S1--S8

| id | adjudication | independent check |
|---|---|---|
| S1 | **PARTIALLY RESOLVED** | Operators now precede scalar matrix elements and all profile/limit families are explicit.  The endpoint Lie object is nevertheless ill-typed against D10 and phase-gauge dependent (NEW 1). |
| S2 | **RESOLVED** | Pointwise `[omega]`-blindness is REFUTED; the D2 adjoint decompositions and closed characters independently reproduce the counterexample. |
| S3 | **PARTIALLY RESOLVED** | The all-orders no-go is REFUTED and global weights/dimension are retained.  SPT-D' still turns Whitehead's “coboundary” into “zero in the displayed section” (NEW 5). |
| S4 | **RESOLVED** | Exact AKLT, TRIV2, and TRIV1 tensors and physical boundary terms are given; the static green/red computation is executable and its scope no longer masquerades as scattering. |
| S5 | **RESOLVED** | D2 is used only for finite endpoint algebra; O(2) supplies the Lie charge comparison; the product is not called SO(3)-symmetric. |
| S6 | **RESOLVED** | Protection is confined to the endpoint module/capacity.  Nonzero scattering is a separate conjecture and accidental trivial-edge memory is allowed. |
| S7 | **RESOLVED** | The general conjugation formula uses `hgh^{-1}`; the slant ratio is restricted to commuting elements, with convention and endpoint compensation stated. |
| S8 | **RESOLVED** | Merge statuses remain SKETCH and all physical/dynamical assumptions are exposed in the shard.  The new proof failures are recorded separately below. |

---

## Lockstep, notation, and fresh-attack audit

The non-SPT shard/DAG/TRIANGLE statuses agree.  The SPT status merge is not
exact: SPT-E's DAG cell assigns both SKETCH and CONJECTURE, while TRIANGLE's
status index assigns SKETCH; SPT-D's shard requires H-dress for a physical
edge operator, while the DAG and TRIANGLE omit it.  SPT-M'-dyn also refers to
an “explicit boundary-magnon coupling” that is not specified by D23.  These
are collected in NEW 6.

Notation overloads 9, 10, and 12 have workable syntactic rules.  Overloads 8
and 11 are incomplete: `E_b(K)` already denotes the bound-pair energy, while
the new row uses `E_b` for the transfer map; and bare `r` already denotes the
bound-pair separation, while overload 11 says bare `r` is the transfer fixed
point.  See NEW 8.

The known Corner-C `mathsf S`/`S`-glyph gap (`tns-ce2`) remains real: the
Corner-C `S-general` soft factor has no D-number home after D20 was rebuilt.
No currently PROVED result silently depends on it.  S-general is CONJECTURE;
ML5-A/B are stated directly in terms of `M_1,M_2`; SPT uses the distinct
`mathbb S`; and the narrow S2-2body multiplier can be stated without the
undefined general symbol.  The gap therefore blocks L4 closure of S-general,
not any promotion recommended below.

Fresh attacks produced the following outcomes.

1. **Rigidity dichotomy.**  A bulk quantized invariant is easy to propose:
   the D2 character multiplicities of `Ad(V)` are discrete and locally
   constant.  SPT-B' explicitly permits this, so it does not refute the narrow
   multiplier no-go.  An edge can also be deformed by integer charge shifts or
   added linear modules without changing `q_omega mod Z`; the rebuilt caveat
   permits that too.  The successful break is instead the phase-gauge/
   centering failure of SPT-E' and the missing external-data continuity of
   SPT-B'.
2. **B3 bookkeeping.**  Re-evaluating both branches with any fixed cut `c`
   gives zero for reflection and `-1/s` for transmission.  Moving `c` shifts
   both in/out kink charges equally, so it cancels.  The arithmetic survives.
3. **ML5-A.**  The old constant-map and four-site `V_int` attacks now violate
   `M_2(0)=0`; `O_eta` violates the first-jet condition.  With both conditions
   imposed, Banach Taylor leaves only `O(k^2)`.  The repaired iff survives.

---

## Numbered NEW objections

### N1. FATAL — SPT-E' identifies incompatible and gauge-dependent Lie residues

**Location:** `definitions.md` D20--D21 (lines 771--805);
`theory/spt-rebuild.md` (2.9), SPT-E'(i),
`<1>4.<2>1.<3>3` (lines 465--501); checker S-C4.

**Independent computation.** D10's `Q[f;xi]` and therefore D20's `R_C` are
anti-Hermitian, while `-iX_C` is Hermitian.  Rephasing
`V_epsilon -> e^{ia epsilon}V_epsilon` shifts `-iX_C` by `aI` without changing
the physical compression.  Transfer telescoping instead produces the centered
generator `+/-[X_C-tr(rX_C)I]`.  S-C4 uses Hermitian `S^z` and
`tr(rX_C)=0`, so its green result is a convention-specialized number, not a
test of the theorem.

**Fix demand:** define a Hermitian partial charge (`-iQ`), fix the endpoint
orientation and phase gauge or center `X_C`, restate the shifted lattice for
that operator, and add a nontrivial U(1) phase-gauge red test.

### N2. MAJOR — SPT-B' continuity omits continuity of the external data

**Location:** `theory/spt-rebuild.md` SPT-B' B2 and
`<1>3.<2>2.<3>1--<3>4` (lines 323--343, 379--402); D20's embeddings.

**Independent computation.** The common transfer gap does give a uniform
Riesz/resolvent bound on a compact tensor path.  But the finite contraction is
polynomial in both `A(t)` **and the external tensors/embeddings**.  B2 supplies
only normalization and a Gram lower bound.  With constant `A(t)` and a
discontinuous normalized choice of external embedding, every stated B1--B3
condition holds while the coefficient jumps.

**Fix demand:** require the external tensors, channel embeddings, gauge fixes,
and any differentiated profiles to be continuous (respectively `C^p`) in the
path parameter before claiming coefficient continuity.

### N3. MAJOR — the repaired fixed-volume ML4 limit is not an on-shell ring limit

**Location:** `theory/ml4-ward-reduction.md` `<1>1` definition of `Gamma_N`,
`<1>4.<2>2--<2>4` and (15)--(17) (especially lines 291--314 and 344--381);
`claims/CLAIMS.md` ML4; `TRIANGLE.md` section 2.5.

**Independent computation.** At fixed periodic `N`, allowed total momenta are
discrete, so there is no nonzero sequence of ring momenta `k->0`.  The checker
and proof vary continuous `k` in (12); away from quantized `h+k`, that vector
does not satisfy the ring boundary condition and is not the declared on-shell
channel.  Along the first physical sequence `k_N=2pi/N`, ML4-Q1 itself shows
the normalized `k^2` constant diverging.

**Fix demand:** relabel (15)--(17) as an off-shell analytic interpolation, or
introduce twisted boundary conditions/a genuine packet infinite-volume
register and prove the estimate there; do not call the iterated fixed-ring
limit on-shell.

### N4. MAJOR — `E_C` is not A1(d1)'s padded-window module

**Location:** `definitions.md` D21 lines 788--797;
`theory/spt-rebuild.md` Sd7' lines 259--271 and SPT-E'(ii).

**Independent computation.** Padded-window injectivity identifies A1(d1)'s
module with `M_chi(C)`, dimension `chi^2`.  D21 defines `E_C=C^chi`, dimension
`chi`.  Under left multiplication, the former is
`E_C tensor (C^chi)^*`, i.e. `chi` copies of the latter, not an equivalent
module.  The `d_omega` lower bound survives, but the asserted register identity
and its link to the prior passed theorem do not.

**Fix demand:** distinguish the Schmidt/edge register from the padded-window
matrix module and state their exact tensor-product/multiplicity relation;
formulate H-split for the intended one only.

### N5. MAJOR — SPT-D' overstates Whitehead's lemma

**Location:** `theory/spt-rebuild.md` SPT-D' lines 619--639;
`claims/CLAIMS.md` SPT-D'; `TRIANGLE.md` section 5/status index.

**Independent computation.** Rephase infinitesimal generators by
`X'(xi)=X(xi)+i ell(xi)I`.  Then
`[X'(xi),X'(zeta)]=X'([xi,zeta])-i ell([xi,zeta])I`.  The central term can be
nonzero even for semisimple Lie algebra; Whitehead says it is a coboundary and
can be removed by choosing a section.  The global projective module remains as
the shard correctly says.

**Fix demand:** replace “has/yields no central term” by “the infinitesimal
central cocycle is cohomologically trivial and can be gauged away,” with the
chosen phase convention stated.

### N6. MAJOR — SPT status and hypothesis lockstep has failed again

**Location:** `claims/CLAIMS.md` SPT-E'/D' rows (lines 45--47);
`TRIANGLE.md` section 5 and status rows 502--504;
`theory/spt-rebuild.md` SPT-D' ASSUME lines 612--615 and SPT-M'-dyn lines
682--687.

**Independent audit.** The SPT-E DAG status cell contains both `SKETCH` and
`CONJECTURE`, contrary to the four-status one-row rule and unlike TRIANGLE's
single SKETCH status.  SPT-D' requires both H-split and H-dress for a physical
edge operator, but its DAG/TRIANGLE rows state only H-split.  Finally
SPT-M'-dyn invokes an “explicit boundary-magnon coupling” absent from D23;
D23 supplies the open parent/boundary Hamiltonians, with `h_partial,A=0`, but
no separately specified coupling.

**Fix demand:** give each claim one L5 status, carry H-dress into every
physical SPT-D consumer, and define the exact AKLT half-chain dynamical
Hamiltonian/coupling before retaining SPT-M'-dyn as a model-specific
conjecture.

### N7. MAJOR — TRIANGLE reasserts the unproved universality of the Fano zero

**Location:** `theory/TRIANGLE.md` section 6.2, lines 444--452; compare section
3.4 and the M-tk DAG row.

**Independent audit.** Section 3.4 and M-tk correctly say universality of the
quadratic zero and coefficient is not established.  Section 6.2 instead says
they “are universal functions” of asymptotic data.  Mq-E proves only the
specified graph formula, and the full-chain leakage is measured rather than
controlled; no source-class theorem closes the gap.

**Fix demand:** change the sentence to “whether the zero and coefficient are
universal remains CONJECTURE” and keep C=>B at its conditional bookkeeping
scope.

### N8. MINOR — overload rules 8 and 11 are not mechanically complete

**Location:** `notation.md` overloads 8--11, lines 119--136; earlier D7 symbol
rows.

**Independent audit.** `E_b(K)` is already the bound-pair energy, while new
`E_b` is the transfer map of `A_b`; bare `r` is already D7's relative
separation, while overload 11 says bare `r` is the right fixed point.  Argument
and local-scope disambiguation is possible, but the two new rules do not state
it.  Overloads 9, 10, and 12 are mechanically adequate.

**Fix demand:** add `E_b(K)` and D7-local separation `r` to the overload rules,
with argument/scope tests that cover every occurrence.

### N9. MINOR — B3's LR proof omits the evolved first local factor

**Location:** `theory/corner-b-draft.md` B3
`<1>1.<2>1--<2>3` (section 7); `TRIANGLE.md` section 6.3(i).

**Independent computation.** For the evolved state,
`rho_t(D tau_n(O))=rho(alpha_t(D) alpha_t(tau_n(O)))`.  The proof approximates
the distant second factor but does not explicitly approximate
`alpha_t(D)` by a local observable or extend D9(a)'s factorized limit by norm
density.  Both are standard consequences of quasi-locality, so the result is
not false; one leaf is missing.

**Fix demand:** add the norm-local approximation of `alpha_t(D)` and the
two-error density estimate before taking the D9(a) factorized limit.

### N10. NOTE — checker success does not cover the failed theorem quantifiers

**Location:** `theory/checks/spt_rebuild_check.py` S-C3--S-C5 and
`theory/checks/ml4_check.py` fixed-volume probes.

The exact finite computations and their red mutants are genuine.  S-C4 does
not vary the virtual phase gauge or D10 Hermiticity convention, and ML4's
fixed-volume exponent uses a continuous non-ring `k`.  These limitations are
now theorem-relevant, not reasons to distrust the finite numbers.

---

## Promotion decisions

| row/item | decision | reason or missing step |
|---|---|---|
| **S2-2body** | **PROMOTE to PROVED** | The narrow exact two-body multiplier/phase expansion follows from the local contact equation with uniform compact-hard remainder and matches the passed oracle.  This does not promote S-general or process independence. |
| **ML4-A** | **PROMOTE to PROVED** | The abstract matching-plus-`C^1` cancellation inequality is a complete operator-norm proof. |
| **exact finite-sector Ward projection (8)--(11)** | **PROMOTE to PROVED** | Direct SU(2) commutator and polar/projection algebra; independent of the ML4 application. |
| **ML4 one-hard fixed-volume/ordered-limit application** | **HOLD** | A physical fixed periodic ring has no on-shell `k->0` sequence; the proved Taylor bound is for an analytic interpolation (NEW 3). |
| **ML5-A** | **PROMOTE to PROVED** | The repaired two-condition iff and `K_O` bound are exactly Banach Taylor. |
| **ML5-B** | **PROMOTE to PROVED (conditional implication)** | Its exhaustive LSZ equality and the two remainder estimates are explicit assumptions.  Microscopic nonemptiness/membership remains CONJECTURE. |
| **M-flux** | **PROMOTE to PROVED** | Exact finite-time telescoping identity for physical boundary currents. |
| **K1** | **PROMOTE to PROVED** | Direct positive `2x2` block diagonalization gives the spectrum and kernel. |
| **K2** | **PROMOTE to PROVED** | Every neighboring product factor lies in K1's kernel. |
| **K3** | **PROMOTE to PROVED** | The boundary field telescopes outside every local observable and leaves the quasi-local derivation unchanged. |
| **B3** | **PROMOTE to PROVED**, with N9 swept | The charge arithmetic is correct and the label-rigidity argument needs only the stated standard density leaf.  This does not prove a `Z`-torsor or the full B=>A slogan. |
| **Mq-AD3** | **PROMOTE to PROVED conditional on Mq-E** | Trace-class scattering, the Feshbach spectral analysis, and local decay follow once Mq-E supplies the graph, labels, and observable map. |
| **M-quant** | **PROMOTE to PROVED conditional on D18** | Charge conservation gives the channel displacement operator, spectrum, expectation, and `Var(Delta X)` exactly.  Full-chain D18 remains open. |
| **M-tk / Fano formula and soft zero** | **PROMOTE to PROVED conditional on Mq-E for the displayed graph** | The one-site Fano matching and expansion are exact; full-chain accuracy and universality remain unproved. |
| **N2 empirical scan** | **HOLD at SKETCH** | It is numerical evidence, not a theorem row. |
| **SPT-B'** | **HOLD** | External-data continuity is absent (NEW 2).  The narrower closed-multiplier cancellation could be split out and promoted. |
| **SPT-E'** | **HOLD** | The Lie residue is ill-typed, uncentered, and phase-gauge dependent; the register equivalence is false (NEW 1, N4).  The exact AKLT formula may be split out and promoted. |
| **SPT-T'** | **HOLD** | The slant algebra is correct, but the row consumes the unresolved one-endpoint residue convention and its physical hypothesis lockstep is not clean. |
| **SPT-D'** | **HOLD** | The infinitesimal Whitehead statement and H-dress propagation must be repaired (NEW 5, N6). |
| **SPT-M'** | **HOLD** | The conditional conservation identity survives, but its charge operator/shifted-lattice input is SPT-E' and is not yet well defined. |
| **SPT-M'-dyn** | **HOLD at CONJECTURE** | The half-chain Hamiltonian/coupling, H-AD-edge, on-shell reflection matrix, and nonvanishing proof are missing. |
| **C=>B edge** | **HOLD at SKETCH** | The graph calculation and charge law are conditional, and TRIANGLE currently overclaims universality (NEW 7). |
| **B=>A edge** | **HOLD at SKETCH** | B3 proves sector preservation/bookkeeping; it does not yet show that measured memory reconstructs an asymptotic-symmetry action or classifying datum. |

The known `S-general` row remains **CONJECTURE**: ML1, ML3, infinite-volume
ML4, ML4-3, microscopic `S_W` membership, and ML6 are still open, independently
of the promotions above.

---

## Final disposition

The r1 non-SPT failures were repaired with only the ML4 on-shell quantifier
remaining major.  The SPT rebuild gets the explicit tensor algebra, AKLT
contraction, slant product, and conditional charge bookkeeping substantially
right, but its central endpoint operator is not well defined as stated and its
status/hypothesis merge is not lockstep.  The exact numerical record cannot
repair those theorem-level defects.

**FAIL(N1, N2, N3, N4, N5, N6, N7)**
