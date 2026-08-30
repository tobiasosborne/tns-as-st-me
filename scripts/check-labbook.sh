#!/usr/bin/env bash
# check-labbook.sh — lockstep gate for the LaTeX labbook (TJO directive
# 2026-08-30). Fails if any claim id in claims/CLAIMS.md or any definition
# number in definitions.md is absent from labbook/sections/*.tex, i.e. the
# labbook has gone stale relative to the claims DAG.
#
# Usage: scripts/check-labbook.sh          (from the repo root)
# Exit 0 = labbook covers every id; exit 1 = missing ids (listed on stdout).

set -u
cd "$(dirname "$0")/.." || exit 2

fail=0

# --- claim ids: first column of the CLAIMS.md table (skip the header) -----
ids=$(awk -F'|' '/^\|/ {gsub(/^[ \t]+|[ \t]+$/, "", $2); print $2}' claims/CLAIMS.md \
      | grep -v -e '^id$' -e '^---*$' -e '^$')

# --- definition numbers: "## Dn (" headings + the embedded D6-D8 ----------
defs=$(grep -oE '^#+ D[0-9]+|^\*\*D[0-9]+ ' definitions.md \
       | grep -oE 'D[0-9]+' | sort -uV)

missing=0
for id in $ids $defs; do
  if ! grep -rqF -- "$id" labbook/sections/; then
    echo "MISSING from labbook: $id"
    missing=$((missing + 1))
  fi
done

if [ "$missing" -gt 0 ]; then
  echo "check-labbook: $missing identifier(s) missing — the labbook is stale."
  echo "Rule: any commit changing claims/CLAIMS.md or definitions.md must"
  echo "update the owning labbook shard in the same commit."
  fail=1
else
  echo "check-labbook: OK — every claim id and definition is covered."
fi

# --- the labbook must not contain verbatim environments (TJO ban) ---------
if grep -rnE '\\begin\{(verbatim|lstlisting|alltt|minted)\}' labbook/sections/ labbook/main.tex 2>/dev/null; then
  echo "check-labbook: FORBIDDEN verbatim-family environment found (see above)."
  fail=1
fi

exit $fail
