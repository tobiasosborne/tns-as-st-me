<!-- ROLE: L6b proposer shard for bd tns-jpd.  D29/D30 text below is
     proposals-only; no shared definition or claims row is edited here. -->

# MATCH-HS — fixed-time charge packets match the two-body multiplier

**Positive result.**  `(MATCH-S)` is proved in this proposer shard for every
fully polarised bilinear spin-`S` ferromagnet `H_S`, `2S in N`, on the
regular primitive two-magnon channel, for the displayed separated-preparation
subclass `(D29-HS-SEP)` of the quarantined D29 proposal.  Along every actual
ordered row-measure limit subsequence the match is exact, hence is stronger than the required
`o(epsilon)` statement.  `(PROTO-LSZ)` is **not proved**.  L5 status remains
**SKETCH**.  An internal self-critic returned four MAJOR repair demands and
no FATAL; the single repair wave required by PRD.md is incorporated below.

## 1. Setup by D-number

### ⟨1⟩1. Frozen registers and the model

**ASSUME.**  `S in {1/2,1,3/2,...}`, `J>0`, and

`H_S=-J sum_x(S_x.S_{x+1}-S^2)`

over the fully polarised all-up vacuum.  At `S=1/2` this is D6.  Use D7's
ordered-coordinate ratio and physical out/in labelling, D8's fixed hard
regular channel, D24(b)'s packet/amputation convention, D29's exact merge
proposal in `theory/soft-index-r2.md` §7.1, and D31's fixed-packet
separation conventions.  D29 and D30 remain proposals: this shard neither
installs nor silently strengthens them.

**PROVE.**  The following register will be used throughout.

**⟨2⟩1.**  Fix a one-sided soft profile
`f_epsilon(k)=epsilon^(-1/2)f(k/epsilon)` and a normalized hard profile
`g_sigma(h)=sigma^(-1/2)g((h-h_0)/sigma)` with

`supp f_epsilon x supp g_sigma subset K_s(epsilon) x I`,

where `I compactly contained in (0,pi)` lies in D8's D7 channel, all
points are in the regular domain (T.1) of `S2-2body-S`, and

`dist(v_S(K_s(epsilon)),v_S(I)) >= d_epsilon > 0`.           (PMLM.1)

The packet widths may shrink only in D29 order: `epsilon` is held fixed
while `sigma downarrow 0`; `epsilon downarrow 0` is last.

*Justification.*  D3(a), D7--D8, proposed D29(2),(6), and D31(4).  The
constant `d_epsilon` need not be uniform as `epsilon downarrow0`.

**⟨2⟩2.**  Let `H_0` be multiplication by
`omega_S(k)+omega_S(h)` on the labelled channel

`H_ch=L^2(K_s(epsilon) x I,dk/(2pi) dh/(2pi))`,

and write `U_0(t)=exp(-itH_0)`.  For a factorized labelled packet `F=f otimes
g`, define the two-lowering identification

`I_S F=(2S)^(-1) Q[f]Q[g]|Omega>` .                         (PMLM.2)

Here `f_x=int exp(ikx)f(k)dk/(2pi)` and
`Q[f]=sum_x f_xS_x^-`; the same convention is used for `g`.  Ring packets
are the Plancherel-normalized samples of these integrals.  Any common D29
discrete-Fourier scalar cancels from its numerator and denominator.

If `psi_g=(2S)^(-1/2)Q[g]|Omega>` is the normalized hard magnon, the D29
fixed-time state is

`Q[f]psi_g=sqrt(2S) I_S(f otimes g)`.                       (PMLM.3)

The scalar `sqrt(2S)` occurs in both D29 numerator and denominator and
cancels.  It is never read as `a_leg` and supplies no value.

*Justification.*  D24(b)(i) gives `Q[g]|Omega>=sqrt(2S)|g>` in the
fully polarised register.  Equation (PMLM.3) is then an exact finite-sector
identity.  Named checker gate **PMLM-C1** verifies the normalized occupation
coefficients, including the double-occupancy coefficient
`sqrt((2S-1)/S) f(x)g(x)` for `S>=1`.

**⟨2⟩2a.**  Define the canonical bulk identification `J_S` on factorized
packets by the same normalized off-diagonal coefficients as `I_S` and by
zero double-occupancy coefficient.  Thus, in proposed D29(3)'s labelled
coordinate map,

`C_SJ_S(f otimes g)(x,y)`
` =(f_xg_y+g_xf_y)/sqrt(2)` for `x!=y`, and is zero for `x=y`.
                                                                    (PMLM.3a)

The difference `I_S-J_S` is supported only on the double/collision row;
at `S=1/2` it is zero.

*Justification.*  The normalized occupation coefficients in (PMLM.2).
`J_S` is the explicit two-Hilbert reference used below; it is not a second
physical creator or a D29 redefinition.

Define separately the ideal labelled-grid symmetrizer `Y_S` by

`Y_S(f otimes g)(x,y)=(f_xg_y+g_xf_y)/sqrt(2)` for all `x,y`, (PMLM.3b)

including the diagonal.  Then `C_SJ_S-Y_S` is also supported only on the
collision row.  `Y_S` is used only as an algebraic readout comparator and
is not a vector in the physical spin-`S` Hilbert space.

**⟨2⟩3.**  Put `F_{epsilon,sigma}=f_epsilon otimes g_sigma`.  Let
`T_R` be relative spatial translation of the hard packet to the incoming
side by an integer `R>=1` sites (a unit-modulus momentum phase), and put

