# R1: continuum reduction of the exact two-magnon soft theorem

## Conventions and scope

Write the lattice spacing as `\ell` (not `a`, because the exact lattice
formula already uses `a=1+z_1z_2`) and set

\[
 k_j=\ell p_j,\qquad z_j=e^{i\ell p_j},\qquad
 d:=p_2-p_1.
\]

The coefficient ratio is the D7/D8 physical out/in ratio on the half-zone.
The lattice inputs used below are the exact spin-half result
`S2-2body` (**PROVED**), its higher-spin generalization `S2-2body-S`
(**PROVED**), and the plain two-sided soft limit `OR2` (**PROVED**).  No
status is changed here.  Unless explicitly stated otherwise, the continuum
expansions keep real, nonzero, distinct `p_1,p_2` fixed as `\ell\to0`.

## 1. Naive continuum limit

### 1.1 Spin `1/2`

For `S=1/2`, use the exact rapidity representation from `S2-2body`,

\[
 S_{12}=\frac{\lambda_1-\lambda_2+i}
              {\lambda_1-\lambda_2-i},\qquad
 \lambda_j=\frac12\cot\frac{k_j}{2}.
\]

The fixed-physical-momentum expansion is

\[
 \lambda_j=\frac1{\ell p_j}-\frac{\ell p_j}{12}
             -\frac{\ell^3p_j^3}{720}+O(\ell^5),
\]

and hence

\[
 \Delta\lambda:=\lambda_1-\lambda_2
 =\frac{d}{\ell p_1p_2}+\frac{\ell d}{12}
   +O(\ell^3).
\]

Expanding the exact quotient gives

\[
 S_{12}=1+\frac{2i\ell p_1p_2}{d}
           -\frac{2\ell^2p_1^2p_2^2}{d^2}+O(\ell^3).
\tag{1.1}
\]

Thus

\[
 \boxed{\lim_{\ell\to0}S_{12}(\ell p_1,\ell p_2)=1}
\]

at fixed generic `p_1,p_2`.  This is exactly compatible with the weaker
plain soft-limit statement `OR2`; here it is obtained in a different,
simultaneous long-wavelength limit.

### 1.2 General site spin

To avoid the spacing collision, denote the two polynomials in
`S2-2body-S` by

\[
 \mathfrak a:=1+z_1z_2,\qquad \mathfrak b:=z_1+z_2,
 \qquad \mu=(2S-1)\mathfrak a+\mathfrak b .
\]

Starting from its exact regular-channel ratio

\[
 S_{12}=\frac{S\mathfrak a\mathfrak b-z_1\mu}
               {z_2\mu-S\mathfrak a\mathfrak b},
\tag{1.2}
\]

direct Taylor division at `z_j=e^{i\ell p_j}` yields

\[
 S_{12}=1+\frac{i\ell p_1p_2}{S d}
 -\frac{\ell^2p_1^2p_2^2}{2S^2d^2}+O(\ell^3),
\tag{1.3}
\]

or, for its continuous phase,

\[
 \log S_{12}=\frac{i\ell p_1p_2}{S d}+O(\ell^3).
\tag{1.4}
\]

Equation (1.3) reduces to (1.1) at `S=1/2`.  Therefore

\[
 \boxed{S_{12}\longrightarrow1\quad\text{for every fixed }S}
\tag{1.5}
\]

on the stated generic domain.  The first interaction correction is
proportional to the length `\ell/S`; it is irrelevant in this strict
continuum limit.  Interpreting (1.5) as Dyson's free long-wavelength magnon
limit is a [physical argument]: the exact two-body result proves the limit,
while the statement that it is the continuum manifestation of an irrelevant
interaction uses EFT power counting.

This conclusion is deliberately narrow.  It does not assert uniform
convergence near `p_1=p_2`, where every coefficient displayed in (1.3)
is singular, nor does it retain a finite dynamics scale if `J` is held fixed:
the lattice dispersion gives energies of order `J S\ell^2p^2`.  A finite
continuum effective mass requires the usual scaling `J\ell^2=O(1)`
[physical argument].

## 2. Commutation of limits and the crossover

### 2.1 A uniform low-momentum form

The singular coefficients in (1.3) can be resummed.  In the exact
real-momentum representation used to prove unitarity in `S2-2body-S`, let
`K=k_1+k_2` and `q=(k_1-k_2)/2`.  Expanding its numerator `n` gives

