<!-- ROLE: round-3 GATE VERIFICATION.  Prior: memory-index-r2.md FAIL(1,2,3) with
     conditional PROMOTE decisions gated on named objections.  Scope: the deltas
     b53809a (docs lane A) and 6f746d5 (checker lane B) against the r2 baseline
     487e7d1.  Every gate fix verified by fresh recomputation, never by reading a
     response table.  Format: rk-light — severity + (a) location + (b) my
     computation + (c) FIX DEMAND + (d) surviving weaker statement. -->

# Verdict: memory-index r3 (gate verification, Opus) — 2026-08-28

Scope: `git diff 487e7d1 b53809a` and `git diff b53809a 6f746d5`; independent
reruns of `memory_index_check.py`, `memory_index_probe.py` and the new
`ansatz_scattering_check.py` in green and every red mode; two independent
recomputation scripts of my own that import nothing from the shard checkers;
lockstep on `claims/CLAIMS.md`, `definitions.md`, `notation.md` and both shards.

---

## 0. Verification record — recomputed, and it CHECKS

Recorded so round 4 does not re-litigate it.

**V1 (obj 1, the three fence surfaces).**  The demanded sentence is present
**verbatim** on all three: `notation.md` `ρ` row (`:270`), `notation.md` `s` row
(`:208`, prefixed "**Fence (r2 objection 1):**"), `definitions.md:582-585`.  I
checked it actually breaks the chain rather than decorating it.  The r2
circularity needed two live assertions: (A) `s=ρ` via H-MQG(2), and (B)
`2s = d-1 ∈ ℕ` via the `s`-row gloss `d=2s+1`.  The fence keeps (A) and denies
(B) as a constraint — "the fully polarised special case and is NOT a constraint
on `ρ` — M-IDX-density (⟨1⟩9) assumes no relation between `ρ` and the on-site
dimension".  Symbol resolution alone therefore no longer delivers `2ρ∈ℤ`: to
run the inference a reader must first establish full polarisation, which no row
asserts.  **Chain broken.**

**V2 (obj 2, AC-EX row vs shard ACE.3).**  Compared character by character
against `theory/ansatz-scattering.md:38-45` and ⟨1⟩7's ASSUME (`:473-476`).
The existence qualifier "**for which Lane T1's outcome measure exists**" is
restored verbatim; `N_T^{ex}`, `H_out^{ex}`, `p_2^{ex}` all carry the `ex`
superscript the notation row exists to protect; the row's "support `{0,2}`" is
weaker than the shard's two-atom formula, and the ledger consequence
`δx_ex=-p_2^{ex}/s` is omitted rather than asserted.  Objection 2's demand is
met.  A *different* hypothesis omission survives — Objection 1 below.

**V3 (obj 3, run in green and red by me).**  `python3 -O
memory_index_check.py` exit **0**, ten rows PASS; `--red` exit **1**, RED-OK,
**10/10 caught**, each with its own message.  `run()` catches `CheckFailure`
per row, and IDX-C7(ii) is a separate registered row, so its red path is
**live**, not dead code behind IDX-C7(i): the red table prints its own
diagnostic (`twisted-transfer defects 0.4793 … and 0.2340 …, |phi_W(2 pi)-1| up
to 1.9979`).  Sub-items:

*(i) Covariance, not counterterm.*  Prong (a) holds the counterterm at the
correct `-ρ` for all three tails and varies only the tensor; the third tail has
density **exactly** `-ρ` (asserted to `1e-9`) and is non-covariant, and the
gauge-invariant defect `max_θ|1-λ_max(E_θ^{ct=-ρ})|` separates it (`0.2340`)
from the true tail (`8.9e-16`).  I rebuilt this from scratch on my own
charge-diagonal tensors: covariant tail at the correct counterterm `4.5e-16`,
same tail at a wrong counterterm `0.591`, and a non-covariant tail of the *same*
density at the correct counterterm `0.141`.  The certificate is genuinely
covariance-sensitive at a fixed correct counterterm.

*(ii) The literal demand was unimplementable — and my r2 demand was the thing at
fault.*  SPEC NOTE 2 claims `φ_W(2π)` is tensor-independent under (INT).  It is,
and I proved it two ways.  Analytically: at `θ=2π`, (INT) makes the on-site
twist the scalar `cI`, so each twisted site factor is `c e^{-2πi ct}` times the
plain one and `φ_W(2π)=c^{|W|}e^{-2πi(ct_L n_L+ct_R n_R)}`.  Numerically: for
**random non-covariant, non-canonical** tensors at `χ=2` and `χ=3`, over four
(window, cut, counterterm) settings, that closed form is reproduced to `1e-8`.
So r2 objection 3(c)(i)'s instruction — "assert that `φ_W(2π)` deviates when the
counterterm is held at the correct `(ρ,-ρ)` and only the tensor's tail
covariance is broken" — asks for a deviation that provably cannot occur.  The
two-prong substitute is the faithful reading and is correctly disclosed.

