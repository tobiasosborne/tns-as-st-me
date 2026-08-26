<!-- ROLE: L6 adversarial critic verdict on paper v2.  Critic: Codex.
     Date: 2026-08-26.  Audited paper snapshot: 83b219b. -->

# Paper v2 critic verdict r1

I audited `paper/main.tex`, all three figures and their generator, `refs.bib`,
`paper/v2-claim-audit.md`, the claim DAG, and the relevant proof shards at the
requested paper snapshot `83b219b`.  The checkout advanced concurrently to
`e237a4e`, which later promotes `S2-2body-S`; that later status is not applied
retroactively to v2 or to its self-audit.  The objections below therefore state
the licensing position of the requested snapshot.

## Numbered objections

### 1. FATAL — the abstract claims that the whole triangle is proved

**Location.** Abstract, `main.tex:34-42`: “The infrared triangle ... is
formulated and proved” and “A soft magnon decouples with a universal phase
slope.”  The self-audit maps the first sentence to a list of individually
PROVED rows at `v2-claim-audit.md:22`.

**Licensing rows.** `S-general` is CONJECTURE; the three edges are respectively
CONJECTURE, SKETCH, and SKETCH; `M-quant-G` is only a conditional implication;
`SPT-M'-dyn` is CONJECTURE.  `S2-2body` proves only the spin-1/2 two-body soft
statement.

**Independent check.** A conjunction of proved corner results does not promote
the unproved edges or the general soft theorem.  The abstract also omits the
two-body scope of the phase slope.  The self-audit's row aggregation is
therefore not a valid license.

**Fix demand.** Replace the blanket theorem claim by a scoped inventory:
proved endpoint identities, a spin-1/2 two-body soft theorem, and a memory law
conditional on H-AD-G; call the remaining triangle relations conjectural.

### 2. FATAL — “numerics verify each claim” is false

**Location.** Abstract, `main.tex:41-42`: “Bethe and matrix-product numerics
verify each claim”; self-audit `v2-claim-audit.md:28`.

**Licensing rows.** `OR1`, `OR2` are PROVED oracle comparisons; `N2` is SKETCH;
`Mq-E`, full-chain D18/H-AD-G, `S-general`, `SPT-M'-dyn`, and the
`|q_hard|>1` part of `Bc` remain unproved or untested.

**Independent check.** The checkers certify selected algebraic identities and
finite computations.  They do not construct the general wave operators,
prove full-chain sector reduction, test the charge-2 leg, or verify every
conjecture.  Mapping `OR1/OR2/N2` to “each claim” silently changes scope.

**Fix demand.** Name only the Bethe coefficients and the selected finite
wavepacket/transfer calculations that were actually checked.

### 3. FATAL — the opening silently drops H-AD-G and declares unproved edges closed

**Location.** Opening summary, `main.tex:52-59`: “a magnon that crosses a
domain wall displaces it by a quantized charge step” and “the lattice triangle
closes through charge transport”; repeated at `main.tex:300-304`.  The
self-audit explicitly excuses the first omission because the condition appears
later, at `v2-claim-audit.md:36`, and maps the closure language at lines 38 and
108-109.

**Licensing rows.** `M-quant-G` is PROVED only as H-MQG(1--4) + H-AD-G implies
(G.1)--(G.2).  The active edge ledger says A=>C CONJECTURE, C=>B SKETCH, and
B=>A SKETCH.  `M-flux` and conditional `M-quant` do not promote those edges.

**Independent check.** The sentence asserting displacement contains no
scattering hypothesis, and a condition in Theorem 2 cannot license an earlier
unqualified sentence under L9.  Likewise, refuting literal Conjecture M does
not prove that the whole triangle “closes.”

**Fix demand.** Put “for packets satisfying H-AD-G” in the opening sentence and
replace “closes” by a statement limited to the proved current-flux and charge-
bookkeeping relations.

### 4. FATAL — finite broken strings are not “locally a vacuum”

**Location.** Corner A, `main.tex:116-120`: “for every finite region the state
is locally a vacuum”; self-audit `v2-claim-audit.md:65`.

