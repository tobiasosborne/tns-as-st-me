<!-- ROLE: adversarial r1 critic verdict on theory/soft-index.md (Lane S1-A,
     codex prover, Theorem S-INDEX).  Work order: briefs/soft-critic-r1.md.
     Writable file of this lane: this file ONLY.  No shared file was edited;
     every computation below was run on private copies in the scratchpad. -->

# r1 verdict — `theory/soft-index.md` (Lane S1-A, S-INDEX)

> **ORCHESTRATOR ERRATUM — appended 2026-08-28, bd `tns-uxr`.  The verdict
> below is NOT rewritten; this annotation narrows two clearances in it.**
>
> The downstream audit (`verdicts/ml4-ward-n2-audit.md`) found that this
> verdict's clearance items (C-d) and §5, and objection M6(d), are **over-broad**
> with respect to the ML4-Ward `n≥2` defect: they clear uses of the projected
> current at general `n` on the strength of `n=1` checks.  An over-broad
> clearance in a verdict is more damaging than a defect in a shard, because it
> is what the next session cites.  Read those three items as scoped to `n=1`.
> The `n≥2` statement sites in `theory/soft-index.md` and
> `theory/soft-index-b.md` are enumerated in the audit's §2.3/§2.4 and are
> repaired by the unified r2 rewrite (`tns-v44`), not by editing the two
> superseded lane records.



**Verdict: FAIL(F1, M1–M8).**  1 FATAL, 8 MAJOR, 9 MINOR, 6 NOTE.

## 0. What I did (obligations 1–5)

**Recomputed, not refereed** (private scripts, scratchpad only; nothing in
`theory/checks/` or any shared file was touched):

* **(C-a) The D6 contact equation (R16) re-derived from scratch.**  I set up
  the two-magnon problem in the relative coordinate independently
  (`psi(x,y)=e^{iK(x+y)/2}phi(r)`, exact hard-core lattice equations, defect
  equations at the separations where the free ansatz fails) and solved for
  `A_12/A_21`.  At nearest-neighbour coupling my condition reduces **exactly**
  to (R16): `A(2z_2−z_1z_2−1)+B(2z_1−z_1z_2−1)=0`, and numerically
  `|mine − closed form| ≤ 9.4e−16` over `k_h∈{0.7,1.3,2.0}`,
  `k_s∈{0.05,0.2,−0.3}`.
* **(C-b) (R17)/(R18) Taylor coefficients** (shard step ⟨1⟩8.⟨2⟩1):
  `a_1 = +2.000000i`, `a_2 = −2.000000 + i·cot(k_h/2)` (max deviation
  `1.1e−4` at `k_h=0.6`, `1.2e−5` elsewhere), `arg s = 2k_s + cot(k_h/2)k_s²`.
  **Shard ⟨1⟩8.⟨2⟩1 is exactly right.**
* **(C-c) S2-2body-S closed form**: `∂_{k_s}arg S_12|_0 = 1/S` to `1e−6` for
  `S∈{1/2,1,3/2,2}` and every `k_h∈{0.7,1.2,1.8,2.4}`.
* **(C-d) The spin-S Ward package (SIDX.3), (SIDX.7)–(SIDX.9), SIDX-W2** —
  built `H`, `Q_0`, `J^-_0=Σ_x(−[h_{x,x+1},S^-_x])`, `J^z_0` directly in the
  deficit sectors of the **general** SU(2)-invariant bond
  `h=−J(S_i·S_j−S²)−b((S_i·S_j)²−S⁴)`, rings `N=8,10`, `S∈{1/2,1,3/2}`,
  `b∈{0,±0.1}`.  All to machine precision:
  `‖Q_0ψ‖²=2m_λ` (`m_λ=NS−1`), `‖P J^-_0 − Q_0J^z_0/m_λ‖ ≤ 1.2e−15`,
  `‖J^z_0|h⟩ − i v_S(h)|h⟩‖ ≤ 1.2e−15`, `⟨h|Q_0^†P J^-_0|h⟩ = 2i v_S(h)`
  exactly, `N^{-1}‖Q_0|Ω⟩‖² = 2S = 2ρ` exactly.
  **(S-IDX.0)'s algebra is correct and does generalise as the shard says.**
* **(C-e) Two falsification attempts on the LAW itself** (obligation 1,
  "construct counterexamples where the quantifiers permit them").  H-SIDX(1)
  quantifies over SU(2)-invariant ferromagnetic vacua, not over D6.  I built
  two families inside that quantifier that change the two-magnon contact
  dynamics while leaving `2ρ` and the Ward residue `2iv_h` untouched:
  (i) spin-1/2 with an extra ferromagnetic NNN coupling `J_2`
  (`ω(k)=J_1(1−cos k)+J_2(1−cos 2k)`; exact 4th-order recursion, evanescent
  root included; lattice-equation residuals `≤8.1e−16` at `r=1..8`);
  (ii) spin-`S` with a biquadratic term (`b∈[−0.25,0.25]`, `S∈{1,3/2,2}`).
  **Result: the slope is EXACTLY `1/ρ` in every case** (`2.000000` for all
  `J_2∈{0,0.05,0.1}`; `1.000000`, `0.666667`, `0.500000` for `S=1,3/2,2` at
  every `b`), `|S_12|=1` to `1e−10`, hard-momentum-independent.
  **The law survives both attacks.**  This is recorded in the shard's favour
  (L10) and it is why F1 below is an objection to the *derivation*, not to
  the *statement*.
* **Checker audit.** `python3 theory/checks/soft_index_probe.py --selftest`
  → `selftest PASS`, exit 0 (re-run by me).  Frozen P1–P4 semantics read from
  the probe source and compared with the shard's §6 CHECKER SPEC (see M7, N3).
* **REFUTED-row audit.**  ML5 (unrestricted): not contradicted — the shard
  quantifies over the hard process only and re-admits sources solely through
  ML5-A with both D24(c) zeros (⟨1⟩7); `O_η` and `V_int` survive (⟨1⟩7.⟨2⟩2)
  ✓.  Old label `S2`: not used; the shard cites `S2-2body`, `S2-2body-S` and
  "the EXPLORATION box of soft-current-recon.md ⟨1⟩6" ✓.  `M-INDEX-LA-strong`:
  unused ✓.  ML4's refuted volume-uniformity: D30(3) explicitly disclaims it ✓
  (but see M3).  `G0-soft-r1`: **cited but not respected** — see M4.

