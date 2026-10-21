"""Independent board #4 audit (board #4 addendum, 2026-10-19).

No seat-script imports. Enumerates folds by u and divisors of p+u;
checks trap closure statically, not by BFS. Streams complete residual fibres.
Run: ulimit -v 1000000; timeout 300 uv run python scripts/z48_closure_verify.py
"""
import json
from functools import lru_cache
from math import gcd, isqrt
from pathlib import Path

from sympy import factorint, isprime, jacobi_symbol, primerange

OUT = Path("data/z48_closure")
MORDELL = {1, 121, 169, 289, 361, 529}


@lru_cache(maxsize=1024)
def factor(n):
    fs = tuple((int(r), int(e)) for r, e in factorint(n).items())
    product = 1
    for r, e in fs:
        # All factors here are well below 2**64 (deterministic SymPy range).
        assert r < 2**64 and isprime(r)
        product *= r**e
    assert product == n
    return fs


def divisors(n, power=1):
    fs = factor(n)

    def descend(i, d):
        if i == len(fs):
            yield d
            return
        r, e = fs[i]
        for _ in range(power * e + 1):
            yield from descend(i + 1, d)
            d *= r

    return descend(0, 1)


def identity(k, n, triple):
    x, y, z = triple
    assert min(triple) > 0
    assert k*x*y*z == n*(x*y + x*z + y*z)


def residual(k, n, x):
    a, b = k*x-n, n*x
    assert a > 0
    g = gcd(a, b)
    return a//g, b//g


