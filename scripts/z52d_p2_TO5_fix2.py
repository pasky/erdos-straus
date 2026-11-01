"""z52d_p2_TO5_fix2.py — lint-fix round for TO5 (computational items Z1708, Z1761, Z1730, Z1780, Z1837, Z1688).
usage: python3 scripts/z52d_p2_TO5_fix2.py"""
import math, collections, itertools, statistics as st
D='data/z52b/pass2/TO5/'
mbm={}
for l in open(D+'mbm_1e6.txt'):
    if l.startswith('#'): continue
    a=l.split()
    if len(a)<6: continue
    n,isp,R,M0,MB=int(a[0]),int(a[1]),int(a[2]),float(a[3]),float(a[4])
    if isp and n%4==1 and n>=5 and MB>0: mbm[n]=(R,MB)
P=sorted(mbm)
def corr(x,y):
    mx,my=st.mean(x),st.mean(y); sx=math.sqrt(sum((a-mx)**2 for a in x)); sy=math.sqrt(sum((b-my)**2 for b in y))
    return sum((a-mx)*(b-my) for a,b in zip(x,y))/(sx*sy)
hard=[p for p in P if mbm[p][0]/mbm[p][1]<0.25]
# ---------- Z1708: splitting of x^3-x-1 mod p (3 roots <=> split completely in splitting field) ----------
def polymulmod(a,b,f,p):
    # a,b lists of coeffs low->high, f monic cubic x^3 = -(f0 + f1 x + f2 x^2)
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%p
    # reduce modulo f (monic degree 3)
    for d in range(len(r)-1,2,-1):
        c=r[d]
        if c:
            r[d]=0
            # x^d = x^{d-3} * x^3 = x^{d-3} * (-(f0+f1 x+f2 x^2))
            for k in range(3): r[d-3+k]=(r[d-3+k]-c*f[k])%p
    return (r+[0,0,0])[:3]
def polypowmod_x(e,f,p):
    res=[1,0,0]; base=[0,1,0]
    while e:
        if e&1: res=polymulmod(res,base,f,p)
        base=polymulmod(base,base,f,p); e>>=1
    return res
def ptrim(a):
    a=list(a)
    while a and a[-1]==0: a.pop()
    return a
def pmod(a,b,p):
    a=ptrim([x%p for x in a]); b=ptrim([x%p for x in b])
    inv=pow(b[-1],p-2,p)
    while len(a)>=len(b):
        c=a[-1]*inv%p; sh=len(a)-len(b)
        for i,y in enumerate(b): a[sh+i]=(a[sh+i]-c*y)%p
        a=ptrim(a)
        if not a: break
    return a
def pgcd(a,b,p):
    a=ptrim([x%p for x in a]); b=ptrim([x%p for x in b])
    while b:
        a,b=b,pmod(a,b,p)
    return a
def nroots_cubic(f,p):
    # f = [f0,f1,f2,1] monic cubic; roots = deg gcd(x^p - x, f)
    xp=polypowmod_x(p,f[:3],p)            # x^p mod f
    g=[(xp[0]-0)%p,(xp[1]-1)%p,xp[2]%p]  # x^p - x
    gg=pgcd(f,g,p)
    return len(gg)-1
f=[-1%10**9,-1%10**9,0]  # placeholder not used
F=[-1,-1,0]   # x^3 - x - 1 : x^3 = 1 + x  -> reduction x^3 = -(f0+f1 x+f2 x^2) with f0=-1,f1=-1,f2=0
# verify nroots on small primes by brute force
for q in (7,11,13,23,29,31,37,41,43):
    bf=sum(1 for x in range(q) if (x**3-x-1)%q==0)
    assert bf==nroots_cubic(F+[1],q), (q,bf,nroots_cubic(F+[1],q))
