"""Exact finite controls for the two gap charts and unique-list selection."""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, gcd, prod


def verifies(n, den):
    assert min(den) > 0 and sum((F(1, a) for a in den), F(0)) == F(4, n)


def old_chart():
    ct = 0
    for u,v,w in product(range(1,8), repeat=3):
        f = 4*u*v*w-1
        for mult in (3, 11):
            n = (-u*pow(v,-1,f)) % f + mult*f
            s, rem = divmod(n*v+u, f)
            assert not rem
            x = s*u*w
            verifies(n, (x, n*s*v*w, n*u*v*w))
            assert f*(4*x-n) == n+4*u*u*w
            ct += 1
    print('old multiplier: exact denominators and gap', ct)


def new_chart():
    ct = 0
    for a,b in product(range(1,40),repeat=2):
        if gcd(a,b)>1: continue
        for e in range(3, a+b+1, 4):
            if (a+b)%e: continue
            c = (a+b)//e
            for d in (1,3,10):
                n = 4*a*b*d-e
                if n<=e: continue
                x = a*b*d
                den = (x,n*b*c*d,n*a*c*d)
                verifies(n,den)
                assert x == min(den) and 4*x-n == e
                ct += 1
    print('reciprocal: exact denominators, minimum and gap',ct)


def selected_lists():
    # Compare the signed-vector unique match against a separate direct
    # divisor-pair implementation, then reconstruct the two fractions.
    hits = accepted = ambiguous = 0
    for e in (79,83,103):
        labels = [(u,v) for u in (3,5,7) for v in (1,3,5) if v<u and gcd(u,v)==1]
        for j in (1,2,3):
            for rs in combinations((107,109,113,127,131,137,139,149), j):
                matches = []
                for vec in product((-1,0,1),repeat=j):
                    if not any(vec): continue
                    A = prod(r for r,k in zip(rs,vec) if k==1)
                    B = prod(r for r,k in zip(rs,vec) if k==-1)
                    matches.extend((u,v,A,B) for u,v in labels if (u*A+v*B)%e==0)
                b = prod(rs)
                ds = [prod(sub) for k in range(j+1) for sub in combinations(rs,k)]
                rhs = [(u,v,A,B) for u,v in labels for A,B in product(ds,repeat=2)
                       if A!=B and gcd(A,B)==1 and (u*A+v*B)%e==0]
                assert sorted(matches)==sorted(rhs)
                hits += bool(matches); ambiguous += len(matches)>1
                if len(matches)!=1: continue
                u,v,A,B = matches[0]
                m = u*v*b; n = 4*m-e; A *= u; B *= v
                assert m%(A*B)==0 and (A+B)%e==0
                den = (m,n*(m//A)*((A+B)//e), n*(m//B)*((A+B)//e))
                verifies(n,den)
                assert min(den)==m and 4*m-n==e
                accepted += 1
    assert hits>accepted>0 and ambiguous>0
    print('unique-list controls: any match, unique, ambiguous:',hits,accepted,ambiguous)


def seed_grid():
    # Bound^2 < e, including non-squarefree e and non-squarefree seed labels.
    bound = 11
    windows = labels_checked = pins_checked = repaired_hits = power_cases = 0
    for e in range(123, 200, 4):
        labels = [(u,v) for u in range(3,bound+1,2) for v in range(1,u,2)
                  if gcd(u,v)==gcd(u*v,e)==1]
        targets = {(-v*pow(u,-1,e)) % e for u,v in labels}
        inverses = {pow(t,-1,e) for t in targets}
        assert len(targets | inverses) == 2*len(labels)
        windows += 1; labels_checked += len(labels)
        for u,v in labels:
            mod = 4*u*v
            factors = []
            for r in (3,5,7,11):
                power, rem = 1, u*v
                while rem % r == 0:
                    power *= r; rem //= r
                if power > 1:
                    factors.append((r,power))
                    power_cases += power > r
            assert prod(power for _,power in factors)==u*v
            for n in range(1,mod,4):
                # Construct the repaired pin by CRT projectors, independently
                # compare with the disjoint preimages of the activation class.
                z = n
                choices = 1
                for r,power in factors:
                    if n % r == 0:
                        cofactor = mod//power
                        z += (1-n)*cofactor*pow(cofactor,-1,power)
                    choices *= int((n+e) % power == 0) + int(n%r == 0 and (1+e)%power == 0)
                active = (z+e) % mod == 0
                assert choices == int(active)
                if gcd(n,u*v)==1: assert active == ((n+e)%mod==0)
                pins_checked += 1
                repaired_hits += active and (n+e)%mod != 0
    assert repaired_hits and power_cases
    print('seed grid: windows, labels, pins, repair-only hits:',
          windows, labels_checked, pins_checked, repaired_hits)


def envelopes():
    ct = 0
    for s in (2,4,6):
        for ds in product(range(8),repeat=3):
            us = [sum((-1)**i*comb(d,i) for i in range(min(s,d)+1)) for d in ds]
            gap = sum(comb(d,s)*prod(us[:b]+us[b+1:]) for b,d in enumerate(ds))
            assert prod(us)-gap <= int(not any(ds)) <= prod(us)
            ct += 1
    print('relative block sieve pointwise envelopes:',ct)


if __name__ == '__main__':
    print('Engine: scripts/z82_b34_gaps.py | deterministic integer and Fraction checks')
    old_chart(); new_chart(); selected_lists(); envelopes(); seed_grid()