**Licensing row.** `A2(a)` says a finite truncation remains in
`K_{alpha,alpha}` and is normal in the vacuum folium.  Its exact tensor is
`A_beta` inside the interval with a kink and antikink at the two ends.

**Independent check.** `corner-a-kinks.md` Theorem A2(a), lines 115-119,
explicitly gives a locally detectable finite decoration.  Same-sector or
vacuum-folium membership is not equality with a vacuum on local algebras.  The
self-audit replaces the proved sector statement by a false local statement.

**Fix demand.** Say “every finite truncation remains in the vacuum folium (and
contains a kink--antikink pair)” rather than “is locally a vacuum.”

### 5. MAJOR — the virtual-divergence theorem loses its unbroken-direction hypothesis

**Location.** Corner A, `main.tex:149-153`, and Appendix A,
`main.tex:450-454`: “the physical charge density equals the divergence of a
purely virtual bond quantity” for an unspecified/“any” generator; self-audit
`v2-claim-audit.md:68-69`.

**Licensing row.** `G0(d)` is only for `xi in h_alpha`, normal ordered.
`G0(e)` separately gives the physical cut-current continuity equation for any
`xi in g` and finite-range invariant H.

**Independent check.** The paper joins the differently quantified clauses and
thereby extends G0(d) to broken directions.  `claims/CLAIMS.md` and
`corner-a-goldstone.md` keep that distinction explicit.

**Fix demand.** State the virtual-divergence identity only for a normal-ordered
unbroken generator, then state the any-generator continuity equation
separately.

### 6. FATAL — Conjecture S is changed into a different, already contradicted conjecture

**Location.** Corner C, `main.tex:204-211`: for arbitrary n-particle scattering
on “any injective MPS vacuum,” `M_{n+1}=2 i k_s M_n+o(k_s)`; self-audit
`v2-claim-audit.md:88`.

**Licensing row.** `S-general` and D25 conjecture an unspecified multiplier
`Sbold(k_s;{q_i,v_i})`, depending on asymptotic leg data, with only linear
leading order.  The coefficient `2i` is proved only for `n=1` in the spin-1/2
model (`S2-2body`).

**Independent check.** `TRIANGLE.md:233-244` expressly restricts `2 i k_s` to
that two-body instance.  The committed spin-s evidence itself gives `1/s`, not
2, away from `s=1/2`.  Calling the stronger sentence a conjecture does not
create the missing DAG row.

**Fix demand.** Use D25's data-dependent `Sbold` in Conjecture S and mention
`2 i k_s` only as its proved spin-1/2 two-body specialization.

### 7. MAJOR — the repaired universality class and its open obligations are truncated

**Location.** Corner C, `main.tex:204-211`: “on the class of Ward-covariant,
no-contact sources” and “rests on three unproved lemmas”; self-audit
`v2-claim-audit.md:88-89`.

**Licensing rows.** `ML5-B` applies only to all five conditions of D24(d),
including norm control, exhaustive normalized LSZ decomposition, and channel
matching.  `S-general` additionally lists packet-smeared ML4, ML4 for two or
more hard legs, exhaustive LSZ, and microscopic nonemptiness/membership of
`S_W`, besides ML1/ML3/ML6.

**Independent check.** Two adjectives do not carry the five hypotheses, and
the theorem does not reduce to the three parenthetical gaps printed in the
Letter.  Appendix B later lists more gaps, confirming that the main-text count
is incomplete.

**Fix demand.** Name `S_W` as the five-condition D24(d) class and replace the
three-item claim by the complete open-obligation list or a pointer that does
not state a false count.

### 8. MAJOR — Theorem 2 does not carry H-AD-G inside its statement

**Location.** Theorem 2, `main.tex:247-263`: “Assume the scattering hypothesis
H-AD (Appendix C)” followed by a partial paraphrase; self-audit
`v2-claim-audit.md:97`.

**Licensing row.** `M-quant-G` requires H-MQG(1--4) and H-AD-G exactly as
D18(AD1--AD4) for one fixed normalizable D17 packet, with
`q_in=q_L=-1`, `q_T=+1`, no further propagating channel, no bound-state
component, local decay, and the infinite-volume/time/window limit order.