\[
 n=iS\ell d-\frac{\ell^2p_1p_2}{2}
   -\frac{i\ell^3d}{12}
       \bigl[2S(p_1^2+p_1p_2+p_2^2)-3p_1p_2\bigr]
   +O(\ell^4p^4),
\]

with `S_{12}=n/[-\overline n]`.  It follows that, uniformly through the
near-coincident crossover as long as `\ell|p_j|\ll1`,

\[
 S_{12}=\frac{d+i\,\ell p_1p_2/(2S)}
               {d-i\,\ell p_1p_2/(2S)}
          \left[1+O\!\left(\ell^2(p_1^2+p_2^2)\right)\right].
\tag{2.1}
\]

The controlling dimensionless variable is therefore

\[
 \boxed{X:=\frac{\ell p_1p_2}{2S(p_2-p_1)}}.
\tag{2.2}
\]

For `|X|\ll1`, (2.1) reproduces the free expansion (1.3).  For
`|X|=O(1)` the interaction phase is finite even though both lattice momenta
are small.  For `|X|\gg1`, approached from the regular domain,
`S_{12}\to-1`.  Thus the free continuum limit is not uniform in the layer

\[
 |p_2-p_1|\lesssim \frac{\ell|p_1p_2|}{2S}.
\tag{2.3}
\]

This is a near-equal-velocity threshold layer, not the fixed-hard-momentum
soft limit.  Identifying it as a threshold boundary layer is a [physical
argument]; equation (2.1) itself follows algebraically from the exact ratio.

### 2.2 The two literal limits

Put `F_\ell(p_s,p_h):=S_{12}(\ell p_s,\ell p_h)` with fixed nonzero
`p_h` and remain in D8's physical channel.  The exact soft theorem
`S2-2body-S` (and `OR2` at spin half) gives

\[
 \lim_{p_s\to0}F_\ell(p_s,p_h)=1
\]

for every sufficiently small nonzero `\ell`.  Section 1 gives

\[
 \lim_{\ell\to0}F_\ell(p_s,p_h)=1
\]

for fixed `p_s\ne p_h`.  Consequently

\[
 \boxed{
 \lim_{p_s\to0}\lim_{\ell\to0}F_\ell
 =\lim_{\ell\to0}\lim_{p_s\to0}F_\ell=1.}
\tag{2.4}
\]

There is **no non-commutation of the two amplitude values**.  Claiming one
would confuse a nonuniform derivative with a noncommuting pointwise limit.

### 2.3 What does not survive: the unrescaled physical first jet

The first jets do distinguish the lattice family from its strict continuum
limit.  On D8, `S2-2body-S` states

\[
 \left.\partial_{k_s}\delta_{\rm phys}\right|_{k_s=0}=\frac1S.
\]

Since `k_s=\ell p_s`, this becomes

\[
 \left.\partial_{p_s}\delta_{\rm phys}\right|_{p_s=0}
 =\frac{\ell}{S},\qquad
 \lim_{\ell\to0}\partial_{p_s}\delta_{\rm phys}=0,
\tag{2.5}
\]

whereas the cutoff-rescaled jet is

\[
 \boxed{
 \lim_{\ell\to0}\frac1\ell
 \left.\partial_{p_s}\delta_{\rm phys}\right|_{0}=\frac1S.}
\tag{2.6}
\]

Thus the number `1/S` is visible in the continuum EFT regime only as the
coefficient of the cutoff-suppressed term.  More explicitly, require

\[
 \ell|p_h|\ll1,\qquad |p_s|\ll|p_h|,
 \qquad |X|\ll1.
\]

Then (2.1) gives

\[
 \delta_{\rm phys}=\frac{\ell p_s}{S}
 +O\!\left(\frac{\ell p_s^2}{p_h}\right)
 =\frac{k_s}{S}+\cdots .
\tag{2.7}
\]

It is therefore an exact slope with respect to dimensionless lattice
momentum, but a length `\ell/S` with respect to physical momentum.  The
strict fixed-`p` continuum amplitude is free and has zero unrescaled first
jet.

## 3. EFT matching to the accepted continuum description

### 3.1 Schrödinger EFT and the lattice parameters

Normalize the continuum magnon field by
`[\psi(x),\psi^\dagger(y)]=\delta(x-y)` and
`\int dx\,\psi^\dagger\psi=N_{\rm mag}`.  Thus
`[\psi]=L^{-1/2}`.  Expanding the exact one-magnon dispersion from
`S2-2body-S`,

\[
 \omega(p)=2JS(1-\cos\ell p)
 =JS\ell^2p^2-\frac{JS\ell^4p^4}{12}+O(\ell^6p^6),
\]

