# Digest — Memory, Symmetries and Soft Theorems

- **Title:** Memory, Symmetries and Soft Theorems
- **Speaker:** Andrew Strominger
- **Venue/date:** not stated on the recording. Internal evidence puts it in **early-to-mid 2015**: he refers to
  "at Joe's birthday last year" (Polchinski's 60th, 2014 — the occasion of arXiv:1312.2229), says the
  spin-memory paper with "Sasha" (Zhiboedov) is already written (arXiv:1502.06120, Feb 2015), and says the
  massive-particle generalisation is being written *now*. A small, senior audience interrupts constantly
  (Gary Horowitz and Juan Maldacena are addressed by name; a questioner who asks about causal diamonds and
  finite boxes is plausibly Tom Banks — unconfirmed).
- **Video id:** `CdFyoaNv8GI` — https://youtu.be/CdFyoaNv8GI
- **Duration:** 01:23:59
- **Source file:** `refs/strominger-videos/extra-01-CdFyoaNv8GI.md` (auto-captions; secondary source, not L3 ground truth)
- **Written companion:** arXiv:1703.05448 (`refs/arxiv-1703.05448/soft_Arxiv_update.tex`)

**Arc.** A blackboard seminar walking the three corners of the infrared triangle — soft graviton theorem,
gravitational memory, BMS — and then the two connecting legs, closing on black hole information. The
derivations are the ones in the written lectures. What is not in the written lectures is the *seminar
around* them: roughly half the running time is audience interruption, and Strominger spends it defending
the least popular part of the story (energy conservation at every angle), conceding what he does not
understand (the transverse term in the supertranslation vector field, sub-subleading soft theorems,
whether soft hair contributes to black hole entropy), giving the intuition he actually uses (null infinity
is ultralocal, so the sphere points are free to move independently), saying plainly why the whole subject
appealed to him (memory is *how you measure a soft graviton* — a worry that had bothered him), and — in the
last ten minutes — being pushed into the most campaign-relevant exchange in the recording: whether any of
this survives on a *finite* region with a boundary.

---

## Insights

### 1. Memory is what makes a soft graviton measurable — and that had been bothering him
The clearest "why I care" statement in the talk, offered spontaneously in the middle of an answer about
hydrodynamics. He had been making the argument that these symmetries are non-trivial because they relate
matrix elements with soft gravitons, and the obvious objection — you cannot measure a zero-energy particle
— had been nagging at him. The memory effect is his answer: people are actually building the detector.

> "it always bothered me to have all this ... I like to make the argument that these symmetries are real
> and non-trivial because they relate Matrix elements involving soft gravitons but it sort of bothered me
> you know ... how do you measure a soft graviton and well this is how you measure [a] soft graviton
> people are building detect[ors] ... it makes in my mind it makes soft particles more physical to look at
> them in in in this way even if it is just a fora [Fourier] transform"

`[CdFyoaNv8GI @ 00:34:36]` — tags: memory, soft-theorems, methodology, experiment

### 2. Why supertranslations exist at all: null infinity is ultralocal
His own intuition, flagged as such ("the way I think about this"). Points of null infinity are causally
disconnected from one another, so nothing ties them together; a rule forcing them all to move by the same
amount would itself be the strange thing. The written lectures derive supertranslations from falloff
conditions on the metric; they never give this causal argument.

> "the way I think about this is that all the points at null Infinity are out of causal contact so it's an
> ultr[a]local Theory there's nothing tying together these points on the sphere and so you can you can move
> them up and down um independently it would sort of violate causality to have some principle that forced
> you to move them all together"

`[CdFyoaNv8GI @ 00:37:46]` — tags: asymptotic-symmetries, supertranslations, methodology

### 3. Asymptotic symmetries on a finite region with a boundary — his answer, and its caveat
The most campaign-relevant exchange in the recording. A questioner proposes gauge transformations that are
pure gauge everywhere except in an infinitesimal neighbourhood of the boundary of a causal diamond, and
suggests these should go over into BMS supertranslations in the large-region limit. Strominger agrees, and
gives the symplectic reason: cut off away from infinity the transformation is a null (degenerate) direction
of the symplectic form; the boundary term at infinity is exactly what makes it non-degenerate, hence
physical.

> "a BMS translation transformation is a diffe[o]morphism and if you would you know cut it off away from
> Infinity it's a null direction [of the] simplec[tic] structure but it's a non degenerate direction of
> the simplec[tic] structure exactly because of a boundary term at Infinity so it's the same story as you
> always have when you have a boundary condition that makes some gauge Transformations into things that
> act non-trivially on the phase space"

`[CdFyoaNv8GI @ 01:20:25]` — tags: asymptotic-symmetries, charges, methodology, supertranslations

### 4. …but a finite system generically has *less* symmetry than the infinite one it grows into
The immediate caveat, and it is a warning rather than an encouragement. Whatever boundary conditions you
impose at finite size restrict you to their symmetries, and the known AdS$_3$ cutoff constructions do not
recover the full conformal group. He says this is "almost certainly true" in general, and that in all known
ways of doing it the recovery is difficult.

> "it's generally true that if you try ... your finite system will have the boundary will have less
> symmetry than the infinite system it grows to and so a minute ago I said in ads3 you can do this with a
> cut off but what you actually find with a cut off is of course you don't have the full set of conformal
> Transformations at any finite distance you only have some subset that's been preserved by [the boundary
> conditions] you impose in all known ways of doing it ... it's difficult to recover the full Group by
> doing this"

