# RESULT NON-ARTIFICIAL — a semiclassical soft-phase envelope, but no DH law for the memory weights

**Landing.**  The result belongs in a companion paper as a short
“semiclassical soft envelope” section.  At most the two-sentence clause in
§5 below belongs in the Letter's §7 discussion; the Letter itself is full.

**Status and scope.**  This is a **SPECULATIVE RESULT** about the large-`S`
envelope of the two-magnon phase.  It is not a new finite-`S` slope proof:
`S2-2body-S` remains the only finite-`S` value source.  It derives no exact
support, no integrality, no wall-crossing dichotomy, and no ABBV coefficient.
The six verdicts of `theory/dh-hunt.md` stand unchanged.

The non-artificial output is the continuous, parameter-free envelope

`delta_S(k_s,k_h) = F(k_s,k_h)/S + G(k_s,k_h)/S^2 + O(S^-3)`,       **(SC.1)**

with `F,G` given explicitly in §2.  The leading term is the dilute
Landau--Lifshitz/coadjoint-orbit contact phase and `G/S^2` is the first
subleading contact correction.  Frozen finite-`k` ED rows not previously
compared to this truncation agree within `2.62%`; adding `G/S^2` reduces the
error of every such row by at least `89.8%`.  An independent `N=18` ED
sequence through `S=8` obeys the derived pointwise remainder bound and has
second-order residual `O(S^-3)`.

There is no corresponding positive result for `{p_nu}`.  The one-magnon
memory protocol has escaped charge `O(1)`, not a growing highest weight.
Rescaling by `S` or `N_W` therefore collapses its law, while its unscaled
channel weights are scattering data.  A projective Heckman limit exists for
a different, precisely identified trace/multiplicity family, but applying it
to the measured TPM law would insert the wanted weights as input.

## 1. Route ledger

| route | verdict | what was actually tested |
|---|---|---|
| Heckman limit for escaped-charge weights | **DEAD for `{p_nu}`; seed vindicated** | `H^0(P(C_-1+C_0^2+C_+1),O(n))` has a genuine rescaled multiplicity limit equal to the projective DH spline `(3/2)(1-|x|)^2 dx`.  The memory experiment is not this normalized-trace family: it holds escaped magnon number fixed, uses a pure in-state and two-time dynamics, and stays first-moment tight.  The frozen memory probe ends with at least `0.99601` on `Q_W=-2`, not a broad projective spline. |
| Collective/coadjoint-orbit phase | **RESULT** | Expanding the spin coadjoint-orbit contact problem in `1/S` gives (SC.1), a rigorous pointwise remainder bound, the soft limit `delta'_S(0)=1/S`, and a successful frozen-data plus independent-ED comparison. |
| Kink Liouville pushforward | **DEAD for weights** | Conditional on a classical transmitted or reflected trajectory it gives a deterministic displacement.  A Gaussian blur of that classical coordinate is not the TPM law and would violate the exact-support fence if read literally.  The channel probabilities still require the scattering dynamics. |
| `[Q,R]` / quantization commutes with reduction | **NO EXTRA PURCHASE** | The precise useful statement is the multiplicity/index equality for `Q(M,L^n)` at weight `n xi` (with the usual regularity, and its singular extension), whose large-`n` normalized multiplicity measures give DH.  It proves the projective seed family.  No identification makes the state-specific TPM matrix elements into those indices, and the theorem contains no scattering phase. |

No L3 quotation is used.  The `[Q,R]` item is named only as standard
background and is not imported as a claim-bearing corpus citation.

## 2. Best route: the collective two-wave contact phase

### 2.1 Named phase space and expansion parameter

For a finite ring, the classical spin phase space is the product of coadjoint
orbits

`P_S = product_x O_S`,  `O_S ~= S^2`,  `Omega_S = S sum_x omega_KKS,x`,

