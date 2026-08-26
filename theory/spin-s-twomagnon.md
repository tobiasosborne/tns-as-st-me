# Exact spin-`S` two-magnon scattering and soft phase slope

Status: **SKETCH (L6 proposer shard; critic promotion pending).**  Claim
`S2-2body-S` is the exact higher-spin generalisation of `S2-2body`.  The proof
uses the ordered-coordinate convention of D7 and the physical-channel rule of
D8/claim `S2-2body`, but not an integrability hypothesis or Bethe
completeness.  Uppercase `S` is the local name for the site spin (the `s` of
D13); it is kept distinct from `S_{12}`.

## Statement

**THEOREM S2-2body-S (exact spin-`S` two-magnon phase slope).**

**ASSUME.**  Let `S in {1/2,1,3/2,...}`, `J>0`, and

`H_S = -J sum_x (S_x . S_{x+1} - S^2)`

on the infinite chain, with all-up vacuum.  Use D7's chamber `x<y`, Fourier
sign, and coefficient ratio `S_{12}:=A_{12}/A_{21}`.  Put

`z_j:=exp(i k_j)`, `a:=1+z_1z_2`, `b:=z_1+z_2`, and
`μ:=(2S-1)a+b`.

For the exact ratio take real `k_1,k_2 in (-pi,pi]` in the regular scattering
domain

`k_1 != k_2 (mod 2pi)`, `a b != 0`, and `z_2 μ-Sab != 0`.              (T.1)

For the soft statement set `k_1=k_s`, `k_2=k_h`, hold
`0<|k_h|<pi` fixed, and take signed `k_s -> 0`.  Define

`omega_S(k):=2JS(1-cos k)`, `v_S(k):=2JS sin k`,
`v_h:=v_S(k_h)`, `v_s:=v_S(k_s)`,

`chi:=sgn(v_S(k_h)-v_S(k_s))`, and select the physical out/in ratio by

`S_phys:=S_{12}` if `chi=+1`, while `S_phys:=S_{21}=S_{12}^{-1}` if
`chi=-1`.  Let `delta_phys` be the unique continuous real phase of `S_phys`
with `delta_phys(0,k_h)=0`.

**PROVE.**  The two-magnon eigenvalue equation itself fixes

`S_{12}(k_1,k_2) = (S a b-z_1 μ)/(z_2 μ-S a b)`.              (T.2)

For real momenta in (T.1), `|S_{12}|=1` and
`S_{12}(k_2,k_1)=S_{12}(k_1,k_2)^{-1}`.  Moreover,

`delta_phys(k_s,k_h) = [chi/S] k_s + O(k_s^2)`,
`S_phys(k_s,k_h) = 1 + i[chi/S] k_s + O(k_s^2)`,               (T.3)

locally uniformly when `k_h` stays in a compact subset of
`{k:0<|k|<pi}` on which the physical channel is fixed.  In particular,

`(d delta_phys/d k_s)|_{k_s=0} = sgn(v_h-v_s)/S`.              (T.4)

Here the sign in (T.4) means its constant value in a sufficiently small soft
neighborhood.  On D8's half-zone `k_h in (0,pi)`, it is `+1`, so the slope is
exactly `1/S`.  At `S=1/2`, (T.2) is the frozen D7/oracle ratio and (T.4) is
`2 sgn(v_h-v_s)`, exactly Theorem `S2-2body`.

## ⟨1⟩1. Local two-magnon equations

**⟨2⟩1. ASSUME.**  Use the normalized occupation basis
`n_x:=S-S_x^z in {0,...,2S}`.  In the two-magnon sector write `psi(x,y)` for
`x<y`; when `S>=1`, write `d(x)` for the normalized doubly occupied state at
`x`.

Justification: the spin-`S` ladder representation and D7's ordered chamber.

**⟨2⟩2. PROVE.**  In occupation variables the Hamiltonian acts as

`H_S = 2JS sum_x n_x - J sum_x n_x n_{x+1}`
`      -(J/2) sum_x (S_x^+ S_{x+1}^- + S_x^- S_{x+1}^+)`.      (1)

One magnon therefore has `omega_S(k)=2JS(1-cos k)`.

**⟨3⟩1.**  On a bond, `S_x^zS_{x+1}^z=(S-n_x)(S-n_{x+1})`; summing
the two linear number terms over bonds gives `2S sum_x n_x`.

Justification: direct expansion of the displayed `H_S`.

**⟨3⟩2.**  The ladder matrix elements are

`<n-1|S^+|n>=sqrt[n(2S-n+1)]`,
`<n+1|S^-|n>=sqrt[(n+1)(2S-n)]`.                               (2)

