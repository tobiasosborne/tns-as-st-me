# Lecture 5 — Infinite-Dimensional Fermionic Symmetry in Supersymmetric Gauge Theory

- **Video id:** `WxCY-K-Jb4A`
- **URL:** https://youtu.be/WxCY-K-Jb4A
- **Duration:** 01:44:20
- **Written companion:** arXiv:1703.05448, §§ Massive QED / Magnetic Charges / Supersymmetry / SSB (`refs/arxiv-1703.05448/soft_Arxiv_update.tex` lines 1239–1767)
- **Source status:** secondary. Auto-captions, ASR noise throughout. Not L3 ground truth.

**Scope note (per the orchestrator's steering).** This digest deliberately does *not*
restate the derivations that are already in the written lectures. It harvests the
side channel: opinions, warnings, hesitations, historical asides, answers to
audience questions, and remarks about what is deep versus what is bookkeeping.

**Arc.** The first third is review-plus-commentary: massive charges and hyperbolic
slices, then magnetic charges, then a long and unusually candid digression on what
"spontaneous symmetry breaking" and "Goldstone boson" actually mean here and how
the large-gauge case differs from the Mexican-hat case. The last two thirds set up
the soft photino theorem, and Strominger spends most of that time not deriving it
but arguing — before writing anything down — that the associated symmetry *cannot*
be a subgroup of supersymmetry, and explaining how one actually goes looking for
such a symmetry in practice. He runs out of time at the point where a technical
wrinkle (linear-in-$u$ divergence of the photino components at $\mathcal{I}$) would
have to be dealt with.

---

## Insights

### Framing and "how to think about it"

**1. The massive-particle problem does not merely permit hyperbolic slices — it pushes you into them, and that pressure recurs for the rest of the course.**
The written notes say the hyperbolic slicing is convenient and "essentially forces one" to it. Spoken, he flags it as a structural signal about which foliation the infrared actually cares about.
> "understanding how this whole structure of soft theorems in the case of massive particles is very natural and kind of forces you into thinking about minkowski space and hyperbolic slices rather than in the usual minkowski T equals constant slices that we usually use ... that's going to be a recurring theme"
`[WxCY-K-Jb4A @ 00:07:32]` — tags: methodology, soft-theorems, asymptotic-symmetries

**2. The massive Ward identity does not look like Weinberg's theorem when you first write it down. Recognition is the hard part, not the derivation.**
Useful expectation-setting: a correct symmetry statement can be unrecognizable as the known soft theorem until a lot of algebra has been done.
> "so now we can write down a[] ward identity which when you first write it down looks nothing like the usual Ward identity ... looks nothing like the Weinberg soft theorem for massive particles but indeed after enough work one can show that this indeed reduces to the standard"
`[WxCY-K-Jb4A @ 00:04:18]` — tags: ward-identities, soft-theorems, pitfalls

**3. A soft theorem is properly read as a linear relation between S-matrix elements, and the fact that the soft momentum can go to zero in any direction is what turns one relation into infinitely many.**
This is his compressed answer to "why should a soft theorem be a symmetry at all?", and the direction-counting is the whole reason the symmetry group is infinite-dimensional.
> "soft theorems are properly interpreted they are linear relationships among s Matrix elements they relate one kind of scattering amplitude to another and so they're symmetries of the theory and moreover ... you can take that momentum to zero in any direction you get not just one symmetry but you get an infinit[y of] symmetries"
`[WxCY-K-Jb4A @ 00:56:09]` — tags: soft-theorems, asymptotic-symmetries, ward-identities, methodology

**4. Counting settles the question before any computation: an infinite family cannot sit inside a four-parameter one.**
He makes a point of establishing that the fermionic symmetries must be new *before* writing a single formula. It is a nice illustration of using a cheap invariant to fix what the answer has to look like.
> "there [is] no way to have an Infinity of symmetries as a subgroup of a finite number of symmetries ... before we even start writing anything down it's clear they're going to be there there's no way that they can be a subgroup of supersymmetry they must be something completely new"
`[WxCY-K-Jb4A @ 00:58:15]` — tags: susy, asymptotic-symmetries, methodology, nonabelian

**5. Research method, stated explicitly: brute force does not work; guess the charge from the shape of the soft theorem, then verify conservation and the Ward identity.**
This is the clearest statement in these four lectures of how the results were actually obtained, and it is absent from the written notes.
> "there would be the brute force method which never works in almost any problem of trying to take this thing and just rewriting it in some way as some set of charges ... a better approach is to just kind of look at this formula and try to guess what the symmetries might be write down some charges and then after you've done that verify that the charges are conserved and that their Ward identity is this s[o]ft theorem that's a more practical approach"
`[WxCY-K-Jb4A @ 01:30:32]`, continuing `[WxCY-K-Jb4A @ 01:31:35]` — tags: methodology, open-problems

**6. Deep versus bookkeeping: soft theorems are universal, off-shell formalisms are not, so there is no reason the symmetry should look simple in any particular superfield language.**
A clean criterion for deciding when an ugly formula is a fact about the physics and when it is a fact about your conventions.
> "there are many ways of writing off shell super multiplets and it's a somewhat random procedure ... the offshe[ll] formalism is not Universal the soft theorems are Universal but the offshe[ll] formalism isn't so there's no guarantee that these are going to be the simplest possible thing"
`[WxCY-K-Jb4A @ 01:25:12]` — tags: susy, methodology, pitfalls

**7. Where the fermionic operator "lives": among the superspace objects that trail alongside the supercharge without being it.**
An intuition about the algebraic home of the new operator, offered as orientation rather than derivation.
> "in various super space formalisms ... there's certain combinations of theta derivatives in super space that are the supercharge and then there's some others that just kind of Trail along in the discussion and are not the supercharge this is related to one of those others that isn't quite supersymmetry"
`[WxCY-K-Jb4A @ 01:16:24]` — tags: susy, charges

### Opinions and judgments

**8. The magnetic soft factor is offered explicitly as a conjecture, with an open invitation attached: nobody has looked at it in duality-symmetric theories.**
The notes state the conjecture; spoken, he adds what he would like someone to do with it.
> "which I would conjecture is a non-perturbatively exact formula for the soft factor in the presence of electric and magnetic charges ... I think this should be interesting to investigate this formula in the context of theories that do have Duality symmetries because then it has to transform into itself in some interesting way but nobody's worked that [out] now"
`[WxCY-K-Jb4A @ 00:14:59]` — tags: soft-theorems, charges, open-problems

**9. He is not confident in the name "asymptotic symmetry" for these objects, and says so.**
The terminology is chosen because the symmetries act naturally on the asymptotic Hilbert space, not because it is obviously right.
> "I think I'm still going to call this sort of a new phenomena so I don't know what the right word is but I think I'm still going to call these things asymptotic symmetries because ... they['re] most naturally characterized in terms of their action on the Hilbert space ... described in the asymptotic region at null Infinity"
`[WxCY-K-Jb4A @ 00:18:08]` — tags: asymptotic-symmetries, methodology

**10. The classification problem is open and he says he does not know what to do about it.**
There are evidently many physical symmetries around; no one has a method for finding them all.
> "so this kind of leaves us not knowing exactly what to do there seem[] to be a lot of symmetries around that have important physical consequences and how do we find and characterize all of them ... that is an open question"
`[WxCY-K-Jb4A @ 00:19:13]` — tags: open-problems, asymptotic-symmetries

**11. He speculates that a bigger theory with extra auxiliary fields might make everything manifest — but the lesson he draws is the negative one.**
Given a theory as handed to you, some of its real symmetries may simply not be visible as local symmetries.
> "it may well be possible to introduce more auxiliary fields and write down some bigger Theory with more degrees of freedom that can get constrained away that has all these symmetries but ... the lesson[] we learn is if somebody hands you a theory ... it might not be possible to find all of these"
`[WxCY-K-Jb4A @ 00:17:05]`, continuing `[WxCY-K-Jb4A @ 00:18:08]` — tags: large-gauge, asymptotic-symmetries, open-problems

**12. Detector limitations are not an argument against wanting an S-matrix, and he will not accept that unitarity stops above the soft sector.**
Answering a student who suggested detectors cannot resolve the soft partner processes. The second half is a strong statement of principle.
> "it may be true that physical detectors can't ... but I would not jump from that statement to the statement that it's not interesting to try to have an S Matrix"
> "we can't have symmetries without an S Matrix I mean the Symmetry is a symmetry of an S Matrix we assume that there's an exactly unitary Theory including the soft sector and I think it's very problematic to assume that unitarity does not extend all the way down to the soft sector"
`[WxCY-K-Jb4A @ 01:27:18]`, `[WxCY-K-Jb4A @ 01:28:23]` — tags: ir-divergences, methodology, open-problems

**13. The stated hope for the whole programme: fifty years of infrared work proceeded without knowing the symmetries that govern precisely that sector.**
Offered as a hope, not a claim. This is the closest thing to a mission statement in these lectures.
> "one of my hopes about this program is that ... now we have found that there are infinite numbers of symmetries that govern the infrared behavior of the theory and these were never used in trying to understand or characterize the S Matrix and that perhaps it can shed light on this problem"
`[WxCY-K-Jb4A @ 01:27:18]` — tags: ir-divergences, history, open-problems

**14. Duality here is a change of variables used to dodge a nasty calculation, not a claimed symmetry of the theory.**
He is careful to separate the computational trick from any physical duality assumption, and says what the direct calculation would have cost.
> "it would be kind of a nasty calculation because the vector potential ... isn't globally defined ... rather than do that we used a trick of just analyzing it [in] terms of these different variables it's a field redefinition not a symmetry of the theory"
`[WxCY-K-Jb4A @ 00:11:50]` — tags: charges, methodology

### Warnings and common confusions

**15. Goldstone pedantry with a point: strictly it is the *zero mode* that transforms inhomogeneously, and calling the whole field the Goldstone boson has caused real confusion.**
He is explicit that he is being pedantic, and equally explicit about why it matters once several fields transform and their zero modes get identified.
> "more precise language which people don't use is to say that the constant mode ... the zero mode of theta is the Goldstone mode for spontaneous breaking of the symmetry ... but everybody has different reasons for adopting certain terminologies"
> "I think there was a lot of confusion caused by the fact that people call the whole Theta the Goldstone boson"
`[WxCY-K-Jb4A @ 00:28:53]`, `[WxCY-K-Jb4A @ 00:35:26]` — tags: vacuum-degeneracy, pitfalls, methodology

**16. The word "soft" in "soft photons are the Goldstone bosons" is optional, and he keeps it only because listeners follow better — "it's a free world."**
A rare explicit statement that a piece of the standard phrasing is a communication choice rather than a technical distinction.
> "I don't actually need ... if I'm following this terminology I don't really need to add the word soft there because in this example the only thing that transforms inhomogeneously is the zero mode"
> "it's a free world you can say whatever you want"
`[WxCY-K-Jb4A @ 00:34:24]`, `[WxCY-K-Jb4A @ 00:35:26]` — tags: vacuum-degeneracy, methodology, pitfalls

**17. Soft photons are Goldstone bosons of *both* the electric and the magnetic large gauge symmetry.**
Said in passing, and worth noting: the same mode is the Goldstone boson of two separate infinite families.
> "in fact it turns out that the soft photons [a]re the Goldstone bosons of both the electric and the Magnetic large gauge symmetry because they transform under both of them"
`[WxCY-K-Jb4A @ 00:36:29]` — tags: vacuum-degeneracy, large-gauge, charges

**18. What was actually proved is a symmetry of the S-matrix, not of the Lagrangian, and he flags the gap rather than papering over it.**
Lagrangian-level statements would require a long argument about surface terms on which people disagree.
> "we didn't show it was a symmetry of the lagrangian because you would have to have a long discussion about ... boundary terms ... we showed it was a symmetry [of] the S Matrix which ... doesn't necessarily go the other way around because people have different ideas about lagrangians as far as what the surface terms are"
`[WxCY-K-Jb4A @ 00:30:02]` — tags: methodology, ward-identities, charges

**19. Superselection sectors are the hinge: with them you get no useful Ward identities, without them you do.**
This is the sharpest statement of *why* the absence of superselection sectors matters for the whole programme, and the written notes do not put it this way.
> "when you have super selection sectors you don't get interesting Ward identities in the same way"
> "you can't really write down Ward identities for spontaneously broken symmetries with super selection sectors but here we don't have the super selection sectors it only takes a finite amount of energy to go from one vacuum to the other"
`[WxCY-K-Jb4A @ 00:42:47]`, `[WxCY-K-Jb4A @ 00:43:50]` — tags: ward-identities, vacuum-degeneracy, asymptotic-symmetries

**20. "Untethered" — the physical reason vacuum change is cheap here is that the angles are not tied to one another, which makes the problem behave like 1+1 dimensions.**
He returns to this three times. The global Mexican-hat symmetry has to be moved everywhere at once; the large gauge parameter can have compact support in one patch of the sphere.
> "it's a symmetry at every angle the different angles are not tied together and that makes it like the one plus one dimensional problem"
> "it's untethered these symmetry Transformations the point[s] on the sphere ... at n[ull] Infinity are not Tethered to one another and so ... [it] doesn't cost energy in the same way"
`[WxCY-K-Jb4A @ 00:41:44]`, `[WxCY-K-Jb4A @ 00:52:52]`, background at `[WxCY-K-Jb4A @ 00:51:50]` — tags: vacuum-degeneracy, memory, asymptotic-symmetries

**21. Honest gap: the norm of the state created by the charge has not been defined, and he says so twice.**
He suspects a definition exists, but declines to assert it. He is nevertheless confident about the conclusion that matters (no superselection sectors).
> "I don't think the norm has been fully defined ... there['re] tricky issues about limits and so on ... I suspect there is a way to define it ... but we certainly wouldn't want to conclude that there are super selection sectors"
`[WxCY-K-Jb4A @ 00:48:34]`, `[WxCY-K-Jb4A @ 00:49:42]` — tags: vacuum-degeneracy, open-problems, pitfalls

**22. Answer to a student's tunnelling analogy: these are transitions in *space* along the slice on which the Hilbert space is defined, not transitions in time.**
A useful correction to a natural mental picture — the analogy the student was reaching for does not apply.
> "we're thinking of this as the slice on which we define our Hilbert space not as time ... in the analogy that you're trying to draw these would be transitions in space"
`[WxCY-K-Jb4A @ 00:46:14]` — tags: vacuum-degeneracy, pitfalls

**23. The degenerate photon vacua have the same energy but different angular momentum — that is another way to see that they are genuinely different states.**
The written notes make the angular-momentum-labels-vacua argument in the gravitational setting; here he applies it to soft photons.
> "the different degenerate vacua with different number of s[o]f[t] photons they have the same energy but they have different angular momentum which is another way of understanding why they're different"
`[WxCY-K-Jb4A @ 01:29:28]` — tags: vacuum-degeneracy, charges

**24. The photino charge has a wrinkle he almost walked into: the field components diverge linearly in $u$ at the edges of $\mathcal{I}$, and a delicate projection is needed.**
He says out loud that the obvious guess looks like a five-minute job, then flags the trap. He also connects it to the homework, marking it as a recurring phenomenon rather than a one-off.
> "actually it seems like it would be so easy that I could do it in the next five minutes and then that would be the obvious guess ... but there's a wrinkle"
> "the field equations imply that the components of Lambda ... actually diverge as [you approach] s[c]ri plus minus they can diverge linearly with [u]"
> "we have to do a very subtle projection to get rid of that to get a well-defined quantity ... that's an instructive exercise but it takes half an hour not three minutes"
`[WxCY-K-Jb4A @ 01:41:13]`, `[WxCY-K-Jb4A @ 01:42:17]`, `[WxCY-K-Jb4A @ 01:43:19]` — tags: pitfalls, charges, susy

### History and asides

**25. The magnetic conservation law is entirely classical, and he finds it surprising that it went unnoticed for a century and a half.**
Answering a student who asked whether the magnetic symmetries were a quantum phenomenon.
> "it's a classical formula in both the electric case and in the magnetic case which makes it all the more surprising it could have been discussed 150 years ago or something but nobody looked at it this way for some reason"
`[WxCY-K-Jb4A @ 00:20:18]` — tags: history, charges, large-gauge

**26. A joke with content: in a supersymmetric theory every theorem has a superpartner.**
Used as the motivation for expecting a soft photino theorem at all, before any calculation.
> "in supersymmetric Theory everything ... [h]as a super partner including theorems you have one theorem it's a super transformation of it is [another]"
`[WxCY-K-Jb4A @ 00:55:05]` — tags: susy, soft-theorems, methodology

---

## Structure of the argument (thin skeleton)

- `00:00`–`00:08` Review: extending the gauge parameter inward in Lorenz gauge, hyperbolic slices, massive charges. (Notes §Massive QED.)
- `00:08`–`00:20` Magnetic charges via the duality field redefinition; the corrected soft factor; the second infinity of conserved charges. (Notes §Magnetic Charges.)
- `00:20`–`00:52` Long digression on spontaneous symmetry breaking, Goldstone terminology, and superselection sectors. (Notes §SSB — but see deltas below.)
- `00:52`–`01:06` Setup for the soft photino theorem: the $\mathcal{N}=1$ Lagrangian, the supercurrent coupling, the operator $F$ that maps bosons to fermions at fixed momentum. (Notes §Soft Photino Theorem.)
- `01:06`–`01:26` The soft photino theorem itself, the properties of $F$ (fermionic, charge-conserving, blind to neutrals), and why it is *not* supersymmetry.
- `01:26`–`01:31` Q&A on detectors, the S-matrix, and whether soft states are real.
- `01:31`–`01:44` Guessing the fermionic charge: soft part linear in $\Lambda$ with fermionic parameter $\chi$; the required commutator with supersymmetry; and the linear-in-$u$ wrinkle that stops the derivation. (Notes §Fermionic Conservation Laws.)

---

## Deltas versus the written lectures (arXiv:1703.05448)

This is the point of the file. Ordered roughly by how much the spoken version adds.

1. **The superselection-sector argument is given a purpose the notes do not state.** The notes (§SSB) explain that $d>2$ global symmetry breaking gives superselection sectors and that large gauge symmetry does not, and note that the symmetry action "in some regards mimics the $d=2$ case". They do **not** say *why that matters*: spoken, the point is that superselection sectors kill Ward identities, so the absence of them is what makes the whole programme possible (`00:42:47`, `00:43:50`). The word "untethered" (`00:52:52`) and the repeated framing "a symmetry at every angle" are spoken only.

2. **He admits the norm of $Q^+_\varepsilon|0\rangle$ has not been defined.** Nowhere in the notes. Spoken at `00:48:34`–`00:49:42`, under student pressure, with an explicit "I suspect there is a way to define it" and a refusal to let the gap license a superselection conclusion.

3. **The Goldstone-terminology pedantry.** The notes carry a footnote saying that words like "spontaneous symmetry breaking", "Goldstone boson" and "superselection sector" have been adapted. They do not contain the specific correction that only the zero mode transforms inhomogeneously (`00:28:53`), the remark that lumping the whole field under "Goldstone boson" has caused confusion (`00:35:26`), or the "it's a free world" concession about the word "soft".

4. **Soft photons as Goldstone bosons of *both* electric and magnetic large gauge symmetry** (`00:36:29`). The notes derive the complexified $U(1)$ but do not make this identification in these words.

5. **The explicit research method — guess the charge, then verify — is spoken only** (`01:30:32`, `01:31:35`), together with the blunt judgement that brute-force rewriting "never works in almost any problem". This is a methodology delta and, given the campaign's L6 loop, probably the most transferable item in the lecture.

6. **The "everything has a superpartner including theorems" heuristic and the counting argument delivered *before* any computation** (`00:55:05`, `00:57:13`, `00:58:15`). The notes make the same logical point (infinitely many fermionic symmetries cannot sit inside four supercharges) but present it as a consequence; spoken, it is presented as something you can know in advance, which is a different epistemic move.

7. **The technical wrinkle in the photino charge is flagged as an instance of a recurring phenomenon.** The notes' §Fermionic Conservation Laws handles the construction; spoken (`01:41:13`–`01:43:19`) he first says the obvious guess looks trivially easy, then warns that the linear-in-$u$ divergence forces a subtle projection, and ties it to the same phenomenon seen in the first problem set. Lecture 8 hits this a third time (`00:59:29` there), and he there calls it "ubiquitous". The recurrence is spoken-only framing.

8. **The S-matrix creed.** The notes' §Infrared Divergences argues that an S-matrix is needed for discussing unitarity or symmetries. The spoken version (`01:27:18`, `01:28:23`) is stronger and more personal: detector limits are not a licence to give up, and assuming unitarity fails in the soft sector is "very problematic — I don't know what that is".

9. **Classical Maxwell could have had this 150 years ago** (`00:20:18`). The notes make a related remark about QED being a century old; the spoken version pushes the date back and applies it to the *classical* magnetic conservation law, which is a sharper historical claim.

10. **Open-problem inventory not in the notes:** how to find and characterize all asymptotic symmetries (`00:19:13`); the magnetic soft factor in duality-symmetric theories (`00:14:59`); whether a larger theory with auxiliary fields could make all of them manifest (`00:17:05`).

11. **Not a delta (checked):** the duality-as-field-redefinition caveat, the Mexican-hat setup, the bubble-wall energy argument, the $d=2$ Coleman–Mermin–Wagner remark, the statement that not all asymptotic symmetries are subgroups of gauge symmetries, and the $\mathcal{N}=1$ counting argument all appear in the notes (lines 1289–1300, 1510, 1581, 1587). Only the framings listed above are new.

---

## Transcript quality notes

- Systematic ASR substitutions: "cell photon"/"self photon"/"sulf photon" → soft photon; "fotino"/"photina"/"fortino" → photino; "scribe plus"/"scry plus"/"square plus"/"cribe plus" → $\mathcal{I}^+$ (scri); "a billion"/"not a billion" → abelian/non-abelian; "Felicity" → helicity; "infinite decimal" → infinitesimal; "monkowski" → Minkowski; "Western backer" → Wess and Bagger; "Dumatresco" → Dumitrescu; "vacuole"/"vacuum a"/"tobacco" → vacua; "award identity" → a Ward identity.
- `[01:24:12]` "and then usually people go to something like Western Union" is unrecoverable ASR garbage — most likely "Wess–Zumino". Do not quote this line.
- `[00:45:07]`–`[00:50:45]` is a five-minute Q&A exchange where the student's questions are inaudible and only Strominger's half is captured. His answers are still usable (entries 21, 22) but the question being answered has to be inferred.
- `[01:26:15]`–`[01:27:18]` contains a long student question transcribed with heavy noise ("the Boston production"). The gist — can a detector distinguish the boson from the superpartner channel — is recoverable from his answer.
- Several `[Music]` markers appear where the audio drops; they mark short gaps, not content.
