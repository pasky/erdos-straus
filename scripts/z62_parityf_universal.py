"""Universal sets (4 dropped), brute force (safe bounds):
 U_II(n) = {(g,a,b,c): gabc = a+b+nc}   (ES Type II  <=> 4|g);  c(gab-n)=a+b, so ab<=n+a+b -> (a-1)(b-1)<=n+1
 U_I(n)  = {(g,a,b,c): gabc = na+nb+c}  (ES Type I   <=> 4|g);  c(gab-1)=n(a+b): min(a,b)<=2n, and gab-1 | n(ga^2+1) gives b <= (n(ga^2+1)+1)/(ga)
"""
import sys
from math import isqrt
from sympy import isprime

def U_II(n):
    out = set()
    for a in range(1, n+3):
        b = 1
        while (a-1)*(b-1) <= n+1 and b <= 2*n+2:
            for g in range(1, (n+a+b)//(a*b) + 1):
                t = g*a*b - n
                if t > 0 and (a+b) % t == 0:
                    out.add((g,a,b,(a+b)//t))
            b += 1
    return sorted(out)

def U_I(n):
    out = set()
    for a in range(1, 2*n+2):
        for g in range(1, 2*n//a + 3):
            bmax = (n*(g*a*a+1)+1)//(g*a) + 1
            for b in range(1, bmax+1):
                t = g*a*b - 1
                if t > 0 and (n*(a+b)) % t == 0:
                    c = n*(a+b)//t
                    out.add((g,a,b,c)); out.add((g,b,a,c))
    return sorted(out)

if __name__ == "__main__":
    for n in map(int, sys.argv[1:]):
        tag = 'P' if isprime(n) else ('SQ' if isqrt(n)**2==n else 'C')
        A = U_II(n); B = U_I(n)
        a4 = sum(1 for r in A if r[0]%4==0); b4 = sum(1 for r in B if r[0]%4==0)
        ac1 = sum(1 for r in A if r[3]==1); bc1 = sum(1 for r in B if r[3]==1)
        fa = sum(1 for r in A if r[1]==r[2]); fb = sum(1 for r in B if r[1]==r[2])
        print(n, tag, "|U_II|=%d (c=1:%d, a=b:%d) ES2=%d | |U_I|=%d (c=1:%d, a=b:%d) ES1=%d" % (len(A), ac1, fa, a4, len(B), bc1, fb, b4), flush=True)
