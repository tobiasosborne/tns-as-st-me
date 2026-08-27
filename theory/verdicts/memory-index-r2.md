<!-- ROLE: round-2 ADJUDICATION covering BOTH shards — theory/memory-index.md
     (T1 synthesis, M-INDEX) and theory/ansatz-scattering.md (T2 repair, AC-EX).
     Priors (not re-litigated): memory-index-r1.md PASS, memory-index-b-r1.md
     FAIL(1-6), ansatz-scattering-r1.md FAIL(1,2,3,4).
     Format: rk-light — severity + (a) location + (b) independent computation +
     (c) FIX DEMAND + (d) surviving weaker statement.  Then the decision table,
     then PASS/FAIL.  Work order: briefs/r2-adjudication.md. -->

# Verdict: memory-index r2 (adjudicator, Opus) — 2026-08-28

Scope: `git diff a67e61b -- theory/memory-index.md` plus the lane-B imports
(§5, ⟨1⟩9--⟨1⟩12); the whole of `theory/ansatz-scattering.md` including its §6
repair-response table; lockstep on `definitions.md` D26/D27/D28,
`notation.md` (15 new rows), and the seven new `claims/CLAIMS.md` rows;
`theory/checks/memory_index_probe.py` and `memory_index_check.py` in green and
red, plus one additional mutation of my own on a copy in `/tmp`.

---

## 0. Verification record — what I recomputed, and it CHECKS

Recorded so round 3 does not re-litigate it.

**R1 (⟨1⟩9, density quantization — full recomputation, both tails).**
The convention matches D2(b) verbatim: with
`Σ_{s'}u(g)_{ss'}A^{s'}_α = e^{iθ_α(g)}V_α(g)^{-1}A^s_{g·α}V_α(g)`, the
one-site twisted transfer map is `E_{u(θ)}(X) = e^{if_α(θ)}V_θ^{-1}E_α(V_θX)`,
so `ω_α(u_x(θ)) = e^{if_α(θ)}tr[V_θ^{-1}E_α(V_θ r)]` — exactly the shard's
display, not a paraphrase.  Differentiating at `0` with `V_0=𝟙`,
`dV/dθ|_0 = X_α(ξ)` (D2(e) supplies both):
`F'(0) = if'_α(0)·tr[E(r)] − tr[XE(r)] + tr[E(Xr)] = if'_α(0) − tr[Xr] + tr[Xr]
= if'_α(0)`, using `E_α(r)=r`, `tr r=1` and `tr∘E_α = tr` (left-canonical).
Against `F'(0) = iω_α(S^z) = iρ` this gives `f'_α(0)=ρ` ✓.  ⟨2⟩2 is the
classification of continuous homomorphisms `ℝ → ℝ/2πℤ`, so `f_α(θ)=ρθ mod 2π`
globally ✓ (the local-Cauchy-plus-`f(nθ)=nf(θ)` route as written is valid).
⟨2⟩3: at `θ=2π`, (INT) gives `cA^s_α = e^{if_α(2π)}V_{2π}^{-1}A^s_αV_{2π}`;
D2(b)'s uniqueness clause with `Y=𝟙` (refs/arxiv-2011.12127 `(eq:XAX=B)`,
quoted correctly at definitions.md:162-163) forces `χ=0` and `V_{2π}` scalar,
hence `e^{2πiρ}=c` ✓.  ⟨2⟩4 at `β` with the SAME on-site `u` gives
`e^{-2πiρ}=c` ✓.  ⟨2⟩5: `e^{4πiρ}=1 ⟹ 2ρ∈ℤ`, and `c=(-1)^{2ρ}∈{±1}` ✓.
**No hidden use of D13's `s`:** ⟨1⟩9's ASSUME names D1, D2(a), (S), D26 and a
fresh `ρ`; no step of ⟨2⟩1--⟨2⟩5 cites D13, H-MQG, or `d=2s+1`.  The
decircularization demanded by memory-index-b-r1 objection 1 is genuine **in
the shard** — but not in the shared symbol table; see Objection 1.

**R2 (⟨1⟩11, the characteristic-function formulas).**  ⟨2⟩1's phase
cancellation is exact and survives the branch ambiguity: `f_α(θ)=ρθ` holds
only mod `2π`, but it enters as `e^{i(f_α(θ)-ρθ)} = e^{2πik(θ)} = 1` ✓.  The
telescoping `(L_{V^{-1}}∘E∘L_V)^n = L_{V^{-1}}∘E^n∘L_V` is exact because
`L_V∘L_{V^{-1}} = id` ✓.  ⟨2⟩2: `E_α^n = P_α + O(λ̃^n)` gives
`φ_I(θ) → tr(V_θr)tr(V_θ^{-1}r)`, and
`tr(V_θ^{-1}r) = tr(V_θ^†r) = \overline{tr(V_θ r)}` for `V` unitary and
`r=r^†` — so the product is `|tr(V_θr)|²` ✓.  (The cited `[V_θ,r]=0` is not
needed for this identity; harmless.)  ⟨2⟩3: `spec Q_I^α ⊆ n(κ-ρ)+ℤ = ℤ` ✓.
Tightness closes: `φ_I → G` uniformly with `G` continuous and `G(0)=|tr r|²=1`,
so `u^{-1}∫_{-u}^u(1-Re φ_I) ≤ u^{-1}∫(1-G) + 2sup|φ_I-G| → 0` as `u→0`,
uniformly in `I` ✓.  Fourier inversion on `ℤ` plus tightness gives weak
convergence to (IDX.5) with total mass `1` ✓.  I confirmed the AKLT
cross-check of §7 IDX-C8 analytically: `ρ=0`, `V_θ=diag(e^{iθ/2},e^{-iθ/2})`,
`r=𝟙/2` give `G(θ)=cos²(θ/2)`, whose Fourier coefficients are exactly
`(1/4,1/2,1/4)` on `{-1,0,+1}` ✓.

**R3 (IDX-ρ.6, the truncation inequality — verified numerically and mutated).**
`u^{-1}∫_{-u}^{u}(1-Re φ)dθ = Σ_ν μ(ν)·2(1-\mathrm{sinc}(uν))`: reproduced to
`≤6.4e-12` at `u∈{0.3,0.7,1.0,π}` against a seeded 81-atom law.  The stated
threshold is correct and nearly sharp: `min_{|x|≥2}2(1-\mathrm{sinc}\,x) =
1.0907 ≥ 1` ✓ (`sinc 2 = 0.45465`), the sharp threshold being `x≈1.8955`.
See §2 for the red mutation.

