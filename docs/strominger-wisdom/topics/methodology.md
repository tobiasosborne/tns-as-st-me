# methodology

The largest file: how the work is actually done, how claims are calibrated, and
what he counts as evidence. Pointer convention `[id @ hh:mm:ss]` and all
caveats: [../INDEX.md](../INDEX.md). Entries marked *(guest)* are from lecture 9
and are **not** Strominger.

---

## How results are actually found

- **Brute force never works. Guess the charge from the shape of the soft theorem, then verify conservation and the Ward identity.** "A better approach is to just kind of look at this formula and try to guess what the symmetries might be, write down some charges, and then after you've done that verify that the charges are conserved and that their Ward identity is this soft theorem." `[WxCY-K-Jb4A @ 01:30:32]`, continuing `[WxCY-K-Jb4A @ 01:31:35]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **…the same method one level up:** the subleading soft factor was guessed from an angular-momentum-flux argument plus uniqueness, and only then shown equivalent — because going straight to momentum space produces terms you cannot tell should cancel. `[60U7_P2XJlQ @ 01:24:25]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **How the symmetries were originally found:** gauge-fix, look at the residual gauge transformations, do an asymptotic expansion, see what is left over. `[yeMZKViadhw @ 01:15:48]` — [L2](../lectures/02-yeMZKViadhw-digest.md)
- **Counting can settle a question before any computation** — an infinite family cannot sit inside a four-parameter one, so the fermionic symmetries had to be new before a single formula was written. `[WxCY-K-Jb4A @ 00:58:15]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **Name the structural coincidence first, then do the work:** "it's already looking very suspicious because indeed those soft theorems relate any S-matrix element and the same S-matrix element with a soft photon inserted". `[yeMZKViadhw @ 01:33:08]` — [L2](../lectures/02-yeMZKViadhw-digest.md)
- **The research went gravity first, and the possibility that it applied to QED made him nervous** — "somebody ought to have noticed it". `[Yx7PWgfC1dw @ 01:33:45]`, continuing `[Yx7PWgfC1dw @ 01:34:49]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
- **`w_{1+∞}` was not the target:** they derived something messier and afterwards found the field redefinition that made it recognisable. `[6kH2pl_zvMA @ 00:55:03]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **Explicit divide-and-conquer, with each deferred thing named** — massive charges, magnetic charges, timelike infinity, black holes. `[lvyyxkjwSCg @ 01:41:37]` — [L1](../lectures/01-lvyyxkjwSCg-digest.md)
- **Deliberate isolation: throw away the zero mode so the new phenomenon is visible.** `[H4IZ3jwTDp4 @ 00:53:23]` — [L10](../lectures/10-H4IZ3jwTDp4-digest.md)
- **There is no canonical entry point into the subject; he picks the earliest one on purpose.** Gauge theory or gravity, soft theorems or symmetries — all valid starting points, and 19th-century electromagnetism is chosen as the simplest. `[lvyyxkjwSCg @ 00:20:25]` — [L1](../lectures/01-lvyyxkjwSCg-digest.md)

## Choosing a formalism, a gauge, a language

- **Formalism choice is a tractability question, not a correctness one.** Hamiltonian, covariant phase space, S-matrix, Lagrangian, soft theorems, boundary-condition analysis — "they should all work. But it's a hard problem and it's important to find the simplest approach." `[6kH2pl_zvMA @ 00:36:46]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **The test for a good gauge choice is not correctness — that is guaranteed — but whether the answer comes out without large cancellations you cannot explain.** `[xZ2FG1kLb9I @ 00:32:22]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **Any extension of the gauge parameter into the bulk gives a true relation; only a good one gives a useful relation.** `[yeMZKViadhw @ 00:15:40]` — [L2](../lectures/02-yeMZKViadhw-digest.md)
- **Gauge choices are intuition-generating devices, and different choices teach different things** — the charge identity holds for any `ε` going to one at infinity. `[H4IZ3jwTDp4 @ 00:25:26]` (continues `00:26:29`) — [L10](../lectures/10-H4IZ3jwTDp4-digest.md)
- **The surface integral is gauge invariant; the volume integral requires a gauge** — the sharpest formulation of how a frame-dependent construction can carry frame-independent content. `[H4IZ3jwTDp4 @ 01:04:03]` — [L10](../lectures/10-H4IZ3jwTDp4-digest.md)
- **What is gauge invariant is the *statement*, not the derivation of it.** `[H4IZ3jwTDp4 @ 00:58:43]` — [L10](../lectures/10-H4IZ3jwTDp4-digest.md)
- **He rates a competitor's paper above his own and names the prejudice of his that was wrong** — he had thought fixing a gauge was a bad idea, and the gauge-fixed treatment turned out both nicer and closer to the right structures. `[xZ2FG1kLb9I @ 00:30:14]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **He does not like Bondi coordinates and uses them anyway, so he can look formulas up.** `[OXl7IXT7_Cw @ 01:07:56]`, `[OXl7IXT7_Cw @ 01:09:01]` — [L6](../lectures/06-OXl7IXT7_Cw-digest.md)
- **The route he did not take, and why he says so:** setting the derivation up as classical antipodal matching means subtracting a finite piece off a `u`-divergence with ambiguities to control. Explaining a methodological choice is more useful than the choice itself. `[60U7_P2XJlQ @ 01:07:02]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **Off-shell formalisms are not universal; soft theorems are** — so there is no reason the symmetry should look simple in any particular superfield language. A clean criterion for when an ugly formula is a fact about physics and when it is a fact about your conventions. `[WxCY-K-Jb4A @ 01:25:12]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **Duality is used as a field redefinition to dodge a nasty calculation, not as a claimed symmetry of the theory.** `[WxCY-K-Jb4A @ 00:11:50]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **He keeps every factor of two and pi in the first half of the course, for a stated reason** — the payoff is watching two very differently written objects turn out exactly equal — and abandons factor-precision for the Feynman-diagram section, saying so. `[lvyyxkjwSCg @ 01:21:30]`, `[swrNwD0ypaE @ 01:15:56]` — [L1](../lectures/01-lvyyxkjwSCg-digest.md), [L3](../lectures/03-swrNwD0ypaE-digest.md)
- **Notation choices are trades, and he flags them as such** — the antipodally-twisted sphere coordinate on scri⁻ was chosen over an alternative he judged worse; reusing symbols on scri⁻ was chosen over a parallel alphabet. `[lvyyxkjwSCg @ 00:58:03]`, `[Yx7PWgfC1dw @ 01:13:01]`

## What counts as adequate evidence

- **An asymptotic symmetry group has to earn its keep:** "it should be useful … it should tell us relationships between physical quantities that we can measure that we didn't know about before". `[7S3Eg4VlZf0 @ 00:10:35]` — [extra-03](../lectures/extra-03-7S3Eg4VlZf0-digest.md)
- **Applied to 2d CFT: meromorphic vector fields are kept because "it's good for something".** `[60U7_P2XJlQ @ 00:32:22]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **A conjectured symmetry earns its name only via a new soft theorem.** `[60U7_P2XJlQ @ 00:39:55]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **What he checks in place of the algebra:** that the coupling constants cancel and that the pole structures agree on both sides — "you can see the general features work out without checking all the details". `[swrNwD0ypaE @ 01:13:51]` — [L3](../lectures/03-swrNwD0ypaE-digest.md)
- **A symmetry has to act on in-states *and* out-states, i.e. commute with the Hamiltonian — "those are the useful things".** `[Yx7PWgfC1dw @ 01:25:10]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
- **The measuring-device criterion for physical inequivalence:** two configurations related by a diffeomorphism are physically different if an instrument can tell them apart — "we can measure things that are not related by diffeomorphisms". `[6kH2pl_zvMA @ 00:16:49]`, `[6kH2pl_zvMA @ 00:17:52]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **The boost intuition pump for the same point.** `[6kH2pl_zvMA @ 00:03:12]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **The news–`C` commutator is derived, not assumed — with "what else could it be" offered as supporting evidence.** `[60U7_P2XJlQ @ 00:55:07]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **The Kac–Moody level check is set as homework rather than asserted.** `[OXl7IXT7_Cw @ 00:25:18]` — [L6](../lectures/06-OXl7IXT7_Cw-digest.md)
- **Convergence from unrelated directions is what he counts as evidence that a structure is real** — three independent routes to superrotations. `[6kH2pl_zvMA @ 01:01:22]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **Detector limitations are not an argument against wanting an S-matrix**, and assuming unitarity fails in the soft sector is "very problematic". `[WxCY-K-Jb4A @ 01:27:18]`, `[WxCY-K-Jb4A @ 01:28:23]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)

## Naming what is assumed

- **"If we don't assume there's some kind of matching conditions … we just don't have a theory."** `[H4IZ3jwTDp4 @ 00:28:37]` — [L10](../lectures/10-H4IZ3jwTDp4-digest.md)
- **"Symmetries imply conservation laws only if you have unitarity … I'm assuming unitarity, I'm not trying to prove unitarity."** `[H4IZ3jwTDp4 @ 00:29:40]` — [L10](../lectures/10-H4IZ3jwTDp4-digest.md)
- **…and how one proceeds anyway:** "make some reasonable plausible set of assumptions and try to build a consistent theory". `[H4IZ3jwTDp4 @ 00:30:46]` — [L10](../lectures/10-H4IZ3jwTDp4-digest.md)
- **The bracket computation is labelled semi-classical, and the quantum question — anomalies included — is explicitly conditional and outsourced to Feynman diagrams.** `[yeMZKViadhw @ 01:19:06]`, `[yeMZKViadhw @ 01:22:17]` — [L2](../lectures/02-yeMZKViadhw-digest.md)
- **What was proved is a symmetry of the S-matrix, not of the Lagrangian, and he flags the gap rather than papering over it.** `[WxCY-K-Jb4A @ 00:30:02]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **"No corrections" always silently means "no corrections in perturbation theory".** `[xZ2FG1kLb9I @ 01:10:33]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **The no-monopole assumption is flagged as temporary and load-bearing.** `[yeMZKViadhw @ 00:27:37]` — [L2](../lectures/02-yeMZKViadhw-digest.md)
- **He has not given a complete definition of asymptotic flatness and says so** — "necessary if not sufficient conditions". `[Yx7PWgfC1dw @ 00:14:12]`, `[Yx7PWgfC1dw @ 00:15:14]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
- **"Let me tell you what I am conspicuously not saying"** — flagging the omitted edge-of-scri discussion at the moment of making it. `[Yx7PWgfC1dw @ 00:12:04]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
- **A self-correction from "prove" to "conjecture", mid-sentence.** `[xZ2FG1kLb9I @ 01:20:20]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **The magnetic symmetry statement is explicitly labelled a guess from duality covariance, because the brackets have not been computed.** `[xZ2FG1kLb9I @ 01:44:19]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **He marks mid-talk where established material ends and speculation begins.** `[6kH2pl_zvMA @ 00:57:11]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **The memory/soft-factor dictionary is flagged as semiclassical:** the quantum object is an in-in expectation value, and the reduction to a soft factor assumes a dominant final state. `[8Aml1ToQtt4 @ 00:54:40]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)

## Register: stating a claim without overclaiming

- **"We have not solved the information paradox. I can't say this often enough."** `[wg-4Rm-kk70 @ 00:23:42]` — [extra-02](../lectures/extra-02-wg-4Rm-kk70-digest.md)
- **The model for how to state a research position:** "I doubt that everything I've taught you is qualitatively enough to solve the information problem … I think we've turned the problem upside down and seen that the old arguments are wrong … I don't see an obstacle to solving it through this, but neither do I think it's around the next corner." `[H4IZ3jwTDp4 @ 01:41:26]` — [L10](../lectures/10-H4IZ3jwTDp4-digest.md)
- **The model for stating the status of a research programme:** celestial holography is a *proven* rewriting, not a duality — the open questions are usefulness and an intrinsic definition of the other side, and "here we only have a left". `[6kH2pl_zvMA @ 01:03:27]`, `[6kH2pl_zvMA @ 01:04:30]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **What the programme is *not*:** "not new physics, not a new proposal for what the microscopic laws are … new insights into the structure of the laws in the limits where we already understand them, namely long distances". `[6kH2pl_zvMA @ 00:09:25]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **An explicit disclaimer of novelty, immediately after a striking derivation:** "we haven't discovered anything new here … we've just derived it in a different way from a conservation law". `[wg-4Rm-kk70 @ 00:13:56]` — [extra-02](../lectures/extra-02-wg-4Rm-kk70-digest.md)
- **Grading which steps are hard:** the infinite family of conservation laws is "completely trivial" given the matching; the content is in the translation between corners. `[wg-4Rm-kk70 @ 00:08:40]` — [extra-02](../lectures/extra-02-wg-4Rm-kk70-digest.md)
- **Where the reformulation ends and discovery starts, said plainly:** QED was old physics in new language; superrotations are where something is predicted. `[60U7_P2XJlQ @ 01:15:41]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **A deep-versus-bookkeeping judgment on his own recent work:** the physics is the asymptotic constraint equations; the contribution is the repackaging. `[6kH2pl_zvMA @ 00:48:38]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **He labels his own motivation section "BS" in his notes** — a joke, but a signal about how he separates advocacy from technical content. `[lvyyxkjwSCg @ 00:20:25]` — [L1](../lectures/01-lvyyxkjwSCg-digest.md)
- **He flags that his own motivation has moved:** "how I came into the subject, maybe not how I go out of it". `[lvyyxkjwSCg @ 00:10:54]` — [L1](../lectures/01-lvyyxkjwSCg-digest.md)
- **Self-criticism of the field, delivered mildly:** "this is a basic question about nature which all the experiments have already been done … it's a job for the theorists and we haven't done our job. And we've had a long time to do it in." `[6kH2pl_zvMA @ 00:35:42]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **What gets cut from a talk, and why:** he had prepared the string-worldsheet slide and removed it as too speculative — then said it anyway once a questioner gave him licence. `[7S3Eg4VlZf0 @ 00:37:21]` — [extra-03](../lectures/extra-03-7S3Eg4VlZf0-digest.md)
- **An open invitation, not a result:** "this is a work in progress, my understanding of many points is incomplete … I welcome your input" (2013), against "an exact mathematical equivalence between three phenomena" (2016). The change in register is itself evidence about how confidence was built. `[7S3Eg4VlZf0 @ 00:11:38]` — [extra-03](../lectures/extra-03-7S3Eg4VlZf0-digest.md)

