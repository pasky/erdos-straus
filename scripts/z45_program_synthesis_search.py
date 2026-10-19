"""Bounded enumerative synthesis of growing ES word-search schedules.
No learned lookup tables; training split and grammar are fixed before the run.
Run: ulimit -v 2000000; timeout 900 uv run python scripts/z45_program_synthesis_search.py
Cost counts a root/candidate probe and EVERY divisor inspected, not factorization time.
"""
import csv
import itertools
import json
import math
import time
from array import array
from collections import deque
from pathlib import Path

OUT = Path('data/z45_program_synthesis')
HARD = [409, 577, 3361, 5569, 9601, 23929, 193, 2521, 66529, 5101441]
ATOMS = ['asc', 'desc', 'nr', 'nrdesc', 'four', 'three', 'cfD', 'cfP', 'cfQ',
         'sqrt', 'quot', 'parent', 'parentnr', 'bfsnr']
PREFIXES = [1, 2, 4, 8, 16]


def sieve(n):
    a = bytearray(b'\1') * (n + 1)
    a[:2] = b'\0\0'
    for k in range(2, math.isqrt(n) + 1):
        if a[k]:
            a[k*k::k] = b'\0' * ((n-k*k)//k+1)
    return a


PRIMES = []


def divisors(n):
    ds = [1]
    for q in PRIMES:
        if q*q > n:
            break
        if n % q == 0:
            old = ds[:]
            power = 1
            while n % q == 0:
                n //= q
                power *= q
                ds.extend(d*power for d in old)
    if n > 1:
        ds += [d*n for d in ds]
    return sorted(ds)


def cert(n, u, v, k=4):
    if min(u, v) < 1 or (n+u+v) % (u*v):
        return None
    t = (n+u+v)//(u*v)
    if t % k == 0:
        d = t//k
        return (u*v*d, n*v*d, n*u*d)
    for a, b in ((u, v), (v, u)):
        if a % k == 0:
            d, h = a//k, t*b-1
            return (h*d, h*t*d*n, t*d*n)
        if (t*a-1) % k == 0:
            d, h = (t*a-1)//k, t*b-1
            return (h*d*n, b*d, h*b*d)
    return None


def cf_values(n, limit):
    a0 = math.isqrt(n)
    if a0*a0 == n:
        return []
    m, d, a = 0, 1, a0
    h0, h1, k0, k1 = 0, 1, 1, 0
    out = []
    for _ in range(limit):
        h0, h1 = h1, a*h1+h0
        k0, k1 = k1, a*k1+k0
        m = d*a-m
        d = (n-m*m)//d
        a = (a0+m)//d
        out.append((d, h1 % n, k1 % n))
        if a == 2*a0:
            break
    return out


def run_atom(n, name, budget, numerator=4):
    """Returns hit cost and prefix costs after k raw root proposals (not emitted hits).
    Root proposals rejected by the nonresidue filter also cost one.
    Factoring and generating all divisors is additional work, explicitly not oracle-free.
    """
    c = 0
    prefix = {}
    witness = None
    root_calls = 0
    fact_calls = 0
    inspected = 0
    seen = set()
    cf = cf_values(n, budget) if name.startswith('cf') else []
    queue = deque()
    nextroot = 2
    maxroot = n+2
    for i in range(1, budget+1):
        if c >= budget:
            break
        is_seed = False
        if name.startswith('cf'):
            if i > len(cf):
                break
            u = cf[i-1][{'cfD': 0, 'cfP': 1, 'cfQ': 2}[name]]
        elif name == 'four':
            u = 4*i
        elif name == 'three':
            u = 4*i-1
        elif name == 'sqrt':
            u = math.isqrt(n) + ((i//2) if i % 2 == 0 else -(i//2))
        elif name == 'quot':
            u = n//(i+1)
        elif name == 'bfsnr':
            if queue:
                u = queue.popleft()
            else:
                is_seed = True
                u = nextroot
                nextroot += 1
        else:
            u = i+1 if name.startswith('parent') else i
        c += 1
        root_calls += 1
        if not (1 <= u <= maxroot) or u in seen:
            prefix[i] = c
            continue
        seen.add(u)
        if name in ('nr', 'nrdesc', 'parentnr') or (name == 'bfsnr' and is_seed):
            if pow(u, (n-1)//2, n) != n-1:
                prefix[i] = c
                continue
        if name.startswith('parent'):
            v = (-n) % u
            xyz = cert(n, u, v, numerator) if v else None
            if xyz:
                witness = [u, v, *xyz]
        else:
            fact_calls += 1
            ds = divisors(n+u)
            if name in ('desc', 'nrdesc'):
                ds.reverse()
            for v in ds:
                if c >= budget:
                    break
                c += 1
                inspected += 1
                if (n+u+v) % (u*v) == 0:
                    if name == 'bfsnr' and v not in seen:
                        queue.append(v)
                    xyz = cert(n, u, v, numerator)
                    if xyz:
                        witness = [u, v, *xyz]
                        break
        prefix[i] = c
        if witness:
            break
    # Prefix schedules may exhaust a CF atom early. Continuing means immediate fallback.
    return {'cost': c, 'hit': witness, 'prefix': [prefix.get(k, c) for k in PREFIXES],
            'roots': root_calls, 'factors': fact_calls, 'divisors': inspected}


def evaluate(rec, program):
    a, ki, b = program
    ra = rec[a]
    if ki < 0:
        return ra['cost'], ra['hit']
    spent = ra['prefix'][ki]
    if ra['hit'] and ra['cost'] <= spent:
        return ra['cost'], ra['hit']
    rb = rec[b]
    return spent + rb['cost'], rb['hit']


def main():
    global PRIMES
    start = time.process_time()
    OUT.mkdir(parents=True, exist_ok=True)
    bits = sieve(1000000)
    ps = [p for p in range(25, 1000001, 24) if bits[p]]
    PRIMES = [q for q in range(2, 4001) if bits[q]]
    allps = sorted(set(ps+HARD))
    records = {}
    for j, p in enumerate(allps):
        budget = math.ceil(8*math.log(p)**2)
        records[p] = {a: run_atom(p, a, budget) for a in ATOMS}
        if j % 1000 == 0:
            print('trace', j, p, round(time.process_time()-start, 2), flush=True)
    train = [p for p in allps if p <= 200000 or p in HARD]
    holdout = [p for p in allps if p not in set(train)]
    programs = [(a, -1, a) for a in ATOMS]
    programs += [(a, k, b) for a, b in itertools.permutations(ATOMS, 2)
                 for k in range(len(PREFIXES))]

    def summary(program, sample):
        fails = []
        costs = []
        ratios = []
        for p in sample:
            cost, hit = evaluate(records[p], program)
            if not hit or cost > math.ceil(8*math.log(p)**2):
                fails.append(p)
            costs.append(cost)
            ratios.append(cost/math.log(p)**2)
        worst = max(range(len(sample)), key=lambda i: ratios[i])
        return {'n': len(sample), 'failures': fails, 'max_cost': max(costs),
                'mean_cost': sum(costs)/len(costs), 'max_ratio': ratios[worst],
                'ratio_record': sample[worst]}

    ranking = []
    for prog in programs:
        stat = summary(prog, train)
        hardstat = summary(prog, HARD)
        key = (len(stat['failures']), stat['max_ratio'], hardstat['mean_cost'], stat['mean_cost'])
        ranking.append((key, prog, stat))
    ranking.sort()
    best = ranking[0][1]
    print('best', best, ranking[0], flush=True)
    report = {'grammar': ATOMS, 'prefixes': PREFIXES, 'programs': len(programs),
              'budget': 'ceil(8*(ln p)^2)', 'training': 'p<=200000 plus named HARD fixtures',
              'best': best, 'train': summary(best, train), 'holdout': summary(best, holdout),
              'all': summary(best, allps), 'hard': {},
              'top20': [{'program': prog, 'train': stat} for _, prog, stat in ranking[:20]],
              'atoms': {a: summary((a,-1,a), allps) for a in ATOMS}}
    for p in HARD:
        cost, hit = evaluate(records[p], best)
        report['hard'][p] = {'cost': cost, 'ratio': cost/math.log(p)**2, 'witness': hit}
    report['mordell'] = summary(best, [p for p in ps if p % 840 in (1,121,169,289,361,529)])
    near = [p for p in ps if min(p-math.isqrt(p)**2, (math.isqrt(p)+1)**2-p) <= 24]
    report['near_square_abs_gap_le24'] = summary(best, near)
    report['dyadic'] = {str(lo): summary(best, [p for p in ps if lo < p <= hi])
                        for lo, hi in [(0,10000),(10000,100000),(100000,1000000)]}
    with (OUT/'certificates.csv').open('w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['p','cost','u','v','x','y','z'])
        for p in allps:
            cost, hit = evaluate(records[p], best)
            if hit:
                writer.writerow([p,cost,*hit])
    # Complete controls are independently enumerated by the unique-parent rule,
    # not just tested up to the learned schedule's search cutoff.
    controls = {}
    for n, k in [(131,8),(241,8),(11,8),(17,8)]:
        count = 0
        for v in range(2,n+3):
            u = (-n) % v
            if u and cert(n,u,v,k):
                count += 1
        controls[f'{k}/{n}'] = count
    # T1 tested against actual divisibility certificates; no Euler-symbol prime
    # test is used to manufacture failure on composite inputs.
    square_hits = 0
    for m in range(3, 200, 2):
        n = m*m
        for v in range(2,n+3):
            u = (-n) % v
            if u and cert(n,u,v):
                square_hits += 1
    controls['odd_squares_9_to_199_squared_hits'] = square_hits
    report['controls'] = controls
    report['cpu_seconds'] = time.process_time()-start
    (OUT/'report.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: report[k] for k in ['best','all','holdout','mordell','controls','cpu_seconds']}, indent=2))


if __name__ == '__main__':
    main()
