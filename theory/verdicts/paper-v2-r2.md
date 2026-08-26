<!-- ROLE: L6 adversarial critic verdict on paper v2.1, round 2.
     Critic: Codex. Date: 2026-08-26.
     Audited repair commit: e6e67ac (paper diff against HEAD~1). -->

# Paper v2.1 critic verdict r2

I adjudicated only the twenty demands in `paper-v2-r1.md`, the paper-scoped
repair diff, the rewritten claim audit, and the requested mechanics.  I
recomputed the memory and spin-$s$ plotted records, reran
`mquant_check.py`, regenerated the figures from a clean `git archive` in
`/tmp`, and built the paper from clean LaTeX state there.  Most repairs are
real, but four old demands remain incompletely repaired and one fatal edge
claim survives in changed caption text.

## Adjudication of objections 1--20

| obj. | adjudication | independent check against the r1 fix demand |
|---:|:---:|---|
| 1 | **UNRESOLVED** | The blanket triangle theorem is gone, the memory clause is conditional, and the edges are called conjectural.  However, the demanded model-scoped soft inventory is still absent: the abstract says only that, for “quantum spin chains,” “a soft magnon leaves two-body scattering with a universal phase slope” (`main.tex:45--51`).  The promoted `S2-2body-S` theorem is not a theorem for generic spin chains; it is for the bilinear isotropic ferromagnet on its regular two-magnon domain.  Adding “two-body” does not supply that model/domain fence in the claim-bearing abstract sentence. |
| 2 | **RESOLVED** | “Numerics verify each claim” is deleted.  The remaining numerical prose names individual finite calculations and committed records. |
| 3 | **RESOLVED** | The opening now carries H-AD-G in the displacement clause (`main.tex:93--95`) and replaces “the triangle closes” by the proved current-flux and conditional charge-bookkeeping content (`main.tex:95--98`, `319--329`). |
| 4 | **RESOLVED** | The text now says finite truncations remain in the vacuum folium and explicitly carry a kink--antikink pair (`main.tex:151--155`); it no longer equates them locally with a vacuum. |
| 5 | **RESOLVED** | Both main text and Appendix A restrict the virtual-divergence identity to a normal-ordered unbroken generator and state the any-generator physical continuity equation separately (`main.tex:180--187`, `480--490`). |
| 6 | **RESOLVED** | Conjecture S now uses the D25 data-dependent multiplier $\mathsf S$, linear only at leading order; $2\mathrm{i}k_s$ is stated only as the proved spin-$1/2$ two-body instance (`main.tex:237--246`, `535--543`). |
| 7 | **RESOLVED** | The five-condition D24(d) class $\mathcal S_W$ is named.  The body gives a non-exhaustive open list without a false count and points to Appendix B, which supplies the complete list including exhaustive LSZ, nonemptiness/membership, and limit-order control (`main.tex:237--246`, `535--551`). |
| 8 | **UNRESOLVED** | The displayed Theorem 2 now contains the AD1--AD4 channel, charge, bound-state, decay, and limit-order clauses.  It still replaces the demanded fixed D17 $\ell^1$ kink packet by the weaker “normalizable kink-magnon wavepacket in that sector” (`main.tex:265--273`).  D17 summability is load-bearing: `memory-quantization-general.md:96--99` says weak-* sector membership alone does not make the regularized charge converge.  Appendix C mentions summable charge deviations only after the theorem (`main.tex:589--600`), which does not meet the demand that the packet class be inside the displayed statement.  Claim-audit row 101 is therefore false when it says all H-MQG(4--5) clauses are inside. |
| 9 | **RESOLVED** | Direct recomputation from `memory-scan-1.json` gives eight plotted `main-*` rows and $\max|dx2+2T|=0.063565368$ (the stated 0.064), at `main-D3.0-k0.4`; the corresponding full-scan $dx1$ maximum is 0.075428189.  On the nine rows selected by $N=160$, standoff 36, `dwmax=3`, $J_\perp=1$, and trapped $<10^{-6}$, the maxima are 0.004330050 (`dx1`) and 0.001232702 (`dx2`).  Thus 0.005 is honest for both gated estimators and the caption's 0.002 is honest for its plotted `dx2` estimator.  Normal and `python3 -O` checker runs independently printed those same gated values and PASS. |
| 10 | **RESOLVED** | `bc_memory_points()` applies trapped $<10^{-2}$ after a physical-grid/control-prefix classification and contains no momentum gate.  Re-evaluation of both JSONs selects 17 plotted memory points and excludes `s1-D2.0-k1.8` (trapped 0.054969).  The maximum relative deviation from $1/s$ is 0.026853483, at `s1-D6.0-k0.8`; every selected point is inside 8%.  The caption discloses the trapped gate and exclusion of convergence/truncation/preparation controls. |
| 11 | **UNRESOLVED** | The status repair itself is legitimate: `S2-2body-S` is PROVED after `spin-s-r1.md`.  Appendix B reproduces the exact model, fixed-hard regular domain, signed slope, compact/fixed-channel uniformity, and every exclusion (`main.tex:553--565`).  The claim-bearing main paragraph does not: it asserts the exact spin-$s$ slope while stating only “the unit-charge two-body slope” (`main.tex:342--346`), omitting the bilinear isotropic Hamiltonian, $0<|k_h|<\pi$, the regular/fixed-channel domain, and endpoint/equal-velocity exclusions.  The abstract and Fig. 1 likewise use the promoted result without its model/domain fence.  Claim-audit row 123 incorrectly calls “unit-charge two-body” the theorem's “exact scope”; the exact scoping sentence in `spin-s-r1.md` contains substantially more.  The upward fix therefore does not stay exactly within the promotion sentence on every assertion surface. |
| 12 | **RESOLVED** | The data are described as consistent with $1/s$; the common-charge identification is labelled Conjecture B in the main text, Fig. 3 caption, and Outlook; $|q_{\rm hard}|>1$ is called untested; “every step” is deleted (`main.tex:331--349`, `369--375`, `412--416`). |
| 13 | **UNRESOLVED** | The main SPT sentence adds a common gap, continuous external data, and H-soft-$p$, but still omits the required $C^p$ external data for a coefficient obtained through a soft limit or $p$ derivatives (`main.tex:383--387`).  Appendix D states $C^p$ correctly (`main.tex:654--658`), but r1 demanded these hypotheses wherever the soft-limit theorem is asserted.  Claim-audit row 132 is false in saying that continuous/$C^p$ data are all in the main sentence. |
| 14 | **RESOLVED** | The claim-bearing main sentence now places H-split, H-AD-edge, charge conservation, and definite channel charges before the edge-memory implication, and keeps protection at capacity rather than amplitude (`main.tex:398--406`). |
| 15 | **RESOLVED** | The unsupported Dyson priority attribution, both citations, and the BibTeX entry are removed.  No remaining paper citation relies on that non-local source. |
| 16 | **RESOLVED** | The Cirac and Williamson titles match the local TeX, and the stale `1203.0609` comment is corrected. |
| 17 | **RESOLVED** | There are exactly ten Python checkers.  Exactly five source files expose documented red modes: `ml4_check.py`, `mquant_check.py`, `mquant_general_check.py`, `spin_s_slope_check.py`, and `spt_rebuild_check.py`.  Appendix E now says precisely that (`main.tex:693--698`). |
| 18 | **RESOLVED** | A clean isolated `latexmk` build exits 0.  The final log contains no stuck/deferred-float, underfull/overfull, undefined-reference, or undefined-citation warning.  The only final TeX warning is revtex's default 10-point-size notice; the 17 BibTeX empty-journal warnings are the eprint-only cases explicitly documented and accepted in `refs.bib:5--8`, as the r1 fix demand allowed. |
| 19 | **UNRESOLVED** | The captions are improved but do not yet stand alone.  Fig. 2 uses $v_h/\omega_h$ without defining either quantity and says “every hard momentum”/“all $k_h$” without the theorem's compact subset of $(0,\pi)$ or endpoint/equal-velocity exclusions (`main.tex:165--176`).  Fig. 1 abbreviates H-AD-G without its no-bound-component, local-decay, or limit-order clauses.  More seriously, its edge-status sentence is false; see new objection 21. |
| 20 | **RESOLVED** | The four cited register breaks are replaced by literal scope.  The changed prose introduces no separate editorial/arrogant-register violation. |

