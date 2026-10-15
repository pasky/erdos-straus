#!/usr/bin/env python3
"""R239 from-scratch: (1) Thm 1.1 for all odd non-square n = 1 (mod 4) <= N (composite included):
least window, min cap there, exact Def 1.1 check.  (2) Odd squares n = a^2 <= N2 with all primes = 1 (4):
R239 route D3 -- apply Thm 1.1 to d = n/p (p | a), least prime q with conditions for d only (= Frobenius in
Q(i,sqrt2,sqrt p)), scale by k = p, check exact Def 1.1 at n.  Compare with author's Cor 1.2(c) route.
Usage: review_r239_composite_squares.py N N2
"""
import sys
from fractions import Fraction
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from review_r239_windows import sieve_spf, jacobi, factor, min_cap, build, check_def11  # R239's own code


def least_window(n, spf, extra=lambda q: True):
    q = 3 if (4 - n) % 8 == 3 else 7
    while True:
        if spf[q] == q and n % q and jacobi(q, n) == -1 and extra(q):
            return q
        q += 8


def main():
    N = int(sys.argv[1]); N2 = int(sys.argv[2])
    spf = sieve_spf(max(N, N2) + 5000)
    cnt = 0; recq = (0, 0); recc = (0, 0, 0)
    for n in range(5, N + 1, 4):
        r = int(n ** 0.5)
        if r * r == n:
            continue
        cnt += 1
        q = least_window(n, spf)
        K = (n + q) // 4
        Kf = factor(K, spf)
        e, ex = min_cap(n, q, Kf, q)
        assert e is not None and e <= q - 3, n
        x, y, z = build(n, q, ex)
        assert check_def11(n, x, y, z, sorted(Kf)) == e
        if q > recq[0]: recq = (q, n)
        if e > recc[0]: recc = (e, n, q)
    print("odd non-squares n=1(4) <= %d: %d; least window record %s; min-cap record at least window %s" % (N, cnt, recq, recc))
    # odd squares
    sq = 0; worst = (0, 0, 0); cmp_ = []
    a = 1
    while (a + 2) ** 2 <= N2:
        a += 2
        n = a * a
        af = factor(a, spf)
        if any(l % 4 != 1 for l in af):
            continue
        sq += 1
        assert all(jacobi(qq, n) != -1 for qq in (3, 7, 11, 19, 23, 31))  # T1: no window at n itself
        p = max(af)
        d = n // p
        q = least_window(d, spf)  # conditions for d only
        K = (d + q) // 4
        Kf = factor(K, spf)
        assert K % p != 0
        e, ex = min_cap(d, q, Kf, q)
        x, y, z = build(d, q, ex)
        allowed = sorted(Kf)
        assert check_def11(d, x, y, z, allowed) == e
        X, Y, Z = p * x, p * y, p * z
        en = check_def11(n, X, Y, Z, allowed)
        assert en == e
        # author's route: Thm 1.1 at p with exclusions q != -p mod l, l | a, l != p
        qa = least_window(p, spf, extra=lambda qq: all((qq + p) % l for l in af if l != p))
        cmp_.append((n, q, qa))
        if q > worst[0]: worst = (q, n, e)
    print("odd squares (all primes 1 mod 4) <= %d: %d, all verified via d=n/p route; worst q %s" % (N2, sq, worst))
    print("sample (n, q via D3 route, q via author's Cor1.2(c) route):", cmp_[:8])


if __name__ == "__main__":
    main()
