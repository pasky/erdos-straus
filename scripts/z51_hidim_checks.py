#!/usr/bin/env python3
"""Bounded exact toys and streaming profiles for z51 hidim (stdlib only).
Run: ulimit -v 8000000; timeout 180 uv run python scripts/z51_hidim_checks.py
No product arrays beyond the explicitly capped 2^14 toy cube.
"""
from array import array
from collections import Counter
from fractions import Fraction
from math import exp, isqrt, log, log1p
import json
from pathlib import Path


def prime_table(n):
    spf = array('I', [0]) * (n + 1)
    for p in range(2, n + 1):
        if not spf[p]:
            spf[p] = p
            if p * p <= n:
                for j in range(p * p, n + 1, p):
                    if not spf[j]:
                        spf[j] = p
    return spf


def divisors(n, spf):
    ds = [1]
    while n > 1:
        p = spf[n]
        old = ds[:]
        power = 1
        while n % p == 0:
            n //= p
            power *= p
            ds.extend(d * power for d in old)
    return ds


def in_s(u):
    return u % 4 == 0 or u % 8 == 7


def classes(p, spf):
    return {(-u) % p for u in divisors(p + 1, spf) if in_s(u)}


def entropy_and_support(rows, m):
    # Holder: product-law mass of ANY m atoms is at most this expression.
    best = 0.0
    best_a = None
    for a in (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0):
        v = (a * log(m) + sum(log(p ** (1+a) + (1-p) ** (1+a))
                               for _, p in rows)) / (1+a)
        if v < best:
            best, best_a = v, a
    h = sum(-p * log(p) - (1-p) * log1p(-p) for _, p in rows)
    return {'entropy': h, 'support_log_upper': best,
            'tv_lower': 1-exp(best), 'holder_a': best_a}


def exact_toy(z, nmax, spf):
    local = [(p, classes(p, spf)) for p in range(3, z+1)
             if spf[p] == p and classes(p, spf)]
    assert len(local) <= 14
    # Product probabilities indexed by hit-bit mask; exact rational arithmetic.
    probs = [Fraction(1)]
    for p, f in local:
        rho = Fraction(len(f), p)
        probs = [q*(1-rho) for q in probs] + [q*rho for q in probs]
    counts = Counter()
    sq = 0
    direct_zero = 0
    for n in range(1, nmax+1, 8):
        mask = sum((n % p in f) << j for j, (p, f) in enumerate(local))
        if isqrt(n)**2 == n:
            assert mask == 0
            sq += 1
        else:
            counts[mask] += 1
        # Independent check through the divisibility formulation.
        hits = any((n+u) % p == 0 and p < n+u
                   for p, _ in local for u in range(1, p+2)
                   if (p+1) % u == 0 and in_s(u))
        assert hits == bool(mask)
        direct_zero += not hits
    m = sum(counts.values())
    tv = sum(abs(Fraction(counts.get(i, 0), m)-q)
             for i, q in enumerate(probs))/2
    support_mass = sum(probs[i] for i in counts)
    top_mass = sum(sorted(probs, reverse=True)[:len(counts)])
    assert support_mass <= top_mass
    assert tv >= 1-support_mass
    # Exact Holder a=1: mass(T)^2 <= |T| sum nu(x)^2.
    collision = sum(q*q for q in probs)
    assert support_mass**2 <= len(counts)*collision
    # Collision sum factors, independently of the expanded cube.
    collision_product = Fraction(1)
    for p, f in local:
        q = Fraction(len(f), p)
        collision_product *= q*q+(1-q)**2
    assert collision == collision_product
    return {'z': z, 'N': nmax, 'active_primes': len(local), 'squares': sq,
            'nonsquares': m, 'avoiders': direct_zero, 'nonsquare_avoiders': counts[0],
            'nonsquare_ratio_to_I_V': float(Fraction(counts[0], len(range(1,nmax+1,8)))/probs[0]),
            'actual_tv': float(tv), 'support_size': len(counts),
            'product_mass_of_actual_support': float(support_mass),
            'top_support_mass': float(top_mass),
            **entropy_and_support([(p, len(f)/p) for p, f in local], len(counts))}


def crt(a, q, b, p):
    return a + q * ((b-a)*pow(q, -1, p) % p), q*p


