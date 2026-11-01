"""z52d_p2_TO5_semiprime_bias.py — Z1819/Z1827 follow-up: is the semiprime slice-success rate ~1/phi(4C)?
For N = 4C*m + 1 with m ranging over (a) primes p ≡ 1 (mod 4) [the (★) slices], (b) ALL odd m (not only primes),
restricted to squarefree semiprimes N=q*r; success iff q ≡ -1 (mod 4C).  Compare rates with 1/phi(4C).
usage: python3 scripts/z52d_p2_TO5_semiprime_bias.py MMAX CMAX"""
import sys, math, numpy as np
MMAX=int(sys.argv[1]); CMAX=int(sys.argv[2])
NMAX=4*CMAX*MMAX+1
spf=np.zeros(NMAX+1,dtype=np.int32)
for i in range(2,int(NMAX**0.5)+1):
    if spf[i]==0:
        s=spf[i*i::i]; m=(s==0); s[m]=i; spf[i*i::i]=s
isp=np.ones(MMAX+1,bool); isp[:2]=False
for i in range(2,int(MMAX**0.5)+1):
    if isp[i]: isp[i*i::i]=False
def sp(n):  # smallest prime factor
    return int(spf[n]) if spf[n] else n
res={}
for mode in ('primes_p','all_odd_m'):
    for C in range(1,CMAX+1):
        q4=4*C; phi=sum(1 for a in range(1,q4) if math.gcd(a,q4)==1)
        cnt=0; succ=0
        if mode=='primes_p':
            ms=[p for p in range(5,MMAX+1) if isp[p] and p%4==1]
        else:
            ms=range(3,MMAX+1,2)
        for m in ms:
            N=q4*m+1
            if N>NMAX: continue
            f=sp(N)
            if f==N: continue            # prime N: no divisor
            r=N//f
            if r==f or sp(r)!=r: continue   # need squarefree semiprime N=f*r, f,r prime, distinct
            cnt+=1
            if f%q4==q4-1 or r%q4==q4-1: succ+=1
        res.setdefault(phi,[]).append((C,mode,cnt,succ))
for phi in sorted(res):
    for (C,mode,cnt,succ) in res[phi]:
        if cnt: print("phi(4C)=%3d C=%3d %-10s semiprimes=%6d success=%.4f  1/phi=%.4f ratio=%.2f"%(phi,C,mode,cnt,succ/cnt,1/phi,(succ/cnt)*phi))
