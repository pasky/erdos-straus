#!/bin/bash
# z60 MS105: F2 sensitivity control — the same kernel census (106 kernels s <= 1000, n = s*m^2 < 2^64) for the C-even
# sub-line R8 (engine scripts/z60_ms105_sm2.c compiled with -DR8; LIM = 10^8; UNK = no R8 witness d <= 10^8).
gcc -O2 -march=native -DR8 -o /tmp/ms105_sm2_r8 scripts/z60_ms105_sm2.c || exit 1
python3 - > /tmp/ms105_slist.txt <<'PY'
import math
def sqf(s): return all(s % (p*p) for p in range(2, int(s**0.5)+1))
for s in range(13, 1001, 4):
    if math.gcd(s, 105) == 1 and sqf(s): print(s, math.isqrt((2**64 - 1) // s))
PY
ulimit -v 4000000
for L in 0 1 2; do
  ( rc=0; while read s mm; do
      timeout 1700 /tmp/ms105_sm2_r8 1 $mm 100000000 100000000000 $s || rc=1
    done < <(awk -v L=$L 'NR % 3 == L' /tmp/ms105_slist.txt) > data/z60/ms105/r8ctl/lane$L.txt
    echo "EXIT $rc" >> data/z60/ms105/r8ctl/lane$L.txt; exit $rc ) &
done
rc=0; for p in $(jobs -p); do wait $p || rc=1; done
[ $rc -eq 0 ] || echo "SOME LANE FAILED" >&2
exit $rc
