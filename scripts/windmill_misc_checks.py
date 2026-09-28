"""Miscellaneous parity checks for WINDMILL.md §2.4 and §3 (lambda weights,
crossing pairs, non-local counts, signed character sums, pairwise-AND GF(2)
features, generalised windmill identity).  Each block is a verbatim copy of the
ad-hoc check used; run from scripts/ with the /tmp/wm data files present.
Usage: uv run python windmill_misc_checks.py {lam,cross,nonlocal,signs,pairs,genzag}
"""
import sys, runpy, tempfile, os
BLOCKS = {}
BLOCKS['lam'] = r'''
import sys; sys.path.insert(0,'scripts')
from windmill_parity_features import load
from math import gcd, isqrt
from sympy import factorint
d=load('/tmp/wm/pos60k.txt')
def nlam(c):
    r=1
    for e in factorint(c).values(): r*=e//2+1
    return r
tot={'NII/2':0,'NI/2':0,'N/2':0}
for p,S in d.items():
    a=b=0
    for s in S:
        pd=[v%p==0 for v in s]
        if sum(pd)==2:
            x=[v for v in s if v%p][0]; Y,Z=[v//p for v in s if v%p==0]
            g=gcd(Y,Z); a0,b0=Z//g,Y//g; c0=x//(a0*b0); assert c0*a0*b0==x
            a+=nlam(c0)
        else:
            z0=[v for v in s if v%p==0][0]//p; X,Yy=[v for v in s if v%p]
            g=gcd(X,Yy); a0,b0=Yy//g,X//g; c0=z0//(a0*b0); assert c0*a0*b0==z0
            b+=nlam(c0)
    tot['NII/2']+=a%2; tot['NI/2']+=b%2; tot['N/2']+=(a+b)%2
print(len(d),tot)
'''
BLOCKS['cross'] = r'''
import sys
sys.path.insert(0,'scripts')
from windmill_signed_parity import load
from collections import Counter, defaultdict
d=load('/tmp/wm/signed30k.txt')
res=Counter()
names=['cross_pairs','sum_ab','cnt_aodd_bodd','buckets_mixed','posbuckets_with_nonpos','denoms_pos_only_odd']
tot=Counter()
for p,V in d.items():
    B=defaultdict(lambda:[0,0])
    pairs=set()
    byd=defaultdict(list)
    for i,v in enumerate(V):
        pos=v[0]>0
        for x in set(v):
            B[x][0 if pos else 1]+=1; byd[x].append(i)
    for x,L in byd.items():
        P=[i for i in L if V[i][0]>0]; N=[i for i in L if V[i][0]<0]
        for i in P:
            for j in N: pairs.add((i,j))
    vals=[len(pairs), sum(a*b for a,b in B.values()), sum(1 for a,b in B.values() if a%2 and b%2),
          sum(1 for a,b in B.values() if a and b), sum(1 for x,(a,b) in B.items() if a and b and x>0),
          sum(1 for a,b in B.values() if a%2 and not b)]
    for n,v in zip(names,vals): tot[n]+=v%2
print(len(d), dict(tot))
'''
BLOCKS['nonlocal'] = r'''
import sys; sys.path.insert(0,'scripts')
from windmill_parity_features import load
from collections import Counter
d=load('/tmp/wm/pos60k.txt')
tot=Counter(); n=0
for p,S in d.items():
    n+=1
    xs=set(s[0] for s in S); zs=set(s[2] for s in S); ys=set(s[1] for s in S)
    alld=set(v for s in S for v in s)
    pf=set(v for s in S for v in s if v%p)
    pdv=set(v for s in S for v in s if v%p==0)
    c=Counter(s[0] for s in S)
    vals={'distinct_x':len(xs),'distinct_y':len(ys),'distinct_z':len(zs),'distinct_all':len(alld),
          'distinct_pfree':len(pf),'distinct_pdiv':len(pdv),'x_with_odd_mult':sum(1 for v in c.values() if v%2),
          'max_mult_x':max(c.values()), 'min_x_mult':c[min(xs)], 'sum_sq_mult':sum(v*v for v in c.values())}
    # sols with x equal to global min x
    for k,v in vals.items(): tot[k]+=v%2
print(n, dict(tot))
'''
BLOCKS['signs'] = r'''
import sys; sys.path.insert(0,'scripts')
from windmill_parity_features import load, leg
from collections import Counter
d=load('/tmp/wm/pos60k.txt')
def jac(a,n):
    a%=n; r=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): r=-r
        a,n=n,a
        if a%4==3 and n%4==3: r=-r
        a%=n
    return r if n==1 else 0
sums={}
for p,S in sorted(d.items()):
    acc=Counter()
    for s in S:
        pd=[v%p==0 for v in s]
        if sum(pd)==2:
            x=[v for v in s if v%p][0]; Y,Z=sorted(v//p for v in s if v%p==0); q=4*x-p
            acc['II']+=1
            acc['II_legx']+=leg(x,p); acc['II_legq']+=leg(q,p)
            acc['II_jac_x_3']+=jac(x,3) ; acc['II_par_x']+=(-1)**x
            acc['II_legY-legZ']+= leg(Y,p) if Y<Z else -leg(Y,p)
            acc['II_legYZ+']+=leg(Y+Z,p)
        else:
            z0=[v for v in s if v%p==0][0]//p; X,Yy=sorted(v for v in s if v%p); m=(4*z0-1)//p
            acc['I']+=1
            acc['I_legm']+=leg(m,p); acc['I_legX']+=leg(X,p); acc['I_par_z0']+=(-1)**z0
            acc['I_legX+Y']+=leg(X+Yy,p)
    for k,v in acc.items(): sums.setdefault(k,[]).append(v)
for k,L in sums.items():
    c=Counter(L)
    print(k, 'min',min(L),'max',max(L),'mod4',sorted(Counter(v%4 for v in L).items()), 'zero frac', round(c[0]/len(L),3))
'''
BLOCKS['pairs'] = r'''
import sys; sys.path.insert(0,'scripts')
import numpy as np
from windmill_parity_features import load, features, gf2_solve
d=load('/tmp/wm/pos60k.txt'); primes=sorted(d)
names=None; per=[]
for p in primes:
    M=[]
    for s in d[p]:
        F=features(p,s); names=names or list(F); M.append([F[k] for k in names])
    per.append(np.array(M,dtype=np.uint8))
nb=len(names)
# pairwise AND features
cols=[]
for P in per:
    row=[]
    X=P.astype(np.int64)
    G=(X.T@X)%2   # counts of AND(i,j) mod 2
    iu=np.triu_indices(nb)
    row=G[iu]
    cols.append(row)
A=np.array(cols,dtype=np.uint8)
print(A.shape)
n=len(primes)
for split in (400,500,600):
    w=gf2_solve(A[:split],np.ones(split,dtype=np.uint8))
    if w is None: print(split,'no solution'); continue
    pred=(A[split:].astype(np.int64)@w.astype(np.int64))%2
    print(split,'validation odd fraction',pred.mean())
'''
BLOCKS['genzag'] = r'''
# test parity identity: #{x^2+m y^2=n, x,y>0}  vs  #{UV=n, 0<U<V, U=V mod m}  (x>0 variant)
from math import isqrt
def reps(n,m):
    c=0; y=1
    while m*y*y<n:
        r=n-m*y*y; x=isqrt(r)
        if x*x==r and x>0: c+=1
        y+=1
    return c
def facts(n,m):
    c=0; U=1
    while U*U<n:
        if n%U==0:
            V=n//U
            if (V-U)%m==0: c+=1
        U+=1
    return c
for m in range(1,13):
    agree=0; tot=0; agree_odd=0; tot_odd=0
    for n in range(2,4000):
        a=reps(n,m)%2; b=facts(n,m)%2
        tot+=1; agree+= a==b
        if n%2 and n%m: tot_odd+=1; agree_odd+= a==b
    print(m, round(agree/tot,3), round(agree_odd/max(tot_odd,1),3))
'''
if __name__ == "__main__":
    code = BLOCKS[sys.argv[1]]
    sys.argv = [sys.argv[0]]
    exec(compile(code, sys.argv[0], "exec"), {"__name__": "__main__"})
