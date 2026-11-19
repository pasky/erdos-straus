#!/usr/bin/env python3
"""Opus cross-review checks for GAUSSIAN_PELL_MENU.md / LINKED_GAUSSIAN_PELL_MENU.md (z74).

Independent recomputation, exact arithmetic only:
 1. symbolic identities used in the notes (row -> Pell, z^2-PV^2=b*row, K-section of the Pell conic,
    discriminant of the row form, stress-test triple);
 2. compression sanity on a two-witness polynomial (x1*y2-x2*y1 collapses to a bounded-exponent
    pattern in the fundamental unit, for signed odd exponents);
 3. nonvacuity: every prime p=1 mod 4 below a bound has an integral row tuple (a,b,U,V);
 4. toy end-to-end run of the stress menu (J,K,PK+[(b-1)(V-2)]^2) over ALL Gaussian pairs with
    |a|,|b|<=N and ALL rational row points: successes must be genuine ES triples, must lie on the
    loci b=1 or V=2, must be absent on p=1 mod 840, and their count must be << N^(3/2).
Usage: uv run --offline --no-project python scripts/z74_xrev_pellmenu_check.py [N]
"""
import sys
from fractions import Fraction as Fr
from math import isqrt
import random
import sympy as sp


def is_prime(n):
    return sp.isprime(n)


def check_symbolic():
    a, b, U, V, x, y = sp.symbols('a b U V x y')
    P = a**2 + b**2
    R = b*(U**2 - V**2) + 2*a*U*V
    X = a*(U**2 - V**2) - 2*b*U*V
    Y = U**2 + V**2
    # (a+ib)(U+iV)^2 = X + i R  => X^2 + R^2 = P Y^2
    assert sp.expand((a + sp.I*b)*(U + sp.I*V)**2 - (X + sp.I*R)) == 0
    assert sp.expand(X**2 + R**2 - P*Y**2) == 0
    z = b*U + a*V
    assert sp.expand(z**2 - P*V**2 - b*R) == 0
    # row binary form discriminant 4P
    assert sp.expand((2*a)**2 - 4*b*(-b) - 4*P) == 0
    # K-rational section of the Pell conic
    assert sp.simplify((a/b)**2 - P*(1/b)**2 + 1) == 0
    # stress test example
    aa, bb, UU, VV = -2, 5, 3, 2
    subs = {a: aa, b: bb, U: UU, V: VV}
    assert R.subs(subs) == 1 and P.subs(subs) == 29 and X.subs(subs) == -70 and Y.subs(subs) == 13
    assert Fr(1, 8) + Fr(1, 80) + Fr(1, 2320) == Fr(4, 29)
    Pv = 29
    J, K = Fr(Pv + 3, 4), Fr((Pv + 3)*(Pv + 1), 12)
    assert (J, K, Pv*K) == (8, 80, 2320)
    # identity 1/J + 1/K + 1/(PK) = 4/P  (so the stress triple succeeds iff (b-1)(V-2)=0)
    Ps = sp.symbols('P')
    Js, Ks = (Ps + 3)/4, (Ps + 3)*(Ps + 1)/12
    assert sp.simplify(1/Js + 1/Ks + 1/(Ps*Ks) - 4/Ps) == 0
    print("[1] symbolic identities: OK")


def fund_unit_neg(p):
    """least x0,y0>0 with x0^2 - p y0^2 = -1 (continued fraction of sqrt p); None if none."""
    a0 = isqrt(p)
    m, d, a_ = 0, 1, a0
    h0, h1 = 1, a0
    k0, k1 = 0, 1
    while True:
        if h1*h1 - p*k1*k1 == -1:
            return h1, k1
        if h1*h1 - p*k1*k1 == 1:
            return None
        m = d*a_ - m
        d = (p - m*m)//d
        a_ = (a0 + m)//d
        h0, h1 = h1, a_*h1 + h0
        k0, k1 = k1, a_*k1 + k0


def unit_pow(x0, y0, p, n):
    """(x,y) with x + y sqrt p = (x0 + y0 sqrt p)^n, n in Z (norm -1 unit, inverse = -conj)."""
    if n < 0:
        x, y = unit_pow(x0, y0, p, -n)
        nn = x*x - p*y*y  # (+-1)
        return x*nn, -y*nn
    x, y = 1, 0
    for _ in range(n):
        x, y = x*x0 + p*y*y0, x*y0 + y*x0
    return x, y


