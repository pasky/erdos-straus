"""Finite falsification panel for full-window genus union & secondary remainder.
PARI-based literal divisor test; use only distinct primes for kernel test.
"""
from cypari2 import Pari
from math import log,sqrt
from z80_gap_constants import chars,chi,RS
P=Pari(); P.allocatemem(64000000,silent=True);P.default('factor_proven',1);ws=[3,7,11,15,19,23,27,31,35,39,51,63,95,119,231];A={m:[0,0] for m in ws};J=[0,0];n=0
for p in P.primes([10**7,2*10**7]).python():
    if p%840 not in RS:continue
    fail=[];gen=[];n+=1
    for k in ws:
        x=(p+k)//4;s=p*x;ds=P.divisors(x).python();R={d%k for d in ds}|{p*d%k for d in ds};b=all((-r)%k not in R for r in R);fs=P.factor(x)[0].python();g=any(all(chi(f)[l%f]==1 for l in fs) for f in chars(k));assert g<=b,(p,k)
        A[k][0]+=g;A[k][1]+=b;fail.append(b);gen.append(g)
    J[0]+=all(gen[:2]);J[1]+=all(fail[:2]);
print('M primes in (1e7,2e7]',n,'cols k,genus,actual_fail,non_genus')
for k,(g,b) in [*A.items(),('3:7',J)]:print(k,g,b,b-g)
