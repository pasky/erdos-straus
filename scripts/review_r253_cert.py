# review_r253_cert.py — R253 FROM-SCRATCH checker for the z14 tree certificates (no z14_/z8/ec_cover imports).
# Usage: PYTHONPATH=scripts uv run python scripts/review_r253_cert.py c0 k cert.txt [SMAX]
# Independent semantics (derived from EXP_105 §2 and ET Prop 1.9, not from z14_check.py):
#  * tree: DFS preorder; "S l" splits node {mu : mu = u mod L} into l children by mu mod l^{e_l+1}.
#  * D q : q prime, q | n_s on the whole class (needs ord_q(4) | L and n_u = 0 mod q); ES(n) = (n/q)*ES(q).
#  * P a d f : II2 identity x = abd, y = acdn, z = bcdn, c = (f+1)/(4ad), e = (n+4a^2 d)/f, b = ce - a.
#  * I c d f : I3 identity a = (n+f)/(4cd), b = (n^2+4c^2 d+nf)/(4cdf); x = abdn, y = acd, z = bcd.
#  * W m j code w h : x = (n+m)/4, N = n x, pieces of N; relation d1 + d2 = 0 mod m found HERE by own search.
# Coverage: exact Haar measure sum (Fractions) == 1 plus, for every s <= SMAX, exactly one leaf contains s and
# that leaf yields an explicit verified solution (else s must be solved by an independent search).
import sys
from fractions import Fraction as Fr
from math import gcd, prod
from itertools import product as iprod
from sympy import isprime, n_order, factorint, symbols, expand, cancel, cyclotomic_poly, Poly, divisors

c0, k = int(sys.argv[1]), int(sys.argv[2]); toks = [ln.split() for ln in open(sys.argv[3]) if ln.strip()]
SMAX = int(sys.argv[4]) if len(sys.argv) > 4 else 1500
pos = [0]; leaves = []; meas = [Fr(0)]


def crt(e, c):
    u, M = 0, 1
    for l, v in e.items():
        md = l ** v
        while u % md != c[l] % md: u += M
        M *= md
    return u % M, M


def walk(e, c):
    t = toks[pos[0]]; pos[0] += 1
    if t[0] == 'S':
        l = int(t[1]); assert isprime(l)
        v = e.get(l, 0)
        for i in range(l):
            e2, c2 = dict(e), dict(c); e2[l] = v + 1; c2[l] = c.get(l, 0) + i * l ** v
            walk(e2, c2)
        return
    u, L = crt(e, c)
    meas[0] += Fr(1, L); leaves.append((u, L, t))


walk({}, {}); assert pos[0] == len(toks), 'trailing tokens'
assert meas[0] == 1, meas[0]

# ---- symbolic identities (own derivation) ----
nn, a_, d_, f_, c_ = symbols('n a d f c', positive=True)
cc = (f_ + 1) / (4 * a_ * d_); e_ = (nn + 4 * a_ ** 2 * d_) / f_; b_ = cc * e_ - a_
assert cancel(1 / (a_ * b_ * d_) + 1 / (a_ * cc * d_ * nn) + 1 / (b_ * cc * d_ * nn) - 4 / nn) == 0
A_ = (nn + f_) / (4 * c_ * d_); B_ = (nn ** 2 + 4 * c_ ** 2 * d_ + nn * f_) / (4 * c_ * d_ * f_)
assert cancel(1 / (A_ * B_ * d_ * nn) + 1 / (A_ * c_ * d_) + 1 / (B_ * c_ * d_) - 4 / nn) == 0

def nval(s): return c0 * 4 ** s + k

def ok_sol(n, x, y, z): return min(x, y, z) > 0 and 4 * x * y * z == n * (x * y + y * z + x * z)

