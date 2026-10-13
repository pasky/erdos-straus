"""R202: tally CF hits of depth k <= 5 (odd n < 300, sqrt(4n/3) < mu <= 4n) by region and B-class."""
import sys
sys.path.insert(0, "scripts")  # run from repo root
from review_mk_cf import cf_hits
from math import isqrt
tally={}
for n in range(3,300,2):
    for mu in range(isqrt(n)+1, 4*n+1):
        if 3*mu*mu<=4*n: continue
        h=cf_hits(n,mu,10**6)
        if not h: continue
        for (A,B,D),k in h.items():
            reg='mu>2n' if mu>2*n else 'mu<=2n'
            cls='B=1' if B==1 else ('partner' if B==2*mu*A-1 else 'B>1 other')
            if k<=5: tally[(reg,k,cls)]=tally.get((reg,k,cls),0)+1
for key in sorted(tally): print(key,tally[key])
