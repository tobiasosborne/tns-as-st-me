# Campaign hooks

Where the harvest touches this campaign. Each hook gives the wisdom (with a
pointer), the campaign object it bears on, and one sentence on why it matters.

**This file only points.** It edits nothing in `claims/`, `definitions.md`,
`theory/` or `paper/`, and it creates no claims. Nothing here is L3-citable —
these are auto-captioned videos, and the written source for any citation is
arXiv:1703.05448 in `refs/arxiv-1703.05448/`. Read a hook as "an expert, talking
freely, took this position", not as evidence.

Pointer convention `[id @ hh:mm:ss]` and all caveats: [INDEX.md](INDEX.md).
Entries marked *(guest)* are lecture 9, whose speaker is **not** Strominger.

**Hook numbers are stable anchors, not an ordering** — other files link to
`#h1`, `#h3`, `#h4`, `#h10`, so the numbers do not run consecutively down the
page. Contents:

| § | hooks | subject |
|---|---|---|
| A | H1, H2, H10, H9, H11, H13, H28 | the two memory registers, D32 / D33 |
| B | H6, H18, H19, H20 | the operational razor and corner A |
| C | H2b, H8, H3, H27, H22 | the finite-system / reduction program |
| D | H4, H5 | antipodal matching as an input assumption |
| E | H7, H16, H17, H21 | which register the lattice corner is in |
| F | H24, H26, H25, H14 | register, naming, not overclaiming |
| G | H12, H23, H15, H30 | warnings the campaign should carry |
| H | — | hooks looked for and not found |

---

## A. The two memory registers — D32 and D33

### H1
**The explicit inter-source tension: calibration versus phase space.**

*Wisdom (a).* Lecture 9's closing remark: "the memory was always described by
change in something — we always started with some set of calibrated detectors,
if the word *calibrated* is extremely important here. We calibrated them and
then we look at the change. If you give me an electron and you ask what is its
phase, this question is meaningless … unless there is a god-given prescription
to call that electron the zero phase."
`[8Aml1ToQtt4 @ 01:50:18]` — [L9 (guest)](lectures/09-8Aml1ToQtt4-digest.md)

*Wisdom (b).* Strominger, pressed on the apparatus in the same programme:
"no, you don't care about experimental device … the flat connections on the
sphere at infinity are physical, you have to specify a flat connection, and that
is a physical thing which has meaning."
`[F42XbX45Dzw @ 01:02:06]` — [extra-05](lectures/extra-05-F42XbX45Dzw-digest.md)

*Campaign object.* **D32** (memory, absolute-response register) and **D33**
(calibrated relational memory susceptibility), `definitions.md`; the TJO ruling
of 2026-08-31 that made them two registers rather than one.

*Why it matters.* The campaign's split is not an invention forced by the SYK/JT
result — it is a live disagreement inside the source literature, with one
speaker locating the physical content in a *calibrated difference between
measurements* (that is D33's declared-cost ratio functional) and the other in
*data you must specify in the phase space* (that is closer to D32's absolute
response against a fixed allowed observable). Neither position is in the written
notes; `calibrat*` occurs zero times in the TeX. This is the sharpest external
support the campaign has for treating the two registers as genuinely different,
and it also warns that D32/D33 will read as a substantive choice to anyone who
holds the other view.

### H2
**Displacement memory is frame-robust; clock desynchronisation is not.**

*Wisdom.* "The difference between geodesic observer and the BMS observer is that
they both agree on the memory, but for some of them there is a desynchronization
of the clocks … for geodesic observer you can check that at linear order there
is no clock desynchronization."
`[8Aml1ToQtt4 @ 01:11:34]` — [L9 (guest)](lectures/09-8Aml1ToQtt4-digest.md).
He also warns explicitly against reading "supertranslation shifts `u`" as
"memory is a clock shift" `[8Aml1ToQtt4 @ 01:14:41]`, and demystifies the
drift as ordinary acceleration redshift `[8Aml1ToQtt4 @ 01:12:37]`.

*Campaign object.* D32's requirement of a *single allowed observable fixed in
advance with `T`-independent norm bound*; D33 clause (ii), invariance under the
specification's gauge redundancies.

*Why it matters.* This is the continuum precedent for the campaign's own finding
that which register a system passes depends on the reference apparatus, not only
on the dynamics: the same physical event yields a robust DC displacement and a
frame-dependent timing record. It is also a reminder to state, for every lattice
memory claim, which of those two the observable is.

### H10
**Higher soft moments are not memories — and Strominger says they are.**

*Wisdom (a).* Lecture 9 declines the name on two grounds: only the `n=0` moment
is a boundary quantity, the rest need the whole time history
`[8Aml1ToQtt4 @ 00:18:02]`; and the higher moments depend on an arbitrary time
origin `u₀`, so two experimenters must agree on a *second* calibration
convention before they can compare `[8Aml1ToQtt4 @ 00:34:22]`. He adds that no
clean `u₀`-free protocol is known past the first subleading order
`[8Aml1ToQtt4 @ 00:35:25]`. — [L9 (guest)](lectures/09-8Aml1ToQtt4-digest.md)

*Wisdom (b).* Strominger, late period: "each current has an observable memory
effect … and there's an algorithmic way to compute what these effects are."
`[6kH2pl_zvMA @ 00:51:49]` — [cstq](lectures/cstq-6kH2pl_zvMA-digest.md)

*Campaign object.* D32's reserved use of the unqualified word "memory"; the
Letter naming-discipline decision (**bd tns-94j**); the N1 finding that
D26+D27 are charge-transfer counting statistics rather than radiative memory.

*Why it matters.* The campaign already ruled that satisfying D33 does not
license the word "memory". Lecture 9 is an independent instance of exactly that
ruling being made in the continuum, with the *same* reasons — boundary-locality
of the observable, and an extra convention that two parties must agree on. That
is useful support for the naming discipline, and (b) is a fair warning that not
everyone in the field draws the line there.

### H9
**The memory ↔ soft-factor dictionary is a semiclassical statement.**

*Wisdom.* Memory is an in-in (Schwinger–Keldysh) expectation value, not an
S-matrix element; it collapses to a ratio of amplitudes, and hence to the soft
factor, only when a single final state dominates. For a genuinely superposed
final state you must compute the in-in object directly.
`[8Aml1ToQtt4 @ 00:54:40]` — [L9 (guest)](lectures/09-8Aml1ToQtt4-digest.md)

*Campaign object.* D32/D33 are both stated on *states* `ω_T^P` at detector time
`T`, not on S-matrix elements; the SYK/JT observables spec's Layer 0/1/2
structure (`theory/lanes/syk-jt/observables-spec.md`).

*Why it matters.* It says the campaign's choice to define both registers on
expectation values in a declared window — rather than on scattering data — is
the *more general* of the two continuum formulations, not a lattice
approximation to it. That is worth knowing when the reduction program has to
argue that the lattice statement limits onto an accepted continuum one.

### H11
**"The signal has memory; the detector does not" — and the readout cost.**

*Wisdom.* "The actual signal I think has a memory, but the detector does not."
A null result from a band-limited instrument says nothing about whether the
effect is there. `[8Aml1ToQtt4 @ 00:33:18]` —
[L9 (guest)](lectures/09-8Aml1ToQtt4-digest.md)

*Campaign object.* D33's declared measurement cost (shot count for a stated
relative error at time `T`); the adjudicated instance **JT-B-susc** /
**JT-noplat-abs**, where the readout cost grows exponentially in detector time.

