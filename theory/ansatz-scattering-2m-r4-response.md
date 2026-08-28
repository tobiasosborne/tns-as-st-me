<!-- ROLE: disposition of theory/verdicts/ansatz-scattering-2m-r4.md. -->

# AC-EX-2M r4 repair response

Verdict addressed: `theory/verdicts/ansatz-scattering-2m-r4.md`.
Repaired shard: `theory/ansatz-scattering-2m.md`.
Repaired checker: `theory/checks/ansatz_scattering_2m_check.py`.

R4-O1 takes fix (A): ⟨1⟩9.⟨2⟩5 is now explicitly a one-element
**constructed-channel** `(ACE2M-SR)` instance and backs no D29 claim.  The
current unsplit `AC-EX-2M` row remains mirrored byte-for-byte from
`claims/CLAIMS.md`; beneath that audit mirror, §7 proposes the requested split
into `AC-EX-2M` at PROVED (conditional on D31) and `AC-EX-2M-D29` at SKETCH.
No edit to `claims/CLAIMS.md` was made.

## Dispositions

| ID | Disposition | What changed | Exact edit location |
|---|---|---|---|
| R4-O1 | **FIXED** | Relabelled the sole D6 `(SR)` computation as the constructed-channel packet-amputated datum, stated that it is a singleton, removed the `(ACE2M-LSZ)`/⟨1⟩8 citation from its justification, displayed the `-2ik_s` branch mismatch, and stated that no D29 `(SR)` instance is exhibited.  All theorem/status echoes now say the same. | `theory/ansatz-scattering-2m.md` proposer status; ⟨1⟩1(A2M.3); ⟨1⟩9.⟨2⟩5--⟨2⟩6; §7 current lockstep mirror and `AC-EX-2M-D29` proposal; §8 **Conditional** |
| R4-O2 | **RETRACTED** | Kept the honest retraction: `ratio_route` is named only as agreement in rescaled units, is bounded by `16×` the pointwise agreement on the finite grid, and can fire alone only in `(6.25·10^-14,10^-12]`.  It is not advertised as evidence against a two-sided support factor. | `theory/ansatz-scattering-2m.md` §6 A2M-C1b and **Uncertified scope**; `theory/checks/ansatz_scattering_2m_check.py` module docstring, `C1bResult`, `violations`, output label |
| R4-O3 | **FIXED** | Added registered data mutant `--red-truth`, reaching G1/G2, and subtraction mutant `--red-c1b-sub`, reaching G4/G5/G6.  Every gate now has a registered mutant and every exit prints its gate path. | `theory/checks/ansatz_scattering_2m_check.py` `check_c1a`, `check_c1b`, `parse_args`, `main`; shard §6 A2M-C1a/C1b and coverage sentence |
| R4-O4 | **FIXED** | Added the theorem-domain gate `1/3<λ̃<1` and registered `--red-lambda` at `λ̃=3.7`.  The scope text now says that the `0.1` cap is only a `λ̃=1/2` statement and fails at `λ̃=0.34`; it does not certify the theorem's every-`λ̃` quantifier. | `theory/checks/ansatz_scattering_2m_check.py` `LAMBDA_E`, `violations`, `--red-lambda`, `main`; shard §6 A2M-C1b and **Uncertified scope** |
| R4-O5 | **FIXED** | Removed the pre-downgrade framing from both headings and made ⟨1⟩9's assumptions clause-specific: D29 clauses 1--4 generally, separate HR clause 5 only for ⟨2⟩2. | `theory/ansatz-scattering-2m.md` headings ⟨1⟩8 and ⟨1⟩9; ⟨1⟩9 **ASSUME** |
| R4-O6 | **FIXED** | Corrected ownership of (2M-1P): it is proved on D6 for the HR family built from the adjudicated charge acting on the vacuum.  What fails for fixed-time D29 is HR admissibility on an already prepared hard vector, not (2M-1P). | `theory/ansatz-scattering-2m.md` ⟨1⟩1 **ASSUME** paragraph; ⟨1⟩8 clause 5(b) |
| R4-N1 | **RESIDUE** | Preserved exact current-row lockstep while quarantining the two new rows as an r5 split proposal.  `cmp` of the first `AC-EX-2M` row in the shard against the merged row exits 0. | `theory/ansatz-scattering-2m.md` §7 **Current claims row lockstep mirror** and **ROW SPLIT proposal**; this response, **Lockstep and row split** |
| R4-N2 | **RESIDUE** | Preserved the real non-baseline monotonicity margin `-6.503e-03@(1,2,6)`. | checker `check_c1b`; shard §6 A2M-C1b |
| R4-N3 | **RESIDUE** | The two-sided support-fold claim remains retracted.  No new gate is claimed to exclude it; support-length independence remains the analytic content of ⟨1⟩3. | shard §6 A2M-C1b and **Uncertified scope** |
| R4-N4 | **RESIDUE** | Retained the independent ground-truth route and added `--red-truth`; shifting the target by `10^-6` now exits on G1/G2. | checker `check_c1a`; this response, **Checker verification** |
| R4-N5 | **RESIDUE** | Preserved all-gate evaluation before exit.  `violations()` returns every fired `(gate,message)` pair, and `main` reports the complete path. | checker `violations`, `main` |
| R4-N6 | **RESIDUE** | The original three red modes retain the mutually specific paths `{G2,G3}`, `{G5,G7}`, `{G6}`.  The four new modes are coverage mutants and report their additional paths explicitly. | checker `parse_args`, `main`; this response, exit-path table |
| R4-N7 | **FIXED** | Added a controlled fixed-route subtraction probe and registered `--red-route-collapse`.  Collapsing both routes now prints `agreement=0`, `ratio_route=0`, but fails G8 with probe error `1.0`; the pattern-#1 regression is guarded. | checker `connected_routes`, `check_c1b`, G8 in `violations`, `--red-route-collapse` |
| R4-N8 | **RESIDUE** | The verified local-TeX citations and the HR port were not changed. | shard ⟨1⟩8.⟨2⟩1--⟨2⟩2 and ⟨1⟩10 (unchanged) |
| R4-N9 | **RESIDUE** | Preserved the charge-sector reading and made its consequence precise: (2M-1P) belongs to the D6 HR family; fixed-time D29 still lacks HR admissibility. | shard ⟨1⟩8 clause 5(b) and ⟨2⟩1 |
| R4-N10 | **RESIDUE** | The analytic support-length-independent D31-C2 proof remains untouched. | shard ⟨1⟩3 (unchanged) |
| R4-N11 | **RESIDUE** | The downgrade still has no downstream consumer; the row split changes only merge proposals. | shard §7; no shared-file edit |
| R4-N12 | **RESIDUE** | Fenced proof sections ⟨1⟩2--⟨1⟩7 were not churned; checker edits are confined to this lane's checker. | `git diff -- theory/ansatz-scattering-2m.md theory/checks/ansatz_scattering_2m_check.py` |
| R4-N13 | **FIXED** | The singleton status is now explicit at theorem, leaf, honest-status, current-row, and split-interface-row levels. | shard ⟨1⟩1(A2M.3); ⟨1⟩9.⟨2⟩5; §7 rows; §8 **Conditional** |

