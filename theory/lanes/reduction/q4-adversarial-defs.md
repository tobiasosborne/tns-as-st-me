# Q4 hostile audit: definitional correspondence to continuum objects

## 0. Scope, test, and status discipline

This is an adversarial correspondence audit, not an audit of the lattice algebra alone.  For each requested family I ask whether there is a controlled sequence of lattice spacing, volume, time, wave-packet, and observation-window limits in which the campaign object becomes the object bearing the same name in the continuum literature.  Exact finite-lattice identities survive this audit only if the limiting object and its quotient structure, locality, spectrum, and operational meaning survive too.  The three failure modes are: **limit obstruction**, **wrong-object identification**, and **degenerate-instance/nonvacuity failure**.

The claim-status distinction is load-bearing.  The following lattice implications are marked PROVED and therefore receive the sharpest scrutiny: `A1` (using D4), `G0` (using D5/D12), `ML5-B` and `D24-VAL` (using D24, both explicitly conditional), `M-INDEX-fin`, `M-INDEX-spec`, `M-IDX-density`, `LR1-GEN`, `LD-ID`, `B3`, `M-flux`, `M-quant(-G)`, `AC-EX` (using D5/D28, conditional), and `AC-EX-2M` (using exact D31 data).  A proof of `P => Q` does not establish that `P` is the discretisation of an accepted continuum hypothesis, nor that `P` has any microscopic member.  In particular:

- `ML5-B` is a proved implication on `S_W(rho)`, while microscopic membership and even nonemptiness remain open.
- `M-INDEX-spec` assumes D27(LR); only LR1 is proved generically (`LR1-GEN`), while LR2--LR3 do the substantive work.
- `AC-EX` assumes exact ansatz band maps and the two-cluster estimate D28-C, which the claims table says are unverified on every model.
- `AC-EX-2M` is genuinely instantiated on D6, but is fixed-packet only and explicitly has no soft-uniform control.

I use **[physical argument]** for continuum-limit and scattering reasoning not presented as a rigorous theorem here, and **[textbook]** for standard structures such as Fock asymptotics, Gauss-law generators, flux spectra, and soliton collective coordinates.  Continuum evidence below is quoted only from the required local TeX sources, with file and line number.

## 1. D13: the wall coordinate and its two dresses

### 1.1 What `X_W` converges to

Restore a lattice spacing `ell`, write the saturated spin density as `M_0=s/ell`, and convert the dimensionless D13 observable to a physical length.  Its Riemann-sum limit is

`X_W^phys = x_a + (2M_0)^(-1) integral_W dx [m_z(x)+M_0]`

up to the one-site endpoint convention.  For a one-parameter rigid wall `m_z(x)=M_0 f(x-X)` with `f(-infinity)=+1`, `f(+infinity)=-1`, this gives

`X_W^phys = X + C_f + exponentially small edge terms`,

where `C_f=(1/2) integral dy [f(y)+1-2 Theta(-y)]` is a profile-dependent centering constant.  For the usual antisymmetric `tanh` wall, `C_f=0`.  Thus D13(a) really does have an accepted continuum target: it is a discretisation of a soliton collective coordinate on the rigid one-wall moduli space.  [textbook]

But D13(a)'s stated semantic conditions only put the propagating packet outside `W` and pad the core from the edges.  They do **not** hold the core profile or its integrated charge fixed.  A change of charged core dressing at fixed geometric center changes `X_W` by exactly the same amount as a translation.  More generally,

`Delta X_W^phys = Delta X + Delta C_f + (Delta core charge)/(2M_0)`.

This is a **wrong-object ambiguity**: `X_W` is an integrated relative charge, and becomes “position” only after a centering/dressing convention not present in D13.  The sharp-wall calibration proves one value on one configuration; it does not identify the observable on the whole kink sector.  [physical argument]

