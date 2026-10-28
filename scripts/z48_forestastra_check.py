"""Independent small/full-tree checks and streaming analysis for FOREST_DEEP_ASTRA.

Uses existing z43 exact edge/certificate helpers rather than duplicating them.
Run: PYTHONPATH=scripts uv run python scripts/z48_forestastra_check.py
Memory O(p) for p <= 100000, and streaming CSV statistics (no Cartesian arrays).
"""
import csv
import gzip
import json
from collections import Counter
from math import gcd, isqrt, lcm
from pathlib import Path

from sympy import factorint, isprime, jacobi_symbol, primerange
from z43_astra_check import certificates, divisor_edges, residue_edges

OUT = Path('data/z48_forestastra')
HARD = [193, 409, 577, 2521, 3361, 5569, 9601, 66529]


def chi(a, p):
    x = pow(a % p, (p - 1) // 2, p)
    return 1 if x == 1 else -1 if x == p - 1 else 0


def formula(t, u, v):
    if u % 2 and v % 2:
        return 1 if u % 4 == v % 4 == 1 else -1
    even = v if u % 2 else u
    if even % 4 == 0:
        return -1
    return 1 if t % 4 in (1, 2) else -1


def local_checks():
    checked = 0
    cells = set()
    # Covers odd/odd, v_2=1, and the higher 2-adic valuations used in the proof.
    for t in range(1, 17):
        for u in list(range(1, 33, 2)) + [2**a*w for a in range(1, 9) for w in range(1, 8, 2)]:
            for v in range(1, 33, 2):
                n = t*u*v-u-v
                if n <= 1 or n % 4 != 1 or gcd(u, v) != 1:
                    continue
                sign = int(jacobi_symbol(u*v, n))
                slots = [t, u, v, t*u-1, t*v-1]
                assert sign == formula(t, u, v)
                assert (sign == -1) == any(x % 4 == 0 for x in slots)
                assert sign == int(jacobi_symbol(t*u-1, n))
                if sign == 1:
                    cells.add((t % 4, u % 4, v % 4))
                    cells.add((t % 4, v % 4, u % 4))
                checked += 1
    return {'unit_words': checked, 'positive_mod4_cells': sorted(cells)}


def full_tree(p):
    # Character table independently by squaring, not Jacobi or exponentiation.
    col = [-1]*p
    col[0] = 0
    for x in range(1, (p+1)//2):
        col[x*x % p] = 1
    assert sum(col[1:]) == 0
    actual_root = list(range(p))
    E = set()
    roots = [1]
    missing = []
    virtual_cuts = 0
    for v in range(2, p):
        a = (-p) % v
        assert 0 < a < v
        q = (p+a)//v
        assert p == q*v-a
        assert col[q] == col[a]*col[v]
        virtual_cuts += col[a] != col[v]
        t,s = divmod(q+1,a)
        assert p-s*v == t*a*v-a-v
        if q > a:
            assert (-p) % q == a
        if (q+1) % a == 0:
            actual_root[v] = actual_root[a]
            E.add((a, v))
        else:
            roots.append(v)
            missing.append((v, actual_root[a]))
    assert len(roots) == p-1-len(E)
    assert len(missing) == len(roots)-1
    quotient_cuts = sum((p-1)//(q-1)-(p-1)//q for q in range(2,p) if col[q] == -1)
    assert quotient_cuts == virtual_cuts
    r = next(q for q in range(2,p) if col[q] == -1)
    rblock = [v for v in range((p+r-1)//r, (p-1)//(r-1)+1) if 2 <= v < p]
    assert len(rblock) == (p-1)//(r-1)-(p-1)//r
    for v in rblock:
        a = r*v-p
        assert col[a] != col[v]
    # For every surviving edge, the divisor parent sits at the bottom of its
    # quotient block: a=a0, or the single t=1 boundary a=q+1 when a0=1.
    for a,v in E:
        q = (p+a)//v
        a0 = (-p) % q
        assert a == a0 or (a0 == 1 and a == q+1)
    assert all(a < v and actual_root[a] == a for v, a in missing)
    assert E | {(1, p+1), (2, p+2)} == residue_edges(p)
    # Root-component character balance and exact Dirichlet energy.
    sizes = Counter(actual_root[1:])
    opposite = Counter(actual_root[v] for v in range(1, p) if col[v] != col[actual_root[v]])
    assert sum(col[r]*(sizes[r]-2*opposite[r]) for r in roots) == 0
    mixed_roots = {actual_root[u] for u, v in E if col[u] != col[v]}
    assert mixed_roots == set(opposite)
    good = sum(col[u] != col[v] for u, v in E)
    energy = sum((col[u]-col[v])**2 for u, v in E)
    assert energy == 4*good
    cminus = (p-1)//2-sum(col[u] == col[v] == -1 for u,v in E)
    degree_negative = sum((col[u] == -1)+(col[v] == -1) for u,v in E)
    assert good == degree_negative-(p-1)+2*cminus
    return {'p': p, 'vertices': p-1, 'edges': len(E), 'components': len(roots),
            'virtual_cuts': virtual_cuts, 'actual_cuts': good,
            'mixed_components': len(mixed_roots), 'r':r, 'least_qnr_block_cuts':len(rblock),
            'least_qnr_block_survivors':sum((r*v-p,v) in E for v in rblock)}


def fibre_details(p, stop):
    ans = []
    for b in range(1, stop+1):
        f = {int(q): int(e) for q, e in factorint(p+b).items()}
        ds = [1]
        for q, e in f.items():
            ds = [d*q**a for d in ds for a in range(e+1)]
        opposite = sorted(d for d in ds if b < d < p and chi(d, p) != chi(b, p))
        if opposite:
            hits = [d for d in opposite if (p+d) % b == 0]
            ans.append({'b': b, 'root_colour': chi(b, p), 'factorization': f,
                        'opposite_children': opposite, 'actual_opposite_children': hits})
    return ans


def family_check():
    seed = 9601
    cs = [seed+i for i in range(1, 7)]
    M = 6*lcm(24, *cs)
    assert gcd(seed, M) == 1
    assert all(M % (6*c) == 0 for c in cs)
    for j, c in enumerate(cs, 1):
        assert all(M % (8*q if q == 2 else 4*q) == 0 for q in factorint(c))
        assert chi(j, seed) == chi(c, seed) == 1
        if j < 6:
            assert all(chi(int(q), seed) == 1 for q in factorint(c))
        else:
            assert factorint(c) == {13: 1, 739: 1}
            assert chi(13, seed) == chi(739, seed) == -1
    assert all(chi(q, seed) == 1 for q in (2, 3, 5, 7, 11)) and chi(13, seed) == -1
    # At every prime other than seed, k=0 avoids all seven forms.
    # At seed, explicitly count the excluded classes (no large Cartesian product).
    forbidden = {0}
    for c in cs:
        forbidden.add((-pow(M//c, -1, seed)) % seed)
    assert len(forbidden) < seed
    return {'seed': seed, 'M': M, 'M_factorization': {int(q):int(e) for q,e in factorint(M).items()},
            'excluded_classes_mod_seed': sorted(forbidden),
            'linear_forms': [[seed, M]] + [[1, M//c] for c in cs]}


def repetition_checks():
    def ds(n):
        out = [1]
        for q,e in factorint(n).items():
            out = [d*int(q)**a for d in out for a in range(int(e)+1)]
        return out
    checks = []
    for seed,h in [(5,1),(13,2),(17,2),(29,3)]:
        r = next(a for a in range(2,seed) if chi(a,seed) == -1)
        cs = [seed+i for i in range(1,h+1)]
        M = 8*lcm(*range(1,h+1))*lcm(*cs)*lcm(*range(1,r+1))
        found = 0
        for k in range(1,50001):
            p = seed+M*k
            if not isprime(p):
                continue
            ls = [1+(M//c)*k for c in cs]
            if min(ls) <= max(cs) or not all(isprime(x) for x in ls):
                continue
            assert next(a for a in range(2,r+1) if chi(a,p) == -1) == r
            for i,(c,ell) in enumerate(zip(cs,ls),1):
                old = ds(c)
                new = old + [d*ell for d in old]
                assert c*ell == p+i and ell % i == 1 % i and chi(ell,p) == 1
                assert all(chi(d,p) == chi(d,seed) for d in old)
                oldsplit = any(chi(int(q),seed) == -1 for q in factorint(c))
                newsplit = any(chi(int(q),p) == -1 for q in factorint(c)) or chi(ell,p) == -1
                assert oldsplit == newsplit
                oldhit = any(d != i and (seed+d) % i == 0 and chi(d,seed) != chi(i,seed) for d in old)
                newhit = any(d != i and (p+d) % i == 0 and chi(d,p) != chi(i,p) for d in new)
                assert oldhit == newhit
                for d in old:
                    if i < d < seed and chi(d,seed) != chi(i,seed):
                        assert i < d < p and (p+i) % d == 0 and chi(d,p) != chi(i,p)
            checks.append({'seed':seed,'h':h,'k':k,'p':p,'new_primes':ls})
            found += 1
            if found == 3:
                break
        assert found == 3, (seed,h,found)
    return checks


def main():
    summary = {'local': local_checks(), 'family': family_check(), 'repetition_examples':repetition_checks()}
    # Dirichlet progression: the entire q=13 virtual cut block is deleted.
    progression = []
    for k in range(300):
        p = 9601+120120*k
        if not isprime(p):
            continue
        assert next(q for q in range(2,14) if chi(q,p)==-1) == 13
        assert (-p) % 13 == 6 and 14 % 6 != 0
        lo,hi = (p+12)//13,(p-1)//12
        # Checking only the first two and last two vertices is a numerical
        # spot-check; the no-survivor assertion is proved algebraically.
        for v in set((lo,lo+1,hi-1,hi)):
            a=13*v-p
            assert 0<a<v and chi(a,p)!=chi(v,p)
            assert 14 % a != 0
        progression.append({'p':p,'virtual_cut_block_size':hi-lo+1})
    summary['dirichlet_block_examples'] = progression
    records = {}
    stats = Counter()
    hist = Counter()
    first_fail = []
    near = {k: [] for k in (-24, -8, -3, 1, 8, 24)}
    max_c_r = (0, None)
    with gzip.open(OUT/'census_1e7.csv.gz', 'rt') as f:
        for raw in csv.DictReader(f):
            row = {k:int(v) for k,v in raw.items()}
            p = row['p']
            if p in HARD or row['split_fibres_to_hit'] >= 5 or p in (7449289,4962049,1726201):
                records[p] = row
            if p % 24 != 1:
                continue
            stats['primes'] += 1
            stats['edges'] += row['edges']
            stats['good_edges'] += row['good_edges']
            stats['first_split_fail'] += 1-row['first_split_hit']
            stats['root1_fail'] += 1-row['root1_mixed']
            stats['min_good_smaller_ge_r'] += row['min_good_smaller'] >= row['r']
            hist[row['split_fibres_to_hit']] += 1
            ratio = row['min_good_smaller']/row['r']
            if ratio > max_c_r[0]:
                max_c_r = (ratio, p)
            if not row['first_split_hit'] and len(first_fail) < 12:
                first_fail.append(row)
            for k in near:
                m = isqrt(max(p-k, 0))
                if m*m == p-k:
                    near[k].append((p,row['H'],row['first_split_hit']))
    summary['p1mod24_to_1e7'] = dict(stats)
    summary['split_fibres_to_hit_histogram'] = dict(sorted(hist.items()))
    summary['first_split_fail_examples'] = first_fail
    summary['max_min_good_smaller_over_r'] = max_c_r
    summary['fixtures_and_extremes'] = [records[p] for p in sorted(records)]
    summary['near_squares'] = {k: {'count':len(rows), 'max_H':max((x[1] for x in rows),default=0),
                                      'first_split_fail':sum(not x[2] for x in rows)} for k,rows in near.items()}
    # Full remainder trees: all eligible small primes plus every hard fixture.
    ps = sorted(set(p for p in primerange(5,30001) if p % 24 == 1) | set(HARD))
    trees = [full_tree(p) for p in ps]
    summary['full_tree_checks'] = {'primes':len(trees), 'vertices':sum(x['vertices'] for x in trees),
                                    'fixtures':[x for x in trees if x['p'] in HARD]}
    # Independent full divisor enumeration at hard fixtures; existing rational identities.
    from fractions import Fraction
    frac_count = 0
    for p in HARD:
        E = divisor_edges(p)
        assert E == residue_edges(p)
        good = [(u,v) for u,v in E if chi(u,p)*chi(v,p) == -1]
        assert min(v for u,v in good) == records[p]['H']
        assert min(u for u,v in good) == records[p]['min_good_smaller']
        for u,v in good:
            for xyz in certificates(p,u,v):
                assert sum((Fraction(1,x) for x in xyz),Fraction()) == Fraction(4,p)
                frac_count += 1
    summary['hard_fixture_fraction_checks'] = frac_count
    detail_primes = HARD + [row['p'] for row in first_fail[:5]] + [4437721,1726201,4962049]
    summary['split_details'] = {p:fibre_details(p, records[p]['min_good_smaller'] if p in records else
                                               next(x['min_good_smaller'] for x in first_fail if x['p']==p))
                                for p in dict.fromkeys(detail_primes)}
    # Existing T1/control tests already cover broader ranges. These expose specifically
    # where our character criterion fails to be an 8-certificate criterion.
    controls = []
    for n in (11,17,131,241,105,9,25,49,81,121,169):
        E = divisor_edges(n)
        slot8 = sum(bool(list(certificates(n,u,v,8))) for u,v in E)
        unit_mixed = sum(gcd(n,u*v)==1 and jacobi_symbol(u*v,n)==-1 for u,v in E)
        if n in (11,17,131,241):
            assert slot8 == 0
        if isqrt(n)**2 == n:
            assert unit_mixed == 0
            assert all(not list(certificates(n,u,v)) for u,v in E)
        if n == 105:
            assert unit_mixed == 0
        controls.append({'n':n,'edges':len(E),'unit_mixed':unit_mixed,'eight_slot_edges':slot8})
    summary['controls'] = controls
    (OUT/'analysis.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k not in ('split_details','family')},indent=2))


if __name__ == '__main__':
    main()
