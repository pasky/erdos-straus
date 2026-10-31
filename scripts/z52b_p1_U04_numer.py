"""Z0742 check: U_m(p) := #{x<=y<=z positive : m/p = 1/x+1/y+1/z} for m in {4,8,12,20}, p≡1 mod 4, p<=PMAX.
x ranges over [ceil(p/m), floor(3p/m)]; for each x, a/b = (m x - p)/(p x) reduced, two-term count via divisors of b'^2.
Memory: divisor lists only. Run under ulimit -v 4000000."""
import sys, json
from math import gcd
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def divs(fac):
    ds = [1]
    for q, e in fac.items(): ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
def U(p, m):
    tot = 0
    for x in range(-(-p // m), (3 * p) // m + 1):
        a, b = m * x - p, p * x
        if a <= 0: continue
        g = gcd(a, b); a1, b1 = a // g, b // g
        fac = {q: 2 * e for q, e in factor(b1).items()}
        for d in divs(fac):
            if (d + b1) % a1: continue
            y = (d + b1) // a1
            dd = b1 * b1 // d
            if (dd + b1) % a1: continue
            z = (dd + b1) // a1
            if x <= y <= z: tot += 1
    return tot
def isprime(n): return n > 1 and all(n % q for q in range(2, int(n**0.5) + 1))
P = [p for p in range(5, PMAX + 1) if p % 4 == 1 and isprime(p)]
rows = {}
for p in P:
    rows[p] = {m: U(p, m) for m in (4, 8, 12, 20)}
json.dump({str(p): v for p, v in rows.items()}, open(f'data/z52b/pass1/U04/numer_U_{PMAX}.json', 'w'))
import statistics as st
for m in (8, 12, 20):
    rat = [rows[p][m] / rows[p][4] for p in P if rows[p][4] > 0]
    zeros = [p for p in P if rows[p][m] == 0]
    print(f"m={m}: mean U_m/U_4 = {st.mean(rat):.4f}, median {st.median(rat):.4f}; zero-count primes {len(zeros)} {zeros[:10]}")
print('n_primes', len(P), 'U4 zero:', [p for p in P if rows[p][4] == 0][:10])
print('hard check 193,577,2521:', {p: rows[p] for p in (193, 577, 2521) if p in rows})
