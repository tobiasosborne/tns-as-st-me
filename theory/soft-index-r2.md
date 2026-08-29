<!-- ROLE: the ONE unified r2 S1 shard for bd tns-v44.  This file
     supersedes theory/soft-index.md (S1-A) and theory/soft-index-b.md
     (S1-B) as a theorem candidate.  The two r1 files remain lane records.
     Proposed D29/D30 and CLAIMS text is quarantined in section 7. -->

# S-INDEX r2 — the charge-created protocol datum and its soft index

## 0. Status, scope, and supersession

### ⟨1⟩1. Status theorem for this shard

**ASSUME.**  The process constitution in `PRD.md`; the L4 registers D3,
D6--D8, D10, D12, D24--D26, and D31; the adjudication
`theory/verdicts/soft-index-adjudication-r1.md`, with its prepended
orchestrator erratum taking precedence; and the authoritative L5 rows
`ML4-Ward`, `ML4-A`, `ML5-B`, `D24-VAL`, `AMP`, `S2-2body-S`, and
`AC-EX-2M`.

**PROVE.**  The following is the exact claim strength of this r2 deliverable.

**⟨2⟩1.**  `theory/soft-index.md` and `theory/soft-index-b.md` are
superseded as theorem candidates, but not edited and not erased as records.

*Justification.*  The binding r2 work order in
`theory/verdicts/soft-index-adjudication-r1.md` §4 and bd `tns-v44`, whose
scope is forced by the repaired claim `ML4-Ward` and the open interface claim
`AC-EX-2M-D29`.

**⟨2⟩2.**  **S-IDX-fin** is an unconditional finite-volume theorem
within its displayed finite SU(2) ring hypotheses.  Its primary projected
current identity is stated in the **full-sector register**

\[
 P_{\lambda,N}J^-_0
 =2D_{\lambda,N}A_{\lambda,N}^{-1}J^z_0,
 \qquad
 A_{\lambda,N}=D_{\lambda,N}^{\dagger}D_{\lambda,N}
 \text{ on all of }\mathcal H_{\lambda,N},                 \tag{R2.1}
\]

when applied to highest-weight inputs.  The weight `m_{\lambda,N}` is
retained as a scalar register, but is never substituted for the non-scalar
full-sector operator `A_{\lambda,N}`.  A separately named
highest-weight-restricted corollary contains the mandatory projector
`\Pi_{\rm hw}`.

*Justification.*  Claim `ML4-Ward`, including its register-dependent
ERRATUM; named computation **UXR-R1** in
`theory/checks/ml4_ward_n2_check.py` C5.  This is the full-sector option
allowed by the orchestrator erratum and explains the displayed design choice.

**⟨2⟩3.**  **S-IDX-spec-struct** is a complete conditional implication:
for every actual D29 ordered limit point satisfying D30(TGT) and the separately
displayed hypothesis (PROTO-LSZ), symmetry gives an Adler zero and the linear
form

\[
 \mathcal A_*(\epsilon)
 =2i\,\mathfrak a_{\rm leg}(\rho)\,
   \operatorname{sgn}(v_h-v_s)\,\ell_h\,
   \bar k_*(\epsilon)+o(\epsilon).                           \tag{R2.2}
\]

The constant `\mathfrak a_{\rm leg}(\rho)` is the **OPEN** constant of
D24(d)3b.  Equation (R2.2) fixes structure, not a numerical slope.

*Justification.*  Claim `ML5-B` supplies exactly this conditional
factorisation shape, with no value at any density; D24(d)3b defines the open
class constant.  The finite protocol-to-LSZ decomposition is carried as a
hypothesis rather than smuggled into D29 by definition, as required by the
r1 adjudication §3.6.

**⟨2⟩4.**  **S-IDX-spec** adds the displayed on-shell matching interface
(MATCH-S) and the D24-VAL membership antecedent needed to make the shared
class constant nonvacuous.  For a primitive unit-charge leg in the fully
polarised spin-`S` band, it gives

\[
 \mathcal A_*(\epsilon)
 =i\,{\operatorname{sgn}(v_h-v_s)\over S}\,
   \bar k_*(\epsilon)+o(\epsilon),
 \qquad
 {\arg(1+\mathcal A_*(\epsilon))\over\bar k_*(\epsilon)}
 \longrightarrow {\operatorname{sgn}(v_h-v_s)\over S}.      \tag{R2.3}
\]

Equivalently, where `\rho=S` and `\ell_h=1`, the slope is
`\operatorname{sgn}(v_h-v_s)\ell_h/\rho`.  No `|q|>1` formula is promoted:
`\ell_h=|q|` is used only for the proved primitive value `|q|=1`.

*Justification.*  The numerical value in (R2.3) is supplied by the PROVED
row `S2-2body-S`,
`\partial_{k_s}\delta_{\rm phys}|_0
=\operatorname{sgn}(v_h-v_s)/S`, and not by D29 or D30.  The need to display
the separate matching interface is the binding ruling of
`soft-index-adjudication-r1.md` §3.2: no regularity-only target hypothesis can
pin a jet.

**⟨2⟩5.**  The logical implication in ⟨2⟩4 has a complete proof,
but no theorem in the current DAG proves (MATCH-S) or (PROTO-LSZ) for the
adjudicated fixed-time D29 datum.  Therefore the proposed L5 row
`S-IDX-spec` remains **SKETCH**.  `AC-EX-2M` proves fixed-packet Haag--Ruelle
limits and the D7 multiplier on D6; it explicitly proves no soft-uniform
D29 identification.  The missing D29 bridge is the existing SKETCH row
`AC-EX-2M-D29`.

*Justification.*  Claims `AC-EX-2M` and `AC-EX-2M-D29`.  The latter names
both missing steps: first-order identification of the fixed-time D29 readout
with the constructed channel and an `(ACE2M-SR)` instance for the same
family.

**⟨2⟩6.**  The constructed-channel D6 datum is a PROVED value supplier,
not a proved D29 protocol instance.  Its multiplier obeys (R2.3) by
`AC-EX-2M` plus `S2-2body-S`; calling it a D29 instance would silently assume
the bridge excluded in ⟨2⟩5.

*Justification.*  `AC-EX-2M` (fixed packets), `S2-2body-S` (exact value),
and the negative scope sentence in `AC-EX-2M-D29`.

**⟨2⟩7.**  The proposed CLAIMS rows in §7 are all labelled SKETCH for
this pre-critic proposer pass, even where the conditional proof ladder is
complete.  Existing PROVED supplier rows retain their authoritative status.

*Justification.*  `PRD.md`, “The gate to PROVED”, together with the still-open
supplier claims `AC-EX-2M-D29` and `AMP`: a complete proposer proof is
necessary, not sufficient, for a new PROVED row.

**⟨2⟩8. QED.**

The separation in ⟨2⟩3--⟨2⟩5 is load-bearing: **structure from the
Ward/LSZ symmetry interface; value from on-shell data; existence and matching
from dynamics.**

## 1. Frozen definitions used

### ⟨1⟩2. Definition and type registry

**ASSUME.**  The symbols below occur in the theorem ladder.

**PROVE.**  Every pre-existing symbol has one frozen D-numbered source; this
section introduces no competing definition.

**⟨2⟩1.**  Finite soft profiles, packet-only plane waves, and the
distinction between finite-support operators and wave-packet kernels are used
in the sense of D3(a).

*Justification.*  D3(a).

**⟨2⟩2.**  The finite-ring ferromagnet, ordered two-magnon chamber,
physical out/in convention, signed soft momentum, hard momentum, velocities,
and continuous phase branch are used in the senses of D6, D7, and D8.

*Justification.*  D6--D8.

**⟨2⟩3.**  `Q_k`, `J^-_k`, `J^z_0`, and the finite-range cut current
are the charge/current objects of D10.  Every momentum label is either a
finite-ring momentum or a kernel inside a D3(a) packet.

*Justification.*  D10(a)--(c) and D3(a).

**⟨2⟩4.**  Whenever an infinite-volume packet identity is used, the
packet is in the `\ell^1\cap BV` regime; no fixed-momentum equality is inferred
from a `c_0` remainder statement.

*Justification.*  D12(a′) and D12's type-discipline paragraph.

**⟨2⟩5.**  `M_1^O`, `M_2^O`, `L(k,h)`, `E^O_{\rm desc}`,
`\mathcal S_W(\rho)`, `Z_\rho`, and
`\mathfrak a_{\rm leg}(\rho)` have exactly the meanings and normalisation of
D24.  In particular,

\[
 L(0,h)=\mathfrak a_{\rm leg}(\rho)
          {-i\,\operatorname{sgn}(v_h-v_s)\over v_h}          \tag{R2.4}
\]

displays the **OPEN** D24(d)3b class constant; (R2.4) fixes only its
`h`-profile and fixes no value, including at `\rho=1/2`.

*Justification.*  D24(b), D24(d)3a, and D24(d)3b.

