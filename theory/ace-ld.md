<!-- ROLE: proposer shard for the named lemma ACE-LD, round 2 (the reroute).
     r1 verdict: theory/verdicts/ace-ld-r1.md FAIL(F1,M1-M6).  Work order:
     briefs/ace-ld-repair-r2.md.  r1's (E-TAIL)/(V-ch) escape route is
     DELETED per F1 (empty hypothesis class); the obstruction is restated at
     the minimal strength of verdict objection M2; the main positive content
     is now the epsilon-version (AD3-ex-eps) of D13(a)'s own tail bound.
     Objection dispositions: theory/ace-ld-r2-response.md.
     Lane: this file, theory/ace-ld-r2-response.md, and
     theory/checks/ace_ld_check.py only.  All text destined for shared files
     is in section MERGE PROPOSALS below.
     Status: proposer draft, r2.  A critic pass is pending; nothing here
     upgrades any CLAIMS.md row until the L6 loop converges. -->

# ACE-LD r2 — window-charge spectral collapse, the ε-version, and the first-moment obstruction

**Proposer status (r2).**  Four results, stated with their exact quantifiers
in §0:

1. **ACE-LD-abs** (abstract; N channels; general on-site spin) — unchanged
   from r1, VERIFIED by the r1 critic (verdict §5 item 1): first-moment
   channel escape plus distinct channel charges implies window-charge
   spectral diagonality with a `t`-uniform constant.
2. **ACE-LD-nec** (necessity) — unchanged modulo the m3 lockstep fix:
   distinct charges are necessary.
3. **ACE-LD-ε** (NEW; the main positive content): under two named
   hypotheses — confined-core exponential tail clustering **(K-TAIL)** and
   sharp relative charge **(K-Q)** — the **ε-version** of (AD3-ex) holds:

   > **(AD3-ex-ε).**  `limsup_{t→+∞} ||(Q̂_{W,c_0} − q_ch)P_chΨ_t|| ≤
   > C λ̃^{d_W}` at each fixed window `W`, with `d_W` the core-to-edge
   > padding of D13(a); hence `→ 0` as `W↑ℤ` in the D18(AD4) order.

   This is D13(a)'s own tail-bound clause elevated to a theorem, it is
   compatible with D27(LR3), and it is what `ansatz-scattering.md`
   ⟨1⟩7.⟨2⟩2 consumes in the ordered limit (⟨1⟩4.⟨2⟩7).  Its hypothesis
   class is **inhabited**: D16's static-kink sector states satisfy both
   hypotheses, and the r1 critic measured the predicted `λ̃^{d_W}` decay on
   D16's exact zero modes to three digits (ratios `0.2089, 0.2085, 0.2041`
   against `q = 0.208712`; re-certified here by checker gate LD-C7).
4. **ACE-LD-obst′** (the obstruction, restated at minimal strength per
   verdict M2): D27(LR3) fails on every class with nonvanishing mean tail
   transport, from D27's own first-moment identity alone — no `(E-TAIL)`,
   no `(V-ch)`, no `(V-in)`, no `σ_L ≠ σ_T`, no channel structure at all.

**DELETED in r2 (verdict F1 — do not restore).**  r1's PROPOSITION
ACE-LD-esc, COROLLARY ACE-LD, and PROPOSITION ACE-LD-obst as previously
stated are withdrawn, together with their hypotheses `(E-TAIL)`, `(V-ch)`,
`(V-in)`.  Reason: `(E-TAIL)` is *equivalent* to `χ=1` `S^z`-product vacua
(REMARK ⟨1⟩4.⟨2⟩9 below), which pins the class to D16 — and D16's kink band
is **exactly flat** (`v_K ≡ 0`, ground energy `0` in every `S^z` sector;
verdict F1(b)(iii), re-certified by LD-C7), so `(V-ch)` fails there:
`(E-TAIL) ∧ (V-ch)` is empty on every instantiated model.  Also withdrawn
as FALSE: the r1 sentence "on the fixed-packet class of D28 the kink is
ballistic" — D28(4) constrains only the *relative* velocity `v_M − v_K`, so
D28's class contains the static-kink class and D16 realises it (verdict
F1(b)(iv)).  Their correct proof steps that the r1 critic verified
(LD-STRADDLE, LD-CONE, LD-IN, LD-TPM, and the r1 obstruction's conclusion
*on its own hypotheses*) are recorded in the r1 file history and the
verdict; none is re-claimed here on an empty class, and no repaired
hypothesis pair replaces them.

