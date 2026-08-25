# Exact Bethe oracle for the isotropic Heisenberg ferromagnet

This shard is self-contained modulo the canonical symbols and conventions in
[`notation.md`](../notation.md) and Definitions D6--D8 in
[`definitions.md`](../definitions.md). Every formula follows from the bond
permutation in D6. Two local references are used only to audit the term
"scattering length"; no formula is imported from them. The coefficient ratio
is fixed by D7; this matters because its inverse is also called the S-matrix.

**THEOREM (Bethe oracle).**

**ASSUME.** D6--D8.

**PROVE.** Oracle facts O1--O10 in ⟨1⟩4.

## ⟨1⟩1. Setup and the exact one-magnon sector

**⟨2⟩1. ASSUME.** Work first on an `N`-site ring and then take the
infinite-volume generalized-state limit prescribed by D6.
Justification: D6.

**⟨2⟩2. PROVE.** The vacuum has exactly zero energy and every bond term is
positive semidefinite.

**⟨3⟩1.** For two spin halves,
`P_{x,x+1}=2 S_x·S_{x+1}+1/2`; hence

\[
h_{x,x+1}=-J(S_x\!\cdot S_{x+1}-1/4)
             ={J\over2}(1-P_{x,x+1}).
\]
Justification: direct Pauli-matrix algebra, equivalently comparison on the
triplet and singlet eigenspaces.

**⟨3⟩2.** Since a swap has eigenvalues `±1`, `h` has eigenvalues `0,J`
and is positive semidefinite.
Justification: ⟨3⟩1 and the spectral calculus of an involution `P²=1`.

**⟨3⟩3.** Every neighboring pair in `|Ω⟩` is `|↑↑⟩`, is fixed by
`P`, and is therefore annihilated by `h`; thus `H|Ω⟩=0`.
Justification: D6 and ⟨3⟩1.

**⟨3⟩4. QED.**

**⟨2⟩3. PROVE.** In the one-down-spin sector,

\[
H|x\rangle=J|x\rangle-{J\over2}
 (|x-1\rangle+|x+1\rangle).                                      \tag{1}
\]

**⟨3⟩1.** Bonds not incident on `x` contain equal spins and vanish.
Justification: D6 and ⟨3⟩1 of ⟨2⟩2.

**⟨3⟩2.** On either incident bond,
`(J/2)(1−P)|↓↑⟩=(J/2)(|↓↑⟩−|↑↓⟩)`.
Justification: the definition of the swap in D6.

**⟨3⟩3.** Adding the left and right incident-bond actions gives (1).
Justification: ⟨3⟩1--⟨3⟩2 and linearity.

**⟨3⟩4. QED.**

**⟨2⟩4. PROVE.** The D6 momentum states are exact eigenstates with

\[
\boxed{\omega(k)=J(1-\cos k)},\qquad
\boxed{v(k)={d\omega\over dk}=J\sin k}.                           \tag{2}
\]

**⟨3⟩1.** Insert the Fourier sum `|k⟩_N` into (1); the coefficient of
`|x⟩` is `J−(J/2)(e^{ik}+e^{-ik})=J(1−cos k)`.
Justification: ⟨2⟩3, an index shift in a periodic sum, and the cosine
exponential identity.

**⟨3⟩2.** Differentiate the energy with respect to lattice momentum.
Justification: the definition of `v` in D6 and elementary differentiation.

**⟨3⟩3. QED.**

**⟨2⟩5. QED.** Setup and one-magnon dispersion are proved.

## ⟨1⟩2. Exact two-magnon coordinate Bethe ansatz

**⟨2⟩1. ASSUME.** Use the ordered chamber and coefficient convention D7,
with real distinct momenta unless a bound-state continuation is stated.
Justification: D7.

**⟨2⟩2. PROVE.** Away from contact, `y>x+1`, the coordinate equation is

\[
E\psi(x,y)=2J\psi(x,y)-{J\over2}
 [\psi(x-1,y)+\psi(x+1,y)+\psi(x,y-1)+\psi(x,y+1)].               \tag{3}
\]

