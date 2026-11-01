"""z52d_p2_TO5_fix4.py — lint-fix round for TO5, part 4:
Z1910/Z1940 (non-degenerate ℤ[T] identities: x,y,z nonconstant-or-nonzero, n with positive leading coefficient),
Z1734 (random multiplicative model for the spread of T(p)), Z1773 (search-order programs), Z1730 (slope), Z1896 (fixed points).
usage: python3 scripts/z52d_p2_TO5_fix4.py"""
import math, collections, statistics as st, random
import numpy as np
D='data/z52b/pass2/TO5/'
mbm={}
for l in open(D+'mbm_1e6.txt'):
    if l.startswith('#'): continue
    a=l.split()
    if len(a)<6: continue
    n,isp,R,M0,MB=int(a[0]),int(a[1]),int(a[2]),float(a[3]),float(a[4])
    if isp and n%4==1 and n>=5 and MB>0: mbm[n]=(R,M0,MB)
P=sorted(mbm)
def corr(x,y):
    mx,my=st.mean(x),st.mean(y); sx=math.sqrt(sum((a-mx)**2 for a in x)); sy=math.sqrt(sum((b-my)**2 for b in y))
    return sum((a-mx)*(b-my) for a,b in zip(x,y))/(sx*sy)
def pmul(p1,p2):
    r=[0]*(len(p1)+len(p2)-1)
    for i,x in enumerate(p1):
        for j,y in enumerate(p2): r[i+j]+=x*y
    return r
def padd(*ps):
    L=max(len(p) for p in ps); r=[0]*L
    for p in ps:
        for i,x in enumerate(p): r[i]+=x
    return r
def iszero(p): return all(v==0 for v in p)
# ---------- Z1910 / Z1940 : non-degenerate identities ----------
lin=[[b,a] for a in range(-3,4) for b in range(-3,4) if not (a==0 and b==0)]    # nonzero linear forms const+T*coef
quads=[[c,b,a] for a in range(-3,4) for b in range(-3,4) for c in range(-3,4) if a>0]   # n(T) with positive leading coeff
def posT(p): # leading coefficient positive (so positive for large T)
    for v in reversed(p):
        if v!=0: return v>0
    return False
def run(signed):
    cnt=0; ex=[]
    for i,X in enumerate(lin):
        for j,Y in enumerate(lin):
            if j<i: continue
            for k,Z in enumerate(lin):
                if k<j: continue
                if not (posT(X) and posT(Y) and posT(Z)): continue     # x,y,z positive for large T
                lhs=[4*c for c in pmul(pmul(X,Y),Z)]
                if signed: rhs2=padd(pmul(Y,Z),pmul(X,Z),[-c for c in pmul(X,Y)])
                else: rhs2=padd(pmul(X,Y),pmul(Y,Z),pmul(X,Z))
                if iszero(rhs2): continue
                for q in quads:
                    rhs=pmul(q,rhs2)
                    L=max(len(lhs),len(rhs))
                    d=padd(lhs+[0]*(L-len(lhs)), [-x for x in rhs]+[0]*(L-len(rhs)))
                    if iszero(d):
                        cnt+=1
                        if len(ex)<4: ex.append((X,Y,Z,q))
    return cnt,ex
c1,e1=run(False)
print("== Z1910 non-degenerate positive identities 4xyz = n(xy+yz+zx) over Z[T] (x,y,z linear, positive leading coeff; n quadratic, lead>0): %d ; examples [const,T]: %s ; n [const,T,T²]: %s"%(c1,[(e[0],e[1],e[2]) for e in e1],[e[3] for e in e1]))
c2,e2=run(True)
print("== Z1940 non-degenerate signed identities 4/n = 1/x+1/y-1/z over Z[T] (x,y,z positive for large T, n quadratic lead>0): %d ; examples: %s"%(c2,[(e[0],e[1],e[2],e[3]) for e in e2]))
# ---------- Z1734 ----------
print("== Z1734 random multiplicative model for T(p)")
Xmax=250000
spf=np.zeros(Xmax+1,dtype=np.int64)
for i in range(2,Xmax+1):
    if spf[i]==0: spf[i::i][spf[i::i]==0]=i
phi=np.arange(Xmax+1,dtype=np.float64); omega=np.zeros(Xmax+1,dtype=np.int64)
for i in range(2,Xmax+1):
    if spf[i]==i:
        phi[i::i]*=(1-1.0/i); omega[i::i]+=1