It is not a Bondi-type falloff coefficient under any direct limit.  Accepted gravitational memory is the detector displacement `Delta s` determined by the change `Delta C_zz`; the local canon says the detectors sit where there is no early/late Bondi news and gives `Delta s^bar z=(gamma^{z bar z}/2r) Delta C_zz s^z` (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:2582-2595`).  The earlier memory paper instead defines the datum as an asymptotic metric jump and says it “approaches finite but different values” at early and late retarded time (`refs/arxiv-1411.5745/memory_4.tex:688-695`).  Neither object is a volume integral of matter charge.  D13 can model the same *response logic*, but a 1D wall charge does not converge to a null-infinity field coefficient merely by sending `ell -> 0` or `W -> R`.  [physical argument]

**Verdict on D13(a): survives narrowly as a collective-coordinate discretisation, but not as an unqualified wall position and not as a Bondi observable.**  A continuum claim must carry the rigid-profile/fixed-core-charge condition.  Its absence is a **MAJOR caveat**, because `B3`, `M-flux`, `M-quant(-G)`, `M-INDEX-fin/spec`, `LD-ID`, and `AC-EX` all use D13's normalization or observable.

### 1.2 The spectral dress is kinematics, not identification

D13(b) is an exact finite-window identity: integrate `dot m_x` and sum.  It has the same Fourier-residue form as the continuum relation

`Delta h^TT = (4 pi i r_0)^(-1) lim_(omega->0)[-i omega h^TT(omega)]`

under the stated finite-endpoint and `omega r >> 1` assumptions (`refs/arxiv-1411.5745/memory_4.tex:688-695`).  This correspondence survives.  What does not follow is that the quantity whose residue was taken is the accepted radiative field, or that its residue is a soft amplitude.  The continuum paper makes the extra amplitude identification separately (`refs/arxiv-1411.5745/memory_4.tex:698-700`).  Therefore the “spectral dress” is a valid Fourier rewrite of D13(a), but it supplies no evidence that D13(a) has become gravitational, electromagnetic, or pion memory.  [physical argument]

### 1.3 The conserved-center trap exists in the continuum, but D13(c) is not actually a dress

The continuum analogue of the trap is standard.  In a ferromagnet, translating a wall by `Delta X` changes the wall contribution to the conserved spin by `2M_0 Delta X`.  Total spin conservation therefore forbids a change of the *wall plus all radiation* charge; a wall can move only because spin crosses the subsystem boundary or is deposited by an asymptotic leg.  [textbook]  Continuum soliton dynamics evades the apparent zero by decomposing the conserved total charge into wall and radiation/reservoir pieces, then following the wall piece.  D13(a)'s fixed-window ordering is a lattice implementation of that open-subsystem decomposition once the legs have separated.  In this respect the trap is real and the physical cure is the same charge ledger.

There is nevertheless a definitional failure in D13(c).  The displayed `X_1(t)` is exactly the conserved regularised total magnetisation, so its displayed `delta x^dyn` is identically zero.  Merely “invoking D18” cannot change the value of the formula.  One must first replace `X_1` by a new, explicitly leg-subtracted operator or channel-dependent functional; D18 states channel/local-decay hypotheses but does not define that replacement.  Hence D13(c), as written, is **not a second characterisation of D13(a)**.  It is a deliberately trapped zero together with prose pointing toward an undefined corrected observable.

**Rat D13-dyn:** any downstream use of the displayed `delta x^dyn` as nonzero memory is invalid.  Severity is **MAJOR caveat**, not fatal to results using D13(a): the proved memory rows use the window observable/charge ledger, while the dynamic “dress” itself has no nonzero continuum or lattice instance until the subtraction is separately defined.

## 2. D26 and D27 as a package

### 2.1 INT survives only for the global compact charge

D26(INT) has a clean continuum ancestor in the narrowest sense.  A compact `U(1)` representation has a weight lattice, so after normalization the global matter charge is integral.  The QED canon defines

`Q_E=(1/e^2) integral_(S^2) *F = integral_Sigma *j in Z`

and explicitly chooses the electron to have charge one (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:457-461`).  [textbook]  This is the continuum version of `spec S_x^z subset kappa+Z` and of offset cancellation in a difference measured with the same normalization.