with the diagonal `U(1)` moment map `sum_x S_x^z`.  Dividing the symplectic
form by `S` makes the effective semiclassical parameter `hbar_eff=1/S`.
The north-pole Darboux/Holstein--Primakoff chart gives, after rescaling time by
`JS`, a free spin-wave Hamiltonian at order one and a two-wave contact
interaction at order `1/S`.  Thus the `S=infinity` two-wave contact condition
has no phase, and the first nontrivial phase is order `1/S`.

Concretely, the two contact channels of the quantized orbit reduce to the
`S2-2body-S` contact equation

`W[(2S-1)a+b]=S Sigma a b`,

where `a=1+z_s z_h`, `b=z_s+z_h`,
`W=A z_h+B z_s`, and `Sigma=A+B`.  After division by `S` this is

`a[2W-b Sigma]+S^-1(b-a)W=0`.                              **(SC.0)**

At `S=infinity`, `2W-b Sigma=(A-B)(z_h-z_s)`, so regular scattering forces
`A=B`: the classical dilute waves pass with zero contact phase.  Write
`A/B=1+r_1/S+O(S^-2)`.  The next order of (SC.0) gives

`r_1=b(a-b)/[a(z_h-z_s)]=iF`.

This is the collective-coordinate derivation of the leading envelope.  It
uses the contact Hamiltonian obtained by quantizing the named orbit, but does
not fit or assume `F`.  Keeping the contact equation unexpanded produces the
closed branch formula below and hence all subleading coefficients.

This phase-space statement concerns dilute spin waves near one coadjoint-orbit
pole.  It is not a semiclassical derivation of the integer magnon charge.  The
charge sector is fixed before this expansion is taken.

For the actual coefficient, import the exact contact ratio from
`S2-2body-S`, as required by the finite-`S` value fence.  Put

`p=(k_s+k_h)/2`, `q=(k_s-k_h)/2`, `c_p=cos p`, `c_q=cos q`, `s_q=sin q`.

In the regular chamber `c_p s_q != 0`, the numerator used in the unitary form
of the exact contact ratio is

`n = -2 i S c_p s_q + exp(iq)(c_p-c_q)`

and `S_12=n/(-conj(n))`.  Separating its real and imaginary parts, taking the
continuous phase with `delta_S(0,k_h)=0`, and staying on the branch where the
denominator does not cross zero gives

`delta_S(k_s,k_h) = 2 atan( F/(2S+d) )`,                    **(SC.2)**

where

`F = c_q(c_p-c_q)/(c_p s_q)`,  `d=-1+c_q/c_p`.             **(SC.3)**

Equation (SC.2) is a reparameterization of the imported exact two-body
contact ratio, not a second finite-`S` proof.  Its new use here is to expose
and test the semiclassical hierarchy.  Expanding at fixed regular momenta,

`delta_S = F/S + G/S^2 + H/S^3 + O(S^-4)`,                 **(SC.4)**

with

`G = -F d/2`,  `H = F d^2/4 - F^3/12`.                    **(SC.5)**

The functions in (SC.3)--(SC.5) are fixed before any fit; there are no fitted
coefficients.

### 2.2 Soft limit and fluctuation discipline

At `k_s=0`, `p=k_h/2`, `q=-k_h/2`, hence `c_p=c_q`.  Direct differentiation
of (SC.3) gives

`F(0,k_h)=0`, `partial_s F(0,k_h)=1`, `d(0,k_h)=0`.

It follows that `G=O(k_s^2)` and

`partial_s delta_S(0,k_h)=1/S`.                             **(SC.6)**

Thus the proved `1/S` slope is exactly the leading semiclassical phase, while
the first subleading term cannot renormalize the linear soft coefficient.
This is compatible with, but does not evade, AMP: (SC.6) uses the physical
two-body phase already fixed by `S2-2body-S`; it does not infer an amputated
leg coefficient from a DH volume or a normalization factor.

