"""R197 from-scratch word-level check of MODEL_SPECIFIC Lemma 3.0, 3.0', Thm 3.1, Cor 3.2.

Words: (t,u,v) >= 1, t*u*v - u - v = n (n odd >= 3), A = t*u-1 >= 1, A* = t*v-1.
Own Jacobi symbol; every slice solution verified in exact rationals.
Usage: PYTHONPATH=scripts uv run python scripts/review_ms_words.py NMAX
"""
import sys
from fractions import Fraction as F
from math import gcd


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    s = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                s = -s
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            s = -s
        a %= n
    return s if n == 1 else 0


def words(n):
    out = []
    # t = 1: (u-1)(v-1) = n+1
    N = n + 1
    for a in range(1, N + 1):
        if N % a == 0:
            out.append((1, a + 1, N // a + 1))
    t = 2
    while True:
        # u = 1 allowed: need (t-1)v - 1 = n  (v>=1)
        umax = (n + 1) // (t - 1)
        if umax < 1:
            break
        for u in range(1, umax + 1):
            A = t * u - 1
            if (n + u) % A == 0:
                v = (n + u) // A
                if v >= 1 and t * u * v - u - v == n:
                    out.append((t, u, v))
        t += 1
    return out


def slice_solutions(m, t, u, v, n):
    """Lemma 3.0 solutions (each a triple of denominators) for the slices hit."""
    A, As = t * u - 1, t * v - 1
    sols = []
    if A % m == 0:
        d = A // m
        sols.append(("I", (As * d * n, v * d, As * v * d)))
    if As % m == 0:
        d = As // m
        sols.append(("I'", (A * d * n, u * d, A * u * d)))
    if t % m == 0:
        c = t // m
        sols.append(("T", (u * v * c, u * c * n, v * c * n)))
    if u % m == 0:
        w, f = u // m, t * v - 1
        sols.append(("U", (w * f, t * n * w, t * n * w * f)))
    if v % m == 0:
        w, f = v // m, t * u - 1
        sols.append(("V", (w * f, t * n * w, t * n * w * f)))
    return sols


def cell_rhs(n, t, u, v):
    A, As = t * u - 1, t * v - 1
    return (n + 1 - n * (t + u + v - 9) - A - As) % 8


def main():
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    MS = list(range(4, 25))
    tot = 0
    nchi = {1: 0, -1: 0}
    inS = {m: {1: 0, -1: 0} for m in MS}
    bad_cell = bad_gcd = bad_sol = bad_thm = 0
    per_n = {}
    for n in range(3, NMAX + 1, 2):
        W = words(n)
        cnt = {m: 0 for m in (4, 8)}
        neg = 0
        for (t, u, v) in W:
            tot += 1
            A = t * u - 1
            if gcd(A, n) != 1:
                bad_gcd += 1
            jA = jacobi(A, n)
            if (2 * jA - cell_rhs(n, t, u, v)) % 8:
                bad_cell += 1
            chi = jacobi(-A % n, n) if A % n else 0
            nchi[chi] += 1
            if chi == -1:
                neg += 1
            for m in MS:
                sols = slice_solutions(m, t, u, v, n)
                for (_, (x, y, z)) in sols:
                    if min(x, y, z) <= 0 or F(1, x) + F(1, y) + F(1, z) != F(m, n):
                        bad_sol += 1
                if sols:
                    inS[m][chi] += 1
                    if m in cnt:
                        cnt[m] += 1
            s4 = bool(slice_solutions(4, t, u, v, n))
            if s4 != (chi == -1):
                bad_thm += 1
        per_n[n] = (len(W), neg, cnt[4], cnt[8])
    print("odd n in [3,%d]: words=%d  chi=-1:%d chi=+1:%d" % (NMAX, tot, nchi[-1], nchi[1]))
    print("gcd(A,n)>1:", bad_gcd, " cell-formula mismatches:", bad_cell,
          " bad slice solutions:", bad_sol, " Thm3.1(a) word mismatches:", bad_thm)
    for m in MS:
        print("m=%2d  S_m among chi=-1: %6d  among chi=+1: %6d" % (m, inS[m][-1], inS[m][1]))
    for n in (131, 241):
        if n in per_n:
            print("n=%d words=%d chi=-1:%d in S_4:%d in S_8:%d" % ((n,) + per_n[n]))


if __name__ == "__main__":
    main()
