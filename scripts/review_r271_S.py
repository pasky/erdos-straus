"""R271 from-scratch S(p): distinct slices g = 4ka-1, 4kb-1 of d = 1 meeting points a + b = k(4ab - p)
(equivalently q | 4k^2 p + 1 with q = -1 mod 4k); also checks the factorisations quoted in Cor 1.3(ii)."""
import sys
def S(p):
    sl = set()
    for a in range(1, p + 2):
        if 4 * a > p + a + 1: break
        for b in range(1, p + 2):
            if 4 * a * b > p + a + b: break
            g = 4 * a * b - p
            if g > 0 and (a + b) % g == 0:
                k = (a + b) // g
                assert (4*k*a - 1) * (4*k*b - 1) == 4*k*k*p + 1
                sl |= {4 * k * a - 1, 4 * k * b - 1}
    return len(sl)
print({p: S(p) for p in map(int, sys.argv[1:])})
from sympy import factorint
print({n: factorint(n) for n in (194, 2522, 66530)})
