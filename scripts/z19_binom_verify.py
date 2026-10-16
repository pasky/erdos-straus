# z19_binom_verify.py — independent numeric replay of a z19_binom.py hit: build (a,b,c,d) as functions of Y = 2^{s/D},
# check the ES identity 4/n = 1/x+1/y+1/z with x,y,z positive integers at every s = D*j (j <= JMAX) where all
# parameters are integers, and report the set of such j modulo a period (should contain j = 0 mod P for large j).
# Usage: z19_binom_verify.py c0 k MENU p1 p2 D "P(Y)" kappa [JMAX]
import sys
from fractions import Fraction as Fr
from sympy import sympify, symbols, Poly
c0, k = int(sys.argv[1]), int(sys.argv[2]); MENU = sys.argv[3]; p1, p2, D = map(int, sys.argv[4:7])
Ys = symbols('Y'); P = Poly(sympify(sys.argv[7]), Ys); kap = Fr(sys.argv[8]); JMAX = int(sys.argv[9]) if len(sys.argv) > 9 else 240
good = []
for j in range(1, JMAX + 1):
    Y = 2 ** j; s = D * j; n = c0 * 2 ** s + k
    f = kap * int(P.eval(Y))
    if MENU == 'II-ac':
        a, c = p1, p2; B = c * n + a; d = (f + 1) / (4 * a * c); b = Fr(B) / f
    elif MENU == 'II-ad':
        a, d = p1, p2; B = n + 4 * a * a * d; b = (f + n) / (4 * a * d); c = (Fr(B) / f + 1) / (4 * a * d)
    elif MENU == 'I-ac':
        a, c = p1, p2; B = a * n + c; d = (f + n) / (4 * a * c); b = Fr(B) / f
    vals = [Fr(t) for t in (a, b, c, d)]
    if all(t.denominator == 1 and t > 0 for t in vals):
        a, b, c, d = [int(t) for t in vals]
        x, y, z = (a * b * d, a * c * d, b * c * d) if MENU == 'I-ac' else (a * b * d, a * c * d * n, b * c * d * n)
        if MENU == 'I-ac': x *= n
        assert Fr(4, n) == Fr(1, x) + Fr(1, y) + Fr(1, z), (j, 'IDENTITY FAILS')
        good.append(j)
print('%s c0=%d k=%d params=(%d,%d) D=%d P=%s kappa=%s: integral & verified at %d of %d j; first: %s'
      % (MENU, c0, k, p1, p2, D, P.as_expr(), kap, len(good), JMAX, good[:12]))
