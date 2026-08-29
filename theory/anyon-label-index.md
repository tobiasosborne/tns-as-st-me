# RESULT — a finite toric-code endpoint has an exact Drinfeld-center label and an exact same-circle TPM shift

**One-sentence theorem.** On every finite square-lattice toric-code torus, a
pure open ribbon of type $x\in\operatorname{Irr}Z(\mathrm{Vec}_{\mathbb Z_2})\cong\mathbb Z_2^e\times\mathbb Z_2^m$ with one endpoint inside a
contractible boundary circle and the other outside obeys
$P_bW_xP_a=\delta_{b,a+x}W_xP_a$, so the enclosed endpoint has the definite
anyon label $x$, the same-circle two-projective-measurement (TPM) flux
increment is exactly $x$, and closed probe ribbons return the nondegenerate
braiding character $(-1)^{x_ey_m+x_my_e}$.

**Status.** The finite toric-code theorem and proof in §§1--3 are **PROVED**
by finite Pauli algebra and were certified at that strength by the capped
review. The doubled-Ising calculation in §4 is
exact fusion arithmetic, but its identification with a chosen microscopic
endpoint tensor is not proved here. The PEPS statement in §5 is deliberately
**SKETCH**, conditional on the displayed exact pulling-through/tube-algebra
hypothesis.

This is a 2+1-dimensional label theorem. It does not alter or repackage any
of the campaign's 1D rows. In particular, the finite-window
offset-cancellation argument of `M-INDEX-fin` is used only as the protocol
design pattern; no current, wall coordinate, scattering limit, or
Gram-inverse conclusion is imported.

## 1. Finite model and protocol registers

### 1.1 Toric-code model

Let

\[
 \Lambda=C_{L_x}\mathbin{\square}C_{L_y},\qquad L_x,L_y\geq3,
\]

be a finite square cellulation of the torus. Put one qubit on each edge and
write $X_j,Z_j$ for its Pauli operators. For every vertex $v$ and plaquette
$p$, define

\[
 A_v:=\prod_{j\ni v}X_j,\qquad
 B_p:=\prod_{j\in\partial p}Z_j,\qquad
 H_{\rm TC}:=-\sum_v A_v-\sum_p B_p.                     \tag{A.1}
\]

A star and plaquette share zero or two edges, so all terms in (A.1) commute.
Let $\Omega$ be any torus ground vector:

\[
 A_v\Omega=B_p\Omega=\Omega\quad\text{for every }v,p.     \tag{A.2}
\]

The two global relations $\prod_vA_v=\prod_pB_p=I$ leave four ground states,
but no choice of logical ground state enters the local theorem.

The anyon label set is the pointed Drinfeld center

\[
 \mathcal A:=\operatorname{Irr}Z(\mathrm{Vec}_{\mathbb Z_2})
 =\{1,e,m,\epsilon\}
 \cong\mathbb Z_2^e\times\mathbb Z_2^m.                  \tag{A.3}
\]

Write $x=(x_e,x_m)$, with $e=(1,0)$, $m=(0,1)$, and
$\epsilon=(1,1)$. Addition in (A.3) is fusion. This group structure is
special to the pointed model and is what makes the difference $b-a$
meaningful below.

### 1.2 Boundary-circle PVM

Choose a proper contractible disk $D\subset\Lambda$, together with compatible
sets of vertices $V(D)$ and plaquettes $P(D)$ in its cellulation. Define

\[
 F_e(D):=\prod_{v\in V(D)}A_v,\qquad
 F_m(D):=\prod_{p\in P(D)}B_p.                            \tag{A.4}
\]

Every interior edge occurs twice in the appropriate product, so these are
closed lattice boundary operators. They commute, are self-adjoint, and
square to $I$. Their joint PVM is

\[
 P_a(D):={1\over4}\bigl(I+(-1)^{a_e}F_e(D)\bigr)
                    \bigl(I+(-1)^{a_m}F_m(D)\bigr),
 \qquad a\in\mathcal A.                                   \tag{A.5}
\]

