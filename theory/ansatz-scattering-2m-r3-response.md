<!-- ROLE: disposition of theory/verdicts/ansatz-scattering-2m-r3.md. -->

# AC-EX-2M r3 repair response

Verdict addressed: `theory/verdicts/ansatz-scattering-2m-r3.md`.
Repaired shard: `theory/ansatz-scattering-2m.md` (status **SKETCH**).
Checker repaired at `theory/checks/ansatz_scattering_2m_check.py`.
The repair takes R3-O1 branch (ii), preserves the verified Haag--Ruelle port,
and matches the merged `AC-EX-2M` row in `claims/CLAIMS.md` exactly.  Every
R3 objection and NOTE is disposed below.

| ID | Disposition | What changed | Exact edit location |
|---|---|---|---|
| R3-O1 | **DOWNGRADED** | The adjudicated D29 is now identified as the fixed-time insertion `Q[f_ε]ψ`, not an HR creator family.  The valid `(ACE2M-LSZ)` port remains a theorem for admissible asymptotic HR families, while the D29 datum/channel identification is **OPEN**.  The sentence **“This theorem does NOT apply to the adjudicated D29.”** appears verbatim, and the R8/R19 `-2ik_s` obstruction is retained at its own linear order.  The shard's claims proposal is byte-for-byte the merged claims row. | `theory/ansatz-scattering-2m.md` proposer status; ⟨1⟩1(A2M.3); ⟨1⟩8 clauses 1 and 5, ⟨2⟩2; ⟨1⟩9.⟨2⟩2, ⟨2⟩6--⟨2⟩7; ⟨1⟩10.⟨2⟩3; §7 `AC-EX-2M` row; §8 HONEST STATUS |
| R3-O2 | **RETRACTED** | The false claim that the ratio-profile gate directly certifies absence of a hidden support-length factor is deleted.  The checker and spec now call it what it is: route agreement in ratio units under a one-sided mutation.  The finite `w≤3` cap and genuine monotonicity gate remain; the uncertified-scope paragraph expressly says a two-sided `w_Cw_D` fold is not excluded. | `theory/ansatz-scattering-2m.md` §6 A2M-C1b and Uncertified scope; `theory/checks/ansatz_scattering_2m_check.py` module docstring, `C1bResult`, `check_c1b`, `violations`, and output label |
| R3-O3 | **FIXED** | `(D29-den)` is quantified over every allowed full index tuple in the D29 interface family, matching (A2M.3)'s “every sequence” conclusion. | `theory/ansatz-scattering-2m.md` ⟨1⟩8 clause 3 |
| R3-O4 | **FIXED** | “Unconditional” is replaced by “conditional only on `(D29-den)`” at theorem/status/interface level.  Clause 3 now states that both displayed bounds are assumptions; Cauchy--Schwarz only motivates the numerator assumption. | `theory/ansatz-scattering-2m.md` proposer status; ⟨1⟩1(A2M.3); ⟨1⟩8 clauses 3--4; §8 HONEST STATUS |
| R3-O5 | **FIXED** | The source isolation hypothesis is relativized at the point of use: D6's magnon shell is globally embedded but isolated in the conserved `S^z`-charge-one sector; `S_x^-Ω` lies entirely on that band.  The distinct hypothesis scope of `commutators-decay(a)` is also stated. | `theory/ansatz-scattering-2m.md` ⟨1⟩8.⟨2⟩1, paragraph after the filter-transparency argument and its Justification |
| R3-O6 | **FIXED** | The source filter-transparency condition is displayed: the filter multiplier is one on the one-particle spectral support over `supp f_ε`.  D6's multiplicity label is bound explicitly as `b=1` on both sides of the vacuum identity. | `theory/ansatz-scattering-2m.md` ⟨1⟩8.⟨2⟩1, displayed vacuum identity and following paragraph |
| R3-O7 | **FIXED** | Diagonal compactness and fixed-`ε` HR creator independence are stated as separate results for different families.  Their composition is not claimed; `(ACE2M-SR)` controls regularity/order but does not supply the missing fixed-time amplitude match. | `theory/ansatz-scattering-2m.md` ⟨1⟩1(A2M.3); ⟨1⟩9.⟨2⟩2, ⟨2⟩6--⟨2⟩7; §8 HONEST STATUS |
| R3-N1 | **FIXED** | The C1a red text now names the two failures exactly: route-value and successive-ratio gates. | `theory/ansatz-scattering-2m.md` §6 A2M-C1a |
| R3-N2 | **FIXED** | Baseline `(1,1,d_sep)` points are excluded from the reported monotonicity margin.  Green now reports the actual negative margin `-6.503e-03@(1,2,6)` instead of an identically zero baseline. | `theory/checks/ansatz_scattering_2m_check.py` `check_c1b`; `theory/ansatz-scattering-2m.md` §6 A2M-C1b |
| R3-N3 | **RESIDUE** | Reproducibility is recorded below: all four optimized runs on the temporary copy produced the expected exits and stable numerical values. | This response, “Checker verification” |
| R3-N4 | **RESIDUE** | The independently reproduced `S'_{12}(0)=2i` / R8--R19 obstruction remains displayed and is now used only to fence the adjudicated fixed-time D29. | `theory/ansatz-scattering-2m.md` ⟨1⟩8.⟨2⟩2; §7 claims row; §8 HONEST STATUS |
| R3-N5 | **RESIDUE** | The verified local-TeX citations for the HR theorem, `commutators-decay(a)`, `HR-auxiliary(d)`, and `(creation-on-vacuum)` are preserved; the filter-transparency citation is added from the same source. | `theory/ansatz-scattering-2m.md` ⟨1⟩8.⟨2⟩1--⟨2⟩2; ⟨1⟩10 |
| R3-N6 | **RESIDUE** | The fenced D31-C2 derivation, including `V_w`, `Ψ_O`, and the exact chain identity, was not changed. | `theory/ansatz-scattering-2m.md` ⟨1⟩3 (unchanged) |
| R3-N7 | **FIXED** | The shard no longer silently chooses the asymptotic reading.  It follows the binding adjudication and merged row: D29 is fixed-time, and the HR theorem is separate. | `theory/ansatz-scattering-2m.md` proposer status; ⟨1⟩1; ⟨1⟩8 clauses 1 and 5; §7; §8 |
| R3-N8 | **RESIDUE** | Only this lane's checker was edited; no frozen checker or other file under `theory/checks/` was touched. | `git diff -- theory/checks/`; this response, “Scope audit” |

