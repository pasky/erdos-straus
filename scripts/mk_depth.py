"""O202: CF-depth dictionary.  For mu >= 1 let N = 4(mu^2 - n).  Claim (MARKOFF_ES Thm 4.3):
admissible points of V_n with lam*D = mu  <->  odd k with Q_k | mu (Q_k = CF complete-quotient denominator of
sqrt(N)); the point is (A, B) = (2 q_{k-1}, mu*A -/+ p_{k-1}); ES's shot family (B = 1) <-> k in {1, 3}.
Checks: every hit gives a valid V_n point; B = 1 occurs exactly at k <= 3; cross-check against brute force
enumeration of V_n points with A, B <= BOX.
Usage: mk_depth.py n MU BOX
"""
import sys
from math import isqrt, gcd


def hits(n, mu):
    N = 4 * (mu * mu - n)
    if N <= 0:
        return []
    a0 = isqrt(N)
    if a0 * a0 == N:
        return []
    out = []
    m, d, a = 0, 1, a0
    p_prev, p, q_prev, q = 1, a0, 0, 1
    k, L = 0, None
    while True:
        k += 1
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        if k % 2 == 1 and d % 2 == 1 and mu % d == 0 and gcd(d, n) == 1:
            assert p * p - N * q * q == -d
            A = 2 * q
            for B in (mu * A - p, mu * A + p):
                out.append((k, d, A, B))
        if d == 1 and L is None:
            L = k
        if L is not None and k >= 2 * L:
            return out
        p_prev, p = p, a * p + p_prev
        q_prev, q = q, a * q + q_prev


def main():
    n, MU, BOX = map(int, sys.argv[1:4])
    found = set()
    nk = {}
    for mu in range(1, MU + 1):
        for (k, D, A, B) in hits(n, mu):
            lam = mu // D
            assert n * A * A + B * B + D == 2 * lam * D * A * B, (mu, k)
            assert A % 2 == 0 and B % 2 == 1 and gcd(A, B) == 1 and gcd(B, n) == 1 and D % 4 == 3
            assert (B == 1) == (k <= 3) or B != 1, (mu, k, A, B)
            if B == 1:
                assert k <= 3, (n, mu, k, A, B)
            found.add((A, B, lam, D))
            nk[k] = nk.get(k, 0) + 1
    # brute force: all V_n points with A, B <= BOX and lam*D <= MU
    brute = set()
    for A in range(2, BOX + 1, 2):
        for B in range(1, BOX + 1, 2):
            if gcd(A, B) != 1 or gcd(B, n) != 1:
                continue
            S = n * A * A + B * B
            g0 = 2 * A * B
            # D*(lam*g0 - 1) = S: enumerate g = lam*g0 - 1 dividing S
            g = g0 - 1
            while g <= S:
                if S % g == 0:
                    lam = (g + 1) // g0
                    D = S // g
                    if lam * D <= MU:
                        brute.add((A, B, lam, D))
                g += g0
    inbox = {t for t in found if t[0] <= BOX and t[1] <= BOX}
    print(f"n={n} mu<={MU}: CF hits {len(found)} (by depth k: {dict(sorted(nk.items()))}); "
          f"brute box {BOX}: {len(brute)}; CF-in-box {len(inbox)}; brute-not-CF {sorted(brute - found)[:5]}; "
          f"B=1 count {sum(1 for t in found if t[1] == 1)}")


if __name__ == "__main__":
    main()
