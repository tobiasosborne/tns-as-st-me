# EM fragment critic report — round 1

## 1. Verdict

**Not ready to integrate without repair.** The inlined reference core is byte-for-byte correct and the
fragment's central numerical spine is good: W2 really streamlines the exact field, W3 really evaluates
the spectrum and photon number, W6's two core routes agree at the requested precision at its default,
and W7's local ledger is correct. The visible account of those calculations is not yet reliable,
however. W3 loses the binding electric-field/soft-coefficient sign and mislabels quadratic scaling as
linear; W4 fundamentally misdescribes the polarization-summed pattern, duplicates its formula outside
the core, and fabricates a maximum in an allowed zero-pattern state; W2 labels exact nonconcentric
fronts with inexact `ct`/`cτ` geometry; and W6 both overstates the quantity being integrated and fails
under legal controls. These are truth-constraint failures, not polish. The fixes are localized enough
that the fragment remains a strong repair candidate.

## 2. FATAL physics/truth items

1. **W4's bright-spot/pole account is false for the polarization-summed pattern it actually plots**
   (`frag-em.html:1958-1964,2004,2029-2049,2111`). For one massive leg,
   `P=Q²β² sin²θ/(1−β cosθ)²`: its own contribution is zero exactly along the velocity, is maximal on
   the ring `cos θ=β`, and has maximum `Q²β²/(1−β²)`, not `Q²/(1−β)²`. The page instead says the
   contribution is largest in the particle direction, quotes the latter scaling, and calls the finite
   massive feature a “pole” in visible copy, fallback copy, and the canvas accessibility text. Its
   `β=0.99` versus `β=0.5` comparison is consequently about `1.48e2` at the individual maxima, not
   four orders of magnitude. Lines `2038-2040` also say the already-projected `S` “points radially”;
   a nonzero `S` is tangent by definition—the unprojected `H` can be radial, making `S=0`. This
   directly violates the core NOTES' massive-leg prohibition. **Fix:** explain the forward polarization
   zero and the beamed annular maximum with the formulas above; replace every massive “pole” with
   “finite peak/ring” (reserving “collinear pole” for the null limit); update the colour-scale rationale
   and accessible/fallback text accordingly. Also repair `:2043-2049`: two legs combine into one
   effective leg only when their full velocities are equal, not merely their directions; the formula
   depends on speed as well as `Q` and `β-hat`.

2. **W4 reimplements the physics locally and its “Nothing here is interpolated” provenance is false**
   (`frag-em.html:2029-2032,2183-2186,2242-2276,2293-2302`). Readouts and the coarse statistics call
   `P.spherePattern`, but `paintSphere` independently reconstructs `H`, projects it, and squares it per
   texel. The 440×440/210×210 texture is then resized with canvas smoothing explicitly enabled. This
   contradicts both the builder report (“`spherePattern` evaluated per pixel”) and the page's claim of
   one uninterpolated sample per displayed pixel. **Fix:** use `P.spherePattern(coreParts(), n)` as the
   sole texel evaluator and describe the honest pipeline: exact core samples on a finite texture,
   bilinearly resampled only for display. Alternatively disable smoothing and make physical pixels map
   one-to-one, but still remove the station-local formula.

3. **W3 says an even-in-frequency energy correction is linear, while its printed examples are
   quadratic** (`frag-em.html:1560-1568`). For a real time-domain pulse, `|J(ω)|²` is even in `ω`, so
   its first generic correction to the plateau is `O(ω²)`; the page's own sequence
   `2.5e−8, 2.5e−10, 2.5e−12` when `ω` falls by factors of ten confirms quadratic scaling. **Fix:**
   change “first correction in `ωτ`” to “first correction of order `(ωτ)²`” and “exact proportion to
   `ω`” to “quadratically with `ω`.”

