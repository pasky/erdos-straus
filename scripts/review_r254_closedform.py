# review_r254_closedform.py -- R254: closed forms of the mu=0 Sophie-Germain window leaves, derived by hand:
#  n = c0*4^s + k, s even, b = 2^{(s-2)/2}, A+- = 2b^2 +- 2b + 1 (A+ A- = 4b^4 + 1 = 4^{s-1} + 1), m = 4c0 - k (j=1, t=1),
#  x = (n+m)/4 = c0 A+ A-, N = n x; relation d1 = c0, d2 = A+ (m | c0 + A+ on the leaf cylinder):
#  y = N (c0 + A+)/(m A+) = c0 n A- (c0+A+)/m,  z = N (c0+A+)/(m c0) = n A+ A- (c0+A+)/m.
import sympy as sp
from fractions import Fraction as Fr
from sympy import n_order
b = sp.Symbol('b', positive=True)
for (c0, k, P) in ((3, 1, None), (7, 9, None)):
    m = 4 * c0 - k
    n = c0 * 4 * (4 * b**4) + k          # 4^s = 4 * 4^{s-1} = 4*(4 b^4)
    Ap, Am = 2*b*b + 2*b + 1, 2*b*b - 2*b + 1
    assert sp.expand(Ap * Am - (4 * b**4 + 1)) == 0
    x = c0 * Ap * Am
    assert sp.expand(4 * x - n - m) == 0
    y = c0 * n * Am * (c0 + Ap) / m; z = n * Ap * Am * (c0 + Ap) / m
    assert sp.simplify(1/x + 1/y + 1/z - 4/n) == 0
    # S-integer limit at mu=0: b -> 1/2 : c0 + A+ = c0 + 5/2 = m/2 ?
    print((c0, k), 'm', m, 'c0 + A+(1/2) =', c0 + Fr(5, 2), ' m/2 =', Fr(m, 2))
    # which s (even) have m | c0 + A+(b) and m | c0 + A-(b)?  period 2*ord_m(2) in s
    per = 2 * n_order(2, m)
    good_p = [s for s in range(2, 2 + per, 2) if (c0 + 2*pow(2, s-2, m) + 2*pow(2, (s-2)//2, m) + 1) % m == 0]
    good_m = [s for s in range(2, 2 + per, 2) if (c0 + 2*pow(2, s-2, m) - 2*pow(2, (s-2)//2, m) + 1) % m == 0]
    print('  period', per, ' m | c0+A+ at s mod per in', [s % per for s in good_p], '; m | c0+A- at', [s % per for s in good_m])
    for s in range(2, 400, 2):
        if s % per in [g % per for g in good_p]:
            B = 2 ** ((s - 2) // 2); N_ = c0 * 4**s + k; ap, am = 2*B*B+2*B+1, 2*B*B-2*B+1
            X, Y, Z = c0*ap*am, c0*N_*am*(c0+ap), N_*ap*am*(c0+ap)
            assert Y % m == 0 and Z % m == 0; Y //= m; Z //= m
            assert 4 * X * Y * Z == N_ * (X*Y + Y*Z + Z*X)
print('closed forms OK')
