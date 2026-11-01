"""z52d_p2_TO5_fix1.py — lint-fix round for TO5 (data-based items).
Z1768: data-based evader thresholds f(Q)=min{p≡1 mod 840 : min certificate modulus 4uB > Q} (p ≤ 1e6, from certs2 minuB).
Z1871: dossier densities of PROVED/forcing necessary conditions among p≡1 (mod 4), p≤1e6 and their joint count.
Z1873: failure counts of unions of B-slices (K=1..6) and of the (★) statement, p≡1 (mod 4), p≤1e6.
Z1850: least interior endpoint u(p) of I3 words: solutions t,u,v≥3 of tuv-u-v=p, least u; distribution up to 1e6, + evader model.
usage: python3 scripts/z52d_p2_TO5_fix1.py"""
import math, collections
import numpy as np
D='data/z52b/pass2/TO5/'
mbm={}
for l in open(D+'mbm_1e6.txt'):
    if l.startswith('#'): continue
    a=l.split()
    if len(a)<6: continue
    n,isp,R,M0,MB=int(a[0]),int(a[1]),int(a[2]),float(a[3]),float(a[4])
    if isp and n%4==1 and n>=5: mbm[n]=(R,M0,MB)
cert={}
for l in open(D+'certs2_1e6.txt'):
    a=list(map(int,l.split())); cert[a[0]]=a
P=sorted(mbm)
# ---------- Z1768 ----------
print("== Z1768 data-based evader thresholds (p≡1 mod 840, p≤1e6)")
P840=[p for p in P if p%840==1]
mod_min={p:(4*cert[p][3] if cert[p][3]>0 else 10**9) for p in P840}   # smallest certificate modulus 4uB
for Q in (10,50,100,200,500,1000,2000,5000):
    ev=[p for p in P840 if mod_min[p]>Q]
    print("  Q=%5d: first evader p=%s ; #evaders among %d primes ≡1(840) ≤1e6: %d"%(Q, ev[0] if ev else None, len(P840), len(ev)))
zero=[p for p in P if mbm[p][0]==0]
print("  (★)-failures (all p≡1(4), ≤1e6): %d = %s"%(len(zero),zero))
print("  (★)-failures ≡1(840): ",[p for p in zero if p%840==1])
# ---------- Z1871 ----------
print("== Z1871 dossier densities (p≡1 mod 4, p≤1e6, n=%d)"%len(P))
def leg(q,p): return 1 if pow(q,(p-1)//2,p)==1 else -1
C0=[p for p in P if leg(3,p)==1 and leg(5,p)==1 and leg(7,p)==1]          # forcing lines F_3,F_5,F_7 not firing
M=[p for p in P if p%840 in (1,121,169,289,361,529)]                       # Mordell square classes mod 840
print("  C0 (all-QR 3,5,7): %d = %.4f ; Mordell square classes mod 840: %d = %.4f"%(len(C0),len(C0)/len(P),len(M),len(M)/len(P)))
Bfail={B:set() for B in range(1,7)}
# B=1 exact criterion (verified); B>=2 slice: p+B has a divisor ≡ -1 (mod 4B) (no gcd filter, as in misc)
def divisors_of(n):
    ds=[1]; m=n; d=2
    while d*d<=m:
        if m%d==0:
            e=0
            while m%d==0: m//=d; e+=1
            ds=[x*d**k for x in ds for k in range(e+1)]
        d+=1
    if m>1: ds=ds+[x*m for x in ds]
    return ds
def slice_ok(p,B):
    n=p+B
    return any(d%(4*B)==4*B-1 for d in divisors_of(n) if d>1)
Cand=[p for p in C0 if p>3]
joint=[]
slice_fail={B:set() for B in range(1,7)}
for p in P:
    fails=[B for B in range(1,7) if not slice_ok(p,B)]
    for B in fails: slice_fail[B].add(p)
print("  B-slice failure counts over all P (p≡1(4)):", {B:len(slice_fail[B]) for B in slice_fail})
for K in range(1,7):
    fk=set(p for p in P if all(p in slice_fail[B] for B in range(1,K+1)))
    print("  union of B=1..%d slices fails for %d primes (%.5f)"%(K,len(fk),len(fk)/len(P)))
both=[p for p in C0 if all(p in slice_fail[B] for B in range(1,7))]
print("  dossier-joint (all-QR cell AND all B=1..6 slices fail): %d primes: %s"%(len(both),both[:12]))
print("  (★)-failures in all-QR cell:", [p for p in zero if p in set(C0)], " ; (★)-failures in Mordell square classes mod 840:", [p for p in zero if p%840 in (1,121,169,289,361,529)])
# ---------- Z1873 ----------
print("== Z1873 ES-implying statements: failure sets on p≡1(4), p≤1e6")
print("  (★) [all pairs]: %d failures"%len(zero))
for K in (1,2,3,6):
    fk=set(p for p in P if all(p in slice_fail[B] for B in range(1,K+1)))
    print("  S_K = 'some B-slice, B≤%d, succeeds': %d failures"%(K,len(fk)))
# ---------- Z1850 ----------
print("== Z1850 least interior endpoint u(p) (I3: tuv-u-v=p, t,u,v>=3)")
def least_u(p, umax=2000):
    for u in range(3,umax):
        # need t = (p+u+v)/(u v) >= 3 integer; v >= 3, and 3uv <= p+u+v  => v <= (p+u)/(3u-1)
        Vmax=(p+u)//(3*u-1)
        if Vmax<3: return None
        v=np.arange(3,Vmax+1,dtype=np.int64)
        num=p+u+v
        ok=(num % (u*v)==0)&(num//(u*v)>=3)
        if ok.any(): return u
    return None
us={}
for p in P:
    us[p]=least_u(p)
vals=collections.Counter(us.values())
print("  distribution of least u over p≡1(4), p≤1e6:",sorted(vals.items(), key=lambda kv:(kv[0] is None, kv[0] or 0)))
mx=max(v for v in us.values() if v); print("  max u(p) = %s at p=%s ; primes with no word of endpoint <2000: %d"%(mx,[p for p in P if us[p]==mx][:3],sum(1 for v in us.values() if v is None)))
Ub={}
for U in (3,4,5,6,8,10,15,20,39):
    frac=sum(1 for p in P if (us[p] is None or us[p]>U))/len(P)
    Ub[U]=frac
print("  fraction of primes with NO I3 word with endpoint u ≤ U:", {k:round(v,6) for k,v in Ub.items()})
# Z1850 model test: independence of 'has an I3 word with endpoint u' across u (no-word-with-u≤U vs product)
def has_word(p,u):
    Vmax=(p+u)//(3*u-1)
    if Vmax<3: return False
    v=np.arange(3,Vmax+1,dtype=np.int64); num=p+u+v
    return bool(((num % (u*v)==0)&(num//(u*v)>=3)).any())
UM=13
H={u:np.array([has_word(p,u) for p in P]) for u in range(3,UM+1)}
for U in (3,4,5,6,8,10,13):
    obs=float(np.mean(~np.any(np.array([H[u] for u in range(3,U+1)]),axis=0)))
    prod=1.0
    for u in range(3,U+1): prod*=1-float(H[u].mean())
    print("  Z1850 model: P(no word with endpoint <= %d): observed %.6f vs product of marginals %.6f"%(U,obs,prod))
print("  Z1850 marginal densities d_u (P has a word with endpoint u):", {u:round(float(H[u].mean()),4) for u in range(3,UM+1)})
