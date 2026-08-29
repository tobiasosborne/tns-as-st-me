# S-INDEX (lane B) — the soft law as a constraint on limit points of the charge-created protocol datum

> **ERRATUM (orchestrator, 2026-08-29, bd `tns-iu5`).**  D24(d) clause 3 is
> split and the value of the soft-leg amputation constant `𝔞_leg(ρ)` is
> RETIRED from the definition: `𝔞_leg(ρ)` is OPEN at every density, carried
> as `claims/CLAIMS.md` rows `D24-VAL` (conditional) and `AMP` (CONJECTURE).
> Flux/leg-density text in this shard that displays a value of the constant,
> or the soft coefficient `2` off `ρ = 1/2`, is superseded.  Merged text of
> record: `theory/verdicts/d24d3-adjudication-r5.md` §5.

Status: **SKETCH** (self-status; only the L6 loop promotes).  Independent
S1-B prover shard (Fable lane).  Lane discipline: this file is the only
writable artifact of this lane; `theory/soft-index.md` (the codex lane) was
NOT read.  All shared-file changes are in MERGE PROPOSALS only.

Dependencies (cite, never redefine — L4): D3(a), D6--D8, D10, D12(a′),
D24(a)--(e), D25, D26; claims ML2, ML4-A, ML4-Ward, ML5-A, ML5-B, S2-2body,
S2-2body-S, OR2, G0-soft-r1 (REFUTED — fence), ML5 (REFUTED — fence);
`theory/soft-current-recon.md` (R1)--(R19); `theory/ml4-ward-reduction.md`
(1)--(17) and ML4-Q1; `theory/ml5-universality.md` ⟨1⟩1--⟨1⟩4;
`theory/spin-s-twomagnon.md` (spin-S two-magnon equations);
`theory/memory-index.md` ⟨1⟩1, ⟨1⟩4--⟨1⟩8 (hypothesis-discipline precedent
for D29-B/D30-B).  No integrability, no Bethe completeness (ML2 is cited
instead), no `ρ∈½ℤ` anywhere.

---

## §0. Statement

**Campaign register.** *Symmetry fixes the soft law; the ansatz supplies the
kinematics; dynamics only picks the values.*  This shard proves the
constraint half: any subsequential limit point of the windowed,
packet-smeared, charge-created soft amplitude datum obeys the Adler zero and
has its phase slope pinned to the leg-charge datum `|q|/ρ` — with NO wave
operators, NO completeness, NO channel inventory assumed.  Existence of
limit points is Lane S2's / the probe's burden, except for the finite-volume
nonvacuity exhibit proved unconditionally in ⟨1⟩1.

**Order of limits (binding, stated once).** Finite-volume data are indexed
by `(N, T, W, σ; ε)`: ring size `N`, settling time `T`, readout window `W`
(the momentum-window data `(K_h,\;T\text{-placement})` of (B3): hard-column
set and the position of `T` inside the settling interval), hard packet
width register `σ` (fixed compact support in `I=[a,b]⋐(0,π)`), soft scale
`ε`.  *(The target brief's index `W` is refined here into the pair
`(T,W)`; the target's limit-order sentence is unchanged under this
refinement.)*  Every limit is taken along a subsequence
`j↦(N_j,T_j,W_j,σ_j)` with `N_j→∞`, `T_j→∞`, and the settling/recollision
sandwich `T_{\min}(W_j,σ_j)≤T_j≤c_{rec}N_j` of ⟨1⟩3, at FIXED `ε`, and
`ε→0` STRICTLY LAST.  No `ε`-derivative is taken before the
`j`-subsequence is fixed.  The soft limit commutes with nothing (ML4-Q1);
see ⟨1⟩3 for the displayed immunity line.

### H-SIDX (hypotheses)

1. **(H-SIDX.1, setting.)** The concrete anchor is the spin-`S` isotropic
   ferromagnet `H_S=−JΣ_x(S_x·S_{x+1}−S²)` of `spin-s-twomagnon.md`
   (at `S=1/2` this is D6), on the `N`-site ring, with the D7
   ordered-coordinate register and the D8 half-zone soft convention.  The
   abstract level of ⟨1⟩5 assumes only: an SU(2)-invariant finite-range `H`
   (D10 register) on a chain with on-site charge `S^z` obeying D26(INT), a
   fully polarized highest-weight vacuum `|Ω⟩` with charge density
   `ρ:=ω_Ω(S^z_x)>0` carried as a FREE real parameter (no `ρ∈½ℤ` is
   assumed; in the concrete anchor `ρ=S`), and one isolated magnon band over
   it.  The hard leg is one magnon of charge `q` relative to the vacuum
   (`q=−1` in `S^z` units for `S^-`-created legs; only `|q|` enters the
   slope law).
2. **(H-SIDX.2 = D29-B, the protocol object.)** The datum family
   `𝒜_{N,W,σ}(ε)` of the D29-B proposal below: the window-resolved ratio of
   outgoing- to incoming-chamber coordinate readouts of the energy-filtered
   charge-created state, minus one.  The soft leg is created by `Q[f_ε]`
   ONLY — the smeared broken charge itself; no arbitrary local source (that
   is how the O_η freedom of D24(e) is structurally removed; sources
   re-enter only through ⟨1⟩6/ML5-A).
3. **(H-SIDX.3 = D30-B, tightness/regularity.)** The (LR)-analogue clauses
   (a),(b) (+(d) at `S≥1`) of the D30-B proposal below for (S-IDX.1a),
   and the package (e) for (S-IDX.1b), assumed along the stated
   subsequence.  NO convergence of the full family is assumed; NO
   scattering theory is assumed; no clause fixes the value of any
   scattering datum.  The optional clause (c) buys only uniqueness of the
   limit function, mirroring D27 clause 3.

### THEOREM S-INDEX-B

Under H-SIDX:

- **(S-IDX.0) Finite-volume soft-index identity (UNCONDITIONAL — no D29/D30
  needed).**  In every finite sector `ℋ_{n,N}` with `M:=ρN−n|q| >0`, for
  every hard packet `ψ∈ker S^+`, the descendant-channel component of the
  charge-created soft current datum is EXACTLY the charge datum:
  `P_{n,N}J^-_0ψ = (2/(2M))\,Q_0J^z_0ψ` (ML4-Ward (9)--(11) at `S=1/2`,
  where `2M=N−2n`; proved for the abstract H-SIDX.1 register in ⟨1⟩2), with
  the offset bookkeeping `N−2n` vs `N−2` vs `2ρN` done in public and the
  kinematic factor `(e^{ik_s}−1)` separated explicitly via (R10) — the two
  factors are kept distinct (G0-soft-r1 fence).  Restated for the D29-B
  datum: the `ε=0` fiber of the datum exists unconditionally and equals `0`
  (exact finite-`N` Adler value), because `Q_0ψ` is an exact eigenpacket
  with chamber ratio exactly `1` (R7).
