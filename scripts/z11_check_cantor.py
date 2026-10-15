# z11_check_cantor.py — independent check of Result 1.1: the binary label Cantor set C = prod_l {4, -2} of n_s = 4^s + 105
# is covered by the 10 listed classes.  For each class: the period support T = supp(lcm ord_{q^e}(4)) is recomputed; for
# every pattern on T the value n mod M is computed by CRT (2-part: 105 mod 2^a, valid for s >= a/2); the class residue
# set is recomputed from the ET parametrisation (mordell_lib.cls_modulus_residues) and, for each covered residue, an
# explicit ES solution of a large representative n = r (mod M) is produced and verified with exact fractions.
# Then all 2^|S| patterns over S = union of supports are checked to be covered.
import itertools
from fractions import Fraction as F
from math import lcm
from sympy import n_order, factorint
from sympy.ntheory.modular import crt
import mordell_lib as ML

K = 105
LAB = {0: 4, 1: -2}
CL = [(19, ('D', (19,))), (919, ('II2', (2, 23, 919))), (41, ('D', (41,))), (191, ('D', (191,))),
      (35288, ('II1', (11, 802, 271))), (419, ('II2', (3, 5, 419))), (1787, ('II2', (1, 447, 1787))),
      (27551, ('II2', (287, 12, 27551))), (32008, ('II1', (1, 8002, 151))), (213384, ('II1', (6, 8891, 1271)))]


def es_ok(n, sol):
    return sol is not None and min(sol) > 0 and F(4, n) == sum(F(1, v) for v in sol)


info = []
for M, (fam, P) in CL:
    fa = factorint(M)
    a = fa.get(2, 0)
    ords = {q ** e: n_order(4, q ** e) for q, e in fa.items() if q != 2}
    T = sorted(set().union(*[set(factorint(o)) for o in ords.values()]))
    if fam == 'D':
        R = {0}
    else:
        MM, R = ML.cls_modulus_residues(fam, P)
        assert MM == M
        R = set(R)
        for r in R:  # explicit solution at a large member of the class
            n = r + M * 10 ** 6
            assert es_ok(n, ML.solve(fam, P, n)), (M, r)
    good = set()
    for bits in itertools.product((0, 1), repeat=len(T)):
        pat = dict(zip(T, bits))
        ms, rs = ([2 ** a], [K % 2 ** a]) if a else ([], [])
        for Q, o in ords.items():
            f = factorint(o)
            mu = int(crt([l ** e for l, e in f.items()], [LAB[pat[l]] % l ** e for l, e in f.items()])[0]) if f else 0
            ms.append(Q); rs.append((pow(4, mu, Q) + K) % Q)
        if int(crt(ms, rs)[0]) in R: good.add(bits)
    info.append((T, good))
    print('M=%d %s %s support %s covers %d/%d patterns' % (M, fam, P, T, len(good), 2 ** len(T)))
S = sorted(set().union(*[set(T) for T, _ in info]))
unc = 0
for bits in itertools.product((0, 1), repeat=len(S)):
    pat = dict(zip(S, bits))
    if not any(tuple(pat[l] for l in T) in good for T, good in info): unc += 1
print('S =', S, 'patterns', 2 ** len(S), 'uncovered', unc)
assert unc == 0
# D classes: q prime, n = 0 mod q gives ES(n) from ES(q) by scaling; check ES(q) has a solution
for q in (19, 41, 191):
    assert any((q * x * y) % (4 * x * y - q * (x + y)) == 0 for x in range(1, q) for y in range(x, 4 * q * q)
               if 4 * x * y - q * (x + y) > 0)
print('CHECKED: the binary Cantor set prod_l {4,-2} of 4^s + 105 lies in the union of the 10 classes')
