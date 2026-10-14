# y7 (O215): Mordell-type covering of residue classes mod L by ET-shaped one-parameter identity families of M/n.
# Families (no coprimality needed; identities checked symbolically in the memo y7_mordell_levels):
#  II-d: n = M a b d - e, e | a+b                     -> n ≡ -e        (mod M a b)
#  II-c: b = c e - a:  n ≡ -M a^2 d - e                (mod M a d e)
#  II-e: b = c e - a:  n ≡ -M a^2 d                    (mod M a c d - 1)
#  I-d : n e + 1 = M a b d, e | a+b, gcd(e,Mab)=1      -> n ≡ -e^{-1}   (mod M a b)
#  I-c : b = c e - a, e | M a^2 d + 1                   -> n ≡ -(M a^2 d+1)/e (mod M a d)
import sys
from math import gcd
def divisors(x):
    return [d for d in range(1,x+1) if x%d==0]
def cover(M,L):
    assert L%M==0
    U=[r for r in range(L) if gcd(r,L)==1]
    cov=set()
    def add(cls,q):
        if q<=0 or L%q: return
        cls%=q
        for r in range(cls,L,q):
            if gcd(r,L)==1: cov.add(r)
    D=divisors(L)
    for q in D:
        if q%M==0:
            ab=q//M
            for a in divisors(ab):
                b=ab//a
                for e in divisors(a+b):
                    add(-e,q)
                    if gcd(e,q)==1: add(-pow(e,-1,q),q)
    for q in D:  # II-c: q = M a d e
        if q%M: continue
        r=q//M
        for a in divisors(r):
            for d in divisors(r//a):
                e=r//(a*d)
                add(-M*a*a*d-e,q)
        # I-c: q = M a d
        for a in divisors(r):
            d=r//a; t=M*a*a*d+1
            for e in divisors(t):
                if q>0: add(-(t//e),q)
    for g in D:  # II-e: g = M a c d - 1
        if (g+1)%M: continue
        acd=(g+1)//M
        for a in divisors(acd):
            for d in divisors(acd//a):
                add(-M*a*a*d,g)
    unc=[r for r in U if r not in cov and r%M!=0]
    return U,unc
def is_sq_mod(r,L):
    return any((x*x-r)%L==0 for x in range(L))
if __name__=="__main__":
    M=int(sys.argv[1])
    for L in map(int,sys.argv[2:]):
        U,unc=cover(M,L)
        sq=[r for r in unc if is_sq_mod(r,L)]
        allsq=[r for r in U if is_sq_mod(r,L)]
        print(f"M={M} L={L} units={len(U)} uncovered={len(unc)} (squares among them {len(sq)}/{len(allsq)} unit squares)", unc[:24])
