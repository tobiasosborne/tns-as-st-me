# Soft-current reconnaissance for the Heisenberg ferromagnet

Status: prover reconnaissance for **S2**.  This shard uses D6--D8 and D10,
the exact identity in `corner-a-goldstone.md` ⟨1⟩6(e), and objection 18 of
`verdicts/corner-a-r1.md`.  It does not modify or assume the conclusions of
`oracle-bethe.md`: its boxed equations (1)--(17) are used only in ⟨1⟩5 as an
independent check.  Rigorous parts use the finite-ring/generalized-coordinate
register; the proposed scattering theorem is boxed as **EXPLORATION**.
The number `2` can be derived in M1 without the closed Bethe ratio: the local
contact/current equation has the Ward interpretation

\[
 \langle k_h|Q_0^\dagger J^-_0|k_h\rangle=2i\,v(k_h).
\]

Symmetry alone does not prove it.  The full current has an orthogonal contact
component; a general soft theorem still needs the lemmas in ⟨1⟩7.

## ⟨1⟩1. Register and assumptions

**ASSUME.** D6--D8.  On an `N`-site periodic ring, `N>3`, all displayed ring
momenta lie in `2πℤ/N`; `k_h≠0`, `k_h∈(0,π)`, and `k_s≠k_h`.  Write
`z_s=e^{ik_s}`, `z_h=e^{ik_h}`, and `K=k_s+k_h`.  Use the complexified broken
charge density `q_x=S_x^-`,

\[
 Q_k=\sum_xe^{ikx}S_x^-,\qquad
 j^-_{x,x+1}:=-[h_{x,x+1},S_x^-],\qquad
 J^-_k=\sum_xe^{ikx}j^-_{x,x+1}.
\]

This is the lowering combination of the two real broken directions used in
`corner-a-goldstone.md`; linearity extends D10 from anti-Hermitian real
generators to the complexified Lie algebra.

**⟨2⟩1. PROVE.** The exact current is

\[
 \boxed{j^-_{x,x+1}={J\over2}(S^-_{x+1}-S^-_x)P_{x,x+1}},       \tag{R1}
\]

and `[H,Q_k]=(z_s-1)J^-_k`.

**⟨3⟩1.** The swap intertwines one-site operators:
`P S_x^-=S_{x+1}^-P`; hence
`(J/2)[P,S_x^-]=(J/2)(S^-_{x+1}-S^-_x)P`.
Justification: D6 and direct action on the four two-spin basis vectors.

**⟨3⟩2.** Since `h=(J/2)(1-P)`, the expression in ⟨3⟩1 equals
`-[h,S_x^-]`; Abel summation gives the Fourier identity.
Justification: D10(a)--(c) and `corner-a-goldstone.md` ⟨1⟩6(e).

**⟨3⟩3. QED.**

## ⟨1⟩2. The state created by the broken charge

**⟨2⟩1. PROVE.** On the vacuum and a normalized hard magnon,

\[
 Q_{k_s}|\Omega\rangle=\sqrt N\,|k_s\rangle_N,                \tag{R2}
\]

\[
 \boxed{Q_{k_s}|k_h\rangle_N={1\over\sqrt N}\sum_{x<y}
 [e^{i(k_sx+k_hy)}+e^{i(k_hx+k_sy)}]|x,y\rangle.}              \tag{R3}
\]

For distinct ring momenta its squared norm is `N-2`.

**⟨3⟩1.** Equation (R2) is D6 after applying the Fourier sum.
Justification: `S_x^-|\Omega\rangle=|x\rangle`.

**⟨3⟩2.** In `Q_{k_s}|k_h\rangle`, terms with coincident lowering sites
vanish.  For every `x<y`, the added magnon can be at `x` or at `y`, giving
the two terms in (R3).
Justification: `(S_x^-)^2=0`, commutativity at distinct sites, and D6.

**⟨3⟩3.** The two diagonal norm contributions total `N-1`.  For
`k_s≠k_h`, Fourier orthogonality gives
`2 Re Σ_{x<y}e^{i(k_h-k_s)(x-y)}/N=-1`.
Justification: `Σ_{x,y}e^{i(k_h-k_s)(x-y)}=0`, with the `x=y` sum removed.

**⟨3⟩4. QED.**

### Exact coefficients in the two-magnon Bethe basis

For this computation only, let

