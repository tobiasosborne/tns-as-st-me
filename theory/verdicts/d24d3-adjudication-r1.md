<!-- ROLE: orchestrator-lane ADJUDICATION of corpus referral bd `tns-iu5` —
     the ρ-dependence of the D24(d) clause-3 external-flux normalisation.
     Work order: briefs/d24d3-adjudication.md.  Adjudicator lane, not a
     prover lane: neither S1-A nor S1-B owns this edit and neither lane's
     workaround was imported.
     Writable files of this lane: this file and
     theory/checks/d24d3_normalization_check.py — nothing else was edited.
     definitions.md and claims/CLAIMS.md are NOT edited here; the repaired
     text is quarantined in §5 MERGE PROPOSALS for the orchestrator. -->

# r1 adjudication — D24(d) clause 3, the external-flux normalisation

**Verdict: the frozen clause is REFUTED as a universal statement and is
REINSTATED as the `2ρ = 1` special case.  It is SPLIT into a surviving
hypothesis (3a) and a derived value (3b),**

    L(0,h) = −iχ / (Z · v_h),        Z := ⟨Ω|[S^+_x, S^-_x]|Ω⟩ = 2ρ ∈ ℤ_{>0},

**with the fence `ρ > 0`.  D24(c)'s constant moves in lockstep.  ML5-B stays
PROVED with its displayed conclusion changed from `2iχk M_1` to
`(iχ/ρ) k M_1`.  `𝒮_W` is NOT nonempty after the repair — the repair removes
a proof of emptiness, it does not supply an instance (bd `tns-axg`).**

Certificate: `theory/checks/d24d3_normalization_check.py`
(green `python3 -O` exit **0**; four red modes `--red-frozen`, `--red-power`,
`--red-halfpower`, `--red-ward`, each exit **1**).

---

## 0. What I did

Everything below was recomputed on this lane; nothing was taken on the
critic's word, and no number was copied from either S1 shard.

* **(A-a)** Symbolic evaluation of ML5-B (6) with the frozen constant, in
  `sympy`, carrying `ρ` and `v_h` as free symbols.
* **(A-b)** First-principles spin-`S` ladder matrices (built from
  `⟨m±1|S^±|m⟩`, not imported); the order-parameter residue
  `Z = ⟨Ω|[S^+_x,S^-_x]|Ω⟩` at `2S = 1…6`; the soft-leg norm
  `‖Q^-_k|Ω⟩‖²/N`.
* **(A-c)** Exact ring computation of the Ward residue
  `⟨h|Q_0^†J^-_0|h⟩` at `2S = 1,2,3,4`, with `Q_0 = Σ_x S^-_x` and
  `J^-_0 = Σ_x −[h_{x,x+1},S^-_x]` applied configuration-by-configuration
  from the raw two-site bond matrix `h = −J(S_x·S_{x+1} − S²)`.
* **(A-d)** An **ansatz-free** two-magnon ED of the spin-`S` ring: momentum
  blocks assembled from the same raw bond matrix, levels inverted through
  `E = ω_S(k_1)+ω_S(k_2)`, `k_1+k_2 = K`, and `δ` read off by Bethe–Yang.
  `N ∈ {40,60,90,120,160}`, `2S ∈ {1,2,3,4}`.  My `N = 60`, `2S = 1`,
  `K = 0.942477796077` row reproduces
  `numerics/results/spin1-bc-falsifier.json` `A_ring_runs[0]`
  (`k_s = 0.108839701468`, `δ = 0.247196780925`,
  `δ/k_s = 2.27120046812`) to all printed digits — my implementation and
  the frozen data are independent and agree.
* **(A-e)** Ground truth reused per the work order:
  `numerics/results/spin1-bc-falsifier.json` `A_ring_summary`
  (12 extrapolated ansatz-free rows, `S ∈ {1/2,1,3/2,2}`) and
  `theory/checks/spin_s_slope_check.py` (read, not re-derived).
* **(A-f)** L3 check of the type-B Goldstone register against local TeX:
  `refs/arxiv-1203.0609/revision3.tex` (Watanabe–Murayama), which defines
  the symplectic density `ρ_{ij} = −i⟨0|[Q_i, j^0_j]|0⟩` and, for the
  Heisenberg ferromagnet `H = −J Σ s_i·s_j`, identifies its coefficient as
  `m = ⟨j^0_z⟩`, "the magnetization of the ground state".

---

## 1. The defect, reproduced independently

### 1.1 The frozen clause is density-blind — exactly

ML5-B (6) is `(e^{ik}−1) L(k,h) [2i v_h M_1^O(h)]`.  Substituting the frozen
D24(d)3 value `L(0,h) = −iχ/v_h` and expanding:

    (ik + O(k²)) · (−iχ/v_h) · 2i v_h M_1  =  2iχ k M_1 + O(k²).

`sympy` confirms both derivatives vanish identically:
`∂_ρ[jet] = 0` and `∂_{v_h}[jet] = 0` (**D24N-C1**).  The frozen flux does
not merely happen to give `2`; it *cancels `v_h` in full*, and `v_h` is the
only place the density could have entered.  So the frozen clause forces
soft slope `2χ` at **every** tail density, with no room for a correction.

### 1.2 The exact dynamics gives `1/S`, and I measured it myself

My ansatz-free ED (A-d) — no closed form used to obtain `δ` — gives, at
`K ≈ 0.9425`, `J = 1`:

| `2S` | `δ/k_s` at `k_s ≈ 0.167 … 0.040` | linear-in-`k_s` extrapolation | `1/S` | dev |
|---|---|---|---|---|
| 1 | 2.4872 → 2.0847 | 1.9433 | 2.0000 | 2.8% |
| 2 | 1.2864 → 1.0525 | 0.9688 | 1.0000 | 3.1% |
| 3 | 0.8659 → 0.7039 | 0.6455 | 0.6667 | 3.2% |
| 4 | 0.6523 → 0.5287 | 0.4841 | 0.5000 | 3.2% |