Thus $F_e$ measures the parity of enclosed electric charge and $F_m$ the
parity of enclosed magnetic charge. Equivalently, the two commuting bits

\[
 \widehat q_D=
 \left({I-F_e(D)\over2},{I-F_m(D)\over2}\right)            \tag{A.6}
\]

take values in the sector lattice $\mathcal A$. Here “lattice” means the
finite torsion group (A.3), not an ordering of four anyon names.

This is the toric-code realization of the general tube-algebra picture in the
local source: minimal central idempotents resolve Drinfeld-center sectors
(`refs/arxiv-2011.12127/TN-Review-main.tex:1595`--`:1597`), the toric-code
idempotents reduce to two binary labels (`:1637`), and the same idempotents
label bulk excitations (`:1642`--`:1649`).

### 1.3 Pure ribbons and endpoint cells

Let $\gamma$ be a direct-lattice path and $\gamma^*$ a dual-lattice path.
Each has one endpoint in $D$ and one in its complement, hence crosses
$\partial D$ once modulo two. Put

\[
 Z(\gamma)=\prod_{j\in\gamma}Z_j,\qquad
 X(\gamma^*)=\prod_{j\pitchfork\gamma^*}X_j,\qquad
 W_x=Z(\gamma)^{x_e}X(\gamma^*)^{x_m}.                    \tag{A.7}
\]

An irrelevant Pauli phase is chosen so that $W_x$ is unitary. For
$x=\epsilon$, a direct and a dual endpoint in the same small endpoint
neighbourhood form the composite ribbon endpoint. “Pure” means that the
single $x$-component (A.7) has been selected. A coherent sum of different
$W_x$ need not have one label and is outside the definite-sector clause.
For $x=1$, $W_1=I$ is the empty/identity ribbon and is not a physical
endpoint. The boundary covariance and TPM shift are invariant under ribbon
deformations that preserve the inside/outside endpoint partition, including
arbitrary extra even crossings; they need not survive moving an endpoint
across $\partial D$ or changing the circle between the two measurements.

### 1.4 Same-circle TPM protocol

For an arbitrary initial density matrix $\rho$, measure the PVM (A.5), apply
the charge-creation ribbon $W_x$, and measure the **same** PVM again. Its
joint law is

\[
 p_x(a,b):=\operatorname{Tr}\!\left[
 P_bW_xP_a\rho P_aW_x^\dagger P_b\right].                 \tag{A.8}
\]

The sector increment is

\[
 \Delta q_D:=b-a\in\mathcal A.                             \tag{A.9}
\]

Using the same finite boundary register twice is load-bearing. It is the
finite-anyon counterpart of the `M-INDEX-fin` mechanism: the two outcomes
belong to the same affine spectral register before their difference is
taken. Here the register already has zero offset and is the fusion group
$\mathcal A$. Equation (A.9) is not spectral arithmetic for a difference of
noncommuting operators.

## 2. Exact finite-lattice selection-rule theorem

### Theorem A-INDEX-TC-fin

Under §§1.1--1.4, for every $a,b,x\in\mathcal A$:

1. **Definite endpoint sector.** The ribbon has exact boundary covariance

   \[
    F_eW_x=(-1)^{x_e}W_xF_e,\qquad
    F_mW_x=(-1)^{x_m}W_xF_m,                              \tag{A.10}
   \]

   and hence

   \[
    P_bW_xP_a=\delta_{b,a+x}W_xP_a.                       \tag{A.11}
   \]

   In particular,
   $P_bW_x\Omega=\delta_{b,x}W_x\Omega$: the enclosed string endpoint is in
   the definite Drinfeld-center sector $x$.

2. **TPM sector quantization.** The law (A.8) is a probability distribution
   supported on

   \[
    \{(a,b):b=a+x\}.                                      \tag{A.12}
   \]

   Consequently every run has the group-valued outcome
   $\Delta q_D=x\in\mathbb Z_2^e\times\mathbb Z_2^m$. Starting from any
   ground state, $p_x(1,x)=1$.

