# Critic verdict ml2-r1 — `theory/ml2-completeness.md` (+ `theory/checks/ml2_completeness_check.py`)

Critic: Opus (L6 adversarial loop, round 1). Date 2026-08-25.
Artifact status at review time: "PROVER COMPLETE; L6 critic pending".

**SUMMARY: FAIL(M1, M2, M3)**

No fatal objection. I re-derived every analytic step of ⟨1⟩2--⟨1⟩5 independently
and could not break any of them; the finite-ring classification and the
infinite-volume Plancherel statement are, as far as I can tell, correct, and
correct at every `N` and every parity, including the near-threshold cases where
a naive string count fails. The three MAJOR objections are (M1) the shard does
not actually deliver its own advertised downstream consequence, and (M2, M3)
the numerical certificate quoted in ⟨1⟩6 is partly vacuous and structurally
blind to exactly the parity classes the shard exists to settle. All three are
cheaply repairable and I supply the repairs.

---

## 0. What I did

Everything below is my own computation; none of it reuses
`ml2_completeness_check.py` or the doc's formulas except where I am explicitly
testing them.

- **C1** (`scratchpad/indep2.py`, `indep3.py`). Brute-force two-magnon ED from
  **D6** directly (`H=(J/2)Σ_x(1−P_{x,x+1})` assembled in the coordinate basis,
  `J=0.8137`, deliberately not the checker's `J`). Momentum fibers obtained by
  **projecting with the translation operator**, not by writing down (4).
  Descendants identified by an independent SU(2) criterion (the span of
  `S^-_tot` applied to the one-magnon sector), computed **eigenspace-wise** so
  that the degenerate `K=π` level is handled by a trace of a projector rather
  than by an arbitrary `eigh` basis. Strings identified by `X=(2−E/J)/(2c)>1`.
  Run for **every `N` from 4 to 28**.
- **C2** (`scratchpad/inf.py`). Numerical and analytic checks of (20), of the
  ⟨1⟩5.⟨2⟩3.⟨3⟩3 Abel-summation claims, and of onto-ness (`VV*=1`).
- **C3** (`scratchpad/mut/`). Eight mutants of a **copy** of the checker,
  plus forced `SIZES` variants.
- **C4** Overlaps of `Q_{k_s}|k_h⟩_N` with the two exceptional vectors.

---

## M1 — MAJOR. ⟨1⟩6.⟨2⟩2 and ⟨1⟩1 PROVE-3: (R5) has no value at the singular contact state, so the advertised consequence is not delivered

⟨1⟩6.⟨2⟩2 asserts:

> "Equations (R5)--(R7) of `soft-current-recon.md` now use a proved complete
> family, with strings, descendants, and (for even `N`) the singular contact
> state included."

(R5) in `soft-current-recon.md` ⟨2⟩2 is a formula in `(k_1,k_2,A_{12},A_{21},
\mathcal N_B)`; it evaluates `F_N(k_s−k_1^*,k_h−k_2^*)` and three siblings.
It therefore requires a **finite** pair `(k_1,k_2)` and finite coefficients.
The shard's own ⟨1⟩4.⟨2⟩2.⟨3⟩1 concedes that for `|χ_π⟩` there is none:

> "This is the singular completion labelled by the compactified rapidity pair
> `{+i/2,−i/2}`, equivalently `z_1=∞, z_2=0`. The unscaled D7 two-plane-wave
> formula is undefined there…"

So (R5) cannot produce `c_B` for `B=χ_π`. Saying that (R5) "now … [has] the
singular contact state included" is false: the singular state is included in the
*basis*, and excluded from the *coefficient formula*. ⟨1⟩1 PROVE-3's
"unconditional Parseval expansion" is true as a statement about completeness,
but the pair (R5)+(R6) is what the soft shard actually uses, and it still has a
hole precisely at the exceptional vector ML2 was written to supply.

**This is material, not pedantic.** (C4) At `N=12`, with `k_s+k_h≡π`:

| `k_h` | `2π/12` | `4π/12` | `8π/12` | `18π/12` |
|---|---|---|---|---|
| `\|⟨χ_π\|Q_{k_s}\|k_h⟩\|` | 1.0000 | 1.7321 | 1.7321 | 2.0000 |

against `‖Q_{k_s}|k_h⟩‖=\sqrt{N−2}=3.1623`. The singular state carries up to
63% of the norm of the charge-created state. Dropping it, or leaving its
coefficient undefined, wrecks (R6) whenever `k_s+k_h≡π`.

**Fix (verified, `scratchpad`, max error 2.7e-15 over `N=8,12,16,18`).** Add a
step to ⟨1⟩6 giving the coefficient directly from (12) and (R3), which is a
two-line computation:

> For `N` even and `k_s+k_h≡π (mod 2π)`,
> `⟨χ_π|Q_{k_s}|k_h⟩_N = 2i\cos((k_h−k_s)/2)`;
> for `k_s+k_h≢π` the overlap vanishes by translation fibering.

(Proof sketch: with `k_s+k_h=π` every adjacent-pair coefficient in (R3) equals
`(−1)^x·2\cos((k_h−k_s)/2)e^{iπ/2}`, and for `N` even the wrap-around pair
`{N−1,0}` contributes the same value again, so the `N` terms add coherently.)

**Half of the objection is withdrawn**, and I record why, because the doc could
have made the same mistake and did not: the `K=0` double descendant
`(S^-_tot)^2|Ω⟩` *is* representable in D7 form. At `k_1=k_2=0` the contact
equation `oracle-bethe.md` (7) degenerates to `0=0` (the doc says so at
⟨1⟩4.⟨2⟩1.⟨3⟩2), so `A_{12}=A_{21}=1/2` is admissible and (R5) applies.
Its coefficient is `−\sqrt{2/(N−1)}` for `k_s=−k_h≠0` (verified to 1.2e-15).
Stating that choice explicitly would still help, since `S_{12}=A_{12}/A_{21}`
is `0/0` in the limit and the reader has no way to know which representative
is meant.

---

## M2 — MAJOR. ⟨1⟩6.⟨2⟩1: the "coincident zero" certificate is a tautology and the (22) column is a hard-coded literal

⟨1⟩6.⟨2⟩1 justifies (22) with

> "the checker constructs (4), (12)--(13), independently constructs the full D6
> coordinate Hamiltonian, and exits explicitly on every failure"

and (22) carries a final column headed "coincident zero" with entries `12, 16,
20`. Neither the column nor the underlying claim is certified.

**(a) The vanishing-wave test is identically zero.** `ml2_completeness_check.py`
lines 245--252:

```python
abs(
    -np.exp(1j * momentum * (x + y))
    + np.exp(1j * momentum * (x + y))
)
```

This is `|−A+A|`, which is `0.0` for every `momentum`, every basis element, and
every value of anything else in the program. It is not a test of "their
coordinate wave is identically zero" (⟨1⟩4.⟨2⟩1.⟨3⟩1); it is an arithmetic
identity typeset to look like one. (C3) **Demonstrated:** I changed the
amplitude from `1` to `7` in a scratchpad copy (`mut/taut.py`) — a change that
would falsify any genuine reading of the expression — and the checker still
prints `PASS`, exit 0. The only non-vacuous part of that block is
`abs(np.exp(1j*n*momentum)+1.0)`, which merely confirms that
`k=(2n+1)π/N` solves `e^{iNk}=−1`; mutating *that* (mutant `mut/coincident.py`)
does go red (exit 1, `coincident zero-vector check failed N=12: 2.0`).

**(b) The (22) column is a literal.** Line 261:
`f"pi-deg={counts['pi_degenerate']:2d} coincident-zero={n_sites:2d}"`.
The printed number is `n_sites`, not a count of anything the program computed.

The underlying mathematics is fine — I checked it: `k_1=k_2=k`, `e^{ik}≠1` gives
`S_{12}=−1` from `oracle-bethe.md` (6), hence `A_{12}=−A_{21}` and
`ψ(x,y)=A_{12}[e^{ik(x+y)}−e^{ik(x+y)}]≡0`, with exactly `N` roots of
`e^{iNk}=−1`. So M2 is a defect of the *certificate* and of ⟨1⟩6.⟨2⟩1's claim
about the certificate, not of ⟨1⟩4.

**Fix.** Either build the actual coordinate vector from D7 at `k_1=k_2=k` and
assert its norm is zero, or delete the block and the (22) column and let
⟨1⟩4.⟨2⟩1 stand on its (correct) algebra alone. Under **L1** ("'runs without
errors' is never a test") the present form should not survive.

---

## M3 — MAJOR. ⟨1⟩6.⟨2⟩1: the certificate is blind to the parity classes the shard exists to settle

`SIZES = (12, 16, 20)` (line 18). All three are `≡0 (mod 4)`. Consequences:

**(a) Two branches are dead code.** With `L=N/2 ∈ {6,8,10}` always even and `N`
always even:
- line 59, `block[-1,-1] -= ((-1)**label)*coupling` — the odd-`N` reflection
  endpoint `2−σ_m c_m` of (4) / ⟨1⟩2.⟨2⟩3 — is never executed;
- line 226, `expected_pi_degenerate = length−2 if length%2==0 else length−3` —
  the `L−3` count of ⟨1⟩4.⟨2⟩3 — never takes its `else` branch;
- lines 121--122, the `label%2` odd branch of `pi_fiber_vectors`, i.e. the
  second line of (13) `q=jπ/(L−1), 1≤j≤L−2`, is never executed.

(C3) **Demonstrated by surviving mutants** (scratchpad copies, both exit 0,
both still print `PASS`):
- `mut/signflip.py`: `block[-1,-1] -= …` → `+=` (corrupts the odd-`N` endpoint);
- `mut/pideg.py`: `expected_pi_degenerate = length−2` (deletes the `L−3` branch).

**(b) The checker cannot be run at odd `N` at all.** Line 212 hard-asserts
`counts["singular"] != 1 → fail`, which contradicts (14) row 3
("`1 (N even), 0 (N odd)`"). (C3) Forcing `SIZES=(11,13)` gives
`FAIL: exceptional inventory mismatch N=11: {'descendant': 11, 'bound': 8,
'real': 36, 'singular': 0, 'pi_degenerate': 0}` — i.e. the checker rejects a
correct inventory.

Since the shard's stated purpose is exceptional-root bookkeeping — and
`soft-current-recon.md` ⟨1⟩6 itself says "The main nuisance is
exceptional/singular root bookkeeping" — a certificate that skips every `N≡2
(mod 4)` and every odd `N` does not discharge it.

**Fix.** `SIZES = (11, 12, 13, 14, 16, 18, 20)` plus replacing line 212's
`counts["singular"] != 1` by `counts["singular"] != (1 if n_sites % 2 == 0
else 0)`. **I ran the even half of this myself and it passes:** with
`SIZES=(6,10,14,18,22,26)` and *no other change*, the unmodified checker prints
`PASS` and reproduces exactly the counts my independent ED gives (below). So
this is a coverage gap, not a hidden bug — but it must be closed before (22)
can be cited.

---

## Confirmations (NOTE) — what I could not break

**N1. The finite inventory (14)/(22) is correct at every `N` I can reach.**
(C1) Independent ED, `N=4…28`, both parities, all residues mod 4. Every `N`
matched the doc's formula exactly, including all six sizes with `L` odd where
the untested `L−3` branch applies:

```
N   dim  desc string real  sing  pi-deg      N   dim  desc string real  sing  pi-deg
4     6    4     0     1     1     0        17   136   17    14   105    0     0
5    10    5     2     3     0     0        18   153   18    14   114    1     6
6    15    6     2     6     1     0        19   171   19    16   136    0     0
8    28    8     4    13     1     2        20   190   20    16   145    1     8
10    45   10     6    26     1     2        21   210   21    18   171    0     0
12    66   12     8    41     1     4        22   231   22    16   184    1     8
14    91   14    10    62     1     4        24   276   24    18   223    1    10
16   120   16    12    85     1     6        26   325   26    20   268    1    10
                                            28   378   28    22   315    1    12
```

The `N=12,16,20` rows reproduce (22) exactly. The fiber dimensions (2) matched
for every `(N,m)`. **No overlap or double count between the "singular" and
"π-degenerate" classes at any `N`, and no `N mod 4` dependence** (the specific
failure mode I was asked to hunt): they are eigenvectors of *different*
eigenvalues (`J` and `2J`) of the *same* `c=0` block, so they are orthogonal
automatically, and the descendant sits at `q=π/2`, i.e. `j=(L−2)/2` for `L`
even and `j=(L−1)/2` for `L` odd — an integer in range for every `L≥3`, so it
is subtracted exactly once and is never missing. At `L=2` (`N=4`) and `L=3`
(`N=6`) the family (13) collapses to the descendant alone and `L−2=L−3=0`
correctly; the formulas degrade gracefully at the boundary.

**N2. The string count (10) survives the near-threshold test, which is where a
sloppier claim would have died.** `N(1−c_m)>2` for odd `m` is genuinely tight:
at `N=20, |m|=3` it is `2.17986>2` (string present), at `N=22, |m|=3` it is
`1.98810<2` (string absent). Hence `B_20=B_22=16` even though `dim` grows from
190 to 231. My ED confirms both. The algebraic-integer argument of
⟨1⟩3.⟨2⟩5.⟨3⟩3 excluding equality (`2c_m=2−4/N` is a rational algebraic
integer ⇒ `N|4`; `N=4` checked by hand) is correct and is doing real work.
*(I initially recorded a mismatch at `N=22`; it was a floating-point bug in my
own `|K_m|<π` test — `2π·11/22` rounds to `> math.pi`. The repo checker's
integer test `0 < abs(label) < n_sites/2` is exact and does not have it.
Objection withdrawn.)*

**N3. Simplicity, `X≥−1`, one string per fiber.** (C1) No fiber with `c>0` had
a repeated eigenvalue at any `N≤28`, so ⟨1⟩3.⟨2⟩2's simplicity claim holds; no
root with `X<−1` appeared. I also re-derived the two quadratic-form estimates
of ⟨1⟩3.⟨2⟩4.⟨3⟩1--⟨3⟩2 by hand (including the exceptional `−\sqrt2 c` edge
and the `2−σ_m c` endpoint) and the rank-one min--max step
(`λ_2(h)≥λ_1(h')≥2−2c`): both are correct as stated.

**N4. `F_r(1)=1−r(1−c)` and `F_r(−1)=(−1)^{r−1}(rc+r−1)` are correct**, and I
re-derived all four rows of (11) and the four values `P_m(−1)` — none vanishes
for `c>0, N>3`, so `X=−1` is never a root, as ⟨1⟩4.⟨2⟩1.⟨3⟩2 claims. I also
verified the coincident solutions land at `X=cos(πj)=±1` (since `2k=K_m+2πj`
forces `q=πj`), which is what makes that argument complete.

**N5. Orthogonality is *proved*, not merely observed** — with one exception,
which the doc under-justifies (see m7). Distinct fibers are distinct translation
eigenspaces; within a fiber with `c>0` the Jacobi matrix is Hermitian with
simple spectrum. Only the `K=π` fiber has a degenerate level (`E=2J`,
multiplicity `d_m−1`), and there orthogonality is a genuine computation.
I verified it: for `L` even, with `q_j=(j+½)π/M`, `M=L−1`, and the last
coordinate carrying weight `½`, `Σ_{s=0}^{M−1}\sin(sq_j)\sin(sq_{j'})
+ ½(−1)^{j+j'}` is `M/2·δ_{jj'}` — the `½(−1)^{j+j'}` from the `√2`-weighted
last coordinate is exactly what cancels the `∓½` left over by
`Σ_{s=0}^{M−1}\cos(sπd/M) ∈ \{M,0,1\}`. For `L` odd it is the standard DST-I
sum. Both work.

**N6. Eq. (20) is exactly right, including at the endpoints.** (C2) Verified to
`2.9e-15` for `c∈{0,0.11,0.37,0.6,0.85,0.999,1}` and `r,s≤6`. I reproduced the
contour argument independently: `S=(cz−1)/(z(z−c))`, so
`(2π)^{-1}\int_{-π}^{π} S e^{iqn}dq` is the residue at `z=c` of
`(cz−1)z^{n−2}/(z−c)`, i.e. `−(1−c^2)c^{r+s−2}`, and `n=r+s≥2` keeps `z=0`
regular. The doc's appeal to continuity at `c=0,1` is stronger than it needs to
be: both endpoints are *exact* (at `c=1` the pole sits on the contour but the
`n≥2` numerator kills the coefficient anyway).

**N7. The Plancherel statement (21) is correct with the stated normalizations.**
I checked the bookkeeping by hand: `U` in (15) is unitary with `\int dK`
(not `dK/2π`); `⟨Ψ^{sc}_{Kq},ψ⟩=(2π)^{-1/2}Σ_r\overline{w_q(r)}(Uψ)(K,r)`;
combining with (20) gives exactly (21) with measures `dK\,dq` and `dK`. The
delta-normalizations `⟨Ψ^{sc}_{Kq},Ψ^{sc}_{K'q'}⟩=δ(K−K')δ(q−q')` and
`⟨Ψ^b_K,Ψ^b_{K'}⟩=δ(K−K')` both come out right. The three Jacobians in
⟨1⟩5.⟨2⟩4.⟨3⟩3 all check (`dk_1dk_2=dK\,dq`; `dE=2Jc\sin q\,dq`;
`dE_b/dK=J\sin(K/2)\cos(K/2)=\sqrt{E_b(J−E_b)}`), as do the rescaled measures
`dKdq/(2π)^2` and `dK/(2π)`. Restricting `q` to `(0,π)` is right and does not
double count: `w_{−q}=\overline{S(q)}\,w_q`.

**N8. `E_b(K)=J\sin^2(K/2)` in (19) is right and its factor-2 tension with
⟨1⟩3.⟨2⟩6 is real physics, not a typo.** `E_b(K)=ω(K)/2`, whereas the
descendant energy is `2J(1−c^2)=ω(K)`. I checked both against ED. At `K=π`,
(19) gives `E_b=J`, matching the finite-ring singular state's energy `J` — a
nice consistency the doc does not point out but should (see n5).

**N9. Checker robustness and non-circularity.** Runs identically under `python3`
and `python3 -O` (no bare `assert`s; `fail()` raises `SystemExit(1)`), and
reproduces (22) and all three quoted error magnitudes to the digit
(`8.882e-15`, `2.313e-14`, `2.126e-14`). It is **not circular**:
`ring_hamiltonian` is assembled from D6 swaps in the coordinate basis with no
reference to (4), and the residual/orthogonality/projector/spectrum comparisons
are genuine cross-checks of the ⟨1⟩2 reduction; class counts come from
thresholded eigenvalues rather than from re-evaluating (10)/(11).
Red-capability confirmed for every branch it does exercise — four mutants all
exit 1: even-`m` `−\sqrt2 c` endpoint → `−c` (`FAIL: missing descendant`);
`√2` embedding weight dropped (`FAIL: bad fiber embedding norm`); descendant
energy shifted by `1e−6` (`FAIL: missing descendant`); coincident momenta
`(2n+1)π/N → 2nπ/N` (`FAIL: coincident zero-vector check`). M2 and M3 are the
only certificate defects I found.

---

## MINOR

**m1. ⟨1⟩1 PROVE-2 cites the wrong equation range.** It promises
"eigenfunctions, energies, Plancherel measures, and resolution of the identity
are (15)--(20)". The resolution of the identity is **(21)**, and the measures
are in ⟨1⟩5.⟨2⟩4.⟨3⟩3. Should read (15)--(21).

**m2. ⟨1⟩1 PROVE-1 cross-references the wrong step.** "every nonzero two-magnon
Bethe vector is one of the real-pair, complex-pair, or descendant vectors
classified in ⟨1⟩3" — but ⟨1⟩3.⟨2⟩1 assumes `c=c_m>0` throughout, so the `K=π`
degenerate real pairs (13) are classified in ⟨1⟩4.⟨2⟩2, not in ⟨1⟩3. Should
read ⟨1⟩3--⟨1⟩4.

**m3. ⟨1⟩3.⟨2⟩3.⟨3⟩3's converse is false at one root.** "conversely that
condition reconstructs both Bethe equations" — at `m=0`, `X=1` *is* a root of
`P_0` (by (11), since `c=1`), and reconstructing gives `q=0`, i.e.
`k_1=k_2=0`, a **coincident** pair, which the statement of ⟨2⟩3 excludes by
hypothesis. The bijection is: roots of `P_m` ↔ eigenlines (⟨2⟩2, unconditional);
and noncoincident Bethe solutions ↔ roots *minus the single root `X=1` at
`m=0`*, which is re-added as the double descendant in ⟨2⟩6.⟨3⟩2. The shard
handles this correctly in substance but the two-way claim in ⟨3⟩3 is stated
without its exception. One clause.

**m4. ⟨1⟩5.⟨2⟩3: "The bound vector is present for almost every `K≠0`."** It is
present for **every** `K≠0`: `c=\cos(K/2)<1` strictly on `(−π,π]\{0\}`, so
`c^{r-1}∈ℓ^2` always. "almost every" is a gratuitous weakening that will look
like an admitted gap if it reaches the paper.

**m5. ⟨1⟩5.⟨2⟩4.⟨3⟩2: absence of singular continuous spectrum is asserted, not
derived.** The step reads "Hence the scattering spectrum is absolutely
continuous … Justification: (18)--(21) and unitarity of the spectral transform."
Unitary equivalence to multiplication by `E(K,q)` on `L^2(dK\,dq)` does **not**
by itself give an a.c. spectrum: the spectral measure of `ψ` is the pushforward
of `|\hatψ|^2dK\,dq` under `E`, and absolute continuity of a pushforward needs
`∇E≠0` off a null set. That hypothesis holds here — `∇E=0` only on
`\{\sin(K/2)=0\}∪\{\sin q=0\}`, and `dE_b/dK=J\sin(K/2)\cos(K/2)` vanishes only
at `K∈\{0,π\}` — and the required Jacobians are *already written down* in the
very next step ⟨3⟩3. But ⟨3⟩2 does not invoke them, so as written the
"no singular continuous spectrum" claim (part of what the theorem is being
cited for) is a leaf with no justification. One extra leaf fixes it; please add
it, because this is exactly the kind of sentence a referee will stop on.

**m6. ⟨1⟩5.⟨2⟩3.⟨3⟩3 hides a cancellation.** The step states
`Σ_r \overline{w_q(r)}w_{q'}(r)=2πδ(q−q')` as a bare equality. The Abel limit of
that sum carries, a priori, a regular remainder
`−½(1+\bar S)(1+S') + (i/2)[\cot((q'−q)/2)(\bar S S'−1) + \cot((q+q')/2)(S'−\bar S)]`.
(C2) I evaluated it: it **vanishes identically** for every `(c,q,q')` I tested,
so the doc's claim is *true* — and I confirmed onto-ness (`VV^*=1`) directly
against a smooth test function to `~1e-9`. But the step gives no hint that a
cancellation is needed, so it currently reads as a formal manipulation of a
divergent series. Write the remainder down and note that it is zero.

**m7. ⟨1⟩4.⟨2⟩2.⟨3⟩2 hand-waves the one orthogonality that is not automatic.**
"use finite sine/cosine orthogonality" is the only justification offered for the
`K=π` family (13), and that is the single place in the shard where the spectral
theorem does *not* give orthogonality for free (the level `E=2J` is
`(d_m−1)`-fold degenerate). It happens to be true (N5), but the `L`-even case
needs the `√2`-weighted last coordinate to cancel a `∓½`, which is not
something a reader will supply unprompted. Promote it to a ⟨3⟩ sub-proof.

**m8. L6b structure defects.** (a) There is no top-level `⟨1⟩7. QED` closing
THEOREM ML2; ⟨1⟩6.⟨2⟩3 is doing that job one level down. (b) ⟨1⟩5.⟨2⟩2,
⟨1⟩6.⟨2⟩1 and ⟨1⟩6.⟨2⟩2 are `PROVE` steps with a bare `Justification:` line —
no ⟨3⟩ sub-proof and no terminal QED, contrary to L6b's "sub-proofs ⟨2⟩1…,
… terminal QED steps". (c) ⟨1⟩6.⟨2⟩1 labels a script run as `PROVE`. A named
computation is an admissible L6b leaf, but placing it as a `PROVE` step inside
the theorem's own tree invites reading the inventory (14)/(22) as established
by numerics; it is in fact established by ⟨1⟩3--⟨1⟩4, and (22) is corroboration.
Relabel as a certificate/remark outside the proof tree.

**m9. L4 collisions with `notation.md`.** ⟨1⟩3.⟨2⟩1 excuses the new symbols as
"definitions local to this proof", but L4 says every symbol lives exactly once.
Three are already taken: `U` is `U[f]`, the modulated symmetry operation
(`notation.md` line 51, D3), reused in (15) for the center Fourier transform;
`S(k;·)` is the soft factor of Conjecture S (`notation.md` line 17), reused in
(18) as `S(K,q)` for the two-magnon S-matrix — which **D7 already names
`S_{12}`**, so this is also a second name for a frozen object; and `X` is the
MPS tangent-space gauge matrix (`notation.md` line 16), reused for `\cos q`.
Rename or register.

**m10. D7 tie-in for `t` and `η` is missing.** D7 (frozen) defines `t` as the
bound state's geometric decay factor and `η:=−\log|t|`. (19) has `t=c` but never
says so. Worse, ⟨1⟩3.⟨2⟩4.⟨3⟩3 writes `q=iη` for the **finite-ring** string,
where `f_r=Se^{−ηr}+e^{+ηr}` has *both* branches, so `|t|=e^{−η}` is only
asymptotically true there. State `t=c`, `X=\cosh η=(c+c^{-1})/2`, and that the
finite-ring identification is the `N→∞` limit.

---

## NOTE

**n1. ⟨1⟩1 PROVE-2 should not be read as ML1.** Calling (17) "the D7 scattering
representation" is a generalized-eigenfunction / Plancherel statement. ML2 does
**not** construct the Møller wave operators `Ω^±` and does not prove asymptotic
completeness in the scattering-theoretic sense — that is ML1 in
`soft-current-recon.md` ⟨1⟩6, still open. Please reword so the Letter cannot
overclaim. Relatedly: the shard never mentions domains, which is fine — `H` is
bounded on this sector — but saying so once (`‖H‖≤4J`, no domain question, the
two-magnon subspace is `H`-invariant because `H` conserves `S^z_{tot}`) would
close the question a referee will ask.

**n2. (14) and (22) use different meanings of "real".** (14)'s "other real-pair
states" absorbs the `K=π` degenerate waves; (22)'s "real" column excludes them.
At `N=12`: `66 = 45+8+12+1` under (14) and `66 = 41+8+12+1+4` under (22). The
doc *does* flag this in ⟨1⟩6.⟨2⟩1's preamble — keep the flag attached if either
table migrates to the paper, because the tables otherwise look contradictory.

**n3. ⟨1⟩5.⟨2⟩1's center gauge is anti-periodic in `K`.** The phase
`e^{−iK(x+r/2)}` is anti-periodic in `K` for odd `r`, so "`−π<K≤π`" is a fixed
fundamental domain, not a circle. Harmless as used, but it matters for anything
that differentiates in `K` or takes `K→±π` — including ⟨2⟩4.⟨3⟩3's bound-band
Jacobian at the band top. One parenthesis.

**n4. Suggested regression addition.** The `N=20` vs `N=22` string threshold
(N2) is the sharpest single test of (10) available at reachable sizes and costs
nothing. Adding `N=22` to `SIZES` alongside the M3 fix would pin it.

**n5. Worth stating explicitly:** on the infinite chain the singular contact
state is simply the `K=π` member of the bound band ((19) at `c=0` gives
`f_r=δ_{r1}`, `E_b=J`). That is a genuinely satisfying consistency between
⟨1⟩4 and ⟨1⟩5 and it is currently left for the reader to notice.

---

## Verdict

The mathematics of ⟨1⟩2--⟨1⟩5 is sound and I recommend it be kept essentially
as is; I tried hard to break the finite-ring counting and could not. But **L6**
requires a critic pass with no fatal *or major* objections, and there are three:
the shard does not deliver the (R5) coefficient for the one basis vector it was
written to add (M1), and the numerical certificate it cites is partly vacuous
(M2) and blind to half the parity classes (M3). All three fixes are mechanical
and are spelled out above; I expect r2 to pass.

**SUMMARY: FAIL(M1, M2, M3)**
