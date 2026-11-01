# Lint-fix computations (part 2): Z2569, Z2596, Z2602, Z2611, Z2625, Z2437, Z2755, Z2842, Z2647, Z2870, Z2878, Z2855
import sys, math, itertools, random
from collections import Counter, defaultdict
import numpy as np
sys.path.insert(0,'scripts')
from z52d_p2_TO7_load import load, bits
a=load(); B=bits(a)
tsv=np.genfromtxt('data/z52b/pass2/TO7/slices_1e6_T400.tsv',delimiter='\t',names=True,dtype=np.int64)
P=tsv['p']; hard=tsv['hard']==1; minI=tsv['minI']; nI=tsv['nI']; nII=tsv['nII']
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
which=sys.argv[1]
if which in ('Z2569',):
    # p = a^2+b^2 (a odd, b even), angle theta = atan2(b,a) bins, norm = p bins; failure proxy minI>7
    pts=[]
    for i,p in enumerate(P):
        if p<1000: continue
        for b in range(2,int(p**.5)+1,2):
            r=p-b*b; x=math.isqrt(r)
            if x*x==r and x%2==1:
                th=math.atan2(b,x); pts.append((th,minI[i],p,hard[i])); break
    th=np.array([t[0] for t in pts]); mI=np.array([t[1] for t in pts]); hd=np.array([t[3] for t in pts])
    fail=(mI>7)
    print("Z2569 Gaussian angle bins (theta in [0,pi/4]); frac minI>7 per bin, all p>=1e3 n=%d"%len(pts))
    edges=np.linspace(0,math.pi/4,9)
    for lo,hi in zip(edges[:-1],edges[1:]):
        s=(th>=lo)&(th<hi)
        print(f"  [{lo:.3f},{hi:.3f}) n={s.sum()} fail={fail[s].mean():.4f} hard-only fail={fail[s&hd].mean() if (s&hd).sum() else float('nan'):.4f}")
if which in ('Z2596',):
    # quotient sets Q_k (type II prime slice k, hard primes) with omega>=4: test longest geometric progression inside Q (ratio g in units)
    spf=np.zeros(250001,dtype=np.int64)
    for i in range(2,501):
        if spf[i]==0:
            idx=np.arange(i*i,250001,i); m=spf[idx]==0; spf[idx[m]]=i
    def divisors(n):
        ds=[1]; m=n
        while m>1:
            q=int(spf[m]) or m; e=0
            while m%q==0: m//=q; e+=1
            ds=[d*q**j for d in ds for j in range(e+1)]
        return ds
    def Q(M,k):
        D=divisors(M); S=set()
        for x in D:
            for y in D:
                if M%(x*y)==0: S.add((x*pow(y,-1,k))%k)
        return S
    def longest_gp(S,k):
        best=1
        for g in range(2,k):
            if math.gcd(g,k)!=1: continue
            for x in S:
                # distinct-term GP x, xg, ..., xg^{L-1} inside S, L <= ord(g)
                L=1; y=x; seen={x}
                while True:
                    y=(y*g)%k
                    if y in S and y not in seen: L+=1; seen.add(y)
                    else: break
                best=max(best,L)
        return best
    stats=[]
    for k in [31,43,59,67]:
        for p in P[hard][:400]:
            if (int(p)+k)%4: continue
            M=(int(p)+k)//4
            if M<2 or M>250000: continue
            w=len(set(q for q in divisors(M) if q>1 and all(q%r for r in range(2,int(q**.5)+1))))
            S=Q(M,k)
            stats.append((k,w,len(S),longest_gp(S,k)))
    stats=np.array(stats)
    rng=random.Random(1)
    for k in [31,43,59,67]:
        # control: random subsets of Z/k^* of the same size: longest distinct GP
        sz=[int(x[2]) for x in stats if x[0]==k]
        ctrl=[]
        for L in sz[:100]:
            U=[u for u in range(1,k) if math.gcd(u,k)==1]
            S=set(rng.sample(U,min(L,len(U))))
            ctrl.append(longest_gp(S,k))
        print(f"Z2596 control k={k}: random subsets of matched size: longest GP mean {np.mean(ctrl):.2f} max {max(ctrl)}")
        s=stats[stats[:,0]==k]
        if len(s)==0: continue
        print(f"Z2596 k={k}: n={len(s)} max omega={s[:,1].max()} |Q| mean={s[:,2].mean():.1f}; longest GP in Q mean={s[:,3].mean():.2f} max={s[:,3].max()}; omega>=4 subset: n={np.sum(s[:,1]>=4)} GP mean={s[s[:,1]>=4,3].mean() if np.sum(s[:,1]>=4) else float('nan'):.2f}")
