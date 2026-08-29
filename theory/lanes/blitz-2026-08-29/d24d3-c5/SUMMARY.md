STATUS: PROVED-candidate

- Proved C4 implies both old C5 predicates; the `require()` calls cannot fire.
- Lane copy deletes only those guards and corrects the module/function docstrings.
- Green output and all seven red paths are byte-identical to the original checker.
- Source-audit mutation restores a no-op C5 guard and is detected (red-capable).
- `C5_AUDIT.md` gives the Lamport proof; `verify_repair.out` records execution.
- `PATCH.md` targets only `theory/checks/d24d3_normalization_check.py`.
