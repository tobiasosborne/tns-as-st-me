# R2+R4 reduction: lattice Ward structure and the continuum infrared triangle

## 1. R2 — dimensional specialization of the asymptotic symmetry

### 1.1 What becomes of “one charge per angle” in 1+1 dimensions

The continuum construction has a charge for every angular smearing function.  In the soft-pion example the unsmeared charge is labelled by the null direction `q-hat` and the resulting charges are explicitly said to form an infinite family (`refs/arxiv-1709.05018/draft1004.tex:359-412`).  Equivalently, the smeared charges are integrals against an arbitrary function `epsilon(theta)` on `S^2` (`refs/arxiv-1709.05018/draft1004.tex:469-481`).

In one spatial dimension an asymptotic massless ray has only two possible directions.  The celestial sphere is therefore

`S^0 = {L,R}`,

so a `G`-valued function on it is exactly a pair `(g_L,g_R)`.  Constant functions form `G_diag`, and removing the ordinary global transformation gives the homogeneous space

`Maps(S^0,G)/G_diag = (G_L x G_R)/G_diag`.

This is the full dimensional specialization of the angular construction: there are two directional charges and one relative charge after quotienting the common mode.  There are no higher angular harmonics on `S^0`.  Thus the infinite tower which is essential in four-dimensional BMS/large-gauge applications is absent in 1+1 dimensions by geometry, not because space was discretized.  A continuum quantum field theory in 1+1 dimensions has the same two-point celestial set.

For nonabelian `G`, `(G x G)/G_diag` is a homogeneous space, not naturally a quotient group, because `G_diag` is not normal.  As a set (and manifold) it is identifiable with one relative `G` element, but a canonical group law exists only when the relevant quotient subgroup is normal.  This is the same correction already enforced by claim **A1**.

### 1.2 Exact comparison with corner A

In the unbroken case, **WI** proves that a symmetry restricted to a finite interval leaves only `V_alpha(g)^{-1}` and `V_alpha(g)` on its two boundary bonds.  Sending the two ends to opposite infinities therefore realizes the two entries `(g_L,g_R)` of `Maps(S^0,G)` as left- and right-end operations.  This is not merely a visual analogy: the bulk action telescopes exactly to the two endpoints.  Claim **A1** then computes the physical stabilizer and orbit:

`S_alpha = {(g_L,g_R) : g_L g_R^{-1} in N_alpha}`,

`orbit = (G x G)/S_alpha ~= G/N_alpha = A_eff`.

When the virtual action is faithful, `N_alpha={e}`, this is precisely the `S^0` homogeneous space `(G x G)/G_diag`.  When `N_alpha` is nontrivial, the continuum directional parameterization overcounts transformations which act trivially on the lattice state; corner A removes that kernel and obtains `A_eff=G/N_alpha`.  The finite-dimensionality agrees with the continuum specialization and is forced by dimension.  The quotient by `N_alpha` is additional microscopic information.

Corner A is also finer in two other respects.

First, in the broken case the objects being classified are asymptotic vacuum pairs, not two independent transformations of one fixed vacuum.  Under hypothesis (T), **A2** gives

`Omega_vac x Omega_vac ~= (G/H_alpha) x (G/H_alpha)`,

and, after the physical diagonal `G` action is removed, the complete relative invariant is

`H_alpha \ G / H_alpha`.

This double coset replaces `(G x G)/G_diag`; without (T) the statement holds separately on each `G`-orbit of vacua.  Second, **A1** retains the projective virtual multiplier `[omega_alpha] in H^2(G,U(1))`.  It is the obstruction to replacing the projective padded-window action by an honest `G -> U(chi)` representation.  A direction-only continuum quotient contains neither the kernel `N_alpha` nor this microscopic SPT datum.

### 1.3 What is standard, and what corner A actually adds

The following content is standard superselection-sector bookkeeping:

- asymptotic left/right vacuum labels define soliton or kink sectors;
- normal states remain in the same folium, while different asymptotic labels give disjoint sectors;
- local operations cannot change data fixed at spatial infinity;
- orbit-stabilizer and double-coset classification organize symmetry-related sector labels.

This is DHR-style in logic, but not literally a DHR construction: the kink and half-string charges are localized on a half-line and interpolate between different vacua, rather than being transportable charges localized in bounded regions.  The `H^2(G,U(1))` projective class is likewise standard one-dimensional MPS/SPT classification, not a new cohomology principle.

