# Novelty Sweep — Final Report
## SYK / JT companion paper (candidate claims C1–C5)
**Sweep window:** all published work through **2026-08-31**
**Corpus:** 10 blind lanes (first pass) + 1 targeted gap round (citation-graph crawls, full-text greps, named-concept searches). **88 deduped records**, ~118 raw hits.
**Method:** abstract-level keyword sweep across arXiv/INSPIRE/Semantic Scholar in the first pass; forward-citation crawling, citer-set intersection, arXiv full-text search, and direct full-text reads in the gap round.

> **L3 gate warning up front.** Nothing in this report has yet been checked against local TeX in `refs/arxiv-<id>/`. Several ids carry *known* author/title/content conflicts across lanes (see §7). **No id below may be cited in the Letter until it has been fetched, title-verified, and any mismatch recorded in `refs/LEDGER.md`.**

---

## 1. Executive summary — final verdicts

| Claim | Final verdict | Decided by |
|---|---|---|
| **C1** — Shenker–Stanford frame shift as memory in JT/SYK; adjudicated **not** memory | **PARTIAL-OVERLAP** | 2305.14411, 1809.07266 (framing move); **2603.18509** (transient/late-time-recovery result, numerically) |
| **C2** — DC identity: permanent relative boundary-time shift = ω→0 limit of Schwarzian soft-mode response | **NOVEL (conditional)** | No hit states it; **the decisive check was never run** — GJW/MSY/Maldacena–Qi/LMTV full texts |
| **C3** — operational asymptotic symmetry of JT/SYK is finite (SL(2)/Casimir only) | **PARTIAL-OVERLAP (heavily anticipated qualitatively)** | 1708.08471, 2005.08999, 2108.04841, 2603.18154 — four independent prior formulations |
| **C4** — two-register memory taxonomy (absolute-response vs calibrated relational) | **NOVEL** | Named-concept sweep empty; FGHN forward-citation crawl (~80 citers) found no thermal/holographic application |
| **C5** — no prior full IR triangle for AdS2/JT/SYK/any 0+1d system | **NOVEL** (evidence materially strengthened; still a negative claim) | Citer-set intersections and cross-community citation signatures all came back empty |

### C1 — PARTIAL-OVERLAP

**What is already claimed.** The framing move "shockwave time-shift = gravitational memory" is *established prior art in two independent forms*:
- **2305.14411** (He–Raclariu–Zurek) proves 't Hooft shockwave commutators *are* the soft/Goldstone commutator on the memory phase space, via an explicit diffeomorphism.
- **1809.07266** (Donnay–Giribet–Gonzalez–Puhm) does the horizon-local version: a transient shockwave crossing a horizon *is* a supertranslation between early and late good cuts.

And the gap round found that the *empirical* half of the adjudication has a partial precedent: **2603.18509** (Joshi–Mishra, 2026) drives a two-sided SYK wormhole with a GW-like Floquet strain and reports, verbatim, *"the late-time recovery: F(t_R) under the GW drive returns to the unperturbed baseline for t_R ≫ t\*. This rules out permanent channel disruption and establishes the GW effect as a transient distortion of the scrambling dynamics."* That is a published, numerically supported "it is transient, not permanent" statement about a driven two-sided SYK time delay.

**Required framing.** The Letter must **not** claim first-ness for "shockwave = memory," and must **not** claim first-ness for "the two-sided SYK time delay is transient." It may claim:
1. the **AdS2/JT/SYK instantiation** of the memory question, posed inside the Strominger triangle vocabulary (2603.18509 never uses memory / soft-theorem / asymptotic-symmetry language; its object is a *drive-induced scrambling delay*, not the Shenker–Stanford shock frame shift);
2. the **adjudication itself as a memory-theoretic verdict** — that the two-sided correlator response decays exponentially and therefore fails the memory criterion;
3. the **positive residue**: that a *calibrated relative-clock ratio* nonetheless plateaus. No hit in the corpus computes or names this.

Cite 2305.14411 and 1809.07266 **in the first paragraph that makes the memory claim**, and cite 2603.18509 at the point of the numerical adjudication, or the Letter overclaims on both counts.

### C2 — NOVEL, conditional on an unrun check

No paper in the corpus states the identity. But the novelty is **instantiation, not structure**: "memory = zero-frequency limit of the soft factor" is the textbook flat-space content of the triangle (rederived with detectors in 2604.19866; done as memory two-point functions from a supertranslation Ward identity in 2512.02825). C2's honest content is *the nAdS2/Schwarzian realization of a known Fourier pairing, proved at tree level in 1/C*.

**The live risk is unchanged and unresolved.** The traversable-wormhole lineage (**1608.05687** GJW, **1704.05333** MSY, **1804.00491** Maldacena–Qi, technical home **1804.09834** LMTV, pulse ancestor **1707.02325**) computes a permanent relative boundary-time shift from a compact negative-energy pulse *in exactly this theory*, from traversability rather than a DC/soft-mode pairing. **BRIEF 2 was never executed.** The gap round ran the C5 citation crawl, the C3 full-text reads, the C1 switchback/2603.18509 reads and the C4 named-concept sweep — it did **not** grep MSY/GJW/Maldacena–Qi/LMTV for `zero frequency`, `zero mode`, `DC`, `Kubo`, `susceptibility`, `static response`, `ω→0`. **A single sentence in MSY or a follow-up identifying the shift with an ω→0 limit turns C2 from a theorem into a repackaging.** This is now the single highest-value remaining action item in the whole sweep.

**Required framing (assuming the check comes back clean).** State C2 as the *nAdS2 realization* of the memory↔soft-theorem Fourier pairing, cite 2604.19866/2512.02825 as the flat-space statement of the structure, and cite GJW/MSY/Maldacena–Qi explicitly as the prior computations of the same shift by a different route — then claim the identity, not the shift.

### C3 — PARTIAL-OVERLAP (most endangered claim)

The **qualitative content** of C3 — infinite naive reparametrization symmetry, finite surviving observable algebra — is established prior art in **four independent formulations**, and the gap round's full-text reads confirmed and sharpened each:

- **1708.08471** (Grumiller–McNees–Salzer–Valcárcel–Vassilevich, 2017): *"on-shell some of these algebras reduce to finite-dimensional ones, reminiscent of the on-shell breaking of conformal invariance in SYK … {Q[σ1],Q[σ2]}=0 … a single generator (essentially the mass) on-shell, due to the on-shell conservation of the Casimir."* This is C3's headline, in a 2017 abstract, with the Casimir mechanism named.
- **2005.08999** (Godet–Marteau, 2020): charges are generically **non-integrable**; only after restricting the phase space do they become true conserved generators, and the survivor is exactly SL(2,R)×U(1).
- **2108.04841** (Harlow–Wu, 2021): Peierls-bracket computation; the only nonzero, integrable charges acting on matter are an SL(2,R) family, built **relationally** (geodesics anchored to the boundary).
- **2603.18154** (Maxfield, 2026): generalizes the on-shell-finiteness phenomenon across the *entire* Virasoro coadjoint-orbit menagerie, identifying the finite set of conserved orbit invariants.

