# z52b pass1 U09 (fix round): concrete first steps for Z0440, Z0494, Z0593, Z0604, Z1071, Z1189, Z1235, Z1419, Z2233, Z0863.
# Data: data/z52b/pass1/U09/R7.txt  (cols: p R minC minMax mask u_at_minC B_at_minC), primes ≡1 (4), p<=2e5.
import sys, math, zlib, random, collections, itertools
import numpy as np
from scipy.stats import pearsonr
rows=[list(map(int,l.split())) for l in open('data/z52b/pass1/U09/R7.txt')]
P=np.array([r[0] for r in rows]); R=np.array([r[1] for r in rows],float)
L=np.log(P.astype(float))**2; y=R/L
def leg(a,l):
    a%=l
    return 0 if a==0 else (1 if pow(a,(l-1)//2,l)==1 else -1)
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**0.5)+1))
def se_diff(a,b): return math.sqrt(a.var()/len(a)+b.var()/len(b))
def show_classes(name, keys, vals):
    d=collections.defaultdict(list)
    for k,v in zip(keys,vals): d[k].append(v)
    out=[(k,round(float(np.mean(v)),4),len(v)) for k,v in sorted(d.items()) if len(v)>=20]
    means=[m for _,m,_ in out]
    print(f"  {name}: class means {out}; spread max/min = {max(means)/min(means):.3f}")
    return out

