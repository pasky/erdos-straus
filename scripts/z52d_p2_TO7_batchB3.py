# Lint-fix computations (part 3): Z2602, Z2611, Z2625, Z2437, Z2755, Z2842, Z2647, Z2870, Z2878, Z2855
import sys, math, itertools, random
from collections import Counter, defaultdict
import numpy as np
sys.path.insert(0,'scripts')
from z52d_p2_TO7_load import load, bits
a=load(); B=bits(a)
tsv=np.genfromtxt('data/z52b/pass2/TO7/slices_1e6_T400.tsv',delimiter='\t',names=True,dtype=np.int64)
P=tsv['p']; hard=tsv['hard']==1; minI=tsv['minI']; minII=tsv['minII']; nI=tsv['nI']; nII=tsv['nII']
which=sys.argv[1]
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
if which=='Z2602':
    # x_p = (-1)^{nI(p)} (parity of count of successful type-I slices k<=399) along primes p≡1 mod 4 (index order)
    x=(-1.0)**nI
    N=len(x); best={}
    for d in range(1,41):
        for aa in range(d):
            seq=x[aa::d]
            S=np.cumsum(seq)
            best[(d,aa)]=np.max(np.abs(S))
    D=max(best.values())
    print(f"Z2602 x_p=(-1)^nI over {N} primes p≡1(4) ≤1e6: discrepancy over APs of index (d≤40) = {D:.1f}; sqrt(N)={math.sqrt(N):.1f}; ratio {D/math.sqrt(N):.2f}")
    # same on hard primes only (sequence of hard-prime indices)
    xh=(-1.0)**nI[hard]; Nh=len(xh); Dh=0
    for d in range(1,41):
        for aa in range(d):
            Dh=max(Dh,np.max(np.abs(np.cumsum(xh[aa::d]))))
    print(f"Z2602 hard primes only: N={Nh}, discrepancy={Dh:.1f}, ratio to sqrt(N) {Dh/math.sqrt(Nh):.2f}")
