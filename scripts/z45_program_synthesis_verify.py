"""Independent verification of emitted witnesses and frozen-policy extrapolation.
Uses trial-pair divisors (not search engine's prime-power generator), and a direct
five-slot predicate, plus exact rational verification of every saved certificate.
Run under a memory limit and timeout as documented in the memo.
"""
import csv
import json
import math
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path
from sympy import primerange, isprime

OUT = Path('data/z45_program_synthesis')


def ds_trial(n):
    low, high = [], []
    for d in range(1, math.isqrt(n)+1):
        if n % d == 0:
            low.append(d)
            if d*d != n:
                high.append(n//d)
    return low + high[::-1]


def is_hit(n, u, v, k=4):
    if not u or not v or (n+u+v) % (u*v):
        return False
    t = (n+u+v)//(u*v)
    return any(a % k == 0 for a in (t,u,v,t*u-1,t*v-1))


def frozen(p, maxcost=None):
    if maxcost is None:
        maxcost = math.ceil(8*math.log(p)**2)
    cost = 0
    for u in (4,8,12,16):
        cost += 1
        for v in ds_trial(p+u):
            cost += 1
            if is_hit(p,u,v):
                return cost,u,v,'prefix'
            if cost >= maxcost:
                return None
    for v in range(2,maxcost+2):
        cost += 1
        u = (-p) % v
        if is_hit(p,u,v):
            return cost,v,u,'parent'
        if cost >= maxcost:
            return None


def main():
    start = time.process_time()
    rows = list(csv.DictReader((OUT/'certificates.csv').open()))
    expected = set(p for p in primerange(2,1000001) if p % 24 == 1) | {5101441}
    assert {int(row['p']) for row in rows} == expected
    stage = Counter()
    for row in rows:
        p,c,u,v,x,y,z = map(int, row.values())
        assert min(x,y,z) > 0
        assert sum((Fraction(1,a) for a in (x,y,z)), Fraction()) == Fraction(4,p)
        assert is_hit(p,u,v)
        got = frozen(p)
        assert got[:3] == (c,u,v), (p,got,row)
        stage[got[3]] += 1
    print('independent verified',len(rows),'certificates and frozen-policy costs',flush=True)
    fails=[]
    ratios=[]
    maxcase=None
    maxratio=None
    n=0
    total=0
    parent_total=0
    parent_max=None
    parent_fail=[]
    extstage=Counter()
    # This range was not used in synthesis or model selection.
    for p in primerange(1000001,10000001):
        if p % 24 != 1:
            continue
        n += 1
        parent_cost = None
        for v in range(2, math.ceil(8*math.log(p)**2)+2):
            if is_hit(p, (-p) % v, v):
                parent_cost = v-1
                break
        if parent_cost is None:
            parent_fail.append(p)
        else:
            parent_total += parent_cost
            ratio = parent_cost/math.log(p)**2
            if parent_max is None or ratio > parent_max[1]:
                parent_max = [p,ratio,parent_cost]
        got=frozen(p)
        if not got:
            fails.append(p)
            continue
        c,u,v,s=got
        extstage[s] += 1
        total += c
        if maxcase is None or c > maxcase[1]:
            maxcase=[p,c,u,v]
        r=c/math.log(p)**2
        if maxratio is None or r > maxratio[1]:
            maxratio=[p,r,c,u,v]
    # Near-square and square-mimicking adversaries, deterministic exact primality.
    adversaries=set()
    for m in range(100000,100400):
        for gap in (-24,-8,-3,1,8,24):
            p=m*m+gap
            if p % 24 == 1 and isprime(p):
                adversaries.add(p)
    for modulus in (840, 27720, 360360):
        for a in range(10000,10200):
            p=modulus*a+1
            if isprime(p):
                adversaries.add(p)
    # Trial factoring is deliberately bounded: these inputs have sqrt(p)<200000.
    advfail=[]
    advmax=None
    for p in sorted(adversaries):
        got=frozen(p)
        if not got:
            advfail.append(p)
        elif advmax is None or got[0]/math.log(p)**2 > advmax[1]:
            advmax=[p,got[0]/math.log(p)**2,list(got)]
    shadow_toys=[]
    for h in (4,8,12,16,20,24,28,32):
        modulus=math.lcm(24,*range(1,h+1))
        for a in range(1,10001):
            p=1+a*modulus
            assert p < 2**64
            if isprime(p):
                break
        else:
            raise AssertionError('toy prime search cap reached')
        assert not any(is_hit(p,(-p)%v,v) for v in range(2,h+1))
        first=None
        for v in range(h+1, math.ceil(8*math.log(p)**2)+2):
            if is_hit(p,(-p)%v,v):
                first=v
                break
        shadow_toys.append({'H':h,'p':p,'first_parent_vertex':first})
    r={'verified_rows':len(rows),'original_stages':dict(stage),'shadow_toys':shadow_toys,
       'extension':{'range':'1000000<p<=10000000, p=1 mod24','n':n,'failures':fails,
                    'max_cost_case':maxcase,'max_ratio_case':maxratio,
                    'mean_cost':total/(n-len(fails)),'stages':dict(extstage),
                    'parent_baseline':{'failures':parent_fail,'max_ratio_case':parent_max,
                                       'mean_cost':parent_total/(n-len(parent_fail))}},
       'adversaries':{'n':len(adversaries),'failures':advfail,'max_ratio_case':advmax,
                      'primes':sorted(adversaries)},
       'cpu_seconds':time.process_time()-start}
    (OUT/'verification.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k != 'adversaries'},indent=2))
    print('adversaries',len(adversaries),'failures',advfail,'maxratio',advmax)


if __name__ == '__main__':
    main()
