<!-- ROLE: disposition of theory/verdicts/ansatz-scattering-2m-r5.md.
     Writable lane: theory/ansatz-scattering-2m.md, this file,
     theory/checks/ansatz_scattering_2m_check.py.  claims/CLAIMS.md was NOT
     edited: the r5 critic's cells are already applied there verbatim.
     No commit was made by this lane. -->

# AC-EX-2M r5 repair response — the hoist

Verdict addressed: `theory/verdicts/ansatz-scattering-2m-r5.md` —
**FAIL(R5-O1)**, 0 FATAL, 1 MAJOR, 6 MINOR, 12 NOTE.
Repaired shard: `theory/ansatz-scattering-2m.md`.
Repaired checker: `theory/checks/ansatz_scattering_2m_check.py`.

Scope taken from the critic's own framing: r5's sole MAJOR indicts **no
mathematics**.  Nothing was redesigned and nothing the critic fenced in §7 was
churned.  The round is one hoist, one gate relabel, and eighteen small
dispositions.

**The promotion had already landed before this round.**  `claims/CLAIMS.md`
carries `AC-EX-2M` at **PROVED** (conditional, A2M.1--A2M.2; per
ansatz-scattering-2m-r5.md §9) and `AC-EX-2M-D29` at **SKETCH**, both cells
written by the critic and applied verbatim.  This repair brings the shard into
lockstep with **those** cells, not with the prover's r4 draft rows, which were
correctly not applied.  `claims/CLAIMS.md` was not touched.

## 1. R5-O1 — the hoist (the MAJOR)

`⟨1⟩9.⟨2⟩4` proved *D6 satisfies D31(1)--(5)* — the promoted row's nonvacuity
certificate — while sitting beneath `⟨1⟩9`'s **ASSUME** of the adjudicated D29
interface clauses 1--4, and while proving a proposition that is not part of
`⟨1⟩9`'s **PROVE** (A2M.3).  Under L6b inheritance the certificate therefore
read as consuming the D29 interface, in the one round whose entire basis is
D29-independence.

**Executed.**  A new top-level step now sits between `⟨1⟩7` and `⟨1⟩8`:

- new section `## 3′. Nonvacuity: D6 is a model of D31`;
- new step `### ⟨1⟩7′. D6 is a nonempty instance of D31`, with
  **ASSUME.** *D6 and fixed compact packets obeying D31(4).*
  **PROVE.** *D6 satisfies D31(1)--(5).*  — the critic's FIX DEMAND verbatim;
- the demanded sentence, in the step header: *"This step uses no D29 interface
  clause and stands outside ⟨1⟩8--⟨1⟩9's interface ASSUME; it is stated here so
  that (A2M.1)--(A2M.2)'s conditional implication carries its own nonvacuity
  certificate."*
- `⟨1⟩7′.⟨2⟩1` is the old `⟨1⟩9.⟨2⟩4` body **byte-for-byte**, with its
  Justification line unchanged (`D1`, D6's positive swap form, proposed D31,
  ML2 (17)--(21), the Plancherel resolution ML2 (21) — no D29 clause);
- `⟨1⟩7′.⟨2⟩2 QED` records that its only inputs are D1, D6, ML2 and
  `⟨1⟩2.⟨2⟩3`, none of them a D29 clause.

**No mathematics changed.**  The hoisted text was diffed against the old block
before and after the move; the body and Justification are identical strings.

**Echoes brought into line.**  `⟨1⟩1` gains a **NONVACUITY** paragraph naming
`⟨1⟩7′`; the header status block and §8 say the same; `⟨1⟩2.⟨2⟩2`'s
acyclicity sentence now covers `⟨1⟩7′` explicitly (it uses `⟨1⟩2.⟨2⟩3`, not the
forward-referencing `⟨2⟩2`, so the step graph stays acyclic).

### The one deviation from the FIX DEMAND, and why

