"""R232: FROM-SCRATCH check of STERILE_LOWER Lemma 3.1 (joint parametrisation of level-1 data).
Per-n enumerators here use DIVISORS (P: f | n + 4a^2 d, f == -1 mod 4ad; Q: f | 4a^2 d + 1, f == -n mod 4ad), which is a
different loop structure from the lemma's (a,c,d)/(a,d,f,c) sweeps; tiny n are additionally brute-forced over (a,b,c,d).
Compares the SETS of tuples (a,b,c,d) per n, not only counts.  Usage: review_r232_joint.py X  (checks n in [X, 2X))."""
import sys
from collections import defaultdict

def divisors(m):
    ds, i = [], 1
    while i * i <= m:
        if m % i == 0: ds.append(i); ds.append(m // i) if i * i != m else None
        i += 1
    return ds

def P_per_n(N):
    out = set()
    a = 1
    while 4 * a * a <= 2 * N:            # 4a^2 d <= 4abd = N + e <= N + 2b, b <= N/2  (SE L1.2; also brute-checked below)
        d = 1
        while 4 * a * a * d <= 2 * N:
            for f in divisors(N + 4 * a * a * d):
                if (f + 1) % (4 * a * d): continue
                c = (f + 1) // (4 * a * d); e = (N + 4 * a * a * d) // f; b = c * e - a
                if b >= a:
                    assert 4 * a * b * c * d == a + b + N * c; out.add((a, b, c, d))
            d += 1
        a += 1
    return out

def Q_per_n(n):
    out = set()
    a = 1
    while 4 * a <= 2 * n + 2:
        d = 1
        while 4 * a * d <= 2 * n + 2:
            for f in divisors(4 * a * a * d + 1):
                if (f + n) % (4 * a * d): continue
                c = (f + n) // (4 * a * d); e = (4 * a * a * d + 1) // f; b = c * e - a
                if b >= a and 4 * a * b * c * d == n * (a + b) + c: out.add((a, b, c, d))
            d += 1
        a += 1
    return out

def brute(n):
    P, Q = set(), set()
    for a in range(1, n + 2):
        for b in range(a, 4 * n * n + 2):
            for d in range(1, n + 2):
                if 4 * a * b * d > 4 * n * n * (a + b) + 4 * n * n: break
                for c in range(1, 2 * n + 4):
                    if 4 * a * b * c * d == a + b + n * c: P.add((a, b, c, d))
                    if 4 * a * b * c * d == n * (a + b) + c and (a + b) % c == 0: Q.add((a, b, c, d))   # e integral
    return P, Q

def joint(X):
    JP, JQ = defaultdict(set), defaultdict(set)
    # (i) literally: a,c,d >= 1, f = 4acd - 1, N == -4a^2 d (mod f), and a <= b <=> cN >= 4a^2cd - 2a
    a = 1
    while 4 * a * a - 2 * a < 2 * X:
        d = 1
        while 4 * a * a * d - 2 * a < 2 * X:
            c = 1
            while True:
                f = 4 * a * c * d - 1
                Nmin = -(-(4 * a * a * c * d - 2 * a) // c)          # smallest N with cN >= 4a^2cd - 2a
                if Nmin >= 2 * X and c > 1: pass
                # N == -4a^2 d mod f and N >= 1; residues below 2X exist only while f is not too large:
                start = (-4 * a * a * d) % f
                if start == 0: start = f
                if start >= 2 * X and f - 4 * a * a * d >= 2 * X: break
                N = start
                while N < 2 * X:
                    if N >= X and c * N >= 4 * a * a * c * d - 2 * a:
                        b = (N * c + a) // f; e = (N + 4 * a * a * d) // f
                        assert (N * c + a) % f == 0 and (N + 4 * a * a * d) % f == 0
                        assert 4 * a * b * d == N + e and c * e == a + b
                        JP[N].add((a, b, c, d))
                    N += f
                c += 1
                if c > 4 * X + 4: break
            d += 1
        a += 1
    # (ii) literally: a,d,f with f | 4a^2 d + 1, c >= 1 with n = 4acd - f > 0, b = (na + c)/f, keep b >= a
    for a in range(1, X + 2):
        for d in range(1, X + 2):
            if 4 * a * d > 4 * X + 4: break
            for f in divisors(4 * a * a * d + 1):
                c = 1
                while 4 * a * c * d - f < 2 * X:
                    n = 4 * a * c * d - f
                    if n >= X:
                        assert (n * a + c) % f == 0
                        b = (n * a + c) // f
                        assert 4 * a * b * c * d == n * (a + b) + c and c * ((4 * a * a * d + 1) // f) == a + b
                        if b >= a: JQ[n].add((a, b, c, d))
                    c += 1
    return JP, JQ

if __name__ == '__main__':
    for n in range(1, 13):
        P, Q = brute(n)
        assert P == P_per_n(n) and Q == Q_per_n(n), n
    print("brute force n <= 12: per-n divisor enumerators complete")
    X = int(sys.argv[1])
    JP, JQ = joint(X)
    bad = 0; tp = tq = 0
    for n in range(X, 2 * X):
        P, Q = P_per_n(n), Q_per_n(n); tp += len(P); tq += len(Q)
        if P != JP[n] or Q != JQ[n]: bad += 1; print("MISMATCH", n, P ^ JP[n], Q ^ JQ[n])
    print(f"X={X}: P data {tp}, Q data {tq}, mismatching n: {bad}")
