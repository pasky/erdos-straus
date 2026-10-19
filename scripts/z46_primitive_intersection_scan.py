"""Targeted Lucas intersections; O(limit) sieve storage plus bounded rows.
Run: ulimit -v 2000000; timeout 300 uv run python scripts/z46_primitive_intersection_scan.py
Existing z45 script already tests the Cayley census and numerator controls; this
extends the census, tests exact-index resultants, and adds unit/shift controls.
"""
import argparse
import gzip
import json
from functools import lru_cache
from math import isqrt, prod
from pathlib import Path
from random import Random
from sympy import factorint, isprime, primerange

OUT = Path('data/z46_primitive_intersection')
HARD = [193, 409, 577, 2521, 3361, 5569, 9601, 66529]
MORDELL = {1, 121, 169, 289, 361, 529}

@lru_cache(maxsize=4096)
def tfactors(t):
    return tuple(int(q) for q in factorint(t))

def phi(t):
    a = t
    for q in tfactors(t):
        a = a // q * (q-1)
    return a

def factors(n):
    f = {int(q): int(e) for q, e in factorint(n).items()}
    assert prod(q**e for q, e in f.items()) == n
    assert all(isprime(q) for q in f)
    return f

def mul(x, y, D, ell):
    return ((x[0]*y[0]+D*x[1]*y[1]) % ell,
            (x[0]*y[1]+x[1]*y[0]) % ell)

def power(x, k, D, ell):
    ans = (1, 0)
    while k:
        if k & 1:
            ans = mul(ans, x, D, ell)
        x = mul(x, x, D, ell)
        k >>= 1
    return ans

