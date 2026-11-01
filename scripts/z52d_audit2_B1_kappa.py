# Z3090: correlate ES counts with arithmetic invariants kappa(p), primes p≡1 (4) <= 3e6.
# counts from words file (n ESC R Uv W I3), see scripts/z52d_audit2_B1_esc.py header.
import numpy as np, sys
from sympy import primerange
W=np.loadtxt(sys.argv[1],dtype=np.int64)
ps=np.array([p for p in primerange(5,3_000_001) if p%4==1],dtype=np.int64)
L=np.log(ps.astype(float)); L2=L*L
ESC=W[ps-1,1].astype(float); R=W[ps-1,2].astype(float)
qs=list(primerange(3,3000))
logL_p=np.zeros(len(ps)); logL_m4p=np.zeros(len(ps)); lqnr=np.zeros(len(ps))
chi2=np.where((ps%8==1)|(ps%8==7),1.0,-1.0)            # (2/p)
logL_p+= -np.log(1-chi2/2)
for q in qs:
    sq=np.zeros(q,bool); sq[(np.arange(1,q)**2)%q]=True
    leg=np.where(ps%q==0,0.0,np.where(sq[ps%q],1.0,-1.0))   # (p/q) = (q/p) for p≡1(4)
    logL_p+= -np.log(1-leg/q)
    m1=1.0 if q%4==1 else -1.0
    logL_m4p+= -np.log(1-m1*leg/q)
    lqnr=np.where((lqnr==0)&(leg==-1),q,lqnr)
lqnr=np.where(chi2==-1,2,lqnr)
h4p_rel=logL_m4p                                     # log h(-4p) = log(2 sqrt p/pi) + log L(1,chi_-4p)
p8=(ps%8==1).astype(float)                           # 4 | h(-4p)
r8=np.array([1.0 if p%8==1 and pow(p-4,(p-1)//8,p)==1 else 0.0 for p in ps.tolist()])   # 8 | h(-4p) (Barrucand-Cohn)
mod3=( (ps%3)==1).astype(float); 
feats={'logL(1,chi_p)':logL_p,'logL(1,chi_-4p)':logL_m4p,'log lqnr':np.log(lqnr),'p≡1(8) [4|h(-4p)]':p8,'8|h(-4p)':r8,'p≡1(3)':mod3}
for name,y in (('log ESC − 2loglog p',np.log(ESC)-2*np.log(L)),('log(1+R) − 2loglog p',np.log1p(R)-2*np.log(L))):
    y=y-np.polyval(np.polyfit(L,y,1),L)
    print('==',name,' var',round(y.var(),4))
    for k,v in feats.items():
        c=np.corrcoef(v,y)[0,1]; print(f'   corr with {k:22s} {c:+.3f}  R2 {c*c:.3f}')
    M=np.column_stack([np.ones(len(y))]+list(feats.values())); b=np.linalg.lstsq(M,y,rcond=None)[0]
    print('   joint R2', round(1-np.var(y-M@b)/np.var(y),3))
# floors by quintile of each invariant (ESC/log^2 p, p>1e5)
big=ps>1e5
for k,v in feats.items():
    if len(np.unique(v))<10:
        for val in np.unique(v):
            m=big&(v==val); print(f'{k}={val}: n={m.sum()} min ESC/L2={np.min(ESC[m]/L2[m]):.3f} mean={np.mean(ESC[m]/L2[m]):.3f} zeros(R)={(R[m]==0).sum()}')
    else:
        qq=np.quantile(v[big],[0,.2,.4,.6,.8,1])
        out=[]
        for i in range(5):
            m=big&(v>=qq[i])&(v<=qq[i+1]); out.append(f'Q{i+1}: min {np.min(ESC[m]/L2[m]):.3f} mean {np.mean(ESC[m]/L2[m]):.3f} R0 {(R[m]==0).sum()}')
        print(k,' | '.join(out))
# restricted to Mordell-hard primes (p mod 840 in the six square classes): every other class has an identity
print('== Mordell-hard primes only')
hard=np.isin(ps%840,[1,121,169,289,361,529])&big
y=np.log(ESC)-2*np.log(L); y=y-np.polyval(np.polyfit(L[hard],y[hard],1),L)
for k,v in feats.items():
    if len(np.unique(v[hard]))<3:
        continue
    c=np.corrcoef(v[hard],y[hard])[0,1]
    if len(np.unique(v))<10:
        print(f'{k}: corr {c:+.3f}', [ (val,int((hard&(v==val)).sum()), round(float(np.min(ESC[hard&(v==val)]/L2[hard&(v==val)])),3)) for val in np.unique(v[hard])]); continue
    qq=np.quantile(v[hard],[0,.2,.4,.6,.8,1]); out=[]
    for i in range(5):
        m=hard&(v>=qq[i])&(v<=qq[i+1]); out.append(f'Q{i+1}: min {np.min(ESC[m]/L2[m]):.3f} mean {np.mean(ESC[m]/L2[m]):.3f} R0 {(R[m]==0).sum()}')
    print(f'{k} (corr {c:+.3f}, n={hard.sum()}) '+' | '.join(out))
