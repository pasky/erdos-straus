# Z1448: the one place Heath-Brown's real-character large sieve fits ES: T(p) = sum_{m<=p/4, 2|m} (-m/p) 2^w(m)/(4 phi(m))
# (bulk of the BM term, BM_CORRECTED_COUNT Prop 2.1(e)); modulus = p (averaged), argument = m, weights a_m independent of p
# once the cutoff m <= N is fixed. Compare the actual mean square over primes with the HB/Elliott shape (M+N) sum|a_m|^2 / M.
import numpy as np, sympy, sys
P0=int(sys.argv[1]); K=int(sys.argv[2])
N=P0//4
w=np.zeros(N+1,dtype=np.int64); phi=np.arange(N+1,dtype=np.float64)
for q in sympy.primerange(2,N+1):
    w[q::q]+=1; phi[q::q]*= (1-1/q)
a=np.zeros(N+1); m=np.arange(N+1)
ev=(m%2==0)&(m>0); a[ev]=2.0**w[ev]/(4*phi[ev])
sa2=(a**2).sum(); sa1=a.sum()
ps=[p for p in sympy.primerange(P0,P0*2) if p%4==1][:K]
Ts=[]; Tfull=[]
for p in ps:
    x=np.arange(p,dtype=np.int64); qr=np.full(p,-1,dtype=np.int64); qr[(x*x)%p]=1; qr[0]=0
    chi=qr[(-m[:N+1])%p]  # (-m/p)
    Ts.append((chi*a).sum())
Ts=np.array(Ts)
print(f"P0={P0} N=P0/4={N} primes={len(ps)} sum|a|^2={sa2:.4f} sum|a|={sa1:.3f} mean T={Ts.mean():.3f} mean T^2={np.mean(Ts**2):.3f} max|T|={abs(Ts).max():.3f}")
print(f"HB shape (M+N)/M*sum|a|^2 (M=#primes-range ~P0) = {(P0+N)/P0*sa2:.3f}  [times (MN)^eps]; Elliott (6) shape (M+N^2 log N)/M*sum|a|^2 = {(P0+N*N*np.log(N))/P0*sa2:.3e}")