All definitions are by D-number from `definitions.md` (L4); no symbol is
redefined here.  Inherited results are cited by Lamport address into
`theory/memory-index.md` (prefix **MI**); `theory/ansatz-scattering.md`
(prefix **AS**) is *discussed* but no estimate of AS is consumed by any
proof below.

---

## 0. Statements

### LEMMA ACE-LD-abs (abstract spectral collapse; N channels)

**ASSUME.**
(A1) A Hilbert space `H`, a strongly continuous unitary group `e^{-itH}`, a
unit vector `Ψ`, and `Ψ_t := e^{-itH}Ψ`.
(A2) A bounded self-adjoint operator `Q̂` on `H` (time independent —
Schrödinger picture) whose spectrum is a **finite** set contained in a single
coset `κ+ℤ`, `κ∈[0,1)`.  [In the instance this is `Q̂_{W,c_0}` at a fixed
finite window, and the coset containment is the PROVED **M-INDEX-fin**
(MI ⟨1⟩1), cited — not re-proved.]
(A3) A finite family `{P_ch}_{ch=1}^{n}` of mutually orthogonal projections,
each commuting with `e^{-itH}`, with `Σ_ch P_ch Ψ = Ψ`.
(A4) Real numbers `{q_ch}_{ch=1}^{n}` (the *channel charges*) and
first-moment escape: `ε_ch(t) := ||(Q̂-q_ch)P_chΨ_t|| → 0` as `t→+∞`, for
every `ch`.
(A5) The `q_ch` are pairwise distinct.

**PROVE.**  With `E(·)` the spectral measure of `Q̂` and
`d_ch := dist(q_ch, spec Q̂ ∖ {q_ch}) > 0`,

  `||E({q_ch})Ψ_t − P_chΨ_t|| ≤ Σ_{ch'=1}^{n} d_{ch'}^{-1} ε_{ch'}(t) → 0`
  for every `ch`,                                                **(LD.1)**

the constant `Σ_{ch'} d_{ch'}^{-1}` being independent of `t`.  Moreover if
`q_ch ∈ κ+ℤ` then `d_ch ≥ 1`, so under (A2) the constant is at most `n` for
coset-valued charges.

### LEMMA ACE-LD-nec (necessity of distinct charges)

**ASSUME.** (A1)--(A4) with `n=2` and `q_1 = q_2 =: q`, and
`w_i := liminf_{t→+∞}||P_iΨ_t|| > 0` for **both** `i=1,2`.  *(r2 lockstep
fix, verdict m3: `w_1 > 0` is a hypothesis, used in ⟨1⟩3.⟨2⟩4; r1's §0
listed only `w_2`.)*

**PROVE.**  For **every** `q'∈ℝ`,
`liminf_{t→+∞} ||E({q'})Ψ_t − P_1Ψ_t|| > 0`; in particular the
(AD3-ex)-form display fails for channel 1 for every charge assignment, and
by symmetry for channel 2.

### THEOREM ACE-LD-ε (the ε-version of (AD3-ex); D13(a)'s tail bound as a theorem)

Fix a representation `π` of `𝔄` on a Hilbert space `H` (in the instance,
the covariant kink-sector realization of D28(1)) and write `S^z_x` for
`π(S^z_x)`, `ω_φ(·) := ⟨φ, ·φ⟩` for unit `φ ∈ H`.  For a finite interval
`K = [ℓ,r] ⊂ ℤ` and `x ∉ K` put `γ(x) := α` if `x < ℓ`, `β` if `x > r`, and

  `D_x := S^z_x − s_{γ(x)}`,  `s_α = +s`, `s_β = −s`