The FIX DEMAND ends "*Renumber `⟨1⟩9`'s remaining sub-steps.*"  **That was not
done, deliberately**, and `⟨1⟩9.⟨2⟩4` is retained as a vacated address
carrying only a labelled cross-reference marker (*"[HOISTED — now ⟨1⟩7′;
address retained, not renumbered]"*, explicitly not a proof step).

Reason: renumbering would falsify two pointers inside **applied,
un-editable** `claims/CLAIMS.md` cells.  `AC-EX-2M-D29`'s `where-proved` reads
"*⟨1⟩8--⟨1⟩9, excluding ⟨1⟩9.⟨2⟩4 (which belongs to AC-EX-2M)*", and its
statement cell cites "*(⟨1⟩9.⟨2⟩5)*" for the constructed-channel jet.  Sliding
`⟨2⟩5→⟨2⟩4` would make that exclusion name the jet — which does belong to
`AC-EX-2M-D29` — and would strand the jet pointer.  Keeping the addresses
stable keeps every applied pointer exact at the cost of one documented gap.
The marker states the reason in the shard, so no auditor has to reconstruct it.

Renumbering becomes safe in the same pass in which the orchestrator applies r5
§9 condition 2 (below).  Filed as RESIDUE-1.

## 2. R5-O3 — the G8 `route_guard`

The critic is right and the objection is accepted without argument: the guard
added last round as the fix to R4-N7 is

`|raw − (raw − ω_Cω_D) − ω_Cω_D| ≡ 0`

for every input — the corpus's fifth identically-zero gate, shipped as the fix
to the NOTE warning about identically-zero gates.

**Option (β) taken: renamed and documented as a code-shape guard, in all four
places it is advertised.**  Option (α) was tried first and **rejected on
evidence** (§4 below).  (β) is also what the applied `where-tested` cell
requires — it already reads "*The `route_guard` gate (G8) is identically `0`
for every input by algebra — a code-shape guard against route collapse, not a
numerical certificate*" — so (α) would have put the shard out of lockstep with
an un-editable cell, and would have changed the nine-gate/seven-exit-path
inventory the same cell records.

What changed:

- `C1bResult.route_independence_error/_location` → `route_shape_error/_location`;
- G8's message is now "*C1b route-shape guard (code shape only, identically 0
  in green; certifies no number)*";
- a twelve-line comment at the probe states that it is identically zero, is
  blind to the tensor, the fixed point, the observable, the norms and the
  λ̃ domain, and that a genuine subtraction-coefficient error leaves it at 0
  while G4 reports `1e-6`;
- the module docstring gains a **WHAT EACH GATE IS EVIDENCE FOR** paragraph
  separating the seven numerical gates from G8, and forbidding the (α)
  "upgrade" with the measured numbers;
- shard §6 gains **"G8 is a code-shape guard, not a numerical certificate"**,
  ending "*No round may cite G8 as numerical evidence for D31-C2 or for
  anything the `AC-EX-2M` row claims.*"

**The printed key `route_guard` is unchanged on purpose** — the applied cell
names it, and the name is already a guard-word, not a certificate-word.  The
gate id, the red mode, the exit path and the nine-gate inventory are all
unchanged, so the applied `where-tested` cell stays true to the byte.

G8 keeps the only content it ever had, and that content is retained: it still
kills all three route-collapse implementations (the registered flag,
`direct:=fixed`, `fixed:=direct`), each on G8 alone (§4).

## 3. Dispositions