*Why it matters.* The campaign's structural finding — a thermal reference frame
erodes its own record, so the ratio survives while the absolute response does
not — is exactly a "the signal has it, the detector cannot get at it" situation,
and this is the continuum vocabulary for saying so without conceding that the
effect is absent.

### H13
**LIGO cannot see memory, and the reason is the declared window.**

*Wisdom.* Suspended mirrors impose a sensitivity band around 100 Hz; memory is a
zero-frequency effect and falls entirely outside it, so the published waveforms
are already missing it by construction of the instrument
`[8Aml1ToQtt4 @ 00:12:45]` — [L9 (guest)](lectures/09-8Aml1ToQtt4-digest.md).
Strominger's version: memory is "a DC effect … *if they are inertial detectors*"
`[wg-4Rm-kk70 @ 00:03:18]` — [extra-02](lectures/extra-02-wg-4Rm-kk70-digest.md).

*Campaign object.* D32/D33's **declared asymptotic window** — the order in which
large-parameter limits are taken before `T`, and the admissible `T`-range within
stated validity.

*Why it matters.* It is a concrete precedent that a DC memory statement is
meaningless without saying in which band, over which times, with which
apparatus — which is exactly the work the declared window does in D32/D33, and
a good argument for keeping it in the Letter rather than in a footnote.

### H28
**An implementable protocol for the electromagnetic case.**

*Wisdom.* Prepare two charges with aligned phases, separate them, let the large
gauge transformation act, bring them back and interfere; his favourite version
is a short Susskind note using an array of SQUIDs connected by resistors.
`[F42XbX45Dzw @ 01:01:02]` — [extra-05](lectures/extra-05-F42XbX45Dzw-digest.md)

*Campaign object.* The O2 experiment list from the operational wave
(`theory/verdicts/operational-wave-adjudication-r1.md`); the "family of
implementable protocols" clause in D32.

*Why it matters.* It is the most operationally specific thing anyone in this
corpus says about measuring an electromagnetic memory, and it is the closest
continuum analogue to an interference-based lattice protocol — worth comparing
against before claiming a lattice protocol is novel.

---

## B. The operational razor

### H6
**The measuring-device criterion for physical inequivalence.**

*Wisdom.* Two gravitons leaving the poles, supertranslated so that one departs
fifty years early and the other a hundred years late: "that's a diffeomorphism,
but it's a physically inequivalent situation. We could construct a measuring
device which would distinguish between these two possibilities." Generalised one
beat later: "we can measure things that are not related by diffeomorphisms."
`[6kH2pl_zvMA @ 00:16:49]`, `[6kH2pl_zvMA @ 00:17:52]` —
[cstq](lectures/cstq-6kH2pl_zvMA-digest.md)

*Campaign object.* The **operational razor** (TJO, 2026-08-31): only
observable/implementable quantities count; representations never are. The 48-row
operational registry (O1) and the O2 impossibility result that the ansatz gauge
datum has zero quantum Fisher information.

*Why it matters.* Strominger's criterion is the razor stated from the other
side: not "discard what is not observable" but "*admit* what an instrument can
distinguish, even when a formal redundancy says it should not be admitted". The
campaign needs both directions — the razor to discard `V(g)`, and this to keep
the endpoint data — and it is worth knowing that the constructive half has a
named continuum precedent.

### H18
**The surface integral is gauge invariant; the volume integral requires a gauge.**

