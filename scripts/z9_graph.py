"""Build G_p / Frob on the lattice side and the path-edge (certificate) data.
Usage: z9_graph.py p  -> prints summary."""
import sys
from z9_lib import *


def build(p):
    ws = words(p)
    neg = [w for w in ws if chi(w, p) == -1]
    if not neg:
        return None
    # start vertex
    G0 = path_gram(neg[0])
    x = iso_classes_mod4(G0)[0]
    H0 = canon(overlattice_hessian(G0, x))
    verts = {H0: None}
    edges = {}  # edge key -> (sorted endpoint tuple)
    stack = [H0]
    while stack:
        H = stack.pop()
        Hg = key_to_gram(H)
        for L in sublattices_hessian(Hg):
            assert det3(L) == p, (L, det3(L))
            k = canon(L)
            if k in edges:
                continue
            Lg = key_to_gram(k)
            ends = []
            for y in iso_classes_mod4(Lg):
                ends.append(canon(overlattice_hessian(Lg, y)))
            assert len(ends) == 2
            edges[k] = tuple(sorted(ends))
            for e in ends:
                if e not in verts:
                    verts[e] = None
                    stack.append(e)
    # path classes with pointers
    path = {}
    for w in neg:
        k = canon(path_gram(w))
        G = path_gram(w)
        ptr = []
        for vec, ent in pentagon_vectors(w):
            if ent % 4 == 0:
                xm = tuple(c % 2 for c in vec)
                ptr.append(canon(overlattice_hessian(G, xm)))
        path.setdefault(k, []).append((w, ptr))
    return verts, edges, path


if __name__ == "__main__":
    p = int(sys.argv[1])
    verts, edges, path = build(p)
    print("p", p, "V", len(verts), "E", len(edges), "path classes", len(path))
    for k, lst in path.items():
        print(k, edges.get(k) is not None, [(w, [list(verts).index(q) for q in ptr]) for w, ptr in lst][:4],
              [list(verts).index(e) for e in edges[k]])
