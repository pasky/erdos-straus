"""z50 ncrt: for every endpoint-grouped ES5 certificate subclass of modulus 4A <= QMAX (A = tv-1; certificate
4|u or 4|tu-1, i.e. a class mod 4A), test (1) whether it is contained in ONE K2 class (modulus dividing 4A);
(2) if not, whether its members n <= NMAX are covered by K2 classes of modulus <= GMAX, and the max least modulus.
Usage: uv run --with sympy python z50_ncrt_k2contain.py QMAX GMAX NMAX"""
import sys
from sympy import divisors, factorint
QMAX, GMAX, NMAX = map(int, sys.argv[1:4])
def g_of(D):
    g = 1
    for p, e in factorint(D).items(): g *= p ** ((e + 1) // 2)
    return g
def sqfree(r): return all(e == 1 for e in factorint(r).values())
_cache = {}
def k2res(G):
    if G in _cache: return _cache[G]
    out = {}
    if G % 4 == 3:
        A = (G + 1) // 4
        for D in divisors(A * A): out.setdefault((-4 * D) % G, ("R", G, D))
    if G % 4 == 0:
        q = G // 4
        for a in divisors(q):
            g = q // a
            for D in divisors(g * g):
                if D % g == 0 and g_of(D) == g: out.setdefault((-(4 * D + a)) % G, ("aD", a, D))
        for r in divisors(q):
            if not sqfree(r): continue
            h = q // r
            for m in divisors(4 * r * h * h + 1): out.setdefault((-pow(m, -1, G)) % G, ("A", r, h, m))
    _cache[G] = out
    return out
Gs = [G for G in range(3, GMAX + 1) if k2res(G)]
def minG(n):
    for G in Gs:
        if n % G in _cache[G]: return G
    return None
tot = single = 0; bad = []
for A in range(2, QMAX // 4 + 1):
    if A % 4 == 0: continue
    for v in divisors(A + 1):
        t = (A + 1) // v
        if t % 4 == 0 or v % 4 == 0: continue
        subs = [("4|u", (-v) % (4 * A))]
        if t % 2 == 1:
            subs.append(("4|tu-1", (pow(t, -1, 4) * A - v) % (4 * A)))
        for lab, b in subs:
            q = 4 * A; tot += 1
            hit = None
            for G in divisors(q):
                r = k2res(G).get(b % G)
                if r: hit = (G, r); break
            if hit: single += 1; continue
            unc = 0; worst = 0
            for n in range(b if b > 0 else q, NMAX, q):
                m = minG(n)
                if m is None: unc += 1
                else: worst = max(worst, m)
            bad.append((t, v, A, lab, b, q, unc, worst))
print("QMAX", QMAX, "GMAX", GMAX, "NMAX", NMAX)
print("subclasses tested:", tot, " contained in a single K2 class:", single)
for x in bad[:40]:
    print("  NOT single: t=%d v=%d A=%d %s class %d mod %d | members<=NMAX uncovered by K2 mod<=GMAX: %d, max least modulus %d" % x)
print("not-single total:", len(bad))
