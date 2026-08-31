# Novelty sweep: 1D lattice infrared triangle (soft theorem / asymptotic symmetry / memory) in JT/SYK/AdS2

Conducted via web search (arXiv, Google Scholar-adjacent results) and arXiv abstract fetches.
Search budget was exhausted mid-sweep (WebSearch capped by harness); coverage below is
extensive but NOT guaranteed exhaustive — see "recommended local fetch+verification" list
at the end, and treat this as a strong first pass rather than a final clearance.

## PRIORITY summary (read this first)

No single existing paper appears to already assemble and prove the full "1D lattice
infrared triangle" (soft theorem + asymptotic symmetry + memory effect, with the
"NOT memory / transient relational time delay" verdict) for JT/SYK. However, there
are two **PRIORITY** items the team must engage with directly, because they attack
almost exactly the technical content of Claim 3 (operational asymptotic symmetry
algebra is finite):

1. **arXiv:1904.12820, Lin–Maldacena–Zhao, "Symmetries Near the Horizon"** — constructs
   *exact, gauge-invariant* boundary operators in nAdS2/SYK that close on an SL(2)
   algebra "up to non-perturbative corrections," explicitly contrasting these "exact
   generators" (SL(2) only) against "approximate, but simpler" constructions for other
   would-be symmetry generators (e.g. the size operator). This is the closest existing
   statement to "only the SL(2)/Casimir sector survives as an operational observable
   algebra" in the SYK/nAdS2 literature. It does **not** use infrared-triangle,
   soft-theorem, or memory-effect language, and does not draw the connection to
   asymptotic-symmetry Ward identities per se — but a referee who knows this paper will
   ask why Claim 3 is not simply a restatement of it in different language.

2. **arXiv:1708.08471, Grumiller–McNees–Salzer–Valcárcel–Vassilevich, "Menagerie of
   AdS2 boundary conditions"** — explicitly states (quoting the abstract): *"Besides
   the (centerless) 𝔰𝔩(2) current algebra we find for stricter boundary conditions a
   Virasoro algebra, a warped conformal algebra and a 𝔲(1) current algebra... However,
   on-shell some of these algebras reduce to finite-dimensional ones, reminiscent of
   the on-shell breaking of conformal invariance in SYK."* This is a direct, quotable
   precedent for the *mechanism* of Claim 3 — an infinite asymptotic symmetry algebra
   at the level of boundary conditions that collapses to a finite algebra "on-shell."
   The team should read this paper in full before asserting the finite-algebra result
   as novel; at minimum, Claim 3 needs to be reframed relative to this paper's
   "on-shell reduction" language and cite it as the closest prior statement.

No paper was found that:
- frames the Shenker–Stanford shockwave/butterfly time shift as memory effect and
  refutes it (Claim 1) — no hits combining "JT gravity" or "SYK" with "memory effect"
  in this sense at all;
- states a DC/zero-frequency Schwarzian-response identity for a permanent boundary
  time shift (Claim 2);
- assembles the full infrared triangle for AdS2/JT/SYK (Claim 5);
- makes the two-register absolute-vs-calibrated-relational memory distinction with
  thermal erosion (Claim 4).

These four remain, on current evidence, open ground. Claim 3 is the one with real
adjacent/overlapping prior art and needs the most careful differentiation in the paper.

## Claim 1 — Shockwave/butterfly frame shift as (non-)memory effect

Search terms used: "memory effect JT gravity Schwarzian shockwave soft theorem",
"Shenker Stanford butterfly effect shockwave time shift SYK memory", "JT gravity
memory effect", "SYK memory effect".

No paper combines the Shenker–Stanford shockwave/butterfly frame shift with the
Strominger-style "memory effect" framing, and no paper argues (or argues against)
that this shift is "not memory" in the soft-theorem/asymptotic-symmetry sense.

