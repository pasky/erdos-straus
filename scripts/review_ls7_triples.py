"""R73 from-scratch check of LS7 Lemmas 1.1, 1.2 (M ≡ 3 mod 4, M < MMAX).

Lemma 1.1: {−4D mod M : D | A²} == {−u/v mod M : gcd(u,v)=1, uv | A}, bijection D <-> (u,v),
D = u²t, A²/D = v²t, and −4D ≡ −u/v ≡ −4u²t ≡ −1/(4v²t) (mod M).
H* bound: brute-force least label height H*(class) <= min(max(u,v), 4u²t, 4v²t), for M < HMAX.
Lemma 1.2: for prime p | M: p ∤ uvt, 4uvt ≡ 1, u ≡ −a v, v²t ≡ −1/(4a), u²t ≡ −a/4 (mod p).
"""
import sys
from math import gcd
import numpy as np
from sympy import divisors, primefactors

MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
HMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 4000


def hstar(b, M):
    s = np.arange(1, M + 1, dtype=np.int64)
    r = (-b * s) % M
    ok = np.gcd(s, M) == 1
    h = np.maximum(r, s)[ok]
    return int(h.min())


bad = 0
ntrip = 0
nhs = 0
tight = 0
for M in range(3, MMAX, 4):
    A = (M + 1) // 4
    divA2 = divisors(A * A)
    R1 = {(-4 * D) % M for D in divA2}
    pairs = []
    for u in divisors(A):
        for v in divisors(A // u):
            if gcd(u, v) == 1:
                pairs.append((u, v))
    R2 = {(-u * pow(v, -1, M)) % M for u, v in pairs}
    if R1 != R2:
        bad += 1; print("R mismatch", M)
    # bijection
    Ds = sorted(A * u // v for u, v in pairs if (A * u) % v == 0)
    if len(Ds) != len(pairs) or sorted(Ds) != sorted(divA2):
        bad += 1; print("bijection fail", M)
    ps = primefactors(M)
    for u, v in pairs:
        t = A // (u * v)
        D = A * u // v
        if D != u * u * t or A * A // D != v * v * t:
            bad += 1; print("D formula", M, u, v)
        c = (-4 * D) % M
        l1 = (-u * pow(v, -1, M)) % M
        l2 = (-4 * u * u * t) % M
        l3 = (-pow(4 * v * v * t, -1, M)) % M
        if not (c == l1 == l2 == l3):
            bad += 1; print("label fail", M, u, v)
        if M < HMAX:
            hs = hstar(c, M)
            nhs += 1
            bnd = min(max(u, v), 4 * u * u * t, 4 * v * v * t)
            if hs > bnd:
                bad += 1; print("H* bound fail", M, u, v, hs, bnd)
            if hs == bnd:
                tight += 1
        for p in ps:
            ntrip += 1
            if (u * v * t) % p == 0 or (4 * u * v * t) % p != 1:
                bad += 1; print("1.2 unit fail", M, p, u, v, t)
                continue
            a = c % p
            ia = pow(a, -1, p)
            if (u + a * v) % p or (v * v * t + pow(4 * a, -1, p)) % p or (4 * u * u * t + a) % p:
                bad += 1; print("1.2 pin fail", M, p, u, v, t)
print(f"MMAX={MMAX} HMAX={HMAX} prime-triples={ntrip} H*-checks={nhs} tight={tight} failures={bad}")
# Remark (a) example
M = 167
print("M=167 class -36:", (-36) % M, "H*=", hstar(-36 % M, M), "check -13/5:", (-13 * pow(5, -1, M)) % M)