---

## 1. FATAL

### F1. The entire quantitative content of (S-IDX.1)(ii) is a stipulation inside D29(5); its only support is the anchor it is then said to "match"

**(a) Location.** `theory/soft-index.md` §7.1 **D29 clause 5** ("Normalizing
the Goldstone leg by this `2ρ_λ` norm fixes, independently of the hard
process, `L_λ(0,h)=−i sgn(v_h−v_s)/(2ρ_λ v_h)`"), used at ⟨1⟩2.⟨2⟩4
(SIDX.10), carried into ⟨1⟩5.⟨2⟩1 (SIDX.4)/(SIDX.5) and into
§0 (S-IDX.1-spec); leaf justification "named computation **SIDX-FLUX**".

**(b) My computation.**

1. *The leaf does not exist.*  `grep -rn "SIDX-FLUX\|SIDX-JET\|SIDX-W1\|
   SIDX-W2\|SIDX-OFFSET\|SIDX-LEGNORM" theory/ numerics/` returns **nothing**.
   None of the shard's six "named computations" is implemented anywhere, and
   §6's CHECKER SPEC does not schedule `SIDX-FLUX` or `SIDX-LEGNORM` either
   (M7).  In this repo a *named computation* is an implemented, recorded
   checker row (ML4-Q1, ML5-I1, IDX-TPM.1, ACE-C1a…).  Under L6b the single
   most load-bearing leaf of the shard is unjustified.
2. *The step is not derivable from what precedes it.*  ⟨1⟩2.⟨2⟩4's stated
   justification is "`e^{ik}−1=ik+O(k²)` and the exact cancellations above".
   The exact cancellations above are (SIDX.6)–(SIDX.8): divide by `N−2n`,
   multiply by `‖Q_0|h⟩‖²=N−2`.  They cancel to `2iv_h` and produce **no**
   `ρ`.  Everything `ρ`-dependent in the theorem enters through the asserted
   value of `L_λ(0,h)` and nowhere else.
3. *A one-parameter counterexample inside the shard's own hypotheses.*
   Replace `L_λ ↦ μ L_λ` for any constant `μ>0`.  D29(1)–(4),(6) are
   untouched; D30(1),(3),(4) are untouched (they constrain `Γ_*,J_*,U_*,ρ_λ,
   ℓ_λ`, not the flux value); only D30(2)'s clause "with D29(5)'s value at
   zero" fails.  The conclusion becomes
   `∂_k arg(1+𝗌_*)|_0 = μ·sgn(v_h−v_s)ℓ_h/ρ` — **an arbitrary number**.
   Hence the jet VALUE is pinned by exactly one clause, and that clause is an
   assertion.  (Lane B reaches the same negative conclusion by a different
   route — see X7 — and my deformation is its constructive form.)
4. *The stated rationale is off by a square root.*  "Normalizing the
   Goldstone leg by this `2ρ_λ` norm" cannot produce `1/(2ρ)`.  I verified
   `‖Q_k|Ω⟩‖² = 2ρN` for every `k` and every `S` (C-d).  The soft leg occurs
   **linearly** in `M_2` and not at all in `M_1`, so normalising it to a unit
   external magnon divides by `‖Q_k|Ω⟩‖=(2ρN)^{1/2}` — **one** power of
   `(2ρ)^{1/2}`, not `2ρ`.  D29(3)'s norm-projection `⟨M_1,M_2⟩/‖M_1‖²`
   supplies the second power for the *hard* leg only.  The rationale sentence
   is therefore wrong as stated even though the value it asserts is right.
5. *The value is right, and I can say why the shard cannot claim credit for
   it.*  From (C-c)/(C-e) the physical slope is `1/ρ` across three model
   families; combined with the `b`- and `J_2`-independent Ward residue
   `2iv_h` (C-d) and the kinematic `ik`, the flux factor **must** be
   `−i·sgn/(2ρ v_h)`.  But in the exact route the `1/ρ` comes from the
   **contact equation** (my (C-a); at spin `S` from `μ=(2S−1)a+b` in
   S2-2body-S), i.e. from dynamics, not from a leg normalisation.  Asserting
   that a normalisation reproduces the contact algebra is a substantive
   unproved lemma, and it is the lemma this campaign was supposed to supply.
6. *The anchoring is circular.*  §0 (S-IDX.3-anchors) and ⟨1⟩8 present
   S2-2body (`2` at `ρ=1/2`) and S2-2body-S (`1/S` at `ρ=S`) as consistency
   checks ("any mismatch is a FATAL bug").  Those are precisely the two data
   points that determine the one free constant in D29(5).  A hypothesis fitted
   to an anchor cannot then be certified by that anchor.

**(c) FIX DEMAND.**  Either (i) **derive** `L_λ(0,h)` from D29(1)–(4) — i.e.
prove the missing lemma "charge-created soft-leg amputation contributes the
per-site leg density `2ρ` to the external flux", with a displayed
LSZ/normalisation computation and a red-certified checker (Lane B's proposed
`SIB-C3 --red-legnorm` is the right shape) — or (ii) **demote**: state
S-INDEX-spec as "jet `= sgn(v_h−v_s)·ℓ_h·(2ρ)^{-1}·(2 v_h)·|L(0,h)|`, with
`L(0,h)` an explicitly assumed datum of D29", drop every claim that the law
is *pinned* by symmetry, and move the `1/ρ` into HONEST STATUS as an
assumption calibrated on S2-2body(-S).

**(d) SURVIVING WEAKER STATEMENT.**  *Under H-SIDX + D29 + D30, every limit
point of the datum family satisfies `𝗌_*(k;h) = (e^{ik}−1)L(0,h)·2iv_hℓ_h +
O(k²)`; in particular the jet exists, is hard-independent whenever
`L(0,h)v_h` is, and vanishes to first order iff `L(0,·)≡0`.  The VALUE
`sgn(v_h−v_s)ℓ_h/ρ` holds iff `L(0,h) = −i sgn(v_h−v_s)/(2ρ v_h)`, which is
assumed, not derived.*  (Independently: that value is correct — verified here
against S2-2body, S2-2body-S, an NNN family and a biquadratic family — so the
missing lemma is true and worth proving.)

---

## 2. MAJOR

### M1. D29(5) silently redefines the frozen D24(d) clause-3 constant; the collision is real and is a correction to a frozen definition

**(a) Location.** §7.1 D29(5) vs `definitions.md` D24(d)3
(`L(0,h) = −iχ/v_h`), and `theory/ml5-universality.md` ⟨1⟩3 hypothesis 3 /
equation (6).  Also §0 (S-IDX.2-source) + (SIDX.17), which import the D24
normalisation into the same shard.

**(b) My computation.**  D24(d)3 + ML5-B(6) give, for **every** model in the
class, `M_2 = 2iχ k M_1 + O(k²)`, i.e. phase slope `2χ`.  My (C-c)/(C-e)
computations give slope `1/S` — `1.000000` at `S=1`, `0.666667` at `S=3/2`,
`0.500000` at `S=2`.  So D24(d)3's frozen value is compatible with the PROVED
row S2-2body-S **only at `ρ=1/2`**; at any other density the class `𝒮_W` is
empty as frozen.  The shard's `L_λ` is the corrected constant, but it is
introduced under a new subscript with no statement that it differs from
D24(d)3, and the same shard then uses the uncorrected D24 normalisation in
(SIDX.17).  Under L4 (one symbol, one definition) this is a defect; under L10
it is a suppressed finding.

**(c) FIX DEMAND.**  Add a displayed line: "D29(5)'s `L_λ(0,h)` differs from
D24(d)3's `L(0,h)` by the factor `1/(2ρ)`; D24(d)3 is a `ρ=1/2` statement and
`𝒮_W` as frozen is empty for `ρ≠1/2`" — and route it into MERGE PROPOSALS as
an amendment to D24(d)3 (or as an explicit fence).

**(d) SURVIVING WEAKER STATEMENT.**  *At `ρ=1/2` the two normalisations agree
and the shard's ⟨1⟩7 bridge is consistent; for `ρ≠1/2` the shard's law and
D24(d)/ML5-B are inconsistent normalisations of the same object, and only the
shard's is compatible with PROVED S2-2body-S.*

### M2. Nonvacuity: not one instance of the D29 datum is exhibited, and ⟨1⟩6.⟨2⟩1 substitutes a different object

**(a) Location.** ⟨1⟩6.⟨2⟩1–⟨2⟩2 (vacuous-truth fence); §7.1 D29(1),(3).

**(b) My computation.**  ⟨1⟩6.⟨2⟩1 offers two things: (i) "(S-IDX.0) has
instances on every D6 ring" — true, but (S-IDX.0) is the Ward identity, not
the datum; (ii) "S2-2body and S2-2body-S give exact stationary multiplier
instances" — these are statements about `S_12`, a *different object* from
`𝗌_λ = ⟨M_1,M_2(k)⟩/‖M_1‖²`.  The shard never computes `𝗌_λ` at a single
index `(N,W,T,σ,ς)`, never bounds it, never exhibits a nonzero value.  D29(1)
defines it through unnamed "window-local preparation/resolution matrices"
followed by `Π_{N,T}` and momentum filters; no formula is given, so I could
not compute it either.  This matters beyond hygiene: with `T→∞` taken at
**fixed** `W` (D29(6)), the hard packet has left the window before the
readout, and the connected pairing may be zero.  If it is, the theorem is not
vacuous but **false**: (SIDX.4) asserts a *nonzero* slope `ℓ_h/ρ`, while
`𝗌_*≡0` satisfies D30(1)'s only nondegeneracy clause (which constrains the
*hard* denominator `‖M_1‖`, not `M_2`).  Nobody currently knows which.

