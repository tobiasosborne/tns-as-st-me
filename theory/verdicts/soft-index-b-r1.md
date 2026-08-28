<!-- ROLE: r1 adversarial critic verdict on theory/soft-index-b.md (Lane S1-B,
     independent Fable prover, Theorem S-INDEX).  Work order:
     briefs/soft-critic-r1.md (S1 specialization).  Writable lane: THIS FILE
     ONLY.  All computations below were run on private copies in the session
     scratchpad; no shared file was edited and theory/checks/ was not touched. -->

# r1 verdict — `theory/soft-index-b.md` (Lane S1-B)

**Verdict: FAIL(F1, F2, M1, M2, M3, M4, M5, M6, M7).**
2 FATAL, 7 MAJOR, 11 MINOR, 4 NOTE.  Cross-lane section at the end.

## 0. What I did (obligations 1–5)

**Independent recomputation (not refereeing).**  I built the spin-`S`
isotropic ferromagnet `H_S=−JΣ_x(S_x·S_{x+1}−S²)` from scratch in the FULL
Hilbert space (no repo import, no magnon-basis shortcut), for
`(S,N) ∈ {(1/2,8),(1/2,10),(1,5),(1,6),(1,7),(3/2,5)}`, with
`j^-_{x|x+1}=−[h_{x,x+1},S^-_x]`, `j^z_{x|x+1}=−[h_{x,x+1},S^z_x]` (D10(a)),
`Q_k=Σ_xe^{ikx}S^-_x`, and re-derived, by direct linear algebra:

| step | shard location | result |
|---|---|---|
| `[S^+_{tot},J^-_0]=2J^z_0` | ⟨1⟩2.⟨2⟩1 | **exact** (0.00e0 / 1.6e-15) — CONFIRMED |
| `‖Q_0ψ‖²=2M‖ψ‖²` on `ker S^+` | ⟨1⟩2.⟨2⟩2 ⟨3⟩1 | **exact**, `n=1,2,3`, `S=1/2,1` (≤7e-15) — CONFIRMED |
| `⟨h|J^z_0\|h⟩=iv(h)`, and `J^z_0` diagonal | ⟨1⟩2.⟨2⟩3 ⟨3⟩2 | **exact** at `S=1/2,1,3/2`, every `h≠0` (≤1e-15) — CONFIRMED |
| Ward residue `⟨h\|Q_0^†J^-_0\|h⟩=2iv(h)` | (B14) bullet 1, SIB-C3 | **exact and `ρ`-INDEPENDENT** at `S=1/2,1,3/2` — CONFIRMED |
| `P_{n,N}J^-_0=Q_0J^z_0/M` on `ker S^+` | (B4) | **TRUE at `n=1`, FALSE at `n≥2`** — see **F1** |
| contact defect support `{\|x−y\|≤1}` | ⟨1⟩2.⟨2⟩4 ⟨3⟩2 | **CONFIRMED** at `S=1/2,1,3/2` (≤3e-15 outside) |
| `‖𝔇‖=J\|z_k−1\|\|z_h−1\|` at `S=1/2` | (B9) | **exact** to 1e-15 — CONFIRMED |
| Duhamel identity (B8) | ⟨1⟩3.⟨2⟩1 | **exact** (1.5e-14 vs ‖LHS‖=3.4); mutation (drop the `e^{-iω(k)s}` phase) → 1.9e0 — CONFIRMED, mutation-killed |
| `ℛ(0)=1` "at every finite index" | (B6) | **FALSE at `S≥1`; tautological at `S=1/2`** — see **F2** |
| descendant/shell separation on fiber `K=k+h` | SIB-L1(i) | separation `= k·v(h)+O(k²)`, i.e. `Θ(ε)` not `Θ(1)` — see **M3** |

**Checker audit.**  `python3 -O theory/checks/soft_index_probe.py --selftest`
→ `selftest PASS`, exit 0.  Frozen results re-read from
`soft_index_probe_results.json` (P1 `S=1/2` slope 1.9929, `S=1` 1.0217; P2
`protocol_eta_diff = 0.0`; P3 growth 20.499 / smeared max-over-median 1.392;
P4 geometry-limited).  I read `phase_function`, `run_p2`, `run_p3` line by
line against the shard's CHECKER SPEC and against the frozen P1–P4 semantics
of `briefs/soft-index-target.md`; findings in **m4, m5, m6**.

**Quantifier/limit-order audit, vacuous-truth attack, ML4-Q1 attack, B10
box attack, REFUTED-row audit, lockstep audit, HONEST-STATUS audit:** below.
No mutation or edit was made to any shared file.

---

## FATAL

### F1. (B4) — the general-sector Ward projection is FALSE for `n≥2`; the shard states it "for every `N`, every `n` with `M>0`" and enters it in CLAIMS

