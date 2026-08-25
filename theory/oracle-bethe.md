# Exact Bethe oracle for the isotropic Heisenberg ferromagnet

This shard is self-contained modulo the canonical symbols and conventions in
[`notation.md`](../notation.md) and Definitions D6--D8 in
[`definitions.md`](../definitions.md). No literature result is quoted: every
formula follows from the bond permutation in D6. The coefficient ratio is
fixed by D7; this matters because its inverse is also called the S-matrix.

**THEOREM (Bethe oracle).**

**ASSUME.** D6--D8.

**PROVE.** Oracle facts O1--O10 in ⟨1⟩5.

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
Justification: the named bond-swap computation ⟨2⟩3.⟨3⟩2.

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
Justification: ⟨3⟩1 and ⟨2⟩4.

**⟨3⟩3. QED.**

**⟨2⟩4. PROVE.** At contact, `y=x+1`, the equation is

\[
(E-J)\psi(x,x+1)=-{J\over2}
 [\psi(x-1,x+1)+\psi(x,x+2)].                                   \tag{5}
\]

**⟨3⟩1.** The down-down bond is fixed by `P` and vanishes, while only
the two outer unequal-spin bonds act.
Justification: D6 and the bond-swap computation ⟨2⟩3.⟨3⟩2.

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
Justification: ⟨3⟩1 and (6).

**⟨3⟩3. QED.**

**⟨2⟩7. PROVE.** The rapidity cross-check fixes a convention mismatch:

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

**⟨3⟩4.** Thus the momentum fraction (6) and the quoted rapidity
fraction `(λ_1−λ_2−i)/(λ_1−λ_2+i)` are not the same coefficient ratio for
positive D7 rapidity: the latter is `S_{21}`. Treating them as literally equal
reverses every phase below.
Justification: (8).

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

**⟨3⟩2.** Substitute `f_r=t^{r-1}` in (10); eliminating `E` gives
`t=cos(K/2)`, and the boundary equation then gives (9).
Justification: algebra in (10).

**⟨3⟩3.** For `0<|K|<π`, `|t|<1`; equivalently
`k_1=K/2−iη`, `k_2=K/2+iη`, `e^{−η}=cos(K/2)`, and the denominator
of (6) vanishes, so this is the `S_{12}` pole selected by normalizability.
Justification: D7, (6), and direct substitution.

**⟨3⟩4.** At fixed `K`, the real scattering continuum begins at
`2J[1−cos(K/2)]`; its gap above (9) is `J[1−cos(K/2)]²`, closing only
as `K→0`.
Justification: minimize (4) at fixed total momentum and subtract (9).

**⟨3⟩5.** At `K=0`, `t→1` and the state ceases to be normalizable;
this is the bound-state threshold relevant to uniformity below.
Justification: ⟨3⟩2--⟨3⟩4 and the geometric-series norm criterion.

**⟨3⟩6. QED.**

**⟨2⟩9. QED.** The exact scattering and required bound-state sectors are
proved.

## ⟨1⟩3. The soft expansion

**⟨2⟩1. ASSUME.** Set `k_1=k_s`, `k_2=k_h` as in D8 and expand the D7
phase of `S_{12}`. The inverse convention is stated separately.
Justification: D7--D8.

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

**⟨3⟩3.** Thus the connected interaction `S_{12}−1`, not the identity
part, has the Dyson/Adler zero.
Justification: (11) and subtraction of the free S-matrix identity.

**⟨3⟩4. QED.**

**⟨2⟩3. PROVE.** Through second order in signed soft momentum,
\[
\boxed{\delta(k_s,k_h)=2k_s+\cot(k_h/2)k_s^2+O(k_s^3)},           \tag{12}
\]
\[
\boxed{S_{12}=1+2ik_s+[i\cot(k_h/2)-2]k_s^2+O(k_s^3)}.           \tag{13}
\]
**⟨3⟩1.** Differentiating the logarithm of (6) at zero, with
`a=e^{ik_h}`, gives
\[
\left.\partial_{k_s}\log S_{12}\right|_0=2i,\qquad
\left.\partial_{k_s}^2\log S_{12}\right|_0
=-2{1+a\over a-1}=2i\cot(k_h/2).                                \tag{14}
\]
Justification: quotient differentiation of (6) and
`(1+e^{ik})/(e^{ik}−1)=−i cot(k/2)`.

**⟨3⟩2.** Taylor's theorem for the D7 logarithm gives (12), and
exponentiating it, including `(2ik_s)²/2=−2k_s²`, gives (13).
Justification: D7, (11), (14), and the exponential power series.

**⟨3⟩3.** For the inverse convention in (8), `δ_{21}=−δ_{12}`; both
phase coefficients therefore change sign.
Justification: D7, ⟨2⟩6, and continuity at one.

**⟨3⟩4. QED.**

**⟨2⟩4. PROVE.** The linear phase coefficient is the hard-data-independent
constant `2`; the first hard invariant occurs quadratically:
\[
\boxed{\cot(k_h/2)={v_h\over\omega_h}
 ={2J-\omega_h\over v_h}
 =\sqrt{{2J-\omega_h\over\omega_h}}},\qquad 0<k_h<\pi.           \tag{15}
\]
**⟨3⟩1.** Equation (14) makes the `O(k_s)` coefficient identically `2`,
so neither `1/v_h` nor `ω_h/v_h²` occurs at that order.
Justification: (12)--(14).

**⟨3⟩2.** From (2), `v_h/ω_h=sin(k_h)/[1−cos(k_h)]=cot(k_h/2)`
and `v_h²=ω_h(2J−ω_h)`; positivity gives all forms in (15).
Justification: (2), half-angle identities, and D8.

**⟨3⟩3.** The natural invariant statement is: leading scattering length
`2`, followed by curvature `v_h/ω_h`. In contrast,
`ω_h/v_h²=1/(2J−ω_h)` and `1/v_h` are inequivalent candidates.
Justification: ⟨3⟩1--⟨3⟩2.

**⟨3⟩4. QED.**

**⟨2⟩5. PROVE.** Momentum is the regular coordinate; energy gives the
direction-labelled Puiseux expansion
\[
\boxed{\delta=2\sigma\sqrt{2\omega_s/J}
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

**⟨3⟩3.** Both signed momentum limits equal one and use one analytic
Taylor series, but energy forgets `σ`; the connected term is `O(√ω_s)`, not a
Taylor series in `ω_s`.
Justification: (11), (16), and (17).

**⟨3⟩4. QED.**

**⟨2⟩6. PROVE.** The fixed-hard expansion has the following endpoint and
bound-threshold qualifications.

**⟨3⟩1.** As `k_h→0`, the quadratic coefficient is `2/k_h+O(k_h)` and
higher coefficients also diverge; truncation requires `|k_s|≪k_h`.
Justification: (12), the cotangent series, and the rapidity difference (8).

**⟨3⟩2.** If `k_s,k_h→0` together away from `k_s=k_h`, then
`δ∼2k_sk_h/(k_h−k_s)`; at `k_s=k_h≠0`, (6) gives `S_{12}=−1`.
Justification: `λ(k)=1/k−k/12+O(k³)`, (8), and substitution in (6).

**⟨3⟩3.** Complex singularities obey `λ(k_s)−λ(k_h)=±i`; the
normalizable sign is the string pole of ⟨2⟩8. They approach zero precisely
when the bound state delocalizes at total momentum `K→0`.
Justification: (8) and ⟨2⟩8.⟨3⟩3--⟨2⟩8.⟨3⟩5.

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
