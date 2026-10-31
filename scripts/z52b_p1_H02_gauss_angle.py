"""Z0799: does ES-hardness correlate with the Gaussian angle θ_p (p = a²+b²) beyond congruences?
R(n) = #{(u,B,C): 4uBC-u-B = n} for n <= X via sum over (u,C) of 1[(4uC-1) | n+u]; residual of log R(p) after
regressing on log p and indicators of p mod 48 (absorbs the a,b mod-small-power information); Spearman/Pearson with
cos(4kθ), k=1..3 (Hecke Grössencharacters of Q(i), well defined), and θ-bins."""
import numpy as np, sys, math
X=int(sys.argv[1]); LO=int(sys.argv[2])
R=np.zeros(X+1,np.int32)
u=1
while 4*u-1<=X+u:
    C=1
    while True:
        m=4*u*C-1
        if m>X+u: break
        # n ≡ -u mod m, n>=1 ; also need B>=1: n = B*m - u >= m-u
        start=m-u
        R[start::m]+=1
        C+=1
    u+=1
isp=np.ones(X+1,bool); isp[:2]=False
for i in range(2,int(X**.5)+1):
    if isp[i]: isp[i*i::i]=False
ps=[p for p in range(LO,X+1) if isp[p] and p%4==1]
def two_sq(p):
    # sqrt(-1) mod p via quadratic non-residue
    for c in range(2,p):
        if pow(c,(p-1)//2,p)==p-1: break
    r=pow(c,(p-1)//4,p); a,b=p,r
    while b*b>p: a,b=b,a%b
    x=b; y=int(math.isqrt(p-x*x))
    assert x*x+y*y==p
    if x%2==0: x,y=y,x
    return x,y  # x odd, y even
th=[]; lr=[]; feats=[]
for p in ps:
    a,b=two_sq(p); th.append(math.atan2(b,a)); lr.append(math.log(R[p]+1))
th=np.array(th); lr=np.array(lr); P=np.array(ps,float)
cls=np.array([p%48 for p in ps]); ucl=sorted(set(cls))
A=np.column_stack([np.ones(len(ps)),np.log(P)]+[(cls==c).astype(float) for c in ucl[1:]])
coef,*_=np.linalg.lstsq(A,lr,rcond=None); res=lr-A@coef
print("X=%d primes p≡1(4) in [%d,%d]: %d; R(p)=0 count %d; residual sd %.3f"%(X,LO,X,len(ps),int((R[np.array(ps)]==0).sum()),res.std()))
from scipy.stats import spearmanr, pearsonr
for k in (1,2,3):
    c=np.cos(4*k*th)
    # also residualize the feature on the same congruence design (θ correlates with p mod 16 via a,b mod 4/8)
    cc,*_=np.linalg.lstsq(A,c,rcond=None); cr=c-A@cc
    s=spearmanr(res,cr); q=pearsonr(res,cr)
    print("cos(4·%dθ): Spearman %.4f (p=%.2g)  Pearson %.4f (p=%.2g)  [raw feature sd %.3f, after congruence-residualisation sd %.3f]"%(k,s[0],s[1],q[0],q[1],c.std(),cr.std()))
# θ bins
bins=np.linspace(0,math.pi/2,9); idx=np.digitize(th,bins)-1
print("mean residual by θ octile:", " ".join("%.3f"%res[idx==i].mean() for i in range(8)))
print("count by θ octile:", " ".join(str(int((idx==i).sum())) for i in range(8)))
