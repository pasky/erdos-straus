"""R199: independent check of 5.2 (T_ell spectra of C[G+_p] and C[G-_p] share only the Eisenstein eigenvalue ell+1).
Own Kneser ell-neighbour construction (ell odd, ell != p) on my canonical classes (review_ce_classes.canon),
exact characteristic polynomials (sympy) and their gcd."""
import sys
from itertools import product
from fractions import Fraction as F
import sympy as sp
sys.path.insert(0, 'scripts')
from review_ce_classes import classes, canon, aniso_p
from review_ce_lib import lattice_basis_from_gens


def B(G, x, y):
    return sum(G[i][j] * x[i] * y[j] for i in range(3) for j in range(3))


def neighbours(G, l):
    out = []
    seen = set()
    for x in product(range(l), repeat=3):
        if not any(x):
            continue
        # projective normalisation: first nonzero coordinate 1
        f = next(c for c in x if c)
        if f != 1:
            continue
        if B(G, x, x) % l:
            continue
        x = list(x)
        q = B(G, x, x)
        # find y with 2 B(x,y) = -q/l (mod l)
        need = (-(q // l)) % l
        for y in product(range(l), repeat=3):
            if (2 * B(G, x, y) - need) % l == 0:
                break
        xp = [x[i] + l * y[i] for i in range(3)]
        assert B(G, xp, xp) % (l * l) == 0
        # L_x = {z : B(xp, z) = 0 mod l}: generators l*e_i and lattice kernel
        gens = [[F(l if i == k else 0) for i in range(3)] for k in range(3)]
        for z in product(range(l), repeat=3):
            if any(z) and B(G, xp, z) % l == 0:
                gens.append([F(c) for c in z])
        gens.append([F(c, l) for c in xp])
        # 3-dim HNF: reuse 4-dim routine by padding
        Bas = lattice_basis_from_gens([g + [F(0)] for g in gens])
        Bas = [r[:3] for r in Bas if any(r[:3])]
        assert len(Bas) == 3
        Gn = [[B(G, u, v) for v in Bas] for u in Bas]
        assert all(F(c).denominator == 1 for r in Gn for c in r)
        Gn = [[int(c) for c in r] for r in Gn]
        out.append(canon(Gn))
    return out


def charpoly(keys, reps, l):
    idx = {k: i for i, k in enumerate(keys)}
    n = len(keys)
    M = [[0] * n for _ in range(n)]
    for k in keys:
        nb = neighbours(reps[k], l)
        assert len(nb) == l + 1
        for k2 in nb:
            M[idx[k]][idx[k2]] += 1
    X = sp.symbols('X')
    return sp.Matrix(M).charpoly(X).as_expr(), X


for arg in sys.argv[1:]:
    p, l = map(int, arg.split(':'))
    cl = classes(p)
    neg = [k for k in cl if aniso_p(cl[k], p)]
    pos = [k for k in cl if not aniso_p(cl[k], p)]
    cn, X = charpoly(neg, cl, l)
    cp_, _ = charpoly(pos, cl, l)
    g = sp.gcd(sp.Poly(cn, X), sp.Poly(cp_, X))
    print(f'p={p} T_{l}: |G-|={len(neg)} |G+|={len(pos)}; gcd of char polys = {g.as_expr()}; '
          f'factor G+ = {sp.factor(cp_)}', flush=True)
