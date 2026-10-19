"""Exact cyclotomic elimination and shifted-trace toy, bounded degree <= 128.
Run: ulimit -v 2000000; timeout 120 uv run python scripts/z46_primitive_intersection_algebra.py
"""
import json
from math import comb, gcd
from pathlib import Path
from sympy import Poly, QQ, Rational, divisors, factorint, symbols, totient
from z46_primitive_intersection_scan import exact, recurrence, factors

OUT=Path('data/z46_primitive_intersection')
X=symbols('X')

def specialized_phi(t):
    cs={}
    for d0 in divisors(t):
        d=int(d0)
        if d == 1:
            continue
        u=Poly(sum(Rational(comb(d,2*j+1),2**(d-1)) *
                   Rational(-1,t)**j * X**(d-2*j-1)
                   for j in range((d+1)//2)),X,domain=QQ)
        for e in divisors(d):
            if 1 < e < d:
                u=u.exquo(cs[int(e)])
        cs[d]=u
    assert cs[t].degree() == int(totient(t))
    den,num=cs[t].clear_denoms()
    assert all(int(q) in factors(2*t) for q in factorint(int(den)))
    return int(den),num

def main():
    OUT.mkdir(exist_ok=True)
    rows=[]
    for t in range(4,129,4):
        den,f=specialized_phi(t)
        roots=f.ground_roots()
        assert set(roots) == ({Rational(-1,2),Rational(1,2)} if t == 4 else set())
        affine=[]
        for a in range(-8,9,2):
            for b in range(-9,10,2):
                if f.eval(Rational(b)-Rational(a,t)) == 0:
                    affine.append([a,b])
        small=[]
        if t <= 32:
            for P in range(1,16,2):
                val=int(f.eval(P))
                fs=factors(abs(val)) if abs(val)>1 else {}
                eligible=[ell for ell in fs if ell % t == t-1]
                for ell in eligible:
                    p=-pow(t,-1,ell) % ell
                    assert exact(t,P,p,ell)
                    assert recurrence(t,P,p,ell)==0
                small.append(dict(P=P,value=val,factors=fs,eligible=eligible))
        rows.append(dict(t=t,denominator=den,polynomial=str(f.as_expr()),
                         rational_roots=[str(x) for x in roots],affine=affine,small=small))
    # All shift offsets, not a Monte Carlo test, for an actual target (193,8,103).
    p,t,ell,H=193,8,103,32
    good=[a for a in range(ell) if exact(t,a,p,ell)]
    assert len(good)==int(totient(t))
    counts=[sum((2*j+1+off)%ell in good for j in range(H)) for off in range(ell)]
    assert sum(counts)==H*len(good)
    assert all((ell-a)%ell in good for a in good)
    hist={str(k):counts.count(k) for k in sorted(set(counts))}
    # Exact joint trace independence after restricting to valid integral traces.
    admissible=[P for P in range(210) if P % 2 and P % 5]
    counts2=[sum(exact(4,P,5,q) for q in [3,7]) for P in admissible]
    assert len(admissible)==84
    assert [counts2.count(i) for i in range(3)]==[20,48,16]
    joint=dict(p=5,pairs=[[4,3],[4,7]],modulus=210,admissible=84,
               histogram=[20,48,16],union_density='16/21',both_density='4/21')
    # Independent full-range certificate enumeration via h | p+u, not tp+1.
    summary=json.loads((OUT/'summary.json').read_text())
    full=[]
    for row in summary['selected']:
        n=row['p']
        witnesses=[]
        for u in range(1,(n+1)//3+1):
            for hh in divisors(n+u):
                h=int(hh)
                if (h+1) % (4*u):
                    continue
                C=(h+1)//(4*u)
                B=(n+u)//h
                assert 4*C*u*B-u-B==n
                witnesses.append([4*C,u,B,h,4*C*B-1])
        levels={w[0] for w in witnesses}
        from sympy import isprime
        primelevels={w[0] for w in witnesses if isprime(w[3])}
        assert len(levels)==row['divisor_levels']
        assert len(primelevels)==row['prime_levels']
        full.append(dict(p=n,witnesses=witnesses))
    # Independently certify every failure of the reverse prime-support sieve.
    # h=p+u is handled via u | p+1. A proper prime factor h of p+u is
    # <=(p+u)/2, so h>=4u-1 implies u<=(p+2)/7. SPF makes this linear
    # in a few million small integers rather than repeated general factoring.
    from array import array
    support=json.loads((OUT/'full_support.json').read_text())
    failures=support['all']['failures']
    bound=max(failures)*4//3+2
    spf=array('I',range(bound+1))
    from math import isqrt
    for q in range(2,isqrt(bound)+1):
        if spf[q]==q:
            for k in range(q*q,bound+1,q):
                if spf[k]==k:
                    spf[k]=q
    trials=0
    for n in failures:
        for u0 in divisors(n+1):
            u=int(u0)
            if (n+1)//u % 4 == 3:
                assert not isprime(n+u)
        for u in range(1,(n+2)//7+1):
            trials+=1
            v=n+u
            while v>1:
                q=spf[v]
                assert (q+1) % (4*u) != 0
                while v % q == 0:
                    v//=q
    support_check=dict(failures_checked=len(failures),proper_factor_trials=trials,
                       method='SPF factors of p+u plus prime h=p+u divisor test')
    data=dict(polynomials=rows,joint_toy=joint,independent_full=full,
              support_check=support_check,toy=dict(p=p,t=t,ell=ell,H=H,good=good,
          shift_histogram=hist,mean=Rational(sum(counts),ell).__str__(),
          actual=counts[0],any_fraction=f'{sum(v>0 for v in counts)}/{ell}'))
    (OUT/'algebra.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data['toy'],indent=2))
    print('32 cyclotomic specializations, 2880 affine specializations, all assertions passed')

if __name__=='__main__':
    main()