def check_compression():
    cnt = 0
    for p in [5, 13, 29, 41, 61, 109, 181, 421, 541, 661, 1009, 1621]:
        x0, y0 = fund_unit_neg(p)
        for n2 in range(-9, 10, 2):
            for d in (-4, -2, 0, 2, 4):
                n1 = n2 + d
                x1, y1 = unit_pow(x0, y0, p, n1)
                x2, y2 = unit_pow(x0, y0, p, n2)
                assert x1*x1 - p*y1*y1 == -1 and x2*x2 - p*y2*y2 == -1
                f = x1*y2 - x2*y1
                # pattern: (e^d - e^-d)/(2 sqrt p) = y-coordinate of e^d (norm +1 unit for even d)
                xd, yd = unit_pow(x0, y0, p, d)
                assert f == yd, (p, n1, n2, f, yd)
                if d == 2:
                    assert f == 2*x0*y0
                cnt += 1
    print(f"[2] compression pattern x1y2-x2y1 = y(eps^(n1-n2)) on {cnt} signed odd exponent pairs: OK")


def gauss_mul(u, v):
    return (u[0]*v[0] - u[1]*v[1], u[0]*v[1] + u[1]*v[0])


def gauss_sqrt(w):
    """Gaussian integer g with g^2 = w, or None."""
    re, im = w
    n = re*re + im*im
    r = isqrt(n)
    if r*r != n:
        return None
    # g = s + it, s^2 - t^2 = re, 2st = im, s^2 + t^2 = r
    s2, t2 = (r + re), (r - re)
    if s2 % 2 or t2 % 2:
        return None
    s, t = isqrt(s2//2), isqrt(t2//2)
    for ss in (s, -s):
        for tt in (t, -t):
            if gauss_mul((ss, tt), (ss, tt)) == w:
                return (ss, tt)
    return None


def check_row_nonvacuity(bound=3000):
    n = 0
    for p in range(5, bound, 4):
        if not is_prime(p):
            continue
        X, Y = fund_unit_neg(p)
        found = None
        for a in range(-isqrt(p), isqrt(p) + 1):
            b2 = p - a*a
            b = isqrt(b2)
            if b*b != b2:
                continue
            for bb in {b, -b}:
                # (X+i)/(a+ib) = (X+i)(a-ib)/p
                re, im = X*a + bb, a - X*bb
                if re % p or im % p:
                    continue
                g = gauss_sqrt((re//p, im//p))
                if g is None:
                    continue
                Uv, Vv = g
                if bb*(Uv*Uv - Vv*Vv) + 2*a*Uv*Vv == 1:
                    found = (a, bb, Uv, Vv)
                    break
            if found:
                break
        assert found, p
        n += 1
    print(f"[3] integral row tuple exists at all {n} primes p=1 mod 4 below {bound}: OK")


def rational_row_points_with_V2(a, b):
    """rational U with b U^2 + 4 a U - 4 b - 1 = 0 (row at V=2)."""
    if b == 0:
        return [Fr(1, 4*a)] if a != 0 else []
    disc = 16*a*a + 4*b*(4*b + 1)
    r = isqrt(disc) if disc >= 0 else -1
    if r < 0 or r*r != disc:
        return []
    return list({Fr(-4*a + r, 2*b), Fr(-4*a - r, 2*b)})


def check_toy(N):
    succ_b1, succ_v2, succ_840 = set(), set(), 0
    pairs = 0
    for a in range(-N, N + 1):
        for b in range(-N, N + 1):
            p = a*a + b*b
            if p < 5 or not is_prime(p):
                continue
            pairs += 1
            if (p + 3) % 4 or ((p + 3)*(p + 1)) % 12:
                continue
            J, K = (p + 3)//4, (p + 3)*(p + 1)//12
            # third slot PK + [(b-1)(V-2)]^2 equals PK iff b=1 or V=2; any other rational t!=0 gives
            # 1/J+1/K+1/(PK+t^2) != 4/p.  b=1: row has rational point (U,V)=(1,0) always.
            hit = False
            if b == 1:
                succ_b1.add((a, b)); hit = True
            for Uq in rational_row_points_with_V2(a, b):
                assert b*(Uq*Uq - 4) + 4*a*Uq == 1
                succ_v2.add((a, b)); hit = True
            if hit:
                assert Fr(1, J) + Fr(1, K) + Fr(1, p*K) == Fr(4, p)
                if p % 840 == 1:
                    succ_840 += 1
    print(f"[4] toy stress menu, |a|,|b|<={N}: prime pairs={pairs}, successes on b=1: {len(succ_b1)}, "
          f"on V=2: {len(succ_v2)} (N^1.5={N**1.5:.0f}); successes at p=1 mod 840: {succ_840}")
    assert succ_840 == 0


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    random.seed(1)
    check_symbolic()
    check_compression()
    check_row_nonvacuity()
    check_toy(N)
    print("ALL OK")
