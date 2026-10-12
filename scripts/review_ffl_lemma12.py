"""R161: exhaustive check of Lemma 1.2 on small monic triples.

For all monic X <= Y <= Z (degrees <= D) compute 1/X+1/Y+1/Z = U/V reduced with V monic. If U is monic,
V = P irreducible and deg V > deg U (i.e. a genuine A/P with A monic, k >= 1), record whether the minimal
denominator degree equals n - k (NC) and the multiplicity m of the minimal degree.
"""
import sys
from collections import Counter
from review_ffl_poly import PolyRing

q, D = int(sys.argv[1]), int(sys.argv[2])
R = PolyRing(q)
mons = [M for d in range(0, D + 1) for M in R.monics(d)]
stats = Counter()
examples = {}
irr_cache = {}
for i, X in enumerate(mons):
    for j in range(i, len(mons)):
        Y = mons[j]
        XY = R.mul(X, Y)
        for l in range(j, len(mons)):
            Z = mons[l]
            num = R.add(R.add(XY, R.mul(Y, Z)), R.mul(Z, X))
            den = R.mul(XY, Z)
            if not num:
                continue
            g = R.gcd(num, den)
            U, V = R.divmod(num, g)[0], R.divmod(den, g)[0]
            c = V[-1]
            U, V = R.scal(R.F.inv[c], U), R.monic(V)
            if U[-1] != 1 or R.deg(V) <= R.deg(U) or R.deg(U) < 1:
                continue
            if V not in irr_cache:
                irr_cache[V] = R.is_irreducible(V)
            if not irr_cache[V]:
                continue
            n, k = R.deg(V), R.deg(U)
            degs = sorted(map(R.deg, (X, Y, Z)))
            m = degs.count(degs[0])
            nc = degs[0] >= n - k
            key = (m, "NC" if nc else "cancel", "has deg n-k" if (n - k) in degs else "no deg n-k")
            stats[key] += 1
            examples.setdefault(key, (R.show(X), R.show(Y), R.show(Z), "A=" + R.show(U), "P=" + R.show(V)))
print(f"q={q} D={D}")
for key in sorted(stats):
    print(key, stats[key], "e.g.", examples[key])
