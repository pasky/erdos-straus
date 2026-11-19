"""One-slot transfer from 4/Q via scaling by k to 4/p, p=kQ-d.
Run: uv run --no-sync python scripts/z74_single_retune.py
"""
from functools import cache
from math import gcd
from sympy import divisors, factorint, primerange


@cache
def ds_square(n):
    return tuple(divisors(n*n))


def donor_pairs(Q, u):
    c, h = 4*u-Q, Q*u
    if c <= 0:
        return
    g = gcd(c,h); c//=g; h//=g
    for t in ds_square(h):
        if t > h: break
        if (h+t)%c == 0:
            yield (h+t)//c, (h+h*h//t)//c


def transfer(Q,k,d):
    """Every 3-term donor with one replaced denominator; no upper search cap."""
    p = k*Q-d; A=p*Q
    for h in divisors(k*A*A):
        if (h-A)%(4*d): continue
        u=(h-A)//(4*d)
        if u<=0 or (k*u*A)%h: continue
        if d>0 and p%2 and gcd(k*Q,p)==1:
            assert u%p==0  # p is assumed prime in this experiment
        v=k*u*A//h
        for x,y in donor_pairs(Q,u):
            assert 4*x*y*u == Q*(x*y+x*u+y*u)
            X,Y=k*x,k*y
            assert 4*X*Y*v == p*(X*Y+X*v+Y*v)
            yield x,y,u,v


def positions(Q,k,d):
    """Independent ES(Q) search, only for downward change and p>Q coprime to 4kQ."""
    p=k*Q-d; assert p>Q and gcd(4*k*Q*d,p)==1 and d>0 and 4*p>2*Q
    # The other two donor terms are p-multiples, and the remaining one is x.
    for x in range(Q//4+1, p*Q//(4*p-2*Q)+1):
        c,h=p*(4*x-Q),Q*x
        g=gcd(c,h); c//=g; h//=g
        for t in ds_square(h):
            if t>h: break
            if (t+h)%c: continue
            a,b=(t+h)//c,(h+h*h//t)//c
            for u,y in {(p*a,p*b),(p*b,p*a)}:
                h1=p*Q+4*d*u
                if k*u*p*Q%h1==0:
                    yield x,y,u,k*u*p*Q//h1


def check():
    hits=[]; small=0; failures=0
    for Q in range(2,72):
        for p in primerange(Q+1,3*Q):
            k=3;d=3*Q-p
            if gcd(4*k*Q*d,p)>1:continue
            # Compare all witnesses, normalizing retained donor pair only.
            norm=lambda rows:{(min(x,y),max(x,y),u,v) for x,y,u,v in rows}
            x=norm(positions(Q,k,d)); y=norm(transfer(Q,k,d)); assert x==y
            small+=1
            if x: hits.append((Q,p,min(x)))
    print('donor-first vs difference-first pairs checked:',small,'hits:',len(hits),'examples:',hits[:4])
    for p in primerange(1,50_000):
        if p%840!=1 or p%11 not in (2,6):continue
        Q=(p+11)//12;R=11*Q-10
        fs=[r%11 for r,e in factorint(Q).items() for _ in range(e) if r%11!=1]
        rs=[r%11 for r,e in factorint(R).items() for _ in range(e) if r%11!=1]
        if fs!=[p%11] or not (all(r in (3,4,5,9) for r in rs) or sorted(rs)==[2,6]):continue
        t=list(positions(Q,12,11));failures+=1
        print('joint-11 miss p,Q,successful retunings:',p,Q,t[:2],len(t))
    print('joint-11 miss inputs:',failures)

if __name__=='__main__':check()
