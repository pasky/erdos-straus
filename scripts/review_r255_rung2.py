"""R255 from-scratch test of MENU_LADDER Theorem 4.1 (Type II families on n = c0*Y^2 + k).
For each pair (a, b) of small polynomials (positive lc, rational scalar), find ALL (c, d) in Q[Y] with
  c*n = 4abcd - a - b,  i.e.  m := 4abd - n divides a + b  (c = (a+b)/m)  and  4ab | n + m  (d = (n+m)/(4ab)).
m ranges over (positive scalar) x (monic divisor of a+b over Q); the scalar is forced by the linear condition
(n + mu*g) = 0 mod ab unless ab is constant (then mu is free; we sample).  Exhaustive for the given (a, b).
For every family found: check identity, positivity of lcs, deg(abd) = 2, and f = 4acd - 1 mod n is constant.
Polynomials: lists of Fractions, low degree first."""
import sys, itertools
from fractions import Fraction as F

def trim(p):
    p = list(p)
    while p and p[-1] == 0: p.pop()
    return p
def add(p, q):
    r = [F(0)] * max(len(p), len(q))
    for i, x in enumerate(p): r[i] += x
    for i, x in enumerate(q): r[i] += x
    return trim(r)
def scal(c, p): return trim([c * x for x in p])
def mul(p, q):
    if not p or not q: return []
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q): r[i + j] += x * y
    return trim(r)
def divmod_(p, q):
    p = trim(p); q = trim(q); qt = []
    if len(p) < len(q): return [], p
    quo = [F(0)] * (len(p) - len(q) + 1); p = list(p)
    while len(p) >= len(q) and p:
        c = p[-1] / q[-1]; s = len(p) - len(q); quo[s] = c
        for i, y in enumerate(q): p[s + i] -= c * y
        p = trim(p)
    return trim(quo), p
def deg(p): return len(trim(p)) - 1
def lc(p): return trim(p)[-1]
def ev(p, x): return sum(c * x**i for i, c in enumerate(p))

def rational_roots(p):
    """rational roots of p (Fraction coeffs), with multiplicity, plus leftover cofactor"""
    p = trim(p); roots = []
    while deg(p) >= 1:
        # clear denominators
        from math import lcm, gcd
        L = 1
        for c in p: L = lcm(L, c.denominator)
        z = [int(c * L) for c in p]
        if z[0] == 0:
            roots.append(F(0)); p, _ = divmod_(p, [F(0), F(1)]); continue
        def divs(N):
            N = abs(N); return [d for d in range(1, N + 1) if N % d == 0]
        found = None
        for u in divs(z[0]):
            for v in divs(z[-1]):
                for sg in (1, -1):
                    r = F(sg * u, v)
                    if ev(p, r) == 0: found = r; break
                if found is not None: break
            if found is not None: break
        if found is None: break
        roots.append(found); p, rem = divmod_(p, [-found, F(1)]); assert not rem
    return roots, p

def monic_divisors(p):
    roots, rest = rational_roots(p)
    assert deg(rest) <= 3 or True
    pieces = [[-r, F(1)] for r in roots]
    restm = scal(1 / lc(rest), rest) if deg(rest) >= 1 else None
    if restm is not None and deg(restm) >= 4:
        return None  # cannot certify irreducibility of the leftover; skip
    if restm is not None: pieces.append(restm)
    out = set()
    for mask in itertools.product([0, 1], repeat=len(pieces)):
        g = [F(1)]
        for take, pc in zip(mask, pieces):
            if take: g = mul(g, pc)
        out.add(tuple(g))
    return [list(g) for g in out]

def polys(maxdeg, R, lcs):
    for dgr in range(maxdeg + 1):
        for low in itertools.product(range(-R, R + 1), repeat=dgr):
            for l in lcs:
                yield [F(x) for x in low] + [F(l)]

def search(c0, k, maxdeg_a, maxdeg_b, R, scalars):
    n = [F(k), F(0), F(c0)]
    base = list(polys(maxdeg_a, R, (1, 2)))
    A = [scal(F(s), p) for p in base for s in scalars]
    Bbase = list(polys(maxdeg_b, R, (1, 2)))
    B = [scal(F(s), p) for p in Bbase for s in scalars]
    fams = 0; bad = []; shapes = {}; skipped = 0
    for a in A:
        for b in B:
            s = add(a, b); ab = mul(a, b)
            divsr = monic_divisors(s)
            if divsr is None: skipped += 1; continue
            for g in divsr:
                if deg(ab) == 0:
                    mus = [F(1), F(2), F(1, 3)]
                else:
                    _, rn = divmod_(n, ab); _, rg = divmod_(g, ab)
                    rn = trim(rn); rg = trim(rg)
                    if not rg:
                        if rn: continue
                        mus = [F(1), F(2), F(1, 3)]
                    else:
                        # need rn + mu*rg = 0 : mu = -rn[i]/rg[i] consistently
                        i = len(rg) - 1
                        mu = -(rn[i] if i < len(rn) else F(0)) / rg[i]
                        if trim(add(rn, scal(mu, rg))): continue
                        mus = [mu]
                for mu in mus:
                    if mu <= 0: continue
                    m = scal(mu, g)
                    c, r1 = divmod_(s, m); d, r2 = divmod_(add(n, m), scal(F(4), ab))
                    if r1 or r2 or not c or not d: continue
                    if lc(c) <= 0 or lc(d) <= 0: continue
                    # identity
                    lhs = mul(c, n); rhs = add(scal(F(4), mul(mul(ab, c), d)), scal(F(-1), s))
                    assert trim(add(lhs, scal(F(-1), rhs))) == []
                    fams += 1
                    f = add(scal(F(4), mul(mul(a, c), d)), [F(-1)])
                    _, fr = divmod_(f, n)
                    sh = (deg(a), deg(b), deg(c), deg(d), deg(m))
                    shapes[sh] = shapes.get(sh, 0) + 1
                    if deg(mul(ab, d)) != 2 or deg(fr) >= 1:
                        bad.append((a, b, c, d, m, fr))
    return fams, shapes, bad, skipped

if __name__ == '__main__':
    c0, k, da, db, R = map(int, sys.argv[1:6])
    scalars = [F(1), F(2), F(1, 2), F(3), F(1, 3), F(1, 4), F(4)]
    fams, shapes, bad, skipped = search(c0, k, da, db, R, scalars)
    print(f'c0={c0} k={k} deg a<={da} deg b<={db} R={R}: families={fams} skipped(a+b with deg>=4 leftover)={skipped}')
    print('shapes (deg a, deg b, deg c, deg d, deg m): count', dict(sorted(shapes.items())))
    print('VIOLATIONS (deg(abd)!=2 or nonconstant f mod n):', len(bad))
    for x in bad[:5]: print(x)
