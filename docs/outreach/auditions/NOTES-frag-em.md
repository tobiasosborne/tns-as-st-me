# Builder report — frag-em.html (Builder A, EM lane, tns-fse)

Lane brief: `docs/outreach/BRIEF-builder-em.md`.
Design document: `docs/outreach/BRIEF-why-prologue.md`.
Binding contract: `docs/outreach/AUDITION-SPEC.md`.
Deliverable: `docs/outreach/auditions/prologue/frag-em.html` (196 KB).

Stations built: **W2, W3, W4, W6, W7.** Nothing else was created or edited.

> **A repair round has since been applied.** See **§10, Repair round r1**, at the end of
> this file. Where §3.2, §4, §5, §7 or §8 below conflict with §10, §10 is the current
> state of the fragment.

---

## 1. Physics source

The codex core landed while station 2 was being built and is the ground truth for
everything. `docs/outreach/auditions/prologue/em-core.js` is inlined **verbatim,
byte for byte**, inside a single `<script data-station="em-core">` between the
marker lines `/* BEGIN VERBATIM em-core.js */` and `/* END VERBATIM em-core.js */`.

* inlined revision: `em-core.js`, mtime 2026-09-02 23:13:05 +0200, 28 278 bytes,
  sha256 prefix `bc71fb940a41bea7`
* `node docs/outreach/auditions/prologue/em-core.test.mjs` → **exit 0, all tests
  pass**, run by this lane after the inline (output copied in §3).
* `em-core-NOTES.md` was read in full before the final pass and its constraints
  were applied station by station (§4).

Every printed number in the fragment comes from `window.PROLOGUE.em`. There is one
stated exception, in station 2, described in §2. Nothing else in the fragment
computes physics: the only local numerics are (a) station 2's RK4 streamline
integrator, whose right-hand side is the core's `fieldAt`, and (b) station 6's
third route, an 8-node Gauss–Legendre rule (the same nodes and weights the core
uses) applied to the core's `fieldAt(...).radiationPart`. Both are labelled as
such on the page.

**No `PHYSICS: builder-implemented` marker is present** and none is needed — the
core landed and is used.

## 2. The one disagreement, and its resolution — read this before believing an
earlier draft

An earlier draft of the fragment header accused the core's `purcellLines` of using
the wrong map (relativistic aberration instead of length contraction). **That
accusation was wrong and has been retracted in the file.** The two maps describe
the same construction in different angle variables:

* Station 2 labels a field line by its angle **from the charge's present
  position**. On a fixed lab-time slice the rest-frame spoke pattern is
  length-contracted along the motion, so `tan θ_lab = γ tan θ_rest`.
* The core labels the same line by its direction **from the origin**, read off
  where the line crosses the shell `|x| = t`. That is the aberration formula.

Composing contraction with the ray/sphere intersection reproduces
`aberrateDirection` exactly. Verified numerically for β = 0.73 at
θ_rest = 0.3, 0.9, 1.6, 2.4 rad: agreement to **9 decimal digits** in every
component (the check script is in the lane scratch directory; it is four lines and
trivially reproducible). Both are right; the core's flux Jacobian identity
`C_β(A_β ℓ) dΩ_n = dΩ_ℓ` and this lane's cone-flux relation
`Φ(θ) = 2πq[1 − cos θ/√(1−β² sin²θ)]` are the same statement.

Station 2 nevertheless does **not call** `purcellLines`, for the reason
`em-core-NOTES.md` §3 gives itself: it draws a *resolved* shell (a smooth kick of
duration τ > 0), and for a resolved shell the notes say to streamline the field
rather than use the great-circle representative connector. The page therefore
streamlines the core's exact `fieldAt` across the shell and prints, live, the
residual between where the streamline lands and where the flux label says it
should. This is the only genuinely independent physics check on the page's own
geometry, and it is the number `1.2e-4` in §3.2 — see the convergence table there.

## 3. Residuals

### 3.1 The core's own harness (`node em-core.test.mjs`, exit 0)

| Check | Achieved |
|---|---:|
| retarded-time solver vs uniform-motion closed form | 1.634e-13 abs |
| LW decomposition, B = n×E, shell radial coefficient | 0 |
| RK4 streamline straightness on uniform motion | 1.617e-15 |
| Purcell flux/Jacobian identity | 8.882e-16 |
| instantaneous spectrum plateau vs formula | 4.066e-20 abs |
| radiation-spectrum GL8, 4 panels vs 64 | 2.541e-21 |
| classical soft coefficient vs Weinberg factor | 1.110e-16 |
| photon number, exact logarithm | 3.795e-19 |
| polarization sum on the sphere | 0 |
| two-route memory, 30 fixed-seed random kicks | 1.204e-15 rel |
| memory GL8, 2 panels | 1.980e-16 rel |
| Coulomb drift closed form vs GL8 | 9.065e-16 rel |
| boosted-Coulomb radial profile | 2.498e-16 abs |
| angular ledger, analytic | 5.551e-17 |
| angular ledger, 5-point sphere divergence | 1.417e-11 abs |
| Penrose tan map / free-particle antipodes | 3.553e-15 / 0 |

### 3.2 The page's own live checks, at the settings each figure opens with

| Station | Check | Value |
|---|---|---:|
| W2 | streamlined shell exit angle vs closed-form flux match, worst over 22 lines | **1.2e-4** |
| W2 | \|E⊥\|/\|E_r\| just outside the shell (must be 0) | 0.00 |
| W3 | quadrature vs ω→0 closed form at the lowest plotted ω | 2.52e-8 |
| W3 | classical soft coefficient vs `softFactorWeinberg` | 0 |
| W3 | Σ ηQ over the two legs | 0 |
| W4 | `spherePattern` vs sum over two explicit orthonormal polarizations | **5.33e-15** |
| W6 | `memoryKickQuadrature` vs `memoryKickClosedForm`, relative | **1.21e-16** |
| W6 | same, at 1 / 2 / 4 panels | 2.72e-9 / 2.88e-12 / 0 |
| W6 | finite-r route: relative difference × r at r = 10²…10⁵ | 0.004854 / 0.004853 / 0.004853 / 0.004850 |
| W7 | closed-form ledger vs 5-point `sphereDivergence`, h = 1e-4 | **2.17e-12** |
| W7 | \|n̂_past + n̂_future\| | 0 |

The W2 residual is discretisation of the streamline and nothing else, and this was
settled rather than assumed. Halving the RK4 arclength step divides it by about
four, monotonically, over five halvings — second order, which is the rate this
scheme should give once the last step is walked back to the exact crossing of the
outer shell face (that back-off is in the shipped code):

| step | worst residual | ratio |
|---|---:|---:|
| τ/10 | 2.914e-3 | |
| τ/20 | 5.139e-4 | 5.67 |
| τ/40 (shipped) | 1.217e-4 | 4.22 |
| τ/80 | 3.367e-5 | 3.62 |
| τ/160 | 7.258e-6 | 4.64 |
| τ/320 | 2.049e-6 | 3.54 |

