#!/usr/bin/env python3
"""Independent Python verification: full 1e8 character census, sampled exact caps,
odd-square and numerator-eight controls. Standard library; ~250 MB peak memory.
"""
import argparse
import csv
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
from z51_lcaps_toy import factor


def sieve(n):
    b = bytearray(b'\1')*(n+1)
    b[:2] = b'\0\0'
    for q in range(2, isqrt(n)+1):
        if b[q]:
            b[q*q::q] = b'\0'*((n-q*q)//q+1)
    return b


def ratio_cap(p, q, full, budget):
    f = factor((p+q)//4)
    for e in range(budget+1):
        values = {1}
        for s, b in f.items():
            exps = list(range(-b, b+1))
            if s != 2:
                exps += [b+2*h for h in range(1, e+1)]
            opts = {pow(s, t, q) for t in exps}
            values = {a*c % q for a in values for c in opts}
        targets = {q-1}
        if full:
            targets |= {(-p) % q, (-pow(p, -1, q)) % q}
        if values & targets:
            return e
    raise AssertionError('missing cap')


def divisors_square(k):
    ds = [1]
    for s, b in factor(k).items():
        ds = [d*s**j for d in ds for j in range(2*b+1)]
    return ds


def least_window(p, maxm):
    for m in range(3, maxm+1, 4):
        if gcd(p, m) != 1:
            continue
        K = (p+m)//4
        if any((d+K) % m == 0 for d in divisors_square(K)):
            return m
    return 0


def explicit_witness(p, q):
    K = (p+q)//4
    choices = []
    for s, b in factor(K).items():
        if s == 2 or b % 2 == 0 or pow(s, (q-1)//2, q) != q-1:
            continue
        o = next(j for j in range(1, q) if pow(s, j, q) == 1)
        j = o//2
        h = max(0, (j-b)//2)
        choices.append((h,s,j))
    h,s,j = min(choices)
    d = K*s**j
    assert (K+d) % q == 0
    A = (K+d)//q
    z = Fraction(p*K*A, d)
    assert Fraction(4,p) == Fraction(1,K)+Fraction(1,p*A)+1/z
    assert z.denominator == s**(2*h) and (p*A) % s == 0 and s != p
    assert 4*h <= q-3
    return h


def has_three(m, n):
    # Exhaustive sorted first-denominator/two-term test, not a cap identity.
    for x in range(n//m+1, 3*n//m+1):
        r = Fraction(m,n)-Fraction(1,x)
        A,B = r.numerator,r.denominator
        for d in divisors_square(B):
            if d > B or (B+d) % A:
                continue
            y=(B+d)//A
            if y >= x:
                return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--N', type=int, default=100000000)
    ap.add_argument('--stem', default='1e8')
    args = ap.parse_args()
    root = Path('data/z51_lcaps')
    report = json.loads((root/f'census_{args.stem}.json').read_text())
    b = sieve(args.N)
    assert sum(b) == report['all_primes']
    assert sum(b[1::4]) == report['primes_1mod4']
    remain = [p for p in range(17,args.N+1,8) if b[p]]
    assert len(remain) == report['primes_1mod8']
    hq = {}
    for q in range(3,10000,4):
        if not b[q]:
            continue
        sq = {t*t % q for t in range(1,q)}
        new = [p for p in remain if p % q in sq]
        hit = len(remain)-len(new)
        if hit:
            hq[str(q)] = hit
        remain = new
        if not remain:
            break
    assert hq == report['q3'] and not remain
    independent = (root/f'independent_{args.stem}.txt').read_text().splitlines()
    assert independent[0] == f"count {report['primes_1mod8']}"
    keys = ['q3', 'typeii_cap', 'full_cap', 'oneprime_cap', 'least_typeii_window']
    assert len(independent) == 6
    for key,line in zip(keys,independent[1:]):
        actual = {a:int(b) for a,b in (item.split(':') for item in line.split())}
        if key == 'least_typeii_window' and '0' in actual:
            actual['256'] = actual.pop('0')
        assert actual == report[key], (key,actual)
    rows = list(csv.DictReader((root/f'sample_{args.stem}.csv').open()))
    controls = {193,409,577,2521,3361,5569,9601,66529,8813281,
                23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561}
    seen = [int(row['p']) for row in rows]
    assert len(seen) == len(set(seen))
    assert {p for p in controls if p <= args.N} <= set(seen)
    for rr in rows:
        r = {k:int(v) for k,v in rr.items()}
        p,q,e = r['p'],r['q3'],r['oneprime_cap']
        assert ratio_cap(p,q,False,e) == r['typeii_cap']
        assert ratio_cap(p,q,True,e) == r['full_cap']
        assert explicit_witness(p,q) == e
        assert least_window(p,report['window_limit']) == r['least_typeii_window']
    # T1: both character forcing and the actual Type-II divisor test fail at squares.
    for a in range(3,102,2):
        n=a*a
        for q in [q for q in range(3,152,4) if b[q]]:
            if gcd(n,q)==1:
                assert pow(n,(q-1)//2,q)==1
        assert least_window(n,255)==0
    for n in [17,241]:
        assert not has_three(8,n)
        assert has_three(4,n)
    print(json.dumps(dict(status='PASS', full_character_census=args.N,
                          full_independent_cap_histograms=True,
                          exact_cap_rows=len(rows), odd_squares=50,
                          numerator_eight_controls=[17,241]),indent=2))


if __name__ == '__main__':
    main()
