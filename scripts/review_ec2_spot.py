# review_ec2_spot.py — R189 reviewer 2: (a) own brute-force ES for every m with n = k 2^m + 1 <= NMAX;
# (b) exact-integer spot checks of the certificate identities at random huge m (thousands of digits);
# (c) for every m in [m*, MSEQ] exactly one-or-more classes apply and give a valid positive integer solution.
# Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_ec2_spot.py NMAX MSEQ NRAND k1 k2 ...
import sys, json, random
from fractions import Fraction
from review_ec2_check import es_solve, check


def ev(coeffs, n):
    v = Fraction(0)
    for c in reversed(coeffs):
        v = v * n + Fraction(c)
    return v


def apply_cert(C, m):
    n = C['k'] * 2**m + 1
    hits = 0
    for cl in C['classes']:
        if n % cl['M'] == cl['r']:
            x, y, z = (ev(p, n) for p in cl['xyz'])
            assert x.denominator == y.denominator == z.denominator == 1, (m, cl['M'])
            x, y, z = int(x), int(y), int(z)
            assert min(x, y, z) > 0 and 4 * x * y * z == n * (x * y + y * z + x * z), (m, cl['M'])
            hits += 1
    return hits


if __name__ == '__main__':
    NMAX, MSEQ, NRAND = int(float(sys.argv[1])), int(sys.argv[2]), int(sys.argv[3])
    random.seed(189)
    for k in map(int, sys.argv[4:]):
        C, mstar = check(f'data/ec/cert_k{k}.json', verbose=False)
        m = 0
        nb = 0
        while k * 2**m + 1 <= NMAX:
            assert es_solve(k * 2**m + 1), (k, m)
            nb += 1
            m += 1
        for m in range(mstar, MSEQ + 1):
            assert apply_cert(C, m) >= 1, ('uncovered', k, m)
        digs = []
        for _ in range(NRAND):
            m = random.randint(5000, 40000)
            assert apply_cert(C, m) >= 1, ('uncovered', k, m)
            digs.append(int((k * 2**m + 1).bit_length() * 0.30103) + 1)
        print(f'k={k}: brute ES ok for m<{nb} (n<={NMAX}); certificate ok for {mstar}<=m<={MSEQ}; '
              f'{NRAND} random m in [5000,40000] ok (n has {min(digs)}..{max(digs)} digits)')