- **(S-IDX.1a) Subsequential soft law (concrete anchor; conditional on
  D29-B + D30-B).** For ANY subsequential limit point `𝖲^*(·)` of the datum
  family along the stated order, on the spin-`S` anchor:
  (i) *Adler zero:* `𝖲^*(0)=0` (equivalently the ratio limit `𝔯^*(0)=1`),
      from the current/contact structure (O6/OR2 + (R16)-uniformity), not
      from the bare difference factor;
  (ii) *slope rigidity:* the first-order jet exists along the subsequence
      and `∂_{k_s}\arg 𝔯^*|_0 = \mathrm{sgn}(v_h−v_s)\,|q|/ρ`; on D8 with
      `ρ=S` this is `1/S`, and `2` at `S=1/2`;
  (iii) *law uniqueness:* the value of the jet is the same for every
      subsequence along which D30-B holds; the LIMIT need not be unique,
      and full-family convergence is bought only by D30-B's optional
      convenience clause (exactly D27's discipline).
  NO claim that limit points exist; bound states and extra bands are
  allowed — they can empty a subsequence or carry different hard data; they
  do not break the constraint.
- **(S-IDX.1b) Abstract descendant-projected law.** In the abstract
  H-SIDX.1 register (no contact equation available), the same conclusion
  holds for the DESCENDANT-PROJECTED datum: every limit point of the
  `P_{n,N}`-projected family obeys (i)--(ii) with the same charge datum
  `|q|/ρ`, PROVIDED the orthogonal-channel family obeys the ML4-A-style
  regularity clause (TGT2′) of D30-B.  The orthogonal contact vector is
  NONZERO at every finite `N` (R15); it is controlled by hypothesis on the
  LIMIT family, never assumed away.  This is the honest fallback of the
  target brief, stated prominently as such.
- **(S-IDX.2) Source bridge (corollary; cite ML5-A, do not reprove).**  Any
  D24(a) source `O` with `M_2^O(0,·)=0` and `𝔠_h(O)=0` inherits
  (S-IDX.1a)(i)--(ii) with `M_1^O` in place of the charge-created hard
  amplitude, in the per-`(N,W,σ)` D24(b) norms along the same subsequence.
  Unrestricted sources remain REFUTED (ML5, O_η) — nothing here implies
  source universality.
- **(S-IDX.3) Consistency anchors (any mismatch = FATAL bug).**
  (a) On D6--D8 the law reduces term by term to S2-2body's boxed
  (R17)--(R18).  (b) On the spin-`S` family it reduces to S2-2body-S's
  slope `sgn(v_h−v_s)/S`.  (c) If two-magnon wave operators are ASSUMED
  (ML1 as a hypothesis, not proved), limit points exist, D30-B holds, and
  (S-IDX.1a) reproduces the S2 EXPLORATION box of
  `soft-current-recon.md` ⟨1⟩6 — the old conjecture becomes the
  value-computation corollary of the new theorem.

### D29-B (proposal — the windowed charge-created protocol datum)

*(Exact merge text in MERGE PROPOSALS §M1; the working form is (B1)--(B3)
of ⟨1⟩1.)*  Sketch of the object: fix `I=[a,b]⋐(0,π)`, a hard packet
`g∈C_c^∞(I)` sampled on ring momenta with the ML4 norm (1), a one-sided
soft profile `f∈C_c^∞((c_1,c_2))`, `0<c_1<c_2<1`, rescaled as
`f_ε(k)=ε^{-1/2}f(k/ε)` and sampled on ring momenta ONLY (no
interpolation; the sample set is empty unless `Nε≳2π/(c_2−c_1)` — this is
the structural ML4-Q1 immunity, ⟨1⟩3).  The charge-created state is
`Φ_{N,σ}(0;ε):=Q[f_ε]\,ψ_{g,σ}` (D10(c) smearing of the broken charge
itself; a finite local sum on the ring; NO source freedom).  The readout is
the interacting-vs-free momentum-kernel pairing at the settling time `T`:
the interacting kernel `Φ̂_N(T)` of `e^{-iHT}Φ` is paired row-by-row
against the band-data free reference
`Φ̂^{free}_N(T)=Φ̂_N(0)e^{-i[ω(k)+ω(h)]T}` on the window `W=(K_h,·)`, and
the datum is the weighted row aggregate `𝔯_{N,T,W,σ}(ε)` of (B3), with
`𝒜_{N,T,W,σ}(ε):=𝔯_{N,T,W,σ}(ε)−1`.  Everything is a finite exact
linear-algebra object at each `(N,T,W,σ;ε)` — computable by ED with no
wave operators (probe-compatible: `soft_index_probe.py` `phase_function`
implements exactly this readout).

### D30-B (proposal — tightness/regularity of the datum family)

*(Exact merge text in MERGE PROPOSALS §M2; authoritative clause forms in
⟨1⟩4's ASSUME and ⟨1⟩5's ASSUME.)*  Clauses along a stated admissible
subsequence `j↦(N_j,T_j,W_j,σ_j)`:
**(a)=(TGT1) row-mass nondegeneracy** — free row masses dominate the
declared row weights;
**(b)=(TGT2) readout settling (the LR-analogue; load-bearing)** — the
row readouts settle onto the D7 chamber out/in ratios of SOME exact
near-shell eigenvectors (`δ_j→0` spectral window, `η_j→0` defect);
the clause fixes the value of NO ratio — values are computed from the
PROVED contact algebra, which is the theorem's content;
**(c)=(TGT3) convenience clause (optional)** — full-family convergence
per `ε`; buys uniqueness of the limit function only, exactly as D27
clause 3 (the jet VALUE is subsequence-free without it);
**(d)=(TGT4) spin-`S≥1` representability** — near-shell eigenvectors are
regular scattering vectors and the window excludes the bound band(s);
a THEOREM at `S=1/2` (SIB-L1), assumed at `S≥1`;
**(e) abstract descendant package** (used only by (S-IDX.1b)):
(H-band) `N`-uniform `O(k)` defect bound; the transit bound (tr′); and
D24(d) clauses 1, 3, 4 transplanted ((1′),(3′),(4′)) — clauses 2 and 5
are NOT assumed, they are discharged by the protocol (⟨1⟩5.⟨2⟩1).

---

## ⟨1⟩1. Register: the datum, well-definedness, and finite-volume nonvacuity

**ASSUME.** H-SIDX.1 at the concrete anchor: the spin-`S` ring
(`H_S=−JΣ_x(S_x·S_{x+1}−S²)`, `spin-s-twomagnon.md` Statement; `S=1/2` is
D6), `N>3`.  Fix `I=[a,b]⋐(0,π)` and `ε_I>0` exactly as in
`ml4-ward-reduction.md` ⟨1⟩1 (for `h∈I`, `|k|≤ε_I`: `h+k∈(0,π)`,
`v(h)>v(k)`, `h+k≠π`).  Hard packets are samples of `g∈C_c^∞(I)` in the
ML4 norm (1); soft profiles are `f_ε(k)=ε^{-1/2}f(k/ε)` with
`f∈C_c^∞((c_1,c_2))`, `0<c_1<c_2<1`, `0<ε≤ε_0<ε_I` — one-sided (`σ=+1`
register of D8; the `σ=−1` datum uses `supp f⊂(−c_2,−c_1)` and is carried
by the same steps).  All ring momenta lie in `2πℤ/N`; plane waves are
kernels inside these packets (D3(a), D12(a′)).

**⟨2⟩1. PROVE (the charge-created state is finite, exact, and sector-free
of source ambiguity).**  Let `Λ_N(ε):=(2πℤ/N)∩supp f_ε` and

\[
 ψ_{g,σ}:=c_{g,N}\sum_{h∈I∩(2πℤ/N)}g_σ(h)\,|h⟩_N,\qquad
 Φ_{N,σ}(0;ε):=Q[f_ε]\,ψ_{g,σ}
 =c_{g,N}\sum_{k∈Λ_N(ε)}\sum_h f_ε(k)g_σ(h)\,Q_k|h⟩_N,   \tag{B1}
\]

with `c_{g,N}` the `‖·‖_{I,N}`-normalizer and `Q_k=Σ_xe^{ikx}S^-_x`
(soft-current-recon ⟨1⟩1, extended to spin `S` verbatim: `S^-_x` is the
on-site lowering operator).  Then: (i) `Φ_{N,σ}(0;ε)` is a finite exact
vector in the two-magnon sector `ℋ_{2,N}`; (ii) it is NONZERO whenever
`Λ_N(ε)≠∅`, i.e. whenever `Nε≥2π/c_… := 2π/(c_2−c_1)` up to endpoint
placement (sufficient: `Nε>2π/(c_2−c_1)`); (iii) no D24(e)-type source
freedom exists in (B1): the only inserted operator is the broken charge
itself.

**⟨3⟩1.** (i): `Q_k` maps the one-magnon sector into `ℋ_{2,N}`
(`[S^z_{tot},Q_k]=−Q_k`), and both sums are finite.
*Justification.* D10(c), D6/`spin-s-twomagnon.md` sector structure.

**⟨3⟩2.** (ii): the momentum kernel of (B1) is exact: for ring momenta
`k≠h`,

\[
 Q_k|h⟩_N=\frac{1}{\sqrt N}\sum_{x<y}
 \big[u_{kh}e^{i(kx+hy)}+u_{hk}e^{i(hx+ky)}\big]|x,y⟩
 +(\text{double-occupancy component, }S≥1),                  \tag{B2}
\]

with `u`-weights fixed by the `S^-` matrix elements (`u_{kh}=u_{hk}=√(2S)`
relative to the normalized occupation basis at `S≥1`; at `S=1/2` (B2) is
exactly (R3) and the double-occupancy component is absent).  Distinct ring
momenta make the kernels linearly independent, so (B1)`≠0` when the sum is
nonempty.  An interval of length `ε(c_2−c_1)` contains a ring momentum
whenever `Nε(c_2−c_1)>2π`.
*Justification.* (R3) at `S=1/2`; `spin-s-twomagnon.md` ⟨1⟩1 (occupation
amplitudes) at `S≥1`; Fourier independence on the ring; pigeonhole on
`2πℤ/N`.

**⟨3⟩3.** (iii): (B1) contains no adjustable source: the map
`(f_ε,g)↦Φ` is fixed by `Q[·]` alone.  The D24(e) deformation `O_η=S^-_0+ηD`
changes a SOURCE-created two-magnon component `D|Ω⟩`; in the protocol
register the leg is created on top of the hard ONE-magnon state by the
total broken charge, and adding `ηD` to the CHARGE is not a gauge freedom
of the protocol — `Q[f_ε]` is the unique D10(c) smearing of the symmetry
generator.  (The quantitative dodge certificate is the probe's P2(b),
`η`-insensitivity `≤10^{-10}`; the structural statement here is that no
`η` appears in (B1) to vary.)
*Justification.* D10(c), D24(e), and inspection of (B1).

**⟨3⟩4. QED.**

**⟨2⟩2. PROVE (the D29-B datum is well defined at every finite index).**
Define, for `T>0` and a hard-column window `K_h⊂I∩(2πℤ/N)`:

- interacting readout kernel: `Φ̂_{N}(T)(k,h)`, the coefficient of the
  symmetrized momentum pair `(k,h)` in `e^{-iH_ST}Φ_{N,σ}(0;ε)`;
- free reference kernel:
  `Φ̂^{free}_{N}(T)(k,h):=Φ̂_{N}(0)(k,h)\,e^{-i[ω_S(k)+ω_S(h)]T}`, using
  ONLY the exact one-magnon band `ω_S(k)=2JS(1−\cos k)` — band data, no
  wave operators;
- row pairing and datum:

\[
 \mathfrak r_{N,T,W,σ}(ε):=
 \frac{\sum_{k∈Λ_N(ε)}w_ε(k)\,\mathcal R(k)}
      {\sum_{k∈Λ_N(ε)}w_ε(k)},\qquad
 \mathcal R(k):=\frac{\sum_{h∈K_h}\Phî_N(T)(k,h)\,
 \overline{\Phî^{free}_N(T)(k,h)}}
      {\sum_{h∈K_h}|\Phî^{free}_N(T)(k,h)|^2},              \tag{B3}
\]

with row weights `w_ε(k):=|f_ε(k)|^2‖g_σ‖^2`-induced (the free-kernel row
masses), and `𝒜_{N,T,W,σ}(ε):=\mathfrak r_{N,T,W,σ}(ε)−1`.  `W` denotes
the readout window data `(K_h, T\text{-window placement})`; the settling
constraint on `T` is part of the subsequence discipline (⟨1⟩3), not of
well-definedness.  Then (B3) is defined whenever `Λ_N(ε)≠∅` and the row
denominators are nonzero — and the denominators are AUTOMATICALLY nonzero:
`|Φ̂^{free}(T)(k,h)|=|Φ̂(0)(k,h)|` and the `t=0` kernel is the explicit
nonzero (B2)-kernel `∝f_ε(k)g_σ(h)` on `Λ_N(ε)×K_h` (plus an
`O(1/N)`-overlap correction off the diagonal).  Hence (TGT1) is needed
only for the LOWER bound uniform along a subsequence, not for
definedness at fixed index.

**⟨3⟩1.** The free kernel has time-independent modulus, equal to its
`t=0` value; the `t=0` kernel restricted to `Λ_N(ε)×K_h` is the
symmetrized product `c_{g,N}f_ε(k)g_σ(h)u_{kh}·(1+O(N^{-1}))`, where the
`O(N^{-1})` is the non-orthonormality of the pair basis (the (R3)-norm
computation: diagonal `N−1`… at `S=1/2`, i.e. relative defect `O(1/N)`).
Nonvanishing for `N≥N_1(f,g)` follows.
*Justification.* (B2); soft-current-recon ⟨1⟩2.⟨2⟩1 (norm `N−2` for
distinct ring momenta, `S=1/2`) and the same finite Fourier computation at
spin `S`; named computation **SIB-C0** (CHECKER SPEC).

**⟨3⟩2.** Every object in (B3) is a finite-dimensional exact
linear-algebra quantity (dense `H_S` on `ℋ_{2,N}`, exact exponential,
finite Fourier transform): computable by ED with no scattering theory.
This is the probe-compatibility clause of the target brief (D29
requirement (i)); `theory/checks/soft_index_probe.py` `phase_function`
implements exactly this readout (its `ratio` is the row kernel pairing of
(B3)).
*Justification.* Inspection of (B3) and of the pre-registered probe.

**⟨3⟩3. QED.**

**⟨2⟩3. PROVE (nonvacuity at finite index; the vacuous-truth landmine,
first half).**  For every `ε∈(0,ε_0]` there exist `N,T,W,σ` such that
`𝒜_{N,T,W,σ}(ε)` is defined; the finite-index family is therefore
nonempty at every soft scale, and the pre-registered probe exhibits
recorded instances (S=1/2: extrapolated slope `1.9929`; `S=1`: `1.0217`,
out-of-sample; `soft_index_probe_results.json`).  What is NOT claimed here:
existence of subsequential LIMIT points of the family — that is Lane S2's
/ D30-B's burden, and (S-IDX.1a/b) are constraints conditional on D30-B.
Silence on this point is a MAJOR objection per the target brief; the split
is stated here once and repeated in HONEST STATUS.

**⟨3⟩1.** Take `N>max(N_1(f,g), 2π/(ε(c_2−c_1)))` and any `T>0`: ⟨2⟩2
gives definedness.
*Justification.* ⟨2⟩1--⟨2⟩2.

**⟨3⟩2. QED.**

## ⟨1⟩2. (S-IDX.0): the unconditional finite-volume soft-index identity

**ASSUME.** The abstract H-SIDX.1 register: `H` translation invariant,
finite range, SU(2)-invariant on-site (D10), on the `N`-ring; fully
polarized highest-weight vacuum `|Ω⟩` with `H|Ω⟩=0` and charge density
`ρ=ω_Ω(S^z_x)>0`; `Q_0=S^-_{tot}`, `J^-_0=Σ_xj^-_{x|x+1}` the D10(a) cut
current of `S^-`, `J^z_0` the same construction for `S^z`.  Sector
`ℋ_{n,N}` (`n` lowerings), `M:=ρN−n` (`S^z_{tot}=M` there).  No dynamics
beyond the commutators below; no `k_s` expansion; every `N`, every
`n` with `M>0`, every packet.  *(At the concrete anchor `ρ=S`; at
`S=1/2`, `2M=N−2n` and everything below is ML4-Ward (8)--(11) verbatim —
those steps are cited, not reproved.  The point of this section is that
the identity is an SU(2)/density statement, with `ρ` FREE.)*

**⟨2⟩1. PROVE (vector Ward commutator, abstract register).**
`[S^+_{tot},J^-_0]=2J^z_0`.

**⟨3⟩1.** For each bond term, `[S^+_{tot},h_x]=0` and
`[S^+_{tot},S^-_y]=2S^z_y`; the cut current is a finite sum of terms
`−[h_x,Σ_{y≤m}S^-_y]`, so Jacobi gives
`[S^+_{tot},j^-_{m|m+1}]=−[h_x,Σ_{y≤m}2S^z_y]`-summed `=2j^z_{m|m+1}`.
*Justification.* D10(a) (cut current, finite range), SU(2) invariance
`[h_x,Σ_{y∈supp}q_y]=0`, and `[S^+,S^-]=2S^z` on-site; this is the
computation of ML4 ⟨1⟩3.⟨3⟩1 with (R1) replaced by the D10(a) general
form.

**⟨3⟩2. QED.**

**⟨2⟩2. PROVE (index normalization and Ward projection; bookkeeping in
public).**  On `ℋ^{hw}_{n,N}:=\ker S^+∩ℋ_{n,N}` with `M>0`:

\[
 D_{n,N}^†D_{n,N}=2M\,\mathbb 1,\qquad
 P_{n,N}J^-_0=\frac{1}{M}\,Q_0J^z_0
 \quad\text{on }ℋ^{hw}_{n,N}.                                 \tag{B4}
\]

**The three normalizations, displayed once:**
`2M = 2(ρN−n)` (density form, `ρ` free) `= N−2n` (at `ρ=1/2`, the
ML4-Ward form) `= 2SN−2n` (concrete spin-`S` anchor, `ρ=S`); the one-hard
case `n=1` gives `N−2` at `S=1/2` — the (R15) denominator.  The `2` in
`2M` is the su(2) structure constant of ⟨2⟩1 and is NOT the slope `2`;
the slope datum of (S-IDX.1) is `|q|/ρ`, which equals `2` only at
`ρ=1/2`.  Conflating the two `2`s is the first place the critic will
look; they are kept separate everywhere below.

**⟨3⟩1.** For `ψ∈ℋ^{hw}_{n,N}`:
`‖Q_0ψ‖²=⟨ψ,S^+S^-ψ⟩=⟨ψ,[S^+,S^-]ψ⟩=2⟨ψ,S^z_{tot}ψ⟩=2M‖ψ‖²`.
*Justification.* `S^+ψ=0`, `[S^+,S^-]=2S^z`, `S^z_{tot}=M` on the sector;
at `S=1/2` this is ML4 (9) (`2M=N−2n`).

**⟨3⟩2.** `D^†J^-_0=2J^z_0+J^-_0S^+` (expand `S^+J^-_0` with ⟨2⟩1); on
`\ker S^+` the second term dies, and inserting into the projection
`P=D(D^†D)^{-1}D^†` with ⟨3⟩1 gives (B4).
*Justification.* ⟨2⟩1, ⟨3⟩1, and orthogonal projection onto the range of
an injective map; ML4 (8)--(10) at `S=1/2`.

**⟨3⟩3. QED.**

**⟨2⟩3. PROVE (one-hard specialization: charge datum × velocity datum).**
For every nonzero ring momentum `h`, in the abstract register:

\[
 ⟨h|J^z_0|h⟩_N=i\,v(h),\qquad
 P_{1,N}J^-_0|h⟩_N=\frac{i\,v(h)}{M}\,Q_0|h⟩_N,\quad M=ρN−1,   \tag{B5}
\]

and diagonally for every hard packet supported away from `h=0`.  The
descendant-channel component of the charge-created soft current datum is
therefore EXACTLY (leg-charge datum `1/M`) × (hard velocity datum
`iv(h)`) — no dynamics, no `k_s` expansion.

**⟨3⟩1.** One-magnon exactness: `ℋ_{1,N}` is spanned by `|k⟩_N` with
`H|k⟩_N=ω(k)|k⟩_N` (translation invariance + `S^z` conservation), and
`ω(0)=0` because `Q_0|Ω⟩=√{2ρN}\,|0⟩_N` and `[H,Q_0]=0`, `H|Ω⟩=0` — the
`k=0` magnon is the global-rotation descendant (Goldstone leaf).
*Justification.* H-SIDX.1; SU(2) invariance; at the anchor,
`ω_S(k)=2JS(1−\cos k)` (`spin-s-twomagnon.md` Statement, D6 at `S=1/2`).

**⟨3⟩2.** Velocity datum: with the normal-ordered `Q^z_k` (D2(d)
register), `Q^z_k|h⟩_N=−|h+k⟩_N` exactly, and `[H,Q^z_k]=(z_k−1)J^z_k`
(G0(e) with profile `e^{ikx}`, D12(b) fixed-`k` register on the finite
ring, where the sum is finite and exact).  Taking `⟨h+k|·|h⟩`:
`−[ω(h+k)−ω(h)]=(z_k−1)⟨h+k|J^z_k|h⟩` at every ring momentum `k` (the
`e^{ikx}` profile telescopes exactly on the ring only for periodic `k`).
Both sides are trigonometric polynomials in `k` of degree `≤d(R_h)`
independent of `N`; agreeing at `N>2d(R_h)+1` points they agree
identically, and the removable `k=0` value gives
`⟨h|J^z_0|h⟩=−\lim_{k→0}[ω(h+k)−ω(h)]/(z_k−1)=iv(h)` for all
`N>N_0(R_h)`.  (`J^z_0` is diagonal on `|h⟩_N`: it conserves both
momentum and `S^z`, so the diagonal value is the full action.)
*Justification.* G0(e) (PROVED, any `ξ∈𝔤`, finite range), the displayed
matrix-element computation, uniqueness of trigonometric interpolation,
and l'Hôpital on a polynomial; at `S=1/2` this reproduces (R14)'s
`⟨k_h|Q_0^†J^-_0|k_h⟩=2iv_h` via ⟨2⟩2.

**⟨3⟩3.** Insert `n=1` in (B4) with ⟨3⟩2's diagonal value; Fourier modes
diagonalize translations, giving the packet statement.
*Justification.* (B4), ⟨3⟩2, translation covariance; ML4 (11) at
`S=1/2`.

**⟨3⟩4. QED.**

**⟨2⟩4. PROVE ((S-IDX.0) restated for the D29-B datum: the exact `ε=0`
fiber, and the kinematic separation).**  Adjoin the `k=0` row to the
readout (B3) (the running family never samples it — `supp f_ε⊂(0,ε_Ic_2)`
— so this is the fiber statement the `ε→0` law is anchored to).  Then,
for EVERY `(N,T,W,σ)`:

\[
 \mathcal R(0)=1\ \text{exactly},\qquad\text{i.e.}\qquad
 𝒜\big|_{k=0\ \text{fiber}}=0\ \text{at every finite index}.   \tag{B6}
\]

Moreover the deviation of the full datum from `1` is driven exclusively
by the current, with the kinematic factor separated: on the ring, for
each soft ring momentum `k`,

\[
 [H,Q_k]=(z_k−1)J^-_k,\qquad
 (H−ω(h)−ω(k))\,Q_k|h⟩_N=(z_k−1)\Big[J^-_k−\frac{ω(k)}{z_k−1}Q_k\Big]|h⟩_N,
                                                              \tag{B7}
\]

where `ω(k)/(z_k−1)=O(k)` with `ω(k)=O(k²)` (Goldstone leaf ⟨2⟩3.⟨3⟩1),
and at `S=1/2` the bracket is exactly the contact vector
`(J/\sqrt N)(z_h−1)|C_K⟩` of (R10)/(R11).  **Fence (G0-soft-r1,
REFUTED row; TRIANGLE §1.5):** the profile factor `(z_k−1)` alone is NOT
a soft factor and is never used as one below; (B6) comes from `[H,Q_0]=0`
plus `ω(0)=0` (symmetry + band bottom), and the `ε→0` Adler zero of
(S-IDX.1) comes from `ω(k)=O(k²)` plus contact-channel control (D30-B),
never from `(z_k−1)` by itself.

**⟨3⟩1.** (B6): `e^{-iHT}Q_0ψ_{g,σ}=Q_0e^{-iHT}ψ_{g,σ}` by
`[H,Q_0]=0`; one-magnon evolution is the exact band evolution (⟨2⟩3.⟨3⟩1),
so the interacting kernel on the `k=0` row is
`Φ̂_N(0)(0,h)e^{-iω(h)T}`; the free reference multiplies the same `t=0`
kernel by `e^{-i[ω(0)+ω(h)]T}=e^{-iω(h)T}` (using `ω(0)=0`).  Numerator
and denominator of `\mathcal R(0)` coincide term by term.
*Justification.* ⟨2⟩3.⟨3⟩1, (B3), and `[H,Q_0]=[H,S^-_{tot}]=0`
(SU(2) invariance).

**⟨3⟩2.** (B7): the first identity is G0(e) at profile `e^{ikx}` (finite
exact ring sum); the second is the first plus `H|h⟩=ω(h)|h⟩` rearranged;
at `S=1/2` the bracket evaluates to the contact vector by (R10)/(R11).
At `S≥1` the bracket is supported on `{|x−y|≤1}` (adjacent and
coincident pairs): away from contact the two free plane waves satisfy
the separated two-magnon equation (`spin-s-twomagnon.md` ⟨1⟩1), so the
defect has contact support; its exact coefficients are checker-certified
(SIB-C1), not quoted from memory.
*Justification.* G0(e); (R10)--(R11); `spin-s-twomagnon.md` ⟨1⟩1
separated equation; named computation **SIB-C1**.

**⟨3⟩3. QED.**  *(This completes (S-IDX.0): (B4)--(B5) are the index
identity — descendant part = charge datum × velocity datum, offset
bookkeeping public — and (B6)--(B7) restate it for the D29-B protocol
object with the kinematic factor separated.  Everything is unconditional
finite-volume linear algebra.)*

## ⟨1⟩3. The exact Duhamel identity, the admissible index set, and ML4-Q1 immunity

**⟨2⟩1. PROVE (exact finite-`N` Duhamel identity: the datum's deviation
is driven by the contact defect alone).**  With
`Φ^{free}(T):=\sum_{k∈Λ_N(ε)}f_ε(k)e^{-iω(k)T}Q_k\,e^{-iHT}ψ_{g,σ}` (the
unscattered comparison; its kernel is the (B3) free reference exactly at
`S=1/2`, and up to the coincident-fiber bookkeeping certified in SIB-C1
at `S≥1`):

\[
 e^{-iHT}Φ(0)−Φ^{free}(T)
 =−i\sum_{k∈Λ_N(ε)}\sum_{h}f_ε(k)\,c_{g,N}g_σ(h)
 \int_0^T\!ds\;e^{-iH(T−s)}e^{-i[ω(k)+ω(h)]s}\,𝔇(k,h),        \tag{B8}
\]

where `𝔇(k,h):=(H−ω(h)−ω(k))Q_k|h⟩_N` is the contact-supported defect of
(B7), with the `N`-INDEPENDENT, `O(k)` norm bound

\[
 ‖𝔇(k,h)‖=J\,|z_k−1|\,|z_h−1|\ \ (S=1/2,\ \text{exact}),\qquad
 ‖𝔇(k,h)‖≤C_𝔇(S)\,|k|\ \ (S≥1,\ \text{SIB-C1}).               \tag{B9}
\]

**⟨3⟩1.** Mode-wise fundamental theorem of calculus: for fixed `(k,h)`,
`\frac{d}{ds}\big[e^{-iH(T−s)}e^{-iω(k)s}Q_k e^{-iHs}\big]|h⟩
=ie^{-iH(T−s)}e^{-iω(k)s}\big([H,Q_k]−ω(k)Q_k\big)e^{-iHs}|h⟩`, and on
the one-magnon eigenvector `e^{-iHs}|h⟩=e^{-iω(h)s}|h⟩` the bracket is
`(H−ω(h)−ω(k))Q_k|h⟩=𝔇(k,h)` by (B7).  Integrating over `s∈[0,T]` and
summing the finite packet sums gives (B8).
*Justification.* (B7), ⟨1⟩2.⟨2⟩3.⟨3⟩1 (one-magnon exactness), and
finiteness of all sums; every operator is bounded on the
finite-dimensional sector.

**⟨3⟩2.** (B9) at `S=1/2`: `𝔇(k,h)=(J/\sqrt N)(z_k−1)(z_h−1)|C_{k+h}⟩`
by (R11), and `‖|C_K⟩‖=\sqrt N` (R9), so the norm is exactly
`J|z_k−1||z_h−1|≤2J|k|·2`.  At `S≥1`, `𝔇(k,h)` is supported on
`{|x−y|≤1}` (⟨1⟩2.⟨2⟩4.⟨3⟩2); each of the `O(N)` contact coefficients
carries the factor `(z_k−1)`-type profile difference and the `1/\sqrt N`
kernel normalization, giving `C_𝔇(S)|k|` with `C_𝔇` certified
numerically per SIB-C1 (no closed form is quoted from memory).
*Justification.* (R9), (R11); named computation **SIB-C1**.

**⟨3⟩3. QED.**  *(Interpretation, binding for ⟨1⟩4: the datum's
deviation from `1` is EXCLUSIVELY the windowed readout of the
time-integrated contact defect.  The band-rephasing channel — R10's
`ω(k)/(z_k−1)`-coefficient descendant part — is cancelled EXACTLY by the
free reference; no `(z_k−1)` profile factor is counted as a soft zero.)*

**⟨2⟩2. Admissible index set (definition, not hypothesis).**  Fix
`c_{set},c_{rec}∈(0,∞)`.  An index `(N,T,W,σ;ε)` is *admissible* iff
(i) `Nε(c_2−c_1)>2π` (nonempty soft sample set, ⟨1⟩1.⟨2⟩1);
(ii) `T∈[T_{\min},T_{\max}]` with
`T_{\min}:=c_{set}\,\mathrm{sep}(W,σ)/Δv`,
`Δv:=\min_{h∈K_h,\,k∈\mathrm{supp}f_ε}[v(h)−v(k)]>0` (positive by the
`ε_I` choice, D8's half-zone), `sep(W,σ)` the initial packet-separation
scale of the window data, and `T_{\max}:=c_{rec}N/v_{\max}` (the
recollision bound; the probe's `t_final·dv_max<0.92(gap+n)` is an
instance).  Subsequences in H-SIDX.3 run through admissible indices only.
*Justification.* Definition; D8; the pre-registered probe geometry.

**⟨2⟩3. PROVE (ML4-Q1 immunity, the displayed line).**

\[
 \boxed{\;\text{At fixed }N\text{ the sequence }k_s=2π/N\text{ enters no
 admissible datum: for }ε<2π/(c_2N)\text{ the sample set }Λ_N(ε)\text{ is
 EMPTY, so }ε→0\text{ at fixed }N\text{ exits the family's domain; the
 ordered limit takes }N_j→∞\text{ BEFORE }ε→0,\text{ and the rescaled
 interpolation ratio whose }\sqrt N\text{ growth ML4-Q1 proves is never
 formed.}\;}                                                   \tag{B10}
\]

Two further immunity mechanisms, stated for the record:
(i) the datum is a normalized RATIO (B3); where defined, its modulus is
controlled by row masses ((TGT1)), not by the unnormalized orthogonal
trace `𝒜_{⊥,N}` whose rescaling diverges in ML4 ⟨1⟩4.⟨2⟩3;
(ii) the pre-registered probe P3 certifies BOTH directions on the same
rings: the raw on-shell `k=2π/N` object reproduces the disease (growth
`20.5 > 2.5` gate) while the D29-B smeared datum stays bounded
(`1.39 ≤ 2.0` gate) — the probe can see the disease and the protocol
does not have it.

**⟨3⟩1.** `Λ_N(ε)=(2πℤ/N)∩(c_1ε,c_2ε)=∅` when `c_2ε<2π/N`.  The
admissibility clause (i) therefore forces `N_jε→∞` along every
subsequence evaluated at fixed `ε`, and `ε→0` last (the H-SIDX order)
keeps every evaluated index admissible.  No step of ⟨1⟩4--⟨1⟩5 ever
evaluates the family at `(N` fixed`, ε→0)`, and no constant of ⟨1⟩4 is
claimed uniform in that regime — volume-uniformity of the fixed-`N`
on-shell interpolation is REFUTED (ML4 ⟨1⟩4.⟨2⟩3) and is not used.
*Justification.* Pigeonhole on `2πℤ/N`; ML4-Q1 (named computation);
`theory/checks/soft_index_probe.py` P3 (recorded PASS,
`soft_index_probe_results.json`).

**⟨3⟩2. QED.**

## ⟨1⟩4. (S-IDX.1a): subsequential soft law on the spin-`S` anchor

**ASSUME.**  H-SIDX at the concrete anchor; an admissible subsequence
`j↦(N_j,T_j,W_j,σ_j)` (⟨1⟩3.⟨2⟩2); D30-B along it, in the sharpened form
fixed here (authoritative clause text: MERGE PROPOSALS §M2):

- **(TGT1) row-mass nondegeneracy.**  There is `c_1^{row}>0` with
  `\sum_{h∈K_h}|Φ̂^{free}_j(T_j)(k,h)|^2 ≥ c_1^{row}\,w_ε(k)` for all rows
  `k∈Λ_j(ε)`, all `j≥j_0(ε)`.
- **(TGT2) readout settling (the LR-analogue; the load-bearing clause).**
  There are `δ_j→0` and `η_j→0` such that for every fixed admissible `ε`,
  every row `k∈Λ_j(ε)`: there exist exact eigenvectors `B_j(k,h)` of
  `H_S` on `ℋ_{2,N_j}`, in the total-momentum fiber `k+h`, with
  `|E_{B_j(k,h)}−ω(k)−ω(h)|≤δ_j`, such that

  \[
   \mathcal R_j(k)=\sum_{h∈K_h}\varrho_j(k,h)\,
   r_{\mathrm{out/in}}[B_j(k,h)]+η_j(k),\qquad
   \sup_{k∈Λ_j(ε)}|η_j(k)|≤η_j,                                \tag{B11}
  \]

  where `\varrho_j(k,h)≥0`, `Σ_h\varrho_j(k,h)=1` are the row weights
  induced by the free kernel, and `r_{\mathrm{out/in}}[B]` is the D7
  chamber-coefficient ratio of `B` in the out/in labelling fixed by the
  window geometry (⟨2⟩3).  *(TGT2) asserts that the protocol readout
  settles onto the chamber data of SOME near-shell eigenvectors; it does
  NOT assert the value of any ratio — the values are computed below from
  the PROVED exact contact algebra.  This is the exact analogue of
  D27(LR1--LR2): convergence of the protocol readout plus vanishing of a
  named defect; existence of the settling is dynamics (Lane S2 / ML1
  territory; probe P1 is its empirical certificate), while the VALUE is
  symmetry.*
- **(TGT3) (optional convenience clause.)**  The full family
  `{𝒜_j(ε)}_j` converges for each admissible `ε`.  This buys only
  uniqueness of the LIMIT FUNCTION; the jet value of (ii) below is
  subsequence-free without it (mirroring D27 clause 3).
- **(TGT4) (spin-`S≥1` representability; empty at `S=1/2`.)**  The
  near-shell eigenvectors of (TGT2) are regular two-magnon scattering
  vectors in the sense of `spin-s-twomagnon.md` (T.1) (two-plane-wave
  chamber form with double-occupancy closure), and the near-shell window
  `δ_j` excludes the spin-`S` bound band(s) on the relevant fibers.  At
  `S=1/2` this clause is PROVED (ML2 + ⟨2⟩1 below) and is not assumed.

**⟨2⟩1. LEMMA SIB-L1 (near-shell root localization; `S=1/2`
unconditional).**  Fix `k∈(0,ε_Ic_2]`, `h∈I`, `K=k+h`, and let `B` be an
exact eigenvector on the fiber `K` with `|E_B−ω(k)−ω(h)|≤δ`.  There is
`δ_I>0` (depending on `I`, `ε_I` only) such that for `δ≤δ_I`:
(i) `B` is a regular D7-representable scattering vector (not the bound
vector, not the `K=π` singular vector, not a descendant);
(ii) its D7 roots `(κ_1,κ_2)` (ordered `κ_1` soft) satisfy
`|κ_1−k|+|κ_2−h|≤C_Iδ`;
(iii) its chamber ratio is the exact contact-equation value
`S_{12}(κ_1,κ_2)` of (R16)/(T.2).

**⟨3⟩1.** (i): on the fiber, the bound-band energy is separated from the
scattering shell by at least `J\sin^2(a/2)` for `h∈I`, `|k|≤ε_I`
(computed in ML4 ⟨1⟩4.⟨2⟩1.⟨3⟩4); the singular completion vector
requires `K=π`, excluded by the `ε_I` choice; `SU(2)` descendants of
lower sectors have energies `ω` of one-magnon type, separated from the
two-magnon shell on `I` — wait: the descendant `Q_0|h'⟩` has energy
`ω(h')`, and `ω(h')=ω(k)+ω(h)` CAN occur for some ring `h'`.  Repair: the
descendant lies in the fiber `K=h'` and has `S^z`-highest-weight
deficit — it is orthogonal to `\ker S^+`… it is NOT in `\ker S^+`.
Restrict the statement: (i) holds for the eigenvectors carrying the
readout, which lie in the two-magnon HIGHEST-WEIGHT part plus descendant
part; the descendant component of the readout is treated separately in
⟨2⟩2.⟨3⟩3 below.  For `B∈\ker S^+` on the fiber, ML2's enumeration
(real-pair, complex-pair/bound, singular) is exhaustive, and the bound
and singular classes are excluded as displayed.
*Justification.* ML2 (PROVED; enumeration and fiber structure), ML4
⟨1⟩4.⟨2⟩1.⟨3⟩4 (bound-gap and `K=π` exclusion), D8/`ε_I`.

**⟨3⟩2.** (ii): on the fiber `K`, the scattering energy in ML2 variables
is `E(K,q)=J[2−2\cos(K/2)\cos q]` with `∂_qE` bounded below by
`\min_I v>0` near the shell point (ML4 ⟨1⟩4.⟨2⟩1.⟨3⟩2--⟨3⟩3, the unique
`C¹` branch).  The inverse function theorem converts the energy window
`δ` into a root window `C_Iδ`.
*Justification.* ML2 (18); ML4 ⟨1⟩4.⟨2⟩1; compactness of `I`.

**⟨3⟩3.** (iii): every D7-representable eigenvector's chamber
coefficients satisfy the contact equation exactly — (R16) at `S=1/2` is
the statement that the contact residual vanishes, and its unique solution
fixes `A_{12}/A_{21}=S_{12}(κ_1,κ_2)`.
*Justification.* soft-current-recon ⟨1⟩4.⟨2⟩2 (R16); D7.

**⟨3⟩4. QED.**

**⟨2⟩2. THEOREM ((S-IDX.1a)).**  Under the standing ASSUME, let
`𝖲^*` be ANY subsequential limit point of `{𝒜_j(·)}`: a function on a
set `E⊂(0,ε_0]` of admissible soft scales with `0∈\bar E`, with
`𝒜_{j'}(ε)→𝖲^*(ε)` for each `ε∈E` along a further subsequence `j'`.
Then:

\[
 \text{(i)}\ \ |𝖲^*(ε)|≤C_Iε\ \text{on }E,\ \text{hence }𝖲^*(0):=\lim_{ε→0}𝖲^*(ε)=0
 \ \text{(Adler zero)};                                        \tag{B12}
\]
\[
 \text{(ii)}\ \ \arg\big(1+𝖲^*(ε)\big)=\mathrm{sgn}(v_h−v_s)\,\frac{|q|}{ρ}\,
 \bar k_w(ε)+O(ε^2),\qquad ρ=S,\ |q|=1,                        \tag{B13}
\]

with `\bar k_w(ε)∈[c_1ε,c_2ε]` the limiting weighted mean row momentum;
hence the jet `\lim_{ε→0}\arg(1+𝖲^*(ε))/\bar k_w(ε)` exists and equals
`\mathrm{sgn}(v_h−v_s)/S` — subsequence-INDEPENDENT (every limit point
carries the same jet), which is (iii) without the convenience clause.

**⟨3⟩1.**  Fix `ε∈E`.  For `j` large, (TGT2) gives (B11); by SIB-L1
(with (TGT4) at `S≥1`) each `B_j(k,h)` is a regular scattering vector
with roots `(κ_1,κ_2)`, `|κ_1−k|+|κ_2−h|≤C_Iδ_j`, and out/in ratio
`S_{phys}(κ_1,κ_2)` in the labelling of ⟨2⟩3.
*Justification.* (TGT2), SIB-L1, (TGT4), ⟨2⟩3.

**⟨3⟩2.**  The exact expansion (T.3) (S2-2body-S, PROVED; at `S=1/2`
equivalently (R17), remainder uniform on compact hards) gives, with the
linear coefficient INDEPENDENT of the hard leg,
`r_{\mathrm{out/in}}[B_j(k,h)]=1+i\,\mathrm{sgn}(v_h−v_s)\,κ_1/S+O(κ_1^2)`,
uniformly for `h∈I`.  Averaging over the normalized row weights
`\varrho_j` and then the row aggregate `w_ε` of (B3):

`𝒜_j(ε)=i\,\mathrm{sgn}(v_h−v_s)\,S^{-1}\bar k_{w,j}(ε)
 +O(ε^2)+O(δ_j)+O(η_j)`,

where `\bar k_{w,j}(ε):=Σ_kw_ε(k)\,κ_1(k)/Σ_kw_ε(k)∈[c_1ε,c_2ε]+O(δ_j)`.
The hard-column average is harmless at linear order precisely because
the linear coefficient carries no `h`-dependence — this is the
finite-volume avatar of (R17)'s "all hard dependence cancels", and the
reason NO `σ→0` limit is needed for the slope.
*Justification.* S2-2body-S (T.2)--(T.3); (R17); (B3); (B11);
triangle inequality.  Named computation **SIB-C2** (checker: the
displayed aggregate at ED-accessible sizes).

**⟨3⟩3.**  Passing `j'→∞` at fixed `ε` kills `O(δ_j)+O(η_j)` and gives
`𝖲^*(ε)=i\,\mathrm{sgn}(v_h−v_s)S^{-1}\bar k_w(ε)+O(ε^2)`, whence (B12)
and (B13); `\arg(1+z)=\Im z+O(|z|^2)`.  The jet value depends only on
the displayed constants, not on the subsequence: (iii).  *(Descendant
bookkeeping promised in ⟨2⟩1.⟨3⟩1: `S^+Φ(0)=2Σ_kf_ε(k)Q^z_kψ_{g,σ}≠0`,
so (B1) has a descendant component — the `Q_0`-descendants
`Q_0|m⟩_N`, whose kernels are the `(0,m)` pair modes.  The readout rows
`k∈Λ_j(ε)∌0` and columns `h∈K_h∌0` pair with them only through the
half-plane Dirichlet tails `F_N` of (R4), of relative size
`O_ε(1/N_j)` (constants `∼1/\mathrm{dist}(\{0\},Λ_j(ε)∪K_h)`); the
descendant admixture therefore vanishes along the subsequence and never
carries readout weight in the limit.)*
*Justification.* ⟨3⟩2; `[S^+,Q_k]=2Q^z_k` (su(2), as in ⟨1⟩2.⟨2⟩1);
(R4) with the geometric-sum bound (16) of ML4 ⟨1⟩4.⟨2⟩2.⟨3⟩3; named
computation **SIB-C0**.

**⟨3⟩4. QED.**

**⟨2⟩3. Channel labelling (the oracle-r2 residue-4 subtlety, carried).**
The window data `W` fix the initial geometry: the hard packet is prepared
BEHIND the soft support in the direction of relative motion
(`v(h)>v(k)` on the admissible set, D8's half-zone), as in the probe
(`x_{hard}=x_{soft}−gap`).  With D7's convention (for `v(k_2)>v(k_1)`
and the `k_2` packet initially on the left, `A_{21}` is incoming,
`A_{12}` outgoing), the readout ratio `r_{\mathrm{out/in}}` is
`S_{12}=S_{phys}` on this geometry, and the mirrored geometry reads
`S_{21}=S_{phys}^{-1}` with `\mathrm{sgn}(v_h−v_s)=−1` — the sign in
(B13) is the D7/D8 channel sign, spelled out, never the bare `χ`
(notation.md overload 2).  A datum whose window geometry is UNMATCHED to
the velocity ordering reads the unphysical ratio and (B13) then holds
with the opposite sign; D29-B therefore includes the matching clause in
its window data.
*Justification.* D7, D8; notation.md rows `S_phys`, `sgn(v_h−v_s)`;
oracle-bethe-r2 residue 4 (labelling, not value).

## ⟨1⟩5. (S-IDX.1b): abstract descendant-projected law

*(Architecture: this is ML5-B transplanted to the charge-created protocol
over tail density `ρ`, with two of the five D24(d) clauses DISCHARGED by
the protocol — that is the structural gain over ML5-B, where all five are
assumed — and the remaining three carried as the abstract D30-B clause
(TGT2′).  No contact equation is available here, so the conclusion is the
law for the DESCENDANT-PROJECTED datum, stated prominently as such: the
orthogonal contact vector is NONZERO ((R15) and ML4 ⟨1⟩3 closing remark)
and is controlled by hypothesis on the limit family, never assumed away.)*

**ASSUME.**  The abstract H-SIDX.1 register of ⟨1⟩2 (`ρ` free, `|q|=1`
soft leg from `S^-`); the finite-volume identities (B4)--(B9); and:

- **(H-band)** the contact-defect bound `‖𝔇_N(k,h)‖≤C_I|k|` uniformly in
  `N` on `h∈I`, `|k|≤ε_I` (PROVED at the anchor, (B9); a named
  finite-volume locality hypothesis abstractly — checkable at any fixed
  model by SIB-C1, strictly weaker than any scattering input);
- **(TGT1)** row-mass nondegeneracy as in ⟨1⟩4;
- **(TGT2′) abstract reduction clauses** for the limit family, verbatim
  the three UNDISCHARGED clauses of D24(d) transplanted to the protocol:
  (1′) exhaustive normed LSZ decomposition of the limit datum into
  descendant, orthogonal-current, and transit terms (D24(d)1);
  (3′) kinematic flux normalization: the external soft-leg flux factor
  `L(k,h)` of the limit datum is process independent, uniformly `C¹`,
  with `L(0,h)=−i\,\mathrm{sgn}(v_h−v_s)/v_h` (D24(d)3);
  (4′) orthogonal-channel regularity: the limit orthogonal family
  satisfies ML4-A's hypotheses (4) in the trace register (D24(d)4 —
  fixed-volume ML4 does NOT supply this volume-uniform clause; ML4-Q1 is
  the standing counterexample to its unsmeared form, which is why it is
  a hypothesis on the SMEARED limit family only);
  and additionally **(tr′)** the transit bound: the time-integrated
  windowed pairing of the evolved defect in (B8) is bounded by
  `C_{tr}\sup_k‖𝔇_N(k,h)‖` per unit row mass along the subsequence.

**⟨2⟩1. PROVE (the protocol discharges D24(d) clauses 2 and 5).**
(2) *Ward covariance:* the descendant current residue of the
charge-created datum factorizes as `2i\,v(h)M_1(h)` — this is (B4)--(B5),
PROVED in ⟨1⟩2 for every `N`, every sector, `ρ` free.
(5) *No direct soft contact:* the protocol has NO source jet to deform:
the soft leg is `Q[f_ε]` itself, and by ⟨1⟩1.⟨2⟩1(iii) the map defining
the datum contains no source parameter; the D24(e) deformation acts on
sources, and the protocol quantifies over NONE.  Consequently the contact
first jet of the protocol datum is not an independent datum: it is the
transit term of (B8), bounded by (tr′)+(H-band) as `O(k²)`-per-unit-jet
— wait: (H-band) gives only `O(k)`; the `O(k²)` needed for clause 5 is
exactly what (tr′) must supply through the `(z_k−1)`-prefactor already
separated in (B7): the defect `𝔇` CONTAINS one explicit factor
`(z_k−1)`-type smallness ((B9)), and (tr′) bounds its time integral
without further growth; the product is `O(k)·O(k)=O(k²)` relative to the
unit-normalized hard datum.  *(Displayed so the critic sees no circular
use: (H-band) is one power of `k`; (tr′) prevents the time integral from
eating it; the second power is the kinematic `ik_s` of (3′).)*
*Justification.* ⟨1⟩2 (B4)--(B5); ⟨1⟩1.⟨2⟩1(iii); (B8)--(B9); (tr′).

**⟨2⟩2. PROVE (descendant-channel jet: the bookkeeping that turns the
su(2) `2` into `|q|/ρ`).**  Under the ASSUME block, the
descendant-channel component of any limit point of the
descendant-projected datum family has first-order jet

\[
 \boxed{\;\partial_{k_s}\arg\big(1+𝖲^*_{desc}\big)\Big|_0
 =\mathrm{sgn}(v_h−v_s)\,\frac{|q|}{ρ}\;}                       \tag{B14}
\]

via the displayed cancellation (each factor cited, none from memory):

- Ward residue (numerator datum): `2i\,v(h)` per unit hard amplitude —
  (B4)--(B5); the `2` is `[S^+,S^-]=2S^z`;
- soft-leg normalization: the charge-created leg has squared norm
  `‖Q_{k_s}|Ω⟩‖^2=2ρN` (one displayed line:
  `⟨Ω|S^+_{-k}S^-_{k}|Ω⟩=Σ_x⟨Ω|2S^z_x|Ω⟩=2ρN`), so one unit-normalized
  soft magnon carries `(2ρN)^{-1/2}` of the charge-created datum, and the
  multiplier normalization divides by the per-volume leg density `2ρ`;
- external flux/pole factor: `L(k_s,h)` with
  `L(0,h)=−i\,\mathrm{sgn}(v_h−v_s)/v_h`, uniformly `C¹` — clause (3′);
  the `1/v_h` is the on-shell pole residue `[ω(h+k_s)−ω(h)]^{-1}·k_s`
  with the band `C²` on `I`;
- kinematic factor: `(e^{ik_s}−1)=ik_s+O(k_s^2)`, separated since (B7)
  and never counted as a zero (G0-soft-r1 fence).

Net, exactly as in ML5-B (6) but with the leg-density weight made
explicit:

`(e^{ik_s}−1)·L(k_s,h)·[2i\,v_h]·\frac{1}{2ρ}
 =ik_s·\big(−i\,\tfrac{\mathrm{sgn}}{v_h}\big)·2iv_h·\tfrac{1}{2ρ}
 +O(k_s^2)
 =i\,\mathrm{sgn}(v_h−v_s)\,\tfrac{k_s}{ρ}+O(k_s^2)`,

so the multiplier is `1+i\,\mathrm{sgn}\,k_s/ρ+O(k_s^2)` and the phase
slope is `\mathrm{sgn}(v_h−v_s)/ρ`, i.e. `|q|/ρ` at `|q|=1`; the hard
velocity cancels EXACTLY between residue and flux — the abstract avatar
of (R17)'s hard-independence.  At `ρ=1/2` this is `2` (ML5-B (6)
verbatim); at `ρ=S` it is `1/S`, matching ⟨1⟩4 (consistency anchor
⟨1⟩7(b)).

