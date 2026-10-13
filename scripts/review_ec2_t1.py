# review_ec2_t1.py — R189 reviewer 2: from-scratch EVIDENCE that no residue class of the seven Elsholtz–Tao
# Prop 1.9 families (transcribed directly from arXiv:1107.1010 p.8) contains a unit square, i.e. that r is
# never a square of a unit modulo every prime power of M.  Also checks every class is primitive (gcd(r,M)=1).
# Usage: uv run --with sympy python scripts/review_ec2_t1.py MMAX
import sys
from math import gcd
from sympy import factorint, legendre_symbol, sqrt_mod

MMAX = int(sys.argv[1])


def unit_square_mod(r, M):
    if gcd(r, M) != 1:
        return False
    for p, e in factorint(M).items():
        if p == 2:
            if (e == 2 and r % 4 != 1) or (e >= 3 and r % 8 != 1):
                return False
        elif legendre_symbol(r % p, p) != 1:
            return False
    return True


def crt(r1, m1, r2, m2):
    assert gcd(m1, m2) == 1
    return (r1 + m1 * ((r2 - r1) * pow(m1, -1, m2) % m2)) % (m1 * m2), m1 * m2


classes = []  # (fam, r, M)
for a in range(1, MMAX):
    for d in range(1, MMAX // (4 * a) + 1):
        M = 4 * a * d
        if M > MMAX:
            break
        F = 4 * a * a * d + 1                           # I1: n = -f mod 4ad, f | 4a^2 d + 1
        for f in range(1, F + 1):
            if F % f == 0:
                classes.append(('I1', (-f) % M, M))
        for e in range(1, MMAX // M + 2):               # II3: -4a^2d - e mod 4ade, (4ad, e) = 1
            if M * e > MMAX:
                break
            if gcd(M, e) == 1:
                classes.append(('II3', (-4 * a * a * d - e) % (M * e), M * e))
    for f in range(2, MMAX + 1):                        # II2: -4a^2 d mod f, 4ad | f+1
        if (f + 1) % (4 * a) == 0:
            for d in range(1, (f + 1) // (4 * a) + 1):
                if (f + 1) % (4 * a * d) == 0:
                    classes.append(('II2', (-4 * a * a * d) % f, f))
for a in range(1, MMAX):
    for c in range(1, MMAX // (4 * a) + 1):
        M1 = 4 * a * c
        for f in range(1, MMAX // M1 + 1):              # I2 and I3 (moduli 4ac*f, 4cd*f)
            if gcd(M1, f) != 1:
                continue
            classes.append(('I2', *crt((-f) % M1, M1, (-c * pow(a, -1, f)) % f if f > 1 else 0, f)))
            # I3 with (c, d) := (a, c) renamed: n = -f mod 4cd, n^2 = -4c^2 d mod f
            cc, dd = a, c
            roots = sqrt_mod((-4 * cc * cc * dd) % f, f, all_roots=True) if f > 1 else [0]
            for rt in roots or []:
                classes.append(('I3', *crt((-f) % M1, M1, rt, f)))
        b = c                                           # I4 / II1 with (a, b), e | a + b, (e, 4ab) = 1
        for e in range(1, a + b + 1):
            if (a + b) % e == 0 and gcd(e, M1) == 1:
                classes.append(('I4', (-pow(e, -1, M1)) % M1, M1))
                classes.append(('II1', (-e) % M1, M1))
bad = [(f, r, M) for f, r, M in classes if M <= MMAX and unit_square_mod(r, M)]
nonprim = [(f, r, M) for f, r, M in classes if M <= MMAX and gcd(r, M) != 1]
print('classes (with multiplicity, M <= %d):' % MMAX, sum(1 for c in classes if c[2] <= MMAX))
print('classes containing a unit square:', bad[:10], len(bad))
print('non-primitive classes:', nonprim[:10], len(nonprim))
