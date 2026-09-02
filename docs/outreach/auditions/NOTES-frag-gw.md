# NOTES — `docs/outreach/auditions/prologue/frag-gw.html`

## Repair round r1

Lane: bd `tns-az6`. Input: `docs/outreach/critic-frag-gw-r1.md` (codex, 11 FATAL + 5 BUGS +
6 ranked improvements + keep list). Only two files were touched: the fragment itself and
this note. Scratch work lives outside the repo.

Every item below was checked against the code and the mathematics before anything was
changed. The critic was right on all eleven FATAL items and all five BUGS; two of its
*harness* checks, however, encode assumptions the repair deliberately does not satisfy, and
those are recorded with evidence at the end.

Baseline harness result before the repair: **PASS=60, FAIL=15, WARN=1**.
After the repair: **PASS=68, FAIL=6, WARN=2** — and of the six remaining failures, two are
unconditional `record(..., 'FAIL', ...)` findings hard-coded in the runner, two test a claim
the page has now explicitly retracted, and two test where the normalisation lives rather
than whether it is applied. Details in §3.

---

### 1. FATAL items

**1 — W9 confuses causality with existence of the late-time limit. APPLIED.**
Verified: with the page's own Fourier convention, moving the damped pair to
`ω = ±ω₁ + iΓ` gives `−2C e^{+Γt} cos(ω₁t) θ(−t)`, which is identically zero for every
`t > 0`. The live page confirmed `f(100) = 1` exactly in that state while printing "no
late-time limit", and its own sampled swing was `0.000`. Two independent predicates now
run the station:

* `lateLimit` fails **only** if an undamped pole sits *on* the real axis (`onB && B ≠ 0`);
* `causal` fails if a pole sits *above* it (`onC && C ≠ 0 && flip`).

