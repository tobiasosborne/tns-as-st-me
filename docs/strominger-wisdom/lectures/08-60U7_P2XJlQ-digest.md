# Lecture 8 — Superrotation Charges and Ward Identity

- **Video id:** `60U7_P2XJlQ`
- **URL:** https://youtu.be/60U7_P2XJlQ
- **Duration:** 01:35:42
- **Written companion:** arXiv:1703.05448, § Superrotations (`refs/arxiv-1703.05448/soft_Arxiv_update.tex` lines 2407–2582)
- **Source status:** secondary. Auto-captions, ASR noise throughout. Not L3 ground truth.

**Scope note (per the orchestrator's steering).** This digest deliberately does *not*
restate the derivations that are already in the written lectures. It harvests the
side channel: opinions, warnings, hesitations, historical asides, answers to
audience questions, and remarks about what is deep versus what is bookkeeping.

**Arc.** Superrotations, presented as a live and unfinished subject rather than a
settled one. The lecture has a distinctive tone: where lecture 7 argued with the
past, this one negotiates with the present. Strominger drops the orthonormal-frame
restriction, recovers the holomorphy condition that BMS used to *discard* the extra
vector fields and that Belavin–Polyakov–Zamolodchikov used to *keep* them, and then
spends several minutes on what he thinks the honest justification for keeping them
is. He tells the discovery history as personal archaeology — Barnich–Troessaert,
then a Banks footnote, then de Boer–Solodukhin, then obscure Penrose notes — makes a
dated prediction about the central charge, admits a $1/r$-expansion problem he does
not know how to solve, fumbles a boost-charge formula live, and closes with a list
of things about the celestial CFT that are "a blank slate". The final Q&A has him
retracting a guess in real time.

---

## Insights

### The criterion: when does a conjectured symmetry earn the name?

**1. He gives his own answer to why 2d CFT is allowed to keep meromorphic vector fields, and it is a pragmatic one: because the resulting Ward identities give checkable relations among correlators.**
He first notes that CFT practitioners each give a different answer, that a common one ("who cares about singularities outside the patch") does not fully convince him, and then supplies his own. "It's good for something" is the operative standard.
> "if you ask people who[se] life's work is two-dimensional conformal field Theory ... they'll all give ... different answer[s] ... one of the answers you might hear a lot is if we're only studying physics in some local region why do we care if there's singularities in our symmetry Transformations somewhere else well there might be a reason that we would care I don't know"
> "the reason it's interesting why we should do it is because we use it we d[e]rive identities that relate some correlation functions to other correlation functions and we know we can show algorithmically that those identities are correct identities ... that would be my sort of practical view of it that it's good for something"
`[60U7_P2XJlQ @ 00:31:19]`, `[60U7_P2XJlQ @ 00:32:22]` — tags: celestial, methodology, superrotations

**2. Applied to superrotations, the criterion becomes: there had better be a new soft theorem, or the symmetry claim does not stand.**
He states this as the plan of attack before deriving anything, and the whole lecture is built to satisfy it.
> "we still didn't know the answer to the question of whether or not these things should be allowed and the way I'm going to propose ... the question should be answered is we need to have some concrete relationship between s Matrix element[s] in other words there better be some new soft theorem that this is related to"
`[60U7_P2XJlQ @ 00:39:55]` — tags: methodology, superrotations, soft-theorems, open-problems

**3. Self-assessment of what is genuinely new: the QED chapters restated known physics in a new language; this one predicts something.**
An unusually clear statement of where he thinks the programme crosses from reformulation into discovery.
> "so this is an example where now we're really starting to learn something new when we were talking about QED we were saying things everybody knew in a new language but now we ... [had] a conjectured symmetry of gravity if that symmetry were really to be a good symmetry there would have to be a soft theorem this is the soft [theorem] that it would have to be and then you can check diagrammatically"
`[60U7_P2XJlQ @ 01:15:41]` — tags: methodology, superrotations, soft-theorems, history

**4. The subleading soft factor was guessed, not derived — and he says why deriving it directly would have been confusing.**
Same method as in lecture 5 (guess the charge, then verify), applied here at the level of the soft factor. The reason given is concrete: going straight to momentum space produces terms you cannot tell should cancel.
> "if you just start from this expression and try to go into momentum space you're going to get all kinds of terms and you're going to be confused about what should and shouldn't cancel ... the way it actually worked was this formula was ... kind of guessed based on the combination of ... this argument about angular momentum flux ... and the fact that this seems to be the unique formula that ... vanishes for ... Pure gauge gravitons and then once you know what to look for it becomes much easier to show that these statements are equivalent"
`[60U7_P2XJlQ @ 01:24:25]`, setup at `[60U7_P2XJlQ @ 01:23:20]` — tags: methodology, soft-theorems, superrotations

**5. A one-line reply to "it's only a diffeomorphism": the charges are non-zero, conserved, and coordinate-invariant, so something coordinate-invariant is changing.**
Compact, and reusable whenever someone objects that asymptotic symmetries are gauge.
> "just the fact that the charges are non-zero and conserved means that these are not trivial these charges are coordinate [in]variant[s] so something coordinate invariant is changing under these ... super translations"
`[60U7_P2XJlQ @ 00:13:09]` — tags: supertranslations, charges, methodology, pitfalls

### History, attribution and personal archaeology

**6. The discovery order is told as a sequence of things he found out after the fact, not as a tidy citation list.**
Barnich and Troessaert first; then a Tom Banks footnote in a paper about something else, two to four years earlier; then de Boer and Solodukhin coming at it from Minkowski holography; then obscure Penrose material including the twistor newsletter. The moral he draws is that the idea had been "floating around ... in various forms".
> "I first learned about this conjecture in some papers of [Barnich] and [Troessaert] about five years ago"
> "then I discovered that there was a footnote in a paper by Tom Banks about two [to] four years earlier ... [a] paper on something completely different in which he clearly made the statement that one should allow all the conformal killing vectors"
> "then I realized that actually there's some obscure papers by Penrose and including in his twist[o]r newsletter that he actually knew a lot of this also so it's an idea which has been sort of floating around there in various forms"
`[60U7_P2XJlQ @ 00:35:42]`, `[60U7_P2XJlQ @ 00:37:47]`, `[60U7_P2XJlQ @ 00:38:51]` — tags: history, superrotations, celestial

**7. Candid on readability: he did not assign the Barnich–Troessaert papers because they are long, formula-heavy and hard to read — while insisting they are important.**
A small, honest remark about the gap between a paper's importance and its usability.
> "they have some very long papers which is why I didn't assign any of them they're important papers but they're long ones and they have a lot of formulas and they're not ... easy to read"
`[60U7_P2XJlQ @ 00:35:42]`, echoed at `[60U7_P2XJlQ @ 00:36:44]` — tags: history, methodology

**8. A dated bet: the central charge is clearly there, its definition and normalisation have not been worked out, and he expects that to be done "within the next year".**
Worth recording precisely because it is falsifiable and time-stamped. He also notes how thin the literature was at the time.
> "another interesting thing about this super rotation group is that there have been very few [p]apers written on it and there clearly is a central charge as you'll see in a minute but exactly how it's defined and what the proper normalization is ... hasn't been worked out yet but I'm pretty sure that will happen ... within the next year or something like that"
`[60U7_P2XJlQ @ 00:36:44]` — tags: celestial, superrotations, open-problems, history

**9. The same holomorphy equation was written down twice, twenty years apart, and the two communities drew opposite conclusions from it.**
BMS discarded the extra vector fields because $\partial_{\bar z}Y^z$ fails to vanish at isolated points; BPZ kept them. He tells it as a genuine fork in the road rather than as an obvious choice.
> "this same equation was encountered 20 years later by [Belavin] and [Polyakov] and [Zamolodchikov] ... when they were developing the theory of two-dimensional conformal field Theory"
> "when BMS saw this they said okay we're throwing out all these guys we're just going to keep these six ... [when] BPZ saw it they said let's keep the whole thing"
`[60U7_P2XJlQ @ 00:29:12]`, `[60U7_P2XJlQ @ 00:30:14]` — tags: history, superrotations, celestial

### Open problems he admits to not understanding

**10. The $1/r$-expansion integration constants: he does not know whether new ones appear at every order, suspects not, and knows of nowhere the problem is written down — "even in electromagnetism I'm not sure how it works".**
This is the most explicit "I don't know and neither does anyone else" moment in the four lectures, and it concerns exactly the data-specification question that lecture 7 called the point everybody would have missed.
> "interestingly I'm not completely clear if it's ... understood I know that I don't understand exactly what the situation is at higher orders and if you want to be able to solve to all orders in the one over R expansion if you get new integration constants at every order or ... I suspect not I suspect that it stops [at] some order but I don't actually know how it works or know of anywhere that that problem has been spelled out in fact even [in] electromagnetism I'm not sure how it works"
`[60U7_P2XJlQ @ 01:01:37]`, context at `[60U7_P2XJlQ @ 01:00:32]` — tags: open-problems, charges, superrotations, methodology

**11. The linear-in-$u$ divergence of subleading data is "ubiquitous", and he traces it back to the first problem set.**
Third appearance of this phenomenon in the course (see lecture 5 at `01:42:17`). Naming it as a pattern rather than an accident is the spoken contribution.
> "in the first problem set when I had you sol[ve] for box Epsilon equals zero ... one found that the sub leading term necessarily ... had a u Divergence and so this phenomena of sub-leading terms having linear behavior in [u] and diverging at U goes to plus and minus infinity is ... ubiquitous and this is another albeit more complicated example of it"
`[60U7_P2XJlQ @ 00:59:29]` — tags: pitfalls, charges, superrotations

**12. One-loop corrections: he lists three possible readings and endorses none.**
Anomaly in the symmetry? Loop-corrected transformation laws? Or an unexplored subject? He also hedges the word "corrections" itself, since people set the calculations up differently.
> "it's ... known [is] maybe too strong a word because people set up their calculations in a different way but there seem to be Corrections at one Loop and only at one Loop and we don't understand what that means whether it's an anomaly in the [s]ymmetry or it means one has to make Loop corrections to the transformation laws or it's just a subject which hasn't been explored"
`[60U7_P2XJlQ @ 01:26:32]` — tags: ir-divergences, superrotations, open-problems

**13. Low's 1958 subleading soft theorem in abelian gauge theory is tied to "some symmetry that we don't really understand very well".**
A reminder that the older corner of this story is not in better shape than the new one.
> "there's also a sub leading s[o]f[t] theorem [in] gauge Theory in a[be]lian gauge Theory which was discovered in 1958 and it's related to some symmetry that we don't really understand very well"
`[60U7_P2XJlQ @ 01:24:25]` — tags: history, soft-theorems, open-problems, large-gauge

**14. The celestial stress tensor had not been constructed. He is confident the problem is solvable and explicitly unsure the answer will be useful.**
He sketches the whole programme in one breath — build $T$, check the OPE, normalise, read off $c$ — and marks each step as not yet done.
> "I don't think that's been worked out carefully I ... don't think we tried to construct the current I think there is a current but I don't think we tried to"
> "first we have to construct T and that hasn't been done yet ... I'm sure it's a solvable problem it's a different question whether the answer will be useful"
> "this appearance of this term is strongly suggestive that there's some kind of central charge floating around somewhere but in order to say what that is one must first construct T and then show that it ... has the right O[PE] and then normalize it correctly and then get the central charge"
`[60U7_P2XJlQ @ 01:30:47]`, `[60U7_P2XJlQ @ 01:33:01]` — tags: celestial, open-problems, superrotations

**15. A guess retracted live: he starts to say he expects the gravity central charge to work like the gauge theory one, then talks himself out of it.**
The gauge-theory mechanism runs through non-commuting double soft limits, and he is not sure that carries over.
> "I was about to say I'd expect it to be like the gauge Theory but ... in the gauge Theory ... it comes about because double soft limits don't commute and I'm not sure that ... that is true [in] gravity gravity ... has less infrared divergences though it does have this pole"
`[60U7_P2XJlQ @ 01:34:01]`, continuing `[60U7_P2XJlQ @ 01:35:05]` — tags: celestial, nonabelian, open-problems, superrotations

**16. The closing position: cautious. Tree level plus one-loop corrections of unknown form; the representation theory is "a blank slate".**
He wants the 2d-CFT analogy to be powerful and says so, then immediately lists what is unknown: which representations, highest or lowest weight, what norm.
> "it appears that four-dimensional quantum gravity ... at least at tree level and with some one Loop Corrections whose form we don't understand has the transformation laws of a two-dimensional conformal field Theory"
> "but we should not expect ... I think it won't be the same story we don't know exactly what kind of representations are appearing we don't know highest weight lowest weight we don't know what sort of [n]orm we should be using it's all sort of a blank slate at this point"
`[60U7_P2XJlQ @ 01:27:35]`, `[60U7_P2XJlQ @ 01:28:38]` — tags: celestial, open-problems, superrotations

### Method, bookkeeping and honest fumbles

**17. Bookkeeping honesty: the $4/3$ and the $C^2$ shift in the angular momentum aspect "look kind of funny" and exist only to simplify later formulas.**
A small but useful signal about which parts of a definition carry physics and which carry convenience — conventions differ across the literature.
> "there are various different conventions in the literature ... this four-thirds looks kind of funny but it makes ... some subsequent [formulas simpler] and this shift by this quadratic term in C also looks kind of funny but it makes some of the subsequent formula[s] simpler"
`[60U7_P2XJlQ @ 00:03:09]` — tags: superrotations, methodology, pitfalls

**18. The route he did *not* take, and why: matching classically is harder because you are subtracting a finite piece off a $u$-divergence and the ambiguities have to be controlled.**
He explains a methodological choice explicitly, which is more useful than the choice itself.
> "I might have proceeded a little differently in this discussion ... I might have said okay [i]n classical GR this should be ant[ipodally] matched and therefore we have a conservation law ... but that's a little harder to do because ... it's a finite piece that you're subtracting out [of] some [u] Divergence and you have to worry about various kinds of ambiguities so probably could have been set up that way but instead what I did is ..."
`[60U7_P2XJlQ @ 01:07:02]` — tags: methodology, charges, superrotations

**19. A live fumble on the boost charge, handled honestly: he tries to reconstruct $p_i t - E x_i$, gets tangled, and declines to fix it on the board.**
Worth flagging both as a transcript-reliability note and as a small window on which formulas are memorised and which are not.
> "this must be the non-rela[tivistic] version of it ... wait this isn't quite right all right let me not try to sort that out in real time but it's something ... the Boost charge is something like that"
`[60U7_P2XJlQ @ 01:02:40]` — tags: charges, pitfalls

**20. On the news–$C$ commutator: it is derived, not assumed — and "what else could it be" is offered as supporting evidence.**
He also gives the free-field-on-a-null-surface intuition and the antisymmetry argument, in response to a student pressing on whether it was assumed.
> "but this isn't an assumption this is derived in any ... number of papers and there's also what else could it be"
`[60U7_P2XJlQ @ 00:55:07]`, with the free-field argument at `[60U7_P2XJlQ @ 00:52:00]` — tags: methodology, charges, superrotations

**21. A geometric picture for why the orthonormal-frame condition excludes boosts: the boost vector field grows towards the ends of $\mathcal{I}$ even though it fixes the light cone of the origin.**
The written notes state the falloff condition and note that it eliminates boosts and rotations; the picture of *how* they blow up is spoken.
> "the action of a boost ... [on] s[c]ri Plus is a vector field which goes like this and gets bigger and bigger as you go to U equals plus infinity"
> "the Boost[s] map the hyperboloids to themselves ... and it leaves fixed the light cone of the origin so this point doesn't get moved but nevertheless it does become singular at Infinity"
`[60U7_P2XJlQ @ 00:23:47]`, `[60U7_P2XJlQ @ 00:24:50]` — tags: superrotations, asymptotic-symmetries

**22. Orienting analogy stated plainly: $N_z$ is to angular momentum what $m_B$ is to energy and momentum.**
Simple, and it is the sentence that makes the whole superrotation construction feel inevitable.
> "roughly speaking the standard ADM formula for ang[ular] momentum involves this N[-]Z in the same way that the ADM formula for the energy ... [involves the Bondi mass]"
`[60U7_P2XJlQ @ 00:04:13]` — tags: charges, superrotations

**23. Why the subleading soft factor is finite where the leading one has a pole: there is a $q$ upstairs as well as downstairs.**
Also the interpretive point — the rotation is about the axis through which the particle emerges — stated as intuition ahead of the precise geodesic argument.
> "one important thing about this s[o]f[t] factor is now notice ... that we have a Q on the top and a Q on the bottom so ... as we take omega to zero this remains finite"
> "we're generating a rotation around the axis which the particle is emerging through"
`[60U7_P2XJlQ @ 01:16:49]`, `[60U7_P2XJlQ @ 01:17:54]` — tags: soft-theorems, superrotations

---

## Structure of the argument (thin skeleton)

- `00:00`–`00:09` The next order in $1/r$: the angular momentum aspect $N_z$, its constraint equation, and $T_{uz}$ as a momentum density. (Notes §Superrotations / Conserved Charges.)
- `00:09`–`00:17` Recap of supertranslations, why they are not trivial diffeomorphisms, and the Weinberg soft graviton theorem as their Ward identity. (Notes §Supertranslations.)
- `00:17`–`00:28` Dropping the orthonormal-frame restriction; the Lorentz vector fields $\zeta_Y$; the holomorphy condition $\mathcal{L}_Y g_{zz}\propto \partial_{\bar z}Y^z$. (Notes §Symmetries.)
- `00:28`–`00:35` BMS versus BPZ on meromorphic $Y^z$; his own justification for keeping them.
- `00:35`–`00:40` Attribution history and the plan: superrotations earn their name only via a new soft theorem.
- `00:40`–`00:55` Transformation laws for $C_{zz}$ and $N_{zz}$; the stress-tensor form at $u=0$; constructing $Q_Y^+$ hard and soft pieces from the required commutators. (Notes §Canonical Formalism.)
- `00:55`–`01:07` Finiteness of the charge at $\mathcal{I}^+_-$; the $u$-divergence and the leftover integration constant; the open $1/r$ question; the boost-charge fumble.
- `01:07`–`01:24` The Ward identity, the subleading soft theorem, and the pure-gauge-graviton consistency check. (Notes §Subleading Soft Theorem.)
- `01:24`–`01:35` Loop corrections, the closing assessment, and Q&A on constructing the celestial stress tensor.

---

## Deltas versus the written lectures (arXiv:1703.05448)

1. **The attribution history is told as personal discovery, in the order he learned things** (`00:35:42`, `00:37:47`, `00:38:51`). The notes cite Penrose, de Boer–Solodukhin, Banks and Barnich–Troessaert in a tidy logical order (lines 2439–2442) with no indication of who found what when, or in what sequence he came across them. The spoken version also records that Penrose material sat in the *twistor newsletter*, which the notes do not mention.

2. **The dated prediction about the central charge** (`00:36:44`): normalisation "hasn't been worked out yet but I'm pretty sure that will happen ... within the next year". Nothing like this appears in the notes. It is the clearest example of a "what he'd bet on" statement in the four lectures.

3. **The admitted $1/r$-expansion gap** (`01:01:37`) is spoken only and is substantial: whether new integration constants appear at every order is unknown to him, he suspects not, he knows of no place the problem is written down, and he adds that he is unsure even in electromagnetism. The notes mention only that "at higher orders in $1/r$, more data are needed, including $N_z|_{\mathcal{I}^+_-}$", with no admission of uncertainty.

4. **His operational criterion for admitting a symmetry** (`00:32:22`). The notes list two justifications used in 2d CFT ("One is... Another is...") in neutral voice. Spoken, he says CFT practitioners disagree, that the local-patch answer does not fully convince him ("there might be a reason that we would care I don't know"), and that his own view is practical: it is good because it is good for something. That epistemic stance is the delta.

5. **The self-assessment that QED was old physics in new language and superrotations are where something new begins** (`01:15:41`) is spoken only, and it is the clearest signal in the course about where he thinks the real content is.

6. **The three candidate readings of the one-loop corrections** (`01:26:32`) — anomaly, corrected transformation laws, or simply unexplored — with none endorsed. The notes' footnote takes a position ("these one-loop corrections deform rather than eliminate the conserved charges"); spoken he declines to.

7. **The closing list of unknowns about the celestial CFT** (`01:28:38`): representations, highest versus lowest weight, the norm, "a blank slate". The notes are more optimistic in tone and mention the principal series in a footnote; the spoken version is more openly unfinished.

8. **The whole final Q&A on constructing $T$** (`01:29:39`–`01:35:05`) has no counterpart in the notes, which simply cite the later Kapec et al. and Cheung et al. constructions as accomplished (line 2577). The spoken record catches the moment before that: the current not attempted, the OPE-then-normalise-then-read-off-$c$ programme sketched, "I'm sure it's a solvable problem it's a different question whether the answer will be useful", and the retracted guess about non-commuting double soft limits.

9. **The route not taken** (`01:07:02`) — why he did not set the derivation up as classical antipodal matching — is spoken only, and the reason given (subtracting a finite piece off a $u$-divergence, with attendant ambiguities) is a real technical warning.

10. **The linear-in-$u$ divergence called "ubiquitous" and tied back to problem set 1** (`00:59:29`). The notes handle the divergence locally in the superrotation charge and do not present it as a recurring pattern across the course.

11. **The boost picture** (`00:23:47`, `00:24:50`) and the **boost-charge fumble** (`01:02:40`) are both spoken-only, the first as useful intuition, the second as a candour signal.

12. **Bookkeeping honesty about the $4/3$ and $C^2$ conventions** (`00:03:09`). The notes say only "Our definition here of this term is shifted relative to some of the literature to simplify some formulas below" — the spoken "looks kind of funny" is warmer but carries the same information; a mild emphasis delta at most.

13. **Not a delta (checked):** the holomorphy condition and its BMS-versus-BPZ reading; $Y^z=1,z,z^2$ giving the six global conformal Killing vectors; $\delta_Y C_{zz}$, $\delta_Y N_{zz}$ and the Schwarzian linearisation at $u=0$; the news–$C$ commutator; the split of $Q_Y^+$ into hard and soft; the subleading soft factor $S^{(1)-}$ and the $(1+\omega\partial_\omega)$ projector; the pure-gauge-graviton consistency check; "angular momentum is to superrotations as energy-momentum is to supertranslations"; the remark that the formula was guessed before it was derived; the semidirect product and the angular momentum "problem" being a feature — all appear in the notes (lines 2409–2578).

---

## Transcript quality notes

- Systematic ASR substitutions: "super rotation[s]" is usually fine but "super transation[s]"/"super trans[l]ations" varies; "s[c]ri"/"scry"/"scribe"/"Sprite" → $\mathcal{I}$; "bonding"/"bondy" → Bondi; "versaro"/"varosaur"/"varosaurus" → Virasoro; "belove and polyakov and Sam logikov" → Belavin, Polyakov and Zamolodchikov; "barnic and true seret"/"barnacan trusart"/"Barnett contrassar"/"barnac" → Barnich and Troessaert; "Deborah and saludkin" → de Boer and Solodukhin; "vial tensor" → Weyl tensor; "Cur" → Kerr; "Felicity" → helicity; "simplectic" → symplectic; "lead/leader derivative" → Lie derivative; "cachazo" is correct; "twister newsletter" → twistor newsletter; "solve theorem" → soft theorem; "a billion" → abelian.
- `[01:02:40]` contains the live boost-charge fumble. Do not take the formula on that line as correct; he abandons it himself.
- `[01:29:39]`–`[01:35:05]` is the closing Q&A with a student named in the transcript as "Shu Hong". The questions are only partly audible and one is transcribed as "long singular turn in the j-o-oop", which is almost certainly "leading singular term in the $T\mathcal{O}$ OPE". His answers are coherent enough to quote; the questions mostly are not.
- `[00:19:31]` the superrotation vector field $\zeta_Y$ is dictated across two turns with several self-corrections; use the notes (line 2448) rather than the transcript for the formula.
- `[00:36:44]` "yes tarek of course this is a very thorough algebra right" is a fragment of an inaudible student exchange spliced into the middle of a sentence; ignore it.