**⟨3⟩1.** Four unequal-spin boundary bonds surround two separated down
spins; each gives the diagonal and exchanged terms used in (1).
Justification: the bond-swap computation ⟨1⟩1.⟨2⟩3.⟨3⟩2.

**⟨3⟩2.** Summing the four bond actions gives (3).
Justification: ⟨3⟩1 and linearity.

**⟨3⟩3. QED.**

**⟨2⟩3. PROVE.** The scattering energy is additive:

\[
\boxed{E(k_1,k_2)=\omega(k_1)+\omega(k_2)
 =J(2-\cos k_1-\cos k_2)}.                                      \tag{4}
\]

**⟨3⟩1.** Substitute either plane wave in D7 into (3); each shift
multiplies it by `e^{±ik_1}` or `e^{±ik_2}`.
Justification: D7 and direct substitution.

**⟨3⟩2.** Collecting the shifts gives (4), using (2).
Justification: ⟨3⟩1 and ⟨1⟩1.⟨2⟩4.

**⟨3⟩3. QED.**

**⟨2⟩4. PROVE.** At contact, `y=x+1`, the equation is

\[
(E-J)\psi(x,x+1)=-{J\over2}
 [\psi(x-1,x+1)+\psi(x,x+2)].                                   \tag{5}
\]

**⟨3⟩1.** The down-down bond is fixed by `P` and vanishes, while only
the two outer unequal-spin bonds act.
Justification: D6 and the bond-swap computation ⟨1⟩1.⟨2⟩3.⟨3⟩2.

**⟨3⟩2.** Adding those two actions and moving the diagonal term gives
(5).
Justification: ⟨3⟩1 and algebra.

**⟨3⟩3. QED.**

**⟨2⟩5. PROVE.** The exact D7 coefficient ratio is

\[
\boxed{S_{12}(k_1,k_2)=-{e^{i(k_1+k_2)}-2e^{ik_1}+1
 \over e^{i(k_1+k_2)}-2e^{ik_2}+1}}.                             \tag{6}
\]

**⟨3⟩1.** Substitute the D7 wave and (4) into (5), cancel
`(e^{i(k_1+k_2)})^x`, and obtain

\[
(2z_2-z_1z_2-1)A_{12}+(2z_1-z_1z_2-1)A_{21}=0.                  \tag{7}
\]
Justification: direct collection of the two Bethe coefficients.

**⟨3⟩2.** Solving (7) for `A_{12}/A_{21}` gives (6).
Justification: D7 and one linear algebraic rearrangement.

**⟨3⟩3.** If `v(k_2)>v(k_1)` and the `k_2` packet starts on the left,
the `A_{21}` term is incoming and the `A_{12}` term outgoing, so (6) is the
out/in amplitude under D7.
Justification: D7 and ballistic motion with velocities (2).

**⟨3⟩4. QED.**

**⟨2⟩6. PROVE.** For real momenta, (6) is unitary and exchanging the
momenta inverts it.

**⟨3⟩1.** If `|z_1|=|z_2|=1`, the denominator in (6) equals `z_1z_2`
times the complex conjugate of its numerator.
Justification: multiply the conjugated numerator by `z_1z_2`.

**⟨3⟩2.** Therefore `|S_{12}|=1`, and direct exchange of `z_1,z_2` in
(6) gives `S_{12}(k_2,k_1)=S_{12}(k_1,k_2)^{-1}`.
The numerator can vanish for real momenta only at the excluded point
`k_1=k_2=0`; there (6) is `0/0`.
Justification: ⟨3⟩1, (6), and `|z_1|=|z_2|=1`.

**⟨3⟩3. QED.**

**⟨2⟩7. PROVE.** The rapidity form and its inverse are

\[
\boxed{S_{12}={\lambda_1-\lambda_2+i\over\lambda_1-\lambda_2-i}},
\qquad
\boxed{S_{21}=S_{12}^{-1}
 ={\lambda_1-\lambda_2-i\over\lambda_1-\lambda_2+i}}.           \tag{8}
\]

**⟨3⟩1.** D7 implies `z=(λ+i/2)/(λ−i/2)` by solving
`λ=(i/2)(z+1)/(z−1)` for `z`.
Justification: the exponential half-angle identity and algebra.

