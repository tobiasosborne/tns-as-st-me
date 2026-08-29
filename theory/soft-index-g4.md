# G4 — the soft index as a superselection-label difference

**PARTIAL (sector-label/integrality half of S-IDX-fin, plus the FIN.8
zero-mode anchor, recovered for general compact Lie `G`; FIN.1--FIN.3 are
NOT recovered).**

**Self-status.**  The positive statements below are proved as a proposer
proof, but any new CLAIMS row remains **SKETCH** until the capped PRD critic
round.  This shard takes only the symmetry/superselection route: no root
`sl_2`, no ladder-operator calculation, no weight-sector inventory, and no
moment-map argument.

## 1. Setup

### ⟨1⟩1. The effective central charge lattice

**ASSUME.**  Let `G` be a compact Lie group, not necessarily connected, with
finite-dimensional on-site unitary representation `u`; let a periodic ring of
`N` sites carry a finite-range `G`-invariant Hamiltonian `H_N`.  Fix a vacuum
label `α` of D2(a), its unbroken subgroup `H_α`, its centre, and its connected
central torus

\[
 Z_α:=Z(H_α),\qquad T_α:=Z_α^0.
\]

Only a nonzero Lie-algebra component can create a soft leg.  Thus finite
groups are not soft-theorem instances.  A zero-dimensional centre can still
supply a finite (torsion) selection label, but it supplies no circle integer;
if the selected broken component has trivial central character, this route
returns the zero label and no nontrivial index.

**PROVE.**  The conserved finite-ring sectors of the effective action of
`Z_α` form an affine torsor over its character group, and differences of
sector labels lie in that lattice.

**⟨2⟩1.**  A scalar on-site rotation is invisible to conjugation.  Define

\[
 K_u:=\{z\in Z_α:u(z)\in U(1)\mathbf1\},\qquad
 Z_{α,\mathrm{eff}}:=Z_α/K_u .                              \tag{G4.1}
\]

The physical finite-ring action of `Z_α` is honest.  Every element of `K_u`
acts by one common scalar on the whole ring, so all occupied `Z_α` characters
have the same restriction to `K_u`.  They therefore form an affine torsor;
the ratio of any two occupied labels is trivial on `K_u` and is an honest
character in

\[
 \Lambda_α^*:=\widehat{Z_{α,\mathrm{eff}}}
       =\operatorname{Hom}(Z_{α,\mathrm{eff}},U(1)).          \tag{G4.2}
\]

This discrete abelian group consists of the free character lattice of
`Z_{α,eff}^0` together with a possible finite torsion part.

*Justification.*  This is the same scalar-quotient discipline as D4(b): states
see scalar symmetry actions trivially.  All irreducible representations of a
compact abelian group are characters.  If `u(z)=s(z)I` on one site, then
`U_N(z)=s(z)^NI`; hence every occupied character restricts to `s^N` on
`K_u`.  That common offset cancels from a ratio, exactly as the fixed-window
offset cancels in M-INDEX-fin ⟨1⟩5.⟨2⟩3.

**⟨2⟩2.**  Equivalently, and without choosing a global lift, take any
one-parameter central direction with Hermitian one-site generator `C_η` such
that

\[
 e^{2\pi iC_η}=e^{2\pi i\kappa_η}\mathbf1 .                 \tag{G4.3}
\]

Then

\[
 \operatorname{spec}C_{η,N}\subset N\kappa_η+\mathbb Z,
 \qquad C_{η,N}:=\sum_{x=1}^N C_{η,x}.                       \tag{G4.4}
\]

Thus two eigen-sectors have an integer difference even when neither label is
itself an integer.

*Justification.*  D26(INT) and the finite-dimensional spectral calculation of
M-INDEX-fin ⟨1⟩1, with no spatial window: (G4.3) implies
`spec C_η⊂κ_η+ℤ`, and sums of the commuting on-site spectra give (G4.4).

**⟨2⟩3.**  Intrinsically, evaluating `χ∈Λ_α^*` on a cocharacter
`η:U(1)→Z_{α,eff}^0` gives

\[
 \chi(η(e^{i\theta}))=e^{i n_η(\chi)\theta},\qquad
 n_η(\chi)\in\mathbb Z.                                    \tag{G4.5}
\]

