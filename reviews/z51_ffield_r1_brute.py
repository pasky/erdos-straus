#!/usr/bin/env python3
"""Independent divisor/shift audit; no word-map enumeration.

Run: ulimit -v 8000000; timeout 240s uv run --no-project \
    reviews/z51_ffield_r1_brute.py --engine /tmp/rev_enum

Only prime fields F_3 and F_7, degrees 2..5. Build the full proper
monic divisor table by ordinary multiplication A*Q. For each monic f,
scan monic shifts v of degree < n and the actual divisors of f+v,
testing A+1 mod v directly. Stop at the first witness unless --full-scan.
Space is O(n*q^n) small tuples, never a Cartesian-product array.
"""
import argparse
import itertools
import re
import subprocess
import time


def monics(q, d):
    # Coefficients in ascending order, enumeration agrees with base-q encoding.
    return [tuple(reversed(c)) + (1,) for c in itertools.product(range(q), repeat=d)]


def multiply(a, b, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % q
    return tuple(out)


def encode(coeffs, q):
    ans = 0
    for x in reversed(coeffs):
        ans = ans * q + x
    return ans


def minus_one_mod(a, v, q):
    # a is monic, v is monic (possibly 1). Test v | a+1.
    r = list(a)
    r[0] = (r[0] + 1) % q
    b = len(v) - 1
    for i in range(len(r) - 1, b - 1, -1):
        c = r[i]
        if c:
            for j, x in enumerate(v):
                r[i - b + j] = (r[i - b + j] - c * x) % q
    return not any(r[:b])


def audit(q, n, full_scan):
    polys = [monics(q, d) for d in range(n + 1)]
    divisors = [[] for _ in range(q ** n)]
    for d in range(1, n):
        for a in polys[d]:
            for cofactor in polys[n - d]:
                h = multiply(a, cofactor, q)
                divisors[encode(h[:-1], q)].append(a)
    # Each divisor occurs once (unique monic cofactor); table contains all of them.
    assert sum(map(len, divisors)) == (n - 1) * q ** n
    squares = set()
    if n % 2 == 0:
        squares = {encode(multiply(g, g, q)[:-1], q) for g in polys[n // 2]}
    assert len(squares) == (q ** (n // 2) if n % 2 == 0 else 0)
    shifts = [(b, v) for b in range(n) for v in polys[b]]
    failures = []
    shift_checks = 0
    for f_id, f in enumerate(polys[n]):
        assert encode(f[:-1], q) == f_id
        witnessed = False
        for b, v in shifts:
            shift_checks += 1
            h = list(f[:-1])
            for i, x in enumerate(v):
                h[i] = (h[i] + x) % q
            for a in divisors[encode(h, q)]:
                d = len(a) - 1
                if d < b or not (d % 2 or b % 2):
                    continue
                if minus_one_mod(a, v, q):
                    witnessed = True
                    break
            if witnessed and not full_scan:
                break
        if not witnessed:
            failures.append(f_id)
    failure_set = set(failures)
    assert squares <= failure_set, 'Square has a divisor/shift witness!'
    return len(failures), len(failure_set - squares), len(squares), shift_checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--engine', help='Optional independently compiled C engine')
    parser.add_argument('--full-scan', action='store_true', help='Scan all shifts even after finding a witness')
    parser.add_argument('--q', type=int, choices=(3, 7), nargs='+', default=[3, 7])
    parser.add_argument('--max-n', type=int, choices=range(2, 6), default=5)
    args = parser.parse_args()
    for q in args.q:
        for n in range(2, args.max_n + 1):
            start = time.monotonic()
            failed, nonsquare, squares, checks = audit(q, n, args.full_scan)
            status = ''
            if args.engine:
                output = subprocess.check_output([args.engine, str(q), str(n)], text=True, timeout=30)
                expected = int(re.search(r'failU_nonsq=(\d+)', output)[1])
                sqfail = int(re.search(r'sqfailU=(\d+)', output)[1])
                assert nonsquare == expected, (q, n, nonsquare, expected)
                assert squares == sqfail
                status = ' C=MATCH'
            print(f'q={q} n={n} total={q**n} fail={failed} '
                  f'fail_nonsquare={nonsquare} squares={squares} '
                  f'shift_checks={checks}{status} seconds={time.monotonic()-start:.3f}', flush=True)


if __name__ == '__main__':
    main()