`F_{epsilon,sigma,R}=T_RF_{epsilon,sigma}`.                  (PMLM.4)

The D29 window/separation datum `W` is specialized to this `R`-geometry.
It changes no momentum support, width, or row measure.

*Justification.*  Relative translation is precisely an initial-position
choice of proposed D29(4),(6).  Under backward free evolution the faster
hard packet moves farther into the incoming side, so (PMLM.1) makes the
past separation at least `R+d_epsilon|t|`.

### ⟨1⟩2. The displayed separated-preparation class `(D29-HS-SEP)`

**ASSUME.**  The D29 indices are specialized as follows.  At fixed
`epsilon>0`, take `sigma_j downarrow0`, `R_j to infinity`, and settling
times `T_j` with `L_j:=d_epsilon T_j-R_j to infinity`.  Put

`B_{M,epsilon}:=max_(a+b<=M)||partial_k^a partial_h^b S_phys||_infinity`

on `K_s(epsilon) x I`, and
`K_{M,epsilon}:=C_{M,S,J}(1+B_{M,epsilon})/d_epsilon`; both are
finite at fixed `epsilon` by (T.1).  For one integer `M>=8`, require

`K_{M,epsilon}s_M(f_epsilon)s_M(g_sigma_j)`
` * [(1+R_j)^(3-M)+(1+L_j)^(3-M)] to 0`,                     (SEP)

where `s_M` is the fixed-packet Schwartz seminorm used by `AC-EX-2M`,
evaluated on the untranslated envelopes.  The unit-modulus `R_j` phase is
kept in the stationary phase and is not differentiated as part of the
envelope; this is the translation-covariant form of the packet estimate.
The D29 hard-column window is the labelled rectangle
`K_s(epsilon) x supp g_sigma_j`; zero-mass rows carry zero measure as in
proposed D30(a).

After fixing `(sigma_j,R_j,T_j)`, choose a finite ring `N_j` so large that

`N_j epsilon(c_2-c_1)>2pi`,
`T_j<=c_rec N_j/v_max`, and `eta_j<=1/j`,                    (PMLM.4a)

where `eta_j` is the sum of the norm errors between the periodized finite-
ring interacting/free kernel vectors at `T_j` and their infinite-chain
counterparts, after the selected D29 Fourier projection.  This is one D29
admissible finite-ring sequence; no infinite-chain datum is substituted for
the protocol.

**PROVE.**  `(SEP)` is a nonempty, directly verified model class, not a
renaming of `(MATCH-S)`.

**⟨2⟩1.**  Compactly supported `C^infty` packets satisfy

`s_M(g_sigma)=O(sigma^(-M-1/2))`.                            (PMLM.5)

Choosing, for example, `R_j=ceil(sigma_j^(-2))` and
`T_j=2R_j/d_epsilon` makes `L_j=R_j` and the left side of `(SEP)`
`O_epsilon(sigma_j^(M-13/2))`, hence sends it to zero for `M>=8`.

*Justification.*  Differentiate the definition of `g_sigma`; insert
`R_j=ceil(sigma_j^(-2))` into `(SEP)`.  The soft seminorm is a finite constant
at this outer-limit stage.  Named checker gate **PMLM-C2** independently
corroborates the decay of the free collision trace and has a no-separation
red mutation.

**⟨2⟩2.**  Rings satisfying (PMLM.4a) exist.  For each fixed packet tuple
and finite `T_j`, Plancherel sampling/periodization converges in the
two-particle norm.  Finite-range dynamics converges strongly on that vector,
and proposed D29(3)'s coordinate Fourier map plus its selected-row
projection are contractions.  Hence their interacting and D29-free kernel
errors tend to zero as `N to infinity`; choose `N_j` diagonally to make their
sum at most `1/j`, and enlarge it further to meet the sampling and
recollision inequalities.

*Justification.*  Proposed D29(2),(3),(6), strong thermodynamic convergence
at fixed time, and a diagonal choice after `(sigma_j,R_j,T_j)` is fixed.

**⟨2⟩3. QED.**

## 2. The ladder

### ⟨1⟩3. Two-body wave operators for `H_S`

**ASSUME.**  The regular compact packet rectangle of ⟨1⟩1 and the
two-magnon sector of `H_S`.

**PROVE.**  There are incoming/outgoing isometries `W_-^S,W_+^S` on this
packet channel, with equal range in the direct integral of the fibrewise
relative-coordinate absolutely continuous subspaces (the two-unbound-magnon
scattering summand), such that

`(W_+^S)^* W_-^S = M_{S_phys}`,                              (PMLM.6)

where `M_{S_phys}` is multiplication by D7's physical ratio from the PROVED
row `S2-2body-S`.

**⟨2⟩1.**  Fourier transform in the centre coordinate decomposes the
two-magnon Hamiltonian as a direct integral over total momentum `K`.  For
relative coordinate `r>=2` the fibre equation is the constant-coefficient
Jacobi recurrence obtained from `spin-s-twomagnon.md` (3).  The only changed
rows are `r=1` and, for `S>=1`, the single normalized double-occupancy row
`r=0`, given by equations (4)--(5).

*Justification.*  Translation invariance and the exhaustive separated,
adjacent, and double-occupancy equations of `S2-2body-S`.  The `r=0` degree
is a boundary degree, not a second propagating channel.

