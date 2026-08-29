# Work order — S-IDX-fin for general compact on-site symmetry (bd tns-fea)

TJO directive: the finite-volume soft index identity currently stated for
SU(2) rings (theory/soft-index-r2.md ⟨1⟩3, S-IDX-fin) should hold for
GENERAL compact on-site symmetry groups. Your job: prove the general
theorem, or exhibit the precise obstruction. This is exploration+proving;
the SU(2) shard is under separate review — treat it as input, do not edit
it, and do not assume its critic passes.

## Process contract (PRD.md — read first)

- ONE critic round + ONE repair follow IF you deliver a positive theorem.
- If you find an OBSTRUCTION: per PRD's negative-results rule it gets NO
  rounds — state it sharply in your shard header with the surviving
  weaker statement (which roots/groups DO work), and stop there.
- Label every step honestly; a wrong label is the only fatal sin.

## READ FIRST

1. `PRD.md`, `CLAUDE.md`, `notation.md`, `definitions.md`.
2. `theory/soft-index-r2.md` §2 (S-IDX-fin, ⟨1⟩3–⟨1⟩5) — the SU(2)
   theorem you are generalizing; understand exactly which su(2) facts
   each step consumes.
3. Corner A general-group machinery: `theory/corner-a.md`,
   `theory/corner-a-goldstone.md` + their CLAIMS rows — charges on the
   center of the unbroken subgroup, Weyl-wall structure. This is the
   campaign's existing general-G language; REUSE its registers and cite
   its rows rather than rebuilding.
4. `claims/CLAIMS.md` rows ML4-Ward (incl. ERRATUM — the register trap
   generalizes: check whether YOUR general identity has the analogous
   full-sector vs highest-weight distinction, and name both registers).

## THE TASK

Setting: finite periodic ring, on-site action of a compact connected Lie
group `G` (finite-dimensional unitary on-site rep), `G`-invariant
finite-range Hamiltonian. Symmetry broken to a closed subgroup `H` on the
relevant sector/vacuum structure (state your breaking hypothesis
explicitly and minimally — do not import more than the proof needs).

1. **Root-wise reduction.** Each broken root `α` gives an sl₂ triple
   `(E_α, F_α, H_α)` in the zero-mode algebra. Determine: does the SU(2)
   S-IDX-fin identity apply verbatim to each such triple on the
   `H_α`-weight sectors? Where does the argument consume MORE than the
   sl₂ triple (e.g. the full weight-sector decomposition, absence of
   multiplicity mixing)?
2. **Multiplicity spaces.** The unbroken `H` acts on the multiplicity
   spaces of the sl₂_α decomposition. Show the identity is block-diagonal
   over this action, or exhibit the mixing obstruction. This is where the
   theorem lives or dies — spend your effort here.
3. **Rank >1 phenomena.** Non-orthogonal roots, Weyl-group action
   relating the per-root identities, and whether the identities for
   different α are independent constraints or one orbit. Connect to
   corner A's Weyl-wall picture if the connection is real; do not force
   an analogy.
4. **Register discipline.** State the general identity in BOTH registers
   (full-sector with the operator `A` uninverted-scalar-free, and
   highest-weight-restricted with its projector), exactly as the SU(2)
   ERRATUM requires. The hybrid form was refuted at SU(2); assume the
   trap generalizes until proven otherwise.
5. **Sanity instances.** Check your general statement reduces exactly to
   S-IDX-fin at `G=SU(2)`, and work one genuinely new instance (SU(3) or
   SU(2)×U(1)) concretely enough that a checker can compute it.

## LANE (writable; NOTHING else)

- `theory/soft-index-g.md` (CREATE — Lamport L6b shard)
- `theory/checks/soft_index_g_check.py` (CREATE — green exit 0 under
  `python3 -O`, no bare asserts; must include a small-N exact
  diagonalization of the general identity on your new instance (SU(3) or
  SU(2)×U(1)) with at least one red mode mutating the identity's
  structure; must ALSO verify the G=SU(2) reduction against the numbers
  soft_index_r2_check.py certifies)
- `theory/soft-index-g-notes.md` (CREATE, optional)

Do NOT edit theory/soft-index-r2.md, claims/CLAIMS.md, definitions.md,
notation.md, or any existing file. Proposed rows go in a MERGE PROPOSALS
section. No commits.

## Deliverable shape

(0) status header: THEOREM (general G) / THEOREM (restricted class,
named) / OBSTRUCTION — stated in the first ten lines with the exact class
covered; (1) setup, citing corner-A registers; (2) the ladder; (3) the
SU(2) reduction check; (4) the new instance; (5) checker section; (6)
MERGE PROPOSALS. Write each section as you complete it.