and `max|δ_ED − arg S_{12}^{closed}| = 1.6·10^{-12}` over all rows: the ED
levels *are* the closed-form phase, to machine precision, at every spin.
The frozen 12-row `A_ring_summary` extrapolation (richer `N` ladder, up to
`N = 480`) sharpens this to `≤ 0.43%` (**D24N-C4**).

### 1.3 The collision, and hence the emptiness

Corpus-internal identification (not mine): the soft multiplier's first jet
IS the two-body contact-ratio derivative.  `soft-current-recon.md` ⟨1⟩4
(R17) derives `s = 1 + 2ik_s + …`, i.e. `s_1 = 2i`, and
`ml5-universality.md` ⟨1⟩4.⟨3⟩4 uses exactly that `s'(0,h) = 2i` as the
number ML5-B (5) reproduces; `oracle-bethe.md` O9 calls the same `2` "the
signed Wigner displacement coefficient".  `S2-2body-S` (T.3)–(T.4)
generalises `s_1` to `i/S`.

Therefore, for a source `O ∈ 𝒮_W` with `M_1^O ≠ 0` in the spin-`S`
ferromagnet `H_S` of S2-2body-S:

    ML5-B  ⇒  jet = 2χ                (frozen D24(d)3, every ρ)
    S2-2body-S ⇒  jet = χ/S           (PROVED, exact, every S)
    ⇒  S = 1/2.

**Relative deviations of the frozen prediction from the ansatz-free data
(D24N-C5): `0.000` at `S=1/2`, `1.002` at `S=1`, `2.003` at `S=3/2`,
`3.003` at `S=2`** — pre-registered band `0.08`.  The frozen class `𝒮_W` is
therefore **empty in the spin-`S` ferromagnet register at every `ρ ≠ 1/2`**,
and D24(d)'s own admission that no microscopic member is known makes it
vacuous, not false, elsewhere.  The critic's finding is confirmed in full.

### 1.4 The honest second horn

The emptiness argument uses one bridge: *the jet of the D24(d) soft
multiplier equals the jet of the two-body physical phase*.  That bridge is
the corpus's own (§1.3), but it is not itself a PROVED row.  Both horns
condemn the frozen clause:

* if the bridge holds, `𝒮_W` is provably empty off `ρ = 1/2`;
* if the bridge fails, then ML5-B's constant has no contact with any PROVED
  row at all, and D24(d)3 stipulates the value of an object no computation
  in the corpus can reach — a stronger vacuity.

Either way the clause cannot stand as frozen.  The repair below is stated
so that it is correct under the first horn and *harmless* under the second
(it is a value, derived by matching, with its provenance displayed).

### 1.5 Root cause: `L(k,h)` is never defined

`grep -rn "L(k,h)\|L(0,h)"` over `theory/`, `definitions.md`, `paper/`
returns only clause D24(d)3, `ml5-universality.md` ⟨1⟩3 hyp. 3 / (6) /
⟨2⟩1.⟨3⟩2, and the two S1 shards transplanting them.  **There is nowhere in
the corpus a definition of the symbol `L`.**  D24(d)3 assigns a value to an
undefined object.  Under L4 that is the actual defect: an undefined symbol
can be neither stipulated nor derived.  The repair must therefore *first*
define `L` and only then evaluate it — which is what §2 does, and it is why
neither S1 lane could derive its factor (S1-A redefined the value of an
undefined symbol; S1-B multiplied an undefined symbol by an undefended
factor).

---

## 2. The adjudication (Lamport)

**THEOREM D24N (repaired external-flux normalisation).**

**ASSUME.**  D24(a)–(b); D24(d) clauses 1 and 2; a broken-symmetry tail with
density `ρ := ω_α(S^z) > 0` in the sense of `notation.md`'s `ρ`-row and
claim `M-IDX-density`; and the fully polarised ferromagnetic register
`H_S = −JΣ_x(S_x·S_{x+1} − S²)` of `S2-2body-S`, in which `ρ = S`.

**PROVE.**  With `L` defined as in ⟨1⟩1 below,

    Z := ⟨Ω|[S^+_x, S^-_x]|Ω⟩ = 2⟨Ω|S^z_x|Ω⟩ = 2ρ,
    L(0,h) = −iχ / (Z v_h) = −iχ / (2ρ v_h),                        (D24N.1)

and consequently the ML5-B multiplier is

    𝖲(k;h) = (e^{ik}−1) L(k,h) · 2i v_h  =  (2χ/Z) i k + O(k²)
                                          =  (χ/ρ) i k + O(k²).     (D24N.2)

At `Z = 1` (`ρ = 1/2`) this is the frozen clause and the frozen `2χ`,
verbatim.

### ⟨1⟩1.  `L` is a quotient, not a datum

**⟨2⟩1. PROVE.**  Under D24(d)1–2 the descendant external-leg term
`𝔈^O(k,h)` is a well-defined summand of `M_2^O`, and

    L(k,h) := 𝔈^O(k,h) / [ (e^{ik}−1) · 2i v_h · M_1^O(h) ]        (D24N.3)

is well defined wherever `M_1^O ≠ 0` and `k ≠ 0`, and the surviving content
of clause 3 is that (D24N.3) is independent of `O` and uniformly `C¹`.

**⟨3⟩1.**  Clause 1 states that `M_2^O` is *exactly* the sum of the
descendant external-leg term, the orthogonal-current term and the direct
contact term; so `𝔈^O` is a named object of the decomposition, not an
auxiliary.
Justification: D24(d)1.

**⟨3⟩2.**  Clause 2 states that the descendant residue factorises as
`2i v_h M_1^O(h)`; the remaining kinematic factor `(e^{ik}−1)` is fixed by
the lattice charge/current relation used in ML5-B (6).  Hence the quotient
(D24N.3) is exactly what is left over, and it is the object clause 3 talks
about.
Justification: D24(d)2, `ml5-universality.md` (6).

**⟨3⟩3.**  Being a quotient of two model-determined objects, `L(0,h)` is an
**output** of any model in the class, not a free input.  Clause 3's
process-independence hypothesis is precisely the statement that this output
is the same for every `O`; it is therefore legitimate to *compute* it in one
member of the class and transport it.
Justification: ⟨3⟩1–⟨3⟩2 and clause 3's own process-independence clause.

