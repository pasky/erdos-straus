# "Periodic-atom" exponential window classes for n_s = 4^s + k, windows m_j = 4^j - k (j < s), K = 4^{j-1}(4^r+1), r = s-j.
# Atoms (all with residues mod m periodic in r): 2^i (|i| <= 2j-2), small primes l | 4^r+1 (exponent 1),
# G_e = 4^{r/e}+1 (odd e | r, e <= EMAXE), Aurifeuille halves of G_e (r/e odd).  d1 = 2^{i+}*U, d2 = 2^{i-}*V,
# U,V products of <= 2 atoms, gcd(U,V)=1, UV | 4^r+1, d1 = -d2 mod m.  Exact ES check of every hit.
import sys, math, itertools
from fractions import Fraction as F
from sympy import primerange
k=int(sys.argv[1]); S0=int(sys.argv[2]); S=int(sys.argv[3]); JMAX=int(sys.argv[4]); EMAXE=int(sys.argv[5]); LB=int(sys.argv[6])
SMALLP=list(primerange(3,LB))
def atoms(r):
    X=4**r+1; at=[]
    for l in SMALLP:
        if X%l==0: at.append(('l',l,l))
    for e in range(1,EMAXE+1,2):
        if r%e==0:
            g=r//e; G=4**g+1; at.append(('G',e,G))
            if g%2==1:
                h=2**((g+1)//2); at.append(('A-',e,2**g-h+1)); at.append(('A+',e,2**g+h+1))
    return X,at
def solve(s):
    n=4**s+k
    for j in range(1,min(JMAX,s-1)+1):
        m=4**j-k
        if m<=0: continue
        K=(n+m)//4
        if math.gcd(K,n)!=1: continue
        r=s-j; X,at=atoms(r)
        prods=[('1',1)]+[(a[0]+str(a[1]),a[2]) for a in at]
        prods+=[(a[0]+str(a[1])+'*'+b[0]+str(b[1]),a[2]*b[2]) for a,b in itertools.combinations(at,2) if math.gcd(a[2],b[2])==1]
        res={}
        for name,v in prods:
            if v>1 and X%v: continue
            res.setdefault(v%m,[]).append((name,v))
        T=2*j-2
        for i in range(-T,T+1):
            # want 2^i * U = - V  (mod m)
            for ru,Ul in res.items():
                rv=(-pow(2,i,m)*ru)%m
                if rv not in res: continue
                for (nu,U) in Ul:
                    for (nv,V) in res[rv]:
                        if math.gcd(U,V)!=1 or X%(U*V): continue
                        d1=U*2**max(i,0); d2=V*2**max(-i,0)
                        d=K*d1//d2; assert (K*d1)%d2==0 and (K+d)%m==0
                        A=(K+d)//m; z=F(n*K*A,d)
                        assert F(4,n)==F(1,K)+F(1,n*A)+1/z and z.denominator==1 and z>0
                        return (j,i,nu,nv)
    return None
un=[]; sig={}
for s in range(S0,S+1):
    h=solve(s)
    if h is None: un.append(s)
    else:
        key=(h[0],h[2].split('*')[0][0],h[3].split('*')[0][0]); sig[key]=sig.get(key,0)+1
print("k",k,"range",S0,S,"uncovered",len(un),un[:80])
print(sorted(sig.items(),key=lambda x:-x[1])[:25])