**The apparent contradiction dissolves.** 2409.15415 (Banerjee–Kibe–Molina–Mukhopadhyay) was read in full: its ideal-observer construction performs **state/trajectory estimation of the mode f(u)** from weak measurements, and the paper *itself* notes f(u) is different from the conserved charge H_f unless Sch(f,u)=0. It therefore does **not** contradict "no operational charge for non-Möbius modes." This must be stated explicitly in the paper, or a referee will raise it.

**Universality bound.** C3 cannot be phrased as "SL(2,R) always." Enlarging the gauge/matter content enlarges the surviving finite algebra: **2503.13680** (W₃ → sl(3,R) via the dilaton), **2506.02629** (affine osp(1|2)_k → OSp(1|2) stabilizer), **2410.10768** (so(2,2), genuine Virasoro–Kac–Moody edge-mode charges), **2204.09685** (PSL(N,R) higher-spin JT: N−1 genuinely conserved higher-spin charges). The correct phrasing is *"a finite subalgebra set by the isometry content"*, with plain JT/SYK giving SL(2,R).

**What survives as novel:** (i) a sharp **obstruction theorem** valid at all N, rather than an on-shell reduction, an integrability restriction, or a by-construction coset quotient; (ii) the **operational/measurement-protocol framing** — none of the four prior formulations discusses a physical boundary detector protocol; (iii) the **finite-N numerically measured O(1) Ward defect**, for which no prior art and no contradiction was found. Nearest methodological neighbours only: 2002.05725 (large-scale ED of SYK to N=60, but testing Lyapunov/OTOC, not Ward defects) and 2102.06647 (Milekhin, finite-N corrections to the reparametrization action, analytic).

**Required framing.** Restate C3 as **a sharpened, quantified version of a known structural fact**, with the theorem's strength (all N, obstruction not reduction) and the numerics as the actual contribution. Cite all four prior formulations in the same sentence that states the structural fact. Do not present "only SL(2) survives" as a discovery.

### C4 — NOVEL

No hit names or proposes the dichotomy. The gap round ran the named-concept sweep directly: *"relational memory"* and *"calibrated memory"* return only CS/ML memory-network papers; *"decoherence" + "memory effect" + "reference frame"* returns **0 results**; *"memory susceptibility"* returns one unrelated transport-geometry paper (2608.09607). arXiv abstract search for *"memory effect" AND "SYK"* returns **0**; *"memory effect" AND "JT gravity"* returns **1** (2604.26600, entanglement revivals in evaporating-BH JT/RST — a different, CFT-entanglement sense of "memory"). Forward-citation crawls of **1901.00021** (51 citers) and **2109.03832** (~30 citers) found **no** application of the persistent-observable framework to thermal, holographic, SYK, or quantum-mechanical systems; all citers stay in binary-merger GW astrophysics, BMS/Carrollian/celestial holography, or classical-GR soft hair.

Nothing found says *"thermal reference frames erode their own memory records."*

**Required framing.** C4's value is **comparative**, so the paper must survive a direct comparison with the Flanagan–Grant–Harte–Nichols persistent-observable programme (1901.00021, 1912.13449, 2109.03832) rather than merely cite it — a referee will ask why the two registers are not a special case of persistent observables. Also position against: **2601.23019** (*"gravitational wave detectors are intrinsically insensitive to the final offset and can only probe the associated transition"* — the closest published statement to C4's calibration register, in the very system where C4 asserts the registers coincide); **2608.09295** (observable inspiral memory depends on detector low-frequency cutoff and calibration); **2406.07106 / 2402.02594** (displacement-vs-velocity memory, a two-register distinction *of a different kind*); **2312.10454** (memory as a quantum-noise floor); **2308.02445** (finite-T soft theorems — thermal *corrections* to soft factors, explicitly **not** erosion of the record).

### C5 — NOVEL (evidence upgraded from "no counterexample surfaced" to "citation-graph clean")

The gap round executed the kill-shot brief. Results:

- **Citer-set intersection of 2411.13633 (Soft gravitons in 3d) ∩ 2112.14609 (Flat JT / BMS-Schwarzian)** — exactly where a 2d/JT triangle paper would sit — contains precisely **two** papers: **2603.12902** (Ecker, *Carroll symmetries in field theory and gravity*: 2d Carroll dilaton gravity, Carroll–Hawking effect; no soft theorem, no memory, no triangle) and **2412.05038** (Simon–Yu, *BMS3 fermionic localization*: pure BMS3 partition-function paper). Neither is a counterexample.
- **Cross-community citation signature** (cites Strominger 1703.05448 **and** Penington–Witten 2301.07257): exactly **one** paper, **2407.11132** (Ciambelli–Freidel–Leigh, *Quantum Null Geometry and Gravity*), which cites both only as general background and has no AdS2/JT triangle content.
- **Cites 1703.05448 and 1804.00491:** two papers, **2011.13870** (Limits of JT gravity) and **2405.18465** (Magnetic Braneworlds). Neither relevant.
- **arXiv full-text** search for *"infrared triangle"* paired with AdS2 surfaced one hit, **2603.21941** (Varrin PhD thesis, corner symmetry) — read directly, **false positive**.
- Forward citations of 2310.16683, 2512.15796 (single citer: 2602.20037, Curtright dual-graviton BMS) and 2301.07257 (40 citers) contain no triangle-in-JT/SYK paper.

**Required framing.** The **transplant methodology is crowded and active** and the Letter must say so: 1709.05018 (soft pion triangle, 2017), 2310.16683 (fracton triangle — explicitly *"the first realization of an infrared triangle beyond Lorentz symmetry"*), 2512.15796 (acoustic triangle, Dec 2025), 2412.16142/2412.16149 (classical super-rotation / super-phaserotation triangles), 2411.13633 (3d triangle with no propagating gravitons and "Schwarzian-like" boundary dof). **The move is not novel; only the target is.** Phrase C5 as "the first assembly for a 0+1d / nearly-AdS2 system," never as "the first triangle beyond X" — 2310.16683 owns that phrasing and 2512.15796 is three months inside the window.

**Watch item:** **2602.14079** (Özer–Filiz, *Holonomies and Boundary Symmetries in Discrete BF Formulation of JT Gravity*, v1 Feb 2026, v2 retitled Aug 2026) derives JT asymptotic symmetry algebras **directly at the lattice level**. It is not a triangle and has no soft-theorem/memory content, but it is contemporaneous with this campaign and is the closest thing in the literature to "lattice + asymptotic symmetry." Re-check at submission.

---

## 2. PRIORITY — papers that overlap C1 / C2 / C5

### C1 overlaps