3. **Braiding readout.** A closed probe ribbon of type $y=(y_e,y_m)$ around
   the circle can be represented by

   \[
    L_y(D):=F_m(D)^{y_e}F_e(D)^{y_m},                     \tag{A.13}
   \]

   and obeys

   \[
    L_yW_x=(-1)^{x_ey_m+x_my_e}W_xL_y.                    \tag{A.14}
   \]

   The pairing in (A.14) is nondegenerate, so the two measured bits
   distinguish all four sectors.

The theorem is finite-volume and exact. It assumes neither a thermodynamic
limit nor a PEPS approximation.

## 3. Full proof of A-INDEX-TC-fin

### ⟨1⟩1. Endpoint stabilizer algebra

**⟨2⟩1.** $Z(\gamma)$ anticommutes with $A_v$ exactly at the two direct-path
endpoints and commutes with every $B_p$.

*Justification.* A path enters and leaves every internal vertex, so its
support overlaps the corresponding star in zero or two edges. At either
endpoint the overlap is one edge. The Pauli relation $XZ=-ZX$ gives the two
minus signs. Every $B_p$ is $Z$-type and therefore commutes with
$Z(\gamma)$.

**⟨2⟩2.** $X(\gamma^*)$ anticommutes with $B_p$ exactly at the two dual-path
endpoints and commutes with every $A_v$.

*Justification.* The same parity argument on the dual cellulation applies;
now the single-overlap relation is $ZX=-XZ$. Both $X(\gamma^*)$ and the
stars are $X$-type.

**⟨2⟩3.** Multiplying the star identities of ⟨2⟩1 over $V(D)$ and the
plaquette identities of ⟨2⟩2 over $P(D)$ leaves exactly one endpoint sign in
each active component and proves (A.10).

*Justification.* By hypothesis each active path has one endpoint in $D$ and
one outside. All interior incidences cancel modulo two. Raising the two
strings to $x_e,x_m\in\mathbb Z_2$ gives the displayed exponents.

### ⟨1⟩2. Projector selection rule and definite label

**⟨2⟩1.** For $s\in\{e,m\}$, (A.10) implies

\[
 \bigl(I+(-1)^{b_s}F_s\bigr)W_x
 =W_x\bigl(I+(-1)^{b_s+x_s}F_s\bigr).                    \tag{A.15}
\]

*Justification.* Move $F_s$ through $W_x$ using (A.10); addition of binary
labels is modulo two.

**⟨2⟩2.** Multiplying the two equations (A.15) and using (A.5) gives

\[
 P_bW_x=W_xP_{b-x}.                                      \tag{A.16}
\]

*Justification.* $F_e$ and $F_m$ commute, so their two spectral factors may
be multiplied. In $\mathbb Z_2^2$, subtraction and addition agree, but the
subtraction in (A.16) shows which projector was transported.

**⟨2⟩3.** Right multiplication by $P_a$ proves (A.11).

*Justification.* The PVM is orthogonal:
$P_{b-x}P_a=\delta_{b-x,a}P_a$, equivalently
$\delta_{b,a+x}P_a$.

**⟨2⟩4.** Equations (A.2) and (A.4) give
$P_a\Omega=\delta_{a,1}\Omega$; inserting this in (A.11) gives
$P_bW_x\Omega=\delta_{b,x}W_x\Omega$.

*Justification.* Every factor in both products (A.4) has eigenvalue $+1$ on
a ground vector. This proves the definite endpoint-sector clause.

### ⟨1⟩3. TPM support and normalization

**⟨2⟩1.** Every number $p_x(a,b)$ in (A.8) is nonnegative.

*Justification.* It is the trace of
$K_{a,b}\rho K_{a,b}^\dagger$, with $K_{a,b}=P_bW_xP_a$.

**⟨2⟩2.** Equation (A.11) makes $p_x(a,b)=0$ unless $b=a+x$.

*Justification.* Outside that support the Kraus operator $K_{a,b}$ is zero
before any property of $\rho$ is used.

**⟨2⟩3.** Summing (A.8) over $a,b$ gives one.

