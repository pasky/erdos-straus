#!/usr/bin/env python3
"""Opus cross-review checks for the PELLNOGO lane (z74; notes by GPT Astra).

Independent recomputation (exact integer / rational arithmetic; sympy only for symbolic identities and primality):
 A. ES size bounds used by every compression argument (u<=3p/4, v<=2pu/(4u-p), w<=puv<=9p^4/8), all ES triples p<400.
 B. PELL_POLYNOMIAL_MENU_AUDIT §4 certificate (p=142211032321, x=15461460, y=41) and its success locus K=cY.
 C. PELL_MULTI_GAP_AUDIT exact cancellation tests (p=5,17,176401; N=1,21,101), cube-generator break, quotient
    identity, and the 0/0 example.
 D. symbolic identities quoted as (counter)examples: (P/4,X,-X); (P/2,P(1+Y)/2,P(1+Y)/(2Y)); the rational identity
    branch G1=P(x+2)/(4(x+1)), G2=G3=P(x+2)/2, its t-form, resultant, and a brute-force check that it never succeeds.
 E. PELL_RAMIFIED_MENU_AUDIT: exact valuation law v_p(Y_j)=v_p(j)+v_p(y0) at signed j, and the §4 ES construction.
 F. PELL_REMAINDER_SELECTOR / PELL_RESIDUE_INTERFACE_AUDIT: permutation of U_{1+4j} mod n^k (incl. composite n and
    p|y anchors), the two-remainder division-free decoder, and constancy of coordinates mod 5^L for (2+sqrt5)^(5^L).
 G. PELL_MULTI_GAP_AUDIT integer-pair replacement: x1*x2 - p*y1*y2 = -X_{n1-n2}, an integer polynomial in (x0,y0).
 H. PELL_ES_MENU_NOGO §"unit-square progression" on the §4 menu entry: an explicit prime l and nonzero square class r
    mod l on which the success curve has no rational point (no root of G(P,Z) mod l, unit leading coefficient).
Usage: uv run --offline --no-project python scripts/z74_xrev_pellnogo_check.py
"""
from fractions import Fraction as Fr
from math import isqrt, gcd
import random
import sympy as sp


def pw(x0, y0, p, j, mod=None):
    """(x0 + y0 sqrt p)^j for integer j (negative via the inverse of a norm -1 unit); optionally mod `mod`."""
    if j < 0:
        assert x0 * x0 - p * y0 * y0 == -1
        x0, y0, j = -x0, y0, -j
    X, Y = 1, 0
    bx, by = x0, y0
    while j:
        if j & 1:
            X, Y = X * bx + p * Y * by, X * by + Y * bx
        bx, by = bx * bx + p * by * by, 2 * bx * by
        if mod:
            X, Y, bx, by = X % mod, Y % mod, bx % mod, by % mod
        j >>= 1
    return X, Y


