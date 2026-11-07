"""S_p = {(k, eps, y, z): k odd, eps in {1,p}, 4k/(pk+eps) = 1/y + 1/z, y<=z}.
ES elements are k = 3 mod 4. Print counts split by k mod 4 and eps."""
import sys
from math import gcd
from sympy import isprime, divisors

def two_unit(m, N):
    """all (y,z) y<=z with m/N = 1/y+1/z (m,N positive, not nec. coprime)."""
    g = gcd(m, N); m //= g; N //= g
    out = []
    for d in divisors(N*N):
        if d > N: break
        if (d + N) % m == 0 and (N*N//d + N) % m == 0:
            y = (d + N)//m; z = (N*N//d + N)//m
            out.append((y, z))
    return out

def Sset(p, kmax=None):
    res = []
    k = 1
    while True:
        found_any = False
        for eps in (1, p):
            num, den = 4*k, p*k + eps
            sols = two_unit(num, den)
            for (y, z) in sols:
                res.append((k, eps, y, z))
        # bound: y in (p/4, p]; z = p(k+1)y/(k(4y-p)-p) integrality implies k bounded ~ 4p^3; use crude bound
        k += 2
        if kmax and k > kmax: break
    return res

if __name__ == "__main__":
    for p in map(int, sys.argv[1:]):
        kmax = 4*p**3 + 10
        S = Sset(p, kmax)
        c = {}
        for (k, eps, y, z) in S:
            key = (k % 4, 'p' if eps == p else '1')
            c[key] = c.get(key, 0) + 1
        print("p=%d |S|=%d" % (p, len(S)), dict(sorted(c.items())))
        if p <= 30:
            for r in S: print("   ", r)