**⟨3⟩1.**  The leg-norm line is the display above (uses only
`[S^+_x,S^-_y]=2S^z_xδ_{xy}` and the vacuum density); the residue line is
(B5); the pole and kinematic lines are Taylor on the `C²` band and
`e^{ik}−1`; (3′) supplies the flux factor and its `C¹` uniformity; the
product of the displayed factors is the jet, by the same linearization
as ML5-B ⟨2⟩1.⟨3⟩2 (whose (6) is exactly this computation at `ρ=1/2`).
*Justification.* (B4)--(B5); D24(d)3 = (3′); ML5-B ⟨2⟩1 (PROVED,
conditional); Taylor's theorem; named computation **SIB-C3** (the
`ρ`-scaling of the displayed product, checkable at `S∈{1/2,1,3/2}`).

**⟨3⟩2. QED.**

**⟨2⟩3. PROVE (orthogonal channel and the full projected law).**  Under
(4′), ML4-A applies verbatim to the limit family: `Γ(0)=U` (energy-shell
channel matching) plus `C¹` trace regularity give
`‖b(k)Γ(k)^†R‖≤C_bC_Γ‖J‖k²` and `O(ε²)` in the rescaled soft-packet
norm — the orthogonal channel contributes NOTHING to the jet.  With
⟨2⟩1 (clauses 2, 5 discharged), ⟨2⟩2 (descendant jet), and (1′)
(exhaustiveness), every limit point of the descendant-projected abstract
datum obeys (i) the Adler zero (from (H-band)+(tr′): `|𝒜|≤Cε`) and
(ii) the jet (B14).  What is NOT claimed: the full unprojected abstract
datum — its orthogonal part is controlled only by hypothesis (4′), and
if (4′) is dropped the honest statement is (B14) for the
descendant-projected datum ONLY.  This sentence is the prominent
fallback demanded by the target brief.
*Justification.* ML4-A (PROVED); (1′), (4′); ⟨2⟩1--⟨2⟩2.