For a single magnon the hopping amplitude is `-JS` and the diagonal is
`2JS`, giving the stated dispersion by Fourier substitution.

Justification: the irreducible spin-`S` representation and the D6/D7 Fourier
sign.

**⟨3⟩3. QED.**

**⟨2⟩3. PROVE.**  Put `g:=sqrt[S(2S-1)]`.  The exact coordinate equations are

`E psi(x,y)=4JS psi(x,y)`
` -JS[psi(x-1,y)+psi(x+1,y)+psi(x,y-1)+psi(x,y+1)]`,           (3)

for `y>x+1`,

`E psi(x,x+1)=J(4S-1)psi(x,x+1)`
` -JS[psi(x-1,x+1)+psi(x,x+2)]-Jg[d(x)+d(x+1)]`,              (4)

and, for `S>=1`,

`E d(x)=4JS d(x)-Jg[psi(x-1,x)+psi(x,x+1)]`.                  (5)

At `S=1/2`, `g=0`, the `d` channel is absent, and (4) is the D7 contact
equation.

**⟨3⟩1.**  Two separated single occupancies have diagonal `4JS` and four
empty-target hops, each of amplitude `-JS` by (2).

Justification: (1)--(2), named local computation **SS-C1**.

**⟨3⟩2.**  Adjacent single occupancies acquire `-J n_xn_{x+1}=-J`; the two
outer hops remain `-JS`.  An inner hop has magnitude

`(J/2)sqrt(2S)sqrt[2(2S-1)]=Jg`.

The same matrix element takes a double occupancy to either adjacent state.

Justification: (1)--(2), named local computation **SS-C2**.

**⟨3⟩3.**  A double occupancy has diagonal `4JS`, no occupied-neighbor
correction, and the two hops just computed, giving (5).

Justification: (1), **SS-C2**, and the normalized occupation basis.

**⟨3⟩4. QED.**

## ⟨1⟩2. The two contact conditions

**⟨2⟩1. ASSUME.**  Let

`Psi(x,y):=A z_1^x z_2^y+B z_2^x z_1^y`                      (6)

on all of `Z^2`, but identify the physical separated wave with `Psi` only in
the chamber `x<y`.  Put `P:=z_1z_2`, `Sigma:=A+B`,
`W:=A z_2+B z_1`, and, for `S>=1`, take `d(x)=rho P^x`.

Justification: this is a trial solution to be checked directly in (3)--(5),
not an assumed consequence of integrability.

> [!WARNING]
> **The free extension (6) is not symmetric at the diagonal.**  In general
> `Psi(y,x) != Psi(x,y)` unless `A=B`.  Therefore one may not replace
> `Psi(x+1,x)` by `Psi(x,x+1)` when extending the free equation to `(x,x)`.
> That illicit replacement collapses the two contacts to the spin-`1/2`
> condition and falsely gives slope `2` for every `S`.  The valid proof keeps
> (6) unsymmetrised, introduces the independent physical amplitude `d(x)`,
> and imposes both (4) and (5).

**⟨2⟩2. PROVE.**  Equation (3) holds term by term with

`E=omega_S(k_1)+omega_S(k_2)`.                                (7)

**⟨3⟩1.**  Each of the four shifts of either plane wave in (6) multiplies it
by `z_1^{+/-1}` or `z_2^{+/-1}`; collecting them gives (7).

Justification: direct substitution in (3), named residual computation
**SS-Rfree**.

**⟨3⟩2. QED.**

**⟨2⟩3. PROVE.**  For `S>=1`, the double-occupancy equation (5) gives

`rho=sqrt[(2S-1)/S] W/b`.                                     (8)

**⟨3⟩1.**  The two adjacent values in (5) sum to
`P^{x-1}aW`.  From (7), `E-4JS=-JS(ab/P)`.

Justification: (6)--(7) and the identities
`a=1+P`, `ab/P=z_1+z_1^{-1}+z_2+z_2^{-1}`.

**⟨3⟩2.**  Substitution in (5), followed by cancellation of the nonzero
`a,b` from (T.1), gives `S b rho=gW`; since `g/S=sqrt[(2S-1)/S]`, this is
(8).

Justification: (5), ⟨3⟩1, and domain (T.1).

**⟨3⟩3. QED.**

**⟨2⟩4. PROVE.**  The remaining contact equation is

`W[(2S-1)a+b]=S Sigma a b`.                                   (9)

It also holds at `S=1/2`, where it reduces to `2W=aSigma` on (T.1).

**⟨3⟩1.**  Compare the physical adjacent equation (4) with the free equation
(3) evaluated at `(x,x+1)`.  The two outer hops cancel, leaving

