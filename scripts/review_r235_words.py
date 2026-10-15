# review_r235_words.py -- R235 from-scratch checks of SIGN_FIELDS §2 (Prop 2.1, Thm 2.2, 8/131, 8/241).
# Words of n: (t,u,v) >= 1 with t u v - u - v = n; A = tu-1, A* = tv-1. nu-word: nu | one of t,u,v,A,A*.
import sys
from fractions import Fraction as F
from math import gcd, isqrt
from sympy import jacobi_symbol, isprime


def words(n):
    out = []
    for u in range(1, n + 2):
        for t in range(1, (n + 1) // u + 3):
            A = t * u - 1
            if A <= 0:
                continue
            if A > n + u:
                break
            if (n + u) % A == 0:
                v = (n + u) // A
                assert t * u * v - u - v == n
                out.append((t, u, v))
    return out


def slots(w):
    t, u, v = w
    return {'t': t, 'u': u, 'v': v, 'A': t * u - 1, 'As': t * v - 1}


def decomp_ok(nu, n, w):
    t, u, v = w
    A, As = t * u - 1, t * v - 1
    res = []
    if u % nu == 0:
        x = u // nu
        res.append(F(1, x * As) + F(1, t * n * x) + F(1, t * n * x * As))
    if v % nu == 0:
        x = v // nu
        res.append(F(1, x * A) + F(1, t * n * x) + F(1, t * n * x * A))
    if A % nu == 0:
        x = A // nu
        res.append(F(1, x * v) + F(1, x * v * As) + F(1, n * x * As))
    if As % nu == 0:
        x = As // nu
        res.append(F(1, x * u) + F(1, x * u * A) + F(1, n * x * A))
    return all(r == F(nu, n) for r in res)


def unit_frac3(num, n):
    # does num/n = 1/x+1/y+1/z have a solution? x <= y <= z
    for x in range(n // num + 1, 3 * n // num + 1):
        a, d = num * x - n, n * x
        if a <= 0:
            continue
        for y in range(max(x, d // a + 1), 2 * d // a + 1):
            p, q = a * y - d, d * y
            if p > 0 and q % p == 0:
                return x, y, q // p
    return None


if __name__ == '__main__':
    P = int(sys.argv[1])
    NUS = [3, 4, 5, 7, 8, 12]
    ns = [p for p in range(3, P) if isprime(p)] + [m * m for m in range(3, 60, 2)]
    fails = 0
    sqwords = {nu: 0 for nu in NUS}
    for n in ns:
        W = words(n)
        sq = isqrt(n) ** 2 == n
        for w in W:
            S = slots(w)
            t, u, v = w
            A = S['A']
            for nu in NUS:
                isw = any(x % nu == 0 for x in S.values())
                if isw:
                    assert decomp_ok(nu, n, w)
                    if sq:
                        sqwords[nu] += 1
                # Prop 2.1 under its hypotheses
                if gcd(nu, u) == 1 and gcd(nu, n) == 1 and (n + u) % nu != 0 and gcd(A, nu) == 1:
                    assert (A + 1) % u == 0
                    cls = {(-1) % nu, (-(n + u) * pow(n, -1, nu)) % nu}
                    pred = (A % nu) in cls
                    if pred != isw:
                        fails += 1
    print('Prop 2.1 mismatches:', fails, ' nu-words at odd squares 9..59^2:', sqwords)

    # u = 3 mod 4 with nu = 4, n = 1 mod 4 non-square: every odd-A word is a 4-word via v, and chi = (A/n) = -1
    bad = 0
    tot = 0
    for n in [p for p in range(5, P) if isprime(p) and p % 4 == 1]:
        for (t, u, v) in words(n):
            A = t * u - 1
            if u % 4 == 3 and A % 2 == 1:
                tot += 1
                if not (v % 4 == 0 and jacobi_symbol(A, n) == -1):
                    bad += 1
    print('u=3 mod 4, odd A words at primes 1 mod 4:', tot, 'not (4|v and chi=-1):', bad)

    for n in [131, 241]:
        W = words(n)
        Wun = {(t, min(u, v), max(u, v)) for (t, u, v) in W}
        four = [w for w in W if any(x % 4 == 0 for x in slots(w).values())]
        eight = [w for w in W if any(x % 8 == 0 for x in slots(w).values())]
        mod8 = sorted({x % 8 for w in four for x in slots(w).values() if x % 4 == 0})
        print(n, 'ordered words', len(W), 'unordered', len(Wun), '4-slot words', len(four),
              '4-slot values mod 8', mod8, '8-words', len(eight), 'chi of 4-words',
              sorted({jacobi_symbol(w[0] * w[1] - 1, n) for w in four if (w[0] * w[1]) % 2 == 0}),
              ' 8/n three unit fractions:', unit_frac3(8, n))
