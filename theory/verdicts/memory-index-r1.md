<!-- ROLE: round-1 critic verdict on theory/memory-index.md (codex T1 shard,
     M-INDEX).  Critic A (Fable), cross-family per briefs/t1-critics.md.
     Format: rk-light — severity + (a) location + (b) independent
     computation/counterexample + (c) fix demand + (d) surviving weaker
     statement.  Final line PASS/FAIL. -->

# Verdict: memory-index r1 (Critic A, Fable) — 2026-08-28

Target: `theory/memory-index.md` (M-INDEX-spec, L-A-fin, L-A-arith,
L-A-obstruction, L-B, L-C, L-D, (G-IDX.2), (G-IDX.3), D26/D27 merge
proposals).  Read in lockstep with `definitions.md` (D1, D9, D13(a), D17,
D18), `claims/CLAIMS.md` (M-flux, M-quant-G, B3), and
`theory/memory-quantization-general.md`.  Every refs/ citation opened and
checked against the TeX (L3).

## 0. What I independently recomputed (verification record)

The following all CHECK.  They are recorded so round 2 does not re-litigate
them.

**V1 (L-A-fin offset arithmetic, ⟨1⟩1).**  From D13(a),
`2s(𝔛_W−c) = Σ_{x∈W}S^z_x + s(a+b−1−2c)`: expanding
`2s(a−1−c) + Σ(S^z+s) = ΣS^z + s(2a−2−2c+b−a+1)` ✓, and this equals the
(G.3) left side `ΣS^z − s(c−a+1) + s(b−c)` ✓.  With D26 (`spec S^z ⊂ κ+ℤ`),
commuting on-site addition gives `spec Q̂_{W,c_0} ⊂ |W|κ + s(a+b−1−2c_0) + ℤ`
✓.  Spectrum invariant under `α_t` ✓.

**V2 (offset bookkeeping through the double limit, brief surface 3).**
(i) `s = 1/2`, the shard's own spin-3/2 site (`κ = 1/2`), `W = [−1,2]`,
`c_0 = 0`: `ρ = 4·(1/2) + (1/2)(−1+2−1) = 2 ≡ 0`; any two-time TPM
increment `ν = q_− − q_+ ∈ ℤ` ✓.
(ii) `s = 0.37`, `spec S^z = {−1,0,1}` (`κ = 0`), `W = [−2,4]`, `c_0 = 0`:
`ρ = 0.37·(−2+4−1) = 0.37`; the two spectral values sit in `0.37+ℤ` and
their difference is in `ℤ` — the irrational offset never reaches `ν` ✓.
(iii) Drifting-window probe `W_m = [−m,2m]`: `ρ_m = 0.37(m−1) mod ℤ` drifts
with `m`, but `ν` is formed at fixed `W_m` BEFORE `m→∞` (⟨1⟩5.⟨2⟩3), so the
drift never enters and the weak limit stays on the closed set `ℤ` ✓.  The
weak-limit-smearing landmine is genuinely closed by the order of
operations, not by tightness alone.  Nothing anywhere assumes `s ∈ ½ℤ` ✓.

**V3 (two-time landmine, brief surface 1).**  The shard nowhere uses
"difference of lattice-valued observables is lattice-valued".  Sanity
`2×2` check that the naive route indeed fails: `Q = diag(0,1)`,
`Q(t) = UQU^†` with a rotation `U` by `φ`; `spec(Q(0)−Q(t)) = {±|\sin φ|}`,
not integers.  The TPM law never forms this difference; integrality enters
only through the two same-window spectral resolutions (⟨1⟩5.⟨2⟩3).  The
checker mutation IDX-C2 (naive `⟨Q̂(t_-)⟩−⟨Q̂(t_+)⟩`) would genuinely fail:
the discrepancy is exactly the dephasing defect, generically nonzero for
Haar `U`.

**V4 (IDX.4, ⟨1⟩6).**  Substituting `ν = q−q'` in
`Σ_{ν,q}ν‖E_+({q−ν})E_-({q})Ψ‖²` gives
`Σ_q q‖E_-({q})Ψ‖² − Σ_q⟨E_-({q})Ψ, Q̂(t_+)E_-({q})Ψ⟩
 = ⟨Q̂(t_-)⟩ − ⟨𝒟_{W,t_-}(Q̂(t_+))⟩` ✓.  Normalisation ⟨1⟩5.⟨2⟩2 ✓ (two
resolutions of identity).  The `ν`-support is finite at fixed `W` (finite
window algebra), so all sum/limit exchanges in ⟨1⟩7.⟨2⟩1 are legitimate ✓.

