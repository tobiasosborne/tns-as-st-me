<!-- ROLE: r4 ADJUDICATION verdict on theory/ansatz-scattering-2m.md
     (Theorem AC-EX-2M, Lane S2).  Priors: ansatz-scattering-2m-r1.md,
     -r2.md, -r3.md.  Work order: briefs/s2-critic-r4.md +
     briefs/critic-protocol.md (incl. the 2026-08-29 standing checker
     obligations and the "every gate can FAIL AT ALL" addendum).
     Writable lane: this file only. -->

# Critic verdict r4 — `theory/ansatz-scattering-2m.md` (Theorem AC-EX-2M, Lane S2)

Critic: Opus, adversarial, 2026-08-29.  **Adjudication round.**  Priors:
`theory/verdicts/ansatz-scattering-2m-r1.md`, `-r2.md`, `-r3.md` (mine).
Work order audited: `briefs/s2-repair-r3.md`.  Claimed dispositions:
`theory/ansatz-scattering-2m-r3-response.md`.

Repair round audited: `git diff cf2e443..65a6d32` — 15 hunks in
`theory/ansatz-scattering-2m.md`, 35 changed lines in
`theory/checks/ansatz_scattering_2m_check.py`.  Reading was scoped to the
diff; **§§1–3 of the shard were confirmed untouched** (zero hunks between
lines 65 and 370) and r3 §7's fenced list is not churned.

All prototype computation in
`/tmp/claude-1000/…/scratchpad/{indep_c1.py,mut/m1…m16.py}`; nothing outside
this file was written, no commit.

**Headline.** The downgrade is **substantially executed but not complete**.
Six copies of the quarantine sentence, byte-for-byte lockstep with the merged
row, five of six MINORs genuinely fixed — and then **one untouched leaf,
`⟨1⟩9.⟨2⟩5`, still computes the D6 instance of `(ACE2M-SR)` by identifying
the D29 datum with `S_phys`, and justifies that identification by citing
`⟨1⟩8.⟨2⟩1–⟨2⟩2`, the very port the shard says six times does not apply.**
That leaf silently assumes exactly the branch-(i) result the prover declined
to prove.  The `ratio_route` gate is **not** a replacement: it is the r3 gate
**renamed**, byte-for-byte blind to the same mutation — but the prover
*retracted the claim* rather than pretending otherwise, which is the honest
disposition the repair brief authorized.

---

## 0. Disposition verification table (round obligation 1)

Every row verified by fresh recomputation, by running mutants on copies, or by
reading the local TeX — never by reading the response.