\[
 F_N(a,b):=\sum_{0\le x<y<N}e^{i(ax+by)},\qquad
 G_N(t):=\sum_{y=1}^{N-1}e^{ity}.
\]

Then, with the value at `e^{ia}=1` understood by the finite sum,

\[
 F_N(a,b)={G_N(b)-G_N(a+b)\over1-e^{ia}}.                      \tag{R4}
\]

**⟨2⟩2. PROVE.** Let `|B\rangle` be any normalized D7 Bethe wave with
momenta `(k_1,k_2)`, coefficients `(A_{12},A_{21})`, and coordinate norm
`\mathcal N_B`.  Its exact coefficient in (R3) is

\[
\boxed{\begin{aligned}
c_B(k_s,k_h)={1\over\sqrt{N\mathcal N_B}}\{&
A_{12}^*[F_N(k_s-k_1^*,k_h-k_2^*)+F_N(k_h-k_1^*,k_s-k_2^*)]\\
&+A_{21}^*[F_N(k_s-k_2^*,k_h-k_1^*)+F_N(k_h-k_2^*,k_s-k_1^*)]\}.
\end{aligned}}                                                \tag{R5}
\]

Thus, for any complete orthonormal Bethe family `\mathscr B_K` containing
real scattering states, strings, and infinite-root descendants,

\[
 Q_{k_s}|k_h\rangle_N=\sum_{B\in\mathscr B_K}c_B|B\rangle.     \tag{R6}
\]

**⟨3⟩1.** Summing first over `x=0,…,y-1` gives (R4).
Justification: a finite geometric sum.

**⟨3⟩2.** Pairing the two conjugated Bethe plane waves with the two
source plane waves in (R3) gives the four terms of (R5).
Justification: D7, (R3), (R4), and the Hilbert-space inner product.

**⟨3⟩3.** Equation (R6) is Parseval expansion if the stated family is
complete.  Formula (R5) itself does not require completeness.
Justification: the finite-dimensional spectral theorem.  Identifying a
globally complete Bethe labelling, including exceptional roots, is ML2.

**⟨3⟩4.** At `k_s=0`, `[H,Q_0]=0` and

\[
 |B_{\infty,h}\rangle:={Q_0|k_h\rangle_N\over\sqrt{N-2}}       \tag{R7}
\]

is a single normalized eigenstate of energy `ω(k_h)`: the Bethe descendant
with one rapidity at infinity.  Hence the expansion collapses to
`Q_0|k_h\rangle_N=\sqrt{N-2}|B_{\infty,h}\rangle`.
Justification: (R3), its norm, and the global `SU(2)` commutator.

**⟨3⟩5. QED.**

### Exact mismatch with a scattering state

Let `|P_{12}\rangle=N^{-1/2}Σ_{x<y}e^{i(k_sx+k_hy)}|x,y\rangle`
and define `|P_{21}\rangle` by exchanging the momenta.  The incoming-normalized
D7 scattering wave is `|B^{in}\rangle=S_{12}|P_{12}\rangle+|P_{21}\rangle`.

**⟨2⟩3. PROVE.** Exactly in the ordered chamber,

\[
 \boxed{Q_{k_s}|k_h\rangle_N-|B^{in}\rangle
       =(1-S_{12})|P_{12}\rangle.}                             \tag{R8}
\]

**⟨3⟩1.** Equation (R3) has coefficient ratio `1`, while a scattering
eigenstate has D7 ratio `S_{12}`.
Justification: (R3) and D7.

**⟨3⟩2. QED.** The charge creates the root-infinity descendant at
zero momentum, but away from zero it is not an on-shell scattering state.

## ⟨1⟩3. Exact current form factors and the zero-current Ward reduction

Define the adjacent-pair contact vector

\[
 |C_K\rangle:=\sum_{x=0}^{N-1}e^{iKx}|x,x+1\rangle,            \tag{R9}
\]

with the pair across the periodic seam interpreted cyclically.

**⟨2⟩1. PROVE.** The current acting on a hard magnon is exactly

\[
\boxed{J^-_{k_s}|k_h\rangle_N=
 {\omega(k_s)\over z_s-1}Q_{k_s}|k_h\rangle_N
 +{J\over\sqrt N}(z_h-1)|C_K\rangle,}                          \tag{R10}
\]

where `ω(k_s)/(z_s-1)=(J/2)(z_s^{-1}-1)` and its value at zero is `0`.