## New objection

### 21. FATAL — Fig. 1 asserts the conjectural $\mathcal A\Rightarrow\mathcal C$ edge as holding

**Location.** Fig. 1 caption, `main.tex:73--80`: immediately after “No edge is
a theorem,” the caption says
“$\mathcal A\!\Rightarrow\!\mathcal C$ holds in the two-body sector,
conjectural beyond.”  The rewritten audit maps this to the edge ledger as
self-contained and correct at `v2-claim-audit.md:158`.

**Licensing rows.** The ledger says **A $\Rightarrow$ C -- CONJECTURE** and,
more explicitly, `claims/CLAIMS.md:93--96` says that the edge is *not supplied
by Corner A*: G0(e) provides neither an Adler zero nor universality.  The
proved `S2-2body`/`S2-2body-S` rows establish a Corner-C two-body amplitude;
they do not prove the implication from Corner A to Corner C.

**Independent check.** “No edge is a theorem” does not cure the next clause's
affirmative “holds.”  This is also not the harmless statement that Corner C
itself is proved in a two-body model.  It assigns a proved sector to the
specific A-to-C edge that the authoritative ledger keeps conjectural for the
missing Ward/LSZ/regularity reasons.  The audit has conflated a proved corner
with a proved edge.

**Fix demand.** Replace the clause by the actual ledger status, e.g. “the
$\mathcal A\Rightarrow\mathcal C$ edge remains Conjecture S; independently,
Corner C is proved in the stated two-body ferromagnet.”  Correct claim-audit
row 158 at the same time.

## Claim-audit spot checks

The repaired numerical rows are accurate: row 106 reproduces the independent
0.063565/0.004330/0.001233 calculation, row 122's 2.69% maximum is correct,
and rows 171--180 correctly record the bibliography and checker edits.  Four
rewritten rows are not accurate: row 101 overlooks the missing D17 $\ell^1$
packet clause; row 123 calls a truncated phrase the exact `S2-2body-S` scope;
row 132 claims $C^p$ appears in the main SPT sentence when it does not; and
row 158 promotes the A-to-C edge in the two-body sector.

## Mechanics and reproduction

- `make_figures.py` ran from a clean `git archive` of `e6e67ac`.  All three
  regenerated PNGs are byte-identical to the commit.  Each regenerated PDF
  has identical extracted text and an identical 300-dpi rendering; its raw
  byte difference is generation metadata only.
- The Fig. 3 memory inset contains the mechanically selected 17 points.  Its
  largest relative deviation is 2.6853483%, and the excluded trapped row is
  outside the gate as claimed.
- Clean `latexmk` produces eight pages.  The acknowledgments end on page 4 and
  Appendix A starts on page 5.  There are exactly three `figure` environments.
  The normalized abstract is 595 characters.  The caption self-containment
  requirement fails for the reasons in objections 19 and 21.

FAIL(FATAL 1,11,21; MAJOR 8,13; MINOR 19)