**⟨3⟩2.** Substitution in the numerator and denominator of (6) gives

\[
z_1z_2-2z_1+1={4i(\lambda_1-\lambda_2+i)\over
 (2\lambda_1-i)(2\lambda_2-i)},\quad
z_1z_2-2z_2+1={-4i(\lambda_1-\lambda_2-i)\over
 (2\lambda_1-i)(2\lambda_2-i)}.
\]
Justification: common-denominator algebra.

**⟨3⟩3.** Equations (6) and ⟨3⟩2 give the first fraction in (8);
D7 gives the inverse fraction.
Justification: (6), D7, and cancellation.

**⟨3⟩4.** Thus (8)'s first fraction is the D7 ratio. A source using
`λ↦−λ`, or using the reversed channel, may display the inverse fraction;
the distinction is algebraic and does not depend on the sign of `λ`.
Justification: (8) and the definitions of `S_{12},S_{21}` in D7.

**⟨3⟩5. QED.**

**⟨2⟩8. PROVE.** The bound-state information needed for the soft domain is

\[
f_r=t^{r-1},\qquad t=\cos(K/2),\qquad
\boxed{E_b(K)=J\sin^2(K/2)}.                                    \tag{9}
\]

**⟨3⟩1.** Inserting `ψ=e^{iK(x+y)/2}f_r` into (3) and (5) gives

\[
Ef_r=2Jf_r-J\cos(K/2)(f_{r-1}+f_{r+1})\ (r\ge2),\qquad
Ef_1=Jf_1-J\cos(K/2)f_2.                                       \tag{10}
\]
Justification: pair the center-of-mass phases `e^{±iK/2}` in (3)--(5).

**⟨3⟩2.** Take the representative `K∈[−π,π]` modulo `2π` and put
`c=cos(K/2)`. For `0<|K|<π`, the bulk equation has characteristic
polynomial
`Jc t²−(2J−E)t+Jc`; its two roots have product one. Any nonzero
`ℓ²(ℕ)` solution therefore has only the unique root with `|t|<1`, so it is
`f_r=Ct^{r−1}` up to normalization.
Justification: the standard solution of a constant-coefficient second-order
recursion; roots on the unit circle, including a repeated root, give no
nonzero square-summable sequence.

**⟨3⟩3.** Substitution of that necessary form in both equations (10)
fixes uniquely `t=c` and `E=J(1−c²)=J sin²(K/2)`. Conversely these values
satisfy (10), and `0<c<1`, proving existence and uniqueness up to scale.
Justification: eliminate `E` in (10), then use the geometric-series norm.

**⟨3⟩4.** At `|K|=π`, `c=t=0`; below the bulk level `2J`, (10) has
the unique solution `f_1≠0`, `f_{r≥2}=0`, with `E=J`, so the closed endpoint
in (9) is included.
For `0<|K|<π`, equivalently `k_1=K/2−iη`, `k_2=K/2+iη` and
`e^{−η}=c`; the denominator of (6) vanishes.
Justification: (10), D7, (6), and direct substitution.

**⟨3⟩5.** At fixed canonical `K`, write the real momenta as
`K/2±p`. Since `c≥0`, (4) is minimized at `cos p=1`; the continuum
edge is `2J(1−c)` and its gap above (9) is `J(1−c)²`.
Justification: (4), `K∈[−π,π]`, and subtraction of (9).

**⟨3⟩6.** At `K=0`, `t→1`, the geometric norm diverges, and the gap
closes. Other representatives modulo `2π` describe the same momentum, not
additional omitted bound-state families.
Justification: ⟨3⟩3--⟨3⟩5 and D6's Brillouin-zone convention.

**⟨3⟩7. QED.**

**⟨2⟩9. QED.** The exact scattering and required bound-state sectors are
proved.

## ⟨1⟩3. The soft expansion

**⟨2⟩1. ASSUME.** Set `k_1=k_s`, `k_2=k_h`. For the invariant statement
allow fixed `0<|k_h|<π` and sufficiently small `|k_s|`; set
`ω_h:=ω(k_h)`, `v_h:=v(k_h)`, `v_s:=v(k_s)`, `χ:=sgn(v_h−v_s)`, and
`S_phys:=S_{12}` if `χ=+1`, while
`S_phys:=S_{21}` if `χ=−1`. Let `δ_phys` be its continuous phase at
`k_s=0`. On D8's restricted domain, `χ=+1` and `S_phys=S_{12}`.
Justification: D7--D8 and the incoming/outgoing velocity ordering.

