"""z50 ncrt: verify the five certificate identities (EXSET_BEYOND_CRT §1.3 table), the Type I/II parameters,
the class memberships (R(M), Case A), and the U-atom identity of §3, by exact rational arithmetic on random words."""
import random
from fractions import Fraction as F
from math import gcd
random.seed(5)
def g_of(D):
    g, d, p = 1, D, 2
    while p * p <= d:
        e = 0
        while d % p == 0: d //= p; e += 1
        g *= p ** ((e + 1) // 2); p += 1
    if d > 1: g *= d
    return g
bad = 0; cnt = {}
for _ in range(200000):
    t, u, v = random.randint(1, 60), random.randint(1, 60), random.randint(1, 60)
    n = t * u * v - u - v
    if n < 1: continue
    four = F(4, n)
    def ok(x, y, z, lab):
        global bad
        cnt[lab] = cnt.get(lab, 0) + 1
        if min(x, y, z) <= 0 or F(1, x) + F(1, y) + F(1, z) != four: bad += 1; print("FAIL", lab, t, u, v)
    if t % 4 == 0:
        C = t // 4; ok(u * v * C, n * v * C, n * u * C, "4|t")
        # R-class: n = -4D mod M with M = 4Cv-1, D = C v^2
        M = 4 * C * v - 1
        if M > 1 and (n + 4 * C * v * v) % M: bad += 1; print("FAIL R 4|t")
        a, b, c, d = v, u, 1, C
        if 4 * a * b * c * d != a + b + c * n: bad += 1; print("FAIL typeII 4|t")
    if v % 4 == 0 and t * u > 1:
        w = v // 4; ok(w * (t * u - 1), n * t * w, n * t * w * (t * u - 1), "4|v")
        a, b, c, d = 1, t * u - 1, t, w
        if 4 * a * b * c * d != a + b + c * n: bad += 1; print("FAIL typeII 4|v")
    if u % 4 == 0 and t * v > 1:
        d = u // 4; ok(d * (t * v - 1), n * t * d, n * t * d * (t * v - 1), "4|u")
        a, b, c, dd = 1, t * v - 1, t, d
        if 4 * a * b * c * dd != a + b + c * n: bad += 1; print("FAIL typeII 4|u")
    if (t * v - 1) % 4 == 0 and t * v > 1 and t * u > 1:
        m = (t * v - 1) // 4; ok(m * u, m * u * (t * u - 1), n * m * (t * u - 1), "4|tv-1")
        a, b, c, d = 1, t * u - 1, u, m      # Type I: 4abcd = n(a+b) + c
        if 4 * a * b * c * d != n * (a + b) + c: bad += 1; print("FAIL typeI")
        G = 4 * g_of(m)
        if (n * t + 1) % G: bad += 1; print("FAIL CaseA class", t, u, v)
    if (t * u - 1) % 4 == 0 and t * u > 1 and t * v > 1:
        m = (t * u - 1) // 4; ok(m * v, m * v * (t * v - 1), n * m * (t * v - 1), "4|tu-1")
print("identity checks:", cnt, "failures:", bad)
# U-atom of §3: k=1 mod 4, prime l, 4w | kl+1, n = -4w mod kl  => word (t,u,4w), t=(kl+1)/(4w), u=(n+4w)/(kl)
from sympy import primerange
bad2 = tot2 = 0
for l in primerange(3, 400):
    for k in range(1, 60, 4):
        M = k * l
        for w in range(1, 40):
            if (M + 1) % (4 * w): continue
            t = (M + 1) // (4 * w)
            for u in range(2, 12):
                n = u * M - 4 * w
                if n < 1: continue
                tot2 += 1
                if t * u * 4 * w - u - 4 * w != n: bad2 += 1
                if F(1, w * (t * u - 1)) + F(1, n * t * w) + F(1, n * t * w * (t * u - 1)) != F(4, n): bad2 += 1
print("U-atom checks:", tot2, "failures:", bad2)
