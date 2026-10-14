"""si_uvform: check (i) X_n <-> {(u,v): uv | n+u+v}, t=(n+u+v)/(uv), A=(n+u)/v; (ii) chi=(-A/n) equals (-uv/n) when gcd(uv,n)=1;
(iii) N_-(n) >= 1 for n = 3 mod 4 via (1,2,n+2) and n = 5 mod 8 via (1,3,(n+3)/2). usage: si_uvform.py NMAX"""
import sys
from math import gcd
from sympy import jacobi_symbol as J
N = int(sys.argv[1])
bad = cnt = cop = 0
for n in range(1, N + 1, 2):
    for u in range(1, n + 3):
        if (u - 1) * (u - 1) > n + 1 and u > 2:
            pass
        for v in range(1, n + 3):
            if u * v > n + u + v:
                break
            if (n + u + v) % (u * v):
                continue
            t = (n + u + v) // (u * v)
            assert t * u * v - u - v == n
            A = t * u - 1
            assert A >= 1 and (n + u) % v == 0 and (n + u) // v == A
            cnt += 1
            chi = J((-A) % n, n) if n > 1 else 1
            if gcd(u * v, n) == 1:
                cop += 1
                if chi != (J((-u * v) % n, n) if n > 1 else 1):
                    bad += 1
    if n % 4 == 3:
        assert J(n - 1, n) == -1  # word (1,2,n+2), A=1
    if n % 8 == 5:
        assert J(n - 2, n) == -1  # word (1,3,(n+3)/2), A=2
print(f"words={cnt} coprime={cop} mismatches={bad}")
