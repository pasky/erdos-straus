"""R199: recount of Section 5.5 / Prop 4.1 EVIDENCE: number of classes of G^-_p, number of path classes (classes
containing some L_w with chi(w) = -1), and ranks of the first path class by min(L) and by min(E^0) = min of the
form adj(G) (E^0 = p L^#, Gram adj(G)).  Also the least quadratic non-residue."""
import sys
sys.path.insert(0, 'scripts')
from review_ce_classes import classes, canon, aniso_p, short_vectors, leg
from review_ce_words import words, adj


def minimum(G):
    c = min(G[i][i] for i in range(3))
    return min(q for q, x in short_vectors(G, c))


for p in [int(x) for x in sys.argv[1:]]:
    cl = classes(p)
    neg = {k: G for k, G in cl.items() if aniso_p(G, p)}
    path = {}
    for (t, u, v) in words(p):
        G = [[v, -1, 0], [-1, t, -1], [0, -1, u]]
        if leg(-(t * u - 1), p) == -1:
            k = canon(G)
            assert k in neg, (p, t, u, v)
            path.setdefault(k, []).append((t, u, v))
    data = []
    for k, G in neg.items():
        data.append((minimum(G), minimum(adj(G)), k in path, k))
    rL = sorted(data, key=lambda d: d[0])
    rE = sorted(data, key=lambda d: d[1])
    first = lambda lst: next(i + 1 for i, d in enumerate(lst) if d[2])
    nqr = next(a for a in range(2, p) if leg(a, p) == -1)
    print(f'p={p} (n_p={nqr}): |G^-|={len(neg)} |G^+|={len(cl) - len(neg)} path classes={len(path)}; '
          f'first path rank by min(L)={first(rL)} (ties: min L values {[d[0] for d in rL[:first(rL)]]}), '
          f'by min(E0)={first(rE)}; min(E0) list head={[(d[1], d[2]) for d in rE[:12]]}', flush=True)
