#!/bin/bash
# z60 MS105: (a) m-windows beyond 2^64 for the 106 kernels s <= 1000: m in [10^k, 10^k + 2*10^7], k = 10..17
#            (n = s*m^2 up to ~10^37), engine scripts/z60_ms105_sm2w.c, LIM = 10^8, LATE = 10^6; 2 lanes (k parity).
#            (b) near squares n = m^2 + c, c in +-{8, 16, ..., 200}, odd m <= 10^9, engine scripts/z60_ms105_nsq.c;
#            2 lanes (sign of c).  Outputs data/z60/ms105/win/ and data/z60/ms105/nsq/.
gcc -O2 -march=native -o /tmp/ms105_sm2w scripts/z60_ms105_sm2w.c || exit 1
gcc -O2 -march=native -o /tmp/ms105_nsq scripts/z60_ms105_nsq.c -lm || exit 1
mkdir -p data/z60/ms105/win data/z60/ms105/nsq
S=$(python3 -c "
import math
def sqf(s): return all(s % (p*p) for p in range(2, int(s**0.5)+1))
print(' '.join(str(s) for s in range(13,1001,4) if math.gcd(s,105)==1 and sqf(s)))")
ulimit -v 4000000
for P in 0 1; do
  ( for k in 10 11 12 13 14 15 16 17; do
      [ $((k % 2)) -eq $P ] || continue
      lo=$(python3 -c "print(10**$k)"); hi=$(python3 -c "print(10**$k + 2*10**7)")
      timeout 1700 /tmp/ms105_sm2w $lo $hi 100000000 1000000 $S || echo "FAIL k=$k"
    done > data/z60/ms105/win/lane$P.txt; echo "EXIT $?" >> data/z60/ms105/win/lane$P.txt ) &
done
( timeout 1700 /tmp/ms105_nsq 1 1000000000 100000000 1000000 $(seq 8 8 200) > data/z60/ms105/nsq/pos.txt; echo "EXIT $?" >> data/z60/ms105/nsq/pos.txt ) &
( timeout 1700 /tmp/ms105_nsq 1 1000000000 100000000 1000000 $(seq -8 -8 -200) > data/z60/ms105/nsq/neg.txt; echo "EXIT $?" >> data/z60/ms105/nsq/neg.txt ) &
wait
