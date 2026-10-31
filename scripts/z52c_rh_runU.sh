#!/bin/bash
# z52c RESIDUE_HARDNESS: independent solution counter (z52c_rh_count.c, mode 2) for primes p = 1 (mod 4) in (200000, 1000000],
# 20 equal-work chunks (work ~ p), then concatenated into data/z52c/rh/U_counter_2e5_1e6.txt.gz
# (columns as in z52b_fingerprint_count.c: n U D O minz minz_x minz_y maxx minx nx k1 k2 k3 minlcm).
set -euo pipefail
mkdir -p /tmp/rh/raw_counter data/z52c/rh
gcc -O2 -o /tmp/rh/cnt2 scripts/z52c_rh_count.c
a=200001; b=1000000; K=20; pids=()
for k in $(seq 0 $((K-1))); do
  lo=$(python3 -c "import math;print(int(math.sqrt($a**2+$k*($b**2-$a**2)/$K))+ (1 if $k>0 else 0))")
  hi=$(python3 -c "import math;print(int(math.sqrt($a**2+($k+1)*($b**2-$a**2)/$K)))")
  ( ulimit -v 2000000; timeout 7200 /tmp/rh/cnt2 4 $lo $hi 2 > /tmp/rh/raw_counter/U_${lo}_${hi}.txt ) & pids+=($!)
done
for p in "${pids[@]}"; do wait $p; done
cat /tmp/rh/raw_counter/U_*.txt | sort -n | gzip -9 > data/z52c/rh/U_counter_2e5_1e6.txt.gz
