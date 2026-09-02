# frag-gw.html QA and constructive critique — round 1

Audit target: `docs/outreach/auditions/prologue/frag-gw.html`.

Status: audit complete. The source fragment was treated as read-only.

## 1. Verdict

**Not ready to integrate without repair.** The fragment has a strong explanatory arc and the core
`ℓ ≤ 8` harmonic inversion is mathematically sound, but several visible claims do not describe the
calculation actually performed. In particular, W5 changes the total GW energy when the beam-width
slider moves while calling it one, its EM wavefront uses far-zone rather than exact finite-detector
retardation, and W9 says an advanced transient has no future limit even though its own closed form
settles exactly to `A`. These are truth-constraint failures, not polish. The repair is localized and
the fragment should be worth integrating after it is made and the harness passes.

## 2. FATAL — physics and truth-constraint items

1. **W9 confuses causality with existence of the late-time limit** (`frag-gw.html:2410-2412,
   2520-2543`). Moving the damped pair above the real axis correctly changes its inverse transform
   to
   `−2C exp(Γt) cos(ω₁t) θ(−t)`. That term is advanced, but it is identically zero for `t>0`;
   therefore `lim(t→+∞) f(t)=A` still exists and still equals
   `lim(ω→0)(−iω f̃(ω))=A`. The page instead prints “no late-time limit” (indeed its sampled swing
   is zero). **Fix:** track two independent predicates: `lateLimit = !(onB && B !== 0)` and
   `causal = !(onC && C !== 0 && flip)`. For the upper-half-plane pair report “future limit exists
   and equals A, but the response is advanced (non-retarded),” and reserve “no limit” for a nonzero
   real-axis pole. Change the prose from “exactly when every other pole is below” to the correct
   split: lower-half-plane support enforces a retarded decaying response; absence of other real-axis
   singularities is what makes the future limit exist in this family. The “put its poles above”
   control also leaves the displayed frequency-space formula at `+iΓ` (`:2273-2282`) while the JS
   evaluates the `−iΓ`/advanced branch. Display both cases (including the minus sign and `θ(−t)`),
   and switch/highlight the formula with the control.

2. **W5's “burst energy set to 1” is false and the width slider changes total energy**
   (`frag-gw.html:865-869, 901-909, 1033-1037, 1337-1339`; duplicated in W8 at
   `:1809-1817,1876-1882`). The beam actually used is
   `F(n)=exp[κ(n·n₀−1)]`, whose integral is
   `2π(1−exp(−2κ))/κ`, not one (for `κ=12`, approximately `0.5235987756`). Thus changing `κ`
   changes both angular width and injected energy, contaminating every absolute strain readout.
   **Fix:** multiply each beam by `Nκ=κ/[2π(1−exp(−2κ))]`; define whether two-lobe weights are
   energy fractions and normalize their sum if the total is to remain one. Apply the same factor to
   the displayed `F_{ℓm}` formula and both duplicated solvers. Alternatively relabel the quantity as
   unit peak flux and print its changing integral, but that would not support the current ledger.

3. **W5 says exact per-detector retardation and bisection, but implements the leading far-zone
   map parametrically** (`frag-gw.html:448-457, 761-769, 802-820`). The code uses
   `t=t′+R−n·r_s(t′)` at `:810`; there is no bisection. At finite detector position `x_d=Rn`, exact
   retardation is `t=t′+|x_d−r_s(t′)|`, and its direction and denominator use
   `N=(x_d−r_s)/|x_d−r_s|` and the retarded distance, not fixed `n,R`. **Fix:** either implement that
   finite-distance retarded solve and recompute the displayed detector field, or explicitly make the
   engine a null-infinity/leading-`1/R` calculation and say “the retarded map is evaluated
   parametrically; no root solve is used.” Remove “inverted exactly, by bisection” in either case.
   The latter repair preserves the endpoint ledger but must stop presenting the drawn finite range as
   exact finite-distance geometry.