**⟨3⟩1.** Away from `y=x+1`, the two terms in (R3) obey the free
two-magnon equation with energy `ω(k_s)+ω(k_h)`.
Justification: direct application of the four unequal-spin D6 swap bonds.

**⟨3⟩2.** At contact, direct application of `(J/2)(1-P)` gives

\[
 (H-\omega(k_h))Q_{k_s}|k_h\rangle_N
 =\omega(k_s)Q_{k_s}|k_h\rangle_N
 +{J\over\sqrt N}(z_s-1)(z_h-1)|C_K\rangle.                   \tag{R11}
\]

Justification: substitution of (R3); all non-contact terms cancel pairwise.

**⟨3⟩3.** Divide (R11) by `z_s-1` using
`(H-ω_h)Q_{k_s}|k_h\rangle=(z_s-1)J^-_{k_s}|k_h\rangle`.
The first coefficient follows from the one-magnon D6 bond calculation, also
independently rederived from the current in `corner-a-goldstone.md`.
Justification: (R1), D6, and the commutator identity.

**⟨3⟩4. QED.**

**⟨2⟩2. PROVE.** For every normalized two-magnon eigenvector
`|B_\alpha\rangle` of energy `E_\alpha` and total momentum `K`,

\[
\boxed{\langle B_\alpha|J^-_{k_s}|k_h\rangle
={E_\alpha-\omega_h\over z_s-1}c_\alpha
={\omega_s\over z_s-1}c_\alpha
 +{J(z_h-1)\over\sqrt N}d_\alpha,}                             \tag{R12}
\]

where `c_\alpha=⟨B_\alpha|Q_{k_s}|k_h⟩` and
`d_\alpha=⟨B_\alpha|C_K⟩`; for a matching D7 wave,
`d_B=N(A_{12}^*e^{-ik_2^*}+A_{21}^*e^{-ik_1^*})/\sqrt{\mathcal N_B}`.

**⟨3⟩1.** The first equality is the commutator between energy
eigenvectors; the second is (R10).
Justification: (R1), (R10), and the eigenvalue equations.

**⟨3⟩2. QED.**

**⟨2⟩3. PROVE.** The exact `k_s=0` statement is

\[
 J^-_0|k_h\rangle_N={J\over\sqrt N}(z_h-1)|C_{k_h}\rangle,    \tag{R13}
\]

\[
 \boxed{\langle k_h|Q_0^\dagger J^-_0|k_h\rangle_N
       =2iJ\sin k_h=2i\,v_h,}                                 \tag{R14}
\]

and, with `D_h=Q_0|k_h⟩_N`,

\[
 \boxed{P_{D_h}J^-_0|k_h\rangle_N
 ={2iv_h\over N-2}Q_0|k_h\rangle_N.}                          \tag{R15}
\]

The complementary vector `(1-P_{D_h})J^-_0|k_h⟩_N` is nonzero for generic
`k_h`; therefore **`J^-_0` is not equal to velocity times total charge**.

**⟨3⟩1.** Equation (R13) is (R10) at zero.  Contracting (R3) at
`k_s=0` with (R13) gives
`J(z_h-1)(1+z_h^{-1})=2iJ sin k_h`.
Justification: (R3), (R9), (R10), and Fourier orthogonality.

**⟨3⟩2.** Alternatively, `SU(2)` covariance gives
`[S^+_{tot},J^-_0]=2J^z_0`, while direct one-magnon evaluation gives
`⟨k_h|J^z_0|k_h⟩=i v_h`; also `S^+_{tot}|k_h⟩=0` for `k_h≠0`.
Justification: `[S^+,S^-]=2S^z`, invariance of `P`, and (R1) with `S^-`
replaced by `S^z`.

**⟨3⟩3.** Divide (R14) by `⟨D_h|D_h⟩=N-2` to obtain (R15).
The contact vector in (R13) is not proportional to (R3), proving the last
claim.
Justification: (R3), ⟨1⟩2.⟨2⟩1, and orthogonal projection.

**⟨3⟩4. QED.**

### Regular versus singular

**⟨2⟩4. PROVE (finite volume).** All normalized current matrix elements
are regular at `k_s=0`.  The pole displayed in the first form of (R12) is
removable off the descendant and indeterminate, not divergent, on it.

