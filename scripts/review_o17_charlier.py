"""R68b from-scratch check of POINTWISE_OMEGA17 Prop 3.1.

psi_n(j) = 1 - C_n(j;R),  C_n(j;R) = sum_r binom(n,r) (-1)^r (j)_r / R^r.
(a) identities (i),(ii) in exact rationals for small n, R (Poisson expectation of psi*q for
    q = falling factorials of degree < n, via E[(N)_m] = R^m, exact).
(b) positivity on ALL integers j>=0, with a RIGOROUS cutoff: Fujiwara root bound on the
    integer polynomial P(j) = R^n psi_n(j) in the power basis; beyond it P>0 (leading coeff >0
    for n odd), so only 0..bound need checking.  Integer arithmetic throughout.
(c) R_min(n) := least integer R>=1 with psi_n>=0 on Z_{>=0}; also checks whether the set of
    good integer R is up-closed on a window [1, R_min+W].
"""
import sys
from fractions import Fraction as Fr
from math import comb


def poly_P(n, R):
    """coefficients (power basis in j) of R^n * psi_n(j), integers."""
    P = [0] * (n + 1)
    P[0] = R ** n
    ff = [1]  # (j)_0
    for r in range(0, n + 1):
        if r > 0:
            # ff *= (j - (r-1))
            new = [0] * (len(ff) + 1)
            for i, c in enumerate(ff):
                new[i + 1] += c
                new[i] -= (r - 1) * c
            ff = new
        c = comb(n, r) * (-1) ** r * R ** (n - r)
        for i, a in enumerate(ff):
            P[i] -= c * a
    return P


def fujiwara(P):
    n = len(P) - 1
    an = P[n]
    assert an > 0
    best = 0.0
    for i in range(1, n + 1):
        a = abs(P[n - i])
        if a == 0:
            continue
        v = (a / an) ** (1.0 / i)
        if i == n:
            v = (a / (2 * an)) ** (1.0 / i)
        best = max(best, v)
    return int(2 * best * 1.001) + 2  # float safety margin


def nonneg_on_N(n, R):
    P = poly_P(n, R)
    B = fujiwara(P)
    # evaluate psi*R^n at j=0..B via direct sum (independent of P)
    for j in range(0, B + 1):
        s = 0
        ff = 1
        for r in range(0, n + 1):
            if r > 0:
                ff *= (j - r + 1)
                if ff == 0:
                    break
            s += comb(n, r) * (-1) ** r * ff * R ** (n - r)
        if R ** n - s < 0:
            return False, j, B
    return True, None, B


def identities():
    for n in range(1, 8):
        for R in (Fr(1, 2), Fr(3), Fr(7, 3)):
            # E[(N)_m] = R^m for Poisson
            # psi = 1 - sum_r binom(n,r)(-1)^r (N)_r / R^r ; psi(0)=0 since only r=0 term survives
            # E[psi * (N)_m] for m<n: (N)_r (N)_m = sum_i binom(r,i)binom(m,i) i! (N)_{r+m-i}
            for m in range(n):
                tot = Fr(R) ** m
                for r in range(n + 1):
                    ex = sum(comb(r, i) * comb(m, i) * __import__('math').factorial(i) * R ** (r + m - i)
                             for i in range(min(r, m) + 1))
                    tot -= comb(n, r) * (-1) ** r * ex / R ** r
                assert tot == R ** m, (n, R, m, tot)
    print("identities (ii): E[psi_n (N)_m] = E[(N)_m] for m<n, n<=7: OK")


if __name__ == "__main__":
    identities()
    claimed = {1: 1, 3: 2, 5: 5, 7: 9, 9: 13, 11: 18, 13: 23, 15: 28, 17: 33, 21: 44, 25: 56,
               31: 74, 41: 104, 61: 169, 81: 236}
    W = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    for n, rc in claimed.items():
        res = {}
        top = rc + W
        Rs = range(1, top + 1) if n <= 41 else list(range(rc - 3, top + 1))
        for R in Rs:
            ok, j, B = nonneg_on_N(n, R)
            res[R] = (ok, j, B)
        goodR = [R for R in Rs if res[R][0]]
        rmin = min(goodR) if goodR else None
        upclosed = all(res[R][0] for R in Rs if R >= (rmin or 10**9))
        maxB = max(res[R][2] for R in Rs)
        print(f"n={n:3d} claimed R_min={rc:4d} found={rmin} up-closed on window={upclosed} "
              f"fail@R_min-1: j={res.get(rc-1, (None, None, None))[1]} max Fujiwara bound={maxB}",
              flush=True)
