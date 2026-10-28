#!/usr/bin/env python3
"""Independent finite checks for H4_NOT_POLYLOG; O(H²) time, bounded storage.

Reuses z43_astra_check for existing full-forest/fraction controls. The CRT
sampler uses exact Python randrange on finite unit groups (no modulo bias).
"""
import argparse
from fractions import Fraction
from math import gcd, lcm, log
import json
import random

from sympy import divisors, factorint, isprime, jacobi_symbol, primerange, totient
from z43_astra_check import certificates, divisor_edges

EX_EDGE = {(1, 2), (2, 3)}
EX_COVER = {(2, 1), (3, 2)}


def atoms(h):
    edges = [(a*v, (-a-v) % (a*v))
             for v in range(2, h+1) for a in range(1, v)
             if gcd(a, v) == 1 and (a, v) not in EX_EDGE]
    cover = [(a, (-int(d)) % a) for a in range(2, h+1)
             for d in divisors(a+1) if d < a and (a, int(d)) not in EX_COVER]
    return sorted(set(edges+cover))


def parent_edges(n, h):
    out = set()
    for v in range(2, h+1):
        a = (-n) % v
        if a and (n+a+v) % (a*v) == 0:
            out.add((a, v))
    return out


def smooth(n, y):
    return all(q <= y for q in factorint(n))


def smooth_modulus(h, y):
    out = 1
    for q in primerange(2, y+1):
        power = q*q
        z = q
        while z <= h:
            power *= q
            z *= q
        out *= power
    return out


