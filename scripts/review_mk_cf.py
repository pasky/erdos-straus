"""R202 from-scratch check of MARKOFF_ES Thms 4.1-4.3 (does NOT reuse scripts/mk_*).

For odd n in [nlo, nhi]:
 (1) brute force V_n points: A even <= X, B odd <= X, gcd(A,B)=gcd(B,n)=1, divisors g of nA^2+B^2 with
     g = -1 mod 2AB, lambda=(g+1)/(2AB), D=(nA^2+B^2)/g, mu = lambda*D <= M;
 (2) CF hits: for sqrt(n) < mu <= M, CF of sqrt(N), N=4(mu^2-n): odd k, Q_k odd, gcd(Q_k,n)=1, Q_k | mu
     -> (A,B) = (2q_{k-1}, mu*A -+ p_{k-1});  N square handled by factoring;
     small mu (3mu^2 <= 4n) handled by an exhaustive Nagell-bound solver;
 (3) compare (1) vs (2) inside the box, per region; record depth k of every B=1 point;
 (4) Thm 4.3 formulas for 2n < mu <= 5n.
Usage: review_mk_cf.py nlo nhi X M_factor
"""
import sys
from math import gcd, isqrt


def cf_upto(N, qmax, kmin):
    """yield (k, Q_k, p_{k-1}, q_{k-1}) for k>=1 until q_{k-1} > qmax and k > kmin."""
    a0 = isqrt(N)
    m, d, a = 0, 1, a0
    p_prev, p = 1, a0
    q_prev, q = 0, 1
    k = 0
    while True:
        k += 1
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        # now d = Q_k, (p,q) = (p_{k-1}, q_{k-1})
        assert p * p - N * q * q == (-1) ** k * d
        yield k, d, p, q
        if q > qmax and k > kmin:
            return
        p_prev, p = p, a * p + p_prev
        q_prev, q = q, a * q + q_prev


def fund_unit(N):
    for k, Q, p, q in cf_upto(N, 10 ** 30, 0):
        if Q == 1 and k % 2 == 0:
            return p, q