*Justification.* Sum first over $b$, use $\sum_bP_b=I$, cyclicity of trace,
and $W_x^\dagger W_x=I$. The result is
$\sum_a\operatorname{Tr}(P_a\rho P_a)=\operatorname{Tr}\rho=1$. No
commutation of $\rho$ with the first measurement is assumed.

**⟨2⟩4.** On the support from ⟨2⟩2,
$\Delta q_D=b-a=x$ in the actual fusion group $\mathcal A$.

*Justification.* This is group arithmetic only after the two same-register
PVM outcomes have been obtained. For
$\rho=|\Omega\rangle\langle\Omega|$, ⟨1⟩2.⟨2⟩4 fixes $a=1$, hence $b=x$
with unit probability. This proves the TPM clause.

### ⟨1⟩4. Braiding character

**⟨2⟩1.** The factor $F_m^{y_e}$ in (A.13) contributes
$(-1)^{x_my_e}$ when moved through $W_x$.

*Justification.* $F_m$ is a closed $Z$-type boundary string. It commutes
with the $Z$-component of $W_x$ and has odd intersection with its active
dual $X$-string exactly when $x_m=y_e=1$.

**⟨2⟩2.** The factor $F_e^{y_m}$ contributes $(-1)^{x_ey_m}$.

*Justification.* This is the direct/dual exchange of ⟨2⟩1: the closed
$X$-type boundary string detects the active open $Z$-string.

**⟨2⟩3.** The two factors commute, so their signs multiply and give (A.14).

**⟨2⟩4.** If $x\neq1$, choose $y=m$ when $x_e=1$, and choose $y=e$
otherwise. Then the exponent in (A.14) is one.

*Justification.* Every nontrivial $x$ is detected by some probe; hence the
pairing is nondegenerate. This completes the proof. □

## 4. Non-abelian instance: doubled Ising

**Status: exact fusion-algebra instance; microscopic string-net operator
identification remains SKETCH.**

Let Ising have simple objects $1,\psi,\sigma$ and fusion rules

\[
 \psi\otimes\psi=1,\qquad \psi\otimes\sigma=\sigma,\qquad
 \sigma\otimes\sigma=1\oplus\psi.                         \tag{A.17}
\]

The Levin--Wen model with Ising input has bulk category
$Z(\mathrm{Ising})$, the doubled-Ising theory. Since Ising is modular, its
simples can be written $(r,\bar s)$ with componentwise fusion. Choose

\[
 x=(\sigma,\bar1),\qquad a=(\sigma,\bar1).                \tag{A.18}
\]

Then the exact bulk fusion rule is

\[
 x\otimes a=(1,\bar1)\oplus(\psi,\bar1).                  \tag{A.19}
\]

Thus a pure $x$-endpoint is a definite non-abelian anyon, but if it is fused
with the pre-existing sector $a$, a boundary-circle measurement can return
either

\[
 b_1=(1,\bar1),\qquad b_2=(\psi,\bar1),                   \tag{A.20}
\]

with a one-dimensional channel
$\mu_i\in\operatorname{Hom}(b_i,x\otimes a)$ in each branch. The exact fine
datum is

\[
 (x,a\longrightarrow b_i;\mu_i),                         \tag{A.21}
\]

not a quotient $b_i/a$. The two different outputs in (A.20) are the explicit
obstruction to subtracting Drinfeld-center names.

There is nevertheless a group-valued shadow. The universal grading of Ising
is $\mathbb Z_2$, with $1,\psi$ even and $\sigma$ odd, hence

\[
 U(Z(\mathrm{Ising}))\cong\mathbb Z_2\times\mathbb Z_2.  \tag{A.22}
\]

For (A.18)--(A.20),

\[
 |x|=|a|=(1,0),\qquad |b_1|=|b_2|=(0,0),\qquad
 |b_i|-|a|=(1,0)=|x|.                                    \tag{A.23}
\]

Equation (A.23) is the universal-grading shadow of the fine fusion event. It
conserves a coarse parity but does not choose between the two channels. No
probability or nonzero amplitude is fixed by (A.17)--(A.23).

