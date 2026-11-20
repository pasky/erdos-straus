"""Opus cross-review (z74) of the PELLMODELS lane: independent finite/symbolic checks.

Not a proof of any model construction; checks the quoted identities, smoothness certificates,
local recipes, point counts and ordinary-prime examples used in
LOGIC_POSITIVE_PELL_AUDIT, LOGIC_NEGATIVE_PELL_TS_TEST, LOGIC_NEGATIVE_PELL_ROOT_AUDIT,
LOGIC_NEG_PELL_MARKS, LOGIC_PELL_UNIT_GROUP, LOGIC_SIGNED_PELL_FIBER.
Run: (ulimit -v 6000000; timeout 1800 uv run --offline --no-sync python scripts/z74_xrev_pellmodels_checks.py)
"""
from itertools import product
from math import isqrt, gcd
from sympy import (I, Rational, cancel, expand, groebner, symbols, sqrt, simplify,
                   factor_list, Poly, isprime)


def ok(cond, msg):
    assert cond, msg
    print('  ok:', msg)


def symbolic():
    print('A. symbolic identities and smoothness certificates')
    s, z, v, t, b0 = symbols('s z v t b0')
    # A1 positive Pell stage (POSITIVE_PELL §1)
    g = v**2 - 2*z - s*z**2
    x, y = 1 + s*z, v
    ok(expand(x**2 - s*y**2 - 1 + s*g) == 0, 'Pell stage: x^2-s y^2 = 1 on v^2=2z+sz^2')
    G = groebner([g, g.diff(z), g.diff(v)], z, v, s, domain='QQ')
    ok(G.exprs == [1], 'Pell stage smooth over Q[s] (g, g_z, g_v generate 1)')
    zl, vl = 2*t**2/(1 - b0*t**2), 2*t/(1 - b0*t**2)
    ok(cancel(vl**2 - 2*zl - b0*zl**2) == 0 and cancel(zl/vl - t) == 0,
       'local chart z=2t^2/(1-bt^2), v=2t/(1-bt^2) solves the stage, t=z/v')
    # A2 negative Pell edge smooth (TS_TEST §3 / SIGNED §2)
    xx, yy = symbols('xx yy')
    h = xx**2 - s*yy**2 + 1
    ok(groebner([h, h.diff(xx), h.diff(yy)], xx, yy, s, domain='QQ').exprs == [1],
       'negative Pell edge x^2-sy^2+1 smooth over Q[s]')
    # A3 joint base of TS_TEST §2 (= row of ROOT_AUDIT, MARKS, SIGNED)
    a, b, U, V = symbols('a b U V')
    H = b*(U**2 - V**2) + 2*a*U*V
    X, Y, P = a*(U**2 - V**2) - 2*b*U*V, U**2 + V**2, a**2 + b**2
    ok(expand((a + I*b)*(U + I*V)**2 - X - I*H) == 0, '(a+ib)(U+iV)^2 = X + i H')
    ok(expand(X**2 + H**2 - P*Y**2) == 0, 'X^2+H^2 = P Y^2, so X^2+1=PY^2 on H=1')
    ok(expand(U*H.diff(U) + V*H.diff(V) - 2*H) == 0, 'Euler identity: base smooth over Q[a,b]')
    ok(groebner([H - 1, H.diff(U), H.diff(V)], U, V, a, b, domain='QQ').exprs == [1],
       'row H=1 smooth over Q[a,b] (Groebner certificate)')
    C, D = U**2 - V**2, 2*U*V
    lhs = (D*a + C*b)**2 - b*((C**2 - D**2)*b + 2*C*D*a)
    ok(cancel(lhs / P) == expand(D**2), '(Da+Cb)^2 = b[(C^2-D^2)b+2CDa] + D^2 P: b unit mod P')
    # inverse chart (ROOT §4, MARKS, UNIT_GROUP §1)
    Xs = symbols('Xs')
    ch = {a: (C*Xs + D)/Y**2, b: (C - D*Xs)/Y**2}
    ok(all(cancel(f.subs(ch)) == 0 for f in (H - 1, X - Xs, P*Y**2 - 1 - Xs**2)),
       'chart a=(CX+D)/Y^2, b=(C-DX)/Y^2 inverts (X,L)=(X,1)')
    # E/P isomorphism and X = j mod P (ROOT §2)
    tt, vv = symbols('tt vv')
    for j in (I, -I):
        fib = {a: j/tt**2, b: 1/tt**2, U: tt - j*vv, V: vv}
        ok(all(cancel(f.subs(fib, simultaneous=True)) == 0 for f in (P, H - 1, X - j)),
           f'E/P chart b=t^-2, a={j} t^-2, u=t-{j}v: P=0, row=1, X={j}')
        ok(expand(Y.subs(fib, simultaneous=True) - tt*(tt - 2*j*vv)) == 0, f'Y = t(t-2({j})v) on fibre')
    # MARKS: a - X b = S(a^2+b^2) modulo row (S=D here, D_marks=C here)
    rowv = D*a + C*b
    ok(expand((a*rowv - X*b) - D*P) == 0, 'a*row - Xb = S*P  (so a = Xb mod (row,P))')
    # b(D_marks + X S) = 1 mod (row, P): b(C+XD) - row = S(Xb - a), and Xb - a = -S P + a(1-row)
    ok(expand(b*(C + X*D) - rowv - D*(X*b - a)) == 0, 'b(C+XD) - row = S(Xb - a), so b(D+XS)=1 mod (row,P)')
    # square cover chart (MARKS): t=wY-X, X=(1/t-t)/2, w=(t+1/t)/(2Y)
    tc = symbols('tc')
    Xc, wc = (1/tc - tc)/2, (tc + 1/tc)/(2*Y)
    ok(cancel(wc*Y - Xc - tc) == 0 and cancel((wc*Y)**2 - Xc**2 - 1) == 0,
       'square-cover chart: (wY)^2 - X^2 = 1 with t = wY-X')
    # c^2 P - 1 numerator (MARKS)
    c = symbols('c', nonzero=True)
    num = expand(cancel((c**2*(1 + Xs**2)/Y**2 - 1)*Y**2))
    disc = Poly(num, Xs).discriminant()
    ok(expand(num - (c**2*Xs**2 + c**2 - Y**2)) == 0 and expand(disc + 4*c**2*(c**2 - Y**2)) == 0,
       'c^2P-1 = (c^2X^2+c^2-Y^2)/Y^2, discriminant -4c^2(c^2-Y^2) != 0')
    # UNIT_GROUP §1 isomorphism both ways
    Zs = symbols('Zs', nonzero=True)
    X0, t0 = (Zs - 1/Zs)/2, (Zs + 1/Zs)/(2*Y)
    a0, b0_ = (C*X0 + D)/Y**2, (C - D*X0)/Y**2
    ok(cancel(D*a0 + C*b0_ - 1) == 0 and cancel(C*a0 - D*b0_ - X0) == 0
       and cancel(t0**2 - a0**2 - b0_**2) == 0 and cancel(X0 + t0*Y - Zs) == 0,
       'E[t,1/Y] = Q[u,v,1/Y][Z^{+-1}]: relations and Z -> X+tY')
    pt = {U: 1, V: I, a: 0, b: Rational(1, 2)}
    ok(Y.subs(pt) == 0 and (H - 1).subs(pt) == 0 and P.subs(pt) == Rational(1, 4),
       'complex point (1,i,0,1/2,t=1/2) of E[t] has Y=0: Y not a unit')
    T = symbols('T')
    zz = Poly((X + T*Y)**2, T).rem(Poly(T**2 - P, T)).as_expr()
    ok(expand(zz - (X**2 + P*Y**2) - 2*X*Y*T) == 0, 'z^2 = (X^2+PY^2) + 2XY t = (2X^2+1)+2XY t on PY^2=X^2+1')
    # SIGNED §4 vertical-component example
    Uu, Vu, Wu, Zu = symbols('Uu Vu Wu Zu')
    Gb = groebner([Uu*Vu - Wu**2, Uu + Wu*Zu], Uu, Vu, Wu, Zu, order='lex', domain='QQ')
    ok(Gb.reduce(Wu*(Vu*Zu + Wu))[1] == 0, 'D[Z]/(U+WZ): W(VZ+W)=0')
    ok(Gb.reduce(Wu)[1] != 0 and Gb.reduce(Vu*Zu + Wu)[1] != 0, '... with both factors nonzero')
    ok(Gb.reduce(Wu)[1] != 0 and groebner([Uu*Vu - Wu**2, Uu], Uu, Vu, Wu, domain='QQ').reduce(Wu)[1] != 0,
       'U does not divide W in Q[U,V,W]/(UV-W^2)')


