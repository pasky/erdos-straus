"""Sanity check for EXCEPTIONAL_MN3 Lemma 3.1 and the twin map: enumerate Type I quadruples
(a,c,d,f) with f | 4a^2 d+1, n = 4acd - f, and check the SL2 identity, n = 2c*M21 - M22,
the sigma_d fixed-point property, ET's identities (2.1)-(2.9) and the twin (b,a,c,d,e,f')."""
from math import gcd
N = 600; cnt = 0
for a in range(1, N):
    for d in range(1, N // a + 1):
        m = 4*a*a*d + 1
        for f in range(1, m + 1):
            if m % f: continue
            e = m // f
            for c in range(1, N // (a*d) + 1):
                n = 4*a*c*d - f
                if n <= 0 or n > N: continue
                assert (n*a + c) % f == 0  # automatic from f | 4a^2d+1, n = 4acd - f
                b = c*e - a
                if b <= 0: continue
                M = ((e, 2*a), (2*a*d, f))
                assert M[0][0]*M[1][1] - M[0][1]*M[1][0] == 1
                assert M[1][0] == d*M[0][1] and n == 2*c*M[1][0] - M[1][1]
                assert 4*a*b*d == n*e + 1 and b*f == n*a + c and 4*a*b*c*d == n*a + n*b + c
                fp = 4*b*c*d - n
                assert fp > 0 and e*fp == 4*b*b*d + 1 and f*fp == n*n + 4*c*c*d
                # 1/n-type check: 4/n = 1/x+1/y+1/z with (x,y,z)=(abdn, acd, bcd)
                x, y, z = a*b*d*n, a*c*d, b*c*d
                assert 4*x*y*z == n*(y*z + x*z + x*y)
                cnt += 1
print("checked", cnt, "Type I points with n <=", N, ": all identities hold")
