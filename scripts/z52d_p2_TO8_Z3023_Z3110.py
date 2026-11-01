# z52d P2 TO8: Z3023 (look-ahead greedy: least k with x=ceil(p/4)+k leaving a two-term-solvable remainder), Z3110 (new primes of 4Cp+1 with q ≡ -1 mod 4C)
import sys, math
from math import gcd
from sympy import factorint, primerange
def divisors_from_factor(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
def two_term(a, b):
    # is a/b = 1/y + 1/z solvable in positive integers? iff exists divisor d of b^2 with d ≡ -b (mod a), (b^2/d) ≡ -b (mod a)
    g = gcd(a, b); a //= g; b //= g
    if a == 1: return True  # 1/y+1/z = 1/b-type with y=z=2b handled below
    fb = factorint(b)
    f2 = {q: 2 * e for q, e in fb.items()}
    for d in divisors_from_factor(f2):
        if (d + b) % a == 0 and ((b * b // d) + b) % a == 0:
            return True
    return False
def least_k(p, kmax=200):
    x0 = -(-p // 4)
    for k in range(kmax):
        x = x0 + k
        a = 4 * x - p
        if a <= 0: continue
        b = p * x
        if two_term(a, b): return k
    return None
ps = [p for p in primerange(5, 3000) if p % 4 == 1]
res = {}
for p in ps:
    res[p] = least_k(p)
from collections import Counter
cnt = Counter(res.values())
print("Z3023: primes ≡1 (4), 5≤p<3000:", len(ps), " least-k distribution:", sorted(cnt.items(), key=lambda t: (t[0] is None, t[0] if t[0] is not None else 0)))
print("max least-k:", max(v for v in res.values() if v is not None), " at p:", [p for p in ps if res[p] == max(v for v in res.values() if v is not None)][:5])
print("primes with k>=3:", [(p, res[p]) for p in ps if res[p] is None or res[p] >= 3][:20])
# Z3110: new primes of 4Cp+1 relative to smaller levels; freq of q ≡ -1 mod 4C among new primes
for p in [409, 10009, 999029]:
    seen = set(); tot = 0; hit = 0
    for C in range(1, 301):
        N = 4 * C * p + 1
        f = factorint(N)
        for q in f:
            if q not in seen:
                seen.add(q); tot += 1
                if (q + 1) % (4 * C) == 0: hit += 1
    print(f"Z3110 p={p}: C<=300: new primes {tot}, with 4C | q+1 (certificate-type) {hit}, frequency {hit/tot if tot else 0:.3f}")