4. **W3 equates two coefficients that have opposite signs in the binding core convention**
   (`frag-em.html:1502-1508,1600-1618,1621-1631`; core NOTES `:201-212`). The vector defined by the
   zero-frequency electric-field integral is
   `M=n×(n×[h_f−h_i])`, so for transverse polarization `M·epsilon=−S_cl`, whereas
   `softAmplitude` and Weinberg's bracket return `S_cl=(h_f−h_i)·epsilon`. The ledger displays the
   latter but labels it “`S-vector·epsilon` from the closed form above,” and the prose asserts a plus
   sign. This is not an arbitrary metric sign after the page has fixed both definitions. **Fix:** name
   the vector in the plateau `M`/`J(0)`; display `M·epsilon=−S_cl`; and write Weinberg's term as
   `Q S_cl/ω=−Q M·epsilon/ω` in the stated convention. Magnitudes and the spectrum need no change.

5. **The W3 source is not quoted verbatim despite the binding verbatim requirement and its own
   “quoted as it stands” claim** (`frag-em.html:1571-1591`; source
   `soft_Arxiv_update.tex:1075-1082`). The displayed equation expands five source macros and normalizes
   notation/spacing; the prose excerpt omits the beginning of the source sentence, and “the leading
   order term … is a pole” is line 1083, outside the cited range. **Fix:** either reproduce lines
   1075–1082 literally in a clearly marked source block (with a separately rendered faithful equation),
   or remove “verbatim/as it stands” and obtain approval for a disclosed macro-expanded transcription;
   cite the pole sentence as `:1083`.

6. **W2's prose and canvas label contradict its exact finite-duration retardation geometry**
   (`frag-em.html:866-876,903-906,936-937,1360`). For the raised-cosine kick, the outer and inner
   faces at page time `t` are `|x−r(−τ/2)|=t+τ/2` and
   `|x−r(+τ/2)|=t−τ/2`. They are nonconcentric, so their radial separation from the displayed origin
   is angle-dependent—not `cτ`—and neither face has radius `ct`. At the defaults I obtain thicknesses
   from `0.06525` to `0.11475` as the viewing angle runs from 0° to 180°, while `τ=0.09`.
   **Fix:** call `cτ` the source-time emission duration/characteristic thickness; state the two exact
   face equations in the caption; replace “no point further away than `ct`,” “shell of thickness
   `cτ`,” and the canvas's “shell radius `ct`” with an angle-aware distance/readout or neutral “page
   time `ct`.”

7. **W6 first equates the unqualified full-field integral with the soft coefficient, then retracts
   that claim only later** (`frag-em.html:2605-2624,2627-2630,2714-2745`). The opening says “the thing
   to compute is `∫E dt`” and “this integral is the same number” and displays unqualified `E`; the
   core NOTES permit only the leading transverse radiation-order integral and explicitly prohibit
   saying the DC field is the whole time integral of `E`. **Fix:** put
   `E_rad^(1/r)` (or the corresponding asymptotic coefficient) in the first prose and equation, and
   introduce the finite-window Coulomb drift before making the equality. Also restore the test-body
   coupling: `Delta v=(q_test/m_test)∫E_source dt`, and say explicitly that the ledger strips/sets the
   source-charge and test charge-to-mass factors. Do not rely on a later correction to cure an earlier
   false statement.

8. **W6 has the vector-potential Fourier sign wrong under its displayed convention**
   (`frag-em.html:2612-2620`). With `E-tilde(ω)=∫dt e^{iωt}E(t)` and radiation-gauge
   `E=−∂t A`, integration by parts gives `E-tilde=iω A-tilde`, hence
   `A-tilde=E-tilde/(iω)`, not `E-tilde/(−iω)`. **Fix:** change the denominator to `iω` and carry
   the resulting sign consistently into the residue language (the spectrum remains unaffected).