**⟨2⟩6.**  The D24(d)2 descendant residue and `E^O_{\rm desc}` are not
silently put in one normalisation.  D24(d)2 uses the charge-created leg,
whereas D24(b) uses the delta-normalised asymptotic leg.  Their conversion is
`\sqrt{Z_\rho}` only in the LSZ limit and
`\sqrt{Z_\rho-2/N}` at finite `N` on a descendant with `q\ne h`.

*Justification.*  D24(b)(i)--(ii) and D24(d)2.

**⟨2⟩7.**  No leg-normalisation mechanism is used to assign a value to
`\mathfrak a_{\rm leg}`.  The leg conversion in ⟨2⟩6 supplies only
`Z_\rho^{-1/2}` in the LSZ limit, not `Z_\rho^{-1}`; any conditional matched
value `1/Z_\rho` requires a second factor from a different mechanism.

*Justification.*  D24(b)(ii) and the quantitative fence in D24(d)3b.

**⟨2⟩8.**  `\mathsf S(k_s;\{q_i,v_i\})` denotes only D25's proposed
Corner-C multiplier.  The concrete protocol datum below is written
`\mathcal A`; `S_{12}`, `S_{21}`, and `S_{\rm phys}` retain their D7 meanings.

*Justification.*  D25 and D7.

**⟨2⟩9.**  D26(INT) is compatible with the finite SU(2) rings but is
not used to prove the Ward projection or the soft slope.  No arithmetic
assumption on a free real `\rho` is inserted into S-IDX-fin.

*Justification.*  D26.

**⟨2⟩10.**  D31 supplies the exact fixed-packet two-magnon band and
creator hypotheses used by the `AC-EX-2M` interface.  Its own scope is
fixed-packet: a soft scale and a soft-uniform limit are absent.

*Justification.*  D31(1)--(5) and the final sentence of D31.

**⟨2⟩11.**  D29(PROTO) and D30(TGT) are not live definitions at the
time of this proposer pass.  In §§7.1--7.2 they occur only as exact merge
proposals; the proof uses those proposed clauses by name and does not install
them in this section.

*Justification.*  D31 is the last live numbered definition in the frozen
registry; the proposed numbers are therefore quarantined until merge.

**⟨2⟩12. QED.**

## 2. S-IDX-fin — unconditional finite-volume index identity

### ⟨1⟩3. Theorem S-IDX-fin

**ASSUME.**  Let a finite periodic ring carry an on-site SU(2) action and an
SU(2)-invariant finite-range Hamiltonian in the D10 register.  Let
`Q_0=S^-`, let `(J^+_0,J^z_0,J^-_0)` be its vector-current zero modes, and
let `\mathcal H_{\lambda,N}` be the **full** finite-dimensional weight sector
on which `S^z=m_{\lambda,N}>0`.  Put, locally for this theorem,

\[
 D_{\lambda,N}:=Q_0|_{\mathcal H_{\lambda,N}},\qquad
 A_{\lambda,N}:=D_{\lambda,N}^{\dagger}D_{\lambda,N}
 \quad\hbox{on all of }\mathcal H_{\lambda,N},
\]

and let `P_{\lambda,N}` be the orthogonal projection onto
`\operatorname{ran}D_{\lambda,N}`.  Let
`\Pi_{\rm hw}` be the orthogonal projection in
`\mathcal H_{\lambda,N}` onto
`K_{\lambda,N}:=\ker S^+\cap\mathcal H_{\lambda,N}`.  The theorem makes no
D29, D30, wave-operator, completeness, integrability, or soft-limit
assumption.

**PROVE.**  For every `\psi\in K_{\lambda,N}`:

\[
 \boxed{P_{\lambda,N}J^-_0\psi
 =2D_{\lambda,N}A_{\lambda,N}^{-1}J^z_0\psi}                 \tag{FIN.1}
\]

in the full-sector register.  In the distinct highest-weight-restricted
register,

\[
 D_{\rm hw}^{\dagger}D_{\rm hw}=2m_{\lambda,N}\mathbb 1,
 \qquad
 \boxed{P_{\rm hw}J^-_0\psi
 ={1\over m_{\lambda,N}}Q_0\Pi_{\rm hw}J^z_0\psi}.           \tag{FIN.2}
\]

For a nonzero-momentum primitive one-magnon vector `|h\rangle_N` in the
spin-`S` ferromagnetic band, `m_{\lambda,N}=NS-1`, the projector in (FIN.2)
may be removed and

\[
 J^z_0|h\rangle_N=i v_S(h)|h\rangle_N,\qquad
 \langle h|Q_0^{\dagger}P_{\lambda,N}J^-_0|h\rangle_N
 =2i v_S(h).                                                  \tag{FIN.3}
\]

**⟨2⟩1. PROVE.**  `A_{\lambda,N}` is strictly positive on the full
weight sector and hence invertible.

**⟨3⟩1.**  Decompose the finite SU(2) representation into spin-`j`
irreducibles.  On a weight-`m_{\lambda,N}` vector in such an irrep,

\[
 S^+S^-=(j+m_{\lambda,N})(j-m_{\lambda,N}+1)
        \ge 2m_{\lambda,N}>0.                                \tag{FIN.4}
\]

*Justification.*  Named weight-register gate **SIDXR2-C2**; its
operator form is the SU(2) ladder calculation underlying the norm clause of
claim `ML4-Ward`.

**⟨3⟩2.**  Since `A_{\lambda,N}` is the restriction of `S^+S^-`,
(FIN.4) proves strict positivity and invertibility.

*Justification.*  ⟨3⟩1 and the definition of `D_{\lambda,N}` in the
ASSUME block; named gate **SIDXR2-C2**.

**⟨3⟩3. QED.**

**⟨2⟩2. PROVE.**  On the full sector,

\[
 P_{\lambda,N}=D_{\lambda,N}A_{\lambda,N}^{-1}
 D_{\lambda,N}^{\dagger}.                                   \tag{FIN.5}
\]

**⟨3⟩1.**  The right side of (FIN.5) is self-adjoint, is the
identity on `\operatorname{ran}D_{\lambda,N}`, and vanishes on its orthogonal
complement.

*Justification.*  ⟨2⟩1 and finite-dimensional polar/projection algebra,
named gate **SIDXR2-C2**; claim `ML4-Ward` calls the same object
the full-sector projection.

**⟨3⟩2. QED.**

**⟨2⟩3. PROVE.**  The vector-current commutator gives

\[
 D_{\lambda,N}^{\dagger}J^-_0\psi=2J^z_0\psi.               \tag{FIN.6}
\]

**⟨3⟩1.**  SU(2) covariance of the D10 cut current gives
`[S^+,J^-_0]=2J^z_0`; hence
`S^+J^-_0\psi=2J^z_0\psi+J^-_0S^+\psi=2J^z_0\psi`.

*Justification.*  D10(a), the Jacobi computation for an invariant finite-range
bond current, and claim `ML4-Ward` equation (8); independently checked by
named gate **SIDXR2-C2**.

**⟨3⟩2.**  Restricting the left side to the source and target weight
sectors turns `S^+` into `D_{\lambda,N}^{\dagger}`, proving (FIN.6).

*Justification.*  ⟨3⟩1 and named gate **SIDXR2-C2**.

**⟨3⟩3. QED.**

**⟨2⟩4. PROVE.**  Equation (FIN.1).

**⟨3⟩1.**  Substitute (FIN.6) into (FIN.5):
`P J^-_0\psi=D A^{-1}D^{\dagger}J^-_0\psi
=2DA^{-1}J^z_0\psi`.

*Justification.*  ⟨2⟩2--⟨2⟩3; claim `ML4-Ward`'s corrected
full-sector formula.

**⟨3⟩2.**  No scalar `2m_{\lambda,N}` was pulled through
`A_{\lambda,N}^{-1}`: `J^z_0\psi` need not be highest weight when the sector
contains two or more magnons.

*Justification.*  Named register-trap computation **UXR-R1** / checker gate
**SIDXR2-C1**: the cross-register error is `O(1)` at `n\ge2`, while (FIN.1)
is exact.

**⟨3⟩3. QED.**

**⟨2⟩5. PROVE.**  Equation (FIN.2) in the separately named
highest-weight-restricted register.

**⟨3⟩1.**  For `\phi\in K_{\lambda,N}`,
`S^+S^-\phi=2S^z\phi=2m_{\lambda,N}\phi`; hence
`D_{\rm hw}^{\dagger}D_{\rm hw}=2m_{\lambda,N}\mathbb 1`.

*Justification.*  The first display of claim `ML4-Ward` (9), which remains
PROVED for every `n`; named computation **SIDXR2-C1**.

**⟨3⟩2.**  Because the adjoint of a restricted-domain map contains
the source projection,
`D_{\rm hw}^{\dagger}J^-_0\psi
=\Pi_{\rm hw}S^+J^-_0\psi=2\Pi_{\rm hw}J^z_0\psi`.

*Justification.*  ⟨2⟩3 and named computation **UXR-R1**.

**⟨3⟩3.**  Insert ⟨3⟩1--⟨3⟩2 into
`P_{\rm hw}=D_{\rm hw}(D_{\rm hw}^{\dagger}D_{\rm hw})^{-1}
D_{\rm hw}^{\dagger}` to obtain (FIN.2).