The collection of integers `n_η(χ)` is the coordinate-free content of
membership in the character lattice.  No basis of weights, Weyl chamber, or
root inventory has been chosen.

*Justification.*  The composite `χ∘η` is a continuous character of `U(1)`;
all such characters are `e^{iθ}↦e^{inθ}` with `n∈ℤ`.

**⟨2⟩4. QED.**

### ⟨1⟩2. The charge-created soft component

**ASSUME.**  Complexify only to select a one-dimensional central-character
component of the represented Lie algebra.  Let `X∈𝔤_ℂ` obey

\[
 u(z)q(X)u(z)^\dagger=q(\operatorname{Ad}_zX)
   =\chi_X(z)q(X)\quad(z\in Z_α),\qquad
 \chi_X\in\Lambda_α^*.                                    \tag{G4.6}
\]

Let

\[
 Q_X:=\sum_xq_x(X),\qquad J_X:=\sum_xj_{x\mid x+1}(X)       \tag{G4.7}
\]

be the zero-mode charge and zero-mode cut current, extended complex-linearly
from D10.  Write `Π_γ` for the finite-ring spectral projector onto an occupied
`Z_α` character `γ` (or for the corresponding joint projector after choosing
central circle generators).  The character `χ_X` is inflated from
`Z_{α,eff}` to `Z_α`, so it is trivial on `K_u`.

**PROVE.**  `Q_X` and `J_X` have the same central character `χ_X`.

**⟨2⟩1.**  On-site covariance gives

\[
 U_N(z)Q_XU_N(z)^\dagger=\chi_X(z)Q_X.                      \tag{G4.8}
\]

*Justification.*  Equation (G4.6), summed over the ring.  This is
representation covariance, not a decomposition into weights.

**⟨2⟩2.**  The D10 current is linear in `q(X)` and the bond Hamiltonians are
`G`-invariant, hence

\[
 U_N(z)J_XU_N(z)^\dagger=\chi_X(z)J_X.                      \tag{G4.9}
\]

*Justification.*  For each cut,
`j(X)=-[H,Σ_{y≤m}q_y(X)]`.  Conjugate this identity by `U_N(z)`, use
`U_N(z)HU_N(z)^†=H`, and apply (G4.6).  Summation preserves the character.

**⟨2⟩3.**  Global `G` invariance also gives

\[
 [H_N,Q_X]=0.                                               \tag{G4.10}
\]

*Justification.*  Differentiate `U_N(g)H_NU_N(g)^†=H_N` in the `X`
direction and extend complex-linearly.

**⟨2⟩4. QED.**

## 2. Proof ladder

### ⟨1⟩3. THEOREM G4-S-IDX-label (finite-volume soft-sector index)

**ASSUME.**  The setup of ⟨1⟩1--⟨1⟩2.  Let `γ` be an occupied `Z_α`
character in the affine sector torsor and let `Π_γ` be its orthogonal
projector.  Let the selected
component `X` satisfy (G4.6), and let `Q_X`, `J_X` be nonzero on the vectors to
which they are applied.

**PROVE.**  The following exact finite-volume operator block identities hold:

\[
 \boxed{\Pi_\delta Q_X\Pi_\gamma
 =\begin{cases}Q_X\Pi_\gamma,&\delta=\gamma\chi_X,\\0,&
 \delta\ne\gamma\chi_X,\end{cases}}                         \tag{G4.11}
\]

\[
 \boxed{\Pi_\delta J_X\Pi_\gamma
 =\begin{cases}J_X\Pi_\gamma,&\delta=\gamma\chi_X,\\0,&
 \delta\ne\gamma\chi_X.\end{cases}}                       \tag{G4.12}
\]

Consequently the charge-created soft datum is the difference of the target
and source labels,

\[
 \boxed{\operatorname{ind}_{Z_α}(X;\gamma)
 :=(\gamma\chi_X)\gamma^{-1}=\chi_X\in\Lambda_α^*.}          \tag{G4.13}
\]

For every central scalar-period circle `η`, its numerical component is

