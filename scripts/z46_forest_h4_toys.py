#!/usr/bin/env python3
"""New H4-specific toys: CRT separation and exact finite endpoint laws.
The existing z43/z45 suites already test the underlying forest dictionary.
"""
import json
from math import gcd,lcm,log
from pathlib import Path
from sympy import isprime,nextprime,primerange
from sympy.ntheory.modular import crt
from z46_forest_h4_analyze import independent,amin
OUT=Path('data/z46_forest_h4')

def bounded(n,H):
    count=0
    for v in range(2,H+1):
        u=(-n)%v
        if not u or (n+v)%u:continue
        t=(n+u+v)//(u*v)
        count+=any(x%4==0 for x in (t,u,v,t*u-1,t*v-1))
    return count

def hj_length(p,a):
    k=0
    while a:
        p,a=a,(-p)%a;k+=1
        if k>3:return k
    return k

separation=[]
for H in (4,8,12,16,20,24):
    M=lcm(24,*range(1,H+1))
    q=next(q for q in primerange(H+1,10*H+100) if q%12==7)
    s=next(z for z in primerange(H+1,10*H+100) if z%12==11)
    a,mod=map(int,crt([M,q,s],[1,q-1,s-3]))
    p=a
    while p<=max(H,q,s) or not isprime(p):p+=mod
    assert bounded(p,H)==0 and amin(p)==3 and hj_length(p,q)==2
    h=independent(p,100000)
    assert h>H
    separation.append({'cutoff':H,'M':M,'q':q,'s':s,'p':p,'H4':h,'a_min':3,'lambda':2})

haar=[]
for H in (4,6,8,10,12,14,16):
    M=4*lcm(24,*range(1,H+1))
    units=miss=edges=0
    for a in range(1,M,24):
        if gcd(a,M)!=1:continue
        c=bounded(a+M,H)
        units+=1;miss+=c==0;edges+=c
    haar.append({'H':H,'modulus':M,'unit_classes':units,'avoiding_classes':miss,'density':miss/units,'mean_edges':edges/units})

# Classical least-NR lower bound vs colour-free parents at the saved record.
p=1002125860849
r=31;parent=(-p)%r
assert (p+r)%parent!=0
report={'separation':separation,'finite_prime_Haar':haar,'record_parent':{'p':p,'r':r,'parent':parent,'remainder':(p+r)%parent}}
(OUT/'toys.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
