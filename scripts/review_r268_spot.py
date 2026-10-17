"""R268 spot check in (1e7, 1e8]: for random primes p = 1 (4), find an explicit b = 1 witness via the divisor
form (factor p + 4d, d = 1, 2, ...) and an explicit c = 1 witness (a = 1, 2, ..., divisors of p + a), and verify
each witness by exact rational arithmetic 4/p = 1/x + 1/y + 1/z.  Also prints the witnesses at the 3 b=1 failures'
c = 1 line (the union claim) and at the 14 c = 1 failures' b = 1 line.
"""
import random
from fractions import Fraction as F
from sympy import isprime, divisors


def b1_witness(p):
    for d in range(1, (p + 3) // 8 + 1):
        n = p + 4 * d
        for w in divisors(n):
            if w < n and w % (4 * d) == 4 * d - 1:
                c = (w + 1) // (4 * d)
                assert (c * p + 1) % w == 0
                a = (c * p + 1) // w
                x, y, z = a * d, a * c * d * p, c * d * p
                assert F(1, x) + F(1, y) + F(1, z) == F(4, p)
                return (a, c, d)
    return None


def c1_witness(p):
    a = 1
    while a * (4 * a - 2) <= p:
        for b in divisors(p + a):
            if b >= a and (p + a + b) % (4 * a * b) == 0:
                d = (p + a + b) // (4 * a * b)
                assert F(1, a * b * d) + F(1, a * d * p) + F(1, b * d * p) == F(4, p)
                return (a, b, d)
        a += 1
    return None


if __name__ == "__main__":
    random.seed(268)
    ps = []
    while len(ps) < 400:
        p = random.randrange(10**7 + 1, 10**8, 4)
        if isprime(p):
            ps.append(p)
    nb = sum(b1_witness(p) is not None for p in ps)
    nc = sum(c1_witness(p) is not None for p in ps)
    print(f"random primes p=1(4) in (1e7,1e8]: {len(ps)}; b1 witness found & verified: {nb}; c1: {nc}")
    for p in [193, 2521, 66529]:
        print("b1-failure", p, "b1:", b1_witness(p), " c1 witness:", c1_witness(p))
    for p in [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]:
        print("c1-failure", p, "c1:", c1_witness(p), " b1 witness:", b1_witness(p))
