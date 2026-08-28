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
The r1 uniqueness argument LD-UNIQUE lived in the deleted r1 ⟨1⟩4 (the r2 ⟨1⟩4 below is the ε-version) and is not
re-claimed; nothing below consumes it.)*

---

## 2. The ε-version

### ⟨1⟩4. PROOF of ACE-LD-ε and its corollaries

**ASSUME.**  The ASSUME block of THEOREM ACE-LD-ε (§0): H-MQG(1)--(2),
`K = [ℓ,r] ⊆ W = [a,b]` finite, `c_0 ∈ W`, unit `φ` with (K-TAIL) and
(K-Q), `d_W = dist(K, ℤ∖W)`.

**⟨2⟩1. (LEMMA LD-SPLIT — window difference identity.)**  For finite
windows `W = [a,b] ⊆ W' = [a',b']` with `c_0 ∈ W`,

  `Q̂_{W',c_0} − Q̂_{W,c_0}
   = Σ_{x=a'}^{a−1}(S^z_x − s) + Σ_{x=b+1}^{b'}(S^z_x + s)`,

i.e. the difference is exactly the sum of the on-site tail deviations
`D_x` over the annulus `W'∖W` (left annulus on the `α` side, deviation
`S^z_x − s`; right annulus on the `β` side, deviation `S^z_x + s`),
PROVIDED `W ⊇ K` so that every annulus site is outside `K` on a definite
side.

*Justification.*  MI ⟨1⟩1.⟨2⟩2 (M-INDEX-fin's expansion of D13(a)):
`Q̂_{W,c_0} = Σ_{x∈W}S^z_x + s(a+b−1−2c_0)`.  Subtracting,

`Q̂_{W',c_0} − Q̂_{W,c_0} = Σ_{x=a'}^{a−1}S^z_x + Σ_{x=b+1}^{b'}S^z_x
 + s[(a'+b') − (a+b)]`,

and the scalar regroups exactly: `−s·#[a',a−1] + s·#[b+1,b']
= −s(a−a') + s(b'−b) = s(a'+b'−a−b)`.  Named computation **LD-SPLIT**.
The cut dependence cancels in the difference (`c_0` appears in both terms
with the same coefficient) — the same cancellation mechanism as
M-INDEX-fin ⟨1⟩5.⟨2⟩3, here at the level of the operator itself.

**⟨2⟩2. (LEMMA LD-TAIL — tail sums, and the relative-charge limit
vector.)**  Under (K-TAIL):

(i) For every finite `F ⊂ ℤ∖K` lying entirely on one side of `K`, with
`d := dist(F,K)`,

  `||Σ_{x∈F} D_x φ|| ≤ \frac{C_K}{1−λ̃}\,λ̃^{d}`.

(ii) For every exhaustion `{W_n}` of `ℤ` by finite windows with
`W_n ⊇ K ∪ {c_0}`, the vectors `Q̂_{W_n,c_0}φ` converge in norm; the limit
`𝒬_{c_0}φ := lim_n Q̂_{W_n,c_0}φ` is the same for every such exhaustion,
and for every finite `W ⊇ K` with `c_0 ∈ W`,

  `||𝒬_{c_0}φ − Q̂_{W,c_0}φ|| ≤ \frac{2C_K}{1−λ̃}\,λ̃^{d_W}`.   **(LD-TAIL)**

*Justification.*  (i): expand the square and use self-adjointness of each
`D_x`:
`||Σ_{x∈F}D_xφ||² = Σ_{x,x'∈F}⟨D_xφ, D_{x'}φ⟩ = Σ_{x,x'∈F}ω_φ(D_xD_{x'})`,
every pair being same-side; (K-TAIL) bounds this by
`(Σ_{x∈F}C_Kλ̃^{dist(x,K)})²`.  Distinct sites of a one-sided `F` have
pairwise distinct integer distances to `K`, all `≥ d`, so
`Σ_{x∈F}λ̃^{dist(x,K)} ≤ Σ_{j≥d}λ̃^{j} = λ̃^{d}/(1−λ̃)`.  Taking the
square root gives (i).  (ii): for `W ⊆ W'` both containing `K ∪ {c_0}`,
LD-SPLIT (⟨2⟩1) writes `(Q̂_{W',c_0} − Q̂_{W,c_0})φ` as the sum of two
one-sided annulus sums, each at distance `≥ d_W` from `K`, so by (i)

`||(Q̂_{W',c_0} − Q̂_{W,c_0})φ|| ≤ 2C_Kλ̃^{d_W}/(1−λ̃)`.

Along any exhaustion `d_{W_n} → ∞`, so `{Q̂_{W_n,c_0}φ}` is Cauchy;
interleaving two exhaustions shows the limit agrees; and letting
`W' ↑ ℤ` in the display gives the uniform bound.  Named computation
**LD-TAIL**.  *(No operator `𝒬_{c_0}` on the sector is constructed —
only the limit VECTOR on a (K-TAIL) state.  The REFUTED
M-INDEX-LA-strong, which excludes an unconditional sector-wide
total-charge operator, is respected: the tail hypothesis is exactly the
extra condition under which the limit exists on this state.)*

**⟨2⟩3. (PROOF of (LD.4) and the coset location.)**  Decompose

`(Q̂_{W,c_0} − q_φ)φ = (Q̂_{W,c_0}φ − 𝒬_{c_0}φ) + (𝒬_{c_0}φ − q_φφ)`.

The second term has norm `≤ ε_Q` by (K-Q); the first has norm
`≤ 2C_Kλ̃^{d_W}/(1−λ̃)` by ⟨2⟩2(ii).  The triangle inequality gives
(LD.4).  For the coset location: for unit `φ`, the spectral theorem gives
`||(Q̂_{W,c_0} − q_φ)φ||² = ∫|λ−q_φ|²\,dμ_φ(λ) ≥ dist(q_φ, spec π(Q̂_{W,c_0}))²`,
so `dist(q_φ, spec π(Q̂_{W,c_0}))` is bounded by (LD.4)'s right side; and
`spec π(Q̂_{W,c_0}) ⊂ κ_{W,c_0}+ℤ` by M-INDEX-fin with spectral permanence
(⟨1⟩1.⟨2⟩3).  Hence `dist(q_φ, κ_{W,c_0}+ℤ) ≤ ε_Q + 2C_Kλ̃^{d_W}/(1−λ̃)`.
Named computation **LD-EPS**.  □ (THEOREM ACE-LD-ε.)

**⟨2⟩4. (REMARK — how (K-Q) propagates in `t`; the conservation
mechanism.)**  (K-Q) concerns the relative charge, which is CONSERVED;
that is what makes ACE-LD-ε-t's `t`-uniform hypothesis honest rather than
a disguised assumption of the conclusion.  Precisely: suppose the
realization carries a self-adjoint `𝒬̂` with `[e^{-itH}, 𝒬̂] = 0` whose
action on (K-TAIL) states agrees with the ⟨2⟩2 limit vector
(`𝒬̂φ = 𝒬_{c_0}φ`).  Then for `φ_t = e^{-itH}φ_0` (up to normalisation),
`||(𝒬̂ − q)φ_t|| = ||(𝒬̂ − q)φ_0||`: (K-Q) at `t = 0` propagates to all
`t` with the same `q, ε_Q`.  The window charge `Q̂_{W,c_0}` is NOT
conserved — that is the entire content of D13(c)'s trap paragraph — and no
such propagation is claimed for it; (LD.4) converts conserved-charge
sharpness plus instantaneous tail clustering into the window statement at
each time separately.  Whether a commuting `𝒬̂` exists is
realization-dependent and is NOT proved here in general (M-INDEX-LA-strong
forbids the unconditional sector-wide construction); in the D16 instance
it exists trivially — the fixed-`S^z`-sector realization, where sector
membership gives (K-Q) with `ε_Q = 0` exactly — and (K-TAIL)'s
`t`-uniformity there is the statement that the kink stays confined, true
because D16's kink band is exactly flat (verdict F1(b)(iii); certified
LD-C7).

