#!/bin/bash
# z52c RESIDUE_HARDNESS: U(p) etc. for primes p = 1 (mod 4) in (200000, 1000000], 20 equal-work chunks (work ~ p).
# Output data/z52c/rh/raw/U_<lo>_<hi>.txt (columns as in z52b_fingerprint_count.c).
set -e
gcc -O2 -o /tmp/rh/cnt2 scripts/z52c_rh_count.c
a=200001; b=1000000; K=20
for k in $(seq 0 $((K-1))); do
  lo=$(python3 -c "import math;print(int(math.sqrt($a**2+$k*($b**2-$a**2)/$K))+ (1 if $k>0 else 0))")
  hi=$(python3 -c "import math;print(int(math.sqrt($a**2+($k+1)*($b**2-$a**2)/$K)))")
  ( ulimit -v 2000000; timeout 7200 /tmp/rh/cnt2 4 $lo $hi 2 > data/z52c/rh/raw/U_${lo}_${hi}.txt ) &
done
wait
