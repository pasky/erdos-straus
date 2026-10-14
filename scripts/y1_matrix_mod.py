"""y1_matrix_mod (O209): is chi(w) a function of M_w = S_v S_t S_u = [[n,-A*],[A,-t]] mod N (N = 4, 8, 16)?
(Then it is a Gamma(N)-class function and a Gamma(N) trace formula could carry the sign.)  Also: rotation pairs
(conjugate in SL2(Z)) with opposite chi -> chi is not an SL2(Z)-class function."""
from itertools import product
from cf_lib import jacobi
L = 48
for N in (4, 8, 16, 32):
    f, clash = {}, 0
    for t, u, v in product(range(1, L), repeat=3):
        n = t * u * v - u - v
        if n < 3 or n % 2 == 0:
            continue
        A, As = t * u - 1, t * v - 1
        key = (n % N, (-As) % N, A % N, (-t) % N)
        c = jacobi(-A % n, n)
        if c == 0:
            continue
        if f.setdefault(key, c) != c:
            clash += 1
    print('N', N, 'keys', len(f), 'clashes', clash)
ex = []
for t, u, v in product(range(1, 12), repeat=3):
    n, n2 = t * u * v - u - v, u * v * t - v - t
    if n > 1 and n2 > 1 and n % 2 and n2 % 2 and int(n ** .5) ** 2 != n and int(n2 ** .5) ** 2 != n2:
        c1, c2 = jacobi(-(t * u - 1) % n, n), jacobi(-(u * v - 1) % n2, n2)
        if c1 * c2 == -1:
            ex.append(((t, u, v), n, c1, (u, v, t), n2, c2))
print('rotation pairs with opposite chi (non-square n):', len(ex), ex[:3])