The local tensor-network source supports only the categorical input used
here: MPO blocks have nonnegative integral fusion rules and zipper/pulling-
through tensors
(`refs/arxiv-2011.12127/TN-Review-main.tex:1308`--`:1334`), and the anyon
fusion category is the Drinfeld-center output (`:1642`--`:1666`). It does
not by itself identify a microscopic operator with the pure endpoint
(A.18), so that physical step is not promoted here.

## 5. Model-general statement — SKETCH under exact PEPS pulling-through

### Displayed hypothesis (PT)

Let $\mathcal C$ be a finite unitary fusion category and let a finite
MPO-injective PEPS lattice model supply all of the following exact data:

1. **(PT1: tube PVM)** An annular representation of
   $\operatorname{Tub}(\mathcal C)$ whose minimal central idempotents
   $\{P_a\}_{a\in\operatorname{Irr}Z(\mathcal C)}$ are mutually orthogonal
   and sum to the identity on the chosen boundary-circle register.
2. **(PT2: pure endpoint)** A small-circle resolution of the endpoint tensor
   $T_x$ such that $P_y^{\rm end}T_x=\delta_{y,x}T_x$ for one simple
   $x\in\operatorname{Irr}Z(\mathcal C)$. A sum over $x$ is not called a
   pure endpoint.
3. **(PT3: pulling-through module action)** Exact zipper, associator, and
   pulling-through equations identify the large-circle action of $T_x$ on a
   source sector $a$ with the semisimple decomposition

   \[
    x\otimes a\cong
    \bigoplus_b\operatorname{Hom}(b,x\otimes a)\otimes b. \tag{A.24}
   \]

4. **(PT4: protocol instrument)** The physical charge-creation operation is
   supplied either as a normalized family of channel-resolved Kraus maps
   $T_{x,\mu}$, or the experiment is explicitly conditioned on the success
   of one displayed Kraus map. Category data alone do not provide its
   normalization or probabilities.

The physical motivation and typing of (PT) are recorded locally: pulling
through represents PEPS tensor symmetries
(`refs/arxiv-2011.12127/TN-Review-main.tex:1324`--`:1338`), and the tube
$C^*$-algebra central idempotents give Drinfeld-center sectors
(`:1591`--`:1600`). These references motivate the hypotheses; they do not
replace them.

### SKETCH A-INDEX-PEPS

Under (PT), the following selection rule holds on the declared finite annular
register:

\[
 \boxed{P_bT_{x,\mu}P_a=0\quad\text{unless}\quad
        \mu\in\operatorname{Hom}(b,x\otimes a),\quad
        N_{xa}^b>0.}                                      \tag{A.25}
\]

The endpoint datum is the definite anyon $x$; after interaction with an
enclosed source $a$, the fine transition datum is

\[
 \operatorname{Ind}_{\rm any}(T;x,a\to b)
   =(x,a\to b;\mu).                                       \tag{A.26}
\]

For the same-circle tube-PVM protocol, the joint weight

\[
 p_x(a,b,\mu)=\operatorname{Tr}\!\left(
 P_bT_{x,\mu}P_a\rho P_aT_{x,\mu}^\dagger P_b\right)      \tag{A.27}
\]

is supported only on the fusion events (A.25). Under the normalization clause
in (PT4), these weights sum to one; under postselection they are divided by
their displayed total success probability. Hence the outcomes are quantized
in the discrete Drinfeld-center sector set and its fusion spaces.

*Algebraic derivation.* By (A.24), $T_xP_a$ has no component outside the
direct sum of $b$'s with $N_{xa}^b>0$; applying the orthogonal idempotent
$P_b$ proves (A.25). Resolving the multiplicity factor gives $\mu$, and
inserting the zero block in (A.27) proves its support statement. The missing
model-general step is precisely the physical implication from a microscopic
finite PEPS/ribbon construction to (PT2)--(PT4), so the statement remains
SKETCH rather than being advertised as an unconditional theorem about all
topological phases.

If $x$ is invertible, tensoring by $x$ is an equivalence and sends simple
$a$ to the unique simple $b=x\otimes a$. The supplied label

