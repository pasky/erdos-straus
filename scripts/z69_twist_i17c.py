# z69 TWIST round 2, I17 follow-up of the "unresolved signal" (pre-registered finer null + post-hoc mechanism test), d = 1.
#  N2w : mu-rank-window null (each inversion-orbit of G replaced by a random unused orbit of the same type within +-W
#        places in the mu-ordering of the genus coset)                      [the registered "finer null"]
#  RES : residual statistics after deleting the ordered pairs (x, y) of G that lie in a common divisor fibre
#        F_a(+-) = {classes of the ideals (A, 2a + sqrt(-p)), A | p + 4a^2, A == -1 (4a)} and their inverses   [post hoc]
#  LEM : how many of the l-translation overlaps are pairs (A, l*A) of good divisors of the same p + 4a^2 (Lemma DL)  [post hoc]
#  (A "cube shuffle" null N3 was tried and discarded: it treats the a-fibres as independent, but every solution lies in
#   the a-fibre and, inverted, in the b-fibre, so the fibres are coupled; the null doubled |G| and is not evidence.)
import sys, math, random
sys.path.insert(0,'scripts')
from collections import Counter
from sympy import divisors, factorint, primerange
from z69_twist_i17 import reduce
from z69_twist_i17b import Grp, mu, stats