fixes

\[
 \boxed{\frac1{2m_*}=JS\ell^2},
 \qquad \omega(p)=\frac{p^2}{2m_*}
 -\frac{\ell^2p^4}{24m_*}+\cdots .}
\tag{3.1}
\]

A convenient on-shell operator basis for the number-conserving EFT is

\[
\begin{aligned}
 \mathcal L={}&i\psi^\dagger\partial_t\psi
 -\frac{\partial_x\psi^\dagger\partial_x\psi}{2m_*}
 +\frac{\ell^2}{24m_*}
       \partial_x^2\psi^\dagger\partial_x^2\psi \\
 &-\frac{C_0}{2}\psi^{\dagger2}\psi^2
 -\frac{G}{4m_*}\left[
   \psi^{\dagger2}(\partial_x\psi)^2
  +(\partial_x\psi^\dagger)^2\psi^2\right]+\cdots .
\end{aligned}
\tag{3.2}
\]

Using a local Schrödinger field and organizing its operators by derivatives
is a [physical argument] (the EFT locality and derivative-expansion
assumption).  Once (3.2) is chosen, the matching below is algebraic.  The
normalization in (3.2) is fixed so that its on-shell two-body contact kernel
is

\[
 g_{\rm on}(p_1,p_2)=C_0-\frac{G}{m_*}p_1p_2+\cdots .
\tag{3.3}
\]

The exact fact that a zero-momentum magnon decouples (`S2-2body-S`) rules out
a nonderivative scattering term, while comparison with (2.1) fixes

\[
 \boxed{C_0=0,\qquad G=\frac{\ell}{2S}.}
\tag{3.4}
\]

The dimensions are

\[
 [m_*]=E^{-1}L^{-2},\qquad [C_0]=E L=\frac1{m_*L},
 \qquad [G]=L,\qquad
 \left[\frac{G}{m_*}\right]=E L^3.
\]

Different off-shell bases related by integrations by parts or field
redefinitions move strength among derivative operators [physical argument];
the on-shell number `G` in (3.3)--(3.4) is the matched invariant used here.

### 3.2 The 1d two-body `S`-matrix

In the two-body sector let `r=x_2-x_1>0`.  A contact interaction
`g_{\rm on}\delta(r)` imposes

\[
 \left.\partial_r\Psi\right|_{0^+}
 =\frac{m_*g_{\rm on}}2\Psi(0).
\tag{3.5}
\]

For

\[
 \Psi=A_{12}e^{ip_1x_1+ip_2x_2}
      +A_{21}e^{ip_2x_1+ip_1x_2},
\]

equations (3.3)--(3.5), with `C_0=0`, give

\[
 \boxed{S_{12}^{\rm EFT}:=\frac{A_{12}}{A_{21}}
 =\frac{d+iGp_1p_2}{d-iGp_1p_2}}
 =\frac{d+i\ell p_1p_2/(2S)}
        {d-i\ell p_1p_2/(2S)}.
\tag{3.6}
\]

This is the uniform leading expression (2.1), including the threshold
resummation.  Away from `d=0`, its expansion is

\[
 S_{12}^{\rm EFT}=1+\frac{i\ell p_1p_2}{Sd}
 -\frac{\ell^2p_1^2p_2^2}{2S^2d^2}
 -\frac{i\ell^3p_1^3p_2^3}{4S^3d^3}+O(\ell^4).
\tag{3.7}
\]

Direct expansion of the exact lattice ratio (1.2) one order farther gives

\[
\begin{aligned}
 S_{12}^{\rm lat}={}&1+\frac{i\ell p_1p_2}{Sd}
 -\frac{\ell^2p_1^2p_2^2}{2S^2d^2}\\
 &+\frac{i\ell^3p_1^2p_2^2
   \left[S(5S-3)d^2-3p_1p_2\right]}
 {12S^3d^3}+O(\ell^4).
\end{aligned}
\tag{3.8}
\]

Hence the LO EFT matches exactly at `O(\ell)` and at the `O(\ell^2)` term
required by elastic unitarity.  At `O(\ell^3)`, (3.7) already supplies the
`-3p_1p_2` part of (3.8); the remaining difference is

\[
 S_{12}^{\rm lat}-S_{12}^{\rm EFT}
 =\frac{i\ell^3(5S-3)p_1^2p_2^2}{12S^2d}+O(\ell^4).
\tag{3.9}
\]

