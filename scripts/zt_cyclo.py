"""zt_cyclo.py (O227): the cyclotomic ("thirds corner") Case B tuples of R217/R218 versus x*_c, explicitly.

Over F_3, s = 3^h + 1, v1 = -1: m' w1 C1 = T^{3^h - 1} - 1 (all monic irreducibles of degree | h except T), a = b,
g' = -(w1 + C1)/T. For every such tuple (exhaustive for h = 2, 3; random sample of assignments for h = 4) we verify (B)
and compute dep_c = v_T(E + 1 + cT), c = 1, 2. FF_THIRDS_CORNER Cor 1.3 predicts dep_c <= max(a - 1, b) = a < N(s) + 1.
usage: uv run --with python-flint python scripts/zt_cyclo.py [SAMPLES_h4]"""
import random
import sys
from collections import Counter
from itertools import product

import flint

p = 3
T = flint.nmod_poly([0, 1], p)
one = flint.nmod_poly([1], p)


def tval(f):
    c = [int(x) for x in f.coeffs()]
    for i, x in enumerate(c):
        if x:
            return i
    return 10 ** 9


def run(h, assignments):
    F = flint.nmod_poly([p - 1] + [0] * (p ** h - 2) + [1], p)
    fs = [f for f, e in F.factor()[1]]
    s = p ** h + 1
    N = (s + 1) // 2  # N(s) for k = 2: ceil(s/2)
    ntup = 0
    depc = Counter()
    worst = 0
    for asg in assignments(len(fs)):
        parts = [one, one, one]
        for f, j in zip(fs, asg):
            parts[j] = parts[j] * f
        m, w1, C1 = parts
        if w1.degree() != C1.degree():
            continue
        S = w1 + C1
        if tval(S) != 1:
            continue
        g = -(S // T)
        if int(g.coeffs()[-1]) != 1 or int(g.coeffs()[0]) == 0:
            continue
        v1 = flint.nmod_poly([p - 1], p)
        assert m * w1 * C1 == T ** (s - 2) + v1 and w1 + C1 == T * g * v1
        ntup += 1
        a = w1.degree() + 1
        E = T * g * m * w1 - one
        for c in (1, 2):
            d = tval(E + one + c * T)
            depc[(c, d)] += 1
            assert d <= a, (h, d, a)
            worst = max(worst, d)
    return s, N, len(fs), ntup, worst, depc


h2 = run(2, lambda n: product(range(3), repeat=n))
h3 = run(3, lambda n: product(range(3), repeat=n))
SAM = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
rng = random.Random(1)
h4 = run(4, lambda n: (tuple(rng.randrange(3) for _ in range(n)) for _ in range(SAM)))
for h, r in ((2, h2), (3, h3), (4, h4)):
    s, N, nf, ntup, worst, depc = r
    print(f"h={h} s={s} N(s)={N} factors={nf} tuples={ntup} max dep(E+1+cT)={worst} (needed N+1={N+1}); dep histogram {sorted(depc.items())}")
