# ML2: complete two-magnon resolution

Status: **R1 MAJORS REPAIRED; L6 r2 critic pending**.  No literature result is used.
The proof starts from D6,
uses the D7 coefficient convention, and uses the local equations already proved
in `oracle-bethe.md` ⟨1⟩2.  In particular, it does not assume Bethe
completeness.  A formal zero Bethe vector is never counted as a state.

## ⟨1⟩1. The theorem

**THEOREM ML2 (finite ring and infinite chain).**

**ASSUME.** D6--D8, `J>0`, and, in finite volume, `N>3`.

**PROVE.**

1. On the `N`-site ring, every nonzero two-magnon Bethe vector is one of the
   real-pair, complex-pair, or descendant vectors classified in ⟨1⟩3.  For
   even `N` the singular completion supplies one further vector.  The
   coincident solutions listed in ⟨1⟩4 are zero vectors and supply none.
   The physical vectors number exactly `N(N-1)/2` and can be normalized to an
   orthonormal eigenbasis.
2. On the infinite chain, the two-magnon Hilbert space is the orthogonal sum
   of the D7 scattering representation and one bound-magnon band.  The
   eigenfunctions, energies, Plancherel measures, and resolution of the
   identity are (15)--(20).
3. Consequently the finite-volume expansion (R6) in
   `soft-current-recon.md`, with the singular class and coefficient separated
   as in (23)--(24), is unconditional; (R7) is its single-infinite-root
   descendant at `k_s=0`.

## ⟨1⟩2. Momentum fibers on the finite ring

**⟨2⟩1. ASSUME.** Put `N=2L+1` or `N=2L`.  Use the unique labels

\[
 {\cal M}_N=\{-L,\ldots,L\}\quad(N=2L+1),\qquad
 {\cal M}_N=\{-L+1,\ldots,L\}\quad(N=2L),                     \tag{1}
\]

and set `K_m=2πm/N`, `c_m=cos(K_m/2)≥0`, and `σ_m=(-1)^m`.
Justification: D6 and the chosen representatives of the ring momenta.

**⟨2⟩2. PROVE.** The total-momentum fiber has dimension

\[
 d_m=L\ (N=2L+1),\qquad
 d_m=L\ (N=2L,\ m\ \text{even}),\qquad
 d_m=L-1\ (N=2L,\ m\ \text{odd}),                              \tag{2}
\]

and `Σ_m d_m=N(N-1)/2`.

**⟨3⟩1.** For directed separation `1≤r<N`, define

\[
 \Phi_{m,r}=N^{-1/2}\sum_{x=0}^{N-1}
 e^{iK_m(x+r/2)}|\{x,x+r\}\rangle .                           \tag{3}
\]

Then `Φ_{m,N-r}=σ_m Φ_{m,r}`.  If `N=2L`, `Φ_{m,L}=0` for odd
`m`, while `||Φ_{m,L}||²=2` for even `m`; all other retained vectors have
norm one.
Justification: replace `x` by `x+r` in (3), use
`e^{iK_mN/2}=σ_m`, and count the two descriptions of an opposite pair.

**⟨3⟩2.** Thus the orthonormal relative bases are `Φ_{m,r}`, `1≤r≤L`,
for odd `N`; `Φ_{m,r}`, `1≤r<L`, for even `N` and odd `m`; and the
same list completed by `2^{-1/2}Φ_{m,L}` for even `N` and even `m`.
Justification: ⟨3⟩1 and Fourier orthogonality in `x`.

**⟨3⟩3.** Counting these bases gives (2), and summing gives
`N L=N(N-1)/2` for odd `N` and
`L·L+L(L-1)=N(N-1)/2` for even `N`.
Justification: (1)--(2) and arithmetic.

**⟨3⟩4. QED.**

**⟨2⟩3. PROVE.** In the bases of ⟨2⟩2, `H/J` is the real Jacobi matrix

\[
 h_m=\begin{pmatrix}
 1&-c_m&&\\[-2mm]
 -c_m&2&-c_m&\\
 &\ddots&\ddots&\ddots
 \end{pmatrix},                                                \tag{4}
\]

