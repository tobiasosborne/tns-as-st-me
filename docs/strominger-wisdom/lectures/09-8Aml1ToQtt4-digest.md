# Digest — Lecture 9: Memory Effects

- **Title:** Memory Effects (Lecture 9 of 10, *Infrared Structure of Gravity and Gauge Theory*, Harvard)
- **Speaker:** **NOT Strominger.** A guest lecturer who introduces himself as "Sasha" and says he is
  "talking instead of Andy". Most likely Alexander Zhiboedov (coauthor of the Strominger–Zhiboedov
  memory paper), but this is **unconfirmed** from the transcript alone. Every opinion, hesitation and
  judgment below is **the guest lecturer's**, not Strominger's.
- **Video id:** `8Aml1ToQtt4` — https://youtu.be/8Aml1ToQtt4
- **Duration:** 01:51:49
- **Source file:** `refs/strominger-videos/09-8Aml1ToQtt4.md` (auto-captions; secondary source, not L3 ground truth)
- **Written companion:** arXiv:1703.05448 §"The Memory Effect" (`refs/arxiv-1703.05448/soft_Arxiv_update.tex` ll. 2582–2657)

**Arc.** The lecture walks the memory corner of the triangle from the linearised plane-wave picture, to
the Christodoulou-type non-linear formula, to spin memory, to electromagnetic memory. The *derivations*
are essentially those of the written notes. What the notes do not contain is the running commentary:
which observables the speaker thinks deserve the name "memory" and which do not, why LIGO is blind to
the effect, why the standard "BMS detector" is an unphysical fiction with a rocket strapped to it,
where the classical memory/soft-factor dictionary quietly assumes a semiclassical process, an explicit
refusal to endorse the Goldstone-boson language the written notes use freely, and a closing insistence
that memory is only ever defined relative to a prior **calibration**. That commentary is what this
digest records.

---

## Insights

### 1. Memory is a *change* relative to a calibration, and without the calibration the question is empty
The closing remark of the lecture, and the sharpest conceptual statement in it. Every memory observable
he discussed was a difference measured against a reference state that the experimenters agreed on in
advance. Absent that agreement, asking for "the" memory of a system is not a well-posed question — the
example he gives is that the phase of a single electron, or the supertranslation frame of a distant
black hole, has no answer unless something fixes the zero.

> "the memory was always described by change in something we always started with some set of calibrated
> detectors if the word calibrated is extremely important here we calibrated them and then we look at
> the change for example if you give me an electron and you ask what is its phase this question is
> meaningless because I can choose it as I like unless there is a god-given prescription to call that
> election [sic: electron] was the zero phase"

`[8Aml1ToQtt4 @ 01:50:18]` — tags: memory, methodology, pitfalls, experiment, vacuum-degeneracy

### 2. …and the same warning applied to an isolated black hole
He extends the point immediately: a supertranslation charge is only meaningful against a pre-given
asymptotic structure. This is a caution against treating "the supertranslation hair of *this* black
hole" as an intrinsic, self-standing label.

> "if we go to the middle of the Galaxy and they ask what is a super translation [supertranslation] of
> this black hole I think it's this question can only be answered if we know that there was some
> pre-given structure of a space-time"

`[8Aml1ToQtt4 @ 01:51:20]` — tags: memory, charges, black-holes, pitfalls

### 3. The detector is defined by a protocol, not by a formula
Before writing a single equation he sets up memory operationally: two bodies carrying clocks, first
*synchronise*, then let the wave pass, then re-measure by exchanging light signals and comparing.
The calibration step is built into the definition of the measurement from the very start.

> "first they synchronize the clocks then some some some wave comes or something happens in a space
> time and they check their clocks the distance between them by exchanging signals again and then they
> can conclude if their clocks are still synchronized or or not"

`[8Aml1ToQtt4 @ 00:05:20]` — tags: memory, experiment, methodology

### 4. The signal has memory; the instrument does not
His crispest answer to an audience question, separating the physics from the apparatus. Worth keeping
as a slogan: a null result from a band-limited detector says nothing about whether the effect is there.

> "the actual signal I think has has a memory but the detector does not and this is signal for the as a
> detector"

