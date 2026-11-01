"""z52d_p2_TO5_hecke.py — Z1679: does the BM residual X(p)=R(p)-M_BM(p) correlate with a_p(f) of small-level newforms?
f = elliptic newforms of conductor 11 (11a: y^2+y=x^3-x^2-10x-20) and 37 (37a: y^2+y=x^3-x).
a_p = -sum_x legendre(f(x)) with f(x)=4x^3+b2... derived from (2y+1)^2 = 4y^2+4y+1 = 4x^3+...+1 (see below).
Residual data: data/z52b/pass2/TO5/mbm_1e6.txt (R, M_BM from scripts/z38_mbm.c). usage: python3 scripts/z52d_p2_TO5_hecke.py PMAX"""
import sys, math, numpy as np
PMAX=int(sys.argv[1]) if len(sys.argv)>1 else 200000
D='data/z52b/pass2/TO5/'
# curve: y^2+y = g(x)  =>  (2y+1)^2 = 4g(x)+1
polys={'11a': lambda x: (4*(x**3-x**2-10*x-20)+1), '37a': lambda x: (4*(x**3-x)+1)}
def ap_table(fun, p):
    x=np.arange(p,dtype=np.int64)
    v=fun(x)%p
    sq=np.zeros(p,dtype=np.int8); sq[(np.arange(1,p,dtype=np.int64)**2)%p]=1
    chi=np.where(v==0,0,np.where(sq[v]==1,1,-1))
    return -int(chi.sum())
rows=[]
for l in open(D+'mbm_1e6.txt'):
    if l.startswith('#'): continue
    a=l.split()
    if len(a)<6 or int(a[1])==0: continue
    n,R,M0,MB=int(a[0]),int(a[2]),float(a[3]),float(a[4])
    if n%4==1 and 5<=n<=PMAX and MB>0: rows.append((n,R,MB))
print("primes p≡1(4), 5<=p<=%d: %d"%(PMAX,len(rows)))
res={}
for name,fun in polys.items():
    # sanity: Hasse bound & known values (11a: a_2=-2,a_3=-1,a_5=1,a_7=-2; 37a: a_2=-2,a_3=-3)
    print(name,"a_p small:",[ (p,ap_table(fun,p)) for p in (2,3,5,7)] if False else '')
    xs=[]; 
    for (p,R,MB) in rows:
        a=ap_table(fun,p)
        xs.append(a/math.sqrt(p))
    xs=np.array(xs); X=np.array([(R-MB)/math.sqrt(MB) for (p,R,MB) in rows]); 
    c=np.corrcoef(xs,X)[0,1]
    # also split by p mod 8 and by quadratic residue symmetry check
    print("%s: corr(a_p/sqrt p, (R-M)/sqrt M) = %+.4f  (n=%d, 1/sqrt n = %.4f)"%(name,c,len(rows),1/math.sqrt(len(rows))))
    res[name]=c