*(iii) Prong (b) is exact.*  With `n_R=n-cut` and `c=e^{2πiρ}`, the closed form
reduces to `φ_W(2π)=e^{4πiρ n_R}`, which I verified independently to `4.8e-14`
over `n=2..12`, `cut=-2..2`.  Hence the offset vanishes at every window and cut
**iff** `2ρ∈ℤ` — the necessity of ⟨1⟩9.⟨2⟩4 is exact arithmetic, not a
numerical coincidence.  The check also certifies that the charge-shifted
witness family exists: (INT) holds, both tails covariant and injective,
`ρ_a-ρ_b=1∈ℤ` while `2ρ_a∉ℤ`.

*(iv) SPEC NOTE count.*  Seven printed with a COUNT ledger explaining that
`a529a10`'s claimed six were four printed plus two in-code devices (the
deep-shell anti-vacuity guard, IDX-C4's inserted-assertion mutation), now notes
5 and 6.  `a529a10`'s message does say "6 spec ambiguities".  Reconciled.

*(v) IDX-C8rho is non-vacuous.*  I recomputed its constants from scratch:
`min_{|x|≥2}2(1-sinc x) = 1.09070257`, sharp threshold `x* = 1.89549427`
(5.23% slack), `min_{|x|≥1} = 0.31705803`.  The exhibit `μ=(δ_{-1}+δ_{+1})/2` at
`u=1` gives tail mass `0` at threshold `2/u` and `1.0` at `1/u`, so the mutated
claim is `1.0000 ≤ 0.3171`, false — the red catch, verbatim.  Part (c) runs nine
exhibits with strictly positive mass beyond the cutoff (`require(out > 0)`),
worst ratio `1.0907`, so both sides are nonzero.  The χ=2 family's vacuity is
printed as a **VACUITY LEDGER** and guarded by `require(family_mass < 1e-12)`,
which will fire if the family is ever redrawn.  The r2 §2 complaint is closed.

*(vi) Docstring contract.*  `:21-45` now states one named mutation per row,
registers the two-mutation certificates as two rows, names r2 objection
3(c)(i)/(iii) as the reason, and prints the full mutation table.  Residual
imprecision at Finding 8.

**V4 (obj 9 checker half — the shift is genuinely coprime).**  `RED_SHIFT =
(√5-1)/10 = 0.123606798`.  I computed `min_k dist(k·RED_SHIFT, ℤ)` over the
multiplier set `{1..7}` the battery uses: `0.1236 > 0.1`.  The defect it
replaces is real: the probe's `RED_RHO_SHIFT=0.3` on a 10-site window is
`3.0`, `dist = 0` exactly, and the spec's own `0.1` on a 10-site window is
likewise `dist = 0`.  No `(window, cut)` pair is silent (min deviation
`0.7573`), and the asymmetric family shows the n-drift the spec asked for.

**V5 (probe unchanged and still green).**  `memory_index_probe.py` exit **0**,
`--red` exit **1**, `--selftest` exit **0**.  Neither repair commit touched it.

**V6 (T2 checker, all five runs by me).**  `ansatz_scattering_check.py`: green
exit **0**; `--red`, `--red-slow-kernel`, `--red-equal-velocity`,
`--red-absorption` each exit **1**.  The red discipline is stronger than the T1
file's: every mutation registers both the checks it must break **and** the
checks it must leave standing, and an unregistered casualty exits 2.
`--red-absorption` is registered as a fence regression guard and explicitly not
counted as a red test of AC-EX, honouring r1 objection 2 / r2 R9 row 2.
ACE-C1 reproduces the spec's six reference `C(t)` values to better than 0.4%.

**V7 (lockstep — pointerization lost no hypothesis).**  I compared the deleted
merge blocks against the live files.  memory-index.md §8.1 (D26+D27) matches
`definitions.md:1018-1072` except the licensed objection-7 rewording;
ansatz-scattering.md §5 (D28(1)--(5), (D28-C), Remark D28-R) is byte-identical
to `definitions.md:1081-1158` after stripping blockquote scaffolding, including
`C_cl`, `λ̃∈(max(λ_{E_α},λ_{E_β}),1)`, `ε_v`, the two-sided side conditions
`Λ_α⊂(-∞,min(x,x')-r]` / `Λ_β⊂[max(x,x')+r,∞)`, and the full uniformity list
("not on any time parameter").  All fifteen notation rows are live.  The
`D28-P → D28` rename resolves correctly at every citation, including all six
`D28(5)`-family citations, none of which now points at the withdrawn
thresholds.  **No hypothesis was lost and no conclusion strengthened by the
pointerization.**

