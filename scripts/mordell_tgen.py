"""T-generic boxes: points with x_q = 1 for all primes q not in T.  A class (modulus
M = M_T * N, (N, T)=1) meets these points iff its residues are = 1 mod N; it then defines
a box (residue mod M_T) in prod_{q in T} Z_q.  Brute force over all M <= Mmax.
Reports coverage of the target region (x_r non-square, plus optional square condition
at other q in T) at resolution prod q^k.
usage: mordell_tgen.py Mmax r k T(comma) [np]"""
import sys, itertools, time
from math import gcd, prod
from mordell_lib import classes_for_modulus, cls_modulus_residues, factor_small
Mmax = int(sys.argv[1]); r = int(sys.argv[2]); k = int(sys.argv[3])
T = [int(t) for t in sys.argv[4].split(',')]
npv = len(sys.argv) > 5 and sys.argv[5] == 'np'
CDEF = (1, 1)   # default value c = num/den at primes outside T
for a in sys.argv[6:]:
    if a.startswith('c='):
        v = a[2:]
        CDEF = tuple(map(int, v.split('/'))) if '/' in v else (int(v), 1)
KQ = {q: (k + 3 if q == 2 else k) for q in T}
R = prod(q ** KQ[q] for q in T)
boxes = {}   # (MT, res) -> witness
t0 = time.time()
for M in range(3, Mmax + 1):
    MT = 1
    for q in T:
        while M % (MT * q) == 0 and (M // MT) % q == 0:
            MT *= q
    N = M // MT
    if any(M % (q ** (KQ[q] + 1)) == 0 for q in T):
        continue
    for fam, P in classes_for_modulus(M):
        _, Rs = cls_modulus_residues(fam, P)
        for res in Rs:
            if N == 1 or res % N == (CDEF[0] * pow(CDEF[1], -1, N)) % N:
                key = (MT, res % MT)
                if key not in boxes:
                    boxes[key] = (M, fam, P)
print(f"boxes: {len(boxes)}  ({time.time()-t0:.0f}s)")
def issq(v, q):
    return pow(v % q, (q - 1) // 2, q) == 1
targets = []
for v in range(R):
    ok = True
    for q in T:
        if v % q == 0: ok = False; break
        if q == 2:
            if v % 8 != 1: ok = False; break
            continue
        if q == 3:
            if v % 3 != 1: ok = False; break
            continue
        if q in (5, 7) and not issq(v, q): ok = False; break
        if q == r and issq(v, q): ok = False; break
        if q != r and npv and q < r and q > 3 and not issq(v, q): ok = False; break
    if ok:
        targets.append(v)
unc = [v for v in targets if not any(v % MT == res for (MT, res) in boxes)]
print(f"targets mod {R}: {len(targets)}, uncovered {len(unc)} ({len(unc)/len(targets):.4f})")
from collections import Counter
print(Counter(tuple(v % q for q in T) for v in unc))
print("uncovered cells:", sorted(tuple(v % q ** KQ[q] for q in T) for v in unc)[:200])
import pickle
pickle.dump(boxes, open(f"/tmp/o80_boxes_{Mmax}_{sys.argv[4]}_{k}.pkl", "wb"))
for key, w in sorted(boxes.items())[:0]:
    print(key, w)
