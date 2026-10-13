"""R187 (review of O178 DEPTH_ASPECT Thm 3.1), from scratch.

Checks, for a general prime r, the reduction that Thm 3.1 imports from MORDELL17 Lemmas 1.1, 2.1-2.3:
every box cut out on the r-generic line {x_q = 1 (q != r), x_r = u} by a class of the seven ET Prop 1.9
families is contained in a box predicted from ES solutions of 4/r^k:
  * non-P types at level k (<= 6 per ordered solution (x,y,z) of 4/r^k):
      -y/z, -z/y, the square roots of -y/z, -(x/y + x/z), and its inverse   (all mod r^k)
  * P type: for each ordered solution of 4/r^K with r^K | y, z (i.e. an N-point of Sigma^II_{r^K}),
      the box 1 - 4y/r^K mod r^ceil(K/2).
The classes are read literally off the statement of ET Prop 1.9 (not off the POINTWISE_MORDELL 2.1 table)
for all moduli M <= Mmax.  Also checks: no level-0 boxes.

Usage: PYTHONPATH=scripts uv run python scripts/review_da2_rgeneric.py r Mmax kmax
"""
import sys
from math import gcd
from fractions import Fraction
from itertools import permutations


def vr(n, r):
    v = 0
    while n % r == 0:
        n //= r
        v += 1
    return v


def split(m, r):
    k = vr(m, r)
    return k, m // r**k


def divisors(n):
    ds = [1]
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            ds = [d * p**i for d in ds for i in range(e + 1)]
        p += 1 if p == 2 else 2
    if m > 1:
        ds = ds + [d * m for d in ds]
    return ds


def factor(n):
    f = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divs_from_fac(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p**i for d in ds for i in range(e + 1)]
    return ds


# ---------------- brute force of ET Prop 1.9 classes on the r-generic line ----------------

_sqrt_cache = {}


def sqrt_mod(s, R):
    key = (s % R, R)
    if key not in _sqrt_cache:
        _sqrt_cache[key] = [u for u in range(R) if (u * u - s) % R == 0]
    return _sqrt_cache[key]


def boxes_of(conds, r):
    """conds: list of ('lin', rho, m) meaning n = rho mod m, or ('sq', s, m) meaning n^2 = s mod m.
    Returns set of (k, u mod r^k) with u a unit mod r, the boxes of x(u) in the class; None if empty."""
    K = 0
    lin = []
    sq = []
    for typ, val, m in conds:
        k, mp = split(m, r)
        if typ == 'lin':
            if (val - 1) % mp:
                return set()
            lin.append((val % r**k, k))
        else:
            if (val - 1) % mp:
                return set()
            sq.append((val, k))
        K = max(K, k)
    R = r**K
    # candidate set mod R
    if lin:
        # combine linear constraints: all are u = val mod r^k; take the finest and check consistency
        lin.sort(key=lambda t: -t[1])
        u0, k0 = lin[0]
        for v, k in lin[1:]:
            if (u0 - v) % r**k:
                return set()
        cands = [u0 + j * r**k0 for j in range(r**(K - k0))]
    else:
        cands = list(range(R))
    out = set()
    for u in cands:
        if K > 0 and u % r == 0:
            continue
        ok = all((u * u - s) % r**k == 0 for s, k in sq)
        if ok:
            out.add((K, u % R))
    return out


