"""R207: positive words tuv - u - v = n  <=>  (tu-1)(tv-1) = tn + 1.  For primes p: check |X(p)| odd (p>3),
unique sigma-fixed word, chi = (-(tu-1)/p) sigma-invariant, and parity of #chi=-1 sigma-orbits by p mod 8.
Odd squares: #chi=-1 words. Usage: N"""
import sys
from math import isqrt
from sympy import jacobi_symbol as J, isprime, divisors
N = int(sys.argv[1])
def words(n):
    W = []
    for t in range(1, n + 3):
        M = t * n + 1
        for a in divisors(M):
            b = M // a
            if (a + 1) % t == 0 and (b + 1) % t == 0:
                W.append((t, (a + 1) // t, (b + 1) // t))
    return W
tab = {}; bad = 0
for p in range(5, N):
    if not isprime(p): continue
    W = words(p)
    assert all(t * u * v - u - v == p for t, u, v in W)
    fixed = [w for w in W if w[1] == w[2]]
    if len(W) % 2 != 1 or fixed != [(p + 2, 1, 1)]: bad += 1
    if any(J(-(t*u-1), p) != J(-(t*v-1), p) for t, u, v in W): bad += 1
    orbits = {(t, min(u, v), max(u, v)) for t, u, v in W if J(-(t * u - 1), p) == -1}
    key = p % 8; tab.setdefault(key, [0, 0])[len(orbits) % 2] += 1
sq = sum(1 for m in range(3, isqrt(N) + 1, 2) for t, u, v in words(m * m) if J(-(t * u - 1), m * m) == -1)
print(f"N={N} defects={bad} parity of #chi=-1 orbits [even, odd] by p mod 8: {dict(sorted(tab.items()))}; "
      f"chi=-1 words at odd squares: {sq}")