**⟨2⟩2. PROVE.** The soft magnon decouples:
\[
\boxed{\lim_{k_s\to0^+}S_{12}(k_s,k_h)
=\lim_{k_s\to0^-}S_{12}(k_s,k_h)=1}.                             \tag{11}
\]
**⟨3⟩1.** At `k_s=0`, the numerator of (6) is `e^{ik_h}−1` and the
denominator is `1−e^{ik_h}`.
Justification: substitution in (6).

**⟨3⟩2.** The outer minus sign makes their ratio one; the denominator is
nonzero for fixed `k_h∈(0,π)`.
Justification: ⟨3⟩1 and D8.

**⟨3⟩3.** Thus the mathematical soft-zero statement is simply
`S_{12}−1→0`; no named low-energy theorem is needed here.
Justification: (11) and subtraction of the identity amplitude.

**⟨3⟩4. QED.**

**⟨2⟩3. PROVE.** The exact local phase and physical soft expansion are
\[
 \delta_{12}=2\arctan{1\over\lambda(k_s)-\lambda(k_h)},
 \qquad (k_s\hbox{ near }0),                                  \tag{11a}
\]
\[
\boxed{\delta_{\rm phys}=2\chi k_s+{|v_h|\over\omega_h}k_s^2
 +R_\delta(k_s,k_h)},                                         \tag{12}
\]
\[
\boxed{S_{\rm phys}=1+2i\chi k_s+
 [i|v_h|/\omega_h-2]k_s^2+R_S(k_s,k_h)}.                       \tag{13}
\]
**⟨3⟩1.** With `Δλ=λ(k_s)−λ(k_h)`, (8) gives (11a) on the
branch tending to zero. Differentiating the logarithm of (6) at zero gives
\[
\left.\partial_{k_s}\log S_{12}\right|_0=2i,\qquad
\left.\partial_{k_s}^2\log S_{12}\right|_0
=-2{1+e^{ik_h}\over e^{ik_h}-1}=2i\cot(k_h/2).                 \tag{14}
\]
Justification: (8), quotient differentiation of (6), and
`(1+e^{ik})/(e^{ik}−1)=−i cot(k/2)`.

**⟨3⟩2.** For `k_h>0`, `S_phys=S_{12}` and (14) gives coefficients
`2` and `cot(k_h/2)=|v_h|/ω_h`. For `k_h<0`, the velocity order selects
`S_{21}=S_{12}^{−1}`, which negates both D7 phase coefficients; hence the
linear coefficient is `2χ` and the quadratic one is again `|v_h|/ω_h`.
Exponentiation gives (13), including `(2iχk_s)²/2=−2k_s²`.
Justification: D7, (2), (8), (14), and `χ=sgn(k_h)` near `k_s=0`.

**⟨3⟩3.** The remainders in (12)--(13) are uniform on stated compacta.
For `0<a<b<π`, set
`ε_{ab}:=(1/2)min{a,π−b,sin a,sin b}` and
`D_{ab}:={(q,h): |q|≤ε_{ab}, a≤|h|≤b}`. Define
\[
C_\delta(a,b):={1\over6}\max_{D_{ab}}|\partial_q^3\delta_{\rm phys}|,
\qquad C_S(a,b):={1\over6}\max_{D_{ab}}|\partial_q^3S_{\rm phys}|.
\]
These finite, explicit constants give
`|R_δ|≤C_δ(a,b)|k_s|³` and
`|R_S|≤C_S(a,b)|k_s|³` throughout `D_{ab}`, and are `O(a^{−2})`
as `a↓0` with `b` fixed.
Justification: `ε_{ab}` fixes the velocity order and excludes the pole and
coincident-momentum locus. In (11a),
`1/Δλ=2sin(q/2)sin(h/2)/sin((h−q)/2)` and the last denominator has
absolute value at least `a/(2π)` on `D_{ab}`; three differentiations give the
`O(a^{−2})` bound. Taylor's theorem gives the displayed inequalities.

