<!-- ROLE: L6 critic verdict, round 2, on theory/oracle-bethe.md (499 lines) +
     theory/checks/oracle_bethe_check.py (373 lines) + definitions.md D8.
     Critic: Opus. Date: 2026-08-25. Predecessor: oracle-bethe-r1.md (FAIL, 5 MAJOR). -->

# Critic verdict r2 — `theory/oracle-bethe.md` (Bethe oracle O1–O10)

Critic: Opus (adversarial pass, L6, round 2). Date 2026-08-25.
Method: each r1 MAJOR re-attacked on its own terms rather than read for
compliance — the new remainder-bound constants recomputed numerically, the new
O5 existence/uniqueness argument checked step by step against an independent
ED, every boxed equation re-derived again for regression (including the new
`χ`-carrying (12)/(13) and the new `|v_h|` form of (15)), the revised checker
run normally and under `-O` and mutation-tested six ways, D8's amendment traced
across every sibling shard, and the ML2 singular-state matrix element
cross-checked against the `K=π` sector of my own ED.

---

## Part I — adjudication of the r1 objections

### MAJOR 1 (scattering-length misnomer) — **FIXED**

⟨1⟩3.⟨2⟩4.⟨3⟩1 now calls `2χ` the *signed Wigner phase-slope / spatial-displacement
coefficient* and says outright "The physical linear coefficient is `2χ`, not an
invariant hard-independent `2`". ⟨3⟩3 states "The number `2` is not a scattering
length", derives `δ₁₂/ε → 2xy/(y−x)` in the joint soft limit, concludes "no
nonzero relative-momentum scattering length exists", and cites both local TeX
sources by file *and line* (`arxiv-1312.6793` l.102 for the
`φ ≈ −a(κ₁−κ₂)` definition, `arxiv-1602.08692` l.656 for the vanishing FM
value), with the explicit disclaimer "No numerical comparison with the spin-1
antiferromagnet is implied" — which is precisely the trap r1 warned against.
O9 carries the same wording. I re-verified the joint-soft limit independently
(`ε = 10⁻²…10⁻⁴`): `δ/ε → 4.000`, `2.500`, `−1.333` for `(x,y) = (1,2), (1,5),
(−1,2)` against `2xy/(y−x) = 4, 2.5, −4/3`. Correct, and correctly interpreted.

### MAJOR 2 (the linear coefficient carries `sgn(v_h − v_s)`) — **FIXED**

The sgn-carrying form is now primary: ⟨1⟩3.⟨2⟩1 defines
`χ := sgn(v_h − v_s)`, `S_phys := S₁₂` if `χ=+1` else `S₂₁`, and (12)/(13) are
stated as
`δ_phys = 2χk_s + (|v_h|/ω_h)k_s² + R_δ`,
`S_phys = 1 + 2iχk_s + [i|v_h|/ω_h − 2]k_s² + R_S`. O7/O8/O9 match.

I re-derived both independently rather than accepting the substitution.
For `k_h < 0` the physical channel is `S₂₁ = S₁₂^{-1}`; expanding the *inverse*
series gives coefficients `1`, `−2i`, and (at `k_h = 1.10`, evaluated exactly)
`−2 + 1.6310i`, against `cot(|k_h|/2) = cot(0.55) = 1.63104` — i.e.
`i|v_h|/ω_h − 2` with `χ = −1`. Numerically at `J=1` for
`k_h ∈ {−2.4, −1.1, −0.37, 0.37, 1.1, 2.4}` and `k_s = ±10⁻³`,
`δ_phys − (2χk_s + |v_h|/ω_h k_s²)` divided by `|k_s|³` is
`0.424, 0.830, 13.81` in magnitude (even in `k_h → −k_h`), matching the cubic
coefficient `cos k_h/(1−cos k_h)` — so (12) holds on the full `0<|k_h|<π`, not
merely on D8's half-zone.

