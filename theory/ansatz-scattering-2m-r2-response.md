<!-- ROLE: disposition of theory/verdicts/ansatz-scattering-2m-r2.md. -->

# AC-EX-2M r2 repair response

Verdict addressed: `theory/verdicts/ansatz-scattering-2m-r2.md`.
Repaired shard: `theory/ansatz-scattering-2m.md` (self-status remains
**SKETCH**).  Checker implemented at
`theory/checks/ansatz_scattering_2m_check.py`.  Every R2 objection is
disposed below; no objection is silently deferred.

| ID | Disposition | What changed | Exact edit location |
|---|---|---|---|
| R2-O1 | **FIXED** | D29's charge-created soft slot is now expressly an asymptotic HR leg carried through `t→±∞`.  The one-particle equality (2M-1P) and D31(4)'s disjoint velocities feed a port of source Theorem `Haag-Ruelle`'s final creator-choice-independence clause.  The commutator proof gives equality of the connected pairings, so `(ACE2M-LSZ)` is a theorem, not the old vacuum-vector hypothesis.  The raw fixed-time D6 obstruction `(1-S_{12})|P_{12}⟩` is displayed and retained. | `theory/ansatz-scattering-2m.md` ⟨1⟩8(1),(5), ⟨1⟩8.⟨2⟩1--⟨2⟩2; ⟨1⟩9.⟨2⟩2; ⟨1⟩10.⟨2⟩3; §8 HONEST STATUS |
| R2-O2 | **DOWNGRADED** | The unconditional part of (A2M.3) is now exactly the full-index diagonal statement proved by reflexive weak compactness; no iterated inner limit is claimed.  `(ACE2M-SR)` separately assumes existence of the `N,t` limits before its first-jet conclusion.  Interface clause 3 restores “on the selected hard packet” and displays `ess inf|𝒟_α|≥d_I>0`, `sup||𝒝_α||≤C_I`, hence `sup||𝒜_α||≤C_I/d_I`.  Statement, proof, merge row, and status moved in lockstep. | `theory/ansatz-scattering-2m.md` ⟨1⟩1(A2M.3); ⟨1⟩8(3)--(4), `(ACE2M-SR)`; ⟨1⟩9.⟨2⟩1--⟨2⟩3; §7 AC-EX-2M row; §8 |
| R2-O3 | **FIXED** | `ε_0` is retained only as D31's nonzero-velocity packet condition and is declared unused by A2M.1--A2M.2.  It was removed from the Cook constant, while the soft interval endpoint is renamed `ε_★`.  The notation proposal now scopes `ε_v,ε_0,s_N(F)`. | `theory/ansatz-scattering-2m.md` ⟨1⟩2.⟨2⟩1,⟨2⟩3; ⟨1⟩5.⟨2⟩4; ⟨1⟩8 `(ACE2M-SR)`; §7 D31(4) and notation rows |
| R2-O4 | **DOWNGRADED** | (D29-order) now makes `W↑ℤ,σ↓0` a named joint exhaustion `j` after `N,t`, with `ε` last.  It explicitly disclaims an iterated `lim_σ lim_W`; `(SR)` is the stated diagonal specialization. | `theory/ansatz-scattering-2m.md` ⟨1⟩8(4), `(ACE2M-SR)`; ⟨1⟩9.⟨2⟩3 |
| R2-O5 | **FIXED** | The dangling fixed-`ε`/`ε→0` quantifier is removed.  The theorem defines data at every fixed positive scale and quantifies over families with `ε_r↓0`. | `theory/ansatz-scattering-2m.md` ⟨1⟩1(A2M.3) |
| R2-O6 | **FIXED** | The claims proposal now says a fixed range “lies in” the ML2 summand; dependencies add D10 and D24; every flagged new symbol is covered by an exact notation proposal or its shard-local defining step. | `theory/ansatz-scattering-2m.md` §7 AC-EX-2M row and notation rows |
| R2-O7 | **FIXED** | A2M-C1a again requires two **connected** contractions.  Its successive-ratio gate is explicitly `|ratio+1/3|≤10^-8`, which passes through `d=12`; the value gate remains `10^-12`. | `theory/ansatz-scattering-2m.md` §6 A2M-C1a; `theory/checks/ansatz_scattering_2m_check.py` `check_c1a`, `violations` |
| R2-O8 | **FIXED** | C1b retains the cap and adds support-length monotonicity plus agreement of the entire normalized support profile between direct and fixed-point-subtracted contractions.  `--red-supportfold` multiplies the latter numerator by `w_Cw_D` and now exits 1 on a `1.646091e-02` profile disagreement. | `theory/ansatz-scattering-2m.md` §6 A2M-C1b; `theory/checks/ansatz_scattering_2m_check.py` `check_c1b`, `violations` |
| R2-O9 | **FIXED** | A Lamport leaf checks D31(1)--(5) on D6: product MPS, positive swap Hamiltonian and vacuum kernel, exact isometric magnon map, filtered `S^-` creators, packet conditions, and ML2's isolated bound summand.  A second leaf displays the normalized smeared Taylor formula `A(ε)=A(0)+εm_1∂S_phys(0)+O_{L²}(ε²)`, with no extra `ε^{-1}` amputation. | `theory/ansatz-scattering-2m.md` ⟨1⟩9.⟨2⟩4--⟨2⟩5 |
| R2-O10 | **FIXED** | The D6 exact-match leaf now maps every torus pair to ML2's `K^♯∈(-π,π]`, `q^♯∈(0,π)` chart and states that odd-`r` anti-periodicity changes the fiber gauge, not `S_phys`. | `theory/ansatz-scattering-2m.md` ⟨1⟩7.⟨2⟩3 |
| R2-O11 | **FIXED** | The charge is written `Q[f̂_ε;ξ^-]` in D10(c)'s position-profile convention; `q_x^-=S_x^-` cites `soft-current-recon.md` ⟨1⟩1; and the creator multiplicity label `b` is bound on both sides of (2M-1P). | `theory/ansatz-scattering-2m.md` ⟨1⟩8(1),(5), ⟨1⟩8.⟨2⟩1; §7 notation rows |

