"""Z0345 (pass 2, SK0): ES with denominators in a common imaginary quadratic order, first test case Z[i].
(a) general search: x,y in Z[i] with |Re|,|Im| <= BOX, z = 1/(4/p-1/x-1/y) must lie in Z[i]  (exact integers).
(b) conjugate-pair ansatz x=a+bi, y=a-bi (1/x+1/y=2a/(a^2+b^2) in Q), z in Z:  4/p - 1/z = 2a/(a^2+b^2)  (search z<=ZMAX, a<=AMAX).
Verify every hit exactly with Fractions. Primes p <= PMAX."""
import sys
from fractions import Fraction as F
from sympy import primerange
from math import isqrt
PMAX, BOX, ZMAX, AMAX = map(int, sys.argv[1:5])

def inv_gauss(u, v):
    """1/(u+vi) in Z[i]? returns (re,im) integers or None (u,v Fractions/ints)."""
    N = u * u + v * v
    if N == 0: return None
    re, im = F(u, 1) / N, -F(v, 1) / N
    if re.denominator == 1 and im.denominator == 1: return (int(re), int(im))
    return None

def gauss_sum_recip(p, x, y):
    # s = 4/p - 1/x - 1/y in Q(i); return s
    def inv(c):
        a, b = c; N = a * a + b * b
        return (F(a, N), F(-b, N))
    ix, iy = inv(x), inv(y)
    return (F(4, p) - ix[0] - iy[0], -ix[1] - iy[1])

res_a = {}; res_b = {}
gauss_pts = [(a, b) for a in range(-BOX, BOX + 1) for b in range(-BOX, BOX + 1) if (a, b) != (0, 0)]
for p in primerange(3, PMAX + 1):
    # (a) general search (x<=y by index, z any)
    hits = []
    for i, x in enumerate(gauss_pts):
        for y in gauss_pts[i:]:
            s = gauss_sum_recip(p, x, y)
            if s == (0, 0): continue
            z = inv_gauss(s[0], s[1])   # 1/s in Z[i]?  s = s[0] + s[1] i
            if z is None: continue
            # exact check
            def inv(c):
                a, b = c; N = a * a + b * b; return (F(a, N), F(-b, N))
            t = [inv(x), inv(y), inv(z)]
            tot = (sum(q[0] for q in t), sum(q[1] for q in t))
            assert tot == (F(4, p), 0)
            hits.append((x, y, z))
            break
        if len(hits) >= 1: break
    res_a[p] = hits[:1]
    # (b) conjugate pair with integer z
    found = None
    for z in range(1, ZMAX + 1):
        r = F(4, p) - F(1, z)
        if r == 0: continue
        # need 2a/(a^2+b^2) = r  -> for r>0 a>0; r<0 a<0
        sgn = 1 if r > 0 else -1
        for a in range(1, AMAX + 1):
            aa = sgn * a
            N = F(2 * aa) / r        # must equal a^2+b^2
            if N.denominator != 1: continue
            Nn = int(N); b2 = Nn - aa * aa
            if b2 < 0: continue
            b = isqrt(b2)
            if b * b == b2 and b > 0:
                x = (aa, b); y = (aa, -b)
                assert F(1, aa * aa + b * b) * 2 * aa == 2 * F(aa) / (aa * aa + b * b)
                assert F(1, 1) * 0 == 0
                found = (x, y, z); break
        if found: break
    res_b[p] = found
ps = list(res_a)
print("primes", len(ps))
print("(a) general Z[i] triples found for:", sum(1 for p in ps if res_a[p]), "primes; examples:", [(p, res_a[p]) for p in ps[:4]])
print("(b) conjugate-pair ansatz found for:", sum(1 for p in ps if res_b[p]), "primes")
print("(b) primes NOT found:", [p for p in ps if not res_b[p]][:30])
print("(b) examples:", [(p, res_b[p]) for p in ps[:6]])
