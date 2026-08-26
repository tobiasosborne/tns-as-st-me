# ML5 — process independence, its exact hypothesis, and a local counterexample

Status: **REFUTED** for unrestricted process independence.  A four-site local
source leaves the one-hard amplitude unchanged and changes the linear
hard-plus-soft coefficient.  The repaired conditional result is **SKETCH —
under repair after `verdicts/mquant-ml45-r1.md` objections 2--3**: ML5-A now
requires both a zero soft intercept and a zero contact first jet with an
explicit second-derivative norm, and ML5-B explicitly assumes an exhaustive
normed LSZ decomposition.  Deriving these hypotheses for a nontrivial
microscopic source class is future work (bd `tns-axg`).

This shard uses ML4-A and the FM Ward residue (11) of
`ml4-ward-reduction.md`, D6--D8, and the local contact equation (R16) of
`soft-current-recon.md`.  Bethe factorization and the closed S-matrix are not
used.

## ⟨1⟩1. Process and function-space register

**ASSUME.** Fix `I=[a,b]⋐(0,π)` and `ε_I` as in ML4, and use the source norm,
amplitudes, packet register, and relative remainder bound fixed once in
D24(a)--(b).  All plane waves are generalized kernels inside the D3/D12(a′)
smooth packets.  The physical sign is
`χ(h,k)=sgn(v(h)-v(k))`; on this `I`, `χ=+1`, but it is retained in invariant
statements.

**⟨2⟩1. PROVE.** The register above is stable under the Ward and packet
operations used below.

**⟨3⟩1.** Finite support implies D24(a)'s source norm is finite, and that norm makes sums of translated local
matrix elements absolutely convergent after compact smooth momentum smearing.
Justification: the triangle inequality and exponential domination of every
polynomial weight.

**⟨3⟩2.** Compact smooth momentum packets have `ℓ¹∩BV` position profiles.
Justification: ML4 ⟨1⟩1.⟨2⟩1 and D12(a′).

**⟨3⟩3.** Multiplication by a bounded function of `h` is bounded on `L²(I)`;
therefore all uniform pointwise Taylor bounds below imply D24(b)'s relative
bound when its source-uniform hypothesis is met.
Justification: the `L²` multiplier norm.

**⟨3⟩4. QED.**

## ⟨1⟩2. Exact first-jet criterion for process independence

Define the contact first-jet functional

\[
 \mathfrak c_h(O):=
 \left.\partial_kM_2^O(k,h)\right|_{k=0}
 -2i\,\chi(h,0)M_1^O(h).                                      \tag{3}
\]

**LEMMA ML5-A (repaired intercept-and-first-jet criterion).**

**ASSUME.** `𝒮` is a linear source class in the D24(a) norm; for every `O∈𝒮`,
`M_1^O∈L²(I)` and `M_2^O(k,·)` is `C²` for `|k|≤ε` as an
`L²(I)`-valued map.  Put

\[
 K_O(ε):={1\over2}\sup_{|q|\le ε}
 \|\partial_q^2M_2^O(q,\cdot)\|_{L²(I)}<∞.                    \tag{3a}
\]

**PROVE.** The factorisation

\[
 M_2^O(k,h)=2i\chi k\,M_1^O(h)+O_{L²(I)}(k^2)                 \tag{4}
\]

holds on `𝒮` **if and only if both**

\[
 M_2^O(0,\cdot)=0,
 \qquad \mathfrak c_h(O)=0                                   \tag{4a}
\]

in `L²(I)` for every `O∈𝒮`.  Under (4a), the remainder obeys

\[
 \|M_2^O(k,\cdot)-2i\chi kM_1^O\|_{L²(I)}\le K_O(ε)|k|².      \tag{4b}
\]

The relative form of D24(b) additionally requires
`K_O(ε)≤C_I‖M_1^O‖_{L²(I)}` uniformly on the source class.  On an affine class
`O_0+𝒱`, both conditions in (4a) must hold for every difference `V∈𝒱`, and
the base source must obey (4), with the same advertised norm control.

