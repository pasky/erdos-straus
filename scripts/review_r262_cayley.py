"""R262 from-scratch re-run of LATTICE_MEETING §4 table (class-group Cayley distances to ES classes).

Order O = Z[w], w = 2k*sqrt(-p), w^2 = -N, N = 4k^2 p, disc -16k^2 p.  Classes = reduced primitive forms (a, b, c),
b even.  Ideal of (a, b, c) = aZ + (-b/2 + w)Z.  Composition = product of Z-lattices + HNF (no shortcut, no skipped
steps), then reduction.  Generators: ideals [l, -t + w] for primes l <= L, l ∤ 2kp, t^2 = -N (mod l), both roots.
ES classes on line k: forms [g, 2Y, (N+Y^2)/g] with g = -1 (mod 4k), d | k, g | N + d, Y^2 = d (mod g).
usage: review_r262_cayley.py PMAX L k1,k2,...
"""
import sys
import math
from collections import deque
from sympy import primerange, divisors


def reduce_form(a, b, c):
    while True:
        if c < a or (c == a and b < 0):
            a, b, c = c, -b, a
            continue
        if b > a or b <= -a:
            # translate b into (-a, a]
            t = (a - b) // (2 * a)
            nb = b + 2 * a * t
            c = (nb * nb + 4 * a * c - b * b) // (4 * a)  # keeps disc
            b = nb
            continue
        return (a, b, c)


def ideal(f):
    a, b, c = f
    return [(a, 0), (-b // 2, 1)]


def mul(f1, f2, N):
    (a1, _), (x1, _) = ideal(f1)
    (a2, _), (x2, _) = ideal(f2)
    # elements x + y w; (x1 + w)(x2 + w) = x1 x2 - N + (x1 + x2) w
    vecs = [(a1 * a2, 0), (a1 * x2, a1), (a2 * x1, a2), (x1 * x2 - N, x1 + x2)]
    # HNF in Z^2: find dy = gcd of y's with a vector (x0, dy); A = gcd of x-parts of lattice ∩ (y = 0)
    dy, x0 = 0, 0
    A = 0
    for (x, y) in vecs:
        if y == 0:
            A = math.gcd(A, x)
            continue
        if dy == 0:
            dy, x0 = y, x
            continue
        g, u, v = egcd(dy, y)
        # new pivot u*(x0,dy) + v*(x,y) = (u x0 + v x, g); kernel combination (y/g)*(x0,dy) - (dy/g)*(x,y) has y = 0
        A = math.gcd(A, (y // g) * x0 - (dy // g) * x)
        dy, x0 = g, u * x0 + v * x
    if dy < 0:
        dy, x0 = -dy, -x0
    A = abs(A)
    assert A % dy == 0 and x0 % dy == 0, (f1, f2)
    a = A // dy
    t = (x0 // dy) % a  # ideal = dy * [a, t + w]
    b = -2 * t
    assert (b * b + 4 * N) % (4 * a) == 0
    return reduce_form(a, b, (b * b + 4 * N) // (4 * a))


def egcd(a, b):
    if b == 0:
        return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, u, v = egcd(b, a % b)
    return g, v, u - (a // b) * v


def classes(N):
    D = 4 * N  # |disc|
    out = []
    for a in range(1, math.isqrt(D // 3) + 1):
        for b in range(-a + 1, a + 1):
            if b % 2 or (b * b + D) % (4 * a):
                continue
            c = (b * b + D) // (4 * a)
            if c < a or (c == a and b < 0) or math.gcd(math.gcd(a, b), c) != 1:
                continue
            out.append((a, b, c))
    return out


def run(PMAX, L, ks):
    for k in ks:
        N0 = 4 * k * k
        stats = dict(primes=0, hsum=0, noes=0, unreached=0, hist={})
        for p in primerange(5, PMAX + 1):
            if p % 4 != 1:
                continue
            N = N0 * p
            cl = classes(N)
            S = set(cl)
            gens = []
            for l in primerange(3, L + 1):
                if (2 * k * p) % l == 0:
                    continue
                for t in range(l):
                    if (t * t + N) % l == 0:
                        gens.append(reduce_form(l, -2 * t, (4 * t * t + 4 * N) // (4 * l)))
            es = set()
            for d in divisors(k):
                for g in divisors(N + d):
                    if g % (4 * k) != 4 * k - 1:
                        continue
                    for Y in range(g):
                        if (Y * Y - d) % g == 0:
                            f = reduce_form(g, 2 * Y, (N + Y * Y) // g)
                            assert f in S
                            es.add(f)
            stats['primes'] += 1
            stats['hsum'] += len(cl)
            if not es:
                stats['noes'] += 1
                continue
            dist = {f: 0 for f in es}
            q = deque(es)
            while q:
                f = q.popleft()
                for gg in gens:
                    h2 = mul(f, gg, N)
                    if h2 not in dist:
                        dist[h2] = dist[f] + 1
                        q.append(h2)
            if len(dist) < len(cl):
                stats['unreached'] += 1
            w = max(dist.values())
            stats['hist'][w] = stats['hist'].get(w, 0) + 1
        print(f"k={k}: primes {stats['primes']}, mean #classes {stats['hsum']/stats['primes']:.1f}, "
              f"lines with no ES class {stats['noes']}, worst-start hist {dict(sorted(stats['hist'].items()))}, "
              f"lines with unreached classes {stats['unreached']}", flush=True)


if __name__ == "__main__":
    run(int(sys.argv[1]), int(sys.argv[2]), [int(t) for t in sys.argv[3].split(',')])
