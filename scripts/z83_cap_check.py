"""Exact finite probes of the multiscale comparison and signed menu bound."""
from fractions import Fraction as F
from itertools import product
from math import gcd, prod, isqrt
from pathlib import Path


def factors(n):
    out = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            out[i] = out.get(i, 0) + 1
        i += 1
    if n > 1:
        out[n] = 1
    return out


def interpolation():
    # Signed nonnegative degree-two cylinder expansion, differing coordinate costs.
    coords = (3, 4, 5)
    fs = ({0}, {1, 3}, {1})
    costs = (1, 3, 5)
    def mean(z):
        ans = F(0)
        for x in product(*(range(q) for q in coords)):
            bits = [d in a for d, a in zip(x, fs)]
            weight = prod((1-z**c)/q + z**c*(not hit)/(q-len(a))
                          for c, q, a, hit in zip(costs, coords, fs, bits))
            ans += weight * (1 - sum(bits))**2
        return ans
    # Polynomials are multilinear in the marginal laws; a squared Boolean digit collapses.
    d = sum(costs[-2:])
    grid = [F(j, 3*d) for j in range(d+1)]
    values = list(map(mean, grid))
    def interp(t):
        return sum(v*prod((t-y)/(x-y) for y in grid if x!=y)
                   for v,x in zip(values,grid))
    for t in [F(1), F(1,2), F(2,7), F(7,13)]:
        assert mean(t)==interp(t)
    assert mean(F(1))==1
    print('W: degree bound',d,'base',mean(F(0)),'repaired',mean(F(1)))


def screens():
    zeros = [int(s) for s in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if s and not s.startswith('#')]
    panels = [[i*i for i in range(3,62,2)], [11,17,131,241,1590284203561,6955940568721],
              [105,1465,3865,4545,10305,12145,39361,67425],
              zeros+[17401609,2521,3361,21841,76441,113035442521,3189177846574333650961]]
    labels = []
    for A in range(1,501):
        ff = 4*A-1
        ds = [1]
        for q,i in factors(A).items():
            digits = list(range(2*i+1))+([2*i+2] if q>2 else [])
            ds = [d*q**e for d in ds for e in digits]
        labels.extend((A,ff,d) for d in ds)
    for j, panel in enumerate(panels,1):
        hits = []
        for n in panel:
            cnt = 0
            for A,ff,d in labels:
                if (n+4*d)%ff or gcd(n,d*ff)>1: continue
                V=(n+4*d)//ff; x=(n+V)//4; y=n*A; z=F(n*x*A,d); r=isqrt(z.denominator)
                assert F(4,n)==F(1,x)+F(1,y)+1/z and r*r==z.denominator
                assert gcd(2*n,r)==1 and y%r==0 and all(v==1 for v in factors(r).values())
                cnt+= r>1
            hits.append(cnt)
        if j==1: assert not any(hits)
        print('F'+str(j), 'nonintegral root hits',sum(bool(c) for c in hits),'/',len(panel),'per-input',hits)


def signed():
    checks = mixed = flips = 0
    for p in range(17,5000,8):
        if factors(p)!={p:1}: continue
        for a,b,c in product(range(-3,5),repeat=3):
            vec=((3,a),(5,b),(7,c)); u=prod(q**max(0,t) for q,t in vec); v=prod(q**max(0,-t) for q,t in vec)
            if u==v: continue
            for m in [d for d in range(3,100,4) if (u+v)%d==0 and gcd(d,p)==1]:
                K=(p+m)//4; vals=factors(K)
                if any(t and (q not in vals or -t>vals[q] or (t>vals[q] and (t-vals[q])%2)) for q,t in vec): continue
                E=max([0]+[(t-vals.get(q,0))//2 for q,t in vec]); S=prod(q for q,t in vec if t); W=S**(2*E)
                assert u*v<=(p+W+1)*W**2
                D=K*u//v; assert D*v==K*u and (K+D)%m==0
                A=(K+D)//m; z=F(p*K*A,D)
                assert F(4,p)==F(1,K)+F(1,p*A)+1/z
                r=isqrt(z.denominator); assert r*r==z.denominator
                assert E==max(factors(r).values(),default=0)
                checks+=1; mixed+= bool(u>1 and v>1); flips+=u<v
    assert mixed and flips
    print('S: exact signed packets',checks,'mixed',mixed,'reoriented',flips)


if __name__=='__main__':
    interpolation(); signed(); screens()
