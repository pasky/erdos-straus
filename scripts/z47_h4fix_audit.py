#!/usr/bin/env python3
"""Censor regressions, original-row replay, and independent FULL random-hunt audit.
Run under ulimit -v 8000000 and timeout; stores O(saved rows), never all draws.
The full replay independently generates the xorshift stream, tests primality with
SymPy, and detects edges using mutual divisibility/Legendre colours (no slots).
"""
import argparse
from collections import Counter, defaultdict
import csv
import gzip
import io
from itertools import zip_longest
import json
import math
from pathlib import Path
import subprocess
import time

from sympy import isprime
from z46_forest_h4_analyze import (
    THRESHOLDS, OUT, audit_hunt_counts, independent, log_fields, observe, tally,
)

FIELDS = ('family', 'p', 'H', 'u', 't', 'r')
BASELINE = '4cbcd32c'
RESULT = Path('data/z47_h4fix/audit.json')


def run(scanner, *args, input=None):
    p = subprocess.run([scanner, *map(str, args)], input=input, text=True,
                       capture_output=True, check=True, timeout=30)
    return list(csv.DictReader(io.StringIO(p.stdout))), p.stderr


def original_rows():
    result = {}
    for name in ('census', 'hunt', 'qnr'):
        path = OUT / (name + '.csv.gz')
        proc = subprocess.Popen(['git', 'show', f'{BASELINE}:{path}'], stdout=subprocess.PIPE)
        n = 0
        with io.TextIOWrapper(gzip.GzipFile(fileobj=proc.stdout)) as old, gzip.open(path, 'rt') as new:
            for a, b in zip_longest(csv.DictReader(old), csv.DictReader(new)):
                assert a is not None and b is not None, (name, n)
                assert tuple(a[k] for k in FIELDS) == tuple(b[k] for k in FIELDS), (name, n)
                assert b['status'] == 'HIT' and int(b['cap']) == 1000000
                n += 1
        assert proc.wait(timeout=10) == 0
        result[name] = n
    return result


def regressions(scanner):
    # Exercise exhaustion, inclusive cap, and recovery on the same prime.
    below, log = run(scanner, 'input', 4, input='boundary 193\n')
    at, _ = run(scanner, 'input', 5, input='boundary 193\n')
    assert len(below) == len(at) == 1
    assert below[0]['status'] == 'CENSORED' and below[0]['H'] == ''
    assert log_fields(log)['censored'] == '1'
    assert at[0]['status'] == 'HIT' and independent(193, 5) == int(at[0]['H']) == 5

    # Cap 256 counts censored draws in ALL five tails through 256, and retains
    # them even though the missing numeric H would otherwise fail H >= 256.
    rows, text = run(scanner, 'hunt', 256, 50000)
    counts = defaultdict(tally)
    recovered = []
    for row in rows:
        observe(counts[row['family']], row)
        p = int(row['p'])
        assert isprime(p)
        h = independent(p, 1000000)
        assert h
        if row['status'] == 'CENSORED':
            assert h > 256 and independent(p, 256) == 0
            larger, _ = run(scanner, 'input', 100000000, input=f'resolve {p}\n')
            assert larger[0]['status'] == 'HIT' and int(larger[0]['H']) == h
            recovered.append({'family': row['family'], 'p': p, 'cap': 256, 'exact_H': h})
        else:
            assert h == int(row['H'])
    assert recovered, 'regression must actually exercise censorship'
    audit_hunt_counts(text, counts)
    for d in map(log_fields, text.splitlines()):
        assert int(d['censored']) > 0 and int(d['maxH_complete']) == 0
        tails = list(map(int, d['tails16,32,64,128,256,512,1024'].split(',')))
        assert all(t >= int(d['censored']) for t in tails[:5])

    # Corruptions must be rejected: a lost censored row, a hidden censor count,
    # or an aggregate tail inconsistent with the retained records.
    rejected = []
    missing = defaultdict(tally)
    for row in rows[1:]:
        observe(missing[row['family']], row)
    first = log_fields(text.splitlines()[0])
    for name, bad_text, bad_counts in (
        ('dropped_row', text, missing),
        ('hidden_censor', text.replace(f"censored={first['censored']}", 'censored=0', 1), counts),
        ('wrong_kept', text.replace(f"kept={first['kept']}", 'kept=0', 1), counts),
        ('wrong_tail', text.replace(f"1024={first['tails16,32,64,128,256,512,1024']}",
                                   '1024=0,0,0,0,0,0,0', 1), counts),
    ):
        try:
            audit_hunt_counts(bad_text, bad_counts)
        except (AssertionError, KeyError):
            rejected.append(name)
        else:
            raise AssertionError(f'audit accepted {name}')
    # A cap below tail thresholds produces explicit lower bounds, not fake exact tails.
    low, low_text = run(scanner, 'hunt', 4, 3)
    low_counts = defaultdict(tally)
    for row in low:
        observe(low_counts[row['family']], row)
        assert row['status'] == 'CENSORED'
        assert independent(int(row['p']), 1000000) > 4
    audit_hunt_counts(low_text, low_counts)
    return {'boundary_test': 'passed', 'low_cap_draws': len(low),
            'cap256_recoveries': recovered, 'rejected_corruptions': rejected}


def randoms():
    s, mask = 460419, 2**64-1
    while True:
        s ^= (s << 13) & mask
        s ^= s >> 7
        s ^= (s << 17) & mask
        yield s


def full_hunt():
    logs = [log_fields(line) for line in (OUT/'hunt_counts.txt').read_text().splitlines()]
    with gzip.open(OUT/'hunt.csv.gz', 'rt') as f:
        saved = Counter((row['family'], int(row['p']), int(row['H'])) for row in csv.DictReader(f))
    rng = randoms()
    result = []
    for band, base in enumerate((10**12, 10**14)):
        d = logs[band]
        assert int(d['band']) == band and int(d['primes']) == 2000000
        got, candidates, kept, maxh = 0, 0, 0, 0
        tails = [0]*len(THRESHOLDS)
        record = (0, 0, 0)
        while got < int(d['primes']):
            p = base + next(rng) % base
            p += (25 - p % 24) % 24
            candidates += 1
            if not isprime(p):
                continue
            got += 1
            h = independent(p, 1000000)
            assert h, f'independent replay censored at p={p}; resolve at larger cap'
            maxh = max(maxh, h)
            record = max(record, (h/math.log(p)**2, p, h))
            for j, bound in enumerate(THRESHOLDS):
                tails[j] += h > bound
            if h >= 256:
                key = (f'hunt_{band}', p, h)
                assert saved[key] > 0, key
                saved[key] -= 1
                kept += 1
            if got % 250000 == 0:
                print(f'independent band={band} draws={got}', flush=True)
        assert kept == int(d['kept']) and maxh == int(d['maxH'])
        assert int(d['censored']) == 0
        assert tails == list(map(int, d['tails16,32,64,128,256,512,1024'].split(',')))
        result.append({'band': band, 'candidates': candidates, 'prime_draws': got,
                       'kept': kept, 'censored': 0, 'max_H': maxh, 'tails': tails,
                       'max_ratio_record': {'ratio': record[0], 'p': record[1], 'H': record[2]}})
    assert not +saved
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('scanner')
    parser.add_argument('--full-hunt', action='store_true')
    args = parser.parse_args()
    start = time.process_time()
    result = {'baseline': BASELINE, 'unchanged_original_rows': original_rows(),
              'regressions': regressions(args.scanner)}
    if args.full_hunt:
        result['independent_full_hunt'] = full_hunt()
    result['python_cpu_seconds'] = time.process_time() - start
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
