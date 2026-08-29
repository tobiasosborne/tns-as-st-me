<!-- ROLE: adversarial critic verdict, round 2, on theory/ace-ld.md,
     theory/ace-ld-r2-response.md and theory/checks/ace_ld_check.py.
     Protocol: briefs/critic-protocol.md (incl. Standing checker obligations).
     Brief: briefs/ace-ld-critic-r2.md.  Prior: theory/verdicts/ace-ld-r1.md
     FAIL(F1,M1-M6).  Lane: this file only.  Nothing here edits the shard,
     definitions.md, notation.md or claims/CLAIMS.md; no merge is authorised
     by this file; no commit. -->

# ACE-LD r2 — critic verdict

**Verdict: FAIL(F1, M1, M2, M3, M4, M5, M6).**

Every number below was produced by me, by an independent route, not read off
the shard.  Scripts live in the session scratchpad and are named inline.

**Headline.**  The reroute is a real improvement and most of it survives.  The
`(E-TAIL)/(V-ch)` route is genuinely gone (grep-clean), the eighteen r1
dispositions are almost all honest, `ACE-LD-abs`/`-nec` are untouched and
still correct, the r2 §5 spec/code lockstep is exact to the last digit, and
`--red-coset` is now a true coset break distinct from `--red-gap` in mechanism,
not merely in registered pattern.  **THEOREM ACE-LD-ε is correct and its class
is genuinely inhabited: I reproduced the D16 instantiation from scratch and
verified (K-TAIL) directly — `‖D_xφ‖` falls by exactly `0.2087` per site, four
octaves running.**  r1's FATAL is answered for the theorem.

What fails is again the *reach*, and it fails for a reason that is structural,
not repairable by rewording.  `𝒬_{c_0} := lim_n Q̂_{W_n,c_0}` is **identically
the exactly conserved regularised total charge of the frozen D13(c) trap
paragraph**: `Q̂_{W,c_0} = Σ_{x∈W}(S^z_x − s_{γ_{c_0}}(x))`, so
`𝒬_{c_0} = 2s(X_1 − c_0)`.  (K-TAIL) is therefore exactly the hypothesis *no
charge has escaped the core*, and D18(AD3) — the clause (AD3-ex) is a piece of
— is exactly the hypothesis *the leg charge has left the window*.  They are
mutually exclusive.  Consequently ACE-LD-ε-t/-x have **no instance among the
channel states AS ⟨1⟩7.⟨2⟩2 is about**, and on the states where they do apply
they force `δx = 0` — no memory.  The round's advertised bridge (§0 item 3,
⟨1⟩4.⟨2⟩7, MP-1's `ACE-LD-eps` row, MP-3(ii)) is false, and MP-3 would write
it into `theory/ansatz-scattering.md`.

`ACE-LD-obst′` is **correct**; I re-derived it in full.  Its contrapositive is
the valuable part, it is more general than the shard states, and the shard
states it with the wrong quantifier.

---

## 0. What I recomputed first

**(i) The window-charge identity, from the frozen definitions.**  With D13(a)
`𝔛_W = a−1+(1/2s)Σ_{x=a}^b(S^z_x+s)` and `Q̂_{W,c_0}=2s(𝔛_W−c_0)`
(MI ⟨1⟩1.⟨2⟩2), put `s_{γ_{c_0}}(x) := +s` for `x ≤ c_0`, `−s` for `x > c_0`.
Then `Σ_{x∈W}s_{γ_{c_0}}(x) = s(2c_0−a−b+1)`, hence

> `Q̂_{W,c_0} = Σ_{x∈W}S^z_x + s(a+b−1−2c_0) = Σ_{x∈W}\big(S^z_x − s_{γ_{c_0}}(x)\big)`
> **exactly** — no offset, no factor.

(Checked symbolically and on a 201-site lattice, `ledger.py`: both sides `0.0`.
The parallel lane's critic reached the same identity independently —
`theory/verdicts/lr-d16-r1.md` §2 item 1.)  Therefore

> `𝒬_{c_0} = Σ_{x∈ℤ}(S^z_x − s_{γ_{c_0}}(x)) = 2s\,(X_1 − c_0)`,

with `X_1` the first-moment wall coordinate **frozen in D13(c)** and in
`notation.md` line 211.  This identification is nowhere in the shard and it is
what F1 turns on.

**(ii) The D16 instantiation, rebuilt from scratch** (`d16.py`, my own sector
construction, my own `Q̂_W`): flat band `max_sector|E_0| = 8.23e-17` across all
13 sectors; kernel dimension exactly `13 = L+1` with a uniform gap `1.5341`
above it; half-filled ground state has overlap `1 − 6e-16` with the q-deformed
kink `Σ_{|S|=n}q^{Σ_{i∈S}i}|S⟩`; window defects and coset

| `W` | `⟨Q̂_W⟩` | `min_q‖(Q̂_W−q)Ψ‖` | ratio |
|---|---|---|---|
| `[4,7]` | `−0.99801996` | `4.453450e-02` | — |
| `[3,8]` | `−0.99991374` | `9.304727e-03` | `0.208933` |
| `[2,9]` | `−0.99999624` | `1.941946e-03` | `0.208705` |
| `[1,10]`| `−0.99999984` | `4.045736e-04` | `0.208334` |

against `q = Δ−√(Δ²−1) = 0.20871215`.  **The checker's LD-C7 numbers are
right; ⟨1⟩4.⟨2⟩9(c)'s are not** (see m1).

**(iii) (K-TAIL) itself, which no gate tests** (`d16b.py`).  With core
`K=[4,7]` and the tail assignment of the *actual* model (↓ at `−∞`, ↑ at
`+∞`), the one-site deviations are

`‖D_xφ‖ = 4.36e-02, 9.09e-03, 1.90e-03, 3.96e-04, 8.27e-05` at
`dist(x,K)=1,2,3,4,5` on the right, and `1.90e-03, 3.96e-04, 8.27e-05` at
`dist=1,2,3` on the left — **successive ratios `0.2087` every single step,
both sides**.  So (K-TAIL) holds on the D16 sector state at rate exactly `q`,
and the shard's inhabitation claim is **true**.  It is not, however, what
LD-C7 certifies (see n5), and it holds only in the ℤ₂-flipped orientation
(m2).

---

## 1. FATAL

### F1 (FATAL) — (K-TAIL) is the hypothesis "no charge escaped"; D18(AD3) is the hypothesis "the leg charge escaped".  ACE-LD-ε-t/-x therefore have no instance on the AS ⟨1⟩7 channel class, and where they do apply they force `δx = 0`