**Independent check.** The theorem says neither that the selected incoming
state is a fixed `ell^1` kink packet nor that it has no bound component; it
does not state `q_in`, exclude additional propagating channels unambiguously,
or carry AD4's limit order.  A parenthetical Appendix pointer is precisely the
footnote-style outsourcing forbidden by the brief.

**Fix demand.** Put H-AD-G by name and all load-bearing AD1--AD4 clauses,
including packet class, charge assignments, channel/bound exclusions, and
limit order, directly in the theorem statement.

### 9. FATAL — the printed 0.004-site “across the scan” accuracy is wrong

**Location.** Memory text `main.tex:276-277`, Fig. 3 caption
`main.tex:321-324`, and Appendix E `main.tex:644-645`; self-audit
`v2-claim-audit.md:102,161`.

**Licensing row/data.** `N2` is SKETCH and cites
`numerics/results/memory-scan-1.json`.  The `0.004` record in
`mquant_check.py` is a gated nine-row certificate with trapped weight below
`10^-6`, and uses the `dx1` estimator (`max=0.004330`).

**Independent check.** Fig. 3(b) plots `dx2` for all eight `main-*` momentum
rows.  Direct recomputation gives
`max |dx2+2T|=0.063565` sites (Delta=3, k0=0.4), not 0.004; even the full-scan
`dx1` maximum is 0.075428.  The caption says “Across the scan” and discloses
neither the low-trapped-weight gate nor the estimator switch.

**Fix demand.** Either report the full plotted-scan residual, or explicitly
restrict `0.004` to the named low-trapped-weight rows and use the same estimator
in text, caption, and plot.

### 10. MAJOR — Fig. 3(c)'s inset uses a post hoc gate not implied by the caption

**Location.** Fig. 3 caption `main.tex:328-332`; generator
`paper/figures/make_figures.py:114-130`; self-audit
`v2-claim-audit.md:164`.

**Licensing row/data.** `Bc` is CONJECTURE with a pre-registered 8% decision
band.  The numerical record identifies `trapped < 10^-2` as the asymptotic
quality gate for the spin-1 grid (`spin1-twomagnon-notes.md:229-237`).

**Independent check.** The generator instead selects falsifier rows solely by
labels `k0=1.2` or `1.8` and cross-check rows by `k0=1.5`.  It includes
`s1-D2.0-k1.8`, with trapped weight 0.05497 and an `dx2/T` deviation 8.075%
(outside the stated 8% band), while excluding clean `k0=0.8` falsifier rows
with trapped weight about 0.0012 and deviations about 2--3%.  The caption does
not disclose this momentum-label selection.

**Fix demand.** Apply the documented asymptotic/quality gate mechanically and
state it in the caption; do not describe the current label filter as fixed in
advance.

### 11. FATAL — v2 asserts the spin-s result that its own licensing authority marks SKETCH

**Location.** Conjecture B paragraph, `main.tex:342-349`: “an exact two-magnon
contact computation gives the slope 1/s in closed form”; Appendix B
`main.tex:511-517`; self-audit `v2-claim-audit.md:121,178-180`.

**Licensing row.** At `83b219b`, `S2-2body-S` is SKETCH pending its critic.

**Independent check.** The main-text sentence asserts exactness without saying
that this is unverified evidence.  The self-audit admits that no promoted row
licenses it and attempts to cure the main-text statement with an Appendix
caveat, contrary to L9's same-sentence status rule.  The later `e237a4e`
promotion resolves the theorem status prospectively but does not make this
v2 self-map accurate at its audited commit.

**Fix demand.** For v2, label the exact computation “unverified evidence” in
the same main-text sentence, or rebase the paper/audit explicitly onto the
later promoted DAG and update every status reference consistently.

### 12. FATAL — Conjecture B's untested charge identification is restated as fact

**Location.** Fig. 3 caption `main.tex:331-332`: “Both follow the charge
datum”; Outlook `main.tex:384-388`: “the magnon's soft phase and the wall's
memory measure one conserved charge ... where every step ... can be checked.”
The self-audit tries to license the latter from an earlier conjecture label at
`v2-claim-audit.md:147-148`.

