# review_r253_mu0.py — R253 from-scratch cross-check of EXP_105 Prop 2.4/Cor 2.5/Prop 2.7/Cor 2.8.
# At the unit-square point mu = 0 (c0 + k = 4^J) compute the S-integer limits mod m of all window pieces
# (odd primes of c0; n -> 4^J; algebraic factors of 4^r + t with 4^r -> 4^{-j}) and search relations
# 2^i prod(pieces^{eps}) = -1 (mod m), eps in {-1,0,1}, |i| <= E = 2j-2 (c0 odd).  Generic search over the whole
# menu (cyclotomic h, 'sg', 'sg1'), NOT the reduced form of the author's z14_sg1mu0.py.
# Part B: the caveat 'splitting the SG numerators by fixed primes' — allow every prime of the numerators as an atom.
import sys
from itertools import product
from math import gcd
from sympy import factorint, cyclotomic_poly, Poly, symbols, divisors, n_order

Xs = symbols('X')

def cyc_homs(h, w):
    out = []
    for e in divisors(h):
        p = Poly(cyclotomic_poly(2 * e, Xs)); D = p.degree()
        out.append([(i, int(cf) * w ** (D - i)) for (i,), cf in p.terms()])
    return out

def relation(res, E, m):
    res = [r % m for r in res]
    if any(gcd(r, m) != 1 for r in res): return None  # cannot occur at mu=0 (Prop 2.4)
    for eps in product((-1, 0, 1), repeat=len(res)):
        v = 1
        for r, e in zip(res, eps):
            if e: v = v * pow(r, e, m) % m
        for i in range(-E, E + 1):
            if v * pow(2, i, m) % m == m - 1: return (eps, i)
    return None

def windows_at0(c0, k, JMAX=7, WMAX=9, HS=(1, 3, 5, 7, 9, 15), MMAX=10 ** 40):
    J = (c0 + k).bit_length() // 2; assert 4 ** J == c0 + k
    ps = [p for p, v in factorint(c0).items() for _ in range(v)]
    hits = []; tested = 0
    for j in range(1, JMAX + 1):
        for w in range(1, WMAX + 1):
            shapes = [('pow', h, w ** h) for h in HS] + [('sg', 2, 4 * w ** 4), ('sg1', 2, w ** 4)]
            for kind, h, t in shapes:
                m = c0 * 4 ** j * t - k
                if m <= 1 or m % 2 == 0 or m > MMAX: continue
                # class containment of mu=0 and limits
                if kind == 'pow':
                    if j % h: continue
                    X = pow(4, -(j // h), m)
                    Y = [sum(c * pow(X, i, m) for i, c in hom) % m for hom in cyc_homs(h, w)]
                elif kind == 'sg':
                    if j % 2: continue
                    a = pow(2, -(j // 2), m)
                    Y = [(a * a + 2 * a * w + 2 * w * w) % m, (a * a - 2 * a * w + 2 * w * w) % m]
                else:
                    if j % 2 == 0: continue
                    b = pow(2, -((j + 1) // 2), m)
                    Y = [(2 * b * b + 2 * b * w + w * w) % m, (2 * b * b - 2 * b * w + w * w) % m]
                tested += 1
                res = ps + [4 ** J] + Y
                rel = relation(res, 2 * j - 2, m)
                if rel: hits.append((kind, j, w, h if kind == 'pow' else '', m, rel))
    return tested, hits

def split_sg1(c0, k, WMAX):
    """sg1, j = 1, w odd, numerators split into primes: relation D1 + 2 D2 = 0 (mod m), D1, D2 disjoint
    sub-multisets of {odd primes of c0, n-atom 4^J, primes of 2w^2+2w+1, primes of 2w^2-2w+1}."""
    J = (c0 + k).bit_length() // 2
    out = []
    for w in range(1, WMAX + 1, 2):
        m = 4 * c0 * w ** 4 - k
        atoms = [p for p, v in factorint(c0).items() for _ in range(v)] + [4 ** J]
        for A in (2 * w * w + 2 * w + 1, 2 * w * w - 2 * w + 1):
            atoms += [p for p, v in factorint(A).items() for _ in range(v)]
        for eps in product((0, 1, 2), repeat=len(atoms)):
            D1 = D2 = 1
            for a, e in zip(atoms, eps):
                if e == 1: D1 *= a
                elif e == 2: D2 *= a
            if (D1 + 2 * D2) % m == 0: out.append((w, m, D1, D2)); break
    return out

if __name__ == '__main__':
    fams = [(3, 1), (7, 9), (23, 41), (39, 25), (15, 1), (31, 33), (7, 57), (63, 1), (47, 17), (55, 9)]
    for c0, k in fams:
        tested, hits = windows_at0(c0, k)
        bad = [h for h in hits if not (h[0] == 'sg1' and h[1] == 1 and h[2] % 2 == 1)]
        print('(%d,%d): %d windows contain mu=0; relations: %s; outside Prop 2.7 survivor shape: %s'
              % (c0, k, tested, [(h[0], h[1], h[2], h[4]) for h in hits][:6], bad))
    print('Part B (split SG numerators, sg1 j=1 w odd <= 15):')
    for c0, k in fams[4:]:
        print('  (%d,%d):' % (c0, k), split_sg1(c0, k, 15))
