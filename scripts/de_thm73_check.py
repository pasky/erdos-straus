"""O168 Thm 7.3 check: primes p ≡ 1 (mod M_E) have no block witness at Type II slices e <= E."""
import sys
from math import lcm
from sympy import isprime, factorint, primerange
from de_joint_slices import witnesses


def M_E(E):
    M = 1
    for i in range(1, E + 1):
        M = lcm(M, i)
    for l in primerange(2, (E + 1) // 4 + 1):
        k = 0
        while l ** (k + 1) <= (E + 1) / 4:
            k += 1
        M = lcm(M, l ** (k + 3) if l == 2 else l ** (k + 1))
    return M


def block_ok(p, e, E):
    N = (p + e) // 4
    fac = factorint(N)
    sm = {l: k for l, k in fac.items() if l <= (E + 1) / 4}
    P = N
    for l, k in sm.items():
        P //= l ** k
    blk = dict(sm)
    if P > 1:
        blk[P] = 1
    return next(witnesses(N, e, blk), None) is not None


for E in map(int, sys.argv[1:]):
    M = M_E(E)
    tested = viol = 0
    p = 1
    while tested < 20:
        p += M
        if isprime(p):
            tested += 1
            viol += any(block_ok(p, e, E) for e in range(3, E + 1, 4))
    print(f"E={E} M_E={M} tested primes={tested} violations={viol} (last p={p})")
