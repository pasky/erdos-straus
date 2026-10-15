# R246: rebuild each JSON class from its parameters via Elsholtz–Tao Prop 1.9 (Type II, 2nd family:
# n = -4a^2 d (mod f), 4ad | f+1; sextuple (a, c(n+4a^2d)/f - a, c=(f+1)/(4ad), d, e=(n+4a^2d)/f, f),
# (x,y,z) = (abd, nacd, nbcd)) and 'D' classes (M | n: scale an ES solution of 4/M); compare with JSON.
import json
import sympy as sp
n = sp.Symbol('n')
C = json.load(open('data/s6_cert105_et.json'))
for cl in C['classes']:
    M, r, fam, P = cl['M'], cl['r'], cl['fam'], cl['params']
    X = [sum(sp.Rational(c)*n**j for j, c in enumerate(p)) for p in cl['xyz']]
    if fam == 'II2':
        a, d, f = P
        assert f == M and (f + 1) % (4*a*d) == 0 and (-4*a*a*d - r) % f == 0, cl
        c = sp.Rational(f + 1, 4*a*d); e = (n + 4*a*a*d)/f; b = c*e - a
        # constraints of Sigma^II used: 4abd = n + e?  check the ES relation directly
        Y = [sp.expand(a*b*d), sp.expand(n*a*c*d), sp.expand(n*b*c*d)]
        assert sp.simplify(4/n - sum(1/y for y in Y)) == 0
        assert sorted(map(str, Y)) == sorted(map(str, [sp.expand(x) for x in X])), (cl, Y, X)
        print(f"II2 M={M} r={r} (a,d,f)={P}: matches ET Prop 1.9 Type II family 2")
    else:
        assert P == [M] and r == 0
        q = [sp.expand(x/n) for x in X]   # constants
        assert all(v.is_Rational for v in q) and sum(1/v for v in q) == 4 and all((M*v).is_integer for v in q)
        print(f"D   M={M}: n = M m, x,y,z = m*{[M*v for v in q]}")
