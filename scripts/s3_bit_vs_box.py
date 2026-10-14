"""O208 memo s3_across_n_slicing: does the ES^box 'bit' (p/g) = -1 (i.e. -p/4 a square mod g) raise the chance that
-p lies in Box((g+1)/4) mod g (an ES certificate at modulus g)?  Primes p = 1 (4) < PMAX, primes g = 3 (4) < GMAX.
Also checks the identity 4tj-1 | nj+t  <=>  4tj-1 | n+4t^2 used in memo s3_eps_mu_sieve."""
import sys
from sympy import primerange, divisors, jacobi_symbol
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
GMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
G = [g for g in primerange(3, GMAX) if g % 4 == 3]
box = {}
for g in G:
    k = (g + 1) // 4
    box[g] = sorted({(4 * c * c * d) % g for c in divisors(k) for d in divisors(k // c)})
cnt = {1: [0, 0], -1: [0, 0], 0: [0, 0]}
for p in primerange(5, PMAX):
    if p % 4 != 1:
        continue
    for g in G:
        if g == p:
            continue
        b = jacobi_symbol(p, g)
        hit = ((-p) % g) in set(box[g])
        cnt[b][0] += 1
        cnt[b][1] += hit
for b in (-1, 1):
    n, h = cnt[b]
    print('(p/g) = %+d : pairs %d, box hits %d, rate %.5f' % (b, n, h, h / n))
bad = 0
for n in range(3, 400, 2):
    for t in range(1, 40):
        for j in range(1, 40):
            m = 4 * t * j - 1
            bad += (((n * j + t) % m == 0) != ((n + 4 * t * t) % m == 0))
print('identity check 4tj-1 | nj+t <=> 4tj-1 | n+4t^2: mismatches', bad)
