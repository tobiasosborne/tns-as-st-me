# THEOREM (any finite lattice)
**Verdict.** S-IDX-fin-G is dimension-free once its displayed current map is supplied.
**Scope.** The same statement holds on every finite graph or finite periodic lattice.
**Input.** Only finite-dimensional root-`sl_2` algebra and `[Q(X),J_0(Y)]=J_0([X,Y])` are used.
**Geometry.** No operator-identity proof leaf uses an order, interval, translation, momentum, cut, or dimension.
**D10 audit.** D10(a)'s half-line `y <= m` is 1D notation, not an operator-theorem premise.
**Replacement.** On a graph use a displayed cut-current map `-[H,Q_S]`; only a periodic directional sum is called a zero-momentum flux.
**Registers.** The full `A^{-1}` and highest-restricted `lambda^{-1} Pi_hw` registers remain distinct.
**ED.** SU(2) `2x3` and SU(3) `2x2` instances reproduce both registers and Ward index one.
**Status.** The capped review certified the finite-lattice carrier at **PROVED** strength.

## 1. Scope and dimension audit

This shard changes only the carrier of the already-PROVED operator theorem:
the finite ring is replaced by a finite vertex set `V`.  It does not claim that
an arbitrary graph canonically chooses a current, a direction, or a cycle.  As in
`soft-index-general.md` (H.1), the adjoint-covariant complex-linear map
`J_0` is displayed data.  The finite-range Hamiltonian is relevant to the
local construction of such data, but it is absent from the ladder proof once
the commutator is assumed.

The table audits every logical leaf of the operator identity and normalized
Ward residue.  The citations in the first column refer to the detailed ladder
in `soft-index-g.md` and its compressed final form in
`soft-index-general.md`.