**(a) Location.**  §0 (S-IDX.0) bullet; `⟨1⟩2` ASSUME ("every `N`, every `n`
with `M>0`, every packet"); `⟨1⟩2.⟨2⟩2` display (B4) and its `⟨3⟩2`;
`⟨1⟩5.⟨2⟩1` clause (2) ("this is (B4)--(B5), PROVED in ⟨1⟩2 for every `N`,
every sector, `ρ` free"); MERGE PROPOSALS §M3 row `S-IDX-fin-B`.

**(b) My independent computation.**  With `D=Q_0|_{ℋ_{n,N}}`,
`P=D(D^†D)^{-1}D^†` (ML4 ⟨1⟩1 (2)), and `ψ` running over an orthonormal basis
of `ker S^+∩ℋ_{n,N}`:

```
S=1/2 N=8   n=1 M=3 : ||P J^-_0 ψ − Q_0J^z_0ψ/M||  = 1.4e-16      (rhs 2.3e-1)
S=1/2 N=8   n=2 M=2 : ||P J^-_0 ψ − Q_0J^z_0ψ/M||  = 1.51e-01     (rhs 4.8e-1)
S=1/2 N=8   n=3 M=1 : ...                          = 4.84e-01     (rhs 9.1e-1)
S=1   N=6   n=2 M=4 : ...                          = 1.03e-01     (rhs 6.6e-1)
S=1   N=6   n=3 M=3 : ...                          = 2.07e-01     (rhs 7.9e-1)
```
Same failure with `P` built from `D` restricted to `ker S^+` instead
(`n=2`: 2.52e-01).  Meanwhile the *correct* general form
`P J^-_0 = D(D^†D)^{-1}(2J^z_0)` — i.e. ML4 (10) restricted to `ker S^+` —
holds to `≤6e-15` at **every** `n` tested.

**Mechanism (I verified it directly).**  `⟨3⟩2` replaces `(D^†D)^{-1}` by the
scalar `(2M)^{-1}` after applying it to `2J^z_0ψ`.  That is legitimate only if
`J^z_0ψ∈ker S^+`, since `D^†D=2M` holds **only on `ker S^+`**.  But
`[S^+_{tot},J^z_0]=−J^+_0`, and I measure `‖S^+J^z_0ψ‖`:

```
S=1/2 N=8: n=1 → 6.9e-18 (zero)   n=2 → 1.20    n=3 → 0.83
S=1   N=6: n=1 → 2.2e-16 (zero)   n=2 → 1.19    n=3 → 2.36
```
`n=1` is special because `J^+_0|h⟩∈ℋ_{0,N}=ℂ|Ω⟩` and zero-momentum current
conservation kills it for `h≠0`.  There is no analogue at `n≥2`.

**(c) FIX DEMAND.**  Restate (B4) as
`P_{n,N}J^-_0 = 2D_{n,N}(D_{n,N}^†D_{n,N})^{-1}J^z_0` on `ker S^+`, and state
the scalar form `Q_0J^z_0/M` **only** under the extra hypothesis
`J^z_0ψ∈ker S^+` — proved for `n=1` (and for that reason only for one hard
leg).  Delete "every sector" from `⟨1⟩5.⟨2⟩1` clause (2) and from the
`S-IDX-fin-B` row.

**(d) SURVIVING WEAKER STATEMENT.**  On `ker S^+∩ℋ_{1,N}` (one hard magnon,
any `N`, any packet supported away from `h=0`, any `S`, `ρ` free):
`D^†D=2M·1` with `M=ρN−1`, `P_{1,N}J^-_0|h⟩=(iv(h)/M)Q_0|h⟩`, and
`⟨h|Q_0^†J^-_0|h⟩=2iv(h)`.  All three verified exactly by me at
`S=1/2,1,3/2`.  Everything the shard actually *uses* downstream is inside
this surviving statement.

**NOTE for the orchestrator (out of my lane, but load-bearing).**  The
defect is inherited: `ml4-ward-reduction.md` (9) states the scalar form "on
the highest-weight subspace `ℋ^{hw}_{n,N}`, `n<N/2`" and (18) states
`P_{2,N}J^-_0=2Q_0J^z_0/(N−4)` "on the ML2 highest-weight subspace".  My
`n=2` computation refutes both as stated.  `ML4-Ward` is a **PROVED** row in
`claims/CLAIMS.md`; its `n≥2` clause needs the same repair (its `n=1`
consequence (11)/(R15) is untouched and I re-verified it).  This is a corpus
finding, not a lane-B finding — recorded here because S1-B cited it faithfully.

### F2. (B6) — "the `k=0` fiber of the datum is exactly `1` at every finite index" is false at `S≥1`, and vacuous at `S=1/2`

**(a) Location.**  §0 (S-IDX.0) last sentence; `⟨1⟩2.⟨2⟩4` display (B6)
("Adjoin the `k=0` row to the readout (B3) … Then, for EVERY `(N,T,W,σ)`:
`ℛ(0)=1` exactly"); `⟨1⟩8.3` ("The Adler zero (B6)/(B12) is derived from
`[H,Q_0]=0` …"); §M3 row `S-IDX-fin-B` ("the `k=0` fiber of the protocol
datum is exactly `1` at every finite index").

**(b) My independent computation.**  Under the only concrete kernel
convention in the repo — the probe's `fft2` of the symmetrised pair grid,
which the shard itself endorses ("`phase_function` implements exactly this
readout"), I formed the *running* family `Φ(0)=Σ_{k∈Λ}f(k)Q_kψ_{g}`,
evolved exactly, and evaluated the adjoined `k=0` row of (B3):

```
S=1/2 N=10  Λ={2π/N,4π/N} : running family  ℛ(0) = 1.0000000000 − 0.0e0   |ℛ(0)−1| = 6.9e-16
S=1   N=7   Λ={2π/N,4π/N} : running family  ℛ(0) = 2.1633 + 0.1527i        |ℛ(0)−1| = 1.17e+00
S=1   N=7                  : PURE Q_0-created datum  ℛ(0) = 1.0000000000   |ℛ(0)−1| = 9.5e-16
```
So the boxed "for EVERY `(N,T,W,σ)`" claim is **false at `S≥1`**.  The proof
`⟨3⟩1` silently evaluates a *different* object — the datum of the pure
`Q_0`-created state `Φ=Q_0ψ_g` — for which `ℛ(0)=1` does hold at every `S`
(momentum conservation confines `Q_0|h'⟩` to fibre `h'`).  Statement and
proof are about different vectors.

Worse, in the reading where the claim *is* true (`S=1/2`), it carries **no
protocol content**: I ran the same readout on a *random* (not charge-created,
not even Ward-related) two-magnon state:

```
S=1/2 N=10  random 2-magnon state : ℛ(0) = 1.000000000000   |ℛ(0)−1| = 2.1e-15
S=1   N=6   random 2-magnon state : ℛ(0) = 0.9548 + 0.1014i  |ℛ(0)−1| = 1.1e-01
```
At `S=1/2` the `(0,c)` grid-Fourier mode *is* the descendant `Q_0|c⟩`, which
is an exact eigenvector; hence `ℛ(0)=1` for **every** initial state.  It is a
tautology of the readout convention, not an "exact finite-`N` Adler value" of
the charge-created protocol.

**(c) FIX DEMAND.**  Either (i) restate (B6) for the pure `Q_0`-created
datum, and then say in the same sentence that at `S=1/2` the same identity
holds for arbitrary two-magnon input, so it is a property of the readout and
not of the protocol; or (ii) keep the adjoined-row formulation and prove it
at `S≥1` — which my computation says is impossible.  Either way, fix D29's
undefined "momentum kernel" (see m7) first, because the truth value depends
on the convention.

**(d) SURVIVING WEAKER STATEMENT.**  For the `Q_0`-created state
`Φ=Q_0ψ_{g,σ}` (soft profile `f≡1`), at every `S`, `N`, `T`, `W`:
`ℛ(0)=1` exactly, because `[H,Q_0]=0` and `ω(0)=0`.  This is a one-line
consequence of `SU(2)` invariance and says nothing about `lim_{ε→0}` of the
family, since (by B10, the shard's own construction) no admissible index of
the family is continuously connected to it.

---

## MAJOR

### M1. `⟨1⟩4` — the headline conditional theorem uses **no part of (S-IDX.0)**; the "soft-index" content is decorative at the anchor

**(a) Location.**  `⟨1⟩4` ASSUME and `⟨2⟩1`–`⟨2⟩2` in full, versus §0's
framing and the campaign register sentence.

**(b) My computation/audit.**  Step-by-step leaf audit of `⟨1⟩4`:
`⟨2⟩1` (SIB-L1) cites ML2, ML4 ⟨1⟩4.⟨2⟩1, (R16), D8; `⟨2⟩2.⟨3⟩1` cites
(TGT2), SIB-L1, (TGT4), `⟨2⟩3`; `⟨2⟩2.⟨3⟩2` cites S2-2body-S (T.2)–(T.3),
(R17), (B3), (B11); `⟨2⟩2.⟨3⟩3` cites `⟨3⟩2`, `[S^+,Q_k]=2Q^z_k`, (R4),
ML4 (16).  **(B4), (B5), (B6), (B7), (B8), (B9) appear in no leaf of
`⟨1⟩4`.**  Removing `⟨1⟩1.⟨2⟩4`–`⟨1⟩3` entirely leaves `⟨1⟩4` intact.
Hence the anchor theorem is exactly: *`S2-2body-S` (PROVED) + a hypothesis
that the protocol readout settles onto exact-eigenvector chamber ratios*.
The advertised inversion ("symmetry fixes the soft law; dynamics only picks
the values") is not realised here: symmetry (the Ward index identity)
contributes nothing to the value, and the hypothesis contributes the channel
identification.

**(c) FIX DEMAND.**  Either route `⟨1⟩4`'s value through (B4)–(B5) (i.e.
derive the settled row value from the Ward residue plus a flux factor, as
`⟨1⟩5` attempts), or state plainly in §0 and HONEST STATUS that (S-IDX.1a)
is independent of (S-IDX.0) and that the two rungs share only the datum.

**(d) SURVIVING WEAKER STATEMENT.**  (S-IDX.1a) is a corollary of
S2-2body-S under D29-B+D30-B(a,b,d); (S-IDX.0) is a separate, unused,
finite-volume identity (repaired per F1).

### M2. (TGT2) hands the conclusion to the hypothesis: (S-IDX.1a) is a computation, not a constraint — and has no proved instance

**(a) Location.**  `⟨1⟩4` ASSUME (TGT2), display (B11); D30-B(b) merge text
§M2; defended at `⟨1⟩8.8`.

**(b) My analysis.**  (B11) asserts
`ℛ_j(k)=Σ_hϱ_j(k,h)·r_{out/in}[B_j(k,h)]+η_j(k)` with `B_j` exact
near-shell eigenvectors and `η_j→0`.  Combined with SIB-L1(ii)–(iii)
(roots within `C_Iδ_j`, chamber ratio = the exact contact value) the datum
is *determined* to `o(1)`: `ℛ_j(k)=S_{12}(κ_1,κ_2)+O(δ_j)+O(η_j)`.  Nothing
is left for the theorem to constrain; the "limit point" language is
decoration on a hypothesis that already names the object the limit is.  The
shard's own defence "(TGT2) fixes the value of NO ratio" is true only in the
weak sense that the *numerical* value is then read off `S2-2body-S`; the
*channel identification* — the whole content of an LSZ/soft theorem — is
assumed.  Contrast D27(LR1–LR2), the claimed analogue: those assume
convergence of a protocol *outcome law* and a nondemolition defect, not that
the outcome law equals the spectral data of a named family of eigenvectors.
Second half: (TGT2) has **no proved instance**.  `⟨1⟩1.⟨2⟩3` proves only
*definedness* at finite index (a much weaker thing, correctly labelled);
`⟨1⟩7.⟨2⟩3` derives (TGT2) from ML1+ML6 **with the interchange step admitted
as not derived**; probe P1 is empirical at `N≤32`.  So the shard's answer to
the vacuous-truth landmine is honest at the level of wording but the
hypothesis is unrealised in every register.

**(c) FIX DEMAND.**  State (S-IDX.1a) as: "under (TGT2), the settled datum
equals the exact two-body multiplier, whose jet is `sgn/S` by S2-2body-S" —
i.e. advertise it as a *transfer* theorem, not a constraint theorem — or
weaken (TGT2) to something that does not name eigenvectors (e.g. tightness
of a spectral measure attached to the readout plus the Ward residue), which
is what the target brief asked for.

**(d) SURVIVING WEAKER STATEMENT.**  Under D29-B + (TGT1)+(TGT2)(+(TGT4)),
every subsequential limit point of the aggregate datum is a convex-combination
limit of exact two-magnon chamber ratios and therefore inherits S2-2body-S's
Adler zero and slope `sgn(v_h−v_s)/S`.  No independent soft-theorem content.

### M3. SIB-L1 is false as stated — the descendant sits `Θ(ε)`, not `Θ(1)`, from the shell; and (TGT2) does not restrict `B_j` to `ker S^+`

**(a) Location.**  `⟨1⟩4.⟨2⟩1` LEMMA SIB-L1 statement (i) and its proof
`⟨3⟩1` (which contains an unresolved in-line "— wait:" and a "Repair" that is
never applied to the lemma statement); applied at `⟨1⟩4.⟨2⟩2.⟨3⟩1`.

**(b) My independent computation.**  On the fibre `K=k+h` the descendant
`Q_0|K⟩` has energy `ω(K)`, so its distance to the two-magnon shell is
`ω(k+h)−ω(k)−ω(h)`.  Exactly:

```
S=1/2 h=π/2 : k=0.500 → 0.357008 (k·v(h)=0.500)   k=0.100 → 0.094838 (0.100)
              k=0.050 → 0.048729 (0.050)          k=0.020 → 0.019799 (0.020)
S=1   h=π/2 : k=0.100 → 0.189675 (0.200)          k=0.020 → 0.039597 (0.040)
```
i.e. the separation is `k·v(h)+O(k²) = Θ(ε)`.  SIB-L1 claims
"there is `δ_I>0` (depending on `I`, `ε_I` only)" such that `δ≤δ_I` excludes
the descendant.  **False**: for any fixed `δ_I` pick `k<δ_I/v(h)`.  The
correct threshold is `δ ≲ c·|k|`, i.e. `ε`-dependent.  The bound-band and
`K=π` exclusions *are* `Θ(1)` (ML4 ⟨1⟩4.⟨2⟩1.⟨3⟩4) — only the descendant
branch fails, exactly as the author's own "wait" spotted.
The attempted repair ("(i) holds for … `B∈ker S^+`") does **not** cover the
use: (TGT2)/(B11)/D30-B(b) quantify over "exact eigenvectors `B_j(k,h)` of
`H_S` on `ℋ_{2,N_j}` in the total-momentum fibre `k+h`", with **no
highest-weight restriction**.  `⟨2⟩2.⟨3⟩1` then applies SIB-L1(i) to them.
The parenthetical in `⟨2⟩2.⟨3⟩3` handles a different object (the descendant
*admixture of `Φ(0)`*), not descendant *eigenvectors admitted by (TGT2)*.

**(c) FIX DEMAND.**  (1) Restate SIB-L1 with the threshold `δ≤c_I|k|` and
carry the resulting `j≥j_1(ε)` in `⟨2⟩2.⟨3⟩1`; (2) add `B_j(k,h)∈ker S^+`
to D30-B(b)/(B11) — or prove that descendant eigenvectors carry no readout
weight, which is a different estimate from the `(R4)` one given.

**(d) SURVIVING WEAKER STATEMENT.**  For `S=1/2`, `h∈I`, `0<k≤ε_Ic_2`, and
`B∈ker S^+` on fibre `K=k+h` with `|E_B−ω(k)−ω(h)|≤δ≤min(δ_I, c_I k)`:
`B` is a regular D7-representable scattering vector with roots within `C_Iδ`
of `(k,h)` and chamber ratio `S_{12}(κ_1,κ_2)`.  (Unconditional at `S=1/2`
via ML2 as claimed; the `ε`-dependence of the threshold is the repair.)

### M4. (B14) — the density factor `1/(2ρ)` is asserted, its own justification does not produce it, and it is checkable only where it equals `1`

**(a) Location.**  `⟨1⟩5.⟨2⟩2` box (B14), bullet 2 ("soft-leg
normalization"), and the displayed product; `⟨1⟩7.⟨2⟩2` ("the two routes
agree BECAUSE …"); §M3 row `S-IDX-desc-B`; CHECKER SPEC SIB-C3.

**(b) My independent computation.**  I verified every *other* factor in the
product and they are all `ρ`-independent:
* Ward residue `⟨h|Q_0^†J^-_0|h⟩ = 2iv(h)` — measured `2iv` at `S=1/2`
  (1.414i, 2.000i), `S=1` (3.464i), `S=3/2` (5.706i, 3.527i), i.e. exactly
  `2i·2JS sin h` with **no** extra `S`-dependence;
* flux factor `L(0,h)=−iχ/v_h` — this is D24(d)3 *verbatim*, which the shard
  says it transplants verbatim as (3′);
* kinematic `(e^{ik}−1)=ik+O(k²)`.
ML5-B (6) closes exactly this product at `2χ` with **no** residual factor
(`ml5-universality.md` ⟨2⟩1.⟨3⟩2).  So the entire `ρ`-dependence of the
campaign's headline law rides on the one inserted factor.  Its stated
justification is `‖Q_{k_s}|Ω⟩‖²=2ρN`, hence "one unit-normalized soft magnon
carries `(2ρN)^{-1/2}`" — I confirm `‖Q_k|Ω⟩‖²=2ρN` (it is
`Σ_x⟨Ω|2S^z_x|Ω⟩`) — but `(2ρN)^{-1/2} ≠ (2ρ)^{-1}`: the power is wrong and
an uncancelled `N^{-1/2}` is dropped without comment.  No step supplies the
missing `√N` or the second half-power.  The factor is verified nowhere except
`ρ=1/2`, where it is `1`.  Consequently `⟨1⟩7.⟨2⟩2`'s "consistency anchor
(b)" is **not** a cross-check: `⟨1⟩4` obtains `1/S` from the PROVED spin-`S`
contact algebra (where the `S`-dependence is genuinely dynamical — `μ=(2S−1)a+b`
in (T.2)), while `⟨1⟩5` obtains `1/ρ` from a factor tuned to agree with it.
SIB-C3's proposed red mode (`leg norm → ρN` ⟹ jet `2/ρ`) tests the arithmetic
of the inserted factor, not its derivation.

**(c) FIX DEMAND.**  Derive the soft-leg normalisation factor from the D29-B
datum itself (the datum is a *ratio*, so state precisely how the leg norm
enters `M_2` and not `M_1`, and where the `N`-dependence cancels against the
`f_ε` packet normalisation) — or scope (B14), `S-IDX-desc-B`, and the
"abstract descendant-projected law" to `ρ=1/2` (ML5-B's register), exactly as
`⟨1⟩6`/(S-IDX.2) already scopes itself.

**(d) SURVIVING WEAKER STATEMENT.**  At `ρ=1/2` (the D6 register), under
(1′),(3′),(4′): the descendant-projected limit datum has jet
`2·sgn(v_h−v_s)` — this is ML5-B (5) transplanted, with the Ward residue
`2iv_h` now verified at every `S`.  The `1/ρ` generalisation is a
CONJECTURE of this shard, not a proved bookkeeping.

### M5. `⟨1⟩5.⟨2⟩1` — the discharge of D24(d) clause 5 is an unresolved in-line "wait" and double-counts a kinematic factor

**(a) Location.**  `⟨1⟩5.⟨2⟩1`, clause (5), the passage beginning "— wait:
(H-band) gives only `O(k)`".

**(b) My analysis.**  D24(d)5 requires the contact term bounded by
`C_I|k|²‖M_1‖`.  The shard's chain is: (H-band) gives `‖𝔇‖≤C_I|k|`; (tr′)
prevents the time integral from growing; "the second power is the kinematic
`ik_s` of (3′)".  But by my own verification of (B9),
`𝔇(k,h)=(J/√N)(z_k−1)(z_h−1)|C_K⟩` **already contains** the single factor
`(z_k−1)` — it *is* the `O(k)` of (H-band).  There is no second, independent
`(e^{ik_s}−1)`: (B8) inserts `𝔇` directly, with no further kinematic
prefactor.  Multiplying by (3′)'s `(e^{ik_s}−1)` counts the same profile
difference twice, which is precisely the `G0-soft-r1` failure mode the shard
fences elsewhere (`⟨1⟩8.3`).  Note also that the naive bound on (B8) is
`T·sup‖𝔇‖`, and `T_j→∞` along every admissible subsequence, so (tr′) is not
a mild regularity clause: it is the whole dispersive/transit estimate.
Consequence: the advertised "structural advance over ML5-B — two of five
D24(d) clauses genuinely discharged" is established for clause 2 only (and
that one only at `n=1`, per F1); clause 5 is **replaced** by (tr′)+(H-band),
which deliver `O(k)`, one power short.

**(c) FIX DEMAND.**  Either exhibit the second power (name the operator whose
matrix element carries it, and show it is not the `(z_k−1)` already inside
`𝔇`), or downgrade the advertised gain to "clause 2 discharged at one hard
leg; clause 5 replaced by the named hypothesis (tr′) at strength `O(k)`",
and propagate the `O(k)` (not `O(k²)`) into the `⟨2⟩3` conclusion — where it
contaminates the linear jet and therefore breaks (B14) as stated.

**(d) SURVIVING WEAKER STATEMENT.**  Under (H-band)+(tr′) the contact/transit
channel is `O(k)` uniformly in the subsequence, which suffices for the Adler
zero `|𝒜|≤Cε` but **not** for the jet; the jet statement (B14) requires
`O(k²)` and must therefore keep D24(d)5 as an assumption, giving 1 of 5
clauses discharged, not 2.

### M6. `|q|` overclaim: every proof step has `|q|=1`, the boxes and the claim row state `|q|/ρ`

**(a) Location.**  §0 (S-IDX.1a)(ii); (B13) (which itself writes
"`ρ=S, |q|=1`"); (B14) box; `⟨1⟩5` ASSUME ("`|q|=1` soft leg"); §M3 rows
`S-IDX-spec-B` and `S-IDX-desc-B`, both of which state the law as
`sgn(v_h−v_s)|q|/ρ` with no `|q|=1` scoping; HONEST STATUS (does **not** list
this as a retreat).

**(b) My audit.**  No step of the shard treats a charge-`|q|>1` leg.  The
hard leg is a single magnon throughout (`ℋ_{1,N}`, `n=1`), and (B14)'s
derivation ends at "`i sgn k_s/ρ`, i.e. `|q|/ρ` at `|q|=1`" — the `|q|` is
inserted, not derived.  `claims/CLAIMS.md` records the `|q_hard|>1` factor as
**open** (`Bc`, bd `tns-ebh`), the target brief pre-registers P4 as *evidence,
not a gate*, and the frozen P4 record is `"status": "geometry-limited"` with
an explicit warning that its number "must not be read against the
prediction".  So `|q|/ρ` in a SKETCH row would enter the DAG a claim the
corpus explicitly holds open.  The other S1 lane refuses exactly this step
(see X4).

**(c) FIX DEMAND.**  Replace `|q|/ρ` by `1/ρ` in (B13), (B14) and both claim
rows, and add a sentence stating that the `|q|>1` factor is Conjecture `Bc`
and is untested (P4 geometry-limited).

**(d) SURVIVING WEAKER STATEMENT.**  For a single primitive magnon leg
(`|q|=1`) the jet is `sgn(v_h−v_s)/ρ`; the extension to `|q|>1` is Bc, open.

### M7. Lockstep: the headline states a pointwise jet `∂_{k_s}arg 𝔯^*|_0`; the proof delivers a profile-averaged ratio, and D29-B has no soft-width limit at all

**(a) Location.**  §0 (S-IDX.1a)(ii) ("`∂_{k_s}arg 𝔯^*|_0 = …`") versus
`⟨1⟩4.⟨2⟩2` (B13) and its `⟨3⟩3` ("hence the jet
`lim_{ε→0}arg(1+𝖲^*(ε))/\bar k_w(ε)`"); §M3 row `S-IDX-spec-B`
("`∂arg(1+𝖲^*)|_0`").

**(b) My audit.**  `𝖲^*` is a function of `ε` only; `\bar k_w(ε)∈[c_1ε,c_2ε]`
is the *weighted mean row momentum of the profile*.  `arg(1+𝖲^*(ε))/\bar
k_w(ε)` is not the derivative at `0` of any function of `k_s`: D29-B's soft
parameter is a *scale* (`f_ε(k)=ε^{-1/2}f(k/ε)`, support `(c_1ε,c_2ε)`), and
there is **no independent soft width** that could be sent to zero to recover
a pointwise `k_s`.  The ratio does converge to `sgn/S`, so the statement is
true as written in `⟨3⟩3` — but it is a different (weaker, profile-dependent
normalisation) statement from the target template's `∂_{k_s}arg 𝖲^*|_0`, and
from what the claim row will advertise.  Related smaller mismatch: §0
attributes the Adler zero to "O6/OR2 + (R16)-uniformity"; `⟨1⟩4` derives it
from the (T.3) expansion via (TGT2), and OR2/O6 appear in no leaf of the
proof.

**(c) FIX DEMAND.**  Write the conclusion as
`lim_{ε→0}arg(1+𝖲^*(ε))/\bar k_w(ε) = sgn(v_h−v_s)/ρ` in §0, in (B13) and in
`S-IDX-spec-B`, and say in one sentence why D29-B cannot state a pointwise
`k_s`-derivative (no width parameter).  Fix the Adler-zero attribution.

**(d) SURVIVING WEAKER STATEMENT.**  As above: an averaged-slope law with an
explicitly profile-dependent normalisation; equal to the pointwise jet only
if a `σ`-type soft-width parameter is added to D29-B (as the other lane does).

---

## MINOR

**m1. `M := ρN − n|q|` (§0, S-IDX.0 bullet) vs `M := ρN − n` (`⟨1⟩2` ASSUME).**
The sector value of `S^z_{tot}` after `n` applications of `S^-` is `ρN−n`
regardless of the hard leg's charge; my `‖Q_0ψ‖²=2M` runs confirm `M=ρN−n`
at `n=1,2,3`.  FIX: delete `|q|` from §0.  Surviving: `M=ρN−n`.

**m2. "`ρ` carried as a FREE real parameter" is empty in this shard's own
register.**  H-SIDX.1 assumes a *fully polarized highest-weight* vacuum of an
`SU(2)`-invariant chain with on-site charge `S^z`; that forces
`ρ=ω_Ω(S^z_x)=S∈½ℤ`.  Nothing *assumes* `ρ∈½ℤ` (so the campaign landmine is
not stepped on), but the advertised generality — and the M-IDX-density
precedent invoked in §0 — does not survive the hypotheses.  Additionally, the
exact identity `M=ρN−n` needs `ρN∈spec S^z_{tot}` for every `N` in the
subsequence.  FIX: say "`ρ=S` in this register; the free-`ρ` statement is the
abstract *form* of the identity, not an instantiable generalisation" (the
other lane's `m_λ/N_λ→ρ` is the honest version — X3).

**m3. The advertised "offset bookkeeping in public" stops before the
cancellation.**  `⟨1⟩2.⟨2⟩2` displays `2M=2(ρN−n)=N−2n=2SN−2n` but never
performs the step that actually matters:
`⟨h|Q_0^†P_{1,N}J^-_0|h⟩=(2iv_h/2M)·‖Q_0|h⟩‖²=2iv_h`.  The `2iv_h` then
appears in (B14) cited to "(B4)--(B5)" with the pairing step missing.  I
verified the cancellation numerically at `S=1/2,1,3/2`.  FIX: display it (the
other lane does — SIDX.8).

**m4. "`phase_function` implements exactly this readout" is false.**  Read
against `theory/checks/soft_index_probe.py` lines 246–284: the probe (i) never
forms (B3)'s aggregate `𝔯=Σ_kw_ε(k)ℛ(k)/Σ_kw_ε(k)` — it returns per-row
phases and fits `[k,k²,k³]` across rows, i.e. it measures the *row-resolved*
datum and a genuine `∂_k`; (ii) has **no `ε`** — the soft profile is a fixed
position-space Gaussian (`sigma=3`, carrier `k_center=0.25`), not
`f_ε(k)=ε^{-1/2}f(k/ε)` sampled on ring momenta, so it cannot certify D29-B's
`ε→0`-last discipline or the admissibility clause `Nε(c_2−c_1)>2π`; (iii)
computes `ratio = ft*conj(free_t)` — the *numerator* of `ℛ(k)`, not the
ratio; the phases agree only because the denominator `Σ_c|free_t|²` is real
positive (that part of the shard's claim is fine).  The shard's own retreat 7
concedes (i); the CHECKER SPEC sentence and `⟨1⟩1.⟨2⟩2.⟨3⟩2` do not.
FIX: claim the *row-resolved* correspondence only, and add an `ε`-scaled
profile to SIB-C2 if the aggregate datum is to be certified at all.

**m5. P3 is mis-cited as certifying the D29-B datum.**  `run_p3` (lines
422–472) builds both objects from the **ML4 orthogonal trace**
`(e^{ik}−1)⟨out|(1−P)J^-_k|h⟩`, not from the (B3) readout; and the raw entry
is divided by `√(N−2)k²` while the smeared entry is divided by nothing, so
"growth 20.5 vs bounded 1.39" is not a like-for-like comparison — the smeared
number is a fixed-`k`-scale quantity that is expected to converge trivially.
The shard's `⟨1⟩3.⟨2⟩3(ii)` ("the D29-B smeared datum at the same `N` stays
bounded") therefore has no support in the probe as written.  This is a defect
of the frozen probe against its own pre-registration (P3 of
`briefs/soft-index-target.md` says "the D29-smeared datum"), inherited by the
shard.  FIX: state that P3 certifies the disease's *visibility* only, and put
the smeared-datum half on SIB-C2/the checker lane.

**m6. P2(b)'s η-insensitivity certificate is a no-op in code.**
`soft_index_probe.py:386–389` computes `proto = qk @ hard_vec` and
`proto_dressed = qk @ hard_vec` — the *identical expression* — so
`protocol_eta_diff = 0.0` by construction (confirmed in the frozen results
JSON: exactly `0.0`, not `≤1e-10`).  The mathematical claim (that `ηD` acting
on a one-magnon state lands in `ℋ_{3,N}`) is asserted in a comment, never
computed.  The shard leans on this twice (`⟨1⟩1.⟨2⟩1.⟨3⟩3`, `⟨1⟩8.5`) as
"the quantitative dodge certificate".  FIX: cite the *structural* argument
(which is correct and is the shard's own `⟨3⟩3`), and flag the probe row to
the orchestrator's checker lane.

**m7. D29-B never defines its momentum kernel.**  "`Φ̂_N(T)(k,h)`, the
coefficient of the symmetrized momentum pair `(k,h)`" — expansion coefficient
in a non-orthogonal frame, or inner product with the pair mode?  The pair
modes overlap at `O(1/N)` and the shard's own `⟨1⟩1.⟨2⟩2.⟨3⟩1` invokes an
"`O(1/N)`-overlap correction" without summing over the `Θ(N²ε)` mode pairs
involved, and `⟨1⟩4.⟨2⟩2.⟨3⟩3` gives a descendant-admixture bound
`O_ε(1/N_j)` whose constant is `∼1/dist({0},Λ∪K_h)∼1/(c_1ε)` — i.e. really
`O(1/(N_jε))`, `ε`-dependent, not displayed as such.  F2's truth value depends
on this convention.  FIX: pin the convention in the D29 merge text (the
probe's `fft2`-of-grid is the only concrete one), and state the two overlap
estimates with their `ε`-dependence.

**m8. (B9)/(H-band) at `S≥1` rest on a checker that does not exist.**
`SIB-C1` is "proposed"; `⟨1⟩3.⟨3⟩2` says `C_𝔇(S)` is "certified numerically
per SIB-C1".  I verified the *support* claim independently at `S=1/2,1,3/2`
(components at separation `>1` are `≤3e-15`) and the exact `S=1/2` norm; the
`N`-uniformity of `C_𝔇(S)` at `S≥1` remains uncertified.  Since `(H-band)`
is the sole input to `⟨1⟩5`'s Adler zero, a claim row citing it should say
"asserted, checker not yet written" (L1: "runs without errors" is never a
test; here not even that).

**m9. L4 collisions not flagged in §M4.**  (i) `ρ` is already file-local in
`theory/spin-s-twomagnon.md` ⟨1⟩1–⟨1⟩2 as the *double-occupancy coefficient*
(`notation.md` line 201/270) — and that is the very file this shard cites for
(T.1)–(T.3); (ii) `𝒜` is used inside this shard both for the D29-B datum and
for ML4's orthogonal trace `𝒜_{⊥,N}` (`⟨1⟩3.⟨2⟩3(i)`); (iii) the `M` row is
flagged against D1(e) bond insertions but not against the shard's own
`M_1^O,M_2^O` amplitudes.  FIX: three disambiguation rows.

**m10. L2.**  1234 lines against the 200–500 guidance; self-flagged with
split points — accepted as post-promotion hygiene, recorded so it is not lost.

**m11. Drafting hygiene / L6b.**  Two unresolved in-line self-corrections
survive in the shard ("— wait:" at `⟨1⟩4.⟨2⟩1.⟨3⟩1` and at `⟨1⟩5.⟨2⟩1`).
In both cases the "repair" is narrated rather than applied to the statement
being proved, and in both cases the repair is defective (M3, M5).  L6b
requires each leaf to stand as a justified step; a leaf that argues with
itself is not one.

---

## NOTE

**n1. Steps I re-derived and CONFIRM (do not churn these in the repair).**
`[S^+_{tot},J^-_0]=2J^z_0`; `‖Q_0ψ‖²=2M‖ψ‖²` on `ker S^+` (`n=1,2,3`);
`⟨h|J^z_0|h⟩=iv(h)` exactly, with `J^z_0` diagonal on `|h⟩_N`, at
`S=1/2,1,3/2` — and the trig-interpolation argument of `⟨1⟩2.⟨2⟩3.⟨3⟩2` is
structurally sound (both sides are `N`-independent-degree trigonometric
polynomials in `k`, agreeing at `N` ring points; the removable value at `k=0`
gives `−ω'(h)/i=iv(h)`); Ward residue `2iv(h)`, `ρ`-independent; the **exact
Duhamel identity (B8)**, which I reproduced to `1.5e-14` with an exact
spectral evaluation of the `s`-integral and killed with a mutation
(`1.9e0`); `‖𝔇‖=J|z_k−1||z_h−1|` at `S=1/2`; contact support `{|x−y|≤1}` at
`S=1/2,1,3/2`; the D7/D8 channel-labelling discussion of `⟨1⟩4.⟨2⟩3` (checked
against D7's frozen text and against the probe geometry `x_hard=x_soft−gap`
with `v_hard>v_soft` — correct, and the `sgn(v_h−v_s)` overload discipline of
`notation.md` overload 2 is respected).

**n2. B10 — the mandatory box attack, adjudicated.**  The box is *literally
true* and I confirm the arithmetic (`Λ_N(ε)=(2πℤ/N)∩(c_1ε,c_2ε)=∅` when
`c_2ε<2π/N`), and the limit-order discipline is genuinely respected: at fixed
`ε`, `N_j→∞` forces `kN_j→∞`, so the `kN=Θ(1)` regime where ML4-Q1 lives is
exited.  But the immunity is **definitional and is written into D29 itself**
(§M1: "no interpolation off the ring momenta (for `ε<2π/(c_2N)` the sample
set is EMPTY … outside the datum's domain by construction)").  Two
consequences the shard should state rather than leave to the critic: (i) the
admissible set *does* contain `kN=Θ(1)` indices — the minimal admissible `N`
gives `kN≈2πc_1/(c_2−c_1)` — so the immunity is a statement about limit
points only, not about the family's members; (ii) taken together with F2,
**both** of the shard's unconditional anchors live outside the running
family's domain: the exact Adler value (B6) is at `k=0`, which `Λ_N(ε)` never
samples, and the ML4-Q1 exclusion (B10) is by emptiness.  So the honest
reading is: *this is a real dodge of the counterexample, and simultaneously an
admission that the theorem says nothing about the physically realizable
fixed-`N` on-shell soft sequence.*  Not a refutation of the theorem; a
scoping sentence the shard owes the reader.  (It is **not** a "definitional
retreat that empties the theorem": the family is nonempty at every `ε`, as
`⟨1⟩1.⟨2⟩3` correctly proves.)

**n3. REFUTED-row audit — CLEAN.**  I found no reliance on ML5
(unrestricted universality), on the withdrawn `S2` label, or on
`M-INDEX-LA-strong`; no step contradicts the `O_η` counterexample D24(e)
(`⟨1⟩6.⟨2⟩2` reproduces `𝔠_h(ηD)=2iη(1−e^{-3ih})` correctly and the
corollary is silent there, as required); the `G0-soft-r1` fence is respected
in `⟨1⟩2.⟨2⟩4` and `⟨1⟩8.3` — with the single exception of M5, where a second
`(e^{ik_s}−1)` is invoked as an independent power of `k_s`, which is exactly
the fenced move.  `D26(INT)` is carried and unused, honestly flagged
(`⟨1⟩8.6`, retreat 5) — I checked: no step uses it.

**n4. HONEST STATUS audit — one retreat is a silent refutation (L10).**
Retreats 1,3,4,5,6,7,8,9 are honest and match the proof text.  Retreat 2 (the
`(TGT)`-strengthening) is honest about *what* was assumed but its stated
justification — "equicontinuity … pins no VALUE" — is used to license a
hypothesis that pins the *channel*, not merely the value (M2), and its
"negative-space finding" does not hold against the other lane's D30 (X1).
The item that is **missing** from HONEST STATUS is the `|q|` extrapolation
(M6): a law stated with `|q|` while only `|q|=1` is proved, in a corpus that
records `Bc`'s `|q|>1` factor as open, is an overclaim that belongs in the
retreat list.  Nothing else in HONEST STATUS conceals a refutation.

---

## CROSS-LANE — `theory/soft-index-b.md` (S1-B) vs `theory/soft-index.md` (S1-A)

Read after the attack above.  Each item names the lane it counts against.

**X1. "Equicontinuity cannot pin the jet" does NOT hit S1-A's D30 — MAJOR
against S1-B's negative claim.**  S1-B's retreat 2 and `⟨1⟩8.8(iv)` present
the target template's `(TGT)` as insufficient and imply the other lane must
either fall to it or be stronger.  S1-A's D30 is *not* "uniform boundedness +
equicontinuity": D30(2) requires every component cluster point to have "a
`C¹` limiting external flux **with D29(5)'s value at zero**", and D30(3)
requires `Γ_*(0)=U_*` plus two `C¹` trace bounds — i.e. ML4-A's energy-shell
*channel matching* (`ml4-ward-reduction.md` (7)).  Both are value/channel
reaching clauses.  So S1-A independently agrees with S1-B's negative finding
and routes around it by a *different* door (ML4-A matching on the limit
objects) instead of by naming finite-volume eigenvectors.  S1-B's claim that
its (TGT2) is "the weakest clause I found" is therefore untested against the
only competitor; and S1-A's clause is arguably weaker in the respect that
matters (it constrains the *limit* family, never the finite-`N` spectral
data).  Both remain unproved in every model.

**X2. Where the `2ρ` enters — MAJOR against S1-B; both lanes install the
density by convention.**  S1-A puts it **inside the flux factor** and makes
it *definitional*: D29(5) fixes `L_λ(0,h) = −i sgn(v_h−v_s)/(2ρ_λ v_h)`, and
(SIDX.10) then closes to `i sgn (ℓ_h/ρ)k`.  S1-B keeps D24(d)3's
`L(0,h)=−iχ/v_h` "transplanted verbatim" as (3′) **and** multiplies by a
separate `1/(2ρ)` (B14).  These are numerically identical and structurally
incompatible; S1-B's version additionally contradicts its own claim that (3′)
is D24(d)3 verbatim, because ML5-B's product with that `L` already closes at
`2` with no residual factor.  The deeper cross-lane finding, which the
orchestrator must not merge away: **neither lane derives the `ρ` in `|q|/ρ`** —
S1-A by definition, S1-B by an undefended factor whose stated justification
gives `(2ρN)^{-1/2}` (M4).  The `S`-dependence that is actually PROVED
(S2-2body-S) comes from the spin-`S` *contact algebra* (`μ=(2S−1)a+b` in
(T.2)), not from a leg norm; the abstract "derivation" of `1/ρ` in either lane
is at present a fit to that known answer.

**X3. The two (S-IDX.0) statements ARE the same identity — and both inherit
F1.**  S1-A (SIDX.3): `D_λ^†D_λ=2m_λI`, `P_λJ^-_0=Q_0J^z_0/m_λ` on a
highest-weight space with `S^z=m_λ`.  S1-B (B4): identical with `m_λ→M`.
Both are false at `n≥2` by my computation (F1), both citing ML4-Ward (9).
*Register difference (MINOR against S1-B):* S1-A carries `m_λ` as the **actual**
`S^z` eigenvalue with only the asymptotic `m_λ/N_λ→ρ`, which keeps `ρ` a
genuinely free real; S1-B asserts `M=ρN−n` exactly, which silently requires
`ρN∈spec S^z_{tot}` for every `N` in the subsequence and, under its own
fully-polarized H-SIDX.1, forces `ρ=S∈½ℤ` (m2).  S1-A's register is the
correct one for the "free `ρ`" advertisement.

**X4. `|q|` vs `ℓ_h` — MAJOR against S1-B.**  S1-A explicitly refuses the step:
H-SIDX(2) records a *measured* Ward datum `ℓ_λ(h)` with "`ℓ_h=|q|` for a
composite charge-`q` band is an additional checkable hypothesis, not a
conclusion here", and its HONEST STATUS 2 says "asserting more would
contradict open claim Bc".  S1-B states `|q|/ρ` in (B13), (B14) and both claim
rows with only `|q|=1` ever treated (M6).  On this point S1-A is right and
S1-B is wrong.

**X5. Two different D29 objects, hence two different theorems — MAJOR for the
merge; on the template's clause (ii), S1-A matches and S1-B does not.**
S1-A's soft insertion is a packet with a **carrier `k` and an independent
width `ς`** (`f_{k,ς}(p)=ς^{-1/2}f((p−k)/ς)`), with the ordered limit
`ς↓0` *before* `k→0` (SIDX.14), so `∂_k arg(1+𝗌_*)|_0` is a genuine pointwise
jet.  S1-B's soft insertion is a **scale-only** profile
`f_ε(k)=ε^{-1/2}f(k/ε)` sampled on ring momenta, with no width parameter, so
its conclusion is necessarily the profile-averaged
`arg(1+𝖲^*(ε))/\bar k_w(ε)` (M7).  The two `D29`s are not variants of one
definition; the orchestrator must choose, and the choice decides whether the
theorem states the target's (S-IDX.1)(ii) or a weaker averaged surrogate.
S1-B's version buys the ML4-Q1 immunity structurally (X6) at exactly this price.

**X6. Two different ML4-Q1 immunity mechanisms — compatible, not equivalent.**
S1-A: limit-order only (SIDX.15 — "`k` is fixed while `N→∞`"), which leaves
the fixed-`N` on-shell object *inside* the definitional universe and excludes
it only from the limit.  S1-B: domain-emptiness (B10 — `Λ_N(ε)=∅`), a
strictly stronger, definitional exclusion written into D29 itself.  S1-B's is
the more robust dodge; S1-A's is the more conservative definition.  Neither is
wrong; they cannot both be D29.  Note S1-A's `⟨1⟩5.⟨2⟩6` is the *only* line in
either lane that displays the two limits side by side, which is the form the
target brief asked for.

**X7. Exhaustiveness of the LSZ split — a definitional dodge in S1-A, an
honest hypothesis in S1-B (this one counts against S1-A).**  S1-A's D29(4)
says "the pairing is, **by definition of PROTO**, the exact sum of its
descendant and `R_λ(k)` components"; S1-B carries the same content as the
named hypothesis (1′) = D24(d)1.  Assuming exhaustiveness by definition is
the move ML5-B was careful to make an explicit hypothesis; the S1-A critic
should be pointed at it.

**X8. Adler-zero mechanism — MINOR against S1-B.**  S1-A derives the zero
from two displayed `O(k)` factors (SIDX.13): `ω(k)/(e^{ik}−1)` on the charge
term and `Γ_*^†(1−P)J` accompanied by `(e^{ik}−1)` on the orthogonal term.
S1-B's `⟨1⟩4` derives it from the (T.3) expansion via (TGT2) — i.e. inherits
it — while §0 attributes it to "O6/OR2 + (R16)-uniformity", which matches
neither its own proof nor S1-A's mechanism.

**X9. Vacuous-truth fences — both honest; S1-A's is sharper.**  S1-A ⟨1⟩6
states flatly that "if another model has no D30-admissible limit point,
(S-IDX.1) has no instance there" and that "D30 is a closure property, not an
existence hypothesis".  S1-B proves finite-index *definedness* and scopes
limit-point existence to Lane S2 — correct, but `⟨1⟩8.1`'s "Answered twice"
oversells it, since definedness of the family is not an instance of (TGT2)
(M2).  Both lanes agree that D26(INT) is unused and that `O_η`/ML5 survive.

---

## Summary of severities

* **FATAL (2):** F1 (general-sector Ward projection false for `n≥2`; verified
  numerically, mechanism identified, repair given), F2 (`ℛ(0)=1` "at every
  finite index" false at `S≥1`, tautological at `S=1/2`; verified numerically
  including with a random input state).
* **MAJOR (7):** M1 (S-IDX.0 unused by S-IDX.1a), M2 ((TGT2) assumes the
  channel identification; no proved instance), M3 (SIB-L1 false as stated —
  descendant is `Θ(ε)`-close; (TGT2) admits descendant eigenvectors),
  M4 (`1/(2ρ)` unjustified and unfalsifiable at `ρ=1/2`), M5 (clause-5
  discharge double-counts a kinematic factor), M6 (`|q|` overclaim against an
  open Bc row), M7 (pointwise-jet vs averaged-ratio lockstep break).
* **MINOR (11):** m1–m11 above.
* **NOTE (4):** n1–n4 above.

## FAIL(F1, F2, M1, M2, M3, M4, M5, M6, M7)
