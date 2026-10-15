"""R228: Remark 2.4 even-A check on u-side predicted-clean levels, k = 0 mod 4 (K odd), relaxed genericity.
Counts even-A words and those with chi = -1 (Jacobi, all n), split by u mod 4."""
import sys
from math import gcd
sys.argv=['x','1','1','1','1']
src=open(__file__.replace('review_r228_evenA2.py','review_r228_signfield.py')).read().rsplit('\nmain()',1)[0]
exec(src)
from sympy import divisors
KMAX, UMAX, MMAX = 60, 150, 400
stat={1:[0,0,0],3:[0,0,0]}
for k in range(4, KMAX+1, 4):
    for u in range(1, UMAX+1, 2):
        if not F_in_Sigma(sqfree(k+u), u): continue
        r=u%4; stat[r][0]+=1
        b=k+u
        for m in range(1, MMAX+1, 2):
            g=gcd(m,b)
            if g!=1: continue
            n=m*m+k; N=n+u
            for A in divisors(N):
                if A%2 or (A+1)%u: continue
                stat[r][1]+=1
                if jacobi_symbol(A%n,n)==-1: stat[r][2]+=1; print("FAIL",k,u,m,A)
print("u mod 4 -> [levels, even-A words, chi=-1]:", stat)