def exact(t, P, D, ell):
    P %= ell
    D %= ell
    den = (P*P-D) % ell
    if not den or not D:
        return False
    inv = pow(den, -1, ell)
    z = ((P*P+D)*inv % ell, 2*P*inv % ell)
    return power(z, t, D, ell) == (1, 0) and all(
        power(z, t//q, D, ell) != (1, 0) for q in tfactors(t))

def recurrence(t, P, D, ell):
    Q = (P*P-D)*pow(4, -1, ell) % ell
    a, b = 0, 1
    for _ in range(t):
        a, b = b, (P*b-Q*a) % ell
    return a

def divisor_hit(fs, t):
    ds = [1]
    for q, e in fs.items():
        old = ds[:]
        v = 1
        for _ in range(e):
            v *= q
            ds.extend(d*v for d in old)
    return any(d % t == t-1 for d in ds)

def pell(n):
    """First CF convergent of sqrt(n) with norm +/-1; exact integer arithmetic."""
    a0 = isqrt(n)
    m, d, a = 0, 1, a0
    hm2, hm1, km2, km1 = 0, 1, 1, 0
    for _ in range(10000):
        x, y = a*hm1+hm2, a*km1+km2
        norm = x*x-n*y*y
        if abs(norm) == 1:
            return x, y, norm
        hm2, hm1, km2, km1 = hm1, x, km1, y
        m = d*a-m
        d = (n-m*m)//d
        a = (a0+m)//d
    raise RuntimeError('Pell iteration bound exceeded')

def scan(p, T, P0, rng, detail=False):
    r = dict(p=p, T=min(T, p+2), divisor_levels=0 if detail else None, prime_levels=0,
             prime_pairs=0, hits=0, trace1_levels=0, trace3_levels=0,
             trace15_levels=0, trace63_levels=0, bhv_levels=0,
             expectation=0., independent_any_expectation=0.,
             shifted_hits=[0]*8, unit_levels=0, unit_square_levels=0,
             unit_eligible=0, unit_square_eligible=0)
    x, y, norm = pell(p)
    r['pell_norm'] = norm
    r['pell_bits'] = x.bit_length()
    examples = []
    for t in range(4, min(T, p+2)+1, 4):
        N = t*p+1
        fs = factors(N)
        if detail:
            r['divisor_levels'] += divisor_hit(fs, t)
        ps = [ell for ell in fs if ell % t == t-1]
        if not ps:
            continue
        r['prime_levels'] += 1
        r['prime_pairs'] += len(ps)
        levelhits, unit, unit2 = [], False, False
        for ell in ps:
            assert pow(p, (ell-1)//2, ell) == ell-1
            # p modulo ell is determined by t: no hidden p dependence.
            assert p % ell == -pow(t, -1, ell) % ell
            rho = phi(t)/ell
            traces = [P for P in range(1, P0+1, 2) if P % p]
            r['expectation'] += len(traces)*rho
            r['independent_any_expectation'] += 1-(1-rho)**len(traces)
            good = [P for P in traces if exact(t, P, p, ell)]
            r['hits'] += len(good)
            levelhits.extend(good)
            if good and len(examples) < 4:
                examples.append([t, ell, good[0]])
            # Uniform translated odd trace list: exact marginal rho, not
            # independent entries. Each replicate chooses one offset per pair.
            for j in range(8):
                off = rng.randrange(ell)
                r['shifted_hits'][j] += sum(exact(t, P+off, p, ell) for P in traces)
            if y % ell:
                a = x*pow(y, -1, ell) % ell  # normalized trace X/Y
                z = exact(t, a, p, ell)
                unit |= z
                k = (ell+1)//t
                eligible = (k % 2 == 0) if norm == 1 else (k % 2 == 1)
                r['unit_eligible'] += eligible
                assert not z or eligible
            x2, y2 = x*x+p*y*y, 2*x*y
            if y2 % ell:
                z2 = exact(t, x2*pow(y2, -1, ell), p, ell)
                unit2 |= z2
                r['unit_square_eligible'] += ((ell+1)//t % 2 == 0)
                assert not z2 or (ell+1)//t % 2 == 0
        r['trace1_levels'] += 1 in levelhits
        r['trace3_levels'] += 3 in levelhits
        r['trace15_levels'] += any(P <= 15 for P in levelhits)
        r['trace63_levels'] += bool(levelhits)
        r['bhv_levels'] += bool(levelhits) and t > 30
        r['unit_levels'] += unit
        r['unit_square_levels'] += unit2
    r['examples'] = examples
    return r

def aggregate(rows):
    keys = ['prime_levels','prime_pairs','hits','expectation','trace1_levels',
            'trace3_levels','trace15_levels','trace63_levels','bhv_levels',
            'unit_levels','unit_square_levels','unit_eligible','unit_square_eligible']
    return {'n':len(rows), 'sums':{k:sum(r[k] for r in rows) for k in keys},
            'primes_hit':{k:sum(r[k]>0 for r in rows) for k in keys if k.endswith('levels')},
            'shifted_hits':[sum(r['shifted_hits'][j] for r in rows) for j in range(8)],
            'no_prime':[r['p'] for r in rows if not r['prime_levels']],
            'no_short_trace':[r['p'] for r in rows if not r['trace63_levels']]}

def full_prime_support(limit):
    # Reverse sieve: every target prime is <= (4p+1)/3. Enumerate all
    # t | ell+1 with 4 | t, then mark p=-1/t (mod ell), p=1 (mod4).
    from array import array
    from sympy import divisors
    counts = array('I', [0])*limit
    for ell0 in primerange(3, (4*(limit-1)+1)//3+1):
        ell=int(ell0)
        if ell % 4 != 3:
            continue
        for d in divisors((ell+1)//4):
            t=4*int(d)
            r=-pow(t,-1,ell) % ell
            start=r+ell*((1-r)*pow(ell,-1,4) % 4)
            for p in range(start,limit,4*ell):
                if p >= 5:
                    counts[p] += 1
    ps=[int(p) for p in primerange(5,limit) if p % 4 == 1]
    hard=[p for p in ps if p % 840 in MORDELL]
    def stats(pool):
        return dict(n=len(pool),pairs=sum(counts[p] for p in pool),
                    failures=[p for p in pool if not counts[p]])
    blocks=[]
    for lo,hi in [(5,10000),(10000,100000),(100000,1000000)]:
        pool=[p for p in ps if lo <= p < min(hi,limit)]
        if pool:
            blocks.append(dict(lo=lo,hi=min(hi,limit),**stats(pool)))
    return dict(all=stats(ps),mordell=stats(hard),blocks=blocks),counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit',type=int,default=1000000)
    ap.add_argument('--T',type=int,default=256)
    ap.add_argument('--P0',type=int,default=63)
    ap.add_argument('--support-only',action='store_true')
    args = ap.parse_args()
    if args.support_only:
        data,counts=full_prime_support(args.limit)
        (OUT/'full_support.json').write_text(json.dumps(data,indent=2)+'\n')
        s=json.loads((OUT/'summary.json').read_text())
        for r in s['selected']:
            if r['p'] < args.limit:
                assert counts[r['p']]==r['prime_pairs']
        with gzip.open(OUT/'rows.jsonl.gz','rt') as f:
            for line in f:
                r=json.loads(line)
                assert counts[r['p']] >= r['prime_pairs']
        print({k:dict(n=v['n'],pairs=v['pairs'],failures=len(v['failures']))
               for k,v in data.items() if k != 'blocks'})
        return
    assert args.P0 == 63
    OUT.mkdir(exist_ok=True)
    rng = Random(460513)
    primes = [int(p) for p in primerange(5,args.limit) if p % 840 in MORDELL]
    rows = []
    for i,p in enumerate(primes):
        rows.append(scan(p,args.T,args.P0,rng))
        if (i+1)%500 == 0:
            print('completed',i+1,flush=True)
    selected = [scan(p,p+2,args.P0,rng,True) for p in HARD]
    pool = [int(p) for p in primerange(5,args.limit)
            if p % 4 == 1 and p % 840 not in MORDELL]
    baseline = [scan(p,args.T,args.P0,rng) for p in pool[::max(1,len(pool)//256)][:256]]
    near = [r for r in rows if min(abs(r['p']-isqrt(r['p'])**2),
                                  abs(r['p']-(isqrt(r['p'])+1)**2)) <= 4]
    # Independent recurrence verification on every selected actual hit.
    for r in selected:
        for t,ell,P in r['examples']:
            assert recurrence(t,P,r['p'],ell) == 0
            assert all(recurrence(t//q,P,r['p'],ell) != 0 for q in tfactors(t))
    # Numerator-8 full finite range, including p=131 (not 1 mod4):
    # its finite-field dictionary still makes sense, with integral D=4p if needed.
    controls = []
    for M,n in [(8,131),(8,241)]+[(4,m*m) for m in range(3,32,2)]:
        hits=0
        inert=0
        for t in range(M,n+3,M):
            fs=factors(t*n+1)
            hits += divisor_hit(fs,t)
            inert += sum(pow(n,(ell-1)//2,ell)==ell-1 for ell in fs)
        assert hits == 0
        if M == 4:
            assert inert == 0
        controls.append(dict(M=M,n=n,hits=hits,inert_factor_incidence=inert))
    summary = dict(parameters=vars(args),mordell=aggregate(rows),near_squares=aggregate(near),
                   baseline=aggregate(baseline),selected=selected,controls=controls)
    (OUT/'baseline.json').write_text(json.dumps(baseline,indent=2)+'\n')
    with gzip.open(OUT/'rows.jsonl.gz','wt') as f:
        for r in rows:
            f.write(json.dumps(r)+'\n')
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    support,counts=full_prime_support(args.limit)
    for r in selected:
        if r['p'] < args.limit:
            assert counts[r['p']]==r['prime_pairs']
    assert all(counts[r['p']] >= r['prime_pairs'] for r in rows)
    (OUT/'full_support.json').write_text(json.dumps(support,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k != 'selected'},indent=2))

if __name__ == '__main__':
    main()
