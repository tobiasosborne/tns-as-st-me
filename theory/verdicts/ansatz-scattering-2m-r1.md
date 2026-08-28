# Critic verdict r1 — `theory/ansatz-scattering-2m.md` (Theorem AC-EX-2M, Lane S2)

Critic: Opus, adversarial, 2026-08-28.  Work order: `briefs/soft-critic-r1.md`
(S2 specialization).  Writable lane: this file only.  All prototype
computation done in `/tmp/.../scratchpad/a2m_c1_proto.py`; no shared file
touched.

## 0. What was independently recomputed (obligation 1)

| # | Step | Method | Outcome |
|---|---|---|---|
| V1 | ⟨1⟩3 (D31-C2 from the D1 transfer gap) | re-derived from D1(b)–(d) via the Stinespring isometry `V_w x = Σ_s|s⟩⊗A^{s_1}⋯A^{s_w}x` | **CORRECT**; see O8 for the norm gap |
| V2 | ⟨1⟩2.⟨2⟩3 (D6 bound-band gap `E_sc−E_b=J\|e^{iq}−c\|²`) | recomputed from ML2 (18)–(19) | **EXACT MATCH** |
| V3 | ⟨1⟩5.⟨2⟩1 (2M-Cook identity) | expanded `H a_1(x)a_2(y)Ω_A` from scratch | **CORRECT** |
| V4 | ⟨1⟩5.⟨2⟩4 (Cook majorant `\|t\|^{-3}` at `N≥5`) | re-counted the cone split | **CORRECT** |
| V5 | ⟨1⟩6.⟨2⟩2 (Gram cone bookkeeping) | re-counted the four-fold sum | **WRONG EXPONENT** (O7) |
| V6 | ⟨1⟩7.⟨2⟩3 (exact ML2/D7 match, `W_+^*W_-=S_12`) | re-derived the in/out labelling from D7 + ML2 (17) | **CORRECT** (O13 caveat) |
| V7 | `d_B` in the soft limit | `d_B → J sin²(k_h/2) > 0` as `k_s→0` | **does not degenerate** (favourable; unstated) |
| V8 | CHECKER A2M-C1, green + red | AKLT `A^a=σ_a/√3`, `d=1..12`, python3 -O | green `\|err\|≤3.2e−15`, ratios `−1/3`; red errs by exactly `1.0` at every `d` — **red-capable** but see O6 |
| V9 | `theory/checks/soft_index_probe.py --selftest` | run | `selftest PASS`, exit 0 |

The shard's central ambition — deriving the clustering inequality instead of
assuming it (the D28-C ⟹ D31-C2 inversion) — **survives attack**.  That is a
real advance over the AC-EX precedent and should be preserved verbatim.  The
failures below are concentrated in ⟨1⟩7.⟨2⟩4 and in §4 (the D29/(SR) block).

---

## 1. FATAL

None.

## 2. MAJOR

### O1 (MAJOR) — the fixed-packet fence enumerates the wrong parameters; the ε-divergence is not fenced

**(a) Location.** `theory/ansatz-scattering-2m.md` ⟨1⟩2.⟨2⟩1, first sentence:
"Every estimate fixes `K_1,K_2` and may depend on `ε_v,ε_0,d_B,η_inel`."
⟨1⟩2's PROVE is "Neither the soft endpoint nor the two-string is hidden in
Cook."

**(b) My computation.** The Cook majorant of ⟨1⟩5.⟨2⟩4 is
`C_N|t|²⟨ε_v|t|/2⟩^{-N} + O(|t|^{2−N})`, where `C_N` comes from ACE-SP
(⟨1⟩5.⟨2⟩3), i.e. from repeated integration by parts with
`(it(x/t−ω'(p)))^{-1}∂_p`.  Its constant is
`C_N ∝ sup_{j≤N}‖∂_p^j F‖_∞ · ε_v^{-N}` — it depends on the **Schwartz
seminorms of the packet amplitude**, which the fence sentence never mentions.
For the shard's own soft profile `f_ε(k)=ε^{-1/2}f(k/ε)`,
`‖∂_p^N f_ε‖_∞ = ε^{-N-1/2}‖f^{(N)}‖_∞`, and the onset time of the ACE-SP
regime is `t_0 ∼ 1/(ε ε_v)`.  So the Cook constants diverge like `ε^{-N}`.

Of the four listed parameters, only `ε_0=dist(V_i,{0})` degenerates, and `ε_0`
appears in **no displayed estimate in the shard**.  Explicit counterexample to
the fence as literally stated: fix a soft momentum `k_0≠0` and shrink only the
*width*, `f_δ(k)=δ^{-1/2}f((k−k_0)/δ)`.  On D6 this gives
`ε_v→|v_h−v(k_0)|>0`, `ε_0→|v(k_0)|>0`, `d_B>0`, `η_inel=+∞` — **all four
listed parameters bounded below** — while the Cook constants still blow up
like `δ^{-N}`.  A reader who takes the enumeration at face value can therefore
conclude soft-uniformity, which is false.  The fence does not fence the leak
it exists to fence.

