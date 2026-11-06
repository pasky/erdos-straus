#!/bin/bash
# z60 MS105: production run of the n = s*m^2 family search (squarefree kernel s = 1 (4), 13 <= s <= 1000, gcd(s,105)=1;
# odd m coprime to 105, m <= floor(sqrt((2^64-1)/s)) i.e. n < 2^64).  4 lanes, each s in one call.
# Usage: scripts/z60_ms105_sm2_run.sh   (outputs data/z60/ms105/sm2/lane{0..3}.txt)
set -e
gcc -O2 -march=native -o /tmp/ms105_sm2 scripts/z60_ms105_sm2.c
mkdir -p data/z60/ms105/sm2
python3 - > /tmp/ms105_slist.txt <<'PY'
import math
def sqf(s):
    return all(s % (p*p) for p in range(2, int(s**0.5)+1))
for s in range(13, 1001, 4):
    if math.gcd(s, 105) == 1 and sqf(s):
        print(s, math.isqrt((2**64 - 1) // s))
PY
ulimit -v 4000000
for L in 0 1 2 3; do
  ( awk -v L=$L 'NR % 4 == L' /tmp/ms105_slist.txt | while read s mm; do
      timeout 1800 /tmp/ms105_sm2 1 $mm 100000000 100000 $s
    done > data/z60/ms105/sm2/lane$L.txt; echo "lane $L exit $?" >> data/z60/ms105/sm2/lane$L.txt ) &
done
wait
