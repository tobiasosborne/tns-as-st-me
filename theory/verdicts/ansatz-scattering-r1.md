<!-- ROLE: round-1 critic verdict on theory/ansatz-scattering.md (codex T2
     shard, AC-EX).  Critic A (Fable), per briefs/t1-critics.md surfaces
     8-10.  Format: rk-light — severity + (a) location + (b) independent
     computation/counterexample + (c) fix demand + (d) surviving weaker
     statement.  Final line PASS/FAIL. -->

# Verdict: ansatz-scattering r1 (Critic A, Fable) — 2026-08-28

Target: `theory/ansatz-scattering.md` (AC-EX: ACE.1–ACE.3, D28-P merge
proposal).  Read in lockstep with `definitions.md` (D1, D5, D9, D10, D17,
D18), `claims/CLAIMS.md`, `theory/memory-quantization-general.md`, and the
full TeX of `refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`,
`refs/arxiv-1103.2286/dispersionrelation_final.tex`,
`refs/arxiv-1810.07006/p5_excitations.tex` (L3).

## 0. Port audit (brief surfaces 8–10) and verification record

**P1 (label audit).**  Every cited source label exists and its content
matches the shard's use: `(LRB)` (line 614), `(exchange-property)` (696),
`lem:FT` (721 — uses `U(x)Ω = Ω` for a translation-invariant ground state,
exactly as ⟨1⟩2.⟨2⟩1 says), `(SNAG)` (748), `(EM-transfer-relation)` (803
— verbatim `π(A)P(Δ) = P(\overline{Δ+Sp_Aτ})π(A)P(Δ)`),
`smearing-theorem` (874), `harmonic-theorem` (888), `norm-corollary`
(1045), `HR-auxiliary` (1120 — part (a) is `B_t^*(g_t)Ω = B^*(g)Ω` via the
mass-shell spectral integral, `(creation-on-vacuum)` at 1138),
`clustering-lemma` (1206 — uses `P({0})^⊥ = 1−|Ω⟩⟨Ω|` and vacuum
clustering), `Haag-Ruelle` (1291 — its proof's first paragraph commutes
the `Ω`-annihilating derivative to the right, as ⟨1⟩2.⟨2⟩2 says),
`Haag-Ruelle-Fock` (1338), `s-matrix` (1441), `single-particle-density`
(1490), `Lebesgue-absolute-continuity` (1505),
`single-particle-density-two` (1532), `cor:localization` (2482 — the
conditional-expectation localization), `almost-locality` (2545).
`refs/arxiv-1103.2286`: the Rayleigh–Ritz sentence ("this generalized
eigenvalue system can be recognized as the Rayleigh-Ritz equation")
appears directly after the two displayed quadratic forms, as ⟨1⟩1.⟨2⟩4
cites.  `refs/arxiv-1810.07006`: `(eq:kink)` at p5:1108 with the
phase-ambiguity remark immediately below ("multiplying `Ã_R` with an
arbitrary phase shifts `p ← p+φ`") ✓, `(eig)` at 1210, and the warning
after `(eq:quasi_inveff)` ("all the other solutions fall within the
continuous bands.  It is not expected that these states are approximated
well") ✓.  No citation-from-memory defects.

**P2 (re-derive vs analogize, per ported item).**
- `lem:FT` + `HR-auxiliary(a)` (vacuum invariance `U(t,n)Ω = Ω`; time
  independence of `B_t^*(g_t)Ω`): NOT ported — replaced by HYPOTHESES
  D28-P(1)–(3) (covariant sector representation, exact fiber equations).
  Honest substitution, correctly inventoried in ⟨1⟩2.⟨2⟩1.
- `Haag-Ruelle` Cook step (`Ω`-annihilating derivative): RE-DERIVED as
  **ACE-Cook** — the algebraic cancellation ⟨1⟩5.⟨2⟩2 is correct
  (`Haκ = aHκ + [H,a]κ`, exact kink equation kills the `E_K` part, exact
  magnon equation leaves `D_{c,b}(y)κ_a(x)`), but its quantitative closure
  fails under D28-P as stated — Objection 1.
- `clustering-lemma` / `Haag-Ruelle-Fock` (vacuum clustering + `BΩ = 0`
  factorization): NEITHER re-derived NOR a checkable hypothesis — replaced
  by the imprecise D28-P(6) — Objection 3.
- `cor:localization` / `almost-locality`: RE-DERIVED in sketch (**ACE-LR**,
  ⟨1⟩3.⟨2⟩1–⟨2⟩2), matching the source's conditional-expectation argument.
- `norm-corollary`: RE-DERIVED (**ACE-SP**, ⟨1⟩4) — I checked the
  non-stationary-phase computation: `N` integrations by parts with
  `(it(x/t−E'(p)))^{−1}∂_p` give `C_N⟨|x|+|t|⟩^{−N}` off the cone, and
  `Σ_{|x|>C|t|}⟨x⟩^{−N} = O(|t|^{1−N})` ✓ (the `‖f_t‖_1 = O(1+|t|)` used
  alongside is a safe overestimate of the true `O(|t|^{1/2})` — NOTE 7).
- `EM-transfer-relation`: cited verbatim and correctly applied
  (⟨1⟩6.⟨2⟩3): a creator with strictly positive energy transfer has
  vanishing vacuum one-point function ✓.
- `single-particle-density`, `Lebesgue-absolute-continuity`,
  `single-particle-density-two`, `s-matrix`: correctly NOT ported; no
  density or completeness claim survives anywhere ✓.
- SNAG/Arveson (campaign landmine "make the fibering precise"): the
  automorphism-level filter `τ_F(A)` is representation independent and the
  fibering is obtained by SNAG on the ASSUMED `U_{αβ}` — the fibering is
  bought by hypothesis D28-P(1), and the shard says so.  Legitimate.

**P3 (surface 10).**  Confirmed: no `k→0`, plane-wave, equal-velocity, or
packet-soft statement anywhere in the theorem, proof, checker, merge
rows, or HONEST STATUS; velocity separation `ε_v > 0` is standing in
D28-P(4) with the three sign clauses ✓.

**P4 (checker arithmetic).**  ACE-C1's gates recomputed: `W_K = 0.32`,
`Δ_M = 1`, packet energy sup `≈ 0.16(1−cos 0.15) + 1 + 0.6(1−cos 0.75)
= 0.0018 + 1.1608 < 1.163` ✓, velocity separation
`≥ 0.6 sin 0.65 − 0.16 sin 0.15 ≈ 0.363 − 0.024 = 0.339 > 0.33` ✓.  The
spec is implementable.  `--red-equal-velocity` would genuinely fail (no
cone separation ⇒ `C(t)` decays at most diffusively, the doubling
exponents cannot reach `< −2`).  `--red-absorption` fails only an
arithmetic gate on a hypothesis the proof never uses — see Objection 2.

## 1. Objections

**Objection 1 — MAJOR.  False regularity leaf: `C²(𝕋)` dispersions do not
have rapidly decreasing hopping kernels, and the Cook majorant does not
close under D28-P as stated.**
(a) ⟨1⟩3.⟨2⟩3 ("Since the band dispersion is smooth on the selected
support, its Fourier hopping kernel is rapidly decreasing"), consumed by
⟨1⟩5.⟨2⟩3–⟨2⟩5; hypothesis source D28-P(2) ("`E_K ∈ C²(𝕋)`") and D28-P(3)
(band `ω_γ`, global `C²` retained; local `C^∞` only near packet supports).
(b) My computation.  The kernel `h_{γ,bb'}` is FORCED to be the Fourier
kernel of the true band on ALL of `𝕋`: `D_{γ,b}(n)Ω_γ = 0` requires
`Σ_m h(m−n)a(m)Ω_γ = [H,a(n)]Ω_γ = Γ_{M,γ}(ω\,δ̂_n)`, and D28-P(3)'s
normalisation `a(n)Ω_γ = Γ_{M,γ}δ_{n,b}` is a position delta — spread over
the WHOLE band — so `ĥ = ω̂` globally.  Local smoothness of `ω` near the
packet support contributes nothing to the global Fourier decay: `C²(𝕋)`
gives only `ĥ(m) = o(m^{−2})` (Riemann–Lebesgue on `ω''`), and "rapidly
decreasing" (`O(m^{−N})` for all `N`) is FALSE.  Consequences downstream:
(i) `D_{γ,b}(n)` is quasi-local with `o(m^{−2})` tails, not almost local,
so ACE-tail's truncation at radius `|x−y|/3` leaves `o(⟨x−y⟩^{−2})`, not
`⟨x−y⟩^{−N}`; (ii) in ⟨1⟩5.⟨2⟩4, the long-hop part of "commuting the
hopping kernels through `θ_c`" is bounded by
`Σ_{|m| ≳ ε_v|t|}|ĥ(m)| = o(|t|^{−1})` times an `O(1)` packet norm —
because for `|m| ≳ ε_v|t|` the `θ`-straddling region contains the whole
outgoing cone, so no packet smallness is available — and `o(1/t)` is NOT
Cook-integrable; `∫dt Σ_{|m|>ε_vt}|ĥ(m)| < ∞` is equivalent to
`Σ_m|m||ĥ(m)| < ∞`, which `C²(𝕋)` does not supply.  (iii) The same defect
infects the KINK side: `Hκ_a(x)` carries the global Fourier kernel of
`E_K ∈ C²(𝕋)`, and ⟨1⟩3.⟨2⟩3 does not even address its decay although
⟨1⟩5.⟨2⟩4 uses "the hopping kernels" (plural).  So ⟨1⟩5.⟨2⟩5's "Taking
`N ≥ 5` gives an integrable majorant" is unsupported: no `N > 3` power is
available from the stated hypotheses.
Two sufficient repairs, both inside the shard's own lane: (R1) strengthen
D28-P(2)–(3) to `E_K, ω_γ ∈ C^∞(𝕋)` — physically costless, since an
isolated band of the assumed exact spectral problem is typically
real-analytic; or (R2) keep `C²` but replace D28-P(3)'s position-delta
normalisation by a momentum-filtered frame `a(n)Ω_γ = Γ_{M,γ}(ê_n)`,
`ê_n(k) = e^{−ikn}χ(k)` with `χ ∈ C_c^∞` `≡ 1` on the packet support
inside the local-`C^∞` neighbourhood; then `h := ω·χ̃` (`χ̃ ∈ C_c^∞`,
`χ̃ ≡ 1` on `supp χ`, supported where `ω ∈ C^∞`) is rapidly decreasing AND
`D(n)Ω_γ = Γ_{M,γ}((ω−h)χ ê_n) = 0` still holds exactly.  Either repair
restores every downstream step verbatim.
(c) FIX: adopt (R1) or (R2) in D28, and rewrite ⟨1⟩3.⟨2⟩3 to derive kernel
decay from the corrected hypothesis, covering the kink kernel explicitly.
(d) Surviving: AC-EX verbatim under `C^∞(𝕋)` band dispersions.

**Objection 2 — MAJOR.  The D28-P(5) inelastic/absorption threshold
inequalities are never used in the proof, yet are advertised as
load-bearing (brief surface 9: they are NOT used where claimed).**
(a) D28-P(5); theorem preamble ("PROVE ... on the fixed packet domains of
D28-P"); §4 CHECKER SPEC ("both load-bearing threshold inequalities");
proposed claims row ("explicit inelastic-threshold hypotheses" listed
among the operative assumptions).
(b) My leaf-by-leaf audit of every justification in ⟨1⟩3–⟨1⟩7:
⟨1⟩3 uses P(1),(3),(4),(6), D10(a); ⟨1⟩4 uses P(4); ⟨1⟩5 uses
P(2),(3),(4),(6), D1(c,e′); ⟨1⟩6 uses P(2),(3),(6) and
`(EM-transfer-relation)`; ⟨1⟩7 uses the charge clause, B3, and ⟨1⟩6.
`d_abs`, `Δ_M > W_K`, `Θ_inel`, `η_inel` occur in NO justification line.
This is structural, not cosmetic: because P(2)–(3) assume the bands EXACT
and P(6) assumes tail factorization, Cook existence and isometry hold
regardless of any competing spectrum — an open absorption channel cannot
damage a limit whose defect is already `Ω_γ`-annihilated and cone-
separated.  The thresholds' true role is to make the EXACTNESS hypothesis
physically plausible (excluding the wall–magnon/absorption scenarios that
would destroy an exact isolated band), i.e. they belong to the
justification of D28, not to the proof of AC-EX.  As placed, they inflate
the hypothesis package recorded in the DAG row, and the checker's
`--red-absorption` mutation certifies a gate with no inferential
connection to the theorem — a red test that cannot catch any error in the
proof.
(c) FIX: move P(5) to a clearly-labelled plausibility remark on D28-P(2)–
(3) (or exhibit the proof step that consumes it); align the claims row and
the checker prose ("motivational gate", not "load-bearing").
(d) Surviving: AC-EX with P(5) deleted — the identical proof.

**Objection 3 — MAJOR.  D28-P(6), the sole replacement for the source's
vacuum-clustering apparatus, is not a mathematical statement.**
(a) D28-P(6); consumed at ⟨1⟩5.⟨2⟩3 (**ACE-tail**), ⟨1⟩6.⟨2⟩1
(**ACE-Gram**), ⟨1⟩6.⟨2⟩3.
(b) The clause ("mixed matrix elements with observables separated onto
either tail factor through the corresponding vacuum transfer projection
with the D1(c) `λ̃` bound") has no quantifiers, no constants, no stated
observable class, and no definition of the separation.  What the proof
actually needs, reconstructed from its uses: (i) two-cluster form — for
local `O` supported at distance `r` from the kink cores on the `γ` tail,
`|⟨κ_a(x), O κ_{a'}(x')⟩ − ω_γ(O)⟨κ_a(x), κ_{a'}(x')⟩| ≤ C‖O‖λ̃^r`,
uniformly over the finite frame and over `x, x'` (ACE-tail applies this
with `O = (D†D)_{trunc}` and `ω_γ(D†D) = 0`); (ii) a MULTI-cluster form
for ACE-Gram — the same-channel scalar product has FOUR clusters (two
kink cores, two magnon dressings), and ⟨1⟩6.⟨2⟩1's "product of the exact
kink and magnon Gram forms" needs the iterated factorization with
controlled cross terms, which the two-cluster sentence does not state;
(iii) uniformity in the time-dependent positions, since the bound is
integrated over `t`.  The source replaces exactly this with Lemma
`clustering-lemma`'s proven `O(⟨x_i−x_j⟩^{−∞})` decay from the unique
gapped vacuum — the one ingredient the campaign flagged as "the adaptation
IS the theorem" — and the shard's substitute is currently a gesture, not a
hypothesis one could verify on D16's XXZ kink (where I checked the package
is at least satisfiable: the `|K(z)⟩` family gives an exact flat kink band
and the one-magnon states over either product vacuum are exact and
finite-core, so precision is achievable, not vacuous).
(c) FIX: display D28-P(6) as the two inequalities (i)-(ii) with explicit
quantifiers and the frame/position uniformity (iii).
(d) Surviving: AC-EX conditional on the displayed inequalities; nothing
else changes.

**Objection 4 — MAJOR.  ACE.3's identification of the T1 outcome measure
with the Born weights is asserted, not proved.**
(a) ⟨1⟩7.⟨2⟩2 and its justification line ("The assumed T1 ordered-limit
measure, D14, D17, the theorem's definite channel charges, and
⟨1⟩6.⟨2⟩3–⟨2⟩5").
(b) None of the cited items computes the ordered-limit TPM/window-charge
law on `ran W_+`.  Missing lemma, reconstructed: for
`Ψ = W_+(F_L, F_T)`, the fixed-window restriction of `e^{−itH}Ψ`
converges per channel to a definite kink-charge state (so the initial and
final window-charge measurements are asymptotically channel-diagonal:
`‖E({q_ch})Ψ_t − P_{ch}Ψ_t‖ → 0`), and inter-channel cross terms vanish
(`|⟨R|E({q_R})|T⟩| ≤ ⟨T|E({q_R})|T⟩^{1/2} → 0`, Cauchy–Schwarz).  This is
precisely the AD3 clause of D18 — which D28-P deliberately does NOT
contain — restricted to the constructed channels.  It is plausibly
derivable from the shard's own estimates (⟨1⟩4's cone decay plus
almost-locality of the creators pushes the magnon dressing out of any
fixed `W` at rate `O(|t|^{−N})`), but no step in the shard derives it.
As written, ACE.1–ACE.2 are proved (modulo Objections 1, 3) while ACE.3
is a claim.  The charge arithmetic itself checks: `ν = q_L−q_in = 0`,
`ν = q_T−q_in = 2`, `2sδx_ex + 2p_2^{ex} = 0` matches B3 and Lane T1's
`δx = −(1/2s)Σννp_ν` on support `{0,2}` exactly ✓.
(c) FIX: prove the local-decay lemma from ⟨1⟩3–⟨1⟩4 (one Lamport step), or
add "AD3-for-constructed-channels" to the ACE.3 ASSUME line explicitly and
say in HONEST STATUS that ACE.3 is conditional on it.
(d) Surviving: ACE.1–ACE.2 in full; ACE.3 as a conditional bridge given
AD3-type local decay on the constructed channels.

**Objection 5 — MINOR.  `θ_c` is undefined beyond its two asymptotic
values.**
(a) ⟨1⟩5.⟨2⟩1, ⟨2⟩4.
(b) If `θ_c` is a sharp step, "commuting the hopping kernels through
`θ_c`" produces straddling terms whose only smallness is the kernel decay
(Objection 1's weakest link); the near-region bookkeeping in ⟨2⟩4 tacitly
uses a transition profile whose difference kernel is summable.  A smooth
monotone `θ_c` of fixed transition width makes the near-step terms live on
`|y−x| = O(1)` with Schwartz-tailed leakage, which is what ⟨2⟩4 asserts.
(c) FIX: define `θ_c ∈ C^∞(ℤ)`, monotone, with a fixed-width transition,
in ⟨1⟩5.⟨2⟩1.
(d) Surviving: the same estimate with `θ_c` specified.

**Objection 6 — MINOR.  Vacuum-vector/state conflation in ⟨1⟩5.⟨2⟩3.**
(a) "The leading transfer projection is `‖D_{γ,b}(y)Ω_γ‖² = 0`".
(b) There is no `Ω_γ` in `H_{αβ}`; the quantity that enters the two-sided
contraction is the STATE evaluation `ω_γ((D†D)_{trunc})`, which vanishes
up to truncation error because `ω_γ(D†D) = ‖π_γ(D)Ω_γ‖²_{H_γ} = 0`.  The
intended argument is clear; the wording plants exactly the cross-sector
confusion the campaign warned about.
(c) FIX: replace the display by `ω_γ(D†D) = 0` with the truncation error
split out.
(d) Surviving: unchanged content.

**Objection 7 — NOTE.**  ⟨1⟩4.⟨2⟩2's `‖f_t‖_1 = O(1+|t|)` overestimates
the true `O(|t|^{1/2})`; harmless (upper bound used upward), but the
constant chase in ⟨1⟩5.⟨2⟩4's `|t|²` prefactor inherits it — worth
tightening if the `N ≥ 5` margin is ever load-bearing.

**Objection 8 — NOTE (lockstep).**  The proposed claims row lists
`M-quant-G` among depends-on; AC-EX's proof uses only B3 and the T1
target's ledger formula in ⟨1⟩7, not M-quant-G's conclusion.  Either cite
B3 + the T1 row (once merged) or justify the M-quant-G edge; spurious
DAG edges misprice the dependency graph.

## 2. Summary

The architecture is right and honestly fenced: the vacuum-invariance
inventory (⟨1⟩2) is accurate against the source TeX line by line, the
Fock/completeness machinery is correctly NOT ported, no soft statement
survives anywhere, and the ACE-Cook cancellation and ACE-SP propagation
estimates are correct as algebra.  But the quantitative closure fails
under D28-P as stated (Objection 1 — a false regularity leaf with a
one-line repair), the advertised threshold inequalities are decorative
(Objection 2), the single clustering-substitute hypothesis is not yet a
statement (Objection 3), and the T1 bridge clause is asserted rather than
proved (Objection 4).  All four are repairable within the shard's own
lane without touching the shared files.

Final line: **FAIL(1,2,3,4)** (4 MAJOR, 2 MINOR, 2 NOTE; no FATAL — the
theorem survives with `C^∞` bands, a pruned P(5), a displayed P(6), and
either a proved or an explicitly hypothesised local-decay lemma for
ACE.3).
