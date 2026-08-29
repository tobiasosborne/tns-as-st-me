#!/usr/bin/env python3
"""Enumerate and classify every Γ_M / Γ_{M,γ} use outside blitz lanes."""

from __future__ import annotations

import sys
from pathlib import Path


SYMBOLS = ("Γ_M", "Γ_{M,γ}")
ACTIVE = {
    "Γ_M": {
        "notation.md",
        "definitions.md",
        "claims/CLAIMS.md",
        "theory/ansatz-scattering-2m.md",
    },
    "Γ_{M,γ}": {
        "notation.md",
        "definitions.md",
        "theory/ansatz-scattering.md",
        "theory/ace-ld.md",
    },
}


def is_history(path: str) -> bool:
    return (
        path.startswith("briefs/")
        or path.startswith("theory/verdicts/")
        or path.endswith("-response.md")
    )


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    occurrences: dict[str, list[tuple[str, int, str]]] = {
        symbol: [] for symbol in SYMBOLS
    }
    unexpected: list[str] = []

    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root).as_posix()
        if relative.startswith(".git/") or relative.startswith(
            "theory/lanes/blitz-2026-08-29/"
        ):
            continue
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for symbol in SYMBOLS:
                if symbol not in line:
                    continue
                occurrences[symbol].append((relative, line_number, line.strip()))
                if relative in ACTIVE[symbol]:
                    kind = "ACTIVE"
                elif is_history(relative):
                    kind = "HISTORY"
                else:
                    kind = "UNEXPECTED"
                    unexpected.append(f"{symbol} {relative}:{line_number}")
                print(f"{symbol}\t{kind}\t{relative}:{line_number}")

    for symbol in SYMBOLS:
        active_count = sum(
            1 for path, _, _ in occurrences[symbol] if path in ACTIVE[symbol]
        )
        history_count = len(occurrences[symbol]) - active_count
        print(
            f"SUMMARY {symbol}: active={active_count}, "
            f"history={history_count}, total={len(occurrences[symbol])}"
        )
    if unexpected:
        for item in unexpected:
            print(f"FAIL unexpected register: {item}", file=sys.stderr)
        raise SystemExit(1)
    print("PASS: every occurrence belongs to the D31 register, D28 register, or history")


if __name__ == "__main__":
    main()
