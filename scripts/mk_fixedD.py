"""O202: fixed-level census for V_n : nA^2 + B^2 + D = 2 lam D A B (A even, B odd, coprime).

Dictionary (MARKOFF_ES Prop 4.1): (A,B) solution with given (lam, D)  <=>  x^2 - N z^2 = -D primitive,
N = 4(lam^2 D^2 - n), x = B - lam*D*A, z = A/2.  If D < sqrt(N) every primitive solution is a convergent of
sqrt(N) (Lagrange), so existence <=> some odd-index CF denominator Q_k of sqrt(N) equals D (k <= 2*period).

Usage: mk_fixedD.py n D LAM [verify]
Prints: number of lam <= LAM with a solution, list of first few, and (if verify) explicit (A,B) checked exactly.
"""
import sys
from math import isqrt, gcd


def cf_hit(N, D, want_conv=False):
    """Return k (odd) with Q_k == D in CF of sqrt(N) within 2 periods, else None.
    If want_conv, also return the convergent (p_{k-1}, q_{k-1})."""
    a0 = isqrt(N)
    if a0 * a0 == N:
        return None
    m, d, a = 0, 1, a0
    p_prev, p = 1, a0
    q_prev, q = 0, 1
    k = 0
    L = None
    while True:
        k += 1
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        # now d = Q_k, and (p, q) = (p_{k-1}, q_{k-1})
        if k % 2 == 1 and d == D:
            if want_conv:
                assert p * p - N * q * q == -D
                return k, p, q
            return k
        if d == 1 and L is None:
            L = k
        if L is not None and k >= 2 * L:
            return None
        if want_conv:
            p_prev, p = p, a * p + p_prev
            q_prev, q = q, a * q + q_prev


def solve(n, D, lam, want=False):
    N = 4 * (lam * lam * D * D - n)
    if N <= 0 or D * D >= N:
        return "skip"
    return cf_hit(N, D, want)


def main():
    n, D, LAM = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    verify = len(sys.argv) > 4
    hits, skips = [], []
    for lam in range(1, LAM + 1):
        r = solve(n, D, lam, verify)
        if r == "skip":
            skips.append(lam)
            continue
        if r is not None:
            hits.append(lam)
            if verify:
                k, p, q = r
                A = 2 * q
                for x in (p, -p):
                    B = x + lam * D * A
                    assert B > 0 and B % 2 == 1 and gcd(A, B) == 1 and gcd(B, n) == 1
                    assert n * A * A + B * B + D == 2 * lam * D * A * B
    print(f"n={n} D={D} LAM={LAM}: hits {len(hits)}/{LAM - len(skips)} skips={skips[:5]} first={hits[:12]}")


if __name__ == "__main__":
    main()
