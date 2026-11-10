# z69 TWIST round 2, I17: full translation-overlap profile of the good class set G_d(p) in Cl(-4dp).
# Good forms (Type II: 4abd = p+e, ce = a+b):  [4acd-1, 4ad, d*e], discriminant -4dp  (d = 1: round-1 set G(p)).
# For every class t:  O(t) = #{g in G : t*g in G}  (autocorrelation of G).  Statistics (pre-registered, Z69_TWIST §9):
#   stab = #{t : O(t) = |G|} (order of the stabiliser),  M = max_{t != 1} O(t),  E = sum_{t != 1} O(t)^2,
#   L1 = O(class of a prime ideal over the least split prime l whose class lies in the principal genus),
#   L3 = sum of O over the three least such primes.
# Nulls (R replicates each), both inversion-symmetric, drawn inside the genus coset containing G:
#   N1 uniform;  N2 norm-matched: same number of inversion-orbits as G in every dyadic bin of mu(g),
#   mu(g) = least value coprime to 2d among the three smallest values (a, c, a-|b|+c) of the reduced form (else a).
import sys, math, random
sys.path.insert(0,'scripts')
from collections import Counter
from sympy import divisors, isprime, primerange, jacobi_symbol
from z69_twist_i17 import reduce, compose_std, classgroup_elems

