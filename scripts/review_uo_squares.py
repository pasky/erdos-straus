"""R186: from-scratch box search for ES^(S)(n), S = {3,5,7,11}, at n = 13^2, 17^2, 19^2 (and controls).
Enumerate integer x <= Bx*n, x <= y <= By*n; t = 4/n - 1/x - 1/y = Q^2/Z must have reduced numerator in <S>^2
(the parity-normalised third term). Classify the shape at the prime l of n (Type I: one var with v_l >= v_l(n),
two l-units; Type II: one l-unit, two with v_l >= v_l(n)); compute inv_v of alpha = (-x/z, -y/z) at inf, 2, q in S, l.
With --noparity: the third term is any element of Z[1/S] (numerator in <S>, no parity), the control.
usage: review_uo_squares.py Bx By n... [--noparity]
"""
import sys
import numpy as np
from fractions import Fraction
from review_uo_common import *

S = [3, 5, 7, 11]
args = [a for a in sys.argv[1:] if not a.startswith("--")]
noparity = "--noparity" in sys.argv
Bx, By = int(args[0]), int(args[1])
ns = [int(a) for a in args[2:]]


def in_monoid(m, parity):
    for q in S:
        k = 0
        while m % q == 0:
            m //= q
            k += 1
        if parity and k % 2:
            return False
    return m == 1


for n in ns:
    l = [p for p in primes_upto(n) if n % p == 0]
    assert len(l) == 1
    l = l[0]
    s = vp(n, l)
    sols = []
    ys = np.arange(1, By * n + 1, dtype=np.int64)
    for x in range(n // 4 + 1, Bx * n + 1):
        A, B = 4 * x - n, n * x  # 4/n - 1/x = A/B
        if A <= 0:
            continue
        yy = ys[ys >= x]
        num = A * yy - B
        den = B * yy
        ok = num > 0
        yy, num, den = yy[ok], num[ok], den[ok]
        g = np.gcd(num, den)
        num //= g
        # numerator must be in <S> (cheap filter): strip S
        m = num.copy()
        for q in S:
            for _ in range(40):
                d = (m % q == 0)
                if not d.any():
                    break
                m[d] //= q
        for y in yy[m == 1]:
            t = Fraction(4, n) - Fraction(1, x) - Fraction(1, int(y))
            if in_monoid(t.numerator, not noparity):
                sols.append((x, int(y), 1 / t))
    shapes = {"I": 0, "II": 0, "other": 0}
    invstats = {}
    for x, y, z in sols:
        if not noparity:
            check_ESS(n, x, y, z, S)
        vs = [vp(Fraction(x), l), vp(Fraction(y), l), vp(z, l)]
        units = sum(1 for v in vs if v == 0)
        big = sum(1 for v in vs if v >= s)
        sh = "I" if (units == 2 and big == 1) else "II" if (units == 1 and big == 2) else "other"
        shapes[sh] += 1
        a1, a2 = -Fraction(x) / z, -Fraction(y) / z
        key = (inv(a1, a2, 0), inv(a1, a2, 2), tuple(inv(a1, a2, q) for q in S), inv(a1, a2, l), sh)
        tot = key[0] + key[1] + sum(key[2]) + key[3]
        assert tot % 2 == 0, "product formula"
        invstats[key] = invstats.get(key, 0) + 1
    print(f"n={n} ({'no parity' if noparity else 'ES^(S)'}), box x<={Bx}n, y<={By}n: {len(sols)} solutions, shapes {shapes}")
    for k, v in sorted(invstats.items(), key=lambda kv: -kv[1])[:8]:
        print("   (inf,2,S,l,shape)", k, v)