print("== Z0440: base-b digit (leading/last) vs R/log^2 p")
for b in [3,5,6,10,12]:
    last=P % b
    lead=np.array([int(p)//(b**int(math.log(p,b))) for p in P])  # leading digit
    show_classes(f"base {b} last digit", last, y)
    show_classes(f"base {b} leading digit", lead, y)
    # digit-recursive proxy: is R=0 (or C=1 failure) concentrated in a last-digit class?
    zero=(R==0).astype(float)
    print(f"    frac(R=0) by last digit base {b}:", {int(k):round(float(zero[last==k].mean()),4) for k in range(b) if (last==k).sum()>0})

print("== Z0494: reciprocity-type correlation with (p/q), q small; also p mod 9 (p≡1 mod 24 subset)")
qs=[3,5,7,11,13,17,19,23]
for q in qs:
    s=np.array([leg(int(p),q) for p in P])
    a=y[s==1]; c=y[s==-1]
    if len(a)>1 and len(c)>1:
        z=(a.mean()-c.mean())/se_diff(a,c)
        print(f"  q={q}: mean(R/log^2 | (p/q)=+1)={a.mean():.4f} (n={len(a)}), | -1: {c.mean():.4f} (n={len(c)}), z={z:.2f}")
m24=P%24==1
show_classes("p mod 9 within p≡1 (mod 24)", (P%9)[m24], y[m24])

print("== Z0593: p = a^2+b^2 (a odd): R/log^2 vs a mod 8 and vs quartic class of a/b")
def sq_rep(p):
    for a in range(1,int(math.isqrt(p))+1):
        b2=p-a*a; b=math.isqrt(b2)
        if b*b==b2 and a%2==1: return a,b
    return None
ab=[sq_rep(int(p)) for p in P]
amod8=np.array([a%8 for a,b in ab]); bmod4=np.array([b%4 for a,b in ab])
show_classes("a mod 8 (p=a²+b², a odd)", amod8, y)
show_classes("b mod 4", bmod4, y)

print("== Z0604: local densities of 4xyz = n(xy+yz+zx) at odd q (primitive solutions mod q^k, normalised by q^{2k})")
def rho(q,k,n):
    m=q**k; cnt=0
    r=np.arange(m)
    x,yy,z=np.meshgrid(r,r,r,indexing='ij')
    F=(4*x*yy*z - n*(x*yy+yy*z+z*x)) % m
    prim=~((x%q==0)&(yy%q==0)&(z%q==0))
    return float(np.sum((F==0)&prim))/m**2
for q in [3,5,7,11]:
    sq=sorted({(t*t)%q for t in range(1,q)})
    nonsq=[n for n in range(1,q) if n not in sq]
    rs=[rho(q,1,n) for n in range(1,q)]
    print(f"  q={q}: rho(n) for n=1..q-1 {[round(v,3) for v in rs]}; squares {sq}; mean over squares {np.mean([rho(q,1,n) for n in sq]):.3f}, over non-squares {np.mean([rho(q,1,n) for n in nonsq]) if nonsq else float('nan'):.3f}")
print("  q=3,k=2 check:", [round(rho(3,2,n),3) for n in range(1,9)])

print("== Z1071: autocorrelation of R over consecutive primes (subsequences)")
for name,mask_ in [("p≡1 (mod 4), all", np.ones(len(P),bool)),("p≡1 (mod 840)", P%840==1)]:
    seq=R[mask_]
    if len(seq)>3:
        r1=pearsonr(seq[:-1],seq[1:])[0]
        print(f"  {name}: n={len(seq)}, lag-1 autocorrelation of R = {r1:.4f}")
        # shuffled baseline
        rs_=[pearsonr(np.random.permutation(seq)[:-1], np.random.permutation(seq)[1:])[0] for _ in range(200)]
        print(f"     shuffled baseline: mean {np.mean(rs_):.4f}, sd {np.std(rs_):.4f}")

print("== Z1189: compressibility of the (C,u,B) sequence of minimal triples (zlib) vs shuffled")
trip=[(r[0],r[2],r[5],r[6]) for r in rows if r[2]>0]
txt=" ".join(f"{C},{u},{B};" for p,C,u,B in trip).encode()
comp=len(zlib.compress(txt,9))
shuf=[]
for _ in range(20):
    t2=[(C,u,B) for _,C,u,B in trip]; random.shuffle(t2)
    shuf.append(len(zlib.compress(" ".join(f"{C},{u},{B};" for C,u,B in t2).encode(),9)))
print(f"  triples n={len(trip)}, raw {len(txt)} B, zlib {comp} B, shuffled-order zlib {np.mean(shuf):.0f} ± {np.std(shuf):.0f}; ratio {comp/np.mean(shuf):.4f}")
# also: the (u,B) of minimal triple: how often is min(u,B)=1 and how often C=1 among them
print("  frac C=1:", round(float(np.mean([C==1 for _,C,_,_ in trip])),4), " frac min(u,B)=1:", round(float(np.mean([min(u,B)==1 for _,_,u,B in trip])),4))

print("== Z1235: calibration of 'R>0' success prediction (train p<=1e5, test p>1e5) with class-mean predictor mod 840")
train=P<=10**5; test=~train
succ=(R>0).astype(float)
cls=P%840
pred_map={}
for c in set(cls[train]):
    m=train&(cls==c)
    pred_map[c]=succ[m].mean() if m.sum()>0 else succ[train].mean()
pt=np.array([pred_map.get(c, succ[train].mean()) for c in cls[test]])
st=succ[test]
print(f"  test n={test.sum()}, base rate {st.mean():.3f}; Brier(class predictor) {np.mean((pt-st)**2):.4f} vs Brier(base rate) {np.mean((st.mean()-st)**2):.4f}")
bins=[0,0.5,0.7,0.8,0.9,1.01]
for lo,hi in zip(bins[:-1],bins[1:]):
    s=(pt>=lo)&(pt<hi)
    if s.sum()>0: print(f"   predicted in [{lo},{hi}): n={int(s.sum())}, mean pred {pt[s].mean():.3f}, observed {st[s].mean():.3f}")

print("== Z1419: is C_min(p) mod q a function of p mod q?  (C_min = minC; purity = Σ_classes max-count / N)")
minC=np.array([r[2] for r in rows])
ok=minC>0
for q in [3,5,7,11,13,17,19,23,29,31]:
    lab=minC[ok]%q; cl=P[ok]%q
    tot=0; pur=0
    for c in range(q):
        s=lab[cl==c]
        if len(s): pur+=np.bincount(s,minlength=q).max(); tot+=len(s)
    # baseline: same class sizes, labels shuffled
    base=[]
    for _ in range(20):
        sh=np.random.permutation(lab); pb=0
        for c in range(q):
            s=sh[cl==c]
            if len(s): pb+=np.bincount(s,minlength=q).max()
        base.append(pb/tot)
    print(f"  q={q}: purity {pur/tot:.4f} vs shuffled {np.mean(base):.4f} (N={tot})")
