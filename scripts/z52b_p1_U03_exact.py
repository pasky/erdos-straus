"""z52b Pass-1 U03: exact small searches.
(a) m/p = 1/x+1/y+1/z failures for m in {12,15,20,24}, primes p<=PMAX (exhaustive over x in (p/m, 3p/m]; 2-term step by divisors of b^2).
(b) Z2038: 4/p = 1/x + 1/(kx) + 1/z (z free): exact via D=4kx-p(k+1) | p^2(k+1)  (D | 4pkx and D | p^2(k+1)).
(c) Z0119: AP denominators x,x+d,x+2d for 4/p, p<=4000, exact quadratic in d for each x in (p/4, 3p/4].
Usage: uv run python scripts/z52b_p1_U03_exact.py PMAX
"""
import sys, math, json
from math import gcd, isqrt
PMAX = int(sys.argv[1])
def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\x00\x00"
    for i in range(2, isqrt(n) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]
def fac_small(n):
    f = {}; q = 2
    while q * q <= n:
        while n % q == 0: f[q] = f.get(q, 0) + 1; n //= q
        q += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def divisors(f):
    ds = [1]
    for q, e in f.items(): ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
def two_term(a, b, fb2):
    # does a/b = 1/y+1/z have a positive solution? fb2 = factorization of b^2
    for D in divisors(fb2):
        if (D + b) % a == 0:
            Z = (b * b // D + b)
            if Z % a == 0 and Z // a >= 1 and (D + b) // a >= 1: return True
    return False
def m_over_p_solvable(m, p):
    lo = p // m + 1; hi = (3 * p) // m
    for x in range(lo, hi + 1):
        num = m * x - p; den = p * x
        if num <= 0: continue
        g = gcd(num, den); a, b = num // g, den // g
        fb = fac_small(b); fb2 = {q: 2 * e for q, e in fb.items()}
        if two_term(a, b, fb2): return (x,)
    return None
pr = [p for p in primes_upto(PMAX) if p % 2 == 1]
out = {"m_over_p": {}, "Z2038": {}, "Z0119": []}
for m in [4, 12, 15, 20, 24]:
    fails = [p for p in pr if p > m and m_over_p_solvable(m, p) is None]
    out["m_over_p"][m] = fails
    print("m", m, "failures p<=", PMAX, len(fails), fails[:40], flush=True)
# (b)
for k in [1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20]:
    hit = 0; ex = None
    for p in pr:
        f = fac_small(p * p * (k + 1)); ok = None
        for D in divisors(f):
            if (D + p * (k + 1)) % (4 * k) == 0:
                x = (D + p * (k + 1)) // (4 * k)
                if x >= 1 and (p * k * x) % D == 0:
                    ok = (x, p * k * x // D); break
        if ok: hit += 1; ex = ex or (p, ok)
    out["Z2038"][k] = (hit, len(pr), ex)
    print("Z2038 k", k, "solvable", hit, "/", len(pr), "example", ex, flush=True)
# (c) AP
ap = []
for p in pr:
    if p > 4000: break
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        s = 4 * x - p; M = p * x
        A = 2 * s; B = 3 * x * s - 3 * M; Cc = s * x * x - 2 * M * x
        if A == 0: continue
        disc = B * B - 4 * A * Cc
        if disc < 0: continue
        r = isqrt(disc)
        if r * r != disc: continue
        for num in (-B + r, -B - r):
            if num % (2 * A) == 0:
                d = num // (2 * A)
                if d >= 1: ap.append((p, x, d))
out["Z0119"] = ap
print("Z0119 AP solutions p<=4000:", len(ap), ap[:5], flush=True)
json.dump(out, open("data/z52b/pass1/U03/exact_results.json", "w"))
