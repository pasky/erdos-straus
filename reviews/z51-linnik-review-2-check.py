"""Independent bounded checks for review 2; no project-code imports.
Run: ulimit -v 8000000; timeout 180 uv run --no-project python3 reviews/z51-linnik-review-2-check.py
Optional --runs reads the supplied-program outputs in /tmp/z51-r2-*.
Trial division and streamed loops only; no large arrays or Cartesian products.
"""
from math import isqrt, log
import json
import sys


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def divisors(n):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def leg(a, q):
    t = pow(a % q, (q - 1) // 2, q)
    return -1 if t == q - 1 else t


def window_check():
    count = live = 0
    for p in range(5, 201, 4):
        if not prime(p):
            continue
        for q in range(3, 101, 4):
            if not prime(q):
                continue
            x = (p + q) // 4
            B = p * x
            ds = divisors(B)
            residues = {d % q for d in ds}
            criterion = any((-a) % q in residues for a in residues)
            # Exhaustive direct search: order y <= z, hence B/q < y <= 2B/q.
            direct = False
            for y in range(B // q + 1, 2 * B // q + 1):
                den = q * y - B
                if B * y % den == 0:
                    z = B * y // den
                    assert y <= z
                    assert 4 * x * y * z == p * (y * z + x * z + x * y)
                    direct = True
                    break
            assert direct == criterion, (p, q, direct, criterion)
            count += 1
            live += direct
    print('window direct-y search:', dict(cases=count, live=live, disagreements=0))
    # A prescribed cap-0 window is a strengthening, not a relaxation of ES.
    assert all((a+b) % 7 for a in divisors(15) for b in divisors(15))
    assert 4*2*4*20 == 5*(4*20 + 2*20 + 2*4)
    print('orientation example: p=5 has ES (2,4,20), but window q=7 has no cap-0 solution.')


def all_plane_labels(q):
    """Complete finite parametrization, not a scan with an empirical m cutoff.
    Sort k<=k'. Then k<=q+2, and m=(k+k'+2q)/(kk'-q^2).
    For k>=2, m>=1 implies (k-1)(k'-1)<=(q+1)^2.
    For k=1, (m-1)(k'-q^2)=(q+1)^2.
    Retain divisibility by 4 and the original class restrictions.
    """
    labels = set()
    for k in range(1, q + 3):
        ks = (q*q + d for d in divisors((q+1)**2)) if k == 1 else range(k, (q+1)**2 // (k-1) + 2)
        for kp in ks:
            den, num = k * kp - q*q, k + kp + 2*q
            if den <= 0 or num % den:
                continue
            m = num // den
            if m < 1 or m % q == 0 or q*m % 4 != 3:
                continue
            if (k*m-1) % 4 or (kp*m-1) % 4:
                continue
            D, Dp = (k*m-1)//4, (kp*m-1)//4
            if min(D, Dp) < 1:
                continue
            A = (q*m+1)//4
            assert D*Dp == A*A
            assert (1+4*D) % m == (1+4*Dp) % m == 0
            for d in (D, Dp):
                assert leg(-4*d, q) == -1
                labels.add((q*m, d))
    return labels


def plane_check():
    cache = {}
    for q in range(3, 301, 2):
        if not prime(q):
            continue
        exact = all_plane_labels(q)
        cache[q] = exact
        # Independent original-definition enumeration at small pivots.
        brute = set()
        for m in range(1, 5000//q + 1):
            M = q*m
            if m % q == 0 or M % 4 != 3:
                continue
            A = (M+1)//4
            for D in divisors(A*A):
                if (1+4*D) % m == 0:
                    brute.add((M, D))
        assert brute == {(M, D) for M, D in exact if M <= 5000}, q
    chosen = {q: lab for q, lab in cache.items() if q >= 25}
    print('plane complete enumeration:', dict(primes=len(cache),
          mean_labels_q25_300=sum(map(len, chosen.values()))/len(chosen),
          maximum_pivot=max(M for lab in chosen.values() for M, _ in lab),
          residue_hits=0))
    for lo, hi in ((25,50), (50,100), (100,150), (150,200), (200,300)):
        qs = [q for q in chosen if lo <= q < hi]
        print('plane band', lo, hi, sum(len({(-4*D)%q for _,D in chosen[q]}) for q in qs)/sum((q-1)//2 for q in qs))
    return cache


def compare_runs(cache):
    for mode in (0,1):
        with open(f'/tmp/z51-r2-forcing-{mode}.txt') as f:
            rows = [{k:int(v) for k,v in (field.split('=') for field in line.split())} for line in f if line.startswith('q=')]
        if mode == 1:
            for row in rows:
                q = row['q']
                labels = {(M,D) for M,D in cache[q] if M <= 1000609}
                hit = {(-4*D)%q for _,D in labels}
                assert row['labels'] == len(labels)
                assert row['reached'] == len(hit)
                assert row['residues_hit'] == 0
        labels = [r['labels'] for r in rows if r['q'] >= 25]
        mean = sum(labels)/len(labels)
        print('supplied forcing mode', mode, 'mean_labels', mean, 'ratio_log3', mean/log(1000609)**3,
              'first_hole', next(r['q'] for r in rows if r['reached']<r['nonres']))
        for lo,hi in ((25,50),(50,100),(100,120)):
            rs = [r for r in rows if lo <= r['q'] < hi]
            print('  band',lo,hi,sum(r['reached'] for r in rs)/sum(r['nonres'] for r in rs))
    with open('/tmp/z51-r2-windows.json') as f:
        data = json.load(f)
    print('supplied windows mean forced/unforced:', *(sum(data[key].values())/len(data[key]) for key in ('rho_forced','rho_unforced')))


if __name__ == '__main__':
    window_check()
    labels = plane_check()
    if '--runs' in sys.argv:
        compare_runs(labels)
    print('PASS: all independent finite checks and exact plane parametrization assertions.')
