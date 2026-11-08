#!/usr/bin/env python3
"""z66 IE1 kill test K1: search for (*) and ES solutions in M_E = Z + xQ[x] (x positive infinite).

Elements of M_E: polynomials in x with rational coefficients and integer constant term; order = sign of the
leading coefficient (x -> +infinity).  For a target n in M_E we enumerate u, C (resp. X, Y) in a finite box of
M_E of degree <= DEG and solve for the third unknown by exact polynomial division, then check membership in M_E
and positivity (>= 1 in the discrete order).

Theory (Z66_IE1.md Thm E): for n(0) = 1 (n = x+1, x^2+1, ...) there are NO solutions at all.  Positive controls:
n = 8x + 5 (landing value 5) must have (*) solutions; n = x + 2 (landing 2) must have ES solutions.

Usage: python3 scripts/z66_ie1_k1_search.py [DEG] [HNUM] [HDEN] [HCONST]
"""
import sys
from fractions import Fraction as F
from itertools import product

DEG = int(sys.argv[1]) if len(sys.argv) > 1 else 2
HNUM = int(sys.argv[2]) if len(sys.argv) > 2 else 3
HDEN = int(sys.argv[3]) if len(sys.argv) > 3 else 3
HCONST = int(sys.argv[4]) if len(sys.argv) > 4 else 6


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(p, q):
    n = max(len(p), len(q))
    return trim([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)])


def scal(c, p):
    return trim([c * a for a in p])


def mul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                r[i + j] += a * b
    return trim(r)


def divexact(p, q):
    """return p/q if q divides p in Q[x], else None"""
    p = list(trim(p))
    q = trim(q)
    if q == (0,):
        return None
    dq = len(q) - 1
    if len(p) - 1 < dq:
        return (F(0),) if all(a == 0 for a in p) else None
    out = [F(0)] * (len(p) - dq)
    for k in range(len(p) - 1 - dq, -1, -1):
        c = p[k + dq] / q[dq]
        out[k] = c
        for j in range(dq + 1):
            p[k + j] -= c * q[j]
    if any(a != 0 for a in p):
        return None
    return trim(out)


def in_ME(p):
    return p[0].denominator == 1


def geq1(p):  # p >= 1 in the order of M_E (p in M_E assumed)
    p = trim(p)
    if len(p) == 1:
        return p[0] >= 1
    return p[-1] > 0


rats = sorted({F(a, b) for a in range(-HNUM, HNUM + 1) for b in range(1, HDEN + 1)})
elems = []
for c0 in range(-HCONST, HCONST + 1):
    for tail in product(rats, repeat=DEG):
        p = trim((F(c0),) + tuple(tail))
        if geq1(p):
            elems.append(p)
elems = sorted(set(elems))

ONE = (F(1),)


def star_search(n, limit=5):
    sols = []
    for u in elems:
        nu = add(n, u)
        for C in elems:
            d = add(scal(F(4), mul(u, C)), (F(-1),))   # 4uC - 1
            B = divexact(nu, d)
            if B is None or not in_ME(B) or not geq1(B):
                continue
            sols.append((u, B, C))
            if len(sols) >= limit:
                return sols
    return sols


def es_search(n, limit=5):
    # 4XYZ = n(XY+YZ+ZX)  =>  Z (4XY - nX - nY) = nXY
    sols = []
    for X in elems:
        for Y in elems:
            if Y < X:
                continue
            den = add(scal(F(4), mul(X, Y)), scal(F(-1), mul(n, add(X, Y))))
            if den == (0,):
                continue
            Z = divexact(mul(n, mul(X, Y)), den)
            if Z is None or not in_ME(Z) or not geq1(Z):
                continue
            sols.append((X, Y, Z))
            if len(sols) >= limit:
                return sols
    return sols


def show(p):
    return " + ".join(f"({a})x^{i}" for i, a in enumerate(p) if a != 0) or "0"


targets = [("x+1", (F(1), F(1))), ("x^2+1", (F(1), F(0), F(1))), ("x/840*840+1 = 840x+1", (F(1), F(840))),
           ("CONTROL 8x+5", (F(5), F(8))), ("CONTROL x+2 (landing 2)", (F(2), F(1)))]
print(f"K1: box DEG<={DEG}, numerators<={HNUM}, denominators<={HDEN}, |const|<={HCONST}; {len(elems)} positive elements")
for name, n in targets:
    s1 = star_search(n)
    s2 = es_search(n)
    print(f"n = {name}: (*) solutions found: {len(s1)}; ES solutions found: {len(s2)}")
    for (a, b, c) in s1[:2]:
        print(f"   (*) u={show(a)}  B={show(b)}  C={show(c)}")
    for (a, b, c) in s2[:2]:
        print(f"   ES  x={show(a)}  y={show(b)}  z={show(c)}")