**Fluctuation label.**  The coadjoint-orbit stationary-phase expansion puts
Gaussian corrections one power of `1/S` below the classical term.  The
checked mathematical statement is only that `G/S^2` is the first subleading
contact correction of exactly that size.  Identifying all of `G` with one
particular path-integral determinant is **SPECULATIVE** and is not needed for
the result.

### 2.3 Pointwise error model

Let `u=1/S`, `t=du/2`, and `x=Fu/(2+du)`.  When `1+t>0` and `|x|<=1`, the
geometric-series remainder in the denominator of (SC.2), together with
`|atan x-x|<=|x|^3/3`, gives

`|delta_S-(Fu-Fdu^2/2)|`
` <= |F|d^2u^3/[4|1+t|] + (2/3)|x|^3`.                     **(SC.7)**

This is the pointwise phase gate used for the new ED sequence.  It is a
derived bound, not an error bar fitted to that sequence.  For the frozen
wavepacket rows, whose observable is `partial_s delta` rather than `delta`,
the checker uses the declared descriptive gate `3%` on the compact recorded
set `k_s<=0.12`, `k_h=1.5`, `S in {1/2,1}`.  That derivative gate is post-hoc
in the honest sense that the rows were already frozen; the ED gate (SC.7) is
the coefficient-free falsifier.

## 3. Data comparison

### 3.1 Frozen soft-phase data

The twelve `A_ring_summary` rows of
`numerics/results/spin1-bc-falsifier.json` cover
`S in {1/2,1,3/2,2}` and `k_h in {0.8,1.5,2.4}`.  Every measured extrapolated
slope contains `1/S` inside its reported error; the largest displacement is
`0.338904` of that row's error bar.  This checks the leading limit, but the
same JSON already reported that comparison.

The new frozen comparison is the second-order finite-`k` envelope.  The eight
soft-window wavepacket rows give:

| `S` | `k_s` | measured `partial_s delta` | `F'/S` | `F'/S+G'/S^2` | relative error |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.03 | 1.061625477 | 1.091745672 | 1.061245612 | 0.0358% |
| 1 | 0.05 | 1.104386928 | 1.157200721 | 1.103294985 | 0.0989% |
| 1 | 0.08 | 1.171130810 | 1.262442059 | 1.168189164 | 0.2512% |
| 1 | 0.12 | 1.265129324 | 1.417417180 | 1.258039995 | 0.5604% |
| 1/2 | 0.03 | 2.064558477 | 2.183491345 | 2.061491103 | 0.1486% |
| 1/2 | 0.05 | 2.107614448 | 2.314401442 | 2.098778498 | 0.4192% |
| 1/2 | 0.08 | 2.171899084 | 2.524884118 | 2.147872537 | 1.1062% |
| 1/2 | 0.12 | 2.256253448 | 2.834834360 | 2.197325619 | 2.6118% |

All eight pass the `3%` derivative-envelope gate.  More sharply, adding the
parameter-free `G'/S^2` term improves every row, with minimum error reduction
`89.8151%`.  This is the first recorded comparison of those frozen measured
rows with the semiclassical truncation rather than with the full exact
two-body answer.

The frozen `soft_index_probe_results.json` is credited exactly as
**P1+P2(a)-only**.  P1 gives slopes `1.992924816` at `S=1/2` and
`1.021726489` at `S=1`, relative errors `0.354%` and `2.173%`.  P2(a)'s two
jet errors are `4.28e-8` and `5.45e-8`, far inside its `8%` band.  P2(b) is
neither read nor credited here; the open tracker defect says its
eta-insensitivity gate is a no-op.

### 3.2 Frozen memory data: calibration match, weight route rejected

