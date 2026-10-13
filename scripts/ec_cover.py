# ec_cover.py — search an exponent covering of n_m = k*b^m + c by Elsholtz–Tao Prop 1.9 classes
# (the seven fixed-parameter Type I/II families of mordell_lib).
# A class of modulus M = b-part * M' with M' | k^inf (b^L - 1) contains n_m for all large m in a fixed
# set of residues m mod L.  Greedy set cover of Z/L.
# Usage: PYTHONPATH=scripts uv run python scripts/ec_cover.py k L Mmax [b c]
import sys
from math import gcd
from itertools import product
import mordell_lib as ML
from ec_screen import primes_upto, admissible_prime_powers


def candidate_moduli(k, b, c, L, Mmax):
    pps = admissible_prime_powers(b, L, QMAX=Mmax)
    # also primes dividing k (n_m mod q^j is eventually constant there? only mod q^{v_q(k)}); skip
    odd = [1]
    for q, Q in pps:
        new = []
        for d in odd:
            x = d
            while x * q <= Mmax and Q % (x * q // d) == 0:
                x *= q
                new.append(x)
        odd += new
    odd = sorted(set(odd))
    Ms = set()
    bp = [1]
    for p in ML.factor_small(b):
        bp = [u * p ** i for u in bp for i in range(0, 8)]
    for u in bp:
        for d in odd:
            if u * d <= Mmax and u * d > 2:
                Ms.add(u * d)
    return sorted(Ms)


def covered_exponents(k, b, c, L, M, R, base):
    out = set()
    for m in range(L):
        mm = base + ((m - base) % L)
        if (k * pow(b, mm, M) + c) % M in R:
            out.add(m)
    return out


def search(k, L, Mmax, b=2, c=1, verbose=True, divisor_classes=True, restrict=None, Mfilter=None):
    """restrict: optional (L0, set of residues mod L0) — only cover m whose residue mod L0 is in the set."""
    base = 10 * L + 64
    target = set(range(L)) if restrict is None else {m for m in range(L) if m % restrict[0] in restrict[1]}
    Ms = candidate_moduli(k, b, c, L, Mmax)
    if Mfilter:
        Ms = [M for M in Ms if Mfilter(M)]
    sets = []
    if divisor_classes:
        # 'D' classes: n = 0 (mod q), q odd prime; ES(n) from ES(q) scaled by n/q
        for q, Q in admissible_prime_powers(b, L, QMAX=Mmax):
            if q == 2 or b % q == 0:
                continue
            s = {m for m in target if (k * pow(b, base + ((m - base) % L), q) + c) % q == 0}
            if s:
                sets.append((q, ('D', (q,)), s))
    for M in Ms:
        if M % 4 and M % 4 != 3:
            # only II2 has M not divisible by 4 (M = 3 mod 4)
            continue
        W = ML.residue_table(M)
        if not W:
            continue
        cov = {}
        for m in target:
            mm = base + ((m - base) % L)
            r = (k * pow(b, mm, M) + c) % M
            if r in W:
                cov.setdefault(W[r], set()).add(m)
        for cls, s in cov.items():
            sets.append((M, cls, s))
    unc = set(target)
    allcov = set().union(*[s for _, _, s in sets]) if sets else set()
    if unc - allcov:
        if verbose:
            print('k=%d L=%d Mmax=%d: UNCOVERABLE exponents' % (k, L, Mmax), sorted(unc - allcov)[:20])
        return None
    chosen = []
    while unc:
        M, cls, s = max(sets, key=lambda t: (len(unc & t[2]), -t[0]))
        chosen.append((M, cls, sorted(s)))
        unc -= s
    if verbose:
        print('k=%d L=%d: covering with %d classes' % (k, L, len(chosen)))
        for M, cls, s in chosen:
            print('  M=%d %s %s  m mod %d in %s' % (M, cls[0], cls[1], L, s[:12]))
    return chosen


def interp_poly(pts):
    """Lagrange interpolation over Q; returns coefficient list (low->high) of Fractions."""
    from fractions import Fraction as F
    n = len(pts)
    coeffs = [F(0)] * n
    for i, (xi, yi) in enumerate(pts):
        basis = [F(1)]
        den = F(1)
        for j, (xj, _) in enumerate(pts):
            if j == i:
                continue
            basis = [F(0)] + basis
            for t in range(len(basis) - 1):
                basis[t] -= xj * basis[t + 1]
            den *= (xi - xj)
        for t in range(n):
            coeffs[t] += F(yi) * basis[t] / den
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs


def certificate(k, L, chosen, b=2, c=1):
    """explicit polynomial certificate: for each class, x(n), y(n), z(n) as rational polynomials in n."""
    out = {'k': k, 'b': b, 'c': c, 'L': L, 'classes': []}
    for M, cls, s in chosen:
        fam, P = cls
        if fam == 'D':
            q = P[0]
            from fractions import Fraction as F
            xq = next((x, y, (q * x * y) // (4 * x * y - q * (x + y))) for x in range(1, 2 * q) for y in range(x, 4 * q * q)
                      if 4 * x * y - q * (x + y) > 0 and (q * x * y) % (4 * x * y - q * (x + y)) == 0)
            out['classes'].append({'M': q, 'r': 0, 'fam': 'D', 'params': [q], 'exps': s,
                                   'xyz': [['0', str(F(v, q))] for v in xq]})
            continue
        MM, R = ML.cls_modulus_residues(fam, P)
        base = 10 * L + 64
        mm = base + ((s[0] - base) % L)
        r = (k * pow(b, mm, M) + c) % M
        assert r in R
        t0 = 10 ** 6
        pts = []
        for t in range(t0, t0 + 9):
            n = r + M * t
            sol = ML.solve(fam, P, n)
            assert sol is not None
            pts.append((n, sol))
        polys = []
        for i in range(3):
            pc = interp_poly([(n, sol[i]) for n, sol in pts[:8]])
            assert len(pc) <= 7, 'degree too high'
            polys.append([str(x) for x in pc])
        out['classes'].append({'M': M, 'r': r, 'fam': fam, 'params': list(P), 'exps': s, 'xyz': polys})
    return out


if __name__ == '__main__':
    k, L, Mmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    b = int(sys.argv[4]) if len(sys.argv) > 4 else 2
    c = int(sys.argv[5]) if len(sys.argv) > 5 else 1
    ch = search(k, L, Mmax, b, c)
    if ch and len(sys.argv) > 6:
        import json
        json.dump(certificate(k, L, ch, b, c), open(sys.argv[6], "w"))