W=np.zeros(Xmax+1); ev=np.arange(2,Xmax+1,2); W[ev]=(2.0**omega[ev])/(4*phi[ev])
bigP=[p for p in P if 9*10**5<p<=10**6]
Tr=[mbm[p][1]-mbm[p][2] for p in bigP]
print("  real T(p), p∈(9e5,1e6], n=%d: mean %.4f sd %.4f ; M0 mean %.4f"%(len(Tr),st.mean(Tr),st.pstdev(Tr),st.mean(mbm[p][1] for p in bigP)))
rng=np.random.default_rng(1)
samples=[]
for trial in range(300):
    # completely multiplicative random signs on primes ≤ Xmax
    f=np.zeros(Xmax+1,dtype=np.int64); f[1]=1
    sg=rng.choice([-1,1],size=Xmax+1)
    for m in range(2,Xmax+1):
        q=spf[m]; f[m]=sg[q]*f[m//q]
    samples.append(float(np.sum(f[ev]*W[ev])))
print("  random-f model T_f (300 draws): mean %.4f sd %.4f  (vs real sd %.4f, real mean %.4f)"%(st.mean(samples),st.pstdev(samples),st.pstdev(Tr),st.mean(Tr)))
print("  real T quantiles 5/50/95%%: %s ; model: %s"%([round(float(np.quantile(Tr,q)),3) for q in (0.05,0.5,0.95)],[round(float(np.quantile(samples,q)),3) for q in (0.05,0.5,0.95)]))
# ---------- Z1773: search-order programs ----------
print("== Z1773 search programs for a certificate (p≡1(4), p≤5000): mean/max number of pairs examined before the first certificate")
def pairs_for(p):
    out=[]
    for u in range(1,(p+2)//3+1):
        for B in range(1,(p+u)//(4*u-1)+1):
            if (u+B)%2==0: continue
            if math.gcd(u,B)!=1: continue
            out.append((u,B))
    return out
orders={'by u+B':lambda t:(t[0]+t[1],t[0]),'by uB':lambda t:(t[0]*t[1],t[0]),'by B then u':lambda t:(t[1],t[0]),'by u then B':lambda t:(t[0],t[1]),'by max(u,B)':lambda t:(max(t),t[0])}
res={k:[] for k in orders}; fails=0; tot=0
for p in [q for q in P if q<=5000]:
    prs=pairs_for(p); tot+=1
    cert=[t for t in prs if (p+t[0]+t[1])%(4*t[0]*t[1])==0]
    if not cert: fails+=1; continue
    for k,key in orders.items():
        srt=sorted(prs,key=key)
        idx=next(i for i,t in enumerate(srt) if (p+t[0]+t[1])%(4*t[0]*t[1])==0)
        res[k].append(idx+1)
print("  primes %d (no certificate: %d)"%(tot,fails))
for k in orders: print("  order %-12s mean pairs examined %.1f  max %d  median %d"%(k,st.mean(res[k]),max(res[k]),sorted(res[k])[len(res[k])//2]))
# ---------- Z1730 slope ----------
def cf_len(a,p):
    x,y=a,p; L=0
    while y:
        x,y=y,x%y; L+=1
    return L
xs=[];ys=[]
for p in [q for q in P if 1000<=q<=10**4][::4]:
    ls=[cf_len(a,p) for a in range(1,p)]
    xs.append(math.log(p)); ys.append(st.mean(ls))
mx,my=st.mean(xs),st.mean(ys)
slope=sum((a-mx)*(b-my) for a,b in zip(xs,ys))/sum((a-mx)**2 for a in xs)
print("== Z1730 mean CF length of a/p vs ln p (p∈[1e3,1e4], %d primes): slope %.4f (Heilbronn: 12 ln2/π² = %.4f)"%(len(xs),slope,12*math.log(2)/math.pi**2))
# ---------- Z1896 ----------
fixed=0; tot=0
for p in P[:3000]:
    for u in range(1,(p+2)//3+1):
        for B in range(u,(p+u)//(4*u-1)+1):   # swap-fixed points have B=u
            if B==u and math.gcd(u,B)==1 and (u+B)%2==1: fixed+=1
    tot+=1
print("== Z1896 swap-involution (u,B)→(B,u) on the trial set: fixed points with u=B among %d primes: %d (requires u=B=1, excluded since u+B odd)"%(tot,fixed))