**⟨3⟩4. QED.**

### ⟨1⟩2.  The order-parameter density `Z`, and its quantisation

**⟨2⟩1. PROVE.**  `Z := ⟨Ω|[S^+_x,S^-_x]|Ω⟩ = 2ρ`; in the fully polarised
spin-`S` tail `Z = 2S ∈ ℤ_{>0}`; and `‖Q^-_k|Ω⟩‖² = Z·N` for every `k`,
where `Q^-_k = Σ_x e^{ikx}S^-_x`.

**⟨3⟩1.**  `[S^+_x,S^-_x] = 2S^z_x`, so `Z = 2⟨S^z_x⟩ = 2ρ`; on the fully
polarised tail `⟨S^z_x⟩ = S`.
Justification: the su(2) algebra; named computation **D24N-C2**
(first-principles ladder matrices, `2S = 1…6`, max error `8.9·10^{-16}`).

**⟨3⟩2.**  `‖Q^-_k|Ω⟩‖² = Σ_{x,y}e^{ik(x−y)}⟨Ω|S^+_yS^-_x|Ω⟩
 = Σ_x⟨Ω|S^+_xS^-_x|Ω⟩ = ZN`, `k`-independent.
Justification: `S^+_y|Ω⟩ = 0` forces `x = y`; named computation
**D24N-C2**.

**⟨3⟩3.**  `Z = 2ρ ∈ ℤ_{>0}` whenever (S) at both tails and D26(INT) hold,
by claim `M-IDX-density` (`2ρ ∈ ℤ`), together with the fence `ρ > 0`.
Justification: `M-IDX-density`, D26.

**⟨3⟩4.**  `Z` is the type-B Goldstone symplectic density of the broken
pair.  In the local ground truth
`refs/arxiv-1203.0609/revision3.tex` the type-B normalisation is
`ρ_{ij} = −i⟨0|[Q_i, j^0_j]|0⟩`, and for the Heisenberg ferromagnet its
value is `m = ⟨j^0_z⟩`, the ground-state magnetisation.  In the complexified
basis used throughout this campaign (`q_x = S^-_x`, `soft-current-recon.md`
⟨1⟩1) that is exactly `Z = ⟨[S^+_x,S^-_x]⟩ = 2ρ`.
Justification: L3 quotation from local TeX; D10, D26.

**⟨3⟩5. QED.**

### ⟨1⟩3.  The Ward residue is exactly linear in `Z`

This is the load-bearing step: it is where the density actually lives, and
it is why the frozen clause loses it.

**⟨2⟩1. PROVE.**  On the spin-`S` ring, with normalised one-magnon `|h⟩`,

    ⟨h|Q_0^† J^-_0|h⟩  =  Z · (2iJ sin h)  =  2i v_S(h),           (D24N.4)

exactly, where `v_S(h) = ω_S'(h) = 2JS sin h = Z J sin h`.

**⟨3⟩1.**  `ω_S(k) = 2JS(1 − cos k)`, hence `v_S(h) = ZJ sin h`.
Justification: independent ED of the one-magnon block assembled from the raw
bond matrix, `2S = 1,2,3,4` (agreement `≤ 3.3·10^{-16}`); shard
`spin-s-twomagnon.md` ⟨1⟩1.⟨2⟩2 states the same dispersion.

**⟨3⟩2.**  Direct ring computation of `⟨h|Q_0^†J^-_0|h⟩` with
`J^-_0 = Σ_x −[h_{x,x+1},S^-_x]` reproduces `Z·2iJ sin h` at
`2S = 1,2,3,4` and two hard momenta, max error `4.8·10^{-15}`.
Justification: named computation **D24N-C3**.

**⟨3⟩3.**  Frozen `soft-current-recon.md` (R14) reads
`⟨k_h|Q_0^†J^-_0|k_h⟩_N = 2iJ sin k_h = 2i v_h`.  Both readings are correct
**only at `Z = 1`**: `2iJ sin k_h` is the `Z`-free kinematic number,
`2i v_h` carries one factor of `Z`.  D24(d)2 adopts the `Z`-carrying
reading; D24(d)3's `−iχ/v_h` then cancels it *in full*.  That single
cancellation is the entire defect.
Justification: (R14) as frozen, ⟨3⟩1–⟨3⟩2, and D24N-C1.

**⟨3⟩4.**  Structural reading (why one power of `Z`, not a half-power and
not two).  `Z` is the residue of the order-parameter two-point function,
`⟨Ω|S^+_xS^-_y|Ω⟩ = Zδ_{xy}`; equivalently `S^-_x = √Z a^†_x(1 + O(n/Z))`
in Holstein–Primakoff variables.  The residue (D24N.4) is a pairing of
**two** order-parameter insertions — the charge `Q_0` that projects onto the
soft leg and the current `J^-_0` that emits it — hence carries `(√Z)² = Z`
exactly once, which is what ⟨3⟩2 measures.  Converting that two-insertion
pairing into a **single** unit-normalised on-shell soft leg is division by
`Z` once.  Hence (D24N.1).
Justification: ⟨3⟩1–⟨3⟩3, D24N-C2, D24N-C3.  *This leaf is a structural
identification, not a proof — see §6 HONEST STATUS item H3.*

**⟨3⟩5. QED.**

### ⟨1⟩4.  The value, and why the exponent cannot be anything else

**⟨2⟩1. PROVE.**  `L(0,h) = −iχ/(Z v_h)` and (D24N.2).

**⟨3⟩1.**  By ⟨1⟩1 the value is an output.  Compute it in `H_S`:
ML5-B (6) with the quotient definition gives `𝖲 = (e^{ik}−1)L(0,h)2iv_h`,
and `S2-2body-S` (T.3) gives `𝖲 = i(χ/S)k + O(k²)` with `ρ = S`.
Equating the coefficients of `ik`: `L(0,h)·2iv_h = χ/ρ = 2χ/Z`, hence
`L(0,h) = −iχ/(Z v_h)`.
Justification: `S2-2body-S` (PROVED), ⟨1⟩1.⟨3⟩3, D24N-C1.

