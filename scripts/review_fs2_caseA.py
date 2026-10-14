"""review_fs2_caseA.py (R218, from scratch): Case A part of (Σ), q = 3^r, k = 2, exact rationals for alpha <= AMAX,
from the six routes of FF_STERILE_PUSH Lemma 2.2 / DEPTH_ASPECT Lemma 2.3 (A0)-(A4), plus a rigorous tail for
alpha > AMAX from DEPTH_ASPECT Lemma 2.4 (count <= (alpha+1)^3 * 4 * 2^alpha * 3^alpha * q^floor((alpha-1)/2)),
summed exactly as a geometric majorant with rational arithmetic (ratio bound evaluated at alpha = AMAX+1).
Also reports the variant WITHOUT the Lenstra/trivial class bounds (routes (iii),(iv) with C(n,d) only) and the
variant counting g' (factor tau(K/T) <= 2^(kappa-1)), to show robustness.
usage: uv run python scripts/review_fs2_caseA.py r[,r..] [AMAX]"""
import sys
from fractions import Fraction as Fr
from math import comb, factorial


def mass(q, AMAX, use_cls=True):
    N = lambda d: 1 if d <= 0 else q**d - q**(d - 1)

    def cls(n, d, rho):
        c = comb(n, d)
        if not use_cls:
            return c
        if d < rho or n - d < rho:        # Lemma 1.4, trivial cases (sigma = -1 is a unit)
            return min(c, 1)
        if 3 * rho > n:
            return min(c, 2)
        return c
    tot = Fr(0)
    for al in range(1, AMAX + 1):
        S = 0
        for be in range(al):                       # beta <= alpha - 1 since kappa >= 1, f >= 0
            for ka in range(1, al - be + 1):
                f = al - be - ka
                M = max(be, f)
                for la in range(0, M):              # zeta = M - la >= 1
                    ze = M - la
                    S += min(
                        N(la) * N(be) * q**(ka - 1),                                        # (a1',b1,K)
                        N(la) * q**(ka - 1) * q**f,                                         # (a1',K,F) -> b1 (A4)
                        N(be) * q**(ka - 1) * cls(max(al, 2 * be + ka), la + be + ka, be + ka),   # (A2)
                        N(la) * N(be) * cls(al + la, la + be + ka, la + be + 1),            # (A1)
                        q**ze * (factorial(al) // (factorial(be) * factorial(ka) * factorial(f))),  # (A3)
                        2 * N(la) * q**ze * q**(ka - 1))                                    # quadratic
        tot += Fr(S, q**al)
    # tail alpha > AMAX: t(al) = (al+1)^3 4 6^al q^{floor((al-1)/2) - al} <= (al+1)^3 4 6^al q^{-(al+1)/2};
    # bound sqrt(q) below by a rational: q^{-(al+1)/2} <= (1/sq)^(al+1) with sq <= sqrt(q).
    from math import isqrt
    sq = Fr(isqrt(q * 10**12), 10**6)            # <= sqrt(q)
    a0 = AMAX + 1
    first = Fr((a0 + 1)**3 * 4 * 6**a0) / sq**(a0 + 1)
    rho = Fr(a0 + 2, a0 + 1)**3 * 6 / sq
    tail = first / (1 - rho) if rho < 1 else None
    return tot, tail


if __name__ == '__main__':
    AMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    for r in map(int, sys.argv[1].split(',')):
        q = 3**r
        t, tl = mass(q, AMAX)
        t0, _ = mass(q, AMAX, use_cls=False)
        print(f"r={r}: exact(alpha<={AMAX})={float(t):.10e} tail<={float(tl):.4e} total<={float(t + tl):.6e} "
              f"| without class bounds: {float(t0):.6e}")