(the on-site deviation from the D13(a)/H-MQG(2) tail density on the side of
`x`).  The two named hypotheses, for a unit vector `φ`:

> **(K-TAIL) — confined-core exponential tail clustering.**  There are a
> finite interval `K = [ℓ,r]` and constants `C_K < ∞`, `λ̃ ∈ (0,1)` such
> that for all `x, x' ∉ K` with `γ(x) = γ(x')` (same side),
>
>   `|ω_φ(D_x D_{x'})| ≤ C_K² λ̃^{dist(x,K)} λ̃^{dist(x',K)}`.
>
> *(With `x = x'` this contains the on-site bound
> `||D_xφ||² ≤ C_K²λ̃^{2·dist(x,K)}`.)*

> **(K-Q) — sharp relative charge.**  There are `q_φ ∈ ℝ` and `ε_Q ≥ 0`
> with `||𝒬_{c_0}φ − q_φφ|| ≤ ε_Q`, where `𝒬_{c_0}φ :=
> lim_{n} Q̂_{W_n,c_0}φ` is the relative-charge limit vector, which EXISTS
> on every (K-TAIL) state and is exhaustion-independent (⟨1⟩4.⟨2⟩2 — a
> lemma, not a hypothesis; no sector-wide operator is constructed, so
> M-INDEX-LA-strong is not touched).

**ASSUME.**  H-MQG(1)--(2); a finite window `W = [a,b] ⊇ K` with cut
`c_0 ∈ W`; a unit vector `φ` satisfying (K-TAIL) and (K-Q); and
`d_W := dist(K, ℤ∖W) = min(ℓ−a, b−r) + 1 ≥ 1` (the D13(a) core-to-edge
padding).

**PROVE.**

  `||(Q̂_{W,c_0} − q_φ)φ|| ≤ ε_Q + \frac{2C_K}{1−λ̃}\,λ̃^{d_W}`.  **(LD.4)**

Consequently `dist(q_φ, spec π(Q̂_{W,c_0})) ≤` the same bound, so `q_φ`
lies within it of the M-INDEX-fin coset `κ_{W,c_0}+ℤ`.

### COROLLARY ACE-LD-ε-t (the family form; the display of the work order)

**ASSUME.**  Additionally (A1), a projection `P_ch` commuting with
`e^{-itH}`, `P_chΨ ≠ 0`, and: the normalized family
`φ_t := P_chΨ_t/||P_chΨ||` satisfies (K-TAIL) with `t`-independent
`(K, C_K, λ̃)` and (K-Q) with `t`-independent `(q_ch, ε_Q)`, for all
`t ≥ 0`.

**PROVE.**  `sup_{t≥0} ||(Q̂_{W,c_0} − q_ch)P_chΨ_t|| ≤
||P_chΨ||\,(ε_Q + \frac{2C_K}{1−λ̃}λ̃^{d_W})`; in particular, with
`ε_Q = 0` and `C := 2C_K||P_chΨ||/(1−λ̃)`,

  `limsup_{t→+∞} ||(Q̂_{W,c_0} − q_ch)P_chΨ_t|| ≤ C\,λ̃^{d_W}`
  **(AD3-ex-ε)**

at each fixed `W`, hence `→ 0` as `W↑ℤ` along any exhaustion with
`d_W → ∞` — the D18(AD4) order, window limit last.  No statement about
D27's TPM tails is made; (AD3-ex-ε) is **compatible with D27(LR3)**.

### COROLLARY ACE-LD-ε-x (cross-term vanishing in the ordered limit)

**ASSUME.**  Two channels `ch ∈ {L,T}` each satisfying ACE-LD-ε-t with
charges `q_L ≠ q_T`, common `λ̃`, `ε_Q = 0`; put `δ := |q_L − q_T|/2 > 0`
and `ε_W := \max_{ch} \frac{2C_{K,ch}||P_{ch}Ψ||}{1−λ̃}λ̃^{d_W}`, and let
`W` be large enough that `ε_W < δ`.

