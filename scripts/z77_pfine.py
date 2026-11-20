"""Finer P routes for the binding exponents, pooling all shifts above cube root."""
from z77_routes import *
from z77_routes import edges as coarse_edges

def pooled(n,j):
    m=(n+(1<<j))//4
    # Pool subsets [2^i,2^j) in one short interval to pay one endpoint error.
    a=small(n,j)
    for i in range((rootup(m,3)-1).bit_length(),j):
        H=ceildiv((1<<j)-(1<<i),4)
        a=min(a,small(n,i)+4*tau_sum(m,H))
    return a

def refine(n,steps=5):
    b=n.bit_length(); es=[1]; cut=b//3-3; high=(n//(1<<cut)+1)//2
    while es[-1]<=high:es.append(es[-1]+max(1,es[-1]//steps))
    buckets=[0]*(b+2)
    for ia,A in enumerate(es):
        if 2*A*A>n or A>high:break
        A1=es[ia+1]-1;wa=A1-A+1
        for ic,C in enumerate(es):
            if A*C>high:break
            C1=es[ic+1]-1;wc=C1-C+1
            for id,D in enumerate(es):
                t=A*C*D
                if t>high or 2*A*A*D>n:break
                D1=min(es[id+1]-1,n//(2*A*A));wd=D1-D+1
                f=4*t-1; v1=min(n+4*A1*A1*D1,3*n); hi=min(n//(2*t-1),v1//f)
                if hi<1<<cut:continue
                F=lo4(f);v2=n*C1+A1;v3=4*C1*C1*D1*n+1
                bd=min(wa*wd*cap(hi4(v1),F,wc),wa*wc*cap(hi4(v2),F,wd),wc*wd*cap(hi4(v3),F,wa))
                # For a fixed a,d, cofactor e varies in one class mod 4ad,
                # as c ranges over wc consecutive integers. Fractional-linear difference:
                # e0-e1 = V * 4ad*(wc-1)/(f0*f1).
                w=1+v1*(wc-1)//(f*f)
                F1=max(1,n//2//(4*A1*C1*D1)) # for N in (n/2,n]
                bd=min(bd,wa*wd*cap(hi4(v1),lo4(F1),w))
                buckets[hi.bit_length()-1]+=bd
    for i in reversed(range(len(buckets)-1)):buckets[i]+=buckets[i+1]
    return min((pooled(n,j)+min(2*buckets[j],n//(1<<j)+2),j) for j in range(cut,b//2+1))

if __name__=='__main__':
    import sys
    for b in map(int,sys.argv[1:]):
        v,j=refine(1<<b);print(b,j,v,flush=True)
