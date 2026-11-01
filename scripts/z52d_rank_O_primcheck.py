"""Sanity check of Z0866 lemma: for primes p≡1(4), Type I solutions (p divides exactly one denominator) are never primitive."""
from math import gcd
def primerange(a, b):
    return [n for n in range(a, b) if n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))]
bad = 0; tot = 0
for p in primerange(5, 400):
    if p % 4 != 1: continue
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        num, den = 4 * x - p, p * x            # 1/y+1/z = num/den, y<=z
        if num <= 0: continue
        for y in range(max(x, den // num + 1), 2 * den // num + 1):
            zn, zd = num * y - den, den * y
            if zn <= 0 or zd % zn: continue
            z = zd // zn
            k = sum(1 for t in (x, y, z) if t % p == 0)
            if k == 1:
                tot += 1
                if gcd(gcd(x, y), z) == 1: bad += 1; print('primitive Type I', p, x, y, z)
print('Type I solutions checked', tot, 'primitive', bad)