*Justification.*  Named computation **UXR-R1**, which verifies the
`\Pi_{\rm hw}` form at every tested `n` to `7.6\times10^{-16}`.

**⟨3⟩4. QED.**

**⟨2⟩6. PROVE.**  On a nonzero-momentum one-magnon vector,
`\Pi_{\rm hw}J^z_0|h\rangle_N=J^z_0|h\rangle_N`.

**⟨3⟩1.**  Vector-current covariance gives
`S^+J^z_0|h\rangle_N=-J^+_0|h\rangle_N`.  The zero-mode current preserves
momentum, while its raised target is the momentum-zero vacuum; therefore
`J^+_0|h\rangle_N=0` for `h\ne0`.

*Justification.*  Claim `ML4-Ward`'s one-hard consequence (11)/(R15), and
named gate **SIDXR2-C2**.

**⟨3⟩2.**  Thus `S^+J^z_0|h\rangle_N=0`, which is exactly the claimed
highest-weight membership.

*Justification.*  ⟨3⟩1 and named gate **SIDXR2-C2**.

**⟨3⟩3. QED.**

**⟨2⟩7. PROVE.**  The first identity in (FIN.3).

**⟨3⟩1.**  D10's continuity equation at a periodic plane-wave
profile gives, between exact one-magnon states,

\[
 -[\omega_S(h+k)-\omega_S(h)]
 =(e^{ik}-1)\langle h+k|J^z_k|h\rangle_N.                   \tag{FIN.7}
\]

*Justification.*  D10(b)--(c), D12(b)'s fixed-momentum register, and named
gate **SIDXR2-C2**.

**⟨3⟩2.**  The removable `k=0` value of (FIN.7) is
`i\partial_h\omega_S(h)=iv_S(h)`; translation covariance makes
`J^z_0` diagonal on the scalar one-magnon band.

*Justification.*  D6--D8 and named gate **SIDXR2-C2**.

**⟨3⟩3. QED.**

**⟨2⟩8. PROVE.**  The residue identity in (FIN.3).

**⟨3⟩1.**  By ⟨2⟩5--⟨2⟩7,
`P J^-_0|h\rangle_N=(iv_S(h)/m_{\lambda,N})Q_0|h\rangle_N`, while
`\|Q_0|h\rangle_N\|^2=2m_{\lambda,N}`.

*Justification.*  (FIN.2), ⟨2⟩6--⟨2⟩7, and the norm identity in
claim `ML4-Ward`; spin-`S` instances are checked by **SIDXR2-C2**.

**⟨3⟩2.**  Pairing ⟨3⟩1 with `Q_0|h\rangle_N` cancels
`m_{\lambda,N}` and yields `2iv_S(h)`.

*Justification.*  ⟨3⟩1 and named gate **SIDXR2-C2**.

**⟨3⟩3. QED.**

**⟨2⟩9. QED.**

### ⟨1⟩4. Corollary ADLER-Q0 — the honest finite-volume anchor

**ASSUME.**  In the setting of ⟨1⟩3, let `\psi_g` be a one-magnon
packet made from exact band vectors and form the **pure** zero-mode-created
state `\Phi_0:=Q_0\psi_g`.  Evaluate the D29 coordinate-kernel row readout
at soft row `k=0`, with nonzero free-row denominator.  This is not the
running D29 state `Q[f_\epsilon]\psi_g` at `\epsilon>0`.

**PROVE.**  Its interacting/free row ratio is exactly one for every finite
`N,T,W,\sigma` and every site spin `S`:

\[
 \boxed{\mathcal R_{\Phi_0}(0)=1}.                            \tag{FIN.8}
\]

**⟨2⟩1.**  SU(2) invariance gives `[H,Q_0]=0`, and the zero-mode
Goldstone energy is `\omega_S(0)=0`; hence
`e^{-iHT}Q_0|h\rangle_N=Q_0e^{-iHT}|h\rangle_N
=e^{-i[\omega_S(0)+\omega_S(h)]T}Q_0|h\rangle_N` row by row.

*Justification.*  D10(b), D6, and named computation **SIDXR2-C3**.

**⟨2⟩2.**  The interacting row kernel and the D29 free reference are
therefore identical, so their normalized pairing is one.

*Justification.*  ⟨2⟩1 and named computation **SIDXR2-C3**.

**⟨2⟩3.**  (FIN.8) is only an anchor for the object just named.  It
does not assert that the adjoined `k=0` row of the running D29 family equals
one at `S\ge1`, and it implies nothing about `\epsilon\downarrow0` because
the admissible D29 family contains no fixed-`N` continuous path to that row.

*Justification.*  Named countercomputation **S1B-F2**: the running-family
row is `2.1633+0.1527i` at `S=1,N=7`, whereas the pure `Q_0`-created row is
one to `9.5\times10^{-16}`.

**⟨2⟩4.**  At `S=1/2`, the same row identity also holds for arbitrary
two-magnon input in the coordinate readout, so it is a readout tautology
there rather than independent evidence for the protocol Adler zero.

*Justification.*  Named countercomputation **S1B-F2**.

**⟨2⟩5. QED.**

### ⟨1⟩5. QED for S-IDX-fin

**ASSUME.**  The hypotheses of ⟨1⟩3.

**PROVE.**  S-IDX-fin and its honest anchor are established without D29,
D30, or any limiting hypothesis.

**⟨2⟩1.**  Equations (FIN.1)--(FIN.3) follow from
⟨1⟩3.⟨2⟩1--⟨2⟩8.

*Justification.*  Claim `ML4-Ward` and named checker gates
**SIDXR2-C1--C2**.

**⟨2⟩2.**  Equation (FIN.8), with its exact scope and no protocol
inference, follows from ⟨1⟩4.

*Justification.*  Named computation **SIDXR2-C3** and named negative control
**S1B-F2**.

**⟨2⟩3. QED.**

## 3. S-IDX-spec — constraints on subsequential protocol limits

### ⟨1⟩6. The actual-limit-point register

**ASSUME.**  Use the proposed D29(PROTO) of §7.1.  At fixed soft scale
`\epsilon>0`, let
`j\mapsto(N_j,T_j,W_j,\sigma_j;\epsilon)` be an admissible outer sequence,
and let `\mathcal A_j(\epsilon)` be its finite, packet-smeared ratio datum.
Let `\mu_{j,\epsilon}` be D29's normalized nonnegative free-row measure on
`(k,h)` and

\[
 \bar k_j(\epsilon):=\int k\,d\mu_{j,\epsilon}(k,h).
\]

The support of its soft marginal lies in
`[c_1\epsilon,c_2\epsilon]` (or its reflected one-sided interval).  An
**actual limit point** means a common outer subsequence on which, for every
`\epsilon` in a set `E\downarrow0`, `\mathcal A_j(\epsilon)`, the row
measures, the hard Ward registers, and every component named by
(PROTO-LSZ) below converge in the topologies required there.  No assertion
that such a subsequence exists is included in the phrase.

**PROVE.**  The ordered and normalized soft variable of the theorem is the
packet mean `\bar k_*(\epsilon)`, not the carrier of an un-smeared plane
wave, and

\[
 c_1\epsilon\le |\bar k_*(\epsilon)|\le c_2\epsilon          \tag{SPEC.1}
\]

with the sign fixed by the chosen one-sided profile.

**⟨2⟩1.**  Every finite D29 datum uses the single rescaled packet
`f_\epsilon`; no independent width is sent to zero before `\epsilon`.

*Justification.*  D3(a), D12(a′), and proposed D29(2); this is the scale-only
option selected by `soft-index-adjudication-r1.md` §3.1.

**⟨2⟩2.**  A probability measure supported on the stated one-sided
interval has its mean in that interval; passage to the outer cluster measure
preserves the inequality.

*Justification.*  Proposed D29(4), proposed D30(b), and named packet-mean
gate **SIDXR2-C5**.

**⟨2⟩3.**  Thus (SPEC.1) holds.  The strict lower bound permits division
by `\bar k_*(\epsilon)` when a jet is compared below.

*Justification.*  ⟨2⟩2 and named gate **SIDXR2-C5**.

**⟨2⟩4. QED.**

### ⟨1⟩7. D30(TGT) is regularity-only and cannot supply the value

**ASSUME.**  Proposed D30(TGT) of §7.2 holds for an actual D29 limit point.

**PROVE.**  D30 provides compactness, a continuous-extension register, and a
well-defined first jet when one exists in its declared `C^1` cluster class;
it supplies no numerical value for that jet.

**⟨2⟩1.**  D30's clauses contain row-mass nondegeneracy, component
relative compactness, soft equicontinuity, convergence of `\rho_j` and
`\ell_j`, and an optional uniqueness clause.  They contain no phase-slope
number and no on-shell amplitude.

*Justification.*  Proposed D30(a)--(e).

**⟨2⟩2.**  For any regular family with `1+\mathcal A(\epsilon)\ne0`,
the transformation

