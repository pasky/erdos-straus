# z52d pass2 SK1 fix round: Z1137 (toy annealer on the (star) word energy) and Z1138 (parallel tempering over two
# box sizes = two charts with a known overlap). Energy E(u,B,C) = |4uBC-u-B-p|. Zeros are verified by integer arithmetic.
# Exact baseline: in-box words (u,B,C <= K) enumerated for each prime p = 1 mod 4 <= 2000.
import math, random
random.seed(11)
K=40
def isp(m): return m>1 and all(m%d for d in range(2,int(m**.5)+1))
primes=[p for p in range(5,2001,4) if isp(p)]
# exact in-box baseline
inbox={}
for u in range(1,K+1):
    for B in range(1,K+1):
        for C in range(1,K+1):
            n=4*u*B*C-u-B
            if 1<=n<=2000: inbox.setdefault(n,0); inbox[n]+=1
exact=set(p for p in primes if inbox.get(p,0)>0)
def E(u,B,C,p): return abs(4*u*B*C-u-B-p)
def anneal(p,steps=40000,T0=2.0):
    u,B,C=random.randint(1,K),random.randint(1,K),random.randint(1,K); e=E(u,B,C,p)
    best=None
    for s in range(steps):
        T=T0*(1-s/steps)+0.05
        nu,nB,nC=u+random.choice([-1,0,1]),B+random.choice([-1,0,1]),C+random.choice([-1,0,1])
        if not(1<=nu<=K and 1<=nB<=K and 1<=nC<=K): continue
        ne=E(nu,nB,nC,p)
        if ne<=e or random.random()<math.exp(-(ne-e)/T): u,B,C,e=nu,nB,nC,ne
        if e==0:
            n=4*u*B*C-u-B
            assert n==p
            return (u,B,C)
    return None
def tempering(p,steps=40000,temps=(0.2,0.6,1.5,4.0)):
    reps=[[random.randint(1,K),random.randint(1,K),random.randint(1,K)] for _ in temps]
    for s in range(steps):
        for r,T in enumerate(temps):
            c=reps[r]
            nu=[c[i]+random.choice([-1,0,1]) for i in range(3)]
            if not all(1<=x<=K for x in nu): continue
            de=E(*nu,p)-E(*c,p)
            if de<=0 or random.random()<math.exp(-de/T): reps[r]=nu
            if E(*reps[r],p)==0:
                u,B,C=reps[r]; assert 4*u*B*C-u-B==p; return (u,B,C)
        if s%10==0:
            r=random.randrange(len(temps)-1)
            d=(E(*reps[r],p)-E(*reps[r+1],p))*(1/temps[r]-1/temps[r+1])
            if d>=0 or random.random()<math.exp(d): reps[r],reps[r+1]=reps[r+1],reps[r]
    return None
ann_hit=set(); pt_hit=set(); ann_false=0; pt_false=0
for p in primes:
    if anneal(p) is not None: ann_hit.add(p)
    if tempering(p) is not None: pt_hit.add(p)
print(f"primes 1 mod 4 <=2000: {len(primes)}; in-box exact (K={K}) R>0: {len(exact)}")
print(f"annealer found words for {len(ann_hit)} primes, all inside exact set: {ann_hit<=exact}; recall {len(ann_hit&exact)}/{len(exact)}")
print(f"tempering found words for {len(pt_hit)} primes, all inside exact set: {pt_hit<=exact}; recall {len(pt_hit&exact)}/{len(exact)}")
print("primes with exact in-box word missed by tempering (first 8):", sorted(exact-pt_hit)[:8])
