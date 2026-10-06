"""Which classes (all seven families, modulus M <= Mmax) contain a given profinite point?
The point: x_q = value mod q^k for listed q (given as q:value:k with value a q-adic integer
known mod q^k), x_q = 1 for all other q.  A class mod M is decided by the point iff
v_q(M) <= k for listed q.  usage: mordell_point.py Mmax q:val:k ... [--step s]"""
import sys
from mordell_lib import classes_for_modulus, cls_modulus_residues, factor_small
Mmax = int(sys.argv[1])
spec = {}
step = 1
for a in sys.argv[2:]:
    if a.startswith('--step='):
        step = int(a.split('=')[1]); continue
    q, v, k = map(int, a.split(':'))
    spec[q] = (v, k)
def point_mod(M):
    """x mod M, or None if undecided"""
    x, m = 0, 1
    for q, e in factor_small(M).items():
        qe = q ** e
        if q in spec:
            v, k = spec[q]
            if e > k:
                return None
            t = v % qe
        else:
            t = 1 % qe
        x = (x + m * (((t - x) * pow(m, -1, qe)) % qe)) % (m * qe)
        m *= qe
    return x
hits = []
for M in range(step, Mmax + 1, step):
    if M < 3:
        continue
    xm = point_mod(M)
    if xm is None:
        continue
    for fam, P in classes_for_modulus(M):
        _, R = cls_modulus_residues(fam, P)
        if xm in R:
            hits.append((M, fam, P))
            print("HIT", M, fam, P, flush=True)
            break
print("total moduli with a hit:", len(hits))
