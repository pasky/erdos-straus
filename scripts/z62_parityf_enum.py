"""Enumerate all solutions of 4/n = 1/x+1/y+1/z (x<=y<=z), classify by which denominators n divides.
Also count (*) solutions R(n) = #{(u,B,C): 4uBC-u-B = n} and shape2 R2(n) = #{(a,b,c,d): 4abcd = a+b+nc}."""
import sys
from math import gcd, isqrt
from sympy import isprime, divisors

def es_solutions(n):
    sols = []
    # x in (n/4, 3n/4]
    for x in range(n//4 + 1, (3*n)//4 + 1):
        # 4/n - 1/x = (4x-n)/(nx) = 1/y + 1/z, y<=z, y >= x
        num = 4*x - n; den = n*x
        # (num*y - den)(num*z - den) = den^2 ; y >= x, y <= 2*den/num
        ymin = x; ymax = (2*den)//num
        for y in range(ymin, ymax+1):
            t = num*y - den
            if t <= 0: continue
            if (den*y) % t == 0:
                z = den*y // t
                if z >= y: sols.append((x,y,z))
    return sols

def R_star(n):
    cnt = 0; sols=[]
    C = 1
    while (4*C-1)**2 <= 4*C*n+1:
        N = 4*C*n+1
        for d in divisors(N):
            if d % (4*C) == 4*C-1:
                u = (d+1)//(4*C); B = (N//d + 1)//(4*C)
                sols.append((u,B,C)); cnt += 1
        C += 1
    return cnt, sols

if __name__ == "__main__":
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    for n in range(lo, hi+1):
        if n % 4 != 1: continue
        sols = es_solutions(n)
        types = {}
        for (x,y,z) in sols:
            k = sum(1 for v in (x,y,z) if v % n == 0)
            types[k] = types.get(k,0)+1
        rs, _ = R_star(n)
        tag = 'P' if isprime(n) else ('SQ' if isqrt(n)**2==n else 'C')
        print(n, tag, len(sols), dict(sorted(types.items())), rs)
