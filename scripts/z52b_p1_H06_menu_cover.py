"""Z2323: which unit classes r mod M (r ≡ 1 mod 4) are covered by the Type I/II families of
scripts/z52b_dividing_leastfam.py whose modulus divides M?  Compare the uncovered set with the square classes mod M.
Type I (a,d): n ≡ -f (mod 4ad), f | 4a^2 d + 1.  Type II (a,b): n ≡ -e (mod 4ab), e | a + b."""
import sys
from math import gcd
from sympy import divisors
def run(M):
    cov=set()
    for m4 in divisors(M):
        if m4%4: continue
        s=m4//4
        for a in divisors(s):
            d=s//a
            for f in divisors(4*a*a*d+1):
                r=(-f)%m4
                cov.update(range(r,M,m4))
            b=d
            for e in divisors(a+b):
                if gcd(a,b)!=1: continue
                r=(-e)%m4
                cov.update(range(r,M,m4))
    units=[r for r in range(1,M) if gcd(r,M)==1 and r%4==1]
    sq={(x*x)%M for x in range(M) if gcd(x,M)==1}
    unc=[r for r in units if r not in cov]
    print('M=%d units≡1(4)=%d uncovered=%d squares=%d uncovered==squares:%s nonsquare-uncovered=%d square-covered=%d'%(
        M,len(units),len(unc),len(sq),set(unc)==sq,len(set(unc)-sq),len(sq&cov)))
    return unc
for M in map(int,sys.argv[1:]): run(M)

def covered_set(M):
    cov=set()
    for m4 in divisors(M):
        if m4%4: continue
        s=m4//4
        for a in divisors(s):
            d=s//a
            for f in divisors(4*a*a*d+1):
                r=(-f)%m4; cov.update(range(r,M,m4))
            if gcd(a,d)==1:
                for e in divisors(a+d):
                    r=(-e)%m4; cov.update(range(r,M,m4))
    return cov
