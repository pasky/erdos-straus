"""Global statistics of path edges on G_p/Frob, p = 1 mod 4 in [lo, hi].
Columns: p V E loops P Ploop oddV ptdV both  (see GLOBAL_FANO.md §1)."""
import sys
from collections import Counter
from sympy import isprime
from z9_graph import build

lo, hi = int(sys.argv[1]), int(sys.argv[2])
mod = int(sys.argv[3]) if len(sys.argv) > 3 else 4
for p in range(lo, hi + 1):
    if not isprime(p) or p % mod != 1 % mod or p < 5:
        continue
    r = build(p)
    if r is None:
        print(p, "NO CERT")
        continue
    verts, edges, path = r
    loops = sum(1 for e in edges.values() if e[0] == e[1])
    deg = Counter()
    ploops = 0
    for k in path:
        a, b = edges[k]
        deg[a] += 1
        deg[b] += 1
        ploops += a == b
    oddV = sum(1 for v in deg if deg[v] % 2)
    ptd = set()
    both = 0
    for k, lst in path.items():
        s = set()
        for w, ptr in lst:
            s |= set(ptr)
        ptd |= s
        both += len(s) == 2
    print(p, len(verts), len(edges), loops, len(path), ploops, oddV, len(ptd), both, flush=True)