**⟨3⟩1.** The direct current is a finite sum of matrices analytic in
`e^{ik_s}`, so its finite-volume matrix elements are finite.
Justification: (R1).

**⟨3⟩2.** If `E_\alpha≠ω_h` at `k_s=0`, conservation of `Q_0`
implies `c_\alpha(0)=0`; for a differentiable eigenvector family this zero
cancels `(z_s-1)^{-1}`.  In the descendant channel, both energy difference
and denominator vanish and (R13)--(R15), not the quotient, give the limit.
Justification: `[H,Q_0]=0`, (R7), and (R12)--(R15).

**⟨3⟩3.** Singular objects remain in the generalized basis: the soft
rapidity tends to infinity, half-chamber overlaps contain delta/principal-
value distributions, and standard unnormalized Bethe norms can be singular.
These are basis/distribution singularities.  Their uniform cancellation after
wave-packet smearing is ML3, not a finite-volume theorem.
Justification: D3(a), D7, and (R4)--(R7).

**⟨3⟩4. QED.**

## ⟨1⟩4. Local current/contact derivation of O7--O9

**⟨2⟩1. ASSUME.** Use only that a real two-magnon scattering eigenwave
is a sum of the two free plane waves away from contact.  Normalize the incoming
coefficient `A_{21}=1`; write the unknown outgoing coefficient as `s(k_s,k_h)`.
No closed Bethe ratio or rapidity formula is inserted.

**⟨2⟩2. PROVE.** The contact bond imposes

\[
 (2z_h-z_sz_h-1)s+(2z_s-z_sz_h-1)=0.                           \tag{R16}
\]

**⟨3⟩1.** For general `(A_{12},A_{21})`, the coefficient of
`(H-E)ψ` at `|x,x+1⟩` is `-J(z_sz_h)^x/2` times the left side of
(R16).
Justification: apply the two outer swap bonds; the down-down bond vanishes.

**⟨3⟩2.** An eigenvector has zero contact residual, giving (R16).
For `s=1`, the residual is precisely the contact term of (R11); thus (R16)
is the on-shell cancellation of the current-created contact vector.
Justification: (R11) and ⟨3⟩1.

**⟨3⟩3. QED.**

**⟨2⟩3. PROVE.** For fixed `k_h∈(0,π)`, the solution analytic at
`k_s=0` obeys

\[
\boxed{s=1+2ik_s+[i\cot(k_h/2)-2]k_s^2+O(k_s^3),}              \tag{R17}
\]

\[
\boxed{\arg s=2k_s+\cot(k_h/2)k_s^2+O(k_s^3).}                \tag{R18}
\]

The remainder is uniform when `k_h` lies in a compact subset of `(0,π)`.

**⟨3⟩1.** Put `a=z_h` and
`s=1+s_1k_s+s_2k_s^2+O(k_s^3)`.  Since `a-1≠0`, (R16) has a unique analytic
solution near zero.
Justification: the analytic implicit-function theorem.

**⟨3⟩2.** The coefficient of `k_s` in (R16) is
`(a-1)s_1+2i(1-a)`, hence `s_1=2i`, with all hard dependence cancelling.
Justification: `z_s=1+ik_s-k_s^2/2+O(k_s^3)`.

**⟨3⟩3.** The coefficient of `k_s^2` gives
`s_2=-(3a-1)/(a-1)=i cot(k_h/2)-2`.
Justification: the same Taylor substitution and
`(1+a)/(a-1)=-i cot(k_h/2)`.

**⟨3⟩4.** Taking the continuous logarithm adds `2k_s^2` to the
quadratic coefficient of `s`, yielding (R18).  Compact hard support keeps
`|a-1|` bounded below and makes Taylor's remainder uniform.
Justification: `log(1+u)=u-u^2/2+O(u^3)` and compactness.

**⟨3⟩5. QED.**

**⟨2⟩4. PROVE (mechanism for `2`).** The charge source differs from the
on-shell state by the single ordered-branch factor (R8).  Contact cancellation
changes that branch by

\[
 S_{12}=e^{i\delta}=e^{2ik_s+O(k_s^2)}.                         \tag{R19}
\]

Thus its leading phase is the D6 Fourier phase of a two-site displacement
(the sign of an active spatial shift is convention-dependent).  Equivalently,
the non-Abelian current Ward residue is `2iv_h` by (R14); a hard external-pole
reduction would divide by the linear energy shift `v_h k_s`, cancelling the
hard velocity and leaving the root coefficient `2`.

