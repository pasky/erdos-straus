# Z2443 (relative density of fixed-K slice-success primes), Z2565 (tails of minI = first successful slice), Z2804/Z2803 (v2(ord_p a) = v2(p-1) density),
# Z2887 (two-squares residues vs minI), Z2905 (least-QNR-type character sum vs minI), Z2884 (Thue pairs with uv | p+u+v, p<1e5)
import sys, math; sys.path.insert(0,'scripts')
import numpy as np
tsv=np.genfromtxt('data/z52b/pass2/TO7/slices_1e6_T400.tsv',delimiter='\t',names=True,dtype=np.int64)
P=tsv['p']; minI=tsv['minI']; minII=tsv['minII']; hard=tsv['hard']==1
mI=np.where(minI>0,minI,10**6); mII=np.where(minII>0,minII,10**6)
print("== Z2443: fraction of primes (p ≡1 mod 4, p<=1e6) with minI<=K, by p-range; and among hard")
bins=[(5,1e4),(1e4,1e5),(1e5,1e6)]
for K in [3,7,11,19,31,63]:
    row=[]
    for lo,hi in bins:
        s=(P>=lo)&(P<hi); row.append(round((mI[s]<=K).mean(),4))
    print(f"K={K}: per-bin frac={row}  hard(1e5..1e6)={round((mI[(P>=1e5)&hard]<=K).mean(),4)}")
print("== Z2565 tail of minI (first successful type-I slice k) and min over both types")
mm=np.minimum(mI,mII)
for K in [7,15,31,63,127]:
    print(f"minI>{K}: frac all={np.mean(mI>K):.5f} ; min(I,II)>{K}: frac={np.mean(mm>K):.6f}; count={np.sum(mm>K)}")
print("== Z2804/Z2803: density of p with v2(ord_p a)=v2(p-1) (a fixed), p<=1e6, p≡1 mod 4")
def ordv2(a,p):
    # v2 of multiplicative order of a mod p
    m=p-1; e=0
    while m%2==0: m//=2; e+=1
    # order = 2^j * odd ; compute v2(ord): smallest j with a^{m*2^{?}}...
    x=pow(a,m,p)  # odd part killed
    j=0
    while x!=1:
        x=x*x%p; j+=1
    return j
ps=[int(p) for p in P]
v2p=[]
for p in ps:
    q=p-1; e=0
    while q%2==0: q//=2; e+=1
    v2p.append(e)
v2p=np.array(v2p)
union=np.zeros(len(ps),bool)
for a in [2,3,5,6,7,10,11,13,14,15,17,19,21,22,23]:
    hit=np.array([ordv2(a,p)==v2p[i] if a%p else False for i,p in enumerate(ps)])
    union|=hit
    print(f"a={a}: density {hit.mean():.4f}")
print(f"union over a in list: {union.mean():.4f}  (n={len(ps)})")
print("== Z2887: two-squares p=a^2+b^2: residues (a mod 8, b mod 8) vs minI (hard primes excluded?)")
import collections
tab=collections.defaultdict(list)
for i,p in enumerate(ps):
    if p<1000: continue
    # find a,b by brute force (small)
    for b in range(1,int(p**0.5)+1):
        r=p-b*b; a=int(math.isqrt(r))
        if a*a==r and a>0 and a%2==1:  # a odd, b even (p≡1 mod4 gives unique up to order)
            key=(a%8,b%8); tab[key].append(mI[i]); break
for kk in sorted(tab): 
    v=np.array(tab[kk]); print(kk, len(v), "median minI", np.median(v), "mean minI", round(v[v<10**6].mean(),3), "frac minI>7", round(np.mean(v>7),3))
print("== Z2905: correlation of L-type sum S(p)=sum_{m<=100} (m/p)/m with minI (p>=1000)")
def leg_table(p,M):
    # Legendre (m/p) for m<=M via quadratic residues mod p? uses Euler criterion vectorized over m (costly); use squares for p small enough
    qr=np.zeros(p,dtype=np.int8)
    x=np.arange(1,p)
    qr[(x*x)%p]=1
    out=np.zeros(M+1)
    for m in range(1,M+1):
        r=m%p
        if r==0: out[m]=0
        else: out[m]= 1 if qr[r] else -1
    return out
S=np.zeros(len(ps)); sel=[]
for i,p in enumerate(ps):
    if p<1000 or p>2e5: continue
    lt=leg_table(p,100)
    S[i]=sum(lt[m]/m for m in range(1,101))
    sel.append(i)
sel=np.array(sel)
x=S[sel]; y=np.minimum(mI[sel],100).astype(float)
print("n",len(sel),"corr(S,minI_capped100)=",round(np.corrcoef(x,y)[0,1],4), " corr(S, nI)=", round(np.corrcoef(x,tsv['nI'][sel])[0,1],4))
print("hard only corr(S,minI)=", round(np.corrcoef(x[hard[sel]],y[hard[sel]])[0,1],4), "n hard", hard[sel].sum())