| id | title / authors | exact overlap |
|---|---|---|
| **2305.14411** | *From Shockwaves to the Gravitational Memory Effect* — He, Raclariu, Zurek (2023) | **Executes C1's framing move in 4D.** *"The shockwave momentum is related to the soft graviton mode, which is responsible for the memory effect, while the shift in the shockwave position is related to the Goldstone mode."* / *"We demonstrate this equivalence via a diffeomorphism that takes a shockwave metric to a metric whose transverse traceless component is the gravitational memory."* Kills any first-ness claim for "shockwave = memory." |
| **1809.07266** | *Black hole memory effect* — Donnay, Giribet, Gonzalez, Puhm (2018) | **Horizon-local version of the same move.** A transient shockwave crossing a black-hole horizon is reinterpreted as a BMS supertranslation relating early and late good cuts. This is the paper C1's *negative* adjudication is implicitly contradicting, in a different dimension. |
| **2603.18509** | *Gravitational Wave-Induced Scrambling Delay in SYK Wormhole Teleportation* — Joshi, Mishra (2026) | **Partially anticipates C1's adjudication, numerically.** Floquet GW-like strain drive on two-sided SYK; Δt_scr^fid = +0.11 J⁻¹, Δt_scr^OTOC = +0.20 J⁻¹, βJ=2, N=10–16. Verbatim: *"the late-time recovery: F(t_R) under the GW drive returns to the unperturbed baseline for t_R ≫ t\*. This rules out permanent channel disruption and establishes the GW effect as a transient distortion of the scrambling dynamics."* Different protocol (drive, not shock), different observable (teleportation fidelity), and **no memory/soft-theorem vocabulary** — but the "transient, not permanent" conclusion is published. |
| **1804.09834** | *Shockwave S-matrix from Schwarzian Quantum Mechanics* — Lam, Mertens, Turiaci, Verlinde (2018) | **The exact technical object C1 re-reads:** semiclassical Schwarzian OTOC reproduces the Dray–'t Hooft shockwave S-matrix; heavy-operator two-point functions reduce to Schwarzian saddles. Uses **no** memory or asymptotic-symmetry language. Flagged by two lanes as read in snippet only — still not read in full. |
| **1406.2678** | *Complexity and Shock Wave Geometries* — Stanford, Susskind (2014) | **C1's central object under another name.** Introduces the switchback effect: the shocked Schwarzian/ERB boundary trajectory compared against the no-shock counterfactual, C/K = t\* − 2 n_sb t₊. **Confirmed by full-text check to be the true origin of "switchback."** Reports the object as complexity growth, never as memory. |
| **2304.15008 / 2406.04397 / 2506.19013** | *The Cosmological Switchback Effect* I & II (Baiguera, Berman) and *Geometry of Chord Intertwiner, Multiple Shocks and Switchback in DSSYK* | The switchback descendants. **Gap round confirmed: none states or plots the late-time behaviour (decay vs plateau) of the shock-induced boundary time shift** — only its growth rate and duration. C1's decay-vs-plateau question is genuinely unasked in this lineage. |
| **2405.17559** | *New horizon symmetries, hydrodynamics, and quantum chaos* — Knysh, Liu, Pinzani-Fokeeva (2024) | **The structural spine of C1 minus the memory vocabulary.** Horizon-shifting diffeomorphisms appear on the boundary as emergent low-energy gauge symmetries, connected to OTOCs and pole-skipping — in general higher-dimensional holography, not AdS2/JT/SYK. |

### C2 overlaps

| id | title / authors | exact overlap |
|---|---|---|
| **1704.05333** | *Diving into Traversable Wormholes* — Maldacena, Stanford, Yang (2017) | **Nearest existing computation to C2's mechanism.** Induced negative null energy produces a permanent relative time shift (advance) between the two boundary clocks, computed directly in the Schwarzian/JT effective theory. Derived from traversability, **never** (as far as the sweep saw) framed as a zero-frequency Fourier pairing with the soft mode. **Full text not read — this is the unrun kill-shot check.** |
| **1608.05687** | *Traversable Wormholes via a Double Trace Deformation* — Gao, Jafferis, Wall (2016) | Same mechanism, the originating construction. Same unrun check. |
| **1804.00491** | *Eternal traversable wormhole* — Maldacena, Qi (2018) | The two-sided coupled-SYK setup underlying both C1 and C2; carries the same permanent-relative-shift physics. Same unrun check. Forward citations were crawled for triangle language (none found) but **not** for ω→0/Kubo/susceptibility language. |
| **1707.02325** | *Pure states in the SYK model and nearly-AdS2 gravity* — Kourkoulou, Maldacena (2017) | **Pulse-protocol ancestor for C2.** Low-energy pure states via projected boundary conditions; state-dependent perturbation δH = g Σ s_k S_k; diagonal correlators thermal, off-diagonal decaying. No soft-theorem or memory framing. |
| **1804.09834** | *Shockwave S-matrix from Schwarzian QM* — LMTV (2018) | Shared with C1. Any statement there about permanence or the ω→0 structure of the response bears directly on C2. |
| **2604.19866** | *Asymptotic charges as detectors and the memory effect in massive QED and perturbative quantum gravity* — Oertel, Moult, Pasterski (2026) | **States the structure C2 instantiates**, in flat space: charge conservation ⟺ memory, rederived in detector/light-ray-operator language with Faddeev–Kulish dressings. Establishes that the *pairing* is textbook, so C2's claim must be the AdS2 instantiation only. |
| **2512.02825** | *Memory Correlators and Ward Identities in the "in-in" Formalism* (2025) | Same role: supertranslation Ward identity for soft-graviton insertions in Schwinger–Keldysh, memory two-point functions related to ANEC correlators. Flat space. |
| **2412.14238** | *Twisted times, the Schwarzian and its deformations in DSSYK* | Flagged by a lane as bearing on Schwarzian response structure; **never fetched, never read.** Open C2 exposure. |

### C5 overlaps

| id | title / authors | exact overlap |
|---|---|---|
| **2411.13633** | *Soft gravitons in three dimensions* — Cotler, Jensen, Prohazka, Riegler, Salzer (2024) | **Highest structural risk to C5.** A *complete* triangle in a theory with **no propagating gravitons** and **"Schwarzian-like" boundary degrees of freedom**: *"there are no propagating gravitons in three dimensions and thus no soft graviton external states [yet] we find … three equivalent features: a soft graviton theorem, an infinite-dimensional BMS asymptotic symmetry, and a gravitational memory effect."* One dimension and one boundary condition from the target, by authors already working flat JT / Carrollian 2d. **Forward citations crawled — no descent to 2d/AdS2 found.** |
| **2310.16683** | *Fracton Infrared Triangle* — Pérez, Prohazka, Seraj (2023; PRL 2024) | **Competing priority phrasing:** *"Together with their asymptotic symmetries this constitutes the first realization of an infrared triangle beyond Lorentz symmetry."* Lattice-motivated, condensed-matter-adjacent. Sets the bar for what counts as a new corner and constrains how C5 may phrase its own first-ness. |
| **2512.15796** | *Sound as a gauge theory and its infrared triangle* — de Aguiar Alves, Landulfo (Dec 2025) | **The other "triangle in a condensed-matter system" claim**, three months before the window closes: *"We show how low-frequency changes in an acoustic source can lead to lasting displacements of fluid particles … This exhibits an example of an infrared triangle in a condensed matter system."* Too recent for citations to accumulate; **must be re-checked at submission time.** |
| **1709.05018** | *Soft pion theorem, asymptotic symmetry and new memory effect* — Hamada, Sugishita (2017) | **Earliest non-gravity triangle transplant.** Soft pion theorem as Ward identity of an asymptotic axial symmetry, with a pion memory effect. Establishes the transplant methodology as seven years old. |
| **2412.16142 / 2412.16149** | *Classical Super-Rotation / Super-Phaserotation Infrared Triangle* — Choi, Laddha, Puhm (2024) | Active 4D triangle-completion programme; demonstrates "assemble the remaining corner" is a recognized publication genre. (One lane recorded the first id as **2312.16142** — resolve.) |
| **2112.14609** | *Flat JT Gravity and the BMS-Schwarzian* (2021/JHEP 2022) | **The only explicit 2d asymptotic-symmetry algebra (BMS2) in the corpus**: Minkowskian JT in Bondi gauge, extension of the warped Virasoro group, BMS-Schwarzian boundary action with a dilatonic zero mode, one-loop-exact partition function. Adjacent to C5's target and used as one of the two citer-crawl anchors. **Authorship conflict across lanes — verify (see §7).** |
| **2602.14079** | *Holonomies and Boundary Symmetries in Discrete BF Formulation of JT Gravity* — Özer, Filiz (2026) | **Contemporaneous watch item.** *"We develop a fully discrete and non-perturbative realization of two-dimensional Jackiw-Teitelboim (JT) gravity as an sl(2,R) BF theory … derive the corresponding asymptotic symmetry algebras directly at the lattice level, including an affine Kac-Moody symmetry."* Lattice + JT asymptotic symmetry, classical/algebraic, **no soft theorem, no memory, no triangle** — but nearest neighbour to the campaign's lattice angle and revised Aug 2026. |
| **2603.12902 / 2412.05038** | *Carroll symmetries in field theory and gravity* (Ecker) / *BMS3 fermionic localization* (Simon, Yu) | The **entire** citer-set intersection of 2411.13633 ∩ 2112.14609 — i.e. the precise locus where a scoop would live. Both read: neither has soft-theorem, memory, or AdS2/JT/SYK triangle content. **This is the positive evidence supporting C5.** |
| **2407.11132** | *Quantum Null Geometry and Gravity* — Ciambelli, Freidel, Leigh (2024) | The **only** paper citing both Strominger's IR lectures and Penington–Witten JT algebras. Read: cites both as general background only. Second piece of positive C5 evidence. |
| **2504.12521** | BMS lecture notes (2025) | Contemporary pedagogical statement of the triangle; needed for the definitional baseline. **Id and authorship unverified.** |