`[CdFyoaNv8GI @ 01:22:31]` — tags: asymptotic-symmetries, pitfalls, open-problems, methodology

### 5. …and the intermediate position: finite distance plus extra boundary conditions might work
Between the two, he does allow the constructive version — work at finite distance, impose extra boundary
conditions, and look for an analogue of BMS there. He calls whether this works in Minkowski space a
technical question, not a conceptual obstruction.

> "you could do what Tom wants to do which is you could work at finite distance and impose extra boundary
> conditions and then there could be an analog of [B]MS Transformations so it's the the infinite size limit
> of a system ... you can certainly do this in ads to recover a boundary gravity in ads3 you know it's just
> a technical question of whether it works in [Mink]owsky space"

`[CdFyoaNv8GI @ 01:21:28]` — tags: asymptotic-symmetries, open-problems, methodology

### 6. AdS has no version of this because it is gapped
An offhand line in the opening taxonomy, and a strong one: the triangle occurs in QED, non-abelian gauge
theory, gravity, higher dimensions, cosmology — but not in anti-de Sitter space, and the stated reason is
the gap. For any programme that wants to import the triangle into a new system, this is the sharpest
available statement of the necessary condition.

> "we can talk about cosmology and uh this is perhaps not unrelated to what Juan was talking about last
> week uh anti- Deiter [anti-de Sitter] seems not to have a version of this because it's gapped"

`[CdFyoaNv8GI @ 00:04:31]` — tags: asymptotic-symmetries, soft-theorems, methodology, open-problems

### 7. …and the corresponding methodological complaint about studying gravity in a box
Later, in the black hole discussion, the same point returns as an opinion about how the field has been
working. He is careful not to overstate it, but he does not withdraw it either.

> "if you were to study quantum gravity by putting it in a box and taking that box out to Infinity you
> would miss all of this right so I'm not sure that um I myself would not dismiss the relevance of that"

`[CdFyoaNv8GI @ 01:07:45]` — tags: methodology, black-holes, open-problems

### 8. Why gravity got there first, told as a joke
Gravity is normally the corner we understand worst; here it is the best understood, and he says the reason
is historical rather than technical.

> "it's [o]ddly the best understood example ... and it's the one that involves gravity gravity is usually
> the thing that we understand the least but in this case for really peculiar not for technical reasons but
> really for peculiar historical reasons I guess it's just the relativists are smarter than the field
> theorists or something"

`[CdFyoaNv8GI @ 00:04:31]` — tags: history, methodology

### 9. The two literatures were separated by nothing but notation
On putting the Weinberg soft factor and the Braginsky–Thorne memory formula side by side. He says outright
that the similarity is hard to miss — and was missed for three or four decades.

> "now it's hard to miss the similarity between this formula here and this formula here even though it
> actually was missed for the last 40 years um 30 years"

`[CdFyoaNv8GI @ 00:25:01]` — tags: history, memory, soft-theorems

### 10. …and the one-line explanation of why
The cleanest summary of the sociology anywhere in these talks.

> "so these are the same formulas Weinberg was scattering particles [Brag]insk[y] and Thorn[e] were
> scattering Stars"

`[CdFyoaNv8GI @ 00:27:09]` — tags: history, memory, soft-theorems

### 11. A wry note on how the memory effect got its name
Told without malice, but the point stands: attribution follows the last important paper, not the first.

> "then there was [Christodoulou] in [1991] who as the last person to write [an] important pap[er] on the
> subject got his name attached to it and it's sometimes called Christo[doulou] memory"

