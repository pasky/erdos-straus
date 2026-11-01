# z52d pass2 TO4 lint-fix A: Z1025 (pairwise C-composition), Z1091 (finite-memory automaton predictability),
# Z1113 (SVD of family×prime incidence + interlacing), Z1163 (winning-pair imbalance), Z1402 (mod-840 class effect),
# Z1551 (Artin-type densities of win(p,C) per C), Z1468 (I3 census with t≡0 mod 4 vs any t)
import math, statistics, sys, random
import numpy as np
from collections import defaultdict, Counter
from sympy import primerange, factorint
rows={}
for line in open('/tmp/cf_1e7_K400.txt'):
    t=list(map(int,line.split())); rows[t[0]]=set(t[2:2+t[1]])
P24=[p for p in sorted(rows) if p%24==1 and 10**4<=p<=10**6]
print("sample p≡1 mod 24 in [1e4,1e6]:",len(P24))
# ---- Z1025: composition of partial certificates: does win(p,C1) & win(p,C2) predict win(p,C1*C2) / win(p,lcm)?
def cond(op):
    a=b=ab=0
    for p in P24:
        W=rows[p]
        for C1 in range(1,21):
            for C2 in range(C1+1,21):
                C=op(C1,C2)
                if C>400: continue
                if C1 in W and C2 in W:
                    a+=1
                    if C in W: b+=1
    return (round(b/a,3) if a else None, a)
base=Counter(); tot=0
for p in P24:
    for C in range(1,401): tot+=1; base[C in rows[p]]+=1
