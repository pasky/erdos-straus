# O72: Z[1/2] Vieta descent (POINTWISE_TYPEI3 §5 scope) on near misses from typei3_nmdump 7 9 X > file. Usage: typei3_descent.py file
from fractions import Fraction as Fr
import sys
def v2(x):
    x=Fr(x); n,d=x.numerator,x.denominator; e=0
    if n==0: return 99
    while n%2==0: n//=2; e+=1
    while d%2==0: d//=2; e-=1
    return e
rows=[l.split() for l in open('sys.argv[1]')]
seen=0
for r in rows:
    c,k,al,ga,t,F,e,d=map(int,r)
    if F>=e or al+2*ga<=4: continue
    n=(4*c*k)>>t
    assert (e-F)%(16*n)==0
    delta=(e-F)//(16*n); lam=2**(t-4)
    ct=Fr(c,lam*lam); K=lam*k
    chain=[]; Fc=Fr(F); Kc=Fr(K)
    for step in range(60):
        if Fc==1: chain.append('END1'); break
        rho=Kc-delta*Fc
        if rho<=0: chain.append('rho<=0'); break
        Fp=Fc-4*ct*rho*delta
        chain.append((str(Fc) if Fc.denominator==1 else 'v2=%d'%v2(Fc)))
        Fc,Kc=Fp,rho
    seen+=1
    if seen<=25: print(c,k,al,ga,t,F,e,'delta',delta,'|',chain[:8], '...' if len(chain)>8 else '', chain[-1], len(chain))