\[
 1+\mathcal A(\epsilon)\longmapsto
 [1+\mathcal A(\epsilon)]e^{ic\epsilon}                     \tag{SPEC.2}
\]

preserves the D30 regularity and compactness clauses but shifts
`\partial_\epsilon\arg(1+\mathcal A)|_0` by the arbitrary real constant
`c`.

*Justification.*  Named constructive computation **SIDXR2-C6
(TGT-MOBIUS)**; this is the value-shift argument adjudicated in
`soft-index-adjudication-r1.md` §3.2.

**⟨2⟩3.**  Therefore any proof that reads a numerical coefficient out
of D30 alone is invalid.  A separate value supplier must appear at the exact
leaf where the coefficient is fixed.

*Justification.*  ⟨2⟩2 and claim `S2-2body-S`, the value supplier used
in ⟨1⟩9.

**⟨2⟩4. QED.**

### ⟨1⟩8. Theorem S-IDX-spec-struct — symmetry fixes the form

**ASSUME.**  An actual D29 limit point in the sense of ⟨1⟩6; D30(TGT);
and the following hypothesis, which is **not** part of D29 or D30:

**(PROTO-LSZ).**  In D24(b)'s packet/amputation normalisation, after the
outer limit and uniformly for `h\in I`, the limit datum has an exhaustive
decomposition

\[
 \mathcal A_*=\mathcal A_*^{\rm desc}
              +\mathcal A_*^{\perp}
              +\mathcal A_*^{\rm dir}
              +\mathcal A_*^{\partial},                     \tag{SPEC.3}
\]

where

\[
 \mathcal A_*^{\rm desc}(\epsilon)=
 \int (e^{ik}-1)L(k,h)\,[2iv_h\ell_h],
       d\mu_{*,\epsilon}(k,h),                               \tag{SPEC.4}
\]

`L` is uniformly `C^1` and has exactly the D24(d)3b profile (R2.4), and

\[
 \mathcal A_*^{\perp}=O(\epsilon^2),\qquad
 \mathcal A_*^{\rm dir}=O(\epsilon^2),\qquad
 \mathcal A_*^{\partial}=o(\epsilon).                       \tag{SPEC.5}
\]

The four terms respectively name the descendant, orthogonal-current,
direct-contact, and two window-boundary-gradient contributions.  Thus
(PROTO-LSZ) carries D24(d)1,3,4,5 and the finite-window boundary limit as
an explicit hypothesis; it does not make exhaustiveness true by definition.
It also carries the antecedents that the relevant `\mathcal S_W(\rho)` is
nonempty and that the D24(b) asymptotic kernel exists, solely so that
`\mathfrak a_{\rm leg}(\rho)` is defined; neither antecedent has a proved D29
instance.
It also assumes the measured hard Ward register converges to a finite
`\ell_h`, with `\ell_h=1` only for the primitive one-magnon band proved in
⟨1⟩3.

**PROVE.**  Every such limit point obeys

\[
 \boxed{\mathcal A_*(\epsilon)
 =2i\mathfrak a_{\rm leg}(\rho)
  \operatorname{sgn}(v_h-v_s)\ell_h\bar k_*(\epsilon)
  +o(\epsilon)},                                             \tag{SPEC.6}
\]

and hence has the continuous Adler extension
`\mathcal A_*(0):=0`.  Before on-shell matching, its phase jet is only

\[
 {\arg(1+\mathcal A_*(\epsilon))\over\bar k_*(\epsilon)}
 \longrightarrow
 2\operatorname{Re}\mathfrak a_{\rm leg}(\rho)\,
 \operatorname{sgn}(v_h-v_s)\ell_h,                         \tag{SPEC.7}
\]

not a numerical `1/\rho` law.

**⟨2⟩1. PROVE.**  Uniformly on the packet support,

\[
 e^{ik}-1=ik+O(\epsilon^2),\qquad
 L(k,h)=\mathfrak a_{\rm leg}(\rho)
 {-i\operatorname{sgn}(v_h-v_s)\over v_h}+O(\epsilon).      \tag{SPEC.8}
\]

**⟨3⟩1.**  The first expansion is Taylor's formula on
`|k|\le c_2\epsilon`; the second is the uniform `C^1` clause of
(PROTO-LSZ) combined with D24(d)3b.

*Justification.*  D24(d)3a--3b and named Taylor computation
**SIDXR2-C5**.

**⟨3⟩2. QED.**

**⟨2⟩2. PROVE.**  The descendant term has the expansion

\[
 \mathcal A_*^{\rm desc}(\epsilon)=
 2i\mathfrak a_{\rm leg}(\rho)
 \operatorname{sgn}(v_h-v_s)\ell_h\bar k_*(\epsilon)
 +O(\epsilon^2).                                             \tag{SPEC.9}
\]

**⟨3⟩1.**  Multiplication of the three leading factors in
(SPEC.4) and (SPEC.8) gives

`(ik)\,[\mathfrak a_{\rm leg}(-i\operatorname{sgn}/v_h)]
 [2iv_h\ell_h]
=2i\mathfrak a_{\rm leg}\operatorname{sgn}\ell_h k`.

*Justification.*  D24(d)2--3b and named factor computation
**SIDXR2-C5**.

**⟨3⟩2.**  Integration replaces `k` by the D29 packet mean
`\bar k_*(\epsilon)`; every cross term is `O(\epsilon^2)` uniformly because
`I\Subset(0,\pi)` keeps `v_h` away from zero in the chosen channel.

*Justification.*  D8, (SPEC.1), and named packet computation
**SIDXR2-C5**.

**⟨3⟩3. QED.**

**⟨2⟩3. PROVE.**  Equation (SPEC.6).

**⟨3⟩1.**  Add (SPEC.5) to (SPEC.9).  The `O(\epsilon^2)` terms and
the `o(\epsilon)` boundary term are `o(\epsilon)`.

*Justification.*  (PROTO-LSZ), ⟨2⟩2, and claim `ML4-A` for the
orthogonal `O(\epsilon^2)` architecture.

**⟨3⟩2. QED.**

**⟨2⟩4. PROVE.**  The Adler extension and (SPEC.7).

**⟨3⟩1.**  By (SPEC.1) and (SPEC.6),
`\mathcal A_*(\epsilon)=O(\epsilon)`, so its continuous extension at zero is
zero.

*Justification.*  ⟨1⟩6, ⟨2⟩3, D24(d)'s zero-intercept discipline,
and named expansion check **SIDXR2-C5**.

**⟨3⟩2.**  For `z=O(\epsilon)`,
`\arg(1+z)=\operatorname{Im}z+O(|z|^2)`.  The imaginary part of
`2i\mathfrak a_{\rm leg}` is
`2\operatorname{Re}\mathfrak a_{\rm leg}`; divide by the nonzero mean in
(SPEC.1).

*Justification.*  D7's continuous phase branch and named logarithm
gate **SIDXR2-C5**.

**⟨3⟩3. QED.**

**⟨2⟩5.**  **INSTANCE STATUS: CONJECTURE.**  No current claim proves
(PROTO-LSZ) for the adjudicated fixed-time D29 datum.  In particular, the
two boundary gradients and the fixed-time-charge/constructed-channel
identification are not controlled by `AC-EX-2M`.

*Justification.*  Claim `AC-EX-2M-D29` (SKETCH), which explicitly excludes
the fixed-time D29 interface from the PROVED creator-choice theorem.

**⟨2⟩6. QED.**

### ⟨1⟩9. Theorem S-IDX-spec — on-shell data fix the value

**ASSUME.**  The hypotheses of S-IDX-spec-struct; a fully polarised
spin-`S` vacuum, so `\rho=S`; a primitive one-magnon hard leg, so
`\ell_h=1`; the D24-VAL membership antecedent
`(\beta_S): O\in\mathcal S_W(\rho)|_{\rho=S}` with `M_1^O\ne0`; and the
following separate matching hypothesis:

**(MATCH-S).**  For the same limiting row measures and D7 window labelling,

\[
 \mathcal A_*(\epsilon)-
 \int [S_{\rm phys}(k,h)-1]\,d\mu_{*,\epsilon}(k,h)
 =o(\epsilon).                                               \tag{SPEC.10}
\]

This is a first-order identification of the fixed-time protocol readout with
the on-shell multiplier.  It contains no numerical slope; that number is
supplied only after the identification by `S2-2body-S`.

**PROVE.**  Equations (R2.3), and the conditional matched value

\[
 \mathfrak a_{\rm leg}(S)={1\over2S}={1\over Z_\rho}         \tag{SPEC.11}
\]

in the D24(b) normalisation.  More generally, any datum at the same density
that shares this D24(d) class constant and satisfies (PROTO-LSZ) obeys the
structural slope
`\operatorname{sgn}(v_h-v_s)\ell_h/\rho`; no conclusion
`\ell_h=|q|` is added beyond the primitive `|q|=1` case.

**⟨2⟩1. PROVE.**  The on-shell packet average has expansion

\[
 \int[S_{\rm phys}(k,h)-1]\,d\mu_{*,\epsilon}
 ={i\operatorname{sgn}(v_h-v_s)\over S}\bar k_*(\epsilon)
 +O(\epsilon^2).                                             \tag{SPEC.12}
\]