**⟨2⟩1. PROVE (necessity).**

**⟨3⟩1.** Evaluate (4) at `k=0` to obtain `M_2^O(0,·)=0`.
Justification: (4).

**⟨3⟩2.** Differentiate (4) at `k=0`; the `O(k²)` remainder has zero first
derivative, giving `𝔠_h(O)=0`.
Justification: (3), (4), and `C²` regularity.

**⟨3⟩3. QED.**

**⟨2⟩2. PROVE (sufficiency and norm).** If both conditions in (4a) hold, the
`L²` Taylor theorem gives (4b), hence (4).  It gives D24(b)'s relative bound only when the stated
additional inequality `K_O≤C_I‖M_1^O‖` is assumed.
Justification: Banach-space Taylor's theorem with integral remainder, (3a),
and (4a).  **⟨3⟩1. QED.**

**⟨2⟩3. PROVE (affine statement).** Amplitudes are linear in the source, so
both `M_2(0)` and `𝔠_h` are linear.  Apply ⟨2⟩1--⟨2⟩2 to `O_0+V`; the
remainder norm is the one explicitly assumed on the affine class.
Justification: (3), (3a), and source linearity.  **⟨3⟩1. QED.**

**⟨2⟩4. QED.** □

The intercept condition is independent of the first jet even within the FM
local-source model.  The four-site source `V_int` of D24(e) has
`M_1^{V_int}=0` and `∂_kM_2^{V_int}(0,h)=0`, but

`M_2^{V_int}(0,h)=3/4−(1/2)e^{-ih}+(3/4)e^{-2ih}−(1/2)e^{-3ih}`,

which is not identically zero.  Named computation **ML5-I1** in
`checks/ml4_check.py` verifies a nonzero intercept and a zero numerical first
jet.  This is the in-model red guard against the superseded first-jet-only
criterion.

Lemma ML5-A is a criterion, not an assertion that every quasi-local source
obeys it.  The next step identifies structural hypotheses that force it for a
single FM external leg.

## ⟨1⟩3. Conditional Ward/Wigner universality theorem

**ML5-B (conditional one-external-leg implication; SKETCH pending
r2).**

**ASSUME.** In addition to ⟨1⟩1, let a source class `𝒮_W` satisfy:

1. **Exhaustive normed LSZ decomposition.** In `L²(I)`, the full amplitude is
   exactly the sum of (i) the descendant external-leg term (6), (ii) the
   orthogonal-current term, and (iii) the direct source/contact term.  There
   is no additional reduced term, and the equality holds in the packet norm
   fixed in D24(b).
2. **Ward covariance.** Its descendant current residue factorizes as
   `2iv_h M_1^O(h)` for every `O∈𝒮_W`.
3. **Kinematic LSZ normalization.** The external flux factor `L(k,h)` is
   process independent, uniformly `C¹`, and
   `L(0,h)=-iχ/v_h`.
4. **Reduced-channel regularity in the target limit.** The orthogonal current
   channel contributes `O_{L²(I)}(k²)`, with its norm bounded by
   `C_I|k|²||M_1^O||_{L²(I)}`.  Fixed-volume ML4 does not prove this
   volume-uniform hypothesis.
5. **No direct soft contact.** The amputated source commutator/contact term is
   bounded by `C_I|k|²||M_1^O||_{L²(I)}`.

**PROVE.** Every `O∈𝒮_W` obeys

\[
 \boxed{M_2^O(k,h)=2i\chi k\,M_1^O(h)+O_{L²(I)}(k^2).}         \tag{5}
\]

The coefficient is the signed two-site Wigner displacement and is independent
of the hard process within `𝒮_W`.

**⟨2⟩1. PROVE (descendant external leg).** Its contribution is

\[
 (e^{ik}-1)L(k,h)[2iv_hM_1^O(h)].                              \tag{6}
\]

**⟨3⟩1.** Ward covariance supplies the bracketed residue.
Justification: hypothesis 2 and ML4 equation (11).