9. **W6 falsely says all three routes are the reference core's** (`frag-em.html:2694-2711,
   2852-2874`). Route three is a station-local copy of the GL8 nodes and weights applied to the
   core's `fieldAt(...).radiationPart`; only the field samples come from the core. This also breaks
   the header's “one stated exception” provenance claim (`:39-65`). The observer-time limits
   themselves are correct because `t_obs(s)=s+|x−r(s)|` is monotone for a subluminal trajectory, so
   the endpoint source times map exactly to the two limits used. **Fix:** label it “page-owned GL8
   quadrature of core field samples,” remove “all three routes are the reference core's,” and include
   this as a second explicit exception in the header.

10. **W7 calls the moving Coulomb profile an `ell=1` structure, but it contains an infinite multipole
   tower** (`frag-em.html:3034-3043`; source `soft_Arxiv_update.tex:553`). The source says only that
   the `ell=1` mode is nonzero. **Fix:** say “it has a nonzero `ell=1` moment (and generally higher
   moments), distinct from the usual static electric dipole moment.”

11. **W6's third route is neither controlled nor total over the full advertised control range**
    (`frag-em.html:2637-2643,2694-2706,2852-2874,2912-2922`). The fixed 32-panel rule has no
    panel-doubling check. At the allowed setting `β_i=−0.9, β_f=0.9, τ=0.4, θ=8°`, its vector result
    at `r=100` differs from 64 panels by `2.86e−6` relative (16→32 differs by `3.16e−4`), and the
    core retarded-time solve throws at the table's `r=10^4` and `10^5`; `render()` does not catch it.
    Thus a legal interaction produces an uncaught error instead of the promised table. **Fix:** use
    adaptive panel doubling with a displayed tolerance and per-row failure handling; either repair the
    large-radius solver upstream or cap/mark unsupported rows `NOT COMPUTED` instead of claiming a
    controlled solve.

12. **W6 promises last-bit agreement while exposing deliberately unconverged panel counts**
    (`frag-em.html:2637-2639,2653-2654,2684-2691`). At the default physics parameters the page's own
    recorded one-panel residual is about `2.72e−9`, not machine precision. The core's 16-panel default
    does satisfy the requested claim: I reran the page defaults and obtained relative residual
    `1.18e−16`, with both displayed components identical through 13 significant figures. **Fix:** say
    that agreement to 12 digits holds at the default/converged setting, let low-panel choices visibly
    demonstrate convergence, and gate any “12 digits” status on the measured residual.

13. **W2 draws a radiation shell when the allowed controls specify no kick**
    (`frag-em.html:899-906,1113-1117,1259-1292,1333-1338`). Setting `β_i=β_f` makes the core
    acceleration and memory identically zero, but the canvas still paints the interval between two
    timing surfaces in the radiation colour and labels it “the shell … the sideways field.” **Fix:**
    detect equal endpoint velocities, suppress the radiation band/connector styling, and show an exact
    “no kick, no radiation shell” state.

14. **W4 prints a fabricated nonzero maximum for an exactly zero pattern**
    (`frag-em.html:2021-2026,2214-2238`). All charge controls allow `Q=0` (and exact cancellations
    are also possible); when every core sample is zero, code replaces the true maximum 0 with 1 and
    reports `1` at the north pole. **Fix:** preserve `stats.max=0`, branch the logarithmic colour scale
    to a labelled zero-pattern state, and print the exact maximum 0.

## 3. BUGS

1. **W2's error-control header disagrees with the shipped integrator** (`frag-em.html:83-88,1108,
   1158,928-935`): it records `h=τ/48`; code and visible caption use `h=τ/40`. **Fix:** change the
   header record to `τ/40` and keep the convergence table tied to that shipped value.

2. **The fragment violates the token-only palette rule in every station helper**
   (`frag-em.html:1055,1733,2117,2126,2825,3327`). Five `tok` functions fall back to literal
   `#888`, and W4's parser also falls back to `[136,136,136]`, despite comments claiming that no
   literal colour exists. **Fix:** treat a missing named token as an integration error/fallback state;
   do not invent a palette value.

3. **W3 and W6 do not handle the allowed zero-kick state** (`frag-em.html:1527-1530,1754-1765,
   1873-1874,2645-2648,2895-2897,2915-2920,2958-2964`). Both slider pairs can be equal. W3 then
   divides a zero plateau by zero for its gap and has no positive chart data; W6 divides by zero in
   all relative residuals and takes `log10(0)` for the memory line. **Fix:** branch on
   `|β_f−β_i|` (or memory norm) below tolerance: print exact zero/absolute residuals, show a clear
   “no kick, no radiation/memory” empty state, and skip log plotting and relative normalization.

