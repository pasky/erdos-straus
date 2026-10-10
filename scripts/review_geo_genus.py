"""R126 from-scratch: enumerate ALL solutions of 4/p = 1/u1+1/u2+1/u3 (p prime < PMAX) via the divisor
identity (A u2 - B)(A u3 - B) = B^2, classify Type I/II, and check
 * BL Cor 1.3 ((-u_i/u_j)/p) = -1 for the unit pair,
 * Prop 5.1: Type I => (-d/p) = -1 (d = gcd(x/p, y, z)),
 * Prop 5.2: Type II => (-d/f) = -1, (f/p) = -(-1/p), f = 4acd-1,
 * BL Thm 1.2 / Lemmas 3.5, 3.8 (product of Hilbert symbols at all places),
 * GEOMETRY_ES §3.1 restrictions alpha|F1 = (n(n-4t), -u2/u3), alpha|F2 = (-lam, -nZ) at every place,
 * Type II completeness bound a <= sqrt(p)/2 + 1 (a <= b normalisation), Type I bound a <= 3p/(4d).
No code from scripts/geo_*.py."""
import sys
from fractions import Fraction as Fr
from math import gcd, isqrt
from sympy import factorint, primerange, divisors

def sqfree_core(r):  # r nonzero Fraction -> squarefree integer in same square class
    m = r.numerator * r.denominator
    s = -1 if m < 0 else 1
    out = s
    for q, e in factorint(abs(m)).items():
        if e % 2: out *= q
    return out

def vp(m, p):
    k = 0
    while m % p == 0: m //= p; k += 1
    return k, m

def legendre(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def hilbert(a, b, p):  # a, b nonzero squarefree-ish ints, p prime or 0 (=inf)
    if p == 0:
        return -1 if (a < 0 and b < 0) else 1
    al, u = vp(a, p); be, v = vp(b, p)
    if p != 2:
        r = (-1) ** (al * be * ((p - 1) // 2) % 2)
        return r * legendre(u, p) ** be * legendre(v, p) ** al
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    e = (eps(u) * eps(v) + al * om(v) + be * om(u)) % 2
    return -1 if e else 1

def hs(r1, r2, p):
    return hilbert(sqfree_core(r1), sqfree_core(r2), p)

def places(*rs):
    ps = {0, 2}
    for r in rs:
        for m in (r.numerator, r.denominator):
            ps |= set(factorint(abs(m)).keys())
    return sorted(ps)

def jacobi(a, n):  # n odd positive
    a %= n; res = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: res = -res
        a %= n
    return res if n == 1 else 0

def solutions(p):
    out = []
    for u1 in range(p // 4 + 1, 3 * p // 4 + 1):
        A, B = 4 * u1 - p, p * u1
        g = gcd(A, B); A //= g; B //= g
        # 1/u2+1/u3 = A/B, u1<=u2<=u3: (A u2 - B)(A u3 - B) = B^2, X = A u2 - B <= B
        for X in divisors(B * B):
            if X > B: break
            if (X + B) % A: continue
            Y = B * B // X
            if (Y + B) % A: continue
            u2, u3 = (X + B) // A, (Y + B) // A
            if u2 >= u1: out.append((u1, u2, u3))
    return out

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
stats = dict(sol=0, I=0, II=0, bad=0)
maxratioII = 0; maxratioI = 0
for p in primerange(3, PMAX):
    sols = solutions(p)
    if not sols: print('NO SOLUTION', p); stats['bad'] += 1
    for u in sols:
        stats['sol'] += 1
        ru = [Fr(x) for x in u]
        # BL Thm 1.2 + local lemmas: invariants at all places
        a1, a2 = -ru[0] / ru[2], -ru[1] / ru[2]
        inv = {v: hs(a1, a2, v) for v in places(a1, a2)}
        assert inv[0] == -1 and inv[p] == -1 and all(inv[v] == 1 for v in inv if v not in (0, p)), (p, u, inv)
        # Cor 1.3
        V = [vp(x, p) for x in u]
        pairs = [(i, j) for i in range(3) for j in range(3) if i != j and V[i][0] == V[j][0]]
        assert pairs and all(legendre(-V[i][1] * pow(V[j][1], -1, p), p) == -1 for i, j in pairs)
        # F1 restriction (u1 = t fibre, any ordering of coordinates), at all places
        for (i, j, k) in [(0, 1, 2), (1, 0, 2), (2, 0, 1)]:
            t = ru[i]; w = ru[j] / ru[k]
            if 4 * t == p: continue
            b1 = Fr(p) * (p - 4 * t)
            for v in places(b1, -w, a1, a2):
                assert hs(b1, -w, v) == hs(a1, a2, v), ('F1', p, u, v)
        # F2: u_i = lam u_j, Z = 4 lam u_j - n(lam+1)
        for (i, j, k) in [(0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1)]:
            lam = ru[i] / ru[j]; Z = 4 * lam * ru[j] - p * (lam + 1)
            if Z == 0 or lam == -1: continue
            for v in places(lam, Z, a1, a2):
                assert hs(-lam, -p * Z, v) == hs(a1, a2, v), ('F2', p, u, v)
        # classification
        div = [x % p == 0 for x in u]
        if sum(div) == 1:
            stats['I'] += 1
            x = u[div.index(True)]; y, z = [u[m] for m in range(3) if not div[m]]
            if y > z: y, z = z, y
            d = gcd(gcd(x // p, y), z)
            xp, yp, zp = x // p // d, y // d, z // d
            a2_ = xp * yp // zp; a = isqrt(a2_); assert a * a == a2_
            b = xp // a; c = yp // a
            assert legendre(-d, p) == -1, ('5.1', p, u, d)
            assert legendre(-a * b, p) == -1
            f = 4 * a * c * d - p; assert f > 0 and (4 * a * a * d + 1) % f == 0
            assert a <= b and a * 4 * d <= 3 * p; maxratioI = max(maxratioI, 4 * a * d / (3 * p))
        elif sum(div) == 2:
            stats['II'] += 1
            x = u[div.index(False)]; y, z = [u[m] for m in range(3) if div[m]]
            if y > z: y, z = z, y
            d = gcd(gcd(x, y // p), z // p)
            xp, yp, zp = x // d, y // p // d, z // p // d
            a2_ = xp * yp // zp; a = isqrt(a2_); assert a * a == a2_
            b = xp // a; c = yp // a
            f = 4 * a * c * d - 1; e = (p + 4 * a * a * d) // f
            assert e * f == p + 4 * a * a * d and a <= b
            assert jacobi(-d, f) == -1 and jacobi(p, f) == -1
            assert legendre(f, p) == -legendre(-1, p)
            assert a <= isqrt(p) / 2 + 1, ('IIbound', p, u)
            maxratioII = max(maxratioII, a / (p ** 0.5 / 2))
        else:
            raise AssertionError(('type?', p, u))
print(stats, 'max a/(sqrt p/2) TypeII:', round(maxratioII, 4), 'max 4ad/3p TypeI:', round(maxratioI, 4))