(15) is now the even form `|v_h|/ω_h = (2J−ω_h)/|v_h| = √((2J−ω_h)/ω_h)`, with
`= cot(k_h/2)` demoted to a D8 specialization. I checked all three forms agree
to `4e−15` at `|k_h| ∈ {0.2, 0.9, 1.7, 2.6, 3.1}` for **both** signs of `k_h`,
and confirmed that the r1-objected `v_h/ω_h` would be wrong-signed for `k_h<0`.
⟨2⟩4.⟨3⟩4 adds the parity statement `δ_phys(−k_s,−k_h) = δ_phys(k_s,k_h)`,
which the checker also enforces (`parity=1.735e−18`).

The domain widening is handled cleanly: D8 still says `k_h∈(0,π)` and "a hard
momentum outside this half-zone is not included **unless explicitly stated**";
⟨1⟩3.⟨2⟩1 explicitly states it. No smuggling.

### MAJOR 3 (no quantifier / remainder bound) — **FIXED, and the rate is right**

⟨1⟩3.⟨2⟩3.⟨3⟩3 now constructs an explicit compactum
`ε_ab := ½min{a, π−b, sin a, sin b}`,
`D_ab := {(q,h) : |q| ≤ ε_ab, a ≤ |h| ≤ b}`, defines
`C_δ := ⅙ max_{D_ab}|∂_q³δ_phys|`, `C_S` likewise, asserts
`|R_δ| ≤ C_δ|k_s|³`, `|R_S| ≤ C_S|k_s|³`, and claims `C = O(a^{−2})` as `a↓0`.
⟨2⟩5.⟨3⟩3 does the analogous job for (16)–(17) with `D_δ, D_S` and
`Ω_ab := J(1−cos ε_ab)`.

I checked every load-bearing piece rather than the shape of the claim:

* The rewriting `1/Δλ = 2 sin(q/2) sin(h/2)/sin((h−q)/2)` is **exact** (sympy
  residual `0`). It is the right move: it removes the removable singularity at
  `q=0` where `λ(q) = ½cot(q/2)` blows up, which is what makes `δ_phys`
  manifestly `C^∞` across `k_s = 0`.
* The bound `|sin((h−q)/2)| ≥ a/(2π)` on `D_ab` is correct. My derivation:
  `ε_ab ≤ a/2` gives `|h−q| ≥ a/2`; `ε_ab ≤ (π−b)/2` gives
  `|h−q| ≤ (π+b)/2 < π`, so `|(h−q)/2| < π/2` and
  `|sin((h−q)/2)| ≥ sin(a/4) ≥ (2/π)(a/4) = a/(2π)`. Numerically over `D_ab`
  for `a ∈ {0.05, 0.1, 0.2, 0.4, 0.8}`, `b = 3.0`: measured minima
  `0.0125, 0.0250, 0.0647, 0.1640, 0.3567` vs `a/(2π) =
  0.0080, 0.0159, 0.0318, 0.0637, 0.1273` — the bound holds in every case with
  room to spare.
* `ε_ab` is correctly *designed*, not merely stated: the `½sin a`, `½sin b`
  entries are exactly what forces `|sin q| < |sin h|`, hence `χ` constant on
  each component of `D_ab` — without which (12)'s `2χk_s` would be ill-posed.
  I checked this is why those two entries are there; they are load-bearing.
* The `O(a^{−2})` rate is **correct**, which is the part I most expected to
  fail. Measured `C_δ(a, 3.0)` by a 5-point third-derivative stencil over the
  whole of `D_ab`:

      a = 0.05 → C_δ = 12575.4,  C_δ·a² = 31.44
      a = 0.10 → C_δ =  2981.4,  C_δ·a² = 29.81
      a = 0.20 → C_δ =   253.7,  C_δ·a² = 10.15
      a = 0.40 → C_δ =    22.41, C_δ·a² =  3.59

  `C_δ·a²` plateaus at ≈ 30 in the `a↓0` regime (the drift at larger `a` is
  just `ε_ab` saturating at `½(π−b)`), so `C_δ = Θ(a^{−2})` exactly as claimed.
* `D_δ, D_S` are finite. Measured over `a ≤ k_h ≤ b`, `σ = ±1`,
  `0 < ω ≤ Ω_ab`: `D_δ(0.37,3.0) = 29.51`, `D_S(0.37,3.0) = 35.79`;
  `D_δ(1.0,3.0) = 2.229`, `D_S = 6.922`; `D_δ(0.2,3.0) = 131.9`.
  Finite, and growing as `a↓0` consistently with the `C = O(a^{−2})` picture.

