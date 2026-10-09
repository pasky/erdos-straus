"""m13e_parity_check.py — empirical check of 13E Lemma 2.1: for every engine box (fam, M_T, r) meeting the cell
x = (2,2) mod (11,13) (r = 2 mod q for each q | M_T), the ES level N(P) of its datum has v_T(N) odd, except
I3 where v_T(N) = v_T(f_T) + 1 mod 2.  usage: m13e_parity_check.py rundir"""
import glob, pickle, sys
from m13b_invert import tpart

def vT(m):
    k = 0
    for q in (11, 13):
        while m % q == 0:
            m //= q; k += 1
    return k

def es_level(fam, P):
    if fam in ('II1', 'I4'):
        a, b, e = P; return tpart(a * b)
    if fam == 'II2':
        a, d, f = P; return tpart(f)
    if fam == 'I2':
        a, c, f = P; return tpart(a * c) * tpart(f)
    a, d, e = P                      # II3 (a,d,e), I3 (c,d,f), I1 (a,d,f): N = B * a_T^2 * d_T
    B = 1 if fam == 'I1' else tpart(e)
    return B * tpart(a) ** 2 * tpart(d)

n = bad = 0
for fn in glob.glob(sys.argv[1] + '/inv_*.pkl'):
    for (fam, MT, r), P in pickle.load(open(fn, 'rb'))['boxes'].items():
        if MT == 1 or any(MT % q == 0 and r % q != 2 for q in (11, 13)):
            continue
        n += 1
        N = es_level(fam, P)
        want = (vT(tpart(P[2])) + 1) % 2 if fam == 'I3' else 1
        if vT(N) % 2 != want:
            bad += 1; print('VIOLATION', fam, P, MT, r, N)
print(f'boxes in the (2,2) cell: {n}; parity violations: {bad}')
