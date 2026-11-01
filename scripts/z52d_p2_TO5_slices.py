"""z52d_p2_TO5_slices.py — Z1819: C-slice success vs factorisation type of N=4Cp+1.
Slice C succeeds for prime p iff some divisor d of N=4Cp+1 has d ≡ -1 (mod 4C) (then d*e=N, e ≡ -1 too).
Primes p ≡ 1 (mod 4), p ≤ PMAX; C ≤ CMAX. Memory: spf sieve up to 4*CMAX*PMAX+1 (int32, ~80 MB at 2e7).
usage: python3 scripts/z52d_p2_TO5_slices.py PMAX CMAX"""
import sys, numpy as np, collections
PMAX=int(sys.argv[1]); CMAX=int(sys.argv[2])
NMAX=4*CMAX*PMAX+1
spf=np.zeros(NMAX+1,dtype=np.int32)
for i in range(2,int(NMAX**0.5)+1):
    if spf[i]==0:
        s=spf[i*i::i]; m=(s==0); s[m]=i; spf[i*i::i]=s
def factor(n):
    f=[]
    while n>1:
        p=int(spf[n]) if spf[n] else n
        e=0
        while n%p==0: n//=p; e+=1
        f.append((p,e))
    return f
def divisors(fs):
    ds=[1]
    for p,e in fs:
        ds=[d*p**k for d in ds for k in range(e+1)]
    return ds
isprime=np.ones(PMAX+1,bool); isprime[:2]=False
for i in range(2,int(PMAX**0.5)+1):
    if isprime[i]: isprime[i*i::i]=False
primes=[p for p in range(5,PMAX+1) if isprime[p] and p%4==1]
stats=collections.defaultdict(lambda:[0,0])   # key -> [count, successes]
primeN_success=0; primeN_total=0
for p in primes:
    for C in range(1,CMAX+1):
        N=4*C*p+1
        fs=factor(N)
        Om=sum(e for _,e in fs)
        # success test: divisor d (1<d<N) with d%(4C)==4C-1
        succ=any(d%(4*C)==4*C-1 for d in divisors(fs) if 1<d<N)
        stats[('Omega',Om)][0]+=1; stats[('Omega',Om)][1]+=succ
        if Om==1:
            primeN_total+=1; primeN_success+=succ
        sqfree=all(e==1 for _,e in fs)
        if Om==2 and sqfree:
            # distinct semiprime N=q*r: q≡-1 (4C) iff r≡-1 (4C); success iff q≡-1 mod 4C.
            phi=sum(1 for a in range(1,4*C) if a%2==1 and __import__('math').gcd(a,4*C)==1)
            stats[('semiprime_sqfree_phi4C_inv', phi)][0]+=1
            stats[('semiprime_sqfree_phi4C_inv', phi)][1]+=succ
print("primes p≡1(4) ≤",PMAX,": count",len(primes),"; C ≤",CMAX)
print("prime-N slices:",primeN_total,"successes:",primeN_success)
for k in sorted(stats, key=lambda x:str(x)):
    c,s=stats[k]
    extra=''
    if k[0]=='semiprime_sqfree_phi4C_inv': extra='  (1/phi(4C) = %.4f)'%(1.0/k[1])
    print(k, "slices",c, "success rate %.4f"%(s/c if c else 0)+extra)
