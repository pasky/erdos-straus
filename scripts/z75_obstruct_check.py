"""Independent exact checker: partition by order of the three coordinates, no factoring.
Also establish primality by trial division. Stdlib only. n odd <= 10^12 recommended.
"""
from math import isqrt
import sys


def check(n, k):
    # sort the symmetric coordinates u <= b; now partition by position of c
    ans = []
    for u in range(1, isqrt(n)+2):
        if k*u**3-2*u > n:
            break
        # u <= b <= c: k*u*b^2 - b - (n+u) <= 0
        for b in range(u, (1+isqrt(1+4*k*u*(n+u)))//(2*k*u)+1):
            c, z = divmod(n+u+b, k*u*b)
            if not z:
                ans.append((u,b,c))
        # u <= c < b: c*(k*u*c-1) < n+u
        for c in range(u, (1+isqrt(1+4*k*u*(n+u-1)))//(2*k*u)+1):
            b, z = divmod(n+u, k*u*c-1)
            if not z:
                ans.append((u,b,c))
    # c < u <= b: k*c*u^2-2u <= n
    for c in range(1, isqrt(n)+2):
        hi = (1+isqrt(1+k*c*n))//(k*c)
        if hi <= c:
            break
        for u in range(c+1, hi+1):
            b, z = divmod(n+u,k*c*u-1)
            if not z:
                ans.append((u,b,c))
    assert len(set(ans)) == len(ans)
    assert all(u<=b and k*u*b*c-u-b==n for u,b,c in ans)
    return sorted(ans)


if __name__=='__main__':
    for n in map(int,sys.argv[1:]):
        assert n>=2 and all(n%i for i in range(2,isqrt(n)+1))
        for k in (4,8):
            rows=check(n,k)
            print(n,'prime',k,'unordered',len(rows),'first',rows[:1],flush=True)