## Checker verification

All runs used a copied checker in
`/tmp/ansatz-scattering-2m-r3.dV5lZU`, under `python3 -O`:

| run | decisive output | exit |
|---|---|---:|
| green | `max_ratio=0.049383@(1,1,2)`, `ratio_route=1.187e-15`, `monotonicity_excess=-6.503e-03@(1,2,6)`; `PASS` | 0 |
| `--red-c1a` | route error `1.000000e+00`, ratio error `2.400000e+00`; `RED-OK` | 1 |
| `--red-c1b` | cap `1.404664`, monotonicity excess `6.145405e-01`; `RED-OK` | 1 |
| `--red-supportfold` | ratio-route disagreement `1.646091e-02`; `RED-OK` | 1 |

An additional copy was mechanically mutated so `w_Cw_D` multiplied **both**
contraction routes.  Green still exited 0, with `max_ratio=0.049383` and
negative monotonicity margin.  This reproduces R3-O2's criticism and is why the
former certificate claim is retracted rather than softened.  The source
checker contains no bare `assert`.

## Scope audit

- The §7 `AC-EX-2M` proposal is identical to the merged claims row, including
  its status, dependencies, proof/test fields, gate caveat, and verbatim
  scoping sentence.
- No REFUTED row, ML4-Ward second display at `n≥2`, or Bethe hypothesis is
  used.  The verified fixed-packet proof sections fenced by the r3 critic were
  not churned.
- The proof/checker/response repair is confined to the three authorized lane
  files; no commit was made.