def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n)+1))


def embedding_toy(z, spf):
    local = [(p, classes(p, spf)) for p in range(3,z+1)
             if spf[p] == p and classes(p, spf)]
    k = max(len(f) for _, f in local)
    bs = []
    for i in range(k):
        b, q = 1, 2  # all forms are odd when t is even; no parity obstruction
        for p, f in local:
            roots = sorted((r-1)*pow(8,-1,p) % p for r in f)
            # L_i(t)=t+b_i, assign roots cyclically among forbidden t classes.
            b, q = crt(b, q, -roots[i % len(roots)] % p, p)
        bs.append(b)
    for p, f in local:
        bad = {(r-1)*pow(8,-1,p) % p for r in f}
        roots = {(-b) % p for b in bs}
        assert bad == roots
        assert len(bad) <= k
    prime_tuples = 0
    for t in range(z+1, z+2001):
        if all(is_prime(t+b) for b in bs):
            prime_tuples += 1
            assert all((8*t+1) % p not in f for p, f in local)
    assert prime_tuples > 0
    return {'z': z, 'k': k, 'shifts': bs, 'period': q,
            'prime_tuples_checked': prime_tuples}


def controls(spf):
    hard = [193,409,577,2521,3361,5569,9601,66529,8813281]
    rzeros = [409,577,5569,9601,23929,83449,102001,329617,712321,
              1134241,1724209,1726201,5212561,8813281]
    witnesses = {}
    # Deliberately a bounded prime-modulus search, not a full U assertion.
    for n in sorted(set(hard+rzeros)):
        witness = None
        for p in range(3, min(10000,n+1)+1):
            if spf[p] == p:
                for u in divisors(p+1, spf):
                    if in_s(u) and (n+u) % p == 0:
                        assert p < n+u
                        t, v = (p+1)//u, (n+u)//p
                        assert n == t*u*v-u-v
                        witness = [p,u,t,v]
                        break
            if witness:
                break
        witnesses[n] = witness
    # Exact denominator test for numerator 8, independent of U.
    numerator8 = {}
    for n in [17,241]:
        count = 0
        for x in range(n//8+1, 3*n//8+1):
            f = Fraction(8,n)-Fraction(1,x)
            a,b = f.numerator,f.denominator
            for d in range(1,b+1):
                if b*b % d == 0 and (b+d) % a == 0:
                    y,z = (b+d)//a,(b+b*b//d)//a
                    if x <= y <= z:
                        count += 1
        assert count == 0
        numerator8[n] = count
    return {'prime_U_witnesses_modulus_at_most_10000': witnesses,
            'numerator_8_sorted_solutions': numerator8}


def main():
    maxz = 1000000
    spf = prime_table(maxz+1)
    rows = []
    profiles = []
    points = {100,1000,10000,100000,1000000}
    mass = logv = lam = h = 0.0
    qnr_checks = 0
    for p in range(3,maxz+1):
        if spf[p] == p:
            ds = [u for u in divisors(p+1, spf) if in_s(u)]
            f = {(-u) % p for u in ds}
            assert len(f) == len(ds)
            if p <= 10000:
                for r in f:
                    assert pow(r,(p-1)//2,p) == p-1
                    qnr_checks += 1
            if f:
                rho = len(f)/p
                rows.append((p,rho))
                mass += rho
                logv += log1p(-rho)
                lam += rho*log(p)
        if p in points:
            # No full product cube for large z: sums over one prime at a time.
            profiles.append({'z':p,'mass':mass,'log_V':logv,'Lambda':lam,
                             **entropy_and_support(rows, p)})
    assert classes(13,spf) == {6}
    broad13 = {(-u)%13 for u in divisors(14,spf)
               if in_s(u) or in_s(((1+u)*pow(13,-1,8)) % 8)}
    assert broad13 == {6,11}
    result = {'profiles_support_bound_M_equals_z':profiles,
              'qnr_checks':qnr_checks,
              'toys':[exact_toy(z,n,spf) for z,n in [(13,1001),(31,1001),(43,1001),(43,10001)]],
              'root_embedding':embedding_toy(13,spf),
              'family13':{'direct':[6],'broader':[6,11]},
              'controls':controls(spf)}
    out = Path('data/z51_hidim/checks.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