def all_points_small(n, mu, X):
    """all V_n points with this mu (any D | mu), A<=X, exhaustive (Nagell bound for classes, then orbit)."""
    N = 4 * (mu * mu - n)
    out = set()
    if N <= 0:
        return out
    s = isqrt(N)
    for D in range(1, mu + 1, 2):
        if mu % D or gcd(D, n) != 1:
            continue
        if s * s == N:  # (x - s z)(x + s z) = -D
            for e in range(1, D + 1):
                if D % e:
                    continue
                f = D // e  # x - s z = -e, x + s z = f  (or signs swapped)
                for (u, v) in ((-e, f), (e, -f)):
                    if (v - u) % (2 * s) == 0:
                        z = (v - u) // (2 * s)
                        x = (u + v) // 2
                        if z > 0 and (u + v) % 2 == 0 and gcd(x, z) == 1:
                            for xx in (x, -x):
                                A, B = 2 * z, mu * 2 * z - xx
                                if A <= X and 0 < B <= X:
                                    out.add((A, B, D))
            continue
        x1, y1 = fund_unit(N)
        bound = isqrt((x1 + 1) * D // 2 + 1) + 1
        reps = []
        for x in range(0, bound + 1):
            t = x * x + D
            if t % N == 0:
                z = isqrt(t // N)
                if z * z * N == t and z > 0 and gcd(x, z) == 1:
                    reps.append((x, z))
        for (x0, z0) in reps:
            for sx in (x0, -x0):
                x, z = sx, z0
                for _ in range(60):  # walk the orbit forward
                    if z > 0:
                        A = 2 * z
                        if A > X:
                            break
                        for xx in (x, -x):
                            B = mu * A - xx
                            if 0 < B <= X:
                                out.add((A, B, D))
                    x, z = x * x1 + N * z * y1, x * y1 + z * x1
    return out


def brute(n, X, M):
    pts = {}
    for A in range(2, X + 1, 2):
        for B in range(1, X + 1, 2):
            if gcd(A, B) != 1 or gcd(B, n) != 1:
                continue
            S = n * A * A + B * B
            m2 = 2 * A * B
            i = 1
            while i * i <= S:
                if S % i == 0:
                    for g in {i, S // i}:
                        if (g + 1) % m2 == 0:
                            lam = (g + 1) // m2
                            D = S // g
                            if lam * D <= M:
                                assert n * A * A + B * B + D == 2 * lam * D * A * B
                                pts[(A, B, D)] = lam * D
                i += 1
    return pts


def cf_hits(n, mu, X):
    N = 4 * (mu * mu - n)
    out = {}
    if N <= 0 or isqrt(N) ** 2 == N:
        return None
    for k, Q, p, q in cf_upto(N, X // 2, 2):
        if k % 2 == 1 and Q % 2 == 1 and gcd(Q, n) == 1 and mu % Q == 0:
            A = 2 * q
            for B in (mu * A - p, mu * A + p):
                if A <= X and 0 < B <= X:
                    out[(A, B, Q)] = k
    return out


def main():
    nlo, nhi, X, Mf = map(int, sys.argv[1:5])
    tot = dict(brute=0, cfmiss=0, cfextra=0, small_mu_pts=0, sqN_mu=0, b1_by_depth={}, f43_bad=0,
               nlam=0, Dmod4=0)
    small_examples = []
    for n in range(nlo, nhi + 1, 2):
        M = Mf * n
        bp = brute(n, X, M)
        tot['brute'] += len(bp)
        cf = {}
        for mu in range(isqrt(n) + 1, M + 1):
            h = cf_hits(n, mu, X)
            if 3 * mu * mu <= 4 * n or h is None:
                sp = all_points_small(n, mu, X)
                if h is None:
                    tot['sqN_mu'] += 1
                for (A, B, D) in sp:
                    tot['small_mu_pts'] += 1
                    if B <= X and (A, B, D) not in bp:
                        print("MISS-small brute", n, mu, A, B, D)
                    if len(small_examples) < 12:
                        small_examples.append((n, mu, A, B, D))
                    cf[(A, B, D)] = "small" if h is None or (A, B, D) not in h else h[(A, B, D)]
                    if cf[(A, B, D)] == "small":
                        print("NON-CF small-mu point", n, mu, A, B, D, "sqN" if h is None else "")
                if h is None:
                    continue
            cf.update({key: k for key, k in h.items() if key not in cf})
        for key, mu in bp.items():
            if key not in cf:
                tot['cfmiss'] += 1
                print("CF-MISS", n, key, mu)
        for key in cf:
            if key not in bp:
                tot['cfextra'] += 1
                print("CF-EXTRA", n, key)
        for (A, B, D), k in cf.items():
            if (A, B, D) in bp:
                mu = bp[(A, B, D)]
                lam = mu // D
                tot['nlam'] += (lam % n == 0)
                tot['Dmod4'] += (D % 4 != 3)
                if B == 1:
                    reg = '>2n' if mu > 2 * n else '<=2n'
                    tot['b1_by_depth'][(reg, k)] = tot['b1_by_depth'].get((reg, k), 0) + 1
                if mu > 2 * n and k != 3 and k != 'small' and B == 1:
                    print("B1 not depth 3", n, A, B, D, mu, k)
                if mu > 2 * n and k == 3 and B != 1 and B != 2 * mu * A // 1 - 1:
                    print("depth3 but B not in {1,4mu j-1}", n, A, B, D, mu)
        # Thm 4.3 formulas
        for mu in range(2 * n + 1, 5 * n + 1):
            t = mu % n or n
            j = (mu - t) // n
            N = 4 * (mu * mu - n)
            g = cf_upto(N, 0, 3)
            got = [next(g) for _ in range(3)]
            exp = [(1, 4 * mu - 1 - 4 * n), (2, 4 * n), (3, 4 * t * j - 1)]
            if [(k, Q) for k, Q, _, _ in got] != exp or (got[2][2], got[2][3]) != (2 * mu * j - 1, j):
                tot['f43_bad'] += 1
                print("4.3 formula fails", n, mu, got)
    print(tot)
    print("small-mu examples (n, mu, A, B, D):", small_examples)


if __name__ == "__main__":
    main()