pr=base[True]/tot
print("Z1025 base rate win=%.3f"%pr)
for name,op in [("C1*C2",lambda x,y:x*y),("C1+C2",lambda x,y:x+y),("lcm",lambda x,y: x*y//math.gcd(x,y))]:
    cp,n=cond(op)
    print("Z1025 P(win(C))| win(C1),win(C2)) for C=%s: %s over %d pairs"%(name,cp,n))
# ---- Z1091: finite-memory automaton (last k base-b digits of p) predictor for L(p)=[C=1 wins]; train p<5e5, test p in [5e5,1e6]
def label(p): return 1 if 1 in rows[p] else 0
train=[p for p in P24 if p<5*10**5]; test=[p for p in P24 if p>=5*10**5]
print("Z1091 n_train=%d n_test=%d base rate label=%.3f"%(len(train),len(test),statistics.mean(label(p) for p in train)))
for base_ in (2,3):
    for k in (1,2,3,4,6,8):
        cnt=defaultdict(Counter)
        for p in train: cnt[p % base_**k][label(p)]+=1
        acc=0
        for p in test:
            c=cnt.get(p%base_**k)
            pred = (c.most_common(1)[0][0] if c else 0)
            acc+= (pred==label(p))
        print("Z1091 base %d, last %d digits: test accuracy %.4f (baseline %.4f)"%(base_,k,acc/len(test),max(statistics.mean(label(p) for p in test),1-statistics.mean(label(p) for p in test))))
# ---- Z1113: incidence matrix M[family C][prime p] = win(p,C), C≤40; singular values; greedy addition; interlacing check
Cs=list(range(1,41)); ps=P24[:2000]
M=np.array([[1.0 if C in rows[p] else 0.0 for p in ps] for C in Cs])
sv=np.linalg.svd(M,compute_uv=False)
print("Z1113 full M (40x%d): rank %d, smallest nonzero sv %.3f, top sv %.2f"%(len(ps),np.sum(sv>1e-9),sv[np.sum(sv>1e-9)-1],sv[0]))
# interlacing: singular values of M_k (first k rows) interlace with those of M_{k+1}
ok=True
prev=np.linalg.svd(M[:1],compute_uv=False)
for k in range(2,len(Cs)+1):
    cur=np.linalg.svd(M[:k],compute_uv=False)
    # adding a row: sv_i(new) >= sv_i(old) and sv_{i+1}(new) <= ... check Weyl (σ_i(old) ≤ σ_i(new)) and σ_i(new) ≤ σ_{i}(old)+ ... use Weyl: |σ_i(A+B)-σ_i(A)|≤σ_1(B)
    prev_pad=np.pad(prev,(0,len(cur)-len(prev)))
    if np.any(cur[:len(prev)]+1e-9 < prev): ok=False
    prev=cur
print("Z1113 interlacing (σ_i nondecreasing under row addition, Weyl) holds:",ok)
# greedy: family whose addition raises the smallest nonzero singular value of the current span most
S=[1]; rem=[C for C in Cs if C!=1]
def smin_nz(idx):
    s=np.linalg.svd(M[[i-1 for i in idx]],compute_uv=False)
    nz=s[s>1e-9]; return nz[-1] if len(nz) else 0
order=[]
while rem and len(order)<8:
    best=max(rem,key=lambda C: smin_nz(S+[C]))
    S.append(best); rem.remove(best); order.append((best,round(smin_nz(S),3)))
print("Z1113 greedy order (family, smallest nonzero σ after adding):",order)
# ---- Z1163: imbalance of winning pairs (a, N/a) for C-form witnesses; cusp-type excursion vs hardness
# (uses winning divisors computed exactly for p≡1 mod 24 ≤ 2e4, C≤30)
imb_first=[]; imb_all=[]; hard=[]
for p in primerange(5,20001):
    if p%24!=1: continue
    ws=[]
    for C in range(1,31):
        N=4*C*p+1; m=4*C
        f=factorint(N); divs=[1]
        for q,k in f.items(): divs=[d*q**j for d in divs for j in range(k+1)]
        W=[a for a in divs if a>1 and a%m==m-1]
        for a in W: imb_all.append(math.log(max(a,N//a)/min(a,N//a)))
        if W: ws.append(min(W))
    hard.append(len(ws))
print("Z1163 winning-pair log-imbalance: median %.2f, 90%% %.2f (n=%d winning divisors)"%(statistics.median(imb_all),sorted(imb_all)[int(.9*len(imb_all))],len(imb_all)))
# ---- Z1402: is win(p,C) (C≤20) explained by p mod 840 ? variance explained by residue class (mod 840) vs null
res=defaultdict(lambda: defaultdict(list))
allp=[p for p in rows if p>=10**4 and p%4==1]
for p in allp[:150000]:
    for C in range(1,21):
        res[p%840][C].append(1 if C in rows[p] else 0)
tot_var=0; between=0; n_all=0
for C in range(1,21):
    xs=[v for r in res for v in res[r][C]]
    mu=statistics.mean(xs); tot_var+=statistics.pvariance(xs)*len(xs); n_all+=len(xs)
    for r in res:
        v=res[r][C]
        if v: between+=len(v)*(statistics.mean(v)-mu)**2
print("Z1402 fraction of win(p,C) variance (C≤20) explained by p mod 840: %.4f (p≡1 mod 4, 1e4≤p, %d primes)"%(between/tot_var, len(allp[:150000])))
# ---- Z1551: Artin-type densities: density of primes p (≡1 mod 24) with win(p,C), per C ≤ 12, and ratio to 1/C
dens={C: sum(1 for p in P24 if C in rows[p])/len(P24) for C in range(1,13)}
print("Z1551 density of win(p,C) over p≡1 mod 24 in [1e4,1e6]:", {C: round(d,4) for C,d in dens.items()})
print("Z1551 density*C:", {C: round(d*C,3) for C,d in dens.items()})
# ---- Z1468: I3-type census: p = t·u·v − u − v with t,u,v≥3 ⇔ (tu−1)(tv−1)=tp+1 ; compare t≡0 mod 4 with any t≥3
def reps(p, tset):
    out=[]
    for t in tset:
        N=t*p+1; m=t
        f=factorint(N); divs=[1]
        for q,k in f.items(): divs=[d*q**j for d in divs for j in range(k+1)]
        if any(a>=3*t-1 and a%m==m-1 and (N//a)%m==m-1 and a>1 and N//a>1 and ((a+1)//m)>=3 and ((N//a+1)//m)>=3 for a in divs): out.append(t)
    return out
exc=[409,577,5569,9601,23929,83449,102001,329617,712321]
for p in exc:
    anyT=reps(p,range(3,401)); four=[t for t in anyT if t%4==0]
    print("Z1468 p=%d: t≥3 reps (t≤400): %s ; of which 4|t: %s"%(p, anyT[:6], four[:6]))
cnt_any=0; cnt_four=0; cnt_nonfour_only=0
sample=[p for p in primerange(1000,6000) if p%24==1]
for p in sample:
    a=reps(p,range(3,101)); f4=[t for t in a if t%4==0]
    cnt_any+= bool(a); cnt_four+= bool(f4); cnt_nonfour_only += bool(a) and not f4
print("Z1468 primes ≡1 mod 24 in [1000,6000] (n=%d): with any t≤100 %d ; with 4|t %d ; only non-4|t %d"%(len(sample),cnt_any,cnt_four,cnt_nonfour_only))
