<!-- ROLE: proposer shard for the named lemma ACE-LD, round 4.
     r1 verdict: theory/verdicts/ace-ld-r1.md FAIL(F1,M1-M6).  r2 verdict:
     theory/verdicts/ace-ld-r2.md FAIL(F1,M1-M6).  r3 verdict:
     theory/verdicts/ace-ld-r3.md FAIL(F1,M1-M3) — and three promotions
     approved on cells (A)-(D) subject to the section 8(E) preconditions.
     Work order: briefs/ace-ld-repair-r4.md.
     r4 changes: THEOREM ACE-LD-chi is RETIRED and restated as THEOREM
     ACE-LD-sharp per r3 F1 — (K-TAIL) forces SHARP ON-SITE CHARGE of the
     tail vacua, not chi=1 product vacua; the two coincide only when the
     tail density is a SIMPLE eigenvalue of S^z, which H-MQG/D2(a)/D26
     refuse to impose, and the unqualified chi=1 form is REFUTED by the
     critic's C^2 (x) C^3 counterexample.  MP-3(ii)'s LD-MONO sentence
     takes the "beyond the outer window" quantifier back (r3 M1).  LD-C5b
     is re-anchored at the genuine D27(LR2) double-Cesaro average and the
     LR2-failure finding republished at the corrected number (r3 M2).
     The reachability disclosure is completed and C6_MOM_BOUND is keyed
     to a recorded t_+ sweep (r3 M3).  MP-1 carries the four verdict
     cells verbatim; MP-4 is string-anchored (section 8(E) precondition 2).
     Objection dispositions: theory/ace-ld-r4-response.md (prior rounds:
     theory/ace-ld-r3-response.md, theory/ace-ld-r2-response.md).
     Lane: this file, theory/ace-ld-r4-response.md, and
     theory/checks/ace_ld_check.py only.  All text destined for shared files
     is in section MERGE PROPOSALS below.
     Status: proposer draft, r4.  A critic pass is pending; nothing here
     upgrades any CLAIMS.md row until the L6 loop converges. -->

# ACE-LD r4 — window-charge spectral collapse, the ε-version on the confined-charge corner, and the first-moment obstruction

**Proposer status (r4).**  Five results, stated with their exact quantifiers
in §0:

1. **ACE-LD-abs** (abstract; N channels; general on-site spin) — unchanged
   from r1, VERIFIED by the r1 critic (verdict §5 item 1): first-moment
   channel escape plus distinct channel charges implies window-charge
   spectral diagonality with a `t`-uniform constant.
2. **ACE-LD-nec** (necessity) — unchanged modulo the m3 lockstep fix:
   distinct charges are necessary.
3. **ACE-LD-ε** (the main positive content, now correctly scoped): under
   two named hypotheses — confined-core exponential tail clustering
   **(K-TAIL)** and sharp relative charge **(K-Q)** — the **ε-version** of
   (AD3-ex) holds:

   > **(AD3-ex-ε).**  `limsup_{t→+∞} ||(Q̂_{W,c_0} − q_ch)P_chΨ_t|| ≤
   > C λ̃^{d_W}` at each fixed window `W`, with `d_W` the core-to-edge
   > padding of D13(a); hence `→ 0` as `W↑ℤ` in the D18(AD4) order.

   This is D13(a)'s own tail-bound clause elevated to a theorem, and its
   hypothesis class is **inhabited**: D16's static-kink sector states
   satisfy both hypotheses, verified two ways — the fixed-`W` defect
   decays at exactly `λ̃^{d_W}` (`λ̃ = q = 0.208712`; checker gate LD-C7),
   and (K-TAIL) itself holds at rate exactly `q` per site (r2 verdict
   §0(iii), now certified directly by LD-C7(e)).  **What the theorem is
   about (r3, verdict F1):** `𝒬_{c_0} = 2s(X_1 − c_0)` is D13(c)'s exactly
   conserved charge, so (K-TAIL) is precisely the hypothesis *no charge
   has escaped the core*.  The ε-version is a theorem about the
   **confined-charge (leg-free) corner** — and it is therefore **jointly
   unsatisfiable with D18(AD3)'s escaping-leg clause**.  The r2 claim
   that (AD3-ex-ε) supplies what `ansatz-scattering.md` ⟨1⟩7.⟨2⟩2
   consumes is **RETRACTED** (see the r3 retraction notice below and
   ⟨1⟩4.⟨2⟩7): the consumer needs the opposite regime.
4. **ACE-LD-sharp** (r4; replaces r3's THEOREM ACE-LD-χ per verdict
   ace-ld-r3 F1): (K-TAIL) plus membership in the D9 kink class *forces*
   both tail vacua to have **sharp on-site charge** — zero on-site charge
   variance, `ω_γ((S^z_x − s_γ)²) = 0`, equivalently
   `ω_γ(Π_x^{(s_γ)}) = 1`, at every site — hence `±s ∈ spec S^z`.  The
   scope boundary is a theorem, not a hedge: it excludes every vacuum
   with nonzero on-site charge variance (generic injective-MPS vacua in
   particular), and it excludes (for example) spin-1 at `s = 1/2` by
   arithmetic alone.  **The r3 form ACE-LD-χ, which concluded `χ=1`
   `S^z`-product tail vacua, is RETIRED: its `χ=1` clause is REFUTED
   under H-MQG(1)--(2) alone** (the critic's `ℂ²⊗ℂ³` counterexample —
   sharp wall over an AKLT spectator factor, injective `χ=2` vacua,
   `D_xφ ≡ 0`; recorded at ⟨1⟩4.⟨2⟩9(b) and in HONEST STATUS).  The
   `χ=1` product form needs `s_γ` to be a **simple** eigenvalue of
   `S^z` — true in the standard spin-`S` register `d = 2s+1` and in D16,
   but explicitly fenced as NOT a constraint by the corpus
   (`notation.md` `ρ`-row fence; `definitions.md` D26 preamble).
5. **ACE-LD-obst′** (the obstruction, restated at minimal strength per
   r1 verdict M2, closing statement strengthened per r2 verdict M2):
   D27(LR3) fails on every class with nonvanishing mean tail transport,
   from D27's own first-moment identity alone — no `(E-TAIL)`, no
   `(V-ch)`, no `(V-in)`, no `σ_L ≠ σ_T`, no channel structure at all.
   On any (LR) state the mean wall transport is uniformly **O(1)**
   (⟨1⟩5.⟨2⟩3), not merely `o(|W_m|)`.

**DELETED in r2 (verdict F1 — do not restore).**  r1's PROPOSITION
ACE-LD-esc, COROLLARY ACE-LD, and PROPOSITION ACE-LD-obst as previously
stated are withdrawn, together with their hypotheses `(E-TAIL)`, `(V-ch)`,
`(V-in)`.  Reason: `(E-TAIL)` is *equivalent* to vacua of **sharp on-site
charge** (REMARK ⟨1⟩4.⟨2⟩9 below; *r4 correction, verdict ace-ld-r3 F1:
the r1--r3 reading "equivalent to `χ=1` `S^z`-product vacua" holds only
when `s_γ` is a simple eigenvalue of `S^z` — true on every model
instantiated in this corpus, D16 included, so the emptiness argument
below is unaffected*), which pins the instantiated class to D16 — and
D16's kink band
is **exactly flat** (`v_K ≡ 0`, ground energy `0` in every `S^z` sector;
verdict F1(b)(iii), re-certified by LD-C7), so `(V-ch)` fails there:
`(E-TAIL) ∧ (V-ch)` is empty on every instantiated model.  Also withdrawn
as FALSE: the r1 sentence "on the fixed-packet class of D28 the kink is
ballistic" — D28(4) constrains only the *relative* velocity `v_M − v_K`, so
D28's class contains the static-kink class and D16 realises it (verdict
F1(b)(iv)).  *(r3 register note on this historical notice: "exactly
flat" as a model statement is K1+K2 plus the K4 CONJECTURE — see
⟨1⟩5.⟨2⟩6(iii) for the corrected form; the emptiness argument needs only
the existence of the exactly stationary K1--K2 states, which is PROVED.)*  Their correct proof steps that the r1 critic verified
(LD-STRADDLE, LD-CONE, LD-IN, LD-TPM, and the r1 obstruction's conclusion
*on its own hypotheses*) are recorded in the r1 file history and the
verdict; none is re-claimed here on an empty class, and no repaired
hypothesis pair replaces them.

**RETRACTED in r3 (verdict ace-ld-r2 F1 — do not restore).**  The r2
sentence "it is what `ansatz-scattering.md` ⟨1⟩7.⟨2⟩2 consumes in the
ordered limit", the whole of the r2 step ⟨1⟩4.⟨2⟩7 that argued it, the
"Compatible with D27(LR3)" clauses, and MERGE PROPOSAL MP-3(ii) (which
would have written the claim into `theory/ansatz-scattering.md`) are
**withdrawn as FALSE**.  Reason (the r2 critic's identification, adopted):
`𝒬_{c_0} := lim_n Q̂_{W_n,c_0}` satisfies, exactly,
`Q̂_{W,c_0} = Σ_{x∈W}(S^z_x − s_{γ_{c_0}}(x))`, hence
`𝒬_{c_0} = 2s(X_1 − c_0)` — the exactly conserved regularised charge of
the frozen D13(c) trap paragraph.  Therefore **(K-TAIL) is the hypothesis
"no charge escaped the core" while D18(AD3) is the hypothesis "the leg
charge left the window": they are mutually exclusive** (proved at
⟨1⟩4.⟨2⟩7, THEOREM LD-ID).  On an escaping magnon the escaped tail sum
saturates at `2s`, and the minimal admissible `C_K` grows as `λ̃^{−vt}`
(r2 verdict F1(b)(ii)); charge conservation makes `q_L ≠ q_T` unavailable
within one D18 sector (r2 F1(b)(iii)); and even granting the hypotheses
with `ε_Q = 0`, (LD.4) plus conservation force the ordered wall
displacement **`δx = 0`** (r2 F1(b)(iv)).  The true relationship, stated
once and repeated at ⟨1⟩4.⟨2⟩7: **the ε-version is a theorem about states
whose charge has NOT escaped; the ordered-limit consumer AS ⟨1⟩7.⟨2⟩2
needs the opposite regime.**  What survives for the AS lane is only the
anchor-free window-monotonicity lemma LD-MONO (⟨1⟩4.⟨2⟩7), which is
compatible with an escaping leg.

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
> `||D_xφ||² ≤ C_K²λ̃^{2·dist(x,K)}`.  Conversely — r4, ace-ld-r3 n1,
> claimed — the on-site bound implies the full same-side clause: each
> `D_x` is self-adjoint, so
> `|ω_φ(D_xD_{x'})| = |⟨D_xφ, D_{x'}φ⟩| ≤ ||D_xφ||\,||D_{x'}φ||`.
> (K-TAIL) is therefore an ON-SITE TAIL-DECAY hypothesis, not a
> clustering hypothesis, and LD-C7(e)'s site-by-site profile certifies
> it IN FULL.)*

> **(K-Q) — sharp relative charge.**  There are `q_φ ∈ ℝ` and `ε_Q ≥ 0`
> with `||𝒬_{c_0}φ − q_φφ|| ≤ ε_Q`, where `𝒬_{c_0}φ :=
> lim_{n} Q̂_{W_n,c_0}φ` is the relative-charge limit vector, which EXISTS
> on every (K-TAIL) state and is exhaustion-independent (⟨1⟩4.⟨2⟩2 — a
> lemma, not a hypothesis; no sector-wide operator is constructed, so
> M-INDEX-LA-strong is not touched).  **Identification (r3, verdict F1
> and m3):** `𝒬_{c_0}` is the vector-valued lift of D13(c)'s exactly
> conserved first-moment wall coordinate: `𝒬_{c_0} = 2s(X_1 − c_0)`
> (THEOREM LD-ID, ⟨1⟩4.⟨2⟩7).  (K-Q) is therefore a sharpness hypothesis
> on the *conserved* charge, and (K-TAIL) is equivalent, up to the
> uniform bound of ⟨2⟩2(ii), to "no charge lies outside the core".

**ASSUME.**  H-MQG(1)--(2); a finite window `W = [a,b] ⊇ K` with cut
`c_0 ∈ W`; a unit vector `φ` satisfying (K-TAIL) and (K-Q); and
`d_W := dist(K, ℤ∖W) = min(ℓ−a, b−r) + 1 ≥ 1` (the D13(a) core-to-edge
padding).

**PROVE.**

  `||(Q̂_{W,c_0} − q_φ)φ|| ≤ ε_Q + \frac{2C_K}{1−λ̃}\,λ̃^{d_W}`.  **(LD.4)**

Consequently `dist(q_φ, spec π(Q̂_{W,c_0})) ≤` the same bound, so `q_φ`
lies within it of the M-INDEX-fin coset `κ_{W,c_0}+ℤ`.

**SCOPE (forced; THEOREM ACE-LD-sharp below; r4 restatement per verdict
ace-ld-r3 F1).**  (K-TAIL) entails tail vacua of **sharp on-site
charge** — `ω_γ((S^z_x − s_γ)²) = 0` at every site — hence
`±s ∈ spec S^z`; the theorem is claimed for that corner only.  Sharp
on-site charge excludes every vacuum with nonzero on-site charge
variance, in particular generic injective-MPS vacua: nothing about them
is claimed or available.  *(It does NOT entail `χ=1` product vacua: that
needs `s_γ` simple in `spec S^z`, and the unqualified `χ=1` form is
REFUTED — see ACE-LD-sharp.)*  Moreover, by LD-ID, no state carrying an
escaping leg of nonzero charge satisfies (K-TAIL) with `t`-independent
constants (⟨1⟩4.⟨2⟩7): the theorem's class and D18(AD3)'s escaping-leg
regime are disjoint.

### THEOREM ACE-LD-sharp (the forced boundary; r4 restatement of the retired ACE-LD-χ per verdict ace-ld-r3 F1)

**ASSUME.**  H-MQG(1)--(2); a unit vector `φ` whose state
`ω_φ ∈ 𝒦_{αβ}` (D9(a)) satisfies (K-TAIL) with core `K` and constants
`C_K, λ̃`.

**PROVE.**  Both tail vacua have **sharp on-site charge**: for
`γ ∈ {α, β}` and every site `x`, `ω_γ((S^z_x − s_γ)²) = 0`, equivalently
`ω_γ(Π_x^{(s_γ)}) = 1` where `Π_x^{(m)}` is the on-site spectral
projection of `S^z_x` at eigenvalue `m`.  Hence the tail density is an
on-site **eigenvalue**: `s_α = +s ∈ spec S^z` and
`s_β = −s ∈ spec S^z`.  In particular a spin-1 chain with calibration
`s = 1/2` admits **no** (K-TAIL) kink state — the exclusion is
arithmetic (`±1/2 ∉ {−1,0,1}`).  (Proof: ⟨1⟩4.⟨2⟩9(b).  The hypothesis
"tails relax to translation-invariant vacua" of the r2 remark is NOT
needed: D9(a) *supplies* the weak-\* relaxation.)

