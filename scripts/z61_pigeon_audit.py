#!/usr/bin/env python3
"""Independent exact-integer PIGEON audit; stdlib only, streaming per integer.
Run under ulimit -v 4000000 and timeout 1800; see Z61_PIGEON.md.
The census is complete in rho, not merely the board's rho <= 400 scan.
"""
import argparse
from array import array
import csv
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/z61/pigeon'


class Arithmetic:
    def __init__(self, limit):
        self.spf = array('I', range(limit + 1))
        for q in range(2, isqrt(limit) + 1):
            if self.spf[q] == q:
                for j in range(q*q, limit + 1, q):
                    if self.spf[j] == j:
                        self.spf[j] = q
        self.primes = [q for q in range(2, limit + 1) if self.spf[q] == q]
        self.phis = array('I', range(limit + 1))
        for q in self.primes:
            for j in range(q, limit + 1, q):
                self.phis[j] -= self.phis[j] // q

    def factors(self, n):
        result = []
        if n >= len(self.spf):
            assert isqrt(n) < len(self.spf), 'trial-prime table too short'
            for q in self.primes:
                if q*q > n:
                    break
                if n % q == 0:
                    e = 0
                    while n % q == 0:
                        n //= q
                        e += 1
                    result.append((q, e))
        while n > 1:
            q = self.spf[n] if n < len(self.spf) else n
            e = 0
            while n % q == 0:
                n //= q
                e += 1
            result.append((q, e))
        return result

    def divisors(self, n):
        ds = [1]
        for q, e in self.factors(n):
            base = ds[:]
            power = 1
            for _ in range(e):
                power *= q
                ds.extend(d*power for d in base)
        return ds

    def phi(self, n):
        if n < len(self.phis):
            return self.phis[n]
        value = n
        for q, _ in self.factors(n):
            value -= value // q
        return value

    def prime(self, n):
        return n >= 2 and self.factors(n) == [(n, 1)]