| ID | Disposition | What changed | Exact location |
|---|---|---|---|
| R5-O1 (MAJOR) | **FIXED** | `⟨1⟩9.⟨2⟩4` hoisted verbatim to a new top-level `⟨1⟩7′` outside the D29 ASSUME, with the demanded ASSUME/PROVE and the demanded sentence; QED records D29-freeness of its inputs.  Sub-steps deliberately **not** renumbered (§1, RESIDUE-1). | shard §3′ `⟨1⟩7′.⟨2⟩1--⟨2⟩2`; marker at `⟨1⟩9.⟨2⟩4`; echoes at header, `⟨1⟩1` **NONVACUITY**, `⟨1⟩2.⟨2⟩2`, §8 |
| R5-O2 (MINOR) | **FIXED** | §7's draft split proposal is deleted; §7 now mirrors the two **applied** rows byte-for-byte, so the adjudicated `ratio_route` retraction (`16×`, `(6.25·10^-14,10^-12]`, "does NOT certify that a two-sided support-length factor is absent") is back in the row at the moment the status ratchets.  It also remains in §6 and the module docstring, as it already did. | shard §7 **Applied `claims/CLAIMS.md` lockstep mirror** |
| R5-O3 (MINOR) | **FIXED** (option β) | G8 renamed and documented as a code-shape guard in code, message, docstring and §6; option (α) tried and rejected on evidence. | checker docstring, `C1bResult`, `check_c1b` probe comment, `violations` G8, `--red-route-collapse` help; shard §6 |
| R5-O4 (MINOR) | **FIXED** | `⟨1⟩8` gains the **Schema convention** paragraph: `(SR)[X]` is the three clauses with `A_j` replaced by any `L²(I)`-valued `ε`-family; `(ACE2M-SR)=(SR)[A_j]` for the D29 datum, together with existence of its `N,t` limits.  `⟨1⟩9.⟨2⟩5` now says it verifies `(SR)[A]`, that the two **uniformity** clauses are trivial, and that the `N,t`-limit clause is **bypassed rather than satisfied** because no `N` or `(W,σ)` family is formed.  Same correction at `⟨1⟩1(A2M.3)`, §8 **Conditional**, and the `notation.md` proposal row. | shard `⟨1⟩8` after **(SR)**; `⟨1⟩9.⟨2⟩5` PROVE line and closing paragraph; `⟨1⟩1(A2M.3)`; §7 notation table; §8 |
| R5-O5 (MINOR) | **FIXED** | Both defects were in the draft row, which is gone.  The applied row carries the house register `**PROVED** (conditional, A2M.1--A2M.2; per ansatz-scattering-2m-r5.md §9)` and D31(5) in the correct direction (`𝓡_inel` energies **exceed** `sup_{I_2}E+η_inel`).  The theorem statement `⟨1⟩1(A2M.2)` was upgraded to the same wording, so the shard and the row now state the separation identically. | shard §7 mirror; `⟨1⟩1(A2M.2)` |
| R5-O6 (MINOR) | **FIXED** | The applied `AC-EX-2M-D29` row restores both losses: "*the `(W,σ)`-uniform form of `(SR)` is open on every model, D6 included*" and the full D29 provenance (`theory/soft-index.md` §7.1 D29(2); `theory/soft-index-b.md` §M1 adopted by `theory/verdicts/soft-index-adjudication-r1.md` §3.1).  §8 **Conditional** was re-worded to match the first. | shard §7 mirror; §8 **Conditional** |
| R5-O7 (MINOR) | **FIXED** | The false blanket sentence is replaced by the critic's text, extended to cover `⟨1⟩7′`: `⟨2⟩1` cites nothing later; `⟨2⟩2` is the only forward-pointing step of `⟨1⟩2`, to `⟨1⟩7.⟨2⟩2`, which no step of `⟨1⟩3--⟨1⟩7′` uses; `⟨1⟩5.⟨2⟩4` refers to `⟨1⟩2.⟨2⟩1` for scope only; `⟨1⟩7′.⟨2⟩1` uses `⟨2⟩3`, not `⟨2⟩2`. | shard `⟨1⟩2.⟨2⟩2` Justification |
| R5-N1 | **RESIDUE** | The r4 leaf fix is untouched: `⟨1⟩9.⟨2⟩5`'s Justification line, its constructed-channel PROVE line and its `−2ik_s\|P_{12}⟩` disclaimer are unchanged apart from R5-O4's `(SR)[A]` naming. | shard `⟨1⟩9.⟨2⟩5` |
| R5-N2 | **RESIDUE, with disclosure** | The byte-freeze of the promoted material now **ends**, in exactly one place and only because the critic demanded it: `⟨1⟩2.⟨2⟩2`'s non-circularity sentence (R5-O7).  `⟨1⟩3`--`⟨1⟩7` remain byte-identical (verified by diff, §5).  `⟨1⟩7′` is new text only in its heading, ASSUME/PROVE and QED; its body is the hoisted block unchanged. | shard `⟨1⟩2.⟨2⟩2`; §3′ |
| R5-N3 | **SUPERSEDED** | Quarantine is no longer the right posture: the split is merged.  §7's old *"Current lockstep mirror (not a merge action)"* + *"ROW SPLIT proposal"* pair is replaced by one **Applied ... lockstep mirror** section carrying both applied rows byte-for-byte, with "*do not reapply, paraphrase, or amend*". | shard §7 |
| R5-N4 | **FIXED** | `--red-supportfold`'s self-fulfilling character is now disclosed in the spec, not only in the verdicts: it multiplies `ratio` and not `direct_ratio`, **after** `agreement_error` is recorded, so G6 is the only gate it can reach; retained as G6's reachability witness, not as evidence. | shard §6 A2M-C1b |
| R5-N5 | **RESIDUE** | The `16×` amplification and the `(6.25·10^-14,10^-12]` fire-alone window stay quantified in §6 and in the applied row.  Reconfirmed this round by mutant `c3`: `agreement 1.000e-06 → ratio_route 1.600e-05`, exactly `16×`. | shard §6; §7 mirror; §4 below |
| R5-N6 | **RESIDUE** | Recorded in the shard rather than only in a verdict: "*Nothing under `theory/` consumes `AC-EX-2M`, so the split carries no downstream blast radius.*" | shard §8 **Proved from D31** |
| R5-N7 | **RESIDUE** | `\|S_phys\|=1` remains proved at `⟨1⟩7.⟨2⟩3` from ML2 (18) and is now also stated in the theorem clause, matching the applied row. | shard `⟨1⟩7.⟨2⟩3` (unchanged); `⟨1⟩1(A2M.2)` |
| R5-N8 | **FIXED** | The velocity-ordering caveat now appears in the theorem clause as well as at `⟨1⟩7.⟨2⟩3`: "*`S_{21}` under the opposite velocity ordering*".  The applied row carries it too. | shard `⟨1⟩1(A2M.2)`; §7 mirror |
| R5-N9 | **RESIDUE** | No `refs/` citation, anchor or ML2 equation number was added, removed or altered this round.  The only new prose citing sources is the hoisted block, whose citations are unchanged. | shard (no citation diff) |
| R5-N10 | **RESIDUE** | `⟨1⟩2.⟨2⟩3`'s exact identity `E_sc−E_b=J\|e^{iq}−c\|²` is untouched, and `⟨1⟩7′.⟨2⟩1` still consumes it for `d_B>0`. | shard `⟨1⟩2.⟨2⟩3` (unchanged) |
| R5-N11 | **RESIDUE** | `⟨1⟩8` clause 3's "*Both displayed inequalities are assumptions … not a derivation of it in this shard*" is unchanged; the only `⟨1⟩8` edit is R5-O4's schema paragraph, which is appended after **(SR)** and touches no clause. | shard `⟨1⟩8` clause 3 (unchanged) |
| R5-N12 | **RESIDUE** | §6 continues to say the `0.1` cap is a `λ̃=1/2` statement that fails at `λ̃=0.34` and certifies no every-`λ̃` quantifier; re-verified this round (`λ̃=0.34` → exit 2 at `cap 0.106797`; `λ̃=0.9999` → exit 0). | shard §6 **Uncertified scope**; §4 below |

