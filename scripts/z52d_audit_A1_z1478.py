# Z1478: F2 (mod-squares) relaxation of the (*) divisor condition at level t=4C.
# Full: exists d | N=4Cn+1, d ≡ -1 (mod 4C).  Relax: -1 ∈ <prime factors of N> · (squares) in (Z/4C)^x.
import sys, math
from collections import Counter
P = int(sys.argv[1]) if len(sys.argv)>1 else 100000
CMAX = int(sys.argv[2]) if len(sys.argv)>2 else 100
def factor(n):
    f={}; d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1 if d==2 else 2
    if n>1: f[n]=f.get(n,0)+1
    return f
sqcache={}
def squares(m):
    if m not in sqcache:
        sqcache[m]=frozenset((x*x)%m for x in range(1,m) if math.gcd(x,m)==1)
    return sqcache[m]
def closure(m, gens):
    H=set(squares(m))
    for g in gens:
        g%=m
        if g in H: continue
        H |= {(h*g)%m for h in H}
    return H
def divres(m,f):
    S={1}
    for q,e in f.items():
        new=set(); pw=1
        for k in range(e+1):
            new|={(s*pw)%m for s in S}; pw=pw*q%m
        S=new
    return S
def run(nlist, tag):
    tot=Counter(); firstF2=[]; percond=[]
    for n in nlist:
        nf2=0; nfull=0; first=None
        for C in range(1,CMAX+1):
            m=4*C; N=m*n+1; f=factor(N)
            H=closure(m,list(f))
            rel=(m-1) in H
            full=(m-1) in divres(m,f)
            assert not(full and not rel)
            tot[(rel,full)]+=1
            if rel:
                nf2+=1
                if first is None: first=C
            if full: nfull+=1
        firstF2.append((n,first,nf2,nfull))
    return tot, firstF2
if __name__=="__main__":
    def isprime(n):
        if n<2: return False
        for d in range(2,int(n**.5)+1):
            if n%d==0: return False
        return True
    primes=[p for p in range(5,P+1) if p%4==1 and isprime(p)]
    tot,ff=run(primes,'p')
    print("primes p≡1(4) ≤",P,"count",len(primes),"C≤",CMAX)
    s=sum(tot.values())
    for k,v in sorted(tot.items()): print(" (rel,full)=",k,v,round(v/s,4))
    rel=tot[(True,True)]+tot[(True,False)]
    print(" P(full|rel)=",round(tot[(True,True)]/rel,4)," P(rel)=",round(rel/s,4))
    print(" max first-F2 C over primes:",max(x[1] or 10**9 for x in ff), "primes with no F2 C≤CMAX:",[x[0] for x in ff if x[1] is None][:20])
    worst=sorted(ff,key=lambda x:(x[1] or 10**9))[-8:]; print(" worst (p,firstC,#relC,#fullC):",worst)
    nz=sorted(ff,key=lambda x:x[3])[:8]; print(" fewest full C:",nz)