`[8Aml1ToQtt4 @ 00:33:18]` — tags: memory, experiment, pitfalls

### 5. Why LIGO is blind to memory — the mechanism, not just the fact
The written notes say memory is "harder to see than gravity waves themselves". Here he says *why*:
LIGO's mirrors hang on suspensions rather than floating freely, which imposes a sensitivity band around
100 Hz, and memory is a zero-frequency effect that falls entirely outside it. The waveform plots
everyone has seen are therefore already missing the memory, by construction of the instrument.

> "if they attach to something like a mirrors there is a frequency range in which in which the detector
> is sensitive and say for ligo [LIGO] it's around 100. Hertz and this effect is zero it's an infrared
> effect it's a zero frequency … they just cannot they just cannot see it"

`[8Aml1ToQtt4 @ 00:12:45]` — tags: memory, experiment, ir-divergences, pitfalls

### 6. Free-flying detectors are the natural home for a DC observable
Immediately after: the fix is detectors that are genuinely inertial over long baselines, i.e. a
space-based constellation. He is careful to disclaim expertise.

> "there are efforts to detect … this gravitational memory effect using uh some other experiments say
> Eliza [LISA] space experiment when there are satellites which are freely flying in space is better
> for this kind of for this kind of effect"

`[8Aml1ToQtt4 @ 00:13:48]` — tags: memory, experiment

### 7. Higher soft moments are *not* memories, and he says so
Subleading soft factors can be written as higher moments $\int du\,(u-u_0)^n \partial_u h$. He derives
this and then declines to call the result a memory, on two grounds. First, only the $n=0$ moment is a
boundary quantity — the rest need the whole time history. This is a judgment about what earns the name.

> "the unpleasant thing about this memory this moments compared to that one is that this this integral
> is really localized at the boundaries … whereas for this moments to compute the integral you really
> have to integrate over time so they're a little bit non-local that's unpleasant and not really not
> really memories in this sense"

`[8Aml1ToQtt4 @ 00:18:02]` — tags: memory, soft-theorems, methodology, pitfalls

### 8. …and the second ground is a calibration ambiguity between observers
The higher moments depend on an arbitrary origin of time $u_0$, and shifting it mixes lower moments
into higher ones. Two experimenters would have to agree not only on the observable but on their choice
of $u_0$ — a second, independent calibration convention. This is the same theme as insight 1, arriving
by a different route.

> "when we compare this memory you put your detector and I put my detector and we will agree on the on
> the memory but here we will have to agree also the shift of your notice [u-nought] by shift by memory
> it's the first thing which is annoying"

`[8Aml1ToQtt4 @ 00:34:22]` — tags: memory, soft-theorems, pitfalls, methodology

### 9. Open problem: no clean detector protocol beyond the first subleading order
He can construct a $u_0$-free measurement for the subleading factor (the spin-memory ring, below), but
says he does not know how to do it at second subleading order or beyond, and that nobody has.

> "there is a way I know how to do it for M1 but I don't know for M2 and higher moments how to do this
> other than that principle one can try to imagine designing a some kind of a good procedure but it was
> not it hasn't been done so far"

`[8Aml1ToQtt4 @ 00:35:25]` — tags: open-problems, memory, soft-theorems, experiment

### 10. He dislikes the linear/non-linear memory terminology
Said twice, mildly but clearly. He uses the words because the literature does, not because he thinks
they carve anything at a joint.

> "even though I don't like so much as terminology but let me call this consideration say yeah a linear
> linear memory"

`[8Aml1ToQtt4 @ 00:25:44]` — tags: methodology, memory, history, pitfalls

### 11. …because the split is an artefact of which community you came from
The relativists' division — "linear" if sourced by massive matter, "non-linear" if sourced by the waves
themselves — has no counterpart on the amplitudes side, where the soft factor is blind to what the
external legs are. The distinction records a sociological history, not a physical one.

> "if you're a person who is coming from Quantum field Theory and then say you look at the soft factor
> for you all the particles such as the same gravity couples to everything"

`[8Aml1ToQtt4 @ 00:45:04]` — tags: history, methodology, soft-theorems, memory

