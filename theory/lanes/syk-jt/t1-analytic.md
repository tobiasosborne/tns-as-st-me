# T1: exact tree-level Schwarzian memory computation

## ⟨1⟩0. Scope, conventions, and source audit

⟨1⟩0.⟨2⟩1. **ASSUME (controlled regime).** Work at classical/tree level in the
Schwarzian theory, with \(C>0\), and write

\[
\kappa={2\pi\over\beta},\qquad E(\kappa)={C\kappa ^2\over2}.
\tag{0.1}
\]

The approximation is the large-\(C/\beta\) saddle expansion: the local source
says that the Schwarzian is of order \(1/G\) and is therefore perturbatively
evaluated around a solution, and that its effective coupling is \(\beta/C\)
(`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:680-684,717-719`).

⟨1⟩0.⟨2⟩2. **ASSUME (thermal representatives and orientation).** Fix the early
simultaneous two-sided \(SL(2,\mathbb R)\) redundancy by

\[
t_R^{\,i}(u)=e^{\kappa_i u},\qquad
t_L^{\,i}(u)=-e^{-\kappa_i u},\qquad u=0\text{ is the synchronized origin}.
\tag{0.2}
\]

Both maps have positive derivative.  They have charges
\(Q_R=(0,-C\kappa_i,0)\) and \(Q_L=-Q_R\), as follows by inserting (0.2)
in the displayed charge formula below; the equal-and-opposite two-sided
constraint is stated explicitly in
`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:902-909`, and the
thermal value \(Q^0=-2\pi C/\beta\) is printed at that source's lines 912--915.

⟨1⟩0.⟨2⟩3. **PROVE (only a relative frame survives).** A simultaneous map

\[
t_L\mapsto h\mathbin\cdot t_L,\qquad
t_R\mapsto h\mathbin\cdot t_R,\qquad
h\mathbin\cdot t={a t+b\over c t+d},\quad ad-bc=1,
\tag{0.3}
\]

does not change any bilocal used below.  Hence (0.2) spends that one common
redundancy, while a right-only late map \(g_{\rm rel}\) is relational and is
not subsequently quotiented out.  Indeed, direct substitution in
\(t'_1t'_2/(t_1-t_2)^2\) cancels the two Möbius denominators and the determinant;
the source states both the Möbius identification
(`GravityReparametrizationsRevised.tex:373-382`) and that the bilocal vertex is
\(SL(2)\)-invariant (`GravityReparametrizationsRevised.tex:729-740`).

⟨1⟩0.⟨2⟩4. **ASSUME (detector).** For a matter primary of dimension
\(\Delta>0\), use the operational two-copy correlator

\[
G_{LR}(u_L,u_R)=
{\cal N}_\Delta
\left[{t'_L(u_L)t'_R(u_R)\over
              (t_R(u_R)-t_L(u_L))^2}\right]^{\!\Delta}.
\tag{0.4}
\]

The normalization \({\cal N}_\Delta\) cancels from every comparison.  The local
source derives precisely the reparametrized kernel
\([t'(u)t'(u')/(t(u)-t(u'))^2]^\Delta\) and says that every insertion carries
the corresponding derivative factor
(`GravityReparametrizationsRevised.tex:645-657,662-675`).  A two-sided
correlator is an explicit detector in the shock calculation
(`refs/arxiv-1306.0622/shock.tex:275-293`).

⟨1⟩0.⟨2⟩5. **PROVE (sign fixed by (T.1), not by prose).** Define the
standard Schwarzian and printed soft charges by

\[
\begin{aligned}
\operatorname{Sch}(t,u)&={t'''\over t'}-{3\over2}\left({t''\over t'}\right)^2,\\
Q^-&=C\left({t'''\over t'^2}-{t''^2\over t'^3}\right),\\
Q^0&=C\left({tt'''\over t'^2}-{t t''^2\over t'^3}-{t''\over t'}\right),\\
Q^+&=C\left({t^2t'''\over t'^2}-{t^2t''^2\over t'^3}
             -{2tt''\over t'}+2t'\right).
\end{aligned}
\tag{0.5}
\]

Elementary differentiation gives the exact identities

\[
{d\over du}(Q^-,Q^0,Q^+)
=C{\operatorname{Sch}'(t,u)\over t'}(1,t,t^2).
\tag{0.6}
\]

Consequently the sourced equation required by the brief,

\[
C{\operatorname{Sch}'(t,u)\over t'}=-t'T_{tz},
\tag{0.7}
\]

implies

\[
Q_f^a-Q_i^a=-{\cal J}^a,qquad
{\cal J}^a:=\int_{u_i}^{u_f}du\;t'T_{tz}(1,t,t^2)^a.
\tag{0.8}
\]

Thus the quantity called an “injected charge increment” in the work order is
\({\cal J}^a\), while the *soft* charge increment is its negative.  Equations
(0.5) are quoted at
`GravityReparametrizationsRevised.tex:889-900`; (0.7), including its minus
sign, is printed at lines 611--623.  The prose equation at lines 957--964 has
the opposite sign, but the immediately following TeX comment says
`FIXSIGNS AND FACTORS` (`GravityReparametrizationsRevised.tex:955-965`).
Equations (0.6)--(0.8), a named quotient-rule computation, therefore fix every
normalization below without fitting.

⟨1⟩0.⟨2⟩6. **PROVE (energy bookkeeping).** The charge Casimir and (0.7)
give

\[
H={-Q^+Q^-+(Q^0)^2\over2C}=-C\operatorname{Sch}(t,u),
\qquad {dH\over du}=t'^2T_{tz}=:P(u).
\tag{0.9}
\]

