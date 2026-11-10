"""Independent Z70 GEN review audit; run against an exported side-agent/z70-gen tree.
Predeclared checks: all stored aggregate/X-null numbers; fresh first/middle/last
prime of each window at every d (45 records); independent reduced-form census
and e-fibre enumeration at the first W1 prime for each d; all canonical REP
fibres; screen input/count audit. No tuning or new significance thresholds.
Memory: stream files, at most one window/d (~1561 small records) in memory;
class engines retain at most one group. Use ulimit -v 6000000 and timeout 1800.
Usage: uv run --with cypari2 python THIS /tmp/xrev_GEN [aggregate|fresh|rep|screens]
"""
import collections
import glob
import json
import math
import os
import sys

root, mode = sys.argv[1:3]
os.chdir(root)
sys.path.insert(0, os.path.join(root, 'scripts'))


def rows(path):
    with open(path) as f:
        return [json.loads(s) for s in f]


def z(h, e, v):
    return (h - e) / math.sqrt(v) if v else float('nan')


def aggregate():
    for ws in [('W1', 'W2'), ('W3',)]:
        union = collections.defaultdict(bool)
        empty = fr = seeds = 0
        for d in [1, 2, 3, 5, 7]:
            rr = sum((rows(f'raw/run_{w}_d{d}.jsonl') for w in ws), [])
            assert len({r['n'] for r in rr}) == len(rr)
            hist = collections.defaultdict(lambda: [0, 0])
            for r in rr:
                assert len(r['base_primes']) == r['genera'], (r['n'], d)
                for a, (n, k) in r['ahist'].items():
                    hist[int(a)][0] += n
                    hist[int(a)][1] += k
                union[r['n']] |= bool(r['fam']['GEN2']['hit'])
                empty += not r['G']
                fr += r['it3']['frviol']
                seeds += r['it3']['nT']
            for fam in ['RED', 'CYC', 'GEN2']:
                h = e = v = 0
                dropped = unseen = 0
                for r in rr:
                    for a, weight, hit, _ in r['seeds'][fam]:
                        if a > 5000:
                            dropped += 1
                            continue
                        n0, k0 = r['ahist'][str(a)]
                        n, k = hist[a]
                        unseen += n == n0
                        rate = (k - k0) / (n - n0) if n != n0 else 0
                        h += weight * hit
                        e += weight * rate
                        v += weight ** 2 * rate * (1 - rate)
                print('/'.join(ws), d, fam, 'H', h, 'E', round(e, 3),
                      'z', round(z(h, e, v), 3), 'dropped', dropped, 'unseen', unseen)
            for fam in ['CYC', 'GEN2']:
                print('/'.join(ws), d, fam, 'seed identity',
                      sum(r['seedid'][fam]['seed_ideal_natural'] for r in rr),
                      '/', sum(r['seedid'][fam]['hits'] for r in rr))
        failures = [p for p, hit in union.items() if not hit]
        assert all(p % 840 in {1, 121, 169, 289, 361, 529} for p in failures)
        print('/'.join(ws), 'union', sum(union.values()), '/', len(union),
              'empty', empty, 'FR violations', fr, 'target seed ideals', seeds)
    for screen in ['F2', 'F4']:
        covered, hits = collections.defaultdict(bool), collections.Counter()
        nonempty, empty = set(), 0
        for path in sorted(glob.glob(f'screens/scr_{screen}_d*.jsonl')):
            for r in rows(path):
                assert 'skipped' not in r
                empty += r['G'] == 0
                if r['G']:
                    nonempty.add(r['n'])
                for fam, s in r['fam'].items():
                    hits[fam] += s['hit']
                    covered[r['n']] |= bool(s['hit'])
                assert r['it3']['frviol'] == 0
        print(screen, 'nonempty primes', len(nonempty), 'empty pairs', empty,
              'hits', dict(hits), 'uncovered', [p for p, h in covered.items() if not h])


