# soft-theorems

Pointer convention `[id @ hh:mm:ss]` and all caveats: [../INDEX.md](../INDEX.md).
Entries marked *(guest)* are from lecture 9 and are **not** Strominger.

---

## What a soft theorem is

- **Properly read, a soft theorem is a linear relation among S-matrix elements — and the fact that the soft momentum can go to zero in *any direction* is what turns one relation into infinitely many.** `[WxCY-K-Jb4A @ 00:56:09]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **The slogan he says out loud and the notes never quite do: one soft theorem for every globally conserved quantity** — electric charge, energy-momentum, magnetic charge, angular momentum, "and then some others that are more mysterious". `[xZ2FG1kLb9I @ 01:33:38]` (runs into `01:34:42`) — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **The soft factor is generically an *operator* on the external states; the abelian case where it is a number is the exception.** `[OXl7IXT7_Cw @ 00:06:26]`, continuing `[OXl7IXT7_Cw @ 00:07:29]` — [L6](../lectures/06-OXl7IXT7_Cw-digest.md)
- **Why the term is called "soft", in the route he actually gives:** insert `e^{iωu}` into the `u`-integral and note there is no `ω` in the expression, so it is the zero-frequency Fourier component, linear in the field, creating or annihilating one photon of zero energy. `[yeMZKViadhw @ 00:23:16]` — [L2](../lectures/02-yeMZKViadhw-digest.md)
- **Gauge invariance of the soft factor is equivalent to global charge conservation**, and he attributes something close to this argument to Low in 1958. `[swrNwD0ypaE @ 01:33:11]` — [L3](../lectures/03-swrNwD0ypaE-digest.md)
- **The subleading soft factor is finite where the leading one has a pole, because there is a `q` upstairs as well as downstairs**; interpretively, it rotates about the axis through which the particle emerges. `[60U7_P2XJlQ @ 01:16:49]`, `[60U7_P2XJlQ @ 01:17:54]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)

## How they are actually found

- **Brute force never works: guess the charge from the shape of the soft theorem, then verify conservation and the Ward identity.** `[WxCY-K-Jb4A @ 01:30:32]`, continuing `[WxCY-K-Jb4A @ 01:31:35]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **The subleading soft factor was guessed, not derived** — going straight to momentum space produces terms you cannot tell should cancel; it was guessed from the angular-momentum-flux argument plus uniqueness, and only then shown equivalent. `[60U7_P2XJlQ @ 01:24:25]`, setup at `[60U7_P2XJlQ @ 01:23:20]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **A conjectured symmetry earns its name only by producing a new soft theorem** — stated as the plan of attack before deriving anything. `[60U7_P2XJlQ @ 00:39:55]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **What he checks when he declines to do the algebra:** that the coupling constants cancel and that the pole structure matches on both sides. `[swrNwD0ypaE @ 01:13:51]` — [L3](../lectures/03-swrNwD0ypaE-digest.md)
- **Choosing `ε = 1/(z−w)` costs no generality** — if the identity holds for that family for every `w`, a few lines give it for arbitrary `ε`. `[swrNwD0ypaE @ 01:12:36]` — [L3](../lectures/03-swrNwD0ypaE-digest.md)
- **The uniqueness argument that stands in for the general-spin calculation:** the soft factor is the only expression with the right dimensions invariant under shifts of the polarization by the photon momentum. `[swrNwD0ypaE @ 01:35:18]` — [L3](../lectures/03-swrNwD0ypaE-digest.md)
- **What makes the diagrammatic derivation powerful is that the interior is a black box** — only the external-leg propagator and the vertex matter, so it applies to every theory containing a photon. `[swrNwD0ypaE @ 01:20:11]` — [L3](../lectures/03-swrNwD0ypaE-digest.md)
- **The two derivations have opposite difficulty profiles in the mass:** in the diagrammatic proof the mass hardly enters, while in the asymptotic-symmetry derivation massive and massless are qualitatively different problems. `[swrNwD0ypaE @ 01:24:33]` — [L3](../lectures/03-swrNwD0ypaE-digest.md)
- **The massive Ward identity looks nothing like Weinberg's theorem when you first write it down** — recognition is the hard part, not the derivation. `[WxCY-K-Jb4A @ 00:04:18]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **He names the structural coincidence before doing the work:** the identity "already looks very suspicious", since both sides relate an amplitude to the same amplitude with a soft photon inserted. `[yeMZKViadhw @ 01:33:08]` — [L2](../lectures/02-yeMZKViadhw-digest.md)

## Scope, corrections and what "exact" means