The nonstandard proved content of corner A is the exact bridge between that bookkeeping and the microscopic tensor network: **WI** gives the oriented bond implementers for every finite interval; **A1** identifies endpoint states modulo scalars, computes the physical kernel `N_alpha`, and realizes the multiplier on padded window vectors; **A2** constructs the broken half-string limit as a weak-* kink state with an explicit transfer-gap rate and proves the sector jump.  These are new statements of this manuscript's construction.  The cited inputs do not establish a broader literature-priority claim.  The GNS realization of the endpoint charge algebra remains **SKETCH**, as stated in **A1**.

## 2. R2 — the soft/hard split

### 2.1 Continuum target

The accepted soft-pion construction separates the asymptotic charge into a vacuum-changing part and an external-leg part.  Its soft term

`Q^soft(q-hat) = -(i/4pi) lim_(omega->0)(a_pi^dagger-a_pi)`

creates or annihilates the soft Goldstone (`refs/arxiv-1709.05018/draft1004.tex:359-368`).  Its hard term is a number-preserving fermion bilinear whose kernel depends on the hard momentum and on `q-hat` (`refs/arxiv-1709.05018/draft1004.tex:370-409`).  Together they obey

`<out|[Q^soft(q-hat)+Q^hard(q-hat),S]|in> = 0`

(`refs/arxiv-1709.05018/draft1004.tex:375-385`).  The paper then derives the same soft theorem from the ordinary broken-current Ward identity by Fourier transformation, LSZ reduction, and the soft limit (`refs/arxiv-1709.05018/draft1004.tex:438-464`).  Thus “soft” and “hard” name two pole contributions of one conserved charge, not two independent symmetries.

### 2.2 Lattice identification

Take the modulated lattice charge

`Q[f;xi] = sum_x f(x) q_x(xi)`

with `f` a wave packet concentrated near `k=0`; a bare plane wave is only a distributional kernel, as required by D3.  On a scattering domain with a one-Goldstone projection `P_G` and vacuum projection `P_Omega`, the direct lattice counterpart is [physical argument]

`Q_lat^soft[f;xi] := P_G Q[f;xi] P_Omega + P_Omega Q[f;xi] P_G`,

`Q_lat^hard[f;xi] := Q_as[f;xi] - Q_lat^soft[f;xi]`.

Here `Q_as` denotes the charge transported to asymptotic particle states.  The first line is the part which creates or annihilates a `k -> 0` Goldstone on the vacuum.  The second is the number-preserving action on the nonsoft asymptotic legs; after LSZ it becomes the signed sum of the symmetry action on the incoming and outgoing hard legs [physical argument].  In 1+1 dimensions the smearing label has only the two directional components `L,R` found in section 1.

The proved lattice inputs reach different parts of this split:

| lattice input | content actually supplied |
|---|---|
| **G0** (**PROVED**) | D11(b) identifies `Q_k(xi)` acting on the vacuum with the Goldstone-tensor insertion.  On the ferromagnet, Proposition FM proves the exact normalization `Q_k(xi_x)|Omega> = (i/2)|k>` and the exact one-magnon dispersion.  This supplies a concrete soft vacuum-to-one-particle matrix element, not a general asymptotic soft-charge operator. |
| **G0(e)** (**PROVED**) | The finite-range continuity equation `[H,Q[f;xi]] = sum_x Delta f(x) j_(x|x+1)(xi)` and its packet form `[H,Q_k]=(e^{ik}-1)J_k`.  This is the local conserved-current input to a Ward reduction.  It does not imply regularity of `J_k`, an Adler zero, or factorization. |
| **WI** (**PROVED**) | A finite truncated symmetry acts exactly through two oriented bond residues.  It supplies the microscopic finite-region Ward operation and keeps its boundary terms explicit.  It is not an S-matrix Ward identity. |
| **A1** (**PROVED** in the stated padded-window/state registers) | The unbroken endpoint action, its physical kernel, and its projective multiplier.  The action on the GNS Hilbert space is still **SKETCH**, so A1 does not by itself define `Q_as` on scattering states. |
| **A2** (**PROVED** per fixed broken transformation) | The half-string changes the asymptotic vacuum sector in weak-* topology.  It identifies the sector on which a broken charge must act, but it supplies neither wave operators nor hard-leg LSZ. |
| **S-IDX-fin-r2** and **ML4-Ward** (**PROVED**, narrowly scoped) | Exact finite-sector Ward projections and a one-hard-magnon residue.  These are finite-register hard-action data, not the infinite-volume soft/hard decomposition. |
| **S-IDX-MATCH-HS-SEP** and **S-IDX-PROTO-SCALAR-HS-SEP** (**PROVED**, model/subclass scoped) | On the separated fully polarized spin-`S` protocol they give the on-shell match and an exact scalar LSZ-shaped factorization.  They explicitly do not prove the exhaustive component decomposition, microscopic class membership, or general proto-LSZ statement. |

