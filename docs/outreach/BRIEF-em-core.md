<!-- LANE BRIEF (codex, tns-lqj): the EM reference physics core for the
     IR-triangle WHY prologue. YOUR LANE (create/edit ONLY):
       docs/outreach/auditions/prologue/em-core.js
       docs/outreach/auditions/prologue/em-core.test.mjs
       docs/outreach/auditions/prologue/em-core-NOTES.md
     No other files. No bd operations. No git operations. Write files
     EARLY and INCREMENTALLY (network outages kill lanes; disk survives). -->

# Brief — EM reference physics core (kicked charge engine)

Context: docs/outreach/BRIEF-why-prologue.md (read fully — sections
"Truth constraint", "Physics substrate / EM engine", stations W2, W3, W4,
W6, W7). An Opus builder will inline your library into an interactive HTML
fragment and render from it. YOU are the ground truth: every number the
page prints comes from your functions, and every identity the page claims
("both routes agree to 12 digits") must be a passing test in your harness.
Ground-truth text for quotes: refs/arxiv-1703.05448/soft_Arxiv_update.tex
(quote by line; the soft photon theorem is at :1075-1082; find the EM
leading-order constraint / conservation-per-angle equation in the EM
chapter yourself and record its line numbers in the NOTES).

Units: Gaussian or Heaviside-Lorentz, c=1 — pick one, state it in the
header, use it everywhere. Conventions section at the top of NOTES.

## What em-core.js must provide (browser-safe, no modules, no deps)

A single IIFE that assigns `EMCore` to `window.PROLOGUE = window.PROLOGUE
|| {}; window.PROLOGUE.em = EMCore` in a browser and `module.exports =
EMCore` under node. ES2017, no imports. Pure functions; no DOM.

1. **Trajectory model.** `makeKick({betaI, betaF, tau, profile})` — a
   charge at the origin at t=0 with velocity betaI (3-vector, |β|<1) for
   t<0 and betaF for t>0, connected by a smooth kick of duration tau with
   a named C^1 profile (default raised-cosine; also 'tanh' and
   'instant' with tau=0 as the closed-form limit). Provide
   `position(t)`, `velocity(t)`, `acceleration(t)` in closed form.
2. **Exact Liénard–Wiechert field.** `fieldAt(kick, x, t)` → {E, B, tRet,
   n, R, velocityPart, radiationPart}: solve the retarded-time equation
   |x − r(t_ret)| = t − t_ret by a bracketed Newton/secant iteration with
   a stated tolerance (1e-13), then evaluate the standard LW decomposition
   (velocity/Coulomb term ∝ 1/R², acceleration/radiation term ∝ 1/R).
   For profile 'instant' give the closed-form piecewise field: boosted
   Coulomb of the OLD motion for |x| > t, of the NEW motion for |x| < t,
   and the shell as a delta-function with a stated transverse coefficient
   (this is the Purcell construction; derive it in the NOTES, including
   the transverse/radial ratio in the shell as a function of angle and
   of the two velocities — the W2 readout).
3. **Field lines (W2).** `fieldLine(kick, t, seedPoint, {step, maxSteps})`
   — RK4 streamline of the exact E-field at fixed t, for the smooth kick;
   AND `purcellLines(betaI, betaF, t, {nLines})` — the exact instantaneous
   construction: outer lines from the extrapolated old position, inner
   lines from the actual position, matched across the shell by flux
   conservation (angle map between old and new line labels — derive it).
   Both must agree in the tau→0 limit; test this.
4. **Frequency domain (W3).** `radiationSpectrum(kick, nhat, omegas)` →
   d²I/dωdΩ from the exact time-domain radiation field along the retarded
   trajectory (Jackson-style formula; state which form you integrate and
   the quadrature rule; the 'instant' case must reduce to the closed form
   |n̂×(n̂×(β_f/(1−n̂·β_f) − β_i/(1−n̂·β_i)))|² × const, ω-independent).
   `softAmplitude(kick, nhat, eps)` → the ω→0 coefficient of the
   amplitude's 1/ω pole, and `softFactorWeinberg(particles, nhat, eps)`
   evaluating Σ_k η_k Q_k β_k·ε/(1−n̂·β_k) for a list of {Q, beta, eta=±1}.
   `photonNumber(kick, nhat, omegaMin, omegaMax)` → ∫dω (dI/dωdΩ)/(ħω)
   with the constant made explicit (choose units so the reader sees a
   pure number times α; state it). NOTES must state the EXACT relation
   between the classical soft coefficient and the quantum soft factor
   (:1075-1082): p·ε/(p·q) = β·ε/(ω(1−n̂·β)) — write the sentence the
   page may print, with no hand-waving about "classical limit".
