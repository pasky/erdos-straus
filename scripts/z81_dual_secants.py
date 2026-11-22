"""Fixed-x Vieta and a transverse parameter. Each row is checked by multiplying
rational numbers, not by trusting a genus/residue proxy. b finite bound c<=127;
cap search at no-integral x uses ALL s|g up to exponent 4 for the root.
"""
from fractions import Fraction as F
from math import gcd,lcm, isqrt,prod
from sympy import divisors,factorint,isprime,jacobi_symbol,nextprime
from pathlib import Path
from z81_dual_chords import points
from z46_brauer_twists_check import hilbert

def cands(M,n,B=127):
    out={}; f2= M==8 and n in (11,17,131,241)
    for c in range((-n)%M,B+1,M):
        x=(n+c)//M
        if gcd(x*c,n)>1:continue
        t=F(n*x,c); g=t.numerator;j=t.denominator
        if j<2:continue
        D=divisors(g*g); m=next((d for d in D if d<g and (g-d)%j==0),None)
        if not m: continue
        P=(x,(g-m)//j,-(g*g//m-g)//j);assert min(P)<0<min(P[:2]);
        poss=next((b for b in D if (g+b)%j==0),None)
        if poss: items=[('integral',F(poss*m,g*g))]
        else:items=[]
        if 'cap' not in out and not poss:
            for s in factorint(g):
                if s%2==0 or n%s==0:continue
                for e in range(1,5):
                    h=s**(2*e)
                    # For z'=G+b/(j*h), congruence is g*h+b=0 (mod j).
                    b=next((b for b in D if b%s and (g*h+b)%j==0),None)
                    if b is not None:items.append(('cap',F(m*h,b)));break
                else:continue
                break
        if 'prime' not in out:
            s=next(a for a in range(j-g%j,10**7,j) if isprime(a) and gcd(a,2*n*g)==1 and (not isprime(n) or jacobi_symbol(-M*a,n)==-1))
            items.append(('prime',F(m*s,g*g)))
        for tag,k in items:
            if tag in out or k*g*g==m*m:continue
            W=(x,t+k*g*g/(j*m),t+F(m,j)/k);K=P[0]+P[1]-k*P[2]
            assert W[0]+W[1]-k*W[2]==K and min(W)>0 and W[1].denominator==1
            for R in (P,W):assert sum(F(1,v) for v in R)==F(M,n)
            if tag=='cap':assert isqrt(W[2].denominator)**2==W[2].denominator>1 and all(W[1]%s==0 for s in factorint(W[2].denominator))
            if tag=='prime' and isprime(n):assert hilbert(-F(W[0],W[2]),-F(W[1],W[2]),n)==-1
            r=-k*g*g/(m*m);assert r!=-1
            # Choose ell witnessing non-torsion after specialization on the conic.
            ell=13
            while any(v.numerator%ell==0 or v.denominator%ell==0 for v in map(F,(M,n,x,j,g,m,k,r,*P,*W))) or any((r**i-1).numerator%ell==0 for i in range(1,14)):
                ell=int(nextprime(ell))
            out[tag]=(c,ell,k,P,W)
        if len(out)==3:break
    print(M,n,out,flush=True)

if __name__=='__main__':
    f4=[int(s) for s in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if not s.startswith('#')]
    for n in sorted(set(f4+[25,49,121,2521,3361,102001,8813281,183783601,113035442521,1590284203561,6955940568721,105,1465,3865,4545,10305,12145,39361,67425,17401609])): cands(4,n)
    for n in (11,17,131,241,1590284203561,6955940568721):cands(8,n)
