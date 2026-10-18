"""R271 from-scratch fixture scores (HARD_PAIR §2.3 raw columns N1, fII, m0, e0, LI) by brute force.
Type II: all (a, b, c, d) >= 1 with c(4abd - p) = a + b (ET form 4abcd = a + b + pc), ordered in (a, b).
Type I level e = 3 (4): exists x <= y with e/H = 1/x + 1/y, H = (pe + 1)/4 (ES solution containing pH)."""
import sys
from math import gcd

def typeII(p):
    sols = []
    for a in range(1, (p + 1) // 3 + 1):  # a(4b - 1) <= p + b forces a <= (p + 1)/3
        b = 1
        while 4 * a * b <= p + a + b:
            dlo = p // (4 * a * b) + 1
            d = dlo
            while 4 * a * b * d - p <= a + b:
                g = 4 * a * b * d - p
                if (a + b) % g == 0:
                    sols.append((a, b, (a + b) // g, d))
                d += 1
            b += 1
    return sols

def level_ok(p, e):
    H = (p * e + 1) // 4
    for x in range(H // e + 1, 2 * H // e + 1):
        num = e * x - H
        if num > 0 and (x * H) % num == 0:
            return True
    return False

for p in map(int, sys.argv[1:]):
    S = typeII(p)
    for (a, b, c, d) in S:
        assert 4 * a * b * c * d == a + b + p * c
    N1 = sum(1 for s in S if s[1] == 1)
    f_all = len(S)
    f_ac = sum(1 for (a, b, c, d) in S if gcd(a, c) == 1)
    f_astra = sum(1 for (a, b, c, d) in S if gcd(gcd(a, b), c) == 1 and gcd(a * b * d, p) == 1)
    m0 = min(((a + b) // c for (a, b, c, d) in S), default=None)
    levels = [e for e in range(3, 200, 4) if level_ok(p, e)]
    print(p, 'N1', N1, 'fII(all/gcd(a,c)=1/Astra-norm)', f_all, f_ac, f_astra, 'm0', m0,
          'e0', levels[0] if levels else None, 'LI', len(levels),
          'a<=b tuples' if p < 300 else '', sorted(s for s in S if s[0] <= s[1]) if p < 300 else '')
