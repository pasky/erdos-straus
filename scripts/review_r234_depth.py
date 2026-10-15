"""R234 from-scratch check of z9_depth_walks Lemma 1 / Cor 2 / Prop 3 on all chi=-1 words, p <= P.
Lattices = Z-bases (rows) in Q^3 (word coordinates), Gram of the path lattice."""
import sys
from fractions import Fraction as Fr
from itertools import product
from review_r234_lib import *
import sympy


def coords(Bs, z):
    M = sympy.Matrix([[sympy.Rational(c.numerator, c.denominator) for c in r] for r in Bs]).T
    sol = M.LUsolve(sympy.Matrix([sympy.Rational(Fr(c).numerator, Fr(c).denominator) for c in z]))
    return [Fr(int(s.p), int(s.q)) for s in sol]


def contains(Bs, z):
    return all(c.denominator == 1 for c in coords(Bs, z))


def same(B1, B2):
    return all(contains(B1, v) for v in B2) and all(contains(B2, v) for v in B1)


def classical_index2_through(G, Fb, z):
    """index-2 sublattices of lattice Fb (rows) that are classical (B integral) and (optionally) contain z."""
    res = []
    for phi in product((0, 1), repeat=3):
        if not any(phi):
            continue
        # kernel basis: vectors y = sum c_i b_i with phi.c even
        gens = [Fb[i] for i in range(3) if phi[i] == 0] + [[2 * c for c in Fb[i]] for i in range(3) if phi[i]]
        i0 = [i for i in range(3) if phi[i]][0]
        gens += [[Fb[i][k] + Fb[i0][k] for k in range(3)] for i in range(3) if phi[i] and i != i0]
        S = hnf_basis(gens)
        H = gram_basis(G, S)
        if all(H[a][b].denominator == 1 for a in range(3) for b in range(3)):
            res.append((S, z is None or contains(S, z)))
    return res


def walk(G, x, k):
    """marked walk; returns number of half-steps, raises on violation."""
    E = [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
    L = E; Fprev = None; Lprev = None; steps = 0; j = 1
    while True:
        z = [Fr(c, 2 ** (j - 1)) for c in x]
        if qf(G, z) % 4 != 0:
            break
        c = coords(L, z); g = 0
        for ci in c:
            g = math.gcd(g, int(ci))
        assert g == 1, 'z not primitive in L_j'
        F = hnf_basis(L + [[ci / 2 for ci in z]])
        assert det3(gram_basis(G, F)) * 4 == det3(G)
        if Fprev is not None:
            assert not same(F, Fprev), 'backtrack F'
        steps += 1
        zp = [ci / 2 for ci in z]
        if qf(G, zp) % 2 != 0:
            break
        subs = classical_index2_through(G, F, zp)
        assert len(subs) == 3
        thr = [S for S, c in subs if c]
        assert len(thr) == 1, 'not unique'
        Lnew = thr[0]
        assert not same(Lnew, L), 'backtrack L'
        assert det3(gram_basis(G, Lnew)) == det3(G)
        Lprev, L, Fprev = L, Lnew, F
        steps += 1; j += 1
    return steps


def unmarked_continuations(G, x):
    """number of classical index-2 sublattices of F1 = L + Z x/2 through x/2 (no marking)."""
    E = [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
    F = hnf_basis(E + [[Fr(c, 2) for c in x]])
    return sum(c for S, c in classical_index2_through(G, F, [Fr(c, 2) for c in x]))


def run(P, only1mod4):
    tot = 0; bad = 0; unm = Counter()
    for p in sympy.primerange(3, P + 1):
        if only1mod4 and p % 4 != 1:
            continue
        for w in words(p):
            G = path_gram(w)
            if not aniso_at_p(G, p):
                continue
            t, u, v = w
            A, As = t * u - 1, t * v - 1
            for x in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (A, u, 1), (1, v, As)]:
                q = qf(G, x)
                if q % 4:
                    continue
                k = 0
                while q % 2 == 0:
                    q //= 2; k += 1
                tot += 1
                s = walk(G, x, k)
                if s != k - 1:
                    bad += 1; print('BAD', p, w, x, k, s)
                if k == 2:
                    unm[unmarked_continuations(G, x)] += 1
    print('P', P, '1mod4only' if only1mod4 else 'all odd primes', 'pointers', tot, 'bad', bad,
          'k=2 pointers by #unmarked classical continuations through x/2:', dict(unm))

from collections import Counter
import math
if __name__ == '__main__':
    run(int(sys.argv[1]), sys.argv[2] == '1')
