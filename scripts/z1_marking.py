"""z1 (O224): for which M is five-slice membership S_M a function of the isometry class of L_w?
Scan all odd n in [N0,N1) (all words incl. boundary); report mixed classes per M."""
import sys
from cf_lib import words
from ce_classes import canon

def penta(w):
    t, u, v = w
    return (t, u, v, t*u-1, t*v-1)

N0, N1 = int(sys.argv[1]), int(sys.argv[2])
Ms = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16]
mixed = {M: 0 for M in Ms}; ex = {}; mixed_int = {M: 0 for M in Ms}
ncls = 0
for n in range(N0, N1, 2):
    cls = {}
    for w in words(n):
        t, u, v = w
        cls.setdefault(canon([[v, -1, 0], [-1, t, -1], [0, -1, u]]), []).append(w)
    for k, ws in cls.items():
        ncls += 1
        for M in Ms:
            s = {any(x % M == 0 for x in penta(w)) for w in ws}
            if len(s) > 1:
                mixed[M] += 1
                ex.setdefault(M, (n, ws))
                # interior-only check
                wi = [w for w in ws if min(w) >= 2]
                if len({any(x % M == 0 for x in penta(w)) for w in wi}) > 1:
                    mixed_int[M] += 1
print('odd n in [%d,%d): path classes %d' % (N0, N1, ncls))
for M in Ms:
    print('M=%d mixed classes %d (mixed among interior words %d) first %s' % (M, mixed[M], mixed_int[M], ex.get(M)))