### Addendum — C3 overlaps (included because C3 is the most endangered claim)

| id | title / authors | exact overlap |
|---|---|---|
| **1708.08471** | *Menagerie of AdS2 boundary conditions* — Grumiller, McNees, Salzer, Valcárcel, Vassilevich (2017) | *"on-shell some of these algebras reduce to finite-dimensional ones, reminiscent of the on-shell breaking of conformal invariance in SYK … {Q[σ1],Q[σ2]}=0 … a single generator (essentially the mass) on-shell, due to the on-shell conservation of the Casimir."* |
| **2005.08999** | *New boundary conditions for AdS2* — Godet, Marteau (2020) | *"whose breaking to SL(2,R) × U(1) controls the near-AdS2 dynamics … if we find a proper restriction of the phase space on which Ξ_ξ vanishes, the associated symmetries will be true [integrable] symmetries."* The integrability half of C3. |
| **2108.04841** | *Algebra of diffeomorphism-invariant observables in JT Gravity* — Harlow, Wu (2021) | *"the existence of a family of SL(2,R) algebras acting on the matter fields … rather than saying we study an observable at some fixed coordinate location, we instead define its location relative to some other features of the state."* Nonzero integrable charges classically; silent on measurement protocol and finite N. |
| **2603.18154** | *A menagerie of Schwarzians: coadjoint orbits of Virasoro and near-dS2 quantum gravity* — Maxfield (2026) | *"classical solutions […] can never belong to these orbits if ∫1/u≠0 […] the constraint ∫1/u=0 [is required for] enhanced symmetry."* Generalizes the on-shell finiteness phenomenon across the whole orbit classification; supersedes 1708.08471 as ground truth for the classical-algebra half. |
| **2409.15415** | *Generalized conformal quantum mechanics as an ideal observer in two-dimensional gravity* — Banerjee, Kibe, Molina, Mukhopadhyay (2024; PRD 111 066011) | **Tension, resolved on full-text read.** *"we demonstrate that the time-reparametrization mode can be inferred from the weak measurements of suitable observables of the quantized GCM theory without affecting the gravitational sector in the large N limit."* This is **state estimation of f(u)**, not measurement of a conserved non-Möbius Noether charge — the paper itself notes f(u) differs from the conserved charge H_f unless Sch(f,u)=0. Does **not** refute C3, but the Letter must say why. |
| **2503.13680 / 2506.02629 / 2410.10768 / 2204.09685** | sl(3,R) JT (Özer–Filiz) / N=1 osp(1|2) JT supergravity (Özer–Filiz) / so(2,2) Virasoro–Kac–Moody JT (Chirco–Vacchiano–Vitale) / higher-spin JT matrix model (Kruthoff) | **Universality bound.** Enlarged models carry genuine charges beyond SL(2,R) — but always a *finite* surviving algebra: *"the dilaton restricts the full W(3)-symmetry to sl(3,R)"*; *"a controlled dynamical reduction of the full affine osp(1|2)_k symmetry to its OSp(1|2) stabilizer subalgebra."* C3 must be phrased as "a finite subalgebra set by the isometry content." |

---

## 3. Per-claim annotated bibliographies (deduped, verdict-labeled)

Verdict key: **OVERLAP** = contests part of the claim · **ADJACENT** = neighbouring result the paper must differentiate · **BACKGROUND** = cite for context, no priority risk · **TENSION-RESOLVED** = looked contradictory, isn't · **WATCH** = contemporaneous, recheck at submission.

### C1 — shockwave frame shift as (non-)memory

- **2305.14411** — He, Raclariu, Zurek, *From Shockwaves to the Gravitational Memory Effect* (2023). **OVERLAP.** Shockwave commutators = soft/Goldstone commutators via explicit diffeo. 4D flat.
- **1809.07266** — Donnay, Giribet, Gonzalez, Puhm, *Black hole memory effect* (2018). **OVERLAP.** Horizon shockwave = supertranslation between good cuts.
- **2603.18509** — Joshi, Mishra, *GW-Induced Scrambling Delay in SYK Wormhole Teleportation* (2026). **OVERLAP (partial).** Measured transient delay with explicit late-time recovery; no memory vocabulary.
- **1804.09834** — Lam, Mertens, Turiaci, Verlinde, *Shockwave S-matrix from Schwarzian QM* (2018). **ADJACENT.** The technical home of shockwaves inside Schwarzian mechanics; no memory/asymptotic-symmetry language at all.
- **1406.2678** — Stanford, Susskind, *Complexity and Shock Wave Geometries* (2014). **ADJACENT.** Switchback seed (verified).
- **2304.15008** — *The Cosmological Switchback Effect* (2023). **ADJACENT.** No late-time decay/plateau statement (confirmed).
- **2406.04397** — Baiguera, Berman, *The Cosmological Switchback Effect II* (2024). **ADJACENT.** Same.
- **2506.19013** — *Geometry of Chord Intertwiner, Multiple Shocks and Switchback in DSSYK* (2025). **ADJACENT.** Same; growth machinery only.
- **2405.17559** — Knysh, Liu, Pinzani-Fokeeva, *New horizon symmetries, hydrodynamics, and quantum chaos* (2024). **ADJACENT.** Horizon-shifting diffeos → emergent boundary gauge symmetry → OTOC/pole-skipping.
- **1306.0622** — Shenker, Stanford, *Black holes and the butterfly effect*. **BACKGROUND.** The object C1 reinterprets; ground truth for the frame shift.
- **1611.10214** — *Spontaneously Broken Asymptotic Symmetries and an Effective Action for Horizon Dynamics* (2016). **BACKGROUND.** Horizon reparametrization pseudo-Goldstone action; 4D, no JT/SYK, no memory statement.
- **2103.00824** — Kundu, Patra, Poojary, *Reparametrization mode Ward Identities and chaos in higher-pt correlators in CFT2* (2021). **BACKGROUND.** Reparametrization-mode Ward identities used for OTOC growth; bulk side matches linearized shockwave backreaction.
- **1909.05847** — *Reparametrization modes, shadow operators, and quantum chaos in higher-dimensional CFTs* (2019). **BACKGROUND.**
- **1801.00010 / 1809.01169 / 1808.02898** — Blake–Lee–Liu chaos EFT; Blake–Davison–Grozdanov–Liu pole-skipping; EFT for chaotic CFTs. **BACKGROUND.** Shift-symmetric Goldstone-like structure for chaos without soft-theorem language.
- **2503.18124** — *On the Topological Nature of the Butterfly Effect* (2025). **BACKGROUND.** Chaos as broken time-translation with Goldstone-theorem CFT structure.
- **2604.12784** — *Quantum chaos and the holographic principle* lecture notes (2026). **BACKGROUND.** Useful negative evidence: a comprehensive 2026 review of SYK/JT chaos containing **no** soft-theorem or memory-effect language.
- **2604.10090 / 2506.15373** — sparse-SYK NISQ wormhole teleportation; β-regime two-qubit teleportation benchmarks. **BACKGROUND.** Experimental two-sided SYK context.