**⟨2⟩4. QED.**

## ⟨1⟩6. (S-IDX.2): the ML5-A source bridge

**COROLLARY (cheap; cites ML5-A, reproves nothing).**

**ASSUME.**  H-SIDX; a D24(a) source `O`; the per-index source amplitudes
`M_{1,j}^O∈L²(I)`, `M_{2,j}^O(k,·)` defined as the settled window
readouts of the `O`-created data at index `j` (same window discipline as
D29-B, soft leg now `O`-created); and

- **(SRC1)** D24(b)--(c) regularity per index with constants uniform
  along the subsequence: `M_{2,j}^O(k,·)` is `C²` in `k` as an
  `L²(I)`-valued map with `\sup_jK_{O,j}(ε_0)<∞`, and the limit
  amplitudes `M_1^O:=\lim M_{1,j}^O`, `M_2^O(k,·):=\lim M_{2,j}^O(k,·)`
  exist in `L²(I)` along the subsequence (this is where the per-`(N,W,σ)`
  norms enter: the D24 norms are read PER INDEX and carried through the
  limit by the stated uniformity — the target brief's porting question,
  answered);
- **(SRC2)** the two ML5-A zero conditions on the LIMIT:
  `M_2^O(0,·)=0` and `𝔠_h(O)=0` in `L²(I)`.

