"""Analyse bsB_caseB output: cylinders in v-space (u = 1 + T v, v a T-adic unit over F_3) covered by Case B
families on the slice x = 1 off T (SIGNLAYER_DEEP Lemma 1.1). Each solution (K, w) covers v = -w mod T^N0,
N0 = max(2, ceil(K/2)+1). Reports: is v = c (x*_c) covered; union measure of covered v (Haar on units);
coverage of random generic v.   usage: python bsB_caseB_cover.py FILE"""
import sys, random
cyl=set()
for line in open(sys.argv[1]):
    K,a,b,w=line.split(); K=int(K); N0=max(2,-(-K//2)+1)
    v=tuple((3-int(ch))%3 for ch in w[:N0]); cyl.add(v)
# minimal set: drop cylinders contained in shorter ones
cyl=sorted(cyl,key=len); mins=[]
for c in cyl:
    if not any(c[:len(m)]==m for m in mins): mins.append(c)
meas=sum(3.0**(-(len(c)-1))/2 for c in mins)
print("distinct minimal cylinders",len(mins),"union measure (fraction of units v)",round(meas,4))
for c in (1,2):
    hit=[m for m in mins if m[0]==c and all(x==0 for x in m[1:])]
    print(f"x*_{c} (v = {c}) covered:", bool(hit), hit[:3])
random.seed(7); L=max(len(m) for m in mins); cov=0; R=20000
for _ in range(R):
    v=tuple([random.choice((1,2))]+[random.randrange(3) for _ in range(L)])
    cov+=any(v[:len(m)]==m for m in mins)
print("random generic v covered fraction",cov/R)
from collections import Counter
print("cylinder lengths (N0):",sorted(Counter(len(m) for m in mins).items()))
# near misses for x*: longest prefix agreement of v=c with any cylinder relative to its length
for c in (1,2):
    best=max(mins,key=lambda m: next((i for i,x in enumerate(m) if x!=(c if i==0 else 0)),len(m))/len(m))
    print("closest cylinder to x*_%d:"%c,best)
