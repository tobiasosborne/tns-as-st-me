# peps-pt lane summary

STATUS: PROVED-candidate

- `peps-pt.md` gives a Lamport proof that an explicit fixed-point toric-code PEPS discharges PT1--PT4, so A-INDEX-PEPS is unconditional on this nonzero instance.
- `peps_pt_check.py` contracts the `3x3` PEPS and checks PT1--PT4 exactly; `green.log` has C0--C9 PASS.
- `--red pt2-mix` is caught only by PT2 purity (residual `0.7071`, exit 1); see `red-pt2-mix.log`.
- Standard RFP string nets and finite-`G` G-injective PEPS structurally supply PT1--PT3 only for canonical resolved endpoints on supported registers; PT4 is extra protocol data.
- Proposed rows: retain A-INDEX-PEPS at PROVED (conditional globally; annotate unconditional toric PEPS instance); no change to A-INDEX-TC-fin or SHAPE-FLAT; no class-wide promotion yet.
- `PATCH.md`: none; no existing file is targeted.
