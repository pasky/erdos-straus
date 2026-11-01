# Z2048/Z2747 check: every (★) certificate M = 4uC-1 | p+u is a quadratic non-residue mod p (p ≡ 1 mod 4).
from sympy import primerange, legendre_symbol
bad = tot = 0
for p in primerange(5, 20000):
    if p % 4 != 1: continue
    for u in range(1, p):
        # M = 4uC-1 <= p+u
        C = 1
        while 4*u*C - 1 <= p + u:
            M = 4*u*C - 1
            if (p + u) % M == 0 and M % p:
                tot += 1
                if legendre_symbol(M % p, p) != -1: bad += 1
            C += 1
        if 4*u - 1 > p + u: break
print("certificates", tot, "with (M/p) != -1:", bad)