`[CdFyoaNv8GI @ 00:14:15]` — tags: history, memory

### 12. A caveat on the soft theorem raised from the floor that he had not heard before
An audience member points out that the soft limit needs non-exceptional momenta — the soft momentum must be
smaller than every internal momentum and every partial sum, and if an internal line is itself soft you must
add emissions from it. Strominger's reply is an honest "I didn't know about this", and a hope that it does
not matter for the talk. Worth recording as a live caveat on the domain of validity.

> "okay um I didn't know about this um I hope it doesn't affect what I'm going to say it sounds interesting
> though I'm sure it just makes the story prettier when you take it"

`[CdFyoaNv8GI @ 00:10:02]` — tags: soft-theorems, pitfalls, methodology

### 13. Detection optimism, with a mechanism
He expects gravitational memory to be measured, names pulsar timing arrays as the likely route, and
explains why the $1/R$ suppression is survivable — the sources are enormous and the flux is what enters.

> "I should stress that ... gravitational memory is probably going to be measured ... in the coming decades
> if not sooner ... it's probably going to be you know the Pulsar timing array ... despite the one over R
> this one over R is is is Big because they're looking at you know things in the other side of the Galaxy
> but ... there are also fantastic amounts of energy involved when you merge two black holes"

`[CdFyoaNv8GI @ 00:30:22]` — tags: memory, experiment

### 14. A live self-correction on what "cumulative" means
He first says memory is cumulative and always the same sign, is challenged from the floor, and walks it
back on the spot to the statement he actually means: the effect scales with the total energy flux.

> "no I don't think it's always separating so what do you mean by cumulative it could oscillate ... it's
> proportional to the total energy flux that's what I want to say"

`[CdFyoaNv8GI @ 00:31:25]` — tags: memory, pitfalls, experiment

### 15. Spin memory is out of reach for distant sources — and he does not pretend otherwise
The subleading effect carries an extra $1/R$, which removes distant galaxies from consideration; he
speculates about nearby sources and a space-based detector and immediately says he does not know.

> "you're not going to measure the this what we call the spin memory effect from things in distant
> Galax[ies] but ... it's possible that something like [a comet?] going through [LISA] or something would
> make a big enough effect I don't know you know you look at you have to look at completely different
> things"

`[CdFyoaNv8GI @ 00:32:27]` — tags: memory, superrotations, experiment, open-problems

### 16. Sub-subleading soft theorems: he says plainly that he does not understand them
Asked whether the tower of subleading triangles is infinite, he invokes Gross's 1960s paper for where it
stops and then simply concedes the limit of his understanding.

> "David wrote the seminal paper on this in the 60s and said that it stops here um we don't as they go
> further down we understand them less and less I don't know what the sub sub[lead]ing guy is it's
> confusing"

`[CdFyoaNv8GI @ 00:33:33]` — tags: open-problems, soft-theorems

### 17. He has no good reason for the transverse piece of the supertranslation vector field
Asked why the supertranslation must be accompanied by a correlated transverse diffeomorphism, he declines
to invent an explanation, while stressing that the term is indispensable.

> "you have any intuition about the second term in Zeta there like why you have to adjust transversely ...
> I wish I had a good answer to that but this term is crucial in everything you can't just drop this term"

`[CdFyoaNv8GI @ 00:40:56]` — tags: supertranslations, open-problems, methodology

### 18. "Energy conservation at every angle drives people crazy" — and he knows it
The longest and most contested passage of the seminar, and the one he had already fought a year earlier. He
does not soften the claim; he notes that it upsets people and then argues it.

> "so how do how do you see that energy at every angle is yeah this drives people crazy"
> … "to answer the question in the kind of detail — and I think I did this a year ago because it also
> upset people a year ago"

`[CdFyoaNv8GI @ 00:48:35]`, `[CdFyoaNv8GI @ 00:49:42]` — tags: charges, soft-theorems, pitfalls

### 19. …the resolution: the soft quantum, not the hard particles, moves the energy around the sphere
Bhabha-type scattering appears to send energy to new angles. His answer is that the process necessarily
emits a soft quantum, and that this is what restores the angle-by-angle balance.

> "think of Baba [Bhabha] scattering two electrons in[to] different angles well they created [a] soft
> graviton ... it will create a soft graviton that will redistribute energy around the sphere"

`[CdFyoaNv8GI @ 00:50:45]` — tags: charges, soft-theorems, memory

