"""pd_k1.py — the k = 1 slice of the cap ladder (PHASE_DIAGRAM.md §3).
k = 1 shots: g | 4n + Q1^2, g ≡ 3 (mod 4), Q0 = (g+1)/4, Q = Q0*Q1, overflow exactly Q1 (EXPONENT_CAP Prop 1.3).
Mute rungs: ES^{(y,e)}: g ≡ -1 (mod 4 rad Q1) and v_l(Q1) <= e;  ES^[2]: g ≡ -1 (mod 4 Q1).
For each n in the list and odd Q1 <= QMAX, gcd(Q1, n) = 1, count shots per rung, verify each exactly, and report
counts per dyadic Q1-range for the e = 2 rung restricted to non-squarefree Q1 (the part beyond ES^{(y,1)}).
Usage: pd_k1.py QMAX n1 n2 ...
"""
import sys
from fractions import Fraction
from math import gcd
from sympy import factorint, divisors

QMAX = int(sys.argv[1]); ns = list(map(int, sys.argv[2:]))
for n in ns:
    e1 = []; e2 = {}; maxQ2 = 0
    for Q1 in range(1, QMAX + 1, 2):
        if gcd(Q1, n) != 1:
            continue
        f = factorint(Q1); R = 1
        for l in f: R *= l
        emax = max(f.values()) if f else 0
        if emax > 2:
            continue
        for g in divisors(4 * n + Q1 * Q1):
            if (g + 1) % (4 * R):
                continue
            Q0 = (g + 1) // 4; Q = Q0 * Q1
            if gcd(Q, n) != 1:
                continue
            m = (n + 4 * Q * Q) // g; assert (n + 4 * Q * Q) % g == 0 and (n + m) % 4 == 0
            x = (n + m) // 4; y = n * (g + 1) // 4; z = Fraction(n * x * (g + 1), 4 * Q * Q)
            assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
            assert z.denominator == Q1 * Q1 and (y % R == 0)
            if emax <= 1:
                assert (g + 1) % (4 * Q1) == 0
                e1.append((Q1, g))
            else:
                b = Q1.bit_length(); e2[b] = e2.get(b, 0) + 1; maxQ2 = max(maxQ2, Q1)
    W = (16 * n + 1) / 3
    print(f"n={n}: e<=1 (=ES^[2] sqfree) k=1 shots: {len(e1)}, max Q1 {max([q for q,_ in e1], default=0)} (wall {W:.1f});"
          f" e=2 non-sqfree shots by bit-length of Q1: {dict(sorted(e2.items()))}, max Q1 {maxQ2}")