**Licensing row.** `Bc` is CONJECTURE and explicitly says the `|q_hard|`
factor is UNTESTED because every computed leg has `|q|=1`.

**Independent check.** Varying s with fixed unit charge distinguishes `1/s`
from the constant 2, but it cannot establish the proposed charge dependence.
Neither quoted sentence labels that identification conjectural, and the
closing claim that every step is checkable is contradicted by the named open
wave-operator, sector-reduction, and charge-2 tests.

**Fix demand.** Say the data are “consistent with 1/s”; label the charge
identification as Conjecture B in each occurrence, and delete “every step.”

### 13. MAJOR — the SPT bulk statement omits SPT-B' hypotheses

**Location.** SPT section, `main.tex:356-360`, and Appendix D,
`main.tex:595-605`: “every normalized soft/bulk coefficient is continuous”;
self-audit `v2-claim-audit.md:130-131`.

**Licensing row.** `SPT-B'` requires a common-gap path, continuous external
tensors/channel embeddings/gauge fixes/normalizations, `C^p` data for a
coefficient through order p, and H-soft-p uniformity for derivative soft
limits.

**Independent check.** The main text says only “symmetric gapped deformation
paths.”  Appendix D adds continuous external data but still omits H-soft-p
while retaining “every normalized bulk coefficient.”  The self-audit's claim
that Appendix D carries the full hypotheses is false.

**Fix demand.** Carry common-gap, continuous/`C^p` external-data, and H-soft-p
hypotheses wherever the soft-limit continuity theorem is asserted.

### 14. MAJOR — the main-text SPT memory claim carries H-split but not H-AD-edge

**Location.** SPT section, `main.tex:370-375`: “Physical edge statements carry
H-split ... and charge bookkeeping then quantizes edge-memory outcomes”;
self-audit `v2-claim-audit.md:136-138`.

**Licensing row.** `SPT-M'` is PROVED only as the implication from H-split,
H-AD-edge, charge conservation, and definite channel charges.  It protects
module/capacity, not a nonzero transition amplitude.

**Independent check.** The main-text syntax makes H-split the only visible
hypothesis before the quantization claim.  Appendix D later supplies the
other conditions, but that does not repair the claim-bearing main sentence.

**Fix demand.** State H-AD-edge, conservation, and definite channel charges in
the main sentence alongside H-split.

### 15. MAJOR — a cited priority claim has no L3-local source

**Location.** Introduction `main.tex:69-71`; `refs.bib:396-406` (`Dyson1956`);
`refs/LEDGER.md` “Still non-local.”

**Licensing row.** LIT attribution, governed by L3 rather than a DAG theorem
row.  `OR2` independently proves the soft limit but does not prove the
historical attribution.

**Independent check.** The bibliography itself says that no local Dyson scan
or source exists and asks for verification before submission, yet the paper
cites it twice and attributes the 1956 result to it.  This violates the
binding local-TeX/source rule.

**Fix demand.** Fetch and locally verify an authoritative scan/source before
citing Dyson, or remove the priority attribution and unsupported entry.

### 16. MINOR — two checked bibliography titles do not match the local TeX

**Location.** `refs.bib:116-124` (`Cirac2020`) and `refs.bib:322-330`
(`Williamson2014`).

**Licensing row.** L3 bibliographic fidelity.

**Independent check.** The local source title in
`refs/arxiv-2011.12127/TN-Review-main.tex:46-47` is “Matrix Product States and
Projected Entangled Pair States: Concepts, Symmetries, and Theorems,” while
the BibTeX omits “and.”  The local title in
`refs/arxiv-1412.5604/SPT.tex:56-57` continues “: Gauging and edge theories,”
which the BibTeX omits.  Titles/authors for six other spot checks
(`0802.0447`, `1709.05018`, `1411.5745`, `2107.05401`, `1602.08692`, and
`1203.0609`) match their local TeX.

**Fix demand.** Copy the two complete titles verbatim from the local TeX and
repair the stale `refs.bib:13-14` comment that still calls `1203.0609`
non-local.

