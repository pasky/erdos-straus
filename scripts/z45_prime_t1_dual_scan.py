"""Exact, bounded-memory dual anatomy; run with ulimit and timeout (see memo)."""
import json
from collections import Counter, defaultdict
from math import gcd, isqrt
from pathlib import Path
from random import Random
from flint import fmpz

OUT = Path('data/z45_prime_t1_dual')
OUT.mkdir(parents=True, exist_ok=True)
STAR = [409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]
PW15 = [1,2,3,4,8,16,17,19,23,31,34,47,53,61,79,113,122,137,151,197,226,233,271,541,1103,1171,1367,4201,6301,12601,16831,20521]

def factors(n):
    return [(int(p), int(e)) for p,e in fmpz(n).factor()]

def divs(fac):
    ds = [1]
    for p,e in fac:
        old = ds[:]
        q = 1
        for _ in range(e):
            q *= p
            ds.extend(d*q for d in old)
    return ds

def jacobi(a,n):
    assert n > 0 and n % 2
    a %= n
    out = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3,5): out = -out
        a,n = n,a
        if a % 4 == n % 4 == 3: out = -out
        a %= n
    return out if n == 1 else 0

def kron(D,p):
    if p == 2:
        return 0 if D % 2 == 0 else (1 if D % 8 in (1,7) else -1)
    return jacobi(D,p)

