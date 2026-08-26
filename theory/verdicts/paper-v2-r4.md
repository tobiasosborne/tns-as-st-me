<!-- ROLE: L6 adversarial critic verdict on paper v2.3, round 4.
     Critic: Codex. Date: 2026-08-26.
     Audited repair commit: 37ba616 (paper diff against HEAD~1). -->

# Paper v2.3 critic verdict r4

I adjudicated only objections 1 and 11 against the r3 fix demands, checked the
new three-mode licensing rule and its affected rows, and audited every
compression in `HEAD~1..HEAD` under `paper/` for repair drift.  Both old
objections are resolved.  One new compression deletes a load-bearing register
from Fig. 1, so the paper does not yet pass.

## Adjudication

| obj. | adjudication | independent check against the r3 fix demand |
|---:|:---:|---|
| 1 | **RESOLVED** | The abstract now prints the bilinear isotropic model, regular two-magnon domain, fixed hard momentum inside the band, and unit charge (`main.tex:45--50`).  The remaining clauses really are entailed at the soft point.  For the spin-$s$ dispersion $v_s(k)=2Js\sin k$, a fixed hard momentum strictly inside the band has $0<|k_h|<\pi$ and hence $v_h\neq0$; equivalently the soft-base denominator used in `spin-s-r1.md` sec. 3 is $s(e^{2ik_h}-1)\neq0$.  Thus the band edges are excluded.  Since $v_s(k_s)\to0$, continuity gives a two-sided soft neighborhood in which $\operatorname{sgn}(v_h-v_s)$ is constant; this both fixes the D7 physical channel and keeps $v_h\neq v_s$.  No compact-hard uniformity is asserted in the abstract.  The opening (`main.tex:94--96`) uses the existential “in an exactly solved two-magnon problem” and immediately points to Theorem 1; it asserts no model, spin, domain, charge, or process breadth independent of that fenced theorem.  It is therefore a genuine indexical signpost at the breadth at issue. |
| 11 | **RESOLVED** | Fig. 1's Corner-C gloss (`main.tex:66--71`) now enumerates the complete promotion fence: two-body scattering, bilinear isotropic ferromagnet, regular two-magnon domain, fixed hard momentum in $(0,\pi)$, fixed channel, unit charge, and explicit band-edge/equal-velocity exclusions.  Restricting to the positive half-zone is narrower than the promoted $0<|k_h|<\pi$ domain and makes the displayed slope $1/s$ the positive-channel specialization.  The caption claims no compact-set uniformity, Bethe completeness, many-body theorem, memory half, or higher-charge factor. |

## Licensing-rule audit

The three modes in `v2-claim-audit.md:35--40` are sound with the limitation
the rule itself states: an indexical sentence is permissible only when it
points to a fenced theorem and carries no independent breadth claim.
Enumeration preserves the fence literally; entailment is legitimate when it
is checked from the licensed hypotheses rather than supplied by another
sentence; and a genuinely indexical signpost delegates scope without asserting
a wider theorem.  The updated abstract, opening, and Fig. 1 Corner-C rows at
lines 52, 62, and 177 apply those modes accurately.  In particular, “fixed
hard momentum inside the band” supplies the nonzero hard velocity needed for
both channel constancy and equal-velocity exclusion only pointwise; the audit
correctly disclaims compact-hard uniformity.

## New objection

### 22. MAJOR — Fig. 1's Corner-A compression drops the padded-window register

**Location.**  The diff changes Fig. 1 from “on windows padded about a bond
these generate the charge algebra” to “padded about a bond, these generate the
charge algebra” (`main.tex:62--66`).

**Licensing rows.**  A1(d1)/(d3) prove the twisted-group-algebra action on
finite windows padded around the distinguished bond.  The paper itself keeps
the extension to the physical half-infinite algebra open as H-split
(`main.tex:154--156`, `466--470`).

**Independent check.**  After “windows” is deleted, the participial phrase
grammatically modifies the bond operators (“these”), not a representation
window.  The caption therefore says that the endpoint operators themselves
generate $\mathbb C_\omega[G]$ without identifying the proved padded-window
register.  That is exactly the qualifier separating A1(d1) from the open
physical-edge reading, and a later body or appendix qualification does not
make a claim-bearing figure caption self-contained.  The unchanged Fig. 1
Corner-A audit row at `v2-claim-audit.md:176` consequently overstates the
license after this compression.

**Fix demand.**  Restore the subject, for example: “on windows padded about a
bond, these generate the charge algebra $\mathbb C_\omega[G]$.”  Update the
caption row only if its quoted fragment changes.

## Remaining drift and mechanics

The other compressions preserve their accepted hypotheses and statuses.  In
particular, “windows” in the main A1 paragraph still denotes the finite-window
register, H-AD-G remains conditional on the stated sector-reduction
hypothesis, and the SPT deformation sentence retains the common-gap,
continuous/$C^p$-data, H-soft-$p$, and local-constancy clauses.

From a clean `git archive` of `37ba616`, `latexmk -C` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` exited 0 and
produced eight pages.  The final log has no undefined references or citations,
overfull/underfull boxes, or stuck/deferred floats; only revtex's default
10-point notice remains (the documented eprint-only BibTeX warnings are
unchanged).  The whitespace-normalized abstract is **599 characters**, the
acknowledgments end on page 4 and Appendix A begins on page 5, and the source
contains exactly three figure environments and three figure includes.

FAIL(MAJOR 22)