**⟨3⟩1.**  Uniformly for hard momenta in the compact window,
`S_{\rm phys}(k,h)-1
=i\operatorname{sgn}(v_h-v_s)k/S+O(k^2)`.

*Justification.*  PROVED claim `S2-2body-S`, equations (T.3)--(T.4).

**⟨3⟩2.**  Integrate ⟨3⟩1 and use
`\int k\,d\mu=\bar k_*` and `|k|\le c_2\epsilon`.

*Justification.*  ⟨1⟩6 and named gate **SIDXR2-C4**.

**⟨3⟩3. QED.**

**⟨2⟩2. PROVE.**  The protocol law (R2.3).

**⟨3⟩1.**  Combine (MATCH-S) with (SPEC.12):
`\mathcal A_*=i\operatorname{sgn}\bar k_*/S+o(\epsilon)`.

*Justification.*  ⟨2⟩1, the displayed hypothesis (MATCH-S), and claim
`S2-2body-S` supplying the expansion being matched.

**⟨3⟩2.**  Apply
`\arg(1+z)=\operatorname{Im}z+O(|z|^2)` and divide by (SPEC.1).

*Justification.*  D7, ⟨1⟩6, and named computation
**SIDXR2-C4**.

**⟨3⟩3. QED.**

**⟨2⟩3. PROVE.**  The conditional matched value (SPEC.11).

**⟨3⟩1.**  Compare (SPEC.6) at `\ell_h=1` with ⟨2⟩2.  Since
`|\bar k_*|\ge c_1\epsilon`, equality to first order gives
`2\mathfrak a_{\rm leg}(S)=1/S`.

*Justification.*  ⟨1⟩6, ⟨1⟩8, ⟨2⟩2, and claim
`D24-VAL`'s jet-identification antecedent.

**⟨3⟩2.**  As `Z_\rho=2\rho=2S`, this is exactly (SPEC.11).  At
`S\in\{1/2,1,3/2,2\}` this is precisely the existing PROVED conditional row
`D24-VAL`.  At any other half-integer `S`, it is the same one-line
conditional consequence of `S2-2body-S`, but remains part of this new SKETCH
row rather than an extension silently attributed to `D24-VAL`.

*Justification.*  D24(d), PROVED conditional claim `D24-VAL` on its four
stated spins, and claim `S2-2body-S` for the displayed all-`S` conditional
algebra.

**⟨3⟩3.**  This is a **conditional matched value**, not a derivation
from leg normalisation and not evidence that `\mathcal S_W(\rho)` is
nonempty.  The antecedents (MATCH-S), (PROTO-LSZ), and microscopic class
membership remain open for D29.

*Justification.*  Claims `D24-VAL` (antecedents explicitly unproved), `AMP`
(CONJECTURE), and `AC-EX-2M-D29` (SKETCH).

**⟨3⟩4. QED.**

**⟨2⟩4. PROVE.**  The `\ell_h` corollary at the same matched class
constant.

**⟨3⟩1.**  Substitute
`\mathfrak a_{\rm leg}(\rho)=1/(2\rho)` into (SPEC.6).

*Justification.*  ⟨1⟩8, the conditional value in ⟨2⟩3, and claim
`D24-VAL`.

**⟨3⟩2.**  This yields
`\mathcal A_*=i\operatorname{sgn}(v_h-v_s)(\ell_h/\rho)\bar k_*+o(\epsilon)`.
The substitution is licensed only for a datum sharing the matched D24(d)
class constant; it is not a claim that a composite band has
`\ell_h=|q|`.

*Justification.*  ⟨3⟩1 and the charge-scoping ruling in claim
`S2-2body-S` (unit-charge only).

**⟨3⟩3. QED.**

**⟨2⟩5.**  **INSTANCE STATUS: SKETCH for D29.**  (MATCH-S) is exactly
the open first-order bridge named by `AC-EX-2M-D29`; D30 cannot replace it by
⟨1⟩7.  Thus the theorem is a complete conditional implication but no
current DAG row instantiates it for the adjudicated protocol.

*Justification.*  Claims `AC-EX-2M-D29` and `ML6`, both non-PROVED at this
interface.

**⟨2⟩6. QED.**

### ⟨1⟩10. Instances and non-instances from the PROVED ansatz bands

**ASSUME.**  D31 on the D6 model and the PROVED rows `AC-EX-2M` and
`S2-2body-S`.

**PROVE.**  The exact status of the ansatz-band interface is as follows.

**⟨2⟩1.**  At every fixed pair of compact, velocity-separated packets,
`AC-EX-2M` constructs isometric Cook limits and identifies
`W_+^*W_-` with multiplication by D7's `S_{\rm phys}`.

*Justification.*  PROVED claim `AC-EX-2M` under D31.

**⟨2⟩2.**  For the **constructed-channel** soft packet average

\[
 \mathcal A_{\rm HR}(\epsilon):=
 \int[S_{\rm phys}(\epsilon u,h)-1]\,d\mu_f(u,h),          \tag{SPEC.13}
\]

`S2-2body-S` gives (R2.3), with
`\bar k=\epsilon\int u\,d\mu_f`.

*Justification.*  Claims `AC-EX-2M` and `S2-2body-S`; named aggregation
gate **SIDXR2-C4**.

**⟨2⟩3.**  Equation (SPEC.13) is a PROVED on-shell value instance but
is not the fixed-time charge-created D29 datum.  The Cook/Gram constants in
`AC-EX-2M` diverge along `f_\epsilon`, and creator-choice independence does
not apply to the fixed-time insertion `Q[f_\epsilon]\psi_g`.

*Justification.*  Claims `AC-EX-2M` (fixed-packet caveat) and
`AC-EX-2M-D29` (explicit non-composition result).

**⟨2⟩4.**  Consequently there is presently no PROVED D29 instance of
S-IDX-spec, no proved microscopic member of `\mathcal S_W(\rho)`, and no
permission to use `AMP` as a value supplier.

*Justification.*  Claims `AC-EX-2M-D29` (SKETCH), `ML5-B` (nonemptiness
open), and `AMP` (CONJECTURE).

**⟨2⟩5. QED.**
## 4. Ward, Adler, and on-shell-matching interfaces

### ⟨1⟩11. Interface theorem and load-bearing fences

**ASSUME.**  The proof ladders of §§2--3 and the frozen D24 normalisation.

**PROVE.**  Each interface has one named register, supplier, and limitation.

**⟨2⟩1. Ward interface.**  The all-sector statement is (FIN.1), with
`A_{\lambda,N}=D^{\dagger}D` on the **full** weight sector.  The
highest-weight-restricted statement is (FIN.2), with `\Pi_{\rm hw}`.  The
string

\[
 {1\over m_{\lambda,N}}Q_0J^z_0                             \tag{IF.1}
\]

without `\Pi_{\rm hw}` is **REFUTED for `n\ge2`** and appears nowhere as a
claim in this shard.

*Justification.*  Claim `ML4-Ward`; named register-trap computation
**UXR-R1** and checker gate **SIDXR2-C1**.

**⟨2⟩2. Adler interface.**  The exact value one is (FIN.8) for the
pure state `Q_0\psi_g`.  It is not an adjoined row of the running
`Q[f_\epsilon]\psi_g` family, and at `S=1/2` it is not protocol evidence.
The protocol Adler zero in (SPEC.6) instead uses the exhaustive
(PROTO-LSZ) estimate.

*Justification.*  Named computations **SIDXR2-C3** and **S1B-F2**;
S-IDX-spec-struct ⟨1⟩8.

**⟨2⟩3. S2 value interface.**  The only numerical slope supplier in
S-IDX-spec is

\[
 \left.\partial_{k_s}\delta_{\rm phys}\right|_0
 ={\operatorname{sgn}(v_h-v_s)\over S}.                     \tag{IF.2}
\]

It enters after (MATCH-S), never as a D29 clause and never as a D30
regularity condition.

*Justification.*  PROVED claim `S2-2body-S`; ⟨1⟩7 proves that D30 cannot
fix (IF.2).

**⟨2⟩4. Open-constant interface.**  In every pre-matching display,
`\mathfrak a_{\rm leg}(\rho)` is the open D24(d)3b constant.  The conditional
matched value `1/Z_\rho` is licensed only under the antecedents of
`D24-VAL`; the bridge-free assertion of the same value is `AMP`, a
CONJECTURE.  No microscopic member of `\mathcal S_W(\rho)` is known.

*Justification.*  D24(d)3b and claims `D24-VAL`, `AMP`, and `ML5-B`.

**⟨2⟩5. Leg-normalisation fence.**  The exact charge-created/asymptotic
leg conversion gives only `Z_\rho^{-1/2}` in the LSZ limit and
`(Z_\rho-2/N)^{-1/2}` at finite `N` on the descendant leg.  It is never used
to produce (SPEC.11).  Under both the charge-created reading of
`E^O_{\rm desc}` and the unproved jet-identification bridge, the leg-only
value is refuted against the ansatz-free slopes by factors `5.2--12.5` over
the registered band, so any proof of AMP needs another
`Z_\rho^{-1/2}` from a non-leg mechanism.

