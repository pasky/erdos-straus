# z52d pass2 TO4: analysis of C-form (K=400, p<=1e7) and Type I c=1 (D=100, p<=1e6) sweeps
import sys, math, statistics
from collections import Counter, defaultdict
def load(fn):
    out={}
    for line in open(fn):
        t=list(map(int,line.split())); out[t[0]]=t[2:2+t[1]]
    return out
cf=load('/tmp/cf_1e7_K400.txt')
ti=load('/tmp/typeI_1e6_D100.txt')
print("C-form primes<=1e7 (K=400):",len(cf))
exc=[p for p,w in cf.items() if not w]
print("C-form zero-win (K=400) primes <=1e7:",exc)
print("C-form zero-win <=1e6:",[p for p in exc if p<=10**6])
ex_I=[p for p,w in ti.items() if not w]
print("TypeI c=1 (D=100) zero primes <=1e6:",ex_I)
print("intersection C-form(K400) zero & TypeI(D100) zero, <=1e6:",sorted(set(exc)&set(ex_I) & set(p for p in ti if p<=10**6)))
# mean wins and wins-per-prime distribution
ws=[len(w) for p,w in cf.items() if p>=10**4]
print("mean #wins C<=400, p in [1e4,1e7]:", round(statistics.mean(ws),2), "median", statistics.median(ws), "min",min(ws))
# residue-class effects (higher-residue substitute, item Z1009): P(win) by p mod 9 and p mod 16 (p≡1 mod 4)
def pw(mod):
    d=defaultdict(list)
    for p,w in cf.items():
        if p>=10**4: d[p%mod].append(len(w))
    return {r:round(statistics.mean(v),3) for r,v in sorted(d.items())}
print("mean wins by p mod 9:", pw(9))
print("mean wins by p mod 16:", pw(16))
# Legendre proxy: L(p)=#{q<=50 prime: (p/q)=+1} ; correlate with wins (p in [1e4,1e7])
from sympy import primerange, legendre_symbol
qs=list(primerange(3,51))
def proxy(p): return sum(1 for q in qs if legendre_symbol(p%q,q)==1)
xs=[];ys=[]
for p,w in cf.items():
    if p<10**4 or p%24!=1: continue
    if len(xs)>=20000: break
    xs.append(proxy(p)); ys.append(len(w))
import numpy as np
xs=np.array(xs,float); ys=np.array(ys,float)
print("n=",len(xs),"corr(proxy, #wins) =", round(np.corrcoef(xs,ys)[0,1],4))
for v in sorted(set(xs.astype(int))):
    m=ys[xs==v]; print(" proxy",v,"count",len(m),"mean wins",round(m.mean(),3))
