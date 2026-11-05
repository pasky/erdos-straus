#!/bin/bash
# z59 WALDS: reruns after internal review (good-square rows on the cusp space; level-840 survivor screens).
# Usage: bash scripts/z59_walds_rerun_review.sh   (writes data/z59/walds/halfint_cusp_good.txt, diag_survivors_good.txt)
cd "$(dirname "$0")/.."
ulimit -v 4000000
for D in 1 8 21 56 105 168 280 840; do
  timeout 1500 uv run --with cypari2 python scripts/z59_walds_halfint.py 840 $D 16000 -1 1 2>&1 | grep -v -e Warn -e "stack size"
done > data/z59/walds/halfint_cusp_good.txt
for p in "168 168 40000" "280 56 40000" "420 21 40000" "420 105 40000" "240 120 40000" "336 56 40000" "336 168 40000" "560 56 40000" "560 280 40000" "840 21 16000" "840 56 16000" "840 105 16000" "840 168 16000" "840 280 16000" "840 840 16000"; do
  set -- $p
  timeout 1500 uv run --with cypari2 python scripts/z59_walds_diag.py $1 $2 $3 2>&1 | grep -v -e Warn -e "stack size"
done > data/z59/walds/diag_survivors_good.txt
