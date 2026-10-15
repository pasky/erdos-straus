"""z1 (O224) (B): classes of G^-_p; which are path classes; norm-one split classes <1>+M."""
import sys
from sympy import primerange
from cf_lib import words
from ce_classes import canon, classes, gram_of, aniso_at

P0, P1 = int(sys.argv[1]), int(sys.argv[2])
for p in primerange(P0, P1):
    if p % 8 != 1: continue
    cl = classes(p)
    minus = [k for k in cl if aniso_at(gram_of(k), p)]
    paths = set()
    for (t, u, v) in words(p):
        paths.add(canon([[v, -1, 0], [-1, t, -1], [0, -1, u]]))
    m1 = [k for k in minus if k[0] == 1]
    m1p = [k for k in m1 if k in paths]
    pm = [k for k in paths if k in minus]
    print(p, 'G-', len(minus), 'paths in G-', len(pm), 'min1 in G-', len(m1), 'min1&path', len(m1p),
          'min of path classes', sorted(k[0] for k in pm))
