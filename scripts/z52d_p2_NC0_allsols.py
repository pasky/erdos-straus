# z52d Pass 2 NC0 — exhaustive list of unordered solutions 4/n = 1/x+1/y+1/z (x<=y<=z) for small n (python, exact).
import sys
from math import gcd
def sols(n, m=4):
    out=[]
    for x in range(n//m+1, 3*n//m+1):
        a=m*x-n; b=n*x
        if a<=0: continue
        g=gcd(a,b); A=a//g; B=b//g
        # 1/y+1/z = A/B  -> (A y - B)(A z - B) = B^2 ; need y>=x
        B2=B*B
        d=1
        # enumerate divisors d of B^2 with d<=B (so y<=z)
        from sympy import divisors
        for d in divisors(B2):
            if d> B: continue
            if (d+B)%A: continue
            y=(d+B)//A
            if y<x: continue
            z=((B2//d)+B)//A
            out.append((x,y,z))
    return sorted(set(out))
if __name__=='__main__':
    n=int(sys.argv[1])
    S=sols(n)
    print(n, len(S))
    for s in S: print(s, [t for t in s if t%3==0] and 'has3' or '-')
