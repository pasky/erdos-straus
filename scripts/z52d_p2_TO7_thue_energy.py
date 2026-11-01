# Z2884: signed Thue pairs (u,v), 1<=|u|,|v|<=sqrt p, with u,v QNR mod p and |uv| | p+u+v ; count vs heuristic sum 1/|uv|.
# Z2425/Z2426: multiplicative energy / convolution peaks of the quotient set Q_M = {a/b mod k : ab | M} (type II, k prime, hard primes)
import sys, math; sys.path.insert(0,'scripts')
import numpy as np
from collections import Counter
tsv=np.genfromtxt('data/z52b/pass2/TO7/slices_1e6_T400.tsv',delimiter='\t',names=True,dtype=np.int64)
P=[int(x) for x in tsv['p'] if 5<=x<=50000]
hard=set(int(x) for x in tsv['p'][tsv['hard']==1])
tot_hits=0; tot_pairs=0; heur=0.0; hits_by_val=Counter()
for p in P:
    r=math.isqrt(p)
    qnr=np.zeros(p,dtype=bool)
    x=np.arange(1,p); qr=np.zeros(p,bool); qr[(x*x)%p]=True
    U=np.array([u for u in range(-r,r+1) if u!=0],dtype=np.int64)
    Ures=np.array([int(u)%p for u in U])
    good=~qr[Ures] & (Ures!=0)
    Ug=U[good]
    if len(Ug)==0: continue
    UU=Ug[:,None]; VV=Ug[None,:]
    prod=np.abs(UU*VV)
    s=p+UU+VV
    hit=(s % prod)==0
    tot_hits+=int(hit.sum()); tot_pairs+=int(hit.size); heur+=float((1.0/prod).sum())
print(f"Z2884: primes {len(P)} pairs {tot_pairs} hits {tot_hits} frac {tot_hits/tot_pairs:.5f}  sum 1/|uv| over same pairs {heur:.3f} (ratio hits/heur {tot_hits/heur:.3f})")
# Z2425/6: energy of quotient sets at hard primes, slice k (prime) type II
import sys as _s; _s.path.insert(0,'scripts')
from z52d_p2_TO7_load import load
a=load(); typ=a['type']; 
N=1000001
spf=np.zeros(N+1,dtype=np.int64)
for i in range(2,int(N**0.5)+1):
    if spf[i]==0:
        idx=np.arange(i*i,N+1,i); m=spf[idx]==0; spf[idx[m]]=i
def divisors(n):
    ds=[1]; m=n
    while m>1:
        q=int(spf[m]) or m; e=0
        while m%q==0: m//=q; e+=1
        ds=[d*q**j for d in ds for j in range(e+1)]
    return ds
def Qset(M,k):
    D=divisors(M)
    S=set()
    for aa in D:
        for bb in D:
            if (M % (aa*bb))==0 and (aa+bb)%k==0:
                S.add(aa % k)  # placeholder, replaced below
    return None
import itertools
def Qset2(M,k):
    D=divisors(M); S=set()
    for aa in D:
        ainv=None
        for bb in D:
            if M % (aa*bb)==0:
                S.add((aa*pow(bb,-1,k))%k)
    return S
for k in [19,23,31]:
    E_ratio=[]; sizes=[]; top=[]
    for p in sorted(hard)[:600]:
        if (p+k)%4: continue
        M=(p+k)//4
        if M<2: continue
        S=Qset2(M,k)  # subset of (Z/k)^*
        if k-1 in S or len(S)<4: pass
        Sx=np.zeros(k,bool)
        for s in S: Sx[s]=True
        # multiplicative energy normalized: E = #{(x,y,z,w) in Q^4: x y = z w}/|Q|^3 ; random set of same size in units
        units=np.arange(1,k)
        cnt=Counter()
        L=list(S)
        for x in L:
            for y in L:
                cnt[(x*y)%k]+=1
        # E = sum_t r(t)^2 where r(t)=#{(x,y): xy=t}
        Eq=sum(v*v for v in cnt.values())/len(L)**3
        # random comparator: uniform random subset of units of same size, averaged over 20 draws
        rng=np.random.default_rng(p)
        Er=[]
        for _ in range(20):
            R=list(rng.choice(units, size=len(L), replace=False))
            c2=Counter((x*y)%k for x in R for y in R)
            Er.append(sum(v*v for v in c2.values())/len(R)**3)
        E_ratio.append(Eq/np.mean(Er)); sizes.append(len(L))
    print(f"k={k}: hard primes used {len(E_ratio)}, mean |Q| {np.mean(sizes):.2f}/(k-1)={k-1}, energy ratio Q vs random same-size: mean {np.mean(E_ratio):.3f}, median {np.median(E_ratio):.3f}, max {np.max(E_ratio):.3f}")