**(a) Location.**  `theory/ace-ld.md` §0 item 3 (the sentence "it is what
`ansatz-scattering.md` ⟨1⟩7.⟨2⟩2 consumes in the ordered limit"); §0 COROLLARY
ACE-LD-ε-t ASSUME (the `t`-independent `(K,C_K,λ̃)` clause); §0 COROLLARY
ACE-LD-ε-x ASSUME (`q_L ≠ q_T`); **⟨1⟩4.⟨2⟩7** (the whole step); ⟨1⟩4.⟨2⟩8
first bullet; MERGE PROPOSALS **MP-1** row `ACE-LD-eps` ("plus ordered-limit
inter-channel cross-term vanishing … — the input AS ⟨1⟩7.⟨2⟩2 consumes";
"Compatible with D27(LR3)"); **MP-3(ii)**, which is the text destined for
`theory/ansatz-scattering.md`.

**(b) My computation.**  Three parts; each is definition-level.

*(i) (K-TAIL) forbids escaped charge, quantitatively.*  By §0(i) above,
`𝒬_{c_0}φ − Q̂_{W,c_0}φ = Σ_{x∉W}D_xφ`, and ⟨1⟩4.⟨2⟩2(ii) — which I verified
and endorse — bounds that by `2C_Kλ̃^{d_W}/(1−λ̃)`.  So (K-TAIL) says, in
words, *the total charge outside the window is smaller than
`2C_Kλ̃^{d_W}/(1−λ̃)`, for every `W ⊇ K`*.  D18(AD3), frozen, says the
opposite about the very same quantity: "the free leg charge and non-bound
dressing **leave the window** as `t→±∞`", with the leg charges fixed by
H-MQG(5) at `q_in=q_L=−1`, `q_T=+1`.

*(ii) A quantitative refutation on a moving leg* (`ktail_leg.py`,
`ktail_leg2.py`; one magnon over a polarised vacuum, `D_x|y⟩ = −2sδ_{xy}|y⟩`,
free hopping, `K` = 17 sites containing the initial packet, `λ̃ = 0.208712`).
The escaped tail sum `‖Σ_{x∉W}D_xφ_t‖` that ⟨2⟩2(ii) must dominate:

| `t` | `d_W=1` | `d_W=4` | `d_W=16` | `d_W=64` | (K-TAIL) bound `2C_Kλ̃^{d_W}` at `C_K=1` |
|---|---|---|---|---|---|
| `0` | `6.50e-02` | `1.29e-02` | `4.03e-07` | `1.82e-13` | `4.2e-01 … 5.7e-44` |
| `32` | `1.0000` | `1.0000` | `1.0000` | `8.76e-02` | same |
| `128`| `1.0000` | `1.0000` | `1.0000` | `1.0000` | same |

The escaped charge **saturates at exactly `2s = 1`, the leg's charge, at every
padding**.  The minimal admissible `C_K` at the packet centre grows like
`λ̃^{−vt}`: `10^{−0.5}, 10^{+5.0}, 10^{+15.2}, 10^{+37.0}, 10^{+79.8}` at
`t = 0, 8, 16, 32, 64`.  So (K-TAIL) with `t`-independent `(K,C_K,λ̃)` — the
literal hypothesis of ACE-LD-ε-t — is **false for every state carrying an
escaping leg**, which is every state (AD3-ex) is about.

*(iii) The dichotomy, with no escape.*  Since `𝒬_{c_0}` is the same operator
for both channels and (K-Q) at `ε_Q=0` makes `φ_ch` its eigenvector at
`q_ch`, ACE-LD-ε-x's `q_L ≠ q_T` demands the two channels sit at **different
values of the conserved regularised charge**.  D18's preamble fixes *one*
conserved regularised-charge sector, so they cannot.  The explicit ledger
(`ledger.py`, `s=1/2`, `c_0=0`, `W=[−8,8]`, magnon at `x=∓60`):

| channel | configuration | `Q̂_W` | `𝒬_{c_0}` |
|---|---|---|---|
| L (reflected) | wall at `c_0`, magnon in the `α` tail | `0` | `−1` |
| T (transmitted) | wall at `c_0−2`, magnon in the `β` tail | `−2` | `−1` |

Charge conservation *selects* the wall shift `−2`, reproducing
`ΔQ_W = −2`, `ν = +2` (memory-index §0, frozen) — while `𝒬_{c_0} = −1` in
**both**.  Hence: either `q_ch` are the window charges of (AD3-ex), and
(K-Q) holds only with `ε_Q = |𝒬 − q_ch| = 1` in *each* channel, so (LD.4)'s
bound is `≥ 1 = δ` and ACE-LD-ε-x says nothing; or `q_ch := 𝒬`, and then
`q_L = q_T`, `δ = 0`, and ACE-LD-ε-x is vacuous.  Equivalently and most
sharply: `q_L − q_T = (\text{escaped}_T − \text{escaped}_L)` is a nonzero
coset integer, while (K-TAIL) forces both escaped charges below
`2C_Kλ̃^{d_W}/(1−λ̃) < 1/2` for large `d_W`.  Contradiction.

*(iv) Even granting the hypotheses, the conclusion kills the memory.*  (K-Q)
makes `q_φ` an eigenvalue of the **conserved** `𝒬_{c_0}`, hence `t`-independent;
(LD.4) then gives `|⟨Q̂_W⟩_{φ_t} − q_φ| ≤ ε_Q + 2C_Kλ̃^{d_W}/(1−λ̃)` at every
`t`.  Applying this on both time wings and using D27's own
`δx = lim_m[ω^+_{W_m}(𝔛_{W_m}) − ω^-_{W_m}(𝔛_{W_m})] = (2s)^{-1}\lim_m[\dots]`
gives `|δx| ≤ (s)^{-1}(ε_Q + 2C_Kλ̃^{d_W}/(1−λ̃)) → 0`: **on the class where
the ε-version is available with `ε_Q=0`, the ordered memory is exactly zero.**
This is D13(c)'s trap in windowed dress, and it is the reason the shard's
"Compatible with D27(LR3)" is the wrong thing to say: the ε-version is not
merely compatible with (LR3), it is *incompatible with a nonzero `δx`*, i.e.
with the campaign's target `δx = −⟨N_T⟩/s`.  The parallel lane's critic
reached the same mechanism from the other side: "under `U(1)` conservation the
sharp-kink position and the regularised charge are the same variable … on the
`𝒬=𝒬_0` eigenspace the wall position is **pinned** and cannot drift at all"
(`theory/verdicts/lr-d16-r1.md` M2(b)2).

**(c) FIX DEMAND.**  Delete ⟨1⟩4.⟨2⟩7, MP-3(ii) and MP-1's "the input AS
⟨1⟩7.⟨2⟩2 consumes" clause; state in §0, ⟨1⟩4.⟨2⟩8 and HONEST STATUS that
`𝒬_{c_0} = 2s(X_1−c_0)` is D13(c)'s conserved charge, that (K-TAIL) is
equivalent to "no leg charge outside `K`", that it is therefore **jointly
unsatisfiable with D18(AD3)'s escaping-leg clause and with `q_L ≠ q_T`**, and
that on its own class `δx = 0`.

**(d) SURVIVING WEAKER STATEMENT.**  THEOREM ACE-LD-ε and both corollaries
stand **as conditional implications on their own ASSUME blocks** — I found no
error in ⟨1⟩4.⟨2⟩1--⟨2⟩6 and I endorse them (see §5).  What survives of the
downstream story is a *window-monotonicity* lemma, which is worth keeping and
is genuinely new: *under (K-TAIL) restricted to the annulus `W∖K` (no
statement about the far tail), `‖(Q̂_{W'}−Q̂_W)φ‖ ≤ 2C_Kλ̃^{d_W}/(1−λ̃)` for
every `W' ⊇ W ⊇ K`, so (AD3-ex) at **one** window containing the core implies
(AD3-ex) at every larger window up to `2C_Kλ̃^{d_W}/(1−λ̃)`.*  That version has
no anchor at infinity, so it is uniform in `W'` rather than decaying — and
that is exactly the price of dropping the conserved-charge anchor.  It is
compatible with an escaping leg, and it is the honest thing to offer the AS
lane.  Also surviving: ACE-LD-ε as stated is a correct theorem about the
*leg-free* corner, inhabited by D16 sector states (verified, §0(ii)--(iii)).

---

## 2. MAJOR

### M1 (MAJOR) — the χ=1 boundary is *forced*, not conditional, and it is absent from §0, HONEST STATUS and the MP-1 row that would enter the DAG

**(a) Location.**  ⟨1⟩4.⟨2⟩9(b) (the sentence beginning "If the far tails of a
(K-TAIL) state relax to translation-invariant vacua"); §0 THEOREM ACE-LD-ε
(no scope clause at all); §4 HONEST STATUS, "Proved conditionally" bullet;
MP-1 row `ACE-LD-eps`, the "NOT claimed" enumeration; r2-response row M1
("the same boundary is imposed on the new route … ACE-LD-eps row's
not-claimed clause").

**(b) My computation.**  The "if" is not needed and the conclusion is
stronger than stated.  For any `φ` in the D9 kink class `𝒦_{αβ}`, D9(a)
*supplies* weak-\* convergence of the translated restrictions to `ω_α, ω_β`.
`D_x² = τ_x((S^z_0 − s_γ)²)` is a fixed local observable translated, so
(K-TAIL) at `x=x'` gives

`ω_γ((S^z_0−s_γ)²) = \lim_{dist(x,K)→∞} ω_φ(D_x²) ≤ \lim C_K²λ̃^{2\,dist} = 0`,

and then ⟨2⟩9(a)'s own Cauchy--Schwarz argument (which is correct — r1's, and
I re-derived it) forces `ω_γ = ⊗_x|s_γ⟩⟨s_γ|`.  So: **every (K-TAIL) state in
the kink class has `χ=1` `S^z`-product tail vacua — unconditionally, as a
theorem, not as a remark-level scope hedge.**  A second consequence the shard
never states: `ω_γ(Π_x^{(s_γ)})=1` requires `s_γ ∈ spec S^z`, so (K-TAIL) also
forces the tail density to be an *on-site eigenvalue* — spin-1 with `s=1/2` is
excluded by arithmetic alone (this is r1's M1(d) witness, now applying to the
new hypothesis).  I checked the three places this must appear: §0's THEOREM
has no scope clause, HONEST STATUS's conditional bullet has none, and MP-1's
not-claimed enumeration lists five items, **none of which is the χ=1
restriction**.  The r2-response's M1 row asserts that the not-claimed clause
carries it.  It does not.  This is the precise register defect r1 §6
identified — MERGE PROPOSALS not inheriting HONEST STATUS's caution —
recurring on the new route.

**(c) FIX DEMAND.**  State the forced form as a clause of THEOREM ACE-LD-ε's
statement ("(K-TAIL) entails `χ=1` `S^z`-product tail vacua with `s∈spec S^z`;
the theorem is claimed for that corner only"), and repeat it verbatim in
HONEST STATUS and in MP-1's not-claimed enumeration.

**(d) SURVIVING WEAKER STATEMENT.**  ACE-LD-ε is a correct theorem about the
`χ=1`, `s∈spec S^z` corner of the programme — the corner D16 occupies, and,
within this corpus, the only corner it occupies.  Nothing about generic
injective-MPS vacua is claimed or available.

---

### M2 (MAJOR) — ACE-LD-obst′'s contrapositive is stated with the wrong quantifier and is materially weaker than the shard's own ⟨1⟩5.⟨2⟩3

**(a) Location.**  §0 PROPOSITION ACE-LD-obst′, the closing sentence
("Contrapositive: **D27(LR3) forces `θ = 0`** — mean wall transport must be
`o(|W_m|)` on any (LR) state"); ⟨1⟩5.⟨2⟩4's closing sentence; MP-1 row
`ACE-LD-obst-prime` ("Contrapositive: (LR3) forces mean wall transport
`o(|W_m|)`").

**(b) My computation.**  I re-derived (a),(b),(c) and they are correct (§5).
The contrapositive is not.  `(M-ESC)` is a **liminf** hypothesis, so its
literal contrapositive is

> `LR3 ⟹ liminf_m |ω^+−ω^-|(𝔛_{W_m})/|W_m| = 0`,

which permits `|ω^+−ω^-|(𝔛_{W_m}) ≍ |W_m|` along a subsequence and therefore
does **not** give `o(|W_m|)`.  Meanwhile the shard's own ⟨1⟩5.⟨2⟩3 gives far
more than `o(|W_m|)`: choosing `M_0` with
`sup_mΣ_{|ν|>M_0}(1+|ν|)p_{W_m}≤1` yields `sup_m Σ_ν|ν|p_{W_m} ≤ M_0+1`,
hence by ⟨2⟩2

> **`LR3 ⟹ sup_m |ω^+_{W_m}(𝔛_{W_m}) − ω^-_{W_m}(𝔛_{W_m})| ≤ (M_0+1)/(2s) < ∞`**
> — mean wall transport is **`O(1)`, uniformly bounded**, not merely `o(|W_m|)`.

So the sentence is wrong in kind twice over in the same clause: it asserts a
full-sequence `o(·)` that the contrapositive does not deliver, and it reports a
`o(|W_m|)` where the proof delivers `O(1)`.  Since the brief asked whether the
contrapositive is "as general as stated", the answer is: **it is stated both
too strongly (as a contrapositive) and too weakly (as a rate).**

**(c) FIX DEMAND.**  Replace the contrapositive sentence, in all three places,
by: "⟨2⟩3 gives directly: on any (LR) state the mean wall transport is
uniformly bounded, `sup_m|ω^+_{W_m}(𝔛_{W_m})−ω^-_{W_m}(𝔛_{W_m})| ≤ (M_0+1)/(2s)`;
in particular `θ = 0`."  Do not label it a contrapositive.

**(d) SURVIVING WEAKER STATEMENT — actually the stronger one.**  The displayed
`O(1)` bound above is correct, is what should carry the round's negative
content, and is exactly the quantitative form of D27's own one-line existence
corollary.

---

### M3 (MAJOR) — LD-C6, the gate built to satisfy r1's M3 fix demand, is a tautology: `p_W = δ_0` holds for **every** state and **every** position-diagonal Hamiltonian

**(a) Location.**  `theory/checks/ace_ld_check.py` `check_c6` and
`BarrierModel(flat=True)`; `theory/ace-ld.md` §5 `LD-C6` bullet ("the confined
side of ⟨1⟩5.⟨2⟩6's dichotomy"); `theory/ace-ld-r2-response.md` row M3 ("The
demanded static contrast exists: LD-C6 certifies `p_W = δ_0` with LR3 tail
`0`"); MP-1 row `ACE-LD-obst-prime`, "tested in … LD-C6".

**(b) My computation.**  With `flat=True` the Hamiltonian is
`H = diag(V)` and `evolve` is multiplication by `exp(−iVt)`.  The clamp charge
`qv` is also position-diagonal, so `E_W({q})` commutes with the evolution and
the TPM law is `δ_0` **identically**.  I ran `check_c6`'s gates on absurd
inputs (`probe_c6.py`):

| state / model | `p_0` at the four windows | LR3 tail |
|---|---|---|
| shipped green packet | `1.0, 1.0, 1.0, 1.0` | `0,0,0,0` |
| uniform over the whole ring | `1.0, 1.0, 1.0, 1.0` | `0,0,0,0` |
| random complex vector (seed 0) | `1.0, 1.0, 1.0, 1.0` | `0,0,0,0` |
| packet 1000 sites outside `W` | `1.0, 1.0, 1.0, 1.0` | `0,0,0,0` |
| random diagonal potential `×17` | `1.0, 1.0, 1.0, 1.0` | — |

Nothing moves.  The gate cannot fail on its own model class; `--red-c6-moving`
does not mutate the static model, it **substitutes a different model**
(`BarrierModel()`), which is the weakest possible form of red test.  What r1's
M3 demanded was a *static-kink* contrast — a model where the dynamics is
nontrivial but the wall is confined (D16 with a magnon is the obvious one).
What was delivered is a model in which the certified observable is conserved
by construction.  This is the campaign's now-familiar no-op pattern
(five prior instances listed in the protocol); it is number six.

**(c) FIX DEMAND.**  Replace LD-C6 by a contrast in which the dynamics does
**not** commute with `Q̂_W` — e.g. the D16 battery with one magnon added,
certifying that the TPM law is supported on a bounded set of `ν` while
`Σ|ν|p_{W_m}` stays bounded as `|W_m|` grows — and register a mutation *of that
model* that breaks it.

**(d) SURVIVING WEAKER STATEMENT.**  LD-C6 certifies the elementary fact that
if `[H,Q̂_W]=0` then the D27 TPM law is `δ_0` with zero LR3 tail.  That is
true, is a one-line consequence of D27's definition, and is not evidence for
"the confined side of the dichotomy".

---

### M4 (MAJOR) — LD-C5's identity gate is deductively subsumed by its own concentration gate, its tail gate reduces to `1 > 0.9`, and two of its five gates are unreachable by any registered mode; §5's blanket reachability claim is false

**(a) Location.**  `check_c5` gates (c), (d), (e); `theory/ace-ld.md` §5,
`LD-C5` bullets (c)--(e) and the sentence "**every gate — including each
internal sub-gate that carries evidence — has a registered red mode that
reaches it**"; §5 design note (iii) ("the two 'different' expressions in C5(d)
are … independent computations"); §5 design note (iv) ("no other gate pair is
deductively linked"); `theory/ace-ld-r2-response.md` checker record ("No gate
is unreachable").

**(b) My computation.**

*Gate (d) is a tautology given gate (a).*  Gate (a) forces
`‖ψ_0·1\{qv≠0\}‖ < 1e-4`, i.e. the initial state is a **single** spectral
branch.  Then `tpm_law` has one surviving `q=0` branch, `ν = −q'`, and
`Σ_ν ν p(ν) = −⟨Q̂⟩_{t_+}`, while `mean_early = ⟨Q̂⟩_{t_-} ≈ 0` — the two
"independent" sides are the same expression.  Measured (`probe_c5.py`), for
four *different* barrier configurations:

| model | LD-C5(a) defect | `Σνp` | `⟨Q̂⟩_- − ⟨Q̂⟩_+` | gap |
|---|---|---|---|---|
| green, `v_0=1.2` | `8.1e-07` | `−12.4023985609` | `−12.4023985609` | `4.3e-11` |
| `v_0=6.0` (weights `0.90/0.10`) | `8.1e-07` | `−1.6567093095` | `−1.6567093095` | `8.9e-12` |
| three barriers, multi-atom law | `8.1e-07` | `−5.2155945444` | `−5.2155945444` | `3.5e-12` |
| broad packet, defect `4.4e-03` | `4.4e-03` | `−12.1640290766` | `−12.1641314338` | `1.0e-04` |

The gap is not `~1e-4`, it is `~1e-11`, and it tracks the *concentration
defect* exactly — it is nonzero only when gate (a) is near failing.  The gate
therefore certifies nothing about MI ⟨1⟩7.⟨2⟩1--⟨2⟩2, whose entire content is
the **dephasing** term `𝒟_{W,t_-}` and D27(LR2); the configuration makes the
dephasing defect exactly zero by construction.  `--red-c5-meanshift` shifts the
checker's own computed `mean_early` by `+1` — mutating one of its own numbers,
which the standing obligations name as proving nothing about the claim.

*Gate (e) reduces to `1 > 0.9`.*  Given gates (b)+(c), the law is
`p_0 = |r|²`, `p_{−|W|} = |t|²`, so
`Σ_{|ν|>10}(1+|ν|)p = (1+|W|)|t|²` and the floor is `0.9(1+|W|)|t|²`.
Measured at `|W|=129`: tail `94.84` versus `(1+129)(0.7296) = 94.85`.  I ran it
at `v_0 = 1.2, 6.0, 20.0` (`|t|² = 0.7296, 0.0975, 0.0096`): the gate passes in
all three, because it is arithmetically `1 > 0.9`.  The monotone-growth clause
likewise reduces to `1+|W_{j+1}| > 1+|W_j|`.

*Reachability.*  Exit paths of the three registered barrier modes
(`probe_gates.py`): `c5-nobarrier` fires at gate (b1) `p_0 = 0`;
`c5-meanshift` fires at gate (d); `c5-inwindow` fires at gate (a).  **Gates (c)
and (e) are reached by no registered mode.**  Gate (e) is the one that
exhibits the linear LR3 tail growth — the mechanism ACE-LD-obst′ is about.

*And in LD-C1:* the same audit shows the **orthogonality** and **resolution**
sub-gates are reached by no registered mode either (`gap`, `coset`,
`halfspace` all fire earlier; `merged`/`dup` pass LD-C1 outright).  Both
sub-gates do have teeth — my mutations fire them ("channel projections not
orthogonal"; "sum P_ch psi != psi (4.188e-01)") — so this is r1's m1 only
**partially** fixed, while the r2-response records it as "FIXED".

**(c) FIX DEMAND.**  Delete §5's blanket reachability sentence and the
"independent computations" note; disclose that (d) is implied by (a) and that
(e) is implied by (b)+(c); register modes that reach (c) and (e) (e.g. an
absorbing barrier that destroys the weight match; a window-independent tail);
register mutations reaching LD-C1's orthogonality and resolution sub-gates; and
either certify MI ⟨1⟩7.⟨2⟩2 in a genuinely two-branch configuration (incoming
state spread over two window charges, so `𝒟` acts) or stop claiming that gate.

**(d) SURVIVING WEAKER STATEMENT.**  LD-C5 certifies, on a one-particle
barrier model with a definite-side incoming packet: the incoming state is
concentrated on one window charge to `≤3.2e-6`; the TPM law is exactly the two
atoms `{0, −|W|}` with off-atom mass `<1e-4`; and the `ν=0` atom that r1's
certificate never produced is present with `p_0 = 0.2704 = |r|²`.  That is
real, it is r1's M3 fix demand met at the level of the *configuration*, and it
is the honest content.  The identity, the weight match and the tail growth are
consequences of those facts, not independent evidence.

---

### M5 (MAJOR) — the `tns-xf4` fence rests on an inference from band flatness that LD-C7(a) does not certify and that the parallel lane's critic has just ruled out as K4-strength

**(a) Location.**  ⟨1⟩5.⟨2⟩6(iii) ("D16 is in the COMPLEMENT of (M-ESC): its
kink band is exactly flat … so `θ = 0` there and NOTHING in this shard bears
on … bd `tns-xf4`"); the same inference in §0 ACE-LD-obst′'s Scope
parenthesis, in MP-1's `ACE-LD-obst-prime` not-claimed clause, and in **MP-6**;
`theory/checks/ace_ld_check.py` `check_c7` gate (a).

**(b) My computation.**  LD-C7(a) certifies that the **ground energy** of each
`S^z` sector of the open `L=12` chain is `0` to `8.2e-17`.  I reproduced that,
and went further: the kernel of `H_kink` at `L=12` is exactly
`13 = L+1`-dimensional, with a uniform gap `1.5341` above it.  Two gaps follow.

*First*, "the kink band is exactly flat" as a **model** statement requires
`ker H_kink` to be exhausted by the K1--K2 family — which is claim **K4**, a
CONJECTURE row with finite-volume evidence only.  My `L=12` count *is* that
finite-volume evidence; it is not the claim.  The parallel lane's critic has
just flagged the identical upgrade as MAJOR in the other lane
(`theory/verdicts/lr-d16-r1.md` M3: "'The D16 core has no group velocity' …
need the kernel to be exhausted by the family — which is precisely **K4**").
ACE-LD ⟨2⟩6(iii) makes the same move.

*Second, and worse for the fence:* even granting exact flatness of the bare
kink family, `θ = 0` is a statement about the **D17/D27 states**, which are
kink *plus magnon*.  At `L=12` there is no kink+magnon state anywhere near the
kernel (gap `1.5341`), so LD-C7(a) says nothing at all about them.  `θ = 0` for
those states needs the magnon-induced wall displacement to be bounded — true,
and bounded by `|δx| ≤ ⟨N_T⟩/s`, but that is M-quant-G's conclusion, not a
consequence of band flatness.

**(c) FIX DEMAND.**  Replace "its kink band is exactly flat … so `θ = 0`
there" (three places plus MP-6) by: "every state in the closed span of D16's
K1--K2 family is exactly stationary (K1+K2, PROVED; `ker H_kink` exhaustion is
K4, CONJECTURE), and for D17 kink--magnon packets the mean wall transport is
bounded by `⟨N_T⟩/s`, so `θ = 0`; LD-C7(a) certifies only the sector ground
energies at `L=12`."

**(d) SURVIVING WEAKER STATEMENT.**  The fence's *conclusion* is right and I
believe it: D16 has `θ = 0` and `ACE-LD-obst′` does not pre-empt `tns-xf4`.
Only the stated justification is too strong.  LD-C7(a) stands as an exact,
independently reproduced certificate that all 13 sector ground energies vanish
and that the kernel is `(L+1)`-dimensional at `L=12`.

---

### M6 (MAJOR) — MP-2 asserts a counterexample to (AD3-ex) on a state that is not an (AD3-ex) vector

**(a) Location.**  MERGE PROPOSALS **MP-2** ("the exact display is FALSE at
every fixed `W` in the D16 instantiation"); the same claim at ⟨1⟩4.⟨2⟩8(i),
§4 HONEST STATUS "Refuted / withdrawn" second bullet, and MP-1's `ACE-LD-eps`
not-claimed clause; MP-3(i).

**(b) My computation.**  (AD3-ex) is displayed in AS ⟨1⟩7's ASSUME for
`Ψ = W_+(F_L,F_T)` with channel projections `P_ch`, `ch∈{L,T}` — a
kink--magnon scattering vector in `ran W_+`.  The state LD-C7 and r1 §8
measure is the **sector ground state**: an exact zero mode with **no magnon**
(I verified: at `L=12` the kernel is the 13 bare-kink states, and the magnon
costs `≥1.5341`).  It is stationary, has no channel decomposition, and is not
in `ran W_+`.  So the shard's `min_q‖(Q̂_W−q)Ψ‖ > 0` computation, which I
reproduce exactly (`4.453e-02, 9.305e-03, 1.942e-03, 4.046e-04`), is an
out-of-class computation — the same defect r1 recorded as its own NOTE n3 for
the AKLT illustration, now in merge text destined for `claims/CLAIMS.md`.

The *substance* is nonetheless recoverable and should be stated in the
recoverable form: D18(AD3)'s clause "the remaining local state is a kink charge
eigenstate" fails for D16 because a D16 kink is **never** a `Q̂_W` eigenvector
at finite `W` — its own exponential tails give dispersion `∼ q^{d_W} > 0`.
That argument does transfer to a scattering vector's late-time window content;
it is just not what the certificate measures.

**(c) FIX DEMAND.**  Rewrite MP-2 and the three companion sentences as: "D16's
exact kink states are never `Q̂_{W,c_0}` eigenvectors at finite `W` — the
defect is `min_q‖(Q̂_W−q)Ψ‖ = 4.45e-02 … 4.05e-04` decaying as `q^{d_W}`
(LD-C7) — so D18(AD3)'s 'remaining local state is a kink charge eigenstate'
clause can hold at fixed `W` only in ε-form.  No in-class (AD3-ex) vector is
exhibited; the exact display is not refuted, it is unavailable."

**(d) SURVIVING WEAKER STATEMENT.**  `AD3-ex` stays CONJECTURE (correct — M4
of r1 is properly fixed), with the prose "its exact fixed-`W` form requires the
window content to have zero `Q̂_W` dispersion, which D16's kink tails
contradict; only an ε-form is available at fixed `W`, and the ε-form's own
hypothesis (K-TAIL) is incompatible with the escaping leg that (AD3-ex)
presupposes (ace-ld-r2 F1)."

---

## 3. MINOR

**m1 (MINOR) — ⟨1⟩4.⟨2⟩9(c) quotes numbers that do not reproduce, and they
disagree with §5's, which do.**  *(a)* ⟨1⟩4.⟨2⟩9(c) ("`4.45e-02, 9.30e-03,
1.94e-03, 3.96e-04` — successive ratios `0.2089, 0.2085, 0.2041`"); §5 LD-C7
bullets (b),(c) ("`… 4.05e-04`"; "`0.2089, 0.2087, 0.2083`").  *(b)* My
independent ED gives `4.453450e-02, 9.304727e-03, 1.941946e-03, 4.045736e-04`
and ratios `0.208933, 0.208705, 0.208334`; the shipped checker agrees exactly.
⟨2⟩9(c)'s fourth defect and last two ratios are wrong, and its claim "to three
digits" is false of its own last ratio (`0.2041`).  These are r1's numbers,
carried over unrecomputed.  *(c)* Replace ⟨2⟩9(c)'s figures with §5's.
*(d)* The `λ̃^{d_W}` claim is correct; only the r1-inherited digits are stale.

**m2 (MINOR) — the D16 battery is the ℤ₂-image of D13(a)'s orientation, so
(K-TAIL) as displayed fails on the very state cited as its instance.**
*(a)* §0 THEOREM ACE-LD-ε (`D_x := S^z_x − s_{γ(x)}`, `s_α=+s`, `s_β=−s`);
§5 D16 battery ("WITH the telescoping boundary field
`(J/2)√(Δ²−1)(S^z_1 − S^z_L)`"); ⟨1⟩4.⟨2⟩9(c).  *(b)* I computed the site
profile of the ED ground state: `⟨S^z_x⟩ = −0.5, −0.5, −0.5, −0.4999, −0.4981,
−0.4565, +0.4565, +0.4981, +0.4999, +0.5, +0.5, +0.5` — **↓ at `−∞`, ↑ at
`+∞`**, the opposite of D13(a).  Read with the shard's own `s_α=+s`, the left
tail has `D_x ≡ −1` and (K-TAIL) fails outright; read with the flipped
assignment it holds at rate exactly `q` (§0(iii)).  The parallel lane treats
this same sign as binding, not cosmetic (`theory/lr-d16.md` ⟨1⟩1.⟨2⟩2,
convention (LRD-O)).  *(c)* Either flip the sign of the D16 battery's boundary
field, or state the ℤ₂ conjugation explicitly at ⟨2⟩9(c) and in §5.
*(d)* Under the flip, the instantiation is correct as claimed.

**m3 (MINOR, L4) — MP-4's `𝒬_{c_0}` is a third name for a frozen object.**
*(a)* MP-4 row 1; ⟨1⟩4.⟨2⟩2(ii).  *(b)* By §0(i), `𝒬_{c_0} = 2s(X_1 − c_0)`
with `X_1` frozen in D13(c) and `notation.md` line 211; its tail-restricted
cousins `Q_W^α, Q_W^β` are frozen at `notation.md` line 271.  Introducing a
fresh symbol without the identification is exactly what L4 forbids.  *(c)*
Rewrite the MP-4 row as "`𝒬_{c_0}φ` — the vector-valued lift of D13(c)'s
conserved `X_1`: `𝒬_{c_0} = 2s(X_1−c_0)`; exists on (K-TAIL) states".
*(d)* The object is well defined and its limit is correctly constructed.

**m4 (MINOR) — r1's m1 is recorded FIXED but only one of its three gates is
armed.**  *(a)* `theory/ace-ld-r2-response.md` row m1; §5's red table.
*(b)* See M4(b): `--red-halfspace` arms `[P,H]`; nothing arms the
orthogonality or the resolution sub-gate, and both fire under mutations I
wrote.  *(c)* Register the two missing mutations, or downgrade the disposition
to PARTIAL.  *(d)* The `[P,H]` gate is genuinely armed, as claimed.

**m5 (MINOR) — ACE-LD-ε-x carries an unused hypothesis.**  *(a)* §0 COROLLARY
ACE-LD-ε-x ASSUME ("and let `W` be large enough that `ε_W < δ`").  *(b)* The
proof ⟨1⟩4.⟨2⟩6 uses only the set geometry `dist(q_L,S_T)>δ` and
`dist(q_T,S∖S_T)≥δ`, both of which hold for any `ε_W`; the conclusion
`≤ δ^{-1}ε_W` is valid without the smallness assumption (it is merely vacuous
when `ε_W ≥ δ`).  *(c)* Delete the clause or mark it as the regime in which the
bound is informative.  *(d)* The corollary is correct with or without it.

**m6 (MINOR) — ⟨1⟩4.⟨2⟩4's "in the D16 instance it exists trivially" asserts
M-INDEX-LA-folium (CONJECTURE) without citing it.**  *(a)* ⟨1⟩4.⟨2⟩4, the
parenthesis; §4 HONEST STATUS, "(K-Q) for all `t`" bullet.  *(b)* In finite
volume the conserved sector charge is trivial; in infinite volume the existence
of a self-adjoint conserved `𝒬̂` on the D16 kink folium is exactly the content
of the CONJECTURE row **M-INDEX-LA-folium** ("the entire content is EXISTENCE
of the strongly continuous implementer").  The step is the *only* route the
shard offers for (K-Q)'s `t`-uniformity, i.e. for ACE-LD-ε-t's hypothesis.
*(c)* Cite M-INDEX-LA-folium by id and replace "trivially" by "in finite
volume; in infinite volume this is M-INDEX-LA-folium, CONJECTURE".
*(d)* No collision with the REFUTED M-INDEX-LA-strong: see §5 item 7.

**m7 (MINOR) — MP-1's obst row drops HONEST STATUS's uninstantiation
disclosure.**  *(a)* MP-1 row `ACE-LD-obst-prime`, not-claimed enumeration;
§4 HONEST STATUS, "(M-ESC) on any concrete model/state" bullet.  *(b)* HONEST
STATUS says no model is known to realise `θ>0`; the row does not.  The
parallel lane's critic has independently confirmed that the corpus supplies no
such model (`theory/verdicts/lr-d16-r1.md` M2(b)1).  *(c)* Append "no model or
state realising `(M-ESC)` is exhibited anywhere in this corpus" to the row.
*(d)* As a negative result the row does not need an instance; it needs to say
so.

**m8 (MINOR, L2) — 1033 lines against the 200--500 band**, self-reported;
MP-5's split is endorsed (see §8).

---

## 4. NOTE

**n1 (NOTE) — ACE-LD-obst′ is the contrapositive of a sentence already frozen
in D27.**  D27's own definition paragraph reads: "Existence is a corollary of
LR1--LR3: at every fixed `m`, `Σ_ννp_{W_m}(ν)=−2s[ω^+−ω^-](𝔛_{W_m})`, and LR3
makes the left side converge, hence the right side."  Converging implies
bounded implies `θ=0`.  The genuine addition of ⟨1⟩5.⟨2⟩3 is the `M_0`
argument, which gets the uniform bound directly from tightness without passing
through weak convergence.  That is worth having and worth *saying*; the row
should disclose the subsumption rather than presenting the result as new.

**n2 (NOTE) — MP-4's `θ` overloads the twist angle, and the m6 disposition's
grep is inaccurate.**  `notation.md` carries `θ_α(g)`, `θ'_α(ξ)`, `θ_c`, and a
bare `θ` as the twist variable in `μ_∞^α = (2π)^{-1}∫e^{-iθν}|tr(V_θ r)|²dθ`
(line 271) — in `memory-index.md`, the very shard ACE-LD cites throughout.  The
r2-response's "grep-checked against `notation.md` (no hits)" is false for `θ`.
Rename (e.g. `θ_{tr}`) or flag the overload explicitly.

**n3 (NOTE) — mode count.**  The REGISTRY holds **13** modes producing **14**
gate firings (LD-C1 fires on three distinct sub-gates, LD-C2/C4 on two modes
each).  The orchestrator's "14 red modes" is the firing count, not the mode
count; §5's "thirteen" is right.  `python3 -O … --red` → exit 1, RED-OK,
13/13, every registered pattern reproduced; green → exit 0 in 32 s.

**n4 (NOTE) — LD-C1's coset gate is arithmetic on the checker's own
construction.**  `qvals` is an integer clamp by construction, so the coset gate
can fail only if the definition is deliberately corrupted — the same status
`memory_index_probe.py` P2 carries and discloses ("an arithmetic certificate …
not a dynamical one").  Worth the same disclosure here.

**n5 (NOTE) — LD-C7 measures the conclusion, not the hypothesis.**  MP-1's row
says "(K-TAIL) at rate `q = Δ−√(Δ²−1)` certified by ED at `L=12`, ratios
`0.2089/0.2087/0.2083`".  Those ratios are **defect** ratios — the conclusion
of (LD.4) — not the (K-TAIL) clustering constants; no gate computes
`ω_φ(D_xD_{x'})`.  I computed (K-TAIL) directly (§0(iii)) and it does hold at
rate exactly `q`, so the claim is true and the attribution is wrong.  Add a
gate that measures `‖D_xφ‖λ̃^{-dist(x,K)}` and gate its boundedness.

**n6 (NOTE) — citing MI ⟨1⟩7 inside a proof by contradiction against LR3.**
MI ⟨1⟩7's ASSUME is "H-IDX, **including D27(LR)**", i.e. including LR3.
⟨1⟩5.⟨2⟩2 cites its sub-steps ⟨2⟩1--⟨2⟩2, whose own justifications name only
LR1--LR2 and (IDX.1).  I checked both leaves: the citation is sound.  The shard
flags this ("No use of D27(LR3) is made"); it should also say *why* — that the
sub-steps' justifications carry weaker hypotheses than the theorem's ASSUME.

---

## 5. VERIFIED CORRECT — fenced; the repair lane must not churn this

Each item re-derived or re-run by me, independently.  **Do not rework.**

1. **⟨1⟩1 (LD-GAP) and ⟨1⟩2 (ACE-LD-abs) and ⟨1⟩3 (ACE-LD-nec)** — unchanged
   from r1 apart from the m3 fix and the ⟨2⟩5 addition; r1 fenced them and I
   re-checked the fence still applies.  The m3 fix is correctly applied: §0's
   ACE-LD-nec ASSUME now lists `w_i > 0` for **both** `i`.
2. **⟨1⟩1.⟨2⟩5 (LD-GAP-SET), the r2 addition.**  On `ran(1−E(B))` the spectrum
   is `S∖B` and the inverse norm is `d_B^{-1}`; the dual form on `ran E(B)`
   likewise.  Both correct, including the degenerate `S∖B=∅` case.
3. **⟨1⟩4.⟨2⟩1 (LD-SPLIT).**  The annulus identity and the exact regrouping
   `−s(a−a')+s(b'−b) = s(a'+b'−a−b)` are right; the `c_0` dependence cancels.
   I reproduced it from D13(a) directly.
4. **⟨1⟩4.⟨2⟩2 (LD-TAIL), both clauses.**  (i) The square expansion, the
   same-side distinctness of integer distances, and
   `Σ_{j≥d}λ̃^j = λ̃^d/(1−λ̃)` are all correct.  (ii) The Cauchy property, the
   two-annulus factor `2`, exhaustion-independence by interleaving, and the
   uniform bound `2C_Kλ̃^{d_W}/(1−λ̃)` are correct.  **The limit vector exists
   as claimed.**
5. **⟨1⟩4.⟨2⟩3 (LD-EPS) and the coset location.**  Triangle inequality and
   `‖(Q̂−q)φ‖² = ∫|λ−q|²dμ_φ ≥ dist(q,\mathrm{spec})²`; both right.
6. **⟨1⟩4.⟨2⟩6 (ACE-LD-ε-x's algebra).**  The set geometry
   (`|λ−q_L| > δ` on `S_T`, `|λ−q_T| ≥ δ` off it), the two LD-GAP-SET
   applications, and the Cauchy--Schwarz step are all correct, and
   `E_W(\{q_T\}) ≤ E_W(S_T)` makes the ball form imply AS ⟨1⟩7.⟨2⟩2's
   singleton form.  **The estimate is right; only its hypothesis is
   unavailable (F1).**
7. **LD-TAIL does *not* collide with the REFUTED M-INDEX-LA-strong.**  I
   checked this directly, as the brief demands.  ⟨2⟩2 constructs a *vector* on
   a state satisfying an extra exponential-clustering hypothesis; it does not
   construct a densely defined self-adjoint operator on the sector, and the
   folium-independent statement M-INDEX-LA-strong refutes is not asserted.
   The refuting counterexample (MI ⟨1⟩3.⟨2⟩2, `ε_n = (n+1)^{-1/2}`) has
   `ω(D_{-n}²) = 1/(n+1)` — **polynomial** decay — so it is excluded from the
   (K-TAIL) class by exactly the margin (K-TAIL) demands, and no contradiction
   arises.  The distinction the shard draws at ⟨2⟩2 and MP-4 is legitimate.
   (The sector-wide *operator* does appear at ⟨2⟩4 — that is m6, a CONJECTURE
   citation defect, not a REFUTED-row collision.)
8. **⟨1⟩5 (ACE-LD-obst′), all three claims, at the stated minimal hypotheses.**
   ⟨2⟩1: at fixed `m` the law is supported on the finite set
   `spec Q̂_{W_m} − spec Q̂_{W_m}`, so the pointwise limit of probabilities is a
   probability — correct.  ⟨2⟩3: `Σ|ν|p ≤ M_0·1 + 1` — correct.  ⟨2⟩4: (a) from
   the liminf, (b) via `Σ_{|ν|>M}|ν|p ≥ Σ|ν|p − M ≥ |Σνp| − M`, (c) no
   subsequence of a divergent sequence converges — all correct.  ⟨2⟩5's mean
   arithmetic (`ω^-(𝔛)=a_m−1`, `ω^+(𝔛)=a_m−1+p_{tr}|W_m|+o(|W_m|)`,
   `θ=p_{tr}`) is correct in D13(a)'s orientation.  **The minimal-hypothesis
   claim is true: no `(E-TAIL)`, `(V-ch)`, `(V-in)`, `σ_L≠σ_T`, channels,
   wave operators or D28 are used anywhere in ⟨1⟩5.**
9. **The F1 deletion is complete.**  I grepped the whole shard: `(E-TAIL)`,
   `(V-ch)`, `(V-in)`, `σ_L≠σ_T`, ACE-LD-esc, COROLLARY ACE-LD and r1's
   ACE-LD-obst survive **only** in the deletion notice, in "not used"
   enumerations, and in ⟨2⟩9(a)'s equivalence remark.  **No surviving step
   cites a deleted hypothesis.**  The false D28 sentence is gone and every
   remaining D28 mention correctly says D28(4) constrains only `v_M−v_K`.
10. **⟨1⟩4.⟨2⟩9(a) is correct**, and recording it once with its two-line
    proof is the right disposition of r1's M1.
11. **§5 spec/code lockstep is exact.**  I checked every constant and every
    quoted number against the shipped run: `N=8192`, no detune, asserted
    constant, `W=[N/2−16,N/2+16]`, dyadic times, `N_BAR=2048`, `V_0=1.2`,
    offset 300, `t_±=0/300`, `|W|=17,33,65,129`, D16 `Δ=2.5, J=1, L=12,
    c_0=5`, the four windows, and every green figure (`7.2e-12/3.3e-12`,
    `0.168`, `0.2704/0.7296`, `13.13→24.80→48.15→94.84`, floor `85.4`,
    `8.2e-17`, defects, ratios, worst coset `2.0e-3`) and every red figure
    (`0.1`, `0.414`, `0.53`, `0.80`, `1.00`, `0.27`, `0.1717`, `−0.499`,
    `1.146`, and the `t=8, lhs 4.121597e-01 > rhs 3.724759e-01` line).
    **All exact.**  r1's m4 is fully fixed.
12. **r1's M6 is genuinely fixed, all three parts.**  (i) LD-C3's "tests the
    CONSTANT" claim is gone and the honesty clause is *accurate*: I bisected
    the asserted constant and it passes at `0.17`, fails at `0.16` — a factor
    `5.9`, matching §5's "~6× smaller would also pass".  (ii) `--red-coset` is
    a **true** coset break, distinct from `--red-gap` in mechanism and not
    merely in registered pattern: it shifts one edge eigenvalue by `√2−1`
    keeping `min gap = 1`, fires only LD-C1's coset sub-gate, and LD-C3
    survives *non-vacuously* — the mutation is visible to LD-C3, which moves
    from `max lhs/rhs = 0.168053` (green) to `0.161897` (coset) and still
    passes.  `--red-gap` fires the gap sub-gate **and** LD-C3.  Different
    mechanisms, different survivors.  (iii) §5 now says the constant is
    asserted, matching the code.
13. **r1's M4 is fixed.**  `AD3-ex` stays CONJECTURE; all MP-1 statuses are
    bare L5 values; the compound non-status is withdrawn.
14. **The green and red runs are as documented.**  `python3 -O` green → exit
    0 (32 s); `--red` → exit 1, RED-OK, 13/13; no bare `assert` anywhere.

---

## 6. Register comparison against the nearest PROVED rows

The nearest adjudicated rows — **M-INDEX-fin**, **M-INDEX-spec**, **AC-EX** —
each carry an *"Adjudicated scoping (verbatim)"* paragraph that (i) names every
hypothesis in full, (ii) states the conclusion as an explicit conditional
implication, and (iii) closes with an enumeration of what is **not** claimed,
including the negative facts that hurt ("no implication H-AD-G ⟹ (LR) is
claimed"; "no sector-wide total-charge operator is constructed, and its
unconditional existence is REFUTED"; "(D28-C) is the load-bearing hypothesis
and is unverified on any model").

MP-1's three rows now do (i) and (ii) properly and **do** carry not-claimed
clauses — a genuine advance on r1, where they carried none.  The remaining gap
is that the not-claimed clauses omit precisely the facts that hurt: the `χ=1`
tail-vacuum forcing (M1), the incompatibility with an escaping leg (F1), the
`δx = 0` consequence (F1(b)(iv)), the absence of any `(M-ESC)` instance (m7),
and the D27 subsumption (n1).  The `ACE-LD-obst-prime` row is **closest to
register** of the three; the `ACE-LD-eps` row is furthest, because its
positive clause ("the input AS ⟨1⟩7.⟨2⟩2 consumes") is not merely unscoped but
false.  HONEST STATUS is, again, in better register than MERGE PROPOSALS — the
same diagnosis as r1 §6, at reduced severity.

---

## 7. Cross-lane ruling — ACE-LD-obst′ versus LR-D16

**They are consistent, and I believe both — but the brief's premise is already
out of date, and ACE-LD's fence is supported for the wrong reason.**

1. **The premise.**  `theory/lr-d16.md` ⟨1⟩5 no longer stands as "LR3 proved
   for D16 from (NR)".  The parallel critic pass landed at commit `560a6c7`:
   `theory/verdicts/lr-d16-r1.md` is **FAIL(F1,F2,M1--M4)**, and its **F2**
   holds that (LRD.13) is *not* `m`-independent — the second term is a
   `W_m`-pinching and pinchings are not monotone — so THEOREM (LRD-3) does not
   follow from (NR) as written.  It is recoverable under a repaired (NR)
   carrying a `sup_m`.  So: LR3 for D16 is currently **not proved**, from (NR)
   or otherwise.
2. **Logical consistency.**  ACE-LD-obst′ says `θ>0 ⟹ ¬LR3`; LR-D16 (repaired)
   says `(NR) ⟹ LR3` for D16.  These conflict only if D16 has `θ>0`.  It does
   not: D16's wall displacement under a D17 kink--magnon packet is bounded by
   `⟨N_T⟩/s`, so `θ = liminf O(1)/|W_m| = 0`.  **No contradiction, in either
   direction.**  The LR-D16 critic reached the same conclusion from the other
   side and recorded it as its n3 ("Both lanes agree; there is no cross-lane
   contradiction"), quoting ACE-LD's own `θ=0` scope clause.
3. **More than consistency: mutual reinforcement.**  My M2 sharpening of
   obst′ — `LR3 ⟹ sup_m|ω^+−ω^-|(𝔛_{W_m}) < ∞` — is the *first-moment* shadow
   of LR-D16's ⟨1⟩5.⟨2⟩4 monotonicity remark, which says the same thing at
   second-moment level: an increment `|ν| ≍ 2s|W_m|` cannot be manufactured by
   window geometry and requires the fixed smallest-window quantity `𝒩_{W_1}` to
   be large.  Composing them gives a statement neither lane has:
   **`(M-ESC) ⟹ (NR) fails`.**  That is the right thing to transmit to
   `tns-xf4`, and it is stronger than MP-6's hint.
4. **Where ACE-LD is wrong on D16.**  Its stated reason for `θ=0` — "its kink
   band is exactly flat … so `θ=0` there" — is the K4-strength upgrade that the
   LR-D16 critic has just ruled MAJOR in the other lane (M3 there), and it
   concerns bare kinks while `θ` concerns kink+magnon states (my M5).  **The
   conclusion is right; the justification must be replaced.**
5. **Which I believe, if forced.**  Both, on their corrected statements.  If a
   conflict ever emerges, I would believe **ACE-LD-obst′**: its proof is four
   lines from D27's own frozen identity and needs no model input, whereas
   LR-D16's LR3 route has already failed once on a pinching-monotonicity error
   and still rests on an open hypothesis (NR) whose companion (LR2′) the same
   verdict found **empty**.

---

## 8. Deliverables the brief asks for by name

**(A) May `ACE-LD-ε` enter `claims/CLAIMS.md`, and at what status?**
**Yes — at PROVED (conditional) — but only after the F1 and M1 repairs, and
only with the AS-supply clause deleted.**  The mathematics is correct and the
class is inhabited (I verified both).  Exact verbatim scoping sentence, to be
carried in the row:

> **Adjudicated scoping (verbatim).**  Proved only as the conditional
> implication: H-MQG(1)--(2), a finite core `K = [ℓ,r]`, a finite window
> `W = [a,b] ⊇ K` with cut `c_0 ∈ W` and padding
> `d_W = \min(ℓ−a, b−r)+1`, and a unit vector `φ` satisfying **(K-TAIL)**
> (same-side exponential tail clustering of the on-site deviations `D_x`,
> constants `C_K, λ̃`) and **(K-Q)** (`‖𝒬_{c_0}φ − q_φφ‖ ≤ ε_Q`, where
> `𝒬_{c_0} = \lim_n Q̂_{W_n,c_0}` is the vector-valued lift of D13(c)'s
> exactly conserved `X_1`, `𝒬_{c_0} = 2s(X_1−c_0)`) `⟹`
> `‖(Q̂_{W,c_0} − q_φ)φ‖ ≤ ε_Q + 2C_Kλ̃^{d_W}/(1−λ̃)`, and hence
> `dist(q_φ, κ_{W,c_0}+ℤ)` is bounded by the same quantity.  (K-TAIL) is
> equivalent, in the D9 kink class, to the statement that **no charge lies
> outside the core**: `‖𝒬_{c_0}φ − Q̂_{W,c_0}φ‖ ≤ 2C_Kλ̃^{d_W}/(1−λ̃)`; it
> therefore **forces both tail vacua to be `χ=1` `S^z`-product states with
> `s ∈ spec S^z`**, and it is **jointly unsatisfiable with D18(AD3)'s clause
> that the free leg charge leaves the window** — so no state carrying an
> escaping leg of nonzero charge satisfies it, and on states that do satisfy
> it with `ε_Q = 0` and `t`-uniform data the ordered wall displacement is
> `δx = 0`.  NOT claimed: that (AD3-ex-ε) supplies AS ⟨1⟩7.⟨2⟩2's cross-term
> step (it does not — the hypothesis fails on that class); the exact
> fixed-`W` (AD3-ex); D18(AD3)'s weak-\* clause or M-INDEX-spec's reduction
> clause; any statement about generic injective-MPS vacua; any
> infinite-volume proof of (K-TAIL) or (K-Q) on any model; the existence of a
> sector-wide conserved charge operator (M-INDEX-LA-strong is REFUTED;
> M-INDEX-LA-folium is CONJECTURE).  The hypothesis class is inhabited: D16's
> exact zero-energy sector states satisfy (K-Q) exactly and (K-TAIL) at rate
> `λ̃ = q = Δ−√(Δ²−1)` (verified by ED at `L=12`, `‖D_xφ‖` ratios `0.2087`
> per site, in the ℤ₂-image of D13(a)'s orientation).

Depends-on: `D13`, `D26`, `M-INDEX-fin`.  Tested in: `LD-C7` (which certifies
the *conclusion's* rate, not the hypothesis — see n5).

**(B) May `ACE-LD-obst′` enter as a negative row?**  **Yes, at PROVED
(conditional)**, once M2's quantifier is fixed and n1/m7's disclosures are
added.  I re-derived it in full and it is correct at the stated minimal
hypotheses.  Its row must (i) state the contrapositive in the `O(1)` form, not
`o(|W_m|)`, and not call it a contrapositive; (ii) record that it is the
quantitative contrapositive of D27's own existence corollary; (iii) record
that no model or state realising `(M-ESC)` is exhibited in this corpus; (iv)
keep the `tns-xf4` non-pre-emption clause but with M5's corrected
justification.  Its "tested in" cell must be trimmed: LD-C5's identity, weight
and tail gates are subsumed (M4) and LD-C6 is a tautology (M3), so the honest
cell is "LD-C5 (incoming concentration and the two-atom support, incl. the
`ν=0` atom)".

**(C) Does LD-TAIL survive the M-INDEX-LA-strong collision test?**  **Yes.**
See §5 item 7: no sector-wide operator is constructed, and the state that
refutes M-INDEX-LA-strong has polynomially-decaying deviations and is excluded
from the (K-TAIL) class.  The distinction the shard draws is rigorous and
should be kept verbatim.  The sector-wide operator that *does* appear —
⟨1⟩4.⟨2⟩4's "in the D16 instance it exists trivially" — is a CONJECTURE
(M-INDEX-LA-folium) citation defect, m6, not a REFUTED-row reliance.

**(D) Ruling on MP-1--MP-6.**
- **MP-1 row `ACE-LD-abs`** — **MERGE** as written (unconditional given its
  ASSUME, no depends-on, per r1's m5; verified twice).
- **MP-1 row `ACE-LD-eps`** — **HOLD.**  Merge only with the §8(A) scoping
  sentence substituted and the AS-supply and "Compatible with D27(LR3)"
  clauses deleted.
- **MP-1 row `ACE-LD-obst-prime`** — **HOLD**, merge after M2/m7/n1 per §8(B).
- **MP-2** — **HOLD**; `AD3-ex` correctly stays CONJECTURE, but the prose must
  be rewritten per M6(c).
- **MP-3** — **DO NOT MERGE.**  Clause (ii) is the F1 claim and would put a
  false statement into `theory/ansatz-scattering.md`.  Clauses (i), (iii), (iv)
  and the `ν`-orientation flag are sound and may be merged separately, with
  (i) rewritten per M6(c).
- **MP-4** — **HOLD**; `𝒬_{c_0}` must be identified with D13(c)'s `X_1` (m3)
  and `θ` renamed or flagged (n2).
- **MP-5** — **ENDORSE.**  Split ⟨1⟩5 into `theory/ace-ld-obst.md`; the
  hypothesis sets are disjoint and the file is at 1033 lines.
- **MP-6** — **ENDORSE with the justification replaced** per M5(c), and
  strengthened with §7 item 3: transmit `(M-ESC) ⟹ (NR) fails` to `tns-xf4`,
  which is a usable constraint rather than a hint.

**(E) Should `AD3-ex`'s CONJECTURE row now carry the regime split?**  **Yes,
but not MP-2's split.**  The honest split, after this round, is by *escaped
charge*, not by velocity class:
> `AD3-ex` at fixed `W` asserts that the channel state becomes a `Q̂_W`
> eigenvector while the leg charge sits **outside** `W`.  Any route through
> tail clustering proves the opposite regime: (K-TAIL) forces the escaped
> charge to zero, whereupon both channels carry the same conserved charge and
> `δx = 0` (ace-ld-r2 F1).  So the sharpness of `Q̂_W` on a channel state must
> come from the **wall's own localisation at fixed `W` given an escaped leg**,
> and no route to that exists in the corpus.  Additionally, D16's exact kink
> states are never `Q̂_W` eigenvectors at finite `W` (defect `∼ q^{d_W} > 0`),
> so only an ε-form is available at fixed `W` even for the leg-free corner.

---

## 9. Objection ledger

| id | severity | one line |
|---|---|---|
| F1 | **FATAL** | `𝒬_{c_0}=2s(X_1−c_0)` is D13(c)'s conserved charge; (K-TAIL) ⟺ no escaped charge, which contradicts D18(AD3)'s escaping leg and `q_L≠q_T`; where the hypotheses hold, `δx=0`.  The AS ⟨1⟩7.⟨2⟩2 supply claim (MP-3(ii), MP-1) is false |
| M1 | MAJOR | the `χ=1` (and `s∈spec S^z`) boundary is *forced* by D9(a)+(K-TAIL), not conditional, and is absent from §0, HONEST STATUS and MP-1's not-claimed clause |
| M2 | MAJOR | obst′'s "contrapositive ⟹ `o(\|W_m\|)`" is a quantifier slip; ⟨2⟩3 gives the stronger `sup_m\|ω^+−ω^-\|(𝔛_{W_m}) ≤ (M_0+1)/(2s)` |
| M3 | MAJOR | LD-C6 is a tautology: `p_W=δ_0`, tail `0`, for every state and every position-diagonal `H`; the r1 M3 static contrast is not delivered |
| M4 | MAJOR | LD-C5(d) is implied by LD-C5(a) (gap `4e-11`, not `1e-4`); LD-C5(e) reduces to `1>0.9`; gates (c),(e) and LD-C1's orthogonality/resolution sub-gates are unreached — §5's blanket reachability claim is false |
| M5 | MAJOR | the `tns-xf4` fence infers `θ=0` from band flatness — a K4-strength model claim (flagged MAJOR in the parallel lane) about bare kinks, while `θ` concerns kink+magnon states |
| M6 | MAJOR | MP-2's "(AD3-ex) is FALSE at every fixed `W` in D16" is measured on a magnon-free zero mode that is not an (AD3-ex) vector |
| m1 | MINOR | ⟨2⟩9(c)'s `3.96e-04` / ratios `0.2085, 0.2041` do not reproduce; correct values `4.046e-04` / `0.20871, 0.20833` (§5's are right) |
| m2 | MINOR | the D16 battery is the ℤ₂-image of D13(a)'s orientation; (K-TAIL) as displayed fails on it |
| m3 | MINOR | L4: MP-4's `𝒬_{c_0}` is a third name for D13(c)'s frozen `X_1` |
| m4 | MINOR | r1's m1 recorded FIXED; only one of its three LD-C1 sub-gates is armed |
| m5 | MINOR | ACE-LD-ε-x's `ε_W < δ` hypothesis is unused |
| m6 | MINOR | ⟨2⟩4's "exists trivially" is M-INDEX-LA-folium (CONJECTURE), uncited |
| m7 | MINOR | MP-1's obst row drops HONEST STATUS's "no `(M-ESC)` instance" disclosure |
| m8 | MINOR | L2: 1033 lines; MP-5's split endorsed |
| n1 | NOTE | obst′ is the quantitative contrapositive of D27's own existence corollary |
| n2 | NOTE | MP-4's `θ` overloads the twist angle; the m6 disposition's grep claim is false |
| n3 | NOTE | 13 modes, 14 gate firings; green exit 0 (32 s), `--red` exit 1 RED-OK 13/13 |
| n4 | NOTE | LD-C1's coset gate is arithmetic on the checker's own construction |
| n5 | NOTE | LD-C7 measures the conclusion's rate, not (K-TAIL); the (K-TAIL) claim is true (I verified it) but not certified |
| n6 | NOTE | MI ⟨1⟩7's ASSUME includes LR3; the cited sub-steps' justifications do not — sound, but say why |

---

FAIL(F1, M1, M2, M3, M4, M5, M6)