**⟨3⟩2.**  The exponent is over-determined, so this is not a one-point fit.
Write the candidate family `L_p(0,h) := −iχ/((2ρ)^p v_h)`, giving jet
`2χ(2ρ)^{-p}`.  Requiring it to equal `χ/ρ` at two distinct densities forces
`(2ρ)^p = 2ρ` for both, hence `p = 1`.  The corpus supplies **four**
densities (`S ∈ {1/2,1,3/2,2}`); a least-squares fit of `p` to the
ansatz-free data returns `p = 1.0024` (band `0.08`), and to the exact law
`p = 1` to `< 10^{-9}`.
Justification: named computation **D24N-C6**.

**⟨3⟩3.**  `Z = 1` at `ρ = 1/2` returns the frozen clause verbatim, so the
repair is conservative: it does not overturn D24(d)3, it scopes it.
Justification: (D24N.1) at `Z = 1`; D6 is a spin-`1/2` model (`S_x = σ_x/2`),
so the frozen O7–O9 constants and the paper's Theorem `thm:soft` are
untouched.

**⟨3⟩4.**  Independent corroboration from the memory side (no status
promotion): `1/Z = 1/(2ρ)` is exactly D13(a)'s frozen wall-position
normalisation `1/(2s)`, with `s = ρ` fixed by H-MQG(2) (`notation.md`
`ρ`-row).  The repaired multiplier `𝖲 = iχk·(2 sites)/(2ρ per site)` is
therefore the *same* charge-to-displacement conversion the memory half
already uses, which is the content of Conjecture `Bc`'s "`|q_hard|/s`", and
of the paper's phrase "the hard particle's `U(1)` charge in units of the
vacuum spin density" (`paper/main.tex:338–339`).
Justification: D13(a), `notation.md` `ρ`-row, claim `Bc`.  *Corroboration
only; `Bc` stays CONJECTURE.*

**⟨3⟩5. QED.**  □

### ⟨1⟩5.  Both lanes' stated justification is refuted (not merely undefended)

**⟨2⟩1. PROVE.**  The `(2ρN)^{-1/2}` route asserted by S1-A (F1(b)4) and by
S1-B ((B14) bullet 2) cannot produce the factor, for a reason stronger than
"wrong power".

**⟨3⟩1.**  `‖Q^-_k|Ω⟩‖² = ZN` is `N`-dependent (⟨1⟩2.⟨2⟩1.⟨3⟩2), while
`L(0,h)` is a factor in a thermodynamic-limit, `N`-free multiplier.  No
chain that terminates in an uncancelled `N^{±1/2}` can yield it.  On the
data's own ring sizes the gap `|(ZN)^{-1/2} − Z^{-1}|` never falls below
`0.185`.
Justification: named computation **D24N-C7**.

**⟨3⟩2.**  A leg *normalisation* cannot in any case generate the jet: the
charge-created descendant wave has chamber amplitudes `A = B = √Z` at
**every** `k`, hence `S_{12}^{desc} ≡ 1` and zero first jet.  The `k`-linear
term comes from `(e^{ik}−1)` with the coefficient fixed by the residue, i.e.
by the contact algebra (`μ = (2S−1)a + b`, `S2-2body-S` (T.2)), never by
normalising a leg.
Justification: direct construction of `Q^-_k|h⟩` in the normalised
occupation basis; `spin-s-twomagnon.md` ⟨1⟩2.⟨2⟩1 conventions.

**⟨3⟩3.**  The `N`-free invariant that *is* available from the same data is
`Z = ‖Q^-_k|Ω⟩‖²/N`, and it enters once, through the residue (⟨1⟩3).  This
is why the corrected value coincides with both lanes' arithmetic while none
of their arguments does.
Justification: ⟨1⟩3, ⟨3⟩1–⟨3⟩2.

**⟨3⟩4. QED.**  □

---

## 3. Acceptance check (fixed in advance by the work order)

Predicted jet `= 2/(2ρ)^p`, `ρ = S`, against the ansatz-free
`A_ring_summary` extrapolations (mean over the three `k_h` targets):

| `S = ρ` | measured (ansatz-free) | `1/S` | frozen `p=0` | rel. dev. | repaired `p=1` | rel. dev. |
|---|---|---|---|---|---|---|
| 1/2 | 1.9991 | 2.0000 | 2.0000 | 0.000 ✅ | 2.0000 | 0.000 ✅ |
| 1   | 0.9984 | 1.0000 | 2.0000 | 1.002 ❌ | 1.0000 | 0.002 ✅ |
| 3/2 | 0.6649 | 0.6667 | 2.0000 | 2.003 ❌ | 0.6667 | 0.003 ✅ |
| 2   | 0.4983 | 0.5000 | 2.0000 | 3.003 ❌ | 0.5000 | 0.003 ✅ |

Pre-registered decision band `0.08` (read from the data file, and the
checker fails if that band is moved).  Worst repaired deviation `0.0033`.
Fitted exponent `p = 1.0024`.

* reproduces **`1/S`** at `S ∈ {1/2,1,3/2,2}` — ✅
* reproduces **`2`** at `ρ = 1/2` — ✅ (exactly, `Z = 1`)
* leaves every other clause of D24(d) intact — ✅ for clauses 1, 2, 4, 5;
  **D24(c) must move** (§4), and D24(d) acquires a `ρ > 0` fence.

Note for the record: the two acceptance conditions are not independent —
`ρ = 1/2` *is* the `S = 1/2` member of the spin-`S` family.  What makes the
repair non-fitted is the *four*-density over-determination of the exponent
(⟨1⟩4.⟨2⟩1.⟨3⟩2), not the two anchors.

---

## 4. Blast radius

Every address below was obtained by grep, not by recall.

### 4.1 Text that MUST change (merge proposals in §5 for the first two)