### 20. …and the paradox he cheerfully accepts: soft quanta carry no energy, yet they redistribute it
The audience puts the tension in exactly those words. His reply is definitional: "energy at an angle" is a
field quantity, not a particle count, and he sees no other coordinate-invariant definition.

> "the soft gravitons or soft photons don't carry charge or energy so how can they redistribute energy but
> you're defining energy in a way that [makes it work] — I don't think there is another coordinate [in]variant
> way to define it"
> … "I'm defining the charge at a given angle as the radial component of the electric field I don't think
> there's another reasonable definition of it"

`[CdFyoaNv8GI @ 00:52:50]`, `[CdFyoaNv8GI @ 00:51:49]` — tags: charges, methodology, pitfalls

### 21. …and then a concession on that very point
Pressed that in a U(1) theory both the radial electric field and the charge current are separately gauge
invariant, so his uniqueness claim is too strong, he gives ground. A small moment, but it shows where the
argument is soft.

> "I see what you're saying so maybe maybe there is yeah ... maybe in a U1 Theory it's more — in a non
> a[be]lian Theory you wouldn't be able to do this but in a U1 Theory there might be two gauge [in]variant
> things right I guess the radial component of electric field and the charge current are both separately
> gaug[e in]variant"

`[CdFyoaNv8GI @ 00:52:50]` — tags: charges, pitfalls, methodology

### 22. The matching condition is not a modelling choice — it is the only Lorentz- and CPT-invariant one
A strong claim, stated as a claim: to define gravitational scattering you must relate the past of $\mathcal{I}^+$
to the future of $\mathcal{I}^-$, and he knows of only one invariant way to do it. The consistency with the
soft theorem is then read backwards as evidence that Feynman diagrams have been using that boundary
condition all along.

> "in order to define gravit[at]ional scattering you must impose boundary conditions out here that relate
> the data at the past of scri[be] plus to the future of scr[i] minus as far as I know there's only one
> loren[t]ce invariant CPT ... invariant way of of specifying those that that boundary condition ...
> and that that's that's the one um that I gave and moreover the agreement of this
> with the soft graviton theorem implies that that boundary condition used in real space coordinates is the
> one that's implicitly being used when we do [Feynman] diagrams"

`[CdFyoaNv8GI @ 00:57:05]` — tags: charges, methodology, soft-theorems

### 23. Snapshot of the programme's state: massless only, massive "somehow more complicated"
Useful for dating the talk and for seeing what looked hard at the time. He expects the generalisation to be
trivial and admits it is not behaving that way.

> "this work here was done only [with] massless stuff ... and the generalization to massive particles ...
> we're writing a paper on it now I mean I think it does all trivially generalize but massive particles
> somehow are more complicated"

`[CdFyoaNv8GI @ 00:58:10]` — tags: history, open-problems, charges

### 24. Radiation through null infinity as a domain wall between inequivalent vacua
His preferred picture of the memory effect: the flux is a wall in retarded time, flat vacuum on either side,
the two sides related by a BMS transformation with an explicit formula.

> "so we can think of a radiation flux through null Infinity a[s] a kind of domain wall which separates two
> BMS in[e]quivalent vacua"

`[CdFyoaNv8GI @ 01:01:17]` — tags: memory, vacuum-degeneracy, supertranslations

### 25. Supertranslation charges cannot label the degenerate vacua — you must look at the Lorentz part
A live confusion, resolved on the board. All the supertranslation vacua carry zero supertranslation charge
(the group is abelian), so the charges do not distinguish them; what does distinguish them is $\Delta C$ and
the angular momentum. Anyone building a "which vacuum am I in?" observable should note this first.

> "but these are zero for the entire infinite class of vacua ... so you can't use this to distinguish two
> vacuum States ... so I have to look at something different to diagnose the different vacuum so the
> angular momenta will certainly be different each vacuum has a different angular m[omentum]"

`[CdFyoaNv8GI @ 01:12:01]` — tags: charges, vacuum-degeneracy, pitfalls, superrotations

### 26. The soft sector matters even with no black hole in sight
A questioner grants that a supernova is unitary for ordinary reasons and therefore has nothing to do with
soft gravitons. Strominger disagrees: the supernova emits arbitrarily soft gravitons too, and ignoring them
means you are not describing a unitary process.

> "that's not really true because there are amplitudes where you emit arbitrarily soft gravitons in the
> process of that ... Supernova ... if you don't take them all into account you're not dealing with the
> unitary sc[attering] so you can lose some extra information in soft gravitons if you're not careful"