That is **not** the spectrum of a generic asymptotic/large-gauge charge.  The same source defines one charge for every boundary function `epsilon` (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:647-657`).  After Gauss' law it splits as

`Q_epsilon = Q_epsilon^soft + Q_epsilon^hard`,

where the hard matter charges are weighted by arbitrary angle-dependent values and the soft term is linear in the electromagnetic field (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:699-711`).  Even if every particle charge is an integer, `sum_k epsilon(Omega_k) Q_k` is not integer-valued for a generic real function `epsilon`, and the radiative field contribution is not an on-site weight-lattice operator.  Thus D26 discretises the constant global `U(1)` mode, not the continuum charge family that carries soft memory.

**Rat D26-asymptotic:** identifying D26(INT) with integrality of large-gauge/BMS-type memory charges is a wrong-object identification.  It is **FATAL to that 3+1 continuum claim**, while harmless for the finite-window lattice arithmetic `M-INDEX-fin` actually proves.

### 2.2 LR is an FCS protocol, not the accepted memory hypothesis

D27 does three things beyond ordinary relaxation: it chooses the spectral PVM of a bounded finite-window relative charge; inserts two projective measurements and a dephasing map; and requires first-moment tightness of the resulting charge-transfer laws as the window grows.  This is a legitimate full-counting-statistics protocol.  [textbook]  It is not the hypothesis used in the accepted memory statement.  The latter assumes that a radiative field approaches finite early and late values and extracts their Fourier residue (`refs/arxiv-1411.5745/memory_4.tex:688-695`); the QED/gravity canon defines gravitational memory directly by the permanent detector displacement and `Delta C_zz` (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:2582-2595`).  Neither statement contains a projective charge measurement, nondemolition/dephasing condition, common double-Cesaro subsequence, or integer first-moment-tight law.

LR1 is generic compactness (`LR1-GEN`); it contributes essentially no physics.  LR2 is a measurement-backaction assumption specific to this TPM protocol.  LR3 rules out charge histories whose first moment escapes to larger and larger values with the window.  These clauses are sufficient to manufacture a subsequential integer-supported law, but no accepted continuum memory theorem was found whose physical falloff hypotheses discretise to LR2--LR3.  At most, a finite-particle soliton scattering problem can be *additionally instrumented* this way.  That is a new charge-transfer observable, not a discretisation forced by continuum memory.

The claim status makes this more serious, not less: `M-INDEX-spec` is PROVED only as `(INT)+(LR) => integer-supported TPM law and first-moment ledger`; it does not prove LR, and it does not prove that the TPM law is a continuum memory observable.  The theorem is mathematically sound while its continuum naming is unearned.

### 2.3 Explicit free-radiation stress test

Consider the asymptotically free Maxwell radiative sector of a scattering solution, separated from the hard charged sector that fixes the constraint data.  The local canon explicitly says that even free Maxwell has infinitely many large-gauge symmetries (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:852-860`).  Its soft mode is

`integral du F_uz^(0) = A_z^(0)|late - A_z^(0)|early`,

with the endpoint fields pure gauge for finite energy (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:735-743`).  Choose scattering data whose free radiation-zone field has a smooth finite-energy pulse and a nonzero such endpoint shift; the hard sector supplies the associated Gauss-constraint change, while the asymptotic radiative evolution is free.  This is accepted electromagnetic soft memory: the canon describes the abelian effect as a relative phase measurable by adjacent charged probes (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:2651-2655`).  [physical argument]

Now naively transplant D27:

1. If `Q_hat_W` is the compact **matter charge** and D27 is naively applied to the separated free radiative sector, that sector has no matter charge.  Every PVM is the zero-charge PVM, every TPM law is `delta_0`, and D27 returns zero.  The accepted soft mode above can nevertheless be nonzero.  The transplant is **vacuous**.
2. If `Q_hat_W` is replaced by the radiative field memory coordinate, it is a field quadrature/zero mode with continuous spectrum, not one coset of `Z`; D26 fails and the support theorem disappears.  [textbook]
3. If one instead substitutes photon number merely to recover an integer spectrum, one has changed the symmetry charge and the observable.  Moreover, a sharp memory step is represented by an infrared coherent cloud whose number need not be finite even when its energy and classical memory are finite, so D27's first-moment tightness can fail.  [physical argument]