**⟨3⟩1.** The exact mismatch is (R8), while (R17)--(R18) give (R19).
Justification: ⟨1⟩2.⟨2⟩3 and ⟨1⟩4.⟨2⟩3.

**⟨3⟩2.** The Ward residue is rigorously (R14), but the statement that
only this pole contributes to a general amplitude is ML4.
Justification: ⟨1⟩3.⟨2⟩3 and objection 18.

**⟨3⟩3. QED.** The `2` is derived for M1 local scattering, not from
the bare difference factor `(e^{ik_s}-1)` and not yet as an abstract theorem.

## ⟨1⟩5. Bethe-oracle and numerical verification

**⟨2⟩1. PROVE.** Equations (R17)--(R18) agree with frozen oracle facts
O7--O9 on D8's half-zone, including the D7 sign and the value `2` of the
linear coefficient there.
*(Reconciled at the 2026-08-26 freeze: O7/O9 were re-stated in oracle round r2
as `δ_phys = 2 sgn(v_h−v_s)k_s + (|v_h|/ω_h)k_s² + R_δ`, and the phrase
"hard-independent linear coefficient" was removed — the coefficient is
`2 sgn(v_h−v_s)`, which reduces to `2` **on D8**, where `sgn(v_h−v_s) = +1`.
`verdicts/oracle-bethe-r2.md` residue 4.  ⟨1⟩4.⟨2⟩3's own derivation is
unaffected: it works on D8 throughout and derives the cancellation of hard
dependence there.)*

**⟨3⟩1.** Compare (R17) with oracle equation (13) and (R18) with
oracle equation (12); the coefficients coincide term by term.
Justification: `oracle-bethe.md` O7--O9, used only after ⟨1⟩4.

**⟨3⟩2. QED.**

**⟨2⟩2. PROVE.** The independent checker
`checks/soft_current_recon_check.py` passes for `N=18`, including under
`python3 -O`.

**⟨3⟩1.** It assembles `H`, `Q_k`, `J^-_k`, and `J^z_0` directly;
checks (R3), (R5), (R8), (R10), all ED form factors (R12), and (R14)--(R18);
all failures call `SystemExit(1)` rather than `assert`.
Justification: inspection and the run recorded below.

Recorded maximum operator/form-factor residual: `1.560e-14`; quadratic-phase
fit error: `2.167e-10`; final status: `PASS`.

**⟨3⟩2. QED.**

## ⟨1⟩6. BOXED EXPLORATION -- draft Theorem S2

> **EXPLORATION: THEOREM S2 (conditional; M1, connected `1+soft -> 2`).**
>
> **ASSUME.** (i) The infinite D6 Hamiltonian has incoming/outgoing two-magnon
> wave operators in the real scattering channel, with D7 normalization and
> the bound state split off.  (ii) Hard momenta lie in a fixed compact interval
> `I⋐(0,π)` and signed `k_s→0` with `|k_s|<dist(I,{0,π})/2`.
> (iii) Plane waves occur only after smearing by `C_c^∞` packets.  (iv) The
> connected two-body amplitude is the multiplier
> `M_2(k_s,k_h):=[S_{12}(k_s,k_h)-1]M_1(k_h)` for
> `M_1∈L²(I)`; equivalently the one-particle scattering operator is the
> identity and the disconnected identity is subtracted.
>
> **PROVE.** With the universal leading soft factor
> `\mathsf S(k_s):=2ik_s`,
>
> \[
> \boxed{M_2(k_s,k_h)=\mathsf S(k_s)M_1(k_h)+R(k_s,k_h)},       \tag{S2}
> \]
>
> \[
> R=[i\cot(k_h/2)-2]k_s^2M_1+O_I(k_s^3)M_1,\qquad
> \|R(k_s,\cdot)\|_{L^2(I)}\le C_I|k_s|^2\|M_1\|_{L^2(I)}.
> \]
>
> Hence `||R||=o(|k_s|)` in hard-wave-packet norm, uniformly on `I`.  For a
> normalized rescaled soft packet `f_\epsilon(k)=ε^{-1/2}f(k/ε)`, the
> corresponding product-space remainder is `O(ε²)` in
> `L²(dk_s dk_h)`, while the leading term is `O(ε)`.
>
> **SCOPE.** This narrow theorem concerns the connected exact two-magnon
> scattering multiplier.  Extension to amplitudes generated by an arbitrary
> quasi-local hard process is not asserted without ML5.

