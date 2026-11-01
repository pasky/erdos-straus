"""z52d avenue Q05 Z1999: R(p)/L^2 at Euler primes p = n^2+n+41 (p = 1 mod 4, p <= 5e7) vs all primes p = 1 (4)
in the same range, both overall and within the Mordell (square mod 840) classes. R from scripts/z52b_p1_H04_rstar.c. EVIDENCE."""
import numpy as np, sys, math
R=np.fromfile(sys.argv[1],dtype=np.uint16); N=len(R)-1
s=np.ones(N+1,bool); s[:2]=False
for i in range(2,int(N**0.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]; P=P[(P%4==1)&(P>1000)]
n=np.arange(0,8000); E=n*n+n+41; E=E[(E<=N)]; E=E[s[E]&(E%4==1)&(E>1000)]
sqc=np.array(sorted({(x*x)%840 for x in range(840) if math.gcd(x,840)==1}))
def ratio(ps):
    L2=np.log(ps.astype(float))**2; return R[ps]/L2
# compare in matched log-bins
bins=np.logspace(3,math.log10(N),8)
print('bin  n_euler  euler R/L2  all R/L2  | mordell-class: n_euler euler all')
for a,b in zip(bins[:-1],bins[1:]):
    e=E[(E>=a)&(E<b)]; p=P[(P>=a)&(P<b)]
    em=e[np.isin(e%840,sqc)]; pm=p[np.isin(p%840,sqc)]
    print('%9.0f %5d  %.3f  %.3f | %4d %s %.3f'%(a,len(e),ratio(e).mean() if len(e) else np.nan,ratio(p).mean(),len(em),('%.3f'%ratio(em).mean()) if len(em) else ' nan ',ratio(pm).mean()))
print('zeros among Euler primes:', [int(x) for x in E if R[x]==0])
print('fraction of Euler primes in Mordell classes: %.3f vs all %.3f'%(np.isin(E%840,sqc).mean(),np.isin(P%840,sqc).mean()))
