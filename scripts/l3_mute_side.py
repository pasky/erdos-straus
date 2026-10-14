#!/usr/bin/env python3
"""O206 §6: pentagons with frozen sides (Q^2,1,1,1,n) and middle diagonal 4 <-> divisors h = 3 (4) of 4n + Q^2 (Q odd),
giving 4/n = 1/(sn) + 1/(sc) + Q^2/(cn).  Checks Ptolemy + identity in exact rationals, n odd <= NMAX, Q odd <= QMAX."""
import sys
from fractions import Fraction as F
from math import gcd
NMAX = int(sys.argv[1]); QMAX = int(sys.argv[2])
bad = tot = 0
for n in range(3, NMAX + 1, 2):
    for Q in range(1, QMAX + 1, 2):
        M = 4 * n + Q * Q
        for h in range(3, M + 1, 4):
            if M % h:
                continue
            c = (h + Q * Q) // 4; assert 4 * c == h + Q * Q
            if (n + c) % h:
                bad += 1; continue
            s = (n + c) // h; m = 4; hp = m * s - 1; tot += 1
            lam = {(1,2): Q*Q, (2,3): 1, (3,4): 1, (4,5): 1, (1,5): n, (1,3): c, (2,4): m, (3,5): s, (1,4): h, (2,5): hp}
            L = lambda i, k: lam[(min(i,k), max(i,k))]
            ok = all(L(a,c_)*L(b,d) == L(a,b)*L(c_,d) + L(a,d)*L(b,c_)
                     for (a,b,c_,d) in [(1,2,3,4),(2,3,4,5),(1,2,3,5),(1,3,4,5),(1,2,4,5)])
            ok &= F(4, n) == F(1, s*n) + F(1, s*c) + F(Q*Q, c*n)
            bad += (not ok)
print('mute-side pentagons', tot, 'failures', bad)
sys.exit(1 if bad else 0)
