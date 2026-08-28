<!-- ROLE: r3 ADJUDICATION verdict on theory/ansatz-scattering-2m.md
     (Theorem AC-EX-2M, Lane S2).  Priors: ansatz-scattering-2m-r1.md,
     -r2.md.  Work order: briefs/s2-critic-r3.md + briefs/critic-protocol.md.
     Writable lane: this file only. -->

# Critic verdict r3 — `theory/ansatz-scattering-2m.md` (Theorem AC-EX-2M, Lane S2)

Critic: Opus, adversarial, 2026-08-29.  **Adjudication round.**  Priors:
`theory/verdicts/ansatz-scattering-2m-r1.md` and `-r2.md` (mine).  Work order
audited: `briefs/s2-repair-r2.md`.  Claimed dispositions:
`theory/ansatz-scattering-2m-r2-response.md`.

Repair round audited: `git diff d5c8a10..HEAD -- theory/ansatz-scattering-2m.md`
(398 changed lines, landed across `3ab33cd` and `742c89c`) plus the new
`theory/checks/ansatz_scattering_2m_check.py` (288 lines, new file).  Reading
was scoped to the diff; §§1–3 of the shard (D31-C2, Cook, isometry, ML2/D7
match) were **not** re-litigated — they are fenced in §7 below.

All prototype computation in
`/tmp/claude-1000/.../scratchpad/{indep_c1.py,mut_*.py}`; no shared file
touched, no commit.

---

## 0. Disposition verification table (round obligation 1)

Every row verified by fresh recomputation or by reading the source TeX, not by
reading the response.

