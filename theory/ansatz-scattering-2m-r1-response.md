<!-- ROLE: disposition of theory/verdicts/ansatz-scattering-2m-r1.md. -->

# AC-EX-2M r1 repair response

Verdict addressed: `theory/verdicts/ansatz-scattering-2m-r1.md`.
Repaired shard: `theory/ansatz-scattering-2m.md` (self-status remains
**SKETCH**).  Every objection is accepted; no rebuttal computation is needed.

| ID | Disposition | What changed | Shard location |
|---|---|---|---|
| O1 | ACCEPTED | The fixed-packet fence now includes packet Schwartz seminorms, displays `||∂^jf_ε||_∞=ε^{-j-1/2}||f^{(j)}||_∞` and the relative `ε^{-N}` integration-by-parts growth, and records the favourable D6 soft-limit behaviour of `ε_v,d_B,η_inel`. | ⟨1⟩2.⟨2⟩1, ⟨1⟩2.⟨2⟩3, ⟨1⟩5.⟨2⟩4 |
| O2 | ACCEPTED | Clause 5 is split into comparison convention (5a) and named hypothesis `(ACE2M-LSZ)` (5b); the D6 identity `Q[f]Ω=Σ_x f̂(x)|x⟩=a_2[f]Ω` proves it with zero remainder, while abstract D31 leaves it unproved.  The status now says wave operators enter (A2M.3) only through LSZ. | ⟨1⟩8(5a--5b), ⟨1⟩8.⟨2⟩1, ⟨1⟩9.⟨2⟩2, §8 HONEST STATUS |
| O3 | ACCEPTED | `(SR)` is posed after `N→∞,t→±∞` only; `j` explicitly labels `(W_j,σ_j)`, `A_j(0)` is a required continuous extension, the outer display uses `lim_ℓ` along an exhaustion subsequence, and the text concedes genuine `j`-uniform soft regularity. | ⟨1⟩8 `(ACE2M-SR)`, ⟨1⟩9.⟨2⟩3 |
| O4 | ACCEPTED | The D6 claim is downgraded to the `j`-independent infinite-chain amplitude.  The full `(W,σ)`-uniform hypothesis is explicitly open on every model, including D6, and the theorem/status reflect that limited nonvacuity. | ⟨1⟩1(A2M.3), ⟨1⟩9.⟨2⟩4--⟨2⟩5, §8 HONEST STATUS |
| O5 | ACCEPTED | The unproved compatible-union/entire-summand claim is deleted.  Only each fixed packet range is identified with the matching closed ML2 scattering subspace; range exhaustion and completeness remain open. | ⟨1⟩1(A2M.2), ⟨1⟩7.⟨2⟩4, claims-row proposal, §8 |
| O6 | ACCEPTED | A2M-C1 is scoped to the fixed-point-subtracted connected two-point identity on AKLT.  A support-length gate for `w_C,w_D∈{1,2,3}` and its own red mutation were added; Jordan-safe decay is explicitly uncertified; all gates require `raise`/`sys.exit`, including under `python3 -O`. | §6 CHECKER SPEC, A2M-C1a--C1b and Uncertified scope |
| O7 | ACCEPTED | The four-fold Gram errors are corrected to `O(|t|^{4-N})` and `O(|t|^4⟨ε_v|t|/2⟩^{-N})`. | ⟨1⟩6.⟨2⟩2 |
| O8 | ACCEPTED | The condition-number gloss is replaced by the block Stinespring isometry `V_w`; the trace-norm contraction has constant one and `C_{A,λ̃}` absorbs finite-dimensional norm equivalence. | ⟨1⟩3.⟨2⟩2 |
| O9 | ACCEPTED | The irrelevant kink-class dependency D17 is removed; the campaign limit-order clause is cited instead. | ⟨1⟩2.⟨2⟩1 |
| O10 | ACCEPTED | D2(a) is removed from proposed D31 and the proposed claims-row dependencies. | §7 D31 opening; AC-EX-2M claims-row proposal |
| O11 | ACCEPTED | The proposed claims row now says D1 derives C2 and D31(3) almost locality supplies C4, and restores “D31-listed” for bound bands. | §7 AC-EX-2M claims-row proposal |
| O12 | ACCEPTED | The Cook identity now cites D31(3)'s compact energy--momentum transfer to put the two-creator vector in `Dom H`. | ⟨1⟩5.⟨2⟩1 |
| O13 | ACCEPTED | The exact-match leaf states `|S(K,q)|=1` from ML2 (18) with real `c`. | ⟨1⟩7.⟨2⟩3 |
| O14 | ACCEPTED | The false “ε never enters” sentence is replaced by: no `ε→0` limit occurs inside Cook; `ε` is a fixed packet parameter and its constants diverge. | ⟨1⟩1(A2M.1), ⟨1⟩9.⟨2⟩3 |
| O15 | ACCEPTED | Proposed D31(3) now displays `a_{i,b}(n)=τ_n(a_{i,b}(0))`. | §7 D31(3) proposal |
| N1 | ACCEPTED | The selected band is expressly isolated only within the charge-one sector, both in D31 and in the source-hypothesis audit. | ⟨1⟩10.⟨2⟩1; §7 D31(2) proposal |
| N2 | ACCEPTED | The favourable D6 limits `ε_v→|v_h|`, `d_B→J sin²(k_h/2)`, `η_inel=+∞` and the unused degeneration of `ε_0` are stated. | ⟨1⟩2.⟨2⟩3 |
| N3 | ACCEPTED | The forward reference to ⟨1⟩7 is marked non-circular and the independent dependency chain is named. | ⟨1⟩2.⟨2⟩2 |
| N4 | ACCEPTED | D31 now specifies a scalar band times a fixed multiplicity space; matrix-valued crossings are outside scope, so `V_i=ω'(K_i)` is defined. | §7 D31(2)--(4) proposal |
| N5 | ACCEPTED | HONEST STATUS now distinguishes the assumed spectral gap `d_B>0` from the derived D31-listed bound-band exclusion. | §8 Assumed |
| N6 | ACCEPTED | The surviving port audit is preserved.  The one missing creator-independence clause is explicitly not ported because the repaired theorem makes only a fixed-pair claim. | ⟨1⟩7.⟨2⟩4; ⟨1⟩10 reference audit |
| N7 | ACCEPTED | No frozen soft-index checker semantics or files were changed; A2M-C1 remains a separate specification. | §6 CHECKER SPEC |
| N8 | ACCEPTED | No refuted claim is used; the proposed dependency row is further narrowed by deleting unused D2(a), and all repaired soft/completeness fences remain explicit. | §7 claims-row proposal; §8 HONEST STATUS |

## Rebuttal computations

None.  O1--O15 and N1--N8 were all accepted and repaired at or below the
verdict's surviving-statement ceiling.
