#!/bin/bash
# z49_i3fable_grid.sh — run the CRT splitting model over a grid of nominal sizes N and local types; results to
# data/z49_i3fable/crt_grid/ (main grid, seed = job index), crt_grid/rep_* (replicate seeds for the error estimate) and
# crt_grid/m120_* (the local type 120 | m at N = m^2 for the 13 multiples of 120 up to 1560).
# usage: bash scripts/z49_i3fable_grid.sh BIN M
BIN=${1:-/tmp/z49crt}; M=${2:-20000}
OUT=data/z49_i3fable/crt_grid; mkdir -p $OUT
ulimit -v 8000000
throttle() { while [ "$(jobs -r | wc -l)" -ge 20 ]; do sleep 3; done; }
i=0
for N in 1000 3000 10000 30000 100000 300000 1000000 3000000 10000000 30000000 100000000 300000000 1000000000; do
  for T in "sq 2:0" "sq 2:1" "sq2" "gen 2:0" "gen 2:1"; do
    i=$((i+1)); name=$(echo "$T" | tr ' :' '_-')
    throttle; timeout 7200 $BIN split $N $M $i $T > $OUT/N${N}_${name}.txt 2>&1 &
  done
done
for s in 101 102 103 104; do
  for N in 10000 1000000 100000000; do throttle; timeout 7200 $BIN split $N $M $s sq 2:0 > $OUT/rep_N${N}_sq_2-0_s$s.txt 2>&1 & done
  throttle; timeout 7200 $BIN split 100000 $M $s gen 2:0 > $OUT/rep_N100000_gen_2-0_s$s.txt 2>&1 &
  throttle; timeout 7200 $BIN split 1000000 $M $s sq2 > $OUT/rep_N1000000_sq2_s$s.txt 2>&1 &
done
for j in 1 2 3 4 5 6 7 8 9 10 11 12 13; do m=$((120*j)); throttle; timeout 7200 $BIN split $((m*m)) $M $((200+j)) sq 8:0 3:0 5:0 > $OUT/m120_${m}.txt 2>&1 & done
wait
echo grid done