**⟨3⟩2.** `e^{ik}-1=ik+O(k²)` and
`L(k,h)=-iχ/v_h+O_I(k)`; since `v_h` is bounded away from zero on `I`, (6)
equals `2iχ kM_1^O+O_{L²(I)}(k²)`.
Justification: hypothesis 3, compactness of `I`, and Taylor's theorem.

**⟨3⟩3. QED.**

**⟨2⟩2. PROVE (exhaustive remainder).** The orthogonal current contribution
is `O(k²)` by hypothesis 4, and the direct source term is `O(k²)` by
hypothesis 5.  Hypothesis 1 states that these are **all** terms besides
⟨2⟩1.
Justification: hypotheses 1, 4, and 5.  **⟨3⟩1. QED.**

**⟨2⟩3. PROVE (5).** Add ⟨2⟩1 and ⟨2⟩2.  Its phase slope is `2χ`, so the
Wigner displacement has signed value `2χ` sites.
Justification: linearity and the definition of Wigner displacement as the
momentum derivative of the scattering phase.  **⟨3⟩1. QED.**

**⟨2⟩4. QED.** □

The velocity-domain condition fixes `χ` and the external flux orientation.
It does not suppress the orthogonal current and does not constrain a direct
contact source.  Hypotheses 1, 4, and 5 are explicit assumptions, not
consequences of the finite-volume Ward identity.

> **EXPLORATION ML5-W (what remains).**
>
> A nonempty class `𝒮_W` containing more than symmetry-generated external-leg
> insertions has not been derived from microscopic source covariance.  One
> needs an LSZ Ward identity for the quasi-local source showing that its
> amputated commutator has zero first jet, not merely that it is regular.
> For two hard magnons one additionally needs ML4-3; a sum of external Wigner
> displacements is conditional on the absence of degenerate three-body
> channels.  Charge algebra plus kinematics fixes (6), but it does not prove
> hypotheses 1 and 5.

## ⟨1⟩4. Sharp local counterexample to unrestricted ML5

On four consecutive sites define

\[
 D:=S^-_0S^-_1-S^-_1S^-_2+S^-_2S^-_3-S^-_0S^-_3,\qquad
 O_\eta:=S^-_0+\eta D .                                       \tag{7}
\]

Every `O_η` is local and therefore belongs to D24(a).  It is deliberately not a
single `SU(2)`/`S^z` tensor source: it mixes one- and two-lowering components.

Let the incoming-normalized physical two-magnon wave in the ordered chamber be

\[
 \Psi_{k,h}(x,y)=s(k,h)e^{i(kx+hy)}+e^{i(hx+ky)},              \tag{8}
\]

where `s` is fixed only by the local contact equation (R16).  Define source
form-factor amplitudes

\[
 M_1^{O_\eta}(h)=\langle h|O_\eta|\Omega\rangle,\qquad
 M_2^{O_\eta}(k,h)=\langle\Psi_{k,h}|O_\eta|\Omega\rangle .   \tag{9}
\]

Overall delta-normalization factors, common to all `η`, are suppressed.

**⟨2⟩1. PROVE.** `M_1^{O_η}(h)` is independent of `η`, while

\[
 M_2^{O_\eta}(k,h)
 =\eta\{2i(1-e^{-3ih})k+O_I(k^2)\}.                           \tag{10}
\]

Thus varying `η` changes the linear soft coefficient without changing the
hard process amplitude.

**⟨3⟩1.** `D|Ω⟩` lies in the two-magnon sector, so it has zero overlap with a
one-magnon state; `S^-_0|Ω⟩` lies in the one-magnon sector, so it has zero
overlap with (8).
Justification: orthogonality of distinct `S^z` sectors.

**⟨3⟩2.** The coefficient of every one-site marginal of `D|Ω⟩` vanishes:
at sites `0,1,2,3` the incident pair coefficients are respectively
`1-1`, `1-1`, `-1+1`, and `1-1`.
Justification: direct inspection of (7).