## Classroom candour and self-correction

- **He asks the class to correct his equations and says plainly that he makes a lot of mistakes**; "I hope everybody is checking me". `[yeMZKViadhw @ 00:09:23]`, `[lvyyxkjwSCg @ 01:00:09]`
- **He admits he never managed the direct Green's-function integral and got the answer another way.** `[xZ2FG1kLb9I @ 00:44:05]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **A live boost-charge fumble, abandoned honestly:** "wait, this isn't quite right — let me not try to sort that out in real time". `[60U7_P2XJlQ @ 01:02:40]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **"I'll always get confused by that"** — about the factor of `i` relating the sphere component of the field strength to the magnetic field. `[xZ2FG1kLb9I @ 01:36:50]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **A live hermiticity slip and correction:** `A_z` is not hermitian — roughly `a_x + i a_y` — so the conjugate creates the opposite helicity. `[yeMZKViadhw @ 01:55:46]` — [L2](../lectures/02-yeMZKViadhw-digest.md)
- **A live self-correction on what "cumulative" means, walked back under challenge to "proportional to the total energy flux".** `[CdFyoaNv8GI @ 00:31:25]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **A guess retracted live about the gravity central charge.** `[60U7_P2XJlQ @ 01:34:01]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **A concession under pressure that his uniqueness-of-definition argument for "energy at an angle" may be too strong.** `[CdFyoaNv8GI @ 00:52:50]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **An honest "I didn't know about this"** when told from the floor that the soft limit needs non-exceptional momenta. `[CdFyoaNv8GI @ 00:10:02]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **He stops the lecture to make the class compute the things he judges load-bearing** — the soft-photon pairing coefficient in the symplectic form, and the asymptotic value `ρ → |p|/m` on the hyperboloid. `[yeMZKViadhw @ 00:50:44]`, `[xZ2FG1kLb9I @ 00:58:49]`
- **He raises the natural objection to his own result before anyone else can.** `[H4IZ3jwTDp4 @ 01:05:24]` — [L10](../lectures/10-H4IZ3jwTDp4-digest.md)
- **A modelling choice made on taste, said out loud: "somehow I don't like having white holes".** `[H4IZ3jwTDp4 @ 01:15:09]` — [L10](../lectures/10-H4IZ3jwTDp4-digest.md)
- **The `ħ`-counting exercise done live to license the classical/quantum split.** `[H4IZ3jwTDp4 @ 00:22:19]` — [L10](../lectures/10-H4IZ3jwTDp4-digest.md)
