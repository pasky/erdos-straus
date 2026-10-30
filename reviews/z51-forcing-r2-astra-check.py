#!/usr/bin/env python3
"""Independent pair-first audit; no campaign code imported.

Memory: one 32-bit SPF table of size p//4+2 (<1.3 MB at tested p),
a divisor list for one integer, and residue sets of size <= q.
Run with: ulimit -v 8000000; timeout 120s uv run --no-project THIS_FILE
"""
from array import array
from fractions import Fraction
from math import isqrt, log, exp
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def spf_table(n):
    spf = array('I', range(n + 1))
    for d in range(2, isqrt(n) + 1):
        if spf[d] == d:
            for v in range(d * d, n + 1, d):
                if spf[v] == v:
                    spf[v] = d
    return spf


def divisors(n, spf):
    result = [1]
    while n > 1:
        d = spf[n]
        power = 1
        old = result[:]
        while n % d == 0:
            n //= d
            power *= d
            result.extend(v * power for v in old)
    return result


def enumerate_reach(p, qs):
    assert p % 4 == 1
    spf = spf_table(p // 4 + 1)
    output = {}
    for q in qs:
        reached = set()
        full = set()
        tail = []
        witnesses = {}
        count_i = count_ii = 0
        bound = p // (4 * q)
        for u in range(1, bound + 1):
            if u % q == 0:
                continue
            for v in range(1, bound // u + 1):
                if v % q == 0:
                    continue
                modulus_off_q = 4 * u * v
                for e in divisors(q * u + v, spf):
                    if e % q == 0:
                        continue
                    if (p + e) % modulus_off_q == 0:
                        r = -e % q
                        full.add(r)
                        if e <= p // 4:
                            reached.add(r)
                            witnesses.setdefault(r, ('II', u, v, e))
                            count_ii += 1
                        else:
                            tail.append(('II', u, v, e, r))
                    if (e * p + 1) % modulus_off_q == 0:
                        r = -pow(e, -1, q) % q
                        full.add(r)
                        if e <= p // 12:
                            reached.add(r)
                            witnesses.setdefault(r, ('I', u, v, e))
                            count_i += 1
                        else:
                            tail.append(('I', u, v, e, r))
        nr = {r for r in range(1, q) if pow(r, (q - 1) // 2, q) == q - 1}
        output[q] = (sorted(nr - reached), sorted(nr - full), count_i, count_ii, tail, witnesses)
    return output


def verify_actual(p, q, witness):
    kind, u, v, e = witness
    if kind == 'II':
        a, b = q * u, v
        c = (a + b) // e
        d = (p + e) // (4 * a * b)
        denominators = (a * b * d, a * c * d * p, b * c * d * p)
    else:
        b, c = q * u, v
        k = (e * p + 1) // (4 * b * c)
        g = k * (b + c) // e
        denominators = (p * b * c * k, g * b, g * c)
    assert min(denominators) > 0
    assert sum((Fraction(1, d) for d in denominators), Fraction()) == Fraction(4, p)
    return denominators


def audit_small():
    p = 100049
    assert prime(p)
    expected = {}
    for line in (ROOT / 'data/z51_forcing/reach/p100049_exact.txt').read_text().splitlines():
        if not line.startswith('#'):
            fields = line.split()
            expected[int(fields[0])] = int(fields[3])
    result = enumerate_reach(p, [q for q in range(3, 61) if prime(q)])
    print('p=100049: q, independently unreached, stored col4, full-definition unreached, I/II tuples')
    for q, (missing, full_missing, ni, nii, tail, _) in result.items():
        print(q, len(missing), expected[q], len(full_missing), ni, nii, 'missing=', missing)
        assert len(missing) == expected[q], (q, missing, expected[q])
    print('16 odd-prime comparisons: PASS')
    tails = [(q, t) for q, row in result.items() for t in row[4]]
    print('Tail tuples beyond declared cutoffs:', len(tails), 'first=', tails[:8])
    interior = [(q, t) for q, t in tails if t[0] == 'I' and t[1] > 1 and t[2] > 1]
    print('Type I tails with BOTH parameters >1:', interior[:8])


def audit_line():
    p, q = 1240009, 17
    assert prime(p)
    signs = [(r, pow(p % r, (r - 1) // 2, r)) for r in (3, 5, 7, 11, 13, 17)]
    assert p % 8 == 1 and all(s == 1 for _, s in signs[:-1]) and signs[-1][1] == 16
    row = enumerate_reach(p, [q])[q]
    missing, full_missing, ni, nii, tail, witnesses = row
    print('p=1240009: n2=17; p mod17=', p % 17, '; missing=', missing, '; full missing=', full_missing)
    assert missing == full_missing == [5] and p % 17 == 12
    print('actual-cell witness:', witnesses[p % q], 'denominators=', verify_actual(p, q, witnesses[p % q]))
    assert p - 1 == 2**3 * 3 * 7 * 11**2 * 61
    for scale in (6, 7, 8):
        rows = []
        for line in (ROOT / f'data/z51_forcing/line17_1e{scale}.txt').read_text().splitlines():
            fields = line.split()
            rows.append({int(x.split(':')[0]): int(x.split(':')[1]) for x in fields[1:] if ':' in x and not x.startswith('#')})
        print('stored line17 aggregate', scale, len(rows), [(r, sum(row[r] == 0 for row in rows)) for r in (13, 17, 19, 23, 29, 31)])


def audit_stored_witnesses():
    counts = {'I': 0, 'II': 0}
    for path in sorted((ROOT / 'data/z51_forcing/reach').glob('*.txt.wit')):
        p = int(path.name.split('_')[0][1:])
        for line in path.read_text().splitlines():
            q, residue, kind, e, u, v = map(int, line.split())
            off = 4*u*v
            assert off*q <= p and u*v*e % q != 0
            n = p + off * ((residue-p) * pow(off, -1, q) % q)
            assert n % q == residue and (q*u+v) % e == 0
            type_name = 'I' if kind == 1 else 'II'
            assert (n+e) % (off*q) == 0 if kind == 2 else (e*n+1) % (off*q) == 0
            verify_actual(n, q, (type_name, u, v, e))
            counts[type_name] += 1
    print('Independently rebuilt stored witness identities:', counts, 'total=', sum(counts.values()))


def audit_generic():
    # At the generic point e=4*u*v*t-1 and q*u+v=c*e,
    # so u=(v+c)/(4*v*t*c-q). Positivity forces v,c <= (q+1)//3,
    # and t <= (q+v+c)//(4*v*c). This is a complete finite search,
    # with NO modulus-size cutoff, for exactly the two families of Def 6.1.
    for q in (3, 5, 7, 11, 13, 17):
        covered = set()
        tuples = []
        for v in range(1, (q+1)//3 + 1):
            for c in range(1, (q+1)//3 + 1):
                for t in range(1, (q+v+c)//(4*v*c) + 1):
                    denominator = 4*v*t*c-q
                    if denominator <= 0 or (v+c) % denominator:
                        continue
                    u = (v+c)//denominator
                    e = 4*u*v*t-1
                    if u*v*e % q == 0:
                        continue
                    assert q*u+v == c*e
                    covered.update((-e % q, -pow(e, -1, q) % q))
                    tuples.append((u, v, e))
        nr = {r for r in range(1,q) if pow(r, (q-1)//2, q) == q-1}
        print('generic two-family reach q=', q, 'covered=', sorted(covered), 'missing NR=', sorted(nr-covered), 'tuples=', tuples)
    # Explicit violation of the asserted globally exact Type-II cutoff p/4.
    p, q, u, v, e = 89, 11, 2, 1, 23
    assert prime(p) and e > p//4 and (q*u+v) % e == 0
    assert 4*q*u*v <= p and (p+e) % (4*u*v) == 0 and u*v*e % q != 0
    print('Type-II cutoff counterexample:', (p,q,u,v,e))


def audit_fits():
    groups = {}
    ratios = []
    bands = {128: [0, 0, 0.0], 256: [0, 0, 0.0]}
    for path in sorted((ROOT / 'data/z51_forcing/reach').glob('*.txt')):
        p = int(path.name.split('_')[0][1:])
        rows = [list(map(float, line.split())) for line in path.read_text().splitlines() if not line.startswith('#')]
        first_hole = next(int(row[0]) for row in rows if row[3] > 0)
        selected = [row[0] * row[7] for row in rows if 11 <= row[0] <= 300]
        supply = sum(selected) / len(selected)
        covered = 0
        rmaj = 0
        for index, row in enumerate(rows, 1):
            covered += row[3] == 0
            if covered / index >= 0.6:
                rmaj = int(row[0])
        scale = int(log(p, 10))
        groups.setdefault(scale, []).append((log(p), first_hole, supply, rmaj))
        ratios.append(supply / log(p)**3)
        if scale == 10:
            for lo, band in bands.items():
                for row in rows:
                    if lo <= row[0] < 2 * lo:
                        band[0] += row[3]
                        band[1] += row[2]
                        band[2] += row[2] * exp(-row[7])
    medians = []
    for scale, rows in sorted(groups.items()):
        values = tuple(median(row[j] for row in rows) for j in range(4))
        medians.append(values)
        print('fit group', scale, len(rows), values)
    xs = [log(v[0]) for v in medians]
    def slope(index):
        ys = [log(v[index]) for v in medians]
        xm, ym = sum(xs)/len(xs), sum(ys)/len(ys)
        return sum((x-xm)*(y-ym) for x,y in zip(xs,ys)) / sum((x-xm)**2 for x in xs)
    print('independent median slopes: supply=', slope(2), 'first-hole=', slope(1))
    print('supply/log^3 range=', min(ratios), max(ratios))
    for lo, (missing, total, predicted) in bands.items():
        print('coupon band', lo, 2*lo, 'observed=', missing/total, 'weighted exp(-lambda)=', predicted/total)
    for L in (200, 1000, 1500):
        print('crossover check L=', L, 'lhs=', .033 * L**.9, 'rhs=', 2.1 * log(L))
    low, high = 200.0, 10000.0
    for _ in range(80):
        mid = (low + high)/2
        if .033 * mid**.9 < 2.1 * log(mid):
            low = mid
        else:
            high = mid
    print('stated crossover equation root L=', high, '; log10(p)=', high/log(10))


if __name__ == '__main__':
    audit_small()
    audit_line()
    audit_generic()
    audit_stored_witnesses()
    audit_fits()
