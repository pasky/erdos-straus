# z57 BFII: dyadic profile of Type II solutions by witness modulus f (target-set form).
# For prime p and f = 3 (4), f <= FMAX: actual A_f = #{(a,c): ac | m_f, a c^{-1} == -p (mod f)};
# genus expectation G_f = (2^{omega(f)}/phi(f)) * #{(a,c): ac | m_f, -p*c*a^{-1} is a square unit mod f}
#   (square test: Legendre symbol +1 at every prime l | f; f odd so this is exact for prime powers too);
# naive expectation N_f = #{(a,c)}/phi(f).  Sums per dyadic block [2^k, 2^{k+1}).
import sys
from math import gcd
FMAX=int(sys.argv[1]); ps=[int(x) for x in sys.argv[2:]]
spf=list(range(FMAX+2))
for i in range(2,int((FMAX+1)**0.5)+1):
    if spf[i]==i:
        for j in range(i*i,FMAX+2,i):
            if spf[j]==j: spf[j]=i
def primes_of(n):
    s=[]
    while n>1:
        q=spf[n]; s.append(q)
        while n%q==0: n//=q
    return s
def phi(n):
    r=n
    for q in primes_of(n): r=r//q*(q-1)
    return r
def divisors(n):
    ds=[1]; m=n
    while m>1:
        q=spf[m]; e=0
        while m%q==0: m//=q; e+=1
        ds=[d*q**i for d in ds for i in range(e+1)]
    return ds
for p in ps:
    blocks={}
    for f in range(3,FMAX+1,4):
        m=(f+1)//4; P=primes_of(f); ph=phi(f)
        A=G=Nn=0
        r=(-p)%f
        for c in divisors(m):
            ci=pow(c,-1,f)
            for a in divisors(m//c):
                Nn+=1
                if (a*ci-r)%f==0: A+=1
                t=(-p*c*pow(a,-1,f))%f
                if all(pow(t%q,(q-1)//2,q)==1 for q in P): G+=1
        k=f.bit_length()-1
        b=blocks.setdefault(k,[0,0.0,0.0]); b[0]+=A; b[1]+=G*2**len(P)/ph; b[2]+=Nn/ph
    print("p=",p)
    tA=tG=tN=0
    for k in sorted(blocks):
        A,G,Nn=blocks[k]; tA+=A; tG+=G; tN+=Nn
        print(f"  f in [2^{k},2^{k+1}): actual {A:4d}  genus {G:8.2f}  naive {Nn:8.2f}   cum actual {tA:4d} genus {tG:8.2f}")