def vp(n, p):
    if n == 0:
        return 10 ** 9
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def check_A():
    cnt = 0
    for p in sp.primerange(3, 400):
        for u in range(p // 4 + 1, 3 * p // 4 + 2):
            r = Fr(4, p) - Fr(1, u)
            if r <= 0:
                continue
            vmax = int(2 / r) + 1
            for v in range(u, vmax + 1):
                s = r - Fr(1, v)
                if s <= 0 or s.numerator != 1 or s.denominator < v:
                    continue
                w = s.denominator
                assert 4 * u <= 3 * p and v * (4 * u - p) <= 2 * p * u and w <= p * u * v and 8 * w <= 9 * p ** 4
                cnt += 1
    print(f"[A] ES size bounds hold on all {cnt} sorted ES triples for primes 3<=p<400: OK")


def check_B():
    p, x, y, c = 142211032321, 15461460, 41, 867140441
    assert x * x + 1 == y * y * p and p % 840 == 1 and sp.isprime(p)
    assert all(p % q for q in sp.primerange(2, isqrt(p) + 1))  # explicit trial division
    K = (p + 3) // 4
    assert 4 * K == p + 3 and K == c * y and (y + 1) % 3 == 0
    T = (K, p * c * (y + 1) // 3, p * c * y * (y + 1) // 3)
    assert T == (35552758081, 1726437121946560709854, 70783921999808989104014)
    assert Fr(1, T[0]) + Fr(1, T[1]) + Fr(1, T[2]) == Fr(4, p)
    P, Y, C = sp.symbols('P Y c', positive=True)
    Ks = (P + 3) / 4
    lhs = 1 / Ks + 3 / (P * C * (Y + 1)) + 3 / (P * C * Y * (Y + 1)) - 4 / P
    num = sp.fraction(sp.together(lhs))[0]
    assert sp.rem(sp.Poly(num, Y), sp.Poly(P + 3 - 4 * C * Y, Y)).is_zero
    # the cleared defect H=4fgh-P(fg+gh+hf) of the triple: its zero locus = {K=cY} plus coordinate-zero loci only
    f, g, h = Ks, P * C * (Y + 1) / 3, P * C * Y * (Y + 1) / 3
    H = sp.factor(sp.expand(4 * f * g * h - P * (f * g + g * h + h * f)))
    facs = [fa for fa, _ in sp.factor_list(sp.numer(sp.together(H)), P, Y, C)[1]]
    curve = [fa for fa in facs if sp.expand(fa - (P + 3 - 4 * C * Y)) == 0 or sp.expand(fa + (P + 3 - 4 * C * Y)) == 0]
    rest = [fa for fa in facs if fa not in curve]
    assert len(curve) == 1 and all(fa in (P, C, Y, Y + 1) for fa in rest), facs
    print("[B] §4 certificate: prime (trial division), Pell, 1 mod 840, exact ES triple, locus K=cY: OK")


def check_C():
    def xs(p, x0, y0, j):
        return pw(x0, y0, p, j)[0]
    for N in (1, 21, 101):
        v5 = xs(5, 2, 1, N + 4) - 18 * xs(5, 2, 1, N + 2) + xs(5, 2, 1, N) + 7
        v17 = xs(17, 4, 1, N + 4) - 18 * xs(17, 4, 1, N + 2) + xs(17, 4, 1, N) + 7
        w17 = xs(17, 4, 1, N + 4) - 66 * xs(17, 4, 1, N + 2) + xs(17, 4, 1, N) + 7
        # cube generator at 5: eps^3 = 38+17 sqrt5 as spacing generator
        c5 = xs(5, 2, 1, 3 * (N + 4)) - 18 * xs(5, 2, 1, 3 * (N + 2)) + xs(5, 2, 1, 3 * N) + 7
        assert v5 == 7 and v17 != 7 and w17 == 7 and c5 != 7
        for (p, x0, y0) in ((5, 2, 1), (17, 4, 1), (176401, 420, 1)):
            num = xs(p, x0, y0, N + 4) + xs(p, x0, y0, N)
            den = xs(p, x0, y0, N + 2)
            assert num == (4 * x0 * x0 + 2) * den
    assert sp.isprime(176401) and 420 ** 2 + 1 == 176401 and 4 * 420 ** 2 + 2 == 705602
    # 0/0 example: 1+(y3-1)/(x1-x2) at p=5, third witness the fundamental one (y3=1)
    for n1, n2 in ((1, 3), (5, -7), (-1, 9)):
        x1, x2 = pw(2, 1, 5, n1)[0], pw(2, 1, 5, n2)[0]
        assert x1 != x2 and Fr(1) + Fr(1 - 1, x1 - x2) == 1
    print("[C] cancellation at 5 (all N), failure at 17 unless 66, break under eps^3, quotient = 4x0^2+2 at 5,17,"
          "176401 (prime), 0/0 example: OK")


def check_D():
    P, X, Y, x, s, t = sp.symbols('P X Y x s t')
    assert sp.simplify(4 / P + 1 / X - 1 / X - 4 / P) == 0
    assert sp.simplify(2 / P + 2 / (P * (1 + Y)) + 2 * Y / (P * (1 + Y)) - 4 / P) == 0
    G1, G2 = P * (x + 2) / (4 * (x + 1)), P * (x + 2) / 2
    assert sp.simplify(1 / G1 + 2 / G2 - 4 / P) == 0
    xt = (t - 1 / t) / 2
    g1t = sp.factor(sp.together(G1.subs(x, xt).subs(P, s ** 2)))
    n, d = sp.fraction(g1t)
    assert sp.expand(n * 4 * (t ** 2 + 2 * t - 1) - d * s ** 2 * (t ** 2 + 4 * t - 1)) == 0
    assert sp.resultant(t ** 2 + 4 * t - 1, t ** 2 + 2 * t - 1, t) != 0
    # brute force: never three positive integers at an integral negative-Pell witness
    hits = 0
    for p in sp.primerange(5, 3000):
        if p % 4 != 1:
            continue
        x0 = y0 = None
        for yy in range(1, 20000):
            q = p * yy * yy - 1
            r = isqrt(q)
            if r * r == q:
                x0, y0 = r, yy
                break
        if x0 is None:
            continue
        for j in range(-41, 42, 2):
            xx = pw(x0, y0, p, j)[0]
            for sx in (xx, -xx):
                if sx + 1 == 0:
                    continue
                g1 = Fr(p * (sx + 2), 4 * (sx + 1))
                g2 = Fr(p * (sx + 2), 2)
                if g1 > 0 and g2 > 0 and g1.denominator == 1 and g2.denominator == 1:
                    hits += 1
    assert hits == 0
    print("[D] (P/4,X,-X), (P/2,P(1+Y)/2,P(1+Y)/(2Y)), G-branch identity, t-form, nonzero resultant; no success of the "
          "G-branch at fundamental-unit powers |j|<=41 for primes p=1(4)<3000 found by search: OK")


def fund_neg(p):
    for yy in range(1, 10 ** 6):
        q = p * yy * yy - 1
        r = isqrt(q)
        if r * r == q:
            return r, yy
    raise ValueError(p)


def check_E():
    tests = 0
    for p in (5, 13, 17, 29, 37):
        x0, y0 = fund_neg(p)
        for anchor_exp in (1, p, p * p):
            ax, ay = pw(x0, y0, p, anchor_exp)
            w = vp(ay, p)
            mod = p ** (w + 12)  # valuations below w+12 are read off exactly modulo p^(w+12)
            for j in list(range(-3 * p, 3 * p + 1)) + [p ** 3, -p ** 3, 2 * p ** 2]:
                if j == 0:
                    continue
                Yj = pw(ax, ay, p, j, mod)[1]
                assert vp(j, p) + w < w + 12 and vp(Yj % mod, p) == vp(j, p) + w, (p, anchor_exp, j)
                tests += 1
    # §4: q=3 mod 4, q ∤ M, p = 1 mod M, p = -4 mod q ; triple (b, cp, bcp) scaled by p^(2a)
    M = 840 * 4
    cons = 0
    for q in (11, 19, 23, 31):
        c = (q + 1) // 4
        found = 0
        for p in sp.primerange(5, 10 ** 7):
            if p % M == 1 and (p + 4) % q == 0:
                b = (1 + p * c) // q
                assert (1 + p * c) % q == 0 and 4 * b * c == 1 + b + p * c
                for a in (0, 1, 2):
                    n = p ** (2 * a + 1)
                    T = (b * p ** (2 * a), c * p ** (2 * a + 1), b * c * p ** (2 * a + 1))
                    assert Fr(1, T[0]) + Fr(1, T[1]) + Fr(1, T[2]) == Fr(4, n)
                found += 1
                cons += 1
                if found == 3:
                    break
    print(f"[E] ramified valuation law on {tests} signed indices (anchors eta, eta^p, eta^(p^2)); §4 ES triples at "
          f"{cons} primes x 3 tower levels: OK")


def U(x, y, n, m):
    X, Y = pw(x, y, n, m)
    assert Y % y == 0
    return Y // y


def check_F():
    cases = [(5, 2, 1, 4), (13, 18, 5, 3), (65, 8, 1, 2), (145, 12, 1, 2), (5, 682, 305, 4), (125, None, None, 2)]
    tot = 0
    for n, x, y, k in cases:
        if x is None:  # n=125: negative Pell 682^2-125*61^2=-1
            x, y = 682, 61
        assert x * x - n * y * y == -1
        N = n ** k
        seen = set()
        # recurrence U_{m+2} = 2x U_{m+1} + U_m mod N (independent of the binomial proofs)
        u0, u1 = 0, 1
        vals = {}
        m = 1
        while len(vals) < N:
            # advance from index m to m+4 by recurrence
            vals[(m - 1) // 4] = u1 % N
            for _ in range(4):
                u0, u1 = u1, (2 * x * u1 + u0) % N
            m += 4
        seen = set(vals.values())
        assert len(seen) == N
        tot += N
        # division-free decoding with two remainders
        for _ in range(30):
            s = random.choice([1 + 4 * random.randrange(N), random.randrange(1, 3 * N)])
            Ys = pw(x, y, n, s)[1]
            r = Ys % (y * N)
            D = (-N * r) % (y * N + 1)
            assert r == y * (Ys // y % N) and D == (Ys // y) % N
    # coordinates mod 5^L constant for anchor (2+sqrt5)^(5^L), while U_s mod 5 = s mod 5
    for L in (1, 2, 3):
        ax, ay = pw(2, 1, 5, 5 ** L)
        assert vp(ay, 5) == L
        mod = 5 ** L
        cl = set()
        us = set()
        for s in range(1, 4 * 40, 4):
            Xs, Ys = pw(ax, ay, 5, s)
            cl.add((Xs % mod, Ys % mod))
            us.add((Ys // ay) % 5)
        assert len(cl) == 1 and us == set(range(5))
    print(f"[F] permutation verified on {tot} residues (n=5,13,65,145,125 and 5|y anchor); two-remainder decoder; "
          "mod-5^L coordinate blindness for L=1,2,3: OK")


def check_G():
    x0, y0, X, Yv, P = sp.symbols('x0 y0 X Y P')
    for p in (5, 13, 29, 41):
        a, b = fund_neg(p)
        for n1, n2 in ((1, 3), (7, -5), (-9, -9), (21, 19)):
            x1, y1 = pw(a, b, p, n1)
            x2, y2 = pw(a, b, p, n2)
            lhs = x1 * x2 - p * y1 * y2
            assert lhs == -pw(a, b, p, n1 - n2)[0]
    # integer polynomial form of X_k for k=2,-2 (no new denominators)
    X2 = sp.expand((x0 ** 2 + P * y0 ** 2))
    assert all(cf.is_integer for cf in sp.Poly(X2, x0, y0, P).coeffs())
    print("[G] x1x2-p y1y2 = -X_{n1-n2} (integer polynomial pair in x0,y0,P): OK")


def check_H():
    c = 867140441
    # success locus of the §4 triple: K=cY, i.e. Y=(P+3)/(4c); Pell x^2 = P Y^2 - 1.
    # G(P,Z) = (4c)^2 Z^2 - (P (P+3)^2 - 16 c^2), leading coefficient 16c^2.
    P, Z = sp.symbols('P Z')
    G = (4 * c) ** 2 * Z ** 2 - (P * (P + 3) ** 2 - 16 * c ** 2)
    assert sp.Poly(G, P, Z).is_irreducible
    for ell in sp.primerange(11, 200):
        if (2 * c) % ell == 0:
            continue
        for r in range(1, ell):
            if pow(r, (ell - 1) // 2, ell) != 1:
                continue  # r must be a nonzero square
            f = (r * (r + 3) ** 2 - 16 * c * c) % ell
            if f != 0 and pow(f, (ell - 1) // 2, ell) == ell - 1:
                p = 142211032321
                assert p % ell != r  # the certified hit cannot lie in the excluded class
                print(f"[H] NOGO square-class step on the §4 entry: l={ell}, r={r} (nonzero square) gives no rational "
                      f"point on the success curve for p=r mod l; the certified hit has p mod l={p % ell}: OK")
                return
    raise AssertionError("no class found")


if __name__ == "__main__":
    random.seed(74)
    check_A(); check_B(); check_C(); check_D(); check_E(); check_F(); check_G(); check_H()
    print("ALL OK")
