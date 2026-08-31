<!-- ROLE: citation notes for the SYK/JT companion paper (tns-wvp).
     Produced by the batch-12 summary pass (4 Sonnet lanes, 2026-08-31),
     merged by orchestrator. Every quote carries file:line into refs/.
     LEDGER records the 1408.6560 mismatch; Stanford-Susskind complexity
     paper is 1406.2678 (fetched + title-verified). -->

# Companion-paper citation notes (batch-12 summary pass)



# C1 — shockwave / chaos group

(EXTRACTION FAILED for task aa0d44add9a611a1c — orchestrator must re-merge from notification text)


# C3 — asymptotic symmetries of 2d gravity

(EXTRACTION FAILED for task a9f4bc5d14604c033 — orchestrator must re-merge from notification text)


# C4 — memory classifications and detector registers

(EXTRACTION FAILED for task ab5badca99dd7844a — orchestrator must re-merge from notification text)


# C5 — infrared-triangle landscape

(EXTRACTION FAILED for task aa5d7446808e641cb — orchestrator must re-merge from notification text)


---

## Orchestrator notes on agent flags (2026-08-31)

- The C3 agent flagged 2603.18154 as "date-anomalous"; it is not — the id
  denotes 2026 March, five months before today (2026-08-31). No action.
- The 1408.6560 mismatch (sweep cited the wrong id for Stanford-Susskind)
  is recorded in refs/LEDGER.md; the correct id 1406.2678 is fetched and
  title-verified. arxiv-1408.6560/ must not be cited for complexity content.
- Maxfield framing caveat (finiteness of classifying data, not a literal
  "finite-dimensional orbit invariant" phrase) must be respected at
  drafting time; flagged for the pre-submission critic pass.


# C1 — shockwave / chaos group

# Literature Report — C1 (Shockwave/Chaos Group)

Context used: `claims/CLAIMS.md` rows `JT-bfly-decay` (butterfly frame shift is a transient relational delay, zero plateau, `Δu_rel^NL(T)=−ακ⁻¹e^{−κ(T−u_*)}+…`), `JT-B-susc` (calibrated susceptibility, large-C-first, no permanence claim), `JT-noplat-abs` (absolute two-sided correlator `δG_LR(T)` has no nonzero late plateau even when the calibrated ratio saturates). All five refs read in full (TeX bodies + abstracts + conclusions).

---

## 1. `refs/arxiv-2305.14411/` — He, Raclariu, Zurek

**Verified title/authors:** "From Shockwaves to the Gravitational Memory Effect" — `shockwaveMemoryDraft_arxiv_v2.tex:434`. Authors: Temple He, Ana-Maria Raclariu, Kathryn M. Zurek — `shockwaveMemoryDraft_arxiv_v2.tex:438`. Matches expectation exactly (CALT-TH 2023-013, `:426`).

