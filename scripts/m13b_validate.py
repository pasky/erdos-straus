"""Completeness check of the m13b engine against the brute-force T-generic boxes of mordell_tgen
(all seven families, all moduli M<=1e6, v_q(M)<=3; pickle {(MT,res): (M,fam,P)}).
For each witness compute its ES level N (Lemmas 2.1-2.4); if N<=NMAX, its (fam,MT,res) must be in the
engine output inv_N.pkl.  usage: m13b_validate.py brute.pkl rundir NMAX"""
import glob, pickle, sys
from m13b_invert import tpart, boxes_of
brute = pickle.load(open(sys.argv[1], 'rb'))
NMAX = int(sys.argv[3])
eng = {}
for fn in glob.glob(sys.argv[2] + '/inv_*.pkl'):
    d = pickle.load(open(fn, 'rb'))
    eng[d['N']] = set(d['boxes'])
def level(fam, P):
    if fam in ('II1', 'I4'):
        return tpart(P[0] * P[1])
    if fam == 'II2':
        return tpart(P[2])
    if fam in ('II3', 'I3', 'I1'):
        a, d, e = P
        return tpart(e) * tpart(a) ** 2 * tpart(d)
    if fam == 'I2':
        return tpart(P[0] * P[1]) * tpart(P[2])
tested = missing = skipped = 0
for (MT, res), (M, fam, P) in brute.items():
    N = level(fam, P)
    if N > NMAX or N not in eng:
        skipped += 1
        continue
    assert (MT, res) in boxes_of(fam, P)
    tested += 1
    if (fam, MT, res) not in eng[N]:
        missing += 1
        print('MISSING', fam, P, MT, res, 'N=', N)
print(f'tested {tested}, missing {missing}, skipped (N>{NMAX}) {skipped}')