**⟨2⟩5. (PROOF of COROLLARY ACE-LD-ε-t.)**  `P_ch` commutes with
`e^{-itH}`, so `||P_chΨ_t|| = ||e^{-itH}P_chΨ|| = ||P_chΨ||` for all `t`
and `φ_t := P_chΨ_t/||P_chΨ||` is a unit vector.  By hypothesis `φ_t`
satisfies (K-TAIL) and (K-Q) with `t`-independent data, so ⟨2⟩3 applies at
each `t` separately:

`||(Q̂_{W,c_0} − q_ch)P_chΨ_t|| = ||P_chΨ||\,||(Q̂_{W,c_0} − q_ch)φ_t||
 ≤ ||P_chΨ||\,(ε_Q + 2C_Kλ̃^{d_W}/(1−λ̃))`,

uniformly in `t ≥ 0`.  The `limsup` display (AD3-ex-ε) is the special case
`ε_Q = 0` with `C := 2C_K||P_chΨ||/(1−λ̃)`; `d_W → ∞` along any padded
exhaustion, so the bound `→ 0` with the window limit LAST — the D18(AD4)
order.  Compatibility with D27(LR3) is by inspection: no statement about
the TPM law `p_{W_m}` or its tails is made or implied; (LD.4) is a bound on
one channel's window-charge dispersion, not on the two-time increment law.
□ (ACE-LD-ε-t.)

**⟨2⟩6. (PROOF of COROLLARY ACE-LD-ε-x.)**  Write `S := spec π(Q̂_{W,c_0})`
and `S_T := S ∩ (q_T−δ, q_T+δ)`, `2δ = |q_L − q_T|`.  Every `λ ∈ S∖S_T`
has `|λ − q_T| ≥ δ`, and every `λ ∈ S_T` has
`|λ − q_L| ≥ |q_L−q_T| − |λ−q_T| > 2δ − δ = δ`.  By LD-GAP-SET
(⟨1⟩1.⟨2⟩5), with the ⟨2⟩5 bound `||(Q̂−q_ch)P_chΨ_t|| ≤ ε_W`:

- `||E_W(S_T)P_LΨ_t|| ≤ δ^{-1}||(Q̂_{W,c_0}−q_L)P_LΨ_t|| ≤ δ^{-1}ε_W`
  (dual form of (LD.3′), `q' = q_L`, `dist(q_L, S∩S_T) > δ`);
- `||(1−E_W(S_T))P_TΨ_t|| ≤ δ^{-1}||(Q̂_{W,c_0}−q_T)P_TΨ_t|| ≤ δ^{-1}ε_W`
  (first form, `q = q_T`, `dist(q_T, S∖S_T) ≥ δ`).

Cauchy--Schwarz with `E_W(S_T)` self-adjoint gives
`|⟨Ψ_t, P_LE_W(S_T)Ψ_t⟩| = |⟨E_W(S_T)P_LΨ_t, Ψ_t⟩| ≤ δ^{-1}ε_W`.  All
three bounds are uniform in `t` and `= O(λ̃^{d_W})`; they vanish in the
ordered limit.  □ (ACE-LD-ε-x.)  *(When `q_L, q_T` differ by a nonzero
integer of the coset — the expected situation, the transferred charge
being a coset step per M-INDEX-fin — one has `δ ≥ 1/2`, so the constants
are `≤ 2ε_W`.)*