with the following right endpoint: for odd `N`, the last diagonal is
`2-σ_mc_m`; for even `N`, odd `m` has the displayed Dirichlet endpoint,
and even `m` has last diagonal `2` and last off-diagonal `-√2c_m`.

**⟨3⟩1.** At `r=1`, the contact equation is
`Ef_1=Jf_1-Jc_mf_2`; in the interior it is
`Ef_r=2Jf_r-Jc_m(f_{r-1}+f_{r+1})`.
Justification: `oracle-bethe.md` equations (10), derived there directly from
the D6 swaps.

**⟨3⟩2.** At the far endpoint insert `f_{N-r}=σ_mf_r`.  For the even,
even case, pass from the coefficient `f_L` to the normalized coordinate
`f_L/√2`.
Justification: (3) and ⟨2⟩2.

**⟨3⟩3.** These substitutions give (4) and its three endpoints.
Justification: ⟨3⟩1--⟨3⟩2.

**⟨3⟩4. QED.**

## ⟨1⟩3. Every nondegenerate Bethe root and the exact count

**⟨2⟩1. ASSUME.** In this step `c=c_m>0`.  Define polynomials

\[
 F_0(X)=1,\quad F_1(X)=c,\quad
 F_{r+1}(X)=2X F_r(X)-F_{r-1}(X),                              \tag{5}
\]

and

\[
 P_m(X)=\begin{cases}
 F_{L+1}(X)-σ_mF_L(X),&N=2L+1,\\
 F_L(X),&N=2L,\ m\ \text{odd},\\
 F_{L+1}(X)-F_{L-1}(X),&N=2L,\ m\ \text{even}.
 \end{cases}                                                   \tag{6}
\]
Justification: definitions local to this proof.

**⟨2⟩2. PROVE.** The `d_m` roots of `P_m` are real and simple, and the
map

\[
 X\longmapsto E=J(2-2cX),\qquad f_r=F_r(X)                    \tag{7}
\]

is a bijection from them to all eigenlines of `h_m`.

**⟨3⟩1.** The contact equation and the interior recurrence in ⟨1⟩2,
after (7), say precisely `f_0=1`, `f_1=c`, and (5).
Justification: substitute `E/J=2-2cX`; overall scale is immaterial and
`c>0` makes `f_1` nonzero.

**⟨3⟩2.** The three far boundary conditions are respectively
`f_{L+1}=σ_mf_L`, `f_L=0`, and `f_{L+1}=f_{L-1}`.  They are exactly (6).
Justification: ⟨1⟩2.⟨2⟩3.

**⟨3⟩3.** Matrix (4) is real symmetric and irreducible when `c>0`; hence
it has `d_m` simple real eigenvalues.  Equations (6)--(7) identify its
characteristic equation up to a nonzero constant.
Justification: the finite-dimensional spectral theorem and the elementary
Jacobi fact proved by forward recurrence: an eigenvector with first entry
zero has every entry zero.

**⟨3⟩4. QED.**

**⟨2⟩3. PROVE.** Modulo exchanging `k_1,k_2` and adding `2π`, every
noncoincident solution of the two Bethe equations is exactly one root in
⟨2⟩2.

**⟨3⟩1.** Multiplying the two equations
`e^{iNk_1}=S_{12}`, `e^{iNk_2}=S_{12}^{-1}` gives
`K=k_1+k_2=K_m`.  Write

\[
 k_1=K_m/2-q,\quad k_2=K_m/2+q,\quad X=\cos q.                 \tag{8}
\]
Justification: periodicity of the D7 wave and elementary algebra.

**⟨3⟩2.** With incoming coefficient one, the contact equation gives

\[
 S_{12}(K_m,q)={c-e^{-iq}\over e^{iq}-c},\qquad
 f_r=S_{12}e^{iqr}+e^{-iqr}.                                  \tag{9}
\]

This is exactly the D7 fraction (6) of `oracle-bethe.md` after (8).
Justification: impose `f_1=cf_0` and solve for `S_{12}`.

**⟨3⟩3.** The remaining periodic equation is the far boundary condition in
⟨2⟩2, hence `P_m(cos q)=0`; conversely that condition reconstructs both
Bethe equations.  The choices `q` and `-q` only exchange the roots.
Justification: (3), (6), and (8)--(9).

