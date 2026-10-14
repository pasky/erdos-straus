#!/usr/bin/env python3
"""O206 LENGTH_THREE: check the pentagon / Machin-CM / pencil dictionaries.

Usage: PYTHONPATH=scripts uv run python scripts/l3_dict.py NMAX PMAX
 (1) all words (c,m,s), letters >= 2, K = mcs - c - s <= NMAX:
     Farey pentagon 0, inf, c, h/m, N/h' has unit sides, closing side N, diagonals c,m,s,h,h' (exact dets),
     five Ptolemy relations; Machin-CM identity (c+z)(s+z) = (c+s)(1/m+z) mod z^2 + N/m;
     Thm 4.5 restated: for N = 1 mod 4, Jacobi (h'/N) = -1  <=>  some cluster variable = 0 mod 4.
 (2) all primes 5 <= p <= PMAX: Type II cube points (c,d,j) <-> words (c,4dj,s) at pj <-> CM point
     z^2 = -p/(4d); for d = 1: the V_p pencil member mu = pj + c has N_mu(1+2j w) = -h, h | mu, and the
     CF of sqrt(4 mu^2 - 4p) has Q_3 = h (mu > 2p) / Q_1 = h (mu <= 2p).
 Odd squares: control (no word with a cluster variable = 0 mod 4 when N = 1 mod 4).
"""
import sys
from fractions import Fraction as F
from math import isqrt


def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def check_words(NMAX):
    nw = 0; bad = 0; sq_hits = 0; slice_words = 0
    for m in range(2, NMAX + 1):
        for c in range(2, NMAX + 1):
            if m * c * 2 - c - 2 > NMAX:
                break
            for s in range(2, NMAX + 1):
                N = m * c * s - c - s
                if N > NMAX:
                    break
                nw += 1
                h, hp = c * m - 1, m * s - 1
                V = [(0, -1), (1, 0), (c, 1), (h, m), (N, hp)]  # Farey path, HJ convergents
                sides = [det(V[i], V[i + 1]) for i in range(4)]
                if sides != [1, 1, 1, 1] or abs(det(V[4], V[0])) != N:
                    bad += 1
                diag = {(0, 2): c, (1, 3): m, (2, 4): s, (0, 3): h, (1, 4): hp}
                for (i, k), val in diag.items():
                    if abs(det(V[i], V[k])) != val:
                        bad += 1
                pt = [c * m == h + 1, m * s == hp + 1, h * hp == m * N + 1, h * s == N + c, c * hp == N + s]
                if not all(pt):
                    bad += 1
                # Machin-CM: (c+z)(s+z) - (c+s)(1/m+z) = z^2 + cs - (c+s)/m  must equal z^2 + N/m
                if F(c * s) - F(c + s, m) != F(N, m):
                    bad += 1
                # Penner h-length (Farey-telescoping) identities at the five vertices, divided by N
                hv = [F(hp, N) == F(1, c) + F(1, c * h) + F(1, h * N),          # V1, opp. diag h'
                      F(c, N) == F(1, hp) + F(1, hp * m * N) + F(1, m * N),     # V2, opp. diag c
                      F(m, N) == F(1, c * s) + F(1, c * N) + F(1, s * N),       # V3, opp. diag m
                      F(s, N) == F(1, h) + F(1, h * m * N) + F(1, m * N),       # V4, opp. diag s
                      F(h, N) == F(1, s) + F(1, s * hp) + F(1, hp * N)]         # V5, opp. diag h
                if not all(hv):
                    bad += 1
                if N % 2 == 1 and N % 4 == 1:
                    j = jacobi(hp, N)
                    four = any(x % 4 == 0 for x in (c, m, s, h, hp))
                    if (j == -1) != four:
                        bad += 1
                    r = isqrt(N)
                    if r * r == N and four:
                        sq_hits += 1
                    if four:
                        slice_words += 1
    return nw, slice_words, bad, sq_hits


def primes_upto(n):
    sv = bytearray([1]) * (n + 1); sv[0:2] = b'\x00\x00'
    for i in range(2, isqrt(n) + 1):
        if sv[i]:
            sv[i * i::i] = bytearray(len(sv[i * i::i]))
    return [i for i in range(n + 1) if sv[i]]


def cf_Q(Nn, kmax):
    """complete-quotient denominators Q_1..Q_kmax of sqrt(Nn) (Nn non-square)."""
    a0 = isqrt(Nn); m, q, a = 0, 1, a0; Qs = []
    for _ in range(kmax):
        m = q * a - m; q = (Nn - m * m) // q; a = (a0 + m) // q
        Qs.append(q)
    return Qs


def check_typeII(PMAX):
    bad = 0; npts = 0; nd1 = 0
    for p in primes_upto(PMAX):
        if p < 5:
            continue
        for c in range(1, p + 2):
            for d in range(1, (p + 1) // (3 * c) + 1):
                # (c,d)-line: h | p + 4c^2 d, h = 4cdj - 1
                Nn = p + 4 * c * c * d
                # enumerate divisors h = -1 mod 4cd
                mod = 4 * c * d
                for h in range(mod - 1, Nn + 1, mod):
                    if Nn % h:
                        continue
                    j = (h + 1) // mod
                    if (p * j + c) % h:
                        bad += 1; continue
                    s = (p * j + c) // h
                    npts += 1
                    m = 4 * d * j
                    if m * c * s - c - s != p * j:
                        bad += 1
                    # Machin / CM point: cs - (c+s)/m == p/(4d)
                    if F(c * s) - F(c + s, m) != F(p, 4 * d):
                        bad += 1
                    if d == 1:
                        nd1 += 1
                        mu = p * j + c
                        if 1 - 4 * j * mu + 4 * j * j * p != -h or mu % h:
                            bad += 1
                        f = mu * mu - p
                        r = isqrt(4 * f)
                        if r * r != 4 * f:
                            Qs = cf_Q(4 * f, 3)
                            k = 3 if mu > 2 * p else 1
                            if Qs[k - 1] != h:
                                bad += 1
    return npts, nd1, bad


def check_controls(NMAX):
    """n = 105 and odd squares: interior words and whether any has a cluster variable = 0 mod 4."""
    from collections import Counter
    cnt = Counter(); four = Counter()
    for m in range(2, NMAX + 1):
        for c in range(2, NMAX + 1):
            if 2 * m * c - c - 2 > NMAX:
                break
            for s in range(2, NMAX + 1):
                N = m * c * s - c - s
                if N > NMAX:
                    break
                r = isqrt(N)
                if N == 105 or (N % 2 and r * r == N):
                    cnt[N] += 1
                    if any(x % 4 == 0 for x in (c, m, s, c * m - 1, m * s - 1)):
                        four[N] += 1
    return cnt.get(105, 0), sum(1 for k in cnt if k != 105), sum(four.values())


if __name__ == '__main__':
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    PMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 500
    w = check_words(NMAX); t = check_typeII(PMAX); c = check_controls(NMAX)
    print('words (#words, #slice words N=1(4), failures, slice words at odd squares)', w)
    print('typeII (#cube points, #d=1, failures)', t)
    print('controls (words at 105, #odd squares with words, #slice words at controls)', c)
    sys.exit(1 if (w[2] or w[3] or t[2] or c[0] or c[2]) else 0)