**PROVE.**  The limit amplitudes obey
`M_2^O(k,h)=2i\,\mathrm{sgn}(v_h−v_s)\,k\,M_1^O(h)+O_{L²(I)}(k²)`; hence
the `O`-sourced datum family inherits (S-IDX.1a)(i)--(ii) with `M_1^O` in
place of the charge-created hard amplitude — Adler zero and jet
`\mathrm{sgn}(v_h−v_s)\,|q|/ρ` at `ρ=1/2` (ML5-A's register is the D6
anchor; the spin-`S` transplant would need D24 re-normed at density `ρ`
and is NOT claimed).

**⟨2⟩1.**  Uniform `C²` bounds pass Taylor remainders to the limit:
`K_O(ε)≤\liminf_jK_{O,j}(ε)<∞`, so the limit `M_2^O` is `C¹` at `0` with
second-order control; ML5-A (necessity-and-sufficiency, PROVED) applied
to the limit amplitudes under (SRC2) gives the factorisation with
remainder `K_O(ε)|k|²`.
*Justification.* ML5-A (4)--(4b); Banach-space Taylor with integral
remainder; (SRC1)--(SRC2).

**⟨2⟩2.**  Nothing here implies unrestricted universality: for `O_η`
(D24(e)), `𝔠_h(ηD)=2iη(1−e^{-3ih})≠0` violates (SRC2) on any packet
where `1−e^{-3ih}≠0`, and the corollary is silent — O_η survives every
formulation, exactly as the frozen conjecture requires; the probe's
P2(a) reproduces the obstruction numerically (jet within 8%).
*Justification.* ML5 (REFUTED row), D24(e), `ml5-universality.md` ⟨1⟩4;
probe P2 record.