def checks():
    out = {}
    # These are the new gcd identities, not tests restating a configuration.
    count = 0
    for a in range(1, 251):
        for v in range(a+1, 251):
            s = a+v+1
            assert gcd(a*v, s) == gcd(a*(a+1), s)
            count += 1
    for d in range(1, 251):
        for k in range(1, 251):
            if d*k >= 3:
                assert gcd(d*k-1, d+1) == gcd(d+1, k+1)
                count += 1
    out['gcd_identities'] = count
    masses = []
    for h in (16, 32, 64, 128, 256, 512):
        e = sum(gcd(a*v, a+v+1)/(a*v)
                for v in range(2, h+1) for a in range(1, v))
        c = sum(gcd(a, int(d)+1)/a for a in range(2, h+1)
                for d in divisors(a+1) if d < a)
        masses.append({'H': h, 'edge_g_mass': e, 'cover_g_mass': c,
                       'edge_over_log4': e/log(3*h)**4,
                       'cover_over_log3': c/log(3*h)**3})
    out['mass_evidence'] = masses
    # Compare two genuinely different edge enumerations with the congruences.
    aa = atoms(32)
    comparisons = 0
    for n in range(1, 20000, 24):
        if any(n % q == 0 for q in primerange(2, 33)):
            continue
        brute = {(a, v) for v in range(2, 33) for a in range(1, v)
                 if (n+a+v) % (a*v) == 0}
        assert parent_edges(n, 32) == brute
        edge_hit = any((a, v) not in EX_EDGE for a, v in brute)
        cover_hit = any(n % a == (-int(d)) % a
                        for a in range(2, 33) for d in divisors(a+1)
                        if d < a and (a, int(d)) not in EX_COVER)
        assert any(n % m == b for m, b in aa) == (edge_hit or cover_hit)
        comparisons += 1
    assert all(1 % m != b for m, b in atoms(128))
    out['independent_atom_comparisons'] = comparisons
    fixtures = []
    for h, y in ((4, 3), (8, 3), (12, 5), (24, 5), (40, 7)):
        mod = smooth_modulus(h, y)
        start = max(1, h*h//mod+1)
        primes = []
        for k in range(start, start+10000):
            p = 1+mod*k
            if isprime(p):
                ee = parent_edges(p, h)
                brute = {(a, v) for v in range(2, h+1) for a in range(1, v)
                         if (p+a+v) % (a*v) == 0}
                assert ee == brute
                assert {e for e in ee if all(smooth(z, y) for z in e)} == EX_EDGE
                assert all(not list(certificates(p, *e)) for e in EX_EDGE)
                primes.append(p)
                if len(primes) == 10:
                    break
        assert len(primes) == 10
        fixtures.append({'H': h, 'Y': y, 'L': mod, 'primes': primes})
    out['smooth_actual_prime_fixtures'] = fixtures
    # Exercise the even-coordinate extension and the adaptive charging rule.
    quarantine = []
    for h in (16, 32, 64):
        events = atoms(h)
        fac = {m: factorint(m) for m, _ in events}
        phi = {m: int(totient(m)) for m, _ in events}
        q = 840
        steps = []
        while True:
            masses_by_prime = {}
            live = []
            for m, b in events:
                g = gcd(m, q)
                if (b-1) % g:
                    continue
                assert m % g == 0 and g != m
                prob = Fraction(int(totient(g)), phi[m])
                assert prob <= Fraction(gcd(m, b-1), phi[m])
                support = [ell for ell, v in fac[m].items()
                           if q % (ell**v)]
                live.append((prob, support))
                for ell in support:
                    masses_by_prime[ell] = masses_by_prime.get(ell, Fraction())+prob
            bad = None
            for ell in sorted(masses_by_prime):
                power, exp = ell, 0
                while q % power == 0:
                    power *= ell
                    exp += 1
                if float(masses_by_prime[ell]) > (exp+1)*log(ell)/(64*log(h*h)):
                    bad = ell
                    break
            if bad is None:
                break
            steps.append(int(bad))
            q *= bad
        for _, support in live:
            assert sum((masses_by_prime[z] for z in support), Fraction()) <= Fraction(1, 64)
        quarantine.append({'H': h, 'Q': int(q), 'steps': steps,
                           'residual_events': len(live),
                           'residual_mass': float(sum((z[0] for z in live), Fraction()))})
    # Nontrivial even-prime interface: the starting 2^3 does not decide mod16.
    assert Fraction(int(totient(gcd(16, 840))), int(totient(16))) == Fraction(1, 2)
    assert 9 % 8 == 1 and 9 % 16 != 1
    out['graded_quarantine'] = quarantine
    controls = []
    for p in (17, 241, 193, 409, 577, 2521, 3361, 5569, 9601, 66529, 8813281):
        ee = divisor_edges(p)
        good = [e for e in ee if list(certificates(p, *e))]
        h4 = min(v for _, v in good)
        assert parent_edges(p, h4) == {e for e in ee if e[1] <= h4}
        amin = None
        for a in range(2, p+1):
            d = (-p) % a
            odd = a
            while odd % 2 == 0:
                odd //= 2
            if d and (a+1) % d == 0 and jacobi_symbol(-d, odd) == -1:
                amin = a
                break
        assert amin is not None
        # Full-forest identities are already tested in z43, so only reuse them.
        if p in (17, 241):
            assert all(not list(certificates(p, *e, 8)) for e in ee)
        controls.append({'p': p, 'H4': h4, 'A_min': amin, 'edges': len(ee)})
    out['hard_prime_and_numerator8_controls'] = controls
    return out


def model(samples):
    rng = random.Random(490049)
    out = []
    for h in (64, 128, 256):
        cover = {}
        for a in range(2, h+1):
            odd = a
            while odd % 2 == 0:
                odd //= 2
            cover[a] = {(-int(d)) % a for d in divisors(a+1)
                        if d < a and jacobi_symbol(-int(d), odd) == -1}
        # Full powers needed for the slot test modulo 4av, a,v coprime.
        mm = lcm(24, *(4*a for a in range(1, h+1)))
        pp = [(int(q), int(q**e)) for q, e in factorint(mm).items()]
        coefficients = [(mm//power)*pow(mm//power, -1, power) for _, power in pp]
        for y in (0, 3, 5, 7, 13):
            edge_surv = slot_surv = cover_surv = joint_surv = 0
            for _ in range(samples):
                residues = []
                for q, power in pp:
                    if q <= y:
                        r = 1
                    elif q == 2:
                        r = 1+8*rng.randrange(power//8)
                    elif q == 3:
                        r = 1+3*rng.randrange(power//3)
                    else:
                        r = rng.randrange(1, power)
                        while r % q == 0:
                            r = rng.randrange(1, power)
                    residues.append(r)
                n = sum(c*r for c, r in zip(coefficients, residues)) % mm
                ee = parent_edges(n, h)
                noedge = not (ee-EX_EDGE)
                noslot = True
                for a, v in ee:
                    t = (n+a+v)//(a*v)
                    if any(z % 4 == 0 for z in (t, a, v, t*a-1, t*v-1)):
                        noslot = False
                        break
                nocover = not any(n % a in rr for a, rr in cover.items())
                noshadow = all((d := (-n) % a) == 0 or (a+1) % d != 0
                               or (a, d) in EX_COVER for a in range(2, h+1))
                if noedge:
                    assert noslot
                if noshadow:
                    assert nocover
                edge_surv += noedge
                slot_surv += noslot
                cover_surv += nocover
                joint_surv += noedge and noshadow
            out.append({'H': h, 'Y_forced_to_1': y, 'samples': samples,
                        'no_nontrivial_edge': edge_surv, 'H4_gt_H': slot_surv,
                        'A_min_gt_H': cover_surv, 'joint_shadow_survival': joint_surv})
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--samples', type=int, default=10000)
    parser.add_argument('--mode', choices=('checks', 'model', 'all'), default='all')
    args = parser.parse_args()
    result = {}
    if args.mode != 'model':
        result['checks'] = checks()
    if args.mode != 'checks':
        result['model_evidence'] = model(args.samples)
    print(json.dumps(result, indent=2))