### C2 — DC / zero-frequency identity in nAdS2

- **1704.05333** — Maldacena, Stanford, Yang, *Diving into Traversable Wormholes*. **ADJACENT / unresolved scoop risk.**
- **1608.05687** — Gao, Jafferis, Wall, *Traversable Wormholes via a Double Trace Deformation*. **ADJACENT / unresolved scoop risk.**
- **1804.00491** — Maldacena, Qi, *Eternal traversable wormhole*. **ADJACENT / unresolved scoop risk.**
- **1707.02325** — Kourkoulou, Maldacena, *Pure states in SYK and nearly-AdS2*. **ADJACENT.** Pulse-protocol ancestor.
- **1804.09834** — LMTV. **ADJACENT.** Shared with C1.
- **2412.14238** — *Twisted times, the Schwarzian and its deformations in DSSYK*. **ADJACENT / never fetched.**
- **2604.19866** — Oertel, Moult, Pasterski (2026). **BACKGROUND (structural).** Memory ⟺ asymptotic charge in detector language.
- **2512.02825** — *Memory Correlators and Ward Identities in the in-in Formalism* (2025). **BACKGROUND (structural).**
- **1711.08467** — *The soft mode in SYK and its gravity dual* (2017). **BACKGROUND.** Foundational: Schwarzian as the Goldstone of broken reparametrization symmetry. **Authorship conflict across lanes — verify.**
- **2412.14799** — Bucca, Mezei, *Nonlinear soft mode action for the large-p SYK model* (2024/25). **BACKGROUND.** Exact nonlinear soft-mode action; no memory/asymptotic framing.
- **2310.19885** — Daguerre, *Boundary correlators and the Schwarzian mode* (2023). **BACKGROUND (methodological).** Schwarzian-dressed retarded two-point function; late-time power-law decay with a branch cut — a useful methodological neighbour for "what decays vs plateaus." **Content description conflicts across lanes — verify.**
- **1706.07803 / 1811.06006** — SYK quench dynamics (Eberlein–Kasper–Sachdev–Steinberg; Bhattacharya et al.). **BACKGROUND.** Establish thermalization/relaxation baselines for a pulsed protocol.
- **2606.27308** — *Universal Lichnerowicz Lifting of Near-Horizon Soft Modes* (2026). **BACKGROUND.** Bulk tensor zero modes = boundary reparametrizations; confirmed on read to be spectral matching only, **not** a triangle.

### C3 — finite operational asymptotic symmetry

- **1708.08471** — Grumiller, McNees, Salzer, Valcárcel, Vassilevich (2017). **OVERLAP (qualitative content).**
- **2005.08999** — Godet, Marteau (2020). **OVERLAP (integrability half).**
- **2108.04841** — Harlow, Wu (2021). **OVERLAP (SL(2,R)-only integrable charges, relationally constructed).**
- **2603.18154** — Maxfield (2026). **OVERLAP / supersedes 1708.08471 as classical ground truth.**
- **2409.15415** — Banerjee, Kibe, Molina, Mukhopadhyay (2024). **TENSION-RESOLVED.** State estimation of f(u), not charge measurement.
- **2503.13680** — Özer, Filiz, sl(3,R) JT (2025). **ADJACENT / bound.**
- **2506.02629** — Özer, Filiz, N=1 JT supergravity beyond the Schwarzian regime (2025). **ADJACENT / bound.**
- **2410.10768** — Chirco, Vacchiano, Vitale, so(2,2) JT via Virasoro–Kac–Moody (2024). **ADJACENT / bound.**
- **2204.09685** — Kruthoff, *Higher spin JT gravity and a matrix model dual* (2022). **ADJACENT / bound.** N−1 genuinely conserved higher-spin charges.
- **2602.14079** — Özer, Filiz, discrete BF JT (2026). **WATCH.** Lattice-level asymptotic symmetry algebras; contemporaneous.
- **2402.01847** — Nitti, Piazza, Taskov, *Relativity of the event: examples in JT gravity and linearized GR* (2024). **ADJACENT.** Relational/operational bulk observables via boundary-anchored geodesics, frame-dependent variances, smeared horizon — very close to C3's *spirit*, but not organized around charges or Ward identities.
- **2005.08999 / 2405.03128 / 2504.14003 / 2503.09371 (+2510.10692, 2605.28753)** — the AdS2 boundary-condition zoo: Godet–Marteau; Cárdenas KdV conformal symmetry breaking in nearly AdS2; Galante–Maneerat–Svesko conformal boundaries near extremal black holes; Parvizi–Sheikh-Jabbari–Taghiloo freelance holography. **BACKGROUND.** Establishes that the surviving-symmetry answer is boundary-condition dependent.
- **1709.09871** — *Canonical Charges in Flatland* (2017). **BACKGROUND / conflicting descriptions.** One lane: JT and CGHS charges finite but not conserved absent field-dependent redefinitions. Another: pedagogical 2+1D flat-space lecture notes, not about JT at all. **Must be resolved before citing** (§7).
- **2304.06088** — Joung, Narayan, Yoon, *Gravitational Edge Mode in Asymptotically AdS2* (2023/24). **BACKGROUND.** Schwarzian as JT edge mode in sl(2,R) BF; PSL(2,R) gauging and measure.
- **2507.04091** — Pinzul, Stern, Xu, *Gauging the Schwarzian Action* (2025). **ADJACENT.** Promotes SL(2,R) to a local gauge symmetry.
- **2301.07257 / 2303.04701 / 2412.15549 / 2112.12828 / 2206.10780 / 2403.09021 / 2306.01837** — Penington–Witten *Algebras and States in JT Gravity*; Kolchmeyer; super-JT; Witten crossed product; CLPW de Sitter algebra; DSSYK Type II₁; generalized entropy for subregions. **BACKGROUND.** The von Neumann-algebraic account of "what is an observable in JT" — the natural alternative formalization a referee may compare C3 against.
- **2002.05725** — Kobrin, Yang, Kahanamoku-Meyer, Olund, Moore, Stanford, Yao, *Many-Body Chaos in SYK* (2020). **BACKGROUND.** ED to N=60 benchmarking Schwarzian predictions — the closest methodological precedent for C3's finite-N numerics, but a different observable class.
- **2102.06647** — Milekhin, *Non-local reparametrization action in coupled SYK* (2021). **ADJACENT.** Nearest miss on the "finite-N + reparametrization" search; analytic/semi-analytic, not ED Ward-identity testing. **Worth a full-text read for any Ward-flavoured finite-N estimate.**
- **2207.03351** — *Operational islands and black hole dissipation in JT gravity* (2022). **BACKGROUND.** "Operational" here means entanglement entropy, not charges — a false friend worth noting.
- **2601.07911** — *Unimodular time in JT gravity: a holographic clock* (2026). **ADJACENT.** Relational bulk clock via Henneaux–Teitelboim; boundary dynamics = Schwarzian + U(1) free particle. Relevant to C1/C3's relational-clock language.