Relevant background (all standard, all BACKGROUND-CITE):
- **arXiv:1306.0622** (implied; not directly fetched but canonical) Shenker–Stanford,
  "Black holes and the butterfly effect," JHEP 03 (2014) 067 — the shockwave/butterfly
  computation itself. Uses holography to study sensitive dependence on initial
  conditions by perturbing a thermofield double state; the blueshift of an early
  infalling quantum creates a shock wave and destroys two-sided correlations.
  Verdict: BACKGROUND-CITE (the phenomenon Claim 1 reinterprets).
- **arXiv:1804.09834**, Lam–Mertens–Turiaci–Verlinde, "Shockwave S-matrix from
  Schwarzian Quantum Mechanics" — shows the semiclassical OTOC computed in Schwarzian
  quantum mechanics exactly matches the Dray–'t Hooft shockwave S-matrix amplitude.
  This is the closest existing paper doing "shockwave physics in Schwarzian/JT
  language," but it never invokes memory-effect or soft-theorem language, and does
  not distinguish a permanent vs. transient time shift. Verdict: ADJACENT — read
  before writing the intro, since it is the natural "prior formalism" citation for
  translating shockwave time delays into Schwarzian quantities.
- Flat-space precedent for the general shockwave↔memory relation (4D, not AdS2):
  **arXiv:2305.14411**, "From Shockwaves to the Gravitational Memory Effect," and
  **arXiv:2105.09337**, "Quantum imprints of gravitational shockwaves" — these show
  in 4D asymptotically flat gravity that 't Hooft shockwave commutators equal
  soft/Goldstone-mode commutators, and relate the time delay in a shockwave to the
  memory effect. Both explicitly frame time-delay and memory as *distinct* phenomena
  at the level of UV vs. IR ("time delay is revealed in the high-energy limit... more
  naturally associated with the ultraviolet" while memory is IR/soft). This is a
  strong methodological precedent and citation for the "shockwave time-shift is not
  automatically memory" logic that underlies Claim 1, just not in AdS2/JT. Verdict:
  ADJACENT / BACKGROUND-CITE — worth citing as the flat-space analogue of exactly
  the distinction Claim 1 wants to make in AdS2.

## Claim 2 — DC/zero-frequency identity: permanent boundary time shift ↔ zero-frequency Schwarzian soft-mode response

Search terms used: "Schwarzian zero frequency response soft mode DC susceptibility",
"relative time shift boundary time shift matter perturbation Schwarzian permanent JT
gravity two-sided", "double holography boundary time memory soft charge Maldacena
Stanford Yang shockwave relative shift derivation".

No paper was found stating a soft-theorem-to-memory Fourier/DC pairing for the
Schwarzian mode. The closest material is entirely about the *classical* relative time
shift δ between the two boundaries of the eternal JT black hole, which is the natural
object the DC identity would act on:

- **arXiv:1606.01857**, Maldacena–Stanford–Yang, "Conformal symmetry and its breaking
  in two dimensional Nearly Anti-de-Sitter space" — foundational nAdS2/JT paper;
  derives the Schwarzian action from spontaneous+explicit breaking of Diff(S¹) to
  SL(2,R), and (per background search results, not confirmed by direct full-text
  fetch) the two-sided JT phase space is parameterized by dilaton horizon value and
  the relative time shift δ between boundaries — exactly the "permanent shift"
  observable of Claim 2. No soft-theorem or memory language used. Verdict:
  BACKGROUND-CITE, load-bearing — this is very likely the natural reference point the
  paper should build the DC identity on top of; needs full-text local read to confirm
  whether δ's response to a matter perturbation is already computed there (if so, the
  novel content of Claim 2 is purely the soft-theorem/Fourier reframing, not the
  computation).
- **arXiv:1804.09834** (see Claim 1) again relevant: it already relates OTOC/shockwave
  physics to Schwarzian quantum mechanics quantitatively, which is adjacent machinery.
- **arXiv:1608.05687**, Gao–Jafferis–Wall, "Traversable Wormholes via a Double Trace
  Deformation" — introduces the negative-null-energy shockwave that produces a time
  *advance* ΔU for geodesics; this is the doubly-coupled-SYK "knob" whose response is
  a natural candidate for the DC/zero-frequency object in Claim 2. Verdict:
  BACKGROUND-CITE.
