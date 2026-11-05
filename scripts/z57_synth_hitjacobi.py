# z57 SYNTH: sanity check of Lemma A.1 (hit classes are Jacobi non-residues): for every d = 3 (4), 3 <= d <= DMAX and every
# k | (d+1)/4, the class -k mod d has Jacobi symbol (-k/d) = -1.  Also checks gcd(k, d) = 1.  Exact integer arithmetic.
import sys
from math import gcd
def jacobi(a, n):
    a %= n; t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: t = -t
        a %= n
    return t if n == 1 else 0
DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
bad = 0; cnt = 0
for d in range(3, DMAX + 1, 4):
    m = (d + 1) // 4
    k = 1
    while k * k <= m:
        if m % k == 0:
            for kk in {k, m // k}:
                cnt += 1
                if gcd(kk, d) != 1 or jacobi(-kk, d) != -1: bad += 1; print('BAD', d, kk)
        k += 1
print(f'DMAX={DMAX} classes checked={cnt} violations={bad}')