### C4 — two-register memory taxonomy

- **1901.00021** — Flanagan, Grant, Harte, Nichols, *Persistent gravitational wave observables: general framework* (2019). **ADJACENT / must be beaten, not merely cited.** 51 citers crawled: none thermal/holographic/quantum.
- **1912.13449** — same authors, *Nonlinear plane wave spacetimes* (2020). **ADJACENT.**
- **2109.03832** — Grant, Nichols, *Curve deviation in asymptotically flat spacetimes* (2022). **ADJACENT.** ~30 citers crawled: none in the C4 sense.
- **2601.23019** — Zosso, Magaña Zertuche, Gasparotto, Cogez, Inchauspé, Jacobs, *Toward claiming a detection of gravitational memory* (2026). **ADJACENT — closest published statement to C4's calibration register.** *"gravitational wave detectors are intrinsically insensitive to the final offset and can only probe the associated transition."*
- **2608.09295** — *Detector Dependence of Inspiral Christodoulou GW Memory in Binary Black Hole Systems* (2026). **ADJACENT.** Observable memory depends on detector low-frequency cutoff, mass ratio, total mass.
- **2406.07106 / 2402.02594** — displacement vs velocity memory from a gravitational plane wave. **ADJACENT.** An existing two-register classification of a *different* kind; C4 must differentiate explicitly.
- **2010.03119** — *A Gravitational non-Radiative Memory Effect* (2020). **ADJACENT.** Memory without radiation; velocity-type, falls off too fast to observe.
- **2312.10454** — Guo, Wang, *GW memory and quantum Michelson interferometer* (2023). **ADJACENT.** Memory as a quantum-noise floor — the measurement-cost intuition, from the opposite direction.
- **2308.02445** — Solanki, Bhattacharjee, *Soft Theorems and Memory Effects at Finite Temperatures* (2023). **ADJACENT.** *Thermal corrections* to soft factors (spin-dependence, universality lost at finite T), **not** erosion of the record — the paper C4's thermal claim must distinguish itself from.
- **2405.08868** — *A Review of Gravitational Memory and BMS Frame Fixing in Numerical Relativity* (2024). **BACKGROUND.** Frame/gauge dependence of memory observables.
- **1906.09361** — *Memory Effect in Anti-de Sitter Spacetime* (2019). **BACKGROUND.** Higher-dimensional AdS, Fermi normal coordinates; reduces locally to the flat formula. Not AdS2, no dilaton, no Schwarzian.
- **1912.12806** — *Black Hole Memory* (2019). **ADJACENT.** Horizon memory tensor that provably does **not** reduce to CFP asymptotic charges: *"the memory tensor does not relate to CFP symmetries and their charges/fluxes in the manner seen at null infinity"* — a published memory-vs-charge structural tension, useful precedent for C1/C4's negative results.
- **2203.08983** — *Gravitational Memory Effect for Near-Horizon Asymptotic Symmetries* (2022). **BACKGROUND.**
- **2603.12670** — Hou, Zhu, *Shaving off soft hairs and the black hole image memory effect* (2026). **BACKGROUND.**
- **2406.15604** — *Can the Near-Horizon Black Hole Memory be detected through Binary Inspirals?* (2024). **BACKGROUND.**
- **2607.18675** — *Gravitational Memory Beyond Null Infinity through Finite-Distance Carrollian Screens* (2026). **BACKGROUND.**
- **2606.15552 / 2502.03007** — Casimir wormholes with gravitational memory; displacement and B-memory in Ellis–Bronnikov wormholes. **BACKGROUND.** Classical 4D wormhole memory; unrelated to JT/SYK despite the keyword collision.
- **2604.26600** — entanglement revivals in evaporating-BH JT/RST models. **BACKGROUND / false friend.** The *only* arXiv abstract hit for "memory effect" + "JT gravity", and it uses a different (CFT-entanglement) sense of memory.
- **2608.09607** — Kassmi, unrelated "memory susceptibility metric" for transport-history holonomy. **NOT RELEVANT.** Recorded only so the name collision is on the record.

### C5 — first full triangle in 0+1d

- **2411.13633** — Cotler, Jensen, Prohazka, Riegler, Salzer (2024). **ADJACENT / highest structural risk.**
- **2310.16683** — Pérez, Prohazka, Seraj (2023; PRL 2024). **ADJACENT / competing priority phrasing.**
- **2512.15796** — de Aguiar Alves, Landulfo (2025). **ADJACENT / recheck at submission.**
- **1709.05018** — Hamada, Sugishita (2017). **ADJACENT.**
- **2412.16142 / 2412.16149** — Choi, Laddha, Puhm (2024). **BACKGROUND.**
- **2504.12521** — BMS lecture notes (2025). **BACKGROUND.**
- **2512.21239** — scalar-QED superphaserotation triangle. **BACKGROUND.**
- **2112.14609** — Flat JT and the BMS-Schwarzian. **ADJACENT.** The only explicit 2d asymptotic-symmetry algebra found.
- **2011.15053 / 2011.13870** — non-relativistic and Carrollian limits of JT; *Limits of JT gravity* (Grumiller, Hartong, Prohazka, Salzer). **BACKGROUND.** Technical ancestors of any Carrollian/flat JT triangle.
- **2603.12902** — Ecker, *Carroll symmetries in field theory and gravity* (2025/26). **ADJACENT / negative evidence.** Citer-intersection member; 2d Carroll dilaton gravity, Carroll–Hawking effect; no triangle.
- **2412.05038** — Simon, Yu, *BMS3 fermionic localization* (2024). **BACKGROUND / negative evidence.** Other citer-intersection member.
- **2407.11132** — Ciambelli, Freidel, Leigh (2024). **BACKGROUND / negative evidence.** Only Strominger ∩ Penington–Witten citer.
- **2603.21941** — Varrin, *At the Corner of Quantum and Gravity* (2026). **NOT RELEVANT.** Full-text-search false positive; corner symmetry, no triangle content.
- **2405.18465** — Antonini, Bariuan, *Magnetic Braneworlds* (2024). **NOT RELEVANT.** Strominger ∩ Maldacena–Qi citer; braneworld cosmology.
- **2602.20037** — Curtright, dual-graviton BMS extensions. **NOT RELEVANT.** Sole forward citer of 2512.15796; no AdS2/JT/SYK.
- **2602.14079** — Özer, Filiz (2026). **WATCH.** Lattice JT boundary symmetries.
- **2310.10078 / 2301.11363** — Chojnacki et al., GW analogues in spin nematics and cold atoms; Cheung, Derda, Helset, Parra-Martinez, *Soft Phonon Theorems*. **BACKGROUND.** Condensed-matter analogue-gravity and soft-theorem context for the transplant genre.
- **1611.09783** — *Soft hairy horizons in three spacetime dimensions* (2016). **BACKGROUND.** Soft-hair programme seed; 2024–26 citation trail crawled (19 papers), dominated by Carrollian/AdS3 follow-ups, no JT/SYK triangle.
- **2504.10577** — *Soft Theorems and Spontaneous Symmetry Breaking* (2025). **BACKGROUND.** Soft theorems as Ward identities of broken asymptotic symmetries; Goldstone modes as celestial discrete-series reps.
- **2512.24833** — Cárdenas, *Classical integrability in 2D and asymptotic symmetries* (2025). **BACKGROUND.** The only 2024–26 citer of "Canonical Charges in Flatland."