def solutions(p):
    out=[]; e=3
    while 3*e<=p+4:
        if (p+e)%4==0:
            x=(p+e)//4
            for a in divisors(x):
                b=x//a
                if (a+b)%e==0: out.append((a,b,(a+b)//e,e))
        e+=4
    return out

def stats_pairs(G,X,tl,excl):
    C=Counter(); k=len(X)
    for x in X:
        nx=G.negd[x]
        for y in X:
            if y!=x and (x,y) not in excl: C[G.add(y,nx)]+=1
    vals=list(C.values())
    return dict(M=max(vals) if vals else 0, E=sum(v*v for v in vals), L1=C.get(tl[0],0) if tl else 0, L3=sum(C.get(t,0) for t in tl))

def analyse(p,R,W,rng):
    D=-4*p; sols=solutions(p)
    if len(sols)<2: return None
    G=Grp(D); H=set(G.add(u,u) for u in G.coords.values())
    fib={}
    for (a,b,c,e) in sols: fib.setdefault(a,set()).add(G.coords[reduce(4*a*c-1,4*a,e)])
    X=sorted(set().union(*fib.values())); Xs=set(X); k=len(X)
    x0=X[0]; pool=[u for u in G.coords.values() if G.sub(u,x0) in H]
    seen=set(); orbs=[]
    for u in sorted(pool,key=lambda u:(mu(G.form[u],1),u)):
        if u in seen: continue
        v=G.negd[u]; seen.add(u); seen.add(v); orbs.append((u,) if u==v else (u,v))
    tl=[]; l=5; l1=None
    while len(tl)<3 and l<10**5:
        if all(l%q for q in range(2,int(l**.5)+1)) and l%4==1 and pow(-p%l,(l-1)//2,l)==1:
            r=next(t for t in range(l) if (t*t+p)%l==0); u=G.coords[reduce(l,2*r,(r*r+p)//l)]
            if u!=G.one and u not in tl and G.negd[u] not in tl:
                tl.append(u)
                if l1 is None: l1=l
        l+=4
    obs=stats(G,X,tl)
    # --- RES
    excl=set()
    for a,F in fib.items():
        Fpm=F|{G.negd[u] for u in F}
        for x in Fpm:
            for y in Fpm:
                if x!=y: excl.add((x,y))
    res=stats_pairs(G,X,tl,excl); nexcl=len(excl)
    # --- N2w
    gidx=[i for i,o in enumerate(orbs) if o[0] in Xs]
    acc={s:[] for s in ('M','E','L1','L3')}
    for _ in range(R):
        while True:                      # redraw on exhaustion, so that Y is always a set of |G| distinct classes
            used=set(); Y=[]; ok=True
            for i in gidx:
                cand=[j for j in range(max(0,i-W),min(len(orbs),i+W+1)) if j not in used and len(orbs[j])==len(orbs[i])]
                if not cand: ok=False; break
                j=rng.choice(cand); used.add(j); Y.extend(orbs[j])
            if ok: break
        assert len(set(Y))==len(Y)==k
        st=stats(G,Y,tl)
        for s in acc: acc[s].append(st[s])
    n2w={s:(sum(v)/R,(sum(x*x for x in v)/R-(sum(v)/R)**2)**0.5) for s,v in acc.items()}
    # --- lemma pairs: A and l*A both good divisors of p + 4a^2 at the same root (Lemma DL), l = the prime of tl[0]
    lemL1=0
    if tl:
        LP=set()
        for a in fib:
            good={4*a*c-1:G.coords[reduce(4*a*c-1,4*a,e)] for (a2,b,c,e) in sols if a2==a}
            for A,u in good.items():
                if l1*A in good:
                    v=good[l1*A]
                    for (x,y) in ((u,v),(v,u),(G.negd[u],G.negd[v]),(G.negd[v],G.negd[u])): LP.add((x,y))
        lemL1=sum(1 for x in X if (x,G.add(x,tl[0])) in LP)
    return dict(p=p,k=k,obs=obs,res=res,nexcl=nexcl,n2w=n2w,lemL1=lemL1,nf=sum(1 for F in fib.values() if len(F)>1))

if __name__=="__main__":
    R=int(sys.argv[1]); W=int(sys.argv[2]); spec=sys.argv[3:]
    P=[p for p in primerange(int(spec[1]),int(spec[2])) if p%8==1] if spec[0]=='range' else [int(x) for x in spec]
    rng=random.Random(691)
    ag={'n2w':{s:[0.0,0.0] for s in ('M','E','L1','L3')}}
    tot=Counter(); n=0
    for p in P:
        o=analyse(p,R,W,rng)
        if o is None: continue
        n+=1; ob=o['obs']
        for s in ('M','E','L1','L3'):
            ag['n2w'][s][0]+=ob[s]-o['n2w'][s][0]; ag['n2w'][s][1]+=o['n2w'][s][1]**2
            tot['obs_'+s]+=ob[s]; tot['res_'+s]+=o['res'][s]
        tot['k']+=o['k']; tot['lemL1']+=o['lemL1']
        for s in ('M','E','L1','L3'): tot['n2w_'+s]+=o['n2w'][s][0]
        print(f"p={p} k={o['k']} fibres>1:{o['nf']} obs M={ob['M']} E={ob['E']} L1={ob['L1']} L3={ob['L3']} | res M={o['res']['M']} E={o['res']['E']} L1={o['res']['L1']} L3={o['res']['L3']} "
              f"| N2w M {o['n2w']['M'][0]:.1f} E {o['n2w']['E'][0]:.0f} L1 {o['n2w']['L1'][0]:.1f} L3 {o['n2w']['L3'][0]:.1f} | lemma-pairs in L1: {o['lemL1']}",flush=True)
    Z=lambda a: a[0]/math.sqrt(a[1]) if a[1]>0 else float('nan')
    print(f"# primes {n}; sum k {tot['k']}; totals obs M/E/L1/L3 = {tot['obs_M']}/{tot['obs_E']}/{tot['obs_L1']}/{tot['obs_L3']}; residual (same-fibre pairs removed) = {tot['res_M']}/{tot['res_E']}/{tot['res_L1']}/{tot['res_L3']}; N2w null means = {tot['n2w_M']:.0f}/{tot['n2w_E']:.0f}/{tot['n2w_L1']:.0f}/{tot['n2w_L3']:.0f}; L1 counts that are Lemma-DL pairs: {tot['lemL1']}")
    print("# vs N2w (mu-rank window +-%d): "%W+"; ".join(f"Z_{s} = {Z(ag['n2w'][s]):+.2f} (excess {ag['n2w'][s][0]:+.1f})" for s in ('M','E','L1','L3')))