5. **Celestial sphere (W4).** `spherePattern(particles, nhat)` → the
   polarization-summed |soft factor|² = |n̂×(n̂×Σ_k η_k Q_k β_k/(1−n̂·β_k))|²;
   test that summing over two explicit orthonormal ε equals this.
   Include a helper for charge conservation (Σ η Q = 0) since the pole
   structure is otherwise ill-posed — decide and document whether the
   builder should enforce it or display the violation.
6. **Memory, two routes (W6, W5 soft-photon mode).**
   `memoryKickQuadrature(kick, x, {rule, n})` → Δv of a unit-mass unit-
   charge test particle at x from ∫E dt of the EXACT field over a window
   containing the shell passage (Gauss–Legendre or adaptive Simpson;
   state; convergence check by doubling n). `memoryKickClosedForm(kick,
   x)` → the DC (ω→0) closed form of the radiation-field integral. TEST:
   agreement to 1e-10 relative for random kicks and random x with |x| ≫ tau.
   SUBTLETY you must resolve honestly, not paper over: the velocity
   (Coulomb) part of the field also contributes to ∫E dt over any finite
   window, and it is O(1/r²)×(window) which is comparable to the O(1/r)
   shell term when the window is O(r). State precisely which quantity is
   the "memory" identity (the 1/r radiation-order term, equal to the soft
   pole coefficient), give the Coulomb-drift contribution as a separate
   function `coulombDrift(kick, x, t0, t1)` in closed form (boosted
   Coulomb integrated in time), and specify in NOTES exactly what the
   page should print so that the 12-digit identity is TRUE as stated.
7. **Conservation per angle (W7).** `coulombProfile(beta, nhat, r)` — the
   exact boosted-Coulomb radial field at large r and angle n̂ (the
   leading 1/r² coefficient as a function of angle, the F_ru^{(2)}
   analogue). `angularLedger(kick, nhat)` → {before, after, difference,
   dcRadiationTerm} where dcRadiationTerm is the term the EM constraint
   equation at null infinity says balances the difference. Locate the
   constraint equation in soft_Arxiv_update.tex (EM chapter; grep
   "constraint" and F_{ru}), quote its line numbers, and state the
   precise per-angle identity (the difference of the Coulombic profile
   at a given angle equals the SPHERE-DIVERGENCE of the DC radiation
   field there, not the DC field itself — check this against the TeX
   and against your numerics: implement the sphere divergence in
   spherical coordinates and verify the balance to tolerance for random
   kicks). If the identity involves the charge flux term for a massive
   charge (which never reaches null infinity), say so and give the
   correct form for this setup.
8. **Antipodal geometry (W7 interlude).** `penroseCoords(t, r)` → the
   conformal-compactification map (state the map, e.g. tan-based on
   u=t−r, v=t+r) and `freeParticleEndpoints(x0, v)` → the celestial-
   sphere directions at t→−∞ and t→+∞ of a straight line (they are
   antipodal; test it). One sentence in NOTES on how this relates to the
   antipodal matching condition WITHOUT claiming more than the geometry.

## Tests (em-core.test.mjs; `node em-core.test.mjs` must exit 0)

Plain node asserts, no framework. Each identity above is a named test
with a stated tolerance; print the achieved residuals. Include
convergence tables (n vs residual) for every quadrature. Random seeds
fixed. Also test the retarded-time solver against the closed-form
retarded time for uniform motion.

## NOTES (em-core-NOTES.md)

Conventions; every formula implemented with its derivation or its TeX
line reference; the exact sentences the builder may print for (a) the
classical↔quantum soft-factor relation, (b) the two-route memory
identity, (c) the per-angle conservation law, (d) the antipodal
geometry; the list of things that are NOT true and the page must not
say (e.g. "the DC field is the whole time-integral of E"); and the
achieved residuals table copied from the test run. Report at the end:
what you verified, what you could not, and any place where the brief's
physics description (BRIEF-why-prologue.md) is wrong or imprecise —
say so plainly.