class Grp:
    def __init__(self,D):
        self.D=D; forms=sorted(classgroup_elems(D)); self.h=len(forms)
        ident=reduce(1,0,-D//4); coords={ident:()}; ns=[]; rels=[]
        for g in forms:
            if len(coords)==self.h: break
            if g in coords: continue
            pw=g; n=1
            while pw not in coords: pw=compose_std(pw,g,D); n+=1
            rel=coords[pw]
            new={}
            for f,cd in coords.items():
                new[f]=cd+(0,); cur=f
                for j in range(1,n):
                    cur=compose_std(cur,g,D); new[cur]=cd+(j,)
            coords=new; ns.append(n); rels.append(rel)
        assert len(coords)==self.h, (D,len(coords),self.h)
        self.ns=ns; self.rels=rels; self.r=len(ns); self.coords=coords
        self.form={cd:f for f,cd in coords.items()}
        self.negd={cd:coords[reduce(f[0],-f[1],f[2])] for f,cd in coords.items()}
        self.one=coords[ident]
    def add(self,u,v):
        w=[x+y for x,y in zip(u,v)]
        for i in range(self.r-1,-1,-1):
            while w[i]>=self.ns[i]:
                w[i]-=self.ns[i]
                for t in range(i): w[t]+=self.rels[i][t]
        return tuple(w)
    def sub(self,u,v): return self.add(u,self.negd[v])
    def autocorr(self,X):
        C=Counter()
        for x in X:
            nx=self.negd[x]
            for y in X:
                if y!=x: C[self.add(y,nx)]+=1
        return C

def good_classes_d(p,d):
    S=set(); e=3; emax=(p+4*d)//(4*d-1)
    while e<=emax:
        if (p+e)%(4*d)==0:
            x=(p+e)//(4*d)
            for a in divisors(x):
                b=x//a
                if (a+b)%e==0:
                    c=(a+b)//e; S.add(reduce(4*a*c*d-1,4*a*d,d*e))
        e+=4
    return S

def mu(f,d):
    a,b,c=f
    for v in (a,c,a-abs(b)+c):
        if math.gcd(v,2*d)==1: return v
    return a

def stats(G,X,tl):
    C=G.autocorr(X); k=len(X)
    vals=list(C.values())
    return dict(stab=1+sum(1 for v in vals if v==k), M=max(vals) if vals else 0, E=sum(v*v for v in vals),
                L1=C.get(tl[0],0) if tl else 0, L3=sum(C.get(t,0) for t in tl))

def analyse(p,d,R,rng):
    D=-4*d*p; S=good_classes_d(p,d)
    if len(S)<2: return dict(p=p,d=d,k=len(S))
    G=Grp(D); X=[G.coords[f] for f in S]
    H=set(G.add(u,u) for u in G.coords.values())            # squares = principal genus
    x0=X[0]; assert all(G.sub(x,x0) in H for x in X), "good classes not in one genus"
    pool=[u for u in G.coords.values() if G.sub(u,x0) in H]
    # inversion orbits of the pool (the genus coset is inversion-stable because G is)
    seen=set(); orbs=[]
    for u in pool:
        if u in seen: continue
        v=G.negd[u]; seen.add(u); seen.add(v); orbs.append((u,) if u==v else (u,v))
    Xs=set(X); assert all(G.negd[x] in Xs for x in X), "G not inversion-closed"
    gorb=[o for o in orbs if o[0] in Xs]
    def bin_(o): return (int(math.log2(mu(G.form[o[0]],d))), len(o))
    # translations by small split primes whose class is a square
    tl=[]; l=3
    while len(tl)<3 and l<10**5:
        if isprime(l) and D%l!=0 and jacobi_symbol(D%l,l)==1:
            r=next(t for t in range(l) if (t*t-D//4)%l==0); u=G.coords[reduce(l,2*r,(r*r-D//4)//l)]
            if u in H and u!=G.one and u not in tl and G.negd[u] not in tl: tl.append(u)
        l+=2
    obs=stats(G,X,tl)
    by={}
    for o in orbs: by.setdefault(bin_(o),[]).append(o)
    need=Counter(bin_(o) for o in gorb); typ=Counter(len(o) for o in gorb)
    bylen={1:[o for o in orbs if len(o)==1],2:[o for o in orbs if len(o)==2]}
    out=dict(p=p,d=d,h=G.h,m=len(pool),k=len(X),r=G.r,obs=obs)
    # how norm-driven is G: fraction of G among the k classes of smallest mu
    ranked=sorted(pool,key=lambda u:mu(G.form[u],d)); out['lowmu']=len(Xs&set(ranked[:len(X)]))/len(X)
    for name in ('N1','N2'):
        acc={s:[] for s in obs}
        for _ in range(R):
            Y=[]
            if name=='N1':
                for L,cnt in typ.items():
                    for o in rng.sample(bylen[L],cnt): Y.extend(o)
            else:
                for b,cnt in need.items():
                    for o in rng.sample(by[b],cnt): Y.extend(o)
            st=stats(G,Y,tl)
            for s in obs: acc[s].append(st[s])
        out[name]={s:(sum(v)/R, (sum(x*x for x in v)/R-(sum(v)/R)**2)**0.5) for s,v in acc.items()}
    return out

if __name__=="__main__":
    d=int(sys.argv[1]); R=int(sys.argv[2]); spec=sys.argv[3:]
    if spec[0]=='range': P=[p for p in primerange(int(spec[1]),int(spec[2])) if p%8==int(spec[3])] if len(spec)>3 else [p for p in primerange(int(spec[1]),int(spec[2])) if p%4==1]
    else: P=[int(x) for x in spec]
    rng=random.Random(69)
    agg={n:{s:[0.0,0.0] for s in ('M','E','L1','L3')} for n in ('N1','N2')}; npr=0; stabs=Counter(); Mfrac=[]
    for p in P:
        o=analyse(p,d,R,rng)
        if 'obs' not in o: print(f"p={p} d={d} k={o['k']} (skipped)",flush=True); continue
        npr+=1; ob=o['obs']; stabs[ob['stab']]+=1; Mfrac.append(ob['M']/o['k'])
        line=f"p={p} d={d} h={o['h']} genus={o['m']} k={o['k']} gens={o['r']} lowmu={o['lowmu']:.2f} stab={ob['stab']} M={ob['M']} E={ob['E']} L1={ob['L1']} L3={ob['L3']}"
        for n in ('N1','N2'):
            line+=f" | {n}:"
            for s in ('M','E','L1','L3'):
                mu_,sd=o[n][s]; line+=f" {s} {mu_:.1f}±{sd:.1f}"
                agg[n][s][0]+=ob[s]-mu_; agg[n][s][1]+=sd*sd
        print(line,flush=True)
    print(f"# d={d} primes analysed {npr}; stabiliser orders {dict(stabs)}; M/k: median {sorted(Mfrac)[len(Mfrac)//2]:.2f} max {max(Mfrac):.2f}; share with M/k > 1/2: {sum(1 for x in Mfrac if x>0.5)/len(Mfrac):.2f}")
    for n in ('N1','N2'):
        print(f"# aggregate vs {n}: "+"; ".join(f"Z_{s} = {agg[n][s][0]/math.sqrt(agg[n][s][1]) if agg[n][s][1]>0 else float('nan'):+.2f} (sum excess {agg[n][s][0]:+.1f})" for s in ('M','E','L1','L3')))
