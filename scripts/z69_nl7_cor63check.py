"""Sanity check of Corollary 6.3 (Mordell-Schinzel along positive definite quadratic curves).
Enumerate congruence-type polynomial words on P(t) = t^2 + beta: two constant letters, the third quadratic, on every
residue class of t modulo the natural period where the word is integral with 8 | xy; check that P(t) on the class is
never congruent mod M to an odd square (M as in the corollary), and count the classes found (non-vacuity).
"""
from math import gcd
def odd_square_residues(M):
    return {(m * m) % M for m in range(1, 2 * M, 2)}
tot = 0
for beta in (1, 16, 18, 64):
    P = lambda t: t * t + beta
    for a in range(1, 13):
        for b in range(1, 13):
            # case Y=a, Z=b : X = (P + b)/(ab-1)
            m = a * b - 1
            if m >= 1:
                M = 8 * m; sq = odd_square_residues(M)
                for r in range(M):
                    n = P(r)
                    if n % 2 == 1 and (n + b) % m == 0 and (((n + b) // m) * a) % 8 == 0:
                        tot += 1
                        assert n % M not in sq, ('YZ', beta, a, b, r)
            # case X=a, Y=b : Z = (P + a)/(ab-1), 8 | ab
            f = a * b - 1
            if f >= 1 and (a * b) % 8 == 0:
                sq = odd_square_residues(f) if f > 1 else {0}
                for r in range(2 * f):
                    n = P(r)
                    if n % 2 == 1 and (n + a) % f == 0:
                        tot += 1
                        assert n % f not in sq, ('XY', beta, a, b, r)
            # case X=a, Z=b : Y = (P + a + b)/(ab), 8 | a*Y
            w = 8 // gcd(8, a); M = w * a * b; sq = odd_square_residues(M)
            for r in range(M):
                n = P(r)
                if n % 2 == 1 and (n + a + b) % (a * b) == 0 and ((n + a + b) // (a * b)) % w == 0:
                    tot += 1
                    assert n % M not in sq, ('XZ', beta, a, b, r)
print("Corollary 6.3: congruence-type words found on", tot, "(curve, letters, class) triples; in every case P(t) mod M is not an odd-square residue")