`[CdFyoaNv8GI @ 01:14:08]` — tags: ir-divergences, dressing, pitfalls

### 27. How this differs from ordinary spontaneous symmetry breaking: angle dependence
Asked whether the black hole simply moves along a moduli space of vacua as in ordinary Goldstone physics, he
gives the distinction he thinks matters. Global Goldstone vacua are not allowed to vary with angle, so the
structure is rigid; here the ultralocality of null infinity liberates the angles from one another, and
motion in the vacuum manifold costs no energy.

> "those symmetries ... are not allowed to be angl[e] dependent so somehow the vacuum at every angle is
> forced to be tied together so it's a much more rigid structure ... here they're liberated from one another
> by the locality[,] the ultra locality at infinity[,] and so you can make a black hole and move around in
> the moduli space of th[e]se [vacua at] finite energy"

`[CdFyoaNv8GI @ 01:17:17]` — tags: vacuum-degeneracy, methodology, supertranslations

### 28. The soft sector may not factorise out of the S-matrix
Asked whether all of this is "just how you treat the soft photons", he starts to deny that the Hilbert space
factorises, corrects himself to a weaker and sharper statement — perhaps the Hilbert space does factorise,
but the S-matrix mixes the factors — and says the soft sector cannot simply be disentangled. He flags his
own uncertainty.

> "I'm not very clear about this but I don't think the Hilbert space on scr[i] minus is just a tensor
> product ... yeah maybe the h[il]bert space is a tensor product but the S Matrix is more complicated ...
> mixes things up in a complicated way we can't just disentangle the soft sector from everything else"

`[CdFyoaNv8GI @ 01:19:22]` — tags: dressing, ir-divergences, open-problems, pitfalls

### 29. Does soft hair contribute to black hole entropy? An honest "I can't answer"
A good question from the floor, met with a work-in-progress reply and an explicit refusal to guess. Note the
distinction he does draw: the soft modes contribute differently to black hole entropy than to vacuum entropy.

> "do they contribute to the black hole entropy very good question do they contribute infinitely well we're
> trying to compute it ... they contribute differently to the black hole entropy than they contribute to the
> entropy of the vacuum ... I can't answer"

`[CdFyoaNv8GI @ 01:04:30]` — tags: open-problems, black-holes, soft-hair

### 30. Where the hair actually *is* is not clear to him
A small but honest admission when challenged that soft hair is long-wavelength and not localised near the
horizon.

> "well I I think it's a little confusing where this stuff is it certainly is long wavelength"

`[CdFyoaNv8GI @ 01:07:45]` — tags: soft-hair, black-holes, open-problems

### 31. Provenance note: the S-matrix symmetry was announced at Polchinski's 60th
Useful for dating the programme's steps, and a reminder that the BMS-invariance-of-scattering claim was first
made in a birthday-conference talk.

> "at Joe's birthday last year I defined a subgroup of BMS ... I put some boundary conditions here I found a
> subgroup that preserved those boundary conditions and argued that that gives us a symmetry of the S Matrix"

`[CdFyoaNv8GI @ 00:45:21]` — tags: history, asymptotic-symmetries

---

## Structure of the argument (thin skeleton)

- `00:00:08` Collaborators; the triangle and its variants (QED, Yang–Mills, gravity, higher dimensions,
  cosmology; not AdS).
- `00:06:50` Corner 1: soft graviton theorem, with a sketch of Weinberg's derivation and an audience caveat
  about exceptional momenta.
- `00:12:06` Corner 2: gravitational memory; geodesic deviation, $\Delta C_{zz}$, and the observation that
  $C$ can be non-zero with zero curvature.
- `00:21:52` Braginsky–Thorne's formula copied from their 1987 paper and matched to Weinberg's soft factor.
- `00:34:36` Corner 3: BMS supertranslations, the vector field, ultralocality, and $\delta C_{zz}=-2D_z^2 f$.
- `00:45:21` Ward identity: BMS invariance of the S-matrix = Weinberg's theorem; long contested Q&A on
  energy conservation at every angle.
- `00:59:12` The memory–symmetry leg: constraint equation, Green's function on the sphere, vacuum transition
  as a domain wall.
- `01:03:26` Black hole information: infinite hair, infinitely many conservation laws, degenerate final
  vacuum; then thirty minutes of Q&A ending on finite regions and boundaries.

---

## Deltas vs the written sources (arXiv:1703.05448)