**⟨3⟩4. QED.**

**⟨2⟩4. PROVE.** The invariant quadratic coefficient and its D8
specialization are
\[
\boxed{{|v_h|\over\omega_h}={2J-\omega_h\over|v_h|}
 =\sqrt{{2J-\omega_h\over\omega_h}}},\quad 0<|k_h|<\pi;
\qquad {|v_h|\over\omega_h}=\cot(k_h/2)\quad\hbox{on D8}.       \tag{15}
\]
**⟨3⟩1.** The physical linear coefficient is `2χ`, not an invariant
hard-independent `2`. Its magnitude is the two-site Wigner phase-slope, or
spatial-displacement, coefficient of the soft packet. Only D8 fixes `χ=+1`.
Justification: (12) and D7's physical channel convention.

**⟨3⟩2.** From (2), `v_h²=ω_h(2J−ω_h)`; positivity gives the
first three forms in (15). On D8, `v_h>0` and the half-angle identity gives
`v_h/ω_h=cot(k_h/2)`.
Justification: (2), half-angle identities, and D8.

**⟨3⟩3.** The number `2` is not a scattering length. In the joint soft
limit `k_1=εx`, `k_2=εy`, `x≠y`, (11a) gives
`δ_{12}/ε→2xy/(y−x)`: the phase vanishes but is not a constant times
`k_1−k_2`. Thus no nonzero relative-momentum scattering length exists; in
the massless-EFT convention it is reported as zero, with an ill-definedness
caveat. This reconciles the definition in
[`arxiv-1312.6793`, line 102](../refs/arxiv-1312.6793/scatteringpaper.tex)
with the ferromagnet statement in
[`arxiv-1602.08692`, line 656](../refs/arxiv-1602.08692/spinwave.arXiv.final.tex).
No numerical comparison with the spin-1 antiferromagnet is implied.
Justification: (11a), `λ(k)=1/k−k/12+O(k³)`, and the cited terminology
audit.

**⟨3⟩4.** Parity reverses both velocities and swaps the physical channel,
so `δ_phys(−k_s,−k_h)=δ_phys(k_s,k_h)`.
Justification: (6), ⟨1⟩2.⟨2⟩6, and the definition in ⟨2⟩1.

**⟨3⟩5. QED.**

**⟨2⟩5. PROVE.** Momentum is the regular coordinate; energy gives the
direction-labelled D8 Puiseux expansion
\[
\boxed{\delta_{12}=2\sigma\sqrt{2\omega_s/J}
 +{2v_h\over J\omega_h}\omega_s+O(\omega_s^{3/2})},             \tag{16}
\]
\[
\boxed{S_{12}=1+2i\sigma\sqrt{2\omega_s/J}
 +[-4+2iv_h/\omega_h]{\omega_s\over J}+O(\omega_s^{3/2})}.       \tag{17}
\]
**⟨3⟩1.** Equation (2) gives
`ω_s=J(k_s²/2−k_s⁴/24+⋯)` and
`k_s=σ sqrt(2ω_s/J)+O(ω_s^{3/2})`.
Justification: cosine Taylor series, D8, and series inversion.

**⟨3⟩2.** Substitution in (12)--(13), using (15), gives (16)--(17).
Justification: ⟨3⟩1, algebra, and power counting.

**⟨3⟩3.** These remainders also have explicit compact bounds. For
`a≤k_h≤b` and `0<ω≤Ω_{ab}:=J(1−cos ε_{ab})`, put
`k_σ(ω):=σ arccos(1−ω/J)` and let `δ_2,S_2` denote the displayed
two-term expressions in (16),(17). Define
\[
D_\delta(a,b):=\max_{\substack{a\le h\le b,\ \sigma=\pm1\\
0\le\omega\le\Omega_{ab}}}{|\delta_{12}(k_\sigma(\omega),h)-\delta_2|\over
\omega^{3/2}},\quad
D_S(a,b):=\max_{\substack{a\le h\le b,\ \sigma=\pm1\\
0\le\omega\le\Omega_{ab}}}{|S_{12}(k_\sigma(\omega),h)-S_2|\over
\omega^{3/2}},
\]
where each quotient at `ω=0` means its continuous extension. Both maxima are
finite, and the remainders in (16),(17) are bounded respectively by
`D_δ(a,b)ω_s^{3/2}` and `D_S(a,b)ω_s^{3/2}` on this compactum.
Justification: ⟨3⟩1, the bounds in ⟨2⟩3.⟨3⟩3, and continuity of the
normalized remainders at zero.

