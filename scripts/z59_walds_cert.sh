#!/bin/bash
# z59 WALDS: validity certificates for the 15 survivor pairs: T1 rows + rows g(z) = 0 at every known R-zero z <= B.
# Rank 0 on C1 => every valid proxy of that (L, psi) vanishes on C1 ∩ [1, B] (full space: all of M_{3/2};
# cusp space with good-square rows: the TERNARY class, genus-theta Eisenstein part).
# Usage: bash scripts/z59_walds_cert.sh > data/z59/walds/cert_survivors.txt
set -o pipefail
cd "$(dirname "$0")/.."
ulimit -v 4000000
for p in "168 168 10000 0 4" "280 56 10000 0 4" "420 21 10000 0 4" "420 105 10000 0 4" "240 120 8000 0 4" "336 56 8000 0 4" "336 168 8000 0 4" "560 56 8000 0 4" "560 280 8000 0 4" "840 56 8000 0 4" "840 168 8000 0 4" "840 280 8000 0 4" "840 21 16000 -1 1" "840 105 16000 -1 1" "840 840 16000 -1 1"; do
  set -- $p
  timeout 1500 uv run --with cypari2 python scripts/z59_walds_halfint.py $1 $2 $3 $4 $5 1 2>&1 | grep -v -e Warn -e "stack size"
done
