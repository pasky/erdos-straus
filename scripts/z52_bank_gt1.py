"""GT1 check (z52 bank §1(b)). For n = 1 (4), non-square, n <= LIM:
 t_G(n) = least t = 0 (4) at which n is NOT genus-obstructed, i.e. no odd real character psi mod t is +1 on every prime
 factor of tn+1 coprime to t.  Linear algebra over F_2: with v(s) = values of a basis of real characters mod t at s,
 'not obstructed' <=> v(-1) lies in the F_2-span of {v(s) : s | tn+1 prime, s coprime to t}.
 Also verifies the planted construction t = 4r (a = 3 (4) prime with (n/a) = -1, r = 1 (4) prime, 4rn = -1 mod a)."""
import sys
from sympy import factorint, primerange, isprime, jacobi_symbol
from math import isqrt
def real_char_basis(t):
    """basis of the group of real characters mod t, as functions s -> 0/1 (exponent of -1)"""
    B = []
    e2 = (t & -t).bit_length() - 1
    if e2 >= 2: B.append(lambda s: ((s % 4) == 3) * 1)            # chi_{-4}
    if e2 >= 3: B.append(lambda s: (s % 8 in (3, 5)) * 1)        # chi_8
    for l in factorint(t):
        if l > 2: B.append(lambda s, l=l: (jacobi_symbol(s % l, l) == -1) * 1)
    return B
def obstructed(n, t):
    B = real_char_basis(t)
    vec = lambda s: sum(f(s) << i for i, f in enumerate(B))
    target = vec(t - 1)
    basis = []                       # xor basis
    def reduce(v):
        for b in basis: v = min(v, v ^ b)
        return v
    for s in factorint(t * n + 1):
        if t % s == 0: continue
        v = reduce(vec(s))
        if v: basis.append(v); basis.sort(reverse=True)
    return reduce(target) != 0
LIM = int(sys.argv[1])
worst = (0, 0); worst_c = (0, 0); hist = {}
for n in range(5, LIM + 1, 4):
    if isqrt(n) ** 2 == n: 
        assert all(obstructed(n, t) for t in range(4, 41, 4)), n   # T1 sanity on squares
        continue
    t = 4
    while obstructed(n, t): t += 4
    hist[t] = hist.get(t, 0) + 1
    if t > worst[0]: worst = (t, n)
    a = next(a for a in primerange(3, 10**6) if a % 4 == 3 and jacobi_symbol(n, a) == -1)
    r = next(r for r in primerange(5, 10**7) if r % 4 == 1 and (4 * r * n + 1) % a == 0)
    assert not obstructed(n, 4 * r), (n, a, r)
    if 4 * r > worst_c[0]: worst_c = (4 * r, n)
print('non-squares n=1(4) <=', LIM, ': max t_G =', worst, '; histogram', dict(sorted(hist.items())))
print('planted level 4r always genus-free; max planted level (least a, least r):', worst_c)
