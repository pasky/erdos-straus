"""O170 Prop 4.1 check: n = 1 mod 4, t = 3 mod 4, tn+1 = m m'' with 4 | m.
Claim: m'' = +1 (mod t) => (m''/n) = +1 ; m'' = -1 (mod t) => (m''/n) = -1."""
from sympy import jacobi_symbol, divisors
stats = {}
for n in range(5, 4001, 4):
    for t in range(3, n + 3, 4):
        N = t * n + 1
        for m in divisors(N):
            if m % 4:
                continue
            mpp = N // m
            for cls in (1, -1):
                if (mpp - cls) % t == 0:
                    key = (cls, jacobi_symbol(mpp, n))
                    stats[key] = stats.get(key, 0) + 1
print(stats)