**⟨3⟩4. QED.**

**⟨2⟩4. PROVE.** Every root is either real scattering (`-1≤X≤1`) or a
normalizable finite-ring string (`X>1`); no root has `X<-1`.  There is at
most one string in a fiber.

**⟨3⟩1.** Applying `2|ab|≤|a|²+|b|²` to (4), and
`2√2|ab|≤|a|²+2|b|²` at its exceptional last edge, gives
`h_m≤(2+2c)1`.  Thus (7) gives `X≥-1`.
Justification: direct quadratic-form estimation of (4).

**⟨3⟩2.** Raise only the first diagonal of (4) from `1` to `2`.  The
resulting free finite path, with the same reflection endpoint, has spectrum
in `[2-2c,2+2c]` by the same quadratic-form estimate.  Restoring (4) is a
negative rank-one perturbation, so at most one eigenvalue lies below
`2-2c`.
Justification: the min--max principle for a rank-one perturbation.

**⟨3⟩3.** If `X>1`, choose `q=iη`, `η>0`, in (8).  The roots are the
conjugate pair `K_m/2∓iη`, and (9) is the two exponential branches required
by periodicity.  It tends to the D7 bound wave as `N→∞`.
Justification: (8)--(9) and `cos(iη)=cosh η>1`.

**⟨3⟩4. QED.**

**⟨2⟩5. PROVE.** The exact number of finite strings is

\[
 B_N=\#\{m\in{\cal M}_N:0<|K_m|<\pi,\quad
 [m\ \text{even}\ne0]\ \hbox{or}\
 [m\ \text{odd},\ N(1-c_m)>2]\}.                              \tag{10}
\]

There is no equality case for `N>3`.

**⟨3⟩1.** From (5), `F_r(1)=1-r(1-c)`.  Therefore

\[
 P_m(1)=\begin{cases}
 -(1-c),&N\ \text{odd},\ m\ \text{even},\\
 2-N(1-c),&N\ \text{odd},\ m\ \text{odd},\\
 1-(N/2)(1-c),&N\ \text{even},\ m\ \text{odd},\\
 -2(1-c),&N\ \text{even},\ m\ \text{even}.
 \end{cases}                                                   \tag{11}
\]
Justification: substitute the finite arithmetic sequence into (6).

**⟨3⟩2.** The leading coefficient of `P_m` is positive.  By ⟨2⟩4 there
is at most one root above one, so it exists exactly when `P_m(1)<0`.
Equation (11) is precisely (10); `m=0` has the threshold root `X=1`.
Justification: continuity, the sign as `X→+∞`, and ⟨2⟩4.

**⟨3⟩3.** Equality for odd `m` would give
`2c_m=2-4/N`.  The left side is an algebraic integer because it is
`z+z^{-1}` for a root of unity `z`; a rational algebraic integer is an
integer.  Hence `N` divides `4`.  For `N>3`, only `N=4` remains, and direct
substitution of its odd label gives `cos(π/4)≠1/2`.
Justification: the monic polynomial of a root of unity and rational-root
division of a monic integer polynomial.

**⟨3⟩4. QED.**

**⟨2⟩6. PROVE.** Each momentum fiber contains exactly one `SU(2)`
descendant.  For `K_m≠0` it is the Bethe pair `(0,K_m)`; at `K_0=0` it is
the double-infinite-root vector proportional to `(S^-_{tot})²|Ω⟩`.

**⟨3⟩1.** In (5), `X=c` gives `F_r(c)=cos(rK_m/2)` and satisfies every
far boundary condition.  Its energy is
`2J(1-c²)=ω(K_m)`, and (9) is the pair `(0,K_m)` with `S_{12}=1`.
Justification: the cosine recurrence, D6, and `oracle-bethe.md` (2), (6).

**⟨3⟩2.** At `m=0`, the constant coordinate vector has energy zero and is
the normalized vector `binom(N,2)^{-1/2}Σ_{x<y}|x,y⟩`.
Justification: every D6 swap fixes it and direct expansion of
`(S^-_{tot})²|Ω⟩`.