**⟨2⟩2.**  On the selected labelled chart put
`K=k_1+k_2`, `q=(k_2-k_1)/2`; its Jacobian is one.  The canonical free fibre
space is `L^2(dq/(2pi))` with multiplication by

`E_0(K,q)=omega_S(K/2-q)+omega_S(K/2+q)`.

Let `F_(0,K)` be its bulk generalized Fourier transform, normalized so the
incoming plane wave has coefficient one and the common flux/Plancherel
density is included in the transform.  Its two-Hilbert coordinate
identification is exactly the fibre of `J_S` from (PMLM.3a).

*Justification.*  The change `(k_1,k_2)<->(K,q)` preserves
`dk_1 dk_2`; disjoint labelled supports select one chart.  The constant
bulk recurrence in ⟨2⟩1 has the standard scalar Jacobi spectral transform.
The density is common to the incoming and outgoing normalizations, so it
cannot alter their unit-modulus ratio.

**⟨2⟩3.**  Relative to this explicit free fibre, the physical fibre differs
only in the finitely many `r=0,1` matrix entries.  The boundary difference
`H_(S,K)J_(S,K)-J_(S,K)E_0(K)` is finite rank.  The scalar Jacobi spectral
theorem therefore gives isometric generalized transforms `F_(-,K)` and
`F_(+,K)` with the same range, namely the selected part of the fibrewise
relative-ac subspace; the finitely many square-summable boundary solutions
are orthogonal bound fibres.

*Justification.*  Finite-rank boundary perturbations are trace class after
the two-Hilbert identification, so the trace-class wave-operator theorem
gives existence and completeness in the relative-ac fibre.  Equivalently,
the resolvent identity is finite dimensional at the boundary and the scalar
Jacobi eigenfunction expansion supplies the same transforms.  This is a
direct two-body spectral theorem, not assumed Bethe completeness.

**⟨2⟩4.**  A regular physical fibre eigenfunction has the two bulk branches

`A_12 exp(i(k_1 x+k_2 y)) + A_21 exp(i(k_2 x+k_1 y))`.

The boundary equations give

`A_12/A_21=(S a b-z_1 mu)/(z_2 mu-S a b)`.                  (PMLM.7)

*Justification.*  `S2-2body-S` (T.2), proved by direct substitution into
all configuration classes.  Regularity (T.1) excludes boundary poles on the
packet support.

**⟨2⟩5.**  Stationary phase assigns the incoming and outgoing branch
exactly as D7 does.  Hence their transition multiplier is `S_12` when
`v(k_2)>v(k_1)` and `S_21=S_12^(-1)` in the reversed channel.

*Justification.*  D7 and the separated velocity supports (PMLM.1).  This is
the same branch argument as `AC-EX-2M` ⟨1⟩7.⟨2⟩3, now with the
spin-`S` boundary equations (4)--(5).

**⟨2⟩6.**  The recurrence coefficients, boundary resolvent, common spectral
density, and normalized eigenfunctions are continuous away from (T.1)'s
singular set; hence the fibre transforms are measurable in `K`.  Put

`W_±^S=int^oplus F_(±,K)^* F_(0,K) dK/(2pi)`.

They are isometries on `H_ch` with equal selected scattering range, and
⟨2⟩4--⟨2⟩5 give `(W_+^S)^*W_-^S=M_(S_phys)` in the displayed
`dk/(2pi)dh/(2pi)` normalization.  Their time-dependent realization with
the canonical identification is

`W_±^SF=s-lim_(t to ±infinity) exp(iH_St)J_SU_0(t)F`.         (PMLM.6a)

**⟨2⟩7.**  The same limit holds with the D29 charge identification `I_S`:

`||(I_S-J_S)U_0(t)F|| to 0` as `t to ±infinity`              (PMLM.6b)

on every separated fixed packet.  Therefore (PMLM.6a) remains true after
`J_S` is replaced by `I_S`.

*Justification.*  `I_S-J_S` is the collision row by (PMLM.3a).  The
outside-cone/nonstationary-phase estimate of (PMLM.10), with no time
integration needed, sends its norm to zero.  Two-Hilbert wave operators are
unchanged by an identification difference that vanishes on freely evolved
channel packets.

**⟨2⟩8.**  Bound eigenvalues are point spectrum in each relative fibre;
their direct integrals form separate propagating bound-band summands and do
not occur in either range.  Thus the equality asserted here is only equality
of the two wave-operator ranges inside the selected relative-ac spectral
window, not completeness of the full two-magnon absolutely continuous
space when bound bands disperse.

*Justification.*  The direct-integral splitting in ⟨2⟩3 and the compact
regular packet restriction.

**⟨2⟩9. QED.**

### ⟨1⟩4. The fixed-time charge state approaches the incoming channel

**ASSUME.**  Put `F=F_{epsilon,sigma}` and `F_R=T_RF`.  Let
`M_S=M_{S_phys}`.

**PROVE.**  For every `M>=5` there is a finite model constant
`C_{M,S,J}` such that

`||I_S F_R-W_-^S F_R||`
` <= [C_{M,S,J}/d_epsilon]s_M(f_epsilon)s_M(g_sigma)`
`      *(1+R)^(3-M)`,                                       (PMLM.8)

and, for `d_epsilon T>R`,

`||exp(-iH_ST)W_+^S M_SF_R-I_SU_0(T)M_SF_R||`
` <= [C_{M,S,J}/d_epsilon]s_M(M_SF)`
`    *(1+d_epsilon T-R)^(3-M)`.                              (PMLM.9)