*Justification.*  D24(b)(ii), D24(d)3b, claim `AMP`, and named computation
**D24N-C8** with its `--red-halfpower` negative control.

**⟨2⟩6. Normalisation-register fence.**  Clause D24(d)2's residue is
quoted against `Q_0|h\rangle`; `E^O_{\rm desc}` is in D24(b)'s asymptotic-leg
normalisation.  The two are related by `\sqrt{Z_\rho}` only in the LSZ limit
and by `\sqrt{Z_\rho-2/N}` at finite `N`, `q\ne h`.  No step cancels them as
if they were the same vector.

*Justification.*  D24(b)(i)--(ii), D24(d)1--2, and named computation
**D24N-C8(ii)**.

**⟨2⟩7. Hard-charge fence.**  `\ell_h` remains the measured hard Ward
register.  This shard proves `\ell_h=1=|q|` only for the primitive magnon;
it states no composite `\ell_h=|q|` or `|q|/\rho` theorem.

*Justification.*  S-IDX-fin (FIN.3) and the explicit unit-charge scope of
claim `S2-2body-S`.

**⟨2⟩8. Integrability fence.**  The value supplier is the direct
two-body contact calculation, while the fixed-packet channel supplier uses
D31.  No Bethe completeness or many-body integrability assumption enters.

*Justification.*  Claims `S2-2body-S` (separated/double/adjacent equations,
no integrability) and `AC-EX-2M` under D31; claim `ML2` is a direct Jacobi
diagonalisation.

**⟨2⟩9. QED.**

## 5. The fifteen damaged r1 statement sites

### ⟨1⟩12. Correction-table theorem

**ASSUME.**  The damaged-site lists C-1--C-15 and E-1--E-19 in
`theory/verdicts/ml4-ward-n2-audit.md` §§2.3--2.4.

**PROVE.**  Every one of the fifteen entries classified **DAMAGED** in the
two superseded lane shards has an explicit corrected r2 home.

| audit site | damaged r1 content | corrected r2 home |
|---|---|---|
| C-1 | lane-A headline scalar projection at general `m_\lambda,n` | §0 ⟨1⟩1.⟨2⟩2 and §2 (FIN.1)--(FIN.2): full-sector inverse; restricted form has `\Pi_{\rm hw}` |
| C-2 | highest-weight ASSUME over general `n` feeding the scalar form | §2 ⟨1⟩3 ASSUME names the full sector and its distinct highest-weight subspace |
| C-5 | substitution of `D_{\rm hw}^\dagger D_{\rm hw}=2m` directly into `J^z_0\psi` | §2 ⟨1⟩3.⟨2⟩4--⟨2⟩5: full inverse or projected restricted input |
| C-6 | D6 formula `2Q_0J^z_0/(N-2n)` for general `n` | §2 (FIN.1); scalar specialization occurs only after ⟨2⟩6 at `n=1` |
| C-11 | nonvacuity claim using the false scalar form at every `n<N/2` | §2 ⟨1⟩3 applies at every positive full weight with (FIN.1); no scalar all-`n` claim |
| C-12 | checker demanded the false scalar residual vanish at `n=2` | §6 **SIDXR2-C1** requires the old form to fail and both registered repairs to pass |
| C-14 | proposed `S-INDEX-fin` row contained `PJ^-=QJ^z/m` generally | §7.3 proposed `S-IDX-fin` row quotes (FIN.1) and the projected (FIN.2) separately |
| C-15 | honest-status claim called the scalar formula unconditional | §0 ⟨1⟩1.⟨2⟩2 and §2 ⟨1⟩5 state exactly which registered forms are unconditional |
| E-1 | lane-B theorem bullet asserted the scalar projection in every finite sector | §2 (FIN.1)--(FIN.2), with no hybrid |
| E-2 | `for all n` ASSUME silently fed the scalar formula | §2 ⟨1⟩3 makes the full-sector quantifier explicit and scopes the scalar corollary |
| E-5 | (B4) second display | §2 (FIN.1) primary; (FIN.2) restricted |
| E-7 | projection leaf inserted the restricted scalar inverse before projecting `J^z_0` | §2 ⟨1⟩3.⟨2⟩5.⟨3⟩2 inserts `\Pi_{\rm hw}` first |
| E-15 | landmine audit cited general (B4) as settled | §4 ⟨1⟩11.⟨2⟩1 records the register trap and ⟨2⟩7 scopes `\ell_h` |
| E-17 | proposed `S-IDX-fin-B` row repeated general scalar form | §7.3 corrected unified row |
| E-19 | honest status called all of (B4)--(B7) airtight | §0 ⟨1⟩1.⟨2⟩2--⟨2⟩7 separates the complete finite proof, conditional structure, open instances, and pre-critic L5 status |

*Justification.*  Claim `ML4-Ward`, named audit computations **UXR-R1** and
**UXR-R2**, and the displayed r2 addresses in the third column.

**⟨2⟩1.**  The two additional **D-SUB** inheritance sites are also
repaired: E-11's wholesale import of (B4)--(B9) is replaced by the precise
interfaces (FIN.1)--(FIN.3) plus (PROTO-LSZ), and E-12's “every sector”
residue claim is narrowed to the one-hard residue (FIN.3).  Their downstream
coefficient is unchanged.

*Justification.*  Claim `ML4-Ward`'s one-hard consequence and
S-IDX-fin (FIN.3).

**⟨2⟩2.**  No statement inherited from the lane records uses the
former two-hard equation (18), including on the singular vector
`|\chi_\pi\rangle`; the valid all-sector replacement is (FIN.1).

*Justification.*  Claim `ML4-Ward`'s ERRATUM and named computation
**UXR-R2**, where the old equation fails by relative error one and (FIN.1)
is exact.

**⟨2⟩3. QED.**
## 6. Checker and falsifier contract

### ⟨1⟩13. Red-green checker theorem

**ASSUME.**  The checker `theory/checks/soft_index_r2_check.py` created with
this shard and the standing certificate
`theory/checks/ml4_ward_n2_check.py`.

**PROVE.**  The following gates and mutations cover every load-bearing
finite numerical identity used above, remain active under `python3 -O`, and
have the stated evidential limits.

| gate | green identity | registered red mutation | what it certifies | what it does **not** certify |
|---|---|---|---|---|
| **SIDXR2-C1** | imports the complete ML4 `n\ge2` pattern: old scalar form exact at `n=1`, false at `n\ge2`; full-sector (FIN.1) exact; restricted (FIN.2) exact; cross-register substitution nonzero; old (18) false on `\|\chi_\pi\rangle` | `--red-register-trap`; default green also runs the standing certificate's `--red`, `--red-register`, and `--red-chi` and requires each subprocess to exit 1 | the r1 F1 defect class and both valid registers | any infinite-volume or spin-`S>1/2` theorem |
| **SIDXR2-C2** | direct spin-matrix construction at `S=1/2,1,3/2`: vector-current commutator, one-hard (FIN.1), `J^z_0\|h\rangle=iv_S(h)\|h\rangle`, descendant norm `2(NS-1)`, residue `2iv_S(h)` | `--red-ward-residue` deletes the factor two in the expected residue | finite spin-`S` Ward/velocity bookkeeping in (FIN.3) | the all-model quantifier or any soft limit |
| **SIDXR2-C3** | exact time-evolution ratio one for the pure `Q_0\|h\rangle` state, and a nonzero deviation for a `Q_k\|h\rangle`, `k\ne0`, negative control | `--red-adler-anchor` substitutes `Q_k` for `Q_0` | the exact scope of (FIN.8) and the real defect that the mutation creates | the running D29 Adler limit; at `S=1/2` it remains a readout tautology |
| **SIDXR2-C4** | packet average of the exact spin-`S` multiplier has phase jet `\operatorname{sgn}/S` for `S=1/2,1,3/2,2` | `--red-s2-value` changes the target to `1/(S+1)` | the on-shell value supplier and packet-mean normalization | (MATCH-S), D29, or creator-choice identification |
| **SIDXR2-C5** | the factor product in (SPEC.4) gives `2i\mathfrak a_{\rm leg}\operatorname{sgn}\ell_h\bar k+O(\epsilon^2)` and the phase reads `2\operatorname{Re}\mathfrak a_{\rm leg}\operatorname{sgn}\ell_h` | `--red-lsz-factor` drops the Ward factor two | the algebra after (PROTO-LSZ) is assumed | (PROTO-LSZ), boundary decay, or a value of `\mathfrak a_{\rm leg}` |
| **SIDXR2-C6** | the Möbius/phase deformation (SPEC.2) preserves regularity but shifts the jet by arbitrary `c` | `--red-tgt-value` falsely requires the jet to stay fixed | that regularity-only TGT cannot determine a value | existence or compactness of any physical family |
| **SIDXR2-C7** | direct occupation-sector norms `\|Q_k\|\Omega\rangle\|^2=Z_\rho N` and `\|Q_q\|h\rangle\|^2=Z_\rho N-2`, hence the finite descendant-leg ratio `\sqrt{Z_\rho-2/N}` | `--red-leg-power` replaces the measured square-root conversion by a full `Z_\rho` factor | the D24 normalisation fence | AMP, the extra factor, `E^O_{\rm desc}`, or class membership |
| **SIDXR2-C8** | at fixed `N`, the D29 soft sample is empty below `2\pi/(c_2N)`; an interval longer than one grid spacing is nonempty | `--red-limit-order` pretends the forbidden fixed-`N` soft sample remains nonempty | the discrete-domain exclusion of the ML4-Q1 sequence | boundedness, settling, or any outer limit |