**Summary (10 sentences):** This is a 4D asymptotically-flat-spacetime paper (no black hole needed) proving an *algebraic* equivalence between 't Hooft's shockwave commutation relations near a horizon and the canonical commutation relations of the soft-graviton/Goldstone modes that parametrize the gravitational memory sector of the BMS phase space. They review the Aichelburg–Sexl/'t Hooft spherical shockwave (§2.1), the time delay `δx⁺ = α(z,z̄)` a probe acquires crossing it (`eq. time-delay`, `:649`), and 't Hooft's promotion of `(P^±, X^±)` to operators obeying `[P^±,X_±]=−iγ^{zz̄}δ²(z−z')` (`:670-675`). They then construct a diffeomorphism (§3) mapping the shockwave metric to a Bondi memory metric with shear `C_{zz}` and soft mode `N(z,z̄)`, matching symplectic forms so that the shockwave momentum `P⁺` is identified with the soft graviton mode `N` and the shockwave-position shift `X⁻` with the Goldstone mode `C`. This lets them re-derive the 't Hooft commutators from the known `[N,C]` commutator (§3.3, `sec:hooft`). The claimed result is that shockwave time delay and gravitational memory are the same phase-space algebra viewed two ways, not that a particular two-sided correlator or relative-clock observable is literally the memory displacement. The paper is purely 4D linearized-gravity/celestial-holography; there is no JT/Schwarzian/SYK content, no discussion of eternal-black-hole two-sided correlators, and no late-time-decay analysis of any observable — memory here is by construction the asymptotic step-function shear `C_{zz}∝Θ(u−u_i)` (`:773`), i.e. a permanent quantity by definition of the BMS vacuum-transition framework, not something whose permanence is being tested.

**Exact quotes to cite/differentiate:**
- Abstract, `:450`: "we show the 't Hooft commutation relations of shockwave operators are equivalent to the commutation relation between soft and Goldstone modes parametrizing a sector of the gravitational phase space… The shockwave momentum in 't Hooft's analysis is related to the soft graviton mode, which is responsible for the memory effect, while the shift in the shockwave position is related to the Goldstone mode."
- `:980`: "we established a relation between the time delay acquired by a particle propagating in a shockwave background and the gravitational memory effect."
- `:987` (Discussion, the sentence closest to a literal "shockwave = memory" framing): "Nevertheless, by treating shockwaves as a gravitational memory effect, we open up additional directions to understand the infrared behavior of shockwave geometries…"
- `:773`: memory mode `N,C` built explicitly as a step function `Θ(v−v_0)` — memory is a *permanent* asymptotic vacuum transition by construction, never asserted to decay.

**Verdict: OVERLAPS (terminology/title risk only) / otherwise ADJACENT.** This is the single most dangerous paper for a reader to conflate with our thesis, because its title and abstract literally equate "shockwave" with "memory effect" — the opposite of our headline claim. The companion paper's introduction must explicitly scope this away: He–Raclariu–Zurek's equivalence is an *algebraic identification of canonically-conjugate phase-space variables* in 4D asymptotically-flat celestial holography at null infinity (no black hole, no correlator dynamics, memory defined as a permanent step), whereas our claim concerns a specific *dynamical, calibrated relative-clock observable* in JT/Schwarzian dynamics that we show is a decaying transient, not a permanent BMS-type charge; the two papers are not in tension because they are statements about different objects in different theories, but the shared vocabulary ("shockwave", "memory effect", "time delay") must be disambiguated in the first paragraph that cites this reference.

---

## 2. `refs/arxiv-1809.07266/` — Donnay, Giribet, González, Puhm

**Verified title/authors:** "Black hole memory effect" — `Memory.tex:130`. Authors: Laura Donnay, Gaston Giribet, Hernán A. González, Andrea Puhm — `Memory.tex:134`. Matches expectation exactly (CPHT-RR021.042018, `:124`).

**Summary:** This is the near-horizon companion to Hawking–Perry–Strominger (HPS): they take the HPS result that a transient linearized gravitational shockwave sourced at advanced time `v_0` (`eq. TvvLO`, `:199`) supertranslates a bald Schwarzschild black hole into a physically distinct, permanently-charged supertranslated geometry (`eq. supertranslatedSchw`, `:241`) carrying nonzero superrotation charge `Q_Y^HPS` (`:253`), and re-derive/extend this from the perspective of a near-horizon (Rindler-like) observer using the Donnay–Giribet–González asymptotic-symmetry algebra of horizons. They find the shockwave induces not only a horizon supertranslation but also a horizon superrotation, compute its charge and show it matches HPS's null-infinity charge (§3), identify the supertranslation zero-mode with the entropy change of the process (`:345`), and extend the whole analysis to charged (Einstein–Maxwell/Reissner–Nordström) black holes (§4–5), finding an extra infinite-dimensional current algebra. Throughout, "memory effect" = a permanent change of asymptotic/horizon charges (a before/after difference between two genuinely inequivalent, static classical geometries), induced by an explicitly transient (`δ(v−v_0)`) shockwave — this is the textbook usage that motivates the whole IR-triangle literature. There is no discussion of decaying correlators, Schwarzian dynamics, SYK, or any observable that could plateau vs. decay; it is purely classical 3+1D GR asymptotic-symmetry bookkeeping.

**Exact quotes to cite/differentiate:**
- Abstract, `:161`: "We compute the memory effect produced at the black hole horizon by a **transient** gravitational shockwave. As shown by Hawking, Perry, and Strominger (HPS) such a gravitational wave produces a deformation of the black hole geometry which from future null infinity is seen as a Bondi-Metzner-Sachs (BMS) supertranslation. This results in a diffeomorphic but physically distinct geometry which differs from the original black hole by their charges at infinity."
- `:176`: canonical statement of the IR triangle ("soft theorems… enhanced symmetry group… memory effect produced by transient gravitational waves").
- `:345`: "The physical interpretation of the zero-mode of [the supertranslation charge] is clear: it encodes the variation of the entropy (times the temperature) due to the transient shockwave" — the clearest example in this corpus of "transient perturbation ⇒ permanent (charge) shift" being called "memory."

**Verdict: BACKGROUND (canonical IR-triangle reference, not competing).** DGGP is the field's standard illustration that a transient shockwave produces a *permanent* change (a genuinely conserved asymptotic charge / entropy shift) — exactly the notion of "memory" our paper is contrasting our JT observable against. Our paper should cite this as the template for what a real memory effect looks like (permanent charge difference between two static end states), to sharpen the claim that the Shenker–Stanford frame shift fails this test because `δG_LR(T)→0` and `Δu_rel^NL(T)→0` exponentially (`JT-bfly-decay`, `JT-noplat-abs`) rather than settling into a new charge sector.

---

## 3. `refs/arxiv-1408.6560/` — TITLE MISMATCH, FLAGGED

**refs/arxiv-1408.6560/ does NOT contain "Complexity and Shock Wave Geometries" (Stanford–Susskind).** The actual TeX (`phase.ARS.tex`) is:

- Title (`phase.ARS.tex:47`): **"Hawking-Page transition in holographic massive gravity"**
- Authors (`phase.ARS.tex:51`): **Allan Adams, Daniel A. Roberts, and Omid Saremi**
- Preprint number (`:42`): MIT-CTP/4578
- Abstract (`:61-65`): "We study the Hawking-Page transition in a holographic model of field theories with momentum dissipation. We find that the deconfinement temperature strictly decreases as momentum dissipation is increased…"

This is a completely different arXiv paper (a massive-gravity/Hawking–Page-transition/momentum-dissipation paper co-authored by Daniel Roberts, who is also a Stanford–Susskind-adjacent author, which may explain the mix-up) with **zero content on shockwave geometries, complexity, or the memory effect**. The auxiliary files in the directory (`allan_macros.tex`, `allan_layout.tex`, `phase-diagram.pdf`) confirm this is the Adams–Roberts–Saremi paper, not Stanford–Susskind 1408.6560.

**Action needed (loud flag, not performed by me per task scope):** `refs/LEDGER.md` needs a mismatch entry for arxiv-1408.6560, and the actual Stanford–Susskind "Complexity and Shock Wave Geometries" TeX must be re-fetched before any claim in the paper cites its content (e.g., the standard `α=e^{κ(t−t_w)}` two-sided shockwave/complexity growth formula that `JT-bfly-decay`'s scope note references via `refs/arxiv-1306.0622 shock.tex:223-234` — note that's a *different* ref id, 1306.0622, which is Shenker–Stanford "Black holes and the butterfly effect," and appears to be the one actually already in use for the geodesic-shift formula; 1408.6560 (Stanford–Susskind, complexity) is a separate, currently-missing reference).

**Verdict: N/A — wrong file, cannot assess overlap.** Do not cite 1408.6560 for any Stanford–Susskind complexity content until the correct TeX is fetched and verified against its title.

---

## 4. `refs/arxiv-2506.19013/` — Aguilar-Gutierrez, Xu

**Verified title/authors:** "Geometry of Chord Intertwiner, Multiple Shocks and Switchback in Double-Scaled SYK" — `draft.tex:183`. Authors: Sergio E. Aguilar-Gutierrez, Jiuci Xu — `draft.tex:184`. Matches expectation.

**Summary:** This is a chord-Hilbert-space (double-scaled SYK, DSSYK) technical paper, not about memory at all. They build an "intertwiner" formalism that isometrically factorizes the one-particle bulk chord Hilbert space, enabling systematic computation of multi-point correlators with arbitrarily many matter insertions (§2). Using this, they build a path-integral description of "wormhole density matrices" (Berkooz et al.) whose classical saddle-point solutions reproduce the Shenker–Stanford two-sided geodesic length / shockwave picture (`:224`, `:1667`), but with `q`-deformation corrections and no triple-scaling limit needed. They find the DSSYK model exhibits *sub-maximal* chaos at finite temperature (Lyapunov exponent set by an effective "fake temperature" `β_fake`, tied to the semiclassical 6j-symbol, `:1671-1740`), consistent with Lin's "fake disk" scramblon picture. They then use the intertwiner formalism to construct multi-shockwave (alternating precursor) configurations and derive precise conditions for the switchback effect (cancellation of complexity growth from alternating early/late shocks) to hold in both geodesic length and Krylov operator complexity (§4). The shockwave-induced time shift they compute (`:1642`, "the effect of the precursor is to create a time shift in the evolution of Krylov operator complexity") is treated as a fixed additive parameter entering the geodesic-length/complexity formula — analogous in spirit to the Shenker-Stanford `α` shift our `JT-bfly-decay` claim analyzes — but the paper never asks whether that shift decays, plateaus, or is "memory"; it is purely a static input to a complexity/OTOC calculation, with no discussion of two-sided correlator late-time behavior, no IR-triangle/soft-theorem language, and no use of the words "memory" or "permanent" anywhere in the file.

**Exact quotes relevant to positioning (no memory-framing language found — confirmed by full-text grep for "memory"/"permanent", zero hits):**
- `:212`: switchback effect defined as "a decrease in complexity due to a cancellation between early and late time backreaction in the bulk, modeled by several shockwave pulses inserted in an alternating order."
- `:224-228`: "we deduce the saddle point solutions… of the DSSYK model with one-particle insertions… these semiclassical solutions have the same evolution as the two-sided geodesic lengths in an effective AdS$_2$ black hole background… Our result is consistent with earlier findings that DSSYK exhibits a submaximal chaos."
- `:1642`: "the effect of the precursor is to create a time shift in the evolution of Krylov operator complexity."

**Verdict: ADJACENT.** Same underlying object (Shenker–Stanford geodesic shockwave shift, extended to DSSYK) but a disjoint question (complexity/switchback/sub-maximal chaos vs. our memory-effect no-go). No competing claim to differentiate against — it neither supports nor contradicts `JT-bfly-decay`/`JT-noplat-abs`. Our paper should cite it only as evidence that the Shenker–Stanford shock parameter is a live, actively-studied object across SYK-family models (motivating why its memory-effect status is worth settling), not as a source needing rebuttal.

---

## 5. `refs/arxiv-2603.18509/` — Joshi, Mishra

**Verified title/authors (previously "unconfirmed"):** "Gravitational Wave-Induced Scrambling Delay in SYK Wormhole teleportation" — `main.tex:73`. **Authors: Sudhanva Joshi and Sunil Kumar Mishra**, Department of Physics, IIT (BHU) Varanasi — `main.tex:74,78`. Title matches the expected framing exactly; author list is now confirmed (2 authors, both IIT-BHU).

**Summary:** This is a numerical (exact-diagonalization, finite-`N` Majorana SYK) study of traversable-wormhole (Gao–Jafferis–Wall / teleportation) protocols perturbed by a Floquet drive engineered to mimic a gravitational-wave metric-strain coupling via the JT holographic dictionary (App. A). They measure teleportation fidelity `F` and an OTOC scrambling diagnostic under this drive at `βJ=2`, `N∈{10,…,16}`. Main findings: (i) fidelity suppression grows with drive amplitude with two regimes split near `ε∼J`; (ii) the channel is a "low-pass filter," most sensitive at `ω≲β⁻¹` with monotone recovery above the thermal scale — explicitly *not* peaked at the MSS chaos scale `2π/β`; (iii) an inspiral chirp drive delays the fidelity peak by `Δt_scr^(fid)=+0.11 J⁻¹`, cross-checked by an independent OTOC-based scrambling delay `Δt_scr^(OTOC)=+0.20 J⁻¹` (same sign, ruling out a pure calibration artifact); (iv) both effects persist (are not suppressed) over the accessible `N` range. Crucially, they emphasize repeatedly and explicitly that the observed delay is **transient**: the fidelity and the OTOC both return to their undriven baseline at late times, and they use this late-time recovery as direct evidence *against* interpreting the effect as any kind of permanent channel/memory disruption — a logical structure ("delay ≠ permanence, demonstrated by late-time recovery to baseline") directly analogous to ours, though applied to a driven Floquet teleportation-fidelity/OTOC observable rather than a static post-shock two-sided correlator computed via a Möbius horizon translation.

**Exact late-time-recovery quotes (as requested):**
- `main.tex:598` (figure caption): "The late-time recovery to the unperturbed baseline establishes the effect as a **transient scrambling delay rather than permanent channel disruption**. The scrambling-delay interpretation is confirmed by the OTOC diagnostic…"
- `main.tex:613`: "A key feature of Fig.~(\ref{fig:chirp}) is the late-time recovery: $\mathcal{F}(t_R)$ under the GW drive returns to the unperturbed baseline for $t_R \gg t^*$. This **rules out permanent channel disruption** and establishes the GW effect as a **transient distortion** of the scrambling dynamics. In holographic language, this is consistent with a transient deformation of the effective traversable channel rather than a permanent loss of transmissivity."
- `main.tex:659-660` (OTOC panel c): "$\Delta C<0$ near $t^*=7.00\,J^{-1}$, returning to zero at late times, **establishing a delay rather than a permanent disruption**."
- `main.tex:767` (Conclusion): "both show late-time recovery to the unperturbed baseline, ruling out permanent channel disruption."

**Verdict: OVERLAPS (structural precedent, different observable/mechanism).** This is the closest thing in the corpus to an independent numerical demonstration of our thesis's *logical shape* — "an apparent delay in a chaos-related SYK observable is transient, not memory, and this is proved by showing late-time recovery to baseline" — but on a completely different observable (driven Floquet teleportation fidelity / OTOC under an external periodic GW-mimicking strain) rather than the static post-single-shock two-sided correlator/relative-clock ratio that `JT-bfly-decay`/`JT-B-susc`/`JT-noplat-abs` analyze analytically in the Schwarzian EFT. The companion paper should cite this as independent, numerically-obtained support for the general principle from a sister (finite-`N`, driven) corner of the SYK universality class, explicitly noting the difference in setup (driven/periodic vs. single static shock; fidelity/OTOC vs. two-sided correlator/frame-shift ratio; finite-`N` exact diagonalization vs. large-`C` Schwarzian EFT) so as not to overstate equivalence between the two results.


# C3 — asymptotic symmetries of 2d gravity

All nine papers have been read in full from local TeX sources (no network access used). Compiled report below.

## 1. Godet–Marteau — "New boundary conditions for AdS2" (arxiv-2005.08999)

**Verified:** Title `\title{New boundary conditions for AdS$_2$}` at `paperJTv2.tex:52`; authors Victor Godet and Charles Marteau, `paperJTv2.tex:96` (byline; `\author{}` field itself is empty on line 53, name/affiliation appear separately). Matches description.

**Summary:** Studies JT gravity in Bondi gauge, finding an enhanced asymptotic symmetry $\mathrm{Diff}(S^1)\ltimes C^\infty(S^1)$ (warped Virasoro) acting on currents $P(\tau),T(\tau)$. Using covariant phase space methods they compute surface charges $k_\xi=\delta\mathcal Q_\xi+\Xi_\xi$ and show the non-integrable piece $\Xi_\xi$ is generically nonzero for arbitrary periodic $P,T$ — so the naive charges are not honest phase-space functions except under a modified (Barnich–Troessaert) bracket. Integrability, and a genuine (possibly centrally extended) representation of the charge algebra, is recovered only on restriction to constant $P_0,T_0$, which simultaneously breaks the symmetry down to $\mathrm{SL}(2,\mathbb R)\times \mathrm U(1)$.

**Key quotes:**
- "Again, one can show that under the modified bracket..., these non-integrable charges belong to a representation the $\mathrm{Diff}(S^1)$ algebra. A consistent condition to have integrability is to impose $s(\tau)=s_0$, a constant held fixed in the solution space." — `paperJTv2.tex:813`
- "Thus, requiring $s$ to be constant realizes the symmetry breaking from $\mathrm{Diff}(S^1)$ to $\mathrm{SL}(2,\mathbb{R})$." — `paperJTv2.tex:831`
- "We have found that using this boundary condition, which leads to integrable charges, the asymptotic symmetry group is bigger than the vacuum symmetry group $\mathrm{SL}(2,\mathbb R)$." — `paperJTv2.tex:672`
- Symmetry-breaking pattern: "$\mathrm{Diff}(S^1)\ltimes C^{\infty}(S^1)\to \mathrm{SL}(2,\mathbb{R})\times \mathrm{U}(1)$." — `paperJTv2.tex:670`
- General integrable/non-integrable framework: "When the charges are integrable, the bracket ... defines a representation (possibly centrally extended) of the asymptotic symmetry group ... When the charges are not integrable ... The non conservation of the charge is sourced by the non integrable part." — `paperJTv2.tex:608–642`

**Verdict: OVERLAPS.** Godet–Marteau give a genuine classical covariant-phase-space calculation showing full Diff(S¹) charges are non-integrable off the SL(2,R)-fixed locus, integrable exactly on it. They stay classical/Noether throughout — no operator-algebraic (vN-algebra/affiliation) statement, and their SL(2,R)×U(1) is the vacuum symmetry of a solution-space point, not an operator algebra on a single boundary's Hilbert space. Our paper sharpens this: integrable-classically becomes affiliated-with-the-physical-vN-algebra, and non-integrable Diff(S¹) charges become unrealized constraint bookkeeping rather than operators at all.

## 2. Harlow–Wu — algebra of diff-invariant observables in JT (arxiv-2108.04841)

**Verified:** Title `\title{Algebra of diffeomorphism-invariant observables in Jackiw-Teitelboim gravity}` at `version2.tex:39`; authors Daniel Harlow and Jie-qiang Wu, `version2.tex:40–41`. Matches description.

**Summary:** Uses the covariant Peierls bracket to build a closed classical "gravitational algebra" of diff-invariant relational observables ($\widetilde L$, $\widetilde\eta_\pm$, $H_\pm$, dressed matter $\psi_{\widetilde\lambda}$). Only diffeomorphisms acting as pure boundary-time translations are declared physical; everything else (the bulk diffeomorphisms that would generate a full reparametrization-charge family) is defined out as gauge redundancy from the start. Inside the physical algebra they isolate a two-parameter $SL(2,\mathbb R)$ family ($P_0,P_\pm$) that acts nontrivially/simply on the dressed matter fields (reproducing LMRS), explicitly noting $H_\pm$ is *not* in this or any $SL(2,\mathbb R)$ subalgebra. They contrast this with the Schwarzian/boundary-particle formalism, which they say carries "unphysical degrees of freedom" their approach avoids. No integrability language is used (confirmed absent by exhaustive grep) — the same conclusion is reached instead via the gauge/physical distinction at the outset.

**Key quotes:**
- "The larger set is the set of diffeomorphisms whose actions on $\Gamma_\pm$ are time-translations of $t_\pm$ ... The smaller set are those for which these time-translations vanish. This latter set must be viewed as gauge redundancies in order for the theory to have sensible dynamics, while the former are physical symmetries which act nontrivially on phase space." — `version2.tex:277`
- "Unlike the ``Schwarzian'' or ``boundary particle'' formalism, our techniques involve no unphysical degrees of freedom..." — `version2.tex:45` (abstract); expanded at `version2.tex:55`.
- "$P_\pm$ also act simply on the two-sided dressed matter fields ... indeed obey the $SL(2,\mathbb{R})$ algebra ... we emphasize that the Hamiltonians $H_\pm$ are not in the $SL(2,\mathbb{R})$ algebra at any time. In fact none of $\widetilde L$, $\widetilde\eta_\pm$, or $H_\pm$ is even in the algebraic union of all the $SL(2,\mathbb{R})$ algebras together..." — `version2.tex:1335–1344`
- "...the construction of traversable wormholes, the existence of a family of $SL(2,\mathbb{R})$ algebras acting on the matter fields, and the calculation of the scrambling time, can be recast as simple consequences of this algebra." — `version2.tex:45`

**Verdict: OVERLAPS — the single most important anchor.** Harlow–Wu prove, by direct classical construction, that generic bulk/boundary reparametrizations are pure gauge and that the only finite family acting nontrivially and simply on matter is the relational SL(2,R) family, excluding $H_\pm$. They do not phrase this in von Neumann algebra language, do not address non-integrability as a mechanism (they gauge-fix the extra diffeomorphisms away rather than showing their charges fail to close/converge), and their SL(2,R) charges are intrinsically two-sided/dressed, not single-boundary. Our paper promotes their classical statement to a precise one-boundary operator-affiliation statement and supplies the non-integrability mechanism (Godet–Marteau-style) explaining why the excluded sector never becomes physical.

## 3. Daguerre — boundary correlators and the Schwarzian mode (arxiv-2310.19885)

**Verified:** Title `\title{\bf Boundary correlators and the Schwarzian mode}` at `Paper_near_extremal_RN.tex:182–183`; sole author Lucas Daguerre, UC Davis, `:175–178`. Matches description.

**Summary:** A computational holography paper (not an observables/algebra paper). Dimensionally reduces a near-extremal RN-AdS throat to JT gravity, treats the boundary reparametrization $\tau(u)$ — identified explicitly as the SL(2,R) zero mode ("the Schwarzian mode") — as a fully quantum-fluctuating field, and imports the exact (all-orders-in-Schwarzian) JT two-point function, continuing it to Lorentzian time via the gravitational Schwinger-Keldysh formalism to get an exact retarded correlator with a late-time power-law tail. It works entirely within existing Stanford–Witten-style coadjoint-orbit technology and never discusses integrability, asymptotic symmetry algebras, or operator affiliation; SL(2,R) enters only implicitly as the source of the Schwarzian zero mode.

**Key quotes:**
- "The emergent AdS$_2$ throat has enhanced $SL(2,\mathbb{R})$ symmetry, and the associated zero modes (henceforth Schwarzian mode) get an action by considering thermal deviations away from extremality... The Schwarzian mode lives at the boundary of the near-horizon region, and its quantum fluctuations become strongly coupled at low temperatures..." — `Paper_near_extremal_RN.tex:209`
- "the exact euclidean 2-point function of boundary operators in JT gravity ... is exact because it accounts for all orders in the Schwarzian mode expansion around the thermal saddle." — `Paper_near_extremal_RN.tex:353`
- "$\tau(u)$ is the boundary mode or Schwarzian mode..." — `Paper_near_extremal_RN.tex:305`

(Note: the terms "reparametrization"/"reparameterization" and "soft mode" do not literally occur anywhere in this file; the paper's own vocabulary is exclusively "Schwarzian mode"/"boundary mode".)

**Verdict: BACKGROUND.** Standard-technology usage of the already-established Schwarzian/SL(2,R) sector as the fluctuating boundary content in a correlator calculation; consistent with but not making our non-integrability/non-affiliation argument. Cite only as evidence that the community already treats SL(2,R)-zero-mode data as the operative physical content of the boundary mode.

## 4. "Canonical Charges in Flatland" (arxiv-1709.09871)

**Verified:** Title `\title{Canonical Charges in Flatland}` at `Modave.tex:69`; authors Max Riegler and Céline Zwikel, `Modave.tex:73`. Matches description.

**Summary:** Pedagogical lecture notes (3D gravity, Chern-Simons and metric formulations, building to BMS₃/flat-space holography and soft hair). Distinguishes generic existence of surface charges (generalized Noether theorem, reducibility parameters) from the further, non-automatic requirement of integrability before any Dirac-bracket charge algebra with central extension even makes sense; stresses that finiteness + integrability + non-trivial asymptotic symmetries together are "usually very difficult" to arrange simultaneously.

**Key quotes:**
- "This algebra of charges is valid only when the charges are integrable. The second term on the right-hand side is recognized as a central extension, which cannot be absorbed in a redefinition of the generators and thus has important physical consequences." — `Modave.tex:841`
- "Usually, well defined boundary conditions require to: contain physically interesting spacetimes, have non-trivial asymptotic symmetries, and lead to finite and integrable charges. It is usually very difficult to find such a set." — `Modave.tex:893`
- "If we assume that the gauge parameter is field independent, then the boundary charge $Q[\lambda]$ is trivially integrable." — `Modave.tex:596`
- "A reducibility parameter is a parameter of a gauge transformation such that its associated gauge transformation vanishes on-shell but not the parameter itself." — `Modave.tex:668`

**Verdict: BACKGROUND.** Generic 3D/BMS₃ methodology with no JT/SYK or vN-algebra content — cite for the general lesson that integrability/finiteness of asymptotic charges is a hard-won, non-automatic condition, not for anything setup-specific.

## 5. "Ideal observer in 2d gravity" (arxiv-2409.15415) — authors now confirmed

**Verified:** Title `\title{Generalized conformal quantum mechanics as an ideal observer in two-dimensional gravity}` at `main.tex:68`; authors Archi Banerjee, Tanay Kibe, Martín Molina, and Ayan Mukhopadhyay, `main.tex:69–72`. (Author list, previously unconfirmed, is now confirmed.)

**Summary:** Couples a probe generalized-conformal-mechanics (GCM) particle to classical JT gravity as an "ideal observer" that can measure the bulk reparametrization mode $f(u)$ without backreacting, in a large-N/double-scaling limit. It distinguishes the exact, on-shell SL(2,R) conserved charges ($H_f,D_f,K_f$, an "instantaneous SL(2,R) frame") from the observer's inferred/estimated reconstruction of $f(u)$ from continuous weak measurements of $\langle x^2(u)\rangle$ and $\langle\mathbb H(u)\rangle$. Full reparametrization symmetry is explicitly stated to be broken to SL(2,R) by JT gravity (and further to U(1) by a solution); the paper self-admits the estimation of the remaining reparametrization content is only approximate due to irreducible quantum measurement uncertainty.

**Key quotes (the estimator-vs-conserved-charge admission is the load-bearing one):**
- "For a general function $f(u)$, we will need continuous weak measurements of $x^2$ and the energy to determine the function $f(u)$. In practice we will be able to attain only an approximation of the function $f(u)$ with continuous weak measurements ... of $\langle x^2(u)\rangle$ and the energy (which are fraught with inherent quantum uncertainties as discussed below)." — `main.tex:805`
- "It is to be noted that the continuous weak measurements ... are fraught with quantum uncertainties." — `main.tex:823`
- "Time-reparametrization symmetry is broken to SL(2,R) in JT gravity. A solution of JT gravity further breaks SL(2,R) to U(1)." — `main.tex:93` (footnote)
- "Since the action is extremized for any $f(u)$ when $x(u)$ is on-shell, we do not expect a new set of SL(2,R) conserved charges to exist which generate transformation of $f(u)$ alone..." — `main.tex:396`

**Verdict: OVERLAPS.** Constructs an explicit observer/detector model where only SL(2,R) is exactly conserved/measurable and the rest of the reparametrization data is merely estimated, never an exact conserved observable. Cite as an anticipating case study; we sharpen it with the algebraic (affiliated-operator, one-boundary vN-algebra) reason no non-Möbius charge is exactly conserved/affiliated, versus their information-theoretic/measurement-uncertainty argument.

## 6. Maxfield — "menagerie of Schwarzians" (arxiv-2603.18154) — date-anomalous id, content verified

**Verified:** Title `\title{A menagerie of Schwarzians: coadjoint orbits of Virasoro and near-dS$_2$ quantum gravity}` at `main.tex:30`; sole author Henry Maxfield, `main.tex:32`. Flag: the arXiv id `2603.18154` is date-anomalous (2026-03, i.e. after the stated "today" of 2026-08-31 falls just months later — self-consistent with a very-near-future id but worth a manual sanity check on the fetch date in `refs/LEDGER.md`). Content is internally consistent and unambiguous as the described paper.

**Summary:** Classifies all generalized Schwarzian theories as integrals over Virasoro coadjoint orbits $\mathcal O(b)$, each with residual stabilizer $G_b$ (U(1), PSL(2,R), or R), in bijection with the moduli of constant-positive-curvature Lorentzian 2D geometries (near-dS₂ JT). Orbits with zeroes of the "coupling" are classified by a finite list of invariants (number of zeroes, derivatives at zeroes up to cyclic permutation, and a principal-value integral $\Delta$), yielding a low-dimensional (often one real parameter, or a discrete label) residual moduli space rather than an infinite-dimensional one.

**Key quotes:**
- "Among such vector fields with fixed $\lambda$, there remains only a one-dimensional space of conjugacy classes of $u$ up to overall normalisation, characterised by the invariant $\Delta$..." — `main.tex:319` (definition follows at `:320–322`)
- "This exhausts the invariants, so a pair of vector fields with $2n$ simple zeroes are related by a smooth change of coordinates if and only if they have the same values of the $2n+1$ invariants." — `main.tex:313` (line approximate)
- "These orbits exhaust all the usual Schwarzian theories ... where the stabilizer $G_b$ is $U(1)$ or $PSL(2,\mathbb R)$..." — `main.tex:306`
- "This theory has a finite-dimensional configuration space matching the diagram in figure~\ref{fig:moduli}..." — `main.tex:171`

**Verdict: ADJACENT.** Caveat noted by the sub-agent for our critic pass (L6): the "finite invariant" quotes describe finiteness of the classifying data/moduli dimension, not a single literal phrase "the orbit invariant is finite-dimensional" — double-check this framing before locking the citation. Classification is on the classical coadjoint-orbit side of near-dS₂ JT, not SYK/AdS₂ affiliated-operator language, but structurally parallels our claim that residual-symmetry-invariant content collapses to finite/low-dimensional data once redundancy is quotiented.

## 7. so(2,2)/Yang-Mills extension of JT (arxiv-2410.10768) — the universality counterexample

**Verified:** Title `\title{A $\mathfrak{so}(2,2)$ extension of JT gravity via the Virasoro-Kac-Moody semidirect product}` at `arxiv2.tex:107`; authors Goffredo Chirco, Lucio Vacchiano, Patrizia Vitale (Università di Napoli Federico II / INFN), `arxiv2.tex:111–113`. Note: an earlier commented-out draft title (line 105) included "Yang-Mills" explicitly; the final title drops it, though the body/conclusions repeatedly call the construction a "JT-Yang-Mills generalization."

**Summary:** Builds JT gravity as an $\mathfrak{so}(2,2)$-valued Poisson Sigma Model from dimensional reduction of $\mathfrak{so}(2,2)$ Chern-Simons/AdS₃-BTZ. Since $\mathfrak{so}(2,2)\cong\mathfrak{sl}(2,\mathbb R)_L\oplus\mathfrak{sl}(2,\mathbb R)_R$, isolating ordinary JT leaves a residual non-abelian Yang-Mills-type sector that also becomes boundary-dynamical. With appropriate boundary conditions the physical boundary symmetry is the infinite-dimensional Virasoro-Kac-Moody semidirect product $\mathrm{diff}(S^1)\ltimes\hat{\mathfrak g}$ — strictly larger than plain SL(2,R)/Virasoro. Without extra boundary conditions, the boundary dynamics is a particle on the full SO(2,2) group with genuinely conserved classical Noether charges for every generator. Entirely classical/topological (BF theory, coadjoint orbits, tree-level entropy) — no operator-algebra/finite-N statement.

**Key quotes (the enlargement result, load-bearing for our universality hedge):**
- "In this work, we propose a bulk plus boundary theory which reproduces a broken $\mathfrak{diff}(S^1)\ltimes \hat{\mathfrak{g}}$ symmetry at the boundary and can be regarded as a gauge extension of the JT gravity model..." — `arxiv2.tex:170`
- "Together with an appropriate choice of boundary conditions, this leads to a boundary dynamics governed by the $\mathfrak{diff}(S^1)\ltimes \hat{\mathfrak{g}}$ symmetry breaking. The boundary Casimir action is then identified with the action associated with coadjoint orbits of the Virasoro-Kac-Moody semidirect product." — `arxiv2.tex:194`
- "the boundary dynamics is that of a particle on the entire SO$(2,2)$ group. The global SO(2,2) symmetry for the boundary theory implies the presence of the conserved charges $J_i = \langle g^{-1}dg, \tau_i \rangle$" — `arxiv2.tex:609`
- "The proposed $\mathfrak{so}(2,2)$-PSM provides a class of possible JT-Yang-Mills generalizations of the JT/SYK correspondence with a purely gravitational interpretation from a 3d perspective." — `arxiv2.tex:647`

**Verdict: OVERLAPS as a bounding counterexample.** This is a precise, named case where, for a genuine JT-like model with an added non-abelian bulk gauge sector (dual to SYK tensor models), the physical/classical boundary symmetry provably exceeds SL(2,R), reaching an infinite-dimensional Virasoro-Kac-Moody algebra. Our "only SL(2,R) survives" wording must therefore be scoped explicitly to plain Schwarzian/JT-type actions (SL(2,R)-BF gravity with no extra gauge sector), not asserted for any 2d dilaton-gravity-like theory; cite this paper as exactly the kind of extension that forces the hedge.

## 8. Afshar–Oblak — "Flat JT Gravity and the BMS-Schwarzian" (arxiv-2112.14609)

**Verified:** Title `\title{Flat JT Gravity and the BMS-Schwarzian}` at `main.tex:146` (note: "Gravity" is in the actual title, differing slightly from the shorthand given); authors Hamid Afshar and Blagoje Oblak, `main.tex:148`. Matches description.

**Summary:** Studies Minkowskian (flat) JT gravity in Bondi gauge at finite temperature/nonzero vacuum energy. The asymptotic symmetry is BMS₂ (an extension of warped Virasoro): $(L_m,Q_m)$ with Witt/Virasoro brackets for $L_m$, semidirect abelian action on $Q_m$, $[Q_m,Q_n]=0$, and three real central charges — genuinely infinite-dimensional, unlike AdS₂/JT's reduction to global SL(2,R). However BMS₂ has a structural pathology: for real, nonzero non-Virasoro central charges the *entire* group is a single coadjoint orbit (trivial stabilizer), unlike Virasoro/warped-Virasoro orbits of positive codimension; consequently the "BMS-Schwarzian" action has no saddle points and only matches the true flat-JT boundary action after adding an extra dynamical dilatonic zero-mode.

**Key quotes:**
- "We show that this extension has a single coadjoint orbit when central charges are real and non-zero. The ensuing BMS-Schwarzian action has no saddle points, and only coincides with the boundary action functional of flat JT gravity up to a crucial dilatonic zero-mode..." — `main.tex:156` (abstract)
- "The goal of this paper is to avoid this reduction to a subgroup and work with BMS$_2$ throughout... it is the BMS$_2$ group, not warped Virasoro, that describes flat JT gravity..." — `main.tex:167`
- "...this ultimately entails shift transformations of the translation current that turn the BMS$_2$ group itself into a single, giant coadjoint orbit, in contrast to orbits of the more standard Virasoro or warped Virasoro groups whose codimension is strictly positive." — `main.tex:169`
- "The BMS$_2$ group has a single coadjoint orbit for all real values of its three real central charges such that $b\neq0$ and $c\neq0$..." — `main.tex:702`

**Verdict: ADJACENT.** A genuine infinite-dimensional enlargement, but for flat (Bondi-gauge) rather than near-AdS₂/SL(2,R)-Schwarzian boundary conditions — a different setup than our theorem's target — and it comes with its own pathology (no saddle points, single giant orbit, ad hoc fix required). Best cited as a companion caution that "beyond SL(2,R)" constructions tend to run into their own consistency issues, reinforcing our claim's spirit for the AdS₂ setting rather than directly falsifying it; weaker as a counterexample than 2410.10768.

## 9. Kitaev–Suh — "The soft mode in the SYK model and its gravity dual" (arxiv-1711.08467)

**Verified:** Title `\title{The soft mode in the Sachdev-Ye-Kitaev model and its gravity dual}` at `soft_mode.tex:310`; authors Alexei Kitaev and S. Josephine Suh, `soft_mode.tex:312–317`. Matches description exactly.

**Summary:** The foundational SYK soft-mode/Schwarzian paper. Frames the near-conformal ($\beta J\gg1$) reparametrization invariance of the Schwinger-Dyson equations as *approximate*, explicitly broken by the UV kinetic term $-\partial_\tau$; the associated pseudo-Goldstone collective coordinate $\varphi(\tau)$ obeys the Schwarzian effective action. Because the Schwarzian derivative is exactly PSL(2,R)-invariant, the space of physically distinct soft configurations is the coset $PSL(2,\mathbb R)\backslash\mathrm{Diff}(S^1)$ — only PSL(2,R)/SL(2,R) is exact/unbroken, the rest of Diff(S¹) is the explicitly-broken pseudo-Goldstone sector, never treated as a conserved charge algebra.

**Key quotes:**
- "This was reported by Kitaev along with other results: an approximate reparametrization symmetry, the existence of a soft (pseudo-Goldstone) mode, and its effective action." — `soft_mode.tex:432`
- "When $\beta J\gg 1$, the derivative term $-\partial_\tau$ in the Schwinger-Dyson equations ... is relatively small. Without this term, the equations are invariant under arbitrary changes of the time coordinate..." — `soft_mode.tex:435`
- "These transformations act on the variable $z=e^{i\varphi(\tau)}$ by linear fractional maps preserving the unit circle... The manifold of distinct $G$'s is $\mathrm{PGL}(2,\mathbb R)\backslash\mathrm{Diff}(S^1) \cong \mathrm{PSL}(2,\mathbb R)\backslash\mathrm{Diff}^{+}(S^1)$." — `soft_mode.tex:463`

**Verdict: BACKGROUND (foundational).** This is the origin of "soft mode = pseudo-Goldstone of an explicitly-broken, only-approximate reparametrization symmetry with PSL(2,R) as the sole exact residual symmetry" — directly supportive of, not merely adjacent to, our restriction claim. Cite as the original statement of the phenomenon our theorem formalizes at the operator/algebra level.

---

### Summary table

| # | Paper | Verdict | One-line positioning |
|---|---|---|---|
| 1 | Godet–Marteau 2005.08999 | OVERLAPS | classical non-integrability ⇒ SL(2,R)×U(1) survivor, no operator algebra |
| 2 | Harlow–Wu 2108.04841 | OVERLAPS (key anchor) | relational SL(2,R) is the only matter-acting charge family, classically |
| 3 | Daguerre 2310.19885 | BACKGROUND | standard use of SL(2,R)/Schwarzian sector in correlators |
| 4 | Riegler–Zwikel 1709.09871 | BACKGROUND | general lesson: integrability/finiteness of charges is hard-won |
| 5 | Banerjee et al. 2409.15415 | OVERLAPS | observer model: estimator of non-Möbius mode ≠ exact conserved charge |
| 6 | Maxfield 2603.18154 | ADJACENT | classical coadjoint-orbit analogue: finite residual invariant data |
| 7 | Chirco–Vacchiano–Vitale 2410.10768 | OVERLAPS (counterexample) | forces "plain Schwarzian/JT" scoping of universality claim |
| 8 | Afshar–Oblak 2112.14609 | ADJACENT | flat-space enlargement, but pathological (no saddle points) |
| 9 | Kitaev–Suh 1711.08467 | BACKGROUND (foundational) | origin of "PSL(2,R) is the sole exact residual symmetry" |

Flags for the L3/critic pass: (a) 2603.18154's arXiv id is date-anomalous relative to today (2026-08-31) — worth a manual sanity check against `refs/LEDGER.md`'s fetch record; (b) the "finite orbit-invariant" quotes for Maxfield describe finiteness of classifying/moduli data rather than a single literal "finite-dimensional orbit invariant" phrase — verify framing before locking the citation; (c) 2410.10768's final title omits "Yang-Mills" (present only in a commented-out draft title and in body prose) — cite the final title as given above.


# C4 — memory classifications and detector registers

# C4 Literature Confirmation Report — Memory Classifications and Detector Registers

Context: checking against D32 (absolute-response memory: fixed observable, `lim_T [ω^pulse(O)−ω^ref(O)]` nonzero) and D33 (calibrated relational memory susceptibility: gauge-invariant ratio/algebraic-combination functional `F_T` with declared measurement cost, equal to a soft-theorem DC datum), plus the structural claim that thermal reference frames erode their own records and that the two registers coincide when the ruler is persistent (GW strain).

---

## 1. arXiv:1901.00021 — Flanagan, Grant, Harte, Nichols, "Persistent gravitational wave observables: general framework"

**Verified**: title at `ms_i.tex:48`; authors at `ms_i.tex:33,36,39,42` (Éanna É. Flanagan, Alexander M. Grant, Abraham I. Harte, David A. Nichols). Matches the assigned citation.

**Summary**: This is the foundational paper defining "persistent gravitational wave observables" — quantities that, like the displacement memory effect, remain nonzero and measurable after a burst of gravitational radiation has passed, whether or not they are tied to an asymptotic symmetry. Table I (`ms_i.tex:139-159`) enumerates the complete class list: displacement memory, relative velocity, relative rotation, relative proper time, subleading displacement (= spin + center-of-mass memory), plus the paper's own three new observables — curve deviation, holonomy (of linear/angular momentum), and a spinning-test-particle observable. Every single one is defined as an absolute difference of a fixed geometric/tensorial quantity between a "before" and "after" flat region (Δξ, ΔΩ, Δτ, Δp, Δs) — there is no ratio, no normalization, no gauge-invariant relational functional anywhere in the paper. Zero temperature, no thermal states, no detector-cost accounting beyond a qualitative "feasibility of measurement" discussion.

**Key quotes**:
- Full observable-class table, `ms_i.tex:139-159` — nine rows, none phrased as a ratio.
- "we will be referring to them simply as persistent observables" (not "memory") when not tied to a symmetry, `ms_i.tex:229-230`.
- Feasibility discussion (`ms_i.tex:630-647`): "All of the persistent observables in this paper are (in principle) measurable... Gravitational wave detectors measure the components of the Riemann tensor, and these components can be integrated in time while the gravitational waves are passing by." — this is a measurement-procedure discussion, not a cost/shot-count or calibration discussion.
- No occurrence anywhere in the file of "ratio," "calibrat*," "thermal," or "temperature" (checked via grep over full text).

**Verdict**: **BACKGROUND.** FGHN's entire taxonomy lives inside D32 (absolute-response register) exclusively — every listed class is a fixed-observable before/after difference, with zero engagement with ratio/calibrated functionals, gauge-redundancy invariance, measurement cost, or thermal states. It anticipates neither D32's naming register explicitly nor D33 at all. Positioning sentence for the paper: *"FGHN's canonical taxonomy of persistent observables is entirely absolute-response (D32); it neither poses nor needs the calibrated/relational distinction, since all its constructions are vacuum, zero-temperature, and reference-frame-persistent by assumption."*

---

## 2. arXiv:2109.03832 — Grant, Nichols, "Persistent gravitational wave observables: Curve deviation in asymptotically flat spacetimes"

**Verified**: title at `ms.tex:41`; authors at `ms.tex:32,35` (Alexander M. Grant, David A. Nichols). Matches.

**Summary**: Paper II in the FGHN series; computes the curve-deviation observable at null infinity using Bondi–Sachs asymptotics, and splits every persistent observable into a "charge" contribution (difference of nonradiative data before/after) and a nonlinear "flux" contribution (vanishes without radiation) — generalizing the ordinary/null memory split. Again everything is a fixed-observable difference; no ratio or calibration functional appears. The only place a "ratio" word occurs is standard GW detection language (signal-to-noise ratio for detectability), unrelated to a memory-susceptibility construction.

**Key quotes**:
- "the displacement memory signal... its detectability can be estimated in terms of its signal-to-noise ratio," `ms.tex:1230` — ordinary SNR, not a calibrated relational functional.
- Charge/flux decomposition summary, `ms.tex:1206-1220` — purely difference-based (Δξ, ΔK, ΔH), consistent with the parent paper's D32-only structure.
- No hits for "thermal," "temperature," "calibrat*" in the full text.

**Verdict**: **BACKGROUND.** Same register as FGHN — pure D32, no thermal setting, no ratio functional beyond ordinary detection SNR. Positioning sentence: *"Grant–Nichols extends FGHN's absolute-response taxonomy with a charge/flux split, still entirely within D32; it does not touch calibration, gauge-redundancy invariance, or thermal degradation."*

---

## 3. arXiv:2601.23019 — Zosso, Magaña Zertuche, Gasparotto, Cogez, Inchauspé, Jacobs, "Toward claiming a detection of gravitational memory"

**Verified**: title at `main_v2.tex:78`; authors at `main_v2.tex:80-99` (Jann Zosso, Lorena Magaña Zertuche, Silvia Gasparotto, Adrien Cogez, Henri Inchauspé, Milo Jacobs). Matches (2026 preprint, CERN-TH-2026-042).

**Summary**: A detection-strategy paper for LISA/ground-based memory searches, not a classification paper. Its central physics point is exactly the one flagged in the brief: interferometric GW detectors are *intrinsically insensitive to the DC (zero-frequency) memory offset itself* and can only ever probe the time-dependent transition/rise leading up to it, because instrumental noise diverges at low frequency (AC-coupled, band-limited detectors). It builds a rigorous, physically-motivated model of the observable "memory rise" (via Isaacson frequency-scale separation between oscillatory GWs and the low-frequency memory buildup) and uses a Bayes-factor ratio 𝓑 = 𝒵_mem/𝒵_no-mem as a statistical detection criterion. No thermal states, no gauge-invariant relational-memory functional in the D33 sense — the Bayes factor is a statistical model-comparison ratio (evidence ratio), not a physical detector observable equal to a soft-theorem DC datum.

**Key quotes** on detector insensitivity to the final offset:
- Abstract, `main_v2.tex:108`: "gravitational wave detectors are intrinsically insensitive to the final offset and can only probe the associated transition."
- `main_v2.tex:143`: "they are fundamentally insensitive to the final, constant memory offset, in the sense that once a radiation burst has passed, it is not possible to verify a permanent displacement of the test masses" (with footnote: true for both ground- and space-based detectors, since "uncontrolled low-frequency noise prevents a direct observation of a permanent shift").
- `main_v2.tex:366`: "interferometric detectors are intrinsically insensitive to this zero-frequency memory offset itself and can only probe the time-dependent transition between the initial and final states."
- `main_v2.tex:822`: "current and planned GW observatories are intrinsically unable to measure the net, DC component of the memory offset... renders them effectively blind to DC signals, where instrumental noise grows steeply toward low frequencies."
- Bayes factor definition, `main_v2.tex:993-996`: 𝓑 = 𝒵_mem/𝒵_no-mem — a ratio, but a *statistical* evidence ratio for model selection, not a gauge-invariant physical susceptibility.

**Verdict**: **ADJACENT.** This paper is the closest prior art on the *instrumental* mechanism by which a D32-style absolute record can become practically unreadable — but the mechanism is classical detector bandwidth/noise, not thermal record erosion, and there is no gauge-invariant calibrated ratio functional, no measurement-cost-vs-detector-time scaling, and no mention of thermal states anywhere in the paper (grep confirms zero occurrences of "thermal"/"temperature"). Positioning sentence: *"Zosso et al. independently identify that a detector's practical inability to read a D32 record can be as physically important as its existence, but attribute this to band-limited instrumental noise rather than to a thermal reference frame eroding its own calibration — the mechanism, register, and formalism are disjoint from D32/D33."*

---

## 4. arXiv:2308.02445 — Solanki, Bhattacharjee, "Soft Theorems and Memory Effects at Finite Temperatures"

**Verified**: title at `main.tex:17`; authors at `main.tex:19` (Divyesh N. Solanki, Srijit Bhattacharjee). Matches.

**Summary**: Computes leading soft-photon and soft-graviton theorems in thermofield dynamics, i.e. with the **radiation field itself** (the soft photon/graviton bath) placed in a thermal state via the doubled thermofield Hilbert space `ℋ_T = ℋ⊗ℋ̃` (`main.tex:52-63`) — *not* the detector, and not the source/scatterers, which remain ordinary asymptotic in/out states. This is explicitly motivated by the T=2.7K CMB photon bath (`main.tex:41`). The paper's central finding is that the soft factor loses universality at finite temperature (bosons and fermions contribute with opposite signs and different magnitudes), while the zero-temperature (β→∞) limit correctly reproduces the standard Weinberg soft theorem and Ward identities remain exact (with a temperature-augmented gauge parameter). It then derives thermal corrections to both the EM "velocity kick" memory and the gravitational (Christodoulou/BT) memory.

**Key quotes** — the memory statements are literally written as *ratios of S-matrix elements*, structurally the closest formal echo of a calibrated relational functional found across the group's papers:
- `main.tex:427-431` (EM memory): 
  `⟨out|ΔA_z^(0) S|in⟩ / ⟨out|S|in⟩ = (-√2e/4π(1+z z̄)) lim_{ω→0} ω Σ_n Q_n η_n (p_n·ε⁺)[e^{βp_{n0}}/(p_n·q+iη_nε) − 1/(p_n·q−iη_nε)]` — reducing at β→∞ to the ordinary zero-T memory ratio, `main.tex:438-440`.
- `main.tex:539-547` (gravitational memory): the analogous ratio `⟨out|ΔC_zz S|in⟩/⟨out|S|in⟩`, reducing at zero temperature to the Braginsky–Thorne result, `main.tex:552-554`.
- Setting statement: "we use the thermal field operator... The total Hilbert space of the combined system is defined as ℋ_T=ℋ⊗ℋ̃" (`main.tex:52-56`) — confirms the field/radiation bath, not detector or source, is what's hot.
- Main memory statement/summary, Conclusion (`main.tex:648-650`): "the soft photon and graviton theorems both receive temperature dependent contributions... the universal character of the leading soft factors as known for the zero temperature field theory is getting lost... the thermal contributions to the soft factors do not alter the Ward identities."
- Numerical sensitivity claim, `main.tex:409-410`: "It seems, by studying the memory signal at finite temperatures compared to the zero temperature signal one may be able to tell the nature of scatterers involved in the bulk."

**Verdict**: **OVERLAPS (partial, on form only).** This is the single closest piece of prior art to a "ratio functional" appearing under the word "memory": both the EM and gravitational memory statements are written exactly as normalized S-matrix ratios ⟨out|ΔO·S|in⟩/⟨out|S|in⟩, i.e., a cross-section-like calibrated quantity, and the setting is explicitly thermal. However it is thermal *in a different register entirely* from D33's adjudicated instance: the heat bath lives in the radiation/soft-mode sector of the field (motivated by the CMB), not in the detector's own reference frame or its calibrating ruler, and the paper never asks whether the *ratio itself degrades or becomes hard to read out* as T grows — it only tracks the ratio's *value* (a smooth deformation, bosons/fermions moving oppositely, both converging to the zero-T answer as β→∞). There is no discussion of gauge-redundancy invariance of the ratio, no measurement-cost/shot-count accounting, and no notion of "record erosion" — the paper's thermal bath modifies the soft-factor coefficient but never threatens the calibrating denominator's persistence. Positioning sentence: *"Solanki–Bhattacharjee write the leading photon/graviton memory as a normalized S-matrix ratio under a thermal radiation bath — the closest formal precedent for a ratio-shaped memory functional in the literature — but the heat bath sits in the field/soft sector, not the detector's own reference frame, and the paper tracks only the ratio's finite-temperature value, never asking whether the calibrating denominator itself decays or whether readout cost grows; D33's thermal-record-erosion claim (a detector reference frame eroding its own record, cost diverging in detector time) is not anticipated."*

---

## 5. arXiv:2406.07106 — Ben Achour, Uzan, "Displacement versus velocity memory effects from a gravitational plane wave"

**TITLE/AUTHOR VERIFICATION — no mismatch found**: `MEM-DRAFT-Revised.tex` has no arXiv metadata comment and, unusually, `\begin{document}` does not appear until deep in the preamble (line ~275), so an initial header-only scan returned nothing (0 hits for "document"/"memory" case-sensitive) — this was a false alarm caused by grep case-sensitivity plus the very long preamble of `\def`/macro lines before content begins; a case-insensitive scan (`grep -ain`) resolved it cleanly. Confirmed at:
- `MEM-DRAFT-Revised.tex:277`: `\title{...Displacement versus velocity memory effects \\ from a gravitational plane wave}`
- `MEM-DRAFT-Revised.tex:278`: `\author{Jibril Ben Achour^{1,2,3} and Jean-Philippe Uzan^{4,5}}`

Title matches the brief's stated title exactly — **no flag needed.**

**Summary**: A purely classical, vacuum (zero-temperature) general-relativity paper on test-particle geodesic deviation in an exact gravitational plane-wave (pp-wave) spacetime. It establishes analytic conditions, in terms of initial separation ζ, initial relative velocity ζ̇, and the wave profile 𝒜_i(u), for three mutually exclusive outcomes at late times (`MEM-DRAFT-Revised.tex:809-847`): Velocity Memory (VM: Δζ̇≠0), Vanishing Velocity Memory (VM0: Δζ̇=0 but nontrivial history), and Displacement Memory (DM: ζ̇_f=0, particles settle at constant separation). This resolves a standing puzzle (Zhang et al.) about whether vacuum plane waves can support displacement memory at all. The classification criterion is purely kinematic (sign/vanishing of asymptotic relative velocity/acceleration), with no ratio, no calibration, no detector-cost or thermal content whatsoever.

**Key quotes**:
- Classification definitions, `MEM-DRAFT-Revised.tex:817-830`: VM, VM0, DM as above — criteria are differences of ζ̇, not ratios.
- Grep for "ratio," "calibrat," "thermal," "temperature," "measurement cost," "detector" across the full file returns **zero hits** (confirmed via `grep -ain`).

**Verdict**: **BACKGROUND.** Pure classical vacuum GR, D32-shaped by construction (fixed observable ζ, difference before/after), with a displacement-vs-velocity classification criterion orthogonal to (and much narrower than) D32/D33 — it distinguishes two *kinds* of D32 memory (position-type vs velocity-type), not absolute-vs-calibrated registers. No thermal, no ratio, no cost. Positioning sentence: *"Ben Achour–Uzan's displacement-vs-velocity classification is a taxonomy internal to D32 (which fixed observable — position or velocity — carries the persistent shift), not a distinction between absolute and calibrated registers; it has no thermal or ratio content to differentiate from D33."*

---

## Overall assessment for the campaign

None of the five papers anticipates the D32/D33 distinction as such, and none states or implies the specific structural claim that a thermal reference frame erodes its own record (calibrating denominator decays, readout cost grows exponentially in detector time). The closest material is:

1. **arXiv:2308.02445** (Solanki–Bhattacharjee) — the only place in this set where "memory" is literally written as a ratio of amplitudes, and the only place a thermal bath appears at all — but the bath is in the radiation/soft sector, not the detector's reference frame, and the paper never interrogates whether the ratio's readability degrades.
2. **arXiv:2601.23019** (Zosso et al.) — the only place that explicitly foregrounds a detector's structural inability to access a D32-type absolute record, but the cause is band-limited instrumental noise, not thermal record erosion, and there is no calibrated gauge-invariant ratio functional in the D33 sense (only a statistical Bayes-factor evidence ratio).

The taxonomy's novelty claim — a two-register split (absolute vs. calibrated-relational) with an explicit gauge-invariance condition, a declared measurement-cost obligation, and a structural thermal-erosion phenomenon distinguishing the registers (adjudicated on the two-boundary Schwarzian) — is not present in any of these five papers. Recommend citing FGHN/Grant–Nichols/Ben Achour–Uzan as establishing that the entire prior persistent-observable literature lives in D32, citing Solanki–Bhattacharjee as the nearest formal precedent for a ratio-shaped memory functional (to differentiate sharply: field-thermal vs. detector-thermal, no erosion claim), and citing Zosso et al. as the nearest precedent for detector-side record inaccessibility (to differentiate: instrumental bandwidth vs. thermal calibration decay).


# C5 — infrared-triangle landscape

# Literature Report — C5 Triangle Landscape (0+1d JT/SYK positioning)

Context consulted first: `claims/CLAIMS.md` rows **JT-B-susc** (line 109), **JT-bfly-decay** (line 110), **JT-noplat-abs** (line 111). These prove, at leading one-soft/tree order in the Schwarzian EFT of large-`C` SYK/JT, a calibrated late-time susceptibility equal to a DC soft residue (JT-B-susc); that the celebrated butterfly frame shift is a **transient, non-permanent** relational time delay with zero plateau, not stationary memory (JT-bfly-decay); and that the allowed absolute correlator observable has **no nonzero late plateau** in the balanced sector even where the calibrated ratio has a nonzero susceptibility (JT-noplat-abs). So our own triangle fragment is explicitly scoped, adjudicated, and honest about a negative/no-permanence corner — this is the yardstick for how the other four papers' own permanence and priority claims should be read against ours.

---

## 1. arXiv:2411.13633 — "Soft gravitons in three dimensions"

**Verified**: title at `refs/arxiv-2411.13633/arXiv_v1.tex:60`; authors Jordan Cotler, Kristan Jensen, Stefan Prohazka, Max Riegler, Jakob Salzer at `arXiv_v1.tex:63`; abstract at `arXiv_v1.tex:89–93`.

**Summary.** This is 2+1-dimensional (bulk) quantum gravity with Λ=0 coupled to massless matter, so the asymptotic/null-infinity boundary theory lives on a circle × null time (effectively 1+1d Carrollian data). Pure 3d gravity is first rewritten as a boundary "magnetic Carrollian" field theory of supermomentum/super-angular-momentum whose action is built from the Schwarzian derivative — the authors are explicit this is "Schwarzian-**like**" and only "playing a similar role" to the JT Schwarzian (`arXiv_v1.tex:93`, `:107`), not the Schwarzian itself: it is a function of an angle θ as well as null time u, has different symmetry content (BMS₃, not just PSL(2,R)), and a different effective coupling/density of states from the JT/SYK Schwarzian (`arXiv_v1.tex:686`, footnote). All three corners are constructed for gravity+matter: a BMS₃ Ward identity (asymptotic symmetry), a soft graviton theorem, and a "rotational displacement" + "time displacement" memory effect sourced by null energy/angular-momentum flux (boxed eq. `E:memorybox1`, `arXiv_v1.tex:1303`). Memory permanence is asserted directly at the level of the classical shift Δξ₀ʳ(θ) between early and late null time; no detector/probe operationalization or falloff subtleties beyond the classical shift are discussed. There is no 0+1d or 1+1d claim anywhere — the paper stays strictly in 2+1 bulk / 1+1 boundary.

**Exact quotes:**
- Novelty/priority framing: *"is there a three-dimensional version of the infrared triangle? Naïvely the answer is no... Even so, we will find a suitable analogue"* (`arXiv_v1.tex:105`).
- Permanence: *"Unlike in four spacetime dimensions these memory effects describe a permanent radial displacement rather than angular displacements."* (`arXiv_v1.tex:1307`).
- Low-dimension/triviality claim being refuted: *"There has been some expectation, from the point of view of soft theorems and memory effects, that three-dimensional flat space gravity is in some way trivial. Our work has shown that this is not the case."* (`arXiv_v1.tex:1352`).

**Verdict.** OVERLAPS (closest continuum antecedent for a "Schwarzian-flavored boundary d.o.f. carrying a full triangle"), but not competing directly: their boundary theory is 1+1d Carrollian on a circle at null infinity within a 2+1d bulk, ours is a genuine 0+1d (single-time) Schwarzian/SYK system with no spatial circle and no null-infinity construction at all. Our claim should be worded as **"first infrared triangle assembled entirely within a 0+1-dimensional (single-time, no null infinity) holographic/thermal quantum system"** — 2411.13633's boundary mode is Schwarzian-*like* on a 1+1d Carrollian manifold, explicitly not identical to (and richer than) the plain JT Schwarzian. Positioning sentence: *"Cotler–Jensen–Prohazka–Riegler–Salzer complete the IR triangle for a Schwarzian-like magnetic-Carrollian boundary theory of 2+1d flat-space gravity; our result is the reduction one dimension further, to the 0+1d Schwarzian/SYK system itself, with no residual angular/null-infinity data."*

---

## 2. arXiv:2512.15796 — "Sound as a gauge theory and its infrared triangle"

**Verified**: title at `refs/arxiv-2512.15796/arXivV2.tex:21`; authors Níckolas de Aguiar Alves and André G. S. Landulfo (UFABC) at `arXivV2.tex:23,26`; abstract at `arXivV2.tex:32`.

**Summary.** This is a 3+1-dimensional condensed-matter system: linear acoustics (sound) in an inviscid, irrotational, barotropic fluid, treated at null infinity exactly as in 4d relativistic field theory. All three corners are built: a memory effect (permanent Lagrangian-displacement shift of fluid particles from a retarded-Green's-function large-r expansion, `arXivV2.tex:169` section), asymptotic symmetries (via dualizing the acoustic scalar to a Kalb–Ramond two-form and applying scalar-asymptotic-charge machinery of Campiglia et al., `sec: asymptotic-symmetries`), and a "toy" soft theorem reproducing a Braginsky–Thorne-type formula from image sources (`sec: soft-theorem`, explicitly flagged as not deep — a proof of principle). They are careful that the soft-theorem corner is qualitatively different from the high-energy case because acoustic sources are not fundamental particles but "image sources." Memory permanence is treated with real care: they explicitly separate an "exact" piece of the memory two-form (tied to a large gauge transformation / asymptotic symmetry) from a "harmonic" piece that is *not* captured by any asymptotic symmetry — an honest negative/incomplete corner, analogous in spirit to Satishchandran–Wald's finding for GR. No detector-operational discussion beyond stating lab-measurement prospects.

**Exact quotes:**
- Priority: *"our results provide one of the first examples of an infrared triangle in a condensed matter system"* (`arXivV2.tex:58`).
- On dimension being essential to their construction: *"this is not a property of any specific theory... but rather a very general property of the wave equation in four dimensions"* (`arXivV2.tex:1063`, Discussion §1).
- Honest incomplete-corner statement (their own negative result): *"There is one notable exception to the asymptotic symmetry interpretation... the nonexact part [of the memory tensor] was instead associated... to a permanent shift in the monopole term of φ"* (`arXivV2.tex:1076`).
- Soft-theorem caveat: *"the interpretation of a soft theorem is not as obvious as in high-energy theories... but highlight how this should be interpreted differently from the high-energy counterparts"* (`arXivV2.tex:54`).

**Verdict.** ADJACENT (competitive-landscape precedent for "triangle in a non-fundamental/condensed-matter system," and for candidly reporting an incomplete/negative corner — directly comparable rhetorical move to our JT-noplat-abs). Not a dimensional competitor: their system is 3+1d, tied explicitly to the 4d wave equation's 1/r falloff structure; nothing here touches 0+1d. Our claim should read **"first infrared triangle in a 0+1-dimensional thermal/holographic quantum system"** — cleanly disjoint in dimension and physical system from sound-in-3+1d. Positioning sentence: *"Alves–Landulfo give an honest, partly-negative acoustic triangle in 3+1d built on the standard null-infinity 1/r machinery; our triangle requires no null infinity or spatial falloff at all, since the system has no space."*

---

## 3. arXiv:2310.16683 — "Fracton infrared triangle"

**Verified**: title at `refs/arxiv-2310.16683/frac-short.tex:119`; authors Alfredo Pérez, Stefan Prohazka, Ali Seraj at `frac-short.tex:121,125,128`; abstract at `frac-short.tex:133`.

**Summary.** This is a 3+1d (3 spatial dims, per the dipole moment $d^i=\int x^i \rho\,d^3x$) non-Lorentzian fracton gauge theory. All three corners: a "double kick" memory effect on a probe dipole (two velocity kicks from two distinct radiative null infinities, since fracton theory has two propagation speeds/dispersion relations, `frac-short.tex:423–458`), a novel dipole soft theorem derived both from the memory effect and independently via Feynman diagrams, and novel asymptotic symmetries of the fracton gauge field. This is explicitly billed as the **first non-Lorentzian** triangle, i.e. the competitive landscape's headline "beyond Lorentz symmetry" claim, not a dimensional claim per se — the novelty axis is loss of Lorentz invariance, not low spacetime dimension. Their memory effect is defined generically as "observables that persist in a probe system after the passage of waves" (a kick/velocity-type memory, not obviously permanent displacement in the Zel'dovich–Braginsky sense) — no explicit "permanent" language is used for their own double-kick effect, unlike papers 1 and 2. No detector-operational subtlety or low-dimensional/0+1d discussion appears anywhere.

**Exact quotes:**
- Priority (abstract, doubly stated): *"Together with their asymptotic symmetries this constitutes the first realization of an infrared triangle beyond Lorentz symmetry."* (`frac-short.tex:133`); reaffirmed in Discussion: *"This provides the first instance of an IR triangle... for a theory beyond Lorentz symmetry and further evidence for the robustness of this triangular correspondence."* (`frac-short.tex:802–807`).
- Memory definition (their working definition, generic, no "permanent" language used): *"Memory effects refer to observables that persist in a probe system after the passage of waves."* (`frac-short.tex:200–201`).
- Richness-from-non-Lorentz framing: *"This makes the asymptotic structure of these theories richer than that of their relativistic counterparts... need for implementing new techniques beyond the conventional ones."* (`frac-short.tex:826–830`).

**Verdict.** BACKGROUND for us (it is the direct precedent for the *rhetorical form* "first infrared triangle beyond X," here X = Lorentz symmetry; we use X = spacetime dimension/holographic thermal system). No dimensional overlap — this is 3+1d condensed matter, and their double-kick memory is a velocity kick, not the calibrated-susceptibility/no-plateau structure central to our JT-B-susc/JT-noplat-abs results. Our claim can safely be worded as **"first infrared triangle in a 0+1-dimensional system"**, entirely orthogonal to their "first beyond Lorentz symmetry" claim; both can be true simultaneously without either subsuming the other. Positioning sentence: *"Pérez–Prohazka–Seraj open the non-Lorentzian axis of the competitive landscape (first triangle beyond Lorentz symmetry, in 3+1d); we open the low-dimensional/holographic axis (first triangle in 0+1d), and unlike their double-kick memory, we show one allowed corner in our system has provably no permanent plateau at all."*

---

## 4. arXiv:1709.05018 — Hamada–Sugishita, "Soft pion theorem, asymptotic symmetry, and new memory effect"

**Verified**: title at `refs/arxiv-1709.05018/draft1004.tex:80–82`; authors Yuta Hamada, Sotaro Sugishita at `draft1004.tex:84–89`; abstract at `draft1004.tex:105`.

**Summary.** This is standard 3+1d (explicitly "four-dimensional flat spacetime," `draft1004.tex:121`) QFT: a toy $U(1)_A$ model (complex scalar + Dirac fermion, spontaneously broken axial symmetry) whose Nambu–Goldstone boson is called "pion." All three corners are built for this non-gauge, non-gravity system for the first time: the (subleading) soft pion theorem is rewritten as a Ward–Takahashi identity of an asymptotic symmetry with an infinite tower of conserved dipole-type charges (`sec_soft_ward`), and charge conservation is shown to be equivalent to a "pion memory effect" — a permanent shift in the $1/r^2$ coefficient of the pion field at null infinity, memorizing the dipole flux of hard particles that passed through (`draft1004.tex:707–826`). This is explicitly the earliest transplant of the triangle to a non-gauge-boson (matter/NG-boson) setting — a template the fracton and sound papers both build on conceptually. No detector/operational discussion, and no mention of low dimension or 0+1d/1+1d triviality — the paper stays in ordinary 4d Minkowski throughout.

**Exact quotes:**
- Framing/scope: *"asymptotic symmetries for QED and Quantum Gravity (QG) in four-dimensional flat spacetime are related to soft photon and graviton theorems... We expect that such triangular relations hold in other theories with massless particles."* (`draft1004.tex:121,133`).
- Result/priority: *"the triangular relation in figure \ref{fig:tri} is established for a theory with pions"* (`draft1004.tex:153`); *"we have established that the triangular equivalence relation in a NG boson theory, as in the case of QED and QG"* (`draft1004.tex:826`).
- Memory-permanence mechanism: *"the information of hard particles is memorized in a shift of $1/r^2$ coefficient of pion fields in future or past null infinity"* (`draft1004.tex:153`).

**Verdict.** BACKGROUND (the direct continuum antecedent already flagged in `refs/LEDGER.md` as "THE direct continuum antecedent"); it is the template for extending the triangle beyond gauge/gravity fields to any spontaneously-broken-symmetry NG boson, which is conceptually close to how a Schwarzian mode (pseudo-NG-boson of broken reparametrization symmetry in nearly-AdS₂/JT) plays its role in our construction. No dimensional or system overlap: strictly 4d Minkowski scattering theory, no holography, no thermal/finite-temperature system, no lattice. Our claim is safely **"first infrared triangle in a 0+1-dimensional (finite-temperature, holographic) quantum system"**, wholly disjoint from Hamada–Sugishita's 4d flat-space NG-boson triangle. Positioning sentence: *"Hamada–Sugishita show the triangle survives the move from gauge bosons to any spontaneously-broken-symmetry NG boson in 4d flat space; our result shows it survives the much more severe move to 0+1 dimensions and finite temperature, where the Schwarzian mode plays the analogous near-Goldstone role but there is no null infinity, no spatial falloff, and (per JT-noplat-abs) not every corner has a nonzero plateau."*

---

## Cross-paper synthesis for our wording

None of the four papers touches 0+1d, and none claims impossibility or triviality of a triangle in 0+1d/1+1d — the "trivial" worry that appears (2411.13633, line 1352) is specifically about 2+1d *gravity* (no propagating graviton), refuted there, and is not a statement about low-dimensional systems in general. So there is no direct refutation to argue against; the safe, exactly-true novelty claim for our paper is:

> "the first construction of the full soft-theorem/asymptotic-symmetry/memory infrared triangle within a 0+1-dimensional (single-time, no spatial null infinity) quantum system — specifically a holographic/thermal (JT/SYK–Schwarzian) system — with an honestly adjudicated negative corner (no late-time plateau for the allowed absolute observable, JT-noplat-abs) rather than a uniformly positive assembly."

This is compatible with, and should be positioned alongside rather than against: 2411.13633 (dimension-reduction precedent, but 2+1d bulk/1+1d boundary, not 0+1d), 2512.15796 (condensed-matter precedent with its own honest incomplete corner, but 3+1d), 2310.16683 (non-Lorentzian-axis precedent, 3+1d), and 1709.05018 (matter/NG-boson-axis precedent, 4d flat space).


---

## Orchestrator notes on agent flags (2026-08-31)

- The C3 agent flagged 2603.18154 as "date-anomalous"; it is not — the id
  denotes 2026 March, five months before today (2026-08-31). No action.
- The 1408.6560 mismatch (the SWEEP cited a wrong id for Stanford-Susskind
  "Complexity and Shock Wave Geometries") is recorded in refs/LEDGER.md;
  the correct id 1406.2678 is fetched and title-verified. arxiv-1408.6560/
  (Adams-Roberts-Saremi, Hawking-Page in massive gravity) must not be
  cited for complexity content.
- 2406.07106 title verified (Ben Achour-Uzan) — the earlier NO-TITLE flag
  was a long-preamble false alarm; recorded in LEDGER batch-12 update.
- Maxfield (2603.18154) framing caveat: the "finite" statements concern
  finiteness of classifying/moduli data, not a literal phrase; respect at
  drafting time (pre-submission critic obligation).
