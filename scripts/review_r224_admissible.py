# R224: §3 admissibility-gap numerics: all p = 1 (4) prime in (1e5, 1.2e5), levels t <= 30 (§1 'clean' incl. r = 2).
from sympy import primerange, factorint
def leg(a, p): a %= p; return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
n = unc = neg = 0
for p in primerange(10 ** 5, 12 * 10 ** 4):
    if p % 4 != 1: continue
    for t in range(1, 31):
        f = factorint(t * p + 1); ds = [1]
        for r, e in f.items(): ds = [d * r ** i for d in ds for i in range(e + 1)]
        n += 1; u = not all(leg(r, p) == 1 for r in f); unc += u
        g = any((A + 1) % t == 0 and leg(A, p) == -1 for A in ds); neg += g
        assert not g or u
print("levels", n, "unclean %.3f" % (unc / n), "carrying chi=-1 word %.3f" % (neg / n), "ratio %.3f" % (neg / unc))