def splits(a, b):
    for d in divisors(b, 2):
        if d <= b and (b+d) % a == 0:
            assert (b+b*b//d) % a == 0
            yield d, (b+d)//a, (b+b*b//d)//a


def solutions(k, n):
    for x in range(n//k+1, 3*n//k+1):
        for _, y, z in splits(*residual(k, n, x)):
            if x <= y:
                identity(k, n, (x, y, z))
                yield x, y, z


def folds():
    ps = [p for p in primerange(5, 10001) if p % 24 == 1]
    hits = {2: set(), 4: set()}
    fibres = {2: set(), 4: set()}
    odd, unfiltered, rows = set(), set(), []
    for p in ps:
        zero_cache = {}
        # p+u = v(tu-1); unlike the seat scans, neither m nor K is outermost.
        for u in range(4, p, 4):
            for v in divisors(p+u):
                if u+v > p or v % 2 == 0 or gcd(u, v) != 1:
                    continue
                j = (p+u)//v
                if (j+1) % u:
                    continue
                t = (j+1)//u
                if t % 4 == 0:
                    continue
                m, K = u+v, (p+u+v)//4
                assert 4*K == p+m and gcd(m, p) == 1
                unfiltered.add(p)
                if m not in zero_cache:
                    zero_cache[m] = any((d+K) % m == 0 for d in divisors(K, 2))
                if zero_cache[m]:
                    continue
                s = 4 if t % 2 else 2
                h = t*s//4
                assert h % 2 and K*s == h*u*v
                dmark = K*u//v
                assert K*u % v == 0 and (dmark+K) % m == 0
                assert (s*K*K) % dmark == 0
                target = (u//4*(t*v-1), p*t*u//4, p*t*u//4*(t*v-1))
                identity(4, p, target)
                # Existing a=1 ET-II certificate, not a new family.
                a, b, c, d, e = 1, t*v-1, t, u//4, v
                assert a+b == c*e and 4*a*b*d == p+e
                assert gcd(p, target[0]) == 1
                hits[s].add(p)
                fibres[s].add((p, m))
                if s == 4 and K % 2:
                    odd.add(p)
                rows.append(dict(p=p, m=m, K=K, s=s, u=u, v=v, t=t, target=target))
    summary = dict(primes=len(ps), internal=len(hits[2]), odd_t=len(hits[4]),
                   union=len(hits[2] | hits[4]), odd_K=len(odd),
                   unfiltered=len(unfiltered), marks=len(rows),
                   fibres={str(s): len(fibres[s]) for s in (2, 4)},
                   missed=sorted(set(ps)-hits[2]-hits[4]))
    assert (len(ps), summary['internal'], summary['union'], len(odd), len(rows)) == (143, 99, 131, 93, 542)
    assert len(unfiltered) == 137
    identity(4, 115, (29, 6670, 6670))
    # Genuine numerator-8 failure has an external-2 source but no integral fold.
    n, K, m, u, v, h = 241, 35, 39, 4, 35, 1
    assert 8*K == n+m and K == h*u*v//4 and u+v == m
    assert not any((d+K) % m == 0 for d in divisors(K, 2))
    assert (n+v) % 8 == 4
    (OUT/'folds.json').write_text(json.dumps(rows, indent=2)+'\n')
    return summary


def trap(p):
    assert isprime(p) and p > 5 and p % 5 == 1
    vertices = {tuple(sorted(v)) for v in (
        (2*p, 2*p, 3*p), (p+1, 3*p, p*(p+1)),
        (2*p, (6*p+4)//5, 3*p*(3*p+2)//5),
        (2*p, 3*(2*p+3)//5, 2*p*(2*p+3)//5))}
    assert len(vertices) == 4
    for v in vertices:
        identity(4, 3*p, v)
    table, closed = [], True
    for x in sorted({x for v in vertices for x in v}):
        a, b = residual(4, 3*p, x)
        pairs = list(splits(a, b))
        neighbours = {tuple(sorted((x, y, z))) for _, y, z in pairs}
        closed &= neighbours <= vertices
        table.append(dict(x=x, a=a, b=b, factors=factor(b), divisors=sorted(d for d, _, _ in pairs),
                          fibre=sorted(neighbours)))
    return dict(p=p, closed=closed, vertices=sorted(vertices),
                targets=sum(all(x % 3 == 0 for x in v) for v in vertices), fibres=table)


def gaussian(p):
    pairs = [(isqrt(p-b*b), b) for b in range(1, isqrt(p//2)+1)
             if isqrt(p-b*b)**2 == p-b*b]
    assert len(pairs) == 1
    return pairs[0]


def elementary(q):
    return q % 840 not in MORDELL or any(r % 4 != 1 for r, _ in factor(q))


def free_census():
    ps = [p for p in primerange(5, 100000) if p % 840 in MORDELL]
    records, exceptional, diagonal_checks = [], [], 0
    for p in sorted(set(ps) | {97, 193, 313, 3361, 5209, 233689}):
        a, b = gaussian(p)
        Q = sorted({a, b, a+b, a-b}-{1})
        bad = [q for q in Q if not elementary(q)]
        assert set(bad) <= {169, 289}
        for q in (a+b, a-b):
            for ell, _ in factor(q):
                if ell != 2:
                    assert jacobi_symbol(p, ell) == jacobi_symbol(2, ell)
                    diagonal_checks += 1
        for q in bad:
            r = isqrt(q)
            base = next(solutions(4, r))
            identity(4, q, tuple(r*x for x in base))
        row = dict(p=p, a=a, b=b, Q=Q, scaling_only=bad)
        records.append(row)
        if p in ps and bad:
            exceptional.append(row)
    assert len(ps) == 273 and len(exceptional) == 8
    (OUT/'coordinates.json').write_text(json.dumps(records, indent=2)+'\n')
    return dict(primes=len(ps), elementary=len(ps)-len(exceptional), all_soluble=len(ps),
                scaling_cases=exceptional, diagonal_checks=diagonal_checks,
                fixtures=[r for r in records if r['p'] in {97,193,313,3361,5209,233689}])


def mixed():
    counts, rows = {}, []
    for p in primerange(5, 100):
        count = 0
        for triple in solutions(4, p*p):
            valuations = []
            for x in triple:
                e = 0
                while x % p == 0:
                    e += 1
                    x //= p
                valuations.append(e)
            if sorted(valuations)[:2] != [0, 1] or max(valuations) < 2:
                continue
            assert sorted(valuations) == [0, 1, 2]
            K = triple[valuations.index(0)]
            m = 4*K-p*p
            assert m > 0 and m % 4 == 3 and gcd(m, p) == 1
            assert jacobi_symbol(p, m) == -1
            rows.append(dict(p=p, triple=triple, K=K, m=m))
            count += 1
        counts[p] = count
    assert sum(counts.values()) == 1096
    assert sum(v for p, v in counts.items() if p < 60) == 529
    (OUT/'mixed.json').write_text(json.dumps(rows, indent=2)+'\n')
    return dict(total=sum(counts.values()), below60=529, violations=0, by_prime=counts)


def controls():
    out = []
    for k, p in ((12,1657), (10,181)):
        a, b = gaussian(p)
        # Q excludes 1: it is outside ES's domain, not a soluble source.
        Q = sorted({a,b,a+b,a-b}-{1})
        witnesses = {q: next(solutions(k,q)) for q in Q}
        assert list(solutions(k,p)) == []
        out.append(dict(k=k, p=p, coordinates=[a,b], sources=witnesses, target_solutions=0))
    for p in (11,17,131,241):
        assert list(solutions(8,p)) == []
    # Explicit normalization-loophole witness at an odd square.
    identity(4, 9, (3,18,18))
    identity(4, 169, (52,234,6084))
    assert 169 == 12**2 + 5**2
    assert all(next(solutions(4, q), None) for q in (5,7,12,17))
    return out


def pairing():
    # Fully deterministic replacement for the seat's unavailable random-pair raw data.
    ps = [p for p in primerange(10000, 100000) if p % 840 in MORDELL]
    rows, matched, shuffled = [], 0, 0
    for p in ps:
        for D in (1,2,3):
            b = next(b for b in range(1,isqrt(p//D)+1)
                     if isqrt(p-D*b*b)**2 == p-D*b*b)
            modulus = 4*b-1
            allowed = {(-d*pow(b,-1,modulus)) % modulus for d in divisors(b,2)}
            own = p % modulus in allowed
            others = sum(q % modulus in allowed for q in ps if q != p)
            matched += own
            shuffled += others
            rows.append(dict(p=p, D=D, b=b, hit=own, other_hits=others))
    (OUT/'pairing.json').write_text(json.dumps(rows, indent=2)+'\n')
    return dict(primes=len(ps), windows=len(rows), matched_hits=matched,
                matched_rate=matched/len(rows), all_other_hits=shuffled,
                all_other_trials=len(rows)*(len(ps)-1),
                all_other_rate=shuffled/(len(rows)*(len(ps)-1)))


def forms():
    # Finite sanity check of the separately proved principal-form audit.
    records = []
    for p in (1201,3361,5209,14281,233689):
        assert p % 840 in MORDELL
        row = {'p':p}
        for D in (1,2,5,-2,-3):
            pair = next((isqrt(p-D*y*y),y) for y in range(1,4*isqrt(p)+1)
                        if p-D*y*y >= 0 and isqrt(p-D*y*y)**2 == p-D*y*y)
            row[str(D)] = pair
        for D in (3,7):
            pair = next((isqrt(4*p-D*y*y),y) for y in range(1,isqrt(4*p//D)+1)
                        if isqrt(4*p-D*y*y)**2 == 4*p-D*y*y)
            row['4p_D'+str(D)] = pair
        records.append(row)
    return records


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    summary = {}
    for name, fun in [('folds',folds), ('coordinates',free_census), ('controls',controls),
                      ('pairing',pairing), ('mixed',mixed), ('forms',forms)]:
        summary[name] = fun()
        print(name, json.dumps(summary[name]), flush=True)
    traps = [trap(p) for p in (1321,6121,12241,14281)]
    assert all(r['closed'] and r['targets'] == 0 for r in traps)
    counter = trap(61)
    assert not counter['closed']
    (OUT/'traps.json').write_text(json.dumps(traps+[counter], indent=2)+'\n')
    summary['traps'] = {str(r['p']):r['closed'] for r in traps+[counter]}
    (OUT/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print('All independent audits passed.', flush=True)


if __name__ == '__main__':
    main()
