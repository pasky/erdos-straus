"""s7_typeII_free: odd non-square n ≡ 1 (4) with f_II(n) = 0, i.e. no cap-0 window m ≤ n
(a Type II solution has n/4 < x ≤ n/2, so m = 4x − n ≤ n). Usage: python s7_typeII_free.py N
"""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from s7_window_excess import spf_sieve, m0, factor
N = int(sys.argv[1])
spf = spf_sieve(N + 10)
out = []
for n in range(5, N + 1, 4):
    r = math.isqrt(n)
    if r * r == n:
        continue
    if m0(n, spf, n) is None:
        out.append((n, factor(n, spf)))
print("non-square n ≡ 1 (4) <=", N, "with f_II(n) = 0:", len(out))
for n, f in out[:60]:
    print(" ", n, f)
