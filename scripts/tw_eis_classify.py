"""O182: classify TES(pi) solvability (window B) by cubic characters of omega, 2 (and lambda) mod pi.
usage: tw_eis_classify.py B maxnorm"""
import sys
from collections import Counter, defaultdict
import tw_eis as E, tw_eis_solve as S
B, maxnorm = int(sys.argv[1]), int(sys.argv[2])
t = (9, 0); cs = [(0, 1), (-1, -1), (2, 0)]


def isprime(p): return p > 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))


tab = defaultdict(Counter)
for p in range(13, maxnorm + 1):
    if not (isprime(p) and p % 3 == 1):
        continue
    for pi0 in E.split_prime(p):
        pi = [E.mul(u, pi0) for u in E.UNITS if (E.mul(u, pi0)[0] % 2, E.mul(u, pi0)[1] % 2) == (1, 0)][0]
        key = (E.cubic_class(E.W, pi), E.cubic_class((2, 0), pi), E.cubic_class(E.LAM, pi))
        sols, st = S.run(t, cs, pi, 1, B, verbose=False)
        n12 = sum(v for k, v in st.items() if k[0] in ('I', 'II'))
        tab[key]['solved' if n12 else 'none'] += 1
        if not n12 and p > 100:
            tab[key]['none>100'] += 1
for k in sorted(tab):
    print('(chi(w), chi(2), chi(lam)) =', k, dict(tab[k]))
