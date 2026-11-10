# z69 TWIST round 2, I12 (reviewer's target-only cofactor experiment).
# For a prime p and Q_r = product of the r least primes q with (p/q) = -1: forced shifts u == -p (mod Q_r), u = u0 + Q_r j,
# 0 <= j < J.  N = p + u = D*m, D = Q_r-smooth part.  hits(b) = #{f | N : f == -1 (mod 4u)};  hits(a) = those with f | D.
# lambda(u) = #{f | N : f >= 4u-1, gcd(f,4u)=1}/phi(4u);  kappa(u) = #{distinct residues mod 4u of divisors coprime to 4u}/phi(4u).
# Control arm: u+1 for each forced u.
import sys, math
from sympy import factorint, nextprime, jacobi_symbol, totient, primerange, isprime
def divs(fac):
    D=[1]
    for q,e in fac.items(): D=[x*q**i for x in D for i in range(e+1)]
    return D
def arm(p,u,Q):
    N=p+u; fac=factorint(N); m4=4*u; ph=int(totient(m4)); ds=divs(fac)
    hits=[f for f in ds if (f+1)%m4==0]
    Dpart=1
    for q in fac:
        if Q%q==0: Dpart*=q**fac[q]
    ha=sum(1 for f in hits if Dpart%f==0)
    cop=[f for f in ds if math.gcd(f,m4)==1]
    lam=sum(1 for f in cop if f>=m4-1)/ph
    kap=len(set(f%m4 for f in cop))/ph
    return len(hits),ha,lam,kap,len(ds)
def load(fn):
    out=[]
    for line in open(fn):
        t=line.split('#')[0].split()
        if t: out.append(int(t[0]))
    return out
J=int(sys.argv[1]); rs=[int(x) for x in sys.argv[2].split(',')]
P=load('data/z58/screens/r8_zeros_1e10.txt'); q=10**10
while len(P)<40:
    q=nextprime(q)
    if q%840==1: P.append(q)
for r in rs:
    T={a:dict(h=0,ha=0,lam=0.0,kap=0.0,tau=0,n=0) for a in ('forced','control')}
    for p in P:
        nr=[]; l=3
        while len(nr)<r:
            if isprime(l) and jacobi_symbol(p%l,l)==-1: nr.append(l)
            l+=2
        Q=math.prod(nr); u0=(-p)%Q
        if u0==0: u0=Q
        for j in range(J):
            u=u0+Q*j
            for a,uu in (('forced',u),('control',u+1)):
                h,ha,lam,kap,tau=arm(p,uu,Q)
                t=T[a]; t['h']+=h; t['ha']+=ha; t['lam']+=lam; t['kap']+=kap; t['tau']+=tau; t['n']+=1
    out=f"r={r} ({len(P)} primes, J={J}):"
    for a in ('forced','control'):
        t=T[a]; z=(t['h']-t['lam'])/math.sqrt(t['lam']) if t['lam']>0 else float('nan')
        out+=f" {a}: shifts {t['n']}, mean tau {t['tau']/t['n']:.1f}, hits {t['h']} (from D alone {t['ha']}), sum lambda {t['lam']:.3f}, z {z:+.2f}, mean kappa {t['kap']/t['n']:.2e};"
    f_,c_=T['forced'],T['control']
    if f_['h'] and c_['h']:
        rf=f_['h']/f_['lam']; rc=c_['h']/c_['lam']; se=(rf/rc)*math.sqrt(1/f_['h']+1/c_['h'])
        out+=f" ratio (hits/lambda) forced/control = {rf/rc:.3f} +- {se:.3f}"
    print(out,flush=True)
