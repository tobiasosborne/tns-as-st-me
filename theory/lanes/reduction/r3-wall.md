# R3 — continuum reduction of the XXZ kink memory corner

## Source note

The recommended source arXiv:1108.5570 was absent.  After the prescribed
three-second wait, a fetch from `https://arxiv.org/e-print/1108.5570` was
attempted, but the execution environment could not resolve `arxiv.org`; no
source archive was received and `refs/arxiv-1108.5570/` remains empty.  More
importantly, verification reveals that the identifier in the brief is wrong:
arXiv:1108.5570 is *Hamiltonian dynamics and constrained variational
calculus: continuous and discrete settings* (de Leon--Jimenez--Martin de
Diego), whereas Yan--Wang--Wang's *All-magnonic spin-transfer torque and domain
wall propagation*, PRL 107, 177207 (2011), is arXiv:**1106.4382**.  The latter
title, authors, DOI, and journal data are also present locally in
`refs/arxiv-2107.05401/particle_collision_V4.8.tex:586-596` (entry
`yan_AllMagnonic_2011`) and `refs/arxiv-1406.6051/AF-wall-magnons.bbl:99-107`.
I do not pretend that the failed fetch verified the requested title.  The
continuum equations below are instead taken from the locally available
ferromagnetic calculation `refs/arxiv-1712.06578/QD-9.tex`; the Yan paper is
used only through a separately identified primary-source result and the local
literature's summary of its angular-momentum argument.

## 1. Continuum limit of the D16 kink model

Write the lattice spacing explicitly as `a`, put `x=na`, and replace the spin
by a slowly varying coherent field, `S_n=s n(x)`, `|n|=1`.  Expanding the D16
Hamiltonian relative to either polarised vacuum gives

\[
 E[\mathbf n]=\frac12\int dx\,
 \left[A(\partial_x\mathbf n)^2+K(1-n_z^2)\right]+O(a^2\partial_x^4),
 \qquad
 A=Js^2a,\qquad K=\frac{2Js^2(\Delta-1)}a .                 \tag{1.1}
\]

[physical argument]  Here the exchange contribution follows from
`1-n(x)\cdot n(x+a)=a^2(\partial_x n)^2/2+...`, while the excess Ising
coupling supplies `Js^2(Delta-1)(1-n_z^2)` per site.  Together with the spin
Berry term of density

\[
 M_0=\frac{s}{a},
\]

