import sys; sys.path.insert(0,__import__('os').path.dirname(__file__))
from gp import *
from sympy import isprime, divisors
from functools import lru_cache
pos=lambda v: all(x>0 for x in v)
def bfs_dist(p,maxd=4):
    t=(p-1)//4
    sig=tuple(sorted((t,-2*p*t,-2*p*t)))
    seen={sig:0}; fr=[sig]; d=0
    fibc={}
    while fr and d<maxd:
        d+=1; nf=[]
        for v in fr:
            for z in set(v):
                if z not in fibc: fibc[z]=fibre(p,z)
                for u in fibc[z]:
                    if u not in seen:
                        seen[u]=d; nf.append(u)
                        if pos(u): return d
        fr=nf
    return None  # >maxd
def crit9(p):
    t=(p-1)//4
    for h in divisors(t*t):
        m=p*h-t; K=4*h-1
        for D in divisors(m*m):
            if (D+h)%K==0: return True
    return False
def productive(p,z):
    return z>0 and any(pos(v) for v in fibre(p,z))
def critA(p):
    t=(p-1)//4
    for c in divisors(t*t):
        n=p*c+t
        for d in divisors(n*n):
            if (d+c)%(4*c+1)==0:
                a=(d+c)//(4*c+1); x=t+a; w=x*n//d
                assert x*n%d==0
                if productive(p,x) or productive(p,w): return True
    return False
def critB(p):
    t=(p-1)//4
    for d0 in divisors(t*t):
        for dl in (d0,-d0):
            if dl in (t,-t): continue
            for m in (dl-t, t*t//dl-t):
                B=fibre(p,p*m)
                # bucket of pm: vertices; one is the L1 vertex containing t
                for v in B:
                    if t in v: continue
                    xs=[x for x in v if x%p]
                    if xs and productive(p,xs[0]): return True
    return False
lim=int(sys.argv[1]); mism=0; cnt={}
for p in range(5,lim):
    if p%4!=1 or not isprime(p): continue
    d=bfs_dist(p,3)
    c9=crit9(p)
    pred = 2 if c9 else (3 if (critA(p) or critB(p)) else None)
    cnt[pred]=cnt.get(pred,0)+1
    if d!=pred: mism+=1; print('MISMATCH',p,d,pred)
print('checked up to',lim,cnt,'mismatches',mism)
# special p=297049
p=297049
print('297049: crit9',crit9(p),'A',critA(p),'B',critB(p),'bfs',bfs_dist(p,3))