**⟨2⟩1.**  The identification defect

`(H_S I_S-I_SH_0)U_0(t)F_R`

is supported only on the adjacent/double collision rows `r<=1`.

*Justification.*  Away from contact, `H_S` is the sum of the two one-magnon
Hamiltonians by `S2-2body-S` equation (3); equations (4)--(5) list every
remaining row.  This is the spin-`S` analogue of the two-creator Cook defect
in `AC-EX-2M` ⟨1⟩5.

**⟨2⟩2.**  On the backward evolution of `F_R`, the two velocity cones are
separated by at least `(R+d_epsilon|t|)/2` outside rapidly
decaying tails.  Summing the collision rows gives

`||(H_S I_S-I_SH_0)U_0(t)F_R||`
` <= C_{M,S,J}s_M(f_epsilon)s_M(g_sigma)`
`       *(1+R+d_epsilon|t|)^(2-M)`.                           (PMLM.10)

The analogous future estimate holds after the collision, with separation
`d_epsilon t-R`, and with `s_M(F)` replaced by `s_M(M_SF)`.  Leibniz's rule
on the regular rectangle gives

`s_M(M_SF)<=C_M(1+B_(M,epsilon))`
`             s_M(f_epsilon)s_M(g_sigma)`.                  (PMLM.10a)

Here too the relative-translation phase is extracted before the centered
envelope seminorm is taken.

*Justification.*  Repeated integration by parts in each compact momentum
packet gives the usual outside-cone estimate.  On the product of the main
cones no collision row occurs; on its complement one packet supplies rapid
decay and the other has `l^1` norm `O(1+|t|)`.  This is exactly the
fixed-packet `ACE-SP` estimate, and it is deliberately not uniform in
`epsilon` or `sigma`.

**⟨2⟩3.**  Integrating (PMLM.10) over `(-infinity,0]` gives
(PMLM.8).  Integrating its outgoing version over `[T,infinity)` gives
(PMLM.9).

*Justification.*  Cook's fundamental-theorem-of-calculus estimate and
`M>=5`.  Integrating `(1+R+d_epsilon|t|)^(2-M)` contributes the explicit
factor `[d_epsilon(M-3)]^(-1)`; `M-3` is absorbed into `C_{M,S,J}`.

**⟨2⟩4.**  Equality of the wave-operator ranges and (PMLM.6) give

`W_-^S F_R=W_+^S M_SF_R`.                                    (PMLM.11)

Consequently

`||exp(-iH_ST)I_SF_R-I_SU_0(T)M_SF_R||`
` <= K_{M,epsilon}s_M(f_epsilon)s_M(g_sigma)`
`    *[(1+R)^(3-M)+(1+d_epsilon T-R)^(3-M)]`.                (PMLM.12)

*Justification.*  Apply the unitary `exp(-iH_ST)` to (PMLM.8), use
(PMLM.11), and add (PMLM.9).  This displayed estimate is the bridge: it
starts with the fixed-time D29 charge state and ends with the constructed
outgoing channel.  No equality between those two states was assumed.

**⟨2⟩5. QED.**

### ⟨1⟩5. Passage through the D29 readout

**ASSUME.**  Let `C_S` be proposed D29(3)'s isometric coordinate-kernel map
and let `P_{epsilon,sigma}` select the labelled soft-row/hard-column
rectangle, with the finite ring embedded in the continuum channel by its
Plancherel step-function sampling.  After removing the common factor in
(PMLM.3), put

`x_j=P_j C_S Phi^(free)_(N_j,j)`,
`y_j=P_j C_S Phi^(int)_(N_j,j)`,

and define the ideal labelled vectors

`x_j^0=P_j Y_SU_0(T_j)F_(epsilon,sigma_j,R_j)`,
`y_j^0=P_j Y_SU_0(T_j)M_SF_(epsilon,sigma_j,R_j)`.            (PMLM.13a)

Write `e_j^in=x_j-x_j^0`, `e_j^out=y_j-y_j^0`, and put

`r_j=<x_j,y_j>/||x_j||^2`,
`A_j=r_j-1`.                                                  (PMLM.13)

**PROVE.**  Along `(D29-HS-SEP)`,

`r_j-int S_phys(k,h)dmu_{j,epsilon}(k,h) to 0`,               (PMLM.14)

where `mu_{j,epsilon}` is the same normalized D29 free-row measure.

**⟨2⟩1.**  For normalized one-particle coordinate packets `u,v`, both
`C_S(I_S-J_S)(u otimes v)` and `(C_SJ_S-Y_S)(u otimes v)` are supported on
the diagonal.  The first has physical double coefficient
`sqrt((2S-1)/S)u(x)v(x)` for `S>=1` and is zero at `S=1/2`; the second is
the missing ideal labelled diagonal.  Hence the D29 free-reference error is
the freely phase-propagated sum of those initial collision rows plus the
finite-ring sampling/seam error.  The outgoing error is the sum of
(PMLM.12), both outgoing collision rows taking `C_SI_S` to `Y_S`, and that
finite-ring error.

*Justification.*  The spin ladder matrix elements in D24(b)(i) and the exact
identity (PMLM.2).  **PMLM-C1** checks this coefficient by a route independent
of the displayed formula and kills a wrong-double-row mutation.

**⟨2⟩2.**  Repeated integration by parts as in (PMLM.10), Leibniz's bound
(PMLM.10a), and (PMLM.4a) give

