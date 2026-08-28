# Work order — S2 repair round 3 (codex #2 of 7)

You are the PROPOSER repairing Theorem AC-EX-2M after its round-3 critic
verdict.  The trajectory is **6 → 2 → 1 MAJOR, 0 FATAL throughout**.  A fourth
round should reach 0 MAJOR.  Get it there.

READ FIRST, in order:
1. `CLAUDE.md` (laws; **L6b Lamport is mandatory**; L10 honest verdicts)
2. `theory/verdicts/ansatz-scattering-2m-r3.md` **IN FULL** — your work order.
   Read §7 ("VERIFIED CORRECT — fenced, do not churn") FIRST and do not touch
   anything listed there.
3. `theory/verdicts/ansatz-scattering-2m-r2.md` and `-r1.md` (priors),
   `theory/ansatz-scattering-2m-r2-response.md` (your own r2 response format)
4. `claims/CLAIMS.md` — **the `AC-EX-2M` row now EXISTS at SKETCH**, merged by
   the orchestrator with the r3 critic's scoping sentence applied verbatim.
   **That row is now the register your shard must match.**  Lockstep is
   checked this round.
5. `theory/verdicts/soft-index-adjudication-r1.md` §3.1 (BINDING: the
   adjudicated D29 is lane B's) and its prepended ORCHESTRATOR ERRATUM.

## YOUR LANE (writable — nothing else)

- `theory/ansatz-scattering-2m.md`
- `theory/ansatz-scattering-2m-r3-response.md` (create)
- `theory/checks/ansatz_scattering_2m_check.py`

Do NOT edit `definitions.md`, `notation.md`, `claims/CLAIMS.md`, `HANDOFF.md`,
any other shard, or any verdict.  Do NOT git commit.

## THE ONE MAJOR — R3-O1

The Haag--Ruelle creator-independence port is **REAL** and the critic
confirmed every citation against the local TeX; the vector→operator gap of
R2-O1 is genuinely closed.  That is a real advance and you keep it.

The defect is its **antecedent**.  Interface clause 1 asserts D29's soft leg
is an asymptotic HR leg "not the fixed-time action of a charge operator on an
already prepared hard vector".  **Both D29 proposals on record say the
opposite** — `soft-index-b.md` §M1 (`Φ(0):=Q[f_ε]ψ_{g,σ}`, adopted as binding
by the adjudication §3.1) and `soft-index.md` §7.1 D29(2).  So `(ACE2M-LSZ)`
is currently a theorem about a soft leg the campaign has not adopted.

The r2 fix demand was a disjunction and you took branch (a) without checking
its antecedent.  Now do one of:

- **(i)** prove the `T→∞` D29-B readout of the *fixed-time* charge-created
  state has the same connected on-shell pairing as the HR asymptotic leg.
  This must be established **at `O(k_s)`**, because (R8)+(R19) give the exact
  mismatch `Q_{k_s}|k_h⟩−|B^{in}⟩ = −2ik_s|P_{12}⟩+O(k_s²)` there — precisely
  the soft law's own linear order.  The critic independently re-derived
  `S'_{12}(0)=2i` exactly.  Attempt this ONLY if you can close it cleanly.
- **(ii) — the expected and preferred outcome (rk-light law 5, downgrade over
  ambition):** take the r2 branch-(b) downgrade.  State plainly, in the
  theorem statement, in interface clause 1, and in HONEST STATUS, that under
  the adjudicated D29 the identification of the D29 datum with the constructed
  channel is **OPEN**, and that `(ACE2M-LSZ)` is a theorem about HR creator
  families, which the adjudicated D29 is not.
  **The DAG has already taken this branch**: the merged `AC-EX-2M` row says
  verbatim "**This theorem does NOT apply to the adjudicated D29.**"  If you
  choose (ii), your job is to bring the shard into exact lockstep with that
  sentence — no softer, no stronger.

Either way: `(A2M.3)`'s channel identification must not be readable as
available to Lane S1.

## THE SIX MINORS — all six get a response row

- **R3-O2 (fix in CODE).**  The profile-agreement gate is a **rescaled
  duplicate** of the agreement gate: the critic folded `w_Cw_D` into the
  constant in BOTH routes on a copy and every gate still passed, exit 0 — the
  measured ratios decay like `3^{−(w_C−1)−(w_D−1)}`, beating `w_Cw_D`.  So
  `--red-supportfold` detects a one-sided code edit, not mathematics.  Either
  build a gate that actually detects a two-sided support-length fold, or
  **delete §6's false sentence** calling it "the direct certificate that a
  support-length factor has not been hidden".  Do not leave a gate whose
  advertised meaning it does not have — this corpus has already shipped one
  no-op gate and it cost a headline.  (The monotonicity gate IS real and is
  killed by `--red-c1b`; keep it.)
- **R3-O3** quantifier mismatch: (D29-den) says "along the chosen tuple
  family", (A2M.3) says "for every sequence".  Make them agree.
- **R3-O4** register slip: "unconditional" is wrong for a statement resting
  entirely on an assumed bound; §8 already says "Under (D29-den)" correctly.
  Also clause 3 says both "assume" and "supplies" of the same inequality.
- **R3-O5** the source's isolated-mass-shell hypothesis is un-owned on D6 —
  the critic computed the magnon embedded in the two-magnon continuum at every
  `p∈(0,π)`.  Display the `S^z`-sector relativization **at the point of use**.
- **R3-O6** ⟨1⟩8.⟨2⟩1 proves (2M-1P) for the **unfiltered** charge and asserts
  the filtered family inherits it; add the source's filter-transparency
  condition.
- **R3-O7** (A2M.3)'s two halves concern different families; their join is
  interface clause 2, not a proof.  Say so.

Also address the eight NOTEs R3-N1…R3-N8 with a row each.

## OBLIGATIONS

- `ansatz-scattering-2m-r3-response.md`: one row per objection —
  FIXED / RETRACTED / DOWNGRADED / RESIDUE — with the exact edit location.
  No objection silently ignored.
- **LOCKSTEP against the merged CLAIMS row** is a first-class obligation this
  round; the r3 critic will check it.
- Checker: green exit 0 and every red exit 1 under `python3 -O`, mutation
  tested on COPIES in a temp dir, no bare `assert`.
- No reliance on REFUTED rows; no ML4-Ward (9) second display at `n≥2`; Bethe
  is oracle only.

Work fully autonomously.  Do not ask questions.  Do not stop at a plan.