**(c) FIX DEMAND.** Replace the enumeration by "may depend on `ε_v,ε_0,d_B,
η_inel` **and on the Schwartz seminorms `sup_{j≤N}‖∂^j F‖_∞` of the packet
amplitudes, which is where the `ε→0` divergence lives**", and display the
`ε^{-N}` growth of `C_N` for `f_ε` once.

**(d) SURVIVING WEAKER STATEMENT.** For each fixed packet amplitude `F` and
each fixed `ε>0`, ⟨1⟩5's Cook estimate holds with a constant depending on
`ε_v,ε_0,d_B,η_inel` and on the Schwartz seminorms of `F`; no bound uniform in
the packet family, and in particular none uniform in `ε`, is claimed or
implied.

---

### O2 (MAJOR) — D29 interface clause 5 smuggles the soft-leg LSZ identification, which *is* (A2M.3)'s content

**(a) Location.** ⟨1⟩8, interface clause 5: "At every fixed `ε>0`, D29's
on-shell pairing agrees with the constructed channel pairing of `W_±^(ε)`";
used as the sole substantive input of ⟨1⟩9.⟨2⟩1.

**(b) My computation.** D29's soft leg is created by the **charge** operator
`Q[f_ε]`/`J^-[f_ε]` (`briefs/soft-index-target.md`, Lane S1, PROTO).  The
constructed channel's soft leg is the D31(3) **exact filtered magnon creator**
`a_{2,b}(n)` with the displayed normalisation
`a_{2,b}(n)Ω_A=Γ_M(χ_2e_n⊗e_b)`.  These are different operators, and the
assertion that their on-shell pairings agree is precisely the soft-leg LSZ
reduction: that `Q[f_ε]Ω_A` lies on the selected magnon band with the D31(3)
normalisation, with no admixture that survives the on-shell filter.

Stripping clause 5 out, the *entire* mathematical content of ⟨1⟩9.⟨2⟩1 is:
a family bounded in `L²(I)` (Cauchy–Schwarz + clause 3) has weak subsequential
limit points (Banach–Alaoglu).  **(A2M.1)–(A2M.2) are logically inert in
⟨1⟩9.⟨2⟩1 except through clause 5.**  The shard's HONEST STATUS sentence
"D31 supplies every fixed-scale channel value" is therefore false as written:
D31 supplies the wave operator; clause 5 supplies the value.

On D6 the identification *is* verifiable and exact: `J^-[f]Ω=Σ_x f(x)|x⟩` is
literally the one-magnon packet (D6 bases), so clause 5 is a theorem there.  In
the abstract D31 setting it is not.

**(c) FIX DEMAND.** Split clause 5 into (5a) an interface *convention* (which
pairing is compared) and (5b) a **named hypothesis (ACE2M-LSZ)**: at each fixed
`ε>0` the charge-created soft leg `Q[f_ε]Ω_A` equals the D31(3) filtered
one-magnon vector for the profile `f_ε` up to an on-shell-null remainder.
Prove (ACE2M-LSZ) on D6 (one line, as above) and list it as an unproved
hypothesis elsewhere; then say plainly in HONEST STATUS that the wave operators
enter (A2M.3) only through (ACE2M-LSZ).

**(d) SURVIVING WEAKER STATEMENT.** On D6–D8 the charge-created soft leg is
exactly the D31(3) filtered magnon packet, so the constructed channel supplies
D29's fixed-`ε` value there.  In general, (A2M.3) holds conditionally on the
named hypothesis (ACE2M-LSZ); unconditionally, ⟨1⟩9.⟨2⟩1 asserts only
Banach–Alaoglu for a bounded family and does not use `W_±`.

---

### O3 (MAJOR) — (ACE2M-SR) and the ⟨1⟩9.⟨2⟩2 display are mutually inconsistent; under the only reading that makes Arzelà–Ascoli non-vacuous, (SR) *is* a soft-uniform hypothesis

**(a) Location.** ⟨1⟩8, the (ACE2M-SR) block; ⟨1⟩9.⟨2⟩2 and its display.

**(b) My computation.** (SR) is posed "**after the first four D29-order
operations**", i.e. after `N→∞ ≺ t→±∞ ≺ W↑ℤ ≺ σ↓0`.  But the objects it
quantifies over are "any **exhaustion/packet-width** sequence `A_j(ε)`", and
`W↑ℤ`, `σ↓0` *are* operations three and four.  The two clauses cannot both
hold:

* Reading (i) — the four inner limits genuinely exist.  Then there is no
  `j`-family; `sup_j` is vacuous; and Arzelà–Ascoli in ⟨2⟩2 has **nothing to
  extract a subsequence from**.  ⟨2⟩2 is then a non-argument.
* Reading (ii) — `j` indexes `(W_j,σ_j)` and the inner limits are only
  subsequential.  Then AA works, but (a) `sup_j` makes (SR) a **uniform-in-
  `(W,σ)` equicontinuity of `∂_ε` on an interval containing `ε=0`** — exactly a
  soft-uniform regularity assumption, the class of hypothesis the campaign
  target flags as the disease (ML4-Q1); and (b) the display
  `lim_{ε_j↓0}[lim_{σ↓0}lim_{W↑ℤ}lim_{t→±∞}lim_{N→∞}𝒜]` is **false as printed**,
  since `lim_{σ↓0}` and `lim_{W↑ℤ}` do not exist and must read `lim_j`.

Second prong: (SR) requires `{A_j(ε),∂_εA_j(ε)}` on the **closed** interval
`[0,ε_0]`, so it presupposes that `A_j(0)` and `∂_εA_j(0)` exist for each `j`.
But `f_ε(k)=ε^{-1/2}f(k/ε)` is undefined at `ε=0`; the shard never says what
`A_j(0)` means.  The endpoint is the entire physical content (Adler zero,
slope), so this is not a formality.

**(c) FIX DEMAND.** Restate (SR) as posed after operations one and two only,
with `j` an explicit index of an `(W_j,σ_j)` exhaustion sequence; replace the
⟨2⟩2 display's `lim_{σ↓0}lim_{W↑ℤ}` by `lim_j`; and add one clause defining
`A_j(0)` (e.g. by continuous extension of the fixed-`j` datum, stated as part
of (SR)).  Add one sentence conceding that (SR) is uniform in `j` down to
`ε=0` and is therefore a genuine (if non-Cook) soft-uniformity hypothesis.

**(d) SURVIVING WEAKER STATEMENT.** For each fixed `(W,σ)` and each `ε>0` the
datum is defined and bounded, so the family has weak `L²(I)` limit points with
`ε↓0` last.  The `C¹`/first-jet upgrade holds under a hypothesis that is
explicitly uniform in the `(W,σ)` exhaustion index and that presupposes the
first jet at `ε=0` at each fixed index; no such uniformity is derived here.

---

### O4 (MAJOR) — the sole claimed nonempty instance of (SR) is not established; ⟨1⟩9.⟨2⟩3 contradicts ⟨1⟩9.⟨2⟩4

**(a) Location.** ⟨1⟩9.⟨2⟩3 ("so `(SR)` holds and the limit-point set is
nonempty") vs ⟨1⟩9.⟨2⟩4 ("D31 alone does not imply `(SR)` … they control
neither an on-shell first derivative nor the `W,σ` exhaustion").

**(b) My computation.** The claims row for S2-2body reads: "For D6 with fixed
`0<|k_h|<π` and signed `k_s→0`, the displayed `δ_phys`/`S_phys` expansion and
cubic remainders follow from the local current/contact equation with a
compact-hard uniform remainder."  Its uniformity is over the **hard** momentum
in a compact `I⋐(0,π)`.  It is a statement about the exact infinite-chain
two-body amplitude.  It contains **no window, no packet width, no finite
volume**, hence nothing about the index `j` of O3.  But by O3 reading (ii) the
`j`-uniformity is exactly what (SR) demands, and by the campaign target it is
exactly where the ML4-Q1 `√N` disease lives.  So ⟨2⟩3's "The family is
therefore relatively compact with an equicontinuous first jet" does not follow
from the cited inputs; the word "therefore" spans the missing step.  ⟨2⟩4 then
says in plain language that this step is not available.

This matters more than a bookkeeping slip: (A2M.3) exists to answer Lane S1's
**vacuous-truth landmine**, and the D6 anchor is the shard's only offered
non-vacuous instance.

**(c) FIX DEMAND.** Either (i) supply the `(W,σ)` bookkeeping on D6 explicitly
— exhibit `A_j(ε)` for a named window/width exhaustion and verify relative
compactness and equicontinuity of `∂_ε` in `L²(I)` uniformly in `j`; or
(ii) downgrade ⟨2⟩3 to "(SR) holds for the `j`-independent infinite-chain
amplitude on D6; the `(W,σ)`-uniform version is open", and mark (A2M.3)'s
non-vacuity claim accordingly.

**(d) SURVIVING WEAKER STATEMENT.** On D6–D8 the *infinite-chain, exhaustion-
free* channel datum is `C²` at `k_s=0` uniformly on compact hard windows
(S2-2body), so the `j`-free version of (SR) holds and the limit-point set for
that object is nonempty.  Whether (SR) holds uniformly along a `(W,σ)`
exhaustion is not established on any model, D6 included.

---

### O5 (MAJOR) — ⟨1⟩7.⟨2⟩4's "entire scattering summand" is unproved and contradicts the shard's own claims row

**(a) Location.** ⟨1⟩7.⟨2⟩4: "Taking the compatible union over all compact
packet windows … On that union the isometric extensions match ML2's **entire**
scattering summand."  Against MERGE PROPOSALS claims row: "No … **asymptotic
completeness** is claimed", and HONEST STATUS: ML1 item "(v) general-model
range exhaustion" open.

**(b) My computation.** Two defects.

*Defect 1 (unproved).* "Compatible" is asserted, not proved.  The creators
`a_{i,b}(n)` depend on the filter `χ_i`, hence on the window; two different
window pairs give **different identification maps `I`**, and there is no step
in the shard showing that the resulting `W_±` agree on the common domain.  The
one-particle vectors do agree (`Σ_xF(x)a_1(x)Ω_A=Γ_M(F̂e_b)` when `χ_1≡1` on
`supp F̂`), but that does not settle the two-particle precursor.  The source
*does* prove the needed statement — `refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`,
Theorem `Haag-Ruelle`, final clause: "If `B̃*_{i,t}(g̃_i)Ω=B*_{i,t}(g_{i,t})Ω`
for all `i`, and `V(g̃_i)∩V(g_j)=∅` for all `i≠j`, then `Ψ̃^out=Ψ^out`" —
and the shard does **not** port it, in a shard whose ⟨1⟩10 explicitly audits
which source results are and are not imported.

*Defect 2 (contradiction).* Combine ⟨2⟩4 with ⟨1⟩2.⟨2⟩2 (`P_BW_±=0`, so
`ran W_± ⊆` scattering summand).  If ⟨2⟩4's density also gives
`ran W_± ⊇` scattering summand, the conclusion is
`ran W_± =` ML2's scattering summand — i.e. **asymptotic completeness on the
charge-two sector modulo the bound band**.  The claims row disclaims exactly
this.  Under the AC-EX register comparison this is the one place the shard
claims more than its precedent allows: AC-EX's adjudicated row says "No
completeness … is claimed", and AC-EX ⟨1⟩6.⟨2⟩5 is scrupulous to add "No
assertion is made on `(H_out^{ex})^⊥` or that `H_out^{ex}` exhausts a spectral
subspace."  ⟨1⟩7.⟨2⟩4 makes precisely that assertion.

**(b′) Un-flagged sub-issue.** ML2's fundamental domain is `−π<K≤π`, where
`c=cos(K/2)≥0` and hence `v(k_2)>v(k_1)` for every chart point with
`0<q<π`.  Packet windows with `K_Σ=K_1+K_2` outside `(−π,π]` fold back with
`c<0` and the reversed labelling, and ML2 flags the odd-`r` anti-periodicity of
`e^{−iK(x+r/2)}` in `K`.  ⟨2⟩4's "compatible union" never addresses the folding.

**(c) FIX DEMAND.** Port the final clause of source Theorem `Haag-Ruelle`
(creator-choice independence under disjoint velocity supports) as a numbered
step with its hypotheses checked against D31, add the chaining across
non-nested window pairs and the `K`-folding, **or** delete the word "entire"
and state only what ⟨1⟩1 (A2M.2) already says ("a fixed packet range lies in
the matching part of ML2's scattering summand").  Do not leave ⟨2⟩4 stronger
than the claims row.

**(d) SURVIVING WEAKER STATEMENT.** For each fixed D31 packet pair on D6–D8,
`ran W_±` is a closed subspace of ML2's scattering summand orthogonal to the
bound band, and `W_+^*W_-` acts on it as multiplication by D7's `S_phys`.
Whether the union over windows exhausts the scattering summand is open, and no
completeness statement is made.

---

### O6 (MAJOR) — CHECKER SPEC A2M-C1 is red-capable but does not certify the named computation it claims to certify

**(a) Location.** §6, A2M-C1: "This certifies **MPS-2M-cluster**, including
fixed-point subtraction."

**(b) My computation.** I implemented the spec exactly (AKLT `A^a=σ_a/√3`,
`l=1`, `r=I/2`, Cartesian `S^z`, `C=D=I+S^z`, `d=1..12`, direct contraction vs
`⟨l,E_C(E^{d−1}−P)E_D(r)⟩`, `python3 -O`).  Results:

* GREEN: both routes reproduce `(4/3)(−1/3)^d` with `|err| ≤ 3.2e−15` (the
  spec's `1e−12` gate is comfortable) and successive ratios `−1/3` to machine
  precision.  I also verified the expected value analytically:
  `E(Y)=(1/3)(2 tr Y·1 − Y)`, `λ_E=1/3` on the traceless block,
  `E_{S^z}(r)=−σ_z/3`, giving `⟨S^z_0S^z_d⟩=(4/3)(−1/3)^d`.  The `d−1` in the
  checker is consistent with the `d_sep` of ⟨1⟩3.⟨2⟩1 (sites strictly between).
* RED: the mutant errs by **exactly 1.0** at every `d` and the ratios become
  `+2.07, +0.83, +1.07, …`.  Both gates fail; the mutation is genuinely red.

So the spec is sound as far as it goes.  What it does **not** test is the
content of MPS-2M-cluster that is actually novel and load-bearing in ⟨1⟩3.⟨2⟩2:

1. **Support-length independence of `C_{A,λ̃}`.**  `C=D=I+S^z` are one-site.
   I extended the probe to `C=∏_{j<w}(I+S^z_j)` for `w=1,2,3` at gaps `2,4,6`
   and confirmed `|conn|/(‖C‖‖D‖)` is uniformly bounded and in fact *decreasing*
   in `w` (`1.24e−2, 4.12e−3, 1.03e−3` at gap 2).  This is the claim that
   makes D31-C2 a theorem rather than a hypothesis, and the shard's spec omits
   it entirely — a mutant that replaced `C_{A,λ̃}` by `C·w_C·w_D` would pass
   A2M-C1.
2. **The Jordan-safe `λ̃` form.**  AKLT's `E` is diagonalizable
   (`λ_E=1/3`, no Jordan block), so the spec cannot distinguish D1(c)'s honest
   `C_λ̃λ̃^m` from the bare `O(λ_E^m)` that D1(c) explicitly calls *false in
   general* — the shard's own ⟨2⟩2 boasts "No bare `O(λ_E^{d_sep})` is used",
   and nothing certifies that.
3. **(D31-C4).**  The isometry ⟨1⟩6 uses C4, not C2.  A2M-C1 touches no
   creator, no truncation, no commutator.  "Load-bearing for isometry" in the
   spec's own heading is therefore an overstatement.

**(c) FIX DEMAND.** Keep A2M-C1 and its red mutation; rename its certified
scope to "the connected two-point transfer-matrix identity with fixed-point
subtraction on one model".  Add (i) a support-length row (`w_C,w_D∈{1,2,3}`,
gate: `|conn|/(‖C‖‖D‖λ̃^{d_sep})` bounded uniformly in `w`) with its own red
mutation, and (ii) at least one model with a Jordan block at modulus `λ_E`, or
state in the spec that the Jordan-safe form is uncertified.  Also state
explicitly that the checker must use `raise`/`sys.exit`, **not** bare
`assert` — the spec mandates `python3 -O`, under which asserts are stripped and
the red mutation would silently exit 0.

**(d) SURVIVING WEAKER STATEMENT.** A2M-C1 certifies, on AKLT, that the
fixed-point-subtracted transfer-matrix route reproduces the direct connected
two-point function to `3e−15` and that omitting the subtraction fails by
exactly `1`.  It certifies neither the support-length uniformity nor the
Jordan-safe rate nor (D31-C4).

---

## 3. MINOR

### O7 (MINOR) — ⟨1⟩6.⟨2⟩2 exponent error: the Gram sum is four-fold, not two-fold

**(a)** ⟨1⟩6.⟨2⟩2: "The complement of the product cones contributes
`O(|t|^{2−N})`; summing (D31-C4) on the main cones contributes
`O(|t|²⟨ε_vt/2⟩^{-N})`."

**(b)** `⟨Ie^{-itH_0}F, Ie^{-itH_0}G⟩ = Σ_{x,y,x',y'} F̄_t(x,y)G_t(x',y')
ω_A(a_2(y)^*a_1(x)^*a_1(x')a_2(y'))` — **four** position sums.
`Σ|F̄_t||G_t| = ‖F_t‖_1‖G_t‖_1 = O(|t|²)·O(|t|²) = O(|t|⁴)`, and the off-cone
part is `≤ 4·O(|t|^{1−N})·O(|t|³) = O(|t|^{4−N})`.  The correct exponents are
`O(|t|⁴⟨ε_v|t|/2⟩^{-N})` and `O(|t|^{4−N})`.  The Cook step ⟨1⟩5.⟨2⟩4 (two
sums, `O(|t|^{2−N})`) is right; the exponents were carried over unchanged into
a quadratically larger sum.  Harmless — `N` is free — but wrong as printed in a
shard that is otherwise exact about exponents.

**(c) FIX DEMAND.** Replace `2−N` by `4−N` and `|t|²` by `|t|⁴` in ⟨1⟩6.⟨2⟩2.

**(d)** The isometry conclusion `lim_{t→±∞}⟨Ie^{-itH_0}F,Ie^{-itH_0}G⟩=⟨F,G⟩`
is unaffected: `N≥5` still gives an `O(|t|^{-1})` error.

### O8 (MINOR) — ⟨1⟩3.⟨2⟩2's mechanism is not the one that works, and the norm in D1(c) is unnamed

**(a)** ⟨1⟩3.⟨2⟩2 justification: "in the `l=1` gauge each finite MPS block is a
Stinespring contraction; conjugating the right environment by `r^{1/2}` costs
only `‖r^{1/2}‖‖r^{-1/2}‖`."

**(b)** The clean derivation needs no `r^{1/2}` and no condition number.  With
`V_w:ℂ^χ→(ℂ^d)^{⊗w}⊗ℂ^χ`, `V_wx=Σ_s|s⟩⊗A^{s_1}⋯A^{s_w}x`, D1(c)'s `l=1`
(`Σ_sA^{s†}A^s=1`) makes `V_w` an **isometry** for every `w`; then
`Ψ_D(r)=tr_{d^w}[(D⊗1)V_w r V_w^†]` gives `‖Ψ_D(r)‖_1≤‖D‖‖r‖_1=‖D‖` and
`|tr Ψ_C(Z)| ≤ ‖C‖‖Z‖_1`, both with constant **1**, uniformly in `w`.  Hence
`|ω_A(CD)−ω_A(C)ω_A(D)| = |tr Ψ_C((E^{d_sep}−P)Ψ_D(r))| ≤ ‖C‖‖D‖·‖E^{d_sep}−P‖_{1→1}`.
The residual gap is that D1(c) states `‖E^m−P‖≤C_λ̃λ̃^m` **without naming the
norm**, whereas what is used here is the trace-norm→trace-norm bound (or,
contracting the other way, the `∞→∞` bound for `E^*`).  Finite-dimensionality
repairs this with a `χ`-dependent equivalence constant, which is admissible
since `C_{A,λ̃}` may depend on `A`, but the shard should say so rather than
route through the condition number of `r`.

**(c) FIX DEMAND.** Replace the `r^{1/2}` gloss by the `V_w`-isometry argument
and add one clause: "`C_{A,λ̃}` absorbs the finite-dimensional norm-equivalence
constant between D1(c)'s norm and `‖·‖_{1→1}`."

**(d)** (D31-C2) as displayed is true, with `C_{A,λ̃}` independent of the two
support lengths (verified numerically in O6 item 1).

### O9 (MINOR) — ⟨1⟩2.⟨2⟩1 cites D17, the ℓ¹ **kink** class, in a one-vacuum two-magnon shard

D17 defines `𝒦^{(1)}_{αβ}⊂𝒦_{αβ}` (D9(a)) by
`Σ_{x<0}|ϱ(S^z_x)−s_α|+Σ_{x>0}|ϱ(S^z_x)−s_β|<∞` — a condition on **kink states
with two distinct vacuum tails**.  D31 has one vacuum, no `α/β`, no `s_α,s_β`;
D17 is neither in D31 nor in the claims row's depends-on.  This is a copy-paste
residue from D28(4) ("the resulting physical packet states lie in the `ℓ¹`
class D17"), which D31 correctly dropped.  I read the intent as invoking D17's
closing fence sentence ("Every soft statement about memory must fix the packet
first and take `k→0` afterwards"), but that sentence is not D17's defined
object.
**FIX DEMAND.** Delete D17 from the ⟨1⟩2.⟨2⟩1 justification; cite the campaign
target's limit-order clause instead.
**SURVIVING.** ⟨1⟩2.⟨2⟩1's substance (D3(a), D12(a′), D31(4)) is unaffected.

### O10 (MINOR) — D2(a) is a phantom dependency

D31's opening sentence ("from a D2(a) covariant vacuum family") and the claims
row's depends-on both list D2(a); no step of ⟨1⟩1–⟨1⟩10 uses on-site symmetry
or the covariant vacuum family, and ⟨1⟩1's own Justification line omits it.
**FIX DEMAND.** Drop D2(a), or name the step that uses it.
**SURVIVING.** The theorem holds over a single D1 injective translation-
invariant MPS vacuum with no covariance structure.

### O11 (MINOR) — claims-row / proof lockstep drift (two places)

(i) Row: "D1's transfer gap **derives D31-C2/C4**."  ⟨1⟩3.⟨2⟩3 derives C4 from
C2 **plus** D31(3)'s uniform almost-locality **plus** finite-range
Lieb–Robinson commutator decay; D31's own merge text is honest here ("After
uniformly almost-local truncation this implies (D31-C4)"), the row is not.
(ii) Row: "avoid the fiberwise-isolated charge-two bound bands" — the theorem
⟨1⟩1(A2M.2) and ⟨1⟩2.⟨2⟩2 both carry the qualifier "**D31-listed**", which the
row drops.  D31(5) only isolates bands "in the supplied exact data".
**FIX DEMAND.** Row → "D1's transfer gap derives D31-C2, and with D31(3)'s
uniform almost-locality also D31-C4"; restore "D31-listed" in the row.
**SURVIVING.** Both proof-text statements are correct as written; only the row
is loose.

### O12 (MINOR) — ⟨1⟩5.⟨2⟩1 drops the domain justification the parent shard supplies

The parent's ⟨1⟩5.⟨2⟩2 justifies `H(a κ)` by "⟨1⟩1.⟨2⟩3 for the domain (all
vectors lie in a bounded spectral subspace, and `a_{c,b}(y)` has compact
energy–momentum transfer by D28(3))".  The 2M leaf cites only "⟨1⟩4.⟨2⟩2 and
the product commutator identity" — `H` is unbounded and
`H a_1(x)a_2(y)Ω_A = [H,a_1(x)a_2(y)]Ω_A` needs the domain remark.  D31(3)'s
"compact-energy-momentum-supported" filter supplies it.
**FIX DEMAND.** Add the domain clause citing D31(3).
**SURVIVING.** (2M-Cook) is correct — I re-derived it independently (V3):
`(HI−IH_{0,12})F = Σ F(x,y)[D_1(x),a_2(y)]Ω_A`, using
`D_2(y)Ω_A=0` and `D_1(x)Ω_A=0` exactly twice.

### O13 (MINOR) — ⟨1⟩7.⟨2⟩3's `W_+^*W_-=S_{12}` needs `|S_{12}|=1`, unstated

`W_-=𝒰_{sc}^{-1}`, `W_+=𝒰_{sc}^{-1}∘M_{S^{-1}}` give
`W_+^*W_-=M_{\overline{S^{-1}}}`, which equals `M_S` only if `|S|=1`.  It is
true: ML2 (18) gives `S(K,q)=(c−e^{-iq})/(e^{iq}−c)=−\overline{(e^{iq}−c)}/(e^{iq}−c)`
with `c` real, so `|S|=1`.  One clause missing.
**FIX DEMAND.** Add "`|S(K,q)|=1` by ML2 (18) since `c` is real".
**SURVIVING.** The exact-match computation is otherwise correct: I verified
independently that the `e^{-iqr}` term is `e^{i(k_2x_1+k_1x_2)}` (`k_2` on the
left), so it is D7's `A_{21}` (incoming when `v(k_2)>v(k_1)`), the `e^{iqr}`
term is `A_{12}`, and `S_{12}=A_{12}/A_{21}=S(K,q)` — exactly D7's out/in
convention, and `S_phys` per notation.md ("`S_{12}` if `sgn(v_h−v_s)=+1`, else
`S_{21}`").

### O14 (MINOR) — "ε_j never enters ⟨1⟩5's Cook integral" is false as printed

⟨1⟩9.⟨2⟩2.  `ε` **does** enter ⟨1⟩5's Cook integral — it is the packet
parameter of `W_±^{(ε)}` in ⟨1⟩2.⟨2⟩1, and by O1 it drives the constants like
`ε^{-N}`.  What is true, and is the substantive point, is that **no `ε→0`
limit is taken inside the Cook integral**.  The brief predicts the critic will
"hunt for one place where `ε` enters a Cook integral"; the substance survives
the hunt, the sentence does not.
**FIX DEMAND.** "no `ε→0` limit is taken inside ⟨1⟩5's Cook integral; `ε`
enters only as a fixed packet parameter, with constants that diverge as `ε↓0`".
**SURVIVING.** The limit-order discipline is genuinely respected.

### O15 (MINOR) — D31(3) never displays translation covariance, on which the bound-band fence rests

⟨1⟩7.⟨2⟩2 ("Translation covariance of `a_i(n)` gives the analogous
total-momentum intertwining") and hence ⟨1⟩2.⟨2⟩2 (`P_BW_±=0`) require
`a_{i,b}(n)=τ_n(a_{i,b}(0))`.  D28(3) at least said "translation covariance
makes `χ_γ` independent of `n`"; D31(3) states only the normalisation
`a_{i,b}(n)Ω_A=Γ_M(χ_ie_n⊗e_b)`, which fixes the action on `Ω_A` and not the
operator.  The same relation is what makes the uniform commutator bound
`‖[D_1(x),a_2(y)]‖≤C_N⟨x−y⟩^{-N}` uniform in `x` when ported from source Lemma
`commutator-decay` (which bounds `[A_1,τ_y(A_2)]`, one fixed pair).
**FIX DEMAND.** Display `a_{i,b}(n)=τ_n(a_{i,b}(0))` in D31(3).
**SURVIVING.** With covariance displayed, ⟨1⟩5.⟨2⟩2 and ⟨1⟩7.⟨2⟩2 are correct.

---

## 4. NOTE

### N1 — D31(2)'s "isolated" holds only relative to the charge grading, and on the anchor model the band is *not* spectrally isolated

On D6, `ω(K)=2J sin²(K/2)`, while the two-magnon continuum at total momentum
`K` starts at `2J(1−cos(K/2))=4J sin²(K/4)`.  For small `K`,
`JK²/2 > JK²/4`: the one-magnon band is **embedded** in the two-magnon
continuum for every `K≠0`.  What isolates it is D31(1)'s conserved circle
charge, not spectral separation.  This is fine — indeed it is why D31(1)'s
charge clause is load-bearing — but the shard cites the source's mass-shell
notion (`mass-shell-definition`) in ⟨1⟩10.⟨2⟩1 without the qualifier, and a
reader importing that notion gets a false statement on the anchor model.  Add
one clause to D31(2): "isolated **within the charge-one sector**".

### N2 — favourable fact the shard does not use: `d_B` survives the soft limit

I computed `d_B` along `k_2=k_s→0` at fixed `k_1=k_h`: `c=cos(k_h/2)`,
`q→−k_h/2`, so `E_sc−E_b → J(1−c²)=J sin²(k_h/2)>0` for `0<|k_h|<π`.  So of the
four fence parameters, `ε_v→|v_h|`, `d_B→J sin²(k_h/2)`, `η_inel=+∞` all stay
bounded below in the soft limit; only `ε_0→0`, and `ε_0` is used nowhere.  This
strengthens the shard's position and is worth stating — it is also exactly why
O1's fence sentence is insufficient.

### N3 — ⟨1⟩2 forward-references ⟨1⟩7

⟨1⟩2.⟨2⟩2 is justified by "the standard intertwining computation proved in
⟨1⟩7.⟨2⟩2".  I checked for circularity: ⟨1⟩5 ASSUMEs ⟨1⟩4 and ⟨1⟩4 ASSUMEs
D31(2)–(4); neither depends on ⟨1⟩2, so there is none.  Under L6b, restate
⟨1⟩2.⟨2⟩2 as a corollary placed after ⟨1⟩7, or mark it "forward reference, no
circularity (⟨1⟩5 is independent of ⟨1⟩2)".

### N4 — matrix-valued vs scalar band

D31(2) writes `ω∈C²(𝕋)` (scalar) while D31(3)/⟨1⟩4.⟨2⟩2 use `h_{i,b'b}` and
`ℋ_{0,12}=L²(K_1;ℂ^m)⊗L²(K_2;ℂ^m)` (multiplicity `m`).  For `m>1` with a
degenerate band, `V_i=ω'(K_i)` is undefined as written.  D28(2) said "matrix
valued on the finite frame index"; D31(2) should say the same and define `V_i`
via the eigenvalue branches, or restrict to `m=1` where velocities are used.

### N5 — HONEST STATUS §"Assumed" phrasing collides with (A2M.2)

"…and **bound-band exclusion** are not used" reads against (A2M.2)'s "Their
ranges avoid every D31-listed bound-band projection".  The intended reading
(exclusion is not *assumed*; `d_B>0` is assumed and avoidance derived) is
correct and is a genuine advance over the AC-EX register — but say it that way.

### N6 — port audit result (obligation: verify each claimed VERBATIM PORT)

All five claimed VERBATIM PORTs check out against their cited locations:

| Shard step | Cited source | Verdict |
|---|---|---|
| ⟨1⟩4.⟨2⟩1 | `ansatz-scattering.md` ⟨1⟩3.⟨2⟩2–⟨2⟩3; source Thm `smearing-theorem` (l.874), Lem `almost-locality` (l.2545), eq `(wave-packet)` (l.1033) | **matches** — `almost-locality` does exist (appendix, l.2545: `A∈𝔄(Λ), f∈S(ℝ×Γ) ⟹ τ_f(A)∈𝔄_aloc`) |
| ⟨1⟩4.⟨2⟩2 | `ansatz-scattering.md` ⟨1⟩3.⟨2⟩4–⟨2⟩5 (ACE-filter) | **matches**, and is legitimately *cleaner*: in the one-vacuum rep the parent's `ω_γ(D^†D)=0` upgrades to the vector identity `D_{i,b}(n)Ω_A=0`, which (2M-Cook) uses twice |
| ⟨1⟩5.⟨2⟩3 | `ansatz-scattering.md` ⟨1⟩4 (ACE-SP); source Prop `norm-corollary` (l.1045), eq `(non-stationary)` (l.1050) | **matches** at `d=1`: `‖g_t‖_1=O(t^d)=O(t)`, `‖χ_{-,t}g_t‖_1=O(t^{-∞})`.  D28(4)'s three velocity **sign** conditions are absent from D31(4) but are not needed for the cone bound |
| ⟨1⟩6.⟨2⟩3 | `ansatz-scattering.md` ⟨1⟩6.⟨2⟩2 | **matches** (polarization/extension added, trivially valid) |
| ⟨1⟩7.⟨2⟩1 | `ansatz-scattering.md` ⟨1⟩6.⟨2⟩4 | **matches** |

The ADAPTED steps (ACE-tail ⟨1⟩3.⟨2⟩6, ACE-Cook ⟨1⟩5.⟨2⟩2, ⟨1⟩5.⟨2⟩5,
ACE-Gram ⟨1⟩6.⟨2⟩1) all point at the right parent steps.  ⟨1⟩5.⟨2⟩5's
reference-hypothesis claim — "The source uses `HR-auxiliary(a)` to kill the
one-particle derivative; exact ansatz equations and **2M-Cook** replace
precisely that source hypothesis here" — is **accurate**: source Thm
`Haag-Ruelle`'s proof reads "Due to Lemma~\ref{HR-auxiliary}~(a),
`∂_t(B^*_{i,t}(g_{i,t}))` annihilates `Ω`."  Source Thm `clustering` (l.664)
does assume "a lower mass gap", so ⟨1⟩10.⟨2⟩2's "permitting gapless D6" is
honest.  The **one missing port** is the final clause of Thm `Haag-Ruelle`
(creator independence) — see O5.

### N7 — checker semantics vs the pre-registered probe

A2M-C1 is a new, self-contained certificate; it does not touch or contradict
the frozen P1–P4 semantics of `theory/checks/soft_index_probe.py`.
`--selftest` was run: **`selftest PASS`, exit 0**.  The shard correctly did not
edit `theory/checks/`.

### N8 — REFUTED-row audit: clean

Depends-on is `D1, D2(a), D3(a), D6–D8, D12(a′), D31, ML2, S2-2body`.  No
reliance on ML5, on the withdrawn `S2` label, on M-INDEX-LA-strong, on ML1/ML3/
ML6.  Nothing contradicts D24(e)'s `O_η` counterexample (no source
quantification appears anywhere) or the G0-soft-r1 kinematic-factor fence (no
soft factor is computed).  D2(a) is unused (O10) but harmless.