**⟨3⟩4.** Both signed momentum limits equal one, but energy forgets
`σ`; the connected term is `O(√ω_s)`, not a Taylor series in `ω_s`.
Justification: (11), (16), and (17).

**⟨3⟩5. QED.**

**⟨2⟩6. PROVE.** The fixed-hard expansion has the following endpoint and
bound-threshold qualifications.

**⟨3⟩1.** As `k_h→0^+` in D8, the quadratic coefficient is
`2/k_h+O(k_h)` and
higher coefficients also diverge; truncation requires `|k_s|≪k_h`.
Justification: (12), the cotangent series, and the rapidity difference (8).

**⟨3⟩2.** If `k_s,k_h→0` together away from `k_s=k_h`, then
`δ∼2k_sk_h/(k_h−k_s)`; at `k_s=k_h≠0`, (6) gives `S_{12}=−1`.
The associated Bethe vector is nevertheless identically zero because
`A_{12}=−A_{21}` multiplies two identical plane waves.
Justification: `λ(k)=1/k−k/12+O(k³)`, (8), (6), and D7.

**⟨3⟩3.** Complex singularities obey `λ(k_s)−λ(k_h)=±i`; the
normalizable sign is the string pole of ⟨1⟩2.⟨2⟩8. Quantitatively the
nearest complex `k_s` has `|k_s^{sing}|≍|k_h|` as `k_h→0`, which licenses
`|k_s|≪k_h`. The complex singular point is not itself the real bound state,
although both scales vanish at the `K→0` threshold.
Justification: (8), the inverse function for `λ`, and
⟨1⟩2.⟨2⟩8.⟨3⟩4--⟨1⟩2.⟨2⟩8.⟨3⟩6.

**⟨3⟩4.** As `k_h→π`, there is no analytic non-uniformity:
`v_h/ω_h→0`, and at `k_h=π` the nearest complex zero/pole is
`k_s=±i log 3`.
Justification: (15) and (6) with `e^{ik_h}=−1`.

**⟨3⟩5.** There is a kinematic non-uniformity in D7: `v_h→0`, so for
`k_s>0` the incoming condition `v_h>v_s` requires
`k_s≪sin k_h∼π−k_h`. The algebraic ratio (6) remains regular.
Justification: D7, (2), and ⟨3⟩4.

**⟨3⟩6. QED.**

**⟨2⟩7. QED.** The soft expansions, invariant content, and validity
domain are proved.

## ⟨1⟩4. Oracle facts O1--O10