### 12. Universality is the reason the two literatures could not see each other
Following on: the soft factor does not care whether the emitter is massive or massless, a graviton or a
star. This is what let Weinberg and Braginsky–Thorne write the same formula for different systems
without either noticing.

> "the soft gravity soft soft Factor it immediately emphasizes that you completely it's completely
> Universal effect it does not care if the particle is massive or massless if it's a graviton or not"

`[8Aml1ToQtt4 @ 00:57:55]` — tags: soft-theorems, memory, history

### 13. The horse in the desert — an intuition pump for the memory kernel's non-locality
The best pedagogical moment in the lecture. Does a horse galloping past your detector produce memory?
No — the Green's function vanishes at zero angular separation. The memory you actually see is dominated
by enormous energy fluxes at large angles, which is why black-hole mergers matter and nearby motion does
not. The written notes state the same fact about the kernel; they do not give you a way to feel it.

> "imagine I have a detector and uh it's in the desert and the horse run through the detector does it
> cause a lot of memory compared to some jet which goes very very far in the galaxies … this kernel is
> not peaked along the direction of observation so if you consider Theta equal to zero uh the kernel is
> zero"

`[8Aml1ToQtt4 @ 01:01:07]` (answer continues at `01:02:09`) — tags: memory, charges, methodology, experiment

### 14. Memory is a diagnostic that scattering occurred at all
If every incoming momentum equals an outgoing momentum, the memory vanishes identically; any genuine
rearrangement produces a generically non-zero memory. He returns to this framing twice as one of the
two things he wants remembered from the lecture.

> "if there is no scattering if just particles goes through space-time there is no memory on the other
> hand Whenever there is some non-trivial scattering this thing generically is not zero"

`[8Aml1ToQtt4 @ 00:27:54]` — tags: memory, soft-theorems, charges

### 15. IR divergences are the bookkeeping telling you the memory was ignored
He ties the two together directly: if you expand around Fock states that pretend no memory occurred,
loop diagrams punish you with infrared divergences. Then a plain admission that there is still no
systematic cure.

> "you'll have infrared divergences because if all right Divergence [an IR divergence] is telling you
> that you are not taken properly into account as infrared effects and uh as far as I know … there is
> no really a good way to take care of all that in a systematic fashion … but it seems that still in an
> open question"

`[8Aml1ToQtt4 @ 01:00:04]` — tags: ir-divergences, dressing, open-problems, soft-theorems

### 16. The "BMS detector" is a fiction, and he flags it rather than hiding it
The detector that makes the formalism work is *not* freely falling. Each element sits at fixed $(z,\bar z)$
in a chosen Bondi frame, which requires acceleration — he pictures a little rocket on each one — and he
does not know how to build one.

> "these detectors are not they're not geodesic detectors they're accelerated detectors so each of these
> each of the BMS detector carries a little rocket which keeps its fixed … the question how to realize
> it in practice I don't know but it's a convenient Choice"

`[8Aml1ToQtt4 @ 00:46:04]` (continues at `00:47:06`) — tags: memory, experiment, methodology, pitfalls

### 17. Displacement memory is frame-robust; clock desynchronisation is not
This is the single most campaign-relevant technical remark in the lecture. Accelerated (BMS) observers
and freely falling (geodesic) observers **agree** on the displacement memory at leading order, but only
the accelerated ones see their clocks drift apart. The DC displacement is the robust register; the
timing register depends on how the detector is held.

> "the difference between geodesics Observer and the BMS Observer is that they both agree on the memory
> but for some of them there is a desynchronization of the clocks which is for BMS Observer but for
> geodesic Observer you can check that the linear order there is no no clock desynchronization"

`[8Aml1ToQtt4 @ 01:11:34]` — tags: memory, supertranslations, experiment, methodology

### 18. Explicit warning: "supertranslation shifts $u$" does **not** mean "memory is a clock shift"
He anticipates the natural but wrong inference. Because a supertranslation acts by shifting retarded
time, one is tempted to read the memory effect as a desynchronisation. He calls this misleading: the
physical content is the residual deformation on the sphere, and for geodesic observers there is no
clock effect at all.

