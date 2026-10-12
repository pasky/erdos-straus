"""O163 Lemma 8.4 sanity check: for every square class C mod M and every octant, find a
prime lam and X with lam*X in C (in the octant), Q(X) = w^2 (w odd), gcd(w, G(lam X)) = 1 and
lam not dividing w*H(X).  G is chosen with G(0,0) = 0 so that R159's original route (needing
gcd(Q(P), G(P)) = 1 at P itself) fails on the classes without primitive square points; the
script also reports those classes (no primitive square point found in the box).
"""
from math import gcd, isqrt, atan2, pi
import sys

FORMS = {
    'u2+v2': (1, 0, 1),
    'u2+uv+v2': (1, 1, 1),
    'u2+2v2': (1, 0, 2),
    'u2+5v2': (1, 0, 5),
}


def run(name, M, B, lam_max):
    A, Bc, Cc = FORMS[name]
    Q = lambda u, v: A * u * u + Bc * u * v + Cc * v * v
    G = lambda u, v: u * (u - 2 * v + 3) * (v * v + u - 1) * (u + v)  # G(0,0)=0, Q does not divide G
    H = lambda u, v: (u + 2 * v) * (3 * u - v)
    primes = [p for p in range(3, lam_max + 1) if all(p % q for q in range(2, isqrt(p) + 1))]
    sq = []
    for u in range(-B, B + 1):
        for v in range(-B, B + 1):
            if u == 0 and v == 0:
                continue
            q = Q(u, v)
            w = isqrt(q)
            if w * w == q and w % 2 == 1:
                sq.append((u, v, w))
    # square classes mod M
    classes = []
    for u0 in range(M):
        for v0 in range(M):
            q = Q(u0, v0) % M
            if gcd(q, M) != 1:
                continue
            if any((s * s - q) % M == 0 for s in range(M)):
                classes.append((u0, v0))
    octant = lambda u, v: int(((atan2(v, u) + 2 * pi) % (2 * pi)) // (pi / 4))
    found = set()
    prim = set()
    for (u, v, w) in sq:
        if gcd(u, v) == 1:
            prim.add(((u % M, v % M), octant(u, v)))
        for lam in primes:
            P = (lam * u, lam * v)
            key = ((P[0] % M, P[1] % M), octant(u, v))
            if key in found:
                continue
            if w % lam == 0 or (w * H(u, v)) % lam == 0:
                continue
            if gcd(w, G(*P)) != 1:
                continue
            found.add(key)
    allkeys = {(c, o) for c in classes for o in range(8)}
    miss = allkeys - found
    noprim = {c for c in classes if not any((c, o) in prim for o in range(8))}
    print(f"{name} M={M}: {len(classes)} square classes, {len(allkeys)} (class,octant) pairs; "
          f"found {len(found & allkeys)}, missing {len(miss)}; classes with no primitive square "
          f"point in box: {len(noprim)}")
    if miss:
        print("  missing sample:", sorted(miss)[:10])
    return len(miss)


if __name__ == "__main__":
    tot = 0
    for name, M, B in (('u2+v2', 8, 260), ('u2+v2', 24, 260), ('u2+v2', 40, 260),
                       ('u2+uv+v2', 24, 260), ('u2+2v2', 16, 1200), ('u2+2v2', 24, 260),
                       ('u2+5v2', 40, 1500)):
        tot += run(name, M, B, 200)
        sys.stdout.flush()
    print("TOTAL missing", tot)