**⟨3⟩3.** Global `SU(2)` lowering commutes with `H`, proving the stated
multiplet interpretation and agreeing with (R7).
Justification: D6 is globally `SU(2)` invariant.

**⟨3⟩4. QED.**

## ⟨1⟩4. Singular, coincident, and degenerate roots

**⟨2⟩1. PROVE.** The formal coincident solutions do not represent states.

**⟨3⟩1.** If `k_1=k_2=k` and `e^{ik}≠1`, D7 gives `S_{12}=-1`; the
Bethe equations reduce to `e^{iNk}=-1`.  There are exactly `N` such formal
solutions, but their coordinate wave is identically zero.
Justification: direct substitution in D7 and (9).

**⟨3⟩2.** A derivative regularization could be physical only if the
corresponding `X=1` or `X=-1` solved (6).  Equation (11), the no-equality
argument in ⟨1⟩3, and
`F_r(-1)=(-1)^{r-1}[cr+r-1]` exclude every formal solution.  At `m=0`,
the formal solution is `k=π` for odd `N` and hence uses `X=-1`; the separate
`k_1=k_2=0` contact equation is instead `0=0` and was retained as the double
descendant.
Justification: (5)--(6), (11), and direct evaluation at `-1`.

**⟨3⟩3. QED.**

**⟨2⟩2. PROVE.** If `N=2L`, the `K=π` fiber consists of one singular
contact state and an explicitly resolved `E=2J` eigenspace.

**⟨3⟩1.** Here `c=0`, so (4) is diagonal.  The normalized contact state

\[
 |\chi_\pi\rangle=N^{-1/2}\sum_x(-1)^x|\{x,x+1\}\rangle       \tag{12}
\]

has energy `J`.  This is the singular completion labelled by the compactified
rapidity pair `{+i/2,-i/2}`, equivalently `z_1=∞,z_2=0`.  The unscaled D7
two-plane-wave formula is undefined there and is not counted as an ordinary
root; (12), obtained from the Jacobi fiber, is the physical definition.  It
exists only for even `N`, as its total momentum is `π`.
Justification: direct action of the two outer D6 swap bonds and ring
periodicity.

**⟨3⟩2.** All vectors orthogonal to the contact coordinate have energy
`2J`.  A nonzero D7 basis is obtained from

\[
 f_r=-{\sin((r-1)q)\over\sin q},\quad
 q=\begin{cases}
 (j+1/2)\pi/(L-1),&L\ \text{even},\ 0\le j\le L-2,\\
 j\pi/(L-1),&L\ \text{odd},\ 1\le j\le L-2.
 \end{cases}                                                   \tag{13}
\]

The `q=π/2` member is the `(0,π)` descendant.
Justification: set `c=0` in (5)--(6), use
`F_r=-sin((r-1)q)/sin q`, and use finite sine/cosine orthogonality.

**⟨3⟩3.** Thus this fiber has dimension `L` when `L` is even and `L-1`
when `L` is odd: one singular vector, one descendant, and respectively
`L-2` or `L-3` other degenerate real-pair vectors.
Justification: count (12)--(13), consistently with (2).

**⟨3⟩4. QED.**

**⟨2⟩3. PROVE.** The finite physical inventory is

\[
 \begin{array}{c|c}
 \text{class}&\text{number}\\ \hline
 SU(2)\text{ descendants}&N\\
 \text{finite strings}&B_N\\
 \text{singular contact state}&1\ (N\text{ even}),\ 0\ (N\text{ odd})\\
 \text{other real-pair states}&N(N-1)/2-N-B_N-\mathbf1_{2\mid N}.
 \end{array}                                                    \tag{14}
\]

The `N` coincident zero solutions of ⟨2⟩1 are not in (14).

**⟨3⟩1.** For `c>0`, distinct eigenvalues of each Hermitian Jacobi block
give orthogonal eigenvectors; distinct `m` are orthogonal translation
eigenspaces.  At `K=π`, (12)--(13) are an orthogonal basis.
Justification: ⟨1⟩2--⟨1⟩4 and finite Fourier orthogonality.

