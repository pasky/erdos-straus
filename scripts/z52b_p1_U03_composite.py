"""z52b Pass-1 U03 (Z1527/Z1575/Z0946): R_K(n)=sum_{C<=K} #{d | 4Cn+1 : d = -1 (4C)} for all odd n<=NMAX (K=100).
Reports: composite n = 1 mod 4 with R_K(n)=0 ('C-form exceptions' up to K), multiples of 409, and n in {33,105,385,1155,15015}.
Usage: uv run python scripts/z52b_p1_U03_composite.py NMAX"""
import sys, json
from math import isqrt
NMAX = int(sys.argv[1]); K = 100
M = 4 * K * NMAX + 2
spf = list(range(M + 1))
for i in range(2, isqrt(M) + 1):
    if spf[i] == i:
        for j in range(i * i, M + 1, i):
            if spf[j] == j: spf[j] = i
def factor(n):
    f = {}
    while n > 1:
        q = spf[n]; f[q] = f.get(q, 0) + 1; n //= q
    return f
def ndiv_m1(f, m):
    ds = [1]
    for q, e in f.items(): ds = [x * q**k for x in ds for k in range(e + 1)]
    return sum(1 for x in ds if x % m == m - 1)
def RK(n):
    tot = 0
    for C in range(1, K + 1):
        if 4 * C > 4 * n: break
        tot += ndiv_m1(factor(4 * C * n + 1), 4 * C)
    return tot
res = {}
zeros = []
for n in range(5, NMAX + 1, 4):
    r = RK(n); res[n] = r
    if r == 0 and n > 1 and len(factor(n)) > 1: zeros.append(n)
print("composite n=1 mod 4, n<=", NMAX, ": R_100(n)=0 count:", len(zeros), zeros[:30])
print("R_100 for 409*k (k=1 mod 4 odd), k<=25:", [(409 * k, res.get(409 * k, RK(409 * k))) for k in [1, 9, 25, 49, 81]])
print("R_100 for 3681(=9*409), 10225(=25*409):", RK(3681), RK(10225))
print("Z0946 n=105,385,33,1155,15015:", {n: RK(n) for n in [33, 105, 385, 1155, 15015]} if NMAX >= 15015 else {n: RK(n) for n in [33,105,385]})
json.dump({"zeros": zeros}, open("data/z52b/pass1/U03/composite_zeros.json", "w"))
