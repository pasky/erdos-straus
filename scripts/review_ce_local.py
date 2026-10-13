"""R199: from-scratch check of Lemma 1.1 and Thm 1.2 (a),(b) on all 64 diagonal triples <a1,a2,a3>, a_i in {1,3,5,7}.

Lemma 1.1: isotropy over Z_2 decided by brute force (primitive x mod 8 with Q(x) = 0 mod 8 suffices by Hensel, since
Q diagonal with unit coefficients: dQ/dx_i = 2 a_i x_i has valuation 1 for x_i odd, and 8 = 2^(2*1+1)), compared with
(i) 'residues mod 4 not all equal', (ii) Hilbert symbol (-a1a3, -a2a3)_2 = 1, (iii) number of x mod 2 (nonzero) with
Q(x) = 0 mod 4.
Thm 1.2: exact enumeration of ALL 2-power overorders of C_0 (via trace dual), not a ladder.
"""
import sys
from itertools import product
from fractions import Fraction as F
sys.path.insert(0, 'scripts')
from review_ce_lib import Cliff, two_power_overorders, discrd, is_order


def hilbert2(a, b):
    # a, b odd units here (2-adic)
    e = lambda u: ((u % 4) - 1) // 2 if u % 2 else None
    ua, ub = a % 8, b % 8
    s = (-1) ** ((((ua - 1) // 2) * ((ub - 1) // 2)) % 2)
    return s


def iso_brute(a):
    for x in product(range(8), repeat=3):
        if all(xi % 2 == 0 for xi in x):
            continue
        if sum(ai * xi * xi for ai, xi in zip(a, x)) % 8 == 0:
            return True
    return False


fails = 0
rows = []
for a in product([1, 3, 5, 7], repeat=3):
    iso = iso_brute(a)
    mod4 = len({x % 4 for x in a}) > 1
    hs = hilbert2(-a[0] * a[2], -a[1] * a[2]) == 1
    n4 = sum(1 for x in product(range(2), repeat=3) if any(x) and sum(ai * xi for ai, xi in zip(a, x)) % 4 == 0)
    ok1 = (iso == mod4 == hs) and (n4 == (2 if iso else 0))
    C = Cliff([[a[0], 0, 0], [0, a[1], 0], [0, 0, a[2]]])
    B = C.c0_basis()
    assert is_order(C, B)
    d0 = discrd(C, B)
    assert d0 == 4 * a[0] * a[1] * a[2]
    evtr = all(C.trd(b) % 2 == 0 for b in B)
    ovs = two_power_overorders(C, B)
    idx2 = [Bo for i, Bo in ovs if i == 2]
    idx4 = [Bo for i, Bo in ovs if i == 4]
    big = [i for i, Bo in ovs if i > 4]
    ok2 = evtr and len(idx2) == 1 and not big
    if ok2:
        E = idx2[0]
        ok2 &= discrd(C, E) * 2 == d0
        oddtr = any(C.trd(b) % 2 for b in E)
        ok2 &= oddtr  # then Lambda = E^ev (both index 2 in E, Lambda inside E^ev)
        if iso:
            ok2 &= len(idx4) == 2 and all(discrd(C, M) * 4 == d0 for M in idx4)
            # E is contained in both maximal 2-overorders (Eichler = intersection of the two)
            from review_ce_lib import coords
            ok2 &= all(all(x.denominator == 1 for x in coords(M, b)) for M in idx4 for b in E)
        else:
            ok2 &= len(idx4) == 0
    if iso and ok2:
        # Thm 1.2(b): the two maximal 2-overorders are C_0(L+_i), L+_i = L + Z x_i/2, Q(x_i) = 0 mod 4, x_i in {0,1}^3
        from review_ce_lib import hnf_key, lattice_basis_from_gens
        xs = [x for x in product(range(2), repeat=3) if any(x) and sum(ai * xi for ai, xi in zip(a, x)) % 4 == 0]
        keys = set()
        for x in xs:
            half = {}
            for k in range(3):
                for m, c in C.e[k].items():
                    half[m] = half.get(m, 0) + F(x[k], 2) * c
            Lp = [C.e[0], C.e[1], C.e[2], half]
            gens = [C.vec({0: F(1)})] + [C.vec(C.mul(Lp[r], Lp[s])) for r in range(4) for s in range(4)]
            Bp = lattice_basis_from_gens(gens)
            ok2 &= is_order(C, Bp) and discrd(C, Bp) * 4 == d0
            keys.add(hnf_key(Bp))
        ok2 &= keys == {hnf_key(M) for M in idx4} and len(keys) == 2
    rows.append((a, iso, len(idx2), len(idx4)))
    if not (ok1 and ok2):
        fails += 1
        print('FAIL', a, iso, mod4, hs, n4, len(idx2), len(idx4), big)
print('triples', len(rows), 'failures', fails)
print('isotropic', sum(r[1] for r in rows), 'anisotropic', sum(not r[1] for r in rows))
