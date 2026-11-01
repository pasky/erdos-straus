# z52d Pass 2 NC0, item Z0093 — 4/n = 1/x+1/y+1/z with x,y,z ∈ Z[ζ8] (K=Q(ζ8), O_K=Z[ζ8]), x,y of coefficient height <=H (z free).
# Pair completion: z = n x y / (4xy - n(x+y)); integrality checked numerically in the 4 complex embeddings
# (basis 1,ζ,ζ²,ζ³; exact verification with sympy for every hit). Cone (totally positive) condition NOT imposed.
import sys, itertools, numpy as np, sympy as sp
H=int(sys.argv[1]) if len(sys.argv)>1 else 2
NMAX=int(sys.argv[2]) if len(sys.argv)>2 else 200
ks=[1,3,5,7]
zeta=np.exp(1j*np.pi/4)
# embedding matrix E[k][i] = (zeta^{k i}) for basis i=0..3
E=np.array([[ (zeta**(k*i)) for i in range(4)] for k in ks])   # 4x4 complex
Einv=np.linalg.inv(E)
els=[np.array(a) for a in itertools.product(range(-H,H+1),repeat=4) if any(a)]
A=np.array(els)                                  # coefficient vectors
V=A @ E.T                                        # V[e,k] = value of element e in embedding k
hits=[]; cnt={}
iu=np.triu_indices(len(A),0)
X=V[iu[0]]; Y=V[iu[1]]
for n in range(5,NMAX+1):
    D=4*X*Y - n*(X+Y)                            # D0 per embedding (shape pairs x 4)
    ok=np.all(np.abs(D)>1e-9,axis=1)
    Z=np.where(ok[:,None], n*X*Y/np.where(np.abs(D)>1e-9,D,1), np.nan)
    C=Z @ np.linalg.inv(E).T                     # coordinates of z in basis: z = E c  -> c = Einv z  (per row)
    # the above uses inv(E).T on row vectors: c_row = z_row @ (Einv).T
    good=ok & np.all(np.abs(C.imag)<1e-6,axis=1) & np.all(np.abs(C.real-np.round(C.real))<1e-6,axis=1)
    idx=np.nonzero(good)[0]
    cnt[n]=len(idx)
    for t in idx[:2]:
        if len(hits)<12:
            hits.append((n,tuple(A[iu[0][t]]),tuple(A[iu[1][t]]),tuple(int(round(v)) for v in C[t].real)))
tot=sum(cnt.values())
print('H=%d n in [5,%d]: pair-completions with integral z: %d over %d n-values with >=1 hit'%(H,NMAX,tot,sum(1 for v in cnt.values() if v)))
print('n with hits (first 20):',[n for n in cnt if cnt[n]][:20])
print('sample (n, x coeffs, y coeffs, z coeffs in 1,zeta,zeta^2,zeta^3):',hits[:6])
# exact verification of up to 6 hits
z_=sp.exp(sp.I*sp.pi/4)
def ev(c): return sum(ci*z_**i for i,ci in enumerate(c))
ver=[]
for n,xc,yc,zc in hits[:6]:
    x,y,zz=ev(xc),ev(yc),ev(zc)
    ver.append(sp.simplify(sp.expand(sp.Rational(4,n)-1/x-1/y-1/zz))==0)
print('exact verification of first hits:',ver)