The same obstruction is even plainer for gravitational memory: `Delta C_zz` varies continuously with the hard momenta in the Braginsky--Thorne formula (`refs/arxiv-1411.5745/memory_4.tex:680-684`), so no integer on-site circle spectrum can be its direct discretisation.

**Verdict on the package:** D26+D27 survives as an integer charge-transfer/FCS theorem for a compact-charge domain wall.  It **does not reduce to accepted electromagnetic or gravitational memory**.  Calling its law a general “memory index” is a **MAJOR wrong-object caveat**; using it as the continuum memory theorem is **FATAL**.  A nonvacuous continuum counterpart would have to be stated explicitly as soliton-position full counting statistics, not as radiative memory.

## 3. D24: the engineered universality class `S_W`

### 3.1 What the continuum sources actually restrict

The requested continuum sources do have restrictions, but they are not D24's source restriction.

- The textbook QED formula is written for plane-wave in/out states (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1035-1049`) and the Ward identity is said to relate “any pair of incoming and outgoing states” (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:916-925`).  The same text discusses wavepackets as ordinary scattering initial data (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:513-515`).  It does not impose compact support or a no-contact condition on an interpolating source.  It also warns that conventional QED Fock-basis S-matrix elements vanish because of infrared divergences (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1767-1768`), so “accepted Fock states” is itself only the textbook/formal register in QED.
- The soft-pion paper starts from mode expansions and defines one-particle states by creation operators on the free vacuum (`refs/arxiv-1709.05018/draft1004.tex:216-232`).  Its theorem is between asymptotic multiparticle states with no soft pion before the insertion (`refs/arxiv-1709.05018/draft1004.tex:323-350`).  Again there is no local-source subclass.
- The type-B paper assumes a genuine single-soft kinematics: the selected momentum is scaled to zero while the other external momenta remain nonzero (`refs/arxiv-2201.01393/manuscript.tex:81-87`).  Its current argument allows in/out states containing an arbitrary number of NG bosons or other particles (`refs/arxiv-2201.01393/manuscript.tex:418-423`).  The extra assumption is regularity of the current remainder in the simultaneous on-shell/soft limit (`refs/arxiv-2201.01393/manuscript.tex:423-439`).

I found **no smooth-compact-support state-class hypothesis in the four required TeX sources**.  Smooth packets are a rigorous/operational replacement for their generalized plane waves, and D3/D12's `C_c^infinity` packet discipline is reasonable.  [textbook]  But this only supports D24(b)'s packet topology.  It does not support D24(d)'s five source conditions.

### 3.2 The closest continuum analogue, and where the analogy stops

There is a genuine analogue of part of `S_W`: the regularity assumption on `R^mu`.  The continuum source also explains its failure mechanism—additional soft singularities can arise when the current inserts on external legs, for example through bilinear current terms (`refs/arxiv-2201.01393/manuscript.tex:433-439`).  D24's direct-contact and reduced-channel clauses are trying to exclude precisely this kind of obstruction.  Likewise, continuum soft bootstrap can classify **theories** by locality, factorization, symmetry, and assumed soft data (`refs/arxiv-2201.01393/manuscript.tex:89-95`).

The mismatch is categorical:

1. Continuum regularity is a property derived from or assumed about a theory/current and then applied to its asymptotic amplitudes.  `S_W` is a class of **local sources `O` inside one microscopic theory**, selected by conditions on the very amplitudes whose factorization is at issue.
2. D24(d)1 assumes an exhaustive LSZ decomposition; (d)4 assumes the reduced channel is already `O(k^2)`; (d)5 assumes the direct contact is already `O(k^2)`; and (d)2--3 impose the desired external-leg residue/profile.  Together with the zero-intercept/zero-first-jet criterion D24(c), these conditions are nearly the conclusion unpacked into membership clauses.
3. In accepted LSZ scattering, changing a local interpolating operator without changing the normalized asymptotic state does not change the S-matrix.  [textbook]  If `M_2^O` retains an arbitrary source contact jet while `M_1^O` is fixed, the object is a source-dependent form factor or preparation amplitude, not yet the source-independent asymptotic S-matrix.  D24(e)'s `O_eta` family demonstrates exactly that dependence.