**⟨2⟩3. QED.**

## ⟨1⟩7. (S-IDX.3): the three consistency anchors

*(Any mismatch here is a FATAL bug in ⟨1⟩4--⟨1⟩5; each anchor is an
exact-match obligation against a PROVED row.)*

**⟨2⟩1. PROVE (anchor (a): reduction to S2-2body (R17)--(R18) on
D6--D8).**  At `S=1/2` on D8's half-zone, the settled row values of
⟨1⟩4.⟨2⟩2.⟨3⟩2 are `S_{12}(κ_1,κ_2)` with
`S_{12}=1+2ik_s+[i\cot(k_h/2)−2]k_s²+O(k_s³)` and
`\arg S_{12}=2k_s+\cot(k_h/2)k_s²+O(k_s³)` — (R17)--(R18) verbatim, with
the compact-hard uniform remainder.  The linear term matches (B13) at
`ρ=1/2`, `\mathrm{sgn}=+1`: jet `2`.  No second-order claim is made by
S-INDEX-B (the quadratic coefficient is hard-dependent and is averaged by
the window; only the hard-independent linear term survives aggregation
untouched).  OR1 certifies (R17)--(R18) = O7/O8 term by term.
*Justification.* (R17)--(R18); OR1 (PROVED); ⟨1⟩4.⟨2⟩2.

**⟨2⟩2. PROVE (anchor (b): spin-`S` slope `1/S`).**  (B13) at `ρ=S`,
`|q|=1` gives `\mathrm{sgn}(v_h−v_s)/S`, which is (T.3)--(T.4) of
S2-2body-S (PROVED per spin-s-r1.md); the abstract bookkeeping (B14)
gives the same value through `2iv_h/(2ρ)/(v_h)` — the two routes agree
BECAUSE the leg-norm display `‖Q_{k_s}|Ω⟩‖²=2ρN` and the su(2) residue
`2iv_h` are spin-independent facts while the density is `ρ=S`.  The
probe's out-of-sample `S=1` measurement (`1.0217`, 2.2%) is the
empirical certificate.
*Justification.* S2-2body-S (T.3)--(T.4); (B13)--(B14); probe P1
record.

**⟨2⟩3. PROVE (anchor (c): ML1-as-hypothesis recovers the S2
EXPLORATION box; conditional, with the missing step NAMED).**  Assume,
as HYPOTHESES (not proved): ML1 (two-magnon wave operators `W_±` on
packets away from equal velocities and endpoints, D7 normalization,
bound state split off) and the limit-order control ML6 for the triple
`(N→∞, T→∞, \text{window})` at fixed `ε`.  Then:
(i) the interacting-vs-free kernel comparison of D29-B converges: for
`t→∞` on the infinite chain,
`⟨e_{kh},e^{-iHt}Φ(0)⟩\,\overline{⟨e_{kh},Φ^{free}(t)⟩}` settles to the
on-shell S-matrix multiplier times the free row mass — this is the
standard scattering identification `W_+^*W_-=S`; so (TGT1)--(TGT2) HOLD
along every admissible subsequence, with the near-shell eigen-data
replaced by on-shell S-matrix values;
(ii) limit points exist (nonvacuity discharged), and (S-IDX.1a) yields
`M_2=𝖲(k_s)M_1+R_{S2}` with `𝖲(k_s)=2ik_s` and
`‖R_{S2}(k_s,·)‖_{L²(I)}≤C_I|k_s|²‖M_1‖_{L²(I)}` — exactly the boxed
EXPLORATION Theorem S2 of `soft-current-recon.md` ⟨1⟩6, now as the
value-computation COROLLARY of the constraint theorem, mirroring how
M-quant-G became the value-computation corollary of M-INDEX-spec
(TRIANGLE §3.6).
**Missing step, named:** the interchange of the settled-`t` limit with
the ring eigen-sum along `(N_j,T_j)` — i.e. that the FINITE-volume
settling defect `η_j` of (TGT2) actually tends to `0` given ML1 on the
infinite chain — is a finite-size/infinite-volume comparison of exactly
ML6's type; it is used here as part of the hypothesis package and is NOT
derived.  At SKETCH level anchor (c) is therefore: ML1+ML6 ⟹ (TGT1),
(TGT2), nonvacuity, and the S2 box.
*Justification.* ML1, ML6 (CONJECTURE rows, assumed here as
hypotheses); soft-current-recon ⟨1⟩6 (boxed EXPLORATION); ⟨1⟩4.⟨2⟩2;
TRIANGLE §3.6 (the restructuring precedent).