**⟨3⟩2.** Their count is (14), which sums to `N(N-1)/2`, the dimension in
⟨1⟩2.  Normalizing therefore gives a complete orthonormal eigenbasis.
Justification: the finite-dimensional spectral theorem.

**⟨3⟩3. QED.**

## ⟨1⟩5. Infinite-chain spectral resolution and measures

**⟨2⟩1. ASSUME.** Identify the chamber with `(x,r)∈Z×N`, `r=y-x`, and
define the unitary center Fourier transform

\[
 ({\cal U}\psi)(K,r)={1\over\sqrt{2\pi}}\sum_{x\in\mathbb Z}
 e^{-iK(x+r/2)}\psi(x,x+r),\qquad -\pi<K\le\pi .               \tag{15}
\]
Justification: D6 and the Fourier Plancherel theorem on `ℓ²(Z)`.

**⟨2⟩2. PROVE.** With `c=cos(K/2)`, the fiber is the half-line Jacobi
operator

\[
 (h_Kf)_1=Jf_1-Jcf_2,\qquad
 (h_Kf)_r=2Jf_r-Jc(f_{r-1}+f_{r+1})\quad(r\ge2).               \tag{16}
\]
Justification: the D6 bond computation in `oracle-bethe.md` (10) and (15).

**⟨2⟩3. PROVE.** The delta-normalized D7 scattering waves and normalized
bound fibers are

\[
 \Psi^{\rm sc}_{Kq}(x,x+r)={e^{iK(x+r/2)}\over2\pi}
 [S(K,q)e^{iqr}+e^{-iqr}],\quad 0<q<\pi,                       \tag{17}
\]

\[
 S(K,q)={c-e^{-iq}\over e^{iq}-c},\qquad
 E(K,q)=J(2-2c\cos q)=\omega(K/2-q)+\omega(K/2+q),             \tag{18}
\]

\[
 \Psi^{\rm b}_{K}(x,x+r)={e^{iK(x+r/2)}\over\sqrt{2\pi}}
 \sqrt{1-c^2}\,c^{r-1},\qquad E_b(K)=J(1-c^2)=J\sin^2(K/2).  \tag{19}
\]

The bound vector is present for almost every `K≠0`; at `K=0` it becomes the
nonnormalizable threshold resonance.

**⟨3⟩1.** Substitution in (16) gives (18); the `r=1` equation gives the
D7 ratio in (18).  Substitution of `c^{r-1}` gives (19), whose squared
relative norm is `(1-c²)Σ_{r≥1}c^{2r-2}=1`.
Justification: geometric sums and direct recurrence substitution.

**⟨3⟩2.** For `w_q(r)=S(K,q)e^{iqr}+e^{-iqr}`, direct unit-circle
integration gives

\[
 \delta_{rs}=\int_0^\pi{dq\over2\pi}\,
 \overline{w_q(r)}w_q(s)+(1-c^2)c^{r+s-2}.                    \tag{20}
\]

Indeed, put `z=e^{iq}`, insert `(c-z^{-1})/(z-c)`, expand the geometric
denominator, and take the zero Fourier coefficient; the pole `z=c` is
exactly the last term.  The formula remains valid at `c=0,1` by continuity.
Justification: the residue theorem, equivalently coefficient extraction of
an absolutely convergent geometric series for `0<c<1`.

**⟨3⟩3.** Abel-summing the same geometric series gives
`Σ_r overline{w_q(r)}w_{q'}(r)=2πδ(q-q')`,
`Σ_r c^{r-1}w_q(r)=0`, and `Σ_r(1-c²)c^{2r-2}=1`.
Thus (20) is both the isometry and onto identity for the fiber transform.
Justification: `Σ_{r≥1}ρ^r e^{irα}` followed by `ρ↑1`, and (18).

**⟨3⟩4. QED.**

**⟨2⟩4. PROVE.** For every chamber vector `ψ`,

\[
 \|\psi\|^2=\int_{-\pi}^{\pi}dK\int_0^\pi dq\,
 |\langle\Psi^{\rm sc}_{Kq},\psi\rangle|^2
 +\int_{-\pi}^{\pi}dK\,|\langle\Psi^{\rm b}_{K},\psi\rangle|^2, \tag{21}
\]