**PROVE.**  With `S_T := spec π(Q̂_{W,c_0}) ∩ (q_T−δ, q_T+δ)`,

  `limsup_{t→+∞} |⟨Ψ_t, P_L E_W(S_T) Ψ_t⟩| ≤ δ^{-1} ε_W`,
  `limsup_{t→+∞} ||(1 − E_W(S_T))P_TΨ_t|| ≤ δ^{-1} ε_W`,

both `= O(λ̃^{d_W}) → 0` in the ordered limit (`t→+∞` at fixed `W`, then
`W↑ℤ`).  This is the inter-channel cross-term vanishing that AS ⟨1⟩7.⟨2⟩2
derives from (AD3-ex) — supplied here in the ordered limit without the
false fixed-`W` exact form.  *(Reading discipline, verdict M5: this is the
**kink**-eigenstate reading of D18(AD3), ε-weakened — the kink is confined
inside `W` and the window state is an approximate `Q̂_W`-eigenvector.  It
is NOT the vacuum-eigenstate reading of r1's deleted route, and NOT the
weak-\* state convergence that M-INDEX-spec's reduction clause assumes;
⟨1⟩4.⟨2⟩8 itemises exactly what is and is not supplied.)*

### PROPOSITION ACE-LD-obst′ (first-moment obstruction to D27(LR3); minimal hypotheses)

**ASSUME.**  H-MQG(1)--(3), D26(INT); the D27 setting: a D17 vector `Ψ`, a
cut `c_0`, a padded exhaustion `W_m = [a_m,b_m] ↑ ℤ` containing `c_0`;
D27(LR1)--(LR2) (so the fixed-window Cesàro states `ω^±_{W_m}` and TPM laws
`p_{W_m}` exist, `p_{W_m}` is a probability on `ℤ` by MI ⟨1⟩5, and the
first-moment identity MI ⟨1⟩7.⟨2⟩1--⟨2⟩2 holds); and

> **(M-ESC) — mean tail transport.**
> `θ := liminf_m \frac{|ω^+_{W_m}(𝔛_{W_m}) − ω^-_{W_m}(𝔛_{W_m})|}{|W_m|}
> > 0.`

**PROVE.**
(a) `|Σ_ν ν\,p_{W_m}(ν)| ≥ 2sθ|W_m|(1 − o(1)) → ∞`.
(b) D27(LR3) **fails**: for every `M`,
`sup_m Σ_{|ν|>M}(1+|ν|)\,p_{W_m}(ν) = ∞`.
(c) D27's ordered wall expectation `δx` is undefined along the exhaustion:
its defining differences diverge linearly, at rate `≥ θ` per window site.
Contrapositive: **D27(LR3) forces `θ = 0`** — mean wall transport must be
`o(|W_m|)` on any (LR) state.

*(Scope.  (M-ESC) needs only the MEAN tail density — no variance
hypothesis, no channel structure, no wave operators, no `(E-TAIL)`,
`(V-ch)`, `(V-in)`, no `σ_L ≠ σ_T`, no incoming concentration.  A
kink component transiting every fixed window with asymptotic mean weight
`p_tr > 0` gives `θ = p_tr` (⟨1⟩5.⟨2⟩5), so on such "ballistic" classes the
unsubtracted window charge admits no (LR) outcome measure.  D16 is in the
COMPLEMENT: its kink band is exactly flat, `θ = 0`, and nothing here bears
on the (LR)-for-D16 lane bd `tns-xf4`.)*

---

## 1. The abstract lemmas (r1 content, VERIFIED by the r1 critic — verdict §5 items 1–2; not churned)

### ⟨1⟩1. LEMMA (finite-spectrum gap estimate)

**ASSUME.** (A2) of ACE-LD-abs: `Q̂` bounded self-adjoint with finite
spectrum `S := spec Q̂`, and a real number `q` with
`d_q := dist(q, S∖{q}) > 0` (automatic for finite `S` unless `S={q}`, in
which case set `d_q := +∞` and read `1/d_q = 0` below).