- **The ultralocality argument for supertranslations is spoken only.** The word does not occur in
  `soft_Arxiv_update.tex`. The notes obtain supertranslations from falloff conditions; the causal picture —
  points of $\mathcal{I}^+$ are out of causal contact, so nothing may tie them together — is offered here as
  the reason the symmetry exists (insight 2), and is reused later to distinguish this from ordinary
  Goldstone physics (insight 27).
- **"AdS has no version of this because it's gapped" (insight 6) has no written counterpart.** The notes
  discuss AdS thirty times, mostly as an analogy (Brown–Henneaux, Fefferman–Graham); they nowhere state the
  gap as the obstruction, nor make the methodological complaint that studying quantum gravity in a box loses
  the whole structure (insight 7).
- **Finite regions with boundaries are discussed here and not in the notes.** Insights 3–5 are the most
  campaign-relevant material in the recording: the symplectic reason a boundary term promotes a gauge
  transformation to a physical one; the warning that a finite system generically carries *less* symmetry than
  its infinite limit, with the AdS$_3$ cutoff as the cautionary example; and the concession that finite
  distance plus extra boundary conditions might still support an analogue of BMS. The notes treat only exact
  null infinity.
- **The personal motivation is stated, and is about measurement.** The notes present memory as one corner of
  a triangle. Here he says that the unmeasurability of a soft graviton had bothered him, and that memory is
  what makes soft particles physical to him (insight 1). This is a framing delta with direct bearing on any
  attempt to give a soft mode an operational meaning.
- **Live defence of energy conservation at every angle, including a concession.** The notes state the
  angle-by-angle conservation laws flatly. The seminar records that the claim "drives people crazy", that he
  had fought the same fight a year earlier, the soft-quantum resolution, and then a genuine concession that
  in a U(1) theory his uniqueness-of-definition argument may be too strong (insights 18–21). The concession
  has no written trace.
- **Honest gaps named aloud.** Three appear here and not in the notes: no good reason for the transverse
  term in $\zeta_f$ (17); no understanding of sub-subleading soft theorems (16); no answer on whether soft
  hair contributes to black hole entropy (29). The notes discuss the subleading theorem confidently and
  treat the vector field as given.
- **Soft/hard factorisation is left open here, before it became a debate.** Insight 28 — the Hilbert space
  may factorise but the S-matrix does not respect the split — is a cautious statement made in 2015, before
  the dressing literature made this contested. Worth pairing with the Strings 2017 talk
  (`extra-04-GpN8VAauyj8`), where he says the Faddeev–Kulish basis is probably incomplete and may fail to
  cluster.
- **Reverse delta (in the notes, absent here):** colour memory, the antipodal matching condition derived from
  the Liénard–Wiechert field (which dominates the 2016–2017 talks and is barely mentioned here — he asserts
  the boundary condition rather than deriving it), the celestial-sphere/CFT reformulation, superrotations
  beyond a passing mention, and the whole Faddeev–Kulish / infrared-divergence chapter.

---

## Transcript quality notes

Auto-captions from a blackboard seminar, so the equations exist only as spoken words and several are
unreconstructable without the board. Recurring substitutions, normalised silently in the prose and bracketed
in quotes: "ASM totic"/"asmtoic" for asymptotic, "super transation" for supertranslation, "scry"/"scribe"/"SC"
for $\mathcal{I}$ (scri), "czz"/"cze" for $C_{zz}$, "fora transform" for Fourier transform, "simplec structure"
for symplectic structure, "manowski"/"MOSI"/"Makowski" for Minkowski, "binsky"/"berinsky"/"ginsky and Thorne"
for Braginsky and Thorne, "Chris sadulu" for Christodoulou, "pnov"/"P norov"/"polarov" for Polnarev,
"anti-Deiter" for anti-de Sitter, "veror"/"barasa" for Virasoro, "Brown and Hano" for Brown and Henneaux,
"jaboa"/"Sasha" for Zhiboedov, "gold stone" for Goldstone, "ultr local" for ultralocal. Dates are mangled:
"911" for 1991, "6D" for the 1960s. Audience members are unidentified except where Strominger names them
("Gary", "Juan", "Tom", "David"); several questions are half-inaudible and the captions merge questioner and
speaker without a break, so a few of the quotes above required judgment about who is talking — where that
judgment mattered it is stated in the entry. One attribution is lost entirely: at `01:20:25` he credits the
symplectic-boundary-term result to "car and somebody ... in the late 80s", which the captions do not resolve
(Crnkovic–Witten is a plausible but unverified reading).
