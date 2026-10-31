"""Z2345: size of N_+(p), N_-(p), S(p) = N_+ - N_- at primes p ≡ 1 (4) (SIGN_IDENTITY word convention, t,u,v >= 1,
tuv - u - v = p, chi = (-(tu-1)/p)). An ADH-type closed formula (Hecke-character sum over ideals of norm A p + B in a fixed
quadratic field) is bounded by tau(Ap+B), whose mean over primes is ≍ log p; compare growth of mean |S(p)|."""
import sys, math, random
from sympy import primerange, jacobi_symbol, isprime
def counts(p):
    Np=Nm=0
    for u in range(1,p+3):
        t=1
        while (t-1)*u<=p+1:
            A=t*u-1
            if A>0 and (p+u)%A==0:
                j=jacobi_symbol((-A)%p,p)
                if j==1: Np+=1
                elif j==-1: Nm+=1
            t+=1
    return Np,Nm
random.seed(1)
for lo in [10**3,10**4,10**5]:
    ps=[p for p in primerange(lo,2*lo) if p%4==1]; ps=random.sample(ps,min(30,len(ps)))
    rows=[counts(p) for p in ps]
    mS=sum(abs(a-b) for a,b in rows)/len(rows); mN=sum(b for a,b in rows)/len(rows); mP=sum(a for a,b in rows)/len(rows)
    L=math.log(1.5*lo)
    print('p~[%d,%d): mean N+=%.1f N-=%.1f |S|=%.1f  |S|/log p=%.2f |S|/log^2 p=%.3f  max|S|=%d'%(lo,2*lo,mP,mN,mS,mS/L,mS/L**2,max(abs(a-b) for a,b in rows)))
