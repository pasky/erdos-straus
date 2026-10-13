"""R202 from-scratch recomputation of MARKOFF_ES §6 table entries (does NOT reuse scripts/mk_*).

For fixed (n, D) and lambda in [L0, L0+W): mu = lambda*D, N = 4(mu^2 - n).
 global: x^2 - N z^2 = -D has a primitive solution (z >= 1).  Methods: N square -> factor;
         D < sqrt(N) -> Lagrange: some odd k with Q_k = D in the CF of sqrt(N) (scan 1 or 2 periods);
         else exhaustive Nagell bound over class representatives.
 local:  N > 0, (D = 7 mod 8 or lambda even), and (-D/p) = 1 for every odd p | mu^2 - n
         (own derivation; also tested against global: global => local must hold).
Usage: review_mk_fibre.py n D L0 W [--depth lam]
"""
import sys
from math import gcd, isqrt
from sympy import factorint


def leg(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


def cf_scan(N, D):
    """return (found, first odd k with Q_k = D, period)."""
    a0 = isqrt(N)
    m, d, a = 0, 1, a0
    k, per, found = 0, None, None
    while True:
        k += 1
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        if d == D and k % 2 == 1 and found is None:
            found = k
        if d == 1 and per is None:
            per = k
        if per is not None and (k >= 2 * per or (per % 2 == 0 and k >= per)):
            return found is not None, found, per


def fund_unit(N):
    a0 = isqrt(N)
    m, d, a = 0, 1, a0
    p_prev, p, q_prev, q = 1, a0, 0, 1
    k = 0
    while True:
        k += 1
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        if d == 1 and k % 2 == 0:
            return p, q
        p_prev, p = p, a * p + p_prev
        q_prev, q = q, a * q + q_prev


def solve(N, D):
    if N <= 0:
        return False
    s = isqrt(N)
    if s * s == N:
        for e in range(1, D + 1):
            if D % e == 0:
                f = D // e
                for (u, w) in ((-e, f), (e, -f)):
                    if (w - u) % (2 * s) == 0 and (u + w) % 2 == 0:
                        z, x = (w - u) // (2 * s), (u + w) // 2
                        if z > 0 and gcd(x, z) == 1:
                            return True
        return False
    if D < s:
        return cf_scan(N, D)[0]
    x1, _ = fund_unit(N)
    for x in range(0, isqrt((x1 + 1) * D // 2 + 1) + 2):
        t = x * x + D
        if t % N == 0:
            z = isqrt(t // N)
            if z > 0 and z * z * N == t and gcd(x, z) == 1:
                return True
    return False


def local_ok(n, D, lam):
    mu = lam * D
    f = mu * mu - n
    if f <= 0:
        return False
    if not (D % 8 == 7 or lam % 2 == 0):
        return False
    for p in factorint(f):
        if p > 2 and leg(-D, p) != 1:
            return False
    return True


def main():
    n, D, L0, W = map(int, sys.argv[1:5])
    if len(sys.argv) > 5 and sys.argv[5] == '--depth':
        lam = L0
        N = 4 * (lam * lam * D * D - n)
        print("lam", lam, "sqrtN", isqrt(N), "scan", cf_scan(N, D))
        return
    loc = glo = sq = 0
    for lam in range(L0, L0 + W):
        mu = lam * D
        N = 4 * (mu * mu - n)
        if N > 0 and isqrt(N) ** 2 == N:
            sq += 1
        g = solve(N, D)
        l = local_ok(n, D, lam)
        if g and not l:
            print("GLOBAL BUT NOT LOCAL", n, D, lam)
        loc += l
        glo += g
    print(f"n={n} D={D} lam in [{L0},{L0 + W}): global/local = {glo}/{loc}  (square-N lambdas: {sq})")


if __name__ == "__main__":
    main()
