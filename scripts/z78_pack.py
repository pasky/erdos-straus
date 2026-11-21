"""Knapsack compression of prime-exponent blocks. See R17_PUSH for factor 8."""
from z78_bbr import *
Q=32
primes=[p for p in range(2,2000) if all(p%i for i in range(2,isqrt(p)+1))]
@lru_cache(None)
def penalty(b,h):
    R=1000
    atom=max([R]+[ceildiv(rootup(R**Q*(2*v+1)**h,Q),v+1) for v in range(1,b+1)])
    l=0;prod=1
    for p in primes:
        if prod*p>=1<<b:break
        l+=1;prod*=p
    else:raise ValueError('insufficient primes')
    return atom**l,R**l
@lru_cache(None)
def interval(n,i,j):
    t=1<<i;H=ceildiv((1<<j)-t,4);m=(n+(1<<j))//4;b=m.bit_length();h=Q-Q*i//b
    f,g=penalty(b,h)
    return ceildiv(8*f*tsum(n,m,H),g)
@lru_cache(None)
def packed(n,j):
    if j==0:return 0
    m=(n+(1<<j))//4
    vals=[smallshift(n,j),packed(n,j-1)+fixed(n,j)-fixed(n,j-1)]
    for i in range(max(0,j-9),j):
        vals.append(packed(n,i)+interval(n,i,j))
        if (1<<i)**3>=m:vals.append(packed(n,i)+4*tsum(n,m,ceildiv((1<<j)-(1<<i),4)))
    return min(vals)
if __name__=='__main__':
    import sys
    for b in map(int,sys.argv[1:]):
        n=1<<b
        print(b,*(packed(n,j) for j in range(b//2+1)),flush=True)
