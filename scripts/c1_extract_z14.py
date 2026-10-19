# c1_extract_z14.py -- helper for O277 (paper es-exponential-families): flatten a z14 tree certificate
# (data/z14/cert_c*_k*.txt, format documented in scripts/z14_check.py) into an explicit list of leaves
#   (u, L, token, relation)
# where the node is {s : s = u (mod L)} and, for window leaves, relation = (eps, i) is the explicit
# relation  -1 = 2^i * prod piece^eps  (mod m)  found at this node (pieces = odd primes of c0, n, Y-pieces).
# The output is embedded (after reformatting) in scripts/c1_expfam_verify.py, which re-verifies everything
# from scratch; this helper is NOT part of the verification.
# Usage: PYTHONPATH=scripts uv run python scripts/c1_extract_z14.py c0,k cert.txt > out.json
import sys, json
from math import gcd, prod
from itertools import product as iprod
from sympy import isprime, n_order, factorint, Symbol, cyclotomic_poly, expand, divisors, Poly, lambdify

c0, k = map(int, sys.argv[1].split(','))
lines = (ln.split() for ln in open(sys.argv[2]))
OUT = []


def homs_for(code, w, h):
    if code == 0:
        X = Symbol('X')
        res = []
        for e in divisors(h):
            p = Poly(cyclotomic_poly(2 * e, X), X)
            res.append(expand(sum(cf * X ** i * w ** (p.degree() - i) for (i,), cf in p.terms())))
        return res, X
    if code == 1:
        a = Symbol('a'); return [a * a + 2 * a * w + 2 * w * w, a * a - 2 * a * w + 2 * w * w], a
    b = Symbol('b'); return [2 * b * b + 2 * b * w + w * w, 2 * b * b - 2 * b * w + w * w], b


def window_relation(t, L, u):
    m, j, code, w, h = map(int, t[1:6])
    homs, var = homs_for(code, w, h)
    fns = [lambdify(var, e) for e in homs]
    P = h * n_order(4, m) if code == 0 else 2 * n_order(2, m)
    assert L % P == 0
    rr = (u - j) % P
    if code == 0: V = pow(4, rr // h, m)
    elif code == 1: V = pow(2, rr // 2, m)
    else: V = pow(2, (rr - 1) // 2, m)
    ys = [int(f(V)) % m for f in fns]
    nm = (c0 * pow(4, u, m) + k) % m
    oc = c0
    while oc % 2 == 0: oc //= 2
    E = 2 * j - 2 + ((c0 & -c0).bit_length() - 1)
    pieces = [p for p, v in factorint(oc).items() for _ in range(v)] if oc > 1 else []
    res = [p % m for p in pieces] + [nm] + ys
    best = None
    for eps in iprod((-1, 0, 1), repeat=len(res)):
        v = 1; ok = True
        for r_, e_ in zip(res, eps):
            if e_ == 0: continue
            if gcd(r_, m) != 1: ok = False; break
            v = v * pow(r_, e_, m) % m
        if not ok: continue
        for i in range(-E, E + 1):
            if v * pow(2, i, m) % m == m - 1:
                cand = (sum(abs(x) for x in eps) + abs(i), eps, i)
                if best is None or cand < best: best = cand
    assert best, 'no relation'
    return {'eps': list(best[1]), 'i': best[2], 'P': P, 'pieces_const': pieces}


def walk(e, c):
    t = next(lines)
    L = prod(l ** v for l, v in e.items())
    u, M = 0, 1
    for l, v in e.items():
        md = l ** v
        u = u + M * (((c[l] - u) * pow(M, -1, md)) % md); M *= md
    if t[0] == 'S':
        l = int(t[1]); v = e.get(l, 0); base = c.get(l, 0)
        for jj in range(l):
            e2 = dict(e); c2 = dict(c); e2[l] = v + 1; c2[l] = base + jj * l ** v
            walk(e2, c2)
        return
    rec = {'u': u, 'L': L, 'tok': t}
    if t[0] == 'W':
        rec['rel'] = window_relation(t, L, u)
    OUT.append(rec)


sys.setrecursionlimit(10000)
walk({}, {})
print(json.dumps(OUT))
