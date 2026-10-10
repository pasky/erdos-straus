"""R124 from-scratch check of POINTWISE_TERNARY §8 (Step 4 EVIDENCE); does not reuse scripts/tern_qd.py.

For Mordell-hard primes p (p mod 840 in {1,121,169,289,361,529}) find a_min(p) = least a such that for some d <= DMAX
there is f | p + 4a^2 d with f = -1 mod 4ad and b = c*e - a >= 1 (c = (f+1)/(4ad), e = (p+4a^2 d)/f).
Every hit is verified as an actual ES solution 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp) (ET (2.22)) in exact arithmetic.
usage: review_tern_qd.py N DMAX AMAX [stride]   (stride>1 = sample every stride-th hard prime)
"""
import sys
from fractions import Fraction
from sympy import primerange, divisors

HARD = {1, 121, 169, 289, 361, 529}

def amin(p, DMAX, AMAX):
    for A in range(1, AMAX + 1):
        for D in range(1, DMAX + 1):
            m = p + 4*A*A*D
            mod = 4*A*D
            for F in divisors(m):
                if (F + 1) % mod:
                    continue
                Cc = (F + 1)//mod; E = m//F; B = Cc*E - A
                if B < 1:
                    continue
                x, y, z = A*B*D, A*Cc*D*p, B*Cc*D*p
                assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z), (p, A, B, Cc, D)
                return A, D
    return None, None

if __name__ == '__main__':
    N, DMAX, AMAX = map(int, sys.argv[1:4]); stride = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    hist = {}; worst = (0, None); cnt = 0; fails = []
    for i, p in enumerate(x for x in primerange(2, N + 1) if x % 840 in HARD):
        if i % stride:
            continue
        cnt += 1
        A, D = amin(p, DMAX, AMAX)
        if A is None:
            fails.append(p); continue
        hist[A] = hist.get(A, 0) + 1
        if A > worst[0]:
            worst = (A, p)
    print('N', N, 'DMAX', DMAX, 'AMAX', AMAX, 'stride', stride, 'primes', cnt)
    print('hist', dict(sorted(hist.items())), 'worst', worst, 'fails', fails[:20], len(fails))
