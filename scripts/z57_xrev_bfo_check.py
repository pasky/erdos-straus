"""Independent BFO numeric audit; argument is an exported branch directory.

Run with uv run --with sympy python scripts/z57_xrev_bfo_check.py /tmp/xrev_BFO.
Uses an unordered-small-entry enumeration, not the source's three-region engine.
Memory is bounded by divisors of one integer and the solutions for one input.
"""
from collections import Counter
from math import isqrt, log
from pathlib import Path
import sys

from sympy import divisors, isprime, primerange


def solutions(n):
    # P <= Q, C >= 1 imply 4P^2 - 2P <= n.
    found = []
    for p in range(1, (1 + isqrt(1 + 4*n)) // 4 + 1):
        cap = (n + 2*p) // (4*p*p)
        if p < 1024:
            ms = (int(m) for m in divisors(n+p)
                  if (m+1) % (4*p) == 0 and m <= (n+p)//p)
        else:
            ms = (4*p*c-1 for c in range(1, cap+1)
                  if (n+p) % (4*p*c-1) == 0)
        for m in ms:
            q, c = (n+p)//m, (m+1)//(4*p)
            assert p <= q and 4*p*q*c-p-q == n
            assert (p+q) % 2 == 1
            found.append((p, q, c))
    assert len(found) == len(set(found))
    return found


def counts(n, ss):
    hc = int(log(n)**2)
    return (len(ss), sum(c <= hc for p, q, c in ss),
            sum(64*c**3 <= n for p, q, c in ss),
            sum(q**4 > p*n for p, q, c in ss),
            sum(q**4 > p*n and p**15 > n for p, q, c in ss))


def main():
    root = Path(sys.argv[1])
    data = root / 'data/z57/bfo'
    # Validate the new enumeration against a direct bounded P,Q search.
    for n in range(3, 1200, 2):
        brute = []
        for p in range(1, (1+isqrt(1+4*n))//4+1):
            for q in range(p, (n+p)//(4*p-1)+1):
                if (n+p+q) % (4*p*q) == 0:
                    brute.append((p, q, (n+p+q)//(4*p*q)))
        assert set(solutions(n)) == set(brute), n
    print('599 odd inputs <1200: hybrid enumeration = direct P,Q search')
    jacobi_count = 0
    for n in primerange(5, 6000):
        if n % 4 != 1:
            continue
        for p, q, c in solutions(n):
            jacobi_count += 1
            assert pow(4*c*p-1, (n-1)//2, n) == n-1
            assert pow(4*c*q-1, (n-1)//2, n) == n-1
    assert all(not solutions(n*n) for n in range(3, 80, 2))
    print('Jacobi:', jacobi_count, 'solutions, no violations; squares 9..79^2: no solutions')
    zs = [int(t) for t in (data/'F4zeros.txt').read_text().split()]
    least = []
    for n in zs:
        assert isprime(n) and n % 4 == 1
        assert counts(n, solutions(n))[3] == 0, n
        least.append(next(q for q in primerange(2, 1000)
                          if pow(int(q), (n-1)//2, n) == n-1))
    print('G* listed zeros independently verified:', len(zs), 'last', max(zs))
    print('least QNR distribution:', sorted(Counter(least).items()))
    print('QNR >=11:', sum(q >= 11 for q in least),
          '>=17:', sum(q >= 17 for q in least), '=2:', least.count(2))
    rows = 0
    for k in range(4):
        recorded = []
        for line in (data/f'decide_1e10_2e10_{k}.txt').read_text().splitlines():
            if not line or line.startswith('#'):
                continue
            n, *expected = map(int, line.split())
            assert isprime(n) and n % 4 == 1
            ss = solutions(n)
            actual = counts(n, ss)
            assert tuple(expected) == actual, (n, expected, actual)
            for p, q, c in ss:
                assert pow(4*c*p-1, (n-1)//2, n) == n-1
                assert pow(4*c*q-1, (n-1)//2, n) == n-1
                if 64*c**3 <= n:
                    assert q**4 > p*n
            recorded.append(actual)
            rows += 1
            print('record verified:', n, actual, flush=True)
        print('chunk', k, 'zero totals',
              [sum(r[i] == 0 for r in recorded) for i in range(5)], flush=True)
    print('All recorded exception rows independently verified:', rows)
    for theta in (1/3, .4, .5):
        def relative(decade):
            lq = decade*log(10)
            return min(lq*(-theta/r+(r+1)/(4*r*r))+log(lq)/(2*r)
                       for r in range(2, 400))
        lo, hi = 1., 200.
        for _ in range(60):
            mid = (lo+hi)/2
            if relative(mid) > -log(2):
                lo = mid
            else:
                hi = mid
        print('Burgess half-bound threshold:', theta, (lo+hi)/2)


if __name__ == '__main__':
    main()