**V5 (the L-A counterexample, ⟨1⟩3 — recomputed in full).**
Per-site mean: `(1−ε²)(1/2) + (ε²/2)(−1/2+3/2) = 1/2` exactly ✓, so both
D17 sums (including `|x|`-weighted) vanish identically ✓; D9(a) factorised
limits hold for the product state ✓; `e^{2πiS^z} = −𝟙` on the 4-dim site ✓
(D26 with `c = −1`); `H = 0` satisfies H-MQG(3) ✓; the covariant family
`{⊗|1/2⟩, ⊗|−1/2⟩}` under `U(1)⋊ℤ₂` satisfies D1/D2(a) with `χ = 1` ✓.
Window charge on `W_N = [−N,N]`, `c_0 = −1`: scalar
`= (1/2)(−N+N−1+2) = 1/2`; right tail contributes `−(N+1)/2`
deterministically; total `= L_N` ✓.  Characteristic function
`φ_N(t) = Π(1−ε_n²(1−\cos t))` ✓; `u = ε_n²(1−\cos t) ∈ [0,1]` for all
`n ≥ 1` so `|1−u| ≤ e^{−u}` ✓; `1−\cos t ≥ 2t²/π²` on `[−π,π]` ✓; hence
`|φ_N| ≤ e^{−2V_Nt²/π²}` with `V_N = Σ_1^N (n+1)^{−1} → ∞` ✓; Fourier
inversion gives `sup_k P(L_N=k) ≤ √(π/(8V_N))` ✓; the split
`(2K+1)CV_N^{−1/2} + 1/K` kills the resolvent matrix element ✓; strong
resolvent convergence to any self-adjoint `Q̂` would keep
`Im⟨Ω,(Q̂−i)^{−1}Ω⟩ = ∫(λ²+1)^{−1}dμ > 0` — contradiction ✓.
**The refutation of M-INDEX-LA-strong is correct.**  I additionally
verified robustness: no rescue via the implementer route either — the
rotated state `ϱ∘Ad(Π e^{iθS^z_x})` has product fidelity
`Π_n(1−ε_n²(1−\cos θ)) → 0`, so the `U(1)` orbit leaves the folium and no
strongly continuous implementing group (hence no Stone generator) exists
in this GNS representation.

**V6 ((G-IDX.3) reduction against M-quant-G, brief surface 6 — line by
line).**  Charge changes: reflection `q_L−q_in = 0`, transmission
`q_T−q_in = 2` ✓ (M-quant-G ⟨1⟩4); `ν` = minus core change ⇒ values
`{0, 2}` ✓; mean `Σνp = 2⟨N_T⟩`, so
`δx = −(1/2s)·2⟨N_T⟩ = −⟨N_T⟩/s` = (G.1) ✓; Bernoulli on `{0,2}` gives
`Var_p(ν) = 4⟨N_T⟩(1−⟨N_T⟩)`, and `(2s)^{−2}Var_p(ν) =
s^{−2}⟨N_T⟩(1−⟨N_T⟩)` = (G.2) ✓.  D13(a) calibration (one lattice
translation = charge `2s`) is used identically in both shards ✓.  No
constant, convention, or quantifier mismatch found.  D7/D8 do not enter.

**V7 (L3 citation audit).**  `refs/arxiv-1810.07351/Index_Re.tex`:
`(A:IntegerCharge)` is exactly on-site `Spec(Q_x) ⊂ ℤ` (line 372);
`(eq: choice t)` is the integrality constraint on `Q+T_-` (line 415);
Assumptions (iii)–(v) are approximate eigenvector, local charge
fluctuations, clustering — exactly as ⟨1⟩3a characterises them; `(Defchi)`
(line 1132) and `(lem:the phase understood)` (line 1143) sit in
`\section{Proof of Theorem \ref{thm:main}}` ✓.  ⟨1⟩3a's claim that BBDF
does not construct a regularised total charge in a D9 sector is accurate:
their `T_±` live on finite `Λ` with `‖T_±‖ ≤ C|Λ|` and everything is
anchored on the clustering assumptions the counterexample lacks.  No
citation-from-memory defects found in this shard.

