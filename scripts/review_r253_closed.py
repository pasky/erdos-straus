# review_r253_closed.py — R253: check the closed-form window identities (EXP_105 §2) exactly, from scratch.
# (a) Thm 2.2 window: n = 3*4^s+1, s even, b = 2^{(s-2)/2}, A± = 2b^2±2b+1, x = 3A+A-, y = nx(nA±+1)/11, z = 3A∓(nA±+1)/11.
# (b) Sophie-Germain: 4X^4+1 = (2X^2+2X+1)(2X^2-2X+1).
# (c) 7*4^s+9, m = 19 window at mu = 0 (j=1, t=1): x = 7(4^{s-1}+1), analogous closed form, which s mod lcm fire.
from sympy import symbols, expand
from fractions import Fraction as Fr
X = symbols('X')
assert expand((2*X**2+2*X+1)*(2*X**2-2*X+1) - (4*X**4+1)) == 0

def fire_table(c0, k, m):
    """for n = c0 4^s + k, j = 1, t = 1, s even (r = s-1 odd), b = 2^{(s-2)/2}: residues s mod 2*ord_m(2) where
    m | n*A + c0' relation of the form c0*A± ... we just test all d1,d2 among {c0,n,A+,A-} products, return dict."""
    out = {}
    for s in range(2, 2 + 2 * 60 * m, 2):
        if len(out) >= 1 and s > 4 * 60 * 2: break
    return out

ok = 0
fires = set()
for s in range(2, 1502, 2):
    b = 2 ** ((s - 2) // 2); Ap, Am = 2*b*b+2*b+1, 2*b*b-2*b+1
    n = 3 * 4 ** s + 1; x = 3 * Ap * Am
    assert Ap * Am == 4 ** (s - 1) + 1 and 4 * x - n == 11
    for (A, B, tag) in ((Ap, Am, '+'), (Am, Ap, '-')):
        if (n * A + 1) % 11 == 0:
            y = n * x * (n * A + 1) // 11; z = 3 * B * (n * A + 1) // 11
            assert Fr(4, n) == Fr(1, x) + Fr(1, y) + Fr(1, z); ok += 1
            fires.add((s % 20, tag))
print('(a) closed form verified at', ok, 'even s<=1500; firing (s mod 20, sign):', sorted(fires))
# which even residues mod 20 fire with neither sign
print('   even s mod 20 with no closed-form firing:', sorted(set(range(0, 20, 2)) - {f[0] for f in fires}))
# (c) 7*4^s+9 with m=19: x = 7(4^{s-1}+1) = 7 A+ A-; candidate y = n x (nA+ + c)/19 type relations: search d1,d2 in
# products of {7, n, A+, A-} with 19 | d1 + d2, record s mod 36 (period 2*ord_19(2) = 36).
from itertools import product
rows = {}
for s in range(2, 2 + 36 * 4, 2):
    b = 2 ** ((s - 2) // 2); Ap, Am = 2*b*b+2*b+1, 2*b*b-2*b+1
    n = 7 * 4 ** s + 9; x = 7 * Ap * Am; assert 4 * x - n == 19
    pcs = [7, n, Ap, Am]; got = []
    for eps in product((0, 1, -1), repeat=4):
        d1 = 1; d2 = 1
        for p, e in zip(pcs, eps):
            if e == 1: d1 *= p
            if e == -1: d2 *= p
        if (d1 + d2) % 19 == 0 and eps.count(1) and eps.count(-1): got.append(eps)
    rows.setdefault(s % 36, set()).add(bool(got))
print('(c) 7*4^s+9, m=19, pieces {7,n,A+,A-} w/o 2-powers: s mod 36 -> fires?', sorted(rows.items()))
