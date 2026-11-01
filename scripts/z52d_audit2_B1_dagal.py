# Z2134: Dagal's rewriter (arXiv:2003.13229 Thm 5.1): 1/s + 1/(rs) = 1/(qr) + 1/(qs), r = q+d, s = qr-d (q>1,d>=1).
# On ES solution sets of 4/p: which solutions are linked by a Dagal move on a pair of denominators, vs general pivots
# (hold one denominator, replace the other two by any pair with the same sum; Q3_PIVOT.md).
import sys
from math import gcd
from sympy import primerange, divisors
sys.path.insert(0,'scripts'); 
def sols(p):
    out=[]
    for x in range(p//4+1, 3*p//4+1):
        a=4*x-p; b=p*x
        for d in divisors(b*b):
            if d*d>b*b: break
            if (d+b)%a==0 and (b*b//d+b)%a==0:
                y=(d+b)//a; z=(b*b//d+b)//a
                if y>=x: out.append((x,y,z))
    return out
def dagal_images(y,z):
    # pair {y,z} as {qr,qs}: q | gcd, r<s, s = qr - d with r = q + d  =>  s = q r - r + q
    res=set(); g=gcd(y,z)
    for q in divisors(g):
        if q<2: continue
        r,s=sorted((y//q,z//q))
        d=r-q
        if d>=1 and s==q*r-d: res.add(tuple(sorted((s,r*s))))
    # pair as {s, rs}: r = z/y if y | z, then q from s = qr - r + q -> q = (s + r)/(r+1)
    lo,hi=sorted((y,z))
    if hi%lo==0:
        r=hi//lo; s=lo
        if (s+r)%(r+1)==0:
            q=(s+r)//(r+1)
            if q>1 and r-q>=1: res.add(tuple(sorted((q*r,q*s))))
    return res
tot=0; moved=0; dag_edges=0; comps_d=[]; comps_p=[]
for p in primerange(5,int(sys.argv[1])):
    if p%4!=1: continue
    S=sols(p); Sset=set(S); tot+=len(S)
    adj={s:set() for s in S}
    for t in S:
        for i in range(3):
            keep=t[i]; pair=[t[j] for j in range(3) if j!=i]
            for (a,b) in dagal_images(*pair):
                u=tuple(sorted((keep,a,b)))
                assert u in Sset, (p,t,u)
                if u!=t: adj[t].add(u); adj[u].add(t)
    moved+=sum(1 for t in S if adj[t]); dag_edges+=sum(len(v) for v in adj.values())//2
    # components: dagal graph and pivot graph (share a denominator)
    def ncomp(nb):
        seen=set(); c=0
        for s in S:
            if s in seen: continue
            c+=1; st=[s]; seen.add(s)
            while st:
                v=st.pop()
                for w in nb(v):
                    if w not in seen: seen.add(w); st.append(w)
        return c
    comps_d.append((ncomp(lambda v:adj[v]),len(S)))
    byden={}
    for t in S:
        for x in set(t): byden.setdefault(x,[]).append(t)
    comps_p.append((ncomp(lambda v:[w for x in set(v) for w in byden[x]]),len(S),p))
print('solutions',tot,'touched by a Dagal move',moved,'Dagal edges',dag_edges)
print('mean #components Dagal graph / #solutions', sum(c for c,_ in comps_d)/len(comps_d), sum(n for _,n in comps_d)/len(comps_d))
print('pivot graph: primes with 1 component',sum(1 for c,_,_ in comps_p if c==1),'of',len(comps_p),' mean comps',sum(c for c,_,_ in comps_p)/len(comps_p))
print('largest #pivot comps',sorted(comps_p)[-5:])