There is a respectable continuum object nearby: soft Ward identities for **operator insertions** include contact terms involving the symmetry variation of the inserted operator.  Restricting to invariant/covariant operators can remove them.  [textbook]  But D24 has not shown that `O in S_W` is equivalent to a natural symmetry-invariant operator class; it defines membership through amplitude decomposition and jet bounds instead.  Thus `S_W` is best read as an on-shell bootstrap/test class, not as a discretisation of the continuum's smooth-wavepacket or Fock-state domain.

### 3.3 Nonvacuity is the rat

D24 itself states that no nontrivial microscopic class is proved to satisfy all five conditions and that nonemptiness remains open.  The claims DAG correspondingly marks `ML5-B` PROVED only as a conditional implication, `S-general` CONJECTURE, `AMP` CONJECTURE, and even `D24-VAL` as a proved implication with “VACUOUS-OR-UNKNOWN” antecedents.  Therefore:

- As a logical definition, `S_W` is consistent and D24(c)/`ML5-A` correctly characterise its required first jet.
- As a claimed universality class corresponding to accepted continuum scattering, it presently has no physical content.  No limit sequence can be exhibited because there is no lattice member to put on the sequence.
- Calling the `ML5-B` implication a lattice soft theorem in the accepted sense hides the central burden—showing that a natural microscopic source/state class lands in `S_W`—inside the definition.

**Rat D24-class:** this is a **degenerate-instance/nonvacuity failure** and a **wrong-object identification**.  Severity is **FATAL to any present continuum soft-theorem claim based on `ML5-B`/`S-general`**.  It is only a **MAJOR caveat** if advertised honestly as a conditional bootstrap criterion awaiting a membership theorem.  The packet/amputation conventions of D24(b) survive; the five-condition “universality class” does not yet have the continuum status its name suggests.

## 4. D5/D12: an ansatz is not a particle definition

### 4.1 Missing spectral data

The accepted objects are asymptotic spectral states.  The soft-pion source defines one-particle states by asymptotic creation operators acting on the free vacuum (`refs/arxiv-1709.05018/draft1004.tex:216-232`) and states its soft theorem as an S-matrix relation between asymptotic multiparticle states (`refs/arxiv-1709.05018/draft1004.tex:323-350`).  The type-B current argument extracts the physical amplitude from the on-shell NG pole between in/out states (`refs/arxiv-2201.01393/manuscript.tex:418-431`).  [textbook]  The common defining data are a Hamiltonian spectral shell/pole, normalized asymptotic states, and an in/out map.

D5 has none of these.  It defines a momentum superposition of one replaced MPS tensor and quotients a telescoping null direction.  It does not mention the Hamiltonian, require `H Phi_k=omega(k) Phi_k`, isolate a band from continuum, control a resolvent pole, or construct a wave operator.  D12 proves only that the two boundary terms left by summation by parts vanish in specified packet or delta-normalized senses.  Vanishing of a tangent-space gauge remainder is not an LSZ condition.

The soft regime makes the gap dangerous rather than benign.  For a type-B mode `omega(k)~k^2`, a variational residual or mixing with a multiparticle threshold must be controlled uniformly at least relative to the shrinking spectral scale.  D5/D12 provide no such estimate.  A tensor `B` can parameterize an excellent fixed-momentum variational vector yet cease to select any isolated asymptotic particle as `k->0`.  [physical argument]  Therefore there is no generic limit sequence from “D5 leg” to accepted Fock/Haag--Ruelle leg.

**Rat D5-name:** calling the D5 quotient class a “particle” or using it as an external scattering leg without extra spectral hypotheses is a wrong-object identification.  Severity is **MAJOR**.  D12 survives as a correct kinematic/gauge statement, but it cannot cure the spectral defect.

### 4.2 Exact registers where the correspondence does survive

The problem disappears when exactness is added independently:

- D6's one-magnon plane waves are exact eigenstates, and the Bethe/Jacobi rows `S2-2body(-S)`, `ML1`, and `ML2` use the actual model spectrum rather than variational faith.
- D31 assumes a Gram-normalized exact band map, exact momentum-filtered creators, spectral isolation/inelastic inventory, and then constructs fixed-packet Cook limits.  `AC-EX-2M` is instantiated on D6 and is a genuine asymptotic-state theorem in its stated fixed-packet domain.
- D28 likewise assumes exact kink and magnon band maps and a two-cluster estimate before `AC-EX` constructs its channels.  But D28-C and the exact ansatz bands are unverified on every model, and D28 explicitly excludes the soft endpoint.  This is a coherent conditional theorem, not a continuum soft-particle construction.

### 4.3 Did a PROVED row silently cross the gap?

After the campaign's repairs, I find **no present PROVED row that silently crosses it**:

- `G0` uses D5 to express the exact charge-created vacuum vector and its summation-by-parts identity; it does not assert that a generic `B_G` is an asymptotic eigenparticle.
- `A2` concerns exact weak-* sector change under half strings, not particle scattering, despite listing D5 among its dependencies.
- `A1`/`ML4-A` use only the relevant algebraic or packet remainder facts.
- `AC-EX` states exact-band and cluster data as hypotheses and advertises the absence of a soft limit.
- `AC-EX-2M` states and instantiates the exact band data, while explicitly denying soft-uniform Cook bounds.
- `ML1-D31-kernel`, the remaining bridge from exact band rigging to D24 unit-weight external kernels, is only SKETCH.

This is a survivor with an important wording fence: **D5 defines an excitation ansatz, not “particle”; D28/D31 or an independent spectral theorem defines the particle.**  The serious residual is nonvacuity of the kink register, not a hidden invalid inference in a currently PROVED row.

## 5. Independent 3+1 compact Hamiltonian lattice-QED transplant

### 5.1 The target algebra

On an oriented cubic spatial lattice, compact Hamiltonian `U(1)` gauge theory assigns `L^2(U(1))` to every link.  The link holonomy `U_l` and electric field `E_l` obey

`[E_l,U_l]=U_l`, `spec E_l=Z`.

At a vertex `x`, the Gauss generator is

`G_x = sum_i(E_(x,i)-E_(x-i,i)) - rho_x`.

Physical vectors obey `G_x|phys>=0` for gauge transformations treated as redundancies.  Summing over a finite region `R` cancels every interior link and gives

`sum_(x in R) G_x = Phi_(partial R)-Q_R`,

where `Phi_(partial R)` is the oriented electric flux through all boundary links and `Q_R=sum_(x in R)rho_x`.  Thus, on the physical Hilbert space, a truncated **matter** phase rotation is represented by boundary electric flux.  [textbook]

This is precisely the accepted Gauss structure: the continuum canon writes electric charge both as a boundary flux and as a bulk current integral, with integer normalization (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:457-461`).  For angle-dependent boundary parameter `epsilon`, however, the charge includes both a soft field term and a hard current term (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:699-711`).

### 5.2 D4 transplant: four mismatches

There are two possible transplants, and neither yields D4's claimed asymptotic object.

**Full local gauge transformation.**  Transplant `G` in D4 as the vertex gauge group and apply it in `R`.  The operator is `exp(i sum_(x in R) alpha_x G_x)` and acts as the identity on physical states for parameters belonging to the redundant gauge group.  Its D4 state orbit is therefore a point.  Boundary charge appears only after distinguishing gauge transformations that remain nonzero at the boundary from those treated as constraints.  The accepted quotient is

`ASG = allowed gauge symmetries / trivial gauge symmetries`,