Defining the constant as the max of the quantity it bounds is unilluminating
but not circular — it is the standard Taylor–Lagrange constant, and the
non-trivial content (finiteness, and the `a^{−2}` rate) is supplied and true.

### MAJOR 4 (bound-state ansatz / O5 domain) — **FIXED**

⟨1⟩2.⟨2⟩8.⟨3⟩2 now derives rather than assumes: the bulk recursion has
characteristic polynomial `Jc t² − (2J−E)t + Jc` whose roots have product one,
so `ℓ²(ℕ)` forces the single root with `|t|<1` and hence `f_r = Ct^{r−1}`; the
justification explicitly disposes of the unit-circle case "including a repeated
root". I checked the algebra (`Jc t² − (2J−E)t + Jc = 0` from `f_r = t^r`,
product of roots `= 1`) and the exclusion argument (`|t|=1` ⇒ `A t^r + B t̄^r`
never `ℓ²`; `t = ±1` repeated ⇒ `t^r, r t^r` neither `ℓ²`). Sound and complete.
⟨3⟩3 then gets `t = c`, `E = J(1−c²) = J sin²(K/2)` uniquely (sympy returns the
single root `cos(K/2)`) and states existence *and* uniqueness up to scale.

The r1 domain mismatch is gone: ⟨3⟩4 handles `|K| = π` separately and
correctly. At `c = 0` the recursion decouples; below the bulk level `2J` the
only solution is `f_1 ≠ 0`, `f_{r≥2} = 0`, `E = J = J sin²(π/2)`. O5 now reads
"Canonical `0<|K|≤π`; threshold at `K=0`; `|K|=π` included", matching the proof.
⟨3⟩6 disposes of the mod-`2π` representatives r1 flagged. ⟨3⟩5 now states the
`c ≥ 0` hypothesis that makes `cos p = 1` the continuum minimizer.

Independent ED confirmation (`N = 18`, momentum-projected): at `K = π` the
sector has dimension 8, containing exactly **one** level below `2J`, at
`1.370000000000 = J`, with the remaining seven degenerate at `2J` — the flat
`K=π` continuum. At `K = 8·2π/18` the level is `1.328689445237` vs
`J sin²(K/2) = 1.328689445238`.

### MAJOR 5 (checker coverage; `-O`) — **FIXED**

All `assert`s are gone, replaced by `require()` → `fail()` → `raise SystemExit(1)`.
Coverage is now genuine, not claimed:

| fact | r1 | r2 |
|---|---|---|
| O1 `ω, v` | partial | `check_one_magnon`: independent 1-magnon block + Richardson `v(k)` |
| O2/O3/O4 | yes | unchanged, still ED-backed |
| **O5** | **no** | `check_bound_states`: translation-operator momentum projection, level-below-continuum and ground-state-of-sector assertions |
| **O6** | **no** | `check_soft_oracle`: `|S_phys(0,k_h) − 1|` and `|phase(0)|` |
| O7/O8 | vs (6) | now for **both signs of `k_h`**, with `2·sgn` and `|v_h|/ω_h` |
| **O9 identity** | **no** | `invariant_error` checks `|v_h|/ω_h = √((2J−ω_h)/ω_h) = cot(|k_h|/2)` |
| **O10** | **no** | `check_puiseux`: both remainders after division by `ω_s^{3/2}`, both `σ` |
| parity | — | new |

Both runs reproduce byte-identically and exit `0`:

    ONE residual=2.190e-15 velocity=4.694e-12
    RAPIDITY S12_error=2.483e-16 S21_error=1.570e-16
    ED ... residual=2.585e-15 (max) spectral=2.220e-15 (max)
    BOUND K=2.792526803191 level=1.328689445237 exact=1.328689445238 error=8.802e-13
    BOUND K=3.141592653590 level=1.370000000000 exact=1.370000000000 error=1.110e-15
    SOFT limit=2.966e-16 linear=3.084e-10 quadratic=1.250e-09 invariant=4.441e-15
         parity=1.735e-18 remainder_ratio=1.658e+01
    PUISEUX phase_ratio=2.545e+01 S_ratio=3.036e+01
    PASS: oracle facts O1--O10