Count: 1 MAJOR + 6 MINOR + 12 NOTE = **19 dispositions**, one row each.

## 4. Checker verification

All runs `python3 -O` from the repository root, on the committed file; mutants
on copies in a scratch directory, never in place.  `grep -cE '^\s*assert\b'` →
**0**.

### 4.1 Registered modes — exit code and exit path

| run | gates fired | exit |
|---|---|---|
| green | — (`C1a direct 3.354e-15 route 3.243e-15 ratio 5.605e-10`; `C1b agreement 1.128e-16, max_ratio 0.049383@(1,1,2), ratio_route 1.187e-15@(1,1,6), route_guard 0.000e+00@(1,1,2), monotonicity −6.503e-03@(1,2,6)`) | **0** |
| `--red-lambda` | `{G0}` | 1 |
| `--red-truth` | `{G1,G2}` | 1 |
| `--red-c1a` | `{G2,G3}` | 1 |
| `--red-c1b-sub` | `{G4,G5,G6}` | 1 |
| `--red-c1b` | `{G5,G7}` | 1 |
| `--red-supportfold` | `{G6}` | 1 |
| `--red-route-collapse` | `{G8}` | 1 |

Every number and every exit path is unchanged from the critic's §4.1 table, so
the applied `where-tested` cell remains true to the byte.  Nine gates, seven
pairwise-distinct violation sets, all nine evaluated before exit.