**NOT PROVED — the retired `χ=1` clause (r3 THEOREM ACE-LD-χ), REFUTED.**
The r3 statement concluded further that `ω_γ = ⊗_x|s_γ⟩⟨s_γ|`, a `χ=1`
`S^z`-product state.  That clause is **FALSE under H-MQG(1)--(2)
alone** (verdict ace-ld-r3 F1, adopted; the instruction to state it was
r2 M1(c), withdrawn by its own author): sharp on-site charge names a
unique on-site *vector* only if `dim ker(S^z − s_γ) = 1`, and no
hypothesis in force supplies simplicity — `notation.md`'s `ρ`-row and
`definitions.md`'s D26 preamble explicitly fence `d = 2s+1` as "the
fully polarised special case … NOT a constraint".  Counterexample
(critic-built, numerically verified in ace-ld-r3 F1(b)): on-site space
`ℂ² ⊗ ℂ³` with `S^z := σ^z/2 ⊗ 𝟙_3` (`spec S^z = {±1/2}`, each of
multiplicity 3; `e^{2πiS^z} = −𝟙`, so D26(INT) holds with `κ = 1/2`),
vacua `ω_α = ⊗_x(|↑⟩⟨↑| ⊗ ϱ_{AKLT})`, `ω_β = ⊗_x(|↓⟩⟨↓| ⊗ ϱ_{AKLT})` —
injective MPS with bond Schmidt spectrum `(1/2, 1/2)`, i.e. **`χ = 2`**,
transfer gap `1/3` — covariant for `G = U(1) ⋊ ℤ₂` with
`ω_α(S^z) = +1/2 = s = −ω_β(S^z)`; the sharp domain wall in the `ℂ²`
factor lies in `𝒦_{αβ}` and has `D_xφ = 0` at **every** site, so
(K-TAIL) holds with `C_K = 0` while the tail vacua are not product
states.  When `s_γ` **is** a simple eigenvalue of `S^z` (the standard
spin-`S` register `d = 2s+1`; D16), the sharp-charge conclusion does
give `ω_γ = ⊗_x|s_γ⟩⟨s_γ|` and `χ = 1` — that conditional clause
survives, as a corollary, not as the theorem.

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
`d_W → ∞` — the D18(AD4) order, window limit last.  **Class warning (r3,
verdict F1(b)(ii)):** the `t`-independent `(K, C_K, λ̃)` hypothesis is
FALSE on every state carrying an escaping leg of nonzero charge — on such
states the escaped tail sum saturates at the leg charge `2s` while the
minimal admissible `C_K` grows as `λ̃^{−vt}` — so this corollary's class
excludes the D18(AD3) regime entirely.  **Consequence on its own class
(F1(b)(iv)):** with `ε_Q = 0` and `t`-uniform data, (LD.4) on both time
wings plus conservation of `𝒬_{c_0}` force the ordered wall displacement
`δx = 0` (⟨1⟩4.⟨2⟩7).  The ε-version is not merely compatible with
D27(LR3); on its own class it *excludes nonzero ordered memory* — the
D13(c) trap in windowed dress.

### COROLLARY ACE-LD-ε-x (cross-term vanishing in the ordered limit)

**ASSUME.**  Two channels `ch ∈ {L,T}` each satisfying ACE-LD-ε-t with
charges `q_L ≠ q_T`, common `λ̃`, `ε_Q = 0`; put `δ := |q_L − q_T|/2 > 0`
and `ε_W := \max_{ch} \frac{2C_{K,ch}||P_{ch}Ψ||}{1−λ̃}λ̃^{d_W}`.  *(The
r2 clause "`W` large enough that `ε_W < δ`" is deleted per verdict m5:
the proof ⟨1⟩4.⟨2⟩6 uses only the set geometry, and the conclusion is
valid — merely uninformative — when `ε_W ≥ δ`.)*

**PROVE.**  With `S_T := spec π(Q̂_{W,c_0}) ∩ (q_T−δ, q_T+δ)`,

  `limsup_{t→+∞} |⟨Ψ_t, P_L E_W(S_T) Ψ_t⟩| ≤ δ^{-1} ε_W`,
  `limsup_{t→+∞} ||(1 − E_W(S_T))P_TΨ_t|| ≤ δ^{-1} ε_W`,

both `= O(λ̃^{d_W}) → 0` in the ordered limit (`t→+∞` at fixed `W`, then
`W↑ℤ`).  **Emptiness warning (r3, verdict F1(b)(iii); the r2 sentence
claiming this supplies AS ⟨1⟩7.⟨2⟩2 is RETRACTED).**  The estimate is a
correct conditional implication (r2 verdict §5 item 6), but within one
D18 conserved-charge sector its hypothesis set is **empty**: (K-Q) at
`ε_Q = 0` makes each `φ_ch` an eigenvector of the *same* conserved
`𝒬_{c_0}` at `q_ch`, and D18's preamble fixes one sector, so `q_L ≠ q_T`
is unavailable — the difference `q_L − q_T` would be the difference of
escaped charges, which (K-TAIL) forces below any coset step (⟨1⟩4.⟨2⟩7).
The corollary can only ever be instantiated OUTSIDE the D18(AD3)
setting, and no such instantiation is exhibited in this corpus.
*(Reading discipline, r1 verdict M5: what the ε-family supplies is the
**kink**-eigenstate reading of D18(AD3), ε-weakened — the kink confined
inside `W`, the window state an approximate `Q̂_W`-eigenvector.  It is
NOT the vacuum-eigenstate reading of r1's deleted route, and NOT the
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
**Positive form (r3, verdict M2(c) adopted verbatim; not a
contrapositive):** ⟨2⟩3 gives directly: on any (LR) state the mean wall
transport is uniformly bounded,
`sup_m |ω^+_{W_m}(𝔛_{W_m}) − ω^-_{W_m}(𝔛_{W_m})| ≤ (M_0+1)/(2s)`;
in particular `θ = 0`.  *(The r2 closing sentence "(LR3) forces mean wall
transport `o(|W_m|)`" is replaced: it both overclaimed the quantifier —
the literal contrapositive of the liminf hypothesis (M-ESC) yields only a
liminf statement — and underclaimed the rate, since the proof delivers
`O(1)`, uniformly bounded.  Disclosure, verdict n1: boundedness of the
mean transport under (LR3) is the quantitative form of D27's own
existence corollary — "LR3 makes the left side converge, hence the right
side" — already frozen in D27's definition paragraph; the genuine
addition of ⟨2⟩3 is the `M_0` tightness argument, and it is a strict
strengthening (r4, ace-ld-r3 n2): D27's corollary delivers convergence
along the full sequence only under D27's optional convenience clause,
and otherwise only along an (LR3) subsequence — ⟨2⟩3 delivers `sup_m`
over ALL `m`, with no subsequence, no convenience clause, and no pass
through weak convergence.)*

*(Scope.  (M-ESC) needs only the MEAN tail density — no variance
hypothesis, no channel structure, no wave operators, no `(E-TAIL)`,
`(V-ch)`, `(V-in)`, no `σ_L ≠ σ_T`, no incoming concentration.  A
kink component transiting every fixed window with asymptotic mean weight
`p_tr > 0` gives `θ = p_tr` (⟨1⟩5.⟨2⟩5), so on such "ballistic" classes the
unsubtracted window charge admits no (LR) outcome measure.  D16 is in the
COMPLEMENT, for the corrected reason of r2 verdict M5(c): every state in
the closed span of D16's K1--K2 family is exactly stationary (K1+K2,
PROVED; exhaustion of `ker H_kink` by that family is **K4, CONJECTURE**),
and for D17 kink--magnon packets the mean wall transport is bounded by
`⟨N_T⟩/s` — M-quant-G's conclusion, PROVED **conditional on H-AD-G,
i.e. on D18(AD1)--(AD4) for the selected vector**, which is open for
D16 (bd `tns-d51`; `AD3-ex` is CONJECTURE) — so `θ = 0`; LD-C7(a)
certifies only the sector ground energies at `L = 12`.  Note (r4,
ace-ld-r3 m3): D18(AD3) is jointly unsatisfiable with (K-TAIL) (LD-ID
⟨3⟩3), so this `θ = 0` fence and the ε-theorems of ⟨1⟩4 concern
**disjoint** state classes — a kink--magnon D17 packet under H-AD-G
versus a magnon-free (K-TAIL) sector state.  Nothing here bears on the
(LR)-for-D16 lane bd `tns-xf4`.)*

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
square root gives (i).  *(r4 remark, ace-ld-r3 n1: since (K-TAIL)'s
off-diagonal clause follows from its on-site clause by Cauchy--Schwarz,
(i) also follows from the triangle inequality alone,
`||Σ_F D_xφ|| ≤ Σ_F ||D_xφ||` — the square expansion is retained as the
verified derivation, unchanged.)*  (ii): for `W ⊆ W'` both containing `K ∪ {c_0}`,
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
it exists **in finite volume** (the fixed-`S^z`-sector realization, where
sector membership gives (K-Q) with `ε_Q = 0` exactly); **in infinite
volume its existence on the D16 kink folium is exactly the content of
M-INDEX-LA-folium, CONJECTURE** (r2 verdict m6 — the word "trivially" is
withdrawn; this conjecture is the only route this shard offers to
(K-Q)'s `t`-uniformity, i.e. to ACE-LD-ε-t's hypothesis, in infinite
volume).  (K-TAIL)'s `t`-uniformity in the D16 instance is the statement
that the kink stays confined; the honest support is that the K1--K2
family is exactly stationary (K1+K2 PROVED; `ker H_kink` exhaustion is
K4, CONJECTURE — r2 verdict M5), certified at `L = 12` by LD-C7(a) at the
level of sector ground energies only.

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
order.  *(r3 correction of the r2 closing sentence, per verdict
F1(b)(iv): the honest relation to D27 is NOT bare "compatibility".  On
this corollary's own class with `ε_Q = 0`, LD-ID ⟨3⟩4 shows the ordered
wall displacement is exactly `δx = 0` — the ε-version excludes nonzero
ordered memory on its class, and its class excludes every escaping-leg
state by LD-ID ⟨3⟩3.)*  □ (ACE-LD-ε-t.)

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

**⟨2⟩7. (THEOREM LD-ID — the identification and the incompatibility;
RETRACTION of the r2 bridge; LEMMA LD-MONO — the surviving offering.)**

**THEOREM LD-ID.**  ASSUME, per clause (r4 lockstep fix, ace-ld-r3 m1 —
the r3 theorem-level "ASSUME H-MQG(1)--(2)" covered ⟨3⟩1 only):
H-MQG(1)--(2) throughout; for ⟨3⟩2 additionally the existence of the
increasing-window limit on the state ((K-TAIL) suffices, ⟨2⟩2(ii)) and
D13(c); for ⟨3⟩3 additionally D18(AD3) and (K-TAIL) with
`t`-independent constants; for ⟨3⟩4 additionally (K-Q) at `ε_Q = 0`,
`t`-uniform (K-TAIL) data, and D27's definition of `δx`.  With
`s_{γ_{c_0}}(x) := +s` for `x ≤ c_0` and `−s` for `x > c_0`:

**⟨3⟩1. (The window-charge identity.)**  For every finite `W = [a,b] ∋ c_0`,

  `Q̂_{W,c_0} = Σ_{x∈W}\big(S^z_x − s_{γ_{c_0}}(x)\big)`  **exactly** —
  no offset, no factor.

