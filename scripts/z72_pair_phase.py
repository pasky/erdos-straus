"""Two-factor phase test: integer arithmetic, adversarial screens and direct witnesses.
Run: uv run python scripts/z72_pair_phase.py
"""
from collections import Counter
from functools import cache
from itertools import combinations
from pathlib import Path
from math import gcd

from sympy import factorint, primerange, primitive_root


@cache
def logs(c):
    g = int(primitive_root(c))
    return {pow(g, i, c): i for i in range(c - 1)}


def score(m, a, b, v, w):
    def dist(x):
        return min(x % m, -x % m)
    return min((v + 1) * dist(j*a) + (w + 1) * dist(j*b)
               for j in range(1, m, 2))


def hit(m, a, b, v, w):
    return next(((i, j) for i in range(-v, v+1) for j in range(-w, w+1)
                 if (a*i+b*j) % m == m//2), None)


def fires(m, s, v, w):
    return s > m or (s == m and (v % 2 or w % 2))


def group_test():
    tally = Counter()
    for c in primerange(3, 85):
        if c % 4 != 3:
            continue
        m = c-1
        for a in range(m//2+1):  # independent inversion of either generator
            for b in range(a, m//2+1):
                for v in range(1, 6):
                    for w in range(1, 6):
                        s = score(m, a, b, v, w)
                        h = hit(m, a, b, v, w)
                        if fires(m, s, v, w):
                            assert h is not None, (m, a, b, v, w, s)
                        if h is None and s == m:
                            assert not (v % 2 or w % 2)
                            assert gcd(v+1, w+1) == 1
                        tally['cases'] += 1
                        tally['fires'] += bool(fires(m, s, v, w))
                        tally['equality misses'] += h is None and s == m
    print('finite group regression:', dict(tally))


def scan(ns, shifts, pnr=False):
    """Keep only genuinely mixed hits (neither factor works by itself)."""
    good, misses = [], []
    for n in ns:
        first = None
        for c in shifts:
            if n % c == 0 or (n+c) % 4 or (pnr and pow(n,(c-1)//2,c) != c-1):
                continue
            K = (n+c)//4
            for (q,v),(r,w) in combinations(factorint(K).items(), 2):
                a, b = logs(c)[q%c], logs(c)[r%c]
                m = c-1
                if hit(m,a,0,v,0) or hit(m,0,b,0,w):
                    continue
                s = score(m,a,b,v,w)
                if not fires(m,s,v,w):
                    continue
                i,j = hit(m,a,b,v,w)
                A = q**max(i,0)*r**max(j,0)
                B = q**max(-i,0)*r**max(-j,0)
                assert K % (A*B) == (A+B) % c == 0
                D, E = K//(A*B), (A+B)//c
                x,y,z = K,n*A*D*E,n*B*D*E
                assert min(x,y,z)>0 and 4*x*y*z == n*(x*y+x*z+y*z)
                first = n,c,q,r,v,w,s,m,(i,j),(x,y,z)
                break
            if first:
                break
        if first:
            good.append(first)
        else:
            misses.append(n)
    return good, misses


if __name__ == '__main__':
    group_test()
    root = Path(__file__).resolve().parents[1]/'data/z58/screens'
    def load(name):
        return [int(l.split()[0]) for l in (root/name).read_text().splitlines()
                if l.strip() and not l.startswith('#')]
    shifts = [c for c in primerange(3,200) if c % 4 == 3]
    for name, ns in [('odd squares',[i*i for i in range(1,100,2)]),
                     ('8-line zeros',load('r8_zeros_1e10.txt')),
                     ('composite zeros',load('composite_zeros_le8e6.txt')),
                     ('star zeros',load('star_prime_zeros.txt')),
                     ('gstar zeros',load('gstar_zeros.txt')),
                     ('Mordell primes under 200000',[p for p in primerange(2,200000)
                        if p%840 in {1,121,169,289,361,529}])]:
        for pnr in (False, True):
            good, bad = scan(ns, shifts, pnr)
            print(name, 'PNR' if pnr else 'all', len(good), '/', len(ns),
                  'first hit', next(iter(good),None), 'first misses', bad[:4])