cnt=collections.Counter(nroots_cubic(F+[1],p) for p in P)
print("== Z1708 splitting of x^3-x-1 mod p over p≡1(4), p≤1e6 (roots: count)", dict(cnt))
def split(p): return nroots_cubic(F+[1],p)==3
base=sum(split(p) for p in P)/len(P)
hs=sum(split(p) for p in hard)/len(hard)
print("  P(split completely) overall %.4f (Chebotarev 1/6 for the S3 splitting field, modulo the quadratic subfield ≡ (-23/p)=1 cases); among hard primes (R/M<0.25, n=%d): %.4f"%(base,len(hard),hs))
rat=[mbm[p][0]/mbm[p][1] for p in P]
sp=[mbm[p][0]/mbm[p][1] for p in P if split(p)]; ns=[mbm[p][0]/mbm[p][1] for p in P if nroots_cubic(F+[1],p)==1]
print("  mean R/M: split completely %.3f (n=%d) vs 1 root %.3f (n=%d); fraction of primes with R=0 among split: %.4f"%(st.mean(sp),len(sp),st.mean(ns),len(ns),sum(1 for p in P if split(p) and mbm[p][0]==0)/max(1,sum(split(p) for p in P))))
# control matched on (-23/p) (quadratic subfield): compare split vs non-split within the same quadratic character
def leg(q,p): return 1 if pow(q%p,(p-1)//2,p)==1 else -1
for sgn in (1,-1):
    S=[mbm[p][0]/mbm[p][1] for p in P if leg(-23,p)==sgn and split(p)]; N=[mbm[p][0]/mbm[p][1] for p in P if leg(-23,p)==sgn and not split(p) and nroots_cubic(F+[1],p)==1]
    if S and N: print("  matched on (-23/p)=%+d: split mean R/M %.3f (n=%d) vs 1-root %.3f (n=%d)"%(sgn,st.mean(S),len(S),st.mean(N),len(N)))
# ---------- Z1761: greedy Egyptian expansion of all a/p ----------
def greedy_depth(a,p,cap=60):
    num,den=a,p; L=0
    while num>0 and L<cap:
        x=-(-den//num); L+=1
        num,den=num*x-den, den*x
        g=math.gcd(num,den)
        if g>1: num//=g; den//=g
    return L if num==0 else None
Ps=[p for p in P if p<=2000]
dist=collections.Counter(); le3=[]; depth_hard=collections.Counter()
for p in Ps:
    ds=[greedy_depth(a,p) for a in range(1,p)]
    c=collections.Counter(ds); 
    le3.append(sum(v for k,v in c.items() if k is not None and k<=3)/(p-1))
    dist.update(c)
print("== Z1761 greedy-Egyptian depth of all a/p (p≡1(4), p≤2000, %d primes): depth counts"%len(Ps), {k:v for k,v in sorted(dist.items(), key=lambda kv:(kv[0] is None, kv[0] or 0))})
print("  average fraction of a with greedy depth ≤3: %.4f ; for a=4: depth 3 for %d of %d primes"%(st.mean(le3), sum(1 for p in Ps if greedy_depth(4,p)<=3), len(Ps)))
hp=[p for p in Ps if p in set(hard)]
print("  hard primes (R/M<0.25) among these: %d; their mean fraction of a with depth ≤3: %.4f vs all %.4f"%(len(hp), st.mean([le3[Ps.index(p)] for p in hp]) if hp else float('nan'), st.mean(le3)))
# ---------- Z1730: CF length of a/p ----------
def cf_len(a,p):
    x,y=a,p; L=0
    while y:
        x,y=y,x%y; L+=1
    return L
Ps2=[p for p in P if p<=10**4]
meanL=[]; c3=[]
for p in Ps2:
    ls=[cf_len(a,p) for a in range(1,p)]
    meanL.append(st.mean(ls)); c3.append(sum(1 for l in ls if l<=3)/(p-1))
print("== Z1730 CF length of a/p (p≡1(4), p≤1e4, n=%d): mean length vs (12 ln2/π²) ln p:"%len(Ps2))
print("  corr(mean CF length, ln p)=%+.4f ; mean length / ln p = %.4f (Heilbronn/Baladi–Vallée constant 12 ln2/π² = %.4f)"%(corr(meanL,[math.log(p) for p in Ps2]), st.mean([m/math.log(p) for m,p in zip(meanL,Ps2)]), 12*math.log(2)/math.pi**2))
rr=[mbm[p][0]/mbm[p][1] for p in Ps2]
print("  corr(fraction of a/p with CF length ≤3, R/M) = %+.4f ; corr(same, ln p) = %+.4f"%(corr(c3,rr), corr(c3,[math.log(p) for p in Ps2])))
# ---------- Z1780: omega(4Cp+1) for hard slices ----------
def factor_small(n):
    f={}; d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
om=collections.Counter(); maxw=0; tot=0
for p in hard+[p for p in P if mbm[p][0]==0]:
    for C in range(1,31):
        w=len(factor_small(4*C*p+1)); om[w]+=1; maxw=max(maxw,w); tot+=1
print("== Z1780 omega(4Cp+1), C≤30, hard primes + (★)-failures (%d slices): distribution"%tot, dict(sorted(om.items())), "; max omega %d -> 2^omega ≤ %d subsets"%(maxw,2**maxw))
# ---------- Z1837: F_2 span vs subset products for 4C=24 ----------
def bits24(a):  # (Z/24)^x ≅ (Z/2)^3 via chi_{-4}, chi_8, chi_{-3}
    def chi_m4(a): return 0 if a%2==0 else (0 if a%4==1 else 1)
    def chi_8(a): return 0 if a%8 in (3,5)==False and a%8 in (1,7) and False else (0 if a%8 in (1,7) else 1)
    def chi_m3(a): return 0 if a%3==1 else 1
    return (chi_m4(a), chi_8(a), chi_m3(a))
units24=[a for a in range(1,24) if math.gcd(a,24)==1]
assert len({bits24(a) for a in units24})==8
def span_contains(vecs,target):
    # F2 span of vectors in F2^3 (as ints)
    S={0}
    for v in vecs:
        S|={s^v for s in S}
    return target in S
mone=bits24(23)
agree=collections.Counter()
for p in P:
    for C in (6,):   # 4C=24
        N=24*p+1; f=factor_small(N)
        ds=[1]
        for q,e in f.items():
            ds=[d*q**k for d in ds for k in range(e+1)]
        sub=any(d%24==23 for d in ds if d>1 and d<N)
        vecs=[bits24(q) for q in f if math.gcd(q,24)==1]
        vint=[(b[0]<<2)|(b[1]<<1)|b[2] for b in vecs]
        sp=span_contains(vint,(mone[0]<<2)|(mone[1]<<1)|mone[2])
        agree[(sub,sp)]+=1
print("== Z1837 (4C=24) over all p≡1(4), p≤1e6: (subproduct=-1, F2-span contains -1) counts:", dict(agree))
# ---------- Z1688: tropical cones and realised valuation patterns ----------
trop=[]
for a,b,c in itertools.product(range(-3,4),repeat=3):
    vals=[a+b+c, 1+a+b, 1+b+c, 1+a+c]
    m=min(vals)
    if vals.count(m)>=2: trop.append((a,b,c))
print("== Z1688 tropical points in [-3,3]^3 of 4xyz=n(xy+yz+zx), v_p(n)=1: %d points"%len(trop))
# realised valuation vectors of ALL positive solutions of 4/p=1/x+1/y+1/z for small p
def vp(n,p):
    k=0
    while n%p==0: n//=p; k+=1
    return k
real=collections.Counter()
for p in [q for q in range(5,120) if all(q%d for d in range(2,q)) and q%4==1]:
    for x in range(p//4+1, 3*p//4+2):
        # 1/y+1/z = 4/p - 1/x = (4x-p)/(px)
        num=4*x-p; den=p*x
        if num<=0: continue
        for y in range(max(x,-(-den//num)), 2*den//num+2):
            rem_num=num*y-den; 
            if rem_num<=0: continue
            if (den*y)%rem_num==0:
                z=den*y//rem_num
                if z>=y:
                    real[tuple(sorted([vp(x,p),vp(y,p),vp(z,p)]))]+=1
print("  realised p-adic valuation multisets (v(x),v(y),v(z)) over solutions with 4/p, p≡1(4), p<120:", dict(real))
print("  tropical multisets:", sorted(set(tuple(sorted([a,b,c])) for a,b,c in trop if min(a,b,c)>=0 and max(a,b,c)<=2)))