> "you could have thought that shifting U and super translating [supertranslating] is dual to or
> describes the synchronization of the clock so it's misleading"

`[8Aml1ToQtt4 @ 01:14:41]` — tags: pitfalls, supertranslations, memory

### 19. The desynchronisation is ordinary acceleration redshift in disguise
The demystification: Fermi normal coordinates (geodesic observer) give corrections quadratic in
separation, while Fermi–Walker coordinates (accelerated observer) put a correction in $g_{tt}$. The
clock drift is then just the redshift you always get from acceleration — nothing specific to BMS.

> "in the completely generic language when you have acceleration you can expect time desynchronization
> due to the usual time rate shift [redshift]"

`[8Aml1ToQtt4 @ 01:12:37]` — tags: memory, methodology, pitfalls

### 20. Open problem, stated as one: would free-falling satellites see spin memory at all?
Given insight 17, the worry is obvious and he raises it himself. His spin-memory ring was built from
BMS observers. LISA-like constellations follow geodesics. He does not know whether the effect survives,
and says the literature does not either.

> "if we have a set of detectors set of satellites each of them is following uh geodesic if they … will
> observe this effect so as far as I know it was not say answered the literature so uh I I I'm not sure
> if they will observe this effect or not"

`[8Aml1ToQtt4 @ 01:37:36]` — tags: open-problems, memory, experiment, superrotations

### 21. The LHC as a spin-memory detector — a joke with real content
A proton's quantum phase oscillates, so counter-circulating beams are a pair of clocks running the
right way round a loop. The obstruction is not the clock but the frame.

> "can we observe the gravitational memory effect was it with LHC for example again one has to LHC is
> not a HC is not a BMS Observer they don't they haven't built it properly"

`[8Aml1ToQtt4 @ 01:38:37]` — tags: experiment, memory, superrotations, pitfalls

### 22. The practical obstruction to spin memory: it is one power of $1/R$ down from a contaminant
Leading memory is $O(1/R)$; spin memory is $O(1/R^2)$. So the loop must be held in a BMS frame to a
precision set by the *larger* effect you are trying to see past.

> "you have to control your Loop was [with] a great precision to to keep it BMS so the Rockets which are
> on the loop keep it BMS have to be very very precise"

`[8Aml1ToQtt4 @ 01:42:53]` — tags: experiment, memory, superrotations, pitfalls

### 23. The memory/soft-factor dictionary is a semiclassical statement
Often passed over. The memory is an expectation value — an in-in (Schwinger–Keldysh) observable, not an
S-matrix element. It collapses to a ratio of amplitudes, and hence to the soft factor, only when a
single final state dominates the sum. For a genuinely superposed final state you must compute the in-in
object directly.

> "in principle you can choose a very very Quantum States states with as many superpositions of photons
> coming or particles coming from different directions and then they will evolve into superpositions of
> States also and then we really have to compute this in in [in-in] type of observable in quantum theory
> to to compute the memory"

`[8Aml1ToQtt4 @ 00:54:40]` — tags: memory, soft-theorems, methodology, pitfalls

### 24. Fixing the vacuum frame is a one-time choice; Einstein's equations do the rest
You may gauge-fix $C=0$ on the initial slice, but that exhausts your freedom — the constraints then
determine the supertranslation frame at every later time. A useful way to see why the "initial
calibration" is not an innocent convention: it is the only free choice you get.

> "we can do a gauge transformation where the initial State F equal to zero but as soon as we choose it
> at some point in time the Einstein's equations fix us and fixes for us f for all other times"

`[8Aml1ToQtt4 @ 00:32:13]` — tags: vacuum-degeneracy, supertranslations, methodology

### 25. Measuring electromagnetic memory is *harder* than gravitational, because a phase is a quantum observable
An asymmetry worth noting, given how often EM is offered as "the easy case". The gravitational effect is
a displacement you can watch; the electromagnetic one requires bringing charges back into interference.

> "notice that to measure the electromagnetic memory is interestingly it's harder to than to measure the
> gravitational memory because to measure the phase of a particle it's a Quantum measurement"

`[8Aml1ToQtt4 @ 01:50:18]` — tags: memory, dressing, experiment, large-gauge

