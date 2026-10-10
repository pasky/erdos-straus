"""O127: exact divisor-in-progression forms of ES (CONDITIONAL_ES.md §1).

Checks, for primes p <= X:
  (I1)  Type I, a=1 slice:  exists t>=1 and tp+1 = m*m2 with m = m2 = -1 (mod t), 4 | m.
        Equivalent: (c,f,g) with c(fg-1) - f = p, fg = 1 (mod 4); witness x=bdp,y=cd,z=bcd.
  (II1) Type II, a=1 slice: exists e>=1 and a divisor b of (p+e)/4 with b = -1 (mod e).
For each witness the ES triple is rebuilt and 4/p = 1/x+1/y+1/z is checked exactly.
Reports primes failing I1, failing II1, failing both.
Usage: PYTHONPATH=scripts uv run python scripts/cond_divisor_forms.py X
"""
import sys
from fractions import Fraction
from sympy import primerange, divisors


def check(p, x, y, z):
    assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z), (p, x, y, z)


def typeI_a1(p):
    # enumerate g=t; (g c - 1)(g f - 1) = g p + 1 ; need 4 | g f - 1
    for g in range(1, p + 3):
        N = g * p + 1
        if N % 4:
            continue
        for m in divisors(N):
            if m % g == g - 1 and m % 4 == 0 and (N // m) % g == g - 1:
                f = (m + 1) // g
                c = (N // m + 1) // g
                if c < 1 or f < 1:
                    continue
                d = m // 4
                # ET Sigma_I with a=1: 4bd = p e + 1 with e = g? rebuild via (a,b,c,d,e) = (1, b, c, d, e)
                # here 4cd = p + f, e f = 4d + 1, b = (p + c)/f
                assert 4 * c * d == p + f and g * f == 4 * d + 1
                assert (p + c) % f == 0
                b = (p + c) // f
                check(p, b * d * p, c * d, b * c * d)
                return (g, m, N // m)
    return None


def typeII_a1(p):
    # 4ab | p+e, e | a+b with a=1: b | (p+e)/4, b = -1 (mod e)
    for e in range(1, 3 * p):
        if (p + e) % 4:
            continue
        M = (p + e) // 4
        for b in divisors(M):
            if (b + 1) % e == 0:
                d = M // b  # 4*1*b*d = p+e
                c = (1 + b) // e
                # x = bd: 4/p - 1/(bd) = e/(pbd) = (1+b)/(pcbd) = 1/(pcbd) + 1/(pcd)
                check(p, b * d, c * d * p, b * c * d * p)
                return (e, b)
    return None


if __name__ == "__main__":
    X = int(sys.argv[1])
    fI, fII, both = [], [], []
    for p in primerange(3, X):
        a = typeI_a1(p)
        b = typeII_a1(p)
        if a is None:
            fI.append(p)
        if b is None:
            fII.append(p)
        if a is None and b is None:
            both.append(p)
    print("primes 3..%d" % X)
    print("fail TypeI a=1 :", len(fI), fI[:30])
    print("fail TypeII a=1:", len(fII), fII[:30])
    print("fail both      :", len(both), both[:30])