**PROVE.**  For every vector `φ∈H`,

  `||(1 − E({q}))φ|| ≤ d_q^{-1} ||(Q̂ − q)φ||`.                  **(LD.3)**

If `q ∉ S` then `E({q}) = 0` and (LD.3) reads
`||φ|| ≤ dist(q,S)^{-1}||(Q̂−q)φ||`.

**⟨2⟩1.**  `Q̂` restricted to `ran(1−E({q}))` is self-adjoint with spectrum
`S∖{q}`, hence `(Q̂−q)` restricted there is invertible with
`||((Q̂−q)|_{ran(1−E({q}))})^{-1}|| = max_{λ∈S∖{q}} |λ−q|^{-1} = d_q^{-1}`.

*Justification.*  Spectral theorem for a bounded self-adjoint operator with
finite spectrum: `Q̂ = Σ_{λ∈S} λE({λ})`, so the restriction to the invariant
subspace `ran(1−E({q}))` has the stated spectrum, and functional calculus
gives the inverse norm.  Named computation **LD-GAP.1**.

**⟨2⟩2.**  `1−E({q})` commutes with `Q̂−q`, so

`||(1−E({q}))φ|| = ||((Q̂−q)|^{-1})(Q̂−q)(1−E({q}))φ||
 ≤ d_q^{-1}||(1−E({q}))(Q̂−q)φ|| ≤ d_q^{-1}||(Q̂−q)φ||`,

the last step because `||1−E({q})||≤1`.

*Justification.*  ⟨2⟩1 and functional calculus (spectral projections commute
with `Q̂`).  Named computation **LD-GAP.2**.

**⟨2⟩3.**  If additionally `S ⊂ κ+ℤ` and `q ∈ κ+ℤ`, then every point of
`S∖{q}` lies in `κ+ℤ` at distance `≥1` from `q`, so `d_q ≥ 1`.

*Justification.*  Two distinct points of one coset of `ℤ` differ by a nonzero
integer.  This is where the PROVED **M-INDEX-fin** (MI ⟨1⟩1: under D26(INT)
and H-MQG(2), `spec Q̂_{W,c_0} ⊂ κ_{W,c_0}+ℤ` with
`κ_{W,c_0} ≡ |W|κ + s(a+b−1−2c_0) (mod ℤ)`, time independent) enters the
instance: it supplies the hypothesis of this step for `Q̂ = Q̂_{W,c_0}`, and
it is cited, not re-proved.  In a GNS or sector representation
`spec π(Q̂_{W,c_0}) ⊂ spec Q̂_{W,c_0}`, so the coset containment survives
representation (C*-algebra spectral permanence).  Named computation
**LD-GAP.3**.

**⟨2⟩4.**  The constants `d_q` (and hence (LD.3)) are independent of `t` in
any application with `Q̂` fixed: `Ψ_t` varies, `Q̂` does not, and `S` is a
fixed finite set.  No Lagrange-interpolation or Riesz-contour constant needs
tracking, because (LD.3) needs only the spectral gap, which is a property of
the fixed operator.

*Justification.*  ⟨2⟩1--⟨2⟩3; the operator `Q̂_{W,c_0}` of the instance is a
fixed element of `𝔄_W` (D13(a), D27), and the displays of §0 are in the
Schrödinger picture: `E_W(·)` fixed, `Ψ_t` evolving.

**⟨2⟩5. (Set form — r2 addition, consumed by ACE-LD-ε-x.)**  For a Borel
set `B ⊂ ℝ` with `d_B := dist(q, S∖B) > 0` for a real `q` (i.e. every
spectral point OUTSIDE `B` is at distance `≥ d_B` from `q`; `B` need not
contain `q`),

  `||(1 − E(B))φ|| ≤ d_B^{-1} ||(Q̂ − q)φ||`,   and dually
  `||E(B)φ|| ≤ d'^{-1}||(Q̂ − q')φ||` whenever `d' := dist(q', S∩B) > 0`.
  **(LD.3′)**

