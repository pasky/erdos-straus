"""R222 (hostile review of O219 STERILE_EXPLICIT.md): from-scratch brute force of the P/Q identities and size facts
used by se_box.c / se_tail.py.  No author code imported.
P-data: 4abd = N+e, a+b = ce, a<=b (all, then in-cell r-free subset).  Q-data: N-points of Sigma^I_F: 4abcd = F(a+b)+c.
Usage: PYTHONPATH=scripts uv run python scripts/review_se_lemmas.py"""
import math, sys
from math import gcd

def pdata(N):
    out = []
    a = 1
    while 2 * a * a <= N:
        d = 1
        while 2 * a * a * d <= N:
            s = 4 * a * d
            lo = N // s + 1                      # 4abd > N
            hi = (N + a) // (s - 1)              # e <= a+b  <=>  b(4ad-1) <= N+a
            for b in range(max(lo, a), hi + 1):
                e = s * b - N
                if e > 0 and (a + b) % e == 0:
                    out.append((a, b, (a + b) // e, d, e))
            d += 1
        a += 1
    return out

def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n: ds.append(n // i)
        i += 1
    return ds

def qdata(F):
    out = []
    for a in range(1, F + 1):
        if 4 * a > F + F + 2: break
        for d in range(1, F // a + 1):           # acd <= F
            s = 4 * a * d
            if s > 2 * F + 2: break             # 4acd = f+F <= 2F+2
            t = 4 * a * a * d + 1
            for f in divisors(t):
                if (f + F) % s: continue
                e = t // f; c = (f + F) // s
                if (e * F + 1) % s: continue
                b = (e * F + 1) // s
                if b < a or (a + b) != c * e: continue
                assert 4 * a * b * c * d == F * (a + b) + c
                out.append((a, b, c, d, e, f))
    return out

def check_P(r, K):
    N = r ** K; bad = 0
    D = pdata(N); cell = [t for t in D if all(x % r for x in t[:4])]
    for (a, b, c, d, e) in D:
        f, f2 = 4 * a * c * d - 1, 4 * b * c * d - 1
        ok = (e * f == N + 4 * a * a * d and e * f2 == N + 4 * b * b * d and b * f == N * c + a and a * f2 == N * c + b
              and f * f2 == 4 * c * c * d * N + 1 and e % 2 == 1 and 2 * a * a * d <= N and a * c * d <= N and e <= N)
        A, C, Dd = 2 ** (a.bit_length() - 1), 2 ** (c.bit_length() - 1), 2 ** (d.bit_length() - 1)
        ok &= N / (16 * A * Dd) < b <= N / (2 * A * Dd) and N / (32 * A * C * Dd) < e <= N / (A * C * Dd)
        ok &= 4 * A * C * Dd - 1 <= f < 32 * A * C * Dd
        ok &= N < 4 * a * c * d * e <= 2 * (N + e)            # tail: e > N/(4acd), e <= N/(acd)
        if all(x % r for x in (a, b, c, d)):
            ok &= gcd(e, a * b * d) == 1                    # unit classes (Lemma 1.1(iv)) -- in-cell only
            ok &= (-f) % r ** ((K + 1) // 2) == (-a * pow(b, -1, r ** ((K + 1) // 2))) % r ** ((K + 1) // 2)
        if (a % r == 0) != (b % r == 0) and c % r and d % r: ok = False
        if not ok: bad += 1; print("P FAIL", r, K, (a, b, c, d, e))
    return len(D), len(cell), bad

def check_Q(r, k):
    F = r ** k; bad = 0
    D = qdata(F); cell = [t for t in D if t[4] % r]
    per = {}
    for (a, b, c, d, e, f) in D:
        per[(a, d)] = per.get((a, d), 0) + 1
        ok = (e * f == 4 * a * a * d + 1 and 4 * a * b * d == e * F + 1 and f * b == a * F + c
              and f * (4 * b * c * d - F) == F * F + 4 * c * c * d and c * d <= F and 0 < f <= F + 2 and e % 2 == 1 and f % 2 == 1)
        if e % r:
            ok &= (-4 * a * a * d - (-a * pow(b, -1, F))) % F == 0     # Q box centre -a/b
            if c % r:
                ok &= gcd(f, F) == 1 and a % r != 0 and b % r != 0 and d % r != 0
                ok &= (c + a * F) % f == 0 and (4 * a * a * d + 1) % f == 0
                ok &= (a * F + c) % f == 0                              # a == -c/F (mod f)
                ok &= gcd(F, 4 * a * c) == 1 and gcd(e, a * b * d) == 1
            else:
                ok &= (a + b) % r == 0                                # r|c => centre == 1 (not in a non-residue cell)
        if not ok: bad += 1; print("Q FAIL", r, k, (a, b, c, d, e, f))
    return len(D), len(cell), bad, max(per.values()) if per else 0

if __name__ == '__main__':
    tot = 0
    for (r, K) in [(3, 7), (3, 9), (5, 5), (7, 5), (13, 3), (17, 3), (17, 5), (19, 3), (23, 3), (29, 3), (101, 3), (7, 7)]:
        n, nc, bad = check_P(r, K); tot += bad
        print(f"P r={r} K={K}: data {n}, in-cell {nc}, failures {bad}")
    for (r, k) in [(3, 5), (3, 7), (5, 3), (7, 3), (13, 3), (17, 3), (19, 3), (23, 3), (101, 2), (1009, 1), (9973, 1)]:
        n, nc, bad, mx = check_Q(r, k); tot += bad
        print(f"Q r={r} k={k}: N-points {n}, r-free-e {nc}, failures {bad}, max per (a,d) {mx}")
    print("TOTAL failures", tot); sys.exit(1 if tot else 0)
