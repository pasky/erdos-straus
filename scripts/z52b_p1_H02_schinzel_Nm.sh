#!/bin/bash
# Z0409: largest exceptional prime of m/p (PW Cor 2.2/2.4 scanner scripts/emn2_scan.c) for m=16..40, p <= PMAX.
# Output: data/z52b/pass1/H02/schinzel_m<m>.txt (lines 'E p' + summary)
PMAX=${1:-3000000}
gcc -O2 -o /tmp/emn2_scan_h02 scripts/emn2_scan.c -lm
for m in $(seq 16 40); do
  ( ulimit -v 4000000; timeout 2400 /tmp/emn2_scan_h02 $m 1 $PMAX 2 > data/z52b/pass1/H02/schinzel_m$m.txt ) &
done
wait
