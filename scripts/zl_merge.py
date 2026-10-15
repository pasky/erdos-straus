"""zl_merge.py -- O228 (STERILE_LOWER.md §6): merge split zl_sweep runs (ZL_BIN dumps over the same [X0, X1)) by adding the
per-prime counters, and print the same cell lines "C j lo hi maxP maxQ maxPQ nprimes" as zl_sweep (cells [2^{j/q}, 2^{(j+1)/q})
with exact integer endpoints: lo = least n with n^q >= 2^j).  Fails closed (exit 1) on a saturated counter (65535).
Usage: python3 zl_merge.py X0 X1 q bin1 [bin2 ...]"""
import sys, array
X0, X1, q = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
if X0 % 2 == 0: X0 += 1
M = (X1 - X0 + 1) // 2 + 1
JP = [0] * M; JQ = [0] * M
for fn in sys.argv[4:]:
    a = array.array('H'); a.frombytes(open(fn, 'rb').read())
    if len(a) != 2 * M: sys.exit(f"{fn}: size {len(a)} != {2 * M}")
    if 65535 in a: sys.exit(f"{fn}: saturated counter")
    for i in range(M):
        JP[i] += a[i]; JQ[i] += a[M + i]
def iroot_ceil(j):                     # least n >= 1 with n^q >= 2^j
    n = max(1, int(2 ** (j / q)) - 2)
    while n ** q < 2 ** j: n += 1
    return n
from sympy import isprime
j = (X0.bit_length() - 1) * q - 1
while True:
    lo, hi = iroot_ceil(j), iroot_ceil(j + 1)
    if lo >= X1: break
    lo2, hi2 = max(lo, X0), min(hi, X1)
    if lo2 < hi2:
        mp = mq = ms = cnt = 0
        for n in range(lo2 | 1, hi2, 2):
            i = (n - X0) >> 1
            if JP[i] == 0 and JQ[i] == 0 and not isprime(n): continue
            cnt += 1; mp = max(mp, JP[i]); mq = max(mq, JQ[i]); ms = max(ms, JP[i] + JQ[i])
        print(f"C {j} {lo2} {hi2} {mp} {mq} {ms} {cnt}")
    j += 1
