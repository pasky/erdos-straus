"""R234: 105 control. Words of 105, their 2-adic isotropy; the 2-neighbour component of <1,3,35> (edge = classical det-105
lattice isotropic at 2, vertex = its overlattices L + Z x/2)."""
import sys
from review_r234_lib import *
from review_r234_depth import classical_index2_through

n = int(sys.argv[1]) if len(sys.argv) > 1 else 105
start = [[1, 0, 0], [0, 3, 0], [0, 0, int(n // 3)]] if len(sys.argv) < 3 else eval(sys.argv[2])
ws = words(n)
iso = [w for w in ws if iso_classes_mod4(path_gram(w))]
print('n', n, 'words', len(ws), ws, '2-adically isotropic words', iso)
E = [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
edges, verts = {}, {}
todo = [start]
while todo:
    G = todo.pop()
    k = canon(G)
    if k in edges:
        continue
    G = key_to_gram(k)
    ov = overlattices(G)
    assert len(ov) == 2, ov
    ends = []
    for x, Bs, F in ov:
        kf = canon(F); ends.append(kf)
        if kf not in verts:
            verts[kf] = F
            # neighbours: 3 classical index-2 sublattices of F
            subs = classical_index2_through(F, E, None)
            for S, _ in subs:
                H = gram_basis(F, S)
                todo.append([[int(H[a][b]) for b in range(3)] for a in range(3)])
    edges[k] = ends
from collections import Counter
deg = Counter()
for k, (a, b) in edges.items():
    deg[a] += 1; deg[b] += 1
print('vertex classes', len(verts), 'edge classes', len(edges), 'degrees', sorted(deg.values()))
pathkeys = {canon(path_gram(w)) for w in ws}
print('path classes in component', len(pathkeys & set(edges)))
