# summarise cf_census output: n W Nminus (all odd n)
import math, sys
from sympy import isprime
zero=[];sqbad=[];mins=(9,0);ratios=[];sqW=[]
for line in open(sys.argv[1]):
    n,W,M=map(int,line.split())
    r=math.isqrt(n)
    if r*r==n:
        sqW.append(W)
        if M>0: sqbad.append(n)
        continue
    if M==0: zero.append((n,W))
    if n%8==1 and isprime(n):
        ratios.append(M/W)
        if M/W<mins[0]: mins=(M/W,n,W,M)
print("non-square odd n with no chi=-1 word (n, |X_n|):",zero)
print("odd squares:",len(sqW),"with a chi=-1 word:",sqbad,"mean |X|",sum(sqW)/len(sqW))
print("primes 1 mod 8:",len(ratios),"mean N-/W %.4f"%(sum(ratios)/len(ratios)),"min",mins)
