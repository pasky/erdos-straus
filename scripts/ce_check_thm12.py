"""Thm 1.2 local check at 2: for every diagonal odd-unimodular <a1,a2,a3> (a_i in {1,3,5,7}), the Z-order
C0(diag) has a unique 2-power overorder of index 2; its discrd is half; C0 = E^{ev}; maximal 2-overorders:
2 if isotropic at 2, 1 (= E itself) if anisotropic."""
from itertools import product
from fractions import Fraction as Fr
from ce_lib import *
from ce_lib import _solve
from cf_lib import ternary_aniso
bad = 0
for a in product((1, 3, 5, 7), repeat=3):
    G = [[a[0], 0, 0], [0, a[1], 0], [0, 0, a[2]]]
    al = Alg(c0_table(G)); B0 = ident_basis(); d0 = discrd(al, B0)
    assert d0 == 4 * a[0] * a[1] * a[2]
    ov = maximal_overorders_2(al, B0)
    idx2 = [B for k, (B, d) in ov.items() if d * 2 == d0]
    tops = [B for k, (B, d) in ov.items() if d % 2 == 1 or d * 4 == d0 and False]
    dmin = min(d for k, (B, d) in ov.items())
    nmin = sum(1 for k, (B, d) in ov.items() if d == dmin)
    iso = not ternary_aniso(list(a), 2)
    ok = len(idx2) == 1
    E = idx2[0]
    # C0 = E^{ev}: all of C0 even trace (automatic), E has odd-trace element
    odd = any(al.trd(e).numerator % 2 == 1 for e in E)
    exp = (dmin * 4 == d0 and nmin == 2) if iso else (dmin * 2 == d0 and nmin == 1)
    if not (ok and odd and exp):
        bad += 1; print('BAD', a, len(idx2), odd, dmin, nmin, iso)
print('64 diagonal classes, bad =', bad)