---

## 5. Register comparison against the adjudicated AC-EX row (obligation)

| Item | AC-EX adjudicated register | AC-EX-2M | Verdict |
|---|---|---|---|
| Cook/isometry | "proved **only** as the conditional implication" from D28 | proposer status says the same from D31 | **in register** |
| clustering | "(D28-C) is the load-bearing hypothesis and is **unverified on any model**" | D31-C2 **derived** from D1(c,d); C2 verified numerically | **stronger, and earned** — the lane's real advance |
| bound states | "No … bound-state exclusion … is claimed"; "An uncomputed wall–magnon bound band is not excluded" | `P_BW_±=0` for **D31-listed** bands | **stronger, but with a stronger hypothesis** (D31(5) `d_B>0`), and the argument is sound |
| thresholds | "Remark D28-R's threshold inequalities are used in no step" | D31(5)'s `η_inel/Θ_inel` **are** used (⟨1⟩7.⟨2⟩2) | in register (they are hypotheses of D31, not a fence) |
| completeness / range | "No completeness…"; "No assertion is made … that `H_out^{ex}` exhausts a spectral subspace" | ⟨1⟩7.⟨2⟩4 claims the **entire** ML2 scattering summand | **OUT OF REGISTER — O5** |
| soft limit | "no soft limit is claimed" | soft scale strictly last, `W_±^{(ε)}` fixed-`ε` only | in register, modulo O1/O14 wording |

