LANE: ace-ld | BEADS: tns-hfw (P2) + tns-dsh (P3), same file family | LANE DIR: theory/lanes/blitz-2026-08-29/ace-ld/
Read RULES.md first, then theory/ace-ld.md section 5, theory/checks/ace_ld_check.py, theory/verdicts/ace-ld-r4.md (M1, m5, m6).
TASK on COPIES in your lane dir (both issues touch the same files — you own both to avoid a race):
(1) tns-hfw: gates C5b-STABILITY and C6-SWEEP are reached by no registered mutation, yet section 5 + docstring claim a complete unreached-gate enumeration. Either register mutations that demonstrably reach both gates (run them, show the red), or move both to the unreached list naming the shadowing gate, and correct the completeness claim in BOTH places. Verify by measurement on your copy, not by reading.
(2) tns-dsh: the double-Cesaro protocol wraps the N=2048 ring at 4T >= N/2 (T>=256) with NO guard on C5B_LR2_TS; add an explicit guard or documented ceiling derived from N at the configuration point; also replace the stale 'notation.md line 271' citation in HONEST STATUS with a content anchor (the twist row moved to 289 — anchor by content, not number).
Deliver PATCH.md (anchored) + measured reachability table + red/green logs.
