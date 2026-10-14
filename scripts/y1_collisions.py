"""y1_collisions (O209): GZ x=4 'collisions' J(-4A,-4A*) with AA* = tp+1 and (-A/p) = -1 WITHOUT the level-t condition
A = A* = -1 (mod t): least such t per prime (existence is trivial), vs words (with the condition)."""
import sys
from sympy import primerange, divisors
from cf_lib import jacobi
X = int(sys.argv[1])
worst, cnt = 0, 0
for p in primerange(5, X):
    if p % 24 != 1:
        continue
    cnt += 1
    for t in range(1, 50):
        if any(jacobi(-A % p, p) == -1 for A in divisors(t * p + 1)):
            worst = max(worst, t)
            break
    else:
        print('none t<50', p)
print('primes p=1(24) <', X, ':', cnt, ' max over p of least t with an x=4 collision (no level condition):', worst)