4. **The EM shell's angular brightness is not the field/flux on the wavefront it depicts**
   (`frag-gw.html:790-800,1015-1025,1103-1125,1271-1278,1332-1335`). Every emission-time shell is
   painted with `fluAt`, the *time-integrated* fluence of the entire kick, while only a scalar
   `|β̇(t′)|` weight changes between shells. Relativistic beaming depends on the instantaneous
   `β(t′)` through `(1−n·β)`, so an overshoot cannot have this fixed angular pattern. The footer's
   “normalised at each instant” claim is therefore false. **Fix:** pass the shell's emission time to
   the angular painter and evaluate the displayed Liénard–Wiechert numerator/denominator there
   (choose and label field amplitude or Poynting flux); keep the integrated fluence only as a
   separately labelled whole-pulse summary.

5. **W5 describes the arbitrary GW transient using the wrong integral** (`frag-gw.html:521-528,
   992-999,1231-1233`). `gwProfile` is the strain/shear history `C(u)` and `gwNews` is its derivative.
   The constraint fixes the endpoint change `ΔC=∫N du`; the added odd Gaussian-sine term contributes
   no memory because it tends to zero at both endpoints, not because its own time integral is zero.
   **Fix:** say exactly that, and identify the transient news as the derivative of the displayed
   profile. The implemented deformation can remain unchanged.

