# z52d avenue Q18 (Z0511, Z0624): size of ES solutions at primes.
# For each prime p <= PMAX: all 4/p = 1/x+1/y+1/z, x<=y<=z. Report max z/p^2 over all
# solutions and min over solutions of log(z)/log(p) (smallest achievable max denominator).
import math, sys
from sympy import primerange
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
worst_ratio = 0; worst_min_exp = 0; rows = []
for p in primerange(5, PMAX):
    maxz = 0; minmax = None
    for x in range(p // 4 + 1, (3 * p) // 4 + 2):
        num = 4 * x - p          # 4/p - 1/x = num/(p x)
        if num <= 0: continue
        den = p * x
        ylo = max(x, den // num + 1)
        yhi = (2 * den) // num
        for y in range(ylo, yhi + 1):
            n2 = num * y - den   # num/den - 1/y = n2/(den y)
            if n2 <= 0: continue
            d2 = den * y
            if d2 % n2 == 0:
                z = d2 // n2
                if z < y: continue
                maxz = max(maxz, z)
                minmax = z if minmax is None else min(minmax, z)
    r = maxz / p**2; e = math.log(minmax) / math.log(p)
    rows.append((p, r, e, math.log(maxz)/math.log(p), minmax/p**2))
    worst_ratio = max(worst_ratio, r); worst_min_exp = max(worst_min_exp, e)
print("primes", len(rows), "max over p of (max z)/p^2 =", round(worst_ratio, 4))
print("max over p of min-solution log z/log p =", round(worst_min_exp, 4))
print("max log(max z)/log p =", round(max(t[3] for t in rows),3), "at", max(rows,key=lambda t:t[3])[0]); print("max over p of (min max-denominator)/p^2 =", round(max(t[4] for t in rows),4), "at", max(rows,key=lambda t:t[4])[0])
big = sorted(rows, key=lambda t: -t[2])[:8]
print("largest min-exponents:", [(p, round(e, 3)) for p, _, e, *_ in big])
print("p=1 mod 24 largest min-exp:", [(p, round(e, 3)) for p, _, e, *_ in big if p % 24 == 1][:5])