### 4.2 Mutants on copies (re-run after the relabel)

| mutant | falsifies | result |
|---|---|---|
| `c1` — `direct := fixed` unconditionally | route collapse, implementation 2 | exit 2, **G8 alone** |
| `c2` — `fixed := direct` unconditionally | route collapse, implementation 3 | exit 2, **G8 alone** |
| `c3` — subtraction coefficient `1 → 1.000001` | a genuine route error | exit 2, `G4 1.000e-06`, `G6 1.600e-05` (the `16×`); **G8 stays `0`** |
| `d1` — `A^a=σ_a/2` | tensor normalization | exit 2 (`G1,G2,G3,G5`) |
| `d2` — `RIGHT_FIXED=diag(0.6,0.4)` | transfer fixed point | exit 2 (`G1,G2,G3,G5`) |
| `d3` — `C=I+2S^z` | the observable | exit 2 (`G1,G2`) |
| `d4` — `block_operator_norm→1.0` | the SVD norms | exit 2 (`G5`, `cap 0.197531`) |
| `λ̃ = −5.0 / 1e6 / 1/3` | absurd and boundary domain | exit 2 in all three |
| `λ̃ = 0.34` | in-domain but past the cap | exit 2 (`G5 cap 0.106797`) |
| `λ̃ = 0.9999` | in-domain | exit 0 |

`c1`/`c2` are the critic's own two extra route-collapse implementations,
rebuilt and re-run: G8 still catches both, and nothing else does.  `c3`
re-confirms that G8 is blind to a genuine numerical error that G4 catches.

### 4.3 Why option (α) was rejected — measured, not asserted

The critic's (α) recomputes the fixed route with
`subtracted = propagated − (1+δ)·fixed_projection(right)` and requires the
response to equal `δ·ω_Cω_D`.  Implemented on a copy over the full 27-point
grid, the residual is

`|(fixed − fixed_δ) − δ·ω_Cω_D| = 8.3e−17` (baseline),
`8.8e−17` (`A^a=σ_a/2`), `1.0e−16` (`RIGHT_FIXED=diag(0.6,0.4)`),
`2.9e−16` (`C=I+2S^z`).

`block_transfer` and `fixed_projection` are linear, so
`fixed − fixed_δ = δ·tr(right)·tr(T_C^{w_C}(RIGHT\_FIXED)) = δ·ω_Cω_D`
identically; the residual is pure roundoff and does **not** move under data
mutation.  (α) is therefore a *sixth* identically-zero gate wearing a
numerical name — a worse outcome than the honest relabel, since it would read
as a certificate.  This is recorded in the checker docstring and in §6 so no
future round re-proposes it.

