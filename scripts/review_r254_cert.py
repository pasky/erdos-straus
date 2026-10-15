# review_r254_cert.py -- R254 FROM-SCRATCH checker for the z14 tree certificates (no z14_/z8/ec_cover imports).
# Usage: PYTHONPATH=scripts uv run python scripts/review_r254_cert.py c0 k cert.txt SMAX
# Proof part (all s >= 0):
#   * parse DFS preorder tree; each leaf = cylinder {s : s = u mod L}; children of "S l" partition the parent
#     (mu_l mod l^{e+1} refines mu_l mod l^e).  Haar measures summed exactly (Fraction) must equal 1.
#   * every leaf is checked to give a solution for ALL s = u (mod L) with s >= s0(leaf); s < s0 collected as exceptions.
#     D q : q prime, ord_q(4) | L, q | c0*4^u + k  -> q | n_s on whole cylinder; ES(q) solved explicitly.
#     P a d f (II2) : f = -1 (mod 4ad), f | n + 4a^2 d on the cylinder (ord of each prime power of f divides L).
#     I c d f (I3)  : gcd(f,4cd)=1, n = -f (mod 4cd) on cylinder, f | n^2 + 4c^2 d.
#     W m j code w h: window; residues of all pieces mod m depend on s mod P with P | L; relation searched here.
#   * identities verified symbolically (sympy) below.
# Sanity part: explicit solution for every s <= SMAX built from the leaf covering s and verified exactly.
import sys
from fractions import Fraction as Fr
from math import gcd, prod
from itertools import product as iprod
import sympy as sp
from sympy import isprime, n_order, factorint, totient

c0, k, path, SMAX = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
toks = [ln.split() for ln in open(path) if ln.strip()]
pos = [0]
LEAVES = []  # (u, L, tok)


def crt(res):  # res: dict l -> (c, e)  -> (u, L)
    u, L = 0, 1
    for l, (c, e) in res.items():
        md = l ** e
        # solve x = u mod L, x = c mod md
        t = ((c - u) * pow(L, -1, md)) % md
        u, L = u + L * t, L * md
    return u % L, L


def walk(res):
    t = toks[pos[0]]; pos[0] += 1
    if t[0] == 'S':
        l = int(t[1]); assert isprime(l)
        c, e = res.get(l, (0, 0))
        for i in range(l):
            r2 = dict(res); r2[l] = (c + i * l ** e, e + 1); walk(r2)
        return
    assert t[0] in 'DPIW', t
    u, L = crt(res); LEAVES.append((u, L, t))


walk({})
assert pos[0] == len(toks), 'trailing tokens'
meas = sum(Fr(1, L) for (_, L, _) in LEAVES)
assert meas == 1, meas
print('leaves', len(LEAVES), 'measure', meas, 'kinds', {c: sum(1 for x in LEAVES if x[2][0] == c) for c in 'DPIW'})


# ---------- symbolic identities ----------
def sym_identities():
    n, a, d, f, c = sp.symbols('n a d f c', positive=True)
    C = (f + 1) / (4 * a * d); e = (n + 4 * a * a * d) / f; b = C * e - a
    assert sp.simplify(1 / (a * b * d) + 1 / (a * C * d * n) + 1 / (b * C * d * n) - 4 / n) == 0
    A = (n + f) / (4 * c * d); B = (n ** 2 + 4 * c * c * d + n * f) / (4 * c * d * f)
    assert sp.simplify(1 / (A * B * d * n) + 1 / (A * c * d) + 1 / (B * c * d) - 4 / n) == 0
    # window: x = (n+m)/4, N = n x, d1,d2 | N, m | d1+d2
    m, N, d1, d2 = sp.symbols('m N d1 d2', positive=True)
    x = (n + m) / 4
    y = n * x * (d1 + d2) / (m * d2); z = n * x * (d1 + d2) / (m * d1)
    assert sp.simplify(1 / x + 1 / y + 1 / z - 4 / n) == 0
    # Sophie Germain identities
    X, w = sp.symbols('X w')
    assert sp.expand((X**2 + 2*X*w + 2*w**2) * (X**2 - 2*X*w + 2*w**2) - (X**4 + 4*w**4)) == 0
    assert sp.expand((2*X**2 + 2*X*w + w**2) * (2*X**2 - 2*X*w + w**2) - (4*X**4 + w**4)) == 0


sym_identities()


def ordp(q, e=1):  # multiplicative order of 4 mod q^e
    return n_order(4, q ** e)


def nres(s_mod_list, M):  # helper
    pass


