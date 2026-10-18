"""z43 (FABLE): verify the canonical two-line form

  ES(p)  <=>  exists m,u >= 1 such that  N = m p + u  has a divisor d with
              d == -1 (mod 4mu)   [Type II: two denominators divisible by p]
           or d == -p (mod 4mu)   [Type I : one denominator divisible by p]

against brute force over 4/p = 1/x+1/y+1/z, and the explicit reconstruction
of the unit fractions from (m,u,d).

Reconstruction:
  Type II: d = 4muw-1, v = N/d, e = (u+v)/m, p+e = 4uvw;
           4/p = 1/(uvw) + 1/(m p v w) + 1/(m p u w).
  Type I : d = 4muw-p, with (4muw-p) | (pm+u); set e = d, v = (pm+u)/d... see below.
"""
import sys
from fractions import Fraction
from sympy import primerange, divisors

def brute(p):
    hasI = hasII = False
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        num, den = 4 * x - p, p * x
        for y in range(den // num + 1, 2 * den // num + 1):
            n2 = num * y - den
            if n2 > 0 and (den * y) % n2 == 0:
                z = den * y // n2
                c = sum(1 for w in (x, y, z) if w % p == 0)
                if c == 1: hasI = True
                elif c == 2: hasII = True
    return hasI, hasII

def canon(p, B):
    """return (I_cert, II_cert) found with m,u <= B, each a verified unit-fraction triple or None"""
    cI = cII = None
    for m in range(1, B + 1):
        for u in range(1, B + 1):
            N = m * p + u
            M = 4 * m * u
            for d in divisors(N):
                if cII is None and d % M == M - 1:
                    w = (d + 1) // M
                    v = N // d
                    assert (u + v) % m == 0
                    e = (u + v) // m
                    assert p + e == 4 * u * v * w
                    tri = (u * v * w, m * p * v * w, m * p * u * w)
                    assert sum(Fraction(1, t) for t in tri) == Fraction(4, p)
                    cII = (m, u, d, tri)
                if cI is None and d % M == (-p) % M:
                    w = (d + p) // M
                    # d = 4 m u w - p divides p m + u ; h = (pm+u)/d
                    h = N // d
                    tri = (m * u * w, h * p * m * w, h * u * w)
                    assert sum(Fraction(1, t) for t in tri) == Fraction(4, p)
                    cI = (m, u, d, tri)
    return cI, cII

if __name__ == "__main__":
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    B = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    miss = 0
    for p in primerange(5, P):
        bI, bII = brute(p)
        cI, cII = canon(p, B)
        if (cI is not None) != bI or (cII is not None) != bII:
            print("mismatch", p, bI, bII, cI is not None, cII is not None); miss += 1
    print("done; mismatches:", miss)