The lattice analogue of the continuum charge Ward identity is therefore [physical argument]

`<out|[Q_lat^soft[epsilon;xi] + Q_lat^hard[epsilon;xi], S_lat]|in> = 0`,

or, more precisely when in/out charges live in different representations,

`<out|(Q_as^+ S_lat - S_lat Q_as^-)|in> = 0`,

with `Q_as^+/- = Q_lat^soft,+/- + Q_lat^hard,+/-` [physical argument].  The second form does not pretend that a broken half-string is a strongly convergent operator on one vacuum Hilbert space; **A1** and **A2** show why that pretense would be false.

### 2.3 The exact gap

The general split and Ward identity above are not proved.  Claim **S-IDX-spec-struct-r2** is **SKETCH** because it assumes the uninstantiated **(PROTO-LSZ)** hypothesis.  That hypothesis must exhaust the lattice datum into descendant/soft-leg, orthogonal-current, direct-contact, and window-boundary-gradient pieces, with the first having the required `C^1` soft profile and the other three controlled at `O(k^2)` or `o(k)` (`theory/soft-index-r2.md:597-640`).  No present row supplies that decomposition for the adjudicated fixed-time charge insertion (`theory/soft-index-r2.md:737-743`).

The associated regularity obligations also remain open: **ML3** is **CONJECTURE** and must exclude a physical `1/k_s` pole in the packet-smeared infinite-volume current form factor; **ML4** is **SKETCH**, and its first physical sequence `k_s=2pi/N` already refutes the needed finite-volume uniformity.  Consequently the lattice has a proved microscopic current identity and a proved soft vacuum residue, but only a conditional physics-level soft/hard `S`-matrix charge.

## 3. R4 — edge correspondence

### 3.1 Continuum assumptions and their named lattice counterparts

| accepted continuum step | corresponding named lattice hypothesis or claim, with current status |
|---|---|
| After extracting the Goldstone pole, the remainder `R^mu(p)` is regular in the simultaneous on-shell soft limit.  The continuum source explicitly says this does not follow automatically from ordinary pole arguments (`refs/arxiv-2201.01393/manuscript.tex:418-439`). | **ML3 — CONJECTURE:** packet-smeared infinite-volume current-form-factor regularity, including exclusion of physical `1/k_s` poles. **ML4 — SKETCH:** only a fixed-volume off-shell interpolation is controlled; the physical `k_s=2pi/N` sequence is not volume-uniform. **S-IDX-spec-struct-r2 — SKETCH:** assumes the uninstantiated **(PROTO-LSZ)** exhaustive regular decomposition. **G0 — PROVED** supplies the discrete continuity factor but not this regularity. |
| The memory field approaches finite, possibly different values at `u -> +/-infinity`, so its DC jump is the residue of its `1/omega` Fourier pole.  This is an explicit assumption in the standard gravity derivation (`refs/arxiv-1411.5745/memory_4.tex:688-695`). | **D27 (LR)** is the named lattice local-relaxation hypothesis. **LR1-GEN — PROVED** gives only common-subsequence Cesaro limits at every fixed window. D27(LR2) and D27(LR3) remain hypotheses. **LR-D16-NR — SKETCH** proves only `(NR) => LR3`, without proving `(NR)` or LR2. **M-INDEX-spec — PROVED conditional on D27(LR1-LR3)**; it does not prove LR. |
| Massive hard fields have the hyperbolic-slice falloff `psi ~ tau^(-3/2)` and the hard current behaves as `j ~ tau^(-3)`, allowing a finite hard charge on `H^3` (`refs/arxiv-1709.05018/draft1004.tex:559-576,649-658`). | **D18(AD3)** is the named local-decay clause and **AD3-ex — CONJECTURE** is its exact fixed-window formulation. **Mq-AD3 — PROVED** only for the projected D16 incoming `<=3`-wall component; it does not prove full-chain D18. **AC-EX** does not remove the gap: its charge-law clause assumes AD3-ex. |
| Integrations by parts discard boundary contributions.  The soft-pion memory derivation says explicitly that no surface term is assumed (`refs/arxiv-1709.05018/draft1004.tex:764-772`). | The spatial counterpart is not discarded silently. **G0/Lemma SBP — PROVED** retains the two exact window-edge terms; they vanish for `l^1 intersect BV` profiles in the norm limit or after delta normalization for plane waves.  The scattering-time/window counterpart remains **AD3-ex — CONJECTURE** and D27(LR2-LR3) assumed.  Thus the proved spatial summation-by-parts result does not prove the dynamical no-surface-term statement. |

