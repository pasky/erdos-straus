#!/bin/bash
# z60 SIGNED: the five survivor-line runs of scripts/z60_signed_pseudosq.py (Sec. 6.2), summaries to stdout
set -o pipefail
ulimit -v 4000000
cd "$(dirname "$0")/.."
while read L D G DP; do
  echo "== L=$L D=$D G=$G D'=$DP"
  timeout 1700 uv run --with cypari2 python scripts/z60_signed_pseudosq.py $L $D 40000 "$G" $DP 200 data/z60/signed/pseudosq_${L}_${D}.txt 2>&1 | grep -v -e Warn -e "stack size"
done <<'LIST'
168 168 [0,-1,0,-36,-72] -168
280 56 [0,0,0,37,-138] -56
560 280 [0,-1,0,-40,-84] -280
420 21 [0,-1,0,-56,-84] -84
420 105 [0,1,0,-120,-432] -420
LIST
