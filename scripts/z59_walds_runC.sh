#!/bin/bash
# z59 WALDS: the 12 (L,D) reruns of sweep A/B (crashed print or stack overflow) -> data/z59/walds/halfint_sweep_C.txt
# Usage: bash scripts/z59_walds_runC.sh > data/z59/walds/halfint_sweep_C.txt
cd /home/pasky/projects/math/erdos-straus-claude-agent-worktree-0044
ulimit -v 4000000
for p in "168 168 10000 4" "280 56 10000 4" "420 21 10000 4" "420 105 10000 4" "240 120 8000 4" "336 56 8000 4" "336 168 8000 4" "560 56 8000 4" "560 280 8000 4" "840 1 8000 1" "840 8 8000 1" "840 21 8000 1"; do
  set -- $p
  for l0 in 0 11; do
    timeout 1500 uv run --with cypari2 python scripts/z59_walds_halfint.py $1 $2 $3 $l0 $4 2>&1 | grep -v -e Warn -e "stack size"
  done
done