So the flux-label map is exact and the printed number measures the drawing, not the
physics. The figure caption states the rate.

The W3 gap of 2.5e-8 is **not** quadrature error: raising the panel count eightfold
does not move it, and it falls in exact proportion to ω (2.5e-8, 2.5e-10, 2.5e-12
at ω = 1e-2, 1e-3, 1e-4). It is the first physical correction in ωτ. The page says so
in the figure caption.

The W6 finite-r column is the strongest single result on the page: the third route
never uses the r → ∞ formula, and its disagreement with the closed form, multiplied
by r, is constant to four figures over three decades of r. That is what "of order
1/r" means, demonstrated rather than asserted.

## 4. Compliance with `em-core-NOTES.md`

Every item on the notes' "things the page must not say" list was checked against
the copy:

| Prohibition | How the page complies |
|---|---|
| not "the DC field is the whole time integral of E" | W6 devotes a whole figure and a boxed paragraph to the opposite, with `coulombDrift` plotted separately and the crossing window printed |
| not "the Coulomb-profile difference equals the DC radiation field" | W7 says **sphere divergence** everywhere, quotes the notes' builder-safe sentence, and prints \|M\| as a separate row explicitly labelled "a different number" |
| no unregulated instantaneous-shell E⊥/E_r | W2 uses a smooth kick with a slider-set τ, prints the literal `fieldAt` ratio, and carries a caveat paragraph saying the ratio has no τ→0 limit |
| don't call the great-circle connector an observable field line | the connector is never used; W2 streamlines the resolved field |
| don't call `tanh` compactly supported | `tanh` is not used anywhere in the fragment |
| don't claim massive legs make literal poles | W4's heading was changed from "its own pole" to "a bright spot", and the body states 1 − n̂·β ≥ 1 − β > 0 and that a true collinear pole needs a null leg |
| don't present a charge-nonconserving pattern as a gauge-invariant event | W4 shows a Σ ηQ chip, a red-ruled banner that appears when unbalanced and withdraws the claim, and a provenance tag that changes to "Exact formula — not an observable"; the "Balance the charge" button is user-initiated, never automatic |
| don't say the straight-line antipode argument derives the matching condition | W7 quotes the notes' builder-safe sentence verbatim and then Strominger's own admission that he knows no first-principles derivation |
| don't multiply field/memory by α/4π² | that prefactor appears only in W3's spectrum and photon number, which is where the core puts it |

The two "builder-safe sentences" the notes supply (classical/quantum in §4,
two-route memory in §6, per-angle in §7, antipodes in §8) are quoted on the page
with quotation marks and attributed to the reference core.

TeX line references were corrected to the notes' numbers: `:541-550` (Coulomb
angular coefficient), `:568-573` (antipodal matching), `:699-704` (the abelian
constraint), `:1075-1082` (the soft photon theorem). The lecture remarks are
`[lvyyxkjwSCg @ 00:35:17]` (W2), `[yeMZKViadhw @ 01:12:34]`,
`[lvyyxkjwSCg @ 01:26:02]` and `[lvyyxkjwSCg @ 00:01:06]` (W7), each tagged
"Lecture remark", each said to be auto-captions, none load-bearing.

## 5. What each station is

* **W2 — the bedrock.** 2-D canvas. A charge drifting at β_i is kicked to β_f over
  a duration τ; drag the arrow to set the kick's size and direction, drag anywhere
  else to move a probe around the shell, four sliders and a play button. The two
  straight regions are Heaviside's boosted Coulomb field in closed form, drawn as
  rays from the correct extrapolated positions; the two shell boundaries are the
  exact (non-concentric) spheres about where the charge sat when the kick began and
  ended; the connector is an RK4 streamline of the core's `fieldAt` with arclength
  step τ/40. Live readout of \|E⊥\|, \|E_r\| and their ratio at the probe, plus the
  same ratio just outside the shell (zero), plus the streamline residual. Scope
  fence in the caption: the construction is exact for a collinear kick, and a
  direction-changing kick is a Poisson problem on the shell this page does not solve.
* **W3 — the same event in frequency.** Two stacked log-log SVG charts: the exact
  energy spectrum with the closed-form soft plateau as a dashed asymptote, and the
  amplitude with the 1/ω pole against its reference line. Sliders for β_i, β_f, τ,
  direction and a marker frequency. Weinberg's theorem quoted verbatim from
  `:1075-1082` with the paper's macros expanded and named. A live two-row ledger
  comparing `softAmplitude` with `softFactorWeinberg`, honestly labelled as a
  typo check rather than evidence. A photon-number panel with a log ω_min slider
  and a table showing that each further decade adds the same amount.
* **W4 — the celestial sphere.** A scattering-event editor (2–5 lines; incoming or
  outgoing, integer charge, speed slider, delete) over an interactive sphere painted
  per pixel with `spherePattern` by orthographic ray casting. Drag to rotate, drag a
  marker to aim that line, wheel to zoom, hover to probe, and an idle spin button.
  Adaptive logarithmic colour scale whose span is printed. Live polarization-sum
  identity check at the probe.
* **W6 — the two-route identity.** Three routes to the radiation-order memory
  coefficient, printed to 13 significant figures with the difference, the relative
  residual, a panel-doubling convergence table, and a finite-r table demonstrating
  1/r convergence. Then a separate closed-form figure of the Coulomb drift against
  the observing-window length, with the crossing window printed, and a boxed
  paragraph saying exactly what the page does *not* claim.
* **W7 — one conservation law per angle.** The Coulombic profile and the constraint
  equation quoted from the TeX; the per-angle identity C_f − C_i = D_A M^A stated as
  the notes state it; two stacked charts (the two profiles; their difference with the
  numerical sphere divergence drawn as markers on top of it) and a live ledger with
  the residual. Then the antipodal interlude: a conformal diagram with the exact
  `penroseCoords` map, a companion circle of directions, `freeParticleEndpoints`
  printed, the student's remark, the honest caveat, and the closing "I kind of
  dislike this word asymptotic symmetries" quote.

## 6. QA

Run through the codex lane's own harness,
`qa-harness.html?frag=frag-em.html`, driven by Playwright chromium 1.62.1.

* **JS errors: none.** Six configurations (light and dark × 390, 768, 1300 px),
  each after an interaction stress pass that swept all **26 range inputs** to both
  ends and the midpoint, set all **4 number inputs** to 3, 0 and back, flipped all
  **4 selects**, clicked all **11 buttons** (add / balance / reset / play / spin /
  view), then dragged and wheel-zoomed the W4 sphere and dragged inside the W2
  canvas. Zero `pageerror`, zero console errors, in every configuration.
* **No readout ever degraded** to an em dash, an empty string, `NaN`, `Infinity`
  or `undefined` after that stress pass, in any configuration.