def reduced_forms(p, d):
    """Plain integer enumeration, independent of PARI class-number assumptions."""
    out = set()
    for a in range(1, math.isqrt(4 * d * p // 3) + 1):
        for b in range(-a + a % 2, a + 1, 2):
            c, rem = divmod(b * b + 4 * d * p, 4 * a)
            if rem or c < a or math.gcd(math.gcd(a, b), c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            out.add((a, b, c))
    return out


def same(a, b):
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    if isinstance(a, float):
        return math.isclose(a, b, rel_tol=1e-12, abs_tol=1e-10)
    return a == b


def fresh():
    import z70_gen_core as C
    import z70_gen_run as R
    count = 0
    for w in ['W1', 'W2', 'W3']:
        for d in [1, 2, 3, 5, 7]:
            rr = rows(f'raw/run_{w}_d{d}.jsonl')
            for idx in [0, len(rr) // 2, len(rr) - 1]:
                old = rr[idx]
                new = json.loads(json.dumps(R.run_one(old['n'], d)))
                old.pop('sec'); new.pop('sec')
                # PARI's generator basis may change between calls; position labels
                # are not canonical. Compare inversion-orbit occupancy and orders,
                # not the arbitrary coordinate names. Preserve every other field.
                for rec in (old, new):
                    mods = [m & -m for m in rec['cyc']]
                    occupancy = {}
                    for label, count_at in rec['pos'].items():
                        pos = tuple(int(x) for x in label.strip('()').split(',') if x.strip())
                        neg = tuple(-x % m for x, m in zip(pos, mods))
                        order = math.lcm(*(m // math.gcd(x, m) for x, m in zip(pos, mods)))
                        key = (min(pos, neg), order, pos == neg)
                        occupancy[key] = occupancy.get(key, 0) + count_at
                    rec['pos'] = sorted((o, fixed, n) for (_, o, fixed), n in occupancy.items())
                    for family in rec['seeds']:
                        rec['seeds'][family].sort()
                assert same(old, new), (w, d, old['n'], [k for k in old if not same(old[k], new[k])])
                count += 1
                if w == 'W1' and idx == 0:
                    p = old['n']
                    cg = C.ClassGroup(p, d)
                    assert reduced_forms(p, d) == set(cg.elts)
                    exact = set()
                    for e in range((-p) % (4*d), (p+4*d)//(4*d-1)+1, 4*d):
                        m = (p+e)//(4*d)
                        for a in C.divisors(m):
                            b = m//a
                            if (a+b) % e == 0:
                                exact.add((a, b, (a+b)//e, e))
                    assert exact == C.solutions(p, d)
                    print('independent census', p, d, 'h', cg.h, 'solutions', len(exact), flush=True)
                print('fresh equality', w, d, old['n'], flush=True)
    print('fresh records matched', count)


def rep():
    import z70_gen_core as C
    counts = collections.Counter()
    for w in ['W1', 'W2', 'W3']:
        primes = [r['n'] for r in rows(f'raw/run_{w}_d1.jsonl')]
        for d in [1, 2, 3, 5, 7]:
            for p in primes:
                # Direct integer square search, independent of qfbsolve.
                for a in range(1, math.isqrt(p//(4*d))+1):
                    x2 = p - 4*d*a*a
                    if math.isqrt(x2)**2 != x2:
                        continue
                    assert all((A+1) % (4*a*d) for A in C.divisors(p+4*d*a*a))
                    counts[d] += 1
    assert dict(counts) == {1: 2152, 2: 2152, 3: 2152, 5: 565, 7: 1067}
    print('REP direct square search', dict(counts), 'total', sum(counts.values()))


def screens():
    import z70_gen_core as C
    def inputs(name):
        with open('data/z58/screens/' + name) as f:
            return {int(s.split()[0]) for s in f if s.strip() and not s.startswith('#')}
    expected = {
        'F2': inputs('r8_zeros_1e10.txt'),
        'F4': inputs('star_prime_zeros.txt') | inputs('gstar_zeros.txt') | {2521, 3361, 21841, 76441},
    }
    count = 0
    for screen, primes in expected.items():
        for path in sorted(glob.glob(f'screens/scr_{screen}_d*.jsonl')):
            rr = rows(path)
            assert {r['n'] for r in rr} == primes
            for r in rr:
                p, d = r['n'], r['d']
                sols = C.solutions(p, d)
                gg = {C.good_class(p, d, s) for s in sols}
                assert len(sols) == r['nsol'] and len(gg) == r['G'], (p, d)
                if screen == 'F2' and d == 2:
                    assert all(s[2] > 1 for s in sols)
                    assert all((A+1) % 8 for A in C.divisors(8*p+1))
                count += 1
            print('screen solutions/G matched', path, len(rr), flush=True)
    print('screen pairs checked', count)


{'aggregate': aggregate, 'fresh': fresh, 'rep': rep, 'screens': screens}[mode]()
