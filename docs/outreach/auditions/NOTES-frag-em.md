# Builder report — frag-em.html (Builder A, EM lane, tns-fse)

Lane brief: `docs/outreach/BRIEF-builder-em.md`.
Design document: `docs/outreach/BRIEF-why-prologue.md`.
Binding contract: `docs/outreach/AUDITION-SPEC.md`.
Deliverable: `docs/outreach/auditions/prologue/frag-em.html` (196 KB).

Stations built: **W2, W3, W4, W6, W7.** Nothing else was created or edited.

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
