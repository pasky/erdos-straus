"""Independent stdlib-only checker for the finite-family proof in THIN_CYCLO.md."""
import json,math
from pathlib import Path
from collections import Counter
assert __debug__

def check(k):
    C=json.loads(Path(f'data/z75/thin_cyclo/cert_{k}.json').read_text());H=C['H'];assert C['S']==32 and C['k']==k
    triples={int(n):xyz for n,xyz in C['triples'].items()}
    for n,(x,y,z) in triples.items():assert min(x,y,z)>0 and 4*x*y*z==n*(x*y+x*z+y*z)
    assert all(4**s+k in triples for s in range(32));covered=bytearray(H);counts=Counter()
    for P,j,kind,args in C['rows']:
        assert 0<=j<P and H%P==0;s=32+(j-32)%P
        def nr(M):
            # n mod M is constant from this first s onwards, by multiplication by 4^P.
            x=pow(4,s,M);assert x*pow(4,P,M)%M==x;return (x+k)%M
        if kind=='M':assert nr(840) not in {1,121,169,289,361,529}
        elif kind=='D':
            q,=args;assert q in triples and nr(q)==0
        elif kind=='A':
            A,u=args;assert A>0 and u>=2 and k%4==1;t,r=divmod(A+1,u);assert r==0 and min(t,u)>=2 and 4**32+k>=2*A
            n=nr(8*A);v,r=divmod(n+u,A);assert r==0 and (n+t)*t*u*v%8==0
        elif kind=='II':
            f,a,b=args;assert f>1 and min(a,b)>0 and (f+1)%(4*a*b)==0 and (b*nr(f)+a)%f==0
        elif kind=='K':
            f,K0,*ds=args;assert f>0 and f%4==3 and K0>0 and len(ds)==2
            M=4*K0*(f if any(t[2] for t in ds) else 1);n=nr(M);K,r=divmod(n+f,4);assert r==0 and K%K0==0
            rr=0
            for y,i,h in ds:
                assert y>0 and K0%y==0 and i in (0,1) and h in (0,1); rr+=y*nr(f)**i*(K//K0)**h
            assert rr%f==0
        elif kind=='gap':
            f,d,ds=args;assert len(ds)==2 and f>0 and f%4==3;g=k+f;m=(g&-g).bit_length()-1;b=g>>m
            assert m>=2 and 2*s>=m and (2*P)%d==0
            if d==4:
                assert (2*s-m)%4==2;a=math.isqrt(math.isqrt(b));assert a**4==b
            else:
                assert d>0 and d%2 and (2*s-m)%d==0;a=next(i for i in range(1,b+1) if i**d==b)
            r=(2*s-m)//d;assert pow(2,r,f)==pow(2,r+2*P//d,f);z=2**r
            if d==4: V=[2*z*z-2*z*a+a*a,2*z*z+2*z*a+a*a]
            else:
                V=[];hs=[]
                for h in range(1,d+1):
                    if d%h:continue
                    w,rem=divmod(z**h+a**h,math.prod(v for v,e in zip(V,hs) if h%e==0));assert not rem
                    V.append(w);hs.append(h)
            assert min(V)>0 and (2**(m-2))*math.prod(V)==(4**s+k+f)//4
            V.insert(0,nr(f));rr=0
            for mask,e in ds:
                assert 0<=mask<2**len(V) and 0<=e<=m-2;rr+=2**e*math.prod(v for i,v in enumerate(V) if mask>>i&1)
            assert rr%f==0
        else:raise ValueError(kind)
        covered[j::P]=bytes([1])*(H//P);counts[kind]+=1
    assert all(covered);print(k,H,'classes covered;',dict(counts),'small/divisor triples',len(triples))
for k in (297,33,273):check(k)