*Wisdom.* Under sustained audience pushback ("I just don't want anything to
change if I make a gauge transformation"), this is where he lands: "if you're
not going to choose a gauge you're only going to be able to discuss the surface
integral … the minute you want to discuss a volume integral you must choose some
gauge" `[H4IZ3jwTDp4 @ 01:04:03]`. And the separation: "this equation is gauge
invariant … but to understand it in this nice simple way as a change in `A_z`
induced by the shock wave, I had to choose a gauge"
`[H4IZ3jwTDp4 @ 00:58:43]`. — [L10](lectures/10-H4IZ3jwTDp4-digest.md)

*Campaign object.* The operational registry's OBSERVABLE / IMPLEMENTABLE / GAUGE
trichotomy; **bd tns-0g9** (fold O1 statuses into definitions and labbook);
the corner-A result that `V_α(g)` is GAUGE with conjugacy class and `[ω_α]`
surviving.

*Why it matters.* This is a transferable argument for exactly the position the
campaign occupies: a frame-dependent construction can carry frame-independent
content, provided you say which is which. It is also the register in which to
answer the referee who objects that the endpoint construction is "just a gauge
choice".

### H19
**An asymptotic symmetry group has to earn its keep — and "allowed/trivial" is squishy.**

*Wisdom (a).* "What exactly you mean by [an asymptotic symmetry group] changes
with every new application … my point of view is that it should be useful. It
should tell us relationships between physical quantities that we can measure
that we didn't know about before." `[7S3Eg4VlZf0 @ 00:10:35]` —
[extra-03](lectures/extra-03-7S3Eg4VlZf0-digest.md)

*Wisdom (b).* Both halves of the definition are "a little bit squishy":
constructing charges to decide triviality is often impractical, and even when
you can, "if the charges vanish you might say they're trivial, but that also
turns out not to always be exactly right."
`[swrNwD0ypaE @ 00:13:01]` — [L3](lectures/03-swrNwD0ypaE-digest.md)

*Wisdom (c).* Applied to superrotations, the criterion becomes concrete: "there
better be some new soft theorem that this is related to."
`[60U7_P2XJlQ @ 00:39:55]` — [L8](lectures/08-60U7_P2XJlQ-digest.md)

*Campaign object.* Corner A (`theory/corner-a.md`, claims **WI**, **A1**,
**A2**, **G0**), and specifically **A1(e)**: stabiliser `S_α ⊇ G_diag`, effective
orbit `𝒜_eff = G/N_α`, not `𝒜` — the lattice instance of "the trivial subgroup
is not what you assumed it was".

*Why it matters.* (b) is direct external support that a non-trivial kernel
`N_α` is a *feature of the scheme*, not a defect of the lattice instantiation —
the accepted continuum construction has the same soft spot and says so. (a) and
(c) set the bar the campaign has already accepted: corner A earns its name via
the A⇒C edge, not by construction alone.

### H20
**What a Ward identity is when there is no S-matrix.**

*Wisdom.* Two definitions, both given in answer to questions: the charges
commute with the S-matrix — equivalently, since `S = lim exp(iHT)`, with the
Hamiltonian; and, more loosely, "Ward identity is a pretty general term which
means relationships between objects that are implied by symmetries."
`[yeMZKViadhw @ 01:16:52]`, `[yeMZKViadhw @ 01:20:08]` —
[L2](lectures/02-yeMZKViadhw-digest.md). The operative criterion: a symmetry has
to act on in-states *and* out-states, i.e. commute with `H` — "those are the
useful things" `[Yx7PWgfC1dw @ 01:25:10]` — [L7](lectures/07-Yx7PWgfC1dw-digest.md).

*Campaign object.* **ML4-Ward** and the A⇒C edge; **bd tns-5oc** (corner-C
campaign: general soft theorem from Ward identity + AC-EX).

*Why it matters.* The campaign uses "Ward identity" in a lattice setting where
the S-matrix framing does not transfer. The second, looser definition is
Strominger's own and is the one that does transfer; the commutes-with-`H`
version is the bridge. Quoting the criterion in this form — from the TeX where
possible — pre-empts the objection that the lattice statement is not really a
Ward identity.

---

## C. The finite-system / reduction program

### H2b
**Finite regions with boundaries: the symplectic argument, and the warning.**

*Wisdom (a).* A questioner proposes gauge transformations that are pure gauge
everywhere except in an infinitesimal neighbourhood of a causal-diamond
boundary, and suggests these should go over into BMS supertranslations in the
large-region limit. Strominger agrees, and gives the reason: cut off away from
infinity the transformation is a *null* direction of the symplectic form; "it's
a non-degenerate direction of the symplectic structure exactly because of a
boundary term at infinity — so it's the same story as you always have when you
have a boundary condition that makes some gauge transformations into things that
act non-trivially on the phase space."
`[CdFyoaNv8GI @ 01:20:25]` — [extra-01](lectures/extra-01-CdFyoaNv8GI-digest.md)
*(He credits the symplectic result to "car and somebody in the late 80s";
Crnkovic–Witten is a plausible but **unverified** reading.)*

*Wisdom (b) — the caveat, and it is a warning.* "It's generally true that … your
finite system will have less symmetry than the infinite system it grows to …
in AdS₃ you can do this with a cutoff, but what you actually find is that you
don't have the full set of conformal transformations at any finite distance —
you only have some subset preserved by the boundary conditions you impose. In
all known ways of doing it, it's difficult to recover the full group."
`[CdFyoaNv8GI @ 01:22:31]` — [extra-01](lectures/extra-01-CdFyoaNv8GI-digest.md)

*Wisdom (c) — the intermediate position he does allow.* Work at finite distance,
impose extra boundary conditions, look for an analogue of BMS there; whether it
works in Minkowski space is "just a technical question", not a conceptual
obstruction. `[CdFyoaNv8GI @ 01:21:28]` — [extra-01](lectures/extra-01-CdFyoaNv8GI-digest.md)

*Campaign object.* The **reduction program** (TJO directive: results must limit
onto what people actually accept; `docs/reduction-limits.md`, lanes in
`theory/lanes/reduction/`, **bd tns-4as**); corner A's finite-window
constructions (**WI**, **A1** padded windows); the Kähler/moment-map lane
(**bd tns-89h**, symplectic structure on the MPS manifold, charges generating
asymptotic symmetries via Poisson brackets).

*Why it matters.* This is the most campaign-relevant exchange in the whole
corpus, and it cuts three ways. (a) is Strominger endorsing, in his own words,
the mechanism the campaign relies on — a boundary term is what promotes a gauge
transformation to a physical one, and the symplectic/moment-map framing in
`docs/framing.md` is the same picture. (c) says the finite-region programme is
legitimate. But (b) is the sharpest available *external* statement of the
campaign's own risk: a finite system generically carries **less** symmetry than
the infinite limit, with the AdS₃ cutoff as the named cautionary tale. Any claim
that the lattice construction recovers the full asymptotic group in the limit
has to survive that expectation. It also predicts, correctly, the shape of the
campaign's own R2 finding — that the naive specialization of the continuum
construction is the REFUTED orbit row.

### H8
**Integration constants at every order in `1/r` — the data-specification gap.**

*Wisdom.* "I'm not completely clear if it's understood. I know that I don't
understand exactly what the situation is at higher orders — if you want to be
able to solve to all orders in the `1/r` expansion, if you get new integration
constants at every order … I suspect not, I suspect that it stops at some order,
but I don't actually know how it works or know of anywhere that that problem has
been spelled out. In fact, even in electromagnetism I'm not sure how it works."
`[60U7_P2XJlQ @ 01:01:37]`, context at `[60U7_P2XJlQ @ 01:00:32]` —
[L8](lectures/08-60U7_P2XJlQ-digest.md)

*Campaign object.* The reduction program's obligation to name every silent
continuum assumption as a lattice hypothesis (R4); the **PROTO-LSZ** definitional
gap (**bd tns-7ou**); **bd tns-94g** (Cesàro-versus-pointwise Tauberian bridge).

*Why it matters.* It is an explicit admission that the *continuum* side of the
reduction has an unspecified data problem at subleading orders, in gravity and
in electromagnetism alike. That is a licence to scope: the lattice statement
does not have to reduce onto a subleading continuum statement that nobody has
written down, and saying so is honest rather than evasive. It is also the exact
question lecture 7 calls "the point that everybody would have missed"
(`[Yx7PWgfC1dw @ 01:08:32]`), which makes it a good candidate for where a
lattice treatment could actually say something.

### H3
**"AdS has no version of this, because it's gapped."**

*Wisdom.* In the opening taxonomy — the triangle occurs in QED, non-abelian
gauge theory, gravity, higher dimensions, cosmology — "anti-de Sitter seems not
to have a version of this because it's gapped."
`[CdFyoaNv8GI @ 00:04:31]` — [extra-01](lectures/extra-01-CdFyoaNv8GI-digest.md).
The methodological version returns later: "if you were to study quantum gravity
by putting it in a box and taking that box out to infinity you would miss all of
this" `[CdFyoaNv8GI @ 01:07:45]`. Lecture 10 gives the sharp technical
disanalogy — no infinite degeneracy at fixed energy in AdS₃, because Virasoro
changes the energy `[H4IZ3jwTDp4 @ 01:39:19]` —
[L10](lectures/10-H4IZ3jwTDp4-digest.md).

*Campaign object.* Model selection across the campaign: the gapped SPT/AKLT lane
versus the gapless XXZ/kink lanes; the showcase model (**bd tns-f5r**); the
SYK/JT companion (**bd tns-62n**, **bd tns-wvp**).

*Why it matters.* This is the sharpest necessary condition anyone in the corpus
states for importing the triangle into a new system, and the campaign works on
both sides of it. It is a reason to be explicit about *why* a gapped lattice
model can still host a corner-A construction (the answer being that the
degeneracy is an edge/endpoint degeneracy, not a bulk gaplessness), and a
prompt to say so before a referee raises it. Note the counter-pull recorded in
[misc.md](topics/misc.md#cross-source-tensions-collected): the massive-QED
Green's function *is* the AdS₃ bulk-to-boundary propagator, and CSTQ says the
flat-space programme was an extension of AdS work.

### H27
**Why non-abelian is harder: the interactions do not switch off at long distance.**

*Wisdom.* "The basic reason why non-abelian gauge theories are different from
gravity and QED is that the problems we're talking about here are problems at
very long distances … in both QED and gravity at very long distances there's no
interactions and you have free field theory. The same thing is not true in
non-abelian gauge theories — there are interactions which persist and must be
dealt with at arbitrarily long distances."
`[OXl7IXT7_Cw @ 00:58:11]` — [L6](lectures/06-OXl7IXT7_Cw-digest.md)

*Campaign object.* Model selection again; the R1 reduction finding that the
strict continuum limit is free (Dyson) and that limits commute.

*Why it matters.* It gives a physical criterion for which lattice models should
be expected to support a clean reduction: those whose effective long-distance
theory becomes free. The campaign's R1 result is the lattice instance of exactly
that condition being met, which is worth stating as the reason the reduction
works rather than as a lucky fact.

### H22
**The soft limit needs non-exceptional momenta.**

*Wisdom.* An audience member points out that the soft momentum must be smaller
than every internal momentum and every partial sum, and that if an internal line
is itself soft you must add emissions from it. Strominger's reply is an honest
"I didn't know about this — I hope it doesn't affect what I'm going to say."
`[CdFyoaNv8GI @ 00:10:02]` — [extra-01](lectures/extra-01-CdFyoaNv8GI-digest.md)

*Campaign object.* **D31** clause 4 — the packet velocity separation
`dist(V₁,V₂) ≥ ε_v > 0` and `dist(V_i,{0}) ≥ ε₀ > 0`; **AC-EX-2M**; the
order-of-limits discipline in **bd tns-acr**.

*Why it matters.* The campaign's fixed-packet separation hypotheses are usually
presented as technical conditions needed for the Cook/Gram estimates. This says
the continuum soft theorem has a hypothesis of the same *kind* — a
non-exceptional-momentum condition — that the standard statements leave implicit
and that its own author had not internalised. That is a reasonable defence of
the lattice hypotheses as faithful rather than restrictive.

---

## D. Antipodal matching as an input assumption

### H4
**There is no first-principles proof.**

*Wisdom.* "I've never seen this matching condition discussed. It's a property of
the Liénard–Wiechert potential and that's been sitting there for 130 years …
you can derive it quantum mechanically from the soft photon theorem — the soft
photon theorem implies it — but it seems pretty weird to be using quantum field
theory to prove results relevant to 19th-century electromagnetism … I would
think that there would be some set of assumptions and some way to prove it, make
it into a mathematical theorem, but I haven't seen that."
`[lvyyxkjwSCg @ 01:26:02]` — [L1](lectures/01-lvyyxkjwSCg-digest.md)

*And the hedged bet:* "I believe it would not be hard to prove that this is the
only Lorentz invariant boundary condition, though I haven't tried to do it";
plus the practical reason it cannot be dropped — "if you want to solve a
scattering problem you need to define what you're doing all the way out at
infinity." `[lvyyxkjwSCg @ 01:28:42]`

*Contrast, a year earlier:* "as far as I know there's only one Lorentz-invariant
CPT-invariant way of specifying that boundary condition … and moreover the
agreement with the soft graviton theorem implies that that boundary condition is
the one that's implicitly being used when we do Feynman diagrams."
`[CdFyoaNv8GI @ 00:57:05]` — [extra-01](lectures/extra-01-CdFyoaNv8GI-digest.md)

*Campaign object.* The antipodal matching condition as a quoted input assumption
in `theory/lanes/reduction/q1-gauss.md` §0 (quoting
`refs/arxiv-1703.05448/soft_Arxiv_update.tex:633-650`); the reduction program's
mapping of continuum assumptions onto named lattice hypotheses (R4).

*Why it matters.* The campaign quotes the matching condition as an input rather
than deriving it. This is the author saying, in the lecture that introduces it,
that *he* has no derivation either, that it is verified rather than proved, and
that the only known derivation runs backwards from the quantum soft theorem. So
importing it as an assumption is not a shortcut the campaign is taking — it is
the state of the art, and the honest thing is to say so in exactly those terms.
The 2015/2016 discrepancy also warns against quoting the stronger uniqueness
claim without the hedge.

### H5
**Assumptions named as assumptions — matching, and unitarity.**

*Wisdom (a).* Asked whether the matching conditions survive violent non-linear
dynamics in the middle: "if we don't assume there's some kind of matching
conditions, I mean we just don't have a theory … what you're asking me is how do
we know that there is a theory." Preceded by the physical plausibility argument:
"the long distance metric from the Sun is no different than the long distance
metric from a Schwarzschild." `[H4IZ3jwTDp4 @ 00:28:37]`

*Wisdom (b).* Unprompted: "symmetries imply conservation laws only if you have
unitarity, so I'm not proving here that information is [preserved] — I'm
assuming unitarity, I'm not trying to prove unitarity."
`[H4IZ3jwTDp4 @ 00:29:40]`

*Wisdom (c).* And how one proceeds anyway: "nobody can ever prove that there
isn't some crazy thing that happens in the middle of the spacetime that violates
unitarity … the way to proceed is to make some reasonable plausible set of
assumptions and try to build a consistent theory." `[H4IZ3jwTDp4 @ 00:30:46]` —
all [L10](lectures/10-H4IZ3jwTDp4-digest.md)

*Campaign object.* Repo law **L10** (honest verdicts) and **L9** (no
overclaiming); the L5 claims DAG's `depends-on` column; the scope qualifiers
copied verbatim from critic rulings into the JT-A rows.

*Why it matters.* It is a worked model, from the source the campaign is
reducing onto, of the register the campaign has committed to: name the
assumption, give the plausibility argument, refuse to dress the assumption as a
result, and say what the research strategy is anyway. Worth reading before
writing the Letter's assumptions paragraph.

---

## E. Which register the lattice corner is in

### H7
**The observability contrast: phases need interference, a time shift does not.**

*Wisdom.* "A gauge transformation, a phase on a state — in classical
electromagnetism the phases are unobservable, so in order to talk about
observable consequences of these angle-dependent gauge transformations we have
to talk about quantum interference. And here we have an actual physical time
translation — so if we start moving things around, translating them forward or
backward in time in an angle-dependent way on the sphere, that is something
which has a classically observable consequence."
`[swrNwD0ypaE @ 00:06:37]` — [L3](lectures/03-swrNwD0ypaE-digest.md)

Repeated as the historical explanation ("phases are kind of slippery quantum
mechanical objects", `[Yx7PWgfC1dw @ 01:02:09]`), as the reason gravity was
found first (`[F42XbX45Dzw @ 01:01:02]`), and inverted for the non-abelian case,
where colour-singlet-ness is already a classical question
(`[OXl7IXT7_Cw @ 00:49:47]`).

*Campaign object.* D32 versus D33 again — which register a corner sits in;
the operational registry's classification of endpoint phases as OBSERVABLE;
**bd tns-25h** (the reconstruction theorem: charge ledger ↔ field-side memory).

*Why it matters.* It is the continuum taxonomy the campaign's registers refine.
Strominger's split is *classical displacement* versus *quantum phase*; the
campaign's is *absolute response* versus *calibrated ratio*. They are not the
same cut, and the Letter should say which one it means — a lattice kink
displacement is Strominger's "classically observable" side and D32's side, while
a phase-only observable would need an interference protocol before it counts as
either.

### H16
**"Untethered" and ultralocality — why a 1D chain might host this, and the caution.**

*Wisdom (a).* "It's a symmetry at every angle; the different angles are not tied
together, and that makes it like the one-plus-one dimensional problem … it's
untethered — these symmetry transformations, the points on the sphere at null
infinity, are not tethered to one another, and so it doesn't cost energy in the
same way." `[WxCY-K-Jb4A @ 00:52:52]`, `[WxCY-K-Jb4A @ 00:41:44]` —
[L5](lectures/05-WxCY-K-Jb4A-digest.md)

*Wisdom (b).* The causal version: "all the points at null infinity are out of
causal contact, so it's an ultralocal theory — there's nothing tying together
these points on the sphere, and so you can move them up and down independently.
It would sort of violate causality to have some principle that forced you to
move them all together." `[CdFyoaNv8GI @ 00:37:46]` —
[extra-01](lectures/extra-01-CdFyoaNv8GI-digest.md)

*Wisdom (c).* And the reason it matters technically: superselection sectors kill
Ward identities, and the absence of them here — because it costs only finite
energy to move between vacua — is what makes the whole programme possible.
`[WxCY-K-Jb4A @ 00:42:47]`, `[WxCY-K-Jb4A @ 00:43:50]` —
[L5](lectures/05-WxCY-K-Jb4A-digest.md)

*Campaign object.* Corner A's two-endpoint structure (**A1**, **D4**: boundary
maps modulo the trivially-acting subgroup, two endpoint copies); the R4 note in
`theory/lanes/reduction/q1-gauss.md` that a 3D region has an *extensive* 2D
boundary, not two copies.

*Why it matters.* Strominger himself says the mechanism "makes it like the
one-plus-one dimensional problem" — the best available motivation for looking
for the triangle on a chain. But it also names precisely what does *not*
transfer: on the sphere the untethering is over a continuum of angles, whereas a
chain has two endpoints, and the reduction lane has already flagged that
asymmetry as the place the two asymptotic algebras fail to be isomorphic.
Quote (a) as motivation and (b)/(c) as the mechanism, and keep the disanalogy
visible.

### H17
**The `U=1` flat-connection assumption, and the discomfort he flags immediately.**

*Wisdom.* "Something that should be but isn't usually emphasized in textbooks is
that we're assuming that the sphere at infinity has a flat connection on it,
`U=1`" `[OXl7IXT7_Cw @ 00:16:02]` — followed at once by "already here we see
that that assumption is a little bit funny, because when there's soft gluons
around … they characterize transitions from one flat connection to another flat
connection" `[OXl7IXT7_Cw @ 00:17:06]` — [L6](lectures/06-OXl7IXT7_Cw-digest.md)

*Campaign object.* The corner-A reference datum: **A1(c)** (`ω^{M@b} = ω^{M'@b}`
iff `M' ∈ ℂ^× M`, the endpoint space as a `PGL(χ)`-torsor) and **A1(d3)**
(`[ω_α]` obstructs removing the multiplier, not the projective window action);
**bd tns-r7q** (Haag duality as the cut-exhaustiveness theorem for corner A).

*Why it matters.* The campaign's endpoint/reference-frame datum plays the role
`U=1` plays here, and the tension is the same one: the reference frame is
assumed fixed, and the very excitations under study are what move it. Strominger
flags the assumption as textbook-silent and immediately uncomfortable, which is
useful cover for the campaign stating its own reference-frame choice loudly —
and a reminder that a torsor, not a value, is the honest object.

### H21
**The vacuum label is an extra integration function, and the charges do not see it.**

*Wisdom (a).* "You would also have to specify `C_zz` up there … and this is the
point that everybody would have missed."
`[Yx7PWgfC1dw @ 01:08:32]` — [L7](lectures/07-Yx7PWgfC1dw-digest.md)

*Wisdom (b).* And the trap for anyone building a "which vacuum am I in?"
observable: all the supertranslation vacua carry *zero* supertranslation charge,
because the group is abelian — "you can't use this to distinguish two vacuum
states, so I have to look at something different … the angular momenta will
certainly be different."
`[CdFyoaNv8GI @ 01:12:01]` — [extra-01](lectures/extra-01-CdFyoaNv8GI-digest.md)

*Campaign object.* **bd tns-25h** — the missing reconstruction theorem
connecting the charge ledger (D26/D27) to the field-side (bond/potential)
memory; the N1 finding that D26+D27 are counting statistics, not radiative
memory.

*Why it matters.* This is the continuum instance of exactly the gap the
definitional audit found: the conserved charges do **not** by themselves label
the vacuum, and the label lives in a separate datum that the charges are blind
to. It supports the campaign's decision to treat the reconstruction as an open
obligation rather than an assumed identification, and it names what the
reconstructed object should be — the field-side integration datum, not a charge.

---

## F. Register, naming and not overclaiming

### H24
**How to state the status of a programme without overclaiming.**

*Wisdom (a).* On celestial holography: "it's not a conjecture … it's been proven
that you could rewrite, until you're blue in the face, any scattering amplitude
in quantum gravity so it looks like a correlation function of conformal field
theory and it will obey the symmetries. That's been proven. The question is
whether it's useful … and even more whether you could intrinsically define the
right hand side on its own right." `[6kH2pl_zvMA @ 01:03:27]` — with the
diagnosis: "for AdS/CFT we have a left and a right, they have separate
definitions and wherever we can compare them, they agree. Here we only have a
left." `[6kH2pl_zvMA @ 01:04:30]` — [cstq](lectures/cstq-6kH2pl_zvMA-digest.md)

*Wisdom (b).* "We have not — I can't say this often enough — we have not solved
the information paradox." `[wg-4Rm-kk70 @ 00:23:42]` —
[extra-02](lectures/extra-02-wg-4Rm-kk70-digest.md)

*Wisdom (c).* The hedged personal position: "I doubt that everything I've taught
you in this course is qualitatively enough to solve the information problem …
I think we've turned the problem upside down and seen that the old arguments are
wrong … and I don't see an obstacle to solving the information problem through
this, but neither do I think it's around the next corner."
`[H4IZ3jwTDp4 @ 01:41:26]` — [L10](lectures/10-H4IZ3jwTDp4-digest.md)

*Campaign object.* Repo law **L9** (the paper is the product; no overclaiming —
every statement traces to a PROVED claim or is labelled a conjecture) and **L7**
(register: cautious scientific optimism, no arrogant tone); `docs/prose-guide.md`.

*Why it matters.* (a) is the exact shape the Letter's central claim needs: state
what is *proved* (a rewriting / an exact identity), state separately what is
*open* (usefulness, and whether the other side has an independent definition),
and give the disanalogy plainly. (b) and (c) are calibration models for the
Letter's discussion section. This is the same register `docs/prose-guide.md`
targets, sourced from the field this campaign is writing into.

### H26
**Scope words that silently mean less than they say.**

*Wisdom.* "All the derivations you will often see in the literature of this
statement that the soft theorem has no corrections — when you look at it, what
is really meant is that it has no corrections in perturbation theory … in some
sense the soft theorem is exact in QED, but QED doesn't actually exist as a
quantum field theory because of the Landau pole."
`[xZ2FG1kLb9I @ 01:10:33]` — [L4](lectures/04-xZ2FG1kLb9I-digest.md). Related:
what was proved is a symmetry of the S-matrix, not of the Lagrangian, and he
flags the gap rather than papering over it `[WxCY-K-Jb4A @ 00:30:02]`; the
non-abelian relations are "really only valid at tree level"
`[OXl7IXT7_Cw @ 00:59:12]`.

*Campaign object.* **bd tns-94j** (Letter naming discipline after the
definitional audit — safe names are charge ledger / Fourier response / TPM
statistics / exact-band scattering); the scope qualifiers on the JT-A rows;
**bd tns-md9** (Fig-2 caption overclaims universality of the coefficient 2).

*Why it matters.* The campaign already has a naming-discipline decision pending.
This is the same discipline applied by the author of the results the campaign
reduces onto, and it supplies the pattern: state the qualifier *in the sentence*
("no corrections **in perturbation theory**", "a symmetry **of the S-matrix**",
"**at tree level**"), not in a later caveat.

### H25
**Method: guess then verify, and the no-unexplained-cancellations test.**

*Wisdom (a).* "There would be the brute force method, which never works in
almost any problem … a better approach is to just look at this formula and try
to guess what the symmetries might be, write down some charges, and then after
you've done that verify that the charges are conserved and that their Ward
identity is this soft theorem."
`[WxCY-K-Jb4A @ 01:30:32]` — [L5](lectures/05-WxCY-K-Jb4A-digest.md)

*Wisdom (b).* The test for a good choice of extension or frame: "one should get
the same answer no matter how you do this, but if you do it in a nice way it
should come out simply; if you do it in a bad way you'll have all kinds of terms
which cancel each other but it's not obvious why they should do so."
`[xZ2FG1kLb9I @ 00:32:22]` — [L4](lectures/04-xZ2FG1kLb9I-digest.md)

*Wisdom (c).* What he checks when he skips the algebra: that the coupling
constants cancel and the pole structures agree.
`[swrNwD0ypaE @ 01:13:51]` — [L3](lectures/03-swrNwD0ypaE-digest.md)

*Campaign object.* Repo law **L6** (proposer/critic to fixed point) and **L1**
(red-green TDD); the `rk-light` skill's checker discipline.

*Why it matters.* (a) is the same shape as the campaign's proposer/critic loop —
propose a structure, then adversarially verify it — and (b) is a cheap
additional checker the campaign could adopt verbatim: if a derivation only works
through cancellations you cannot explain, the frame is wrong even though the
answer is right. (c) is a calibration for how much verification an intermediate
step needs.

### H14
**Infrared divergences as the enforcement of comparability.**

*Wisdom.* "The role of infrared divergences in QED is: if you try to compute
something that is forbidden by the conservation laws, QFT is much cleverer than
you and it will set that amplitude to zero by introducing infrared divergences
which just shut it down … there are no real infrared divergences in QED; they're
just a penalty that we pay if we are so foolish as to try to compute something
that must be zero due to an elementary conservation law."
`[GpN8VAauyj8 @ 00:10:50]`, `[GpN8VAauyj8 @ 00:11:55]` —
[extra-04](lectures/extra-04-GpN8VAauyj8-digest.md)

*Campaign object.* D32's **comparability** clause: two protocols are comparable
only when they agree on every exactly conserved allowed charge of the
specification.

*Why it matters.* The comparability clause can look like a technical guard
against trivial answers. This says it is the same condition the continuum theory
enforces on itself, violently: a protocol pair that disagrees on a conserved
charge does not merely give a meaningless memory, it gives an amplitude the
theory sets to zero. That is a good one-sentence justification for the clause in
the Letter.

---

## G. Warnings the campaign should carry

### H12
**The detector that makes the formalism work is not physically realisable.**

*Wisdom.* "These detectors are not geodesic detectors, they're accelerated
detectors — each of the BMS detectors carries a little rocket which keeps it
fixed … the question how to realize it in practice, I don't know, but it's a
convenient choice."
`[8Aml1ToQtt4 @ 00:46:04]` (continues `00:47:06`) —
[L9 (guest)](lectures/09-8Aml1ToQtt4-digest.md)

*Campaign object.* The operational razor's IMPLEMENTABLE column; the O2
experiment list.

*Why it matters.* A cautionary case directly against the campaign's own
standard: the accepted continuum memory formalism is stated in terms of a
detector nobody knows how to build, and its own expositor says so. If the
lattice construction's protocols *are* implementable, that is a real and
statable advantage — but only if the claim is made in the same breath as
acknowledging that the continuum comparison object is not.

### H23
**What does not transfer: the kernel's angular structure.**

*Wisdom.* The horse in the desert — a horse galloping past your detector
produces no memory, because the Green's function vanishes at zero angular
separation; the memory you see is dominated by enormous fluxes at large angles.
`[8Aml1ToQtt4 @ 01:01:07]` — [L9 (guest)](lectures/09-8Aml1ToQtt4-digest.md).
The same kernel, `D²(D²+2)` on the sphere, reappears in the black-hole corner
`[H4IZ3jwTDp4 @ 01:22:40]` — [L10](lectures/10-H4IZ3jwTDp4-digest.md).

*Campaign object.* The reduction program's obligation to identify what does and
does not limit correctly (R1–R4, `docs/reduction-limits.md`); the R3
non-reduction already on the books (**bd tns-bsk**, transmission crossover).

*Why it matters.* A large part of the continuum memory story is the *geometry*
of a kernel on `S²`, and a chain has no such geometry. The campaign already has
one honest non-reduction on record; this is a second place to check, and a
reason to be precise that what reduces is the DC response and the soft-charge
split, not the angular kernel structure.

### H15
**Superselection sectors are the hinge.**

*Wisdom.* "When you have superselection sectors you don't get interesting Ward
identities in the same way … you can't really write down Ward identities for
spontaneously broken symmetries with superselection sectors — but here we don't
have the superselection sectors, it only takes a finite amount of energy to go
from one vacuum to the other."
`[WxCY-K-Jb4A @ 00:42:47]`, `[WxCY-K-Jb4A @ 00:43:50]` —
[L5](lectures/05-WxCY-K-Jb4A-digest.md). Related: the Faddeev–Kulish basis's
unitarity is "a slightly subtle question because there are superselection sectors
associated with the conserved charges … it might be that it's unitary but
doesn't cluster properly" `[GpN8VAauyj8 @ 00:30:05]` —
[extra-04](lectures/extra-04-GpN8VAauyj8-digest.md).

*Campaign object.* The SYK/JT observables spec's Layer 0 parity superselection
("a single Majorana is NOT an observable"),
`theory/lanes/syk-jt/observables-spec.md`; D32's comparability clause.

*Why it matters.* The campaign's Layer 0 imposes a superselection rule as the
operational bedrock. Strominger says superselection sectors are precisely what
*obstruct* useful Ward identities in the continuum. Those are compatible — his
sectors are large-gauge sectors, the campaign's is fermion parity — but the
Letter should not let a reader conflate them, and should say which superselection
rules are in force and which are argued to be absent.

### H30
**A norm that has not been defined, and a gap he refuses to spend.**

*Wisdom.* "I don't think the norm has been fully defined … there are tricky
issues about limits and so on … I suspect there is a way to define it … but we
certainly wouldn't want to conclude that there are superselection sectors."
`[WxCY-K-Jb4A @ 00:48:34]`, `[WxCY-K-Jb4A @ 00:49:42]` —
[L5](lectures/05-WxCY-K-Jb4A-digest.md)

*Campaign object.* Repo law **L10**; the campaign's own pattern of registering a
gap as an open obligation (**bd tns-25h**, **bd tns-7ou**) rather than assuming
past it.

*Why it matters.* A short, exact model of the move the campaign makes
repeatedly: state the gap, state what you nevertheless believe, and state
explicitly that the gap does not license the opposite conclusion. Worth having
as a template sentence.

---

## H. Hooks looked for and not found

Recorded so a later session does not repeat the search.

- **Nothing in this corpus addresses lattice or tensor-network realisations of
  the triangle.** The nearest approaches are the finite-region exchange (H2b),
  the ultralocality/1+1d remark (H16), and the AdS-is-gapped line (H3). No
  speaker mentions spin chains, MPS, discretisation, or a finite-dimensional
  Hilbert space in this connection.
- **Nothing addresses SYK or JT gravity.** The corpus predates or ignores the
  Schwarzian literature; the closest is the AdS₃-cutoff cautionary tale in H2b
  and the AdS-degeneracy disanalogy in H3.
- **No statement about memory in a system whose reference frame decays.** The
  campaign's D33 divergence — a thermal reference frame eroding its own
  record — has no counterpart here. H11 is the closest vocabulary, and it is
  about instrument bandwidth, not about the ruler decaying.
- **No treatment of measurement cost or shot counts.** D33's declared-cost
  clause has no continuum precedent in this corpus; the nearest is the practical
  precision argument for spin memory `[8Aml1ToQtt4 @ 01:42:53]`.
