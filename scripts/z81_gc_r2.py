"""Finite checks for z81 GEOM_COMB §§8–10. No asymptotic inferred."""
from itertools import product
from math import gcd, lcm, prod
from random import Random
from fractions import Fraction
from pathlib import Path
from z81_gc_screen import factors, prime, window, divisors2


def code_check():
    d,m=16,8; rng=Random(31703)
    for _ in range(100):
        v=[rng.randrange(1<<m) for _ in range(d)]
        # Syndrome minimum via subset DP, dual via characters.
        dp={0:0}
        for b in v:
            old=dp.copy()
            for k,n in old.items(): dp[k^b]=min(dp.get(k^b,d+1),n+1)
        if len(dp)!=1<<m: continue
        s=min(sum((a&b).bit_count()%2 for b in v) for a in range(1<<m) if a.bit_count()%2)
        r=dp[(1<<m)-1]
        if min(r,s)>=3:
            print('columns',v,'R^2',r,'4S^2',s); return
    raise RuntimeError('code check failed')


def variance_check(type_i):
    # Direct finite Haar, then covariance via the independent CRT formula.
    primes=(17,19,23,29); ks=(3,7,11)
    period=prod(primes); atoms=[]
    for k in ks:
        for signs in product((-1,0,1),repeat=len(primes)):
            if not any(signs) or (not type_i and next(s for s in signs if s)!=1): continue
            a=prod(r for r,e in zip(primes,signs) if e==1)
            b=prod(r for r,e in zip(primes,signs) if e==-1)
            value=4*a*a*b+1 if type_i else a+b
            if value%k==0: atoms.append((a*b,-k))
    def phi(n):return prod(r-1 for r in primes if n%r==0)
    hist=[0]*(len(atoms)+1)
    for n in range(period):
        if gcd(n,period)==1:hist[sum((n-r)%d==0 for d,r in atoms)]+=1
    mean=sum(Fraction(1,phi(d)) for d,r in atoms)
    second=sum(Fraction(1,phi(lcm(d,e))) for d,r in atoms for e,s in atoms if (r-s)%gcd(d,e)==0)
    assert mean==Fraction(sum(i*v for i,v in enumerate(hist)),sum(hist))
    assert second==Fraction(sum(i*i*v for i,v in enumerate(hist)),sum(hist))
    print('type',1 if type_i else 2,'atoms',len(atoms),'mean',mean,'variance',second-mean*mean)


def cofactor_check():
    # Small host for the deterministic all-cancel test (not the huge sieve constant).
    r=next(r for r in range(839,10**6,840) if prime(r) and r>100000)
    def base_ok(w):
        if any(pow(w,(r-1)//l,r)==1 for l,_ in factors(r-1)):return False
        return all((pow(8,j,r)*prod(pow(q,e+j,r) for q,e in zip((3,5,7,-2,w),es)))%r!=r-1 for j in (-1,0,1) for es in product((-1,0,1),repeat=5))
    g=next(w for w in range(2,r) if base_ok(w))
    print('sample r, primitive class, 4-only planted ratio',r,g,(-2*pow(2,-1,r))%r)
    # Replay the actual large controls through the same-window full box in §3.
    import json
    for case in json.loads(Path('data/z81/geom_comb/smooth.json').read_text()):
        p=case['p'];x=11**case['b']*prod(case['Q']);assert p==8*x-31
        booleans=[]
        for m,extra in ((8,0),(4,1)):
            residues={pow(11,i,31)*pow(p,j,31)*pow(2,e,31)%31 for i in range(-case['b'],case['b']+1) for j in (-1,0,1) for e in range(-extra,extra+1)}
            booleans.append(30 in residues)
        print('paired full hits (8,4)',case['b'],booleans)


def max_gap_check():
    # Compare the maximum over actual windows from full fractions and the
    # strict-type divisor tests. Bound the literal y loop by k*y<=2*p*x.
    for p in (17,73,193,241,409,577,1009):
        max1={'I':1,'II':1};max2=max1.copy();ybound=13
        for x in range(p//4+1,3*p//4+1):
            k=4*x-p;s=p*x
            if any(l>ybound for l,_ in factors(k)): continue
            for typ in window(p,4,x,True):
                # k>=p can have a solution with a smaller denominator;
                # reconstruct before counting in a sorted maximum.
                for D in divisors2(factors(x)):
                    h=(p*p if typ=='I' else p)*D
                    y,r=divmod(s+h,k); z,t=divmod(s+s*s//h,k)
                    if not r and not t and min(y,z)>=x: max1[typ]=max(max1[typ],k);break
            for y in range(max(x,s//k+1),2*s//k+1):
                z,r=divmod(s*y,k*y-s)
                if r or z<y:continue
                typ='II' if y%p==z%p==0 else 'I';max2[typ]=max(max2[typ],k)
        assert max1==max2
        print('paired maximum check',p,ybound,max1)


if __name__=='__main__':
    code_check();variance_check(False);variance_check(True);cofactor_check();max_gap_check()