---

## 4. Background citations the paper will need regardless

**The triangle itself**
- 1703.05448 — Strominger, *Lectures on the Infrared Structure of Gravity and Gauge Theory* (definitional ground truth for every corner and edge statement).
- 2604.19866 — Oertel, Moult, Pasterski (detector formulation of charge ⟺ memory).
- 2512.02825 — memory correlators from a supertranslation Ward identity in in-in.
- 2504.10577 — soft theorems as Ward identities of broken asymptotic symmetries.

**Triangle transplants (the genre)**
- 1709.05018 (pions) · 2310.16683 (fractons) · 2512.15796 (sound) · 2411.13633 (3d gravity) · 2412.16142, 2412.16149 (super-rotation/phaserotation) · 2504.12521 (BMS lectures).

**Memory taxonomy**
- 1901.00021, 1912.13449, 2109.03832 (FGHN persistent observables) · 2406.07106, 2402.02594 (displacement vs velocity) · 2601.23019 (detection/calibration) · 2608.09295 (detector dependence) · 2010.03119 (non-radiative memory) · 2405.08868 (BMS frame fixing) · 2312.10454 (memory as quantum noise) · 2308.02445 (finite-T soft theorems).

**Horizon / shockwave memory**
- 1809.07266 · 1912.12806 · 2203.08983 · 2305.14411 · 2603.12670 · 2607.18675.

**SYK / JT / Schwarzian foundations**
- 1306.0622 (Shenker–Stanford) · 1711.08467 (soft mode in SYK) · 1707.02325 (pure states) · 1804.09834 (shockwave S-matrix from Schwarzian) · 2412.14799 (nonlinear large-p soft mode) · 1706.07803, 1811.06006 (quenches) · 2002.05725 (finite-N ED chaos benchmark) · 2604.12784 (2026 chaos/holography lectures).

**Two-sided / traversable wormhole**
- 1608.05687 · 1704.05333 · 1804.00491 · 2601.07911 (holographic clock) · 1807.04276 (entanglement holonomies) · 2310.05912 (crossed-product interiors) · 2603.18509 (GW-driven scrambling delay).

**AdS2 boundary conditions and charges**
- 1708.08471 · 2005.08999 · 1709.09871 · 2603.18154 · 2405.03128 · 2504.14003 · 2503.09371 · 2304.06088 · 2507.04091 · 2112.14609 · 2011.13870.

**Observables / algebras in JT**
- 2108.04841 · 2301.07257 · 2303.04701 · 2112.12828 · 2206.10780 · 2403.09021 · 2402.01847 · 2409.15415 · 2310.19885.

**Chaos EFT and reparametrization Ward identities**
- 1801.00010 · 1809.01169 · 1808.02898 · 2103.00824 · 1909.05847 · 2405.17559 · 2102.06647.

**Switchback / complexity lineage**
- 1406.2678 · 2304.15008 · 2406.04397 · 2506.19013. *(Note: 1503.01409 is Maldacena–Shenker–Stanford, "A bound on chaos" — a real paper, but not the switchback seed. 1408.6560 is not a switchback paper at all; see §7.)*

---

## 5. Definitive fetch list (pull locally, title-verify, then draft)

**Tier 0 — must be read in full before a single sentence is drafted (they can change verdicts)**

| id | expected title | why |
|---|---|---|
| 1704.05333 | Diving into Traversable Wormholes | **C2 kill-shot.** Grep for `zero frequency`, `zero mode`, `DC`, `Kubo`, `susceptibility`, `static response`, `omega -> 0`, `Fourier` near the time-shift computation. |
| 1608.05687 | Traversable Wormholes via a Double Trace Deformation | C2 kill-shot, same grep. |
| 1804.00491 | Eternal traversable wormhole | C2 kill-shot, same grep. |
| 1804.09834 | Shockwave S-matrix from Schwarzian Quantum Mechanics | C1 + C2 technical home; read in full (only snippets so far). |
| 1707.02325 | Pure states in the SYK model and nearly-AdS2 gravity | C2 pulse-protocol ancestor; same grep. |
| 2412.14238 | Twisted times, the Schwarzian and its deformations in DSSYK | Never fetched; open C2 exposure. |
| 2411.13633 | Soft gravitons in three dimensions | C5's structural nearest neighbour; the differentiation paragraph is written from this. |
| 2305.14411 | From Shockwaves to the Gravitational Memory Effect | C1's framing precedent; must be quoted and differentiated. |
| 2603.18509 | Gravitational Wave-Induced Scrambling Delay in SYK Wormhole Teleportation | C1's numerical precedent; **id/authors reached the sweep via search summaries — verify before quoting.** |

**Tier 1 — required for C3's framing and the C1/C5 differentiation paragraphs**

1306.0622 · 1703.05448 · 1809.07266 · 1708.08471 · 2005.08999 · 2108.04841 · 2603.18154 · 2409.15415 · 2310.19885 · 1709.09871 · 2310.16683 · 2512.15796 · 1709.05018 · 2112.14609 · 1711.08467 · 1406.2678.

**Tier 2 — bounds, watch items, and comparison targets**

2410.10768 · 2503.13680 · 2506.02629 · 2204.09685 · 2602.14079 · 2402.01847 · 2102.06647 · 2002.05725 · 1901.00021 · 2109.03832 · 1912.13449 · 2601.23019 · 2608.09295 · 2406.07106 · 2308.02445 · 2604.19866 · 2512.02825 · 2405.17559 · 2304.15008 · 2406.04397 · 2506.19013 · 2412.16142 · 2412.16149 · 2504.12521 · 1912.12806.

---

## 6. Honest residual-coverage caveats

1. **C2's decisive check was never run.** BRIEF 2 — full-text grep of GJW / MSY / Maldacena–Qi / LMTV / Kourkoulou–Maldacena for `zero frequency` / `Kubo` / `susceptibility` / `ω→0` near the time-shift computation, plus a 2020–2026 citer sweep with the same terms — remains outstanding. C2's NOVEL verdict is **conditional on that check**, and the report says so rather than pretending otherwise. This is the single largest open exposure in the sweep.

