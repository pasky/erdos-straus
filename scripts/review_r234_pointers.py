"""R234 spot-check of z9_pointer_parity: P(p) parity, odd vertices of the path subgraph, both-end pointers.
Pointer of a path class = isotropic class (mod 2L) of a pentagon vector with 4 | entry, transported to a canonical basis.
Two 'both' notions: (V) pointed vertex *classes* (author's: impossible on loops); (I) isotropic classes of L/2L, with flag
whether Aut(L) swaps the two isotropic classes (then 'which end' is not well defined)."""
import sys
from collections import Counter
from review_r234_lib import *


def inv3(M):
    import sympy
    return [[Fr(int(x.p), int(x.q)) for x in row] for row in sympy.Matrix(M).inv().tolist()]


def run(ps):
    for p in ps:
        cls = {}
        for w in words(p):
            G = path_gram(w)
            if not aniso_at_p(G, p):
                continue
            key, bases = canon_full(G)
            cls.setdefault(key, []).append((w, bases[0]))
        verts = {}
        deg = Counter(); ploops = 0; bothV = 0; bothI = 0; swapI = 0
        for key, lst in cls.items():
            G0 = key_to_gram(key)
            iso = iso_classes_mod4(G0)
            ov = overlattices(G0)
            ends = [canon(F) for _, _, F in ov]
            deg[ends[0]] += 1; deg[ends[1]] += 1
            ploops += ends[0] == ends[1]
            # Aut(G0) action on the iso classes
            _, auts = canon_full(G0)  # bases of G0 achieving the key: these ARE the automorphisms (rows = images)
            swap = False
            for M in auts:
                # automorphism sends e_i -> M[i]; class x -> sum x_i M[i]
                img = tuple(sum(iso[0][i] * M[i][j] for i in range(3)) % 2 for j in range(3))
                if img == iso[1]:
                    swap = True
            hitV, hitI = set(), set()
            for w, B in lst:
                # B rows = canonical basis vectors in word coords; word coords -> canonical coords: x_can = x_word * B^{-1}
                Binv = inv3(B)
                t, u, v = w
                A, As = t * u - 1, t * v - 1
                pent = [((1, 0, 0), v), ((0, 1, 0), t), ((0, 0, 1), u), ((A, u, 1), p * A), ((1, v, As), p * As)]
                for x, ent in pent:
                    assert qf(path_gram(w), x) == ent
                    if ent % 4:
                        continue
                    xc = [sum(x[i] * Binv[i][j] for i in range(3)) for j in range(3)]
                    assert all(c.denominator == 1 for c in xc)
                    cl = tuple(int(c) % 2 for c in xc)
                    assert cl in iso, (cl, iso)
                    hitI.add(cl)
                    hitV.add(ends[iso.index(cl)])
            bothV += len(hitV) == 2
            bothI += len(hitI) == 2
            swapI += swap
        oddV = sum(1 for x in deg if deg[x] % 2)
        print(p, 'P', len(cls), 'Ploop', ploops, 'oddV', oddV, 'bothV', bothV, 'bothI', bothI, 'AutSwapsEnds', swapI, flush=True)


if __name__ == '__main__':
    run([int(a) for a in sys.argv[1:]])