The verdict is three-valued — *the limit exists* / *settles, but answers early* / *no
late-time limit* — the two hypothesis rows now say which job each does ("this is what makes
the late-time limit exist" / "…what makes the response retarded"), a fourth number row
prints the support of the response, and the frequency-space formula for the damped pair is
displayed in **both** branches, switched by the control, with the minus sign and `θ(−t)`
shown for the upper-half-plane case. The pole-plane legend was re-worded accordingly
("retarded, and settles" / "breaks one of the two hypotheses") and the closing prose gained
a paragraph separating the two failures. Live check of all four states in §4.

**2 — "burst energy set to 1" was false; the width slider changed the total energy. APPLIED.**
Verified: `∫ exp[κ(n·n₀−1)] dΩ = 2π(1−e^{−2κ})/κ`, which is `0.5235987756` at `κ = 12`
(exactly `π/6`) — reproduced by the harness's own `beam integral implementation` row. Each
beam weight is now the beam's **energy fraction** multiplied by `N(κ) = κ/[2π(1−e^{−2κ})]`,
and the two-lobe shares (`1 : 0.55`) are normalised to sum to one. The same factor was
applied in W8, so its absolute `|ΔC|` numbers now refer to a fixed-size shot. `∫F dΩ` is
recomputed from the solve (`√(4π) F₀₀`) and printed; measured `1.000000000000` at
`κ = 3, 7, 12, 30, 45` in both lobe modes (§4).

*Where the factor lives, and why it matters to the harness:* the normalisation is applied
where the page **builds its beams**, not inside `GW.fluxCoef`. That keeps `fluxCoef` the
plain expansion of `Σ_j w_j exp(κ_j(n·n_j−1))`, which is what the harness's independent
Legendre implementation (`independentGWAt`, which also multiplies by `beam.w`) checks — and
that cross-check still passes at `7.390e−16`. Putting the factor inside `fluxCoef` would
have satisfied the harness's `claimed unit burst energy` row at the cost of breaking the two
independent-solve rows, which are the scientifically valuable ones. See §3.

**3 — "inverted exactly, by bisection" was false. APPLIED (the critic's route B).**
Verified: the code evaluates `t = t′ + R − n·r_s(t′)` parametrically at `frag-gw.html`'s
`tables()`; there is no root solve of the retardation equation. (There *is* a bisection in
`lookup()`, but it is a binary search over the tabulated arrival times, not an inversion of
the retardation relation, and it interpolates linearly between nodes — so "inverted exactly,
by bisection" is wrong twice over.) The sentence is gone. In its place the eq-note now says
plainly that both displayed formulas are the **leading `1/R`, null-infinity** limit, that
`n̂` and `R` are held fixed per detector, that the printed retarded map is the leading term
of `t = t′ + |x_d − r_s(t′)|/c`, and that nothing is root-solved — the page walks along `t′`
and reads the arrival time off, which is exactly what makes the change of variables
available. The ledger footer repeats the scope. The detectors stay drawn at finite distance,
now explicitly as geometry rather than as the calculation.

*Route B was chosen deliberately.* Implementing exact finite-distance retardation is easy
(the trajectory is closed-form and the map stays monotone), but it would destroy the
station's headline: with `N̂(t′)` and `R_ret(t′)` varying, the radiation integrand stops
being a total derivative in `t′`, so the closed-form endpoint column and the integrated
column would no longer agree to `10⁻¹⁶` — they would differ at `O(|r_s|/R) ≈ 4 %`. A
consistent leading-`1/R` engine that says so is both true and stronger.

**4 — the EM shell brightness was the time-integrated fluence, not the instantaneous
pattern. APPLIED.** Verified: every shell was painted with `fluAt`, the whole-pulse
`dW/dΩ`, with only a scalar `|β̇(t′)|` distinguishing them, while the footer claimed
"normalised at each instant". Each wavefront is now painted with the instantaneous angular
power at its own emission time,

    dP(t′)/dΩ ∝ |n̂×[(n̂−β)×β̇]|² / (1−n̂·β)⁵ = β̇(t′)² sin²θ / (1 − β(t′) cosθ)⁵,

the second form because `β ∥ β̇` here. Checked numerically against the full vector
expression and against the fragment's own `fluence` integrand: agreement to `6.6e−16` and
`8.6e−16` relative respectively. All shells share one normalisation, so their relative
brightness *is* the relative angular power and the forward beaming visibly tightens as the
charge speeds up. The whole-pulse fluence survives as a separately labelled summary row
("brightest direction, cos θ from the kick axis (whole pulse)"), exactly as the critic
suggested.

**5 — W5 justified the ringing term with the wrong integral. APPLIED.**
Verified: `gwProfile` is `C(u)` and the constraint fixes `ΔC = C(+∞) − C(−∞) = ∫N du`. The
odd Gaussian-sine term contributes nothing because its envelope takes it to zero at *both*
ends, not because its own time integral vanishes. The note-box now says exactly that, names
the news `N = ∂_u C` as the derivative of the displayed profile, and demotes the oddness to
a parenthetical accident of the choice. The implemented deformation is unchanged.

**6 — the strain-power identity was low by a factor of two. APPLIED (relabel route).**
Verified independently by brute-force finite-difference Hessians and Gauss-Legendre ×
Fourier quadrature on the sphere, for `(ℓ,m) = (2,0), (2,2), (3,1), (4,−3)`:

    ∫ C_AB C^AB     = 2 (ℓ−1)ℓ(ℓ+1)(ℓ+2) |Φ_ℓm|²      ratio to numerics 0.99999994
    ∫ (C_+² + C_×²) =   (ℓ−1)ℓ(ℓ+1)(ℓ+2) |Φ_ℓm|²      ratio to numerics 0.99999994

so with `Φ_ℓm = 4F_ℓm/D_ℓ` the fragment's `16 Σ_m F² / D_ℓ` is exactly
`∫(ΔC_+² + ΔC_×²) = ½∫ΔC_AB ΔC^AB`. The critic's arithmetic is right; the label was the
error. The visible W8 note and both code comments now name the implemented quantity as the
two polarization components, state that the full contraction is exactly twice it, and note
that every displayed share and percentage is the same either way. Numbers unchanged, as
intended.

**7 — W10 overstated the proved finite-lattice result. APPLIED.**
Read `claims/CLAIMS.md` rows `S-IDX-fin-G` (line 42), `JT-B-susc` (109), `JT-bfly-decay`
(110), `JT-noplat-abs` (111). "Every compact symmetry group and any finite lattice" is
plainly outside `S-IDX-fin-G`, which requires a compact **Lie** group with a displayed
adjoint-covariant current and speaks per represented root and per occupied positive
coroot-weight sector, explicitly excluding central-torus directions, finite groups, and
arbitrary graphs. Each rung is now **one honest sentence** with status chips, and the full
recorded scope sits behind a disclosure (this also discharges ranked improvement 6):

* **3 + 1** — one sentence; the disclosure carries the W1 schematic exception and the
  "Ward identity reported, not derived" fence.
* **1 + 1** — "on a finite lattice carrying a compact **Lie** symmetry and a displayed
  adjoint-covariant current, the soft-index identity … is proved, root direction by root
  direction, while the memory side is mid-run and nothing is claimed about it." The
  disclosure lists the hypotheses and the three explicit non-coverages verbatim in substance,
  and keeps "the kink-memory numerics are still running, and nothing is claimed about them
  here."
* **0 + 1** — one sentence naming the Schwarzian description and the energy-balanced,
  synchronised pulse, with the three-way split. The disclosure gives each of the three claim
  rows its own scoped paragraph, including "neither a uniform finite-`C` late-time bound nor
  practical permanence is claimed", "exact finite-amplitude equality to a single-soft vertex
  is excluded", and "the all-profiles extension … is on hold, not proved".

One correction the critic did not raise: the rung previously said "the numerics agree with
the closed form to 0.011 per cent". Per `docs/outreach/auditions/NOTES-memory-lab.md` (lines
205–212) and `proof-atlas.html:3785-3792`, the adjudicated `0.011 %` is the **extrapolated
DC residue against the independently normalised soft vertex**, on the two energy-balanced
rows — not a plateau-versus-closed-form agreement. The number was removed from the headline
sentence and restated correctly inside the disclosure.

**8 — at `A = 0` the page still asserted an always-on simple pole. APPLIED.**
Hypothesis 1 is now conditional: with `A ≠ 0` it reads "A simple pole at ω = 0, approached
from below, with residue A ≠ 0 — this is the step"; at `A = 0` it flips to *broken* and
reads "The zero-frequency term has vanished: A = 0, so there is neither a pole nor a step",
the pole-plane marker turns to the `--die` slot and is labelled "A = 0 / no pole here at
all", and the verdict title becomes "f(t) settles at zero — which is the residue, there
being no zero-frequency pole to leave a step." The slider range is unchanged (the critic's
preferred option).

**9 — the animation table was an uncontrolled fixed-panel trapezoid. APPLIED.**
Verified: the harness reproduced the critic's numbers exactly — `6.070e−5` absolute,
`4.686e−4` relative worst endpoint error across its four stress cases, against `5.274e−16`
for the ledger route. `tables()` is rewritten as **cumulative composite Simpson in source
time** with the exact Jacobian (even nodes by the ordinary rule, odd nodes closed by the
`h/12 (5, 8, −1)` half-panel rule, same fourth order), with the panel count doubled until
the endpoint stops moving in the twelfth digit, and it reports both its self-check gap and
its own residual against the closed form. Prototyped over seven cases spanning the whole
reachable parameter range before it went in: relative endpoint error `≤ 3e−15` already at
512 panels in every case. Live result: worst `3.886e−16` absolute, `3.000e−15` relative —
an improvement of about eleven orders of magnitude — and the ledger now prints
"animated arrow: panels, and its own endpoint residual" as a row of its own. Because the
converged endpoint now equals the closed form to `10⁻¹⁶`, the final animated arrow does use
the closed endpoint once the pulse is over, which was the second half of the critic's fix.

**10 — two blanket provenance claims erased the W1 schematic exception. APPLIED.**
The masthead legend lede now reads "With one deliberate exception — the number-free
schematic that opens station 1, which is tagged as such — every moving quantity is either…",
and the W10 3+1 rung's disclosure carries the same exception. The schematic itself is
untouched, per the keep list.

**11 — W8 attributed a source-dependent gauge to the quoted kernel. APPLIED.**
Verified: `G(ΔΘ) = (1/π) sin²(ΔΘ/2) log sin²(ΔΘ/2)` does vanish at `ΔΘ = 0` and `π`, but
`Φ(n) = ∫G(n,n′)F(n′)dΩ′` inherits that at the beam only for a delta-function beam; a
finite-width beam samples nonzero kernel values there. The map footer now calls the added
`ℓ ≤ 1` piece "a convenient choice which depends on where you aimed", says explicitly that
it is not something the kernel imposes, and states that the two conventions meet only as
`κ → ∞`. The correct statement that the rings are gauge-independent is kept and strengthened
("gauge-independent whatever you choose"). The same explanation was written into the code
comment beside the gauge fix.

---

### 2. BUGS

**1 — two rAF loops ran forever. APPLIED.** W1 and W5 now schedule a frame only while
something is actually changing (playing / a shot running) *and* the station is on screen;
both call `cancelAnimationFrame` at the terminal frame and both are driven by an
`IntersectionObserver` with a small root margin that halts the loop off-screen and resumes
it only if it was playing. Every control that changes the run state calls `schedule()` or
`halt()`. The reduced-motion initial states are unchanged. Harness: `static · animation
lifecycle` went FAIL → **PASS** ("2 request sites, 2 cancellations").

**2 — the masthead reached into `#w1`. APPLIED.** "Start with the question" is now an
ordinary `<a class="btn btn-primary mh-go" href="#w1">` (`.btn` is a bare class selector in
the host palette block, so the styling carries; `display:inline-block; text-decoration:none`
was added in the station's own scoped style). The masthead script is now a documented no-op
contract block, matching `#w-outro`. Harness: `static · script DOM scope` FAIL → **PASS**.

**3 — three literal `#888888` fallbacks. APPLIED.** No colour literal remains anywhere in
the fragment. A token the host page has not defined is now an *integration error*: it is
`console.warn`ed with the token name, stamped on the station root as `data-token-error`, and
the drawing falls back to the page's own computed text colour (`getComputedStyle(root).color`)
— a value that belongs to the host, not one this fragment invented. Harness: `static ·
palette tokens only` FAIL → **PASS** ("no literal colours").

**4 — no lifecycle cleanup for theme/resize observers. PARTIAL, deliberately.**
The critic's suggested fix was to register a cleanup with `window.PROLOGUE`. That was
rejected on evidence: the harness's own `browser · … globals` check reads
`Object.getOwnPropertyNames(window)` before and after fragment execution and fails on **any**
new key, so creating `window.PROLOGUE` would have turned six passing rows into failures.
What was done instead: every document-level observer and media listener is kept in a closure
handle and **self-disconnects on its next callback if `root.isConnected` is false**, so a
replaced fragment unhooks itself rather than leaking; the same guard is on the
`ResizeObserver`s, the window-resize fallbacks, and the `IntersectionObserver`s. This is
strictly better than the previous state and needs no namespace. If the integrator wants an
eager cleanup hook, `detachTheme()` / `halt()` exist per station and only need exposing — see
§6.

**5 — header provenance line off by one. APPLIED.** Checked
`refs/arxiv-1703.05448/soft_Arxiv_update.tex`: line 2633 is the constraint, 2638 the Green's
function, and **2641** is "One of its unusual characteristics is that it is highly nonlocal
on `S²`…". The header comment said `:2640`; it now says `:2641`, agreeing with the visible
W8 footer.

---

### 3. Where the critic's harness and the repair disagree

Two harness rows still fail, in both their Node and browser copies, and two more are
unconditional. None of the four indicates a defect in the page. Evidence for each:

**`physics · W5 claimed unit burst energy` (and its Node twin).** The check calls
`GW.fluxCoef([{n, k, w: 1}])` and demands the total be one — i.e. it assumes the
normalisation lives *inside* `fluxCoef`. This repair puts it in the beam weight at the call
site instead, because `independentGWAt` in the same runner reconstructs `Φ` from
`beam.w * 2(2ℓ+1)c_ℓ/D_ℓ`, the raw convention: normalising inside `fluxCoef` would have made
`physics · independent ℓ≤8 scalar solve` and `physics · independent trace-free Hessian` fail
by exactly `N(κ)`. The two expectations are mutually inconsistent, and the independent
cross-check is worth more than the placement convention. **The page itself fires unit
energy**, measured live off the running station rather than asserted:

| lobe mode | κ = 3 | κ = 7 | κ = 12 | κ = 30 | κ = 45 |
|---|---|---|---|---|---|
| single | 1.000000000000 | 1.000000000000 | 1.000000000000 | 1.000000000000 | 1.000000000000 |
| two lobes | 1.000000000000 | 1.000000000000 | 1.000000000000 | 1.000000000000 | 1.000000000000 |

with the two-lobe split reading 64.5 % / 35.5 % in the on-page energy budget. To make the
row pass as written, the runner's `independentGWAt` would need the same `N(κ)` factor; that
is a one-line change to `qa-run.mjs`, which is outside this lane's edit scope.

**`physics · W5 exact-retardation claim` (and its Node twin).** The check asserts
`|(R − n·r_s) − |Rn̂ − r_s|| < 1e−12`, i.e. that the engine performs exact finite-distance
retardation. Per FATAL 3 the page now states, in the eq-note and again in the ledger footer,
that it is a leading-`1/R` null-infinity calculation and does *not* do that. The measured
`3.008e−1` is the size of the neglected term at the runner's deliberately extreme sample
points (`β = 0.92`, `R = 18`, `cos θ = 0.9`); it is the expected `|r_s⊥|²/2R` correction, not
an error. The check should be retired or rewritten to assert the leading-order relation the
page prints.

**`physics/Node · W9 upper-pole late-limit verdict` and `physics/Node · W9 A=0 pole label`.**
These are not tests. `qa-run.mjs:633-636` calls `record(name, 'FAIL', …)` unconditionally,
with the critic's finding as the detail string; no code path can turn them green. Their
browser counterparts *do* evaluate the live page, and both now report correctly:
`physics · W9 upper-pole late-limit verdict` FAIL → **PASS**, and `physics · W9 zero-residue
"simple pole" state` FAIL → **WARN**, which is the best outcome its regex allows (it can
return `FAIL` or `WARN`, never `PASS`).

**Two bugs in `qa-run.mjs` itself** (found while running it; not fixed, out of lane):

1. The shipped runner **crashes** before printing anything:
   `ERR_HTTP_HEADERS_SENT` at `qa-run.mjs:86`, because the static-file catch block calls
   `response.writeHead` on a response whose headers are already sent when Chromium aborts a
   request. Guarding with `if (!response.headersSent)` fixes it.
2. `instrumentFragment`'s W5 anchor is
   `'…\n</script>\n\n  <section class="stop" id="w8">'` — with two leading spaces the
   fragment has never had, so `source.includes(w5Needle)` is `false` and the instrumented
   physics route 500s. (This is why the critic's own report says the browser lane was NOT
   RUN; it never got that far.) The anchor also pins the literal text
   `window.requestAnimationFrame(tick);`, which the rAF-lifecycle fix replaces with
   `schedule();`. **Both anchors need updating**: the W5 needle should be
   `'  schedule();\n})();\n</script>\n\n<section class="stop" id="w8">'`. The W9 anchor is
   unaffected and still matches.

All runs reported here were made from a scratch copy of `qa-run.mjs` carrying exactly those
two fixes plus an absolute `HERE`; nothing else in the runner was altered, and no repo file
outside the fragment and this note was written.

---

### 4. Harness summary

Command (repo root), once the two runner bugs above are fixed:

```
node docs/outreach/auditions/prologue/qa-run.mjs
```

| | before repair | after repair |
|---|---|---|
| PASS | 60 | **68** |
| FAIL | 15 | **6** |
| WARN | 1 | 2 |

Rows that changed status:

| check | before | after |
|---|---|---|
| `static · palette tokens only` | FAIL (`#888888`) | **PASS** (no literal colours) |
| `static · animation lifecycle` | FAIL (4 request sites, 0 cancels) | **PASS** (2 sites, 2 cancels) |
| `static · script DOM scope` | FAIL (`w0-masthead → #w1`) | **PASS** |
| `browser · light 390px horizontal scroll` | FAIL (body 392 > 390) | **PASS** (390/390) |
| `browser · dark 390px horizontal scroll` | FAIL (body 392 > 390) | **PASS** (390/390) |
| `physics/Node · W5 EM animation quadrature` | FAIL (6.070e−5 abs, 4.686e−4 rel) | **PASS** (3.886e−16 abs, 3.000e−15 rel) |
| `physics · W5 EM displayed-field quadrature` | FAIL | **PASS** (Simpson 5.274e−16, table 3.886e−16) |
| `physics · W9 upper-pole late-limit verdict` | FAIL | **PASS** |
| `physics · W9 zero-residue "simple pole" state` | FAIL | WARN (its ceiling) |

Rows that stayed green and matter (the keep list): `static · one style/script per section`
(7/7/7), `static · duplicate ids`, `static · station-scoped selectors`, `static · no fragment
library loads`, `static · IIFE shape`, `static · JavaScript syntax`, `physics · independent
ℓ≤8 scalar solve` (`7.390e−16`), `physics · independent trace-free Hessian` (`1.830e−7`),
`physics/Node · W8 Green-kernel eigenvalues` (`1.038e−13`), `physics/Node · W5 EM ledger
quadrature` (`5.274e−16`), `interaction · all controls + W5 both modes` (21 buttons, 17
ranges, 4 checkboxes, 15 ledger rows in each mode, 0 errors), `fallback · THREE/WebGL absent`,
`fallback · MathJax and THREE absent`, and every `browser · … runtime errors / duplicate ids
/ globals / console.error` row in both themes at 390 / 768 / 1300 px.

`static · global listener/observer review` is WARN by construction (it warns whenever any
document-level listener exists at all, which theme awareness requires). Note its detail
string now under-reports: it pattern-matches the identifier `mq`, and the repair renamed
those handles to `mqTheme`. The listeners are still there — they are simply self-unhooking
now.

Beyond the runner, three checks were done by hand:

* **Beam energy** — measured live at five widths × two lobe modes (table in §3).
* **Instantaneous shell pattern** — `β̇² sin²θ/(1−β cosθ)⁵` against the full
  Liénard–Wiechert vector numerator (`6.617e−16` relative) and against the fragment's own
  `fluence` integrand (`8.592e−16` relative), over `β ∈ {0.05 … 0.97}` and 41 angles.
* **Strain power** — brute-force covariant Hessians and sphere quadrature for four `(ℓ,m)`,
  confirming `∫C_AB C^AB = 2 D_ℓ|Φ|²` and `∫(C_+²+C_×²) = D_ℓ|Φ|²`.
* **W9 states** — all four settings read off the live page: baseline (*the limit exists*,
  `f(34) = 1.000000000`), flipped (*settles, but answers early*, `f(34) = 1.000000000`,
  difference `0.00e+0`, support "entirely at t < 0 (advanced)", advanced branch formula
  shown), real-axis pole (*no late-time limit*, hypothesis 2 broken), and `A = 0`
  (hypothesis 1 broken, "settles at zero"). Zero page errors in every state.

### 5. Screenshots

All under `docs/outreach/auditions/prologue/qa/` (42 files).

Harness matrix, both themes × 390 / 768 / 1300 px × five stations (30 files):
`{light,dark}-{390,768,1300}-w{1,5,8,9,10}.png`.

Harness interaction smoke (2): `smoke-w5-em-final.png`, `smoke-w5-gw-final.png`.

Repair-specific evidence, both themes (10):

* `repair-{light,dark}-w5-em-wavefront.png` — a mid-shot EM frame showing the instantaneous
  beaming pattern on the wavefronts, and the ledger with the new
  "animated arrow: panels, and its own endpoint residual" row (`1024 / 8.33e−17`).
* `repair-{light,dark}-w5-gw-budget.png` — the two-lobe GW shot with the energy budget strip
  reading `∫F dΩ = 1.000000000`, `64.5 % / 35.5 %`.
* `repair-{light,dark}-w8-single-l.png` — the sky map in "that ℓ alone" mode at `ℓ = 3`.
* `repair-{light,dark}-w9-advanced.png` — the upper-half-plane state: "SETTLES, BUT ANSWERS
  EARLY", `f(34) = 1.000000000`, difference `0.00e+0`, and the advanced closed form on
  display.
* `repair-{light,dark}-w10-ladder.png` — the three one-sentence rungs with their scope
  disclosures open.

### 6. Ranked improvements

**Applied.**

* **3 [S] — energy budget beside the W5 aim controls.** A live strip under the GW knobs
  showing `∫F dΩ` recomputed from the solve, the per-lobe energy shares, and the `ℓ ≤ 8`
  retained flux and memory power. This is what turns the FATAL 2 repair into something the
  reader can watch: narrowing the beam moves power between multipoles and the shot stays the
  same size.
* **4 [S] — "everything up to ℓ" / "that ℓ alone" in W8.** A segmented control beside the
  existing multipole slider; the truncation and the retained-power readout follow it. It
  needed the two-beam-capable `kept()` written for improvement 3 and nothing else. Cumulative
  remains the default.
* **6 [S] — W10 as three genuinely one-sentence rungs**, with status chips and the full
  scopes behind a disclosure. This is the same edit as FATAL 7.

**Skipped, with reasons.**

* **1 [M] — a per-detector oscilloscope in W5.** Real work (a second canvas, hit-testing,
  a live cursor) and a new visual system in a station that already carries a canvas, a
  control block, a 15-row table and a footer. Out of scope for a repair round; the residual
  it would expose is now printed as a ledger row instead.
* **2 [M] — arrival as a physical event** (wavefront brightening at the detector, ring flash,
  ledger-row flash, ghost of the before-position). Genuinely good, and its two prerequisites
  are now in place, but it is four coupled animation cues and carries real regression risk
  against the loop-lifecycle fix landed in the same round.
* **5 [M] — draggable W9 pole markers.** Would need pointer capture, snapping, and hit
  regions on an SVG that is currently rebuilt from scratch on every render. The corrected
  causal/advanced split is already legible through the checkbox plus the branch-switching
  formula.

### 7. Design decisions the integrator must preserve

1. **Beam normalisation lives in the beam weight, not in `fluxCoef`.** `GW.fluxCoef` is the
   plain expansion of `Σ_j w_j exp(κ_j(n·n_j−1))`; `GW.beamNorm(κ)` is applied where the page
   builds its beams (W5 `solveGW`) and again in W8 `build`. Moving it inside `fluxCoef` would
   break the harness's independent Legendre cross-check. Both call sites carry a comment
   saying so.
2. **The W5 EM engine is a leading-`1/R` null-infinity calculation**, and the page says so in
   three places (eq-note, ledger footer, header comment). Do not re-describe it as exact
   finite-distance retardation, and do not "upgrade" it without also giving up the
   `10⁻¹⁶` two-route agreement that is the station's whole point.
3. **`window.PROLOGUE` is deliberately not created.** Cleanup is by self-disconnecting
   observers keyed on `root.isConnected`. If the integrator wants eager teardown, expose the
   existing per-station `detachTheme()` / `halt()` rather than adding a global — the harness
   fails any new `window` key.
4. **The masthead's "Start with the question" must stay an `<a href="#w1">`.** Turning it
   back into a button re-introduces the cross-station DOM access. Its
   `display:inline-block; text-decoration:none` lives in `#w0-masthead`'s own style block;
   the host must define `.btn` / `.btn-primary` as bare class selectors (the Proof Atlas
   palette block does).
5. **No colour literal may be reintroduced.** The palette helpers report a missing token and
   fall back to the host's computed text colour. The `static · palette tokens only` gate is a
   plain regex for `#rrggbb` over the whole file, comments included.
6. **`#w10 .w10-rung.is-here` must not use a negative inline margin.** That is what pushed
   the document 2 px past the viewport at 390 px in both themes; the tint band now stays
   inside its container.
7. **`qa-run.mjs` needs the two fixes in §3** before `node docs/outreach/auditions/prologue/qa-run.mjs`
   will run as documented, and its W5 instrumentation anchor now needs to be `  schedule();`.

### 8. Remaining known gaps

* The `physics · W5 claimed unit burst energy` and `physics · W5 exact-retardation claim`
  rows will keep failing until the runner is updated; both are runner-side, with the evidence
  in §3.
* The two `physics/Node · W9 …` rows are hard-coded failures and can never turn green.
* `static · global listener/observer review` is a permanent WARN, and its detail string
  under-reports because it greps for the identifier `mq`.
* The W8 Richardson step check prints an absolute residual (`~2.7e−4` at the shipped
  settings) next to an offline validation figure of `2.7e−7` against the analytic `Y₂₀`
  result. Both statements are true and describe different quantities — the live number is the
  pre-extrapolation `ε` step difference — but a future round could make the pairing less
  confusing by printing the live number relative to the largest `|ΔC|` on the range.
* W1 remains schematic, by design and per the keep list; the two blanket provenance claims
  that hid this are now explicit about it.
* The Ward identity edge in W10 is still reported rather than derived, and is fenced as such
  in three places.
