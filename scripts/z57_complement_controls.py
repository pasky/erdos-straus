# z57 COMPLEMENT: control lists.  usage: python z57_complement_controls.py KIND LO LEN [MAXCOUNT]
#   rough : composite non-square n ≡ 1 (mod 4) in [LO, LO+LEN) with least prime factor > n^0.4 (semiprimes q1*q2, q1 >= n^0.4)
#   all   : every n ≡ 1 (mod 4) in [LO, LO+LEN)  (for the small-n census)
import sys, math
import numpy as np
kind, lo, ln = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); mx = int(sys.argv[4]) if len(sys.argv) > 4 else 10**9
if kind == 'all':
    for n in range(lo + ((1 - lo) % 4), lo + ln, 4): print(n)
    sys.exit()
hi = lo + ln; r = math.isqrt(hi) + 1
sv = np.ones(r + 1, bool); sv[:2] = False
for i in range(2, math.isqrt(r) + 1):
    if sv[i]: sv[i * i::i] = False
P = np.nonzero(sv)[0]
lpf = np.zeros(ln, np.int64)
for q in P:
    st = (-lo) % q
    seg = lpf[st::q]; seg[seg == 0] = q; lpf[st::q] = seg
cnt = 0
for i in range(ln):
    n = lo + i
    if n % 4 != 1 or lpf[i] == 0: continue          # lpf 0 => prime (no factor <= sqrt)
    if lpf[i] < n ** 0.4: continue
    m = math.isqrt(n)
    if m * m == n: continue
    print(n); cnt += 1
    if cnt >= mx: break
