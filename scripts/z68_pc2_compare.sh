#!/bin/bash
# z68 PC2 kill test K1: reduction-built two-prime events vs literal seven-family brute force (modulus <= MMAX).
set -euo pipefail
ulimit -v 6000000
cd "$(dirname "$0")/../data/z68/pc2"
MMAX=${1:-1000000}
for kk in "11 2 13 2" "11 3 13 2" "11 2 13 3" "17 2 19 2"; do
  set -- $kk
  uv run --with cypari2 python ../../../scripts/z68_pc2_events.py events $1 $2 $3 $4 ev_$1_$3_K$2$4.txt
  uv run --with cypari2 python ../../../scripts/z68_pc2_events.py compare $1 $2 $3 $4 $MMAX ev_$1_$3_K$2$4.txt
done
