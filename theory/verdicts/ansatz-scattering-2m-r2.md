# Critic verdict r2 — `theory/ansatz-scattering-2m.md` (Theorem AC-EX-2M, Lane S2)

Critic: Opus, adversarial, 2026-08-28.  Work order: `briefs/s2-critic-r2.md`
(incorporating `briefs/soft-critic-r1.md`, S2 specialization).  Writable lane:
this file only.  All prototype computation in
`/tmp/.../scratchpad/a2m_c1_r2.py`; no shared file touched.  Repair round
audited: commit `d5c8a10` (diff `7b6f5f9..d5c8a10`, 258 lines) against
`theory/verdicts/ansatz-scattering-2m-r1.md` and
`theory/ansatz-scattering-2m-r1-response.md`.

---

## 0. Repair verification table (obligation 1)

| r1 id | Disposition claimed | r2 verdict | Where checked / residue |
|---|---|---|---|
| O1 (fence params) | ACCEPTED | **VERIFIED-FIXED** | ⟨1⟩2.⟨2⟩1 now names `s_N(F)`; `‖∂^jf_ε‖_∞=ε^{-j-1/2}‖f^{(j)}‖_∞` recomputed **correct**; r1's fixed-`k_0` narrowing counterexample is now covered.  New residue → **R2-O3** |
| O2 (clause 5 = LSZ) | ACCEPTED | **PARTIALLY-FIXED** | (5a)/(5b) split present, D6 anchor present, ⟨1⟩9.⟨2⟩1 is now `W_±`-free ✓.  But (5b) is a *vector* statement and ⟨1⟩9.⟨2⟩2 uses it as an *operator* statement → **R2-O1 (MAJOR)** |
| O3 ((SR) quantifiers) | ACCEPTED | **VERIFIED-FIXED** | `j=(W_j,σ_j)` explicit; `(SR)` posed after `N,t` only; `A_j(0)` required; display uses `lim_ℓ`; concession sentence present.  Arzelà–Ascoli now has a genuine family (verified below).  Residues → **R2-O3, R2-O4** |
| O4 (D6 (SR) instance) | ACCEPTED | **VERIFIED-FIXED** (via r1's option (ii)) | ⟨1⟩9.⟨2⟩4 downgraded to the exhaustion-free single function; `(W,σ)`-uniform version declared open on every model incl. D6; ⟨2⟩5 no longer contradicts ⟨2⟩4.  Residue → **R2-O9** |
| O5 ("entire summand") | ACCEPTED | **VERIFIED-FIXED** | `grep` confirms "entire"/"compatible union" gone; ⟨1⟩7.⟨2⟩4 is fixed-pair only; row adds "range exhaustion" to the disclaimer.  Residues → **R2-O6(i), R2-O10** |
| O6 (checker scope) | ACCEPTED | **VERIFIED-FIXED** | Rescoped; C1b support-length gate + its own red added; Jordan-safe declared uncertified; `raise`/`sys.exit`/`-O` mandated.  Implemented and mutation-tested (§4).  Residues → **R2-O7, R2-O8** |
| O7 (Gram exponents) | ACCEPTED | **VERIFIED-FIXED** | `O(|t|^{4-N})`, `O(|t|⁴⟨ε_v|t|/2⟩^{-N})` — I re-counted the four-fold sum independently: **correct** |
| O8 (`V_w` isometry) | ACCEPTED | **VERIFIED-FIXED** | Recomputed in full (§2 V1): `V_w^†V_w=1` from `l=𝟙`, both contractions have constant **one**, `‖·‖_{1→1}` clause present.  D31-C2 derivation **undamaged and strengthened** |
| O9 (D17 residue) | ACCEPTED | **VERIFIED-FIXED** | `grep D17` → no hits |
| O10 (D2(a) phantom) | ACCEPTED | **VERIFIED-FIXED** | Removed from D31 opening and from the depends-on cell.  But two *used* definitions are still absent → **R2-O6(ii)** |
| O11 (row lockstep) | ACCEPTED | **VERIFIED-FIXED** | Row: "derives D31-C2, and with D31(3)'s uniform almost-locality also D31-C4"; "D31-listed" restored |
| O12 (Cook domain) | ACCEPTED | **VERIFIED-FIXED** | ⟨1⟩5.⟨2⟩1 now cites D31(3) compact E–p transfer for `Dom H`; (2M-Cook) re-derived independently, **correct** |
| O13 (`|S|=1`) | ACCEPTED | **VERIFIED-FIXED** | Clause present; verified against ML2 (18): `S=(c−e^{-iq})/(e^{iq}−c)=−\overline{(e^{iq}−c)}/(e^{iq}−c)`, `c=cos(K/2)∈[0,1]` real, `e^{iq}≠c` on `0<q<π` ⟹ `|S|=1` |
| O14 ("ε never enters") | ACCEPTED | **VERIFIED-FIXED** | Replaced in both ⟨1⟩1(A2M.1) and ⟨1⟩9.⟨2⟩3 by the true statement |
| O15 (covariance) | ACCEPTED | **VERIFIED-FIXED** | D31(3) displays `a_{i,b}(n)=τ_n(a_{i,b}(0))` |
| N1 (charge-sector isolation) | ACCEPTED | **VERIFIED-FIXED** | D31(2) + ⟨1⟩10.⟨2⟩1 both carry "within the charge-one sector" |
| N2 (`d_B` survives soft limit) | ACCEPTED | **VERIFIED-FIXED** | ⟨1⟩2.⟨2⟩3; I recomputed `d_B→J sin²(k_h/2)` independently — **correct**.  Residue → **R2-O3** |
| N3 (forward reference) | ACCEPTED | **VERIFIED-FIXED** | Marked non-circular; stated reason is under-inclusive → **R2-N3** |
| N4 (matrix vs scalar band) | ACCEPTED | **VERIFIED-FIXED** | D31(2) scalar `ω` ⊗ fixed multiplicity; `V_i=ω'(K_i)` now defined.  Residue → **R2-N4** |
| N5 (HONEST STATUS phrasing) | ACCEPTED | **VERIFIED-FIXED** | "Separation … is derived from `d_B>0`, not assumed" |
| N6 (port audit) | ACCEPTED | **VERIFIED-FIXED** | Ports unchanged; the two edited ported/adapted steps re-verified.  The explicit refusal to port creator-independence is *correct for* ⟨1⟩7.⟨2⟩4 but is exactly what ⟨1⟩9.⟨2⟩2 needs → **R2-O1** |
| N7 (frozen checker) | ACCEPTED | **VERIFIED-FIXED** | `theory/checks/` untouched; `soft_index_probe.py --selftest` re-run: **`selftest PASS`, exit 0** |
| N8 (REFUTED audit) | ACCEPTED | **VERIFIED-FIXED** | Re-audited: no ML5, no withdrawn `S2`, no M-INDEX-LA-strong, no ML1/ML3/ML6 reliance; nothing contradicts D24(e) or the G0-soft-r1 kinematic-factor fence |

**Nothing REGRESSED in the mathematics.**  One text regression (interface
clause 3, §R2-O2(ii)) and two checker-text regressions (§R2-O7) were
introduced by the repair's compression.

---

## 1. What was independently recomputed (obligation: recompute, never referee)

| # | Step | Method | Outcome |
|---|---|---|---|
| V1 | ⟨1⟩3.⟨2⟩2 (the O8 replacement) | `V_wx=Σ_s|s⟩⊗A^{s_1}⋯A^{s_w}x`; `V_w^†V_w=Σ_s(A^{s_1}⋯A^{s_w})^†(⋯)=𝟙` by `E^*(𝟙)=𝟙`; `Ψ_D(r)=tr_{d^w}[(D⊗𝟙)V_wrV_w^†]=E_D(r)`; `‖Ψ_D(r)‖_1≤‖D‖‖r‖_1=‖D‖`; `|tr Ψ_C(Z)|≤‖C‖‖Z‖_1` | **CORRECT**, both constants exactly **one**, uniform in `w`.  Strictly better than the r1 text.  D31-C2 **preserved** |
| V2 | ⟨1⟩8.⟨2⟩1 (the D6 (ACE2M-LSZ) anchor) | `q_x^-=S_x^-` (`soft-current-recon.md` ⟨1⟩1); `S_x^-Ω=|x⟩` (D6); `Γ_M(e_n)=∫(dk/2π)e^{-ikn}Σ_xe^{ikx}|x⟩=|n⟩`; `Σ_nf̂(n)a_2(n)Ω=Γ_M(χ_2f)=Γ_M(f)=Σ_xf̂(x)|x⟩` | **CORRECT as a vacuum identity** (`R_ε=0`), with the normalized measure `dk/2π` making `Γ_M` isometric.  **But see R2-O1: this is not the statement ⟨1⟩9.⟨2⟩2 uses** |
| V3 | ⟨1⟩6.⟨2⟩2 (corrected exponents) | four position sums; `‖F_t‖_{ℓ¹(ℤ²)}=O(|t|²)` per side ⟹ `O(|t|⁴)` total; off-cone `≤O(|t|^{1-N})·O(|t|³)` | **CORRECT** — `O(|t|^{4-N})` and `O(|t|⁴⟨ε_v|t|/2⟩^{-N})` are the right exponents; `N≥5` still gives `O(|t|^{-1})→0` |
| V4 | (ACE2M-SR) ⟹ ⟨1⟩9.⟨2⟩3 (Arzelà–Ascoli) | with `j` a genuine sequence index and `A_j∈C¹([0,ε_0];L²(I))`: relative compactness of `{∂_εA_j(ε)}` ⟹ `sup_j‖∂_εA_j‖<∞` ⟹ equicontinuity of `{A_j}`; (SR) gives equicontinuity of `{∂_εA_j}`; Banach-valued AA in `C⁰` twice ⟹ `C¹` subsequence | **VALID** — O3's "nothing to extract from" defect is genuinely repaired |
| V5 | ⟨1⟩2.⟨2⟩1 soft seminorm display | `f_ε(k)=ε^{-1/2}f(k/ε)`, `∂_k^jf_ε=ε^{-1/2-j}f^{(j)}(k/ε)`; `‖f_ε‖_{L²}=‖f‖_{L²}` | **CORRECT** (see R2-N5 for a conservative over-estimate) |
| V6 | ⟨1⟩2.⟨2⟩3 D6 fence + N2 limits | `E_sc−E_b=J(2−2c\cos q)−J(1−c²)=J|e^{iq}−c|²`; along `k_2=k_s→0`, `q→−k_h/2`, `c→\cos(k_h/2)`, `d_B→J(1−c²)=J\sin²(k_h/2)` | **EXACT MATCH** |
| V7 | ⟨1⟩7.⟨2⟩3 exact ML2/D7 match | `e^{iK(x+r/2)}e^{-iqr}=e^{i(k_2x+k_1y)}` (=`A_{21}`, incoming when `v(k_2)>v(k_1)`); `W_+^*W_-=M_{\overline{S^{-1}}}=M_S` iff `|S|=1` | **CORRECT**; the O13 clause closes the last gap.  Chart caveat → **R2-O10** |
| V8 | ⟨1⟩5.⟨2⟩1 (2M-Cook) | expanded `Ha_1(x)a_2(y)Ω` from scratch; `D_1(x)Ω=D_2(y)Ω=0` used exactly twice | **CORRECT** (unchanged from r1) |
| V9 | ⟨1⟩2.⟨2⟩2 / ⟨1⟩7.⟨2⟩2 two-string fence | joint SNAG intertwining `E(Δ)W_±=W_±E_0(Δ)`; `ran W_±⊆ran E(Ī_2)`; `d_B>0` ⟹ `P_BE(Ī_2)=0` | **CORRECT**; the mandatory two-string-isolation attack **fails to break it** |
| V10 | Checker A2M-C1a/C1b, green + 3 mutants, `python3 -O` | full independent implementation (§4) | green exit 0 (C1a `|err|≤3.4e−15`; C1b max ratio `0.049383`), both spec reds exit 1.  **Two spec defects found** → R2-O7 |
| V11 | `theory/checks/soft_index_probe.py --selftest` | re-run | `selftest PASS`, exit 0 |
| V12 | non-vacuity of D31 on D6 | `χ=1` product-state MPS (`λ_E` over an empty set, `ω_A` exactly product); `Γ_M(g)=Σ_xĝ(x)|x⟩` isometric with `HΓ_M=Γ_M ω`; `a_i(n)` = spacetime-filtered `S_n^-`; `\ker H=ℂΩ` (band a.c., no normalizable zero mode) | **D31 IS satisfiable on D6** at each fixed `ε>0` — favourable, but never displayed → **R2-O9(i)** |

The lane's central advance — deriving (D31-C2) from the D1 transfer gap instead
of assuming it — **survives a second, independent attack and is now proved by a
cleaner mechanism** (constant-one Stinespring contractions, no condition
number).  It should be preserved verbatim.

---

## 2. FATAL

None.

---

## 3. MAJOR

### R2-O1 (MAJOR) — `(ACE2M-LSZ)` is a *vacuum-vector* hypothesis, but ⟨1⟩9.⟨2⟩2 uses it as an *operator* statement; on the shard's own D6 anchor the operator statement is contradicted by the corpus's PROVED (R8)

**(a) Location.** ⟨1⟩8 clause (5b) (`Assume Q[f_ε]Ω_A=a_2[f_ε]Ω_A+R_ε, where
substituting the on-shell-null R_ε in every (5a) soft slot gives zero`);
⟨1⟩8.⟨2⟩1 (`Thus (ACE2M-LSZ) holds on D6--D8 with R_ε=0: the charge-created leg
is literally the D31(3) packet`); ⟨1⟩9.⟨2⟩2 (`(5a)'s soft slot is the D31(3)
leg modulo a pairing-null remainder, so the D29 value is the constructed-channel
value`); and ⟨1⟩7.⟨2⟩4's deliberate refusal to port creator-independence.

**(b) My computation.** Three parts.

*(i) The stated hypothesis has no content beyond a definition plus an
undefined clause.*  `R_ε := Q[f_ε]Ω_A − a_2[f_ε]Ω_A` always exists, so the
displayed equation is a definition, not an assumption.  All the content sits in
"substituting the on-shell-null `R_ε` in every (5a) soft slot gives zero".  But
(5a)'s soft slot is filled by the **operator** `Q[f_ε]` acting inside a
connected pairing with hard vectors — clause 1 says the datum is the pairing
"with and without one … soft leg `Q[f_ε]`".  A vector `R_ε` cannot be
substituted into an operator slot.  The clause is meaningful only under the
unstated additional assumption *that the pairing depends on the soft leg only
through the vector `Q[f_ε]Ω_A`* — which is precisely the soft-leg LSZ reduction,
i.e. the thing at issue.

*(ii) That unstated assumption is FALSE on D6, by a PROVED corpus row.*
`soft-current-recon.md` ⟨1⟩2.⟨2⟩3 (inside the chain of the **PROVED** row
S2-2body) states exactly

  `Q_{k_s}|k_h⟩_N − |B^{in}⟩ = (1−S_{12})|P_{12}⟩`   **(R8)**,

with the gloss "the charge creates the root-infinity descendant at zero
momentum, but **away from zero it is not an on-shell scattering state**", and
(R19) `S_{12}=e^{2ik_s+O(k_s²)}`.  So the mismatch is
`−2ik_s|P_{12}⟩+O(k_s²) ≠ 0`, of **exactly the order of the soft law's linear
term** — the term (A2M.3) exists to deliver to Lane S1.  It cannot be waved
away as an on-shell-null remainder.

*(iii) The operator-level reason, in D31's own language.*  `a_{2,b}(n)` is a
spacetime-Schwartz **filtered** creator (D31(3)):
`a_2(n)=∫dt Σ_m F(t,m)e^{itH}τ_{n+m}(S_0^-)e^{-itH}` on D6.  On the vacuum the
filter is transparent because `HΩ_A=0` — that is why V2 above holds exactly.  On
a hard magnon it is **not**: `a_2(n)|k_h⟩` retains only total energy in
`ω_h+\mathrm{supp}_E\tilde F`, discarding the bound-band and far-off-shell
components that `Q[f_ε]=Σ_x\hat f_ε(x)S_x^-` keeps.  The vacuum identity
therefore does not propagate to hard states, and ⟨1⟩8.⟨2⟩1 proves the wrong
statement for its use.

*(iv) The available repair is a source theorem the shard explicitly declines to
port.*  Source Theorem `Haag-Ruelle`'s final clause
(`refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`) — "if
`B̃*_{i,t}(g̃_i)Ω=B*_{i,t}(g_{i,t})Ω` for all `i`, and `V(g̃_i)∩V(g_j)=∅` for
`i≠j`, then `Ψ̃^{out}=Ψ^{out}`" — has exactly the two hypotheses the shard
already owns: matching vacuum-to-one-particle vectors (⟨1⟩8.⟨2⟩1 / clause (5b))
and disjoint velocity supports (D31(4), `ε_v>0`).  ⟨1⟩7.⟨2⟩4 says of it: "The
creator-choice-independence clause … is **not ported**".  So the shard declines
the one result that would turn (5b) into what ⟨1⟩9.⟨2⟩2 needs — *provided* D29's
soft leg is itself carried through the `t→±∞` limit.  If instead D29's soft leg
is a fixed-time insertion (as ML4-Ward's `J^-_0` is, and as the campaign's
"protocol-explicit soft leg" design suggests), creator-independence does **not**
apply and (R8) is the exact, nonzero obstruction.

**(c) FIX DEMAND.** State `(ACE2M-LSZ)` at the level at which it is used — "at
fixed `ε>0` the connected on-shell pairing with the `Q[f_ε]`-created soft slot
equals the pairing with the `a_2[f_ε]` slot" — and then either
**(a)** port the creator-independence clause of source Theorem `Haag-Ruelle` as
a numbered step, checking its hypotheses against D31(4) and ⟨1⟩8.⟨2⟩1, and say
in one line that this requires D29's soft leg to be an asymptotic leg carried
through `t→±∞`; **or (b)** if D29's soft leg is a fixed-time insertion, replace
the D6 "`R_ε=0`" anchor by the honest one: the two legs differ by the PROVED
(R8) branch factor and agree only in their **first jet**, by S2-2body/(R19).
Either way, delete "the charge-created leg is literally the D31(3) packet".

**(d) SURVIVING WEAKER STATEMENT.** On D6--D8 the charge-created soft leg agrees
with the D31(3) filtered magnon packet **exactly on the vacuum** (`R_ε=0`,
verified in V2), and its two-magnon amplitude agrees with the
constructed-channel amplitude **to first order in `k_s`** (S2-2body, (R19)).
The exact amplitude-level identification fails on D6 by `(1−S_{12})|P_{12}⟩`
(R8) and is unproved in abstract D31.  (A2M.3)'s channel identification is
therefore conditional on an amplitude-level hypothesis strictly stronger than
the one displayed in (5b).

---

### R2-O2 (MAJOR) — the sole *unconditional* step of (A2M.3) does not support the theorem statement it is cited for, and its boundedness input lost its hard-window quantifier in the repair

**(a) Location.** ⟨1⟩9.⟨2⟩1 ("Clauses 1 and 3 give a uniform Cauchy–Schwarz
bound, hence every soft sequence has weakly convergent `L²(I)` subsequences");
⟨1⟩1 (A2M.3); ⟨1⟩8 interface clause 3.

**(b) My computation.**  Two prongs.

*(i) The theorem statement over-reads its only unconditional proof.*  Clause 1
defines the **full-index** object `𝒜_{N,W,σ,t}(ε)`.  The Cauchy–Schwarz bound of
⟨2⟩1 is available exactly at that level, so what ⟨2⟩1 honestly proves is: *along
any sequence of index tuples `(N_i,W_i,σ_i,t_i,ε_i)` with `ε_i↓0`, the family is
bounded in `L²(I)` and has a weakly convergent subsequence.*  That is a
**diagonal** statement.  But ⟨1⟩1 (A2M.3) asserts limit points "with `ε→0`
**strictly last**", i.e. of the object obtained **after** `N→∞ ≺ t→±∞ ≺ W↑ℤ ≺
σ↓0`.  For that object to be a sequence in `L²(I)` at all, the inner limits must
exist — and nothing in the shard supplies `lim_{t→±∞}` unconditionally: clause 2
supplies only `N→∞` for *local* matrix elements, and the existence of the fixed-
`ε` `t→±∞` datum is either a wave-operator statement (⟨1⟩5, hence conditional
via R2-O1) or part of `(ACE2M-SR)`'s own setup ("put `A_j(ε):=lim_{t→±∞}lim_{N→∞}
…`", which *presupposes* the limits).  As printed, the lane's one unconditional
claim quantifies over a family that may be empty — the campaign target's
**vacuous-truth landmine**, which `briefs/soft-index-target.md` makes a MAJOR if
left silent.

*(ii) Regression: clause 3 lost its hard-packet quantifier.*  r1 text: "The
amputating hard denominator is nonzero **on the selected hard packet** and is
bounded away from zero along the chosen subsequence."  Repaired text: "The
amputating hard denominator is nonzero and bounded away from zero along the
chosen subsequence."  The datum is `L²(I)`-valued, i.e. a **function of the hard
momentum on `I`**; a uniform `L²(I)` bound needs the denominator bounded below
**uniformly on `I`**, not merely along the subsequence index.  If the denominator
has a zero in the interior of `I`, the datum need not lie in `L²(I)` at all and
⟨2⟩1 fails at its first word.  The repair's one-line compression of clauses 1–4
dropped the only phrase that localized the condition.

**(c) FIX DEMAND.** (i) Restate (A2M.3) and ⟨1⟩9.⟨2⟩1 over the explicit index
set: "for every sequence of index tuples respecting (D29-order) with `ε↓0`, the
datum is bounded in `L²(I)` and has weakly convergent subsequences", and say in
one clause that the iterated-order object exists only under `(ACE2M-SR)`'s
standing assumption.  (ii) Restore and strengthen clause 3: "nonzero and bounded
away from zero **uniformly for hard momenta in `I`** and along the chosen
subsequence", and display the resulting bound `sup‖𝒜‖_{L²(I)}≤C`.

**(d) SURVIVING WEAKER STATEMENT.** Under clauses 1 and 3 with the hard-window
uniformity restored, the full-index family `{𝒜_{N,W,σ,t}(ε)}` is bounded in
`L²(I)`, so every sequence of index tuples respecting (D29-order) with `ε↓0` has
a weakly convergent subsequence.  Nothing unconditional is claimed about the
iterated-order object, whose existence is part of `(ACE2M-SR)`.

---

## 4. Checker audit (obligation 4) — implemented, run green and red under `python3 -O`

Full independent implementation of the **repaired** spec at
`/tmp/.../scratchpad/a2m_c1_r2.py` (AKLT `A^a=σ_a/√3`, `χ=2`, `l=𝟙`, `r=I/2`,
Cartesian `S^a_{bc}=−iε_{abc}`, `E_O(Y)=Σ_{s,s'}O_{s's}A^sY(A^{s'})^†`,
`ω_A(O)=⟨l,E_O(r)⟩`, `P(Y)=tr(Y)r`; no bare `assert`, all gates `raise
SystemExit`).

| run | result | exit |
|---|---|---|
| green (C1a + C1b) | C1a `|err|≤3.35e−15` at `d=1..12`, ratios `−1/3`; C1b max `0.049383` at `(w_C,w_D,d_{sep})=(1,1,2)` ≤ `0.1` | **0** |
| `--red-c1a` (spec red: `E^{d-1}−P → E^{d-1}`) | errs by **exactly 1.000000** at every `d`; both gates fail | **1** |
| `--red-c1b` (spec red: rate `→ λ̃^{d_{sep}+2(w_C+w_D)}`) | max ratio **1.404664** at `(3,2,2)` > `0.1` | **1** |
| `--literal-c1a` (spec read literally, "direct" = raw contraction) | fails by **exactly 1.000000** at every `d` — see R2-O7(i) | **1** |
| `--red-supportfold` (r1 O6's own named mutant `C_{A,λ̃}→C·w_Cw_D`) | **PASSES** — see R2-O8 | **0** |

**Verdict on implementability:** the spec is implementable and red-capable
**after** two textual repairs (R2-O7).  Both spec-mandated red modes exit
nonzero; `theory/checks/` was not touched; `soft_index_probe.py --selftest`
still `PASS`, exit 0 (N7 confirmed, obligation 5).

---

## 5. MINOR

### R2-O3 (MINOR) — `ε_0` is used for two different things, and the fence contradicts its own constant

**(a)** ⟨1⟩2.⟨2⟩3 ("only `ε_0` degenerates, and **`ε_0` occurs in no estimate
below**") vs ⟨1⟩5.⟨2⟩4 (`C_N=C_N(ε_v,ε_0,d_B,η_inel,s_N(F))`); and
D31(4) (`dist(V_i,{0})≥ε_0>0`) vs (ACE2M-SR)/⟨1⟩9.⟨2⟩3 (`C¹([0,ε_0];L²(I))`,
the **soft-scale** interval).

**(b)** Both texts were added by this repair, and they disagree: ⟨1⟩5.⟨2⟩4
displays `ε_0` as an argument of the Cook constant while ⟨1⟩2.⟨2⟩3 asserts it
occurs in no estimate.  This is not cosmetic: ⟨1⟩2.⟨2⟩1's claim that the
seminorms "carry the soft-family divergence" is only true if the one parameter
that *does* degenerate as `ε↓0` enters nothing.  Independently: `ε_0` is in fact
**not needed** for (A2M.1)–(A2M.2) — the Cook and Gram cone bounds use only
`|x−y|≥ε_v|t|/2` (velocity *separation*), never `dist(V_i,{0})`; nonzero
velocities matter in the kink parent (`ansatz-scattering.md`) because the kink is
at rest, not here.  Separately, `[0,ε_0]` in (SR) re-uses the same symbol for the
soft scale, whose degeneration is *caused by* `ε_0(ε)→0` — a symbol whose two
meanings move in lockstep is the worst possible collision (L4).  Neither `ε_v`
nor `ε_0` appears in the proposed `notation.md` rows, and `notation.md`'s
existing `ε_v` row is scoped to D28.

**(c) FIX DEMAND.** Drop `ε_0` from `C_N`'s argument list in ⟨1⟩5.⟨2⟩4 (and
state in ⟨1⟩2.⟨2⟩1 that `ε_0` is a D31(4) hypothesis used by no estimate in
§§2–3); rename (SR)'s interval endpoint to e.g. `ε_★`; add `ε_v,ε_0` rows to the
`notation.md` merge block scoped to D31.

**(d)** Everything else in the O1/N2 repair stands: the seminorm mechanism and
the D6 limits `ε_v→|v_h|`, `d_B→J\sin²(k_h/2)`, `η_inel=+∞` are correct (V5, V6).

### R2-O4 (MINOR) — (D29-order) clause 4 is iterated, but (SR) and ⟨1⟩9.⟨2⟩3 use a diagonal `(W_j,σ_j)`

**(a)** ⟨1⟩8 clause 4 (`N→∞ ≺ t→±∞ ≺ W↑ℤ ≺ σ↓0 ≺ ε↓0`) vs (ACE2M-SR) ("let `j`
index `(W_j,σ_j)` with `W_j↑ℤ`, `σ_j↓0`") and ⟨1⟩9.⟨2⟩3's `lim_ℓ`.

**(b)** A joint sequence `(W_j,σ_j)` is a **diagonal**; the iterated limit
`lim_{σ↓0}lim_{W↑ℤ}` neither implies nor is implied by it.  r1's O3 asked for
`lim_j` in the display (correctly — the iterated limits do not exist), but clause
4 was left asserting the iterated order, so the shard now asserts an interface
condition that its own proof does not realize.  Since clause 4 is an *interface
assumption on Lane S1's D29*, a mismatch here is a merge hazard, not a
typographical one.

**(c) FIX DEMAND.** Either weaken clause 4 to "no later operation is taken inside
an earlier one; `W↑ℤ` and `σ↓0` may be taken jointly along a sequence", or state
in (SR) that the diagonal is a specialization and record that the iterated order
is not claimed.

**(d)** The essential discipline — `N,t` first, `ε` strictly last — is respected
in every display.

### R2-O5 (MINOR) — (A2M.3)'s statement has a dangling quantifier

**(a)** ⟨1⟩1(A2M.3): "For each fixed soft packet scale `ε>0` satisfying D31,
Lane S1's intended protocol data have weak `L²(I)` subsequential limit points
with `ε→0` strictly last."

**(b)** If `ε` is fixed there is no `ε→0`; the sentence binds `ε` twice.  The r1
opener survived a rewrite of the rest of the clause.  In a theorem whose r1
verdict's principal MAJOR was quantifier incoherence, the statement line should
be exact.

**(c) FIX DEMAND.** "The data are defined for each fixed `ε>0` satisfying D31,
and the family `{·(ε)}_{ε>0}` has weak `L²(I)` subsequential limit points as
`ε↓0`, that operation taken strictly last."

**(d)** The intended content is clear and is what ⟨1⟩9 proves (subject to R2-O2).

### R2-O6 (MINOR) — three residual lockstep drifts (row vs proof; depends-on; notation)

**(a)(i)** Claims row: "a fixed packet range **matches** the corresponding part
of ML2's Jacobi scattering summand" vs ⟨1⟩7.⟨2⟩4: "**is a closed subspace of**
the matching part".  r1's O5 demanded ⟨2⟩4 not be stronger than the row; the
repair has left the row marginally stronger than ⟨2⟩4, re-importing an
exhaustion flavour into the one cell a reader quotes.  **Fix:** row → "lies in".

**(a)(ii)** Depends-on cell is `D1, D3(a), D6--D8, D12(a′), D31, ML2, S2-2body`,
but **D10(c)** is cited in ⟨1⟩8.⟨2⟩1's justification (newly, by this repair) and
**D24(b)** in interface clause 1, in (ACE2M-SR)'s justification and in
⟨1⟩9.⟨2⟩4's.  Both are load-bearing for (A2M.3).  **Fix:** add `D10, D24` to the
depends-on cell.  (I confirmed D3(a) and D12(a′) are *not* phantoms: they supply
the profile-class and `ℓ¹∩BV` wave-packet discipline the shard actually uses.)

**(a)(iii)** New symbols introduced with no `notation.md` row: `s_N(F)`, `V_w`,
`Ψ_D`, `A_j(ε)`, `Q[f_ε]`, `a_2[f_ε]`, `R_ε`, `f_ε`, plus `ε_v,ε_0` (R2-O3).
**Fix:** add rows or point at the shard step that fixes each (L4).

**(d)** All three are cell-level; every proof-text statement is correct as
written.

### R2-O7 (MINOR) — A2M-C1a as repaired is not implementable as printed: "connected" was deleted, and the ratio gate has no tolerance

**(a)** §6, A2M-C1a: "contract `C=D=I+S^z` directly and independently as
`⟨l,E_C(E^{d-1}-P)E_D(r)⟩`.  **Both answers must equal** `4/3·(-1/3)^d` within
`10^-12` **and successive ratios** `-1/3`."

**(b)(i)** The r1 text read "Both **connected** answers must equal …"; the repair
dropped the word.  The *direct* contraction is
`ω_A(C_0D_d)=1+⟨S^z⟩+⟨S^z⟩+⟨S^z_0S^z_d⟩=1+(4/3)(−1/3)^d`.  My `--literal-c1a`
run fails the green gate by **exactly 1.000000 at every `d`** (exit 1) — the same
signature as the spec's own red mutant, which is the tell that the intended
reading is the connected one (the red text says "its retained `+1` must fail both
gates").  As printed, green and red are indistinguishable.
**(ii)** The ratio gate has **no stated tolerance**.  Taking the spec's own
`10^-12` for it fails the *green* run: the ratio deviation grows by `×3` per step
(`1.06e−15, 5.05e−15, …, 1.69e−10, 5.61e−10` at `d=2,…,12`), because the value
gate is *absolute* while values decay to `2.5e−6`, so the ratio gate is
effectively *relative*.  Any tolerance `≤5.6e−10` fails green at `d=11,12`; the
spec's `1e−12` fails from `d=7`.

**(c) FIX DEMAND.** Restore "Both **connected** answers" (or define "direct" as
`ω_A(CD)−ω_A(C)ω_A(D)`), and state the ratio tolerance explicitly (`1e−8`
works with margin; `|ratio+1/3|≤1e−8`), or cap `d` at `8`.

**(d)** With those two words restored, A2M-C1a is exactly implementable and
red-capable: green `|err|≤3.35e−15`, spec red exit 1 with error exactly `1.0`.

### R2-O8 (MINOR) — A2M-C1b's cap is saturated at `w=1`, so it barely tests what it was added to test

**(a)** §6, A2M-C1b: `max_{w_C,w_D,d_{sep}}|conn|/(‖C‖‖D‖λ̃^{d_{sep}})≤0.1`,
red = "replace the rate by `λ̃^{d_{sep}+2(w_C+w_D)}`".

**(b)** Measured (green): the max is `0.049383` at `(w_C,w_D,d_{sep})=(1,1,2)`
and the ratio **decreases** monotonically in `w` (`0.049383, 0.016461, 0.004115`
at `d_{sep}=2` for `w_C=1,2,3` with `w_D=1`), because `‖C_w‖=2^w` grows faster
than `|conn|`.  So the gate is decided entirely by the `w=1` row that A2M-C1a
already covers, with margin `0.1/0.049383 = 2.02×`: any support-length growth
smaller than a factor `2.02` passes undetected.  The spec's red mutation shrinks
the denominator (`λ̃^{larger}`), which is the *rate* direction, not the *constant*
direction the gate exists to certify.  Concretely, r1's O6 named the mutant
"`C_{A,λ̃}` replaced by `C·w_Cw_D`"; I implemented it (`--red-supportfold`) and it
**passes, exit 0**.

**(c) FIX DEMAND.** Add a monotonicity gate that is actually about `w`:
require `ratio(w_C,w_D,d_{sep}) ≤ ratio(1,1,d_{sep})` for all `w_C,w_D∈{1,2,3}`
(true here with room), with a red mutation that multiplies `|conn|` by
`w_Cw_D`; or extend to `w∈{1,…,5}` and gate on the *variation*, not the max.

**(d)** A2M-C1b as written still certifies, on AKLT, that the ratio is bounded by
`0.1` uniformly over `w_C,w_D∈{1,2,3}` and `d_{sep}∈{2,4,6}`, and that direct and
fixed-point-subtracted contractions agree to `1e−12` at every one of the 27
points — real evidence for the support-length independence of `C_{A,λ̃}`, just
weaker than "uniform in `w`".

### R2-O9 (MINOR) — the D6 non-vacuity anchor rests on two steps that are never displayed

**(a)** ⟨1⟩9.⟨2⟩4.

**(b)(i)** *D6 ⊨ D31 is never verified.*  Every anchor (⟨1⟩2.⟨2⟩3, ⟨1⟩7.⟨2⟩3,
⟨1⟩8.⟨2⟩1, ⟨1⟩9.⟨2⟩4) says "on D6--D8" and silently assumes D31 holds there.  I
checked it (V12) and it **does** hold at each fixed `ε>0` — `χ=1` product MPS,
`Γ_M` isometric with `HΓ_M=Γ_Mω`, `\ker H=ℂΩ_A` despite gaplessness, filtered
`S_n^-` creators — but a theorem whose only defence against the vacuous-truth
landmine is one model must display that model's satisfaction of its hypotheses.
**(ii)** *"C² in `k_s`" ⟹ "C¹ in `ε`" is not displayed.*  S2-2body gives
`|R_δ|≤C_δ(a,b)|k_s|³` uniformly on `D_{ab}` — a statement about the **soft
momentum**.  `(SR)` needs `ε↦A(ε)∈C¹([0,ε_★];L²(I))` — a statement about the
**soft packet scale**.  The bridge is the smeared Taylor expansion
`A(ε)=A(0)+ε·∂_{k_s}𝖲|_0·m_1+O(ε²)` with `m_1` the first moment of the
normalized profile, which is legitimate under D24(b)'s own convention
("for `f_ε(k)=ε^{-1/2}f(k/ε)`, as `O(ε²)` in the product packet norm") — but the
conclusion is normalization-sensitive: with an amputation carrying an extra
`ε^{-1}`, the same hard data give `A(ε)∼ε^{1/2}`, which is continuous but
**not** `C¹` at `0`, and the anchor would fail.

**(c) FIX DEMAND.** Add one leaf verifying D31(1)–(5) on D6, and one displayed
line taking the smeared Taylor expansion from S2-2body's cubic `k_s` remainder
to `A∈C¹([0,ε_★];L²(I))`, naming the amputation normalization used.

**(d)** With D24(b)'s stated `f_ε` convention the inference is correct and the
exhaustion-free anchor stands; only its display is missing.

### R2-O10 (MINOR) — the fixed-pair ML2 identification still needs the `K`-chart map

**(a)** ⟨1⟩7.⟨2⟩3--⟨2⟩4.

**(b)** ML2's chart is `−π<K≤π`, `0<q<π`, where `c=\cos(K/2)∈[0,1]`; (17)'s
`e^{iK(x+r/2)}` is anti-periodic in `K` for odd `r`.  A D31 pair with
`K_Σ=K_1+K_2` outside `(−π,π]` folds, sending `c→−c` and shifting the branch
labels, so ⟨2⟩3's stationary-phase assignment of `e^{∓iqr}` to in/out is stated
on a chart the packet pair need not lie in.  r1 flagged this inside O5 and
offered a disjunction; the repair took the other branch, so the point is still
open — and it applies to the **fixed-pair** claim too, not only to a union.  (The
gap `E_{sc}−E_b=J|e^{iq}−c|²` is folding-invariant, so ⟨1⟩2.⟨2⟩3 is unaffected.)

**(c) FIX DEMAND.** One clause: "`(k_1,k_2)↦(K \bmod 2π, q∈(0,π))` maps the
packet pair into ML2's fundamental domain; the in/out labelling of ⟨2⟩3 is stated
there", or restrict D31's windows to `K_Σ⊂(−π,π]`.

**(d)** For packet pairs with `K_Σ∈(−π,π]` the exact-match computation is
correct as verified in V7.

### R2-O11 (MINOR) — `Q[·]` silently changes argument convention from D10(c), and (5b)'s `b` index dangles

**(a)** ⟨1⟩8 clauses 1, (5b) and ⟨1⟩8.⟨2⟩1.

**(b)** D10(c) fixes `Q[f;ξ]:=Σ_x f(x)q_x(ξ)` with `f` a **position-space**
profile in `𝔉_c(ξ)`; the shard's `Q[f_ε]` has a **momentum-space** argument
(`f_ε(k)=ε^{-1/2}f(k/ε)`), and ⟨1⟩8.⟨2⟩1 correspondingly writes
`Q[f]Ω=Σ_x\hat f(x)S_x^-Ω`.  The same bracket therefore means
`Q[\hat f_ε;ξ^-]` in D10(c)'s notation — a Fourier transform apart.  A merge that
misses this flips a convention in the one identity the anchor rests on.  Also,
`q_x^-=S_x^-` is fixed in `soft-current-recon.md` ⟨1⟩1 (per `notation.md` l.186),
not in D10(c), whose `q_x(ξ)` is anti-Hermitian with real `ξ`; the leaf cites
D10(c) alone.  Finally `a_2[f_ε]Ω_A:=Σ_n\hat f_ε(n)a_{2,b}(n)Ω_A` has a free `b`
on the right and none on the left.

**(c) FIX DEMAND.** Write `Q[\hat f_ε;ξ^-]` (or declare the momentum-argument
convention once, in the notation merge block); cite `soft-current-recon.md` ⟨1⟩1
for `q_x^-=S_x^-` alongside D10(c); bind `b` on both sides.

**(d)** With the conventions made explicit the D6 vacuum identity is exact
(V2), including the `dk/2π` measure that makes `Γ_M` isometric.

---

## 6. NOTE

**R2-N1 — D31-C2 (⟨1⟩3) is undamaged and strictly stronger.**  Obligation 5
discharged: ⟨2⟩1 and ⟨2⟩3 are byte-identical to r1; only ⟨2⟩2 changed, and the
new mechanism is the one that works, with both contraction constants equal to
one and uniformity in the two support lengths now explicit and
numerically corroborated at 27 points (§4).

**R2-N2 — `Ψ_C` is used before definition.**  ⟨1⟩3.⟨2⟩2 defines only
`Ψ_D(r):=tr_{d^w}[(D⊗𝟙)V_wrV_w^†]` and then writes `|tr Ψ_C(Z)|≤‖C‖‖Z‖_1` and
(implicitly) `ω_A(CD)−ω_A(C)ω_A(D)=tr Ψ_C((E^{d_{sep}}−P)Ψ_D(r))`.  Say
"`Ψ_O(Y):=tr_{d^{w_O}}[(O⊗𝟙)V_{w_O}YV_{w_O}^†]=E_O(Y)`" once and display the
chain identity; it is one line and it is the link to ⟨2⟩1.

**R2-N3 — the non-circularity note is under-inclusive.**  ⟨1⟩2.⟨2⟩2 justifies
its forward reference by "⟨1⟩5 uses only D31(2)--(4) and ⟨1⟩4, not ⟨1⟩2", but the
referenced step ⟨1⟩7.⟨2⟩2 ASSUMEs ⟨1⟩5–⟨1⟩6, and ⟨1⟩6 ASSUMEs ⟨1⟩3–⟨1⟩5.  The
chain is still acyclic (none of ⟨1⟩3–⟨1⟩7 uses ⟨1⟩2) — I checked — but the stated
reason names the wrong witness.

**R2-N4 — matrix kernel residue after the N4 repair.**  D31(2) now fixes a
**scalar** band `ω` with multiplicity space `ℂ^m` (`HΓ_M=Γ_M(ω⊗1_m)`), while
⟨1⟩4.⟨2⟩2 still carries the matrix kernel `h_{i,b'b}(m-n)`.  Harmless
(`h_{i,b'b}=δ_{b'b}h_i`), but under the repaired D31 it should be scalar.

**R2-N5 — the `ε^{-N}` fence is conservative, not sharp.**  ⟨1⟩2.⟨2⟩1's
"the `N` integrations by parts contribute `ε^{-N}`" ignores the `O(ε)` measure of
`\mathrm{supp}f_ε`, which improves the true rate to `ε^{1/2-N}`.  Over-stating a
divergence in a fence is safe, so this is not an objection; but the parenthetical
"(equivalently the raw `L∞` seminorm has the displayed additional `ε^{-1/2}`
factor)" reads as if it were an identity and should be marked as a bound.

**R2-N6 — `ε_0` is not needed by (A2M.1)–(A2M.2) (favourable, unstated).**  As
computed in R2-O3, the Cook and Gram cone bounds use only velocity *separation*.
D31(4) could drop `dist(V_i,{0})≥ε_0>0` for these two parts, which would make the
theorem strictly stronger and would also remove the last parameter that
degenerates in the soft limit.  (`ε_0>0` is still convenient in ⟨1⟩2.⟨2⟩3, though
`ε_v>0` alone already excludes the `q=0,c=1` zero there, since `V_1∩V_2=∅ ⟹
K_1∩K_2=∅ ⟹ k_1≠k_2`.)

**R2-N7 — port audit: unchanged and re-verified where edited.**  The repair
touched two of the ported/adapted steps: ⟨1⟩5.⟨2⟩1's justification (domain
clause, O12) and ⟨1⟩6.⟨2⟩2's exponents (O7).  Both re-verified against
`ansatz-scattering.md` ⟨1⟩5.⟨2⟩2 and ⟨1⟩6.⟨2⟩1–⟨2⟩2.  r1's N6 table stands; the
one un-ported source result (creator independence) is now consequential — R2-O1.

**R2-N8 — checker semantics and REFUTED rows: clean.**  A2M-C1 remains
self-contained and does not touch or contradict the frozen P1–P4 semantics of
`theory/checks/soft_index_probe.py` (`--selftest` re-run: PASS, exit 0).  No
reliance on ML5, the withdrawn `S2` label, M-INDEX-LA-strong, or ML1/ML3/ML6; no
contradiction of D24(e)'s `O_η` counterexample or the G0-soft-r1 kinematic-factor
fence (no bare `(e^{ik_s}−1)` soft factor appears anywhere).  D2(a) and D17 are
gone.

---

## 7. Register comparison against the adjudicated AC-EX row (obligation 3, re-run)

| Item | AC-EX adjudicated register | AC-EX-2M (repaired) | Verdict |
|---|---|---|---|
| Cook/isometry | "proved **only** as the conditional implication" from D28 | proposer status says the same from D31 | **in register** |
| clustering | "(D28-C) is the load-bearing hypothesis and is **unverified on any model**" | D31-C2 **derived** from D1(c,d) by a constant-one Stinespring argument; corroborated at 27 numerical points | **stronger, and earned** — the lane's real advance, twice survived |
| bound states | "No … bound-state exclusion … is claimed" | `P_BW_±=0` for **D31-listed** bands, derived from `d_B>0`; row and HONEST STATUS both carry "D31-listed" | **stronger with a stronger hypothesis**; argument re-verified (V9) |
| thresholds | "Remark D28-R's threshold inequalities are used in no step" | D31(5)'s `η_inel/Θ_inel` are used (⟨1⟩7.⟨2⟩2) | in register (D31 hypotheses, not a fence) |
| completeness / range | "No completeness…"; "No assertion is made … that `H_out^{ex}` exhausts a spectral subspace" | ⟨1⟩7.⟨2⟩4 fixed-pair only; row adds "range exhaustion" to the disclaimer | **BREACH CLOSED** (r1's only register breach); residual row wording → R2-O6(i) |
| soft limit | "no soft limit is claimed" | soft scale strictly last; `W_±^{(ε)}` fixed-`ε`; seminorm divergence displayed | **in register**, O1/O14 wording now correct |
| nonvacuity | (not applicable to AC-EX) | conditional on `(ACE2M-LSZ)`/`(ACE2M-SR)`, both named, both declared open abstractly | in register **as declared**; but the LSZ hypothesis as displayed is weaker than its use → R2-O1 |

The r1 breach is closed.  The repaired shard is nowhere stronger than its
precedent without a correspondingly stronger displayed hypothesis — with the one
exception that ⟨1⟩9.⟨2⟩2 draws an amplitude-level conclusion from a
vector-level hypothesis (R2-O1).

---

## 8. Summary

- **FATAL 0**
- **MAJOR 2** — R2-O1 ((ACE2M-LSZ) is stated on vectors and used on operators;
  its D6 "proof" does not transfer, and the corpus's PROVED (R8) contradicts the
  operator-level reading on the anchor model), R2-O2 (the sole unconditional step
  of (A2M.3) proves a diagonal statement while the theorem asserts an iterated
  one, and clause 3 lost its hard-window quantifier in the repair)
- **MINOR 9** — R2-O3 … R2-O11
- **NOTE 8** — R2-N1 … R2-N8

**Trajectory: 6 MAJOR → 2 MAJOR, 0 FATAL throughout.**  Fourteen of the fifteen
r1 objections and all eight NOTEs are VERIFIED-FIXED by recomputation, not by
inspection; O2 is PARTIALLY-FIXED.  §§0–3 of the shard — the D31-C2 derivation
(now via a strictly better mechanism), the Cook estimate, the isometry with
corrected exponents, the bound-band/two-string fence, and the exact ML2/D7
match with `|S|=1` — are **sound and independently reproduced for the second
time**, and (A2M.1)–(A2M.2) can be promoted to SKETCH once R2-O3, R2-O6,
R2-O7, R2-O10 are applied.  (A2M.3) still cannot be promoted: its conditional
half rests on a hypothesis that does not say what its use requires (R2-O1) and
its unconditional half is stated for a family the shard does not construct
(R2-O2).  Both are repairable at the surviving-statement ceilings given above,
and R2-O1's fix (a) would *upgrade* the lane by turning `(ACE2M-LSZ)` into a
theorem.

**FAIL(R2-O1,R2-O2)**