* **Horizontal scroll: none.** `document.scrollWidth − clientWidth = 0` at all
  three widths in both themes. A per-element audit at 390 px found **zero**
  elements escaping the viewport without an ancestor `overflow-x: auto` that is
  itself inside it; the wide MathJax displays and the wide tables scroll inside
  their own `.eq` / `.w3-tabwrap` / `.w6-tabwrap` / `.w7-wrap` containers
  (measured `scrollWidth` up to 640 px inside a 362 px box).
* **Both themes** were rendered and inspected. Every colour is read at run time
  from the proof-atlas tokens with `getComputedStyle`; the canvases re-read them on
  a `prefers-color-scheme` change and on a `data-theme` mutation, so a theme toggle
  repaints correctly without a reload. The W4 sequential ramp inverts as it should
  (light surface: pale → deep accent; dark surface: near-surface → bright accent),
  because it is built from tokens rather than literals.
* **three.js absent:** the fragment contains **zero** references to `THREE` and
  loads no library, so it is unaffected either way. See §7 for why.
* **`prefers-reduced-motion`** disables the W2 playback and the W4 spin (both start
  stopped regardless), and both animation loops are additionally suspended by an
  `IntersectionObserver` when their canvas is off screen.
* MathJax rendered every display in the fragment; the harness reported
  `mathjax: loaded`.

Screenshots at all three widths in both themes are in the lane scratch directory
(not committed).

## 7. Known gaps and judgement calls

1. **W4 is drawn on a 2-D canvas, not with three.js.** The lane brief asked for
   three.js with a hand-rolled fallback; `BRIEF-why-prologue.md` (the design
   document the lane brief points at) grants "three.js … or hand-rolled projection
   — builder's choice". The choice made here is the hand-rolled one, on grounds
   that are about the physics and not about effort: painting the sphere by
   orthographic ray casting evaluates `spherePattern` **once per output pixel at
   the direction that pixel actually represents**, with no mesh tessellation and no
   texture resampling between the formula and the reader's eye. A textured
   `SphereGeometry` would interpolate the data twice. It also removes a library
   dependency and a WebGL failure mode entirely. The cost is real and is stated
   here: the sphere is orthographic, so there is no perspective and no camera
   dolly, and repainting is CPU work (440 samples across the disc at rest, 210
   while dragging, which is fast but not free). If the integrator wants the
   three.js version, the clean seam is `paintSphere()`: replace it with a texture
   painter and keep everything else.
2. **File size is 196 KB, above the 120–180 KB target.** 28 KB of that is the
   verbatim core, which the integrator may want to hoist out of the fragment and
   load once for the whole page; that would bring the fragment to 168 KB. The rest
   is prose, five `<style>` blocks and five station scripts.
3. **W2 keeps the kick collinear.** A kick that changes direction leaves the outer
   field axisymmetric about one axis and the inner field about another, and the
   line-matching across the shell then requires solving a Poisson equation on the
   sphere. That is honest work and it is not done; the caption says so rather than
   drawing something plausible. The "direction" control rotates the whole
   configuration and sets the speed, which is exact.
4. **W3's photon number is per unit solid angle**, at the selected direction, not
   integrated over the sphere. The log divergence is the point and it is visible
   per angle; a sphere integral would have needed a second quadrature layer for no
   extra physics. The row label says "per unit solid angle in this direction".
5. **W7's conformal diagram has a dotted segment** where the particle passes its
   closest approach. This is not a bug and not a hidden approximation: a conformal
   diagram suppresses the angles, so a trajectory that misses the origin cannot be
   drawn continuously across a signed radial axis. The segment is dotted and the
   caption explains it, and it shrinks to nothing as the closest approach goes to
   zero.
6. **W7 stops short of the symmetry corner.** Turning the per-angle conservation
   laws into symmetry generators and their Ward identities into the soft theorem is
   reported, with the TeX line, not derived. That is deliberate and is stated in
   the body.
7. The W3 and W4 "identity checks" are, by construction, checks that two routines
   implementing the same algebra agree. The page says so in both places rather
   than dressing them as independent evidence. The genuinely independent checks are
   W2's streamline residual, W6's finite-r route, and W7's five-point sphere
   divergence.

## 8. Three design decisions to preserve

1. **Two colours, one meaning, five stations.** `--keep` is the Coulombic / hard /
   "before" class and `--die` is the radiative / soft / "after" class, everywhere:
   the shell connectors in W2, the spectrum curve in W3, outgoing lines in W4, the
   memory line in W6, the after-profile in W7. A reader who learns the code once
   can read every figure. Please do not re-map these per station when assembling,
   and please keep `--die` reserved for radiation rather than spending it on rail
   highlights or link states.
2. **The interface gets plainer where the numbers decide.** Every station ends in
   an unstyled bordered ledger — mono, tabular figures, a dotted rule per row, no
   card, no shadow, no icon — and the decisive row is the only coloured one. The
   charts above them are allowed to be beautiful; the ledgers are not. This is the
   spec's register rule made structural, and it is what makes the residuals read as
   evidence rather than decoration.
3. **Every scope fence is in the figure caption, not in a footnote or a
   disclosure.** The collinear restriction in W2, the adaptive colour span in W4,
   the finite-window caveat in W6, the dotted crossing in W7: each sits directly
   under the thing it qualifies, in the caption, in the same voice as the rest.
   If the integrator adds a global "limitations" section, these should stay where
   they are as well — a reader who scrolls past a caption has been told, and a
   reader who never reaches an appendix has not.

## 9. For the codex critic

The three places most worth attacking, in order:

1. W6's third route. The observer-time window is taken to be
   `[-τ/2 + |x − r(−τ/2)|, τ/2 + |x − r(τ/2)|]`, which is exactly the shell passage
   for that detector; if that window is even slightly wrong the 1/r scaling would
   still look right while the constant was off. The constant 0.004853 is stable to
   four figures over three decades of r, which is suggestive but is not a proof
   that the window is exactly right.
2. W3's statement that the printed low-frequency gap is the first correction in ωτ.
   The evidence is that it is panel-count-independent and exactly linear in ω over
   three decades. Linear in ωτ, not quadratic, is worth someone checking against
   the raised-cosine's own expansion.

---

## 10. Repair round r1

Lane: bd `tns-as`. Input: `docs/outreach/critic-frag-em-r1.md` (codex, 14 FATAL + 14 BUGS +
5 ranked improvements + keep list + a "could not verify" section). Three files were touched:
`docs/outreach/auditions/prologue/frag-em.html`, `docs/outreach/auditions/prologue/qa-run.mjs`
(two runner bugs plus two hard-coded rows, see §10.5) and this note. Scratch work lives
outside the repo.