| ID | Exact statement | Validity domain |
|---|---|---|
| **O1** | `ω(k)=J(1−cos k)`, `v(k)=J sin k`, equation (2). | One magnon; `k∈(−π,π]`, `J>0`. |
| **O2** | `E(k_1,k_2)=ω(k_1)+ω(k_2)`, equation (4). | Two real scattering momenta. |
| **O3** | `S_{12}` is the exact lattice-momentum fraction (6). | D7 ordering with distinct real momenta and nonzero denominator; at coincident nonzero momenta the formal ratio `−1` gives a null Bethe vector. |
| **O4** | `S_{12}=(Δλ+i)/(Δλ−i)`, `S_{21}=S_{12}^{−1}`, and locally `δ_{12}=2 arctan(1/Δλ)`, (8),(11a). | `λ=(1/2)cot(k/2)`; reversing the channel inverts the phase. |
| **O5** | There is a unique (up to scale) bound state: `t=cos(K/2)`, `E_b(K)=J sin²(K/2)`, (9). | Canonical `0<|K|≤π`; threshold at `K=0`; `|K|=π` included. |
| **O6** | `S_{12}(k_s,k_h)→1` from either sign, (11). | D8: fixed `k_h∈(0,π)`, signed `k_s→0`. |
| **O7** | `δ_phys=2 sgn(v_h−v_s)k_s+(|v_h|/ω_h)k_s²+R_δ`, (12). | `0<|k_h|<π`, physical D7 channel; `|R_δ|≤C_δ(a,b)|k_s|³` on `D_{ab}`; D7 kinematic proviso near `π`. |
| **O8** | `S_phys=1+2i sgn(v_h−v_s)k_s+[i|v_h|/ω_h−2]k_s²+R_S`, (13). | Same compacta as O7; `|R_S|≤C_S(a,b)|k_s|³`. |
| **O9** | The signed Wigner displacement coefficient is `2 sgn(v_h−v_s)`; its magnitude is two sites, not a scattering length; the curvature is the even invariant `|v_h|/ω_h`, (15). | D8 reduces the coefficients to `2` and `cot(k_h/2)=v_h/ω_h`; non-uniform at `k_h→0`, kinematically restricted at `k_h→π`. |
| **O10** | The D8 energy-coordinate series are (16)--(17), beginning `δ_{12}=2σ√(2ω_s/J)+O(ω_s)`. | On `a≤k_h≤b`, remainders are bounded by `D_δ(a,b)ω_s^{3/2}`, `D_S(a,b)ω_s^{3/2}`; `σ=sgn k_s`. |

**⟨2⟩1. PROVE.** O1--O5 are respectively (2), (4), (6), (8), and
(9); O6--O10 are respectively (11), (12), (13), (15), and (16)--(17).
Justification: the proved steps ⟨1⟩1--⟨1⟩3 and the domains stated there.

**⟨2⟩2. QED.** O1--O10, and hence the Bethe oracle theorem, are proved.
□

## Numerical record (non-deductive)

The standalone [`oracle_bethe_check.py`](checks/oracle_bethe_check.py)
assembles `(J/2)(1−P)` independently and covers numerical consequences of
O1--O10: rapidity orientation, periodic Bethe vectors, momentum-resolved bound
levels, the soft limit, both physical-phase signs and parity, (15), and both
Puiseux remainders. Bound-state uniqueness and the incoming/outgoing reading
remain the analytic arguments above, not numerical assumptions.

**Summary of a fresh normal and `python3 -O` run, 2026-08-25** — this block is
a hand-**aggregated summary**, not verbatim script output: the per-root `ED`
lines and the per-`K` `BOUND` lines are collapsed into their maxima, and the
header, the `RAPIDITY` line and `remainder_ratio` are omitted.  Every number
below is a correct maximum over a real passing run; for the verbatim transcript,
run the checker.  *(Amended at the 2026-08-26 freeze; `verdicts/oracle-bethe-r2.md`
residue 1.)*
```text
ONE residual=2.190e-15 velocity=4.694e-12
ED max_residual=2.585e-15 max_spectral=2.220e-15
BOUND max_energy_error=8.802e-13 max_projector_error=3.656e-15
SOFT limit=2.966e-16 linear=3.084e-10 quadratic=1.250e-09 invariant=4.441e-15 parity=1.735e-18
PUISEUX phase_ratio=2.545e+01 S_ratio=3.036e+01
PASS: oracle facts O1--O10
```
**Enforced tolerances, corrected.**  `BETHE_TOL = 2e−11` governs the `ONE`
residual, the (omitted) `RAPIDITY` errors, and `limit`, `invariant`, `parity`
on the `SOFT` line, as well as the `ED` and `BOUND` quantities; `1e−10` governs
the `ONE` velocity only; `DERIVATIVE_TOL = 3e−9` governs `linear` and
`quadratic` only; the omitted `remainder_ratio` is checked against a hardcoded
`1.0e2`; and `PUISSEUX_TOL = 4.0e1` governs both `PUISEUX` ratios.  The last two
are calibrated to the sampled set `k_h ∈ {0.37,1.10,2.40,3.00}`, `|k_s| ≤ 0.016`,
not derived from `C_δ(a,b)`/`D_δ(a,b)` (r2 residue 5).  Every failure path is
explicit and survives `-O`.