**V8 ((LR)/D27 audit, brief surface 4).**  D27 is NOT secretly channel
structure or completeness: it names no channels, no wave operators, no
inventory, and the H-AD-G corollary is quarantined in ⟨1⟩8.  Nor is it too
weak: given LR1–LR3, I verified that ⟨1⟩7 closes — LR1 gives the two
window expectations of `Q̂_{W,c_0} ∈ 𝔄_W`, LR2 converts the TPM mean to
their difference via V4, LR3 passes support and first moment through
`W↑ℤ`.  The weakest (LR) under which the shard's own proof survives is:
LR1 + LR2 + (tightness-with-first-moments only, subsequential form) — see
objections 1–2.

## 1. Objections

**Objection 1 — MINOR.  D27 carries two dead clauses; it is not the
weakest (LR), which the campaign target prices at "half the theorem's
value".**
(a) §6.1, D27(LR3) final sentence (the interaction-range-collar TV
clause) and D27(LR4) (existence of the ordered `δx`).
(b) My audit of every justification leaf in ⟨1⟩4–⟨1⟩8: the collar/TV
clause is cited nowhere.  And LR4's existence clause is a THEOREM given
LR1–LR3: from ⟨1⟩7.⟨2⟩2, `Σ_ν ν p_{W_m}(ν) = −2s[ω^+_{W_m}(𝔛_{W_m}) −
ω^-_{W_m}(𝔛_{W_m})]` at every fixed `m`, and LR3 makes the left side
converge, hence the right side converges — LR4's limit exists
automatically and equals `−(1/2s)Σνp(ν)`.
(c) FIX: delete the collar clause or exhibit the step that needs it;
demote LR4 from hypothesis to definition-of-`δx` plus a one-line corollary.
(d) Surviving: M-INDEX-spec exactly as proved, under the pruned D27.

**Objection 2 — MINOR.  LR3 assumes weak convergence of `p_{W_m}`
outright; the campaign's (LR) granted only tightness.**
(a) §6.1 D27(LR3), first sentence; campaign brief Lane T1 (LR) clause.
(b) With tightness + first-moment uniform integrability only, my
computation: Prokhorov on the closed set `ℤ` gives, along any
subsequence, a further subsequence with `p_{W_{m_j}} ⇒ p'`, `p'` a
probability on `ℤ` with converging first moments; support quantization is
therefore subsequence-free, and only the uniqueness of the VALUE `δx`
needs the extra convergence assumption.  The shard buys uniqueness by
assumption and does not say so.
(c) FIX: state the tightness-only subsequential variant alongside LR3, or
mark LR3's convergence clause as a convenience normalisation.
(d) Surviving: M-INDEX-spec as stated (with LR3), plus the strictly weaker
subsequential theorem (with tightness only).

**Objection 3 — MINOR.  The refutation ⟨1⟩3 is sound but the honest
surviving statement — L-A on the A2 folium — is neither stated nor
conjectured, although the campaign's route hint ("A2 covariance + INT +
D17") points exactly there.**
(a) ⟨1⟩3, ⟨1⟩3a, HONEST STATUS 2, and merge row M-INDEX-LA-strong.
(b) My computation: the counterexample state is disjoint from every
A2/D1(e′) MPS-kink folium.  Two independent markers: (i) its window-charge
variance `V_N ≍ log N` diverges, whereas for any state normal to the GNS
representation of a two-sided injective-MPS decoration the window-charge
variance is `O(1)` — by (IT), the `θ`-twisted transfer matrix `E_θ` is
similar to `e^{iθ_α(θ)}E`, so the extensive part of
`log ω(e^{iθQ̂_W})` is purely imaginary (mean only) and the second cumulant
is boundary-law; (ii) the `U(1)` rotation moves the counterexample state
to a disjoint state (V5), while on the A2 folium the same rotation is
locally implemented.  So the refutation operates entirely outside the
folium where the campaign's route would run, and a folium-restricted L-A
(self-adjoint `Q̂` with `e^{2πiQ̂}` scalar in the GNS representation of a
FIXED A2 kink state) is untouched and plausibly true.
(c) FIX: add to §6.2 a CONJECTURE row `M-INDEX-LA-folium` recording this
surviving candidate (statement + the two markers above as the route), so
the REFUTED row does not silently over-advertise its reach (L10).
(d) Surviving: the refutation of the sector-wide claim stands verbatim.

