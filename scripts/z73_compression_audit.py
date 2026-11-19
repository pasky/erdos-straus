"""Tiny exact regressions for the compressed ET count. No external packages.
Compare *parameterized* events (including I-3 roots), not just cylinders.
Fixed bounds: m <= 480, N <= 30. Run with uv run --no-project python.
"""
from collections import Counter
from functools import cache
from fractions import Fraction
from math import gcd, isqrt, prod

M, B = 480, 30


@cache
def divs(n):
    small = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return small + [n // d for d in reversed(small) if d*d != n]


def literal():
    rows = set()

    def emit(tag, a, b, f, m, r):
        r %= m
        assert gcd(r, m) == 1
        for n in divs(m if tag == 'II2' else m//4):
            if n <= B and (r-1) % (m//n) == 0:
                assert n > 1
                rows.add((tag, a, b, f, m, r, n))

    for a in range(1, M//4+1):
        for b in range(1, M//(4*a)+1):
            t = 4*a*b
            for f in divs(4*a*a*b+1):
                emit('I1', a, b, f, t, -f)
            for e in divs(a+b):
                if gcd(e, t) == 1:
                    emit('I4', a, b, e, t, -pow(e, -1, t))
                    emit('II1', a, b, e, t, -e)
            for f in range(1, M//t+1):
                if gcd(t, f) != 1:
                    continue
                m = t*f
                emit('II3', a, b, f, m, -4*a*a*b-f)
                for r in range(-f % t, m, t):
                    if (a*r+b) % f == 0:
                        emit('I2', a, b, f, m, r)
                    if (r*r+4*a*a*b) % f == 0:
                        emit('I3', a, b, f, m, r)
    for f in range(3, M+1, 4):
        for a in divs((f+1)//4):
            for d in divs((f+1)//(4*a)):
                emit('II2', a, d, f, f, -4*a*a*d)
    return rows


@cache
def weighted(coeff):
    """Complete positive solutions for fixed slots, no small-factor trick."""
    sols = set()
    for i in range(3):  # label a maximal summand Lx
        j, k = (i+1) % 3, (i+2) % 3
        L, M1, H = coeff[i], coeff[j], coeff[k]
        lim = 3*L//4
        for y in range(1, lim+1):
            for z in range(1, lim//y+1):
                for d in range(1, lim//(y*z)+1):
                    e = 4*y*z*d-L
                    if e <= 0 or (M1*y+H*z) % e:
                        continue
                    x = (M1*y+H*z)//e
                    if L*x < max(M1*y, H*z):
                        continue
                    # Check the actual five-factor inequality with the larger
                    # of the two remaining summands in the middle slot.
                    s = z if M1*y >= H*z else y
                    mid = M1 if M1*y >= H*z else H
                    assert 4*e**2*(s*d)*(x*s)*(x*d) <= 9*(L*mid)**2
                    v = [0, 0, 0]
                    v[i], v[j], v[k] = x, y, z
                    sols.add((*v, d))
    return sols


def decoded():
    rows = set()
    for n in range(2, B+1):
        def emit(tag, a, b, f, t, s=None):
            # t principal block; optional auxiliary block f with residue s
            m = t if s is None else t*f
            if m > M or m % n or (s is not None and gcd(t, f) > 1):
                return
            if tag == 'II2':
                r = -4*a*a*b
            elif tag == 'I4':
                r = -pow(f, -1, t)
            else:
                r = -f
            if s is not None:
                r += t*((s-r)*pow(t, -1, f) % f)
            r %= m
            if (r-1) % (m//n) == 0:
                rows.add((tag, a, b, f, m, r, n))

        for a, c, w, d in weighted((n, n, 1)):
            f = 4*a*c*d-1
            if f % n == 0:
                emit('II2', a, d, f, f)
        for A in divs(n):
            V = n//A
            for x, y, z, h in weighted((A, V, 1)):
                e, a, b = 4*x*y*h-1, A*x, V*y
                if gcd(e, 4*a*b) == 1:
                    for tag in ('I4', 'II1'):
                        emit(tag, a, b, e, 4*a*b)
            for D in divs(V):
                F = V//D
                for x, y, w, h in weighted((F*A, F*D, 1)):
                    a, b, f = A*x, D*y, 4*x*y*h-1
                    t = 4*a*b
                    if t*f <= M and f % F == 0 and gcd(t, f) == 1:
                        emit('I2', a, b, f, t, -b*pow(a, -1, f))
                for x, h, w, y in weighted((F*A*A*D, F, 1)):
                    a, b, f = A*x, D*y, 4*x*y*h-1
                    t = 4*a*b
                    if F == 1 and (4*a*a*b+1) % f == 0:
                        emit('I1', a, b, f, t)
                    if t*f > M or f % F or gcd(f, t) > 1:
                        continue
                    emit('II3', a, b, f, t, -4*a*a*b)
                    for s in range(f):
                        if (s*s+4*a*a*b) % f == 0:
                            emit('I3', a, b, f, t, s)
    return rows


def probability_test(rows):
    # Unconditional masses in a finite CRT box, including noncoprime N,m/N.
    # 13 is the Haar unit place; we release the fourth bit at 2.
    mod = 16*9*13
    small = {(m, r) for _, _, _, _, m, r, _ in rows if mod % m == 0}
    qr = {i*i % 13 for i in range(1, 13)}
    critical = (208, 89)  # mod 8 OK, mod 16 not OK, nonresidue mod 13
    assert critical in small
    for K in (4, 3):
        depths = {2: K, 3: 1, 13: 0}
        frozen = prod(p**k for p, k in depths.items())
        box = [x for x in range(1, mod, frozen) if x % 13]
        alive = {x for x in box if x % 13 not in qr}
        alive0 = alive.copy()  # before any cylinder is deleted
        gainable_loss = Fraction(0)
        for m, r in small:
            keep = gcd(frozen, m)
            n = m//keep
            prob = (Fraction(13 if m % 13 == 0 else 1,
                             (12 if m % 13 == 0 else 1)*n)
                    if (r-1) % keep == 0 else Fraction(0))
            hits = [x for x in box if x % m == r]
            assert prob == Fraction(len(hits), len(box))
            if (m, r) == critical:
                assert Fraction(len(alive0.intersection(hits)), len(box)) == (
                    0 if K == 4 else Fraction(1, 24))
            if K == 3 and m % 16 == 0:
                gainable_loss += prob
            alive.difference_update(hits)
        mass = Fraction(len(alive), len(box))
        print(f'2-depth {K}: survival {mass}; released-step deep-class sum {gainable_loss}')
        if K == 3:
            assert gainable_loss > 0 and mass >= old-gainable_loss
        old = mass


if __name__ == '__main__':
    actual, inverse = literal(), decoded()
    assert actual == inverse, (sorted(actual-inverse)[:2], sorted(inverse-actual)[:2])
    print('matched parameterized rows', sorted(Counter(row[0] for row in actual).items()))
    print('N not coprime to m/N:', sum(gcd(n, m//n) > 1 for *_, m, r, n in actual))
    for tag in ('I2', 'I3', 'II3'):
        mixed = [row for row in actual if row[0] == tag and gcd(row[-1], row[3]) > 1
                 and gcd(row[-1], 4*row[1]*row[2]) > 1]
        assert mixed, tag
        print(tag, 'opposite-block hits', len(mixed), 'sample', min(mixed))
    # Z66's out-of-box II-3 regression: peel 11 from a, 13 from e.
    a, d, f, A, D, F = 11, 2, 247, 11, 1, 13
    m, r = 4*a*d*f, -4*a*a*d-f
    assert (m, r, r % (m//143), r % 11, r % 13) == (21736, -1215, 1, 6, 7)
    x, y = a//A, d//D
    h, rem = divmod(f+1, 4*x*y)
    assert rem == 0
    w, rem = divmod(h+A*A*D*x, f//F)
    assert rem == 0 and 4*x*y*h*w == F*h+F*A*A*D*x+w
    probability_test(actual)