*Justification.*  Claims `ML4-Ward` and `S2-2body-S`; D24(b); named
computations **UXR-R1**, **UXR-R2**, and **SIDXR2-C1--C8**.

**⟨2⟩1.**  Green is

`python3 -O theory/checks/soft_index_r2_check.py`

and must exit zero.  The file contains no bare `assert`.  Every red flag in
the table must exit one by detecting its registered mutation; unknown or
combined flags also exit one.

*Justification.*  Named code-shape gate **SIDXR2-C0** and gates
**SIDXR2-C1--C8**.

**⟨2⟩2.**  The checker is a finite arithmetic/regression certificate.
It does not promote a theorem and tests none of: existence of D29 limit
points, D30 on a model, (PROTO-LSZ), (MATCH-S), microscopic
`\mathcal S_W(\rho)` membership, or the value of
`\mathfrak a_{\rm leg}(\rho)`.

*Justification.*  Claims `AC-EX-2M-D29`, `ML5-B`, `D24-VAL`, and `AMP`, whose
antecedent/status fences remain open.

**⟨2⟩3.**  The frozen `soft_index_probe.py` is quoted here as positive
evidence **only for P1 and P2(a)**.  P2(b)'s `\eta` gate is VOID: its
`proto` and `proto_dressed` expressions are textually identical, so it is a
no-op.  No sentence in this shard says that the probe certified the protocol
dodge “both ways.”

*Justification.*  Named code audit **tns-9z4/P2(b)-NO-OP** and the binding
probe instruction in bd `tns-v44`.

**⟨2⟩4. QED.**

## 7. MERGE PROPOSALS

Nothing in this section edits a shared file.  The orchestrator may merge the
text only after adjudicating this proposer/critic round.

### ⟨1⟩14. Exact D29/D30 and CLAIMS proposals

**ASSUME.**  The r2 binding design: lane B's finite ratio datum, lane A's
`m_\lambda` and `\ell_h` registers, a single scale-tied soft packet, a
regularity-only TGT, and an external on-shell value supplier.

**PROVE.**  The following blocks are the exact proposed shared-file text.

**⟨2⟩1. Proposed D29 (append to `definitions.md`).**

> ## D29 (PROTO: windowed, packet-smeared, charge-created ratio datum)
>
> **1. Finite anchor and hard register.**  On an `N`-site periodic
> spin-`S` ferromagnetic ring (D6 at `S=1/2`, and the Hamiltonian of claim
> `S2-2body-S` otherwise), fix `I=[a,b]\Subset(0,\pi)` in one D8 physical
> channel.  Let `\psi_{g,\sigma}` be a normalized one-magnon hard packet
> sampled from `g_\sigma\in C_c^\infty(I)` on ring momenta.  Its
> highest-weight scalar register is `m_{\lambda,N}`; on the primitive band
> `m_{\lambda,N}=NS-1`, while an abstract use carries only
> `m_{\lambda,N}/N\to\rho>0`.  In the **full hard weight sector** put
> `D_{\lambda,N}=Q_0`,
> `A_{\lambda,N}=D_{\lambda,N}^\dagger D_{\lambda,N}` on the whole sector,
> and
> `P_{\lambda,N}=D_{\lambda,N}A_{\lambda,N}^{-1}
> D_{\lambda,N}^\dagger`.  For a scalar hard band with `v_h\ne0`, record
> the measured Ward register
> `\ell_{\lambda,N}(h):=
> \langle h|Q_0^\dagger P_{\lambda,N}J^-_0|h\rangle/(2iv_h)`.
> Thus `\ell_{\lambda,N}=1` for the primitive magnon by S-IDX-fin; no
> composite formula `\ell=|q|` is part of PROTO.
>
> **2. One scale-tied soft packet and charge-created state.**  Fix
> `f\in C_c^\infty((c_1,c_2))`, `0<c_1<c_2<1`, `\|f\|_2=1`, or its
> reflection for the opposite channel.  Put
> `f_\epsilon(k)=\epsilon^{-1/2}f(k/\epsilon)` and
> `\Lambda_N(\epsilon)=(2\pi\mathbb Z/N)\cap
> \operatorname{supp}f_\epsilon`.  The only soft insertion is
> `Q[f_\epsilon]=\sum_{k\in\Lambda_N(\epsilon)}f_\epsilon(k)Q_k`, and
> the finite state is
> `\Phi_{N,\sigma}(0;\epsilon)=Q[f_\epsilon]\psi_{g,\sigma}`.  There is no
> independent carrier/width limit and no arbitrary local source.
>
> **3. Coordinate-kernel register.**  Let
> `\mathcal C_{N,S}:\mathcal H_{2,N}\to
> \mathbb C^{N\times N}_{\rm sym}` send a normalized occupation coefficient
> `c_{xy}`, `x<y`, to the two labelled entries
> `c_{xy}/\sqrt2` at `(x,y)` and `(y,x)`, and, when `S\ge1`, send a normalized
> double-occupancy coefficient `c_{xx}` to the diagonal entry `(x,x)`.
> Define the momentum kernel by the discrete Fourier transform
> `\widehat\Phi(k,h)=N^{-1}\sum_{x,y}e^{-i(kx+hy)}
> (\mathcal C_{N,S}\Phi)(x,y)`.  This fixes the convention left implicit in
> r1 and is exactly the convention used by the frozen probe's
> `grid_wavefunction`/`fft2` readout, up to the common Fourier factor that
> cancels below.
>
> **4. Windowed interacting/free readout.**  For a settling time `T`, let
> `\widehat\Phi_N(T)` be the kernel of
> `e^{-iH_ST}\Phi_{N,\sigma}(0;\epsilon)` and let
> `\widehat\Phi_N^{\rm free}(T)(k,h)=
> \widehat\Phi_N(0)(k,h)e^{-i[\omega_S(k)+\omega_S(h)]T}`.
> The window datum `W` consists of a hard-column set
> `K_h\subset I\cap(2\pi\mathbb Z/N)` and an initial position ordering
> matched to the D7 velocity/out-in labelling.  Put
> `d_N(k)=\sum_{h\in K_h}|\widehat\Phi_N^{\rm free}(T)(k,h)|^2`,
> `n_N(k)=\sum_{h\in K_h}\widehat\Phi_N(T)(k,h)
> \overline{\widehat\Phi_N^{\rm free}(T)(k,h)}`.  On the domain where
> `D_N(\epsilon):=\sum_{k\in\Lambda_N(\epsilon)}d_N(k)>0`, define
> `\mathcal R_N(k)=n_N(k)/d_N(k)` on nonzero rows,
> `d\mu_{N,\epsilon}(k,h)=
> |\widehat\Phi_N^{\rm free}(T)(k,h)|^2/D_N(\epsilon)`,
> `\mathfrak r_{N,T,W,\sigma}(\epsilon)=
> \sum_kn_N(k)/D_N(\epsilon)`, and
> `\mathcal A_{N,T,W,\sigma}(\epsilon)=
> \mathfrak r_{N,T,W,\sigma}(\epsilon)-1`.
> The packet mean is
> `\bar k_{N,T,W,\sigma}(\epsilon)=\int k\,d\mu_{N,\epsilon}`.
> Thus the aggregate is a norm projection, not pointwise division by a hard
> amplitude, and every finite datum is an explicit finite matrix quantity.
>
> **5. Exact finite diagnostics, not asymptotic assumptions.**  Record
> separately the full-sector split
> `J^-_k=P_{\lambda,N}J^-_k+(1-P_{\lambda,N})J^-_k` and both terms of the
> D6 current/contact identity; neither split is identified with the other.
> For an exact hard vector define the contact defect
> `\mathfrak D_N(k,h)=(H_S-\omega_S(k)-\omega_S(h))Q_k|h\rangle_N`.
> Finite-dimensional Duhamel gives the exact interacting-minus-free
> evolution as the time integral of `\mathfrak D_N`; no LSZ exhaustiveness,
> boundary decay, on-shell matching, value of `\mathfrak a_{\rm leg}`, wave
> operator, or completeness statement is definitional.  The pure
> `Q_0\psi_g` row ratio is the separate ADLER-Q0 anchor and is not declared
> to be the `\epsilon=0` member of this family.
>
> **6. Admissible indices and order.**  An index is admissible only if
> `N\epsilon(c_2-c_1)>2\pi`, its initial geometry matches the D7 channel,
> and its settling time lies in a declared settling/recollision sandwich
> `[T_{\min}(W,\sigma,\epsilon),c_{\rm rec}N/v_{\max}]`.
> Outer limits use admissible sequences
> `j\mapsto(N_j,T_j,W_j,\sigma_j)` at fixed `\epsilon`, with
> `N_j,T_j\to\infty`, the window padding/separation increased as declared,
> and any hard-width limit carried by `\sigma_j`; only after an outer limit
> point is selected is `\epsilon\downarrow0` taken.  At fixed `N`,
> `\Lambda_N(\epsilon)=\varnothing` when
> `c_2\epsilon<2\pi/N`; the joint ML4-Q1 sequence is not a PROTO limit.