| id | claimed | **r3 verdict** | evidence |
|---|---|---|---|
| R2-O1 | FIXED | **PARTIALLY-FIXED** | The Haag–Ruelle port is real, faithful and correctly cited (V1, V2 below): the **vector→operator gap is genuinely closed** for asymptotic HR soft legs.  But the port's antecedent — interface clause 1's "the charge leg is an **asymptotic** HR leg … **not** the fixed-time action of a charge operator on an already prepared hard vector" — is **contradicted by the adjudicated D29** (`soft-index-adjudication-r1.md` §3.1 adopts S1-B's design; `soft-index-b.md` §M1: `Φ(0):=Q[f_ε]ψ_{g,σ}` … "the smeared broken charge itself — no other source is admitted").  The r2 FIX DEMAND was branch **(a) or (b)**; the shard took (a) and never checked whether (a)'s antecedent holds, and never supplied (b) for the D29 that does hold → **R3-O1 (MAJOR)** |
| R2-O2 | DOWNGRADED | **VERIFIED-FIXED** (with two residues) | (A2M.3) ⟨1⟩1(3) is now the full-index diagonal statement; ⟨1⟩9.⟨2⟩1 proves exactly that; the iterated inner limits are explicitly moved into `(ACE2M-SR)`; clause 3 restores "on the **selected hard packet**" and displays `ess inf|𝒟_α|≥d_I>0`, `sup‖𝒝_α‖≤C_I`, `sup‖𝒜_α‖≤C_I/d_I`.  I re-derived the last inequality: `|𝒜_α(h)|≤|𝒝_α(h)|/d_I` pointwise ⟹ `‖𝒜_α‖_{L²}≤C_I/d_I` — **correct**.  Row, HONEST STATUS and status line all say "diagonal".  Residues → **R3-O3, R3-O4** |
| R2-O3 (`ε_0` collision) | FIXED | **VERIFIED-FIXED** | `grep ε_0` → 5 sites, all declarative: `C_N=C_N(ε_v,s_N(F))` (l.251), "`ε_0` occurs in no Cook constant" (l.252), "used by no estimate in §§2--3" (l.106), D31(4) carries the same disclaimer (l.686), notation row present (l.716).  `(SR)`'s endpoint is `ε_★` at every occurrence (ll.493, 494, 535, 586).  No collision remains |
| R2-O4 ((D29-order)) | DOWNGRADED | **VERIFIED-FIXED** | clause 4 now reads `N→∞ ≺ t→±∞ ≺ (W↑ℤ,σ↓0)_j ≺ ε↓0` with the explicit disclaimer "not an asserted iterated `lim_σ lim_W`"; `(SR)` names the diagonal as the specialization |
| R2-O5 (dangling `ε`) | FIXED | **VERIFIED-FIXED** | "The data are defined for every fixed soft packet scale `ε>0` … For every sequence … with `ε_r↓0`".  `ε` bound once |
| R2-O6 (lockstep drifts) | FIXED | **VERIFIED-FIXED** | row now "lies in" (matches ⟨1⟩7.⟨2⟩4's "is a closed subspace of"); depends-on cell gains `D10, D24`; notation block gains rows for `ε_v,ε_0,s_N(F)`, `V_w,Ψ_O`, `f_ε,Q[f̂_ε;ξ^-],a_{2,b}[f_ε],a_{Q,2,b,t}`, `𝒜_α,𝒝_α,𝒟_α,d_I,C_I`, `A_j(ε),ε_★`.  `R_ε` is deleted, not orphaned |
| R2-O7 (checker spec) | FIXED | **VERIFIED-FIXED in code and text** | §6 restores "Both **connected** answers"; code computes `direct_connected = raw − ω(C)ω(D)` (`check_c1a`); ratio gate is explicit `|ratio+1/3|≤10^-8` in the spec and `RATIO_TOL=1.0e-8` in code.  My independent re-implementation confirms the tolerance is *necessary*: `1e-12` fails green from `d=8` in my basis (`d=7` in theirs) |
| R2-O8 (C1b saturated at `w=1`) | FIXED | **PARTIALLY-FIXED** | The **monotonicity** gate is real and is the substantive repair (`--red-c1b` fires it at `6.145e-01`).  The added **profile-agreement** gate is *not* what §6 says it is: my honest support-fold mutant passes every gate, exit 0 → **R3-O2 (MINOR)** |
| R2-O9 (undisplayed anchors) | FIXED | **VERIFIED-FIXED** (one undisplayed step remains) | ⟨1⟩9.⟨2⟩4 (D6 ⊨ D31) and ⟨1⟩9.⟨2⟩5 (smeared Taylor) both added; I re-derived both (V4, V5) — **correct**.  Residues → **R3-O5, R3-O6** |
| R2-O10 (`K`-chart) | FIXED | **VERIFIED-FIXED** | ⟨1⟩7.⟨2⟩3 now maps every torus pair to `K^♯∈(−π,π]`, `q^♯∈(0,π)`; I verified existence/uniqueness constructively (V6) |
| R2-O11 (`Q[·]` convention, `b`) | FIXED | **VERIFIED-FIXED** (cosmetic residue) | `Q[f̂_ε;ξ^-]` in D10(c)'s position convention throughout; `soft-current-recon.md` ⟨1⟩1 cited alongside D10(c); `b` bound on all three sides of (2M-1P).  `b` still dangles in the ⟨1⟩8.⟨2⟩1 display → folded into **R3-O6** |

**Nothing REGRESSED.**  Every r2 MINOR is closed at or below its surviving
ceiling.  The single MAJOR of this round is not a re-opening: it is the
consequence of the branch the prover chose for R2-O1.

---

## 1. What I independently recomputed (obligation: recompute, never referee)

| # | step | method | outcome |
|---|---|---|---|
| **V1** | the port's **citations**, against `refs/arxiv-1412.2970/Scattering_spin-AHP1.tex` (L3) | located every cited anchor by label: `\subsection{Scattering states and their Fock space structure}` (`\label{Scattering-states-existence}`, l.1283); `\bet\label{Haag-Ruelle}` (l.1291) and its final clause immediately after `\label{Asymptotic symmetry}` (l.1301); `\bel\label{commutators-decay}` (a) (l.1171); `\bel\label{HR-auxiliary}` (d) (l.1120); `\label{creation-on-vacuum}` (l.1138) inside `\subsection{Haag-Ruelle creation operators}` (l.1076) | **every citation is accurate**.  Source clause, verbatim: "*If `B̃*_{i,t}(g̃_i)Ω=B*_{i,t}(g_{i,t})Ω`, for all `i=1,…,n`, and `V(g̃_i)∩V(g_j)=∅` for all `i≠j`, then `Ψ̃^out=Ψ^out`*".  Its proof paragraph uses exactly `commutators-decay`(a) + `HR-auxiliary`(d) — the two lemmas the shard cites.  **No from-memory citation anywhere** (the target brief makes that FATAL; the shard is clean) |
| **V2** | the port's **mathematics**, `n=2` specialization at ⟨1⟩8.⟨2⟩2 | source iterated relation `B_1^*B_2^*Ω=B_1^*B̃_2^*Ω=B̃_2^*B_1^*Ω+O(t^{-∞})`; shard writes `Δ_{2,t}a_{1,t}Ω=[Δ_{2,t},a_{1,t}]Ω` with `Δ_{2,t}Ω=0` | **CORRECT**; it is the source proof, faithfully specialized.  Hypothesis ownership: the source's cross-condition `V(g̃_i)∩V(g_j)=∅ (i≠j)` reduces here to soft-vs-hard disjointness, owned by D31(4) `ε_v>0`.  `commutators-decay`(a) needs **no** isolation hypothesis (I read its proof: almost locality + `norm-corollary` only) — so the port is *not* damaged by D6's gaplessness.  **The upgrade the r2 verdict demanded is real** |
| **V3** | the obstruction the port must dodge: (R8)+(R19) | analytic, from D6/D7.  With `u=e^{ik_h}`, `S_{12}=−(e^{i(k_s+k_h)}−2e^{ik_s}+1)/(e^{i(k_s+k_h)}−2e^{ik_h}+1)`; `S_{12}(0)=−(u−1)/(1−u)=1`; `S'_{12}(0)=−[N'D−ND']/D²|_0` with `N'D−ND' = i(u−2)(1−u)+iu(1−u) = i(1−u)(2u−2) = −2i(1−u)²` ⟹ `S'_{12}(0)=2i` **exactly** | **`1−S_{12}=−2ik_s+O(k_s²)`, exactly as the shard's retained display says.**  Cross-check: `S=e^{iδ}` ⟹ `∂_{k_s}δ|_0=2`, which is S2-2body-S's `1/S` at `S=1/2` — **PROVED row reproduced independently**.  The obstruction is nonzero at exactly the soft law's linear order |
| **V4** | ⟨1⟩9.⟨2⟩5, the smeared Taylor bridge | `‖f‖_2=1`, `dμ_f=|f(u)|²du`, `A(ε)(h)=∫dμ_f(u)S_phys(εu,h)`; expand: `∫|f|²[S(0,h)+εu∂_{k_s}S(0,h)+O(ε²u²)]du` | **CORRECT**: `A(0)=S_phys(0,·)`, linear term `εm_1∂_{k_s}S_phys(0,·)`, remainder `O(ε²)` under S2-2body's uniform cubic remainder and `∫u²dμ_f<∞`.  The `|f_ε(k)|²dk=|f(u)|²du` change of variables is consistent with `f_ε=ε^{-1/2}f(·/ε)`.  No hidden `ε^{-1}` |
| **V5** | ⟨1⟩9.⟨2⟩4, D6 ⊨ D31 | `H=Σ(J/2)(1−P_{x,x+1})≥0`; `Hψ=0 ⟺ P_{x,x+1}ψ=ψ ∀x ⟺` fully symmetric `⟺` constant coefficient `⟹ ∉ℓ²` for `n≥1`.  `Γ_Mg=Σ_x ǧ(x)|x⟩` with `ǧ(x)=∫(dk/2π)g(k)e^{ikx}`: Parseval ⟹ isometric.  `H|x⟩=J|x⟩−(J/2)(|x±1⟩)` ⟹ `HΓ_M=Γ_M ω`, `ω(k)=J(1−\cos k)` | **CORRECT** on every displayed clause.  The one clause the leaf does *not* display is the source's own filter-transparency condition → **R3-O6** |
| **V6** | ⟨1⟩7.⟨2⟩3's chart map | `K^♯=K+2πm ⟹ K^♯/2=K/2+πm`; take `q^♯=q+πm` ⟹ `K^♯/2−q^♯=k_1`, `K^♯/2+q^♯≡k_2 (2π)`.  `q` may then be reflected into `(0,π)` by swapping the labels; `q^♯∈{0,π}` ⟺ `k_1=k_2`, excluded by `ε_v>0` | **CORRECT and unique**; R2-O10 closed |
| **V7** | D6's mass shell vs the source's **isolation** hypothesis | numerically, `ω_1(p)=J(1−\cos p)` vs the two-magnon lower edge `min_k[ω(k)+ω(p−k)]=2J(1−\cos(p/2))`: `p=0.05→0.001250` vs `0.000625`; `p=0.3→0.044664` vs `0.022458`; `p=1.0→0.459698` vs `0.244835`; `p=3.0→1.989992` vs `1.858526` | the one-magnon shell is **embedded in the two-magnon continuum at every `p∈(0,π)`** — D6's mass shell is **not isolated** in `Sp U` in the source's global sense.  The port survives only via the `S^z` grading → **R3-O5** |
| **V8** | checker A2M-C1a/C1b, **independent re-implementation** from the spec text in the *standard spin-1 AKLT basis* (`A^+=√(2/3)σ^+`, `A^0=−σ^z/√3`, `A^-=−√(2/3)σ^-`, `S^z=diag(1,0,−1)`) — different tensors from the shard's Cartesian ones | see §4 | **reproduces every number**: max ratio `0.049383@(1,1,2)`, full ratio table, monotonicity excess exactly `0`, C1a errors `1.04e−15` (theirs `3.35e−15`), ratio deviation `1.75e−10` (theirs `5.61e−10`) |
| **V9** | reliance audit (obligation 5) | `grep` over the shard for `ML4`, `ML5`, bare `S2`, `ML1/ML3/ML6`, Bethe | **clean**: no ML4-Ward at all (so the `n≥2` ERRATUM cannot bite), ML5 unused, no bare `S2` label (only `S2-2body`, **PROVED**), ML2 **PROVED**, ML1/ML3/ML6 named only as *open*, "no integrability hypothesis enters" at ⟨1⟩9.⟨2⟩5.  `𝒮_W`/`tns-iu5` is not relied on |
| **V10** | `theory/checks/soft_index_probe.py --selftest` | re-run | not re-run this round — `theory/checks/` was **added to**, not edited: `git diff` shows `ansatz_scattering_2m_check.py` as a *new file* and no change to `soft_index_probe.py`.  N7 stands by inspection of the diff |

---

## 2. FATAL

None.

---

## 3. MAJOR

### R3-O1 (MAJOR) — the port is a real theorem, but its antecedent is refuted by the **adjudicated** D29: interface clause 1 misdescribes the object it claims to describe, and the "FIXED" disposition of R2-O1 is therefore wrong

**(a) Location.**
`theory/ansatz-scattering-2m.md` ⟨1⟩8 interface clause **1** (ll.379–388,
"The charge leg is an **asymptotic** Haag--Ruelle leg carried through the same
`t→±∞` operation as the hard leg; it is **not** the fixed-time action of a
charge operator on an already prepared hard vector");
clause **5(b)** (2M-1P); ⟨1⟩8.⟨2⟩2; ⟨1⟩9.⟨2⟩2; §7 AC-EX-2M row ("If the
charge-created soft leg is carried as an asymptotic HR leg …"); §8 "Proved
diagonal bridge"; the proposer-status line ll.8–13; and
`theory/ansatz-scattering-2m-r2-response.md` row R2-O1, disposition
"**FIXED**".

**(b) My computation.**  Four parts.

*(i) The port itself is sound — I am not attacking it.*  V1 and V2 above:
the cited clause exists, says what the shard says it says, its proof uses
exactly the two cited lemmas, the `n=2` specialization is faithful, and the
cross-velocity hypothesis is owned by D31(4).  `commutators-decay`(a) needs no
isolation hypothesis, so D6's gaplessness does not damage it (V7 notwithstanding
— see R3-O5).  **The vector→operator gap of R2-O1 is genuinely closed.**  This
is the round's real advance and it should be preserved.

*(ii) The antecedent is false for every D29 on record.*  The shard's clause 1
is not a free choice: it is stated under the header "INTERFACE ASSUMPTIONS ON
**LANE S1'S PROPOSED D29** — ALL ARE HERE", i.e. as a description of D29.  I
read both D29 proposals and the adjudication:

- `theory/soft-index-b.md` §M1 (D29, lane-B wording), verbatim: "the
  charge-created state `Φ(0):=Q[f_ε]ψ_{g,σ}` (D10(c); **the smeared broken
  charge itself — no other source is admitted**)"; the datum is then
  `Φ̂_N(T)` = the momentum kernel of `e^{-iHT}Φ(0)`, compared against
  `Φ̂^{free}_N(T):=Φ̂_N(0)e^{-i[ω(k)+ω(h)]T}`.
- `theory/soft-index.md` §7.1 D29(2), verbatim: "**The only soft insertion**
  is `Q_W[f_{k,ς}]=Σ_{x∈W}\widehat f_{k,ς}(x)q_x^-` … It is **local** for
  finite `W`".
- `theory/verdicts/soft-index-adjudication-r1.md` §3.1 (**BINDING**, and item
  4 of the prover's own READ FIRST list): "**D29 (protocol datum): S1-B's
  design wins.**"

Both are **fixed-time insertions on an already prepared hard vector** — the
exact object clause 1 says the interface is *not*.  Structurally: D29-B applies
`Q[f_ε]` at `t=0` and then evolves the whole state by `e^{-iHT}`, i.e.
`τ_{-T}(Q[f_ε])·e^{-iHT}ψ`.  An HR creator is
`τ_t∘τ^{(d)}_{g_t}(A^*)` — the interacting evolution of the creator *composed
with the free backward evolution of the packet*.  D29-B has the first half and
not the second, and its profile `f_ε` is never free-evolved.  It is not an HR
creator family, at any `T`.

*(iii) The consequence is exactly the r2 obstruction, unmoved.*  For the actual
D29 object, V3 gives, on D6, `Q_{k_s}|k_h⟩−|B^{in}⟩=(1−S_{12})|P_{12}⟩ =
−2ik_s|P_{12}⟩+O(k_s²)` — nonzero at exactly the order (A2M.3) exists to hand
to Lane S1.  Nothing in the port touches this: the shard says so itself
(⟨1⟩8.⟨2⟩2 tail, ⟨1⟩9.⟨2⟩6).  So the r2 FIX DEMAND's branch **(b)** — "if
D29's soft leg is a fixed-time insertion … replace the D6 `R_ε=0` anchor by the
honest one: the two legs differ by the PROVED (R8) branch factor and agree only
in their first jet" — is the branch that is **operative for the merge**, and it
was not supplied.  The demand was "(a) **or** (b)"; the shard executed (a) and
was silent on which branch applies.

*(iv) Why this is MAJOR and not cosmetic.*  Three reasons.
(1) The **disposition is wrong**: R2-O1 is PARTIALLY-FIXED, not FIXED, and the
response's own §"Rebuttal computations" says "No objection was rebutted.  All
were repaired at or below the critic's surviving-statement ceiling" — but
branch (a) is *above* the ceiling for the object the ceiling was set for.
(2) It is the campaign's own **first landmine**, in its interface form.
`briefs/soft-index-target.md` §"Known landmines": "A constraint on limit points
of a family with NO limit points is empty. … **Silence here is a MAJOR
objection**."  A conditional whose antecedent is refuted by the adjudicated
definition is the same defect one level up: the §7 row would enter
`claims/CLAIMS.md` announcing a *theorem* whose hypothesis nothing in the
corpus satisfies, and the orchestrator would read the LSZ gap as closed.
(3) Under the asymptotic reading the theorem also loses the campaign's content:
if the soft leg is an HR creator whose one-particle vector matches `a_2`'s,
then by (A2M.2) the pairing *is* `W_+^*W_-=S_phys` by construction.  The
non-trivial physics — that the **charge**-created leg reproduces the S-matrix —
is precisely what is discarded when `Q` is replaced by its on-shell filtered
HR avatar.  The port converts a hard hypothesis into a true-but-tautologous one
by changing the object.

*(v) Lockstep.*  The statement layer is conditional ("**If** D29's
charge-created soft leg is an asymptotic leg …", ⟨1⟩1(3); "For the
asymptotic-leg reading …", status line; row: "**If** the charge-created soft
leg is carried as an asymptotic HR leg …").  Interface clause 1 is **not**
conditional — it asserts the reading flatly, and asserts the negation of the
adjudicated one.  Statement and interface block therefore disagree in
modality.  The disclaimer "No fixed-time charge/scattering-vector equality …
is claimed" is present and honest, but nowhere does the shard record that the
adjudicated D29 *is* the fixed-time object.

**(c) FIX DEMAND.**  In interface clause 1, replace the categorical assertion
with the disjunction and name the corpus fact: "*Two readings of D29's soft leg
are possible.  (i) Asymptotic HR leg: clauses 5(a)–(b) and ⟨1⟩8.⟨2⟩2 apply and
`(ACE2M-LSZ)` is a theorem.  (ii) Fixed-time insertion `Q[f_ε]ψ` — the reading
of `soft-index.md` §7.1 D29(2), of `soft-index-b.md` §M1, and of the adjudicated
D29-B (`soft-index-adjudication-r1.md` §3.1): creator-choice independence does
**not** apply, and the two legs differ by the PROVED (R8) branch factor
`(1−S_{12})|P_{12}⟩=−2ik_s|P_{12}⟩+O(k_s²)`, agreeing only in their first jet
by S2-2body/(R19).  Reading (ii) is the one the campaign has adjudicated;
under it (A2M.3)'s channel identification is **open**.*"  Move the same
disjunction, verbatim in substance, into the §7 row, §8 and the status line;
and correct the R2-O1 disposition to PARTIALLY-FIXED.

**(d) SURVIVING WEAKER STATEMENT.**  `(ACE2M-LSZ)` is a **theorem** — proved,
not assumed — in the following exact form: *at fixed `ε>0`, if the soft slot is
filled by an admissible Haag–Ruelle creator family whose one-particle vector
equals the D31(3) filtered magnon's ((2M-1P)) and whose velocity support is
disjoint from the hard packet's (D31(4)), then every connected on-shell
`t→±∞` pairing is unchanged when that family is replaced by `a_{2,b}`.*  This
is new and it is right.  For the **adjudicated** D29 soft leg — the fixed-time
`Q[f_ε]ψ_{g,σ}` — the surviving statement is unchanged from r2: exact agreement
on the vacuum (`R_ε=0`, V2 of the r2 verdict), first-order-in-`k_s` agreement
of the two-magnon amplitude (S2-2body/(R19)), and an exact nonzero obstruction
`(1−S_{12})|P_{12}⟩` at the soft law's own linear order.  (A2M.3)'s
identification of the D29 datum with the constructed channel therefore remains
**conditional on an amplitude-level hypothesis about the fixed-time charge leg
that the shard does not display** — the same gap as r2, now correctly
quarantined but not closed.

---

## 4. Checker audit (obligation 4) — run green, run every red, mutated on copies

Runs under `python3 -O`, from the repository root:

| run | printed | exit |
|---|---|---|
| green | `C1a direct=3.354e-15 route=3.243e-15 ratio=5.605e-10`; `C1b agreement=1.128e-16 max_ratio=0.049383@(1,1,2) profile=1.187e-15@(1,1,6) monotonicity_excess=0.000e+00@(1,1,2)`; `PASS` | **0** |
| `--red-c1a` | `RED-OK: C1a route value error 1.000000e+00 > 1.0e-12 \| C1a ratio error 2.400000e+00 > 1.0e-08` | **1** |
| `--red-c1b` | `RED-OK: C1b cap 1.404664 at (3,2,2) > 0.1 \| C1b support monotonicity excess 6.145405e-01 at (3,2,2)` | **1** |
| `--red-supportfold` | `RED-OK: C1b support-profile disagreement 1.646091e-02 at (2,2,2)` | **1** |

Every number in `ansatz-scattering-2m-r2-response.md` reproduces **exactly**.

**Independent re-implementation (V8).**  I re-implemented the §6 spec from its
text in the standard spin-1 AKLT basis (different tensors, `l=𝟙` and `E(r)=r`
verified before use).  C1a: `max|direct−(4/3)(−1/3)^d|=1.04e−15`,
`max|route−…|=1.02e−15`, `max|ratio+1/3|=1.75e−10`; the spec's old `1e-12`
would fail green from `d=8` — **the `1e-8` tolerance is necessary, not
cosmetic**.  C1b ratio table at `d_sep=2` (rows `w_C`, cols `w_D`):

```
        w_D=1     w_D=2     w_D=3
w_C=1  0.049383  0.016461  0.004115
w_C=2  0.016461  0.005487  0.001372
w_C=3  0.004115  0.001372  0.000343
```

max `0.049383` at `(1,1,2)`, monotonicity excess exactly `0`.  All reproduced.

**Mutation tests, on copies in a temp dir (never in place).**

| mutant | what it breaks | exit |
|---|---|---|
| `RIGHT_FIXED → diag(0.6,0.4)` | wrong transfer fixed point | **2** (`C1a direct 1.96e-01`, `C1b cap 2.43`) |
| `A^a=σ_a/√3 → σ_a/2` | wrong tensor normalization | **2** (`C1a 5.39e-01`, `C1b cap 7.40`) |
| **honest support-fold** — multiply the numerator by `w_Cw_D` in **both** the fixed-point-subtracted *and* the direct route (i.e. fold `w_Cw_D` into `C_{A,λ̃}` itself) | the exact defect A2M-C1b exists to exclude | **0 — PASSES** → **R3-O2** |

The checker is genuinely red-capable beyond its registered mutants, contains no
bare `assert`, and no gate is a code no-op (`fixed_connected` and
`direct_connected` are computed by two genuinely different routes).  One gate is
tautological rather than a no-op — R3-O2.

---

## 5. MINOR

### R3-O2 (MINOR) — the profile-agreement gate is a rescaled duplicate of the agreement gate; §6's sentence naming it "the direct certificate" is false, and the real support-fold passes

**(a)** §6 A2M-C1b, the sentence "*The ordinary monotonicity gate is retained,
but this profile-agreement gate is the direct certificate that a support-length
factor has not been hidden in `C_{A,λ̃}`*"; code `check_c1b`, the
`if red_supportfold: ratio *= width_c * width_d` line and the
`support_profile_error` computation.

**(b)** Algebraically, `ratio=|fixed_conn|/(‖C‖‖D‖λ̃^e)` and
`direct_ratio=|direct_conn|/(‖C‖‖D‖λ̃^e)` share their denominator, so
`|ratio−direct_ratio| ≤ |fixed_conn−direct_conn|/(‖C‖‖D‖λ̃^e)` — the *agreement*
gate divided by a positive number of order one (`‖C_3‖‖C_3‖λ̃^6=8·8·0.0156≈1`).
The gate carries no information the `agreement_error` gate does not already
carry.  `--red-supportfold` multiplies `ratio` and **not** `direct_ratio`, so
the detection is by construction: any one-sided edit of that shape fires it, and
no mathematical property is tested.  I built the honest version — fold
`w_Cw_D` into the certified constant, i.e. into **both** routes — on a copy:
green output is byte-identical to the unmutated green run, **exit 0**.
Independently, neither surviving gate can see it: the cap under the fold is
`max_{w} w_Cw_D·ratio = 0.049383` at `(1,1,2)` (`< 0.1`, because the measured
ratios decay like `3^{-(w_C-1)-(w_D-1)}`, which beats `w_Cw_D` growth over
`w≤3`), and the monotonicity excess is `0`.  So the r1-O6 / r2-O8 question —
*is `C_{A,λ̃}` support-length independent?* — is still **not** decided by the
checker at `w≤3`.

**(c) FIX DEMAND.**  Delete the "direct certificate" sentence; state instead
"the profile gate re-tests route agreement in ratio units".  To actually close
r2-O8, extend `w_C,w_D` to `{1,…,6}` and gate on the **variation**
`max_w ratio(w,w,d)/ratio(1,1,d) ≤ 1` with the red mutation applied to the
*certified constant* (both routes), which must then fail; or state in
"Uncertified scope" that support-length independence of `C_{A,λ̃}` is corroborated
only through `w=3` and is not excluded up to a `w_Cw_D` factor.

**(d) SURVIVING WEAKER STATEMENT.**  A2M-C1b still certifies, on AKLT, that the
normalized connected ratio is `≤0.1` uniformly over `w_C,w_D∈{1,2,3}`,
`d_sep∈{2,4,6}`, that it is **monotone non-increasing in the support lengths**
at every `d_sep` (a genuine new gate, killed by `--red-c1b` at `6.1e-01`), and
that the two contraction routes agree to `1.1e-16` at all 27 points.  That is
real corroboration of D31-C2's constant; it does not exclude a `w_Cw_D`
prefactor.

### R3-O3 (MINOR) — quantifier mismatch between (D29-den)'s hypothesis and (A2M.3)'s conclusion

**(a)** ⟨1⟩8 clause 3 vs ⟨1⟩1(A2M.3) vs ⟨1⟩9.⟨2⟩1.

**(b)** Clause 3 assumes the bounds "**along the chosen tuple family**", while
the displayed formulas quantify uniformly (`ess inf_α`, `sup_α`), and (A2M.3)
concludes "**For every sequence** of full index tuples … the corresponding data
are bounded".  ⟨1⟩9.⟨2⟩1 uses the uniform reading ("For **any** full-index
sequence `α_r` … interface clause 3 gives `sup_r‖𝒜_{α_r}‖≤C_I/d_I`").  If
(D29-den) holds only along one chosen family, (A2M.3)'s "for every sequence" is
not proved; if it holds for all allowed `α`, the phrase "the chosen tuple
family" is wrong.  This is the corpus's most common defect class (protocol
obligation 2) reappearing in the one clause that was rewritten to fix it.

**(c) FIX DEMAND.**  Delete "and along the chosen tuple family"; write "for
every allowed full index tuple `α` in the D29 interface family", matching the
displayed `ess inf_α` / `sup_α`.

**(d)** With the uniform reading — the one the displays and the proof already
use — ⟨1⟩9.⟨2⟩1 is correct and (A2M.3)'s diagonal half stands.

### R3-O4 (MINOR) — "unconditional" is the wrong register for a statement that rests entirely on an assumed bound, and clause 3 says "assume" and "supplies" of the same inequality

**(a)** Status line l.10 ("Part (A2M.3) proves an **unconditional**
diagonal-order bounded-family/weak-limit-point statement"); ⟨1⟩8 clause 4 ("the
**unconditional** statement below"); ⟨1⟩9.⟨2⟩1's heading "[NEW — diagonal
bounded-family core]"; against §8's correct "**Under the displayed**
selected-hard-packet denominator bound (D29-den) …".

**(b)** After the repair, the entire content of ⟨1⟩9.⟨2⟩1 is: assume
`sup_α‖𝒜_α‖≤C_I/d_I` (clause 3), conclude by reflexivity of `L²(I)` that
bounded sequences have weakly convergent subsequences.  That is Banach–Alaoglu
applied to a hypothesis.  Calling it "unconditional" is true only in the
narrow sense "not conditional on `(ACE2M-LSZ)`/`(ACE2M-SR)`"; a reader of the
status line reads it as unconditional simpliciter, and §8 says something
different.  Second, within clause 3 itself: the block opens "**assume** the
displayed uniform denominator and numerator bounds" and closes
"Cauchy--Schwarz … **supplies** the second bound" — assumed and derived in six
lines.

**(c) FIX DEMAND.**  Replace "unconditional" by "conditional only on
(D29-den)" in the three places; and in clause 3 either drop "Cauchy--Schwarz
supplies" or demote it to "is the estimate (D29-den) is modelled on".

**(d)** The mathematics is correct and the §8 wording is already right; this is
a three-word lockstep repair.

### R3-O5 (MINOR) — a source hypothesis is invoked that D6 does not satisfy; the sector relativization that rescues it is never displayed at the point of use

**(a)** ⟨1⟩8.⟨2⟩1's justification ("source equation `(creation-on-vacuum)` in
§"Haag--Ruelle creation operators"") and ⟨1⟩8.⟨2⟩2's justification (source
Theorem `Haag-Ruelle`).

**(b)** Source Definition `HR-creation-operators` (l.1083) requires
`Sp_{A^*}τ ⊂ (0,∞)×Γ̂` compact **and** `Sp_{A^*}τ ∩ Sp U ⊂ 𝔥`, and Theorem
`Haag-Ruelle` stands on an **isolated** mass shell (Definition
`mass-shell-definition`, isolation clause 1, l.980).  On D6 the one-magnon shell
is **not** isolated in `Sp U`: I computed the two-magnon lower edge at total
momentum `p`, `min_k[ω(k)+ω(p−k)] = 2J(1−\cos(p/2))`, against `ω(p)=J(1−\cos p)`
— `0.000625 < 0.001250` at `p=0.05`, `0.022458 < 0.044664` at `p=0.3`,
`0.244835 < 0.459698` at `p=1.0`, `1.858526 < 1.989992` at `p=3.0`.  The
magnon is embedded in the two-magnon continuum at every `p∈(0,π)`.  The port
nevertheless survives, for a reason the shard has but does not display at the
leaf: `S^z` is conserved, D31(2) relativizes isolation to the charge-one sector,
and `S^-_xΩ` is *exactly* one-magnon, so `B^*Ω` has spectral support in `𝔥`
regardless — which is all `(creation-on-vacuum)` needs.  `commutators-decay`(a)
needs no isolation at all (V2).

**(c) FIX DEMAND.**  Add one sentence at ⟨1⟩8.⟨2⟩1: "the source's isolation and
`Sp_{A^*}τ∩Sp U⊂𝔥` conditions are used only in the charge-graded form of
D31(2); on D6 the shell is embedded in the two-magnon continuum and is isolated
only within the charge-one sector, which is what `(creation-on-vacuum)` and
`commutators-decay`(a) require here."

**(d)** The port stands; only its hypothesis audit is incomplete.  D31(2)
already carries "isolated within the charge-one sector", so the fix is a
cross-reference, not new mathematics.

### R3-O6 (MINOR) — ⟨1⟩8.⟨2⟩1 proves (2M-1P) for the **unfiltered** charge and asserts the filtered family inherits it; the source's own transparency condition is the missing line

**(a)** ⟨1⟩8.⟨2⟩1, the sentence "Applying the two on-shell HR evolutions
preserves this vacuum vector for every `t` by the exact band equation".

**(b)** The displayed computation is
`Q[f̂_ε;ξ^-]Ω=Σ_x f̂_ε(x)S_x^-Ω=Γ_M(f_ε)` — the **time-zero, unfiltered**
charge.  (2M-1P) is about `a_{Q,2,b,t}[f_{ε,t}]Ω_A`, i.e. after the
positive-energy filter *and* the HR evolution.  The evolution half is
`(creation-on-vacuum)` (cited, correct).  The **filter** half is not:
`τ_f(A^*)Ω=A^*Ω` is not automatic, and the source states the condition for it
explicitly in the `Haag-Ruelle-Fock` proof — "*Demanding in addition that `f̂`
is equal to one on `𝔥∩Sp_{A^*}τ` we can ensure that `B^*_{f,t}(g_t)Ω=B^*_t(g_t)Ω`*".
Here that condition *is* met, because `S^-_xΩ` is purely one-magnon and the
packet restricts momentum to `supp f_ε`; but it is the one place where filtering
could change the vector, and it is the whole reason the *hard*-state version of
the same statement fails (r2-O1(iii)).  Leaving it as "by the exact band
equation" is a gesture at exactly the step under audit.  Cosmetic residue of
R2-O11: the display writes `Γ_M(f_ε)` and `a_{2,b}[f_ε]Ω` with `b` free on the
right and absent on the left (harmless at D6's `m=1`).

**(c) FIX DEMAND.**  Insert the transparency line: "choose the filter with
`χ̂_2=1` on `𝔥∩Sp_{Q}τ` over `supp f_ε`, so that filtering does not move the
vacuum vector (source, `Haag-Ruelle-Fock` proof, pseudo-relativistic case);
`S_x^-Ω` is purely one-magnon on D6, so the condition holds."  Bind `b` on both
sides.

**(d)** (2M-1P) is **true on D6** as claimed; only one justificatory line is
missing.

### R3-O7 (MINOR) — (A2M.3)'s two halves are about different families, and their join is interface clause 2, not a proof

**(a)** ⟨1⟩9.⟨2⟩1 vs ⟨1⟩9.⟨2⟩2 vs ⟨1⟩1(A2M.3).

**(b)** ⟨2⟩1 produces weak limit points along **`ε_r↓0` diagonals**.  ⟨2⟩2
identifies "every **fixed-`ε`** subsequential value for which the hard
preparation/resolution converges".  Nothing connects the two: no step shows an
`ε↓0`-diagonal limit point is a limit of fixed-`ε` identified values, and the
step from the port (an equality of exact `t→±∞` HR pairings) to "the weak
subsequential limit of the finite-index datum equals the constructed value" is
interface clause 2 (assumed convergence into `ran W_∓`), cited but not proved.
Since (A2M.3) is billed as the *nonvacuity bridge to Lane S1*, and Lane S1 needs
the `ε↓0` limit points to be constructed-channel values, the bridge as written
does not span the gap it is named for.

**(c) FIX DEMAND.**  Add one clause to (A2M.3): "the diagonal compactness of
⟨2⟩1 and the fixed-`ε` channel identification of ⟨2⟩2 are **separate**
statements; that an `ε↓0`-diagonal limit point is a limit of identified
fixed-`ε` values is **not** claimed and would require (ACE2M-SR)."

**(d)** Both halves are individually correct at the strengths stated; only their
composition is unasserted, and saying so costs one sentence.

---

## 6. NOTE

**R3-N1 — `--red-c1a` fails the route and ratio gates, not the direct gate.**
`direct_connected` is computed connectedly in both green and red, so the spec's
"its retained `+1` must fail **both gates**" is satisfied only if "both" means
{route value, ratio}.  Say which two.

**R3-N2 — `monotonicity_excess` is pinned at exactly `0` in green.**  The max
ranges over the baseline points `(1,1,d_sep)` themselves, where the excess is
identically `0`, so the printed green value carries no margin information.
Excluding the baseline would print the true margin (`−0.033` at `(1,2,2)`).

**R3-N3 — the response's paste is reproducible to the digit.**  All four runs
reproduce the pasted stdout exactly under `python3 -O` from a clean checkout.
That is worth recording: this lane's reported numbers have been trustworthy in
all three rounds.

**R3-N4 — (R8)/(R19) reproduced from scratch.**  `S'_{12}(0)=2i` exactly
(V3), independent of `soft-current-recon.md`, and consistent with S2-2body-S's
`∂_{k_s}δ_phys|_0 = 1/S = 2` at `S=1/2`.  The corpus's PROVED row is right and
the shard quotes it correctly.

**R3-N5 — L3 citation discipline is clean.**  Every 1412.2970 anchor in the
new text resolves to a real `\label` in the local TeX (V1).  The target brief
makes a from-memory citation FATAL; there is none.

**R3-N6 — the D31-C2 derivation is untouched.**  `git diff` shows ⟨1⟩3.⟨2⟩1
and ⟨2⟩3 unchanged since r2; ⟨2⟩2 gained only the `Ψ_O` definition and the
displayed chain identity (r2-N2's fix).  Fenced, do not churn.

**R3-N7 — the shard is now the only place in the corpus that states the
asymptotic-leg reading of D29.**  If the orchestrator ever *adopts* that reading
(overriding adjudication §3.1), R3-O1 dissolves and the port closes the LSZ gap
outright.  That decision is above this lane's pay grade and should be recorded
as a bd item, not silently taken inside a proof shard.

**R3-N8 — `theory/checks/` was added to, not edited.**  `ansatz_scattering_2m_check.py`
is a new file; `soft_index_probe.py` and the other frozen checkers are byte-identical
in the diff.  N7 of r2 is preserved.

---

## 7. VERIFIED CORRECT — fenced, do not churn

- **⟨1⟩3 (D31-C2 from the D1 transfer gap)**, including the r2 `V_w`
  Stinespring mechanism and the newly displayed `Ψ_O` chain identity.  Third
  independent survival.
- **⟨1⟩5 (2M-Cook)**, **⟨1⟩6 (isometry, corrected exponents)**, **⟨1⟩7.⟨2⟩2
  (bound/two-string fence)** — unchanged since r2, re-verified there.
- **⟨1⟩7.⟨2⟩3's chart map** (V6) — new, correct, R2-O10 closed.
- **⟨1⟩8.⟨2⟩2's port** (V1, V2) — citations accurate to section, theorem,
  equation and lemma part; the `n=2` specialization is the source proof; the
  cross-velocity hypothesis is owned by D31(4).  **This is a genuine theorem
  and a genuine advance over r2.**
- **⟨1⟩9.⟨2⟩1's inequality** `sup‖𝒜_α‖≤C_I/d_I` (re-derived).
- **⟨1⟩9.⟨2⟩4 (D6 ⊨ D31)** (V5) — every displayed clause correct, including
  the `P_{x,x+1}ψ=ψ ⟹ ψ∉ℓ²` zero-mode argument and `Γ_M` isometric with
  `dk/2π`.
- **⟨1⟩9.⟨2⟩5 (smeared Taylor)** (V4) — correct, no hidden `ε^{-1}`.
- **A2M-C1a** as repaired: connected reading implemented, `1e-8` ratio
  tolerance necessary and sufficient through `d=12`, red exits 1.
- **A2M-C1b's monotonicity gate** — a real new gate, killed by `--red-c1b`.
- **Reliance audit** (V9): no REFUTED row, no ML4-Ward `n≥2`, no Bethe.

---

## 8. Register comparison against the nearest PROVED row

Nearest adjudicated precedent for a *conditional* theorem with a named
interface hypothesis is **M-INDEX-spec** (`claims/CLAIMS.md` l.71), whose
adjudicated scoping sentence reads, in part: "*Proved **only** as the
conditional implication: … ⟹ … **along that subsequence** … D27 is assumed, not
derived; **no implication H-AD-G ⟹ (LR) is claimed**.*"

| item | M-INDEX-spec register | AC-EX-2M r3 | verdict |
|---|---|---|---|
| conditionality named at the point of statement | yes, "Proved only as the conditional implication" | yes for `(ACE2M-SR)` and for the asymptotic-leg reading | **in register** |
| the assumed hypothesis named as assumed | "D27 is **assumed, not derived**" | (D29-den) displayed and assumed; `(ACE2M-SR)` named | **in register** |
| subsequence/diagonal discipline | "along that subsequence"; "support quantization is subsequence-free" | "diagonal-order statement; no unconditional existence of the iterated limit" | **in register** |
| the *refuted* neighbour named in the row | yes — "its unconditional existence is REFUTED (M-INDEX-LA-strong)" | **no** — the row does not say that the adjudicated D29 soft leg is the fixed-time object for which the identification fails by (R8) | **BREACH** → R3-O1 |
| "unconditional" used loosely | never | status line + clause 4 | minor breach → R3-O4 |

The M-INDEX precedent is the exact template: it names the refuted neighbour
*inside the row*, so no reader can mistake the conditional for the general
statement.  AC-EX-2M's row omits the corresponding sentence.  That omission is
the register content of R3-O1, and the scoping sentence in §9 supplies it.

---

## 9. PROMOTE / HOLD (deliverable)

### (A2M.3) interface clause — **HOLD**

**Missing step, named:** a treatment of the *fixed-time* D29 soft leg
`Φ(0)=Q[f_ε]ψ_{g,σ}` (adjudicated D29-B, `soft-index-adjudication-r1.md` §3.1).
Either (i) prove that the `T→∞` D29-B readout of the fixed-time
charge-created state has the same connected on-shell pairing as the HR
asymptotic leg — which must be established **at `O(k_s)`**, since (R8)+(R19)
give an exact mismatch `−2ik_s|P_{12}⟩+O(k_s²)` there — or (ii) take the r2
branch (b) downgrade and state plainly that under the adjudicated D29 the
identification is open.  Until one of these lands, `(ACE2M-LSZ)` is a theorem
about a soft leg the campaign has not adopted, and (A2M.3)'s channel
identification must not be read as available to Lane S1.

### AC-EX-2M as a whole — **PROMOTE at SKETCH**, with the scoping sentence below applied verbatim

Rationale: (A2M.1)–(A2M.2) have now survived three hostile rounds with 0 FATAL;
the four r2 preconditions I set for their promotion (R2-O3, R2-O6, R2-O7,
R2-O10) are all VERIFIED-FIXED above; the D31-C2 derivation is independently
reproduced for the third time; the checker is green, red-capable and
mutation-tested; the reliance audit is clean.  The single MAJOR is confined to
(A2M.3)'s interface and is fully quarantined by the sentence below.  Merging at
SKETCH with this row is strictly better for the corpus than leaving the whole
theorem out.

**Exact replacement text for the `AC-EX-2M` cell in `claims/CLAIMS.md`
(statement column) — copy verbatim, no paraphrase:**

> Under D31/H-ACE2M over one D1 injective translation-invariant MPS vacuum, exact momentum-filtered magnon bands and two compact separated-velocity packets give fixed-packet Cook wave operators `W_±`; D1's transfer gap derives D31-C2, and with D31(3)'s uniform almost-locality also D31-C4, so no independent clustering hypothesis is assumed.  The maps are isometries, intertwine joint translations, and avoid the D31-listed fiberwise-isolated charge-two bound bands.  On D6--D8 a fixed packet range lies in the corresponding part of ML2's Jacobi scattering summand: `W_+^*W_-` carries D7's `S_phys`, while the two-string is orthogonal.  D6 is verified to satisfy D31(1)--(5).  **Adjudicated scoping (verbatim):** for Lane S1's D29 interface the shard proves exactly two separate things.  (1) *Diagonal compactness, conditional on (D29-den):* assuming the displayed selected-hard-packet bounds `ess inf_α ess inf_{h∈I}|𝒟_α(h)|≥d_I>0` and `sup_α‖𝒝_α‖_{L²(I)}≤C_I<∞`, one has `sup_α‖𝒜_α‖_{L²(I)}≤C_I/d_I`, so every full-index sequence respecting (D29-order) with `ε↓0` has a weakly convergent `L²(I)` subsequence.  This is Banach--Alaoglu on an assumed bound; nothing unconditional is claimed, and no iterated-order object is asserted to exist.  (2) *Creator-choice independence, `(ACE2M-LSZ)`, a THEOREM:* at fixed `ε>0`, if the soft slot is filled by an admissible Haag--Ruelle creator family whose one-particle vector equals the D31(3) filtered magnon's ((2M-1P)) and whose velocity support is disjoint from the hard packet's (D31(4)), then every connected on-shell `t→±∞` pairing is unchanged when that family is replaced by `a_{2,b}` (ported from `refs/arxiv-1412.2970` Theorem `Haag-Ruelle`, final clause).  **This theorem does NOT apply to the adjudicated D29.**  Both D29 proposals on record — `theory/soft-index.md` §7.1 D29(2) and `theory/soft-index-b.md` §M1, the latter adopted by `theory/verdicts/soft-index-adjudication-r1.md` §3.1 — specify a fixed-time insertion `Q[f_ε]ψ` on an already prepared hard vector, which is not a Haag--Ruelle creator family; for it the PROVED row S2-2body gives `Q_{k_s}|k_h⟩−|B^{in}⟩=(1−S_{12})|P_{12}⟩=−2ik_s|P_{12}⟩+O(k_s²)` (R8, R19), nonzero at the soft law's own linear order, and the identification of the D29 datum with the constructed channel is **OPEN**.  First-jet compactness is conditional on `(ACE2M-SR)`, including existence of the `N,t` limits; its full `(W,σ)`-uniform version is open on every model, and D6 verifies only the exhaustion-free infinite-chain first jet.  No fixed-time charge/scattering-vector equality, soft-uniform Cook bound, equal-velocity/endpoint construction, bound-state wave operator, range exhaustion, or asymptotic completeness is claimed.

(Status column `SKETCH`; depends-on `D1, D3(a), D6--D8, D10, D12(a′), D24, D31,
ML2, S2-2body`; where-proved `theory/ansatz-scattering-2m.md`; where-tested
`theory/checks/ansatz_scattering_2m_check.py`, A2M-C1a/C1b.)

---

## 10. Summary and trajectory

- **FATAL 0** (0 in r1, 0 in r2, 0 in r3)
- **MAJOR 1** — R3-O1 (the port is a real theorem; its antecedent is refuted by
  the adjudicated D29, so R2-O1 is PARTIALLY-FIXED, not FIXED)
- **MINOR 6** — R3-O2 … R3-O7
- **NOTE 8** — R3-N1 … R3-N8

**Trajectory: 6 MAJOR → 2 MAJOR → 1 MAJOR, 0 FATAL throughout.  Severity is
falling monotonically.**  Ten of eleven r2 objections are VERIFIED-FIXED by
recomputation; R2-O1 is PARTIALLY-FIXED and R2-O8 is PARTIALLY-FIXED.  The
artifact is **not** being re-overclaimed each round: the statement layer, the
HONEST STATUS and the merge row all weakened in lockstep this round, the two
checker-spec defects were fixed in code, and the one MAJOR is the *consequence*
of a correctly-executed but wrongly-aimed repair, not new ambition.  The
remaining work is a single disjunction in interface clause 1 plus six
one-to-three-line MINOR repairs; a fourth round should reach 0 MAJOR.

**FAIL(R3-O1)**
