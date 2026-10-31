#!/usr/bin/env python3
"""U07 batch-2 checks (capped). Z0169: which a/b in (1,3] (b<=20) are sums of 3 unit fractions (count reps per b).
Z1016: Gauss-reduce L_p={(x,y): y = i x mod p} (i^2=-1) for primes p=1 mod 4 <= 2000; count reduced-basis changes between
consecutive primes. Z1153: integer Y->Delta resistances for star inputs 1..20 (integer outputs). Z1169: min(x+y+z) - 9p/4
over solutions (AM-HM gap) for primes <=400 (uses solution enumeration). Z1171: Hessian of z(x,y) = p x y/(4xy - p(x+y))."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (2_000_000_000, 2_000_000_000))
import math
from fractions import Fraction as F
from sympy import primerange, sqrt_mod, symbols, hessian, simplify, Matrix
# Z0169
cnt = {}
for b in range(1, 21):
    for a in range(1, 3 * b + 1):
        r = F(a, b)
        if not (1 < r <= 3): continue
        reps = 0
        for x in range(1, int(3 / (r - 1 + F(1, 10**9))) + 2 if r > 1 else 1):
            if F(1, x) < r / 3: continue
            rem1 = r - F(1, x)
            if rem1 <= 0: continue
            for y in range(x, int(2 / rem1) + 2):
                rem = rem1 - F(1, y)
                if rem > 0 and rem.numerator == 1 and rem.denominator >= y: reps += 1
        cnt.setdefault(b, []).append((a, reps))
print("Z0169 reps per b (a/b in (1,3], 3 unit fractions, x<=y<=z):", {b: sum(r for _, r in v) for b, v in list(cnt.items())[:8]})
# Z1016
def gauss(u, v):
    # reduce basis u,v of 2D lattice with standard inner product
    while True:
        if u[0]**2+u[1]**2 > v[0]**2+v[1]**2: u, v = v, u
        m = round((u[0]*v[0]+u[1]*v[1]) / (u[0]**2+u[1]**2))
        if m == 0: return tuple(sorted([u, v], key=lambda w: w[0]**2+w[1]**2))
        v = (v[0]-m*u[0], v[1]-m*u[1])
prev = None; changes = 0; n = 0
for p in primerange(5, 2001):
    if p % 4 != 1: continue
    i = sqrt_mod(-1, p)
    # lattice {(x,y): y ≡ i x mod p}: basis (1,i), (0,p)
    red = gauss((1, i), (0, p)); n += 1
    shape = (red[0][0]**2+red[0][1]**2, red[1][0]**2+red[1][1]**2)
    if prev is not None and shape != prev: changes += 1
    prev = shape
print("Z1016 primes p=1 mod 4 <= 2000:", n, " consecutive reduced-shape changes:", changes)
# Z1153
def ydelta(a, b, c):
    s = a*b + b*c + c*a
    return (F(s, c), F(s, a), F(s, b))
ints = [(a, b, c) for a in range(1, 21) for b in range(1, 21) for c in range(1, 21) if all((x.denominator == 1) for x in ydelta(a, b, c))]
print("Z1153 star inputs in [1,20]^3 with integer triangle outputs:", len(ints), "of", 20**3)
# Z1169 (AM-HM gap)
import math as _m
from sympy import divisors as _div, symbols as _sym, hessian as _hess, simplify as _simp
def sols(p):
    res = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        num, den = 4 * x - p, p * x
        if num <= 0: continue
        g = _m.gcd(num, den); a, b = num // g, den // g
        for d in _div(b * b):
            if (b + d) % a: continue
            y = (b + d) // a
            if y < x: continue
            e = b * b // d
            if (b + e) % a: continue
            z = (b + e) // a
            if z >= y: res.append((x, y, z))
    return res
gaps = []
for p in primerange(5, 401):
    S = sols(p)
    if S: gaps.append(min(x + y + z for x, y, z in S) - F(9 * p, 4))
print("Z1169 min over p<=400 of (min x+y+z) - 9p/4:", min(gaps), " max:", max(gaps), " primes:", len(gaps))
X, Y = _sym('x y'), None
x, y, p_ = _sym('x'), _sym('y'), _sym('p', positive=True)
z = p_*x*y/(4*x*y - p_*(x+y))
H = _hess(z, (x, y))
print("Z1171 Hessian of z(x,y) (simplified):", [[_simp(H[i, j]) for j in range(2)] for i in range(2)])