`||e_j^in|| <= C s_M(f_epsilon)s_M(g_sigma_j)(1+R_j)^(2-M)`
`                 +eta_j`,

`||e_j^out|| <= K_(M,epsilon)s_M(f_epsilon)s_M(g_sigma_j)`
` *[(1+R_j)^(3-M)+(1+L_j)^(3-M)+(1+L_j)^(2-M)] +eta_j`.
                                                                    (PMLM.15)

Both right sides tend to zero by `(SEP)` and `eta_j<=1/j`.

*Justification.*  The first line separately tracks the initial D29-free
diagonal defect.  The second tracks the wave-operator bridge and the
outgoing `I_S-J_S` defect.  No error is identified with another.

**⟨2⟩3.**  Because the two momentum supports are disjoint, (PMLM.3a) has two
orthogonal labelled rectangles of equal mass.  With normalized `F`, the
selected one obeys exactly

`D_j^0:=||x_j^0||^2=1/2`, `||y_j^0||^2=1/2`.                 (PMLM.15b)

For all sufficiently large `j`, `||e_j^in||` is small enough that
`D_j:=||x_j||^2>=1/4`.

*Justification.*  Plancherel in the explicit `dk/(2pi)dh/(2pi)` convention,
the `1/sqrt(2)` in (PMLM.3a), `|S_phys|=1`, and the reverse triangle
inequality.

**⟨2⟩4.**  Let `nu_j` be the ideal probability density
`|x_j^0|^2/D_j^0` and let `mu_{j,epsilon}` be D29's actual density
`|x_j|^2/D_j`.  Then

`||mu_{j,epsilon}-nu_j||_TV<=C||e_j^in||=o(1)`,              (PMLM.15c)

and the normalized pairings obey

`|r_j-<x_j^0,y_j^0>/D_j^0|`
` <= C(||e_j^in||+||e_j^out||)=o(1)`.                        (PMLM.16)

*Justification.*  The total-variation estimate follows from
`|| |x|^2-|y|^2 ||_1 <= (||x||+||y||)||x-y||` and denominator
lower bounds (PMLM.15b).  Expanding
`<x^0+e^in,y^0+e^out>` and the denominator, then applying Cauchy--Schwarz,
gives (PMLM.16).  **PMLM-C3** checks its one-error core and the conjugation
orientation; the analytic estimate here includes both errors.

**⟨2⟩5.**  In the ideal labelled Fourier rectangle,
`U_0(T_j)` contributes the same phase to the free and outgoing vectors.
The translation phase in `F_R` also occurs on both sides.
They cancel in (PMLM.13), leaving

`<x_j^0,y_j^0>/D_j^0=int S_phys(k,h)dnu_j(k,h)`.              (PMLM.17)

By (PMLM.15c), replacing `nu_j` by the same D29 row measure
`mu_{j,epsilon}` changes this expression by at most
`||S_phys||_infinity o(1)=o(1)`.

*Justification.*  `H_0` and `M_S` are commuting multiplication operators.
D7's label is fixed before the pairing; no inverse multiplier is inserted.
**PMLM-C4** verifies this cancellation on nontrivial complex packet data and
kills a physical-channel inversion mutation.

**⟨2⟩6.**  More quantitatively, (PMLM.15)--(PMLM.17) give

`|r_j-int S_phys dmu_(j,epsilon)|`
` <= C{K_(M,epsilon)s_M(f_epsilon)s_M(g_sigma_j)`
` *[(1+R_j)^(3-M)+(1+L_j)^(3-M)]+eta_j} to 0`.               (PMLM.17a)

This is (PMLM.14) for the actual finite-ring D29 sequence.

*Justification.*  `(SEP)`, (PMLM.4a), and the explicit two-error normalized
readout algebra above.

**⟨2⟩7. QED.**

### ⟨1⟩6. Theorem `(MATCH-HS-SEP)`

**ASSUME.**  `(D29-HS-SEP)` and any actual D29 row-measure limit point
`mu_{*,epsilon}` along the same indices.

**PROVE.**  Along that same row-measure limit subsequence the scalar D29
datum converges and satisfies

`boxed{ A_*(epsilon)
       =int [S_phys(k,h)-1]dmu_{*,epsilon}(k,h) }`.           (PMLM.18)

In particular the hypothesis `(MATCH-S)` of `S-IDX-spec-r2` holds, with
zero remainder rather than merely `o(epsilon)`.

**⟨2⟩1.**  The probability measures are tight on the compact
hard window and the scale-tied soft support, so a subsequence converges
weakly.  Continuity of `S_phys` on the regular compact rectangle passes the
right side of (PMLM.14) to that limit.

*Justification.*  Proposed D29(2),(4), compactness of the support, and
regularity (T.1).  For the displayed `g_sigma`, the hard marginal converges to
`delta_{h_0}`.

**⟨2⟩2.**  Equation (PMLM.14) then proves (PMLM.18) and at the same
time supplies the scalar limit on the left.

*Justification.*  ⟨1⟩5.  This is a proof of the protocol/on-shell
bridge, not an identification clause placed into D29.

**⟨2⟩3.**  Since the difference in `(MATCH-S)` is identically zero
for every fixed `epsilon` after the ordered outer limit, it is
`o(epsilon)` when `epsilon downarrow0` is finally taken.  No Cook constant
was required to be uniform in `epsilon`.

*Justification.*  D29 order and (PMLM.18).  This is precisely why the
fixed-packet divergence recorded by `AC-EX-2M` does not obstruct this
subclass.

