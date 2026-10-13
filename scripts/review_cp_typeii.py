"""R203 from-scratch checks of COMPOSITION_ES Prop 4.1(b) and Prop 5.1, plus the '99 primes' count.
usage: review_cp_typeii.py PMAX [P99MAX]
"""
import sys
from fractions import Fraction as F
from math import isqrt, gcd
import mpmath

mpmath.mp.dps = 60
PMAX = int(sys.argv[1])
P99 = int(sys.argv[2]) if len(sys.argv) > 2 else 0

def primes_upto(m):
    s = bytearray([1]) * (m + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(m) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(m + 1) if s[i]]

def divisors(m):
    ds = [1]; q = 2
    while q * q <= m:
        if m % q == 0:
            e = 0
            while m % q == 0: m //= q; e += 1
            ds = [d * q**k for d in ds for k in range(e + 1)]
        q += 1
    if m > 1: ds += [d * m for d in ds]
    return ds

fails = 0
def check(c, msg):
    global fails
    if not c:
        fails += 1
        if fails < 20: print("FAIL", msg)

ncube = nes = 0
for p in primes_upto(PMAX):
    if p < 5: continue
    # cube points from the definition: c, d, s >= 1, j = (c+s)/(4cds - p) integer >= 1
    cube = set()
    for c in range(1, p + 2):
        for d in range(1, (p + 1) // (3 * c) + 2):
            if 4 * c * d - 1 <= 0: continue
            for s in range(1, (p + c) // (4 * c * d - 1) + 2):
                e = 4 * c * d * s - p
                if e > 0 and (c + s) % e == 0:
                    j = (c + s) // e
                    h = 4 * c * d * j - 1
                    check((p * j + c) % h == 0 and (4 * d * j * j * p + 1) % h == 0, ("cube def", p, c, d, j))
                    check(3 * c * d <= p + 1, ("3cd", p, c, d))
                    cube.add((c, d, j, s))
    # B = 1 points of V_{pd} with d | lambda, via A = 2j, g | n'A^2 + 1, g = -1 mod 2A
    es = set()
    for d in range(1, (p + 1) // 3 + 1):
        n2 = p * d
        for j in range(1, n2 + 2):
            A = 2 * j; M = n2 * A * A + 1
            for g in divisors(M):
                if (g + 1) % (2 * A): continue
                lam = (g + 1) // (2 * A); D = M // g; mu = lam * D
                if D < 1 or lam % d: continue
                check(n2 * A * A + 1 + D == 2 * mu * A, ("V eq", p, d, j))
                es.add((lam // d, d, j))
    check({(c, d, j) for (c, d, j, s) in cube} == es, ("Prop 4.1(b) bijection", p, len(cube), len(es)))
    ncube += len(cube); nes += len(es)
    # Prop 5.1 on all cube points
    for (c, d, j, s) in cube:
        check(4 * c * s * d * j == p * j + c + s, "(i)")
        # (ii) exact: (2cd + w)(2sd + w) with w^2 = -pd
        re, im = 4 * c * s * d * d - p * d, 2 * d * (c + s)
        k = F(d * (c + s), j)
        check(F(re) == k and F(im) == k * 2 * j, ("(ii)", p, c, d, j))
        # (iii) numerically
        acot = lambda x: mpmath.atan(1 / x)
        lhs = acot(2 * c * mpmath.sqrt(d) / mpmath.sqrt(p)) + acot(2 * s * mpmath.sqrt(d) / mpmath.sqrt(p))
        rhs = acot(1 / (2 * j * mpmath.sqrt(p * d)))
        check(abs(lhs - rhs) < mpmath.mpf(10) ** -50, ("(iii)", p, c, d, j))
        check(F(4, p) == F(1, c * d * s) + F(1, p * d * s * j) + F(1, p * d * c * j), "Egyptian")
        check((4 * c * d * j - 1) * (4 * s * d * j - 1) == 4 * d * j * j * p + 1, "norm-type identity")
        # norms of (ii): d^2 (4c^2 d + p)(4 s^2 d + p) j^2 = d^2 (c+s)^2 (1 + 4 j^2 p d)
        check((4*c*c*d + p) * (4*s*s*d + p) * j * j == (c + s)**2 * (1 + 4*j*j*p*d), "norm of (ii)")
        if d == 1:
            mu = c * (4 * s * j - 1)  # lambda = c, D = 4sj - 1 (Prop 4.1(b) map)
            check(mu == p * j + s and (s <= p) , ("t = s", p, c, j, s))
    # converse of Prop 5.1 on a box: (i) false => (iii) false
    for c in range(1, 6):
        for s in range(1, 6):
            for d in range(1, 4):
                for j in range(1, 4):
                    if 4*c*s*d*j != p*j + c + s:
                        lhs = mpmath.acot(2*c*mpmath.sqrt(mpmath.mpf(d)/p)) + mpmath.acot(2*s*mpmath.sqrt(mpmath.mpf(d)/p))
                        check(abs(lhs - mpmath.acot(1/(2*j*mpmath.sqrt(p*d)))) > mpmath.mpf(10)**-40, "(iii) converse")
print(f"primes <= {PMAX}: cube points {ncube}, d-sliced ES points {nes}, FAILS {fails}")

if P99:
    LIM = P99 + 4 * (isqrt(4 * P99) // 4 + 2) ** 2 + 10
    spf = list(range(LIM + 1))
    for i in range(2, isqrt(LIM) + 1):
        if spf[i] == i:
            for k in range(i * i, LIM + 1, i):
                if spf[k] == k: spf[k] = i
    def divs(m):
        ds = [1]
        while m > 1:
            q = spf[m]; e = 0
            while m % q == 0: m //= q; e += 1
            ds = [d * q**k for d in ds for k in range(e + 1)]
        return ds
    bad = []
    for p in primes_upto(P99):
        if p < 5: continue
        tmax = (1 + isqrt(4 * p + 1)) // 4 + 1
        ok = any((D + 1) % (4 * t) == 0 for t in range(1, tmax + 1) for D in divs(p + 4 * t * t))
        if not ok: bad.append(p)
    print(f"primes 5 <= p < {P99} with no d = 1 (B = 1, V_p) ES point: {len(bad)}; first: {bad[:8]}")