\[
 \operatorname{Ind}_{\rm inv}
 =x\in\operatorname{Inv}(Z(\mathcal C))                  \tag{A.28}
\]

is then group-valued. The toric-code theorem is the case in which every
simple is invertible and (A.28) is the full $e$-$m$ lattice.

For non-invertible $x$, there need not be a unique $b$. Present the universal
grading group $U(Z(\mathcal C))$ by the fusion relations $[c]=[r][s]$
whenever $N_{rs}^c>0$. Every allowed event in (A.25) then obeys

\[
 |b|=|x||a|,\qquad |b||a|^{-1}=|x|.                      \tag{A.29}
\]

This is the maximal group-grading shadow compatible with all channels, but it
is not the fine label and does not authorize subtraction in
$\operatorname{Irr}Z(\mathcal C)$. Doubled Ising (A.19) is the explicit
branching instance.

### Scope fences

- The theorem uses bulk Drinfeld-center labels because the boundary circle is
  in the 2D bulk. A physical edge or condensate requires its own module or
  boundary excitation category; bulk anyons may then condense, identify, or
  split.
- Tube projectors select sectors. They do not supply a current operator, a
  Ward identity, a Gram inverse, a transition amplitude, or a persistence
  theorem.
- Only in a pointed/invertible sector is $b-a$ defined. In the non-abelian
  case the retained object is (A.26), with (A.29) as a coarse shadow.
- This is one 2+1D selection-rule statement. It is not an omnibus packaging
  of `S-IDX-G-label`, `M-INDEX-fin`, and a PEPS theorem; those results
  consume different hypotheses and remain separate.

## 6. Exact checker

The checker performs finite Pauli algebra on a $4\times4$ torus. It verifies
the stabilizer rank and four-dimensional ground register, all four exact
endpoint syndromes, the two boundary-sector bits, the complete $4\times4$
braiding table, and the same-circle TPM support over every initial sector and
every ribbon type using exact rational weights.

Green command:

```bash
python3 -O theory/checks/anyon_label_check.py
```

Registered red command:

```bash
python3 -O theory/checks/anyon_label_check.py --red wrong-sector
```

The red mode falsely identifies an electric ribbon as magnetic in the TPM
selection rule; the computed boundary commutators are unchanged and the
protocol gate exits nonzero. The checker contains no bare `assert` and is
optimization-safe. Passing it certifies only the displayed finite toric-code
arithmetic; the proof above carries the theorem, and it supplies no evidence
for the model-general (PT) hypothesis.

## 7. MERGE PROPOSALS

1. **New 2+1D claim row.** Add `A-INDEX-TC-fin` at `PROVED`: on a finite
   toric-code torus, a pure open ribbon $W_x$ crossing a fixed contractible
   boundary circle once obeys (A.11); its endpoint has definite
   $x\in\mathbb Z_2^e\times\mathbb Z_2^m$, the same-circle TPM increment is
   $x$, and (A.14) gives the braiding character. Point to §§2--3 and checker
   gates `ANYON-C1`--`ANYON-C4`; the capped review is complete.
2. **Non-abelian companion row.** Add `A-INDEX-PEPS` only at `SKETCH`,
   with (PT1)--(PT4) displayed verbatim: the fine outcome is the fusion event
   $(x,a\to b;\mu)$; invertible $x$ gives an
   $\operatorname{Inv}(Z(\mathcal C))$ index and general $x$ gives only the
   universal-grading shadow (A.29). Cite doubled Ising (A.19) as the branching
   example.
3. **Protocol cross-reference, not a merge.** A companion discussion may note
   that `M-INDEX-fin` and (A.8) both measure the same finite register twice
   before forming an allowed difference. Do not make either result a
   corollary of the other.
4. **Binding non-edits.** Make no change to `S-IDX-G-label`,
   `M-INDEX-fin`, or any other 1D claim row. Do not introduce a naive
   difference of Drinfeld-center simple labels and do not package the three
   mechanisms under one theorem.

No existing file is edited and no merge is performed by this work order.