**⟨3⟩3.** Since `s(0,h)=1`, ⟨3⟩2 gives
`⟨Ψ_{0,h}|D|Ω⟩=0` for every `h`.
Justification: insert (8) at `k=0`; each pair contributes
`e^{-ihx}+e^{-ihy}`.

**⟨3⟩4.** Differentiating (R16) at zero gives `s'(0,h)=2i`, uniformly on
`I`; hence the derivative of the bra coefficient is `-2i`.
Justification: the coefficient-of-`k` computation in
`soft-current-recon.md` ⟨1⟩4.⟨2⟩3, which used only (R16).

**⟨3⟩5.** Differentiating the four terms gives

\[
 -i\sum_{(x,y)}d_{xy}[(2+x)e^{-ihy}+y e^{-ihx}]
 =2i(1-e^{-3ih}),                                             \tag{11}
\]

with `(d_{01},d_{12},d_{23},d_{03})=(1,-1,1,-1)`.
Justification: substitute the four pairs; the constant and `e^{-3ih}` terms
survive and the `e^{-ih},e^{-2ih}` terms cancel.

**⟨3⟩6.** The contact solution is analytic uniformly on `I`, so Taylor's
theorem upgrades (11) to (10) with an `L²(I)` `O(k²)` remainder.
Justification: `|e^{ih}-1|≥2sin(a/2)` and compactness.

**⟨3⟩7. QED.**

**⟨2⟩2. PROVE (refutation).** Choose an `h`-packet supported where
`1-e^{-3ih}≠0`.  Then `O_η-O_0=ηD` leaves `M_1` fixed but has nonzero contact
first jet, so ML5-A fails on the local source class.

**⟨3⟩1.** Equation (10) gives
`𝔠_h(ηD)=2iη(1-e^{-3ih})`, nonzero on the chosen support.
Justification: (3) and (10), noting `M_1^D=0`.

**⟨3⟩2.** Lemma ML5-A says vanishing of this functional is necessary for
process independence.
Justification: ML5-A necessity.  **⟨3⟩3. QED.** □

This counterexample does not contradict the FM two-body phase O7--O9.  It
shows that a local source can emit an independent soft contact term.  ML4
controls `(e^{ik}-1)R`, whereas (7) is not multiplied by that current
difference.  Source covariance/no-contact is therefore necessary, not
cosmetic.

## ⟨1⟩5. Numerical certificate

**⟨2⟩1. PROVE.** `theory/checks/ml4_check.py`, normally and with `python3 -O`,
checks (10)--(11) in addition to ML4.

**⟨3⟩1.** It solves (R16) numerically, finds the exact soft zero to
`3.140e-16`, and compares the numerical derivative to (11) at three hard
momenta with maximum error `9.963e-06`.
Justification: the recorded optimized-mode run.

**⟨3⟩2.** It also evaluates `V_int`: the minimum sampled intercept magnitude
is nonzero while the centered numerical first jet vanishes, killing the
superseded first-jet-only sufficiency criterion.
Justification: named computation **ML5-I1** and the recorded optimized-mode
run.

**⟨3⟩3.** Every failure uses `SystemExit`, so optimization cannot remove it.
Justification: inspection of the checker.  **⟨3⟩4. QED.** □

## ⟨1⟩6. ML5 verdict

1. **REFUTED:** universality over all local or exponentially quasi-local
   sources.  The explicit counterexample is (7), with coefficient (10).
2. **SKETCH pending r2:** ML5-A, the necessary-and-sufficient
   zero-intercept-and-zero-first-jet criterion with the explicit `K_O` norm.
3. **SKETCH pending r2:** ML5-B.  Under the exhaustive normed LSZ
   decomposition, Ward residue plus external flux kinematics gives the signed
   Wigner coefficient `2χ`; reduced-channel regularity and the no-contact
   hypothesis bound every remaining term.
4. **CONJECTURE / future work:** deriving the exhaustive decomposition and
   no-contact condition for a useful microscopic covariant source class, and
   extending it to two hard magnons without
   three-body integrability.  The surviving unconditional statement is the
   FM two-body Hamiltonian result O7--O9, not process independence for arbitrary
   sources.