def window_pieces_poly(code, w, h):
    """returns (t, list of integer-coefficient polynomials in X, description of X as function of r)."""
    X = sp.Symbol('X')
    if code == 0:
        t = w ** h
        polys = []
        for e in sp.divisors(h):
            ph = sp.Poly(sp.cyclotomic_poly(2 * e, X), X); D = ph.degree()
            polys.append(sp.Poly(sum(cf * X ** i * w ** (D - i) for (i,), cf in ph.terms()), X))
        assert sp.expand(prod(p.as_expr() for p in polys) - (X ** h + t)) == 0
        return t, polys
    if code == 1:
        t = 4 * w ** 4
        return t, [sp.Poly(X**2 + 2*X*w + 2*w**2, X), sp.Poly(X**2 - 2*X*w + 2*w**2, X)]
    if code == 2:
        t = w ** 4
        return t, [sp.Poly(2*X**2 + 2*X*w + w**2, X), sp.Poly(2*X**2 - 2*X*w + w**2, X)]
    raise ValueError


def Xval(code, h, r, mod=None):
    # code 0: X = 4^{r/h} (h | r); code 1: X = 2^{r/2} (r even), X^4 = 4^r; code 2: X = 2^{(r-1)/2} (r odd), 4X^4 = 4^r
    if code == 0:
        assert r % h == 0; ex, base = r // h, 4
    elif code == 1:
        assert r % 2 == 0; ex, base = r // 2, 2
    else:
        assert r % 2 == 1; ex, base = (r - 1) // 2, 2
    return pow(base, ex, mod) if mod else base ** ex


def peval(p, v, mod=None):
    acc = 0
    for cf in p.all_coeffs():
        acc = acc * v + int(cf)
        if mod: acc %= mod
    return acc


def find_rel(vals, m, E):
    """vals: list of piece values (residues or ints). find eps in {-1,0,1}^len, i in [0,E] with
    2^i * prod_{eps=1} + prod_{eps=-1} = 0 mod m, or prod_{eps=1} + 2^i prod_{eps=-1} = 0 mod m."""
    for eps in iprod((-1, 0, 1), repeat=len(vals)):
        p1 = prod(v for v, e in zip(vals, eps) if e == 1) % m
        p2 = prod(v for v, e in zip(vals, eps) if e == -1) % m
        for i in range(E + 1):
            if (pow(2, i, m) * p1 + p2) % m == 0 and (p1 or p2):
                return eps, i
    return None


def wleaf(u, L, t):
    """check window leaf on whole cylinder; returns s0 such that all s >= s0 in cylinder are covered."""
    m, j, code, w, h = map(int, t[1:6])
    tt, polys = window_pieces_poly(code, w, h)
    assert m == c0 * 4 ** j * tt - k and m > 1 and m % 2 == 1 and j >= 1
    # period of residues: n mod m: ord_m(4); X mod m: code0 -> r/h mod ord_m(4) => r mod h*ord_m(4); codes1/2 -> r mod 2*ord_m(2)
    o4, o2 = n_order(4, m), n_order(2, m)
    P = h * o4 if code == 0 else 2 * o2
    assert P % o4 == 0
    assert L % P == 0, ('period', P, L)
    r = (u - j) % P  # representative of r mod P; conditions h|r / parity well defined as h|P, 2|P
    vX = Xval(code, h, r, m)
    v2c = (c0 & -c0).bit_length() - 1; co = c0 >> v2c
    E = 2 * j - 2 + v2c
    ys = [peval(p, vX, m) for p in polys]
    nm = (c0 * pow(4, u % o4, m) + k) % m
    vals = [q for q, v in factorint(co).items() for _ in range(v)] + [nm] + ys
    rel = find_rel(vals, m, E)
    assert rel, ('window does not fire', u, L, t)
    return j + 1  # r >= 1 guaranteed for s >= j+1