**R4 (⟨1⟩7.⟨2⟩1--⟨2⟩4, the core of M-INDEX-spec).**  Double-Cesàro averaging
of (IDX.4): LR1 sends the two one-time terms to `ω^∓_W(Q̂_{W,c_0})` and LR2 is
exactly the statement that the averaged dephasing defect vanishes, giving
`Σ_ν ν p_W(ν) = ω^-_W(Q̂) - ω^+_W(Q̂)` ✓; substituting `Q̂=2s(𝔛_W-c_0)` the
common scalar `-2sc_0` cancels, giving
`Σ_ν ν p_W(ν) = -2s[ω^+_W(𝔛_W)-ω^-_W(𝔛_W)]` ✓; with the D27 definition of
`δx` this is `δx = -(2s)^{-1}Σ_ν ν p_ν` ✓, sign-consistent with §0's
`ν=-ΔQ_W`.  The tightness-only retreat of ⟨2⟩3 is correct: `ℤ` is closed and
every `p_W` lives there, so support quantization is subsequence-free, and only
uniqueness of the VALUE needs the convenience clause ✓.

**R5 (⟨1⟩8.⟨2⟩2, the AD3-topology lemma).**  Both halves check.  (i)
`‖PΨ-Ψ‖² = ⟨Ψ,(1-P)Ψ⟩ = 1-⟨Ψ,PΨ⟩` for a projection and a unit vector ✓, and
the named AD3 reading suffices exactly: weak-* convergence on the
finite-dimensional `𝔄_W` applied to `E_W({q_*}) ∈ 𝔄_W` gives
`⟨Ψ_t,E({q_*})Ψ_t⟩ → 1` ✓.  (ii) `|⟨R|E|T⟩| ≤ ‖E|T⟩‖ = ⟨T|E|T⟩^{1/2} → 0` ✓
(`E`	a projection, `‖R‖=1`).  Downstream, `‖E({q_R})(r|R⟩+t|T⟩)‖² → |r|²` and
`‖E({q_T})(·)‖² → |t|² = ⟨N_T⟩` ✓, with the `ν`-sum finite at fixed `W`.  The
strengthened reading is disclosed in ⟨1⟩8's ASSUME, in HONEST STATUS and in
the M-INDEX-spec row — r1 objection 4 is closed without over-reach.

