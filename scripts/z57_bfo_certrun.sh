#!/bin/bash
# z57 BFO: extend the exhaustive F4 = G* decision (scripts/z56_famdesign_decide.c, unchanged) to (1e10, 2e10].
# 4 parallel nice'd chunks of 2.5e9; output data/z57/bfo/decide_1e10_2e10_<k>.txt (stdout lines + stderr summary).
set -e
gcc -O2 -o /tmp/z57bfo_dec scripts/z56_famdesign_decide.c -lm
for k in 0 1 2 3; do
  A=$((10000000001 + k*2500000000)); B=$((10000000000 + (k+1)*2500000000))
  ( ulimit -v 2000000; nice -n 19 timeout 30000 /tmp/z57bfo_dec $A $B > data/z57/bfo/decide_1e10_2e10_$k.txt 2>&1 ) &
done
wait
