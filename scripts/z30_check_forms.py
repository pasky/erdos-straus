"""O260: brute-force checks of SINGLE_P_COUNT Lemma 1.1 (pair, divisor, SL2 forms) and Lemma 2.1 (genus split
R = Mg + X with Mg(m^2) = 0), for small n.  Exact rational arithmetic for the character split."""
from fractions import Fraction
from math import gcd
from sympy import primerange, factorint, totient
from sympy.ntheory import jacobi_symbol
import itertools, sys

def R_triples(n):
    r = 0
    for u in range(1, n + 2):
        if 3 * u - 1 > n: break
        for B in range(1, n + 2):
            if 4 * u * B - u - B > n: break
            if (n + u + B) % (4 * u * B) == 0: r += 1
    return r

def R_pairs(n):
    return sum(1 for u in range(1, n + 2) for B in range(1, (n + u) // max(1, 4 * u - 1) + 1)
               if gcd(u, B) == 1 and (n + u + B) % (4 * u * B) == 0)

def R_divisor(n):
    r = 0; half = 0
    for C in range(1, n + 2):
        N = 4 * C * n + 1
        for d in range(4 * C - 1, N + 1, 4 * C):
            if d * d > N and d > N: break
            if N % d == 0:
                r += 1
                if d * d < N: half += 1
            if d > N: break
    return r, half

def R_sl2(n):
    r = 0
    for c in range(4, 4 * n + 8, 4):
        # a = uc - 1, d = Bc - 1, ad - nc = 1
        for u in range(1, n + 2):
            a = u * c - 1
            if a > n * c + 1: break
            num = 1 + n * c
            if num % a == 0:
                d = num // a
                if d >= 1 and (d + 1) % c == 0: r += 1
    return r

def is_sq_unit(x, q):
    # x unit mod q (q = 2^k * odd); square iff square mod each prime power
    for l, e in factorint(q).items():
        if l == 2:
            m = min(2 ** e, 8)
            if e == 1: continue
            if e == 2:
                if x % 4 != 1: return False
            elif x % 8 != 1: return False
        else:
            if jacobi_symbol(x % l, l) != 1: return False
    return True

def Mg(n):
    tot = Fraction(0)
    for u in range(1, n + 2):
        if 3 * u - 1 > n: break
        for B in range(1, (n + u) // (4 * u - 1) + 1):
            if gcd(u, B) != 1 or (u + B) % 2 == 0: continue
            q = 4 * u * B; a = (-(u + B)) % q
            if gcd(n, q) != 1: continue
            phi = totient(q)
            s = 1
            for l, e in factorint(q).items():
                s *= 2 if l != 2 else (1 if e == 1 else (2 if e == 2 else 4))
            if is_sq_unit(n * a % q, q): tot += Fraction(s, phi)
    return tot

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    for p in primerange(3, N):
        rt, rp = R_triples(p), R_pairs(p)
        rd, half = R_divisor(p)
        rs = R_sl2(p)
        assert rt == rp == rd == rs == 2 * half, (p, rt, rp, rd, rs, half)
    print("Lemma 1.1 forms agree for all primes <", N)
    for m in range(3, 40, 2):
        assert R_triples(m * m) == 0 and Mg(m * m) == 0, m
    print("R(m^2) = Mg(m^2) = 0 for odd m < 40")
    for p in [101, 103, 113, 409, 577]:
        print(p, "R =", R_triples(p), "Mg = %.4f" % float(Mg(p)))
