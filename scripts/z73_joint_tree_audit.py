"""Exact finite-place regressions, not a proof about the infinite tree."""
from collections import Counter
from fractions import Fraction as F


def dyadic():
    # Direct counts of all represented odd residues, with at least one odd coordinate.
    for k in range(2, 9):
        m = 2**k
        hit = {(a*a+b*b) % m for a in range(m) for b in range(m) if (a+b) % 2}
        assert hit == set(range(1, m, 4))
    print('2-adic unit norm test: exact mod 2^k, k=2..8')


def four_squares():
    # Convolve two independently counted two-square blocks, including zero.
    for p in (3, 5, 7, 11, 13, 17):
        two = Counter((a*a+b*b) % p for a in range(p) for b in range(p))
        four = Counter()
        for t, u in two.items():
            for v, w in two.items():
                four[(t+v) % p] += u*w
        assert four[0]-1 == p**3+p*p-p-1  # smooth part of the zero fiber
        assert all(four[t] == p**3-p for t in range(1, p))
    primitive = {(a*a+b*b+c*c+d*d) % 8 for a in range(8) for b in range(8)
                 for c in range(8) for d in range(8) if (a | b | c | d) & 1}
    assert primitive == set(range(1, 8))  # not the full represented set!
    print('rank-four smooth fiber counts: q=3..17 prime; primitive mod 8 excludes 0')


def fork(p):
    # Base (x,y), square norm P. Two siblings: skip and add Q=1+xZ;
    # accept x=A^2+B^2. Demand (toy finite forbidden lists) x, Q, A nonzero.
    # The bad parent x=0 is seen by both branches; resampling it is incorrect.
    squares = {x*x % p for x in range(1, p)}
    pairs = Counter((x*x + y*y) % p for x in range(p) for y in range(p))
    root = [(x, y) for x in range(p) for y in range(p) if (x*x+y*y) % p in squares]
    n = p-1 if p % 4 == 1 else p+1
    assert all(pairs[s] == n for s in range(1, p))
    assert 2*len(root) == (p-1)*n
    # Enumerate the joint (shared parent) success probability. Full product
    # has O(p^4) leaves; compute sibling counts conditionally and multiply.
    good_z = [sum((1+x*z) % p != 0 for z in range(p)) for x in range(p)]
    good_a = Counter((a*a+b*b) % p for a in range(1, p) for b in range(p))
    mass = F(sum(good_z[x]*good_a[x] for x, y in root if x), len(root)*p*n)
    # Bad bounds: parent x=0; one forbidden Z; at most two conic points A=0.
    assert 1-mass <= F(2, n) + F(1, p) + F(2, n)
    assert mass > 0
    print(f'p={p}: root points {len(root)}, joint good mass {mass}')


if __name__ == '__main__':
    dyadic()
    four_squares()
    for p in (5, 7, 13, 31, 67, 101):
        fork(p)
