"""For mixed (2,1,0) solutions of k/p^2: X ≡ 1/k mod p, j=(kX-1)/p; is j/X a sum of
two unit fractions (=> k/p = 1/(pX) + j/X solvable)?"""
import sys
from math import gcd
from sympy import primerange
from z25_common import W, two_term
def v(n,p):
    c=0
    while n%p==0: n//=p; c+=1
    return c
k=int(sys.argv[1]); P=int(sys.argv[2])
for p in primerange(k+1,P):
    good=bad=0
    for s in W(p*p,k):
        vs=[v(t,p) for t in s]
        if min(vs)>0: continue
        x=[t for t in s if v(t,p)>=2][0]; X=x//(p*p)
        j=(k*X-1)//p; assert (k*X-1)%p==0
        g=gcd(j,X); A,B=j//g,X//g
        ok = A==0 or len(two_term(A,B,1))>0 or (A==1)  # A/B=1/B... if A==1 need 1/B=1/u+1/v always ok
        if ok: good+=1
        else: bad+=1
    print(p, 'mixed sols descend:',good,'not:',bad)