**⟨2⟩4. QED.**

## ⟨1⟩8. Landmine audit (pre-QED self-attack; binding register)

1. **Vacuous truth.**  Answered twice: ⟨1⟩1.⟨2⟩3 proves the FINITE-index
   family nonempty at every soft scale (with recorded probe instances),
   and nonvacuity of LIMIT points is explicitly scoped as conditional —
   discharged by ML1-as-hypothesis in ⟨1⟩7.⟨2⟩3, intended to be
   discharged unconditionally by Lane S2's (A2M.3).  The theorem is a
   constraint on whatever limit points exist; it is stated nowhere that
   any exist unconditionally.
2. **Limit-order smuggling.**  The single displayed immunity line is
   (B10).  Every `ε`-operation in ⟨1⟩4--⟨1⟩5 happens AFTER the
   `j`-subsequence is fixed; no constant is claimed uniform in the
   fixed-`N` on-shell regime; the REFUTED volume-uniform interpolation
   (ML4 ⟨1⟩4.⟨2⟩3) is cited as refuted and used nowhere.  The probe's P3
   certifies both the visibility of the disease and the boundedness of
   the smeared datum.
3. **Kinematic-factor conflation (G0-soft-r1 fence).**  `(e^{ik_s}−1)`
   appears exactly twice: as the PROFILE factor in (B7)/(B8), where it is
   cancelled or carried explicitly, and as the LSZ kinematic line of
   (B14), where it contributes one power of `k_s` only in combination
   with the Ward residue and the pole.  The Adler zero (B6)/(B12) is
   derived from `[H,Q_0]=0`, `ω(0)=0`, `ω(k)=O(k²)`, and contact-channel
   control — never from the bare difference factor.  TRIANGLE §1.5's
   negative row is the fence; it is respected.
4. **Descendant vs orthogonal contact.**  (R15)'s complementary vector is
   NONZERO and is nowhere assumed away: at the anchor the contact channel
   is handled by the exact contact algebra ((R16)/(T.2)) through (TGT2);
   abstractly the orthogonal channel is controlled ONLY by the (4′)
   ML4-A clause, and dropping (4′) degrades the claim to the
   descendant-projected law — stated prominently in ⟨1⟩5.⟨2⟩3.
5. **O_η (D24(e)).**  The protocol quantifies over NO sources
   (⟨1⟩1.⟨2⟩1(iii)); sources re-enter only through ⟨1⟩6, where both
   D24(c) zero conditions appear as hypotheses (SRC2).  Nothing proved
   here implies unrestricted universality; O_η survives every statement
   of this shard, and P2 certifies the dodge quantitatively.
6. **`ρ` free.**  No step assumes `ρ∈½ℤ`.  `ρ` enters only through the
   sector weight `M=ρN−n` ((B4), bookkeeping displayed) and the leg norm
   `2ρN` ((B14)).  D26(INT) is carried in H-SIDX.1 as the interface
   hypothesis of the campaign template (the Corner-B/C junction); **no
   step of this shard uses it** — recorded here and in HONEST STATUS so
   the critic need not hunt for a hidden use.
7. **`δ` vs `𝖲` normalization; sign labelling.**  The datum's relation
   to D25's multiplier: `𝒜=𝔯−1` plays the role of `𝖲(k_s;·)` with
   `M_1`-normalization absorbed by the ratio; the phase read is
   `\arg\mathfrak r=\arg S_{phys}=δ_{phys}` (D7 branch fixed at
   `k_s=0`).  The channel sign is carried as the spelled-out
   `\mathrm{sgn}(v_h−v_s)` (notation.md overload 2), and the
   window-geometry matching clause (⟨1⟩4.⟨2⟩3) is part of D29-B — the
   oracle-r2 residue-4 labelling subtlety is carried, not dropped.
8. **Self-attack on (TGT2) (anticipated MAJOR).**  (TGT2) is
   dynamics-shaped: it assumes the readout settles onto near-shell
   chamber data.  Defense: (i) it fixes NO value — values come from the
   PROVED contact algebra, which is the constraint content; (ii) it is
   the exact structural analogue of D27(LR1--LR2), which the memory
   campaign's L6 loop accepted as the honest protocol hypothesis;
   (iii) it is empirically certified at `N≤32` by P1 (both `S=1/2`
   in-sample and `S=1` out-of-sample) and is the precise interface Lane
   S2's (A2M.3) is contracted to discharge on `\mathrm{ran}\,W_±`;
   (iv) the target brief's weaker template (TGT) ("uniform boundedness +
   equicontinuity") is NOT sufficient to pin the VALUE of the jet — with
   only equicontinuity the limit family is constrained by no exact
   identity at `ε>0`, and the jet could be anything; the value-pinning
   clause must reach the on-shell data somewhere.  Recorded as a
   deliberate strengthening WITH this justification, not a silent one.

## CHECKER SPEC

Proposed file: `theory/checks/soft_index_b_check.py` (orchestrator lane
implements; this shard does not touch `theory/checks/`).  Discipline:
no bare asserts, `SystemExit(1)` failures, green exit 0, every red mode
exit 1, runs under `python3 -O`.  Sector machinery may be imported from
the frozen `soft_index_probe.py`.

- **SIB-C0 (pair-mode Gram control; supports ⟨1⟩1.⟨2⟩2, ⟨1⟩4.⟨2⟩2.⟨3⟩3).**
  Model: D6 ring, `N∈{12,18,24}`, `S∈{1/2,1}`.  Compute the Gram matrix
  of the symmetrized pair modes `e_{kh}` for `k∈{2π/N,4π/N}`,
  `h∈I`-samples, and the descendant modes `e_{0,m}`: off-diagonal
  entries must be `≤C/N` with fitted decay exponent `≥0.9` in `N`.
  RED: replace the half-plane sum `F_N` bound by the claim that distinct
  modes are exactly orthogonal (tolerance `1e-12`) — must FAIL.
- **SIB-C1 (contact defect: support and norm; LOAD-BEARING for
  (B7)--(B9) and (H-band)).**  Model: spin-`S` ring, `S∈{1/2,1,3/2}`,
  `N∈{14,18}`.  Assemble `𝔇(k,h)=(H_S−ω_S(h)−ω_S(k))Q_k|h⟩_N` for ring
  momenta `k∈{2π/N,4π/N}`, `h` mid-zone.  Check (i) support: components
  on configurations with `\min`-separation `>1` are `≤1e-12`;
  (ii) scaling: `‖𝔇(k,h)‖/|k|` bounded by a fitted `C_𝔇(S)` constant
  across `N` (volume-independence) with variation `≤5%`; (iii) at
  `S=1/2` the exact value `J|z_k−1||z_h−1|` to `1e-12`.  RED
  (`--red-defect`): drop the double-occupancy channel from `H_S` at
  `S=1` — support/value checks must FAIL.
- **SIB-C2 (settled readout vs exact chamber ratio; certifies the ⟨1⟩4
  aggregation step (B11)→(B13) at ED sizes).**  Model: `S∈{1/2,1}`,
  `N=28`--`32` (probe geometry).  Compute the D29-B row datum
  `\mathcal R(k)` at the probe's settling time and compare
  `\arg\mathcal R(k)` row-wise against `δ_{phys}(k,k_h)` from the exact
  ratio (T.2): weighted max deviation `≤0.05` on the fitted rows.  RED:
  the probe's frozen `--red` (predicted slope `1/(S+1)`) — must FAIL.
- **SIB-C3 (ρ-bookkeeping of (B14); symbolic).**  Symbolically (or in
  exact rationals) verify, for `ρ∈{1/2,1,3/2}`: leg norm
  `‖Q_{k}|Ω⟩‖²=2ρN` on `N∈{8,12}` rings; residue `⟨h|Q_0^†J^-_0|h⟩=2iv(h)`
  with `v=v_S`; and that the displayed product
  `[2iv_h]·[1/(2ρ)]·[1/(v_hk)]·[ik]` equals `−1/ρ`-phase-slope pattern,
  i.e. jet `1/ρ`.  RED (`--red-legnorm`): mutate the leg norm to `ρN` —
  the reconstructed jet becomes `2/ρ` and the comparison with the
  measured P1 slope must FAIL.

The load-bearing certificate is SIB-C1: it is the only place the spin-`S`
generalization of the (R10)/(R11) contact structure enters, and both
⟨1⟩3 (B9) and ⟨1⟩5 (H-band) lean on it.

## MERGE PROPOSALS

