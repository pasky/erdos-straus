# R246: independent ES search (no certificate) for n = 4^s + 105, small s.
# 4/n = 1/x + 1/y + 1/z  <=>  with m = 4x - n > 0, N = n x:  (m y - N)(m z - N) = N^2.
# So find x, and a divisor d | N^2 with d <= N, d = -N (mod m); then y = (N + d)/m, z = (N + N^2/d)/m.
import sys
import sympy as sp

def divisors_from(fac):
    ds = [1]
    for p, e in fac.items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return ds

def es(n, xspan=2000):
    fn = sp.factorint(n)
    for x in range((n + 3)//4 + (1 if n % 4 == 0 else 0), (n + 3)//4 + xspan):
        m = 4*x - n
        if m <= 0: continue
        fac = dict(fn)
        for p, e in sp.factorint(x).items(): fac[p] = fac.get(p, 0) + e
        N = n*x
        fac2 = {p: 2*e for p, e in fac.items()}
        for d in divisors_from(fac2):
            if d <= N and (N + d) % m == 0 and (N + N*N//d) % m == 0:
                y, z = (N + d)//m, (N + N*N//d)//m
                assert 4*x*y*z == n*(x*y + y*z + z*x)
                return x, y, z
    return None

S = int(sys.argv[1]) if len(sys.argv) > 1 else 14
for s in range(S + 1):
    n = 4**s + 105
    r = es(n)
    print(s, n, r)
    assert r is not None