`W=SaSigma-g a rho`.                                          (10)

Justification: (3)--(7); the artificial diagonal free values are
`Psi(x,x)+Psi(x+1,x+1)=P^x aSigma` and are used only in this subtraction.

**⟨3⟩2.**  For `S>=1`, insert (8) and `g^2=S(2S-1)` into (10), then multiply
by `b`, obtaining (9).

Justification: (8), (10), and algebra.

**⟨3⟩3.**  For `S=1/2`, the last term of (10) is absent, so
`W=(1/2)aSigma`; since then `μ=b`, this is exactly (9) on `b!=0`.

Justification: (4)--(5) at `S=1/2` and domain (T.1).

**⟨3⟩4. QED.**

## ⟨1⟩3. Exact ratio, unitarity, and direct eigenvector validity

**⟨2⟩1. PROVE.**  Contact equation (9) fixes the coefficient ratio (T.2).

**⟨3⟩1.**  Expanding `W μ=S Sigma ab` gives

`A(z_2mu-Sab)+B(z_1mu-Sab)=0`.

Justification: the definitions in ⟨1⟩2.⟨2⟩1 and (9).

**⟨3⟩2.**  Since the first coefficient is nonzero on (T.1), solving for
`A/B` gives `(Sab-z_1mu)/(z_2mu-Sab)`.

Justification: D7's definition of `S_{12}` and (T.1).

**⟨3⟩3. QED.**

**⟨2⟩2. PROVE.**  For real regular momenta, (T.2) is unitary and exchanging
the momenta inverts it.

**⟨3⟩1.**  Put `K:=k_1+k_2`, `q_rel:=(k_1-k_2)/2`,
`c_K:=cos(K/2)`, and

`n:=2S c_K cos(q_rel)-exp(iq_rel)[(2S-1)c_K+cos(q_rel)]`.       (11)

Direct Laurent-polynomial reduction of (T.2) gives

`S_{12}=n/(-conj(n))`.                                        (12)

Justification: named exact computation **SS-C3**; substitute
`z_1=u r`, `z_2=u/r`, `u=exp(iK/2)`, `r=exp(iq)`, and use
`conj(u)=u^{-1}`, `conj(r)=r^{-1}`.

**⟨3⟩2.**  Equation (12) has unit modulus wherever (T.1) makes it defined.
Swapping `z_1,z_2` exchanges the numerator and denominator of (T.2) up to
the same minus sign, hence gives the inverse.

Justification: (T.1)--(T.2), (12), and complex conjugation.

**⟨3⟩3. QED.**

**⟨2⟩3. PROVE.**  The wave consisting of (6) on `x<y` and (8) on `x=y`
(when present) satisfies the complete infinite-chain two-magnon eigenvalue
equation with energy (7).

**⟨3⟩1.**  Equations (3)--(5) exhaust the separated, adjacent, and doubly
occupied configurations.  Their residuals vanish respectively by (7),
(8), and (9).

Justification: ⟨1⟩1.⟨2⟩3 and ⟨1⟩2.⟨2⟩2--⟨1⟩2.⟨2⟩4.

**⟨3⟩2.**  No completeness or many-body Bethe assumption entered: (6) was
validated by direct substitution into every configuration class.

Justification: the exhaustive residual computation in ⟨3⟩1; compare the
integrability-free framing of claim `S2-2body`.

**⟨3⟩3.**  On a ring, adding the Bethe--Yang conditions
`Nk_1=2pi n_1+delta_12`, `Nk_2=2pi n_2-delta_12` cancels the seam residual.
The independent checker assembles the occupation Hamiltonian and verifies
this full residual for `2S=1,2,3,4`.

Justification: D7 periodic continuation and named computation **SS-C6**.

**⟨3⟩4. QED.**

## ⟨1⟩4. The exact soft derivative and its physical sign

**⟨2⟩1. PROVE.**  For every fixed `0<|k_h|<pi`, the algebraic D7 phase of
`S_{12}(k_s,k_h)` has derivative `1/S` at `k_s=0`.

**⟨3⟩1.**  Write (T.2) as `N/D` and put `y:=exp(ik_h)`.  At `z_1=1`,

`N(0)=D(0)=S(y-1)(y+1) != 0`.                                 (13)

Justification: direct substitution in (T.2); the exclusions
`k_h!=0,+/-pi` make the product nonzero.

**⟨3⟩2.**  With `partial_{k_s}=i z_1 partial_{z_1}`, direct differentiation
gives

`[partial_{k_s}N-partial_{k_s}D]_{k_s=0}=i(y-1)(y+1)`.         (14)

