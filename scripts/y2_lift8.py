"""y2_lift8: the lifting problem mod 8 for pentagon friezes with frozen (1,1,1,1,N).

For each odd N <= X, R(N) = set of classes (c,m,s) mod 8 realized by positive words (letters >= 2 if INTERIOR=1,
else >= 1) with K(c,m,s) = N.  A(N) = all classes (c,m,s) mod 8 with K = N mod 8 ("locally allowed").
T1-allowed set A'(N) = A(N) minus {classes with 8 | ee'} if N is a square.  (Sign of class: even-edge thm.)
Report: |A|, and the N for which R(N) != A'(N) (the "lifting failures"), grouped.
usage: y2_lift8.py X INTERIOR
"""
import sys
from collections import defaultdict
from math import isqrt


def K(c, m, s):
    return m * c * s - c - s


def ee_bit(c, m, s, N):
    h, hp = c * m - 1, m * s - 1
    q = [hp, c, m, s, h]
    ev = [x for x in q if x % 2 == 0]
    return (ev[0] * ev[1]) % 8 == 0


def main(X, interior):
    lo = 2 if interior else 1
    R = defaultdict(set)
    m = lo
    while m * lo * lo - 2 * lo <= X or m <= 3:
        c = lo
        while True:
            if K(c, m, lo) > X and m >= 2:
                break
            if m == 1 and c > X + 3:
                break
            s = lo
            while True:
                N = K(c, m, s)
                if N > X:
                    break
                if N > 0 and N % 2:
                    R[N].add((c % 8, m % 8, s % 8))
                if m == 1 and s > X + 3:
                    break
                s += 1
            c += 1
        m += 1
        if m > X + 3:
            break
    allowed = {}
    for r in range(1, 8, 2):
        A = set()
        for c in range(8):
            for mm in range(8):
                for s in range(8):
                    if K(c, mm, s) % 8 == r:
                        A.add((c, mm, s))
        allowed[r] = A
    print("|A(N)| by N mod 8:", {r: len(allowed[r]) for r in allowed})
    fails = defaultdict(list)
    for N in range(3, X + 1, 2):
        A = allowed[N % 8]
        sq = isqrt(N) ** 2 == N
        Ap = {t for t in A if not (sq and ee_bit(*t, N))}
        RN = R.get(N, set())
        if RN - Ap:
            print("IMPOSSIBLE: realized class outside A'", N)
        miss = len(Ap - RN)
        if miss:
            fails[N % 8].append((N, miss))
    for r in sorted(fails):
        L = fails[r]
        print(f"N={r} mod 8: {len(L)} N with missing classes; largest 8:", L[-8:])
    # squares: check that all T1-allowed classes are realized beyond small N
    return 0


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))


def class_rates(X, interior):
    """per (N mod 8, class): fraction of non-square odd N in [X/2, X] realizing the class; print the min ones."""
    lo = 2 if interior else 1
    R = defaultdict(set)
    for m in range(lo, X + 4):
        if m * lo * lo - 2 * lo > X and m > 3:
            break
        c = lo
        while (K(c, m, lo) <= X or m == 1) and c <= X + 3:
            s = lo
            while s <= X + 3:
                N = K(c, m, s)
                if N > X:
                    break
                if N > X // 2 and N % 2:
                    R[N].add((c % 8, m % 8, s % 8))
                s += 1
            c += 1
    cnt = defaultdict(int); tot = defaultdict(int)
    for N in range(X // 2 + 1, X + 1):
        if N % 2 == 0 or isqrt(N) ** 2 == N:
            continue
        tot[N % 8] += 1
        for t in R.get(N, ()):
            cnt[(N % 8, t)] += 1
    for r in (1, 3, 5, 7):
        rates = []
        for c in range(8):
            for mm in range(8):
                for s in range(8):
                    if K(c, mm, s) % 8 == r:
                        rates.append((cnt[(r, (c, mm, s))] / tot[r], (c, mm, s), ee_bit(c, mm, s, r)))
        rates.sort()
        print(f"N={r} mod 8: min rates", [(round(a, 3), t, b) for a, t, b in rates[:5]], " max", round(rates[-1][0], 3))
