#!/usr/bin/env bash
# Fetch arXiv e-print TeX sources into refs/arxiv-<id>/ (L3 ground truth).
# Polite: 3 s between requests. Records raw download + extraction result.
set -u
cd "$(dirname "$0")/.."
mkdir -p refs
IDS="1103.2286 1312.6793 1506.01008 2012.07243 1703.05448 1703.07885 2504.10577 1305.2176 0802.0447 2011.12127 1810.07006 1907.02474"
for id in $IDS; do
  dir="refs/arxiv-$id"
  if [ -d "$dir" ] && [ -n "$(ls -A "$dir" 2>/dev/null)" ]; then
    echo "SKIP $id (exists)"; continue
  fi
  mkdir -p "$dir"
  raw="$dir/eprint.raw"
  code=$(curl -sL -w '%{http_code}' -o "$raw" "https://arxiv.org/e-print/$id")
  if [ "$code" != "200" ]; then echo "FAIL $id http=$code"; sleep 3; continue; fi
  t=$(file -b "$raw")
  case "$t" in
    *gzip*)
      if tar -tzf "$raw" >/dev/null 2>&1; then
        tar -xzf "$raw" -C "$dir" && echo "OK $id (tar.gz)"
      else
        gunzip -c "$raw" > "$dir/main.tex" && echo "OK $id (single gz tex)"
      fi ;;
    *tar*) tar -xf "$raw" -C "$dir" && echo "OK $id (tar)" ;;
    *PDF*) mv "$raw" "$dir/paper.pdf"; echo "PDFONLY $id" ;;
    *TeX*|*text*) mv "$raw" "$dir/main.tex"; echo "OK $id (plain tex)" ;;
    *) echo "UNKNOWN $id ($t)" ;;
  esac
  [ -f "$raw" ] && rm -f "$raw"
  sleep 3
done
echo DONE
