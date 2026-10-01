import sys; sys.path.insert(0,__import__('os').path.dirname(__file__))
from gp import *
from sympy import isprime, divisors, factorint, primerange, divisor_count
pos=lambda v: all(x>0 for x in v)
bad=defaultdict(int); nB=0
# Lemma B/C
for k in range(2,8):
    M=4*k+1
    for x in range(2,40000):
        f=factorint(x)
        if not all(q%M==1 for q in f): continue
        t=x+k; p=4*t+1
        if not isprime(p): continue
        nB+=1
        F=fibre(p,x)
        pred={tuple(sorted((x,-p*(x-d)//M, p*x*(x-d)//(M*d)))) for d in divisors(x*x) if d<x}
        if F!=pred: bad['B']+=1
        if len(F)!=(divisor_count(x*x)-1)//2: bad['Bcount']+=1
        for d in divisors(x):
            w=x//d
            if w>1 and w%4==1:
                Dd=tuple(sorted((x-d,-p*(x-d)//M,-p*(w-1)//4)))
                Fd=fibre(p,-p*(x-d)//M)
                Vd=tuple(sorted((x,-p*(x-d)//M, p*x*(x-d)//(M*d))))
                if Fd!={Vd,Dd}: bad['C']+=1
print('Lemma B/C instances',nB,dict(bad))
# Lemma E, fresh, fibre parity
bad=defaultdict(int); cE=0
for p in primerange(5,1500):
    if p%4!=1: continue
    t=(p-1)//4
    for a in range(1,t+1):
        x=t+a
        if x%p==0: continue
        F=fibre(p,x)
        # fibre parity
        r=4*x-p; s=p*x
        Np=sum(1 for D in divisors(s*s) if (D+s)%r==0)
        Nm=sum(1 for D in divisors(s*s) if (D-s)%r==0)
        if Np%2 or Nm%2==0: bad['parity']+=1
        npv=sum(1 for v in F if pos(v)); n1=sum(1 for v in F if sum(1 for y in v if y<0)==1)
        if npv!=Np//2 or n1!=(Nm-1)//2 or npv+n1!=len(F): bad['paritycount']+=1
        if any(q%(4*a-1)==4*a-2 for q in factorint(x)):
            cE+=1
            if F and npv==0: bad['E']+=1
        # fresh: type I exits / type II exits at anchor need nonresidue
        for v in F:
            if pos(v):
                ps=[y for y in v if y%p==0]
                if len(ps)==1:  # Type I exit: (z, p(z+pD)/q, (pz+z^2/D)/q)
                    y=[u for u in v if u%p and u!=x] or [x]
                    w=y[0]; q=r
                    # D from w=(pz+z^2/D)/q -> z^2/D = q w - p z
                    D=x*x//(q*w-p*x)
                    if legendre(D,p)!=-1: bad['freshI']+=1
                else:
                    m=ps[0]//p; D=q=r; D=q*ps[0]//p - x  # p(z+D)/q = pm -> D = q m - z
                    if legendre(x*D,p)!=-1: bad['freshII']+=1
    # bucket version of E and fresh(1)
    for h in range(1,40):
        m=p*h-t
        if m%p==0: continue
        F=fibre(p,p*m)
        if any(q%(4*h-1)==4*h-2 for q in factorint(m)):
            if F and not any(pos(v) for v in F): bad['Ebucket']+=1
        if (t*t)%h==0:
            for v in F:
                if pos(v):
                    ys=[u for u in v if u%p]; D=(4*h-1)*ys[0]-m
                    if legendre(D,p)!=-1: bad['fresh1']+=1
    # X-branch path validity
    for d in divisors(t*t):
        z=t+d; v=tuple(sorted((-p*t,z,t*z//d)))
        if v not in fibre(p,-p*t): bad['Xpath']+=1
print('E instances',cE,dict(bad))
