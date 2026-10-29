"""z50 ncrt Round 4 numerics.
(1) Prop R4.5 as a decision procedure: for C = a mod M (8 | M, a = 1 mod 4) and a U-admissible endpoint v
    (v = 0 mod 4 or v = -a mod 8), decide 'single-shift forced up to valuation depth J' by the witness rule
    (delta | D_j, delta > 1, delta = -1 mod v) or (delta | D_j, delta < D_j, delta*rho = -1 mod v) for every
    admissible unit rho mod v; then brute-force: every n in C, n <= NMAX, outside the depth-J tail and n >= n0, must
    have a U-word with endpoint v.  (2) Compactness illustration for C = 17 mod 24: number of n in C (n <= NMAX2)
    lying in no U-word class of grouping modulus <= T.
Usage: python3 z50_ncrt_r4.py NMAX NMAX2"""
import sys
from math import gcd
NMAX, NMAX2 = int(sys.argv[1]), int(sys.argv[2])
def divisors(x):
    out = []; d = 1
    while d * d <= x:
        if x % d == 0:
            out.append(d)
            if d * d != x: out.append(x // d)
        d += 1
    return out
def primes_of(x):
    ps = []; p = 2
    while p * p <= x:
        if x % p == 0:
            ps.append(p)
            while x % p == 0: x //= p
        p += 1
    if x > 1: ps.append(x)
    return ps
def uword_at(n, v):
    m = n + v
    for A in divisors(m):
        if 1 < A < m and (A + 1) % v == 0:
            t, u = (A + 1) // v, m // A
            if t * u - 1 > 1: return (t, u, v)
    return None
J = 5
def decide(a, M, v):
    D = gcd(a + v, M); Mp = M // D; rp = ((a + v) // D) % Mp if Mp > 1 else 0
    ps = primes_of(v)
    import itertools
    for js in itertools.product(range(J + 1), repeat=len(ps)):
        if any(j > 0 and Mp % p == 0 for p, j in zip(ps, js)): continue
        Dj = D
        for p, j in zip(ps, js): Dj *= p ** j
        if any((a + v) % 1 for _ in [0]): pass
        # units rho mod v; compatible with m = r' mod M' : m = prod p^j * m_j, m_j = rho (mod v)
        for rho in range(1, v + 1):
            if gcd(rho, v) != 1: continue
            P = Dj // D
            g = gcd(Mp, v)
            if g > 1 and (P * rho - rp) % g: continue
            ok = any(dl > 1 and (dl + 1) % v == 0 for dl in divisors(Dj)) or \
                 any(dl < Dj and (dl * rho + 1) % v == 0 for dl in divisors(Dj))
            if not ok: return False
    return True
forced = []; tested = 0
for M in [8, 24, 40, 56, 72, 120, 168]:
    for a in range(1, M, 4):
        vs = [v for v in range(1, 41) if v % 4 == 0 or (v + a) % 8 == 0]
        for v in vs:
            tested += 1
            if decide(a, M, v): forced.append((a, M, v))
print("(1) progressions x shifts tested:", tested, " decided single-shift-forced:", len(forced))
bad = 0; checked = 0
for a, M, v in forced:
    D = gcd(a + v, M)
    for n in range(a, NMAX, M):
        if n < 50: continue
        m = (n + v) // D
        if any(m % (p ** (J + 1)) == 0 for p in primes_of(v)): continue   # depth-J tail (remainder)
        checked += 1
        if uword_at(n, v) is None: bad += 1; print("  counterexample", a, M, v, n)
print("    brute-force check of all n <= %d in forced (C, v), outside the tail: %d checked, %d without a word" % (NMAX, checked, bad))
print("    sample forced:", forced[:12])
# (2) compactness illustration
def min_grouping_modulus_U(n):
    best = None; t = 1
    while t <= 2 * n + 4:
        mm = t * n + 1; a = t - 1 if t >= 2 else t
        while a * a <= mm:
            if a >= 1 and mm % a == 0:
                b = mm // a
                if (b + 1) % t == 0 and (a + 1) % t == 0:
                    u, v = (a + 1) // t, (b + 1) // t
                    if u >= 1 and v >= 1 and a > 1 and b > 1:
                        if any(e % 4 == 0 or (e + n) % 8 == 0 for e in (u, v)):
                            g = min(u * v, a, b)
                            best = g if best is None else min(best, g)
            a += t
        t += 1
    return best
Ts = [10, 30, 100, 300, 1000]
cnt = {T: 0 for T in Ts}; tot = 0; noword = 0
for n in range(17, NMAX2, 24):
    if n < 1000: continue
    tot += 1
    g = min_grouping_modulus_U(n)
    if g is None: noword += 1; continue
    for T in Ts:
        if g > T: cnt[T] += 1
print("(2) C = 17 mod 24, n in [1000,%d): %d integers, %d without any U-word" % (NMAX2, tot, noword))
for T in Ts: print("    cheapest U-word grouping modulus > %4d: %d integers" % (T, cnt[T]))