### 26. Mild surprise that electromagnetism had an undiscovered memory effect
An aside on how such a thing could go unnoticed in a theory that old — and a refusal to make too much
of it.

> "the memory effect in electromagnetism which is very simple uh even though electromagnetism is so old
> I think it was not discussed before so I don't know if it's … one has to be proud about that"

`[8Aml1ToQtt4 @ 01:15:44]` — tags: history, memory, large-gauge

### 27. Explicit scepticism about the Goldstone-boson / spontaneous-symmetry-breaking language
The clearest dissent in the lecture, and it is a dissent from the framing the written notes use without
hesitation. He does not think the dictionary is well defined, and suspects everything sayable can be
said without it.

> "this dictionary I think is not completely well defined of ghosts and bosons [Goldstone bosons] and
> spontaneous symmetry breaking … probably any statement that can be made can be State can be can be
> made without saying the word ghost in both [Goldstone boson]"

`[8Aml1ToQtt4 @ 01:43:55]` (continues at `01:44:56`) — tags: pitfalls, vacuum-degeneracy, methodology

### 28. …and the reason is a missing counting theorem, which he names as a nice open problem
For internal symmetries the number of Goldstone bosons is fixed by the number of broken generators. For
spacetime symmetries it is not — his example is a crystal, where phonons are outnumbered by broken
generators. No analogue of the counting theorem is known here, and he says a proof would be what puts
the language on solid ground.

> "if we have a crystal with phonons many symmetries are broken but … the number of bosons is not equal
> to number of space symmetry broken generators … there is no such theorem as far as I know here and I
> guess if there is one that would be nice"

`[8Aml1ToQtt4 @ 01:44:56]` (continues at `01:45:58`) — tags: open-problems, vacuum-degeneracy, methodology

### 29. An honest closing verdict on that whole discussion
He does not resolve it and does not pretend to.

> "I thought well it's all very confusing at least I I find it the discussion to be quite preliminary at
> the moment"

`[8Aml1ToQtt4 @ 01:45:58]` — tags: open-problems, methodology, vacuum-degeneracy

### 30. Historical anecdote: Einstein to the editor
Told as a one-minute warm-up. Einstein and Rosen's 1936 submission arguing gravitational waves do not
exist was rejected by a referee — a practice Einstein was not used to.

> "the paper was rejected the gravity waves do not exist and uh in his complaint letter he … sent to the
> editor he said I send you my paper to publish not to referee"

`[8Aml1ToQtt4 @ 00:02:11]` — tags: history

---

## Structure of the argument (thin skeleton)

- `00:00:04` Framing and a potted history: Einstein 1916/1936, Hulse–Taylor 1975, LIGO 2016.
- `00:04:16` Detectors defined operationally (bodies + clocks + light signals + prior synchronisation).
- `00:06:23` Plane-wave metric; residual $\Delta h$ as a flat-space diffeomorphism; memory identified.
- `00:13:48` Fourier transform: memory $\leftrightarrow$ $1/\omega$ pole; higher moments $\leftrightarrow$ subleading soft factors (and his objections to calling them memory).
- `00:19:22` Linearised memory from a point-particle stress tensor; reproduces the soft factor.
- `00:29:31` Bondi gauge; vacuum transition; the non-linear formula with the $\log\sin^2(\Delta\Theta/2)$ kernel.
- `00:46:04` Detector taxonomy: BMS (accelerated) vs geodesic; displacement agrees, clock behaviour does not.
- `01:00:04` Break, then IR divergences and the horse-in-the-desert kernel discussion.
- `01:16:48` Spin memory: counter-orbiting clocks on a loop, angular-momentum flux, $1/R^2$ suppression, open detectability question.
- `01:43:55` Q&A on Goldstone language; `01:47:03` electromagnetic memory; `01:50:18` the calibration coda.

---

## Deltas vs the written lectures (arXiv:1703.05448)

The derivations here largely track §"The Memory Effect" of the notes. What follows is what the spoken
version adds, softens, or contradicts.

