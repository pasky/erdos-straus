from math import gcd, log
from sympy import divisors, isprime, factorint
from fractions import Fraction
# Lemma H brute force
bad=0;cnt=0
for s in [3,5,7,11]:
  for h in range(1,9):
    for m in divisors(s**h+1):
      for p in range(1,200000):
        if (p+m)%4 or gcd(p,m)!=1: continue
        K=(p+m)//4
        if K%s: continue
        c=0;k=K
        while k%s==0: k//=s;c+=1
        E=max(0,(h-c+1)//2)
        cnt+=1
        if h>4*E+log(p+1)/log(s)+1e-9: bad+=1;print('H fail',s,h,m,p)
print('H checked',cnt,'bad',bad)
# Lemma I independent: random-ish construction, full capped-relaxation check
import itertools
ok=0
for s in [13,17,29,37,41,53]:
  F=s*s-s+1
  for h in [3,9,15,21,27,33,45]:
    N=s**h+1
    ts=[t for t in factorint(N) if t%4==3 and F%t and t<10**7]
    for p in range(17,3000,8):
      if not isprime(p) or pow(p,(s-1)//2,s)!=s-1: continue
      hit=None
      for r in range(1,len(ts)+1,2):
        hit=None
        for S in itertools.combinations(ts,r):
          m0=1
          for t in S: m0*=t
          if (m0+p)%s==0: hit=m0;break
        if hit: break
      if not hit: continue
      m=hit if (p+hit)%(s*s) else hit*F
      K=(p+m)//4; assert 4*K==p+m
      d=K*s**h; A=(K+d)//m
      if (K+d)%m: print("DBG",s,h,p,hit,m,N%m,F,N%F); break
      x,y,z=K,p*A,Fraction(p*K*A,d)
      assert Fraction(1,x)+Fraction(1,y)+1/z==Fraction(4,p)
      den=z.denominator; r=s**((h-1)//2)
      assert den==r*r and y%s==0 and p%s
      ok+=1
print('Lemma I packets ok',ok)