- **arXiv:1804.00491**, Maldacena–Qi, "Eternal traversable wormhole" — two coupled SYK
  models with the same gravitational dynamics; describes signal transmission as a
  "revival" of a scrambled perturbation. No time-shift response function or
  soft/memory framing found in the abstract. Verdict: BACKGROUND-CITE for the
  two-sided-protocol setup Claim 2/4 would use experimentally.

No finite-temperature or thermal-noise treatment of this specific DC/soft-mode
identity was found (see also Claim 4).

## Claim 3 — Operational asymptotic symmetry algebra of JT/SYK is finite (SL(2)/Casimir only)

This is where the strongest prior art sits. Search terms used: "Penington Witten
Algebras and States in JT gravity", "JT gravity SL(2,R) charges observables
operational finite algebra boundary", "double-scaled SYK symmetry algebra chord soft
mode asymptotic", "finite-dimensional asymptotic symmetry algebra JT gravity OR SYK
operational charges no soft charge", "Afshar Grumiller soft hair dilaton gravity two
dimensions AdS2 boundary charges", "Cadoni Mignemi asymptotic symmetries AdS2
conformal group D=1", "JT gravity boundary conditions affine sl(2 Kac-Moody current
algebra Schwarzian pseudo-Goldstone".

- **arXiv:1904.12820, Lin–Maldacena–Zhao, "Symmetries Near the Horizon."**
  **PRIORITY.** Full abstract: *"We consider a nearly-AdS2 gravity theory on the
  two-sided wormhole geometry. We construct three gauge-invariant operators in NAdS
  which move bulk matter relative to the dynamical boundaries. In a two-sided system,
  these operators satisfy an SL(2) algebra (up to non-perturbative corrections). In a
  semiclassical limit, these generators act like SL(2) transformations of the
  boundary time, or conformal symmetries of the two sided boundary theory... A
  particular large N and low temperature limit of the SYK model has precisely the
  same structure, and this construction of the exact generators also applies. We also
  discuss approximate, but simpler, constructions of the generators in the SYK
  model."* The distinction between "exact generators" (SL(2) only) and "approximate...
  constructions" for everything else is functionally the claim that only the
  SL(2)/Casimir sector is realized as a genuine operator algebra. Verdict:
  **OVERLAPS-CLAIM-3** (partial/methodological overlap — does not use "asymptotic
  symmetry" or "operational" language, does not connect to soft theorems, but the
  mathematical content is close enough that it must be read in full and explicitly
  distinguished from or built upon).

- **arXiv:1708.08471, Grumiller–McNees–Salzer–Valcárcel–Vassilevich, "Menagerie of
  AdS2 boundary conditions."** **PRIORITY.** Quoted above; states that AdS2 boundary
  conditions give asymptotic symmetry algebras ranging from 𝔰𝔩(2) current algebra up
  to Virasoro/warped-conformal/𝔲(1) algebras, but *"on-shell some of these algebras
  reduce to finite-dimensional ones, reminiscent of the on-shell breaking of conformal
  invariance in SYK."* Verdict: **OVERLAPS-CLAIM-3** — this is the closest existing
  quotable statement of "the asymptotic symmetry algebra of AdS2/SYK reduces to a
  finite algebra." Needs full local read: does "on-shell reduces to finite-dimensional"
  match "operational charges only exist for SL(2)/Casimir," or is it a different
  (Fourier-mode-counting) sense of "finite"? This distinction is central to whether
  Claim 3 is novel or a re-derivation.

- **arXiv:2005.08999, Godet–Marteau, "New boundary conditions for AdS2."** Shows the
  opposite regime: an *enhancement* of the asymptotic symmetry group to
  Diff(S¹)⋉C∞(S¹) (twisted warped Virasoro), reproducing the complex SYK model's
  effective action. Useful as the "infinite tower" foil against which Claim 3's
  finiteness claim should be argued (i.e., Claim 3 must specify boundary
  conditions/observable class carefully, since other choices give genuinely infinite
  asymptotic algebras). Verdict: ADJACENT / BACKGROUND-CITE, load-bearing for framing.

- **arXiv:2301.07257, Penington–Witten, "Algebras and States in JT Gravity."**
  Abstract (paraphrased/quoted fragments): pure JT gravity's boundary observable
  algebra is *"commutative, generated by the ADM Hamiltonian"*; with matter it becomes
  *"a highly noncommutative algebra of Type II∞ with a trivial center."* This is
  superficially supportive of "the algebra is small/finite" in vacuum JT, but the
  moment matter is coupled (which the campaign's memory-effect setup requires, since
  a matter pulse is exactly what produces the shift/response) the algebra becomes
  infinite Type II∞, not finite. This is a **tension**, not a clean overlap: Claim 3
  as stated (finite operational algebra, no charges for non-Möbius modes) needs to be
  reconciled with Penington–Witten's result that adding matter blows the algebra up
  to Type II∞. The paper likely needs to state precisely what "operational asymptotic
  symmetry charges" means as a sub-statement inside the larger noncommutative algebra,
  distinct from the full crossed-product algebra of bounded operators. Verdict:
  ADJACENT, must be cited and reconciled — a critic will raise this immediately.

- **arXiv:2307.15725, Lin–Stanford, "A symmetry algebra in double-scaled SYK."**
  The chord-Hilbert-space symmetry algebra "contains a subalgebra that is a
  deformation of the sl2 near-horizon symmetries" with "finite-dimensional unitary
  representations corresponding to matter moving around in a discrete Einstein-Rosen
  bridge." Another data point for "sl(2)-type subalgebra is the operationally
  distinguished piece," in the double-scaled (finite p, finite λ) generalization.
  Verdict: ADJACENT — worth citing as the DSSYK-generalized version of the
  Lin-Maldacena-Zhao statement.

- **arXiv:2108.04841, Harlow–Wu, "Algebra of diffeomorphism-invariant observables in
  Jackiw-Teitelboim Gravity."** Computes "the algebra of a sizable number of
  diffeomorphism-invariant observables" in classical JT+matter via the covariant
  Peierls bracket, and finds "a family of SL(2,ℝ) algebras acting on the matter
  fields." Background precedent for privileging SL(2,R) as the operationally
  constructible charge algebra, at the classical level. Verdict: BACKGROUND-CITE,
  load-bearing.

- **arXiv:hep-th/9902040, Cadoni–Mignemi, "Asymptotic symmetries of AdS2 and
  conformal group in d=1."** Foundational 1999 paper relating AdS2 asymptotic
  symmetries to the 1d conformal group, used for microscopic 2d black hole entropy.
  Verdict: BACKGROUND-CITE (historical origin of "asymptotic symmetries of AdS2" as a
  phrase/subject).

- **arXiv:2503.13680, "On the Explicit Asymptotic Symmetry Breaking of sl(3,R)
  Jackiw–Teitelboim Gravity"** (2025) — extends the asymptotic-symmetry-breaking story
  to higher-spin JT (W3-type), finding the dilaton induces "controlled symmetry
  breaking" down to sl(3,R). Shows this is an active 2025 research line (i.e., not a
  dead topic a referee would consider settled). Verdict: ADJACENT / BACKGROUND-CITE.