*Justification.*  Identical to ⟨2⟩1--⟨2⟩2 with `1−E({q})` replaced by
`1−E(B)` (resp. `E(B)`): on the invariant subspace `ran(1−E(B))` the
spectrum of `Q̂` is `S∖B`, so `(Q̂−q)` is invertible there with inverse norm
`max_{λ∈S∖B}|λ−q|^{-1} = d_B^{-1}`; likewise on `ran E(B)` with `q'` and
`S∩B`.  Named computation **LD-GAP-SET**.

**⟨2⟩6. QED.**

### ⟨1⟩2. PROOF of ACE-LD-abs

**ASSUME.** (A1)--(A5) of the §0 statement.

**PROVE.** (LD.1).

**⟨2⟩1. (Decomposition.)**  Fix `ch`.  Since `Σ_{ch'}P_{ch'}Ψ = Ψ` and each
`P_{ch'}` commutes with `e^{-itH}` (A3), also `Σ_{ch'}P_{ch'}Ψ_t = Ψ_t` for
every `t`.  Hence

`E({q_ch})Ψ_t − P_chΨ_t
 = −(1 − E({q_ch}))P_chΨ_t + Σ_{ch'≠ch} E({q_ch})P_{ch'}Ψ_t`.

*Justification.*  Algebra: `E({q_ch})Σ_{ch'}P_{ch'}Ψ_t − P_chΨ_t
= [E({q_ch})P_ch − P_ch]Ψ_t + Σ_{ch'≠ch}E({q_ch})P_{ch'}Ψ_t`.  Named
computation **LD-ABS.1**.

**⟨2⟩2. (Diagonal term.)**
`||(1 − E({q_ch}))P_chΨ_t|| ≤ d_ch^{-1} ε_ch(t)`.

*Justification.*  ⟨1⟩1 (LD.3) applied to `φ = P_chΨ_t` and `q = q_ch`, and
the definition of `ε_ch(t)` in (A4).

**⟨2⟩3. (Cross terms.)**  For `ch' ≠ ch`,
`||E({q_ch})P_{ch'}Ψ_t|| ≤ d_{ch'}^{-1} ε_{ch'}(t)`.

*Justification.*  By (A5), `q_ch ≠ q_{ch'}`.  If both are spectral points,
`E({q_ch})E({q_{ch'}}) = 0` (orthogonality of spectral projections of the
same self-adjoint operator at distinct points); if either is not a spectral
point its projection is `0` and the product vanishes trivially.  Hence

`E({q_ch})P_{ch'}Ψ_t = E({q_ch})(1 − E({q_{ch'}}))P_{ch'}Ψ_t`,

and `||E({q_ch})|| ≤ 1` with ⟨1⟩1 (LD.3) at `q = q_{ch'}`, `φ = P_{ch'}Ψ_t`
gives the bound.  Named computation **LD-ABS.2**.

**⟨2⟩4. (Assembly.)**  Triangle inequality over ⟨2⟩1's decomposition, using
⟨2⟩2 once and ⟨2⟩3 for the `n−1` cross terms, gives

`||E({q_ch})Ψ_t − P_chΨ_t|| ≤ d_ch^{-1}ε_ch(t) + Σ_{ch'≠ch}d_{ch'}^{-1}ε_{ch'}(t)
 = Σ_{ch'} d_{ch'}^{-1}ε_{ch'}(t)`,

which tends to `0` by (A4).  The constant is `t`-independent by ⟨1⟩1.⟨2⟩4,
and `≤ n` when all `q_{ch'} ∈ κ+ℤ` by ⟨1⟩1.⟨2⟩3.

*Justification.*  ⟨2⟩1--⟨2⟩3.