\[
 \Delta q_η=n_η(\chi_X)\in\mathbb Z.                         \tag{G4.14}
\]

This result is independent of `N`, the hard vector inside `Π_γ`, the
Hamiltonian couplings, and any inventory of scattering channels.

**⟨2⟩1.**  If `ψ=Π_γψ`, then for every `z∈Z_α`,

\[
 U_N(z)Q_Xψ=\chi_X(z)\gamma(z)Q_Xψ,
 \qquad
 U_N(z)J_Xψ=\chi_X(z)\gamma(z)J_Xψ.                          \tag{G4.15}
\]

*Justification.*  Move `U_N(z)` through `Q_X` or `J_X` using (G4.8) or
(G4.9), then use `U_N(z)ψ=γ(z)ψ`.  On `K_u`, `χ_X=1`, so the common scalar
restriction of the source and target labels agrees.

**⟨2⟩2.**  Distinct central characters are orthogonal.  Hence (G4.15) lies
entirely in the `γχ_X` block and has zero projection onto every other block.

*Justification.*  Haar orthogonality, equivalently the spectral theorem for
the commuting central action.  One may write
`Π_δ=∫_{Z_α}overline{δ(z)}U_N(z)dz`; substituting
(G4.15) gives zero unless `δ=γχ_X`.  This proves (G4.11)--(G4.12).

**⟨2⟩3.**  Dividing the target label `γχ_X` by the source label `γ` gives
(G4.13).  Evaluation on a cocharacter gives (G4.14).

*Justification.*  Group cancellation in the affine label torsor, followed by
⟨1⟩1.⟨2⟩3.  This is the direct transplant of M-INDEX-fin's mechanism: the
offset is present in each label and absent from their difference.

**⟨2⟩4.**  `H_N` commutes with the central action, so it preserves every
`Π_γ`.  The label difference therefore cannot change under finite-volume
dynamics.

*Justification.*  `G` invariance of `H_N`; functional calculus of the compact
torus action.  No channel projector or completeness statement occurs.

**⟨2⟩5. QED.**

**LD-ID analogue.**  Equation (G4.13) is not a new dynamical observable: it
is the grade of the charge-created vector under the already conserved central
symmetry.  In the same sense that LD-ID identifies the window charge with the
lift of D13(c)'s conserved sector datum, G4 identifies the soft label with the
ratio of two conserved central-sector labels.  The analogy stops at the
label: no infinite-volume charge operator or scattering amplitude is
constructed here.

### ⟨1⟩4. COROLLARY G4-ADLER-Q0 (general-`G` pure zero-mode anchor)

**ASSUME.**  The setting of ⟨1⟩3.  Let `ψ_h` be an exact hard-band vector,
`H_Nψ_h=E_hψ_h`, with `Q_Xψ_h≠0`.  Compare the interacting propagation of
the *pure* zero-mode-created vector `Q_Xψ_h` with the free reference that
assigns zero energy to the global symmetry mode, exactly as in S-IDX-fin
FIN.8.  Assume the row denominator is nonzero.

**PROVE.**

\[
 \boxed{\mathcal R_{Q_X\psi_h}(0)=1}                         \tag{G4.16}
\]

for every finite `N` and every compact Lie `G` in this setup.

**⟨2⟩1.**  From (G4.10),
`e^{-iH_NT}Q_Xψ_h=Q_Xe^{-iH_NT}ψ_h=e^{-iE_hT}Q_Xψ_h`.

*Justification.*  Exact global symmetry conservation; no limiting argument.

**⟨2⟩2.**  The free zero-mode row has precisely the same phase and vector, so
the normalized interacting/free pairing is one.

*Justification.*  The stated readout definition and ⟨2⟩1.  As in
soft-index-r2.md ⟨1⟩4, this says nothing about a running nonzero-soft-momentum
family or its soft limit.

**⟨2⟩3. QED.**

### ⟨1⟩5. THEOREM G4-SPLIT (exact boundary of the route)

**ASSUME.**  The hypotheses of ⟨1⟩3.  Put

\[
 D_\gamma:=Q_X\Pi_\gamma,
 \qquad P_{D,\gamma}:=\text{orthogonal projector onto }
 \operatorname{ran}D_\gamma .                              \tag{G4.17}
\]

