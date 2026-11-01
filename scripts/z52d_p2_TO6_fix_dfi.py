"""z52d pass2 TO6 fix: Z2396 (joint distribution of root nu/f of nu^2 ≡ -D mod f with f mod 4cd, D=4c^2 d),
Z2359 (Stern–Brocot / Calkin–Wilf depth of p/4 = sum of continued-fraction quotients), Z2125 (F_5[T] analogue:
4/P = 1/X+1/Y+1/Z with X,Y,Z nonzero polynomials of degree <= 2 over F_5)."""
import json, math, itertools
import numpy as np
from sympy import primerange, sqrt_mod
from fractions import Fraction
out={}
# ---- Z2396: c=1, d=3 => D = 4c^2 d = 12, 4cd = 12. Roots nu of nu^2 ≡ -12 (mod f) for primes f <= 3e5 with f ≡ -p (mod 12) style split:
D=12; m4cd=12
bins=np.zeros((10,m4cd)); cnt=np.zeros(m4cd)
for f in primerange(5,300000):
    if f in (2,3): continue
    r=sqrt_mod(-D % f, f)
    if r is None: continue
    cls=f%m4cd
    nu=min(int(r), f-int(r))            # root up to sign
    b=min(9,int(10*nu/f))
    bins[b,cls]+=1; cnt[cls]+=1
# chi-square of joint distribution (bins x classes), restricted to classes with cnt>0
tot=bins.sum(); rows=bins.sum(1,keepdims=True); cols=bins.sum(0,keepdims=True)
exp=rows@cols/tot
mask=exp>0
chi=float((((bins-exp)**2)[mask]/exp[mask]).sum())
dof=(bins.shape[0]-1)*(np.count_nonzero(cols)-1)
out['Z2396_DFI_joint']=dict(D=D,modulus=m4cd, primes_with_roots=int(tot), chi2=round(chi,2), dof=int(dof),
   class_counts={int(c):int(cnt[c]) for c in range(m4cd) if cnt[c]>0},
   bin_density_check=[round(float(x),3) for x in (bins.sum(1)/tot)])
# ---- Z2359: depth of p/4 in the Stern–Brocot tree = sum of regular continued-fraction quotients
def cf_sum(fr):
    n,d=fr.numerator, fr.denominator; s=0
    while d:
        q=n//d; s+=q; n,d=d,n-q*d
    return s
dep=[]
for p in primerange(5,100000):
    if p%4!=1: continue
    dep.append((p,cf_sum(Fraction(p,4))))
out['Z2359_SB_depth_p_over_4']=dict(primes=len(dep), median_depth=int(np.median([d for _,d in dep])),
    min_depth=min(d for _,d in dep), max_depth=max(d for _,d in dep), example=dep[:3],
    ratio_depth_over_p_median=round(float(np.median([d/p for p,d in dep])),4))
# ---- Z2125: F_5[T] analogue. polynomials as tuples of coefficients (low->high) mod 5
Q=5
def pmul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                r[i+j]=(r[i+j]+x*y)%Q
    return tuple(r)
def padd(a,b):
    n=max(len(a),len(b)); return tuple(((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%Q for i in range(n))
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return tuple(a)
def polys(deg):
    for c in itertools.product(range(Q),repeat=deg+1):
        if any(c): yield trim(c)
res={}
for P in [(2,1),(3,1),(1,1),(2,0,1),(3,0,1),(0,1,1),(4,1,1)]:   # monic P in F_5[T] (low->high) of degrees 1,2
    P=trim(P)
    if len(P)-1>2: continue
    sols=0; ex=None; degen=0
    Ps=[tuple(x) for x in [P]]
    cand=list(polys(2))
    for X in cand:
        for Y in cand:
            XY=pmul(X,Y)
            for Z in cand:
                lhs=pmul(pmul(X,Y),pmul(Z,(4,)))
                rhs=pmul(P,padd(padd(XY,pmul(Y,Z)),pmul(X,Z)))
                if trim(lhs)==trim(rhs):
                    # nondegenerate: no vanishing subsum of 1/X,1/Y,1/Z (pairwise X+Y, Y+Z, X+Z nonzero)
                    if trim(padd(X,Y))==(0,) or trim(padd(Y,Z))==(0,) or trim(padd(X,Z))==(0,): degen+=1; continue
                    sols+=1
                    if ex is None: ex=(X,Y,Z)
    res[str(P)]=dict(nondegenerate_ordered_deg_le2=sols, degenerate_cancelling=degen, example=ex)
out['Z2125_Fq_T_analogue_deg_le2']=res
json.dump(out, open('data/z52b/pass2/TO6/dfi_depth_fq_TO6.json','w'), indent=1, default=float)
print(json.dumps(out, default=float)[:3000])
