# Lecture 7 — Supertranslation Charges and Ward Identity

- **Video id:** `Yx7PWgfC1dw`
- **URL:** https://youtu.be/Yx7PWgfC1dw
- **Duration:** 01:48:05
- **Written companion:** arXiv:1703.05448, §§ Asymptotically Flat Spacetimes / Supertranslations / The scattering problem / Conserved Charges (`refs/arxiv-1703.05448/soft_Arxiv_update.tex` lines 2145–2407)
- **Source status:** secondary. Auto-captions, ASR noise throughout. Not L3 ground truth.

**Scope note (per the orchestrator's steering).** This digest deliberately does *not*
restate the derivations that are already in the written lectures. It harvests the
side channel: opinions, warnings, hesitations, historical asides, answers to
audience questions, and remarks about what is deep versus what is bookkeeping.

**Arc.** This is the richest of the four lectures for side-channel material, and the
reason is that the physics forces him into history. The mechanical part —
solve for the diffeomorphisms preserving Bondi gauge, find supertranslations, write
the constraint equation, impose antipodal matching, get the charges, note that the
Ward identity is Weinberg's theorem — takes maybe forty minutes. The rest is an
extended argument with fifty years of the relativity literature: why BMS did not
think they had a symmetry, why Penrose's asymptotic simplicity was too strong, why
the peeling theorems in every textbook fail for two scattering protons, why hundreds
of papers on the edges of $\mathcal{I}$ were wrong, and how a 1992-or-93 email to
Christodoulou turned up the missing falloff in an unpublished lecture note. He also
tells, almost in passing, the actual order in which the research happened.

---

## Insights

### The historical argument (the core of this lecture)

**1. BMS were looking for the Poincaré group and expecting GR to reduce to special relativity in the infrared. They failed, people kept trying for years, and we now know it was impossible.**
The strongest historical framing in the course. Note also his judgement on BMS themselves: they got a hint, but not the import.
> "what they were expecting was that they would out of this story somehow get the [Poincaré] group and they would learn that general relativity reduced to special relativity in some infrared limit and they failed to do that people tried for years to do this ... I think we now know nobody ever succeeded in it and we now know why which is general relativity doesn't reduce [to] special relativity in [the] infrared limit ... general relativity has a spectacularly Rich infrared structure that is just not there in special relativity and BMS were the first to get a hint at this though I don't think they understood the full import of what they found"
`[Yx7PWgfC1dw @ 00:20:34]`, setup at `[Yx7PWgfC1dw @ 00:18:29]` — tags: history, supertranslations, asymptotic-symmetries

**2. BMS did not think they had a symmetry, and he is candid that he does not understand how they *did* think of it.**
A useful reminder that the same equations can sit in the literature for fifty years without anyone drawing the conclusion.
> "BMS did not really ... think of what they did as some kind of symmetry of the theory I'm [not] really [sure] how they thought of it but they certainly didn't think of it as a symmetry of the theory"
`[Yx7PWgfC1dw @ 01:24:05]` — tags: history, supertranslations, asymptotic-symmetries

**3. The criterion for what counts as a symmetry: it has to act on in-states *and* out-states — that is, commute with the Hamiltonian. "Those are the useful things."**
This is the operative definition behind the matching condition, and it is the sharpest statement of it in these lectures.
> "we can't have symmetries that act just on out States and not on in[]states we need to have symmetries that act both on in[]states and out States ... in other words things that commute with the hamiltonian those are the useful things and BMS didn't think they had that and so I'm not sure they used the word symmetry"
`[Yx7PWgfC1dw @ 01:25:10]` — tags: methodology, asymptotic-symmetries, ward-identities, supertranslations

**4. Penrose's asymptotic simplicity, roughly speaking, forces all the BMS charges to vanish — "a fantastic reduction of the phase space".**
And it was not obvious that any solutions satisfied it; families had to be constructed afterwards.
> "asymptotic Simplicity roughly implies that all these charges vanish which is a ... fantastic uh reduction of the phase space ... and it wasn't obvious that there was any solutions that obeyed penrose's boundary conditions and then people proved that there were some families of solutions for which these charges vanishes"
`[Yx7PWgfC1dw @ 01:26:13]`, continuing `[Yx7PWgfC1dw @ 01:27:20]` — tags: history, charges, pitfalls, supertranslations

**5. The view that going beyond asymptotic simplicity was merely technical was, in his words, completely wrong — and the peeling theorems in every GR textbook fail for two protons scattering.**
The example he reaches for is deliberately mundane: not black holes, protons. This is the most quotable warning in the lecture.
> "there was some kind of sense that you would understand most things there are things like the [peeling] theorems which are in every single textbook on general relativity which depend on this asymptotic Behavior which are wrong in very simple situations like for example the scattering that we just observed in the sky of the two black hole mergers ... it doesn't have to be two black holes scattering if you scatter two protons ... the gravitational field produced by that will violate penrose's as[ymptotic] Simplicity"
`[Yx7PWgfC1dw @ 01:27:20]`, `[Yx7PWgfC1dw @ 01:28:23]` — tags: history, pitfalls, open-problems

**6. Two incompatible failure modes had blocked the field: asymptotic simplicity was too strong, and the general case seemed to make $C_{zz}$ logarithmically ill-defined at the boundaries.**
Neither route permitted matching past to future BMS frames, so the matching condition could not even be contemplated.
> "if the [B]ondi news goes like one[ over] U ... the energy can be finite but C won't be well defined c will have a logarithm in it so there were two different kinds of situations that were considered both of which ... did not allow for any matching of the BMS at the future to the BMS at the past"
`[Yx7PWgfC1dw @ 01:29:28]` — tags: history, pitfalls, supertranslations, charges

**7. Christodoulou and Klainerman broke the deadlock with an explicit $|u|^{-3/2}$ falloff for the news, which kills the logarithms and makes $C$ well defined at the edges of $\mathcal{I}$ — "which was crucial".**
He is generous about the work and specific about which part mattered for him: not the global existence theorem, but the falloffs.
> "they showed uh well their big contribution was ... it's really sort of great work in mathematics and also in relativity ... they gave explicit fal[l]offs and in particular they showed that the Bondi news ... falls off like 1 over U to the 3[/2] which means there can be no [log]arithms and that ... this quantity C is well defined at the boundaries of s[c]ry which was crucial"
`[Yx7PWgfC1dw @ 01:30:33]`, continuing `[Yx7PWgfC1dw @ 01:31:38]` — tags: history, memory, supertranslations

**8. The email anecdote: around 1992–93 he wrote to Christodoulou pointing out the contradiction, and was told the answer was in an unpublished Cetraro lecture note, after Lemma 46.**
A small piece of oral history that exists nowhere in the written record, and a nice illustration of how a needed result can sit unpublished for years.
> "this happened ... in '92 or 93 I asked when I realized that penrose's boundary condition and the [peeling] theor[ems] implied that all the BMS charges were trivial I sent [Christodoulou] an email ... I said what's wrong with ... this is contradicting what you're saying ... [he] said oh yes and I explained it in after Lemma 46 in my unpublished lectures at ... [Cetraro] ... and he sent me a copy but the world didn't ... learn about it ... he's a character"
`[Yx7PWgfC1dw @ 01:32:43]` — tags: history, methodology

**9. The research actually went gravity first, and the possibility that it applied to QED made him nervous.**
The notes say only that the lectures are presented "in ahistorical order". This is why.
> "in fact all of this was done before all the stuff that I've presented so far ... because in this BMS story there was this very sharp puzzle nothing made any sense QED seemed to make sense and in fact we didn't think there could be anything new to be learned about QED and it made me nervous to think that all this might also apply to QED where somebody ought to have noticed it"
`[Yx7PWgfC1dw @ 01:33:45]`, continuing `[Yx7PWgfC1dw @ 01:34:49]` — tags: history, methodology, large-gauge

**10. A sociological observation, told without malice: mathematical relativists "shudder" at Bondi quantities and will only discuss coordinate-invariant objects.**
The point is not that they are wrong to prefer invariants; it is that invariants alone cannot solve the scattering problem.
> "if you say to them ... Bondi ... they shudder they don't know what they mean they don't know ... why they should exist and they will only have a discussion with you about coordinate [in]variant quantities like [Riemann] tensors"
`[Yx7PWgfC1dw @ 01:19:48]` — tags: history, methodology, pitfalls

**11. Consequently: computing diffeomorphism-invariant quantities is far from solving gravitational scattering, and the scattering problem was never even properly posed.**
The second half is the stronger claim, and it is stated flatly.
> "finding only the diff[eo]morphism ... invariant quantities is far from solving the problem of gravitational scattering"
> "not only ... was that question never answered the problem was never even posed it was never asked in a way that made any sense"
`[Yx7PWgfC1dw @ 01:21:56]`, `[Yx7PWgfC1dw @ 01:23:00]` — tags: history, methodology, open-problems

### Framing and "how to think about it"

**12. Gravity is the *cleaner* place to see this than QED, because in QED all that changes is a phase, and phases are "slippery".**
His explanation for the century-long delay in noticing large gauge symmetry in electromagnetism, and a good argument for teaching gravity first even though the formulas are longer.
> "in electromagnetism all that was happening was we were changing phases of things coming out in the North Pole and things coming out at the South Pole and phases are kind of slippery quantum mechanical objects and do you count them as real or not ... QED has been around 100 years and nobody noticed them and the reason is that ... it involves these slippery phases"
`[Yx7PWgfC1dw @ 01:02:09]`, continuing `[Yx7PWgfC1dw @ 01:03:14]` — tags: history, large-gauge, supertranslations, methodology

**13. The pulse-relabelling example needs no charge computation at all: it is manifestly a different physical configuration, like boosting a black hole.**
He signposts the moment — "it's all about to get really strange" — and then makes the argument entirely at the level of what an observer sees.
> "so far this may have all seemed kind of formal and not so weird but it's all about to get really strange"
> "you don't need to compute any charges or do any more work it's clear that they're acting non-trivially on the phase space just like you boost a black hole you change its energy ... everybody is going to agree that that is something different"
`[Yx7PWgfC1dw @ 00:58:45]`, `[Yx7PWgfC1dw @ 01:01:07]` — tags: supertranslations, vacuum-degeneracy, methodology

**14. "The geometry really remembers a lot" — the delta-function reading of the charge is energy conservation at every angle, and it says the out-state remembers infinitely much about the in-state.**
The written notes italicise "energy is conserved at every angle"; the spoken version adds the memory framing that ties this corner to the third one.
> "so the geometry really remembers a lot remembers an infinite amount of stuff the outgoing State remembers an infinite amount of stuff about the structure of ... the incoming State and so we can think of this as energy conservation at every angle"
`[Yx7PWgfC1dw @ 01:43:27]` — tags: memory, charges, supertranslations, ward-identities

**15. What "soft" means energetically: soft gravitons can carry locally negative energy, but the contribution is a total derivative and integrates to zero on the sphere.**
A crisp characterisation offered in answer to a question, and one that clarifies the status of the soft term in the local energy flux.
> "it looks like the soft part ... soft gravitons can certainly have locally negative energy now it's a total derivative so it integrates to zero on the sphere ... so they can have negative local energy but ... their total energy is [zero] that's the meaning of the statement that they're sof[t]"
`[Yx7PWgfC1dw @ 01:46:33]` — tags: soft-theorems, charges, memory

**16. Gravitational wave energy at null infinity is unambiguous, and LIGO is the proof — it moved the mirrors.**
He contrasts this with the general curved-spacetime case where local gravitational energy is not well defined.
> "in general in a general curve[d] SpaceTime it's hard to say how much energy is carried by the gravitational field but if you're in near flat space then it is an unambiguous concept and certainly out at null Infinity it is [an] unambiguous concept and we know exactly how much energy was carried by the gravity waves ... it did work moving those things around moving the ... mirrors on the interferometer around"
`[Yx7PWgfC1dw @ 00:54:26]` — tags: memory, charges, history

**17. The Bondi mass rises along $\mathcal{I}^-$ to its maximum, the ADM mass, then falls along $\mathcal{I}^+$.**
A one-line mental picture of the whole conservation story, offered while resolving a sign question from the floor.
> "the Bondi mass is increasing along s[c]ry minus to its maximum the ADM mass and then decreasing again along s[c]ry plus"
`[Yx7PWgfC1dw @ 01:18:43]` — tags: charges, supertranslations

### Warnings, hesitations and open gaps

**18. He has not given a complete definition of asymptotic flatness, and says so plainly — necessary conditions, probably not sufficient.**
Honest scoping. He also notes that superrotations will require going to further subleading orders.
> "I haven't given you here a complete ... mathematical specification of what an as[ymptotically] flat metric is ... I've told you enough of the ingredients of it so that we can get on with our business"
> "I'm pretty sure now that everybody would agree that ... these are necessary if not sufficient conditions for asymptotic flatness"
`[Yx7PWgfC1dw @ 00:14:12]`, `[Yx7PWgfC1dw @ 00:15:14]` — tags: methodology, open-problems

**19. "Let me tell you what I am conspicuously not saying" — the behaviour at the edges of $\mathcal{I}$ has been a huge source of confusion, with hundreds of papers almost all completely wrong.**
He flags the omission at the moment he makes it, rather than letting it pass silently, and gives the physical reason edge conditions are needed: constant news would mean radiating forever at infinite energy.
> "now let me tell you what I am conspicuously not saying and which has been a huge source of confusion ... in the literature"
> "if we had nzz equals constant that would be some Infinite Energy configuration which had been radiating for[]ever"
> "a subject [on] which there were hundreds of papers ... before [Christodoulou] and [Klainerman] almost all of which were completely wrong"
`[Yx7PWgfC1dw @ 00:12:04]`, `[Yx7PWgfC1dw @ 00:13:08]` — tags: pitfalls, history, open-problems

**20. Pitfall raised by a student and confirmed: you cannot perform a supertranslation "at $u=6$". A $u$-dependent shift is not a supertranslation.**
This is exactly the confusion a careful reader will have on first meeting the pulse-relabelling example, and it gets a clean answer — plus a forward pointer.
> "you can't just make the coordinate transformation at U equals 6 because things which depend on [u] ... are not super trans[l]ations so you can't just make it at U equals 6 at least not in any simple way"
`[Yx7PWgfC1dw @ 01:04:16]` — tags: supertranslations, pitfalls

**21. Forward pointer given in the same breath: energy going out to infinity *does* induce a supertranslation.**
The one-sentence version of the memory effect, dropped three lectures before it is treated.
> "however it will turn out that ... energy going out to Infinity does induce a super trans[l]ation ... but it's a more complicated discussion than which we will get to"
`[Yx7PWgfC1dw @ 01:04:16]`, continuing `[Yx7PWgfC1dw @ 01:05:21]` — tags: memory, supertranslations

**22. In gauge theory only phase *differences* were measurable; the gravitational analogue has forty years of literature behind it under the name memory.**
The bridging remark that connects the QED discussion of the earlier lectures to the memory corner.
> "in [gauge] theories the thing[s] we could actually measure were the differences of the ph[as]es it wasn't ... really meaningful to say that the phase at this point is this"
> "there has been 40 Years of discussion of measuring this effect and it's called the gravitational memory effect and so there is a very precise sense in which this can be measured but ... we're not quite there yet"
`[Yx7PWgfC1dw @ 01:05:21]`, `[Yx7PWgfC1dw @ 01:06:26]` — tags: memory, large-gauge, history

**23. The extra integration function $C|_{\mathcal{I}^+_-}$ is "the point that everybody would have missed" — specifying the news is not enough.**
This is the crux of the whole lecture stated as a piece of research-hygiene advice: the free data are not just the radiative field, and the missing datum is exactly where the vacuum label lives.
> "you would also have to specify czz up there and czz would have had to be in order for it to be a vacuum up there ... [of the form] DZ squ[ared] of something so you specify czz up here ... and this is the point that everybody would have missed"
`[Yx7PWgfC1dw @ 01:08:32]`, context from `[Yx7PWgfC1dw @ 01:07:29]` — tags: vacuum-degeneracy, supertranslations, pitfalls, memory

**24. He says outright that pieces of the final-data problem are still unsolved, and that he is only getting us "partway" because of subleading subtleties.**
Twice in three minutes he marks the boundary of what is settled.
> "I think there are still pieces of this problem which are un[]solved but the beginning point of thinking about what that is is you start by specifying everywhere on s[c]ri plus the news function"
> "the reason I say partway is there's some really interesting subtleties in the subleading terms which we're not discussing now"
`[Yx7PWgfC1dw @ 01:06:26]`, `[Yx7PWgfC1dw @ 01:09:35]` — tags: open-problems, supertranslations, methodology

**25. A live "I don't understand this": why $C$ transforms with $-2D_z^2 f$ on $\mathcal{I}^+$ and $+2D_z^2 f$ on $\mathcal{I}^-$.**
Nothing is inconsistent; he simply expects a conceptual reason and does not have one. A good marker of an unresolved small thing that might matter.
> "I feel there should be some conceptual reason that I'm missing why this C is transforming with a minus two on s[c]ry plus and ... a plus two on s[c]ry minus I don't quite understand why this sign was needed but there it is"
`[Yx7PWgfC1dw @ 01:15:19]` — tags: supertranslations, open-problems, pitfalls

**26. Two terminology decisions, both stated as his own preferences rather than conventions.**
First, he abuses "Bondi mass" for "Bondi mass aspect" out of impatience. Second — more useful — he has concluded that inventing separate symbols for the $\mathcal{I}^-$ quantities causes more confusion than it removes, so he reuses the same symbols and distinguishes by argument.
> "I should warn you I have a habit of abusing terminology a little bit and just calling this the Bondi Mass because I get tired of saying the word aspect"
> "different notations appear in different papers and I['ve] myself have come to the conclusion that ... introducing a whole new set of symbols for the ... things on s[c]ry minus causes more confusion than it clarifies"
`[Yx7PWgfC1dw @ 00:06:30]`, `[Yx7PWgfC1dw @ 01:13:01]` — tags: methodology, pitfalls

**27. Black holes: he expects an exact identity to survive, but the integration by parts he performed assumed no flux through $\mathcal{I}^+_+$.**
An explicit statement of which step would need repair, given in answer to a question rather than buried.
> "I am assuming here ... that there will still be an exact identity if you form a black hole but when I took this and integrated by Parts I assumed that there was no boundary term up at s[c]ry Plus[-plus] and if there's anything going out at s[c]ry Plus[-plus] I have to worry about that"
`[Yx7PWgfC1dw @ 01:45:32]` — tags: black-holes, charges, open-problems

**28. On skipping the algebra: the derivation of Weinberg's theorem from the Ward identity is "five pages" and he keeps a promise not to repeat the QED version.**
Worth recording as an honest statement of what has and has not been shown in class, as opposed to in the literature.
> "to show that ... is 5 pages of algebra but it's just like the algebra ... we did it before we did the QED case ... I promise[d] you wouldn't have to go through it again"
`[Yx7PWgfC1dw @ 01:39:04]` — tags: methodology, ward-identities, soft-theorems

---

## Structure of the argument (thin skeleton)

- `00:00`–`00:12` Review of Bondi gauge and the large-$r$ expansion; the news $N_{zz}$ as the gravitational field strength. (Notes §Asymptotically Flat Spacetimes.)
- `00:12`–`00:17` The conspicuous omission: behaviour at the edges $\mathcal{I}^+_\pm$, flagged and deferred.
- `00:17`–`00:43` The BMS calculation, done in class only to leading order, with a three-minute exercise for the students. Result: supertranslations $\zeta_f$. (Notes §BMS Analysis.)
- `00:43`–`00:52` Transformation laws for $N_{zz}$, $m_B$, $C_{zz}$; the inhomogeneous $-2D_z^2f$ term and flat-but-nonzero-$C$ vacua. (Notes eq. for $\mathcal{L}_f C_{zz}$.)
- `00:52`–`00:57` The $uu$ constraint equation and $T_{uu}$; the LIGO remark on unambiguous radiated energy.
- `00:57`–`01:06` The two-pulse relabelling example, and Q&A on why this is physical.
- `01:06`–`01:19` The space of final data on $\mathcal{I}^+$, the extra integration function, and the mirror story on $\mathcal{I}^-$.
- `01:19`–`01:35` The historical argument: relativists versus Bondi quantities, why the scattering problem was never posed, Penrose, peeling, Christodoulou–Klainerman, the email.
- `01:35`–`01:48` Matching conditions, supertranslation charges, the Ward identity, and energy conservation at every angle. (Notes §The scattering problem, §Conserved Charges.)

---

## Deltas versus the written lectures (arXiv:1703.05448)

1. **The Penrose / peeling critique is spoken only, and it is severe.** The notes never discuss asymptotic simplicity or the peeling theorems. Spoken: asymptotic simplicity "roughly implies that all these charges vanish" (`01:26:13`); the belief that going beyond it was technical was "completely wrong" (`01:27:20`); the peeling theorems "are in every single textbook on general relativity ... [and] are wrong in very simple situations", with two scattering protons as the example (`01:28:23`). If any single item from these four lectures deserves to be recorded in a secondary source, it is this one.

2. **The Christodoulou email anecdote** (`01:32:43`), including the date (1992 or 93), the Cetraro lectures, "after Lemma 46", and "he's a character". Entirely absent from the notes, which cite Christodoulou–Klainerman as a published result with no story attached.

3. **The research order.** The notes contain one sentence: "These lectures have presented the material in ahistorical order." Spoken (`01:33:45`, `01:34:49`) he explains that the gravity work came first, that the BMS puzzle was sharp while "QED seemed to make sense", and that the prospect of the same structure in QED "made me nervous ... where somebody ought to have noticed it".

4. **The "what counts as a symmetry" criterion** (`01:25:10`) is stated as an operational rule spoken only: symmetries must act on both in- and out-states, i.e. commute with the Hamiltonian, "those are the useful things". The notes present the diagonal subgroup as a construction; the spoken version gives the reason the construction is the point.

5. **The BMS motivation and failure is told as a multi-year human effort.** The notes say the Poincaré expectation in two sentences. Spoken (`00:18:29`, `00:20:34`): "people tried for years to do this", "nobody ever succeeded", "BMS were the first to get a hint at this though I don't think they understood the full import of what they found".

6. **The sociology of mathematical relativity** (`01:19:48`) and the claim that the classical scattering problem "was never even posed ... in a way that made any sense" (`01:23:00`). The notes make the technical point (the maximal Cauchy development determines the data only up to a BMS frame) but not the historical or sociological one.

7. **The "everybody would have missed it" framing of the extra integration function** (`01:08:32`). The notes list the Cauchy data as $\{N_{zz}, C|_{\mathcal{I}^+_-}, m_B|_{\mathcal{I}^+_-}\}$ without comment. Spoken, the extra datum is singled out as the thing the whole field overlooked — which, given that it is the vacuum label, is the pedagogically important point.

8. **The live sign puzzle** (`01:15:19`): why $\mp 2D_z^2 f$ on $\mathcal{I}^\pm$. The notes simply carry both signs. An admitted small gap in understanding is worth recording as such.

9. **The soft-graviton-negative-local-energy characterisation** (`01:46:33`) is spoken only, in answer to a question, and is a genuinely useful clarification of what the soft term in the local energy flux is doing.

10. **The "you cannot supertranslate at $u=6$" pitfall** (`01:04:16`) arises from a student question and does not appear in the notes. Nor does the immediate forward pointer that outgoing energy *induces* a supertranslation.

11. **Notation policy** (`01:13:01`): reuse the same symbols on $\mathcal{I}^-$ and distinguish by argument, rather than inventing a parallel alphabet. The notes silently follow this convention without justifying it.

12. **Emphasis deltas rather than content deltas.** The two-pulse example appears in the notes with $u=100/200$ and here with $u=6/1000$ — but the spoken version adds "you don't need to compute any charges" and the black-hole-boost comparison (`01:01:07`). Likewise "energy is conserved at every angle" is italicised in the notes, but "the geometry really remembers a lot ... an infinite amount of stuff about the structure of the incoming State" (`01:43:27`) is spoken only, and it is the phrasing that connects this corner to memory. The "slippery phases" explanation for why QED took a century (`01:02:09`, `01:03:14`) is a richer version of the notes' one-clause "perhaps in part due to the quantum nature of the electromagnetic symmetries".

13. **Not a delta (checked):** the Bondi metric expansion, $\mathcal{L}_f$ on $N_{zz}$, $m_B$, $C_{zz}$; $C_{zz}=-2D_z^2C$ as the flatness condition; $C$ as the Goldstone mode; the constraint equation and $T_{uu}$; the antipodal matching conditions and the diagonal subgroup; the supertranslation charges; and the equivalence to Weinberg's theorem all appear in the notes (lines 2169–2377).

---

## Transcript quality notes

- This transcript appears to come from a different ASR pass than lectures 5, 6 and 8: it uses different error patterns ("s[c]ry"/"scri" spelled several ways within one paragraph, "ASM totically" for "asymptotically", "dimorphism" for "diffeomorphism", "lead derivative"/"leader" for "Lie derivative", "manowski"/"Makowski"/"monkowski" for Minkowski, "bond[y]" for Bondi, "pon[er]" for Poincaré, "remon"/"remont" for Riemann, "vial tensor" for Weyl tensor, "noose" for news, "appealing"/"healing" for peeling, "Cur" for Kerr, "chrisad"/"Christ douer"/"chris sadulu" for Christodoulou, "cpri" for Cetraro).
- `[00:17:24]` he corrects an order-of-$r$ error he made in lecture 6 (`OXl7IXT7_Cw @ 01:19:46`): $\beta$ must be $O(1/r^2)$, not $O(1/r)$. Worth carrying if cross-referencing.
- `[00:29:14]`–`[00:39:20]` is a ten-minute in-class exercise with only fragments of the exchange captured; several student questions are inaudible and his replies are elliptical ("no it's g g that's right but I'm only working out ..."). Not usable for quotation.
- `[00:54:26]` "whatever it was gw9 what that whatever those black" is ASR garbage for a LIGO event designation (presumably GW150914). The surrounding sentence about the interferometer mirrors is clean.
- `[01:47:36]` the lecture ends mid-thought with a single stray "I".