Consequently

`[partial_{k_s} log S_{12}]_0=i/S`.                            (15)

Justification: (T.2), (13), and named symbolic computation **SS-C4**.

**⟨3⟩3.**  Since `S_{12}(0,k_h)=1` and the ratio is unitary on the real
axis, the continuous D7 phase satisfies
`partial_{k_s}delta_12|_0=Im(i/S)=1/S`.

Justification: D7's phase convention, ⟨1⟩3.⟨2⟩2, and (15).

**⟨3⟩4. QED.**

**⟨2⟩2. PROVE.**  The physical phase satisfies (T.3)--(T.4).

**⟨3⟩1.**  Because `v_S(k_h)!=0`, the sign
`chi=sgn(v_S(k_h)-v_S(k_s))` is constant for all sufficiently small
`|k_s|`.  D7's velocity ordering chooses `S_{12}` for `chi=+1` and its
inverse for `chi=-1`.

Justification: the displayed velocity in the theorem, D7, and the channel
construction in `oracle-bethe.md` ⟨1⟩3.⟨2⟩1.

**⟨3⟩2.**  Inversion negates the continuous phase.  Multiplying ⟨2⟩1's
derivative by `chi` gives (T.4), and Taylor expansion of the analytic regular
ratio gives both statements in (T.3).

Justification: ⟨2⟩1, D7, and the analytic quotient (T.2) near (13).

**⟨3⟩3.**  On any compact hard subset away from `0,+/-pi`, the denominator in
(13) has a positive lower bound; finitely many derivatives of (T.2) are then
uniformly bounded on a common soft neighborhood.

Justification: continuity, compactness, and Taylor's theorem.

**⟨3⟩4. QED.**

**⟨2⟩3. PROVE.**  At `S=1/2`, the theorem reduces exactly to frozen
`S2-2body`.

**⟨3⟩1.**  Then `μ=b`, and cancellation in (T.2) gives

`S_{12}=-(z_1z_2-2z_1+1)/(z_1z_2-2z_2+1)`.                   (16)

Justification: substitution of `S=1/2` in (T.2), named computation
**SS-C5**.

**⟨3⟩2.**  Equation (T.4) becomes `2 sgn(v_h-v_s)`.  On D8 it is `2`, and
the checker also recovers the frozen quadratic coefficients
`cot(k_h/2)` for `delta_phys` and `i cot(k_h/2)-2` for `S_phys`.

Justification: claim `S2-2body`, oracle O7--O9, (16), and **SS-C5**.

**⟨3⟩3. QED.**

**⟨2⟩4. QED.**  Theorem `S2-2body-S` is proved within this proposer shard.
Its L5 status remains SKETCH until the dedicated L6 critic loop converges.

## ⟨1⟩5. Checker certificate and scope

**⟨2⟩1. PROVE.**  `theory/checks/spin_s_slope_check.py` is an independent,
red-capable certificate for **SS-C3**--**SS-C6**.

**⟨3⟩1.**  SymPy proves the Laurent identity (12), the derivative (15), and
the exact `S=1/2` reduction including the frozen second-order coefficients.
NumPy checks (T.2) against (11) on a grid of spins and real momenta.

Justification: inspection of checker functions `check_symbolic_identities`,
`check_grid`, and `check_half_spin_freeze`.

**⟨3⟩2.**  The ring Hamiltonian is assembled from (1)--(2), not from (T.2).
Its Bethe--Yang vectors satisfy the full eigenvalue equation, including the
periodic seam.

Justification: checker functions `ring_hamiltonian` and `check_ring_residual`.

**⟨3⟩3.**  `--red` replaces `(2S-1)` in `μ` by `(2S+1)` while retaining the
theorem target.  The symbolic independent-form check must exit `1`; all
failures use `SystemExit(1)`, so `python3 -O` cannot disable them.

Justification: the checker module docstring and explicit `require` calls.

**⟨3⟩4. QED.**

**⟨2⟩2. REMARK (relation to Conjecture Bc; no status promotion).**  Equations
(T.2)--(T.4) prove the **slope half** of Bc's proposed `|q_hard|/s` law for a
unit-charge hard magnon, `|q_hard|=1`, for every site spin.  The memory half
remains the conditional content of `M-quant`/`M-quant-G`; the `|q_hard|>1`
factor is open (`tns-ebh`).  Therefore Bc remains CONJECTURE, and nothing here
promotes `S-general` or process independence.

Justification: claims `Bc`, `M-quant`, `M-quant-G`, `S-general`, and D25.

**⟨2⟩3. QED.**
