"""R268: table rows 'support-1 prime s' (b=1 solution with a prime) and 'D-form, prime divisor' (b=1 solution with
w = 4cd-1 prime) — failures among primes p = 1 (4) <= 1e6; plus max least t of the b=1 line."""
import numpy as np
from sympy import primerange, isprime
fa = fw = 0; mx = (0, 0)
for p in primerange(5, 10**6 + 1):
    if p % 4 != 1: continue
    t = np.arange(1, (p + 1) // 3 + 1, dtype=np.int64)
    g = (-p) % (4 * t)
    hit = np.nonzero((t + 1) % g == 0)[0]
    if len(hit) == 0: continue
    if t[hit[0]] > mx[0]: mx = (int(t[hit[0]]), p)
    oka = okw = False
    for i in hit:
        T, G = int(t[i]), int(g[i]); c = (T + 1) // G; d = (p + G) // (4 * T); w = 4 * c * d - 1
        assert (c * p + 1) % w == 0
        a = (c * p + 1) // w
        oka |= isprime(a); okw |= isprime(w)
        if oka and okw: break
    fa += not oka; fw += not okw
print("support-1 (a prime) failures <=1e6 (excl. the 3 b=1 failures):", fa, "; D-form prime-w failures:", fw, "; max least t:", mx)