`P_{D,γ}` is the general-`G` analogue of the descendant-range projector in
FIN.1, whereas `Π_{γχ_X}` is only the conserved central-sector projector.

**PROVE.**  Superselection gives

\[
 \operatorname{ran}D_\gamma\subseteq
 \operatorname{ran}\Pi_{\gamma\chi_X},\qquad
 P_{D,\gamma}\leq\Pi_{\gamma\chi_X},                        \tag{G4.18}
\]

but it does not determine `P_{D,γ}J_XΠ_γ`, and therefore does not imply any
general-`G` version of FIN.1, FIN.2, or FIN.3.

**⟨2⟩1.**  Inclusion (G4.18) is (G4.11).  Equality would assert that every
vector in the target central sector is a global-charge descendant.  No
superselection statement says this.

*Justification.*  (G4.11) fixes only the target block.  It gives no rank,
multiplicity, or range-completeness information about `D_γ`.

**⟨2⟩2.**  The missing information is not a cosmetic coefficient.  Consider
abstractly one source line of character `γ` and a two-dimensional target
space on which the torus acts with the single character `γχ_X`.  The maps

\[
 Dψ=e_1,\qquad Jψ=a e_1+b e_2                              \tag{G4.19}
\]

obey exactly the same source/target superselection law for every `a,b`, while
`P_DJψ=a e_1` ranges over inequivalent answers.  Labels cannot see `a`, `b`,
or the orthogonal direction `e_2`.

*Justification.*  Direct finite-dimensional construction.  It is an
information-separation witness, not a counterexample to the SU(2) theorem.

**⟨2⟩3.**  In S-IDX-fin, FIN.1 uses the strictly finer projector onto
`ran D_{λ,N}` and the positive inverse
`(D_{λ,N}^†D_{λ,N})^{-1}`; FIN.2 uses a still finer highest-weight source
projector; FIN.3 uses a current matrix element and a band velocity.  None of
these objects is determined by the character `χ_X` or by the affine sector
labels.

*Justification.*  Compare soft-index-r2.md (FIN.1)--(FIN.3).  The G4 input
contains no multiplicity-space theorem and no relation between the two
intertwiners `D_γ` and `J_XΠ_γ`.  Supplying such a relation would leave the
superselection route and enter one of the other parallel strategies.

**⟨2⟩4.**  Therefore the exact recovered half of S-IDX-fin is:

1. the charge-created and current-created vectors lie in one conserved target
   sector;
2. the soft datum is the integral label difference (G4.13)--(G4.14); and
3. the pure zero-mode anchor FIN.8 generalizes exactly by (G4.16).

The unrecovered half is the projected-current operator content
FIN.1--FIN.2 and its primitive-band residue FIN.3.  In particular, G4 does
not derive the number `2`, the inverse Gram operator, removal of a
highest-weight projector, or the velocity residue.

*Justification.*  ⟨1⟩3--⟨1⟩4 versus ⟨2⟩1--⟨2⟩3.

**⟨2⟩5. QED.**

## 3. SU(2) reduction

### ⟨1⟩6. Reduction to the S-IDX-fin charge labels

**ASSUME.**  Take `G=SU(2)`, the ferromagnetic vacuum with
`H_α=U(1)`, central generator `C=S^z`, and selected component `X=S^-`.

**PROVE.**  G4 reduces to the weight-label consequence of S-IDX-fin and to
FIN.8, but not to FIN.1--FIN.3.

**⟨2⟩1.**  On one spin-`S` site,
`e^{2πiS^z}=e^{2πiS}\mathbf1`, so a ring sector lies in
`NS+ℤ`.  The central character of `S^-` evaluates to `-1`; hence

\[
 \Pi_{m-1}S^-\Pi_m=S^-\Pi_m,
 \qquad \Pi_{m-1}J^-_0\Pi_m=J^-_0\Pi_m.                    \tag{G4.20}
\]

*Justification.*  (G4.3)--(G4.5) and (G4.11)--(G4.12).  This uses the circle
character only, not an `SU(2)` ladder norm.