| # | Address | What changes | Why |
|---|---|---|---|
| B1 | `definitions.md:960–961` — D24(d) clause 3 | split into (3a) hypothesis + (3b) derived value `−iχ/(Zv_h)`, still ONE numbered clause so the "five-condition" count is unchanged | the referral itself |
| B2 | `definitions.md:952–953` — D24(d) preamble | `𝒮_W` becomes `𝒮_W(ρ)`, a `ρ`-indexed family with the fence `ρ > 0` | `Z = 2ρ` appears in a defining clause; `ρ = 0` (admitted by D26) makes the flux singular and there is no type-B soft leg |
| B3 | `definitions.md:933` — D24(c), `𝔠_h(O)` | `− 2i χ(h,0) M_1^O(h)` → `− i(χ(h,0)/ρ) M_1^O(h)` | **required**: `𝔠_h` is *defined* to be the obstruction to the factorisation; if (d)3 gives jet `χ/ρ` and (c) keeps `2`, ML5-A becomes the criterion for a factorisation nobody claims |
| B4 | `definitions.md:938, 945` — the ML5-A criterion display and its `K_O` bound | `2iχ k M_1^O(h)` → `i(χ/ρ) k M_1^O(h)` (twice) | same reason as B3 |
| B5 | `claims/CLAIMS.md:41` — row **ML5-B** | status stays **PROVED**; statement re-scoped to the repaired constant, `ρ>0`, and the new certificate | the implication survives; its displayed conclusion changes |
| B6 | `claims/CLAIMS.md:40` — row **ML5-A** | status stays **PROVED**; add "the criterion is constant-agnostic and is now stated with the D24(c) constant `1/ρ`" | the proof (`ml5-universality.md` ⟨1⟩2) never uses the value |

### 4.2 Shard steps that must be re-typeset in lockstep (not this lane's files)

`theory/ml5-universality.md`:

| Step address | Current | Repaired |
|---|---|---|
| ⟨1⟩2, eq. (3) | `−2iχ(h,0)M_1^O(h)` | `−i(χ/ρ)M_1^O(h)` |
| ⟨1⟩2, eq. (4) and (4b) | `2iχ k M_1^O(h)` | `i(χ/ρ)k M_1^O(h)` |
| ⟨1⟩3 hypothesis 3 (line 142–144) | `L(0,h) = −iχ/v_h` | `L` defined as the quotient (D24N.3); `L(0,h) = −iχ/(2ρ v_h)`, `ρ>0` |
| ⟨1⟩3 eq. (5), boxed (line 155) | `2iχ k M_1^O(h)` | `i(χ/ρ)k M_1^O(h)` |
| ⟨1⟩3 ⟨2⟩1.⟨3⟩2 (line 170–172) | `L(k,h)=−iχ/v_h+O_I(k)` … `equals 2iχ kM_1^O` | `−iχ/(2ρ v_h)+O_I(k)` … `equals i(χ/ρ)kM_1^O`; the step is otherwise **verbatim**, needing only `Z>0` bounded away from 0 |
| ⟨1⟩3 ⟨2⟩3 (line 183–184) | "phase slope is `2χ` … Wigner displacement `2χ` sites" | "phase slope `χ/ρ` … displacement `χ/ρ` sites = `2χ` sites per unit `Z` of vacuum charge" |
| ⟨1⟩6 item 3 (line 324–327) | "signed Wigner coefficient `2χ`" | "signed Wigner coefficient `χ/ρ`, `=2χ` at `ρ=1/2`" |
| shard header (lines 3–10) | — | add the `tns-iu5` ERRATUM pointer, as `ml4-ward-reduction.md` does for its own erratum |

`theory/TRIANGLE.md:24, 215, 254, 257, 528` — `𝒮_W` references acquire the
`ρ` index; no numerical constant is displayed at any of those five lines
(verified by reading them), so the edit is a cross-reference refresh only.

### 4.3 Text that does NOT change (checked, do not "fix" it)

* `theory/oracle-bethe.md:299, 303, 320, 470` (O7/O8/O9) and
  `theory/soft-current-recon.md` (R14), (R17), (R18): all are **D6**
  statements, and D6 is spin-`1/2` (`definitions.md:348`, `S_x = σ_x/2`), so
  `ρ = 1/2`, `Z = 1`, and every displayed `2` is correct.
* `paper/main.tex:208` Theorem `thm:soft` (`δ = 2 sgn(v_h−v_s)k_s + …`) —
  same reason.  `paper/main.tex:71, 77, 288, 324, 338–344` already state the
  law as `1/s`/`|q_hard|/s`; the repair moves D24(d) **towards** the paper,
  not away from it.
