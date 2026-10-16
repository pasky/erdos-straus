# review_r258_misc.py — R258 from-scratch checks: Prop 2.1 (3*2^s+1 cubic family), Reduction 2.5 algebra at (63,1),
# Prop 4.1 arithmetic facts for 4^s + 297.
from fractions import Fraction as F
# Prop 2.1
ok = []
for s in range(0, 400, 3):
    Y = 2 ** (s // 3); n = 3 * Y ** 3 + 1; a, c = 80, 1
    d = F(21 * Y + 64, 320); b = F(Y * Y - 3 * Y + 9, 7)
    if d.denominator == 1 and b.denominator == 1 and d > 0 and b > 0:
        x, y, z = a * b * d, a * c * d * n, b * c * d * n
        assert F(4, n) == 1 / x + 1 / y + 1 / z
        ok.append(s)
print('Prop 2.1 family valid (s<400, 3|s) at s mod 36 =', sorted({s % 36 for s in ok}), 'min s', min(ok))
print('  Y^2-3Y+9 mod 7 for Y=1,2,4:', [(Y * Y - 3 * Y + 9) % 7 for Y in (1, 2, 4)])
# Reduction 2.5, (63,1): z = 2^E a1 = 20 -> c0(u^3 - z) = (1+z)^2
print('Red 2.5 (63,1):', 63 * (27 - 20) == 21 ** 2, (1 + 1700) % 63 == 0, (1 + 1700) // 63)
# Prop 4.1: n = 4^s+297, s=3 -> 361; ord_19(4)
o = 1; t = 4
while t != 1: t = t * 4 % 19; o += 1
print('4^3+297 =', 64 + 297, ' ord_19(4) =', o)
# windows m = 3 mod 4 with 19 | m exist: gcd(N(1), m) = gcd(361, m) can be > 1
print('m = 3 mod 4 with 19|m (first few):', [m for m in range(3, 400, 4) if m % 19 == 0])
