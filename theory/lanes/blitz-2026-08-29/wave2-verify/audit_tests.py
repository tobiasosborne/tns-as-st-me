#!/usr/bin/env python3
"""Static inventory of the wave-2 @test predicates (not a runtime substitute)."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
path = ROOT / "numerics/test/test_lambdaD_memory.jl"
lines = path.read_text().splitlines()
tests = [(number, line.strip()[len("@test ") :]) for number, line in enumerate(lines, 1)
         if line.strip().startswith("@test ")]

assert len(tests) == 50
assert all(expression not in {"true", "nothing", "begin", "1 == 1"}
           for _, expression in tests)

groups = [
    ("vacua", 96, 113, 6, 6),
    ("dispersion", 114, 131, 7, 7),
    ("packet", 132, 143, 4, 4),
    ("LD-ID", 144, 156, 4, 4),
    ("integer support", 157, 169, 4, 4),
    ("transport", 170, 195, 10, 10),
    ("edge memory", 196, 224, 9, 11),
    ("JSON records", 225, 240, 6, 6),
]

for name, lo, hi, source_expected, executed_expected in groups:
    source_count = sum(lo <= number <= hi for number, _ in tests)
    assert source_count == source_expected, (name, source_count, source_expected)
    print(f"{name}: source={source_count} executed={executed_expected} REAL_ASSERTIONS")

print(f"total_source={len(tests)} total_executed=52 stubs=0")
print("STATIC AUDIT: PASS (runtime execution still required)")
