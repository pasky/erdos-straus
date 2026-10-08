"""m13b_invert.py — recover all T-generic ET data (T={11,13}) from ES solutions of 4/N (MORDELL13B §2).

usage: PYTHONPATH=scripts uv run python scripts/m13b_invert.py N es_file [out.pkl]
  es_file: output of m13b_es N (all x<=y<=z with 4/N = 1/x+1/y+1/z).
For every permutation of every solution and every unitary split N = B*lam, apply the inverse maps of
Lemmas 2.1-2.4 (schemes U, Q, PQ, I2), producing candidate parameter triples; each candidate is then
tested EXACTLY: T-free part of the class condition (residue = 1 mod M') via mordell_lib, giving its
box (fam, M_T, r mod M_T); and x* = x(2) membership (r = 2 mod M_T).  Completeness (every T-generic
datum of ES level N is produced) is Lemma 2.1-2.4; soundness is the exact test.
Prints: N, #ES solutions, #boxes (distinct (fam,MT,res)), x*-hits.
"""
import itertools
import pickle
import sys
from math import gcd, isqrt

from sympy import divisors

from mordell_lib import cls_modulus_residues

T = (11, 13)


def tpart(m):
    r = 1
    for q in T:
        while m % q == 0:
            m //= q
            r *= q
    return r


def sq_triples(P1, P2, P3):
    """all (t, A, B, C) with P1=tA^2, P2=tB^2, P3=tC^2 (positive integers)."""
    g = gcd(gcd(P1, P2), P3)
    for t in divisors(g):
        q1, q2, q3 = P1 // t, P2 // t, P3 // t
        A, B, C = isqrt(q1), isqrt(q2), isqrt(q3)
        if A * A == q1 and B * B == q2 and C * C == q3:
            yield t, A, B, C


def unitary_splits(N):
    parts = []
    m = N
    for q in T:
        p = 1
        while m % q == 0:
            m //= q
            p *= q
        parts.append(p)
    assert m == 1, "N must be a {11,13}-unit"
    for s in itertools.product((0, 1), repeat=2):
        B = (parts[0] if s[0] else 1) * (parts[1] if s[1] else 1)
        yield B, N // B


def cands(N, X, Y, Z):
    out = []
    # (U) II1/I4: (X,Y,Z) = (iab, iac, ibc), N = (ab)_T
    if (X * Y) % Z == 0 and (X * Z) % Y == 0 and (Y * Z) % X == 0:
        for i, a, b, c in sq_triples(X * Y // Z, X * Z // Y, Y * Z // X):
            if (a + b) % c == 0:
                e = (a + b) // c
                if gcd(e, 4 * a * b) == 1:
                    out.append(('II1', (a, b, e)))
                    out.append(('I4', (a, b, e)))
    # (Q) II2: (X,Y,Z) = (amdF, ajd, mjd), F = N
    if (X * Y) % (Z * N) == 0 and (X * Z) % (Y * N) == 0 and (N * Y * Z) % X == 0:
        for d, a, m, j in sq_triples(X * Y // (Z * N), X * Z // (Y * N), N * Y * Z // X):
            out.append(('II2', (a, d, 4 * a * d * m - 1)))
    for B, lam in unitary_splits(N):
        # (PQ) II3/I3/I1: (X,Y,Z) = (d'mj, lam a'd'j, B lam a'd'm)
        if (B * X * Y) % Z == 0 and (X * Z) % (B * Y) == 0 and (Y * Z) % (B * lam * lam * X) == 0:
            for dp, j, m, ap in sq_triples(B * X * Y // Z, X * Z // (B * Y), Y * Z // (B * lam * lam * X)):
                e = 4 * ap * dp * m - 1
                for aT in divisors(lam):
                    if aT * aT > lam or lam % (aT * aT):
                        continue
                    a, d = aT * ap, (lam // (aT * aT)) * dp
                    if gcd(4 * a * d, e) == 1:
                        out.append(('II3', (a, d, e)))
                        out.append(('I3', (a, d, e)))
                    if (4 * a * a * d + 1) % e == 0:
                        out.append(('I1', (a, d, e)))
        # (I2): (X,Y,Z) = (cth, ath, B act), N = A*B, A=(ac)_T, B=f_T
        if (B * X * Y) % Z == 0 and (X * Z) % (B * Y) == 0 and (Y * Z) % (B * X) == 0:
            for t, h, c, a in sq_triples(B * X * Y // Z, X * Z // (B * Y), Y * Z // (B * X)):
                ac = a * c
                f = 4 * (ac // tpart(ac)) * t - 1
                if f > 0 and gcd(4 * ac, f) == 1:
                    out.append(('I2', (a, c, f)))
    return out


def boxes_of(fam, P):
    """boxes (MT, r mod MT) of the class met by T-generic points; [] if none."""
    M, res = cls_modulus_residues(fam, P)
    MT = tpart(M)
    Mp = M // MT
    return sorted({(MT, r % MT) for r in res if r % Mp == 1 % Mp})


def main():
    N = int(sys.argv[1])
    sols = []
    with open(sys.argv[2]) as fh:
        for line in fh:
            if line.strip():
                sols.append(tuple(map(int, line.split())))
    boxes = {}
    hits = []
    for s in sols:
        for X, Y, Z in set(itertools.permutations(s)):
            for fam, P in cands(N, X, Y, Z):
                for MT, r in boxes_of(fam, P):
                    key = (fam, MT, r)
                    if key not in boxes:
                        boxes[key] = P
                    if MT > 1 and (r - 2) % MT == 0:
                        hits.append((fam, P, MT, r))
                    if MT == 1:
                        hits.append(('LEVEL0', fam, P))
    print(f"N={N} ES={len(sols)} boxes={len(boxes)} xstar_hits={len(hits)}", hits[:5])
    if len(sys.argv) > 3:
        with open(sys.argv[3], 'wb') as fh:
            pickle.dump({'N': N, 'boxes': boxes, 'hits': hits}, fh)


if __name__ == '__main__':
    main()