def finite_fields():
    print('B. finite-field counts and local points')
    for q in (3, 5, 7, 11, 13, 17, 19, 23):
        sq = {n*n % q for n in range(1, q)}
        roots = sum(1 for x in range(q) if (x*x + 1) % q == 0)
        pairs = sum(1 for u, v in product(range(q), repeat=2) if (u*u + v*v) % q)
        good_X = sum(1 for x in range(q) if (1 + x*x) % q in sq)
        assert pairs == ((q - 1)**2 if roots else q*q - 1)
        assert good_X == (q - 1 - roots)//2
        # MARKS cover chart: (u,v,t) with Y t (t^2+1) != 0 maps <=2:1 onto root points with Y!=0, P square
        img = {}
        n = 0
        for u, v, tc in product(range(q), repeat=3):
            Y = (u*u + v*v) % q
            if Y == 0 or tc == 0 or (tc*tc + 1) % q == 0:
                continue
            n += 1
            it = pow(tc, -1, q)
            X = (it - tc)*pow(2, -1, q) % q
            img[(u, v, X)] = img.get((u, v, X), 0) + 1
        assert max(img.values()) <= 2 and n == pairs*(q - 1 - roots)
        assert len(img) == pairs*good_X
        # local signed points: every unit s has a smooth point on x^2-sy^2=-1 and on x^2+y^2=s
        for s_ in range(1, q):
            assert any((x*x - s_*y*y + 1) % q == 0 for x, y in product(range(q), repeat=2))
            assert any((x*x + y*y - s_) % q == 0 and (x or y) for x, y in product(range(q), repeat=2))
    print('  ok: q<=23: (u,v) counts, X counts (q-1-#roots)/2, cover chart 2:1 with q^3+O(q^2) points,'
          ' signed local points')


