# Orchestrator patch — M-ESC versus NR

All three target files have complete patched copies in this lane directory.
Apply only the anchored deltas below; do not replace a concurrently changed
target wholesale.

## 1. Owning shard: `theory/lr-d16.md`

Anchor the unique block immediately after the paragraph ending
`The exhaustiveness/no-recoil upgrade is precisely K4 (CONJECTURE).`.

Replace the block beginning

`**⟨2⟩9. QED** (LR3 proved from (NR);`

and ending

`⟨2⟩6 in the exact \`LR-D16-EDW\` register). □`

with the block in the lane copy `lr-d16.md` beginning

`**⟨2⟩9 (THEOREM LRD-MESC-NR — cross-lane incompatibility).**`

and ending

`⟨2⟩6 in the exact \`LR-D16-EDW\` register). □`

This inserts the full Lamport proof and renames only that section's terminal
QED step from `⟨2⟩9` to `⟨2⟩10`.  No other text changes.

## 2. DAG rows: `claims/CLAIMS.md`

Insert the two complete rows `LR-D16-NR` and `M-ESC-NR` from the lane copy
`CLAIMS.md` immediately AFTER the row whose first cell is

`| LR-D16-EDW |`

and immediately BEFORE the row whose first cell is

`| M-IDX-density |`.

The insertion order is `LR-D16-NR`, then `M-ESC-NR`.  Keep both at `SKETCH`:
the first is the missing DAG transcription of the already written and
critic-rederived LRD-3 conditional; the second is a PROVED-candidate pure
composition pending orchestrator adjudication.  Do not promote either row as
part of this mechanical patch.

## 3. Non-owning shard citations: `theory/ace-ld.md`

The ACE shard must cite the owning theorem, not restate it.

First replacement: within `⟨1⟩5.⟨2⟩6(iv)`, replace the paragraph beginning

`(iv) *Cross-lane composition (recorded as such, r2 verdict §7 item 3;`

and ending

`and is not proved in this shard.`

with the shorter paragraph in the lane copy `ace-ld.md` beginning

`(iv) *Cross-lane citation; ownership is in LR-D16.*`

and ending

`realising (M-ESC) is exhibited in the corpus.`

Second replacement: within MP-6's blockquote, replace the bold passage
beginning

`> classes.  **Usable constraint (cross-lane composition — attributed`

and ending

`> antecedent constrains nothing until a witness exists.**`

with the blockquote passage in the lane copy `ace-ld.md` beginning

`> classes.  **Usable constraint:** cite THEOREM **LRD-MESC-NR** at`

and ending

`> exhibited in the corpus.`

No other ACE-LD proof or claim text changes.