| Leaf | What the leaf uses | Dimension audit | Verdict |
|---|---|---|---|
| ⟨1⟩2.⟨2⟩1; (H.3) | The on-site infinitesimal action gives `[Q(X),Q(Y)]=Q([X,Y])`; global symmetry gives `[Q(X),H]=0`. | A sum over a finite vertex set replaces the sum over ring sites. | Independent. |
| ⟨1⟩2.⟨2⟩2; (H.1) | Jacobi and invariance make the supplied current an adjoint tensor. | The abstract hypothesis has no geometry.  The cited D10 half-line construction is 1D-bound as written; the graph-cut replacement is proved in §2.1 below. | Independent theorem input; 1D-only example repaired. |
| ⟨1⟩2.⟨2⟩3; (H.4) | Substitute the root brackets into current covariance. | Lie algebra only. | Independent. |
| ⟨1⟩2.⟨2⟩4 | Finite-dimensional compact root-`SU(2)` representation theory gives integral coroot weights. | The tensor-product carrier is finite; its adjacency is irrelevant. | Independent. |
| ⟨1⟩2.⟨2⟩5; (H.5)--(H.7) | The last two weight commutators type `J_0(H_alpha)` and `J_0(F_alpha)` between weight sectors. | Spectral subspaces of a finite matrix have no geometric input. | Independent. |
| ⟨1⟩3.⟨2⟩1.⟨3⟩1; (H.11) | Complete reducibility under the represented root triple. | Depends only on finite-dimensional unitarity. | Independent. |
| ⟨1⟩3.⟨2⟩1.⟨3⟩2; (H.12) | The standard `sl_2` ladder coefficient `a_(n,lambda)` and `a >= lambda > 0`. | Representation theory only. | Independent. |
| ⟨1⟩3.⟨2⟩1.⟨3⟩3 | `Q(E)=Q(F)^dagger` identifies those coefficients with the spectrum of `A=D^dagger D`. | Hilbert-space adjoints only. | Independent. |
| ⟨1⟩3.⟨2⟩2; (H.13) | `P=D A^{-1}D^dagger` for injective finite-dimensional `D`. | Polar/projection algebra only. | Independent. |
| ⟨1⟩3.⟨2⟩3.⟨3⟩1; (H.14) | The Ward commutator and `Q(E)psi=0` give `Q(E)J_0(F)psi=J_0(H)psi`. | Operator algebra only. | Independent. |
| ⟨1⟩3.⟨2⟩3.⟨3⟩2 | Between the typed sectors, `Q(E)` is `D^dagger`. | Hilbert-space adjoints only. | Independent. |
| ⟨1⟩3.⟨2⟩4.⟨3⟩1 | Substitute (H.14) into (H.13) to obtain the full-register identity (H.8). | Algebra only. | Independent. |
| ⟨1⟩3.⟨2⟩4.⟨3⟩2 | `J_0(H)psi` need not be highest; therefore `A^{-1}` cannot be replaced by `1/lambda`. | A register warning, witnessed again by the 2D SU(3) ED below. | Independent. |
| ⟨1⟩3.⟨2⟩5.⟨3⟩1; (H.15) | On the highest subspace, `Q(E)Q(F)=Q(H)=lambda`. | Root algebra only. | Independent. |
| ⟨1⟩3.⟨2⟩5.⟨3⟩2; (H.16) | The adjoint of a restricted-domain map inserts `Pi_hw`. | Finite-dimensional operator typing only. | Independent. |
| ⟨1⟩3.⟨2⟩5.⟨3⟩3 | Apply the same polar formula with `D_hw^dagger D_hw=lambda I` to obtain (H.9). | Algebra only. | Independent. |
| (H.17), first equality | Since `D psi` lies in `ran D`, the projector can be removed in that bra. | Orthogonal projection only. | Independent. |
| (H.17), second and third equalities | Move `D` to the other side and use (H.14). | Inner-product algebra only. | Independent. |
| (H.10) | Divide by the explicitly nonzero denominator. | Scalar arithmetic only. | Independent. |
| (H.18)--(H.19) | Compact-centralizer equivariance and its canonical isotypic decomposition. | Internal representation theory; equivalent-copy mixing is unrelated to lattice geometry. | Independent. |
| (H.27)--(H.28) | Globally covariant conjugation transports root rows and their projectors. | Group action only. | Independent. |
| (H.41)--(H.42) | Insert the SU(2) root dictionary into the two operator identities. | A normalization change only. | Independent. |
| `soft-index-general.md` §5.1 residue table | The quoted `(2i,4i,6i)` values use the one-dimensional `N=4`, `h=pi/2` one-magnon band and its scalar group velocity. | This benchmark is 1D-specific as stated, but is not a premise or conclusion of (H.8)--(H.10).  In `d>1`, choose a displayed current direction and use the corresponding velocity component; (ED.4) is the direct 2D replacement. | 1D-only benchmark, not an operator-theorem obstruction. |
| `soft-index-g.md` ⟨1⟩3.⟨2⟩6.⟨3⟩2 | The separate pure-zero-mode anchor uses `[H,Q(F_alpha)]=0` and identical interacting/reference rows. | Global symmetry and finite-dimensional time evolution only. | Independent, but not part of the projected-current identity. |
| `soft-index-general.md` §6 fences | Central tori have no root, finite groups have no Lie component, and global form restricts represented sectors. | Lie/group structure only. | Independent. |

There is therefore no one-dimensional obstruction to the theorem.  The only
hidden one-dimensional object is the *particular current supplier* in D10(a):
the ordered half-line `(-infinity,m]` and its named bond.  Section 2.1 gives
the honest graph replacement and also records the unavoidable non-canonicity
on a graph with no chosen direction or cycle.

## 2. General finite-lattice theorem

### 2.1 Honest current register on a graph

Let `Gamma=(V,E)` be a finite graph with graph metric, let

\[
 H_\Gamma=\sum_Z h_Z,
 \qquad Q_S(Y)=\sum_{v\in S}q_v(Y),
 \qquad Q(Y)=Q_V(Y),
\]

where the interaction has finite graph range and each term is invariant:
`[h_Z,sum_(v in Z)q_v(Y)]=0`.  For any displayed vertex subset `S`, define
the displayed cut-current map

