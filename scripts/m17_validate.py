"""Soundness check for m17_enum (POINTWISE_MORDELL17 §3): rebuild genuine ET classes from the
enumerated data and check, with mordell_lib, that each class contains the 17-generic points of the
claimed box and that solve() gives a valid ES solution at a prime in the class.
usage: m17_validate.py  (uses small levels: Q,U k=3, P K=3,5)"""
import random
from math import gcd
from sympy import isprime
from mordell_lib import cls_modulus_residues, solve

def tf(m):
    while m % 17 == 0:
        m //= 17
    return m

def check(fam, P, k, r):
    M, Rs = cls_modulus_residues(fam, P)
    F = 17 ** k
    assert M % F == 0 and (M // F) % 17 != 0, (fam, P, M)
    N = M // F
    good = [x for x in Rs if x % N == 1 % N and x % F == r % F]
    assert good, (fam, P, r)
    x0 = good[0]
    for t in range(1, 10 ** 6):          # a prime p in the class, p > 10^6
        p = x0 + M * t
        if p > 10 ** 6 and isprime(p):
            assert solve(fam, P, p) is not None, (fam, P, p)
            return

def typeI(n):      # N-points of Sigma^I_n, a <= b
    for a in range(1, n):
        for d in range(1, 3 * n // (4 * a) + 1):
            for c in range(n // (4 * a * d) + 1, 3 * n // (4 * a * d) + 1):
                f = 4 * a * c * d - n
                if f <= 0 or (4 * a * a * d + 1) % f or (n * a + c) % f:
                    continue
                b = (n * a + c) // f
                if b >= a and (a + b) % c == 0:
                    yield a, b, c, d

def typeII(n):
    for a in range(1, n):
        for d in range(1, n // (2 * a * a) + 1):
            for c in range(1, n // (a * d) + 1):
                f = 4 * a * c * d - 1
                if (n + 4 * a * a * d) % f:
                    continue
                e = (n + 4 * a * a * d) // f
                b = c * e - a
                if b >= a:
                    yield a, b, c, d

cnt = 0
for k in (1, 3):
    F = 17 ** k
    for a, b, c, d in typeI(F):
        e = (a + b) // c
        if e % 17 == 0:
            continue
        for A, B in ((a, b), (b, a)):
            f = 4 * A * B * d - 1                     # II2 class (A, d, f): box -4A^2 d
            check('II2', (A, d, f), k, -4 * A * A * d); cnt += 1
for K in (1, 3, 5):
    N = 17 ** K
    for a, b, c, d in typeII(N):
        if c % 17 == 0 or d % 17 == 0:
            continue
        for A in (a, b):
            f = 4 * A * c * d - 1
            for al in range(0, K // 2 + 1):
                aa, dd = 17 ** al * c, 17 ** (K - 2 * al) * d   # I1 class (aa, dd, f), level K-al
                check('I1', (aa, dd, f), K - al, -f); cnt += 1
for k in (1, 3):                                   # U: II1 class (a,b,e), box -e; I4 box -1/e
    F = 17 ** k
    for i in range(1, F):
        for u in range(1, F):
            if 4 * i * u * u > 3 * F: break
            for v in range(u, 3 * F // (4 * i * u) + 1):
                D = 4 * i * u * v - F
                if D <= 0 or (F * (u + v)) % D: continue
                w = F * (u + v) // D
                if w < v: continue
                for c, a, b in ((u, v, w), (v, u, w), (w, u, v)):
                    if (a * b) % F or (a * b // F) % 17 == 0 or (a + b) % c: continue
                    e = (a + b) // c
                    if gcd(e, 4 * a * b) != 1: continue
                    check('II1', (a, b, e), k, -e); check('I4', (a, b, e), k, -pow(e, -1, F)); cnt += 2
print("validated", cnt, "classes: OK")
