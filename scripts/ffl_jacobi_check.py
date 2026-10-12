"""Check (FUNCTIONFIELD_ES.md §4): for every Type II datum (a,b,c,d) of P (P = A a b d - E, E c = a + b, gcd(a,b)=1),
with f := A a c d - 1, the Jacobi symbol (P/f) equals (-1)^{((q-1)/2)((1+deg f)(1+deg Ad)-1)}.
usage: ffl_jacobi_check.py p A(high->low digits) n   (p prime, small)"""
import sys, itertools
from sympy import Poly, GF, symbols, factor_list
T = symbols('T')
p = int(sys.argv[1]); n = int(sys.argv[3])
A = Poly([int(c) for c in sys.argv[2]], T, modulus=p); k = A.degree()
def monics(d):
    for low in itertools.product(range(p), repeat=d):
        yield Poly([1] + list(low), T, modulus=p)
def legendre_irr(g, l):  # (g / l), l monic irreducible
    r = g.rem(l)
    if r.is_zero: return 0
    e = (p ** l.degree() - 1) // 2
    v = pow_mod(r, e, l)
    return 1 if v == Poly(1, T, modulus=p) else -1
def pow_mod(b, e, m):
    res = Poly(1, T, modulus=p); b = b.rem(m)
    while e:
        if e & 1: res = (res * b).rem(m)
        b = (b * b).rem(m); e >>= 1
    return res
def jacobi(g, f):
    s = 1
    for l, mult in f.factor_list()[1]:
        s *= legendre_irr(g, l.monic()) ** mult
    return s
cnt = bad = 0
for sa in range(0, n - k + 1):
    for sb in range(0, n - k - sa + 1):
        for a in monics(sa):
            for b in monics(sb):
                if a.gcd(b).degree() > 0: continue
                S = a + b
                if S.is_zero: continue
                Sm = S.monic()
                for c in divisors(Sm) if False else []: pass
                # monic divisors of S
                fl = Sm.factor_list()[1]
                divs = [Poly(1, T, modulus=p)]
                for l, m in fl:
                    divs = [dv * l.monic() ** e for dv in divs for e in range(m + 1)]
                for c in divs:
                    E = S.quo(c)
                    for d in monics(n - k - sa - sb):
                        P = A * a * b * d - E
                        if P.degree() != n or not P.is_irreducible: continue
                        f = A * a * c * d - Poly(1, T, modulus=p)
                        if f.degree() < 1: continue
                        pred = (-1) ** (((p - 1) // 2) * ((1 + f.degree()) * (1 + (A * d).degree()) - 1) % 2)
                        cnt += 1; bad += jacobi(P, f.monic()) != pred
print(f"p={p} A={sys.argv[2]} n={n}: {cnt} Type II data on irreducible P (deg f >= 1), mismatches {bad}")