- **Calibration is named as the load-bearing concept — the notes never use the word.** `calibrat*`
  appears zero times in `soft_Arxiv_update.tex`. The notes say inertial detectors are "stationed near
  $\mathcal{I}^+$" and compute $\Delta s$; the lecture makes the prior synchronisation an explicit part
  of the measurement and then closes by arguing that without it the observable does not exist
  (insights 1–3, 8, 24). This is the sharpest available external support for treating "absolute
  response" and "calibrated relational susceptibility" as genuinely different registers.
- **The BMS detector is admitted to be unphysical.** The notes say "inertial detectors" and move on. The
  lecture says the detectors that make the formalism work carry rockets, are not geodesic, and that he
  does not know how to build one (insight 16). The notes contain no discussion of accelerated versus
  freely falling detectors at all.
- **Clock desynchronisation, and its absence for geodesic observers, is entirely new.** `desynchron*`
  and `Fermi normal` appear zero times in the notes. The whole `01:03:13`–`01:14:41` segment — including
  the explicit warning that "supertranslation shifts $u$" must not be read as "memory is a clock shift"
  — has no written counterpart (insights 17–19).
- **A judgment the notes do not make: higher soft moments are not memories.** The notes describe spin
  memory and colour memory as further memory effects without qualification. The lecture argues that only
  the leading moment is a boundary observable and that the higher ones carry an origin-of-time ambiguity,
  so calling them memories is a stretch (insights 7–8), and that no clean protocol is known past the
  first subleading order (insight 9).
- **Detectability is discussed mechanistically, not just optimistically.** The notes state that memory
  "has a decent chance of being measured in the coming decades" and cite measurement proposals. The
  lecture explains the specific reason LIGO cannot see it (suspended mirrors, ~100 Hz band, DC effect),
  and asks the unanswered question of whether geodesic satellite constellations see *spin* memory at all
  (insights 5, 6, 20, 22). `LISA` appears zero times in the notes.
- **Open dissent from the Goldstone/SSB framing.** The notes have a subsection titled "Spontaneous
  Symmetry Breaking, Vacuum Degeneracy, and Goldstone Bosons" and use the language throughout
  (`Goldstone` appears nine times). The guest lecturer declines to endorse it, points at the missing
  spacetime-symmetry counting theorem, and calls the discussion preliminary (insights 27–29). This is a
  direct emphasis conflict between the two sources and should be recorded as such.
- **The in-in caveat on the memory/soft-factor dictionary.** The notes derive memory classically and
  relate it to the soft theorem by Fourier transform. The lecture points out that the quantum object is
  an expectation value, and that the reduction to a soft factor assumes a dominant final state
  (insight 23). Nothing equivalent appears in the notes.
- **The horse-in-the-desert picture.** The notes state the kernel's non-locality ("if a gravity wave
  passes through the north pole, the effect vanishes both there and at the south pole but is large near
  the equator"). The lecture gives the same fact an operational reading — near-field motion produces
  nothing, distant large fluxes produce everything (insight 13).
- **Reverse delta (in the notes, absent here):** colour memory in non-abelian gauge theory, the
  detector-array/diffeomorphism-on-the-celestial-sphere picture (figure `membms`), and the observation
  that memory can be measured in finite time despite soft gravitons taking forever to resolve. The
  lecture does not mention any of these.

---

## Transcript quality notes

Auto-captions, with the expected damage. Recurring substitutions, silently normalised in the prose
above and bracketed in quotes: "super translation" for supertranslation, "ghosts and bosons" for
Goldstone bosons, "Eliza"/"Lisa" for LISA, "bondage gauge" for Bondi gauge, "short Shield" for
Schwarzschild, "vigil metric" for Vaidya metric, "koshy" for Cauchy, "Trigger keldish" for
Schwinger–Keldysh, "cze"/"CCC" for $C_{zz}$, "your note" for $u_0$, "polarov" for Polnarev, "braginsky
and thorn" for Braginsky and Thorne, "Crystal dulu" for Christodoulou. Author names and dates are
unreliable — at `00:45:04` the 1991 non-linear-memory attribution is left blank by the captions. Board
work is invisible, so equations are described only in words; several audience questions are inaudible
and only the answers survive, which is why some entries above quote a reply with no visible prompt.
