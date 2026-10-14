"""y1_conic_orbits (O209): compare #(O(Z^3)-orbits on the conic x^2+y^2+z^2=0 over F_p) with the number of classes
of the genus G+_p (positive ternary lattices of det p isotropic at p; scripts/ce_classes.py).
Usage: PYTHONPATH=scripts uv run python scripts/y1_conic_orbits.py p1 p2 ..."""
import sys
from itertools import permutations, product
from ce_classes import classes, aniso_at, gram_of


def conic_orbits(p):
    pts = set()
    for x, y, z in product(range(p), repeat=3):
        if (x, y, z) != (0, 0, 0) and (x * x + y * y + z * z) % p == 0:
            # normalise projective point
            f = next(c for c in (x, y, z) if c)
            inv = pow(f, -1, p)
            pts.add(tuple(c * inv % p for c in (x, y, z)))
    G = [(perm, sg) for perm in permutations(range(3)) for sg in product((1, -1), repeat=3)]
    seen, orbits = set(), 0
    for P in pts:
        if P in seen:
            continue
        orbits += 1
        for perm, sg in G:
            Q = [sg[i] * P[perm[i]] % p for i in range(3)]
            f = next(c for c in Q if c)
            inv = pow(f, -1, p)
            seen.add(tuple(c * inv % p for c in Q))
    return len(pts), orbits


for p in map(int, sys.argv[1:]):
    cl = classes(p)
    plus = sum(1 for k in cl if not aniso_at(gram_of(k), p))
    print('p', p, 'conic pts', *conic_orbits(p), '| G+ classes', plus, '| G- classes', len(cl) - plus)
