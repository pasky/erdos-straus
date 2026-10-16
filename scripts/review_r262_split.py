"""R262 from-scratch: for each empty-M prime, least ET d with a Type II solution and least d with a solution
having a split slice (-p a square mod g or mod D).

Parametrisation (ET Prop 2.6, re-derived in the review): (x, y, z) = (abd, acdp, bcdp), 4abcd = a + b + cp.
Then g := 4acd - 1 divides n := p + 4a^2 d, g = -1 (mod 4ad), and conversely each such (a, d, g) gives
c = (g+1)/(4ad), m = n/g, b = (p + m)/(4ad) (integral since 4ad | p + m).  Bound: (4ad-1)(4bd-1) <= 4dp + 1, so
WLOG a = min(a, b) <= (1 + sqrt(4dp+1))/(4d), and then n <= 2p + O(1): one SPF sieve to 2N + 10 suffices.
Every solution found is checked as an exact Egyptian-fraction identity.
usage: review_r262_split.py N DMAX   (empty primes recomputed by review_r262_meet's method A)
"""
import sys
import math
from fractions import Fraction
from sympy import factorint
from review_r262_meet import spf_sieve, factor, divs_from, meet_nonempty


def neg_p_square_mod(p, g, spf):
    f = factor(g, spf) if g < len(spf) else factorint(g)
    for l, e in f.items():
        if l == p:
            return False  # slice not coprime to p: no slice lattice (never happened; flagged below)
        if pow((-p) % l, (l - 1) // 2, l) != 1:
            return False  # odd prime l not dividing p: square mod l^e iff square mod l
    return True


def sols_d(p, d, spf):
    A = int((1 + math.sqrt(4 * d * p + 1)) / (4 * d)) + 1
    for a in range(1, A + 1):
        n = p + 4 * a * a * d
        for g in divs_from(factor(n, spf)):
            if g % (4 * a * d) != 4 * a * d - 1:
                continue
            c = (g + 1) // (4 * a * d)
            m = n // g
            assert (p + m) % (4 * a * d) == 0
            b = (p + m) // (4 * a * d)
            x, y, z = a * b * d, a * c * d * p, b * c * d * p
            assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p) and x % p
            D = 4 * b * c * d - 1
            assert math.gcd(g, p) == 1 and math.gcd(D, p) == 1
            yield (a, b, c, d), neg_p_square_mod(p, g, spf) or neg_p_square_mod(p, D, spf)


if __name__ == "__main__":
    N, DMAX = int(sys.argv[1]), int(sys.argv[2])
    spf = spf_sieve(2 * N + 10)
    empt = [p for p in range(5, N + 1, 4) if spf[p] == p and not meet_nonempty(p, spf)]
    hist_any, hist_split, invisible = {}, {}, []
    for p in empt:
        dany = dsplit = None
        for d in range(1, DMAX + 1):
            for rep, vis in sols_d(p, d, spf):
                if dany is None:
                    dany = d
                if vis:
                    dsplit = d
                    break
            if dsplit is not None:
                break
        assert dany != 1
        hist_any[dany] = hist_any.get(dany, 0) + 1
        hist_split[dsplit] = hist_split.get(dsplit, 0) + 1
        if dsplit is None:
            invisible.append(p)
        if dsplit is None or dsplit > 2 or (dany or 0) > 2:
            print(p, "least d any:", dany, " least d split:", dsplit, flush=True)
    print("#empty", len(empt), "least-d(any) hist", hist_any, " least-d(split) hist", hist_split)
    print("no split-slice solution with d <=", DMAX, ":", invisible)
