# z14_check.py — independent replay checker for z14 tree certificates of ES on n_s = 4^s + k (s >= 0).
# Uses only exact integer arithmetic + sympy primality/order; does NOT import the search code or mordell_lib.
# Stream format (one token line per node, DFS preorder):
#   "S l"              split current node on prime l: children j = 0..l-1 get mu_l = c_l + j*l^{e_l} (mod l^{e_l+1})
#   "D q"              leaf: prime q | n_s for all s in the node, q !| k  (ES(n) follows from ES(q), shown explicitly)
#   "P a d q1 .. qr"   leaf, ET family II2: f = q1..qr (distinct primes), f = -1 mod 4ad, f | n + 4a^2 d
#   "I c d q1 .. qr"   leaf, ET family I3:  gcd(f,4cd) = 1, n = -f mod 4cd, f | n^2 + 4c^2 d
#   "X" stuck / "ABORT" -> certificate invalid.
# Node data: residue u = mu mod L, L = prod l^{e_l}.  A leaf's class must have period dividing L: ord_q(4) | L for every
# prime q of f, and for I3 also ord_w(4) | L, w = odd part of 4cd.  Then for every integer s = u mod L, s >= s_min,
# the class identity gives an explicit positive solution (checked symbolically once per family below); members below
# s_min are checked directly with an explicit solution.
#   "W m j code w h"   leaf, exponential window class (see below)
# Family n_s = c0*4^s + k.
# Usage: PYTHONPATH=scripts uv run python scripts/z14_check.py [c0,]k cert.txt[.gz] [--allow-stuck]
# Window class W: m = c0*4^j*t - k (t = w^h for code 0, 4w^4 for code 1, w^4 for code 2), x = (n+m)/4 = c0*4^{j-1}(4^r+t),
# r = s - j; N = n*x is written as an explicit product of pieces (2^E, odd primes of c0, n, and the algebraic factors of
# 4^r + t: homogenised cyclotomic pieces for code 0 (h | r), Sophie Germain pieces for codes 1 (r even) / 2 (r odd)).
# The checker verifies symbolically that the pieces multiply to N, finds itself a relation d1 + d2 = 0 (mod m) between
# sub-products (from residues, which are periodic with period P | L), and then y = N(d1+d2)/(m d2), z = N(d1+d2)/(m d1).
import sys, gzip
from fractions import Fraction as Fr
from math import gcd, prod
from sympy import isprime, n_order, factorint, symbols, simplify, divisors

c0, k = map(int, sys.argv[1].split(',')) if ',' in sys.argv[1] else (1, int(sys.argv[1])); path = sys.argv[2]
ALLOW = '--allow-stuck' in sys.argv  # report exact uncovered measure instead of failing
UNC = [Fr(0)]
EXPL = int(sys.argv[sys.argv.index('--explicit') + 1]) if '--explicit' in sys.argv else 0  # build+verify solutions s <= EXPL
LEAVES = []
fh = gzip.open(path, 'rt') if path.endswith('.gz') else open(path)
lines = (ln.split() for ln in fh)


def check_identities():
    n, a, d, f, c = symbols('n a d f c', positive=True)
    # II2: c = (f+1)/(4ad), e = (n+4a^2 d)/f, b = c e - a; x = abd, y = acdn, z = bcdn
    cc = (f + 1) / (4 * a * d); e = (n + 4 * a * a * d) / f; b = cc * e - a
    assert simplify(1 / (a * b * d) + 1 / (a * cc * d * n) + 1 / (b * cc * d * n) - 4 / n) == 0
    # I3 (c,d,f): a = (n+f)/(4cd), b = (n^2 + 4c^2 d + n f)/(4cdf); x = abdn, y = acd, z = bcd
    A = (n + f) / (4 * c * d); B = (n * n + 4 * c * c * d + n * f) / (4 * c * d * f)
    assert simplify(1 / (A * B * d * n) + 1 / (A * c * d) + 1 / (B * c * d) - 4 / n) == 0


