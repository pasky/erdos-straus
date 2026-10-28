#!/bin/bash
# z49_i3fable_grid.sh — run the CRT splitting model over a grid of nominal sizes N and local types; results to data/z49_i3fable/crt_grid/
# usage: sh scripts/z49_i3fable_grid.sh BIN M
BIN=${1:-/tmp/z49crt}; M=${2:-20000}
OUT=data/z49_i3fable/crt_grid; mkdir -p $OUT
ulimit -v 8000000
i=0
for N in 10000 30000 100000 300000 1000000 3000000 10000000 30000000 100000000 300000000 1000000000; do
  for T in "sq 2:0" "sq 2:1" "sq2" "gen 2:0" "gen 2:1"; do
    i=$((i+1)); name=$(echo "$T" | tr ' :' '_-')
    timeout 7200 $BIN split $N $M $i $T > $OUT/N${N}_${name}.txt 2>&1 &
    # at most 12 concurrent jobs
    while [ $(jobs -r 2>/dev/null | wc -l) -ge 12 ]; do sleep 5; done
  done
done
wait
echo grid done