**Objection 4 — MINOR.  ⟨1⟩8.⟨2⟩2's channel identification uses an
unstated reading of D18(AD3) plus an unproven (but two-line) cross-term
lemma.**
(a) ⟨1⟩8.⟨2⟩2, justification paragraph.
(b) My reconstruction of what the leaf actually needs: (i) the incoming
window-charge law tends to a point mass — this follows from AD3 read as
weak-* convergence of the window restriction to a charge eigenstate,
because `E_{W,t_-}({q_*}) ∈ 𝔄_W` and
`‖E({q_*})Ψ_t − Ψ_t‖² = 1 − ⟨E({q_*})⟩ → 0`; (ii) inter-channel cross
terms vanish: for the outgoing `r|R⟩+t|T⟩`,
`|⟨R|E({q_R})|T⟩| ≤ ‖E({q_R})|T⟩‖ = ⟨T|E({q_R})|T⟩^{1/2} → 0` since the
`T`-leg's window law concentrates on `q_T ≠ q_R` (Cauchy–Schwarz).
Neither step is displayed; D18 fixes no topology for AD3's "the remaining
local state is a kink charge eigenstate", so the leaf currently cites a
hypothesis at a strength the hypothesis file does not pin down.  Note this
gap is NOT present in M-quant-G itself (its ⟨1⟩5 works directly with the
channel projections and never forms a TPM), so it is new debt of this
shard, not inherited.
(c) FIX: display the two-step lemma inside ⟨1⟩8 with the AD3 reading named
(weak-* window convergence per channel), or add that reading to the
H-AD-G recital in the M-INDEX-spec row.
(d) Surviving: (G-IDX.3) under the explicitly strengthened reading of AD3
— certainly the intended one, and the one M-quant-G's own uses need.

**Objection 5 — NOTE.  `δx` overload (L4).**  D27(LR4) reuses D13(a)'s
symbol `δx` for the ordered asymptotic limit; D13(a)'s `δx` is a
finite-time two-state difference.  The §6.3 notation rows do not flag the
overload.  FIX: one notation row ("`δx` in D27(LR4) is the ordered
asymptotic value of D13(a)'s observable; finite-time `δx` unchanged").

**Objection 6 — NOTE.  ⟨1⟩4.⟨2⟩2 (L6b leaf discipline).**  "…(IDX.3)
becomes the asymptotic ledger" is a prose leaf with no displayed
statement; the content is subsumed by ⟨1⟩7, so either display the averaged
identity or point ⟨1⟩4's asymptotic clause at ⟨1⟩7.

## 2. Checker spec assessment (not implemented, per brief)

IDX-C1–C5 are all implementable as specified.  Mutations: IDX-C2 fails
genuinely (V3 — the dephasing defect is generically nonzero under Haar
conjugation, so the naive difference misses (IDX.4) at `>10^{−6}`);
IDX-C3's `ε_n → (n+1)^{−1}` makes `V_N` convergent and fails the
registered growth test ✓; IDX-C4's `p_m = (1−1/m)δ_0 + (1/m)δ_m` is tight
with first moment `≡ 1 ↛ 0`, correctly killing "tightness alone" ✓;
IDX-C5's `2→1` mutation breaks both target expressions ✓.  The checker
suite genuinely certifies the load-bearing steps ⟨1⟩5–⟨1⟩7.

## 3. Summary

The shard's retreat is honest and its two central results are correct as
stated: the refutation of the strong L-A is verified end to end (V5), and
the conditional TPM quantization theorem closes both campaign landmines by
construction rather than by evasion (V2–V4).  The (G-IDX.3) reduction
matches M-quant-G exactly (V6).  All refs/ citations are lockstep-accurate
(V7).  The residue is minimality and completeness of the retreat: two dead
D27 clauses, an over-strong convergence assumption, one missing (easy)
lemma in the H-AD-G corollary, and the unstated folium-restricted
surviving conjecture.

Final line: **PASS** (0 FATAL, 0 MAJOR; MINOR 1–4, NOTE 5–6 to be swept in
the merge round).
