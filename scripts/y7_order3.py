# y7 (O215, goal d): double failure of the two "order-3-type" slices and cubic residue characters.
# M=4: p ≡ 1 (12), slices e=3: N_II=(p+3)/4, N_I=(3p+1)/4.  M=7: p ≡ 1 (21), slices e=6: N_II=(p+6)/7, N_I=(6p+1)/7.
# Slice e in {3,6} fires iff N (3-free, odd) has a prime factor ≡ 2 (mod 3).  "Double failure" = both N only have
# primes ≡ 1 (mod 3) (3-part ignored).  Correlate with cubic characters of 2, 3, M mod p.
import sys
X=int(sys.argv[1])
spf=list(range(X*7//1+8))
import math
N=len(spf)
for i in range(2,int(N**.5)+1):
    if spf[i]==i:
        for j in range(i*i,N,i):
            if spf[j]==j: spf[j]=i
def only1mod3(n):
    while n%3==0: n//=3
    while n>1:
        q=spf[n]
        if q%3==2: return False
        n//=q
    return True
def cube(a,p): return pow(a,(p-1)//3,p)==1
for M,e,mod in [(4,3,12),(7,6,21)]:
    tot=df=0; tab={}
    for p in range(5,X+1):
        if spf[p]!=p or p%mod!=1: continue
        tot+=1
        d=only1mod3((p+e)//M) and only1mod3((e*p+1)//M)
        df+=d
        key=(cube(2,p),cube(3,p),cube(M if M!=4 else 2,p))
        k2=(cube(2,p),cube(3,p),cube(7,p))
        s=tab.setdefault(k2,[0,0]); s[0]+=1; s[1]+=d
    print(f"M={M}: primes p≡1 ({mod}) <= {X}: {tot}, double failures {df} ({df/tot:.3%})")
    for k,(a,b) in sorted(tab.items()):
        print(f"   (2 cube, 3 cube, 7 cube)={k}: {a} primes, double-fail rate {b/a:.3%}")
