# z53_thin15_solve.py — explicit ES certificates for n = 15*2^s + 1, s = 60t, t = T0..T1 (Z53_THIN15.md §5).
# For each n: try m = 3, 7, 11, ... (m = 4x - n, x = (n+m)/4); let S = B-smooth part of x (primes < B, via gcd with a
# primorial).  Any two divisors d1, d2 of S (hence of N = n x) with m | d1 + d2 give
#   y = N k / d1, z = N k / d2, k = (d1 + d2)/m,   4/n = 1/x + 1/y + 1/z.
# Output line per t: "t m d1 d2" (compact certificate); checked separately by z53_thin15_check.py.
# Usage: z53_thin15_solve.py T0 T1 [B] [MMAX]
import sys, gmpy2
from gmpy2 import mpz
T0, T1 = int(sys.argv[1]), int(sys.argv[2])
B = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
MMAX = int(sys.argv[4]) if len(sys.argv) > 4 else 4000
def primes_upto(m):
    s = bytearray([1]) * (m + 1); s[0:2] = b'\x00\x00'
    for i in range(2, int(m ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(2, m + 1) if s[i]]
PR = primes_upto(B)
PRIM = mpz(1)
for q in PR: PRIM *= q
def smooth_factors(x):
    g = gmpy2.gcd(x, PRIM); fac = []
    if g == 1: return fac
    for q in PR:
        if g % q == 0:
            e = 0
            while x % q == 0: x //= q; e += 1
            fac.append((q, e))
            g //= q
            while g % q == 0: g //= q
            if g == 1: break
    return fac
def divisors(fac, cap=200000):
    ds = [1]
    for q, e in fac:
        new = []
        for d in ds:
            v = d
            for _ in range(e + 1):
                new.append(v); v *= q
        ds = new
        if len(ds) > cap: break
    return ds
def solve(n):
    for m in range(3, MMAX, 4):
        x = (n + m) // 4
        fac = smooth_factors(x)
        if not fac: continue
        ds = divisors(fac)
        res = {}
        for d in ds: res.setdefault(d % m, d)
        for d in ds:
            r = (-d) % m
            if r in res: return m, d, res[r]
    return None
for t in range(T0, T1 + 1):
    n = 15 * (mpz(1) << (60 * t)) + 1
    sol = solve(n)
    if sol is None: print(t, 'NONE', flush=True)
    else: print(t, *sol, flush=True)
