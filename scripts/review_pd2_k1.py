"""R210 from-scratch check of PHASE_DIAGRAM §3 k = 1 evidence.

(A) For given n and Q1 <= QMAX odd, gcd(Q1, n) = 1: divisors g = 3 (mod 4) of 4n + Q1^2, Q0 = (g+1)/4,
    gcd(Q0, n) = 1, exponent cap e(Q1) = max v_l(Q1), ES^{(y,e)} membership: rad Q1 | Q0.
    Verify the exact solution (den z = Q1^2, rad Q1 | y) and report e<=1 counts / max, e = 2 bit-lengths.
(B) For primes 5 <= p < PMAX: least a <= AMAX with a divisor g of 4p + 9^a, g = 3 (mod 4), and 3 | (g+1)/4 if
    a >= 1; ALSO report whether the shot convention gcd((g+1)/4, p) = 1 can be met.
Usage: review_pd2_k1.py A QMAX n1 n2 ...   |   review_pd2_k1.py B PMAX AMAX
"""
import sys
from fractions import Fraction as F
from math import gcd
from sympy import factorint, primerange


def divs(fac):
    ds = [1]
    for p, e in fac.items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return ds


def sol(n, Q, g):
    x = F(n * (g + 1) + 4 * Q * Q, 4 * g)
    y = n * (g + 1) // 4
    z = x * y / (Q * Q)
    assert x.denominator == 1 and F(4, n) == 1 / x + F(1, y) + 1 / z
    return z.denominator, y


def partA(QMAX, ns):
    for n in ns:
        e1 = []
        e2 = []
        for Q1 in range(1, QMAX + 1, 2):
            if gcd(Q1, n) != 1:
                continue
            fq = factorint(Q1)
            rad = 1
            for p in fq:
                rad *= p
            e = max(fq.values(), default=0)
            if e > 2:
                continue
            N = 4 * n + Q1 * Q1
            for g in divs(factorint(N)):
                if g % 4 != 3 or (g + 1) % (4 * rad):
                    continue
                Q0 = (g + 1) // 4
                if gcd(Q0, n) != 1:
                    continue
                dz, y = sol(n, Q0 * Q1, g)
                assert dz == Q1 * Q1 and y % rad == 0
                (e1 if e <= 1 else e2).append(Q1)
        bits = sorted({q.bit_length() for q in e2})
        W = F(16 * n + 1, 3)
        print(f"n={n}: e<=1 shots {len(e1)} max {max(e1, default=None)} (W={float(W):.1f}); "
              f"e=2 non-sqf shots {len(e2)} max {max(e2, default=None)} bits {bits}")


def partB(PMAX, AMAX):
    hist = {}
    conv_fail = []
    for p in primerange(5, PMAX):
        found = None
        for a in range(0, AMAX + 1):
            N = 4 * p + 9 ** a
            good = [g for g in divs(factorint(N)) if g % 4 == 3 and (a == 0 or (g + 1) % 12 == 0)]
            if good:
                ok = [g for g in good if ((g + 1) // 4) % p != 0]
                if not ok:
                    conv_fail.append((p, a))
                    continue
                g = ok[0]
                dz, y = sol(p, ((g + 1) // 4) * 3 ** a, g)
                assert dz == 9 ** a and (a == 0 or y % 3 == 0)
                found = a
                break
        hist[found] = hist.get(found, 0) + 1
    print("least-a histogram:", dict(sorted(hist.items(), key=lambda t: (t[0] is None, t[0] or 0))))
    print("cases where only convention-violating g existed at some a:", conv_fail[:20], len(conv_fail))


if __name__ == "__main__":
    if sys.argv[1] == "A":
        partA(int(sys.argv[2]), [int(t) for t in sys.argv[3:]])
    else:
        partB(int(sys.argv[2]), int(sys.argv[3]))