*Justification.*  MI ⟨1⟩1.⟨2⟩2 gives
`Q̂_{W,c_0} = Σ_{x∈W}S^z_x + s(a+b−1−2c_0)`, and
`Σ_{x∈W}s_{γ_{c_0}}(x) = s\,[(c_0−a+1) − (b−c_0)] = −s(a+b−1−2c_0)`.
Named computation **LD-ID.1** (the r2 critic's §0(i), verified
symbolically and on a 201-site lattice there, and reached independently
by the LR-D16 lane's critic — `theory/verdicts/lr-d16-r1.md` §2 item 1).

**⟨3⟩2. (`𝒬_{c_0}` is D13(c)'s conserved charge.)**  On every (K-TAIL)
state, `𝒬_{c_0}φ − Q̂_{W,c_0}φ = lim_n Σ_{x∈W_n∖W}D_xφ`, so by ⟨2⟩2(ii)

  `||𝒬_{c_0}φ − Q̂_{W,c_0}φ|| ≤ \frac{2C_K}{1−λ̃}λ̃^{d_W}`
  for every `W ⊇ K` with `c_0 ∈ W`:  **(K-TAIL) says, in words, that the
  total charge outside the window is smaller than `2C_Kλ̃^{d_W}/(1−λ̃)`,
  for every such `W`.**  Moreover, summing ⟨3⟩1 over an exhaustion,
  `𝒬_{c_0} = Σ_{x∈ℤ}(S^z_x − s_{γ_{c_0}}(x)) = 2s(X_1 − c_0)` with `X_1`
  the first-moment wall coordinate **frozen in D13(c)** — the regularised
  total magnetisation, which D13(c)'s trap paragraph records as **exactly
  conserved**.

*Justification.*  ⟨2⟩1, ⟨2⟩2(ii), ⟨3⟩1, D13(c).  Named computation
**LD-ID.2**.  *(L4 note, verdict m3: `𝒬_{c_0}` is thereby not a new
object but the vector-valued lift of the frozen `X_1`; MP-4 records the
identification.)*

**⟨3⟩3. (Joint unsatisfiability with D18(AD3).)**  Let `Ψ_t` carry an
outgoing free leg of charge `q_leg ≠ 0` that has left `W` in the sense of
D18(AD3).  Then `||𝒬_{c_0}Ψ_t − Q̂_{W,c_0}Ψ_t|| ≥ |q_leg| − o(1)` as
`t → ∞`, while (K-TAIL) with `t`-independent `(K, C_K, λ̃)` bounds the
same quantity by `2C_Kλ̃^{d_W}/(1−λ̃)`, uniformly in `t`; choosing `d_W`
with `2C_Kλ̃^{d_W}/(1−λ̃) < |q_leg|` is a contradiction.  Hence **no
state in D18(AD3)'s escaping-leg class satisfies (K-TAIL) with
`t`-independent constants**, and ACE-LD-ε-t/-x have no instance on the
channel class AS ⟨1⟩7.⟨2⟩2 is about.  Quantitative witness (r2 verdict
F1(b)(ii), one magnon over a polarised vacuum): the escaped tail sum
saturates at exactly `2s = 1` at every padding, and the minimal
admissible `C_K` grows as `λ̃^{−vt}` (`10^{+79.8}` at `t = 64`).

*Justification.*  ⟨3⟩2 and D18(AD3)'s frozen clause ("the free leg
charge and non-bound dressing leave the window as `t→±∞`").  The lower
bound's leaf, displayed (r4, ace-ld-r3 m2): for unit `Ψ_t`,

  `||𝒬_{c_0}Ψ_t − Q̂_{W,c_0}Ψ_t|| = ||Σ_{x∉W}D_xΨ_t||
   ≥ |⟨Ψ_t, Σ_{x∉W}D_xΨ_t⟩| = |Σ_{x∉W}ω_{Ψ_t}(D_x)|`

(Cauchy--Schwarz), and D18(AD3) says that mean tends to `q_leg`.

**⟨3⟩4. (On the ε-class the ordered memory vanishes.)**  Under (K-Q)
with `ε_Q = 0` and `t`-uniform data, `q_φ` is an eigenvalue of the
conserved `𝒬_{c_0}` and is `t`-independent; (LD.4) applied on both time
wings gives `|⟨Q̂_{W_m,c_0}⟩_{φ_t} − q_φ| ≤ 2C_Kλ̃^{d_{W_m}}/(1−λ̃)` at
every `t`, so D27's ordered wall expectation obeys

  `|δx| = (2s)^{-1}\lim_m |ω^+_{W_m}(Q̂_{W_m,c_0}) − ω^-_{W_m}(Q̂_{W_m,c_0})|
   ≤ (s)^{-1}\lim_m \frac{2C_K}{1−λ̃}λ̃^{d_{W_m}} = 0`:

**on the class where the ε-version is available with `ε_Q = 0`, the
ordered memory is exactly zero** — D13(c)'s trap in windowed dress.  The
parallel lane's critic reached the same mechanism independently: on the
`𝒬 = 𝒬_0` eigenspace the wall position is pinned
(`theory/verdicts/lr-d16-r1.md` M2(b)2).

*Justification.*  ⟨2⟩3, ⟨3⟩2, conservation, D27's definition of `δx`.
□ (LD-ID.)

**RETRACTION (r2 F1(c), adopted in full).**  The r2 version of this step
claimed that ACE-LD-ε-x supplies the cross-term vanishing AS ⟨1⟩7.⟨2⟩2
consumes.  By ⟨3⟩3 that claim is **FALSE** — the hypothesis class of the
ε-corollaries is disjoint from the class AS ⟨1⟩7.⟨2⟩2 is about — and it
is withdrawn, together with MERGE PROPOSAL MP-3(ii), which would have
written it into `theory/ansatz-scattering.md`.  The true relationship:
**the ε-version is a theorem about states whose charge has NOT escaped
the core; the ordered-limit consumer needs states whose leg charge HAS
left the window.**  The two regimes partition the problem, and no bridge
between them exists in this shard.  *(Orientation note, r1 verdict n1,
still standing: AS ⟨1⟩7.⟨2⟩1 writes `ν = q_T − q_in`, opposite to the
frozen `ν = q_- − q_+`; the flag remains in MP-3.)*

**LEMMA LD-MONO (window monotonicity — anchor-free; r2 verdict F1(d)
adopted).**  ASSUME H-MQG(1)--(2), finite windows `W' ⊇ W ⊇ K` with
`c_0 ∈ W`, and the (K-TAIL) bound only for same-side pairs
`x, x' ∈ W'∖W` (an assumption about the **annulus at one time** — no
statement about the far tail or about any limit).  PROVE:

  `||(Q̂_{W',c_0} − Q̂_{W,c_0})φ|| ≤ \frac{2C_K}{1−λ̃}λ̃^{d_W}`,

hence `||(Q̂_{W',c_0} − q)φ|| ≤ ||(Q̂_{W,c_0} − q)φ|| +
2C_Kλ̃^{d_W}/(1−λ̃)` for every `q`: an ε-form (AD3-ex) at ONE window
containing the core propagates to every larger window `W'` **whose
annulus `W'∖W` carries no escaped charge — equivalently, every `W'` the
leg has already passed beyond** — up to a uniform additive
`2C_Kλ̃^{d_W}/(1−λ̃)`; at the first `W'` that reaches the leg the
difference is exactly the leg charge (LD-ID ⟨3⟩3), so the transport is
not available past that window.  *(r4 lockstep fix, ace-ld-r3 M1: the
universal-`W'` gloss must carry the quantifier its own ASSUME fixes —
the r3 gloss dropped it, and the shard's own ⟨3⟩3 refutes the dropped
form by up to `10^{21}`: measured `||(Q̂_{W'}−Q̂_W)φ|| = 2s = 1.0000` at
every padding for a leg inside the annulus, against an asserted bound
down to `4.25e-22`.)*

*Proof.*  LD-SPLIT (⟨2⟩1) writes the difference as two one-sided annulus
sums over `W'∖W`, each at distance `≥ d_W` from `K`; ⟨2⟩2(i)'s estimate
uses (K-TAIL) only on pairs inside the summed set, which here lies in
`W'∖W`.  □  *(This is the honest offering to the AS lane: it has no
anchor at infinity, so the bound is uniform in `W'` rather than decaying
— exactly the price of dropping the conserved-charge anchor — and it is
**compatible with an escaping leg that has already passed beyond `W'`**,
since the annulus is then locally back at vacuum.  It does NOT supply
(AD3-ex) at any window; it only transports an assumed ε-form outward.)*

**⟨2⟩8. (Reading discipline — what is and is not supplied; verdict M5.)**
D18(AD3) has two readings in the corpus, and every statement here is
explicit about which it touches:

- **Supplied (kink reading, ε-weakened, LEG-FREE corner only — r3):**
  with the kink CONFINED in `K ⊂ W` and **no escaped leg charge**
  (LD-ID ⟨3⟩3 makes this a consequence of the hypothesis, not an extra
  assumption), the state is an ε-approximate `Q̂_{W,c_0}`-eigenvector at
  the conserved charge `q_φ` — uniformly in `t`, defect `O(λ̃^{d_W})`
  (ACE-LD-ε-t).  This is the "remaining local state is a kink charge
  eigenstate" clause of D18(AD3) in ε-approximate NORM form, but ONLY on
  states to which the rest of D18(AD3) does not apply.  Also supplied:
  the anchor-free window transport LD-MONO (⟨2⟩7), which IS compatible
  with an escaping leg.
- **Not supplied:** (i) the exact fixed-`W` (AD3-ex) — **not refuted,
  unavailable** (r2 verdict M6 adopted): D16's exact kink states are
  never `Q̂_{W,c_0}` eigenvectors at finite `W` (defect
  `min_q||(Q̂_W−q)Ψ|| = 4.45e-02 … 4.05e-04`, decaying as `λ̃^{d_W}`;
  LD-C7), so D18(AD3)'s eigenstate clause can hold at fixed `W` only in
  ε-form — but the measured state is a magnon-free sector zero mode, NOT
  an (AD3-ex) vector (no channel decomposition, not in `ran W_+`), so no
  in-class counterexample is exhibited; the `AD3-ex` claims row stays
  CONJECTURE (MERGE PROPOSALS MP-2).  (ii) The *vacuum*-eigenstate
  reading (r1's deleted route) — no statement about escaped-window
  vacuum charges is made anywhere.  (iii) D18(AD3)'s remaining clauses —
  weak-\* convergence of the window restriction to a specific kink
  charge eigenstate, and existence of the increasing-window limit of
  D13(a) on it — in particular **M-INDEX-spec's reduction clause is NOT
  supplied** and its adjudicated scoping is untouched.  (iv) Any
  statement on classes where the kink transits: there (K-TAIL) fails for
  every fixed `K` and ACE-LD-obst′ (⟨1⟩5) rules instead.  (v) Any
  model-level PROOF of (K-TAIL)/(K-Q): the D16 instantiation is
  numerically certified on finite chains (⟨2⟩9), not proved in infinite
  volume.  (vi) **The input AS ⟨1⟩7.⟨2⟩2 consumes — retracted, r3:**
  neither ACE-LD-ε-t nor ACE-LD-ε-x supplies the inter-channel
  cross-term vanishing on the (AD3-ex) class; LD-ID ⟨3⟩3 shows the
  hypothesis fails on that entire class.

**⟨2⟩9. (The sharp-charge boundary — equivalence, PROOF of ACE-LD-sharp —
and the D16 instantiation.)**
(a) *The deletion rationale, recorded once (r1 verdict F1/M1; r4
correction per ace-ld-r3 F1).*  r1's `(E-TAIL)` demanded
`ω_γ((S^z_x−s_γ)²) = 0` at every site — **sharp on-site charge**.  This
is EQUIVALENT to `ω_γ` assigning full weight to the on-site spectral
projection at `s_γ`: if `ω_γ((S^z_x−s_γ)²)=0` then Cauchy--Schwarz gives
`|ω_γ((S^z_x−s_γ)A)|² ≤ ω_γ((S^z_x−s_γ)²)\,ω_γ(A^*A) = 0` for every
`A ∈ 𝔄`; taking `A = Π_x^{(m)}` the on-site spectral projections of
`S^z_x` pins `ω_γ(Π_x^{(m)}) = δ_{m,s_γ}` at every `x` (in particular
`s_γ ∈ spec S^z`); the converse is immediate.  *(The r1--r3 continuation
"…and a state assigning `1` to finitely many commuting projections
assigns `1` to their product, forcing `ω_γ = ⊗_x|s_γ⟩⟨s_γ|`" is
CORRECT only when the eigenvalue `s_γ` is simple: `ω_γ(Π_x^{(s_γ)}) = 1`
confines the state to the eigenspace `ker(S^z_x − s_γ)` at each site,
and only a one-dimensional eigenspace names a vector.  With degenerate
`s_γ` the state is unconstrained inside the eigenspace factor — the
ace-ld-r3 F1 counterexample puts an AKLT state there, at `χ = 2`.  The
`χ=1` reading of the equivalence is REFUTED; the sharp-charge reading
is what (E-TAIL) says.)*

(b) *PROOF of THEOREM ACE-LD-sharp (r3 upgrade, verdict M1: the boundary
is FORCED — D9(a) supplies the tail relaxation, so no relaxation
hypothesis is needed; r4 restatement, verdict ace-ld-r3 F1: the
conclusion is sharp on-site charge, and the former ⟨3⟩3 `χ=1` clause is
retired as REFUTED).*

**⟨3⟩1.**  For `γ ∈ {α, β}` and the fixed local observable
`A_γ := (S^z_0 − s_γ)²`, one has `D_x² = τ_x(A_γ)` for `x` on the `γ`
side of `K`, and D9(a) (with `D = 𝟙`) gives
`ω_φ(τ_x(A_γ)) → ω_γ(A_γ)` as `x → ∓∞`.

*Justification.*  Definition of `D_x`; D9(a)'s plain boundary condition
`ϱ(τ_n(O)) → ω_{α/β}(O)` for `O ∈ 𝔄_loc`.

**⟨3⟩2.**  (K-TAIL) at `x = x'` gives
`ω_φ(D_x²) ≤ C_K²λ̃^{2\,dist(x,K)} → 0`, so with ⟨3⟩1,
`ω_γ((S^z_0 − s_γ)²) = 0`; by translation invariance of the vacuum
(D2(a)) the same holds at every site.

*Justification.*  (K-TAIL) on-site clause; ⟨3⟩1; uniqueness of limits.

**⟨3⟩3.**  By (a)'s Cauchy--Schwarz argument,
`ω_γ(Π_x^{(m)}) = δ_{m,s_γ}` at every site: `ω_γ` has **sharp on-site
charge** `s_γ`, with translation invariance already supplied by ⟨3⟩2.
Further, `ω_γ(Π_0^{(s_γ)}) = 1` requires `Π_0^{(s_γ)} ≠ 0`, i.e.
**`s_γ ∈ spec S^z`**: the tail density must be an on-site eigenvalue.
With H-MQG(2)'s `s_α = +s`, `s_β = −s`, a spin-1 chain at calibration
`s = 1/2` is excluded by arithmetic alone (`±1/2 ∉ {−1,0,1}`).
*(RETIRED, r4: the r3 version of this step continued "hence
`ω_γ = ⊗_x|s_γ⟩⟨s_γ|` — a `χ=1` `S^z`-product state".  That inference
presumes `dim ker(S^z − s_γ) = 1` and is REFUTED without it — see the
counterexample recorded under the §0 statement and (a)'s corrected
equivalence note.  The surviving conditional: if `s_γ` is a simple
eigenvalue of `S^z`, sharp on-site charge does force
`ω_γ = ⊗_x|s_γ⟩⟨s_γ|` and `χ = 1`.)*

*Justification.*  (a); spectral theorem for the finite-dimensional
`S^z`; D2(a) for translation invariance.  □ (ACE-LD-sharp.)

The ε-version is therefore a theorem about the sharp-on-site-charge,
`s ∈ spec S^z` corner of the programme — the corner D16 occupies (there
with `χ=1` product tails, `s` being simple in D16's register), though
not, by the F1 counterexample, the only shape that corner can take —
and is NOT claimed for generic injective-MPS vacua, whose on-site
charge variance is a nonzero constant and for which
`min_q||(Q̂_W−q)φ||` does not decay.  This scope clause is carried in
§0's THEOREM statement, in HONEST STATUS, and in MP-1's not-claimed
enumeration.

(c) *The D16 instantiation (evidence, not proof; digits corrected per
verdict m1, orientation stated per m2).*  For D16's exact zero-energy
kink states projected to a fixed `S^z` sector: (K-Q) holds with
`ε_Q = 0` exactly (sector membership; ⟨2⟩4), and (K-TAIL) holds with
`λ̃ = q = Δ−√(Δ²−1)` on the numerical evidence: at `Δ = 2.5`, `L = 12`,
`c_0 = 5`, the sector ground state has
`min_q||(Q̂_W−q)Ψ|| = 4.453e-02, 9.305e-03, 1.942e-03, 4.046e-04` at
`W = [4,7],[3,8],[2,9],[1,10]` — successive ratios
`0.2089, 0.2087, 0.2083` against `q = 0.208712` — with `⟨Q̂_W⟩` on the
integer coset (checker gate LD-C7, whose figures the r2 critic
reproduced independently; the r1-inherited digits `3.96e-04` /
`0.2085, 0.2041` were stale and are corrected).  **Orientation (m2):**
the ED ground state of the D16 battery has `↓` at `−∞` and `↑` at `+∞` —
the ℤ₂-image of D13(a)'s orientation — so (K-TAIL) is instantiated with
the conjugated assignment `s_α = −s`, `s_β = +s`; under that flip the r2
critic measured (K-TAIL) itself directly: `||D_xφ||` falls by the factor
`0.2087` per site, both sides, four steps (r2 verdict §0(iii)), and
LD-C7(e) now certifies exactly this profile (n5: the defect ratios of
LD-C7(b)--(c) certify (LD.4)'s conclusion; the hypothesis is certified
by (e)).  The class of ACE-LD-ε's hypotheses is therefore INHABITED —
verified at both ends — while its infinite-volume verification on D16
remains open and is priced as such in HONEST STATUS.

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
definition paragraph.  No use of D27(LR3) is made — and the citation is
sound inside this proof by contradiction against LR3 *because* (r2
verdict n6) MI ⟨1⟩7's theorem-level ASSUME includes D27(LR), but the two
sub-steps cited here carry their own leaf justifications naming only
LR1--LR2 and (IDX.1): the sub-steps' hypotheses are strictly weaker than
their theorem's ASSUME, so no LR3 circularity arises.

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
undefined along the exhaustion — *(claim (c))*.  The surviving positive
statement is ⟨2⟩3's own bound, read directly (r3, verdict M2 — not a
contrapositive, and `O(1)`, not `o(|W_m|)`): **on any (LR) state the
mean wall transport is uniformly bounded,
`sup_m |ω^+_{W_m}(𝔛_{W_m}) − ω^-_{W_m}(𝔛_{W_m})| ≤ (M_0+1)/(2s)`; in
particular `θ = 0`.**  **QED (a)--(c).**  □

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
(i) *Dichotomy (r3 sharpening).*  ⟨1⟩4 and ⟨1⟩5 partition the reach of
the unsubtracted window charge: on confined-charge sharp-tail states
((K-TAIL)+(K-Q); `θ = 0`) the ε-version holds and — by LD-ID ⟨3⟩4 — the
ordered memory is exactly `δx = 0`; on mean-transiting states (`θ > 0`)
D27(LR3) fails and no ordered outcome measure exists.  Neither side of
the dichotomy carries a nonzero ordered memory for the unsubtracted
charge; a `{0,2}`-type ledger with `δx ≠ 0` therefore requires a
subtracted or co-moving observable (the D13(c) trap paragraph's leg
subtraction — a definition-level move, proposed for adjudication in r1
and still open, not made here).  (ii) *Evidence for the mechanism.*
The two-atom law `||F_ret||²δ_0 + ||F_tr||²δ_{−2s|W|}` with LR3 tail
`(1+2s|W|)||F_tr||²` — r1's obstruction shape — is real as a MECHANISM:
the r1 critic reproduced it to four digits on a scattering model
(verdict §0: weights `0.5567/0.4433`, incoming-concentration defect
`2.4e-09`, tail `(1+513)(0.4433) = 227.86` vs measured `227.867`), and
checker gate LD-C5 re-certifies the configuration on a barrier model
(honest content per r2 M4(d): incoming concentration and the two-atom
support including the `ν=0` atom; the identity and tail gates are
consequences of those facts, disclosed as such in §5, not independent
evidence).  It is recorded as evidence for ⟨2⟩5's `θ = p_tr` arithmetic,
NOT re-claimed as a theorem: the r1 proposition that asserted it had an
empty hypothesis class (F1).  (iii) *Fence (justification replaced per
r2 verdict M5).*  D16 is in the complement of (M-ESC): every state in
the closed span of D16's K1--K2 family is exactly stationary (K1+K2,
PROVED; exhaustion of `ker H_kink` by that family is **K4, CONJECTURE**
— the r2 sentence "its kink band is exactly flat, so `θ = 0`" was a
K4-strength upgrade about BARE kinks, while `θ` concerns kink+magnon
states, and is withdrawn), and for D17 kink--magnon packets the mean
wall transport is bounded by `⟨N_T⟩/s` — M-quant-G's conclusion, PROVED
**conditional on H-AD-G, i.e. on D18(AD1)--(AD4) for that vector**
(open for D16, bd `tns-d51`; `AD3-ex` is CONJECTURE), not a consequence
of band flatness — so `θ = 0` there and NOTHING in this shard bears on
the (LR)-for-D16 lane bd `tns-xf4`.  LD-C7(a) certifies only the 13
sector ground energies at `L = 12`.  (r4, ace-ld-r3 m3: since D18(AD3)
is jointly unsatisfiable with (K-TAIL) by LD-ID ⟨3⟩3, this fence and
the ε-theorems apply to disjoint state classes; see the §0 Scope note.)
(iv) *Cross-lane composition (recorded as such, r2 verdict §7 item 3;
re-cited in r4 per ace-ld-r3 m5; NOT this shard's theorem).*
`theory/lr-d16.md` ⟨1⟩5.⟨2⟩7 THEOREM (LRD-3) — in its repaired
lr-d16-r2 form, `(NR)` now the two-clause `sup_m` statement — proves
`(NR) ⟹ D27(LR3)` outright, with tail bound `2S_{NR}/M`.  Composing
with this shard's ACE-LD-obst′(b) (`(M-ESC) ⟹ ¬D27(LR3)`) gives
**`(M-ESC) ⟹ ¬(NR)` directly** — no appeal to lr-d16's ⟨1⟩5.⟨2⟩4
monotonicity remark is needed (the r3 route through it is superseded,
as are the lr-d16-r1 citations: lr-d16-r2 has adjudicated that lane).
The constraint is attributed to the composition of the two lanes'
critic passes, is transmitted to `tns-xf4` via MP-6 with the no-witness
disclosure attached (lr-d16-r2 M4(b)3: a conditional with an empty
antecedent constrains nothing until an (M-ESC) witness exists), and is
not proved in this shard.

**⟨2⟩7. QED (⟨1⟩5).**  □

---

## 4. HONEST STATUS

**Proved, given only its own ASSUME block (unconditional as an
implication):**

- **ACE-LD-abs** (⟨1⟩1--⟨1⟩2) and **ACE-LD-nec** (⟨1⟩3).  Verified by the
  r1 critic (verdict §5, items 1--2), re-fenced by the r2 critic, and
  unchanged in r2/r3 except the m3 lockstep fix and the LD-GAP-SET
  addition ⟨1⟩1.⟨2⟩5 (a two-line parallel of the verified ⟨2⟩1--⟨2⟩2,
  consumed only by ACE-LD-ε-x).
- **ACE-LD-sharp** (r4; §0 and ⟨1⟩4.⟨2⟩9(b)): (K-TAIL) plus D9
  kink-class membership FORCES tail vacua of **sharp on-site charge**
  (`ω_γ((S^z_x − s_γ)²) = 0` at every site) with `±s ∈ spec S^z`.
  Inputs: D9(a), D2(a), (K-TAIL) itself.  This is the theorem form of
  what r2 carried as a hedged remark (r2 verdict M1), restated at the
  correct strength per ace-ld-r3 F1 — the r3 `χ=1` product-vacuum
  clause is REFUTED (see "Refuted / withdrawn" below) and only the
  bond-dimension clause died: the `±s ∈ spec S^z` clause and the
  spin-1-at-`s=1/2` exclusion survive intact, critic-certified.
- **LD-ID** (⟨1⟩4.⟨2⟩7), with the m1 per-clause split (ace-ld-r3):
  **unconditional under H-MQG(1)--(2):** the window-charge identity
  ⟨3⟩1, `Q̂_{W,c_0} = Σ_{x∈W}(S^z_x − s_{γ_{c_0}}(x))` exactly, and —
  on any state where the increasing-window limit exists ((K-TAIL)
  suffices, ⟨2⟩2(ii)) — ⟨3⟩2's identification
  `𝒬_{c_0} = 2s(X_1 − c_0)` with D13(c)'s exactly conserved charge.
  **Conditional as named in the sub-steps:** ⟨3⟩3 (joint
  unsatisfiability of (K-TAIL)-with-`t`-independent-constants and
  D18(AD3)'s escaping-leg clause) consumes D18(AD3); ⟨3⟩4 (`δx = 0` on
  the `ε_Q = 0` class) consumes (K-Q) at `ε_Q = 0`, `t`-uniform data,
  and D27's definition of `δx`.  (The r2 critic's F1 identification,
  adopted as a theorem of this shard.)
- **LD-MONO** (⟨1⟩4.⟨2⟩7): anchor-free window monotonicity of ε-forms of
  (AD3-ex), uniform (not decaying) in the outer window, compatible with
  an escaped leg beyond the outer window.
- **ACE-LD-obst′** (⟨1⟩5): D27(LR3) fails whenever the mean tail transport
  is a positive fraction of the window.  Inputs: MI ⟨1⟩5 and MI
  ⟨1⟩7.⟨2⟩1--⟨2⟩2 (both inside the PROVED M-INDEX-fin/M-INDEX-spec
  perimeter), D27(LR1)--(LR2), and (M-ESC).  No channel structure, no
  variance hypothesis, no D28.  This is r1 verdict M2's statement,
  adopted; its closing positive statement is the **O(1)** bound
  `sup_m|ω^+−ω^-|(𝔛_{W_m}) ≤ (M_0+1)/(2s)` (r2 verdict M2), which is
  the quantitative form of D27's own existence corollary (r2 n1) — the
  genuine addition is the `M_0` tightness route.

**Proved conditionally (each hypothesis named, none hidden):**

- **ACE-LD-ε / ACE-LD-ε-t / ACE-LD-ε-x** (⟨1⟩4): conditional on
  **(K-TAIL)** and **(K-Q)** (with `t`-uniform data for the family form).
  **Forced scope (ACE-LD-sharp; r4 per ace-ld-r3 F1, carried in §0 and
  MP-1): (K-TAIL) entails tail vacua of sharp on-site charge with
  `±s ∈ spec S^z`; the theorems are claimed for that corner only, and
  nothing about generic injective-MPS vacua — whose on-site charge
  variance is nonzero — is claimed.**  The hypothesis class
  is inhabited (D16 static-kink sector states — ⟨2⟩9(c), verified at
  hypothesis AND conclusion level), unlike r1's `(E-TAIL) ∧ (V-ch)`.
  **But (r3, F1): the class is disjoint from D18(AD3)'s escaping-leg
  class (LD-ID ⟨3⟩3); ACE-LD-ε-x's `q_L ≠ q_T` is unavailable within one
  D18 sector (⟨3⟩3, §0 emptiness warning); and on the `ε_Q = 0` class
  the ordered memory is `δx = 0` (⟨3⟩4).  Nothing here supplies AS
  ⟨1⟩7.⟨2⟩2's input.**

**Hypothesised / not proved:**

- (K-TAIL) for the infinite-volume D16 kink sector: supported by
  finite-chain ED at `L ≤ 12` (⟨2⟩9(c), LD-C7) with the measured rate
  equal to the model's `λ̃ = q = Δ−√(Δ²−1)` to three digits; an
  infinite-volume proof (e.g. from D1(c)'s transfer gap on the sector
  MPS) is the natural next target and is NOT claimed here.
- (K-Q) for all `t`: propagated from `t=0` by conservation WHERE a
  commuting relative-charge operator exists (⟨1⟩4.⟨2⟩4); exact in the
  finite-volume D16 sector realization; **in infinite volume the
  existence of the commuting implementer on the D16 kink folium is
  exactly M-INDEX-LA-folium, CONJECTURE** (r2 m6) — and unconditionally
  it CANNOT exist sector-wide (M-INDEX-LA-strong, REFUTED row).
- (M-ESC) on any concrete model/state: **no model or state realising
  `θ > 0` is exhibited anywhere in this corpus** (r2 m7; independently
  confirmed by the parallel lane, lr-d16-r1 M2(b)1 and lr-d16-r2
  M4(b)3 — the latter ruling that a conditional with an empty
  antecedent constrains nothing until a witness exists).  The barrier-model
  certificate LD-C5 exhibits the mechanism's configuration on a
  one-particle model; whether a D28-class kink--magnon state realises
  `θ > 0` is a model question this shard does not answer.  *(r1's claim
  that D28 packets force ballistic kinks was FALSE — r1 F1(b)(iv) — and
  is withdrawn; D28's class contains `θ = 0` members, D16 among them.)*

**Refuted / withdrawn (r2, r3, r4):**

- r1's ACE-LD-esc, COROLLARY ACE-LD, ACE-LD-obst as stated: hypothesis
  class `(E-TAIL) ∧ (V-ch)` EMPTY on every instantiated model (r1 F1);
  withdrawn, not repaired.
- **r4 (ace-ld-r3 F1): THEOREM ACE-LD-χ's `χ=1` clause is REFUTED under
  H-MQG(1)--(2) alone** and the theorem is retired in favour of
  ACE-LD-sharp.  (K-TAIL) forces *sharp on-site charge*, which coincides
  with a `χ=1` product vacuum only when `s_γ` is a **simple** eigenvalue
  of `S^z` — a hypothesis the corpus explicitly refuses to impose.
  Counterexample (critic-built, verified): `ℂ²⊗ℂ³` with
  `S^z = σ^z/2 ⊗ 𝟙_3`, vacua `|↑⟩/|↓⟩ ⊗ AKLT` — injective, `χ = 2`,
  transfer gap `1/3`, D26(INT) holding at `κ = 1/2` — with the sharp
  wall in the `ℂ²` factor giving `D_xφ ≡ 0`, hence (K-TAIL) with
  `C_K = 0`.  The r2 §8(A) row sentence carrying the `χ=1` clause was
  withdrawn by the critic itself; MP-1's eps row now carries the
  ace-ld-r3 §8(A) cell instead.  What survives: `±s ∈ spec S^z`, the
  spin-1-at-`s=1/2` exclusion, and the exclusion of every
  nonzero-variance vacuum — everything the scope argument needs.
- **r3 (r2 verdict F1):** the r2 claim that (AD3-ex-ε)/ACE-LD-ε-x
  supplies what AS ⟨1⟩7.⟨2⟩2 consumes, the "Compatible with D27(LR3)"
  framing, and MP-3(ii) are withdrawn as FALSE: `𝒬_{c_0} = 2s(X_1−c_0)`
  is D13(c)'s conserved charge, (K-TAIL) is equivalent to "no leg charge
  outside `K`", it is jointly unsatisfiable with D18(AD3)'s
  escaping-leg clause and with `q_L ≠ q_T`, and on its own class
  `δx = 0` (⟨1⟩4.⟨2⟩7).
- On (AD3-ex) at fixed `W` (r2 M6 correction of the r2 wording): D16's
  exact kink states are never `Q̂_{W,c_0}` eigenvectors at finite `W`
  (defect decaying as `λ̃^{d_W}`, LD-C7), so the exact display can hold
  at fixed `W` only in ε-form; but the measured state is a magnon-free
  zero mode, not an (AD3-ex) vector, so **the exact display is not
  refuted — it is unavailable**, and no in-class vector is exhibited.
  `AD3-ex` stays CONJECTURE.

**Merely evidence:**

- The numerical certificates (§5, `theory/checks/ace_ld_check.py`):
  LD-C1--C4 instantiate ACE-LD-abs/-nec surfaces on a free two-channel
  lattice model; LD-C5 certifies, on a barrier scattering model, the
  incoming one-charge concentration and the exact two-atom TPM support
  including the `ν=0` atom (its identity and tail gates are disclosed as
  consequences, not independent evidence — r2 M4), plus a two-branch
  dephasing certificate for the `𝒟` mechanism of MI ⟨1⟩7 — re-anchored
  in r4 per ace-ld-r3 M2: the wedge `6.083` at `(t_-,t_+) = (0,300)`
  certifies only that `𝒟` acts; the D27(LR2) claim is now measured at
  D27's own quantity, the **double-Cesàro defect `−3.3592`**, stable
  across `T = 20, 40, 80` (checker) and `T = 20…200` (ace-ld-r3 M2(b)),
  with the mechanism that the backward-evolved packet stays split across
  three window-charge branches (`0.8563/0.0170/0.1267`) forever — the
  barrier bound state is NOT the cause (critic: projecting it out
  leaves `−3.4116`); LD-C6 certifies the bounded-transport contrast on
  the D16 kink+magnon battery, where the dynamics does NOT commute with
  `Q̂_W` (r2 M3: the r2 position-diagonal LD-C6 was a tautology and is
  replaced; r4: the first-moment bound is keyed to a recorded `t_+`
  sweep, ace-ld-r3 M3); LD-C7 certifies the D16 sector ground energies,
  the strictly positive fixed-`W` defect, its `λ̃^{d_W}` decay rate, the
  coset location, AND (K-TAIL) itself site-by-site (r2 n5) — **in
  full**: by Cauchy--Schwarz on the self-adjoint `D_x`, (K-TAIL)'s
  off-diagonal clause is equivalent to its on-site clause, so LD-C7(e)
  certifies the whole hypothesis, not merely its diagonal (ace-ld-r3
  n1, claimed) — by exact diagonalisation.  All on those models only.

**Honest defects and L2 self-report.**  (i) This shard is 1785 lines
(r4; the r3 count was 1447, mis-reported as ~1200 — ace-ld-r3 m7; the
r4 growth is the F1 restatement, the verbatim promotion cells, and the
completed reachability disclosure) against the 200--500 band; the r1
critic's m7 split proposal (obstruction into its own shard) is endorsed
by three critic passes (r2 m8, r3 §9 MP-5 "the single highest-value
structural action left", MP-5 below) but outside this lane's writable
set — a MERGE PROPOSAL requests the split.
(ii) (K-TAIL) is a hypothesis ABOUT the channel family `{φ_t}`; its
reduction to initial data + dynamics (confinement) is supplied only in
the D16 instance, and there only up to K4 (CONJECTURE) and
M-INDEX-LA-folium (CONJECTURE).  (iii) The `o(|W_m|)` in (M-ESC)/⟨2⟩5 is
not quantified; any downstream use wanting rates must sharpen it.
(iv) The shard-local symbol `θ` of (M-ESC) collides with the frozen twist
variable `θ` in notation.md's `μ_∞^α` row (r2 n2); MP-4 proposes the merged
name `θ_{tr}` and flags the overload — inside this shard `θ` always means
(M-ESC)'s transport fraction.

## 5. CHECKER SPEC — `theory/checks/ace_ld_check.py` (r3 rebuild, r4 repair)

Deterministic; no randomness; no bare `assert` (every violation raises
`CheckFailure`, active under `python3 -O`).  Green exits 0; `--red` exits
1 iff every registered mutation reproduces exactly its registered
pattern, else 2; a green gate failure exits 3.  Rebuilt after r2 verdict
M3 (LD-C6 was a tautology — the campaign's sixth no-op gate — and is
REPLACED) and M4 (LD-C5's subsumptions disclosed; unreached sub-gates
armed or listed; **no blanket reachability claim** — the table below is
the claim, including its honest unreached rows).  Repaired in r4 after
ace-ld-r3 M2 (LD-C5b re-anchored at D27(LR2)'s own double-Cesàro
quantity; the `V_0 = 0` separator registered), M3 (LD-C6 first-moment
gate evaluated first; its bound keyed to a recorded `t_+` sweep; the
unreached list expanded below) and m8 (the docstring's phantom
`--table` flag deleted — the table lives here, in this section, only).

**Model batteries** (constants in the code header; spec and code in
lockstep):

- **FREE** (gates LD-C1--C4; the ACE-LD-abs/-nec surface): one particle
  on `ℤ_N`, `N = 8192`, `H` = nearest-neighbour hopping (dispersion
  `2cos k`, FFT propagation), window `W = [N/2−16, N/2+16]`, D13(a)
  clamp charge, `spec = {0,…,|W|} ⊂ ℤ`; channels = momentum-sign
  projections; state = two counter-propagating bump packets at
  `k = ∓π/2` (no detune), weights `0.8/0.6` normalised; dyadic times
  `t = 4,…,1024`; ring-cut guard `< 1e-16`.
- **BARRIER** (gates LD-C5, LD-C5b): one particle on `ℤ_N`, `N = 2048`,
  `H` = hopping plus a one-site barrier `V_0 = 1.2` at the centre, dense
  `eigh` (cached per `V_0` — the H is identical across instances; states
  are never shared); LD-C5: incoming bump packet 300 sites LEFT of the
  barrier; `t_- = 0`, `t_+ = 300`; windows `|W| = 17, 33, 65, 129`.
  LD-C5b: the SAME dynamics with the packet centred ON the barrier
  inside the `|W| = 17` window (straddling configuration); r4 adds the
  double-Cesàro protocol — `9×9` grids on
  `[T,2T] × [−2T,−T]`, `T ∈ {20, 40}`, pinching `𝒟_{W,t_-}` realised as
  branch decomposition in the clamp eigenbasis at `t_-` followed by
  forward evolution of each branch to `t_+`; an executable no-wrap guard
  requires `4T < N/2`, equivalently `T < N/8 = 256`.
- **D16** (gates LD-C6, LD-C7): exact diagonalisation of the D16 XXZ
  kink chain, `Δ = 2.5`, `J = 1`, `L = 12`, open, WITH the telescoping
  boundary field; all 13 `S^z` sectors; half-filled-sector ground state;
  `c_0 = 5`; windows `[4,7],[3,8],[2,9],[1,10]` (paddings
  `d_W = 1,2,3,4`); core `K = [4,7]` for the (K-TAIL) profile.  LD-C6
  adds ONE MAGNON: `S^-` applied at site 10 (the `↑` tail of the ED
  ground state, which is the ℤ₂-image of D13(a)'s orientation — m2),
  evolved in the `n_↓ = 7` sector to `t_+ = 4`.

**Green certificates** (measured green values quoted from the shipped
run, `python3 -O`, exit 0; wall clock is machine-local — r3 n3 — and is
50 s on the shipping machine after the r4 double-Cesàro and sweep gates):

- `LD-C1` (hypothesis audit; five sub-gates in order): spectral
  separation `≥ 1`; single coset of `ℤ` (spread `< 1e-12`; disclosure,
  r2 n4: this sub-gate is ARITHMETIC on the checker's own integer clamp
  — it can fail only if the observable's construction is corrupted, the
  same status `memory_index_probe.py` P2 carries and discloses);
  `[P_±,H] = 0`; `P_+P_- = 0`; `(P_++P_-)Ψ = Ψ`, all to `1e-9`.
- `LD-C2` (first-moment escape): `ε_±(t)` decreasing to `< 1e-6`
  (measured final: `7.2e-12`, `3.3e-12`).
- `LD-C3` ((LD.1) at the ASSERTED constant `d^{-1} = 1` per ⟨1⟩1.⟨2⟩3 —
  NOT computed from the model spectrum): at every grid time.  Measured
  `max_t max_{ch} lhs/rhs = 0.168`, green-only liveness floor `0.10`.
  Honesty clause (r1 M6): NOT a sharpness test — constants ~6× smaller
  would also pass.
- `LD-C4` (diagonality at `t = 1024`): `< 1e-6`.  Near-subsumption by
  C2∧C3 disclosed in the gate docstring; its independent value is the
  direct norm test, and it is the `--red-merged`/`--red-dup` surface.
- `LD-C5` (obstruction-mechanism configuration; evidence vs consistency
  split per r2 M4):
  *Evidence gates:* (a) incoming concentration `< 1e-4` at every window
  (measured `≤ 3.2e-6`); (b) the TPM law is EXACTLY two atoms
  `{ν=0, ν=−|W|}` — including the `ν=0` atom — off-atom mass `< 1e-4`;
  (c) atom weights equal the independently measured `|r|² = 0.2704`,
  `|t|² = 0.7296` within `1e-3`.
  *Consistency lines, DISCLOSED as deductively subsumed (r2 M4) — kept
  as cross-checks, NOT claimed as independent evidence:* (d) the
  first-moment identity `Σ_ν ν p_W = ⟨Q̂⟩_{t_-} − ⟨Q̂⟩_{t_+}` within
  `1e-4` — given gate (a) the incoming state is a single spectral
  branch, so the two sides coincide up to the concentration defect (the
  measured gap is `~4e-11` and tracks (a)'s defect); (e) the LR3 tail
  moment `13.13 → 24.80 → 48.15 → 94.84` with floor
  `0.9(1+|W|)|t|² = 85.4` — given (b)+(c) the floor clause is
  arithmetically `1 > 0.9`.  The r2 sentences "independent
  computations" and "no other gate pair is deductively linked" are
  DELETED (they were false).
- `LD-C5b` (two-branch dephasing certificate; r2 M4(c), **re-anchored
  r4 per ace-ld-r3 M2**).  Gate (a), the WEDGE at the single pair
  `(t_-, t_+) = (0, 300)`: the two quantities LD-C5(d) compares are
  measured to DISAGREE, `Σνp = +0.368` vs unpinched
  `⟨Q̂⟩_- − ⟨Q̂⟩_+ = −5.716`, wedge `6.083 > 1.0`.  **This certifies
  ONLY that the pinching `𝒟` genuinely acts on a two-branch state** —
  it is the `t_- = 0` defect, NOT the D27(LR2) quantity, and the
  inference "wedge, therefore LR2 fails" is INVALID: the `V_0 = 0`
  straddling packet has a LARGER `t_-=0` defect (`−8.3868`), passes
  this gate, and satisfies D27(LR2) exactly (r3 M2(b); registered as
  `--red-c5b-nobarrier`).  The r3 sentences "LR2 measurably FAILS there
  (the defect saturates at `6.083` …)" and the log line "AND on
  average (measured)" claimed the wrong quantity and no computed
  average, and are DELETED.  Gate (b), NEW — **D27(LR2) at its own
  double-Cesàro quantity**: the mean over `t_+ ∈ [T,2T]`,
  `t_- ∈ [−2T,−T]` (9×9 grid) of
  `⟨𝒟_{W,t_-}(Q̂_W(t_+))⟩ − ⟨Q̂_W(t_+)⟩`, measured
  **`−3.3592` at `T = 20` and `T = 40`** (floor `|·| > 3.0`, keyed to
  the r3 M2 figure; T-stability gated at `0.02`, measured spread
  `~3e-5`; the critic finds the same value out to `T = 200`, below the
  ring-wrap horizon `T = N/8 = 256`).  **LR2
  genuinely fails on this state — at the corrected number.**
  Mechanism (r3 M2(b), logged: measured branch weights): under
  backward evolution the packet stays split across three window-charge
  branches — left `q=0` / inside `W` / right `q=17` =
  `0.8563 / 0.0170 / 0.1267`, identical at `t_- = −80` and
  `t_- = −400` — so the pinching never becomes trivial; the barrier
  bound state is NOT the cause (projecting it out leaves `−3.4116`,
  r3 M2(b)).  Design decisions, recorded: (i) an identity-with-`𝒟`
  gate is deliberately NOT shipped — against the same branch
  decomposition it reduces to `x ≡ x`, the campaign's no-op pattern
  (refusal certified, r3 n6); (ii) MI ⟨1⟩7.⟨2⟩2's averaged identity is
  NOT certified on any two-branch state, because on this one its LR2
  hypothesis fails (now measured at LR2's own quantity) — which is the
  honest finding: LR2 is a hypothesis, and LD-C5's gate (d) succeeds
  in the concentrated configuration only by virtue of gate (a).
- `LD-C6` (REPLACED per r2 M3 — bounded-transport contrast on the D16
  kink+magnon battery; the dynamics does NOT commute with `Q̂_W`;
  **gate order and moment bound repaired r4 per ace-ld-r3 M3**).
  Gates, in evaluation order: (a) BOUNDED FIRST MOMENT — evaluated
  FIRST (r4 reorder, so `--red-c6-moving` reaches it):
  `Σ|ν|p ≤ 1.2` at every window (measured at `t_+ = 4`: worst `0.453`,
  non-extensive in `|W|`; the LR3 tail beyond `M = 10` is then `0` at
  every window — implied by (b), stated not gated); (b) SUPPORT: TPM
  mass at `|ν| > 3` below `1e-9` at every window (measured worst
  `9.1e-13`) — one magnon transports bounded charge, against LD-C5's
  transit atom at `ν = −|W|` (armed by `--red-c6-weaktransit`, r4);
  (c) LIVENESS at the largest window: `1 − p_0 ≥ 0.02` (measured
  `0.453` at `[1,10]`; per-window `0.017, 0.402, 0.423, 0.453`) — this
  battery CANNOT pass the way the r2 tautology did; (d) `t_+` SWEEP of
  the first moment (r4, r3 M3: the r3 bound `1.0` was time-tuned to
  `t_+ = 4` — the GREEN model fires it at `t_+ = 20` with `1.0712`,
  so it certified "`Σ|ν|p ≤ 1` at `t_+ = 4`", not bounded transport):
  `Σ|ν|p ≤ 1.2` at every window at every
  `t_+ ∈ {4, 20, 40, 200}`, with the sweep recorded — measured sweep
  maximum `1.0712` at `t_+ = 20`, `W = [3,8]` (per-window maxima at
  `t_+ = 20/40/200`: `0.470/0.181/0.057`, `1.071/0.904/0.540`,
  `0.794/0.896/0.566`, `0.055/0.128/0.380`), and `C6_MOM_BOUND = 1.2`
  sits above it.  The support and liveness gates stay at the protocol
  time `t_+ = 4`; the sweep extends the MOMENT claim only — disclosed
  here.
- `LD-C7` (the ε-version on D16): (a) sector ground energies:
  `|E_0| < 1e-10` in every sector (measured max `8.2e-17`) —
  certifies ONLY this (the `θ_{tr} = 0` fence rests on K1+K2 with K4
  CONJECTURE, r2 M5, not on this gate); (b) `min_q||(Q̂_W−q)Ψ| > 1e-6`
  at every window (measured `4.45e-02, 9.30e-03, 1.94e-03, 4.05e-04`) —
  the exact (AD3-ex) display is UNAVAILABLE at fixed `W` (r2 M6: this
  state is a magnon-free zero mode, not an in-class refutation);
  (c) defect ratios = `q = 0.208712` within 2% (measured
  `0.2089, 0.2087, 0.2083`) — the conclusion's `λ̃^{d_W}` law;
  (d) `⟨Q̂_W⟩` within `1e-2` of the integer coset (measured worst
  `2.0e-3`); (e) NEW (r2 n5) — **(K-TAIL) itself**: the one-site
  deviations `||D_xφ||` outside `K = [4,7]`, in the ℤ₂-flipped
  orientation (m2), measured
  `4.36e-02, 9.09e-03, 1.90e-03, 3.96e-04, 8.27e-05` at
  `dist = 1..5` (right) and `1.90e-03, 3.96e-04, 8.27e-05` (left) —
  per-site ratios `0.20871` on BOTH sides (gate: within 2% of `q`), and
  `C_K = max ||D_xφ||λ̃^{−dist} = 0.209 ≤ 0.30`.  These are the r2
  critic's own §0(iii) figures, now certified rather than merely
  reproduced; MP-1's eps row now attributes hypothesis-certification to
  (e) and conclusion-rate to (b)--(c), fixing the n5 mis-attribution.
  **r4, claimed per ace-ld-r3 n1: (e) certifies (K-TAIL) IN FULL, not
  merely its diagonal** — the off-diagonal clause follows from the
  on-site clause by Cauchy--Schwarz on the self-adjoint `D_x`, and the
  critic measured the off-diagonal ratio maxing at exactly `1.0000` on
  the diagonal (ace-ld-r3 §0(iv)).

**Red modes and the REACHABILITY TABLE (this table IS the claim — no
blanket sentence).**  23 registered modes (mode count, not firing
count — r2 n3; r4 adds `c5b-nobarrier` and `c6-weaktransit`), each a
FRESH model variant; `--red` → exit 1, RED-OK, 23/23 (99 s, machine-
local).  Per-mode registered pattern and measured exit path:

| mode | battery | breaks (exit path, measured) | survives |
|---|---|---|---|
| `--red-gap` | FREE | LD-C1 (gap: `separation 0.1 < 1`), LD-C3 (`t=8, lhs 4.12e-01 > rhs 3.72e-01`) | LD-C2, LD-C4 |
| `--red-coset` | FREE | LD-C1 (coset: spread `0.414`) | LD-C2, LD-C3, LD-C4 |
| `--red-halfspace` | FREE | LD-C1 (commutation: `[P_+,H] = 0.53`) | LD-C2, LD-C3, LD-C4 |
| `--red-c1-overlap` (NEW) | FREE | LD-C1 (**orthogonality**: `6.455e-02`), LD-C2 (`2.13`), LD-C4 (`6.46e-02`) | LD-C3 |
| `--red-c1-leak` (NEW) | FREE | LD-C1 (**resolution**: `sum P_ch psi != psi, 8.068e-02`), LD-C2 (`0.11`), LD-C4 (`4.84e-02`) | LD-C3 (rhs inflates with `ε`) |
| `--red-merged` | FREE | LD-C2 (`26.4`), LD-C4 (`0.80`) | LD-C1, LD-C3 |
| `--red-dup` | FREE | LD-C2 (`26.4`), LD-C4 (`1.00`) | LD-C1, LD-C3 |
| `--red-c5-nobarrier` | BARRIER | LD-C5 (atom: `p0 = 0`) | — |
| `--red-c5-meanshift` | BARRIER | LD-C5 (identity line, data mutation: `−12.40 vs −11.40`) | — |
| `--red-c5-inwindow` | BARRIER | LD-C5 (concentration: defect `0.997`) | — |
| `--red-c5-weights` (NEW) | BARRIER | LD-C5 (weights, data mutation: `0.2704 != 0.3204`) | — |
| `--red-c5-fixedwin` (NEW) | BARRIER | LD-C5 (tail growth: `13.132 -> 13.132`, degenerate exhaustion) | — |
| `--red-c5b-flat` (NEW) | BARRIER | LD-C5b (wedge `1.8e-15`: pinching inert) | — |
| `--red-c5b-concentrated` (NEW) | BARRIER | LD-C5b (wedge `4.3e-11`: not two-branch) | — |
| `--red-c5b-nobarrier` (NEW r4) | BARRIER | LD-C5b (**double-Cesàro gate**: mean defect `−1.997e-04` within `3.0` at `T=20` — the r3 M2 separator: its `t_-=0` wedge is `8.3868`, LARGER than green's, and it passes the wedge gate, yet D27(LR2) HOLDS on it) | — |
| `--red-c6-static` (NEW) | D16→BARRIER | LD-C6 (**liveness**: `1−p0 = 0` — the r2 tautology, now DETECTED) | — |
| `--red-c6-moving` | D16→BARRIER | LD-C6 (**first moment**: `12.4024 > 1.2` at `\|W\|=17` — post-r4-reorder exit path; the r3 path was the support gate) | — |
| `--red-c6-weaktransit` (NEW r4) | D16→BARRIER | LD-C6 (**support**: mass `3.742e-02` at `\|ν\|>3` at `\|W\|=17`; its first moment `0.6361` passes — arms the gate the r4 reorder shadows on large-transit mutants) | — |
| `--red-c7-delta` | D16 | LD-C7 (rate: `0.1717` vs `0.2087`) | — |
| `--red-c7-mixed` | D16 | LD-C7 (coset: `⟨Q̂_W⟩ = −0.499`) | — |
| `--red-c7-product` | D16 | LD-C7 (defect-positivity: defect `0`) | — |
| `--red-c7-noboundary` | D16 | LD-C7 (sector energies: max `1.146`) | — |
| `--red-c7-orientation` (NEW) | D16 | LD-C7 (**(K-TAIL) gate**: `C_K = 2525 > 0.3` under D13(a)'s literal orientation) | — |

**Honest unreached rows — measured enumeration for the 23 registered
modes (r4, per ace-ld-r3 M3 and ace-ld-r4 M1: each row names the
shadowing gate or protocol reason).**  The r3 list stopped three
evidence-carrying items early; the two the critic fired on a copy are
items 4 and 5 below.  Post-reorder, LD-C6's first moment IS reached
(`--red-c6-moving`) and its support gate is armed
(`--red-c6-weaktransit`) — those two r3 gaps are closed, not listed.

1. `LD-C5(e)`'s FLOOR clause is reached by no registered mode and no
   in-class mutation can reach it: given gates (b)+(c) it is
   arithmetically `1 > 0.9`, so any mutation breaking the floor breaks
   (b) or (c) first.  It is a disclosed consistency line, not evidence
   (r2 M4(d) adopted).  Its GROWTH clause is armed (`--red-c5-fixedwin`).
2. `LD-C5(d)`'s identity line is armed only by a DATA mutation
   (`--red-c5-meanshift`), which proves the comparison live and nothing
   more; its evidential content in the concentrated configuration is
   subsumed by gate (a) (measured gap `4e-11` tracks the concentration
   defect).  The two-branch content lives in LD-C5b.
3. `LD-C3`'s green-only liveness floor is by design evaluated on no
   mutant (registered patterns stay exact); it can fire only on green.
4. `LD-C7(e)`'s per-side PROFILE-RATIO sub-gate is shadowed by the
   `C_K` gate: `--red-c7-orientation` fires `C_K = 2525` first.  It has
   teeth — the r3 critic disabled the `C_K` gate on a copy and the
   ratio sub-gate fired at `ratio 1.0000` on side L (r3 M3(b)) — but no
   registered mutation reaches it.
5. `LD-C6`'s BOUNDED-FIRST-MOMENT gate was item 4's twin in r3
   (shadowed by the support gate; fired at `12.4024` on a copy with the
   shadow disabled, r3 M3(b)); the r4 reorder makes `--red-c6-moving`
   reach it, and it is now in the table above, not this list.
6. `LD-C5`'s transit-atom sub-gate (`ptr > 0.05`): on the registered
   set the `ν=0`-atom gate fires first (`--red-c5-nobarrier` kills
   reflection, so `p0 = 0` is hit before `ptr` is examined).  A
   no-transmission mutant would reach it; none is registered.
7. `LD-C5`'s off-atom-mass sub-gate (`|other| < 1e-4`): shadowed by
   the concentration gate (a) — every registered mutation that spreads
   TPM mass (`--red-c5-inwindow`) fires (a) first.
8. `LD-C5(c)`'s transmit-weight half (`|ptr − t²| < 1e-3`): shadowed by
   its own reflected-weight half — `--red-c5-weights` shifts the
   measured `|r|²`, so `|p0 − r²|` fires first.
9. `LD-C2`'s monotone-decrease sub-gate: shadowed by the final-value
   gate — every registered mutant breaking LD-C2 already fails
   `ε(t_final) < 1e-6`.
10. Guards, reached by no registered mutation because no mutation
    alters the protocol far enough: `LD-C6`'s magnon-creation guard
    (`norm > 0.5`), the FREE battery's ring-cut guard
    (`guard_no_wrap`), and `LD-C5`'s ring-cut guard.  These gate green
    protocol integrity, not evidence.
11. `LD-C5b`'s `T`-STABILITY gate is reached by no registered mutation:
    `--red-c5b-flat` and `--red-c5b-concentrated` die at the WEDGE, while
    `--red-c5b-nobarrier` passes the WEDGE but dies at the first-span
    Cesàro FLOOR.  Its teeth were re-confirmed on a copy at the shipped
    spans by tightening only `C5B_LR2_STAB` to `1e-6`: both floor checks
    pass at `−3.3592`, then STABILITY fires at measured spread
    `4.882e-05`.  The old `(20, 256)` teeth mutation from ace-ld-r4 M1
    is now rejected by the no-wrap guard at its `T = 256` endpoint.
12. `LD-C6`'s `t_+`-SWEEP gate is reached by no registered mutation:
    `--red-c6-moving`, `--red-c6-weaktransit`, and `--red-c6-static` die
    respectively at FIRST MOMENT, SUPPORT, and LIVENESS.  Moreover, the
    red-battery `C6BarrierAdapter` fixes its protocol time, so a reached
    sweep there would only repeat one cached law.  Its green-side teeth
    were confirmed on a copy with `C6_MOM_BOUND = 1.0`: gate (a) passes
    at `0.453`, then SWEEP fires at `1.0712` for `t_+ = 20`, `W = [3,8]`
    (ace-ld-r4 M1).

Design notes.  (i) Distinct red modes are distinct in effect
(`--red-coset` shifts ONE edge eigenvalue by `√2−1` keeping the gap
`≥ 1`; `--red-gap` is the constant shrink; LD-C3 survives the former and
dies under the latter).  (ii) Data mutations falsify ground truth, not
checker constants: `c5-meanshift` (the state-side mean), `c5-weights`
(the measured `|r|²`), `c7-delta` (the model at `Δ = 3.0` against the
kept `q(2.5)` claim), `c7-orientation` (the tail assignment against the
ED state's actual orientation).  (iii) `--red-c6-static` runs the NEW
LD-C6 gates on the r2 LD-C6's own model class (position-diagonal `H`)
and dies at the liveness gate — the r2 tautology is now itself a
registered mutant, which is the sharpest available proof that the
rebuilt gate tests what the old one could not.  (iv) The eigh cache
shares only the eigendecomposition of the IDENTICAL Hamiltonian at
fixed `V_0`; every mutant is a fresh model instance and no state is
shared.  (v) r4: `--red-c5b-nobarrier` is the r3 M2 separator state —
it PASSES the wedge gate (its `t_-=0` defect `−8.3868` exceeds
green's) and dies only at the double-Cesàro gate, which is exactly
what certifies that the corrected gate, unlike the r3 one, separates
"`𝒟` acts" from "LR2 fails"; `--red-c6-weaktransit` (barrier
`V_0 = 10`, `|t|² ≈ 0.037`) passes the reordered first-moment gate at
`|W| = 17` and dies at SUPPORT, keeping that gate armed post-reorder.
## 6. MERGE PROPOSALS (exact replacement text; orchestrator merges after
the critic converges — nothing below is live.  r4: MP-1 carries the
ace-ld-r3 §8(A)--(D) promotion cells VERBATIM (the r2 §8(A) sentence is
withdrawn by its author, r3 F1); MP-3(ii) carries the r3 M1(c)
quantifier; MP-4 is string-anchored and is a merge PRECONDITION of MP-1
(r3 §8(E)); MP-6 is re-cited to lr-d16-r2 / THEOREM (LRD-3) per r3 m5)

**MP-1. New rows for `claims/CLAIMS.md`** (append after the AD3-ex row).
r4: the ACE-LD-eps, ACE-LD-obst-prime, LD-ID and ACE-LD-sharp rows below
are the ace-ld-r3 verdict's §8(A)--(D) promotion cells **VERBATIM**
(machine-transplanted from `theory/verdicts/ace-ld-r3.md`; the only
transformations are markdown pipe-escaping `|`→`\|` for table cells and
the appended "(pending L6 loop)" status qualifier, which the orchestrator
drops at merge).  The r2 §8(A) sentence that the r3 eps row carried is
WITHDRAWN by its own author (ace-ld-r3 F1) and is replaced here by the
r3 §8(A) cell.  Merge preconditions (ace-ld-r3 §8(E)), both discharged by
this shard revision: (1) the F1 sharp-charge correction is applied
throughout this shard in the same commit; (2) MP-4 (string-anchored
below) merges with or before these rows.

| id | statement | status | depends on | proved in | tested in |
|---|---|---|---|---|---|
| ACE-LD-abs | Given (A1)--(A5) — unitary group, bounded self-adjoint `Q̂` with finite one-coset spectrum, mutually orthogonal dynamics-commuting channel projections resolving the vector, first-moment escape `\|\|(Q̂-q_ch)P_chΨ_t\|\|→0`, pairwise distinct channel charges — spectral diagonality holds: `\|\|E({q_ch})Ψ_t-P_chΨ_t\|\| ≤ Σ_{ch'}d_{ch'}^{-1}ε_{ch'}(t) → 0` with `t`-uniform constant (`≤ n` for coset charges); `N` channels, general on-site spin.  Distinct charges are NECESSARY (ACE-LD-nec): shared charge + two nonvanishing weights refutes the display for every claimed eigenvalue.  NOT claimed: any statement about a concrete model, any instantiation of (A4), or sharpness of the constant beyond the single spectral gap | PROVED (pending L6 loop) | — | theory/ace-ld.md ⟨1⟩1--⟨1⟩3 | theory/checks/ace_ld_check.py LD-C1--C4 (green exit 0; `--red` exit 1, 23 modes, exit paths logged; every LD-C1 sub-gate armed, incl. orthogonality and resolution — r2 M4/m4 fixed) |
| ACE-LD-eps | **Adjudicated scoping (verbatim, ace-ld-r3 §8(A)).**  Proved only as the conditional implication: H-MQG(1)--(2), a finite core `K = [ℓ,r]`, a finite window `W = [a,b] ⊇ K` with cut `c_0 ∈ W` and padding `d_W := min(ℓ−a, b−r)+1`, the on-site tail deviations `D_x := S^z_x − s_{γ(x)}` where `s_{γ(x)}` is the D13(a)/H-MQG(2) tail density on the side of `x` (`s_α = +s`, `s_β = −s`), and a unit vector `φ` satisfying **(K-TAIL)** — `\|ω_φ(D_xD_{x'})\| ≤ C_K²λ̃^{dist(x,K)}λ̃^{dist(x',K)}` for all same-side `x, x' ∉ K`, with constants `C_K < ∞` and `λ̃ ∈ (0,1)` — and **(K-Q)** — `\|\|𝒬_{c_0}φ − q_φφ\|\| ≤ ε_Q`, where the relative-charge limit **vector** `𝒬_{c_0}φ := lim_n Q̂_{W_n,c_0}φ` exists on every (K-TAIL) state, is exhaustion-independent, and satisfies `𝒬_{c_0} = 2s(X_1 − c_0)` with `X_1` the exactly conserved first-moment wall coordinate frozen in D13(c) — `⟹` `\|\|(Q̂_{W,c_0} − q_φ)φ\|\| ≤ ε_Q + 2C_Kλ̃^{d_W}/(1−λ̃)`, and hence `dist(q_φ, κ_{W,c_0}+ℤ)` is bounded by the same quantity.  Two forced consequences of (K-TAIL), each proved: **(i)** in the D9(a) kink class it is equivalent to "no charge lies outside the core" (`\|\|𝒬_{c_0}φ − Q̂_{W,c_0}φ\|\| ≤ 2C_Kλ̃^{d_W}/(1−λ̃)` for every finite `W ⊇ K` with `c_0 ∈ W`), and it forces both tail vacua to have **sharp on-site charge**: `ω_γ((S^z_x − s_γ)²) = 0`, equivalently `ω_γ(Π_x^{(s_γ)}) = 1` for the on-site spectral projection `Π_x^{(m)}` of `S^z_x`, at every site — hence `±s ∈ spec S^z`, so a spin-1 chain with calibration `s = 1/2` admits no (K-TAIL) kink state.  When in addition `s_γ` is a **simple** eigenvalue of `S^z` (as in the standard spin-`S` register `d = 2s+1`) this makes `ω_γ` the `χ=1` fully polarised `S^z`-product state; under H-MQG(1)--(2) alone it does **not**, and the unqualified `χ=1` form is REFUTED (ace-ld-r3 F1).  **(ii)** With `t`-independent `(K, C_K, λ̃)` it is **jointly unsatisfiable with D18(AD3)'s clause that the free leg charge leaves the window** — so no state carrying an escaping leg of nonzero charge satisfies it with `t`-independent constants, `q_L ≠ q_T` is unavailable within one D18 conserved-charge sector, and on states that do satisfy it with `ε_Q = 0` and `t`-uniform data the ordered wall displacement is `δx = 0`.  NOT claimed: that (AD3-ex-ε) supplies `theory/ansatz-scattering.md` ⟨1⟩7.⟨2⟩2's cross-term step (it does not — the hypothesis fails on that entire class; the r2 claim to the contrary is RETRACTED); the exact fixed-`W` (AD3-ex); D18(AD3)'s weak-\* clause or M-INDEX-spec's reduction clause; the `χ=1` product form of the tail vacua under H-MQG alone; any statement about generic injective-MPS vacua; any infinite-volume proof of (K-TAIL) or (K-Q) on any model; the existence of a sector-wide conserved charge operator (only the limit vector on a (K-TAIL) state is constructed; M-INDEX-LA-strong is REFUTED and is not contradicted, its refuting state having polynomially decaying deviations and lying outside the (K-TAIL) class; M-INDEX-LA-folium, the infinite-volume route to (K-Q)'s `t`-uniformity, is CONJECTURE).  The hypothesis class is inhabited: D16's exact zero-energy sector states satisfy (K-Q) exactly and (K-TAIL) at rate `λ̃ = q = Δ−√(Δ²−1)` — independently verified by full-`2^L` exact diagonalisation at `L = 12`, `\|\|D_xφ\|\| = 4.356e-02, 9.092e-03, 1.898e-03, 3.960e-04, 8.266e-05` with per-site ratios `0.20871` on both sides and `C_K = 0.2087`, in the ℤ₂-image of D13(a)'s orientation. | **PROVED** (conditional) (pending L6 loop) | D13, D26, M-INDEX-fin | theory/ace-ld.md ⟨1⟩4 | theory/checks/ace_ld_check.py LD-C7 (green exit 0; --red exit 1, RED-OK 21/21, exit paths tabulated in the shard §5 and re-run independently in ace-ld-r3.md n3).  Gates (b)--(c) certify the conclusion's λ̃^{d_W} rate (defects 4.45e-02 … 4.05e-04, ratios 0.2089/0.2087/0.2083 against q = 0.208712); gate (e) certifies the HYPOTHESIS (K-TAIL) itself site-by-site, and by Cauchy--Schwarz on the self-adjoint D_x the on-site clause is equivalent to the full same-side clause, so (e) certifies (K-TAIL) in full (ace-ld-r3.md n1).  No gate bears on (K-Q), on the infinite-volume statement, or on the sharp-charge corollary, which is exact algebra. |
| ACE-LD-obst-prime | Under H-MQG(1)--(3), D26(INT), and the D27 setting (a D17 vector `Ψ`, a cut `c_0`, a padded exhaustion `W_m = [a_m,b_m] ↑ ℤ` containing `c_0`) with D27(LR1)--(LR2) but **not** D27(LR3), assume **(M-ESC)**: `θ_{tr} := liminf_m \|ω^+_{W_m}(𝔛_{W_m}) − ω^-_{W_m}(𝔛_{W_m})\|/\|W_m\| > 0`.  Then **(a)** `\|Σ_ν ν p_{W_m}(ν)\| ≥ 2sθ_{tr}\|W_m\|(1−o(1)) → ∞`; **(b)** D27(LR3) FAILS: `sup_m Σ_{\|ν\|>M}(1+\|ν\|)p_{W_m}(ν) = ∞` for every `M`; **(c)** D27's ordered wall expectation `δx` is undefined along that exhaustion, its defining differences diverging linearly at rate `≥ θ_{tr}` per window site.  **Positive form (NOT a contrapositive):** the same step gives directly that on any (LR) state the mean wall transport is uniformly bounded, `sup_m \|ω^+_{W_m}(𝔛_{W_m}) − ω^-_{W_m}(𝔛_{W_m})\| ≤ (M_0+1)/(2s)`, where `M_0` is any threshold with `sup_m Σ_{\|ν\|>M_0}(1+\|ν\|)p_{W_m}(ν) ≤ 1`; in particular `θ_{tr} = 0`.  Disclosure: this is the quantitative form of D27's own existence corollary, and the genuine addition is the `M_0` tightness route — strictly stronger than that corollary, which delivers convergence along the full sequence only under D27's optional convenience clause and otherwise only along an (LR3) subsequence, whereas this bound is a `sup` over **all** `m` with no subsequence and no convenience clause.  Mechanism (mean escape gives `θ_{tr} = p_tr`) uses only the mean tail densities of H-MQG(2)/D13(a): no variance hypothesis, no `(E-TAIL)`, `(V-ch)` or `(V-in)`, no `σ_L ≠ σ_T`, no channel projections, no wave operators, no D28.  The first-moment identity is consumed at the level of `theory/memory-index.md` ⟨1⟩7.⟨2⟩1--⟨2⟩2, whose leaf justifications carry only D27(LR1)--(LR2) and (IDX.1) — not the (LR3)-conditional statement of M-INDEX-spec — so the proof by contradiction against (LR3) is non-circular.  NOT claimed: any statement about D16 or any confined-kink class.  There `θ_{tr} = 0`, but only on named conditionals: every state in the closed span of D16's K1--K2 family is exactly stationary (K1+K2 PROVED; exhaustion of `ker H_kink` by that family is K4, CONJECTURE), and the D17 kink--magnon bound `\|δx\| ≤ ⟨N_T⟩/s` is M-quant-G's conclusion, which is PROVED **conditional on H-AD-G, i.e. on D18(AD1)--(AD4) for that vector** — open for D16 (bd `tns-d51`; `AD3-ex` is CONJECTURE).  Note that D18(AD3) is jointly unsatisfiable with (K-TAIL) (row ACE-LD-eps), so this `θ_{tr} = 0` fence and the ε-theorem concern **disjoint** state classes: a kink--magnon D17 packet under H-AD-G, versus a magnon-free (K-TAIL) sector state.  LD-C7(a) certifies only the 13 sector ground energies at `L = 12`.  The bd `tns-xf4` lane is NOT pre-empted.  Also NOT claimed: any statement about D28's packet class as such (D28(4) constrains only `v_M − v_K`, and D28's class contains `θ_{tr} = 0` members); mass-defectiveness of weak limits (first-moment divergence only); the two-atom law as a theorem (numerically exhibited only).  **No model or state realising `(M-ESC)` is exhibited anywhere in this corpus** — independently confirmed by the parallel lane (`theory/verdicts/lr-d16-r1.md` M2(b)1, `theory/verdicts/lr-d16-r2.md` M4(b)3) — so this row constrains a hypothesis class, and until a witness exists it makes no clause of any class theorem necessary. | **PROVED** (conditional) (pending L6 loop) | D13, D17, D26, D27, M-INDEX-fin | theory/ace-ld.md ⟨1⟩5 | theory/checks/ace_ld_check.py LD-C5 — incoming concentration ≤ 3.2e-6 at every window and the exact two-atom TPM support {ν = 0, ν = −\|W\|} including the ν = 0 atom, with weights matching the independently measured \|r\|² = 0.2704, \|t\|² = 0.7296, on a one-particle barrier model; its identity and tail-floor gates are disclosed consequences of those facts, not independent evidence.  LD-C6 — kink+magnon bounded-transport contrast on the D16 battery at the fixed protocol time t_+ = 4 (support: mass at \|ν\| > 3 below 9.1e-13; first moment ≤ 0.453).  Caveats recorded per ace-ld-r3.md M3: LD-C6's first-moment gate is reached by no registered mutation (the support gate shadows it) and its threshold 1.0 is tuned to t_+ = 4 — the same green model at t_+ = 20 gives 1.0712 and the gate fires.  **Neither certificate exhibits an (M-ESC) state, and no gate bears on claims (a)--(c), which are proved, not tested.** |
| LD-ID | Under H-MQG(1)--(2), for every finite window `W = [a,b]` with `c_0 ∈ W`, and with the step density `s_{γ_{c_0}}(x) := +s` for `x ≤ c_0` and `−s` for `x > c_0`: `Q̂_{W,c_0} = Σ_{x∈W}(S^z_x − s_{γ_{c_0}}(x))` **exactly** — no offset and no factor.  Consequently, on any state on which the increasing-window limit exists — in particular on every (K-TAIL) state of row ACE-LD-eps, where `𝒬_{c_0}φ := lim_n Q̂_{W_n,c_0}φ` exists and is exhaustion-independent — `𝒬_{c_0} = Σ_{x∈ℤ}(S^z_x − s_{γ_{c_0}}(x)) = 2s(X_1 − c_0)`: the relative window charge is **not a new object** but the vector-valued lift of D13(c)'s first-moment wall coordinate `X_1`, which D13(c)'s trap paragraph records as exactly conserved.  Two corollaries, each on its own named hypotheses.  **(i)** If `Ψ_t` carries an outgoing free leg of charge `q_leg ≠ 0` that has left `W` in the sense of D18(AD3), then `\|\|𝒬_{c_0}Ψ_t − Q̂_{W,c_0}Ψ_t\|\| ≥ \|Σ_{x∉W} ω_{Ψ_t}(D_x)\| → \|q_leg\|`, while (K-TAIL) with `t`-independent `(K, C_K, λ̃)` bounds the same quantity by `2C_Kλ̃^{d_W}/(1−λ̃)` uniformly in `t`; choosing `d_W` with `2C_Kλ̃^{d_W}/(1−λ̃) < \|q_leg\|` is a contradiction.  Hence **no state in D18(AD3)'s escaping-leg class satisfies (K-TAIL) with `t`-independent constants**, and `q_L ≠ q_T` is unavailable within one D18 conserved-charge sector.  **(ii)** Under (K-Q) with `ε_Q = 0` and `t`-uniform (K-TAIL) data, `q_φ` is a `t`-independent eigenvalue of the conserved `𝒬_{c_0}`, and D27's ordered wall expectation obeys `\|δx\| ≤ s^{-1} lim_m 2C_Kλ̃^{d_{W_m}}/(1−λ̃) = 0`: on that class the ordered memory is exactly zero — D13(c)'s trap in windowed dress.  The window-charge identity is unconditional under H-MQG(1)--(2); the `𝒬_{c_0}` identification additionally requires the increasing-window limit to exist; (i) additionally requires D18(AD3) and `t`-independent (K-TAIL) constants; (ii) additionally requires (K-Q) at `ε_Q = 0`, `t`-uniform data, and D27's definition of `δx`.  NOT claimed: that (i) or (ii) holds outside those hypotheses; which regime any given model occupies; the existence of `𝒬_{c_0}` as a sector-wide operator — only the limit VECTOR on a (K-TAIL) state is constructed, so M-INDEX-LA-strong (REFUTED) is respected and not contradicted, its refuting state having polynomially decaying deviations and lying outside the (K-TAIL) class. | **PROVED** (the identity unconditionally; corollaries (i),(ii) conditional exactly as stated in the cell) (pending L6 loop) | D13, D18, D27, M-INDEX-fin | theory/ace-ld.md ⟨1⟩4.⟨2⟩7 | No gate is required: the identity is exact algebra.  Independently re-verified in ace-ld-r3.md §0(i) on all 2^12 basis states of the D16 battery over six windows (max\|LHS−RHS\| = 0.000e+00), in ace-ld-r2.md §0(i) symbolically and on a 201-site lattice, and reached independently by the parallel lane (theory/verdicts/lr-d16-r1.md §2 item 1).  Corollary (i)'s quantitative witness re-measured in ace-ld-r3.md M1(b): \|\|(Q̂_{W'}−Q̂_W)φ\|\| = 2s at every padding for an escaped leg inside the annulus. |
| ACE-LD-sharp | Under H-MQG(1)--(2), let `φ` be a unit vector whose state `ω_φ` lies in the D9(a) kink sector `𝒦_{αβ}` and satisfies **(K-TAIL)** with core `K` and constants `C_K, λ̃` (row ACE-LD-eps).  Then both tail vacua have **sharp on-site charge**: for `γ ∈ {α, β}` and every site `x`, `ω_γ((S^z_x − s_γ)²) = 0`, equivalently `ω_γ(Π_x^{(s_γ)}) = 1` where `Π_x^{(m)}` is the on-site spectral projection of `S^z_x` at eigenvalue `m`.  Hence the tail density is an on-site **eigenvalue**: `s_α = +s ∈ spec S^z` and `s_β = −s ∈ spec S^z`.  Proof inputs, all named: D9(a) supplies the weak-\* tail relaxation `ω_φ(τ_x(O)) → ω_γ(O)` for `O ∈ 𝔄_loc` (no extra relaxation hypothesis is needed); (K-TAIL) at `x = x'` drives `ω_φ(D_x²) ≤ C_K²λ̃^{2dist(x,K)} → 0`; Cauchy--Schwarz on `(S^z_x − s_γ)` pins the on-site spectral weights; D2(a) gives translation invariance of `ω_γ`.  **Concrete corollary, by arithmetic alone: a spin-1 chain with calibration `s = 1/2` admits NO (K-TAIL) kink state, since `±1/2 ∉ spec S^z = {−1, 0, 1}`.**  Sharp on-site charge means zero on-site charge variance and therefore excludes every vacuum with nonzero on-site charge variance, in particular generic injective-MPS vacua — which is the scope boundary of row ACE-LD-eps.  NOT claimed: that the tail vacua are `χ=1` fully polarised `S^z`-product states.  That stronger form needs `s_γ` to be a **simple** eigenvalue of `S^z` — true in the standard spin-`S` register `d = 2s+1`, and true in D16, but not implied by H-MQG(1)--(2), D2(a) or D26(INT), all of which admit degenerate on-site charge eigenspaces (`notation.md`'s `d = 2s+1` gloss is explicitly fenced as the fully polarised special case and not a constraint).  Under H-MQG(1)--(2) alone the `χ=1` form is **REFUTED**: with on-site space `ℂ² ⊗ ℂ³` and `S^z := σ^z/2 ⊗ 𝟙_3` (so `spec S^z = {±1/2}`, each of multiplicity 3, and `e^{2πiS^z} = −𝟙`, so D26(INT) holds with `κ = 1/2`), the vacua `ω_α = ⊗_x(\|↑⟩⟨↑\| ⊗ ϱ_{AKLT})` and `ω_β = ⊗_x(\|↓⟩⟨↓\| ⊗ ϱ_{AKLT})` are injective MPS of bond dimension `χ = 2` (bond Schmidt spectrum `(1/2, 1/2)`, transfer gap `1/3`), covariant for `G = U(1) ⋊ ℤ₂` with `ω_α(S^z) = +1/2 = s = −ω_β(S^z)`; the sharp domain wall in the `ℂ²` factor lies in `𝒦_{αβ}` and has `D_xφ = 0` at every site, so it satisfies (K-TAIL) with `C_K = 0` while its tail vacua are not product states (ace-ld-r3 F1). | **PROVED** (pending L6 loop) | D2(a), D9(a), D13, D26 | theory/ace-ld.md ⟨1⟩4.⟨2⟩9(b), once ⟨3⟩3's χ=1 clause is replaced by the sharp-charge clause per ace-ld-r3 F1 | theory/checks/ace_ld_check.py LD-C7(e) certifies the HYPOTHESIS (K-TAIL) on the D16 instance (\|\|D_xφ\|\| per-site ratios 0.20871 on both sides, C_K = 0.209, red-armed by --red-c7-orientation at C_K = 2525); the conclusion is exact algebra and needs no gate.  The refuting counterexample to the χ=1 form is verified numerically in ace-ld-r3.md F1(b). |

*(Register/deps notes: row 1 carries NO depends-on — ACE-LD-abs is
unconditional given its ASSUME, per r1 verdict m5; M-INDEX-fin enters
only the instance rows.  M-INDEX-spec is on no row — with the m4
sub-step qualification, carried inside the obst-prime cell: the
first-moment identity is consumed at the level of MI ⟨1⟩7.⟨2⟩1--⟨2⟩2,
whose leaf justifications carry only D27(LR1)--(LR2) and (IDX.1), so no
(LR3) circularity arises.  Statuses are bare L5 values at merge; every
qualifier lives in prose.  r4 delta notes, for the r4 critic — NOT
edits to the cells: (i) cell (D)'s proved-in condition "once ⟨3⟩3's
χ=1 clause is replaced …" is DISCHARGED by this revision (⟨1⟩4.⟨2⟩9(b)
now proves the sharp-charge form); (ii) cell (B)'s tested-in caveat
sentence ("Caveats recorded per ace-ld-r3 M3 …") describes the r3
checker — in r4 the first-moment gate is reached (`--red-c6-moving`,
exit path `12.4024` at `|W|=17`), the support gate is armed by
`--red-c6-weaktransit`, and the bound is `1.2`, set above the recorded
`t_+`-sweep maximum `1.0712` (`t_+=20`, `W=[3,8]`); (iii) cell (A)'s
tested-in "RED-OK 21/21" likewise records the r3 run — the r4 run is
green exit 0, `--red` exit 1 RED-OK **23/23**.  The r4 critic is asked
to bless updated wording for those two tested-in sentences; the cells
are otherwise merge-ready as they stand.)*

**MP-2. Prose append to the `AD3-ex` row** (status stays **CONJECTURE**;
rewritten per r2 verdict M6(c) and §8(E) — the r2 draft's "the exact
display is FALSE at every fixed `W`" was measured on a magnon-free zero
mode that is not an (AD3-ex) vector and is withdrawn):

> r3 update (theory/ace-ld.md): D16's exact kink states are never
> `Q̂_{W,c_0}` eigenvectors at finite `W` — the defect is
> `min_q||(Q̂_W−q)Ψ|| = 4.45e-02 … 4.05e-04` decaying as `q^{d_W}`
> (LD-C7) — so D18(AD3)'s "remaining local state is a kink charge
> eigenstate" clause can hold at fixed `W` only in ε-form.  No in-class
> (AD3-ex) vector is exhibited; **the exact display is not refuted, it
> is unavailable.**  Regime split (by escaped charge, r2 §8(E)):
> (AD3-ex) at fixed `W` asserts that the channel state becomes a `Q̂_W`
> eigenvector while the leg charge sits OUTSIDE `W`.  Any route through
> tail clustering proves the opposite regime: (K-TAIL) forces the
> escaped charge to zero, whereupon both channels carry the same
> conserved charge and `δx = 0` (ace-ld r2 F1; ace-ld.md ⟨1⟩4.⟨2⟩7).
> So the sharpness of `Q̂_W` on a channel state must come from the
> wall's own localisation at fixed `W` given an escaped leg, and no
> route to that exists in the corpus.  The ε-version (AD3-ex-ε) is
> PROVED conditionally (row ACE-LD-eps) but on the leg-free corner
> ONLY; it does NOT supply AS ⟨1⟩7.⟨2⟩2's cross-term step.  r1's
> proposed discharge under (E-TAIL)∧(V-ch) stays withdrawn (ace-ld-r1
> F1).

**MP-3. Gloss replacement in AS ⟨1⟩7's ASSUME block** (replacing the
sentence "The missing derivation is recorded as named lemma ACE-LD (see
HONEST STATUS): …" up to "…no step of this shard supplies.").  *(r3:
clause (ii) of the r2 draft — the ordered-limit supply claim — is
**WITHDRAWN as FALSE** per r2 F1 and is replaced by the honest
statement; nothing else may reintroduce it.)*

> The named lemma **ACE-LD** (theory/ace-ld.md, r3) prices this
> hypothesis as follows.  (i) D16's exact kink states are never `Q̂_W`
> eigenvectors at finite `W` (defect `min_q||(Q̂_W−q)Ψ|| ∼ q^{d_W} > 0`,
> LD-C7), so (AD3-ex)'s eigenstate clause can hold at fixed `W` only in
> ε-form; no in-class (AD3-ex) vector is exhibited, and the exact
> display is not refuted but unavailable.  (ii) The ε-form is PROVED
> under (K-TAIL)+(K-Q) (row ACE-LD-eps) but is a theorem about the
> OPPOSITE regime: `𝒬_{c_0} = 2s(X_1−c_0)` is the conserved D13(c)
> charge, (K-TAIL) is "no charge escaped the core", and it is jointly
> unsatisfiable with (AD3-ex)'s escaping-leg premise — **no step of
> ace-ld supplies the cross-term vanishing this ASSUME consumes** (the
> r2 claim to the contrary is retracted, ace-ld-r2 F1).  What ace-ld
> does offer is LEMMA LD-MONO (⟨1⟩4.⟨2⟩7): an assumed ε-form (AD3-ex)
> at one core-containing window propagates, using annulus clustering
> only, to every larger window `W'` **whose annulus `W'∖W` carries no
> escaped charge — equivalently, every `W'` the leg has already passed
> beyond** — up to a uniform `2C_Kλ̃^{d_W}/(1−λ̃)`; at the first `W'`
> that reaches the leg the difference is exactly the leg charge (LD-ID
> ⟨3⟩3), so the transport is not available past that window.  *(r4
> repair, ace-ld-r3 M1: the r3 draft of this clause dropped the
> quantifier and was refuted by the shard's own LD-ID ⟨3⟩3 — measured
> `||(Q̂_{W'}−Q̂_W)φ|| = 2s` at every padding with the leg inside the
> annulus, against an asserted bound down to `4.25e-22`.  The lemma as
> ASSUMEd was always correct; only the compression was false.)*
> (iii) What would be
> supplied on the leg-free corner is the KINK-eigenstate reading of
> D18(AD3) in ε-approximate norm form; the weak-\* reading consumed by
> M-INDEX-spec's reduction clause is NOT supplied and that row's
> adjudicated scoping is untouched.  (iv) On packet classes whose kink
> transits with mean weight `θ_{tr}>0`, D27(LR3) — hence the T1
> outcome-measure hypothesis of ACE.3 — fails (ACE-LD-obst-prime);
> D28(4) itself does NOT force transit (it constrains only `v_M−v_K`),
> and D16 lies in the confined complement (K1+K2 stationarity + the
> M-quant-G bound; K4 remains CONJECTURE).  *(Also flagged: ⟨2⟩1's
> `ν = q_T − q_in` orientation is opposite to the frozen
> `ν = q_- − q_+` of notation.md/MI ⟨1⟩5.⟨2⟩3; only `|ν|` is consumed
> downstream, but the display should be reconciled — ace-ld-r1 NOTE
> n1.)*

**MP-4. `notation.md` additions** (collision-checked against the frozen
table; r2 m3/n2 applied; r4: **string-anchored** per ace-ld-r3 §8(E)
precondition 2 and briefs/ace-ld-repair-r4.md — line numbers go stale
between merges, the anchors below are unique strings in the current
`notation.md`.  This proposal is a MERGE PRECONDITION of MP-1: it binds
exactly the five symbols the ace-ld-r3 §8(E) audit found unbound —
`𝒬_{c_0}`, `(K-TAIL)`, `(K-Q)`, `(M-ESC)`, `θ_{tr}` — and it must merge
with or before the MP-1 rows, which use them.  All other symbols the
MP-1 cells use are either already bound — per the §8(E) audit: `S^z`,
`s`, `s_α`, `s_β`, `𝔛_W`, `δx`, `X_1`, `Q̂_{W,c_0}` (= `Q̂_{W,c}` row),
`κ_{W,c_0}`, `λ̃`, `𝒦_{αβ}`, `ω_α`, `ω_β`, `τ_x`, `𝔄_loc`,
`p_{W_m}(ν)`, `ω^±_{W_m}`, `𝒟_{W,t_-}`, `N_T`, `⟨N_T⟩`, `Δ`, `q`,
`H_kink`, `χ`, `spec S^z`, `κ`, `H-MQG(1)--(3)` — or defined inline in
the cells themselves (`K = [ℓ,r]`, `d_W`, `D_x`, `C_K`, `ε_Q`, `q_φ`,
`M_0`, `Π_x^{(m)}`, `ϱ_{AKLT}`, `S_{NR}`), so no further `notation.md`
row is created and no existing row is touched.):

**Insertion point (string anchor):** in the `notation.md` table headed
**"ML4 / ML5 / M-quant (added at the freeze with the summit shards)"**,
insert the three rows below immediately AFTER the row whose Symbol cell
is `` `δx` (asymptotic) `` (Meaning beginning "the D27-defined ordered
asymptotic value of D13(a)'s observable") and immediately BEFORE the row
whose Symbol cell is `` `Γ_K`, `Γ_{M,γ}` `` — keeping the D27-family
rows adjacent.

| `𝒬_{c_0}φ` | the relative-charge limit vector `lim_n Q̂_{W_n,c_0}φ` — the vector-valued lift of D13(c)'s conserved `X_1`: `𝒬_{c_0} = 2s(X_1−c_0)`; exists on every (K-TAIL) state, exhaustion-independent (a vector on a state, not a sector operator; M-INDEX-LA-strong untouched) | theory/ace-ld.md ⟨1⟩4.⟨2⟩2, ⟨2⟩7 (THEOREM LD-ID) |
| `(K-TAIL)`, `(K-Q)` | confined-core exponential tail decay (core `K`, rate `λ̃`, on-site deviations `D_x`; the off-diagonal clause is equivalent to the on-site clause by Cauchy--Schwarz, ace-ld-r3 n1); sharp relative charge (`\|\|𝒬_{c_0}φ−q_φφ\|\|≤ε_Q`) | theory/ace-ld.md §0 (THEOREM ACE-LD-ε) |
| `(M-ESC)`, `θ_{tr}` | mean-tail-transport hypothesis `liminf_m \|ω^+−ω^-\|(𝔛_{W_m})/\|W_m\| = θ_{tr} > 0`.  *(Merged name `θ_{tr}`, r2 n2: the shard-local `θ` collides with the frozen twist variable `θ` of the `μ_∞^α` row — the vacuum charge law `(2π)^{-1}∫e^{-iθν}\|tr(V_θr)\|²dθ`, in the same table as this insertion; the merged symbol carries the subscript to avoid the overload.)* | theory/ace-ld.md §0, ⟨1⟩5 |

**MP-5. L2 split (endorsing r1 m7 / r2 m8, outside this lane).**  Move §3
(⟨1⟩5, ACE-LD-obst′) to a shard `theory/ace-ld-obst.md` once the loop
converges; it has a disjoint hypothesis set from ⟨1⟩4 and the split
restores both files to the L2 band.

**MP-6. Note to bd `tns-xf4`** (justification replaced per r2 M5(c);
strengthened per r2 §7 item 3; r4: re-cited per ace-ld-r3 m5 — the
lr-d16-r1 citations are superseded by `theory/verdicts/lr-d16-r2.md`,
the composition now follows DIRECTLY from lr-d16's repaired THEOREM
(LRD-3), and the no-witness disclosure travels with the constraint —
transmit a CONSTRAINT, attributed to the cross-lane composition, not
this shard's own theorem):

> ACE-LD-obst′ is scoped to `θ_{tr} > 0`.  D16 is outside its class:
> every state in the closed span of the K1--K2 family is exactly
> stationary (K1+K2 PROVED; `ker H_kink` exhaustion is K4, CONJECTURE),
> and D17 kink--magnon packets have mean wall transport bounded by
> `⟨N_T⟩/s` — M-quant-G's conclusion, PROVED **conditional on H-AD-G,
> i.e. on D18(AD1)--(AD4) for that vector**, open for D16 (bd
> `tns-d51`; `AD3-ex` is CONJECTURE) — so `θ_{tr} = 0`; LD-C7(a)
> certifies only the sector ground energies at `L=12`.  Usable hint:
> (LR3) for D16 hinges on kink confinement, not on magnon dynamics;
> (K-TAIL)+(K-Q) give the fixed-window ε-eigenvector structure (LD.4)
> that an (LR) proof can consume — noting that D18(AD3) is jointly
> unsatisfiable with (K-TAIL) (ace-ld LD-ID ⟨3⟩3), so the
> `θ_{tr} = 0` fence and the ε-theorems concern disjoint state
> classes.  **Usable constraint (cross-lane composition — attributed
> to the composition of the ace-ld and lr-d16 critic passes, proved in
> neither shard alone; re-cited r4 per ace-ld-r3 m5):
> `(M-ESC) ⟹ ¬(NR)`, now DIRECT — `theory/lr-d16.md` ⟨1⟩5.⟨2⟩7
> THEOREM (LRD-3), in its repaired form (`theory/verdicts/lr-d16-r2.md`;
> `(NR)` the repaired two-clause `sup_m` statement), proves
> `(NR) ⟹ D27(LR3)` with tail bound `2S_{NR}/M`, and ACE-LD-obst′(b)
> proves `(M-ESC) ⟹ ¬D27(LR3)`; no appeal to lr-d16 ⟨1⟩5.⟨2⟩4's
> monotonicity remark is needed (the earlier route through it is
> superseded).  Any (LR) route for D16 through the repaired (NR) is
> therefore confined to the `θ_{tr} = 0` class from the start.
> Disclosure, travelling with the constraint (ace-ld-r2 m7; lr-d16-r1
> M2(b)1; lr-d16-r2 M4(b)3): no model or state realising `(M-ESC)` is
> exhibited anywhere in this corpus — a conditional with an empty
> antecedent constrains nothing until a witness exists.**