Every item was checked against the code, the reference core and the mathematics before
anything was changed; short node scripts against `em-core.js` are quoted as evidence below.
**The critic was right on all 14 FATAL items and all 14 BUGS.** Two items were applied in a
different form from the one prescribed, and those are marked PARTIAL with the reason. Nothing
was rejected — the one place worth flagging is that a *prescription* was declined, not a
finding (FATAL 4).

The inlined core is untouched and still byte-for-byte identical:
`sha256(inlined) = sha256(em-core.js) = bc71fb940a41bea7e2aad7c500a10a775402ebadda307df240cb1d9911b12413`.
`node docs/outreach/auditions/prologue/em-core.test.mjs` still exits 0.

### 10.1 FATAL items

**1 — W4's bright-spot/pole account was false for the pattern it plots. APPLIED.**
Verified from the core, not from the report. For one leg
`P_one(θ) = Q²β² sin²θ/(1−β cos θ)²`; `dP/d(cos θ) ∝ β − cos θ`, so the maximum is the ring
`cos θ = β` with value `Q²β²/(1−β²) = Q²β²γ²`. A 200 001-point scan of `P.spherePattern`
against that closed form: argmax `cos θ = 0.500000 / 0.900000 / 0.990000` for
`β = 0.5 / 0.9 / 0.99`, maxima `0.33333333 / 4.26315789 / 49.25125628`, matching
`β²/(1−β²)` to every printed digit; `P.spherePattern([leg], β̂)` returns **exactly 0**, while
`(1−β)⁻²` would be `4 / 100 / 10000`. The ratio of the two maxima the page compared is
`147.75`, not four orders of magnitude.
What changed: the station heading is now "Every hard particle paints a ring on the sky, with
an exact zero at its centre"; a new displayed equation gives `P_one`, its derivative, its ring
and its maximum with the numbers above; the canvas `aria-label` and the no-canvas fallback text
both describe the ring and the central zero; the caption's `(1−β)⁻²` scaling claim is replaced
by `β²γ²` with the factor `148`. The `:2038-2040` sentence about `S` "pointing radially" is
replaced: it is the **unprojected** `H = Σ η Q β/(1−n̂·β)` that is radial on those ribbons, and
`S` is what survives after that radial part is removed. The `:2043-2049` merging claim now says
two lines combine into one only when their **full velocities** are equal, and states explicitly
that matching directions at different speeds gives rings of different radii that do not merge.

**2 — W4 reimplemented the physics locally; "nothing here is interpolated" was false. APPLIED.**
Verified by reading `paintSphere`: it rebuilt `H`, projected and squared it per texel, and the
440/210 texture was drawn with `imageSmoothingEnabled = true`.
What changed: `P.spherePattern(soloParts(), n)` is now the **sole** texel evaluator — the local
loop is gone — and the texture size is `min(cap, round(2·R_disp))`, so it never over-samples the
display. The label under the sphere is generated at run time and states the size in use and
whether the display is one texel per device pixel or an explicit upscale factor. The caption's
"nothing here is interpolated" is replaced by an honest pipeline description naming the
bilinear resample as the one interpolation in the figure. Cost measured before committing to
this: `P.spherePattern` over the disc takes 42 ms at 440² and 25 ms at 210² in the same V8 that
runs the page.

**3 — W3 called an even-in-ω correction linear. APPLIED.**
Verified at the page defaults: relative gap `2.515836e-8 / 2.515839e-10 / 2.515427e-12` at
`ω = 10⁻², 10⁻³, 10⁻⁴` — a factor of a hundred per decade, i.e. quadratic. Divided by `(ωτ)²`
the coefficient is `3.10597e-2` at `τ = 0.09`, `0.18` **and** `0.36`, so the correction really
is `(ωτ)²` and not merely `ω²`. The caption now says "of order `(ωτ)²`", explains why the linear
term is absent (`|J(ω)|²` is even because the time-domain pulse is real), states that the gap
falls by a hundred per decade, and quotes the measured coefficient.

**4 — W3 equated two coefficients of opposite sign. APPLIED as to substance; PARTIAL as to the
prescribed renaming.**
Verified directly: at the defaults `M·ε = +0.7493910580945078` from `dcRadiationField` while
`softAmplitude = −0.7493910580945075` and `softFactorWeinberg = −0.7493910580945075`; their sum
is `3.33e-16`. The identity is elementary — `n̂×(n̂×A)·ε = −A·ε` for transverse `ε` — and the
core notes record it (`em-core-NOTES.md` §4).
What changed: the eq-note no longer says "an overall sign lives in the convention"; it names the
scalar `S_cl = [β_f/κ_f − β_i/κ_i]·ε`, derives `S⃗·ε = −S_cl` in one line, and writes Weinberg's
bracket as `Q S_cl/ω = −Q S⃗·ε/ω`. The ledger row that was mislabelled now says what it is
("classical current coefficient `S_cl`, from `softAmplitude`"), and two rows were added: the
projection `S⃗·ε` (which prints `−S_cl`) and their sum, which prints `~1e-16`.
**PARTIAL:** the critic also asked that the vector be *renamed* `M`/`J(0)`. That was declined.
`S⃗(n̂)` is the name the displayed closed form gives it, it carries through the whole of W4, and
the page already calls the same object `N⃗` in W6 and `M⃗` in W7 where the sources use those
letters; a fourth renaming would have made the cross-station story worse, not better. The
substantive requirement — that the displayed relation be the true one and that no row be
labelled as something it is not — is met.