def es_explicit(N):
    """explicit (x,y,z) with 4/N = 1/x+1/y+1/z, by the divisor method on 4/N - 1/x = m/(Nx)."""
    for x in range(N // 4 + 1, N // 4 + 2000):
        m, M = 4 * x - N, N * x
        if m <= 0: continue
        g = gcd(m, M); m //= g; M //= g
        if m == 1: return (x, 2 * M, 2 * M)
        fM = factorint(M)
        for dd in divisors(prod(p ** (2 * v) for p, v in fM.items())):
            if dd > M: break
            if (M + dd) % m == 0 and (M + M * M // dd) % m == 0:
                y, z = (M + dd) // m, (M + M * M // dd) // m
                assert Fr(4, N) == Fr(1, x) + Fr(1, y) + Fr(1, z)
                return (x, y, z)
    return None


ORD = {}
def ordq(q):
    if q not in ORD:
        assert isprime(q), q
        ORD[q] = n_order(4, q)
    return ORD[q]


def val(f, ordf, u):
    return (c0 * pow(4, u, f) + k) % f


def win_pieces_sym(m, j, code, w, h):
    """symbolic pieces (sympy exprs in R = 2^{r/h} etc.) -- returns (list of (name, residue-function)), and checks the
    product identity N = n*x symbolically."""
    from sympy import Symbol, cyclotomic_poly, expand, divisors as sdiv, Poly
    T = Symbol('T')   # T = 4^r
    if code == 0:
        X = Symbol('X'); t = w ** h   # T = X^h
        polys = [Poly(cyclotomic_poly(2 * e, X), X) for e in sdiv(h)]
        homs = [expand(sum(cf * X ** i * w ** (p.degree() - i) for (i,), cf in p.terms())) for p in polys]
        prodY = expand(prod(homs)); assert expand(prodY - (X ** h + t)) == 0
        return t, homs, X
    if code == 1:
        a = Symbol('a'); t = 4 * w ** 4   # T = a^4
        homs = [a * a + 2 * a * w + 2 * w * w, a * a - 2 * a * w + 2 * w * w]
        assert expand(prod(homs) - (a ** 4 + t)) == 0
        return t, homs, a
    b = Symbol('b'); t = w ** 4      # T = 4 b^4
    homs = [2 * b * b + 2 * b * w + w * w, 2 * b * b - 2 * b * w + w * w]
    assert expand(prod(homs) - (4 * b ** 4 + t)) == 0
    return t, homs, b


WINCACHE = {}
def check_window(t, L, u):
    from sympy import lambdify
    m, j, code, w, h = map(int, t[1:6])
    assert code in (0, 1, 2) and w >= 1 and h >= 1 and j >= 1 and (code != 0 or h % 2 == 1)
    key = (m, j, code, w, h)   # (R-O239 repair: j is part of the key; parameters validated for every leaf)
    if key not in WINCACHE:
        tt, homs, var = win_pieces_sym(m, j, code, w, h)
        P = h * n_order(4, m) if code == 0 else 2 * n_order(2, m)
        WINCACHE[key] = (tt, [lambdify(var, e) for e in homs], P)
    tt, fns, P = WINCACHE[key]
    assert m == c0 * 4 ** j * tt - k and m > 1 and m % 2 == 1
    assert L % P == 0, 'window period does not divide L'
    rr = (u - j) % P                     # r mod P
    if code == 0:
        assert rr % h == 0; V = pow(4, rr // h, m)
    elif code == 1:
        assert rr % 2 == 0; V = pow(2, rr // 2, m)
    else:
        assert rr % 2 == 1; V = pow(2, (rr - 1) // 2, m)
    ys = [int(f(V)) % m for f in fns]
    nm = (c0 * pow(4, u, m) + k) % m
    oc = c0
    while oc % 2 == 0: oc //= 2
    E = 2 * j - 2 + ((c0 & -c0).bit_length() - 1)
    pieces = [p for p, v in factorint(oc).items() for _ in range(v)] if oc > 1 else []
    res = [p % m for p in pieces] + [nm] + ys
    # pieces multiply to N/2^E: c0_odd * n * (4^r + t) = c0_odd * n * x / (c0 * 4^{j-1}) * ... checked symbolically above
    # search: -1 = 2^i * prod res_i^{eps_i}, eps in {-1,0,1}, |i| <= E, all used residues invertible
    from itertools import product as iprod
    for eps in iprod((-1, 0, 1), repeat=len(res)):
        v = 1; ok = True
        for r_, e_ in zip(res, eps):
            if e_ == 0: continue
            if gcd(r_, m) != 1: ok = False; break
            v = v * pow(r_, e_, m) % m
        if not ok: continue
        for i in range(-E, E + 1):
            if v * pow(2, i, m) % m == m - 1:
                return [s for s in range(u, j + 2, L) if s >= 0]   # s - j < 1 members: check directly
    raise AssertionError('window does not fire at u=%d' % u)


stats = {'W': 0, 'stuck': 0, 'leaves': 0, 'D': 0, 'P': 0, 'I': 0, 'direct': 0, 'nodes': 0}
small = set()   # exponents s that must be checked directly
ESQ = {}


def walk(e, c):
    stats['nodes'] += 1
    t = next(lines)
    L = prod(l ** v for l, v in e.items())
    # u = CRT of c_l mod l^{e_l}
    u, M = 0, 1
    for l, v in e.items():
        md = l ** v
        u = u + M * (((c[l] - u) * pow(M, -1, md)) % md); M *= md
    if t[0] == 'S':
        l = int(t[1]); assert l >= 2 and isprime(l); v = e.get(l, 0); base = c.get(l, 0)
        for j in range(l):
            e2 = dict(e); c2 = dict(c); e2[l] = v + 1; c2[l] = base + j * l ** v
            walk(e2, c2)
        return
    if t[0] in ('X', 'ABORT'):
        if not ALLOW: raise SystemExit('FAIL: stuck/abort node at u=%d mod L=%d' % (u, L))
        stats['stuck'] += 1; UNC[0] += Fr(1, L)
        return
    stats['leaves'] += 1; stats[t[0]] += 1
    if EXPL: LEAVES.append((u, L, t))
    if t[0] == 'W':
        for s_ in check_window(t, L, u): small.add(s_)
        return
    if t[0] == 'D':
        q = int(t[1]); assert k % q and c0 % q and L % ordq(q) == 0 and val(q, 0, u) == 0
        if q not in ESQ: ESQ[q] = es_explicit(q); assert ESQ[q], q
        if u < 64: small.add(u)   # n_u = q itself would need ES(q) only; checked directly anyway
        return
    a, d = int(t[1]), int(t[2]); qs = [int(x) for x in t[3:]]
    assert a >= 1 and d >= 1
    assert len(set(qs)) == len(qs) and qs
    for q in qs: assert L % ordq(q) == 0
    f = prod(qs); n = (c0 * pow(4, u, f) + k) % f
    if t[0] == 'P':
        assert (f + 1) % (4 * a * d) == 0 and (n + 4 * a * a * d) % f == 0
        cc = (f + 1) // (4 * a * d)
        # positivity: b = c e - a > 0 iff e > a/c; e = (n_s + 4a^2 d)/f >= n_s/f; safe if n_s > a f
        s = u
        if c0 * 4 ** s + k <= a * f: small.add(s)  # only the least member can be small (L >= ...); others checked below
        if L < 400:  # several members may be small
            for s in range(u, 400, L):
                if c0 * 4 ** s + k <= a * f: small.add(s)
    else:
        m = 4 * a * d; w = m
        while w % 2 == 0: w //= 2
        j = (m // w).bit_length() - 1
        assert gcd(f, m) == 1
        ow = n_order(4, w) if w > 1 else 1
        assert L % ow == 0
        # n mod m for s >= j/2: n mod 2^j = k mod 2^j
        nm = (c0 * pow(4, u, w) + k) % w if w > 1 else 0
        two = m // w
        n2 = k % two
        nm_full = next(x for x in range(n2, m, two) if x % w == nm) if w > 1 else n2
        assert (nm_full + f) % m == 0 and (n * n + 4 * a * a * d) % f == 0
        for s in range(u, 2 * (j + 1), L): small.add(s)   # 2-adic condition 2s >= j not guaranteed
    return


check_identities()
sys.setrecursionlimit(100000)
walk({}, {})
assert next(lines, None) is None, 'trailing data'
# direct check of small members
for s in sorted(small):
    N = c0 * 4 ** s + k
    sol = es_explicit(N)
    assert sol, ('no direct ES solution', s)
    stats['direct'] += 1


def explicit(s, t):
    """explicit (x, y, z) for n_s from leaf token t (no residue shortcuts); None if not applicable at this s."""
    n = c0 * 4 ** s + k
    if t[0] == 'D':
        q = int(t[1]); X = ESQ.get(q) or es_explicit(q)
        if n % q: return None
        return tuple(v * (n // q) for v in X)
    if t[0] == 'P':
        a, d = int(t[1]), int(t[2]); f = prod(int(x) for x in t[3:]); cc = (f + 1) // (4 * a * d)
        if (n + 4 * a * a * d) % f: return None
        e_ = (n + 4 * a * a * d) // f; b = cc * e_ - a
        return (a * b * d, a * cc * d * n, b * cc * d * n) if b > 0 else None
    if t[0] == 'I':
        c_, d = int(t[1]), int(t[2]); f = prod(int(x) for x in t[3:])
        if (n + f) % (4 * c_ * d) or (n * n + 4 * c_ * c_ * d + n * f) % (4 * c_ * d * f): return None
        a = (n + f) // (4 * c_ * d); b = (n * n + 4 * c_ * c_ * d + n * f) // (4 * c_ * d * f)
        return (a * b * d * n, a * c_ * d, b * c_ * d)
    m, j, code, w, h = map(int, t[1:6]); r = s - j
    if r < 1: return None
    oc = c0
    while oc % 2 == 0: oc //= 2
    E = 2 * j - 2 + ((c0 & -c0).bit_length() - 1)
    if code == 0: X = 4 ** (r // h); tt = w ** h
    elif code == 1: X = 2 ** (r // 2); tt = 4 * w ** 4
    else: X = 2 ** ((r - 1) // 2); tt = w ** 4
    _, homs, var = win_pieces_sym(m, j, code, w, h)
    ys = [int(e_.subs(var, X)) for e_ in homs]
    x = (n + m) // 4; N = n * x
    assert 4 * x - n == m and x == c0 * 4 ** (j - 1) * (4 ** r + tt) and prod(ys) == 4 ** r + tt
    pieces = [p for p, v in factorint(oc).items() for _ in range(v)] + [n] + ys
    assert 2 ** E * prod(pieces) == N
    from itertools import product as iprod
    for eps in iprod((-1, 0, 1), repeat=len(pieces)):
        d1 = prod(p for p, e_ in zip(pieces, eps) if e_ == 1); d2 = prod(p for p, e_ in zip(pieces, eps) if e_ == -1)
        for i in range(-E, E + 1):
            D1, D2 = (d1 * 2 ** i, d2) if i >= 0 else (d1, d2 * 2 ** (-i))
            if (D1 + D2) % m == 0:
                assert N % D1 == 0 and N % D2 == 0
                return (x, N * (D1 + D2) // (m * D2), N * (D1 + D2) // (m * D1))
    return None


if EXPL:
    for s in range(EXPL + 1):
        lf = [t for (u, L, t) in LEAVES if s % L == u % L]
        assert len(lf) == 1, ('leaf partition', s, len(lf))
        sol = explicit(s, lf[0])
        if sol is None:
            assert s in small, ('leaf class gives no solution outside the recorded exceptions', s)
            continue
        x, y, z = sol; n = c0 * 4 ** s + k
        assert min(x, y, z) > 0 and 4 * x * y * z == n * (x * y + y * z + z * x), s
        stats['explicit'] = stats.get('explicit', 0) + 1
print('OK' if not stats['stuck'] else 'PARTIAL (uncovered Haar measure exactly %s ~ %.3e)' % (UNC[0], float(UNC[0])), stats, 'small s checked directly:', sorted(small))
