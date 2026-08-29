# Work order — SPECULATIVE HUNT 2: DH/Heckman in the SEMICLASSICAL soft regime (TJO 2026-08-29)

Successor to theory/dh-hunt.md, which is STANDING for the question it
answered: DH supplies no exact finite-N integrality — the support of the
memory/soft laws on ℤ is superselection, full stop. Do not re-litigate
that; its six verdicts are fences.

TJO's physics objection reframes the question: low-momentum scattering is
a semiclassical regime, and fluctuations should matter there. The spine
splits the law into support (symmetry, exact, done) and WEIGHTS
(dynamics). The first hunt never tested DH against the weights. Your
question: **does a DH/Heckman-type semiclassical statement control the
low-k / large-S envelope of the escaped-charge weights p_ν (and/or the
soft-phase datum), with fluctuations as subleading corrections?**

The seed is in the first hunt's own killing computation: the two-spin
atomic law ¼/½/¼ vs the projective DH spline (3/2)(1−|x|)² are related by
**Heckman's theorem** — rescaled weight measures converge to the DH
pushforward in the large-representation limit. Asymptotically the two
object types DO meet.

## FALSIFIABLE TARGET (what makes this non-artificial)

Predict a continuous envelope for measured atomic data no current row
computes, and TEST it in this session against frozen data:
- numerics/results/spin1-bc-falsifier.json + spin-s memory rows (measured
  escaped-charge / memory data across S ∈ {1/2,1,3/2,2});
- theory/checks/memory_index_probe.py and soft_index_probe.py frozen
  outputs (quote probe as P1+P2(a)-only);
- small-N ED you run yourself for a clean large-S sequence.
A RESULT = a derived envelope law (Heckman/DH measure of a named moment
map, or a collective-coordinate phase-space computation) matching the
data with a stated error model and a red-capable check. A PROGRAM = the
derivation with the first data comparison done. NOTHING = every route
either needs the answer as input or fails the data — say so sharply.

## CANDIDATE ROUTES (kill freely)

1. **Heckman route.** The escaped-charge datum decomposes over weight
   sectors; identify the representation-theoretic family whose large
   parameter (window size, S, magnon number) drives a Heckman limit, and
   compute the limiting DH measure. Check: does it reproduce the measured
   p_ν envelope, and do the fluctuation corrections have the right
   1/S (or 1/N_W) size?
2. **Collective-coordinate route.** Semiclassical kink: position/charge
   zero modes span a reduced phase space; the low-k soft leg couples to
   it. Compute the classical outcome distribution (Liouville measure on
   the reduced space pushed through the protocol observable) + Gaussian
   fluctuations. Landau–Lifshitz limit of H_S at S→∞ is the natural
   arena; the PROVED 1/S slope must emerge as the leading semiclassical
   phase.
3. **[Q,R]-commutation flavor.** If quantization (the exact atomic law)
   and reduction (the DH measure) commute asymptotically in this setting,
   state the precise commutation result being used and what it buys
   beyond routes 1–2; if nothing, drop it.

## FENCES

- theory/dh-hunt.md verdicts stand (no exact-integrality claims, no
  wall-crossing-as-dichotomy, no ABBV soft coefficient).
- The exact quantized support is NEVER derived semiclassically; your
  envelope statements are about weights/envelopes only.
- Value claims respect the AMP obstruction and S2-2body-S as the only
  slope source at finite S.
- L3 quoting from refs/ only. Honest labels; SPECULATIVE marked.

## LANE (writable; NOTHING else)

- theory/dh-semiclassical.md (CREATE)
- theory/checks/dh_semiclassical_check.py (CREATE only for RESULT or a
  PROGRAM's first comparison: green exit 0 under python3 -O, no bare
  asserts, ≥1 red mode; the data comparison itself must be a gate)
- theory/dh-semiclassical-notes.md (CREATE, optional)

No edits to existing files. MERGE PROPOSALS only for RESULT. No commits.

## Deliverable shape

(0) header: RESULT / PROGRAM / NOTHING NON-ARTIFICIAL + where it lands
(likely companion paper or §7 discussion clause; the Letter is full);
(1) route ledger with verdicts; (2) the best route worked to a data
comparison; (3) checker section if warranted; (4) MERGE PROPOSALS if
warranted. Write sections as you complete them.