**V8 (all remaining gate fixes located).**  Objection 4: ⟨1⟩11.⟨2⟩3 now cites
⟨1⟩9.⟨2⟩3 + ⟨1⟩1.⟨2⟩1 with ⟨1⟩10 dropped (`memory-index.md:667-671`), and
`s=ρ` is added to ⟨1⟩12's ASSUME (`:693-695`) and to M-INDEX-LA-strong's
mechanism-B parenthesis.  Objection 5: all three edges landed
(`CLAIMS.md:71,72,75`) and ⟨1⟩7.⟨2⟩3's `briefs/` reference is replaced by the
row id (`ansatz-scattering.md:520-523`).  Objection 6: the AD3-ex row's
displayed limit is character-for-character `ansatz-scattering.md:482`, the
gloss is demoted to a parenthetical, and the last clause is the demanded text.
Objection 7: `definitions.md:1023-1026`, with `ρ=0` admitted and the AKLT
cross-check named.  Objection 9 docs half: `memory-index.md:798-810`, the
demanded text verbatim, and the M-INDEX-fin where-tested cell amended to match.
NOTE 10: verbatim.  NOTE 11: both surfaces, with `ϱ_0` purity disclosed.
NOTE 13: clause (vi) at `ansatz-scattering.md:662-669`, correctly labelled a
normalisation consequence of H-MQG(3).  NOTE 14: re-indexed — but see Finding 5.

---

## 1. Ruling on lane B's finding (obligation 2)

**LANE B IS RIGHT.  The r2 verdict's R9(iii) is wrong, and I am overruling my
own prior text.  The prediction migrates to the majorant object.**

What r2 R9(iii) said: "*ACE-C2 red scalings: correct analytically —
`Σ_{|m|≥R}c⟨m⟩^{-2} ≍ 2c/R` with `R≍ε_vt/2`, so `C_θ ≍ t^{-1}` … so both gates
fail as designed; the `ℓ²`-versus-`ℓ¹` mismatch does not change the scaling
because the kernel tail acts as a scalar multiplier on the cone.*"

What is right and what is wrong.  The **arithmetic** is right, and I reconfirm
it: on my own lattice, `Σ_{|m|≥R}|h_slow|` at `R = 43,87,174,347,695,1390` is
`2.73e-2, 1.33e-2, 6.47e-3, 3.10e-3, 1.40e-3, 5.57e-4` — a clean `R^{-1}`, i.e.
doubling exponent `-1`, against `2.34e-1 → 7.32e-8` for the filtered kernel.
The **attribution** is wrong.  That tail sum is created by the triangle
inequality of ⟨1⟩5.⟨2⟩4(i), which discards the phase; it is a property of the
majorant, not of `C_θ`.  On the literal object the kernel enters as
`ĥ(k)` restricted to the packet's momentum band, and the filter keeps that band
away from `ĥ_slow`'s only singularity at `k=0`.  I verified this directly: on
`k∈[0.65,0.75]`, `ĥ_slow` is smooth (max second difference `5.7e-7`) and
`|ĥ_slow|/|ĥ_γ|` is nearly constant.  A bounded smooth multiplier maps a
`C_c^∞` packet to a `C_c^∞` packet, so the *off-cone* decay that actually
governs `C_θ` survives it and the object is merely rescaled.  The checker's
measurement is the signature: `C_θ_slow/C_θ = 0.298, 0.298, 0.294, 0.292,
0.292, 0.293` — a constant, across five octaves.  The last clause of R9(iii),
"the kernel tail acts as a scalar multiplier on the cone", conflates the
multiplier (which acts on the band and preserves the rate) with the tail sum
(which is an artefact of the discarded phase).

