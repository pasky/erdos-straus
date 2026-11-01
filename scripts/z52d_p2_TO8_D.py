# z52d P2 TO8 batch D: Z3067 (restricted counts with L-smooth divisors d=4uC-1), Z3134 (exception sets of a·t·u·v - b·u - c·v + d, t,u,v>=3),
# Z3076 (b=1 counts relative to log^2 p), Z3174 (non-square classes mod 840 by (★) zero counts)
import math, statistics as st, itertools
from math import gcd
from sympy import primerange, factorint
D = 'data/z52b/pass2/TO8/'
def smooth(n, L):
    for q in factorint(n):
        if q > L: return False
    return True
# ---- Z3067
ps=[p for p in primerange(1001, 20001) if p%4==1]
Ls=[10,50,200]
acc={L:[] for L in Ls}; allR=[]; zeroR={L:0 for L in Ls}
for p in ps:
    cnt={L:0 for L in Ls}; tot=0
    u=1
    while 4*u-1 <= p+u:
        C=1
        while 4*u*C-1 <= p+u:
            m=4*u*C-1
            if (p+u)%m==0:
                tot+=1
                fm=factorint(m)
                mx=max(fm) if fm else 1
                for L in Ls:
                    if mx<=L: cnt[L]+=1
            C+=1
        u+=1
    allR.append(tot)
    for L in Ls:
        acc[L].append(cnt[L])
        if cnt[L]==0: zeroR[L]+=1
print(f"Z3067: primes 1e3<p<=2e4 ({len(ps)}): mean R = {st.mean(allR):.2f}")
for L in Ls:
    fr=[a/b for a,b in zip(acc[L],allR) if b>0]
    print(f"  L={L}: mean R_L={st.mean(acc[L]):.3f} (fraction of R {st.mean(fr):.4f}); #primes with R_L=0: {zeroR[L]}")
# window dependence of mean R_L/ mean R
for lo,hi in [(1000,5000),(5000,10000),(10000,20000)]:
    idx=[i for i,p in enumerate(ps) if lo<p<=hi]
    print(f"  window ({lo},{hi}]: L=10 mean R_L/R = {st.mean(acc[10][i]/allR[i] for i in idx if allR[i]>0):.4f}; L=50: {st.mean(acc[50][i]/allR[i] for i in idx if allR[i]>0):.4f}")
# ---- Z3134: exceptions of f(t,u,v)=a t u v - b u - c v + d with t,u,v>=3 for n<=NN
NN=3000
def rep_set(a,b,c,d):
    S=set()
    for t in range(3, 2*NN):
        for u in range(3, 2*NN):
            if a*t*u - b*u - c*0 - 0 > NN + 10**9: break
            for v in range(3, 2*NN):
                val=a*t*u*v - b*u - c*v + d
                if val > NN:
                    if a*t*u*v - c*v > NN + b*u - d + 10**6: break
                    continue
                if val>=1: S.add(val)
            # break condition for v loop handled by value growth
    return S
res=[]
for a,b,c,d in [(1,1,1,0),(1,1,1,1),(1,2,1,0),(2,1,1,0),(1,1,2,0),(1,2,2,0),(1,1,1,-1)]:
    S=set()
    for t in range(3, 80):
        for u in range(3, 80):
            # solve for v: a t u v - c v = n + b u - d  -> v (a t u - c) = n + b u - d ; loop v directly bounded by NN
            base=a*t*u-c
            if base<=0: continue
            for n in range(1, NN+1):
                pass
            # direct: value(v) = (a t u - c) v - b u + d ; enumerate v
            v=3
            while True:
                val=(a*t*u-c)*v - b*u + d
                if val>NN: break
                if val>=1: S.add(val)
                v+=1
    exc=[n for n in range(1,NN+1) if n not in S]
    res.append(((a,b,c,d), len(exc), exc[-5:]))
for r in res: print("Z3134 (a,b,c,d)=",r[0],": exceptions n<=3000:", r[1], " largest:", r[2])
# ---- Z3076: b=1 count B1(p)/log^2 p minimum among primes 1e3..1e6 (from b1_1e6.txt) and windows
B={int(l.split()[0]):int(l.split()[1]) for l in open(D+'b1_1e6.txt')}
for lo,hi in [(1e3,1e4),(1e4,1e5),(1e5,1e6)]:
    xs=[B[p]/math.log(p)**2 for p in B if lo<p<=hi]
    print(f"Z3076 window ({lo:g},{hi:g}]: min B1/log²p = {min(xs):.4f}, 1st pct = {sorted(xs)[len(xs)//100]:.4f}, median = {st.median(xs):.4f}")
# ---- Z3174: non-square hard classes mod 840 and their (★)-zero counts (data R_all_1e6)
R={int(l.split()[0]):int(l.split()[1]) for l in open(D+'R_all_1e6.txt')}
for r in [241,337,409,457,577, 1,121,169,289,361,529]:
    ps2=[p for p in R if p%840==r]
    print(f"Z3174 class {r} mod 840: primes≤1e6 {len(ps2)}; min R = {min(R[p] for p in ps2)}; #R=0: {sum(1 for p in ps2 if R[p]==0)}; #R<=2: {sum(1 for p in ps2 if R[p]<=2)}")
