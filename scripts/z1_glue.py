"""z1 (O224): gluing a fixed binary M = [[v,-1],[-1,t]] (det A* = tv-1) into lattices of det p.
L_c = <e1,e2,y>, Gram [[v,-1,0],[-1,t,-c],[0,-c,(c^2 v + p)/A*]] for c mod A* with c^2 v = -p (mod A*), 0 < c < A*.
c = +-1 <=> path word (t, (p+v)/A*, v). Question: how often is L_c (c != +-1) isometric to a path lattice of p (other marking)?
Also record the genus (chi) of L_c: same for all c by local theory (check)."""
import sys
from math import gcd
from sympy import primerange
from cf_lib import words_fast, jacobi
from ce_classes import canon, aniso_at
P0, P1, AMAX = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
stats = {'pairs': 0, 'Lc': 0, 'Lc_path': 0, 'chi_mismatch': 0, 'with_path_c1': 0}
for p in primerange(P0, P1):
    paths = set()
    for (t, u, v) in words_fast(p):
        paths.add(canon([[v, -1, 0], [-1, t, -1], [0, -1, u]]))
    for t in range(1, AMAX + 1):
        for v in range(1, AMAX + 1):
            As = t * v - 1
            if As < 2 or As > AMAX or gcd(As, p) > 1: continue
            cs = [c for c in range(1, As) if (c * c * v + p) % As == 0 and gcd(c, As) == 1]
            if not cs: continue
            stats['pairs'] += 1
            ref = None
            for c in cs:
                u = (c * c * v + p) // As
                G = [[v, -1, 0], [-1, t, -c], [0, -c, u]]
                k = canon(G); a = aniso_at(G, p)
                if ref is None: ref = a
                elif a != ref: stats['chi_mismatch'] += 1
                if c in (1, As - 1):
                    stats['with_path_c1'] += 1; continue
                stats['Lc'] += 1
                if k in paths: stats['Lc_path'] += 1
print(stats)