**⟨2⟩4. QED.**

## 3. Interfaces to the proved suppliers

### ⟨1⟩7. `S2-2body-S`

**ASSUME.**  The PROVED row `S2-2body-S` with its exact regular-domain
scope.

**PROVE.**  Its use in this shard is confined to two logically separate
interfaces.

**⟨2⟩1. Kinematics.**  Equations (3)--(5) and (T.2) identify the one-channel
Jacobi boundary scattering matrix in (PMLM.7).  No soft coefficient is used
in ⟨1⟩3--⟨1⟩6.

*Justification.*  The proof of (T.2) is the direct, integrability-free
contact calculation.

**⟨2⟩2. Value.**  Equations (T.3)--(T.4) enter only at
⟨1⟩10.⟨2⟩1, after (MATCH-HS-SEP) has already identified the D29 readout with
the multiplier.

*Justification.*  This is the hard fence that the number `1/S` comes only
from on-shell matching.

**⟨2⟩3. QED.**

### ⟨1⟩8. `AC-EX-2M` and `S-IDX-HR-value-r2`

**ASSUME.**  The PROVED fixed-packet row `AC-EX-2M` and the separately
labelled on-shell row `S-IDX-HR-value-r2`.

**PROVE.**  This shard composes with neither by fiat.

**⟨2⟩1.**  At `S=1/2`, the maps of ⟨1⟩3 are the D6 two-magnon maps of
`AC-EX-2M`, and (PMLM.6) is its exact D7 match.  For `S>=1`, ⟨1⟩3 supplies
the required model-specific half-line Jacobi construction directly; no
unproved spin-`S` extension of `AC-EX-2M` is cited.

*Justification.*  `AC-EX-2M` ⟨1⟩2--⟨1⟩7′ and the D6-only exact-match clause
in its live claims row.

**⟨2⟩2.**  The fixed-packet Cook constants in both constructions carry
packet seminorms and need not be bounded as `epsilon downarrow0`.  This shard
first applies them at fixed `epsilon`, then uses `(SEP)` in the
`(R,sigma,T)` outer limit, and only then takes `epsilon downarrow0`.

*Justification.*  D29 order, `AC-EX-2M` ⟨1⟩2.⟨2⟩1, and (PMLM.12).

**⟨2⟩3.**  At finite separation the D29 vector is still the fixed-time
charge-created vector, not an HR creator family.  In the spin-`1/2` plane-
wave register its exact difference from the incoming eigenwave remains
`(1-S_12)|P_12>=-2ik_s|P_12>+O(k_s^2)`.  Wave-packet velocity separation,
the incoming Cook tail (PMLM.8), and the outgoing tail (PMLM.9) prove that
the normalized D29 readout nevertheless approaches the HR multiplier.

*Justification.*  `soft-current-recon.md` (R8),(R17)--(R19) and
(PMLM.12)--(PMLM.18).  The nonzero branch mismatch is retained, not erased;
its globally written plane-wave branch lies outside the selected incoming
cone after wave-packet localization.

**⟨2⟩4.**  Thus `S-IDX-HR-value-r2` remains a distinct on-shell instance.
The new content is exactly the norm-controlled arrow

`fixed-time D29 state --(PMLM.12)+(readout bound)--> on-shell multiplier`.

*Justification.*  ⟨1⟩4--⟨1⟩6.  Without `(SEP)` this arrow is not claimed.

**⟨2⟩5. QED.**

### ⟨1⟩9. D24 and the Ward register

**ASSUME.**  D24(b),(d), `S-IDX-fin-r2`, and the AMP obstruction.

**PROVE.**  No normalization or Ward statement is over-read.

**⟨2⟩1.**  The factor `sqrt(2S)` in (PMLM.3) is a common finite-state
normalization that cancels in D29's ratio.  It is not a second LSZ residue
and is not used to set `a_leg`.

*Justification.*  D24(b)(i)--(ii) and `AMP`, which leave only one proven
factor `Z_rho^(-1/2)` in the asymptotic-leg conversion.

**⟨2⟩2.**  The full-sector identity keeps
`A=D^dagger D` on the full positive-weight sector; the restricted identity
keeps `Pi_hw`.  Neither is algebraically substituted into (PMLM.12).

*Justification.*  The ML4-Ward ERRATUM and PROVED `S-IDX-fin-r2`.

**⟨2⟩3. QED.**


### ⟨1⟩10. Value corollary — and only here the number `1/S`

**ASSUME.**  The hypotheses of `(MATCH-HS-SEP)` and then take
`epsilon downarrow0` on a one-sided profile.

**PROVE.**  With `bar k_*(epsilon)=int k dmu_{*,epsilon}`,

`A_*(epsilon)=i sgn(v_h-v_s) bar k_*(epsilon)/S+O(epsilon^2)`, (PMLM.19)

and

`arg(1+A_*(epsilon))/bar k_*(epsilon)
       to sgn(v_h-v_s)/S`.                                  (PMLM.20)

**⟨2⟩1.**  Only now invoke

`S_phys(k,h)-1=i sgn(v_h-v_s)k/S+O_I(k^2)`.

*Justification.*  PROVED claim `S2-2body-S` (T.3)--(T.4).  No earlier step
of this shard uses its numerical derivative.

**⟨2⟩2.**  Integrate ⟨2⟩1 against the same measure in
(PMLM.18).  Since `|k|<=c_2 epsilon`, the integrated remainder is
`O(epsilon^2)`, proving (PMLM.19).