**⟨2⟩5.**  Remarks on generality.  (i) Nothing in ⟨2⟩1--⟨2⟩4 restricts `n`
to `2`, restricts the on-site spin, or uses any property of `H` beyond (A1)
and (A3); the lemma is proved for `N` channels and a general on-site charge
observable.  (ii) (A3)'s commutation is used only to propagate
`ΣP_{ch'}Ψ = Ψ` to all `t`; the weaker hypothesis "`Σ_{ch'}P_{ch'}Ψ_t = Ψ_t`
for all `t` and `{P_{ch'}}` mutually orthogonal" suffices verbatim.
(iii) No continuity, gap arithmetic, or Lagrange constant beyond the single
spectral gap of ⟨1⟩1 is consumed: `spec Q̂` is a property of the fixed
Schrödinger-picture operator.

*Justification.*  Inspection of ⟨2⟩1--⟨2⟩4.

**⟨2⟩6. QED.**  □

### ⟨1⟩3. PROOF of ACE-LD-nec (distinct charges are necessary)

**ASSUME.** (A1)--(A4) with `n=2`, `q_1 = q_2 =: q`, and
`w_i := liminf_{t→+∞}||P_iΨ_t|| > 0` for `i=1,2`.

**PROVE.**  For every `q'∈ℝ`,
`liminf_{t→+∞}||E({q'})Ψ_t − P_1Ψ_t|| > 0`.

**⟨2⟩1. (Merged channel.)**  `P := P_1 + P_2` is a projection (mutual
orthogonality, (A3)) commuting with `e^{-itH}`, with `PΨ_t = Ψ_t`, and

`||(Q̂ − q)Ψ_t|| = ||(Q̂−q)(P_1+P_2)Ψ_t|| ≤ ε_1(t) + ε_2(t) → 0`.

*Justification.*  (A3), (A4), triangle inequality.  Named computation
**LD-NEC.1**.

**⟨2⟩2. (The full vector collapses onto one spectral point.)**
`||(1 − E({q}))Ψ_t|| ≤ d_q^{-1}(ε_1(t)+ε_2(t)) → 0`, i.e.
`||E({q})Ψ_t − Ψ_t|| → 0`.

*Justification.*  ⟨1⟩1 (LD.3) with `φ = Ψ_t`, using ⟨2⟩1.  (If `q ∉ spec Q̂`
this forces `||Ψ_t|| → 0`, contradicting `||Ψ_t|| = 1`; so under the
standing normalisation `q ∈ spec Q̂` and `d_q` is the coset gap.)

**⟨2⟩3. (Case `q' = q`.)**
`||E({q})Ψ_t − P_1Ψ_t|| ≥ ||Ψ_t − P_1Ψ_t|| − ||E({q})Ψ_t − Ψ_t||
 = ||P_2Ψ_t|| − o(1)`,
using `Ψ_t − P_1Ψ_t = P_2Ψ_t` (⟨2⟩1) and ⟨2⟩2.  Hence the liminf is
`≥ w_2 > 0`.

*Justification.*  Reverse triangle inequality, ⟨2⟩1, ⟨2⟩2.

**⟨2⟩4. (Case `q' ≠ q`.)**  `E({q'})E({q}) = 0` (distinct points; or
`E({q'})=0` if `q'∉spec`), so

`||E({q'})Ψ_t|| = ||E({q'})(Ψ_t − E({q})Ψ_t)|| ≤ ||Ψ_t − E({q})Ψ_t|| → 0`,

and therefore
`||E({q'})Ψ_t − P_1Ψ_t|| ≥ ||P_1Ψ_t|| − o(1)`, liminf `≥ w_1 > 0`.  This is
the step that consumes `w_1 > 0` (the §0 ASSUME now lists it — r2 fix,
verdict m3).

*Justification.*  Orthogonality of spectral projections, ⟨2⟩2, reverse
triangle inequality.  Named computation **LD-NEC.2**.

**⟨2⟩5. QED.**  □  *(Consequence: when both channels' first moments escape
to the SAME charge, the (AD3-ex)-form display is false for channel 1 no
matter which eigenvalue is claimed for it — ⟨2⟩3 kills the shared value,
⟨2⟩4 kills every other value.  By symmetry the same holds for channel 2.
The r1 uniqueness argument LD-UNIQUE lived in the deleted ⟨1⟩4 and is not
re-claimed; nothing below consumes it.)*

---