**(c) FIX DEMAND.**  Display the D29 datum as an explicit finite matrix
expression (as Lane B does in its (B3)), and either compute one numerical
instance on a D6 ring showing `𝗌 ≈ 2ik`, or state in ⟨1⟩6 and in the claims
rows that no instance of the D29 datum has been exhibited at any index.

**(d) SURVIVING WEAKER STATEMENT.**  *(S-IDX.0) is nonvacuous (I verified it
on rings `N=8,10` at `S∈{1/2,1,3/2}`).  For (S-IDX.1) the honest scope is:
constraint on limit points of a family not yet shown to be nonzero at any
index.*

### M3. D29(6) un-smears the soft leg before the soft limit (`ς→0` at fixed `k`, then `k→0`), contradicting the campaign's own load-bearing-smearing clause and the frozen P3 semantics

**(a) Location.** §7.1 D29(2) (`f_{k,ς}(p)=ς^{-1/2}f((p−k)/ς)`), D29(6)
("then `ς→0` at fixed nonzero carrier `k`; and `k→0` strictly last"),
⟨1⟩5.⟨2⟩5 (SIDX.14), ⟨2⟩6 (SIDX.15).

**(b) My computation.**  The campaign's soft leg is `f_ε(k)=ε^{-1/2}f(k/ε)`
(D24(b), `ml4-ward-reduction.md` (1), and the target brief): **one** soft
scale, packet width tied to the soft momentum.  The shard instead introduces
two independent soft parameters (carrier `k`, width `ς`) and sends `ς→0`
first.  After `ς→0` at fixed `k≠0` the insertion is a **plane-wave** soft
charge `Q_k` in infinite volume — exactly the unsmeared object the brief
declares refuted-in-the-fixed-`N`-register and whose infinite-volume control
is open ML3.  Consequently (SIDX.15)'s immunity is a *rule about which limits
may be written*, not a property of the object: the shard's `𝒜_{N,W,σ}(k)` is
perfectly well defined at `k=2π/N` and fixed `N`, and nothing but the ordering
clause forbids evaluating it there.  Compare the frozen probe: P3 certifies a
**fixed-width** (`ς=0.2`) smeared datum staying bounded (`max/median = 1.39`)
while the raw `k=2π/N` object grows by `20.5`; it certifies nothing after
`ς→0`.  The shard's own CHECKER SPEC item 3 asks only for the fixed-width
statement, so the `ς→0` stage is unsupported by both proof and probe.

**(c) FIX DEMAND.**  Either tie the width to the soft scale (`ς=ε`,
`f_ε(k)=ε^{-1/2}f(k/ε)`, one parameter, as D24(b) and the brief prescribe), or
prove that the `ς→0` limit at fixed `k` exists in infinite volume (that is
ML3) and say so.

