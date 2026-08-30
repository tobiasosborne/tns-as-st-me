<!-- LANE BRIEF O4: SYK/JT reconnaissance — the one-species PURE-GRAVITY
     triangle. TJO 2026-08-30: pure gravity is NOT excluded from the
     one-species map; lattice versions appreciated (JT suggested); "we could
     take a quick look at SYK models". This is RECONNAISSANCE: a physics
     memo, no CLAIMS rows, no status machinery. Honesty rules apply.
     Output: theory/lanes/reduction/o4-syk-jt-recon.md, INCREMENTALLY. -->

# O4: does SYK/JT carry the one-species infrared triangle, and what is the dictionary to the campaign?

## Sources (ALL LOCAL, titles pre-verified by orchestrator — re-verify, then
quote with file+line; NO network access, NO other ids)

- refs/arxiv-1606.01857 (GravityReparametrizationsRevised.tex):
  Maldacena–Stanford–Yang — nearly-AdS2, Diff breaking, Schwarzian.
- refs/arxiv-2412.14799: nonlinear soft-mode action for large-p SYK.
- refs/arxiv-1306.0622: Shenker–Stanford, black holes and the butterfly
  effect (the shockwave frame shift).
- Campaign context: HANDOFF_MPS_SOFT_THEOREM.md §0–§2 (the triangle
  blueprint); docs/reduction-limits.md (skim); the operational directive
  (theory/lanes/reduction/BRIEF-o1-operational-audit.md header quotes it);
  bd memory notes are not accessible to you — the directive is: only
  observable/implementable quantities are operationally meaningful.

## The question

The campaign's triangle blueprint is: (A) asymptotic symmetry = broken
symmetry acting at the boundary, quotient by trivially-acting, charge
algebra + extension; (C) soft theorem = universal symmetry-forced structure
of amplitudes/correlators as a soft mode goes soft; (B) memory = permanent,
DC shift left in a reference degree of freedom after an event, tied to (C)
by a Fourier/zero-mode relation. Map this onto SYK/JT, corner by corner,
with equations quoted from the three sources:

1. **Corner A.** Time-reparametrization symmetry Diff(S¹) broken to
   SL(2,ℝ); the Schwarzian mode as the (pseudo-)Goldstone; the boundary
   charges. Quote the breaking pattern and the Schwarzian action from
   1606.01857. Note the contrast with the campaign's 1D chain: there the
   celestial sphere S⁰ makes the asymptotic group finite-dimensional; in
   JT the asymptotic direction is TIME and the group is
   infinite-dimensional even in low dimension — state this cleanly.
2. **Corner C.** The soft-mode dominance of IR correlators: the enhanced
   Schwarzian contributions as a UNIVERSAL soft factor dressing all
   correlators — is this structurally a soft theorem (universal,
   symmetry-forced, state-independent within a class)? Use 2412.14799's
   nonlinear soft-mode action and 1606.01857's four-point structure.
   State what plays the role of the Adler zero / pole and what plays the
   role of the hard legs.
3. **Corner B.** The memory candidate: a matter pulse permanently shifts
   the boundary time frame / horizon (the Shenker–Stanford shockwave
   shift). Argue at physics level whether the butterfly-effect frame
   shift is a genuine memory effect in the campaign's sense (permanent,
   DC, valued in the broken-symmetry orbit — a reparametrization-frame
   shift IS a Goldstone-manifold displacement). What is the detector?
   (Two-sided correlators / a second boundary — note the resonance with
   "memory needs a probe".) Is the Fourier/zero-mode link to corner C
   visible in the known formulas?
4. **The microscopic dictionary.** SYK : JT :: spin chain : lattice
   triangle. Map: microscopic model (Majoranas with random couplings vs
   spins), emergent soft mode (reparametrizations vs magnons), broken
   symmetry (Diff(S¹)/SL(2,R) vs internal G), memory carrier (frame shift
   vs kink displacement), operational split (microscopic fermion
   correlators = observable; the collective reparametrization coordinate =
   gauge-like scaffolding — the exact analogue of the campaign's proved
   non-identifiability of the ansatz gauge datum). Also the honest
   disanalogies: 0+1d (no spatial infinity — asymptotics in time),
   pseudo-Goldstone (explicit breaking at finite coupling — the soft
   theorem is approximate with computable corrections), disorder average
   (what is operational in a single realization vs the ensemble?).
5. **What would be genuinely new.** Per corner: what the literature
   already has (soft mode action, chaos bound, Schwarzian dominance) vs
   what assembling the TRIANGLE would add (to our knowledge: the memory
   framing of the shockwave shift and the A/C/B Ward-identity assembly are
   not packaged as an infrared triangle anywhere — assess honestly, and
   say what a first falsifiable computation would be, e.g. a permanent
   two-point-function phase shift after a pulse computed exactly in
   large-p SYK or the Schwarzian theory, with its DC/soft-mode identity).
6. **Verdict:** three lines — is there a one-species pure-gravity triangle
   here; what is the cheapest decisive computation; does anything threaten
   or strengthen the campaign's framing (the "opportunity" reading).

## Rules

Physics register; [physical argument] flags; quotes only from the three
local sources with file+line; this memo creates NO claims and changes NO
statuses; no bd operations; no LEDGER edits; edits only in
theory/lanes/reduction/.
