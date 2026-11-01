# z53 HCSHIFTS: Theorem W (Dickson / Theorem-M wall) -- which primes ell are forced into the modulus of any
# Dickson-certified kill of the window-X predicate "no certificate with a coordinate in C_p ∩ [4,X]" (p = 1 mod 8).
# ell is FORCED iff the classes {0} ∪ {-x} ∪ {-x^{-1}} (x in C ∩ [4,X], endpoint resp. level forms) cover Z/ell.
# Prints X, log(prod of forced ell)/X, largest ell such that all odd primes <= ell are forced, and the endpoint-only
# variant (classes {0} ∪ {-x}).
import math, sys
from sympy import primerange
def C(X): return [x for x in range(4, X+1) if x % 4 == 0 or x % 8 == 7]
def forced(X, levels=True):
    cs = C(X); out = []
    for l in primerange(3, X+2):
        S = {0}
        for x in cs:
            S.add((-x) % l)
            if levels and x % l: S.add((-pow(x, -1, l)) % l)
        if len(S) == l: out.append(l)
    return out
print("X  log(prod forced)/X  contiguous_max  | endpoint-only: log/X contiguous_max")
for X in [16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:
    res = []
    for lev in (True, False):
        f = forced(X, lev); lp = sum(math.log(l) for l in f)
        cont = 2
        for l in primerange(3, X+2):
            if l in f: cont = l
            else: break
        res.append((lp / X, cont))
    print(X, "%.4f" % res[0][0], res[0][1], "|", "%.4f" % res[1][0], res[1][1])
