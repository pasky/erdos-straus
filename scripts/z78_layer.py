"""Uniform integer high-P bounds, dyadic shift split with determinant on both
f and complementary e. Also bound the integer complement B=V/f or f'=V/f in
fixed (a,c) and (c,d) rows. Output multi-cut bounds for the large-shift part."""
from z77_pfine import pooled
from z77_routes import *
from sys import argv

def layer(n,step):
    # N<=n and N>=n/2 (use table only inside that interval).
    b=n.bit_length();cut=b*3//8-5; high=(n//(1<<cut)+1)//2
    es=[1]
    while es[-1]<=high:es.append(es[-1]+max(1,es[-1]//step))
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
                f=4*t-1;v1=min(n+4*A1*A1*D1,3*n); hi=min(n//(2*t-1),v1//f)
                if hi<1<<cut:continue
                F=lo4(f);upper=4*A1*C1*D1-1
                best=wa*wc*wd
                for v,lower,w,pairs,scale in ((v1,n//2,wc,wa*wd,1),(n*C1+A1,n//2*C,wd,wa*wc,0),(4*C1*C1*D1*n+1,4*C*C*D*(n//2)+1,wa,wc*wd,1)):
                    V=hi4(v);h=1+v*(w-1)//(f*f)
                    back=cap(V,lo4(max(1,lower//upper)),h) if scale else h
                    best=min(best,pairs*cap(V,F,w),pairs*back)
                buckets[hi.bit_length()-1]+=2*best
    for i in reversed(range(len(buckets)-1)):buckets[i]+=buckets[i+1]
    return cut,buckets
if __name__=='__main__':
    for b in map(int,argv[1:]):
        n=1<<b;cut,s=layer(n,2);print(n,cut,*s[cut:b//2+1],flush=True)
