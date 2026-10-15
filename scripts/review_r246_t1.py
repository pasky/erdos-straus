# R246: T1 controls. (a) no non-divisor ET class contains an odd square (r not a square mod M);
# (b) exponential class: 151 does not divide n, Legendre (n/151), and squares among 256u^3+105, u = 32 (151).
import json, sys
from math import isqrt
C = json.load(open('data/s6_cert105_et.json'))
for cl in C['classes']:
    M, r = cl['M'], cl['r']
    sq = sorted({(a*a) % M for a in range(M)})
    print(cl['fam'], M, r, "r is a square mod M:", r % M in sq)
nm = (256*32**3 + 105) % 151
print("n mod 151 =", nm, " (n/151) =", pow(nm, 75, 151))
T = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
hits = [t for t in range(T) if isqrt(v := 256*(32 + 151*t)**3 + 105)**2 == v]
print(f"squares 256u^3+105 for u = 32+151t, t < {T}:", hits)
hits2 = [u for u in range(1, 10**6) if isqrt(v := 256*u**3 + 105)**2 == v]
print("all u < 1e6 with 256u^3+105 square:", hits2)
