"""rt_slice_special.py (O125, Phase 2 on O127).
(A) Odd-square test T1 for the slice (I1) of CONDITIONAL_ES Lemma 1.1: for odd n = m^2, list slice
    solutions (c,f,g) with cfg - c - f = n, fg = 1 (4); report whether some has gcd(n, cd*bcd) = 1
    (a 'coprime' = genuine Type I solution, forbidden by ET Prop 1.6) -- expected never.
(B) For primes p = 1 (4): which slice quantities carry the forced non-residue (Lemma CT)?
(C) Least slice parameter g_min(p) (Lemma 1.1(1): t = g) and S_G(p) = #{slice solutions with g <= G}
    at primes approximating the class of one, x** and x_hat_9, and random Mordell-hard controls.
usage: rt_slice_special.py A Mmax | B Pmax | C G y nprimes seed
"""
import sys, random
from math import gcd
from sympy import isprime, primerange, divisors, factorint
from sympy.ntheory.modular import crt

def slice_solutions(n, gmax=None):
    """all (c,f,g) with c(fg-1)-f = n, fg = 1 mod 4, via tn+1 = m m'', m = -1 (t), 4|m, t = g."""
    out = []
    G = n + 2 if gmax is None else gmax
    for g in range(1, G + 1):
        N = g * n + 1
        for m in divisors(N):
            if m % 4 == 0 and (m + 1) % g == 0 and (N // m + 1) % g == 0:
                f, c = (m + 1) // g, (N // m + 1) // g
                if c >= 1 and f >= 1 and c * (f * g - 1) - f == n:
                    out.append((c, f, g))
    return out

def sol_xyz(n, c, f, g):
    d = (f * g - 1) // 4; b = c * g - 1
    return b * d * n, c * d, b * c * d

def leg(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)

mode = sys.argv[1]
if mode == 'A':
    Mmax = int(sys.argv[2]); tot = cop = 0; nos = []
    for m in range(3, Mmax + 1, 2):
        n = m * m; S = slice_solutions(n)
        if not S: nos.append(n)
        for c, f, g in S:
            x, y, z = sol_xyz(n, c, f, g)
            assert 4 * x * y * z == n * (x * y + y * z + z * x)
            tot += 1
            if gcd(n, y * z) == 1: cop += 1
    print(f'odd squares m<={Mmax}: {tot} slice solutions, {cop} with gcd(n,yz)=1; squares with none: {nos[:20]} ({len(nos)})')
elif mode == 'B':
    P = int(sys.argv[2]); stat = {}
    for p in primerange(5, P):
        if p % 4 != 1: continue
        for c, f, g in slice_solutions(p):
            d = (f * g - 1) // 4; b = c * g - 1
            key = tuple(leg(v, p) for v in (c, f, g, d, b))
            stat[key] = stat.get(key, 0) + 1
    print('Legendre symbols (c,f,g,d,b) -> count:')
    for k, v in sorted(stat.items(), key=lambda kv: -kv[1]): print(' ', k, v)
else:
    G, y, NP, seed = map(int, sys.argv[2:6]); random.seed(seed)
    odd = list(primerange(3, y + 1))
    base = {2: (1, 8)}; base.update({q: (1, q) for q in odd})
    cls = {'one': dict(base), 'xss': {**base, 11: (2, 11 ** 3), 13: (15, 13 ** 3)},
           'x9': {**base, 2: (9, 16), 7: (7 ** 3 - 1, 7 ** 3)}}
    def stats(p):
        gmin = None; S = 0
        for g in range(1, G + 1, 2):
            if (g * p) % 4 != 3: continue
            N = g * p + 1
            for m in divisors(N):
                if m % 4 == 0 and (m + 1) % g == 0:
                    S += 1
                    if gmin is None: gmin = g
        return gmin, S
    P0 = None
    for name, cl in cls.items():
        r, Q = crt([m for _, m in cl.values()], [a for a, _ in cl.values()]); r, Q = int(r), int(Q)
        k = 10 ** 3; got = 0
        while got < NP:
            k += random.randint(1, 50); p = r + k * Q
            if isprime(p):
                got += 1; P0 = P0 or p
                print(name, f'p~10^{len(str(p))-1}', 'g_min=%s S_G=%d' % stats(p), flush=True)
    sq = {(x * x) % 840 for x in range(840) if gcd(x, 840) == 1}; got = 0
    while got < NP:
        p = random.randrange(P0 // 2, 2 * P0)
        if p % 840 in sq and isprime(p):
            got += 1; print('ctrl', f'p~10^{len(str(p))-1}', 'g_min=%s S_G=%d' % stats(p), flush=True)
