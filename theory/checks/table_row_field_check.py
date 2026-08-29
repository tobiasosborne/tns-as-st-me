#!/usr/bin/env python3
r"""Audit Markdown table rows using only unescaped pipe delimiters.

The repository convention requires literal pipes inside code spans to be
written as ``\|``.  Therefore ``(?<!\\)\|`` is both the table delimiter and
the defect detector; backticks do not need a separate parser.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DELIMITER = re.compile(r"(?<!\\)\|")


def fields(line: str) -> list[str]:
    """Split one pipe-table row, excluding its two boundary delimiters."""
    pieces = DELIMITER.split(line)
    if not pieces or pieces[0] != "" or pieces[-1] != "":
        return pieces
    return pieces[1:-1]


def row_label(line: str) -> str:
    parts = fields(line)
    return parts[0].strip() if parts else "<empty>"


def mutate_row(lines: list[str], label: str, path: Path) -> list[str]:
    """Red mutation: expose one formerly escaped code-span pipe."""
    mutated = list(lines)
    matches = [
        index
        for index, line in enumerate(mutated)
        if line.startswith("|") and row_label(line) == label
    ]
    if len(matches) != 1:
        print(
            f"RED SETUP FAIL: {path}: label {label!r} matched {len(matches)} rows",
            file=sys.stderr,
        )
        raise SystemExit(2)
    index = matches[0]
    if "\\|" not in mutated[index]:
        print(
            f"RED SETUP FAIL: {path}: label {label!r} has no escaped pipe",
            file=sys.stderr,
        )
        raise SystemExit(2)
    mutated[index] = mutated[index].replace("\\|", "|", 1)
    return mutated


def audit(path: Path, expected: int, red_label: str | None) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if red_label is not None:
        lines = mutate_row(lines, red_label, path)

    problems: list[str] = []
    row_count = 0
    for line_number, line in enumerate(lines, start=1):
        if not line.startswith("|"):
            continue
        row_count += 1
        actual = len(fields(line))
        if actual != expected:
            problems.append(
                f"{path}:{line_number}: label={row_label(line)!r}: "
                f"fields={actual}, expected={expected}"
            )
    print(f"AUDIT {path}: rows={row_count}, expected_fields={expected}")
    return problems


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--notation", type=Path, default=Path("notation.md"))
    parser.add_argument("--claims", type=Path, default=Path("claims/CLAIMS.md"))
    parser.add_argument(
        "--red-claims-label",
        help="in-memory mutation: unescape one pipe in this CLAIMS row",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    problems = audit(args.notation, 3, None)
    problems.extend(audit(args.claims, 6, args.red_claims_label))
    if problems:
        for problem in problems:
            print(f"FAIL {problem}", file=sys.stderr)
        print(f"FAIL: {len(problems)} malformed table row(s)", file=sys.stderr)
        raise SystemExit(1)
    print("PASS: all notation rows have 3 fields and all CLAIMS rows have 6")


if __name__ == "__main__":
    main()