The multiplier expansion and uniform estimate follow from ⟨1⟩4 once the
scattering construction in the assumptions is supplied.  Calling (S2) a
symmetry-derived soft theorem, rather than an exact two-body threshold
statement, additionally requires ML3--ML5.

## ⟨1⟩7. MISSING LEMMAS

**ML1 -- two-magnon wave operators and channel norm (MEDIUM).**  Construct the
infinite-chain one- and two-magnon scattering spaces and prove existence and
isometry of the incoming/outgoing maps on packets supported away from equal
velocities and the endpoints.  *Plan:* fiber the two-body Hamiltonian by total
momentum; each relative-coordinate fiber is a half-line Jacobi operator with
one boundary defect.  Use its explicit spectral measure or Cook estimates,
then isolate the single bound eigenvalue.  This supplies the Hilbert-space
meaning of D7 waves without assuming Bethe completeness.

**ML2 -- complete charge-created Bethe resolution (MEDIUM).**  Prove that the
family used in (R6) contains every regular scattering root, the two-string,
and all `SU(2)` descendants, with no missing exceptional finite-ring vector.
*Plan:* diagonalize each total-momentum relative Jacobi matrix directly and
match its characteristic equation to the Bethe quantization condition;
obtain (R7) as the root-at-infinity limit.  Then apply the finite-dimensional
spectral theorem to (R5).  The main nuisance is exceptional/singular root
bookkeeping, not an analytic obstruction.

**ML3 -- uniform current-form-factor regularity (MEDIUM--HIGH).**  Upgrade the
finite-volume regularity after (R15) to a bound uniform in volume and in
`k_s→0` after wave-packet smearing.  *Plan:* insert (R10) into the spectral
resolution from ML1, bound contact evaluation in the relative Jacobi graph
norm, and separate the descendant projection before taking the limit.  This
must show that delta/principal-value pieces in (R5) are distributional
normalization effects and that no physical `1/k_s` current pole survives.

**ML4 -- Ward/LSZ external-leg reduction (HIGH).**  Show that the descendant
piece (R15), and only that piece, supplies the leading on-shell connected
amplitude, while the orthogonal contact vector contributes `O(k_s²)`.
*Plan:* perform a Feshbach decomposition of the two-body resolvent into the
root-infinity descendant and its orthogonal complement.  The pole denominator
is `ω(k_h+k_s)-ω(k_h)=v_hk_s+O(k_s²)`; combine it with (R14) and
`e^{ik_s}-1`.  A uniform reduced-resolvent bound on compact `I` should make the
orthogonal term subleading.  This is the load-bearing answer to objection 18.

**ML5 -- process-independent factorization (HIGH; possible counterexamples).**
Specify the class of quasi-local hard sources/processes for which their
one-hard amplitude `M_1` and hard-plus-soft amplitude `M_2` are related by the
same external-leg factor, with no source-dependent contact term at order
`k_s`.  *Plan:* impose `SU(2)` covariance and an LSZ-amputated locality bound,
commute the smeared broken charge through the source, and classify the contact
commutator.  A generic non-covariant source can add an independent soft
contact term, so hypotheses must exclude it or S2 in that generality is false.

**ML6 -- finite/infinite and bound-channel remainder (MEDIUM).**  Control the
order of `N→∞`, wave-packet width `→0`, and `k_s→0`, and prove that the bound
state and off-shell coefficients in (R5) do not contaminate the leading real
scattering channel.  *Plan:* use the fixed-hard separation between
`ω(k_h)` and the bound energy, spectral projections of the relative Jacobi
operator, and dominated convergence.  Non-uniformity as `k_h→0` is excluded
exactly as in D8/O7.

## ⟨1⟩8. Reconnaissance verdict

1. (R3), (R5), and (R7) give the exact charge-created state, its Bethe
   coefficients, and its zero-momentum infinite-root descendant.
2. Current form factors (R12) are finite in finite volume; (R15) is the
   descendant Ward reduction, but a nonzero orthogonal contact piece remains.
3. The mismatch (R8) and contact equation derive `2`, (R17)--(R19), without
   the closed Bethe solution.  Thus `2` is **FM-derived and Bethe-verified**;
   a process-independent soft theorem remains conditional on ML3--ML5.