**(d) SURVIVING WEAKER STATEMENT.**  *The theorem holds for the fixed-width
smeared datum at width `ς>0`, with the jet taken in the carrier `k`; the
`ς→0` stage of D29(6) is unproved and is not certified by P3.*

### M4. The G0-soft-r1 fence is cited but not respected: in the descendant channel the Adler zero *is* the bare `(e^{ik}−1)`, and ⟨1⟩3.⟨2⟩2 contradicts ⟨1⟩2.⟨2⟩4

**(a) Location.** ⟨1⟩3.⟨2⟩2 ("neither `e^{ik}−1` nor the Ward projection
alone proves an Adler zero") vs ⟨1⟩2.⟨2⟩4 (SIDX.10) and ⟨1⟩5.⟨2⟩3
(SIDX.13).

**(b) My computation.**  (SIDX.10) reads
`(e^{ik}−1)·L_λ(0,h)·[2iv_hℓ_λ(h)]`.  `L_λ(0,h)` is `O(1)` and
`[2iv_hℓ]` is `O(1)`; the vanishing at `k=0` therefore comes from the bare
difference factor and from nothing else.  That is exactly the inference the
REFUTED row `G0-soft-r1` withdraws ("hard data can enter at `O(k)` through
`J_k`").  What in fact rescues the shard is a *different* statement — that the
**orthogonal** channel is `O(k²)` (ML4-A / (SIDX.12)) so that no competing
`O(k)` term exists — but that is a remainder statement, not the origin of the
zero.  (SIDX.13) then displays two objects as "the" ingredients of the zero:
`ω(k)/(e^{ik}−1)Q_k` and `Γ_*^†(1−P_*)J_*`.  The first belongs to (R10)'s
*charge/contact* split of `J^-_k`; the datum's split in D29(4) is
*descendant/orthogonal*.  These are two different decompositions of two
different objects, and the display silently identifies them.  I checked
(SIDX.11) itself: `ω(k)/(e^{ik}−1)=(J/2)(e^{−ik}−1)` ✓, and at spin `S`
`ω_S(k)/(z−1)=JS(z^{−1}−1)` ✓ — the identity is right, its role here is not.

**(c) FIX DEMAND.**  Rewrite ⟨1⟩5.⟨2⟩3: state that the descendant channel's
zero is the kinematic factor, that the fence's content is the absence of a
competing `O(k)` term, and that this absence is D30(3)+ML4-A — then delete or
re-derive (SIDX.13)'s first entry, which belongs to a different split.

**(d) SURVIVING WEAKER STATEMENT.**  *`𝗌_*(0)=0` holds because the descendant
channel carries the factor `(e^{ik}−1)` and the orthogonal channel is
`O(k²)` by D30(3)+ML4-A; the shard's claim to have derived the zero from a
current/contact cancellation rather than from the bare factor is withdrawn.*

### M5. D29(4) makes D24(d)'s exhaustive-LSZ clause true "by definition", and contradicts D29(2)'s own retained boundary terms; `Γ_λ` is used but never defined

**(a) Location.** §7.1 D29(4) ("The pairing is, by definition of PROTO, the
exact sum of its descendant and `R_λ(k)` components; there is no arbitrary
direct soft-source contact… The finite preparation/resolution maps determine
`Γ_λ(k)`") vs D29(2) ("D10's exact summation by parts, **including both
boundary gradients of the truncated profile**… no boundary term is dropped");
used at ⟨1⟩5.⟨2⟩2.

**(b) My computation.**  (i) *Three components, not two.*  G0(e) gives
`[H,Q[f]] = Σ_x(Δf)(x)j_{x|x+1}` for the **untruncated** profile.  For
`Q_W[f]` the forward difference of `f·1_W` contributes, besides `(Δf)1_W`,
two boundary jumps `±f(∂W)j_{∂W}` which are `O(1)` in `k` — they carry no soft
zero (this is the same phenomenon as G0(c)'s two `Θ(1)` boundary window
vectors and D12's `𝔅_Λ`).  D29(2) says these are kept; D29(4) says the pairing
is exactly descendant + `R_λ`.  The two clauses are inconsistent, and the
missing third component is precisely the one with no `k`-smallness.
(ii) *A definition cannot buy a theorem.*  D24(d) clause 1 is, in
`ml5-universality.md`'s own words, "the extra LSZ/contact content beyond the
fixed-volume Ward reduction", and EXPLORATION ML5-W records that it has been
derived for no microscopic class.  D29(4) asserts it of a concrete
finite-volume object; whether the concrete windowed, filtered pairing really
has no further reduced term is a *theorem about the model*.
(iii) *`Γ_λ` is undefined.*  "The finite preparation/resolution maps determine
`Γ_λ(k)`" names no map.  ⟨1⟩5.⟨2⟩2 then leans on (SIDX.12), whose hypotheses
are about `Γ_*`.  The identity "orthogonal contribution to `𝗌_λ` =
`(e^{ik}−1)Γ_λ(k)^†R_λ(k)` / normalisation" is never displayed — the second
load-bearing object of the shard is as undefined as the first (F1).

**(c) FIX DEMAND.**  Display `Γ_λ(k)` explicitly; display the three-term
decomposition of the windowed pairing including the `∂W` gradient terms, with
an estimate showing they vanish in the stated order; and demote D29(4) from a
definition to a named hypothesis (PROTO-LSZ) with the D24(d)1 cross-reference.

**(d) SURVIVING WEAKER STATEMENT.**  *If the windowed pairing decomposes
exactly into descendant + orthogonal-current with `Γ_λ` as in ML4-A and the
`∂W` terms vanish in the stated order, then ⟨1⟩5.⟨2⟩2 follows.  Each of those
three "ifs" is an unproved hypothesis about the concrete object.*

### M6. Lockstep: "the `N−2n → N−2 → 2ρ` cancellation is unconditional" is stronger in the summary than in the proof; and the claims row makes the finite identity depend on D29

**(a) Location.** §8 HONEST STATUS 1; §1 closing line; §7.2 row
`S-INDEX-fin` (`depends on: D10, ML4-Ward, D29`); ⟨1⟩2's PROVE line; target
brief (S-IDX.0) ("UNCONDITIONAL … it alone is publishable").

**(b) My computation.**  Of the three factors, two cancel by arithmetic —
`(1/(N−2n))·(N−2) = 1` at `n=1`, which I verified as an identity and
numerically (C-d) — and the third, `2ρ`, is not a cancellation at all but the
stipulated normalisation of F1.  Calling the chain "unconditional" therefore
overstates the proof by exactly the disputed factor.  Separately: ⟨1⟩1,
⟨1⟩2.⟨2⟩1–⟨2⟩2 and ⟨1⟩3 use only D6/SU(2) algebra + (R10)/(R15) and **are**
unconditional; ⟨1⟩2.⟨2⟩3–⟨2⟩4 use D29.  The claims row nevertheless attaches
D29 to the whole of ⟨1⟩1–⟨1⟩3, which surrenders the one rung the target brief
asked to be delivered clean.  ⟨1⟩2's PROVE line ("The `N−2n`, `N−2`, and `2ρ`
factors enter as follows") is also not a proposition, contra L6b.

**(c) FIX DEMAND.**  Split the row: `S-INDEX-fin` = ⟨1⟩1 + ⟨1⟩2.⟨2⟩1–⟨2⟩2 +
⟨1⟩3, depends on D10/ML4-Ward only, **no D29**; move ⟨1⟩2.⟨2⟩3–⟨2⟩4 into the
conditional row.  Restate HONEST STATUS 1 as "(SIDX.3) and the
`(N−2n)·(N−2)` cancellation are unconditional; the `2ρ` normalisation is
assumed".

**(d) SURVIVING WEAKER STATEMENT.**  *Unconditional: `D^†D=2m_λ`,
`P_λJ^-_0=Q_0J^z_0/m_λ`, `⟨h|Q_0^†P J^-_0|h⟩=2iv_h`, `N^{-1}‖Q_0|Ω⟩‖²=2ρ` —
all four independently verified here at `S∈{1/2,1,3/2}` and for a
biquadratic-deformed SU(2) chain.  Conditional: everything containing `L_λ`.*

### M7. The CHECKER SPEC certifies nothing the theorem claims; the one novel factor is untestable on the models it specifies

**(a) Location.** §6 ⟨1⟩10 items 1–3.

**(b) My computation.**  Item 1 tests (SIDX.6)–(SIDX.8) — already PROVED
(ML4-Ward) and already covered by `ml4_check.py` (Ward/projection residuals
`8.9e−16`, `3.5e−15`).  Item 2 tests (SIDX.11) = (R10) — already covered by
`soft_current_recon_check.py` (max residual `1.56e−14`).  Item 3 tests the
ML4-Q1 growth vs a bounded smeared datum — already the frozen P3.  **No item
computes `𝗌_λ`, its Adler zero, its slope, `ρ_λ`, `ℓ_λ`, or `L_λ`.**  All
three items are specified on D6 rings, where `2ρ=1`, so the single factor that
distinguishes this theorem from ML5-B is invisible by construction: mutating
`2ρ_λ → ρ_λ` in D29(5) would change nothing that item 1–3 measure, i.e. the
load-bearing step has **no red path**.  The pre-registered P1 does measure
`1/S` (`1.9929` at `S=1/2`, `1.0217` at `S=1`), but by a dynamical phase
readout of `arg S_phys`, not through the D29 construction — so P1 certifies
the *law*, never the shard's *route* to it.  (I re-ran `--selftest`: PASS.)

**(c) FIX DEMAND.**  Add a spin-`S` item: compute `N^{-1}‖Q_0|Ω⟩‖²`, the
residue `⟨h|Q_0^†PJ^-_0|h⟩`, and the reconstructed jet
`|(e^{ik}−1)L(0,h)2iv_hℓ|/k` for `S∈{1/2,1,3/2}`, with the red mutation
`2ρ→ρ` (predicted jet doubles, comparison with the P1 slope must FAIL).
Implement the six named computations or delete the names.

**(d) SURVIVING WEAKER STATEMENT.**  *§6 as written is a regression guard for
already-PROVED rows plus the frozen P3; it provides no certificate for any
step of §§2–5.*

### M8. The general-`ρ` theorem rests on a spin-`S` step that is stated only for D6 and justified by a nonexistent computation

**(a) Location.** ⟨1⟩2.⟨2⟩2 (SIDX.7)–(SIDX.8) are D6-only (`N−2`);
⟨1⟩2.⟨2⟩3 asserts the spin-`S` case ("For every primitive spin-`S` magnon,
the direct D10 bond computation `J^z_0|h⟩=iv_S(h)|h⟩` gives `ℓ_λ=1`
(**SIDX-W2**)"); (SIDX.4)/(SIDX.5) are then stated for general `ρ`.

**(b) My computation.**  I verified the assertion by direct construction of
`J^z_0` from `−[h_{x,x+1},S^z_x]` — for `S∈{1/2,1,3/2}` and for
`b∈{0,±0.1}`, `‖J^z_0|h⟩ − i v_S(h)|h⟩‖ ≤ 1.2e−15`, and `‖Q_0|h⟩‖² = 2(NS−1)`
exactly (so the D6 value `N−2` is the `S=1/2` case of `2m_λ`).  **The claim is
true.**  But the shard proves none of it: it displays only the `S=1/2`
numbers, cites a computation that does not exist, and never displays the
general `‖Q_0|h⟩‖² = 2m_λ = 2(ρN−n)` line that would make the bookkeeping
`ρ`-explicit.  A theorem whose conclusion is `ℓ_h/ρ` cannot leave its
`ρ`-carrying step at the level of an unimplemented name.

**(c) FIX DEMAND.**  Display `‖Q_0ψ‖² = 2m_λ = 2(ρN−n)` and
`⟨h|J^z_0|h⟩=iv(h)` with a real derivation (the cleanest is G0(e) at profile
`e^{ikx}` on the ring plus the removable `k=0` value — Lane B's ⟨1⟩2.⟨2⟩3
route), or restrict (SIDX.4) to `ρ=1/2`.

**(d) SURVIVING WEAKER STATEMENT.**  *(SIDX.7)–(SIDX.8) are proved at
`S=1/2`; their spin-`S` form is true (verified here) but unproved in the
shard.*

---

## 3. MINOR

**m1 (⟨1⟩4, SIDX.12).**  The bound mixes trace and operator norms without
saying so.  I re-derived (SIDX.12): `Γ_*(k)^†R_*(k) = [Γ_*(k)−U_*]^†R_*(0) +
Γ_*(k)^†[R_*(k)−R_*(0)]`, `U_*^†R_*(0)=0`, `‖1−U_*U_*^†‖=1`, giving
`‖·‖_1 ≤ (C_Γ‖J_*(0)‖_∞ + C_J sup‖Γ_*‖_∞)|k|` and then `|e^{ik}−1|≤|k|`.
**The lemma is correct**, but Hölder for Schatten norms must be named, and
`sup_k‖Γ_*(k)‖` (used in the statement) is not a D30 hypothesis — it follows
from D30(3) as `≤1+C_Γε`; say so.  *Fix:* label the norms; add the one-line
bound on `sup‖Γ_*‖`.

**m2 (D30(1) vs SIDX.4, SIDX.16).**  D30(1) gives limit points on a
**punctured** soft neighbourhood, so `𝗌_*(0)` is not defined by the limit;
(SIDX.4)'s "`𝗌_*(0;h)=0`" and (SIDX.16)'s "`M_{2,j}^O(0)=0` … passes to each
D30 limit point" both need the value at `0` to be the continuous extension.
*Fix:* define `𝗌_*(0):=lim_{k→0}𝗌_*(k)` once, and note that the intercept
condition is imposed per-index, not in the limit.

**m3 (D30(2) vs D30(4), ⟨1⟩5.⟨2⟩7).**  The quantifier on `ρ,ℓ_h` in D30(2)
is unstated.  Read as `∃ρ ∀` cluster points, D30(2) already delivers
commonality and D30(4) is redundant; read as `∀ ∃`, ⟨2⟩7's appeal to D30(4)
is right.  *Fix:* state the quantifier explicitly (D27's clause 3 is the
model).

**m4 (H-SIDX(1), §8.4).**  "No step assumes `ρ∈(1/2)ℤ`" is decorative in this
register: H-SIDX(1) posits an SU(2) ferromagnetic vacuum with `Q_0=S^-` and
highest-weight hard spaces, which forces the vacuum to be fully polarised and
`ρ=S∈½ℤ`.  The M-IDX-density precedent (`ρ` genuinely free over a general
covariant MPS pair) does not port.  *Fix:* say that `ρ` is carried
symbolically but is `=S` in every instance covered.

**m5 (H-SIDX(1)).**  "D26(INT) holds, but its arithmetic is unused."  An
assumed-and-unused hypothesis should be deleted — the memory campaign deleted
LR4 for exactly this reason (memory-index-r1 objection 1).  *Fix:* delete or
mark as interface-only.

**m6 (H-SIDX(1), ⟨1⟩1 ASSUME).**  "Highest-weight hard packet spaces"
restricts the hard data to `ker S^+`; this restriction appears in neither §0's
PROVE block nor the claims rows, which speak of "the hard process".  *Fix:*
carry `ψ∈ker S^+` into the row statements.

**m7 (§0, SIDX.1).**  `S^phys_λ := 1+𝗌_λ` presumes the disconnected part is
exactly `1` in D29(3)'s norm-projection normalisation; with
`𝗌_λ=⟨M_1,M_2⟩/‖M_1‖²` that is a convention about how the disconnected piece
was subtracted, and it is never stated.  *Fix:* one line in D29(3).

**m8 (⟨1⟩2).**  The PROVE line is not a proposition (L6b).  *Fix:* state the
three displayed identities as the proposition.

**m9 (§0 (S-IDX.2-source), ⟨1⟩7.⟨2⟩3).**  The bridge's non-portability off
`ρ=1/2` is implicit in the words "D24's D6 register" but never stated: at
`ρ≠1/2`, (SIDX.17)'s `2i·sgn·k` and (SIDX.4)'s `i·sgn·(ℓ_h/ρ)k` disagree.
*Fix:* one sentence, as Lane B does ("the spin-`S` source bridge would need
D24 re-normed at density `ρ` and is NOT claimed").

---

## 4. NOTE

**N1.** (SIDX.4) advertises `o(k)`; the proof delivers `O(k²)` (from
(SIDX.10)+(SIDX.12)).  Claim the stronger remainder or say why not.

**N2.** In the stated register `sgn(v_h−v_s)≡+1` (D8 half-zone, `ε_I`), so the
sign is carried but never exercised; the D7 out/in labelling that gives it
content (`S_phys=S_12` vs `S_21`, oracle-r2 residue 4) is gestured at in
⟨1⟩5.⟨2⟩4 but never tied to a window geometry.  Lane B ties it to the packet
ordering explicitly; adopt that at merge.

**N3 (orchestrator lane, not the shard's fault).**  The shard's CHECKER SPEC
item 3 correctly demands `h=2π/5` with `N` divisible by five — that is
ML4-Q1's countersequence.  The frozen probe does **not** do this: `run_p3`
uses `hard_idx = max(1, round(n/5))` over `SIZES_P3=(12,16,20,24,28,32)`, so
`h` ranges over `1.047, 1.178, 1.257, 1.309, 1.346, 1.178` — the hard momentum
moves with `N`.  The recorded "growth 20.5" is therefore not literally
ML4-Q1's fixed-`h` sequence.  Recommend fixing the probe to the shard's
discipline (this strengthens, not weakens, the P3 certificate).

**N4 (orchestrator lane).**  P2(b)'s `η`-insensitivity gate is arithmetically
trivial: `proto` and `proto_dressed` are the *same expression* in the source
(`qk @ hard_vec` twice), so `max(diffs)=0.0` by construction.  It certifies
magnon-number superselection, which is the right structural point, but it is
not a measurement.  The shard does not lean on it — correct.

**N5 (credit).**  §0's replacement of the target's ill-posed
`∂_{k_s}arg 𝖲*|_0` by `∂_k arg(1+𝗌_*)|_0` is a genuine repair (the argument of
a function with a linear zero is undefined at the zero), consistent with D7's
branch and with `arg S_phys` in (R18).  Disclosed in HONEST STATUS 2.  Keep.

**N6 (credit, and a warning for the merge).**  The LAW survived my two
falsification attempts (C-e).  Slope `= 1/ρ` exactly for a spin-1/2 chain with
NNN coupling and for spin-`S` chains with a biquadratic term — models inside
H-SIDX(1) whose contact algebra differs from D6/`spin-s-twomagnon` and whose
`ℓ_h=1`, `2iv_h`, `2ρ` data are unchanged.  That is real, non-trivial evidence
that the missing lemma of F1 is TRUE and provable.  It should be recorded in
HONEST STATUS as evidence, and it raises the value of proving F1's fix rather
than demoting the claim.

---

## 5. CROSS-LANE COMPARISON — `soft-index.md` (A) vs `soft-index-b.md` (B)

Read after attacking A, per the work order.  Each row states which lane the
disagreement indicts.  A and B agree on the **conclusion** (Adler zero; jet
`sgn(v_h−v_s)|q|/ρ`; `=1/S` on the spin-`S` anchor; `2` at `ρ=1/2`) and on the
**finite-volume index identity** (A: `D^†D=2m_λ`, `PJ^-_0=Q_0J^z_0/m_λ`;
B: `D^†D=2M`, `PJ^-_0=Q_0J^z_0/M`, `M=ρN−n` — the same statement, both
correct, both verified by me).  They disagree on almost everything else.

**X1 — the two D29 designs (protocol datum).  Indicts A.**
A: an abstract "connected on-shell pairing" `𝗌_λ=⟨M_1,M_2(k)⟩/‖M_1‖²` built
from unnamed window-local preparation/resolution matrices and a filter
`Π_{N,T}(E)`; no formula, no instance, no checker (M2, M7).
B: an explicit finite linear-algebra object (B3) — interacting-vs-free
momentum-kernel row ratio `ℛ(k)`, aggregated with free-kernel row weights,
`𝒜=𝔯−1` — and B correctly observes that the pre-registered probe's
`phase_function` computes exactly this (I checked the source: `ratio =
ft * conj(free_t)` with `free_t = f0·e^{-i[ω(k)+ω(h)]T}` — B's (B3)).
The target brief made computability-in-finite-volume half of D29's value;
B delivers it, A does not.

**X2 — where the `1/(2ρ)` lives.  Indicts A (and flags a shared gap).**
A folds it into a **redefined** flux constant `L_λ(0,h)=−i sgn/(2ρ_λ v_h)`,
silently colliding with the frozen D24(d)3 (M1).  B keeps D24(d)3 verbatim as
its clause (3′) (`L(0,h)=−i sgn/v_h`) and carries the leg density as a
**separate displayed factor** `1/(2ρ)` with the line
`‖Q_{k}|Ω⟩‖²=⟨Ω|S^+_{-k}S^-_kΩ⟩=Σ_x2ρ=2ρN`.  B's bookkeeping is L4-clean and
auditable; A's is a silent redefinition.  *Shared gap:* B's justification is
also a non sequitur — it writes "one unit-normalized soft magnon carries
`(2ρN)^{-1/2}` … so the multiplier normalization divides by `2ρ`", i.e. it
too jumps from one power of `(2ρ)^{1/2}` to a full power of `2ρ`.  Neither
lane derives the factor; A hides the gap inside a definition, B displays it.
The merge must record this as the campaign's open lemma (F1).

**X3 — ML4-Q1 immunity.  Indicts A.**
A (SIDX.15): "`k` is fixed while `N→∞`" — an ordering *rule*.  A's datum is
still perfectly well defined at `k=2π/N`, fixed `N`.
B (B10): a *structural* immunity — the soft profile is sampled on ring momenta
only, so `Λ_N(ε)=∅` whenever `ε<2π/(c_2N)`; the fixed-`N` soft sequence is
**outside the datum's domain by construction**.  B's mechanism is checkable
and cannot be violated by a careless reader; A's can.  Aggravating for A:
A's `ς→0`-before-`k→0` order (M3) re-creates the unsmeared plane-wave soft
leg, which is the very object ML4-Q1 concerns; B ties the width to `ε`
(`f_ε(k)=ε^{-1/2}f(k/ε)`, one scale) as the brief prescribes.

**X4 — the Adler zero.  Indicts A.**
A proves it only asymptotically, and (M4) in the descendant channel it is the
bare `(e^{ik}−1)`.  B proves an **exact finite-index** statement (B6):
`ℛ(0)=1` exactly at every `(N,T,W,σ)`, from `[H,Q_0]=0` and `ω(0)=0` — the
Goldstone leaf — with the kinematic factor separated in (B7) and the fence
cited.  B's (B6) is the stronger and cleaner G0-soft-r1 answer, and A has no
analogue because A's datum is never concrete.

**X5 — offset bookkeeping (`N−2n` vs `N−2` vs `2ρ` vs `M=ρN−n`).  Indicts A.**
Both lanes are arithmetically correct; the disagreement is what is displayed.
A displays the `S=1/2` numbers (`N/2−n`, `N−2n`, `N−2`) and asserts the
spin-`S` case by the nonexistent `SIDX-W2` (M8).  B displays the abstract
chain once — `2M=2(ρN−n)=N−2n` at `ρ=1/2` `=2SN−2n` at `ρ=S` — and adds the
warning A never makes: **"the `2` in `2M` is the su(2) structure constant and
is NOT the slope `2`; conflating the two `2`s is the first place the critic
will look."**  That is the correct fence, and A does not carry it.
Also: B's §0 writes `M:=ρN−n|q|` while its ⟨1⟩2 writes `M:=ρN−n` — a lane-B
internal inconsistency (harmless at `|q|=1`, MINOR for B).

**X6 — the two D30/(TGT) designs.  Indicts A, decisively.**
A's D30: closure clauses + ML4-A-style `C¹` trace regularity of the limit
objects + **D30(2), which fixes the value of the limiting flux at zero**.
B's D30: (TGT1) row-mass nondegeneracy; (TGT2) readout settling onto the
chamber data of *some* near-shell exact eigenvectors, with the explicit clause
"**(TGT2) fixes the value of NO ratio — the values are computed from the
PROVED contact algebra**"; (TGT3) optional convenience; (TGT4) spin-`S`
representability.  B therefore derives its jet value from S2-2body-S (a PROVED
row) via SIB-L1 + (T.3); A's jet value comes from its own hypothesis (F1).
For the campaign's spine sentence — *symmetry fixes the law; dynamics only
picks the values* — B's split is the intended one and A's inverts it: A
assumes the value and derives nothing quantitative; B assumes the dynamics
(settling, an honest LR-analogue) and derives the value.
The counter-charge available to A is real but weaker: B's (TGT2) is
dynamics-shaped and strong (B self-flags this at ⟨1⟩8.8), and B's ⟨1⟩4 is
anchored to the spin-`S` contact algebra, so B's ⟨1⟩4 is *not* abstract.  B
answers that with its own abstract fallback ⟨1⟩5 (descendant-projected law),
where it, like A, must assume D24(d)1,3,4 — and where it discharges clauses 2
and 5 from the protocol, which A also effectively does but by fiat (M5).

**X7 — adjudication of B's negative claim ("equicontinuity alone cannot pin
the jet value").  B's claim is CORRECT, and it indicts A.**
B (HONEST STATUS retreat 2, ⟨1⟩8.8) asserts that the target brief's suggested
weakest (TGT) — uniform local boundedness + equicontinuity — makes the jet
well defined but pins no value.  I confirm this constructively: any clause
that constrains only regularity of the family is invariant under
`𝒜_λ(ε) ↦ (1+𝒜_λ(ε))(1+icε)−1` (equivalently `L↦μL` in A's parametrisation),
which preserves uniform boundedness, equicontinuity, Lipschitz-in-`k` bounds
and ML4-A's hypotheses, while shifting the jet by an arbitrary constant.
Consequences: (i) B's retreat 2 is sound and should be recorded as a campaign
finding; (ii) it does **not** refute A's formulation directly, because A's
D30 is not equicontinuity-only — but it explains *why* A had to insert a
value-fixing clause, and it converts F1 from "a leaf is missing" into "no
purely-regularity (TGT) can ever supply this leaf".  The value must be reached
either through on-shell/contact data (B's route) or through a genuine
derivation of the leg-density flux normalisation (A's missing lemma).
**Merge consequence:** A's D30(2) value clause must be deleted and replaced by
either B's (TGT2) or F1's derived lemma; keeping both lanes' D30 as-is would
put the answer into `definitions.md` as a hypothesis.

**X8 — nonvacuity.  Indicts A.**
A: ⟨1⟩6 concedes limit-point existence and substitutes S2-2body multipliers
for D29 instances (M2).  B: ⟨1⟩1.⟨2⟩3 proves the finite-index family is
nonempty at **every** soft scale with an explicit threshold
(`N>max(N_1(f,g),2π/(ε(c_2−c_1)))`), cites the recorded probe instances
(`1.9929`, `1.0217`), and separates finite-index nonemptiness from limit-point
existence in one place.  B answers the mandatory landmine; A does not.

**X9 — checker specs.  Indicts A.**
A: three D6-only items, all duplicating already-PROVED rows, none touching
`ρ`, `L`, or the datum's slope; the load-bearing step has no red path (M7).
B: SIB-C0–C3, including **SIB-C3 with `--red-legnorm`** (mutate the leg norm
`2ρN→ρN`; the reconstructed jet becomes `2/ρ` and must FAIL against the
measured P1 slope) — precisely the mutation that would kill A's undefended
factor, and **SIB-C2** (row-resolved `arg ℛ(k)` vs exact `δ_phys`, `≤0.05`),
which certifies the datum's slope.  B's spec tests its theorem; A's does not.

**X10 — what the limit object is a function of.  Merge burden, MINOR both.**
A's limit `𝗌_*(k;h)` is a function of a continuous soft momentum with `ς→0`
first, and its jet is a momentum derivative (matching D25/the target's form).
B's limit `𝖲^*(ε)` is a function of the soft **scale** with the momentum
aggregated out, and its jet is `lim arg(1+𝖲^*(ε))/\bar k_w(ε)` with
`\bar k_w(ε)∈[c_1ε,c_2ε]`.  These are different objects; the merged D29 must
choose.  Given M3, B's single-scale version is the one consistent with D24(b)
and with the frozen probe; A's is the one that literally matches the target
statement's `∂_{k_s}`.  Orchestrator decision, not a defect in either.

**X11 — lane-B defects visible from here (for B's own critic, not adjudicated
by me).**  Unedited self-correction text left in the proof at ⟨1⟩4.⟨2⟩1.⟨3⟩1
("… — wait: the descendant `Q_0|h'⟩` has energy `ω(h')` … Repair: …") and at
⟨1⟩5.⟨2⟩1 ("— wait: (H-band) gives only `O(k)`"); the `M=ρN−n|q|` vs `ρN−n`
inconsistency (X5); the `(2ρN)^{-1/2}→1/(2ρ)` non sequitur (X2); and B's
(S-IDX.1a) inherits the spin-`S` representability clause (TGT4) as an
assumption where A's route needs no analogue.  At least MAJOR for B on the
first item under L6b (a proof shard may not ship deliberation text as
justification).

**Summary of the cross-lane adjudication.**  On the two questions the work
order singles out: (1) the two D29 designs — **B's is materially better**
(concrete, computable, probe-compatible, structurally ML4-Q1-immune, with an
exact `k=0` fiber identity); (2) the two D30/(TGT) designs — **B's is
materially better and B's negative claim about equicontinuity is correct and
indicts A**: A's D30(2) is the only thing pinning A's jet, and no
regularity-only clause can replace it.  A's genuine advantages over B are
narrower: A's `∂_k arg(1+𝗌_*)` phase repair (N5) is cleaner than B's
`\bar k_w`-normalised jet, and A's ⟨1⟩4 (SIDX.12) is a clean, correct,
self-contained restatement of ML4-A in the limit register.

---

## 6. Disposition

`S-INDEX-fin` (as re-scoped in M6: ⟨1⟩1, ⟨1⟩2.⟨2⟩1–⟨2⟩2, ⟨1⟩3, no D29) may
enter the DAG at **SKETCH**; I verified every one of its identities
independently, including their spin-`S` and biquadratic-deformed forms.
`S-INDEX-spec` and `S-INDEX-source` must **not** enter the DAG until F1 is
either derived or demoted, because as written the row's headline number is its
own hypothesis.  The MERGE PROPOSALS' D29/D30 must not be applied to
`definitions.md` in their present form (F1, M1, M3, M5, X6, X7).

**FAIL(F1, M1, M2, M3, M4, M5, M6, M7, M8)**