*Justification.*  D3(a), D6--D8, D10(c), and D12(a′) fix the packet and
finite-current types; S-IDX-fin fixes the corrected Ward register; named
checker gates **SIDXR2-C1--C3,C7--C8** verify the finite diagnostics and
negative controls.

**⟨2⟩2. Proposed D30 (append to `definitions.md`).**

> ## D30 (TGT: regularity and relative compactness of D29 data)
>
> TGT is a closure property for D29 and asserts no outer limit-point
> existence.  Along a stated admissible outer subsequence, whenever the
> scalar datum has an actual cluster family on soft scales
> `E\subset(0,\epsilon_0]`, `0\in\overline E`, require:
>
> **(a) Denominator nondegeneracy.**  The aggregate free mass is nonzero and
> the normalized row measures are tight on the fixed hard window and the
> scale-tied soft support.  Rows of zero free mass carry zero measure.
>
> **(b) Component compactness.**  On the same subsequence, the normalized
> row measures, `m_{\lambda,N}/N`, `\ell_{\lambda,N}`, and every component
> named by any separately assumed decomposition have a further cluster
> point.  Their limits are written `\mu_{*,\epsilon}`, `\rho>0`, and
> `\ell_h`; in particular
> `c_1\epsilon\le|\bar k_*(\epsilon)|\le c_2\epsilon` in a one-sided
> channel.
>
> **(c) Regularity only.**  Each scalar/component cluster family admits the
> stated continuous or `C^1` extension to `\epsilon=0` required at its point
> of use, with locally uniform bounds and equicontinuous first difference
> quotients.  Relative compactness of the resulting jets may be assumed.
> This clause fixes neither an intercept nor a jet value.
>
> **(d) No hidden matching.**  TGT contains no equality with a chamber
> coefficient, no on-shell eigenvector, no `S_{\rm phys}`, no LSZ
> exhaustiveness, no value or reality condition for
> `\mathfrak a_{\rm leg}(\rho)`, and no formula for `\ell_h` in terms of a
> composite charge.  Such statements are separately named hypotheses.
>
> **(e) Optional convenience.**  Full-family convergence of the scalar and
> component data may be assumed.  It buys uniqueness of the selected limit
> function only; it cannot buy the jet value, since multiplication of
> `1+\mathcal A(\epsilon)` by `e^{ic\epsilon}` preserves (a)--(d) and shifts
> the phase jet by arbitrary `c`.

*Justification.*  D24(d) distinguishes regularity from LSZ/contact content;
named computation **SIDXR2-C6 (TGT-MOBIUS)** proves the value-shift
obstruction.

**⟨2⟩3. Proposed rows for `claims/CLAIMS.md`.**

> | S-IDX-fin-r2 | In a finite SU(2) ring positive-weight sector, with `D=Q_0` on the full sector and `A=D^\dagger D` there, `PJ^-_0\psi=2DA^{-1}J^z_0\psi` for highest-weight `\psi`; in the separately restricted register `P_{hw}J^-_0\psi=Q_0\Pi_{hw}J^z_0\psi/m_\lambda`.  For a primitive spin-`S` one-magnon leg the residue is `2iv_S(h)`.  The pure `Q_0`-created row ratio is exactly one, with no claim about the running D29 family. | SKETCH | D10, ML4-Ward | theory/soft-index-r2.md §2 | soft_index_r2_check.py SIDXR2-C1--C3 |
> | S-IDX-spec-struct-r2 | Under D29, D30, and the separately displayed uninstantiated hypothesis (PROTO-LSZ), every actual ordered limit point obeys `\mathcal A_*=2i\mathfrak a_{\rm leg}(\rho)\operatorname{sgn}(v_h-v_s)\ell_h\bar k_*+o(\epsilon)` and has an Adler zero.  The D24(d)3b constant is OPEN; no `1/\rho` value is claimed. | SKETCH | S-IDX-fin-r2, D24, ML4-A, ML5-B, D29, D30 | theory/soft-index-r2.md §3 ⟨1⟩8 | soft_index_r2_check.py SIDXR2-C5 (arithmetic only) |
> | S-IDX-spec-r2 | Add the D24-VAL membership antecedent and (MATCH-S), identifying the fixed-time D29 readout with the on-shell multiplier through `o(\epsilon)`.  For the primitive fully polarised spin-`S` band every actual limit point then has phase slope `\operatorname{sgn}(v_h-v_s)/S`; comparison supplies the conditional matched value `\mathfrak a_{\rm leg}(S)=1/(2S)=1/Z_\rho` (the existing D24-VAL row supplies `S=1/2,1,3/2,2`; other half-integer spins are a new SKETCH extension using S2-2body-S).  No D29 instance, unconditionally exhibited class member, composite-charge factor, or bridge-free AMP conclusion is claimed. | SKETCH | S-IDX-spec-struct-r2, S2-2body-S, D24-VAL, AC-EX-2M-D29 | theory/soft-index-r2.md §3 ⟨1⟩9 | soft_index_r2_check.py SIDXR2-C4,C6,C7; none tests MATCH-S |
> | S-IDX-HR-value-r2 | Under D31 on D6, the fixed-packet constructed Haag--Ruelle channel of AC-EX-2M has multiplier `S_{phys}` and its scale-tied packet average has slope `\operatorname{sgn}(v_h-v_s)/S` by S2-2body-S.  This is an on-shell value instance, explicitly not a D29 protocol instance. | SKETCH | D31, AC-EX-2M, S2-2body-S | theory/soft-index-r2.md §3 ⟨1⟩10 | soft_index_r2_check.py SIDXR2-C4 |

The SKETCH labels are deliberate proposer-pass labels; no new row is proposed
as PROVED before the required hostile round.

*Justification.*  `PRD.md`'s PROVED gate and claims `AC-EX-2M-D29`,
`D24-VAL`, and `AMP` fix the stated scopes.

**⟨2⟩4. Proposed rows for `notation.md`.**

> | `\mathcal A_{N,T,W,\sigma}(\epsilon)`, `\mathfrak r_{N,T,W,\sigma}(\epsilon)` | D29 finite charge-created connected ratio datum and its unshifted ratio `1+\mathcal A` | definitions.md D29 |
> | `\mu_{N,\epsilon}`, `\bar k_{N,T,W,\sigma}(\epsilon)` | D29 normalized free-row measure and its soft packet mean | definitions.md D29 |
> | `\Lambda_N(\epsilon)` | D29 ring-momentum sample set; empty at fixed `N` once `c_2\epsilon<2\pi/N` | definitions.md D29 |
> | `m_{\lambda,N}`, `\ell_{\lambda,N}(h)` | finite hard-sector weight and measured Ward residue register; no scalar replacement of the full-sector `A_{\lambda,N}` and no composite `\ell=\|q\|` assumption | definitions.md D29 |
> | `\mathfrak D_N(k,h)` | D29 finite contact defect `(H_S-\omega_S(k)-\omega_S(h))Q_k\|h\rangle_N` | definitions.md D29 |

*Justification.*  Proposed D29(1)--(6); no pre-existing notation row assigns
these argumented symbols another meaning.

**⟨2⟩5. QED.**

### ⟨1⟩15. Final honest status

**ASSUME.**  The whole r2 ladder.

**PROVE.**  Nothing is labelled above its evidence.

**⟨2⟩1.**  Complete finite proof: S-IDX-fin, in the two correctly
named registers, plus the scoped pure-`Q_0` anchor.

*Justification.*  Claim `ML4-Ward` and checker gates **SIDXR2-C1--C3**.

**⟨2⟩2.**  Complete conditional algebra: D29+D30+(PROTO-LSZ) imply
the structural law with the open D24 constant; adding (MATCH-S) and
`S2-2body-S` implies the primitive `1/S` value.

*Justification.*  Claims `ML5-B`, `D24-VAL`, and `S2-2body-S`; §3.

**⟨2⟩3.**  Open model work: (PROTO-LSZ), (MATCH-S), D29 limit-point
existence, D30 on a model, microscopic `\mathcal S_W(\rho)` membership,
composite `\ell_h=|q|`, and AMP.  These gaps keep every proposed new row at
SKETCH in this pre-critic pass.

*Justification.*  Claims `AC-EX-2M-D29`, `ML1`, `ML3`, `ML6`, `ML5-B`, and
`AMP`.

**⟨2⟩4. QED.**
