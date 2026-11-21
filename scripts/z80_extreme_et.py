"""Sorted primitive ES counts, p prime (or strict ET counts at odd-square controls).
No conjectural pruning. PARI divisors in proof mode via explicit factor proof on
large cofactors; <= 2^64 PARI's isprime is deterministic. Run serially.
"""
from math import gcd, isqrt
import sys
from cypari2 import Pari
P = Pari(); P.default('factor_proven', 1)

def ds(x):
    return P.divisors(x).python()

def count(p):
    small = [set(), set()]
    def put(i,a,b,c,d):
        if a>b or min(a,b,c,d)<1 or gcd(a,b)!=1 or gcd(a*b*c*d,p)!=1:return
        assert (a+b)%c==0
        e=(a+b)//c
        assert (4*a*b*d == (p*e+1 if not i else p+e))
        small[i].add((a,b,c,d))
    # For each I, acd<=3p/4 and ef=4a^2d+1, giving ef*c^2*d <=3p^2
    # (c^2*d <= (acd)^2). If f and e both large, only small c^2*d remain.
    # Choose ET's product e*f*(cd)^2*(ac) <= (5/3)*2*(3p/4)^2*p < 2p^3.
    # Integer coverage check; rectangular, optimizing relative costs heuristically.
    A=max(2,int(p**.5/2)+1); C=max(2,int(p**.48/2)+1)
    F=max(3,int(4*p**.72)+1); E=(2*p**3)//(A*C*C*F)+1
    # E may be costly; trade CD and AC vs single-coordinate loops.
    if p<10**7 or E>4*F:
        A=C=max(2,int(p**.55*1.5)+1);F=max(3,int(p**.68*2)+1)
        E=(2*p**3)//(A*C*C*F)+1
    assert A*C*C*F*E>=2*p**3
    def triples(v):
        for a in ds(v):
            if a*a>v:break
            for b in ds(v//a):
                if b>=a:yield a,b,v//a//b
    # Both looped singles exploit their fixed class mod 4; parity screen exact.
    for e in range((-p)%4,E+1,4):
        for a,b,d in triples((p*e+1)//4):
            if (a+b)%e==0:put(0,a,b,(a+b)//e,d)
    for f in range((-p)%4,F+1,4):
        x=(p+f)//4
        for a in ds(x):
            for d in ds(x//a):
                e,r=divmod(4*a*a*d+1,f)
                if r==0 and e>E:
                    c=x//a//d; put(0,a,c*e-a,c,d)
    for c in range(1,C+1):
        for d in range(1,C//c+1):
            m=4*c*d
            for f in ds(p*p+4*c*c*d):
                if f<=F or (p+f)%m:continue
                a=(p+f)//m; e,r=divmod(4*a*a*d+1,f)
                if not r and e>E:put(0,a,c*e-a,c,d)
    for a in range(1,A+1):
        for c in range(1,A//a+1):
            if gcd(a,c)!=1:continue
            for f in ds(p*a+c):
                if f<=F or (p+f)%(4*a*c):continue
                d=(p+f)//(4*a*c); b=(p*a+c)//f
                if c*d>C and (a+b)%c==0 and (a+b)//c>E:put(0,a,b,c,d)
    # Type II: e^2 (ad)(ac)(cd) <= p^2. Use integer guarantee.
    B=int(p**.4)+1
    while B**5 < p*p:B+=1
    for e in range((-p)%4,B+1,4):
        for a,b,d in triples((p+e)//4):
            if (a+b)%e==0:put(1,a,b,(a+b)//e,d)
    for g in range(1,B+1):
        for a in ds(g):
            d=g//a
            for f in ds(p+4*a*g):
                if (f+1)%(4*g)==0:
                    c=(f+1)//(4*g);put(1,a,c*((p+4*a*g)//f)-a,c,d)
            c=g//a
            for f in ds(p*c+a):
                if (f+1)%(4*g)==0:put(1,a,(p*c+a)//f,c,(f+1)//(4*g))
            c,d=a,g//a
            for f in ds(4*c*g*p+1):
                if (f+1)%(4*g)==0:
                    a=(f+1)//(4*g); b,r=divmod(p*c+a,f)
                    if not r:put(1,a,b,c,d)
    return small

if __name__=='__main__':
    print('p,I,II,distinct,ordered,min_x,min_gap,min_H2,min_Pplus',flush=True)
    for p in map(int,sys.argv[1:]):
        s=count(p); rows=[]
        for i,t in enumerate(s):
            for a,b,c,d in t:
                x=(a*b if i else a*c)*d
                U,V=a*c*d,b*c*d
                es=(x,p*U,p*V) if i else (U,V,p*a*b*d)
                assert min(es)==x and 4*es[0]*es[1]*es[2]==p*(es[0]*es[1]+es[0]*es[2]+es[1]*es[2])
                f=4*a*c*d-(1 if i else p);e=(a+b)//c
                rows.append((len(set(es)),x,4*x-p,sorted((a,b,c,d,e,f))[-2],max(map(int,P.factor(x)[0]), default=1)))
        print(p,*map(len,s),sum(k==3 for k,*_ in rows),sum({3:6,2:3,1:1}[r[0]] for r in rows),*(min(col) for col in list(zip(*rows))[1:]),sep=',',flush=True)