(in units `hbar=1`), (1.1) is the easy-axis ferromagnetic Landau--Lifshitz
field theory.  Equivalently,
`M_0 partial_t n = -n cross delta E/delta n`, up to the convention for the
gyromagnetic sign.  The same continuum energy and Berry structure are written
in `refs/arxiv-1712.06578/QD-9.tex:69-79`, with exchange stiffness `A`,
easy-axis anisotropy `K_e`, and spin density `s` (that source's `s` is a
density, whereas D16's `s` is spin per site).

[physical argument]  The controlled continuum scaling is

\[
 a\longrightarrow0,\qquad \Delta=1+\epsilon\longrightarrow1^+,
 \qquad A=Js^2a\ \hbox{fixed},\qquad
 K=\frac{2Js^2\epsilon}{a}\ \hbox{fixed}.                 \tag{1.2}
\]

Thus `epsilon=K a^2/(2A)`; in lattice units one can say instead that
`epsilon -> 0` while distances are measured in units of the diverging wall
width.  Merely taking long magnon wavelength at fixed `Delta>1` is not this
continuum limit.

Minimising (1.1) with boundary conditions `n_z(+/- infinity)=+/-1` gives the
180-degree Walker/Bloch wall

\[
 n_z(x)=\pm\tanh\frac{x-X}{\lambda},\qquad
 n_x+i n_y=e^{i\Phi}\operatorname{sech}\frac{x-X}{\lambda},
 \qquad \lambda=\sqrt{\frac AK}=\frac{a}{\sqrt{2(\Delta-1)}} .       \tag{1.3}
\]

[physical argument]  This is the easy-axis LL static soliton.  The local
source gives precisely `cos theta_0=tanh((x-X)/lambda)` and
`lambda=sqrt(A/K_e)` at `refs/arxiv-1712.06578/QD-9.tex:81-92`; it also
identifies `X` and `Phi` as the translational and axial collective coordinates
there.

The D16 parameter makes the lattice/continuum match especially transparent.
Set

\[
 q=e^{-\eta},\qquad \eta=\operatorname{arcosh}\Delta .
\]

For the spin-`1/2` product kink `|K(z)>`, `z=q^{-x_0}e^{i\phi}`, direct
normalisation of its one-site factor gives

\[
 2\langle S_n^z\rangle
 =\frac{1-q^{2(n-x_0)}}{1+q^{2(n-x_0)}}
 =\tanh[\eta(n-x_0)].                                      \tag{1.4}
\]

Hence its width is

\[
 \xi_{\rm lat}=\eta^{-1}=\frac1{\operatorname{arcosh}\Delta}
 \quad\hbox{sites},\qquad
 \lambda_{\rm phys}=a\xi_{\rm lat},                       \tag{1.5}
\]

and `eta=sqrt(2 epsilon)+O(epsilon^(3/2))`, so (1.5) agrees with
(1.3) in the broad-wall regime.  Equations (1.4)--(1.5) are an algebraic
consequence of the D16 product family and `q` convention
(`definitions.md:669-680`), not a new status claim.

There are two walls in the lattice discussion that must not be conflated.
The exact dressed `K(z)` profile has the finite width (1.5).  By contrast, the
product-basis incoming wall used by Mq-E and hence by the proved projected
M-tk formula is a **sharp wall on one bond** (`theory/mq-e.md:100-145` and
`390-467`): at fixed `Delta>1` it remains a one-lattice-spacing core.  In the
deep-Ising regime `Delta>>1`, `eta~log(2Delta)` and even the dressed profile
has `xi_lat<1`, so the one-bond description is physically natural.  At any
fixed `Delta>1`, its physical width collapses as `a->0`; it does not approach
a finite-width Walker wall.  The only meaningful LL reduction is therefore
(1.2), for which `xi_lat->infinity`.  [physical argument]  In the sharp-wall
configuration basis, such a broad wall necessarily involves a coherent
superposition whose required wall-number/configuration support is not bounded
by the Mq-E projection.

## 2. Transmission puzzle: the two formulas do not share a controlled limit

### 2.1 What continuum LL actually predicts

Linearise the easy-axis LL equation about (1.3), set
`y=(x-X)/lambda`, and resolve a circular transverse fluctuation.  After the
standard local-frame rotation, its spatial equation contains

\[
 \mathcal H_{\rm PT}=-\partial_y^2+1-2\operatorname{sech}^2y .       \tag{2.1}
\]

[physical argument]  This is the `l=1` Pöschl--Teller problem.  The local
ferromagnetic source derives exactly (2.1), its supersymmetric factorisation,
and the statement that the potential is reflectionless at
`refs/arxiv-1712.06578/QD-9.tex:95-121`.  Its continuum eigenfunction is

\[
 \psi_\kappa(y)=
 \frac{\tanh y-i\kappa}{1-i\kappa}e^{i\kappa y},
 \qquad \kappa=p\lambda,                                    \tag{2.2}
\]

as quoted at `refs/arxiv-1712.06578/QD-9.tex:123-142`.  Since (2.2) contains
only `e^{+i kappa y}` at both infinities, `r_LL=0`; normalising the incoming
coefficient at `y->-infinity` gives, in this convention,

\[
 t_{\rm LL}(\kappa)=-\frac{1-i\kappa}{1+i\kappa},\qquad
 T_{\rm LL}(\kappa)=1                                      \tag{2.3}
\]

for every real `kappa` (with the zero-momentum value understood as the
threshold limit).  This also agrees with the source's explicit summary that
there is no magnon reflection (`QD-9.tex:60`).  Crucially, (2.3) remains true
for `kappa<<1`, when the wavelength is much longer than the wall.  Therefore
"wall width versus wavelength" by itself cannot turn continuum transmission
into reflection.

### 2.2 Put the proved lattice formula in the same variables

M-tk is **PROVED for the projected incoming `<=3`-wall component**, not for
the unprojected XXZ chain (`theory/mq-e.md:488-496`; the unchanged scope and
the full-chain leakage warning also appear in
`theory/corner-b-draft.md:349-356`).  With

\[
 \eta=\operatorname{arcosh}\Delta=\frac a\lambda,
 \qquad \kappa=p\lambda=\frac{k}{\eta},                       \tag{2.4}
\]

the proved projected expression is

\[
 T_{\rm proj}(k,\eta)=
 \left\{1+\left[4(\cosh\eta-\cos k)\sin k\right]^{-2}\right\}^{-1}.
                                                                    \tag{2.5}
\]

At fixed `Delta>1`, `k->0` gives the proved M-tk result

\[
 T_{\rm proj}=16(\Delta-1)^2k^2+O(k^4)\longrightarrow0,       \tag{2.6}
\]

quoted with unchanged status at `theory/memory-quantization.md:385-402`.
Now take the actual broad-wall scaling rather than merely naming it: put
`k=eta kappa`, keep `kappa>0` fixed, and send `eta->0`.  Then

\[
 \cosh\eta-\cos(\eta\kappa)
   =\frac{\eta^2}{2}(1+\kappa^2)+O(\eta^4),
\]

and (2.5) yields

\[
 T_{\rm proj}(\eta\kappa,\eta)
 =4\eta^6\kappa^2(1+\kappa^2)^2+O(\eta^8)
 \longrightarrow0.                                          \tag{2.7}
\]

Thus the projected theorem and continuum LL make opposite predictions in the
*formal* overlap `eta->0`, `k->0`, `k/eta=kappa` fixed:

\[
 T_{\rm proj}\to0,\qquad T_{\rm LL}=1.                       \tag{2.8}
\]

This is a genuine mismatch, not an order-one convention or a missed factor.

### 2.3 What does, and does not, cross over

For the sharp Fano graph at fixed `epsilon=Delta-1`, its own soft
approximation has

\[
 k_* =\frac1{4\epsilon},\qquad
 T_{\rm proj}\simeq\frac1{1+(k_*/k)^2}.
                                                                    \tag{2.9}
\]

Consequently, in the deep-Ising regime where `epsilon>>1` and
`k_*<<1`,

\[
 k\ll k_*:\ T_{\rm proj}\simeq(k/k_*)^2\quad\hbox{(reflection)},
 \qquad
 k_*\ll k\ll1:\ T_{\rm proj}\simeq1\quad\hbox{(transmission)}.  \tag{2.10}
\]

This is the crossover already encoded in D16 (`definitions.md:676-680`) and
the Fano derivation (`theory/corner-b-draft.md:308-347`).  It is a
side-level-detuning crossover, not the continuum smooth-wall crossover:
`k_*` is not `1/xi_lat=eta`.  Indeed, for `epsilon->0`, (2.9) puts `k_*`
outside the Brillouin zone and (2.7) supplies no reflectionless window at
fixed `kappa=k xi_lat`.

[physical argument]  The expected two-parameter continuum organisation of
the **full**, unprojected chain is `T_full(kappa,eta)`, with
`lim_{eta->0}T_full(kappa,eta)=1` at fixed `kappa`, while lattice corrections
may still create an ultra-soft nonuniform region if the limits
`kappa->0` and `eta->0` fail to commute.  No theorem or local calculation in
the supplied corpus establishes that crossover or its scale, so it would be
wrong to draw it in.  The variable that a genuine calculation must hold fixed
is `kappa=k xi_lat=p lambda`; it does not reconcile (2.5) with (2.3).

The scope explains why (2.8) is not a contradiction between two valid
descriptions of the same XXZ limit.  Mq-E retains only one- and three-domain-
wall product configurations.  That projection is natural for the one-bond,
deep-Ising wall; its measured leakage is only small as `Delta` becomes large
and is already about `10%` at `Delta=2`
(`theory/corner-b-draft.md:349-355`).  In contrast, `eta->0` makes the dressed
wall broad and requires an unbounded number of those sharp-wall
configurations.  The projection is therefore singular exactly where LL
becomes controlled.  The statement in `theory/corner-b-draft.md:334-337` that
large-`Delta` transparency is a "lattice counterpart" of the reflectionless
continuum wall is at most a qualitative analogy: large `Delta` is the
opposite anisotropy limit.

**Sub-item (2) verdict: DOES NOT REDUCE.**  The PROVED M-tk soft-reflection
law belongs to a sharp, projected, deep-Ising channel.  The accepted
magnonics result belongs to the broad-wall LL scaling and is reflectionless
for every `p lambda`.  They disagree under the formal broad-wall scaling, and
the projection has no controlled full-chain lift there.  For the paper this
means that M-tk must not be advertised as a discretisation or derivation of
continuum magnon--Walker-wall transmission.  A separate full-chain
`Delta->1+` calculation, retaining the dressed kink sector, is required.

## 3. Displacement per transmitted magnon: the constants match

Take the D16 orientation, magnetisation `+M_0` on the left and `-M_0` on the
right, with

\[
 M_0=\frac{s}{a}                                             \tag{3.1}
\]

the spin angular momentum per unit length in `hbar=1` units.  Translating the
wall to the right by `dX` converts a segment of length `dX` from the right
vacuum to the left vacuum.  Its background angular momentum therefore changes
by

\[
 dS^z_{\rm wall}=2M_0\,dX.                                  \tag{3.2}
\]

[physical argument]  Equation (3.2) is the collective-coordinate evaluation
of the continuum background spin, with no assumption about the detailed wall
profile beyond its two saturated tails.

[physical argument]  A magnon on the `+z` domain lowers `S^z` by one quantum,
whereas the adiabatically transmitted magnon on the `-z` domain raises it by
one quantum.  Its change is consequently

\[
 \Delta S^z_{\rm mag}=+2
\]

per transmitted magnon.  This spin reversal and transfer of two quanta is the
standard magnonic spin-transfer-torque statement; the local continuum
literature states it explicitly at
`refs/arxiv-1406.6051/AF-wall-magnons.tex:37-43`.  The locally available
ferromagnetic model identifies the Berry coefficient as the spin density per
length at `refs/arxiv-1712.06578/QD-9.tex:69-79`.

Conservation of total `S^z` for `N_T` transmitted magnons gives

\[
 2M_0\Delta X+2N_T=0,
 \qquad
 \boxed{\Delta X=-\frac{N_T}{M_0}}.                           \tag{3.3}
\]

[physical argument]  For a coherent, small-amplitude incident spin wave of
unit-vector amplitude `rho`, the magnon line density is
`n_m=M_0 rho^2/2`: expanding `m_z=sqrt(1-rho^2)` loses `rho^2/2` of the
saturated spin density.  Its number flux is `n_m V_g`.  Dividing the angular-
momentum influx by (3.2) gives

\[
 V_{\rm DW}=-\frac{n_mV_g}{M_0}=-\frac{\rho^2}{2}V_g,          \tag{3.4}
\]

which is the Yan--Wang--Wang all-magnonic torque formula (PRL 107, 177207;
correct preprint arXiv:1106.4382).  Thus the packet displacement (3.3) and the
continuous-wave velocity (3.4) are the same conservation law.  The sign is
fixed: the wall moves toward the source for a magnon incident from the left.

The apparent factor-of-two trap is now explicit.  Transmission changes the
magnon's spin by **two**, but a unit wall displacement also changes the
background spin by **`2M_0`**.  The two factors cancel.  A formula
`-N_T/(2M_0)` would count the magnon flip while forgetting one of the two
vacuum densities (or conversely use the full vacuum jump as the definition of
`M_0`).

Convert the lattice theorem to physical units:

\[
 \delta x_{\rm phys}=a\,\delta x
 =-\frac{a}{s}\langle N_T\rangle
 =-\frac{\langle N_T\rangle}{M_0}.                            \tag{3.5}
\]

This is exactly (3.3), constants and sign included.  The corresponding
lattice charge equation is B3's
`2s delta x+(q_out-q_in)=0`, with
`(q_in,q_out)=(-1,+1)` on transmission
(`theory/corner-b-draft.md:526-548`).  The operator/expectation statement
`delta x=-<N_T>/s` is M-quant, whose status remains **PROVED conditional on
D18**, while M-flux alone is **PROVED**
(`theory/memory-quantization.md:6-31` and `268-345`).  Nothing in the
continuum comparison discharges D18 for the unprojected chain.

**Sub-item (3) verdict: REDUCES CLEANLY**, with one scope caveat: the
conservation arithmetic and normalisation reduce exactly, but the lattice
scattering-channel existence used to turn the arithmetic into an asymptotic
expectation remains conditional on D18.  If one additionally adopts the LL
reflectionless result, `N_T=N_in`; that additional transmission statement is
not supplied by M-tk, as Section 2 showed.

## 4. Fourier residue: exact for the response, not for the soft factor

### 4.1 The fixed-window residue identity

Use `Omega` for the Fourier frequency in this subsection, to distinguish it
from the magnon energy `omega(k)`.  At fixed finite window `W=[a,b]`, define

\[
 F_W(t)=\varrho_t(\mathfrak X_W).
\]

The PROVED M-flux identity (`claims/CLAIMS.md:61-63`, status unchanged) is

\[
 \dot F_W(t)=\frac1{2s}
 \left[\varrho_t(j_{a-1|a})-\varrho_t(j_{b|b+1})\right],       \tag{4.1}
\]

and hence, at finite endpoints,

\[
 F_W(t_f)-F_W(t_i)=\frac1{2s}
 \left[\widetilde j_{a-1|a}^{[t_i,t_f]}(0)
       -\widetilde j_{b|b+1}^{[t_i,t_f]}(0)\right].           \tag{4.2}
\]

This is proved by finite telescoping and the fundamental theorem of calculus,
with no scattering or falloff assumption
(`theory/memory-quantization.md:57-103`).

For the asymptotic residue statement, add the D13(b) hypothesis at every
`x in W`, `dot m_x in L^1(dt)`, and finite endpoint values.  Then
`dot F_W in L^1`, `F_W(t)->F_W^+/-`, and distributional Fourier calculus gives

\[
 \boxed{
 \delta x_W=F_W^+-F_W^-
 =\lim_{\Omega\to0}\widetilde{\dot F_W}(\Omega)
 =\lim_{\Omega\to0}[-i\Omega\widetilde F_W(\Omega)]
 =\frac{\widetilde j_L(0)-\widetilde j_R(0)}{2s}.}            \tag{4.3}
\]

The constant average of `F_W^+` and `F_W^-` produces a delta function at
`Omega=0`, which multiplication by `Omega` removes; their difference is the
`1/Omega` residue.  Equation (4.3) is the literal lattice image of
Strominger--Zhiboedov: their large-radius Fourier transform is at
`refs/arxiv-1411.5745/memory_4.tex:688-691`, the assumption of finite but
different retarded-time limits and the resulting pole-residue formula are at
`memory_4.tex:692-695`, and the subsequent soft-amplitude identification is at
`memory_4.tex:698-700`.

There is an important frequency distinction.  `Omega->0` in (4.3) is the DC
frequency of the **response/current history**.  It is not the `k->0` limit of
the D16 magnon energy: D16 is gapped and calls `k->0` soft only relative to
`omega_gap=J(Delta-1)` (`definitions.md:654-665`).  Equating these two limits
would be an extra, false step.

### 4.2 What supplies “finite but different limits” on the lattice

The continuum falloff assumption has three lattice versions of increasing
weakness:

1. **D13(b), pointwise/DC version.**  At fixed `x` and fixed `W`,
   `dot m_x in L^1(dt)` is the direct Abelian/Fourier hypothesis.  It is stated
   at `definitions.md:610-615`, including the mandatory order: thermodynamic
   limit first, then `Omega->0`, without sending `W` to infinity first.

2. **D18(AD3--AD4), scattering version.**  AD3 says that at every fixed
   window the free leg charge and non-bound dressing leave, leaving a local
   kink charge eigenstate; AD4 forms infinite-volume scattering first, then
   fixed-window time limits, then increases the window
   (`definitions.md:723-732`).  [physical argument]  This is the direct
   scattering analogue of a field settling to two stationary endpoint
   configurations.  It is precisely the local decay used by conditional
   M-quant.  D18 remains a hypothesis for the full XXZ chain; only the
   projected Mq-AD3 component is PROVED (`claims/CLAIMS.md:83-85`).

3. **D27(LR1--LR3), averaged local-relaxation version.**  LR1 gives common-
   sequence fixed-window Cesaro endpoint states and TPM laws; LR2 removes the
   first-moment measurement back-action; LR3 gives first-moment tightness as
   `W` grows (`definitions.md:1207-1248`).  The claim `LR1-GEN` is **PROVED**
   but promises only subsequential Cesaro convergence, explicitly not
   pointwise convergence (`claims/CLAIMS.md:93`).  `M-INDEX-spec` is
   **PROVED conditional** on D27(LR1--LR3); it does not prove LR2 or LR3, does
   not prove `H-AD-G => LR`, and gives a subsequential value unless D27's
   optional convenience clause is added (`claims/CLAIMS.md:89-90`).

The third version is enough for the ordered, averaged memory ledger
(`theory/memory-index.md:294-318` and `378-420`), but not by itself for the
ordinary pointwise Fourier pole in (4.3).  A Tauberian/Abelian upgrade from
Cesaro endpoints to pointwise limits or an explicitly averaged Fourier
prescription would still be required.  It is therefore inaccurate to say that
the corpus proves the asymptotic falloff assumption unconditionally.

### 4.3 The subleading-falloff warning and the observable dictionary

Hamada--Sugishita expand the pion as
`pi=pi^(1)/r+pi^(2)/r^2+...` at
`refs/arxiv-1709.05018/draft1004.tex:504-525`.  Because the soft pion theorem
has no leading `1/Omega` pole, its memory is not a shift of the leading
radiative coefficient: the field equation converts the integrated leading
coefficient into a jump of the **subleading** `pi^(2)` coefficient
(`draft1004.tex:679-702`), and the final relation is
`pi^(2)(u=infinity)=Delta_{S^2}Q^hard/4`
(`draft1004.tex:799-813`).

[physical argument]  The correct lattice dictionary is:

| Continuum falloff datum | Lattice datum | What happens |
|---|---|---|
| Leading vacuum/radiative datum (`pi^(1)` zero mode) | Tail densities and vacuum-pair label `(alpha,beta)` | Fixed: B3 preserves the vacuum-pair label at finite time; it is not the displacement memory (`theory/corner-b-draft.md:495-524`). |
| Subleading/dipole-like coefficient (`pi^(2)`) | Localised interface charge, equivalently the windowed wall coordinate `X_W` after asymptotic leg subtraction | May jump: `2s delta x+(q_out-q_in)=0`; this is D13(a), B3, and conditional M-quant. |
| Integrated hard flux/news | DC physical boundary-current difference | Exactly M-flux, (4.1)--(4.3). |
| Soft scattering coefficient | Soft-magnon scattering data such as `t(k)`/`T(k)` | Enters memory only through the transmitted channel weight `N_T`; it is not equal to the boundary-current residue. |

The “subleading” character is also visible in D13's own trap.  The unwindowed
first-moment coordinate D13(c), with all asymptotic legs included, is the
regularised total magnetisation and is exactly conserved, so its naive memory
is zero.  Only after subtracting the leg charge (D18), or geometrically
windowing it as D13(a), does one isolate the localised interface coefficient
that can retain memory (`definitions.md:617-626`).

This is where the warning bites the proposed soft/memory link.  The live claim
`M`—“`delta x` is the DC limit of the soft factor”—is **REFUTED**; the surviving
PROVED statement is M-flux, involving the physical boundary current, and soft
data affect the conditional memory through `N_T`
(`claims/CLAIMS.md:61-63`).  Therefore the lattice reproduces the
**Fourier-residue kinematics** of accepted memory, but it does not reproduce
the last Strominger--Zhiboedov equality between that residue and a leading
soft pole.  In the no-`1/k` magnon problem, the analogue must live one order
later—in the localised wall/charge coefficient—and no theorem in the supplied
inputs identifies it directly with a subleading soft amplitude.

**Sub-item (4) verdict: REDUCES WITH CAVEATS.**  The finite-window statement
“memory = DC boundary flux = endpoint Fourier residue” reduces exactly.
Its asymptotic reading requires D13(b) pointwise integrability or the named
D18 local-decay assumptions; D27 supplies only an averaged conditional
version unless strengthened.  Most importantly, “residue = soft-magnon
factor” does **not** follow and the literal claim is REFUTED.  The paper may
claim the accepted DC-memory structure, but not an established lattice
soft-factor/memory equivalence.

## 5. Consolidated verdict and consequence for the paper

| Sub-item | Verdict | Reason |
|---|---|---|
| (2) Transmission | **DOES NOT REDUCE** | The projected sharp-wall M-tk result has `T->0`; broad-wall LL has `T=1` at every `p lambda`.  They disagree at fixed `k/eta`, and the Mq-E projection is singular/uncontrolled there. |
| (3) Displacement | **REDUCES CLEANLY** | `2M_0 Delta X+2N_T=0` gives `Delta X=-N_T/M_0`; with `M_0=s/a` this is exactly `a delta x=-a N_T/s`.  D18 remains the stated lattice channel hypothesis. |
| (4) Fourier residue | **REDUCES WITH CAVEATS** | M-flux is exactly the DC boundary-current/endpoint-residue identity.  Pointwise asymptotics require D13(b) or D18; D27 is Cesaro/conditional.  The further identification with the soft-magnon factor is not proved and live claim M is REFUTED. |

The memory corner therefore has a clean continuum **conservation-law core**
but not a clean end-to-end continuum reduction.  The accepted magnonic result
is recovered by combining the reflectionless LL transmission law with the
charge ledger; the lattice corpus independently gets the same displacement
per *transmitted* magnon.  What fails is the attempt to use the proved
projected M-tk transmission probability as the lattice route to that accepted
LL process.

Status hygiene, unchanged throughout this report:

- **M-flux: PROVED** (finite-window physical-current DC identity).
- **B3: PROVED** with its stated D18-separated-event hypotheses; the raw
  half-line formula remains refuted.
- **M-quant: PROVED conditional on D18** for the full-chain channel reading.
- **Mq-E/Mq-AD3/M-tk: PROVED only on the projected incoming component** as
  stated in their rows; the unprojected M-tk lift is open.
- **M: REFUTED** for the literal identification of memory with the DC limit of
  the soft factor.

The safe paper claim is consequently narrow but substantive: the lattice
wall observable is a genuine memory observable because its permanent shift is
both an exact DC boundary-flux weight and, conditional on separated channels,
the same angular-momentum-transfer displacement accepted in magnonics.  The
paper must not claim that the projected soft-reflection formula reduces to
reflectionless continuum wall scattering, nor that a Strominger--Zhiboedov
soft-pole equality has been proved for the gapped lattice magnon.  Closing
either gap needs new work: a full dressed-kink `Delta->1+` scattering analysis
for the first, and a subleading soft-amplitude/local-wall-coefficient theorem
with the correct relaxation topology for the second.