Using the frozen `spin1-bc-falsifier.json` production prefixes, `dmax=1`
rows, and its already-used `trapped<10^-2` cut selects thirteen memory rows at
`S in {1/2,1,3/2}`.  Every `delta x_2/T` lies within the file's `8%` band of
`-1/S`; the worst relative difference is `2.6853%`.  There is no measured
`S=2` memory row in that JSON.  The `S=2` member of the stated four-spin set
comes from the phase `A_ring_summary`, not from memory; the checker makes this
absence a gate so it cannot silently manufacture a comparison.

The captured output of `memory_index_probe.py` has two gating geometries.
Their last recorded rows put respectively `0.99601` and `0.99753` on
`Q_W=-2`, with zero off-lattice mass.  In the probe's other convention this
is the corresponding `nu=+2` outcome.  These numbers test exact support and
late-time channel concentration, not a DH density.

The common `1/S` seen in the memory ratio is the kinematic conversion from a
unit transmitted charge to wall displacement.  The reported transmission
weights themselves vary with `Delta`, `k_0`, packet quality, and trapped
mass.  Neither (SC.1) nor a DH volume predicts them.  This comparison therefore
supports the shared semiclassical scale but is a red verdict for a DH law of
the weights.

### 3.3 New small-ring ED sequence

The checker independently enumerates the normalized two-magnon occupation
basis of the periodic `H_S` at `N=18`; it does not call the repository's
two-magnon module or evaluate the closed-form `S_12`.  Translation orbits
give the total-momentum block `K=2pi*5/18`.  In the scattering level with
Bethe integer difference `n_1-n_2=-3`, ED supplies `E`, and the free bulk
dispersion supplies the negative relative momentum through

`E=4S[1-cos(K/2)cos q]`.

The measured finite-volume phase is then

`delta_ED=Nq-pi(n_1-n_2)`.

This uses the finite-volume level displacement, not the exact contact-ratio
formula.  The comparison is:

| `S` | `delta_ED` | `F/S` | `F/S+G/S^2` | second-order residual | `S^3` times residual |
|---:|---:|---:|---:|---:|---:|
| 1/2 | 1.013280306 | 1.541586991 | 0.942021421 | 7.126e-2 | 0.008907 |
| 1 | 0.568297512 | 0.692506602 | 0.563984453 | 4.313e-3 | 0.004313 |
| 3/2 | 0.389091605 | 0.441863437 | 0.388280910 | 8.107e-4 | 0.002736 |
| 2 | 0.294903236 | 0.323784116 | 0.294654952 | 2.483e-4 | 0.001986 |
| 3 | 0.198290327 | 0.210739355 | 0.198243092 | 4.723e-5 | 0.001275 |
| 4 | 0.149243461 | 0.156131787 | 0.149228821 | 1.464e-5 | 0.000937 |
| 6 | 0.099797654 | 0.102806969 | 0.099794824 | 2.830e-6 | 0.000611 |
| 8 | 0.074947812 | 0.076625619 | 0.074946927 | 8.853e-7 | 0.000453 |

Every row lies inside (SC.7), the `G/S^2` term improves every row, the
second-order error decreases monotonically along the sequence, and
`max S^3|error|=0.008907361`.  The fact that even `S=1/2` lies inside the
bound is not used to call it semiclassical; the large-`S` sequence is the
claim-bearing comparison.

## 4. Why the Heckman seed is real but not the memory answer

Let `V=C_-1 direct-sum C_0^2 direct-sum C_+1` and
`M=P(V)=CP^3` with its stated circle moment map.  The first hunt computed

`mu_*(vol_FS)=(3/2)(1-|x|)^2 1_[−1,1](x) dx`.               **(SC.8)**

The correct asymptotic bridge is the geometric-quantization family

`Q_n=H^0(M,O(n)) ~= Sym^n(V^*)`.

If `mult_n(m)` is its circle-weight multiplicity, then the normalized
rescaled measures

`eta_n=[1/dim Q_n] sum_m mult_n(m) delta_(m/n)`

