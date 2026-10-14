"""Brute-force test of Lemma 1.3 / Cor 1.4 (STERILE_EXPLICIT.md): exact-integer evaluation of (Cop),
compared with the true number of divisors of n in a residue class and window. Fails loudly on a violation."""
import random, math, sys
from fractions import Fraction
from sympy import divisors
def cop_ok(n,s,D0,D1,m,k,J):
    w=m+k; X=Fraction(D1-D0,2*s*J)+Fraction(1,2)
    # w^w n^{m(m+1)/2} X^{w(w-1)/2} < D0^{m w}
    return w**w * n**(m*(m+1)//2) * X**(w*(w-1)//2) < Fraction(D0)**(m*w)
def bound(n,s,D0,D1,W=10,Jmax=64):
    best=(D1-D0)//s+1
    for J in range(1,Jmax+1):
        if J>=best: break
        for w in range(2,W+1):
            if J*(w-1)>=best: break
            for m in range(1,w+1):
                if cop_ok(n,s,D0,D1,m,w-m,J): best=min(best,J*(w-1)); break
    return best
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 1)
P=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]
viol=0; tests=0; tight=0
for it in range(int(sys.argv[2]) if len(sys.argv)>2 else 300):
    n=1
    while n<10**9: n*=random.choice(P)
    ds=divisors(n)
    s=random.randint(2,int(n**0.4)+2)
    D0=random.choice(ds); D0=max(1,D0//random.randint(1,4)); D1=D0*random.choice([2,3,4])
    sig=random.choice([d for d in ds if D0<=d<=D1] or [1])%s
    if math.gcd(sig,s)!=1: continue
    true=sum(1 for d in ds if D0<=d<=D1 and d%s==sig)
    b=bound(n,s,D0,D1); tests+=1
    if true>b: viol+=1; print("VIOLATION",n,s,sig,D0,D1,true,b)
    if true==b: tight+=1
print("tests",tests,"violations",viol,"tight",tight)
sys.exit(1 if viol else 0)