- Not confirmed to exist despite searching: no Afshar/Grumiller paper doing "soft
  Heisenberg hair" *specifically for 2d dilaton gravity/AdS2* was found (the
  soft-Heisenberg-hair papers by this group that surfaced are for 3d BTZ/near-horizon
  geometries, e.g. "Soft Heisenberg hair on black holes in three dimensions" and
  "Soft hairy horizons in three spacetime dimensions"). If such a 2d/AdS2-specific
  soft-hair paper exists it was not surfaced by this sweep — worth one more targeted
  search before submission (see recommendations).

## Claim 4 — Absolute-response vs. calibrated-relational memory; thermal erosion

Search terms used: "gravitational memory SYK model soft photon soft graviton
theorem", "Soft Theorems and Memory Effects at Finite Temperatures", "thermal
decoherence quantum clock reference frame erodes memory black hole information",
"traversable wormhole permanent time shift boundary clock relational observable
measurement cost".

No paper was found making the specific two-register distinction (absolute-response
memory vs. calibrated relational memory susceptibility with exponentially growing
measurement cost), nor one arguing that thermal reference frames erode memory
records, in the JT/SYK/AdS2 context.

Adjacent material, all far from the specific claim:
- **arXiv:2308.02445**, Solanki–Bhattacharjee, "Soft Theorems and Memory Effects at
  Finite Temperatures." Abstract (quoted): *"We study the soft theorems for photons
  and gravitons at finite temperatures using the thermofield dynamics approach. The
  soft factors lose universality at finite temperatures... we obtain the thermal
  contribution to the electromagnetic and gravitational memory effects and show that
  they are related to the soft factors consistently."* This is 4D flat-space QED/GR
  thermofield-dynamics, not AdS2/JT/SYK, and does not discuss erosion/decay of memory
  records or a two-register absolute/relational distinction — but it is the only paper
  found that puts "memory effect" and "finite temperature" in the same technical
  frame, so it's the natural methodological citation for "thermal soft theorems have
  been studied before, just not in this system." Verdict: ADJACENT.