2. **C5 is a negative claim and cannot be proved.** The gap round upgraded the evidence from "no counterexample surfaced under abstract keyword search" to "citer-set intersections, cross-community citation signatures, and arXiv full-text phrase searches all came back empty." That is materially stronger, but it is still absence of evidence. Specifically: citation graphs were crawled via Semantic Scholar and INSPIRE, whose coverage of 2026 preprints is incomplete and whose citer lists for recent papers are known-partial (the 2109.03832 crawl was flagged as "~30 citers, likely partial"). Nothing published in the final weeks before 2026-08-31 will have accumulated citations at all.

3. **The 2026 tail is the weakest part of the sweep.** Every 2026 id in this report — 2601.07911, 2601.23019, 2602.14079, 2602.20037, 2603.12670, 2603.12902, 2603.18154, 2603.18509, 2603.21941, 2604.10090, 2604.12784, 2604.14387, 2604.19866, 2604.26600, 2606.15552, 2606.27308, 2607.18675, 2608.09295, 2608.09607 — reached this synthesis through search-engine summaries. Most have unconfirmed author lists. Several were read at abstract level only.

4. **Full-text search was applied unevenly.** arXiv full-text (as opposed to abstract) search was run only for the C5 phrase queries. The claims most likely to be scooped in a *discussion section or footnote* — C2's ω→0 remark, C4's thermal-erosion intuition — were searched at abstract level, where such a remark is invisible by construction.

5. **The WebSearch budget was exhausted in every first-pass lane.** The first pass ran to its limit rather than to saturation, so the raw-hit list reflects a budget boundary, not exhaustive coverage.

6. **Non-arXiv and non-English literature was not swept at all.** Journal-only publications, conference proceedings not mirrored to arXiv, theses outside arXiv, and Russian/Chinese/Japanese-language work are entirely uncovered. Two of the closest neighbours found (2603.12902 Ecker, 2603.21941 Varrin) were PhD theses, which suggests thesis literature is a live channel for exactly this kind of cross-disciplinary construction.

7. **C3's finite-N numerics could not be ruled out either way.** No lane located prior art *or* a contradiction for a numerically measured O(1) Ward defect at finite N. A numerics-heavy paper will undersell an asymptotic-symmetry framing in its abstract, so abstract-level search is structurally blind to it. The suggested cond-mat / quant-ph cross-list search with `Ward identity` + SYK + `finite N` / `exact diagonalization` was not completed.

8. **Contemporaneity risk on 2602.14079.** Özer–Filiz's discrete lattice BF JT paper was revised (retitled, appendices added) in **August 2026** — inside the campaign's own working window. It is not a triangle today. It should be re-fetched immediately before submission.

---

## 7. L3 ledger items — conflicts to resolve before any citation

These must be checked against local TeX and recorded in `refs/LEDGER.md`.

| id | conflict | action |
|---|---|---|
| **1408.6560** | **Confirmed mismatch.** This id is Adams, Roberts, Saremi, *Hawking-Page transition in holographic massive gravity* — **not** a switchback paper. An earlier brief attributed switchback content to it in error. | Record the mismatch. Use **1406.2678** (Stanford–Susskind, *Complexity and Shock Wave Geometries*), confirmed by full-text check as the true origin of "switchback." |
| **1503.01409** | Correctly identified as Maldacena–Shenker–Stanford, *A bound on chaos* — a real paper, but **not** a switchback seed, contra an earlier lane's lineage note. | Record; do not cite as switchback. |
| **1709.09871** | **Author and content conflict.** One lane: "Afshar, Grumiller, Merbis — JT/CGHS charges finite but not conserved." Another: "Riegler, Zwikel — pedagogical lecture notes on 2+1D flat gravity, not about JT at all." These cannot both be right, and the C3 relevance hinges on which. | Fetch and resolve. If it is the lecture notes, drop it from C3's bibliography and demote to methodological background. |
| **2112.14609** | **Author conflict.** "Afshar, Oblak" vs "Grumiller, Hartong, Prohazka, Salzer." (The latter matches **2011.13870**, *Limits of JT gravity*.) | Fetch and resolve; it is a C5 citation-crawl anchor, so the attribution matters. |
| **1711.08467** | **Author conflict.** "Kitaev, Suh" vs "Almheiri, Maldacena et al." | Fetch and resolve. |
| **2310.19885** | **Content conflict.** One lane: observables on the quotient Diff(S¹)/PSL(2,R), non-Möbius content unobservable by construction (a C3 risk). Another: Schwarzian-dressed retarded two-point function with late-time power-law decay and a branch cut (a C1/C4 methodological neighbour). | Fetch and resolve. If only the second description is right, 2310.19885 drops out of C3's overlap list and C3's prior-art count falls from four formulations to three. |
| **2412.16142** | Recorded once as **2312.16142**. | Verify which id carries *The Classical Super-Rotation Infrared Triangle*. |
| **2603.18509, 2601.23019, 2603.18154, 2409.15415, 2602.14079, 2607.18675, 2604.19866, 2603.12670, 2608.09295, 2606.27308, 2604.26600** | Authors and/or titles unconfirmed; reached the sweep via search summaries. | Verify each id against its fetched title on arrival; record every mismatch. |
| **2504.12521, 2512.21239, 2602.20037** | Ids and authorship unverified. | Verify before citing. |
| **"test" record** | A junk entry (`id: test`, `title: test`) appears in the gap-round hit list. | Ignore; noted so the deduped count is not misread. |
---

## Appendix (orchestrator, 2026-08-31): exact citer-set intersections via INSPIRE

TJO asked for the intersection of the citers of Strominger's IR-triangle
lectures with the citers of "the SYK paper." Computed exactly from the
INSPIRE citation graph (recids 1517745 / 1452588 / 1467447):

- Strominger lectures (1703.05448): 1169 citers. Maldacena–Stanford SYK
  (1604.07818): 2152 citers. MSY nearly-AdS2 (1606.01857): 1266 citers.
- **∩ with Maldacena–Stanford SYK: 13 papers.**
- **∩ with MSY nearly-AdS2: 21 papers.** Union of both lists ≈ 30
  (four papers appear in both: 1907.01422, 2003.12252, 2201.05054,
  2407.03866).

Reading of the lists: NO member assembles an IR triangle for SYK/JT.
Categories: (a) celestial/Carrollian holography using SYK-side tools —
2201.05054 Pasterski–Verlinde "Mapping SYK to the sky" is the standout,
and it runs the OPPOSITE direction (2D SYK generalization as a toy model
of the 4D celestial soft sector; no 0+1d triangle) — must-cite,
non-overlapping; (b) 3d/flat reductions touching JT — 2211.13415 (JT from
3d flat holographic reduction), 2411.13633 (soft gravitons in 3d, already
on the fetch list); (c) soft-mode effective actions in 4d modeled on the
Schwarzian — 2008.03321 (superrotation effective action), again the
reverse direction; (d) horizon-symmetry work — 2112.13853, 2608.26725,
2312.08353; (e) unrelated (Krylov complexity, energy correlators, etc.).

Quantitative C5 support: out of ~1200–2200 citers each, only ~30 papers
even cite both programs, and none of them poses the triangle question for
SYK/JT itself. The union list doubles as the highest-risk prior-art set
and as a must-cite shortlist for the companion's introduction.