- **"The soft theorem has no corrections" always silently means "no corrections in perturbation theory"** — and the natural non-perturbative test is unavailable because QED does not exist as a theory. `[xZ2FG1kLb9I @ 01:10:33]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **The magnetic correction is offered as a conjecture, with a self-correction from "prove" to "conjecture" in the sentence**, plus a suggested use: soft factors must transform properly under duality, which may constrain dualities. `[xZ2FG1kLb9I @ 01:20:20]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md); the open invitation "nobody's worked that out" at `[WxCY-K-Jb4A @ 00:14:59]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **Confidence calibration on that conjecture: unproved, but "there doesn't seem to be much room" for corrections.** `[OXl7IXT7_Cw @ 00:26:23]` — [L6](../lectures/06-OXl7IXT7_Cw-digest.md)
- **The magnetic correction bites only in specific regimes** — a magnetically charged final state, or a low-energy effective theory on a monopole superselection sector where the magnetic dipole moments change; he explicitly disavows monopoles in loops. `[xZ2FG1kLb9I @ 01:14:57]` through `[xZ2FG1kLb9I @ 01:18:14]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **The soft gluon theorem gets one-loop corrections, so everything in the non-abelian lecture is tree level**, and understanding those corrections in this language is called an interesting unsolved problem. `[OXl7IXT7_Cw @ 00:26:23]`, continuing `[OXl7IXT7_Cw @ 00:27:28]` — [L6](../lectures/06-OXl7IXT7_Cw-digest.md)
- **A caveat raised from the floor that he had not heard before:** the soft limit needs non-exceptional momenta — the soft momentum must be smaller than every internal momentum and every partial sum, and a soft internal line requires extra emissions. His reply is an honest "I didn't know about this". `[CdFyoaNv8GI @ 00:10:02]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **Sub-subleading soft theorems: he says plainly he does not understand them** — Gross's 1960s paper says where the tower stops, and beyond the first subleading order "we understand them less and less". `[CdFyoaNv8GI @ 00:33:33]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **Low's 1958 subleading soft theorem in abelian gauge theory is tied to "some symmetry that we don't really understand very well"** — the older corner is not in better shape than the new one. `[60U7_P2XJlQ @ 01:24:25]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **The subleading soft photon theorem may be what the SCET community calls reparameterization invariance of jets**, with only a few things understood about it. `[lvyyxkjwSCg @ 01:20:39]` — [L1](../lectures/01-lvyyxkjwSCg-digest.md)
- **The mixed double soft limit of `J_z` and `J_z̄` does not commute** — evidence of structure nobody has understood. `[OXl7IXT7_Cw @ 01:00:16]`, continuing `[OXl7IXT7_Cw @ 01:01:20]` — [L6](../lectures/06-OXl7IXT7_Cw-digest.md)

## Attribution and disclaimers

- **An unusually candid attribution exchange:** Bloch–Nordsieck predate QED, Low apparently used dispersion rather than diagrams, the modern diagrammatic form is Weinberg's, and Weinberg may have been first to treat a single soft photon — "you could also credit it to Maxwell, I don't know". `[swrNwD0ypaE @ 00:58:31]` — [L3](../lectures/03-swrNwD0ypaE-digest.md)
- **An explicit disclaimer of novelty:** having derived a bizarre-looking infinite family of relations, he says immediately "we haven't discovered anything new here … we've just derived it in a different way from a conservation law". `[wg-4Rm-kk70 @ 00:13:56]` — [extra-02](../lectures/extra-02-wg-4Rm-kk70-digest.md)
- **Where he thinks the programme crosses from reformulation into discovery:** the QED chapters restated known physics in a new language, and superrotations are the first place something is predicted. `[60U7_P2XJlQ @ 01:15:41]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **In a supersymmetric theory every theorem has a superpartner** — a joke used as the motivation for expecting a soft photino theorem before any calculation. `[WxCY-K-Jb4A @ 00:55:05]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **Universality is the reason the memory and amplitudes literatures could not see each other** — the soft factor is blind to whether the emitter is a graviton or a star. `[8Aml1ToQtt4 @ 00:57:55]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **Every Hawking quantum is hard** — the thermal distribution goes like `ω²` at small energy, so it has no pole, and a state of purely hard quanta cannot satisfy the conservation laws. `[GpN8VAauyj8 @ 00:21:30]`, `[GpN8VAauyj8 @ 00:23:38]` — [extra-04](../lectures/extra-04-GpN8VAauyj8-digest.md)
- **There are more symmetries and more soft theorems in electromagnetism than he has shown; the sequencing is a limit of exposition, not of the subject.** `[swrNwD0ypaE @ 00:09:45]` — [L3](../lectures/03-swrNwD0ypaE-digest.md)
- **The graviton Ward identity looks like a two-dimensional stress-tensor Ward identity, but those statements are far less investigated than the `U(1)` current-algebra case.** `[swrNwD0ypaE @ 01:45:55]` — [L3](../lectures/03-swrNwD0ypaE-digest.md)