### 3.2 Ward identity plus LSZ gives the continuum soft reduction

The exact lattice starting point is **G0(e)**.  Between energy-momentum states it reads

`(E_beta-E_alpha)<beta|Q_k(xi)|alpha> = (e^{ik}-1)<beta|J_k(xi)|alpha>`.

The lattice analogue of the continuum pole decomposition is [physical argument]

`<beta|J_lat^mu(p)|alpha>`

`= i <Omega|J_lat^mu(0)|G(k)> M_(beta+G,alpha)/(p^0-omega_G(k)) + R_lat^mu(p)`,

with the additional external-hard-leg poles/contact terms assigned to `Q_lat^hard` [physical argument].  Contracting this expression with the lattice divergence symbol and using the Goldstone dispersion cancels the one-Goldstone propagator pole.  If **ML3** regularity holds and **(PROTO-LSZ)** exhausts the remaining terms, taking `p^0=omega_G(k)` and then `k->0` leaves the vacuum-to-Goldstone residue multiplying the symmetry action on the hard external legs [physical argument].  This is the soft factorization statement and the combined Ward identity of section 2.

This is exactly the logic used in the continuum precedent.  There the ordinary broken-current Ward identity is Fourier transformed, the other fields are LSZ reduced, and the soft limit separates the soft-pion term from the hard external-leg term (`refs/arxiv-1709.05018/draft1004.tex:450-458`); the resulting asymptotic Ward identities are stated to be contained in the ordinary broken-symmetry identity (`refs/arxiv-1709.05018/draft1004.tex:460-464`).

To see the dimensional reduction explicitly, restore lattice spacing `a` and put the physical momentum at `p`, so the lattice momentum is `k=ap`.  Then

`(e^{iap}-1)/a = ip + O(a p^2)`.

After the current and charge densities receive their standard powers of `a`, the exact lattice continuity equation tends to `partial_mu J^mu=0`, lattice sums tend to spatial integrals, and the packet LSZ pole decomposition tends to the continuum one [physical argument].  The compact Brillouin zone causes no local obstruction at `p=0`; the missing ingredient is uniform control of the limit, precisely the content absent from **ML3/ML4**.  Under those hypotheses the lattice Ward edge specializes to the `refs/arxiv-1709.05018` Ward-plus-LSZ derivation, rather than merely sharing its diagram.

### 3.3 Soft residue gives memory

Let `X(t)` be the lattice collective coordinate whose ordered shift is the memory `delta x`.  If it has finite asymptotic values `X_+` and `X_-`, then with the Fourier convention `X_tilde(omega)=int dt e^{i omega t}X(t)`,

`X_+ - X_- = lim_(omega->0)(-i omega) X_tilde(omega)`