The honest position, now stated in all four places: **route agreement is
certified by G4** (live and sharp at `1e-6`, per `c3`); G8 certifies only that
the two route expressions have not been collapsed into one.

## 5. Lockstep

- §7's two mirror rows versus `claims/CLAIMS.md` lines for `AC-EX-2M` and
  `AC-EX-2M-D29`: **byte-identical**, 4467 and 3465 bytes, checked
  programmatically after the edit.
- Header status block, `⟨1⟩1`, §7 and §8 now all say: `AC-EX-2M` **PROVED**
  (conditional, A2M.1--A2M.2; per ansatz-scattering-2m-r5.md §9);
  `AC-EX-2M-D29` **SKETCH**; the implication is non-vacuous by `⟨1⟩7′`; the
  only verified `(SR)` instance is `(SR)[A]` for the one-element
  constructed-channel datum and it backs no D29 claim.
- `⟨1⟩3`--`⟨1⟩7` are byte-identical to the promoted text (`git diff`
  against the promotion commit shows no hunk in that range).  The only edit
  inside `⟨1⟩2`--`⟨1⟩7` is `⟨1⟩2.⟨2⟩2`'s sentence, mandated by R5-O7.
- Reliance audit unchanged: no REFUTED row, no ML4-Ward `n≥2`, no ML5, no
  `𝒮_W`, no Bethe/integrability hypothesis; every bare `S2` is the lane name.

## 6. Residues

**RESIDUE-1 (for the orchestrator, one cell).**  `AC-EX-2M`'s `where-proved`
reads "*⟨1⟩2--⟨1⟩7, plus ⟨1⟩9.⟨2⟩4 for the D6 instance of D31 (r5 R5-O1
requires that step be hoisted out of ⟨1⟩9's D29 ASSUME; …)*".  The hoist has
landed, so the parenthetical is satisfied as written and r5 §9 condition 2
permits the cell to be simplified to "*theory/ansatz-scattering-2m.md
⟨1⟩2--⟨1⟩7′*".  That is a `claims/CLAIMS.md` edit, outside this lane, and was
deliberately not made.  `AC-EX-2M-D29`'s `where-proved` would then read
"*⟨1⟩8--⟨1⟩9*" with no exclusion clause.  Only after that edit is it safe to
renumber `⟨1⟩9`'s sub-steps `⟨2⟩5--⟨2⟩7 → ⟨2⟩4--⟨2⟩6` and drop the marker;
doing it now would falsify two applied pointers (§1).

**RESIDUE-2 (unchanged, correctly retracted).**  `--red-supportfold` remains
self-fulfilling; it is now disclosed as such in §6 and kept only as G6's
reachability witness.

**RESIDUE-3 (unchanged, open).**  No gate certifies `⟨1⟩3`'s every-`λ̃`
quantifier; that remains analytic content, as §6 says.  The `0.1` cap is a
`λ̃=1/2` statement.

**NOTE on the working tree.**  This lane made no commit.  A concurrent
orchestrator commit (`d3e14ff`, the ACE-LD r2 lane) swept these two lane files
into its tree along with unrelated files; the content is exactly as repaired
here.

## 7. What this round did not do

No mathematics was added, removed or altered.  No definition, notation entry
or claim row was merged.  `claims/CLAIMS.md`, `definitions.md` and
`notation.md` were not edited.  The critic's §7 fence — the independence walk,
`⟨1⟩3.⟨2⟩1--⟨2⟩2`, the D31-C2 target and C1b grid, the `S_{12}` algebra, the
`⟨1⟩9.⟨2⟩5` Taylor arithmetic, `⟨1⟩2.⟨2⟩3`'s fence, `⟨1⟩9.⟨2⟩4`'s content, the
cone counting, and the checker's hygiene and coverage — was not churned.
