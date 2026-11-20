"""Integer determinant on grouped pair rows, fixed-shift and centre caps."""
from z77_bound import *
from math import comb

@lru_cache(None)
def edges(n):
    a=[1]
    while a[-1]<=n: a.append(a[-1]+max(1,a[-1]//2))
    return a

@lru_cache(400000)
def cap(vbits, fbits, width):
    # Integral exponents, quarter-bit grid for V <= 2^(vbits/4), f >=2^(fbits/4).
    if width<=1:return width
    out=width
    for w in (2,3,4,5,6,8,12):
        b=w*(w-1)//2
        R=max(fbits*h*w-vbits*(h*(h+1)//2) for h in range(1,w))
        k=(R-1)//(4*b)
        if k>=0: out=min(out,(w-1)*ceildiv(width,(1<<k)+1)) # width counts consecutive integers: diameter <=2^k
    return out

def lo4(n):return (n**4).bit_length()-1
def hi4(n):return ((n**4)-1).bit_length()

@lru_cache(None)
def routes(n):
    # three base-ordered pair routes, dyadic shift cutoffs E (select optimum afterwards).
    b=n.bit_length(); buckets=[0]*(b+2); es=edges(n)
    # Only need shifts >=2^(b//4); smaller choices of split excluded.
    cut=b//4; T=(n//(1<<cut)+1)//2
    for ia,A in enumerate(es):
        if 2*A*A>n or A>T:break
        A1=es[ia+1]-1
        for ic,C in enumerate(es):
            if A*C>T:break
            C1=es[ic+1]-1
            for id,D in enumerate(es):
                t=A*C*D
                if t>T or 2*A*A*D>n:break
                D1=min(es[id+1]-1,n//(2*A*A)); wa=A1-A+1; wc=C1-C+1; wd=D1-D+1
                f=4*t-1; hi=min(n//(2*t-1),(n+4*A1*A1*D1)//f)
                if hi<1<<cut:continue
                v1=min(3*n,n+4*A1*A1*D1); v2=n*C1+A1; v3=4*C1*C1*D1*n+1
                F=lo4(f); bound=min(wa*wd*cap(hi4(v1),F,wc),wa*wc*cap(hi4(v2),F,wd),wc*wd*cap(hi4(v3),F,wa))
                bound=min(bound,wa*wd*(1+hi//(4*A*D)))
                buckets[hi.bit_length()-1]+=bound
    for k in reversed(range(len(buckets)-1)):buckets[k]+=buckets[k+1]
    return buckets

if __name__=='__main__':
    import sys
    for b in map(int,sys.argv[1:]):
        n=1<<b; layers=routes(n)
        v,j=min((small(n,j)+min(2*layers[j],n//(1<<j)+2),j) for j in range(n.bit_length()//4,b//2+1));print(b,j,v,flush=True)
