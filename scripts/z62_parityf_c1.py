"""S_n = {(g,a,b): gab = a+b+n}, S'_n = {(g,a,b): gab = n(a+b)+1}.
Count elements, elements with 4|g (ES Type II c=1, resp. Type I c=1).
Also count by g mod 4."""
import sys
from math import isqrt
from sympy import isprime, divisors, primerange

def S_II(n):
    # gab = a+b+n  <=> (ga-1)(gb-1) = gn+1 ; enumerate g, then divisors d of gn+1 with d = -1 mod g
    out = []
    g = 1
    while (g-1)**2 <= g*n+1:   # need a,b>=1: ga-1 >= g-1
        N = g*n+1
        for d in divisors(N):
            if d % g == (g-1) % g:
                a = (d+1)//g; b = (N//d+1)//g
                if a>=1 and b>=1: out.append((g,a,b))
        g += 1
    return out

def S_I(n):
    # gab = n(a+b)+1 <=> (ga-n)(gb-n) = n^2+g ; a,b>=1, ga-n can be any divisor d of n^2+g with d = -n mod g, d>0 (then ga = d+n)
    out = []
    g = 1
    # bound: a*b*g = n(a+b)+1 ; with a<=b: gab <= 2nb+1 -> ga <= 2n + 1/b  -> g <= 2n+1
    while g <= 2*n+1:
        N = n*n+g
        for d in divisors(N):
            if (d + n) % g == 0 and (N//d + n) % g == 0:
                a = (d+n)//g; b = (N//d+n)//g
                out.append((g,a,b))
        g += 1
    return out

if __name__ == "__main__":
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    for n in range(lo, hi+1):
        if n % 4 != 1: continue
        tag = 'P' if isprime(n) else ('SQ' if isqrt(n)**2==n else 'C')
        if tag == 'C' and n % 24 != 1: continue
        A = S_II(n); B = S_I(n)
        a4 = sum(1 for (g,a,b) in A if g%4==0); b4 = sum(1 for (g,a,b) in B if g%4==0)
        am = [sum(1 for (g,a,b) in A if g%4==r) for r in range(4)]
        bm = [sum(1 for (g,a,b) in B if g%4==r) for r in range(4)]
        print(n, tag, n%24, "|S|=%d ES2=%d mod4=%s" % (len(A), a4, am), "|S'|=%d ES1=%d mod4=%s" % (len(B), b4, bm), "NONE" if a4+b4==0 else "")