6. **W8's stated strain-power identity is low by a factor of two** (`frag-gw.html:1898-1905,
   2034-2039`; the same convention is asserted at `:942-953`). With normalized scalar harmonics,
   `C_AB=(2D_AD_B−γ_ABD²)Φ` gives
   `∫C_AB C^AB=2(ℓ−1)ℓ(ℓ+1)(ℓ+2)|Φ_{ℓm}|²`
   and, for `Φ_{ℓm}=4F_{ℓm}/D_ℓ`, `32|F_{ℓm}|²/D_ℓ`, not `16|F|²/D_ℓ`.
   The plotted shares and retained percentages are unaffected because the missing factor is common.
   **Fix:** either multiply the spectrum by two, or—more naturally for the two polarization
   components—label the implemented quantity
   `(1/2)∫C_AB C^AB=∫(C_+²+C_×²)=16Σ_m|F_{ℓm}|²/D_ℓ` everywhere.

7. **W10 overstates the proved finite-lattice result** (`frag-gw.html:2631-2640`). “The
   soft-index identity … is proved, for every compact symmetry group and on any finite lattice” drops
   the decisive scope in `CLAIMS.md` row `S-IDX-fin-G`: compact **Lie** on-site symmetry, a displayed
   adjoint-covariant current, represented roots of the semisimple Lie algebra, and occupied positive
   coroot-weight sectors. Central-torus directions have no root row and finite groups have no
   Lie-current row. **Fix:** replace the sentence with a faithful one-sentence compression of that
   scope; do not say “every compact symmetry group.” Also retain “kink-memory numerics are mid-run;
   nothing is claimed.” The 0+1 rung at `:2648-2660` likewise needs “energy-balanced compact pulse,
   synchronized, large-`C`-first Schwarzian window”: the absolute no-plateau row is proved only in
   that balanced scope. Compress each rung to the brief's requested one honest sentence while adding
   these scopes, rather than using the current multi-sentence mini-abstracts.

8. **At `A=0`, W9 still labels an always-on simple pole** (`frag-gw.html:2250-2254,
   2401,2520,2537`). The residue slider includes zero, where `iA/(ω+i0)` vanishes and there is no
   pole. **Fix:** either exclude zero from the control (awkward with positive/negative `A`) or make
   the hypothesis/status read “zero-pole term present iff `A≠0`; for `A=0` both residue and step are
   zero.”

9. **The detector motion is a real field quadrature, but not the controlled quadrature advertised
   for the ledger** (`frag-gw.html:802-829,1173-1209`). This is not an eased animation: `tables()`
   integrates the displayed radiative field in detector time and then integrates the resulting
   velocity again for position. However it uses a fixed 1024-panel trapezoid with no convergence
   check, while only the ledger uses the converged Simpson route. Across four in-range stress cases,
   the ledger's largest absolute endpoint error was `5.274e−16`, but the animation table reached
   `6.070e−5` absolute / `4.686e−4` relative. Even the shipped clean default at a representative
   detector differed by about `4.1e−6` relative. **Fix:** build the cumulative animation table with
   panel doubling (or a cumulative high-order rule), print/bound its endpoint residual, and make the
   final animated arrow use the closed endpoint once the pulse is over. Do not describe the visual
   detector kick as exact until this is controlled.

10. **Two blanket provenance claims erase the explicitly schematic W1 exception**
    (`frag-gw.html:115-118,2620-2623`). The masthead says every moving quantity is closed-form or a
    numerical solve, and the 3+1 rung says everything on the page is formula/solve/quotation; W1 is
    deliberately a hand-drawn animated waveform. **Fix:** add “except the explicitly tagged,
    number-free schematic at W1” to both summaries. Do not remove the schematic; it is doing useful
    pedagogical work.

11. **W8 attributes a source-dependent gauge choice to the quoted Green kernel**
    (`frag-gw.html:1892-1896,2165-2170`). Adding `ℓ=0,1` so the *convolved, truncated* `Φ` vanishes
    at the beam and antipode is a legitimate translation gauge. But the printed kernel itself being
    zero at angular separations zero and π only makes the convolution vanish at those points for a
    delta-function beam; a finite-width beam samples nonzero kernel values. **Fix:** call this a
    convenient source-dependent translation gauge, say it approaches the printed kernel's endpoint
    convention in the point-beam limit, and retain the correct statement that all ring strains are
    gauge-independent.

Verified and **not** a defect: with `D²Y_{ℓm}=−ℓ(ℓ+1)Y_{ℓm}`, the displayed operator
`D²(D²+2)` has eigenvalue `(ℓ−1)ℓ(ℓ+1)(ℓ+2)`, so the sign and divisor in `Φ_{ℓm}=4F_{ℓm}/D_ℓ`
are correct. The real harmonics in JS are orthonormal (the omitted Condon–Shortley sign is a
consistent basis convention), and the quoted Green kernel has convolution eigenvalue `4/D_ℓ`:
its raw Legendre integral obeys `g_ℓD_ℓ=2/π`. The geodesic map used to draw a ring,
`δs^a=(1/2r)C^a{}_b s^b`, also has the correct factor of one half.

## 3. BUGS — JavaScript, contract, and layout

1. **Two animation loops run forever, including off-screen and after their shots stop**
   (`frag-gw.html:363-411,1516-1538`). W1 redraws every frame even when paused or at `TEND`; W5
   requests every frame even when `S.running=false`. Neither calls `cancelAnimationFrame` nor uses
   intersection/page visibility. On an assembled ten-station page this is avoidable background CPU.
   **Fix:** schedule only while state changes, cancel at the terminal frame, and use an
   `IntersectionObserver` to pause/cancel when each root leaves the viewport. Resume only if it was
   actively playing. The existing reduced-motion initial states are good, but currently they still
   leave the idle loops alive.

2. **The masthead script reaches into another station** (`frag-gw.html:191-203`), violating the
   “IIFE touches only its own section's DOM” rule. **Fix:** make “Start with the question” an ordinary
   `<a class="btn btn-primary" href="#w1">`; then the browser owns the cross-section navigation and
   the masthead script can remain a no-op contract block. Alternatively route through an integrator
   function under the one allowed namespace, `window.PROLOGUE`.

3. **Three canvas palette helpers contain a literal fallback colour**
   (`frag-gw.html:709,1773,2393`). `#888888` contradicts the “proof-atlas token names only” rule and
   the header's statement that no palette value is defined in the fragment. **Fix:** require the
   named token, report a missing-token integration error, and do not silently invent a colour.

4. **Theme/resize observers have no lifecycle cleanup** (`frag-gw.html:722-728,1530-1531,
   1784-1788,2216-2217,2395-2399`). They are closure-scoped and do not overwrite one another, so I
   found no immediate semantic collision; nevertheless three document-root observers, three media
   listeners, and two possible window-resize listeners survive if fragments are replaced. **Fix:**
   retain observer/listener handles and register a cleanup with `window.PROLOGUE`, or let the
   integrator broadcast one namespaced theme event to mounted station roots. `ResizeObserver` on the
   local canvas is already appropriately scoped.

5. **One provenance line is off by one in the source header** (`frag-gw.html:44`): the nonlocality
   quotation is at TeX line `2641`, not `2640`. The visible W8 footer at `:1642` correctly says
   `2641`. **Fix:** correct the header comment so both records agree.