For (0.2), this is (0.1).  The first equality is the printed Hamiltonian
relation at `GravityReparametrizationsRevised.tex:921-929`; the second and
third follow from (0.5)--(0.7) by elementary differentiation.  The source also
explains that two factors of \(t'\) convert the flux to boundary-time power
(`GravityReparametrizationsRevised.tex:618-622`).

## ⟨1⟩1. Step 1 — prepare, perturb, and subtract the final stationary state

⟨1⟩1.⟨2⟩1. **ASSUME (compact event).** Let \(P=t'^2T_{tz}\) have compact
support in \([u_i,u_f]\), let

\[
\Delta E=\int_{u_i}^{u_f}P(u)\,du,qquad
\kappa_f=\sqrt{\kappa_i^2+{2\Delta E\over C}},
\tag{1.1}
\]

and require the square root to be real.  Equation (1.1) is the integral of
(0.9), hence is a displayed-prior-equation computation.

⟨1⟩1.⟨2⟩2. **ASSUME (the two protocols).** Protocol (a) imposes
\(\Delta E=0\), so \(\kappa_f=\kappa_i\).  Protocol (b) permits
\(\Delta E\ne0\), but compares with the synchronized equilibrium saddle of
stiffness \(C\) and inverse temperature \(2\pi/\kappa_f\); no term proportional
to \((\kappa_f-\kappa_i)T\) is called memory.  This implements the requested
final-energy subtraction using (1.1); the source identifies the thermal
solutions as \(\tau=2\pi u/\beta\)
(`GravityReparametrizationsRevised.tex:535-551`) and gives their energy through
the charge Casimir (`GravityReparametrizationsRevised.tex:912-929`).

⟨1⟩1.⟨2⟩3. **ASSUME [physical argument] (unbalanced reference clock).**
For protocol (b), “equilibrium at \(E_f\)” must include a synchronization
choice in addition to an energy: use the same origin \(u=0\) as (0.2), and use

\[
t_L^{\rm eq}(u;E_f)=-e^{-\kappa_f u},\qquad
t_R^{\rm eq}(u;E_f)=e^{\kappa_f u}.
\tag{1.2}
\]

Energy alone does not fix the relative origin; changing only one factor in
(1.2) is precisely the relational clock shift being tested.  This need for
both sides is supported by the source statement that one-sided charges can be
arbitrary while the two-sided charges are equal and opposite
(`GravityReparametrizationsRevised.tex:902-909`).

⟨1⟩1.⟨2⟩4. **PROVE (subtraction removes temperature drift).** If the
late right solution has exponent \(\kappa_f\), subtracting (1.2) removes the
only possible secular term \((\kappa_f-\kappa_i)u\) in its logarithmic clock.
What remains is a constant-\(\kappa_f\) Möbius mismatch.  This follows from the
constant-Schwarzian solution classified in (2.1) below and the elementary
identity \(\operatorname{Sch}(e^{\kappa u},u)=-\kappa^2/2\); it is not an
assumption that the mismatch is nonzero.

## ⟨1⟩2. Step 2 / (T.1) — exact late solution and relative Möbius data

⟨1⟩2.⟨2⟩1. **PROVE (classification outside the source).** On either
connected component of \(u\notin[u_i,u_f]\), (0.7) gives constant Schwarzian.
Every orientation-preserving solution with energy \(E=C\kappa^2/2>0\) is

\[
t(u)=g\mathbin\cdot e^{\kappa u}
 ={a e^{\kappa u}+b\over c e^{\kappa u}+d},\qquad
g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL(2,\mathbb R).
\tag{2.1}
\]

This follows by the named elementary Schwarzian theorem: equal Schwarzians
imply that two locally univalent functions differ by a Möbius map.  Here
\(\operatorname{Sch}(e^{\kappa u},u)=-\kappa^2/2\), while the source states
that the source-free equation is constant Schwarzian
`GravityReparametrizationsRevised.tex:520-524` and that the thermal solutions
are Möbius transforms of \(\tau=2\pi u/\beta\)
`GravityReparametrizationsRevised.tex:535-551`.

⟨1⟩2.⟨2⟩2. **PROVE (charges of a thermal Möbius map).** Substitution
of (2.1) into (0.5) gives, exactly,

\[
Q^-=-2C\kappa cd,\qquad
Q^0=-C\kappa(ad+bc),\qquad
Q^+=-2C\kappa ab.
\tag{2.2}
\]

The Casimir is therefore

\[
(Q^0)^2-Q^+Q^-=C^2\kappa^2(ad-bc)^2=C^2\kappa^2.
\tag{2.3}
\]

Equations (2.2)–(2.3) are a named quotient-rule substitution into displayed
equation (0.5); (2.3) also agrees with the printed Hamiltonian Casimir
`GravityReparametrizationsRevised.tex:921-929`.

⟨1⟩2.⟨2⟩3. **PROVE (what the injected charges do determine).** Set

\[
Q_f=Q_i-{\cal J},\qquad
X=-{Q_f^+\over2C\kappa_f},\quad
Y=-{Q_f^0\over C\kappa_f},\quad
Z=-{Q_f^-\over2C\kappa_f},\quad
A={Y+1\over2}.
\tag{2.4}
\]

Then \(Y^2-4XZ=1\) by (2.3).  In the chart \(A>0\), a definite section of the
charge orbit is

\[
g_{\rm can}(Q_f)=
\begin{pmatrix}
\sqrt A&X/\sqrt A\\[2pt]
Z/\sqrt A&\sqrt A
\end{pmatrix},\qquad
g_{\rm rel}=g_{\rm can}(Q_f)h(\lambda),\qquad
h(\lambda)=\begin{pmatrix}\lambda&0\\0&\lambda^{-1}\end{pmatrix}.
\tag{2.5}
\]

Direct multiplication uses \(XZ=A(A-1)\), gives determinant one, and
reproduces (2.2).  Other nonsingular charts are obtained by interchanging
matrix entries; this is ordinary \(SL(2)\) coordinate algebra based on
(2.2)–(2.4).

⟨1⟩2.⟨2⟩4. **PROVE (charge increments alone do *not* determine
\(g_{\rm rel}\)).** The parameter \(\lambda\) cancels from all four products
\(ab,cd,ad,bc\), so every member of (2.5) has the same three charges.  It acts
on the thermal coordinate by the right composition
\(e^{\kappa_f u}\mapsto\lambda^2e^{\kappa_f u}\), i.e. by a relative time
origin shift \(2\log\lambda/\kappa_f\).  Since (0.2) already fixed the common
two-sided \(SL(2)\), this right-only shift is not residual gauge.  The printed
source likewise says that a charge-induced effect can be gauged away before
or after an insertion, but not on both pieces simultaneously
`GravityReparametrizationsRevised.tex:1116-1122`.

⟨1⟩2.⟨2⟩5. **PROVE (closed reconstruction with the missing endpoint
datum).** Let \(t_f=t_R(u_f+0)\), \(x_f=e^{\kappa_f u_f}\), and write
\(g_{\rm can}=\left(\begin{smallmatrix}a_0&b_0\\c_0&d_0\end{smallmatrix}\right)\).
Continuity of \(t\) gives

\[
\boxed{\quad
\lambda^2={b_0-d_0t_f\over
                 x_f(c_0t_f-a_0)},\qquad
g_{\rm rel}=g_{\rm can}(Q_i-{\cal J})h(\lambda).
\quad}
\tag{2.6}
\]

The positive real branch is selected for an orientation-preserving trajectory;
the adjacent projective chart handles a zero numerator or denominator.
Equation (2.6) is obtained by solving
\(t_f=(a_0\lambda^2x_f+b_0)/(c_0\lambda^2x_f+d_0)\), a named one-line linear
fractional computation using (2.5).  Thus (T.1) supplies \(t_f\) through its
initial-value solution, but the three *integrated* numbers \({\cal J}^a\) do
not supply it.

⟨1⟩2.⟨2⟩6. **PROVE (minimal counterexample to a charge-only map).**
If \(Q_f=Q_i\), then \(g_{\rm can}=I\), while every
\(g_{\rm rel}=h(\lambda)\) has the same charges and changes the right clock by
\(2\log\lambda/\kappa_i\).  Nontrivial such trajectories are generated by a
compact balanced event in ⟨1⟩2.⟨2⟩8 below.  Therefore no single-valued
map \({\cal J}^a\mapsto g_{\rm rel}\) exists with the operational gauge choice
of (0.2); (2.6) is the exact corrected statement.  This is direct matrix
algebra from (2.2) and (2.5), not a physics assumption.

⟨1⟩2.⟨2⟩7. **PROVE (exact impulse transfer).** For an instantaneous
power kick at \(u=s\) changing \(\kappa_-\) to \(\kappa_+>0\), define

\[
\begin{aligned}
B(\kappa_-,\kappa_+)&={1\over2\sqrt{\kappa_-\kappa_+}}
 \begin{pmatrix}
 \kappa_++\kappa_-&\kappa_+-\kappa_-\\
 \kappa_+-\kappa_-&\kappa_++\kappa_-
 \end{pmatrix},\\
H_\kappa(s)&=\operatorname{diag}
 (e^{\kappa s/2},e^{-\kappa s/2}).
\end{aligned}
\tag{2.7}
\]

If the pre-kick global matrix is \(G_-\), then

\[
G_+=G_-H_{\kappa_-}(s)B(\kappa_-,\kappa_+)
                    H_{\kappa_+}(s)^{-1}.
\tag{2.8}
\]

Indeed \(B(\kappa_-,\kappa_+)\cdot e^{\kappa_+(u-s)}\) and
\(e^{\kappa_-(u-s)}\) have identical \(t,t',t''\) at \(u=s\); their
Schwarzians, and hence energies, differ by
\(C(\kappa_+^2-\kappa_-^2)/2\).  This is a named three-derivative matching
calculation using (0.9) and (2.1).  Distributionally the profile is

\[
P(u)={C\over2}(\kappa_+^2-\kappa_-^2)\delta(u-s),\qquad
T_{tz}(u)={P(u)\over t'(s)^2},
\tag{2.9}
\]

which integrates (0.9) exactly; a smooth narrow pulse converges to it with
errors discussed in ⟨1⟩4.⟨2⟩8.

⟨1⟩2.⟨2⟩8. **PROVE (exact balanced and unbalanced families).** An
unbalanced kick at \(s=0\) has

\[
g_{\rm un}=B(\kappa_i,\kappa_f).
\tag{2.10}
\]

A balanced pair which raises \(\kappa\) to \(\kappa_1\) at \(u=0\), holds it
until \(u=L\), and lowers it back to \(\kappa\), has

\[
g_{\rm bal}=B(\kappa,\kappa_1)H_{\kappa_1}(L)
             B(\kappa_1,\kappa)H_\kappa(L)^{-1}.
\tag{2.11}
\]

Its net energy injection is zero, but (unless \(L=0\) or
\(\kappa_1=\kappa\)) the product is not the identity and contains the phase
missing from the final charges.  Equations (2.10)–(2.11) are direct repeated
application of (2.8); compact source support and zero balanced net energy
follow from (2.9).

## ⟨1⟩3. Step 3 / (T.2) — exact two-sided detector and the plateau test

⟨1⟩3.⟨2⟩1. **ASSUME (future projective chart).** Write the reconstructed
late relative matrix as

\[
g_{\rm rel}=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad ad-bc=1,
\qquad a>0,
\tag{3.1}
\]

where the harmless overall \(PSL(2,\mathbb R)\) sign is chosen so that the
future chart has \(a>0\).  This is the matrix of (2.6); the source identifies
Möbius-related representatives as the relevant \(SL(2)\) action
(`GravityReparametrizationsRevised.tex:373-382`).

⟨1⟩3.⟨2⟩2. **PROVE (exact correlator).** Put
\(x=e^{\kappa_fT}\) and use the final-energy reference (1.2).  Direct
substitution of \(t_R=g_{\rm rel}\cdot x\) and \(t_L=-x^{-1}\) into (0.4)
gives

\[
\begin{aligned}
D_g(T)&:=a x+(b+c)+{d\over x},\\
G_{LR}^{\rm pulse}(T,T)
 &= {\cal N}_\Delta\left[{\kappa_f^2\over D_g(T)^2}\right]^\Delta,\\
G_{LR}^{\rm eq}(T,T;E_f)
 &= {\cal N}_\Delta
 \left[{\kappa_f^2\over(x+x^{-1})^2}\right]^\Delta,\\
\boxed{\;
\delta G_{LR}(T)
 ={\cal N}_\Delta\kappa_f^{2\Delta}
\left[D_g(T)^{-2\Delta}-(x+x^{-1})^{-2\Delta}\right].
\;}
\end{aligned}
\tag{3.2}
\]

The cancellation of \(cx+d\) uses \(ad-bc=1\) and is a named fractional-linear
derivative computation.  Equation (0.4), derived from the local source at
`GravityReparametrizationsRevised.tex:645-675`, is the only physical
input.

⟨1⟩3.⟨2⟩3. **PROVE (literal linearized displacement in the brief).** The
equilibrium derivative and exact ratio are

\[
{\partial_TG_{LR}^{\rm eq}\over G_{LR}^{\rm eq}}
 =-2\Delta\kappa_f\tanh(\kappa_fT),\qquad
R_g(T):={G_{LR}^{\rm pulse}\over G_{LR}^{\rm eq}}
 =\left[{x+x^{-1}\over D_g(T)}\right]^{2\Delta}.
\tag{3.3}
\]

Therefore the displacement defined *literally* by
\(\delta G_{LR}\simeq-\Delta u_{\rm rel}\partial_TG_{LR}^{\rm eq}\) is

\[
\boxed{\;
\Delta u_{\rm rel}^{\rm lin}(T)
 ={R_g(T)-1\over2\Delta\kappa_f\tanh(\kappa_fT)}
\;}
\tag{3.4}
\]

when \(|R_g-1|\ll1\) and \(\tanh(\kappa_fT)\ne0\).  Equations (3.3)–(3.4)
are named differentiation and first-order Taylor computations from (3.2).

⟨1⟩3.⟨2⟩4. **PROVE (exact nonlinear clock readout).** Whenever
\(D_g(T)\ge2\), define the dimension-independent exact diagonal shift by

\[
G_{LR}^{\rm pulse}(T,T)
=G_{LR}^{\rm eq}(T-\Delta u_{\rm rel}^{\rm NL},
                 T-\Delta u_{\rm rel}^{\rm NL};E_f).
\tag{3.5}
\]

Solving (3.5) gives

\[
\boxed{\;
\Delta u_{\rm rel}^{\rm NL}(T)
=T-{1\over\kappa_f}\operatorname{arcosh}{D_g(T)\over2}.
\;}
\tag{3.6}
\]

It reduces to (3.4) at first order.  If \(D_g<2\), no real shift along the
equal-time diagonal reproduces a correlator above its equilibrium maximum,
so only the exact observable (3.2) is used.  Equation (3.6) is the named
inverse-hyperbolic-cosine computation from displayed equations (3.2) and
(3.5).

⟨1⟩3.⟨2⟩5. **PROVE (late behavior).** As \(T\to+\infty\),

\[
\begin{aligned}
\delta G_{LR}(T)
&={\cal N}_\Delta\kappa_f^{2\Delta}e^{-2\Delta\kappa_fT}
\left[
a^{-2\Delta}-1
-{2\Delta(b+c)\over a^{2\Delta+1}}e^{-\kappa_fT}
+O(e^{-2\kappa_fT})
\right],\\
\Delta u_{\rm rel}^{\rm lin}(T)
&={a^{-2\Delta}-1\over2\Delta\kappa_f}
+O(e^{-\kappa_fT}),\\
\Delta u_{\rm rel}^{\rm NL}(T)
&=-{\log a\over\kappa_f}+O(e^{-\kappa_fT}).
\end{aligned}
\tag{3.7}
\]

This is the named binomial and \(\operatorname{arcosh}z=\log(2z)+O(z^{-2})\)
expansion of (3.2)–(3.6).  The absolute correlator difference always decays
for \(\Delta>0\), but the relational clock readout has a nonzero plateau
exactly when \(a\ne1\).

⟨1⟩3.⟨2⟩6. **PROVE (balanced protocol).** Put
\(\eta=\frac12\log(\kappa_1/\kappa)\).  Multiplication of (2.11) gives

\[
a_{\rm bal}
=\cosh^2\eta\;e^{(\kappa_1-\kappa)L/2}
 -\sinh^2\eta\;e^{-(\kappa_1+\kappa)L/2}.
\tag{3.8}
\]

Thus a nontrivial raise–hold–lower pulse has, generically,
\[
\Delta u_{{\rm rel,bal}}^{\rm NL}(\infty)
=-{1\over\kappa}\log a_{\rm bal}\ne0.
\tag{3.9}
\]
For \(\delta\kappa=\kappa_1-\kappa\) small,
\[
\Delta u_{{\rm rel,bal}}^{\rm NL}(\infty)
=-{\delta\kappa\,L\over2\kappa}
O(\delta\kappa^2).
\tag{3.10}
\]

Equations (3.8)–(3.10) are elementary \(2\times2\) multiplication and Taylor
expansion of displayed equation (2.11).  They also exhibit constructively the
charge-phase underdetermination proved in ⟨1⟩2.⟨2⟩6.

⟨1⟩3.⟨2⟩7. **PROVE (unbalanced protocol with final-energy subtraction).**
For the one-kick family (2.10),
\[
a_{\rm un}={\kappa_f+\kappa_i\over2\sqrt{\kappa_i\kappa_f}}
=\cosh\!\left({1\over2}\log{\kappa_f\over\kappa_i}\right),
\tag{3.11}
\]
and hence
\[
\Delta u_{{\rm rel,un}}^{\rm NL}(\infty)
=-{1\over\kappa_f}\log a_{\rm un}.
\tag{3.12}
\]
This is nonzero for every finite \(\kappa_f\ne\kappa_i\), but begins at
quadratic response:
\[
\Delta u_{{\rm rel,un}}^{\rm NL}(\infty)
=-{(\kappa_f-\kappa_i)^2\over8\kappa_i^3}
+O((\kappa_f-\kappa_i)^3).
\tag{3.13}
\]
A finite-duration unbalanced pulse can additionally carry a linear plateau,
computed in (4.10) below.  Equations (3.11)–(3.13) are direct substitution of
(2.10) into (3.7) and a named Taylor expansion.

⟨1⟩3.⟨2⟩8. **PROVE (why the Shenker–Stanford shock decays).** The pure
horizon translation is

\[
g_{\rm shock}=\begin{pmatrix}1&\alpha\\0&1\end{pmatrix},\qquad
D_{\rm shock}=x+x^{-1}+\alpha .
\tag{3.14}
\]

Because \(a_{\rm shock}=1\), (3.7) gives
\[
\Delta u_{\rm rel}^{\rm NL}(T)
=-{\alpha\over\kappa_f}e^{-\kappa_fT}
+O(e^{-2\kappa_fT}),\qquad
\delta G_{LR}=O(e^{-(2\Delta+1)\kappa_fT}).
\tag{3.15}
\]

This is exactly the decay mechanism in the shock geodesic: its correction is
\(\alpha e^{-R(t_L+t_R)/(2\ell^2)}\), and the source explicitly says that it
becomes insignificant at sufficiently large \(t_L+t_R\)
(`refs/arxiv-1306.0622/shock.tex:223-234`).  The often-quoted permanent
\(\widetilde v=v+\alpha\) is a null-coordinate matching step
(`shock.tex:188-205`), whereas (3.2) is a late two-boundary detector.
The two computations therefore agree: the butterfly translation is a
transient relational time delay.  A nonzero plateau in (3.7) is a different
Möbius component—a relative thermal dilation \(a\ne1\)—which the shock
double-scaling limit sets to one.

## ⟨1⟩4. Step 4 / (T.3) — retarded DC residue versus the soft vertex

⟨1⟩4.⟨2⟩1. **ASSUME (linear one-soft expansion).** Around a thermal
trajectory of exponent \(\kappa\), write
\[
t_R(u)=e^{\tau(u)},\qquad \tau(u)=\kappa u+\varepsilon(u),
\qquad \varepsilon=O(C^{-1}),
\tag{4.1}
\]
and keep the source power \(P=t_0'^2T_{tz}\) fixed as \(C\to\infty\).
This is the same expansion for which the source obtains the quadratic
Schwarzian action and removes its three \(SL(2)\) modes
(`GravityReparametrizationsRevised.tex:680-719`).

⟨1⟩4.⟨2⟩2. **PROVE (retarded soft equation and normalization).** The
Schwarzian and (0.7) linearize to
\[
\operatorname{Sch}(e^{\kappa u+\varepsilon},u)
=-{\kappa^2\over2}+{\varepsilon'''\over\kappa}
 -\kappa\varepsilon'+O(\varepsilon^2),
\tag{4.2}
\]
\[
{C\over\kappa}
(\partial_u^4-\kappa^2\partial_u^2)\varepsilon_R(u)=-P(u).
\tag{4.3}
\]
With
\[
\widetilde f(\omega)=\int_{-\infty}^{\infty}du\,e^{i\omega u}f(u),
\tag{4.4}
\]
the retarded solution is, before taking any late-time limit,
\[
\widetilde\varepsilon_R(\omega)
=-{\kappa\,\widetilde P(\omega)\over
C(\omega+i0)^2[(\omega+i0)^2+\kappa^2]}.
\tag{4.5}
\]
The prescription in (4.5) is understood together with the charge/endpoint
conditions of (2.6), which select the physical member in the exponentially
growing homogeneous \(SL(2)\) sector.  Equations (4.2)–(4.5) are a named
Taylor expansion and Fourier transform of (0.7).  The source prints the
Lorentzian homogeneous solutions \(e^u,e^{-u},u,1\)
(`GravityReparametrizationsRevised.tex:849-879`), so no oscillatory-pole
assumption has been imported.

⟨1⟩4.⟨2⟩3. **PROVE (final-energy subtraction before \(\omega\to0\)).**
At linear order represent the comparison with the final stationary saddle by
\[
P_{\rm sub}(u)=P(u)-\Delta E\,\delta(u-u_f),\qquad
\int P_{\rm sub}=0.
\tag{4.6}
\]
This is a subtraction, not an additional physical kick.  Its first moment
defines
\[
{\cal A}:={1\over C\kappa}\int_{u_i}^{u_f}(u_f-u)P(u)\,du,
\qquad
\widetilde P_{\rm sub}(\omega)
=-i\omega C\kappa{\cal A}+O(\omega^2).
\tag{4.7}
\]
Equations (4.6)–(4.7) are the named Taylor expansion of (4.4), using
\(\Delta E=\int P\) from (1.1).  For a balanced pulse, the answer is
independent of the arbitrary subtraction time because \(\Delta E=0\).

⟨1⟩4.⟨2⟩4. **PROVE (final-value identity).** Equations (4.5)–(4.7) give
\[
\widetilde\varepsilon_{\rm sub}(\omega)
={i{\cal A}\over\omega+i0}+O(\omega^0),\qquad
\varepsilon_{\rm sub}(u\to+\infty)={\cal A}.
\tag{4.8}
\]
Consequently the literal diagonal clock readout of (3.4) has
\[
\boxed{\;
\Delta u_{\rm rel}^{(1)}
=-{ {\cal A}\over2\kappa}
=-{1\over2C\kappa^2}
  \int_{u_i}^{u_f}(u_f-u)P(u)\,du .
\;}
\tag{4.9}
\]
For the balanced two-kick profile
\(P=\Delta E_1[\delta(u)-\delta(u-L)]\), (4.9) gives
\(-\Delta E_1L/(2C\kappa^2)\), equal to the expansion (3.10) because
\(\delta\kappa=\Delta E_1/(C\kappa)+O(C^{-2})\).  For an unbalanced pulse,
\[
\Delta u_{\rm rel}^{(1)}
=-{1\over2C\kappa^2}
  \int_{u_i}^{u_f}(u_f-u)P(u)\,du
\tag{4.10}
\]
after the same final-energy subtraction; an endpoint delta has zero linear
residue, consistently with the quadratic onset (3.13).  These are elementary
moment evaluations of displayed equation (4.9).

⟨1⟩4.⟨2⟩5. **PROVE (the invariant hard vertex).** Directly varying the
two-sided kernel (0.4) with the right perturbation (4.1) gives
\[
{{\delta G_{LR}}\over G_{LR}^{\rm eq}}
=\Delta\,{\cal B}_{LR}[\varepsilon](T),\qquad
{\cal B}_{LR}[\varepsilon](T)
={\varepsilon'(T)\over\kappa}
 -\tanh(\kappa T)\varepsilon(T).
\tag{4.11}
\]
This is the Lorentzian two-sided continuation of the printed invariant
bilocal vertex
\(\varepsilon'_1+\varepsilon'_2
-(\varepsilon_1-\varepsilon_2)/\tan(u_{12}/2)\)
(`GravityReparametrizationsRevised.tex:729-740`).  The source obtains a
four-point response by attaching two such vertices to its Schwarzian
propagator, with coefficient \(1/(2\pi C)\)
(`GravityReparametrizationsRevised.tex:743-753`).

⟨1⟩4.⟨2⟩6. **PROVE (normalized soft response and (T.3)).** Normalize the
soft attachment to the same diagonal time readout as (3.4):
\[
{\cal S}_{\rm Sch}(\omega;P_{\rm sub})
:=(-i\omega)\,
{\widetilde{\cal B}_{LR}[\varepsilon_R](\omega)\over2\kappa}.
\tag{4.12}
\]
The factor \(1/(2\kappa)\) is not fitted: it is
\(\Delta/[-\partial_T\log G_{\rm eq}]\) at late time, using (3.3), and the
factor \(-i\omega\) extracts the step residue.  Since (4.11) tends to
\(-\varepsilon\), (4.8) yields
\[
\boxed{\;
\lim_{T\to\infty}\Delta u_{\rm rel}^{(1)}(T)
=\lim_{\omega\to0}[-i\omega\,
 \widetilde{\delta u}_{\rm rel}^{(1)}(\omega)]
=\lim_{\omega\to0}{\cal S}_{\rm Sch}(\omega;P_{\rm sub})
=-{{\cal A}\over2\kappa}.
\;}
\tag{4.13}
\]
This is the elementary final-value theorem applied to (4.8), after the
Fourier transform and final-energy subtraction have already been performed.
It is independent of the detector dimension \(\Delta\), which cancels between
the vertex and the detector Jacobian.

⟨1⟩4.⟨2⟩7. **PROVE (precise domain of the equality).** Equation (4.13)
**holds at leading one-soft/tree response**, \(O(C^{-1})\), for every compact
source with finite first moment.  It is not an exact finite-amplitude identity
if \({\cal S}_{\rm Sch}\) is defined using only the linear vertex (4.11): the
exact classical plateau is \(-\log a/\kappa_f\) by (3.7), and differs by
\(O(C^{-2})\) for a fixed source.  The unbalanced endpoint kick makes the
distinction explicit: both sides of (4.13) vanish at \(O(C^{-1})\), while
(3.13) is generally nonzero at \(O(C^{-2})\).  This is order counting between
displayed equations (3.13), (4.5), and (4.13).

⟨1⟩4.⟨2⟩8. **PROVE (pulse-width and coupling errors).** Let
\(w=u_f-u_i\), and hold \(P\) and \(w\) fixed while \(C\to\infty\).  Then
\[
\Delta u_{\rm rel}
=-{1\over2C\kappa^2}\int(u_f-u)P(u)\,du
+O(C^{-2}).
\tag{4.14}
\]
At this order (4.14) is exact in \(w\): only the first moment enters.  Replacing
a pulse by a delta at its power centroid preserves both area and first moment,
so its DC residue has no width error at \(O(C^{-1})\); at small nonzero
frequency the next error is \(O((\omega w)^2/C)\) for a centered symmetric
pulse, and \(O(\omega w/C)\) if only its area is matched.  These estimates are
the Taylor remainder of \(\widetilde P(\omega)\) in (4.4).  The \(O(C^{-2})\)
term contains nonlinear multi-soft response and depends on higher pulse
moments; it is not certified by the single propagator/vertex calculation.

⟨1⟩4.⟨2⟩9. **ASSUME [physical argument] (embedding in large-\(p\) SYK).**
In dimensionless thermal-circle conventions, identify the Schwarzian
stiffness with
\[
C_{\rm th}\longleftrightarrow {N\alpha_S\over\beta{\cal J}},
\qquad \alpha_S={1\over4p^2}\quad(p\gg1).
\tag{4.15}
\]
The SYK source prints this coefficient and defines all variables at
`refs/arxiv-2412.14799/Main.tex:59-68`.  It independently evaluates the
microscopic deformation on the full reparametrized saddle family, recovers
the nonlinear Schwarzian coefficient, and states that orthogonal hard
directions are suppressed at large \(N/p^2\)
(`Main.tex:291-311`).  Thus (4.13) embeds as the leading soft-sector
prediction there; finite \(p,N,\beta{\cal J}\) corrections are outside this
tree Schwarzian computation.

## ⟨1⟩5. Verdict

⟨1⟩5.⟨2⟩1. **VERDICT — plateau, protocol (a): YES, generically, but not
source-universally.** The explicit balanced family (2.11) has the nonzero
plateau (3.9), already at \(O(C^{-1})\) when its energy dwell-time moment is
nonzero.  A tuned balanced source with \(a=1\), equivalently zero moment in
(4.9) at leading order, has NO plateau.  This is the exact if-and-only-if
criterion \(a\ne1\) in displayed equation (3.7).

⟨1⟩5.⟨2⟩2. **VERDICT — plateau, protocol (b): YES, generically after the
specified final-energy synchronization, but order-sensitive.** The exact
unbalanced kick (2.10) has (3.12), which is nonzero but starts at
\(O(C^{-2})\); a finite-duration unbalanced event has the \(O(C^{-1})\)
plateau (4.10) when its dwell-time moment is nonzero.  A source with \(a=1\)
has NO plateau.  This is direct application of (3.7), (3.12), and (4.10).

⟨1⟩5.⟨2⟩3. **VERDICT — the butterfly shift itself: NO plateau.** The
Shenker–Stanford translation has \(a=1\), so its detector delay decays as
\(e^{-\kappa_fT}\) by (3.15), in agreement with the printed geodesic factor
\(\alpha e^{-R(t_L+t_R)/(2\ell^2)}\)
(`refs/arxiv-1306.0622/shock.tex:223-234`).  Its surviving statement is
“a transient, boost-enhanced relational time delay,” not stationary-subtracted
memory.

⟨1⟩5.⟨2⟩4. **VERDICT — (T.3): CONDITIONAL.** It **HOLDS** exactly as
(4.13) at leading \(O(C^{-1})\) one-soft/tree response, for compact sources
with finite first moment and with final energy subtracted before
\(\omega\to0\).  It **FAILS as an exact finite-amplitude equality** if the
right side retains only the single invariant vertex and retarded propagator:
the missing terms begin at \(O(C^{-2})\), as the endpoint-kick example
(3.13) proves.  This is the order comparison in ⟨1⟩4.⟨2⟩7.

⟨1⟩5.⟨2⟩5. **VERDICT — operational qualification [physical argument].**
For every \(\Delta>0\), the *absolute* stationary-subtracted difference
\(\delta G_{LR}\) tends to zero, while the normalized correlator ratio and
the calibrated relative clock readout tend to constants when \(a\ne1\), by
(3.7).  Thus the YES above uses the brief's explicit relative-clock criterion;
a stronger definition demanding a nonzero absolute late correlator difference
would return NO for both protocols.

⟨1⟩5.⟨2⟩6. **One-sentence surviving statement suitable for a future row
(not registered here).** At leading large-\(C\) Schwarzian response, a compact
right-boundary power pulse leaves the final-energy-subtracted two-sided
relative-clock shift
\(\Delta u_{\rm rel}=-(2C\kappa^2)^{-1}
\int_{u_i}^{u_f}(u_f-u)P(u)\,du+O(C^{-2})\), equal to the DC residue of the
same invariant bilocal soft attachment, whereas the pure butterfly
translation has zero plateau and decays as \(e^{-\kappa T}\).  This is a
one-sentence restatement of displayed equations (3.15), (4.13), and (4.14).

## ⟨1⟩6. Numeric handshake

⟨1⟩6.⟨2⟩1. **ASSUME (shared numerical conventions).** In this table
\({\cal N}_\Delta=1\), \(\Delta=1\), and every listed number uses the exact
nonlinear readout (3.6) and exact \(\delta G_{LR}\) in (3.2).  Impulses are
compactly supported distributions; an event-driven ODE code should impose
the \(t,t',t''\) matching (2.8).  Equivalently it may integrate
\(T_{tz}=P/t'^2\) with the delta coefficients below; this is displayed
equation (2.9).

| id | \(C,\beta\) | protocol and explicit \(T_{tz}(u)\) | \([u_i,u_f]\) | exact \(g_{\rm rel}=(a,b;c,d)\) | predicted plateau \(-\log a/\kappa_f\) |
|---|---|---|---|---|---|
| A1 | \(100,\,2\pi\) | balanced \(1\to1.1\to1\): \(10.5000000\,\delta(u)-1.64891095412\,\delta(u-1)\) | \([0,1]\) | \((1.05286503580,-0.0909883081018;\ 0.0334727279376,0.946896647924)\) | \(-0.0515150538087\) |
| A2 | \(50,\,\pi\) | balanced \(2\to2.3\to2\): \(8.06250000\,\delta(u)-1.36885338854\,\delta(u-0.5)\) | \([0,0.5]\) | \((1.08148701912,-0.140375094800;\ 0.0516411114295,0.917949875063)\) | \(-0.0391684818398\) |
| B1 | \(100,\,2\pi\) | unbalanced \(1\to1.1\): \(10.5000000\,\delta(u)\) | \([0,0]\) | \((1.00113571871,0.0476731294623;\ 0.0476731294623,1.00113571871)\) | \(-0.00103188569752\) |
| B2 | \(80,\,4\pi\) | unbalanced \(0.5\to0.6\): \(17.6000000\,\delta(u)\) | \([0,0]\) | \((1.00415802209,0.0912870929175;\ 0.0912870929175,1.00415802209)\) | \(-0.00691566901225\) |

Each coefficient is \(\Delta E/t'(s)^2\) from (2.9).  In A1 and A2 the
pre-second-kick derivatives are respectively \(2.52345780917\) and
\(4.85385045516\); hence the unequal positive/negative \(T_{tz}\) coefficients
still give exactly opposite *power* kicks.  This is direct numerical
evaluation of (2.7)–(2.11), not a fit.

⟨1⟩6.⟨2⟩2. **PROVE (finite-time targets).** The values to compare are:

| id | \(T\) | \(\Delta u_{\rm rel}^{\rm NL}(T)\) | \(\delta G_{LR}(T)\) |
|---|---:|---:|---:|
| A1 | 2 | \(-0.0439168663063\) | \(-1.43615624490\times10^{-3}\) |
| A1 | 4 | \(-0.0505127856135\) | \(-3.21934849346\times10^{-5}\) |
| A1 | 8 | \(-0.0514967277827\) | \(-1.10134890247\times10^{-8}\) |
| A2 | 1 | \(-0.0334367183536\) | \(-8.56539591783\times10^{-3}\) |
| A2 | 2 | \(-0.0384152771109\) | \(-1.90891673143\times10^{-4}\) |
| A2 | 4 | \(-0.0391547192603\) | \(-6.52569291811\times10^{-8}\) |
| B1 | 1 | \(-0.0329831010648\) | \(-6.17931010335\times10^{-3}\) |
| B1 | 3 | \(-0.00422674604349\) | \(-1.51531004613\times10^{-5}\) |
| B1 | 6 | \(-0.00114966288269\) | \(-5.65638658713\times10^{-9}\) |
| B2 | 2 | \(-0.105063956171\) | \(-2.76776253804\times10^{-3}\) |
| B2 | 6 | \(-0.0151914003817\) | \(-4.84087396276\times10^{-6}\) |
| B2 | 12 | \(-0.00714189958382\) | \(-1.71236483051\times10^{-9}\) |

Every entry is direct high-precision evaluation of displayed equations
(3.2) and (3.6).  The slow approach of B1/B2 to a small plateau while
\(\delta G_{LR}\) becomes tiny is itself a useful conditioning check.

## ⟨1⟩7. Honesty ledger

⟨1⟩7.⟨2⟩1. **Literature-known in the allowed local sources.**

1. The sourced trajectory equation (0.7), with the Lorentzian-sign caveat,
   is printed at
   `refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:611-623`.
2. The three \(SL(2)\) charges, their two-sided cancellation, their Casimir
   Hamiltonian, and the matter split are printed at
   `GravityReparametrizationsRevised.tex:889-929,955-972`.
3. Reparametrization dressing of arbitrary matter correlators and the
   invariant linear bilocal vertex are printed at
   `GravityReparametrizationsRevised.tex:645-675,729-753`.
4. The shock translation, its equal-side detector, and its late geodesic
   decay factor are printed at
   `refs/arxiv-1306.0622/shock.tex:188-234,275-293`.
5. The controlled large-\(p\) SYK stiffness and nonlinear soft embedding are
   printed at `refs/arxiv-2412.14799/Main.tex:59-68,291-311`.

These five items are quotations/pointers to local TeX, not novelty claims.

⟨1⟩7.⟨2⟩2. **New in this shard.**

1. Equations (2.2)–(2.6) give the closed charge-orbit reconstruction and prove
   that the integrated charges alone miss the stabilizer phase measured by
   the relative clock.
2. Equations (3.2), (3.7), and (3.14)–(3.15) give the exact
   final-energy-subtracted two-sided response and isolate \(a\ne1\) dilation
   memory from the \(a=1\) transient butterfly translation.
3. Equations (4.9) and (4.13) give the normalized leading DC identity with no
   fitted coefficient and expose its first-moment dependence.

Each item is a pointer to a displayed derivation in this shard; no literature
priority beyond the three-source window is asserted.

⟨1⟩7.⟨2⟩3. **Open or conditional.**

1. Whether a ratio of exponentially small correlators is accepted as a
   practically robust permanent record is an operational choice; the exact
   mathematical distinction is recorded in ⟨1⟩5.⟨2⟩5.
2. Equality of the *finite-amplitude* plateau with a soft object requires the
   nonlinear/multi-soft completion omitted from the single vertex (4.11);
   only (4.13) is established.
3. Finite-\(N\), finite-\(p\), finite-\(\beta{\cal J}\), disorder-sample, and
   loop corrections are not computed; (4.15) is only the controlled embedding
   point supplied by `refs/arxiv-2412.14799/Main.tex:291-311`.
4. The charge algebra and possible extension of the full asymptotic
   \(\mathrm{Diff}\), beyond the displayed three \(SL(2)\) charges, are out of
   scope.  The local source itself says that it has discussed neither that
   algebra nor its central charge
   (`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:1167-1172`).

These are explicit fences on the results above, supported respectively by
displayed shard equations or the cited local-source line.
