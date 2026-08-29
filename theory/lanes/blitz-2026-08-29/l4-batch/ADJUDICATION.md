# L4 batch adjudication

## ⟨1⟩1. The two magnon-band-map spellings remain distinct

**ASSUME.** D28(1)--(4), D31(1)--(4), and the current live use sites.

**PROVE.** Retain the registered `Γ_M` / `Γ_{M,γ}` distinction; no rename is
needed.

**⟨2⟩1.** `Γ_{M,γ}` is a member of a tail-indexed family: its codomain is the
vacuum GNS space `H_γ`, `γ∈{α,β}`, and it is paired with the tail dispersion
`ω_γ` inside the kink--magnon construction.

*Justification.* D28(1), D28(3).

**⟨2⟩2.** `Γ_M` is the one-vacuum charge-one map in `H_A` for a scalar band
with fixed multiplicity.  D31 assumes neither a kink Hilbert space nor a
left/right tail family.

*Justification.* D31(1)--(3).

**⟨2⟩3.** Every active occurrence respects those registers: bare `Γ_M` occurs
only in D31, its notation/claim records, and `ansatz-scattering-2m.md`; indexed
`Γ_{M,γ}` occurs only in D28, its notation record, and the D28 kink--magnon
shards.  Review/brief occurrences merely quote their corresponding register.

*Justification.* Named computation `gamma_use_audit.py`; saved run in
`verification.log`.

**⟨2⟩4.** Therefore no proof step reads one map as the other.  The explicit
subscript rule is mechanically decisive (`γ` present means D28; absent means
D31), so retaining the current registered distinction is lower-risk than
renaming the converged D31 proof surface.

*Justification.* ⟨2⟩1--⟨2⟩3 and `notation.md` rows `Γ_K, Γ_{M,γ}` / `Γ_M`.

**⟨2⟩5. QED.**

## ⟨1⟩2. The free two-packet channel is fixed in the shard, not D31

**ASSUME.** D31 and `ansatz-scattering-2m.md` ⟨1⟩1.

**PROVE.** Point the notation row for `ℋ_{0,12}`, `H_{0,12}`, `𝒟_{12}` at
the shard alone; do not add an introducing clause to D31.

**⟨2⟩1.** D31 fixes the one-particle band, packet windows, creators, velocity
separation, and spectral inventory, but it does not define the tensor-product
channel, its sum Hamiltonian, or its smooth product core.

*Justification.* D31(1)--(5).

**⟨2⟩2.** The three symbols are explicitly introduced together immediately
after the theorem assumptions and are then consumed by (A2M.1)--(A2M.2).

*Justification.* `ansatz-scattering-2m.md` ⟨1⟩1 and claim AC-EX-2M.

**⟨2⟩3.** Moving that construction into D31 would turn theorem-local derived
notation into hypothesis text and would contradict D31's present merge note
that no clause was edited.  A shard-only first-fix pointer is exact and leaves
D31's inferential content unchanged.

*Justification.* D31 header/scaffolding and ⟨2⟩1--⟨2⟩2.

**⟨2⟩4. QED.**

## ⟨1⟩3. ML2 notation, checker residue, and L2 ruling

**ASSUME.** Theorem ML2, its checker, and repository laws L1, L2, and L4.

**PROVE.** Apply the n6 spelling repair and notation repairs, while recording
a deliberate L2 exception for the converged ML2 shard.

**⟨2⟩1.** The n6 edit exposes the two D7 plane-wave slots as
`k_1x+k_2y` and `k_2x+k_1y` before imposing `k_1=k_2`; it changes no value.
The patched checker passes normally and under `python3 -O`, with output
identical to HEAD.

*Justification.* D7's ordered two-plane-wave convention;
`ml2-completeness.md` ⟨1⟩4.⟨2⟩1; named computation
`ml2_completeness_check.patched.py`; saved run in `verification.log`.

**⟨2⟩2.** `X=cos q` is used through ⟨1⟩4, not only ⟨1⟩3, because the
coincident/degenerate-root analysis evaluates the polynomial at `X=±1`.

*Justification.* `ml2-completeness.md` ⟨1⟩3.⟨2⟩1 and
⟨1⟩4.⟨2⟩1.⟨3⟩2.

**⟨2⟩3.** `{\cal U}_c` is a live, globally named unitary transform and is already
explicitly disambiguated from D3's `U[f]` and D2's `𝒰(g)` in its defining
step; it therefore needs a notation row whose first-fix pointer is equation
(15).

*Justification.* `ml2-completeness.md` ⟨1⟩5.⟨2⟩1 and (15); D2, D3.

**⟨2⟩4.** Keep the converged ML2 proof unified as a deliberate L2 exception.
The finite-ring classification, infinite-chain Jacobi resolution, and soft
consequence are the three conclusions of one theorem, share the recurrence
and equation sequence, and terminate in one QED; a post-convergence split
would invalidate audited step/equation anchors without isolating a new claim.
Further ML2 work must go in a new shard.

*Justification.* CLAUDE.md L2; claim ML2; `ml2-completeness.md` ⟨1⟩1 and
⟨1⟩7; verdicts `ml2-r1.md` and `ml2-r2.md`.

**⟨2⟩5. QED.**

## ⟨1⟩4. Pipe escaping is purely structural

**ASSUME.** A notation table has three fields and a CLAIMS table has six,
with delimiters matched by `(?<!\\)\|`.

**PROVE.** Escape only the literal pipes inside code spans in the six named
rows.

**⟨2⟩1.** HEAD has exactly one malformed notation row and five malformed
CLAIMS rows; each gains one extra field per unescaped literal pipe.

*Justification.* Named computation `table_row_field_check.py`; HEAD run in
`verification.log`.

**⟨2⟩2.** The patched copies have the required field counts on every table
row, and an in-memory mutation that removes one escape from `S2-2body-S`
makes the checker fail.

*Justification.* Named computation `table_row_field_check.py`; green and red
runs in `verification.log`.

**⟨2⟩3.** Since the patch inserts backslashes only, the mathematical text and
all claim statuses remain byte-for-byte unchanged otherwise.

*Justification.* `PATCH.md` anchors and the lane-local patched-copy diffs.

**⟨2⟩4. QED.**