Static contract results: **PASS** — seven sections, exactly one matching style and script each; no
duplicate IDs; every CSS selector scoped under its station ID; all seven scripts compile and are
single IIFEs; no external library load; no fragment-created global declaration; no Promise use (and
therefore no fragment promise rejection path). The W5 renderer is hand-rolled 3D projection on a 2D
canvas and never references `THREE` or WebGL, so THREE/WebGL absence is intrinsically non-fatal; if a
2D context itself is missing, `:979-983` exposes a textual fallback and the numerical ledger still
computes.

The headless layout/interaction portion is **NOT RUN**, not passed. `@playwright/cli` and its Chromium
1212 binary were found, but this managed environment kills Chromium before it creates a page:
`FATAL sandbox_host_linux.cc:41 Check failed: shutdown: Operation not permitted (1)`. The same failure
occurred with `--no-sandbox --single-process --no-zygote`. Localhost listening is also denied with
`EPERM`; the runner contains an in-memory HTTP-route fallback for that constraint. Separately, both
cdnjs probes failed DNS resolution (`curl: (6) Could not resolve host`), so MathJax/THREE-dependent
checks are **NOT RUN**. Consequently I could not verify either theme at 390/768/1300 px, horizontal
overflow, button/range interactions, runtime console errors, or the visual fallback, and I do not
claim any layout result.

Headless summary from the last run: `PASS=12, FAIL=8, WARN=2, NOT RUN=1`. The failures are the source
gates documented here (palette literal, animation lifecycle, cross-station DOM access, unit-flux
claim, uncontrolled animation quadrature, finite-distance retardation claim, and the two W9 state
errors). The warnings are the global-listener review and localhost fallback. **Screenshot list:
none** — `docs/outreach/auditions/prologue/qa/` is empty because Chromium never launched; no image was
fabricated as evidence.

## 4. Top improvements ranked by wow/effort

1. **[M] Give the selected W5 detector an oscilloscope.** Clicking a detector or ledger row should
   open two small live traces from the already-computed table: `E_rad(t)` and cumulative `Δv(t)`,
   with the endpoint formula drawn as a horizontal rule and the current retarded time marked. This
   makes “real quadrature, not easing” immediately visible and turns the residual into something a
   physicist can interrogate rather than trust.

2. **[M] Make exact arrival a physical event in W5.** Once the retardation and instantaneous angular
   pattern are repaired, let the wavefront brighten only where the computed field is large, flash the
   corresponding ring/charge and ledger row at its arrival time, and leave a faint before-position
   ghost after the shot. The range then reads spatially at a glance: aim → propagation → local
   response → persistent record. All four cues can be driven by existing solver state.

3. **[S] Put an energy budget beside the GW aim controls.** Show `∫F dΩ = 1` live and split it into
   lobe fractions when the second lobe is enabled. Beside it show `ℓ≤8` retained flux and memory
   power. This turns the required normalization repair into a satisfying invariant: narrowing the
   beam moves power between multipoles without secretly changing the shot's energy.

4. **[S] Add “cumulative ≤ℓ / this ℓ only” to W8.** The current cutoff slider demonstrates
   convergence, but isolating one multipole would let the reader see a quadrupole, octupole, and so
   on appear directly in the ring map. Reuse the existing `PhiT` array and zero every block except
   the selected one; keep the cumulative mode as default.

5. **[M] Let the reader drag W9's pole markers.** Snap horizontal motion to `±ω₀` pairs and vertical
   motion across the real axis, update the rational formula and exact inverse-transform branch, and
   keep the hypothesis ledger visible. Direct manipulation would make the causal/advanced and
   settling/non-settling distinctions much more memorable than three disconnected sliders.

6. **[S] Turn W10's ladder into three genuinely one-sentence rungs.** Keep the current sober tone,
   but replace status mini-essays with one scoped claim sentence plus compact status chips. Put the
   detailed hypotheses behind a disclosure. That meets the brief and lets the triangle, not project
   management, own the final screen.

## 5. Keep list

- **Keep W1's question, SCHEMATIC tag, and number-free figure.** It satisfies the special W1
  contract, states exactly which part is hand drawn, and uses the correct linear ring kinematics
  `δx=(1/2)h·x`. Repair the blanket summaries and loop lifecycle, not this opening.

