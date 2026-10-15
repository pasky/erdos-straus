# z14_sg1mu0.py — Prop 2.7 finite part: for c0 + k = 4^J, k = 1 (mod 8), the only windows that can reach the unit-square
# point mu = 0 are 'sg1', j = 1, w odd (m = 4 c0 w^4 - k).  At mu = 0: pieces -> odd primes p of c0 (exp in {-1,0,1}),
# n -> 4^J, A± -> (2w^2 ± 2w + 1)/2; Jacobi forces exactly one A-atom.  Relation -1 = A^{±1} 4^{Jc} prod p^{eps} (mod m).
# For w with 4^J c0 (2w^2+2w+3) < m every candidate |d1 + d2| < m, so only finitely many w need checking.
# Usage: PYTHONPATH=scripts uv run python scripts/z14_sg1mu0.py c0 k
import sys
from itertools import product
from sympy import factorint
c0, k = map(int, sys.argv[1:3])
J = (c0 + k).bit_length() // 2
assert 4 ** J == c0 + k and k % 8 == 1 and c0 % 2
ps = [p for p, v in factorint(c0).items() for _ in range(v)]
w = 1; fired = []
while True:
    m = 4 * c0 * w ** 4 - k
    if 4 ** J * c0 * (2 * w * w + 2 * w + 3) < m: break
    for sgn in (1, -1):
        A = (2 * w * w + sgn * 2 * w + 1) * pow(2, -1, m) % m
        for eA in (1, -1):
            for cn in (-1, 0, 1):
                for eps in product((-1, 0, 1), repeat=len(ps)):
                    v = pow(A, eA, m) * pow(4 ** J, cn, m) % m
                    for p, e in zip(ps, eps): v = v * pow(p, e, m) % m
                    if v == m - 1: fired.append((w, sgn, eA, cn, eps))
    w += 2
print('c0=%d k=%d J=%d: odd w checked up to %d (bound), relations at mu=0: %s' % (c0, k, J, w - 2, fired[:5] or 'none'))