**⟨2⟩7. (What AS ⟨1⟩7.⟨2⟩2 consumes, and what replaces the exact
display.)**  AS ⟨1⟩7.⟨2⟩2's derivation of the `{0,2}` outcome support
uses (AD3-ex) ONLY through the inter-channel cross-term vanishing
`|⟨Ψ_t,P_LE_W({q_T})Ψ_t⟩| → 0` (its own display) — and the object ⟨1⟩7
feeds, Lane T1's outcome measure, is an ORDERED-limit object (fixed-window
time limit first, `W↑ℤ` last, per D27 and D18(AD4)).  In that order
ACE-LD-ε-x supplies the same vanishing, with the singleton projections
`E_W({q_ch})` replaced by the coset-ball projections `E_W(S_ch)` and with
the quantitative rate `O(λ̃^{d_W})`; at any FIXED `W` an `O(λ̃^{d_W})`
coherence leak remains — which is exactly the tolerance D13(a) itself
grants the observable ("if `d_W` is the minimum core-to-edge distance,
D1(c) gives … a tail bound `C_{λ̃}λ̃^{d_W}`").  So (AD3-ex-ε) does the job
(AD3-ex) was introduced to do in ⟨1⟩7.⟨2⟩2, without asserting the false
fixed-`W` exact limit.  *(Orientation note, verdict n1: AS ⟨1⟩7.⟨2⟩1
writes `ν = q_T − q_in`, the opposite orientation to the frozen
`ν = q_- − q_+` of `notation.md`/MI ⟨1⟩5.⟨2⟩3; only `|ν|` enters here.
The defect is AS-lane's and is flagged in MERGE PROPOSALS MP-3, not
silently compared.)*

**⟨2⟩8. (Reading discipline — what is and is not supplied; verdict M5.)**
D18(AD3) has two readings in the corpus, and every statement here is
explicit about which it touches:

- **Supplied (kink reading, ε-weakened):** with the kink CONFINED in
  `K ⊂ W`, the channel state is an ε-approximate `Q̂_{W,c_0}`-eigenvector
  at the conserved channel charge `q_ch` — uniformly in `t`, defect
  `O(λ̃^{d_W})` (ACE-LD-ε-t) — and the channels are asymptotically
  charge-diagonal in the ordered limit (ACE-LD-ε-x).  This is the
  "remaining local state is a kink charge eigenstate" clause of D18(AD3)
  in ε-approximate NORM form.
- **Not supplied:** (i) the exact fixed-`W` limit (AD3-ex) — false in D16
  at every fixed `W`, where the defect is strictly positive and decays
  exactly like `λ̃^{d_W}` (verdict §8's `d16_var` computation; checker
  LD-C7); the `AD3-ex` claims row stays CONJECTURE, now with a known
  counterexample to its exact form (MERGE PROPOSALS MP-2).  (ii) The
  *vacuum*-eigenstate reading (r1's deleted route) — no statement about
  escaped-window vacuum charges is made anywhere in r2.  (iii) D18(AD3)'s
  remaining clauses — weak-\* convergence of the window restriction to a
  specific kink charge eigenstate, and existence of the increasing-window
  limit of D13(a) on it — in particular **M-INDEX-spec's reduction clause
  is NOT supplied** and its adjudicated scoping is untouched.  (iv) Any
  statement on classes where the kink transits: there (K-TAIL) fails for
  every fixed `K` and ACE-LD-obst′ (⟨1⟩5) rules instead.  (v) Any
  model-level PROOF of (K-TAIL)/(K-Q): the D16 instantiation is
  numerically certified on finite chains (⟨2⟩9), not proved in infinite
  volume.

**⟨2⟩9. (REMARK — scope: the χ=1 boundary, and the D16 instantiation.)**
(a) *The deletion rationale, recorded once (verdict F1/M1).*  r1's
`(E-TAIL)` demanded `ω_γ((S^z_x−s_γ)²) = 0` at every site.  This is
EQUIVALENT to `ω_γ` being the fully polarised `χ=1` `S^z`-product state:
if `ω_γ((S^z_x−s_γ)²)=0` then Cauchy--Schwarz gives
`|ω_γ((S^z_x−s_γ)A)|² ≤ ω_γ((S^z_x−s_γ)²)\,ω_γ(A^*A) = 0` for every
`A ∈ 𝔄`; taking `A` the on-site spectral projections of `S^z_x` pins
`ω_γ(Π_x^{(m)}) = δ_{m,s_γ}` at every `x`, and a state assigning `1` to
each of finitely many commuting projections assigns `1` to their product,
forcing `ω_γ = ⊗_x|s_γ⟩⟨s_γ|`; the converse is immediate.  (b) *The same
boundary scopes (K-TAIL).*  If the far tails of a (K-TAIL) state relax to
translation-invariant vacua `ω_γ` (weak-\* along translated windows), then
`ω_γ((S^z−s_γ)²) = lim_{dist(x,K)→∞} ω_φ(D_x²) = 0`, so by (a) the tail
vacua are `χ=1` `S^z`-product states.  The ε-version is therefore a
theorem about the sharp-tail corner of the programme — the corner D16
occupies — and is NOT claimed for generic injective-MPS vacua, whose
on-site charge variance is a nonzero constant and for which
`min_q||(Q̂_W−q)φ||` does not decay.  This is stated as scope, not hidden
as fine print.  (c) *The D16 instantiation (evidence, not proof).*  For
D16's exact zero-energy kink states projected to a fixed `S^z` sector:
(K-Q) holds with `ε_Q = 0` exactly (sector membership; ⟨2⟩4), and
(K-TAIL) holds with `λ̃ = q = Δ−√(Δ²−1)` on the numerical evidence:
at `Δ = 2.5`, `L = 12`, `c_0 = 5`, the sector ground state has
`min_q||(Q̂_W−q)Ψ|| = 4.45e-02, 9.30e-03, 1.94e-03, 3.96e-04` at
`W = [4,7],[3,8],[2,9],[1,10]` — successive ratios `0.2089, 0.2085,
0.2041` against `q = 0.208712` — with `⟨Q̂_W⟩` on the integer coset
(verdict §8, `d16_var.py`; independently re-implemented as checker gate
LD-C7).  The class of ACE-LD-ε's hypotheses is therefore INHABITED — the
exact defect r1's `(E-TAIL) ∧ (V-ch)` route died of (F1) — while its
infinite-volume verification on D16 remains open and is priced as such in
HONEST STATUS.

**⟨2⟩10. QED (⟨1⟩4).**  □

---

## 3. The obstruction at minimal strength

### ⟨1⟩5. PROOF of ACE-LD-obst′

**ASSUME.**  The ASSUME block of PROPOSITION ACE-LD-obst′ (§0):
H-MQG(1)--(3), D26(INT), the D27 setting (D17 vector `Ψ`, cut `c_0`,
padded exhaustion `W_m ↑ ℤ`), D27(LR1)--(LR2), and (M-ESC) with
`θ > 0`.

**⟨2⟩1. (Each `p_{W_m}` is a probability on `ℤ`.)**  At finite times the
TPM law is a probability supported on `ℤ` by MI ⟨1⟩5 (L-C: positivity and
sequential Parseval; support on `ℤ` by the fixed-window offset cancellation
⟨1⟩5.⟨2⟩3, which needs D26(INT) through M-INDEX-fin).  D27(LR1) makes the
double-Cesàro limits `p_{W_m}` exist at every fixed `m`; a pointwise limit
of probabilities on the fixed countable support `ℤ` is a subprobability,
and no mass escapes at fixed `W_m` because `|ν|` is bounded by the diameter
of the finite set `spec Q̂_{W_m,c_0}` — the law is supported on finitely
many `ν` at fixed `m`.  Hence each `p_{W_m}` is a probability on `ℤ`.

*Justification.*  MI ⟨1⟩5.⟨2⟩1--⟨2⟩3; D27(LR1); finiteness of
`spec Q̂_{W,c_0}` (finite sum of finite-spectrum on-site operators plus a
scalar, MI ⟨1⟩1.⟨2⟩2--⟨2⟩3).

**⟨2⟩2. (The first-moment identity.)**  For every fixed `m`,

  `Σ_ν ν\,p_{W_m}(ν) = −2s\,[ω^+_{W_m}(𝔛_{W_m}) − ω^-_{W_m}(𝔛_{W_m})]`.

*Justification.*  MI ⟨1⟩7.⟨2⟩1--⟨2⟩2, cited — not re-proved: ⟨2⟩1 there
is double-Cesàro averaging of the exact finite-time mean formula (IDX.4)
plus D27(LR2) (the vanishing averaged dephasing defect — exactly the
first-moment nondemolition clause), and ⟨2⟩2 there is the `−2sc_0` offset
cancellation.  This identity is also quoted verbatim in D27's own
definition paragraph.  No use of D27(LR3) is made.

**⟨2⟩3. (LR3 implies a uniform first absolute moment.)**  Suppose
D27(LR3) held: `lim_{M→∞} sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m}(ν) = 0`.  Choose
`M_0` with `sup_m Σ_{|ν|>M_0}(1+|ν|)p_{W_m}(ν) ≤ 1`.  Then for every `m`,

`Σ_ν |ν|\,p_{W_m}(ν)
 = Σ_{|ν|≤M_0}|ν|p_{W_m}(ν) + Σ_{|ν|>M_0}|ν|p_{W_m}(ν)
 ≤ M_0·1 + 1`,

using ⟨2⟩1 (total mass `1`) on the first sum.  Hence
`sup_m |Σ_ν ν\,p_{W_m}(ν)| ≤ M_0 + 1 < ∞`.

*Justification.*  Arithmetic on a probability; named computation
**LD-M0**.

**⟨2⟩4. (Conclusion: (a), (b), (c).)**  By ⟨2⟩2 and (M-ESC),

`|Σ_ν ν\,p_{W_m}(ν)| = 2s\,|ω^+_{W_m}(𝔛_{W_m}) − ω^-_{W_m}(𝔛_{W_m})|
 ≥ 2s\,θ\,|W_m|\,(1 − o(1)) → ∞`   *(claim (a); `s > 0` by H-MQG(2))*,

contradicting ⟨2⟩3's uniform bound: **D27(LR3) fails.**  Quantitatively,
for EVERY fixed `M` and every `m`,

`Σ_{|ν|>M}(1+|ν|)\,p_{W_m}(ν) ≥ Σ_{|ν|>M}|ν|\,p_{W_m}(ν)
 ≥ Σ_ν|ν|p_{W_m}(ν) − M ≥ |Σ_ν νp_{W_m}(ν)| − M`,

which is unbounded in `m` by (a): `sup_m Σ_{|ν|>M}(1+|ν|)p_{W_m} = ∞` for
every `M` — *(claim (b))*.  Finally, D27 defines the ordered wall
expectation as `δx = lim_m[ω^+_{W_m}(𝔛_{W_m}) − ω^-_{W_m}(𝔛_{W_m})]`
along an (LR3) subsequence; by (a) these differences diverge linearly at
rate `≥ θ` per window site and (LR3) supplies no subsequence, so `δx` is
undefined along the exhaustion — *(claim (c))*.  The contrapositive
reading is the surviving positive statement: **on any (LR) state the mean
wall transport is `o(|W_m|)`.**  **QED (a)--(c).**  □

**⟨2⟩5. (REMARK — mean escape gives (M-ESC) with `θ = p_tr`; means only.)**
Suppose (informally, "mean escape"): in the incoming Cesàro states the
window lies entirely in one tail in the mean — say the kink is to the LEFT,
so every `x ∈ W_m` has `ω^-_{W_m}(S^z_x) = −s + o(1)` (window in the `β`
tail) uniformly on all but `o(|W_m|)` sites — while in the outgoing Cesàro
states the kink has transited to the right of `W_m` with weight `p_tr` and
stayed left with weight `1−p_tr`.  Then by D13(a)'s definition
`𝔛_W = a−1+(1/2s)Σ_{x∈W}(S^z_x+s)`:

`ω^-_{W_m}(𝔛_{W_m}) = a_m−1 + o(|W_m|)`,
`ω^+_{W_m}(𝔛_{W_m}) = p_tr\,(a_m−1+|W_m|) + (1−p_tr)(a_m−1) + o(|W_m|)
 = a_m−1 + p_tr|W_m| + o(|W_m|)`,

so `θ = p_tr`.  Only the MEAN tail densities of H-MQG(2)/D13(a) enter —
no variance statement, hence no `(E-TAIL)`; no channel projections, wave
operators, sign-definite velocity classes, or incoming-concentration step.
This is verdict M2's strengthening adopted verbatim.  Named computation
**LD-ESC-MEAN**.

**⟨2⟩6. (REMARK — the dichotomy, the evidence, and the `tns-xf4` fence.)**
(i) *Dichotomy.*  ⟨1⟩4 and ⟨1⟩5 partition the reach of the unsubtracted
window charge: on confined-kink sharp-tail states ((K-TAIL)+(K-Q);
`θ = 0`) the ε-version holds and is compatible with D27(LR); on
mean-transiting states (`θ > 0`) D27(LR3) fails and no ordered outcome
measure exists.  A `{0,2}`-type ledger for the UNSUBTRACTED charge can
therefore live only on the confined side; on transiting classes it
requires a subtracted or co-moving observable (the D13(c) trap paragraph's
leg subtraction — a definition-level move, proposed for adjudication in
r1 and still open, not made here).  (ii) *Evidence for the mechanism.*
The two-atom law `||F_ret||²δ_0 + ||F_tr||²δ_{−2s|W|}` with LR3 tail
`(1+2s|W|)||F_tr||²` — r1's obstruction shape — is real as a MECHANISM:
the r1 critic reproduced it to four digits on a scattering model
(verdict §0: weights `0.5567/0.4433`, incoming-concentration defect
`2.4e-09`, tail `(1+513)(0.4433) = 227.86` vs measured `227.867`), and
checker gate LD-C5 re-certifies it here on a barrier model together with
the ⟨2⟩2 identity itself.  It is recorded as evidence for ⟨2⟩5's
`θ = p_tr` arithmetic, NOT re-claimed as a theorem: the r1 proposition
that asserted it had an empty hypothesis class (F1).  (iii) *Fence.*
D16 is in the complement of (M-ESC): its kink band is exactly flat
(ground energy `0` in every `S^z` sector — verdict F1(b)(iii), checker
LD-C7), so `θ = 0` there and NOTHING in this shard bears on the
(LR)-for-D16 lane bd `tns-xf4`.  What ⟨1⟩5 does transmit to that lane is
a hint, not a constraint: LR3 for D16 hinges on kink confinement (band
flatness), not on magnon dynamics.

**⟨2⟩7. QED (⟨1⟩5).**  □

---

## 4. HONEST STATUS

**Proved, given only its own ASSUME block (unconditional as an
implication):**

- **ACE-LD-abs** (⟨1⟩1--⟨1⟩2) and **ACE-LD-nec** (⟨1⟩3).  Verified by the
  r1 critic (verdict §5, items 1--2) and unchanged in r2 except the m3
  lockstep fix and the LD-GAP-SET addition ⟨1⟩1.⟨2⟩5 (a two-line parallel
  of the verified ⟨2⟩1--⟨2⟩2, consumed only by ACE-LD-ε-x).
- **ACE-LD-obst′** (⟨1⟩5): D27(LR3) fails whenever the mean tail transport
  is a positive fraction of the window.  Inputs: MI ⟨1⟩5 and MI
  ⟨1⟩7.⟨2⟩1--⟨2⟩2 (both inside the PROVED M-INDEX-fin/M-INDEX-spec
  perimeter), D27(LR1)--(LR2), and (M-ESC).  No channel structure, no
  variance hypothesis, no D28.  This is verdict M2's statement, adopted.

**Proved conditionally (each hypothesis named, none hidden):**

- **ACE-LD-ε / ACE-LD-ε-t / ACE-LD-ε-x** (⟨1⟩4): conditional on
  **(K-TAIL)** and **(K-Q)** (with `t`-uniform data for the family form).
  The hypothesis class is inhabited (D16 static-kink sector states —
  ⟨2⟩9(c)), unlike r1's `(E-TAIL) ∧ (V-ch)`.

**Hypothesised / not proved:**

- (K-TAIL) for the infinite-volume D16 kink sector: supported by
  finite-chain ED at `L ≤ 12` (⟨2⟩9(c), LD-C7) with the measured rate
  equal to the model's `λ̃ = q = Δ−√(Δ²−1)` to three digits; an
  infinite-volume proof (e.g. from D1(c)'s transfer gap on the sector
  MPS) is the natural next target and is NOT claimed here.
- (K-Q) for all `t`: propagated from `t=0` by conservation WHERE a
  commuting relative-charge operator exists (⟨1⟩4.⟨2⟩4); exact in the D16
  sector realization; not constructed abstractly (and unconditionally it
  CANNOT be — M-INDEX-LA-strong).
- (M-ESC) on any concrete model/state: the barrier-model certificate
  LD-C5 exhibits the mechanism (including the ⟨1⟩5.⟨2⟩2 identity) on a
  one-particle model; whether a D28-class kink--magnon state realises
  `θ > 0` is a model question this shard does not answer.  *(r1's claim
  that D28 packets force ballistic kinks was FALSE — F1(b)(iv) — and is
  withdrawn; D28's class contains `θ = 0` members, D16 among them.)*

**Refuted / withdrawn (r2):**

- r1's ACE-LD-esc, COROLLARY ACE-LD, ACE-LD-obst as stated: hypothesis
  class `(E-TAIL) ∧ (V-ch)` EMPTY on every instantiated model (F1);
  withdrawn, not repaired.  The exact fixed-window (AD3-ex) additionally
  has a counterexample in D16: strictly positive defect at every finite
  `W`, decaying as `λ̃^{d_W}` (⟨1⟩4.⟨2⟩8, LD-C7) — so the `AD3-ex` row's
  exact form is false at fixed `W` on the one instantiated model of its
  intended class, and only the ε-version survives.

**Merely evidence:**

- The numerical certificates (§5, `theory/checks/ace_ld_check.py`):
  LD-C1--C4 instantiate ACE-LD-abs/-nec surfaces on a free two-channel
  lattice model; LD-C5 exhibits the obstruction mechanism and the
  first-moment identity on a barrier scattering model; LD-C6 certifies the
  static contrast (`p_W = δ_0`, bounded LR3 tail); LD-C7 certifies the
  D16 flat band, the strictly positive fixed-`W` defect, its `λ̃^{d_W}`
  decay rate, and the coset location, by exact diagonalisation.  All on
  those models only.

**Honest defects and L2 self-report.**  (i) This shard is ~1030 lines
against the 200--500 band; the r1 critic's m7 split proposal (obstruction
into its own shard) is endorsed but outside this lane's writable set — a
MERGE PROPOSAL requests the split.  (ii) (K-TAIL) is a hypothesis ABOUT
the channel family `{φ_t}`; its reduction to initial data + dynamics
(confinement) is supplied only in the D16 instance via band flatness, not
abstractly.  (iii) The `o(|W_m|)` in (M-ESC)/⟨2⟩5 is not quantified; any
downstream use wanting rates must sharpen it.  (iv) ⟨2⟩9(b)'s weak-\*
tail-relaxation argument is stated at remark level (it scopes, it is not
load-bearing for any claim).

## 5. CHECKER SPEC — `theory/checks/ace_ld_check.py` (r2 rebuild)

Deterministic; no randomness; no bare `assert` (every violation raises
`CheckFailure`, active under `python3 -O`).  Green exits 0; `--red` exits 1
iff every registered mutation reproduces exactly its registered pattern,
else 2; a green gate failure exits 3.  Rebuilt after verdict M3/M6 against
every bullet of the critic protocol's standing checker obligations; in
particular **red runs print the exit PATH** (the gate that fired, with its
message) per mode, and **every gate — including each internal sub-gate that
carries evidence — has a registered red mode that reaches it** (map below).

**Three model batteries** (constants in the code header; spec and code in
lockstep — verdict m4):

- **FREE** (gates LD-C1--C4; the ACE-LD-abs/-nec surface): one particle on
  `ℤ_N`, `N = 8192`, `H` = nearest-neighbour hopping (dispersion `2cos k`,
  FFT propagation), window `W = [N/2−16, N/2+16]`, D13(a) clamp charge
  `Q̂|x⟩ = clamp_W(x)|x⟩`, `spec = {0,…,|W|} ⊂ ℤ`; channels = momentum-sign
  projections; state = two counter-propagating bump packets centred at
  `k = ∓π/2` (NO detune — r1's phantom detune removed), weights `0.8/0.6`
  normalised; time grid `t = 4,…,1024` dyadic; ring-cut guard `< 1e-16`.
- **BARRIER** (gates LD-C5, LD-C6; the ACE-LD-obst′ mechanism and its
  static contrast): one particle on `ℤ_N`, `N = 2048`, `H` = hopping plus a
  one-site barrier `V_0 = 1.2` at the centre, dense `eigh` propagation;
  incoming bump packet prepared 300 sites LEFT of the barrier moving right;
  protocol times `t_- = 0`, `t_+ = 300`; windows `|W| = 17, 33, 65, 129`
  centred on the barrier.  LD-C6 uses the position-diagonal (`flat`)
  variant with the packet inside `W`.
- **D16** (gate LD-C7; the ε-version's measured decay — the work-order
  gate): exact diagonalisation of the D16 XXZ kink chain, `Δ = 2.5`,
  `J = 1`, `L = 12`, open, WITH the telescoping boundary field
  `(J/2)√(Δ²−1)(S^z_1 − S^z_L)`; all 13 `S^z` sectors; ground state of the
  half-filled sector; `c_0 = 5`; windows `[4,7],[3,8],[2,9],[1,10]`
  (paddings `d_W = 1,2,3,4` about the 4-site core window).

**Green certificates** (measured green values quoted from the shipped run):

- `LD-C1` (hypothesis audit): spectral separation `≥ 1` FIRST, then single
  coset of `ℤ` (max fractional spread `< 1e-12`), `[P_±,H] = 0`,
  `P_+P_- = 0`, `(P_++P_-)Ψ = Ψ`, all to `1e-9`.
- `LD-C2` (first-moment escape): `ε_±(t)` decreasing to `< 1e-6`
  (measured final: `7.2e-12`, `3.3e-12`).
- `LD-C3` (the inequality (LD.1) at the ASSERTED constant): at EVERY grid
  time, `||E({q_±})Ψ_t − P_±Ψ_t|| ≤ Σ_{ch} d_{ch}^{-1}ε_{ch}(t) + slack`,
  with `d_{ch}^{-1} = 1` **asserted per ⟨1⟩1.⟨2⟩3 — NOT computed from the
  model spectrum** (verdict M6: computing it would defeat `--red-gap`).
  The informative statistic `max_t max_{ch} lhs/rhs` is reported
  (measured green: `0.168`) and gated below by a green-only liveness floor
  `0.10` (catches a silently dead lhs).  **Honesty clause (M6): this gate
  does NOT certify sharpness of the constant** — constants down to ~6×
  smaller would also pass on this model; what it certifies is that the
  inequality holds at the asserted constant and that a 10×-optimistic
  constant is DETECTED (`--red-gap` fails it at `t=8`,
  `lhs 4.12e-01 > rhs 3.72e-01`).  r1's "it tests the CONSTANT" claim is
  deleted.
- `LD-C4` (diagonality at `t = 1024`): `||E({q_±})Ψ_t − P_±Ψ_t|| < 1e-6`.
  Near-subsumption disclosure: with C2's `ε < 1e-6`, C3 already implies
  `lhs ≲ 2e-6`; C4's independent value is testing the (AD3-ex)-form norm
  directly, and it is the surface `--red-merged`/`--red-dup` break.
- `LD-C5` (obstruction mechanism, rebuilt per M3 on a genuine scattering
  configuration): (a) incoming concentration
  `||(1−E({0}))Ψ_{t_-}|| < 1e-4` at every window (measured `≤ 3.2e-6`);
  (b) the TPM law is EXACTLY two atoms `{ν=0, ν=−|W|}` — **including the
  `ν = 0` atom r1's certificate never produced** — with off-atom mass
  `< 1e-4`; (c) atom weights equal the independently measured
  `|r|² = 0.2704`, `|t|² = 0.7296` (mass left/right of the barrier at
  `t_+`) within `1e-3`; (d) the MI ⟨1⟩7.⟨2⟩2 first-moment identity
  `Σ_ν ν p_W = ⟨Q̂⟩_{t_-} − ⟨Q̂⟩_{t_+}` holds within `1e-4` (measured
  agreement `1e-4`-exact at all four windows: e.g. `−12.4024` vs
  `−12.4024` at `|W|=17`) — this is ⟨1⟩5.⟨2⟩2's mechanism certified
  directly, with the ground truth measured from the STATE, not from the
  law; (e) the LR3 tail moment `Σ_{|ν|>10}(1+|ν|)p_W` grows across windows
  with floor `0.9(1+|W|)|t|²` at the largest (measured
  `13.13 → 24.80 → 48.15 → 94.84`, floor `85.4`).  The `ν` convention is
  the frozen `ν = q_- − q_+` (MI ⟨1⟩5.⟨2⟩3).
- `LD-C6` (static contrast — verdict M3's fix demand): on the
  position-diagonal model, `p_W = δ_0` EXACTLY (`p_0 > 1−1e-9`) and the
  LR3 tail is `0 < 1e-9`, at every window: the confined side of ⟨1⟩5.⟨2⟩6's
  dichotomy.
- `LD-C7` (the ε-version's measured decay — the work-order gate): (a) the
  kink band is flat: `|E_0| < 1e-10` in EVERY `S^z` sector (measured max
  `8.2e-17`) — the F1 flatness input and the `tns-xf4` fence (`θ = 0`);
  (b) `min_q||(Q̂_W−q)Ψ|| > 1e-6` at every window — **exact (AD3-ex) is
  false at fixed `W` in D16** (measured defects `4.45e-02, 9.30e-03,
  1.94e-03, 4.05e-04`); (c) successive defect ratios equal the claimed
  rate `q = 0.208712` within 2% (measured `0.2089, 0.2087, 0.2083`) —
  the `λ̃^{d_W}` law of (LD.4); (d) `⟨Q̂_W⟩` within `1e-2` of the integer
  coset (M-INDEX-fin arithmetic; measured worst `2.0e-3`).

**Red modes** (thirteen; each a FRESH model variant, never in-place; a
surviving target or an unregistered casualty exits 2).  Gate-reachability
map — every sub-gate that carries evidence, with the mode that reaches it:

| mode | battery | must break (exit path) | must pass |
|---|---|---|---|
| `--red-gap` | FREE | LD-C1 (**gap** sub-gate: `separation 0.1 < 1`), LD-C3 (constant: fails `t=8`) | LD-C2, LD-C4 |
| `--red-coset` | FREE | LD-C1 (**coset** sub-gate: spread `0.414`) | LD-C2, **LD-C3**, LD-C4 |
| `--red-halfspace` | FREE | LD-C1 (**commutation** sub-gate: `[P,H] = 0.53`) | LD-C2, LD-C3, LD-C4 |
| `--red-merged` | FREE | LD-C2 (escape), LD-C4 (diagonality `0.80`) | LD-C1, LD-C3 |
| `--red-dup` | FREE | LD-C2, LD-C4 (diagonality `1.00`) | LD-C1, LD-C3 |
| `--red-c5-nobarrier` | BARRIER | LD-C5 (**atom** gate: `p_0 = 0`) | — |
| `--red-c5-meanshift` | BARRIER | LD-C5 (**identity** gate, DATA mutation: ground truth shifted `+1`) | — |
| `--red-c5-inwindow` | BARRIER | LD-C5 (**incoming-concentration** gate: defect `1.0`) | — |
| `--red-c6-moving` | BARRIER | LD-C6 (`p_0 = 0.27 ≠ 1`) | — |
| `--red-c7-delta` | D16 | LD-C7 (**rate** gate, DATA mutation: `Δ=3.0` ratios `0.1717` vs kept claim `0.2087`) | — |
| `--red-c7-mixed` | D16 | LD-C7 (**coset** gate: `⟨Q̂_W⟩ = −0.499`; (K-Q) broken by a two-sector mixture) | — |
| `--red-c7-product` | D16 | LD-C7 (**defect-positivity** gate: defect `0` — no kink, exact eigenvector, certificate refuses) | — |
| `--red-c7-noboundary` | D16 | LD-C7 (**flat-band** gate: max `|E_0| = 1.146`) | — |

Design notes against the standing obligations.  (i) *Distinct red modes
are distinct in effect:* `--red-coset` shifts ONE edge eigenvalue by
`√2−1` keeping the gap `≥ 1` — it breaks the coset and **LD-C3 survives,
correctly**, since (LD.3) consumes only the gap; `--red-gap` is the
constant shrink.  r1's `--red-coset` (bit-identical to a constant shrink —
verdict M6) is gone.  (ii) *Data mutations:* `--red-c5-meanshift` and
`--red-c7-delta` falsify the ground truth the acceptance gates compare
against, not checker constants.  (iii) *No structurally dead gates:*
`--red-halfspace` arms the `[P,H]` gate (r1 m1); the two "different"
expressions in C5(d) are `Σνp` (from the law) and `⟨Q̂⟩_{t_-}−⟨Q̂⟩_{t_+}`
(from the state) — independent computations, and the meanshift mutation
proves the comparison live.  (iv) *Subsumption:* C4's near-subsumption by
C2∧C3 is disclosed in its gate docstring and above; C5's weight gates (c)
are cross-checked rather than independent of the atom gates (b) plus
unit total mass — disclosed here; no other gate pair is deductively
linked.  (v) The C3 ratio floor is green-only (a liveness gate; on
mutants it is meaningless and is skipped so registered patterns stay
exact).

---

## 6. MERGE PROPOSALS (exact replacement text; orchestrator merges after
the critic converges — nothing below is live)

**MP-1. New rows for `claims/CLAIMS.md`** (append after the AD3-ex row).
Each row states its hypotheses in full, its conclusion as a conditional
implication, and closes with a not-claimed enumeration (the adjudicated
register of the M-INDEX-fin/M-INDEX-spec/AC-EX rows; verdict §6):

| id | statement (short) | status | depends on | proved in | tested in |
|---|---|---|---|---|---|
| ACE-LD-abs | Given (A1)--(A5) — unitary group, bounded self-adjoint `Q̂` with finite one-coset spectrum, mutually orthogonal dynamics-commuting channel projections resolving the vector, first-moment escape `\|\|(Q̂-q_ch)P_chΨ_t\|\|→0`, pairwise distinct channel charges — spectral diagonality holds: `\|\|E({q_ch})Ψ_t-P_chΨ_t\|\| ≤ Σ_{ch'}d_{ch'}^{-1}ε_{ch'}(t) → 0` with `t`-uniform constant (`≤ n` for coset charges); `N` channels, general on-site spin.  Distinct charges are NECESSARY (ACE-LD-nec): shared charge + two nonvanishing weights refutes the display for every claimed eigenvalue.  NOT claimed: any statement about a concrete model, any instantiation of (A4), or sharpness of the constant beyond the single spectral gap | PROVED (pending L6 loop) | — | theory/ace-ld.md ⟨1⟩1--⟨1⟩3 | theory/checks/ace_ld_check.py LD-C1--C4 (green exit 0; `--red` exit 1, 13 modes, exit paths logged) |
| ACE-LD-eps | Under H-MQG(1)--(2) and the two named hypotheses (K-TAIL) (confined-core exponential tail clustering, rate `λ̃`, core `K`) and (K-Q) (sharp relative charge `q_φ`, defect `ε_Q`): at every finite window `W ⊇ K` with `c_0∈W`, `\|\|(Q̂_{W,c_0}−q_φ)φ\|\| ≤ ε_Q + 2C_Kλ̃^{d_W}/(1−λ̃)` (LD.4), `d_W` the D13(a) core-to-edge padding; with `t`-uniform data this gives (AD3-ex-ε): `limsup_t\|\|(Q̂_{W,c_0}−q_ch)P_chΨ_t\|\| ≤ Cλ̃^{d_W}` at fixed `W`, `→0` in the D18(AD4) order, plus ordered-limit inter-channel cross-term vanishing at rate `O(λ̃^{d_W})` (ACE-LD-ε-x) — the input AS ⟨1⟩7.⟨2⟩2 consumes.  Compatible with D27(LR3).  Hypothesis class inhabited: D16 static-kink sector states ((K-Q) exact by sector membership; (K-TAIL) at rate `q=Δ−√(Δ²−1)` certified by ED at `L=12`, ratios `0.2089/0.2087/0.2083` vs `q=0.208712`).  NOT claimed: the exact fixed-`W` (AD3-ex) (FALSE in D16 at every fixed `W` — defect strictly positive, decaying as `λ̃^{d_W}`); D18(AD3)'s weak-\* kink-eigenstate convergence or M-INDEX-spec's reduction clause; anything on transiting classes; an infinite-volume PROOF of (K-TAIL)/(K-Q) on any model; any vacuum-eigenstate statement | PROVED (conditional; pending L6 loop) | D13, D26, D27, M-INDEX-fin | theory/ace-ld.md ⟨1⟩4 | theory/checks/ace_ld_check.py LD-C7 (+ LD-C6 static contrast) |
| ACE-LD-obst-prime | Under H-MQG(1)--(3), D26(INT), the D27 setting, D27(LR1)--(LR2), and (M-ESC) (mean tail transport `θ>0` per window site): the TPM first moments diverge linearly, `\|Σ_ννp_{W_m}\| ≥ 2sθ\|W_m\|(1−o(1))`, so D27(LR3) FAILS along every padded exhaustion and D27's `δx` is undefined there.  Contrapositive: (LR3) forces mean wall transport `o(\|W_m\|)`.  Mechanism (mean escape ⟹ `θ = p_tr`) uses only the mean tail densities — no variance hypothesis, no channel structure, no D28.  NOT claimed: any statement about D16 or any confined-kink class (`θ=0` there — the bd `tns-xf4` lane is NOT pre-empted); any statement about D28's packet class as such (D28(4) does not force transit); mass-defectiveness of weak limits (first-moment divergence only); the two-atom law as a theorem (numerically exhibited only, LD-C5) | PROVED (conditional; pending L6 loop) | D13, D17, D26, D27, M-INDEX-fin | theory/ace-ld.md ⟨1⟩5 | theory/checks/ace_ld_check.py LD-C5 (incl. the MI ⟨1⟩7.⟨2⟩2 identity gate), LD-C6 |

*(Register/deps notes: row 1 carries NO depends-on — ACE-LD-abs is
unconditional given its ASSUME, per verdict m5; M-INDEX-fin enters only
the instance rows.  M-INDEX-spec is on no row — nothing here consumes it,
per m5.  Statuses are bare L5 values; every qualifier lives in prose, per
M4.)*

**MP-2. Prose append to the `AD3-ex` row** (status stays **CONJECTURE** —
verdict M4; append to the statement column):

> r2 update (theory/ace-ld.md): the exact display is FALSE at every fixed
> `W` in the D16 instantiation — `min_q||(Q̂_W−q)Ψ|| > 0` on the sector
> zero modes, decaying exactly as `λ̃^{d_W}` (`λ̃ = q = 0.2087` at
> `Δ=2.5`; ace-ld r1 verdict §8 and checker LD-C7) — so only its
> ε-version can hold at fixed windows.  That ε-version, (AD3-ex-ε), is
> PROVED conditionally (row ACE-LD-eps) and suffices for AS ⟨1⟩7.⟨2⟩2's
> cross-term step in the ordered limit.  On classes with mean transit
> `θ>0` the companion hypothesis D27(LR) fails (row ACE-LD-obst-prime).
> r1's proposed discharge under (E-TAIL)∧(V-ch) is withdrawn: that
> conjunction is empty on every instantiated model (ace-ld-r1 F1).

**MP-3. Gloss replacement in AS ⟨1⟩7's ASSUME block** (replacing the
sentence "The missing derivation is recorded as named lemma ACE-LD (see
HONEST STATUS): …" up to "…no step of this shard supplies."):

> The named lemma **ACE-LD** (theory/ace-ld.md, r2) prices this
> hypothesis as follows.  (i) The exact display is FALSE at fixed `W` in
> D16 (strictly positive defect, decaying as `λ̃^{d_W}`); it survives
> only as the ε-version (AD3-ex-ε), PROVED under the named hypotheses
> (K-TAIL)+(K-Q) (confined kink, sharp relative charge — the D16
> static-kink class).  (ii) In the ordered limit that ⟨2⟩2 actually
> operates in (fixed-window time limit first, `W↑ℤ` last), (AD3-ex-ε)
> supplies the cross-term vanishing `|⟨Ψ_t,P_LE_W(S_T)Ψ_t⟩| = O(λ̃^{d_W})`
> with coset-ball projections in place of the singletons; the fixed-`W`
> exact form is not available and not needed.  (iii) What is supplied is
> the KINK-eigenstate reading of D18(AD3) in ε-approximate norm form; the
> weak-\* reading consumed by M-INDEX-spec's reduction clause is NOT
> supplied and that row's adjudicated scoping is untouched.  (iv) On
> packet classes whose kink transits with mean weight `θ>0`, D27(LR3) —
> hence the T1 outcome-measure hypothesis of ACE.3 — fails
> (ACE-LD-obst-prime); D28(4) itself does NOT force transit (it
> constrains only `v_M−v_K`), and D16 lies in the confined complement.
> *(Also flagged: ⟨2⟩1's `ν = q_T − q_in` orientation is opposite to the
> frozen `ν = q_- − q_+` of notation.md/MI ⟨1⟩5.⟨2⟩3; only `|ν|` is
> consumed downstream, but the display should be reconciled — ace-ld-r1
> NOTE n1.)*

**MP-4. `notation.md` additions** (collision-checked against the frozen
table — no reuse of `q`, `σ`, `ρ`; verdict m6):

| `𝒬_{c_0}φ` | relative-charge limit vector `lim_n Q̂_{W_n,c_0}φ` — exists on every (K-TAIL) state (a vector, not a sector operator; M-INDEX-LA-strong untouched) | theory/ace-ld.md ⟨1⟩4.⟨2⟩2 |
| `(K-TAIL)`, `(K-Q)` | confined-core exponential tail clustering (core `K`, rate `λ̃`); sharp relative charge (`\|\|𝒬_{c_0}φ−q_φφ\|\|≤ε_Q`) | theory/ace-ld.md §0 |
| `(M-ESC)`, `θ` | mean-tail-transport hypothesis `liminf_m \|ω^+−ω^-\|(𝔛_{W_m})/\|W_m\| = θ > 0` | theory/ace-ld.md §0, ⟨1⟩5 |

**MP-5. L2 split (endorsing verdict m7, outside this lane).**  Move §3
(⟨1⟩5, ACE-LD-obst′) to a shard `theory/ace-ld-obst.md` once the loop
converges; it has a disjoint hypothesis set from ⟨1⟩4 and the split
restores both files to the L2 band.

**MP-6. Note to bd `tns-xf4` (transmit as a hint, not a constraint).**
ACE-LD-obst′ is scoped to `θ > 0`; D16's exactly flat kink band
(re-certified LD-C7 across all 13 sectors) puts it at `θ = 0`, outside the
obstruction's class.  Usable hint: (LR3) for D16 hinges on kink
confinement (band flatness), not on magnon dynamics; and (K-TAIL)+(K-Q)
give the fixed-window ε-eigenvector structure (LD.4) that an (LR) proof
can consume.