One breach (O5).  Everything else is either in register or legitimately
stronger because D31 assumes more than D28.

---

## 6. Summary

- **FATAL 0**
- **MAJOR 6** — O1 (fence parameters omit the packet seminorms, where the
  `ε`-divergence lives), O2 (interface clause 5 assumes the soft-leg LSZ
  identification, i.e. assumes (A2M.3)'s bridge), O3 ((SR)/⟨1⟩9.⟨2⟩2 limit-order
  inconsistency; the AA-usable reading makes (SR) soft-uniform and leaves
  `A_j(0)` undefined), O4 (the D6 (SR) instance is not established;
  ⟨1⟩9.⟨2⟩3 contradicts ⟨1⟩9.⟨2⟩4), O5 (⟨1⟩7.⟨2⟩4's completeness claim is
  unproved and contradicts the claims row), O6 (A2M-C1 does not certify
  MPS-2M-cluster's load-bearing content)
- **MINOR 9** — O7–O15
- **NOTE 8** — N1–N8

The core of §§0–3 — the D31-C2 derivation, the Cook estimate, the isometry, the
bound-band fence, and the exact ML2/D7 match — is **sound and independently
reproduced**.  The failures are (i) one over-reach at ⟨1⟩7.⟨2⟩4 and (ii) the
whole of §4, where the "nonvacuity bridge" that justifies Lane S2's existence
is carried by interface clause 5 and by an (SR) hypothesis whose quantifiers do
not parse.  (A2M.1)–(A2M.2) can be promoted to SKETCH after O5–O8 and O11–O15;
(A2M.3) cannot be promoted at any strength until O2–O4 are answered.

**FAIL(O1,O2,O3,O4,O5,O6)**