**⟨2⟩2.**  On the `n`-magnon sector `m=NS-n`, (G4.13) is the integer
label difference `-1`.  The common offset `NS mod ℤ` cancels.

*Justification.*  (G4.13)--(G4.14).  This is the direct analogue of the
fixed-window coset cancellation in M-INDEX-fin.

**⟨2⟩3.**  S-IDX-fin's `P_{λ,N}` is the projector onto
`ran(S^-|_{\mathcal H_{λ,N}})`, not the full weight projector `Π_{m-1}`.
Thus (G4.20) is strictly coarser than FIN.1 whenever the target weight block
contains non-descendant multiplicity.  Even when the two ranges happen to
coincide in a primitive sector, labels alone do not supply the operator
coefficient or FIN.3's current residue.

*Justification.*  G4-SPLIT and the definitions in soft-index-r2.md ⟨1⟩3.

**⟨2⟩4.**  Since `[H_N,S^-]=0`, G4-ADLER-Q0 becomes exactly FIN.8 for the pure
zero-mode-created row.

*Justification.*  G4-ADLER-Q0 and soft-index-r2.md ⟨1⟩4.

**⟨2⟩5.**  The checker cross-check uses the same finite rings and conventions
as `soft_index_r2_check.py` SIDXR2-C2.  At `N=4`, `h=π/2`, and
`S=1/2,1,3/2`, it reproduces respectively

\[
 (m,\|S^-|h\rangle\|^2,
  -i\langle h|(S^-)^\dagger P J^-_0|h\rangle)
 =(1,2,2),(3,6,4),(5,10,6),                                \tag{G4.21}
\]

while separately checking the label shift `m↦m-1`.  The numbers in (G4.21)
are a regression cross-check of the existing SU(2) theorem, not consequences
of G4's character argument.

*Justification.*  `theory/checks/soft_index_g4_check.py`, gate G4-C4, importing
the exact helper matrices of `theory/checks/soft_index_r2_check.py`.

**⟨2⟩6. QED.**

## 4. Non-SU(2) instance: the fundamental SU(3) ferromagnet

### ⟨1⟩7. Exact four-site instance

**ASSUME.**  Let `G=SU(3)` act in its fundamental representation on
`ℂ^3` with colour basis `|0⟩,|1⟩,|2⟩`.  On the `N=4` periodic ring take

\[
 H_4=\sum_{x=0}^{3}(\mathbf1-P_{x,x+1}),                    \tag{G4.22}
\]

where `P` swaps neighbouring colours.  The product vacuum
`Ω=|0,0,0,0⟩` has stabiliser `H_α=S(U(1)\times U(2))`.  Select its effective
central circle generator and one broken complex component

\[
 C={1\over3}\operatorname{diag}(2,-1,-1),
 \qquad X=|1\rangle\langle0|.                               \tag{G4.23}
\]

Put `C_4=Σ_xC_x`, `Q_X=Σ_xX_x`, and form `J_X` from the D10 nearest-neighbour
cut current.  Let

\[
 |h;2\rangle={1\over2}\sum_{x=0}^{3}e^{ihx}|2_x\rangle,
 \qquad h={\pi\over2},                                      \tag{G4.24}
\]

where `|2_x⟩` has colour `2` at `x` and colour `0` elsewhere.

**PROVE / CHECK.**  This is a genuine non-SU(2) instance of
G4-S-IDX-label, and it exhibits the strict projector split of G4-SPLIT.

**⟨2⟩1.**  The selected circle is scalar-periodic and the broken component
has primitive integral character:

\[
 e^{2\pi iC}=e^{-2\pi i/3}\mathbf1,
 \qquad [C,X]=-X.                                           \tag{G4.25}
\]

Thus `spec C_4⊂2/3+ℤ` and `χ_X` evaluates to `-1`.

*Justification.*  Direct `3×3` calculation.  The nonzero offset is deliberate:
it tests cancellation in the label difference rather than only the zero-coset
special case.

**⟨2⟩2.**  The hard vector and its charge-created/current-created partners
have

\[
 C_4|h;2\rangle={5\over3}|h;2\rangle,
 \quad C_4Q_X|h;2\rangle={2\over3}Q_X|h;2\rangle,
 \quad C_4J_X|h;2\rangle={2\over3}J_X|h;2\rangle.            \tag{G4.26}
\]

