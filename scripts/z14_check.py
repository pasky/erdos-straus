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
# Usage: PYTHONPATH=scripts uv run python scripts/z14_check.py k cert.txt[.gz] [--allow-stuck]
import sys, gzip
from fractions import Fraction as Fr
from math import gcd, prod
from sympy import isprime, n_order, factorint, symbols, simplify, divisors

k = int(sys.argv[1]); path = sys.argv[2]
ALLOW = '--allow-stuck' in sys.argv  # report exact uncovered measure instead of failing
UNC = [Fr(0)]
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
    return (pow(4, u, f) + k) % f


stats = {'stuck': 0, 'leaves': 0, 'D': 0, 'P': 0, 'I': 0, 'direct': 0, 'nodes': 0}
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
        l = int(t[1]); v = e.get(l, 0); base = c.get(l, 0)
        for j in range(l):
            e2 = dict(e); c2 = dict(c); e2[l] = v + 1; c2[l] = base + j * l ** v
            walk(e2, c2)
        return
    if t[0] in ('X', 'ABORT'):
        if not ALLOW: raise SystemExit('FAIL: stuck/abort node at u=%d mod L=%d' % (u, L))
        stats['stuck'] += 1; UNC[0] += Fr(1, L)
        return
    stats['leaves'] += 1; stats[t[0]] += 1
    if t[0] == 'D':
        q = int(t[1]); assert k % q and L % ordq(q) == 0 and val(q, 0, u) == 0
        if q not in ESQ: ESQ[q] = es_explicit(q); assert ESQ[q], q
        if u < 64: small.add(u)   # n_u = q itself would need ES(q) only; checked directly anyway
        return
    a, d = int(t[1]), int(t[2]); qs = [int(x) for x in t[3:]]
    assert len(set(qs)) == len(qs) and qs
    for q in qs: assert L % ordq(q) == 0
    f = prod(qs); n = (pow(4, u, f) + k) % f
    if t[0] == 'P':
        assert (f + 1) % (4 * a * d) == 0 and (n + 4 * a * a * d) % f == 0
        cc = (f + 1) // (4 * a * d)
        # positivity: b = c e - a > 0 iff e > a/c; e = (n_s + 4a^2 d)/f >= n_s/f; safe if n_s > a f
        s = u
        if 4 ** s + k <= a * f: small.add(s)  # only the least member can be small (L >= ...); others checked below
        if L < 400:  # several members may be small
            for s in range(u, 400, L):
                if 4 ** s + k <= a * f: small.add(s)
    else:
        m = 4 * a * d; w = m
        while w % 2 == 0: w //= 2
        j = (m // w).bit_length() - 1
        assert gcd(f, m) == 1
        ow = n_order(4, w) if w > 1 else 1
        assert L % ow == 0
        # n mod m for s >= j/2: n mod 2^j = k mod 2^j
        nm = (pow(4, u, w) + k) % w if w > 1 else 0
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
    N = 4 ** s + k
    sol = es_explicit(N)
    assert sol, ('no direct ES solution', s)
    stats['direct'] += 1
print('OK' if not stats['stuck'] else 'PARTIAL (uncovered Haar measure exactly %s ~ %.3e)' % (UNC[0], float(UNC[0])), stats, 'small s checked directly:', sorted(small))
