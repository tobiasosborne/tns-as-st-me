<!-- LANE BRIEF T1 (analytic): the decisive SYK/JT computation, tree level.
     bd tns-62n. TJO 2026-08-31: "I really want to understand the SYK/JT
     example: this would be a compelling motivating argument about the IR
     triangle for a single component system."
     YOUR LANE: theory/lanes/syk-jt/t1-analytic.md ONLY. Do not create or
     edit any other file. No bd operations, no CLAIMS/definitions edits,
     no LEDGER edits. Work fully autonomously; do not ask questions.
     Write INCREMENTALLY, section by section. -->

# T1: exact tree-level Schwarzian memory computation (T.1)–(T.3)

## Context (read first, in order)

1. `theory/lanes/reduction/o4-syk-jt-recon.md` — the recon memo. Your job
   is §5.2 of that memo, executed exactly: steps (T.1)–(T.3). Its citation
   line numbers have been re-verified against the local TeX below.
2. Local sources (titles pre-verified by orchestrator; re-verify, quote
   with file+line; NO network, NO other ids):
   - `refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex`
     (Maldacena–Stanford–Yang). The sourced Schwarzian equation
     C (Sch(t,u))'/t' = − t' T_tz is at lines 611–623. SL(2) charges at
     889–900, Hamiltonian 921–929, two-sided state 902–909, matter split
     957–964, bilocal dressing 662–675, quadratic action + zero modes
     680–719, invariant vertex B_12 at 729–753.
   - `refs/arxiv-2412.14799/Main.tex` (Bucca–Mezei, large-p SYK): needed
     only for the stiffness dictionary C ↔ Nα_S/(βJ) and the statement of
     where the tree-level computation embeds (Main.tex:291–311).
   - `refs/arxiv-1306.0622/shock.tex` (Shenker–Stanford): the shock shift
     (188–215), two-sided correlator (275–293), geodesic decay factor
     α e^{−R(t_L+t_R)/(2ℓ²)} at 223–234.
3. `definitions.md` D-numbers and `claims/CLAIMS.md` only as needed for
   campaign language (memory = permanent, stationary-subtracted,
   relational DC shift with an operational detector).

## The work order (execute, do not re-scope)

Tree-level classical Schwarzian response at large C, two-sided TFD.

**Step 1 — prepare and perturb.** Two Schwarzian boundaries in the
thermofield-double saddle at inverse temperature β. Apply a compactly
supported matter flux T_tz(u) on the RIGHT boundary during u ∈ [u_i, u_f].
Treat BOTH protocols: (a) a balanced source with zero net injected energy,
and (b) an unbalanced pulse compared against the equilibrium saddle at the
measured final energy E_f. The subtraction discipline is load-bearing: a
permanent temperature change must not masquerade as frame memory.

**Step 2 — solve (T.1) exactly.** Outside the source the SL(2) charges
(A.2) are constant, so the before/after solutions are thermal maps related
by definite Möbius data. Derive, in closed form, the map from the injected
charge increments ΔQ^a = ∫ du t' T_tz (1, t, t²) to the relative Möbius
element g_rel ∈ SL(2,ℝ) between the early and late frames. Fix the one
simultaneous two-sided SL(2) redundancy explicitly and state your gauge
choice; retain ONLY the relative transform between right and left clocks.

**Step 3 — the observable (T.2).** Insert the solution into the two-sided
invariant bilocal G_LR and compute
δG_LR(T) = G^pulse_LR(T,T) − G^eq_LR(T,T; E_f).
Extract Δu_rel(T) via δG_LR ≃ −Δu_rel ∂_T G^eq_LR where the linearization
is valid, but ALSO give the exact expression. The memory question is
whether Δu_rel(T) → nonzero constant as T − u_f → ∞. Derive the late-time
behavior analytically. Note the Shenker–Stanford geodesic decay factor
(shock.tex:223–234) — your result must either exhibit that decay, evade
it, or explain precisely why the two computations differ. Do NOT presume
the answer; the computation is decisive in both directions and a clean
NO-plateau is a fully successful outcome (it demotes the butterfly shift
to a transient relational time delay — state that surviving statement
sharply if so).

**Step 4 — the DC identity (T.3).** Fourier-transform the retarded
response before the late-time limit and test
Δu_rel =? lim_{ω→0} [−iω δu_rel(ω)] =? lim_{ω→0} S_Sch(ω; same source),
where S_Sch attaches the invariant vertex (C.3 of the recon; source lines
729–753) to the same hard insertion with the retarded Schwarzian
propagator. Normalization comes from (T.1) and the injected charge —
nothing fitted. State exactly which equality holds, in which limit, with
which error terms in 1/C and pulse width.

## Output spec

`theory/lanes/syk-jt/t1-analytic.md`, Lamport hierarchical style (L6b):
numbered steps ⟨1⟩1…, explicit ASSUME/PROVE per nontrivial step, every
leaf citing a file+line quote from the local TeX, a displayed prior
equation of your own shard, or a named elementary computation. Flag every
physics-level (non-rigorous) step with [physical argument]. End with:

1. **Verdict block**: plateau YES/NO (per protocol (a) and (b)); identity
   (T.3) HOLDS/FAILS/CONDITIONAL; the exact surviving statement in one
   sentence, suitable as a future CLAIMS row (but do NOT touch CLAIMS).
2. **Numeric handshake table**: 3–5 concrete parameter points
   (C, β, pulse profile, u_i, u_f, and your predicted Δu_rel and δG_LR(T)
   at 2–3 finite T values, to ≥6 significant figures where closed-form)
   so an independent numerical lane can check you. Choose simple pulse
   profiles (e.g. a narrow Gaussian or top-hat in T_tz) that a numerical
   ODE integrator can also use.
3. **Honesty ledger**: what is literature-known (with file+line), what is
   new, what remains open (the Diff charge algebra of corner A is out of
   scope here — say so).

Register: physics prose, cautious, no campaign acronyms load-bearing.
This lane creates NO claims and changes NO statuses.
