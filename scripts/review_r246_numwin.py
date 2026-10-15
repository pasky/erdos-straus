# R246: does the window SHAPE (x = K, y = nA, z = nKA/d, d | K^2, d = -K mod m, m = nu*K - n) admit integral
# (cap-0) solutions at odd squares n = a^2 for nu = 3, 7, 9, 11, 19 (where the memo proves no FORCED window exists)?
# Restrict to windows of the forced shape: m odd, every prime factor = 3 (mod 4), gcd(m, n) = 1. Control nu = 4.
import sys
from math import gcd
def fac(n):
    f = {}; d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d, 0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f
def divs(f):
    D = [1]
    for p, e in f.items(): D = [x*p**k for x in D for k in range(e+1)]
    return D
A_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 60; MMAX = 400
for nu in (3, 4, 7, 9, 11, 19):
    hits = []
    for a in range(3, A_MAX, 2):
        if gcd(a, nu) > 1: continue
        n = a*a
        for K in range(n//nu + 1, (n + MMAX)//nu + 1):
            m = nu*K - n
            if m <= 0 or m % 2 == 0 or gcd(m, n) > 1 or any(q % 4 != 3 for q in fac(m)): continue
            fK = fac(K)
            for d in divs({p: 2*e for p, e in fK.items()}):
                if (K + d) % m: continue
                A = (K + d)//m
                if (n*K*A) % d == 0:
                    x, y, z = K, n*A, n*K*A//d
                    assert nu*x*y*z == n*(x*y + y*z + z*x)
                    hits.append((a, m, x, y, z)); break
            if hits and hits[-1][0] == a: break
    print(f"nu={nu}: squares a^2 (a<{A_MAX}) with an integral forced-shape window solution: {len(hits)}; e.g. {hits[:2]}")