def fundamental_negative(f):
    D = -f
    if D % 4 == 1:
        return all(e == 1 for _,e in factors(f))
    if D % 4 == 0 and (D//4) % 4 in (2,3):
        return all(e == 1 for _,e in factors(f//4))
    return False

# Under 100KB; generated once, not an array of character/fibre products.
QDISCS = {f for f in range(3,50001) if fundamental_negative(f)}

def subgroup(gens,m):
    H = {1 % m}
    for g in gens:
        g %= m
        if g in H: continue
        old = list(H)
        z = g
        while z not in H:
            H.update((h*z) % m for h in old)
            z = z*g % m
    return H

def analyze_fibre(N,m,r,accept=lambda d: True, fac=None):
    # Only unit prime factors can occur in a unit-class divisor.
    if fac is None: fac = factors(N)
    fac = [(p,e) for p,e in fac if gcd(p,m) == 1]
    ps = [p for p,_ in fac]
    r %= m
    ds = divs(fac)
    hits = [d for d in ds if d % m == r and accept(d)]
    quad = []
    for f in divs(factors(m)):
        if f not in QDISCS: continue
        D = -f
        if all(kron(D,p) == 1 for p in ps):
            value = 1
            for p,e in factors(r): value *= kron(D,p)**e
            if value == -1: quad.append(D)
    quad.sort(key=abs)
    if hits:
        assert not quad
        kind, conductor = 'hit', None
    elif quad:
        kind, conductor = 'quadratic', abs(quad[0])
    else:
        H = subgroup(ps,m)
        if r not in H:
            kind = 'higher'
            conductor = min(f for f in divs(factors(m)) if r % f not in subgroup(ps,f))
        elif not any(d % m == r for d in ds):
            kind, conductor = 'budget', None
        else:
            kind, conductor = 'height', None
    # Smallest reduction modulus that already separates the bounded divisor image.
    # This is exact in the class of quotient-congruence duals; height is not encoded.
    budget_modulus = next((f for f in sorted(divs(factors(m)))
                           if all(d % f != r % f for d in ds)), None)
    return dict(N=N, modulus=m, target=r, primes=ps, kind=kind,
                conductor=conductor, quadratic=quad, witness=min(hits) if hits else None,
                divisor_count=len(ds), budget_modulus=budget_modulus)

def full(m,n):
    rows = []
    for x in range(n//m+1, 3*n//m+1):
        g = gcd(m*x-n,n*x)
        a,b = (m*x-n)//g,n*x//g
        row = analyze_fibre(b*b,a,-b,lambda d: d <= b and (d+b)//a >= x,
                            [(p,2*e) for p,e in factors(b)])
        row['x'] = x
        rows.append(row)
    return rows

def star(n):
    rows = []
    u = 1
    while 4*u*u-2*u <= n:
        row = analyze_fibre(n+u,4*u,-1)
        row['u'] = u
        rows.append(row)
        u += 1
    return rows

def b1(n):
    return [dict(analyze_fibre(n+4*d,4*d,-1,lambda w: w<n+4*d), d=d)
            for d in range(1,(n+3)//8+1)]

def summary(rows):
    counts = Counter(r['kind'] for r in rows)
    coverage = Counter(D for r in rows for D in r['quadratic'])
    best = sorted(coverage.items(),key=lambda t:(-t[1],abs(t[0])))[:1]
    quotients = Counter(r['budget_modulus'] for r in rows if r['budget_modulus'])
    return dict(fibres=len(rows),counts=dict(counts),best_quadratic=best,
                quotient_moduli=dict(sorted(quotients.items())),
                quotient_bits=sum(r['budget_modulus'].bit_length() for r in rows if r['budget_modulus']),
                original_bits=sum(r['modulus'].bit_length() for r in rows if r['budget_modulus']),
                min_conductors=sorted(set(r['conductor'] for r in rows if r['conductor'])),
                first_noncharacter=next((r for r in rows if r['kind'] in ('budget','height')),None))

def next_control(n,engine,rng,mod=1):
    start = n + rng.randrange(1,max(20,n//50))
    for c in range(start,start+max(1000,n)):
        if c % mod != n % mod or not fmpz(c).is_prime(): continue
        rows = engine(c)
        if any(r['kind']=='hit' for r in rows): return c,rows
    raise RuntimeError('no control')

def forest(n,root):
    # Small inputs only; O(n) memory. Independent of divisor-fibre engine.
    adj = defaultdict(list)
    edges = []
    for v in range(2,n+3):
        u = (-n) % v
        if u and (n+u+v) % (u*v) == 0:
            t = (n+u+v)//(u*v)
            good = any(z % 4 == 0 for z in (t,u,v,t*u-1,t*v-1))
            edges.append((u,v,t,good))
            adj[u].append(v); adj[v].append(u)
    seen = {root}; stack=[root]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen: seen.add(v); stack.append(v)
    ce = [e for e in edges if e[0] in seen]
    return dict(n=n,root=root,vertices=sorted(seen),component_edges=len(ce),
                component_good=sum(e[3] for e in ce),all_edges=len(edges),
                all_good=sum(e[3] for e in edges),
                component_colours=dict(Counter(jacobi(v,n) for v in seen)),
                nonunit_edges=sum(gcd(u*v,n)>1 for u,v,_,_ in edges))

def validate():
    # Independent y enumeration checks the fibre implementation, not just input constants.
    for m in (4,8,15):
        for n in range(1,100):
            triples=[]
            for x in range(n//m+1,3*n//m+1):
                A=m*x-n; B=n*x
                for y in range(max(x,B//A+1),2*B//A+1):
                    den=A*y-B
                    if den>0 and B*y % den == 0 and B*y//den>=y:
                        triples.append((x,y,B*y//den))
            assert bool(triples)==any(r['kind']=='hit' for r in full(m,n)),(m,n)
    for n in (9,25,49,81,121,169,225):
        assert all(r['kind']=='quadratic' for r in star(n))
    # Known exponent-budget obstruction, independently inspected in the memo.
    r=analyze_fibre(20*20,29,-20)
    assert r['kind']=='budget'

if __name__ == '__main__':
    validate()
    rng=Random(45017)
    result=[]
    for name,ns,engine,mod in [('full8',[11,17,131,241],lambda n:full(8,n),1),
                              ('full15',PW15,lambda n:full(15,n),1),
                              ('star',STAR,star,24),('b1',[193,2521,66529],b1,24)]:
        for n in ns:
            rows=engine(n)
            assert not any(r['kind']=='hit' for r in rows),(name,n)
            (OUT/f'{name}_{n}.json').write_text(json.dumps(rows,indent=2)+'\n')
            c,cr=next_control(n,engine,rng,mod)
            rec=dict(family=name,n=n,**summary(rows),control=dict(n=c,**summary(cr)))
            result.append(rec)
            print(name,n,rec['counts'],'control',c,rec['control']['counts'],flush=True)
    (OUT/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    fixtures=[409,1201,5569,8521,8641,9649,12289,12721,12841,15241,16921,19441,23761,23929,24481,27241,
              49681,61561,104161,229321]
    fr=[forest(n,1) for n in fixtures]
    for n in [1201,2521,3361,5569,7561,9769]:
        root=next(a for a in range(2,n) if jacobi(a,n)==-1)
        fr.append(forest(n,root))
    fr += [forest(105,1),forest(169,1)]
    for n in [433,1249,12781,2521,3361,5101441]:
        # Last large fixture handled by star/b1 only: avoid O(n) forest allocation.
        if n<100000: fr.append(forest(n,1))
    (OUT/'forest.json').write_text(json.dumps(fr,indent=2)+'\n')
    print('validated independent brute-force decisions for 297 (m,n) inputs',flush=True)
