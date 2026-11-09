#!/usr/bin/env python3
"""z68 U7F §9.2: relation search. For the primes p = 1 (8) <= 1e6 failing all eight Lemma 2 families, list the
representations p+1 = u^2+v^2 (u>v>0), p+2 = a^2+2b^2 (a,b>0), p+4 = c^2+d^2, 4p+1 = e^2+g^2, and every U7 witness
(f, r, y, z). Test candidate rules: is some letter (r, y, z) or f or f+1 equal to |al*u + be*v| (|al|,|be| <= 3) for a
representation, or to a*b, u*v, (u+-v)/2, gcd-combinations etc.? Report, for each candidate formula, the number of
the primes at which it yields a witness letter. A rule is interesting only if it works at ALL primes."""
import sys
from math import isqrt, gcd
from collections import Counter
from sympy import isprime

def reps2(n, k):  # n = x^2 + k y^2, x,y>0
    out=[]
    y=1
    while k*y*y < n:
        x2=n-k*y*y; x=isqrt(x2)
        if x*x==x2 and x>0: out.append((x,y))
        y+=1
    return out

def witnesses(p):
    out=[]
    for f in range(7,2*p+2,8):
        r=(-p)%f
        if r and (f+1)%r==0: out.append((f,r,(f+1)//r,(p+r)//f))
    return out

allfail=[12721, 42169, 53089, 54121, 83449, 90841, 164089, 170641, 174241, 210961, 223129, 225289, 235369, 236329, 255049, 260761, 289249, 293329, 329401, 351289, 352489, 356449, 361321, 363841, 384001, 384049, 400849, 409081, 550489, 554569, 558721, 623401, 695689, 696361, 727729, 806521, 844201, 857929, 910849, 924361, 940921, 944329, 994249]
hits=Counter(); total=0
for p in allfail:
    W=witnesses(p); letters=set()
    for f,r,y,z in W: letters|={('f',f),('f+1',f+1),('r',r),('y',y),('z',z)}
    data={'A':reps2(p+1,1),'B':reps2(p+2,2),'C':reps2(p+4,1),'D':reps2(4*p+1,1),'E':reps2(2*p+1,2)}
    found=set()
    for tag,reps in data.items():
        for (u,v) in reps:
            cands={}
            for al in range(-3,4):
                for be in range(-3,4):
                    cands[f'{al}u{be:+d}v']=abs(al*u+be*v)
            cands.update({'uv':u*v,'2uv':2*u*v,'u+v/2':(u+v)//2,'u-v/2':abs(u-v)//2,'u2-v2':abs(u*u-v*v),'(u2-v2)/2':abs(u*u-v*v)//2})
            for name,val in cands.items():
                for kind in ('f','f+1','r','y','z'):
                    if (kind,val) in letters: found.add((tag,name,kind))
    for k in found: hits[k]+=1
    total+=1
print("primes:",total)
for k,c in hits.most_common(25): print(c,k)