def two_adic(k=14):
    print('C. 2-adic recipes mod 2^%d' % k)
    M = 1 << k
    for s_ in range(1, M, 2):
        # necessity: x^2+1 = s y^2 with y unit forces s = 1 mod 4 (mod 4 reduction; y odd since x even)
        if s_ % 4 == 1:
            x = 0 if s_ % 8 == 1 else 2
            assert ((1 + x*x)*pow(s_, -1, M)) % 8 == 1   # (1+x^2)/s square unit
            assert (s_ - x*x) % 8 == 1                    # circle remainder
    for x in range(8):
        for y in range(8):
            for s_ in (3, 7):
                assert (x*x + 1 - s_*y*y) % 4 != 0 or y % 2 == 0
    print('  ok: x in 4Z_2 (s=1 mod 8) / 2+4Z_2 (s=5 mod 8) give (1+x^2)/s = 1 mod 8 and s-x^2 = 1 mod 8;'
          ' s=3 mod 4 has no unit-y negative Pell point')


def fundamental_neg_pell(p):
    """Least positive solution of X^2 - pY^2 = -1 via the continued fraction of sqrt p (None if none)."""
    a0 = isqrt(p)
    m, d, aa = 0, 1, a0
    h0, h1, k0, k1 = 1, a0, 0, 1
    while True:
        if h1*h1 - p*k1*k1 == -1:
            return h1, k1
        if h1*h1 - p*k1*k1 == 1:
            return None
        m = d*aa - m
        d = (p - m*m)//d
        aa = (a0 + m)//d
        h0, h1 = h1, aa*h1 + h0
        k0, k1 = k1, aa*k1 + k0


def two_sq(p):
    for a_ in range(1, isqrt(p) + 1):
        b2 = p - a_*a_
        r = isqrt(b2)
        if r*r == b2:
            return a_, r


def gauss_div(x, y):
    (a1, b1), (a2, b2) = x, y
    n = a2*a2 + b2*b2
    re, im = a1*a2 + b1*b2, b1*a2 - a1*b2
    if re % n or im % n:
        return None
    return re//n, im//n


def ordinary():
    print('D. ordinary primes')
    p = 888721
    ok(isprime(p) and p % 840 == 1 and isqrt(p - 1)**2 != p - 1, '888721 prime, 1 mod 840, p-1 nonsquare')
    u, v, a, b = 4, 3, 264, -905
    Cc, Dd = u*u - v*v, 2*u*v
    ok(a*a + b*b == p and Dd*a + Cc*b == 1, 'row (4,3,264,-905): a^2+b^2=p, Sa+Db=1')
    X, Y = Cc*a - Dd*b, u*u + v*v
    ok((X, Y) == (23568, 25) and X*X + 1 == p*Y*Y, '(X,Y)=(23568,25), X^2+1=pY^2')
    ok(fundamental_neg_pell(p) == (X, Y), '(23568,25) is the least negative-Pell solution at 888721')
    x1, y1, z1 = 222183, 17950790754, 10098403901231006322
    ok(4*x1*y1*z1 == p*(x1*y1 + y1*z1 + z1*x1), 'ES triple at 888721 verified')
    # every prime p=1 mod 4 < 6000: negative Pell exists, least solution = row form with (a,b) a TS witness
    cnt = 0
    for p in range(5, 6000, 4):
        if not isprime(p):
            continue
        sol = fundamental_neg_pell(p)
        assert sol is not None
        X, Y = sol
        assert X % 2 == 0 and Y % 2 == 1
        a_, b_ = two_sq(p)
        found = False
        for pi in ((a_, b_), (a_, -b_), (b_, a_), (b_, -a_), (-a_, b_), (-a_, -b_), (-b_, a_), (-b_, -a_)):
            w = gauss_div((X, 1), pi)
            if w is None:
                continue
            re, im = w
            if re + Y < 0 or (re + Y) % 2:
                continue
            u2, v2 = (Y + re)//2, (Y - re)//2
            uu, vv = isqrt(u2), isqrt(v2)
            if uu*uu == u2 and vv*vv == v2:
                for vs in (vv, -vv):
                    if 2*uu*vs == im:
                        aa, bb = pi
                        assert aa*aa + bb*bb == p and (2*uu*vs)*aa + (uu*uu - vs*vs)*bb == 1
                        found = True
        assert found, p
        cnt += 1
    print(f'  ok: all {cnt} primes p=1 mod 4 below 6000 have negative Pell, and the least solution is'
          ' X+i=(a+ib)(u+iv)^2 with a^2+b^2=p (row form)')


if __name__ == '__main__':
    symbolic()
    finite_fields()
    two_adic()
    ordinary()
    print('All PELLMODELS checks pass.')