It is an NLO effective-range correction, not an LO mismatch.  In the same
on-shell basis it is matched by

\[
 G_{\rm on}(p_1,p_2)=\frac{\ell}{2S}
 +\frac{\ell^3(5S-3)}{24S^2}p_1p_2+O(\ell^5p^4),
\tag{3.10}
\]

whose second coefficient has units `L^3`.  Substitution of (3.10) in (3.6)
reproduces (3.8) through `O(\ell^3)`.  This is the order-by-order EFT check;
operators beyond those displayed explicitly in (3.2) are needed at that
order.

### 3.3 Accepted current-conservation route to the soft zero

The accepted nonrelativistic derivation starts from the current one-Goldstone
matrix element

\[
 \langle\Omega|J^\mu(x)|\theta(\boldsymbol p)\rangle
 =e^{-ip\cdot x}\left[ip^\mu F_1+i\delta^{\mu0}F_2\right],
\]

and current conservation fixes its on-shell dispersion relation.  These are
quoted from `refs/arxiv-2201.01393/manuscript.tex:408-415`.  The current
matrix element between scattering states has the Goldstone pole

\[
 \langle\beta|J^\mu(0)|\alpha\rangle
 =\frac{i}{p^0-\omega(|\boldsymbol p|)}
 \langle\Omega|J^\mu(0)|\theta(\boldsymbol p)\rangle
 \langle\beta+\theta(\boldsymbol p)|\alpha\rangle+R^\mu(p),
\tag{3.11}
\]

quoted from `refs/arxiv-2201.01393/manuscript.tex:418-423`.  Conservation
cancels that pole exactly and leaves

\[
 \langle\beta+\theta(\boldsymbol p)|\alpha\rangle
 =\left.\frac{p^0R_0+p^rR_r}{\omega F_1+F_2}
 \right|_{p^0=\omega},
\tag{3.12}
\]

quoted from `refs/arxiv-2201.01393/manuscript.tex:423-432`.  The inference of
an Adler zero additionally assumes that `R^\mu` stays regular in the joint
on-shell and soft limit; the source explicitly says this is not automatic
from standard pole arguments (`refs/arxiv-2201.01393/manuscript.tex:433-439`).

For the matched EFT, the four-point on-shell kernel in a single-soft limit is

\[
 g_{\rm on}(p_s,p_h)
 =-\frac{G}{m_*}p_sp_h+O(p_s^2)=O(p_s),
\tag{3.13}
\]

and the relative velocity is
`v_h-v_s=(p_h-p_s)/m_*+O(\ell^2p^3)`.  The LSZ/flux conversion therefore
gives

\[
 S_{\rm phys}-1
 =\frac{2iG p_sp_h}{p_h-p_s}+O(G^2)
 =\frac{i\ell p_s}{S}+O(p_s^2),
\tag{3.14}
\]

in agreement with `S2-2body-S`.  Relating the contact kernel to the
current-remainder formula (3.12) uses the usual Schrödinger LSZ and regular
effective-range expansion and is a [physical argument].  Its conclusion is
the ordinary linear Adler zero, not an enhanced quadratic zero.

### 3.4 Where the factor `1/S` lives

Introduce the physical spin density

\[
 \rho_{\rm spin}:=\frac{S}{\ell},\qquad [\rho_{\rm spin}]=L^{-1}.
\]

Then the matched quantities carrying the lattice slope are

\[
 \boxed{G=\frac{1}{2\rho_{\rm spin}}=\frac{\ell}{2S}},
 \qquad
 a_{\rm soft}:=\left.\partial_{p_s}\delta_{\rm phys}\right|_0
 =2G=\frac1{\rho_{\rm spin}}=\frac{\ell}{S}.}
\tag{3.15}
\]

Both `G` and `a_{\rm soft}` have units of length.  The dimensionless lattice
number is `a_{\rm soft}/\ell=1/S`.  At fixed site spin, the strict
`\ell\to0` limit has `\rho_{\rm spin}\to\infty`, so these Wilson coefficients
vanish.  Therefore no nonzero `1/S` interaction survives in the strict free
continuum `S`-matrix.  What survives at finite cutoff is the physical
effective-range datum `1/\rho_{\rm spin}`; recovering `1/S` requires measuring
it in lattice-spacing units.  This qualification is forced by the matching,
not a convention.

## 4. Position relative to the type-`B` soft-scaling bound

The continuum soft exponent is defined by rescaling one external spatial
momentum, `p_i\mapsto\epsilon p_i`, and writing

