"""R256: Type-II-free non-squares n = 1 (4) <= N all of whose prime factors are = 1 (4) (claim: only 3985 below 1e6)."""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from math import gcd, isqrt
from review_r256_m0 import spf_sieve, factor, window_fires
N = int(sys.argv[1]); spf = spf_sieve(N)
out = []
for n in range(5, N + 1, 4):
    r = isqrt(n)
    if r*r == n or any(q % 4 != 1 for q in factor(n, spf)):
        continue
    if not any(gcd((n + m)//4, n) == 1 and window_fires((n + m)//4, m, spf) for m in range(3, n + 1, 4)):
        out.append(n)
print('N', N, 'Type-II-free non-squares with all prime factors = 1 (4):', out)
