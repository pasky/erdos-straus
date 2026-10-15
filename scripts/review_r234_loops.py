"""R234: from-scratch recertification of 'loop of G_p/Frob <=> edge lattice represents 2' (GLOBAL_FANO Thm 1.1).
Loop test on the lattice side: the two vertex lattices (maximal-order types = j up to Frob) are isometric.
Also records spine (r(1)>0), path classes, and the loop enrichment of path classes."""
import sys
from review_r234_lib import *

lo, hi = int(sys.argv[1]), int(sys.argv[2])
tot = dict(edges=0, loops=0, rep2=0, bad=0, path=0, pathloops=0, both12=0, both12_notpath=0)
for p in primes_1mod4(lo, hi):
    cls = [k for k in classes_det_p(p) if aniso_at_p(key_to_gram(k), p)]
    paths = set()
    for w in words(p):
        G = path_gram(w)
        if aniso_at_p(G, p):
            paths.add(canon(G))
    assert paths <= set(cls)
    for k in cls:
        G = key_to_gram(k)
        ov = overlattices(G)
        assert len(ov) == 2
        loop = canon(ov[0][2]) == canon(ov[1][2])
        r = rep_counts(G, 2)
        rep2 = r[2] > 0
        tot['edges'] += 1; tot['loops'] += loop; tot['rep2'] += rep2
        if loop != rep2:
            tot['bad'] += 1
            print('MISMATCH', p, k, loop, r)
        if k in paths:
            tot['path'] += 1; tot['pathloops'] += loop
        if r[1] > 0 and r[2] > 0:
            tot['both12'] += 1
            if k not in paths:
                tot['both12_notpath'] += 1
print(lo, hi, tot)