if which=='Z2611':
    # empirical block entropy of success bits b_k = [type-I divisor hit at k], k=3..399 (k≡3 mod 4), windows of W consecutive k
    # compare hard vs typical primes; total correlation = sum H(single) - H(window)
    spf=None
    m0=a['type']==0
    ks=list(range(3,401,4)); K=len(ks)
    Mx=np.zeros((len(P),K),np.int8)
    idx=np.searchsorted(P,a['p'][m0]); Mx[idx,(a['k'][m0]-3)//4]=B['dh'][m0]
    def H(vals):
        c=Counter(map(tuple,vals)); n=len(vals)
        return -sum(v/n*math.log2(v/n) for v in c.values())
    for label,rows in [("hard",Mx[hard]),("typical(hard-complement, p in 1e5..1e6)",Mx[(~hard)&(P>=1e5)])]:
        out=[]
        for W in [1,2,3,4]:
            # windows starting at k-index j, j=0..K-W
            vals=[tuple(r[j:j+W]) for r in rows for j in range(0,K-W+1,20)]
            out.append((W,round(H(vals),4)))
        print("Z2611",label,"block entropies (bits) for W=1..4 (sampled starts):",out, "n rows",len(rows))
        # total correlation of window of 2 vs singles
        h1=H([ (r[j],) for r in rows for j in range(K)]); h2=H([tuple(r[j:j+2]) for r in rows for j in range(0,K-1)])
        print("   total correlation pairs TC2 = 2H1-H2 =", round(2*h1-h2,4))
if which=='Z2625':
    # target constants: max |A| (distinct elements of (Z/t)^*) with -1 not a subset product (nonempty)
    def units(t): return [u for u in range(1,t) if math.gcd(u,t)==1]
    rows=[]
    for t in [3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,20,21,22,24,26,28,30]:
        U=units(t)
        if t==2: continue
        target=(t-1)%t
        # DP over elements: state = frozenset bitmask of nonempty subset products (as set of residues)
        states={0:0}  # bitmask of achieved residues -> max size
        best=0
        cur={frozenset():0}
        for x in U:
            new=dict(cur)
            for S,sz in cur.items():
                prods=set(S)|{x}|{(s*x)%t for s in S}
                if target in prods: continue
                key=frozenset(prods)
                if new.get(key,-1)<sz+1: new[key]=sz+1
            cur=new
        best=max(cur.values())
        rows.append((t,len(U),best))
        print(f"Z2625 t={t}: |G|={len(U)}  max distinct-element sequence avoiding subset product -1: {best}", flush=True)
    # fraction of n<=20000 with some t<=30 whose distinct prime factors of tn+1 (coprime to t) have -1 as subset product
    spf=np.zeros(30*20000+2,dtype=np.int64)
    for i in range(2,int((30*20000+1)**.5)+1):
        if spf[i]==0:
            idx=np.arange(i*i,len(spf),i); mm=spf[idx]==0; spf[idx[mm]]=i
    def pf(n):
        s=[]
        while n>1:
            q=int(spf[n]) if spf[n] else n
            s.append(q)
            while n%q==0: n//=q
        return s
    hit=0; per_t=Counter()
    for n in range(1,20001):
        ok=False
        for t in range(3,31):
            N=t*n+1
            res=[q%t for q in pf(N) if t%q and math.gcd(q,t)==1]
            R=set()
            for r in res: R|={r}|{(s*r)%t for s in R}
            if (t-1)%t in R and t>2: ok=True; per_t[t]+=1
        hit+=ok
    print(f"Z2625 fraction of n<=20000 with some t in [3,30] where subset products of prime factors of tn+1 hit -1: {hit/20000:.4f}")
    print("Z2625 per-t hit counts (t: count) top:", per_t.most_common(6))
if which=='Z2437':
    # spread of uniform measure on Type-I witness supports: witnesses b | M_k, b ≡ -1 (mod k), k in {3,7,11}; support = distinct primes of b.
    # spread q: mu(S ⊆ F) <= q^{-|S|}. Computed as max over S (|S|=1,2) of mu(S ⊆ F) per prime, averaged over hard primes ≤1e5.
    def pf_trial(n):
        s=set(); d=2
        while d*d<=n:
            while n%d==0: s.add(d); n//=d
            d+=1
        if n>1: s.add(n)
        return s
    def divisors_of(M):
        fac={}
        m=M; d=2
        while d*d<=m:
            while m%d==0: fac[d]=fac.get(d,0)+1; m//=d
            d+=1
        if m>1: fac[m]=fac.get(m,0)+1
        ds=[1]
        for q,e in fac.items(): ds=[x*q**j for x in ds for j in range(e+1)]
        return ds
    q1=[]; q2=[]
    for p in P[P>=1000][:3000]:
        if p>1000000: continue
        witnesses=[]
        for k in (3,7,11):
            M=(k*int(p)+1)//4
            if M<2: continue
            for b in divisors_of(M):
                if b%k==k-1: witnesses.append(frozenset(pf_trial(b)) if b>1 else frozenset())
        if len(witnesses)<10: continue
        n=len(witnesses)
        c1=Counter(); c2=Counter()
        for w in witnesses:
            for l in w: c1[l]+=1
            wl=sorted(w)
            for i1 in range(len(wl)):
                for i2 in range(i1+1,len(wl)): c2[(wl[i1],wl[i2])]+=1
        m1=max(c1.values())/n if c1 else 0
        m2=max(c2.values())/n if c2 else 0
        if m1>0: q1.append(1/m1)
        if m2>0: q2.append(math.sqrt(1/m2))
    print(f"Z2437 primes 1e3≤p≤1e6 (first 3000) with ≥10 witnesses: {len(q1)}; spread from singletons: q1=1/max_l mu(l∈F): median {np.median(q1):.3f}, min {np.min(q1):.3f}; spread from pairs: q2=(1/max mu(l,l'∈F))^(1/2): median {np.median(q2):.3f}, min {np.min(q2):.3f}")
