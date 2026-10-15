# review_r254_mu0.py -- R254 from-scratch check of Prop 2.7 / Cor 2.8 (which windows contain the unit-square point mu=0).
# For n_s = c0*4^s + k (c0 odd, c0 + k = 4^J), a window (m, j, code, w, h) contains mu = 0 iff its firing set (a union of
# classes s mod P) contains s = 0 mod P, i.e. iff the relation holds for the residues at s = 0 (mod P), where 4^s = 1,
# 2^s = 1 (mod m) [P = h ord_m(4) resp. 2 ord_m(2)].  Residues there (pure modular arithmetic, inverses mod m):
#   n = c0 + k;  code 0 (needs h | j): X = 4^{-j/h};  code 1 (j even): X = 2^{-j/2};  code 2 (j odd): X = 2^{-(j+1)/2}.
# Menu pieces (as in the z14 construction): 2^i (|i| <= E = 2j-2), odd primes of c0 with multiplicity, n, Y-pieces.
# Full relation search d1 = -d2 (mod m) over eps in {-1,0,1}^pieces and 2^i, NO Jacobi shortcut.
# Part B: for sg1, j = 1, w odd, an exact enumeration up to the magnitude bound (re-derived): every relation is
#   G U + 2 V = 0 (mod m) with U V | c0 4^J, G = 2w^2 +- 2w + 1, so 0 < G U + 2V <= c0 4^J (G + 2) < m for large w.
# Part C: cross-check of the modular limit against actual exponents s = P*t (small m only).
import sys
from math import gcd, prod
from itertools import product as iprod
import sympy as sp
from sympy import factorint, n_order

FAM = [(15, 1), (31, 33), (7, 57), (63, 1), (47, 17), (55, 9), (3, 1), (7, 9), (23, 41), (39, 25)]
JMAX, WMAX, HS = int(sys.argv[1]), int(sys.argv[2]), (1, 3, 5, 7, 9, 15)
X_ = sp.Symbol('X')


def cyc_pieces(w, h):
    out = []
    for e in sp.divisors(h):
        ph = sp.Poly(sp.cyclotomic_poly(2 * e, X_), X_); D = ph.degree()
        out.append([(i, int(cf) * w ** (D - i)) for (i,), cf in ph.terms()])
    return out


def ev(poly, X, m): return sum(cf * pow(X, i, m) for i, cf in poly) % m


def pieces_mu0(c0, k, j, code, w, h, m):
    inv2, inv4 = pow(2, -1, m), pow(4, -1, m)
    if code == 0:
        if j % h: return None
        X = pow(inv4, j // h, m); ys = [ev(p, X, m) for p in cyc_pieces(w, h)]
    elif code == 1:
        if j % 2: return None
        X = pow(inv2, j // 2, m); ys = [(X * X + 2 * X * w + 2 * w * w) % m, (X * X - 2 * X * w + 2 * w * w) % m]
    else:
        if j % 2 == 0: return None
        X = pow(inv2, (j + 1) // 2, m); ys = [(2 * X * X + 2 * X * w + w * w) % m, (2 * X * X - 2 * X * w + w * w) % m]
    return [p for p, v in factorint(c0).items() for _ in range(v)] + [(c0 + k) % m] + ys


def pieces_at_s(c0, k, j, code, w, h, m, s):
    r = s - j; n = (c0 * pow(4, s, m) + k) % m
    if code == 0:
        X = pow(4, r // h, m); ys = [ev(p, X, m) for p in cyc_pieces(w, h)]
    elif code == 1:
        X = pow(2, r // 2, m); ys = [(X * X + 2 * X * w + 2 * w * w) % m, (X * X - 2 * X * w + 2 * w * w) % m]
    else:
        X = pow(2, (r - 1) // 2, m); ys = [(2 * X * X + 2 * X * w + w * w) % m, (2 * X * X - 2 * X * w + w * w) % m]
    return [p for p, v in factorint(c0).items() for _ in range(v)] + [n] + ys


def rel(vals, m, E):
    for eps in iprod((-1, 0, 1), repeat=len(vals)):
        p1 = prod(v for v, e in zip(vals, eps) if e == 1) % m
        p2 = prod(v for v, e in zip(vals, eps) if e == -1) % m
        for i in range(E + 1):
            if (pow(2, i, m) * p1 + p2) % m == 0:
                return eps, i
    return None


for c0, k in FAM:
    J = (c0 + k).bit_length() // 2; assert 4 ** J == c0 + k and k % 8 == 1
    hits, tested, xchk = [], 0, 0
    for j in range(1, JMAX + 1):
        for w in range(1, WMAX + 1):
            for code, h, t in [(0, h, w ** h) for h in HS] + [(1, 1, 4 * w ** 4), (2, 1, w ** 4)]:
                m = c0 * 4 ** j * t - k
                if m <= 1: continue
                vals = pieces_mu0(c0, k, j, code, w, h, m)
                if vals is None: continue
                tested += 1
                R = rel(vals, m, 2 * j - 2)
                if R: hits.append((m, j, code, w, h, R))
                if m < 10 ** 7 and tested % 7 == 0:   # part C cross-check with an actual exponent s = 0 mod P
                    P = (h * n_order(4, m)) if code == 0 else 2 * n_order(2, m)
                    s = P * (j // P + 2)
                    assert sorted(pieces_at_s(c0, k, j, code, w, h, m, s)) == sorted(vals); xchk += 1
    # part B: sg1, j = 1, w odd up to the magnitude bound
    ps = [p for p, v in factorint(c0).items() for _ in range(v)]
    w, B = 1, []
    while True:
        m = 4 * c0 * w ** 4 - k
        if c0 * 4 ** J * (2 * w * w + 2 * w + 3) < m: break
        if m > 1:
            R = rel(pieces_mu0(c0, k, 1, 2, w, 1, m), m, 0)
            if R: B.append((w, m, R))
        w += 2
    print((c0, k), 'J', J, '| menu windows containing-0 tested', tested, 'hits', [(h[0], h[1], h[2], h[3], h[4]) for h in hits][:6],
          '| sg1 j=1 odd w <', w, 'hits', B[:4], '| x-check', xchk, flush=True)