and the same integrals of the rank-one kernels equal the identity.  On the
first summand `H` is multiplication by `E(K,q)`; on the second it is
multiplication by `E_b(K)`.

**⟨3⟩1.** Combine Fourier Plancherel (15) with the fiber identity (20).
Justification: Tonelli's theorem for the nonnegative norm integrals.

**⟨3⟩2.** Hence the scattering spectrum is absolutely continuous, the
full-chain bound eigenvalue becomes a bound-magnon band, and there is no
remaining spectral subspace.
Justification: (18)--(21) and unitarity of the spectral transform.

**⟨3⟩3.** If the factors `1/(2π)` and `1/√(2π)` are removed from (17) and
(19), the measures are respectively `dK dq/(2π)²` and `dK/(2π)`.  Also
`dK dq=dk_1dk_2`; at fixed `K` with `c>0`,
`dq=dE/(2Jc sin q)`.  On either branch of the bound band,
`dK=dE_b/√(E_b(J-E_b))`.
Justification: the Jacobians of (8), (18), and (19).

**⟨3⟩4. QED.**

## ⟨1⟩6. Numerical certificate and consequence for the soft shard

**⟨2⟩1. PROVE.** `theory/checks/ml2_completeness_check.py`, run normally and
with `python3 -O` for `SIZES=(6,10,11,12,13,14,16,18,20,22,26)`, gives the
following representative inventory.  “Real” excludes the separately printed
non-descendant degenerate `K=π` waves; “coincident” zero vectors are excluded.

\[
\begin{array}{c|r|r|r|r|r|r|r}
N&\dim&\text{real}&\text{strings}&\text{desc.}&\text{sing.}&\pi\text{-deg.}&
\text{coincident zero}\\\hline
12&66&41&8&12&1&4&12\\
16&120&85&12&16&1&6&16\\
20&190&145&16&20&1&8&20
\end{array}                                                     \tag{22}
\]

Maximum spectral mismatch is `8.882e-15`, eigenvector residual `4.044e-14`,
projector error `4.640e-14`, and singular-overlap error `6.280e-15`.
Justification: the checker independently builds D6, actual coincident D7
vectors, and (12)--(13), and exits explicitly on every failure.

**⟨2⟩2. PROVE.** Let `\mathscr B_K^{D7}` contain the normalized real, string,
and descendant states representable by D7, and set

\[
 \mathscr E_K=\mathscr B_K^{D7}\mathbin{\dot\cup}\mathscr X_K,\qquad
 \mathscr X_K=\begin{cases}\{|\chi_\pi\rangle\},&2\mid N, K\equiv\pi,\\
 \varnothing,&\text{otherwise}.\end{cases}                    \tag{23}
\]

Here `|χ_π⟩` has the separate unit normalization (12), not a D7 norm; on this
branch choose the congruent representatives with `k_s+k_h=π`.  Then

\[
 Q_{k_s}|k_h\rangle_N=\sum_{B\in\mathscr B_K^{D7}}c_B^{(R5)}|B\rangle
 +\mathbf1_{\mathscr X_K\ne\varnothing}\,
 2i\cos((k_h-k_s)/2)|\chi_\pi\rangle .                        \tag{24}
\]

**⟨3⟩1.** The `N` coefficients in (12) have modulus `N^{-1/2}`, so its norm
is one; its compactified root has no finite D7 normalization.

**⟨3⟩2.** Translation fibering makes the overlap zero unless
`k_s+k_h≡π`.  In that case the `N-1` ordinary adjacent pairs each contribute
`(e^{ik_h}+e^{ik_s})/N`; periodicity makes the wrap pair contribute the same.
Thus the overlap is `e^{ik_h}+e^{ik_s}=2i cos((k_h-k_s)/2)`.

**⟨3⟩3.** Completeness in ⟨1⟩4 and Parseval give (24); (R5) supplies exactly
the first sum, while the second coefficient is the proved singular leaf.

**⟨3⟩4. QED.**

**⟨2⟩3. QED.** The finite and infinite statements of Theorem ML2 are proved.