4. **W6's panel slider has an out-of-range array index** (`frag-em.html:2653-2654,2833-2834,
   2885-2889,2947-2948`). The input permits `S.np=6`, but `PANELS` has indices 0–5; the core silently
   falls back to 16 panels while the visible label becomes `undefined`. **Fix:** use slider indices
   0–5, or append the intended 64-panel entry and make every index explicit.

5. **W4 labels a coarse sampled maximum as the largest value anywhere on the sphere**
   (`frag-em.html:2025,2209-2239`). The hard-line directions added to the search are not peak
   locations—the leg's own transverse contribution vanishes there—and the remaining 96×192 grid
   is only a sample. For the default event, a 720×1440 scan already raises the reported maximum by
   `1.61e−4` relative. **Fix:** label it “largest sampled value (96×192 grid),” or perform and bound
   an adaptive angular maximization before claiming a global maximum.

6. **W4's colour-span prose omits hard clamps** (`frag-em.html:2007,2029-2037,2232-2238`). The text
   says the lower endpoint is the fifth percentile and the printed decades are whatever results,
   but code clamps the span to `[0.8,5]` decades. **Fix:** disclose the clamp in the caption/bar and
   label clipped endpoints, or remove it so the stated percentile rule is exact.

7. **W3's photon-table caption turns an asymptotic logarithm into an exact finite-frequency claim**
   (`frag-em.html:1643-1653`). For the smooth raised-cosine spectrum, successive low-frequency
   decades contribute asymptotically the same amount, not exactly the same amount. **Fix:** insert
   “in the soft limit/asymptotically”; retain the exact logarithm wording only for the instantaneous
   profile.

8. **W6's finite-radius “relative difference” is only one component normalized by the full memory
   norm** (`frag-em.html:2694-2706,2915-2921`). **Fix:** either compute the vector norm
   `|r∫E_rad dt−N|/|N|`, or relabel the current column “across-axis component difference / `|N|`.”

9. **W6 overexports its EM background lesson to gravitational-wave detectability**
   (`frag-em.html:2748-2751`). The plotted Coulomb drift of a test charge is not “the reason” GW
   memory is hard to see. **Fix:** keep the concrete EM detector-window lesson and, if desired, say
   only that GW memory also has foreground/noise-separation challenges, with an appropriate source.

10. **W7 says the entire station rests on antipodal matching, although its local future-null-infinity
   ledger does not** (`frag-em.html:3236-3241`). Antipodal matching is needed to identify the charges
   across `I−` and `I+`; `C_f−C_i=D_A M^A` at `I+` follows locally from the constraint and this
   solution. **Fix:** replace “everything in this station” with “the cross-null-infinity conservation
   statement.”

11. **W4's opening `sin²θ` anchor lacks its necessary nonrelativistic qualification**
    (`frag-em.html:1933-1937`). Relativistic linear acceleration has the Liénard beaming denominator,
    not a pure dipole pattern. **Fix:** say “a nonrelativistically shaken charge.”

12. **W4's “Balance the charge” action can push the last charge outside its own input range**
    (`frag-em.html:2443-2448,2483-2488`). With five same-sign, same-eta rows at `Q=3`, it sets the
    last row to `Q=−12` although the control declares `min=−3,max=3`. **Fix:** distribute the correction
    within bounds or add/replace a compensating leg whose displayed range includes the exact value.

13. **W6 presents a numerically bisected crossing as part of an exact-formula-only panel without
    naming the solve** (`frag-em.html:2722-2745,2937-2943`). **Fix:** add the controlled-numerical tag
    and state the 60-step logarithmic bisection, or omit the crossing readout.

14. **Station-global observers/listeners have no teardown path** (`frag-em.html:1057-1061,
    1450-1457,1735-1739,2148-2152,2578-2585,2827-2831,3329-3333`). They are closure-scoped, so I
    found no present name/handler collision, but reloading or replacing the fragments will accumulate
    media listeners plus document, resize, and intersection observers. Reduced-motion is also sampled
    only once. **Fix:** retain handles and expose an integrator-owned cleanup under the permitted
    `window.PROLOGUE` namespace (or a local abort/disconnect hook), and listen for reduced-motion
    changes so a running loop stops when the preference changes.

Static contract audit otherwise **PASS**: five sections, exactly one matching scoped style and station
IIFE each, plus the separately authorized `em-core` script; no duplicate IDs; all station scripts
compile; selectors are ID-scoped; no external loads; no `THREE` reference; no Promise/async path; and
no station-created global. The W2/W4 continuous loops start stopped, honor reduced motion at load, and
are gated by `IntersectionObserver`; W3/W6/W7 use only cancellable one-frame input throttles.

The answer to “does every printed number come from the core unmodified?” is **no**. W2 owns the RK4
streamline and its residual (despite the core exposing `fieldLine`); W3 visibly derives amplitudes and
relative gaps from core outputs; W4 owns the ray-cast evaluator and sampled maximum; W6 owns route
three and the crossing bisection; W7 computes display residuals from core outputs. Displayed algebraic
post-processing is not inherently a defect. The fatal provenance failures are the hidden duplicated
W4 formula and W6's false “all three routes are the core's” label; W2's page-owned solve is at least
identified as a controlled RK4 route.

## 4. Top improvements ranked by wow/effort

1. **[M — highest wow] Make W4's correct forward-zero/peak-ring geometry the interaction.** Add an
   “isolate this leg / show total interference” toggle. For an isolated massive leg, draw the exact
   zero at its marker, highlight the maximum ring `n-hat·beta-hat=β`, and show a tangent polarization
   arrow at the probe. Restoring the correct physics can make the sphere more distinctive, not less;
   the reader would see beaming and transversality at once.

2. **[S — high wow] Let W2 label the two causal fronts where the probe crosses them.** Print the
   beginning/end emission times, both exact face equations, and the angle-dependent radial width next
   to the probe; flash the probe when each front arrives. This makes the reader's first sight of the
   shell land immediately and converts the required `cτ` repair into the most legible part of the
   figure.

3. **[S] Make gauge failure visible rather than only red.** In W4's unbalanced state, add a small
   exact readout `ΔS=λ ΣηQ` under `epsilon→epsilon+λq`, while keeping the sphere explicitly
   non-observable. The current warning is responsible; a live algebraic gauge shift would make the
   reason memorable without inventing physics.

4. **[M] Give W6 a cumulative-integral trace.** Plot `E_rad^(1/r)(t)` and its running integral beside
   the endpoint rule, with the independently computed Coulomb drift on a separate axis. Adaptive
   quadrature status can sit on that trace. The identity would then read as a physical event rather
   than three rows that the reader must trust.

5. **[M] Turn W7's selected angle into a small angular patch ledger.** Show arrows entering/leaving
   the patch boundary from `M` and the local change in `C`; varying the patch size would make sphere
   divergence visually concrete. Keep the present graph and exact residual as the numerical backstop.

## 5. Keep list

- **Keep the inlined reference core.** The bytes between the marker lines have the same full SHA-256
  (`bc71fb940a41bea7e2aad7c500a10a775402ebadda307df240cb1d9911b12413`) as `em-core.js`, and
  `cmp` reports no difference.

- **Keep W2's resolved-shell strategy and explicit regulator caveat.** It uses a raised-cosine kick,
  projects the literal `fieldAt` result, and tells the reader that the instantaneous-shell ratio is not
  a number (`frag-em.html:913-924,1206-1224`). Its endpoint regions are closed-form boosted-Coulomb
  rays and the connector is an RK4 streamline of the core field, not an eased animation.

- **Keep W2's two descriptions of the Purcell flux label after repairing the face labels.** I compared
  the station's length-contraction ray followed to `|x|=t` with the core's aberrated shell direction
  over 101 directions at each of `β=−0.9,−0.73,0.2,0.73,0.9`; the largest vector residual was
  `1.35e−15`. The collinear restriction is visible in the figure caption (`frag-em.html:928-941`).

- **Keep W3's actual numerical engine and units.** `radiationSpectrum` supplies
  `α|J|²/(4π²)`, the photon-number rows call `photonNumber`, and the page correctly says they are per
  unit solid angle. My direct default rerun gave relative plateau gaps `2.51584e−8`, `2.51584e−10`,
  and `2.51543e−12` at `ω=10^−2,10^−3,10^−4`; those numbers support the quadratic correction once
  its caption and the `M`/`S_cl` sign are repaired.

- **Keep W4's event editor, explicit charge-conservation withdrawal, and labelled logarithmic map.**
  The page does not silently alter an unbalanced event; it displays `ΣηQ`, exposes a warning, and
  changes the provenance tag to “not an observable” (`frag-em.html:1984-2000,2462-2472`). Logarithmic
  scaling is stated beside and below the sphere rather than silently applied. Retain this interaction
  architecture while replacing the local physics evaluator and false peak story.

- **Keep W6's first two routes and its finite-radius window.** Running
  `memoryKickClosedForm` and `memoryKickQuadrature(...,{n:16})` with the page defaults produced
  `rN_closed=(−0.8128417900432666, 0.43219564621460455, 0)` and relative residual
  `1.18e−16`. Route three's observer-time endpoints are also exactly the images of source times
  `±τ/2`; repair its provenance, convergence, and failure handling rather than discarding the idea.
  The separate `coulombDrift` panel is the right cure for the full-field ambiguity.

- **Keep W7's local identity, numerical differentiation, and antipodal scope fence.** The core tests
  achieve `5.55e−17` analytically and `1.42e−11` with the five-point sphere derivative for
  `C_f−C_i=D_A M^A`. The page visibly says the Coulomb-profile change is the *divergence* of memory,
  not memory itself, and says the straight-line picture motivates rather than derives field matching.
  The Coulomb profile (`soft_Arxiv_update.tex:541-550`), constraint (`:699-704`), and matching equation
  (`:568-573`) are faithfully rendered after macro expansion.

- **Keep the lecture remarks.** W2's bedrock excerpt matches digest 01 lines 94–102; W7's
  asymptotic-symmetry remark matches digest 01 lines 30–37, its no-first-principles-proof exchange
  matches digest 01 lines 122–142, and the student antipode exchange matches digest 02 lines 70–76.
  All carry “Lecture remark,” video ID, and timestamp, and the rough auto-caption status is disclosed
  where it matters.

The complete core-NOTES prohibition sweep found two violations: the massive-leg “pole” language
(FATAL 1) and W6's initially unqualified whole-`E` integral (FATAL 7). The other seven prohibitions
pass: W2 uses a smooth regulated shell ratio; no visible `tanh` support claim occurs; no great-circle
connector is presented as observable; W4 withdraws gauge invariance when charge is unbalanced; W7
keeps sphere divergence distinct from the field and does not derive matching from the particle
picture; and `α/(4π²)` appears only in W3's spectrum/photon-number path.

## 6. What I could not verify

The browser/layout run is **NOT RUN**, not passed. I invoked
`node docs/outreach/auditions/prologue/qa-run.mjs --frag=frag-em.html`; localhost listening was denied
with `EPERM`, its in-memory route fallback engaged, and Chromium then died during launch with the
managed-sandbox `Operation not permitted` failure before creating a page. Therefore I could not
verify light/dark rendering at 390/768/1300 px, horizontal overflow, pointer/range/button behavior,
runtime console output, dynamic global leakage, MathJax rendering, or the visual quality of W2/W4.
No EM screenshot was produced.

The runner's pre-browser static and Node audits are hard-coded to `frag-gw.html`; `--frag` changes
only the browser query. Its printed `PASS=12, FAIL=8, WARN=2, NOT RUN=1` summary is therefore not EM
evidence and is not reported as such here. I performed the EM static audit directly and ran
`node docs/outreach/auditions/prologue/em-core.test.mjs`, which exited 0 with all core tests passing.
I did not extend `qa-run.mjs`: the additional EM falsifiers were reproducible directly against the
core and did not require a new runner check.

The lecture wording was checked against the repository digests as required, not against the original
video audio; the digests themselves identify the quoted material as auto-captions.