* `paper/main.tex:244–252` (Conjecture S) — "the **five-condition**
  Ward-covariant no-contact class `𝒮_W`" stays correct because §5.2 keeps the
  count at five, and "Theorem 1 is its proved two-body instance,
  `𝖲 = 2ik_s`" stays correct because Theorem `thm:soft` is the `ρ = 1/2`
  member.  An *optional* one-word clarification ("its proved two-body
  instance at `ρ = 1/2`") is available but not required; likewise
  `paper/v2-claim-audit.md:112` and `theory/verdicts/paper-v2-r2.md:25`,
  which quote the count, need no edit.
* `definitions.md` D24(a), (b), (d)1, (d)2, (d)4, (d)5, (e), D25 — all
  constant-free or `ρ`-free; D24(e)'s `O_η` and `V_int` both have
  `M_1 = 0`, so the counterexamples are constant-independent and survive
  unchanged.
* `theory/checks/ml4_check.py` — its Ward rows (lines 213, 220) hardwire
  `2j*velocity`, which is the D6/spin-`1/2` (`Z = 1`) reading and stays
  correct; the `O_η` (line 299) and `V_int` (lines 312--330) obstructions
  both have `M_1 = 0` and therefore never see D24(c)'s constant.
* `theory/checks/spin_s_slope_check.py`, `numerics/results/*.json` —
  untouched; reused as ground truth.
* `claims/CLAIMS.md` rows `ML5`, `S2-2body`, `S2-2body-S`, `M-IDX-density`,
  `Bc`, `S-general` — no displayed constant that moves.  `S-general`'s
  obligation list is unchanged (microscopic `𝒮_W` membership is still open).

### 4.4 Is `𝒮_W` nonempty after the repair?

**No — nonemptiness remains OPEN, at every `ρ` including `ρ = 1/2`.**

Precisely:

* **Before** the repair, `𝒮_W` was *provably empty* in the spin-`S`
  ferromagnet register for every `ρ ≠ 1/2` (§1.3), and merely *not known to
  be nonempty* at `ρ = 1/2`.
* **After** the repair, the proof of emptiness is gone: the class's own
  prediction now agrees with the PROVED on-shell datum at every density, so
  no PROVED row refutes membership any more.
* But no source has been exhibited satisfying clauses 1, 4 and 5 at any
  density.  D24(d)'s own sentence — "no nontrivial microscopic class has
  been proved to satisfy all five conditions" — is untouched by this
  adjudication and must be retained verbatim in the merge.

So the referral converts *"provably vacuous off `ρ = 1/2`"* into *"not known
to be nonempty anywhere"*.  That is a strictly weaker negative and it
unblocks the D29/D30 merge (the merged shard may now carry `1/(2ρ)` with a
corpus citation instead of an undefended factor), but it does **not**
discharge bd `tns-axg`, which stays open exactly as written.

---

## 5. MERGE PROPOSALS

*The orchestrator applies these.  This lane did not edit either file.*

### 5.1 `definitions.md` — D24(c), lines 931–950

**REPLACE** (from `**(c) The contact first jet.**` through
`factorisation with the same stated norm control.`):

```
**(c) The contact first jet.**  With `χ(h,k) := sgn(v(h) − v(k))` and the
tail density `ρ > 0` of (d) below,

  `𝔠_h(O) := ∂_k M_2^O(k,h)|_{k=0} − i\,(χ(h,0)/ρ)\,M_1^O(h)`.

**Criterion (ML5-A; status in the claims DAG).**  On a linear source class
with `M_1^O ∈ L²(I)` and `M_2^O(k,·)` `C²` at `k=0` as an `L²(I)`-valued map,
the factorisation
`M_2^O(k,h) = i(χ/ρ) k M_1^O(h) + O_{L²(I)}(k²)` holds **if and only if both**

  `M_2^O(0,·) = 0`  and  `𝔠_h(O) = 0`

in `L²(I)`.  With
`K_O(ε) := (1/2)sup_{|q|≤ε}‖∂_q²M_2^O(q,·)‖_{L²(I)}`, Taylor's theorem gives
the exact control
`‖M_2^O(k,·) − i(χ/ρ)kM_1^O‖_{L²(I)} ≤ K_O(ε)|k|²`.
The stronger relative bound used in D24(b) requires the additional uniform
hypothesis `K_O(ε) ≤ C_I‖M_1^O‖_{L²(I)}`; it does not follow from `C²`
regularity alone.  On an affine class both displayed zero conditions must
hold on every source difference, and the base source must obey the full
factorisation with the same stated norm control.
**The criterion is constant-agnostic** — its proof
(`ml5-universality.md` ⟨1⟩2) evaluates at `k=0` and differentiates once, and
never uses the value.  The constant displayed here is the one derived in
(d)3b and must always be the same number as there (`tns-iu5`); at `ρ = 1/2`
it is the frozen `2`, which is the form in which (c) was first registered
and in which D24(e) and `theory/checks/ml4_check.py` test it.
```

### 5.2 `definitions.md` — D24(d), lines 952–973

**REPLACE** (from `**(d) The Ward-covariant no-contact class` through
`is part of the ML5-B future work.`):

```
**(d) The Ward-covariant no-contact class `𝒮_W(ρ)`.**  Fix a broken-symmetry
tail density `ρ := ω_α(S^z) > 0` (`notation.md`'s `ρ`-row; under (S) at both
tails and D26(INT), claim `M-IDX-density` gives `2ρ ∈ ℤ`, so the
order-parameter density `Z := 2ρ = ⟨Ω|[S^+_x,S^-_x]|Ω⟩` is a positive
integer).  `ρ = 0` is excluded: D26 admits it, but there is then no broken
order parameter, no type-B soft leg, and clause (3b) below is singular.  In
the fully polarised spin-`S` ferromagnet `ρ = S`.  `𝒮_W(ρ)` is the class of
sources satisfying all five of (clause 3 has a hypothesis part and a derived
part; the *count* of conditions is deliberately unchanged, so
`paper/main.tex:244` "five-condition" and the audit rows that quote it stay
correct):
1. *Exhaustive normed LSZ decomposition* — in `L²(I)`, `M_2^O` is exactly the
   sum of the descendant external-leg term `𝔈^O`, the orthogonal-current
   term, and the direct source/contact term named below; there is no
   additional reduced term, and the equality holds in the same packet norm
   as D24(b).
2. *Ward covariance* — the descendant current residue factorises as
   `2i v_h M_1^O(h)`.  On the fully polarised tail this residue is exactly
   linear in the order-parameter density,
   `⟨h|Q_0^†J^-_0|h⟩ = Z·(2iJ\sin h) = 2i v_h`, because `v_h = ZJ\sin h`;
   frozen `soft-current-recon.md` (R14) is the `Z = 1` reading of the same
   identity (named computation D24N-C3 in
   `theory/checks/d24d3_normalization_check.py`);
3. *Kinematic LSZ normalisation*, in two parts:
   **(3a) hypothesis** — the external flux factor
   `L(k,h) := 𝔈^O(k,h)/[(e^{ik}−1)\,2i v_h\,M_1^O(h)]`, well defined by
   clauses 1--2 wherever `M_1^O ≠ 0`, is process independent and uniformly
   `C¹`.
   **(3b) its value at zero, derived and not stipulated** —
   `L(0,h) = −iχ/(Z v_h) = −iχ/(2ρ v_h)`, so that ML5-B's multiplier is
   `𝖲(k;h) = i(χ/ρ)k + O(k²)`, i.e. signed Wigner displacement `χ/ρ` sites.
   This value is fixed by on-shell matching against the PROVED row
   `S2-2body-S` in the spin-`S` register (`ρ = S`) and transported by (3a);
   the exponent of `2ρ` is over-determined by `S ∈ {1/2,1,3/2,2}`.  At
   `ρ = 1/2` it is `−iχ/v_h`, the form in which this clause was frozen, and
   the multiplier is the frozen `2iχk`.  Adjudicated in
   `theory/verdicts/d24d3-adjudication-r1.md` (bd `tns-iu5`); certificate
   `theory/checks/d24d3_normalization_check.py`;
4. *Reduced-channel regularity* — the orthogonal current channel is
   `O_{L²(I)}(k²)` in the stated target limit, with the relative norm bound of
   D24(b).  Fixed-volume ML4 does not by itself supply a volume-uniform bound;
5. **No direct soft contact** — the amputated source commutator/contact term is
   bounded by `C_I|k|²‖M_1^O‖_{L²(I)}`.

Hypotheses 1 and 5 are the extra LSZ/contact content beyond the fixed-volume
Ward reduction, and by (c) the zero-intercept and zero-first-jet conditions
are necessary, not cosmetic.  Symmetry-generated external-leg insertions are
the intended seed, but **no nontrivial microscopic class has been proved to
satisfy all five conditions**; nonemptiness in the target scattering register
is part of the ML5-B future work.  The `tns-iu5` repair of clause 3 removed a
*proof* that `𝒮_W(ρ)` is empty for `ρ ≠ 1/2` — as frozen, clause 3 forced
soft slope `2` at every density, contradicting PROVED `S2-2body-S` — but it
supplies no member, so nonemptiness stays open at every `ρ` (bd `tns-axg`).
```

### 5.3 `claims/CLAIMS.md` — the ML5-B row (line 41)

**REPLACE** the whole row:

```
| ML5-B | Conditional implication on the five-condition D24(d) class `𝒮_W(ρ)`, including the exhaustive normed LSZ decomposition.  The implication is proved; its displayed conclusion is `M_2^O(k,h) = i(χ/ρ)k M_1^O(h) + O_{L²(I)}(k²)`, i.e. signed Wigner displacement `χ/ρ` sites, which at `ρ = 1/2` is the frozen `2iχ k M_1^O` / `2χ` sites.  **Re-scoped 2026-08-28 (bd `tns-iu5`):** the frozen D24(d)3 value `L(0,h) = −iχ/v_h` cancelled `v_h` in full and therefore forced slope `2` at EVERY tail density, contradicting PROVED `S2-2body-S` (`1/S`) and making `𝒮_W` provably empty for `ρ ≠ 1/2`.  Clause 3 is now split: 3a keeps the process-independence/`C¹` hypothesis with `L` DEFINED as the descendant quotient, 3b DERIVES `L(0,h) = −iχ/(2ρ v_h)` by on-shell matching to `S2-2body-S`, with `ρ > 0` and `Z = 2ρ ∈ ℤ` the order-parameter density.  The proof of the implication is unchanged apart from the constant (⟨2⟩1.⟨3⟩2 needs only `Z > 0`).  Nonemptiness and microscopic membership remain CONJECTURE/future work bd `tns-axg`, now at every `ρ` rather than only at `ρ = 1/2`. | PROVED | ML4-A, ML5-A, D24(d), S2-2body-S (for the clause-3b value) | theory/ml5-universality.md ⟨1⟩3; PROVED per corpus-r2.md adjudication (conditional implication); clause-3 repair adjudicated in theory/verdicts/d24d3-adjudication-r1.md | theory/checks/ml4_check.py local obstructions only; **theory/checks/d24d3_normalization_check.py** (D24N-C1--C7; green exit 0, `--red-frozen`/`--red-power`/`--red-halfpower`/`--red-ward` exit 1) |
```

### 5.4 ADVISORY (not requested by the work order; orchestrator's call)

Applying 5.1–5.3 without §4.2 would leave `theory/ml5-universality.md`
displaying a constant that `definitions.md` no longer holds — an L4 break.
Either apply §4.2's eight edits in the same commit, or add an ERRATUM block
at the head of `ml5-universality.md` in the style of
`ml4-ward-reduction.md`'s, pointing at this verdict.  Also add to
`claims/CLAIMS.md`'s ML5-A row the sentence "the criterion is
constant-agnostic; it is stated with D24(c)'s constant `1/ρ` since
`tns-iu5`."  I did not write those files.

---

## 6. HONEST STATUS

**H1 — PROVED (and independently recomputed here).**
`Z = 2ρ = ⟨Ω|[S^+_x,S^-_x]|Ω⟩`; `‖Q^-_k|Ω⟩‖² = ZN` for all `k`;
`ω_S(k) = 2JS(1−\cos k)` hence `v_S(h) = ZJ\sin h`;
`⟨h|Q_0^†J^-_0|h⟩ = Z·2iJ\sin h = 2iv_S(h)` exactly at `2S = 1,2,3,4`;
the frozen `L(0,h) = −iχ/v_h` makes ML5-B's jet identically `2χ`,
independent of `ρ` and of `v_h`; the exact spin-`S` phase slope is `1/S`
(my ansatz-free ED, `≤3.2%` at my `N` ladder, `≤0.43%` on the frozen
`N ≤ 480` ladder, and `|δ_ED − arg S_{12}| ≤ 1.6·10^{-12}`).

**H2 — DERIVED BY MATCHING (the adjudicated value).**
`L(0,h) = −iχ/(2ρ v_h)`.  Its provenance is: `L` defined as the descendant
quotient (⟨1⟩1, forced by D24(d)1–2), evaluated in the spin-`S` register
against the PROVED row `S2-2body-S`, and transported by clause 3a's
process-independence hypothesis.  It is *not* a fitted constant: the
exponent of `2ρ` is over-determined by four densities and the `ρ = 1/2`
member reproduces the frozen clause exactly.  It is also *not* a
first-principles derivation of the LSZ decomposition.

**H3 — STRUCTURAL IDENTIFICATION, not proof.**
⟨1⟩3.⟨3⟩4 — "the residue pairs two order-parameter insertions, hence carries
`Z` once, hence the flux divides by `Z` once" — is a reading that correctly
*predicts* the measured power, is consistent with the type-B Goldstone
normalisation of `refs/arxiv-1203.0609` (`ρ_{ij} = −i⟨0|[Q_i,j^0_j]|0⟩`,
`m = ⟨j^0_z⟩` for the ferromagnet), and is verified in its checkable part
(the residue's exact `Z`-linearity, D24N-C3).  It is not a derivation of
D24(d)1.  A genuine LSZ derivation of the descendant decomposition is still
the open lemma named in `ml5-universality.md`'s EXPLORATION ML5-W and in
bd `tns-axg`.

**H4 — REFUTED.**
(i) The frozen D24(d)3 as a *universal* statement.
(ii) Both S1 lanes' stated justification for `1/(2ρ)`: the `(2ρN)^{-1/2}`
route is `N`-dependent and cannot appear in an `N`-free multiplier
(D24N-C7), and a leg normalisation cannot generate a jet at all, since the
charge-created descendant has `S_{12}^{desc} ≡ 1` at every `k`
(⟨1⟩5.⟨2⟩1.⟨3⟩2).  Their *arithmetic* was right; their *reason* was not.
(iii) Value-fixing by stipulation — consistent with, and now extended into
`definitions.md` from, `soft-index-adjudication-r1.md` §3.2.

**H5 — CONDITIONAL, and the one place a critic should push.**
The emptiness argument of §1.3 rests on the corpus's identification of the
D24(d) soft multiplier's jet with the two-body physical phase jet
((R17)/`ml5-universality.md` ⟨1⟩4.⟨3⟩4/O9).  That bridge is not a PROVED
row.  §1.4 shows both horns condemn the frozen clause, but a critic who
rejects the bridge should read §1.3's "empty" as "empty in the only register
the corpus can compute in".

**H6 — EVIDENCE, not proof.**
The four-density acceptance table is numerical (ansatz-free ED, extrapolated,
pre-registered `8%` band).  The exactness claims (H1) are machine-precision
identities at finite `N`, not `N → ∞` theorems.  The `S2-2body-S` input is
exact and PROVED; the extrapolation is what carries residual error.

**H7 — NOT claimed.**
Nothing here promotes `S-general`, `Bc`, `M-quant`, or `S-INDEX`; nothing
here supplies a member of `𝒮_W(ρ)`; nothing here touches the `|q_hard| > 1`
factor (`tns-ebh`) or the `n ≥ 2` Ward erratum (`tns-uxr`).  `𝖲`'s
universality remains `S-general` (CONJECTURE), and D25 is unchanged.

---

## 7. Certificate

`theory/checks/d24d3_normalization_check.py`, 382 loc, no bare `assert`,
every failure `SystemExit(1)`.

```
D24N-C1 frozen_jet_coefficient=2*chi repaired=chi/rho
D24N-C2 Z=2rho max_error=8.882e-16
D24N-C3 Ward residue = Z*2iJ sin h, max_error=4.814e-15
D24N-C4 ansatz-free slopes vs 1/S: max_rel_dev=0.0043 (band 0.08)
D24N-C5 frozen-clause relative deviations at S=1/2,1,3/2,2: 0.000, 1.002,
        2.003, 3.003  -> defect size 3.003
D24N-C6 repaired-clause max_rel_dev=0.0033, fitted exponent=1.0024
D24N-C7 half-power route gap=1.855e-01
PASS: D24(d)3 repaired normalisation L(0,h) = -i chi / (2 rho v_h)
```

| mode | exit | first failure |
|---|---|---|
| green, `python3 -O` | **0** | — |
| `--red-frozen` (the frozen `ρ`-blind constant) | **1** | `D24N-C6 … misses the band at S=1.0 dev=1.0016; S=1.5 dev=2.0027; S=2.0 dev=3.0033` |
| `--red-power` (`1/(2ρ)²`) | **1** | `D24N-C6 … at S=1.0 dev=0.4984; …` |
| `--red-halfpower` (`1/(2ρ)^{1/2}`, both lanes' power) | **1** | `D24N-C6 … at S=1.0 dev=0.4158; …` |
| `--red-ward` (residue scales as `Z²`) | **1** | `D24N-C3 Ward residue Z-scaling error 1.697e+01` |

`--red-frozen` fails **at `S = 1`** as the work order demands, not only at
the largest spin; D24N-C5 additionally requires the frozen constant to miss
the band *at each of* `S = 1, 3/2, 2` separately and to *hit* it at
`S = 1/2`.

Mutation tests were run on **copies in the scratchpad** (`--data` accepts a
copy of the ground-truth file), confirming the acceptance test is not
self-fulfilling:

| mutant (copy) | exit | died at |
|---|---|---|
| `A_ring_summary` `S=1` slope forced to `2.0` | 1 | `D24N-C4 ansatz-free slope deviates from 1/S by 1.0000` |
| `decision_band` moved `0.08 → 0.5` | 1 | `D24N-C4 decision band moved: 0.5` |
| data file absent | 1 | `D24N-C4 missing ground-truth file` |

---

## 8. Disposition

* Apply §5.1–5.3 to `definitions.md` and `claims/CLAIMS.md`.
* Apply §4.2 (or the ERRATUM alternative of §5.4) to
  `theory/ml5-universality.md` in the same commit — do not ship 5.1–5.3
  alone.
* bd `tns-iu5`: the referral is **adjudicated**; close it on merge, and
  record in `HANDOFF.md` that the corpus-damage line "(3) Frozen `𝒮_W` empty
  for `ρ≠1/2`" becomes "repaired; `𝒮_W(ρ)` nonemptiness open at every `ρ`".
* bd `tns-axg`: **stays open, unchanged.**  The repair does not supply a
  member.
* bd `tns-v44` (unified S1 r2): unblocked on this axis.  The r2 shard may
  now cite D24(d)3b for `1/(2ρ)` instead of carrying it as a displayed
  hypothesis, and must cite it — neither lane's own justification survives
  (§H4(ii)).
