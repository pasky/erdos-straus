"""O251 (LATTICE_MEETING §4): line k of the slice lattices = forms [g, 2Y, D] of disc -16 k^2 p (§2.3).
For p = 1 (4) prime <= P and k in KS: enumerate the reduced primitive forms (the class group of the order of
conductor 2k), mark ES classes (some form in the class is [g, 2Y, D] with g = -1 (4k) and g | 4k^2 p + d, d | k:
detected on all reduced forms AND on all forms [g, 2, D] from divisors of 4k^2 p + d, mapped to their reduced
class), then BFS in the Cayley graph with generators the prime forms of norm l <= LMAX (both orientations) from the
class of the least-root window-shot form, and report the distance to the nearest ES class.
T1 control: n = c^2 odd squares in place of p (no ES class may exist).
Usage: z23_cayley.py P LMAX k1,k2,..
"""
import sys
from math import gcd, isqrt
from collections import deque
from sympy import primerange, divisors, isprime
from sympy.ntheory.residue_ntheory import sqrt_mod


def reduce_form(a, b, c):
    while True:
        if not (-a < b <= a):
            t = (a - b) // (2 * a)
            b2 = b + 2 * a * t
            c = (b2 * b2 - (b * b - 4 * a * c)) // (4 * a)
            b = b2
        if a > c or (a == c and b < 0):
            a, b, c = c, -b, a
            continue
        return (a, b, c)


def compose(f1, f2, Delta):
    """Dirichlet composition for gcd(a1, a2) = 1 (both primitive); returns reduced form or None."""
    a1, b1, _ = f1
    a2, b2, _ = f2
    if gcd(a1, a2) != 1:
        return None
    # B = b1 (2a1), B = b2 (2a2), B^2 = Delta (4 a1 a2); b1 = b2 (2) since both = Delta (2)
    m1, m2 = 2 * a1, 2 * a2
    # CRT on (B - b1)/2 mod a1 and (B - b2)/2 mod a2
    u = pow(a1, -1, a2)
    t = ((b2 - b1) // 2 * u) % a2
    B = b1 + 2 * a1 * t
    A = a1 * a2
    assert (B * B - Delta) % (4 * A) == 0
    return reduce_form(A, B, (B * B - Delta) // (4 * A))


def classes(Delta):
    D = -Delta
    out = []
    for a in range(1, isqrt(D // 3) + 1):
        for b in range(-a + 1, a + 1):
            if (b * b - Delta) % (4 * a):
                continue
            c = (b * b - Delta) // (4 * a)
            if c < a or (c == a and b < 0):
                continue
            if gcd(gcd(a, b), c) == 1:
                out.append((a, b, c))
    return out


def es_class_set(n, k, Delta):
    """classes of the ES forms [g, 2Y, (4k^2 n + Y^2)/g]: g = -1 (4k), g | 4k^2 n + d, d | k, Y^2 = d (mod g)."""
    es = set()
    for d in divisors(k):
        N = 4 * k * k * n + d
        for g in divisors(N):
            if g % (4 * k) != 4 * k - 1 or g <= d:
                continue
            for Y in sqrt_mod(d % g, g, all_roots=True):
                f = (g, 2 * Y, (4 * k * k * n + Y * Y) // g)
                if gcd(gcd(f[0], f[1]), f[2]) == 1:
                    es.add(reduce_form(*f))
    return es


def run(n, k, LMAX):
    Delta = -16 * k * k * n
    cls = classes(Delta)
    cset = set(cls)
    es = set()
    for (a, b, c) in cls:  # ES test on reduced forms themselves (b = 2Y)
        Y = b // 2
        if a % (4 * k) == 4 * k - 1 and any((4 * k * k * n + d) % a == 0 for d in divisors(k)):
            es.add((a, b, c))
    es2 = es_class_set(n, k, Delta)
    assert es2 <= cset and es <= es2, (n, k, es - es2)
    es = es2
    gens = []
    for l in primerange(3, LMAX + 1):
        if (2 * k * n) % l == 0:
            continue
        for b in range(0, 2 * l):
            if (b * b - Delta) % (4 * l) == 0:
                gens.append(reduce_form(l, b, (b * b - Delta) // (4 * l)))
    return cls, es, gens, Delta


P, LMAX = int(sys.argv[1]), int(sys.argv[2])
KS = [int(x) for x in sys.argv[3].split(',')]
for k in KS:
    agg = dict(primes=0, h_mean=0, es_classes=0, no_es=0, dist_hist={})
    for p in primerange(5, P + 1):
        if p % 4 != 1:
            continue
        cls, es, gens, Delta = run(p, k, LMAX)
        agg['primes'] += 1
        agg['h_mean'] += len(cls)
        agg['es_classes'] += len(es)
        if not es:
            agg['no_es'] += 1
            continue
        dist = {f: 0 for f in es}  # multi-source BFS: distance of every class to the nearest ES class
        dq = deque(es)
        while dq:
            f = dq.popleft()
            for gq in gens:
                nf = compose(f, gq, Delta)
                if nf is None:
                    a, b, c = f
                    nf = compose((c, -b, a), gq, Delta) if gcd(c, gq[0]) == 1 else None
                if nf is not None and nf not in dist:
                    dist[nf] = dist[f] + 1
                    dq.append(nf)
        found = max(dist.values()) if len(dist) == len(cls) else ('unreached', len(cls) - len(dist))
        agg['dist_hist'][found] = agg['dist_hist'].get(found, 0) + 1
    agg['h_mean'] /= max(1, agg['primes'])
    print('k =', k, agg)
    t1 = [c * c for c in range(3, isqrt(P) + 1, 2) if run(c * c, k, LMAX)[1]]
    print('   T1 odd squares with an ES class (must be none):', t1)