## Rebuttal computations

No objection was rebutted.  All were repaired at or below the critic's
surviving-statement ceiling.  The checker was run under optimization so bare
assertions could not mask a failure:

```text
$ python3 -O theory/checks/ansatz_scattering_2m_check.py
A2M-C1a direct=3.354e-15 route=3.243e-15 ratio=5.605e-10
A2M-C1b agreement=1.128e-16 max_ratio=0.049383@(1, 1, 2) profile=1.187e-15@(1, 1, 6) monotonicity_excess=0.000e+00@(1, 1, 2)
PASS: A2M-C1a/C1b
exit 0

$ python3 -O theory/checks/ansatz_scattering_2m_check.py --red-c1a
A2M-C1a direct=3.354e-15 route=1.000e+00 ratio=2.400e+00
A2M-C1b agreement=1.128e-16 max_ratio=0.049383@(1, 1, 2) profile=1.187e-15@(1, 1, 6) monotonicity_excess=0.000e+00@(1, 1, 2)
RED-OK: C1a route value error 1.000000e+00 > 1.0e-12 | C1a ratio error 2.400000e+00 > 1.0e-08
exit 1

$ python3 -O theory/checks/ansatz_scattering_2m_check.py --red-c1b
A2M-C1a direct=3.354e-15 route=3.243e-15 ratio=5.605e-10
A2M-C1b agreement=1.128e-16 max_ratio=1.404664@(3, 2, 2) profile=2.753e-14@(3, 1, 6) monotonicity_excess=6.145e-01@(3, 2, 2)
RED-OK: C1b cap 1.404664 at (3, 2, 2) > 0.1 | C1b support monotonicity excess 6.145405e-01 at (3, 2, 2)
exit 1

$ python3 -O theory/checks/ansatz_scattering_2m_check.py --red-supportfold
A2M-C1a direct=3.354e-15 route=3.243e-15 ratio=5.605e-10
A2M-C1b agreement=1.128e-16 max_ratio=0.049383@(1, 1, 2) profile=1.646e-02@(2, 2, 2) monotonicity_excess=0.000e+00@(1, 1, 2)
RED-OK: C1b support-profile disagreement 1.646091e-02 at (2, 2, 2)
exit 1
```

The checker contains no bare `assert`; all green failures use explicit
`SystemExit(2)`, and each successfully detected registered mutation uses
`SystemExit(1)`.
