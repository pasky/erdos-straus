"""fz_sum_check.py (O220): independent exact-integer re-implementation of the finite Case B part of (Σ) with the routes of
FF_STERILE_PUSH Lemma 1.6 + FF_STERILE_SMALL Lemmas 1.2-1.4 (written from the .md text, not from fz_sum.c; no Rankin
bound, so it should reproduce `fz_sum r S 1 1 1 0`). Per-pattern bounds are exact integers (min of routes), the per-s
term is an exact rational; the class bound uses its own (m, k) search m <= 80, m + k <= 300.
usage: fz_sum_check.py r S [print_every]"""
import sys
from fractions import Fraction as Fr
from math import comb, factorial
from functools import lru_cache

r = int(sys.argv[1]); S = int(sys.argv[2]); EV = int(sys.argv[3]) if len(sys.argv) > 3 else 10
q = 3**r
Ns = lambda d: 1 if d <= 0 else q**d - q**(d - 1)

@lru_cache(None)
def cop(n, d, rho):
    """least m + k with (C): n m(m+1)/2 + X (m(m+1)/2 + k m + k(k+1)/2) < (m+k+1) m d, X = d - rho >= 0 (Lemma 1.5)"""
    X = d - rho; best = None
    for m in range(1, 81):
        for k in range(0, 301 - m):
            if n * m * (m + 1) // 2 * 2 + X * (m * (m + 1) + 2 * k * m + k * (k + 1)) < 2 * (m + k + 1) * m * d:
                if best is None or m + k < best: best = m + k
                break
    return best

@lru_cache(None)
def cls(n, d, rho, both):
    """class-divisor bound (Lemmas 1.3-1.5 of FF_STERILE_PUSH), without refinement"""
    if d < rho or (both and n - d < rho): return 1
    c = []
    if 3 * rho > n: c.append(2)
    x = cop(n, d, rho)
    if x: c.append(x)
    if both:
        x = cop(n, n - d, rho)
        if x: c.append(x)
    c.append(comb(n, d))
    return min(c)

@lru_cache(None)
def clsr(n, d, rho, both):
    """FF_STERILE_SMALL Lemma 1.4: min_j q^j cls(n, d, rho + j)"""
    best = comb(n, d)
    for j in range(0, max(0, d - rho + 1) + 1):
        if q**j >= best: break
        best = min(best, q**j * cls(n, d, rho + j, both))
    return best

# omega*(e): max number of distinct monic irreducibles != T of total degree <= e
def nirr(j):
    mu = lambda m: 0 if any(m % (p * p) == 0 for p in range(2, int(m**.5) + 1)) else (-1)**sum(1 for p in range(2, m + 1) if m % p == 0 and all(p % u for u in range(2, int(p**.5) + 1)))
    return sum(mu(i) * q**(j // i) for i in range(1, j + 1) if j % i == 0) // j
IRR = [0] + [nirr(j) - (1 if j == 1 else 0) for j in range(1, 40)]
@lru_cache(None)
def omstar(e):
    om, left = 0, e
    for j in range(1, 40):
        tk = min(left // j, IRR[j]); om += tk; left -= tk * j
    return om
V = lambda e, d: q**(e - d) if d <= e else 1          # Lemma 1.3
def Som_all(e):                                         # sum over monic deg e of 2^omega (FF_STERILE_PUSH Lemma 1.6), as exact rational
    return 1 if e <= 0 else Fr(q**e) * (2 + (e - 1) * Fr(q - 1, q))
def Som_class(e, d):                                    # sum over a unit class mod D (deg d) of 2^omega
    a = V(e, d) * 2**omstar(max(e, 0))
    if d <= e:
        b = 2 * sum(max(q**j, q**(e - d)) for j in range(0, e // 2 + 1))
        a = min(a, b)
    return a

def bound(s, a, z, y, t):
    b = y + t; e = t - 2
    W, WB, Z, Y, Vt = Ns(a - 1), Ns(b - 1), Ns(z), Ns(y), Ns(t - 2)
    R = [Z * Y * W, Z * W * Vt, 2 * Y * Vt * Z, Y * Vt * W,
         Vt * (factorial(s - 2) // (factorial(z) * factorial(a - 1) * factorial(b - 1))),
         Z * Y * clsr(s + 2 * y + z, a + y + z, y + z + 1, 1),
         W * Y * clsr(s - 1 + y, a + y + z, a + y, 0),
         Z * W * clsr(s - 2, a + y + z, z + a, 1),
         WB * Y * clsr(s - 1 + y, b + y + z, b + y, 0),
         Z * WB * clsr(z + 2 * b - 2, b + y + z, z + b, 1),
         Vt * W * clsr(s - 1 - a, b - 1, t - 1, 1), Vt * WB * clsr(s - 1 - b, a - 1, t - 1, 1),
         Vt * comb(s - 2, a - 1) * clsr(s - 1 - a, b - 1, t - 1, 1), Vt * comb(s - 2, b - 1) * clsr(s - 1 - b, a - 1, t - 1, 1),
         Y * Vt * comb(s - 2, a - 1), Y * Vt * comb(s - 2, b - 1), Z * Vt * comb(a + b - 2, a - 1),
         Z * 2 * Som_all(e) * clsr(a + b - 2, a - 1, t - 1, 1),
         2 * Som_all(e) * comb(s - 2, z) * clsr(a + b - 2, a - 1, t - 1, 1),
         # FF_STERILE_SMALL Lemmas 1.2/1.3
         Z * V(e, z) * comb(a + b - 2, a - 1),
         Z * 2 * Som_class(e, z) * clsr(a + b - 2, a - 1, t - 1, 1),
         W * V(e, a - 1) * clsr(s - 1 - a, b - 1, t - 1, 1),
         WB * V(e, b - 1) * clsr(s - 1 - b, a - 1, t - 1, 1),
         2 * Y * Z * V(e, z), Y * W * V(e, a - 1), Z * W * V(e, z + a - 1)]
    return min(R)

tot = Fr(0)
for s in range(3, S + 1):
    acc = 0
    for a in range(1, s):
        for z in range(0, s - a):
            b = s - a - z
            if b < a: continue
            for y in range(0, b - 1):
                t = b - y
                acc += (1 if a == b else 2) * bound(s, a, z, y, t)
    term = Fr(acc, q**((s + 1) // 2 - 1))
    tot += term
    if s % EV == 0 or s == S: print(f"s={s} term={float(term):.10e} cum={float(tot):.12e}", flush=True)
print(f"r={r} S={S} exact total = {float(tot):.15e}")
