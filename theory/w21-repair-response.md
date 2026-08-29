<!-- ROLE: response record for the final W21 repair wave, bd tns-7pp. -->

# W21 final repair response

**Scope outcome.**  The seven-item order was applied only to the three target
shards, the NO-CAT-SOFT fence sentence, and the new categorical hybrid.  No
claim registry, definition, notation, verdict, W4/W5 artifact, or checker was
edited.

**Narrow readings used.**  “Promote” means that the reviewed status and merge
proposal in the relevant shard now say `PROVED`; all `claims/CLAIMS.md` edits
remain for the orchestrator.  “One categorical hybrid” means one canonical
selection statement named `A-INDEX-PEPS`, with `FUSION-SOFT` only as its
linear Fourier/window corollary; it is not a second selection row.  The W1
copy-ready cell was applied to the theorem carrier in the shard, not to D10 or
the claim registry.  Item 7 was treated as conditional on citing the legacy
donor checker in the merged record.

## Repair-order dispositions

| item | disposition | location |
|---:|---|---|
| 1 | **DONE.** Added the termwise cut-current norm bound, reserved zero-momentum language for the periodic directional sum, and installed the reviewed `S-IDX-fin-G` finite-lattice carrier without changing either Gram register. | `theory/soft-index-2d.md` §2.1 (2D.1a), §2.2, merge proposal 1 |
| 2 | **DONE.** Added endpoint-partition deformation invariance, both failure fences, and the `x=1` empty/identity-ribbon reading; only `A-INDEX-TC-fin` is marked `PROVED`, while `A-INDEX-PEPS` remains conditional. | `theory/anyon-label-index.md` status, §1.3, §7 proposal 1 |
| 3 | **DONE.** Added termwise conservation and the perimeter norm bound, restricted the current interpretation to the dephased first moment, stated that the finite ED is not an LR2/LR3 witness, marked `M-INDEX-2D-fin` `PROVED`, and retained `M-INDEX-2D-spec` at `SKETCH`. | `theory/memory-index-2d.md` ⟨1⟩4, ⟨1⟩11 (2D.8), §6 final paragraph, §7 MP-2, §8 |
| 4 | **DONE.** Created the sole categorical citation carrier from W2's canonical `(PT1)--(PT4)`, adding only W6's `T_x(k;w)`, linear Fourier/window consequence, SHAPE-FLAT, and the §6.3 dictionary once.  Both source shards remain lane records. | `theory/anyon-selection-hybrid.md` §§1--6 |
| 5 | **DONE.** Gave the selection theorem/corollary an ASSUME/PROVE ladder through typing, fusion decomposition, linearity, and topology, and gave SHAPE-FLAT its separate one-move, finite-composition, coherence, and holonomy-fence ladder. | `theory/anyon-selection-hybrid.md` §§3--4 |
| 6 | **DONE.** Added exactly the AMP-style relation-level witness fence; no full-model counterexample or promotion was added. | `theory/soft-2d-hunt.md` §3, immediately after the normalized-probe discussion |
| 7 | **NOT APPLICABLE.** The merged record does not cite the legacy `memory_index_check.py`, so no `np.trapezoid` compatibility edit was made. | — |

## Objection dispositions

| objection | disposition | location |
|---|---|---|
| `W1-O1` | **CLOSED.** The graph object is a displayed cut-current map with `C(Y,Phi)|partial_r S|` control; only (2D.3) is the directional zero-momentum flux. | `theory/soft-index-2d.md` §2.1 (2D.1)--(2D.3), §2.2 |
| `W2-O1` | **CLOSED.** Fixed-endpoint-partition deformations and even extra crossings preserve the shift; crossing the circle or changing the second circle is fenced, and `x=1` is the identity ribbon. | `theory/anyon-label-index.md` §1.3 |
| `W3-O1` | **HELD AT THE REQUIRED CEILING.** `M-INDEX-2D-spec` remains `SKETCH`; the shard now says no nonzero `(LR2_2D)--(LR3_2D)` model instance is known and the `9x9` ED is not one. | `theory/memory-index-2d.md` §6 final paragraph, §7 MP-2, §8 |
| `W3-O2` | **CLOSED.** The boundary-current paragraph now assumes a termwise charge-conserving decomposition, prints the perimeter bound, and does not identify individual TPM outcomes with current trajectories. | `theory/memory-index-2d.md` ⟨1⟩4, ⟨1⟩11 (2D.7)--(2D.8) |
| `W6-O1` | **CLOSED SUBJECT TO ORCHESTRATOR MECHANICAL VERIFICATION.** Both positive statements now have the demanded Lamport leaves, with no new theorem hypotheses. | `theory/anyon-selection-hybrid.md` §§3--4 |
| `W6-O2` | **CLOSED.** NO-CAT-SOFT is explicitly only a probe-family/relation-level witness, not an AMP-grade pair of microscopic models. | `theory/soft-2d-hunt.md` §3 |

## Verification record

All affected green commands exited `0`; every pre-existing registered red
command reached its mutation gate and exited `1`.  No mutation mode was added.

| carrier | green | registered red(s) |
|---|---:|---:|
| `soft_index_2d_check.py` | `0`, `SIDX2D-C0--C3` pass | `--red-scalar-full`: `1` at `SIDX2D-C2` |
| `anyon_label_check.py` | `0`, `ANYON-C0--C4` pass | `--red wrong-sector`: `1` at `ANYON-C4` |
| `memory_index_2d_check.py` | `0`, `M2D-C1--C4` pass | `--red fractional-charge`: `1` at `M2D-C2` |
| `soft_2d_hunt_check.py` | `0`, `S2DH-C0--C5` pass | `--red wrong-path`: `1` at `C2/C4`; `--red erase-probe-freedom`: `1` at `C3/C4/C5` |
| `cat_hunt_check.py` | `0`, `CATH-C0--C4` pass | `--red missing-ising-channel`: `1` at `CATH-C2` |

`git diff --check` passed.
