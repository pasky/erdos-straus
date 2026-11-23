"""Construct a wheel cover over the nonresidues mod q. All factors used divide
exactly; an unfactored remainder is a single block, never presumed prime.
Run: z83_cap_atlas.py [q=0 (all)] [maximum E=10] [optional extra odd prime]."""
import sys
import os
import gzip
from functools import lru_cache
from itertools import product
from math import gcd,isqrt,prod


def sieve(n):
    s=bytearray([1])*(n+1)
    for i in range(2,isqrt(n)+1):
        if s[i]: s[i*i::i]=bytes(1+(n-i*i)//i)
    return [i for i in range(2,n+1) if s[i]]
PR=sieve(997)

def blocks(n):
    f=[]
    for s in PR:
        if s*s>n: break
        if n%s: continue
        e=0
        while n%s==0: n//=s; e+=1
        f.append((s,e))
    if n>1: f.append((n,1))
    return f


def divs(f):
    out=[1]
    for s,e in f: out=[a*s**j for a in out for j in range(e+1)]
    return out


def atlas(q,limit,extra=0,record=None):
    # Prime inputs in the hard classes; q>=11. A small extra prime is optional.
    S=tuple(t for t in (3,5,7,extra) if t and t!=q)
    digs=[[d for d in range(1,t*t) if gcd(d,t)==1 and (t>q or pow(d,(t-1)//2,t)==1)] for t in S]
    # 2-adic wheel: p=1 or 9 mod 16. Mixed-radix point order.
    ds=[[1,9]]+digs; ps=(2,)+S
    strides=[prod(map(len,ds[:i])) for i in range(len(ds))]
    size=prod(map(len,ds)); full=(1<<size)-1
    @lru_cache(None)
    def one(i,mod,res):
        st=strides[i]; period=len(ds[i])*st
        seed=sum(((1<<st)-1)<<(j*st) for j,d in enumerate(ds[i]) if d%mod==res)
        return seed*(full//((1<<period)-1))
    nr=[i for i in range(1,q) if pow(i,(q-1)//2,q)==q-1]; left={i:full for i in nr}; seen={i:{} for i in nr}
    witnesses=0; maxwin=0
    def mark(c,bits,exc,win,word):
        nonlocal witnesses,maxwin
        bits &=left[c]
        if exc is not None: bits &=~seen[c].get(exc,0)
        if not bits: return
        if record is not None: print(q,E,*word,win,file=record)
        witnesses+=1; maxwin=max(maxwin,win)
        if exc is None: left[c]&=~bits; return
        ex=seen[c]
        for other,v in ex.items():
            if exc!=other: left[c]&=~(bits&v)
        if left[c]&bits: ex[exc]=ex.get(exc,0)|(left[c]&bits)
    # Dictionary f=q*k; S-small digits modulo f generate no q² holes.
    cofs=divs([(s,2) for s in S]); q2=q*q
    for E in range(limit+1):
        for k in cofs:
            f=k*q
            if f%4!=3: continue
            A=(f+1)//4
            # Composite residual blocks only produce legal digits if raised as units:
            # use trial division to completion here instead of relying on that.
            fac=blocks(A)
            if any(s>997*997 for s,_ in fac): continue
            vals={1:1}
            for s,b in fac:
                digits=list(range(2*b+1))+([2*b+2*j for j in range(1,E+1)] if s>2 else [])
                vals={v*pow(s,j,f)%f:n*s**j for j in digits for v,n in vals.items()}
            both={(-4*d)%f:('D',n,1) for d,n in vals.items()}
            both.update({pow(r,-1,f):('I',n,1) for r,(_,n,_) in both.items()})
            for r in sorted(both):
                c=r%q
                if not left.get(c): continue
                bits=full
                for i,s in enumerate(S,1):
                    if k%s==0:
                        mod=s*s if k%(s*s)==0 else s
                        bits &=one(i,mod,r%mod)
                mark(c,bits,None,f,both[r])
        # D1=p²D (positive), or D1=K²U/V (negative), in the fixed-K chart.
        # digits are (exponent,cost): K divisible by prime**cost. Test all
        # enabled words anew: even old digits may have lower cost at higher E.
        for branch in ('plus','minus'):
            axes=[]
            for i,t in enumerate(ps+(q,)):
                B=1 if t==q else 2
                if branch=='plus':
                    choices=[(d,max(1,(d+1)//2) if t==2 or d%2 else max(1,d//2-E)) for d in range(1,2*(B+(0 if t==2 else E))+1)]
                else:
                    choices=[(-d,(d+1)//2) for d in range(1,2*B+1)]+([(2*j,1) for j in range(1,E+1)] if t!=2 else [])
                axes.append(([(0,0)] if t!=q else [])+[(d,cost) for d,cost in choices if cost<=B])
            for terms in product(*axes):
                u=prod(t**max(0,d) for t,(d,cost) in zip(ps+(q,),terms)); v=prod(t**max(0,-d) for t,(d,cost) in zip(ps+(q,),terms))
                value=4*u+1 if branch=='plus' else u+4*v
                for m in divs(blocks(value)):
                    c=(-m)%q
                    if m%4!=3 or not left.get(c): continue
                    bits=left[c]
                    for i,(d,cost) in enumerate(terms[:-1]):
                        if cost:
                            mod=ps[i]**cost*(4 if i==0 else 1); bits &=one(i,mod,(-m)%mod)
                            if not bits: break
                    if bits: mark(c,bits,None,m,(branch,u,v))
        # Include terms first enabled exactly at E.
        for ht in [1,-1]+list(range(3,2*E+2,2)):
            he=max(0,(ht-1)//2)
            digits=[-2,-1,0,1,2]
            for exps in product(digits, *[[-2,-1,0,1,2]+list(range(3,2*E+2,2)) for t in S]):
                if max([he]+[max(0,(d-1)//2) for d in exps])!=E: continue
                u=prod(t**max(0,d) for t,d in zip(ps,exps))*q**max(0,ht)
                v=prod(t**max(0,-d) for t,d in zip(ps,exps))*q**max(0,-ht)
                for m in divs(blocks(u+v)):
                    c=(-m)%q
                    if m%4!=3 or not left.get(c): continue
                    r=-m; bits=left[c]; d=exps[0]
                    if d: mod=4*2**abs(d); bits &=one(0,mod,r%mod)
                    for i,(s,d) in enumerate(zip(S,exps[1:]),1):
                        if not bits: break
                        if d:
                            mod=s*s if abs(d)==2 else s
                            bits &=one(i,mod,r%mod)
                            if d>2: bits &=~one(i,s*s,r%(s*s))
                    if bits: mark(c,bits,m%q2 if ht>1 else None,m,('N',u,v))
        if not any(left.values()): break
    return E,sum(i.bit_count() for i in left.values()),size,witnesses,maxwin

if __name__=='__main__':
    args=[int(x) for x in sys.argv[1:]]; q,E,t=(args+[0,10,0][len(args):])
    from contextlib import nullcontext
    from io import TextIOWrapper
    name=os.environ.get('ATLAS_OUT')
    with (TextIOWrapper(gzip.GzipFile(name,'wb',mtime=0)) if name else nullcontext()) as rec:
        for s in ([q] if q else [r for r in PR if 11<=r<=379]): print(s,*atlas(s,E,t,rec),flush=True)