\[
 j_{\partial S}(Y):=-[H_\Gamma,Q_S(Y)].                    \tag{2D.1}
\]

Terms supported wholly inside `S` or its complement vanish in (2D.1), so
only terms meeting the finite-range boundary contribute.  With
`q_Y=max_(v in V)||q_v(Y)||`,

\[
 \|j_{\partial S}(Y)\|
 \leq 2\!\sum_{\substack{Z:\,Z\cap S\ne\varnothing\\
                              Z\cap S^c\ne\varnothing}}
       \|h_Z\|\,|S\cap Z|\,q_Y
 \leq C(Y,\Phi)|\partial_rS| .                            \tag{2D.1a}
\]

The second inequality uses bounded degree together with a uniformly bounded,
finite-range interaction; `partial_r S` is the range-`r` boundary collar.
Moreover Jacobi,
`[Q(X),H_Gamma]=0`, and
`[Q(X),Q_S(Y)]=Q_S([X,Y])` give

\[
 [Q(X),j_{\partial S}(Y)]=j_{\partial S}([X,Y]).            \tag{2D.2}
\]

Thus any displayed finite linear combination
`J_0(Y)=sum_a c_a j_(partial S_a)(Y)` supplies (H.1).  For an invariant
nearest-neighbour edge term, an alternative local convention is

\[
 j_{v\to w}(Y):=-[h_{\{v,w\}},q_v(Y)],\qquad
 J_0^{(a)}(Y)=\sum_v j_{v\to v+e_a}(Y)                     \tag{2D.3}
\]

on a periodic lattice.  Equation (2D.3) is the directional zero-momentum
flux used by the SU(2) check below.  On the `2x2` simple square graph the
checker instead displays the oriented plaquette cycle.  A general finite
graph may have neither a preferred direction nor a preferred cycle; in that
case `J_0` must remain displayed data.  This non-canonicity is already
present on a ring as the current-improvement warning in
`soft-index-general.md` §0, and is not used by the operator proof.

### 2.2 Theorem S-IDX-fin-G (finite-lattice carrier cell)

Let `Gamma=(V,E)` be any finite graph (including a finite periodic lattice)
carrying the finite-dimensional on-site unitary representation
`U_V=u^{\otimes |V|}` of a compact Lie group `G`.  Supply a displayed
complex-linear adjoint-covariant current map

\[
 J_0:\mathfrak g_{\mathbb C}\longrightarrow
       \operatorname{End}(\mathcal H_V),\qquad
 [Q(X),J_0(Y)]=J_0([X,Y]).                                  \tag{2D.4}
\]

On a periodic lattice `J_0` may be the displayed directional zero-momentum
flux (2D.3); on an arbitrary graph no canonical direction or zero mode is
supplied.  The map may, but need not, be constructed by (2D.1)--(2D.3).
Choose any
represented root `alpha` of the semisimple Lie algebra of `G^0`, with the
normalization (H.3), and any occupied positive coroot-weight sector
`H^alpha_(lambda,V)`.  Put
`K^alpha_(lambda,V)=ker Q(E_alpha) cap H^alpha_(lambda,V)`, and define
`D_alpha`, `A_alpha`, `P_alpha`, `Pi_hw`, `D_hw`, and `P_hw` exactly as in
(H.5)--(H.7), with `N` replaced by `V`.

Then for every `psi in K^alpha_(lambda,V)`, `A_alpha>0` and

\[
 P_\alpha J_0(F_\alpha)\psi
 =D_\alpha A_\alpha^{-1}J_0(H_\alpha)\psi,                 \tag{2D.5}
\]

while in the separately highest-restricted register

\[
 D_{\rm hw}^\dagger D_{\rm hw}=\lambda I,\qquad
 P_{\rm hw}J_0(F_\alpha)\psi
 ={1\over\lambda}Q(F_\alpha)\Pi_{\rm hw}
 J_0(H_\alpha)\psi.                                       \tag{2D.6}
\]

