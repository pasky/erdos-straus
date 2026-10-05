# R31 from-scratch ck_min engine (no reuse of author's code).
# ck_min(p)=min{ck : (c,k) in B_p, sf(c) not in {1,2,3,6}, M_{c,k}(p)>0},
# B_p = {1<=k<=floor(2p/3), 1<=c<=floor((2p+k)/(4k)), (p,ck)=1}; M = #{D | p^2+4ck^2 : D = -p mod 4ck}.
import sys
from sympy import factorint, primerange, legendre_symbol
from itertools import product

def sqfree_part(c):
    s=1
    for q,e in factorint(c).items():
        if e%2: s*=q
    return s

def divisors_from(f):
    ds=[1]
    for q,e in f.items():
        ds=[d*q**i for d in ds for i in range(e+1)]
    return ds

def M(p,c,k):
    h=4*c*k; N=p*p+4*c*k*k
    return sum(1 for D in divisors_from(factorint(N)) if (D+p)%h==0)

def ckmin(p, cap, skip_forced=False):
    for m in range(1, cap+1):
        for k in range(1, m+1):
            if m%k: continue
            c=m//k
            if k> (2*p)//3 or c > (2*p+k)//(4*k) or m%p==0: continue
            s=sqfree_part(c)
            if s in (1,2,3,6): continue
            if skip_forced and legendre_symbol((-s)%p, p)==1: continue
            if M(p,c,k)>0: return m
    return None

def np_(p):
    q=2
    while legendre_symbol(q,p)==1: q+=1
    return q

if __name__=="__main__":
    mode=sys.argv[1]
    if mode=="one":
        p=int(sys.argv[2]); cap=int(sys.argv[3]); sk=len(sys.argv)>4
        print(p, np_(p), ckmin(p,cap,skip_forced=sk))
    if mode=="thm61":
        X=int(sys.argv[2]); worst=0; cnt=0; bad=[]
        for p in primerange(25, X):
            if p%24!=1 or legendre_symbol(5,p)!=-1: continue
            cnt+=1
            v=ckmin(p,12)
            if v is None or v>10 or (p%5==2 and v!=5): bad.append((p,v))
            if v and v>worst: worst=v; print("worst",p,v,flush=True)
        print("n_p=5 hard primes <",X,":",cnt,"bad:",bad[:20],"max",worst)
