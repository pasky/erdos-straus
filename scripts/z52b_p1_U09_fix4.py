# z52b pass1 U09 (fix round 4): Z0582 (least root of x^2≡-1 mod p), Z1543 (max f(p)/log^2 p), Z1820 (least C with Ω(4Cp+1)≤2),
# Z1953 (class coverage by certificate levels), Z2065/Z2371 (prime factors q of 4p+1 for the R=0 primes and their R-values).
import math, numpy as np, collections
rows=[list(map(int,l.split())) for l in open('data/z52b/pass1/U09/R7.txt')]
P=[r[0] for r in rows]; Rv={r[0]:r[1] for r in rows}; masks={r[0]:r[4] for r in rows}
M=4*10**6+10
spf=np.zeros(M+1,dtype=np.int64)
for i in range(2,M+1):
    if spf[i]==0:
        spf[i::i][spf[i::i]==0]=i
def factor(n):
    f=collections.Counter()
    while n>1:
        q=int(spf[n]) if n<=M else None
        if q is None:
            d=2
            while d*d<=n and n%d: d+=1
            q=d if n%d==0 and d*d<=n else n
        f[q]+=1; n//=q
    return f
# Z0582: least root x of x^2 ≡ -1 (mod p), p≡1 mod 4, p<=2e5
roots=[]
for p in P[:3000]:
    for x in range(1,p):
        if (x*x+1)%p==0: roots.append((p,x)); break
ex=[math.log(x)/math.log(p) for p,x in roots]
print(f"Z0582: least root exponent log(x)/log(p): median {np.median(ex):.3f}, 90% {np.percentile(ex,90):.3f}, max {max(ex):.3f} (n={len(ex)}, p<={P[2999]})")
print("   fraction with x <= p^{1/4}:", round(float(np.mean([x<=p**0.25 for p,x in roots])),3))
# Z1543: f(p)/log^2 p from fullf file (p<=12000)
f=np.loadtxt('data/z52b/pass1/U09/fullf_le12000.txt',dtype=np.int64)
r=f[:,1]/np.log(f[:,0].astype(float))**2
print(f"Z1543: f(p)/log^2 p over p≤1.2e4: max {r.max():.3f} at p={int(f[np.argmax(r),0])}, mean {r.mean():.3f}; max f(p)={int(f[:,1].max())} at p={int(f[np.argmax(f[:,1]),0])}")
print("   f(p) ≤ p^0.1 ? fraction:", round(float(np.mean(f[:,1] <= f[:,0]**0.1)),3), " max f(p)/p^0.1:", round(float((f[:,1]/f[:,0]**0.1).max()),3))
# Z1820: least C with Omega(4Cp+1) <= 2 (C up to 200)
ls=[]
for p in P[:1500]:
    best=0
    for C in range(1,200):
        N=4*C*p+1
        if N>M: break
        Om=sum(factor(N).values())
        if Om<=2: best=C; break
    ls.append(best)
ls=np.array(ls)
print(f"Z1820: least C≤199 with Ω(4Cp+1)≤2 over first 1500 primes ≡1(4): none found for {int(np.sum(ls==0))}; C-distribution quantiles 50/90/99: {np.percentile(ls[ls>0],[50,90,99]) if (ls>0).any() else None}")
# Z1953: classes mod 840 (p≡1 mod 4) where some prime is not covered by C<=K (C=1 witness for K... cumulative)
cls=collections.defaultdict(list)
for p in P:
    cls[p%840].append(p)
for K in [1,2,4,8,16,64]:
    unc=0; tot=0
    for c,ps in cls.items():
        if len(ps)<3: continue
        tot+=1
        if any(all(((masks[p]>>(C-1))&1)==0 for C in range(1,K+1)) for p in ps): unc+=1
    print(f"Z1953: K={K}: classes mod 840 (≥3 primes) containing a prime with no witness C≤K: {unc}/{tot}")
# Z2065 / Z2371: for R=0 primes, factor 4p+1 and report prime factors q with R(q)>0 (q ≤ 2e5) and q mod 4
zeros=[p for p in P if Rv[p]==0]
for p in zeros:
    fac=factor(4*p+1)
    info=[(q, q%4, Rv.get(q,'>2e5')) for q in fac]
    print(f"Z2371: zero prime {p}: 4p+1 = {dict(fac)} ; (factor, mod4, R(factor)) = {info}")
