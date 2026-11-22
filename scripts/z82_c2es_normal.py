"""Exact orbit normal forms. Compare to ALL positive points at specified small primes."""
from fractions import Fraction as F
from math import prod,gcd
from functools import lru_cache
from z82_c2es_panel import check,prime,half_window,divisors
from z82_c2es_moves import move


def root(h,xyz):
    t=tuple(h/F(a) for a in xyz); assert sum(t)==1 and min(t)>0
    steps=0
    while 2*max(t)>1:
        t=move(t,t.index(max(t)));steps+=1
    return tuple(sorted(t)),steps


def factors(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            j=0
            while n%d==0:n//=d;j+=1
            out.append((d,j))
        d=3 if d==2 else d+2
    if n>1:out.append((n,1))
    return out


def all_integral(n):
    # Prime inputs. Only divisors <=px are needed for y<=z, hence no p^2 factor.
    assert prime(n)
    res=[]
    for x in range(n//4+1,3*n//4+1):
        m=4*x-n;g=n*x
        ds=[1]
        for p,j in factors(x):ds=[d*p**a for d in ds for a in range(2*j+1)]
        for d in ds:
            for e in (d,n*d):
                if e>g or (g+e)%m:continue
                y=(g+e)//m;z=(g+g*g//e)//m
                if y<x:continue
                check(n,4,(x,y,z));res.append((x,y,z))
    assert len(set(res))==len(res)
    return res


def half(n,params):
    s,a,b,m=params;k=(n+m)//4
    y=n*k*(a*s*s+b)//(m*b);z=F(y*b,a*s*s)
    check(n,4,(k,y,z));assert z.denominator==s and gcd(n,s)==1 and k%s==y%s==0
    return k,y,z


@lru_cache(None)
def sq(n):return prod(p for p,j in factors(n) if j%2)


def signature(xyz):
    c=[sq(F(a).numerator)*sq(F(a).denominator) for a in xyz]
    return tuple(sorted(c[i]*c[i-1]//gcd(c[i],c[i-1])**2 for i in range(3)))


def main():
    for n in (409,2521,3361,21841):
        ints=all_integral(n);h=F(n,4); results={};by_sig={}
        for t in ints:by_sig.setdefault(signature(t),[]).append(t)
        # avoid huge normal-form denominators from ES points already separated by squareclass
        seeds=[('hybrid',half(n,half_window(n,4)))]
        if n==3361:
            a=(n*n+11)//4;s=(4*a*a+n)//11;seeds.append(('quartic',(s*a,s*(s-a),F(n*s+1,4*s))))
        for label,xyz in seeds:
            R,height=root(h,xyz); candidates=by_sig.get(signature(xyz),[])
            hits=[t for t in candidates if root(h,t)[0]==R]
            print('full orbit n seed #ES #signature #actual steps',n,label,len(ints),len(candidates),len(hits),height)
        # Include a constructed success as a positive control, not a method of discovering integral points.
        t=ints[0];R,j=root(h,t);u=tuple(h/w for w in t)
        for i in (1,2,1,0,1):u=move(u,i)
        assert root(h,tuple(h/w for w in u))[0]==R

if __name__=='__main__':main()
