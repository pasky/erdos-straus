# z19_thmW.py — finite part of Theorem W (EXP_OPEN.md §1): constant-gap / constant-ratio ES families through the
# unit-square point mu = 0 of n_s = c0*2^s + k  (c0 odd, 4th-power-free, k = 1 mod 8, c0 + k = 4^J, n irreducible).
# Structure (proved in §1): m = 4c0 w^4 - k (w odd); d1, d2 | N = n x with limits rho_i = d_i(1) = 2^{e_i} a_i,
# e_i = -2*delta_i + 2J*[n in d_i], delta_i in {0, 1/2, 1} (x-degree fraction), delta1 + delta2 <= 1, n in at most one,
# a1 a2 | M = 4^J + m; need m | rho1 + rho2 in Z[1/2].  Magnitude bound B (Lemma 1.4) => only w with m <= B matter.
# Usage: PYTHONPATH=scripts uv run python scripts/z19_thmW.py c0 k
import sys
from fractions import Fraction as Fr
from sympy import divisors, factorint, Poly, symbols, factor_list
c0, k = map(int, sys.argv[1:3])
J = (c0 + k).bit_length() // 2
assert 4 ** J == c0 + k and k % 8 == 1 and c0 % 2 == 1
assert all(v < 4 for v in factorint(c0).values()), 'c0 must be 4th-power-free'
Y = symbols('Y')
for D in (1, 2, 3, 4, 5, 6, 8, 12):   # sanity: n irreducible (Capelli says for all D; spot check)
    assert len(factor_list(c0 * Y ** D + k)[1]) == 1
emax = 2 * J + 2                       # |e1 - e2| <= 2J + 2
def bound(m):
    M = 4 ** J + m; r = Fr(M, m)
    return max(2 ** emax * 4 ** J + 2 ** (2 * emax + 2) * r * r, 2 ** emax * 4 * r * r + 4 ** J)
combos = []
for d1 in (0, 1, 2):                   # 2*delta
    for d2 in (0, 1, 2):
        if d1 + d2 > 2: continue
        for npl in (0, 1, 2):          # n in d1 / d2 / neither
            combos.append((-d1 + (2 * J if npl == 1 else 0), -d2 + (2 * J if npl == 2 else 0), d1 % 2 + d2 % 2))
w = 1; hits = []; checked = []
while True:
    m = 4 * c0 * w ** 4 - k
    if m > bound(m): break
    checked.append((w, m)); M = 4 ** J + m; ds = divisors(M)
    for a1 in ds:
        for a2 in ds:
            if (M // a1) % a2: continue
            for e1, e2, odd in combos:
                lo = min(e1, e2)
                if (a1 * 2 ** (e1 - lo) + a2 * 2 ** (e2 - lo)) % m == 0:
                    hits.append((w, m, e1, a1, e2, a2))
    w += 2
print('c0=%d k=%d J=%d: SG windows m=4c0w^4-k checked for w in %s (bound reached at w=%d, B(m)=%d)'
      % (c0, k, J, [c[0] for c in checked], w, int(bound(4 * c0 * w ** 4 - k))))
print('limit-level relations: %d' % len(hits))
for h in hits[:20]: print('  w=%d m=%d  rho1=2^%d*%d  rho2=2^%d*%d' % h)
