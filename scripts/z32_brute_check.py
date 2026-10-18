"""O262: brute-force check of z32_ladder (Type II count for m/p) on small primes.
Enumerates all x<=y<=z with m/p = 1/x+1/y+1/z and counts Type II ones (p∤x, p|y, p|z; x may sit anywhere in the
sorted triple), with weight 2 if y != z (ordered (y,z) among the two p-multiples), 1 if equal."""
import sys, numpy as np
from fractions import Fraction
from sympy import primerange
def brute(m, p):
    tot = 0; r = Fraction(m, p)
    for x in range(p//m + 1, 3*p//m + 2):
        r1 = r - Fraction(1, x)
        if r1 <= 0: continue
        for y in range(max(x, int(1/r1) + 1), int(2/r1) + 1):
            r2 = r1 - Fraction(1, y)
            if r2 <= 0 or r2.numerator != 1 or r2.denominator < y: continue
            z = r2.denominator; t = (x, y, z)
            mult = [v for v in t if v % p == 0]; non = [v for v in t if v % p]
            if len(mult) == 2 and len(non) == 1:
                tot += 1 if mult[0] == mult[1] else 2
    return tot
for m in (4, 5, 7, 8):
    X = 3000
    import subprocess; subprocess.run(['/tmp/z32/z32_ladder', str(m), str(X), '/tmp/z32/chk.bin'], check=True)
    c = np.fromfile('/tmp/z32/chk.bin', dtype=np.uint32)
    bad = [(p, int(c[p]), brute(m, p)) for p in primerange(m+1, 400) if c[p] != brute(m, p)]
    print(m, 'mismatches', bad[:5])