- **arXiv:hep-th/0406260**, "Realistic Clocks, Universal Decoherence, and the Black
  Hole Information Paradox" — general argument that finite-precision physical clocks
  induce fundamental decoherence; conceptually adjacent to "thermal/finite-resource
  reference frames erode a stored record" but is about clocks/unitarity generally, not
  about memory-effect observables or JT/SYK. Verdict: BACKGROUND-CITE at most, tenuous.
- Switchback effect / complexity-growth literature (e.g. "C=Anything and the
  switchback effect in Schwarzschild-de Sitter space," arXiv:2403.xxxx region) shows
  early-time perturbations can be "erased" by late-time dynamics in a chaotic system —
  thematically resonant with "erosion" but framed via complexity, not memory
  susceptibility or thermal reference frames. Verdict: ADJACENT, worth a citation as
  a related erasure/scrambling phenomenon to distinguish from.

## Claim 5 — Full infrared triangle assembled for AdS2/JT/SYK/0+1d

Search terms used: "infrared triangle soft theorem asymptotic symmetry memory effect
AdS2 SYK", "infrared triangle quantum mechanics OR 0+1 OR one dimension soft theorem
memory asymptotic symmetry 2025 2026", "Strominger lectures infrared structure
gravity gauge theory review AdS2 SYK low dimensional".

No paper was found assembling the full triangle for AdS2/JT/SYK. Strominger's
canonical lecture notes/book are 4D-only and do not mention AdS2 or SYK:

- **arXiv:1703.05448**, Strominger, "Lectures on the Infrared Structure of Gravity and
  Gauge Theory" — the canonical pedagogical reference for the infrared triangle
  (soft theorems + asymptotic symmetries + memory, in 4D QED/YM/gravity). No AdS2/SYK
  content found. Verdict: BACKGROUND-CITE, essentially mandatory citation for the
  general framework being ported to 1D.
- Recent (2024–2026) "infrared triangle" extensions found are all still 4D flat-space
  generalizations (logarithmic soft theorems / super-rotation and super-phaserotation
  triangles, e.g. arXiv:2412.16142, arXiv:2412.16149), not lower-dimensional or
  holographic. No overlap with Claim 5.
- The two GGI/Les Houches 2025–2026 lecture-note sets found (arXiv:2512.16810 on
  boundary/asymptotic symmetries, and arXiv:2412.09537 on 2d gravity/holography) were
  checked and, based on their abstracts, do not combine the two subjects — the former
  is flat-space BMS-only, the latter is JT path-integral/matrix-model content with no
  soft-theorem or memory-effect language visible in the abstract. Full-text checks
  recommended before final claim of clearance (see below).

## Recommended arXiv IDs for local fetch + verification (`refs/arxiv-<id>/`)

In priority order:

1. **1904.12820** — Lin, Maldacena, Zhao, "Symmetries Near the Horizon." (PRIORITY —
   read in full against Claim 3.)
2. **1708.08471** — Grumiller, McNees, Salzer, Valcárcel, Vassilevich, "Menagerie of
   AdS2 boundary conditions." (PRIORITY — read in full against Claim 3, especially the
   "on-shell reduces to finite-dimensional" passage.)