def brute_boxes(r, Mmax):
    B = {}  # (k, u) -> family tag (first found)

    def add(S, tag):
        for b in S:
            B.setdefault(b, tag)

    # I1: n = -f mod 4ad, f | 4a^2 d + 1
    for a in range(1, Mmax // 4 + 1):
        for d in range(1, Mmax // (4 * a) + 1):
            for f in divisors(4 * a * a * d + 1):
                add(boxes_of([('lin', -f, 4 * a * d)], r), ('I1', a, d, f))
    # I2: n = -f mod 4ac, n = -c/a mod f, (4ac, f) = 1; modulus 4acf
    for a in range(1, Mmax // 4 + 1):
        for c in range(1, Mmax // (4 * a) + 1):
            for f in range(1, Mmax // (4 * a * c) + 1):
                if gcd(4 * a * c, f) != 1:
                    continue
                rho = (-c * pow(a, -1, f)) % f if f > 1 else 0
                add(boxes_of([('lin', -f, 4 * a * c), ('lin', rho, f)], r), ('I2', a, c, f))
    # I3: n = -f mod 4cd, n^2 = -4c^2 d mod f, (4cd, f) = 1
    for c in range(1, Mmax // 4 + 1):
        for d in range(1, Mmax // (4 * c) + 1):
            for f in range(1, Mmax // (4 * c * d) + 1):
                if gcd(4 * c * d, f) != 1:
                    continue
                add(boxes_of([('lin', -f, 4 * c * d), ('sq', -4 * c * c * d, f)], r), ('I3', c, d, f))
    # I4 / II1: n = -1/e resp. -e mod 4ab, e | a+b, (e, 4ab) = 1
    for a in range(1, Mmax // 4 + 1):
        for b in range(1, Mmax // (4 * a) + 1):
            m = 4 * a * b
            for e in divisors(a + b):
                if gcd(e, m) != 1:
                    continue
                add(boxes_of([('lin', -pow(e, -1, m), m)], r), ('I4', a, b, e))
                add(boxes_of([('lin', -e, m)], r), ('II1', a, b, e))
    # II2: n = -4a^2 d mod f, 4ad | f+1
    for a in range(1, Mmax // 4 + 1):
        for d in range(1, Mmax // (4 * a) + 1):
            for f in range(4 * a * d - 1, Mmax + 1, 4 * a * d):
                add(boxes_of([('lin', -4 * a * a * d, f)], r), ('II2', a, d, f))
    # II3: n = -4a^2 d - e mod 4ade, (4ad, e) = 1
    for a in range(1, Mmax // 4 + 1):
        for d in range(1, Mmax // (4 * a) + 1):
            for e in range(1, Mmax // (4 * a * d) + 1):
                if gcd(4 * a * d, e) != 1:
                    continue
                add(boxes_of([('lin', -4 * a * a * d - e, 4 * a * d * e)], r), ('II3', a, d, e))
    return B


# ---------------- predicted boxes from ES solutions of 4/r^k ----------------

def es_solutions(n, only_type2=False):
    """All ordered positive (x,y,z) with 4/n = 1/x+1/y+1/z.  If only_type2: only those with n | y, n | z
    (computed via (4x-n)/x = 1/y'+1/z', y = n y', z = n z'), returned as ordered triples."""
    sols = set()
    if only_type2:
        for x in range(n // 4 + 1, n // 2 + 1):
            m = 4 * x - n
            if m <= 0:
                continue
            for d1 in divs_from_fac({p: 2 * e for p, e in factor(x).items()}):
                if d1 > x:
                    continue
                if (d1 + x) % m:
                    continue
                y1 = (d1 + x) // m
                d2 = x * x // d1
                if (d2 + x) % m:
                    continue
                z1 = (d2 + x) // m
                sols.add((x, n * y1, n * z1))
                sols.add((x, n * z1, n * y1))
        return sols
    fn = factor(n)
    for x in range(n // 4 + 1, (3 * n) // 4 + 1):
        m = 4 * x - n
        N = n * x
        fN = dict(fn)
        for p, e in factor(x).items():
            fN[p] = fN.get(p, 0) + e
        for d1 in divs_from_fac({p: 2 * e for p, e in fN.items()}):
            if d1 > N or (d1 + N) % m:
                continue
            y = (d1 + N) // m
            if y < x:
                continue
            d2 = N * N // d1
            if (d2 + N) % m:
                continue
            z = (d2 + N) // m
            for t in set(permutations((x, y, z))):
                sols.add(t)
    for x, y, z in sols:
        assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n)
    return sols


def red(fr, R):
    """rational -> residue mod R (None if denominator not invertible)."""
    if gcd(fr.denominator, R) != 1:
        return None
    return fr.numerator * pow(fr.denominator, -1, R) % R


def predicted(r, kmax, Kmax):
    P = set()  # (level, residue)
    nonP_count = {}
    for k in range(1, kmax + 1):
        R = r**k
        S = es_solutions(R)
        nonP_count[k] = len(S)
        for x, y, z in S:
            vals = []
            q = red(-Fraction(y, z), R)
            if q is not None:
                vals.append(q)
                vals += sqrt_mod(q, R)
            q = red(-Fraction(z, y), R)
            if q is not None:
                vals.append(q)
            e = Fraction(x, y) + Fraction(x, z)
            q = red(-e, R)
            if q is not None:
                vals.append(q)
            q = red(-1 / e, R)
            if q is not None:
                vals.append(q)
            for v in vals:
                P.add((k, v))
    nP = {}
    for K in range(1, Kmax + 1):
        n = r**K
        S = es_solutions(n, only_type2=True)
        nP[K] = len(S)
        lev = (K + 1) // 2
        R = r**lev
        for x, y, z in S:
            f = 4 * y // n - 1
            P.add((lev, (-f) % R))
    return P, nonP_count, nP


def contained(box, P, r):
    k, u = box
    for j in range(0, k + 1):
        if (j, u % r**j) in P:
            return True
    return False


if __name__ == '__main__':
    r, Mmax, kmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    B = brute_boxes(r, Mmax)
    lev0 = [b for b in B if b[0] == 0]
    print(f"r={r} Mmax={Mmax}: {len(B)} unit boxes from Prop 1.9 classes; level-0 boxes: {len(lev0)}")
    P, nc, nP = predicted(r, kmax, 2 * kmax)
    print("ordered solutions f(r^k):", nc, " Sigma^II-type solutions (n|y,z) per K:", nP)
    bad = []
    tested = 0
    for b, tag in sorted(B.items()):
        if b[0] > kmax:
            continue
        tested += 1
        if not contained(b, P, r):
            bad.append((b, tag))
    lv = {}
    for b in B:
        lv[b[0]] = lv.get(b[0], 0) + 1
    print("brute boxes per level:", dict(sorted(lv.items())))
    for k in range(1, kmax + 1):
        R = r**k
        cov = sum(1 for u in range(R) if u % r and contained((k, u), P, r))
        print(f"  predicted union covers {cov}/{R - R // r} unit residues mod r^{k}")
    print(f"tested {tested} boxes of level <= {kmax}; NOT contained in a predicted box: {len(bad)}")
    for b in bad[:20]:
        print("  ", b)