**R6 (⟨1⟩12, mechanism B).**  `Q̂_{W'}-Q̂_W = Σ_{x∈I}S^z_x - sℓ`, which is the
⟨1⟩11 shell charge `Q_I^α` precisely when `s=ρ` (see Objection 4).  On-site
commutation gives `‖(e^{iθQ̂_{W'}}-e^{iθQ̂_W})Ω‖² = 2-2Re⟨Ω,e^{iθQ_I^α}Ω⟩` ✓
(the shard's `e^{-iθ}` version is equal, `Q` being self-adjoint).  ⟨2⟩3:
`tr(Vr) = ⟨r^{1/2},Vr^{1/2}⟩_{HS}`, so `|tr(Vr)| ≤ tr(r) = 1` with equality
iff `Vr^{1/2} = λr^{1/2}`, i.e. — `r>0` being invertible — iff `V ∈ U(1)𝟙` ✓.
The iterated limit is exactly what a Cauchy failure needs (for every `W` there
is `W'⊃W` with the increment bounded below) ✓.  Consistency with ⟨1⟩10 at
`θ∈2πℤ` is correctly noted ✓.

**R7 (T2, the repaired Cook majorant — the `|t|^{-3}` claim).**  The `S(u)`
split is correct.  Substituting `m:=y-y''`, `u:=y''-x` gives
`‖T_M‖ ≤ C_aΣ_{x,y''}|F_t(x,y'')|S(u)`, `S(u)=Σ_m|h_γ(m)||θ_c(u)-θ_c(u+m)|` ✓.
(S1) `S ≤ 2‖h_γ‖_1` ✓.  (S2) for `|u|>2w`, `θ_c` is constant on both sides, so
a nonzero difference forces `|m| ≥ |u|-w ≥ |u|/2`, whence
`S(u) ≤ 2Σ_{|m|≥|u|/2}|h_γ(m)| ≤ C'_N⟨u⟩^{-N-1}` ✓ — and this is where
rapid decay is genuinely consumed.  On the product of the main cones
`|u| ≥ ε_v|t|/2`, so `S·‖F_t‖_1 = O(|t|^{-N-1})·O(|t|²) = O(|t|^{1-N})` ✓;
off them `Σ_{off}|F_t| ≤ ‖1_{out}f_t‖_1‖g_t‖_1 + ‖f_t‖_1‖1_{out}g_t‖_1 =
O(|t|^{2-N})` with (S1) ✓.  The defect term obeys the same split ✓.  Binding
piece `O(|t|^{2-N})`; `N≥5` gives `C|t|^{-3}`, integrable, and `N≥4` already
suffices ✓.  **The `|t|^{-3}` claim is verified.**  I also checked the repair
covers the KINK side, which r1 objection 1(b)(iii) flagged: `Hκ_a(x) =
Γ_K(E_Kχ_Ke_xe_a)` and `Σ_{x'}h_K(x'-x)κ_{a'}(x') = Γ_K(h_Kχ_Ke_xe_a)` differ
by `Γ_K(E_K(1-χ̃_K)χ_Ke_xe_a) = 0` since `χ̃_K≡1` on `supp χ_K` ✓ — exact, no
defect, and `h_K` rapidly decreasing by the same argument as `h_γ` ✓.

**R8 (⟨1⟩6.⟨2⟩1, four-cluster — attacking truncation-radius uniformity).**
The attack fails; the step is sound and uniform.  With `y,y'` at distance `≥r`
from `{x,x'}`, truncate `a(y)^†` and `a(y')` at radius `2r/3`: the operator-norm
error is `≤ C_N⟨2r/3⟩^{-N}·2C_a` uniformly in `y,y'` (⟨1⟩3.⟨2⟩2 gives almost
locality uniformly in `n`), and the union of the two balls sits in the half-line
`(-∞,min(x,x')-r/3]` (resp. `[max(x,x')+r/3,∞)`) — so **ACE-tail** applies at
separation `r/3` and returns `C'_N⟨r⟩^{-N}` ✓.  A disconnected `Λ` inside one
half-line is admitted by (D28-C) as displayed ✓, and no dependence on `|y-y'|`
enters ✓.  I also checked ACE-tail itself (⟨1⟩3.⟨2⟩6): the split at
`|x̄-x|≤r/2` keeps `Λ_α,Λ_β` on their sides at separation `≥r/2` ✓, the
off-diagonal weights sum to `‖χ̂_K‖_1C'_N⟨r⟩^{-N}` ✓, and uniformity in `x,x'`
(hence in `t`) is exactly D28-P(5)'s uniformity clause ✓.  Finally
`ω_γ(a(y)^†a(y')) = ⟨π_γ(a(y))Ω_γ,π_γ(a(y'))Ω_γ⟩ = G_γ^{bb'}(y,y')` by
D28-P(3) ✓.  The multi-cluster form r1 objection 3(ii) demanded is genuinely
DERIVED from the single displayed cut, which is stronger than the fix demand.

**R9 (T2 §6 repair table, row by row).**  Rows 1, 3, 5, 6, 7, 8 verified as
described; row 2 verified (D28-R now says "used nowhere in the proof", the
claims row says "threshold-inequality use ... not claimed", `--red-absorption`
is demoted in §4, and no step cites the renumbered `P(5)` meaning thresholds —
I checked every `D28-P(5)` citation: ⟨1⟩3 ASSUME, ⟨1⟩6 ASSUME, ⟨1⟩6.⟨2⟩3, all
two-cluster); row 4 correctly labelled DOWNGRADED, not FIXED.  ⟨1⟩7.⟨2⟩2's
cross-term derivation is correct: `P_LΨ_t ≈ E_W({q_L})Ψ_t` by (AD3-ex), so
`E_W({q_T})P_LΨ_t → 0` by orthogonality of spectral projections ✓.
**Self-flagged risk adjudication.** (i) *Two-sided D28-C pricing:* the
two-sided form is genuinely stronger than a one-sided display and is genuinely
needed — ⟨1⟩6.⟨2⟩3's operator `A·B` sits on opposite tails and cannot be
reduced to a one-sided application; a factor `2` from two cuts is absorbed by
`C_cl`.  Correctly self-priced; it is displayed and citable.  (ii)
*Truncation-radius uniformity:* survives, see R8.  (iii) *ACE-C2 red
scalings:* correct analytically — `Σ_{|m|≥R}c⟨m⟩^{-2} ≍ 2c/R` with
`R≍ε_vt/2`, so `C_θ ≍ t^{-1}`, doubling exponent `→ -1`, octave contribution
`→ c'\ln 2` and ratio `→1`, so both gates fail as designed; the `ℓ²`-versus-`ℓ¹`
mismatch does not change the scaling because the kernel tail acts as a scalar
multiplier on the cone.  Unrun, however — see the AC-EX decision.  (iv) *The
`HΩ_γ=0` leaf:* legitimate.  H-MQG(3) makes both vacua stationary, so the GNS
generator may be normalised to annihilate the invariant vector; ⟨1⟩3.⟨2⟩4 uses
it only inside `H_γ`, and the resulting `ω_γ(D^†D)=0` reaches `H_{αβ}` only
through (D28-C), as convention (C1) requires.  See NOTE 13 for the ledger.
(v) *L2 length:* ruled in §3.

**R10 (L3 / citation audit on the new material).**  D2(b)'s uniqueness clause
is quoted verbatim and applied correctly (R1).  A2's weak-* clause with rate
`λ̃^{y-w}` is PROVED and cited exactly as ⟨1⟩12.⟨2⟩2 uses it.  Lemma IT
resolves via D2(c) ("proved in corner-a.md ⟨1⟩2").  B3's
`2s·δx+(q_out-q_in)=0` is PROVED and matches ⟨1⟩7.⟨2⟩3's use, once averaged
over the outcome law — legitimate here only because (AD3-ex) kills the
coherent cross term, which the shard states.  M-quant-G (G.1)--(G.2) match
⟨1⟩8.⟨2⟩4 (re-verified in r1 V6).  No citation-from-memory defects found.

**R11 (T1 diff discipline).**  Every deletion from the `a67e61b` baseline is
traceable to a named objection or synthesis-notes item: the `ρ_{W,c_0} →
κ_{W,c_0}` rename (L4), the collar clause and LR4 (r1 objection 1), the
weakening of (G-IDX.2) to subsequential form (r1 objection 2), the ⟨1⟩3b
conjecture (r1 objection 3), the ⟨1⟩8 lemma and AD3 reading (r1 objection 4),
the ⟨1⟩4.⟨2⟩2 leaf (r1 NOTE 6).  **No silent strengthening in the diff** — the
one change to a conclusion is a weakening.  The header's claim holds.

---

## 1. Objections

### MAJOR

**Objection 1 — MAJOR.  The new `notation.md` `ρ` row re-imports, at the file
L4 designates as the single source, exactly the circularity that
memory-index-b-r1 objection 1 called MAJOR.**

(a) `notation.md` row `ρ (density)` (merged from memory-index.md §8.3), read
against `notation.md`'s standing `s` row ("site spin, `d = 2s+1`") and
`definitions.md:579` ("`s` denotes the site spin (`d = 2s+1`)").

(b) My computation.  The new row says `ρ` is "deliberately distinct from D13's
site-spin `s`" and then, in the same parenthesis, "(H-MQG(2) identifies the
D13(a) calibration parameter with `ρ`)".  The parenthesis is *accurate*:
H-MQG(2) reads `ω_α(S^z)=+s`, `ω_β(S^z)=-s`, `s>0`.  But composing the two
live notation rows gives `ρ = s` and `2s = d-1 ∈ ℕ`, hence `2ρ ∈ ℕ` **by
symbol resolution alone**, with no proof read — the exact inference lane B was
failed for.  M-IDX-density's headline ("derived, not assumed") is therefore
false as the shared files now stand, even though ⟨1⟩9 itself is clean (R1).
The underlying collision is *pre-existing* — `definitions.md:579`/`notation.md`
say `s` is the site spin, D13(a)'s own body and H-MQG(2) say `s` is the vacuum
density, and the two agree only for a fully polarised vacuum — but this merge
is the first place both readings are asserted in one sentence, and it is the
merge whose headline depends on keeping them apart.

(c) FIX DEMAND.  Replace the parenthesis in the `ρ` row by: "H-MQG(2) fixes the
D13(a) calibration parameter to be the tail density, `s=ρ`; `notation.md`'s
`s`-row gloss `d=2s+1` is the fully polarised special case and is NOT a
constraint on `ρ` — M-IDX-density (⟨1⟩9) assumes no relation between `ρ` and
the on-site dimension."  Add the same one-line fence to `notation.md`'s `s`
row and to `definitions.md:579`.

(d) SURVIVING WEAKER STATEMENT.  M-IDX-density exactly as proved in ⟨1⟩9:
`e^{2πiρ}=c=e^{-2πiρ}`, hence `2ρ∈ℤ`, under D1, D2(a,b,e), (S) at both tails,
D26(INT) and the antisymmetry `ω_β(S^z)=-ρ`.

**Objection 2 — MAJOR.  The AC-EX claims row drops a stated hypothesis of
ACE.3 and discards the `ex` superscript its own notation row exists to
protect.**

(a) `claims/CLAIMS.md` AC-EX row, second sentence; against
`theory/ansatz-scattering.md` ACE.3, ⟨1⟩7's ASSUME, and `notation.md`'s
`H_out^{ex}, N_T^{ex}` row.

(b) ACE.3 reads "for a normalized event vector in `ran W_-^L∩H_out^{ex}`
**for which Lane T1's outcome measure exists**", and ⟨1⟩7's ASSUME lists that
existence explicitly — correctly, since AC-EX assumes no D27(LR) and therefore
produces no ordered-limit measure of its own.  The row instead reads "on
vectors lying in both the constructed in- and out-ranges the T1 measure has
constructed support `{0,2}`", which asserts the existence the theorem
hypothesises.  Second, the row writes `N_T` and `p_2=⟨N_T⟩` where the theorem
writes `N_T^{ex}` and `⟨Ψ,N_T^{ex}Ψ⟩`; `notation.md`'s new row was added
precisely to separate `N_T^{ex}` ("no completeness implied") from D18's `N_T`,
so the DAG row defeats its own notation entry.  Both defects are in the
citable surface (work-order obligation 4): the row text is what a later reader
quotes, and it currently exceeds the shard in the one direction that matters.

(c) FIX DEMAND.  Restore the existence qualifier and both `ex` superscripts
verbatim; see the AC-EX scoping sentence in §4.

(d) SURVIVING WEAKER STATEMENT.  AC-EX exactly as the shard states it: ACE.1
and ACE.2 under D28 (incl. D28-C); ACE.3 conditional on (AD3-ex) *and* on the
existence of Lane T1's ordered-limit measure for the vector in question.

**Objection 3 — MAJOR.  `memory_index_check.py` over-reports its red coverage:
the only mutation aimed at the two-tail relation ⟨1⟩9.⟨2⟩4 — the single
load-bearing hypothesis of M-IDX-density — is unreachable in red mode, and its
green surrogate is insensitive to the premise it names.**

(a) `theory/checks/memory_index_check.py:544` (red sets `shift=0.1`), `:554`
(`require(worst_sym < TOL_EXACT)`), `:598-608` (mutation (ii) and its `if red:`
branch), `:21-22` (module docstring), SPEC NOTE 2 at `:65-71`; commit
`a529a10`'s message; the addendum to `briefs/r2-adjudication.md`.

(b) My computation, run directly.  In red mode `check_c7` sets `shift=0.1`,
so `worst_sym = 2.000` and the `require` at `:554` raises immediately — the red
run's own line is `IDX-C7(b): |phi_W(2 pi) - 1| = 2.000e+00 over n=2..12,
cuts -2..2`, i.e. line 554.  Execution therefore **never reaches** `:601-604`,
so the tail-covariance-phase mutation is dead code in the mode that is supposed
to exercise it, and the docstring's claim that `--red` "applies the spec's
named mutation to every check" is false for C7.  The green liveness check at
`:605` does run, but its value is set by the counterterm mismatch `(ρ, -ρ+0.2)`
and is independent of `β`'s non-covariance — the number `1.9021130325903` is
reproduced to 15 digits by a *covariant* `β` and by random junk tensors.  So
the step whose necessity I independently established (Objection 10: without
the antisymmetric pair one gets only `ρ_α-ρ_β∈ℤ`, not `2ρ∈ℤ`) has no working
red test at all.  Two further coverage over-reports in the same file:
`SPEC_NOTES` contains **four** entries (`:60-79`), not the six the commit
message and this work order both assert; and `:696`'s "quantified tightness
bound of IDX-ρ.6" is vacuous on its own instantiation — the χ=2 family's
`μ_I` is supported on `{-1,0,+1}` for every `|I|` while the cutoffs are
`2/u ∈ {2,4,8,16}`, so the asserted `tail ≤ integral` compares an exact `0`
against a positive number, twenty times.  This is a certificate silently
weakened relative to its spec, which the work order prices as MAJOR.  (Two
deviations go the other way and are honest strengthenings: SPEC NOTE 1 adds the
asymmetric family `[-n,2n]` to recover the spec's `n`-drift claim after finding
it false on symmetric windows, and SPEC NOTE 4 detects that the
wrong-environment mutation is vacuous on AKLT and re-registers it on the
charged χ=2 draw behind an explicit anti-vacuity guard at `:641`.  SPEC NOTE 3
is neutral.)

(c) FIX DEMAND.  (i) Split `check_c7` so that red mode runs mutation (ii)
independently of mutation (i) — e.g. two red branches, or a per-mutation flag —
and make the mutation-(ii) assertion depend on `β`'s covariance rather than on
the counterterm: assert that `φ_W(2π)` deviates when the counterterm is held
at the *correct* `(ρ,-ρ)` and only the tensor's tail covariance is broken.
(ii) Reconcile the SPEC NOTE count in the commit record: four are printed;
say where the other two resolutions live.  (iii) Replace the IDX-ρ.6 assertion
by a non-vacuous one — the mutation in §2 below is the ready-made red test.
(iv) Correct `:21-22`.

(d) SURVIVING WEAKER STATEMENT.  IDX-C1's (IDX.4) residue (two independent
routes), IDX-C5's exact symbolic reduction, IDX-C6's 50-draw density
certificate, and IDX-C8's convergence-rate, obstruction and deep-shell kink
results are load-bearing and green; the *proof* of ⟨1⟩9 stands on its own
(R1) and is not in question.  What is not currently certified is the necessity
of ⟨1⟩9.⟨2⟩4.

### MINOR

**Objection 4 — MINOR.  ⟨1⟩11 and ⟨1⟩12 consume `s=ρ` without listing it, and
⟨1⟩11.⟨2⟩3 imports it through a step that carries it needlessly.**
(a) ⟨1⟩11 ASSUME ("As ⟨1⟩9"), ⟨1⟩11.⟨2⟩3, ⟨1⟩12 ASSUME, ⟨1⟩12.⟨2⟩1.
(b) ⟨1⟩9's ASSUME deliberately excludes H-MQG(2) and `s=ρ` — that exclusion is
the decircularization.  ⟨1⟩11.⟨2⟩3 needs only `κ≡ρ (mod ℤ)`, which follows
from ⟨1⟩9.⟨2⟩3 (`c=e^{2πiρ}`) and ⟨1⟩1.⟨2⟩1 (`c=e^{2πiκ}`) with no `s`
anywhere; but the leaf cites ⟨1⟩10.⟨2⟩1, whose ASSUME does carry `s=ρ`, so the
leaf imports a hypothesis its own ASSUME disclaims.  ⟨1⟩12.⟨2⟩1 *genuinely*
needs it: `Q̂_{W'}-Q̂_W = Σ_{x∈I}S^z_x - sℓ` equals `Q_I^α = Σ_{x∈I}(S^z_x-ρ)`
only when `s=ρ`, and that hypothesis appears in neither ⟨1⟩12's ASSUME nor the
M-INDEX-LA-strong row's mechanism-B clause.
(c) FIX: in ⟨1⟩11.⟨2⟩3 cite ⟨1⟩9.⟨2⟩3 + ⟨1⟩1.⟨2⟩1 and drop ⟨1⟩10 (removing
the hypothesis outright); add "H-MQG(2)'s `s=ρ`" to ⟨1⟩12's ASSUME and to the
M-INDEX-LA-strong row's mechanism-B parenthesis.
(d) Surviving: ⟨1⟩11 verbatim (it needs no `s`); ⟨1⟩12 verbatim under an
explicit `s=ρ`.

**Objection 5 — MINOR.  Three DAG edges the same merge batch made available
are missing.**
(a) M-INDEX-spec depends-on; AC-EX depends-on and ⟨1⟩7.⟨2⟩3; M-IDX-density
depends-on.
(b) M-INDEX-spec's support-on-`ℤ` conclusion runs through ⟨1⟩5.⟨2⟩3, whose
sole justification is "L-A-fin ⟨1⟩1" — that is **M-INDEX-fin**, a separate row,
absent from the edge list.  AC-EX's ⟨1⟩7.⟨2⟩3 consumes Lane T1's ledger
formula and the shard's own merge note says to cite the T1 row "once merged";
it merged in the same batch (`e0ce677` before `2cd5ec2`), yet ⟨1⟩7.⟨2⟩3 still
points at `briefs/memory-campaign-target.md` and AC-EX's depends-on omits
M-INDEX-spec.  M-IDX-density's depends-on reads "D1, D2(b,e), D26" while both
its own statement text and ⟨1⟩9's ASSUME name D2(a).  Missing edges misprice
the graph in exactly the way r1 objection 8 flagged for the *spurious*
M-quant-G edge — here a later status change would fail to propagate.
(c) FIX: add M-INDEX-fin to M-INDEX-spec; add M-INDEX-spec to AC-EX and
replace the brief reference in ⟨1⟩7.⟨2⟩3 by the row id; change
M-IDX-density's depends-on to "D1, D2(a,b,e), D26".
(d) Surviving: all three claims at their stated strength; only the graph is
wrong.

**Objection 6 — MINOR.  The AD3-ex row misdescribes both what (AD3-ex) says
and what is proved of it.**
(a) `claims/CLAIMS.md` AD3-ex row; against ⟨1⟩7's displayed ASSUME and ⟨2⟩2.
(b) The displayed hypothesis is
`lim_{t→+∞}‖E_W({q_ch})Ψ_t - P_{ch}Ψ_t‖ = 0`, the limit before `W↑ℤ`.  The row
states instead "outgoing boundary-straddling charge on `∂W` vanishes in the
ordered limit" — that is the shard's description of the missing *mechanism*
(the ACE-LD gap), not the hypothesis, and the row is the citable text.
Second, "the cross-term half is proved in ⟨1⟩7.⟨2⟩2" reads as "AD3-ex is half
proved".  It is not: ⟨1⟩7.⟨2⟩2 *derives* cross-term vanishing **from**
(AD3-ex) (R9), entirely downstream.  No part of (AD3-ex) is proved anywhere.
(c) FIX: quote the displayed limit verbatim, and replace the last clause by
"no part of (AD3-ex) is proved; ⟨1⟩7.⟨2⟩2 derives the inter-channel cross-term
vanishing FROM it, which is one of the two items r1 objection 4 demanded."
(d) Surviving: AD3-ex at CONJECTURE, as recorded.

**Objection 7 — MINOR.  D26 writes `ρ>0` into the definition in the act of
disclaiming conditions on `ρ`, and the constraint excludes the shard's own
registered cross-check.**
(a) `definitions.md` D26, third sentence (and memory-index.md §8.1); against
⟨1⟩9's ASSUME and §7 IDX-C8's AKLT cross-check.
(b) "No condition on the real tail-density parameter `ρ>0` is included" is
self-undercutting.  ⟨1⟩9 assumes only `ρ:=ω_α(S^z)` with `ω_β(S^z)=-ρ`, and
its conclusion `2ρ∈ℤ` admits `ρ=0`.  The AKLT cross-check registered in
IDX-C8 *is* the `ρ=0` case, and it is internally consistent (`c=e^{2πi·0}=1`,
matching `e^{2πiS^z}=I` for spin 1; `G(θ)=cos²(θ/2)`; law `(1/4,1/2,1/4)` —
recomputed in R2).  So D26 as written excludes a case the shard registers and
the checker runs green on.
(c) FIX: "No arithmetic condition on the real tail-density parameter `ρ` is
included (`ρ=0` is admitted; H-MQG(2)'s `s>0` is a separate hypothesis of the
kink setting)."
(d) Surviving: D26 and ⟨1⟩9 with `ρ` unrestricted.

**Objection 8 — MINOR (L4).  The merge blocks are now verbatim duplicates of
live shared files.**
(a) memory-index.md §8 (D26, D27, five claim rows, six notation rows);
ansatz-scattering.md §5 (D28 + Remark D28-R, the AC-EX row, nine notation
rows); against definitions.md:1008-1151, claims/CLAIMS.md, notation.md.
(b) Before the merge these were proposals and legitimately lived in the
shards.  After `e0ce677` and `2cd5ec2` the same text is live, so D26, D27, D28
and fifteen notation rows exist twice.  L4 says every definition lives exactly
once and shards reference it.  The duplication is not cosmetic: L6b makes the
shard the ground truth for the proof, so a later edit to `definitions.md` D28
would leave the proof reading a stale hypothesis — and the two copies already
differ in framing ("proposed D26/D27", "D28-P" versus the live D-numbers).
(c) FIX: replace §8 and §5 by a two-line pointer to the live locations, and
drop the "proposed"/"-P" prefixes from the proof text in favour of the live
D-numbers.
(d) Surviving: both shards' mathematics unchanged.

**Objection 9 — MINOR.  §7's findings-of-record over-credit probe P2, which is
an arithmetic rather than a dynamical certificate.**
(a) memory-index.md §7 "Findings of record (i)"; M-INDEX-fin's where-tested
cell; `memory_index_probe.py:344-350`, `:233-238`, `:338-341`, `:352-359`.
(b) The probe builds `Q_W` from `site_sz` (exactly `±0.5`) minus `rho_vac`
(exactly `±0.5`), so every eigenvalue is an exact IEEE integer and
`off_lattice` is identically `0.0` for *any* probability vector — evolved,
unevolved, or random.  P2 therefore cannot fail for any state, Hamiltonian or
time, yet §7 glosses it as "the (G-IDX.0/2) content".  It does correctly
certify the offset arithmetic at this instantiation — which is what
(G-IDX.0) asserts — but it certifies nothing about the *law*, which is
(G-IDX.2), and the genuinely nontrivial empirical finding (the extra integer
mass at `Q_W∈{-1,-3}`) is P3's content, not P2's.  The red mutation's
sensitivity is likewise arithmetic: `RED_RHO_SHIFT=0.3` times a 10-site window
is exactly `3.0`, so all three 10-site windows are silent under red and P2
tracks only `n_sites × shift mod 1`.
(c) FIX: reword §7(i) to "P2 certifies that `spec Q̂_W ⊂ ℤ` holds by
construction of the observable in the D16 instantiation — an arithmetic
certificate of (G-IDX.0), not a dynamical one; the outcome-support finding
(extra integer mass at `Q_W∈{-1,-3}`) is P3's", and amend M-INDEX-fin's
where-tested cell accordingly.  Consider a red shift coprime to the window
widths.
(d) Surviving: the P1/P3/P4/P5 findings, and P2 as an arithmetic certificate.

### NOTE

**NOTE 10.  The M-IDX-density row's LSM sentence drops the antisymmetry its
own first clause carries.**  The row correctly conditions on "tail densities
`(+ρ,-ρ)`", then says "LSM-flavored: U(1)-covariant injective MPS tails admit
only half-integer-quantized densities given (INT)".  Under D26 alone one tail
gives only `e^{2πiρ}=c`, i.e. `ρ∈κ+ℤ` — for arbitrary `c` that is not
half-integrality; a general tail pair gives only `ρ_α-ρ_β∈ℤ`.  `2ρ∈ℤ` needs
the antisymmetric pair.  FIX: append "— for an antisymmetric tail pair; one
tail alone gives only `ρ∈κ+ℤ`, and a general pair only `ρ_α-ρ_β∈ℤ`."

**NOTE 11.  ⟨1⟩3b bundles a one-line consequence with the hard part.**  If the
strongly continuous implementer `U(θ)` exists and `ϱ_0` is pure (so the GNS
representation is irreducible), then `e^{2πiQ̂}` implements
`Ad(u(2π)) = Ad(c𝟙) = id`, hence lies in `π(𝔄)' = ℂ𝟙` by Schur — the scalar
clause is free.  The entire content of the conjecture is EXISTENCE of the
implementer on the kink folium.  FIX: say so in ⟨1⟩3b and in the
M-INDEX-LA-folium row, so a future prover attacks the right statement.

**NOTE 12.  Stale "proposed" / "to implement after merge".**  memory-index.md
§7's heading and the where-tested cells of M-INDEX-fin, M-INDEX-spec,
M-IDX-density and M-INDEX-LA-strong all call `memory_index_check.py`
"proposed"; it is committed at `a529a10` and runs green (§2).  FIX: drop
"proposed", record the run status and the green/red exit codes.

**NOTE 13.  D28(1)'s new `HΩ_γ=0` clause is not in the §6 "no silent
strengthening" ledger.**  The r2 edit added it under objection 6's repair; the
ledger's items (i)--(v) do not mention it.  It is derivable (R9(iv)) and is
used only inside `H_γ`, so nothing is wrong — but the ledger is the artifact
that certifies completeness.  FIX: add clause (vi), labelled a normalisation
consequence of H-MQG(3), not a new assumption.

**NOTE 14.  ⟨1⟩8.⟨2⟩2(i) mixes a fixed-time subscript with a running vector.**
The display writes `‖E_{W,t_-}({q_*})Ψ_t - Ψ_t‖²`, but `E_{W,t_-}` is the
resolution at the *fixed finite* `t_-` of ⟨1⟩5--⟨1⟩6 while `Ψ_t` runs to
`-∞`.  The intended object is `⟨Ψ,E_{W,t}({q_*})Ψ⟩ = ⟨Ψ_t,E_W({q_*})Ψ_t⟩`.
The identity itself is right (R5).  FIX: index consistently.

---

## 2. Checker adjudication (work-order obligation 3)

**Runs** (all with `python3 -O`; neither file contains a bare `assert`, so
`-O` is genuinely strict):

| invocation | exit | outcome |
|---|---|---|
| `memory_index_probe.py` | 0 | PASS, P1--P5 green |
| `memory_index_probe.py --red` | 1 | red caught: 190 pre-registered violations (6 P1, 180 P2, 2 P3, 2 P4; **P5 unchanged**, 3.38e-03 in both modes) |
| `memory_index_probe.py --selftest` | 0 | PASS |
| `memory_index_check.py` | 0 | PASS, IDX-C1--C8 green |
| `memory_index_check.py --red` | 1 | `RED-OK`, 8/8 checks report "caught" |

Both files expose only `--red` (all mutations at once); there are no
per-mutation flags.  Green highlights: `IDX.4` residue `5.6e-17`; C2 dephasing
defect `1.048e-01`; C6 `max|ω(S^z)-ρ| = 3.3e-16` over 50 seeded draws with a
mutant spread of `0.417`; C7 conjugation residue `2.2e-16`; C8 `sup|φ_I-G| =
6.7e-15` at `|I|=40`, fitted rate `0.1180 ≤ λ_E = 0.4292`, AKLT law
`(1/4,1/2,1/4)`, obstruction `1.934`.  All stochasticity is seeded and the runs
are byte-reproducible.

**SPEC NOTE deviation audit.**  Four are printed (`:60-79`), not six.  Notes 1
and 4 are honest *strengthenings* (Note 1 finds the spec's "drifting with `n`"
false on symmetric windows — `a+b-1-2c` carries no `n` — and adds the
asymmetric family `[-n,2n]` to recover it; Note 4 detects that the
wrong-environment mutation is vacuous on AKLT, where `r=𝟙/χ`, and re-registers
it on the charged χ=2 draw behind an anti-vacuity guard).  Note 3 is neutral
and honest (it is right that no charge-diagonal tensor realises a
non-half-integer density in a fixed physical space, so the irrational coset is
reached by shifting `S^z`).  **Note 2 is a silent weakening** — Objection 3.
Beyond the notes, three further certificates are vacuous as instantiated and
should not be counted as evidence: IDX-C4 (every assertion is an arithmetic
identity of the hand-written toy laws, and the red mutation is an *inserted*
false assertion rather than a perturbed premise), IDX-C7(b)'s window/cut/kink
battery (at `θ=2π` with half-integer spins every factor is `1`, so the
identity holds for arbitrary matrices), and IDX-C8's IDX-ρ.6 tail bound
(Objection 3).  IDX-C3's red catch comes solely from the closed-form
`V_N ≥ log N - 0.5` test; its mass, local-CLT and resolvent-monotonicity
assertions all survive the mutation, so the thirteen FFTs contribute nothing
to the catch.

**My additional mutation (a copy in `/tmp`, hypothesis of my choosing).**  I
targeted **IDX-ρ.6**, the truncation inequality at ⟨1⟩11.⟨2⟩3 — chosen because
it is a named computation at a load-bearing leaf (tightness) and, per
Objection 3, the committed checker's version of it cannot fail.  Green: the
identity reproduces to `≤6.4e-12` (R3), and the stated threshold holds with
`min_{|x|≥2}2(1-\mathrm{sinc}\,x) = 1.0907 ≥ 1`.  Red: mutate the threshold
`2/u → 1/u`.  Then `min_{|x|≥1}2(1-\mathrm{sinc}\,x) = 0.3171 < 1`, failing on
`x∈[1, 1.8955]`, and the concrete law `μ = ½(δ_{-1}+δ_{+1})` at `u=1` breaks
it decisively: the mutated bound claims `1.000 ≤ 0.3171`, false, while the
stated bound claims `0.000 ≤ 0.3171`, true.  **The leaf is correct and its
constant is nearly sharp** (the sharp threshold is `x≈1.8955`, so `2` has only
`5%` of slack) — which is exactly why the committed vacuous version should be
replaced by this one.

---

## 3. L2 ruling (work-order obligation 5)

**Ruling: the splits are POST-promotion hygiene, with two carve-outs that are
pre-promotion because they are L4, not L2, defects.**

Reasoning.  L2 is a maintainability law; line count does not bear on whether a
claim is true, and L5's promotion gate is convergence of the L6 loop, which is
about fatal/major objections.  Splitting a Lamport-structured proof is a
mechanical edit across dozens of `⟨1⟩n.⟨2⟩m` cross-references, performed on an
artifact whose correctness has just been certified; doing it *before*
promotion would force a re-verification round for zero mathematical gain.  Both
shards self-report the overrun with a proposed remedy, so nothing is hidden.

The carve-outs, which ARE due before promotion:
1. **Objection 8 (L4).**  §8 of T1 and §5 of T2 are now verbatim duplicates of
   live `definitions.md`/`notation.md`/`CLAIMS.md` content.  Deleting them in
   favour of pointers is required by L4 independently of L2, and it removes
   ~80 lines from T1 and ~145 from T2 as a side effect.
2. **No status upgrade in the same commit as a split**, so the promoted text
   and the restructured text stay separately reviewable.

The L2-correct cut for T1, when it is taken, is **§5 (⟨1⟩9--⟨1⟩12) →
`theory/memory-index-density.md`**: that is a genuinely distinct lemma cluster
(density quantization, zero offset, vacuum charge laws, mechanism B) with its
own claim row (M-IDX-density) and its own hypothesis package ((S) at both
tails), and §§2--4 explicitly do not depend on it.  That cut satisfies L2's
"one lemma-cluster per file" clause, which is the substantive complaint —
not the raw 976.  For T2 the shard's own proposal (§5 → `theory/merge/`,
§6 → `theory/verdicts/ansatz-scattering-r2-response.md`) is correct and,
combined with carve-out 1, brings the proof proper to ~400 lines, inside L2.

---

## 4. Decision table

Every PROMOTE is gated on the MAJOR fixes named in its row; the scoping
sentence is to be copied into the DAG **verbatim**, appended to the row's
statement cell.

| Row | Decision | Gate |
|---|---|---|
| **M-INDEX-fin** | **PROMOTE** SKETCH → **PROVED** | Objection 9 (where-tested wording) |
| **M-INDEX-spec** | **PROMOTE** SKETCH → **PROVED (conditional)** | Objections 4, 5 |
| **M-IDX-density** | **PROMOTE** SKETCH → **PROVED** | Objections 1 **and** 3 (both mandatory) |
| **AC-EX** | **HOLD** | missing step named below |
| **M-INDEX-LA-strong** | **CONFIRM REFUTED** | Objection 4 (disclose mechanism B's hypotheses) |
| **M-INDEX-LA-folium** | **CONFIRM CONJECTURE** | NOTE 11 |
| **AD3-ex** | **CONFIRM CONJECTURE** | Objection 6 |

**M-INDEX-fin — PROMOTE.**  ⟨1⟩1 and ⟨1⟩5 are elementary and were verified in
r1 (V1, V4) and again here (R4, R5); IDX-C1's (IDX.4) residue is a genuine
two-route certificate.  Scoping sentence:

> Hypotheses in full: D26(INT), H-MQG(2) (which fixes the D13(a) calibration
> parameter `s>0` to be the tail density), a finite window `W=[a,b]` and a cut
> `c_0∈W`; the coset is `κ_{W,c_0} ≡ |W|κ + s(a+b-1-2c_0) (mod ℤ)` and is
> time-independent because `α_t` is a C*-automorphism.  Integrality of the TPM
> increment is offset cancellation at fixed `W` (⟨1⟩5.⟨2⟩3), not spectral
> arithmetic for a difference of noncommuting operators; probe P2 certifies
> `spec Q̂_W ⊂ ℤ` by construction of the observable in the D16 instantiation
> and is an arithmetic, not a dynamical, certificate.

**M-INDEX-spec — PROMOTE, as a conditional implication only.**  R4 and R5
close the chain; r1's V2--V4 and V6 close the offset bookkeeping and the
M-quant-G reduction.  Scoping sentence:

> Proved only as the conditional implication: H-MQG(1)--(4) + D26(INT) +
> D27(LR1--LR3, tightness-only) ⟹ every (LR3)-subsequential ordered TPM
> escaped-charge law is a probability on `ℤ` with `δx = -(2s)^{-1}Σ_ν ν p_ν`
> **along that subsequence**; support quantization is subsequence-free, and
> D27's optional convenience clause buys uniqueness of the VALUE `δx` and
> nothing else.  The reduction clause is a further conditional: it additionally
> assumes H-AD-G with D18(AD3) read as weak-* convergence of the window
> restriction, per channel, to the corresponding kink charge eigenstate — a
> reading D18's frozen words do not fix.  D27 is assumed, not derived; no
> implication H-AD-G ⟹ (LR) is claimed; no sector-wide total-charge operator is
> constructed, and its unconditional existence is REFUTED (M-INDEX-LA-strong).

**M-IDX-density — PROMOTE, gated on Objections 1 and 3.**  The proof is
complete and independently re-derived leaf by leaf (R1), including the D2(b)
uniqueness application quoted verbatim from the TeX.  The gate is not
advisory: as the shared files stand the claim is trivialised by symbol
resolution (Objection 1), and its one load-bearing hypothesis has no working
red test (Objection 3).  Scoping sentence:

> Hypotheses in full: D1 injective tensors `A_α,A_β`, D2(a) covariance with a
> common unbroken circle direction `ξ∈𝔥_α∩𝔥_β`, D2(b)'s uniqueness clause, (S)
> of D2(e) at both tails, D26(INT), and the ANTISYMMETRY
> `ω_β(S^z) = -ω_α(S^z) =: -ρ`.  The antisymmetry is load-bearing: one tail
> alone gives only `ρ∈κ+ℤ` and a general tail pair only `ρ_α-ρ_β∈ℤ`; `2ρ∈ℤ`
> needs the antisymmetric pair.  `ρ` is a free real parameter of the vacuum
> pair — `ρ=0` is admitted (the AKLT cross-check) — and no step assumes any
> relation between `ρ` and the on-site dimension `d`; `notation.md`'s `s`-row
> gloss `d=2s+1` is the fully polarised special case and is not imported here.

**AC-EX — HOLD.**  All four r1 MAJORs are genuinely repaired and I verified
each by recomputation, not by reading the table: the filtered-frame repair
restores the exact defect equations on *both* the magnon and the kink side
(R7), the Cook majorant closes at `C|t|^{-3}` (R7), (D28-C) is now a displayed
inequality with quantifiers, constants and time-uniformity, and the
multi-cluster form is derived rather than assumed and survives the
truncation-radius attack (R8).  **Missing step:** the two specified
certificates ACE-C1 and ACE-C2 are not implemented.  ACE-C2's
`--red-slow-kernel` mutation is the only evidence that the Objection-1 repair
is a real gain in decay rather than a re-parameterisation, and it is exactly
the borderline r1 left open (`C²(𝕋) ⟹ o(m^{-2})`, while Cook needs
`Σ_m|m||h(m)|<∞`).  I verified its scalings analytically (R9(iii)) and they
are correct — but this campaign has direct evidence that writing the checker
for a repaired quantitative estimate finds real defects: `memory_index_check.py`
caught one vacuous deep-shell test and two literally-unimplementable mutations
in the T1 lane, and this adjudication found three more vacuous certificates in
it (§2).  Promoting a repaired decay estimate whose red test has never run
would apply a weaker standard to T2 than T1 met.  Second, Objection 2's row
text must be repaired.  On those two, AC-EX promotes to **PROVED (conditional)**
for ACE.1--ACE.2 and remains conditional for ACE.3.  Scoping sentence to use
at that point:

> ACE.1--ACE.2 are proved only as the conditional implication: D28/H-ACE
> (exact kink and magnon band maps, covariant kink-sector realization,
> momentum-filtered creator normalisation, velocity separation `ε_v>0`, and
> the displayed **two-sided** two-cluster inequality (D28-C)) ⟹ the three Cook
> limits exist, `W_-^L` and `W_+=W_+^L⊕W_+^T` are isometries, and
> `N_T^{ex}:=W_+P_TW_+^*` is an orthogonal projection on `H_out^{ex}:=ran W_+`
> — D18's `N_T` restricted to that range, with nothing asserted on its
> orthogonal complement.  ACE.3 is conditional on **both** the named
> local-decay hypothesis (AD3-ex), which this shard does not prove, **and** the
> existence of Lane T1's ordered-limit outcome measure for the vector in
> question, which D28 does not supply.  (D28-C) is the load-bearing hypothesis
> and is unverified on any model; Remark D28-R's threshold inequalities are
> used in no step.  No completeness, raw-band-data implication, bound-state
> exclusion, or soft limit is claimed.

**M-INDEX-LA-strong — CONFIRM REFUTED.**  Mechanism A (⟨1⟩3) alone refutes the
row as stated, since the row quantifies over *every* `𝒦_{αβ}` GNS
representation and ⟨1⟩3 exhibits a state satisfying D9, D17 and D26(INT) whose
window charges have no strong-resolvent limit (verified in full at r1 V5).
Mechanism B (⟨1⟩12) is a strengthening, not a second proof of the same
statement: it needs (S), `s=ρ`, D1(e′), A2 and nonscalar `V_{θ_0}`, none of
which mechanism A needs.  The row should say so (Objection 4), so a reader does
not infer that the refutation depends on (S).

**M-INDEX-LA-folium — CONFIRM CONJECTURE.**  Neither proved nor refuted, and
correctly fenced against ⟨1⟩12 (the implementer route is not the
strong-resolvent-limit route).  Sharpen per NOTE 11: the scalar clause is a
Schur one-liner once the implementer exists, so the whole content is existence.

**AD3-ex — CONFIRM CONJECTURE.**  Nothing of it is proved; the row must stop
suggesting a half is (Objection 6).

---

## 5. Summary

Both shards are in materially better shape than their r1 verdicts.  T1's
synthesis honours every one of lane B's six FAIL objections at the critic's
surviving strength, and I could not find a silent strengthening anywhere in
the diff — the one changed conclusion is a weakening.  T2's four MAJORs are
genuinely repaired, and the two repairs I attacked hardest (the momentum-
filtered Cook majorant and the derived four-cluster factorization) both hold
under recomputation.  The objection count falls from 20 across three r1
verdicts to 14 here, with the residue concentrated not in the mathematics but
in the *shared* artifacts: a symbol table that trivialises the round's
headline result (1), a DAG row that outruns its theorem (2), and a checker
whose red coverage is narrower than it reports (3).  That is the right place
for a campaign to be failing at round 2, and all three are cheap to close.

Objection counts: **3 MAJOR (1, 2, 3), 6 MINOR (4--9), 5 NOTE (10--14).  0
FATAL.**

Final line: **FAIL(1,2,3)** — no FATAL; the three MAJORs are repairable
without touching a proof step, so one repair commit plus a working
mutation-(ii) red test closes the loop, and the four promotion decisions above
then apply as written.
