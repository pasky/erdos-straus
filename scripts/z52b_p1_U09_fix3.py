# z52b pass1 U09 (fix round 3):
#  Z0520: primes p≡1 (24), p<=N: does some ES solution have a PRIME denominator?  (full enumeration, validated code)
#  Z0669: pairwise independence ratios of C-events E_C(p) = [C works for p] (C<=64, from R7.txt bitmask), grouped by characters
#  Z0622/Z0621/Z0620/Z0585: representation exceptions for odd n (p+2^a3^b, p+x^3, p+k!) and even n (difference of primes)
#  Z0657: least prime p≡1 mod 840 with (p/ℓ)=+1 for all primes ℓ≤50 (ℓ∤840), and least p ≡1 mod 24 with same.
import sys, math, collections
import numpy as np
N=int(sys.argv[1]) if len(sys.argv)>1 else 6000
src=open("scripts/z52b_p1_U09_fullf.py").read().split("out=[]")[0].replace("N = int(sys.argv[1]) if len(sys.argv)>1 else 5000","N = %d" % N)
ns={}; exec(compile(src,"ff","exec"),ns)
spf=ns['spf']; dv=ns['divisors_of_b2']
def isprime_td(n):
    if n<2: return False
    if n<=N: return spf[n]==n
    for q in range(2,int(n**0.5)+1):
        if n%q==0: return False
    return True
def has_prime_denom(p):
    for x in range(math.ceil(p/4),(3*p)//4+1):
        a=4*x-p; b=p*x
        if a<=0: continue
        for d1 in dv(p,x):
            if d1%a==(-b)%a and d1>0:
                d2=(b*b)//d1
                if d2%a==(-b)%a:
                    y=d1+b; z=d2+b
                    if y%a==0 and z%a==0:
                        y//=a; z//=a
                        if x<=y<=z:
                            ds=(x,y,z)
                            if any(isprime_td(d) for d in ds): return True
    return False
pp=[q for q in range(5,N+1) if spf[q]==q and q%24==1]
hits=[p for p in pp if has_prime_denom(p)]
print(f"Z0520: primes p≡1 (24), p<={N}: {len(pp)}; with an ES solution having a prime denominator: {len(hits)} (missing: {[p for p in pp if p not in set(hits)][:15]})")
# ---- Z0669
rows=[list(map(int,l.split())) for l in open('data/z52b/pass1/U09/R7.txt')]
masks=[r[4] for r in rows]
E=np.array([[(int(m)>>c)&1 for c in range(64)] for m in masks],float)  # primes x C(1..64)
Pm=E.mean(axis=0)
C=np.arange(1,65)
def joint(i,j):
    return (E[:,i]*E[:,j]).mean()
groups=collections.defaultdict(list)
for i in range(64):
    for j in range(i+1,64):
        if Pm[i]==0 or Pm[j]==0: continue
        ratio=joint(i,j)/(Pm[i]*Pm[j])
        ci,cj=C[i],C[j]
        k1=((-1)**((ci-1)//2)) * ((-1)**((cj-1)//2))   # χ_{-4}(C)χ_{-4}(C') (C odd only matters); use C mod 4 instead:
        key=("both≡1(4)" if ci%4==1 and cj%4==1 else "both≡3(4)" if ci%4==3 and cj%4==3 else "mixed")
        groups[key].append(ratio)
        groups["C·C' square" if int(round(math.sqrt(ci*cj)))**2==ci*cj else "C·C' nonsquare"].append(ratio)
for k,v in groups.items():
    print(f"Z0669 group {k}: pairs {len(v)}, mean independence ratio {np.mean(v):.4f}, median {np.median(v):.4f}")
print("   overall mean ratio all pairs:", round(float(np.mean([x for v in groups.values() for x in v if False] or [0])),3) if False else "")
# ---- Z0622 / Z0621 / Z0620 / Z0585
M=10**6
isp=np.ones(M+1,bool); isp[:2]=False
for i in range(2,int(M**0.5)+1):
    if isp[i]: isp[i*i::i]=False
odd=np.arange(3,M+1,2)
def exceptions_from_set(ns_, cand_fn, nums):
    rep=np.zeros(len(nums),bool)
    for s in cand_fn():
        idx=nums-s
        ok=(idx>=2)&(idx<=M)
        rep[ok]|=isp[idx[ok]]
    return nums[~rep]
# Z0622: odd n = p + 2^a 3^b
def smooth_gen():
    for a in range(0,21):
        for b in range(0,14):
            v=(2**a)*(3**b)
            if v<=M: yield v
ex622=exceptions_from_set(None, lambda: smooth_gen(), odd)
print(f"Z0622: odd n in [3,{M}] not of form p+2^a3^b: {len(ex622)} ; largest 10: {ex622[-10:].tolist()}")
for T in [10**4,10**5,10**6]: print(f"   count ≤{T}: {int(np.sum(ex622<=T))}")
# Z0621: odd n = p + x^3 (x>=1)
ex621=exceptions_from_set(None, lambda: (x**3 for x in range(1,101)), odd)
print(f"Z0621: odd n in [3,{M}] not p + x^3 (x≤100): {len(ex621)} ; first: {ex621[:12].tolist()}")
for T in [10**4,10**5,10**6]: print(f"   count ≤{T}: {int(np.sum(ex621<=T))}")
# Z0620: n = p + k!  (k>=2; 1!=2!=1 so start at 2!=2)
facs=[]; f=1
for k in range(1,12):
    f*=k
    if f<=M: facs.append(f)
ex620=exceptions_from_set(None, lambda: iter(facs), odd)
print(f"Z0620: odd n in [3,{M}] not p+k! : {len(ex620)} (k! up to 11!); first: {ex620[:12].tolist()}")
# even n = difference of two primes (in infinitely many ways): min representation count r(n), n<=1e5
Ns=np.arange(4,100001,2)
cnt=np.zeros(len(Ns),int)
for i,n in enumerate(Ns):
    pass
# vectorised: for each prime q<=1e5 check q+n prime
smallp=np.flatnonzero(isp[:100001+10**6 if False else 100001])
isp_ = isp
Mx=100001+100000
cnt=np.zeros(len(Ns),int)
for q in smallp[smallp<=10**5]:
    tgt=q+Ns
    ok=(tgt<=M)
    cnt[ok]+=isp[tgt[ok]]
print(f"Z0585: even n in [4,1e5]: min #{{(p,q): p-q=n, p,q prime, p≤{M}}} = {cnt.min()}; #n with count 0: {int(np.sum(cnt==0))}; median {int(np.median(cnt))}")
# ---- Z0657
def least_p(q, ells):
    for p in range(q+1, 10**6, q):
        if not isp[p]: continue
        if all(pow(p%l,(l-1)//2,l)==1 for l in ells if l!=p):
            return p
    return None
ells=[l for l in range(3,51) if isp[l] and 840%l!=0]
print("Z0657: least prime p≡1 (840) with (p/ℓ)=+1 for all primes ℓ≤50, ℓ∤840:", least_p(840,ells))
ells2=[l for l in range(3,51) if isp[l] and 24%l!=0]
print("   least prime p≡1 (24) with (p/ℓ)=+1 for all primes ℓ≤50, ℓ∤24:", least_p(24,ells2))
print("   least prime p≡1 (840) with no splitting condition:", least_p(840,[]))
