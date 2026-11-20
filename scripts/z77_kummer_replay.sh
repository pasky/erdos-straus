#!/usr/bin/env bash
# From repository root. One compute at a time; ~0.5 GiB private temporary data.
set -euo pipefail
ulimit -v 6000000
src=$PWD/scripts; dst=$PWD/data/z77/kummer_comp
d=$(mktemp -d); trap 'rm -f "$d"/{prime,check,factor,prime.txt,comp.txt,raw_jobs,jobs,fallback.txt,checks.txt,summary.txt,local.txt,sha256.txt}; rmdir "$d"' EXIT
cd "$d"
for pair in 'prime prime' 'check check' 'factors factor'; do
  read -r source exe <<<"$pair"
  timeout 120 g++ -O3 -Wall -std=c++17 "$src/z77_kummer_$source.cpp" -o "$exe"
done
py=(uv run --offline --no-project python)
timeout 1800 ./prime >prime.txt
timeout 1800 ./prime composites >comp.txt
timeout 1800 ./check prime.txt comp.txt raw_jobs >summary.txt
timeout 120 "${py[@]}" "$src/z77_kummer_jobs.py" raw_jobs >jobs
timeout 1800 ./factor <jobs >fallback.txt
timeout 120 "${py[@]}" "$src/z77_kummer_jobs.py" raw_jobs fallback.txt >checks.txt
timeout 120 "${py[@]}" "$src/z77_kummer_local.py" >local.txt
timeout 120 sha256sum prime.txt comp.txt >sha256.txt
for f in summary.txt checks.txt local.txt sha256.txt fallback.txt; do cmp "$f" "$dst/$f"; done
echo 'All panels, prime enumeration, positive identities and fallback rows reproduced.'
