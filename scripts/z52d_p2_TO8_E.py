# z52d P2 TO8 batch E: Z3117 (fixed points of u<->B swap on (★)-triples), Z3119 (Legendre-level Rédei proxies for failures),
# Z3185 (k=0 term of the root-of-unity expansion vs R), Z3149 (cofactor identity check)
import math, statistics as st
from math import gcd
from sympy import primerange, legendre_symbol
D='data/z52b/pass2/TO8/'
def star(p):
    out=[]; u=1
    while 4*u-1 <= p+u:
        C=1
        while 4*u*C-1 <= p+u:
            if (p+u)%(4*u*C-1)==0: out.append((u,(p+u)//(4*u*C-1),C))
            C+=1
        u+=1
    return out
# Z3117
fix=0; tot=0; swapok=0
for p in primerange(5,3000):
    if p%4!=1: continue
    S=star(p); Sset=set(S)
    for (u,B,C) in S:
        tot+=1
        if u==B: fix+=1
        if (B,u,C) in Sset: swapok+=1
print(f"Z3117: (★)-triples p<3000: {tot}; fixed points of u<->B: {fix}; swap maps triples to triples: {swapok}/{tot}")
# Z3149: cofactor identity: d=4uC-1, e=4BC-1, d*e=4Cp+1 ; c_d/d := (4Cp+1)/(4C p d) = e/(4Cp) = k/(4p) with k=e/C = 4B - 1/C
bad=0; n=0
for p in [409,1009,10009,100049]:
    for (u,B,C) in star(p):
        d=4*u*C-1; e=4*B*C-1; n+=1
        if d*e != 4*C*p+1: bad+=1
        if abs(e/(4*C*p) - (4*B-1/C)/(4*p))>1e-12: bad+=1
print(f"Z3149: cofactor identity d*e=4Cp+1 and k=e/C=4B-1/C checked on {n} certificates; failures {bad}")
# Z3185: root-of-unity expansion. R(p)=sum_{(u,C)} (1/m) sum_{k mod m} e(k(p+u)/m), m=4uC-1. k=0 term = sum 1/m = M0-type.
# compare E[R] and E[S0] where S0 = sum over pairs of 1/m (all pairs, not only hits)
import re
rows=[l.split() for l in open(D+'mbm_le1e5.txt')]
for lo,hi in [(1e3,1e4),(1e4,3e4),(3e4,1e5)]:
    sel=[(int(a),float(c),float(d),int(b)) for a,b,c,d in rows if lo<int(a)<=hi]
    print(f"Z3185 window ({lo:g},{hi:g}]: mean R = {st.mean(r for _,_,_,r in sel):.3f}; mean M_BM = {st.mean(m for _,m,_,_ in sel):.3f}; mean M0 (k=0 pair sum) = {st.mean(z for _,_,z,_ in sel):.3f}; mean R/M0 = {st.mean(r/z for _,_,z,r in sel):.3f}")
# Z3119: Legendre-level proxies: (a/p) for small a vs failure status, over p≡1 mod 4, 1e3<p<=1e6
R={int(l.split()[0]):int(l.split()[1]) for l in open(D+'R_all_1e6.txt')}
B1={int(l.split()[0]):int(l.split()[1]) for l in open(D+'b1_1e6.txt')}
fails=[p for p in R if R[p]==0]; b1f=[p for p in B1 if B1[p]==0]
base=[p for p in R if p>1000]
out=[]
for a in [2,3,5,7,11,13,17,-1]:
    def ch(p): return 1 if pow(a%p,(p-1)//2,p)==1 else -1
    fb=sum(1 for p in base if ch(p)==1)/len(base)
    ff=[ch(p) for p in fails if p>1000]
    out.append((a, round(fb,3), ff, [ch(p) for p in b1f if p>1000]))
for r in out: print(f"Z3119 a={r[0]}: base P((a/p)=+1)={r[1]}; (★)-fail symbols (p>1000) {r[2]}; b1-fail symbols {r[3]}")
