"""O257 Thm 2.6 check: hits of the single-prime point x_{l,2} (x=2 in Z_l, x=1 elsewhere) by witness classes,
slices a<=b<=B, for 4|k and odd primes l not dividing k.  Expected: hits only for k=4, l in {3,5}."""
import sys
sys.path.insert(0, 'scripts')
from z28_adelic_fast import run
from sympy import primerange
B = int(sys.argv[1])
for k in [4, 8, 12, 16, 20, 24, 28, 32]:
    for l in primerange(3, 60):
        if k % l == 0: continue
        h = run(k, {l: 2}, B)
        if h: print(f"k={k} l={l}: {h}")
print("done B =", B)