*(Exact replacement text; the orchestrator reconciles with the S1-A
lane's proposals.  Nothing outside this section edits a shared file.)*

### §M1 — definitions.md, append as D29 (lane-B wording)

> ## D29 (windowed charge-created soft protocol datum)
>
> On the `N`-site spin-`S` ring (D6 register at `S=1/2`;
> `theory/spin-s-twomagnon.md` Statement otherwise), fix `I=[a,b]⋐(0,π)`
> and `ε_I` as in `ml4-ward-reduction.md` ⟨1⟩1.  Data: a hard packet
> `ψ_{g,σ}` sampled from `g∈C_c^∞(I)` in the `‖·‖_{I,N}` norm (ML4 (1)),
> width register `σ`; a soft profile `f∈C_c^∞((c_1,c_2))`, `0<c_1<c_2<1`
> (or its reflection), rescaled `f_ε(k)=ε^{-1/2}f(k/ε)` and sampled on
> ring momenta only, `Λ_N(ε):=(2πℤ/N)∩\mathrm{supp}f_ε`; the
> charge-created state `Φ(0):=Q[f_ε]ψ_{g,σ}` (D10(c); the smeared broken
> charge itself — no other source is admitted); a settling time `T` and
> window data `W=(K_h,\cdot)` with the geometry-matching clause: the
> initial packet ordering matches the velocity ordering so that D7's
> outgoing coefficient is read as "out".  With
> `Φ̂_N(T)` the momentum kernel of `e^{-iHT}Φ(0)` and
> `Φ̂^{free}_N(T):=Φ̂_N(0)e^{-i[ω(k)+ω(h)]T}` (band data only), the
> *row readout* and *datum* are
> `\mathcal R(k):=\frac{Σ_{h∈K_h}Φ̂_N(T)(k,h)\overline{Φ̂^{free}_N(T)(k,h)}}{Σ_{h∈K_h}|Φ̂^{free}_N(T)(k,h)|²}`,
> `\mathfrak r_{N,T,W,σ}(ε):=Σ_kw_ε(k)\mathcal R(k)/Σ_kw_ε(k)`,
> `𝒜_{N,T,W,σ}(ε):=\mathfrak r_{N,T,W,σ}(ε)−1`,
> with free-kernel row weights `w_ε(k)`.  An index is *admissible* iff
> `Nε(c_2−c_1)>2π` and `T` lies in the settling/recollision sandwich
> `[c_{set}\,\mathrm{sep}(W,σ)/Δv,\;c_{rec}N/v_{max}]`
> (`theory/soft-index-b.md` ⟨1⟩3.⟨2⟩2).  Every object is a finite exact
> linear-algebra quantity; no wave operators, no interpolation off the
> ring momenta (for `ε<2π/(c_2N)` the sample set is EMPTY — the fixed-`N`
> on-shell soft sequence of ML4-Q1 is outside the datum's domain by
> construction).  Limit statements use admissible subsequences
> `(N_j,T_j,W_j,σ_j)` at fixed `ε`, with `ε→0` strictly last.

### §M2 — definitions.md, append as D30 (lane-B wording)

> ## D30 (soft-datum tightness/regularity, (TGT))
>
> Along a stated admissible D29 subsequence:
> **(a) row-mass nondegeneracy** — the free row masses dominate the
> declared row weights: `Σ_{h∈K_h}|Φ̂^{free}_j(T_j)(k,h)|²≥c_1^{row}w_ε(k)`;
> **(b) readout settling (the LR-analogue)** — there are `δ_j→0`,
> `η_j→0` and, per row pair `(k,h)`, exact eigenvectors `B_j(k,h)` in the
> total-momentum fiber `k+h` with `|E_{B_j}−ω(k)−ω(h)|≤δ_j`, such that
> `\mathcal R_j(k)=Σ_h\varrho_j(k,h)\,r_{out/in}[B_j(k,h)]+η_j(k)`,
> `\sup_k|η_j(k)|≤η_j`, where `r_{out/in}[B]` is `B`'s D7
> chamber-coefficient out/in ratio in the D29 window labelling.  Clause
> (b) fixes the value of NO ratio; it asserts settling onto near-shell
> spectral data only.
> **(c) convenience clause (optional)** — `{𝒜_j(ε)}_j` converges for each
> admissible `ε`; buys uniqueness of the limit function only (the jet
> value is subsequence-free without it).
> **(d) spin-`S≥1` representability** — the `B_j(k,h)` of (b) are regular
> two-magnon scattering vectors in the sense of `spin-s-twomagnon.md`
> (T.1), and `δ_j` excludes the spin-`S` bound band(s); at `S=1/2` this
> clause is a THEOREM (`soft-index-b.md` ⟨1⟩4.⟨2⟩1, from ML2) and is not
> assumed.
> **(e) abstract descendant package** (used only by the
> descendant-projected law `soft-index-b.md` ⟨1⟩5): (H-band)
> `‖𝔇_N(k,h)‖≤C_I|k|` uniformly in `N`; the transit bound (tr′); and
> D24(d) clauses 1, 3, 4 transplanted to the protocol datum ((1′),(3′),
> (4′) there).  Clauses 2 and 5 of D24(d) are NOT assumed — they are
> discharged by the protocol (`soft-index-b.md` ⟨1⟩5.⟨2⟩1).

### §M3 — claims/CLAIMS.md, append rows (all SKETCH; L6 promotes)

> | S-IDX-fin-B | Unconditional finite-volume soft-index identity, abstract SU(2)/density register: on `ker S^+` with `M=ρN−n>0`, `D†D=2M` and `P_{n,N}J^-_0=Q_0J^z_0/M`; one-hard `⟨h|J^z_0|h⟩=iv(h)` exactly for `N>N_0(R_h)`; D29 restatement: the `k=0` fiber of the protocol datum is exactly `1` at every finite index, and the deviation is driven by the contact defect `𝔇(k,h)` with `‖𝔇‖≤C|k|` (`N`-independent), kinematic factor separated.  `ρ` free; the su(2) `2` and the slope `2` kept distinct. | SKETCH | D6--D8, D10, G0(e), ML4-Ward, S2-2body-S | theory/soft-index-b.md ⟨1⟩2--⟨1⟩3 | SIB-C0, SIB-C1, SIB-C3 (proposed) |
> | S-IDX-spec-B | Conditional subsequential soft law (concrete anchor): under D29+D30(a,b)(+(d) at `S≥1`), every subsequential limit point of the datum family obeys the Adler zero `𝖲^*(0)=0` and the jet `∂\arg(1+𝖲^*)|_0=\mathrm{sgn}(v_h−v_s)|q|/ρ` (`=1/S` on D8), with the jet value subsequence-independent without the convenience clause.  No existence of limit points claimed; bound states/extra bands allowed. | SKETCH | D29, D30, ML2, S2-2body, S2-2body-S, OR1, OR2 | theory/soft-index-b.md ⟨1⟩4 | SIB-C2 (proposed); probe P1 (recorded PASS) |
> | S-IDX-desc-B | Abstract descendant-projected law: in the SU(2)/density register, under D30(e), every limit point of the descendant-projected datum obeys the Adler zero and jet `\mathrm{sgn}(v_h−v_s)|q|/ρ`, by the displayed bookkeeping (Ward residue `2iv_h`) × (leg-norm density `2ρ`)⁻¹ × (pole `v_hk_s`)⁻¹ × (kinematic `ik_s`); D24(d) clauses 2,5 discharged by the protocol, clauses 1,3,4 assumed.  Full unprojected abstract law NOT claimed. | SKETCH | S-IDX-fin-B, ML4-A, ML5-B (architecture), D24(d), D30 | theory/soft-index-b.md ⟨1⟩5 | SIB-C3 (proposed) |
> | S-IDX-src-B | Source bridge: a D24(a) source with per-index D24(b)-(c) regularity uniform along the subsequence and limit zero conditions `M_2^O(0,·)=0`, `𝔠_h(O)=0` inherits the subsequential law with `M_1^O` in place of the charge-created amplitude (ρ=1/2 register).  O_η untouched; no unrestricted universality implied. | SKETCH | ML5-A, D24, S-IDX-spec-B | theory/soft-index-b.md ⟨1⟩6 | probe P2 (recorded PASS) |

### §M4 — notation.md, append rows

> | `𝒜_{N,T,W,σ}(ε)`, `\mathfrak r_{N,T,W,σ}(ε)` | D29 windowed charge-created protocol datum and its ratio form (`𝒜=\mathfrak r−1`) | definitions.md D29 |
> | `Λ_N(ε)` | on-shell soft sample set `(2πℤ/N)∩\mathrm{supp}f_ε`; EMPTY for `ε<2π/(c_2N)` (ML4-Q1 immunity) | definitions.md D29 |
> | `𝔇(k,h)` | contact defect `(H−ω(h)−ω(k))Q_k\|h⟩_N`; `‖𝔇‖≤C_I\|k\|` `N`-uniformly; at `S=1/2` exactly `(J/\sqrt N)(z_k−1)(z_h−1)\|C_{k+h}⟩` | theory/soft-index-b.md (B7)--(B9) |
> | `M` (sector weight) | `S^z_{tot}`-value `ρN−n` of the highest-weight sector; LOCAL to theory/soft-index-b.md; never a D1(e) bond insertion there (overload rule: bond-insertion `M` never appears in that shard) | theory/soft-index-b.md ⟨1⟩2 |
> | `r_{out/in}[B]` | D7 chamber-coefficient out/in ratio of an exact two-magnon eigenvector in the D29 window labelling | definitions.md D30(b) |

## HONEST STATUS

**What is proved (pending L6; self-status SKETCH throughout).**

- (S-IDX.0): the finite-volume soft-index identity (B4)--(B7) — Ward
  projection at the abstract SU(2)/density register with `ρ` free, exact
  one-hard velocity datum `⟨h|J^z_0|h⟩=iv(h)` (for `N>N_0(R_h)`), the
  exact `k=0`-fiber datum value `1`, and the exact Duhamel identity
  (B8)--(B9) with `N`-independent `O(k)` defect bound at `S=1/2`.  These
  steps are unconditional finite-volume algebra; I believe they are
  airtight and they are the lane's rung-0 deliverable.
- (S-IDX.1a): PROVED as a conditional theorem given D29-B + D30-B(a,b)
  (+(d) at `S≥1`), riding on ML2 (PROVED), ML4's branch computation, and
  S2-2body(-S) (PROVED).  The near-shell localization lemma SIB-L1 is
  proved at `S=1/2`.
- (S-IDX.1b): PROVED as the descendant-projected conditional statement
  under the D30(e) package, with D24(d) clauses 2 and 5 genuinely
  discharged by the protocol — the structural advance over ML5-B.
- (S-IDX.2): a corollary of ML5-A under uniform-in-`j` D24 regularity.
- (S-IDX.3): anchors (a), (b) are exact matches; (c) is conditional on
  ML1+ML6 with the missing interchange step NAMED.

**Retreats and downgrades (every fork recorded).**

1. **(S-IDX.1) split.**  The single target statement became (1a)
   (concrete spin-`S` anchor, full datum, contact-algebra route) and
   (1b) (abstract register, DESCENDANT-PROJECTED only).  I could not
   prove the full abstract law: without a contact algebra the orthogonal
   channel is controlled only by the assumed ML4-A clause (4′), and
   dropping it leaves the projected law.  This is the target brief's own
   sanctioned fallback, taken.
2. **(TGT2) is stronger than the target's template (TGT).**  The brief
   suggested "uniform local boundedness + equicontinuity" might suffice.
   It does not, as far as I can see: equicontinuity makes the jet
   WELL-DEFINED but pins no VALUE — no exact identity constrains the
   family at fixed `ε>0` without reaching the on-shell spectral data
   somewhere.  My (TGT2) (readout settling onto near-shell chamber data,
   value-free) is the weakest clause I found that lets the PROVED
   contact algebra pin the value.  Recorded as a deliberate
   strengthening with the defense in ⟨1⟩8.6/⟨1⟩8.8; if the critic or the
   other lane finds a genuinely weaker sufficient (TGT), it supersedes
   mine.
3. **Spin `S≥1` representability is hypothesis (D30(d)).**  There is no
   ML2 analogue at `S≥1`; near-shell eigenvectors being regular
   scattering vectors (and bound-band exclusion) is assumed there,
   proved only at `S=1/2`.
4. **Anchor (c) is conditional on ML1 AND ML6**, with the finite-volume
   settling-defect interchange named as the missing step; I did not
   derive (TGT2) from ML1 alone.
5. **D26(INT) is carried but unused** (H-SIDX template compatibility;
   flagged in ⟨1⟩8.6).
6. **No second-order claim.**  The quadratic coefficient is
   hard-dependent and window-averaged; only the linear jet is law.
7. **Aggregation vs row-resolution.**  The theorem is proved row-wise
   and then aggregated; the probe fits rows.  The row-resolved variant
   of (S-IDX.1a) holds by the same steps (drop the `w_ε` average); D29-B
   records the aggregate as the headline datum for norm-cleanliness.
8. **(S-IDX.2) stays at `ρ=1/2`** (ML5-A's register); the spin-`S`
   source bridge would need D24 re-normed at density `ρ` and is not
   claimed.
9. **Existence of limit points is never claimed** (except conditionally
   in anchor (c)); nonvacuity beyond finite index is Lane S2's burden.

**What broke.**  Nothing was refuted: the target as stated survives in
the split form (1a)+(1b).  The one formulation-level finding is
negative-space: the target's suggested weakest (TGT) (equicontinuity
only) appears INSUFFICIENT for slope rigidity (retreat 2) — the two
lanes' D30 proposals should be compared exactly here.

**Interfaces for the merge.**  D29/D30 wording in §M1--§M2; the S2
interface point is D30(b) on `\mathrm{ran}W_±` (= the brief's (A2M.3));
checker interface is SIB-C0--C3 for the orchestrator's checker lane.

*Line count and shard-size note (L2): this file exceeds the 200--500 loc
shard guidance because the lane brief mandates the full ladder in one
writable file; the natural split points for a post-merge refactor are
⟨1⟩1--⟨1⟩3 (protocol + index identity), ⟨1⟩4--⟨1⟩5 (laws), and
⟨1⟩6--⟨1⟩8 (bridges, anchors, audit).*