### 17. FATAL — Appendix E prints the wrong checker count and overstates red coverage

**Location.** Numerical certificates, `main.tex:633-637`: “nine checkers, all
passing, each with documented failing red mutations.”

**Licensing row.** Meta/numerical provenance; no DAG row licenses this count.

**Independent check.** At `83b219b`, `theory/checks/` contains ten Python
checkers, including `spin_s_slope_check.py`.  Only five source files even
mention a red mode; `corner_a`, `crosscheck_corner_b_tk`, `ml2_completeness`,
`oracle_bethe`, and `soft_current_recon` do not.  All ten normal runs pass, but
that does not make the printed number or “each” true.

**Fix demand.** Print the correct count and identify the specific mutation
tests actually run; do not claim a red mutation for every checker.

### 18. MINOR — the build succeeds but is not warning-clean

**Location.** PRL mechanics, generated `main.log` from an independent clean
`latexmk` build.

**Licensing row.** None; mechanical requirement in the brief.

**Independent check.** `latexmk -pdf -interaction=nonstopmode -halt-on-error`
exits 0 and produces eight pages, with Appendices beginning on page 5.  The
final log nevertheless reports stuck/deferred floats at source lines 156 and
246 and multiple severe underfull boxes.  BibTeX also reports 17 empty-journal
warnings for eprint-only entries.

**Fix demand.** Remove the stuck-float and severe box warnings (and either
accept/document or fill the eprint bibliography fields) before calling the
compile clean.

### 19. MINOR — the captions are not self-contained

**Location.** Fig. 1 caption `main.tex:128-145`, Fig. 2 caption
`main.tex:216-229`, and Fig. 3 caption `main.tex:316-332`.

**Licensing row.** L9/prose-guide rule 25, mechanical rather than a theorem
row.

**Independent check.** Fig. 1 invokes H-AD without defining its content and
defers edge status to the text; Fig. 2 explicitly says “see the text” for the
scope qualifier; Fig. 3 uses `N_T`, `omega`, and `v` without defining them and
hides the inset selection rule.  The captions alone therefore do not teach the
conditions behind the plotted claims.

**Fix demand.** Define the hypotheses/variables and state the relevant scope
and selection gates in each caption without external prose.

### 20. MINOR — several sentences break the binding cautious register

**Location.** `main.tex:153-155` (“learned the hard way”), 178-181
(“independent ... of everything”), 201-204 (“not a technicality”), and
300-304 (“its lattice sharpening”).

**Licensing row.** Prose-guide rules 10--12 and 16; the “of everything” phrase
also exceeds `S2-2body`'s explicitly fixed model/domain.

**Independent check.** These are editorial or absolute constructions rather
than scoped scientific statements.  The result is already strong without
adjudicating its importance or erasing its stated model dependence.

**Fix demand.** Replace them with literal scope: independent of `k_h` and J on
the stated compact domain; explicit counterexample; surviving current/charge
relation.

## Independent checks with no objection

- `apsrev4-2`, exactly three main-text figures, abstract length 598 characters,
  and four pages before the Appendices all meet the stated mechanical limits.
- Regeneration in an isolated temporary tree produced byte-identical PNGs for
  Figs. 1--3.  The PDFs have identical sizes and extracted content; their only
  byte differences are the generated `CreationDate` digits.
- All ten normal checker runs pass.  Independently confirmed values include
  form-factor residual `1.560e-14`, quadratic fit error `2.167e-10`, Fano
  ratios 1.009--1.058 (the stated 0.9--5.8%), bulk coefficient
  `0.125000000000 -> 0.240196078431`, edge magnitude `1/2`, and
  `T(k)=16(Delta-1)^2 k^2+O(k^4)` for the conditional reduced graph.
- No affirmative paper sentence relies on `A2-orbit-r1`, `G0-soft-r1`,
  unrestricted `ML5`, literal Conjecture M, `SPT-B-r1`, or `SPT-nogo`; those
  rows appear only as refutations.  The failures above arise from other scope
  strengthening and from the paper's own incorrect row map.

FAIL(FATAL 1,2,3,4,6,9,11,12,17; MAJOR 5,7,8,10,13,14,15)