def leaf_ok(u, L, t):
    """returns s0: leaf identity valid for all s = u mod L, s >= s0."""
    if t[0] == 'D':
        q = int(t[1]); assert isprime(q) and L % ordp(q) == 0 and (c0 * pow(4, u, q) + k) % q == 0
        return 0
    if t[0] == 'W':
        return wleaf(u, L, t)
    a, d = int(t[1]), int(t[2]); f = prod(int(x) for x in t[3:]); assert a >= 1 and d >= 1 and f > 1
    for q, e in factorint(f).items():
        assert L % ordp(q, e) == 0
    nf = (c0 * pow(4, u, f) + k) % f
    if t[0] == 'P':
        assert (f + 1) % (4 * a * d) == 0 and (nf + 4 * a * a * d) % f == 0
        # b = c e - a > 0 iff c (n+4a^2 d) > a f ; n_s increasing in s
        C = (f + 1) // (4 * a * d); s0 = 0
        while C * (c0 * 4 ** s0 + k + 4 * a * a * d) <= a * f: s0 += 1
        return s0
    M = 4 * a * d  # here a = c (I3 parameter)
    assert gcd(f, M) == 1 and (nf * nf + 4 * a * a * d) % f == 0
    v2 = (M & -M).bit_length() - 1; Mo = M >> v2
    if Mo > 1: assert L % n_order(4, Mo) == 0
    # for 2s + v2(c0) >= v2: n = c0*4^s + k mod M is determined by u mod L ; s0 accordingly
    v2c = (c0 & -c0).bit_length() - 1; s0 = 0
    while 2 * s0 + v2c < v2: s0 += 1
    s1 = u + ((s0 - u + L - 1) // L) * L if s0 > u else u  # first cylinder member >= s0
    assert (c0 * pow(4, s1, M) + k + f) % M == 0
    return s0


def es_small(n):
    """explicit ES solution via 4/n = 1/x + 1/y + 1/z, brute: x in (n/4, ...), then 1/y+1/z = p/q via divisors of q^2."""
    for x in range(n // 4 + 1, n // 4 + 5000):
        p, q = 4 * x - n, n * x
        g = gcd(p, q); p //= g; q //= g
        # 1/y + 1/z = p/q : (py - q)(pz - q) = q^2
        for dd in sp.divisors(q * q):
            if dd > q: break
            if (dd + q) % p == 0 and (q * q // dd + q) % p == 0:
                y, z = (dd + q) // p, (q * q // dd + q) // p
                assert 4 * x * y * z == n * (x * y + y * z + z * x)
                return x, y, z
    return None


exc = set()
for (u, L, t) in LEAVES:
    s0 = leaf_ok(u, L, t)
    for s in range(u, s0, L): exc.add(s)
for s in sorted(exc):
    assert es_small(c0 * 4 ** s + k), s
print('cylinder checks OK; exceptions (checked directly):', sorted(exc))


# ---------- explicit sanity: s <= SMAX ----------
def explicit(s, t):
    n = c0 * 4 ** s + k
    if t[0] == 'D':
        q = int(t[1]); assert n % q == 0
        x, y, z = es_small(q); return x * (n // q), y * (n // q), z * (n // q)
    if t[0] == 'P':
        a, d = int(t[1]), int(t[2]); f = prod(int(x) for x in t[3:]); C = (f + 1) // (4 * a * d)
        assert (n + 4 * a * a * d) % f == 0
        e = (n + 4 * a * a * d) // f; b = C * e - a; assert b > 0
        return a * b * d, a * C * d * n, b * C * d * n
    if t[0] == 'I':
        c, d = int(t[1]), int(t[2]); f = prod(int(x) for x in t[3:])
        assert (n + f) % (4 * c * d) == 0 and (n * n + 4 * c * c * d + n * f) % (4 * c * d * f) == 0
        A = (n + f) // (4 * c * d); B = (n * n + 4 * c * c * d + n * f) // (4 * c * d * f)
        return A * B * d * n, A * c * d, B * c * d
    m, j, code, w, h = map(int, t[1:6]); r = s - j; assert r >= 1
    tt, polys = window_pieces_poly(code, w, h)
    X = Xval(code, h, r); ys = [peval(p, X) for p in polys]
    assert prod(ys) == 4 ** r + tt
    x = (n + m) // 4; assert 4 * x - n == m and x == c0 * 4 ** (j - 1) * (4 ** r + tt)
    v2c = (c0 & -c0).bit_length() - 1; co = c0 >> v2c; E = 2 * j - 2 + v2c
    vals = [q for q, v in factorint(co).items() for _ in range(v)] + [n] + ys
    N = n * x; assert 2 ** E * prod(vals) == N
    eps, i = find_rel(vals, m, E)
    d1 = 2 ** i * prod(v for v, e in zip(vals, eps) if e == 1); d2 = prod(v for v, e in zip(vals, eps) if e == -1)
    assert N % d1 == 0 and N % d2 == 0 and (d1 + d2) % m == 0
    return x, N * (d1 + d2) // (m * d2), N * (d1 + d2) // (m * d1)


cnt = 0
for s in range(SMAX + 1):
    lf = [t for (u, L, t) in LEAVES if s % L == u]
    assert len(lf) == 1, (s, lf)
    if s in exc:
        continue
    x, y, z = explicit(s, lf[0]); n = c0 * 4 ** s + k
    assert min(x, y, z) > 0 and 4 * x * y * z == n * (x * y + y * z + z * x), s
    cnt += 1
print('explicit solutions verified for', cnt, 's <= %d (+%d exceptions direct)' % (SMAX, len([e for e in exc if e <= SMAX])))
