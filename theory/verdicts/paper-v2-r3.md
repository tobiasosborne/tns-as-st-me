<!-- ROLE: L6 adversarial critic verdict on paper v2.2, round 3.
     Critic: Codex. Date: 2026-08-26.
     Audited repair commit: 50a2f16 (paper diff against HEAD~1). -->

# Paper v2.2 critic verdict r3

I adjudicated only objections 1, 8, 11, 13, 19, and 21 against their r2
fix demands, the complete `HEAD~1..HEAD` paper diff, the requested claim-audit
anchors, and the requested mechanics.  Four repairs are complete.  The
model/domain repair is not: the exact `S2-2body-S` fence is still absent from
three of the four claim-bearing summary surfaces.

## Adjudication

| obj. | adjudication | check against the r2 fix demand |
|---:|:---:|---|
| 1 | **UNRESOLVED — FATAL** | The abstract now says “bilinear isotropic ferromagnet” and “regular two-magnon domain,” but its proved soft-slope sentence still omits fixed hard momentum in $(0,\pi)$, fixed channel, the band-edge/equal-velocity exclusions, and unit charge (`main.tex:45--53`).  The opening “whole result” sentence is weaker still: “two-body ferromagnet scattering” supplies none of bilinear/isotropic, regular-domain, fixed-hard/fixed-channel, exclusion, or unit-charge scope (`main.tex:93--101`).  The brief requires the fence inside every assertion surface, not supplied by a later theorem.  Claim-audit lines 38 and 48 therefore overstate the licensing of the abstract and expressly rely on scope carried elsewhere for the opening sentence, contrary to the same-sentence rule at audit lines 25--26. |
| 8 | **RESOLVED** | Theorem 2's displayed statement now fixes one kink-magnon packet whose deviations from the two vacua are summable, calls this the $\ell^1$ kink class, and excludes a plane wave (`main.tex:265--278`).  This is faithful to D17/H-MQG(4): the two tail charge-deviation sums are the load-bearing condition.  D17's additional first moment is required only when D13(c) is used, which this windowed-coordinate theorem does not do. |
| 11 | **UNRESOLVED — FATAL** | The Conjecture-B paragraph now carries the full promotion fence: bilinear isotropic model, regular two-magnon domain, fixed $k_h\in(0,\pi)$ and channel, unit charge, and band-edge/equal-velocity exclusions (`main.tex:334--352`).  The other assertion surfaces do not.  Besides the abstract and opening defects under objection 1, Fig. 1 asserts the spin-$s$ slope while omitting the regular-domain and fixed-channel clauses and unit-charge restriction (`main.tex:66--70`).  Thus the upward fix still does not remain within the exact `spin-s-r1.md` promotion sentence on every surface; claim-audit line 163's “model/domain fence and exclusions in-caption” is incomplete. |
| 13 | **RESOLVED** | The claim-bearing main SPT sentence now says that a coefficient reached through a soft limit or $p$ derivatives additionally requires $C^p$ external data and H-soft-$p$, while the enclosing sentence retains common-gap paths and continuous external data (`main.tex:382--394`).  This matches the Appendix-D/source clause and makes claim-audit line 139 accurate. |
| 19 | **RESOLVED** | Fig. 2 defines $\omega_h=J(1-\cos k_h)$ and $v_h=J\sin k_h$ and restricts the claim to $k_h$ in a compact subset of $(0,\pi)$ (`main.tex:167--181`).  Fig. 1 now names completeness, a fixed packet with no bound component, the reflected/transmitted charged channels, local decay, and the volume--time--window order under H-AD-G (`main.tex:71--76`).  Those are the caption defects identified in r2; the remaining Fig. 1 spin-$s$ fence defect is adjudicated under 11. |
| 21 | **RESOLVED** | Fig. 1 now distinguishes the proved two-body Corner-C amplitude from the edge and says the $\mathcal A\!\Rightarrow\!\mathcal C$ edge remains Conjecture S “at every order” (`main.tex:77--83`).  It no longer assigns a proved two-body sector to the edge. |

## Repair-drift and claim-audit check

No new objection is needed beyond the surviving objections 1 and 11.  I
checked every compression in `main.tex`; none of the other edits deletes a
load-bearing hypothesis or changes a conditional/conjectural status.  In
particular, the current audit rows for Theorem 2, Conjecture B, the SPT
coefficient, the Fig. 1 edge, and Fig. 2 are accurate.  The abstract/opening
soft rows and Fig. 1 Corner-C row are inaccurate only in the already-counted
way above: they call a partial fence complete or defer the missing fence to
another assertion surface.

The whitespace-normalized abstract is exactly **600 characters**, hence
within the stated limit.  Its endpoint-algebra, conditional-memory, edge
status, and refutation clauses remain licensed; its soft-slope clause is not
licensed at the breadth printed because the rest of the mandatory
`S2-2body-S` fence is absent.

## Mechanics

From a clean `git archive` of `50a2f16`, I ran `latexmk -C` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.  The build
exited 0 and produced eight pages.  The final log has no undefined
references/citations, overfull/underfull boxes, or stuck/deferred floats; its
only TeX warning is revtex's default 10-point notice.  The acknowledgments end
on page 4, Appendix A begins on page 5, and the source contains exactly three
`figure` environments and three figure includes.

FAIL(FATAL 1,11)
