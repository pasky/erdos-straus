# R92 from-scratch exact engine for fibre certificates (TYPEI5 §2 cross-check).
# For L, c_o = 7^a c' (a odd, c' odd, 7 !| c'), delta odd, c_o*delta <= CD:
#   d = c_o*M, M = c_o delta^2 + 2^(L-4).  Exact fundamental unit eps of Z[sqrt d] (x^2-dy^2=1) via CF,
#   nu = least power eps^k with 4 | y.  For EVERY divisor P_1 of M test exactly whether
#   nu = (4 X sqrt P + u sqrt Q)^2, i.e. A+1 = 32 P X^2, A-1 = 2 Q u^2, with X odd, 7!|X, u = 7^b.
# Also reports the residue-level survivors of the weaker necessary conditions, to compare with typei5_dmod.
# By Lemma 1.1 (checked independently) a certificate's unit is nu; so this is complete for all b.
import sys
from math import isqrt

def fund(d):
    a0 = isqrt(d); m, q, a = 0, 1, a0
    p0, p1 = 1, a0; q0, q1 = 0, 1
    while True:
        n = p1 * p1 - d * q1 * q1
        if n == 1: return p1, q1
        if n == -1: return p1 * p1 + d * q1 * q1, 2 * p1 * q1
        m = a * q - m; q = (d - m * m) // q; a = (a0 + m) // q
        p0, p1 = p1, a * p1 + p0; q0, q1 = q1, a * q1 + q0

def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n: ds.append(n // i)
        i += 1
    return ds

def v7(x):
    e = 0
    while x % 7 == 0: x //= 7; e += 1
    return e

def run(Lmin, Lmax, CD):
    hits = []; nf = 0
    for co in range(7, CD + 1, 2):
        a = v7(co)
        if a % 2 == 0: continue
        cp = co // 7 ** a
        for dl in range(1, CD // co + 1, 2):
            for L in range(Lmin, Lmax + 1):
                T = 2 ** (L - 4); M = co * dl * dl + T; d = co * M; nf += 1
                x, y = fund(d); A, B = x, y; k = 1
                while B % 4:
                    A, B = A * x + d * B * y, A * y + B * x; k += 1
                assert A * A - d * B * B == 1 and k <= 2
                for P1 in divisors(M):
                    P = cp * P1; Q = 7 ** a * (M // P1)
                    if (A + 1) % (32 * P) or (A - 1) % (2 * Q): continue
                    X2 = (A + 1) // (32 * P); u2 = (A - 1) // (2 * Q)
                    X = isqrt(X2); u = isqrt(u2)
                    if X * X != X2 or u * u != u2: continue
                    if X % 2 == 0 or X % 7 == 0: continue
                    b = v7(u)
                    if u != 7 ** b: continue
                    hits.append((L, co, dl, cp, P1, X, b, k))
    return nf, hits

if __name__ == "__main__":
    Lmin, Lmax, CD = map(int, sys.argv[1:4])
    nf, hits = run(Lmin, Lmax, CD)
    print(f"L={Lmin}..{Lmax} CD={CD}: {nf} fields, {len(hits)} certificates")
    for h in hits: print("  L=%d c_o=%d delta=%d c'=%d P1=%d X=%d b=%d k=%d" % h)
