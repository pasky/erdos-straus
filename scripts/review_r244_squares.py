"""R244: from-scratch checks for EXP_NEAR_SQUARE Lemma 1.2 / Lemma 3.1 / square-point counts.

square_points(c0, k): COMPLETE list of x in Z with c0*4^x + k a rational square, by factoring (no search window):
  x >= 0: c0*4^x + k = y^2  -- finite per x, but x unbounded; for c0 a square (c0 = w^2) it is (y - w 2^x)(y + w 2^x) = k,
          finitely many; for general c0 we fall back to a window (flagged).
  x = -a < 0: c0 + k*4^a = (2^a y)^2 =: Y^2 ; Y^2 - k*4^a = c0.  (window fallback for general c0.)
"""
import sys, random
from fractions import Fraction
from math import isqrt, gcd
import sympy as sp


def is_sq(n):
    return n >= 0 and isqrt(n) ** 2 == n


def square_points_c1(k):
    """exact complete list for c0 = 1 (k odd > 0)."""
    pts = set()
    divs = sp.divisors(k)
    for d in divs:
        e = k // d
        if e > d and (e - d) % 2 == 0:
            h = (e - d) // 2  # = 2^x
            if h & (h - 1) == 0:
                pts.add(h.bit_length() - 1)
    # x = -a: 1 + k*4^a = y^2, y odd; ((y-1)/2)((y+1)/2) = k*4^(a-1)  (a >= 1); consecutive coprime -> {d*4^(a-1), k/d}
    for d in divs:
        e = k // d
        for a in range(1, 80):
            u = d * 4 ** (a - 1)
            if abs(u - e) == 1:
                pts.add(-a)
    return sorted(pts)


def square_points_window(c0, k, lo=-40, hi=200):
    out = []
    for x in range(lo, hi):
        v = Fraction(c0) * Fraction(4) ** x + k
        if is_sq(v.numerator) and is_sq(v.denominator):
            out.append(x)
    return out


def ordm(g, m):
    return int(sp.n_order(g, m))


def lemma12_random(k, P, trials=20000, qmax=20000, seed=1):
    """random label points sigma in prod_l P (labels on primes l <= 200 dividing some ord_q(4)); check:
    q pure (q odd prime, q not | 2k*prod num(s_x)) => nu(sigma)_q is a nonzero square mod q, and = s_x^2 mod q.
    Also: q | k => nu(sigma)_q is a nonzero square mod q for every sigma (any labels)."""
    rnd = random.Random(seed)
    primes = list(sp.primerange(3, qmax))
    sx = {x: Fraction(isqrt((Fraction(4) ** x + k).numerator), isqrt((Fraction(4) ** x + k).denominator)) for x in P}
    bad = [q for q in primes for x in P if (sx[x].numerator % q == 0)]
    npure = nmix = 0
    for _ in range(trials):
        q = rnd.choice(primes)
        L = ordm(4, q)
        supp = list(sp.factorint(L).keys())
        lab = {l: rnd.choice(P) for l in supp}
        if rnd.random() < 0.5:  # bias towards pure
            x0 = rnd.choice(P)
            lab = {l: x0 for l in supp}
        mods = [l ** sp.multiplicity(l, L) for l in supp]
        mu = int(sp.ntheory.modular.crt(mods, [lab[l] % m for l, m in zip(supp, mods)])[0]) if supp else 0
        nu = (pow(4, mu, q) + k) % q
        labs = set(lab.values())
        if k % q == 0:
            assert nu != 0 and sp.legendre_symbol(nu, q) == 1
            continue
        if len(labs) <= 1 and q not in bad:
            x = labs.pop() if labs else P[0]
            s = sx[x]
            assert nu == (s.numerator * pow(s.denominator, -1, q)) ** 2 % q, (q, x)
            assert nu != 0 and sp.legendre_symbol(nu, q) == 1
            npure += 1
        else:
            nmix += 1
    return npure, nmix


def main():
    for k in (105, 33, 273, 297):
        exact = square_points_c1(k)
        win = square_points_window(1, k)
        print(f'k={k}: square points (complete, by factoring) {exact}; window [-40,200) {win}')
        assert exact == win
    print('4^4+273 =', 4 ** 4 + 273, '= 23^2:', 4 ** 4 + 273 == 23 ** 2)
    # ord supports of the divisor classes of 105's square points
    for q, x in ((19, 4), (41, -2), (11, 2), (13, 3)):
        L = ordm(4, q)
        sols = [m for m in range(L) if (pow(4, m, q) + 105) % q == 0]
        print(f'D{q}: ord_q(4)={L}={sp.factorint(L)}, mu mod {L} in {sols}; x={x} mod L = {x % L}')
    print('Lemma 1.2 random test (pure, mixed):', lemma12_random(105, [2, 3, 4, -2]))
    print('Lemma 1.2 random test k=297 (pure, mixed):', lemma12_random(297, [3]))


if __name__ == '__main__':
    main()