**Consequence, and it is favourable.**  r2's own **R7** already identified the
proof's object correctly: "`‖T_M‖ ≤ C_aΣ_{x,y''}|F_t(x,y'')|S(u)`,
`S(u)=Σ_m|h_γ(m)||θ_c(u)-θ_c(u+m)|`".  ⟨1⟩5.⟨2⟩4(i) integrates the **majorant**,
so the majorant is where kernel decay must be shown load-bearing.  ACE-C2b
measures exactly that and reproduces r2's predicted scalings on it: filtered
tail slope `-6.704`, gates pass; slow-kernel tail slope `-1.295` (heading to the
predicted `-1`), doubling exponents `→ -1.393`, octave ratios `→ 0.747`, **both
gates fail**.  I also checked that ACE-C2b's `M(t)` genuinely dominates the
spec's own object at every time in both modes (green ratios `2.85, 3.08, 2.98,
2.85, 2.79, 2.77`; slow-kernel ratios `2.72 → 158.6`), as a pointwise triangle
majorant of an `ℓ²(x,y)` norm must.  So `M(t)` is not a substituted object of
convenience: it is the spec's own object with the proof's own inequality
applied.

**Does `ansatz_scattering_check.py` satisfy the AC-EX hold condition?  YES.**
The r2 HOLD named one missing step — "the two specified certificates ACE-C1 and
ACE-C2 are not implemented", with the rationale that "ACE-C2's
`--red-slow-kernel` mutation is the only evidence that the Objection-1 repair is
a real gain in decay rather than a re-parameterisation".  That evidence is now
delivered, red-first, on the object the proof's estimate consumes, with the
literal-object mutation registered as dead and asserted so it cannot silently
come back.  The r1 borderline the HOLD pointed at (`C²(𝕋) ⇒ o(m^{-2})` versus
Cook's `Σ_m|m||h(m)|<∞`) is exactly what ACE-C2b's two runs separate.  Two
qualifications are recorded as Findings 4 and 10; neither is the missing step.

---

## 2. Findings

### MAJOR

**Objection 1 — MAJOR.  The AC-EX row asserts ACE.3's conclusion while its own
exhaustive "both" omits ACE.3's third stated hypothesis; the r2 scoping
sentence propagates the same omission.**

(a) `claims/CLAIMS.md:75`, AC-EX row, the (ACE.3) sentence; and
`theory/verdicts/memory-index-r2.md:624-637`, the AC-EX scoping sentence, third
sentence.  Against `theory/ansatz-scattering.md:27-30` (theorem ASSUME) and
⟨1⟩7.⟨2⟩1.

(b) My computation.  The theorem's ASSUME reads: "H-MQG(1)--(3) …, the live
`D28 (H-ACE)` …, and — **for ACE.3 only** — the charge assignment
`q_in=q_L=-1`, `q_T=+1` together with the local-decay hypothesis `(AD3-ex)`".
Three ACE.3-only conditions, and ⟨1⟩7.⟨2⟩1 consumes the charge assignment
directly: "Reflection has `ν=q_L-q_in=0`; transmission has `ν=q_T-q_in=2`".
The row says "(ACE.3) is conditional on **both** the named local-decay
hypothesis **(AD3-ex)** … **and** the existence of Lane T1's ordered-limit
outcome measure".  "Both" is exhaustive and it is false: the charge assignment
is a third, and it is the one that produces the row's headline numbers.
Without it `ν∈{q_L-q_in, q_T-q_in}` is unconstrained, so the asserted support
`{0,2}` is unlicensed by the hypotheses the row lists.  This is precisely the
shape r2 priced MAJOR at its own objection 2 — a row dropping a stated
hypothesis of ACE.3 — and it survived that repair because objection 2's fix
demand was narrower ("restore the existence qualifier and both `ex`
superscripts").  It is pre-existing, not introduced by b53809a; I raise it
because AC-EX is being promoted in this round and a PROVED row must not omit a
hypothesis of the theorem it names.  H-MQG(1)--(3) are likewise absent from the
row and from the scoping sentence, on the same footing.

(c) FIX DEMAND.  In the AC-EX row, replace "conditional on **both** … **and**
…" by "conditional on **all three** of: the charge assignment `q_in=q_L=-1`,
`q_T=+1`; the named local-decay hypothesis **(AD3-ex)**, which this shard does
not prove; and the existence of Lane T1's ordered-limit outcome measure for the
vector in question, which D28 does not supply".  Add "H-MQG(1)--(3) and" before
"D28/H-ACE's" in the row's opening clause.  Because the orchestrator applies the
§4 scoping sentence without paraphrase, §3 below carries an **r3-amended** AC-EX
scoping sentence with the same two insertions and nothing else changed; use that
one, not r2's.

(d) SURVIVING WEAKER STATEMENT.  AC-EX exactly as the shard states it: ACE.1
and ACE.2 under H-MQG(1)--(3) and D28 (incl. D28-C); ACE.3 conditional on the
charge assignment, on (AD3-ex), and on the existence of Lane T1's ordered-limit
measure for the vector in question.

### MINOR

**Objection 2 — MINOR.  The two repair lanes were never reconciled: four live
surfaces describe the pre-`6f746d5` checker, two of them falsely.**
(a) `CLAIMS.md:72` (M-IDX-density where-tested), `:75` (AC-EX where-tested),
`:70`, `:71`, and `theory/memory-index.md:824`.
(b) Lane A wrote the docs at `b53809a`, three hours before lane B landed the
checkers at `6f746d5`, and nothing re-read them.  `:72` still says "the mutation
aimed at the load-bearing two-tail step ⟨1⟩9.⟨2⟩4 is **unreachable** in `--red`,
so the necessity of the antisymmetric pair is **not yet red-certified**" — false
since `6f746d5`; I ran the live red path and it is IDX-C7(ii) (V3).  `:75` still
says ACE-C1/ACE-C2 are "**not yet implemented**" — false; I ran all five modes
(V6).  `:70`, `:71` and `memory-index.md:824` say "RED-OK 8/8" and "IDX-C1--C8
all green"; the file now registers ten rows and reports 10/10.  The first two
understate the evidence, which is the safe direction, but a row about to be
promoted must not carry a false statement about its own certificate.
(c) FIX: strike the `:72` coverage caveat and replace it with the IDX-C7(ii)
citation; replace `:75`'s parenthesis with `theory/checks/ansatz_scattering_check.py`
ACE-C1a/C1b/C2a/C2b (green 0; `--red`, `--red-slow-kernel`,
`--red-equal-velocity`, `--red-absorption` each exit 1); update the two counts
to ten rows / 10-of-10.
(d) Surviving: every claim at its stated strength; only the evidence ledger is
stale.

**Objection 3 — MINOR.  `memory-index.md:821-822` asserts of committed code
that "every red mutation breaks a necessary premise".**
(a) `theory/memory-index.md:821-822`, under the new NOTE-12 heading
"IMPLEMENTED AND COMMITTED".
(b) That sentence was spec text at baseline; under a heading asserting
committed status it becomes a coverage claim, and it remains false for two
rows.  IDX-C4's mutation is an inserted false assertion, not a perturbed
premise — the checker itself now says so in SPEC NOTE 6.  IDX-C7(i)(b)'s
window/cut/kink battery is vacuous at `θ=2π`: by the tensor-independence I
proved in V3(ii), `φ_W(2π)` is a product of scalars, so the identity holds for
arbitrary matrices and the battery tests the counterterm arithmetic only.  Lane
B repaired three of r2's four vacuity findings; this sentence still advertises
all of them as repaired.
(c) FIX: qualify to "every red mutation breaks a necessary premise except
IDX-C4 and IDX-C7(i)(b), whose mutations are an inserted false assertion and a
counterterm-arithmetic perturbation respectively (SPEC NOTES 6 and 1)".
(d) Surviving: the eight rows whose mutations do perturb a premise.

**Objection 4 — MINOR.  The shard's own ACE-C2 spec still states the
prediction lane B refuted, in the imperative.**
(a) `theory/ansatz-scattering.md:575-587`.
(b) §4 reads "*Predicted mechanism (⟨1⟩5.⟨2⟩4 regime (i)):* the dominant factor
is `Σ_{|m|≥ε_v t/2}|h(m)|`" and, for the red run, "so `C_θ(t)≍t^{-1}` … **Both
gates must FAIL.**"  Measured, `C_θ` under the slow kernel has doubling
exponents `[-1.170,-2.334,-2.775,-3.397,-4.424]` and both gates **pass**; the
mechanism is the one I established in §1.  A false testable prediction standing
in a shard that is about to be promoted will send the next reader to "fix" the
checker to match it.  The checker registers the deviation (SPEC NOTE 2) and
asserts the mutation is dead, so the campaign is honest; only §4 lags.
(c) FIX: rewrite §4's predicted-mechanism paragraph to record the red-first
finding — the tail sum governs the ⟨1⟩5.⟨2⟩4(i) majorant, not `C_θ`; ACE-C2a
carries the literal object with the dead mutation asserted, ACE-C2b the
majorant with the live red test — and cite this verdict §1.
(d) Surviving: ⟨1⟩5.⟨2⟩4 and the `|t|^{-3}` majorant, unaffected (r2 R7).

**Objection 5 — MINOR.  The NOTE-14 repair introduces a wrong-sign convention
and redefines a D27 object in the shard (L4).**
(a) `theory/memory-index.md:470-473`.
(b) The new parenthesis reads "`E_{W,t}(·)=α_{-t}(E_W(·))` its Heisenberg
translate".  With `Ψ_t:=e^{-itH}Ψ` and `α_t(A)=e^{itH}Ae^{-itH}`,
`⟨Ψ_t,E_WΨ_t⟩ = ⟨Ψ,e^{itH}E_We^{-itH}Ψ⟩ = ⟨Ψ,α_t(E_W)Ψ⟩`, so the displayed
identity at `:467` needs `E_{W,t}=α_t(E_W)`.  The `-t` also contradicts the same
file at `:159` (`Q̂_{W,c_0}(t)=α_t(Q̂_{W,c_0})`) and `:349`, and the live single
source `definitions.md:1035-1036`.  The identity as displayed is correct under
the live convention; only the gloss is wrong, so no proof step is affected.
(c) FIX: delete the redefinition and point at D27 (L4); if a reminder is wanted,
write `α_t`, not `α_{-t}`.
(d) Surviving: ⟨1⟩8.⟨2⟩2 verbatim under D27's convention (verified at r2 R5).

**Objection 6 — MINOR.  Objection 8's second half did not land.**
(a) `notation.md:267,268,269,272` ("| proposed definitions.md D27; …");
`theory/memory-index.md:354` ("*Justification.* **Proposed** D27(LR2)").
(b) Objection 8's demand was two-part: pointerize the merge blocks **and** "drop
the 'proposed'/'-P' prefixes from the proof text in favour of the live
D-numbers".  The first part is clean (V7); the second leaves five live
references calling a merged definition "proposed", which is exactly the stale
pointer L4 exists to prevent.
(c) FIX: drop "proposed" from the four notation rows and from `:354`.
(d) Surviving: both shards' mathematics unchanged.

**Objection 7 — MINOR.  The AD3-ex row drops the window qualifier ⟨1⟩7 uses.**
(a) `claims/CLAIMS.md:76` ("at fixed `W`") against `ansatz-scattering.md:480`
("For every fixed window `W` **containing the kink core region**").
(b) The row states a strictly broader conjecture than the shard's, so a future
prover would attack more than is needed.  Harmless direction for soundness,
wrong for the DAG.
(c) FIX: restore "containing the kink core region".
(d) Surviving: (AD3-ex) at CONJECTURE as the shard displays it.

**Objection 8 — MINOR.  Two red modes flip an assertion rather than perturb a
premise, and the repaired docstring still says otherwise.**
(a) `memory_index_check.py:24-25` ("each *in place of* the premise it breaks"),
against `check_c4` and `check_c7_ii:810-816`.
(b) In IDX-C7(ii) the mutated objects (`beta_bad`, `beta_nc`, the
charge-shifted family) are computed in **both** modes; green asserts they are
live, red asserts they vanish.  That is the correct structure for a *necessity*
certificate — one cannot perturb a premise of a non-implication — but it is not
what the docstring describes, and SPEC NOTE 6 registers the same pattern for
IDX-C4 only.
(c) FIX: add a clause to the red-mode paragraph naming IDX-C4 and IDX-C7(ii) as
assertion-flip rows, and extend SPEC NOTE 6 to cover IDX-C7(ii).
(d) Surviving: the certificate's content, which V3(i)--(iii) confirms is real.

### NOTE

**NOTE 9.**  `ACE-C2b`'s `M(t) = (Σ_u S(u)²P_t(u))^{1/2}` is the `ℓ²(x,y)`
majorant of the spec's own object — the right choice, since the spec defines
`C_θ` as an `ℓ²(x,y)` norm — whereas r2 R7's displayed majorant is the `ℓ¹`
operator-norm pairing `Σ_{x,y''}|F_t|S(u)`, which carries an extra `O(t²)`.
SPEC NOTE 2 discloses this ("against an O(1) packet norm").  A reader must not
read ACE-C2b's `-4.4` exponent as certifying the operator-norm `|t|^{-3}` rate;
that rate is established by R7's analysis, not by this run.  Worth one sentence
in §4.

**NOTE 10.**  `memory_index_probe.py`'s `RED_RHO_SHIFT = 0.3` is still resonant
with the 10-site windows (`dist(3.0,ℤ)=0`, V4).  Objection 9's advisory half was
referred to the checker lane, which fixed `memory_index_check.py` and not the
probe.  Both surfaces disclose it honestly (`memory-index.md:808-810`, SPEC
NOTE 7).  Carry forward, not a gate.

**NOTE 11.**  Rename artefacts: `ansatz-scattering.md:635` now reads "Every
`D28(6)` of r1 therefore reads `D28(5)` here" — r1 wrote `D28-P(6)`, so the
sentence is false as history; `:606` "the provisional `D28` prefix" is
self-referential after the 48× replacement.  Cosmetic.

**NOTE 12.**  ⟨1⟩11.⟨2⟩3 asserts that "no site-spin symbol `s` and no `s=ρ`
identification enters" while citing ⟨1⟩1.⟨2⟩1, whose *lemma* ASSUME does carry
H-MQG(2).  Sound at leaf granularity — ⟨1⟩1.⟨2⟩1's own justification is "D26 and
the finite-dimensional spectral computation" — and r2 prescribed this citation.
Cleaner: cite D26 directly alongside it.

**NOTE 13.**  The AC-EX row says the measure "has support `{0,2}`" where
⟨1⟩7.⟨2⟩3 gives `p_ν^{ex}=‖P_LW_+^*Ψ‖²δ_{ν,0}+‖P_TW_+^*Ψ‖²δ_{ν,2}`, i.e.
support **⊆** `{0,2}` (either weight may vanish).  Pre-existing; write "support
contained in `{0,2}`".

---

## 3. Gate table (obligation 3)

| obj id (r2) | verdict | basis |
|---|---|---|
| **1** (fence, 3 surfaces) | **CLEARED** | verbatim on all three; chain `ρ→s→d=2s+1` broken (V1) |
| **2** (AC-EX row vs ACE.3) | **CLEARED** | qualifier + both `ex` superscripts restored verbatim (V2) |
| **3** (checker red coverage) | **CLEARED** | all four FIX DEMAND items met; 10/10 red, C7(ii) live, C8rho non-vacuous, docstring corrected (V3) |
| **4** (⟨1⟩11/⟨1⟩12 `s=ρ`) | **CLEARED** | ⟨1⟩10 citation dropped, `s=ρ` in ⟨1⟩12 ASSUME and in the LA-strong row (V8) |
| **5** (three DAG edges) | **CLEARED** | all three landed, plus the ⟨1⟩7.⟨2⟩3 citation swap (V8) |
| **6** (AD3-ex row) | **CLEARED** | displayed limit character-for-character; gloss demoted (V8) — window qualifier at Finding 7 |
| **7** (D26 `ρ>0`) | **CLEARED** | `ρ=0` admitted, AKLT cross-check named (V8) |
| **8** (L4 merge blocks) | **NOT CLEARED** | pointerization clean (V7), but the "proposed"/prefix half did not land — Finding 6 |
| **9** (P2 over-credit) | **CLEARED** | §7(i) and the where-tested cell carry the demanded text verbatim; checker half done with a coprime shift (V4, V8) |
| **N10** | **CLEARED** | verbatim append |
| **N11** | **CLEARED** | ⟨1⟩3b and the row, with `ϱ_0` purity disclosed |
| **N12** | **PARTIAL** | heading and four where-tested cells done; five "proposed" references remain — Finding 6 |
| **N13** | **CLEARED** | clause (vi), labelled a normalisation consequence |
| **N14** | **CLEARED (with defect)** | re-indexed as demanded, but the new convention has the wrong sign — Finding 5 |
| **AC-EX HOLD** | **CLEARED** | ACE-C1/ACE-C2 implemented red-first; the missing step is delivered on the object ⟨1⟩5.⟨2⟩4(i) integrates (§1, V6) |

---

## 4. Promotion table (obligation 3)

Scoping sentences are copied **verbatim** from `memory-index-r2.md` §4 and are
to be appended to the row's statement cell without paraphrase.  The AC-EX
sentence is the one exception and is marked.

| Row | Decision | Gate |
|---|---|---|
| **M-INDEX-fin** | **PROMOTE** SKETCH → **PROVED** | none outstanding (obj 9 cleared) |
| **M-INDEX-spec** | **PROMOTE** SKETCH → **PROVED (conditional)** | none outstanding (objs 4, 5 cleared); apply Finding 5 in the same commit |
| **M-IDX-density** | **PROMOTE** SKETCH → **PROVED** | none outstanding (objs 1, 3 cleared); strike the stale caveat, Finding 2 |
| **AC-EX** | **PROMOTE** SKETCH → **PROVED (conditional)** for ACE.1--ACE.2; ACE.3 stays conditional | **Objection 1 (mandatory)** |
| **M-INDEX-LA-strong** | **CONFIRM REFUTED** | none outstanding (obj 4 cleared) |
| **M-INDEX-LA-folium** | **CONFIRM CONJECTURE** | none outstanding (NOTE 11 cleared) |
| **AD3-ex** | **CONFIRM CONJECTURE** | none outstanding (obj 6 cleared); Finding 7 |

**M-INDEX-fin — PROMOTE.**  Scoping sentence (verbatim from r2 §4):

> Hypotheses in full: D26(INT), H-MQG(2) (which fixes the D13(a) calibration
> parameter `s>0` to be the tail density), a finite window `W=[a,b]` and a cut
> `c_0∈W`; the coset is `κ_{W,c_0} ≡ |W|κ + s(a+b-1-2c_0) (mod ℤ)` and is
> time-independent because `α_t` is a C*-automorphism.  Integrality of the TPM
> increment is offset cancellation at fixed `W` (⟨1⟩5.⟨2⟩3), not spectral
> arithmetic for a difference of noncommuting operators; probe P2 certifies
> `spec Q̂_W ⊂ ℤ` by construction of the observable in the D16 instantiation
> and is an arithmetic, not a dynamical, certificate.

**M-INDEX-spec — PROMOTE, as a conditional implication only.**  Scoping
sentence (verbatim from r2 §4):

> Proved only as the conditional implication: H-MQG(1)--(4) + D26(INT) +
> D27(LR1--LR3, tightness-only) ⟹ every (LR3)-subsequential ordered TPM
> escaped-charge law is a probability on `ℤ` with `δx = -(2s)^{-1}Σ_ν ν p_ν`
> **along that subsequence**; support quantization is subsequence-free, and
> D27's optional convenience clause buys uniqueness of the VALUE `δx` and
> nothing else.  The reduction clause is a further conditional: it additionally
> assumes H-AD-G with D18(AD3) read as weak-* convergence of the window
> restriction, per channel, to the corresponding kink charge eigenstate — a
> reading D18's frozen words do not fix.  D27 is assumed, not derived; no
> implication H-AD-G ⟹ (LR) is claimed; no sector-wide total-charge operator is
> constructed, and its unconditional existence is REFUTED (M-INDEX-LA-strong).

**M-IDX-density — PROMOTE.**  Both gates are closed: the fence breaks symbol
resolution (V1) and the load-bearing hypothesis now has an exact necessity
certificate with a live red path (V3).  Scoping sentence (verbatim from r2 §4):

> Hypotheses in full: D1 injective tensors `A_α,A_β`, D2(a) covariance with a
> common unbroken circle direction `ξ∈𝔥_α∩𝔥_β`, D2(b)'s uniqueness clause, (S)
> of D2(e) at both tails, D26(INT), and the ANTISYMMETRY
> `ω_β(S^z) = -ω_α(S^z) =: -ρ`.  The antisymmetry is load-bearing: one tail
> alone gives only `ρ∈κ+ℤ` and a general tail pair only `ρ_α-ρ_β∈ℤ`; `2ρ∈ℤ`
> needs the antisymmetric pair.  `ρ` is a free real parameter of the vacuum
> pair — `ρ=0` is admitted (the AKLT cross-check) — and no step assumes any
> relation between `ρ` and the on-site dimension `d`; `notation.md`'s `s`-row
> gloss `d=2s+1` is the fully polarised special case and is not imported here.

**AC-EX — PROMOTE for ACE.1--ACE.2, gated on Objection 1.**  The r2 HOLD's
missing step is delivered (§1).  Because r2's scoping sentence itself omits the
charge assignment and H-MQG(1)--(3), use this **r3-amended** sentence — it is
r2's text with two insertions, marked `[r3]`, and nothing else changed:

> ACE.1--ACE.2 are proved only as the conditional implication: **[r3]
> H-MQG(1)--(3) and** D28/H-ACE (exact kink and magnon band maps, covariant
> kink-sector realization, momentum-filtered creator normalisation, velocity
> separation `ε_v>0`, and the displayed **two-sided** two-cluster inequality
> (D28-C)) ⟹ the three Cook limits exist, `W_-^L` and `W_+=W_+^L⊕W_+^T` are
> isometries, and `N_T^{ex}:=W_+P_TW_+^*` is an orthogonal projection on
> `H_out^{ex}:=ran W_+` — D18's `N_T` restricted to that range, with nothing
> asserted on its orthogonal complement.  ACE.3 is conditional on **[r3] all
> three of: the charge assignment `q_in=q_L=-1`, `q_T=+1`;** the named
> local-decay hypothesis (AD3-ex), which this shard does not prove; **and** the
> existence of Lane T1's ordered-limit outcome measure for the vector in
> question, which D28 does not supply.  (D28-C) is the load-bearing hypothesis
> and is unverified on any model; Remark D28-R's threshold inequalities are
> used in no step.  No completeness, raw-band-data implication, bound-state
> exclusion, or soft limit is claimed.

Append, as the evidence clause: ACE-C1 and ACE-C2 are implemented at
`theory/checks/ansatz_scattering_check.py` (green exit 0; `--red`,
`--red-slow-kernel`, `--red-equal-velocity`, `--red-absorption` each exit 1);
kernel decay is red-certified load-bearing on the ⟨1⟩5.⟨2⟩4(i) **majorant**,
not on the literal `ℓ²` defect, which is insensitive to it (this verdict §1);
`--red-absorption` is a fence regression guard and is not a red test of AC-EX;
neither certificate touches (D28-C).

**M-INDEX-LA-strong — CONFIRM REFUTED.**  Mechanism A alone refutes the row as
stated and needs neither (S) nor `s=ρ`; the row now discloses mechanism B's
extra hypotheses, as objection 4 demanded.

**M-INDEX-LA-folium — CONFIRM CONJECTURE.**  NOTE 11's sharpening landed on
both surfaces: the whole content is existence of the implementer.

**AD3-ex — CONFIRM CONJECTURE.**  Nothing of it is proved; the row now says so
and displays the limit verbatim.  Apply Finding 7.

---

## 5. Lockstep spot-check (obligation 4)

**No silent strengthening was introduced by the repairs.**  The pointerization
lost no hypothesis, quantifier or constant (V7); the `D28-P → D28` rename
resolves correctly everywhere, including the six `D28(5)` citations, none of
which reaches the withdrawn thresholds (V7); the one definitional widening —
objection 7's removal of `ρ>0` from D26 — is exactly what the verdict demanded
and what ⟨1⟩9 proves; clause (vi) correctly labels `HΩ_γ=0` a normalisation
consequence of H-MQG(3) rather than a new assumption; and no status was
promoted in either commit, as L5 requires.  The row-level changes are additions
or the demanded rewrites, and the two where-tested changes that move in the
"more evidence" direction are the stale ones of Finding 2, which move it
*back* once corrected.  The defects this round found run the other way: a row
that omits a hypothesis it always omitted (Objection 1), evidence ledgers that
lag their own checkers (Objection 2), and a repair that introduced a
wrong-sign gloss (Objection 5).

---

## 6. Summary

The three r2 MAJORs are closed, and I verified each by recomputation rather
than by reading the response tables: the fence genuinely breaks the
symbol-resolution chain, the AC-EX row's restored qualifier and `ex`
superscripts match ACE.3 character for character, and the checker's red
coverage now reaches the one load-bearing hypothesis it did not — with the
bonus that r2 objection 3(c)(i)'s literal instruction turned out to be
unimplementable, and the substitute the checker lane built in its place is
better than what was asked for.  Lane B's red-first finding is correct and I
have overruled my own R9(iii): the kernel-tail scaling belongs to the majorant,
which is the object the proof actually integrates, and that is where the red
test now lives.  Two adjudicator errors were caught by the repair lanes this
round, which is the loop working in the direction it is supposed to.

What is left is one MAJOR — a hypothesis the AC-EX row has always omitted,
which matters now only because the row is being promoted — and a cluster of
bookkeeping defects created by running two repair lanes in parallel without a
reconciliation pass.  All are cheap.

Objection counts: **1 MAJOR (1), 7 MINOR (2--8), 5 NOTE (9--13).  0 FATAL.**
Trajectory across the campaign: 20 (r1, three verdicts) → 14 (r2) → 13 (r3),
with the MAJOR count 6 → 3 → 1 and the residue no longer in the mathematics.

Final line: **FAIL(1)** — no FATAL; every r2 gate objection except the second
half of objection 8 is CLEARED and the AC-EX HOLD is lifted, so six of the
seven promotions apply as written the moment the repair commit lands, and
AC-EX's applies once Objection 1's two insertions are made.