\[
 A_n\propto\epsilon^{\sigma_i}\qquad(\epsilon\to0).
\tag{4.1}
\]

This definition and the ordinary Adler statement `\sigma_i\geq1` are quoted
from `refs/arxiv-2108.03189/main.tex:81-86`.  The nonrelativistic bound for a
type-`B_{2m}` mode with a generalized spatial polynomial shift of degree `n`
is

\[
 \boxed{\sigma\geq\min(2m,n+1),}
\tag{4.2}
\]

quoted from `refs/arxiv-2201.01393/manuscript.tex:483-491`; the meaning of
`n` and the corresponding constraint on the current remainder are given at
`refs/arxiv-2201.01393/manuscript.tex:446-468`.

For the quadratic ferromagnetic magnon, `m=1`.  The matched connected
two-body quantity is either the amputated kernel (3.13) or, equivalently at
fixed nonzero hard momentum, `S_{\rm phys}-1` in (3.14).  Both scale as one
power of `p_s`, so

\[
 \boxed{\sigma_{\rm ferro}=1.}
\tag{4.3}
\]

There is no hidden extra power from 1d flux normalization because the hard
relative velocity remains nonzero in this soft limit.

The classification is therefore:

- For the ordinary broken spin symmetry, corresponding to the constant
  shift (`n=0`), (4.2) reads `\sigma\geq1`.  The exact lattice slope and the
  matched EFT **saturate** this bound.

- If one adds the distinct hypothesis of a linear redundant spatial shift
  (`n=1`), (4.2) reads `\sigma\geq2`.  The Heisenberg ferromagnet result is
  **outside the scope** of that enhanced bound; it neither confirms nor
  saturates it.

This is also stated directly in the accepted continuum source: the
`\mathbb{C}P^1` NLSM describing ferromagnets has
`(\tau,\sigma)=(1/2,1)` and does not have an enhanced soft limit
(`refs/arxiv-2201.01393/manuscript.tex:1138-1145`), whereas the theories with
a linear redundant spatial shift obey `\sigma\ge2`
(`refs/arxiv-2201.01393/manuscript.tex:523-529`).  The same source again
identifies `\mathbb{C}P^1` with `\sigma=1` at
`refs/arxiv-2201.01393/manuscript.tex:1328-1336`.

Accordingly, interpreting the proved linear lattice slope as saturation of
the `n=1`, `\sigma=2` bound would be a mismatch of theories.  The accepted
comparison is the ordinary `\sigma=1` Adler zero of the ferromagnetic
`\mathbb{C}P^1` EFT.

## 5. Verdict

\[
 \boxed{\textbf{REDUCES WITH CAVEATS}}
\]

The reduction is genuine: `S2-2body-S` matches a local Schrödinger magnon EFT
with the lattice effective mass (3.1), zero nonderivative contact, and
derivative-contact length `G=\ell/(2S)`.  Its two-body `S`-matrix (3.6)
reproduces the exact lattice expansion through `O(\ell^2)`, and the
`O(\ell^3)` remainder has the form of a matched NLO effective-range
coefficient.  The accepted pole-cancellation/current-conservation argument
then gives the same ordinary linear Adler zero.

The caveats are substantive:

1. At fixed distinct physical momenta the strict continuum limit is free,
   `S_{12}\to1`.  The lattice's `1/S` is not a finite dimensionless continuum
   interaction; it is `a_{\rm soft}/\ell`, where the physical scattering
   length is `a_{\rm soft}=\ell/S=1/\rho_{\rm spin}` and vanishes at fixed
   site spin as `\ell\to0`.

2. The two amplitude limits commute.  What is nonuniform is the
   near-coincident-momentum layer (2.3), and what is lost is the cutoff-rescaled
   first jet.  The paper should not describe this as noncommutation of the
   pointwise soft and continuum limits.

3. The accepted ferromagnetic `\mathbb{C}P^1` theory has `\sigma=1`.
   Therefore the proved lattice slope saturates the ordinary `n=0` type-`B_2`
   Adler bound, but is outside the enhanced `n=1`, `\sigma\ge2` class.  Any
   framing that claims the linear two-magnon phase proves or saturates the
   enhanced `\sigma=2` theorem is incorrect.

Thus the appropriate paper-level statement is: the exact lattice theorem
has the correct accepted ferromagnetic EFT reduction, including its Wilson
coefficient and ordinary Adler scaling, while its dimensionless `1/S` slope
is a finite-cutoff first-jet datum rather than a nonzero strict-continuum
interaction.