**5 — the W3 source was not verbatim. APPLIED (the critic's route A).**
Verified line by line against `refs/arxiv-1703.05448/soft_Arxiv_update.tex`: the old display
expanded five macros, reordered `p^{out}_k` to `p_k^{out}`, normalised spacing and dropped the
closing `~.`; the prose excerpt began mid-sentence; and "the leading order term … is a pole" is
line **1083**, outside the cited `:1075-1082`.
What changed: a marked source block reproduces lines **1075–1083** character for character —
diffed programmatically against the TeX, including the trailing spaces on 1077, 1078, 1079 and
1083 — inside a `<pre>` so MathJax leaves it alone (`<pre>` is in MathJax 3's default
`skipHtmlTags`; the belt-and-braces classes `mathjax_ignore tex2jax_ignore` are also on it).
This mattered: before the `<pre>`, MathJax typeset the `\begin{equation}` inside the block and
mangled it, which the first screenshot pass caught. Below it, the same equation is typeset with
only the five abbreviations replaced by their definitions — same sub/superscript order, same
`O(q⁰)`, same closing `~.` — and the note names each macro with its defining line
(`\ve` line 60, `\cs` 228, `\co` 229, `\outst` 230, `\inst` 231). The pole sentence is now cited
as `:1083`.

**6 — W2's prose and canvas contradicted its own retardation geometry. APPLIED.**
Verified at the page defaults (`β_i = 0`, `β_f = 0.55`, `τ = 0.09`, `t = 0.70`):
`r(−τ/2) = −0.00449683`, `r(+τ/2) = +0.02025317`, separation `0.02475 = β_f τ/2` exactly, and
the radial width from the origin runs `0.06525` at `0°` to `0.11475` at `180°` while `cτ` is
`0.090` — the critic's numbers, reproduced.
What changed: the "no point further away than `ct`" paragraph is replaced by an exact statement
of the two faces, and a new displayed equation gives them:
`|x − r(−τ/2)| = c(t + τ/2)` and `|x − r(+τ/2)| = c(t − τ/2)`, with an eq-note saying the
spheres have different centres, that the radial gap is angle-dependent and **not** `cτ`, that
`cτ` is the source-time duration, and quoting the `0.0653 … 0.1148` range. The canvas corner
label is now "page time `c t`" instead of "shell radius `c t`"; the legend row is "between the
two faces: the sideways field"; the two circles carry drawn labels "outer face" / "inner face";
and the readout prints `r_out`, `r_in` and their difference beside `cτ` at the probe's own angle.

**7 — W6 asserted the unqualified `∫E dt` equality and only retracted it later. APPLIED.**
What changed, in this order on the page: the impulse anchor now carries the test-body coupling
`Δv = (q_test/m_test)∫E_source dt`; the very next paragraph says that at a real detector that
integral is not one thing, because the field has a `1/r²` Coulomb part whose drift grows with
the window, and points at the second figure; only then does a displayed equation introduce the
quantity that is actually equated, `∫ E_rad^{(1/r)} dt = N⃗(n̂)/r`, with the integral written
out. Its eq-note states that everything printed is `N⃗` per unit source charge with the source
charge and `q_test/m_test` stripped out, and how to put them back. The Fourier equation now
carries `E_rad^{(1/r)}` in both places rather than a bare `E`. No later correction is relied on
to cure an earlier statement.

**8 — W6's vector-potential Fourier sign was wrong. APPLIED.**
Verified: with `Ẽ(ω) = ∫dt e^{iωt}E(t)` and `E = −∂_t A`, integrating by parts gives
`Ẽ = +iω Ã`, hence `Ã = Ẽ/(iω)`, not `Ẽ/(−iω)`. The eq-note now shows the integration by parts,
gives `Ã(ω) = Ẽ(ω)/(iω)` and states the residue as `N⃗/(i r)` rather than silently calling it
"the memory".

**9 — "all three routes are the reference core's" was false. APPLIED.**
Verified by reading the station script: route three's GL8 nodes, weights, panel loop and
observer-time window are all local; only `fieldAt(...).radiationPart` comes from the core.
What changed: the fragment header now says **TWO** stated exceptions and describes route three
as page-owned quadrature of core field samples; the figcaption says two of three routes are the
core's and names them; and the note above the table opens with "Whose arithmetic this is".

**10 — W7 called the moving Coulomb profile an `ℓ=1` structure. APPLIED.**
Verified by numerical Legendre projection of `C_β(cos θ) = (1−β²)/(1−β cos θ)²`. At `β = 0.72`
the coefficients for `ℓ = 0…4` are `1.0000, 1.6370, 1.3682, 0.9216, 0.5561` — an infinite tower,
with `ℓ=2` nearly as large as `ℓ=1`. At `β = 0.9`, `ℓ=3` is *larger* than `ℓ=1`.
The source (`:553`) says only that "the `ℓ = 1` mode of the distribution over the sphere is
nonzero" and that this is "not to be confused" with the usual electric dipole moment. The
eq-note now says the profile has a nonzero `ℓ=1` moment and generally nonzero moments at every
`ℓ`, quotes the five coefficients above, and keeps the source's actual point — the `ℓ=1`
moment is not the classical dipole moment — with the line citation.

**11 — W6's third route was neither controlled nor total over its advertised range. APPLIED.**
Verified: at the legal setting `β_i = −0.9, β_f = 0.9, τ = 0.4, θ = 8°`, the fixed 32-panel rule
differs from 64 panels by `2.859e−6` relative at `r = 10²` and `10³`, and the core's
`retardedTime` **throws** `retarded-time solve did not reach tolerance` at `r = 10⁴` and `10⁵`;
`render()` did not catch it, so the whole station stopped drawing.
What changed: `farField` now doubles panels from 32 up to 512 until the vector moves by less
than `10⁻¹⁰` relative, reports the count it settled on as a new table column, and wraps every
core call so that a non-convergent radius produces a `NOT COMPUTED` row naming the reason
instead of an exception. Live at that hostile setting the table now reads
`10²: 256 panels, 1.04e−3`; `10³: 256 panels, 1.04e−4`; `10⁴, 10⁵: NOT COMPUTED — the
retarded-time solve did not converge at this radius`, with `×r` constant at `0.1044 / 0.1043`.
At the default settings all four radii compute, at 64 panels, with `×r` constant at
`0.005001 / 0.005000 / 0.005000 / 0.004999`.
*Diagnosis for the core lane, not a page defect:* `retardedTime` uses a fixed **absolute**
tolerance of `1e−13` on `t − s − |x − r(s)|`, while `ulp(t)` is `1.8e−12` at `t ≈ 10⁴` and
`1.5e−11` at `t ≈ 10⁵`. The residual is simply not representable below the tolerance there.
Sampling 41 observer times across the window: 0 failures at `r = 10³` and `10⁴`, 4 of 41 at
`r = 10⁵`; the quadrature nodes hit the failures earlier because there are more of them. A
relative tolerance in the core would fix this upstream.

**12 — W6 promised last-bit agreement while exposing unconverged panel counts. APPLIED.**
Verified at the page defaults: relative residual `2.724e−9 / 2.882e−12 / 0 / 2.355e−16 /
1.178e−16 / 3.771e−16` at `1 / 2 / 4 / 8 / 16 / 32` panels. The default slider position is 16
panels and does reach `1.18e−16`; the promise was false only for the low-panel settings the
slider can reach.
What changed: the chart sub-heading says agreement to twelve figures holds "at the converged
default" and invites the reader to turn the panels down and watch it break; the residual row is
gated on the number it just measured and prints one of "0 at binary64 precision", "…—twelve
significant figures or better", or "…— short of twelve figures at *n* panels; the converged
default is 16". Live: `1.52e−3 — short of twelve figures at 1 panel` and
`1.84e−16 — twelve significant figures or better` at 32.

**13 — W2 drew a radiation shell when the controls specified no kick. APPLIED.**
Verified: `makeKick` with `betaI = betaF` gives `Δβ = 0`, so acceleration and the core's
radiation part are identically zero, yet the canvas painted the band in `--die` and the legend
called it "the shell … the sideways field".
What changed: `noKick()` (endpoint speeds equal to `1e−9`) now suppresses the band fill, draws
the connector segment as an ordinary field line rather than in the radiation colour, draws the
two circles in `--rule-2` as plain timing surfaces, changes the legend row to "no kick: no
radiation, no shell", and raises a readout banner saying that the sideways field printed below
is the ordinary boosted Coulomb field seen from the origin and not radiation. Live at
`β_i = β_f = 0` the banner is shown and the ratio row reads `1.57e−16`.

**14 — W4 printed a fabricated maximum for an exactly zero pattern. APPLIED.**
Verified: `stats.max = best > 0 ? best : 1` replaced a true maximum of 0 with 1, and the readout
then reported `1` at the north pole.
What changed: `stats.zero` is carried explicitly; the true maximum `0` is kept; the readout
prints "0 exactly — the pattern vanishes in every direction"; the colour bar reads "(the pattern
is identically zero here)" and its ticks collapse to a single `0`; and the painter fills the
disc with the bottom of the ramp instead of taking a logarithm of zero. Live with every charge
set to 0, all three of those strings appear and `P(n̂)` prints `0.000000`.

