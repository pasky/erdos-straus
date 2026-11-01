"""z52d pass2 fix, TO0b Z0209: local densities of the ES surface X_n: 4xyz = n(xy+yz+zx) (affine, x,y,z nonzero mod l^k).
rho_l(k) = #{(x,y,z) mod l^k : 4xyz == n(xy+yz+zx) mod l^k} / l^(2k)  (the local factor of a Peyre-type singular
series for the family; the count is over a fixed n, so only the local factors are computed).  Also the global count of ES
solutions for n (finite) is listed for comparison, showing the fixed-n count is finite and not governed by these factors."""
import itertools, math
from fractions import Fraction as Fr
def rho(n, l, k):
    m = l ** k
    cnt = 0
    units_or_all = [v for v in range(m) if v % l != 0]  # nonzero mod l (units) ; include non-units separately
    # use all nonzero residues mod m (not only units) to keep the affine surface
    nz = list(range(m))  # all residues (x,y,z in Z_l are allowed to be divisible by l; zero is a measure-zero condition)
    for x in nz:
        for y in nz:
            for z in nz:
                if (4 * x * y * z - n * (x * y + y * z + z * x)) % m == 0:
                    cnt += 1
    return Fr(cnt, m * m)
def es_count(n):
    res = 0
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        r = Fr(4, n) - Fr(1, x)
        if r <= 0: continue
        for y in range(max(x, math.floor(1 / r) + 1), math.floor(2 / r) + 1):
            s_ = r - Fr(1, y)
            if s_ > 0 and s_.numerator == 1 and s_.denominator >= y: res += 1
    return res
out = []
for n in (5, 13, 17):
    row = []
    for l, k in ((2, 1), (2, 2), (3, 1), (3, 2), (5, 1)):
        row.append(f'rho_{l}({k})={rho(n, l, k)}')
    out.append(f'Z0209 n={n}: ' + ', '.join(row) + f'; ES solutions (x<=y<=z) = {es_count(n)}')
print('\n'.join(out))
open('data/z52b/pass2/TO0b/fix_Z0209.txt', 'w').write('\n'.join(out) + '\n')
