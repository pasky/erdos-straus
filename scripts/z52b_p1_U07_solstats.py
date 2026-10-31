#!/usr/bin/env python3
"""Z0953/Z0954/Z0975 (U07): full solution sets of 4/p = 1/x+1/y+1/z (x<=y<=z) for primes p<=PMAX,
via x-enumeration + divisor method ((ay-b)(az-b)=b^2 with a/b = (4/p - 1/x) reduced).
Records per prime: #solutions, min z/x, min (y-x), min (z-y), histogram of x/p (in 10 bins over [1/4,3/4])."""
import sys, json, math, time, resource
resource.setrlimit(resource.RLIMIT_AS, (4_000_000_000, 4_000_000_000))
from sympy import primerange, divisors
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
out = {}
t0 = time.time()
def sols(p):
    res = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        num, den = 4 * x - p, p * x
        if num <= 0 or x * 1 > 3 * p: continue
        g = math.gcd(num, den); a, b = num // g, den // g
        if 3 * p < 4 * x: continue
        b2 = b * b
        for d in divisors(b2):
            # y = (b+d)/a must be integer, y >= x
            if (b + d) % a: continue
            y = (b + d) // a
            if y < x: continue
            e = b2 // d
            if (b + e) % a: continue
            z = (b + e) // a
            if z < y: continue
            res.append((x, y, z))
    return res
for p in primerange(5, PMAX + 1):
    S = sols(p)
    if not S:
        out[p] = None; continue
    out[p] = dict(n=len(S), minzx=min(z / x for x, y, z in S), miny_x=min(y - x for x, y, z in S),
                  minz_y=min(z - y for x, y, z in S),
                  hist=[sum(1 for x, y, z in S if int(10 * (x / p - 0.25) / 0.5) == k) for k in range(10)])
print("time", round(time.time() - t0, 1), "primes", len(out), "no-solution primes", [p for p in out if out[p] is None])
json.dump({str(k): v for k, v in out.items()}, open("data/z52b/pass1/U07/solstats_%d.json" % PMAX, "w"))
