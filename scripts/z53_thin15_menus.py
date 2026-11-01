# z53_thin15_menus.py — exact, D-independent limit test for the five binomial menus at mu = 0 of n = c0*Y^D + 1
# (Z53_THIN15.md §3–4).  All menus share  n + a = f f'  (a > 0 rational constant), X = f(1), X' = f'(1),
# phi = f(0), phi' = f'(0), X X' = F + a (F = c0 + 1 = 4^J), phi phi' = 1 + a, and
#   A  (II-ad): x = (n+f)/4,          y = n(1+f')/4,      z = n x (1+f')/a
#   A' (I-ac) : x = (n+f)/4,          y = x f',           z = n x f'/a
#   B  (II-ac): x = f'(f+1)/4,        y = n(f+1)/4,       z = n f'(f+1)/(4a)
#   B' (II-cd): x = (f+1)(f'+a)/4,    y = n(f'+a)/(4a),   z = n(f+1)/4
# Validity near mu = 0 <=> the three coordinates are in Z[1/2] at Y = 1 (n = F) and in Z_(2) at Y = 0 (n = 1).
# Capelli: (1+a)/c0 = K with K = u^p (p odd prime | D) or K = 4 w^4 (4 | D).
# Complete enumeration for a given K (memo Lemma 5): in every menu phi is a 2-adic unit and X in Z[1/2] with odd part
# X_o | odd numerator of F + a; and rho := P(0)/P(1) = l/g1 with l | A, g1 | A + B (K = A/B lowest terms; Z52D Lemma 6),
# v2(X) = -v2(rho), phi = X rho.  So the test runs over divisors only and is valid for EVERY root degree D.
from fractions import Fraction as Fr
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)

def odd(n):
    while n % 2 == 0: n //= 2
    return n
def v2(x):
    x = Fr(x); n, d, v = abs(x.numerator), x.denominator, 0
    if n == 0: return 10 ** 9
    while n % 2 == 0: n //= 2; v += 1
    while d % 2 == 0: d //= 2; v -= 1
    return v
def in_half(x):       # x in Z[1/2]
    d = Fr(x).denominator; return odd(d) == 1
def in_loc2(x):       # x in Z_(2)
    return Fr(x).denominator % 2 == 1
def divs(n):
    return [int(t) for t in pari.divisors(n)]

def coords(menu, nval, X, Xp, a):
    if menu == 'A':
        x = (nval + X) / 4; return (x, nval * (1 + Xp) / 4, nval * x * (1 + Xp) / a)
    if menu == "A'":
        x = (nval + X) / 4; return (x, x * Xp, nval * x * Xp / a)
    if menu == 'B':
        return (Xp * (X + 1) / 4, nval * (X + 1) / 4, nval * Xp * (X + 1) / (4 * a))
    if menu == "B'":
        return ((X + 1) * (Xp + a) / 4, nval * (Xp + a) / (4 * a), nval * (X + 1) / 4)
    raise ValueError(menu)
MENUS = ('A', "A'", 'B', "B'")

def rho_set(K):
    K = Fr(K); A, B = K.numerator, K.denominator
    return sorted({Fr(l, g1) for l in divs(A) for g1 in divs(A + B)})

def test(c0, a, K, menus=MENUS, Xodd_divs=None):
    """all (menu, X, X', phi, phi') passing the exact limit conditions at Y = 1 and Y = 0, any D."""
    a = Fr(a); K = Fr(K); F = c0 + 1
    assert a > 0 and (1 + a) == c0 * K
    N = F + a
    Xo_list = Xodd_divs if Xodd_divs is not None else divs(odd(N.numerator))
    rhos = rho_set(K)
    byw = {}
    for rho in rhos: byw.setdefault(-v2(rho), []).append(rho)
    out = []
    for w, rl in byw.items():
        for Xo in Xo_list:
            X = Fr(Xo) * Fr(2) ** w
            Xp = N / X
            ms = [m for m in menus if all(in_half(t) for t in coords(m, Fr(F), X, Xp, a))]
            if not ms: continue
            for rho in rl:
                phi = X * rho; phip = (1 + a) / phi      # v2(phi) = 0 by the choice of w
                for m in ms:
                    if all(in_loc2(t) for t in coords(m, Fr(1), phi, phip, a)):
                        out.append((m, X, Xp, phi, phip))
    return out

if __name__ == '__main__':
    # positive controls: c0 = 3 (II-ac cubic family of EXP_OPEN Prop 2.1: a = 80, u = 3, p = 3) and c0 = 63
    # (II-ad family of EXP_OPEN Thm 2.3: a = 4 a^2 d = 1700, u = 3, p = 3)
    for c0, u, p in ((3, 3, 3), (63, 3, 3)):
        a = c0 * u ** p - 1
        hits = test(c0, a, Fr(u) ** p)
        print('control c0=%d u=%d p=%d a=%d:' % (c0, u, p, a), sorted({h[0] for h in hits}), len(hits), 'hits')
        for h in hits: print('   ', h[0], 'X=%s Xp=%s phi=%s phip=%s' % tuple(map(str, h[1:])))
