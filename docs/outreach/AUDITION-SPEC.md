# Audition spec — common constraints for all three outreach prototypes

Binding for every audition lane (Memory Lab tns-024, Butterfly Trial
tns-274, Proof Atlas tns-959). Read `docs/outreach/format-audit.md` — your
lane's Pick section is your design document; this file is the contract.

## What an audition is

A compelling VERTICAL SLICE of the experience, not the full product. It
must carry one complete why → how → what journey end to end at audition
quality; breadth can be cut, the arc cannot. Judged by: would a traditional
physicist (QM, GR, QFT≤QED, many-body QM/Fock space) forward this to three
colleagues?

## Truth constraint (TJO, verbatim; violations are FATAL)

"no oversimplifications are allowed: only true statements, no vague pop sci
bullshit. One is allowed to speak in generalities, and conjectures, but
everything must be mathematically correct."

Operationally:
- Simplification by RESTRICTION (an exactly stated special case) is
  allowed; simplification by DISTORTION is forbidden.
- Every displayed curve/number carries visible provenance, one of:
  **exact formula** (the closed form is displayed and is the one actually
  evaluated in JS, copied exactly from the PROVED source), **computed
  sample** (embedded verbatim from `numerics/results/*.json`), or
  **NOT COMPUTED** (region shown empty/hatched — never a persuasive
  interpolation across a scope boundary).
- Toy stages must be exactly solvable systems with their equations shown;
  a toy may teach the question, it may not carry the conclusion.
- Claim statements, scope fences, and NOT-claimed sentences are quoted or
  faithfully compressed from `claims/CLAIMS.md`; statuses shown honestly
  (PROVED with its scope, HOLD as HOLD).
- Any "verify" affordance in the audition shows the RECORDED test run
  (real test names, real green counts, file paths) and says it is a
  recorded run; it must not pretend to re-execute.
- No fake AI: if a lane mocks an AI component, it is labelled as a mock
  showing the component's answer contract.

## Register

Good simple communication, no arrogant tone, cautious scientific optimism
(docs/prose-guide.md register). The interface becomes LESS glossy at the
decisive moment: equations, values, residuals, and scope take the screen.

## Technical contract (Claude-artifact-compatible single file)

- ONE self-contained HTML file in `docs/outreach/auditions/`
  (`memory-lab.html`, `butterfly-trial.html`, `proof-atlas.html`).
- Artifact conventions: NO doctype/html/head/body wrapper tags; the file
  begins with `<title>` and a `<style>` block, then content. It must also
  render fine opened directly in a browser.
- Theme-aware: complete light palette as CSS custom properties on bare
  `:root`; dark overrides under `@media (prefers-color-scheme: dark)`
  guarded `:root:not([data-theme="light"])` AND under
  `:root[data-theme="dark"]`; explicit token background on the page
  container. No color defined only inside a media/theme block.
- No horizontal page scroll; wide content scrolls inside its own
  `overflow-x:auto` container. Responsive (relative units, flex/grid).
- External resources: NONE preferred (vanilla JS + inline SVG). If a
  library is truly needed, scripts only, pinned versions, only from
  cdnjs.cloudflare.com or cdn.jsdelivr.net/npm/. No external stylesheets
  except Google Fonts (with real fallback stacks). For mathematics use
  MathJax 3 from cdnjs configured for SVG output (needs no external CSS),
  or hand-set HTML/SVG math. KaTeX is NOT usable (its CSS would be
  blocked).
- Embed all data inline (JSON in a `<script type="application/json">`
  block), with a comment naming the source file and git commit.
- localStorage only for per-viewer conveniences, always in try/catch.
- Keep total file size well under 5 MB.

## Provenance the lanes draw from (ground truth, quote don't paraphrase)

- `claims/CLAIMS.md` rows JT-B-susc, JT-bfly-decay, JT-noplat-abs
  (lines ~109–111) — statuses, scope sentences verbatim.
- `definitions.md` D32 (memory, absolute) and D33 (calibrated relational
  memory susceptibility).
- `theory/lanes/syk-jt/t1-analytic.md` — the closed forms (Δu_rel balanced
  formula, δG_LR decay law ⟨1⟩3 (3.2)–(3.9), butterfly law ⟨1⟩3 (3.15)).
- `theory/lanes/syk-jt/observables-spec.md` — allowed algebra, iterated
  limit convention (C→∞ first; 1 ≪ κT ≪ κC).
- `numerics/results/schwarzian_memory.json` — 8 computed parameter points,
  late-time grids, integrator diagnostics, limit-convention metadata.
- `theory/verdicts/syk-jt-joint-critic-r1.md`, `-r2.md`, repair responses —
  the real adversarial history.
- `numerics/test/test_schwarzian_memory.jl` — real test names/counts for
  the recorded-verify affordance.

## Process

Builder (Opus) loads the `artifact-design` skill and the `dataviz` skill
BEFORE writing HTML; reads its Pick section + this spec + the provenance
files; builds the slice; self-QAs (open the file's logic mentally, check
every provenance tag, check both themes). Critic (codex) then reviews per
its brief: constructive, ranked, actionable — the goal is to IMPROVE the
audition, not kill it. One repair round by the same builder. Orchestrator
publishes.