The soft datum is therefore `(2/3)-(5/3)=-1`, exactly (G4.14).

*Justification.*  G4-S-IDX-label.  Gate G4-C2 verifies the three equations by
full exact diagonalisation, without using a hand-written sector inventory.

**⟨2⟩3.**  The global charge is conserved and the hard vector is an exact
eigenvector:

\[
 [H_4,Q_X]=0,
 \qquad H_4|h;2\rangle=2|h;2\rangle.                         \tag{G4.27}
\]

Hence the pure zero-mode-created propagation has ratio one, as in (G4.16).

*Justification.*  Permutation invariance and direct ED; gate G4-C3.

**⟨2⟩4.**  Let `D=Q_X` restricted from the `5/3` sector to the `2/3` sector.
ED gives

\[
 \dim\mathcal H_{5/3}=8,\qquad
 \dim\mathcal H_{2/3}=24,\qquad
 \operatorname{rank}D=8.                                  \tag{G4.28}
\]

Thus `P_D<Π_{2/3}` strictly.  More sharply,

\[
 \|P_DJ_X|h;2\rangle\|=\sqrt{4/3},\qquad
 \|(\Pi_{2/3}-P_D)J_X|h;2\rangle\|=\sqrt{8/3}.              \tag{G4.29}
\]

Both pieces carry the *same* central sector label.  Superselection correctly
retains their sum in `Π_{2/3}` but has no datum that can remove or determine
the second piece.

*Justification.*  Gate G4-C3, using the SVD range projector of the exact ED
matrix `D`.  The nonzero second norm is the promised physical realization of
the abstract multiplicity witness (G4.19).

**⟨2⟩5.**  For reference, this instance happens to give
`P_DJ_X|h;2⟩=(2i/3)Q_X|h;2⟩` and
`⟨Q_Xh|P_DJ_Xh⟩=2i`.  G4 neither predicts nor uses these numbers; changing
the hard vector or resolving the nonabelian `U(2)` multiplicity requires
information beyond the central label.

*Justification.*  Gate G4-C3.  This line is diagnostic evidence, not a
generalized FIN.3 claim.

**⟨2⟩6. QED.**

## 5. Checker

### ⟨1⟩8. Certificate contract

The executable certificate is
`theory/checks/soft_index_g4_check.py`.  Its green path is

```text
python3 -O theory/checks/soft_index_g4_check.py
```

and it contains no bare `assert`.  It evaluates:

1. **G4-C0** — optimization-safe code shape;
2. **G4-C1** — the SU(3) scalar-period coset, `SU(3)` permutation invariance,
   and exact central covariance of `Q_X` and `J_X`;
3. **G4-C2** — the `5/3→2/3` sector shift for both created vectors;
4. **G4-C3** — the exact hard energy, zero-mode anchor, strict
   `P_D<Π_{2/3}` split, the two norms in (G4.29), and the diagnostic projected
   coefficient;
5. **G4-C4** — the SU(2) reduction on the matrices imported from
   `soft_index_r2_check.py`, reproducing SIDXR2-C2's descendant norms and
   residues (G4.21) while separately checking the `-1` label shift.

Two registered red modes must exit `1` under `python3 -O`:

```text
python3 -O theory/checks/soft_index_g4_check.py --red-shift
python3 -O theory/checks/soft_index_g4_check.py --red-projector-collapse
```

The first mutates the integral character from `-1` to `-2`.  The second
mutates the honest inclusion `P_D<Π_{2/3}` into equality.  The latter is a
negative control for the *scope* of the positive theorem: it prevents a green
selection-rule check from being reported as a certificate of FIN.1.

Recorded run, 2026-08-29: green exit `0`; `--red-shift` exit `1` at G4-C1;
`--red-projector-collapse` exit `1` at G4-C3.  The full standing
`soft_index_r2_check.py` also exits `0`, with SIDXR2-C2 residue error
`1.96×10^{-15}`; G4-C4 reproduces the same maximum.

