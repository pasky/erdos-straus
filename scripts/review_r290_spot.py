"""R290 from-scratch spot checks of FRONTIER.md numerical/identity claims (independent code).
(a) Theorem K (METAPLECTIC_ES): R_t(n) = D_t^-(tn+1) - beta_t(n), and the q-series identity
    q^{t-2} (Q;Q)^2 theta(X^2)/theta(X)^2 = sum_n (D^- - D^+)(tn+1) q^n,  X = q^{t-1}, Q = q^t.
(b) E_8 ∩ primes < 2000 = {2,3,11,17,131,241}  (8/p has no 3-term unit-fraction representation).
(c) p = 3361: list all Type II solutions of 4/p (p divides exactly two denominators).
"""
from fractions import Fraction
import math, sys


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


def three_term(m, n):
    """all (x<=y<=z) with m/n = 1/x+1/y+1/z"""
    sols = []
    r0 = Fraction(m, n)
    x = max(1, math.ceil(1 / r0))
    while Fraction(1, x) * 3 >= r0:
        r = r0 - Fraction(1, x)
        if r > 0:
            a, b = r.numerator, r.denominator
            # 1/y + 1/z = a/b, y<=z, y>=x  <=>  (ay-b)(az-b) = b^2 with 0 < ay-b <= b
            fb = factor(b); f2 = {p: 2 * e for p, e in fb.items()}
            for d in divisors_from(f2):
                if d <= b and (b + d) % a == 0 and (b + b * b // d) % a == 0:
                    y = (b + d) // a; z = (b + b * b // d) // a
                    if y >= x:
                        sols.append((x, y, z))
        x += 1
    return sols


def check_K(tmax=9, nmax=150):
    bad = 0
    for t in range(3, tmax + 1):
        # brute R_t
        for n in range(0, nmax):
            R = sum(1 for u in range(2, n + 3) for v in range(2, n + 3) if t * u * v - u - v == n)
            N = t * n + 1
            Dm = sum(1 for d in divisors_from(factor(N)) if d % t == t - 1)
            beta = 2 * ((n + 1) % (t - 1) == 0) - (n == t - 2)
            if R != Dm - beta:
                bad += 1; print("K2 fail", t, n, R, Dm, beta)
        # q-series to order P
        P = nmax
        def mul(a, b):
            c = [0] * P
            for i, ai in enumerate(a):
                if ai:
                    for j in range(P - i):
                        c[i + j] += ai * b[j]
            return c
        def inv(a):
            # a[0] = 1 assumed
            b = [0] * P; b[0] = Fraction(1, a[0])
            for k in range(1, P):
                b[k] = -sum(a[j] * b[k - j] for j in range(1, k + 1)) / a[0]
            return b
        def poch(shift, step):  # prod_{k>=0} (1 - q^{shift + k*step}), shift>=1
            s = [0] * P; s[0] = 1
            e = shift
            while e < P:
                f = [0] * P; f[0] = 1; f[e] = -1
                s = mul(s, f); e += step
            return s
        Q = t
        # theta(q^a) = (q^a;Q)(Q q^{-a};Q) ; for 0<a<Q both shifts positive
        def theta(a):
            return mul(poch(a, Q), poch(Q - a, Q))
        # X = q^{t-1}, X^2 = q^{2t-2} = Q * q^{t-2}: theta(Q x) = -x^{-1} theta(x) -> theta(q^{2t-2}) = -q^{-(t-2)} theta(q^{t-2})
        # so q^{t-2} theta(X^2) = -theta(q^{t-2}) (for t>=3; t-2 >= 1)
        num = [-c for c in theta(t - 2)]
        lhs = mul(mul(poch(Q, Q), poch(Q, Q)), mul(num, inv(mul(theta(t - 1), theta(t - 1)))))
        for n in range(P):
            N = t * n + 1
            ds = divisors_from(factor(N))
            rhs = sum(1 for d in ds if d % t == t - 1) - sum(1 for d in ds if d % t == 1)
            if lhs[n] != rhs:
                bad += 1; print("K1 fail", t, n, lhs[n], rhs); break
    print("Theorem K checks: t=3..%d, n<%d, failures: %d" % (tmax, nmax, bad))


def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** .5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


if __name__ == "__main__":
    check_K()
    E8 = [p for p in primes_upto(2000) if not three_term(8, p)]
    print("E_8 ∩ primes < 2000 =", E8)
    p = 3361
    sols = three_term(4, p)
    t2 = [s for s in sols if sum(1 for w in s if w % p == 0) == 2]
    t1 = [s for s in sols if sum(1 for w in s if w % p == 0) == 1]
    print("p=3361: #solutions", len(sols), "Type I", len(t1), "Type II", len(t2), t2)
