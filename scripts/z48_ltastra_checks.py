"""Independent finite checks of the new Fourier/kernel assertions.
Reuse existing line and genus verifiers rather than duplicate those tests.
Memory bounded: largest DFT is 128x128; group images are built one q at a time.
"""
import csv
import json
import math
from pathlib import Path
from fractions import Fraction

import numpy as np
from sympy import divisors, factorint, isprime, jacobi_symbol, totient
from s8_check_b1 import b1_solutions, c1_solutions, line_counts_k
from z30_check_forms import Mg

DATA = Path(__file__).resolve().parents[1] / 'data/z48_ltastra'


def load(path):
    with path.open() as f:
        return list(csv.DictReader(line for line in f if not line.startswith('#')))


def main():
    report = {}
    rng = np.random.default_rng(480045)
    tests = 0
    for n in range(2, 129):
        grid = np.arange(n)
        chars = np.exp(-2j * np.pi * np.outer(grid, grid) / n)
        delta = np.zeros(n)
        delta[0] = 1
        for _ in range(20):
            slack = rng.random(n)
            slack *= rng.uniform(.01, .99) / slack.sum()
            f = delta - slack
            coeff = chars @ f / n
            mu = f.mean()
            assert mu > 0
            assert np.min(np.abs(coeff)) >= mu - 2e-13
            assert np.abs(coeff).sum() >= n * mu - 2e-12
            tests += 1
        # Fejer peak normalized to 1; subtract the largest off-target value.
        for j in range(1, n):
            kernel = np.abs(chars[:j].sum(axis=0) / j)**2
            c = kernel[1:].max()
            if c >= 1 - 1e-12:
                continue
            f = (kernel - c) / (1 - c)
            assert np.max(f[1:]) <= 1e-12
            assert abs(f[0] - 1) < 1e-12
            if 2*j - 1 < n:
                assert f.mean() <= 1e-12
            if j == n - 1:
                assert np.max(np.abs(f - delta)) < 1e-10
            tests += 1
    report['cyclic_minorant_and_fejer_checks'] = tests

    # Compressed positive kernel: full Fourier support from just five amplitudes.
    S = [0, 1, 4, 14, 16]
    differences = [(a-b)%21 for a in S for b in S if a != b]
    assert sorted(differences) == list(range(1,21))
    amplitudes = np.array([sum(np.exp(2j*np.pi*s*x/21) for s in S) for x in range(21)])
    expected = np.full(21,4.0)
    expected[0] = 25
    assert np.max(np.abs(np.abs(amplitudes)**2-expected)) < 1e-11
    H344 = {x*x%344 for x in range(344) if math.gcd(x,344) == 1}
    g344 = 409*pow(257,-1,344)%344
    assert len(H344) == 21 and g344 == 193 and pow(9,18,344) == g344
    assert abs(abs(amplitudes[18])**2-4) < 1e-11
    report['compressed_difference_set'] = {'h':21, 'S':S, 'q':344, 'p':409,
        'target':257, 'g':g344, 'log_base_9':18, 'squared_amplitude':4}

    detail = {int(r['n']): r for r in load(DATA / 'detail.csv')}
    # Direct kth-power IMAGE sets, independent of the C prime-power criterion.
    direct = {}
    for n in (193, 409, 577):
        totals = {k: Fraction() for k in (2, 6, 12, 60)}
        mbm = Fraction()
        for u in range(1, (n+1)//3 + 1):
            for v in range(1, (n+u)//(4*u-1) + 1):
                if (u+v)%2 == 0 or math.gcd(u,v) > 1:
                    continue
                q = 4*u*v
                units = [a for a in range(1,q) if math.gcd(a,q) == 1]
                g = n * pow(-(u+v), -1, q) % q
                for k in totals:
                    image = {pow(a,k,q) for a in units}
                    if g in image:
                        totals[k] += Fraction(1,len(image))
                mbm += Fraction(1-int(jacobi_symbol(-u*v,n)),len(units))
        r = detail[n]
        assert abs(float(mbm)-float(r['MBM'])) < 1e-9
        assert abs(float(Mg(n))-float(r['Mgen'])) < 1e-9
        for k, value in totals.items():
            assert abs(float(value)-float(r[f'M{k}small'])) < 1e-9
        direct[n] = {str(k): str(value) for k,value in totals.items()}
    report['exact_power_image_sums'] = direct

    # Concrete BM/genus-allowed nonhit: H has order 3, r has order 3.
    q, p, a = 56, 409, 41
    H = {pow(x,2,q) for x in range(1,q) if math.gcd(x,q) == 1}
    g = p*pow(a,-1,q)%q
    assert H == {1,9,25} and g == 25 and pow(g,3,q) == 1 and g != 1
    report['q56_nonhit'] = {'p': p, 'target': a, 'g': g, 'H': sorted(H)}

    census = {int(r['p']): r for r in load(DATA / 'census.csv')}
    for p,r in census.items():
        assert 16*int(r['T']) >= float(r['MBM_upper']), (p,r)
        if p in detail:
            assert float(detail[p]['MBM']) <= float(r['MBM_upper'])
    report['uniform_union_bound'] = {'epsilon':'1/16', 'primes':len(census),
        'method':'MBM <= outward-rounded 2*sum_even_m<=((p+1)/3) 2^omega(m)/(4*phi(m))'}
    # Independently compare the outward bound to exact rational sums at small inputs.
    for p in (193,409,577):
        exact = sum((Fraction(2**len(factorint(m)),2*int(totient(m)))
            for m in range(2,(p+1)//3+1,2)), Fraction())
        assert Fraction.from_float(float(census[p]['MBM_upper'])) >= exact
    hard = [p for p,r in census.items() if int(r['R']) == 0 or int(r['B']) == 0]
    for p in hard:
        assert len(b1_solutions(p)) == int(census[p]['B']), p
        if p < 100000:
            assert len(c1_solutions(p)) == int(census[p]['R']), p
    report['existing_b1_verifier_hard_primes'] = hard
    large = []
    for line in (DATA / 'large_counts.txt').read_text().splitlines():
        p,b,half_r,big = map(int,line.split())
        assert isprime(p) and p%24 == 1
        if p in census:
            assert (2*half_r,b) == (int(census[p]['R']),int(census[p]['B']))
        else:
            t = 2*half_r+b
            assert p < 2**40 and 16*t > 2*29**2
            large.append({'p':p,'R':2*half_r,'B':b,'T':t,
                'near_square_gap':p-math.isqrt(p)**2})
    report['large_prime_counts'] = large
    # Numerator-8 controls use the existing general-numerator enumerator.
    report['numerator8'] = {}
    for p in (11,17,131,241):
        counts = line_counts_k(p,8)
        assert counts == (0,0), (p,counts)
        report['numerator8'][p] = counts

    # Verify every published zero-envelope residue directly against the finite menu.
    zero_checks = 0
    for path in sorted(DATA.glob('cover_*.csv')):
        Q = int(path.stem.split('_')[1])
        star, second = [], []
        for m in divisors(Q//4):
            q = 4*m
            for u in divisors(m):
                v = m//u
                if math.gcd(u,v) == 1 and (u+v)%2:
                    star.append((q,(-u-v)%q))
            for y in divisors(m):
                x = m//y
                if y >= 3 and y%4 == 3 and math.gcd(x,y) == 1:
                    second.append((q,(-4*x-y)%q))
        for row in load(path):
            if int(row['minT']) != 0:
                continue
            r = int(row['argminT'])
            assert r%24 == 1 and math.gcd(r,Q) == 1
            assert not any(r%q == a for q,a in star+second), (Q,r)
            zero_checks += 1
    report['independent_zero_envelope_witnesses'] = zero_checks
    (DATA / 'checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PASS:', tests, 'Fourier checks;', len(hard), 'hard-prime B counts;',
          zero_checks, 'global zero-envelope witnesses')


if __name__ == '__main__':
    main()