If `langle psi,J_0(H_alpha)psi rangle != 0`, then

\[
 {\langle D_\alpha\psi,P_\alpha J_0(F_\alpha)\psi\rangle
  \over
  \langle\psi,J_0(H_\alpha)\psi\rangle}=1.               \tag{2D.7}
\]

The Hamiltonian, graph metric, interaction range, and construction of `J_0`
do not occur in (2D.5)--(2D.7) beyond supplying the finite carrier and the
displayed covariance (2D.4).

Central-torus directions have no root row, finite groups have no Lie-current
row, and the full-sector Gram inverse in (2D.5) is not interchangeable with
the separately highest-restricted scalar register in (2D.6).

### 2.3 Proof by citation (minimal diff)

1. Apply `soft-index-general.md` (H.3)--(H.7) to the finite Hilbert space
   `H_V`.  Their only input is (2D.4); the letter `N` never enters an
   algebraic operation.
2. Apply (H.11)--(H.12) verbatim to the restriction of `H_V` to the compact
   root triple.  Complete reducibility and the ladder coefficient give
   `A_alpha>0` on the full source sector.
3. Apply the finite-dimensional projector identity (H.13) and the Ward leaf
   (H.14).  Their substitution is (2D.5), with the full `A_alpha^{-1}` kept
   in place.
4. Apply (H.15)--(H.16) to the restricted domain.  The inserted source
   projector and the scalar restricted Gram give (2D.6).
5. Apply the three equalities in (H.17), then divide by the displayed
   nonzero denominator.  This is (2D.7).

Every cited step is audited in §1, so this is not an analogy or a
thermodynamic extrapolation: it is literally the same finite-dimensional
proof on a differently indexed tensor product.  QED.

## 3. Sector-label hygiene

**S-IDX-G-label is dimension-independent:** (H.31) sends a source character to `gamma chi_X`, Haar character orthogonality gives (H.32), and restriction to a cocharacter gives the integer (H.34); none of these steps refers to space.

## 4. Two-dimensional exact diagonalization

The executable falsifier is
`theory/checks/soft_index_2d_check.py`.  It constructs the Hamiltonian,
charges, currents, sectors, Gram operators, projectors, and highest-weight
kernels from matrices; no theorem expression is compared with a textual or
rescaled copy of itself.

### 4.1 SU(2), spin one-half, `2x3` periodic lattice

Sites are `(x,y)` with `x in Z_3`, `y in Z_2`.  The ferromagnetic
permutation form of the Heisenberg Hamiltonian is

\[
 H=\sum_{v,a=x,y}(I-P_{v,v+e_a}).                           \tag{ED.1}
\]

The `+y` term is retained at each vertex, so the two orientations of the
length-two wrap link occur as the usual two periodic bond terms.  The
displayed horizontal current zero mode is

\[
 J_0(Y)=\sum_v-[I-P_{v,v+e_x},q_v(Y)].                     \tag{ED.2}
\]

For `E=S^+`, `F=S^-`, `H_alpha=2S^z`, the one-down source has
`lambda=4`, dimension `6`, and highest dimension `5`.  ED gives

\[
 \operatorname{spec}(A)=\{4^{\times5},10\},\qquad
 D_{\rm hw}^\dagger D_{\rm hw}=4I_5.                       \tag{ED.3}
\]

The normalized one-magnon vector with `k=(2pi/3,0)` is highest, has energy
`3`, and obeys

\[
 J_0(H_\alpha)\psi=2\sqrt3\,i\,\psi,\qquad
 \langle D\psi,PJ_0(F)\psi\rangle
 =\langle\psi,J_0(H_\alpha)\psi\rangle=2\sqrt3\,i.         \tag{ED.4}
\]

The normalized Ward residue is therefore `1`.  Direct diagonalization of
(ED.1) also gives the expected seven-dimensional maximum-spin ground
multiplet.  The maximum full/restricted operator-identity residual included
in the combined gate is below `2.3e-15`.