## Checker verification

All primary runs used `python3 -O` from the repository root.  Green exits 0;
every registered mutation exits 1 and names the gates it reaches.

| run | exit path | exit |
|---|---|---:|
| green | no violation; `direct=3.354e-15`, `route=3.243e-15`, `ratio=5.605e-10`; `agreement=1.128e-16`, `max_ratio=0.049383@(1,1,2)`, `ratio_route=1.187e-15@(1,1,6)`, `route_guard=0`, `monotonicity_excess=-6.503e-03@(1,2,6)` | 0 |
| `--red-c1a` | G2 route value `1.0`; G3 ratio `2.4` | 1 |
| `--red-c1b` | G5 cap `1.404664@(3,2,2)`; G7 monotonicity `6.145405e-01@(3,2,2)` | 1 |
| `--red-supportfold` | G6 ratio-route disagreement `1.646091e-02@(2,2,2)` only | 1 |
| `--red-truth` | G1 direct and G2 route values both displaced by `1.0e-6` | 1 |
| `--red-c1b-sub` | G4 agreement `1.0`; consequential G5 cap `15.990245` and G6 ratio-route `15.98049` | 1 |
| `--red-route-collapse` | G8 route-independence probe `1.0` only; ordinary agreement and `ratio_route` both print `0.0` | 1 |
| `--red-lambda` | G0, `λ̃=3.7∉(1/3,1)` only | 1 |

Gate reachability is therefore complete:

| gate | registered reaching mutant(s) |
|---|---|
| G0 lambda domain | `--red-lambda` |
| G1 C1a direct value | `--red-truth` |
| G2 C1a route value | `--red-c1a`, `--red-truth` |
| G3 C1a ratio | `--red-c1a` |
| G4 C1b route agreement | `--red-c1b-sub` |
| G5 C1b cap | `--red-c1b`, `--red-c1b-sub` |
| G6 C1b `ratio_route` | `--red-supportfold`, `--red-c1b-sub` |
| G7 C1b support monotonicity | `--red-c1b` |
| G8 route-independence probe | `--red-route-collapse` |

The absurd-input audit was also run through the checker functions without
editing the source: `λ̃=3.7`, `-5.0`, and `10^6` each reach G0; `λ̃=0.34` is
inside the theorem domain but reaches G5 with cap `0.106797`.  There are no
bare `assert` statements.

## Lockstep and row split

The first §7 `AC-EX-2M` row is an explicitly labelled audit mirror, not a new
merge action.  It includes the orchestrator's r4 replacement sentence and the
renamed `ratio_route` caveat.  The command

`cmp <(rg -m1 '^\| AC-EX-2M \|' theory/ansatz-scattering-2m.md) <(rg -m1 '^\| AC-EX-2M \|' claims/CLAIMS.md)`

exits 0.  Immediately below it, the **ROW SPLIT proposal** supplies exactly
two complete replacement rows:

1. `AC-EX-2M` — **PROVED (conditional on D31)**, limited to
   (A2M.1)--(A2M.2), in the `AC-EX` conditional-implication register and with
   no interface content.
2. `AC-EX-2M-D29` — **SKETCH**, containing `(D29-den)` diagonal compactness,
   the HR-family `(ACE2M-LSZ)` theorem, and the two named missing steps:
   branch (i) at `O(k_s)` and an `(ACE2M-SR)` instance for the fixed-time D29
   family it constrains.

The proposals are verbatim-applicable after r5 adjudication and are not
silently merged here.

## Scope audit

- No REFUTED row, ML4-Ward second display at `n≥2`, `𝒮_W` nonemptiness, or
  Bethe/integrability hypothesis is used.
- The §7 `AC-EX-2M` proposal depends only on the fenced (A2M.1)--(A2M.2)
  material; all D29 dependencies and all open interface work live in
  `AC-EX-2M-D29`.
- Changes are confined to the three authorized lane files.  No commit was
  made.