where “trivial” means acting trivially on physical data (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1195-1204`).  This quotient is fixed by boundary conditions and Gauss' law, not by whether a state-dependent virtual matrix is scalar.

**Truncated matter/global rotation.**  Transplant D4's on-site string as `exp(i alpha Q_R)`.  Gauss' law converts it to `exp(i alpha Phi_(partial R))`, so the endpoint idea survives.  But its endpoint is a two-dimensional boundary surface carrying one rotor flux per boundary link (and, in the continuum, one mode per boundary function), not a single `chi`-dimensional bond matrix.  The continuum explicitly has one conserved charge for every boundary function (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:647-657`) and large transformations do not die at infinity (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:852-860`).

The resulting failures are:

1. **Quotient mismatch.** D4 divides by `N_alpha={g:V_alpha(g) is scalar}` because phases are invisible on one state.  QED divides allowed transformations by Gauss redundancies/trivial boundary action.  A constant `U(1)` phase may be scalar on a fixed charge sector yet is physically measurable as a character across different charged sectors and appears in the hard soft factor.  D4's state-level `PGL` quotient discards exactly that sector information.
2. **Locality mismatch.** D4's residue is a virtual insertion defined only through padded MPS windows.  `Phi_(partial R)` is a physical boundary-link observable (or an edge-mode generator after a gauge-theory factorization choice).  It is not a single local bond degree of freedom.
3. **Spectrum/dimension mismatch.** Compact-QED electric flux is unbounded integer-valued.  A fixed finite `M_chi` bond cannot realize the rotor algebra exactly: `[E,U]=U` makes a unitary `U` shift every electric-field eigenvalue upward by one, which is impossible for a finite spectrum (equivalently the conjugation relation conflicts with determinants in finite dimension).  [textbook]  A QED limit would require `chi->infinity` plus a boundary-surface tensor product and a proved convergence of the flux algebra.  D4 contains no such limit sequence.
4. **Algebra mismatch.** Basic abelian Gauss charges commute and their nontrivial structure is the boundary function space and soft/hard split.  D4's load-bearing extra datum is a finite-dimensional projective multiplier/twisted group algebra.  That SPT multiplier is not the QED Gauss-charge algebra.

**Rat D4-QED:** the finite-chi bond implementer does not transplant to the accepted 3+1 QED boundary charge.  This is a **limit-sequence obstruction** and **wrong quotient**, severity **FATAL** to a QED/asymptotic-gauge interpretation of D4.  The only surviving statement is the schematic Gauss slogan “a truncated symmetry leaves boundary data.”

### 5.3 D26 transplant: the integer survives, the object does not

D26 can be instantiated in two elementary ways:

- set `S_x^z=rho_x` for integer-normalized matter charge; or
- relabel a link as the local cell and set `S_l^z=E_l`, for which `exp(2 pi i E_l)=I` and `spec E_l=Z`.

So `(INT)` with `c=1` correctly captures compact-QED charge/flux integrality.  D26's more general offset `kappa+Z` may describe background/projective matter conventions, but ordinary compact `U(1)` gauge rotors have the single-valued `c=1` spectrum.  [textbook]

What D26 does **not** produce is the Gauss charge.  A sum of matter charges becomes boundary flux only after imposing `G_x=0`; a sum of unoriented link electric fields is not the boundary flux at all; and an angle-dependent asymptotic charge also contains the soft radiative term.  D26 has no incidence matrix, Gauss constraint, boundary-condition quotient, or soft mode.  Therefore it supplies the integer arithmetic used by `M-INDEX-fin`, but not a definition of QED boundary charge.

**Verdict D26-QED:** **survives as a minor arithmetic component**, with a **MAJOR wrong-object caveat** if called the QED circle/boundary charge.  The D4+D26 package does not recover compact Hamiltonian lattice QED without adding Gauss constraints, link/surface edge modes, `chi->infinity`, and the correct allowed/trivial gauge quotient.

## 6. Ranked rat list and survivors

### 6.1 Rats, most severe first

1. **FATAL to the continuum soft-theorem claim — D24(d), `S_W`.**  The class is source-dependent, selected by amplitude conditions that substantially restate the desired factorization, has no proved microscopic member, and is not the asymptotic-state domain used by the continuum theorems.  `ML5-B` remains a correct conditional implication; it is not presently a nonvacuous continuum soft theorem.
2. **FATAL to the 3+1 QED claim — D4.**  Fixed finite-`chi` `PGL(chi)` bond implementers have the wrong quotient, locality, boundary multiplicity, and spectrum.  No limit sequence in D4 yields the unbounded integer electric-flux algebra or the angle-dependent allowed/trivial-gauge quotient.
3. **FATAL if advertised as generic continuum memory — D26+D27.**  The package measures integer compact-charge full counting statistics.  An asymptotically free Maxwell radiative sector can carry a nonzero soft endpoint shift while its D27 matter-charge TPM is `delta_0`; using the field shift instead destroys INT.  Gravitational `Delta C_zz` is continuous.  Hence the package is not electromagnetic/gravitational memory.
4. **MAJOR — D13(a), charged-dressing ambiguity.**  `X_W` tends to a soliton center only for a fixed/centered core profile.  D13's stated packet-outside/padding conditions do not prevent core-charge or profile changes from masquerading as translation.
5. **MAJOR — D13(c), undefined subtraction.**  The displayed dynamical coordinate is exactly conserved and its displayed memory is zero.  D18 does not itself define the leg-subtracted replacement needed for a nonzero dress.
6. **MAJOR — D5 as “particle.”**  D5/D12 provide a tangent/ansatz quotient and boundary-remainder limit, not a spectral band, pole, or wave operator.  The identification is valid only after D28/D31-type exactness or a separate spectral theorem.
7. **MAJOR — D26 as asymptotic QED charge.**  INT captures the constant compact `U(1)` weight lattice, not generic angle-weighted large-gauge charges with their continuous soft field term.  This is independent of the D27 failure.
8. **minor wording — D13(b), “spectral dress.”**  It is an exact Fourier rewrite of the finite-window response, but the word “spectral” can suggest a soft-amplitude or radiative-field identification that the identity does not provide.
9. **minor QED scope — D26's phase `c`.**  Ordinary compact-QED rotor flux has `c=1`; nontrivial offsets require additional background/projective matter structure and should not be presented as the generic gauge-field case.

### 6.2 Definitions/components that survived the hunt

- **D13(a), narrowly:** it is a sound discretisation of a centered rigid soliton collective coordinate, with fixed core charge/profile and asymptotic legs outside the window.
- **D13(b):** at fixed window with integrable time derivative, it is exactly the accepted endpoint-jump/Fourier-residue kinematics.
- **D26(INT), narrowly:** it is the correct local arithmetic for a compact global `U(1)` charge or a `c=1` compact-QED rotor flux.
- **D27, renamed:** it is a coherent conditional TPM/full-counting-statistics definition for lattice charge transfer; its theorem should not be renamed radiative memory.
- **D24(a)--(c):** locality/quasi-locality, packet norms, amputation conventions, and the zero-intercept/first-jet criterion are useful analytic definitions; they do not establish `S_W` membership.
- **D5/D12, narrowly:** they correctly define the MPS excitation ansatz, its gauge redundancy, and the regimes in which the boundary remainder vanishes; exact particle status must come from elsewhere.
- **D4, internally:** it is a valid finite-1D-MPS virtual endpoint construction on padded windows and states.  What fails is the identification with 3+1 QED boundary Gauss charges.

## 7. Bottom-line referee verdict

Rats were found.  The campaign has several exact and useful lattice definitions, but three continuum-facing identifications fail at the definitional level before any hard analysis begins: `S_W` is an uninhabited source bootstrap class rather than the continuum asymptotic-state domain; D4's finite virtual quotient is not the compact-QED boundary gauge algebra; and D26+D27 is integer charge-transfer FCS rather than generic radiative memory.  D13 has a legitimate soliton-coordinate limit only after adding a fixed-core centering condition, while its displayed dynamical dress is identically zero.  D5/D12 are honest ansatz technology, not a particle definition.

Accordingly, the safe continuum claims are narrower than the names: **collective-coordinate charge ledger**, **finite-window Fourier response**, **compact-charge TPM statistics**, and **conditional exact-band scattering**.  Calling these, without the missing bridges, the accepted continuum memory/soft/asymptotic-symmetry objects would be misleading.
