"""Fixed carrier, two sorted slices. Truncated ranges give only witnesses."""
from fractions import Fraction as F
from math import gcd,prod
from functools import lru_cache
from pathlib import Path
from z82_c2es_panel import check


@lru_cache(8192)
def factors(n):
    # For n>=1e9 only trial through 500; store unsplit residual as one block.
    out={};lim=n if n<10**9 else 500
    for d in range(2,lim+1):
        if d*d>n:break
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
    if n>1:out[n]=1
    return out


def divs(parts):
    # Blocks can overlap across parts. Every enumerated number is a divisor;
    # all are attained if factors uses complete prime factorizations.
    ex={}
    for t,j in parts:
        for q,e in factors(t).items():ex[q]=ex.get(q,0)+e*j
    ds=[1]
    for q,e in ex.items():ds=[d*q**i for d in ds for i in range(e+1)]
    return ds


def split(j,g,H,parts):
    # j/g=1/u+H/v, no requirement of lowest terms.
    for d in divs(parts):
        if (g+d)%j:continue
        d2=H*g*g//d
        if (H*g+d2)%j==0:yield ((g+d)//j,(H*g+d2)//j)


def solve(n,M,D,limit):
    assert D>1 and gcd(D,2*n)==1
    # Try small additive offsets on either smallest-denominator chart before expanding.
    for i in range(limit):
        A=n//(M*D)+1+i;x=D*A
        if M*x<=3*n:
            j=M*x-n;g=n*A
            for B,Z in split(j,g,D*D,((D,2),(n,2),(A,2))):
                if gcd(Z,D)==1:
                    xyz=(x,D*B,F(Z,D));check(n,M,xyz);return xyz
        Z=D*n//M+1+i
        if M*Z<=3*D*n and gcd(Z,D)==1:
            j=D*(M*Z-n*D);g=n*Z
            for A,B in split(j,g,1,((n,2),(Z,2))):
                xyz=(D*A,D*B,F(Z,D));check(n,M,xyz);return xyz
    return None


def test(n,M):
    complete=n<1000
    for D in range(3,62,2):
        if gcd(D,n)>1:continue
        xyz=solve(n,M,D,3*D*n//M+2 if complete else 50)
        if xyz:
            print(n,M,D,'minimum' if complete or D==3 or (D==5 and n%3==0) else 'upper', *xyz);return
    print(n,M,'no hit to 61', 'exhaustive' if complete else 'partial offsets')


def prime_census(N=1000000):
    from math import isqrt
    import hashlib
    sieve=bytearray([1])*(N+1);sieve[:2]=b'\0\0'
    for j in range(2,isqrt(N)+1):
        if sieve[j]:sieve[j*j::j]=bytes((N-j*j)//j+1)
    count=0;first=[];missing=[];digest=hashlib.sha256()
    for p in range(17,N+1,8):
        if not sieve[p]:continue
        count+=1; xyz=solve(p,4,3,12)
        if xyz is None: first.append(p);xyz=solve(p,4,3,150)
        if xyz is None:missing.append(p);continue
        assert xyz[2].denominator==3 and xyz[0]%3==xyz[1]%3==0
        digest.update(f'{p} {xyz}\n'.encode())
    print('1 mod 8 prime census:',N,count,'misses at 12,150 offsets',first,missing,'witness SHA256',digest.hexdigest())


if __name__=='__main__':
    zs=[int(r) for r in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if r and r[0]!='#']
    for n in zs+[17401609,2521,3361,21841,76441,113035442521,183783601,2238327841,4367159449,3153419441929,3189177846574333650961]:test(n,4)
    for n in (9,25,49,121,169,289,361,841,105,1465,3865,4545,10305,12145,39361,67425):test(n,4)
    for n in (11,17,131,241,1590284203561,6955940568721):test(n,8)
    prime_census()