As always under PRD.md, passing this finite certificate is corroboration, not
a promotion mechanism.  The character-lattice proof is analytic; the checker
tests one non-SU(2) representative and the exact SU(2) regression interface.

## 6. MERGE PROPOSALS

Nothing in this section is applied by this lane.

### 6.1 Proposed CLAIMS row

> | S-IDX-G-label | Let a finite periodic ring carry a compact Lie on-site
> `G`, a finite-range `G`-invariant Hamiltonian, a D2 vacuum label `α` with
> unbroken subgroup `H_α`, and a represented broken component `X` of central
> character `χ_X∈Hom(Z(H_α)/K_u,U(1))`, where
> `K_u={z:u(z)∈U(1)I}`.  Then the global charge `Q_X` and zero-mode current
> `J_X` obey the exact block-selection identities
> `Π_δQ_XΠ_γ=δ_{δ,γχ_X}Q_XΠ_γ` and
> `Π_δJ_XΠ_γ=δ_{δ,γχ_X}J_XΠ_γ`; the charge-created soft datum is the sector
> difference `χ_X`, whose value on every central scalar-period circle is an
> integer.  Also, the pure zero-mode-created readout has ratio one.  This is
> only the sector-label/integrality and FIN.8 half of S-IDX-fin: it does not
> identify the target central block with `ran Q_X` and proves none of
> FIN.1--FIN.3. | **SKETCH** (proposer proof; critic not yet run) | D2, D10,
> D26, S-IDX-fin | theory/soft-index-g4.md ⟨1⟩1--⟨1⟩7 |
> theory/checks/soft_index_g4_check.py G4-C0--C4 (one SU(3) ED instance;
> two red modes; SU(2) SIDXR2-C2 regression) |

### 6.2 Proposed theorem text beside S-IDX-fin

> **Finite central-sector index (general compact Lie `G`).**  In the notation
> of S-IDX-G-label, a charge-created soft component and the covariant current
> component shift the conserved central sector by the same character
> `χ_X`.  Hence their target/source sector-label difference is the element
> `χ_X` of the character group of the effective unbroken centre; on every
> central circle it is integer-valued.  This statement is channel-free and
> multiplicity-blind.  It is not the projected-current identity FIN.1: in
> general `ran(Q_XΠ_γ)` is a proper subspace of `ran Π_{γχ_X}`.

### 6.3 Hybridization rule for the surviving general-`G` proof

1. Keep (G4.11)--(G4.14) as the symmetry-quantization layer.  They make the
   phrase “the soft datum is a difference of conserved sector labels” exact
   and generalize without a channel inventory.
2. Keep (G4.16) as the general-`G` pure zero-mode anchor.
3. Accept a generalization of FIN.1--FIN.3 only from a surviving parallel
   route that supplies the *descendant-range projector* and its
   multiplicity-space operator.  The central-sector projector must not be
   substituted for it.
4. Retain the SU(3) strict-inclusion numbers (G4.28)--(G4.29) as the regression
   fence against that substitution.

### 6.4 Proposed notation rows

> | `Z_α`, `K_u`, `Z_{α,eff}` | centre `Z(H_α)`, its on-site scalar kernel,
> and the effective unbroken centre `Z(H_α)/K_u` | theory/soft-index-g4.md
> ⟨1⟩1 |
>
> | `Λ_α^*`, `χ_X`, `ind_{Z_α}(X;γ)` | character group of the effective
> unbroken centre, central character of the represented soft component, and
> its target/source sector-label difference | theory/soft-index-g4.md
> ⟨1⟩1--⟨1⟩3 |

### 6.5 Do-not-merge claims

- Do not relabel G4-S-IDX-label as a general-`G` proof of FIN.1, FIN.2, or
  FIN.3.
- Do not call the expectation value of a soft observable quantized.  The
  quantized object is the sector-label difference `χ_X`; mixtures average
  those labels just as `δx` averages M-INDEX-fin outcomes.
- Do not claim a nonzero integer when `χ_X` is trivial, or an integer circle
  component when `Z(H_α)^0` is trivial.  The full character group may then
  carry only a finite torsion label.
- Do not infer a scattering soft limit, D29 matching, an LSZ coefficient, or
  a universal phase slope from (G4.11)--(G4.16).