3. **2301.07257** — Penington, Witten, "Algebras and States in JT Gravity." (reconcile
   Type II∞ result with Claim 3's finiteness statement.)
4. **1606.01857** — Maldacena, Stanford, Yang, "Conformal symmetry and its breaking in
   two dimensional Nearly Anti-de Sitter space." (load-bearing background for Claims
   2 and 3; confirm whether the relative time-shift response to a matter pulse is
   already computed here.)
5. **1804.09834** — Lam, Mertens, Turiaci, Verlinde, "Shockwave S-matrix from
   Schwarzian Quantum Mechanics." (methodology precedent for Claims 1–2.)
6. **2005.08999** — Godet, Marteau, "New boundary conditions for AdS2." (foil for
   Claim 3's finiteness statement; shows the opposite infinite-algebra regime.)
7. **2307.15725** — Lin, Stanford, "A symmetry algebra in double-scaled SYK." (DSSYK
   generalization of item 1, background for Claim 3.)
8. **2108.04841** — Harlow, Wu, "Algebra of diffeomorphism-invariant observables in
   Jackiw-Teitelboim Gravity." (background for Claim 3.)
9. **1608.05687** — Gao, Jafferis, Wall, "Traversable Wormholes via a Double Trace
   Deformation." (background for Claim 2/4 experimental setup.)
10. **1804.00491** — Maldacena, Qi, "Eternal traversable wormhole." (background for
    Claim 2/4 setup.)
11. **2308.02445** — Solanki, Bhattacharjee, "Soft Theorems and Memory Effects at
    Finite Temperatures." (only extant "thermal + memory + soft theorem" paper found;
    cite/distinguish for Claim 4.)
12. **hep-th/9902040** — Cadoni, Mignemi, "Asymptotic symmetries of AdS2 and conformal
    group in d=1." (historical background.)
13. **1703.05448** — Strominger, "Lectures on the Infrared Structure of Gravity and
    Gauge Theory." (mandatory framework citation.)
14. **2210.10846** — Mertens, Turiaci, "Solvable Models of Quantum Black Holes: A
    Review on Jackiw-Teitelboim Gravity," Living Rev. Rel. 26 (2023). (comprehensive
    review; skim for any soft-theorem/memory-effect passages missed by abstract-only
    checks.)

## Caveats / follow-up searches not completed

- WebSearch budget was exhausted before a dedicated check for a 2d-dilaton-gravity
  (AdS2-specific) "soft Heisenberg hair" paper by Afshar/Grumiller could be completed;
  only 3d BTZ-context soft-hair papers by this group were confirmed. Worth one more
  targeted search ("Afshar Grumiller Sheikh-Jabbari soft hair AdS2" / "2d dilaton
  gravity soft hair") before finalizing novelty claims.
- Full-text (not just abstract) checks were not done for items 1–2, 4, 6, 14 above —
  abstract-level reading is enough to flag them as PRIORITY/ADJACENT but not enough
  to write the final "distinguished from prior work" paragraph in the paper.
- No INSPIRE citation-graph check was performed (e.g. "papers citing 1904.12820 AND
  Strominger 1703.05448" as a direct scoop-detector); recommended as a fast final
  check once the paper's actual theorem statements are fixed.
