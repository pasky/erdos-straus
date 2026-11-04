# Zeros of R(n) among n ≡ 1 (mod 4), split into primes / odd squares / other composites.
import sys, math
from sympy import isprime
rows = [tuple(map(int, l.split())) for l in open(sys.argv[1])]
zp, zs, zc = [], [], []
for n, R in rows:
    if R: continue
    r = math.isqrt(n)
    if r * r == n: zs.append(n)
    elif isprime(n): zp.append(n)
    else: zc.append(n)
print("range n<=", rows[-1][0], "count n:", len(rows))
print("prime zeros:", len(zp), zp)
print("square zeros:", len(zs), "(odd squares ≡1 mod 4 in range:", sum(1 for k in range(1, math.isqrt(rows[-1][0]) + 1, 2) if k*k >= 5), ")")
print("non-square composite zeros:", len(zc), "largest 30:", zc[-30:])
import collections
dec = collections.Counter(int(math.log10(n)) for n in zc)
print("by decade:", sorted(dec.items()))
from sympy import factorint
for n in zc[-15:]:
    print(n, factorint(n))
