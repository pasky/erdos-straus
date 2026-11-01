#!/usr/bin/env python3
"""Z53_NONCRTLOGIC -- falsifier / check of the trap-family character lemma (Theorem T, Lemma T4).

Claim (Theorem T, character part): let P in Z[X] be primitive irreducible with P(0) = 1 and no positive real
root; R(X) = X^n P(1/X) (monic), beta a root of R.  If q = 0 mod 8 and q = 0 mod l for every odd prime l
dividing lc(P) * Res(R, h^v) (h^v = reversed h), and p = P(q) is prime with p not dividing h(q), then the
Legendre symbol (h(q)/p) = +1.

The script takes q = M*t (M = 8 * prod of odd primes <= L), keeps prime p = P(q), and for every test
polynomial h (all a + bX, |a|,|b| <= B, plus a + bX + cX^2 for small coefficients) whose relevant primes
(2 * lc(P) * Res(R, h^v)) are all <= L, checks (h(q)/p) = +1.  It also reports, for h whose relevant primes
are NOT all <= L, how often the symbol is -1 (sanity: the claim is not vacuous).

Controls: (a) P = X^2 - 3X + 1 (P(0) = 1 but positive real roots: the real place breaks the trap);
          (b) q = 4 mod 8 instead of 0 mod 8 (2-adic trap condition violated);
          (c) q = M*t + 1 shift (q not 0 mod small odd l).

Usage: uv run --with sympy --with gmpy2 python scripts/z53_noncrtlogic_trapcheck.py [T] [L] [B]
"""
import sys
import itertools
import gmpy2
from sympy import Poly, symbols, resultant, factorint, primerange, ZZ

X = symbols('X')


def relevant_ok(P, h, L):
    n = Poly(P, X).degree()
    R = Poly(X**n * P.subs(X, 1 / X), X)
    R = Poly(R.as_expr().expand(), X)
    d = Poly(h, X).degree()
    hv = Poly((X**d * h.subs(X, 1 / X)).expand(), X)
    res = int(resultant(R.as_expr(), hv.as_expr(), X))
    lc = int(Poly(P, X).LC())
    if res == 0:
        return None
    N = abs(2 * lc * res)
    return all(l <= L for l in factorint(N))


def run(name, P, T, L, B, shift_mode):
    M = 8
    for l in primerange(3, L + 1):
        M *= l
    coeffs = [int(c) for c in Poly(P, X).all_coeffs()]

    def Pv(q):
        v = 0
        for c in coeffs:
            v = v * q + c
        return v
    hs = []
    for a in range(-B, B + 1):
        for b in range(-B, B + 1):
            if a == 0 and b == 0:
                continue
            hs.append(a + b * X)
    for a, b, c in itertools.product(range(-3, 4), range(-3, 4), range(1, 4)):
        hs.append(a + b * X + c * X**2)
    flags = []
    for h in hs:
        ok = relevant_ok(P, h, L)
        if ok is None:
            continue
        hc = [int(c) for c in Poly(h, X).all_coeffs()]
        flags.append((h, hc, ok))
    nprimes = 0
    viol = 0
    viol_ex = []
    pred_tests = 0
    other_tests = 0
    other_minus = 0
    for t in range(1, T + 1):
        if shift_mode == 'q4mod8':
            q = M * t + 4 * (M // 8) * 1  # q = 4 mod 8 (M/8 odd), still 0 mod odd l <= L
        elif shift_mode == 'shift1':
            q = M * t + 24  # q = 24 mod M: violates q = 0 mod 5,7,11,13
        else:
            q = M * t
        p = Pv(q)
        if p <= 0 or not gmpy2.is_prime(p):
            continue
        nprimes += 1
        for h, hc, ok in flags:
            v = 0
            for c in hc:
                v = v * q + c
            if v % p == 0:
                continue
            s = gmpy2.jacobi(v % p, p)
            if ok:
                pred_tests += 1
                if s != 1:
                    viol += 1
                    if len(viol_ex) < 5:
                        viol_ex.append((str(h), q))
            else:
                other_tests += 1
                if s == -1:
                    other_minus += 1
    npred = sum(1 for f in flags if f[2])
    print(f"[{name}] mode={shift_mode} M={M} primes p=P(q) found={nprimes}; h with relevant primes<=L: {npred}/{len(flags)}")
    print(f"   predicted-(+1) tests={pred_tests}  violations={viol}  examples={viol_ex}")
    print(f"   other tests={other_tests}  share of -1 among them={other_minus / max(1, other_tests):.3f}")
    return nprimes, pred_tests, viol


def main():
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    L = int(sys.argv[2]) if len(sys.argv) > 2 else 13
    B = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    fams = [
        ('X^2+1', X**2 + 1),
        ('2X^2+1', 2 * X**2 + 1),
        ('3X^2+1', 3 * X**2 + 1),
        ('X^4+1', X**4 + 1),
        ('Phi5=X^4+X^3+X^2+X+1', X**4 + X**3 + X**2 + X + 1),
        ('Phi6=X^2-X+1', X**2 - X + 1),
        ('2X^3+2X+1', 2 * X**3 + 2 * X + 1),
        ('X+1', X + 1),
    ]
    tot_v = 0
    for name, P in fams:
        _, _, v = run(name, P, T, L, B, 'trap')
        tot_v += v
    print("TOTAL violations at trap points:", tot_v)
    print("--- controls (violations EXPECTED) ---")
    run('X^2-3X+1 (positive real roots)', X**2 - 3 * X + 1, T, L, B, 'trap')
    run('X^2+1', X**2 + 1, T, L, B, 'q4mod8')
    run('X^2+1', X**2 + 1, T, L, B, 'shift1')
    run('X^4+1', X**4 + 1, T, L, B, 'q4mod8')


if __name__ == '__main__':
    main()
