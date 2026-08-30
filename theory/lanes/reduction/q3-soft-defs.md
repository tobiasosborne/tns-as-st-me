# Q3 definitional audit: fixed-time soft insertions versus asymptotic soft legs

## 0. Scope, flags, and result in one paragraph

This is an audit of objects, not a promotion of claims.  In particular, D29
remains **PROPOSED**.  “Accepted soft insertion” below means an additional,
LSZ-amputated asymptotic massless leg at nonzero momentum, with the scattering
limit already taken, followed by the soft limit.  “Campaign insertion” means
the finite-time state made by the proposed D29 operator
`Q[f_epsilon]` acting on an already prepared hard packet, followed by D29's
own ordered limits.  Those are not definitionally the same vector.  They give
the same normalized on-shell readout on the proved separated-preparation
class `D29-HS-SEP`; outside that class the D6 control has an
`O(k_s)=O(epsilon)` state mismatch, exactly at the order of the claimed soft
jet.  The gauge-theory control is discriminating but not automatic: a proper
LSZ transplant has a `1/omega` Laurent pole, which violates D24(c)'s regular
Taylor hypotheses and D25's Adler behavior, while D10's matter/global charge
alone is not the soft-photon part of a large-gauge charge.  Statements marked
**[physical argument]** are perturbative/asymptotic reasoning not proved in
the campaign; statements marked **[textbook]** are standard lattice-QED or
LSZ background, not claims proved by this repository.

## 1. Continuum benchmark: what “insert one soft quantum” means

The local QED source fixes three pieces of the benchmark.

1. The object is an external asymptotic particle.  The theorem is stated for
   an “additional soft (`q^mu -> 0`) photon” and gives

   \[
   \langle {\rm out}|a^{\rm out}_+(\mathbf q){\cal S}|{\rm in}\rangle
   =e\left[
     \sum_{{\rm out}\ k}Q_k{p_k\!\cdot\!\varepsilon^+\over p_k\!\cdot q}
    -\sum_{{\rm in}\ k}Q_k{p_k\!\cdot\!\varepsilon^+\over p_k\!\cdot q}
   \right]\langle {\rm out}|{\cal S}|{\rm in}\rangle+O(q^0).
   \]

   The wording and formula are at
   `refs/arxiv-1703.05448/soft_Arxiv_update.tex:1075-1083`.  Thus the
   unrescaled leading multiplier is a Laurent coefficient of order
   `q^{-1}`, not a derivative of a regular function at `q=0`.

2. The leg is LSZ-amputated.  The same source describes LSZ as computing
   time-ordered Green functions and “then amputating the external legs”
   (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1095`); attaching the photon
   to an amputated hard external leg adds precisely one vertex and the
   adjacent hard propagator (`:1095-1096`).  The scattering operator itself
   is tied there to the asymptotic limit `T -> infinity`
   (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:882-894`).  The definitional
   order is therefore

   \[
   \boxed{\text{amputate/select the asymptotic in/out leg at fixed }q\ne0
   \quad\text{before}\quad q\to0.}                            \tag{1.1}
   \]

   **[textbook]** In a wave-packet construction, “select the asymptotic leg”
   means first taking the Haag--Ruelle/LSZ large-time limit for packets whose
   velocity supports are separated.  A zero-momentum creation operator at a
   finite time is not a substitute for that limit.

