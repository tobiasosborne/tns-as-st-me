# Lecture 6 — Large Gauge Symmetry in Non-Abelian Gauge Theory

- **Video id:** `OXl7IXT7_Cw`
- **URL:** https://youtu.be/OXl7IXT7_Cw
- **Duration:** 01:22:30
- **Written companion:** arXiv:1703.05448, §§ Celestial Correlator / Non-Abelian Gauge Theory / Asymptotically Flat Spacetimes (`refs/arxiv-1703.05448/soft_Arxiv_update.tex` lines 1886–2202)
- **Source status:** secondary. Auto-captions, ASR noise throughout. Not L3 ground truth.

**Scope note (per the orchestrator's steering).** This digest deliberately does *not*
restate the derivations that are already in the written lectures. It harvests the
side channel: opinions, warnings, hesitations, historical asides, answers to
audience questions, and remarks about what is deep versus what is bookkeeping.

**Arc.** Two halves with a hinge in the middle. The first hour finishes non-abelian
gauge theory: the soft gluon theorem written as a Kac-Moody Ward identity on the
celestial sphere, the contour integral that generates holomorphic large gauge
transformations, and then — the most valuable stretch — a sustained set of remarks
on why the classical non-abelian scattering problem is not even well-posed without
a matching condition, why the S-matrix is missing in non-abelian gauge theory, and
what he thinks the received statements about that are getting wrong. The last
twenty minutes open gravity: Bondi coordinates (with an apology for them) and the
falloff conditions defining asymptotic flatness (with a warning that the field got
these wrong at the edges of $\mathcal{I}$ for thirty years).

---

## Insights

### Framing and "how to think about it"

**1. The general situation is that the soft factor is an *operator* on the external states; the abelian case where it is just a number is the exception.**
Worth internalising: "soft factor = number times the same amplitude" is a special-case intuition that will mislead you in the non-abelian, photino and subleading cases alike.
> "the soft factor is no longer just a number and this is the general situation it's only in very special situations that the soft factor is just the number that multiplies [t]he Matrix element the more General situation is that it's an operator which acts on the s Matrix element and changes the external States one at a time and then you sum up all those terms"
`[OXl7IXT7_Cw @ 00:06:26]`, continuing `[OXl7IXT7_Cw @ 00:07:29]` — tags: soft-theorems, nonabelian, methodology

**2. He states a preference: the celestial current-algebra formulation is nicer than either the momentum-space soft theorem or the in/out charge formulation, and more likely to lead somewhere.**
This is a bet about which language is productive, not a theorem. It is also the reason the notes reorganise the non-abelian chapter around celestial correlators.
> "I think that this way of looking at things is much more natural than this way of looking at things ... it's even nicer than the way we were writing it before where we were talking about ingoing and outgoing States and charges ... it captures the same information but I think in a nicer way that can lead to further insights"
`[OXl7IXT7_Cw @ 00:20:17]` — tags: celestial, methodology, nonabelian

**3. Knowing $F$ everywhere in Minkowski space is not a solution of the classical scattering problem.**
He is emphatic that the scattering problem is a map from $A_z$ data on $\mathcal{I}^-$ to $A_z$ data on $\mathcal{I}^+$, and that the field strength alone underdetermines it.
> "the solution of the classical scattering problem ... using the equations of motion to get f is simply not enough so if we have minkowski space and we're given f everywhere in minkowski Space the non-abelian field strength that is not a solution of the scattering problem"
`[OXl7IXT7_Cw @ 00:47:41]`, continuing `[OXl7IXT7_Cw @ 00:48:41]` — tags: large-gauge, nonabelian, charges

**4. Non-abelian theory makes the necessity of the connection visible classically, where the abelian case hides it behind quantum phases.**
A good reason to have done the harder case: colour-singlet-or-not is a classical question, and answering it requires parallel transport around the sphere.
> "in the [a]belian setting ... all it does to [charged excitations] is give them a quantum mechanical phase and you have to do some quantum mechanical experiment to determine if the phases are the same or not ... here already at the classical level in classical non-abelian gauge Theory we certainly know whether something is in a color singlet state or not"
`[OXl7IXT7_Cw @ 00:49:47]`, continuing `[OXl7IXT7_Cw @ 00:50:50]` — tags: large-gauge, nonabelian, memory

**5. Why non-abelian gauge theory is harder in the infrared than either QED or gravity: the interactions do not switch off at long distance.**
This is his physical diagnosis of why the Faddeev-Kulish-type constructions transfer to gravity but not to Yang-Mills, and it is not in the notes.
> "the basic reason ... why non-a[b]elian gauge theories are different from gravity and QED is that the problems that we're talking about here are problems at very long distances ... there's a sense in which in both Quantum electrodynamics and in gravity at very long distances there's no interactions and you have free field Theory the same thing is not true in non-ab[e]lian gauge theories [-] like for example n equals four [Yang]-Mills Theory there are interactions which persist and must be dealt with at arbitrarily long distances"
`[OXl7IXT7_Cw @ 00:58:11]` — tags: ir-divergences, nonabelian, open-problems

**6. What makes a falloff condition the right one: it has to be weak enough to let gravitational waves out.**
Stated as the single most important feature of the BMS definition, and paired with the box analogy in entry 15.
> "the most important feature of this definition is that [it] allows for gravitational waves right it's weak enough so that gravitational waves can pass through null Infinity"
`[OXl7IXT7_Cw @ 01:20:49]` — tags: methodology, asymptotic-symmetries

### Opinions and judgments

**7. "The S-matrix doesn't exist in non-abelian gauge theory" is, in his view, the wrong statement. The right one is that nobody has constructed it.**
A careful correction of received wisdom: no one showed it cannot be defined; the usual tricks just failed.
> "one often hears the phrase the [S-]matri[x] doesn't exist in non-abelian gauge Theory I don't think that statement is correct I think the correct statement is there's been no construction of an S Matrix in non-abelian gauge Theory nobody even really tried to show that there was no way to define an [S] Matrix ... the usual tricks that ... worked in other cases didn't work [in] non-a[b]elian gauge theories"
`[OXl7IXT7_Cw @ 00:53:59]` — tags: ir-divergences, nonabelian, open-problems, methodology

**8. On Faddeev-Kulish: every QFT textbook footnotes it, he doubts the textbook authors read the paper, and he is not persuaded anyone really understands it.**
Delivered as a genuine (and slightly wry) epistemic complaint about a load-bearing citation.
> "there's something called the [Faddeev]-[Kulish] construction which all textbooks [in] Quantum field Theory footnote and I'm not sure that the writers of those textbooks have read the paper but they all footnote this thing ... which I definitely won't go into and don't understand very well myself in fact I'm not persuaded that anybody actually really does understand it"
`[OXl7IXT7_Cw @ 00:55:01]` — tags: ir-divergences, dressing, history, pitfalls

**9. Inclusive cross sections are a perfectly fine tool for the LHC but they have no symmetries — not even energy conservation.**
The sharpest one-line justification for insisting on an S-matrix rather than settling for cutoff cross sections.
> "that's a perfectly fine procedure if your goal is to compute cross sections at the LHC where there is a real physical cut off ... but if you want to understand basic structures about Quantum field Theory ... what are the symmetries of the S Matrix the first thing you need is an S Matrix there are [no] symmetries of inclusive cross-sections or probability amplitudes even energy conservation is not ... a symmetry of those things"
`[OXl7IXT7_Cw @ 00:56:04]`, continuing `[OXl7IXT7_Cw @ 00:57:07]` — tags: ir-divergences, methodology, open-problems

**10. The Kac-Moody level: at this order it is zero, but he says there is a second, poorly understood current algebra hiding in the construction that would carry one.**
He is explicit about the boundary of his knowledge, twice, in response to a persistent student.
> "this is secretly a second current algebra in here which we don't fully understand ... we could bosonize the charge of these things and then take their derivatives ... that would give us a second current and that would have a level ... and then there would be some more complicated set of w[a]rd identities that we don't understand at this point"
> "I'm telling you now what I know to be correct"
`[OXl7IXT7_Cw @ 00:22:54]`, `[OXl7IXT7_Cw @ 00:24:09]` — tags: celestial, nonabelian, open-problems

**11. He does not expect the boundary CFT to be unitary, and says we do not even know whether a level exists or what sign it would have.**
A striking opinion, offered without argument, and absent from the notes.
> "we don't even know if there is a level and we don't know whether to expect it to be positive or negative I don't think there's any reason to expect that the boundary CFT should be unitary"
`[OXl7IXT7_Cw @ 00:27:28]` — tags: celestial, open-problems, nonabelian

**12. Confidence calibration on the magnetic conjecture: unproved, but "there doesn't seem to be much room" for corrections.**
Useful as a record of how strongly he holds it, alongside the contrast with the loop-corrected non-abelian case.
> "the soft [p]hoton theorem has no Loop Corrections it's an exact statement to all orders [in] perturbation Theory and I conjectured that when you add the magnetic stuff then you have non-p[erturbatively] exact formula didn't prove that but there doesn't seem to be much room for correcting that formula"
`[OXl7IXT7_Cw @ 00:26:23]` — tags: soft-theorems, charges, open-problems

**13. The one-loop correction to the soft gluon theorem is called an unsolved problem in this language, with the level as a candidate explanation.**
He explicitly labels everything he presents in this lecture as tree-level.
> "the soft [g]luon theorem does get Corrections at one Loop ... so what I'm doing here is really tree level and it's a very interesting unsolved problem to understand what those loop Corrections mean in this language ... it could be that at the Loop level when Loop Corrections are included there's some kind of level here but this is all unexplored territory"
`[OXl7IXT7_Cw @ 00:26:23]`, continuing `[OXl7IXT7_Cw @ 00:27:28]` — tags: ir-divergences, celestial, open-problems

**14. He does not like Bondi coordinates and uses them anyway, so that he can look formulas up.**
Honest, funny, and a real methodological point: in gravity the formulas get "exponentially longer" and being able to borrow them matters more than coordinate elegance.
> "I don't actually think they're [a] particularly nice set of coordinates ... but then you can't look things up in the literature"
> "when you go to gravity somehow they get exponentially longer and so it's very nice to be able to look up some of those exponentially longer formulas in other people's papers rather than having to work them all out yourself so I'm going to continue in the spirit of the l[ast] half century in using these [Bondi] coordinates"
`[OXl7IXT7_Cw @ 01:07:56]`, `[OXl7IXT7_Cw @ 01:09:01]` — tags: methodology, supertranslations

### Warnings and common confusions

**15. Boundary conditions at $\mathcal{I}$ are not like boundary conditions in a box, and the box intuition actively misleads.**
The Dirichlet-*and*-Neumann example is the warning: over-specify and there are no solutions. But $\mathcal{I}$ is not a reflecting wall at all — radiation boils off and leaves, so you have to know what behaviour to expect rather than choose it.
> "you can't choose dirichlet and Neumann right ... there will be no [s]olutions so you have to do something consistent"
> "at Future null Infinity it's even much more subtle than that ... it's not as if you're reflecting some excitations off of future null Infinity you start somewhere in the middle stuff boils off radiation goes up to null infinity and you have to know what kind of behaviors you would typically get"
`[OXl7IXT7_Cw @ 01:10:06]`, `[OXl7IXT7_Cw @ 01:11:14]` — tags: methodology, pitfalls, asymptotic-symmetries

**16. The whole relativity community had the behaviour at the *edges* of $\mathcal{I}$ wrong from the 1960s until Christodoulou and Klainerman in the 1990s.**
He draws the methodological moral himself: there is no systematic way to decide these boundary conditions — and then hedges that maybe there now is.
> "the whole school of relativity starting from the 60s up until the work of [Christodoulou] and [Klainerman] in the 90s had it wrong in a very important way"
> "the fact that all of these people had it wrong for so many years ... illustrates that there is no really systematic way of deciding what these boundary conditions [are] well maybe there is and maybe [Christodoulou] and [Klainerman] finally solved it"
`[OXl7IXT7_Cw @ 01:11:14]`, `[OXl7IXT7_Cw @ 01:12:15]` — tags: history, pitfalls, methodology, open-problems

**17. The $U=1$ assumption is one that textbooks make silently, and he says so.**
Comparing a red quark at the north pole with a red antiquark at the south pole only makes sense given a flat connection to transport with.
> "I need to emphasize ... something that should be but isn't usually emphasized in textbooks is that we're assuming that the sphere at Infinity has a flat connection on it U equals one"
`[OXl7IXT7_Cw @ 00:16:02]` — tags: large-gauge, nonabelian, pitfalls

**18. And the $U=1$ assumption is already uncomfortable, because soft gluons are precisely what move you between inequivalent flat connections.**
He flags the tension immediately rather than deferring it — this is the seed of colour memory.
> "already here we see that that assumption is a little bit funny because when there's soft gluons around we have to be careful about what that means because when there's soft gluons around ... they characterize transitions from one flat connection to another flat connection"
`[OXl7IXT7_Cw @ 00:17:06]`, continuing `[OXl7IXT7_Cw @ 00:18:10]` — tags: memory, large-gauge, nonabelian, vacuum-degeneracy

**19. How did people study non-abelian gauge theory for half a century without ever stating the matching condition? It is built into the Feynman propagator.**
A direct answer to the obvious objection, and a nice example of a boundary condition hiding inside a computational rule.
> "you might ask how people have gotten away [with] studying non-a[b]elian gauge theories for over half a century without ever saying this well this rule is implicit in Feynman diagrams where all the propagators ... Feynman propagators ... effectively give you things which ... implicitly invoke this boundary condition"
`[OXl7IXT7_Cw @ 00:52:56]` — tags: large-gauge, history, methodology, nonabelian

**20. On the contour: which side is "inside" does not matter, because the full correlator has to be a singlet.**
He anticipates the worry rather than waiting to be asked, and gives the one-line reason.
> "it might have bothered you it's a contour [on] a sphere how do I decide what the inside and the outside is well the point is it doesn't matter because if I were to unrestrict the sum ... that would be zero just by the statement that the whole thing has to be a singlet"
`[OXl7IXT7_Cw @ 00:30:51]` — tags: celestial, ward-identities, nonabelian

**21. Reversing inside and outside picks up residues, i.e. extra soft insertions, and gives a second, equally true relation.**
Note the ASR trap: at this point he says "soft graviton" while discussing gluons.
> "if I redefine what I mean by outside and inside when I try to contract this on the other side I'll run into poles there'll be residues there ... in other words extra soft grav[]iton [sic: gluon] insertions and in that way I will ... get another correct relationship"
`[OXl7IXT7_Cw @ 00:38:13]` — tags: celestial, ward-identities, nonabelian

### Open problems named in passing

**22. A rapid inventory at the end of the gauge-theory half: the magnetic version, the level, the non-commuting mixed double soft limit, and the subleading theorems.**
The mixed double soft limit is the one he singles out as evidence of structure nobody understands.
> "there's also an issue about the double soft limit of a J[-]z and a J[-]z bar and that turns out ... not to commute and that's indicative of some more structure that we haven't fully understood"
`[OXl7IXT7_Cw @ 01:00:16]`, continuing `[OXl7IXT7_Cw @ 01:01:20]` — tags: open-problems, celestial, soft-theorems

**23. The programme's bet for non-abelian theory, stated as a hope: the symmetries might allow an S-matrix, or a suitable replacement, to be defined.**
He is careful with the modality — "the hope would be", "the conjecture would be" — and explicitly limits the present relations to tree level.
> "the hope would be that ... through some kind of understanding of the [s]ymmetry there may be some way to define an S Matrix ... or some generalization of [the] S Matrix ... the relationships that I'm writing down here because of these infrared issues are really only valid in non-a[b]elian Theory at tree level and so the conjecture would be that there's some kind of object ... that relations like this apply to"
`[OXl7IXT7_Cw @ 00:59:12]`, continuing `[OXl7IXT7_Cw @ 01:00:16]` — tags: ir-divergences, open-problems, nonabelian

**24. The Kac-Moody check is set as homework rather than asserted: compute the two-current correlator, take the double soft limit, look for a double pole.**
A small but useful record of what was actually verified versus assumed.
> "it's just [that] you compute [the] correlation function with two J's and you take the doub[le] so[ft] limit and you see if there's a double pole and there isn't"
`[OXl7IXT7_Cw @ 00:25:18]` — tags: celestial, methodology, nonabelian

---

## Structure of the argument (thin skeleton)

- `00:00`–`00:12` Review: celestial notation for in/out states, soft gluon theorem, non-abelian asymptotic expansions, the soft gluon operators $N_z$, $N^-_z$ and the current $J_z$. (Notes §Non-Abelian Gauge Theory.)
- `00:12`–`00:20` Rewriting the soft gluon theorem as a Kac-Moody Ward identity on the celestial sphere. (Notes §$\mathcal{G}$-Kac-Moody Algebra.)
- `00:20`–`00:28` Q&A on the level; loop corrections; the "second current algebra".
- `00:28`–`00:39` The contour integral $J_\mathcal{C}[\varepsilon]$ and its identification as the generator of holomorphic large gauge transformations inside $\mathcal{C}$.
- `00:39`–`00:47` The charge formulation, soft and hard pieces, and an in-class exercise relating the two presentations. (Notes §Conserved Charges.)
- `00:47`–`00:53` Why the classical non-abelian scattering problem needs the matching condition; the Feynman-propagator answer.
- `00:53`–`01:02` The missing S-matrix: what the correct statement is, Faddeev-Kulish, inclusive cross sections, why non-abelian differs from QED and gravity, and the open-problem list.
- `01:02`–`01:22` Gravity begins: Bondi gauge and why he uses it; asymptotic flatness falloffs; the warning about the edges of $\mathcal{I}$. (Notes §Asymptotically Flat Spacetimes.)

---

## Deltas versus the written lectures (arXiv:1703.05448)

1. **The S-matrix commentary is far more opinionated spoken than written.** The notes say plainly that "there is no known unitary $\mathcal{S}$-matrix for quantum non-abelian gauge theories" and call it "an elephant in the room". They do *not* contain: the correction that the common phrasing is wrong and no one tried to prove impossibility (`00:53:59`); the remark that textbook authors may not have read Faddeev-Kulish and that he is not persuaded anyone understands it (`00:55:01`); "people tried ... and it just got too complicated and people gave up" (`00:56:04`); or the line that inclusive cross sections have no symmetries, "even energy conservation is not a symmetry of those things" (`00:57:07`).

2. **The physical diagnosis of *why* non-abelian is worse — persisting long-distance interactions, with $\mathcal{N}=4$ named — is spoken only** (`00:58:11`). The notes attribute the difficulty to the corrected soft theorem and the running coupling, which is a different (and complementary) explanation.

3. **The Kac-Moody level.** The notes mention the mixed double soft ambiguity only in a footnote and never discuss a level. Spoken, there is a whole exchange: the level is zero at this order (`00:21:49`), a "second current algebra ... which we don't fully understand" would carry one (`00:22:54`), the homework check is stated (`00:25:18`), and — the strongest opinion in the lecture — "I don't think there's any reason to expect that the boundary CFT should be unitary" (`00:27:28`).

4. **His ranking of the three formulations** (momentum-space soft theorem / in-out charges / celestial current algebra) as increasingly natural and "can lead to further insights" (`00:20:17`) is a spoken judgement. The notes reorganise around celestial correlators but justify it only as "more efficient".

5. **The Feynman-propagator answer** to "how did anyone get away with this for fifty years" (`00:52:56`) is spoken only; the notes make the corresponding remark for GR, not for gauge theory.

6. **The Bondi-coordinate apology** (`01:07:56`, `01:09:01`). The notes say only that these coordinates are adopted "largely because they are used in most of the literature", with a pointer to harmonic gauge. Spoken adds "I don't actually think they're a particularly nice set of coordinates" and the joke about looking up exponentially longer formulas.

7. **The boundary-condition-at-$\mathcal{I}$ discussion.** The notes say there is "no a priori preferred method" for the falloffs, in one sentence. Spoken (`01:09:01`–`01:12:15`) he gives the Dirichlet-and-Neumann-in-a-box counterexample, explains why $\mathcal{I}$ is *not* a reflecting boundary, and states flatly that the entire field had the edge behaviour wrong for thirty years — with an honest hedge that Christodoulou and Klainerman may have settled it. This is a much stronger historical claim than the notes' footnote.

8. **The colour-memory tension is flagged early and informally** (`00:17:06`, `00:18:10`) as the $U=1$ assumption being "a little bit funny", before the term "colour memory" is introduced. The notes introduce colour memory as a finished concept in §Kac-Moody; the spoken version shows it arriving as a discomfort about an assumption.

9. **The "soft factor is generically an operator" framing** (`00:06:26`) is spoken only. The notes give the operator-valued formula but do not stop to say that the number-valued case is the exception.

10. **Not a delta (checked):** the red-quark/anti-red-quark singlet illustration, the $U=1$ subscript convention, the requirement that $A_z$ be part of the Cauchy data, the antipodal matching condition and its role in defining the scattering problem, the contour-side ambiguity being resolved by the soft theorem, and the Bondi metric and falloff conditions all appear in the notes (lines 2019–2046, 2076–2134, 2154–2199).

---

## Transcript quality notes

- Systematic ASR substitutions: "not a billion"/"non-a billion"/"non-abillion" → non-abelian; "a billion" → abelian; "katsmuti"/"cats moody"/"ketmuri"/"cat's Moody" → Kac-Moody; "scribe plus"/"scry"/"sky"/"square plus"/"Sprite plus"/"scrum minus" → $\mathcal{I}^\pm$ (scri); "fide of coolish"/"day of coolish" → Faddeev-Kulish; "Chris diduler"/"Christ douer"/"chrisad" → Christodoulou; "kleinerman" → Klainerman; "bonding"/"bondy" → Bondi; "Newman and unti" → Newman and Unti; "lorenzian" → Lorentzian; "cork" → quark; "yangmil's"/"young Mills" → Yang-Mills; "X Matrix"/"asymmetrics" → S-matrix.
- `[00:38:13]`: he says "soft graviton insertions" while discussing gluons. Almost certainly a verbal slip rather than ASR, but either way read it as "soft gluon".
- `[00:20:17]`–`[00:25:18]` is a long student exchange on the level where the questions are only partly audible; his answers are self-contained enough to use, but the question he is answering at `[00:21:49]` ("where is that assumption coming [from]") cannot be reconstructed.
- `[01:16:32]`–`[01:18:42]` has him double-checking a power of $r$ live and correcting himself ("I think it's 1 over r squared in a local orthonormal frame"); harmless, but do not treat those numbers as authoritative — the notes' exercise 10 is the reference.
- `[00:17:24]` in the next lecture confirms he corrected an order-of-$r$ error made here at `[01:19:46]`. Worth knowing if cross-referencing the two.
