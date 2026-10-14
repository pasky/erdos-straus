"""R213: independent (W_n-side) search for p = 379: all (a, B, c), c, B odd squarefree coprime, 4 | a,
gcd(caB, 379) = 1, g = caB - 1 <= GMAX, with g | 4*379*a^2 + B^2. Prints all hits."""
import sys
from math import gcd
p = 379; GMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
LIM = GMAX + 2
sqf = bytearray([1]) * LIM
for i in range(2, int(LIM**0.5) + 1):
    sqf[i*i::i*i] = bytearray(len(range(i*i, LIM, i*i)))
hits = []
for c in range(1, LIM, 2):
    if not sqf[c] or c % p == 0: continue
    for B in range(1, LIM//(4*c) + 1, 2):
        if not sqf[B] or gcd(c, B) > 1 or B % p == 0: continue
        cB = c*B
        for a in range(4, (GMAX + 1)//cB + 1, 4):
            if a % p == 0: continue
            g = cB*a - 1
            if (4*p*a*a + B*B) % g == 0:
                hits.append((g, a, B, c, (4*p*a*a + B*B)//g))
hits.sort(); print(hits)