def direct(ar, n, rho, even_d=False):
    """Enumerate ab | M independently of the residue-intersection shortcut."""
    m = (n + rho) // 4
    if even_d:
        if m % 2:
            return None
        m //= 2
    for a in sorted(ar.divisors(m)):
        for b in sorted(ar.divisors(m // a)):
            if b >= a and (a+b) % rho == 0:
                d = m // (a*b) * (2 if even_d else 1)
                w = [a, b, (a+b)//rho, d]
                assert 4*a*b*w[2]*d == a+b+n*w[2]
                return w
    return None


def level(ar, n, rho):
    ds = ar.divisors((n+rho)//4)
    reps = {}
    for d in sorted(ds):
        if gcd(d, rho) == 1:
            reps.setdefault(d % rho, d)
    collision = sorted(s for s in reps if (-s) % rho in reps)
    ph = 2*len(reps) > ar.phi(rho)
    w = None
    if collision:
        u, v = reps[collision[0]], reps[(-collision[0]) % rho]
        g = gcd(u, v)
        a, b = sorted((u//g, v//g))
        m = (n+rho)//4
        assert m % (a*b) == 0
        w = [a, b, (a+b)//rho, m//(a*b)]
        assert 4*a*b*w[2]*w[3] == a+b+n*w[2]
    assert not ph or w is not None
    return {'occupancy': len(reps), 'phi': ar.phi(rho), 'ph': ph,
            'collision': collision, 'unit_witness': w}


def linnik_fixture(ar, p):
    """Least prime in the patched AP, not a claimed Type II witness level."""
    q = next(k for k in range(2, p) if pow(k, (p-1)//2, p) == p-1)
    assert ar.prime(q)
    rho = (-p) % (4*q)
    while not ar.prime(rho):
        rho += 4*q
    m = (p+rho)//4
    assert m % q == 0 and pow(q, (rho-1)//2, rho) == rho-1
    return {'p': p, 'n_p': q, 'rho_L': rho, 'M': m,
            'factors_M': ar.factors(m), 'level': level(ar, p, rho)}


def save(name, data):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/name).write_text(json.dumps(data, indent=2) + '\n')


def check(ar):
    # Existing z59 checks cover the original equation, but not the new gcd
    # reduction, half-density implication, or nonunit prime-level alternative.
    checked = 0
    for n in range(1, 2002, 4):
        for rho in range(3, (n+4)//3 + 1, 4):
            x = level(ar, n, rho)
            w = direct(ar, n, rho)
            if x['unit_witness']:
                assert w is not None
            if ar.prime(rho):
                assert bool(w) == (bool(x['collision']) or (n+rho)//4 % (rho*rho) == 0)
            if isqrt(n)**2 == n:
                assert w is None and not x['ph']
            checked += 1
    # Direct factor-colour comparison includes the p == 5 (mod 8), ell=2 case.
    colours = 0
    for p in ar.primes:
        if p > 2000:
            break
        if p % 4 != 1:
            continue
        q = next(k for k in range(2, p) if pow(k, (p-1)//2, p) == p-1)
        assert ar.prime(q)
        r = (-p) % (4*q)
        while not ar.prime(r):
            r += 4*q
        assert (p+r)//4 % q == 0 and pow(q, (r-1)//2, r) == r-1
        for rho in range(3, 400, 4):
            if not ar.prime(rho):
                continue
            for ell, _ in ar.factors((p+rho)//4):
                assert pow(ell, (p-1)//2, p) in (1, p-1)
                assert (pow(ell, (p-1)//2, p) == 1) == (pow(ell, (rho-1)//2, rho) == 1)
                colours += 1
    result = {'levels_checked': checked, 'factor_colour_checks': colours,
              'status': 'all exact assertions passed'}
    save('checks.json', result)
    print(json.dumps(result))


def census(ar, limit, cutoff):
    rows, missing = [], []
    for p in ar.primes:
        if p > limit:
            break
        if p % 24 != 1:
            continue
        first, firstph, occupancy, totient = None, None, None, None
        for rho in range(3, min(cutoff, (p+4)//3)+1, 4):
            x = level(ar, p, rho)
            if first is None:
                w = direct(ar, p, rho)
                assert bool(w) == bool(x['collision'])
                if w:
                    first, occupancy, totient = rho, x['occupancy'], x['phi']
            if x['ph']:
                firstph = rho
                break
        assert first is not None, f'increase first-witness cutoff at {p}'
        cutoff_missing = firstph is None
        if cutoff_missing:
            for rho in range(3 + 4*((cutoff+1)//4), (p+4)//3+1, 4):
                if level(ar, p, rho)['ph']:
                    firstph = rho
                    break
            missing.append({'p': p, 'rho_star': first, 'rho_ph': firstph,
                            'complete_bound': (p+4)//3})
        rows.append({'p': p, 'rho_star': first, 'rho_ph': firstph,
                     'occupancy_at_star': occupancy, 'phi_at_star': totient,
                     'ph_at_star': 2*occupancy > totient})
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT/'census.csv').open('w') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    hard = [r for r in rows if r['rho_star'] >= 50]
    summary = {'limit': limit, 'initial_cutoff': cutoff, 'count': len(rows),
               'ph_at_star': sum(r['ph_at_star'] for r in rows),
               'hard': hard, 'no_ph_below_cutoff_extended_completely': missing,
               'no_ph_anywhere': [r['p'] for r in missing if r['rho_ph'] is None]}
    save('census_summary.json', summary)
    print(json.dumps(summary, indent=2))


def screens(ar):
    results = []
    for name in ('star_prime_zeros.txt', 'gstar_zeros.txt',
                 'composite_zeros_le8e6.txt', 'r8_zeros_1e10.txt'):
        path = ROOT/'data/z58/screens'/name
        nums = [int(line.split()[0]) for line in path.read_text().splitlines()
                if line and not line.startswith('#')]
        for n in nums:
            row = {'screen': name, 'n': n, 'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
            bound = (n+4)//3
            for rho in range(3, min(bound, 1200)+1, 4):
                w = direct(ar, n, rho)
                if w:
                    row.update(rho=rho, witness=w, level=level(ar, n, rho))
                    break
            if 'witness' not in row:
                assert n == 4545
                assert all(direct(ar, n, r) is None for r in range(3, bound+1, 4))
                row['exhaustive_zero_bound'] = bound
            if name == 'star_prime_zeros.txt' and 'witness' in row:
                assert row['witness'][2] >= 2
            if name == 'r8_zeros_1e10.txt':
                for rho in range(3, 1201, 4):
                    w = direct(ar, n, rho, even_d=True)
                    if w:
                        assert w[2] >= 2 and w[3] % 2 == 0
                        row.update(even_d_rho=rho, even_d_witness=w)
                        break
                assert 'even_d_witness' in row
            results.append(row)
    fixtures = []
    for n in (105, 4545, 67369, 87481, 8803369):
        # Exhaustive for 105/4545; census handles the prime PH absences.
        bound = (n+4)//3 if n in (105, 4545) else 1200
        ph = next((r for r in range(3, bound+1, 4) if level(ar, n, r)['ph']), None)
        first = next((r for r in range(3, bound+1, 4) if direct(ar, n, r)), None)
        fixtures.append({'n': n, 'bound': bound, 'rho_ph': ph, 'rho_star': first,
                         'witness': direct(ar, n, first) if first else None,
                         'level_at_star': level(ar, n, first) if first else None})
    linnik = [linnik_fixture(ar, p) for p in
              (5, 13, 17, 193, 601, 2521, 67369, 87481, 8803369)]
    save('screens.json', results)
    save('fixtures.json', fixtures)
    save('linnik_fixtures.json', linnik)
    summary = {}
    for name in sorted({r['screen'] for r in results}):
        group = [r for r in results if r['screen'] == name]
        summary[name] = {'count': len(group),
                         'hits': sum('witness' in r for r in group),
                         'ph_at_first': sum(r.get('level', {}).get('ph', False) for r in group),
                         'max_rho_star': max(r.get('rho', 0) for r in group),
                         'max_even_d_rho': max(r.get('even_d_rho', 0) for r in group)}
    save('screen_summary.json', summary)
    print(json.dumps({'summary': summary, 'fixtures': fixtures}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('check', 'census', 'screens'))
    parser.add_argument('--limit', type=int, default=2_000_000)
    parser.add_argument('--cutoff', type=int, default=400)
    args = parser.parse_args()
    arithmetic = Arithmetic(max(args.limit, 100_000))
    if args.mode == 'check':
        check(arithmetic)
    elif args.mode == 'census':
        census(arithmetic, args.limit, args.cutoff)
    else:
        screens(arithmetic)