I mutation-tested a copy in `/tmp/.../scratchpad/` (repo untouched). **Six
independent mutations all go red, and all go red under `-O` too**, exiting `1`
with no `PASS` line:

| mutation | caught by |
|---|---|
| outer sign of (6) flipped | `O4 rapidity identities: direct=2.0` |
| `hamiltonian[row,col] -= J/2` → `+=` | `O1 one-magnon residual: 2.5747…` |
| **`physical_scattering` branch forced to `S₁₂`** | `O7 signed linear phase: 4.000…` |
| `exact` bound energy × `1+10⁻⁷` | `O5 bound energy K=2.79…: 1.33e−07` |
| Puiseux coefficient `2v_h/(Jω_h)` → `4v_h/(Jω_h)` | `O10 phase remainder: 4737.0` |
| **`abs(velocity_h)` → `velocity_h` in curvature** | `O7 quadratic phase: 10.687` |

The last two mutations are the important ones: they are the *specific* r1
MAJOR-2 repairs, and the checker detects both. The `-O` hole is closed.

The shard is also honest about what the numerics do *not* do: "Bound-state
uniqueness and the incoming/outgoing reading remain the analytic arguments
above, not numerical assumptions." That is exactly right — no measurement can
test D7's channel convention.

### r1 MINORs and NOTEs

| r1 id | status |
|---|---|
| 6 (wrong cross-references) | **FIXED** — now fully qualified `⟨1⟩1.⟨2⟩3.⟨3⟩2` (l.98, l.130) and `⟨1⟩1.⟨2⟩4` (l.117) |
| 7 (symbols missing from the symbol table) | **HALF-FIXED** — D8 now defines `ω_h, v_h, ω_s, v_s, σ`; `notation.md` not updated. See residue 2 |
| 8 (`-O`) | **FIXED** — see MAJOR 5 |
| 9 (dangling "quoted" referent, vacuous "positive rapidity") | **FIXED** — ⟨2⟩7.⟨3⟩4 now says "A source using `λ↦−λ`, or the reversed channel, may display the inverse fraction; the distinction is algebraic and does not depend on the sign of `λ`" |
| 10 ("precisely when") | **FIXED** — ⟨2⟩6.⟨3⟩3 now gives the quantitative `\|k_s^{sing}\|≍\|k_h\|` and adds "The complex singular point is not itself the real bound state" |
| 11 (`k_s=k_h` null vector) | **FIXED** — stated in ⟨2⟩6.⟨3⟩2 *and* in O3's domain column |
| 12 (`k_h→π` caveat not in the O-table) | **FIXED** — O7 and O9 domain columns now carry it |
| 13 ("Dyson/Adler zero") | **FIXED** — replaced by "the mathematical soft-zero statement is simply `S₁₂−1→0`; no named low-energy theorem is needed here" |
| 14 (closed form missing) | **FIXED** — (11a) `δ₁₂ = 2 arctan(1/Δλ)` promoted into ⟨2⟩3 and into O4; I re-verified it to 30 digits at four kinematic points including `\|δ\|>1` |
| 15 (soft check not independent of (6)) | **PARTLY ADOPTED** — coverage is much wider; the finite-size-level extraction was not added, but the shard no longer claims independence it does not have |
| 16 (ill-conditioned degree-6 polyfit) | **FIXED** — replaced by Richardson-extrapolated central differences |
| 17 (⟨1⟩4 a proof step containing a transcript) | **FIXED** — the O-table is now ⟨1⟩4 (and the theorem's PROVE points at it); the transcript sits in a "Numerical record (non-deductive)" section outside the theorem |
| 18 (numerator nonzero) | **FIXED** — ⟨2⟩6.⟨3⟩2: "The numerator can vanish for real momenta only at the excluded point `k_1=k_2=0`" |

### Regression on (1)–(17)

All eighteen tags `(1)…(11), (11a), (12)…(17)` are present exactly once, no
gaps, no duplicates; 13 boxed displays. (2), (4), (6), (7), (8), (9), (10),
(11), (14), (16), (17) are textually unchanged from r1 and were re-verified
then. (12), (13), (15) changed and were re-derived from scratch above. (11a) is
new and exact. **No regression.**

### D8 amendment / cross-shard integrity

D8's edit is purely additive (`ω_h`, `v_h`, `v_s` named; a remark that
`v_h > v_s` for small `|k_s|`) and therefore cannot break any consumer. The two
other shards that `ASSUME D6--D8` — `soft-current-recon.md` (l.3, l.21) and
`ml2-completeness.md` (l.13) — are unaffected. What *did* change is O7/O9, and
four sibling shards still cite their r1 wording; see residue 4.

