"""R252: from-scratch check of the 7*4^s+9 window m = 19 claim (MENU_STERILITY §4.1): s = 0 (mod 90) covered.
n = 7*4^s + 9 = 112 X^4 + 9 with X = 2^{(s-2)/2}; K = (n+19)/4 = 7(4X^4+1) = 7 f+ f-; d = 7^a f+^b f-^c."""
import sympy as sp
from fractions import Fraction as F
X = sp.symbols('X'); fp = 2*X**2+2*X+1; fm = 2*X**2-2*X+1
n = 112*X**4 + 9; K = sp.expand((n+19)/4); assert sp.expand(K - 7*fp*fm) == 0
MOD = 19*7
good = {}
for a in range(3):
    for b in range(3):
        for c in range(3):
            d = 7**a*fp**b*fm**c
            q, r = sp.div(sp.Poly(sp.expand(n*K*(K+d)), X), sp.Poly(19*d, X))
            if not r.is_zero: continue
            y = sp.Poly(sp.expand(n*(K+d)), X)
            # integrality of z: denominators of q divide MOD (asserted) -> integrality depends on X mod MOD
            den = sp.ilcm(*[sp.fraction(cf)[1] for cf in q.all_coeffs()])
            assert MOD % den == 0 or den == 1, den
            Qz = sp.Poly(sp.expand(q.as_expr()*den), X)
            res = [x0 for x0 in range(MOD) if y.eval(x0) % 19 == 0 and Qz.eval(x0) % den == 0]
            good[(a, b, c)] = set(res)
print({k: sorted(v)[:8] for k, v in good.items() if v})
# s = 0 mod 90 (s >= 90): X = 2^{(s-2)/2} = 2^{44 + 45k}; X mod 133 depends on s mod lcm(2*ord_133(2))
from sympy.ntheory import n_order
o = n_order(2, 133); print("ord_133(2) =", o)
for s in range(90, 90 + 2*o*90 + 1, 90):
    x0 = pow(2, (s-2)//2, MOD)
    hit = [k for k, v in good.items() if x0 in v]
    if not hit: print("s =", s, "NOT covered, X mod 133 =", x0)
# exact check for a few s
for s in (90, 180, 270, 360, 450):
    Xv = 2**((s-2)//2); nv = 7*4**s+9; Kv = (nv+19)//4
    for (a,b,c),v in good.items():
        if Xv % MOD in v:
            fpv, fmv = 2*Xv*Xv+2*Xv+1, 2*Xv*Xv-2*Xv+1; d = 7**a*fpv**b*fmv**c
            y = F(nv*(Kv+d), 19); z = F(nv*Kv*(Kv+d), 19*d)
            assert y.denominator == 1 and z.denominator == 1 and F(4, nv) == F(1, Kv)+1/y+1/z
            print("s =", s, "ok with", (a,b,c)); break