### 10.2 BUGS

**1 — the header's error-control record disagreed with the shipped integrator. APPLIED.**
`HSTEP = 40` and the visible caption both say `τ/40`; the header said `τ/48`. Header corrected.

**2 — the token-only palette rule was violated in every station helper. APPLIED.**
Five `tok` functions fell back to `'#888'` and W4's parser to `[136,136,136]`. A missing token
is now an **integration error**: `console.warn` naming the token and the station, a
`data-token-error` attribute stamped on the station root, and — for drawing only — the host
page's own computed text colour, which is a value belonging to the host rather than one this
fragment invented. W4's colour parser was split into `parseColour` (returns `null` on failure)
and `hex` (reports, then falls back to the host colour); `buildLUT` refuses to build a ramp from
an unreadable anchor and sets `lutFailed`, and `paintSphere` returns rather than painting in an
invented hue. **No colour literal remains in the fragment** (the hex codes in the header comment
are a record of what the GW lane validated and are excluded from every scan, as they were
before; a note in the header now says so). Browser check at all six configurations:
`palette token errors: none`.

**3 — W3 and W6 did not handle the allowed zero-kick state. APPLIED.**
Verified: with `β_f = β_i`, W3's `gap = |spec[0] − plateau|/plateau` was `0/0` and both charts
had no positive data; W6's relative residuals were `0/0` and `drawDrift` took `log10(0)`,
producing an SVG path of `NaN`s.
Both stations now branch on `|β_f − β_i| < 1e−9`. W3 prints "not defined: plateau and spectrum
are both exactly zero", the `ω|A|` row prints "zero — there is no pole", and a banner explains
that the charts are blank because the amplitude is identically zero rather than being drawn with
an invented floor. W6 prints absolute differences in place of relative ones (labelled "(abs)"),
its convergence and finite-`r` tables switch to absolute columns, the crossing row says "the
memory is exactly zero, so the drift is larger at every window", and `drawDrift` skips the level
line and its decade rather than reaching `log10(0)`. Live: no `NaN`, no `Infinity`, no blank
readout anywhere in the interaction sweep.

**4 — W6's panel slider had an out-of-range index. APPLIED.**
`PANELS` has indices 0–5 and the input allowed `1…6`; at 6 the core silently used its 16-panel
default while the label printed `undefined`. The input is now `min="0" max="5" value="4"` (which
is still 16 panels at load), and `render` clamps the index as well. Both ends verified live:
index 0 → label `1`, index 5 → label `32`.