### ML2 cross-check

`ml2-completeness.md` (24)'s coefficient is exact: on the stated representative
`k_s + k_h = π`,
`e^{ik_h} + e^{ik_s} = 2e^{i(k_h+k_s)/2}cos((k_h−k_s)/2) = 2i cos((k_h−k_s)/2)`,
and the shard does fix the representative ("choose the congruent
representatives with `k_s+k_h=π`"), which it must — at `k_s+k_h = −π` the
prefactor is `−i`.

Consistency with the oracle: ML2 says the D7 family fails to span at `K ≡ π`
for even `N`, by exactly one state `|χ_π⟩`. My ED locates that deficiency
precisely inside the **seven-fold degenerate block at `E = 2J`** in the `N=18`,
`K=π` sector — the flat `K=π` continuum — while the oracle's O5 endpoint is the
*isolated* level at `E = J` below it. The two shards therefore meet at `K=π`
without colliding: ML2's singular leaf is a continuum-level completeness gap,
O5's `|K|=π` claim is a below-continuum bound state, and
⟨1⟩2.⟨2⟩8.⟨3⟩4's "below the bulk level `2J`" is exactly the qualifier that
keeps them apart. No inconsistency. (Suggestion, residue 9.)

---

## Part II — residue

### 1. MINOR — the "Numerical record" block is not the transcript it is presented as

**Location:** shard lines 489–499.

"A fresh normal and `python3 -O` run on 2026-08-25 recorded:" introduces a
```text fence which is **not** what the script prints. Actual output has an
`oracle_bethe_check: N=18, dim=153, J=1.37` header, a `RAPIDITY
S12_error=2.483e-16 S21_error=1.570e-16` line, *three* per-root `ED` lines,
*two* per-`K` `BOUND` lines, and a `SOFT` line ending
`remainder_ratio=1.658e+01`. The fenced block silently aggregates the ED and
BOUND lines into invented `max_…` fields, drops the header, drops the RAPIDITY
line entirely, and drops `remainder_ratio`.

Every retained number is a *correct* maximum of a real run — I verified
`2.585e-15`, `2.220e-15`, `8.802e-13`, `3.656e-15` and all five SOFT/PUISEUX
values against my own run — and the run does pass. So nothing scientific is
wrong, which is why this is MINOR and not MAJOR. But the r1 record reproduced
digit-for-digit and this one does not, and this is the one section of the shard
whose entire job is evidentiary. Paste the real output, or reword to
"aggregated from the run".

The following sentence compounds it: "The enforced tolerances are respectively
`1e−10`, `2e−11`, `2e−11`, `3e−9`, and `40`." On the ONE line, `1e−10` governs
only the velocity; the residual uses `ED_TOL = 2e−11`. On the SOFT line,
`3e−9` (`DERIVATIVE_TOL`) governs only `linear` and `quadratic`; `limit`,
`invariant` and `parity` use `BETHE_TOL = 2e−11` and `remainder_ratio` uses a
**hardcoded `1.0e2`** that the sentence does not mention. The RAPIDITY check
(`BETHE_TOL`) is absent from both the block and the list.

### 2. MINOR — `notation.md` still lacks the symbols the shard uses (r1 #7, half-fixed)

D8 now names `ω_h, v_h, ω_s, v_s, σ` — good. But `notation.md`'s row for the
soft-limit symbols is unchanged (`k_s, k_h, ω_s, σ`), and the table has **no**
entry for `ω_h`, `v_h`, `v_s`, `χ`, `δ_phys`, `S_phys`, or `Δλ` — all of which
appear in boxed equations (12), (13), (15) and in the O-table (O4, O7, O8, O9).
`notation.md` ends "a symbol used anywhere without an entry here is a defect",
so this is a defect by the repo's own rule. It was flagged in r1 and only half
repaired.

### 3. MINOR — `definitions.md`'s header contradicts the amendment it now contains

`definitions.md` lines 3–5 still read "D6-D8 belong to the Bethe oracle and are
**FROZEN** -- do not edit them", yet D8 was edited this round (as the prover was
instructed to). `notation.md` handles the analogous situation correctly, with a
dated "Revision r2/r3 (2026-08-25)" note saying what changed and that nothing
was renumbered. D8 needs the same: either lift FROZEN with a dated amendment
note, or re-freeze it explicitly as of r2.

### 4. MINOR — four sibling shards still cite the r1 wording of O7/O9

Not the prover's fault (its brief forbade touching those files), but it must not
be lost:

* `theory/corner-b-draft.md:452` — "the magnon–magnon oracle (`O7`: `δ = 2k_s + …`)"
* `theory/corner-b-draft.md:728` — "`dδ/dk_s = 2` (`O7`)"
* `theory/soft-current-recon.md:376` — "O7--O9, including the D7 sign and the **hard-independent linear coefficient**"
* `theory/corner-a-goldstone.md:390, 398` — "O7's hard-independent linear coefficient `2`"; "hard-independent, matching O9"

None is *false* — all four work on D8's half-zone, where `χ = +1` — but O7/O9
no longer say what they quote, and "hard-independent" is precisely the phrase
r2 removed. File a `bd` issue to re-word them as "on D8, O7 reduces to
`δ = 2k_s + …`".

### 5. MINOR — the two remainder tolerances are magic numbers uncoupled from `C_δ`, `D_δ`

`PUISSEUX_TOL = 4.0e1` and the hardcoded `1.0e2` in `check_soft_oracle` are
calibrated to the sampled set `k_h ∈ {0.37, 1.10, 2.40, 3.00}` and to
`|k_s| ≤ 0.016`, not to the shard's `C_δ(a,b)` / `D_δ(a,b)`. My measurements:
`D_δ(0.37, 3.0) = 29.51`, `D_S(0.37, 3.0) = 35.79` against the checker's
`25.45` / `30.36` and a tolerance of `40` — a ~30% margin. Adding a smaller
hard momentum (`a = 0.2` gives `D_δ = 131.9`) would red the check for reasons
that have nothing to do with correctness. Either derive the tolerance from
`a = min(hard)` or add a comment saying it is calibrated to this sample.

### 6. MINOR — the `R_S` bound needs the integral form of the Taylor remainder

⟨1⟩3.⟨2⟩3.⟨3⟩3 justifies both `|R_δ| ≤ C_δ|k_s|³` and `|R_S| ≤ C_S|k_s|³` by
"Taylor's theorem". That is fine for the real `δ_phys` (Lagrange form) but
Lagrange's mean-value form fails for the **complex-valued** `S_phys` as a
function of a real variable. The bound is nevertheless correct via the integral
remainder, `|R_2(x)| = |∫₀^x (x−t)²/2 · f'''(t)dt| ≤ ⅙ max|f'''| |x|³`. One
clause fixes it.

### 7. MINOR — O7 as printed reads as if its coefficient depended on `k_s`

O7 states `δ_phys = 2 sgn(v_h−v_s)k_s + …`, and `v_s = v(k_s)`. Read literally,
the linear coefficient is a function of the expansion variable. It is in fact
constant on `D_ab` — this is exactly what the `½sin a`, `½sin b` entries of
`ε_ab` buy, and ⟨2⟩3.⟨3⟩2 silently uses the constant value `χ = sgn(k_h)`. Either
write O7 with `2 sgn(k_h)`, or add "χ is constant on `D_ab`" to the domain column.

### 8. NOTE — the soft-derivative check is roundoff-limited with a <3× margin

`quadratic = 1.250e−09` against `DERIVATIVE_TOL = 3e−9` uses 42% of the budget.
Richardson-extrapolated second differences at `h = 2e−3` have a roundoff floor
of about `ε/h² ≈ 2.2e−16/4e−6 ≈ 5.5e−10`, so this is float noise, not
truncation — and it cannot be improved by shrinking `h`. It is a genuine
improvement on the r1 degree-6 polyfit (which was ill-conditioned), but if the
tolerance is ever tightened it will fail for numerical, not physical, reasons.
Consider `mpmath` at 30 digits for this one check, or widen to `1e−8` with a
comment.

### 9. NOTE — add a one-line ML2 cross-reference at `|K| = π`

⟨1⟩2.⟨2⟩8.⟨3⟩4 and `ml2-completeness.md` (23)–(24) meet at exactly `K = π` and
say complementary things (isolated level at `E = J` below the continuum vs. a
completeness gap inside the degenerate block at `E = 2J`). I verified they do
not collide. A single sentence in ⟨3⟩4 — "the `E = 2J` degenerate block at
`K = π` is where ML2's non-D7 singular state lives; it is not below the
continuum edge and does not affect (9)" — would save the next reader the ED run
I just did.

### 10. NOTE — (11a) is exact, not merely local

O4 says "locally `δ₁₂ = 2 arctan(1/Δλ)`". It is in fact an identity wherever
`|δ₁₂| < π`, i.e. everywhere off the `k_s = k_h` locus (I confirmed to 30
digits at `(0.4, 1.3)` and `(−1.1, 1.47)`, where `|δ| ≈ 1.01` and `1.26`). The
"locally" undersells a fact the campaign will want globally.

### 11. NOTE — O6's domain is narrower than its proof

(11) holds verbatim for all `0<|k_h|<π` (the denominator `1−e^{ik_h}` never
vanishes there), but O6's column still says "D8: fixed `k_h∈(0,π)`", making it
the only O-fact in O6–O9 not widened. Harmless, but asymmetric.

### 12. NOTE — `PUISSEUX_TOL` is misspelled (should be `PUISEUX_TOL`).

---

## Summary verdict

**PASS** — all five r1 MAJORs are substantively fixed, not merely re-worded: I
independently reconfirmed the joint-soft-limit `2xy/(y−x)` behind the
scattering-length reconciliation, re-derived the `χ`-carrying (12)/(13) from
the inverse series for `k_h<0` and verified the even form of (15) at both signs
of `k_h`, measured `C_δ(a,3.0)·a² ≈ 30` (confirming the claimed `O(a^{−2})`
rate) and checked the exact `1/Δλ` rewriting and the `a/(2π)` denominator bound
that carry it, audited the new `ℓ²`-based bound-state existence/uniqueness
argument and confirmed O5's corrected `0<|K|≤π` domain against my own
momentum-resolved ED (`E = J` isolated below a 7-fold `2J` block at `K=π`), and
mutation-tested the rebuilt checker six ways — including the two mutations that
target precisely the new claims — with every one going red under **both** normal
and `python3 -O` invocation. Equation tags `(1)`–`(17)` plus `(11a)` are
complete and unique with no regression; D8's amendment is additive and breaks no
consumer. Residue is MINOR: 1 (the "Numerical record" block is a hand-aggregated
summary presented as verbatim output, and the accompanying tolerance sentence
misdescribes four of six enforced tolerances), 2 (`notation.md` still missing
`ω_h, v_h, v_s, χ, δ_phys, S_phys, Δλ`), 3 (`definitions.md` header still says
D6–D8 are FROZEN), 4 (four sibling shards cite the superseded O7/O9 wording),
5 (remainder tolerances are sample-calibrated magic numbers), 6 (`R_S` needs the
integral Taylor remainder), 7 (O7's `sgn(v_h−v_s)` reads as `k_s`-dependent);
NOTE: 8–12. None blocks promotion of OR1; residue 1 should be fixed before the
paper cites this record, and residue 4 should be filed as a `bd` issue.