- **Keep W5's two-mode range, overshoot profile, and two-route EM ledger.** The integrated column is
  genuine composite-Simpson quadrature of the displayed radiative field after the exact Jacobian
  change to source time; it is not an eased endpoint. Four independent stress cases agreed with the
  endpoint formula to `5.274e−16` absolute. Preserve the separation between radiative `1/R` and
  Coulomb `1/R²` terms; repair the finite-distance wording and the separate animation table.

- **Keep the GW operator and harmonic machinery.** An independent Simpson/Legendre implementation,
  using three one/two-beam patterns at three directions, matched the fragment's scalar `Φ` to
  `7.390e−16`; an analytic covariant-Hessian route matched its circle/Richardson strain components to
  `1.830e−7`. The normalized real `Y_{ℓm}` basis, the positive
  `(ℓ−1)ℓ(ℓ+1)(ℓ+2)` eigenvalue, the `ℓ=0,1` translation kernel, and the ring map's factor `1/(2r)`
  are correct. Normalize the source; do not rewrite the solver.

- **Keep W8's Green-function cross-check and nonlocal two-null explanation.** Extracted W8 code gave
  a worst relative deviation `1.038e−13` in `g_ℓD_ℓ=2/π` for `ℓ=2,…,8`. The Green-function sign is
  consistent with `Φ=−ΔC` relative to the TeX scalar convention. Only the strain-power label/factor
  and the finite-beam gauge wording need care.

- **Keep W9's three inverse-transform formulas.** With the stated Fourier convention, contour
  closure gives
  `iA/(ω+i0) ↔ Aθ(t)`, the real-axis pair ↔ `2B cos(ω₀t)θ(t)`, the lower-half-plane pair ↔
  `2C exp(−Γt)cos(ω₁t)θ(t)`, and the upper pair ↔
  `−2C exp(Γt)cos(ω₁t)θ(−t)`. The formulas and JS branches are correct; repair their displayed branch
  and verdict logic.

- **Keep the quotations and their restrained sourcing.** I checked the visible quotations against
  `soft_Arxiv_update.tex`: memory/DC and detection (`:329`), deep infrared (`:336`), the reported
  Ward-identity result (`:1064`), geodesic deviation/displacement (`:2590-2594`), constraint
  (`:2633`), Green kernel (`:2638`), and nonlocality (`:2641`) are verbatim apart from disclosed
  citation elision and typographic spacing. The lecture remark matches
  `extra-01-CdFyoaNv8GI-digest.md` insight 1, `[CdFyoaNv8GI @ 00:34:36]`. Keep W10's explicit
  “reported, not derived” fence around `:1064`.

- **Keep the restrained visual system and local structure.** The token-based palette, scoped CSS,
  internal table/chart scrollers, keyboard-operable W10 SVG controls, and 2D-canvas projection are a
  good integration base. Remove only the three literal fallback colours and add lifecycle cleanup.

## 6. Harness usage

From the repository root, rerun this lane exactly with:

```bash
node docs/outreach/auditions/prologue/qa-run.mjs
```

To exercise the two fragment files together through the same fetch/clone path the integrator uses:

```bash
node docs/outreach/auditions/prologue/qa-run.mjs --frag=frag-em.html,frag-gw.html
```

The runner resolves `playwright` from the globally installed `@playwright/cli`, starts an ephemeral
localhost server, and falls back to Playwright route fulfillment only when the host forbids listening.
It runs light/dark × 390/768/1300 px, screenshots every numbered station to
`docs/outreach/auditions/prologue/qa/`, checks document/body horizontal width, duplicate IDs, new
window globals, console/page/harness errors, all buttons/ranges/checkboxes, both W5 firing modes,
THREE/WebGL absence, and joint MathJax/THREE absence. It also extracts the private W5/W8 engines
without editing the fragment and repeats the independent physics checks. A source or runtime failure
sets a nonzero exit code; `NOT RUN` remains visibly separate.

For manual inspection, `qa-harness.html` accepts, for example,
`?theme=dark&frag=frag-em.html,frag-gw.html`. Its `window.__qa` object contains `errors`, `warnings`,
library state, loaded fragments, and any window keys added by fragment execution. The harness copies
all three Proof Atlas palette blocks verbatim, loads MathJax 3.2.2 with SVG output and three.js 0.160.1
from cdnjs, and re-executes inert `innerHTML` script nodes by cloning them in source order.