up to the fixed normalization used to define the observed field [physical argument].  A step in time and a `1/omega` pole are therefore the same distribution.  The continuum gravity derivation makes exactly this move and then identifies `omega h^TT` with the soft-amplitude ratio (`refs/arxiv-1411.5745/memory_4.tex:688-700`).  The canonical triangle summarizes the same relation as “the Fourier transform of a pole in frequency space is a step function in time” (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:333-336`).

The lattice already has the finite-time DC identity **M-flux — PROVED**:

`delta x = (1/(2s))[j_tilde_(a-1|a)(0)-j_tilde_(b|b+1)(0)]`.

Under D27(LR), **M-INDEX-spec — PROVED conditional** promotes the finite-window charge ledger to an ordered memory value,

`delta x = -(1/(2s)) sum_nu nu p_nu`.

Combining the soft theorem's zero-frequency current residue with **M-flux**, and then taking the D27-ordered time and window limits, gives the same “Fourier residue equals permanent shift” edge [physical argument].  In a continuum scaling limit the discrete collective coordinate and cut currents rescale to the continuum order parameter and flux, while the preceding `e^{iap}-1` factor becomes `ip`; hence the lattice edge becomes the continuum Fourier-residue derivation [physical argument].

D27 supplies Cesaro relaxation and first-moment tightness, not the pointwise limits `X(t)->X_+/-` assumed in `refs/arxiv-1411.5745`.  A direct pointwise Fourier-residue theorem therefore needs either a stronger lattice relaxation hypothesis or a proved Abelian/Tauberian passage from the D27 Cesaro limits [physical argument].  Likewise, identifying the current residue with a soft amplitude still depends on the R2 proto-LSZ step.  The soft-to-memory reduction is structurally exact under these named assumptions, but it is not unconditional.

### 3.4 What “accepted” hides

The difference in status is not a difference in the logical step.  The continuum Adler derivation explicitly adds soft on-shell regularity of `R^mu`; the gravity memory derivation explicitly assumes finite early/late limits; the soft-pion construction uses stationary-phase hyperbolic falloffs and explicitly assumes away a surface term.  The lattice rows give these same requirements names and separate their proved special cases from their open general forms.  Thus the conditional lattice edges rest on counterparts of assumptions already used by the accepted continuum edges.  This observation does not upgrade **ML3**, **ML4**, **AD3-ex**, D27(LR2-LR3), or **(PROTO-LSZ)**.

## 4. Verdicts

### R2: REDUCES WITH CAVEATS

The dimensional specialization reduces cleanly: `S^0` has two points, `Maps(S^0,G)=G_L x G_R`, and removing the common global transformation leaves one relative datum.  The absence of an infinite angular tower is mandatory in 1+1 dimensions and is not a lattice failure.

The caveats are:

1. The physical unbroken lattice orbit is `A_eff=G/N_alpha`, not automatically `(G x G)/G_diag`; equality holds when the virtual action is faithful.  For nonabelian `G`, the diagonal quotient is a homogeneous space rather than a quotient group.
2. In the broken case the correct object is the vacuum-pair space, with diagonal invariant `H_alpha\G/H_alpha` under (T), or the corresponding statement per vacuum orbit.  It is not the naive asymptotic-symmetry coset.
3. The projective `[omega_alpha]` datum is additional microscopic SPT information.  Its existence does not turn it into a continuum Lie-algebra central charge.
4. The endpoint algebra is proved on padded finite-window vectors and on states in the stated sense; its GNS realization remains **SKETCH**.
5. The soft vacuum residue and continuity equation are proved, but the general soft/hard asymptotic charge and `[Q_lat^soft+Q_lat^hard,S_lat]=0` remain [physical argument] pending **(PROTO-LSZ)**, **ML3**, **ML4**, and a suitable scattering construction.  Narrow finite/model-specific Ward and scalar LSZ-shaped results do not close that general gap.

The paper can state that corner A is the correct 1+1-dimensional specialization and is microscopically finer.  It cannot state that the full lattice soft/hard asymptotic Ward construction has been proved.

### R4: REDUCES WITH CAVEATS

The edge formulas reduce to the accepted continuum formulas: `(e^{iap}-1)/a -> ip` turns the lattice Ward identity into current conservation, Ward plus a regular exhaustive LSZ decomposition gives soft factorization, and the `omega=0` Fourier residue of a step gives memory.  These reductions are conditional physics arguments, not completed lattice edge theorems.

The caveats are:

1. Current-remainder regularity is **ML3 — CONJECTURE**; **ML4 — SKETCH** does not provide the required packet-smeared, volume-uniform on-shell limit.
2. The exhaustive soft/hard/contact/boundary decomposition **(PROTO-LSZ)** is uninstantiated, so **S-IDX-spec-struct-r2** remains **SKETCH**.
3. Full local decay is **AD3-ex — CONJECTURE**.  **Mq-AD3** proves only the projected D16 component.
4. D27(LR2-LR3) is assumed.  **LR1-GEN** proves only the common-subsequence Cesaro part, and **LR-D16-NR** does not prove its own antecedent or LR2.
5. D27's Cesaro limits are weaker than the pointwise finite early/late limits used in the standard Fourier-residue derivation; the required Abelian/Tauberian bridge is not proved.
6. Spatial boundary terms are controlled by **G0/Lemma SBP**, but dynamical scattering boundary terms still require AD3-ex and LR-type relaxation.

The paper can present R4 as a named conditional reduction and can observe that the continuum derivations use the corresponding assumptions.  It cannot present the lattice triangle edges as proved merely because those continuum edges are conventionally accepted.
