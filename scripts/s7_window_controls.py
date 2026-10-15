"""s7_window_controls: T1 control (odd squares have no cap-0 window), composites (105, 3985),
and the Mordell split (m0 >= 11 only on the six Mordell-hard classes mod 840) up to N.
Usage: python s7_window_controls.py N MMAX
"""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from s7_window_excess import spf_sieve, m0

N = int(sys.argv[1]); MMAX = int(sys.argv[2])
spf = spf_sieve(N // 4 + MMAX + 10)
sq_bad = [a * a for a in range(3, int(N ** 0.5) + 1, 2) if m0(a * a, spf, MMAX) is not None]
print("odd squares <= N with a cap-0 window m <= %d:" % MMAX, sq_bad[:10], "count", len(sq_bad))
print("m0(105) =", m0(105, spf, MMAX), " m0(3985) =", m0(3985, spf, MMAX))
isp = bytearray([1]) * (N + 1); isp[0] = isp[1] = 0
for i in range(2, int(N ** 0.5) + 1):
    if isp[i]:
        isp[i * i::i] = bytearray(len(isp[i * i::i]))
MH = {1, 121, 169, 289, 361, 529}
viol = 0; mx = 0; cnt = 0; recs = []
for p in range(5, N + 1, 4):
    if not isp[p]:
        continue
    cnt += 1
    v = m0(p, spf, 4000)
    if v is None or v > mx:
        mx = v if v else mx; recs.append((p, v))
    if (v is None or v >= 11) and p % 840 not in MH:
        viol += 1
print("primes p≡1(4) <=", N, cnt, "; m0>=11 off Mordell-hard classes:", viol, "; records:", recs[-6:])