| id | claimed | **r4 verdict** | evidence |
|---|---|---|---|
| R3-O1 | DOWNGRADED | **PARTIALLY-EXECUTED** | The statement layer, interface clauses 1/5, `⟨1⟩8.⟨2⟩2`, `⟨1⟩9.⟨2⟩2`, `⟨1⟩9.⟨2⟩6–⟨2⟩7`, `⟨1⟩10.⟨2⟩3`, §7 and §8 are all correctly quarantined; `grep` finds the sentence "**This theorem does NOT apply to the adjudicated D29.**" at ll.11, 61, 396, 510, 665, 776 (6×) and once in `claims/CLAIMS.md`.  §4's heading is no longer "nonvacuity bridge to Lane S1".  **But `⟨1⟩9.⟨2⟩5` — the sole D6 instance of `(ACE2M-SR)` — was not touched by the diff and still reads the identification as available** → **R4-O1 (MAJOR)** |
| R3-O2 | RETRACTED | **VERIFIED-FIXED as a retraction; the gate is unchanged** | `git diff` shows the gate expression `abs(ratio - direct_ratios[location])` is **identical**, only the identifiers changed (`support_profile_*` → `ratio_route_*`).  I reran both two-sided folds on copies: fold into the constant (r3's mutation, `m1`) → **exit 0**; fold multiplying both routes (`m2`) → **exit 0**; in both, `ratio_route=1.187e-15` is *bit-identical to the unmutated green run*.  §6, the module docstring and the merged row now all say so.  The FIX DEMAND offered "delete the sentence … **or** state in Uncertified scope that … is not excluded up to a `w_Cw_D` factor"; the prover took the second disjunct, which `briefs/s2-repair-r3.md` explicitly authorized.  Residues → **R4-O2, R4-O3, R4-O4** |
| R3-O3 | FIXED | **VERIFIED-FIXED** | Clause 3 now reads "On the **selected hard packet**, **for every allowed full index tuple `α` in the D29 interface family**, assume the displayed uniform … bounds" — the r3 demand verbatim in substance.  `⟨1⟩1(3)` says "for every sequence of full index tuples … in the D29 interface family"; `⟨1⟩9.⟨2⟩1` uses "for any full-index sequence".  All three quantifiers now agree with the displayed `ess inf_α`/`sup_α` |
| R3-O4 | FIXED | **VERIFIED-FIXED** | `grep unconditional` → 2 hits, both in the honest negative direction ("no unconditional existence of the iterated …", "nothing unconditional is claimed").  Clause 4 now says "the statement below, **conditional only on `(D29-den)`**".  Clause 3 closes with "**Both displayed inequalities are assumptions**; Cauchy--Schwarz … is the model for the numerator assumption, **not a derivation of it in this shard**" |
| R3-O5 | FIXED | **VERIFIED-FIXED** | The added paragraph at `⟨1⟩8.⟨2⟩1` is the demanded sentence.  I checked its two load-bearing claims independently: (i) D31(2) as merged in §7 does read "isolated **within the charge-one sector** on clause 4's packet neighbourhoods", so the relativization is owned, not invented; (ii) I read `(creation-on-vacuum)` in `refs/arxiv-1412.2970/Scattering_spin-AHP1.tex` ll.1138–1147 and confirmed its derivation needs exactly `B^*Ω=P(𝔥)B^*Ω`, i.e. the *vector-level* support statement the shard asserts, nothing global.  `commutators-decay(a)`'s independence of isolation was already V2 in r3 |
| R3-O6 | FIXED | **VERIFIED-FIXED, citation checked in the local TeX (L3)** | Source, verbatim, l.1379: "*Demanding in addition that `\wh f` is equal to one on `\mfh\cap \Sp_{A^*}\tau` we can ensure that `B^*_{f,t}(g_t)\Om=B_t^*(g_t)\Om`*" — inside the proof of Theorem `Haag-Ruelle-Fock` (`\bet\label{Haag-Ruelle-Fock}`, l.1338).  The shard's rendition restricts the demand to `supp f_ε`, which is a *weakening* that still suffices for the vacuum-vector statement (2M-1P) and for nothing else — correct as used.  `b=1` is now bound on both sides of the display, closing R2-O11's cosmetic residue |
| R3-O7 | FIXED | **VERIFIED-FIXED** | `⟨1⟩1(3)`: "The diagonal compactness and fixed-`ε` HR statements concern different families and are not composed here."  `⟨1⟩9.⟨2⟩2` tail: "no channel identification for Lane S1 follows from this step."  `⟨1⟩9.⟨2⟩6`: "…are not joined.  Even `(ACE2M-SR)` supplies regularity/limit-order control, not the missing fixed-time amplitude matching."  §8 repeats it.  Four layers, same strength |
| R3-N1 | FIXED | **VERIFIED-FIXED by exit path** | §6 now says "must fail the **route-value and successive-ratio** gates"; the actual `--red-c1a` exit path is exactly `{C1a route value 1.000000e+00, C1a ratio 2.400000e+00}` — the direct-value gate does *not* fire.  Spec and behaviour now name the same two gates |
| R3-N2 | FIXED | **VERIFIED-FIXED by independent recomputation** | My re-implementation in the *standard spin-1 `S^z` AKLT basis* (different tensors) gives `monotonicity_excess = −6.5030737e−03 at (1,2,6)` with the baseline excluded and **exactly `0.0` at `(1,1,2)`** with it included.  The claimed new green margin `−6.503e−03@(1,2,6)` reproduces to five digits from a different basis |
| R3-N3 | RESIDUE | **VERIFIED** | All four runs reproduce the pasted stdout exactly under `python3 -O` from the committed tree.  Fourth consecutive round with trustworthy reported numbers |
| R3-N4 | RESIDUE | **VERIFIED by fresh recomputation** | See V3 below: `(1−S_{12})/(−2ik_s) → 1` at every `k_h`, and `∂_{k_s}δ|_0 = 2.000000000` at `k_h∈{0.4,1.0,2.0,3.0}` |
| R3-N5 | RESIDUE | **VERIFIED** | Every 1412.2970 anchor in the new text resolves to a real `\label`; the newly added filter-transparency citation is quoted correctly (R3-O6 row).  No from-memory citation |
| R3-N6 | RESIDUE | **VERIFIED** | `git diff` has **zero hunks** between shard lines 65 and 370; `⟨1⟩3` is byte-identical.  Fenced list not churned |
| R3-N7 | FIXED | **VERIFIED-FIXED** | The shard no longer states the asymptotic-leg reading as a description of D29; clause 1 now names both D29 sources and the binding adjudication and calls the datum fixed-time |
| R3-N8 | RESIDUE | **VERIFIED** | `git diff --name-only cf2e443 HEAD -- theory/checks/` = `{ansatz_scattering_2m_check.py, d24d3_normalization_check.py}`; the second is the D24(d)3 lane's file in the same orchestrator commit, not this lane's edit.  `soft_index_probe.py` and every other frozen checker are byte-identical |

**Nothing REGRESSED.**  Twelve of fifteen dispositions are VERIFIED-FIXED,
two are VERIFIED as residues, one (R3-O1) is **PARTIALLY-EXECUTED**.  The
single MAJOR is not a re-opening of R3-O1's text: it is the *one leaf the
downgrade forgot*.

---

## 1. What I independently recomputed (obligation: recompute, never referee)

| # | step | method | outcome |
|---|---|---|---|
| **V1** | **byte-for-byte lockstep**, shard §7 row vs `claims/CLAIMS.md` l.77 | extracted both lines to files and ran `cmp` | **IDENTICAL, 3408 bytes each.**  The prover's central lockstep claim is **TRUE** |
| **V2** | is the *merged* row itself the r3 scoping sentence? | word-diff of the statement cell against the `> Under D31…` blockquote of `ansatz-scattering-2m-r3.md` §9 | **identical except two mandatory markdown pipe-escapes** (`\|𝒟_α(h)\|`, `\|k_h⟩`); no semantic drift, nothing added, nothing dropped |
| **V3** | (R8)+(R19), from scratch, not from `soft-current-recon.md` | `S_{12}(k_s,k_h) = −(e^{i(k_s+k_h)}−2e^{ik_s}+1)/(e^{i(k_s+k_h)}−2e^{ik_h}+1)`, evaluated numerically | `S_{12}(0,k_h)=1` exactly; `(1−S_{12})/(−2ik_s) → 1.0000917, 1.0000915·10^{-…}` etc., converging to `1` at `k_h=0.4,1.0,2.0,3.0`; `∂_{k_s}\arg S_{12}|_0 = 2.000000000` at every `k_h`.  **`1−S_{12} = −2ik_s+O(k_s²)` reproduced; S2-2body-S's `1/S = 2` at `S=1/2` reproduced** |
| **V4** | the size of the R8 obstruction *in the units of `⟨1⟩9.⟨2⟩5`'s conclusion* | `‖Q_{k_s}\|k_h⟩−\|B^{in}⟩‖ / ‖\|B^{in}⟩‖ = \|1−S_{12}\|/\sqrt{\|S_{12}\|²+1}` | `1.5487e−01` at `k_s=0.1`, `1.4272e−02` at `k_s=0.01`, `1.4155e−03` at `k_s=0.001` — i.e. `√2·k_s·(1+O(k_s))`.  **The fixed-time D29 vector and the constructed in-state differ at relative order `ε`, the exact order of the first jet `⟨2⟩5` computes.**  This is the quantitative content of R4-O1 |
| **V5** | `⟨1⟩9.⟨2⟩5`'s Taylor arithmetic (fenced by r3 V4 — reproduced, not re-litigated) | `f` smooth on `[1,2]`, `‖f‖_2=1`, `m_1=1.5`; `A(ε)(h)=∫dμ_f S_{12}(εu,h)` on a 41-point hard grid | `max‖A(ε)−A(0)−εm_1∂_{k_s}S(0,·)‖ / ε² = 14.17, 10.36, 10.07` at `ε=10^{-1},10^{-2},10^{-3}` — a **stable `O(ε²)` remainder**.  The computation is right; only its *licensing* is not (R4-O1) |
| **V6** | `⟨1⟩3.⟨2⟩2`'s support-length independence — because §6 newly asserts "*support-length independence is proved analytically in `⟨1⟩3`*" | re-derived the chain: `‖Ψ_D(r)‖_1≤‖D‖`, `\|tr Ψ_C(Z)\|≤‖C‖‖Z‖_1` ⟹ `\|ω_A(CD)−ω_A(C)ω_A(D)\| ≤ ‖C‖‖D‖·‖E^{d_sep}−P‖_{1→1}` | **CORRECT, and trivially support-independent**: the bounding factor `‖E^{d_sep}−P‖_{1→1}` contains no reference to `C`, `D` or their lengths at all.  The new §6 sentence is a **true** addition, cross-referring to a step r3 fenced |
| **V7** | checker A2M-C1a/C1b, **independent re-implementation** from the §6 spec in the standard spin-1 `S^z` AKLT basis (`A^{+}=√(2/3)σ^+`, `A^0=−σ^z/√3`, `A^-=−√(2/3)σ^-`), left/right fixed points verified before use | see §4 | **reproduces every number**: `max_ratio 0.049383@(1,1,2)`; full ratio table; `monotonicity_excess −6.503e−03@(1,2,6)`; `ratio_route` at `(1,1,6)`; C1a errors `1.04e−15` (theirs `3.35e−15`), ratio deviation `1.75e−10` (theirs `5.61e−10`), the `1e−12` ratio tolerance failing green from `d=8` in my basis |
| **V8** | the `ratio_route` gate, **symbolically** | `ratio−direct_ratio = (\|F_α\|−\|D_α\|)/(‖C‖‖D‖λ̃^{e})`; denominators are exactly `2^{w_C+w_D−d_sep}`, minimum `2^{2−6}=1/16` | `ratio_route ≤ 16 × (pointwise agreement)`.  **Max amplification is exactly `16.0`, attained at `(1,1,6)` — which is precisely where the green run reports its `ratio_route` maximum.**  See R4-O2 |
| **V9** | reliance audit (obligation 5) | parsed `claims/CLAIMS.md` for every id the shard cites | `S2-2body` **PROVED**, `ML2` **PROVED**, `ML3/ML6` named only as CONJECTURE, `ML1` named only as open.  `grep` finds **no** `ML4`, **no** `ML5`, **no** bare `S2` (the REFUTED row), **no** `𝒮_W`, and two explicit disclaimers that no Bethe/integrability hypothesis enters.  **Clean** |
| **V10** | downstream blast radius of the downgrade | `grep -rn "AC-EX-2M\|ACE2M-LSZ\|ACE2M-SR" --include=*.md` outside the shard/verdicts/briefs | only `HANDOFF.md` and `soft-index-adjudication-r1.md` (as an aspiration).  **No corpus shard consumes AC-EX-2M yet**, so the downgrade breaks nothing downstream |

---

## 2. FATAL

None.  Fourth consecutive round with none.

---

## 3. MAJOR

### R4-O1 (MAJOR) — the downgrade is announced six times and disobeyed once: `⟨1⟩9.⟨2⟩5`, the sole D6 instance of `(ACE2M-SR)`, still identifies the D29 datum with `S_phys` and justifies it by the quarantined port

**(a) Location.**
`theory/ansatz-scattering-2m.md` `⟨1⟩9.⟨2⟩5` — its **PROVE** line ("The
`j`-independent infinite-chain **datum** is `C¹` at `ε=0` …"), its display
("For the exact D7 multiplier, the packet-amputated datum is
`A(ε)(h)=∫dμ_f(u) S_phys(εu,h)`"), and above all its **Justification leaf**
("*Claims S2-2body and ML2, D24(b), and the exact-match computations
`⟨1⟩7.⟨2⟩3` and **`⟨1⟩8.⟨2⟩1--⟨2⟩2`***").  Consumers of that leaf:
`⟨1⟩1(A2M.3)` tail ("only its exhaustion-free, infinite-chain version is
verified on D6--D8"); §8 **Conditional** ("ML2/S2-2body verify only its
`j`-independent infinite-chain version"); and the **merged** `claims/CLAIMS.md`
l.77 ("*D6 verifies only the exhaustion-free infinite-chain first jet*").
Also `⟨1⟩9`'s own section heading, "**Constructed-channel** limit points".

**(b) My computation.**  Four parts.

*(i) `⟨2⟩5`'s object is the D29 datum, not the constructed-channel datum.*
`(ACE2M-SR)` is defined two steps earlier on
`A_j(ε):=lim_{t→±∞}lim_{N→∞}𝒜_{N,W_j,σ_j,t}(ε)`, and `𝒜` is fixed by
interface clauses 1 and 3 as **the D29 datum** — which clause 1 now says, in
the same breath, is the *fixed-time* insertion `Q[f̂_ε;ξ^-]ψ`.  `⟨2⟩5`'s PROVE
says "the `j`-independent infinite-chain **datum**", i.e. `A_j` at `W=ℤ`.  So
the object whose `C¹` property is being verified is the adjudicated D29 datum.

*(ii) What `⟨2⟩5` actually computes is the constructed-channel datum.*
`A(ε)(h)=∫dμ_f(u)S_phys(εu,h)` is, by (A2M.2), exactly the packet-averaged
matrix element of `W_+^*W_-`.  Writing the D29 datum as that object **is** the
channel identification — the one thing the shard declares **OPEN** at ll.13,
63, 396, 443, 512, 562, 778, 793 and in the merged row.  The Justification
leaf makes this explicit rather than accidental: it cites `⟨1⟩8.⟨2⟩2`, i.e.
`(ACE2M-LSZ)`, as one of the "exact-match computations" — and `⟨1⟩8.⟨2⟩2`'s
own tail says, 30 lines earlier, "**This theorem does NOT apply to the
adjudicated D29.**"  The step therefore stands on a theorem the same file
declares inapplicable to the object the step is about.  **`⟨2⟩5` silently
assumes precisely the branch-(i) conclusion the prover declined to prove.**

*(iii) The gap is not a technicality — it is at the same order as the
conclusion.*  On D6, R8 gives exactly
`Q_{k_s}|k_h⟩−|B^{in}⟩=(1−S_{12})|P_{12}⟩`.  I recomputed the S-matrix from
scratch (V3): `1−S_{12}=−2ik_s+O(k_s²)`, and the *relative* size of the
mismatch (V4) is `√2·k_s(1+O(k_s))` — `1.5487e−01` at `k_s=0.1`,
`1.4272e−02` at `k_s=0.01`, `1.4155e−03` at `k_s=0.001`.  `⟨2⟩5`'s entire
conclusion is the coefficient of `ε¹`.  So the two families agree at `ε=0`
and are **not shown to agree at the order `⟨2⟩5` reports**.  (They may still
agree there — R19 fixes the mismatch's own leading phase — but that is a
theorem nobody has displayed, and displaying it *is* branch (i).)

*(iv) Why MAJOR and not MINOR.*  Three reasons, each independently
sufficient under this protocol.
(1) `briefs/s2-repair-r3.md` closes its MAJOR section with a binding line:
"*Either way: `(A2M.3)`'s channel identification must not be **readable** as
available to Lane S1.*"  At `⟨2⟩5` it is not merely readable, it is *used*.
(2) The defect is now **in the DAG**.  The merged row asserts "D6 verifies
only the exhaustion-free infinite-chain first jet" without saying *for which
family*, and the only leaf backing that clause verifies it for the other one.
An orchestrator reading the row concludes `(ACE2M-SR)` has a verified D6
instance for the adjudicated D29.  It does not.
(3) It is the campaign's own first landmine in its hypothesis form —
`briefs/soft-index-target.md`: "*A constraint on limit points of a family with
NO limit points is empty … **Silence here is a MAJOR objection**.*"  Here the
non-emptiness certificate exists but certifies a different family.  My r4
brief anticipated exactly this: "*A downgrade that leaves one load-bearing
step unchanged is worse than none, because the row now advertises the fence.*"
`git diff` confirms the step is unchanged: the diff's hunks jump from
`@@ -520,13 +552,14 @@` (`⟨2⟩2`) to `@@ -595,14 +628,19 @@` (`⟨2⟩6`),
straddling `⟨2⟩5` without touching it.

*(v) Lockstep.*  §8's **Conditional** paragraph attributes the D6
verification to "ML2/S2-2body" alone, while the leaf's Justification also
names `⟨1⟩8.⟨2⟩1--⟨2⟩2`.  The HONEST STATUS paragraph therefore *understates*
the leaf's dependency, in the direction of concealment.  And `⟨1⟩9`'s heading
"Constructed-channel limit points" is a pre-downgrade label on a step that,
after the downgrade, produces limit points of an *unidentified* family.

**(c) FIX DEMAND.**  Do exactly one of:
**(A)** relabel — change `⟨2⟩5`'s PROVE to "*the `j`-independent
infinite-chain **constructed-channel** datum*", strike `⟨1⟩8.⟨2⟩1--⟨2⟩2` from
its Justification, and add one sentence: "*This exhibits a `(ACE2M-SR)`
instance for the constructed-channel family only; on the adjudicated
fixed-time D29 family the datum differs by the (R8) branch term
`(1−S_{12})|P_{12}⟩=−2ik_s|P_{12}⟩+O(k_s²)`, so no D29 instance of
`(ACE2M-SR)` is exhibited.*"  Then propagate to `⟨1⟩1(3)`, §8 **Conditional**
and the merged row (replacement text in §9 below).
**(B)** or prove, at `O(k_s)` and with a displayed uniform remainder, that the
`T→∞` D29 readout's packet-amputated datum equals `∫dμ_f S_phys(εu,·)+O(ε²)`
— which is branch (i) restricted to the first jet, and would also close
R3-O1 outright.
Do **not** leave the leaf as it is; and rename `⟨1⟩9`'s heading to
"Diagonal limit points and the separately scoped HR theorem".

**(d) SURVIVING WEAKER STATEMENT.**  The Taylor mathematics is correct and
I reproduced it (V5): *for the constructed-channel packet-amputated datum
`A(ε)(h)=∫dμ_f(u)S_phys(εu,h)` on D6--D8 with `‖f‖_2=1`, one has
`A∈C¹([0,ε_★];L²(I))` with `A(ε)=A(0)+εm_1∂_{k_s}S_phys(0,·)+O_{L²(I)}(ε²)`,
`m_1=∫u\,dμ_f`, and no hidden `ε^{-1}`; a one-element family is trivially
relatively compact with an equicontinuous first jet.*  What does **not**
survive is the sentence "D6 verifies …" read of the adjudicated D29 family:
`(ACE2M-SR)` currently has **no exhibited instance for the object it
constrains**.  Everything else in the downgrade — the six quarantine
sentences, the byte-for-byte row, `(ACE2M-LSZ)` as a theorem about HR
families, the diagonal compactness — stands untouched by this objection.

---

## 4. Checker audit (obligations 4 + the 2026-08-29 standing obligations)

Runs under `python3 -O` from the repository root, on the committed file.

### 4.1 Exit **path**, not just exit code

| run | printed decisive line | gates fired | exit |
|---|---|---|---|
| green | `C1a direct=3.354e-15 route=3.243e-15 ratio=5.605e-10`; `C1b agreement=1.128e-16 max_ratio=0.049383@(1,1,2) ratio_route=1.187e-15@(1,1,6) monotonicity_excess=-6.503e-03@(1,2,6)`; `PASS` | — | **0** |
| `--red-c1a` | `RED-OK: C1a route value error 1.000000e+00 \| C1a ratio error 2.400000e+00` | **G2, G3** | **1** |
| `--red-c1b` | `RED-OK: C1b cap 1.404664 at (3,2,2) \| C1b support monotonicity excess 6.145405e-01 at (3,2,2)` | **G5, G7** | **1** |
| `--red-supportfold` | `RED-OK: C1b ratio-route disagreement 1.646091e-02 at (2,2,2)` | **G6 alone** | **1** |

Zero bare `assert` (`grep -c '^\s*assert\b'` → 0); green also exits 0 without
`-O`.  **`violations()` evaluates all seven gates unconditionally and returns
a list — there is no early exit, so no gate is ever masked by an earlier
one.**  That is a genuine design strength and I fence it.

### 4.2 Gate enumeration and red-mode coverage (new standing obligation)

G1 `C1a direct value>1e-12` · G2 `C1a route value>1e-12` · G3 `C1a ratio>1e-8`
· G4 `C1b agreement>1e-12` · G5 `C1b cap>0.1` · G6 `C1b ratio_route>1e-12` ·
G7 `C1b monotonicity excess>1e-12`.

- Covered by a registered red mode: **G2, G3, G5, G6, G7**.
- **Not reached by any registered red mode: G1 and G4** → R4-O3.
- Red-mode **specificity**: the three modes produce three *disjoint* violation
  sets; no two are bit-identical in effect. ✔

### 4.3 Mutation battery, on copies in a temp dir (never in place)

| mutant | what it breaks | result |
|---|---|---|
| `m1` — fold `w_Cw_D` into the **constant** in both routes (r3's exact mutation) | the defect A2M-C1b was once advertised to exclude | **exit 0, PASSES**; `ratio_route=1.187e-15` **bit-identical to green** |
| `m2` — multiply **both** ratios by `w_Cw_D` | same, other sign | **exit 0, PASSES**; `ratio_route` again bit-identical to green |
| `m3` — **ground truth falsified**: `expected += 1e-6` | is the acceptance test self-fulfilling? | **exit 2**, `C1a direct 1.000000e-06 \| C1a route 1.000000e-06`.  **Not self-fulfilling** ✔ |
| `m4` — `A^a=σ_a/√3 → σ_a/2` | wrong tensor normalization | exit 2 (`C1a 5.39e-01`, `C1b cap 7.399`) |
| `m5` — `RIGHT_FIXED → diag(0.6,0.4)` | wrong transfer fixed point | exit 2 (`C1a 1.96e-01`, `C1b cap 2.429`) |
| `m6` — `C=I+2S^z` | wrong observable | exit 2 (`C1a 1.333e+00`) |
| `m7,m8,m9` — **absurd inputs** `λ̃=3.7, −5.0, 1e6` | does anything move? | **all exit 0, PASS** → R4-O4 |
| `m10` — `λ̃=0.34` (just above `λ_E=1/3`) | the cap in the direction that matters | **exit 2**, `C1b cap 0.106797 > 0.1`.  The cap is live, but only at `λ̃=1/2` |
| `m11` — make the two C1b routes the **same expression** | the campaign's pattern-#1 defect | **exit 0, PASS**, with `agreement=0.000e+00` **and** `ratio_route=0.000e+00` → R4-N7 |
| `m12` — `block_operator_norm → 1.0` | do the norms matter? | exit 2 (`C1b cap 0.197531`) |
| `m13` — drop the fixed-point subtraction in C1b only | G4's live-ness | exit 2, `C1b agreement 1.000e+00 \| cap 15.99 \| ratio_route 15.98` — **G4 demonstrably can fail** |
| `m15` — add `5e-13` to `fixed_connected` | can G6 ever fire when G4 does not? | **exit 2 on G6 alone** (`agreement=5.000e-13` passes, `ratio_route=7.999e-12` fires).  This is G6's *entire* non-subsumed domain |
| `m16` — add `5e-15` (control) | | exit 0 ✔ |

---

## 5. MINOR

### R4-O2 (MINOR) — `ratio_route` is the r3 gate **renamed**, not replaced; it is subsumed by the agreement gate up to a fixed factor 16, and `--red-supportfold` is a self-fulfilling mutant

**(a)** `theory/checks/ansatz_scattering_2m_check.py` `check_c1b`, the
`ratio_route_location, ratio_route_error = max(…abs(ratio - direct_ratios[location])…)`
block and the `if red_supportfold: ratio *= width_c*width_d` line; §6's
sentence "*This profile gate merely re-tests contraction-route agreement in
ratio units*"; `claims/CLAIMS.md` l.77 where-tested cell, "*the
**profile-agreement gate** is a rescaled duplicate …*".

**(b)** Three findings.
*(i) It is the same code.*  `git diff cf2e443..HEAD` shows the gate expression
unchanged; only the identifiers `support_profile_error/location` became
`ratio_route_error/location` and the printed label changed.  My two-sided
folds `m1` and `m2` both exit **0** with `ratio_route` **bit-identical to the
unmutated green value** `1.187e-15`.  The r3 defect is present, verbatim.
*(ii) Deductive subsumption, quantified.*  Both routes share the denominator
`‖C_{w_C}‖‖D_{w_D}‖λ̃^{d_sep} = 2^{w_C+w_D−d_sep}`, whose minimum over the
27-point grid is `2^{2−6}=1/16` (V8).  Since `||F|−|D|| ≤ |F−D|`,
`ratio_route ≤ 16 × agreement`.  With `BLOCK_TOL=1e-12` for **both** gates,
G6 can fire while G4 passes only when the pointwise agreement lies in
`(6.25e−14, 1e−12]` — a 16× window entirely inside float noise.  I built the
one witness (`m15`) and it works, so G6 is *strictly* stronger than G4 — by a
bounded factor of 16 and by nothing else.  **G6 is a tolerance-tightening of
G4, not an independent test of any mathematical property.**
*(iii) The registered mutant is self-fulfilling.*  `--red-supportfold`
multiplies `ratio` and not `direct_ratio`, *after* `agreement_error` has
already been recorded — it mutates one of the two quantities the gate
compares, downstream of every other gate.  It is the only registered mutant
G6 catches, and G6 is the only gate that catches it.  The pair certifies the
checker's own arithmetic, not the AKLT clustering claim.
*(iv) Nomenclature drift.*  The code prints `ratio_route`; §6 says "profile
gate"; the merged row says "profile-agreement gate".  The row now names a
gate that no longer exists under that name.

**(c) FIX DEMAND.**  Either (α) build the gate the name implies — extend
`w_C,w_D` to `{1,…,6}`, gate on `max_w ratio(w,w,d)/ratio(1,1,d) ≤ 1+tol`,
and register a red mode that folds `w_Cw_D` into the **certified constant in
both routes**, which must then fail — or (β) keep the retraction and finish
it: rename the §6 and `claims/CLAIMS.md` prose to "`ratio_route` gate", and
add one clause, "*it is the agreement gate rescaled, and can fire on its own
only for pointwise agreement in `(6.25e−14, 1e−12]`*".

**(d) SURVIVING WEAKER STATEMENT.**  A2M-C1b still certifies, on AKLT: the
two contraction routes agree to `1.13e−16` at all 27 grid points; the
normalized connected ratio is `≤0.049383 < 0.1` uniformly over
`w_C,w_D∈{1,2,3}`, `d_sep∈{2,4,6}` at `λ̃=1/2`; and it is **strictly**
decreasing in the support lengths at every `d_sep` (margin `−6.503e−03`,
killed by `--red-c1b` at `+6.145e−01`).  Support-length independence of
`C_{A,λ̃}` is *proved analytically* at `⟨1⟩3.⟨2⟩2` (V6) and needs no
certificate; §6 now says exactly that, which is the right resolution.

### R4-O3 (MINOR) — two of the seven gates have no registered red mode

**(a)** `theory/checks/ansatz_scattering_2m_check.py` `violations()`: the
`direct_error > VALUE_TOL` branch (G1) and the
`c1b.agreement_error > BLOCK_TOL` branch (G4); §6 registers only three reds.

**(b)** Exit-path table §4.1: `--red-c1a` fires G2+G3, `--red-c1b` fires
G5+G7, `--red-supportfold` fires G6.  G1 and G4 are never reached.  I showed
both are live rather than decoration — G1 by `m3` (`expected += 1e-6` →
`C1a direct value error 1.000000e-06`) and G4 by `m13` (drop the C1b
fixed-point subtraction → `C1b contraction disagreement 1.000000e+00`) — but
the artifact ships no evidence of that.  The new protocol clause ("*A gate
with no red mode is decoration … report any gate that no mutation reaches*")
bites here.

**(c) FIX DEMAND.**  Register two more modes in §6 and in code:
`--red-truth` (shift `expected` by `1e-6`; must fail the C1a direct and route
value gates) and `--red-c1b-sub` (drop `- fixed_projection(right)` in
`check_c1b`; must fail the C1b agreement gate).  Both must exit 1.

**(d) SURVIVING WEAKER STATEMENT.**  Both gates are live — I have exhibited
the mutants — so the checker is *not* carrying decoration; it is carrying two
gates whose live-ness is documented only in this verdict.

### R4-O4 (MINOR) — `λ̃` is an unguarded constant: absurd values pass green, and the `0.1` cap is a `λ̃=1/2` statement that fails already at `λ̃=0.34`

**(a)** `LAMBDA_TILDE = 0.5` (module constant) and the `BLOCK_CAP = 0.1`
gate; §6 A2M-C1b, "with `λ̃=1/2`, require `max … ≤0.1`"; §6 **Uncertified
scope**; `⟨1⟩3`'s "**For every** `λ̃∈(λ_E,1)` there is `C_{A,λ̃}<∞`".

**(b)** Per the standing obligation I fed the checker absurd inputs.
`λ̃=3.7` → green, exit 0 (`max_ratio 0.000902`); `λ̃=−5.0` → green, exit 0
(`0.000494`); `λ̃=1e6` → green, exit 0 (`max_ratio 0.000000`,
`monotonicity_excess −1.016e−40`).  Nothing moves the verdict, because every
`λ̃` above `1/2` only *loosens* the cap and the monotonicity margin, and the
checker never tests that `λ̃∈(λ_E,1)` — indeed a **negative** `λ̃` is
accepted.  In the direction that matters the gate is live and tight:
`λ̃=0.34` (just above `λ_E=1/3`) gives `C1b cap 0.106797 > 0.1`, exit 2.  So
the certified statement is "at `λ̃=1/2` the normalized ratio is `≤0.1`", not
`⟨1⟩3`'s "for every `λ̃∈(λ_E,1)`" — and the margin to failure is a factor
`≈1.47` in `λ̃`, not a decade.

**(c) FIX DEMAND.**  Add a one-line guard `if not (1/3 < LAMBDA_TILDE < 1):
fail(...)`, and add to §6 **Uncertified scope**: "*the cap `0.1` is a
`λ̃=1/2` statement; `C_{A,λ̃}` diverges as `λ̃↓λ_E=1/3` and the same cap
already fails at `λ̃=0.34`.  Nothing here certifies `⟨1⟩3`'s `for every
λ̃∈(λ_E,1)` quantifier.*"

**(d) SURVIVING WEAKER STATEMENT.**  At `λ̃=1/2` on AKLT the cap, the
monotonicity and the route agreement all hold as printed, and the cap is
demonstrably not vacuous (it fails under `m10` and `m12`).  `⟨1⟩3`'s uniform-
in-`λ̃` statement is proved analytically and is simply not what C1b tests.

### R4-O5 (MINOR) — pre-downgrade framing survives in `⟨1⟩9`'s heading and ASSUME

**(a)** `### ⟨1⟩9. Constructed-channel limit points`; and `⟨1⟩9`'s
"**ASSUME.** D31 and **the D29 interface block**".

**(b)** After the downgrade `⟨1⟩9.⟨2⟩1` produces limit points of an
*unidentified* family and `⟨2⟩2` is about a different family, so the heading
names a conclusion the step no longer reaches.  Worse, `⟨1⟩8` clause 5 is now
headed "*Separate asymptotic-HR theorem; **not a D29 clause***" while still
living inside a block whose section heading is "The **sole D29 interface
block**" and which `⟨1⟩9` imports wholesale as "the D29 interface block".  A
reader importing "the D29 interface block" imports a clause the shard says is
not part of D29 — the exact ambiguity the downgrade exists to remove.

**(c) FIX DEMAND.**  Retitle `⟨1⟩9` "Diagonal limit points and the separately
scoped HR theorem"; retitle `⟨1⟩8` "The D29 interface block and the separate
HR hypotheses"; change `⟨1⟩9`'s ASSUME to "D31, adjudicated D29 interface
clauses 1--4, and (for `⟨2⟩2` only) the separate HR hypotheses of clause 5".

**(d)** Purely nominal: every substantive statement in `⟨1⟩9` is already
correctly scoped in its own body.  Three headings and one ASSUME line.

### R4-O6 (MINOR) — statement and proof disagree about who owns (2M-1P)

**(a)** §0 PROVE preamble ("*Clause 5 and (2M-1P) instead state the hypotheses
of the separate creator-choice theorem; **they are not properties of the
adjudicated D29**.*") and `⟨1⟩8` clause 5(b) ("*is not a property asserted of
the adjudicated fixed-time D29 insertion*") versus `⟨1⟩8.⟨2⟩1`, whose proof
**begins** `Q[f̂_ε;ξ^-]Ω=Σ_x f̂_ε(x)S_x^-Ω=Γ_M(f_ε⊗e_1)=a_{2,1}[f_ε]Ω`.

**(b)** `⟨2⟩1` derives (2M-1P) *from* the adjudicated fixed-time charge
operator applied to the vacuum, then transports it through the filter (source
transparency, verified above) and the HR evolutions.  So (2M-1P) is a
**consequence** of the adjudicated D29's charge on the vacuum — it is the one
place where the adjudicated object and the HR family provably coincide, and
it is precisely why the HR family is non-empty on D6.  Saying it is "not a
property of the adjudicated D29" is therefore too strong, and it obscures the
correct distinction: what fails for the adjudicated D29 is not (2M-1P) but
*being an HR creator family at all* — which is a statement about the
`t`-dependence, not about the vacuum vector.

**(c) FIX DEMAND.**  Replace both phrases with: "*(2M-1P) is proved on D6 for
the HR family built from the adjudicated charge (`⟨1⟩8.⟨2⟩1`); what the
adjudicated D29 fails is not (2M-1P) but HR admissibility itself — it applies
`Q[f̂_ε;ξ^-]` at fixed time to an already prepared hard vector and never free-
evolves its profile.*"

**(d)** The quarantine is unaffected: it rests on HR *admissibility*, not on
(2M-1P), and R3-O1's argument (D29-B has the interacting forward evolution but
not the free backward packet evolution) is untouched.

---

## 6. NOTE

**R4-N1 — the byte-for-byte lockstep claim is TRUE.**  `cmp` on the two
extracted lines: identical, 3408 bytes each.  And the merged statement cell is
the r3 §9 blockquote verbatim modulo two mandatory markdown pipe-escapes.
Nothing was added, softened or strengthened.  This is the cleanest lockstep
result in four rounds and it deserves to be said.

**R4-N2 — R3-N2's new margin reproduces from a different basis.**
`monotonicity_excess = −6.5030737e−03 @ (1,2,6)` with the baseline excluded;
exactly `0.0 @ (1,1,2)` with it included.  The old printed value carried zero
information; the new one carries a real margin.

**R4-N3 — the two-sided fold still passes, and the prover said so first.**
`m1`/`m2` exit 0.  The r3-response's own "Checker verification" section
states this ("*Green still exited 0 … This reproduces R3-O2's criticism and is
why the former certificate claim is retracted rather than softened*").  A
prover volunteering the mutation that defeats its own gate is the method
working; I record it as such.

**R4-N4 — the acceptance test is not self-fulfilling.**  `m3` shifts the
closed-form ground truth by `1e-6` and the checker dies at exit 2.  The `4/3
(-1/3)^d` target is computed independently of both contraction routes.

**R4-N5 — no reachability hole.**  `violations()` collects all seven gate
results before returning; no gate can be masked by an earlier failure.  Fence
this pattern; it is what let me report an exit *path* at all.

**R4-N6 — the three red modes are mutually specific.**  Their violation sets
are `{G2,G3}`, `{G5,G7}`, `{G6}` — pairwise disjoint, none bit-identical.

**R4-N7 — the campaign's pattern-#1 defect would still be invisible here.**
`m11` collapses `direct_connected` into the fixed-point-subtracted expression;
the run stays green and prints `agreement=0.000e+00` **and**
`ratio_route=0.000e+00`.  The current code does **not** have that defect (the
routes are genuinely different, and `m13` proves the subtraction is load-
bearing), but nothing guards against a future edit introducing it, and the two
gates that would have to catch it both report exactly `0.0` by construction
when it happens.  A cheap guard: assert the two route expressions differ by
recomputing one of them with a deliberately perturbed intermediate.

**R4-N8 — L3 citation discipline stays clean.**  The one new source citation
(filter transparency) is quoted correctly from
`refs/arxiv-1412.2970/Scattering_spin-AHP1.tex` l.1379, inside the proof of
`\bet\label{Haag-Ruelle-Fock}`.  No from-memory citation anywhere in the diff.

**R4-N9 — the `(creation-on-vacuum)` hypothesis audit is exactly right.**  I
read the derivation (ll.1138–1147): the only thing it needs is
`B^*Ω = P(𝔥)B^*Ω`.  The shard's added sentence — "`S_x^-Ω` nevertheless has
spectral support entirely in `𝔥`, which is the condition needed by
`(creation-on-vacuum)`" — is the correct reading, and D6 satisfies it because
`S_x^-Ω=|x⟩` lies in the `S^z`-charge-one sector where the band is the entire
spectrum.

**R4-N10 — §6's new "proved analytically in `⟨1⟩3`" is a true addition.**  It
goes beyond the r3 FIX DEMAND's wording, but V6 shows `⟨1⟩3.⟨2⟩2`'s bounding
factor `‖E^{d_sep}−P‖_{1→1}` contains no `C`,`D` dependence whatever, so
support-length independence is trivial there.  This is the *right* resolution
of r1-O6/r2-O8/r3-O2: the property was never a numerical question.

**R4-N11 — the downgrade has zero downstream blast radius.**  No shard under
`theory/` cites `AC-EX-2M`, `(ACE2M-LSZ)` or `(ACE2M-SR)`; only `HANDOFF.md`
and the S1 adjudication (as an aspiration).  Merging the weakened row costs
the corpus nothing.

**R4-N12 — §§1–3 and the frozen checkers are untouched.**  Zero diff hunks
between shard lines 65 and 370; `theory/checks/` gained edits only to this
lane's file (the `d24d3_normalization_check.py` change belongs to the D24(d)3
lane in the same orchestrator commit).

**R4-N13 — the only exhibited `(SR)` instance is a one-element family.**
Even after R4-O1 is repaired, `⟨1⟩9.⟨2⟩5` exhibits a *singleton*, for which
every uniformity clause of `(SR)` — the `j`-uniform relative compactness and
the `j`-uniform equicontinuity of `∂_εA_j` — is trivially true.  §8 discloses
this ("`(W,σ)`-uniform control is open even on D6") but the merged row does
not say "one-element".  Worth one clause when R4-O1's replacement lands.

---

## 7. VERIFIED CORRECT — fenced, do not churn

New this round (r3's §7 fence remains in force and was not re-litigated):

- **Byte-for-byte lockstep** of the shard §7 `AC-EX-2M` row with
  `claims/CLAIMS.md` l.77 (`cmp`, 3408 bytes each), and of that row's
  statement cell with the r3 §9 scoping sentence (V1, V2).
- **The quarantine, everywhere it was written**: proposer status, `⟨1⟩1(3)`,
  `⟨1⟩8` clauses 1 and 5, `⟨1⟩8.⟨2⟩2`'s tail, `⟨1⟩9.⟨2⟩2`, `⟨1⟩9.⟨2⟩6–⟨2⟩7`,
  `⟨1⟩10.⟨2⟩3`, the notation rows, §8 — nine sites, all correctly scoped, all
  at the same strength.  Only `⟨1⟩9.⟨2⟩5` is out of step (R4-O1).
- **`⟨1⟩8.⟨2⟩1` as repaired** — the filter-transparency line, the `b=1`
  binding, and the `S^z`-sector relativization paragraph.  Citation verified
  verbatim in the local TeX; the `(creation-on-vacuum)` requirement verified
  by reading its derivation (R3-O5, R3-O6 rows; R4-N9).
- **Clause 3 as re-quantified** and clause 4's "conditional only on
  `(D29-den)`" (R3-O3, R3-O4).
- **`⟨1⟩3.⟨2⟩2`'s support-length independence** (V6) — fourth independent
  survival; and the new §6 cross-reference to it is true.
- **(R8)+(R19)** reproduced from scratch: `1−S_{12}=−2ik_s+O(k_s²)`,
  `∂_{k_s}δ|_0 = 2.000000000` at every `k_h` (V3).
- **`⟨1⟩9.⟨2⟩5`'s Taylor arithmetic** (V5) — `O(ε²)` remainder with constant
  `≈10.1`, no hidden `ε^{-1}`.  *The computation is fenced; its licensing is
  R4-O1.*
- **A2M-C1a** end-to-end, including that its ground truth is falsifiable
  (`m3`) and that the `1e-8` ratio tolerance is necessary (my basis fails
  `1e-12` from `d=8`).
- **A2M-C1b's monotonicity gate**, now reporting a real margin
  (`−6.503e−03@(1,2,6)`), independently reproduced.
- **Checker hygiene**: zero bare `assert`, green exits 0 with and without
  `-O`, all three reds exit 1, no early exit in `violations()`, three red
  modes mutually specific.
- **Reliance audit** (V9): no REFUTED row, no `ML4-Ward`, no `ML5`, no bare
  `S2`, no `𝒮_W`, no Bethe.

---

## 8. Register comparison against the nearest PROVED rows

The nearest sibling is **`AC-EX`** (`claims/CLAIMS.md`), this lane's own
predecessor and a *conditional* PROVED row; the nearest adjudicated conditional
with a named interface hypothesis is **`M-INDEX-spec`** (r3's choice).

| item | `AC-EX` / `M-INDEX-spec` register | `AC-EX-2M` r4 | verdict |
|---|---|---|---|
| the *inapplicable* neighbour named inside the row | `M-INDEX-spec`: "*its unconditional existence is **REFUTED** (M-INDEX-LA-strong)*" | "**This theorem does NOT apply to the adjudicated D29**" + the displayed `−2ik_s\|P_{12}⟩` obstruction | **r3's BREACH is CLOSED** |
| conditionality named at the point of statement | "*Proved **only** as the conditional implication*" | "*conditional only on `(D29-den)`*"; "*conditional on `(ACE2M-SR)`*" | **in register** |
| assumed hypotheses flagged as assumed | "*D27 is **assumed, not derived***" | "*Both displayed inequalities are assumptions*" | **in register** |
| **the load-bearing hypothesis's instantiation status** | `AC-EX`: "*(D28-C) is the load-bearing hypothesis and **is unverified on any model***"; and its quantifier carries the caveat inline — "*for a normalized event vector … **for which Lane T1's outcome measure exists***" | "*D6 verifies only the exhaustion-free infinite-chain first jet*" — silent on **which family**, and the backing leaf verifies the other one | **BREACH → R4-O1** |
| checker caveat carried into the row | — | present, and honest, but names a gate (`profile-agreement`) the code no longer has | minor breach → R4-O2(iv) |

`AC-EX` is the exact template and it is scrupulous on precisely the axis
`AC-EX-2M` now slips on: it says outright that its load-bearing hypothesis has
no verified instance, and it writes the nonvacuity caveat into the quantifier
rather than into a footnote.  §9's replacement clause applies that template.

---

## 9. PROMOTE / HOLD (deliverable)

### `(A2M.3)`'s interface clause — **HOLD** (unchanged from r3)

**Missing step, named — now two.**
(1) *Unchanged from r3:* branch (i) — prove that the `T→∞` D29-B readout of
the fixed-time charge-created state `Q[f_ε]ψ_{g,σ}` has the same connected
on-shell pairing as the HR asymptotic leg, **at `O(k_s)`**, since (R8)+(R19)
give the exact mismatch `−2ik_s|P_{12}⟩+O(k_s²)` there (V3, V4).
(2) *New this round:* `(ACE2M-SR)` must be given an instance for the family it
constrains.  The only exhibited instance (`⟨1⟩9.⟨2⟩5`) is for the
constructed-channel family, and it is a one-element family besides (R4-N13).
Until (1) or a direct D6 computation of the fixed-time datum's first jet
lands, `(ACE2M-SR)` is a hypothesis with **no verified D29 instance** and the
`C¹` first-jet conclusion must not be read as instantiated for Lane S1.

### `AC-EX-2M` as a whole — **HOLD at SKETCH**, with the clause below applied verbatim

Rationale.  This is a *good* round: 12/15 dispositions verified fixed, the
lockstep claim is literally true, the HR theorem survives intact with its
hypotheses owned, the checker's false advertisement was **retracted by the
prover before I got there**, and the reliance audit is clean for the fourth
time.  But the row cannot move up while one leaf still consumes the
identification the row fences, because the row's own "D6 verifies…" clause is
the sentence that leaf is supposed to back.  The fix is one relabel and one
sentence; the row should stay at SKETCH for one more round and then move.

**Exact replacement — in `claims/CLAIMS.md` l.77 (and, by the lockstep
obligation, in the shard's §7 row), replace the single sentence**

> First-jet compactness is conditional on `(ACE2M-SR)`, including existence of the `N,t` limits; its full `(W,σ)`-uniform version is open on every model, and D6 verifies only the exhaustion-free infinite-chain first jet.

**by, verbatim, no paraphrase:**

> First-jet compactness is conditional on `(ACE2M-SR)`, including existence of the `N,t` limits; its full `(W,σ)`-uniform version is open on every model.  The only exhibited instance of `(ACE2M-SR)` is the exhaustion-free infinite-chain first jet of the **constructed-channel** packet-amputated datum `A(ε)(h)=∫dμ_f(u)S_phys(εu,h)` on D6 (⟨1⟩9.⟨2⟩5), a one-element family for which every uniformity clause of `(SR)` is trivially satisfied; **no instance is exhibited for the adjudicated fixed-time D29 family**, from which that datum differs at relative order `ε` by the (R8) branch term `(1−S_{12})\|P_{12}⟩=−2ik_s\|P_{12}⟩+O(k_s²)`.  `(ACE2M-SR)` is therefore a hypothesis with no verified D29 instance.

(Everything else in the row — status `SKETCH`, depends-on, where-proved,
where-tested — stays exactly as merged, except that the where-tested caveat's
phrase "the profile-agreement gate" should read "the `ratio_route` gate
(formerly `profile-agreement`)" per R4-O2(iv).)

**What would move the row to PROVED (conditional).**  Two independent paths,
either of which I would accept next round:
- **Narrow:** apply the clause above, execute R4-O1's fix (A), and close the
  five MINORs.  That yields a row whose every clause has a leaf that actually
  backs it — PROVED (conditional on D31 and (D29-den)), in `AC-EX`'s register.
- **Better, and I recommend it:** **split the row.**  `(A2M.1)`--`(A2M.2)` —
  fixed-packet Cook existence, isometry, translation intertwining, bound/
  inelastic separation, the ML2/D7 match on D6--D8, and D31-C2/C4 derived from
  D1 — have now survived **four** hostile rounds with 0 FATAL, are
  independently reproduced (D31-C2 four times, the checker twice from
  different tensors), and depend on **nothing** in the D29 interface.  They
  deserve their own row at PROVED (conditional on D31), leaving a separate
  `AC-EX-2M-D29` row at SKETCH for the interface.  Keeping the strongest
  proved content in this campaign hostage to an open interface clause is the
  only reason this theorem is still at SKETCH.

---

## 10. Summary and trajectory

- **FATAL 0** (0 in r1, r2, r3, r4)
- **MAJOR 1** — R4-O1 (the downgrade is announced six times and disobeyed at
  `⟨1⟩9.⟨2⟩5`)
- **MINOR 5** — R4-O2 … R4-O6
- **NOTE 13** — R4-N1 … R4-N13

**Trajectory: 6 → 2 → 1 → 1 MAJOR, 0 FATAL throughout.  Severity is NOT
falling this round; it is flat.**  I will not dress that up.  What I will say,
because it is also true and measurable:

- The r4 MAJOR is **strictly narrower** than the r3 MAJOR.  R3-O1 indicted an
  interface clause, a theorem statement, a HONEST STATUS paragraph and a merge
  row simultaneously.  R4-O1 indicts **one leaf and its three echoes**, and
  its fix is a relabel plus one sentence — the surviving weaker statement
  (V5) is the same mathematics, correctly addressed.
- **Nothing regressed and nothing was re-overclaimed.**  Twelve of fifteen
  dispositions verified fixed by fresh recomputation; the lockstep claim is
  literally true to the byte; §§1–3 untouched; the fenced list not churned.
- The prover **volunteered** the mutation that defeats its own gate and
  retracted the claim rather than softening it (R4-N3).  That is the single
  most encouraging thing in this diff, and it is the behaviour the four
  shipped no-op gates in this corpus were supposed to teach.
- The one MAJOR is, once again, not new ambition: it is a step the repair
  *forgot to revisit* after the ground under it moved.  A fifth round that
  applies §9's clause and R4-O1's fix (A) reaches 0 MAJOR, and I would
  promote.

**FAIL(R4-O1)**
