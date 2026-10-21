#!/usr/bin/env python3
"""Bounded, exact norm-coordinate witness grammar; see NONET_STEP.md.
No target solution enumeration in the search. --audit uses an independent
least-two-denominator enumeration only to check small source fibres/controls.
"""
import argparse
from bisect import bisect_left, bisect_right
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement
from math import gcd, isqrt, lcm
from pathlib import Path
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_AS, (1_500_000_000, 1_500_000_000))
resource.setrlimit(resource.RLIMIT_CPU, (5000, 5000))
HARD = [409, 577, 3361, 5569, 9601, 193, 2521]
MORDELL = {1, 121, 169, 289, 361, 529}


@lru_cache(maxsize=4096)
def factor(n):
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0)+1
            n //= d
        d = 3 if d == 2 else d+2
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out


@lru_cache(maxsize=1024)
def witnesses(k, n):
    out = []
    for x in range(n//k+1, 3*n//k+1):
        A, B = k*x-n, n*x
        g = gcd(A, B)
        A, B = A//g, B//g
        ds = [1]
        for p, e in factor(B).items():
            ds = [d*p**j for d in ds for j in range(2*e+1)]
        for d in ds:
            if d > B or (d+B) % A:
                continue
            e = B*B//d
            if (e+B) % A:
                continue
            y, z = (d+B)//A, (e+B)//A
            if x <= y <= z:
                out.append((x, y, z))
    return tuple(sorted(set(out)))


def brute(k, n):
    out = set()
    for x in range(n//k+1, 3*n//k+1):
        A, B = k*x-n, n*x
        for y in range(max(x, B//A+1), 2*B//A+1):
            den = A*y-B
            if B*y % den == 0:
                z = B*y//den
                if z >= y:
                    out.add((x, y, z))
    return out


def valid(k, n, w):
    x, y, z = w
    return min(w) > 0 and k*x*y*z == n*(x*y+x*z+y*z)


def representations(n):
    return [(isqrt(n-b*b), b) for b in range(1, isqrt(n//2)+1)
            if isqrt(n-b*b)**2 == n-b*b]


def primes(limit):
    sieve = bytearray(b'\x01')*(limit+1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p::p] = b'\x00'*((limit-p*p)//p+1)
    return [p for p in range(2, limit+1) if sieve[p]]


def pool(C, D, cap):
    """One operation between a coordinate atom and a denominator feature."""
    out = {c: 'C' for c in C if c <= cap}
    for d, expr in D.items():
        for c in C:
            vals = [(d*c, f'{expr}*{c}'),
                    (gcd(d, c), f'gcd({expr},{c})'),
                    (lcm(d, c), f'lcm({expr},{c})')]
            if d % c == 0:
                vals.append((d//c, f'{expr}/{c}'))
            if c % d == 0:
                vals.append((c//d, f'{c}/{expr}'))
            for v, label in vals:
                if 0 < v <= cap:
                    out.setdefault(v, label)
    return out


def features(w, split=False):
    D = {d: f'w{i}' for i, d in enumerate(w)}
    for i in range(3):
        for j in range(i, 3):
            u, v = w[i], w[j]
            g = gcd(u, v)
            for d, s in [(u*v, f'w{i}*w{j}'), (g, f'gcd(w{i},w{j})'),
                         (lcm(u,v), f'lcm(w{i},w{j})'),
                         (u//g, f'w{i}/gcd(w{i},w{j})'),
                         (v//g, f'w{j}/gcd(w{i},w{j})')]:
                D.setdefault(d, s)
    D.setdefault(gcd(*w), 'gcd(w)')
    D.setdefault(lcm(*w), 'lcm(w)')
    if split:
        for i, d in enumerate(w):
            D.setdefault(d+1, f'(w{i}+1)')
            D.setdefault(d*(d+1), f'w{i}*(w{i}+1)')
    return D


def held(k, n, P, counters):
    """Generate exactly those triples whose two least denominators lie in P."""
    vals = sorted(P)
    for x in vals[bisect_right(vals, n//k):bisect_right(vals, 3*n//k)]:
        A, B = k*x-n, n*x
        lo = max(x, B//A+1)
        hi = 2*B//A
        for y in vals[bisect_left(vals, lo):bisect_right(vals, hi)]:
            counters['held_pairs'] += 1
            den = A*y-B
            if B*y % den == 0:
                z = B*y//den
                assert z >= y
                yield (x, y, z), [P[x], P[y]]


def pair_repair(k, n, q, w, ratios, counters):
    for j in range(3):
        u = w[j]
        v, z = [w[i] for i in range(3) if i != j]
        for hnum, hden in ratios:
            counters['repair_trials'] += 1
            if (hnum*v) % hden or (hnum*z) % hden:
                continue
            den = k*hnum*q*u-n*hden*(k*u-q)
            num = n*hnum*q*u
            if den > 0 and num % den == 0:
                X = num//den
                yield tuple(sorted((X, hnum*v//hden, hnum*z//hden))), {
                    'omitted_index': j, 'h': [hnum, hden], 'replacement': X}


def ratio_fibre(k, n, r, s):
    """All positive triples (X,h*r,h*s), via the composite-valid identity.
    (k*X-n)*(k*h*r*s-n*(r+s)) = n*n*(r+s).
    Factor only n and r+s separately, never a large unfactored product.
    """
    fs = dict(factor(r+s))
    for p,e in factor(n).items():
        fs[p] = fs.get(p,0)+2*e
    ds = [1]
    for p,e in fs.items():
        ds = [d*p**j for d in ds for j in range(e+1)]
    N = n*n*(r+s)
    out = []
    for d in ds:
        if (d+n) % k:
            continue
        num = N//d+n*(r+s)
        if num % (k*r*s):
            continue
        X, h = (d+n)//k, num//(k*r*s)
        out.append((tuple(sorted((X,h*r,h*s))), {'ratio':[r,s], 'divisor':d,
                   'multiplier':h, 'replacement':X}))
    return out


def search(k, n, a, b):
    start = time.process_time()
    root = isqrt(n)
    square = root*root == n
    Q = sorted({a,b,a+b,a-b}-{1})
    C = sorted({1,2,k,a,b,a+b,a-b,a*a,b*b,a*b,2*a*b,n})
    cap = 10*n*n
    counters = Counter()
    results = {g: set() for g in ['baseline','repair','greedy','ratio','core','split']}
    examples = {}
    ratio_cache = {}
    source_coverage = Counter()
    source_counts = {q:len(witnesses(k,q)) for q in Q}

    def record(grammar, wout, q=None, win=None, details=None):
        assert valid(k,n,wout)
        results[grammar].add(wout)
        category = 'nonscaling' if not square or any(d % root for d in wout) else 'scaled'
        key = grammar+'_'+category
        examples.setdefault(key, {'q':q, 'input':win, 'output':wout, 'details':details})
        if gcd(n, *wout) == 1:
            examples.setdefault(grammar+'_primitive', {'q':q, 'input':win, 'output':wout, 'details':details})

    base = pool(C, {c:'C' for c in C}, cap)
    for out, detail in held(k,n,base,counters):
        record('baseline',out,details=detail)
    maxpool = len(base)
    for q in Q:
        R = sorted(set(C+[q,n+q,n-q]))
        ratios = sorted({(u//gcd(u,v), v//gcd(u,v)) for u in R for v in R})
        for w in witnesses(k,q):
            counters['source_witnesses'] += 1
            hit = {g:False for g in ['repair','greedy','ratio','core','split']}
            for i,j in combinations_with_replacement(range(3),2):
                if i == j:
                    continue
                v,z = w[i],w[j]
                g = gcd(v,z)
                r,s = v//g,z//g
                if (r,s) not in ratio_cache:
                    ratio_cache[r,s] = ratio_fibre(k,n,r,s)
                    counters['ratio_fibres'] += 1
                for out, detail in ratio_cache[r,s]:
                    hit['ratio'] = True
                    record('ratio',out,q,w,dict(detail, pair_indices=[i,j]))
                    if detail['divisor'] == k-(n % k):
                        hit['greedy'] = True
                        record('greedy',out,q,w,dict(detail, pair_indices=[i,j]))
            for out, detail in pair_repair(k,n,q,w,ratios,counters):
                hit['repair'] = True
                record('repair',out,q,w,detail)
            for grammar, split in [('core',False),('split',True)]:
                P = pool(C, features(w,split),cap)
                maxpool = max(maxpool,len(P))
                for out, detail in held(k,n,P,counters):
                    hit[grammar] = True
                    record(grammar,out,q,w,detail)
            for g, yes in hit.items():
                source_coverage[g] += yes
    assert results['repair'] <= results['ratio']
    assert results['greedy'] <= results['ratio']
    assert results['core'] <= results['split']
    counts = {g:{'solutions':len(v),
                 'nonscaling':sum(not square or any(d%root for d in w) for w in v),
                 'primitive_target':sum(gcd(n,*w)==1 for w in v),
                 'outside_baseline':len(v-results['baseline'])}
              for g,v in results.items()}
    for g in ['repair','greedy','ratio','core','split']:
        for wout in sorted(results[g]-results['baseline']):
            if not square or any(d%root for d in wout):
                # Replay below locates provenance when needed; never reverse-engineer source.
                examples[g+'_beyond_baseline'] = {'output':wout}
                break
    return {'k':k,'n':n,'a':a,'b':b,'square':square,'primitive':gcd(a,b)==1,
            'mordell':n%840 in MORDELL,'near_square_gap':n-isqrt(n)**2,
            'sources':source_counts,'counts':counts,'source_coverage':dict(source_coverage),
            'examples':examples,'operations':dict(counters),'maxpool':maxpool,
            'cpu_seconds':round(time.process_time()-start,4)}


def audit():
    for k in [4,8,10,12]:
        for n in range(2,81):
            assert set(witnesses(k,n)) == brute(k,n), (k,n)
    controls = {n:len(brute(8,n)) for n in [11,17,131,241]}
    assert all(v == 0 for v in controls.values())
    print(json.dumps({'source_audit_fibres':316,'numerator8':controls}))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode',choices=['fixtures','census','audit'],default='fixtures')
    ap.add_argument('--out',default='data/z47_nonet_step/fixtures.jsonl')
    args = ap.parse_args()
    if args.mode == 'audit':
        audit()
        return
    cases = set()
    ms = [5,13,17,25,29,37,65]
    if args.mode == 'census':
        ms = [m for m in range(3,201,2) if all(p%4==1 for p in factor(m))]
    for m in ms:
        for a,b in representations(m*m):
            if gcd(a,b)==1:
                cases.add((4,m*m,a,b))
    ps = HARD+[97,313,5209,233689]
    if args.mode == 'census':
        ps += [p for p in primes(100000) if p%840 in MORDELL or p<10000 and p%8==1]
    for p in ps:
        for a,b in representations(p):
            cases.add((4,p,a,b))
    for k,n in [(8,17),(8,241),(10,181),(12,1657)]:
        for a,b in representations(n):
            cases.add((k,n,a,b))
    path = Path(args.out)
    path.parent.mkdir(parents=True,exist_ok=True)
    start = time.process_time()
    with path.open('w') as f:
        for i,(k,n,a,b) in enumerate(sorted(cases)):
            row = search(k,n,a,b)
            f.write(json.dumps(row,sort_keys=True)+'\n')
            f.flush()
            print(i+1,len(cases),k,n,(a,b),{g:c['solutions'] for g,c in row['counts'].items()},
                  row['cpu_seconds'],flush=True)
    print('TOTAL_CPU',time.process_time()-start)

if __name__ == '__main__':
    main()
