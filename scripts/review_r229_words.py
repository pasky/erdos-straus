# R229 from-scratch word-level check of FOUR_ADIC_INPUT Lemma 1.1, Lemma 1.2, Thm 1.3.
# Independent of the author's scripts: own Jacobi symbol, own 2-adic Hilbert symbol, own mod-2 class enumeration.
import sys
from fractions import Fraction
from itertools import product

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000

def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def v2(x):
    x = abs(x); k = 0
    while x % 2 == 0: x //= 2; k += 1
    return k

def hilbert2(a, b):
    # a, b nonzero integers; 2-adic Hilbert symbol (Serre)
    al, be = v2(a), v2(b)
    u, w = a >> al if a > 0 else -((-a) >> al), b >> be if b > 0 else -((-b) >> be)
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    e = (eps(u) * eps(w) + al * om(w) + be * om(u)) % 2
    return -1 if e else 1

def sqfree_int(fr):
    # represent rational square class by integer num*den
    return fr.numerator * fr.denominator

def iso2(G):
    # diagonalise over Q (Gram-Schmidt), ternary <d1,d2,d3> isotropic at 2 iff (-d1 d3, -d2 d3)_2 = 1
    n = 3
    M = [[Fraction(x) for x in r] for r in G]
    d = []
    for i in range(n):
        piv = M[i][i]; assert piv != 0
        d.append(piv)
        for j in range(i + 1, n):
            f = M[j][i] / piv
            for k in range(i, n):
                M[j][k] -= f * M[i][k]
    a, b, c = (sqfree_int(x) for x in d)
    return hilbert2(-a * c, -b * c) == 1

def Q(G, x):
    return sum(G[i][j] * x[i] * x[j] for i in range(3) for j in range(3))

stats = dict(words=0, bad_even=0, bad_distinct=0, bad_le2=0, bad_thm=0, bad_iso_chi=0, bad_lem12=0, bad_W=0,
             bad_pentvec=0, iso_hits={1: 0, 2: 0}, n1words=0)
for t in range(1, NMAX + 3):
    for u in range(1, NMAX + 3):
        A = t * u - 1
        if A <= 0: continue
        if A - u > NMAX: break  # v=1 gives n = A - u... n = A*v - u increasing in v
        v = 1
        while True:
            n = A * v - u
            if n > NMAX: break
            if n >= 1 and n % 2 == 1:
                As = t * v - 1
                P = [t, u, v, A, As]
                G = [[v, -1, 0], [-1, t, -1], [0, -1, u]]
                assert v * (t * u - 1) - u == n  # det G
                chi = jacobi(-A, n) if n > 1 else 1
                if n == 1: stats['n1words'] += 1
                stats['words'] += 1
                ev = [i for i in range(5) if P[i] % 2 == 0]
                if len(ev) != 2: stats['bad_even'] += 1
                vecs = [(0, 1, 0), (0, 0, 1), (1, 0, 0), (A, u, 1), (1, v, As)]  # e2,e3,e1,f,f* <-> t,u,v,A,A*
                # check norms of pentagon vectors
                if [Q(G, x) for x in vecs] != [t, u, v, n * A, n * As]: stats['bad_pentvec'] += 1
                cls = [tuple(c % 2 for c in x) for x in vecs]
                if len({cls[i] for i in ev}) != 2: stats['bad_distinct'] += 1
                # mod-2 classes: q = Q mod 4
                q = {x: Q(G, x) % 4 for x in product((0, 1), repeat=3) if any(x)}
                W = [x for x in q if q[x] % 2 == 0]
                zero = [x for x in q if q[x] == 0]
                if len(W) != 3 or any(cls[i] not in W for i in ev):
                    stats["bad_W"] += 1
                    if stats["bad_W"] < 3: print("W?", t, u, v, W, cls, ev)
                iso = iso2(G)
                if (len(zero) == 2) != iso or len(zero) not in (0, 2): stats['bad_lem12'] += 1
                if iso != (chi == -1): stats['bad_iso_chi'] += 1
                m4 = sum(1 for x in P if x % 4 == 0)
                if m4 > 2: stats['bad_le2'] += 1
                if (m4 > 0) != (chi == -1): stats['bad_thm'] += 1
                if m4 > 0: stats['iso_hits'][len({cls[i] for i in ev if P[i] % 4 == 0})] += 1
            v += 1
print(NMAX, stats)

# Lemma 1.2 on all diagonal odd unimodular <a,b,c>, a,b,c in {1,3,5,7} (unit square classes of Z_2):
bad = 0
for a, b, c in product((1, 3, 5, 7), repeat=3):
    D = [[a, 0, 0], [0, b, 0], [0, 0, c]]
    z = [x for x in product((0, 1), repeat=3) if any(x) and Q(D, x) % 4 == 0]
    if (len(z) == 2) != iso2(D) or len(z) not in (0, 2): bad += 1
print("Lemma 1.2 diagonal check, failures:", bad)