*Justification.*  D29's scale-tied support and (PMLM.18).

**⟨2⟩3.**  Use `arg(1+z)=Im z+O(|z|^2)` and D29's one-sided lower
bound `|bar k_*|>=c_1 epsilon` to obtain (PMLM.20).

*Justification.*  D7's continuous phase branch and proposed D29(2): a
probability measure on its one-sided soft interval has its mean in that
interval.

**⟨2⟩4.**  No value of `a_leg` follows from this corollary alone.
If `(PROTO-LSZ)`, D24-VAL membership, and the other antecedents of
`S-IDX-spec-r2` are separately supplied, the existing comparison in
`soft-index-r2.md` ⟨1⟩9 gives the conditional value
`a_leg(S)=1/(2S)`.  This shard neither supplies nor replaces those
antecedents.

*Justification.*  D24(d)3b and `AMP`: leg normalization supplies only
`Z_rho^(-1/2)`.  The value in (PMLM.19) came solely from `S2-2body-S`.

**⟨2⟩5. QED.**

### ⟨1⟩11. Honest boundary of the positive result

**ASSUME.**  The preceding ladder.

**PROVE.**  No adjacent gap or register has been silently merged.

**⟨2⟩1.**  `(PROTO-LSZ)` remains **OPEN**.  Nothing above decomposes
the D29 datum into descendant, orthogonal-current, direct-contact, and two
boundary-gradient pieces, proves microscopic `S_W(rho)` membership, or
evaluates D24(d)3b.

*Justification.*  Compare (PMLM.18), which is a whole-datum scattering
identity, with `soft-index-r2.md` (SPEC.3)--(SPEC.5), which is a component
decomposition with strictly stronger content.

**⟨2⟩2.**  The ML4-Ward ERRATUM is respected.  This proof uses no
scalar replacement of the full-sector `A=D^dagger D`.  At `S=1/2`, (R15)
is a diagnostic descendant projection only; (R16)--(R18) check the D7
multiplier but do not replace the wave-operator bridge (PMLM.12).

*Justification.*  `S-IDX-fin-r2` and `soft-current-recon.md` (R15)--(R18).

**⟨2⟩3.**  The theorem is primitive two-body only.  It asserts no
endpoint, equal-velocity, composite-charge, bound-state-channel, many-body,
or asymptotic-completeness result outside the two-magnon Jacobi sector.

*Justification.*  (PMLM.1), `S2-2body-S`'s exact scope, and ⟨1⟩3.

**⟨2⟩4. QED.**

## 4. Checker and frozen falsifier

### ⟨1⟩12. Checker contract

**ASSUME.**  `theory/checks/proto_lsz_match_check.py` and the frozen result
file `theory/checks/soft_index_probe_results.json`.

**PROVE.**  Every finite identity advertised by the new checker has a live
red mutation, while the analytic bridge is not over-certified.

| gate | green content | registered red | evidential limit |
|---|---|---|---|
| **PMLM-C1** | constructs `Q[f]Q[g]/(2S)` using the frozen probe's independent occupation-sector lowering matrix and compares it with (PMLM.2), including the spin-`S` double row | `--red-charge-map` replaces `sqrt((2S-1)/S)` by the canonical-boson diagonal coefficient | finite occupation algebra only; no scattering limit |
| **PMLM-C2** | independent Fourier packets show both initial and post-crossing collision traces decay under the allowed relative translation | `--red-separation` removes the translation | one numerical separated-packet example; `(SEP)` for all smooth packets is proved by nonstationary phase, not this grid |
| **PMLM-C3** | verifies the complex normalized-pairing identity (PMLM.16), phase cancellation, and its denominator bound | `--red-readout` uses a bilinear form without conjugating the free vector | finite functional algebra only; no D29 limit existence |
| **PMLM-C4** | evaluates D7's exact spin-`S` multiplier on a packet and recovers the `1/S` first jet after matching | `--red-channel` inserts `S_phys^(-1)` in the fixed D7 channel | supplier arithmetic only; it does not prove (PMLM.12) |
| **PMLM-C5** | reads the frozen outcome and checks **P1 plus P2(a) only**: the two registered P1 slopes/signs and the D24(e) source-jet errors | `--red-probe` changes the P1 target and corrupts one P2(a) datum | P2(b) fields are deliberately never read; its gate is the known no-op `tns-9z4` |

*Justification.*  Inspection of the checker and the recorded runs below.

**⟨2⟩1.**  Green command

`python3 -O theory/checks/proto_lsz_match_check.py`

exits zero.  The maximum C1 coefficient error is `7.86e-17`; C2's separated
collision ratio is `6.38e-3` and its post-crossing norm is `1.90e-5`; C3's
identity error is `7.98e-17`; C4's maximum finite-epsilon jet error is
`2.54e-5`.

*Justification.*  Recorded optimized run in this proposer pass.

**⟨2⟩2.**  Each of

`--red-charge-map`, `--red-separation`, `--red-readout`,
`--red-channel`, and `--red-probe`

exits one at its correspondingly named gate.  The checker contains no bare
`assert`; combined and unknown flags also exit one.

*Justification.*  Recorded red runs; every failure uses `SystemExit(1)`.