ESQ = {}
def es_small(n):
    """independent ES search: x from n//4+1, then 4/n-1/x = p/q, y range, z exact."""
    if n in ESQ: return ESQ[n]
    for x in range(n // 4 + 1, 3 * n):
        p, q = 4 * x - n, n * x; g = gcd(p, q); p //= g; q //= g
        if p == 1: ESQ[n] = (x, 2 * q, 2 * q); return ESQ[n]
        for y in range(q // p + 1, 2 * q // p + 1):
            P2, Q2 = p * y - q, q * y
            if P2 > 0 and Q2 % P2 == 0: ESQ[n] = (x, y, Q2 // P2); return ESQ[n]
    raise AssertionError(n)


def win_pieces(s, m, j, code, w, h):
    """integer pieces of N = n x, or None if s not in the window's arithmetic domain."""
    n = nval(s); r = s - j
    if r < 0: return None
    if code == 0:
        if r % h: return None
        X, t = 4 ** (r // h), w ** h
        Ys = []
        for e in divisors(h):
            p = Poly(cyclotomic_poly(2 * e, symbols('X')))
            D = p.degree(); Ys.append(sum(int(cf) * X ** i * w ** (D - i) for (i,), cf in p.terms()))
    elif code == 1:
        if r % 2: return None
        X, t = 2 ** (r // 2), 4 * w ** 4
        Ys = [X * X + 2 * X * w + 2 * w * w, X * X - 2 * X * w + 2 * w * w]
    else:
        if r % 2 == 0: return None
        X, t = 2 ** ((r - 1) // 2), w ** 4
        Ys = [2 * X * X + 2 * X * w + w * w, 2 * X * X - 2 * X * w + w * w]
    assert m == c0 * 4 ** j * t - k and m % 2 == 1 and m > 0
    assert prod(Ys) == 4 ** r + t
    x = (n + m) // 4; assert 4 * x == n + m
    v2 = (c0 & -c0).bit_length() - 1; oc = c0 >> v2
    E = 2 * j - 2 + v2
    pcs = [p for p, v in factorint(oc).items() for _ in range(v)] + [n] + Ys
    assert 2 ** E * prod(pcs) == n * x
    return n, x, E, pcs


def win_relation(res, E, m):
    """own search: disjoint subsets S1,S2, 2^i (i in [-E,E]) with 2^{i+} prod S1 + 2^{i-} prod S2 = 0 mod m."""
    for eps in iprod((0, 1, -1), repeat=len(res)):
        d1 = prod(r for r, e in zip(res, eps) if e == 1) % m; d2 = prod(r for r, e in zip(res, eps) if e == -1) % m
        for i in range(0, E + 1):
            if (d1 * pow(2, i, m) + d2) % m == 0: return eps, i
            if (d1 + d2 * pow(2, i, m)) % m == 0: return eps, -i
    return None


def window_class_check(u, L, m, j, code, w, h):
    """prove: for all s = u mod L with r=s-j large enough, the residues of all pieces mod m are those at a fixed
    representative; via the period conditions, then find a relation on residues."""
    o4, o2 = n_order(4, m), n_order(2, m)
    assert L % o4 == 0                                   # n mod m periodic
    if code == 0: assert L % h == 0 and (u - j) % h == 0 and (L // h) % o4 == 0
    else:
        assert L % 2 == 0 and (L // 2) % o2 == 0
        assert (u - j) % 2 == (0 if code == 1 else 1)
    s0 = u
    while s0 - j < 1: s0 += L
    n, x, E, pcs = win_pieces(s0, m, j, code, w, h)
    rel = win_relation([p % m for p in pcs], E, m); assert rel, ('no relation', u, L, m)
    return rel


def explicit(s, t, rels):
    n = nval(s)
    if t[0] == 'D':
        q = int(t[1])
        if n % q: return None
        X = es_small(q); return tuple(v * (n // q) for v in X)
    if t[0] == 'P':
        a, d = int(t[1]), int(t[2]); f = prod(map(int, t[3:]))
        if (f + 1) % (4 * a * d) or (n + 4 * a * a * d) % f: return None
        c = (f + 1) // (4 * a * d); e = (n + 4 * a * a * d) // f; b = c * e - a
        return (a * b * d, a * c * d * n, b * c * d * n) if b > 0 else None
    if t[0] == 'I':
        c, d = int(t[1]), int(t[2]); f = prod(map(int, t[3:]))
        if (n + f) % (4 * c * d) or (n * n + 4 * c * c * d) % f: return None
        a = (n + f) // (4 * c * d); b = (n * n + 4 * c * c * d + n * f) // (4 * c * d * f)
        return (a * b * d * n, a * c * d, b * c * d)
    m, j, code, w, h = map(int, t[1:6])
    W = win_pieces(s, m, j, code, w, h)
    if W is None: return None
    n, x, E, pcs = W; eps, i = rels
    d1 = prod(p for p, e in zip(pcs, eps) if e == 1) * 2 ** max(i, 0)
    d2 = prod(p for p, e in zip(pcs, eps) if e == -1) * 2 ** max(-i, 0)
    N = n * x
    if (d1 + d2) % m or N % d1 or N % d2: return None
    return (x, N * (d1 + d2) // (m * d2), N * (d1 + d2) // (m * d1))


cnt = {}
rels = {}
for (u, L, t) in leaves:
    cnt[t[0]] = cnt.get(t[0], 0) + 1
    if t[0] == 'D':
        q = int(t[1]); assert isprime(q) and L % n_order(4, q) == 0 and nval(u) % q == 0 and k % q and c0 % q
    elif t[0] in 'PI':
        a, d = int(t[1]), int(t[2]); qs = list(map(int, t[3:])); f = prod(qs)
        assert a >= 1 and d >= 1 and all(isprime(q) for q in qs) and len(set(qs)) == len(qs)
        assert all(q > 2 and (c0 % q == 0 or L % n_order(4, q) == 0) for q in qs)  # n mod q periodic on class
        if t[0] == 'P':
            assert (f + 1) % (4 * a * d) == 0 and (nval(u) + 4 * a * a * d) % f == 0
        else:
            M4 = 4 * a * d; assert gcd(f, M4) == 1
            assert (nval(u) * nval(u) + 4 * a * a * d) % f == 0
            wo = M4 >> ((M4 & -M4).bit_length() - 1)
            if wo > 1: assert L % n_order(4, wo) == 0
            # n_s mod 4cd constant for s = u mod L once 4^s = 0 mod 2-part: check at a large representative
            s0 = u + L * (1 + 40 // L)
            assert (nval(s0) + f) % M4 == 0
    else:
        rels[(u, L)] = window_class_check(u, L, *map(int, t[1:6]))

bad = []; nexp = 0
for s in range(SMAX + 1):
    lf = [(u, L, t) for (u, L, t) in leaves if s % L == u]
    assert len(lf) == 1, (s, lf)
    u, L, t = lf[0]
    sol = explicit(s, t, rels.get((u, L)))
    n = nval(s)
    if sol is None:
        sol = es_small(n); bad.append(s)
    assert ok_sol(n, *sol), s
    nexp += 1
print('OK c0=%d k=%d leaves=%d %s measure=%s; explicit solutions verified for all s<=%d; '
      'leaf did not apply (solved by independent search) at s=%s' % (c0, k, len(leaves), cnt, meas[0], SMAX, bad))
