"""Finite arithmetic for CAP_CONST §§6–9, not tests of AP conjectures."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, isqrt, lcm, prod
from pathlib import Path
from z82_cap_hierarchy import factor, packet, check_cap


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))


def linked(n,y,z,b):
    return gcd(2*n,z.denominator)==1 and all(y%p==0 and v<=b for p,v in factor(z.denominator).items())


def linked_check():
    ntest=nonlegal=mixed=0; example=None
    for A in range(1,80):
        f=4*A-1
        for b in [1,2,3]:
            digits=[range(2*h+(b if s%2 else 0)+1) for s,h in factor(A).items()]
            labels={prod(s**d for s,d in zip(factor(A),ds)) for ds in product(*digits)}
            for D in labels|set(range(1,100)):
                if gcd(D,f)>1: continue
                n=(-4*D)%f+f
                while gcd(D,n)>1: n+=f
                x,y,z=packet(n,f,D); ok=linked(n,y,z,b)
                assert ok==(D in labels); ntest+=1;nonlegal+=not ok
                ds=factor(z.denominator)
                if ok and b==2 and set(ds.values())=={1,2}:
                    mixed+=1
                    if example is None: example=(n,f,D,x,y,str(z))
    assert mixed
    print('linked unit chart two-way, rejected, exact mixed cubefree packets:',ntest,nonlegal,mixed,'example:',example)
    # Same tag-3 class: a shared prime need not remain in the root.
    for n,want_z in [(13,F(26,3)),(24,F(24))]:
        _,y,z=packet(n,11,3**3)
        assert z==want_z and linked(n,y,z,1)
    # A shared prime that does remain invalidates the linked packet.
    _,y,z=packet(51,11,3**5)
    assert z==F(68,3) and not linked(51,y,z,3)
    print('nonunit controls: tag 3 at n=13,24 gives z=26/3,24; tag 5 at n=51 gives illegal z=68/3')
    ledger=Path(__file__).resolve().parents[1]/'data/z58/screens/star_prime_zeros.txt'
    star=[int(x) for x in ledger.read_text().splitlines() if x and not x.startswith('#')]
    groups={'squares':[s*s for s in range(1,130,2)],'F2':[11,17,131,241,1590284203561,6955940568721],
        'F3':[105,1465,3865,4545,10305,12145,39361,67425], 'F4':star+[17401609,2521,3361,21841,76441,113035442521,183783601,2238327841,4367159449,3153419441929]}
    for name,ns in groups.items():
        hits=0
        for n in ns:
            for a in range(1,500):
                f=4*a-1
                got=False
                for s,v in factor(a).items():
                    if s==2 or n%s==0: continue
                    D=s**(2*v+1)
                    if (n+4*D)%f==0:
                        _,y,z=packet(n,f,D);assert z.denominator==s and linked(n,y,z,2)
                        got=True;break
                if got: hits+=1;break
        if name=='squares': assert not hits
        print(name,'actual odd-overflow shots (numerator 4 only):',hits,'of',len(ns))


def cofactor():
    base=[5,7,11,13,17,19,23,29]; buckets=defaultdict(list)
    for u,v in combinations(base,2):
        d=u*v;b=1
        while not prime(1+2*b*d): b+=2
        q=1+2*b*d; assert q%4==3; buckets[b].append(q)
    b,T=max(buckets.items(),key=lambda kv:len(kv[1])); h=3*b*prod(base)
    assert all(h%((q-1)//2)==0 for q in T)
    # Separate two-donor test from the b=1 bucket (not the largest bucket).
    qs=buckets[1][:2]; hsmall=lcm(3,*[(q-1)//2 for q in qs]); ex=None
    for p in [17,41,73,89,97,193,241,409,577,2521,3361,21841]:
        for s in range(5,500,4):
            if not prime(s) or pow(s,(p-1)//2,p)!=p-1: continue
            for m in qs:
                if (p+m)%(4*s) or (p+m)%(4*s*s)==0 or pow(s,hsmall,m)!=m-1: continue
                K=(p+m)//4; a=K*((s**hsmall+1)//m); z=F(p*a,s**hsmall)
                assert z.denominator==s**(hsmall-1) and F(1,K)+F(1,p*a)+1/z==F(4,p)
                ex=(p,s,m,hsmall); break
            if ex: break
        if ex: break
    print('least-AP common odd cofactor, donors, h:',b,len(T),h)
    # If the finite hard list missed, synthesize a compatible prime input.
    if ex is None:
        m=qs[0]; hsmall=lcm(3,(m-1)//2)
        for s in range(5,200,4):
            if prime(s) and pow(s,hsmall,m)==m-1:
                p=next((p for p in range(17,100000,8) if prime(p) and (p+m)%(4*s)==0 and (p+m)%(4*s*s) and pow(s,(p-1)//2,p)==p-1),None)
                if p:
                    K=(p+m)//4;a=K*((s**hsmall+1)//m);z=F(p*a,s**hsmall)
                    assert z.denominator==s**(hsmall-1) and F(1,K)+F(1,p*a)+1/z==F(4,p)
                    ex=(p,s,m,hsmall);break
    assert ex
    print('exact inverse packet from b=1 donor list',qs,'(p,s,m,h):',ex)


def band():
    # This includes integer labels larger than the pivot, with no modulus
    # division based merely on their size.
    labels=[(a,m,a*(m**j)) for a in [13,17,19,23] for m in [1,7,11] for j in ([0] if m==1 else [2,4,6,8])];ks=(1,3,5)
    assert len(labels)==len({D for _,_,D in labels})
    killed=kept=big=0; pool=defaultdict(list)
    for ell in range(251,3500):
        if not prime(ell): continue
        if len({D%ell for _,_,D in labels})!=len(labels): killed+=1;continue
        for a,m,D in labels:
            for k in ks:
                f=k*ell
                if (f+1)%(4*a*m): continue
                n=(-4*D)%f + f
                while gcd(n,m)!=1:n+=f
                _,y,z=packet(n,f,D);assert check_cap(n,y,z,3)
                pool[ell].append((k,D,F(a-1,a)))
                kept+=1;big+=D>ell
    assert killed and big and kept
    # Arithmetic identity checks for second and fourth centered moments of
    # two independent pivot digits. The separate mean check detects collisions;
    # these finite identities do not test the theorem's tail bound.
    fibers=moments=0
    for c in range(15): # include nonunits, repair at separate multiplier primes
        active=lambda k,D: k==1 or ((c%k or 1)+4*D)%k==0
        row=[]
        for ell,tuples in sorted(pool.items()):
            w={(-4*D)%ell:v for k,D,v in tuples if active(k,D)}
            if not w:continue
            hist=Counter(w.values());hist[F(0)]+=ell-len(w)
            mu=sum(v*h for v,h in hist.items())/ell
            assert mu==sum((v for k,D,v in tuples if active(k,D)),F(0))/ell
            row.append((ell,hist,mu))
            if len(row)==2:break
        assert len(row)==2
        (l,h,x),(r,g,y)=row
        for j in [1,2]:
            direct=sum(F(i*k,l*r)*(a+b-x-y)**(2*j) for a,i in h.items() for b,k in g.items())
            m2=lambda P,f,m:sum(F(i,P)*(v-m)**2 for v,i in f.items())
            single=sum(sum(F(i,P)*(v-m)**(2*j) for v,i in f.items()) for P,f,m in row)
            assert direct==single+(6*m2(l,h,x)*m2(r,g,y) if j==2 else 0);moments+=1
        fibers+=1
    print('band colliding pivots discarded, retained packets, D>pivot:',killed,kept,big,'fibres/exact centered moments:',fibers,moments)


if __name__=='__main__':
    linked_check();cofactor();band()
