# Generate input lists for z53_noncrtsmooth_lottery: primes p ≡ 1 (24) ≤ 10^6, test primes, near-squares, samples.
import sys
from sympy import isprime, nextprime
out = sys.argv[1]
L = []
if out.endswith('p24.txt'):
    L = [p for p in range(25, 10**6, 24) if isprime(p)]
elif out.endswith('test.txt'):
    L = [409,577,5569,9601,23929,83449,102001,329617,712321,8813281,193,2521,66529,3361,5101441]
elif out.endswith('nearsq.txt'):
    for m in range(1000, 4000):
        for k in (4, 12, 16, 36, 40, 52, 60, 64, 76, 84, 100):
            n = m*m + k
            if n % 4 == 1 and isprime(n): L.append(n)
    L = L[:600]
elif out.endswith('s1e7.txt'):
    p = 10**7
    while len(L) < 400:
        p = nextprime(p)
        if p % 4 == 1: L.append(p)
open(out, 'w').write('\n'.join(map(str, L)) + '\n')
print(out, len(L))
