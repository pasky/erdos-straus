"""Independent residue-set census and arithmetic audit of z47 transport data.
No calls to the scan engine. At most one modulus-sized residue set at a time.
"""
import gzip
import json
from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
from flint import fmpz

P = Path('data/z47_delta_transport')


def fs(n):
    return [(int(p),int(e)) for p,e in fmpz(n).factor()]


def image(factors,m,extra=None):
    S = {1 % m}
    for p,b in factors:
        powers = [pow(p,j,m) for j in range(2*b+1+(p == extra))]
        S = {s*z % m for s in S for z in powers}
    return S


def main():
    rows = {}
    counts = Counter()
    perinput = defaultdict(lambda: Counter())
    with gzip.open(P/'fibres.jsonl.gz','rt') as f:
        for line in f:
            r = json.loads(line)
            name,k,n,m,B = (r[t] for t in ['group','k','n','M','B'])
            key = (name,n,r['x'] if r['x'] is not None else m)
            assert key not in rows
            rows[key] = r
            ff = dict(fs(B))
            # Independently enumerate bounded divisors, then multiply by one prime.
            bounded = [1]
            for p,b in ff.items():
                bounded = [d*p**j for d in bounded for j in range(2*b+1)]
            marked = {(p,p*d) for d in bounded for p,b in ff.items()
                      if d % p**(2*b) == 0 and (p*d+B)%m == 0}
            assert marked == {(w[0],w[2]) for w in r['w']}
            # Valuation proof: one exact extra exponent, all others in budget.
            for ell,b,d,u,v,a,h in r['w']:
                assert b == ff[ell] and d % ell**(2*b+1) == 0 and d % ell**(2*b+2)
                assert B*B*ell % d == 0 and B*B % d != 0
                assert (d+B)%m == 0 and Fraction(d,B) == Fraction(u,v)
                assert gcd(u,v) == 1 and u*v*h == ell*B
                assert u+v == a*m and gcd(a,u*v) == 1 and h % ell
                Y = (B+d)//m
                Z = Fraction(B*Y,d)
                assert Z.denominator == ell
                assert Fraction(1,Y)+1/Z == Fraction(m,B)
                if r['x'] is None:
                    assert k*B == n+m
                    assert Fraction(1,B)+Fraction(1,n*Y)+1/(n*Z) == Fraction(k,n)
                    T = u*v//ell
                    rr = (-n) % (k*T)
                    if k == 4 and ell in (2,3):
                        assert rr == m and (u//ell+v) % rr != 0
                    if k == 4 and ell == 2:
                        # The automatic Fano word is of a*n, not n unless a=1.
                        t = 2*a*h
                        assert t*u*v-u-v == a*n and u%4 == 0 and t%4 == 2
                        X = u//4*(t*v-1)
                        assert gcd(X,a) == 1
                counts['witnesses_checked'] += 1
            if r['x'] is not None:
                continue
            expected = set()
            for i,(ell,b,d,u,v,a,h) in enumerate(r['w']):
                T = u*v//ell
                rr = (-n) % (k*T)
                valid = rr > 0 and gcd(n,rr) == 1
                if valid and (u//ell+v) % rr == 0:
                    expected.add((i,'drop'))
                if valid and any(T%d == 0 and gcd(d,T//d) == 1 and (d+T//d)%rr == 0
                                 for d in range(1,isqrt(T)+1)):
                    expected.add((i,'repartition'))
                if k%ell == 0 and u%k == 0 and a == 1:
                    expected.add((i,'fold'))
            assert expected == {(e[0],e[1]) for e in r['edges']}
            for i,kind,rr,xyz in r['edges']:
                assert sum((Fraction(1,z) for z in xyz),Fraction()) == Fraction(k,n)
                assert k*xyz[0]-n == rr and gcd(xyz[0],n) == 1
                assert xyz[1]%n == 0 and xyz[2]%n == 0 and rr < m
                counts['edges_checked'] += 1
            c = perinput[(name,n)]
            c['sources'] += 1
            c['with_edge'] += bool(r['edges'])
            c['with_fold'] += any(e[1] == 'fold' for e in r['edges'])
    old = json.loads(Path('data/z46_overflow_delta/scan.json').read_text())
    comp = [r[0] for r in old['composite_nonzero'] if r[1] == 1]
    prime = [n for n in range(25,10001,24) if fmpz(n).is_prime()]
    fixtures = sorted(set(r['n'] for r in old['fixtures']) | {2113,31121,3985})
    with gzip.open('data/z46_overflow_delta/failures.json.gz','rt') as f:
        fail = json.load(f)
    fifteen = [r['n'] for r in fail if r['k'] == 15 and r['minimum'] == 1]
    groups = [
        ('prime_complete',4,prime,False,None),
        ('composite_complete',4,comp,False,None),
        ('fixtures_511',4,fixtures,False,511),
        ('four_residual',4,[11,17,131,241,2113,3985],True,None),
        ('eight_residual',8,[11,17,131,241],True,None),
        ('fifteen_residual',15,fifteen,True,None),
        ('eight_shaped',8,[11,17,131,241],False,None)]
    census = {}
    for name,k,ns,residual,limit in groups:
        c = Counter()
        for n in ns:
            c['inputs'] += 1
            for x in (range(n//k+1,3*n//k+1) if residual else range((-n)%k or k,min(n,limit or n)+1,k)):
                if residual:
                    g = gcd(k*x-n,n*x)
                    m,B = (k*x-n)//g,n*x//g
                else:
                    m = x
                    if gcd(n,m) != 1:
                        continue
                    B = (n+m)//k
                f = fs(B)
                S = image(f,m)
                r0 = (-B)%m
                c['fibres'] += 1
                zero = r0 in S
                # Multiplying a bounded divisor by one generator detects radius one.
                one = not zero and any((r0*pow(p,-1,m))%m in S for p,_ in f)
                key = (name,n,x)
                assert one == (key in rows), key
                c['zero'] += zero
                c['delta_one'] += one
                if one:
                    assert rows[key]['B'] == B and rows[key]['M'] == m
                    available = {p for p,_ in f if r0 in image(f,m,p)}
                    assert available == {w[0] for w in rows[key]['w']}
                    counts['profiles_checked'] += 1
        census[name] = dict(c)
        print(name,dict(c),flush=True)
    scan = json.loads((P/'scan.json').read_text())
    for name,c in census.items():
        for key,value in c.items():
            assert scan[name]['counts'].get(key,0) == value
    for row in scan['scaling']:
        n,p,xyz = row['n'],row['p'],row['xyz']
        assert p in (3,5) and n%p == 0
        assert sum((Fraction(1,z) for z in xyz),Fraction()) == Fraction(4,n)
        assert all(gcd(n,z)>1 for z in xyz)
    for n,m,xyz in scan['fixture_targets']:
        assert sum((Fraction(1,z) for z in xyz),Fraction()) == Fraction(4,n)
        assert 4*xyz[0]-n == m and gcd(n,xyz[0]) == 1
    strata = {}
    for label,predicate in [('mordell',lambda n: n%840 in (1,121,169,289,361,529)),
                            ('near_square_24',lambda n: min(n-isqrt(n)**2,(isqrt(n)+1)**2-n)<=24)]:
        selected = [r for r in rows.values() if r['group']=='prime_complete' and predicate(r['n'])]
        strata[label] = dict(inputs=len({r['n'] for r in selected}),sources=len(selected),
                            with_edge=sum(bool(r['edges']) for r in selected))
    report = dict(checks=dict(counts),census=census,strata=strata,
        scaled_by_prime=dict(Counter(str(r['p']) for r in scan['scaling'])),
        prime_inputs_with_sources=sum(('prime_complete',p) in perinput for p in prime),
        prime_inputs_with_fold=sum(perinput[('prime_complete',p)]['with_fold']>0 for p in prime),
        prime_inputs_with_edge=sum(perinput[('prime_complete',p)]['with_edge']>0 for p in prime),
        prime_inputs_no_fold=[p for p in prime if not perinput[('prime_complete',p)]['with_fold']],
        perinput=[dict(group=g,n=n,**dict(c)) for (g,n),c in sorted(perinput.items())])
    (P/'verify.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'perinput'},indent=2))


if __name__ == '__main__':
    main()