**5 — a coarse sampled maximum was labelled the largest value anywhere. APPLIED, and improved.**
Verified: the 96×192 scan gave `12.339404380` for the default event while a 720×1440 scan gave
`12.341393472` (`+1.61e−4` relative, the critic's number) and a 2000×4000 scan `12.341408538`.
The hard-line seeds were useless because each leg's own term vanishes along its velocity.
What changed: the row is relabelled "largest value **found** on the sphere"; the search is
seeded at each leg's beaming ring `cos θ = β` (64 points per leg) as well as its direction, and
the best sample is then refined by six shrinking 5×5 tangent-plane searches, ending at a step of
about `4.5e−5` rad. The caption states all of this and says it is a search, not a proved global
maximum. Live the page now reports `12.341422`, above the 2000×4000 grid scan.

**6 — the colour-span prose omitted the hard clamp. APPLIED.**
The `[0.8, 5]`-decade clamp is now disclosed twice: the bar label prints
"(1.4 decades, span clamped to 0.8–5)" and appends "at the lower stop" / "at the upper stop"
when the clamp is what is deciding, and the caption explains why the clamp exists.

**7 — the photon table turned an asymptotic logarithm into an exact claim. APPLIED.**
Verified: consecutive decade gains are `2.39022229e−4` at `ω_min = 10⁻³` and `2.39022231e−4`
below that — equal to eight figures but not exactly equal, so "adds the same amount" was wrong
in principle even though the table's five printed decimals cannot show it. The caption now says
"asymptotically", explains that the spectrum is only flat below `1/τ`, and reserves the exact
statement for the instantaneous kick.

**8 — the finite-radius "relative difference" was one component over the full norm. APPLIED.**
Now the full vector norm `|r∫E_rad dt − N⃗|/|N⃗|`, with the column head written that way. The
`×r` column consequently reads `0.005001 / 0.005000 / 0.005000 / 0.004999` at the defaults where
it previously read `0.004854 / …`; still constant to four figures over three decades.

**9 — the EM background lesson was exported to gravitational-wave detectability. APPLIED.**
The caption now makes the concrete statement about this electromagnetic detector — the window
must be long compared with the burst and short compared with the light travel time — and says
explicitly that GW memory has its own separation problem and that this figure is not evidence
about it.

**10 — W7 said the whole station rests on antipodal matching. APPLIED.**
The footer now separates the two: `C_f − C_i = D_A M^A` is a **local** statement at `I⁺` that
follows from the constraint and this solution and needs no matching condition, while what needs
the antipodal identification is the conservation law *across* null infinity, because without an
identification of the two spheres there is nothing to equate.

**11 — the `sin²θ` anchor lacked its nonrelativistic qualification. APPLIED.**
The lede now says "a charge shaken *gently* … nonrelativistically, so that the usual dipole
formula applies", and adds that relativistic motion tilts the doughnut forward through the
beaming denominator but does not fill in the hole.

**12 — "Balance the charge" could push a row outside its own input range. APPLIED.**
Verified: with `n` same-sign, same-`η` rows at `Q = 3` the old code wrote `Q = 3 − nΣ` into an
input declaring `min="-3" max="3"`.
The correction is now spread over the existing rows from the last backwards, never leaving
`[−3, 3]` on any row; if a remainder survives and there is room, a new line is added carrying
exactly it; if neither is possible the chip says so ("… left over; every charge is at ±3 and
there is no room for another line") and the unbalanced warning stays up. Live with four
outgoing rows at `Q = 3` (`Σ ηQ = 12`), the button produces `3, 3, −3, −3` — `Σ ηQ = 0`, every
value inside its declared range, no new row needed.

**13 — a numerically bisected crossing sat in an exact-formula-only panel. APPLIED.**
The panel now carries the "Controlled numerical solve" tag as well, the readout row says "by
bisection in `log T`", and the note describes the method: sixty bisection steps in `log T`,
legitimate because the drift increases with the window — checked over six decades of window at
five settings spanning the sliders — while the memory does not depend on it at all.

**14 — station-global observers and listeners had no teardown. APPLIED.**
All five stations now keep handles for the `prefers-color-scheme` media listener and the
`data-theme` `MutationObserver`, and unhook both the first time they fire after
`root.isConnected` goes false; W2 and W4 do the same for their `IntersectionObserver`,
`ResizeObserver` and window-resize fallbacks, and their animation frames bail out on the same
test. Reduced motion is no longer sampled once: both stations listen for changes and stop a
running loop when the preference turns on. The critic offered a `window.PROLOGUE` cleanup
registry *or* a local hook; the local hook was taken, because the harness's globals check reads
`Object.getOwnPropertyNames(window)` before and after and the fragment's one authorised global
is already the core's.

### 10.3 Improvements

**#2 (S) — W2 labels the causal fronts where the probe crosses them. APPLIED.**
The probe now carries a radius as well as an angle (dragging sets both), so it can be parked
outside the shell and watched. The readout prints, at the probe's own direction: where it is
("outside the outer face, nothing has arrived yet" / "inside the shell" / "inside the inner
face, the news has passed"), the two face equations with the radius each has there, the radial
width in that direction beside `cτ`, and the two page times at which the faces reach it,
attributed to the source times `∓cτ/2`. On the canvas the two circles are labelled and the probe
marker grows and turns to the radiation colour while a face is within `0.018` of it, with a tag
saying which one. Live at the defaults: `r_out = 0.7413`, `r_in = 0.6714`, width `0.0700`
against `cτ = 0.090`, arrivals at `ct = 0.667` and `ct = 0.737` for `ct = 0.700` now — the
time separation equalling the radial width, as it must.

**#3 (S) — W4's gauge failure is visible, not merely red. APPLIED.**
The unbalanced banner now carries the argument rather than a warning: because `q² = 0`, the
condition `ε·q = 0` fixes `ε` only up to `ε^μ → ε^μ + λq^μ`; each term of the soft factor moves
by exactly `λ` since `(p·ε + λ p·q)/(p·q) = p·ε/(p·q) + λ`; therefore `ΔS = λ e Σ_k η_k Q_k`. A
`λ` slider is beside it and `ΔS/e` is printed live, together with `Σ ηQ`. The source is cited
where it makes the same computation, `soft_Arxiv_update.tex:1138-1142`, including its
conclusion that "global charge conservation guarantees that this soft factor is gauge
invariant". Live with `Σ ηQ = 12` and `λ = 1`, `ΔS/e = 12.00`; balanced, the row says
"(zero for every λ)".

**#1 (M, highest wow) — W4's forward zero and peak ring are the interaction. APPLIED.**
A "paint" control under the sphere switches between the whole event and any one line alone.
In the single-line view the sphere is painted from `spherePattern` of that one leg, its peak
ring `n̂·β̂ = β` is drawn as a dashed great circle labelled "peak ring, cos θ = β", a dotted
marker at its velocity is labelled "exact zero along β", and three readout rows appear: the
exact maximum `Q²β²/(1−β²)`, the ring half-angle `arccos β`, and `P` along the velocity. The
provenance tag becomes "Exact formula — one term of the sum", because one term is not an
observable either. A tangent arrow showing `S` projected on the screen is drawn at the probe in
every mode, so transversality is visible rather than asserted. Live for the `β = 0.88` leg: the
searched maximum `3.432624` equals the exact `Q²β²γ² = 3.432624` to seven figures, the ring
reads `28.36°` (`arccos 0.88 = 28.357°`), and `P` along the velocity prints `8.04e−31` labelled
as exactly zero at the rounding floor of rebuilding `n̂` from its angles.

**#4 and #5 — NOT DONE.** Both are M-effort and neither is a correctness item: #4 (a cumulative
integral trace in W6) and #5 (an angular patch ledger in W7). They were left for a later round
in favour of finishing every FATAL and BUG item and the three cheap-or-decisive improvements.
Neither is blocked by anything in this repair.

### 10.4 Harness

The shipped `qa-run.mjs` cannot QA this fragment end to end: its static, Node-physics and
`physicsRun` lanes read `frag-gw.html` unconditionally, and `interactionRun` waits on
`[data-w5-mode="em"]`, a GW station, so `node qa-run.mjs --frag=frag-em.html` runs the browser
*matrix* over the EM fragment and then aborts everything after it. Generalising the runner is
outside this lane's edit scope. An EM driver was therefore written in the lane scratch directory
(`qa-em.mjs`), reusing the same harness page, the same viewport/theme matrix and the same
console/error instrumentation.

`node qa-em.mjs`, Playwright chromium, `qa-harness.html?frag=frag-em.html`:
**PASS = 52, FAIL = 0, WARN = 0, NOT RUN = 0.** Rows, for each of light and dark at 390, 768
and 1300 px: horizontal scroll (`html = body = viewport` at all six), escaping elements (none —
the wide MathJax displays, the verbatim source block and the wide tables all scroll inside their
own `overflow-x:auto` containers), runtime errors (none), `console.error` (none), duplicate ids
(none), globals added (`PROLOGUE` only, the contract's one permitted global), palette token
errors (none), MathJax (loaded). Plus:

* `interaction · every control exercised` — 27 ranges swept to both ends, the midpoint and back;
  4 number inputs through `3, 0, −3` and back; 5 selects through every option; all 11 buttons
  clicked and any left running stopped; then a rotate-drag and two wheel-zooms on the W4 sphere
  and a drag inside the W2 canvas. Zero `pageerror`, zero console errors.
* `interaction · degraded readouts` — after that sweep, **no** readout and no table cell is
  empty, an em dash, `NaN`, `Infinity` or `undefined`.
* `fallback · THREE / WebGL absent` — with `three.js` blocked and `getContext('webgl*')` forced
  to `null`: zero errors, the W4 canvas still painted, `pmax = 12.341422`. The fragment contains
  zero references to `THREE` and loads no library, so it is unaffected either way.

Separately, the states the critic said were reachable and broken were driven directly and
checked (`qa-states.mjs`, same scratch directory): W4 solo, W4 all-charges-zero, W4 unbalanced
and then balanced, W2/W3/W6 with `β_f = β_i`, W6 at `β_i = −0.9, β_f = 0.9, τ = 0.4, θ = 8°`,
and W6 at both ends of the panel slider. Zero errors in all of them; the numbers are quoted in
the ledger above.

`node docs/outreach/auditions/prologue/em-core.test.mjs` → exit 0, all tests pass.

**Screenshots** (33), in `docs/outreach/auditions/prologue/qa/`, all prefixed `em-`:
`em-{light,dark}-{390,768,1300}-w{2,3,4,6,7}.png` (30) plus `em-stress-w2.png`,
`em-stress-w4.png`, `em-stress-w6.png` taken after the interaction sweep. They were looked at,
not merely produced. Two layout defects were found in them and fixed: the three-part
single-line equation in W4 overflowed at 390 px and is now stacked in an `aligned` environment,
and the verbatim source block in W3 was being typeset by MathJax (see FATAL 5). One cosmetic
consequence was also caught by eye: the sequential ramp puts high values in *deep* ink on the
light surface, so the heading's original word "bright" was replaced by "paints a ring".

### 10.5 `qa-run.mjs`

Four changes, all inside this lane's remit; nothing else in the runner was touched.

1. **`ERR_HTTP_HEADERS_SENT` crash** (the reason the critic's browser lane was NOT RUN, together
   with item 2). The static-file `catch` called `response.writeHead` on a response whose headers
   were already on the wire when Chromium aborted a request, throwing out of the handler and
   taking the run down before it printed anything. Now guarded with `!response.headersSent` and
   `!response.writableEnded`.
2. **`instrumentFragment`'s W5 anchor.** It pinned
   `'  window.requestAnimationFrame(tick);\n})();\n</script>\n\n  <section class="stop" id="w8">'`
   — with two leading spaces before `<section>` that `frag-gw.html` has never had, and with a
   call the GW lane's rAF-lifecycle repair replaced by `schedule();`. The needle is now
   `'  schedule();\n})();\n</script>\n\n<section class="stop" id="w8">'` and the replacement text
   matches; verified against the current `frag-gw.html` (both the W5 and the untouched W9 anchor
   match). The comment above them says why.
3. **`physics/Node · W9 upper-pole late-limit verdict`** was `record(..., 'FAIL', ...)`
   unconditionally, with the critic's finding as the detail string. It is now **NOT RUN**, with
   a detail saying why it cannot be a Node test — the verdict wording is DOM state and
   `loadW9Core` extracts only `S` and `f` — and pointing at the browser row that does check it
   and the Node row that checks the underlying closed form.
4. **`physics/Node · W9 A=0 pole label`** was likewise unconditional. It is replaced by a **real
   test**, `physics/Node · W9 A=0 residue and late-time limit`: with `A = 0` and the damped pair
   in the lower half plane it asserts `|f(400)| < 1e−15` (the late-time limit equals the residue,
   which is zero) and `|f(0.4)| > 1e−3` (the pair still rings). It passes.

`node qa-run.mjs` (the GW lane, unchanged fragment) now runs to completion and prints:
**PASS = 69, WARN = 2, FAIL = 4, NOT RUN = 1** — against the GW lane's recorded post-repair
`PASS = 68, FAIL = 6, WARN = 2`, i.e. items 3 and 4 turned one hard-coded FAIL into a PASS and
the other into an honest NOT RUN. The four remaining failures are the GW lane's two recorded
harness disagreements and their Node twins, unchanged by this lane.
`node qa-run.mjs --frag=frag-em.html` gives `PASS = 54, WARN = 1, FAIL = 9, NOT RUN = 1`, and
none of the nine is an EM defect: six are `browser · … globals: PROLOGUE` (the contract's one
permitted global, which the GW fragment does not create), two are the GW lane's own recorded
physics disagreements, and the ninth is `Playwright browser matrix` timing out on
`[data-w5-mode="em"]` — the GW hard-wiring described above. Any screenshots that run leaves
behind under the GW naming scheme were removed and the committed GW screenshots restored;
the only new files this lane adds to `qa/` are the 33 `em-` ones.

### 10.6 Remaining gaps

1. **`qa-run.mjs` is still a GW runner.** Its static audit, its Node physics audit and its
   interaction and physics browser lanes all target `frag-gw.html`; `--frag` reaches only the
   browser matrix. Until it is generalised — a `--frag`-aware `FRAGMENT` path and a station
   list per fragment — the EM lane needs its own driver. The one written for this repair is in
   the lane scratch directory and is not committed; it is about 200 lines and reuses
   `qa-harness.html` unchanged.
2. **`retardedTime`'s absolute tolerance.** As diagnosed under FATAL 11, the core's fixed
   `1e−13` absolute residual is below `ulp(t)` for `t ≳ 10⁴`, so a legal W6 setting loses its
   two largest radii. The page now reports those rows as `NOT COMPUTED`. A relative tolerance in
   the core would recover them; that is a core-lane change, not a page change.
3. **File size is now 242 KB**, up from 196 KB — the repair added the verbatim source block, the
   single-line equation, the gauge panel, the solo view and a good deal of prose. 28 KB of the
   total is still the inlined core, which the integrator may hoist out and load once for the
   whole page; that would bring the fragment to about 214 KB.
4. **Improvements #4 and #5 are not done** (see §10.3), and neither is blocked.
5. **W4's sampled maximum is a search, not a bound.** It is now seeded well and refined, and the
   page says "largest value found" rather than "anywhere", but no rigorous angular bound is
   computed. That is the honest state, and it is stated on the page.
6. **The lecture wording was checked against the repository digests**, as in the original build,
   not against the video audio; the digests identify the quoted material as auto-captions and
   the page says so.

### 10.7 Design decisions the integrator must preserve

The builder's three decisions in §8 all survive the repair and still hold. Four more were made
here and matter to anyone editing the fragment next:

1. **`spherePattern` is the sole texel evaluator in W4, and must stay so.** The station-local
   copy of the formula is what made the provenance claim false. If the figure is ever ported to
   a `THREE` texture painter, the seam is still `paintSphere()`, but the loop body must keep
   calling the core once per texel and the label under the sphere must keep saying the texture
   size and the scale factor.
2. **A missing palette token is an integration error, never a colour.** Five `tok` functions and
   W4's colour parser now report and fall back to the host's computed text colour. No colour
   literal may be reintroduced; the static scan for `#rrggbb` outside comments is the gate.
3. **Two names for one vector, deliberately.** W3/W4 call the transverse coefficient `S⃗`, W6
   calls it `N⃗` and W7 calls it `M⃗`, each following the source that station quotes. What is
   *not* negotiable is the sign relation now printed in W3: `S⃗·ε = −S_cl`, with `softAmplitude`
   returning `S_cl` and `dcRadiationField` returning the vector. If the integrator unifies the
   notation, that relation must survive the unification.
4. **Zero states are states, not failures.** Four of them are now reachable and labelled — no
   kick in W2, W3 and W6, and an identically zero pattern in W4. Each prints the exact answer
   (zero) with an explanation, and each suppresses the relative quantity that would otherwise be
   `0/0`. Please do not "fix" them by clamping a floor back in.
