"""Replay final all-s covers using the earlier standalone verifier; sanity-check the norm identity."""
from pathlib import Path
from math import lcm
from z78_proth_check import check, small
import json

root = Path('data/z79/proth')
for m,period in [(11,3825360),(12,55440)]:
    row=json.loads((root/f'period-{m}-{period}.json').read_text())
    assert (row['m'], row['period'], row['left']) == (m,period,[])
    check(row)
    if m==11:
        for P,j,T,*args in row['rows']:
            if T=='X':
                assert P==41580 and j==0
                continue
            if T=='M': M=840
            elif T in ('II','D'): M=args[0]
            elif T=='W': M=8*args[0]
            elif T=='K':
                f,K,D,E=args
                M=4*f*K if D[2] or E[2] else 4*lcm(f,K)
            else: raise ValueError(T)
            assert M&-M<=2**64
small()

def ratio(x,w,q,Q):
    z=1
    for t in range(1,q,3):
        z=z*(1+x*pow(w,t,Q))*pow(1+x*pow(w,-t,Q),-1,Q)%Q
    return z

for h in range(3,1000,6):
    d=h
    while d%3==0: d//=3
    q=h//d; H=(1<<h)-1; w=1<<d
    value=ratio(2,w,q,H)*pow(ratio(8,pow(w,3,H),q//3,H),-1,H)%H
    n=w*w+w+1
    assert value%n==n-1 and value%(H//n)==1%(H//n)
print('cubic sign sanity: every odd multiple of 3 below 1000')
