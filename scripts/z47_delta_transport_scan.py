"""Exact radius-one profiles and explicitly scoped transport graphs.
Run: ulimit -v 2000000; timeout 300 uv run --with python-flint python ...
Streams one fibre at a time; O(tau(B^2)*omega(B)) temporary integers.
"""
import gzip
import json
from collections import Counter
from fractions import Fraction
from math import gcd
from pathlib import Path
from flint import fmpz

OUT = Path('data/z47_delta_transport')
OLD = Path('data/z46_overflow_delta')


def factor(n):
    return [(int(p), int(e)) for p, e in fmpz(n).factor()]


def divisors(fs):
    ds = [1]
    for p, e in fs:
        old = ds[:]
        for j in range(1, e + 1):
            ds.extend(d * p**j for d in old)
    return ds


def fibre(B, M):
    fs = factor(B)
    ds = divisors([(p, 2*e) for p,e in fs])
    hits = [d for d in ds if (d+B) % M == 0]
    if hits:
        return fs, hits[0], []
    ws = []
    for ell, b in fs:
        other = [(p,2*e) for p,e in fs if p != ell]
        for z in divisors(other):
            d = ell**(2*b+1)*z
            if (d+B) % M:
                continue
            g = gcd(B,d)
            u,v = d//g,B//g
            assert u % ell == 0 and v % ell != 0
            T = u*v//ell
            assert B % T == 0 and (B//T) % ell != 0
            a = (u+v)//M
            assert (u+v) % M == 0 and gcd(a,u*v) == 1
            ws.append([ell,b,d,u,v,a,B//T])
    return fs,None,ws


def target(n,k,r,U,V):
    if r <= 0 or (n+r) % k or gcd(n,r) != 1:
        return None
    K = (n+r)//k
    if K % (U*V) or (U+V) % r:
        return None
    a = (U+V)//r
    xyz = [K,n*(K//U)*a,n*(K//V)*a]
    assert sum((Fraction(1,z) for z in xyz),Fraction()) == Fraction(k,n)
    return xyz


def moves(n,k,m,K,w):
    ell,b,d,u,v,a,h = w
    T = u*v//ell
    r = (-n) % (k*T)
    edges = []
    if r and (u//ell+v) % r == 0:
        xyz = target(n,k,r,u//ell,v)
        if xyz:
            edges.append(['drop',r,xyz])
    # Repartition only the known product T; not a full all-window search.
    for U in divisors(factor(T)):
        V = T//U
        if U > V or gcd(U,V) != 1:
            continue
        if r and (U+V) % r == 0:
            xyz = target(n,k,r,U,V)
            if xyz:
                edges.append(['repartition',r,xyz])
                break
    # Integer-word folding. The 4/2 branch has k|u automatically.
    if k % ell == 0 and u % k == 0 and a == 1:
        t = k*h//ell
        r = v
        xyz = target(n,k,r,t*v-1,1)
        assert xyz is not None
        edges.append(['fold',r,xyz])
    return edges


def residual_solution(k,n):
    for x in range(n//k+1,3*n//k+1):
        g = gcd(k*x-n,n*x)
        a,b = (k*x-n)//g,n*x//g
        for d in divisors([(p,2*e) for p,e in factor(b)]):
            if (d+b) % a == 0:
                xyz = [x,(b+d)//a,(b+b*b//d)//a]
                assert sum((Fraction(1,z) for z in xyz),Fraction()) == Fraction(k,n)
                return xyz
    return None


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    old = json.loads((OLD/'scan.json').read_text())
    comps = [r[0] for r in old['composite_nonzero'] if r[1] == 1]
    ps = [n for n in range(25,10001,24) if fmpz(n).is_prime()]
    fixtures = sorted(set(r['n'] for r in old['fixtures']) | {2113,31121,3985})
    summary = {}
    output = gzip.open(OUT/'fibres.jsonl.gz','wt')
    def scan_group(name,cases,residual=False):
        c = Counter()
        over = Counter()
        examples = {}
        for k,n,limit in cases:
            c['inputs'] += 1
            for x in (range(n//k+1,3*n//k+1) if residual else range((-n)%k or k,limit+1,k)):
                if residual:
                    g = gcd(k*x-n,n*x)
                    M,B = (k*x-n)//g,n*x//g
                else:
                    M = x
                    if gcd(n,M) != 1:
                        continue
                    B = (n+M)//k
                fs,hit,ws = fibre(B,M)
                c['fibres'] += 1
                if hit is not None:
                    c['zero'] += 1
                    continue
                if not ws:
                    c['not_radius_one'] += 1
                    continue
                c['delta_one'] += 1
                c['witnesses'] += len(ws)
                have2 = any(w[0] == 2 for w in ws)
                c['has_two' if have2 else 'odd_only'] += 1
                c['has_a1'] += any(w[5] == 1 for w in ws)
                c['has_two_a1'] += any(w[0] == 2 and w[5] == 1 for w in ws)
                all_edges = []
                for i,w in enumerate(ws):
                    over[str(w[0])] += 1
                    c['b_even' if w[1]%2 == 0 else 'b_odd'] += 1
                    if not residual:
                        all_edges.extend([i]+e for e in moves(n,k,M,B,w))
                if not residual:
                    kinds = {e[1] for e in all_edges}
                    for kind in ['drop','repartition','fold']:
                        c[kind+'_windows'] += kind in kinds
                    c['edge_windows'] += bool(all_edges)
                    c['no_edge_windows'] += not all_edges
                key = ('two' if have2 else 'odd') + ('_unscored' if residual else ('_edge' if all_edges else '_noedge'))
                examples.setdefault(key, [n,M,B,ws[0]])
                if any(w[0] == 2 and w[5] == 1 for w in ws):
                    examples.setdefault('two_a1',[n,M,B,next(w for w in ws if w[0] == 2 and w[5] == 1),all_edges])
                row = dict(group=name,k=k,n=n,x=x if residual else None,M=M,B=B,w=ws,edges=all_edges)
                output.write(json.dumps(row,separators=(',',':'))+'\n')
        summary[name] = dict(counts=dict(c),overflow_primes=dict(over),examples=examples)
        print(name,dict(c),flush=True)
    scan_group('prime_complete',[(4,p,p) for p in ps])
    scan_group('composite_complete',[(4,n,n) for n in comps])
    scan_group('fixtures_511',[(4,n,min(n,511)) for n in fixtures])
    # Same residual invariant across numerators, for comparability.
    scan_group('four_residual',[(4,n,0) for n in [11,17,131,241,2113,3985]],True)
    scan_group('eight_residual',[(8,n,0) for n in [11,17,131,241]],True)
    with gzip.open(OLD/'failures.json.gz','rt') as f:
        failures = json.load(f)
    ns15 = [r['n'] for r in failures if r['k'] == 15 and r['minimum'] == 1]
    scan_group('fifteen_residual',[(15,n,0) for n in ns15],True)
    # Matched shaped controls for the transport graph (not a complete ES detector).
    scan_group('eight_shaped',[(8,n,n) for n in [11,17,131,241]])
    output.close()
    scaled = []
    for n in comps:
        p = factor(n)[0][0]
        xyz = [z*(n//p) for z in residual_solution(4,p)]
        assert sum((Fraction(1,z) for z in xyz),Fraction()) == Fraction(4,n)
        div = [z % n == 0 for z in xyz]
        I = sum(div) == 1 and all(gcd(n,z) == 1 for z in xyz if z % n)
        II = sum(div) == 2 and all(gcd(n,z) == 1 for z in xyz if z % n)
        scaled.append(dict(n=n,p=p,xyz=xyz,typeI=I,typeII=II))
    summary['scaling'] = scaled
    # All named primes have exact zero targets, without restricting to our moves.
    summary['fixture_targets'] = []
    for n in fixtures:
        if not fmpz(n).is_prime():
            continue
        for m in range((-n)%4,1001,4):
            if gcd(n,m) != 1:
                continue
            K = (n+m)//4
            _,d,_ = fibre(K,m)
            if d is not None:
                A = (K+d)//m
                xyz = [K,n*A,n*K*A//d]
                assert sum((Fraction(1,z) for z in xyz),Fraction()) == Fraction(4,n)
                summary['fixture_targets'].append([n,m,xyz])
                break
        else:
            raise AssertionError(('no fixture target',n))
    (OUT/'scan.json').write_text(json.dumps(summary,indent=2)+'\n')


if __name__ == '__main__':
    main()