3. Charge insertion is equivalent only after its soft part has been
   identified with that asymptotic mode.  The QED Ward identity inserts
   `Q_epsilon^+ S-S Q_epsilon^-` between in/out states
   (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:889-925`).  Its soft field is

   \[
   \partial_zN\propto\lim_{\omega\to0^+}
   \bigl[\omega a_+^{\rm out}(\omega\hat x)
        +\omega a_-^{{\rm out}\dagger}(\omega\hat x)\bigr],
   \]

   while the matrix element has the compensating pole
   (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1005-1014`).  The source then
   says these Ward identities are “precisely the same thing” as the known
   soft theorems (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:925`) and
   completes the equivalence at `:1064-1066`.  Hence
   the accepted charge statement does **not** say that an arbitrary
   finite-time modulated matter charge is already an LSZ photon; it uses the
   asymptotic soft component of the full large-gauge charge.

The gauge-free source makes the same order explicit for a Goldstone mode:

\[
 Q^{\rm soft}(\hat{\mathbf q})=-{i\over4\pi}
 \lim_{\omega\to0}
 \left(a^{(\pi)\dagger}_{\omega\hat{\mathbf q}}
       -a^{(\pi)}_{\omega\hat{\mathbf q}}\right).
                                                               \tag{1.2}
\]

It states that this operator “creates (or annihilates) a soft pion”
(`refs/arxiv-1709.05018/draft1004.tex:359-363`), and separately instructs one
to Fourier transform to on-shell momentum, apply LSZ to the other fields,
and only then take `omega -> 0`
(`refs/arxiv-1709.05018/draft1004.tex:450-458`).  Equation (1.2) is therefore
a limit of asymptotic creation/annihilation operators, not a fixed-time local
charge density acting on a hard state.

## 2. Fixed-time D29 versus the asymptotic leg: the D6 control

### 2.1 What the fixed-time charge actually creates

On the spin-`1/2` ferromagnet D6, for distinct ring momenta, the charge acting
on a normalized hard magnon makes the exact two-spin-flip state

\[
 Q_{k_s}|k_h\rangle_N={1\over\sqrt N}\sum_{x<y}
 \left[e^{i(k_sx+k_hy)}+e^{i(k_hx+k_sy)}\right]|x,y\rangle .  \tag{2.1}
\]

Thus the two ordered plane-wave branches have coefficient ratio one.  An
incoming scattering eigenwave in the same D7 chamber instead has

\[
 |B^{\rm in}\rangle=S_{12}|P_{12}\rangle+|P_{21}\rangle .    \tag{2.2}
\]

The repository proves the exact difference

\[
 Q_{k_s}|k_h\rangle-|B^{\rm in}\rangle
   =(1-S_{12})|P_{12}\rangle
   =-2ik_s|P_{12}\rangle+O(k_s^2),                            \tag{2.3}
\]

with relative size
`sqrt(2)|k_s|(1+O(k_s))`; see `theory/soft-current-recon.md:57-78,
145-160,351-366` and the authoritative row `AC-EX-2M-D29`.  Equation (2.3)
is the requested quantitative distinction.  The fixed-time charge creates a
bare symmetrized product with a contact/ordered-branch defect.  The accepted
asymptotic creator creates the scattering solution with its incoming boundary
condition and therefore already contains `S_12`.

For D29's scale-tied packet, `k_s` lies between `c_1 epsilon` and
`c_2 epsilon`.  Smearing (2.3) consequently gives a relative
`O(epsilon)` discrepancy, subject to the packet bounds used in the cited
claims.  This is not an ignorable higher-order normalization effect:

\[
 S_{\rm phys}(k_s,k_h)-1
 =2i\,\operatorname{sgn}(v_h-v_s)k_s+O(k_s^2)                 \tag{2.4}
\]

on D6.  The state mismatch and the desired Adler first jet are both linear.
This is why `AC-EX-2M-D29` correctly leaves the unrestricted fixed-time
charge/channel identification **OPEN**, even though Haag--Ruelle
creator-choice independence is proved for genuine Haag--Ruelle families.
That theorem has a different antecedent and cannot be applied to (2.1).

The finite `Q_0|k_h>` anchor does not repair this.  `S-IDX-fin-r2` proves that
the pure zero-mode-created row ratio is one, but explicitly makes no statement
about the running D29 family.  At fixed `N`, D29's one-sided soft sample is
empty once `c_2 epsilon<2pi/N`; there is no fixed-`N` continuous path from
the running packet to its `k=0` row.  An intercept at a separately adjoined
zero mode therefore does not determine the first jet.

### 2.2 The order in which equality can be recovered

The proposed D29 definition gets the essential **order** right.  It holds
`epsilon>0` fixed while the finite-volume/scattering preparation is removed,
and takes `epsilon downarrow 0` only after an outer limit point has been
selected.  In the notation of `AC-EX-2M-D29`, the order is

\[
 N\to\infty\ \prec\ T\to\pm\infty\ \prec\
 (W\uparrow\mathbb Z,\sigma\downarrow0)\ \prec\
 \epsilon\downarrow0,                                      \tag{2.5}
\]

implemented by admissible diagonal sequences respecting D29's sampling and
no-recurrence inequalities.  What is missing in general is not the order but
the theorem that the fixed-time starting vector reaches the asymptotic
channel with sufficient first-order control.

There is now one proved class where that bridge exists.  On the fully
polarized bilinear spin-`S` ferromagnet, restrict to `D29-HS-SEP`:

- the soft and hard packets are smooth, compactly supported, in one regular
  primitive two-magnon channel, and their velocity supports are disjoint at
  each fixed `epsilon`;
- the initial relative separation `R_j` tends to infinity, the hard width
  `sigma_j` tends to zero, and the settling time obeys
  `L_j=d_epsilon T_j-R_j -> infinity`;
- for one `M>=8`, the displayed `(SEP)` product of packet seminorms and the
  powers `(1+R_j)^(3-M)`, `(1+L_j)^(3-M)` tends to zero; and
- only after `R_j,sigma_j,T_j` are fixed is `N_j` chosen large enough for
  momentum sampling, finite-time thermodynamic approximation, and absence of
  recurrence.  The soft limit remains last.

The norm bridge proved in that class has the schematic quantitative form

\[
 \|e^{-iH_ST}I_SF_R-I_SU_0(T)M_{S_{\rm phys}}F_R\|
 \le K_{M,\epsilon}s_M(f_\epsilon)s_M(g_\sigma)
 \left[(1+R)^{3-M}+(1+d_\epsilon T-R)^{3-M}\right],           \tag{2.6}
\]

before the separately controlled finite-ring error.  This is
`theory/proto-lsz-match.md:299-374`.  The `SEP` sequence makes (2.6) and the
readout errors vanish at every fixed `epsilon`; no bound uniform in
`epsilon` is asserted or needed.

Consequently, along every actual row-measure limit subsequence in this
class,

\[
 \boxed{\mathcal A_*(\epsilon)
 =\int [S_{\rm phys}(k,h)-1],d\mu_{*,\epsilon}(k,h)} .        \tag{2.7}
\]

This is the PROVED row `S-IDX-MATCH-HS-SEP` and
`theory/proto-lsz-match.md:495-533`.  It has **zero readout remainder at each
fixed `epsilon` after the outer limit**, so it is automatically an
`o(epsilon)` match when the soft limit is finally taken.  It does not say
that the finite-separation vector equals a Haag--Ruelle creator and does not
prove the componentwise `(PROTO-LSZ)` decomposition.

### 2.3 Clean equivalence statement

The two definitions coincide as scattering **readouts**, not as bare
finite-time vectors, precisely in the following proved setting:

\[
 \boxed{\begin{gathered}
 \text{regular primitive two-magnon channel of the fully polarized }H_S,\\
 \text{the separated class }D29\text{-HS-SEP, and the order (2.5),}\\
 \text{with an actual common row-measure limit subsequence.}
 \end{gathered}}                                             \tag{2.8}
\]

At fixed nonzero soft scale the D29 ratio then equals the accepted on-shell
multiplier average exactly after the outer limit, and its soft expansion is
taken afterward.  For a general D29 preparation no such equivalence theorem
exists.  The best model control is the `O(k_s)=O(epsilon)` mismatch (2.3),
which is nonzero at the first-jet order; calling the two definitions equal in
that scope would assume the missing bridge.

## 3. Weinberg-pole control in 3+1 lattice QED

### 3.1 External-leg calculation

**[textbook] [physical argument]** Consider Hamiltonian lattice QED with
continuous time and a spatial lattice spacing `a`, in a Coulomb/massless-
photon regime.  Work perturbatively with an infrared regulator so that the
usual external charged leg is meaningful.  Let `E(p)` be the hard charged
particle's lattice dispersion, `v(p)=nabla_p E(p)`, and let a soft transverse
photon have spatial momentum `k`, energy
`omega_gamma(k)=c_gamma(hat k)|k|+O(a^2|k|^3)`.  The hard propagator adjacent
to emission from an outgoing on-shell leg has denominator

\[
 (p^0+\omega_\gamma)^2-E(\mathbf p+\mathbf k)^2
 =2E(\mathbf p)\,[\omega_\gamma-\mathbf v(\mathbf p)\!\cdot\!\mathbf k]
  +O(|k|^2).                                                  \tag{3.1}
\]

Equivalently, the lattice Ward--Takahashi identity has the small-momentum
form

\[
 \widehat q_\mu\Gamma^\mu(p+q,p)
 =eQ\,[G^{-1}(p+q)-G^{-1}(p)],                               \tag{3.2}
\]

where `widehat q_mu=q_mu+O(a^2q^3)`.  On shell,
`G^{-1}(p)=0`, so the same first derivative of `G^{-1}` that appears in the
vertex appears in the adjacent propagator.  Contracting the vertex with a
transverse polarization gives, in the long-wavelength limit,

\[
 \Gamma\!\cdot\!\varepsilon\,G(p+q)
 =eQ\,{p_{\rm lat}\!\cdot\!\varepsilon
        \over p_{\rm lat}\!\cdot q}+O(|k|^0)
 ={C(p,\varepsilon,\hat k)\over
   |k|[c_\gamma(\hat k)-\mathbf v(p)\!\cdot\!\hat k]}
  +O(1).                                                       \tag{3.3}
\]

The precise lattice numerator is action-dependent, but the pole is not:
gauge invariance relates it to the derivative of the inverse propagator.
Summing outgoing and incoming attachments yields

\[
 \mathsf S_{\rm gauge}(q)=
 \sum_i\eta_i eQ_i{p_{i,{\rm lat}}\!\cdot\!\varepsilon
                    \over p_{i,{\rm lat}}\!\cdot q}
 ={\mathsf S_{-1}(\hat k)\over |k|}+O(1),                    \tag{3.4}
\]

with `eta_i=+1` for outgoing and `-1` for incoming legs.  Attachments to
generic internal lines remain off shell and are `O(1)`.  This is exactly the
mechanism displayed in the local continuum TeX: the adjacent scalar
propagator becomes `-i/(2p dot q)`
(`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1115-1119`), the vertex supplies
the numerator (`:1120-1127`), and their sum is the Weinberg factor
(`:1129-1136`).

**[textbook]** This is a definitional control, not a nonperturbative lattice theorem.  In
particular, charged states in infinite-volume QED have the usual infrared
dressing/infraparticle qualifications; the calculation tests the same
regulated perturbative LSZ register used by the local continuum source.

### 3.2 Where the pole lands in the campaign's language

D24(b)'s basic object is structurally capable of displaying (3.4): it calls
`M_2` the connected amplitude with one additional, delta-normalized
**asymptotic** soft leg and applies the same hard-leg amputation in `M_2` and
`M_1`.  With a photon in place of a magnon, the factorization would read

\[
 M_{n+1}(k;\{p_i\})
 =\left[{\mathsf S_{-1}(\hat k)\over |k|}+O(1)\right]M_n
   +R(k),\qquad R(k)=O(1)=o(|k|^{-1}).                         \tag{3.5}
\]

In jet language, `mathsf S_{-1}` is the **first Laurent jet** (the residue),
not the ordinary first Taylor derivative.  Equivalently,
`|k| mathsf S_gauge` has a finite directional soft limit, whereas
`mathsf S_gauge` itself has no value or derivative at `k=0`.

This sharply fails the hypotheses that define the campaign's global
Goldstone class:

- D24(c)'s `C^2` Taylor map, zero intercept, and finite contact first jet do
  not exist for (3.5);
- D24(d)3's finite `C^1` external-flux function and its Adler decomposition
  cannot simply be carried over; the hard external propagator is singular;
  and
- D25's scoped conjecture `mathsf S -> 0` with leading term linear in `k_s`
  is replaced by `mathsf S_gauge~1/|k|`.

The physical distinction is the numerator.  The campaign's global-symmetry
Ward insertion carries a lattice difference such as `e^{ik}-1=O(k)` and,
inside its no-contact class, produces a regular Adler expansion.  A
transverse gauge photon couples to the charged external leg with a nonzero
`O(k^0)` vertex numerator, while the adjacent on-shell propagator supplies
`1/(p dot q)=O(1/|k|)`.  Therefore the pole sits in the multiplier itself,
not in a finite value of `mathfrak a_leg` and not in a regular D25 first
derivative.

### 3.3 What the modulated charge does and does not supply

**[textbook] [physical argument]** A literal transplant of D10's
`Q[f]=sum_x f(x)q_x` as a **matter/global** charge does not create a
transverse photon.  On the physical Hilbert space of lattice QED, Gauss's law
relates matter charge to the divergence of electric flux.  Summation by parts
turns a modulated matter charge into a bulk electric-field-gradient term plus
a boundary flux.  The continuum large-gauge charge correspondingly has both
a hard matter part and a soft radiative/boundary part.  It is the latter that
contains
`lim_(omega->0) omega(a+a^dagger)` in the QED source
(`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1005-1019`).

Hence D10 alone does **not produce** the Weinberg pole or even the accepted
photon leg.  To perform the gauge transplant one must:

1. replace the D10 matter/global insertion by the full gauge charge and
   isolate its soft photon component, or insert the asymptotic transverse
   photon directly as D24(b) prescribes;
2. take the thermodynamic/scattering limit at fixed nonzero `k`; and
3. replace D24(c)/D25's Taylor/Adler register by the Laurent register (3.5)
   before taking `k->0`.

**Control verdict.**  The definitions are not blind to the gauge/global
difference: the QED amplitude is rejected by the regular no-contact/Adler
class for the right, observable reason, namely its negative first Laurent
power.  But the campaign does not derive that pole from D10 or D25.  If D25's
linear-zero clause were advertised unchanged as a definition covering QED,
it would be a definitional failure.  As actually written, D25 is explicitly a
Corner-C global-Goldstone conjecture, so the honest conclusion is narrower:
it distinguishes the two infrared classes by **scope and failed regularity**,
not by one unified charge-insertion definition.  The handoff's statement that
there is no clean `1/omega` pole in its 1D spin-chain setting is therefore
consistent with, and does not exclude, the standard long-wavelength pole in
3+1 lattice QED.

## 4. G0 “pure gauge” versus the soft photon as a large gauge mode

### 4.1 The two meanings

G0 uses **MPS representation gauge**.  For an unbroken on-site direction
`xi in h_alpha`, normal ordering removes the ray term and gives

\[
 B_G(\xi)=\mathcal N_0(X_\alpha(\xi))
          =A_\alpha X_\alpha(\xi)-X_\alpha(\xi)A_\alpha .     \tag{4.1}
\]

This is the tangent to the virtual similarity transformation of one tensor
representation.  It leaves the infinite-chain bulk state unchanged.  G0
also proves the converse (allowing the scalar ray before normal ordering): a
Goldstone tensor lies in `ran N_0+C A_alpha` if and only if the physical
symmetry direction is unbroken.  A broken direction fails same-vacuum return
and is a physical tangent to the vacuum manifold, not an MPS-null direction
(`theory/corner-a-goldstone.md:145-160,207-225`).

At nonzero momentum the exact algebra is

\[
 B_G(\xi)=\mathcal N_k(X_\alpha(\xi))
          +(1-e^{ik})A_\alpha X_\alpha(\xi).                  \tag{4.2}
\]

The `N_k` term telescopes to endpoints on a finite window.  It vanishes only
in one of D12's named senses: for `l^1 cap BV` packets after the window limit,
or for a fixed plane wave after delta normalization.  D12 does not say that
the finite-window boundary vector is zero and does not prove convergence for
an arbitrary `c_0` profile.

Electromagnetism uses **spacetime gauge**,
`A_mu -> A_mu+partial_mu epsilon`.  A proper/small transformation is a
redundancy, but a large transformation has a parameter that approaches a
nonzero angle-dependent function at null infinity and acts nontrivially on
the asymptotic phase space.  Under the no-asymptotic-magnetic-field condition,
the local source obtains

\[
 A_z^{(0)}|_{\mathcal I^+_+}-A_z^{(0)}|_{\mathcal I^+_-}
 =e^2\partial_zN,                                             \tag{4.3}
\]

and says the “relative shift better also be pure gauge”
(`refs/arxiv-1703.05448/soft_Arxiv_update.tex:723-743`).  The allowed large
transformation is `delta A_z=partial_z epsilon`, with
`epsilon=epsilon(z,bar z)+O(1/r)`
(`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1224-1234`).  Despite being flat
in the bulk, this boundary mode is not quotiented out: its charge changes the
vacuum and its quantum description creates a zero-energy photon.  The source
accordingly identifies soft photons with the Goldstone modes of spontaneously
broken large-gauge symmetry
(`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1239-1243,1286-1295`).

### 4.2 Exact correspondence and the obstruction

| feature | MPS G0/D12 | electromagnetic soft mode |
|---|---|---|
| coboundary | `delta A^s=A^sX-XA^s` | `delta A_mu=partial_mu epsilon` |
| bulk invariant | the represented infinite-chain local state | `F_munu` and proper-gauge observables |
| finite-region remnant | two virtual endpoint vectors | surface/asymptotic charge data |
| status of the remnant in the definition | sent to zero in the stated D12 bulk topology | retained; it is the large-gauge degree of freedom |
| physical symmetry direction called pure gauge | unbroken direction only | large asymptotic direction, spontaneously broken and physically nontrivial at the boundary |

The exact common statement is therefore only this:

\[
 \boxed{\text{a zero-momentum coboundary changes no local bulk field/state
 but can leave boundary data.}}                               \tag{4.4}
\]

The difference is load-bearing.  G0 calls (4.1) pure gauge precisely because
the endpoint data are discarded in the infinite-bulk excitation topology;
the continuum large-gauge construction calls (4.3) locally pure gauge while
**retaining** its asymptotic endpoint data as a physical charge and vacuum
label.  Consequently:

- G0's unbroken MPS-null direction corresponds most closely to a
  **proper/small** gauge redundancy, not to a physical soft photon.
- G0's broken, non-null Goldstone direction is the closer physical analogue
  of the soft photon as a Goldstone mode, but it is not of the form
  `AX-XA` and hence is not “pure gauge” in G0's definition.
- An exact analogue of a large-gauge soft photon would require an enlarged
  MPS asymptotic/edge phase space in which the telescoping endpoint vectors
  are retained and charged, rather than removed by D12.  D10--D12 do not
  define such a space.

Thus the slogans share a coboundary algebra but not a quotient.  Equating
“MPS null” with “large gauge” would reverse the broken/unbroken content of
both definitions.

## 5. Verdict by definition

### 5.1 D10 + D12

**Verdict: SAME UP TO LISTED GAPS; not the accepted object by definition.**

D10 defines a finite-time, spatially modulated global Noether charge.  D12
controls only the endpoint remainder produced by an MPS representation-gauge
coboundary, in either the `l^1 cap BV` packet limit or the delta-normalized
fixed-momentum topology (`definitions.md:466-500,523-570`).  Together with
D11 they give a legitimate interpolating operator for a Goldstone excitation.
On the D6 vacuum, after normalization, that operator creates the exact
one-magnon kernel.  These are real points of contact with the continuum
definition.

They do not, however, perform LSZ reduction, select an in/out boundary
condition, or prove that the charge acting on a hard state is an asymptotic
additional leg.  Equation (2.3) is a proved counterexample to such a general
identification.  Equality with the accepted global-Goldstone leg therefore
requires, at fixed nonzero momentum, an exact one-particle spectral
projection or Haag--Ruelle/LSZ bridge, leg normalization, separated velocity
supports, and the scattering limit before the soft limit.  In a gauge theory
D10 also lacks the soft radiative part of the large-gauge charge.  D12 cannot
supply any of these missing operations.

### 5.2 D24(b)

**Verdict: SAME OBJECT UNDER ITS STATED ASYMPTOTIC-LEG REGISTER; existence is
not general.**

D24(b) explicitly defines `M_2` with one additional delta-normalized
**asymptotic** magnon of momentum `k` and unit leg weight, and explicitly says
that this is not a charge-created or current-created vector
(`definitions.md:943-1008`).  That is the lattice-magnon analogue of the
accepted LSZ external-leg definition.  It is constructed on the fully
polarized spin-`S` family; off the registers named in D24(b), existence of the
kernel remains open.  Its normalization fence is essential:

\[
 Q_k|\Omega\rangle=\sqrt{Z_\rho}\,|k\rangle,
 \qquad
 {\|Q_q|h\rangle\|\over\sqrt N}
   =\sqrt{Z_\rho-2/N}\longrightarrow\sqrt{Z_\rho}.            \tag{5.1}
\]

Thus a charge-created leg becomes the D24(b) leg only after the displayed
conversion in the LSZ limit; a common finite-state factor must not be used to
set `mathfrak a_leg`.

### 5.3 D25

**Verdict: SAME FACTORIZATION SLOT, DIFFERENT AND NARROWER INFRARED CLASS.**

D25 names a multiplier of an amplitude with an additional asymptotic leg, so
its *slot* is the accepted soft factor.  But it further scopes the proposed
Corner-C object to the Ward-covariant no-contact class and conjectures a
regular Adler law, `mathsf S(k_s)->0` linearly with `k_s`
(`definitions.md:1170-1185`).  That behavior is not the definition of every
continuum Goldstone theorem: the local pion example has a finite `O(1)` soft
factor in the presence of the stated hard fermions and an Adler zero only in
the restricted case without them
(`refs/arxiv-1709.05018/draft1004.tex:146-148,330-350`).  It is emphatically
not the QED soft factor, whose leading term is (3.4).

Accordingly, D25 is an honest candidate definition for a restricted global
spin-chain soft multiplier, with existence/factorization/universality still
`S-general` **CONJECTURE**.  It is not a gauge-unified definition.  The QED
control does not silently pass through it: the `1/|k|` pole makes its Taylor
premises false.

### 5.4 D29 (PROPOSED)

**Verdict: DIFFERENT FINITE DATUM; SAME ASYMPTOTIC READOUT ONLY ON THE PROVED
SEPARATED CLASS AND IN THE STATED ORDER.**

D29 deliberately defines the finite state `Q[f_epsilon]psi_g`, its evolved
coordinate kernel, and a normalized interacting/free projection ratio.  It
also deliberately declines to define LSZ exhaustiveness, wave operators,
on-shell matching, or the `epsilon=0` member of the family
(`theory/soft-index-r2.md:1128-1227`).  It is therefore not the same object as
an amputated soft-leg amplitude.

For general preparations, D6 proves the difference from the incoming
asymptotic wave is `O(k_s)=O(epsilon)` with relative coefficient
`sqrt(2)|k_s|+O(k_s^2)`.  This is the same order as the sought first jet, so
the unrestricted equivalence and D29 first-jet theorem remain open as stated
in `AC-EX-2M-D29`.

For `D29-HS-SEP`, the verdict improves at the level of the normalized
readout: the norm/readout bridge proves (2.7) with zero remainder after the
outer limit at every fixed `epsilon`.  The accepted soft limit may then be
taken.  This is exactly `S-IDX-MATCH-HS-SEP`; it proves neither finite-vector
equality nor `(PROTO-LSZ)` and does not change D29's **PROPOSED** status.

### 5.5 G0's pure-gauge clause

**Verdict: SAME BULK-COBOUNDARY FORM, DIFFERENT PHYSICAL QUOTIENT.**

G0 is exact for unbroken directions and in D12's named topologies.  Its
MPS-null direction is analogous to proper gauge redundancy.  A continuum
soft photon is instead the boundary mode of a broken **large** gauge
symmetry; locally flat does not mean physically quotiented out.  The current
definitions contain no exact MPS counterpart of that retained asymptotic
edge mode.

## 6. Final answer to Q3

The campaign has two different definitions in play and should continue to
name them separately:

\[
 \begin{array}{c}
 \text{D29: fixed-time }Q[f_\epsilon]\text{ datum}\\[2pt]
 \xrightarrow[\text{proved only on }D29\text{-HS-SEP}]
 {N,T,R,W,\sigma\text{ outer limit at fixed }\epsilon}
 \text{D24(b): asymptotic-leg multiplier average}\\[2pt]
 \xrightarrow{\epsilon\downarrow0\text{ last}}
 \text{soft theorem.}
 \end{array}                                                   \tag{6.1}
\]

On that separated class the definitions coincide as readouts with zero
outer-limit remainder.  Otherwise they differ already by `O(k_s)` in the D6
control, so their intercept can agree while their first jets differ.  D24(b)
itself is the accepted LSZ-type definition; D10/D12 supply a possible
interpolating charge but no general LSZ bridge; D25 selects the regular
global/Adler class; and D29 remains a useful but genuinely pre-asymptotic
**PROPOSED** protocol datum.

The Weinberg control confirms rather than blurs the distinction.  Once the
additional leg is a transverse asymptotic photon, its adjacent hard
propagator forces a `1/|k|` Laurent pole.  This lies outside D25 and D24(c)'s
regular Taylor class.  A literal D10 matter-charge insertion will not create
it; the full large-gauge soft charge or the photon LSZ creator is required.
