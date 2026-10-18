"""Does the b=1 hit indicator at level d depend on quartic data (q/p)_4 beyond congruence data?
Stratified (by p mod lcm(4d,16,q)) difference of hit rates between (q/p)_4=+1 and -1 (only primes with (q/p)=1).
Also: canonical quartic bit of witnesses for p=5 (8): (2w/p)_4.  Usage: N D"""
import sys, math, collections; sys.path.insert(0,'scripts')
from z35_lib import *
N=int(sys.argv[1]); D=int(sys.argv[2])
spf=spf_sieve(N+4*D+10)
P=[p for p in primes_upto(N,spf) if p%4==1 and p>5]
Q=[2,3,5,7,11,13]
hits={}; qb={}
bit=collections.Counter()
for p in P:
    e=(p-1)//4
    W=b1_witnesses(p,D,spf); hd=set(d for d,w in W)
    hits[p]=hd
    qb[p]={q:(1 if pow(q,e,p)==1 else -1 if pow(q,e,p)==p-1 else 0) for q in Q}
    if p%8==5:
        r2=pow(2,e,p)
        for d,w in W:
            x=r2*pow(w,e,p)%p; bit[1 if x==1 else -1]+=1
print("primes",len(P),"N",N,"D",D)
print("canonical quartic bit (2w/p)_4 of b=1 witnesses, p=5(8), d<=D:",dict(bit))
zs=[]
for d in range(1,D+1):
    for q in Q:
        L=math.lcm(4*d,16,q)
        S=collections.defaultdict(lambda:[0,0,0,0])  # n+,h+,n-,h-
        for p in P:
            v=qb[p][q]
            if v==0: continue
            s=S[p%L]; h=d in hits[p]
            if v==1: s[0]+=1; s[1]+=h
            else: s[2]+=1; s[3]+=h
        num=0;var=0
        for n1,h1,n2,h2 in S.values():
            if n1==0 or n2==0: continue
            pr=(h1+h2)/(n1+n2); w=n1*n2/(n1+n2)
            num+=w*(h1/n1-h2/n2); var+=w*w*pr*(1-pr)*(1/n1+1/n2)
        z=num/math.sqrt(var) if var>0 else 0
        zs.append((abs(z),d,q,z))
zs.sort(reverse=True)
print("tests",len(zs),"max |z| top5:",[(round(z,2),d,q) for _,d,q,z in zs[:5]])
print("fraction |z|>2: %.3f (null ~0.046), >3: %.4f"%(sum(1 for t in zs if t[0]>2)/len(zs),sum(1 for t in zs if t[0]>3)/len(zs)))
