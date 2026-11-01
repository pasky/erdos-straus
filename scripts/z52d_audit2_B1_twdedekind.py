# Z2534: do character-twisted Dedekind sums (Berndt type) s(a,c;chi) = sum_{n=1}^{ck} chi(n) B1(n/k) B1(a n/(c k))
# carry the symmetric HJ invariant r+r' (DEDEKIND_ES §6 C2: the part with "no reciprocity law"), or separate ES5
# certificates (HJ length r(p/A) = 3, (A/p) = -1) from non-certificates beyond the Jacobi symbol?
import sys, numpy as np
from fractions import Fraction
from sympy import jacobi_symbol, primerange
def B1(num,den):           # sawtooth ((num/den)) as Fraction
    r=num%den
    return Fraction(0) if r==0 else Fraction(r,den)-Fraction(1,2)
def hjlen(n,a):            # length of negative (HJ) continued fraction n/a = [[b1,...,br]]
    r=0
    while a>0:
        b=-(-n//a); n,a=a,b*a-n; r+=1
    return r
chis={'chi-4':(4,lambda n:[0,1,0,-1][n%4]),'chi8':(8,lambda n:[0,1,0,-1,0,-1,0,1][n%8]),'chi-8':(8,lambda n:[0,1,0,1,0,-1,0,-1][n%8]),'chi12':(12,lambda n:{1:1,5:-1,7:-1,11:1}.get(n%12,0))}
def saw(num,den):
    r=num%den; return np.where(r==0,0.0,r/den-0.5)
def s_tw(a,c,k,chi):
    n=np.arange(1,c*k+1); ch=np.array([chi(int(x)) for x in range(k)])[n%k]
    return float(np.sum(ch*saw(n,k)*saw(a*n,c*k)))
def saw2(num,den):   # periodic B2(x)=x^2-x+1/6
    x=(num%den)/den; return x*x-x+1/6
def s_tw2(a,c,k,chi):  # even in a; nonzero only for odd chi
    n=np.arange(1,c*k+1); ch=np.array([chi(int(x)) for x in range(k)])[n%k]
    return float(np.sum(ch*saw(n,k)*saw2(a*n,c*k)))
def s_plain(a,c):
    n=np.arange(1,c); return float(np.sum(saw(n,c)*saw(a*n,c)))
for p in [int(x) for x in sys.argv[1:]]:
    A=np.arange(1,p); r=np.array([hjlen(p,a) for a in A]); rp=np.array([hjlen(p,p-a) for a in A])
    J=np.array([jacobi_symbol(int(a),p) for a in A]); cert=(r<=3)&(J==-1)
    X={'s':np.array([s_plain(int(a),p) for a in A])}
    for nm,(k,chi) in chis.items(): X[nm]=np.array([s_tw(int(a),p,k,chi) for a in A])
    for nm in ('chi-4','chi-8'):
        k,chi=chis[nm]; X[nm+'/B2']=np.array([s_tw2(int(a),p,k,chi) for a in A])
    print('max|odd-chi B1B1 sums|:',max(abs(X['chi-4']).max(),abs(X['chi-8']).max()))
    y2=np.log(r+rp)
    y=r+rp
    def r2(cols):
        M=np.column_stack([np.ones(len(A))]+[X[c] for c in cols]); b=np.linalg.lstsq(M,y,rcond=None)[0]
        return 1-np.var(y-M@b)/np.var(y)
    def r2l(cols):
        M=np.column_stack([np.ones(len(A))]+[X[c] for c in cols]); b=np.linalg.lstsq(M,y2,rcond=None)[0]
        return 1-np.var(y2-M@b)/np.var(y2)
    print('R^2 of log(r+rp) on even-in-a sums:',{c:round(r2l([c]),3) for c in ('chi-4/B2','chi-8/B2')}, 'both:',round(r2l(['chi-4/B2','chi-8/B2']),3))
    print(f'p={p}: #cert={cert.sum()}  R^2(r+r\' ~ s)={r2(["s"]):.3f}  ~ s+all twisted={r2(list(X)):.3f}',
          ' | twisted alone:',{c:round(r2([c]),3) for c in chis})
    # separation: among QNR A, AUC of each feature for certificate vs not
    q=(J==-1)
    for c,v in X.items():
        a1=v[q&cert]; a0=v[q&~cert]
        auc=np.mean([ (x>a0).mean()+0.5*(x==a0).mean() for x in a1])
        print(f'   AUC({c}) cert vs non-cert among QNR: {auc:.3f}', end='')
    print()