**⟨2⟩3.**  The frozen data quoted by C5 are exactly P1 slopes
`1.9929248158` at `S=1/2` and `1.0217264891` at `S=1`, with common positive
sign, and P2(a) relative source-jet errors `4.28e-8,5.45e-8`.  No P2(b)
protocol-insensitivity or finite-slope sentence is inferred.

*Justification.*  `soft_index_probe_results.json`, restricted to the fields
read by C5, and the binding `tns-9z4` falsifier ruling.

**⟨2⟩4.**  Passing these gates proves none of: fibre wave-operator
completeness, (PMLM.8)--(PMLM.12), D29/D30 in another class,
`(PROTO-LSZ)`, microscopic `S_W(rho)` membership, or `a_leg`.

*Justification.*  The checker is a finite regression certificate; the
analytic proofs are ⟨1⟩3--⟨1⟩6.

**⟨2⟩5. QED.**

## 5. MERGE PROPOSALS

Nothing in this section edits a shared definition or claims row.  D29/D30
remain quarantined exactly as required.

### ⟨1⟩13. Optional refinement inside the existing D29 proposal

> **(D29-HS-SEP: separated fully polarised two-magnon subclass).**  In the
> fully polarised `H_S` model, restrict D29's primitive hard/soft packets to
> a compact regular D7 channel with velocity gap `d_epsilon>0`.  Let the
> window datum translate the hard packet to its incoming side by `R_j`, let
> `sigma_j downarrow0`, and choose a settling time `T_j` with
> `L_j=d_epsilon T_j-R_j to infinity`.  At each fixed `epsilon`, require for
> some `M>=8`
> `K_(M,epsilon)s_M(f_epsilon)s_M(g_sigma_j)`
> `*[(1+R_j)^(3-M)+(1+L_j)^(3-M)]to0`, where `K_(M,epsilon)`
> contains the explicit inverse velocity gap and the regular-rectangle
> derivatives of `S_phys`.  After fixing that tuple, choose finite `N_j`
> with the D29 sampling inequality, recollision sandwich, and finite-ring
> kernel error `eta_j<=1/j`.  Take `epsilon downarrow0` last.  The concrete
> choice `R_j=ceil(sigma_j^(-2))`,
> `T_j=2R_j/d_epsilon` satisfies the condition.  This is an optional model
> subclass, not a clause of general D29 and not a matching assumption.

*Justification.*  ⟨1⟩1--⟨1⟩2 and (PMLM.8)--(PMLM.10).

### ⟨1⟩14. Proposed `claims/CLAIMS.md` rows

> | S-IDX-MATCH-HS-SEP | For the fully polarised bilinear ferromagnet `H_S` at every `2S in N`, on the primitive regular two-magnon channel and the displayed separated-preparation subclass `(D29-HS-SEP)`, along every actual row-measure limit subsequence the fixed-time charge-created finite-ring D29 readout converges to `int S_phys dmu` for that same D29 row measure.  Thus `(MATCH-S)` holds with zero remainder (hence through `o(epsilon)`).  The proof uses a norm bridge from the fixed-time product to the incoming wave operator and then to the outgoing multiplier; it does not identify the finite-separation vector with an HR creator, does not require a soft-uniform Cook estimate, and proves no `(PROTO-LSZ)` component decomposition. | SKETCH (post-critic single repair; shared-DAG adjudication pending) | D6--D8, D24(b), proposed D29, S2-2body-S | theory/proto-lsz-match.md ⟨1⟩1--⟨1⟩6 | theory/checks/proto_lsz_match_check.py PMLM-C1--C5; all five public red modes exit 1; gates do not test the wave operators |
>
> | S-IDX-D29-value-HS-SEP | Under `(D29-HS-SEP)`, along every actual row-measure limit subsequence the primitive fixed-time D29 scalar datum obeys `A_*(epsilon)=i sgn(v_h-v_s)bar k_*(epsilon)/S+O(epsilon^2)` and phase slope `sgn(v_h-v_s)/S`.  The value enters only after S-IDX-MATCH-HS-SEP through PROVED `S2-2body-S`.  This row makes no claim about `a_leg`, D24 class membership, `(PROTO-LSZ)`, endpoints, equal velocities, composite charges, or other protocol classes. | SKETCH (post-critic single repair; shared-DAG adjudication pending) | S-IDX-MATCH-HS-SEP, S2-2body-S | theory/proto-lsz-match.md ⟨1⟩10 | theory/checks/proto_lsz_match_check.py PMLM-C4 plus frozen P1+P2(a)-only C5 |

**⟨2⟩1.**  Keep `S-IDX-spec-struct-r2` and the general
`S-IDX-spec-r2` at **SKETCH**.  The former still lacks `(PROTO-LSZ)`; the
latter quantifies beyond `(D29-HS-SEP)` and retains its D24-VAL membership
antecedent.

*Justification.*  ⟨1⟩11.⟨2⟩1 and the live claims-row scopes.

**⟨2⟩2.**  Keep `S-IDX-HR-value-r2` separate and unchanged.  The proposed
bridge row does not cite it; this discussion merely compares with that
separate HR row, whose connection is now proved on `(D29-HS-SEP)` by the
shard's own ⟨1⟩3--⟨1⟩4 construction (MS-O3).

*Justification.*  ⟨1⟩8 and hard fence 4 of the work order.

**⟨2⟩3.**  Propose no change to D24, D30, `AMP`, `AC-EX-2M`, or
`S2-2body-S`.

*Justification.*  The proof neither alters their hypotheses nor widens their
status.

**⟨2⟩4. QED.**
