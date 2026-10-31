# z52b pass1 U09: three cheap checks.
#  (a) Z2910: primes p ≡ 1 mod 4, p <= N: does 4/p = 2^-k + 1/y + 1/z have a solution for some k <= KMAX?  (least k)
#      b = p*2^k, b^2 = p^2 4^k has divisors p^i 2^j only; need d1*d2=b^2, d1≡d2≡-b (mod a), a=4*2^k-p>0.
#  (b) Z2567: correlation of R(p)/log^2 p (data file) with the cubic character of 2 and of 4 (p ≡ 1 mod 3).
#  (c) Z1982: exceptions of n = xyz - x - y - z with x,y,z >= 2, n <= NZ (odd n only reported).
import sys, math, collections
import numpy as np
from scipy.stats import spearmanr
N=int(sys.argv[1]); NZ=int(sys.argv[2]); KMAX=40
def isprime_list(n):
    s=bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
PR=[p for p in isprime_list(N) if p%4==1 and p>=5]
def has_pow2_sol(p):
    for k in range(0,KMAX+1):
        a=4*(1<<k)-p
        if a<=0: continue
        b=p*(1<<k)
        # divisors of b^2 = p^2 * 4^k
        for i in range(3):
            for j in range(0,2*k+1):
                d1=(p**i)*(1<<j)
                if d1 % a == (-b) % a:
                    d2=(b*b)//d1
                    if d2 % a == (-b) % a:
                        y=(d1+b); z=(d2+b)
                        if y%a==0 and z%a==0:
                            y//=a; z//=a
                            if y>0 and z>0: return k
    return None
least=[]
for p in PR:
    least.append(has_pow2_sol(p))
ok=[k for k in least if k is not None]
print(f"(a) Z2910: primes ≡1 (4) <= {N}: {len(PR)}; with power-of-2 denominator (k<={KMAX}): {len(ok)} ({len(ok)/len(PR):.4f})")
print("    least-k distribution:", sorted(collections.Counter(ok).items())[:12])
print("    primes with none:", [p for p,k in zip(PR,least) if k is None][:20])
# (b) cubic characters
rows=[list(map(int,l.split())) for l in open('data/z52b/pass1/U09/R_primes1mod4_le2e5.txt')]
P=[r[0] for r in rows if r[0]%3==1]; R=[r[1] for r in rows if r[0]%3==1]
y=np.array(R,float)/np.log(np.array(P,float))**2
def cubic(a,p):  # 1 if a is a cube mod p (p ≡ 1 mod 3), -1 if not, 0 if a≡0
    t=pow(a%p,(p-1)//3,p)
    return 0 if a%p==0 else (1 if t==1 else -1)
c2=np.array([cubic(2,p) for p in P]); c4=np.array([cubic(4,p) for p in P])
print(f"(b) Z2567: p≡1 (3) primes <=2e5: {len(P)}; mean R/log^2 by cubic char of 2: +1 {y[c2==1].mean():.4f} (n={int((c2==1).sum())}), -1 {y[c2==-1].mean():.4f} (n={int((c2==-1).sum())})")
print(f"    by cubic char of 4: +1 {y[c4==1].mean():.4f}, -1 {y[c4==-1].mean():.4f};  Spearman(c2,y)={spearmanr(c2,y).correlation:.4f}  Spearman(c4,y)={spearmanr(c4,y).correlation:.4f}")
# (c) Z1982
NZ2=NZ
seen=bytearray(NZ2+1)
for x in range(2,NZ2+1):
    for y_ in range(x,NZ2+1):
        if x*y_-1 > NZ2 + 2*(x+y_) and False: pass
        # n = x*y*z - x - y - z, z>=y>=x>=2 ; for given x,y: n = z*(xy-1) - (x+y)  -> z = (n+x+y)/(xy-1)
        m=x*y_-1
        if m<=0: continue
        # smallest n for z=y: n = y*m-(x+y)
        zmin=y_
        n0=zmin*m-(x+y_)
        if n0>NZ2: break
        z=zmin
        while True:
            n=z*m-(x+y_)
            if n>NZ2: break
            if n>=1: seen[n]=1
            z+=1
exc=[n for n in range(1,NZ2+1) if not seen[n]]
print(f"(c) Z1982: n = xyz-x-y-z, x,y,z>=2 (ordered x<=y<=z), n<= {NZ2}: exceptions count {len(exc)}; first 40: {exc[:40]}")
print("    exceptions by parity:", "odd", sum(1 for n in exc if n%2), "even", sum(1 for n in exc if n%2==0))
print("    largest exceptions:", exc[-15:])
# (c') growth of the exception count and square enrichment
cum=[0]*(NZ2+1)
for n in range(1,NZ2+1): cum[n]=cum[n-1]+(0 if seen[n] else 1)
for T in [100,1000,10000,NZ2]:
    print(f"(c') exceptions <= {T}: {cum[T]}")
import math as _m
sq=[n for n in exc if _m.isqrt(n)**2==n]
print("    exceptions that are squares:", len(sq), sq[:12])
print("    exceptions ≡ 1 mod 4 vs 3 mod 4 (odd):", sum(1 for n in exc if n%4==1), sum(1 for n in exc if n%4==3))