### 4.2 SU(3), fundamental, `2x2` square

Number the square sites `(0,0),(1,0),(0,1),(1,1)` by `0,1,2,3`.  Use
`H=sum_(edges)(I-P)` on the four square edges and display the oriented cycle

\[
 0\longrightarrow1\longrightarrow3\longrightarrow2
 \longrightarrow0                                             \tag{ED.5}
\]

in (2D.3).  For the root on colours `0,1`, take
`E=e_(01)`, `F=e_(10)`, and `H_alpha=e_(00)-e_(11)`.

Two occupied positive sectors expose both aspects of the theorem:

| Sector | Full source dim. | Highest dim. | `spec(A)` | Restricted Gram |
|---:|---:|---:|---|---|
| `lambda=1` | 16 | 12 | `1` (x12), `4` (x4) | `I_12` |
| `lambda=2` | 10 | 9 | `2` (x9), `6` | `2I_9` |

On the complete `lambda=1` highest basis, (2D.5) has residual
`1.31e-15`; the false hybrid replacement `A^{-1} -> I/lambda` has norm
defect

\[
 \|PJ_0(F)\Pi_{\rm hw}
   -D\lambda^{-1}J_0(H_\alpha)\Pi_{\rm hw}\|=\sqrt{40}.     \tag{ED.6}
\]

Thus the full/restricted register distinction remains live in two spatial
dimensions.  In the `lambda=2` sector, the colour-1 defect with phase
`(1,i,-1,-i)` around (ED.5) is root-highest, has energy `2`, and gives

\[
 J_0(H_\alpha)\psi=4i\psi,\qquad
 \langle D\psi,PJ_0(F)\psi\rangle
 =\langle\psi,J_0(H_\alpha)\psi\rangle=4i.                 \tag{ED.7}
\]

Again the normalized Ward residue is `1`.  Full ED gives the expected
15-dimensional completely symmetric SU(3) ground multiplet.

### 4.3 Checker contract

Run the green certificate with

```bash
python3 -O theory/checks/soft_index_2d_check.py
```

It exits `0` and executes:

| Gate | Independent content |
|---|---|
| `SIDX2D-C0` | Parses its own AST and rejects bare `assert`. |
| `SIDX2D-C1` | Diagonalizes both Hamiltonians; checks ground multiplets, root-current covariance, and charge conservation. |
| `SIDX2D-C2` | Builds both Gram registers and checks their spectra and the two projected-current identities on complete highest bases. |
| `SIDX2D-C3` | Checks the two hard vectors, their ED energies/current eigenvalues, both unnormalized Ward residues, and both normalized indices. |

The registered structural red mode is

```bash
python3 -O theory/checks/soft_index_2d_check.py --red-scalar-full
```

It replaces the full-sector inverse by `1/lambda` at the acceptance gate,
hits (ED.6), and exits `1`.  Passing the green checker is a falsifier outcome,
not the proof; the proof is §2.3.

## 5. MERGE PROPOSALS

No existing file is edited by this lane.  After the capped theorem review:

1. **S-IDX-fin-G row.** In `claims/CLAIMS.md`, use the finite-lattice carrier
   cell of §2.2 with its “displayed adjoint-covariant current map” wording
   and subordinate periodic directional zero-mode specialization; add this shard and
   `soft_index_2d_check.py` as proof/check pointers.  Do not change the two
   Gram registers.
2. **D10 graph clause.** Add a graph-current clause stating (2D.1)--(2D.3).
   Keep D10(a)'s half-line formula as the one-dimensional specialization,
   and state that an arbitrary graph supplies no canonical direction or
   zero mode.
3. **S-IDX-G-label row.** Replace its carrier phrase “finite periodic ring”
   by the same finite-lattice phrase.  Its proof and label are otherwise
   unchanged.
4. **Checker registration.** Register `SIDX2D-C0`--`C3` and the public
   `--red-scalar-full` command.  The ED values are regression data, not new
   analytic hypotheses.