converge weakly to (SC.8), up to the harmless dual-weight sign convention.
At `n=1`, symmetry removes that sign and `eta_1` is exactly the atomic
`1/4,1/2,1/4` law.  This is the precise sense in which the two object types
in the seed meet asymptotically.

The same construction for a local spin uses
`H^0(CP^1,O(2S))=Sym^(2S)(C^2)` and gives the uniform DH density on the
rescaled local magnetization interval.  For a fixed window the product
orbit gives its convolution.  Those are normalized-trace multiplicity laws.
The memory protocol instead prepares one kink plus `O(1)` magnons, subtracts
the vacuum density, performs a two-time measurement, and takes an ordered
large-window/time limit with escaped charge tight.  Consequently:

1. dividing the escaped integer by `S` or `N_W` gives `delta_0`, not (SC.8);
2. declining to divide leaves the exact atomic law;
3. replacing the pure dynamical weights by normalized multiplicities changes
   the experiment; and
4. inserting the transmission probability as an equivariant weight inserts
   the answer.

Thus Heckman genuinely explains a large-representation envelope, just not
the envelope of the measured `{p_nu}` in this protocol.

## 5. Checker

Run:

```bash
python3 -O theory/checks/dh_semiclassical_check.py
python3 -O theory/checks/dh_semiclassical_check.py --red wrong-leading
python3 -O theory/checks/dh_semiclassical_check.py --red drop-fluctuation
```

Recorded green output:

```text
DHSC-C0-SHAPE PASS bare_asserts=0 optimization_safe=1
DHSC-C1-FROZEN-SLOPES PASS spins=1/2,1,3/2,2 ring_worst_error_fraction=0.338904 P1_worst_relative=0.021726 probe_scope=P1+P2(a)-only
DHSC-C2-FROZEN-FINITE-K PASS rows=8 ksoft<=0.12 worst_relative=0.026118 minimum_error_reduction=0.898151
DHSC-C3-MEMORY-SCOPE PASS calibration_rows=13 spins=1/2,1,3/2 worst_relative=0.026853 S2_memory_row=absent probe_min_p_Qminus2=0.99601 probe_max_off_lattice=0.0 interpretation=kinematic_not_DH-weight
DHSC-C4-INDEPENDENT-ED PASS N=18 K_index=5 Bethe_difference=-3 spins=0.5,1.0,1.5,2.0,3.0,4.0,6.0,8.0 delta_Shalf=1.013280306 delta_S8=0.074947812 max_S3_error=0.008907361 last_error=8.853e-07 last_bound=7.112e-05
ALL DH-SEMICLASSICAL GATES PASS
```

Both registered mutations exit `1`.  `wrong-leading` changes the leading
coefficient `1/S` to `2/S` and is caught by frozen row C1.
`drop-fluctuation` removes `G/S^2` and is caught by the finite-`k` frozen-data
gate C2.  The script has no bare `assert` and the data comparison is gating.

## 6. MERGE PROPOSALS

1. **Companion paper — accept.**  Add (SC.2)--(SC.7), the eight-row frozen
   finite-`k` comparison, and the `N=18` large-`S` ED table under a heading
   “Coadjoint-orbit soft envelope.”  Label the `G`/Gaussian-determinant
   identification speculative, while keeping the `1/S` expansion and ED
   comparison as the result.
2. **Letter §7 — discussion clause only.**  Proposed text: “For the isotropic
   spin-`S` two-magnon oracle, the exact phase has a coadjoint-orbit expansion
   `delta_S=F/S+G/S^2+O(S^-3)`; the `1/S` soft slope is its leading term and
   the first correction begins beyond the linear soft jet.  This controls a
   phase envelope, not the superselected support or dynamical weights of the
   memory law.”
3. **Do not merge a DH claim for `{p_nu}`.**  The only honest Heckman statement
   is the `O(n)` projective multiplicity limit in §4.  It may be included as a
   clarifying contrast, but must not be cited as predicting transmission or
   TPM probabilities.
